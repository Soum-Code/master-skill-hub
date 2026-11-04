# dynamic-workflow-mode

> Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and other adaptive agent harnesses. Use when building a task-local harness, adding eval gates, or extracting a reusable skill from ad-hoc work.

| | |
|---|---|
| **ID** | `affaan-m/ECC:dynamic-workflow-mode` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business, AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 167 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building a task-local harness, adding eval gates, or extracting a reusable skill from ad-hoc work.

## What it says up front

> Use this skill when a coding agent can generate or adapt a task-local harness instead of only following a static command flow. The goal is to turn dynamic workflow mode into a disciplined system: temporary harnesses for one-off work, shared skill extraction for repeated work, and observable control

## How it is structured

The skill's own section headings, in order:

- When To Activate
- Core Contract
  - Preserve Input Boundaries
- Dynamic Harness Decision Tree
- Task-Local Harness Template
- Shared Skill Extraction
- Control Pane Checkpoints
- Eval Gates
- Anti-Patterns
- Output Standard

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [affaan-m/ECC:unified-memory](affaan-m-ecc-unified-memory.md) - Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other age
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h

## Invoke / install

- Invoke: `/affaan-m/ECC:dynamic-workflow-mode`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/dynamic-workflow-mode --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3d50b87e1e04bdd09cc2c8256b007996daf7352e1c05d26687ce6225aa3d55da --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
