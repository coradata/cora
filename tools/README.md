# Tooling

Open-source code that powers CORA's validation and (eventually) the publishing pipeline.

- `/validators/` — schema validators, license-header checks, crosswalk schema validation

Additional tooling (converters from native to derived formats, skill generation, the `cora` CLI) lands as concrete needs surface. Phase 1 ships with validators only.

All tooling is Apache 2.0 licensed. Anything in this directory must be reproducible — anyone should be able to rebuild a derived artifact from native source and verify the result.
