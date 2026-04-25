---
title: Get Session Resource (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/resources/retrieve.md
source: llms
fetched_at: 2026-04-16T22:50:39.596186075-03:00
rendered_js: false
word_count: 71
summary: This document defines the API endpoint and parameter structure for retrieving a specific resource within a session, supporting both GitHub repositories and files.
tags:
    - api-reference
    - session-management
    - resource-retrieval
    - beta-features
category: api
---

## Retrieve

`$ ant beta:sessions:resources retrieve`

**get** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSessionResourceGetResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource`

  The requested session resource.

  - `beta_managed_agents_github_repository_resource: object { id, created_at, mount_path, 4 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `mount_path: string`

    - `type: "github_repository"`

      - `"github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

  - `beta_managed_agents_file_resource: object { id, created_at, file_id, 3 more }`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

      - `"file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

### Example

```cli
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```