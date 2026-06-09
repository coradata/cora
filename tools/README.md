# Tooling

Open-source code that powers CORA's validation, generation, and concept-analysis pipelines.

- [`/extractors/`](extractors/) — Python package (`cora-extractors`) that produces per-module field inventories from each standard's native artifacts, plus the validators, generators, and concept-analysis subcommands. The `cora` CLI exposes everything: `cora extract`, `cora validate`, `cora docs build`, `cora docs check`, `cora concepts census`, `cora concepts suggest`, `cora concepts scaffold`, `cora concepts check`, `cora inventory summary`, `cora inventory merge`. See [`extractors/README.md`](extractors/README.md) for details.

Additional tooling (converters from native to derived formats, skill generation) lands as concrete needs surface.

All tooling is Apache 2.0 licensed. Anything in this directory must be reproducible — anyone should be able to rebuild a derived artifact from native source and verify the result.
