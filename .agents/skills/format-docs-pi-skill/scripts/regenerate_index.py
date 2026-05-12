#!/usr/bin/env python3
"""Phase 4: regenerate 000-index.md from current metadata.json.

Preserves the EXISTING index's structure where possible:
  - Reads existing 000-index.md (if present) for category order + frontmatter
    `categories` field type (int vs YAML list).
  - Drops categories that became empty after deletions.
  - Recomputes per-category file ranges from current numbering (gaps from
    deletions stay — feature, not a bug).
  - Updates total_docs and `generated` timestamp; adds optimized/optimized_at/format
    to frontmatter.

Note: H4 sub-buckets are flattened into a single H3 table per category. If the
original index used H4 sub-grouping (e.g. by filename prefix) and that nuance
matters, manually polish the regenerated index after this script runs.
"""
import sys, json, re
from pathlib import Path
from datetime import datetime, timezone

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
H3_RE = re.compile(r"^###\s+(?:\d+\.\s*)?(.+?)(?:\s*\(\s*\d+\s*[–-]\s*\d+\s*\))?\s*$")


def load_skeleton(idx_path: Path):
    if not idx_path.exists():
        return {"cat_kind": "int", "h1": "Documentation Index", "category_order": []}
    txt = idx_path.read_text()
    fm_match = FM_RE.match(txt)
    body = txt[fm_match.end():] if fm_match else txt
    fm_text = fm_match.group(1) if fm_match else ""

    cat_kind = "int"
    for ln in fm_text.splitlines():
        if ln.startswith("categories:"):
            v = ln.split(":", 1)[1].strip()
            if v.startswith("[") or v == "":
                cat_kind = "list"
            elif v.isdigit():
                cat_kind = "int"
            else:
                cat_kind = "str"
            break

    h1m = H1_RE.search(body)
    h1 = h1m.group(1).strip() if h1m else "Documentation Index"

    cats = []
    for line in body.splitlines():
        m = H3_RE.match(line)
        if m:
            cats.append(m.group(1).strip())

    return {"cat_kind": cat_kind, "h1": h1, "category_order": cats}


def file_num(name: str) -> str:
    m = re.match(r"^(\d{3})-", name)
    return m.group(1) if m else "???"


_TITLE_SUFFIX_RE = re.compile(r"\s*[-–—]\s*[A-Z][\w .]+\s+Docs?\s*$")


def clean_title(s: str) -> str:
    """Strip trailing site-name suffixes like ' - Fireworks AI Docs'."""
    return _TITLE_SUFFIX_RE.sub("", (s or "").strip())


def render_table(rows: list) -> str:
    out = ["| # | File | Title |",
           "|---|---|---|"]
    for r in rows:
        out.append(f"| {r['n']} | `{r['f']}` | {clean_title(r.get('title',''))} |")
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("Usage: regenerate_index.py <dir>", file=sys.stderr)
        sys.exit(1)
    d = Path(sys.argv[1]).resolve()
    meta = json.loads((d / "metadata.json").read_text())
    docs = sorted(meta.get("documents", []), key=lambda e: e.get("file_path", ""))

    skel = load_skeleton(d / "000-index.md")

    by_cat = {}
    for e in docs:
        c = e.get("category", "Uncategorized")
        by_cat.setdefault(c, []).append(e)

    # Honor original category order; append any new categories
    ordered = []
    seen = set()
    cats_lower = {c.lower(): c for c in by_cat}
    for orig in skel["category_order"]:
        ol = orig.lower()
        match = None
        if ol in cats_lower:
            match = cats_lower[ol]
        else:
            for k_low, actual in cats_lower.items():
                if k_low in ol or ol in k_low:
                    match = actual
                    break
        if match and match not in seen and by_cat.get(match):
            ordered.append(match)
            seen.add(match)
    for c in by_cat:
        if c not in seen and by_cat[c]:
            ordered.append(c)
            seen.add(c)

    now = datetime.now(timezone.utc).isoformat()
    src = meta.get("source_url", "")

    fm = ["description: Auto-generated documentation index (AI-optimized)"]
    if src:
        fm.append(f"source: {src}")
    fm.append(f"generated: {now}")
    fm.append(f"total_docs: {len(docs)}")
    if skel["cat_kind"] == "list":
        fm.append(f"categories: [{', '.join(ordered)}]")
    elif skel["cat_kind"] == "str":
        fm.append(f"categories: {', '.join(ordered)}")
    else:
        fm.append(f"categories: {len(ordered)}")
    fm += [
        "optimized: true",
        f"optimized_at: {now}",
        "format: obsidian",
    ]

    out = ["---"] + fm + ["---", "", f"# {skel['h1']}", "",
           "> Organized for AI agent consumption. "
           "Files numbered following a logical learning sequence. "
           "Gaps in numbering reflect intentional deletions during optimization.",
           "", "## Summary", "",
           "| Property | Value |", "|----------|-------|"]
    if src:
        out.append(f"| Source | {src} |")
    out += [
        f"| Generated | {now} |",
        f"| Total Documents | {len(docs)} |",
        f"| Categories | {', '.join(ordered)} |",
        "", "---", "", "## Document Index", "",
    ]

    for i, cat in enumerate(ordered, 1):
        entries = sorted(by_cat[cat], key=lambda e: e.get("file_path", ""))
        nums = [file_num(e.get("file_path", "")) for e in entries]
        rng = f"{nums[0]}–{nums[-1]}" if nums else ""
        out.append(f"### {i}. {cat} ({rng})")
        out.append("")
        rows = [{
            "n": file_num(e.get("file_path", "")),
            "f": e.get("file_path", ""),
            "title": e.get("title", ""),
            "summary": e.get("summary", ""),
            "tags": e.get("tags", []),
        } for e in entries]
        out.append(render_table(rows))
        out.append("")

    (d / "000-index.md").write_text("\n".join(out))
    print(json.dumps({
        "categories": len(ordered),
        "total_docs": len(docs),
        "path": str(d / "000-index.md"),
    }, indent=2))


if __name__ == "__main__":
    main()
