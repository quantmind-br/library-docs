#!/usr/bin/env python3
"""
Build rename script from metadata.json
"""

import json
import os
import re

os.chdir("/home/diogo/dev/library-docs/litellm")

# Load metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Get current files
current_files = set(f for f in os.listdir(".") if f.endswith(".md"))

# Build rename mapping
renames = {}

for doc in metadata["documents"]:
    original = doc.get("original_file_path", "")
    target = doc["file_path"]

    if original == target or not original:
        continue

    # Try to find current file
    # Remove any existing prefix from target to get base name
    base_match = re.match(r"^\d+-(.+)$", target)
    if base_match:
        base_name = base_match.group(1)
    else:
        base_name = target

    # Check all current files for this base name
    for cf in current_files:
        cf_base = re.sub(r"^\d+-", "", cf)
        if cf_base == base_name:
            renames[cf] = target
            break

# Generate bash script
with open("/tmp/do_rename.sh", "w") as f:
    f.write("#!/bin/bash\nset -e\n\ncd /home/diogo/dev/library-docs/litellm\n\n")
    f.write('echo "Starting file renames..."\n\n')
    f.write(f"total={len(renames)}\ncurrent=0\n\n")

    for old, new in sorted(renames.items()):
        f.write(f'if [ -f "{old}" ]; then\n')
        f.write(f"  current=$((current + 1))\n")
        f.write(f'  echo "[$current/$total] {old} -> {new}"\n')
        f.write(f'  mv "{old}" "{new}"\n')
        f.write(f"fi\n\n")

    f.write('echo ""\necho "✓ Renamed $current files"\n')

print(f"Generated rename script with {len(renames)} renames")
print(f"Run: bash /tmp/do_rename.sh")
