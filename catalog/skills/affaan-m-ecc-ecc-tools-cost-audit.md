# ecc-tools-cost-audit

> Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or GitHub App cost spikes in the ECC Tools repo.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ecc-tools-cost-audit` |
| **Pack** | Finance & Accounting (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 162 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or GitHub App cost spikes in the ECC Tools repo.

## What it says up front

> Use this skill when the user suspects the ECC Tools GitHub App is burning cost, over-creating PRs, bypassing usage limits, or routing free users into premium analysis paths.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When To Use
- Scope Guardrails
- Workflow
  - 1. Freeze repo scope
  - 2. Trace ingress before theorizing
  - 3. Trace the worker and side effects
  - 4. Audit the high-signal burn paths
  - 5. Fix in burn order
  - 6. Verify with the smallest proving steps
- High-Signal Failure Patterns
  - 1. One queue type for all triggers
  - 2. Post-enqueue usage reservation
  - 3. Free tier on premium path
  - 4. App-generated branches re-enter the webhook
  - 5. Expensive work before persistence safety
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:finance-billing-ops](affaan-m-ecc-finance-billing-ops.md) - Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the
- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [affaan-m/ECC:production-audit](affaan-m-ecc-production-audit.md) - Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b

## Invoke / install

- Invoke: `/affaan-m/ECC:ecc-tools-cost-audit`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ecc-tools-cost-audit --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9ec066721144ba1670baa339f9c0a96f60b2f7971fe0648b9e681cb0436e3a10 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
