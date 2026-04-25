---
title: Delete a Message Batch (Go)
url: https://platform.claude.com/docs/en/api/go/messages/batches/delete.md
source: llms
fetched_at: 2026-04-16T22:43:40.881776876-03:00
rendered_js: false
word_count: 62
summary: This document provides the API reference for deleting a message batch once its processing is complete.
tags:
    - api-reference
    - message-batch
    - deletion-process
    - endpoint-documentation
category: api
---

## Delete

`client.Messages.Batches.Delete(ctx, messageBatchID) (*DeletedMessageBatch, error)`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `messageBatchID string`

  ID of the Message Batch.

### Returns

- `type DeletedMessageBatch struct{…}`

  - `ID string`

    ID of the Message Batch.

  - `Type MessageBatchDeleted`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `const MessageBatchDeletedMessageBatchDeleted MessageBatchDeleted = "message_batch_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  deletedMessageBatch, err := client.Messages.Batches.Delete(context.TODO(), "message_batch_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", deletedMessageBatch.ID)
}
```