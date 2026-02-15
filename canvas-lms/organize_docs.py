#!/usr/bin/env python3
"""
Organize Canvas LMS documentation files from repodocs-go extraction.
Creates sequential numbering, updates metadata, and generates index.
"""

import json
import os
import re
from datetime import datetime
from collections import defaultdict

# Load metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

documents = metadata["documents"]
print(f"Total documents: {len(documents)}")

# Define category priority order (logical learning sequence)
CATEGORY_PRIORITY = {
    "introduction": 1,
    "overview": 1,
    "getting-started": 2,
    "quickstart": 2,
    "tutorial": 3,
    "guide": 4,
    "concept": 5,
    "configuration": 6,
    "api": 7,
    "reference": 8,
    "other": 9,
}

# Service detection patterns
SERVICE_PATTERNS = {
    "canvas": [
        "canvas",
        "lti",
        "oauth2",
        "permissions",
        "resources",
        "external-tools",
        "data-services",
    ],
    "dap": ["dap", "data-access-platform"],
    "catalog": ["catalog", "waitlist", "programs", "certificates"],
    "commons": ["commons", "conversations"],
    "datasync": ["datasync", "grades-oas", "interop"],
    "parchment": ["parchment", "digital-badges"],
    "studio": ["studio", "media", "captions"],
    "ab-connect": ["ab-connect", "academic-benchmarks"],
    "quizzes": ["quizzes", "new-quizzes"],
    "general": ["index", "services", "get-started"],
}


def detect_service(url_path):
    """Detect which service a document belongs to."""
    url_lower = url_path.lower()

    for service, patterns in SERVICE_PATTERNS.items():
        for pattern in patterns:
            if pattern in url_lower:
                return service
    return "general"


def categorize_document(doc):
    """
    Categorize document based on URL path, title, and existing category.
    Returns: (main_category, subcategory, priority)
    """
    url = doc.get("url", "")
    title = doc.get("title", "").lower()
    file_path = doc.get("file_path", "")
    existing_category = doc.get("category", "other")

    # Detect service
    service = detect_service(url)

    # Priority detection based on URL patterns
    url_lower = url.lower()

    # Introduction/Overview detection
    if any(
        x in url_lower
        for x in ["/index", "/welcome", "/overview", "/introduction", "/readme"]
    ):
        if "index" in file_path.lower() or "get-started" in file_path.lower():
            return ("introduction", service, 1)
        return ("overview", service, 2)

    # Getting Started / Quick Start
    if any(
        x in url_lower
        for x in ["getting-started", "quickstart", "quick-start", "beginner"]
    ):
        return ("getting-started", service, 3)

    # Authentication / Security
    if any(
        x in url_lower
        for x in ["oauth", "authentication", "security", "login", "permissions"]
    ):
        return ("authentication", service, 4)

    # Concepts / Fundamentals
    if any(
        x in url_lower for x in ["concept", "fundamental", "key-concepts", "basics"]
    ):
        return ("concepts", service, 5)

    # Tutorials / How-To
    if any(
        x in url_lower
        for x in ["tutorial", "how-to", "howto", "walkthrough", "example"]
    ):
        return ("tutorials", service, 6)

    # Configuration
    if any(x in url_lower for x in ["config", "setup", "settings", "customize"]):
        return ("configuration", service, 7)

    # API Reference (endpoints)
    if existing_category == "api" or "resources" in url_lower:
        return ("api-reference", service, 8)

    # Guides
    if existing_category == "guide":
        return ("guides", service, 9)

    # Live Events / Data Services
    if any(x in url_lower for x in ["live-events", "data-service", "event-format"]):
        return ("data-services", service, 10)

    # Reference documentation
    if existing_category == "reference":
        return ("reference", service, 11)

    # SIS / Imports
    if any(x in url_lower for x in ["sis", "import", "csv"]):
        return ("sis-integration", service, 12)

    # CLI / Tools
    if any(x in url_lower for x in ["cli", "command-line", "dap-cli"]):
        return ("cli-tools", service, 13)

    # Changelog / Release notes
    if any(x in url_lower for x in ["changelog", "release", "version", "history"]):
        return ("changelog", service, 14)

    # Default to reference
    return ("reference", service, 15)


