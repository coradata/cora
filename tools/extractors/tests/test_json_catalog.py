"""JSON catalog extractor specifics."""

from __future__ import annotations

from pathlib import Path

from cora_extractors.config import JsonCatalogConfig
from cora_extractors.json_catalog import JsonCatalogExtractor
from cora_extractors.path import resolve

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "json"


def _extract(letter: str) -> tuple[JsonCatalogExtractor, Path, JsonCatalogConfig]:
    extractor = JsonCatalogExtractor()
    source = FIXTURES / letter / "catalog.json"
    config = JsonCatalogConfig.from_yaml(FIXTURES / letter / "config.yaml")
    return extractor, source, config


def test_type_map_translates_range() -> None:
    extractor, source, config = _extract("a")
    inv = extractor.extract(source, config, module="a")
    owner = resolve("owner", inv)
    assert owner is not None
    # Config maps "string" → "text".
    assert owner.range == "text"


def test_cardinality_map_translates_booleans() -> None:
    extractor, source, config = _extract("a")
    inv = extractor.extract(source, config, module="a")
    owner = resolve("owner", inv)
    valuation = resolve("valuation", inv)
    assert owner is not None and valuation is not None
    assert owner.cardinality == "required"
    assert valuation.cardinality == "optional"


def test_enumeration_captured() -> None:
    extractor, source, config = _extract("a")
    inv = extractor.extract(source, config, module="a")
    status = resolve("status", inv)
    assert status is not None
    assert status.enumeration == ["draft", "active", "archived"]


def test_second_fixture_different_shape() -> None:
    extractor, source, config = _extract("b")
    inv = extractor.extract(source, config, module="b")
    paths = sorted(f.path for f in inv.fields)
    assert paths == ["loan_id", "principal", "term_months"]
    loan_id = resolve("loan_id", inv)
    assert loan_id is not None
    assert loan_id.range == "id"
    assert loan_id.cardinality == "required"
