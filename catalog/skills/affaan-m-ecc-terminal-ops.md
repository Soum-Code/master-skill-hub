# terminal-ops

> Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exact proof of what was executed and verified.

| | |
|---|---|
| **ID** | `affaan-m/ECC:terminal-ops` |
| **Pack** | MLOps / DevOps / Cloud (also: Software Development, Spec-driven Dev Workflow, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 111 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exact proof of what was executed and verified.

## What it says up front

> Use this when the user wants real repo execution: run commands, inspect git state, debug CI or builds, make a narrow fix, and report exactly what changed and what was verified.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
- Workflow
  - 1. Resolve the working surface
  - 2. Read the failing surface first
  - 3. Keep the fix narrow
  - 4. Report exact execution state
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 
- [affaan-m/ECC:messages-ops](affaan-m-ecc-messages-ops.md) - Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent
- [affaan-m/ECC:research-ops](affaan-m-ecc-research-ops.md) - Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri
- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use

## Invoke / install

- Invoke: `/affaan-m/ECC:terminal-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/terminal-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 462b8a0c071bd25781df9e0ecc0a140f7a78008e58e4552ace2bdb4a3a1697d0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
