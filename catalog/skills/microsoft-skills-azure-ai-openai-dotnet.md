# azure-ai-openai-dotnet

> Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants. Triggers: "Azure OpenAI", "AzureOpenAIClient", "ChatClient", "chat completions .NET", "GPT-4", "embeddings", "DALL-E", "Whisper", "OpenAI .NET".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-ai-openai-dotnet` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 468 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for chat completions, embeddings, image generation, audio transcription, and assistants.

## What it says up front

> Client library for Azure OpenAI Service providing access to OpenAI models including GPT-4, GPT-4o, embeddings, DALL-E, and Whisper.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Client Hierarchy
- Authentication
  - API Key Authentication
  - Microsoft Entra Token Credential
  - Using OpenAI SDK Directly with Azure
- Chat Completions
  - Basic Chat
  - Async Chat
  - Streaming Chat
  - Chat with Options
  - Multi-turn Conversation
- Structured Outputs (JSON Schema)
- Reasoning Models (o1, o4-mini)
- Azure AI Search Integration (RAG)
- Embeddings
  - Batch Embeddings
- Image Generation (DALL-E)
- Audio (Whisper)
  - Transcription
  - Text-to-Speech
- Function Calling (Tools)
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

- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-ai-voicelive-dotnet](microsoft-skills-azure-ai-voicelive-dotnet.md) - Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communica
- [microsoft/skills:azure-eventgrid-dotnet](microsoft-skills-azure-eventgrid-dotnet.md) - Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use f

## Invoke / install

- Invoke: `/microsoft/skills:azure-ai-openai-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-ai-openai-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 2032bca0c465bb8d3e27cdb2977158df0834bc04889fbeb5a43c87d337058ca0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
