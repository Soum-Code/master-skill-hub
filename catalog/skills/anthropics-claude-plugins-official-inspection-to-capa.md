# inspection-to-capa

> Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches history at the moment of writing to say whether this has happened before and whether the last fix held, reads sensor and inspection data on one verified timeline, proposes ranked candidate causes with evidence for and against, drafts the 8D, and produces the customer pack behind a redaction diff. Use when someone says "run the CAPA chain," "take this nonconformance through to an 8D," "inspection to CAPA," or asks for the full corrective-action workflow.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:inspection-to-capa` |
| **Pack** | Security & Privacy (also: Documents, Writing & Content, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 194 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when someone says "run the CAPA chain," "take this nonconformance through to an 8D," "inspection to CAPA," or asks for the full corrective-action workflow.

## What it says up front

> Chain 2. `ncr-writeup` → `root-cause-capa`.

## How it is structured

The skill's own section headings, in order:

- Inputs
- The seven steps
- Approval gates
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
- [anthropics/claude-plugins-official:ncr-writeup](anthropics-claude-plugins-official-ncr-writeup.md) - Writes the nonconformance report: what was found and measured, the specific requirement it violates cited to i
- [anthropics/claude-plugins-official:supplier-escape-to-alternate-source](anthropics-claude-plugins-official-supplier-escape-to-alternate-source.md) - Runs the cross-area chain from a nonconformance traced to purchased material through to an alternate-source RF
- [anthropics/claude-plugins-official:rfq-to-quote](anthropics-claude-plugins-official-rfq-to-quote.md) - Runs the whole RFQ-to-quote chain end to end: reads the inquiry and its drawings, checks it against what the p

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:inspection-to-capa`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/inspection-to-capa --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree f7abf06c3b1cb2110e5f1fdeab1538b3f79d5486be04c558660e246464abe36e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
