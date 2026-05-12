#!/usr/bin/env python3
import subprocess
import sys

try:
    result = subprocess.run(
        ['git', '-C', '/home/diogo/dev/library-docs/zeroclaw', 'status', '--porcelain'],
        capture_output=True,
        text=True,
        timeout=5
    )
    print("Git status output:")
    print(result.stdout)
    print(result.stderr)
    print("Return code:", result.returncode)
except Exception as e:
    print(f"Error: {e}")
