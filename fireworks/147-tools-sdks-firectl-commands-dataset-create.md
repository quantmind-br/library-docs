---
title: firectl dataset create
optimized: true
optimized_at: 2026-04-27T20:17:54Z
source: sitemap
fetched_at: 2026-04-27T20:17:54.465817949-03:00
rendered_js: false
tags:
    - command-line
    - dataset-creation
    - flags
    - cli-tool
    - firectl
category: reference
word_count: 200
---
Create a new dataset.

```
firectl dataset create [flags]
```

### Examples

```
firectl dataset create my-dataset /path/to/dataset.jsonl
firectl dataset create --trace-from-model-id model_abc --format chat --date 2024-01-10 my-dataset
firectl dataset create my-dataset --external-url gs://bucket-name/object-name
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--display-name` | string | Display name of the dataset |
| `--dry-run` | | Print the request proto without running it |
| `--end-time` | string | End time for trace data (`YYYY-MM-DD`). Trace datasets only |
| `--eval-protocol-output` | | Dataset is in eval protocol output format |
| `--external-url` | string | GCS URI of the dataset file |
| `--filter` | string | Filter condition for source dataset |
| `--source` | string | Source dataset ID to filter from |
| `--start-time` | string | Start time for trace data (`YYYY-MM-DD`). Trace datasets only |
| `--quiet` | | Suppress upload progress bar |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |