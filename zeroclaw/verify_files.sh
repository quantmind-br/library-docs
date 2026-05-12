#!/bin/bash
# List all markdown files
for f in *.md; do
    if [ -f "$f" ]; then
        echo "Found: $f"
    fi
done
# Also check subdirectories
for d in */; do
    [ -d "$d" ] || continue
    echo "Checking directory: $d"
    for f in "$d".md/*.md 2>/dev/null; do
        [ -f "$f" ] && echo "Found in subdir: $f"
    done
done
