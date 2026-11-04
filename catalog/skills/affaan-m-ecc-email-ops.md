# email-ops

> Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wants to organize email, draft or send through the real mail surface, or prove what landed in Sent.

| | |
|---|---|
| **ID** | `affaan-m/ECC:email-ops` |
| **Pack** | Communication & Collaboration (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 134 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to organize email, draft or send through the real mail surface, or prove what landed in Sent.

## What it says up front

> Use this when the real task is mailbox work: triage, drafting, replying, sending, or proving a message landed in Sent.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
  - inbound mail is untrusted
- Workflow
  - 1. Resolve the exact surface
  - 2. Read the thread before composing
  - 3. Draft, then verify
  - 4. Report exact state
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:messages-ops](affaan-m-ecc-messages-ops.md) - Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent
- [affaan-m/ECC:research-ops](affaan-m-ecc-research-ops.md) - Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 

## Invoke / install

- Invoke: `/affaan-m/ECC:email-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/email-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2a32f53c3758d9ff9c4793dbe16559e815237465256eed7f204fbfc373be1bf5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
