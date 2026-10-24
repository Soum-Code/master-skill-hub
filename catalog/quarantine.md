# Quarantine

These failed vetting. Findings show rule ids and short excerpts only. Do not install them.

| Repo / skill | Why | Pinned commit |
|---|---|---|
| Egonex-AI/Understand-Anything:understand-domain | persistence (extract-domain-context.py:106) | `e24fcf6d37` |
| addyosmani/agent-skills:source-driven-development | inj-override (SKILL.md:110) | `aeac41d4d0` |
| anthropics/claude-code:Plugin Structure | exfil-sink (SKILL.md:383) | `318b7e6ac4` |
| anthropics/claude-plugins-official:plugin-structure | exfil-sink (SKILL.md:383) | `58267944f9` |
| anthropics/claude-plugins-official:receipts | inj-override (SKILL.md:142); inj-override (scripts/mine-transcripts.mjs:347) | `58267944f9` |
| anthropics/knowledge-work-plugins:nextflow-development | exec-remote (scripts/check_environment.py:120) | `33d3dea41a` |
| anthropics/skills:claude-api | cred-paths (shared/evals/report/build-report-lite.mjs:28); cred-paths (shared/evals/report/runner-scaffold.mjs:112); inj-override (shared/model-migration.md:863) | `dbd4588f9e` |
| code-yeongyu/oh-my-openagent:data-scientist | exec-remote (scripts/setup-uv.ps1:28); exec-remote (scripts/setup-uv.sh:39); exec-remote (scripts/setup-uv.sh:41) | `1a62c298d2` |
| code-yeongyu/oh-my-openagent:frontend | exec-remote (scripts/perfection/lighthouse-audit.py:13) | `1a62c298d2` |
| code-yeongyu/oh-my-openagent:programming | exec-remote (scripts/go/new-project.py:12); exec-remote (scripts/python/new-project.py:12); exec-remote (scripts/python/new-script.py:12) | `1a62c298d2` |
| code-yeongyu/oh-my-openagent:ultimate-browsing | inj-secret-exfil (references/insane-search/jina.md:66) | `1a62c298d2` |
| coreyhaines31/marketingskills:directory-submissions | exfil-sink (references/submission-tracker-template.csv:158) | `e85f3cbc2e` |
| coreyhaines31/marketingskills:lead-magnets | inj-override (evals/evals.json:100); inj-override (references/content-to-skill-corpus-design.md:42) | `e85f3cbc2e` |
| garrytan/gstack:benchmark-models | cred-paths (SKILL.md.tmpl:94) | `6f7488a70f` |
| garrytan/gstack:browse | inj-override (src/cli.ts:1299); exfil-sink (src/content-security.ts:325); exfil-sink (src/content-security.ts:327) | `6f7488a70f` |
| garrytan/gstack:careful | destructive (SKILL.md.tmpl:67); exec-remote (SKILL.md.tmpl:69); destructive (bin/check-careful.sh:36) | `6f7488a70f` |
| garrytan/gstack:gstack | exec-remote (.github/docker/Dockerfile.ci:102); cred-paths (.github/scripts/dia-gui-readiness.c:76); cred-paths (.github/scripts/qualify-dia-macos.ts:1014) | `6f7488a70f` |
| garrytan/gstack:gstack-upgrade | exec-remote (SKILL.md.tmpl:178) | `6f7488a70f` |
| nexu-io/open-design:docs-page | exec-remote (example.html:83) | `e03d5c23f3` |
| openai/skills:cloudflare-deploy | exfil-sink (references/pages-functions/patterns.md:14) | `49f948faa9` |
| openai/skills:screenshot | exec-obfuscated (scripts/take_screenshot.py:27) | `49f948faa9` |
| sickn33/agentic-awesome-skills:007 | inj-override (references/ai-agent-security.md:18); inj-roleplay (references/ai-agent-security.md:18); inj-override (references/ai-agent-security.md:410) | `dda521de21` |
| sickn33/agentic-awesome-skills:2slides-ppt-generator | inj-secret-exfil (SKILL.md:37) | `dda521de21` |
| sickn33/agentic-awesome-skills:agent-evals | inj-override (SKILL.md:163); inj-roleplay (SKILL.md:164); inj-override (SKILL.md:267) | `dda521de21` |
| sickn33/agentic-awesome-skills:agent-evaluation | inj-override (references/architecture-sketches.md:392) | `dda521de21` |
| thedotmack/claude-mem:Agent Cost Report | cred-paths (scripts/tests/test_render.py:168) | `c12d2dd58b` |
| thedotmack/claude-mem:do | no-skill-md (:0); symlink (SKILL.md:0) | `c12d2dd58b` |
| thedotmack/claude-mem:mode-creator | exfil-sink (scripts/configure-telegram.mjs:107) | `c12d2dd58b` |
| thedotmack/claude-mem:openclaw | exec-remote (install.sh:419); exec-remote (install.sh:422); exec-remote (install.sh:479) | `c12d2dd58b` |
