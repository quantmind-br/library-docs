---
title: Delete Session (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/delete.md
source: llms
fetched_at: 2026-04-16T22:44:48.399513681-03:00
rendered_js: false
word_count: 51
summary: This document provides the API reference for deleting a specific session using the beta CLI command, detailing required parameters and the return object structure.
tags:
    - api-reference
    - session-management
    - cli-command
    - anthropic-beta
category: api
---

## Delete

`$ ant beta:sessions delete`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_session: object { id, type }`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Example

```cli
ant beta:sessions delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```