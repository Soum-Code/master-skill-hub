# debug

> Systematic debugging with persistent state across context resets

| | |
|---|---|
| **ID** | `bm:debug` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 258 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Debug issues using scientific method with subagent isolation.

## How it is structured

The skill's own section headings, in order:

- 0. Initialize Context
- 1a. LIST subcommand
- 1b. STATUS subcommand
- 1c. CONTINUE subcommand
- 1d. Check Active Sessions (SUBCMD=debug)
- 2. Gather Symptoms (if new issue, SUBCMD=debug)
- 3. Initial Session Setup (new session)
- 4. Session Management (delegated to gsd-debug-session-manager)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Task`, `AskUserQuestion`

## Related skills

- [bm:thread](bm-thread.md) - Manage persistent context threads for cross-session work

## Invoke / install

- Invoke: `/bm:debug`  (Skill tool: `bm:debug`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
