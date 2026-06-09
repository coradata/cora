# cora-extractors

Field-inventory extractors and the `cora` CLI for the CORA standards corpus. Reads native artifacts (XSD, JSON / CDM-JSON, Excel) from each hosted standard and emits a normalized per-module inventory YAML that crosswalks, the drift register, and the OWL/RDF derivation pipeline (future) can consume.

Ships five extractor adapters (XSD, JSON catalog, CDM-JSON, Excel single-sheet dictionary, Excel multi-sheet dictionary), three validator adapters (inventory-schema, field-count, crosswalk-paths), five generator adapters for the browseable Markdown docs site, and the concepts analyzer (string + semantic clustering, scaffolding, drift gates).

## Install (development)

```bash
pip install -e ".[dev]"
```

The optional `[docs]` extra installs MkDocs Material for the authored site; `[concepts-ml]` installs `sentence-transformers` for the embedding-based concept suggester.

## CLI

```bash
cora --help
cora extract <format> <input> --config <c.yaml> --output <out.yaml>
cora validate                       # inventory-schema + field-count + crosswalk-paths
cora docs build                     # regenerate docs/generated/
cora docs check                     # drift gate
cora concepts census                # field catalogue
cora concepts suggest               # candidate clusters
cora concepts suggest --semantic    # adds the embedding pass
cora concepts scaffold <name> ...   # draft a crosswalk YAML from a cluster or explicit fields
cora concepts check                 # drift gate
cora inventory summary <inv.yaml>   # OWL-aware shape report
cora inventory merge --into A --from B --attribute definition --output M
```

## Lint, type-check, test

```bash
ruff check .
mypy --strict src
pytest -q
```

CI runs all three on every PR; the `concepts-ml` job runs the semantic suggester behind the optional extra so the base workflow stays fast.
