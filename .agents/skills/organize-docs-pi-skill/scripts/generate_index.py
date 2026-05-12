#!/usr/bin/env python3
"""Phase 6: Render 000-index.md from metadata.json + bucket plan.

The crawler-emitted `description` field is intentionally ignored — it is
boilerplate. Title/summary/tags drive the per-row content.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

_NUM_PREFIX_RE = re.compile(r"^\d{3}-")
# AP-style mid-title particles. Limited to unambiguous lowercases — `in`/`on`/
# `to` are excluded because they often appear in verb phrases ("Sign On",
# "Log In", "How To") where capitalization reads better.
_TITLE_LOWERCASE_PARTICLES = {"vs", "and", "or", "of", "the", "a", "an"}
# Common technical acronyms that should always be uppercased in titles.
_TITLE_ACRONYMS = {
    "ai", "api", "sdk", "rbac", "sso", "saml", "oidc", "ui", "ux", "cli",
    "css", "html", "json", "yaml", "xml", "csv", "url", "uri", "uuid",
    "paas", "saas", "iaas", "ci", "cd", "vpc", "vpn", "dns", "tcp", "udp",
    "http", "https", "ssh", "ssl", "tls", "ipv4", "ipv6", "ml", "llm",
    "iot", "aws", "gcp", "faq", "mcp", "rpc", "sql", "orm", "jwt", "oauth",
}

BUCKET_DESCRIPTIONS = {
    1: "Welcome, overview, project introduction",
    2: "Installation, setup, and first steps",
    3: "Step-by-step tutorials and how-to guides",
    4: "Core concepts and fundamental principles",
    5: "Configuration, settings, and customization",
    6: "Feature documentation",
    7: "Integration with external systems",
    8: "Authentication, authorization, and security",
    9: "API and SDK reference",
    10: "Deployment, operations, and infrastructure",
    11: "Automation, workflows, and pipelines",
    12: "Advanced topics and optimization",
    13: "Troubleshooting, FAQs, and error handling",
    14: "Glossary, cheat sheets, and reference appendices",
    15: "Release notes, changelogs, and version history",
    16: "Pricing, legal, community, and other resources",
}


def truncate(s: str | None, n: int = 120) -> str:
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def detect_common_suffix(titles: list[str], min_share: float = 0.7, min_len: int = 10) -> str:
    """Find the longest trailing substring shared by ≥ min_share of titles.

    Used to strip crawler boilerplate like " - Crawl4AI Documentation (v0.8.x)"
    that pads almost every title in a doc set. Returns empty string when no
    qualifying suffix exists.

    Algorithm: scan length from min_len upward; at each length pick the most
    common suffix group; stop when no group meets the share threshold; only
    adopt suffixes that start on a separator to avoid mid-word cuts.
    """
    titles = [t for t in titles if t]
    if len(titles) < 4:
        return ""
    threshold = max(2, int(len(titles) * min_share))
    longest_title = max(len(t) for t in titles)
    best = ""
    for length in range(min_len, longest_title + 1):
        groups: dict[str, int] = {}
        for t in titles:
            if len(t) >= length:
                key = t[-length:]
                groups[key] = groups.get(key, 0) + 1
        if not groups:
            break
        suffix, count = max(groups.items(), key=lambda kv: kv[1])
        if count < threshold:
            break
        if suffix and suffix[0] in " -|(":
            best = suffix
    return best


def humanize_sub_bucket(prefix: str) -> str:
    """Convert a raw filename prefix into a friendlier sub-section header."""
    p = (prefix or "").strip().lower()
    special = {
        "other": "Other",
        "misc": "Other",
        "core": "Core",
        "advanced": "Advanced",
        "api": "API",
        "sdk": "SDK",
        "blog": "Blog",
        "extraction": "Extraction",
        "tutorial": "Tutorials",
        "guide": "Guides",
        "reference": "Reference",
    }
    if p in special:
        return special[p]
    return p.replace("-", " ").replace("_", " ").title()


def md_escape_pipe(s: str) -> str:
    return s.replace("|", r"\|")


def number_from_path(fp: str) -> str:
    m = re.match(r"^(\d{3})-", fp)
    return m.group(1) if m else "???"


def slug_to_title(fp: str) -> str:
    """Derive a human-readable title from a filename slug.

    `004-dokploy-vs-caprover.md` → `Dokploy vs Caprover`. Used as a fallback
    when crawler-emitted titles are uninformative (e.g., a marketing site
    that ships the same `<title>` tag on every page).
    """
    base = _NUM_PREFIX_RE.sub("", fp or "")
    if base.endswith(".md"):
        base = base[:-3]
    if not base:
        return ""
    parts = base.replace("_", "-").split("-")
    out: list[str] = []
    for i, p in enumerate(parts):
        if not p:
            continue
        low = p.lower()
        if low in _TITLE_ACRONYMS:
            out.append(low.upper())
        elif i > 0 and low in _TITLE_LOWERCASE_PARTICLES:
            out.append(low)
        else:
            out.append(p[:1].upper() + p[1:].lower())
    return " ".join(out)


def titles_are_uniform(titles: list[str], common_suffix: str, threshold: float = 0.5) -> bool:
    """Detect when crawler titles carry no per-doc information.

    After stripping the detected common suffix, count how many titles collapse
    to the most-frequent value. Above the threshold, the title column would be
    repetitive ("Dokploy" / "Dokploy" / "Dokploy" …) and we should prefer a
    slug-derived display.
    """
    stripped: list[str] = []
    for t in titles:
        t = t or ""
        if common_suffix and t.endswith(common_suffix):
            t = t[: -len(common_suffix)].rstrip(" -|")
        stripped.append(t.strip())
    if not stripped:
        return False
    counts = Counter(stripped)
    _, top_count = counts.most_common(1)[0]
    return top_count / len(stripped) > threshold


def derive_project_name(metadata: dict, fallback: str) -> str:
    src = metadata.get("source_url") or ""
    if src:
        try:
            host = urlparse(src).netloc
            if host:
                return host
        except Exception:
            pass
    return fallback


def render_table(rows: list[str], header: list[str]) -> list[str]:
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(["---"] * len(header)) + "|",
    ]
    out.extend(rows)
    out.append("")
    return out


def row_for(
    doc: dict | None, fp: str, strip_suffix: str = "", use_slug_title: bool = False
) -> str:
    n = number_from_path(fp)
    raw_title = (doc or {}).get("title", "") or ""
    if strip_suffix and raw_title.endswith(strip_suffix):
        raw_title = raw_title[: -len(strip_suffix)].rstrip(" -|")
    if use_slug_title or not raw_title.strip():
        raw_title = slug_to_title(fp)
    title = md_escape_pipe(truncate(raw_title, 80))
    summary = md_escape_pipe(truncate((doc or {}).get("summary", ""), 120))
    tags = ", ".join(((doc or {}).get("tags") or [])[:6])
    return f"| {n} | `{fp}` | {title} | {summary} | {tags} |"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory")
    p.add_argument("--buckets", required=True, help="Path to categorize.py JSON")
    p.add_argument(
        "--project-name",
        default=None,
        help="Override the derived project name in the index title",
    )
    p.add_argument(
        "--output",
        default=None,
        help="Output path (default: <directory>/000-index.md)",
    )
    args = p.parse_args()

    root = Path(args.directory).resolve()
    md = json.loads((root / "metadata.json").read_text(encoding="utf-8"))
    docs = md.get("documents", [])
    by_path = {d["file_path"]: d for d in docs}
    bucket_data = json.loads(Path(args.buckets).read_text(encoding="utf-8"))

    project = args.project_name or derive_project_name(md, root.name)
    source = md.get("source_url") or "—"
    generated = datetime.now(timezone.utc).isoformat()
    titles = [d.get("title", "") or "" for d in docs]
    common_suffix = detect_common_suffix(titles)
    # Marketing/landing-page sets often ship the same <title> on every page.
    # When that happens the title column collapses to a single repeated value
    # and the index becomes unreadable; fall back to slug-derived titles.
    use_slug_title = titles_are_uniform(titles, common_suffix)

    L: list[str] = []
    L.append("---")
    L.append("description: Auto-generated documentation index")
    L.append(f"generated: {generated}")
    L.append(f"source: {source}")
    L.append(f"total_docs: {len(docs)}")
    L.append(f"categories: {len(bucket_data['buckets'])}")
    L.append("---")
    L.append("")
    L.append(f"# {project} Documentation Index")
    L.append("")
    L.append("> Organized for AI agent consumption. Files numbered following a logical learning sequence.")
    L.append("")
    L.append("## Summary")
    L.append("")
    L.append("| Property | Value |")
    L.append("|----------|-------|")
    L.append(f"| Source | {source} |")
    L.append(f"| Generated | {generated} |")
    L.append(f"| Total Documents | {len(docs)} |")
    L.append(f"| Categories | {', '.join(bucket_data['buckets_used'])} |")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Document Index")
    L.append("")

    header = ["#", "File", "Title", "Summary", "Tags"]

    for i, bucket in enumerate(bucket_data["buckets"], 1):
        items_flat: list[dict] = []
        if bucket.get("sub_buckets"):
            for sb in bucket["sub_buckets"]:
                items_flat.extend(sb["docs"])
        else:
            items_flat = bucket["docs"]
        if not items_flat:
            continue

        first_n = number_from_path(items_flat[0]["file_path"])
        last_n = number_from_path(items_flat[-1]["file_path"])
        L.append(f"### {i}. {bucket['name']} ({first_n}–{last_n})")
        L.append(f"*{BUCKET_DESCRIPTIONS.get(bucket['id'], '')}*")
        L.append("")

        if bucket.get("sub_buckets"):
            for sb in bucket["sub_buckets"]:
                if not sb["docs"]:
                    continue
                L.append(f"#### {humanize_sub_bucket(sb['prefix'])}")
                L.append("")
                rows = [
                    row_for(
                        by_path.get(d["file_path"]),
                        d["file_path"],
                        common_suffix,
                        use_slug_title,
                    )
                    for d in sb["docs"]
                ]
                L.extend(render_table(rows, header))
        else:
            rows = [
                row_for(
                    by_path.get(d["file_path"]),
                    d["file_path"],
                    common_suffix,
                    use_slug_title,
                )
                for d in bucket["docs"]
            ]
            L.extend(render_table(rows, header))

    org = md.get("organization", {})
    dropped = org.get("dropped", [])
    if dropped:
        L.append("---")
        L.append("")
        L.append("## Dropped (deduplication)")
        L.append("")
        L.append("| Path | In favor of | Reason |")
        L.append("|------|-------------|--------|")
        for d in dropped:
            L.append(
                f"| `{d.get('path', '')}` | `{d.get('in_favor_of', '')}` | {d.get('reason', '')} |"
            )
        L.append("")

    L.append("---")
    L.append("")
    L.append("*Auto-generated. Files numbered sequentially following a content-driven learning progression.*")
    L.append("")

    out_path = Path(args.output) if args.output else root / "000-index.md"
    out_path.write_text("\n".join(L), encoding="utf-8")

    print(
        json.dumps(
            {
                "index_path": str(out_path),
                "buckets": len(bucket_data["buckets"]),
                "total_docs": len(docs),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
