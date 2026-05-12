#!/usr/bin/env python3
import os
import glob

print("Files in /home/diogo/dev/library-docs/zeroclaw:")
for f in sorted(glob.glob('/home/diogo/dev/library-docs/zeroclaw/*')):
    if os.path.isfile(f):
        print(f"  {os.path.basename(f)}")
