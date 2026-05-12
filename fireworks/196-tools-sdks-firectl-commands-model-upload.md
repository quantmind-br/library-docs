---
title: firectl model upload - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-upload
source: sitemap
fetched_at: 2026-04-27T20:17:33.386316775-03:00
rendered_js: false
word_count: 83
summary: This document describes the `firectl model upload` command, which is used to resume or complete a previously interrupted model upload operation.
tags:
    - cli-command
    - model-upload
    - fireworks-tool
    - resuming-uploads
    - flags
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
Resumes or completes a model upload for an existing model. Use after an interrupted upload.

```bash
firectl model upload [flags]
```

**Examples**

```bash
firectl model upload my-model /path/to/checkpoint/
```

| Flag | Type | Description |
|------|------|-------------|
| `--quiet` | flag | Suppress the upload progress bar. |

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |