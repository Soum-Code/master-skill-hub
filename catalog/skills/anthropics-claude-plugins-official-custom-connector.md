# custom-connector

> Gets the plugin talking to a manufacturing system that has no vendor MCP, working down a seven-tier access ladder in order — vendor MCP, community MCP, a scoped API wrapper, a read-only database view, a Zapier bridge, screen automation as a last resort, or a scheduled export contract — and stopping at the highest rung that actually works. States plainly at every rung what the customer gets, what it costs, and how it will eventually break. Most often the answer is that a vendor MCP already exists and nothing needs building — just an admin turning it on. Maps whatever it reaches onto the consolidated dataset schema, so no downstream skill changes. Credentials never enter the conversation. Use when someone says "connect our ERP," "we use SAP," "can you reach our MES," "set up a connector for this system," or "our system isn't supported."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:custom-connector` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 419 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when someone says "connect our ERP," "we use SAP," "can you reach our MES," "set up a connector for this system," or "our system isn't supported.".

## What it says up front

> SAP and Infor have the largest installed base in manufacturing, and neither has an official MCP for business data. Neither does most of what actually runs a mid-market plant — a large share of it is on-prem, a decade old, and has a SQL database but no API at all. **That is not a failure case. It is

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Identify the system precisely
  - Step 2 — Scope the need before looking at access
  - Step 3 — Work the ladder, in order
  - Step 4 — Report the finding before building anything
  - Step 5 — Pick the tier, and record why
  - Step 6 — Handle credentials properly
  - Step 7 — Build scoped
  - Step 8 — Gate every write path
  - Step 9 — Map onto the consolidated dataset schema
  - Step 10 — Test against real data, and show it back
  - Step 11 — Register it
  - Step 12 — Say how it will break
- Approval gates
- Output
- Edge cases and failure modes
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/access-ladder.md`, `reference/credentials-and-failure-modes.md`, `reference/known-systems.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:data-consolidate](anthropics-claude-plugins-official-data-consolidate.md) - Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:custom-connector`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/custom-connector --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 3920f2f951b1c4e64590d60e5de79761b9a9113cdd69cad1f2001030be35b45d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
