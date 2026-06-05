"""Tests for the Generator seam and its five adapters.

Strategy: build a minimal fixture repo in tmp_path (one inventory + one
crosswalk), run each Generator, assert the expected files exist with the
expected key content. Plus a global idempotency check (build twice, get
the same bytes) and a Mermaid sanity check (every ```mermaid block parses
as a flowchart).
"""

from __future__ import annotations

import re
import shutil
import textwrap
from pathlib import Path

from cora_extractors.generator import Generator
from cora_extractors.generators.concept_graphs import ConceptGraphsGenerator
from cora_extractors.generators.concept_pages import ConceptPagesGenerator
from cora_extractors.generators.coverage_matrix import CoverageMatrixGenerator
from cora_extractors.generators.index import IndexGenerator
from cora_extractors.generators.inventory_pages import InventoryPagesGenerator

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
INVENTORY_FIXTURE = PACKAGE_ROOT / "fixtures" / "inventory-with-types.yaml"

GENERATORS = [
    CoverageMatrixGenerator(),
    ConceptPagesGenerator(),
    ConceptGraphsGenerator(),
    InventoryPagesGenerator(),
    IndexGenerator(),
]


def _stage_repo(tmp_path: Path, *, with_crosswalk: bool = True) -> Path:
    repo = tmp_path / "repo"
    (repo / "standards" / "ibpdi" / "current" / "inventory").mkdir(parents=True)
    shutil.copy(
        INVENTORY_FIXTURE,
        repo / "standards" / "ibpdi" / "current" / "inventory" / "core.yaml",
    )

    if with_crosswalk:
        (repo / "crosswalks" / "concepts").mkdir(parents=True)
        (repo / "crosswalks" / "concepts" / "street.yaml").write_text(
            textwrap.dedent(
                """\
                concept: street
                canonical_definition: The primary delivery line of an address.
                aliases:
                  - thoroughfare
                maintainer: '@coradata/maintainers'
                last_reviewed: '2026-06-02'
                mappings:
                  ibpdi:
                    field: Address/street
                    version: '1.0'
                    confidence: exact
                  mits:
                    field: null
                    version: '4.0'
                    confidence: not_present
                    notes: MITS not present in this minimal fixture repo.
                """
            )
        )
    return repo


# ---------------------------------------------------------------------------
# Protocol conformance
# ---------------------------------------------------------------------------


def test_every_generator_implements_protocol() -> None:
    for g in GENERATORS:
        assert isinstance(g, Generator), f"{g.__class__.__name__} is not a Generator"
        assert g.name, f"{g.__class__.__name__} has empty name"


# ---------------------------------------------------------------------------
# Per-generator behaviour
# ---------------------------------------------------------------------------


def test_coverage_matrix_emits_table_with_concept_and_standards(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = CoverageMatrixGenerator().generate(repo, out)
    assert paths == [Path("coverage-matrix.md")]
    body = (out / "coverage-matrix.md").read_text()
    assert "# Crosswalk Coverage Matrix" in body
    assert "| [street](concepts/street.md)" in body
    assert "exact" in body
    assert "not_present" in body


def test_coverage_matrix_emits_nothing_when_no_crosswalks(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path, with_crosswalk=False)
    out = tmp_path / "out"
    paths = CoverageMatrixGenerator().generate(repo, out)
    assert paths == []


def test_concept_pages_emits_one_per_crosswalk(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = ConceptPagesGenerator().generate(repo, out)
    assert paths == [Path("concepts/street.md")]
    body = (out / "concepts" / "street.md").read_text()
    assert "# street" in body
    assert "Address/street" in body
    assert "(not present)" in body  # MITS shows up as not_present in the table
    assert "```mermaid" in body
    assert "flowchart LR" in body


def test_concept_pages_resolves_inventory_definitions(tmp_path: Path) -> None:
    """Definition pulled from the inventory's FieldEntry when the path resolves."""
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    ConceptPagesGenerator().generate(repo, out)
    body = (out / "concepts" / "street.md").read_text()
    # The fixture's Address/street field carries a definition string; assert
    # it lands in the rendered table (some non-empty string between `street` and
    # the next pipe).
    assert re.search(r"Address/street.*\|\s*🟢 exact\s*\|\s*\S+", body)


def test_concept_graphs_emits_mermaid_flowchart(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = ConceptGraphsGenerator().generate(repo, out)
    assert paths == [Path("concept-overview.md")]
    body = (out / "concept-overview.md").read_text()
    assert "```mermaid" in body
    assert "flowchart LR" in body
    assert "street" in body
    assert "ibpdi" in body
    assert "exact" in body


def test_inventory_pages_emits_one_per_inventory(tmp_path: Path) -> None:
    """Output path is derived from the inventory's `module` field, not the
    filename on disk — same as how validators key inventories."""
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = InventoryPagesGenerator().generate(repo, out)
    # Fixture inventory's `module:` field is 'example'
    assert paths == [Path("inventories/ibpdi/example.md")]
    body = (out / "inventories" / "ibpdi" / "example.md").read_text()
    assert "# IBPDI / example" in body
    assert "## Types" in body
    assert "## Fields" in body
    assert "Address/street" in body


def test_index_links_to_concepts_and_inventories(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = IndexGenerator().generate(repo, out)
    assert paths == [Path("README.md")]
    body = (out / "README.md").read_text()
    assert "[street](concepts/street.md)" in body
    assert "[example](inventories/ibpdi/example.md)" in body
    assert "Coverage Matrix" in body
    assert "Concept Overview" in body


# ---------------------------------------------------------------------------
# Mermaid sanity — every emitted ```mermaid block opens with `flowchart`
# ---------------------------------------------------------------------------


def test_every_mermaid_block_is_a_flowchart(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    for g in GENERATORS:
        g.generate(repo, out)

    blocks_seen = 0
    for md in out.rglob("*.md"):
        content = md.read_text()
        for match in re.finditer(r"```mermaid\n(.*?)\n```", content, re.DOTALL):
            blocks_seen += 1
            first_line = match.group(1).strip().splitlines()[0].strip()
            assert first_line.startswith("flowchart"), (
                f"Mermaid block in {md.relative_to(out)} doesn't start with flowchart: "
                f"{first_line!r}"
            )
    assert blocks_seen >= 2, "expected at least concept page + concept overview"


# ---------------------------------------------------------------------------
# Idempotency — generators are pure; building twice gives identical output
# ---------------------------------------------------------------------------


def test_build_is_idempotent(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out_a = tmp_path / "build-a"
    out_b = tmp_path / "build-b"
    for g in GENERATORS:
        g.generate(repo, out_a)
    for g in GENERATORS:
        g.generate(repo, out_b)

    files_a = {p.relative_to(out_a) for p in out_a.rglob("*") if p.is_file()}
    files_b = {p.relative_to(out_b) for p in out_b.rglob("*") if p.is_file()}
    assert files_a == files_b
    for rel in files_a:
        assert (out_a / rel).read_text() == (out_b / rel).read_text(), (
            f"non-deterministic output: {rel}"
        )
