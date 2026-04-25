---
title: Delete Environment (Beta) (Ruby)
url: https://platform.claude.com/docs/en/api/ruby/beta/environments/delete.md
source: llms
fetched_at: 2026-04-16T22:44:18.359120376-03:00
rendered_js: false
word_count: 56
summary: This document specifies the API endpoint and parameters required to delete a specific beta environment via its unique identifier.
tags:
    - api-reference
    - beta-features
    - environment-management
    - anthropic-sdk
category: api
---

## Delete

`beta.environments.delete(environment_id, **kwargs) -> BetaEnvironmentDeleteResponse`

**delete** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"advisor-tool-2026-03-01"`

    - `:"user-profiles-2026-03-24"`

### Returns

- `class BetaEnvironmentDeleteResponse`

  Response after deleting an environment.

  - `id: String`

    Environment identifier

  - `type: :environment_deleted`

    The type of response

    - `:environment_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_environment_delete_response = anthropic.beta.environments.delete("env_011CZkZ9X2dpNyB7HsEFoRfW")

puts(beta_environment_delete_response)
```