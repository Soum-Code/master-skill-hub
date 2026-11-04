# agent-security-hardening

> Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write workspace files, manage runtime identifiers, or handle credentials. Use when building or reviewing an agent runtime, autonomous worker, tool gateway, memory service, or multi-tenant agent deployment. Do not use for general web application security or offensive testing.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-security-hardening` |
| **Pack** | Security & Privacy (also: AI / ML Engineering, Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 178 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building or reviewing an agent runtime, autonomous worker, tool gateway, memory service, or multi-tenant agent deployment.
- Do not use for general web application security or offensive testing.

## What it says up front

> Harden the boundaries where an agent turns untrusted data into filesystem, network, memory, or tool actions. Produce concrete controls and tests for the framework being reviewed; a checklist without enforcement evidence is incomplete.

## How it is structured

The skill's own section headings, in order:

- Important
- When to Activate
- Hardening Workflow
  - 1. Map Trust Boundaries
  - 2. Validate Identifiers, Environment Values, and URLs
  - 3. Contain Filesystem Access
  - 4. Protect Temporary Data and Credentials
  - 5. Bound and Sanitize Tool Output
- Verification Gate
- Common Issues
  - Validation exists only in the prompt
  - A normalized path still escapes
  - Redaction happens after logging
- When NOT to Use
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:aspnet-core](openai-skills-aspnet-core.md) - Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET w
- [affaan-m/ECC:docker-patterns](affaan-m-ecc-docker-patterns.md) - Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security
- [example-skills:web-artifacts-builder](example-skills-web-artifacts-builder.md) - Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web tech
- [affaan-m/ECC:agent-runtime-gateway-smoke-test](affaan-m-ecc-agent-runtime-gateway-smoke-test.md) - Verify a local agent API, temporary gateway tunnel, and remote sandbox callback with a tool-free task, then re

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-security-hardening`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-security-hardening --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 257b725180739ca5fc6ab837a0111852c6d9ac56889b6a916d9f1fa3d44c9544 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
