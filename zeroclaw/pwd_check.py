#!/usr/bin/env python3
import os
print(os.getcwd())
print("\nFiles in cwd:")
for f in sorted(os.listdir('.'))[:20]:
    print(f"  {f}")
