#!/usr/bin/env python3
import os

os.chdir('/home/diogo/dev/library-docs/zeroclaw')
md_files = [f for f in os.listdir('.') if f.endswith('.md')]

with open('/home/diogo/dev/library-docs/zeroclaw/ABSOLUTE_RESULT.txt', 'w') as f:
    if md_files:
        f.write('\n'.join(sorted(md_files)) + f"\n\nTotal: {len(md_files)} files")
    else:
        f.write('NO .md FILES FOUND IN DIRECTORY')
