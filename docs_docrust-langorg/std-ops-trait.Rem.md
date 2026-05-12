---
title: Rem in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Rem.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:30:24.516503439-03:00
rendered_js: false
word_count: 85
summary: This document defines the Rem trait in Rust, which allows for the customization of the remainder operator (%) for user-defined types.
tags:
    - rust
    - trait
    - operator-overloading
    - arithmetic
    - remainder-operator
category: reference
---

## Trait Rem

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#571)

```rust
pub trait Rem<Rhs = Self> {
    type Output;

    // Required method
    fn rem(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The remainder operator `%`.

Note that `Rhs` is `Self` by default, but this is not mandatory.

## [§](#examples)Examples

This example implements `Rem` on a `SplitSlice` object. After `Rem` is implemented, one can use the `%` operator to find out what the remaining elements of the slice would be after splitting it into equal slices of a given length.

```rust
use std::ops::Rem;

#[derive(PartialEq, Debug)]
struct SplitSlice<'a, T> {
    slice: &'a [T],
}

impl<'a, T> Rem<usize> for SplitSlice<'a, T> {
    type Output = Self;

    fn rem(self, modulus: usize) -> Self::Output {
        let len = self.slice.len();
        let rem = len % modulus;
        let start = len - rem;
        Self {slice: &self.slice[start..]}
    }
}

// If we were to divide &[0, 1, 2, 3, 4, 5, 6, 7] into slices of size 3,
// the remainder would be &[6, 7].
assert_eq!(SplitSlice { slice: &[0, 1, 2, 3, 4, 5, 6, 7] } % 3,
           SplitSlice { slice: &[6, 7] });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#574)

The resulting type after applying the `%` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#586)

Performs the `%` operation.

##### [§](#example)Example