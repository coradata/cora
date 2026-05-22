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
| `types` | no | Complex types declared by this module (required for XSD/SQL; empty or omitted for flat-table sources) |
| `fields` | yes | Every addressable leaf field in this module |

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

The schema is designed so that the future OWL derivation pipeline is a clean projection — no schema migration required. When that phase opens (see [`internal-planning/CORA-Field-Inventory-Plan.md`](../../internal-planning/CORA-Field-Inventory-Plan.md), Future Phases section), the mapping is:

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

Each format gets a typed extractor adapter at the `Extractor` seam (defined in Phase 2 of the inventory plan). The XSD extractor walks `xs:complexType` definitions into `types[]` and `xs:element`/`xs:attribute` declarations into `fields[]`. The JSON catalog extractor reads a JSONPath-described shape per a per-source config. The Excel data dictionary extractor reads one sheet per inventory module.

The MITS pattern (XSD primary, Excel data dictionary secondary) uses `Inventory.merge(other, match_by='name')` to enrich XSD-derived inventories with Excel-sourced definitions. The merge raises `MergeConflict` if the two sources disagree on type, cardinality, or enumeration — better to surface the disagreement than silently pick one.

## Status

Phase 1 of the [field-inventory plan](../../internal-planning/CORA-Field-Inventory-Plan.md) ships the schema, the typed inventory module, the path module, fixtures, and these docs. **No real inventories have been extracted yet** — that lands in Phase 3 after the extractor adapters arrive in Phase 2.
