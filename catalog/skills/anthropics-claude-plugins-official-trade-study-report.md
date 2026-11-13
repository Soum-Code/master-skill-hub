# trade-study-report

> Turns a filled-in trade study matrix and its analysis results into a scored comparison and a decision memo, with every score cited to its source. Runs the sensitivity analysis every time — where the winner flips, which criterion the decision actually rests on, whether an option never wins under any plausible weighting — because a recommendation with no sensitivity check is a spreadsheet, not a decision. Disqualifies options that violate a hard constraint rather than scoring them low. Consumes design-space-explore's variant manifest when one exists, or a matrix filled in by hand when it doesn't. Use when someone says "compare these options," "write the trade study," "which design should we pick," "score these against the requirements," or "how sensitive is this decision to the weighting."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:trade-study-report` |
| **Pack** | Research & Learning (also: Data & Analytics, Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 237 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when someone says "compare these options," "write the trade study," "which design should we pick," "score these against the requirements," or "how sensitive is this decision to the weighting.".

## What it says up front

> A trade study is the formal way an engineering team chooses between design options: criteria that matter, weights on how much, options scored against each one, a weighted total that ranks them, and a memo that defends the pick in review.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Load the matrix
  - Step 2 — Ingest analysis results
  - Step 3 — Compute weighted totals and rank
  - Step 4 — Run the sensitivity analysis
  - Step 5 — Check constraint compliance, separately from scoring
  - Step 6 — Write the decision memo
  - Step 7 — Produce the scored comparison table
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/decision-memo.md`, `reference/matrix-and-scoring.md`, `reference/sensitivity-analysis.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:design-space-explore](anthropics-claude-plugins-official-design-space-explore.md) - Generates a batch of CAD variants directly in Autodesk Fusion by applying changed parameters to an engineer's 
- [anthropics/claude-plugins-official:ncr-writeup](anthropics-claude-plugins-official-ncr-writeup.md) - Writes the nonconformance report: what was found and measured, the specific requirement it violates cited to i

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:trade-study-report`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/trade-study-report --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree c972c49479dbb1c7cf47efac365e5516ad89737eb3ef45563e181773436c65fc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
