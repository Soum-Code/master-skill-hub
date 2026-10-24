# Security

## Reporting

If you find a malicious skill that passed vetting, a way to make `vet.py` or `install.py` write outside the skills folder, or any issue in the workflows, open a **private security advisory** on this repository (Security tab, Report a vulnerability). Please do not open a public issue for exploitable problems.

## Scope

- `skills/skill-vetter` (scanner and installer), `skills/master-skill` (router and registry refresh), `skillhub/` (pipeline) and `.github/workflows`.
- Third-party skills listed in the catalog are not maintained here. Report problems with them to their owners; we will quarantine on request.

## What this project promises

- Third-party skill files are never executed by the pipeline; they are downloaded into memory and read as text.
- Installs are pinned to a commit, hash-checked and dry-run by default.
- Workflows use least-privilege `permissions`, pin actions to commit SHAs and never interpolate untrusted text into shell commands.

## What it does not promise

That a verified skill is safe. See [docs/TRUST-MODEL.md](docs/TRUST-MODEL.md).
