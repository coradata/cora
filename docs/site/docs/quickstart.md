# Quickstart

The shortest path from "my data is in MITS" to "this field is the same concept in IBPDI." No toolkit install, no CLI. Just YAML and your existing pipeline.

## Scenario

You have property records arriving in two formats. One source publishes MITS XML against the Property-Marketing 5.0 schema. The other publishes IBPDI JSON conforming to the Organisational-Management Common Data Model. You need a single postal-code column from both sources.

## 1. Find the concept

CORA publishes one crosswalk per canonical concept. The list lives in [`crosswalks/concepts/`](https://github.com/coradata/cora/tree/main/crosswalks/concepts), and the at-a-glance view is the [coverage matrix](https://github.com/coradata/cora/blob/main/docs/generated/coverage-matrix.md).

The concept you need is `postal_code`.

## 2. Read the crosswalk

[`crosswalks/concepts/postal_code.yaml`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/postal_code.yaml):

```yaml
concept: postal_code
canonical_definition: >-
  The postal sorting code used by the jurisdiction's postal service to route
  mail to its destination.
aliases: [zip_code, zip, postcode, postal_zip]
mappings:
  mits:
    field: AddressType/PostalCode
    version: '4.0'
    confidence: exact
  ibpdi:
    field: Address/PostalCode
    version: '1.0'
    confidence: exact
  redi:
    field: Zip_Postal_Code
    version: '1.0'
    confidence: exact
```

Three `exact` mappings. Your two sources are both covered with high confidence, and the field path in each standard's schema is named.

## 3. Apply the mapping

Pull the file. Read the YAML. Use the per-standard `field` value to extract the right path from each incoming record.

```python
import yaml
from pathlib import Path

crosswalk = yaml.safe_load(Path("postal_code.yaml").read_text())

# Look up the field path for the source you're processing
mits_path = crosswalk["mappings"]["mits"]["field"]    # "AddressType/PostalCode"
ibpdi_path = crosswalk["mappings"]["ibpdi"]["field"]  # "Address/PostalCode"

# Apply against your records — split the path and walk
def get_field(record: dict, path: str):
    for part in path.split("/")[1:]:  # first segment is the type, not a key
        record = record.get(part)
        if record is None:
            return None
    return record

mits_record = {"AddressType": {"PostalCode": "94110"}}
print(get_field(mits_record, mits_path))  # "94110"
```

That's the workflow. For any concept CORA covers, your pipeline reads one file and gains a definition that survives across sources.

## What to read next

[**Concepts**](concepts.md)
:   The vocabulary used everywhere on this site — canonical concept, mapping, confidence, inventory, crosswalk.

[**What CORA publishes**](artifacts.md)
:   The full catalogue: which inventories are committed, which concepts have crosswalks, where the coverage matrix lives.

[**Finding a concept**](finding-a-concept.md)
:   How to search the crosswalks when the concept name you want isn't immediately obvious.

[**Reading a crosswalk**](reading-a-crosswalk.md)
:   The full YAML shape — aliases, confidence vocabulary, notes, version tracking.

[**Integrating CORA**](integrating-cora.md)
:   Patterns for wiring crosswalks and inventories into a production pipeline.

[**Requesting a crosswalk**](requesting-a-crosswalk.md)
:   What to do when the concept you need isn't yet covered.
