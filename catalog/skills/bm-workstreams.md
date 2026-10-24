# workstreams

> Manage parallel workstreams — list, create, switch, status, progress, complete, and resume

| | |
|---|---|
| **ID** | `bm:workstreams` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 69 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Manage parallel workstreams for concurrent milestone work.

## How it is structured

The skill's own section headings, in order:

- Usage
  - Subcommands
- Step 1: Parse Subcommand
- Step 2: Execute Operation
  - list
  - create
  - status
  - switch
  - progress
  - complete
  - resume
- Step 3: Display Results

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`

## Related skills

- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status
- [finance:close-management](finance-close-management.md) - Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning 
- [openai/skills:linear](openai-skills-linear.md) - Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets

## Invoke / install

- Invoke: `/bm:workstreams`  (Skill tool: `bm:workstreams`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
