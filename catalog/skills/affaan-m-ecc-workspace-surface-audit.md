# workspace-surface-audit

> Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents, and operator workflows. Use when the user wants help setting up Claude Code or understanding what capabilities are actually available in their environment.

| | |
|---|---|
| **ID** | `affaan-m/ECC:workspace-surface-audit` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 127 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants help setting up Claude Code or understanding what capabilities are actually available in their environment.

## What it says up front

> Read-only audit skill for answering the question "what can this workspace and machine actually do right now, and what should we add or enable next?"

## How it is structured

The skill's own section headings, in order:

- When to Use
- Non-Negotiable Rules
- Audit Inputs
- Audit Process
  - Phase 1: Inventory What Exists
  - Phase 2: Benchmark Against Official and Installed Surfaces
  - Phase 3: Turn Gaps Into ECC Decisions
- Output Format
- Recommendation Rules
- Good Outcomes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [affaan-m/ECC:deepseek-harness-setup](affaan-m-ecc-deepseek-harness-setup.md) - Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/ski
- [affaan-m/ECC:config-gc](affaan-m-ecc-config-gc.md) - Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, pe
- [affaan-m/ECC:automation-audit-ops](affaan-m-ecc-automation-audit-ops.md) - Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which 

## Invoke / install

- Invoke: `/affaan-m/ECC:workspace-surface-audit`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/workspace-surface-audit --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 755160cf85425347599c40364bae95aaf541fe829f2e48bf0103636e4dfb0414 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
