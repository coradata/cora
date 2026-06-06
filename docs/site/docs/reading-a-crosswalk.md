# Reading a crosswalk

A crosswalk is a flat YAML file. This page walks one end to end, naming every field a consuming pipeline will encounter and what to do with it.

## The file

```yaml
concept: postal_code
canonical_definition: >-
  The postal sorting code used by the jurisdiction's postal service to route
  mail to its destination. US ZIP, Canadian postal code, UK postcode, and
  similar are all postal codes in this sense.
aliases:
  - zip_code
  - zip
  - postcode
  - postal_zip
maintainer: '@coradata/maintainers'
last_reviewed: '2026-06-01'
mappings:
  mits:
    field: AddressType/PostalCode
    version: '4.0'
    confidence: exact
    source_url: https://github.com/coradata/cora/blob/main/standards/mits/current/inventory/property-marketing.yaml
  ibpdi:
    field: Address/PostalCode
    version: '1.0'
    confidence: exact
    source_url: https://github.com/coradata/cora/blob/main/standards/ibpdi/current/inventory/organisational-management.yaml
  redi:
    field: Zip_Postal_Code
    version: '1.0'
    confidence: exact
    source_url: https://github.com/coradata/cora/blob/main/standards/redi/current/inventory/data-fields.yaml
    notes: >-
      REDI's field name combines US ZIP and international postal-code wording.
      Semantically identical to PostalCode.
```

## Top-level fields

| Field | Purpose for a consumer |
|---|---|
| `concept` | The canonical concept name. Same as the filename (`postal_code.yaml` → `concept: postal_code`). Use this as the key in your own schema if you're producing a unified record. |
| `canonical_definition` | CORA's working definition. Use this when documenting the unified column in your pipeline so downstream consumers see a consistent description. |
| `aliases` | Alternative names this concept is known by in the wild. Useful for matching vendor-supplied field names back to the canonical concept. |
| `maintainer` | Who's responsible for this crosswalk. File issues against this handle if a mapping looks wrong. |
| `last_reviewed` | ISO date of the last human review. Aging crosswalks should be eyed before relying on them through a standard's version bump. |
| `mappings` | One block per participating standard. Detailed below. |

## Per-standard mapping block

```yaml
<std>:
  field: <inventory path or null>
  version: <standard version verified against>
  confidence: exact | close | partial | divergent | not_present
  source_url: <link to the inventory or upstream doc>
  notes: <narrative — required when confidence is divergent or not_present>
```

| Field | Purpose for a consumer |
|---|---|
| `field` | The path into that standard's inventory where the concept lives. Split on `/` and walk your incoming records. `null` when the concept doesn't exist in this standard. |
| `version` | The standard-body-assigned version this mapping was verified against. If your records are from a different version, check whether the path still resolves. |
| `confidence` | How exact the mapping is. See below. |
| `source_url` | The inventory file containing the field's full definition. Open this when you need cardinality, range, or the original schema's definition string. |
| `notes` | Free-text caveats. Always present for `divergent` and `not_present`; sometimes present for `partial` and `close`. Read before integrating. |

## Confidence values

| Value | What to do with it |
|---|---|
| `exact` | Use directly. Identical name (modulo casing), semantics, and cardinality. |
| `close` | Use, but document the minor differences. Most pipelines treat `close` and `exact` the same; some carry a flag for downstream consumers who care. |
| `partial` | Read the notes before relying on equivalence. Definitions overlap but don't fully align — your pipeline may need conditional handling. |
| `divergent` | Do not treat as the same concept. The mapping warns rather than enables; the notes explain why the surface similarity is misleading. |
| `not_present` | The standard doesn't carry this concept. Your pipeline needs a derivation, a default, or a graceful absence for records from this source. |

## How the field path works

The `field` value is an inventory path — a `/`-separated string naming the type and the leaf field within it.

```
AddressType/PostalCode
^^^^^^^^^^^ ^^^^^^^^^^
type        leaf field
```

To apply it to a record, walk the path. For nested JSON or XML-derived dictionaries, the first segment names the containing type and subsequent segments are property names. For flat sources (Excel-style data dictionaries), the path is just `<TypeName>/<FieldName>` where `<TypeName>` is the table or sheet.

The inventory file itself (linked in `source_url`) shows every field with its full path, range, cardinality, and definition.

## Provenance and notes

For mappings labeled `divergent` or `not_present`, the `notes` field is mandatory and tells you *why* — typically a definitional difference too subtle to encode mechanically. Read these. They are the substance of CORA's editorial work and the part of a mapping a pipeline cannot infer on its own.

For mappings labeled `close` or `partial`, notes are optional but common. When present, they call out the specific divergence (units, formatting, optional vs required, scope).

## Versioning

Every mapping carries the standard version it's verified against. When a standard releases a new version, that mapping needs re-verification before it can be trusted against records produced under the new version. CORA's drift register surfaces those re-verification tasks in the repository; consumers can subscribe to the relevant pull-request labels for early notice.

## What to read next

[**Consuming inventories**](consuming-inventories.md)
:   The shape of the inventory files the crosswalk's `field` and `source_url` point at.

[**Integrating CORA**](integrating-cora.md)
:   Wiring crosswalks into a production pipeline, including multi-source reconciliation patterns.
