---
title: WritableStream · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/index.md
source: llms
fetched_at: 2026-01-24T15:30:59.622746012-03:00
rendered_js: false
word_count: 175
summary: This document provides a reference for the WritableStream API, detailing its properties, methods, and usage patterns for handling stream data in Cloudflare Workers.
tags:
    - writable-stream
    - streams-api
    - cloudflare-workers
    - javascript-runtime
    - web-streams
category: api
---

## Background

A `WritableStream` is the `writable` property of a [`TransformStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/). On the Workers platform, `WritableStream` cannot be directly created using the `WritableStream` constructor.

A typical way to write to a `WritableStream` is to pipe a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/) to it.

```js
readableStream
  .pipeTo(writableStream)
  .then(() => console.log('All data successfully written!'))
  .catch(e => console.error('Something went wrong!', e));
```

To write to a `WritableStream` directly, you must use its writer.

```js
const writer = writableStream.getWriter();
writer.write(data);
```

Refer to the [WritableStreamDefaultWriter](https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/) documentation for further detail.

## Properties

* `locked` boolean

  * A Boolean value to indicate if the writable stream is locked to a writer.

## Methods

* `abort(reasonstringoptional)` : Promise\<void>

  * Aborts the stream. This method returns a promise that fulfills with a response `undefined`. `reason` is an optional human-readable string indicating the reason for cancellation. `reason` will be passed to the underlying sink’s abort algorithm. If this writable stream is one side of a [TransformStream](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/), then its abort algorithm causes the transform’s readable side to become errored with `reason`.

  Warning

  Any data not yet written is lost upon abort.

* `getWriter()` : WritableStreamDefaultWriter

  * Gets an instance of `WritableStreamDefaultWriter` and locks the `WritableStream` to that writer instance.

***

## Related resources

* [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
* [Writable streams in the WHATWG Streams API specification](https://streams.spec.whatwg.org/#ws-model)