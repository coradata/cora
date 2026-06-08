"""Tests for the semantic-clustering pass and the scaffold subcommand.

The embeddings module is designed so unit tests inject a stub encoder
(``BagOfWordsEncoder``) instead of pulling in sentence-transformers. The
stub produces deterministic, L2-normalized bag-of-words vectors so cosine
similarity tracks token overlap — exactly the kind of "definition
overlap" the real model captures, but reproducible across runs without
a 250 MB ML dependency.
"""

from __future__ import annotations

import math
import textwrap
from collections.abc import Sequence
from datetime import date
from pathlib import Path

import pytest

from cora_extractors.cli import main
from cora_extractors.concepts import (
    CensusRow,
    EmbeddingEncoder,
    scaffold_crosswalk,
    suggest_semantic_clusters,
    write_scaffold,
    write_semantic_suggestions,
)
from cora_extractors.concepts.report import SUGGESTIONS_SEMANTIC_MD


class BagOfWordsEncoder:
    """Deterministic test encoder. L2-normalized bag-of-words vectors.

    Cosine similarity between two inputs equals the cosine of their token
    overlap — high when definitions share words, zero when disjoint. Good
    enough to test the semantic suggester without sentence-transformers.
    """

    def encode(self, texts: Sequence[str]) -> list[list[float]]:
        vocab = sorted({tok for t in texts for tok in t.lower().split()})
        idx = {tok: i for i, tok in enumerate(vocab)}
        out: list[list[float]] = []
        for text in texts:
            vec = [0.0] * len(vocab)
            for tok in text.lower().split():
                vec[idx[tok]] += 1.0
            norm = math.sqrt(sum(x * x for x in vec))
            if norm > 0.0:
                vec = [x / norm for x in vec]
            out.append(vec)
        return out


def _encoder_satisfies_protocol() -> EmbeddingEncoder:
    """Compile-time check: BagOfWordsEncoder satisfies the protocol."""
    return BagOfWordsEncoder()


# ---- semantic suggester -----------------------------------------------------


def _row(
    standard: str,
    module: str,
    type_name: str,
    leaf: str,
    definition: str,
) -> CensusRow:
    return CensusRow(
        standard=standard,
        module=module,
        type_name=type_name,
        path=f"{type_name}/{leaf}" if type_name else leaf,
        leaf_name=leaf,
        range="string",
        cardinality="optional",
        definition=definition,
    )


def test_semantic_cluster_finds_token_overlap_across_standards() -> None:
    rows = [
        _row("mits", "lease", "Lease", "LeaseStartDate", "the date the lease starts"),
        _row("ibpdi", "pm", "RentalContract", "MoveInDate", "the date the lease starts"),
    ]
    clusters = suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    )
    assert len(clusters) == 1
    c = clusters[0]
    assert c.canonical_key in ("lease_start_date", "move_in_date")
    assert c.standards == ("ibpdi", "mits")
    # Leaf names differ, definitions identical → BoW cosine < 1.0 but high.
    assert c.avg_cosine > 0.8


def test_semantic_skips_clusters_already_in_string_match_pool() -> None:
    # If the bare-string bucketer already groups two rows under the same
    # normalized leaf name (`postal_code`), the semantic pass should not
    # surface the same cluster again — string-match owns it.
    rows = [
        _row("mits", "addr", "AddressType", "PostalCode", "postal code"),
        _row("ibpdi", "core", "Address", "PostalCode", "postal code"),
    ]
    clusters = suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    )
    assert clusters == []


def test_semantic_respects_threshold() -> None:
    # Cosine 0.0 (disjoint definitions) shouldn't cluster.
    rows = [
        _row("mits", "lease", "Lease", "Foo", "absolutely nothing in common"),
        _row("ibpdi", "pm", "Contract", "Bar", "completely different words"),
    ]
    # At threshold 0.5 these are far apart.
    assert suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    ) == []


