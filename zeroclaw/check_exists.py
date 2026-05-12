import os
import glob

# Check for files matching the patterns
patterns = [
    '036-*.md', '037-*.md', '038-*.md', '039-*.md',
    '041-*.md', '042-*.md', '043-*.md', '044-*.md', '045-*.md'
]

for pattern in patterns:
    matches = glob.glob(f'/home/diogo/dev/library-docs/zeroclaw/{pattern}')
    if matches:
        for match in matches:
            print(f"FOUND: {match}")
    else:
        print(f"NO MATCH: {pattern}")

# List all markdown files
print("\nAll .md files:")
for md_file in glob.glob('/home/diogo/dev/library-docs/zeroclaw/*.md'):
    basename = os.path.basename(md_file)
    print(f"  {basename}")
