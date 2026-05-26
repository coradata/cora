# CORA Domain Vocabulary

Canonical glossary for terms used across the CORA codebase, plans, and ADRs. If a term in code or docs disagrees with this file, the disagreement is a bug worth fixing.

Architectural vocabulary (module, seam, adapter, depth, etc.) lives in the `improve-codebase-architecture` skill; this file covers the **domain** terms.

---

## Core artifacts

- **Standard** — A real-estate data standard hosted in CORA (e.g., MITS, IBPDI, REDI). Lives under `standards/<std>/`.
- **Module** — A subdivision of a standard, typically one schema file or one workbook sheet (e.g., MITS Lead-Management, REDI data-fields). The unit of inventory extraction.
- **Native artifact** — The original source file shipped by a standard's authoring body (XSD, JSON Schema, Excel data dictionary, PDF, SQL DDL).
- **Inventory** — A normalized YAML representation of one module's fields and types. The substrate crosswalks reference; the input to OWL projection. Lives at `standards/<std>/current/inventory/<module>.yaml`.
- **Field** — A leaf concept in an inventory (a record property). Has a `path`, optional `concept_id`, `domain`, `range`, `cardinality`, `definition`, etc.
- **Type** — A class concept in an inventory. Has a `name`, optional `extends`, `abstract`, `definition`.
- **Path** — Canonical address of a field within an inventory, e.g. `PersonType/Identification/IDValue`. Constructed and parsed through `cora_extractors.path`.
- **Crosswalk** — A YAML at `crosswalks/concepts/<concept>.yaml` mapping one canonical concept to per-standard inventory paths.

## Seams

- **Extractor** — Protocol (`cora_extractors.extractor`) whose adapters take a native artifact and produce an `Inventory`. Adapters today: `xsd`, `json_catalog`, `cdm_json`, `excel_dictionary`, (Phase 3c) `excel_multisheet`.
- **Validator** — Protocol (`cora_extractors.validator`) whose adapters check committed artifacts and report findings. Adapters: `inventory_schema`, `field_count`, (Phase 4) `crosswalk_paths`.
- **Generator** — (Phase 4.5) Protocol whose adapters read inventories + crosswalks and produce browseable Markdown.

## Inventory operations

- **Merge** — `Inventory.merge(other, *, match_by)`. Symmetric combination of two inventories of equal authority. Raises `MergeConflict` on any attested disagreement. Used when combining two halves of the same conceptual source.
- **Enrich** — `Inventory.enrich(other, *, attributes)`. Asymmetric fill-in from a secondary source. `self` is authoritative; `other` contributes values for the named attributes only. Matches on `(domain, leaf-name)`. Never raises. Used when a secondary artifact (Excel data dictionary, future PDF, future SQL DDL) adds detail to a primary inventory. See [ADR-0001](docs/adr/0001-enrich-vs-merge.md).

## Audit trail (multi-source provenance)

- **Provenance** — Optional list on each `FieldEntry` recording multi-source attestations. Present whenever ≥2 sources attested a value for an attribute; absent for single-source attestations (the common case). Lets reviewers see the full lineage of a merged value in the inventory YAML itself, with no sidecar.
- **Claim** — A single source's attestation of a value: `{source, value, location}`. A `provenance[].claims[]` list contains every claim, including untrusted ones — the trust list controls what wins at the top level, not what's recorded.
- **Chosen** — Within a provenance entry, the source label whose value lives at the top level. Present only when claims disagree; absent when claims agree (no decision was needed).
- **Source label** — Short stable identifier per `Inventory` (`"xsd"`, `"excel"`, `"pdf"`, etc.). Set by the extractor at construction time and carried on the `Inventory` itself, so the same inventory reports the same label everywhere it appears.
- **Trust list** — The `attributes: set[str]` parameter to `Inventory.enrich`. Says which attributes the caller trusts `other` to attest on `self`'s fields. Untrusted claims are still recorded in provenance (so the YAML diff shows them) but never overwrite top-level values.
- **Unmatched enrichments** — Top-level list on the merged `Inventory` recording `other` fields whose `(domain, leaf-name)` found no match in `self`. Lets reviewers spot typos and sheet-mapping errors in the YAML diff without polluting `fields`.

## Confidence vocabulary (crosswalks)

- **exact** — The mapping is verbatim. Same field name, same semantics, same cardinality.
- **close** — Same concept, minor differences (units, formatting, optional vs required).
- **partial** — Same concept, meaningful differences in scope or definition.
- **divergent** — Same word, different concept. Requires narrative `notes`.
- **not_present** — Concept does not exist in this standard. Requires narrative `notes`.
