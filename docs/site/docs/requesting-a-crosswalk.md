# Requesting a crosswalk

CORA's published corpus grows with its consumers. When a concept your organization needs isn't yet covered, the request workflow is straightforward and the maintainer turnaround is usually one review cycle.

## When to request

Open a request when:

- You've checked the [crosswalks directory](https://github.com/coradata/cora/tree/main/crosswalks/concepts) and the [coverage matrix](https://github.com/coradata/cora/blob/main/docs/generated/coverage-matrix.md), and the concept genuinely isn't there.
- You've checked the [aliases](finding-a-concept.md#by-alias) of existing crosswalks — the concept might already be covered under a different canonical name.
- The concept is **leaf-level**. Type-level concepts ("the whole address") are out of scope for the current schema. Stick to single-field concepts like `postal_code`, `last_name`, `lease_term_months`.

## What to include

A request that's easy to act on names:

| | |
|---|---|
| **The concept** | A lowercase snake_case name (`unit_size_sqft`, `pet_deposit_amount`). If you're not sure of the canonical name, propose one and explain. |
| **A working definition** | One or two sentences describing what the concept means. Doesn't have to be polished; the maintainers will refine. |
| **Aliases** | Any vendor or schema names you've seen for the same concept. |
| **Where you've seen it** | Which standards' schemas your organization works with, and which fields you believe correspond. |
| **Why it matters** | A sentence on the use case. Helps maintainers prioritize. |

A complete example is worth more than a polished one. If you've already identified the field path in MITS, IBPDI, or REDI, include it — that's most of the mapping work.

## How to file

Open an issue on the repository, [`coradata/cora`](https://github.com/coradata/cora/issues), titled `Crosswalk request: <concept_name>`. The maintainers triage requests on a published cadence and surface them in the public review channel.

Issues marked `crosswalk-request` are visible in the repository's filtered view; subscribe to be notified when one merges.

## If you want to contribute the crosswalk yourself

Many organizations have done the mapping work internally and have something close to a finished crosswalk in their own documentation. Contributing that work upstream — under your team's review and CORA's CI gates — is welcomed.

The contributor walkthrough is under [Authoring a crosswalk](authoring-a-crosswalk.md). It covers the YAML shape, the validator gates, and how to open the pull request. The technical work is small; the editorial work (writing the canonical definition, picking the confidence label, justifying `divergent` or `not_present` mappings) is what the review focuses on.

## Maintenance after merge

Once a crosswalk is merged, it lives in the corpus and benefits from the same CI gates as the rest: schema validation, path resolution, and field-count checks on every PR. Standard version bumps surface as drift-register items so re-verification happens openly.

Crosswalks carry a `last_reviewed` date. Even when nothing structurally changes, an aging crosswalk should be re-eyeballed; a refresh PR with a new date is a low-cost contribution that strengthens consumer trust.

## What to read next

[**Finding a concept**](finding-a-concept.md)
:   Before requesting, the lookup workflow that confirms the concept isn't already there under another name.

[**Authoring a crosswalk**](authoring-a-crosswalk.md)
:   The contributor walkthrough for opening the pull request yourself.
