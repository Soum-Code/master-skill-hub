# azure-mgmt-apicenter-dotnet

> Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. Use for creating API services, workspaces, APIs, versions, definitions, environments, deployments, and metadata schemas. Triggers: "API Center", "ApiCenterService", "ApiCenterWorkspace", "ApiCenterApi", "API inventory", "API governance", "API versioning", "API catalog", "API discovery".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-mgmt-apicenter-dotnet` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 424 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for creating API services, workspaces, APIs, versions, definitions, environments, deployments, and metadata schemas.

## What it says up front

> Centralized API inventory and governance SDK for managing APIs across your organization.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
- Resource Hierarchy
- Core Workflows
  - 1. Create API Center Service
  - 2. Create Workspace
  - 3. Create API
  - 4. Create API Version
  - 5. Create API Definition (Upload OpenAPI Spec)
  - 6. Export API Specification
  - 7. Create Environment
  - 8. Create Deployment
  - 9. Create Metadata Schema
  - 10. List and Search APIs
- Key Types Reference
- Best Practices
- Error Handling
- Related SDKs
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-mgmt-apimanagement-dotnet](microsoft-skills-azure-mgmt-apimanagement-dotnet.md) - Azure Resource Manager SDK for API Management in .NET. Use for MANAGEMENT PLANE operations: creating/managing 
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient

## Invoke / install

- Invoke: `/microsoft/skills:azure-mgmt-apicenter-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-mgmt-apicenter-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 653b9f0d58d7e9e68b7a43356cf7814ead3a47ddce230cde2864abe6e54ba914 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
