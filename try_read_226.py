#!/usr/bin/env python3
import os

# Try various possible locations
paths_to_try = [
    '/home/diogo/dev/library-docs/zeroclaw/226-security-sandboxing.md',
    '/home/diogo/dev/library-docs/226-security-sandboxing.md',
    '/home/diogo/dev/library-docs/zeroclaw/./226-security-sandboxing.md',
    './226-security-sandboxing.md',
    '226-security-sandboxing.md',
]

for path in paths_to_try:
    exists = os.path.exists(path)
    is_file = os.path.isfile(path) if exists else False
    print(f"{path}: exists={exists}, is_file={is_file}")
    if exists and is_file:
        print(f"  Size: {os.path.getsize(path)} bytes")
