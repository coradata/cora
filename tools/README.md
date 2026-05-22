# Tooling

Open-source code that powers CORA's validation and (eventually) the publishing pipeline.

- `/validators/` — schema validators, license-header checks, crosswalk schema validation
- `/extractors/` — Python package (`cora-extractors`) that produces per-module field inventories from each standard's native artifacts. See [`extractors/README.md`](extractors/README.md) and the [field inventory plan](../../internal-planning/CORA-Field-Inventory-Plan.md) for status.

Additional tooling (converters from native to derived formats, skill generation, the `cora` CLI) lands as concrete needs surface.

All tooling is Apache 2.0 licensed. Anything in this directory must be reproducible — anyone should be able to rebuild a derived artifact from native source and verify the result.
