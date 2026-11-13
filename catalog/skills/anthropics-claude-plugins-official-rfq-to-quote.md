# rfq-to-quote

> Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the plant can build, drafts the questions back, returns a provisional bid/no-bid, pulls cost history, routings and closed-job actuals, builds an internal estimating model in Fusion where connected (from the drawing, a prior part's model saved as new, text specs as a ROM only, or a STEP file), derives machine hours per operation with each hour's basis labelled, and drafts the quote with its cost basis shown. Four approval gates, and the chain pauses for days while the customer answers. Use when someone says "run the RFQ chain," "take this RFQ all the way to a quote," "quote this end to end," "quote this from the drawing," or names an inquiry and asks for the full workflow.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:rfq-to-quote` |
| **Pack** | Security & Privacy (also: AI / ML Engineering, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 331 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when someone says "run the RFQ chain," "take this RFQ all the way to a quote," "quote this end to end," "quote this from the drawing," or names an inquiry and asks for the full workflow.

## What it says up front

> Chain 1. `customer-inquiry-intake` → `data-consolidate` → design step → `quote-build`.

## How it is structured

The skill's own section headings, in order:

- Inputs
- The twelve steps
- Approval gates
- Resuming
  - When the answers come back
  - When a revised drawing arrives
  - When the customer counters on price
  - When they never come back
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/design-step.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp
- [anthropics/claude-plugins-official:quote-build](anthropics-claude-plugins-official-quote-build.md) - Produces the make-to-order quote from the intake form, comparable prior jobs and cost history, with every numb
- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his
- [anthropics/claude-plugins-official:data-consolidate](anthropics-claude-plugins-official-data-consolidate.md) - Joins the plant's scheduled exports and connector data into one working dataset — ERP items (NetSuite or Infor

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:rfq-to-quote`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/rfq-to-quote --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 5e3696d68a931b2882b5d7a79af4c47f8763c515a07653a0c67dadf9b31e878f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
