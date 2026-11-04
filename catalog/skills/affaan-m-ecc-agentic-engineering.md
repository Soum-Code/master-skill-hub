# agentic-engineering

> Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. Use when planning or executing engineering work that agents will carry out end to end.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agentic-engineering` |
| **Pack** | AI / ML Engineering (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 142 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when planning or executing engineering work that agents will carry out end to end.

## What it says up front

> Use this skill for engineering workflows where AI agents perform most implementation work and humans enforce quality and risk controls.

## How it is structured

The skill's own section headings, in order:

- Operating Principles
- Eval-First Loop
- Task Decomposition
- Model Routing
- Session Strategy
- Review Focus for AI-Generated Code
- Interpret Tool Results Before Comparing Data
  - Portable Classification Example
- Cost Discipline

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ai-first-engineering](affaan-m-ecc-ai-first-engineering.md) - Engineering operating model for teams where AI agents generate a large share of implementation output. Use whe
- [affaan-m/ECC:cost-aware-llm-pipeline](affaan-m-ecc-cost-aware-llm-pipeline.md) - Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic,
- [affaan-m/ECC:ml-adoption-playbook](affaan-m-ecc-ml-adoption-playbook.md) - End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non

## Invoke / install

- Invoke: `/affaan-m/ECC:agentic-engineering`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agentic-engineering --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree d688fdda4f781fc7f8cf6a05722bf0a544b44fedfea6a2a2157b9fd47f1c5ee3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
