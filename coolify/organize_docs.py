#!/usr/bin/env python3
"""
Documentation Organizer Script for Coolify Docs
Generates rename mapping, bash script, and updates metadata.json
"""

import json
import os
from datetime import datetime
from collections import OrderedDict

# Read metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

documents = metadata["documents"]

# Define category priority order and URL pattern matching
CATEGORIES = OrderedDict(
    [
        (
            "introduction",
            {
                "priority": 1,
                "name": "Introduction & Overview",
                "patterns": [
                    "introduction",
                    "concepts",
                    "usage",
                    "cloud",
                    "team",
                    "sponsors",
                    "screenshots",
                    "videos",
                    "faq",
                    "overview",
                ],
                "url_patterns": [
                    "/get-started/introduction",
                    "/get-started/concepts",
                    "/get-started/usage",
                    "/get-started/cloud",
                    "/get-started/team",
                    "/get-started/sponsors",
                    "/get-started/screenshots",
                    "/get-started/videos",
                    "/knowledge-base/faq",
                    "/knowledge-base/overview",
                ],
            },
        ),
        (
            "installation",
            {
                "priority": 2,
                "name": "Quick Start & Installation",
                "patterns": ["installation", "uninstallation", "upgrade", "downgrade"],
                "url_patterns": [
                    "/get-started/installation",
                    "/get-started/uninstallation",
                    "/get-started/upgrade",
                    "/get-started/downgrade",
                ],
            },
        ),
        (
            "contribution",
            {
                "priority": 3,
                "name": "Contributing & Development",
                "patterns": ["contribute", "dev"],
                "url_patterns": ["/get-started/contribute/", "/get-started/dev"],
            },
        ),
        (
            "applications",
            {
                "priority": 4,
                "name": "Applications & Frameworks",
                "patterns": [
                    "applications",
                    "django",
                    "jekyll",
                    "laravel",
                    "nextjs",
                    "nuxt",
                    "phoenix",
                    "rails",
                    "symfony",
                    "svelte-kit",
                    "vite",
                    "vuejs",
                    "vitepress",
                ],
                "url_patterns": ["/applications/"],
            },
        ),
        (
            "build-packs",
            {
                "priority": 5,
                "name": "Build Packs",
                "patterns": [
                    "build-packs",
                    "nixpacks",
                    "dockerfile",
                    "docker-compose",
                    "static",
                ],
                "url_patterns": ["/applications/build-packs/"],
            },
        ),
        (
            "cicd",
            {
                "priority": 6,
                "name": "CI/CD & Git Integration",
                "patterns": ["ci-cd", "github", "gitlab", "bitbucket", "gitea"],
                "url_patterns": ["/applications/ci-cd/"],
            },
        ),
        (
            "databases",
            {
                "priority": 7,
                "name": "Databases",
                "patterns": [
                    "databases",
                    "mysql",
                    "mariadb",
                    "postgresql",
                    "mongodb",
                    "redis",
                    "keydb",
                    "dragonfly",
                    "clickhouse",
                    "backups",
                ],
                "url_patterns": ["/databases/"],
            },
        ),
        (
            "services-intro",
            {
                "priority": 8,
                "name": "Services Overview",
                "patterns": [
                    "services-introduction",
                    "services-overview",
                    "services-all",
                ],
                "url_patterns": [
                    "/services/introduction",
                    "/services/overview",
                    "/services/all",
                ],
            },
        ),
        (
            "services",
            {
                "priority": 9,
                "name": "Service Templates",
                "patterns": ["services-"],
                "url_patterns": ["/services/"],
                "exclude": ["introduction", "overview", "all"],
            },
        ),
        (
            "knowledge-base",
            {
                "priority": 10,
                "name": "Knowledge Base",
                "patterns": [
                    "knowledge-base",
                    "destinations",
                    "domains",
                    "environment-variables",
                    "persistent-storage",
                    "docker-compose",
                    "docker-swarm",
                    "proxy-",
                    "s3-",
                    "server-",
                    "how-to-",
                    "oauth",
                    "notifications",
                    "monitoring",
                    "health-checks",
                ],
                "url_patterns": ["/knowledge-base/"],
            },
        ),
        (
            "integrations",
            {
                "priority": 11,
                "name": "Integrations",
                "patterns": ["integrations", "cloudflare"],
                "url_patterns": ["/integrations/"],
            },
        ),
        (
            "troubleshoot",
            {
                "priority": 12,
                "name": "Troubleshooting",
                "patterns": ["troubleshoot"],
                "url_patterns": ["/troubleshoot/"],
            },
        ),
        (
            "api",
            {
                "priority": 13,
                "name": "API Reference",
                "patterns": ["api-reference"],
                "url_patterns": ["/api-reference/"],
            },
        ),
    ]
)


