#!/usr/bin/env python3
"""Single-file rename + metadata.json sync.

Used for semantic renames the agent decides:
  - Phase 1.3 index-named files (after reading content)
  - Phase 2 partial-duplicate -current/-legacy/-vN suffixes

The script is a small wrapper around os.rename + JSON edit so the agent never
has to mutate metadata.json by hand.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory")
    p.add_argument("old_name", help="Current filename (relative to directory)")
    p.add_argument("new_name", help="Target filename (relative to directory)")
    p.add_argument("--reason", default=None, help="Optional reason logged in metadata")
    args = p.parse_args()

    root = Path(args.directory).resolve()
    src = root / args.old_name
    dst = root / args.new_name
    md_path = root / "metadata.json"

    if not src.is_file():
        print(f"error: source missing: {src}", file=sys.stderr)
        return 2
    if dst.exists():
        print(f"error: destination exists: {dst}", file=sys.stderr)
        return 2
    if "index" in args.new_name.lower() and not args.new_name.startswith("000-index"):
        print(
            f"error: forbidden token 'index' in new name {args.new_name!r}",
            file=sys.stderr,
        )
        return 2

    src.rename(dst)

    metadata = json.loads(md_path.read_text(encoding="utf-8"))
    docs = metadata.get("documents", [])
    target = next((d for d in docs if d.get("file_path") == args.old_name), None)
    if target is None:
        print(
            f"warn: {args.old_name} not in documents[]; rename succeeded but no metadata entry to update",
            file=sys.stderr,
        )
    else:
        if "original_file_path" not in target:
            target["original_file_path"] = args.old_name
        target["file_path"] = args.new_name
        if args.reason:
            target.setdefault("rename_history", []).append(
                {"from": args.old_name, "to": args.new_name, "reason": args.reason}
            )

    md_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"old": args.old_name, "new": args.new_name, "metadata_updated": target is not None}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
