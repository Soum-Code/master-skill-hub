# continuous-agent-loop

> Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when running an agent loop that must self-check, gate on evals, and recover from failures.

| | |
|---|---|
| **ID** | `affaan-m/ECC:continuous-agent-loop` |
| **Pack** | AI / ML Engineering (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when running an agent loop that must self-check, gate on evals, and recover from failures.

## What it says up front

> This is the v1.8+ canonical loop skill name. It supersedes `autonomous-loops` while keeping compatibility for one release.

## How it is structured

The skill's own section headings, in order:

- Loop Selection Flow
- Combined Pattern
- Failure Modes
- Recovery

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:autonomous-loops](affaan-m-ecc-autonomous-loops.md) - Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven m
- [affaan-m/ECC:loop-design-check](affaan-m-ecc-loop-design-check.md) - Design a goal-oriented agent loop or review one for failure modes: spinning, Goodhart-gaming the verifier, or 
- [affaan-m/ECC:agent-introspection-debugging](affaan-m-ecc-agent-introspection-debugging.md) - Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and int
- [affaan-m/ECC:delivery-gate](affaan-m-ecc-delivery-gate.md) - Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surfa

## Invoke / install

- Invoke: `/affaan-m/ECC:continuous-agent-loop`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/continuous-agent-loop --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree aea0874df50f678ecdc55a534da2eced2367d67112b58bac9a92ec1bff152cc7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
