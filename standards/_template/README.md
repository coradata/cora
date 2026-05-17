# `_template` — onboarding template for new standards

This directory is a starting point for onboarding a new standard into CORA. It is not a real standard. Tooling that scans `standards/*/` should skip any entry beginning with an underscore.

## How to use

1. Copy `_template/` to `<standard-name>/` (lowercase, no spaces; e.g., `mits`, `redi`, `oscre`).
2. Fill in `PROVENANCE.yaml` with real values (see `_template/PROVENANCE.yaml` for the schema).
3. Place upstream license files in the new directory as `LICENSE-<NAME>-*`.
4. Replace this README with one that describes the standard, links to the upstream owner, and notes the partnership terms.
5. Populate `current/native/` with the bit-identical upstream artifact.
6. Create an initial `current/CHANGELOG.md` entry recording the onboarding.
7. Open a PR. Reference the originating `standard_update.yaml` issue.

See [`docs/onboarding-a-standard.md`](../../docs/onboarding-a-standard.md) for the full walkthrough.
