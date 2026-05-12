#!/usr/bin/env bash
# Phase 7: Verification.
#
# Usage: verify.sh <directory>
# Exit 0 = PASS, non-zero = FAIL.
set -euo pipefail

DIR="${1:-.}"
cd "$DIR"

if [[ ! -f metadata.json ]]; then
  echo "FAIL: metadata.json missing"; exit 1
fi
if [[ ! -f 000-index.md ]]; then
  echo "FAIL: 000-index.md missing"; exit 1
fi

total=$(jq '.documents | length' metadata.json)
on_disk=$(ls [0-9][0-9][0-9]-*.md 2>/dev/null | grep -v '^000-' | wc -l)
echo "metadata=$total disk=$on_disk"

if [[ "$total" -ne "$on_disk" ]]; then
  echo "FAIL: count mismatch (metadata=$total, disk=$on_disk)"
  exit 1
fi

# Missing files referenced by metadata
missing=0
while IFS= read -r f; do
  [[ -f "$f" ]] || { echo "MISSING: $f"; missing=$((missing+1)); }
done < <(jq -r '.documents[].file_path' metadata.json)
if [[ "$missing" -gt 0 ]]; then
  echo "FAIL: $missing file(s) missing on disk"
  exit 1
fi

# Numbering gaps
gaps=0
for n in $(seq -f '%03g' 1 "$total"); do
  if ! ls "${n}-"*.md >/dev/null 2>&1; then
    echo "GAP: $n"
    gaps=$((gaps+1))
  fi
done
if [[ "$gaps" -gt 0 ]]; then
  echo "FAIL: $gaps gap(s) in numbering"
  exit 1
fi

# Forbidden 'index' in source filenames (only 000-index.md may use it)
if ls [0-9][0-9][0-9]-*.md 2>/dev/null | grep -v '^000-' | grep -i 'index' >/dev/null; then
  echo "FAIL: source filename(s) retain forbidden 'index' substring:"
  ls [0-9][0-9][0-9]-*.md | grep -v '^000-' | grep -i 'index'
  exit 1
fi

# original_file_path coverage check
no_orig=$(jq '[.documents[] | select(.original_file_path == null)] | length' metadata.json)
if [[ "$no_orig" -gt 0 ]]; then
  echo "WARN: $no_orig document(s) without original_file_path (acceptable if file was never renamed)"
fi

echo "PASS: $total docs, contiguous 001..$(printf '%03d' "$total"), 000-index.md present"
