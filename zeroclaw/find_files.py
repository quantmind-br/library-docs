#!/usr/bin/env python3
import os
import glob

# Check all .md files in the directory
md_files = glob.glob('/home/diogo/dev/library-docs/zeroclaw/*.md')

print(f"Found {len(md_files)} .md files:")
for f in sorted(md_files):
    basename = os.path.basename(f)
    size = os.path.getsize(f)
    print(f"  {basename} ({size} bytes)")
