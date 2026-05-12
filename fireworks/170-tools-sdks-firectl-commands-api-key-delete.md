---
title: firectl api-key delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/api-key-delete
source: sitemap
fetched_at: 2026-04-27T20:18:03.352039282-03:00
rendered_js: false
word_count: 120
summary: This document describes the 'firectl api-key delete' command, which is used to remove an existing API key within the Firectl interface.
tags:
    - api-key
    - delete
    - firectl
    - command
    - flags
    - authentication
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl api-key delete

Delete an API key by ID.

```
firectl api-key delete [flags]
```

## Examples

```bash
firectl api-key delete key-id
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it |
| `-h, --help` | | help for delete |
| `-o, --output` | Output | Set the output format to `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #api-key #delete #command-line #reference
