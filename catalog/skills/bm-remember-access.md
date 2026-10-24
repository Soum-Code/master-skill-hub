# remember-access

> Capture or review how this project connects to external systems (GitHub, AWS, npm, SSH, etc.) so future sessions know the auth recipe. Auto-detection hook logs candidate captures to an inbox; this skill promotes them to permanent recipes in `.planning/AUTH-RECIPES.md` and optionally to user-global memory at `~/.claude/auth-recipes/`.

| | |
|---|---|
| **ID** | `bm:remember-access` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 32 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Auth setup is one of those things every project does once and then forgets the details of. GSD captures the recipe so future sessions on the same project (or future projects on the same system) can replay or surface it.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `Edit`, `AskUserQuestion`

## Related skills

- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f

## Invoke / install

- Invoke: `/bm:remember-access`  (Skill tool: `bm:remember-access`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
