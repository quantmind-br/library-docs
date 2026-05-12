---
title: firectl user get
optimized: true
optimized_at: 2026-04-27T20:17:09Z
source: sitemap
fetched_at: 2026-04-27T20:17:09.979147656-03:00
rendered_js: false
tags:
    - command-line
    - cli-interface
    - user-commands
    - flags
    - global-options
    - fireworks
category: reference
word_count: 104
---
Retrieve a user by ID.

```
firectl user get <user-id>
```

### Examples

```
firectl user get my-user
firectl user get accounts/my-account/users/my-user
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it |
| `-h, --help` | | help for get |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |