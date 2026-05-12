#!/usr/bin/env python3
"""Phase 1: Filename normalization for organize-docs-skill.

Pipeline:
  1.1  lowercase every basename
  1.2  if every file shares a leading prefix terminated by - _ . (>=2 chars), strip it
  1.3  emit list of files still containing 'index' substring (agent renames these)

Default mode is dry-run (prints the plan as JSON). Pass --apply to mutate the
filesystem and metadata.json.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

TMP_SUFFIX = ".__norm_tmp"


def detect_common_prefix(names: list[str]) -> str | None:
    """Longest common prefix across `names`, terminated by - _ or .

    Returns None when no qualifying prefix exists (or it would be < 2 chars).
    """
    if len(names) < 2:
        return None
    shortest = min(names, key=len)
    common_len = 0
    for i, ch in enumerate(shortest):
        if all(n[i] == ch for n in names):
            common_len = i + 1
        else:
            break
    if common_len == 0:
        return None
    common = shortest[:common_len]
    last_sep = -1
    for i, ch in enumerate(common):
        if ch in "-_.":
            last_sep = i
    if last_sep < 1:
        return None
    return common[: last_sep + 1]


def is_safe_strip(prefix: str, names: list[str]) -> bool:
    seen: set[str] = set()
    for n in names:
        stripped = n[len(prefix) :]
        if not stripped or stripped[0] in "-_.0123456789":
            return False
        if stripped in seen:
            return False
        seen.add(stripped)
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", help="Folder containing metadata.json + .md files")
    p.add_argument("--apply", action="store_true", help="Apply renames; default dry-run")
    args = p.parse_args()

    root = Path(args.directory).resolve()
    md_path = root / "metadata.json"
    if not md_path.is_file():
        print(f"error: missing {md_path}", file=sys.stderr)
        return 2

    metadata = json.loads(md_path.read_text(encoding="utf-8"))
    docs = metadata.get("documents", [])

    md_files = sorted(
        f for f in os.listdir(root) if f.endswith(".md") and f != "metadata.json"
    )

    # name_chain[original_filename_on_disk] = current target name
    chain: dict[str, str] = {f: f for f in md_files}

    # Phase 1.1 lowercase
    lower_renames = []
    for f in list(chain.keys()):
        target = chain[f].lower()
        if target != chain[f]:
            lower_renames.append({"old": chain[f], "new": target})
            chain[f] = target

    # Phase 1.2 prefix strip
    current_targets = list(chain.values())
    prefix = detect_common_prefix(current_targets)
    prefix_renames: list[dict] = []
    prefix_applied: str | None = None
    if prefix and is_safe_strip(prefix, current_targets):
        prefix_applied = prefix
        for orig, cur in chain.items():
            stripped = cur[len(prefix) :]
            if stripped != cur:
                prefix_renames.append({"old": cur, "new": stripped})
                chain[orig] = stripped

    # Phase 1.3 detect leftover 'index' files
    index_pending = sorted(
        cur for cur in chain.values()
        if "index" in cur.lower() and not cur.startswith("000-index")
    )

    out = {
        "directory": str(root),
        "applied": args.apply,
        "total_files": len(md_files),
        "lowercase_renames": lower_renames,
        "prefix_stripped": prefix_applied,
        "prefix_renames": prefix_renames,
        "index_files_pending": index_pending,
        "metadata_updated": False,
    }

    if args.apply:
        # Two-step rename via temp suffix to handle case-insensitive FS + collisions.
        for orig, final in chain.items():
            if orig == final:
                continue
            src = root / orig
            tmp = root / (final + TMP_SUFFIX)
            if not src.exists():
                print(f"warn: source missing during rename: {src}", file=sys.stderr)
                continue
            src.rename(tmp)
        for orig, final in chain.items():
            if orig == final:
                continue
            tmp = root / (final + TMP_SUFFIX)
            if tmp.exists():
                tmp.rename(root / final)

        # Update metadata: track via doc.file_path matching original on-disk name
        by_orig = {d.get("file_path"): d for d in docs}
        for orig, final in chain.items():
            if orig == final:
                continue
            doc = by_orig.get(orig)
            if doc is None:
                continue
            if "original_file_path" not in doc:
                doc["original_file_path"] = orig
            doc["file_path"] = final

        md_path.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        out["metadata_updated"] = True

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
