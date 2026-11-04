# repo-scan

> Bootstrap pointer that installs the external repo-scan skill from a pinned, reviewable commit. Use when repo-scan must be installed before running its cross-stack source-code asset audit; this ECC pointer does not perform the audit itself.

| | |
|---|---|
| **ID** | `affaan-m/ECC:repo-scan` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 171 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when repo-scan must be installed before running its cross-stack source-code asset audit; this ECC pointer does not perform the audit itself.

## What it says up front

> Installation completes only the bootstrap. Reload your agent harness, then invoke `repo-scan` again. This ECC pointer installs the external skill but does not run a scan itself.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Installation
- Core Capabilities
- Analysis Depth Levels
- How It Works
- Examples
- Best Practices
- Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [skill-hub:skill-vetter](skill-hub-skill-vetter.md) - Security-vet an Agent Skill, plugin folder or a GitHub repo of skills before installing or sharing it. Use whe
- [affaan-m/ECC:orch-refine-code](affaan-m-ecc-orch-refine-code.md) - Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k
- [affaan-m/ECC:context-budget](affaan-m-ecc-context-budget.md) - Routes live context checks to the native Codex or Claude Code meter without scanning files, and performs a bou
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h

## Invoke / install

- Invoke: `/affaan-m/ECC:repo-scan`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/repo-scan --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 16ff5c0ab12b4c3887a898eee4b0f74171cc2ec42a7df4d86e6dc8262be6e2ac --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
