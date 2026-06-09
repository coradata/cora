# Onboarding a new extractor format

!!! note "Contributing"
    This page is for contributors adding a new source-format extractor (PDF, SQL DDL, JSON Schema, etc.). Consumers of CORA's published inventories never run an extractor — the YAML is the artifact. Start with [Consuming inventories](consuming-inventories.md) for the consumer path.

How to add a new Extractor adapter — for a format CORA doesn't already handle. PDF, SQL DDL, JSON Schema, GraphQL SDL, etc.

## Decide whether a new adapter is needed

Five adapters ship today. If your format is genuinely different — different file extension, different parse library, different structural assumptions — you need a new adapter. If your format is a *variant* of an existing shape (another flat Excel dictionary with different columns, another XSD), you don't write code: you author a `<Format>Config` YAML.

## The Extractor protocol

```python
@runtime_checkable
class Extractor(Protocol):
    name: str
    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory: ...
```

Implementations live at `cora_extractors/<format>.py`. Set `name` to the CLI identifier (`xsd`, `cdm-json`, `excel-multisheet`, etc.). Return a fully-populated `Inventory` from `extract`.

## The four files you'll touch

### 1. The config class

`cora_extractors/config.py`. Add a pydantic subclass of `ExtractorConfig`:

```python
class MyFormatConfig(ExtractorConfig):
    """Config for the MyFormat extractor.

    <Describe what's required, what's optional, what each field means.>
    """

    namespace_hint: str | None = None
    # Format-specific fields go here.
    skip_header_rows: int = 1
    field_name_column: str
```

`ExtractorConfig` is a pydantic v2 `BaseModel` with `extra="forbid"` so typos in YAML configs raise validation errors. Add validators if anything cross-field needs checking.

### 2. The adapter module

`cora_extractors/<format>.py`. Implementation pattern (lifted from `excel_multisheet.py`):

```python
from datetime import UTC, datetime
from pathlib import Path

from cora_extractors import __version__
from cora_extractors.config import ExtractorConfig, MyFormatConfig
from cora_extractors.inventory import FieldEntry, Inventory

EXTRACTOR_ID = f"cora_extractors.myformat@{__version__}"


class MyFormatExtractor:
    """Extractor adapter for MyFormat sources."""

    name = "myformat"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if not isinstance(config, MyFormatConfig):
            raise TypeError("MyFormatExtractor.extract requires a MyFormatConfig")

        fields = list(_iter_fields(source, config))

        return Inventory(
            standard=module or source.stem,
            module=module or source.stem,
            version="unknown",  # CLI overrides via --version
            source_artifact=str(source),
            extractor=EXTRACTOR_ID,
            extracted_at=datetime.now(tz=UTC),
            namespace_hint=config.namespace_hint,
            source_label="myformat",   # <-- short stable identifier
            types=[],   # populate if the format has classes
            fields=fields,
        )
```

Two things to get right:

- **Always set `source_label`.** It's a required participant in [`Inventory.enrich`](inventory-operations.md) — every adapter sets the same short identifier so the same data wears the same label in every operation.
- **Type hint your helper functions.** Mypy `--strict` is the gate; pydantic catches runtime config errors but mypy catches the structural mistakes earlier.

### 3. Register in the CLI

`cora_extractors/cli.py`. Two dicts:

```python
EXTRACTORS: dict[str, Extractor] = {
    "xsd": XsdExtractor(),
    ...
    "myformat": MyFormatExtractor(),   # NEW
}

CONFIG_TYPES: dict[str, type[ExtractorConfig]] = {
    "xsd": XsdConfig,
    ...
    "myformat": MyFormatConfig,        # NEW
}
```

That's it — `cora extract myformat <source> --config c.yaml --output out.yaml` works now.

### 4. Tests + fixtures

`tools/extractors/tests/test_<format>.py` and `tools/extractors/tests/fixtures/<format>/`. Pattern:

- **Protocol conformance test** — `isinstance(MyFormatExtractor(), Extractor)`.
- **Round-trip test** — feed a fixture source, assert the resulting `Inventory` matches expected. Use `Inventory.from_yaml` for the expected output if it's stable.
- **Two-source genericity audit** — at least two fixture sources of the same format, both extracted by the same adapter. This catches the "I accidentally hard-coded a column letter from the only test case" failure mode.
- **Negative tests** — wrong config type → `TypeError`; malformed source → clean error.

Existing tests for `excel_multisheet`, `xsd`, `cdm_json` are good shape references.

## The "two-source genericity audit"

A core discipline of CORA's extractor work. The rule: **before declaring a format adapter shipped, you've extracted at least two real sources of that format successfully.**

The point: a single source doesn't prove your adapter is general — it proves you encoded that source. With two distinct sources (different column layouts, different file naming, different nesting depth, etc.) you've shown the adapter handles the *format* not the *example*.

In practice:

- XSD adapter has two fixture XSDs in `tests/fixtures/xsd/` with different structures.
- CDM JSON adapter has two cluster directories in `tests/fixtures/cdm_json/`.
- Excel single-sheet adapter has two fixtures in `tests/fixtures/excel/`.
- Excel multi-sheet adapter has two layouts (`with_root_column`, `flat`) in its `test_excel_multisheet.py` (generated inline rather than committed).

If you can't find two real-world sources of your format in the wild, hand-build the second one as a fixture. Cheap insurance.

## A few patterns worth knowing

### Shared low-level helpers

`cora_extractors/_excel_io.py` is module-private (leading underscore) and shared between `excel_dictionary` and `excel_multisheet`. It carries `read_rows`, `column_to_index`, `cell`, `coerce_cardinality`, `parse_enumeration`.

If your format reuses I/O or parsing logic that other adapters could need, put it in a `_<format>_io.py` private module rather than directly in the adapter file. The deletion test: if you delete the helper, the logic respreads across both adapters — concentrating it earns its keep.

### Configurable remaps for external references

The XSD adapter handles `xs:include schemaLocation="http://..."` by consulting `XsdConfig.include_remap` (URL → local path). If your format references external schemas, follow the same pattern: a `dict[str, str]` field on your config, consulted before falling back to the default resolution.

### Cardinality coercion is a footgun

Different formats spell cardinality differently. `excel_multisheet` combines a `Req` column (Y/N) with a `Max occurs` column (numeric or "Unbounded") into a canonical `Cardinality` value (`required` / `optional` / `repeating`). The shared `coerce_cardinality` helper in `_excel_io.py` handles the common cases; format-specific logic that wraps it lives in the adapter.

### Future PDF / SQL DDL hints

When the PDF extractor lands, expect it to be LLM-assisted (extract definitions from prose; human reviews the output). It'll be the second adapter of an "AI-assisted" sub-pattern — and a second adapter usually means a real seam, so factor common AI-call plumbing into a private helper before adding a third.

The SQL DDL extractor will be a straightforward parse of `CREATE TABLE` statements, with comments → definitions. Closer in shape to the XSD adapter than to the others.

---

## Workflow summary

1. Decide if it's a new adapter (vs. a new config).
2. Write the config class (`config.py`).
3. Write the adapter (`<format>.py`). Set `source_label`.
4. Register in `cli.py` (two dicts).
5. Add tests with ≥2 fixture sources.
6. Run gates: `pytest`, `mypy --strict`, `ruff check`.
7. Document in `docs/site/docs/seams.md`'s adapter list.
8. PR. CI re-runs everything.

The pattern is small and stable. Each existing adapter is roughly 60–200 lines plus its config; the tests are 100–250 lines. The protocol's narrowness (one method, three parameters, one return type) is what keeps the discipline.
