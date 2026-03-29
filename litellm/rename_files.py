#!/usr/bin/env python3
"""
Rename files based on updated metadata.json
"""

import json
import os
import subprocess
from pathlib import Path


def load_metadata():
    """Load updated metadata.json"""
    with open("metadata.json", "r") as f:
        return json.load(f)


def get_current_files():
    """Get list of current markdown files"""
    result = subprocess.run(
        ["ls", "-1", "*.md"],
        capture_output=True,
        text=True,
        cwd="/home/diogo/dev/library-docs/litellm",
    )
    return set(result.stdout.strip().split("\n"))


def build_rename_map(metadata, current_files):
    """
    Build map of current filename -> new filename
    """
    rename_map = {}
    documents = metadata.get("documents", [])

    # Build mapping from base name (without prefix) to document
    base_to_doc = {}
    for doc in documents:
        original_path = doc.get("original_file_path", doc["file_path"])
        new_path = doc["file_path"]

        # Skip if no change needed
        if original_path == new_path:
            continue

        base_to_doc[original_path] = new_path

    # Match current files to base names
    for current_file in current_files:
        # Try to find matching base name
        # Current format: XXX-base-name.md or base-name.md
        parts = current_file.split("-", 1)
        if len(parts) == 2:
            base_name = parts[1]
        else:
            base_name = current_file

        if base_name in base_to_doc:
            rename_map[current_file] = base_to_doc[base_name]

    return rename_map


def main():
    print("Loading metadata...")
    metadata = load_metadata()

    print("Getting current files...")
    current_files = get_current_files()

    print(f"Found {len(current_files)} markdown files")

    print("Building rename map...")
    rename_map = build_rename_map(metadata, current_files)

    print(f"Found {len(rename_map)} files to rename")

    if not rename_map:
        print("No files need renaming. Files may already be correctly organized.")
        return

    # Create rename script
    with open("/tmp/rename_files.sh", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("cd /home/diogo/dev/library-docs/litellm\n\n")

        for old, new in sorted(rename_map.items()):
            f.write(f'mv "{old}" "{new}"\n')

    # Also create a mapping for verification
    with open("/tmp/rename_map.json", "w") as f:
        json.dump(rename_map, f, indent=2)

    print(f"\n✓ Created rename script: /tmp/rename_files.sh")
    print(f"✓ Created mapping: /tmp/rename_map.json")
    print(f"\nSample renames:")
    for i, (old, new) in enumerate(sorted(rename_map.items())[:10]):
        print(f"  {old} -> {new}")

    if len(rename_map) > 10:
        print(f"  ... and {len(rename_map) - 10} more")

    print(f"\nTo execute:")
    print(f"  bash /tmp/rename_files.sh")


if __name__ == "__main__":
    main()
