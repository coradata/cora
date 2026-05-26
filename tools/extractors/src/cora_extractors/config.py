"""Per-extractor typed configuration.

Each format-specific extractor takes a concrete ExtractorConfig subclass.
Configs are loaded from YAML and validated at load time; typos surface
as pydantic validation errors instead of attribute errors during a run.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict


class ExtractorConfig(BaseModel):
    """Base class for all extractor configs."""

    model_config = ConfigDict(extra="forbid")

    @classmethod
    def from_yaml(cls, path: Path) -> ExtractorConfig:
        with path.open() as f:
            data = yaml.safe_load(f)
        return cls.model_validate(data)


class XsdConfig(ExtractorConfig):
    """Optional configuration for the XSD extractor.

    The XSD extractor is largely generic-by-construction; this config exists
    for forward-compatibility and for redirecting ``xs:include`` /
    ``xs:import`` ``schemaLocation`` values that point at remote URLs the
    extractor cannot fetch (e.g., MITS modules that reference
    ``http://www.nmhc.info/MITS/MITSCoreData30.xsd`` even though the file
    is shipped locally elsewhere in the corpus).
    """

    namespace_hint: str | None = None
    include_remap: dict[str, str] = {}
    skip_unmapped_remote_includes: bool = True


class JsonCatalogConfig(ExtractorConfig):
    """Configuration for the JSON catalog extractor.

    Describes how to walk an arbitrary JSON catalog of fields. The extractor
    is config-driven so new JSON-based standards land without code changes.
    """

    fields_jsonpath: str
    name_key: str
    type_key: str | None = None
    definition_key: str | None = None
    cardinality_key: str | None = None
    enumeration_key: str | None = None
    type_map: dict[str, str] = {}
    cardinality_map: dict[str, str] = {}
    default_cardinality: str = "optional"
    types_jsonpath: str | None = None
    type_name_key: str | None = None
    type_extends_key: str | None = None
    type_definition_key: str | None = None
    path_prefix: list[str] = []
    namespace_hint: str | None = None


class CdmJsonConfig(ExtractorConfig):
    """Configuration for the Microsoft Common Data Model (CDM) JSON extractor.

    CDM JSON is a defined format (one entity per ``*.cdm.json`` file, attributes
    nested under ``definitions[].hasAttributes[]``), so the extractor is largely
    generic-by-construction. This config exists for the few choices that vary
    per source.
    """

    namespace_hint: str | None = None
    # Treat references to this base type as the "no real parent" marker. CDM
    # entities typically extend ``CdmEntity`` (a framework-level base type)
    # which has no application-domain meaning. By default we keep the
    # reference as a cross-inventory pointer (it will surface in
    # ``Inventory.external_references()``); set to a different value if a
    # corpus uses a different root.
    inheritance_root: str = "CdmEntity"


class ExcelDictionaryConfig(ExtractorConfig):
    """Configuration for the Excel data dictionary extractor (primary mode)."""

    sheet: str
    field_name_column: str
    type_column: str | None = None
    definition_column: str | None = None
    cardinality_column: str | None = None
    enumeration_column: str | None = None
    skip_rows: int = 1
    path_prefix: list[str] = []
    namespace_hint: str | None = None


class ExcelMultiSheetDictionaryConfig(ExtractorConfig):
    """Configuration for the multi-sheet MITS data-dictionary extractor.

    A MITS dictionary workbook has one "top" sheet documenting the module
    tree (currently skipped — the XSD inventory doesn't model the module
    root as a type, so there's nothing to enrich against) plus one sheet
    per shared type (``PersonType``, ``AddressType``, etc.). Each type
    sheet emits per-field rows with ``domain`` set to the target type
    name, so ``Inventory.enrich`` can match them against the XSD-derived
    fields type-scoped.

    The extractor auto-detects the header row by scanning for
    ``header_marker`` in column A of the first ``header_search_rows`` rows
    of each type sheet, then counts consecutive ``hierarchy_marker`` cells
    after it to derive hierarchy depth. Defaults match the MITS
    convention; override if a workbook deviates.
    """

    type_sheets: dict[str, str]
    """Map of sheet name → target type name (the ``domain`` to claim)."""

    header_marker: str = "Common Root Element"
    hierarchy_marker: str = "Child Element/Attribute"
    header_search_rows: int = 10

    description_column_name: str = "Description"
    data_type_column_name: str = "Data Type"
    required_column_name: str = "Req"
    max_occurs_column_name: str = "Max occurs"
    values_column_name: str = "Values"

    namespace_hint: str | None = None
