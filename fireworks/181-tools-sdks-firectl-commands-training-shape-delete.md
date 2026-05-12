---
title: firectl training-shape delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-delete
source: sitemap
fetched_at: 2026-04-27T20:16:02.987790149-03:00
rendered_js: false
word_count: 79
summary: Delete a training shape by ID or full resource name.
tags:
    - command
    - delete
    - training-shape
    - fireworks
    - firectl
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a training shape by ID or full resource name.

```bash
firectl training-shape delete <training-shape-id> [flags]
```

## Examples

```bash
firectl training-shape delete my-shape
firectl training-shape delete accounts/my-account/trainingShapes/my-shape
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `-h`, `--help` | | help for delete |

## Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Defaults to `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key for authentication. |
| `-p`, `--profile` | string | fireworks auth and settings profile to use. |
