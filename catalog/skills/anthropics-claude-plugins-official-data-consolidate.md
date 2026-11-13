# data-consolidate

> Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor M3), sales orders, production work orders, purchase orders, inventory, routings and closed-job operation actuals; CMMS assets and maintenance work orders; and the MES, historian, quality and planning files landing in the Microsoft 365 export folder. Keys on part number, production work order, sales order, lot, asset and supplier, classifies every key that fails to match into one of eight mismatch classes, and proposes the correction rather than reporting a count, applying nothing without a yes. Runs file-only with no connector, or connector-only with no files. Use when someone says "pull the data together," "consolidate the exports," "build the dataset," "join production to the ERP," or "why don't these numbers match," and before any reporting or quoting skill runs.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:data-consolidate` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 487 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when someone says "pull the data together," "consolidate the exports," "build the dataset," "join production to the ERP," or "why don't these numbers match," and before any reporting or quoting skill runs.

## What it says up front

> The foundation layer. The dataset this skill produces is where every data-dependent skill reads from by default, rather than going back to the raw sources — and it is the only place the sources are joined and their key mismatches classified.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Discover
  - Step 2 — Freshness check
  - Step 3 — Pull connector data
  - Step 4 — Normalize keys
  - Step 5 — Join
  - Step 6 — Classify mismatches
  - Step 7 — Count in code, and reconcile before writing
  - Step 8 — Emit
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/join-keys.md`, `reference/mismatch-classes.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:morning-plant-pulse](anthropics-claude-plugins-official-morning-plant-pulse.md) - Runs the overnight chain that has the morning production report waiting before anyone asks for it: joins last 
- [anthropics/claude-plugins-official:custom-connector](anthropics-claude-plugins-official-custom-connector.md) - Gets the plugin talking to a manufacturing system that has no vendor MCP, working down a seven-tier access lad
- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p
- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:data-consolidate`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/data-consolidate --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 773aa3effe633e44f6497efa83d1928fdb6788c1b312a5b67c0f101cb9912a1a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
