---
title: firectl secret delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/secret-delete
source: sitemap
fetched_at: 2026-04-27T20:17:23.614696845-03:00
rendered_js: false
word_count: 106
summary: Delete a secret by name.
tags:
    - command
    - secret-management
    - delete
    - flags
    - cli-tool
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a secret by name.

```bash
firectl secret delete [flags]
```

## Examples

```bash
firectl secret delete MY_SECRET
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
