# error-handling

> Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, retries, circuit breakers, and user-facing error messages. Use when designing error types, retries, circuit breakers, or user-facing failure messages in TypeScript, Python, or Go.

| | |
|---|---|
| **ID** | `affaan-m/ECC:error-handling` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 378 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when designing error types, retries, circuit breakers, or user-facing failure messages in TypeScript, Python, or Go.

## What it says up front

> Consistent, robust error handling patterns for production applications.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
- TypeScript / JavaScript
  - Typed Error Classes
  - Result Pattern (no-throw style)
  - API Error Handler (Next.js / Express)
  - React Error Boundary
- Python
  - Custom Exception Hierarchy
  - FastAPI Global Exception Handler
- Go
  - Sentinel Errors and Error Wrapping
- Retry with Exponential Backoff
- User-Facing Error Messages
- Error Handling Checklist

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:typescript-patterns](affaan-m-ecc-typescript-patterns.md) - TypeScript patterns for strict, type-safe, maintainable code in modern TypeScript and JavaScript applications.
- [affaan-m/ECC:hexagonal-architecture](affaan-m-ecc-hexagonal-architecture.md) - Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, a
- [affaan-m/ECC:llm-trading-agent-security](affaan-m-ecc-llm-trading-agent-security.md) - Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection,
- [affaan-m/ECC:python-patterns](affaan-m-ecc-python-patterns.md) - Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina

## Invoke / install

- Invoke: `/affaan-m/ECC:error-handling`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/error-handling --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6923310a6acadda3eca6c2c5e33d1d9eba80250ccfc48dd88b94a7d6c0d2188a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
