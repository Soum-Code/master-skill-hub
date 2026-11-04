# agent-runtime-gateway-smoke-test

> Verify a local agent API, temporary gateway tunnel, and remote sandbox callback with a tool-free task, then restore the original app connection.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-runtime-gateway-smoke-test` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 84 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Use this workflow when an agent task runs in a remote sandbox that calls back to a local API through a gateway. It verifies the whole path without relying on connected tools or private production data.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Required Inputs
- Authorization and Cleanup
- Smoke Test
- Connected Tool Follow-up
- Failure Handling
- Output Contract
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:mailtrap-email-integration](affaan-m-ecc-mailtrap-email-integration.md) - Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox test
- [affaan-m/ECC:agent-security-hardening](affaan-m-ecc-agent-security-hardening.md) - Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write worksp

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-runtime-gateway-smoke-test`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-runtime-gateway-smoke-test --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 71d403868c9c2bb973a49ad7117b83e1de3e1d8aa61d1d3f9fddcede8ab00191 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
