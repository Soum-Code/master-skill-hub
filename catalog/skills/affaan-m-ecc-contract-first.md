# contract-first

> Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract (OpenAPI, AsyncAPI, Protocol Buffers, or JSON Schema), with generated consumer types and contract-verified integration. Use when parallel consumer and provider work must evolve an API or event schema without field drift, mock/production shape mismatch, or one side silently redefining the interface.

| | |
|---|---|
| **ID** | `affaan-m/ECC:contract-first` |
| **Pack** | Legal & Compliance (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 288 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when parallel consumer and provider work must evolve an API or event schema without field drift, mock/production shape mismatch, or one side silently redefining the interface.

## What it says up front

> Coordinate frontend/backend or service-to-service work through one authoritative, machine-checkable contract. Consumers state what they need, providers implement that shape, and both sides verify against the same artifact before integration.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The Boundary Artifact
- Consumer-First Workflow
  - 1. Identify Consumers and Owners
  - 2. Describe Consumer Jobs
  - 3. Define the Smallest Useful Contract
  - 4. Generate or Derive Consumer Types
  - 5. Verify the Provider
  - 6. Integrate by Comparing Evidence
- Contract Change Protocol
- Anti-Patterns
  - FAIL: Provider-Owned Guesswork
  - FAIL: Duplicate Sources of Truth
  - FAIL: Compile-Time Types as the Only Proof
  - FAIL: Private Field Changes
  - FAIL: Contract After Implementation
- Best Practices
- Completion Checklist
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:frontend-design-review](microsoft-skills-frontend-design-review.md) - Review and create distinctive, production-grade frontend interfaces with high design quality and design system

## Invoke / install

- Invoke: `/affaan-m/ECC:contract-first`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/contract-first --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6aeb7bab82df390ff086bcbced6f0f2ba952bd0f2bbe8dd4b57c54a5dc78e607 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
