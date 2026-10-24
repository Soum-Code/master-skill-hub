# azure-ai-agents-persistent-dotnet

> Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. Use for agent CRUD, conversation threads, streaming responses, function calling, file search, and code interpreter. Triggers: "PersistentAgentsClient", "persistent agents", "agent threads", "agent runs", "streaming agents", "function calling agents .NET".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-ai-agents-persistent-dotnet` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 362 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for agent CRUD, conversation threads, streaming responses, function calling, file search, and code interpreter.

## What it says up front

> Low-level SDK for creating and managing persistent AI agents with threads, messages, runs, and tools.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
- Client Hierarchy
- Core Workflow
  - 1. Create Agent
  - 2. Create Thread and Message
  - 3. Run Agent (Polling)
  - 4. Streaming Response
  - 5. Function Calling
  - 6. File Search with Vector Store
  - 7. Bing Grounding
  - 8. Azure AI Search
  - 9. Cleanup
- Available Tools
- Streaming Update Types
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

- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-ai-openai-dotnet](microsoft-skills-azure-ai-openai-dotnet.md) - Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embe
- [microsoft/skills:azure-ai-document-intelligence-dotnet](microsoft-skills-azure-ai-document-intelligence-dotnet.md) - Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using pr
- [microsoft/skills:azure-mgmt-apimanagement-dotnet](microsoft-skills-azure-mgmt-apimanagement-dotnet.md) - Azure Resource Manager SDK for API Management in .NET. Use for MANAGEMENT PLANE operations: creating/managing 

## Invoke / install

- Invoke: `/microsoft/skills:azure-ai-agents-persistent-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-ai-agents-persistent-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree c90883934f18ffc713327eff6b314ed837a9288f5f738c75d67decc68183687e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
