# ncr-writeup

> Writes the nonconformance report: what was found and measured, the specific requirement it violates cited to its document and locator, how many parts are actually suspect and why that scope rather than a narrower one, and where every one of them physically is across all five locations. Searches prior NCRs and CAPAs at the moment of writing and reports whether the earlier fix held. Where containment places parts at a customer, drafts the escape notification automatically against its contractual clock. Never asserts a requirement it cannot locate. Keeps the site's Quality Register of open NCRs up to date, and closes an NCR there when told to. Use when someone says "write up this nonconformance," "we found bad parts," "raise an NCR," "the inspector rejected this lot," "a customer is complaining about a part," or "close NCR-2026-0141."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:ncr-writeup` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 384 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when someone says "write up this nonconformance," "we found bad parts," "raise an NCR," "the inspector rejected this lot," "a customer is complaining about a part," or "close NCR-2026-0141.".

## What it says up front

> The formal record that something did not meet its requirement, written by whoever found it — an inspector, an operator, a customer complaint landing in somebody's inbox.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Capture the finding, structured
  - Step 2 — Cite the requirement
  - Step 3 — Scope the affected quantity
  - Step 4 — Locate the parts
  - Step 5 — Recommend containment per location
  - Step 6 — Search history, now
  - Step 7 — Draft the escape notification
  - Step 8 — Write the register row, and update the Quality Register
  - Closing an NCR
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/recurrence-and-escape.md`, `reference/requirement-citation.md`, `reference/scope-and-containment.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his
- [anthropics/claude-plugins-official:trade-study-report](anthropics-claude-plugins-official-trade-study-report.md) - Turns a filled-in trade study matrix and its analysis results into a scored comparison and a decision memo, wi
- [anthropics/claude-plugins-official:root-cause-capa](anthropics-claude-plugins-official-root-cause-capa.md) - Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timelin

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:ncr-writeup`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/ncr-writeup --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 005b119964dcf6c78b9bbb1eb9ab333fb24c5f5430442af72d7acd9d1e56e7fe --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
