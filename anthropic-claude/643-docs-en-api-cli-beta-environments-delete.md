---
title: Delete Environment (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/environments/delete.md
source: llms
fetched_at: 2026-04-16T22:44:06.486598724-03:00
rendered_js: false
word_count: 54
summary: This document provides the technical specification for deleting an environment using a unique identifier via the beta command-line interface.
tags:
    - cli-command
    - environment-management
    - api-reference
    - deletion-process
category: api
---

## Delete

`$ ant beta:environments delete`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_environment_delete_response: object { id, type }`

  Response after deleting an environment.

  - `id: string`

    Environment identifier

  - `type: "environment_deleted"`

    The type of response

### Example

```cli
ant beta:environments delete \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```