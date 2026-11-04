# agent-introspection-debugging

> Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports. Use when an agent run fails and you need a reproducible diagnosis instead of a retry.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-introspection-debugging` |
| **Pack** | Software Development (also: AI / ML Engineering, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 155 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an agent run fails and you need a reproducible diagnosis instead of a retry.

## What it says up front

> Use this skill when an agent run is failing repeatedly, consuming tokens without progress, looping on the same tools, or drifting away from the intended task.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Scope Boundaries
- Four-Phase Loop
  - Phase 1: Failure Capture
  - Phase 2: Root-Cause Diagnosis
  - Phase 3: Contained Recovery
  - Phase 4: Introspection Report
- Recovery Heuristics
- Integration with ECC
- Output Standard

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:continuous-agent-loop](affaan-m-ecc-continuous-agent-loop.md) - Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when runn

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-introspection-debugging`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-introspection-debugging --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9b3f268344cb180320e17a5e1e26cc5eef436034b6e5da667d18a922868caf03 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
