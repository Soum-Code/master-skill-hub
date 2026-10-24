# azure-identity-dotnet

> Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and developer credentials. Triggers: "Azure Identity", "DefaultAzureCredential", "ManagedIdentityCredential", "ClientSecretCredential", "authentication .NET", "Azure auth", "credential chain".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-identity-dotnet` |
| **Pack** | MLOps / DevOps / Cloud (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 337 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for DefaultAzureCredential, managed identity, service principals, and developer credentials.

## What it says up front

> Authentication library for Azure SDK clients using Microsoft Entra ID.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
  - Service Principal with Secret
  - Service Principal with Certificate
  - Managed Identity
- DefaultAzureCredential
  - Basic Usage
  - ASP.NET Core with Dependency Injection
  - Customizing DefaultAzureCredential
- Credential Types
  - ManagedIdentityCredential (Production)
  - ClientSecretCredential
  - ClientCertificateCredential
  - ChainedTokenCredential (Custom Chain)
  - Developer Credentials
- Environment-Based Configuration
- Sovereign Clouds
- Credential Types Reference
- Best Practices
  - 1. Use Deterministic Credentials in Production
  - 2. Reuse Credential Instances
  - 3. Configure Retry Policies
  - 4. Enable Logging for Debugging
- Error Handling
- Key Exceptions
- Managed Identity Support
- Thread Safety
- Related packages
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-eventgrid-dotnet](microsoft-skills-azure-eventgrid-dotnet.md) - Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use f
- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-mgmt-apimanagement-dotnet](microsoft-skills-azure-mgmt-apimanagement-dotnet.md) - Azure Resource Manager SDK for API Management in .NET. Use for MANAGEMENT PLANE operations: creating/managing 
- [microsoft/skills:azure-maps-search-dotnet](microsoft-skills-azure-maps-search-dotnet.md) - Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and wea

## Invoke / install

- Invoke: `/microsoft/skills:azure-identity-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-identity-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 7fe9831bd2e9c045192a6db26aba11bbd66fc0872ef834808f0903d4c9dd6b86 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
