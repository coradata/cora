from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest

from cora_extractors.inventory import (
    FieldEntry,
    Inventory,
    MergeConflict,
    StructuralError,
    TypeEntry,
)

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"


def _read(path: Path) -> str:
    return path.read_text()


@pytest.mark.parametrize(
    "fixture",
    ["inventory-with-types.yaml", "inventory-flat.yaml"],
)
def test_fixture_round_trips_textually(fixture: str, tmp_path: Path) -> None:
    src = FIXTURES / fixture
    inv = Inventory.from_yaml(src)
    out = tmp_path / fixture
    inv.to_yaml(out)
    assert _read(out) == _read(src)


@pytest.mark.parametrize(
    "fixture",
    ["inventory-with-types.yaml", "inventory-flat.yaml"],
)
def test_fixture_round_trips_semantically(fixture: str, tmp_path: Path) -> None:
    src = FIXTURES / fixture
    inv = Inventory.from_yaml(src)
    out = tmp_path / fixture
    inv.to_yaml(out)
    reloaded = Inventory.from_yaml(out)
    assert reloaded == inv


def test_validate_accepts_well_formed_inventories() -> None:
    Inventory.from_yaml(FIXTURES / "inventory-with-types.yaml").validate_structure()
    Inventory.from_yaml(FIXTURES / "inventory-flat.yaml").validate_structure()


def test_validate_rejects_dangling_extends() -> None:
    inv = Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        types=[TypeEntry(name="A", extends="Nonexistent")],
        fields=[FieldEntry(path="A/x", domain="A", cardinality="required")],
    )
    with pytest.raises(StructuralError) as exc:
        inv.validate_structure()
    assert any("Nonexistent" in issue for issue in exc.value.issues)


def test_validate_rejects_field_without_domain_when_types_present() -> None:
    inv = Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        types=[TypeEntry(name="A")],
        fields=[FieldEntry(path="A/x", cardinality="required")],
    )
    with pytest.raises(StructuralError) as exc:
        inv.validate_structure()
    assert any("missing domain" in issue for issue in exc.value.issues)


def test_validate_rejects_unknown_domain() -> None:
    inv = Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        types=[TypeEntry(name="A")],
        fields=[FieldEntry(path="A/x", domain="B", cardinality="required")],
    )
    with pytest.raises(StructuralError) as exc:
        inv.validate_structure()
    assert any("domain 'B'" in issue for issue in exc.value.issues)


def test_validate_rejects_unknown_object_reference_range() -> None:
    inv = Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        types=[TypeEntry(name="A")],
        fields=[
            FieldEntry(
                path="A/ref",
                domain="A",
                range="Nonexistent",
                is_reference=True,
                cardinality="required",
            ),
        ],
    )
    with pytest.raises(StructuralError) as exc:
        inv.validate_structure()
    assert any("Nonexistent" in issue for issue in exc.value.issues)


def _base_inv(fields: list[FieldEntry], types: list[TypeEntry] | None = None) -> Inventory:
    return Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        types=types or [],
        fields=fields,
    )


def test_merge_enriches_missing_definition() -> None:
    a = _base_inv([FieldEntry(path="tenant", cardinality="required")])
    b = _base_inv(
        [FieldEntry(path="tenant", cardinality="required", definition="Resident of unit.")]
    )
    merged = a.merge(b, match_by="name")
    assert merged.fields[0].definition == "Resident of unit."


def test_merge_preserves_self_metadata() -> None:
    a = _base_inv([FieldEntry(path="tenant", cardinality="required")])
    b = Inventory(
        standard="other",
        module="other",
        version="9",
        source_artifact="other.xlsx",
        extractor="other@9",
        extracted_at=datetime(2099, 1, 1, tzinfo=UTC),
        fields=[FieldEntry(path="tenant", cardinality="required", definition="d")],
    )
    merged = a.merge(b, match_by="name")
    assert merged.standard == "x"
    assert merged.extractor == "t@0"


def test_merge_appends_unmatched_fields() -> None:
    a = _base_inv([FieldEntry(path="tenant", cardinality="required")])
    b = _base_inv([FieldEntry(path="rent", cardinality="required", definition="Monthly rent.")])
    merged = a.merge(b, match_by="name")
    paths = [f.path for f in merged.fields]
    assert paths == ["tenant", "rent"]


def test_merge_raises_on_cardinality_conflict() -> None:
    a = _base_inv([FieldEntry(path="tenant", cardinality="required")])
    b = _base_inv([FieldEntry(path="tenant", cardinality="optional")])
    with pytest.raises(MergeConflict) as exc:
        a.merge(b, match_by="name")
    assert any("cardinality" in c for c in exc.value.conflicts)


def test_merge_raises_on_enumeration_conflict() -> None:
    a = _base_inv(
        [FieldEntry(path="status", cardinality="required", enumeration=["a", "b"])]
    )
    b = _base_inv(
        [FieldEntry(path="status", cardinality="required", enumeration=["a", "c"])]
    )
    with pytest.raises(MergeConflict) as exc:
        a.merge(b, match_by="name")
    assert any("enumeration" in c for c in exc.value.conflicts)


def test_merge_match_by_path_vs_name() -> None:
    a = _base_inv([FieldEntry(path="A/tenant", cardinality="required")])
    b = _base_inv(
        [FieldEntry(path="B/tenant", cardinality="required", definition="enriched")]
    )
    # match_by="name" considers last segment, so these match
    merged_by_name = a.merge(b, match_by="name")
    assert merged_by_name.fields[0].definition == "enriched"
    assert len(merged_by_name.fields) == 1
    # match_by="path" treats them as distinct
    merged_by_path = a.merge(b, match_by="path")
    assert len(merged_by_path.fields) == 2
