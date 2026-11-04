# research-ops

> Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current public evidence and any supplied local context.

| | |
|---|---|
| **ID** | `affaan-m/ECC:research-ops` |
| **Pack** | Product Management (also: Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 114 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current public evidence and any supplied local context.

## What it says up front

> Use this when the user asks to research something current, compare options, enrich people or companies, or turn repeated lookups into a monitored workflow.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
- Workflow
  - 1. Start from what the user already gave you
  - 2. Classify the ask
  - 3. Take the lightest useful evidence path first
  - 4. Report with explicit evidence boundaries
  - 5. Decide whether the task should stay manual
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:finance-billing-ops](affaan-m-ecc-finance-billing-ops.md) - Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use
- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 

## Invoke / install

- Invoke: `/affaan-m/ECC:research-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/research-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 970fd836bfa6fcd21692f594674020434f08a72271308c229fdd99705e122a5d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
