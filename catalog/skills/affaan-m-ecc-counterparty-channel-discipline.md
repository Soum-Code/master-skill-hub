# counterparty-channel-discipline

> Per-channel strict prompts, mention gating, silent observation, and a communication autonomy policy for agents that sit in shared channels with external counterparties. Use when an agent joins group chats, shared channels, or DMs where outsiders can read every message and you need it to speak only when addressed, never leak internal context, and route risky content to draft-only approval.

| | |
|---|---|
| **ID** | `affaan-m/ECC:counterparty-channel-discipline` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 171 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when an agent joins group chats, shared channels, or DMs where outsiders can read every message and you need it to speak only when addressed, never leak internal context, and route risky content to draft-only approval.

## What it says up front

> Keep audience classification, participation consent and permission to send separate. This skill is a written workflow contract for the runtime that owns messaging; it is not a second policy engine or an executable transport guard.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Trusted destination and audience
  - Participation before work
  - Output and delivery boundary
  - Strict prompt and example policy
  - Communication autonomy and leakage
- Examples
  - Human-addressed group message
  - Explicit agent request, verified business answer
  - Missing attachment capability
- Invariants to test

## What it bundles

- reference docs: `references/channel-policy.example.yaml`, `references/strict-prompt.template.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:operator-approval-loop](affaan-m-ecc-operator-approval-loop.md) - Operator approval contract with internal filing notices for agent-drafted outbound messages, hashed drafts, ep
- [affaan-m/ECC:prompt-optimizer](affaan-m-ecc-prompt-optimizer.md) - Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a

## Invoke / install

- Invoke: `/affaan-m/ECC:counterparty-channel-discipline`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/counterparty-channel-discipline --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5d230fac81056a36e33e17a8aadf589607b5d19811b559d1a5cb59189930bff6 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
