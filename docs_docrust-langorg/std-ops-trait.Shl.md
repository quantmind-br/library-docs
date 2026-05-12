---
title: Shl in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Shl.html#tymethod.shl
source: crawler
fetched_at: 2026-05-06T21:30:27.250328288-03:00
rendered_js: false
word_count: 158
summary: This document defines the Shl trait in Rust, which allows for custom implementation of the bitwise left shift operator.
tags:
    - rust
    - bitwise-operators
    - trait-definition
    - operator-overloading
    - systems-programming
category: reference
---

## Trait Shl

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#461)

```rust
pub trait Shl<Rhs = Self> {
    type Output;

    // Required method
    fn shl(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The left shift operator `<<`. Note that because this trait is implemented for all integer types with multiple right-hand-side types, Rust’s type checker has special handling for `_ << _`, setting the result type for integer operations to the type of the left-hand-side operand. This means that though `a << b` and `a.shl(b)` are one and the same from an evaluation standpoint, they are different when it comes to type inference.

## [§](#examples)Examples

An implementation of `Shl` that lifts the `<<` operation on integers to a wrapper around `usize`.

```rust
use std::ops::Shl;

#[derive(PartialEq, Debug)]
struct Scalar(usize);

impl Shl<Scalar> for Scalar {
    type Output = Self;

    fn shl(self, Self(rhs): Self) -> Self::Output {
        let Self(lhs) = self;
        Self(lhs << rhs)
    }
}

assert_eq!(Scalar(4) << Scalar(2), Scalar(16));
```

An implementation of `Shl` that spins a vector leftward by a given amount.

```rust
use std::ops::Shl;

#[derive(PartialEq, Debug)]
struct SpinVector<T: Clone> {
    vec: Vec<T>,
}

impl<T: Clone> Shl<usize> for SpinVector<T> {
    type Output = Self;

    fn shl(self, rhs: usize) -> Self::Output {
        // Rotate the vector by `rhs` places.
        let (a, b) = self.vec.split_at(rhs);
        let mut spun_vector = vec![];
        spun_vector.extend_from_slice(b);
        spun_vector.extend_from_slice(a);
        Self { vec: spun_vector }
    }
}

assert_eq!(SpinVector { vec: vec![0, 1, 2, 3, 4] } << 2,
           SpinVector { vec: vec![2, 3, 4, 0, 1] });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#464)

The resulting type after applying the `<<` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#476)

Performs the `<<` operation.

##### [§](#examples-1)Examples

```rust
assert_eq!(5u8 << 1, 10);
assert_eq!(1u8 << 1, 2);
```