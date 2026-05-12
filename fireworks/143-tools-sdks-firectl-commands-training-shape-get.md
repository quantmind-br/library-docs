---
title: firectl training-shape get
optimized: true
optimized_at: 2026-04-27T20:16:13Z
source: sitemap
fetched_at: 2026-04-27T20:16:13.556502906-03:00
rendered_js: false
tags:
    - command
    - training-shape
    - get
    - fireworks
    - cli
    - retrieval
category: reference
word_count: 104
---
`firectl training-shape get <training-shape-id> [flags]`

### Examples

```
firectl training-shape get my-shape
firectl training-shape get accounts/my-account/trainingShapes/my-shape
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