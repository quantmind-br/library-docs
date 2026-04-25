---
title: Delete a Message Batch (cli)
url: https://platform.claude.com/docs/en/api/cli/messages/batches/delete.md
source: llms
fetched_at: 2026-04-16T22:43:37.661636377-03:00
rendered_js: false
word_count: 65
summary: This documentation provides the syntax and parameters required to permanently remove a processed message batch from the system using the CLI command.
tags:
    - cli-command
    - message-batches
    - api-reference
    - deletion-process
category: api
---

## Delete

`$ ant messages:batches delete`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

### Returns

- `deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```cli
ant messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```