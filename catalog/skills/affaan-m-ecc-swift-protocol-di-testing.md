# swift-protocol-di-testing

> Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protocols and Swift Testing. Use when Swift code needs testing and file system, network, or external APIs must be mocked.

| | |
|---|---|
| **ID** | `affaan-m/ECC:swift-protocol-di-testing` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 192 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when Swift code needs testing and file system, network, or external APIs must be mocked.

## What it says up front

> Patterns for making Swift code testable by abstracting external dependencies (file system, network, iCloud) behind small, focused protocols. Enables deterministic tests without I/O.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Pattern
  - 1. Define Small, Focused Protocols
  - 2. Create Default (Production) Implementations
  - 3. Create Mock Implementations for Testing
  - 4. Inject Dependencies with Default Parameters
  - 5. Write Tests with Swift Testing
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:agentic-os](affaan-m-ecc-agentic-os.md) - Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, 
- [engineering:system-design](engineering-system-design.md) - Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "s
- [openai/skills:aspnet-core](openai-skills-aspnet-core.md) - Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET w
- [affaan-m/ECC:rust-testing](affaan-m-ecc-rust-testing.md) - Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking,

## Invoke / install

- Invoke: `/affaan-m/ECC:swift-protocol-di-testing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/swift-protocol-di-testing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c20e17c63280f32fa4768417b58155e54678976ba202fdb66bca1f0364e959a7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
