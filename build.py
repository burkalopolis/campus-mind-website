#!/usr/bin/env python3
"""Build paste-ready Grigora HTML blocks.

Each section file in sections/<page>/ holds only the section markup. This script
puts the shared styles (styles/cm-web.css) in front of every section and writes
the result to dist/<page>/, ready to paste into a Grigora HTML block.

Files ending in .standalone.html carry their own styles and are copied as-is.

Usage:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSS = (ROOT / "styles" / "cm-web.css").read_text(encoding="utf-8").strip()
# Drop the leading comment line so pasted blocks stay compact.
CSS_BODY = "\n".join(l for l in CSS.splitlines() if not l.lstrip().startswith("/*"))

count = 0
for src in sorted((ROOT / "sections").rglob("*.html")):
    out = ROOT / "dist" / src.relative_to(ROOT / "sections")
    out.parent.mkdir(parents=True, exist_ok=True)
    body = src.read_text(encoding="utf-8").strip()
    if src.name.endswith(".standalone.html"):
        out.write_text(body + "\n", encoding="utf-8")
    else:
        out.write_text(f"<style>\n{CSS_BODY}\n</style>\n{body}\n", encoding="utf-8")
    count += 1
    print(f"built {out.relative_to(ROOT)}")
print(f"{count} blocks written to dist/")
