---
title: firectl dataset download
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-download
source: sitemap
fetched_at: 2026-04-27T20:17:57.415627188-03:00
rendered_js: false
word_count: 129
summary: Download a single dataset or an entire lineage chain.
tags:
  - command-reference
  - dataset-download
  - flags
  - fireworks
  - lineage-tracking
  - cli
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dataset download

Download a dataset to a local directory, optionally including its full lineage chain.

## Usage

```bash
firectl dataset download [flags]
```

## Examples

```bash
# Download a single dataset
firectl dataset download my-dataset --output-dir /path/to/download

# Download entire lineage chain (only for batch inference continuation jobs)
firectl dataset download my-dataset --download-lineage --output-dir /path/to/download
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--download-lineage` | | | Download entire lineage chain (all related datasets). |
| `--output-dir` | string | `"."` | Directory to download dataset files to. |
| `--quiet` | | | Suppress download progress output. |
| `-h, --help` | | | Help for download. |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |
