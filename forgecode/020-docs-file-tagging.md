---
title: ForgeCode
url: https://forgecode.dev/docs/file-tagging/
source: sitemap
fetched_at: 2026-03-29T14:51:53.988620369-03:00
rendered_js: false
word_count: 204
summary: This document explains how to use file tagging in ForgeCode to attach project context directly in prompts using @ references, with support for files, directories, and images.
tags:
    - file-tagging
    - prompt-context
    - code-reference
    - file-attachments
    - visual-context
category: guide
---

File tagging lets you attach project context directly in your prompt with `@` references.

Press `TAB` to complete file tags

Type `@` followed by a partial file or directory name, then press **`TAB`** . A fuzzy picker opens — type to filter, arrow keys to navigate, `Enter` to select. The full path is inserted automatically.

`.gitignore` is respected; ignored paths won't appear in the list.

Files can be ignored using [Ignoring Files](https://forgecode.dev/docs/ignoring-files/). Ignored files and directories are not listed in tagging suggestions.

### Files[​](#files "Direct link to Files")

Tag a file to give ForgeCode direct code context:

### Directories[​](#directories "Direct link to Directories")

Tag a directory when you want to work across a folder:

This is useful when your task spans multiple related files.

### Images[​](#images "Direct link to Images")

Tag images for visual context (UI states, mockups, diagrams):

Supported formats include PNG, JPG, JPEG, SVG, and WebP.

Tagged files are auto-attached to the prompt, so the agent gets context immediately. This saves a round trip where you would otherwise need to re-send or paste content manually.

Be careful when tagging very large files. Extremely large files can fail to attach due to size limits.

When that happens, tag smaller scopes instead:

- Use a more focused file
- Use line ranges like `@[src/auth/AuthService.ts:120:180]`
- Split the task across multiple smaller tags