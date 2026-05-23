"""End-to-end CLI tests, including the XSD+Excel merge flow.

These tests run the CLI's ``main`` in-process to exercise the registry,
argparse wiring, and config loading without subprocess overhead.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cora_extractors.cli import main
from cora_extractors.inventory import Inventory

FIXTURES_PKG = Path(__file__).resolve().parents[1] / "tests" / "fixtures"


def test_cli_extract_xsd(tmp_path: Path) -> None:
    out = tmp_path / "out.yaml"
    rc = main(
        [
            "extract",
            "xsd",
            str(FIXTURES_PKG / "xsd" / "a" / "main.xsd"),
            "--module",
            "a",
            "--output",
            str(out),
        ]
    )
    assert rc == 0
    inv = Inventory.from_yaml(out)
    assert {t.name for t in inv.types} >= {"Property", "Address", "ResidentialProperty"}


def test_cli_extract_with_standard_version_and_repo_root(tmp_path: Path) -> None:
    out = tmp_path / "out.yaml"
    source = FIXTURES_PKG / "xsd" / "a" / "main.xsd"
    repo_root = FIXTURES_PKG.parents[2]  # tools/extractors root sits above tests/
    rc = main(
        [
            "extract",
            "xsd",
            str(source),
            "--standard",
            "demo",
            "--module",
            "core",
            "--version",
            "1.2",
            "--repo-root",
            str(repo_root),
            "--output",
            str(out),
        ]
    )
    assert rc == 0
    inv = Inventory.from_yaml(out)
    assert inv.standard == "demo"
    assert inv.module == "core"
    assert inv.version == "1.2"
    # source_artifact is repo-relative, not absolute.
    assert not inv.source_artifact.startswith("/")
    assert inv.source_artifact.endswith("main.xsd")


def test_cli_extract_excel(tmp_path: Path) -> None:
    out = tmp_path / "out.yaml"
    rc = main(
        [
            "extract",
            "excel",
            str(FIXTURES_PKG / "excel" / "a" / "dictionary.xlsx"),
            "--config",
            str(FIXTURES_PKG / "excel" / "a" / "config.yaml"),
            "--module",
            "a",
            "--output",
            str(out),
        ]
    )
    assert rc == 0
    inv = Inventory.from_yaml(out)
    assert len(inv.fields) == 5


def test_cli_extract_json(tmp_path: Path) -> None:
    out = tmp_path / "out.yaml"
    rc = main(
        [
            "extract",
            "json",
            str(FIXTURES_PKG / "json" / "a" / "catalog.json"),
            "--config",
            str(FIXTURES_PKG / "json" / "a" / "config.yaml"),
            "--module",
            "a",
            "--output",
            str(out),
        ]
    )
    assert rc == 0
    inv = Inventory.from_yaml(out)
    assert {f.path for f in inv.fields} == {"owner", "valuation", "status"}


def test_cli_inventory_summary(capsys: pytest.CaptureFixture[str]) -> None:
    pkg_fixtures = Path(__file__).resolve().parents[1] / "fixtures"
    inv_path = pkg_fixtures / "inventory-with-types.yaml"
    rc = main(["inventory", "summary", str(inv_path)])
    assert rc == 0
    out = capsys.readouterr().out
    assert "classes:" in out
    assert "properties:" in out


def test_inventory_merge_end_to_end_xsd_plus_excel(tmp_path: Path) -> None:
    """Extract XSD inventory, extract Excel inventory, merge by path.

    Match-by-path keeps full ``Type/field`` paths distinct from flat Excel paths,
    so this exercises the "append unmatched" branch end-to-end. (Match-by-name
    would surface MergeConflicts here because both sources name a ``status``
    field with different enumerations — that's by design; see merge tests.)
    """
    xsd_out = tmp_path / "xsd.yaml"
    excel_out = tmp_path / "excel.yaml"

    rc = main(
        [
            "extract",
            "xsd",
            str(FIXTURES_PKG / "xsd" / "a" / "main.xsd"),
            "--module",
            "merged",
            "--output",
            str(xsd_out),
        ]
    )
    assert rc == 0

    rc = main(
        [
            "extract",
            "excel",
            str(FIXTURES_PKG / "excel" / "a" / "dictionary.xlsx"),
            "--config",
            str(FIXTURES_PKG / "excel" / "a" / "config.yaml"),
            "--module",
            "merged",
            "--output",
            str(excel_out),
        ]
    )
    assert rc == 0

    a = Inventory.from_yaml(xsd_out)
    b = Inventory.from_yaml(excel_out)
    merged = a.merge(b, match_by="path")
    assert merged.standard == a.standard
    # XSD fields use Type/field paths; Excel uses flat paths. No overlap.
    assert len(merged.fields) == len(a.fields) + len(b.fields)
