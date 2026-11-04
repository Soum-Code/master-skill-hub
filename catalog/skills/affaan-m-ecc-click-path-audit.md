# click-path-audit

> Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, produce wrong final state, or leave the UI in an inconsistent state. Use when: systematic debugging found no bugs but users report broken buttons, or after any major refactor touching shared state stores.

| | |
|---|---|
| **ID** | `affaan-m/ECC:click-path-audit` |
| **Pack** | Browser & Web Automation (also: Finance & Accounting, Security & Privacy, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 246 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when: systematic debugging found no bugs but users report broken buttons, or after any major refactor touching shared state stores.

## What it says up front

> Find bugs that static code reading misses: state interaction side effects, race conditions between sequential calls, and handlers that silently undo each other.

## How it is structured

The skill's own section headings, in order:

- The Problem This Solves
- How It Works
- Execution Steps
  - Step 1: Map State Stores
  - Step 2: Audit Each Touchpoint
  - Step 3: Report
- Scope Control
  - Recommended agent split for full app:
- When to Use
- When NOT to Use
- Integration with Other Skills
- Example: The Bug That Inspired This Skill

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:click-path-audit`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/click-path-audit --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 76b4a910853f2fb920825a9ad8455836d65066084dffab4288b2169e8fb1dd3c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
