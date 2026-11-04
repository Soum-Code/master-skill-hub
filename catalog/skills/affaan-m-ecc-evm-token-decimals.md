# evm-token-decimals

> Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normalization for bots, dashboards, and DeFi tools. Use when handling token amounts across EVM chains, or when a balance, price, or transfer amount is off by orders of magnitude.

| | |
|---|---|
| **ID** | `affaan-m/ECC:evm-token-decimals` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 132 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when handling token amounts across EVM chains, or when a balance, price, or transfer amount is off by orders of magnitude.

## What it says up front

> Silent decimal mismatches are one of the easiest ways to ship balances or USD values that are off by orders of magnitude without throwing an error.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Examples
  - Query decimals at runtime
  - Cache by chain and token
  - Handle odd tokens defensively
  - Normalize to 18-decimal WAD in Solidity
  - TypeScript with ethers
  - Quick on-chain check
- Rules

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:evm-token-decimals`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/evm-token-decimals --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 663daddf19b10dafd03b74e47f19b6d2ea38702042139f7a1d5229fc2b2561c9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
