---
title: firectl batch-inference-job create
optimized: true
optimized_at: 2026-04-27T20:18:00Z
source: sitemap
fetched_at: 2026-04-27T20:18:00.437088474-03:00
rendered_js: false
tags:
    - batch-inference
    - job-creation
    - command-line
    - flags
    - model-serving
    - fireworks
category: reference
word_count: 257
---
Create a batch inference job.

```
firectl batch-inference-job create [flags]
```

### Examples

```
firectl batch-inference-job create --input-dataset-id my-dataset --output-dataset-id my-output-dataset --model my-model \
    --job-id my-job --max-tokens 1024 --temperature 0.7 --top-p 0.9 --top-k 50 --n 2 --precision FP16 \
    --extra-body '{"stop": ["\n"], "presence_penalty": 0.5}'
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--job-id` | string | Job ID (auto-generated if unset) |
| `--display-name` | string | Display name of the job |
| `-m, --model` | string | Model for inference |
| `-d, --input-dataset-id` | string | Input dataset ID |
| `-x, --output-dataset-id` | string | Output dataset ID (auto-generated if unset) |
| `--continue-from` | string | Continue from existing job by ID or resource name |
| `--max-tokens` | int32 | Max tokens per response |
| `--temperature` | float32 | Sampling temperature (0–2) |
| `--top-p` | float32 | Top-p sampling (0–1) |
| `--top-k` | int32 | Top-k token limit |
| `--n` | int32 | Number of response candidates per input |
| `--extra-body` | string | Additional inference params as JSON (e.g., `'{"stop": ["\n"]}'`) |
| `--precision` | string | Serving precision; auto-selected if unspecified |
| `--quiet` | | Suppress output except errors |
| `--dry-run` | | Print the request proto without running it |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |