# Field Inventory

## What it is

A **field inventory** is a normalized, deterministic, diffable extraction of every addressable field in one module of a hosted standard. Each hosted standard publishes its native artifact (XSD, JSON manifest, Excel data dictionary, ...); the field inventory is the format-agnostic representation that the rest of CORA reads from.

Inventories are the substrate that:

- **Crosswalks** reference. Every `mappings.<standard>.field` in a `crosswalks/concepts/*.yaml` is an inventory `path`.
- **The drift register** diffs. Inventory YAML diffs cleanly between versions, so renames, type changes, and cardinality changes are mechanically detectable.
- **The OWL/RDF derivation pipeline** projects from. The inventory's `types[]`, `domain`, `range`, and `is_reference` fields are OWL-aware so the future pipeline is a projection, not a redesign.

## Where they live

```
standards/<std>/current/inventory/<module>.yaml
```

One file per module. MITS has 8 modules; IBPDI has cluster modules; REDI ships two (`data-fields`, `lists`). Per-module files diff cleanly and stay reviewable.

## The contract

The wire format is JSON Schema. See [`tools/extractors/schema/inventory.schema.json`](../tools/extractors/schema/inventory.schema.json). The in-process interface is the typed [`cora_extractors.inventory`](../tools/extractors/src/cora_extractors/inventory.py) module — `Inventory`, `FieldEntry`, `TypeEntry` pydantic models. Two example fixtures live alongside:

- [`tools/extractors/fixtures/inventory-with-types.yaml`](../tools/extractors/fixtures/inventory-with-types.yaml) — full OWL-aware shape, mirrors what the XSD extractor produces
- [`tools/extractors/fixtures/inventory-flat.yaml`](../tools/extractors/fixtures/inventory-flat.yaml) — fields-only, no types, mirrors what an Excel-primary extraction produces

### Top level

| Key | Required | Description |
|---|---|---|
| `standard` | yes | Short identifier of the standard (e.g. `mits`, `ibpdi`, `redi`) |
| `module` | yes | Module name within the standard |
| `version` | yes | Version label of the source artifact |
| `source_artifact` | yes | Repo-relative path or URL of the native artifact |
| `extractor` | yes | `module.name@version` (e.g. `cora_extractors.xsd@0.0.0`) |
| `extracted_at` | yes | ISO 8601 timestamp |
| `namespace_hint` | no | URI hint for the future OWL projection |
| `source_label` | no | Short stable identifier for this inventory's primary source (`xsd`, `excel`, `cdm-json`, …). Set by each extractor; required when calling `Inventory.enrich`. |
| `types` | no | Complex types declared by this module (required for XSD/SQL; empty or omitted for flat-table sources) |
| `fields` | yes | Every addressable leaf field in this module |
| `unmatched_enrichments` | no | Audit list of `other.fields` rows that found no `(domain, leaf-name)` match during enrich. Recorded in-place so reviewers see typos/sheet-mapping errors in the YAML diff. |

### Type entries

| Key | Required | Description |
|---|---|---|
| `name` | yes | Type identifier, unique within the module |
| `extends` | no | Name of a parent type within this inventory's `types[]` (→ `rdfs:subClassOf`) |
| `abstract` | no | Default `false` |
| `definition` | no | Human-readable description |
| `source_location` | no | Reference back to native artifact |

### Field entries

| Key | Required | Description |
|---|---|---|
| `path` | yes | Canonical reference; constructed by [`cora_extractors.path`](../tools/extractors/src/cora_extractors/path.py) |
| `concept_id` | no | Optional slugged crosswalk concept id |
| `domain` | conditional | Containing type name (required when `types[]` is non-empty) |
| `range` | no | Primitive type name or a type name from `types[]` |
| `is_reference` | no | Default `false`. `true` for object references (→ `owl:ObjectProperty`) |
| `cardinality` | yes | One of `required`, `optional`, `repeating` |
| `definition` | no | Human-readable description |
| `source_location` | no | Reference back to native artifact |
| `enumeration` | no | Allowed values, if declared |

## Path grammar

The `path` is the load-bearing crosswalks-to-inventory link. The grammar is owned by [`cora_extractors.path`](../tools/extractors/src/cora_extractors/path.py); extractors and validators **must not** construct paths by string concatenation.

Grammar v1:

- **Separator** is `/`.
- **Segments** are local identifiers (no `/` inside).
- **Cardinality** is on the field, not in the path. A field at `Property/tenants` with `cardinality: repeating` is one path regardless of multiplicity.
- **Namespaces** are normalised away by the extractor before path construction. If preserving them ever becomes necessary, the grammar will extend here.
- **Flat-table sources** produce single-segment paths (e.g. `tenant_email`). That's a valid path.

```python
from cora_extractors.path import build, parse, resolve

build(["Property", "Identification", "IDValue"])
# → "Property/Identification/IDValue"

parse("Property/Identification/IDValue")
# → ["Property", "Identification", "IDValue"]

resolve("Property/id", inventory)
# → FieldEntry(...)  or  None
```

