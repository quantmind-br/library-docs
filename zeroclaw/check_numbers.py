#!/usr/bin/env python3
import os
import glob

# Check for numbered .md files
md_files = glob.glob('/home/diogo/dev/library-docs/zeroclaw/[0-9]*.md')

if md_files:
    print("Numbered .md files found:")
    for f in sorted(md_files):
        print(f"  {os.path.basename(f)}")
else:
    print("No numbered .md files found")

# Check all .md files
all_md = glob.glob('/home/diogo/dev/library-docs/zeroclaw/*.md')
print(f"\nTotal .md files: {len(all_md)}")
for f in sorted(all_md):
    print(f"  {os.path.basename(f)}")
