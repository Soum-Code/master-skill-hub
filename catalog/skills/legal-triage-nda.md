# triage-nda

> Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA arrives from sales or business development, when screening for embedded non-solicits, non-competes, or missing carveouts, or when deciding whether an NDA can be signed under standard delegation.

| | |
|---|---|
| **ID** | `legal:triage-nda` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 263 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a new NDA arrives from sales or business development, when screening for embedded non-solicits, non-competes, or missing carveouts, or when deciding whether an NDA can be signed under standard delegation.

## What it says up front

> Triage the NDA: @$1

## How it is structured

The skill's own section headings, in order:

- Invocation
- Workflow
  - Step 1: Accept the NDA
  - Step 2: Load NDA Playbook
  - Step 3: Quick Screen
  - Step 4: Classify
  - Step 5: Generate Triage Report
  - Step 6: Routing Suggestion
- Common NDA Issues and Standard Positions
  - Issue: Overbroad Definition of Confidential Information
  - Issue: Missing Independent Development Carveout
  - Issue: Non-Solicitation of Employees
  - Issue: Broad Residuals Clause
  - Issue: Perpetual Confidentiality Obligation
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [legal:legal-risk-assessment](legal-legal-risk-assessment.md) - Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when ev

## Invoke / install

- Invoke: `/legal:triage-nda`  (Skill tool: `legal:triage-nda`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
