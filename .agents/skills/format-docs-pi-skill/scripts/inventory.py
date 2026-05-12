#!/usr/bin/env python3
"""Phase 0 inventory.

- Lists root *.md files (no recursion), excluding 000-index.md.
- Cross-checks against metadata.json documents[].
- Reports orphans (file on disk, missing from metadata) and missing (vice-versa).
- Detects already-optimized files via `optimized: true` frontmatter flag.
- With --absorb-orphans: writes stub entries for orphans into metadata.json so they
  join the normal triage + optimization flow.

Outputs JSON to stdout.
"""
import sys, json, re, argparse
from pathlib import Path

OPT_RE = re.compile(r"^optimized:\s*true\s*$", re.M)
H1_RE = re.compile(r"^#\s+(.+)$", re.M)


def derive_title(path: Path) -> str:
    text = path.read_text(errors="replace")
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    slug = re.sub(r"^\d{3}-", "", path.stem).replace("-", " ")
    return slug.title()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--absorb-orphans", action="store_true",
                    help="write stub metadata entries for orphan files")
    args = ap.parse_args()

    d = Path(args.dir).resolve()
    meta_path = d / "metadata.json"
    meta = json.loads(meta_path.read_text())
    docs = meta.get("documents", [])
    by_path = {e.get("file_path"): e for e in docs}

    files = sorted(p.name for p in d.glob("*.md") if p.name != "000-index.md")
    orphans = [f for f in files if f not in by_path]
    missing = [k for k in by_path if k not in files]

    already, pending = [], []
    for f in files:
        text = (d / f).read_text(errors="replace")
        (already if OPT_RE.search(text) else pending).append(f)

    absorbed = []
    if args.absorb_orphans and orphans:
        for fname in orphans:
            entry = {
                "file_path": fname,
                "title": derive_title(d / fname),
                "summary": "",
                "tags": [],
                "url": "",
                "category": "Uncategorized",
                "optimized": False,
            }
            docs.append(entry)
            absorbed.append(fname)
        meta["documents"] = docs
        tmp = d / "metadata.json.tmp"
        tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
        tmp.replace(meta_path)

    out = {
        "abs_dir": str(d),
        "files_on_disk": files,
        "documents_in_meta": len(docs),
        "orphans": orphans,
        "absorbed_orphans": absorbed,
        "missing_on_disk": missing,
        "already_optimized": already,
        "pending": pending,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
