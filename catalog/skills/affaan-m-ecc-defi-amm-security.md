# defi-amm-security

> Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipulation, slippage, admin controls, and integer math. Use when auditing or writing Solidity AMM, liquidity pool, or swap code.

| | |
|---|---|
| **ID** | `affaan-m/ECC:defi-amm-security` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 168 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when auditing or writing Solidity AMM, liquidity pool, or swap code.

## What it says up front

> Critical vulnerability patterns and hardened implementations for Solidity AMM contracts, LP vaults, and swap functions.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Execution Safety
- Examples
  - Reentrancy: enforce CEI order
  - Donation or inflation attacks
  - Oracle manipulation
  - Slippage protection
  - Safe reserve math
  - Admin controls
- Security Checklist
- Audit Tools

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:defi-amm-security`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/defi-amm-security --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a793f2633e08eea6be7488e34481a491a02029d5955add25e331bcfabecd0ff9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
