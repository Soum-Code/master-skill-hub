# tinystruct-patterns

> Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase or any project built on tinystruct — including generating the bin/dispatcher and bin/dispatcher.cmd launcher scripts when a project lacks them, creating Application classes, @Action-mapped routes, unit tests, ActionRegistry, HTTP/CLI dual-mode handling, the built-in HTTP server, the event system, JSON with Builder/Builders, database persistence with AbstractData, POJO generation, Server-Sent Events (SSE), file uploads, and outbound HTTP networking.

| | |
|---|---|
| **ID** | `affaan-m/ECC:tinystruct-patterns` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 451 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when working on the tinystruct codebase or any project built on tinystruct — including generating the bin/dispatcher and bin/dispatcher.cmd launcher scripts when a project lacks them, creating Application classes, @Action-mapped routes, unit tests, ActionR.

## What it says up front

> Architecture and implementation patterns for building modules with the **tinystruct** Java framework – a lightweight, high-performance framework that treats CLI and HTTP as equal citizens, requiring no `main()` method and minimal configuration.

## How it is structured

The skill's own section headings, in order:

- Core Principle
- Primary Development Tool: `bin/dispatcher`
  - Generating `bin/dispatcher` and `bin/dispatcher.cmd`
- When to Activate
  - When to Use
- How It Works
- Examples
  - Basic Application (MyService)
  - HTTP Mode Disambiguation (login)
  - Native JSON Data Handling (Builder + Builders)
  - SSE (Server-Sent Events)
  - File Upload
  - Database Metadata Operations
- MCP Server and Tools Integration
  - Overloaded Tool Methods
- Configuration
- Logging and Diagnostics
- Static Files
- Red Flags & Anti-patterns
- Best Practices
- Technical Reference
- Reference Source Files (Internal)

## What it bundles

- reference docs: `references/architecture.md`, `references/data-handling.md`, `references/database.md`, `references/routing.md`, `references/system-usage.md`, `references/testing.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:tinystruct-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/tinystruct-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1d5ea87a2c76eaa3f2a0cacca1bbfb1ca75686627b9fc99b4b6a8d5f4ea05d5d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
