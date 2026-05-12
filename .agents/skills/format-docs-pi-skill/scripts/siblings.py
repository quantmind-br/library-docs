#!/usr/bin/env python3
"""Emit sibling-docs JSON for agent prompt injection.

For every surviving *.md (excluding 000-index.md), produce:
  [{"file": "001-foo.md", "url": "...", "title": "<from H1>"}]

Title MUST come from the file's H1 (fallback: filename slug). NEVER from
metadata.json's top-level `title` field — that field is often the sitemap-fetched
page title and may be duplicated across docs, making title-matching useless.
"""
import sys, json, re
from pathlib import Path

H1_RE = re.compile(r"^#\s+(.+)$", re.M)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)


def derive_title(path: Path) -> str:
    text = path.read_text(errors="replace")
    body = FRONTMATTER_RE.sub("", text, count=1)
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    slug = re.sub(r"^\d{3}-", "", path.stem).replace("-", " ")
    return slug.title()


def main():
    if len(sys.argv) < 2:
        print("Usage: siblings.py <dir>", file=sys.stderr)
        sys.exit(1)
    d = Path(sys.argv[1]).resolve()
    meta = json.loads((d / "metadata.json").read_text())
    by_path = {e.get("file_path"): e for e in meta.get("documents", [])}

    out = []
    for p in sorted(d.glob("*.md")):
        if p.name == "000-index.md":
            continue
        e = by_path.get(p.name, {})
        out.append({
            "file": p.name,
            "url": e.get("url", ""),
            "title": derive_title(p),
        })
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
