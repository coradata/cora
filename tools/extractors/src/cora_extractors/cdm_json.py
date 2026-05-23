"""Microsoft Common Data Model (CDM) JSON extractor adapter.

Reads a CDM cluster manifest (``*.manifest.cdm.json``) and the entity files it
lists, emitting a typed Inventory. Generic-by-construction — CDM JSON is a
defined format, so no per-source field-mapping config is required.

Coverage in v1:
- ``definitions[].entityName`` → ``types[]`` entry.
- ``definitions[].extendsEntity`` → ``extends`` on the type entry. Cross-
  inventory references (the CDM base ``CdmEntity`` and inter-cluster type
  refs) are kept as-is; they surface via ``Inventory.external_references()``.
- Each ``hasAttributes[]`` element with a ``name`` becomes a ``fields[]`` row
  with ``domain`` set to the containing entity and ``range`` set to the
  CDM ``dataType``.
- ``description`` populates ``definition``.
- Enumerations are extracted from the ``does.haveDefault`` trait when the
  attribute carries ``valueConstrainedToList: true``.
- ``attributeGroupReference`` entries are not expanded in v1 (would require
  walking imports and resolving attribute group definitions); their absence
  is noted but does not error.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from cora_extractors import __version__
from cora_extractors.config import CdmJsonConfig, ExtractorConfig
from cora_extractors.inventory import FieldEntry, Inventory, TypeEntry
from cora_extractors.path import build as build_path

EXTRACTOR_ID = f"cora_extractors.cdm_json@{__version__}"


class CdmJsonExtractor:
    """Extractor adapter for Microsoft CDM JSON manifests."""

    name = "cdm-json"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if config is not None and not isinstance(config, CdmJsonConfig):
            raise TypeError("CdmJsonExtractor.extract requires CdmJsonConfig or None")

        cdm_config = config if isinstance(config, CdmJsonConfig) else CdmJsonConfig()
        manifest = _load_json(source)
        manifest_dir = source.parent

        types: list[TypeEntry] = []
        fields: list[FieldEntry] = []
        for entry in manifest.get("entities", []):
            if entry.get("type") != "LocalEntity":
                continue
            entity_path = entry.get("entityPath")
            if not isinstance(entity_path, str) or "/" not in entity_path:
                continue
            relative_file, _, _ = entity_path.partition("/")
            entity_file = manifest_dir / relative_file
            for type_entry, field_entries in _read_entity_file(entity_file, cdm_config):
                types.append(type_entry)
                fields.extend(field_entries)

        return Inventory(
            standard=module or source.parent.name,
            module=module or source.parent.name,
            version="unknown",
            source_artifact=str(source),
            extractor=EXTRACTOR_ID,
            extracted_at=datetime.now(tz=UTC),
            namespace_hint=cdm_config.namespace_hint,
            types=types,
            fields=fields,
        )


def _load_json(path: Path) -> dict[str, Any]:
    with path.open() as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object at {path}, got {type(data).__name__}")
    return data


def _read_entity_file(
    path: Path, config: CdmJsonConfig
) -> Iterable[tuple[TypeEntry, list[FieldEntry]]]:
    """Yield (TypeEntry, fields) tuples for every entity definition in a CDM JSON file."""
    try:
        data = _load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"failed to read CDM entity file {path}: {exc}") from exc

    location_base = path.name
    for defn in data.get("definitions", []):
        if not isinstance(defn, dict):
            continue
        entity_name = defn.get("entityName")
        if not isinstance(entity_name, str) or not entity_name:
            continue

        type_entry = TypeEntry(
            name=entity_name,
            extends=defn.get("extendsEntity"),
            abstract=False,
            definition=_string_or_empty(defn.get("description")),
            source_location=location_base,
        )
        fields = list(_iter_attributes(entity_name, defn.get("hasAttributes", []), location_base))
        yield type_entry, fields


def _iter_attributes(
    entity_name: str, attributes: list[Any], source_location: str
) -> Iterable[FieldEntry]:
    for attr in attributes:
        if not isinstance(attr, dict):
            continue
        name = attr.get("name")
        if not isinstance(name, str) or not name:
            # attributeGroupReference and other non-attribute entries land here.
            continue
        yield FieldEntry(
            path=build_path([entity_name, name]),
            domain=entity_name,
            range=_string_or_none(attr.get("dataType")),
            is_reference=False,
            cardinality="optional",
            definition=_string_or_empty(attr.get("description")),
            source_location=source_location,
            enumeration=_extract_enumeration(attr),
        )


def _extract_enumeration(attr: dict[str, Any]) -> list[str] | None:
    """Extract enumeration values from the CDM does.haveDefault trait.

    The trait carries a 2-D constantValues table whose third column (index 2)
    is the canonical value the CDM runtime emits. We only consider the
    enumeration "real" when the attribute also flags ``valueConstrainedToList``.
    """
    if not attr.get("valueConstrainedToList"):
        return None
    traits = attr.get("appliedTraits", [])
    if not isinstance(traits, list):
        return None
    for trait in traits:
        if not isinstance(trait, dict):
            continue
        if trait.get("traitReference") != "does.haveDefault":
            continue
        for argument in trait.get("arguments", []):
            if not isinstance(argument, dict):
                continue
            entity_ref = argument.get("entityReference")
            if not isinstance(entity_ref, dict):
                continue
            values = entity_ref.get("constantValues")
            if not isinstance(values, list):
                continue
            collected: list[str] = []
            for row in values:
                if isinstance(row, list) and len(row) > 2 and isinstance(row[2], str):
                    collected.append(row[2])
            if collected:
                return collected
    return None


def _string_or_empty(value: Any) -> str:
    return value if isinstance(value, str) else ""


def _string_or_none(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None
