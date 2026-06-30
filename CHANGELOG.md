# Changelog

All notable changes to CORA are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); CORA's first tagged release will bundle the work below as `v0.1.0`.

For per-standard upstream version history see each standard's `current/CHANGELOG.md`:

- [`standards/ibpdi/current/CHANGELOG.md`](standards/ibpdi/current/CHANGELOG.md)
- [`standards/mits/current/CHANGELOG.md`](standards/mits/current/CHANGELOG.md)
- [`standards/redi/current/CHANGELOG.md`](standards/redi/current/CHANGELOG.md)

For per-PR detail see the [merged pull-request list](https://github.com/coradata/cora/pulls?q=is%3Apr+is%3Amerged) and the [release notes](https://github.com/coradata/cora/releases).

## v0.1.0 — 2026-06-30

### Added

- **Three hosted standards** with native artifacts and `PROVENANCE.yaml`: IBPDI Common Data Model (bootstrap mirror under CC BY 4.0 + MIT); MITS (participating under permission from RETTC); REDI Data Model 1.0 (participating under permission from the REDI Data Model Sub-Committee).
- **Fifteen field inventories** — seven MITS modules (accounts-payable, collections, lead-management, lease-application, property-marketing, resident-screening, resident-transactions), seven IBPDI clusters (digital-twin, energy-and-resources, financials, organisational-management, portfolio-and-asset-management, property-management, user-and-customer-experience), and one REDI sheet (data-fields). Combined: 496 types, 3,353 fields.
- **Thirty-three concept crosswalks** under [`crosswalks/concepts/`](crosswalks/concepts/) covering address, identity & contact, identifiers, lease dates, lease economics, financial / investment, and unit & space attributes. See [`crosswalks/taxonomy.md`](crosswalks/taxonomy.md) for the bucket structure and the confidence-label decision tree.
- **Five extractor adapters** at the `Extractor` seam: `xsd`, `json_catalog`, `cdm_json`, `excel_dictionary`, `excel_multisheet`. Generic by construction — each adapter ships with a two-source genericity audit.
- **Three validator adapters** at the `Validator` seam: `inventory-schema`, `field-count`, `crosswalk-paths`. All wired into CI as drift gates.
- **Five generator adapters** producing the Markdown browse view under [`docs/generated/`](docs/generated/) — inventory pages, concept pages with Mermaid graphs, a coverage matrix, and a concept-overview index. Regenerates on every change; drift-gated by `cora docs check`.
- **`Inventory.enrich` operation** with multi-source provenance and unmatched-other audit — see [ADR-0001](docs/adr/0001-enrich-vs-merge.md). Used today on four MITS modules to enrich XSD-derived inventories with Excel data-dictionary definitions.
- **Concepts analyzer** — `cora concepts census` / `suggest` / `--semantic` / `scaffold` / `check`. The semantic pass uses `sentence-transformers/all-MiniLM-L6-v2` behind the optional `[concepts-ml]` extra and a separate CI job.
- **Authored documentation site** at [`docs/site/`](docs/site/) using MkDocs Material — see [ADR-0002](docs/adr/0002-mkdocs-material-for-authored-docs.md). Deploys to [coradata.github.io/cora](https://coradata.github.io/cora/) via GitHub Pages.
- **Governance artifacts**: `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `governance/CLA.md`, `governance/SECURITY.md`, per-standard `PROVENANCE.yaml`, repo-level `LICENSE` (Apache 2.0) and `LICENSE-Docs` (CC BY 4.0).
- **CI gates**: ruff, mypy `--strict`, pytest with coverage, yamllint, markdownlint, `check-jsonschema`, MkDocs strict-build broken-link gate, license-header check.

### Notes on positioning

CORA does not invent its own ontology of real assets. It hosts, translates, and connects the ones that exist. Cherre is the bootstrap custodian; the role is time-bounded and the destination is neutral foundation governance. See [`README.md`](README.md) for the full custodianship statement.

The drift register taxonomy is documented in [`drift/README.md`](drift/README.md) but the register itself is empty today — inter-standard divergences ship under the per-crosswalk `notes` blocks (see, e.g., the `divergent` mappings on `rent_amount` and `market_rent`). Consolidation into a standalone register lands when a hosted standard version-bumps or a fourth standard onboards.
