#!/usr/bin/env python3
"""Phase 1 triage: duplicate-index + empty/unusable detection.

Phase 1a — duplicate-index: any non-numbered file that duplicates 000-index.md's role
(filename like index/README/TOC/contents/catalog/summary/overview, OR body dominated by
a list of links pointing at sibling numbered docs).

Phase 1b — empty/unusable:
  - <30 words AND no code/tables/links → unusable
  - frontmatter + ≤1 link + ≤1 sentence pointing at homepage/index → unusable
  - 404 / "page not found" content → unusable

Default dry-run. --apply mutates: rm files, prune metadata.documents[],
append to metadata.optimization.deleted_files[].

Outputs JSON.
"""
import sys, json, re, argparse
from pathlib import Path

INDEX_NAMES = {"index.md", "README.md", "TOC.md", "contents.md",
               "catalog.md", "summary.md", "overview.md"}
NUMBERED_RE = re.compile(r"^\d{3}-.*\.md$")
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)
LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")
NUM_FILE_RE = re.compile(r"\d{3}-[a-z0-9._-]+\.md")
POINTER_KEYWORDS = ("welcome", "see ", "click here", "read more", "learn more")


def is_numbered(name: str) -> bool:
    return bool(NUMBERED_RE.match(name))


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).strip()


def has_code(text: str) -> bool:
    return "```" in text


def has_table(text: str) -> bool:
    return any(re.match(r"\s*\|.*\|", l) for l in text.splitlines())


def has_link(text: str) -> bool:
    return bool(LINK_RE.search(text))


def is_index_like(path: Path) -> bool:
    name = path.name
    if name == "000-index.md" or is_numbered(name):
        return False
    if name.lower() in {n.lower() for n in INDEX_NAMES}:
        return True
    text = path.read_text(errors="replace")
    body = strip_frontmatter(text)
    refs_to_numbered = NUM_FILE_RE.findall(body)
    if len(refs_to_numbered) >= 5:
        # body dominated by sibling references
        non_blank = [l for l in body.splitlines() if l.strip()]
        link_lines = [l for l in non_blank if LINK_RE.search(l) or NUM_FILE_RE.search(l)]
        if non_blank and len(link_lines) / len(non_blank) > 0.4:
            return True
    return False


def is_unusable(path: Path):
    text = path.read_text(errors="replace")
    body = strip_frontmatter(text)
    words = len(body.split())
    structural = has_code(body) or has_table(body) or has_link(body)

    if words < 30 and not structural:
        return ("low-content", words)

    links = LINK_RE.findall(body)
    if words < 30 and len(links) <= 1:
        sentences = [s for s in re.split(r"[.!?]\s+", body) if s.strip()]
        if len(sentences) <= 2 and any(k in body.lower() for k in POINTER_KEYWORDS):
            return ("pointer-only", words)

    if words < 100 and re.search(r"\b(404|page not found|not found)\b", body, re.I):
        return ("error-page", words)

    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    d = Path(args.dir).resolve()
    meta_path = d / "metadata.json"
    meta = json.loads(meta_path.read_text())
    docs = meta.get("documents", [])

    files = sorted(p for p in d.glob("*.md") if p.name != "000-index.md")
    deleted = []

    # Phase 1a: duplicate index
    for p in files:
        if is_index_like(p):
            deleted.append({"file": p.name, "reason": "duplicate-index"})

    drop_set = {x["file"] for x in deleted}

    # Phase 1b: empty / unusable
    for p in files:
        if p.name in drop_set:
            continue
        v = is_unusable(p)
        if v:
            deleted.append({"file": p.name, "reason": v[0], "words": v[1]})

    if args.apply:
        opt_block = meta.setdefault("optimization", {})
        log = opt_block.setdefault("deleted_files", [])
        for entry in deleted:
            fp = d / entry["file"]
            if fp.exists():
                fp.unlink()
            docs = [e for e in docs if e.get("file_path") != entry["file"]]
            if entry["file"] not in log:
                log.append(entry["file"])
        meta["documents"] = docs
        tmp = d / "metadata.json.tmp"
        tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
        tmp.replace(meta_path)

    print(json.dumps({"deleted": deleted, "applied": args.apply,
                      "count": len(deleted)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
