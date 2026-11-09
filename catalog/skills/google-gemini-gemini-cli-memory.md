# memory

> Expertise in maintaining persistent bot memory, synchronizing with previous sessions via the Task Ledger, and preserving decision logs.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:memory` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 88 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Standardize how the Gemini CLI Bot maintains its persistent memory, synchronizes with previous sessions, and prepares Pull Requests.

## How it is structured

The skill's own section headings, in order:

- Goal
- Memory Structure (`lessons-learned.md`)
- Rituals
  - Phase 0: Context Retrieval & Synchronization (MANDATORY START)
  - Phase 6: Memory Preservation (MANDATORY END)
- Delegation & Sub-agent State

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:resume-work](bm-resume-work.md) - Resume work from previous session with full context restoration
- [bm:thread](bm-thread.md) - Manage persistent context threads for cross-session work
- [affaan-m/ECC:ck](affaan-m-ecc-ck.md) - Persistent per-project memory for Claude Code (Context Keeper) driven by deterministic Node.js /ck commands: i

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:memory`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/gemini-cli-bot/.gemini/skills/memory --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree 5e85adaa580b157c298b47854545ac4fed5b2c11eaacb9ac8242f7c7d5460e75 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
