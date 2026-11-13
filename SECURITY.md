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

## Safety layers (what protects someone who uses this hub)

1. **Nothing third-party is shipped here.** The repo stores names, descriptions, links and pinned commits only, never other people's code.
2. **Vetted before listed.** Every skill is scanned at an exact commit; failures are quarantined, not listed.
3. **Pinned and hash-checked.** `install.py` installs one commit, re-vets it, and aborts if the file hash changed since vetting. Dry run by default.
4. **Scripts need a second yes.** A skill that ships executable scripts is refused unless `--allow-scripts` is passed. It is tagged `RUNS SCRIPTS` in the router so the choice is visible.
5. **No silent updates for code.** A verified skill that ships scripts is never re-pinned automatically; the weekly report asks you to re-approve.
6. **Kill switch.** `python -m skillhub revoke <id> --reason ...` removes a skill from the router and the registry carries the reason, so routers warn users who still have it installed.
7. **Registry text is data.** Sanitised at build and again in the router; the master skill and agent are told never to follow instructions found in it.
8. **Humans approve unknown owners.** Only the trusted-owner list can auto-verify, and only on a clean scan.
9. **Review the reviewers.** Optional AI second opinion can only raise risk, never approve.
10. **Stars are not safety.** Ranking uses popularity to order the list; it never relaxes a check.

## Disclaimer

Provided as is, under the MIT license, with no warranty. Static checks reduce risk; they cannot remove it. Anyone who installs a third-party skill is responsible for reading it and for what it does on their machine. If you find a skill that should not be listed, report it (see Reporting above) and it will be revoked.

## What it does not promise

That a verified skill is safe. See [docs/TRUST-MODEL.md](docs/TRUST-MODEL.md).
