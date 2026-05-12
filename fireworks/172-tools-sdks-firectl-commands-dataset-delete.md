---
title: firectl dataset delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-delete
source: sitemap
fetched_at: 2026-04-27T20:17:59.756786785-03:00
rendered_js: false
word_count: 149
summary: This document describes the command for deleting datasets using the 'firectl' tool, detailing various flags that can modify the execution of the deletion operation.
tags:
    - command-line
    - dataset-deletion
    - firectl
    - api-interaction
    - cli-flags
    - resource-management
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dataset delete

Delete a dataset.

```
firectl dataset delete [flags]
```

## Examples

```bash
firectl dataset delete my-dataset
firectl dataset delete accounts/my-account/datasets/my-dataset
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | | | Print the request proto without running it |
| `-h, --help` | | | help for delete |
| `-o, --output` | Output | `text` | Set the output format to `text`, `json`, or `flag` |
| `--wait` | | | Wait until the dataset is deleted |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait` flag |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #dataset #delete #command-line #reference
