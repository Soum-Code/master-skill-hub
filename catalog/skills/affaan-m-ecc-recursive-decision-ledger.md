# recursive-decision-ledger

> Run repeated rollouts ("Prime Gauss" style recursive prompting) while keeping an append-only decision ledger of trials, marks, coherence checks, and promotion gates, so recursive confidence never auto-approves live trading, deploy, or destructive actions. Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble comparison, or recursive reasoning with a visible evidence trail.

| | |
|---|---|
| **ID** | `affaan-m/ECC:recursive-decision-ledger` |
| **Pack** | Finance & Accounting |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 82 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user asks for repeated rollouts, marked decision processes, high-dimensional search, stochastic optimization, local-optima exploration, ensemble comparison, or recursive reasoning with a visible evidence trail.

## What it says up front

> Use this skill when the user is trying to force deeper computation through repeated rollouts or "Prime Gauss" style recursive prompting. Preserve the useful part: repeated trials, prior memory, fresh information, and explicit marks. Remove the unsafe part: pretending the loop proves certainty.

## How it is structured

The skill's own section headings, in order:

- Ledger Contract
- Rollout Loop
- Coherence Mark
- Promotion Rules
- Summary Shape

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:recursive-decision-ledger`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/recursive-decision-ledger --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c7511802dadad684b066e6db39f271beecf4707985606906e713dbd1881551db --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
