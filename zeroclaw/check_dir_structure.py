#!/usr/bin/env python3
import os

path = '/home/diogo/dev/library-docs/zeroclaw'

print("Directory structure check:")
print(f"Path exists: {os.path.exists(path)}")
print(f"Is directory: {os.path.isdir(path)}")

if os.path.isdir(path):
    print("\nContents:")
    try:
        items = sorted(os.listdir(path))
        for item in items:
            if not item.startswith('.'):
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    print(f"  FILE: {item} ({size} bytes)")
                elif os.path.isdir(full_path):
                    subitems = sorted(os.listdir(full_path))
                    print(f"  DIR: {item}/ (contains {len(subitems)} items)")
    except Exception as e:
        print(f"  Error listing: {e}")
