import os
import json

path = '/home/diogo/dev/library-docs/zeroclaw'
print("Files in directory:")
for f in sorted(os.listdir(path)):
    if not f.startswith('.'):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f"{f} ({size} bytes)")
