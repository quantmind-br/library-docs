---
title: Workers RPC — Error Handling · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/rpc/error-handling/index.md
source: llms
fetched_at: 2026-01-24T15:30:13.090415948-03:00
rendered_js: false
word_count: 122
summary: This document explains how exceptions thrown by RPC methods are propagated to callers, detailing supported error types and limitations regarding property retention.
tags:
    - rpc
    - error-handling
    - exceptions
    - javascript
    - cloudflare-workers
category: reference
---

## Exceptions

An exception thrown by an RPC method implementation will propagate to the caller. If it is one of the standard JavaScript Error types, the `message` and prototype's `name` will be retained, though the stack trace is not.

### Unsupported error types

* If an [`AggregateError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError) is thrown by an RPC method, it is not propagated back to the caller.
* The [`SuppressedError`](https://github.com/tc39/proposal-explicit-resource-management?tab=readme-ov-file#the-suppressederror-error) type from the Explicit Resource Management proposal is not currently implemented or supported in Workers.
* Own properties of error objects, such as the [`cause`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) property, are not propagated back to the caller

## Additional properties

For some remote exceptions, the runtime may set properties on the propagated exception to provide more information about the error; see [Durable Object error handling](https://developers.cloudflare.com/durable-objects/best-practices/error-handling) for more details.