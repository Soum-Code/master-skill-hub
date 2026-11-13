# supplier-escape-to-alternate-source

> Runs the cross-area chain from a nonconformance traced to purchased material through to an alternate-source RFQ: writes the NCR and its containment, establishes root cause against the supplier rather than the process, records the corrective action, then builds the sourcing package with a response format that makes the returned bids comparable. Use when someone says "run the supplier escape chain," "a supplier caused this, find us an alternate," "supplier escape to alternate source," or asks to source around a supplier who caused a defect.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:supplier-escape-to-alternate-source` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 206 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when someone says "run the supplier escape chain," "a supplier caused this, find us an alternate," "supplier escape to alternate source," or asks to source around a supplier who caused a defect.

## What it says up front

> Chain 5. `ncr-writeup` → `root-cause-capa` → `supplier-quote-request`.

## How it is structured

The skill's own section headings, in order:

- Inputs
- The four steps
- Approval gates
- Three timestamps, not two
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:root-cause-capa](anthropics-claude-plugins-official-root-cause-capa.md) - Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timelin
- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his
- [anthropics/claude-plugins-official:supplier-quote-request](anthropics-claude-plugins-official-supplier-quote-request.md) - Builds the RFQ package that goes out to suppliers — drawing and specification at the verified current revision
- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:supplier-escape-to-alternate-source`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/supplier-escape-to-alternate-source --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 432f938012c929557c8464f14e7593140973006089de0b803a569ba9f2c940ef --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
