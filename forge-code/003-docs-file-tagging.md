---
title: "File Tagging in ForgeCode"
url: https://forgecode.dev/docs/file-tagging/
source: sitemap
fetched_at: 2026-04-30T14:09:06.635345177-03:00
rendered_js: false
word_count: 151
summary: "Attach project context directly in prompts using `@` references for files, directories, and images."
tags:
  - file-tagging
  - context-management
  - ide-integration
  - prompt-engineering
  - developer-tools
category: guide
optimized: true
---
# File Tagging in ForgeCode

> **TL;DR**
> Use `@` + `TAB` to attach files, directories, or images to prompts for immediate context.

## How It Works
1. Type `@` followed by a partial name.
2. Press `TAB` to open the fuzzy picker.
3. Select the file/directory/image.

> **Note**: `.gitignore` rules apply. Ignored paths won't appear.

## Tagging Scopes

| Scope | Example | Use Case |
|-------|---------|----------|
| **File** | `@src/utils/auth.ts` | Provide code context |
| **Directory** | `@src/components/` | Work across multiple files |
| **Image** | `@design/mockup.png` | Visual context (UI, diagrams) |

## Best Practices
- **Large files**: Tag smaller scopes (e.g., `@file:120:180`) to avoid size limits.
- **Precision**: Use focused files or line ranges for clarity.
- **Formats**: PNG, JPG, JPEG, SVG, WebP supported for images.

## Troubleshooting
- **Missing files**: Check `.gitignore` or [Ignoring Files](https://forgecode.dev/docs/ignoring-files/).
- **Size limits**: Split tasks or use smaller scopes.