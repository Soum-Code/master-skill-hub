# mcp-dependency-review

> Statically review MCP configuration for mutable package references before approval or CI, without executing discovered MCP servers. Use when reviewing .mcp.json, Cursor, VS Code, Claude, Windsurf, or other repo-scoped MCP config.

| | |
|---|---|
| **ID** | `affaan-m/ECC:mcp-dependency-review` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Software Development, AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 178 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing .mcp.json, Cursor, VS Code, Claude, Windsurf, or other repo-scoped MCP config.

## What it says up front

> Use this skill to review MCP configuration for package references that can resolve to different code after the configuration itself was approved.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Review Boundary
- Static Classification Rules
- Review Workflow
  - 1. Locate repo-scoped configuration
  - 2. Parse without executing
  - 3. Classify the selector
  - 4. Recommend a reproducible fix
  - 5. Produce a bounded report
- Example
- Anti-Patterns
  - Calling every mutable reference a vulnerability
  - Pinning whatever is latest today
  - Expanding scope silently
  - Treating a clean drift review as complete MCP security
- Related Skills
- Further Reading

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:security-scan](affaan-m-ecc-security-scan.md) - Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and 
- [update-config](update-config.md) - Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other auto
- [affaan-m/ECC:config-gc](affaan-m-ecc-config-gc.md) - Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, pe
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h

## Invoke / install

- Invoke: `/affaan-m/ECC:mcp-dependency-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/mcp-dependency-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e1049b4a46d55ac1cde4ce3b69323d68ee545f1b1d71203b2723355fdb63cce3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
