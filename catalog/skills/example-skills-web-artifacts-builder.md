# web-artifacts-builder

> Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

| | |
|---|---|
| **ID** | `example-skills:web-artifacts-builder` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 74 lines in SKILL.md, 5 file(s) |

## When to use it

- Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

## What it says up front

> To build powerful frontend claude.ai artifacts, follow these steps: 1. Initialize the frontend repo using `scripts/init-artifact.sh` 2. Develop your artifact by editing the generated code 3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh` 4. Display artifact to user 5. (Op

## How it is structured

The skill's own section headings, in order:

- Design & Style Guidelines
- Quick Start
  - Step 1: Initialize Project
  - Step 2: Develop Your Artifact
  - Step 3: Bundle to Single HTML File
  - Step 4: Share Artifact with User
  - Step 5: Testing/Visualizing the Artifact (Optional)
- Reference

## What it bundles

- scripts: `scripts/bundle-artifact.sh`, `scripts/init-artifact.sh`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac
- [affaan-m/ECC:angular-developer](affaan-m-ecc-angular-developer.md) - Generates Angular code and provides architectural guidance. Trigger when creating projects, components, or ser
- [affaan-m/ECC:frontend-design-direction](affaan-m-ecc-frontend-design-direction.md) - Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites,
- [affaan-m/ECC:agent-security-hardening](affaan-m-ecc-agent-security-hardening.md) - Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write worksp

## Invoke / install

- Invoke: `/example-skills:web-artifacts-builder`  (Skill tool: `example-skills:web-artifacts-builder`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