def categorize_document(doc):
    """Determine the category for a document based on its URL and file path."""
    url = doc.get("url", "")
    file_path = doc.get("file_path", "")
    title = doc.get("title", "").lower()

    # Check each category in priority order
    for cat_key, cat_info in CATEGORIES.items():
        # Check URL patterns first
        for url_pattern in cat_info.get("url_patterns", []):
            if url_pattern in url:
                # Check exclusions for services
                if cat_key == "services":
                    excluded = cat_info.get("exclude", [])
                    if any(excl in url for excl in excluded):
                        continue
                return cat_key

        # Check file path patterns
        for pattern in cat_info.get("patterns", []):
            if pattern in file_path.lower():
                # Check exclusions for services
                if cat_key == "services":
                    excluded = cat_info.get("exclude", [])
                    if any(excl in file_path.lower() for excl in excluded):
                        continue
                return cat_key

    return "other"


# Categorize all documents
categorized = {cat: [] for cat in CATEGORIES.keys()}
categorized["other"] = []

for doc in documents:
    cat = categorize_document(doc)
    categorized[cat].append(doc)

# Sort documents within each category
for cat in categorized:
    # Sort by URL path depth and then alphabetically
    categorized[cat].sort(key=lambda x: (len(x["url"].split("/")), x["url"]))

# Generate rename mapping
rename_map = {}
counter = 1

print("# Rename Mapping Generated")
print(f"# Total documents: {len(documents)}\n")

for cat_key, cat_info in CATEGORIES.items():
    if cat_key in categorized and categorized[cat_key]:
        print(f"\n# {cat_info['name']} ({cat_key})")
        for doc in categorized[cat_key]:
            old_name = doc["file_path"]
            # Preserve the original name, just add prefix
            new_name = f"{counter:03d}-{old_name}"
            rename_map[old_name] = new_name
            doc["new_file_path"] = new_name
            doc["original_file_path"] = old_name
            print(f'mv "{old_name}" "{new_name}"')
            counter += 1

# Handle 'other' category
if categorized["other"]:
    print(f"\n# Other Resources")
    for doc in categorized["other"]:
        old_name = doc["file_path"]
        new_name = f"{counter:03d}-{old_name}"
        rename_map[old_name] = new_name
        doc["new_file_path"] = new_name
        doc["original_file_path"] = old_name
        print(f'mv "{old_name}" "{new_name}"')
        counter += 1

# Generate rename bash script
with open("rename_docs.sh", "w") as f:
    f.write("#!/bin/bash\n")
    f.write("# Coolify Documentation Rename Script\n")
    f.write(f"# Generated: {datetime.now().isoformat()}\n")
    f.write("# This script renames documentation files with sequential numbering\n\n")
    f.write('cd "$(dirname "$0")"\n\n')
    f.write('echo "Starting file renames..."\n\n')

    for old_name, new_name in rename_map.items():
        f.write(f'mv "{old_name}" "{new_name}"\n')

    f.write('\necho "Renaming complete!"\n')
    f.write(f'echo "Total files renamed: {len(rename_map)}"\n')

os.chmod("rename_docs.sh", 0o755)

# Save rename mapping to JSON
with open("rename_mapping.json", "w") as f:
    json.dump(rename_map, f, indent=2)

# Generate categories summary
categories_summary = []
for cat_key, cat_info in CATEGORIES.items():
    if cat_key in categorized and categorized[cat_key]:
        categories_summary.append(
            {
                "key": cat_key,
                "name": cat_info["name"],
                "count": len(categorized[cat_key]),
                "priority": cat_info["priority"],
            }
        )

if categorized["other"]:
    categories_summary.append(
        {
            "key": "other",
            "name": "Other Resources",
            "count": len(categorized["other"]),
            "priority": 99,
        }
    )

# Save categorized documents info
with open("categorized_docs.json", "w") as f:
    json.dump(
        {
            "generated_at": datetime.now().isoformat(),
            "total_documents": len(documents),
            "categories": categories_summary,
            "documents": {
                cat: [
                    {
                        "old": d["file_path"],
                        "new": d.get("new_file_path", d["file_path"]),
                        "title": d["title"],
                        "url": d["url"],
                    }
                    for d in docs
                ]
                for cat, docs in categorized.items()
                if docs
            },
        },
        f,
        indent=2,
    )

print(f"\n\n# Summary:")
print(f"# Total documents processed: {len(documents)}")
print(f"# Categories identified: {len([c for c in categorized.values() if c])}")
print(f"# Rename script generated: rename_docs.sh")
print(f"# Rename mapping saved: rename_mapping.json")
print(f"# Categorized info saved: categorized_docs.json")

# Print category breakdown
print("\n# Category Breakdown:")
for cat in categories_summary:
    print(f"#   {cat['priority']}. {cat['name']}: {cat['count']} files")
