# agent-payment-x402

> Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. Supports Base through agentwallet-sdk, X Layer through OKX Payments / OKX Agent Payments Protocol, and Solana plus multi-network EVM through the upstream x402 packages with facilitator-based settlement. Use when an agent must pay for something itself and needs per-task budgets, spending controls, and a non-custodial wallet.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-payment-x402` |
| **Pack** | AI / ML Engineering (also: Finance & Accounting) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 593 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an agent must pay for something itself and needs per-task budgets, spending controls, and a non-custodial wallet.

## What it says up front

> Enable AI agents to make policy-gated payments with built-in spending controls. Uses the x402 HTTP payment protocol and MCP tools so agents can pay for external services, APIs, or other agents without custodial risk.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Decision Tree
- Supported Networks
- How It Works
  - x402 Protocol
  - Spending Controls
  - Non-Custodial Wallets
- MCP Integration
  - Option A: agentwallet-sdk (Base / multi-chain)
  - Available Tools (agent-callable)
  - Option B: OKX Agent Payments Protocol (X Layer)
  - Option C: Upstream x402 packages (Solana + Base/EVM)
- Examples
  - Budget enforcement in an MCP client
- Best Practices
- Production Reference

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:swift-protocol-di-testing](affaan-m-ecc-swift-protocol-di-testing.md) - Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs usi

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-payment-x402`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-payment-x402 --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 70993e334d3bb7629e875d08cad023abf9321c2f8d7cd6ffdb1b87e808a0d07d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
