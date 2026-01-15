---
title: Improve Error Messages - Factory Documentation
url: https://docs.factory.ai/guides/droid-exec/refactor-error-messages
source: sitemap
fetched_at: 2026-01-13T19:04:32.800769732-03:00
rendered_js: false
word_count: 351
summary: This tutorial provides a guide and a shell script for using Droid Exec to automatically refactor and improve ResponseError messages across a TypeScript codebase, making them more descriptive and user-friendly.
tags:
    - droid-exec
    - error-handling
    - refactoring
    - shell-script
    - typescript
    - automation
    - ux
category: tutorial
---

This tutorial demonstrates how to use Droid Exec to refactor error messages across hundreds of files simultaneously. The script intelligently finds all ResponseError instantiations and improves their messages to be more descriptive, actionable, and user-friendly.

## How it works

The script:

1. **Finds files**: Searches for all `.ts` and `.tsx` files containing ResponseError classes
2. **Filters smartly**: Excludes `node_modules`, `.git`, `dist`, `build`, and `.next` directories
3. **Identifies errors**: Locates all ResponseError instantiations (400, 401, 403, 404, etc.)
4. **Improves messages**: Makes them more descriptive and actionable
5. **Adds context**: Includes what went wrong and potential fixes
6. **User-friendly language**: Removes technical jargon
7. **Preserves metadata**: Keeps error codes and metadata intact

## Get the script

View full script source

```
#!/bin/bash

# Droid Error Message Improvement Script

# Automatically improves ResponseError messages across the codebase

#

# Usage: ./droid-improve-errors.sh [directory]

# Example: ./droid-improve-errors.sh apps

set -e

# Configuration

CONCURRENCY=${CONCURRENCY:-5}
DRY_RUN=${DRY_RUN:-false}
TARGET_DIR="${1:-.}"

# Colors for output

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Temp files for tracking

TEMP_DIR=$(mktemp -d)
FILES_LIST="$TEMP_DIR/files.txt"
ERRORS_FOUND="$TEMP_DIR/errors_found.txt"
MODIFIED_COUNT=0
PROCESSED_COUNT=0
ERRORS_IMPROVED=0

# Cleanup on exit

trap "rm -rf $TEMP_DIR" EXIT

# Function to process a single file

process_file() {
local filepath="$1"
    local filename=$(basename "$filepath")

    # Check if file contains ResponseError instantiations
    if ! grep -qE "new ResponseError[0-9]+|throw new ResponseError" "$filepath" 2>/dev/null; then
        return 0
    fi

    # Count error instances for reporting
    local error_count=$(grep -cE "new ResponseError[0-9]+" "$filepath" 2>/dev/null || echo 0)

    echo -e "${BLUE}Processing: $filepath${NC}"
    echo -e "  Found $error_count error instantiation(s)"

    # The AI prompt for improving error messages
    local prompt="Improve the error messages in $filepath:

Find all ResponseError instantiations (ResponseError400BadRequest, ResponseError401Unauthorized, etc.)
and improve their error messages following these guidelines:

1. Make messages more descriptive and actionable
2. Include context about what went wrong
3. Suggest potential fixes when appropriate
4. Use user-friendly language (avoid technical jargon)
5. Include relevant details without exposing sensitive data

Examples of improvements:

- 'Invalid api key format' → 'API key must be a 32-character alphanumeric string starting with \"fac\_\"'
- 'Organization not found' → 'Organization with ID {orgId} not found. Please verify the organization exists and you have access.'
- 'Invalid CSRF token' → 'Security validation failed. Please refresh the page and try again.'
- 'Invalid request parameters' → 'Missing required field \"email\". Please provide a valid email address.'
- 'User is already a member' → 'This user is already a member of the organization and cannot be invited again.'

Only modify the error message strings, preserve all other code including metadata parameters.
Return the complete file with improved error messages."

    if [ "$DRY_RUN" = "true" ]; then
        echo -e "${YELLOW}  [DRY RUN] Would improve $error_count error message(s)${NC}"
        echo "$error_count" >> "$ERRORS_FOUND"
        return 0
    fi

    # Get original file hash for comparison
    local original_hash=$(md5sum "$filepath" 2>/dev/null | cut -d' ' -f1 || md5 -q "$filepath")

    # Run droid to improve error messages
    if droid exec --auto low "$prompt" 2>/dev/null; then
        # Check if file was modified
        local new_hash=$(md5sum "$filepath" 2>/dev/null | cut -d' ' -f1 || md5 -q "$filepath")
        if [ "$original_hash" != "$new_hash" ]; then
            echo -e "${GREEN}  ✓ Improved error messages${NC}"
            ((MODIFIED_COUNT++))
            ((ERRORS_IMPROVED+=error_count))
        else
            echo -e "  No changes needed"
        fi
        ((PROCESSED_COUNT++))
    else
        echo -e "${RED}  ✗ Failed to process${NC}"
    fi

}

# Export function and variables for parallel execution

export -f process_file
export DRY_RUN GREEN YELLOW BLUE RED NC ERRORS_FOUND

# Main execution

echo -e "${BLUE}=== Droid Error Message Improvement ===${NC}"
echo -e "${BLUE}Directory: $TARGET_DIR${NC}"
echo -e "${BLUE}Concurrency: $CONCURRENCY${NC}"
[ "$DRY_RUN" = "true" ] && echo -e "${YELLOW}DRY RUN MODE${NC}"
echo ""

# Find TypeScript files containing ResponseError

find "$TARGET_DIR" -type f \( -name "*.ts" -o -name "*.tsx" \) \
    ! -path "*/node_modules/*" \
    ! -path "*/.git/*" \
    ! -path "*/dist/*" \
    ! -path "*/build/*" \
    ! -path "*/.next/*" \
    ! -path "*/coverage/*" \
    -exec grep -l "ResponseError[0-9]" {} \; 2>/dev/null > "$FILES_LIST" || true

FILE_COUNT=$(wc -l < "$FILES_LIST" | tr -d ' ')

if [ "$FILE_COUNT" -eq 0 ]; then
echo -e "${YELLOW}No files with ResponseError found${NC}"
exit 0
fi

echo -e "${BLUE}Found $FILE_COUNT files with ResponseError classes${NC}\n"

# Process files in parallel

cat "$FILES_LIST" | xargs -n 1 -P "$CONCURRENCY" -I {} bash -c 'process_file "$@"' _ {}

# Calculate total errors found in dry run

if [ "$DRY_RUN" = "true" ] && [ -f "$ERRORS_FOUND" ]; then
TOTAL_ERRORS=$(awk '{sum+=$1} END {print sum}' "$ERRORS_FOUND" 2>/dev/null || echo 0)
fi

# Show summary

echo -e "\n${BLUE}=== Summary ===${NC}"
echo -e "${GREEN}Files scanned: $FILE_COUNT${NC}"
echo -e "${GREEN}Files processed: $PROCESSED_COUNT${NC}"

if [ "$DRY_RUN" = "true" ]; then
[ -n "$TOTAL_ERRORS" ] && echo -e "${YELLOW}Error messages to improve: $TOTAL_ERRORS${NC}"
else
echo -e "${GREEN}Files modified: $MODIFIED_COUNT${NC}"
[ "$ERRORS_IMPROVED" -gt 0 ] && echo -e "${GREEN}Error messages improved: ~$ERRORS_IMPROVED${NC}"
fi

if [ "$DRY_RUN" = "false" ] && [ "$MODIFIED_COUNT" -gt 0 ]; then
echo -e "\n${BLUE}Next steps:${NC}"
echo " git diff # Review changes"
echo " npm run typecheck # Verify types"
echo " npm run test # Run tests"
echo " git add -A # Stage changes"
echo " git commit -m 'refactor: improve error messages for better UX'"
fi

```

