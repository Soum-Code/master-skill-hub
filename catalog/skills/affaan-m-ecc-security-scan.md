# security-scan

> Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield. Checks CLAUDE.md, settings.json, MCP servers, hooks, and agent definitions. Use when auditing a .claude/ directory — CLAUDE.md, settings.json, MCP servers, hooks, or agent definitions.

| | |
|---|---|
| **ID** | `affaan-m/ECC:security-scan` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 167 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when auditing a .claude/ directory — CLAUDE.md, settings.json, MCP servers, hooks, or agent definitions.

## What it says up front

> Audit your Claude Code configuration for security issues using [AgentShield](https://github.com/affaan-m/agentshield).

## How it is structured

The skill's own section headings, in order:

- When to Activate
- What It Scans
- Prerequisites
- Usage
  - Basic Scan
  - Output Formats
  - Auto-Fix
  - Opus 4.6 Deep Analysis
  - Initialize Secure Config
  - GitHub Action
- Severity Levels
- Interpreting Results
  - Critical Findings (fix immediately)
  - High Findings (fix before production)
  - Medium Findings (recommended)
  - Info Findings (awareness)
- Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [update-config](update-config.md) - Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other auto
- [affaan-m/ECC:config-gc](affaan-m-ecc-config-gc.md) - Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, pe
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:mcp-dependency-review](affaan-m-ecc-mcp-dependency-review.md) - Statically review MCP configuration for mutable package references before approval or CI, without executing di

## Invoke / install

- Invoke: `/affaan-m/ECC:security-scan`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/security-scan --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c60497e781c21eb3c637b753d998fb518e7511dfa883d7f0ac5dab437eb32ecf --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
