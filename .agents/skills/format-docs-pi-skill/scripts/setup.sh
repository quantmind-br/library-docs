#!/usr/bin/env bash
# Phase 0 setup: validate target folder + metadata.json. Print absolute path.
set -euo pipefail
TARGET="${1:-}"
[ -z "$TARGET" ] && TARGET="$PWD"
TARGET="$(realpath "$TARGET")"
[ -d "$TARGET" ] || { echo "Invalid folder: $TARGET" >&2; exit 1; }
[ -f "$TARGET/metadata.json" ] || {
  echo "Missing metadata.json in $TARGET — run /organize-docs first" >&2; exit 2; }
jq -e . "$TARGET/metadata.json" >/dev/null 2>&1 || {
  echo "Malformed metadata.json in $TARGET" >&2; exit 3; }
echo "$TARGET"
