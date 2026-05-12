#!/usr/bin/env python3
import os

base = '/home/diogo/dev/library-docs/zeroclaw'

# Check if directory exists
if os.path.isdir(base):
    # List all .md files
    md_files = []
    for root, dirs, files in os.walk(base):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.lower().endswith('.md'):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, base)
                md_files.append((rel, os.path.getsize(full)))
    
    if md_files:
        print(f"Found {len(md_files)} .md file(s):")
        for rel_path, size in sorted(md_files):
            print(f"  {rel_path} ({size} bytes)")
    else:
        print("No .md files found")
else:
    print(f"Directory does not exist: {base}")
