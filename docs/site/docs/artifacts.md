# What CORA publishes

Three artifacts. Each one is YAML or Markdown, regenerates on every change, and passes validation in CI before it appears in the repository. All three are openly licensed and available for any team to read, fork, or integrate.

## Inventories

A normalized YAML view of one module of one standard. Fifteen committed today, organized by standard and module:

| Standard | Modules | Path |
|---|---|---|
| **MITS** | 7 — accounts-payable, collections, lead-management, lease-application, property-marketing, resident-screening, resident-transactions | [`standards/mits/current/inventory/`](https://github.com/coradata/cora/tree/main/standards/mits/current/inventory) |
| **IBPDI** | 7 — digital-twin, energy-and-resources, financials, organisational-management, portfolio-and-asset-management, property-management, user-and-customer-experience | [`standards/ibpdi/current/inventory/`](https://github.com/coradata/cora/tree/main/standards/ibpdi/current/inventory) |
| **REDI** | 1 — data-fields | [`standards/redi/current/inventory/`](https://github.com/coradata/cora/tree/main/standards/redi/current/inventory) |

Every inventory carries the same top-level shape regardless of whether the source artifact was XSD, JSON, or Excel. The format-agnostic substrate makes one inventory walkable with the same loader as any other.

The full inventory shape, and patterns for walking it from Python, lives under [Consuming inventories](consuming-inventories.md).

## Crosswalks

A YAML mapping one canonical concept to per-standard inventory paths. Twenty-eight committed today:

- [`accounting_standard`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/accounting_standard.yaml)
- [`area_unit_of_measurement`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/area_unit_of_measurement.yaml)
- [`building_id`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/building_id.yaml)
- [`city`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/city.yaml)
- [`country`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/country.yaml)
- [`currency`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/currency.yaml)
- [`discount_rate`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/discount_rate.yaml)
- [`email_address`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/email_address.yaml)
- [`first_name`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/first_name.yaml)
- [`investment_type`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/investment_type.yaml)
- [`job_title`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/job_title.yaml)
- [`last_name`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/last_name.yaml)
- [`lease_end_date`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/lease_end_date.yaml)
- [`lease_start_date`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/lease_start_date.yaml)
- [`market_rent`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/market_rent.yaml)
- [`move_in_date`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/move_in_date.yaml)
- [`move_out_date`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/move_out_date.yaml)
- [`organisation_id`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/organisation_id.yaml)
- [`ownership_type`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/ownership_type.yaml)
- [`payment_frequency`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/payment_frequency.yaml)
- [`postal_code`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/postal_code.yaml)
- [`rent_amount`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/rent_amount.yaml)
- [`serial_number`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/serial_number.yaml)
- [`space_number`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/space_number.yaml)
- [`space_type`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/space_type.yaml)
- [`state_province`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/state_province.yaml)
- [`street_address`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/street_address.yaml)
- [`unit_id`](https://github.com/coradata/cora/blob/main/crosswalks/concepts/unit_id.yaml)

Each crosswalk lists the canonical concept, aliases, a working definition, and one mapping block per participating standard. The mapping block names the inventory path, the standard version it's verified against, and the confidence label.

Crosswalks are the unit a consuming team reaches for. One concept, three sources, one record. The shape lives under [Reading a crosswalk](reading-a-crosswalk.md). The discovery workflow for finding the right one lives under [Finding a concept](finding-a-concept.md).

## Coverage matrix

A single Markdown table showing every committed concept against every participating standard, with confidence indicators. Regenerates on every PR that touches a crosswalk or inventory. Lives at [`docs/generated/coverage-matrix.md`](https://github.com/coradata/cora/blob/main/docs/generated/coverage-matrix.md).

The matrix is the at-a-glance answer to *which fields can my pipeline rely on across the sources I actually receive?* — green for `exact`, less-green for `close`, amber for `partial`, red for `divergent`, dash for `not_present`.

## Generated concept pages

Each concept also has an auto-generated Markdown page that combines the mappings table, the cross-standard graph, and a link back to the source YAML. Browseable under [`docs/generated/concepts/`](https://github.com/coradata/cora/tree/main/docs/generated/concepts).

These pages are mechanical projections of the same crosswalk YAML — useful for quick visual inspection in a browser or pull-request diff, but the YAML is the authoritative source any pipeline should read.

## Generated inventory pages

Each inventory also has an auto-generated Markdown view of its types and fields, useful for surveying what a standard's module covers before deciding which concept crosswalks apply. Browseable under [`docs/generated/inventories/`](https://github.com/coradata/cora/tree/main/docs/generated/inventories).

## Concept-corpus analyzer output

The repository also ships a flat catalogue of every leaf field in the corpus, plus a periodically-refreshed report of candidate concept clusters that *could* be crosswalked but aren't yet. These artifacts surface the gap between *what CORA covers today* and *what the inventory corpus implies CORA could cover.*

- [`docs/concepts-analysis/field-census.csv`](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/field-census.csv) — one row per leaf field across every committed inventory. Sortable in any spreadsheet; the canonical input for tooling that needs an exhaustive view of the corpus.
- [`docs/concepts-analysis/field-census.md`](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/field-census.md) — counts by standard and by module. The at-a-glance summary.
- [`docs/concepts-analysis/suggestions.md`](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md) — candidate concept clusters from the string-similarity pass: leaf names that appear in two or more standards, ordered with uncovered candidates first. Each cluster lists its member fields, the standards touched, and a quality signal (definition-Jaccard).
- [`docs/concepts-analysis/suggestions-semantic.md`](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions-semantic.md) — candidate concept clusters from the semantic-embedding pass: fields whose `leaf_name :: definition` text is close under a sentence-transformers embedding model, surfacing matches the bare-string pass misses (e.g. `MoveInDate` ↔ `LeaseStartDate`). Noisier than the string pass; review each cluster carefully.

The crosswalks committed today are an explicit starter set. The suggestions report names the obvious next set of concepts to add, and the corpus expands in waves of editorial review against that report.

## Validation gates

Every artifact in the repository passes three validation gates before publication:

| Gate | Checks |
|---|---|
| **Schema** | Every inventory and every crosswalk conforms to its JSON Schema and the structural invariants the loaders depend on. |
| **Field count** | Every inventory clears its per-module minimum field count — catches silent extractor regressions. |
| **Crosswalk paths** | Every `mappings.<std>.field` resolves against the standard's committed inventories. `not_present` requires `field: null` plus narrative notes; `divergent` requires narrative notes. |

A pull request that breaks any gate cannot merge.

## Versioning

Inventories carry the standard-body-assigned version label of the source artifact they were extracted from. Crosswalk mapping blocks carry the version they were verified against. When a standard publishes a new release, the drift register surfaces which mappings need re-verification — that work happens openly in the repository.

---

Next: **[Quickstart](quickstart.md)** — find a concept, read the crosswalk, apply the mapping in your pipeline.
