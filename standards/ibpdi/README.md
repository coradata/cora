# IBPDI Common Data Model

This directory holds CORA's bootstrap mirror of the [IBPDI Common Data Model](https://github.com/ibpdi/cdm), the open-source Common Data Model for Real Estate developed by the International Building Performance & Data Initiative.

**Why this is here.** IBPDI publishes its CDM under CC BY 4.0 (docs) + MIT (code) on GitHub. This means CORA can mirror it without requiring upstream permission, giving the repository immediate concrete content. IBPDI is the bootstrap mirror, not a participating standards body in CORA governance. The relationship may evolve over time.

**Attribution.** All credit for the CDM goes to IBPDI and its contributors (Microsoft, RICS, BuildingMinds, pom+, and others). The license files at `LICENSE-CDM-Docs` and `LICENSE-CDM-Code` carry the upstream terms.

**Provenance.** See [PROVENANCE.yaml](PROVENANCE.yaml) for the upstream commit SHA, fetch date, and license metadata for the current mirrored version.

**Canonical source.** The authoritative IBPDI CDM lives at [github.com/ibpdi/cdm](https://github.com/ibpdi/cdm). CORA mirrors. CORA does not author.

## Documentation

- **Concepts and CLI** — [coradata.github.io/cora](https://coradata.github.io/cora/) (authored docs site)
- **Browse IBPDI inventories** — [`docs/generated/inventories/ibpdi/`](../../docs/generated/) (one Markdown per cluster)
- **Concept crosswalks** — [`docs/generated/coverage-matrix.md`](../../docs/generated/coverage-matrix.md)

## Layout

```
/standards/ibpdi/
  PROVENANCE.yaml          # source metadata
  LICENSE-CDM-Docs         # upstream CC BY 4.0
  LICENSE-CDM-Code         # upstream MIT
  /current/
    /native/               # bit-identical mirror of upstream
    /ontology/             # OWL/RDF derivation (pending Pillar 1 tooling)
    /jsonld/               # JSON-LD context (pending)
    /jsonschema/           # JSON Schema (pending)
```

Derivations (ontology, JSON-LD, JSON Schema) ship when the derivation pipeline is operational. Until then, only the native mirror is present.
