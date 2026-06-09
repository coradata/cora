# CORA

**Common Ontology for Real Assets**

Making real assets standards interpretable by machines and interoperable by meaning.

> Real assets data has always required reconciliation. What has changed is that interpretation can no longer remain manual.

CORA is a vendor-neutral coordination layer for real assets data standards. It provides the shared semantic infrastructure that allows existing standards, systems, and institutional workflows to preserve meaning across asset classes, ownership structures, capital stacks, geographies, and time.

**CORA does not replace existing standards. It gives them a common frame.**

The public-facing project home is [coradata.org](https://coradata.org). This site is the documentation for everyone who consumes CORA's published artifacts — the inventories, crosswalks, and coverage matrix that make cross-standard interpretation possible.

## Who this is for

Data teams at firms whose holdings cross more than one standard — MITS, IBPDI, and REDI today, with more in formation. If your pipelines need to reconcile a field from one standard's schema with the same concept under another's, the artifacts described here are what you reach for. Limited partners, general partners, asset managers, owner-operators, lenders, servicers, and data providers are all represented in the field-level mappings the project maintains.

## Where to start

[**Quickstart**](quickstart.md)
:   Load a crosswalk, look up a concept, apply the mapping. Under ten minutes.

[**Concepts**](concepts.md)
:   The vocabulary CORA publishes — canonical concepts, per-standard mappings, confidence labels, and the shape of an inventory.

[**Consuming inventories**](consuming-inventories.md)
:   Read CORA's YAML artifacts from your own pipeline. Python and SQL patterns.

[**Authoring a crosswalk**](authoring-a-crosswalk.md)
:   Request a new concept mapping when a field your organization needs isn't yet covered.

## What CORA publishes

**Inventories.** A normalized YAML view of one module of one standard. One file per module — fifteen committed today across MITS, IBPDI, and REDI. The format-agnostic substrate everything else reads from.

**Crosswalks.** A YAML mapping one canonical concept to per-standard inventory paths. Confidence labels record how exact each mapping is: `exact`, `close`, `partial`, `divergent`, or `not_present`.

**Coverage matrix.** A single view of concepts × standards with confidence indicators — at-a-glance gap analysis for any team evaluating which fields are safe to rely on across their sources.

All three artifacts live in the repository, regenerate from the YAML on every change, and pass three layers of validation in CI before publication.

## Two structural contributions

CORA's role is narrower and connective: to maintain cross-standard mappings and a longitudinal record of how real assets definitions evolve across standards, versions, and market contexts.

**Cross-standard mapping.** A neutral record of how concepts correspond across multiple standards, schemas, and data models. Individual standards bodies maintain authority over their own work. CORA provides the shared mapping layer.

**Longitudinal record of standards evolution.** A public record of how real assets standards evolve over time, including where definitions converge, diverge, or change across versions.

## Contributing to CORA

The [Contributing](seams.md) section documents the implementation toolkit — the extractor, validator, and generator seams used to maintain the artifacts above. Read it if you're adding a new standard, a new source format, or a new validation rule. Most consumers will never need it.

## Status

Phase 4.5 shipped fifteen inventories (MITS / IBPDI / REDI), an initial six concept crosswalks, three validator adapters, five generator adapters, and five extractor adapters. The concept corpus has since grown to thirty-three crosswalks via the Phase 6 editorial waves; the [suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md) and the [semantic suggestions report](https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions-semantic.md) drive the ongoing additions. CORA itself is in formation; v0.1 public release is anticipated Q2 2026.

The strategic framing of CORA — *why* it exists, the v0.1 scope, the governance perspective, the formation status — lives at [coradata.org](https://coradata.org).

Vendor-neutral · Global by design · Publicly available · Openly licensed.
