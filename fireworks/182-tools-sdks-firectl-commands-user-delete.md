---
title: firectl user delete
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-delete
source: sitemap
fetched_at: 2026-04-27T20:17:07.090693078-03:00
rendered_js: false
word_count: 110
summary: Delete a user by ID or full resource name.
tags:
    - firectl-user
    - delete-command
    - cli-tool
    - flags
    - authentication
    - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Delete a user by ID or full resource name.

```bash
firectl user delete [flags]
```

## Examples

```bash
firectl user delete my-user
firectl user delete accounts/my-account/users/my-user
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
