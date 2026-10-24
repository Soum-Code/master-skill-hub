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

- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [bm:ai-integration-phase](bm-ai-integration-phase.md) - Generate AI design contract (AI-SPEC.md) for phases that involve building AI systems — framework selection, im
- [bm:docs-update](bm-docs-update.md) - Generate or update project documentation verified against the codebase
- [example-skills:doc-coauthoring](example-skills-doc-coauthoring.md) - Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documen

## Invoke / install

- Invoke: `/bm:new-ddd`  (Skill tool: `bm:new-ddd`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
