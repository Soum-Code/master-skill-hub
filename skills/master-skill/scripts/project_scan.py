#!/usr/bin/env python3
"""project_scan.py - read-only fingerprint of a project folder (stdlib only, never executes anything).

    python project_scan.py [dir]      ->  JSON: detected stack signals + task queries to feed route.py
"""
import json
import os
import re
import sys

SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".next", "target"}
# (signal, regex over relative file paths, query to ask the router)
RULES = [
    ("python", r"(^|/)(pyproject\.toml|requirements.*\.txt|setup\.py|Pipfile)$|\.py$", "python code testing"),
    ("javascript/typescript", r"(^|/)(package\.json|tsconfig\.json)$", "typescript javascript frontend testing"),
    ("docker", r"(^|/)(Dockerfile|docker-compose\.ya?ml)$", "docker container deployment"),
    ("kubernetes", r"(^|/)(k8s|kubernetes|helm|charts)/", "kubernetes deployment autoscaling"),
    ("terraform/iac", r"\.tf$", "terraform infrastructure cloud"),
    ("github-actions", r"^\.github/workflows/.+\.ya?ml$", "ci cd github actions pipeline"),
    ("notebooks", r"\.ipynb$", "data analysis notebook machine learning"),
    ("web-ui", r"(^|/)(tailwind\.config\.\w+|index\.html)$|\.(tsx|jsx|vue|svelte)$", "ui design frontend landing page"),
    ("documents", r"\.(docx|pptx|pdf)$", "documents writing presentation"),
    ("sql/db", r"\.sql$|(^|/)(alembic|migrations)/", "sql database migrations"),
    ("mcp", r"(^|/)\.mcp\.json$", "mcp server"),
    ("claude-config", r"(^|/)(CLAUDE\.md|\.claude)(/|$)", "claude code plugin skill"),
]
ML_QUERY = "machine learning model training evaluation llm"
ML_WORDS = re.compile(r"\b(torch|tensorflow|scikit-learn|sklearn|transformers|langchain|openai|anthropic|xgboost|mlflow|huggingface|pandas|numpy)\b", re.I)
MANIFEST = re.compile(r"(^|/)(requirements.*\.txt|pyproject\.toml|package\.json)$")


def scan(root: str) -> dict:
    files = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        if dp[len(root):].count(os.sep) >= 3:
            dns[:] = []
        files += [os.path.relpath(os.path.join(dp, f), root).replace("\\", "/") for f in fns]
        if len(files) > 4000:
            break
    signals, queries = {}, []
    for name, rx, q in RULES:
        hits = [f for f in files if re.search(rx, f)]
        if hits:
            signals[name] = hits[:3]
            queries.append(q)
    words = set()
    for f in filter(MANIFEST.search, files):
        try:
            with open(os.path.join(root, f), encoding="utf-8", errors="replace") as fh:
                words |= {w.lower() for w in ML_WORDS.findall(fh.read(20000))}
        except OSError:
            pass
    if words or "notebooks" in signals:
        signals["ml/llm"] = sorted(words)[:6]
        queries.append(ML_QUERY)
    return {"root": os.path.abspath(root), "files_seen": len(files), "signals": signals,
            "queries": list(dict.fromkeys(queries))}


if __name__ == "__main__":
    print(json.dumps(scan(sys.argv[1] if len(sys.argv) > 1 else "."), indent=2))
