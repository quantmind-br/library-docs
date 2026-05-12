#!/usr/bin/env python3
"""Phase 2: detect identical and partially-similar markdown files.

Self-contained replacement for the formerly-required `duplicate-find` shell
tool. Uses only the Python stdlib. Emits the JSON shape that
`classify_dupes.py` consumes:

    [
      {"file_a": "rel/a.md", "file_b": "rel/b.md",
       "similarity": 100, "type": "identico"},
      {"file_a": "rel/c.md", "file_b": "rel/d.md",
       "similarity": 87,  "type": "parcial"}
    ]

Sorted descending by similarity, then ascending by `file_a`.

Algorithm
---------
1. Collect top-level `*.md` files (excluding the generated `000-index.md`
   and `metadata.json`). Empty files are skipped.
2. SHA-256 each file. Files sharing a digest form an `identico` clique;
   one representative per hash advances to phase 3.
3. For each rep build the set of unique lines. Pairwise Jaccard similarity
   `|A ∩ B| / |A ∪ B|` (as integer percent). Skip a pair early when
   `min(|A|,|B|) / max(|A|,|B|) < threshold / 100` — Jaccard cannot exceed
   that ratio, so the comparison is provably below threshold.
4. Keep partial pairs in `[threshold, 100)`. Identical pairs (100) come
   from phase 2.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# Generated artifacts that should never participate in dedupe scanning.
_SKIP_BASENAMES = {"000-index.md", "metadata.json"}


def collect_md_files(root: Path) -> list[Path]:
    """Top-level non-empty *.md files, sorted by name."""
    out: list[Path] = []
    for p in sorted(root.iterdir()):
        if not p.is_file() or p.suffix != ".md":
            continue
        if p.name in _SKIP_BASENAMES:
            continue
        try:
            if p.stat().st_size == 0:
                continue
        except OSError:
            continue
        out.append(p)
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def line_set(path: Path) -> set[str]:
    """Set of unique line-text (newline stripped). Mirrors `sort -u` semantics."""
    with path.open("r", encoding="utf-8", errors="replace") as f:
        return {line.rstrip("\n") for line in f}


def jaccard_pct(a: set[str], b: set[str]) -> int:
    inter = len(a & b)
    union = len(a) + len(b) - inter
    if union == 0:
        return 0
    return inter * 100 // union


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("directory", help="Folder to scan (top level only)")
    p.add_argument(
        "--threshold",
        type=int,
        default=85,
        help="Jaccard similarity %% threshold for partial pairs (default 85)",
    )
    args = p.parse_args()

    root = Path(args.directory).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    threshold = max(0, min(100, args.threshold))

    files = collect_md_files(root)
    if len(files) < 2:
        print("[]")
        return 0

    # --- phase 2: hash → identical groups ---
    by_hash: dict[str, list[Path]] = {}
    for f in files:
        by_hash.setdefault(sha256(f), []).append(f)

    identical_pairs: list[tuple[Path, Path]] = []
    reps: list[Path] = []
    for group in by_hash.values():
        reps.append(group[0])
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    identical_pairs.append((group[i], group[j]))

    # --- phase 3: Jaccard over reps ---
    partial_pairs: list[tuple[Path, Path, int]] = []
    if threshold < 100 and len(reps) >= 2:
        sets: list[set[str]] = [line_set(r) for r in reps]
        sizes = [len(s) for s in sets]
        for i in range(len(reps)):
            la = sizes[i]
            if la == 0:
                continue
            for j in range(i + 1, len(reps)):
                lb = sizes[j]
                if lb == 0:
                    continue
                lo, hi = (la, lb) if la <= lb else (lb, la)
                if lo * 100 // hi < threshold:
                    continue
                sim = jaccard_pct(sets[i], sets[j])
                if threshold <= sim < 100:
                    partial_pairs.append((reps[i], reps[j], sim))

    def _emit(a: Path, b: Path, sim: int, kind: str) -> dict:
        # Canonicalize order: lexicographically smaller name as file_a so the
        # output is deterministic regardless of hash-group iteration order.
        ra, rb = str(a.relative_to(root)), str(b.relative_to(root))
        if ra > rb:
            ra, rb = rb, ra
        return {"file_a": ra, "file_b": rb, "similarity": sim, "type": kind}

    out: list[dict] = []
    for a, b in identical_pairs:
        out.append(_emit(a, b, 100, "identico"))
    for a, b, sim in partial_pairs:
        out.append(_emit(a, b, sim, "parcial"))
    out.sort(key=lambda d: (-d["similarity"], d["file_a"]))

    if out:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("[]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
