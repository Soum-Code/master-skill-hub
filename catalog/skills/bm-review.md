# review

> Request cross-AI peer review of phase plans from external AI CLIs

| | |
|---|---|
| **ID** | `bm:review` |
| **Pack** | Spec-driven Dev Workflow (also: Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 41 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Invoke external AI CLIs (Gemini, Claude, Codex, OpenCode, Qwen Code, Cursor) to independently review phase plans. Produces a structured REVIEWS.md with per-reviewer feedback that can be fed back into planning via /bm:plan-phase --reviews.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`

## Related skills

- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:eval-review](bm-eval-review.md) - Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL
- [bm:audit-uat](bm-audit-uat.md) - Cross-phase audit of all outstanding UAT and verification items

## Invoke / install

- Invoke: `/bm:review`  (Skill tool: `bm:review`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
