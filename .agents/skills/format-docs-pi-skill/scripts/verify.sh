#!/usr/bin/env bash
# Phase 5 verification. Exit 0 = PASS, non-zero = FAIL (something must be fixed).
# Each check is its own statement (no `&&` chaining) — several checks legitimately
# return non-zero on success-with-no-matches, which would short-circuit a chain.
set -u

DIR="${1:-}"
[ -z "$DIR" ] && { echo "Usage: verify.sh <dir>" >&2; exit 1; }
[ -d "$DIR" ] || { echo "Not a directory: $DIR" >&2; exit 1; }
cd "$DIR"

EXIT=0

# 1. file count matches metadata (000-index.md is the index, NOT a documents[] entry)
n_disk=$(ls -1 [0-9]*.md 2>/dev/null | grep -v '^000-index\.md$' | wc -l)
n_meta=$(jq '.documents | length' metadata.json)
echo "Files on disk: $n_disk"
echo "Docs in metadata: $n_meta"
[ "$n_disk" = "$n_meta" ] || { echo "MISMATCH: counts differ"; EXIT=1; }

# 2. every metadata entry exists on disk
while IFS= read -r f; do
  [ -f "$f" ] || { echo "MISSING: $f"; EXIT=1; }
done < <(jq -r '.documents[].file_path' metadata.json)

# 3. every disk file is in metadata (skip 000-index.md)
for f in [0-9]*.md; do
  [ "$f" = "000-index.md" ] && continue
  jq -e --arg f "$f" '.documents[] | select(.file_path == $f)' metadata.json >/dev/null \
    || { echo "ORPHAN: $f"; EXIT=1; }
done

# 4. every numbered file has the optimized flag (skip 000-index.md)
for f in [0-9]*.md; do
  [ "$f" = "000-index.md" ] && continue
  grep -q '^optimized: true$' "$f" || { echo "NOT-OPTIMIZED: $f"; EXIT=1; }
done

# 5. no wikilinks point to deleted files
DELETED=$(jq -r '.optimization.deleted_files[]?' metadata.json | sed 's/\.md$//')
BROKEN=0
for f in [0-9]*.md; do
  for base in $DELETED; do
    [ -z "$base" ] && continue
    if grep -nE "\[\[${base}(\]|\||#)" "$f" >/dev/null 2>&1; then
      grep -nE "\[\[${base}(\]|\||#)" "$f" | sed "s|^|BROKEN-WIKILINK: $f -> $base |"
      BROKEN=$((BROKEN + 1))
    fi
  done
done
if [ "$BROKEN" -eq 0 ]; then
  echo "OK: no broken wikilinks"
else
  EXIT=1
fi

if [ "$EXIT" -eq 0 ]; then
  echo "PASS"
else
  echo "FAIL"
fi
exit $EXIT
