# AI Skills and Agent Definitions

For each hosted standard and each crosswalk, CORA will publish agent-ready resources:

- `SKILL.md` — prepackaged context an LLM needs to reason over the standard
- Tool schemas in OpenAI function-calling and Anthropic tool-use formats
- Evaluation suites

This directory is currently empty. Skills land alongside use-case demand — when a consumer needs an agent-ready packaging of a hosted standard or a crosswalk, the skill is authored here, alongside the schema it covers, and ships under the same version stream.

Layout when populated:

```
/skills/
  /<standard>/
    SKILL.md
    field-lookup.md
    evals/
```
