# llm-trading-agent-security

> Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit breakers, MEV protection, and key handling. Use when an autonomous agent holds wallet or transaction authority and its limits, simulation, or key handling need review.

| | |
|---|---|
| **ID** | `affaan-m/ECC:llm-trading-agent-security` |
| **Pack** | AI / ML Engineering (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 148 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an autonomous agent holds wallet or transaction authority and its limits, simulation, or key handling need review.

## What it says up front

> Autonomous trading agents have a harsher threat model than normal LLM apps: an injection or bad tool path can turn directly into asset loss.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Examples
  - Treat prompt injection as a financial attack
  - Hard spend limits
  - Simulate before sending
  - Circuit breaker
  - Wallet isolation
  - MEV and deadline protection
- Pre-Deploy Checklist

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-security](affaan-m-ecc-django-security.md) - Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS 
- [affaan-m/ECC:error-handling](affaan-m-ecc-error-handling.md) - Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, r
- [affaan-m/ECC:cost-aware-llm-pipeline](affaan-m-ecc-cost-aware-llm-pipeline.md) - Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic,

## Invoke / install

- Invoke: `/affaan-m/ECC:llm-trading-agent-security`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/llm-trading-agent-security --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 710241d31682f59b1efd909b4f6ffe652ae82e52c72fc8d2a9377d1e70f166c3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
