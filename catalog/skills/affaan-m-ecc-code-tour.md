# code-tour

> Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured "explain how this works" requests. Use when the user asks for a code tour, onboarding walkthrough, PR tour, or an explanation of how a subsystem works.

| | |
|---|---|
| **ID** | `affaan-m/ECC:code-tour` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 255 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured "explain how this works" requests.
- Use when the user asks for a code tour, onboarding walkthrough, PR tour, or an explanation of how a subsystem works.

## What it says up front

> Create **CodeTour** `.tour` files for codebase walkthroughs that open directly to real files and line ranges. Tours live in `.tours/` and are meant for the CodeTour format, not ad hoc Markdown notes.

## How it is structured

The skill's own section headings, in order:

- When to Use
- When NOT to Use
- Workflow
  - 1. Discover
  - 2. Infer the reader
  - 3. Read and verify anchors
  - 4. Write the `.tour`
  - 5. Validate
- The `ref` Field
- Step Types
  - Content
  - Directory
  - File + line
  - Selection
  - Pattern
  - URI
- Writing Rule: SMIG
- Narrative Shape
- Example
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 
- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [affaan-m/ECC:codebase-onboarding](affaan-m-ecc-codebase-onboarding.md) - Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry poi
- [example-skills:algorithmic-art](example-skills-algorithmic-art.md) - Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this wh

## Invoke / install

- Invoke: `/affaan-m/ECC:code-tour`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/code-tour --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree ac209313a64fb6e4d1cb57d57c3c38bdf8cd790f09d6960db77d077d2a8a2d11 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
