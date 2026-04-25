---
title: Delete File (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/files/delete.md
source: llms
fetched_at: 2026-04-16T22:44:26.197899653-03:00
rendered_js: false
word_count: 45
summary: This document defines the API endpoint and parameters required to delete a specific file using the Anthropic beta CLI tool.
tags:
    - api-reference
    - file-management
    - cli-command
    - anthropic-beta
category: api
---

## Delete

`$ ant beta:files delete`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```cli
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```