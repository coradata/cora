# CORA

**Common Ontology for Real Assets**

CORA is a public, vendor-neutral home for the data standards that describe real assets — real estate (equity and debt) and infrastructure — as a coherent, machine-interpretable corpus. We host each standard in its native format, republish it in derived ontology and interchange formats, ship AI skills and agent definitions built on those standards, and maintain a public register of how definitions drift between versions and between standards.

This repository is the canonical source for everything CORA publishes. The public-facing project home is [coradata.org](https://coradata.org).

> **Current state.** Three hosted standards (IBPDI, MITS, REDI). Fifteen committed field inventories — 496 types and 3,353 fields combined. Thirty-three cross-standard concept crosswalks with explicit confidence labels. Five extractor adapters, three validator adapters, and five generator adapters under the `cora` CLI, all running under CI on every change. Licensed Apache 2.0 (code) + CC BY 4.0 (specifications and documentation). See the [CHANGELOG](CHANGELOG.md) for the per-release breakdown.

## Documentation

- **Authored docs site** — [coradata.github.io/cora](https://coradata.github.io/cora/) (built from [`docs/site/`](docs/site/) by MkDocs Material; deployed from `main`)
- **Generated browse view** — [`docs/generated/`](docs/generated/) — every committed inventory and crosswalk as Markdown with Mermaid graphs
- **Inventory contract + path grammar** — [`docs/field-inventory.md`](docs/field-inventory.md)
- **Crosswalk taxonomy** — [`crosswalks/taxonomy.md`](crosswalks/taxonomy.md) — the conceptual buckets, naming conventions, and the editorial decision tree for confidence labels
- **Architecture decisions** — [`docs/adr/`](docs/adr/) — ADR-0001 (`Inventory.enrich`), ADR-0002 (MkDocs Material)
- **Domain vocabulary** — [`CONTEXT.md`](CONTEXT.md) — canonical glossary for terms used across code, ADRs, and crosswalks

---

## Why CORA exists

Real assets run on a stack of data standards built in different decades, by different bodies, for different audiences. MITS is built for multifamily operations. OSCRE's Industry Data Model is built for commercial transactional data. REDI is built for LP investment reporting. NCREIF, INREV, ANREV, and PREA cover regional reporting alignment. CREFC covers debt. MISMO covers residential mortgage. IBPDI covers global building performance and ESG. Each is correct in its own scope. None speaks the same dialect as the others.

That was a tolerable cost when humans were the integrators. It is not a tolerable cost in a world where AI agents are expected to reason across an entire portfolio, fund, or allocator exposure without escalating to a person to translate the schema.

The translation layer that AI agents will use is the ontology, not the data warehouse. Warehouses store the data. Ontologies define what the data means. CORA exists to make sure the meaning layer is public, neutrally governed, and faithful to the standards bodies that own each definition.

## What CORA produces

CORA delivers four classes of artifact:

1. **A version-controlled, multi-format mirror.** Each hosted standard lives at `/standards/<name>/<version>/` with its native specification and (where the derivation has been built) machine-derived formats: OWL/RDF ontology, JSON-LD context, JSON Schema. Every release is tagged. Every change is in `git log`.

2. **Cross-standard crosswalks.** Where two hosted standards describe the same concept, CORA publishes a field-level mapping with an explicit confidence label and a written narrative for any divergence. Crosswalks are versioned alongside the standards they connect. Thirty-three concept crosswalks ship today, organized by [taxonomy](crosswalks/taxonomy.md) into seven editorial buckets.

3. **AI skills and agent definitions.** For each hosted standard and each crosswalk, CORA ships agent-ready resources: `SKILL.md` files, MCP server definitions, tool schemas, prompt libraries, and evaluation suites that test whether an agent applies the standard correctly. Skills land alongside use-case demand; the [`skills/`](skills/) directory describes the shape and is currently empty.

4. **A public drift register.** When a hosted standard changes meaning between versions, or when two hosted standards diverge in their definition of the same concept, the divergence is logged, classified, and published. The taxonomy lives in [`drift/`](drift/) today; per-crosswalk `notes` blocks already document inter-standard `divergent` mappings (see, e.g., `rent_amount`, `market_rent`). Consolidation into a standalone register lands when a hosted standard version-bumps or a fourth standard onboards.

## What CORA is not

- **Not a new standard.** CORA does not invent its own ontology of real assets. It hosts, translates, and connects the ones that exist.
- **Not a competitor to OSCRE, RETTC, REDI, NCREIF, INREV, ANREV, CREFC, MISMO, IBPDI, GRESB, RICS, or any other standards body.** Each retains full authority over its own standard. CORA's role is custodianship of the published artifact and the connective layer above it, not authority over the underlying definitions.
- **Not a Cherre product.** Cherre is the bootstrap custodian. Code and content are Apache 2.0 and CC BY 4.0. There is no Cherre-only edition.
- **Not yet a foundation-governed project.** It will be. See [Governance](#governance).

## Scope

CORA's lane is **real assets data across the investment, operational, and reporting lifecycle**. That includes:

- **Real estate, equity.** Direct property, multifamily, commercial, mixed-use, and specialty sectors. Funds, portfolios, ownership hierarchies, leases, operational data, valuations, transactions.
- **Real estate, debt.** Mortgages, CMBS, mezzanine and preferred equity, construction lending, securitization structures.
- **Infrastructure.** Data centers, renewable energy assets, transport infrastructure, with defined extension points for additional sectors.

CORA does not aim to subsume:

- **Smart-building and IoT modeling.** That is [RealEstateCore](https://github.com/RealEstateCore/rec)'s domain and the emerging [C4SB Foundation](https://www.linuxfoundation.org/press/intent-to-form-c4sb-foundation) at the Linux Foundation. RealEstateCore describes how a building's systems describe themselves; CORA describes how that building shows up in a fund's books. The two are complementary, and where mappings exist CORA publishes them.
- **General semantic interchange across the BI and AI ecosystem.** That is [Open Semantic Interchange](https://open-semantic-interchange.org/)'s domain. OSI is cross-industry; CORA is real-assets-specific and conforms to OSI conventions where they apply.

Where CORA's scope touches one of these, the relationship is documented and the mapping is published. Where it does not, CORA stays out of it.

## Standards we are working with

CORA hosts three standards today: IBPDI (mirror under upstream open licenses), MITS (participating, under permission from RETTC), and REDI (participating, under permission from the REDI Data Model Sub-Committee). Everything else listed below is a future invitation, not an announcement. Each row reflects the actual state of the conversation, not an aspiration.

| Standard | Owner | CORA status |
|---|---|---|
| [IBPDI CDM](https://github.com/ibpdi/cdm) | International Building Performance & Data Initiative | **Hosted (open-license mirror).** CC BY 4.0 + MIT licensing; no upstream permission required. Seven cluster inventories committed. |
| [MITS](https://rettc.org/mits-data-models) | RETTC | **Hosted (participating).** Mirrored under permission from RETTC. Seven module inventories committed; four enriched from Excel data dictionaries via `Inventory.enrich` (see [ADR-0001](docs/adr/0001-enrich-vs-merge.md)). |
| [REDI](https://realestatedatainitiative.netlify.app/) Data Model | Real Estate Data Initiative (LP-led) | **Hosted (participating).** Mirrored under permission from the REDI Data Model Sub-Committee. One inventory committed from the REDI Data Fields workbook. Native cross-mappings to NCREIF/PREA Reporting Standards and INREV preserved for future crosswalks. |
| [OSCRE IDM](https://www.oscre.org/Industry-Data-Model) and Smart Data Highway | OSCRE | **Future invitation.** OSCRE's Smart Data Highway initiative is its own program. If OSCRE decides hosting infrastructure outside its own perimeter is useful, CORA can offer it. |
| [NCREIF / PREA Reporting Standards](https://reportingstandards.info/), [INREV](https://www.inrev.org/standards), ANREV | NCREIF, INREV, ANREV, PREA | **Future invitation.** |
| [CREFC IRP](https://www.crefc.org/irp) | CRE Finance Council | **Future invitation.** |
| [MSCI Real Estate Investment Standards](https://www.msci.com/our-clients/real-assets) | MSCI | **Future invitation.** |
| [MISMO Reference Model](https://www.mismo.org/standards-resources) | MISMO | **Future invitation.** Crosswalks at the real-estate-finance boundary are in scope; the residential mortgage operational layer remains MISMO's. |
| GRESB, RICS | GRESB, RICS | **Future invitation.** |

"Future invitation" means CORA's offer is on the record for any standards body that wants to use the infrastructure. It does not mean CORA controls, hosts, or speaks for the standard, and it is not a public commitment by any of these bodies.

### What ships today

| Artifact | Count | Where |
|---|---|---|
| Hosted standards | 3 (IBPDI, MITS, REDI) | [`standards/`](standards/) |
| Field inventories | 15 modules · 496 types · 3,353 fields | [`standards/<std>/current/inventory/`](standards/) |
| Concept crosswalks | 33 across 7 editorial buckets | [`crosswalks/concepts/`](crosswalks/concepts/) |
| Extractor adapters | 5 (XSD, JSON catalog, CDM-JSON, Excel single-sheet, Excel multi-sheet) | [`tools/extractors/`](tools/extractors/) |
| Validator adapters | 3 (inventory-schema, field-count, crosswalk-paths) | `cora validate` |
| Generator adapters | 5 (inventory pages, concept pages, coverage matrix, README, concept overview) | `cora docs build` |
| Concept analyzer | string-match + semantic-embedding clustering + scaffold | `cora concepts ...` |
| ADRs | 2 | [`docs/adr/`](docs/adr/) |

Track upcoming work through the [merged pull-request history](https://github.com/coradata/cora/pulls?q=is%3Apr+is%3Amerged) and the [CHANGELOG](CHANGELOG.md).

## How custodianship works

### Versioning

Each hosted standard follows its owner's release cadence. CORA publishes a release as soon as the owner does, tagged with the owner's version identifier and a CORA build hash. CORA does not fork. If a standard's owner is silent, the standard sits at its last published version.

### Multi-format publication

Each release ships in:

- **Native format.** The owner's authoritative artifact (XML schema, PDF specification, Excel template), bit-identical to the upstream release.
- **Field inventory.** A normalized YAML view of one module of one standard, format-agnostic. Every crosswalk references inventory paths. See [`docs/field-inventory.md`](docs/field-inventory.md) for the schema and path grammar.
- **Ontology, JSON-LD context, JSON Schema** (future). An OWL/RDF rendering derived from the native format via the same extractor toolchain. The inventory schema is designed as a clean projection — see the OWL/RDF projection roadmap in `docs/field-inventory.md`.

The native format is canonical. Major changes always flow from native through derivation. Derived-format-only bugs (a typo in the generated JSON-LD that does not exist in the source XML) are fixed via patch releases and do not require a new upstream version.

Every committed inventory passes structural validation, field-count thresholds, and crosswalk-path resolution in CI before publication. The derivation tooling lives in [`tools/`](tools/) and is open source under this repository, so anyone can reproduce a build from native to derived and verify the result.

### Crosswalks

Where two hosted standards describe the same concept (city, postal code, organisation id, unit id, lease end date, rent amount, square footage, others), CORA publishes a crosswalk file. Each crosswalk records:

- The canonical concept name and a working definition
- Field-level mappings from each hosted standard, with version and source location
- A confidence label per mapping: `exact`, `close`, `partial`, `divergent`, or `not_present`
- A written narrative for any `divergent` or `not_present` mapping that explains the difference

The full decision tree for confidence labels — with worked examples drawn from the current corpus — lives in [`crosswalks/taxonomy.md`](crosswalks/taxonomy.md). Crosswalks are maintained alongside the standards they connect. When an upstream standard changes, affected crosswalks are reviewed in the same release cycle.

### AI skills and agent definitions

For each hosted standard and each crosswalk, CORA will ship:

- `SKILL.md` files that prepackage the context an LLM needs to reason over the standard
- MCP server definitions for queryable programmatic access
- Tool schemas in OpenAI function-calling and Anthropic tool-use formats
- Prompt libraries for common workflows (validate this record, map this field, explain this container)
- Evaluation suites that test whether an agent applies the standard correctly

Skills land alongside use-case demand. Evaluation suites are part of CI: a failing evaluation blocks merge. AI quality is enforced through tests, not through review alone. The directory shape lives in [`skills/`](skills/) and is currently empty.

### Drift register

The drift register tracks two kinds of divergence:

- **Intra-standard drift.** A field or relationship that changed meaning between two versions of the same standard.
- **Inter-standard drift.** Two hosted standards that name the same concept differently or define it incompatibly.

Each entry records the standards and versions involved, the precise location of the divergence, and a classification:

| Category | Description | Example |
|---|---|---|
| `rename` | Same concept, different name | A field called `Property` in one version becomes `Asset` in the next, with no other change |
| `scope_change` | Definition's scope expanded or narrowed | An `Owner` field redefined to include beneficial owners that were previously excluded |
| `type_change` | Underlying data type changed | An enumeration replaced with free text, or a numeric field made currency-aware |
| `cardinality_change` | Relationship changed from one-to-one to one-to-many or vice versa | `Address` extended from a single value per property to a list |
| `enumeration_change` | Allowed values added, removed, or redefined | The list of permitted property types extended to include `data_center` |
| `semantic_redefinition` | Definition reworded such that meaning shifts even where structure does not | Net Operating Income's treatment of recurring capex changed |

Resolution of any drift entry is the standards bodies' decision, not CORA's.

Inter-standard divergences are partially documented today inside the per-crosswalk `notes` blocks under [`crosswalks/concepts/`](crosswalks/concepts/) (see the `divergent` mappings on `rent_amount` and `market_rent` for worked examples). The consolidated drift register at [`drift/`](drift/) populates as cross-version comparisons are authored or as a fourth standard onboards; the taxonomy above is the contract for what it will contain.

### Conflict resolution

CORA does not arbitrate disagreements between standards bodies about what a concept should mean. When two hosted standards disagree, both definitions are published, the disagreement is logged in the drift register, and CORA stays neutral. If the affected bodies negotiate a reconciliation, CORA publishes the result.

## Repository layout

```
/standards/
  /ibpdi/
    /current/
      native/
      inventory/        # 7 cluster inventories
      PROVENANCE.yaml
      CHANGELOG.md
  /mits/                # participating, mirrored under permission from RETTC; 7 module inventories
  /redi/                # participating, mirrored under permission from the REDI Data Model Sub-Committee; 1 inventory
  /_template/           # PROVENANCE template for onboarding additional standards
/crosswalks/
  /concepts/            # 33 per-concept crosswalk files
  /schema/              # JSON Schema for crosswalk YAML
  README.md
  taxonomy.md
/skills/                # AI skills and agent definitions (shape documented, currently empty)
/drift/                 # Drift register (taxonomy documented, register populates as cross-version comparisons land)
/governance/
  CLA.md
  SECURITY.md
/tools/
  /extractors/          # cora-extractors Python package; `cora` CLI
/docs/
  /adr/                 # Architecture decision records
  /generated/           # Auto-regenerated browse view (Markdown + Mermaid)
  /concepts-analysis/   # Concept-analyzer output (field census + cluster suggestions)
  /site/                # MkDocs Material authored docs site (deployed)
  field-inventory.md
  onboarding-a-standard.md
LICENSE
LICENSE-Docs
NOTICE
CITATION.cff
CHANGELOG.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
CONTEXT.md
README.md
```

## License

- **Code in this repository:** Apache License 2.0
- **Specifications, documentation, crosswalks, skills, and drift register:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Mirrored upstream content:** subject to upstream license. CORA carries license badges and attribution per directory; each standard's terms are documented in `standards/<std>/PROVENANCE.yaml`.

Apache 2.0 is permissive and includes an explicit patent grant. Both properties are load-bearing for a project that republishes definitions owned by other bodies: contributors and consumers need patent protection on the derivations they ship and depend on. These are the same license terms used by Open Semantic Interchange and other contemporary open-specification efforts.

## Contributing

Contributions to CORA are accepted under a Contributor License Agreement based on the Apache 2.0 Individual CLA. The CLA grants CORA a license to redistribute the contribution under Apache 2.0 and confirms that the contributor has the right to make the contribution. It does not assign copyright. See [`governance/CLA.md`](governance/CLA.md) for the current text and signing workflow.

Material changes to a hosted standard's content are not contributed through CORA. They are contributed to the standard's owner through that owner's process. CORA accepts:

- Bug reports on the derived ontology, JSON-LD context, JSON Schema, or skills
- New crosswalk entries and corrections to existing ones (see [Requesting a crosswalk](docs/site/docs/requesting-a-crosswalk.md) and [Authoring a crosswalk](docs/site/docs/authoring-a-crosswalk.md))
- Tooling improvements (extractors, validators, generators, drift detection, the concepts analyzer)
- Drift register entries
- Documentation

The contributor walkthrough lives at [`CONTRIBUTING.md`](CONTRIBUTING.md). Breaking changes to derived formats are handled through a public RFC process.

## Governance

Cherre is the **bootstrap custodian** of CORA. The role is time-bounded by design.

In the bootstrap phase, Cherre staffs the repository, runs the publishing pipeline, and underwrites the operational cost of hosting. Cherre does not hold authority over what any hosted standard says or how it evolves.

CORA's stated intent is to transition to **neutral foundation governance** once the project has more than one hosted standard and at least one standards body has joined as a participating member. The target form is a foundation-style structure modeled on Open Semantic Interchange's stated transition path and on the Linux Foundation's project model. The destination foundation has not been selected.

### Staffing and operational commitment

During the bootstrap phase, Cherre commits dedicated engineering capacity to maintain the publishing pipeline, run the drift register, ship and update skills, and respond to upstream releases from hosted standards. Specific SLAs (response time on upstream releases, drift register update cadence, security disclosure handling) will be published in `governance/SLA.md` as the publishing cadence is established.

### Sunset and review clause

If by 18 months after the first tagged release CORA has not (a) onboarded a participating standards body beyond the bootstrap content or (b) attracted at least one non-Cherre maintainer, the bootstrap custodianship will be formally reviewed. The outcome (continue, transfer to a foundation immediately, or sunset) will be decided publicly. This is to prevent CORA from becoming an abandoned vendor-hosted repository that other projects work around.

### Governance documents

| Document | Status |
|---|---|
| [`LICENSE`](LICENSE) (Apache 2.0) | Shipped |
| [`LICENSE-Docs`](LICENSE-Docs) (CC BY 4.0) | Shipped |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) (Contributor Covenant) | Shipped |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Shipped |
| [`governance/CLA.md`](governance/CLA.md) | Shipped |
| [`governance/SECURITY.md`](governance/SECURITY.md) | Shipped |
| `governance/CHARTER.md` | Planned |
| `governance/GOVERNANCE.md` | Planned |
| `governance/SLA.md` | Planned |

## Cherre's role and commercial position

Cherre is a real estate data platform. Cherre builds commercial products that consume and operate on real assets data. CORA puts the *definitional* layer in public. Cherre's commercial products depend on implementation, integration, and operational reliability against that layer, not on private ownership of the definitions themselves.

This is a deliberate bet: that open, well-governed schemas are better for the industry than vendor-owned ones, and that Cherre wins more business by being the best implementation against a shared substrate than by being the only vendor that owns it.

CORA artifacts are Apache 2.0 and CC BY 4.0 and free for any use, including by Cherre's competitors. Cherre's commercial products remain commercial.

## Citing CORA

The machine-readable citation file is at [`CITATION.cff`](CITATION.cff). The short-form citation pattern:

```
Common Ontology for Real Assets (CORA), version <X.Y.Z>, <release date>. github.com/coradata/cora.
```

When citing a specific hosted standard via CORA, cite both the upstream owner and CORA. For example, citing MITS as hosted through CORA would be:

```
MITS v<X> (RETTC, <year>); hosted via Common Ontology for Real Assets (CORA), <CORA version>, <date>.
```

This pattern keeps attribution clear: the standards body owns the definition; CORA owns the published form.

## Contact

Engagement is by role-level alias. Individual contacts are deliberately not published.

- **Custodianship and partnership inquiries:** `custodianship@coradata.org`
- **Technical and contribution questions:** `technical@coradata.org`
- **Press and public statements:** `press@coradata.org`
- **Security disclosures:** `security@coradata.org` (see [`governance/SECURITY.md`](governance/SECURITY.md))

## References

- CORA public project home: [coradata.org](https://coradata.org)
- Open Semantic Interchange: [open-semantic-interchange.org](https://open-semantic-interchange.org/) · [github.com/open-semantic-interchange/OSI](https://github.com/open-semantic-interchange/OSI)
- RealEstateCore: [realestatecore.io](https://www.realestatecore.io/) · [github.com/RealEstateCore/rec](https://github.com/RealEstateCore/rec)
- Linux Foundation C4SB: [intent to form C4SB Foundation](https://www.linuxfoundation.org/press/intent-to-form-c4sb-foundation)
- IBPDI Common Data Model: [github.com/ibpdi/cdm](https://github.com/ibpdi/cdm)
- MITS / RETTC: [rettc.org/mits-data-models](https://rettc.org/mits-data-models)
- OSCRE Industry Data Model: [oscre.org/Industry-Data-Model](https://www.oscre.org/Industry-Data-Model)
- REDI: [realestatedatainitiative.netlify.app](https://realestatedatainitiative.netlify.app/)
- NCREIF / PREA Reporting Standards: [reportingstandards.info](https://reportingstandards.info/)
- INREV: [inrev.org/standards](https://www.inrev.org/standards)
- CREFC IRP: [crefc.org/irp](https://www.crefc.org/irp)
- MISMO: [mismo.org/standards-resources](https://www.mismo.org/standards-resources)
