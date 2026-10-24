# profile-user

> Generate developer behavioral profile and create Claude-discoverable artifacts

| | |
|---|---|
| **ID** | `bm:profile-user` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Careers, Jobs & Hiring) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Generate a developer behavioral profile from session analysis (or questionnaire) and produce artifacts (USER-PROFILE.md, /gsd-dev-preferences, CLAUDE.md section) that personalize Claude's responses.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`, `Task`

## Related skills

- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill

## Invoke / install

- Invoke: `/bm:profile-user`  (Skill tool: `bm:profile-user`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
