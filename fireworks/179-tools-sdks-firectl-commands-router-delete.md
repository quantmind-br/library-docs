---
title: firectl router delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-delete
source: sitemap
fetched_at: 2026-04-27T20:16:30.352594707-03:00
rendered_js: false
word_count: 110
summary: Delete a router by ID or full resource name.
tags:
    - firectl
    - router-delete
    - cli-command
    - flags
    - api-tool
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a router by ID or full resource name.

```bash
firectl router delete [flags]
```

## Examples

```bash
firectl router delete my-router
firectl router delete accounts/my-account/routers/my-router
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
