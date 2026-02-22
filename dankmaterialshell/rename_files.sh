#!/bin/bash
cd /Users/diogo/dev/library-docs/dankmaterialshell

# Get all markdown files sorted alphabetically and rename with sequential numbers
# Using a simpler approach - alphabetical sort preserves version groupings

# Get list of files sorted
files=($(ls -1 *.md | sort))

# Counter starting at 1
counter=1

for file in "${files[@]}"; do
    # Extract just the filename without path
    filename=$(basename "$file")

    # Skip if already numbered
    if [[ "$filename" =~ ^[0-9]{3}- ]]; then
        continue
    fi

    # Create new filename with zero-padded number
    newname=$(printf "%03d-%s" $counter "$filename")

    # Rename file
    mv "$filename" "$newname"

    # Increment counter
    ((counter++))
done

echo "Renamed $(($counter - 1)) files"
