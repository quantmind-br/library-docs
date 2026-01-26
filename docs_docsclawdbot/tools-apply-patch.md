---
title: "null"
url: https://docs.clawd.bot/tools/apply-patch.md
source: llms
fetched_at: 2026-01-26T10:15:39.968505343-03:00
rendered_js: false
word_count: 132
summary: This document describes the apply_patch tool, which enables multi-file and multi-hunk edits using a specific structured patch syntax. It outlines the tool's parameters, configuration options, and supported file operations like adding, updating, and deleting files.
tags:
    - apply-patch
    - file-operations
    - patch-syntax
    - workspace-management
    - openai-tools
    - developer-utilities
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# apply\_patch tool

Apply file changes using a structured patch format. This is ideal for multi-file
or multi-hunk edits where a single `edit` call would be brittle.

The tool accepts a single `input` string that wraps one or more file operations:

```
*** Begin Patch
*** Add File: path/to/file.txt
+line 1
+line 2
*** Update File: src/app.ts
@@
-old line
+new line
*** Delete File: obsolete.txt
*** End Patch
```

## Parameters

* `input` (required): Full patch contents including `*** Begin Patch` and `*** End Patch`.

## Notes

* Paths are resolved relative to the workspace root.
* Use `*** Move to:` within an `*** Update File:` hunk to rename files.
* `*** End of File` marks an EOF-only insert when needed.
* Experimental and disabled by default. Enable with `tools.exec.applyPatch.enabled`.
* OpenAI-only (including OpenAI Codex). Optionally gate by model via
  `tools.exec.applyPatch.allowModels`.
* Config is only under `tools.exec`.

## Example

```json  theme={null}
{
  "tool": "apply_patch",
  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"
}
```