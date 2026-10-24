# legal-risk-assessment

> Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

| | |
|---|---|
| **ID** | `legal:legal-risk-assessment` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 266 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

## What it says up front

> You are a legal risk assessment assistant for an in-house legal team. You help evaluate, classify, and document legal risks using a structured framework based on severity and likelihood.

## How it is structured

The skill's own section headings, in order:

- Risk Assessment Framework
  - Severity x Likelihood Matrix
  - Risk Score Calculation
  - Risk Matrix Visualization
- Risk Classification Levels with Recommended Actions
  - GREEN -- Low Risk (Score 1-4)
  - YELLOW -- Medium Risk (Score 5-9)
  - ORANGE -- High Risk (Score 10-15)
  - RED -- Critical Risk (Score 16-25)
- Documentation Standards for Risk Assessments
  - Risk Assessment Memo Format
  - Risk Register Entry
- When to Escalate to Outside Counsel
  - Mandatory Engagement
  - Strongly Recommended Engagement
  - Consider Engagement
  - Selecting Outside Counsel

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [operations:vendor-review](operations-vendor-review.md) - Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor propos
- [operations:risk-assessment](operations-risk-assessment.md) - Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk 
- [legal:triage-nda](legal-triage-nda.md) - Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (

## Invoke / install

- Invoke: `/legal:legal-risk-assessment`  (Skill tool: `legal:legal-risk-assessment`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
