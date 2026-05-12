---
title: debug_assert in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.debug_assert.html
source: crawler
fetched_at: 2026-05-06T21:28:36.541792977-03:00
rendered_js: false
word_count: 174
summary: This document describes the debug_assert macro, which performs runtime assertions that are only active in non-optimized builds to aid in debugging without impacting production performance.
tags:
    - rust
    - macros
    - runtime-checks
    - debug-assertions
    - error-handling
    - development-tools
category: reference
---

## Macro debug\_assert

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#288)

```rust
macro_rules! debug_assert {
    ($($arg:tt)*) => { ... };
}
```

Expand description

Asserts that a boolean expression is `true` at runtime.

This will invoke the [`panic!`](https://doc.rust-lang.org/stable/core/macro.panic.html "macro core::panic") macro if the provided expression cannot be evaluated to `true` at runtime.

Like [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert"), this macro also has a second version, where a custom panic message can be provided.

## [§](#uses)Uses

Unlike [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert"), `debug_assert!` statements are only enabled in non optimized builds by default. An optimized build will not execute `debug_assert!` statements unless `-C debug-assertions` is passed to the compiler. This makes `debug_assert!` useful for checks that are too expensive to be present in a release build but may be helpful during development. The result of expanding `debug_assert!` is always type checked.

An unchecked assertion allows a program in an inconsistent state to keep running, which might have unexpected consequences but does not introduce unsafety as long as this only happens in safe code. The performance cost of assertions, however, is not measurable in general. Replacing [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert") with `debug_assert!` is thus only encouraged after thorough profiling, and more importantly, only in safe code!

## [§](#examples)Examples

```rust
// the panic message for these assertions is the stringified value of the
// expression given.
debug_assert!(true);

fn some_expensive_computation() -> bool {
    // Some expensive computation here
    true
}
debug_assert!(some_expensive_computation());

// assert with a custom message
let x = true;
debug_assert!(x, "x wasn't true!");

let a = 3; let b = 27;
debug_assert!(a + b == 30, "a = {}, b = {}", a, b);
```