---
title: Mul in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Mul.html#tymethod.mul
source: crawler
fetched_at: 2026-05-06T21:30:17.551875801-03:00
rendered_js: false
word_count: 176
summary: Defines the Mul trait in Rust, which allows custom types to implement the behavior of the multiplication operator.
tags:
    - rust
    - operator-overloading
    - traits
    - multiplication
    - arithmetic-ops
category: reference
---

## Trait Mul

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#324)

```rust
pub trait Mul<Rhs = Self> {
    type Output;

    // Required method
    fn mul(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The multiplication operator `*`.

Note that `Rhs` is `Self` by default, but this is not mandatory.

## [§](#examples)Examples

### [§](#multipliable-rational-numbers)`Mul`tipliable rational numbers

```rust
use std::ops::Mul;

// By the fundamental theorem of arithmetic, rational numbers in lowest
// terms are unique. So, by keeping `Rational`s in reduced form, we can
// derive `Eq` and `PartialEq`.
#[derive(Debug, Eq, PartialEq)]
struct Rational {
    numerator: usize,
    denominator: usize,
}

impl Rational {
    fn new(numerator: usize, denominator: usize) -> Self {
        if denominator == 0 {
            panic!("Zero is an invalid denominator!");
        }

        // Reduce to lowest terms by dividing by the greatest common
        // divisor.
        let gcd = gcd(numerator, denominator);
        Self {
            numerator: numerator / gcd,
            denominator: denominator / gcd,
        }
    }
}

impl Mul for Rational {
    // The multiplication of rational numbers is a closed operation.
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        let numerator = self.numerator * rhs.numerator;
        let denominator = self.denominator * rhs.denominator;
        Self::new(numerator, denominator)
    }
}

// Euclid's two-thousand-year-old algorithm for finding the greatest common
// divisor.
fn gcd(x: usize, y: usize) -> usize {
    let mut x = x;
    let mut y = y;
    while y != 0 {
        let t = y;
        y = x % y;
        x = t;
    }
    x
}

assert_eq!(Rational::new(1, 2), Rational::new(2, 4));
assert_eq!(Rational::new(2, 3) * Rational::new(3, 4),
           Rational::new(1, 2));
```

### [§](#multiplying-vectors-by-scalars-as-in-linear-algebra)Multiplying vectors by scalars as in linear algebra

```rust
use std::ops::Mul;

struct Scalar { value: usize }

#[derive(Debug, PartialEq)]
struct Vector { value: Vec<usize> }

impl Mul<Scalar> for Vector {
    type Output = Self;

    fn mul(self, rhs: Scalar) -> Self::Output {
        Self { value: self.value.iter().map(|v| v * rhs.value).collect() }
    }
}

let vector = Vector { value: vec![2, 4, 6] };
let scalar = Scalar { value: 3 };
assert_eq!(vector * scalar, Vector { value: vec![6, 12, 18] });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#327)

The resulting type after applying the `*` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#339)

Performs the `*` operation.

##### [§](#example)Example