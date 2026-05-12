---
title: align_of in std::mem - Rust
url: https://doc.rust-lang.org/std/mem/fn.align_of.html
source: crawler
fetched_at: 2026-05-06T21:24:42.439327841-03:00
rendered_js: false
word_count: 53
summary: This document describes the Rust standard library function align_of, which returns the ABI-required minimum alignment for a given type in bytes.
tags:
    - rust
    - memory-management
    - abi
    - alignment
    - std-mem
    - data-types
category: reference
---

[std](https://doc.rust-lang.org/std/index.html)::[mem](https://doc.rust-lang.org/std/mem/index.html)

## Function align\_of

1.0.0 (const: 1.24.0) · [Source](https://doc.rust-lang.org/src/core/mem/mod.rs.html#499)

```rust
pub const fn align_of<T>() -> usize
```

Expand description

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of a type in bytes.

Every reference to a value of the type `T` must be a multiple of this number.

This is the alignment used for struct fields. It may be smaller than the preferred alignment.

## [§](#examples)Examples

```rust
assert_eq!(4, align_of::<i32>());
```