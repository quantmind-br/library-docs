import json
import re
import os
from datetime import datetime

# 1. Load Metadata
with open("metadata.json", "r") as f:
    data = json.load(f)

documents = data.get("documents", [])

# 2. Define Categories and Patterns
# Priority Order 1-16
CATEGORIES = [
    {
        "id": 1,
        "name": "Introduction & Overview",
        "patterns": [
            r"welcome",
            r"overview",
            r"index",
            r"intro",
            r"readme",
            r"about",
            r"home",
            r"start",
        ],
    },
    {
        "id": 2,
        "name": "Quick Start & Installation",
        "patterns": [
            r"quickstart",
            r"quick-start",
            r"install",
            r"setup",
            r"getting-started",
            r"beginner",
            r"get-started",
        ],
    },
    {
        "id": 3,
        "name": "Tutorials & How-To",
        "patterns": [
            r"tutorial",
            r"guide",
            r"how-to",
            r"howto",
            r"learn",
            r"example",
            r"walkthrough",
            r"workshop",
        ],
    },
    {
        "id": 4,
        "name": "Concepts & Fundamentals",
        "patterns": [
            r"concept",
            r"fundamental",
            r"basic",
            r"introduction",
            r"understanding",
            r"explained",
            r"what-is",
            r"core-concept",
        ],
    },
    {
        "id": 5,
        "name": "Configuration & Settings",
        "patterns": [r"config", r"setting", r"customize", r"preferences", r"options"],
    },
    {
        "id": 6,
        "name": "Features & Capabilities",
        "patterns": [r"feature", r"capability", r"what-can", r"functionality"],
    },
    {
        "id": 7,
        "name": "Integration & Connection",
        "patterns": [
            r"integrate",
            r"connect",
            r"provider",
            r"plugin",
            r"extension",
            r"adapter",
        ],
    },
    {
        "id": 8,
        "name": "Authentication & Security",
        "patterns": [
            r"auth",
            r"security",
            r"permission",
            r"access",
            r"login",
            r"user",
            r"account",
            r"sso",
            r"role",
        ],
    },
    {
        "id": 9,
        "name": "API & Reference",
        "patterns": [
            r"api",
            r"reference",
            r"sdk",
            r"library",
            r"endpoint",
            r"method",
            r"cli",
            r"command",
        ],
    },
    {
        "id": 10,
        "name": "Operations & Deployment",
        "patterns": [
            r"deploy",
            r"operation",
            r"run",
            r"execute",
            r"manage",
            r"monitor",
            r"scale",
            r"admin",
        ],
    },
    {
        "id": 11,
        "name": "Automation & Workflow",
        "patterns": [
            r"automat",
            r"workflow",
            r"hook",
            r"trigger",
            r"pipeline",
            r"batch",
            r"ci-cd",
            r"github-action",
        ],
    },
    {
        "id": 12,
        "name": "Advanced Topics",
        "patterns": [
            r"advanced",
            r"expert",
            r"optimize",
            r"performance",
            r"tuning",
            r"deep-dive",
            r"architecture",
        ],
    },
    {
        "id": 13,
        "name": "Troubleshooting & Support",
        "patterns": [
            r"trouble",
            r"faq",
            r"help",
            r"support",
            r"error",
            r"issue",
            r"fix",
        ],
    },
    {
        "id": 14,
        "name": "Reference & Appendix",
        "patterns": [r"glossary", r"appendix", r"cheat-sheet", r"lookup"],
    },
    {
        "id": 15,
        "name": "Changelog & Releases",
        "patterns": [
            r"changelog",
            r"release",
            r"version",
            r"update",
            r"history",
            r"news",
            r"deprecated",
        ],
    },
    {
        "id": 16,
        "name": "Meta & Resources",
        "patterns": [
            r"pricing",
            r"license",
            r"legal",
            r"community",
            r"contributing",
            r"other",
            r"resource",
            r"checklist",
        ],
    },
]


def detect_category(doc):
    # Prepare text for matching
    url_lower = doc.get("url", "").lower()
    title_lower = doc.get("title", "").lower()
    file_path_lower = doc.get("file_path", "").lower()

    # Existing category hint
    existing_cat = doc.get("category", "").lower()

    # Try to match based on Priority Order
    for cat in CATEGORIES:
        for pattern in cat["patterns"]:
            # Check URL segments, Title, and File Path
            if (
                re.search(pattern, url_lower)
                or re.search(pattern, title_lower)
                or re.search(pattern, file_path_lower)
            ):
                return cat

    # Fallback based on existing category if it maps to something?
    # Or just return a default "Other Resources"
    return CATEGORIES[-1]  # Meta & Resources as fallback


# Assign categories
categorized_docs = {cat["id"]: [] for cat in CATEGORIES}

for doc in documents:
    category = detect_category(doc)
    doc["assigned_category_id"] = category["id"]
    doc["assigned_category_name"] = category["name"]
    categorized_docs[category["id"]].append(doc)


