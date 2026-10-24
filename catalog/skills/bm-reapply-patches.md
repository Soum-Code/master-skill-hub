# reapply-patches

> Reapply local modifications after a GSD update

| | |
|---|---|
| **ID** | `bm:reapply-patches` |
| **Pack** | Communication & Collaboration (also: Spec-driven Dev Workflow, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 310 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> After a GSD update reinstalls files, this command merges the user's previously saved local modifications back in. Uses three-way comparison (pristine baseline, user-modified backup, newly installed version) to distinguish user customizations from version drift.

## How it is structured

The skill's own section headings, in order:

- Step 1: Detect backed-up patches
- Step 2: Determine baseline for three-way comparison
  - Option A: Git history (most reliable)
  - Option B: Pristine snapshot directory
  - Option C: No baseline available (two-way fallback)
- Step 3: Show patch summary
- Step 4: Merge each file
  - Three-way merge (when baseline is available)
  - Two-way merge (fallback when no baseline)
  - Git-enhanced two-way merge
  - Post-merge verification
- Step 5: Hunk Verification Gate
- Step 6: Cleanup option
- Step 7: Report

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`

## Related skills

- [bm:update](bm-update.md) - Update GSD to latest version with changelog display
- [bm:version](bm-version.md) - Print the installed GSD plugin version and check online for updates
- [bm:join-discord](bm-join-discord.md) - Join the GSD Discord community

## Invoke / install

- Invoke: `/bm:reapply-patches`  (Skill tool: `bm:reapply-patches`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
