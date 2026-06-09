# Drift Register

The drift register tracks two kinds of divergence:

- **Intra-standard drift.** A field or relationship that changed meaning between two versions of the same standard.
- **Inter-standard drift.** Two hosted standards that name the same concept differently or define it incompatibly.

## Taxonomy

| Category | Description |
|---|---|
| `rename` | Same concept, different name |
| `scope_change` | Definition's scope expanded or narrowed |
| `type_change` | Underlying data type changed |
| `cardinality_change` | Relationship changed (e.g., 1:1 to 1:many) |
| `enumeration_change` | Allowed values added, removed, or redefined |
| `semantic_redefinition` | Meaning shifts even where structure does not |

Resolution of any drift entry is the standards bodies' decision, not CORA's. The register surfaces; it does not arbitrate.

This directory is currently empty. Entries land as cross-version or cross-standard comparisons are authored — until then, the taxonomy above is the contract for what the register will contain. Inter-standard divergences are partially documented today in the per-crosswalk `notes` blocks under [`crosswalks/concepts/`](../crosswalks/concepts/) (see, for example, the `divergent` mappings on `rent_amount` and `market_rent`); the drift register is the consolidated view of those entries plus intra-standard version-bump deltas.
