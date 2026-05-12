---
title: Not in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Not.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:30:19.32691337-03:00
rendered_js: false
word_count: 52
summary: This document defines the Not trait in Rust, which allows for the implementation of the unary logical negation operator '!' on custom types.
tags:
    - rust-language
    - trait-definition
    - operator-overloading
    - logical-negation
    - core-ops
category: reference
---

## Trait Not

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#35)

```rust
pub trait Not {
    type Output;

    // Required method
    fn not(self) -> Self::Output;
}
```

Expand description

The unary logical negation operator `!`.

## [§](#examples)Examples

An implementation of `Not` for `Answer`, which enables the use of `!` to invert its value.

```rust
use std::ops::Not;

#[derive(Debug, PartialEq)]
enum Answer {
    Yes,
    No,
}

impl Not for Answer {
    type Output = Self;

    fn not(self) -> Self::Output {
        match self {
            Answer::Yes => Answer::No,
            Answer::No => Answer::Yes
        }
    }
}

assert_eq!(!Answer::Yes, Answer::No);
assert_eq!(!Answer::No, Answer::Yes);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#38)

The resulting type after applying the `!` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#52)

Performs the unary `!` operation.

##### [§](#examples-1)Examples

```rust
assert_eq!(!true, false);
assert_eq!(!false, true);
assert_eq!(!1u8, 254);
assert_eq!(!0u8, 255);
```