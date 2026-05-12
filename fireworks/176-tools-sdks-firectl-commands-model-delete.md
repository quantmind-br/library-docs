---
title: firectl model delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-delete
source: sitemap
fetched_at: 2026-04-27T20:17:32.6414314-03:00
rendered_js: false
word_count: 110
summary: Delete a model by ID or full resource name.
tags:
    - command
    - model-management
    - delete
    - flags
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a model by ID or full resource name.

```bash
firectl model delete [flags]
```

## Examples

```bash
firectl model delete my-model
firectl model delete accounts/my-account/models/my-model
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | bool | | Print the request proto without running it. |
| `-h`, `--help` | | | help for delete |
| `-o`, `--output` | Output | `text` | Output format: `text`, `json`, or `flag`. |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Defaults to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication. |
| `-p`, `--profile` | string | fireworks auth and settings profile to use. |
