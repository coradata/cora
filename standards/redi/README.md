# REDI — Real Estate Data Initiative Data Model

This directory holds CORA's mirror of the [REDI Data Model](https://realestatedatainitiative.netlify.app/), the LP-led data standard published by the REDI Data Model Sub-Committee. REDI defines a structured set of data fields, lists, and metadata for institutional real estate investment reporting across fund vehicles (open-end North America, APAC, EU; separately managed accounts; closed-end funds), with explicit cross-mappings to the NCREIF/PREA Reporting Standards and INREV.

**Why this is here.** REDI is mirrored in CORA with permission from the REDI Data Model Sub-Committee. REDI is onboarded as a participating standards body.

**Attribution.** All credit for REDI goes to the REDI Data Model Sub-Committee and the limited partners and contributing organizations that author and maintain it. See [PROVENANCE.yaml](PROVENANCE.yaml) for license terms and attribution requirements.

**Provenance.** See [PROVENANCE.yaml](PROVENANCE.yaml) for the distribution URL, upstream version, and license metadata.

**Canonical source.** The authoritative REDI distribution lives at [realestatedatainitiative.netlify.app](https://realestatedatainitiative.netlify.app/). CORA mirrors. CORA does not author. Native files are kept bit-identical to the upstream distribution — no structural changes.

## Documentation

- **Concepts and CLI** — [coradata.github.io/cora](https://coradata.github.io/cora/) (authored docs site)
- **Browse REDI inventory** — [`docs/generated/inventories/redi/data-fields.md`](../../docs/generated/inventories/redi/data-fields.md)
- **Concept crosswalks** — [`docs/generated/coverage-matrix.md`](../../docs/generated/coverage-matrix.md)

## Layout

```
/standards/redi/
  PROVENANCE.yaml          # source metadata
  /current/
    CHANGELOG.md           # mirror history
    /native/               # bit-identical mirror of upstream distribution
    /ontology/             # OWL/RDF derivation (pending Pillar 1 tooling)
    /jsonld/               # JSON-LD context (pending)
    /jsonschema/           # JSON Schema (pending)
```

## Native contents

The current native mirror includes:

- `REDI Data Model 1.0.xlsx` — the REDI Data Model 1.0 workbook, containing three worksheets:
  - **Guide** — metadata definitions, data type reference, and usage notes for end users
  - **REDI Data Fields** — all REDI data fields with type, domain/sub-domain, descriptions, vehicle scope (OEF NA/APAC/EU, SMA Global, CEF Global), and cross-references to NCREIF/PREA Reporting Standards and INREV
  - **REDI Lists** — the structured value lists used by `List`-typed fields in the data model

## Cross-standard references

REDI ships with native mappings to:

- **NCREIF / PREA Reporting Standards** — including the NPI Submission Template, the NCREIF Fund Submission Template, the NCREIF/CREFC Debt Fund Aggregate Report, and the Reporting Standards Manuals.
- **INREV** — mapped to INREV standards by INREV.

These are preserved in the native workbook. Once NCREIF/PREA and INREV are onboarded into CORA, these mappings will inform the crosswalks under [`/crosswalks/`](../../crosswalks/).

Derivations (ontology, JSON-LD, JSON Schema) ship when the derivation pipeline is operational. Until then, only the native mirror is present.
