# laravel-security

> Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. Use when reviewing Laravel auth, Eloquent safety, CSRF, XSS, API security, or deployment configuration.

| | |
|---|---|
| **ID** | `affaan-m/ECC:laravel-security` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 951 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing Laravel auth, Eloquent safety, CSRF, XSS, API security, or deployment configuration.

## What it says up front

> Comprehensive security guidelines for Laravel applications to protect against common vulnerabilities.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Production Configuration
  - Essential Production Settings
  - Environment File Security
  - HTTPS Enforcement
- Authentication
  - Sanctum (API Token Authentication)
  - Password Security
  - Session Management
- Authorization
  - Gates
  - Policies
  - Middleware Authorization
- Eloquent Security
  - Mass Assignment Protection
  - SQL Injection Prevention
  - Attribute Casting
  - Model Security
- CSRF Protection
  - Default Protection
  - Excluding Routes (Carefully)
  - CSRF with JavaScript
- XSS Prevention
  - Blade Templating Security
  - Safe HTML Handling
  - JavaScript Context Escaping
  - HTTP Headers for XSS Protection
- Input Validation
  - Form Request Validation
  - Custom Validation Rules

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-security](affaan-m-ecc-django-security.md) - Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS 
- [affaan-m/ECC:springboot-security](affaan-m-ecc-springboot-security.md) - Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and depende
- [affaan-m/ECC:fastapi-patterns](affaan-m-ecc-fastapi-patterns.md) - FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, 
- [affaan-m/ECC:security-review](affaan-m-ecc-security-review.md) - Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, 

## Invoke / install

- Invoke: `/affaan-m/ECC:laravel-security`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/laravel-security --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3c32cc2a7dd2376a6701998abb5805cedea7c65de23322882ceb6bab62764f09 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
