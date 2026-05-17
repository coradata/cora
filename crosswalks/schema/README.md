# Crosswalk Schema

`crosswalk.schema.json` defines the canonical YAML structure every crosswalk follows. It is enforced by CI on every PR that touches `/crosswalks/concepts/`.

## Confidence values

- `exact` — Identical meaning, field types, and cardinality.
- `close` — Same meaning, minor structural difference (e.g., naming convention).
- `partial` — Overlapping but not identical scope. Notes required.
- `divergent` — Same concept name, materially different definition. Notes **required** explaining the difference.
- `not_present` — Concept does not exist in the standard. Notes **required** explaining what the closest analog is, if any.

## Boundary crosswalks

Crosswalks marked `boundary: true` connect to adjacent ontologies CORA deliberately does not host (e.g., MISMO residential mortgage operations, RealEstateCore building systems). They follow the same schema but reference standards CORA does not mirror.

## Adding a new crosswalk

1. Pick a concept that appears in at least two hosted standards (or one hosted + one boundary).
2. Create `concepts/<concept_name>.yaml`.
3. Ensure all required fields are present.
4. Run validation: `cora validate crosswalk concepts/<concept_name>.yaml` (when CLI lands).
5. Open a PR. CI will run schema validation.
