# daily-production-report

> Produces the morning production report: output against plan by line, cell and product; OEE with availability, performance and quality shown separately; the downtime log ranked both by minutes and by frequency; scrap and downtime priced in dollars; week-over-week movers; and the exceptions needing a decision today. For each significant exception it drafts a specific reschedule or changeover move with its consequences traced, never a re-optimised day. Reads the consolidated dataset and leads with data freshness. When the plant has a floor plan on file, or attaches one, it also draws each machine's OEE, availability and downtime on a schematic of the floor. Use when someone says "morning report," "production report," "how did we do yesterday," "what's our OEE," "downtime report," "what's late," or "what do I take into the production meeting."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:daily-production-report` |
| **Pack** | Data & Analytics (also: Documents, Writing & Content, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 487 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when someone says "morning report," "production report," "how did we do yesterday," "what's our OEE," "downtime report," "what's late," or "what do I take into the production meeting.".

## What it says up front

> Every plant runs a morning production meeting, and somebody spends 60 to 90 minutes before it assembling the same report by hand out of the same four or five exports. This is that report.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Confirm freshness
  - Step 2 — Output against plan
  - Step 3 — Compute OEE
  - Step 4 — Build the downtime log
  - Step 5 — Price the losses
  - Step 6 — Week-over-week movers
  - Step 7 — Fold in breakdown diagnoses
  - Step 8 — Identify exceptions
  - Step 9 — Propose the reschedule or changeover move
  - Step 9a — Floor view
  - Step 10 — Emit
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/floor-schematic.md`, `reference/oee.md`, `reference/reschedule-scope.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:morning-plant-pulse](anthropics-claude-plugins-official-morning-plant-pulse.md) - Runs the overnight chain that has the morning production report waiting before anyone asks for it: joins last 
- [anthropics/claude-plugins-official:breakdown-to-next-report](anthropics-claude-plugins-official-breakdown-to-next-report.md) - Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the s
- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp
- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:daily-production-report`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/daily-production-report --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 921266236f01666eac82028c04d9f79cd74f30a403791ac5f83bee25a1ddffeb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
