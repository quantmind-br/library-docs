---
title: BitXor in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.BitXor.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:29:58.926235296-03:00
rendered_js: false
word_count: 98
summary: This document defines the BitXor trait in Rust, which allows for overloading the bitwise XOR operator for custom types.
tags:
    - rust
    - bitwise-xor
    - operator-overloading
    - trait-definition
    - std-ops
category: reference
---

## Trait BitXor

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#358)

```rust
pub trait BitXor<Rhs = Self> {
    type Output;

    // Required method
    fn bitxor(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The bitwise XOR operator `^`.

Note that `Rhs` is `Self` by default, but this is not mandatory.

## [§](#examples)Examples

An implementation of `BitXor` that lifts `^` to a wrapper around `bool`.

```rust
use std::ops::BitXor;

#[derive(Debug, PartialEq)]
struct Scalar(bool);

impl BitXor for Scalar {
    type Output = Self;

    // rhs is the "right-hand side" of the expression `a ^ b`
    fn bitxor(self, rhs: Self) -> Self::Output {
        Self(self.0 ^ rhs.0)
    }
}

assert_eq!(Scalar(true) ^ Scalar(true), Scalar(false));
assert_eq!(Scalar(true) ^ Scalar(false), Scalar(true));
assert_eq!(Scalar(false) ^ Scalar(true), Scalar(true));
assert_eq!(Scalar(false) ^ Scalar(false), Scalar(false));
```

An implementation of `BitXor` trait for a wrapper around `Vec<bool>`.

```rust
use std::ops::BitXor;

#[derive(Debug, PartialEq)]
struct BooleanVector(Vec<bool>);

impl BitXor for BooleanVector {
    type Output = Self;

    fn bitxor(self, Self(rhs): Self) -> Self::Output {
        let Self(lhs) = self;
        assert_eq!(lhs.len(), rhs.len());
        Self(
            lhs.iter()
                .zip(rhs.iter())
                .map(|(x, y)| *x ^ *y)
                .collect()
        )
    }
}

let bv1 = BooleanVector(vec![true, true, false, false]);
let bv2 = BooleanVector(vec![true, false, true, false]);
let expected = BooleanVector(vec![false, true, true, false]);
assert_eq!(bv1 ^ bv2, expected);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#361)

The resulting type after applying the `^` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#375)

Performs the `^` operation.

##### [§](#examples-1)Examples

```rust
assert_eq!(true ^ false, true);
assert_eq!(true ^ true, false);
assert_eq!(5u8 ^ 1u8, 4);
assert_eq!(5u8 ^ 2u8, 7);
```