#!/usr/bin/env python3
import os

dir_path = "/home/diogo/dev/library-docs/zeroclaw"
if os.path.exists(dir_path):
    files = os.listdir(dir_path)
    md_files = sorted([f for f in files if f.endswith('.md')])
    for f in md_files:
        print(f)
