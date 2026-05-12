#!/bin/bash
find /home/diogo/dev/library-docs/zeroclaw -type f -name "*.md" -o -name "*.markdown" | head -20
ls -lt /home/diogo/dev/library-docs/zeroclaw/*.md 2>/dev/null || echo "No .md files"
ls -lt /home/diogo/dev/library-docs/zeroclaw/*.markdown 2>/dev/null || echo "No .markdown files"
