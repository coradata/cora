"""JSON catalog extractor adapter.

Reads a JSON file (or directory of JSON files) describing a field catalog.
Configuration is supplied via a JsonCatalogConfig; the extractor itself is
format-agnostic so new JSON-shaped standards land as a config file, not
as new code.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

from jsonpath_ng.ext import parse as jsonpath_parse  # type: ignore[import-untyped]

from cora_extractors import __version__
from cora_extractors.config import ExtractorConfig, JsonCatalogConfig
from cora_extractors.inventory import (
    Cardinality,
    FieldEntry,
    Inventory,
    TypeEntry,
)
from cora_extractors.path import build as build_path

EXTRACTOR_ID = f"cora_extractors.json_catalog@{__version__}"

_VALID_CARDINALITY = {"required", "optional", "repeating"}


class JsonCatalogExtractor:
    """Extractor adapter for JSON-shaped field catalogs."""

    name = "json"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if not isinstance(config, JsonCatalogConfig):
            raise TypeError(
                "JsonCatalogExtractor.extract requires a JsonCatalogConfig"
            )

        data = _load_json(source)
        fields = _extract_fields(data, config)
        types = _extract_types(data, config)

        return Inventory(
            standard=module or source.stem,
            module=module or source.stem,
            version="unknown",
            source_artifact=str(source),
            extractor=EXTRACTOR_ID,
            extracted_at=datetime.now(tz=UTC),
            namespace_hint=config.namespace_hint,
            source_label="json",
            types=types,
            fields=fields,
        )


def _load_json(source: Path) -> Any:
    if source.is_dir():
        merged: dict[str, Any] = {"_files": {}}
        for p in sorted(source.glob("*.json")):
            with p.open() as f:
                merged["_files"][p.name] = json.load(f)
        return merged
    with source.open() as f:
        return json.load(f)


def _extract_fields(data: Any, config: JsonCatalogConfig) -> list[FieldEntry]:
    expr = jsonpath_parse(config.fields_jsonpath)
    fields: list[FieldEntry] = []
    for match in expr.find(data):
        entry = match.value
        if not isinstance(entry, dict):
            continue
        name = entry.get(config.name_key)
        if not isinstance(name, str) or not name:
            continue

        path_parts = [*config.path_prefix, name]
        path = build_path(path_parts)

        raw_type = entry.get(config.type_key) if config.type_key else None
        range_value: str | None = None
        if isinstance(raw_type, str):
            range_value = config.type_map.get(raw_type, raw_type)

        raw_card = (
            entry.get(config.cardinality_key) if config.cardinality_key else None
        )
        cardinality = _coerce_cardinality(raw_card, config)

        definition = ""
        if config.definition_key:
            raw_def = entry.get(config.definition_key)
            if isinstance(raw_def, str):
                definition = raw_def

        enumeration: list[str] | None = None
        if config.enumeration_key:
            raw_enum = entry.get(config.enumeration_key)
            if isinstance(raw_enum, list):
                enumeration = [str(v) for v in raw_enum]

        fields.append(
            FieldEntry(
                path=path,
                range=range_value,
                cardinality=cardinality,
                definition=definition,
                source_location=None,
                enumeration=enumeration,
            )
        )
    return fields


def _extract_types(data: Any, config: JsonCatalogConfig) -> list[TypeEntry]:
    if not config.types_jsonpath:
        return []
    if not config.type_name_key:
        raise ValueError("types_jsonpath requires type_name_key in the config")
    expr = jsonpath_parse(config.types_jsonpath)
    types: list[TypeEntry] = []
    for match in expr.find(data):
        entry = match.value
        if not isinstance(entry, dict):
            continue
        name = entry.get(config.type_name_key)
        if not isinstance(name, str) or not name:
            continue
        extends: str | None = None
        if config.type_extends_key:
            raw_extends = entry.get(config.type_extends_key)
            if isinstance(raw_extends, str) and raw_extends:
                extends = raw_extends
        definition = ""
        if config.type_definition_key:
            raw_def = entry.get(config.type_definition_key)
            if isinstance(raw_def, str):
                definition = raw_def
        types.append(TypeEntry(name=name, extends=extends, definition=definition))
    return types


def _coerce_cardinality(raw: Any, config: JsonCatalogConfig) -> Cardinality:
    if raw is None:
        return cast(Cardinality, config.default_cardinality)
    key = str(raw)
    if key in config.cardinality_map:
        mapped = config.cardinality_map[key]
        if mapped in _VALID_CARDINALITY:
            return cast(Cardinality, mapped)
    if key in _VALID_CARDINALITY:
        return cast(Cardinality, key)
    return cast(Cardinality, config.default_cardinality)
