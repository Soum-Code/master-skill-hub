# azure-search-nav

> Builds an Azure portal deep link to a specific blade/menu item for supported Microsoft.ContainerService, Microsoft.Kubernetes, and Microsoft.Compute resources using the aks-search-direct-mid semantic search API. WHEN: 'find where in the Azure portal to do something', 'search the portal for an operation', 'construct a portal link from a search query and a resource'.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-search-nav` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 4 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Container Service, Arc-enabled Kubernetes, or Compute resource. - User wants a portal deep link for a specific blade/menu item. - User provides a resource URL or ARM resource ID and a natural-language search query.

## How it is structured

The skill's own section headings, in order:

- Quick Reference
- When to Use This Skill
- Workflow
- Error Handling

## What it bundles

- scripts: `references/Invoke-PortalSearchNav.ps1`
- reference docs: `references/Invoke-PortalSearchNav.ps1`, `references/README.md`, `references/resource-types.json`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/microsoft/skills:azure-search-nav`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/aks-skills/skills/azure-search-nav --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree f7ea42f720a552cf8fe93c374534e814104620e41d529dc70cd91e3994933093 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
