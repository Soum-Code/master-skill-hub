# ui-phase

> Generate UI design contract (UI-SPEC.md) for frontend phases

| | |
|---|---|
| **ID** | `bm:ui-phase` |
| **Pack** | Web, Frontend & UI Design (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 35 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create a UI design contract (UI-SPEC.md) for a frontend phase. Orchestrates gsd-ui-researcher and gsd-ui-checker. Flow: Validate → Research UI → Verify UI-SPEC → Done

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `Task`, `WebFetch`, `AskUserQuestion`, `mcp__context7__*`

## Related skills

- [bm:ai-integration-phase](bm-ai-integration-phase.md) - Generate AI design contract (AI-SPEC.md) for phases that involve building AI systems — framework selection, im
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:ui-review](bm-ui-review.md) - Retroactive 6-pillar visual audit of implemented frontend code
- [bm:analyze-dependencies](bm-analyze-dependencies.md) - Analyze phase dependencies and suggest Depends on entries for ROADMAP.md

## Invoke / install

- Invoke: `/bm:ui-phase`  (Skill tool: `bm:ui-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
