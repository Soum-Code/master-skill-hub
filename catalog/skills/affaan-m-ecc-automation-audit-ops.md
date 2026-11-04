# automation-audit-ops

> Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing before fixing anything.

| | |
|---|---|
| **ID** | `affaan-m/ECC:automation-audit-ops` |
| **Pack** | Browser & Web Automation (also: Finance & Accounting, Security & Privacy, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 144 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing before fixing anything.

## What it says up front

> Use this when the user asks what automations are live, which jobs are broken, where overlap exists, or what tooling and connectors are actually doing useful work right now.

## How it is structured

The skill's own section headings, in order:

- Skill Stack
- When to Use
- Guardrails
- Workflow
  - 1. Inventory the real surface
  - 2. Classify each item by live state
  - 3. Trace the proof path
  - 4. End with keep / merge / cut / fix-next
- Output Format
- Pitfalls
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:messages-ops](affaan-m-ecc-messages-ops.md) - Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [affaan-m/ECC:terminal-ops](affaan-m-ecc-terminal-ops.md) - Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI fa
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h

## Invoke / install

- Invoke: `/affaan-m/ECC:automation-audit-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/automation-audit-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b362e6315542341083cf1f1537c1f05b008543e2dcb2a77efe9198e0edd6d813 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
