# plan-orchestrate

> Read a plan document, decompose it into steps, classify each step, and emit the ready-to-paste ECC slash command for that step, carrying the step identifier and scope in the command's own documented argument form. Generative only — never invokes commands itself and never claims to control what a command runs internally. Steps whose command cannot carry plan scope fail closed instead of being emitted. Use when the user has a multi-step plan and wants the right command for each step without picking it by hand.

| | |
|---|---|
| **ID** | `affaan-m/ECC:plan-orchestrate` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 260 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user has a multi-step plan and wants the right command for each step without picking it by hand.

## What it says up front

> Bridge a plan document to the current ECC slash-command surface by emitting one ready-to-paste command per step. This skill is a router only: it picks the command and fills in the command's own documented argument form. It does not compose agent chains and does not influence what a command runs inte

## How it is structured

The skill's own section headings, in order:

- When to Use
- Inputs
- Scope rule — a step is only emitted if the command can carry it
- Task description (scope-carrying commands only)
- Command catalogue
- How It Works
  - Phase 0 — Read the plan
  - Phase 1 — Decompose steps
  - Phase 2 — Classify and pick the command
  - Phase 3 — Compress the task description
  - Phase 4 — Output
  - Phase 5 — Self-check (run before emitting)
- Edge cases
- Examples
  - Example 1 — Feature step with security and DB concerns (emitted)
  - Example 2 — Fix step (emitted)
  - Example 3 — Test step (fails closed)
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:prompt-optimizer](affaan-m-ecc-prompt-optimizer.md) - Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a

## Invoke / install

- Invoke: `/affaan-m/ECC:plan-orchestrate`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/plan-orchestrate --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2580095d00a146912fe583c68d41d2ba3077562c87106a85ed6f6f297389fc20 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
