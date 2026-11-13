# breakdown-diagnosis

> When a machine goes down, reads the sensor window before the failure, the asset's maintenance history including the free-text close-out notes technicians actually wrote, photos of what they can see, and the manufacturer's troubleshooting tree — then ranks likely causes, each with its supporting evidence, the specific prior work orders behind it, and the cheapest test that would tell them apart. Surfaces any safety implication before any diagnosis. Drafts the PM interval change that would stop it recurring, and emits a downtime record for the next production report. Batch mode ranks bad actors across every asset. Use when someone says "the machine is down," "what's wrong with this machine," "why does this keep failing," "diagnose this," or "which machines are hurting us most."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:breakdown-diagnosis` |
| **Pack** | AI / ML Engineering (also: Operations & Business, Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 362 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when someone says "the machine is down," "what's wrong with this machine," "why does this keep failing," "diagnose this," or "which machines are hurting us most.".

## What it says up front

> A machine is down. Every minute it stays down, the plant is not producing — and **the largest component of MTTR is usually not the repair, it is working out what is wrong.**

## How it is structured

The skill's own section headings, in order:

- Safety leads. Always.
- Inputs
- Workflow
  - Step 1 — Capture the event
  - Step 2 — Pull the sensor window
  - Step 3 — Mine the maintenance history and close-out notes
  - Step 4 — Read the photos
  - Step 5 — Consult the manual
  - Step 6 — Rank candidate causes
  - Step 7 — Cite the specific prior work orders
  - Step 8 — Propose the PM plan adjustment
  - Step 9 — Batch mode: the bad actor ranking
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/bad-actor-mode.md`, `reference/evidence-sources.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:breakdown-to-next-report](anthropics-claude-plugins-official-breakdown-to-next-report.md) - Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the s
- [anthropics/claude-plugins-official:root-cause-capa](anthropics-claude-plugins-official-root-cause-capa.md) - Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timelin
- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp
- [anthropics/claude-plugins-official:data-consolidate](anthropics-claude-plugins-official-data-consolidate.md) - Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:breakdown-diagnosis`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/breakdown-diagnosis --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree ac57c4d9f0f97f7ddb607e6dafde7ee60115755411177059b7404934da7df9d9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
