# django-security

> Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations. Use when reviewing Django authentication, authorization, input handling, or deployment settings.

| | |
|---|---|
| **ID** | `affaan-m/ECC:django-security` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 642 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing Django authentication, authorization, input handling, or deployment settings.

## What it says up front

> Comprehensive security guidelines for Django applications to protect against common vulnerabilities.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Security Settings
  - Production Settings Configuration
- Authentication
  - Custom User Model
  - Password Hashing
  - Session Management
- Authorization
  - Permissions
  - Custom Permissions
  - Role-Based Access Control (RBAC)
- SQL Injection Prevention
  - Django ORM Protection
  - Extra Security with raw()
- XSS Prevention
  - Template Escaping
  - Safe String Handling
  - HTTP Headers
- CSRF Protection
  - Default CSRF Protection
  - Exempting Views (Use Carefully)
- File Upload Security
  - File Validation
  - Secure File Storage
- API Security
  - Rate Limiting
  - Authentication for APIs
- Security Headers
  - Content Security Policy
- Environment Variables

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:laravel-security](affaan-m-ecc-laravel-security.md) - Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API se
- [affaan-m/ECC:springboot-security](affaan-m-ecc-springboot-security.md) - Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and depende
- [affaan-m/ECC:fastapi-patterns](affaan-m-ecc-fastapi-patterns.md) - FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, 
- [affaan-m/ECC:security-review](affaan-m-ecc-security-review.md) - Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, 

## Invoke / install

- Invoke: `/affaan-m/ECC:django-security`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/django-security --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1bc6d90b9cc9488ad6fc63a618b8ea196b09bf0b04240a824755e434a6ad384c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
