# security-review

> Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Provides comprehensive security checklist and patterns.

| | |
|---|---|
| **ID** | `affaan-m/ECC:security-review` |
| **Pack** | Security & Privacy (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 512 lines in SKILL.md, 2 file(s) |

## When to use it

- Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features.

## What it says up front

> This skill ensures all code follows security best practices and identifies potential vulnerabilities.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Security Checklist
  - 1. Secrets Management
  - 2. Input Validation
  - 3. SQL Injection Prevention
  - 4. Authentication & Authorization
  - 5. XSS Prevention
  - 6. CSRF Protection
  - 7. Rate Limiting
  - 8. Sensitive Data Exposure
  - 9. Blockchain Security (Solana)
  - 10. Dependency Security
- Security Testing
  - Automated Security Tests
- Pre-Deployment Security Checklist
- Resources

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-security](affaan-m-ecc-django-security.md) - Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS 
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [affaan-m/ECC:laravel-security](affaan-m-ecc-laravel-security.md) - Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API se
- [affaan-m/ECC:quarkus-security](affaan-m-ecc-quarkus-security.md) - Quarkus security implementation patterns: JWT and OIDC authentication, @RolesAllowed RBAC and SecurityIdentity

## Invoke / install

- Invoke: `/affaan-m/ECC:security-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/security-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 82f0baf21df8556a77bb38a2b4870c4650a01535ae28925ec92b1c7b3d954beb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
