# ship

> Create PR, run review, and prepare for merge after verification passes

| | |
|---|---|
| **ID** | `bm:ship` |
| **Pack** | MLOps / DevOps / Cloud (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 36 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Bridge local completion → merged PR. After /bm:verify-work passes, ship the work: push branch, create PR with auto-generated body, optionally trigger review, and track the merge.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Grep`, `Glob`, `Write`, `AskUserQuestion`

## Related skills

- [bm:pr-branch](bm-pr-branch.md) - Create a clean PR branch by filtering out .planning/ commits — ready for code review
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [affaan-m/ECC:production-audit](affaan-m-ecc-production-audit.md) - Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b
- [affaan-m/ECC:canary-watch](affaan-m-ecc-canary-watch.md) - Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, stati

## Invoke / install

- Invoke: `/bm:ship`  (Skill tool: `bm:ship`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
