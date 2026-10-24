# azure-eventgrid-dotnet

> Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and EventGridEvents. Triggers: "Event Grid", "EventGridPublisherClient", "CloudEvent", "EventGridEvent", "publish events .NET", "event-driven", "pub/sub".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-eventgrid-dotnet` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 498 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for event-driven architectures, pub/sub messaging, CloudEvents, and EventGridEvents.

## What it says up front

> Client library for publishing events to Azure Event Grid topics, domains, and namespaces.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Client Hierarchy
- Authentication
  - API Key Authentication
  - Microsoft Entra Token Credential
  - SAS Token Authentication
- Publishing Events
  - EventGridEvent Schema
  - CloudEvent Schema
  - Publishing to Event Grid Domain
  - Custom Serialization
- Pull Delivery (Namespaces)
  - Send Events to Namespace Topic
  - Receive and Process Events
  - Reject Events (Dead Letter)
- Consuming Events (Azure Functions)
  - EventGridEvent Trigger
  - CloudEvent Trigger
- Parsing Events
  - Parse EventGridEvent
  - Parse CloudEvent
- System Events
- Key Types Reference
- Event Schemas Comparison
- Best Practices
- Error Handling
- Failover Pattern
- Related SDKs
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo
- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,

## Invoke / install

- Invoke: `/microsoft/skills:azure-eventgrid-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-eventgrid-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 4ed67a7d7854f0ecacf30e95bf859fc73d7f3754dec66a666975c69772786423 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
