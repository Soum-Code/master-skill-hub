# team-agent-orchestration

> Run team-based orchestration for agent squads: work items with owners and scope, agent Kanban state, branch isolation, control pane visibility, and merge gates. Use when coordinating multiple agents in parallel across branches or worktrees — multi-agent fan-out, agent Kanban, squad coordination, or merging agent output into one product.

| | |
|---|---|
| **ID** | `affaan-m/ECC:team-agent-orchestration` |
| **Pack** | Communication & Collaboration (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 112 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when coordinating multiple agents in parallel across branches or worktrees — multi-agent fan-out, agent Kanban, squad coordination, or merging agent output into one product.

## What it says up front

> Use this skill when agents are being managed like a team rather than a single assistant. The purpose is to make team-based orchestration reliable: clear work items, explicit ownership, agent Kanban state, branch isolation, control pane visibility, and merge gates.

## How it is structured

The skill's own section headings, in order:

- When To Activate
- Operating Model
- Agent Kanban
- Team-Based Orchestration Flow
- Control Pane Requirements
- Dynamic Workflow Compatibility
- Failure Modes To Watch
- Output Standard

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [affaan-m/ECC:dev-team](affaan-m-ecc-dev-team.md) - Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer, QA) re
- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes
- [affaan-m/ECC:claude-devfleet](affaan-m-ecc-claude-devfleet.md) - Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated

## Invoke / install

- Invoke: `/affaan-m/ECC:team-agent-orchestration`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/team-agent-orchestration --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree d53a798a9902af7dfd06dfe88d465366adf4243d1abb4ad12ba52dfad89834a1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
