"""Tests for the crosswalk-paths Validator adapter."""

from __future__ import annotations

import shutil
import textwrap
from pathlib import Path

from cora_extractors.validator import Validator
from cora_extractors.validators.crosswalk_paths import CrosswalkPathsValidator

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
INVENTORY_FIXTURE = PACKAGE_ROOT / "fixtures" / "inventory-with-types.yaml"


def _stage_repo(
    tmp_path: Path,
    *,
    crosswalks: dict[str, str],
    inventories: list[tuple[str, str]] | None = None,
) -> Path:
    """Build a minimal repo with the named crosswalks and inventories."""
    repo = tmp_path / "repo"
    (repo / "crosswalks" / "concepts").mkdir(parents=True)
    for name, body in crosswalks.items():
        (repo / "crosswalks" / "concepts" / f"{name}.yaml").write_text(textwrap.dedent(body))

    if inventories:
        for std, module in inventories:
            dest = repo / "standards" / std / "current" / "inventory"
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy(INVENTORY_FIXTURE, dest / f"{module}.yaml")
    return repo


def test_implements_validator_protocol() -> None:
    assert isinstance(CrosswalkPathsValidator(), Validator)


def test_passes_when_all_paths_resolve(tmp_path: Path) -> None:
    """The fixture inventory has a field 'Address/street'."""
    body = """\
        concept: id_value
        canonical_definition: An identifier with at least one specific value attached.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: Address/street
            version: '1.0'
            confidence: exact
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"id_value": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert result.findings == [], result.findings


def test_errors_when_path_does_not_resolve(tmp_path: Path) -> None:
    body = """\
        concept: bogus
        canonical_definition: A concept that doesn't exist in any inventory.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: NoSuchType/NoSuchField
            version: '1.0'
            confidence: exact
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"bogus": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert result.has_errors
    assert any("NoSuchType/NoSuchField" in f.message for f in result.findings)


def test_not_present_with_null_field_is_valid(tmp_path: Path) -> None:
    body = """\
        concept: missing_concept
        canonical_definition: A concept absent from IBPDI but documented as such.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: null
            version: '1.0'
            confidence: not_present
            notes: IBPDI does not model this concept; it's tracked elsewhere.
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"missing": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert not result.has_errors, result.findings


def test_not_present_requires_null_field(tmp_path: Path) -> None:
    body = """\
        concept: bad_not_present
        canonical_definition: Inconsistent — not_present but field is set.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: SomePath/SomeField
            version: '1.0'
            confidence: not_present
            notes: This is wrong.
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"bad": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert result.has_errors
    assert any("must be null when confidence=not_present" in f.message for f in result.findings)


def test_not_present_requires_notes(tmp_path: Path) -> None:
    body = """\
        concept: missing_no_notes
        canonical_definition: not_present without a narrative.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: null
            version: '1.0'
            confidence: not_present
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"x": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert result.has_errors
    assert any("notes required when confidence=not_present" in f.message for f in result.findings)


def test_divergent_requires_notes(tmp_path: Path) -> None:
    body = """\
        concept: divergent_no_notes
        canonical_definition: divergent without a narrative.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          ibpdi:
            field: Address/street
            version: '1.0'
            confidence: divergent
    """
    repo = _stage_repo(
        tmp_path, crosswalks={"x": body}, inventories=[("ibpdi", "core")]
    )
    result = CrosswalkPathsValidator().check(repo)
    assert result.has_errors
    assert any("notes required when confidence=divergent" in f.message for f in result.findings)


def test_unknown_standard_errors(tmp_path: Path) -> None:
    """A crosswalk referencing a standard with no inventories surfaces an error."""
    body = """\
        concept: ghost_standard
        canonical_definition: References a standard not in the repo.
        maintainer: '@coradata/maintainers'
        last_reviewed: '2026-06-01'
        mappings:
          nonexistent_std:
            field: Foo/Bar
            version: '1.0'
            confidence: exact
    """
    repo = _stage_repo(tmp_path, crosswalks={"x": body}, inventories=[("ibpdi", "core")])
    result = CrosswalkPathsValidator().check(repo)
    assert result.has_errors
    assert any("no committed inventories" in f.message for f in result.findings)


def test_no_crosswalks_reports_info_not_error(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / "crosswalks" / "concepts").mkdir(parents=True)
    result = CrosswalkPathsValidator().check(repo)
    assert not result.has_errors
    assert any("no crosswalks found" in f.message for f in result.findings)
