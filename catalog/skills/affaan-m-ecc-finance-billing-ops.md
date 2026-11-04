# finance-billing-ops

> Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sales snapshot, pricing comparison, duplicate-charge diagnosis, or code-backed billing reality instead of generic payments advice.

| | |
|---|---|
| **ID** | `affaan-m/ECC:finance-billing-ops` |
| **Pack** | Finance & Accounting |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 129 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants a sales snapshot, pricing comparison, duplicate-charge diagnosis, or code-backed billing reality instead of generic payments advice.

## What it says up front

> Use this when the user wants to understand money, pricing, refunds, team-seat logic, or whether the product actually behaves the way the website and sales copy imply.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
- Workflow
  - 1. Start from the freshest billing evidence
  - 2. Separate customer incidents from product truth
  - 3. Inspect code-backed billing behavior
  - 4. End with a decision and product gap
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:research-ops](affaan-m-ecc-research-ops.md) - Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri
- [affaan-m/ECC:ecc-tools-cost-audit](affaan-m-ecc-ecc-tools-cost-audit.md) - Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota by
- [affaan-m/ECC:messages-ops](affaan-m-ecc-messages-ops.md) - Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa

## Invoke / install

- Invoke: `/affaan-m/ECC:finance-billing-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/finance-billing-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e72305982b84542597b0a759fa631024a879bd4ac1e4924163b355566053087f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
