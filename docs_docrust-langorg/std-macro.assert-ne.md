---
title: assert_ne in std - Rust
url: https://doc.rust-lang.org/std/macro.assert_ne.html
source: crawler
fetched_at: 2026-05-06T21:32:29.202382115-03:00
rendered_js: false
word_count: 77
summary: This document describes the assert_ne macro in Rust, which is used to verify that two expressions are not equal and triggers a panic with an optional message if they are.
tags:
    - rust
    - macro
    - unit-testing
    - assertion
    - equality-check
category: reference
---

## Macro assert\_ne

1.0.0 · [Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#98)

```rust
macro_rules! assert_ne {
    ($left:expr, $right:expr $(,)?) => { ... };
    ($left:expr, $right:expr, $($arg:tt)+) => { ... };
}
```

Expand description

Asserts that two expressions are not equal to each other (using [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq")).

Assertions are always checked in both debug and release builds, and cannot be disabled. See [`debug_assert_ne!`](https://doc.rust-lang.org/std/macro.debug_assert_ne.html "macro std::debug_assert_ne") for assertions that are disabled in release builds by default.

On panic, this macro will print the values of the expressions with their debug representations.

Like [`assert!`](https://doc.rust-lang.org/std/macro.assert.html "macro std::assert"), this macro has a second form, where a custom panic message can be provided.

## [§](#examples)Examples

```rust
let a = 3;
let b = 2;
assert_ne!(a, b);

assert_ne!(a, b, "we are testing that the values are not equal");
```