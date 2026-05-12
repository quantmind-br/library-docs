---
title: debug_assert_ne in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.debug_assert_ne.html
source: crawler
fetched_at: 2026-05-06T21:28:37.117721173-03:00
rendered_js: false
word_count: 94
summary: This document describes the debug_assert_ne macro in Rust, which asserts inequality between two expressions exclusively during non-optimized builds.
tags:
    - rust
    - macro
    - debugging
    - assertions
    - development-tools
    - runtime-checks
category: reference
---

## Macro debug\_assert\_ne

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#348)

```rust
macro_rules! debug_assert_ne {
    ($($arg:tt)*) => { ... };
}
```

Expand description

Asserts that two expressions are not equal to each other.

On panic, this macro will print the values of the expressions with their debug representations.

Unlike [`assert_ne!`](https://doc.rust-lang.org/stable/std/macro.assert_ne.html "macro std::assert_ne"), `debug_assert_ne!` statements are only enabled in non optimized builds by default. An optimized build will not execute `debug_assert_ne!` statements unless `-C debug-assertions` is passed to the compiler. This makes `debug_assert_ne!` useful for checks that are too expensive to be present in a release build but may be helpful during development. The result of expanding `debug_assert_ne!` is always type checked.

## [§](#examples)Examples

```rust
let a = 3;
let b = 2;
debug_assert_ne!(a, b);
```