# Onboarding a new standard

!!! note "Contributing"
    This page is for contributors expanding CORA's corpus with a new participating standard. Consumers reading the existing inventories and crosswalks should start with [Quickstart](quickstart.md) or [What CORA publishes](artifacts.md).

A walkthrough for adding a fourth (fifth, …) standard to CORA's corpus. The mechanical steps; the editorial decisions are out of scope for this page (license review, governance signaling, etc. — see `standards/_template/` and `docs/onboarding-a-standard.md` in the repo).

Each existing standard demonstrates one path:

| Standard | Primary format | Extractor |
|---|---|---|
| MITS | XML Schema (XSD) | `xsd` |
| IBPDI | Microsoft CDM JSON manifest | `cdm-json` |
| REDI | Excel workbook | `excel` |

A new standard slots into the same flow.

## How proposals are evaluated

Before the mechanical steps below, a proposed standard has to clear an editorial bar. Anyone can propose one by opening a [standard proposal issue](https://github.com/coradata/cora/issues/new?template=standard_proposal.yaml); the proposal is evaluated against four criteria:

1. **Licensing.** The standard is published under an open license CORA may redistribute, *or* the owning body grants written permission to mirror it. A standard CORA cannot legally republish cannot be hosted — only linked.
2. **Scope fit.** The standard describes real-assets data across the investment, operational, or reporting lifecycle (real estate equity/debt, infrastructure). Adjacent domains (smart-building/IoT, general semantic interchange) are out of scope and belong to RealEstateCore, OSI, and similar — CORA crosswalks to them at the boundary rather than hosting them.
3. **Upstream relationship.** Either an open-license mirror path exists (no permission needed) or there is a real conversation with the owning body. CORA does not host standards over a maintainer's objection.
4. **A reason to host it now.** A named consumer who needs the crosswalks, or a participating sponsor, or clear overlap with concepts already in the corpus. Hosting a standard nobody is asking to unify adds maintenance cost without payoff.

**Who decides.** During bootstrap custodianship the decision rests with the bootstrap custodian (Cherre), made in the open on the proposal issue. When CORA transitions to neutral foundation governance, standard intake becomes a governance-body decision. Either way the criteria above are the bar, and the rationale for accepting or declining is recorded on the issue.

A proposal that clears the bar then follows the mechanical onboarding below.

## Step 1: Mirror the native artifact

```
standards/<std>/
├── PROVENANCE.yaml
├── README.md
└── current/
    ├── CHANGELOG.md
    ├── native/         # bit-identical mirror of upstream artifacts
    └── inventory/      # produced in step 3
```

Copy from `standards/_template/`. Fill in `PROVENANCE.yaml` (source URL, license, mirror date) and `README.md` (what this standard is, who maintains it upstream).

The `native/` directory is the source of truth — never edited, only added to as new versions arrive. CORA mirrors it byte-identically and records the SHA in `PROVENANCE.yaml`.

## Step 2: Pick (or build) an extractor

If your standard's primary format matches an existing adapter, you don't write new code — only a config file. The five existing adapters:

- `xsd` — XML Schema; resolves `xs:include` chains; redirect remote URLs via `XsdConfig.include_remap`.
- `cdm-json` — Microsoft Common Data Model JSON manifests (one entity per `*.cdm.json` file).
- `json` — Generic flat JSON catalog described by JSONPath.
- `excel` — Single-sheet Excel data dictionary.
- `excel-multisheet` — Multi-sheet MITS workbook (one sheet per type).

If your format is *something else* (PDF, SQL DDL, GraphQL SDL, JSON Schema, etc.), you write a new Extractor adapter. See [Onboarding a new format](onboarding-a-format.md).

## Step 3: Author the per-module configs and extract

For each module of the standard, author one config file:

```
tools/extractors/configs/<std>-<module>.yaml
```

Then run the extractor against each module:

```bash
tools/extractors/.venv/bin/cora extract <format> \
  standards/<std>/current/native/<module-source> \
  --config tools/extractors/configs/<std>-<module>.yaml \
  --standard <std> --module <module> --version <v> \
  --repo-root . \
  --output standards/<std>/current/inventory/<module>.yaml
```

Commit the resulting inventory YAMLs.

If the standard ships a secondary documentation source (Excel data dictionary, PDF, SQL DDL with comments), extract it separately and merge using [`Inventory.enrich`](inventory-operations.md) — see the MITS pattern: XSD primary + Excel multi-sheet secondary, trust list `{definition, enumeration}`.

## Step 4: Tune validators

Set the per-module field-count minimums so empty extractions are caught early:

```yaml
# tools/extractors/configs/field-count-minimums.yaml
overrides:
  <std>/<module>: <minimum>
```

Then run all three validators:

```bash
tools/extractors/.venv/bin/cora validate --repo-root .
```

Exit 0 means schema-valid, field-count-compliant, and (once you add crosswalks) crosswalk-paths-clean.

## Step 5: Add crosswalks

For every concept your standard *also* models, add a `mappings.<std>` block to the existing crosswalk YAML. For concepts unique to your standard, author new ones — see [Authoring a crosswalk](authoring-a-crosswalk.md).

A first-time crosswalking pass often surfaces vocabulary clashes (IBPDI's "Building" vs MITS's "Property") that the canonical definitions need to disambiguate. Don't paper over the clash with a `close` mapping — use `partial` or `divergent` and write the narrative.

## Step 6: Update generated docs

```bash
tools/extractors/.venv/bin/cora docs build --repo-root .
```

Your new inventory pages appear at `docs/generated/inventories/<std>/<module>.md` and the index page picks up the new standard automatically. Once the new standard has crosswalk mappings (step 5), `docs build` also emits the [adoption briefings](adopting-a-standard.md) for every ordered pair it now participates in — no manual step. The CI drift gate (`cora docs check`) ensures regeneration happens. The worked example on the authored [Adopting a standard](adopting-a-standard.md) page is hand-written, though — consider refreshing it if the new standard makes a better illustration.

## Step 7: Update the CHANGELOG and the corpus-wide README

- `standards/<std>/current/CHANGELOG.md` — record what changed (initial mirror, first inventories extracted, first enrichment, etc.).
- The repo's top-level `README.md` — mention the new standard in the hosted-standards table.

## Step 8: PR + CI

Open the PR. CI runs:

- Ruff / mypy / pytest with 80% coverage
- `cora validate --repo-root .`
- `cora docs check --repo-root .`
- `check-jsonschema` over the new inventory YAMLs and any new crosswalks
- markdownlint / yamllint
- The authored-docs-site build (broken-link check)

All five gates must pass before merge.

---

For deeper details on the *format-extraction* half — protocol shape, config class, fixtures, the "two-source genericity audit" — see [Onboarding a new format](onboarding-a-format.md).
