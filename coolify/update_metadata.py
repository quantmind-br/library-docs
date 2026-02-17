#!/usr/bin/env python3
"""
Update metadata.json with new file paths and organization metadata
"""

import json
from datetime import datetime

# Read the original metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Read the rename mapping
with open("rename_mapping.json", "r") as f:
    rename_map = json.load(f)

# Read the categorized documents info
with open("categorized_docs.json", "r") as f:
    categorized_info = json.load(f)

# Update each document's file_path and add original_file_path
for doc in metadata["documents"]:
    old_path = doc["file_path"]
    if old_path in rename_map:
        doc["original_file_path"] = old_path
        doc["file_path"] = rename_map[old_path]

# Add organization metadata
metadata["organization"] = {
    "method": "sequential-numbering",
    "organized_at": datetime.now().isoformat(),
    "total_files": len(rename_map),
    "categories": categorized_info["categories"],
}

# Write updated metadata back
with open("metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print(f"Updated metadata.json with {len(rename_map)} renamed files")
print(
    f"Organization metadata added with {len(categorized_info['categories'])} categories"
)
