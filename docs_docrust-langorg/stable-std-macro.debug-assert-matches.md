---
title: debug_assert_matches in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.debug_assert_matches.html
source: crawler
fetched_at: 2026-05-06T21:28:45.165402628-03:00
rendered_js: false
word_count: 195
summary: This macro verifies that an expression matches a specific pattern during development, providing detailed diagnostic information upon failure while being excluded from optimized release builds.
tags:
    - rust
    - macro
    - debugging
    - pattern-matching
    - conditional-compilation
    - experimental-api
category: reference
---

## Macro debug\_assert\_matches

[Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#401)

```rust
pub macro debug_assert_matches($($arg:tt)*) {
    ...
}
```

🔬This is a nightly-only experimental API. (`assert_matches` [#82775](https://github.com/rust-lang/rust/issues/82775))

Expand description

Asserts that an expression matches the provided pattern.

This macro is generally preferable to `debug_assert!(matches!(value, pattern))`, because it can print the debug representation of the actual value shape that did not meet expectations. In contrast, using [`debug_assert!`](https://doc.rust-lang.org/stable/std/macro.debug_assert.html "macro std::debug_assert") will only print that expectations were not met, but not why.

The pattern syntax is exactly the same as found in a match arm and the `matches!` macro. The optional if guard can be used to add additional checks that must be true for the matched value, otherwise this macro will panic.

On panic, this macro will print the value of the expression with its debug representation.

Like [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert"), this macro has a second form, where a custom panic message can be provided.

Unlike [`assert_matches!`](https://doc.rust-lang.org/stable/std/macro.assert_matches.html "macro std::assert_matches"), `debug_assert_matches!` statements are only enabled in non optimized builds by default. An optimized build will not execute `debug_assert_matches!` statements unless `-C debug-assertions` is passed to the compiler. This makes `debug_assert_matches!` useful for checks that are too expensive to be present in a release build but may be helpful during development. The result of expanding `debug_assert_matches!` is always type checked.

## [§](#examples)Examples

```rust
#![feature(assert_matches)]

use std::debug_assert_matches;

let a = Some(345);
let b = Some(56);
debug_assert_matches!(a, Some(_));
debug_assert_matches!(b, Some(_));

debug_assert_matches!(a, Some(345));
debug_assert_matches!(a, Some(345) | None);

// debug_assert_matches!(a, None); // panics
// debug_assert_matches!(b, Some(345)); // panics
// debug_assert_matches!(b, Some(345) | None); // panics

debug_assert_matches!(a, Some(x) if x > 100);
// debug_assert_matches!(a, Some(x) if x < 100); // panics
```