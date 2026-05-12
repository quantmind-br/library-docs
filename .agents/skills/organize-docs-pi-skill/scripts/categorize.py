#!/usr/bin/env python3
"""Phase 3: Bucket assignment + ordering.

Reads metadata.json, applies the canonical rules (override > primary > tertiary
> fallback), detects bucket overflow, and emits a JSON plan consumable by
number_and_rename.py and generate_index.py.

Output schema:
{
  "total": <int>,
  "buckets_used": ["Introduction & Overview", ...],
  "buckets": [
    {
      "id": <1-16>,
      "name": "...",
      "count": <int>,
      "docs": [{"file_path": "...", "title": "..."}, ...],
      "sub_buckets": null | [{"prefix": "...", "docs": [...]}, ...]
    }
  ]
}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# 3.1.a Crawler-emitted category → canonical bucket
CRAWLER_TO_BUCKET = {
    "intro": 1, "overview": 1, "welcome": 1, "home": 1,
    "quickstart": 2, "installation": 2, "getting-started": 2,
    "tutorial": 3, "walkthrough": 3, "how-to": 3, "guide": 3,
    "concept": 4, "fundamentals": 4, "principles": 4,
    "configuration": 5, "settings": 5, "customization": 5,
    "feature": 6, "capability": 6,
    "integration": 7, "provider": 7, "plugin": 7, "extension": 7,
    "auth": 8, "security": 8, "permission": 8,
    "api": 9, "reference": 9, "sdk": 9,
    "deployment": 10, "operation": 10, "hosting": 10,
    "automation": 11, "workflow": 11,
    "advanced": 12, "optimization": 12,
    "troubleshooting": 13, "faq": 13, "error": 13,
    "glossary": 14, "appendix": 14,
    "changelog": 15, "release": 15, "version": 15,
    "pricing": 16, "license": 16, "legal": 16, "community": 16,
    "contributing": 16, "privacy": 16, "terms": 16, "meta": 16, "other": 16,
}

BUCKET_NAMES = {
    1: "Introduction & Overview",
    2: "Quick Start & Installation",
    3: "Tutorials & Guides",
    4: "Concepts & Fundamentals",
    5: "Configuration",
    6: "Features",
    7: "Integrations",
    8: "Auth & Security",
    9: "API Reference",
    10: "Operations & Deployment",
    11: "Automation & Workflows",
    12: "Advanced Topics",
    13: "Troubleshooting",
    14: "Glossary & Appendix",
    15: "Changelog & Releases",
    16: "Meta & Resources",
}

# 3.1.b Override patterns: regex on filename + URL beats primary.
# Title is intentionally excluded to avoid matching crawler-generic markers
# like "(v0.8.x)" that appear in every doc title for a versioned doc set.
OVERRIDES: list[tuple[str, int]] = [
    # Bucket 1 — project home / welcome page. Conservative: only file basenames
    # that start with the keyword, so `agent-sdk-overview` (a section overview)
    # stays in its crawler-assigned bucket.
    (r"(?:^|/)(?:welcome|home|about|intro|introduction|readme)(?:[-_.]|$)", 1),
    # Bucket 15 — release notes / changelog. Cover all common shapes:
    #   blog-releases-v0.7.5.md   (versioned with v)
    #   blog-releases-0.7.2.md    (versioned without v)
    #   blog-v1-release.md        (release as suffix segment, requires digit
    #                              before so `blog-tags-release` is excluded)
    #   blog-v1-2-release.md      (multi-segment version + release suffix)
    #   anything-changelog.md, whats-new-*, version-1.0, v1.2.3 in path
    (
        r"release[-_]notes|\breleases?[-_]v?\d|\d[-_]release(?:[-_.]|$)|"
        r"changelog|whats[-_]new|version[-_]|\bv\d+[-_.]\d+",
        15,
    ),
    (r"migration|upgrade[-_]from", 15),
    # Bucket 16 — legal / community / meta pages. Crawler often mislabels these
    # as `reference` (sweeping them into the API bucket) or `guide` (sweeping
    # business pages like /partners into Tutorials).
    (
        r"(?:^|/)(?:privacy|terms|support|pricing|license|legal|community|"
        r"contributing|stats|status|partners?|affiliates?|sponsors?|careers)"
        r"(?:[-_.]|$)",
        16,
    ),
    (r"quickstart|getting[-_]started|^install", 2),
    (r"glossary|cheat[-_]sheet", 14),
    (r"\bfaq\b|troubleshoot|common[-_]errors", 13),
    # Bucket 6 — feature marketing/landing pages. Matches `features-X` filenames
    # and `/features/X` URL paths. Marketing sites are inconsistent about
    # crawler categories for these (some get `concept`, some `guide`); the
    # override unifies them. Placed after quickstart/glossary/faq so something
    # like `features-getting-started.md` still goes to bucket 2.
    (r"(?:^|/)features?(?:[-_/]|$)", 6),
]

# 3.1.c Tertiary keyword → bucket (used only when crawler value unknown)
TERTIARY: list[tuple[int, list[str]]] = [
    (1, ["welcome", "overview", "intro", "readme", "about"]),
    (2, ["quickstart", "install", "setup", "getting-started"]),
    (3, ["tutorial", "guide", "how-to", "walkthrough"]),
    (4, ["concept", "fundamental", "understanding"]),
    (5, ["config", "setting", "customize", "preferences"]),
    (6, ["feature", "capability", "functionality"]),
    (7, ["integrate", "connect", "provider", "plugin"]),
    (8, ["auth", "security", "permission"]),
    (9, ["api", "reference", "sdk", "endpoint"]),
    (10, ["deploy", "operation", "manage", "monitor", "scale"]),
    (11, ["automat", "workflow", "hook", "pipeline"]),
    (12, ["advanced", "expert", "optimize", "performance"]),
    (13, ["trouble", "faq", "error", "fix"]),
    (14, ["glossary", "appendix", "cheat-sheet"]),
    (15, ["changelog", "release", "version", "history"]),
    (16, ["pricing", "license", "legal", "community", "contributing", "privacy", "terms"]),
]


def assign_bucket(doc: dict) -> tuple[int, str]:
    # Overrides operate on filename + URL only. Titles are excluded because crawler
    # titles often carry generic version markers like "(v0.8.x)" that would flood
    # the Changelog bucket with everything that shares a doc-set version label.
    # Strip any existing nnn- numeric prefix so the filename-anchored regexes
    # (e.g. ^welcome) still match on a re-run over an already-numbered folder.
    raw_fp = doc.get("file_path", "")
    fp_unprefixed = _NUM_PREFIX_RE.sub("", raw_fp)
    fp_url = " ".join([fp_unprefixed, doc.get("url", "")]).lower()

    for pattern, bucket in OVERRIDES:
        if re.search(pattern, fp_url):
            return bucket, "override"

    crawler_cat = (doc.get("category") or "").lower().strip()
    if crawler_cat in CRAWLER_TO_BUCKET:
        return CRAWLER_TO_BUCKET[crawler_cat], "primary"

    extended = (
        fp_url
        + " "
        + (doc.get("title") or "").lower()
        + " "
        + (doc.get("summary") or "").lower()
        + " "
        + " ".join(doc.get("tags") or []).lower()
    )
    for bucket, kws in TERTIARY:
        if any(kw in extended for kw in kws):
            return bucket, "tertiary"

    return 16, "fallback"


def order_within_bucket(docs: list[dict]) -> list[dict]:
    """Apply 3.3 ordering rules deterministically."""
    crud = ["list", "get", "create", "update", "delete"]

    def key(d: dict):
        fp = d.get("file_path", "").lower()
        title = (d.get("title") or "").lower()

        # primary: doc class
        if any(w in fp or w in title for w in ("overview", "intro", "welcome")):
            primary = 0
        elif any(
            w in fp or w in title for w in ("quickstart", "getting-started", "install", "setup")
        ):
            primary = 1
        else:
            primary = 5

        # versioned content (newest first). Two passes to handle:
        #   v0.7.5 / 0.7.2  → dot-separated (with or without leading 'v')
        #   v1-2 / v1-2-release / v1-release → hyphen-separated, possibly trailing
        m = re.search(r"v(\d+)(?:[._-](\d+))?(?:[._-](\d+))?", fp)
        if not m:
            m = re.search(r"\b(\d+)\.(\d+)(?:\.(\d+))?", fp)
        if m:
            major = int(m.group(1))
            minor = int(m.group(2)) if m.group(2) else 0
            patch = int(m.group(3)) if m.group(3) else 0
            return (primary, "v", -major, -minor, -patch, fp)

        # week-numbered (whats-new-2026-w15)
        m = re.search(r"(\d{4})-w(\d+)", fp)
        if m:
            return (primary, "w", -int(m.group(1)), -int(m.group(2)), 0, fp)

        # CRUD verbs
        for i, op in enumerate(crud):
            if re.search(rf"\b{op}\b", fp):
                return (primary, "c", i, 0, 0, fp)

        return (primary, "z", 0, 0, 0, fp)

    return sorted(docs, key=key)


_NUM_PREFIX_RE = re.compile(r"^\d{3}-")

# First-level filename segments that are too generic to make a useful
# sub-bucket label on their own ("docs", "blog", ...). When a bucket is
# dominated by one of these, _semantic_prefix descends one level and uses
# the next segment instead, producing meaningful sub-section names.
_GENERIC_FIRST_SEGMENTS = {
    "docs", "doc", "documentation",
    "blog", "post", "posts", "article", "articles",
    "page", "pages",
    "guide", "guides",
}


def _semantic_prefix(fp: str) -> str:
    """Return a meaningful sub-bucket key for a filename (re-run safe).

    Strips any leading nnn- numeric prefix, splits on '-', and returns the
    first segment. When that segment is generic (`docs`, `blog`, `article`,
    ...) and a second segment exists, returns the second segment so the
    sub-bucket carries actual semantic content.
    """
    base = _NUM_PREFIX_RE.sub("", fp)
    if "-" not in base:
        return "misc"
    parts = base.split("-")
    first = parts[0].lower()
    if first in _GENERIC_FIRST_SEGMENTS and len(parts) >= 2:
        second = parts[1].lower()
        # numeric second segment (e.g. `docs-1.5-...`) isn't a useful label —
        # fall back to the third segment when present.
        if re.fullmatch(r"\d+(?:\.\d+)*", second) and len(parts) >= 3:
            return parts[2].split(".")[0].lower()
        return second.split(".")[0]
    return first


def detect_overflow_split(docs: list[dict]) -> list[dict] | None:
    """Split a dominant bucket by filename prefix. Each sub-bucket needs ≥4 docs.

    `misc` is excluded from qualifying as a named sub-bucket: it's the catch-all
    for hyphen-less filenames and humanizes to "Other", so promoting it would
    produce two "Other" headers (the misc group plus the tail group). When the
    only qualifying prefix is `misc`, the bucket renders flat instead.
    """
    groups: dict[str, list[dict]] = {}
    for d in docs:
        fp = d.get("file_path", "")
        prefix = _semantic_prefix(fp)
        groups.setdefault(prefix, []).append(d)
    if len(groups) < 2:
        return None

    sorted_groups = sorted(groups.items(), key=lambda kv: -len(kv[1]))
    sub_buckets: list[dict] = []
    tail: list[dict] = []
    for prefix, items in sorted_groups:
        if prefix != "misc" and len(items) >= 4:
            sub_buckets.append(
                {"prefix": prefix, "docs": order_within_bucket(items)}
            )
        else:
            tail.extend(items)
    if not sub_buckets:
        return None
    if tail:
        sub_buckets.append({"prefix": "other", "docs": order_within_bucket(tail)})
    return sub_buckets


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("metadata", help="Path to metadata.json")
    p.add_argument(
        "--overflow-threshold",
        type=float,
        default=0.25,
        help="Bucket share above which sub-bucketing kicks in (default 0.25)",
    )
    args = p.parse_args()

    md = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
    docs = md.get("documents", [])
    total = len(docs)
    if total == 0:
        print(json.dumps({"error": "no documents"}), file=sys.stderr)
        return 2

    by_bucket: dict[int, list[dict]] = {}
    for d in docs:
        bid, _signal = assign_bucket(d)
        by_bucket.setdefault(bid, []).append(d)

    out_buckets: list[dict] = []
    for bid in sorted(by_bucket.keys()):
        items = by_bucket[bid]
        ordered = order_within_bucket(items)
        bucket: dict = {
            "id": bid,
            "name": BUCKET_NAMES[bid],
            "count": len(ordered),
            "docs": [
                {"file_path": d["file_path"], "title": d.get("title", "")} for d in ordered
            ],
            "sub_buckets": None,
        }
        # Sub-bucket only when the bucket is both proportionally dominant
        # (>overflow_threshold) AND large enough in absolute terms. Splitting
        # 8 docs into 4+4 adds visual scaffolding without navigation value.
        if len(ordered) >= 10 and len(ordered) / total > args.overflow_threshold:
            split = detect_overflow_split(ordered)
            if split:
                bucket["sub_buckets"] = [
                    {
                        "prefix": s["prefix"],
                        "docs": [
                            {"file_path": d["file_path"], "title": d.get("title", "")}
                            for d in s["docs"]
                        ],
                    }
                    for s in split
                ]
        out_buckets.append(bucket)

    print(
        json.dumps(
            {
                "total": total,
                "buckets_used": [b["name"] for b in out_buckets],
                "buckets": out_buckets,
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
