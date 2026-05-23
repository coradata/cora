# IBPDI CDM — CORA mirror changelog

## 2026-05-23 — Field inventories extracted (seven clusters)

All seven core CDM clusters extracted via a new Microsoft-CDM-JSON-shaped extractor adapter (`cora_extractors.cdm_json@0.0.0`). Each cluster's `*.manifest.cdm.json` is the input; the extractor walks every `LocalEntity` reference, opens its `.cdm.json`, and emits the entities and attributes.

| Cluster | Types | Fields |
|---|---|---|
| digital-twin | 140 | 1,409 |
| energy-and-resources | 21 | 90 |
| financials | 12 | 45 |
| organisational-management | 39 | 131 |
| portfolio-and-asset-management | 11 | 61 |
| property-management | 13 | 59 |
| user-and-customer-experience | 20 | 57 |

Total IBPDI coverage: **7 modules / 256 types / 1,852 fields**.

**Coverage notes.**

- Every IBPDI entity nominally `extendsEntity: CdmEntity`. CdmEntity is the Microsoft CDM framework base type, defined outside this corpus. The extractor records the reference faithfully; the inventory's `Inventory.external_references()` lists each such pointer for informational reporting.
- `hasAttributes[]` entries of shape `{attributeGroupReference: "..."}` are not expanded in v1 of the CDM-JSON extractor. Expanding them requires walking CDM imports (`_allImports.cdm.json` and the foundations import) and resolving the group definitions. Deferred to a future phase; the unresolved references mean some shared groups (Audit, Name, ValidityInfo) currently contribute no fields to entity inventories that use them.
- Inheritance depth shows as 0 for every cluster because every type extends `CdmEntity` (one level), and `CdmEntity` is not in the inventory — so the chain depth-counter walks 0 hops. When IBPDI entities extend each other (e.g., a `Building` extending an `Asset`), depth will surface those chains.

## 2026-05-17 — Bootstrap mirror

Initial mirror of IBPDI Common Data Model from upstream SHA `12afb170c8d3a65897bf49234d6e12acb96fe949`.

- Source: https://github.com/ibpdi/cdm
- Upstream commit date: 2024-06-10T11:12:27+02:00
- CORA mirror date: 2026-05-17

No derivations yet; native-only mirror.
