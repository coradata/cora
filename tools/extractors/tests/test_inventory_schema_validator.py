"""Tests for the inventory-schema Validator adapter."""

from __future__ import annotations

import shutil
from pathlib import Path

from cora_extractors.validator import Validator
from cora_extractors.validators.inventory_schema import InventorySchemaValidator

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = PACKAGE_ROOT / "schema" / "inventory.schema.json"
FIXTURES = PACKAGE_ROOT / "fixtures"


def _stage_repo(tmp_path: Path, fixtures: list[tuple[str, str, Path]]) -> Path:
    """Build a tiny ``repo_root`` tree containing the schema and inventories."""
    repo = tmp_path / "repo"
    (repo / "tools" / "extractors" / "schema").mkdir(parents=True)
    shutil.copy(SCHEMA, repo / "tools" / "extractors" / "schema" / "inventory.schema.json")
    for std, module, src in fixtures:
        dest_dir = repo / "standards" / std / "current" / "inventory"
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest_dir / f"{module}.yaml")
    return repo


def test_validator_passes_on_well_formed_inventories(tmp_path: Path) -> None:
    repo = _stage_repo(
        tmp_path,
        [
            ("example", "with-types", FIXTURES / "inventory-with-types.yaml"),
            ("example", "flat", FIXTURES / "inventory-flat.yaml"),
        ],
    )
    result = InventorySchemaValidator().check(repo)
    assert not result.has_errors
    assert result.findings == []


def test_validator_protocol_conformance() -> None:
    v = InventorySchemaValidator()
    assert isinstance(v, Validator)
    assert v.name == "inventory-schema"


def test_validator_reports_schema_errors(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / "tools" / "extractors" / "schema").mkdir(parents=True)
    shutil.copy(SCHEMA, repo / "tools" / "extractors" / "schema" / "inventory.schema.json")
    bad_dir = repo / "standards" / "broken" / "current" / "inventory"
    bad_dir.mkdir(parents=True)
    (bad_dir / "bad.yaml").write_text("standard: x\n")  # missing required fields

    result = InventorySchemaValidator().check(repo)
    assert result.has_errors


def test_validator_reports_missing_schema(tmp_path: Path) -> None:
    result = InventorySchemaValidator().check(tmp_path)
    assert result.has_errors
    assert any("schema file is missing" in f.message for f in result.findings)
