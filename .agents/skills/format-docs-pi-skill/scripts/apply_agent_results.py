#!/usr/bin/env python3
"""Parse agent reports, apply DELETE: lines.

Reads concatenated agent-report text from stdin. Expected line forms:
  OK: <abs_path> — <old_words>w → <new_words>w (-X%)
  DELETE: <abs_path> — <reason>

OK lines are ignored (informational). For each DELETE line: rm the file +
remove its entry from metadata.documents[] + append to
metadata.optimization.deleted_files[].

Usage:
  cat agent_reports.txt | apply_agent_results.py <dir>
"""
import sys, json, re, argparse
from pathlib import Path

DELETE_RE = re.compile(r"^\s*DELETE:\s*(\S+)(?:\s*[—\-]\s*(.+))?\s*$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    args = ap.parse_args()
    d = Path(args.dir).resolve()
    meta_path = d / "metadata.json"
    meta = json.loads(meta_path.read_text())
    docs = meta.get("documents", [])
    opt_block = meta.setdefault("optimization", {})
    log = opt_block.setdefault("deleted_files", [])

    deleted = []
    for line in sys.stdin:
        m = DELETE_RE.match(line)
        if not m:
            continue
        name = Path(m.group(1)).name
        reason = (m.group(2) or "agent-flagged").strip()
        target = d / name
        if target.exists():
            target.unlink()
        docs = [e for e in docs if e.get("file_path") != name]
        if name not in log:
            log.append(name)
        deleted.append({"file": name, "reason": reason})

    meta["documents"] = docs
    tmp = d / "metadata.json.tmp"
    tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    tmp.replace(meta_path)

    print(json.dumps({"deleted": deleted, "count": len(deleted)},
                     indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
