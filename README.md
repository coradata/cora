# CORA

**Common Ontology for Real Assets**

CORA is a public, vendor-neutral home for the data standards that describe real assets — real estate (equity and debt) and infrastructure — as a coherent, machine-interpretable corpus. We host each standard in its native format, republish it in derived ontology and interchange formats, ship AI skills and agent definitions built on those standards, and maintain a public register of how definitions drift between versions and between standards.

This repository is the canonical source for everything CORA publishes. The public-facing project home is [coradata.org](https://coradata.org).

> **Status: bootstrap.** The repository is being initialized. License is Apache 2.0 + CC BY 4.0 (pending Legal review). The first content drop is a mirror of [IBPDI](https://github.com/ibpdi/cdm)'s Common Data Model under its existing CC BY 4.0 + MIT terms, which requires no upstream permission. [MITS](https://rettc.org/mits-data-models) has been onboarded as CORA's first participating standard under permission from RETTC; see [`standards/mits/`](standards/mits/).

---

## Why CORA exists

Real assets run on a stack of data standards built in different decades, by different bodies, for different audiences. MITS is built for multifamily operations. OSCRE's Industry Data Model is built for commercial transactional data. REDI is built for LP investment reporting. NCREIF, INREV, ANREV, and PREA cover regional reporting alignment. CREFC covers debt. MISMO covers residential mortgage. IBPDI covers global building performance and ESG. Each is correct in its own scope. None speaks the same dialect as the others.

That was a tolerable cost when humans were the integrators. It is not a tolerable cost in a world where AI agents are expected to reason across an entire portfolio, fund, or allocator exposure without escalating to a person to translate the schema.

The translation layer that AI agents will use is the ontology, not the data warehouse. Warehouses store the data. Ontologies define what the data means. CORA exists to make sure the meaning layer is public, neutrally governed, and faithful to the standards bodies that own each definition.

## What CORA produces

CORA delivers four classes of artifact:

1. **A version-controlled, multi-format mirror.** Each hosted standard lives at `/standards/<name>/<version>/` with its native specification and machine-derived formats: OWL/RDF ontology, JSON-LD context, JSON Schema. Every release is tagged. Every change is in `git log`.

2. **Cross-standard crosswalks.** Where two hosted standards describe the same concept, CORA publishes a field-level mapping with confidence scoring and a written narrative for any divergence. Crosswalks are versioned alongside the standards they connect.

3. **AI skills and agent definitions.** For each hosted standard and each crosswalk, CORA ships agent-ready resources: `SKILL.md` files, MCP server definitions, tool schemas, prompt libraries, and evaluation suites that test whether an agent applies the standard correctly.

4. **A public drift register.** When a hosted standard changes meaning between versions, or when two hosted standards diverge in their definition of the same concept, the divergence is logged, classified, and published. The drift register is a published artifact, not an internal tool.

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

CORA goes live with two hosted standards: IBPDI (bootstrap mirror under upstream open licenses) and MITS (participating, under permission from RETTC). Everything else listed below is a future invitation, not an announcement. Each row reflects the actual state of the conversation, not an aspiration.

| Standard | Owner | CORA status |
|---|---|---|
| [IBPDI CDM](https://github.com/ibpdi/cdm) | International Building Performance & Data Initiative | **Bootstrap mirror.** CC BY 4.0 + MIT licensing; no upstream permission required. CORA mirrors the CDM as published. |
| [MITS](https://rettc.org/mits-data-models) | RETTC | **Participating.** Mirrored under permission from RETTC. Native XSD/XML schemas and supporting docs hosted as published; derived OWL/RDF, JSON-LD, and JSON Schema to follow once the derivation pipeline is operational. |
| [REDI](https://realestatedatainitiative.netlify.app/) Data Model | Real Estate Data Initiative (LP-led) | **Future invitation.** REDI has a committee-approved model with INREV and NCREIF mappings, owned and operated by REDI's committee. If REDI chooses, CORA can host derived formats, crosswalks, and a drift register. The decision belongs to REDI. |
| [OSCRE IDM](https://www.oscre.org/Industry-Data-Model) and Smart Data Highway | OSCRE | **Future invitation.** OSCRE's Smart Data Highway initiative is its own program. If OSCRE decides hosting infrastructure outside its own perimeter is useful, CORA can offer it. |
| [NCREIF / PREA Reporting Standards](https://reportingstandards.info/), [INREV](https://www.inrev.org/standards), ANREV | NCREIF, INREV, ANREV, PREA | **Future invitation.** |
| [CREFC IRP](https://www.crefc.org/irp) | CRE Finance Council | **Future invitation.** |
| [MSCI Real Estate Investment Standards](https://www.msci.com/our-clients/real-assets) | MSCI | **Future invitation.** |
| [MISMO Reference Model](https://www.mismo.org/standards-resources) | MISMO | **Future invitation.** Crosswalks at the real-estate-finance boundary are in scope; the residential mortgage operational layer remains MISMO's. |
| GRESB, RICS | GRESB, RICS | **Future invitation.** |

"Future invitation" means CORA's offer is on the record for any standards body that wants to use the infrastructure. It does not mean CORA controls, hosts, or speaks for the standard, and it is not a public commitment by any of these bodies.

### Current release status

No CORA releases have shipped yet. The repository is being initialized. The IBPDI bootstrap mirror and the MITS participating mirror are both in `main`. The first tagged release will bundle them. Watch the [GitHub Releases](../../releases) page for updates.

## How custodianship works

### Versioning

Each hosted standard follows its owner's release cadence. CORA publishes a release as soon as the owner does, tagged with the owner's version identifier and a CORA build hash. CORA does not fork. If a standard's owner is silent, the standard sits at its last published version.

### Multi-format publication

Each release ships in:

- **Native format.** The owner's authoritative artifact (XML schema, PDF specification, Excel template), bit-identical to the upstream release.
- **Ontology.** An OWL/RDF rendering derived from the native format, with a published mapping file showing every derived element.
- **JSON-LD context** and **JSON Schema**, generated from the ontology.

The native format is canonical. Major changes always flow from native through derivation. Derived-format-only bugs (a typo in the generated JSON-LD that does not exist in the source XML) are fixed via patch releases and do not require a new upstream version.

Every release ships with a validation report comparing the derived formats to the native specification. The derivation tooling lives in `/tools/` and is open source under this repository, so anyone can reproduce a build from native to derived and verify the result.

### Crosswalks

Where two hosted standards describe the same concept (Property, Address, Owner, NOI, Cap Rate, Occupancy, Loan, Parcel ID, others), CORA publishes a crosswalk file. Each crosswalk records:

- The canonical concept name and a working definition
- Field-level mappings from each hosted standard, with version and source location
- A confidence score per mapping: `exact`, `close`, `partial`, or `divergent`
- A written narrative for any `divergent` mapping that explains the difference

Crosswalks are maintained alongside the standards they connect. When an upstream standard changes, affected crosswalks are reviewed in the same release cycle.

### AI skills and agent definitions

For each hosted standard and each crosswalk, CORA ships:

- `SKILL.md` files that prepackage the context an LLM needs to reason over the standard
- MCP server definitions for queryable programmatic access
- Tool schemas in OpenAI function-calling and Anthropic tool-use formats
- Prompt libraries for common workflows (validate this record, map this field, explain this container)
- Evaluation suites that test whether an agent applies the standard correctly

Skills are regenerated whenever the underlying standard or crosswalk changes. Evaluation suites are part of CI: a failing evaluation blocks merge. AI quality is enforced through tests, not through review alone.

### Drift register

The drift register tracks two kinds of divergence:

- **Intra-standard drift.** A field or relationship that changed meaning between two versions of the same standard.
- **Inter-standard drift.** Two hosted standards that name the same concept differently or define it incompatibly.

Each entry records the standards and versions involved, the precise location of the divergence, and a classification. The initial taxonomy is provisional and will be revised after real-world use against MITS:

| Category | Description | Example |
|---|---|---|
| `rename` | Same concept, different name | A field called `Property` in one version becomes `Asset` in the next, with no other change |
| `scope_change` | Definition's scope expanded or narrowed | An `Owner` field redefined to include beneficial owners that were previously excluded |
| `type_change` | Underlying data type changed | An enumeration replaced with free text, or a numeric field made currency-aware |
| `cardinality_change` | Relationship changed from one-to-one to one-to-many or vice versa | `Address` extended from a single value per property to a list |
| `enumeration_change` | Allowed values added, removed, or redefined | The list of permitted property types extended to include `data_center` |
| `semantic_redefinition` | Definition reworded such that meaning shifts even where structure does not | Net Operating Income's treatment of recurring capex changed |

Resolution of any drift entry is the standards bodies' decision, not CORA's.

> The drift register and its tooling ship with the first tagged release covering both IBPDI and MITS. Until then, the register is scaffolded but does not yet exercise inter-standard drift across the two hosted standards.

### Conflict resolution

CORA does not arbitrate disagreements between standards bodies about what a concept should mean. When two hosted standards disagree, both definitions are published, the disagreement is logged in the drift register, and CORA stays neutral. If the affected bodies negotiate a reconciliation, CORA publishes the result.

## Repository layout

> The layout below is the planned shape for the v0.1 release. It is subject to change once the repository is initialized.

```
/standards/
  /ibpdi/
    /current/
      native/
      ontology/
      jsonld/
      jsonschema/
      mapping.yaml
      CHANGELOG.md
  /mits/             (participating, mirrored under permission from RETTC)
  /redi/             (placeholder)
  /oscre/            (placeholder)
  ...
/crosswalks/
  /concepts/         (per-concept crosswalk files)
  taxonomy.md
/skills/
  /<standard>/       (SKILL.md, MCP definitions, tool schemas, evaluations)
  /cross-standard/   (skills that span standards)
/drift/
  register.yaml
  taxonomy.md
/governance/
  CHARTER.md
  GOVERNANCE.md
  SECURITY.md
  SLA.md
  CLA.md
  CODE_OF_CONDUCT.md
/tools/
  /validators/
  /converters/
  /skill-generation/
LICENSE
LICENSE-Docs
NOTICE
CITATION.cff
CONTRIBUTING.md
README.md
```

## License

- **Code in this repository:** Apache License 2.0
- **Specifications, documentation, crosswalks, skills, and drift register:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Mirrored upstream content:** subject to upstream license. CORA carries license badges and attribution per directory.

Apache 2.0 is permissive and includes an explicit patent grant. Both properties are load-bearing for a project that republishes definitions owned by other bodies: contributors and consumers need patent protection on the derivations they ship and depend on. These are the same license terms used by the Open Semantic Interchange and other contemporary open-specification efforts.

**The license is pending review by Cherre Legal.** Until that review is complete, treat the choice as proposed rather than final.

## Contributing

> Contribution mechanics ship with the v0.1 release. The notes below describe the intended flow.

Contributions to CORA are accepted under a Contributor License Agreement based on the Apache 2.0 Individual CLA. The CLA grants CORA a license to redistribute the contribution under Apache 2.0 and confirms that the contributor has the right to make the contribution. It does not assign copyright.

Material changes to a hosted standard's content are not contributed through CORA. They are contributed to the standard's owner through that owner's process. CORA accepts:

- Bug reports on the derived ontology, JSON-LD context, JSON Schema, or skills
- New crosswalk entries and corrections to existing ones
- Tooling improvements (validators, converters, skill generation, drift detection)
- Drift register entries
- Documentation

Breaking changes to derived formats are handled through a public RFC process.

## Governance

Cherre is the **bootstrap custodian** of CORA. The role is time-bounded by design.

In the bootstrap phase, Cherre staffs the repository, runs the publishing pipeline, and underwrites the operational cost of hosting. Cherre does not hold authority over what any hosted standard says or how it evolves.

CORA's stated intent is to transition to **neutral foundation governance** once the project has more than one hosted standard and at least one standards body has joined as a participating member. The target form is a foundation-style structure modeled on Open Semantic Interchange's stated transition path and on the Linux Foundation's project model. The destination foundation has not been selected.

### Staffing and operational commitment

During the bootstrap phase, Cherre commits dedicated engineering capacity to maintain the publishing pipeline, run the drift register, ship and update skills, and respond to upstream releases from hosted standards. Specific SLAs (response time on upstream releases, drift register update cadence, security disclosure handling) will be published in `governance/SLA.md` before the v0.1 release.

### Sunset and review clause

If by 18 months after the first release CORA has not (a) onboarded a participating standards body beyond the bootstrap content or (b) attracted at least one non-Cherre maintainer, the bootstrap custodianship will be formally reviewed. The outcome (continue, transfer to a foundation immediately, or sunset) will be decided publicly. This is to prevent CORA from becoming an abandoned vendor-hosted repository that other projects work around.

### Status of governance documents

| Document | Status |
|---|---|
| `LICENSE` (Apache 2.0) | Drafted, pending Legal sign-off |
| `LICENSE-Docs` (CC BY 4.0) | Drafted, pending Legal sign-off |
| `governance/CHARTER.md` | Planned for v0.1 |
| `governance/GOVERNANCE.md` | Planned for v0.1 |
| `governance/SECURITY.md` | Planned for v0.1 |
| `governance/SLA.md` | Planned for v0.1 |
| `governance/CLA.md` | Planned for v0.1 |
| `CODE_OF_CONDUCT.md` | Planned for v0.1 (likely Contributor Covenant) |
| `CONTRIBUTING.md` | Planned for v0.1 |

This README is the only governance artifact in place at the time of repository initialization. The list above is the honest state of the rest.

## Cherre's role and commercial position

Cherre is a real estate data platform. Cherre builds commercial products that consume and operate on real assets data. CORA puts the *definitional* layer in public. Cherre's commercial products depend on implementation, integration, and operational reliability against that layer, not on private ownership of the definitions themselves.

This is a deliberate bet: that open, well-governed schemas are better for the industry than vendor-owned ones, and that Cherre wins more business by being the best implementation against a shared substrate than by being the only vendor that owns it.

CORA artifacts are Apache 2.0 and CC BY 4.0 and free for any use, including by Cherre's competitors. Cherre's commercial products remain commercial.

## Citing CORA

Once the first CORA release ships, the citation format will be:

```
Common Ontology for Real Assets (CORA), version <X.Y.Z>, <release date>. github.com/coradata/cora.
```

When citing a specific hosted standard via CORA, cite both the upstream owner and CORA. For example, citing MITS as hosted through CORA would be:

```
MITS v<X> (RETTC, <year>); hosted via Common Ontology for Real Assets (CORA), <CORA version>, <date>.
```

This pattern keeps attribution clear: the standards body owns the definition; CORA owns the published form. A formal `CITATION.cff` file ships with the first release.

## Contact

Engagement is by role-level alias. Individual contacts are deliberately not published.

- **Custodianship and partnership inquiries:** `custodianship@coradata.org`
- **Technical and contribution questions:** `technical@coradata.org`
- **Press and public statements:** `press@coradata.org`
- **Security disclosures:** `security@coradata.org` (see `governance/SECURITY.md` when published)

> Email aliases are being provisioned. Until they resolve, please open a GitHub issue or use the contact form at [coradata.org](https://coradata.org).

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
