# Standards

Each subdirectory here holds a hosted real assets data standard. A directory exists for a standard only when there is real content for it. Directories are not pre-created for bodies that haven't engaged.

## Layout per standard

```
/standards/<name>/
  /current/             -> pointer to latest version
  /<version>/
    native/             # owner's authoritative artifact, bit-identical
    ontology/           # OWL/RDF derivation
    jsonld/             # JSON-LD context
    jsonschema/         # JSON Schema
    mapping.yaml        # element-by-element derivation map
    CHANGELOG.md        # changelog
  PROVENANCE.yaml       # source URL, version, license, fetch metadata
  LICENSE-<name>-*      # upstream license attribution
  README.md             # what's here, link to upstream owner
```

## Current contents

| Directory | Status | Notes |
|---|---|---|
| `ibpdi/` | Bootstrap mirror | CC BY 4.0 + MIT, mirrored from github.com/ibpdi/cdm |
| `mits/` | Participating | Mirrored from rettc.org/mits-data-models under permission from RETTC |
| `redi/` | Participating | Mirrored from realestatedatainitiative.netlify.app under permission from the REDI Data Model Sub-Committee |
| `_template/` | Onboarding template | Copy this when a new standard is being onboarded |

## Target corpus

The full list of standards CORA aims to host. A directory does not exist until partnership terms are agreed and content lands.

| Standard | Status | Notes |
|---|---|---|
| IBPDI | Hosted (bootstrap mirror) | See `ibpdi/` |
| RETTC MITS | Hosted (participating) | See `mits/` |
| OSCRE | Future invitation | OSCRE owns Smart Data Highway; CORA does not produce a competing commercial RE ontology |
| REDI | Hosted (participating) | See `redi/` |
| NCREIF / PREA | Future invitation | |
| INREV / ANREV | Future invitation | |
| CREFC IRP | Future invitation | Commercial real estate debt |
| MSCI | Future invitation | Real estate investment performance and analytics |
| MISMO | Future invitation, scope-bounded | Crosswalks at the real-estate-finance boundary only |
| GRESB | Future invitation | ESG benchmarking |
| RICS | Future invitation | Valuation standards |

"Future invitation" means CORA's openness to participation is on the record. It does not mean the body has committed.

## Onboarding a new standard

See [`docs/onboarding-a-standard.md`](../docs/onboarding-a-standard.md) for the step-by-step. The short version: copy `standards/_template/` to `standards/<name>/`, fill in `PROVENANCE.yaml`, place upstream license files, write the initial `README.md`, open a PR.
