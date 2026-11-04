# laravel-plugin-discovery

> Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibility.

| | |
|---|---|
| **ID** | `affaan-m/ECC:laravel-plugin-discovery` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Product Management) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 231 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibility.

## What it says up front

> Find, evaluate, and choose healthy Laravel packages using the LaraPlugins.io MCP server.

## How it is structured

The skill's own section headings, in order:

- When to Use
- MCP Requirement
- MCP Tools
  - SearchPluginTool
  - GetPluginDetailsTool
- How It Works
  - Finding Packages
  - Evaluating Packages
  - Checking Compatibility
- Examples
  - Example: Find Authentication Packages
  - Example: Find Laravel 12 Compatible Packages
  - Example: Get Package Details
  - Example: Find Packages by Vendor
- Filtering Best Practices
  - By Health Score
  - By Laravel Version
  - Combining Filters
- Response Interpretation
  - Search Results
  - Package Details
- Common Use Cases
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [affaan-m/ECC:fal-ai-media](affaan-m-ecc-fal-ai-media.md) - Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/im
- [anthropics/knowledge-work-plugins:start](anthropics-knowledge-work-plugins-start.md) - Set up your bio-research environment and explore available tools. Use when first getting oriented with the plu
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us

## Invoke / install

- Invoke: `/affaan-m/ECC:laravel-plugin-discovery`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/laravel-plugin-discovery --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5f47629f31b44738a6930fba8c2c25ae61f7db6c685914db1107b97cd5571672 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
