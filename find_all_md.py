#!/usr/bin/env python3
import os

root_dir = '/home/diogo/dev/library-docs'

print("Searching for all .md files...")
found = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Skip hidden directories
    dirnames[:] = [d for d in dirnames if not d.startswith('.')]
    for filename in filenames:
        if filename.lower().endswith('.md'):
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root_dir)
            size = os.path.getsize(full_path)
            found.append((rel_path, size))

print(f"\nFound {len(found)} .md files:")
for rel_path, size in sorted(found):
    print(f"{rel_path} ({size} bytes)")

# Check specifically for the files mentioned in the task
print("\n\nChecking for task files specifically:")
task_files = [
    'zeroclaw/226-security-sandboxing.md',
    'zeroclaw/227-security-security-roadmap.md',
    'zeroclaw/228-summary.fr.md',
    'zeroclaw/229-summary.ja.md',
    'zeroclaw/230-summary.ru.md',
    'zeroclaw/231-summary.zh-cn.md',
    'zeroclaw/232-vi-channels-reference.md',
    'zeroclaw/233-vi-commands-reference.md',
    'zeroclaw/234-vi-config-reference.md',
]

for task_file in task_files:
    exists = os.path.exists(os.path.join(root_dir, task_file))
    print(f"{task_file}: {'EXISTS' if exists else 'MISSING'}")
