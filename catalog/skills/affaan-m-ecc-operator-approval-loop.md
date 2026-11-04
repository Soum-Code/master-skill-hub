# operator-approval-loop

> Operator approval contract with internal filing notices for agent-drafted outbound messages, hashed drafts, epoch-keyed decisions, durable delivery claims and receipts, and a pre-draft baseline gate. Use when an agent drafts messages to external counterparties and a human operator must approve, reject, or steer each send before it leaves.

| | |
|---|---|
| **ID** | `affaan-m/ECC:operator-approval-loop` |
| **Pack** | Productivity & Automation (also: Communication & Collaboration, Legal & Compliance) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 239 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when an agent drafts messages to external counterparties and a human operator must approve, reject, or steer each send before it leaves.

## What it says up front

> An agent that talks to external counterparties should never send on its own judgment and should keep the operator informed internally. This skill defines the contract: every outbound draft is filed as an obligation, an operator decides on the exact text, and a delivery ledger proves what went out.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Objects
  - Filing a draft
  - Baseline gate
  - Deciding
  - Delivering
  - Time-boxed auto-approval (optional)
  - Signal linkage
- Examples
  - File a draft
  - Re-file after a steer
  - Gate refusal
  - Delivery footer in an internal channel
- Invariants to test

## What it bundles

- scripts: `references/approval_claims.py`
- reference docs: `references/approval-ledger.sql`, `references/approval_claims.py`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:counterparty-channel-discipline](affaan-m-ecc-counterparty-channel-discipline.md) - Per-channel strict prompts, mention gating, silent observation, and a communication autonomy policy for agents

## Invoke / install

- Invoke: `/affaan-m/ECC:operator-approval-loop`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/operator-approval-loop --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 43126800246ed3c9cbefa8d1b8912d973997ccbd4c5f851af7842875c6a3b5ac --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
