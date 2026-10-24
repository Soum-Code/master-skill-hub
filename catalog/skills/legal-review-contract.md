# review-contract

> Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.

| | |
|---|---|
| **ID** | `legal:review-contract` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 359 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing vendor or customer agreements, when you need clause-by-clause analysis against standard positions, or when preparing a negotiation strategy with prioritized redlines and fallback positions.

## What it says up front

> Review a contract against your organization's negotiation playbook. Analyze each clause, flag deviations, generate redline suggestions, and provide business impact analysis.

## How it is structured

The skill's own section headings, in order:

- Invocation
- Workflow
  - Step 1: Accept the Contract
  - Step 2: Gather Context
  - Step 3: Load the Playbook
  - Step 4: Clause-by-Clause Analysis
  - Step 5: Flag Deviations
  - Step 6: Generate Redline Suggestions
  - Step 7: Business Impact Summary
  - Step 8: CLM Routing (If Connected)
- Output Format
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [operations:vendor-review](operations-vendor-review.md) - Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor propos

## Invoke / install

- Invoke: `/legal:review-contract`  (Skill tool: `legal:review-contract`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
