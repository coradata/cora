# Contributing to CORA

Thank you for considering a contribution to CORA. This project hosts real assets data standards on behalf of the bodies that own them, plus the crosswalks, AI skills, and drift register that connect them.

## What we accept

- **Bug reports** on derived ontology, JSON-LD context, JSON Schema, or skills
- **New crosswalk entries** and corrections to existing ones (see `/crosswalks/`)
- **Tooling improvements** in `/tools/`
- **Drift register entries** in `/drift/`
- **Documentation** improvements

## What we do not accept

- **Changes to a hosted standard's content.** Those go to the standard's owner through their process, not through CORA.
- **A competing ontology of any concept already covered by a hosted standard.** CORA hosts; it does not author.
- **Derivative formats that conflict with the canonical native source.** When the derived JSON-LD and the native XML disagree, the native wins.

## How to contribute

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Ensure CI passes (lint, license check, crosswalk schema validation)
5. Open a pull request with a clear description and reference to any related issue
6. Agree to the CLA terms in `governance/CLA.md`

## Pull request checklist

- [ ] Linked to an issue (for substantive changes)
- [ ] CI passes
- [ ] License header / SPDX identifier on any new code file

## Questions

Open a discussion at [github.com/coradata/cora/discussions](https://github.com/coradata/cora/discussions) or email `technical@coradata.org` once aliases are provisioned.
