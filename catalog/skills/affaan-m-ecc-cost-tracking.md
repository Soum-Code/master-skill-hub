# cost-tracking

> Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. Use when the user asks about costs, spending, usage, tokens, budgets, or cost breakdowns by model, session, or date.

| | |
|---|---|
| **ID** | `affaan-m/ECC:cost-tracking` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 108 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user asks about costs, spending, usage, tokens, budgets, or cost breakdowns by model, session, or date.

## What it says up front

> Use this skill to analyze Claude Code cost and usage history from the metrics log that ECC's `stop:cost-tracker` hook writes.

## How it is structured

The skill's own section headings, in order:

- Where the data lives
- When to Use
- How It Works
- Example — summary, by model, last 7 days
- Reporting Guidance
- Anti-Patterns
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:token-card](affaan-m-ecc-token-card.md) - Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit
- [anthropics/claude-plugins-official:session-report](anthropics-claude-plugins-official-session-report.md) - Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive p
- [anthropic-skills:explain-usage](anthropic-skills-explain-usage.md) - Explain where this session's tokens went, with one simple chart in plain language. Use when the user says thin
- [affaan-m/ECC:cost-aware-llm-pipeline](affaan-m-ecc-cost-aware-llm-pipeline.md) - Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic,

## Invoke / install

- Invoke: `/affaan-m/ECC:cost-tracking`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/cost-tracking --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8aaa37b71506bb180fe124485c520b578229ffe0937b804d0be7a2aebd35a118 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
