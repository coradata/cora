# AI Skills and Agent Definitions

For each hosted standard and each crosswalk, CORA ships agent-ready resources:

- `SKILL.md` — prepackaged context an LLM needs to reason over the standard
- Tool schemas in OpenAI function-calling and Anthropic tool-use formats
- Evaluation suites

This directory is currently empty. The first skill (covering IBPDI) lands when there's a concrete use case for it. MCP server definitions, prompt libraries, and per-crosswalk skills follow.

Layout when populated:

```
/skills/
  /<standard>/
    SKILL.md
    field-lookup.md
    evals/
```
