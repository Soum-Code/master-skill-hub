# customer-inquiry-intake

> Reads a customer RFQ in whatever shape it arrived — a PDF drawing package, a 40-line spreadsheet, a portal export, a phone photo of a marked-up print, or a forwarded thread where the real requirement is four messages down — and pulls specifications, quantities and dates into one consistent intake form with every field traceable to the file and page it came from. Records how each tolerance was read and which geometry path each line takes. Reports what was never stated separately from what was stated two different ways. Checks the request against what the plant can actually build before asking the customer anything, drafts the questions back as sendable text, and returns a provisional bid/no-bid that names which unanswered question would change it. Use when someone says "an RFQ came in," "can we quote this," "should we bid this job," "read this inquiry," or "what's missing from this RFQ?"

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:customer-inquiry-intake` |
| **Pack** | Operations & Business (also: Data & Analytics, Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 394 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when someone says "an RFQ came in," "can we quote this," "should we bid this job," "read this inquiry," or "what's missing from this RFQ?".

## What it says up front

> An RFQ is a customer asking *what would this cost, and when could I have it?*

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Ingest
  - Step 2 — Extract into the intake form
  - Step 3 — Flag missing and ambiguous, separately
  - Step 4 — Check manufacturability, before anything goes to the customer
  - Step 5 — Draft the questions back
  - Step 6 — Score the provisional bid/no-bid recommendation
  - Step 7 — Fold in the answers, and handle the ones that never come
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/arrival-formats.md`, `reference/bid-no-bid.md`, `reference/registers.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p
- [anthropics/claude-plugins-official:supplier-quote-request](anthropics-claude-plugins-official-supplier-quote-request.md) - Builds the RFQ package that goes out to suppliers — drawing and specification at the verified current revision
- [anthropics/claude-plugins-official:quote-build](anthropics-claude-plugins-official-quote-build.md) - Produces the make-to-order quote from the intake form, comparable prior jobs and cost history, with every numb
- [anthropics/claude-plugins-official:daily-production-report](anthropics-claude-plugins-official-daily-production-report.md) - Produces the morning production report: output against plan by line, cell and product; OEE with availability, 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:customer-inquiry-intake`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/customer-inquiry-intake --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree cfb2ab9aeb5e24651b01ef82e9f49ee94088876b8d837ca0226d2de058f2d866 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