## Prerequisites

Before you begin, complete the [Droid Exec installation](https://docs.factory.ai/cli/droid-exec/overview#installation).

## Basic usage

### Preview changes (dry run)

The dry run feature shows you exactly which files contain ResponseError instantiations and how many:

```
# Preview what would happen (no changes made)
DRY_RUN=true ./droid-improve-errors.sh apps/factory-admin/src/app/api/_utils/middleware.ts

# Example output:
# === Droid Error Message Improvement ===
# Directory: apps/factory-admin/src/app/api/_utils/middleware.ts
# Concurrency: 5
# DRY RUN MODE
#
# Found 1 files with ResponseError classes
#
# Processing: apps/factory-admin/src/app/api/_utils/middleware.ts
#   Found 6 error instantiation(s)
#   [DRY RUN] Would improve 6 error message(s)
#
# === Summary ===
# Files scanned: 1
# Files processed: 0
# Error messages to improve: 6
```

**How dry run works:**

- When `DRY_RUN=true`: Counts all ResponseError instantiations without making changes
- When `DRY_RUN=false` (default): Actually improves the error messages using AI

This helps you:

- Estimate the scope of changes needed
- Test on a small directory first
- Plan your refactoring strategy

### Apply refactoring

Once you’re ready, run the actual error message improvement:

```
# Actually improve the error messages (default behavior)
./droid-improve-errors.sh apps/factory-admin

# Or explicitly set DRY_RUN=false
DRY_RUN=false ./droid-improve-errors.sh apps/factory-admin

# Adjust concurrency for faster processing
CONCURRENCY=10 ./droid-improve-errors.sh packages
```

Actual execution example:

```
% ./scripts/droid-improve-errors.sh apps/factory-admin/src/app/api/_utils/middleware.ts
=== Droid Error Message Improvement ===
Directory: apps/factory-admin/src/app/api/_utils/middleware.ts
Concurrency: 5

Found 1 files with ResponseError classes

Processing: apps/factory-admin/src/app/api/_utils/middleware.ts
  Found 6 error instantiation(s)
## Summary

I've successfully improved all error messages in the `apps/factory-admin/src/app/api/_utils/middleware.ts` file. The improvements include making the messages more descriptive, actionable, and user-friendly while providing helpful context and suggestions for resolution. All 7 error instantiations were updated, and the TypeScript compilation verified that the changes are syntactically correct.
```

## Real-world transformations

### Example 1: Session Authentication

- Before
- After

```
// middleware.ts
if (!sessionCookie?.value) {
  throw new ResponseError401Unauthorized('No session');
}

if (!userRecord) {
  throw new ResponseError401Unauthorized('Invalid session');
}
```

```
// middleware.ts
if (!sessionCookie?.value) {
  throw new ResponseError401Unauthorized(
    'Session cookie not found. Please sign in again to access the admin dashboard.'
  );
}

if (!userRecord) {
  throw new ResponseError401Unauthorized(
    'Session is invalid or has expired. Please sign in again to continue.'
  );
}
```

- Before
- After

```
// middleware.ts
if (!authHeader) {
  throw new ResponseError401Unauthorized('Missing auth header');
}

if (authHeader !== `Bearer ${secret}`) {
  throw new ResponseError401Unauthorized('Invalid token');
}
```

```
// middleware.ts
if (!authHeader) {
  throw new ResponseError401Unauthorized(
    'Authorization header is missing. Please include a valid Bearer token in the Authorization header.'
  );
}

if (authHeader !== `Bearer ${secret}`) {
  throw new ResponseError401Unauthorized(
    'Invalid or expired authorization token. Please verify your API credentials and ensure the token is properly formatted as "Bearer <token>".'
  );
}
```

## Best practices