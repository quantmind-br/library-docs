#!/usr/bin/env python3
import os, sys

base = '/home/diogo/dev/library-docs/zeroclaw'

# Check what exists
if os.path.isdir(base):
    files = sorted([f for f in os.listdir(base) if f.endswith('.md')])
    print("Found .md files:")
    for f in files:
        print(f"  {f}")
    
    # Try to read the first one
    if files:
        sample = files[0]
        sample_path = os.path.join(base, sample)
        print(f"\nTrying to read: {sample_path}")
        try:
            with open(sample_path, 'r', encoding='utf-8') as fh:
                content = fh.read()
                print(f"Success! File size: {len(content)} bytes")
                print("First 500 chars:")
                print(content[:500])
        except Exception as e:
            print(f"Error reading {sample_path}: {e}")
else:
    print(f"Directory does not exist: {base}")
