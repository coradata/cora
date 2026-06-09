# ADR-0001 — `Inventory.enrich` as a Separate Method, with In-Place Multi-Source Provenance

- **Date:** 2026-05-24
- **Status:** Accepted
- **Phase:** 3c (MITS Excel data-dictionary enrichment)

## Context

Phase 1 shipped `Inventory.merge(other, *, match_by)` as the seam for combining inventories. The intent at the time was that "merging a partial inventory into a fuller one is a property of the inventory type, not of any format." This anticipated Phase 3c's MITS XSD + Excel data dictionary combination.

In practice, Phase 3c surfaced that the symmetric `merge` API conflates two operations:

1. **Symmetric merge** — combining two inventories of equal authority (split-and-rejoin).
2. **Asymmetric enrichment** — filling in a primary inventory with a secondary source that doesn't have the same authority. MITS XSD enriched by Excel today; XSD enriched by PDF tomorrow; IBPDI JSON enriched by SQL DDL after that.

Concretely, the MITS Excel dictionary attests `range="Complex"` where XSD attests `range="AddressType"`, and attests `definition="An event in the lead lifecycle"` where XSD attests `definition="EventType"` (a degenerate placeholder where the only XSD annotation is the type name). Symmetric merge raises `MergeConflict` on either disagreement, but the right behaviour is asymmetric: keep XSD's `range`, let Excel's `definition` win.

Additionally, `merge`'s `match_by='name'` over-collapses fields sharing a leaf name across types — common in MITS, where `LastUpdateDate`, `Type`, and `Identification` appear under many parent types. Type-scoped matching `(domain, leaf-name)` is the precise key for enrichment, but unnecessary for symmetric merge.

A sidecar disagreements file (e.g., `<module>.disagreements.yaml`) was considered and rejected: drift risk between the inventory and its sidecar, two diffs per PR to scan, and the audit trail belongs with the data it documents.

## Decision

Add **`Inventory.enrich(other: Inventory, *, attributes: set[str]) -> Inventory`** as a separate method alongside `Inventory.merge`. See [CONTEXT.md](../../CONTEXT.md) for term definitions. The eight sub-decisions below define its semantics.

### 1. Two methods, not one with parameters

`merge` stays unchanged (symmetric, strict, raises on disagreement). `enrich` is its own method (asymmetric, permissive, never raises). Naming the operations separately keeps each interface honest about what it does, and lets a reader see "this is enrichment, not a merge" without inspecting parameters.

### 2. Hardcoded type-scoped matching

`enrich` always matches on `(field.domain, field.path.split("/")[-1])`. No `match_by` parameter. Sources that can't speak in terms of `(domain, leaf)` are not enriching — they're contributing new fields, which is what `merge` is for. This makes the contract clear: enrich = "fill in attributes on the field with this `(domain, leaf-name)`."

### 3. Trust list governs attribute flow

The `attributes: set[str]` parameter names which attributes the caller trusts `other` to attest on `self`'s fields. For listed attributes, `other` wins if attested. Unlisted attributes are untouched on `self` — `other`'s claims for them are ignored at the top level. Required at the call site; there is no default. Forcing the caller to declare trust is the right friction.

### 4. Provenance lives in the inventory YAML

When ≥2 sources attest a value for an attribute on a matched field, a `provenance` block is appended to the `FieldEntry`. Top-level attribute values remain simple-typed; the provenance block is the in-place audit trail. No sidecar file.

```yaml
- path: EventType
  domain: EventType
  range: EventType
  definition: "An event recorded in the lead lifecycle."
  source_location: Lead-Management-4.0.1-Schema-xsd.xml:146
  provenance:
    - attribute: definition
      claims:
        - source: xsd
          value: "EventType"
          location: Lead-Management-4.0.1-Schema-xsd.xml:146
        - source: excel
          value: "An event recorded in the lead lifecycle."
          location: Lead-Management-4.0-Data-Dictionary-xls.xls!Lead Management 4.0!23
      chosen: excel
```

### 5. Provenance recorded always-when-multi-source

