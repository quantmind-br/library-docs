---
title: stringify in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.stringify.html
source: crawler
fetched_at: 2026-05-06T21:28:43.34633804-03:00
rendered_js: false
word_count: 69
summary: This macro converts a sequence of tokens into a static string literal at compile time.
tags:
    - rust
    - macros
    - string-manipulation
    - compile-time
    - tokens
category: reference
---

## Macro stringify

1.38.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#1280)

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