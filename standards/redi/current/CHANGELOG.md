# REDI — CORA mirror changelog

## 2026-05-23 — First field inventory extracted

`REDI Data Fields` sheet extracted to `inventory/data-fields.yaml` via the Phase 2 Excel data-dictionary extractor (`cora_extractors.excel_dictionary@0.0.0`) with `tools/extractors/configs/redi-data-fields.yaml`. 373 fields, no class hierarchy (Excel is flat). Paths are slugified from the source labels — human-readable names like `Number of Shares/ Units` canonicalise to `Number_of_Shares_Units`; the original label is preserved in `definition`.

The `REDI Lists` sheet is **not yet extracted**. It is a vocabulary (one row per enum value, grouped by list name), not a field catalog, and does not map cleanly onto `FieldEntry`. Deferred until the inventory model grows a vocabulary/enumeration-catalog shape (or the Excel extractor learns a "group by" mode). See the field-inventory plan for status.

## 2026-05-21 — Initial mirror

Initial mirror of the REDI Data Model from the REDI Data Model Sub-Committee under permission from the owner.

- Source: https://realestatedatainitiative.netlify.app/
- Upstream version: 1.0
- Upstream modification date: 2026-02-05
- CORA mirror date: 2026-05-21
- Tier: participating

Native files mirrored bit-identically from the upstream distribution. No derivations yet; native-only mirror.

Included artifact:

- `REDI Data Model 1.0.xlsx` — three-sheet workbook (Guide, REDI Data Fields, REDI Lists) with vehicle-scope flags (OEF NA/APAC/EU, SMA Global, CEF Global) and native cross-mappings to NCREIF/PREA Reporting Standards and INREV.
