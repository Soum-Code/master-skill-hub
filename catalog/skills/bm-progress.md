# progress

> Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6-check integrity audit after the standard report.

| | |
|---|---|
| **ID** | `bm:progress` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 27 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Check project progress, summarize recent work and what's ahead, then intelligently route to the next action - either executing an existing plan or creating the next one.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Grep`, `Glob`, `SlashCommand`

## Related skills

- [openai/skills:gh-fix-ci](openai-skills-gh-fix-ci.md) - Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect 
- [bm:ingest-docs](bm-ingest-docs.md) - Scan a repo for mixed ADRs, PRDs, SPECs, and DOCs and bootstrap or merge the full .planning/ setup from them. 
- [bm:new-project](bm-new-project.md) - Initialize a new project with deep context gathering and PROJECT.md
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization

## Invoke / install

- Invoke: `/bm:progress`  (Skill tool: `bm:progress`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
