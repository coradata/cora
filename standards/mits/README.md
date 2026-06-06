# MITS — Multifamily Information & Transactions Standards

This directory holds CORA's mirror of [MITS](https://rettc.org/mits-data-models), the Multifamily Information & Transactions Standards published by the Real Estate Technology & Transaction Standards Consortium (RETTC). MITS defines XSD/XML schemas for lead management, lease applications, resident screening, resident transactions, accounts payable, property marketing (ILS), and supporting core data.

**Why this is here.** MITS is mirrored in CORA with permission from RETTC. MITS is onboarded as a participating standards body.

**Attribution.** All credit for MITS goes to RETTC and the multifamily working groups that author and maintain it. See [PROVENANCE.yaml](PROVENANCE.yaml) for license terms and attribution requirements.

**Provenance.** See [PROVENANCE.yaml](PROVENANCE.yaml) for the distribution URL, fetch date, and license metadata.

**Canonical source.** The authoritative MITS distribution lives at [rettc.org/mits-data-models](https://rettc.org/mits-data-models). CORA mirrors. CORA does not author. Native files are kept bit-identical to the upstream distribution — no structural changes.

## Documentation

- **Concepts and CLI** — [coradata.github.io/cora](https://coradata.github.io/cora/) (authored docs site)
- **Browse MITS inventories** — [`docs/generated/inventories/mits/`](../../docs/generated/) (one Markdown per module)
- **Concept crosswalks** — [`docs/generated/coverage-matrix.md`](../../docs/generated/coverage-matrix.md)

## Layout

```
/standards/mits/
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

- `Core-Data-4.0.xml` — shared core data types
- `Collections-Schema-Version-3.0-xsd.xml` — collections schema
- `Lease-Application-Standard-xsd.xml` — lease application standard
- `Property-Marketing-ILS-5.0 Data Dictionary.xlsx` — ILS 5.0 data dictionary
- `5.0-Supporting-Documentation/` — ILS 5.0 fee transparency model, diagrams, test files
- `Accounts-Payable-4.0/` — schema + data dictionary
- `Lead-Management-4.0/` — schemas (4.0 and 4.0.1), data dictionary, supplemental docs
- `Property-Marketing-ILS-5.0-XSD-with-CORE/` — ILS 5.0 XSD bundle with Core-Data-4.0 and the MITS custom extension
- `Resident-Screening-3.0/` — schema, data dictionary, PDF reference
- `Resident-Transactions-3.0/` — schema, data dictionary, PDF reference

Derivations (ontology, JSON-LD, JSON Schema) ship when the derivation pipeline is operational. Until then, only the native mirror is present.
