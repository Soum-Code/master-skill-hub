# new-ddd

> Initialize a new project using Documentation-Driven Development. Research, then write user-facing docs (SPEC.md) as the spec, then user validates docs, then phases derive from doc sections. Best for CLIs, libraries, SDKs, APIs, plugin systems, anything with a well-defined user-facing surface.

| | |
|---|---|
| **ID** | `bm:new-ddd` |
| **Pack** | Software Development (also: Product Management) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 74 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> 2. Phases derive from `SPEC.md` sections / chapters rather than REQ-ID clusters. 3. Each phase's success criterion is "implementation matches the corresponding SPEC.md section" rather than "tests pass and UAT satisfied."

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `Task`, `AskUserQuestion`

## Related skills

- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an
- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/bm:new-ddd`  (Skill tool: `bm:new-ddd`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
