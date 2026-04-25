---
title: Delete Session (Beta) (TypeScript)
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/delete.md
source: llms
fetched_at: 2026-04-16T22:45:04.201327816-03:00
rendered_js: false
word_count: 31
summary: This documentation defines the API method for permanently deleting a specific session through the beta managed agents interface.
tags:
    - api-reference
    - session-management
    - beta-features
    - anthropic-sdk
category: api
---

## Delete

`client.beta.sessions.delete(stringsessionID, SessionDeleteParamsparams?, RequestOptionsoptions?): BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID: string`

- `params: SessionDeleteParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 20 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"advisor-tool-2026-03-01"`

      - `"user-profiles-2026-03-24"`

### Returns

- `BetaManagedAgentsDeletedSession`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

    - `"session_deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedSession = await client.beta.sessions.delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
);

console.log(betaManagedAgentsDeletedSession.id);
```