"""Copy the router and registry next to the function so `vercel deploy` from connector/ can ship them."""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = Path(__file__).resolve().parent / "_bundle"
out.mkdir(exist_ok=True)
shutil.copy(root / "skills" / "master-skill" / "scripts" / "route.py", out / "route.py")
shutil.copy(root / "skills" / "master-skill" / "references" / "registry.json", out / "registry.json")
print("bundled ->", out)
