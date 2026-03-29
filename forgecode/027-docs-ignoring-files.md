---
title: ForgeCode
url: https://forgecode.dev/docs/ignoring-files/
source: sitemap
fetched_at: 2026-03-29T16:30:41.26099-03:00
rendered_js: false
word_count: 628
summary: This document explains how ForgeCode handles file exclusion rules using .gitignore and .ignore files, including precedence logic, troubleshooting steps for hidden files, and configuration best practices.
tags:
    - file-filtering
    - ignore-patterns
    - configuration
    - troubleshooting
    - file-precedence
    - git-integration
category: guide
---

ForgeCode respects your existing `.gitignore` and `.ignore` patterns automatically. If you've already set up `.gitignore` for your project, you're done. ForgeCode reads it and applies those rules immediately.

The system is designed to work the way you'd expect: keep sensitive files out of Git with `.gitignore`, and use `.ignore` when you need to hide files from ForgeCode's context without affecting Git.

**Already have a `.gitignore`?** You're done. ForgeCode uses it automatically.

**Need additional ignore rules?** Create a `.ignore` file in your project root.

**Files still showing up?** Check [troubleshooting](#troubleshooting) below.

ForgeCode checks multiple ignore sources when deciding whether to show a file. Here's the order of precedence (highest to lowest):

1. **`.ignore` files** - Highest priority, overrides everything else
2. **`.gitignore` files** - Standard Git ignore patterns
3. **Global gitignore** - Your personal ignore file (`~/.config/git/ignore`)
4. **`.git/info/exclude`** - Repository-specific excludes

**Key rule:** `.ignore` always wins. If you whitelist a file in `.ignore` (using `!pattern`), it will be visible even if `.gitignore` hides it.

### What Gets Filtered Out[​](#what-gets-filtered-out "Direct link to What Gets Filtered Out")

ForgeCode automatically skips:

- **Files matched by ignore patterns** - Checked in the precedence order above
- **Binary files** - Non-text content is excluded
- **Hidden files** - Files starting with `.` (except in your project root)

**Hidden file examples:**

- `.env` in project root → **Visible** ✓
- `.env` in `src/` subdirectory → **Hidden** ✗
- `.cache/` directory → **Hidden** ✗ (starts with `.`)
- `src/.DS_Store` → **Hidden** ✗ (hidden file in subdirectory)

**To show a hidden file:** Add `!.filename` to your `.ignore` file

### I Can't Find My File[​](#i-cant-find-my-file "Direct link to I Can't Find My File")

**First, figure out WHY it's hidden.** Common causes:

1. **Matched by an ignore pattern** (`.gitignore` or `.ignore`)
2. **Hidden file or directory** (starts with `.` and not in project root)
3. **Binary or non-text file** (ForgeCode skips these)

**Check if Git is ignoring it:**

**Example output:**

This means line 3 of `.gitignore` is hiding it.

**Important:** `git check-ignore` only checks `.gitignore` patterns. It won't tell you if a file is hidden by `.ignore` or other ForgeCode-specific filters.

**If `git check-ignore` shows nothing but the file is still hidden:**

- Check your `.ignore` file (Git doesn't know about `.ignore` files)
- Verify the file isn't in a hidden directory (like `.cache/`)
- Confirm it's a text file, not binary

**To make a file visible:**

If hidden by `.gitignore`, add to `.ignore`:

If it's a hidden file (starts with `.`), add to `.ignore`:

**Remember:** Changes to ignore files require restarting your ForgeCode session.

### My Ignore Patterns Aren't Working[​](#my-ignore-patterns-arent-working "Direct link to My Ignore Patterns Aren't Working")

**Pattern syntax checklist:**

✓ Use `/` for paths (even on Windows): `src/build/` not `src\build\`  
✓ Add trailing `/` for directories: `dist/` not `dist`  
✓ Patterns are relative to the ignore file location  
✓ Use `*` for wildcards: `*.log` matches all `.log` files  
✓ Use `**` for recursive matching: `**/temp/` matches `temp/` anywhere

**Test your pattern:**

**Precedence issues:**

If a file should be ignored but isn't:

1. Check if it's whitelisted with `!` in a `.ignore` file
2. Verify the pattern is in the right ignore file (`.ignore` overrides `.gitignore`)
3. Check for more nested ignore files that might override parent patterns

**Still not working?**

- Verify your ignore file is saved
- Restart your ForgeCode session (ignore rules are loaded at startup)
- Check for typos in file paths

### Still Having Issues?[​](#still-having-issues "Direct link to Still Having Issues?")

If you've tried the steps above and still can't figure out why a file is hidden or visible, export your session diagnostics:

Then share the output in [Discord](https://discord.gg/kRZBPPkgwq) along with:

1. **The specific file path** you're trying to ignore or include
2. **Your `.gitignore` and `.ignore` contents** (or the relevant patterns)
3. **What you expected** vs. what's actually happening
4. **Output from** `git check-ignore -v path/to/file`

This information helps us debug whether it's a pattern issue, precedence problem, or something else entirely.

- [Tag Files](https://forgecode.dev/docs/file-tagging/) - Reference specific files or code sections
- [AGENTS.md](https://forgecode.dev/docs/custom-rules-guide/) - Define project-specific AI guidelines

* * *

**Need help?** Export your session (`:dump html`) and reach out on [Discord](https://discord.gg/kRZBPPkgwq)