#!/usr/bin/env python3
import os
import glob

for root, dirs, files in os.walk('/home/diogo/dev/library-docs/zeroclaw'):
    for file in files:
        if file.endswith('.md') or file.endswith('.markdown'):
            print(os.path.join(root, file))
