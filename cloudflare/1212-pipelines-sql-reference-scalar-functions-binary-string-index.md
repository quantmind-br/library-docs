---
title: Binary string functions · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/index.md
source: llms
fetched_at: 2026-01-24T15:19:36.043727557-03:00
rendered_js: false
word_count: 71
summary: This document defines the encode and decode scalar functions used in Cloudflare Pipelines for converting binary data to and from textual formats like base64 and hex.
tags:
    - cloudflare-pipelines
    - datafusion
    - binary-data
    - encoding
    - decoding
    - data-transformation
category: reference
---

*Cloudflare Pipelines scalar function implementations are based on [Apache DataFusion](https://arrow.apache.org/datafusion/) (via [Arroyo](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `encode`

Encode binary data into a textual representation.

```plaintext
encode(expression, format)
```

**Arguments**

* **expression**: Expression containing string or binary data

* **format**: Supported formats are: `base64`, `hex`

**Related functions**: [decode](#decode)

## `decode`

Decode binary data from textual representation in string.

```plaintext
decode(expression, format)
```

**Arguments**

* **expression**: Expression containing encoded string data

* **format**: Same arguments as [encode](#encode)

**Related functions**: [encode](#encode)