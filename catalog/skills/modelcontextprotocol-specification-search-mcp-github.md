# search-mcp-github

> Search MCP PRs, issues, and discussions across the modelcontextprotocol GitHub org

| | |
|---|---|
| **ID** | `modelcontextprotocol/specification:search-mcp-github` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification) |
| **License** | Apache-2.0 |
| **Size** | 119 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> For historical decisions, prioritize merged PRs and closed issues over open items.

## How it is structured

The skill's own section headings, in order:

- Where to search
- Searching discussions
- Search term variants
- Deep diving into a PR
- Output format
  - PRs
  - Issues
  - Discussions
  - Notable maintainer quotes
  - Key insights
  - Footnotes
- General strategy

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:inbox](bm-inbox.md) - Triage and review all open GitHub issues and PRs against project templates and contribution guidelines

## Invoke / install

- Invoke: `/modelcontextprotocol/specification:search-mcp-github`
- Install: `python skills/skill-vetter/scripts/install.py modelcontextprotocol/specification --path plugins/mcp-spec/skills/search-mcp-github --commit d0e246ea3c69eafaa2806bc4cd28025703ba2c2b --expect-tree 603135eb93ed658454d5a8d44a2dc26bae3f59d15809e15e4aa71ebc67a88760 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
