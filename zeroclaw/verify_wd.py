#!/usr/bin/env python3
import os
os.chdir('/home/diogo/dev/library-docs/zeroclaw')
print("CWD:", os.getcwd())
print("\nFiles:")
for f in sorted(os.listdir('.')):
    if not f.startswith('.'):
        print(f"  {f}")