# Process all documents
processed_docs = []
for doc in documents:
    main_cat, sub_cat, priority = categorize_document(doc)
    processed_docs.append(
        {**doc, "main_category": main_cat, "subcategory": sub_cat, "priority": priority}
    )

# Sort documents: by priority, then by service, then by URL path
processed_docs.sort(key=lambda x: (x["priority"], x["subcategory"], x.get("url", "")))

# Group by main category for reporting
by_category = defaultdict(list)
for doc in processed_docs:
    by_category[doc["main_category"]].append(doc)

print("\n=== Categories Identified ===")
for cat in sorted(
    by_category.keys(),
    key=lambda x: (
        processed_docs[[d["main_category"] for d in processed_docs].index(x)][
            "priority"
        ]
        if x in [d["main_category"] for d in processed_docs]
        else 99
    ),
):
    docs = by_category[cat]
    print(f"  {cat}: {len(docs)} documents")

# Group by service for reporting
by_service = defaultdict(list)
for doc in processed_docs:
    by_service[doc["subcategory"]].append(doc)

print("\n=== Services Identified ===")
for svc in sorted(by_service.keys()):
    docs = by_service[svc]
    print(f"  {svc}: {len(docs)} documents")

# Create rename mapping
rename_map = {}
counter = 1

for doc in processed_docs:
    old_path = doc["file_path"]

    # Create new filename with 3-digit prefix
    new_name = f"{counter:03d}-{old_path}"
    rename_map[old_path] = new_name

    counter += 1

print(f"\n=== Rename Mapping Created ===")
print(f"Total mappings: {len(rename_map)}")
print(f"First 5 examples:")
for i, (old, new) in enumerate(list(rename_map.items())[:5]):
    print(f"  {old} -> {new}")

# Save rename mapping
with open("rename_map.json", "w") as f:
    json.dump(rename_map, f, indent=2)

print("\nSaved rename_map.json")

# Create bash rename script
with open("rename_files.sh", "w") as f:
    f.write("#!/bin/bash\n")
    f.write("# Auto-generated rename script\n")
    f.write("# Generated: {}\n\n".format(datetime.now().isoformat()))
    f.write("set -e\n\n")
    f.write("echo 'Renaming documentation files...'\n\n")

    for old_name, new_name in rename_map.items():
        if os.path.exists(old_name):
            f.write(f'if [ -f "{old_name}" ]; then\n')
            f.write(f'  mv "{old_name}" "{new_name}"\n')
            f.write(f'  echo "  Renamed: {old_name} -> {new_name}"\n')
            f.write(f"else\n")
            f.write(f'  echo "  WARNING: File not found: {old_name}"\n')
            f.write(f"fi\n")

    f.write("\necho 'Rename complete!'\n")

os.chmod("rename_files.sh", 0o755)
print("Saved rename_files.sh")

# Update metadata with new paths and organization info
updated_documents = []
for doc in processed_docs:
    old_path = doc["file_path"]
    new_path = rename_map.get(old_path, old_path)

    updated_doc = {
        **doc,
        "file_path": new_path,
        "original_file_path": old_path,
        "category_group": doc["main_category"],
        "service": doc["subcategory"],
    }
    # Remove temporary fields
    del updated_doc["main_category"]
    del updated_doc["subcategory"]
    del updated_doc["priority"]

    updated_documents.append(updated_doc)

# Create updated metadata
updated_metadata = {
    **metadata,
    "documents": updated_documents,
    "organization": {
        "method": "sequential-numbering-by-category",
        "organized_at": datetime.now().isoformat(),
        "total_files": len(updated_documents),
        "categories": list(by_category.keys()),
        "services": list(by_service.keys()),
        "file_pattern": "NNN-original-name.md",
    },
}

# Save updated metadata
with open("metadata.json", "w") as f:
    json.dump(updated_metadata, f, indent=2)

