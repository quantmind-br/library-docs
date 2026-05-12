---
title: firectl user create - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-create
source: sitemap
fetched_at: 2026-04-27T20:16:21.967871602-03:00
rendered_js: false
word_count: 201
summary: Create a new user or service account in Fireworks using the firectl CLI.
tags:
    - cli-command
    - user-creation
    - flag-reference
    - firectl
    - authentication
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl user create

Create a new user or service account.

```bash
firectl user create [flags]
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--display-name` | string | — | Display name of the user |
| `--dry-run` | flag | — | Print the request proto without running it |
| `--email` | string | — | Email address (not required for service accounts) |
| `--permission-preset` | string | — | Permission preset for the service account. Automatically sets `role` to `"custom"` |
| `--role` | string | `user` | Role: `user`, `admin`, `contributor`, `inference-user`, or `custom` |
| `--service-account` | flag | — | Admin only: Create as a service account (email auto-generated) |
| `--user-id` | string | — | User ID (required for service accounts) |
| `-o, --output` | Output | `text` | Output format: `text`, `json`, or `flag` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl user create --email="alice.cullen@gmail.com"

firectl user create --service-account --user-id="my-bot"

firectl user create --service-account --user-id="my-agent" --permission-preset=agent
```

#cli #user-creation #firectl #service-account
