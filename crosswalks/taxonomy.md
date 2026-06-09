# Crosswalk taxonomy

The vocabulary CORA's crosswalks live inside — the conceptual buckets that organize the corpus, the naming conventions every concept follows, and the editorial decision tree for picking a confidence label. Read this before authoring a new crosswalk; it answers most of the editorial questions reviewers raise.

The corpus is leaf-level by design: one crosswalk per single field, never per composite type. "The address concept" is out of scope; "the postal code part of an address" is in scope. The schema in [`schema/crosswalk.schema.json`](schema/crosswalk.schema.json) enforces this — `mappings.<std>.field` is a single inventory path, not a list.

## Conceptual buckets

The corpus organizes naturally into seven buckets. Buckets are an editorial convention rather than a structural one — the YAML carries no `bucket:` field — but they're useful for review and for finding gaps. Each bucket is a coherent slice of real-assets domain language.

### Address

Postal addressing and geography. The smallest, cleanest bucket — every standard models a postal address, even if the field names differ.

- [`city`](concepts/city.yaml), [`country`](concepts/country.yaml), [`postal_code`](concepts/postal_code.yaml), [`state_province`](concepts/state_province.yaml), [`street_address`](concepts/street_address.yaml)

### Identity & contact

The natural-person and contact-method concepts. MITS models these richly via `PersonType` and `PhoneType`; IBPDI scopes contacts to `Contact` with name + job-title only (no email, no phone); REDI carries only an email + name pair at the fund-reporting level.

- [`email_address`](concepts/email_address.yaml), [`first_name`](concepts/first_name.yaml), [`last_name`](concepts/last_name.yaml), [`job_title`](concepts/job_title.yaml), [`phone_number`](concepts/phone_number.yaml)

### Identifiers

Opaque keys for real-world entities — buildings, units, organisations, spaces, equipment, transactions. IBPDI uses a consistent identifier-string pattern across many entities (`Unique identifier either coming from previous system…`), which the semantic suggester clusters cleanly.

- [`building_id`](concepts/building_id.yaml), [`organisation_id`](concepts/organisation_id.yaml), [`serial_number`](concepts/serial_number.yaml), [`space_number`](concepts/space_number.yaml), [`transaction_id`](concepts/transaction_id.yaml), [`unit_id`](concepts/unit_id.yaml)

### Lease dates

The temporal anchors of a lease. MITS distinguishes contractual (`Expected*`) from observed (`Actual*`); IBPDI tracks contract start/end on `RentalContract` only. REDI does not surface per-lease dates at all (`not_present` across all four).

- [`lease_start_date`](concepts/lease_start_date.yaml), [`lease_end_date`](concepts/lease_end_date.yaml), [`move_in_date`](concepts/move_in_date.yaml), [`move_out_date`](concepts/move_out_date.yaml)

### Lease economics

The monetary attributes of a lease. MITS uses `UnitType/UnitRent` (contracted) and `UnitType/MarketRent` (asking); IBPDI uses `RentalPayment/ValueMonth`; REDI aggregates at fund / quarter grain (`Contract_Rent_Qtr`, `Market_Rent_Next_12_Months`) — `divergent` rather than `not_present` because the concept exists but the grain differs.

- [`market_rent`](concepts/market_rent.yaml), [`rent_amount`](concepts/rent_amount.yaml), [`payment_frequency`](concepts/payment_frequency.yaml)

### Financial / investment

Fund-level and accounting concepts, anchored in REDI's LP-investment-reporting view of the world. IBPDI pivots most of these.

- [`accounting_standard`](concepts/accounting_standard.yaml), [`currency`](concepts/currency.yaml), [`discount_rate`](concepts/discount_rate.yaml), [`investment_type`](concepts/investment_type.yaml), [`ownership_type`](concepts/ownership_type.yaml)

### Unit & space attributes

Physical attributes of a leasable unit or space. MITS is residential-flavored and models per-unit attributes (bedrooms, bathrooms, square footage) on its `UnitType`. IBPDI surfaces methodology metadata (`AreaMeasurement` — Standard, Unit, Accuracy) but no numeric area value. REDI aggregates at asset level (`Net_Rentable_Area`).

- [`area_unit_of_measurement`](concepts/area_unit_of_measurement.yaml), [`bathroom_count`](concepts/bathroom_count.yaml), [`bedroom_count`](concepts/bedroom_count.yaml), [`space_type`](concepts/space_type.yaml), [`square_footage`](concepts/square_footage.yaml)

## Naming conventions

The concept name is the file's identity — it's the `concept:` field, the filename minus `.yaml`, and the URL slug consumers reach for. Get it right.

