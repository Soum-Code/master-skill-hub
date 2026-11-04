# cost-aware-llm-pipeline

> Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. Use when LLM spend needs to come down, or when routing tasks across model tiers and budgets.

| | |
|---|---|
| **ID** | `affaan-m/ECC:cost-aware-llm-pipeline` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 189 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when LLM spend needs to come down, or when routing tasks across model tiers and budgets.

## What it says up front

> Patterns for controlling LLM API costs while maintaining quality. Combines model routing, budget tracking, retry logic, and prompt caching into a composable pipeline.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - 1. Model Routing by Task Complexity
  - 2. Immutable Cost Tracking
  - 3. Narrow Retry Logic
  - 4. Prompt Caching
- Composition
- Pricing Reference (2026)
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [claude-api](claude-api.md) - Reference for the Claude API and Anthropic SDKs - model ids, pricing, streaming, tool use, MCP, agents, prompt
- [affaan-m/ECC:cost-tracking](affaan-m-ecc-cost-tracking.md) - Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. U
- [affaan-m/ECC:agentic-engineering](affaan-m-ecc-agentic-engineering.md) - Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. Use wh
- [affaan-m/ECC:prompt-caching-strategy](affaan-m-ecc-prompt-caching-strategy.md) - Optimize LLM prompt caching hit rate to reduce API costs and improve latency. Analyzes prompt structure, ident

## Invoke / install

- Invoke: `/affaan-m/ECC:cost-aware-llm-pipeline`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/cost-aware-llm-pipeline --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 383869a61dec71693dbcbc113d1eb5d9ec20dd092df326c7be6eef43d44c3cde --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
