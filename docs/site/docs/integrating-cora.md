# Integrating CORA

Patterns for wiring CORA's crosswalks and inventories into a production pipeline. The artifacts are plain YAML; the integration patterns below assume your pipeline already ingests records under one or more participating standards and you want to add cross-standard normalization.

## The integration shape

Every pattern follows the same three steps:

1. **Load the crosswalks** you care about. One YAML per concept.
2. **For each incoming record, look up the field path** for the source standard it came from.
3. **Walk the path** into the record to extract the value, then write it under the canonical concept name in your unified output.

The artifacts are static — load once at process start, cache in memory, and consult per record.

## Loading at process start

```python
import yaml
from pathlib import Path

def load_crosswalks(repo_root: Path) -> dict[str, dict]:
    """Load every committed crosswalk into a {concept_name: yaml_dict} index."""
    cw_dir = repo_root / "crosswalks" / "concepts"
    return {
        path.stem: yaml.safe_load(path.read_text())
        for path in cw_dir.glob("*.yaml")
    }

CROSSWALKS = load_crosswalks(Path("./cora"))
```

For a long-running process, load once at startup. The artifacts don't change at runtime.

## Path walking

The field path is `<TypeName>/<LeafName>` for single-segment leaves and `<TypeName>/<Segment>/.../<LeafName>` for nested ones. The first segment names the containing type; subsequent segments walk into the record.

```python
def walk_path(record: dict, path: str) -> object | None:
    """Walk a CORA inventory path into a parsed source record."""
    segments = path.split("/")[1:]  # skip the type name
    current = record
    for segment in segments:
        if not isinstance(current, dict):
            return None
        current = current.get(segment)
        if current is None:
            return None
    return current
```

For records that arrive as XML, parse to a dict-like structure first; the walker is shape-agnostic.

## Single-source extraction

The minimal case — one source, one concept:

```python
mits_record = {"AddressType": {"PostalCode": "94110", "City": "San Francisco"}}

concept = CROSSWALKS["postal_code"]
mits_path = concept["mappings"]["mits"]["field"]
postal_code = walk_path(mits_record, mits_path)
# "94110"
```

## Multi-source reconciliation

The point of CORA — one unified column from multiple sources:

```python
def unify(concept_name: str, records_by_standard: dict[str, dict]) -> object | None:
    """Pull the same concept from whichever sources we have for this record."""
    concept = CROSSWALKS[concept_name]
    for std, record in records_by_standard.items():
        mapping = concept["mappings"].get(std)
        if not mapping or mapping["confidence"] == "not_present":
            continue
        value = walk_path(record, mapping["field"])
        if value is not None:
            return value
    return None

records = {
    "mits": {"AddressType": {"PostalCode": "94110"}},
    "ibpdi": {"Address": {"PostalCode": "94110"}},
}
print(unify("postal_code", records))  # "94110"
```

The reconciliation policy above is "first non-null wins." Real pipelines often need richer policies — preferring one source over another, flagging disagreements, recording which source supplied each value. The shape stays the same; the policy is yours.

## Confidence-aware extraction

Pipelines that distinguish between high-confidence and low-confidence mappings can gate behavior on the confidence label:

```python
SAFE = {"exact", "close"}

def unify_strict(concept_name: str, records_by_standard: dict[str, dict]) -> object | None:
    concept = CROSSWALKS[concept_name]
    for std, record in records_by_standard.items():
        mapping = concept["mappings"].get(std)
        if not mapping or mapping["confidence"] not in SAFE:
            continue
        value = walk_path(record, mapping["field"])
        if value is not None:
            return value
    return None
```

`partial` and `divergent` are skipped by `unify_strict`. A more nuanced version might emit a warning instead of skipping silently, or record the confidence on the output row.

## Writing a unified row

Putting it together, building one row of a unified output from many source records:

```python
def build_row(records_by_standard: dict[str, dict]) -> dict:
    return {
        concept: unify(concept, records_by_standard)
        for concept in CROSSWALKS
    }

print(build_row(records))
# {"postal_code": "94110", "city": "San Francisco", ...}
```

The output schema is exactly the set of concept names CORA publishes — stable, documented, and growing with the project.

## SQL view pattern

For warehouses that store the source records as JSON columns, a unified view can be expressed in SQL using the inventory paths directly:

```sql
create view unified_property_v as
select
  coalesce(
    mits_record::jsonb -> 'AddressType' ->> 'PostalCode',
    ibpdi_record::jsonb -> 'Address' ->> 'PostalCode'
  ) as postal_code,
  coalesce(
    mits_record::jsonb -> 'AddressType' ->> 'City',
    ibpdi_record::jsonb -> 'Address' ->> 'City'
  ) as city
from property_intake;
```

The paths come from the crosswalks. A small generator that reads the crosswalk YAML and emits the SQL `coalesce` expressions is a one-pager — most teams write it once for their warehouse and run it as part of schema management.

## Handling `not_present`

When a source genuinely doesn't carry a concept, the mapping says so:

```yaml
mappings:
  ibpdi:
    field: null
    confidence: not_present
    notes: >-
      IBPDI v1.0 does not model contact email at the property level.
```

In your pipeline, `not_present` means "no extraction possible from this source for this concept" — not "missing data." The downstream consumer should see a documented absence, not a null whose meaning is ambiguous.

## Versioning at the boundary

Every mapping records the standard version it was verified against (`mapping["version"]`). At ingest time, compare the version on your incoming record to the version on the mapping. A mismatch isn't necessarily a failure — most field paths survive minor version bumps — but it is a signal that the mapping deserves a re-verification check before going to production.

CORA's drift register tracks this work in the open; the relevant pull requests carry labels your team can watch.

## What to read next

[**Reading a crosswalk**](reading-a-crosswalk.md)
:   The full crosswalk YAML shape, including confidence vocabulary and narrative notes.

[**Consuming inventories**](consuming-inventories.md)
:   The inventory shape your `source_url` points at — useful when you need a field's cardinality, range, or original definition.

[**Requesting a crosswalk**](requesting-a-crosswalk.md)
:   What to do when the concept your pipeline needs isn't yet covered.
