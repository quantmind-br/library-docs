#!/usr/bin/env python3
import os

# Try various possible locations
paths_to_try = [
    '/home/diogo/dev/library-docs/zeroclaw/226-security-sandboxing.md',
    '/home/diogo/dev/library-docs/227-security-security-roadmap.md',
    '226-security-sandboxing.md',
    '227-security-security-roadmap.md',
]

results = []
for path in paths_to_try:
    exists = os.path.exists(path)
    is_file = os.path.isfile(path) if exists else False
    size = os.path.getsize(path) if (exists and is_file) else 0
    results.append((path, exists, is_file, size))

with open('/home/diogo/dev/library-docs/zeroclaw/TRY_RESULTS.txt', 'w') as f:
    for path, exists, is_file, size in results:
        f.write(f"{path}: exists={exists}, is_file={is_file}, size={size}\n")
