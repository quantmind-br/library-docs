#!/usr/bin/env python3
"""
Organize Moodle Developer Documentation
"""
import json
import os
import re
from datetime import datetime
from pathlib import Path

# Configuration
DOCS_DIR = Path("/Users/diogo/dev/library-docs/moodle")
METADATA_FILE = DOCS_DIR / "metadata.json"

# Category order (logical learning sequence)
CATEGORY_ORDER = {
    "gettingstarted": 1,
    "guides": 2,
    "apis": 3,
    "category": 4,
    "tags": 5,
    "devupdate": 6,
}

# Version order (newest first)
VERSION_ORDER = {"4.5": 1, "4.4": 2, "4.1": 3}

def extract_version_category(url):
    """Extract version and category from URL."""
    match = re.match(r"https://moodledev\.io/docs/(\d+\.\d+)/(\w+)", url)
    if match:
        return match.group(1), match.group(2)
    return None, None

def get_sort_key(doc):
    """Generate sort key for a document."""
    url = doc.get("url", "")

    # Root level docs (search, versions, etc.)
    if "/docs/" not in url:
        if "search" in url:
            return (0, 0, 0, 0, doc.get("file_path", ""))
        if "versions" in url:
            return (0, 0, 1, 0, doc.get("file_path", ""))
        return (0, 0, 2, 0, doc.get("file_path", ""))

    # Versioned docs
    version, category = extract_version_category(url)
    if not version:
        return (99, 99, 99, 0, doc.get("file_path", ""))

    version_rank = VERSION_ORDER.get(version, 99)
    category_rank = CATEGORY_ORDER.get(category, 99)

    # Extract additional path for sorting within category
    path_parts = url.replace(f"https://moodledev.io/docs/{version}/{category}/", "").split("/")
    subpath = "/".join(path_parts) if path_parts else ""

    return (version_rank, category_rank, 0, subpath, doc.get("file_path", ""))

def organize_documents():
    """Organize documents and return sorted list with new paths."""
    print("Loading metadata...")
    with open(METADATA_FILE, "r") as f:
        metadata = json.load(f)

    documents = metadata.get("documents", [])
    print(f"Found {len(documents)} documents")

    # Sort documents
    print("Sorting documents...")
    sorted_docs = sorted(documents, key=get_sort_key)

    # Generate new file paths
    print("Generating sequential numbering...")
    rename_map = {}
    organized_docs = []
    current_num = 1

    for doc in sorted_docs:
        original_path = doc.get("file_path", "")

        # Generate new filename
        new_filename = f"{current_num:04d}-{original_path}"
        rename_map[original_path] = new_filename

        # Update document
        doc["original_file_path"] = original_path
        doc["file_path"] = new_filename
        organized_docs.append(doc)

        current_num += 1

    print(f"Generated {len(rename_map)} file mappings")

    # Update metadata
    metadata["documents"] = organized_docs
    metadata["organization"] = {
        "method": "sequential-numbering",
        "organized_at": datetime.utcnow().isoformat() + "Z",
        "total_files": len(organized_docs),
        "categories": list(CATEGORY_ORDER.keys()),
        "versions": list(VERSION_ORDER.keys())
    }

    # Write updated metadata
    print("Writing updated metadata...")
    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f, indent=2)

    print("Metadata updated successfully")

    return rename_map, organized_docs

def generate_rename_script(rename_map):
    """Generate bash script for renaming files."""
    script = ["#!/bin/bash"]
    script.append(f'cd "{DOCS_DIR}"')
    script.append("")
    script.append("# Rename files to sequential numbering")

    for old, new in rename_map.items():
        if old != new:  # Only rename if different
            script.append(f'mv "{old}" "{new}"')

    script_path = DOCS_DIR / "rename_files.sh"
    with open(script_path, "w") as f:
        f.write("\n".join(script))
    os.chmod(script_path, 0o755)
    print(f"Generated rename script: {script_path}")

