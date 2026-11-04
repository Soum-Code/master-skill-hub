# flox-environments

> Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based environment manager. Use when setting up project toolchains, installing system-level dependencies (compilers, databases, native libs), pinning exact package versions for a team, onboarding developers, running local services (PostgreSQL, Redis, Kafka), or solving 'works on my machine' problems — including agent/vibe-coding setups that need project-scoped tools without sudo. Also use when the user mentions .flox/, manifest.toml, flox activate, or FloxHub.

| | |
|---|---|
| **ID** | `affaan-m/ECC:flox-environments` |
| **Pack** | Spec-driven Dev Workflow (also: Claude / Skills / Plugin Tooling, Software Development, AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 496 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up project toolchains, installing system-level dependencies (compilers, databases, native libs), pinning exact package versions for a team, onboarding developers, running local services (PostgreSQL, Redis, Kafka), or solving 'works on my machi.

## What it says up front

> Flox creates reproducible development environments defined in a single TOML manifest. Every developer on the team gets identical packages, tools, and configuration — across macOS and Linux — without containers or VMs. Built on Nix with access to over 150,000 packages.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
- Essential Commands
- Manifest Structure
- Package Installation Patterns
  - Basic Installation
  - Version Pinning
  - Platform-Specific Packages
  - Resolving Package Conflicts
- Language-Specific Recipes
  - Python with uv
  - Node.js
  - Rust
  - Go
  - C/C++
- Hooks and Profile
  - Hooks — Non-Interactive Setup
  - Profile — Interactive Shell Configuration
- Anti-Patterns
  - Absolute Paths
  - Using exit in Hooks
  - Storing Secrets in Manifest
  - Slow Hooks Without Idempotency Guards
  - Putting User Commands in Hooks
- Full-Stack Example
- Environment Sharing
- AI-Assisted and Vibe Coding
- Debugging
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:vite-patterns](affaan-m-ecc-vite-patterns.md) - Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, depend

## Invoke / install

- Invoke: `/affaan-m/ECC:flox-environments`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/flox-environments --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3a26fe19828717b67022f40e6c9b501bab1bfeffdc5c3e59ebe81384419b3305 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
