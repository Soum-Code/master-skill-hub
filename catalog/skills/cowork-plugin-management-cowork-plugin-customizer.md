# cowork-plugin-customizer

> Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

| | |
|---|---|
| **ID** | `cowork-plugin-management:cowork-plugin-customizer` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `cowork-plugin-management` v0.2.2 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 147 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

## What it says up front

> Customize a plugin for a specific organization — either by setting up a generic plugin template for the first time, or by tweaking and refining an already-configured plugin.

## How it is structured

The skill's own section headings, in order:

- Determining the Customization Mode
- Customization Workflow
  - Phase 0: Gather User Intent (scoped and general customization only)
  - Phase 1: Gather Context from Knowledge MCPs
  - Phase 2: Create Todo List
  - Phase 3: Complete Todo Items
  - Phase 4: Search for Useful MCPs
- Packaging the Plugin
- Summary Output
- Additional Resources

## What it bundles

- reference docs: `references/mcp-servers.md`, `references/search-strategies.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:setup-claude](anthropic-skills-setup-claude.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [anthropic-skills:setup-cowork](anthropic-skills-setup-cowork.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [bm:settings](bm-settings.md) - Configure GSD workflow toggles and model profile
- [update-config](update-config.md) - Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other auto

## Invoke / install

- Invoke: `/cowork-plugin-management:cowork-plugin-customizer`  (Skill tool: `cowork-plugin-management:cowork-plugin-customizer`)
- Install: `bundled with Claude desktop (Cowork plugin 'cowork-plugin-management'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
