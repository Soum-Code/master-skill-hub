# connections-optimizer

> Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's real voice. Use when the user wants to clean up following lists, grow toward current priorities, or rebalance a social graph around higher-signal relationships.

| | |
|---|---|
| **ID** | `affaan-m/ECC:connections-optimizer` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 191 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to clean up following lists, grow toward current priorities, or rebalance a social graph around higher-signal relationships.

## What it says up front

> Reorganize the user's network instead of treating outbound as a one-way prospecting list.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Required Inputs
- Tool Requirements
  - Preferred
  - Fallbacks
- Safety Defaults
- Platform Rules
  - X
  - LinkedIn
- Modes
  - `light-pass`
  - `default`
  - `aggressive`
- Scoring Model
- Workflow
- Review Pack Format
- Outbound Rules
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:social-graph-ranker](affaan-m-ecc-social-graph-ranker.md) - Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and 
- [affaan-m/ECC:lead-intelligence](affaan-m-ecc-lead-intelligence.md) - AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered sign
- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use
- [affaan-m/ECC:investor-outreach](affaan-m-ecc-investor-outreach.md) - Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. 

## Invoke / install

- Invoke: `/affaan-m/ECC:connections-optimizer`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/connections-optimizer --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1e3f3bea052e9939989afeec1ee8286377012277b60ace4a1b2b483c6ec6ebd0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
