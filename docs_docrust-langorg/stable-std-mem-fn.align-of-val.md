---
title: align_of_val in std::mem - Rust
url: https://doc.rust-lang.org/stable/std/mem/fn.align_of_val.html
source: crawler
fetched_at: 2026-05-06T21:25:27.962120197-03:00
rendered_js: false
word_count: 44
summary: This document provides the API definition for the align_of_val function in Rust, which retrieves the ABI-required minimum alignment for a given value's type.
tags:
    - rust
    - memory-management
    - abi
    - alignment
    - standard-library
category: api
---

[std](https://doc.rust-lang.org/stable/std/index.html)::[mem](https://doc.rust-lang.org/stable/std/mem/index.html)

## Function align\_of\_val

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/mem/mod.rs.html#519)

```rust
pub const fn align_of_val<T>(val: &T) -> usize
where
    T: ?Sized,
```

Expand description

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of the type of the value that `val` points to in bytes.

Every reference to a value of the type `T` must be a multiple of this number.

## [§](#examples)Examples

```rust
assert_eq!(4, align_of_val(&5i32));
```