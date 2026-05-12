---
title: size_of_val in std::mem - Rust
url: https://doc.rust-lang.org/stable/std/mem/fn.size_of_val.html
source: crawler
fetched_at: 2026-05-06T21:25:28.656256263-03:00
rendered_js: false
word_count: 54
summary: This document describes the Rust function size_of_val, which returns the size in bytes of a value, including dynamically-sized types like slices or trait objects.
tags:
    - rust
    - memory-management
    - type-system
    - byte-size
    - dynamically-sized-types
category: reference
---

[std](https://doc.rust-lang.org/stable/std/index.html)::[mem](https://doc.rust-lang.org/stable/std/mem/index.html)

## Function size\_of\_val

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/mem/mod.rs.html#372)

```rust
pub const fn size_of_val<T>(val: &T) -> usize
where
    T: ?Sized,
```

Expand description

Returns the size of the pointed-to value in bytes.

This is usually the same as [`size_of::<T>()`](https://doc.rust-lang.org/stable/std/mem/fn.size_of.html "fn std::mem::size_of"). However, when `T` *has* no statically-known size, e.g., a slice [`[T]`](https://doc.rust-lang.org/stable/std/primitive.slice.html "primitive slice") or a [trait object](https://doc.rust-lang.org/stable/book/ch17-02-trait-objects.html), then `size_of_val` can be used to get the dynamically-known size.

## [§](#examples)Examples

```rust
assert_eq!(4, size_of_val(&5i32));

let x: [u8; 13] = [0; 13];
let y: &[u8] = &x;
assert_eq!(13, size_of_val(y));
```