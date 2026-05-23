"""XSD-extractor-specific assertions."""

from __future__ import annotations

from pathlib import Path

from cora_extractors.path import resolve
from cora_extractors.xsd import XsdExtractor

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "xsd"


def test_includes_resolved_transitively() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    type_names = {t.name for t in inv.types}
    # Address comes from the included common.xsd.
    assert {"Property", "Address", "ResidentialProperty"} <= type_names


def test_extension_captured_as_extends() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    res = next(t for t in inv.types if t.name == "ResidentialProperty")
    assert res.extends == "Property"


def test_object_reference_marked() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    addr_field = resolve("Property/address", inv)
    assert addr_field is not None
    assert addr_field.range == "Address"
    assert addr_field.is_reference is True


def test_primitive_field_not_marked_reference() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    id_field = resolve("Property/id", inv)
    assert id_field is not None
    assert id_field.range == "xs:string"
    assert id_field.is_reference is False


def test_inline_enumeration_captured() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    status = resolve("Property/status", inv)
    assert status is not None
    assert status.enumeration == ["active", "inactive", "archived"]


def test_repeating_cardinality_from_unbounded() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    tenants = resolve("Property/tenants", inv)
    assert tenants is not None
    assert tenants.cardinality == "repeating"


def test_attribute_use_required() -> None:
    inv = XsdExtractor().extract(FIXTURES / "a" / "main.xsd", module="a")
    created = resolve("Property/created", inv)
    assert created is not None
    assert created.cardinality == "required"


def test_second_fixture_is_generic() -> None:
    inv = XsdExtractor().extract(FIXTURES / "b" / "single.xsd", module="b")
    type_names = {t.name for t in inv.types}
    assert "Asset" in type_names
    kind = resolve("Asset/kind", inv)
    assert kind is not None
    assert kind.enumeration == ["solar", "wind", "battery"]
