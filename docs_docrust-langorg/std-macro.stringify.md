---
title: stringify in std - Rust
url: https://doc.rust-lang.org/std/macro.stringify.html
source: crawler
fetched_at: 2026-05-06T21:32:34.993556913-03:00
rendered_js: false
word_count: 69
summary: This document describes the Rust stringify! macro, which converts a sequence of tokens into a static string literal.
tags:
    - rust-macro
    - string-conversion
    - token-processing
    - static-str
category: reference
---

## Macro stringify

1.38.0 · [Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#1280)

```rust
macro_rules! stringify {
    ($($t:tt)*) => { ... };
}
```

Expand description

Stringifies its arguments.

This macro will yield an expression of type `&'static str` which is the stringification of all the tokens passed to the macro. No restrictions are placed on the syntax of the macro invocation itself.

Note that the expanded results of the input tokens may change in the future. You should be careful if you rely on the output.

## [§](#examples)Examples

```rust
let one_plus_one = stringify!(1 + 1);
assert_eq!(one_plus_one, "1 + 1");
```