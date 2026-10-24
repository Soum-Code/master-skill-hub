# openai-docs

> Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex surfaces, needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; use OpenAI docs MCP tools for non-Codex docs questions, use the Codex manual helper first for broad Codex self-knowledge, and restrict fallback browsing to official OpenAI domains.

| | |
|---|---|
| **ID** | `openai/skills:openai-docs` |
| **Pack** | AI / ML Engineering (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 162 lines in SKILL.md, 10 file(s) |

## When to use it

- Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex surfaces, needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade gui.

## How it is structured

The skill's own section headings, in order:

- Workflow Configuration
  - Source Priority
- OpenAI product snapshots
- Codex self-knowledge
  - Source Route
  - Surface Map
  - Boundaries And Output
- If MCP server is missing
- Workflow
- Reference map
- Quality rules
- Tooling notes

## What it bundles

- scripts: `scripts/fetch-codex-manual.mjs`, `scripts/resolve-latest-model-info.js`
- reference docs: `references/latest-model.md`, `references/prompting-guide.md`, `references/upgrade-guide.md`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [openai/skills:chatgpt-apps](openai-skills-chatgpt-apps.md) - Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widge
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/openai/skills:openai-docs`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/openai-docs --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 787bb3220c88c4f82012d4d522680e183f3cdcfdfe99700699ea424eb90b752d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
