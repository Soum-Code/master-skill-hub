# Contributing

- **Suggest a skill:** open a *Submit a skill* issue with the link. It is vetted and never executed.
- **Ask for one:** open a *Request a skill* issue; the next weekly run searches for it.
- **Fix classification:** add an entry to `registry/overrides.yml`, or tune keywords in `registry/packs.yml`.
- **Code changes:** `pip install pyyaml pytest`, then `python -m pytest -q`, `python -m skillhub build`, `python -m skillhub validate`. CI fails if generated files are out of date, so commit the build output.
- **Scanner rules** live in `skills/skill-vetter/scripts/vet.py`. Every new rule needs a failing-case and a benign-case test in `tests/test_vet.py`.
