"""Multi-sheet MITS Excel data-dictionary extractor adapter.

A MITS data-dictionary workbook contains one "top" sheet describing the
module tree and one sheet per shared type (``PersonType``, ``AddressType``,
``IdentificationType``, etc.). This adapter walks the *type* sheets and
emits per-field rows with ``domain`` set to the sheet's mapped type name,
so the resulting inventory can be fed into ``Inventory.enrich`` against an
XSD-derived inventory using type-scoped ``(domain, leaf)`` matching.

The top sheet is **not** processed: the XSD extractor does not currently
model the module's element tree as a named type, so top-sheet rows would
all land in ``unmatched_enrichments``. Promoting the module-tree to a
synthetic type is a future deepening; for now the loss is documented in
the config and the PR notes.

Convention-driven layout. The extractor scans the first few rows of each
type sheet for a header row whose column-A cell matches ``header_marker``
(default ``"Common Root Element"``). The hierarchy depth (number of
``"Child Element/Attribute"`` columns) is then inferred by counting; the
field name on each data row is the rightmost non-empty hierarchy cell.
Defaults match MITS dictionaries shipped 2021–2024.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from cora_extractors import __version__
from cora_extractors._excel_io import (
    cell,
    coerce_cardinality,
    parse_enumeration,
    read_rows,
)
from cora_extractors.config import (
    ExcelMultiSheetDictionaryConfig,
    ExtractorConfig,
)
from cora_extractors.inventory import FieldEntry, Inventory
from cora_extractors.path import build as build_path

EXTRACTOR_ID = f"cora_extractors.excel_multisheet@{__version__}"


class ExcelMultiSheetDictionaryExtractor:
    """Extractor adapter for multi-sheet MITS Excel data dictionaries."""

    name = "excel-multisheet"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if not isinstance(config, ExcelMultiSheetDictionaryConfig):
            raise TypeError(
                "ExcelMultiSheetDictionaryExtractor.extract requires an "
                "ExcelMultiSheetDictionaryConfig"
            )

        all_fields: list[FieldEntry] = []
        for sheet_name, target_type in config.type_sheets.items():
            rows = read_rows(source, sheet_name)
            layout = _detect_layout(rows, sheet_name, config)
            all_fields.extend(
                _extract_sheet_fields(
                    rows=rows,
                    layout=layout,
                    target_type=target_type,
                    sheet_name=sheet_name,
                    source_name=source.name,
                )
            )

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
            fields=all_fields,
        )


class _SheetLayout:
    """Resolved column positions for one type sheet.

    ``has_root_column`` distinguishes the two MITS dictionary conventions:

    - Lead-Management / Resident-* style: header row has ``Common Root Element``
      in column A followed by N ``Child Element/Attribute`` columns. Column A
      carries the parent type's context; depth-0 rows describe the type itself
      and are skipped.
    - Accounts-Payable style: header row at row 0 with consecutive
      ``Child Element/Attribute`` columns, no root context. All hierarchy
      columns hold field-level names; depth-0 rows are direct fields on the
      target type (except the type-name row, which is filtered by leaf-name).
    """

    __slots__ = (
        "header_row",
        "hierarchy_columns",
        "has_root_column",
        "description_idx",
        "data_type_idx",
        "required_idx",
        "max_occurs_idx",
        "values_idx",
    )

    def __init__(
        self,
        header_row: int,
        hierarchy_columns: list[int],
        has_root_column: bool,
        description_idx: int | None,
        data_type_idx: int | None,
        required_idx: int | None,
        max_occurs_idx: int | None,
        values_idx: int | None,
    ) -> None:
        self.header_row = header_row
        self.hierarchy_columns = hierarchy_columns
        self.has_root_column = has_root_column
        self.description_idx = description_idx
        self.data_type_idx = data_type_idx
        self.required_idx = required_idx
        self.max_occurs_idx = max_occurs_idx
        self.values_idx = values_idx


def _detect_layout(
    rows: list[list[Any]],
    sheet_name: str,
    config: ExcelMultiSheetDictionaryConfig,
) -> _SheetLayout:
    """Find the header row and column positions in a type sheet."""
    root_marker = config.header_marker
    child_marker = config.hierarchy_marker

    header_row: int | None = None
    has_root_column = False
    for r in range(min(config.header_search_rows, len(rows))):
        col_a = cell(rows[r], 0)
        if not isinstance(col_a, str):
            continue
        col_a = col_a.strip()
        if col_a == root_marker:
            header_row = r
            has_root_column = True
            break
        if col_a == child_marker:
            header_row = r
            has_root_column = False
            break
    if header_row is None:
        raise ValueError(
            f"sheet {sheet_name!r}: header row not found in first "
            f"{config.header_search_rows} rows (expected column A to equal "
            f"{root_marker!r} or {child_marker!r})"
        )

    header = rows[header_row]
    hierarchy_columns: list[int] = [0]
    for col_idx in range(1, len(header)):
        v = cell(header, col_idx)
        if isinstance(v, str) and v.strip() == child_marker:
            hierarchy_columns.append(col_idx)
        else:
            break

    def _find(name: str) -> int | None:
        for col_idx in range(len(header)):
            v = cell(header, col_idx)
            if isinstance(v, str) and v.strip() == name:
                return col_idx
        return None

    return _SheetLayout(
        header_row=header_row,
        hierarchy_columns=hierarchy_columns,
        has_root_column=has_root_column,
        description_idx=_find(config.description_column_name),
        data_type_idx=_find(config.data_type_column_name),
        required_idx=_find(config.required_column_name),
        max_occurs_idx=_find(config.max_occurs_column_name),
        values_idx=_find(config.values_column_name),
    )


def _extract_sheet_fields(
    *,
    rows: list[list[Any]],
    layout: _SheetLayout,
    target_type: str,
    sheet_name: str,
    source_name: str,
) -> list[FieldEntry]:
    """Emit one FieldEntry per data row whose leaf hierarchy cell is non-empty."""
    out: list[FieldEntry] = []
    for r in range(layout.header_row + 1, len(rows)):
        row = rows[r]
        leaf = _rightmost_non_empty(row, layout.hierarchy_columns)
        if leaf is None:
            continue
        # In root-column layouts (Lead-Management style), depth 0 is the
        # type-context cell, not a field. In flat layouts (Accounts-Payable
        # style), depth 0 is a direct field.
        if layout.has_root_column and _row_depth(row, layout.hierarchy_columns) == 0:
            continue
        # Skip the row whose leaf is the target type's own name (a type-level
        # header found inside the data area in flat layouts).
        if leaf == target_type:
            continue

        raw_def = cell(row, layout.description_idx) if layout.description_idx is not None else None
        raw_type = cell(row, layout.data_type_idx) if layout.data_type_idx is not None else None
        raw_req = cell(row, layout.required_idx) if layout.required_idx is not None else None
        raw_max = cell(row, layout.max_occurs_idx) if layout.max_occurs_idx is not None else None
        raw_vals = cell(row, layout.values_idx) if layout.values_idx is not None else None

        # Cardinality combines Req (Y/N) and Max occurs ('Unbounded' or > 1 → repeating)
        cardinality = _combine_cardinality(raw_req, raw_max)

        out.append(
            FieldEntry(
                path=build_path([target_type, leaf]),
                domain=target_type,
                range=str(raw_type).strip() if isinstance(raw_type, str) and raw_type else None,
                cardinality=cardinality,
                definition=str(raw_def).strip() if isinstance(raw_def, str) else "",
                source_location=f"{source_name}!{sheet_name}!{r + 1}",
                enumeration=parse_enumeration(raw_vals),
            )
        )
    return out


def _rightmost_non_empty(row: list[Any], columns: list[int]) -> str | None:
    """Return the value of the last non-empty hierarchy cell, or None."""
    for col_idx in reversed(columns):
        v = cell(row, col_idx)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def _row_depth(row: list[Any], columns: list[int]) -> int:
    """Return the 0-indexed depth of the rightmost non-empty hierarchy cell."""
    for offset, col_idx in enumerate(reversed(columns)):
        v = cell(row, col_idx)
        if isinstance(v, str) and v.strip():
            return len(columns) - 1 - offset
    return -1


def _combine_cardinality(raw_req: Any, raw_max: Any) -> Any:
    """Merge a Req (Y/N) and a Max occurs cell into a canonical cardinality.

    'Unbounded' or a numeric > 1 in Max occurs → 'repeating'; else fall
    through to the Req column's normal coercion.
    """
    if isinstance(raw_max, str) and raw_max.strip().lower() == "unbounded":
        return "repeating"
    if isinstance(raw_max, int | float) and raw_max > 1:
        return "repeating"
    if isinstance(raw_max, str):
        try:
            if float(raw_max.replace(",", "").strip()) > 1:
                return "repeating"
        except (ValueError, AttributeError):
            pass
    return coerce_cardinality(raw_req)
