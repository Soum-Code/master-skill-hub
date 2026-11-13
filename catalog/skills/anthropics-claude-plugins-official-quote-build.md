# quote-build

> Produces the make-to-order quote from the intake form, comparable prior jobs and cost history, with every number traced to where it came from — material at the price actually paid on a named purchase order, machine hours per operation from a labelled ladder (current routing, closed-job actuals, the confirmed design, first principles) with setup and run kept apart, setup re-amortized at each quantity break, and margin on its own line. Checks the promised date against real shop load before committing to it. Revises in place when a customer counters, preserving what changed and why. Use when someone says "build the quote," "price this job," "what should we charge," "quote this RFQ," or "the customer came back on price."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:quote-build` |
| **Pack** | Careers, Jobs & Hiring (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 491 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when someone says "build the quote," "price this job," "what should we charge," "quote this RFQ," or "the customer came back on price.".

## What it says up front

> Pricing a make-to-order job means building up a cost and then applying commercial judgment. Every job is priced fresh, which is why quoting is skilled, slow, expert work — and why the estimator is usually the bottleneck.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Load the intake form
  - Step 2 — Find comparables
  - Step 3 — Flag capability, then derive the hours
  - Step 4 — Build up the cost
  - Step 5 — Apply quantity breaks
  - Step 6 — Apply margin
  - Step 7 — Check the promised date against shop load
  - Step 8 — Assemble both documents
  - Step 9 — Handle the negotiation loop
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/cost-buildup.md`, `reference/date-and-load.md`, `reference/hours-ladder.md`, `reference/revisions.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p
- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp
- [anthropics/claude-plugins-official:root-cause-capa](anthropics-claude-plugins-official-root-cause-capa.md) - Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timelin

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:quote-build`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/quote-build --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 30e7f7815f76cdb823a373f38ab351aed24f83ef5fa5b7489370ed3f8fe8901e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
