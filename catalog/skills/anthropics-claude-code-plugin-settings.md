# Plugin Settings

> This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

| | |
|---|---|
| **ID** | `anthropics/claude-code:Plugin Settings` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 545 lines in SKILL.md, 8 file(s) |

## When to use it

- This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior co.

## How it is structured

The skill's own section headings, in order:

- Overview
- File Structure
  - Basic Template
  - Example: Plugin State File
- Reading Settings Files
  - From Hooks (Bash Scripts)
  - From Commands
  - From Agents
- Parsing Techniques
  - Extract Frontmatter
  - Read Individual Fields
  - Read Markdown Body
- Common Patterns
  - Pattern 1: Temporarily Active Hooks
  - Pattern 2: Agent State Management
  - Pattern 3: Configuration-Driven Behavior
- Creating Settings Files
  - From Commands
  - Template Generation
- Best Practices
  - File Naming
  - Gitignore
  - Defaults
  - Validation
  - Restart Requirement
- Security Considerations
  - Sanitize User Input
  - Validate File Paths
  - Permissions
- Real-World Examples

## What it bundles

- scripts: `examples/read-settings-hook.sh`, `scripts/parse-frontmatter.sh`, `scripts/validate-settings.sh`
- reference docs: `references/parsing-techniques.md`, `references/real-world-examples.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:plugin-settings](anthropics-claude-plugins-official-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-plugins-official:command-development](anthropics-claude-plugins-official-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com

## Invoke / install

- Invoke: `/anthropics/claude-code:Plugin Settings`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/plugin-dev/skills/plugin-settings --commit 2eff7a8d21c80be48904f62ebdea36d945d7b504 --expect-tree cdefba18ca4da8beb3e41beb9c445cb63d83b06c9535a3b8aff30d355ffcdd10 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
