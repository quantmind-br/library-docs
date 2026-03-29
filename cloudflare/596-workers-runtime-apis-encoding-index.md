---
title: Encoding · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/runtime-apis/encoding/index.md
source: llms
fetched_at: 2026-01-24T15:27:01.883188149-03:00
rendered_js: false
word_count: 175
summary: This document provides a technical overview of the TextEncoder and TextDecoder interfaces used for converting strings to UTF-8 byte streams and vice versa.
tags:
    - javascript
    - web-api
    - text-encoding
    - utf-8
    - data-conversion
category: api
---

## TextEncoder

### Background

The `TextEncoder` takes a stream of code points as input and emits a stream of bytes. Encoding types passed to the constructor are ignored and a UTF-8 `TextEncoder` is created.

[`TextEncoder()`](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder) returns a newly constructed `TextEncoder` that generates a byte stream with UTF-8 encoding. `TextEncoder` takes no parameters and throws no exceptions.

### Constructor

```js
let encoder = new TextEncoder();
```

### Properties

* `encoder.encoding` DOMString read-only
  * The name of the encoder as a string describing the method the `TextEncoder` uses (always `utf-8`).

### Methods

* `encode(inputUSVString)` : Uint8Array

  * Encodes a string input.

***

## TextDecoder

### Background

The `TextDecoder` interface represents a UTF-8 decoder. Decoders take a stream of bytes as input and emit a stream of code points.

[`TextDecoder()`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder) returns a newly constructed `TextDecoder` that generates a code-point stream.

### Constructor

```js
let decoder = new TextDecoder();
```

### Properties

* `decoder.encoding` DOMString read-only

  * The name of the decoder that describes the method the `TextDecoder` uses.

* `decoder.fatal` boolean read-only

  * Indicates if the error mode is fatal.

* `decoder.ignoreBOM` boolean read-only

  * Indicates if the byte-order marker is ignored.

### Methods

* `decode()` : DOMString
  * Decodes using the method specified in the `TextDecoder` object. Learn more at [MDN’s `TextDecoder` documentation](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/decode).