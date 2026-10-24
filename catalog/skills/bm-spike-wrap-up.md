# spike-wrap-up

> Package spike findings into a persistent project skill for future build conversations

| | |
|---|---|
| **ID** | `bm:spike-wrap-up` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 32 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Curate spike experiment findings and package them into a persistent project skill that Claude auto-loads in future build conversations. Also writes a summary to `.planning/spikes/` for project history. Output skill goes to `./.claude/skills/spike-findings-[project]/` (project-local).

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `AskUserQuestion`

## Related skills

- [bm:sketch-wrap-up](bm-sketch-wrap-up.md) - Package sketch design findings into a persistent project skill for future build conversations
- [bm:graphify](bm-graphify.md) - Build, query, and inspect the project knowledge graph in .planning/graphs/
- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.

## Invoke / install

- Invoke: `/bm:spike-wrap-up`  (Skill tool: `bm:spike-wrap-up`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
