---
title: Shr in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Shr.html#tymethod.shr
source: crawler
fetched_at: 2026-05-06T21:30:29.020139071-03:00
rendered_js: false
word_count: 158
summary: This document defines the Shr trait in Rust, which allows for the implementation of custom right shift operations using the >> operator.
tags:
    - rust-language
    - trait-implementation
    - bitwise-operations
    - operator-overloading
    - standard-library
category: reference
---

## Trait Shr

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#583)

```rust
pub trait Shr<Rhs = Self> {
    type Output;

    // Required method
    fn shr(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The right shift operator `>>`. Note that because this trait is implemented for all integer types with multiple right-hand-side types, Rust’s type checker has special handling for `_ >> _`, setting the result type for integer operations to the type of the left-hand-side operand. This means that though `a >> b` and `a.shr(b)` are one and the same from an evaluation standpoint, they are different when it comes to type inference.

## [§](#examples)Examples

An implementation of `Shr` that lifts the `>>` operation on integers to a wrapper around `usize`.

```rust
use std::ops::Shr;

#[derive(PartialEq, Debug)]
struct Scalar(usize);

impl Shr<Scalar> for Scalar {
    type Output = Self;

    fn shr(self, Self(rhs): Self) -> Self::Output {
        let Self(lhs) = self;
        Self(lhs >> rhs)
    }
}

assert_eq!(Scalar(16) >> Scalar(2), Scalar(4));
```

An implementation of `Shr` that spins a vector rightward by a given amount.

```rust
use std::ops::Shr;

#[derive(PartialEq, Debug)]
struct SpinVector<T: Clone> {
    vec: Vec<T>,
}

impl<T: Clone> Shr<usize> for SpinVector<T> {
    type Output = Self;

    fn shr(self, rhs: usize) -> Self::Output {
        // Rotate the vector by `rhs` places.
        let (a, b) = self.vec.split_at(self.vec.len() - rhs);
        let mut spun_vector = vec![];
        spun_vector.extend_from_slice(b);
        spun_vector.extend_from_slice(a);
        Self { vec: spun_vector }
    }
}

assert_eq!(SpinVector { vec: vec![0, 1, 2, 3, 4] } >> 2,
           SpinVector { vec: vec![3, 4, 0, 1, 2] });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#586)

The resulting type after applying the `>>` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#598)

Performs the `>>` operation.

##### [§](#examples-1)Examples

```rust
assert_eq!(5u8 >> 1, 2);
assert_eq!(2u8 >> 1, 1);
```