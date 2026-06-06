# ADR-0002 — MkDocs Material for the Phase 5 Authored Documentation Site

- **Date:** 2026-06-05
- **Status:** Accepted
- **Phase:** 5 (authored documentation site)

## Context

Phase 4.5 ships a generated Markdown view of the corpus (`docs/generated/`) that GitHub renders natively. Phase 5 adds a separate **authored** documentation site — hand-written prose teaching a developer how to use CORA. It needs to live somewhere richer than GitHub's default Markdown rendering: real navigation, full-text search, syntax highlighting, theme, broken-link enforcement.

Two realistic options for the static-site generator:

1. **MkDocs Material** — Python static-site generator + popular theme. Markdown-native. Single config file. Strict mode for broken-link CI.
2. **Sphinx + Furo** — Python static-site generator + popular theme. reStructuredText native (Markdown via MyST). More configuration ceremony but stronger API auto-documentation.

## Decision

Use **MkDocs Material**.

## Rationale

| Criterion | MkDocs Material | Sphinx + Furo | Winner |
|---|---|---|---|
| Source format | Markdown native | reST native; Markdown via MyST plugin | MkDocs (existing docs are Markdown) |
| Setup ceremony | Single `mkdocs.yml` | `conf.py` + Makefile + extension list | MkDocs |
| Mermaid support | Trivial via `pymdownx.superfences` | Needs `sphinxcontrib-mermaid` | MkDocs (Phase 4.5 emits Mermaid) |
| Search | Built-in client-side; zero infra | Same | Tie |
| Strict mode (broken-link CI gate) | `mkdocs build --strict` | `sphinx-build -W` | Tie |
| API auto-documentation | Plugin (`mkdocstrings`) | Built-in (autodoc) | Sphinx |
| Dev loop | `mkdocs serve` live-reload | `sphinx-autobuild` | Tie |
| Theme quality out-of-box | Material is polished by default | Furo is also good | Tie |
| Adoption in Python ecosystem | FastAPI, Pydantic, Material-UI | Python, Django, NumPy, SciPy | Both strong |

Sphinx's autodoc advantage doesn't apply: CORA's Python module (`cora_extractors`) is internal tooling, not a public library with documented APIs. The protocols are documented by hand in the seams page anyway. We pay Sphinx's setup ceremony for a feature we don't use.

MkDocs Material's Markdown-native source means our existing artifacts ([CONTEXT.md](../../CONTEXT.md), [field-inventory.md](../field-inventory.md), [ADR-0001](0001-enrich-vs-merge.md), the Phase 4.5 generated tree) drop into the site without conversion.

## Consequences

- New optional-dependencies group in `tools/extractors/pyproject.toml`: `docs` pulls `mkdocs-material` and Mermaid support via `pymdownx.superfences`.
- Site sources live at `docs/site/` (separate from Phase 4.5's `docs/generated/`).
- New CI workflow `.github/workflows/docs-site.yaml`: strict build on PRs (`mkdocs build --strict`), deploy to `gh-pages` on main merges.
- Promotion path if MkDocs ever stops fitting: the Markdown source is portable; switching to Sphinx + MyST would be a config migration, not a content rewrite.

## Alternatives considered

- **Sphinx + Furo + MyST** — rejected per the table above. The Markdown-via-MyST path makes Sphinx tolerable but adds a translation layer for no compensating benefit.
- **Plain GitHub-rendered Markdown** (no static-site generator) — already the Phase 4.5 model. Insufficient for narrative content: no full-text search, no styled navigation, no broken-link gate beyond manual review.
- **Docusaurus, VuePress, Astro Starlight** — JavaScript-toolchain options. All capable, but pulling Node into a Python-tooled repo adds a build system; not worth it for a documentation site.

## References

- [Phase 5 plan section](../../../internal-planning/CORA-Field-Inventory-Plan.md)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Sphinx + Furo](https://pradyunsg.me/furo/)
