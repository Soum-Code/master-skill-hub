# quarkus-security

> Quarkus security implementation patterns: JWT and OIDC authentication, @RolesAllowed RBAC and SecurityIdentity checks, Bean Validation and custom validators, parameterized Panache queries, BCrypt password hashing, CORS and security headers, rate limiting, audit logging, Vault or environment-variable secrets, and dependency CVE scanning. Use when adding authentication or authorization, validating input, managing secrets, or hardening a Quarkus application.

| | |
|---|---|
| **ID** | `affaan-m/ECC:quarkus-security` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 469 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding authentication or authorization, validating input, managing secrets, or hardening a Quarkus application.

## What it says up front

> Best practices for securing Quarkus applications with authentication, authorization, and input validation.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Authentication
  - JWT Authentication
  - Custom Authentication Filter
- Authorization
  - Role-Based Access Control
  - Programmatic Security
- Input Validation
  - Bean Validation
  - Custom Validators
- SQL Injection Prevention
  - Panache Active Record (Safe by Default)
  - Native Queries (Use Parameters)
- Password Hashing
- CORS Configuration
- Secrets Management
  - HashiCorp Vault Integration
- Rate Limiting
- Security Headers
- Audit Logging
- Dependency Security Scanning
- Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:springboot-security](affaan-m-ecc-springboot-security.md) - Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and depende
- [affaan-m/ECC:security-review](affaan-m-ecc-security-review.md) - Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, 

## Invoke / install

- Invoke: `/affaan-m/ECC:quarkus-security`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/quarkus-security --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree d065ba0d0f3265d0d543925653dca2be21b74cb7f21c3fa2aa9e42e8032e4319 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
