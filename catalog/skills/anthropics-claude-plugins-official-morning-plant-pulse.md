# morning-plant-pulse

> Runs the overnight chain that has the morning production report waiting before anyone asks for it: joins last night's planning, production and maintenance exports, flags the mismatched keys, then computes output against plan, OEE with its three components, downtime ranked two ways, priced losses and the exceptions needing a decision. Stores a record per production day and keeps one Operations Command Center dashboard per site up to date, with a 14 and 30 day trend. Safe to run unattended. Use when someone says "run the morning pulse," "do the overnight report," "morning plant pulse," "update the operations dashboard," or schedules the daily production run.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:morning-plant-pulse` |
| **Pack** | Productivity & Automation (also: Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 372 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when someone says "run the morning pulse," "do the overnight report," "morning plant pulse," "update the operations dashboard," or schedules the daily production run.

## What it says up front

> Chain 3. `data-consolidate` → `daily-production-report` → publish.

## How it is structured

The skill's own section headings, in order:

- Inputs
- The three steps
- What "safe to run unattended" actually requires
- Approval gates
- Scheduling
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- scripts: `scripts/pulse_compute.py`, `scripts/render_short.py`
- reference docs: `reference/compute-engine.md`, `reference/operations-dashboard.md`, `reference/short-page.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:daily-production-report](anthropics-claude-plugins-official-daily-production-report.md) - Produces the morning production report: output against plan by line, cell and product; OEE with availability, 
- [anthropics/claude-plugins-official:data-consolidate](anthropics-claude-plugins-official-data-consolidate.md) - Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor
- [anthropics/claude-plugins-official:breakdown-to-next-report](anthropics-claude-plugins-official-breakdown-to-next-report.md) - Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the s
- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:morning-plant-pulse`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/morning-plant-pulse --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 8aa71f5b84844be059bd5b9ed2b772b35a71075c05ff8f60d83fbe7e00b88c09 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
