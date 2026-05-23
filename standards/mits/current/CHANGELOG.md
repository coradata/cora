# MITS — CORA mirror changelog

## 2026-05-23 — Remaining six module inventories extracted

The six MITS modules that reference Core-Data via canonical NMHC URLs (the ones deferred from the prior entry) now ship inventories:

| Module | Types | Fields (datatype / object) | Source |
|---|---|---|---|
| Collections 3.0 | 33 | 174 (133 / 41) | `Collections-Schema-Version-3.0-xsd.xml` |
| Lease-Application | 67 | 266 (179 / 87) | `Lease-Application-Standard-xsd.xml` |
| Lead-Management 4.0.1 | 28 | 136 (109 / 27) | `Lead-Management-4.0/Lead-Management-4.0.1-Schema-xsd.xml` |
| Resident-Screening 3.0 | 22 | 102 (79 / 23) | `Resident-Screening-3.0/Resident-Screening-3.0-xsd.xml` |
| Resident-Transactions 3.0 | 24 | 135 (112 / 23) | `Resident-Transactions-3.0/Resident-Transactions-Schema-Version-3.0-xsd1.xml` |
| Accounts-Payable 4.0 | 28 | 124 (99 / 25) | `Accounts-Payable-4.0/Accounts-Payable-4.0-xsd.xml` |

All six were extracted via the Phase 2 XSD extractor using new `XsdConfig.include_remap` (introduced in this PR) to redirect the remote `http://www.nmhc.info/MITS/MITSCoreData30.xsd` and `http://www.nmhc.info/MITS/MITSCustomExtension.xsd` URLs to the local files shipped in `Property-Marketing-ILS-5.0-XSD-with-CORE/`. Per-module configs live at `tools/extractors/configs/mits-<module>.yaml`.

**Best-effort substitution.** The older modules nominally reference Core-Data 3.0; we substitute Core-Data 4.0 (the locally-available version). Most shared type names (PropertyType, AddressType, CompanyType, etc.) exist in both, but a few were renamed between versions — notably `IdentificationType` became `Identification`. Affected `extends` and object-reference `range` values are recorded honestly as **external references** (visible via `cora_extractors.inventory.Inventory.external_references()`) rather than silently rewritten. Those references will resolve cleanly when Core-Data 3.0 is added to the corpus.

**Excel data-dictionary enrichment is not yet applied.** Definitions for these inventories are XSD-sourced only (mostly the schema's `xs:annotation/xs:documentation` text, which is sparse). The Excel data dictionaries for Lead-Management, Resident-Screening, Resident-Transactions, and Accounts-Payable use a multi-sheet shape (one sheet per type) that the current Excel extractor doesn't handle. Phase 3c in the field-inventory plan picks up that work.

## 2026-05-23 — First field inventory extracted

Property-Marketing-ILS-5.0 module extracted to `inventory/property-marketing.yaml` via the Phase 2 XSD extractor (`cora_extractors.xsd@0.0.0`). 38 types, 191 fields (163 datatype properties, 28 object references), max inheritance depth 2.

Property-Marketing was selected first because its XSD bundle (`Property-Marketing-ILS-5.0-XSD-with-CORE/`) ships Core-Data and the custom extension as local files — no remote `xs:include` resolution needed.

## 2026-05-21 — Initial mirror

Initial mirror of MITS data models from RETTC under permission from the owner.

- Source: https://rettc.org/mits-data-models
- CORA mirror date: 2026-05-21
- Tier: participating

Native files mirrored bit-identically from the upstream distribution. No derivations yet; native-only mirror.

Included modules:

- Core-Data 4.0
- Collections 3.0
- Lease Application
- Property Marketing ILS 5.0 (XSD bundle with Core-Data 4.0, custom extension, supporting docs, data dictionary)
- Accounts Payable 4.0
- Lead Management 4.0 and 4.0.1
- Resident Screening 3.0
- Resident Transactions 3.0
