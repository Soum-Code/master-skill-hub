# azure-mgmt-apimanagement-dotnet

> Azure Resource Manager SDK for API Management in .NET. Use for MANAGEMENT PLANE operations: creating/managing APIM services, APIs, products, subscriptions, policies, users, groups, gateways, and backends via Azure Resource Manager. Triggers: "API Management", "APIM service", "create APIM", "manage APIs", "ApiManagementServiceResource", "API policies", "APIM products", "APIM subscriptions".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-mgmt-apimanagement-dotnet` |
| **Pack** | MLOps / DevOps / Cloud (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 320 lines in SKILL.md, 4 file(s) |

## When to use it

- Use for MANAGEMENT PLANE operations: creating/managing APIM services, APIs, products, subscriptions, policies, users, groups, gateways, and backends via Azure Resource Manager.

## What it says up front

> Management plane SDK for provisioning and managing Azure API Management resources via Azure Resource Manager.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
- Resource Hierarchy
- Core Workflow
  - 1. Create API Management Service
  - 2. Create an API
  - 3. Create a Product
  - 4. Create a Subscription
  - 5. Set API Policy
  - 6. Backup and Restore
- Key Types Reference
- SKU Types
- Best Practices
- Error Handling
- Reference Files
- Related Resources

## What it bundles

- reference docs: `references/apis-operations.md`, `references/products-subscriptions.md`, `references/service-management.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-mgmt-apicenter-dotnet](microsoft-skills-azure-mgmt-apicenter-dotnet.md) - Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery
- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient
- [microsoft/skills:azure-maps-search-dotnet](microsoft-skills-azure-maps-search-dotnet.md) - Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and wea

## Invoke / install

- Invoke: `/microsoft/skills:azure-mgmt-apimanagement-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-mgmt-apimanagement-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 808a371731a3bf90670a34e1d679b18604b3e00e59a3c04355dcfb4014012224 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
