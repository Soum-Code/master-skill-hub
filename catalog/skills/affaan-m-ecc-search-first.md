# search-first

> Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before writing custom code, then adopt, extend, or build. Launches the researcher agent for non-trivial needs. Use when starting a feature, adding a dependency or integration, or about to write a utility that may already exist.

| | |
|---|---|
| **ID** | `affaan-m/ECC:search-first` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 184 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when starting a feature, adding a dependency or integration, or about to write a utility that may already exist.

## What it says up front

> Systematizes the "search for existing solutions before implementing" workflow.

## How it is structured

The skill's own section headings, in order:

- Trigger
- Workflow
- Decision Matrix
- How to Use
  - Step 0: Tool Availability Preflight
  - Quick Mode (inline)
  - Full Mode (agent)
- Search Shortcuts by Category
  - Development Tooling
  - AI/LLM Integration
  - Data & APIs
  - Content & Publishing
- Integration Points
  - With planner agent
  - With architect agent
  - With iterative-retrieval skill
- Examples
  - Example 1: "Add dead link checking"
  - Example 2: "Add HTTP client wrapper"
  - Example 3: "Add config file linter"
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us
- [microsoft/skills:copilot-sdk](microsoft-skills-copilot-sdk.md) - Build applications powered by GitHub Copilot using the Copilot SDK. Use when creating programmatic integration
- [anthropics/knowledge-work-plugins:start](anthropics-knowledge-work-plugins-start.md) - Set up your bio-research environment and explore available tools. Use when first getting oriented with the plu
- [openai/skills:chatgpt-apps](openai-skills-chatgpt-apps.md) - Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widge

## Invoke / install

- Invoke: `/affaan-m/ECC:search-first`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/search-first --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a72f5a6461bad9e0869cb12a3c32b566b40fe050131cef9d5c7d1fdc9428375e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
