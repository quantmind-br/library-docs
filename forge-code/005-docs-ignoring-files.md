---
title: "Ignoring Files in ForgeCode"
url: https://forgecode.dev/docs/ignoring-files/
source: sitemap
fetched_at: 2026-04-30T14:09:11.675907014-03:00
rendered_js: false
word_count: 243
summary: "Control file visibility in ForgeCode using `.gitignore` and `.ignore` rules, with troubleshooting for common issues."
tags:
  - file-exclusion
  - configuration
  - troubleshooting
  - ignore-patterns
  - version-control
category: guide
optimized: true
---
# Ignoring Files in ForgeCode

> **TL;DR**
> Use `.gitignore` (Git) or `.ignore` (ForgeCode-only) to hide files. `.ignore` overrides `.gitignore`.

## How It Works

### Precedence (Highest → Lowest)
1. `.ignore` (ForgeCode-specific)
2. `.gitignore` (Git)
3. Global Git ignore (`~/.config/git/ignore`)
4. `.git/info/exclude` (Repo-specific)

> **Key Rule**: `.ignore` always wins. Whitelist with `!pattern`.

### Default Filters
- **Binary files** (non-text)
- **Hidden files** (start with `.`, except in project root)

## Common Issues

| Issue | Solution |
|-------|----------|
| File hidden by `.gitignore` | Add `!pattern` to `.ignore` |
| Hidden file in subdirectory | Add `!.filename` to `.ignore` |
| Binary file included | Convert to text or ignore |

## Troubleshooting

### Step 1: Check Git Ignore
```bash
git check-ignore -v path/to/file
```
- **Output**: Shows which `.gitignore` rule hides the file.
- **Limitation**: Doesn’t check `.ignore` or ForgeCode-specific rules.

### Step 2: Debug Visibility
- **Hidden by `.ignore`?** Check file contents.
- **Hidden by path?** Verify directory isn’t hidden (e.g., `.cache/`).
- **Binary?** Convert or ignore.

### Step 3: Force Visibility
Add to `.ignore`:
```plaintext
!path/to/file
!.env  # For hidden files
```

> **Restart Required**: Changes to ignore files need a ForgeCode restart.

## Pattern Syntax
- **Directories**: End with `/` (e.g., `dist/`)
- **Recursive**: Use `**` (e.g., `**/temp/`)
- **Wildcards**: `*.log`
- **Paths**: Use `/` (even on Windows)

## Advanced Debugging
1. Export session:
   ```bash
   :dump html
   ```
2. Share on [Discord](https://discord.gg/kRZBPPkgwq) with:
   - File path
   - `.gitignore`/`.ignore` contents
   - Expected vs. actual behavior
   - `git check-ignore -v` output

## Related Guides
- [File Tagging](https://forgecode.dev/docs/file-tagging/)
- [AGENTS.md](https://forgecode.dev/docs/custom-rules-guide/)