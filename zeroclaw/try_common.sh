#!/bin/bash
for i in {100..200}; do
  if [ -f "/home/diogo/dev/library-docs/zeroclaw/${i}-*.md" ]; then
    echo "Found pattern: ${i}-*.md"
    ls -la "/home/diogo/dev/library-docs/zeroclaw/${i}-*.md"
  fi
done
