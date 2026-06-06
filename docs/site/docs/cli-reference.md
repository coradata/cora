# CLI reference

!!! note "Contributing"
    This page documents the `cora` CLI used to maintain CORA's published artifacts. Consumers integrating CORA into a pipeline read the published YAML directly and never run the CLI. Start with [Quickstart](quickstart.md) or [Integrating CORA](integrating-cora.md) for the consumer path.

The `cora` CLI is a thin registry over the three protocols (Extractor, Validator, Generator). One entrypoint, four subcommand families.

```
cora [--version] <subcommand> ...
```

| Subcommand | Purpose |
|---|---|
| [`extract`](#cora-extract) | Run an Extractor against a native artifact, write an inventory YAML. |
| [`validate`](#cora-validate) | Run one or all Validators against the repo. |
| [`inventory`](#cora-inventory) | Consumer subcommands: `summary`, `merge`. |
| [`docs`](#cora-docs) | Generated docs site: `build`, `check`. |

---

## `cora extract`

```
cora extract <format> <source> [--config <c.yaml>]
             [--standard <s>] [--module <m>] [--version <v>]
             [--repo-root <path>] --output <out.yaml>
```

Run a registered extractor against `<source>` and write the resulting inventory to `<out.yaml>`.

**`<format>`** picks the adapter:

- `xsd` — XML Schema (resolves `xs:include` chains; `XsdConfig.include_remap` redirects unresolvable URLs)
- `json` — Flat JSON catalog described by JSONPath (`JsonCatalogConfig`)
- `cdm-json` — Microsoft Common Data Model JSON manifests (`CdmJsonConfig`)
- `excel` — Single-sheet Excel data dictionary (`ExcelDictionaryConfig`)
- `excel-multisheet` — Multi-sheet MITS workbook, one sheet per type (`ExcelMultiSheetDictionaryConfig`)

**Examples.**

Extract a MITS XSD module with no config:

```bash
cora extract xsd \
  standards/mits/current/native/Property-Marketing-ILS-5.0-XSD-with-CORE/Property-Marketing-ILS-5.0.xsd \
  --standard mits --module property-marketing --version 5.0 \
  --repo-root . --output /tmp/property-marketing.yaml
```

Extract a MITS module that references remote Core-Data URLs, with the remap config:

```bash
cora extract xsd \
  standards/mits/current/native/Lead-Management-4.0/Lead-Management-4.0.1-Schema-xsd.xml \
  --config tools/extractors/configs/mits-lead-management.yaml \
  --standard mits --module lead-management --version 4.0.1 \
  --repo-root . --output /tmp/lead-management.yaml
```

Extract a multi-sheet MITS Excel data dictionary:

```bash
cora extract excel-multisheet \
  standards/mits/current/native/Lead-Management-4.0/Lead-Management-4.0-Data-Dictionary-xls.xls \
  --config tools/extractors/configs/mits-lead-management-dictionary.yaml \
  --standard mits --module lead-management --version 4.0.1 \
  --repo-root . --output /tmp/lead-management-excel.yaml
```

**`--repo-root`** makes `source_artifact` in the output relative to that path; without it the inventory carries the absolute path.

---

## `cora validate`

```
cora validate [<name>] [--repo-root <path>]
```

Run one or all Validators against the repo. `<name>` is one of:

- `inventory-schema` — every committed inventory validates against the JSON Schema and passes structural invariants
- `field-count` — every inventory clears its minimum field count (see `tools/extractors/configs/field-count-minimums.yaml`)
- `crosswalk-paths` — every crosswalk's `mappings.<std>.field` resolves; `not_present` requires `field: null` + `notes`; `divergent` requires `notes`

Omit `<name>` to run all three. Exit code is 0 if no `error`-severity findings; non-zero otherwise. Findings print as `[<name>:<severity>] <location>: <message>`.

**Examples.**

```bash
cora validate --repo-root .                 # all three
cora validate crosswalk-paths --repo-root . # just that one
```

---

## `cora inventory`

Consumer subcommands. Two today.

### `cora inventory summary`

```
cora inventory summary <inventory.yaml>
```

Print a summary of an inventory YAML — class count, property count, max inheritance depth, datatype-vs-object-property ratio, fields-without-domain count.

```bash
cora inventory summary standards/mits/current/inventory/property-marketing.yaml
```

```
mits/property-marketing
  classes:                38
  properties:             191 (datatype=163, object=28, datatype/total=0.85)
  fields without domain:  0
  max inheritance depth:  2
```

### `cora inventory merge`

```
cora inventory merge --into <primary.yaml> --from <secondary.yaml>
                     --attribute <attr> [--attribute <attr> ...]
                     --output <merged.yaml>
```

Thin CLI wrapper over `Inventory.enrich`. Asymmetric type-scoped fill-in: `<primary>` is authoritative; `<secondary>` contributes values for the named attributes only. Matches on `(domain, leaf-name)`. Never raises.

Valid `--attribute` values: `definition`, `enumeration`, `range`, `concept_id`. The trust list is **required** — no default.

```bash
cora inventory merge \
  --into standards/mits/current/inventory/lead-management.yaml \
  --from /tmp/lead-management-excel.yaml \
  --attribute definition --attribute enumeration \
  --output standards/mits/current/inventory/lead-management.yaml
```

See [merge vs enrich](inventory-operations.md) for semantics.

---

## `cora docs`

Generated docs subcommands. The output tree lives at `docs/generated/` (separate from this authored site under `docs/site/`).

### `cora docs build`

```
cora docs build [--repo-root <path>] [--output <output_dir>]
```

Run every Generator adapter against the repo and write Markdown into `<output_dir>` (default `<repo_root>/docs/generated/`). Generators run in registry order so the index page is written last with the others already on disk.

```bash
cora docs build --repo-root .
```

### `cora docs check`

```
cora docs check [--repo-root <path>]
```

Regenerate everything into a temp directory and diff against the committed `docs/generated/`. Exit non-zero if anything differs. Used as the CI drift gate so any change to inventories or crosswalks that forgets to regenerate the docs fails the build.

```bash
cora docs check --repo-root .
```

---

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | Validator surfaced one or more `error`-severity findings (`cora validate`); or generated docs differ from committed output (`cora docs check`); or argparse error |

---

## Invoking via Python module

The CLI is implemented in `cora_extractors.cli:main`. CI invokes it as a Python module to avoid PATH issues:

```bash
python -m cora_extractors validate --repo-root .
python -m cora_extractors docs check --repo-root .
```

Equivalent to the `cora` entry point.