Provenance is recorded whenever ≥2 sources attested — agreement or disagreement, trusted attribute or not. This makes the YAML a full lineage record: a reviewer can diff two regenerations and see "Excel changed its claim about `range`" even though `range` isn't in the trust list. Files can be pruned later if they bloat; we can't reconstruct discarded provenance.

### 6. `chosen` field present iff claims disagree

Within a provenance block, `chosen: <source>` names whichever source's value lives at the top level. Present only when claims disagree; absent when all claims agree (no decision was needed). The rule: **`chosen` is present iff claims disagree, and it names whichever source's value lives at the top level.** No `reason` field — the trust list lives on the `enrich` call, not in every YAML row.

### 7. Source label on the `Inventory` itself

A new optional `source_label: str` field on `Inventory` carries the short label (`"xsd"`, `"excel"`, etc.). Extractors set it at construction time. Carrying it on the data (rather than at the call site or by parsing the `extractor` string) means the same inventory reports the same label in every merge it participates in. One source of truth per inventory file.

### 8. Unmatched-other audit in the inventory

`other.fields` rows whose `(domain, leaf-name)` find no match in `self` are dropped from `fields` and recorded in a top-level `unmatched_enrichments` list on the merged inventory:

```yaml
unmatched_enrichments:
  - source: excel
    domain: SomeType
    field: SomeField
    location: Lead-Management-4.0-Data-Dictionary-xls.xls!Person Type!42
```

Reviewers see typos and sheet-mapping mistakes in the YAML diff; no separate report file.

## Consequences

- **Phase 1 schema gains optional fields**: `Inventory.source_label`, `Inventory.unmatched_enrichments[]`, `FieldEntry.provenance[]`. All additive; pre-Phase-3c inventories stay valid against the schema.
- **`Inventory.merge` is unchanged.** All Phase 1/2/3 tests survive.
- **New caller surface**: `cora inventory merge --into A.yaml --from B.yaml --attribute definition --attribute enumeration --output M.yaml`.
- **Future enrichment sources** (PDF, SQL DDL) use the same primitive. Each new source gets a `source_label`; provenance accumulates claims across all sources that have attested.
- **YAML inflation risk acknowledged.** Provenance may bloat inventory files. If files become unwieldy, we can scope provenance down to trusted attributes only (a future, narrower ADR). Comprehensive view first, prune later if needed.
- **Excel extractor no longer carries policy.** The Phase 2 design considered baking "Excel emits only definition + enumeration" into the extractor. With `enrich`'s trust list, the policy lives at the call site where it belongs; the extractor emits everything it can read.

## Alternatives considered

- **Symmetric merge with attribute filter** — make `Inventory.merge` accept an `attributes` parameter to filter what flows. Rejected: makes one method do two semantically distinct jobs; the interface stops being honest.
- **Sidecar disagreements file (`<module>.disagreements.yaml`)** — keep working values clean; record disagreements externally. Rejected: drift risk between inventory and sidecar; two diffs per PR; provenance belongs with the data.
- **Halt on every disagreement** (current `merge` behaviour applied to enrichment) — estimated 50–200 disagreements per MITS module from a quick scan; halt-and-fix would block the build at every regeneration.
- **Fill-gaps-only semantics** — `enrich` only writes where `self` is unattested; never overwrites. Rejected: XSD placeholders like `definition="EventType"` are technically attested but degenerate, so they'd block Excel's real prose. Would require a per-attribute "degenerate value" heuristic, which is fuzzy and project-specific.
- **Per-attribute win policy** — separate `prefer_other` / `prefer_self` lists. Rejected: too many knobs; the trust list already captures the intent.
- **Provenance scoped to trust list only** — record only claims for attributes in `attributes`. Rejected: loses the diff-trail for ignored claims; "Excel changed its mind about `range`" is reviewable signal even when `range` isn't trusted.

## References

- [cora/CONTEXT.md](../../CONTEXT.md) — vocabulary
- [cora/docs/field-inventory.md](../field-inventory.md) — inventory contract
- [cora/docs/site/docs/inventory-operations.md](../site/docs/inventory-operations.md) — `merge` vs `enrich` for consumers