## OWL/RDF projection roadmap

The schema is designed so that the future OWL derivation pipeline is a clean projection — no schema migration required. When that work opens, the mapping is:

| Inventory concept | OWL/RDF equivalent |
|---|---|
| `types[].name` | `owl:Class` |
| `types[].extends` | `rdfs:subClassOf` |
| `types[].abstract` | (informational) |
| `fields[]` where `is_reference: false` | `owl:DatatypeProperty` |
| `fields[]` where `is_reference: true` | `owl:ObjectProperty` |
| `fields[].domain` | `rdfs:domain` |
| `fields[].range` | `rdfs:range` |
| `fields[].cardinality` | OWL cardinality restrictions / SHACL shape |
| `fields[].enumeration` | `owl:oneOf` |
| `namespace_hint` | base URI for generated terms |

Inventories that legitimately have no class hierarchy (Excel-primary sources like REDI) ship `types: []`. The OWL projection for those will lift fields onto a single synthetic class or onto SKOS concepts; that decision belongs to the OWL phase.

## How extractors produce inventories

Each format gets a typed extractor adapter at the `Extractor` seam. The XSD extractor walks `xs:complexType` definitions into `types[]` and `xs:element`/`xs:attribute` declarations into `fields[]`. The JSON catalog extractor reads a JSONPath-described shape per a per-source config. The CDM-JSON extractor handles IBPDI's Common Data Model entity-per-file layout. The Excel single-sheet dictionary extractor reads one sheet per inventory module. The Excel multi-sheet dictionary extractor reads MITS-style workbooks where each sheet documents one shared type.

Every extractor sets `source_label` on the inventory it produces (`"xsd"`, `"excel"`, `"cdm-json"`, …) so the same data wears the same label in every operation that consumes it.

## Combining inventories: `merge` vs `enrich`

Two different operations, two methods. Pick by what the two sides represent.

**`Inventory.merge(other, *, match_by)`** — symmetric combination of two inventories of equal authority. Raises `MergeConflict` on any attested disagreement. Use when combining two halves of the same conceptual source (e.g., XSD's `domain` view + `extends` view).

**`Inventory.enrich(other, *, attributes)`** — asymmetric type-scoped fill-in from a secondary source. `self` is authoritative; `other` contributes values for the named attributes only. Matches on `(field.domain, field.path.split("/")[-1])`. Never raises. The MITS XSD + Excel data dictionary flow uses this:

```python
xsd_inv = Inventory.from_yaml(...)
excel_inv = Inventory.from_yaml(...)
enriched = xsd_inv.enrich(excel_inv, attributes={"definition", "enumeration"})
```

The `attributes` parameter is the **trust list** — "I trust `other` for these facts; ignore its claims about anything else." Future PDF / SQL DDL enrichment uses the same primitive.

CLI: `cora inventory merge --into A.yaml --from B.yaml --attribute definition --output M.yaml`.

See [ADR-0001](adr/0001-enrich-vs-merge.md) for the full design rationale.

### Provenance — the in-place audit trail

When `enrich` finds that ≥2 sources both attested a value for the same attribute on the same field, the merged inventory records both claims in a `provenance` block on the `FieldEntry`:

```yaml
- path: EventType/Description
  domain: EventType
  definition: "An event recorded in the lead lifecycle."
  source_location: lead-management.xsd:146
  provenance:
    - attribute: definition
      claims:
        - source: xsd
          value: EventType
          location: lead-management.xsd:146
        - source: excel
          value: An event recorded in the lead lifecycle.
          location: lead-management.xls!Lead Management 4.0!23
      chosen: excel
```

- `claims[]` is always ≥2 entries (single-source attestations don't get provenance; the top-level value carries them).
- `chosen` is present only when claims disagree, naming whichever source's value lives at the top level.
- Untrusted disagreements are still recorded — the trust list controls what wins at the top level, not what's recorded. This makes the YAML diff a complete lineage between regenerations.

`Inventory.unmatched_enrichments` at the top level captures `other` rows that found no match — the audit for typos and sheet-mapping errors.

Inspect any enriched inventory:

```bash
tools/extractors/.venv/bin/python tools/extractors/scripts/show_disagreements.py \
  standards/mits/current/inventory/lead-management.yaml
```

## Status

Fifteen inventories are committed today: seven MITS modules (accounts-payable, collections, lead-management, lease-application, property-marketing, resident-screening, resident-transactions), seven IBPDI clusters (digital-twin, energy-and-resources, financials, organisational-management, portfolio-and-asset-management, property-management, user-and-customer-experience), and one REDI sheet (data-fields). Combined corpus: 496 types and 3,353 fields across three standards. Every inventory was produced by one of the extractor adapters under [`tools/extractors/`](../tools/extractors/) and validated by the inventory-schema, field-count, and crosswalk-paths validators under the same `cora` CLI.
