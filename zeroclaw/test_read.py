#!/usr/bin/env python3
import os

path = '/home/diogo/dev/library-docs/zeroclaw'
if os.path.exists(path):
    print(f"Directory exists: {path}")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(f"Files: {files}")
else:
    print(f"Directory does not exist: {path}")
