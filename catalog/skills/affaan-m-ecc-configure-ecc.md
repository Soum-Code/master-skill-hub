# configure-ecc

> Run the conversational ECC setup wizard inside the current harness: inventory the install, collect scope (user/project/local) and hook mode (off/minimal/standard/strict) in Claude Code, use Codex's native plugin lifecycle, or install the project surface under ./.kimi-code, then preview, apply, and verify. Use when installing, updating, reconfiguring, or repairing an ECC installation, changing hook profiles, or moving ECC between install scopes.

| | |
|---|---|
| **ID** | `affaan-m/ECC:configure-ecc` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 207 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when installing, updating, reconfiguring, or repairing an ECC installation, changing hook profiles, or moving ECC between install scopes.

## What it says up front

> Run a conversational wizard inside the current harness. Inventory first, collect only supported choices, preview, confirm once, apply non-interactively, verify, and show the welcome only after success. Never clone ECC into a temporary directory or copy plugin components by hand.

## How it is structured

The skill's own section headings, in order:

- Route by the current harness
- Claude Code: run the full conversational wizard
  - 1. Inventory without changing anything
  - 2. Collect exactly two choices
  - 3. Preview and confirm once
  - 4. Apply the explicit choices
  - 5. Verify, then render the welcome
- Codex: use the native plugin lifecycle
- Kimi: install the project surface

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:deepseek-harness-setup](affaan-m-ecc-deepseek-harness-setup.md) - Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/ski
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 

## Invoke / install

- Invoke: `/affaan-m/ECC:configure-ecc`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/configure-ecc --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree eab667ffdc50d82b919126ae81ce11332dd1223b58d0164eba48d154b084578b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
