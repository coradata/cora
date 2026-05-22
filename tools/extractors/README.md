# cora-extractors

Field inventory extractors for the CORA standards corpus. Reads native artifacts (XSD, JSON, Excel) from each hosted standard and emits a normalized per-module inventory YAML that crosswalks, the drift register, and (in a later phase) the OWL/RDF derivation pipeline can consume.

This is the Phase 0 scaffold — the package is wired up with dependencies, lint, type-check, and a smoke test, but no extractor logic has been implemented yet. See `internal-planning/CORA-Field-Inventory-Plan.md` for the multi-phase roadmap.

## Install (development)

```bash
pip install -e ".[dev]"
```

## CLI

```bash
cora-extract --help
```

## Lint, type-check, test

```bash
ruff check .
mypy src/cora_extractors
pytest
```
