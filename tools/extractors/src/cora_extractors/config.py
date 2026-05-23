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
