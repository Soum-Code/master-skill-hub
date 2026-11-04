# customer-billing-ops

> Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools like Stripe. Use when the user needs to help a customer, inspect subscription state, or manage revenue-impacting billing operations.

| | |
|---|---|
| **ID** | `affaan-m/ECC:customer-billing-ops` |
| **Pack** | Operations & Business (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 142 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user needs to help a customer, inspect subscription state, or manage revenue-impacting billing operations.

## What it says up front

> Use this skill for real customer operations, not generic payment API design.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Preferred Tool Surface
- Guardrails
- Workflow
  - 1. Identify the customer cleanly
  - 2. Classify the issue
  - 3. Take the safest reversible action first
  - 4. Check operator-side product gaps
  - 5. Produce the operator handoff
- Output Format
- Examples of Good Recommendations

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:google-workspace-ops](affaan-m-ecc-google-workspace-ops.md) - Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and 
- [affaan-m/ECC:finance-billing-ops](affaan-m-ecc-finance-billing-ops.md) - Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the

## Invoke / install

- Invoke: `/affaan-m/ECC:customer-billing-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/customer-billing-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree dfbd3045f5dd3fb8ea074ed5807428cbae03313f1a7e03db8dd93343ecca881b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
