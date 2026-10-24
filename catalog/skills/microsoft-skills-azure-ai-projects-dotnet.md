# azure-ai-projects-dotnet

> Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes. Use for AI Foundry project management, versioned agents, and orchestration. Triggers: "AI Projects", "AIProjectClient", "Foundry project", "versioned agents", "evaluations", "datasets", "connections", "deployments .NET".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-ai-projects-dotnet` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 361 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for AI Foundry project management, versioned agents, and orchestration.

## What it says up front

> High-level SDK for Azure AI Foundry project operations including agents, connections, datasets, deployments, evaluations, and indexes.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
- Client Hierarchy
- Core Workflows
  - 1. Get Persistent Agents Client
  - 2. Versioned Agents with Tools (Preview)
  - 3. Connections
  - 4. Deployments
  - 5. Datasets
  - 6. Indexes
  - 7. Evaluations
  - 8. Get Azure OpenAI Chat Client
- Available Agent Tools
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

- [microsoft/skills:azure-ai-agents-persistent-dotnet](microsoft-skills-azure-ai-agents-persistent-dotnet.md) - Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messa
- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-mgmt-apicenter-dotnet](microsoft-skills-azure-mgmt-apicenter-dotnet.md) - Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient

## Invoke / install

- Invoke: `/microsoft/skills:azure-ai-projects-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-ai-projects-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 733452c23130883cf605c04a69380ec01b4df150907669af9b00f2c0c46b7268 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
