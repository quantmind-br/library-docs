---
title: firectl secret update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/secret-update
source: sitemap
fetched_at: 2026-04-27T20:17:21.386908661-03:00
rendered_js: false
word_count: 183
summary: This document describes the `firectl secret update` command and its available flags, detailing how users can change an existing secret's value or source.
tags:
    - command-line
    - secret-management
    - firectl
    - update
    - flags
    - authentication
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl secret update

Update an existing secret's value or source.

```
firectl secret update [flags]
```

## Examples

```bash
firectl secret update --id MY_SECRET --value newvalue
firectl secret update --id AWS_CREDS --from-file aws-credentials.json
firectl secret update --id AWS_CREDS --aws-access-key-id AKIA... --aws-secret-access-key ...
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--aws-access-key-id` | string | AWS access key ID (automatically formats as JSON with `--aws-secret-access-key`) |
| `--aws-secret-access-key` | string | AWS secret access key (automatically formats as JSON with `--aws-access-key-id`) |
| `--dry-run` | | Print the request proto without running it |
| `--from-file` | string | Path to a file containing the secret value |
| `--id` | string | The id of the secret to be updated |
| `-o, --output` | Output | Set the output format to `text`, `json`, or `flag` (default `text`) |
| `--value` | string | The new value of the secret |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #secret-management #command-line #reference
