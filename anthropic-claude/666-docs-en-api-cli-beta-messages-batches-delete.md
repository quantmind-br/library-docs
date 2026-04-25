---
title: Delete a Message Batch (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/messages/batches/delete.md
source: llms
fetched_at: 2026-04-16T22:43:21.253510866-03:00
rendered_js: false
word_count: 81
summary: This document provides the API specification for deleting a completed message batch using a unique identifier.
tags:
    - api-reference
    - message-batches
    - deletion-process
    - anthropic-beta
category: api
---

## Delete

`$ ant beta:messages:batches delete`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```cli
ant beta:messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```