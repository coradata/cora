"""Tests for the concept-corpus analyzer (census + suggest + report + CLI).

Strategy: build minimal fixture repos under ``tmp_path`` with known
cross-standard overlaps, run the analyzer, assert the expected rows,
clusters, and output bytes. Plus a determinism check (regenerate, same
bytes) and a CLI integration test that exercises ``cora concepts check``.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from cora_extractors.cli import main
from cora_extractors.concepts import (
    collect_census,
    normalize_leaf,
    suggest_clusters,
    write_census_csv,
    write_census_summary,
    write_suggestions,
)
from cora_extractors.concepts.report import CENSUS_CSV, CENSUS_MD, SUGGESTIONS_MD
from cora_extractors.generators._common import load_crosswalks


def _write_inventory(
    repo: Path,
    standard: str,
    module: str,
    fields: list[dict[str, str]],
    types: list[dict[str, str]] | None = None,
) -> None:
    inv_dir = repo / "standards" / standard / "current" / "inventory"
    inv_dir.mkdir(parents=True, exist_ok=True)
    type_block = ""
    if types:
        type_block = "types:\n" + "\n".join(
            f"- name: {t['name']}\n  definition: {t.get('definition', '')}" for t in types
        ) + "\n"
    else:
        type_block = "types: []\n"
    fields_block = "fields:\n" + "\n".join(
        textwrap.dedent(
            f"""\
            - path: {f['path']}
              domain: {f.get('domain', '')}
              range: {f.get('range', 'string')}
              cardinality: {f.get('cardinality', 'required')}
              definition: {f.get('definition', '')}
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
            source_artifact: standards/{standard}/native/whatever
            extractor: cora_extractors.xsd@0.0.0
            extracted_at: '2026-06-01T00:00:00Z'
            source_label: xsd
            """
        )
        + type_block
        + fields_block
    )


def _write_crosswalk(
    repo: Path, concept: str, aliases: list[str], mappings: dict[str, str]
) -> None:
    cw_dir = repo / "crosswalks" / "concepts"
    cw_dir.mkdir(parents=True, exist_ok=True)
    aliases_block = (
        "aliases:\n" + "\n".join(f"  - {a}" for a in aliases) + "\n" if aliases else "aliases: []\n"
    )
    mappings_block = "mappings:\n"
    for std, field_path in mappings.items():
        mappings_block += f"  {std}:\n"
        mappings_block += f"    field: {field_path}\n"
        mappings_block += "    version: '1.0'\n"
        mappings_block += "    confidence: exact\n"
    (cw_dir / f"{concept}.yaml").write_text(
        textwrap.dedent(
            f"""\
            concept: {concept}
            canonical_definition: A canonical definition long enough to satisfy the schema.
            maintainer: '@coradata/maintainers'
            last_reviewed: '2026-06-01'
            """
        )
        + aliases_block
        + mappings_block
    )


# ---- normalize_leaf ---------------------------------------------------------


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("PostalCode", "postal_code"),
        ("Zip_Postal_Code", "zip_postal_code"),
        ("Email-Address", "email_address"),
        ("city", "city"),
        ("CITY", "c_i_t_y"),  # all-caps splits at every char boundary; acceptable
        ("First Name", "first_name"),
        ("HTMLContent", "h_t_m_l_content"),  # known artifact of camel-boundary heuristic
    ],
)
def test_normalize_leaf(raw: str, expected: str) -> None:
    assert normalize_leaf(raw) == expected


# ---- census -----------------------------------------------------------------


def test_collect_census_emits_one_row_per_field(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [
            {
                "path": "AddressType/PostalCode",
                "domain": "AddressType",
                "definition": "Postal code.",
            },
            {"path": "AddressType/City", "domain": "AddressType", "definition": "City name."},
        ],
        types=[{"name": "AddressType", "definition": "Address."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [
            {"path": "Address/PostalCode", "domain": "Address", "definition": "Postal code."},
        ],
        types=[{"name": "Address", "definition": "Address."}],
    )
    rows = collect_census(tmp_path)
    assert len(rows) == 3
    # Deterministic sort: (standard, module, path)
    assert [(r.standard, r.path) for r in rows] == [
        ("ibpdi", "Address/PostalCode"),
        ("mits", "AddressType/City"),
        ("mits", "AddressType/PostalCode"),
    ]
    assert rows[0].leaf_name == "PostalCode"
    assert rows[0].type_name == "Address"


def test_collect_census_handles_flat_source_no_types(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "redi",
        "data-fields",
        [{"path": "Zip_Postal_Code", "domain": "", "definition": "ZIP or postal."}],
    )
    rows = collect_census(tmp_path)
    assert len(rows) == 1
    assert rows[0].type_name == ""
    assert rows[0].leaf_name == "Zip_Postal_Code"


def test_collect_census_empty_repo(tmp_path: Path) -> None:
    assert collect_census(tmp_path) == []


# ---- suggest ----------------------------------------------------------------


def test_suggest_clusters_cross_standard_match(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal code."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal code."}],
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows, crosswalks=[])
    assert len(clusters) == 1
    cluster = clusters[0]
    assert cluster.canonical_key == "postal_code"
    assert cluster.standards == ("ibpdi", "mits")
    assert cluster.already_covered_by is None
    # Definitions are identical so Jaccard is 1.0.
    assert cluster.avg_def_jaccard == pytest.approx(1.0)


def test_suggest_skips_single_standard_clusters(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "a",
        [{"path": "X/Foo", "domain": "X", "definition": "foo."}],
    )
    _write_inventory(
        tmp_path,
        "mits",
        "b",
        [{"path": "Y/Foo", "domain": "Y", "definition": "foo."}],
    )
    rows = collect_census(tmp_path)
    assert suggest_clusters(rows) == []


def test_suggest_marks_already_covered(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal code."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal code."}],
    )
    _write_crosswalk(
        tmp_path,
        concept="postal_code",
        aliases=["zip", "zip_code"],
        mappings={"mits": "AddressType/PostalCode", "ibpdi": "Address/PostalCode"},
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows, crosswalks=load_crosswalks(tmp_path))
    assert len(clusters) == 1
    assert clusters[0].already_covered_by == "postal_code"


def test_suggest_alias_matches_existing_crosswalk(tmp_path: Path) -> None:
    # Two standards expose the concept under different leaf names; one matches
    # the canonical, the other matches via the alias.
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal code."}],
    )
    _write_inventory(
        tmp_path,
        "redi",
        "data-fields",
        [{"path": "Zip_Postal_Code", "domain": "", "definition": "ZIP or postal."}],
    )
    _write_crosswalk(
        tmp_path,
        concept="postal_code",
        aliases=["zip_postal_code"],
        mappings={"mits": "AddressType/PostalCode", "redi": "Zip_Postal_Code"},
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows, crosswalks=load_crosswalks(tmp_path))
    # Each leaf normalizes differently — `postal_code` and `zip_postal_code` —
    # so the bare string clusterer produces two single-standard buckets and
    # therefore zero ≥2-standard clusters. This is the limitation Phase 6c's
    # embeddings pass will address. The assertion captures the current behavior.
    assert clusters == []


def test_suggest_jaccard_signal_low_for_divergent_definitions(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "a",
        [{"path": "X/Description", "domain": "X", "definition": "Notes the agent records."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "b",
        [{"path": "Y/Description", "domain": "Y", "definition": "Free-form prose summary."}],
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows)
    assert len(clusters) == 1
    # Disjoint word sets → Jaccard 0.0.
    assert clusters[0].avg_def_jaccard == pytest.approx(0.0)


# ---- report writers (determinism) -------------------------------------------


def test_report_writers_are_deterministic(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal."}],
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows)

    out_a = tmp_path / "a"
    out_b = tmp_path / "b"
    write_census_csv(rows, out_a)
    write_census_summary(rows, out_a)
    write_suggestions(clusters, out_a)
    write_census_csv(rows, out_b)
    write_census_summary(rows, out_b)
    write_suggestions(clusters, out_b)

    for name in (CENSUS_CSV, CENSUS_MD, SUGGESTIONS_MD):
        assert (out_a / name).read_bytes() == (out_b / name).read_bytes(), name


def test_suggestions_report_marks_covered_section(tmp_path: Path) -> None:
    _write_inventory(
        tmp_path,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal."}],
    )
    _write_inventory(
        tmp_path,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal."}],
    )
    _write_crosswalk(
        tmp_path,
        concept="postal_code",
        aliases=[],
        mappings={"mits": "AddressType/PostalCode", "ibpdi": "Address/PostalCode"},
    )
    rows = collect_census(tmp_path)
    clusters = suggest_clusters(rows, crosswalks=load_crosswalks(tmp_path))
    out = tmp_path / "out"
    write_suggestions(clusters, out)
    text = (out / SUGGESTIONS_MD).read_text()
    assert "Already covered (for reference)" in text
    assert "Already covered by crosswalk: **postal_code**" in text


# ---- CLI integration --------------------------------------------------------


def _seed_two_standard_repo(repo: Path) -> None:
    _write_inventory(
        repo,
        "mits",
        "addressing",
        [{"path": "AddressType/PostalCode", "domain": "AddressType", "definition": "Postal code."}],
    )
    _write_inventory(
        repo,
        "ibpdi",
        "core",
        [{"path": "Address/PostalCode", "domain": "Address", "definition": "Postal code."}],
    )


def test_cli_concepts_census_writes_csv_and_summary(tmp_path: Path) -> None:
    _seed_two_standard_repo(tmp_path)
    rc = main(["concepts", "census", "--repo-root", str(tmp_path)])
    assert rc == 0
    out_dir = tmp_path / "docs" / "concepts-analysis"
    assert (out_dir / CENSUS_CSV).exists()
    assert (out_dir / CENSUS_MD).exists()
    csv_text = (out_dir / CENSUS_CSV).read_text()
    assert "AddressType/PostalCode" in csv_text
    assert "Address/PostalCode" in csv_text


def test_cli_concepts_suggest_writes_report(tmp_path: Path) -> None:
    _seed_two_standard_repo(tmp_path)
    rc = main(["concepts", "suggest", "--repo-root", str(tmp_path)])
    assert rc == 0
    report = (tmp_path / "docs" / "concepts-analysis" / SUGGESTIONS_MD).read_text()
    assert "postal_code" in report
    assert "Uncovered candidates" in report


def test_cli_concepts_check_passes_when_committed_matches_freshly_built(
    tmp_path: Path,
) -> None:
    _seed_two_standard_repo(tmp_path)
    # First write everything by running census + suggest.
    assert main(["concepts", "census", "--repo-root", str(tmp_path)]) == 0
    assert main(["concepts", "suggest", "--repo-root", str(tmp_path)]) == 0
    # Now check should be a no-op.
    assert main(["concepts", "check", "--repo-root", str(tmp_path)]) == 0


def test_cli_concepts_check_fails_when_committed_is_stale(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _seed_two_standard_repo(tmp_path)
    assert main(["concepts", "census", "--repo-root", str(tmp_path)]) == 0
    assert main(["concepts", "suggest", "--repo-root", str(tmp_path)]) == 0
    # Add a new field to one inventory without regenerating the analyzer output.
    inv_path = tmp_path / "standards" / "mits" / "current" / "inventory" / "addressing.yaml"
    inv_path.write_text(
        inv_path.read_text()
        + textwrap.dedent(
            """\
            - path: AddressType/City
              domain: AddressType
              range: string
              cardinality: required
              definition: City name.
            """
        )
    )
    rc = main(["concepts", "check", "--repo-root", str(tmp_path)])
    assert rc == 1
    captured = capsys.readouterr().out
    assert "out of date" in captured
