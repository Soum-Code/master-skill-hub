# prompt-caching-strategy

> Optimize LLM prompt caching hit rate to reduce API costs and improve latency. Analyzes prompt structure, identifies cacheable vs non-cacheable content, and recommends restructuring to maximize cache reuse. TRIGGER when: user says "prompt cache", "cache hit rate", "reduce LLM cost", "optimize token usage", "cheaper LLM calls", or asks about prompt caching strategies for OpenAI/Anthropic/other providers. DO NOT TRIGGER when: user just wants to optimize a single prompt's quality (use prompt-optimizer instead), or asks about general caching infrastructure.

| | |
|---|---|
| **ID** | `affaan-m/ECC:prompt-caching-strategy` |
| **Pack** | AI / ML Engineering (also: Product Management) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 188 lines in SKILL.md, 1 file(s) |

## When to use it

- TRIGGER when: user says "prompt cache", "cache hit rate", "reduce LLM cost", "optimize token usage", "cheaper LLM calls", or asks about prompt caching strategies for OpenAI/Anthropic/other providers.
- DO NOT TRIGGER when: user just wants to optimize a single prompt's quality (use prompt-optimizer instead), or asks about general caching infrastructure.

## What it says up front

> Arrange reusable prompt content to improve cache reuse, then measure input cost and latency. Savings depend on model, platform, cache eligibility, writes, retention, reuse and output volume. Runtime cache hits and savings for this skill are **unmeasured**; the examples below validate arithmetic with

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
  - Preserve a stable prefix
  - Preserve user and workspace boundaries
- Provider Requirements and Usage Evidence
- Cost Comparison Calculator
- Examples
- Verification Workflow
- Relationship to Other Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:prompt-optimizer](affaan-m-ecc-prompt-optimizer.md) - Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a
- [claude-api](claude-api.md) - Reference for the Claude API and Anthropic SDKs - model ids, pricing, streaming, tool use, MCP, agents, prompt
- [anthropics/claude-code:claude-opus-4-5-migration](anthropics-claude-code-claude-opus-4-5-migration.md) - Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants 
- [anthropics/skills:academy-guide](anthropics-skills-academy-guide.md) - Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product

## Invoke / install

- Invoke: `/affaan-m/ECC:prompt-caching-strategy`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/prompt-caching-strategy --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 90a15f0c6777c825043c83dc8d1571fad77d282e3ae183620b5c5cfd188bdc49 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
