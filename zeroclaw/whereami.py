#!/usr/bin/env python3
import os
print(f"Current directory: {os.getcwd()}")
print("\nFiles in current directory:")
for item in os.listdir('.'):
    if item.endswith('.md'):
        print(f"  {item}")
