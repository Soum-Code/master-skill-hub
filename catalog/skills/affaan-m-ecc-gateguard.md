# gateguard

> PreToolUse fact-forcing gate that denies the first Edit/Write/Bash (including MultiEdit and NotebookEdit) attempt until the agent presents concrete facts (importers, data schemas, verbatim user instruction), then allows retry; A/B-tested at +2.25 quality points. Use when enabling or configuring the GateGuard hook, exempting paths via env vars, or handling first-touch denials.

| | |
|---|---|
| **ID** | `affaan-m/ECC:gateguard` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 712 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when enabling or configuring the GateGuard hook, exempting paths via env vars, or handling first-touch denials.

## What it says up front

> A PreToolUse hook that forces Claude to investigate before editing. Instead of self-evaluation ("are you sure?"), it demands concrete facts. The act of investigation creates awareness that self-evaluation never did.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concept
- Evidence
- Gate Types
  - Edit / MultiEdit Gate (first edit per file)
  - Write Gate (first new file creation)
  - Questions fit the change
  - Questions by target class
  - Destructive Bash Gate (every destructive command)
  - Routine Bash Gate (once per session)
- Parallel Batches and Partial Application
- What Counts as Already Done
  - Order of checks
  - Sensitive targets
  - Hard-linked targets
  - Prior-search credit
  - Comment and whitespace-only edits
  - Same-turn sibling creation collapse
  - Canonical path keys
  - In-session counters
  - Compatibility and limits
- Quick Start
  - Option A: Use the ECC hook (zero install)
  - Option B: Full package with config
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:gateguard`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/gateguard --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 097f2ca4ca8391344906537735c3adfb56b8c00289afc0ab328714da3f17b64f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