def test_semantic_skips_within_standard_pairs() -> None:
    # Two rows in the same standard sharing tokens shouldn't form a
    # cross-standard cluster.
    rows = [
        _row("mits", "a", "X", "FooDate", "the start date"),
        _row("mits", "b", "Y", "BarDate", "the start date"),
    ]
    assert suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    ) == []


def test_semantic_report_writer_is_deterministic(tmp_path: Path) -> None:
    rows = [
        _row("mits", "lease", "Lease", "LeaseStartDate", "the date the lease starts"),
        _row("ibpdi", "pm", "RentalContract", "MoveInDate", "the date the lease starts"),
    ]
    clusters = suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    )
    a = tmp_path / "a"
    b = tmp_path / "b"
    write_semantic_suggestions(clusters, a, model_name="stub", threshold=0.5)
    write_semantic_suggestions(clusters, b, model_name="stub", threshold=0.5)
    assert (a / SUGGESTIONS_SEMANTIC_MD).read_bytes() == (b / SUGGESTIONS_SEMANTIC_MD).read_bytes()


# ---- scaffold ---------------------------------------------------------------


def test_scaffold_emits_yaml_with_todos() -> None:
    rows = [
        _row("mits", "lease", "Lease", "LeaseStartDate", "lease start"),
        _row("ibpdi", "pm", "RentalContract", "RentStartDate", "rent start"),
    ]
    yaml_text = scaffold_crosswalk(
        "lease_start_date",
        rows,
        standards_present=("ibpdi", "mits"),
        all_standards=("ibpdi", "mits", "redi"),
        today=date(2026, 6, 7),
    )
    assert "concept: lease_start_date" in yaml_text
    # All editorial fields are marked TODO.
    assert "TODO" in yaml_text
    # Present standards get a path; missing ones get not_present.
    assert "field: Lease/LeaseStartDate" in yaml_text
    assert "field: RentalContract/RentStartDate" in yaml_text
    assert "field: null" in yaml_text  # redi
    assert "not_present" in yaml_text
    assert "last_reviewed: '2026-06-07'" in yaml_text


def test_scaffold_picks_longest_definition_when_standard_has_multiple_paths() -> None:
    rows = [
        _row("mits", "a", "X", "Foo", ""),
        _row("mits", "b", "Y", "Foo", "a longer definition explaining the field"),
        _row("ibpdi", "c", "Z", "Foo", "ibpdi side"),
    ]
    yaml_text = scaffold_crosswalk(
        "foo",
        rows,
        standards_present=("ibpdi", "mits"),
        all_standards=("ibpdi", "mits"),
        today=date(2026, 6, 7),
    )
    # The canonical pick for MITS is module 'b' (longer definition).
    assert "field: Y/Foo" in yaml_text
    # And the alternate path is mentioned in the notes.
    assert "X/Foo" in yaml_text or "a:X/Foo" in yaml_text


def test_scaffold_refuses_to_overwrite(tmp_path: Path) -> None:
    target = tmp_path / "crosswalks" / "concepts" / "lease_start_date.yaml"
    target.parent.mkdir(parents=True)
    target.write_text("existing content")
    with pytest.raises(FileExistsError):
        write_scaffold(
            "lease_start_date",
            [_row("mits", "a", "X", "Foo", "")],
            standards_present=("mits",),
            all_standards=("mits",),
            repo_root=tmp_path,
        )


# ---- CLI integration --------------------------------------------------------


def _write_inventory(repo: Path, standard: str, module: str, fields: list[dict[str, str]]) -> None:
    inv_dir = repo / "standards" / standard / "current" / "inventory"
    inv_dir.mkdir(parents=True, exist_ok=True)
    fields_block = "fields:\n" + "\n".join(
        textwrap.dedent(
            f"""\
            - path: {f['path']}
              domain: {f.get('domain', '')}
              range: string
              cardinality: required
              definition: "{f.get('definition', '')}"
            """
        ).rstrip()
        for f in fields
    ) + "\n"
    (inv_dir / f"{module}.yaml").write_text(
        textwrap.dedent(
            f"""\
            standard: {standard}
            module: {module}
            version: '1.0'
            source_artifact: standards/{standard}/native/x
            extractor: cora_extractors.xsd@0.0.0
            extracted_at: '2026-06-01T00:00:00Z'
            source_label: xsd
            types: []
            """
        )
        + fields_block
    )