| Rule | Example |
|---|---|
| Lowercase snake_case. No spaces, hyphens, or camelCase. | `postal_code`, not `PostalCode` or `postal-code`. |
| Descriptive over abbreviated. | `transaction_id`, not `txn_id`; `phone_number`, not `phone`. |
| Singular over plural. | `bedroom_count`, not `bedrooms`. The count is the concept; the noun is in the alias. |
| Domain-explicit when the bareword is ambiguous. | `market_rent` and `rent_amount` rather than two `rent` crosswalks. |
| Standard-neutral. | `organisation_id` (one canonical spelling), not `corporate_id` (MITS-flavored) or `org_id` (abbreviated). |
| Aliases carry the variants. | `organisation_id` has aliases `organization_id`, `org_id`, `corporate_id`, `company_id`. |

The aliases list is where dialect, casing variation, and vendor names live. A repository grep against `aliases:` is the fastest path from a vendor's field name to the right crosswalk (see [Finding a concept](../docs/site/docs/finding-a-concept.md)).

## Confidence vocabulary

Every mapping in every crosswalk carries one of five confidence labels. The label is editorial — the maintainer's honest assessment of how well the two fields align — and the schema enforces that `divergent` and `not_present` carry narrative notes.

The decision tree:

```
Does the standard have a field that could plausibly map to this concept?
├── Yes
│   ├── Same name (modulo casing), same semantics, same shape?
│   │   ├── Yes → exact
│   │   └── No → continue
│   ├── Minor name / formatting differences only, same semantics?
│   │   ├── Yes → close
│   │   └── No → continue
│   ├── Same concept but meaningful scope, grain, or definition difference?
│   │   ├── Yes → partial   (requires narrative notes by convention)
│   │   └── No → continue
│   └── Same word, different concept entirely?
│       └── divergent       (requires narrative notes per schema)
└── No
    └── not_present         (requires field: null + narrative notes per schema)
```

Worked examples from the corpus:

- **`exact`** — `city` across all three standards: same name, same string-valued city-name semantics.
- **`close`** — `phone_number`'s MITS mapping (`PhoneType/PhoneNumber`). The MITS path is a richer complex (carries Extension, PhoneType, PhoneDescription) — semantically equivalent for the leaf-level concept but the surrounding shape differs.
- **`partial`** — `lease_start_date`'s MITS mapping (`LeaseType/ExpectedMoveInDate`): contractual vs. observed ambiguity. Same concept, meaningful scope difference.
- **`divergent`** — `rent_amount`'s REDI mapping (`Contract_Rent_Qtr`): the concept exists but at a different grain (fund / quarter aggregate vs. per-lease monthly). Reconciliation requires summing and aligning periods.
- **`not_present`** — `move_in_date`'s IBPDI mapping: IBPDI's rental model surfaces the contract (`RentBeginDate`) but no observed move-in event. The concept genuinely does not exist in this standard.

`not_present` and `divergent` are deliberately distinct. `not_present` means *the concept is absent*; `divergent` means *the concept is present but means something else here*. The narrative note for each is what makes a consumer's reconciliation possible — write it for the engineer who'll integrate against the gap, not as filler.

## When a crosswalk is one-standard-only

Some concepts exist meaningfully in only one of the three hosted standards. `bedroom_count` and `bathroom_count` are MITS-only — IBPDI's `RentalUnit` carries no residential attributes, and REDI is fund-level. These crosswalks still ship: the value is in documenting the gap. A consumer reconciling MITS resident data with IBPDI personnel needs to see one place that says "there is no IBPDI counterpart, here's why."

The schema permits one mapping (`minProperties: 1` on `mappings`), but by convention every published crosswalk lists all three hosted standards. The standards that don't carry the concept ship with `field: null`, `confidence: not_present`, and a one-paragraph narrative explaining the absence.

## Boundary crosswalks

A `boundary: true` flag in the YAML marks a crosswalk that connects CORA's corpus to an adjacent ontology CORA does not host (MISMO mortgage operations, RealEstateCore building systems, OSI analytics conventions). None exist in the corpus yet. Phases beyond 6 will surface candidates; the schema is ready.

## When to add a new bucket

A new bucket earns its place when at least three crosswalks naturally live there and the bucket name names a real editorial through-line a reviewer can articulate. Don't pre-emptively create empty buckets; let the corpus push them out.

Buckets aren't structural — there's no `bucket:` field in the YAML — so renaming or splitting a bucket is editorial and reversible. If a bucket grows past ~10 concepts and starts to lose coherence, split it; if two adjacent buckets share more concepts than they don't, merge them.

## What to read next

- [`README.md`](README.md) — the directory layout and the boundary-crosswalk convention.
- [Authoring a crosswalk](../docs/site/docs/authoring-a-crosswalk.md) — the contributor walkthrough from blank YAML to a passing CI build.
- [Finding a concept](../docs/site/docs/finding-a-concept.md) — the lookup workflow for consumers.
- [Requesting a crosswalk](../docs/site/docs/requesting-a-crosswalk.md) — when the concept isn't yet in the corpus.
