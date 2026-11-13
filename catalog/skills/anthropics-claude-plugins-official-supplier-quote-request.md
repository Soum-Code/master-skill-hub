# supplier-quote-request

> Builds the RFQ package that goes out to suppliers — drawing and specification at the verified current revision, the demand picture, the quality clause list, commercial terms, and a mandated response format that makes the returned bids comparable by construction. Lists everything missing. Hard stops on a revision mismatch or restricted technical data. Then runs the supplier loop: candidates from the approved supplier list with unapproved and single-source flagged, one email draft per supplier for the buyer to send, response tracking with chase drafts, returned bids read into one shape with every missing field listed, a comparison per quantity break computed in code, and a recommendation. The buyer decides; the skill records who and when. Use when someone says "source this part," "send an RFQ to suppliers," "we need an alternate supplier," "get quotes on this," "who else can make this?", "chase the suppliers," "compare these bids," or "we're going with this supplier."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:supplier-quote-request` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 413 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when someone says "source this part," "send an RFQ to suppliers," "we need an alternate supplier," "get quotes on this," "who else can make this?", "chase the suppliers," "compare these bids," or "we're going with this supplier.".

## What it says up front

> The RFQ pointed the other way: instead of a customer asking us to quote, we are asking suppliers to quote us.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Take the trigger
  - Step 2 — Assemble the technical package, and verify the revision
  - Step 3 — Build the demand picture, and state the delivery requirements
  - Step 4 — Attach the quality clause list at current revision
  - Step 5 — Attach commercial terms
  - Step 6 — Specify the response schedule and format
  - Step 7 — List what is missing
  - Step 8 — Identify candidate suppliers
  - Step 9 — Draft one email per supplier
  - Step 10 — Track responses, and chase
  - Step 11 — Read each returned bid into one shape
  - Step 12 — Compare, in code
  - Step 13 — Recommend; the buyer decides
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/bid-comparability.md`, `reference/bid-comparison.md`, `reference/hard-stops.md`, `reference/quality-clauses.md`, `reference/supplier-loop.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:customer-inquiry-intake](anthropics-claude-plugins-official-customer-inquiry-intake.md) - Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal exp
- [anthropics/claude-plugins-official:supplier-escape-to-alternate-source](anthropics-claude-plugins-official-supplier-escape-to-alternate-source.md) - Runs the cross-area chain from a nonconformance traced to purchased material through to an alternate-source RF
- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:supplier-quote-request`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/supplier-quote-request --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 16fd900ef402294ad32f59a53848ddffac9f683e7e343f248c0f6c04978babe3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
