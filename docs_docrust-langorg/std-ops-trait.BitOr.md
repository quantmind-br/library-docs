---
title: BitOr in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.BitOr.html#tymethod.bitor
source: crawler
fetched_at: 2026-05-06T21:29:55.822145819-03:00
rendered_js: false
word_count: 94
summary: The BitOr trait provides the mechanism for overloading the bitwise OR operator for custom types in Rust.
tags:
    - rust
    - bitwise-operations
    - trait-definition
    - operator-overloading
category: reference
---

## Trait BitOr

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#254)

```rust
pub trait BitOr<Rhs = Self> {
    type Output;

    // Required method
    fn bitor(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The bitwise OR operator `|`.

Note that `Rhs` is `Self` by default, but this is not mandatory.

## [§](#examples)Examples

An implementation of `BitOr` for a wrapper around `bool`.

```rust
use std::ops::BitOr;

#[derive(Debug, PartialEq)]
struct Scalar(bool);

impl BitOr for Scalar {
    type Output = Self;

    // rhs is the "right-hand side" of the expression `a | b`
    fn bitor(self, rhs: Self) -> Self::Output {
        Self(self.0 | rhs.0)
    }
}

assert_eq!(Scalar(true) | Scalar(true), Scalar(true));
assert_eq!(Scalar(true) | Scalar(false), Scalar(true));
assert_eq!(Scalar(false) | Scalar(true), Scalar(true));
assert_eq!(Scalar(false) | Scalar(false), Scalar(false));
```

An implementation of `BitOr` for a wrapper around `Vec<bool>`.

```rust
use std::ops::BitOr;

#[derive(Debug, PartialEq)]
struct BooleanVector(Vec<bool>);

impl BitOr for BooleanVector {
    type Output = Self;

    fn bitor(self, Self(rhs): Self) -> Self::Output {
        let Self(lhs) = self;
        assert_eq!(lhs.len(), rhs.len());
        Self(
            lhs.iter()
                .zip(rhs.iter())
                .map(|(x, y)| *x | *y)
                .collect()
        )
    }
}

let bv1 = BooleanVector(vec![true, true, false, false]);
let bv2 = BooleanVector(vec![true, false, true, false]);
let expected = BooleanVector(vec![true, true, true, false]);
assert_eq!(bv1 | bv2, expected);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#257)

The resulting type after applying the `|` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/bit.rs.html#271)

Performs the `|` operation.

##### [§](#examples-1)Examples

```rust
assert_eq!(true | false, true);
assert_eq!(false | false, false);
assert_eq!(5u8 | 1u8, 5);
assert_eq!(5u8 | 2u8, 7);
```