# 3. Sort Documents within Categories
def sort_key(doc):
    file_path = doc.get("file_path", "").lower()
    title = doc.get("title", "").lower()

    # 1. Overview/Index/Intro first
    if any(
        x in file_path or x in title
        for x in ["index", "overview", "introduction", "readme", "welcome"]
    ):
        prio = 0
    # 2. Quickstart/Setup second
    elif any(
        x in file_path or x in title
        for x in ["quickstart", "setup", "install", "get-started", "getting-started"]
    ):
        prio = 1
    else:
        prio = 2

    # CRUD for API/CLI (simple heuristic)
    crud_score = 0
    if "list" in file_path or "ls" in file_path:
        crud_score = 1
    elif "get" in file_path or "inspect" in file_path or "read" in file_path:
        crud_score = 2
    elif "create" in file_path or "add" in file_path:
        crud_score = 3
    elif "update" in file_path or "set" in file_path:
        crud_score = 4
    elif "delete" in file_path or "remove" in file_path or "rm" in file_path:
        crud_score = 5

    # Versioning (newest first for changelogs/releases)
    # Extract version numbers if present
    version_match = re.search(r"v?(\d+)\.(\d+)", title)
    version_sort = 0
    if version_match:
        # Inverse for descending sort
        version_sort = -1 * (
            int(version_match.group(1)) * 1000 + int(version_match.group(2))
        )

    return (prio, crud_score, version_sort, file_path)


for cat_id in categorized_docs:
    categorized_docs[cat_id].sort(key=sort_key)

# 4. Generate New Filenames and Rename Map
rename_map = {}  # old -> new
final_docs_list = []
global_counter = 1

sorted_cats = sorted(CATEGORIES, key=lambda x: x["id"])

for cat in sorted_cats:
    docs = categorized_docs[cat["id"]]
    if not docs:
        continue

    for doc in docs:
        old_path = doc["file_path"]
        # Pad with 3 digits, e.g., 001, 010, 100, 1000...
        # Since we have 1200 docs, maybe 4 digits? User said 3 digits (001, 002... 100... etc).
        # But if >999, it fits in 4 digits naturally or overflows?
        # User example: "001-welcome.md".
        # If I have 1206 files, "1206-file.md" works.
        prefix = f"{global_counter:03d}"
        new_path = f"{prefix}-{old_path}"

        rename_map[old_path] = new_path

        # Update doc object
        new_doc = doc.copy()
        new_doc["original_file_path"] = old_path
        new_doc["file_path"] = new_path
        final_docs_list.append(new_doc)

        global_counter += 1

# 5. Generate Rename Script
with open("rename_files.sh", "w") as f:
    f.write("#!/bin/bash\n\n")
    for old, new in rename_map.items():
        # Escape spaces if any (though these filenames seem hyphenated)
        f.write(f'mv "{old}" "{new}"\n')

# 6. Generate Updated Metadata
data["documents"] = final_docs_list
data["organization"] = {
    "method": "sequential-numbering",
    "organized_at": datetime.now().isoformat(),
    "total_files": len(final_docs_list),
    "categories": [c["name"] for c in sorted_cats if categorized_docs[c["id"]]],
}

with open("metadata_updated.json", "w") as f:
    json.dump(data, f, indent=2)

# 7. Generate 000-index.md
index_content = []
index_content.append("---")
index_content.append("description: Auto-generated documentation index")
index_content.append(f"generated: {datetime.now().isoformat()}")
index_content.append(f"source: {data.get('source_url', 'unknown')}")
index_content.append(f"total_docs: {len(final_docs_list)}")
index_content.append(
    f"categories: {len([c for c in sorted_cats if categorized_docs[c['id']]])}"
)
index_content.append("---\n")
index_content.append(f"# {data.get('project_name', 'Project')} Documentation Index\n")
index_content.append(
    "> Organized index for AI agent consumption. Documents follow logical learning sequence.\n"
)

index_content.append("## Metadata Summary\n")
index_content.append("| Property | Value |")
index_content.append("|----------|-------|")
index_content.append(f"| **Source** | {data.get('source_url', 'unknown')} |")
index_content.append(
    f"| **Generated** | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |"
)
index_content.append(f"| **Total Documents** | {len(final_docs_list)} |")
index_content.append("\n---\n")
index_content.append("## Document Index\n")

for cat in sorted_cats:
    docs = categorized_docs[cat["id"]]
    if not docs:
        continue

    first_doc = docs[0]["file_path"].split("-")[0]  # Extract number prefix
    last_doc = docs[-1]["file_path"].split("-")[0]

    index_content.append(f"### {cat['id']}. {cat['name']} ({first_doc}-{last_doc})")
    index_content.append(f"*Category ID: {cat['id']}*")
    index_content.append("\n| # | File | Title | Summary | Keywords |")
    index_content.append("|---|------|-------|---------|----------|")

    for doc in docs:
        num = doc["file_path"].split("-")[0]
        title = doc.get("title", "No Title").replace("|", "\|")
        summary = (
            doc.get("summary", "").replace("|", "\|")[:100] + "..."
            if len(doc.get("summary", "")) > 100
            else doc.get("summary", "")
        )
        tags = (
            ", ".join(doc.get("tags", []))[:50] + "..."
            if len(", ".join(doc.get("tags", []))) > 50
            else ", ".join(doc.get("tags", []))
        )

        index_content.append(
            f"| {num} | `{doc['file_path']}` | {title} | {summary} | {tags} |"
        )

    index_content.append("\n")

# Learning Path (Simplified)
index_content.append("## Learning Path\n")
# We can just reference the first few categories
index_content.append("### Level 1: Foundation")
index_content.append(
    "- Check **Introduction & Overview** and **Quick Start** sections.\n"
)
index_content.append("### Level 2: Core Concepts")
index_content.append("- Study **Concepts & Fundamentals**.\n")
index_content.append("### Level 3: Practice")
index_content.append("- Follow **Tutorials & How-To**.\n")

with open("000-index.md", "w") as f:
    f.write("\n".join(index_content))

print(
    "Processing complete. Created rename_files.sh, metadata_updated.json, and 000-index.md"
)
