#!/usr/bin/env python3
"""Phase 2 helper: classify dedupe pairs into auto-resolvable groups.

Reads the JSON emitted by find_dupes.py and splits it into three lists:

  - `identico`            (similarity 100): drop the loser deterministically
  - `version-mirror`      (parcial pairs whose filenames differ only by a
                           version segment like `1.5-` or `v2-`):
                           keep the canonical / latest, drop the older
  - `parcial-ambiguous`   (everything else): the agent must read both files
                           and apply the manual decision tree

Output JSON shape:
{
  "identico": [{file_a, file_b, keep, drop, similarity}],
  "version_mirror": [{file_a, file_b, keep, drop, reason}],
  "ambiguous": [<original parcial pairs, untouched>],
  "summary": {"identico": N, "version_mirror": N, "ambiguous": N}
}

The agent applies the deterministic groups via `apply_drop.py`, then walks
the ambiguous list with the Read tool + `references/decision_trees.md`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_NUM_PREFIX_RE = re.compile(r"^\d{3}-")
# Matches a version-shaped segment between hyphens.
#   `-1.5-`, `-v2-`, `-v0.7.5-`, `-2024-`
# Anchored on hyphens so we strip whole tokens, not parts of words.
_VERSION_SEGMENT_RE = re.compile(
    r"-(?:v?\d+(?:[._]\d+)*[a-z]?\d*|\d{4})(?=-)",
    re.IGNORECASE,
)


def canonical_form(filename: str) -> str:
    """Strip nnn- prefix, version segments, and the .md extension."""
    base = _NUM_PREFIX_RE.sub("", filename)
    if base.endswith(".md"):
        base = base[:-3]
    # Repeat until stable so multiple version segments collapse
    prev = None
    while prev != base:
        prev = base
        base = _VERSION_SEGMENT_RE.sub("", base)
    return base.lower()


def version_score(filename: str) -> tuple:
    """Higher tuple = newer. Files without a version segment score highest
    (they are typically the canonical / current page on a docs site)."""
    base = _NUM_PREFIX_RE.sub("", filename)
    matches = re.findall(r"-(v?\d+(?:[._]\d+)*)", base)
    if not matches:
        # No version → canonical / latest. Sentinel beats any numeric score.
        return (1, ())
    # Parse the longest version string into a tuple of ints.
    raw = max(matches, key=len).lstrip("v").replace("_", ".")
    parts: list[int] = []
    for chunk in raw.split("."):
        try:
            parts.append(int(chunk))
        except ValueError:
            # alpha/beta suffixes — ignore
            break
    return (0, tuple(parts))


def classify(pair: dict) -> tuple[str, dict]:
    """Return (category, decision)."""
    a, b = pair["file_a"], pair["file_b"]
    sim = pair.get("similarity", 0)

    if pair.get("type") == "identico":
        # Keep the longer name as a tiebreaker (likely more descriptive); the
        # SKILL workflow can override with file size if it cares.
        keep, drop = (a, b) if len(a) >= len(b) else (b, a)
        return "identico", {
            "file_a": a, "file_b": b, "keep": keep, "drop": drop,
            "similarity": sim, "reason": "identico",
        }

    # Partial pair — check version-mirror condition.
    if canonical_form(a) == canonical_form(b) and canonical_form(a):
        sa, sb = version_score(a), version_score(b)
        if sa > sb:
            keep, drop = a, b
        elif sb > sa:
            keep, drop = b, a
        else:
            # Same version score but canonical_form matched — keep both,
            # surfacing as ambiguous because we cannot decide.
            return "ambiguous", pair
        return "version_mirror", {
            "file_a": a, "file_b": b, "keep": keep, "drop": drop,
            "similarity": sim, "reason": "parcial-version-mirror",
        }

    return "ambiguous", pair


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("dupes_json", help="Path to JSON from find_dupes.py")
    args = p.parse_args()

    pairs = json.loads(Path(args.dupes_json).read_text(encoding="utf-8"))
    out = {"identico": [], "version_mirror": [], "ambiguous": []}
    seen_drops: set[str] = set()  # avoid scheduling the same file twice
    for pair in pairs:
        category, decision = classify(pair)
        if category == "ambiguous":
            out["ambiguous"].append(decision)
        else:
            drop = decision["drop"]
            if drop in seen_drops:
                # Already scheduled for drop in another pair (transitive
                # version chain); skip the redundant entry.
                continue
            seen_drops.add(drop)
            out[category].append(decision)

    out["summary"] = {k: len(out[k]) for k in ("identico", "version_mirror", "ambiguous")}
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
