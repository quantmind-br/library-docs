---
title: firectl secret create
optimized: true
optimized_at: 2026-04-27T20:17:24Z
source: sitemap
fetched_at: 2026-04-27T20:17:24.268869707-03:00
rendered_js: false
tags:
    - command-line
    - secret-management
    - flags
    - aws-creds
    - creation
    - api
    - fireworks
category: reference
word_count: 168
---
Create a new secret.

```
firectl secret create [flags]
```

### Examples

```
firectl secret create --name MY_SECRET --value mysecretvalue
firectl secret create --name AWS_CREDS --from-file aws-credentials.json
firectl secret create --name AWS_CREDS --aws-access-key-id AKIA... --aws-secret-access-key ...
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--aws-access-key-id` | string | AWS access key ID (formats as JSON when paired with `--aws-secret-access-key`) |
| `--aws-secret-access-key` | string | AWS secret access key (formats as JSON when paired with `--aws-access-key-id`) |
| `--dry-run` | | Print the request proto without running it |
| `--from-file` | string | File containing the secret value |
| `--name` | string | **Required.** Name of the secret |
| `--value` | string | Secret value directly |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |