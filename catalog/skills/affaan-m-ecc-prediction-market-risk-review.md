# prediction-market-risk-review

> Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, privacy, and execution risk. Use before any workflow handles venue auth, user portfolio data, API keys, or trade planning.

| | |
|---|---|
| **ID** | `affaan-m/ECC:prediction-market-risk-review` |
| **Pack** | Legal & Compliance (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 62 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Use this skill before a prediction-market workflow touches user financial context, venue authentication, portfolio data, automation, or execution-capable tools.

## How it is structured

The skill's own section headings, in order:

- Review Gates
  - Advice Boundary
  - Venue And Regulatory Boundary
  - Data Quality
  - Security
  - Privacy
- Output Contract

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ito-baskets](affaan-m-ecc-ito-baskets.md) - Read-only Itô basket and prediction-market data skill. Index the live basket catalog, compare a basket against
- [legal:compliance-check](legal-compliance-check.md) - Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable reg
- [affaan-m/ECC:prediction-market-oracle-research](affaan-m-ecc-prediction-market-oracle-research.md) - Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate 
- [affaan-m/ECC:laravel-security](affaan-m-ecc-laravel-security.md) - Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API se

## Invoke / install

- Invoke: `/affaan-m/ECC:prediction-market-risk-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/prediction-market-risk-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b53b3e6656c7ebb8e26e49d5189c35c907e5152cd558f4eaaa5452a04e591211 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
