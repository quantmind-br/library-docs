---
title: assert_matches in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.assert_matches.html
source: crawler
fetched_at: 2026-05-06T21:28:44.352018061-03:00
rendered_js: false
word_count: 160
summary: The assert_matches macro provides a mechanism to verify that an expression matches a specific pattern, offering detailed debug information upon failure compared to standard assertions.
tags:
    - rust
    - macros
    - testing
    - pattern-matching
    - debugging
    - experimental-api
category: api
---

## Macro assert\_matches

[Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#172)

```rust
pub macro assert_matches {
    ($left:expr, $(|)? $($pattern:pat_param)|+ $(if $guard:expr)? $(,)?) => { ... },
    ($left:expr, $(|)? $($pattern:pat_param)|+ $(if $guard:expr)?, $($arg:tt)+) => { ... },
}
```

🔬This is a nightly-only experimental API. (`assert_matches` [#82775](https://github.com/rust-lang/rust/issues/82775))

Expand description

Asserts that an expression matches the provided pattern.

This macro is generally preferable to `assert!(matches!(value, pattern))`, because it can print the debug representation of the actual value shape that did not meet expectations. In contrast, using [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert") will only print that expectations were not met, but not why.

The pattern syntax is exactly the same as found in a match arm and the `matches!` macro. The optional if guard can be used to add additional checks that must be true for the matched value, otherwise this macro will panic.

Assertions are always checked in both debug and release builds, and cannot be disabled. See `debug_assert_matches!` for assertions that are disabled in release builds by default.

On panic, this macro will print the value of the expression with its debug representation.

Like [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert"), this macro has a second form, where a custom panic message can be provided.

## [§](#examples)Examples

```rust
#![feature(assert_matches)]

use std::assert_matches;

let a = Some(345);
let b = Some(56);
assert_matches!(a, Some(_));
assert_matches!(b, Some(_));

assert_matches!(a, Some(345));
assert_matches!(a, Some(345) | None);

// assert_matches!(a, None); // panics
// assert_matches!(b, Some(345)); // panics
// assert_matches!(b, Some(345) | None); // panics

assert_matches!(a, Some(x) if x > 100);
// assert_matches!(a, Some(x) if x < 100); // panics
```