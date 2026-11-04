# deepseek-harness-setup

> Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/skills, .agents/skills), the @deepseek-ai/dsh-hooks-claude-code bridge for command hooks, bare-insert patch mounting, generator usage, event-support limits, and update workflow. Use when setting up ECC on DeepSeek Harness, wiring ECC hooks into a DSH profile, or debugging why ECC skills or hooks do not appear in a DSH session.

| | |
|---|---|
| **ID** | `affaan-m/ECC:deepseek-harness-setup` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 90 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up ECC on DeepSeek Harness, wiring ECC hooks into a DSH profile, or debugging why ECC skills or hooks do not appear in a DSH session.

## What it says up front

> Run ECC on the DeepSeek Harness. Full guide: `docs/DEEPSEEK-HARNESS-GUIDE.md`.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Updating
- Limits

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:configure-ecc](affaan-m-ecc-configure-ecc.md) - Run the conversational ECC setup wizard inside the current harness: inventory the install, collect scope (user
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 

## Invoke / install

- Invoke: `/affaan-m/ECC:deepseek-harness-setup`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/deepseek-harness-setup --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e487f572b532bab3399554ae8365b7eb61bb2c100a9567e9058c8f4bbe962616 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
