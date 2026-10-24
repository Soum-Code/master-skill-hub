# eval-review

> Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL/MISSING and produces an actionable EVAL-REVIEW.md with remediation plan

| | |
|---|---|
| **ID** | `bm:eval-review` |
| **Pack** | AI / ML Engineering (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 33 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Conduct a retroactive evaluation coverage audit of a completed AI phase. Checks whether the evaluation strategy from AI-SPEC.md was implemented. Produces EVAL-REVIEW.md with score, verdict, gaps, and remediation plan.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`

## Related skills

- [bm:review](bm-review.md) - Request cross-AI peer review of phase plans from external AI CLIs
- [bm:ai-integration-phase](bm-ai-integration-phase.md) - Generate AI design contract (AI-SPEC.md) for phases that involve building AI systems — framework selection, im
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop

## Invoke / install

- Invoke: `/bm:eval-review`  (Skill tool: `bm:eval-review`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
