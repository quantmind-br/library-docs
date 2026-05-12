#!/usr/bin/env python3
"""Plan parallel agent batches by file size.

Heuristic (per slash command spec, ~10-15k input tokens per agent):
  ≤4 KB     → batch of 9
  4-15 KB   → batch of 5
  15-50 KB  → batch of 2
  >50 KB    → solo

Pre-filters files already carrying `optimized: true` in frontmatter (idempotency).

Outputs JSON: {total_pending, batch_count, batches: [[abs_path, ...], ...]}.
The dispatcher caps concurrent Agent calls at 10 per message; if batch_count > 10,
dispatch in sequential waves.
"""
import sys, json, re
from pathlib import Path

KB = 1024
OPT_RE = re.compile(r"^optimized:\s*true\s*$", re.M)


def bucket(size: int):
    if size <= 4 * KB:
        return "small", 9
    if size <= 15 * KB:
        return "medium", 5
    if size <= 50 * KB:
        return "large", 2
    return "huge", 1


def main():
    if len(sys.argv) < 2:
        print("Usage: plan_batches.py <dir>", file=sys.stderr)
        sys.exit(1)
    d = Path(sys.argv[1]).resolve()

    pending = []
    for p in sorted(d.glob("*.md")):
        if p.name == "000-index.md":
            continue
        text = p.read_text(errors="replace")
        if OPT_RE.search(text):
            continue
        pending.append((p, p.stat().st_size))

    groups = {"small": (9, []), "medium": (5, []), "large": (2, []), "huge": (1, [])}
    for path, size in pending:
        name, _ = bucket(size)
        groups[name][1].append(str(path))

    batches = []
    for name, (cap, files) in groups.items():
        for i in range(0, len(files), cap):
            batches.append(files[i:i + cap])

    print(json.dumps({
        "total_pending": len(pending),
        "batch_count": len(batches),
        "batches": batches,
    }, indent=2))


if __name__ == "__main__":
    main()
