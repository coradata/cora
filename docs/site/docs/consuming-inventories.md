# Consuming inventories

An inventory is a YAML file. Any YAML parser reads it; you don't need CORA's toolkit. This page walks the shape, the patterns for traversal, and the typed model the project ships as a convenience.

## The shape

```yaml
standard: mits
module: property-marketing
version: '5.0'
extractor: cora_extractors.xsd@0.0.0
source_label: xsd
types:
  - name: PropertyType
    extends: Identifiable
    definition: A property listed for marketing.
  - name: AddressType
    extends: null
    definition: Postal address as expressed in MITS property marketing.
fields:
  - path: PropertyType/PropertyID
    domain: PropertyType
    range: Identification
    cardinality: required
    definition: Unique identifier for the property.
  - path: AddressType/PostalCode
    domain: AddressType
    range: string
    cardinality: required
    definition: Postal code for the property's address.
```

Every inventory carries the same top-level keys regardless of which source format produced it.

| Key | Type | Meaning |
|---|---|---|
| `standard` | string | Short identifier — `mits`, `ibpdi`, `redi`. |
| `module` | string | Module name within the standard. |
| `version` | string | Source artifact version, exactly as the standard body publishes it. |
| `extractor` | string | `module.name@version` of the extractor that produced the inventory. Provenance, not behavior. |
| `source_label` | string | `xsd`, `excel`, `cdm-json`, etc. Records which native artifact produced this view. |
| `types` | list | Complex types — classes, records, structs. May be empty for flat sources. |
| `fields` | list | Leaf fields. Always populated. |
| `unmatched_enrichments` | list, optional | Audit trail when an inventory was enriched from a secondary source. Inspectable but not part of the consumable schema. |

## Types

Each entry in `types` describes one complex type:

| Key | Meaning |
|---|---|
| `name` | The type's name in the source schema. Matches the first segment of any `path` in `fields` whose `domain` is this type. |
| `extends` | The parent type if the source schema models inheritance. `null` otherwise. |
| `definition` | The source schema's prose definition of the type. |

Use `types` when you need to know the shape of a containing record (which leaves belong to it, what its parent type is). For most consumption — pulling one field per concept — you can skip directly to `fields`.

## Fields

Each entry in `fields` is one leaf:

| Key | Meaning |
|---|---|
| `path` | The full `<TypeName>/<LeafName>` path. This is the string a crosswalk's `mappings.<std>.field` points at. |
| `domain` | The owning type name. Same as the first segment of `path`. |
| `range` | The field's value type — a primitive (`string`, `int`, `date`) or the name of another type for references. |
| `cardinality` | `required`, `optional`, or `many`. |
| `definition` | The source schema's prose definition. |
| `provenance` | Optional. Present when the inventory was multi-source enriched and one or more attributes have attestation lineage. |
| `enumeration` | Optional. Present when the source schema constrained the field to a fixed value set. |

## Loading the YAML

Any standard library parser works. With Python's PyYAML:

```python
import yaml
from pathlib import Path

inv = yaml.safe_load(
    Path("standards/mits/current/inventory/property-marketing.yaml").read_text()
)
print(inv["standard"], inv["module"], inv["version"])
print(len(inv["fields"]), "fields")
```

For typed access, the project ships a Pydantic model. Install the toolkit, then:

```python
from pathlib import Path
from cora_extractors.inventory import Inventory

inv = Inventory.from_yaml(
    Path("standards/mits/current/inventory/property-marketing.yaml")
)
print(inv.standard, inv.module, inv.version)
print(len(inv.fields))
```

The typed model is a convenience, not a requirement. Treating inventories as plain dicts is fully supported.

## Resolving a path

A crosswalk gives you `AddressType/PostalCode`. To find the corresponding entry in an inventory, match the `path` exactly:

```python
def resolve(path: str, inv: dict) -> dict | None:
    for field in inv["fields"]:
        if field["path"] == path:
            return field
    return None

field = resolve("AddressType/PostalCode", inv)
if field:
    print(field["range"], field["cardinality"], field["definition"])
```

When you have the toolkit installed, the same operation is one function call:

```python
from cora_extractors.path import resolve
field = resolve("AddressType/PostalCode", inv)
```

## Walking by domain

To get every leaf belonging to one type:

```python
def fields_of(type_name: str, inv: dict) -> list[dict]:
    return [f for f in inv["fields"] if f["domain"] == type_name]

address_fields = fields_of("AddressType", inv)
```

Useful when you need not just one mapped concept but every attribute of a containing type — common when materializing a row from a nested source.

## Cardinality and required-ness

`cardinality` is one of three values. Use it to decide whether your pipeline needs null handling and array handling at the boundary:

| Cardinality | Meaning |
|---|---|
| `required` | The source schema guarantees this field is present and non-empty. |
| `optional` | The source schema allows absence. Plan for null. |
| `many` | The field can repeat. Source-side it's an array or a collection of elements. |

## Definitions

The `definition` string is whatever the source standard published. CORA reproduces it verbatim — useful both for documentation and for downstream consumers who need the canonical wording.

Inventories produced by multi-source enrichment (currently MITS, which combines XSD structure with Excel data-dictionary prose) carry `provenance` blocks on fields where two sources attested different values. The top-level value is the trusted source; `provenance` records both claims so the choice is auditable.

## What to read next

[**Integrating CORA**](integrating-cora.md)
:   Wiring crosswalks and inventories into a production pipeline, including multi-source reconciliation patterns.

[**Reading a crosswalk**](reading-a-crosswalk.md)
:   The companion shape — how crosswalks point into the inventories described here.
