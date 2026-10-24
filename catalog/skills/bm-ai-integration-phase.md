# ai-integration-phase

> Generate AI design contract (AI-SPEC.md) for phases that involve building AI systems — framework selection, implementation guidance from official docs, and evaluation strategy

| | |
|---|---|
| **ID** | `bm:ai-integration-phase` |
| **Pack** | AI / ML Engineering (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 37 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create an AI design contract (AI-SPEC.md) for a phase involving AI system development. Orchestrates gsd-framework-selector → gsd-ai-researcher → gsd-domain-researcher → gsd-eval-planner. Flow: Select Framework → Research Docs → Research Domain → Design Eval Strategy → Done

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `Task`, `WebFetch`, `WebSearch`, `AskUserQuestion`, `mcp__context7__*`

## Related skills

- [bm:ui-phase](bm-ui-phase.md) - Generate UI design contract (UI-SPEC.md) for frontend phases
- [bm:eval-review](bm-eval-review.md) - Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL
- [bm:spec-phase](bm-spec-phase.md) - Socratic spec refinement — clarify WHAT a phase delivers with ambiguity scoring before discuss-phase. Produces
- [bm:add-tests](bm-add-tests.md) - Generate tests for a completed phase based on UAT criteria and implementation

## Invoke / install

- Invoke: `/bm:ai-integration-phase`  (Skill tool: `bm:ai-integration-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
