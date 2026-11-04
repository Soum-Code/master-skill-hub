# ralphinho-rfc-pipeline

> Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tests, run research, plan, implement, test, and review per unit, then merge through a queue with re-based branches and final system verification. Use when a feature is too large for a single agent pass, orchestrating RFC-driven multi-agent execution, or managing merge queues across agent-built units.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ralphinho-rfc-pipeline` |
| **Pack** | Spec-driven Dev Workflow (also: MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 69 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a feature is too large for a single agent pass, orchestrating RFC-driven multi-agent execution, or managing merge queues across agent-built units.

## What it says up front

> Inspired by [humanplane](https://github.com/humanplane) style RFC decomposition patterns and multi-unit orchestration workflows.

## How it is structured

The skill's own section headings, in order:

- Pipeline Stages
- Unit Spec Template
- Complexity Tiers
- Quality Pipeline per Unit
- Merge Queue Rules
- Recovery
- Outputs

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:autonomous-loops](affaan-m-ecc-autonomous-loops.md) - Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven m
- [affaan-m/ECC:blueprint](affaan-m-ecc-blueprint.md) - Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering pro
- [affaan-m/ECC:team-agent-orchestration](affaan-m-ecc-team-agent-orchestration.md) - Run team-based orchestration for agent squads: work items with owners and scope, agent Kanban state, branch is
- [bm:verify-work](bm-verify-work.md) - Validate built features through conversational UAT

## Invoke / install

- Invoke: `/affaan-m/ECC:ralphinho-rfc-pipeline`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ralphinho-rfc-pipeline --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 02b8f849b39125cff8690b7b5c8d461c355d3d4056c5b4c7bececaaeb1a49e75 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
