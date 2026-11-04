# ito-baskets

> Read-only Itô basket and prediction-market data skill. Index the live basket catalog, compare a basket against user-supplied research or a watchlist, build a source-grounded market brief, or draft a non-executable planning worksheet. Use when a user asks to browse or index Itô baskets, compare a basket against notes or a thesis, research prediction-market events/venues/liquidity, or plan a basket or market idea without trading. Never advises, orders, trades, reserves, or executes.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ito-baskets` |
| **Pack** | Spec-driven Dev Workflow (also: Product Management, Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 264 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when a user asks to browse or index Itô baskets, compare a basket against notes or a thesis, research prediction-market events/venues/liquidity, or plan a basket or market idea without trading.

## What it says up front

> One read-only skill for every Itô basket/market data workflow. It replaces the former `ito-basket-compare`, `ito-market-intelligence`, `ito-data-atlas-agent`, and `ito-trade-planner` skills; requests naming those route here.

## How it is structured

The skill's own section headings, in order:

- Non-negotiable boundaries
- Access surfaces
- Bundled read-only client
- Mode workflows
  - Index
  - Compare
  - Brief
  - Worksheet
- Provenance contract
- Recovery and safe failure
- Output contracts
- Useful skill chains

## What it bundles

- scripts: `scripts/ito-baskets.js`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:prediction-market-risk-review](affaan-m-ecc-prediction-market-risk-review.md) - Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, pr
- [affaan-m/ECC:prediction-market-oracle-research](affaan-m-ecc-prediction-market-oracle-research.md) - Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate 

## Invoke / install

- Invoke: `/affaan-m/ECC:ito-baskets`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ito-baskets --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b9f7be0750352d9f742b22a275b41d2e843b380c45d35b03943010e95830227e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