print("\nUpdated metadata.json")

# Generate index markdown
index_content = f"""---
description: Auto-generated documentation index for Canvas LMS
generated: {datetime.now().isoformat()}
source: https://developerdocs.instructure.com
total_docs: {len(updated_documents)}
categories: {len(by_category)}
services: {len(by_service)}
---

# Canvas LMS Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from introduction to advanced topics.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://developerdocs.instructure.com |
| **Generated** | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} |
| **Total Documents** | {len(updated_documents)} |
| **Categories** | {len(by_category)} |
| **Services** | {len(by_service)} |
| **Organization** | Sequential numbering by category |

---

## Quick Navigation

### By Category

| # | Category | Document Range | Count |
|---|----------|----------------|-------|
"""

# Calculate ranges for each category
current_num = 1
for cat in sorted(
    by_category.keys(),
    key=lambda x: min(d["priority"] for d in processed_docs if d["main_category"] == x),
):
    docs_in_cat = by_category[cat]
    start_num = current_num
    end_num = current_num + len(docs_in_cat) - 1
    current_num = end_num + 1
    index_content += f"| {docs_in_cat[0]['priority']} | {cat.replace('-', ' ').title()} | {start_num:03d}-{end_num:03d} | {len(docs_in_cat)} |\n"

index_content += """
### By Service

| Service | Document Count |
|---------|----------------|
"""

for svc in sorted(by_service.keys()):
    count = len(by_service[svc])
    index_content += f"| {svc.replace('-', ' ').title()} | {count} |\n"

index_content += """
---

## Document Index

"""

# Add detailed sections for each category
current_num = 1
for cat in sorted(
    by_category.keys(),
    key=lambda x: min(d["priority"] for d in processed_docs if d["main_category"] == x),
):
    docs_in_cat = by_category[cat]
    start_num = current_num
    end_num = current_num + len(docs_in_cat) - 1

    index_content += f"""### {docs_in_cat[0]["priority"]}. {cat.replace("-", " ").title()} ({start_num:03d}-{end_num:03d})

"""

    # Add description based on category
    descriptions = {
        "introduction": "Welcome and overview documents to get started with Canvas LMS.",
        "overview": "High-level overview of Canvas LMS services and capabilities.",
        "getting-started": "Quick start guides and initial setup instructions.",
        "authentication": "Authentication, OAuth2, and security documentation.",
        "concepts": "Core concepts and fundamental understanding of Canvas architecture.",
        "tutorials": "Step-by-step tutorials and how-to guides.",
        "configuration": "Configuration options and settings documentation.",
        "api-reference": "Complete API reference for all Canvas LMS endpoints.",
        "guides": "Implementation guides and best practices.",
        "data-services": "Live events, data services, and event format documentation.",
        "reference": "Reference documentation for permissions, file formats, and schemas.",
        "sis-integration": "Student Information System integration and import documentation.",
        "cli-tools": "Command-line tools and DAP CLI reference.",
        "changelog": "Release notes, changelogs, and version history.",
    }

    index_content += f"*{descriptions.get(cat, f'Documentation for {cat}.')}*\n\n"
    index_content += "| # | File | Title | Summary | Service |\n"
    index_content += "|---|------|-------|---------|---------|\n"

    for doc in docs_in_cat:
        file_num = current_num
        file_name = rename_map.get(doc["file_path"], doc["file_path"])
        title = doc.get("title", "Untitled").replace("|", "\\|")[:50]
        summary = (
            doc.get("summary", "No summary")[:60].replace("|", "\\|").replace("\n", " ")
        )
        service = doc["subcategory"]

        index_content += (
            f"| {file_num:03d} | `{file_name}` | {title} | {summary} | {service} |\n"
        )
        current_num += 1

    index_content += "\n"

