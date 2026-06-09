# Finding a concept

Three ways to discover whether CORA already covers the field your pipeline needs. Pick whichever fits the question you're holding.

## By known name

If you already know the canonical name — `postal_code`, `street_address`, `email_address` — go straight to [`crosswalks/concepts/<concept>.yaml`](https://github.com/coradata/cora/tree/main/crosswalks/concepts). One file per concept; the filename is the concept name.

## By alias

If you're carrying a vendor's field name (`zip_code`, `Zip_Postal_Code`, `postcode`), the crosswalks declare aliases inside the YAML. A repository grep against the `aliases:` block is the fastest path:

```bash
grep -l "zip_code" crosswalks/concepts/*.yaml
# crosswalks/concepts/postal_code.yaml
```

Or, programmatically:

```python
import yaml
from pathlib import Path

target = "zip_code"
for path in Path("crosswalks/concepts").glob("*.yaml"):
    cw = yaml.safe_load(path.read_text())
    if target in cw.get("aliases", []) or cw["concept"] == target:
        print(path, "->", cw["concept"])
```

Every concept's primary name plus its aliases are searchable this way.

## By coverage matrix

If the question is *which fields can my pipeline rely on across the sources I receive*, open the [coverage matrix](https://github.com/coradata/cora/blob/main/docs/generated/coverage-matrix.md). Concepts down the left, standards across the top, confidence indicators in the cells. The matrix answers cross-source feasibility questions faster than reading individual crosswalks.

A `not_present` cell tells you a source genuinely can't answer the question that concept asks; build your pipeline accordingly.

## By browsing the generated concept pages

For visual inspection, the auto-generated concept pages at [`docs/generated/concepts/`](https://github.com/coradata/cora/tree/main/docs/generated/concepts) render each crosswalk as a Markdown table plus a Mermaid graph. Useful when you want to evaluate a concept's mapping without opening the YAML.

These are mechanical projections — the YAML is authoritative. Pipelines should always read the YAML.

## When the concept isn't covered

CORA today publishes thirty-three concept crosswalks, and the corpus grows with the standards bodies' work and the analyzer-driven editorial passes. Before [requesting a crosswalk](requesting-a-crosswalk.md), check the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md) and the [semantic suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions-semantic.md) — the concept may already be a known candidate cluster awaiting an editorial pass. If the field your organization needs is neither covered nor surfaced, file the request. The mapping work is openly maintained; most additions are merged within one review cycle.

## What to read next

[**Reading a crosswalk**](reading-a-crosswalk.md)
:   The full YAML shape — confidence labels, version tracking, narrative notes.

[**Integrating CORA**](integrating-cora.md)
:   Wiring the lookup pattern above into a production pipeline.
