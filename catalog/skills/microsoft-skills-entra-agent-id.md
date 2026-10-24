# entra-agent-id

> Microsoft Entra Agent ID (preview) for creating OAuth2-capable AI agent identities via Microsoft Graph beta API. Covers Agent Identity Blueprints, BlueprintPrincipals, Agent Identities, required permissions, sponsors, and Workload Identity Federation. Includes Microsoft Entra SDK for AgentID (containerized sidecar) for polyglot agent authentication (Docker/Kubernetes), 3P agent integration, autonomous and interactive agent patterns. Triggers: "agent identity", "agent id", "Agent Identity Blueprint", "BlueprintPrincipal", "entra agent", "agent identity provisioning", "Graph agent identity", "entra sidecar", "agent id sidecar", "auth sidecar", "3P agent", "third-party agent identity", "polyglot agent auth".

| | |
|---|---|
| **ID** | `microsoft/skills:entra-agent-id` |
| **Pack** | AI / ML Engineering (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 251 lines in SKILL.md, 4 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create and manage OAuth2-capable identities for AI agents using Microsoft Graph beta API.

## How it is structured

The skill's own section headings, in order:

- Before You Start
- Conceptual Model
- Prerequisites
  - PowerShell (recommended for interactive setup)
  - Python (for programmatic provisioning)
  - Required Entra Roles
- Environment Variables
- Authentication
  - PowerShell (delegated permissions)
  - Python (application permissions)
- Core Workflow
  - Step 1: Create Agent Identity Blueprint
  - Step 2: Create BlueprintPrincipal
  - Step 3: Create Agent Identities
- API Reference
- Required Permissions
- Cleanup
- Best Practices
- References
  - External Links

## What it bundles

- reference docs: `references/known-limitations.md`, `references/oauth2-token-flow.md`, `references/sdk-sidecar.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo

## Invoke / install

- Invoke: `/microsoft/skills:entra-agent-id`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/entra-agent-id --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 7b7537021b1040a68616a9bb70b0c4327b854e4a9f4807dbc08cab91ff1c45e5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
