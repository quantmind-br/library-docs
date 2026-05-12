#!/usr/bin/env python3
import os

print("Files in current directory:")
for item in sorted(os.listdir('.')):
    if not item.startswith('.'):
        path = os.path.join('.', item)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(f"{item} ({size} bytes)")
        else:
            print(f"{item}/ (dir)")
