# nodejs-keccak256

> Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently breaks selectors, signatures, storage slots, and address derivation. Use when hashing for Ethereum in JavaScript or TypeScript, or when a selector, signature, storage slot, or derived address is wrong.

| | |
|---|---|
| **ID** | `affaan-m/ECC:nodejs-keccak256` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 104 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when hashing for Ethereum in JavaScript or TypeScript, or when a selector, signature, storage slot, or derived address is wrong.

## What it says up front

> Ethereum uses Keccak-256, not the NIST-standardized SHA3 variant exposed by Node's `crypto.createHash('sha3-256')`.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Examples
  - ethers v6
  - viem
  - web3.js
  - Common patterns
  - Address from public key
  - Audit your codebase
- Rule

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:nodejs-keccak256`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/nodejs-keccak256 --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree fd08932b881438dd0c7980326740dbd8bdf1dfe04a650f378982767393156f02 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
