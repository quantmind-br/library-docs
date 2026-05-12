#!/usr/bin/env python3
"""Drop a file and update metadata.json deterministically.

Used for Phase 2 identical-content drops. Removes the doc from documents[]
and appends an audit entry under organization.dropped[].
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory")
    p.add_argument("dropped", help="Filename to drop (relative)")
    p.add_argument("--in-favor-of", required=True, help="Filename being kept")
    p.add_argument("--reason", default="identico", help="identico|parcial-superseded|...")
    args = p.parse_args()

    root = Path(args.directory).resolve()
    target = root / args.dropped
    md_path = root / "metadata.json"

    if target.is_file():
        target.unlink()
    else:
        print(f"warn: {target} already missing", file=sys.stderr)

    metadata = json.loads(md_path.read_text(encoding="utf-8"))
    docs = metadata.get("documents", [])
    metadata["documents"] = [d for d in docs if d.get("file_path") != args.dropped]
    if "total_documents" in metadata:
        metadata["total_documents"] = len(metadata["documents"])

    org = metadata.setdefault("organization", {})
    org.setdefault("dropped", []).append(
        {
            "path": args.dropped,
            "in_favor_of": args.in_favor_of,
            "reason": args.reason,
        }
    )

    md_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "dropped": args.dropped,
                "in_favor_of": args.in_favor_of,
                "remaining": len(metadata["documents"]),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
