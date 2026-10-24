# azure-eventhub-dotnet

> Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient, EventHubBufferedProducerClient), receiving events (EventProcessorClient with checkpointing), partition management, and real-time data ingestion. Triggers: "Event Hubs", "event streaming", "EventHubProducerClient", "EventProcessorClient", "send events", "receive events", "checkpointing", "partition".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-eventhub-dotnet` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 369 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for high-throughput event streaming: sending events (EventHubProducerClient, EventHubBufferedProducerClient), receiving events (EventProcessorClient with checkpointing), partition management, and real-time data ingestion.

## What it says up front

> High-throughput event streaming SDK for sending and receiving events via Azure Event Hubs.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
- Client Types
- Core Workflow
  - 1. Send Events (Batch)
  - 2. Send Events (Buffered - High Volume)
  - 3. Receive Events (Production - EventProcessorClient)
  - 4. Partition Operations
- EventPosition Options
- ASP.NET Core Integration
- Best Practices
- Error Handling
- Checkpointing Strategies
- Related SDKs

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-ai-voicelive-dotnet](microsoft-skills-azure-ai-voicelive-dotnet.md) - Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communica
- [microsoft/skills:azure-eventgrid-dotnet](microsoft-skills-azure-eventgrid-dotnet.md) - Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use f
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-maps-search-dotnet](microsoft-skills-azure-maps-search-dotnet.md) - Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and wea

## Invoke / install

- Invoke: `/microsoft/skills:azure-eventhub-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-eventhub-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 27346dafbeea4385a168a9d1a0349393e727eeed7f6d1fb24f674879f45e12c6 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
