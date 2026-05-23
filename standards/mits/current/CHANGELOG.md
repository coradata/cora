# MITS — CORA mirror changelog

## 2026-05-23 — First field inventory extracted

Property-Marketing-ILS-5.0 module extracted to `inventory/property-marketing.yaml` via the Phase 2 XSD extractor (`cora_extractors.xsd@0.0.0`). 38 types, 191 fields (163 datatype properties, 28 object references), max inheritance depth 2.

Property-Marketing was selected first because its XSD bundle (`Property-Marketing-ILS-5.0-XSD-with-CORE/`) ships Core-Data and the custom extension as local files — no remote `xs:include` resolution needed. The six remaining MITS modules (Lead-Management, Resident-Screening, Resident-Transactions, Lease-Application, Collections, Accounts-Payable) reference Core-Data via the canonical NMHC URL and are deferred to a follow-up (Phase 3b in the field-inventory plan), which adds `XsdConfig.include_remap` to redirect remote URLs to local files.

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
