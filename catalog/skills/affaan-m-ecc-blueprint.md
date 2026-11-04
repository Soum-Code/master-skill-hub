# blueprint

> Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-sized steps with self-contained context briefs, dependency graph with parallel-step detection, adversarial review gate, and plan mutation protocol. Use when planning a large feature, refactor, or roadmap that spans multiple PRs or sessions; not for single-PR tasks or when the user says "just do it".

| | |
|---|---|
| **ID** | `affaan-m/ECC:blueprint` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 98 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when planning a large feature, refactor, or roadmap that spans multiple PRs or sessions; not for single-PR tasks or when the user says "just do it".

## What it says up front

> Turn a one-line objective into a step-by-step construction plan that any coding agent can execute cold.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Examples
  - Basic usage
  - Multi-agent project
- Key Features
- Installation
  - Full ECC install
  - Vendored standalone install
- Requirements
- Source

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes
- [affaan-m/ECC:dev-team](affaan-m-ecc-dev-team.md) - Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer, QA) re
- [affaan-m/ECC:claude-devfleet](affaan-m-ecc-claude-devfleet.md) - Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s

## Invoke / install

- Invoke: `/affaan-m/ECC:blueprint`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/blueprint --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 0221125e336958bd4e82a3203429910a69b67ddc6f130edc3beb52c73fc74990 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
