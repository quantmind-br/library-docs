#!/usr/bin/env python3
"""Phase 3a: recalculate `word_count` in each numbered file's frontmatter.

The original `word_count` is set by the upstream crawler (e.g. `repodocs-go`)
based on raw HTML extraction. After format-docs optimization rewrites prose
into tables, code blocks, and structured Obsidian markdown, that count is
stale and misleading.

This script re-counts the body words of each `nnn-*.md` (excluding
frontmatter and code fence interiors) and rewrites the `word_count:` field
in-place. Also syncs `metadata.json[*].word_count` if present.

Idempotent. Safe to re-run.

Usage: recalc_word_count.py <dir>
"""
import sys, re, json
from pathlib import Path

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
WC_LINE_RE = re.compile(r"^word_count:\s*\d+\s*$", re.M)


def count_body_words(text: str) -> int:
    """Words in body, excluding frontmatter and code fence interiors."""
    fm_match = FM_RE.match(text)
    body = text[fm_match.end():] if fm_match else text
    out = []
    in_code = False
    for line in body.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        out.append(line)
    return len(" ".join(out).split())


def update_frontmatter_wc(text: str, new_wc: int) -> str:
    """Replace existing word_count: line, or insert one before closing ---."""
    fm_match = FM_RE.match(text)
    if not fm_match:
        return text
    fm_block = fm_match.group(1)
    rest = text[fm_match.end():]

    if WC_LINE_RE.search(fm_block):
        new_fm = WC_LINE_RE.sub(f"word_count: {new_wc}", fm_block)
    else:
        new_fm = fm_block.rstrip() + f"\nword_count: {new_wc}"

    return f"---\n{new_fm}\n---\n{rest}"


def main():
    if len(sys.argv) < 2:
        print("Usage: recalc_word_count.py <dir>", file=sys.stderr)
        sys.exit(1)

    d = Path(sys.argv[1]).resolve()
    if not d.is_dir():
        print(f"Not a directory: {d}", file=sys.stderr)
        sys.exit(2)

    updated = []
    skipped = []
    file_to_wc = {}

    for f in sorted(d.glob("[0-9][0-9][0-9]-*.md")):
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception as e:
            skipped.append({"file": f.name, "reason": str(e)})
            continue

        if not FM_RE.match(txt):
            skipped.append({"file": f.name, "reason": "no frontmatter"})
            continue

        new_wc = count_body_words(txt)
        new_txt = update_frontmatter_wc(txt, new_wc)
        if new_txt != txt:
            f.write_text(new_txt, encoding="utf-8")
            updated.append({"file": f.name, "word_count": new_wc})
        file_to_wc[f.name] = new_wc

    # Sync metadata.json[*].word_count when the field already exists there.
    meta_path = d / "metadata.json"
    meta_synced = 0
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            changed = False
            for entry in meta.get("documents", []):
                fp = entry.get("file_path") or entry.get("file")
                if fp in file_to_wc and entry.get("word_count") != file_to_wc[fp]:
                    entry["word_count"] = file_to_wc[fp]
                    meta_synced += 1
                    changed = True
            if changed:
                meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
                                     encoding="utf-8")
        except Exception as e:
            skipped.append({"file": "metadata.json", "reason": f"sync failed: {e}"})

    print(json.dumps({
        "updated": len(updated),
        "skipped": len(skipped),
        "metadata_entries_synced": meta_synced,
        "total_words": sum(file_to_wc.values()),
        "skipped_details": skipped[:5],
    }, indent=2))


if __name__ == "__main__":
    main()
