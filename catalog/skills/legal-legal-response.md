# legal-response

> Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

| | |
|---|---|
| **ID** | `legal:legal-response` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `legal` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 458 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

## What it says up front

> Generate a response to a common legal inquiry using configured templates. Customizes the response with specific details and includes escalation triggers for situations that should not use a templated response.

## How it is structured

The skill's own section headings, in order:

- Invocation
- Workflow
  - Step 1: Identify Inquiry Type
  - Step 2: Load Template
  - Step 3: Check Escalation Triggers
  - Step 4: Gather Specific Details
  - Step 5: Generate Response
  - Step 6: Template Creation (If No Template Exists)
- Response Categories
  - 1. Data Subject Requests (DSRs)
  - 2. Discovery Holds (Litigation Holds)
  - 3. Privacy Inquiries
  - 4. Vendor Legal Questions
  - 5. NDA Requests
  - 6. Subpoena / Legal Process
  - 7. Insurance Notifications
- Template Management Methodology
  - Template Organization
  - Template Lifecycle
- Template Creation Guide
  - 1. Define the Use Case
  - 2. Identify Required Elements
  - 3. Define Variables
  - 4. Draft the Template
  - 5. Define Escalation Triggers
  - 6. Add Metadata
  - Template Format
- Output Format
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:draft-response](anthropics-knowledge-work-plugins-draft-response.md) - Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a
- [legal:brief](legal-brief.md) - Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when s

## Invoke / install

- Invoke: `/legal:legal-response`  (Skill tool: `legal:legal-response`)
- Install: `bundled with Claude desktop (Cowork plugin 'legal'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
