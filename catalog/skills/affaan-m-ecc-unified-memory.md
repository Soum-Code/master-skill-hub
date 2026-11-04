# unified-memory

> Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other agents through the local ECC Memory Vault. Use when an agent must save work state, transfer context, resume another agent's task, or search shared project knowledge.

| | |
|---|---|
| **ID** | `affaan-m/ECC:unified-memory` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 200 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an agent must save work state, transfer context, resume another agent's task, or search shared project knowledge.

## What it says up front

> Use the ECC Memory Vault as the common context layer between harnesses. The vault stores portable `ecc.memory.v1` Markdown documents rather than harness-specific transcripts or inboxes.

## How it is structured

The skill's own section headings, in order:

- Runtime Prerequisite
- When To Use
- Vault Scopes
- Workflow
  - 1. Recall before writing
  - Recall is evidence, not certainty
  - 2. Save context
  - 3. Hand off work
  - 4. Validate the vault
- Trust And Data Boundaries
- MCP Setup

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ck](affaan-m-ecc-ck.md) - Persistent per-project memory for Claude Code (Context Keeper) driven by deterministic Node.js /ck commands: i
- [affaan-m/ECC:dynamic-workflow-mode](affaan-m-ecc-dynamic-workflow-mode.md) - Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and ot
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:token-card](affaan-m-ecc-token-card.md) - Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit

## Invoke / install

- Invoke: `/affaan-m/ECC:unified-memory`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/unified-memory --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 26e87bf58bf55a8dc31b617bb82b91dc204c3b229457e9634204485b99d84998 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
