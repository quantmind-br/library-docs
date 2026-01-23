---
title: Code Execution Extension | goose
url: https://block.github.io/goose/docs/mcp/code-execution-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:52.402006173-03:00
rendered_js: true
word_count: 93
summary: This document explains how to automate the creation of a LOG.md file that captures git branch details, recent commit history, and the project version from package.json.
tags:
    - git-metadata
    - automation
    - logging
    - package-json
    - version-tracking
    - git-history
category: guide
---

I'll help you create a LOG.md file with the git branch, last 3 commits, and version from package.json. Let me gather all this information in one operation.

`Execute Code code: import { shell, text_editor } from "developer" ...`

Let me check the package.json path first:

`Execute Code code: import { shell, text_editor } from "developer" ...`

Perfect! I've created the **LOG.md** file with:

- ✅ **Current git branch**
- ✅ **Last 3 commits** (with hash, message, author, and relative time)
- ✅ **Version** from ui/desktop/package.json

The file has been saved to the root directory as `LOG.md`.