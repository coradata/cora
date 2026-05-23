"""Tests for the cdm-json extractor adapter."""

from __future__ import annotations

from pathlib import Path

from cora_extractors.cdm_json import CdmJsonExtractor
from cora_extractors.config import CdmJsonConfig
from cora_extractors.extractor import Extractor
from cora_extractors.path import resolve

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "cdm_json"


def _widgets() -> CdmJsonExtractor:
    return CdmJsonExtractor()


def test_protocol_conformance() -> None:
    extractor = _widgets()
    assert isinstance(extractor, Extractor)
    assert extractor.name == "cdm-json"


def test_walks_manifest_and_extracts_entities() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    type_names = {t.name for t in inv.types}
    assert {"Widget", "Gadget"} == type_names


def test_extends_captured_for_user_and_framework_types() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    widget = next(t for t in inv.types if t.name == "Widget")
    gadget = next(t for t in inv.types if t.name == "Gadget")
    assert widget.extends == "CdmEntity"  # framework base — cross-inventory reference
    assert gadget.extends == "Widget"  # in-inventory reference resolves cleanly
    # Cross-inventory CdmEntity surfaces via external_references.
    externals = inv.external_references()
    assert any("CdmEntity" in r for r in externals)


def test_attribute_group_references_skipped() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    # Widget has 3 hasAttributes entries, one of which is an attributeGroupReference.
    widget_fields = [f for f in inv.fields if f.domain == "Widget"]
    paths = {f.path for f in widget_fields}
    assert paths == {"Widget/WidgetId", "Widget/Color"}


def test_enumeration_extracted_from_haveDefault_trait() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    color = resolve("Widget/Color", inv)
    assert color is not None
    assert color.enumeration == ["Red", "Green", "Blue"]


def test_description_populates_definition() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    widget_id = resolve("Widget/WidgetId", inv)
    assert widget_id is not None
    assert widget_id.definition == "Unique identifier."


def test_datatype_becomes_range() -> None:
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", module="widgets"
    )
    power = resolve("Gadget/Power", inv)
    assert power is not None
    assert power.range == "decimal"


def test_second_fixture_is_generic() -> None:
    """Adapter handles a different manifest with no code changes."""
    inv = _widgets().extract(
        FIXTURES / "b" / "orders.manifest.cdm.json", module="orders"
    )
    assert {t.name for t in inv.types} == {"Order"}
    assert {f.path for f in inv.fields} == {"Order/OrderId", "Order/Total"}


def test_config_namespace_hint_passthrough() -> None:
    config = CdmJsonConfig(namespace_hint="https://example.org/widgets#")
    inv = _widgets().extract(
        FIXTURES / "a" / "widgets.manifest.cdm.json", config, module="widgets"
    )
    assert inv.namespace_hint == "https://example.org/widgets#"
