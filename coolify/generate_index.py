#!/usr/bin/env python3
"""
Generate comprehensive 000-index.md file for Coolify documentation
"""

import json
from datetime import datetime

# Load data files
with open("categorized_docs.json", "r") as f:
    categorized = json.load(f)

with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Create document lookup by new file path
doc_lookup = {doc["file_path"]: doc for doc in metadata["documents"]}

# Build the index content
lines = []

# Frontmatter
lines.append("---")
lines.append("description: Auto-generated documentation index for Coolify")
lines.append(f"generated: {datetime.now().isoformat()}")
lines.append("source: https://coolify.io/docs/llms.txt")
lines.append(f"total_docs: {categorized['total_documents']}")
lines.append(f"categories: {len(categorized['categories'])}")
lines.append("---")
lines.append("")

# Title
lines.append("# Coolify Documentation Index")
lines.append("")
lines.append(
    "> Organized index for AI agent consumption. Documents follow logical learning sequence."
)
lines.append(
    "> Coolify is an open-source, self-hostable deployment platform (PaaS alternative to Heroku, Vercel, Netlify) using Docker and Traefik."
)
lines.append("")

# Metadata Summary
lines.append("## Metadata Summary")
lines.append("")
lines.append("| Property | Value |")
lines.append("|----------|-------|")
lines.append(f"| **Source** | https://coolify.io/docs/llms.txt |")
lines.append(f"| **Generated** | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |")
lines.append(f"| **Total Documents** | {categorized['total_documents']} |")
lines.append(f"| **Categories** | {len(categorized['categories'])} |")
lines.append(f"| **Organization Method** | Sequential Numbering |")
lines.append("")

# Category Overview
lines.append("## Category Overview")
lines.append("")
lines.append("| # | Category | Files | Range |")
lines.append("|---|----------|-------|-------|")

file_counter = 1
for cat in sorted(categorized["categories"], key=lambda x: x["priority"]):
    start_num = file_counter
    end_num = file_counter + cat["count"] - 1
    range_str = (
        f"{start_num:03d}-{end_num:03d}" if cat["count"] > 1 else f"{start_num:03d}"
    )
    lines.append(
        f"| {cat['priority']} | **{cat['name']}** | {cat['count']} | {range_str} |"
    )
    file_counter += cat["count"]

lines.append("")

# Learning Path
lines.append("## Learning Path")
lines.append("")
lines.append("### Level 1: Foundation (Start Here)")
lines.append(
    "Files 001-032: Introduction to Coolify concepts, cloud vs self-hosted, team, and FAQ"
)
lines.append("")
lines.append("### Level 2: Installation & Setup")
lines.append("Files 033-042: Installation, upgrade, downgrade, and contribution guides")
lines.append("")
lines.append("### Level 3: Core Concepts")
lines.append(
    "Files 043-081: Applications, frameworks, build packs, CI/CD, and databases"
)
lines.append("")
lines.append("### Level 4: Service Templates")
lines.append("Files 082-373: Complete directory of 280+ one-click deployable services")
lines.append("")
lines.append("### Level 5: Advanced Topics")
lines.append(
    "Files 374-436: Knowledge base, proxies, S3, server management, how-to guides"
)
lines.append("")
lines.append("### Level 6: Troubleshooting & Reference")
lines.append(
    "Files 437-443: Troubleshooting guides, API reference, and additional resources"
)
lines.append("")

# Detailed Document Index
lines.append("---")
lines.append("")
lines.append("## Document Index by Category")
lines.append("")

# Process each category
for cat in sorted(categorized["categories"], key=lambda x: x["priority"]):
    cat_key = cat["key"]
    cat_name = cat["name"]
    cat_docs = categorized["documents"].get(cat_key, [])

    if not cat_docs:
        continue

    # Category header with range
    start_doc = cat_docs[0]
    end_doc = cat_docs[-1]
    start_num = int(start_doc["new"].split("-")[0])
    end_num = int(end_doc["new"].split("-")[0])

    lines.append(f"### {cat['priority']}. {cat_name} ({start_num:03d}-{end_num:03d})")
    lines.append("")

    # Table header
    lines.append("| # | File | Title | Source URL |")
    lines.append("|---|------|-------|------------|")

    # Table rows
    for doc in cat_docs:
        file_num = int(doc["new"].split("-")[0])
        file_name = doc["new"]
        title = doc["title"].replace("|", "\\|")[:60]  # Escape pipes and limit length
        url = doc["url"]
        lines.append(f"| {file_num:03d} | `{file_name}` | {title} | [Link]({url}) |")

    lines.append("")

# Quick Reference by Topic
lines.append("---")
lines.append("")
lines.append("## Quick Reference by Topic")
lines.append("")

# Extract topics from tags
topic_ranges = {
    "Getting Started": "001-042",
    "Applications & Frameworks": "043-081",
    "Service Templates": "082-373",
    "Knowledge Base": "374-436",
    "Troubleshooting": "437-443",
}

lines.append("| Topic | File Range |")
lines.append("|-------|------------|")
for topic, range_str in topic_ranges.items():
    lines.append(f"| **{topic}** | {range_str} |")

lines.append("")

# Popular Services Quick Access
lines.append("## Popular Services Quick Access")
lines.append("")
lines.append("Common services frequently referenced:")
lines.append("")

popular_services = [
    ("NextCloud", "015"),
    ("WordPress", "371"),
    ("Gitea", "078"),
    ("GitLab", "080"),
    ("Ghost", "178"),
    ("Plex", "291"),
    ("Jellyfin", "203"),
    ("Vaultwarden", "358"),
    ("Uptime Kuma", "356"),
    ("Pi-hole", "287"),
]

lines.append("| Service | File | Service | File |")
lines.append("|---------|------|---------|------|")
for i in range(0, len(popular_services), 2):
    svc1 = popular_services[i]
    svc2 = popular_services[i + 1] if i + 1 < len(popular_services) else ("", "")
    lines.append(f"| {svc1[0]} | {svc1[1]} | {svc2[0]} | {svc2[1]} |")

lines.append("")

# Database Services
lines.append("## Database Services")
lines.append("")
lines.append("| Database | File |")
lines.append("|----------|------|")
db_services = [
    ("MySQL", "089"),
    ("MariaDB", "087"),
    ("PostgreSQL", "090"),
    ("MongoDB", "088"),
    ("Redis", "091"),
    ("KeyDB", "086"),
]
for db, num in db_services:
    lines.append(f"| {db} | {num} |")

lines.append("")

# Footer
lines.append("---")
lines.append("")
lines.append(
    "*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*"
)
lines.append("")
lines.append(
    "*For the complete metadata including tags, summaries, and descriptions, refer to `metadata.json`.*"
)

# Write the index file
with open("000-index.md", "w") as f:
    f.write("\n".join(lines))

print("Generated 000-index.md with comprehensive navigation")
print(f"Total categories: {len(categorized['categories'])}")
print(f"Total documents indexed: {categorized['total_documents']}")
