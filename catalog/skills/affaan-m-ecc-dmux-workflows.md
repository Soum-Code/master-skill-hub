# dmux-workflows

> Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other harnesses. Use when running multiple agent sessions in parallel or coordinating multi-agent development workflows.

| | |
|---|---|
| **ID** | `affaan-m/ECC:dmux-workflows` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 198 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when running multiple agent sessions in parallel or coordinating multi-agent development workflows.

## What it says up front

> Orchestrate parallel AI agent sessions using dmux, a tmux pane manager for agent harnesses.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- What is dmux
- Quick Start
- Workflow Patterns
  - Pattern 1: Research + Implement
  - Pattern 2: Multi-File Feature
  - Pattern 3: Test + Fix Loop
  - Pattern 4: Cross-Harness
  - Pattern 5: Code Review Pipeline
- Best Practices
- Git Worktree Integration
- Complementary Tools
- ECC Helper
- Troubleshooting

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:team-agent-orchestration](affaan-m-ecc-team-agent-orchestration.md) - Run team-based orchestration for agent squads: work items with owners and scope, agent Kanban state, branch is
- [affaan-m/ECC:dynamic-workflow-mode](affaan-m-ecc-dynamic-workflow-mode.md) - Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and ot
- [affaan-m/ECC:token-card](affaan-m-ecc-token-card.md) - Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit
- [affaan-m/ECC:docker-patterns](affaan-m-ecc-docker-patterns.md) - Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security

## Invoke / install

- Invoke: `/affaan-m/ECC:dmux-workflows`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/dmux-workflows --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree dcb7426ed6469c975d0b5002ff17d4669a9e0f3ff06950b4b6ce43fa4b4d3176 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
