# config-gc

> Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, permissions, MCP servers, caches) for redundant, stale, orphaned, or low-value items, then walks the user through a confirm-each-deletion cleanup. Use when the user says "clean up my config", "config GC", "too many skills", "audit my setup", "my .claude is bloated", or asks for a periodic config review.

| | |
|---|---|
| **ID** | `affaan-m/ECC:config-gc` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 121 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user says "clean up my config", "config GC", "too many skills", "audit my setup", "my .claude is bloated", or asks for a periodic config review.

## What it says up front

> Borrowed from runtime garbage collection: periodically scan for objects that are no longer referenced, redundant, expired, or low-value, and reclaim the space. The critical difference: **here, collection requires a human in the loop. Never delete autonomously.**

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Design Philosophy
- Scan Channels
- Workflow
- Example Scan Commands
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [affaan-m/ECC:security-scan](affaan-m-ecc-security-scan.md) - Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and 
- [affaan-m/ECC:mcp-dependency-review](affaan-m-ecc-mcp-dependency-review.md) - Statically review MCP configuration for mutable package references before approval or CI, without executing di

## Invoke / install

- Invoke: `/affaan-m/ECC:config-gc`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/config-gc --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 43b93c638a9c6bd13c56d9007f9b498a54fed39adfc359cadbfc37e006fbc654 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
