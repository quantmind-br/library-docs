---
title: Delete Session (Beta) (Ruby)
url: https://platform.claude.com/docs/en/api/ruby/beta/sessions/delete.md
source: llms
fetched_at: 2026-04-16T22:45:00.167617342-03:00
rendered_js: false
word_count: 50
summary: This document provides the technical specification for deleting a session via the beta API, including parameter details and return types.
tags:
    - api-reference
    - session-management
    - beta-features
    - anthropic-api
category: api
---

## Delete

`beta.sessions.delete(session_id, **kwargs) -> BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `session_id: String`

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

- `class BetaManagedAgentsDeletedSession`

  Confirmation that a `session` has been permanently deleted.

  - `id: String`

  - `type: :session_deleted`

    - `:session_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_session = anthropic.beta.sessions.delete("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_deleted_session)
```