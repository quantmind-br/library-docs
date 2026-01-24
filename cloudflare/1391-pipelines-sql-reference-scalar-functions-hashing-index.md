---
title: Hashing functions · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/index.md
source: llms
fetched_at: 2026-01-24T15:19:38.597698021-03:00
rendered_js: false
word_count: 219
summary: This document provides a reference for cryptographic hash functions available in Cloudflare Pipelines, including digest, MD5, and various SHA algorithms.
tags:
    - cloudflare-pipelines
    - hash-functions
    - cryptography
    - datafusion
    - sql-functions
    - data-processing
category: reference
---

*Cloudflare Pipelines scalar function implementations are based on [Apache DataFusion](https://arrow.apache.org/datafusion/) (via [Arroyo](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `digest`

Computes the binary hash of an expression using the specified algorithm.

```plaintext
digest(expression, algorithm)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.

* **algorithm**: String expression specifying algorithm to use. Must be one of:

  * md5
  * sha224
  * sha256
  * sha384
  * sha512
  * blake2s
  * blake2b
  * blake3

## `md5`

Computes an MD5 128-bit checksum for a string expression.

```plaintext
md5(expression)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.

## `sha224`

Computes the SHA-224 hash of a binary string.

```plaintext
sha224(expression)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.

## `sha256`

Computes the SHA-256 hash of a binary string.

```plaintext
sha256(expression)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.

## `sha384`

Computes the SHA-384 hash of a binary string.

```plaintext
sha384(expression)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.

## `sha512`

Computes the SHA-512 hash of a binary string.

```plaintext
sha512(expression)
```

**Arguments**

* **expression**: String expression to operate on. Can be a constant, column, or function, and any combination of string operators.