---
title: ReadableStreamBYOBReader · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/index.md
source: llms
fetched_at: 2026-01-24T15:30:57.903736902-03:00
rendered_js: false
word_count: 212
summary: This document describes the ReadableStreamBYOBReader interface, which enables efficient reading of stream data into developer-provided buffers to minimize memory copying.
tags:
    - streams-api
    - byob-reader
    - buffer-management
    - cloudflare-workers
    - performance-optimization
category: api
---

## Background

`BYOB` is an abbreviation of bring your own buffer. A `ReadableStreamBYOBReader` allows reading into a developer-supplied buffer, thus minimizing copies.

An instance of `ReadableStreamBYOBReader` is functionally identical to [`ReadableStreamDefaultReader`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/) with the exception of the `read` method.

A `ReadableStreamBYOBReader` is not instantiated via its constructor. Rather, it is retrieved from a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/):

```js
const { readable, writable } = new TransformStream();
const reader = readable.getReader({ mode: 'byob' });
```

***

## Methods

* `read(bufferArrayBufferView)` : Promise\<ReadableStreamBYOBReadResult>

  * Returns a promise with the next available chunk of data read into a passed-in buffer.

* `readAtLeast(minBytes, bufferArrayBufferView)` : Promise\<ReadableStreamBYOBReadResult>

  * Returns a promise with the next available chunk of data read into a passed-in buffer. The promise will not resolve until at least `minBytes` have been read.

***

## Common issues

Warning

`read` provides no control over the minimum number of bytes that should be read into the buffer. Even if you allocate a 1 MiB buffer, the kernel is perfectly within its rights to fulfill this read with a single byte, whether or not an EOF immediately follows.

In practice, the Workers team has found that `read` typically fills only 1% of the provided buffer.

`readAtLeast` is a non-standard extension to the Streams API which allows users to specify that at least `minBytes` bytes must be read into the buffer before resolving the read.

***

## Related resources

* [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
* [Background about BYOB readers in the Streams API WHATWG specification](https://streams.spec.whatwg.org/#byob-readers)