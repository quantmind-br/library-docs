---
title: firectl model create
optimized: true
optimized_at: 2026-04-27T20:17:38Z
source: sitemap
fetched_at: 2026-04-27T20:17:38.639001352-03:00
rendered_js: false
tags:
    - cli-command
    - model-creation
    - firectl-tool
    - flag-options
    - deployment
    - storage-upload
    - fireworks
category: reference
word_count: 240
---
Create a new model.

```
firectl model create <model-id> <source> [flags]
```

### Examples

```
firectl model create my-model /path/to/checkpoint/
firectl model create my-model s3://bucket/path --role-arn arn:aws:iam::123456789012:role/MyRole
firectl model create my-model https://storage-account.blob.core.windows.net/container/path --azure-sas-token-secret accounts/{account}/secrets/{secret}
firectl model create my-model https://storage-account.blob.core.windows.net/container/path --azure-client-id <client-id> --azure-tenant-id <tenant-id>
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | PEFT addon base model |
| `--default-draft-model` | string | Default speculative draft model for deployments |
| `--default-draft-token-count` | int32 | Default speculative draft token count |
| `--description` | string | Model description |
| `--display-name` | string | Display name |
| `--dry-run` | | Print the request proto without running it |
| `--embedding` | | Set model kind to embeddings base model |
| `--enable-resumable-upload` | | Use resumable upload |
| `--github-url` | string | GitHub repository URL |
| `--hugging-face-url` | string | Hugging Face model URL |
| `--poll-duration` | duration | Poll duration for import completion (default `2h`) |
| `--public` | | Make model publicly accessible |
| `--quiet` | | Suppress upload progress bar |
| `--supports-image-input` | | Model supports image inputs |
| `--supports-tools` | | Model supports function calling |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |