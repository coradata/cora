# Adopting a standard

!!! note "For consumers, not contributors"
    This page is for a data team that already works in one hosted standard and is taking on a second. To *add a new standard to CORA's corpus* (a contributor task), see [Onboarding a standard](onboarding-a-standard.md) instead.

## The problem

You already report in one standard and you're expanding into another. A concrete case: an LP that has always invested in funds and reports in **REDI** starts making **direct multifamily investments** — and suddenly receives operational data shaped like **MITS**. The question isn't "what's the field name for rent in MITS." It's the harder one: *which of this new data do I already understand, which is genuinely new to me, and where does it look like something I know but actually mean something different?*

That last category is where integrations quietly go wrong. You "know" rent — but in REDI it's `Contract_Rent_Qtr`, a quarterly aggregate across all leases; in MITS it's `UnitType/UnitRent`, a per-unit figure. Join them naïvely and your numbers are wrong by a factor you won't notice until someone reconciles a report.

## The adoption briefing

CORA generates a **briefing per ordered pair of hosted standards** — directional, because "I know REDI, adopting MITS" is a different journey from the reverse. Each briefing is a pure projection of the committed crosswalks and partitions every concept into three buckets:

- **① Recognise, but reconcile** — concepts both standards carry. Rows where either side is `partial` or `divergent` are pulled to the top with the caveat spelled out. This is the part worth reading slowly: the fields that look comparable but differ in scope or grain.
- **② New territory** — concepts the standard you're adopting carries that the one you know never modelled. For the LP going direct, this is per-lease dates, unit attributes, tenants, identifiers — operational granularity fund reporting never had.
- **③ Stays home** — concepts you have that the new standard won't carry. Your fund-reporting concepts (`discount_rate`, `investment_type`, `ownership_type`) don't show up in operational data; they remain yours to report.

Each briefing ends with an honest coverage note: CORA maps only what's in the corpus today, and points at the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md) for candidate concepts not yet covered. If the journey needs a concept that isn't mapped, [request a crosswalk](requesting-a-crosswalk.md) — those requests are exactly what prioritises the editorial backlog.

## Where to read them

Browse all pairs at [`docs/generated/adoption/`](https://github.com/coradata/cora/tree/main/docs/generated/adoption), or jump to a specific journey:

| You report in | Adopting | Briefing |
|---|---|---|
| IBPDI | MITS | [ibpdi → mits](https://github.com/coradata/cora/blob/main/docs/generated/adoption/ibpdi-to-mits.md) |
| IBPDI | REDI | [ibpdi → redi](https://github.com/coradata/cora/blob/main/docs/generated/adoption/ibpdi-to-redi.md) |
| MITS | IBPDI | [mits → ibpdi](https://github.com/coradata/cora/blob/main/docs/generated/adoption/mits-to-ibpdi.md) |
| MITS | REDI | [mits → redi](https://github.com/coradata/cora/blob/main/docs/generated/adoption/mits-to-redi.md) |
| REDI | IBPDI | [redi → ibpdi](https://github.com/coradata/cora/blob/main/docs/generated/adoption/redi-to-ibpdi.md) |
| REDI | MITS | [redi → mits](https://github.com/coradata/cora/blob/main/docs/generated/adoption/redi-to-mits.md) |

The briefings regenerate on every change to the crosswalks, so they stay current as the corpus grows and as new standards onboard (the set expands automatically to every ordered pair).

## From the command line

The same briefing renders on demand:

```bash
cora adopt --from redi --to mits --repo-root .
```

Prints the REDI→MITS briefing to stdout — handy for piping into a review doc or reading without leaving the terminal.

## What this is not

The briefing tells you *what corresponds and where the hazards are*. It does not transform your data — it won't convert a REDI quarterly aggregate into per-unit MITS figures, because that roll-up logic depends on your data, not on the schema mapping. Use the briefing to scope the work and avoid the grain traps; the transformation itself stays in your pipeline.

## What to read next

[**Reading a crosswalk**](reading-a-crosswalk.md)
:   The full crosswalk YAML behind every briefing row — confidence labels and the narrative notes the briefing surfaces.

[**Integrating CORA**](integrating-cora.md)
:   Once you've scoped the adoption, the patterns for wiring the mappings into a pipeline.
