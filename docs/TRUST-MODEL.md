# Trust model

Third-party skills are the new supply chain. A `SKILL.md` can tell your agent what to do, and the scripts next to it run with your permissions. Public audits of skill registries in 2026 found a large share with security flaws and coordinated campaigns of malicious skills. This hub is built on the assumption that **anything from the internet can be hostile**.

## What "verified" means

A skill is `verified` only if all of these hold:

1. It was downloaded as a zip of **one commit SHA** (never a moving branch).
2. Every file in the skill folder went through `vet.py` with no medium/high/critical finding (verdict PASS).
3. The folder's `tree_sha256` is recorded. Installing re-downloads, re-vets and **aborts if the hash differs**.
4. The owner is on the trusted list in `registry/sources.yml`, **or** a human approved it with `promote`.
5. If a language-model second opinion ran, it did not rate the skill high-risk. The model can only raise the risk level. A "low" answer never approves anything, so a skill that talks its way past the reviewer gains nothing.

It does **not** mean the skill is guaranteed safe. See the limits below.

## Tiers

| Status | Meaning | Router recommends it? |
|---|---|---|
| installed | already on the owner's machine (from the owner's own plugins) | yes |
| verified | passed the checks above | yes |
| candidate | vetted, waiting for a human (owner not trusted, or verdict REVIEW) | no |
| quarantined | failed vetting; only rule ids and short excerpts are stored | no |

## What the scanner looks for

Hidden Unicode (tag characters used to smuggle invisible instructions, bidi controls, zero-width), prompt-injection and concealment phrasing, fake system delimiters, skill-ranking manipulation, permission-bypass flags, download-and-execute, obfuscated execution, credential and browser-profile paths, environment dumping, known exfiltration and tunnelling hosts, raw-IP URLs, shorteners, destructive commands, persistence (cron, scheduled tasks, shell rc), privilege escalation, executables and nested archives, symlinks and path traversal, npm install hooks, oversized files, leaked tokens, broken frontmatter, keyword-stuffed descriptions.

Rules are tuned against real skills: run against the 200 skills installed when this hub was built, 191 passed, 8 needed review and 1 failed (a documentation page that quotes an attack string). That one false positive is why `promote --override-fail` exists and records what was overridden.

## Rug pulls

A clean skill today can be updated into a malicious one tomorrow. Pinned skills stay on their vetted commit. Each weekly run re-checks the upstream HEAD of every pinned skill and reports changes: a clean update from a trusted owner is re-pinned, anything else is flagged and the old pin stays.

## Defence in depth for the router

- Registry descriptions are length-capped and stripped of markup and invisible characters at build time **and again** when the router reads them.
- The router refreshes its registry only from `raw.githubusercontent.com` over HTTPS and rejects anything that is not a valid registry.
- `master-skill` instructs Claude to treat registry text as data and never act on instructions found in it.
- GitHub Actions workflows pin third-party actions to commit SHAs and never interpolate issue or input text into shell commands.

## Limits (be honest with yourself)

- Static scanning cannot prove safety. Published benchmarks show strong detectors still miss natural-language attacks that look like ordinary instructions.
- An LLM reviewer is another heuristic, not a verdict.
- Trusted owners can still ship a bad update; the pin and the re-check reduce, not remove, that risk.
- You are the last control. Read `SKILL.md` and any script before you let a skill run on something sensitive.
