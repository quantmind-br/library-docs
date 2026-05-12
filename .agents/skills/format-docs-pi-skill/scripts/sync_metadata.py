#!/usr/bin/env python3
"""Phase 3: sync metadata.json with on-disk frontmatter.

For every surviving file (no recursion, exclude 000-index.md):
  - Re-read YAML frontmatter
  - Sync `summary`, `tags`, `title`, `optimized` into the matching documents[] entry
  - Count how many carry `optimized: true`

Updates top-level metadata:
  - total_documents = current count
  - optimization{ method, format, optimized_at, files_optimized,
                  files_deleted, deleted_files }
    (preserves existing deleted_files[] accumulator from triage + agent passes)

Atomic write via tmp + rename.
"""
import sys, json, re
from pathlib import Path
from datetime import datetime, timezone

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def parse_frontmatter(text: str) -> dict:
    """Tiny YAML subset parser: scalars, multiline lists with `- value` items."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out = {}
    cur_key = None
    for raw in m.group(1).splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if re.match(r"^\s*-\s+", line):
            if cur_key is not None:
                v = re.sub(r"^\s*-\s+", "", line).strip().strip("'\"")
                out.setdefault(cur_key, []).append(v)
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if not v:
                cur_key = k
                out[k] = []
            else:
                cur_key = None
                v = v.strip("'\"")
                if v.lower() == "true":
                    v = True
                elif v.lower() == "false":
                    v = False
                out[k] = v
    return out


def main():
    if len(sys.argv) < 2:
        print("Usage: sync_metadata.py <dir>", file=sys.stderr)
        sys.exit(1)
    d = Path(sys.argv[1]).resolve()
    meta_path = d / "metadata.json"
    meta = json.loads(meta_path.read_text())
    docs = meta.get("documents", [])
    by_path = {e.get("file_path"): e for e in docs}

    surviving = sorted(p.name for p in d.glob("*.md") if p.name != "000-index.md")
    optimized_count = 0
    new_docs = []
    for name in surviving:
        text = (d / name).read_text(errors="replace")
        fm = parse_frontmatter(text)
        entry = by_path.get(name, {"file_path": name})
        for k in ("summary", "tags"):
            if k in fm:
                entry[k] = fm[k]
        if "title" in fm and not entry.get("title"):
            entry["title"] = fm["title"]
        if fm.get("optimized") is True:
            entry["optimized"] = True
            optimized_count += 1
        new_docs.append(entry)

    existing_opt = meta.get("optimization", {})
    deleted_files = existing_opt.get("deleted_files", [])

    meta["documents"] = new_docs
    meta["total_documents"] = len(new_docs)
    meta["optimization"] = {
        "method": "ai-consumption-optimized",
        "format": "obsidian",
        "optimized_at": datetime.now(timezone.utc).isoformat(),
        "files_optimized": optimized_count,
        "files_deleted": len(deleted_files),
        "deleted_files": deleted_files,
    }

    tmp = d / "metadata.json.tmp"
    tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    tmp.replace(meta_path)

    print(json.dumps({
        "total_documents": len(new_docs),
        "files_optimized": optimized_count,
        "files_deleted": len(deleted_files),
    }, indent=2))


if __name__ == "__main__":
    main()
