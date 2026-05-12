#!/usr/bin/env python3
"""Phase 4 + 5: Sequential numbering and metadata mutation.

Consumes a bucket plan (categorize.py output) and applies `nnn-` prefixes in
canonical order, rewriting metadata.json with original_file_path + a top-level
`organization` audit object.

Re-run safe: existing `nnn-` prefixes are stripped before re-numbering.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

NUM_PREFIX_RE = re.compile(r"^\d{3}-(.+)$")
TMP_SUFFIX = ".__num_tmp"


def strip_existing_prefix(name: str) -> str:
    m = NUM_PREFIX_RE.match(name)
    return m.group(1) if m else name


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory")
    p.add_argument(
        "--buckets",
        required=True,
        help="Path to JSON produced by categorize.py",
    )
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    root = Path(args.directory).resolve()
    md_path = root / "metadata.json"
    md = json.loads(md_path.read_text(encoding="utf-8"))
    docs = md.get("documents", [])
    by_path = {d["file_path"]: d for d in docs}

    bucket_data = json.loads(Path(args.buckets).read_text(encoding="utf-8"))

    plan: list[dict] = []
    counter = 1
    for bucket in bucket_data["buckets"]:
        items: list[dict] = []
        if bucket.get("sub_buckets"):
            for sb in bucket["sub_buckets"]:
                items.extend(sb["docs"])
        else:
            items = bucket["docs"]
        for d in items:
            old = d["file_path"]
            base = strip_existing_prefix(old)
            new = f"{counter:03d}-{base}"
            plan.append({"old": old, "new": new, "bucket": bucket["name"]})
            counter += 1

    out = {"applied": args.apply, "total": len(plan), "rename_plan": plan}

    if args.apply:
        # 1. move every source to temp name (avoids mid-loop collisions)
        for r in plan:
            if r["old"] == r["new"]:
                continue
            src = root / r["old"]
            if not src.exists():
                print(f"warn: source missing: {src}", file=sys.stderr)
                continue
            src.rename(root / (r["new"] + TMP_SUFFIX))
        # 2. settle into final names
        for r in plan:
            tmp = root / (r["new"] + TMP_SUFFIX)
            if tmp.exists():
                tmp.rename(root / r["new"])

        # 3. metadata: file_path + original_file_path
        for r in plan:
            doc = by_path.get(r["old"])
            if doc is None:
                continue
            if "original_file_path" not in doc:
                doc["original_file_path"] = r["old"]
            doc["file_path"] = r["new"]

        # 4. organization audit (preserves any existing dropped[])
        existing_org = md.get("organization", {})
        md["organization"] = {
            "method": "sequential-numbering",
            "organized_at": datetime.now(timezone.utc).isoformat(),
            "total_files": len(plan),
            "categories": bucket_data["buckets_used"],
            "dropped": existing_org.get("dropped", []),
        }
        md["total_documents"] = len(docs)

        md_path.write_text(
            json.dumps(md, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        out["metadata_updated"] = True

        # Sync bucket plan in place so downstream Phase 6 sees the new paths.
        old_to_new = {r["old"]: r["new"] for r in plan}
        for bucket in bucket_data["buckets"]:
            if bucket.get("sub_buckets"):
                for sb in bucket["sub_buckets"]:
                    for d in sb["docs"]:
                        d["file_path"] = old_to_new.get(d["file_path"], d["file_path"])
            else:
                for d in bucket["docs"]:
                    d["file_path"] = old_to_new.get(d["file_path"], d["file_path"])
        Path(args.buckets).write_text(
            json.dumps(bucket_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
