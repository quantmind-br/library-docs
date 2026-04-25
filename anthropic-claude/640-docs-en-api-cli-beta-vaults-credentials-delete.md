---
title: Delete Credential (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/credentials/delete.md
source: llms
fetched_at: 2026-04-16T22:43:52.875799682-03:00
rendered_js: false
word_count: 59
summary: This document provides the API specification for deleting a specific credential within a vault using the Anthropic CLI.
tags:
    - api-reference
    - vaults
    - credential-management
    - cli-command
category: api
---

## Delete

`$ ant beta:vaults:credentials delete`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_credential: object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Example

```cli
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```