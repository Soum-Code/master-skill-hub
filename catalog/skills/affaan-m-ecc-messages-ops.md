# messages-ops

> Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replying, or prove which message source was actually checked.

| | |
|---|---|
| **ID** | `affaan-m/ECC:messages-ops` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 106 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replying, or prove which message source was actually checked.

## What it says up front

> Use this when the task is live-message retrieval: iMessage, DMs, recent one-time codes, or thread inspection before a follow-up.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
- Workflow
  - 1. Resolve the exact thread
  - 2. Read before drafting
  - 3. Handle codes as a focused retrieval task
  - 4. Report exact evidence
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use
- [affaan-m/ECC:research-ops](affaan-m-ecc-research-ops.md) - Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri

## Invoke / install

- Invoke: `/affaan-m/ECC:messages-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/messages-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9242999764e5bf92053fb244d7f87f34f3a27cb6b7a9913e878a98fa6d7128bd --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
