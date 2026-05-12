#!/usr/bin/env python3
import os

target_dir = "/home/diogo/dev/library-docs/zeroclaw"

print("Attempting to list files in:", target_dir)
print("Directory exists:", os.path.isdir(target_dir))
print("Directory contents:")

try:
    items = os.listdir(target_dir)
    for item in sorted(items):
        full_path = os.path.join(target_dir, item)
        if os.path.isfile(full_path):
            print(f"  FILE: {item} ({os.path.getsize(full_path)} bytes)")
        elif os.path.isdir(full_path):
            print(f"  DIR:  {item}/")
except Exception as e:
    print(f"  Error: {e}")
