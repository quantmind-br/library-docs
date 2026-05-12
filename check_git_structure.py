#!/usr/bin/env python3
import os
import sys

base = "/home/diogo/dev/library-docs/zeroclaw"

print("Checking directory structure at:", base)
print("=" * 60)

def scan_tree(path, indent=0):
    try:
        items = sorted(os.listdir(path))
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print("  " * indent + f"📁 {item}/")
                scan_tree(full_path, indent + 1)
            else:
                size = os.path.getsize(full_path)
                print("  " * indent + f"📄 {item} ({size} bytes)")
    except Exception as e:
        print("  " * indent + f"❌ Error reading {path}: {e}")

scan_tree(base)

print("\n" + "=" * 60)
print("Checking for security-related files specifically:")
security_files = [
    "agnostic-security.md",
    "audit-logging.md", 
    "frictionless-security.md",
    "matrix-e2ee-guide.md",
    "sandboxing.md",
    "security-roadmap.md",
    "resource-limits.md"
]

for fname in security_files:
    fpath = os.path.join(base, fname)
    if os.path.exists(fpath):
        print(f"✅ Found: {fname}")
    else:
        print(f"❌ Missing: {fname}")

fr_summary = os.path.join(base, "129-summary.fr.md")
if os.path.exists(fr_summary):
    print(f"✅ Found: 129-summary.fr.md")
else:
    print(f"❌ Missing: 129-summary.fr.md")
