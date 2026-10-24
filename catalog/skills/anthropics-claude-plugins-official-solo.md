# solo

> Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in a notes file so that nothing written is lost if a response is cut off, and end with a self-contained proof.md. Usage: /math-proof:solo .

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:solo` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 70 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> You solve the problem yourself, in this session. There are no sub-agents and no rounds: just you, a notes file and, at the end, proof.md.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash(mkdir`, `*)`, `Bash(cp`, `*)`, `Bash(cmp`, `*)`

## Related skills

- [anthropics/claude-plugins-official:siege](anthropics-claude-plugins-official-siege.md) - Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, inde

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:solo`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/math-proof/skills/solo --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 3eecbb23f82abab4f715610ff1441d9957718d37d75dded7f48c6798beb9f4fa --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
