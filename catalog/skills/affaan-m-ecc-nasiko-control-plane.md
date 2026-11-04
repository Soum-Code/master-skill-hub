# nasiko-control-plane

> Manage the experimental Nasiko CLI lifecycle through ECC — read-only status checks, consent-gated install of the pinned qualified version with dry-run preview, and ownership-checked uninstall, under explicit telemetry and secrets boundaries. Use when the user asks to install, inspect, or remove the Nasiko CLI or check whether it is present.

| | |
|---|---|
| **ID** | `affaan-m/ECC:nasiko-control-plane` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 50 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when the user asks to install, inspect, or remove the Nasiko CLI or check whether it is present.

## What it says up front

> Use this skill when a user explicitly asks ECC to install, inspect, or remove the qualified Nasiko CLI. This skill does not operate a Nasiko control plane.

## How it is structured

The skill's own section headings, in order:

- Safety contract
- Lifecycle boundary
- Failure behavior

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ito-compute](affaan-m-ecc-ito-compute.md) - Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revok
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [affaan-m/ECC:messages-ops](affaan-m-ecc-messages-ops.md) - Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 

## Invoke / install

- Invoke: `/affaan-m/ECC:nasiko-control-plane`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/nasiko-control-plane --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5e410536a91172e19aff4935f728f98e479ecb216d1be40383dc548bf290b369 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
