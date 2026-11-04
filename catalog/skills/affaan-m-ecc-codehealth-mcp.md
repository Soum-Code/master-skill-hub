# codehealth-mcp

> Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and PRs. Use when reviewing code quality, refactoring, checking if AI changes degraded a file, or before commit/PR.

| | |
|---|---|
| **ID** | `affaan-m/ECC:codehealth-mcp` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 168 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing code quality, refactoring, checking if AI changes degraded a file, or before commit/PR.

## What it says up front

> Structural maintainability feedback for AI-assisted coding. Complements style/lint skills (`coding-standards`, `plankton-code-quality`) with **design-level** health scores and regression gates.

## How it is structured

The skill's own section headings, in order:

- Security and boundaries
- When to Use
- When to Activate
- How It Works
  - 1. Connect the MCP server
  - 2. Call standalone tools only
  - 3. Interpret scores (1–10)
  - 4. Run the feedback loop
- Examples
  - Example: Flask maintainability improvement
  - Example: AGENTS.md enforcement block
  - Example: anti-patterns vs correct loop
- Pairing with ECC
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:plankton-code-quality](affaan-m-ecc-plankton-code-quality.md) - Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on eve
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 

## Invoke / install

- Invoke: `/affaan-m/ECC:codehealth-mcp`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/codehealth-mcp --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 10203d3829c0911c40e34113f5cff310cab006172c286ff03a5383b978127168 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
