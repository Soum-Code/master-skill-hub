# agent-eval

> Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics. Use when choosing between coding agents, or when a change to an agent setup needs measured pass rate, cost, and time rather than an impression.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-eval` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 148 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when choosing between coding agents, or when a change to an agent setup needs measured pass rate, cost, and time rather than an impression.

## What it says up front

> A lightweight CLI tool for comparing coding agents head-to-head on reproducible tasks. Every "which coding agent is best?" comparison runs on vibes — this tool systematizes it.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Installation
- Core Concepts
  - YAML Task Definitions
  - Git Worktree Isolation
  - Metrics Collected
- Workflow
  - 1. Define Tasks
  - 2. Run Agents
  - 3. Compare Results
- Judge Types
  - Code-Based (deterministic)
  - Pattern-Based
  - Model-Based (LLM-as-judge)
- Best Practices
- Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:eval-harness](affaan-m-ecc-eval-harness.md) - Eval-driven development (EDD) framework for AI coding sessions — define capability and regression evals before
- [affaan-m/ECC:claude-devfleet](affaan-m-ecc-claude-devfleet.md) - Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated
- [affaan-m/ECC:token-card](affaan-m-ecc-token-card.md) - Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-eval`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-eval --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 867f47401194d0161fe8e76d73e5d4c2fd212deb2d851f2db9846c80214a67f9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
