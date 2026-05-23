"""Inventory summary reader tests."""

from __future__ import annotations

from pathlib import Path

from cora_extractors.inventory import Inventory
from cora_extractors.summary import summarize, summarize_file

FIXTURES_PKG = Path(__file__).resolve().parents[1] / "fixtures"


def test_summary_with_types_fixture() -> None:
    summary = summarize_file(FIXTURES_PKG / "inventory-with-types.yaml")
    assert summary.standard == "example-xsd-standard"
    assert summary.class_count == 3
    assert summary.property_count == 6
    assert summary.object_property_count == 1
    assert summary.datatype_property_count == 5
    assert summary.fields_without_domain == 0
    # ResidentialProperty extends Property → depth 1.
    assert summary.max_inheritance_depth == 1


def test_summary_flat_fixture_has_no_classes() -> None:
    summary = summarize_file(FIXTURES_PKG / "inventory-flat.yaml")
    assert summary.class_count == 0
    assert summary.property_count == 5
    assert summary.fields_without_domain == 5
    assert summary.max_inheritance_depth == 0


def test_summary_render_includes_module() -> None:
    inventory = Inventory.from_yaml(FIXTURES_PKG / "inventory-with-types.yaml")
    rendered = summarize(inventory).render()
    assert "example-xsd-standard/example" in rendered
    assert "classes:" in rendered
    assert "properties:" in rendered
