# Onboarding a Standard

This guide covers what happens between "a standards body agrees to participate in CORA" and "their first content lands on `main`." Target time: under an hour of focused work, assuming the upstream artifact is in hand and partnership terms are agreed.

The contributor doing this work is typically a CORA maintainer, sometimes paired with someone from the standards body. The body itself does not need to file PRs to participate — agreeing to terms and confirming the artifact and license posture is enough.

## Preconditions

Before starting, confirm all of the following:

1. **Partnership terms are agreed.** What CORA can redistribute, what attribution is required, what restrictions apply. Captured in writing somewhere — at minimum a thread or document the maintainer team can reference. The summary lands in the new standard's `PROVENANCE.yaml`.
2. **The upstream artifact is in hand.** A specific version, downloaded from the body's own distribution channel, with the upstream version label and (if available) a SHA or release date.
3. **License posture is documented.** The exact license terms applying to redistribution. If the body uses a standard license (CC BY 4.0, MIT, Apache 2.0), the upstream license text travels with the content. If the body uses a custom license, that text travels too.
4. **A `standard_update.yaml` issue exists.** Filed when partnership terms were being negotiated. The onboarding PR will close it.

If any of these are missing, stop and resolve before continuing. Most onboarding failures come from skipping this step.

## Steps

### 1. Branch and copy the template

```bash
cd ~/cora-workspace/cora
git checkout -b onboard-<standard-shortname>

# Replace <standard> with the lowercase short name (e.g. mits, redi, oscre)
cp -r standards/_template standards/<standard>
```

### 2. Fill in PROVENANCE.yaml

Replace every `REPLACE_WITH_*` value in `standards/<standard>/PROVENANCE.yaml`. Be honest about partnership status — `participating: true` only if the body has signed something explicit; otherwise `participating: false` and a clear note about the relationship.

### 3. Attach upstream license files

Copy the upstream license texts into the standard's directory, named `LICENSE-<STANDARD>-Docs`, `LICENSE-<STANDARD>-Code`, or similar depending on what the body publishes. The CORA repo's root `LICENSE` and `LICENSE-Docs` cover CORA's own work; upstream licenses cover the mirrored content.

### 4. Place the native artifact

Copy the bit-identical upstream content into `standards/<standard>/current/native/`. Do not edit, reformat, or "clean up" anything. Faithfulness to the upstream is the contract.

If the upstream content is bytes (PDF, XLSX, XSD), commit it as-is. If it's text, preserve line endings and encoding. If the upstream uses Git itself (like IBPDI), preserve the file structure but omit `.git/` and similar metadata.

### 4a. Extract the field inventory

After the native artifact is in place, run the inventory extractor for the relevant format and commit the per-module inventory YAML files to `standards/<standard>/current/inventory/<module>.yaml`. See [`docs/field-inventory.md`](./field-inventory.md) for the format and path grammar.

Five extractor adapters ship today: XSD, JSON catalog, CDM-JSON, Excel single-sheet dictionary, and Excel multi-sheet dictionary. See [`tools/extractors/README.md`](../tools/extractors/README.md) for the full CLI surface. If a standard's native format isn't covered by an existing adapter, ship the native artifact and PROVENANCE first; the inventory backfill follows once a new adapter exists ([`docs/site/docs/onboarding-a-format.md`](site/docs/onboarding-a-format.md) walks through adding one).

### 5. Write the standard's README

Replace the template README at `standards/<standard>/README.md` with one that covers:

- Who owns the standard (with link to their homepage)
- What's mirrored (which version, when fetched)
- The partnership terms in plain language
- Pointers to the upstream's authoritative version

Keep it short. Two or three paragraphs.

### 6. Create the initial CHANGELOG entry

Replace the template `current/CHANGELOG.md` with an initial entry recording the onboarding date, upstream version, and partnership status.

### 7. Open the PR

```bash
git add standards/<standard>/
git commit -m "Onboard <standard>: <upstream-version>"
git push origin onboard-<standard-shortname>
gh pr create --fill --base main
```

In the PR description:

- Reference the `standard_update.yaml` issue (`Closes #N`)
- Note the partnership status and link to the partnership record
- Flag any unusual license terms reviewers should check
- Confirm CI is green before requesting review

### 8. Review and merge

Routed to `@coradata/maintainers` (and the per-standard working group when those exist). Reviewers verify:

- PROVENANCE.yaml is accurate
- Upstream license files are present and correctly named
- Native content is bit-identical to upstream
- README accurately describes the partnership

On merge, downstream automation runs (when those workflows exist — see Future Phases in the Setup Plan).

### 9. Update the corpus map

After merge, update `standards/README.md` to move the standard from "Target corpus" to "Current contents" with the appropriate status. This is a small follow-up PR, not part of the onboarding PR itself — keeps each PR focused.

## What this guide is not

- **Not a partnership negotiation guide.** That happens in conversations, not in this repo.
- **Not a derivation guide.** Producing the OWL/RDF, JSON-LD, and JSON Schema derivations is separate work that happens once the derivation pipeline exists. Onboarding lands the native content; derivations come later.
- **Not a crosswalk guide.** Cross-standard mappings are independent. Onboarding a standard does not require any crosswalks to exist.

## Questions

Open a discussion at [github.com/coradata/cora/discussions](https://github.com/coradata/cora/discussions). Onboarding is meant to be done by anyone confident with `git` and `gh`; if the steps above aren't enough, the docs need to improve.