def test_cli_scaffold_by_cluster(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addr",
        [
            {
                "path": "AddressType/PostalCode",
                "domain": "AddressType",
                "definition": "Postal",
            }
        ],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal"}],
    )
    rc = main(
        [
            "concepts",
            "scaffold",
            "postal_code",
            "--repo-root",
            str(tmp_path),
            "--cluster",
            "postal_code",
        ]
    )
    assert rc == 0
    out = tmp_path / "crosswalks" / "concepts" / "postal_code.yaml"
    assert out.exists()
    text = out.read_text()
    assert "field: AddressType/PostalCode" in text
    assert "field: Address/PostalCode" in text


def test_cli_scaffold_by_field(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "lease",
        [{"path": "Lease/LeaseStartDate", "domain": "Lease", "definition": ""}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "pm",
        [
            {
                "path": "RentalContract/MoveInDate",
                "domain": "RentalContract",
                "definition": "",
            }
        ],
    )
    rc = main(
        [
            "concepts",
            "scaffold",
            "lease_start_date",
            "--repo-root",
            str(tmp_path),
            "--field",
            "mits=Lease/LeaseStartDate",
            "--field",
            "ibpdi=RentalContract/MoveInDate",
        ]
    )
    assert rc == 0
    out = tmp_path / "crosswalks" / "concepts" / "lease_start_date.yaml"
    text = out.read_text()
    assert "field: Lease/LeaseStartDate" in text
    assert "field: RentalContract/MoveInDate" in text


def test_cli_scaffold_field_typo_reports_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addr",
        [
            {
                "path": "AddressType/PostalCode",
                "domain": "AddressType",
                "definition": "",
            }
        ],
    )
    rc = main(
        [
            "concepts",
            "scaffold",
            "postal_code",
            "--repo-root",
            str(tmp_path),
            "--field",
            "mits=AddressType/Postal_Code",  # typo
        ]
    )
    assert rc == 2
    assert "not found" in capsys.readouterr().out


def test_cli_concepts_check_ignores_committed_semantic_when_flag_not_passed(
    tmp_path: Path,
) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addr",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal"}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal"}],
    )
    # Generate the string-match outputs.
    main(["concepts", "census", "--repo-root", str(tmp_path)])
    main(["concepts", "suggest", "--repo-root", str(tmp_path)])
    # Pretend a prior `--semantic` run committed a semantic file.
    semantic = tmp_path / "docs" / "concepts-analysis" / "suggestions-semantic.md"
    semantic.write_text("# Semantic candidate concept clusters\n\nstub content.\n")
    # Plain `check` (no --semantic flag) must not flag the committed
    # semantic file as out-of-date.
    rc = main(["concepts", "check", "--repo-root", str(tmp_path)])
    assert rc == 0


def test_semantic_suggest_writes_clusters(tmp_path: Path) -> None:
    rows = [
        _row("mits", "lease", "Lease", "LeaseStartDate", "the date the lease starts"),
        _row("ibpdi", "pm", "RentalContract", "MoveInDate", "the date the lease starts"),
    ]
    clusters = suggest_semantic_clusters(
        rows, crosswalks=[], encoder=BagOfWordsEncoder(), threshold=0.5
    )
    out_dir = tmp_path / "out"
    write_semantic_suggestions(clusters, out_dir, model_name="stub", threshold=0.5)
    text = (out_dir / SUGGESTIONS_SEMANTIC_MD).read_text()
    assert "Semantic candidate concept clusters" in text
    assert "Uncovered candidates" in text
