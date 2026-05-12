---
title: concat_bytes in std - Rust
url: https://doc.rust-lang.org/std/macro.concat_bytes.html
source: crawler
fetched_at: 2026-05-06T21:32:38.019530223-03:00
rendered_js: false
word_count: 69
summary: This document describes the Rust concat_bytes macro, which concatenates various byte-based literals into a single fixed-size byte slice at compile time.
tags:
    - rust
    - macro
    - byte-manipulation
    - compile-time
    - nightly-api
    - systems-programming
category: reference
---

## Macro concat\_bytes

[Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#1131)

```rust
macro_rules! concat_bytes {
    ($($e:literal),+ $(,)?) => { ... };
}
```

🔬This is a nightly-only experimental API. (`concat_bytes` [#87555](https://github.com/rust-lang/rust/issues/87555))

Expand description

Concatenates literals into a byte slice.

This macro takes any number of comma-separated literals, and concatenates them all into one, yielding an expression of type `&[u8; _]`, which represents all of the literals concatenated left-to-right. The literals passed can be any combination of:

- byte literals (`b'r'`)
- byte strings (`b"Rust"`)
- arrays of bytes/numbers (`[b'A', 66, b'C']`)

## [§](#examples)Examples

```rust
#![feature(concat_bytes)]

let s: &[u8; 6] = concat_bytes!(b'A', b"BC", [68, b'E', 70]);
assert_eq!(s, b"ABCDEF");
```