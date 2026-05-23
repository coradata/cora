"""Tests for the field-count Validator adapter."""

from __future__ import annotations

import shutil
from pathlib import Path

from cora_extractors.validator import Validator
from cora_extractors.validators.field_count import FieldCountValidator

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = PACKAGE_ROOT / "fixtures"


def _stage_repo(
    tmp_path: Path,
    inventories: list[tuple[str, str, Path]],
    config: str | None = None,
) -> Path:
    repo = tmp_path / "repo"
    (repo / "tools" / "extractors" / "configs").mkdir(parents=True)
    if config is not None:
        (repo / "tools" / "extractors" / "configs" / "field-count-minimums.yaml").write_text(
            config
        )
    for std, module, src in inventories:
        dest = repo / "standards" / std / "current" / "inventory"
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest / f"{module}.yaml")
    return repo


def test_validator_protocol_conformance() -> None:
    v = FieldCountValidator()
    assert isinstance(v, Validator)
    assert v.name == "field-count"


def test_passes_when_default_minimum_met(tmp_path: Path) -> None:
    repo = _stage_repo(
        tmp_path,
        [("example", "with-types", FIXTURES / "inventory-with-types.yaml")],
        config="default_minimum: 5\n",
    )
    result = FieldCountValidator().check(repo)
    assert not result.has_errors


def test_fails_when_below_default_minimum(tmp_path: Path) -> None:
    repo = _stage_repo(
        tmp_path,
        [("example", "with-types", FIXTURES / "inventory-with-types.yaml")],
        config="default_minimum: 100\n",
    )
    result = FieldCountValidator().check(repo)
    assert result.has_errors
    assert any("below minimum 100" in f.message for f in result.findings)


def test_override_lifts_minimum_for_specific_inventory(tmp_path: Path) -> None:
    # The with-types fixture has 6 fields and the standard is
    # "example-xsd-standard", module "example".
    repo = _stage_repo(
        tmp_path,
        [("example", "with-types", FIXTURES / "inventory-with-types.yaml")],
        config=(
            "default_minimum: 5\n"
            "overrides:\n"
            "  example-xsd-standard/example: 100\n"
        ),
    )
    result = FieldCountValidator().check(repo)
    assert result.has_errors


def test_passes_with_no_config_file(tmp_path: Path) -> None:
    # No config → default_minimum=5, fixture has 6 fields → passes.
    repo = _stage_repo(
        tmp_path,
        [("example", "with-types", FIXTURES / "inventory-with-types.yaml")],
        config=None,
    )
    result = FieldCountValidator().check(repo)
    assert not result.has_errors


def test_passes_when_no_inventories_exist(tmp_path: Path) -> None:
    repo = tmp_path / "empty"
    repo.mkdir()
    result = FieldCountValidator().check(repo)
    assert result.findings == []
