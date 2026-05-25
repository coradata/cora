"""Excel data dictionary extractor adapter (single-sheet primary mode).

Each sheet in a data dictionary workbook becomes one inventory module.
Emits ``fields[]`` only — Excel is flat; ``types[]`` stays empty. For the
multi-sheet MITS-style enrichment shape (one sheet per type), use
``excel_multisheet`` and ``Inventory.enrich``.
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from cora_extractors import __version__
from cora_extractors._excel_io import (
    cell,
    coerce_cardinality,
    column_to_index,
    parse_enumeration,
    read_rows,
)
from cora_extractors.config import ExcelDictionaryConfig, ExtractorConfig
from cora_extractors.inventory import FieldEntry, Inventory
from cora_extractors.path import build as build_path

EXTRACTOR_ID = f"cora_extractors.excel_dictionary@{__version__}"


class ExcelDictionaryExtractor:
    """Extractor adapter for Excel data dictionaries."""

    name = "excel"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if not isinstance(config, ExcelDictionaryConfig):
            raise TypeError(
                "ExcelDictionaryExtractor.extract requires an ExcelDictionaryConfig"
            )

        rows = read_rows(source, config.sheet)
        body = rows[config.skip_rows :]
        fields = list(_iter_fields(body, config, source.name))

        return Inventory(
            standard=module or source.stem,
            module=module or source.stem,
            version="unknown",
            source_artifact=str(source),
            extractor=EXTRACTOR_ID,
            extracted_at=datetime.now(tz=UTC),
            namespace_hint=config.namespace_hint,
            source_label="excel",
            types=[],
            fields=fields,
        )


def _iter_fields(
    rows: list[list[Any]], config: ExcelDictionaryConfig, source_name: str
) -> Iterable[FieldEntry]:
    name_idx = column_to_index(config.field_name_column)
    type_idx = column_to_index(config.type_column) if config.type_column else None
    def_idx = column_to_index(config.definition_column) if config.definition_column else None
    card_idx = column_to_index(config.cardinality_column) if config.cardinality_column else None
    enum_idx = column_to_index(config.enumeration_column) if config.enumeration_column else None

    for row_offset, row in enumerate(rows):
        name = cell(row, name_idx)
        if not isinstance(name, str) or not name.strip():
            continue
        clean_name = name.strip()
        path = build_path([*config.path_prefix, clean_name])
        raw_type = cell(row, type_idx) if type_idx is not None else None
        raw_def = cell(row, def_idx) if def_idx is not None else None
        raw_card = cell(row, card_idx) if card_idx is not None else None
        raw_enum = cell(row, enum_idx) if enum_idx is not None else None

        # Excel rows are 1-indexed for humans; +1 for header skip recorded separately.
        sheet_row = config.skip_rows + row_offset + 1
        source_location = f"{source_name}!{config.sheet}!{sheet_row}"

        yield FieldEntry(
            path=path,
            range=str(raw_type).strip() if isinstance(raw_type, str) and raw_type else None,
            cardinality=coerce_cardinality(raw_card),
            definition=str(raw_def).strip() if isinstance(raw_def, str) else "",
            source_location=source_location,
            enumeration=parse_enumeration(raw_enum),
        )
