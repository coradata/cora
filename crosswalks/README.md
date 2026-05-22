# Crosswalks

Cross-standard mappings between concepts. Each crosswalk records:

- The canonical concept name and a working definition
- Field-level mappings from each hosted standard, with version and source location
- A confidence score per mapping: `exact`, `close`, `partial`, or `divergent`
- A written narrative for any `divergent` mapping

The `field` value in each `mappings.<standard>` block is an inventory `path` — see [`docs/field-inventory.md`](../docs/field-inventory.md) for the path grammar and where inventories live. Crosswalks should reference paths that resolve against the standard's committed inventory; the crosswalk-paths validator (Phase 4 of the inventory plan) enforces this in CI.

Layout:

```
/crosswalks/
  /concepts/            # one YAML file per concept
  /schema/              # JSON Schema defining crosswalk YAML format
  /graph/               # RDF/SKOS and JSON graph derivations
  taxonomy.md           # crosswalk vocabulary
```

## Boundary crosswalks

A subset of crosswalks connects CORA's corpus to adjacent ontologies that CORA deliberately does not host (MISMO mortgage operations, RealEstateCore building systems, OSI analytics conventions). These are flagged with `boundary: true` in the YAML and live under `concepts/` with the rest.
