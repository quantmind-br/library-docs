#!/usr/bin/env python3
"""
LiteLLM Documentation Organization Script
Organizes 732 documentation files into logical learning sequence
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def load_metadata():
    """Load metadata.json file"""
    with open("metadata.json", "r") as f:
        return json.load(f)


def categorize_document(doc):
    """
    Enhanced categorization based on URL, title, and existing category
    Returns: (priority, category_name, subcategory)
    """
    url = doc.get("url", "").lower()
    title = doc.get("title", "").lower()
    existing_cat = doc.get("category", "")

    # Priority 1: Introduction & Overview
    if any(
        p in url
        for p in [
            "index",
            "readme",
            "welcome",
            "home",
            "getting-started",
            "getting_started",
        ]
    ):
        if "overview" in url or "intro" in url:
            return (1, "Introduction & Overview", "Getting Started")
        return (2, "Quick Start & Installation", "Setup Guides")

    # Priority 2: Tutorials (should come early for learning)
    if existing_cat == "Tutorials" or "tutorial" in url:
        # Specialized tutorial ordering
        if any(p in url for p in ["quickstart", "quick_start", "docker"]):
            return (3, "Quick Start & Installation", "Docker Setup")
        if any(p in url for p in ["proxy", "server"]):
            return (4, "Proxy Server Setup", "Server Configuration")
        if "first" in url or "beginner" in url:
            return (5, "Getting Started Tutorials", "Beginner Guides")
        return (6, "Tutorials & How-To Guides", "Integration Tutorials")

    # Priority 3: Concepts & Fundamentals
    if any(
        p in url
        for p in [
            "concept",
            "fundamental",
            "explained",
            "understanding",
            "introduction",
        ]
    ):
        return (7, "Concepts & Fundamentals", "Core Concepts")

    # Priority 4: Configuration
    if any(p in url for p in ["config", "setting", "customize", "environment"]):
        return (8, "Configuration & Settings", "Setup")

    # Priority 5: API & Endpoints (alphabetical by endpoint)
    if url.startswith("/") or "endpoint" in url or "api" in url:
        # Special endpoint ordering
        if any(p in url for p in ["/completions", "/chat"]):
            return (10, "API Reference", "Core Endpoints")
        if "/audio" in url:
            return (11, "API Reference", "Audio APIs")
        if "/batches" in url:
            return (12, "API Reference", "Batch Processing")
        if "/fine_tuning" in url:
            return (13, "API Reference", "Fine Tuning")
        if "/images" in url:
            return (14, "API Reference", "Image APIs")
        if "/videos" in url:
            return (15, "API Reference", "Video APIs")
        return (16, "API Reference", "Additional Endpoints")

    # Priority 6: Provider Integrations
    if "provider" in url or "integration" in url:
        if "observability" in url:
            return (17, "Observability Integrations", "Monitoring")
        if "proxy" in url:
            return (18, "Proxy Configuration", "Server Setup")
        return (19, "Provider Integrations", "Model Providers")

    # Priority 7: Observability
    if any(p in url for p in ["observability", "logging", "monitoring", "tracking"]):
        return (20, "Observability & Monitoring", "Logs & Metrics")

    # Priority 8: Authentication & Security
    if any(
        p in url for p in ["auth", "security", "guardrail", "permission", "credential"]
    ):
        return (21, "Authentication & Security", "Security Features")

    # Priority 9: Proxy Specific
    if "proxy" in url:
        if "ui" in url:
            return (22, "Proxy UI & Dashboard", "User Interface")
        if "deploy" in url or "production" in url:
            return (23, "Deployment & Operations", "Production")
        return (24, "Proxy Server", "Configuration")

    # Priority 10: Advanced Topics
    if any(p in url for p in ["advanced", "optimize", "performance", "tuning"]):
        return (25, "Advanced Topics", "Performance")

    # Priority 11: Reference
    if existing_cat == "Reference" or "reference" in url:
        return (26, "Reference Documentation", "API Reference")

    # Priority 12: Explanation
    if existing_cat == "Explanation":
        return (27, "Concepts & Explanation", "Deep Dives")

    # Priority 13: Changelog
    if any(p in url for p in ["changelog", "release", "version", "update"]):
        return (28, "Changelog & Releases", "Version History")

    # Default
    return (30, "Other Resources", "Additional")


def sort_key(doc):
    """
    Generate sort key for document
    Returns tuple: (priority, url_depth, alphabetical_title)
    """
    priority, main_cat, sub_cat = categorize_document(doc)

    url = doc.get("url", "")
    url_depth = url.count("/")

    # Extract title for alphabetical sorting
    title = doc.get("title", "").lower()

    # For API endpoints, maintain CRUD order
    if "/completions" in url:
        endpoint_priority = 0
    elif "/chat" in url:
        endpoint_priority = 1
    elif "/embeddings" in url:
        endpoint_priority = 2
    elif "/models" in url:
        endpoint_priority = 3
    else:
        endpoint_priority = 10

    return (priority, endpoint_priority, url_depth, title)


def organize_documents(metadata):
    """
    Organize documents into logical order
    Returns list of documents with new file numbers
    """
    documents = metadata.get("documents", [])

    # Sort documents using the sort key
    sorted_docs = sorted(documents, key=sort_key)

    # Assign new sequential numbers
    for idx, doc in enumerate(sorted_docs, start=1):
        # Preserve original file_path
        if "original_file_path" not in doc:
            doc["original_file_path"] = doc["file_path"]

        # Extract original filename without number prefix
        old_path = doc["file_path"]
        # Remove existing number prefix if present
        match = re.match(r"^\d+-(.+)$", old_path)
        if match:
            original_name = match.group(1)
        else:
            original_name = old_path

        # Create new numbered filename
        new_filename = f"{idx:03d}-{original_name}"
        doc["file_path"] = new_filename

    return sorted_docs


def generate_index(metadata, sorted_docs):
    """
    Generate 000-index.md content
    """
    # Group by category
    categories = defaultdict(list)
    for doc in sorted_docs:
        priority, main_cat, sub_cat = categorize_document(doc)
        categories[(main_cat, sub_cat)].append(doc)

    # Build content
    lines = []
    lines.append("# LiteLLM Documentation Index")
    lines.append("")
    lines.append(
        "> Organized index for AI agent consumption. Documents follow logical learning sequence."
    )
    lines.append("")
    lines.append("## Metadata Summary")
    lines.append("")
    lines.append("| Property | Value |")
    lines.append("|----------|-------|")
    lines.append(f"| **Source** | {metadata.get('source_url', 'N/A')} |")
    lines.append(f"| **Generated** | {metadata.get('generated_at', 'N/A')} |")
    lines.append(f"| **Total Documents** | {len(sorted_docs)} |")
    lines.append(f"| **Strategy** | {metadata.get('strategy', 'N/A')} |")
    lines.append(f"| **Organized** | {datetime.utcnow().isoformat()}Z |")
    lines.append("")

    # Main categories sorted by priority
    sorted_categories = sorted(
        categories.items(), key=lambda x: min(sort_key(d)[0] for d in x[1])
    )

    current_num = 1
    category_ranges = {}

    for (main_cat, sub_cat), docs in sorted_categories:
        if not docs:
            continue

        start_num = current_num
        end_num = current_num + len(docs) - 1

        # Build category section
        lines.append(f"### {main_cat}")
        if sub_cat != main_cat:
            lines.append(f"**{sub_cat}** ({start_num:03d}-{end_num:03d})")
        else:
            lines.append(f"({start_num:03d}-{end_num:03d})")
        lines.append("")

        # Table header
        lines.append("| # | File | Title | Summary | Tags |")
        lines.append("|---|------|-------|---------|------|")

        for doc in docs:
            file_num = current_num
            filename = doc["file_path"]
            title = doc.get("title", "N/A")[:60]  # Truncate long titles
            summary = doc.get("summary", "N/A")[:80]  # Truncate long summaries
            tags = ", ".join(doc.get("tags", [])[:5])  # First 5 tags

            lines.append(
                f"| {file_num:03d} | `{filename}` | {title} | {summary} | {tags} |"
            )
            current_num += 1

        lines.append("")

        # Store range for quick reference
        category_ranges[main_cat] = f"{start_num:03d}-{end_num:03d}"

    # Learning Path section
    lines.append("---")
    lines.append("")
    lines.append("## Learning Path")
    lines.append("")
    lines.append("### Level 1: Foundation (Start Here)")
    lines.append(f"- Read files **001-050** for introduction and getting started")
    lines.append(f"- Complete files **051-100** for setup and configuration")
    lines.append("")
    lines.append("### Level 2: Core Understanding")
    lines.append(f"- Learn concepts from files **101-200**")
    lines.append(f"- Understand API endpoints from files **201-300**")
    lines.append("")
    lines.append("### Level 3: Practical Application")
    lines.append(f"- Follow tutorials in files **301-400**")
    lines.append(f"- Explore integrations in files **401-500**")
    lines.append("")
    lines.append("### Level 4: Advanced Usage")
    lines.append(f"- Master advanced topics from files **501-600**")
    lines.append(f"- Implement observability in files **601-650**")
    lines.append("")
    lines.append("### Level 5: Reference & Support")
    lines.append(f"- Consult reference docs **651-700**")
    lines.append(f"- Review changelog in files **701-732**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*"
    )

    return "\n".join(lines)


def create_rename_script(sorted_docs):
    """
    Create bash script to rename files
    """
    lines = ["#!/bin/bash", "", "cd /home/diogo/dev/library-docs/litellm", ""]

    for doc in sorted_docs:
        old_name = doc.get("original_file_path", doc["file_path"])
        new_name = doc["file_path"]

        if old_name != new_name:
            lines.append(f'mv "{old_name}" "{new_name}"')

    return "\n".join(lines)


def main():
    print("Loading metadata...")
    metadata = load_metadata()

    print("Organizing documents...")
    sorted_docs = organize_documents(metadata)

    print("Updating metadata.json...")
    metadata["documents"] = sorted_docs
    metadata["organization"] = {
        "method": "sequential-numbering",
        "organized_at": datetime.utcnow().isoformat() + "Z",
        "total_files": len(sorted_docs),
        "categories": list(set(d.get("category", "Unknown") for d in sorted_docs)),
    }

    # Write updated metadata
    with open("metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print("Generating index...")
    index_content = generate_index(metadata, sorted_docs)

    with open("000-index.md", "w") as f:
        f.write(index_content)

    print("Creating rename script...")
    rename_script = create_rename_script(sorted_docs)

    with open("/tmp/rename_docs.sh", "w") as f:
        f.write(rename_script)

    print(f"\n✓ Organized {len(sorted_docs)} documents")
    print(f"✓ Updated metadata.json")
    print(f"✓ Created 000-index.md")
    print(f"✓ Created rename script at /tmp/rename_docs.sh")
    print(f"\nTo rename files, run:")
    print(f"  bash /tmp/rename_docs.sh")


if __name__ == "__main__":
    main()
