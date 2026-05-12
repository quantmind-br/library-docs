#!/usr/bin/env python3
import os
import glob

print("All .md files in /home/diogo/dev/library-docs/zeroclaw:")
md_files = sorted(glob.glob('/home/diogo/dev/library-docs/zeroclaw/*.md'))
for f in md_files:
    basename = os.path.basename(f)
    size = os.path.getsize(f)
    print(f"  {basename} ({size} bytes)")
