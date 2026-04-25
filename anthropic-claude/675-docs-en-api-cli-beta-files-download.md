---
title: Download File (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/files/download.md
source: llms
fetched_at: 2026-04-16T22:46:30.213988119-03:00
rendered_js: false
word_count: 37
summary: This document provides the technical specification and usage instructions for downloading files via a beta API endpoint.
tags:
    - cli-command
    - api-reference
    - file-management
    - anthropic-beta
category: api
---

## Download

`$ ant beta:files download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `unnamed_schema_0: file path`

### Example

```cli
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```