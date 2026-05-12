---
title: firectl model download
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-download
source: sitemap
fetched_at: 2026-04-27T20:17:37.050007063-03:00
rendered_js: false
word_count: 94
summary: Download a model checkpoint to a local directory.
tags:
  - command-line
  - model-download
  - flags
  - authentication
  - fireworks
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl model download

Download a model checkpoint to a local directory.

## Usage

```bash
firectl model download [flags]
```

## Examples

```bash
firectl model download my-model /path/to/checkpoint/
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--quiet` | | Suppress the upload progress bar. |
| `-h, --help` | | Help for download. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
