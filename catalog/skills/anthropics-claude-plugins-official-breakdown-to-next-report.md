# breakdown-to-next-report

> Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the sensor window, the maintenance history and its free-text close-out notes, technician photographs and the manufacturer's manual together, ranks likely causes with the cheapest test that tells them apart, then folds the diagnosis and its downtime into the next morning's downtime log and exceptions. Use when someone says "run the breakdown chain," "a machine went down," "diagnose this and get it into the report," or "breakdown to next report."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:breakdown-to-next-report` |
| **Pack** | Data & Analytics (also: Documents, Writing & Content, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 211 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when someone says "run the breakdown chain," "a machine went down," "diagnose this and get it into the report," or "breakdown to next report.".

## What it says up front

> Chain 4. `breakdown-diagnosis` → `daily-production-report`.

## How it is structured

The skill's own section headings, in order:

- Inputs
- The five steps
- Approval gates
- The handoff is the chain's whole risk
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:breakdown-diagnosis](anthropics-claude-plugins-official-breakdown-diagnosis.md) - When a machine goes down, reads the sensor window before the failure, the asset's maintenance history includin
- [anthropics/claude-plugins-official:root-cause-capa](anthropics-claude-plugins-official-root-cause-capa.md) - Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timelin
- [anthropics/claude-plugins-official:daily-production-report](anthropics-claude-plugins-official-daily-production-report.md) - Produces the morning production report: output against plan by line, cell and product; OEE with availability, 
- [anthropics/claude-plugins-official:morning-plant-pulse](anthropics-claude-plugins-official-morning-plant-pulse.md) - Runs the overnight chain that has the morning production report waiting before anyone asks for it: joins last 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:breakdown-to-next-report`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/breakdown-to-next-report --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 8dfaf4466e5d10fbf50405a75f422242783c24d954a4e0fb0e1351d0fbb7d773 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
