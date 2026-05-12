#!/bin/bash
for f in /home/diogo/dev/library-docs/zeroclaw/*; do
  echo "=== $f ==="
  if [ -f "$f" ]; then
    echo "File: $f"
    head -5 "$f"
    echo ""
  fi
done