def generate_index(organized_docs):
    """Generate 000-index.md file."""
    print("Generating index file...")

    # Group by version and category
    groups = {}
    for doc in organized_docs:
        url = doc.get("url", "")
        version, category = extract_version_category(url)

        if not version:
            key = f"root"
        else:
            key = f"{version}-{category}"

        if key not in groups:
            groups[key] = []
        groups[key].append(doc)

    # Build index content
    lines = []
    lines.append("---")
    lines.append("description: Auto-generated documentation index for Moodle Developer Resources")
    lines.append(f"generated: {datetime.utcnow().isoformat()}Z")
    lines.append("source: https://moodledev.io/sitemap.xml")
    lines.append(f"total_docs: {len(organized_docs)}")
    lines.append(f"categories: {len(CATEGORY_ORDER)}")
    lines.append("---")
    lines.append("")
    lines.append("# Moodle Developer Documentation Index")
    lines.append("")
    lines.append("> Organized index for AI agent consumption. Documents follow logical learning sequence.")
    lines.append("")
    lines.append("## Metadata Summary")
    lines.append("")
    lines.append("| Property | Value |")
    lines.append("|----------|-------|")
    lines.append("| **Source** | https://moodledev.io |")
    lines.append(f"| **Generated** | {datetime.utcnow().isoformat()}Z |")
    lines.append(f"| **Total Documents** | {len(organized_docs)} |")
    lines.append(f"| **Versions** | 4.5, 4.4, 4.1 |")
    lines.append(f"| **Categories** | {', '.join(CATEGORY_ORDER.keys())} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Document Index")
    lines.append("")

    # Sort groups
    sorted_groups = sorted(groups.items(), key=lambda x: (
        VERSION_ORDER.get(x[0].split("-")[0], 99) if "-" in x[0] else 0,
        CATEGORY_ORDER.get(x[0].split("-")[-1], 99) if "-" in x[0] else 0
    ))

    for group_key, docs in sorted_groups:
        group_name = group_key.replace("-", " / ").title()
        first_num = int(docs[0]["file_path"].split("-")[0])
        last_num = int(docs[-1]["file_path"].split("-")[0])

        lines.append(f"### {group_name} ({first_num:04d}-{last_num:04d})")
        lines.append("")
        lines.append(f"*{len(docs)} documents*")
        lines.append("")
        lines.append("| # | File | Title | Summary |")
        lines.append("|---|------|-------|---------|")

        for doc in docs[:20]:  # Limit to first 20 per group for readability
            num = doc["file_path"].split("-")[0]
            filename = doc["file_path"]
            title = doc.get("title", "N/A")[:60]
            summary = doc.get("summary", "N/A")[:80]
            lines.append(f"| {num} | `{filename}` | {title} | {summary} |")

        if len(docs) > 20:
            lines.append(f"| ... | ... | ... | ({len(docs) - 20} more documents) |")

        lines.append("")

    # Quick reference
    lines.append("## Quick Reference")
    lines.append("")
    lines.append("### By Version")
    lines.append("")
    lines.append("| Version | Files |")
    lines.append("|---------|-------|")
    for version in ["4.5", "4.4", "4.1"]:
        version_docs = [d for d in organized_docs if f"/docs/{version}/" in d.get("url", "")]
        if version_docs:
            first = int(version_docs[0]["file_path"].split("-")[0])
            last = int(version_docs[-1]["file_path"].split("-")[0])
            lines.append(f"| {version} | {first:04d}-{last:04d} |")
    lines.append("")

    # Learning path
    lines.append("## Learning Path")
    lines.append("")
    lines.append("### Level 1: Getting Started")
    lines.append("- Files **0001-XXXX** for introduction and quick start")
    lines.append("")
    lines.append("### Level 2: Guides")
    lines.append("- Files **XXXX-XXXX** for tutorials and how-to guides")
    lines.append("")
    lines.append("### Level 3: APIs & Core")
    lines.append("- Files **XXXX-XXXX** for API references and core subsystems")
    lines.append("")
    lines.append("### Level 4: Plugin Types")
    lines.append("- Files **XXXX-XXXX** for plugin development")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*This index is auto-generated and optimized for AI agent search.*")

    index_path = DOCS_DIR / "000-index.md"
    with open(index_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Generated index: {index_path}")

if __name__ == "__main__":
    rename_map, organized_docs = organize_documents()
    generate_rename_script(rename_map)
    generate_index(organized_docs)
    print("\nOrganization complete!")
    print(f"Run './rename_files.sh' to rename all files")