# Add learning path section
index_content += """---

## Learning Path

### Level 1: Foundation (Start Here)
- Read introduction and overview documents
- Understand the Canvas LMS ecosystem
- **Files**: Look for category "Introduction" and "Overview"

### Level 2: Authentication & Setup
- Configure OAuth2 and authentication
- Set up developer keys and permissions
- **Files**: Authentication category documents

### Level 3: Core Concepts
- Learn fundamental concepts
- Understand data models and architecture
- **Files**: Concepts category documents

### Level 4: API Integration
- Explore API endpoints and resources
- Implement core functionality
- **Files**: API Reference category documents

### Level 5: Advanced Features
- Live events and data services
- SIS integration
- **Files**: Data Services and SIS Integration categories

### Level 6: Reference & Tools
- CLI tools and utilities
- Complete API reference
- **Files**: Reference and CLI Tools categories

---

## Service-Specific Documentation

"""

# Add service-specific sections
for svc in sorted(by_service.keys()):
    svc_docs = by_service[svc]
    if len(svc_docs) > 0:
        index_content += f"""### {svc.replace("-", " ").title()}

| # | File | Title | Category |
|---|------|-------|----------|
"""
        for doc in svc_docs[:20]:  # Limit to first 20 per service
            file_name = rename_map.get(doc["file_path"], doc["file_path"])
            title = doc.get("title", "Untitled").replace("|", "\\|")[:40]
            cat = doc["main_category"].replace("-", " ").title()
            # Find the file number
            file_num = (
                list(rename_map.keys()).index(doc["file_path"]) + 1
                if doc["file_path"] in rename_map
                else 0
            )
            index_content += f"| {file_num:03d} | `{file_name}` | {title} | {cat} |\n"

        if len(svc_docs) > 20:
            index_content += (
                f"| ... | ... | +{len(svc_docs) - 20} more documents | ... |\n"
            )

        index_content += "\n"

index_content += """---

## Quick Reference by Topic

### Authentication & Security
"""

# Add topic-based quick reference
auth_docs = [d for d in processed_docs if d["main_category"] == "authentication"]
for doc in auth_docs[:10]:
    file_num = (
        list(rename_map.keys()).index(doc["file_path"]) + 1
        if doc["file_path"] in rename_map
        else 0
    )
    file_name = rename_map.get(doc["file_path"], doc["file_path"])
    title = doc.get("title", "").replace("|", "\\|")[:50]
    index_content += f"- **{file_num:03d}** `{file_name}` - {title}\n"

index_content += """
### API Endpoints (Most Common)
"""

api_docs = [d for d in processed_docs if d["main_category"] == "api-reference"]
# Group by resource type
resource_types = defaultdict(list)
for doc in api_docs:
    url = doc.get("url", "")
    # Extract resource name from URL
    match = re.search(r"/resources/([^/]+)", url)
    if match:
        resource = match.group(1).replace("_", " ").title()
        resource_types[resource].append(doc)

# Show top resources
for resource in sorted(resource_types.keys())[:15]:
    docs = resource_types[resource]
    if docs:
        doc = docs[0]
        file_num = (
            list(rename_map.keys()).index(doc["file_path"]) + 1
            if doc["file_path"] in rename_map
            else 0
        )
        file_name = rename_map.get(doc["file_path"], doc["file_path"])
        index_content += f"- **{resource}**: {file_num:03d} `{file_name}`\n"

index_content += f"""
---

*This index is auto-generated and optimized for AI agent search. 
Files are numbered sequentially following a logical learning progression.
Total: {len(updated_documents)} documents across {len(by_category)} categories.*
"""

# Save index
with open("000-index.md", "w") as f:
    f.write(index_content)

print("\nGenerated 000-index.md")

# Print summary
print("\n" + "=" * 60)
print("ORGANIZATION COMPLETE")
print("=" * 60)
print(f"""
Total Documents: {len(updated_documents)}
Categories: {len(by_category)}
Services: {len(by_service)}

Files Created:
  - rename_map.json: Mapping of old to new filenames
  - rename_files.sh: Bash script to perform renames
  - 000-index.md: Comprehensive documentation index
  - metadata.json: Updated with new paths

Next Steps:
  1. Run: ./rename_files.sh
  2. Verify files renamed correctly
  3. Use 000-index.md for navigation
""")
