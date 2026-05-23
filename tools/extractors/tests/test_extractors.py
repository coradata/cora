"""Parameterized round-trip tests across every registered Extractor adapter.

Each adapter is exercised against ≥2 fixture sources to prove the
"genericity bar": handling a new source of an already-supported format
should require a config file, not new code.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

import pytest
import yaml
from jsonschema import Draft202012Validator

from cora_extractors.cli import CONFIG_TYPES, EXTRACTORS
from cora_extractors.config import ExtractorConfig
from cora_extractors.extractor import Extractor
from cora_extractors.inventory import Inventory

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCHEMA_PATH = REPO_ROOT / "schema" / "inventory.schema.json"


def _fixture_specs() -> list[tuple[str, Path, Path | None]]:
    return [
        ("xsd", FIXTURES / "xsd" / "a" / "main.xsd", None),
        ("xsd", FIXTURES / "xsd" / "b" / "single.xsd", None),
        ("json", FIXTURES / "json" / "a" / "catalog.json", FIXTURES / "json" / "a" / "config.yaml"),
        ("json", FIXTURES / "json" / "b" / "catalog.json", FIXTURES / "json" / "b" / "config.yaml"),
        (
            "excel",
            FIXTURES / "excel" / "a" / "dictionary.xlsx",
            FIXTURES / "excel" / "a" / "config.yaml",
        ),
        (
            "excel",
            FIXTURES / "excel" / "b" / "dictionary.xlsx",
            FIXTURES / "excel" / "b" / "config.yaml",
        ),
    ]


@pytest.fixture(scope="session")
def schema_validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA_PATH.read_text()))


@pytest.mark.parametrize(
    ("format_name", "source", "config_path"),
    _fixture_specs(),
    ids=lambda v: str(v) if not isinstance(v, Path) else v.name,
)
def test_extractor_produces_schema_valid_output(
    format_name: str,
    source: Path,
    config_path: Path | None,
    tmp_path: Path,
    schema_validator: Draft202012Validator,
) -> None:
    extractor: Extractor = EXTRACTORS[format_name]
    config: ExtractorConfig | None = None
    if config_path is not None:
        config = CONFIG_TYPES[format_name].from_yaml(config_path)

    inventory = extractor.extract(source, config, module="example")

    # Output validates as Inventory (already enforced by pydantic) and against
    # the JSON Schema wire format.
    out = tmp_path / "out.yaml"
    inventory.to_yaml(out)
    data: Any = yaml.safe_load(out.read_text())
    errors = list(schema_validator.iter_errors(data))
    assert not errors, f"schema errors: {[e.message for e in errors]}"

    # Re-read and confirm semantic round-trip.
    reloaded = Inventory.from_yaml(out)
    assert reloaded == inventory

    # Structural invariants (e.g. domain references valid types).
    reloaded.validate_structure()


@pytest.mark.parametrize("format_name", sorted(EXTRACTORS.keys()))
def test_extractor_protocol_conformance(format_name: str) -> None:
    extractor: Any = EXTRACTORS[format_name]
    # Runtime-checkable Protocol verifies presence of name + extract.
    assert isinstance(extractor, Extractor)
    assert isinstance(extractor.name, str) and extractor.name
    # Cast to satisfy mypy; runtime check is the assertion above.
    cast(Extractor, extractor)
