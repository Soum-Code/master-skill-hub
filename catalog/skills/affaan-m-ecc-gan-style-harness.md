# gan-style-harness

> GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on Anthropic's March 2026 harness design paper. Use when a feature should be built autonomously through generator and evaluator iteration until it clears a quality bar.

| | |
|---|---|
| **ID** | `affaan-m/ECC:gan-style-harness` |
| **Pack** | Spec-driven Dev Workflow (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 280 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a feature should be built autonomously through generator and evaluator iteration until it clears a quality bar.

## What it says up front

> A multi-agent harness that separates **generation** from **evaluation**, creating an adversarial feedback loop that drives quality far beyond what a single agent can achieve.

## How it is structured

The skill's own section headings, in order:

- Core Insight
- When to Use
- When NOT to Use
- Architecture
- The Three Agents
  - 1. Planner Agent
  - 2. Generator Agent
  - 3. Evaluator Agent
- Evaluation Criteria
  - Scoring
- Usage
  - Via Command
  - Via Shell Script
  - Via Claude Code (Manual)
- Evolution Across Model Capabilities
  - Stage 1 — Weaker Models (Sonnet-class)
  - Stage 2 — Capable Models (Opus 4.5-class)
  - Stage 3 — Frontier Models (Opus 4.6-class)
- Configuration
  - Environment Variables
  - Evaluation Modes
- Anti-Patterns
- Results: What to Expect
- References

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:verify-work](bm-verify-work.md) - Validate built features through conversational UAT
- [example-skills:mcp-builder](example-skills-mcp-builder.md) - Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with externa

## Invoke / install

- Invoke: `/affaan-m/ECC:gan-style-harness`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/gan-style-harness --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9f7929512415136cf1970f452510ba17a2d3d147348e3cf923d680e147c62759 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
