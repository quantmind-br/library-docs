#!/usr/bin/env python3
import os

root = '/home/diogo/dev/library-docs/zeroclaw'

print("All files in directory tree:")
for dirpath, dirnames, filenames in os.walk(root):
    # Skip hidden directories
    dirnames[:] = [d for d in dirnames if not d.startswith('.')]
    
    for filename in sorted(filenames):
        if filename.endswith('.md'):
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root)
            size = os.path.getsize(full_path)
            print(f"{rel_path} ({size} bytes)")
