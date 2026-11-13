# root-cause-capa

> Reads sensor history, inspection measurements, maintenance records and prior tickets onto one verified timeline, runs the pattern checks in code rather than by eye — SPC drift, clustering by lot, shift, operator, machine and tool change, correlation with a maintenance event — then proposes ranked candidate causal chains, each with the evidence for it, the evidence against it, and the test that would confirm or kill it. Drafts the 8D. Where the leading candidate points at purchased material, raises the supplier-caused flag that starts a sourcing action. Use when someone says "why did this happen," "root cause," "write the 8D," "investigate this nonconformance," "CAPA," or "the customer wants a corrective action report."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:root-cause-capa` |
| **Pack** | Careers, Jobs & Hiring (also: MLOps / DevOps / Cloud, Documents, Writing & Content, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 406 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when someone says "why did this happen," "root cause," "write the 8D," "investigate this nonconformance," "CAPA," or "the customer wants a corrective action report.".

## What it says up front

> The step between "we found a bad part" and "we fixed the reason." It is slow, expert work, and the reason it is slow is that the evidence sits in four systems that nobody looks at together.

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Assemble the evidence window, and verify the clocks
  - Step 2 — Run the pattern checks, computed
  - Step 3 — Build candidate causal chains
  - Step 4 — Rank, and name the discriminating tests
  - Step 5 — Draft the 8D
  - Step 6 — Route the signal
  - Step 7 — Produce the customer-facing pack
  - Step 8 — Update the register row, and the Quality Register
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/8d-and-candidates.md`, `reference/pattern-checks.md`, `reference/redaction.md`, `reference/time-alignment.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:inspection-to-capa](anthropics-claude-plugins-official-inspection-to-capa.md) - Runs the quality chain end to end: writes the nonconformance against the requirement it violates, searches his
- [anthropics/claude-plugins-official:supplier-escape-to-alternate-source](anthropics-claude-plugins-official-supplier-escape-to-alternate-source.md) - Runs the cross-area chain from a nonconformance traced to purchased material through to an alternate-source RF
- [anthropics/claude-plugins-official:breakdown-diagnosis](anthropics-claude-plugins-official-breakdown-diagnosis.md) - When a machine goes down, reads the sensor window before the failure, the asset's maintenance history includin
- [anthropics/claude-plugins-official:breakdown-to-next-report](anthropics-claude-plugins-official-breakdown-to-next-report.md) - Runs the chain from a machine going down to the diagnosis landing in tomorrow's production report: reads the s

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:root-cause-capa`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/root-cause-capa --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree 73cc288c68a7e423b1719e68a2148781a245abcffd58ee9d305d694ea19c8738 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
