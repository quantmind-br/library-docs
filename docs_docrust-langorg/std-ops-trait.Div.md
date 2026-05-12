---
title: Div in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Div.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:30:05.735581922-03:00
rendered_js: false
word_count: 1534
summary: The Div trait defines the behavior of the division operator in Rust, allowing types to implement custom division logic.
tags:
    - rust
    - traits
    - arithmetic-operators
    - operator-overloading
    - division
category: reference
---

## Trait Div

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#462)

```rust
pub trait Div<Rhs = Self> {
    type Output;

    // Required method
    fn div(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The division operator `/`.

Note that `Rhs` is `Self` by default, but this is not mandatory.

## [§](#examples)Examples

### [§](#dividable-rational-numbers)`Div`idable rational numbers

```rust
use std::ops::Div;

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

impl Div for Rational {
    // The division of rational numbers is a closed operation.
    type Output = Self;

    fn div(self, rhs: Self) -> Self::Output {
        if rhs.numerator == 0 {
            panic!("Cannot divide by zero-valued `Rational`!");
        }

        let numerator = self.numerator * rhs.denominator;
        let denominator = self.denominator * rhs.numerator;
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
assert_eq!(Rational::new(1, 2) / Rational::new(3, 4),
           Rational::new(2, 3));
```

### [§](#dividing-vectors-by-scalars-as-in-linear-algebra)Dividing vectors by scalars as in linear algebra

```rust
use std::ops::Div;

struct Scalar { value: f32 }

#[derive(Debug, PartialEq)]
struct Vector { value: Vec<f32> }

impl Div<Scalar> for Vector {
    type Output = Self;

    fn div(self, rhs: Scalar) -> Self::Output {
        Self { value: self.value.iter().map(|v| v / rhs.value).collect() }
    }
}

let scalar = Scalar { value: 2f32 };
let vector = Vector { value: vec![2f32, 4f32, 6f32] };
assert_eq!(vector / scalar, Vector { value: vec![1f32, 2f32, 3f32] });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#465)

The resulting type after applying the `/` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#477)

Performs the `/` operation.

##### [§](#example)Example

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i8)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i16)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-1)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-6)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i32)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-2)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-7)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i64)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-3)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-8)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-i128)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-4)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-9)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-isize)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-5)Panics

This operation will panic if `other == 0` or the division results in overflow.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-10)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u8)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-6)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-11)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u16)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-7)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-12)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u32)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-8)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-13)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u64)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-9)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-14)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-u128)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-10)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-15)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div-for-usize)

This operation rounds towards zero, truncating any fractional part of the exact result.

#### [§](#panics-11)Panics

This operation will panic if `other == 0`.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-16)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Ci8%3E)

#### [§](#examples-1)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2i8), Saturating(5i8) / Saturating(2));
assert_eq!(Saturating(i8::MAX), Saturating(i8::MAX) / Saturating(1));
assert_eq!(Saturating(i8::MIN), Saturating(i8::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0i8) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-17)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Ci16%3E)

#### [§](#examples-2)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2i16), Saturating(5i16) / Saturating(2));
assert_eq!(Saturating(i16::MAX), Saturating(i16::MAX) / Saturating(1));
assert_eq!(Saturating(i16::MIN), Saturating(i16::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0i16) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-18)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Ci32%3E)

#### [§](#examples-3)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2i32), Saturating(5i32) / Saturating(2));
assert_eq!(Saturating(i32::MAX), Saturating(i32::MAX) / Saturating(1));
assert_eq!(Saturating(i32::MIN), Saturating(i32::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0i32) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-19)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Ci64%3E)

#### [§](#examples-4)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2i64), Saturating(5i64) / Saturating(2));
assert_eq!(Saturating(i64::MAX), Saturating(i64::MAX) / Saturating(1));
assert_eq!(Saturating(i64::MIN), Saturating(i64::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0i64) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-20)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Ci128%3E)

#### [§](#examples-5)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2i128), Saturating(5i128) / Saturating(2));
assert_eq!(Saturating(i128::MAX), Saturating(i128::MAX) / Saturating(1));
assert_eq!(Saturating(i128::MIN), Saturating(i128::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0i128) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-21)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cisize%3E)

#### [§](#examples-6)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2isize), Saturating(5isize) / Saturating(2));
assert_eq!(Saturating(isize::MAX), Saturating(isize::MAX) / Saturating(1));
assert_eq!(Saturating(isize::MIN), Saturating(isize::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0isize) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-22)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cu8%3E)

#### [§](#examples-7)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2u8), Saturating(5u8) / Saturating(2));
assert_eq!(Saturating(u8::MAX), Saturating(u8::MAX) / Saturating(1));
assert_eq!(Saturating(u8::MIN), Saturating(u8::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0u8) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-23)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cu16%3E)

#### [§](#examples-8)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2u16), Saturating(5u16) / Saturating(2));
assert_eq!(Saturating(u16::MAX), Saturating(u16::MAX) / Saturating(1));
assert_eq!(Saturating(u16::MIN), Saturating(u16::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0u16) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-24)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cu32%3E)

#### [§](#examples-9)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2u32), Saturating(5u32) / Saturating(2));
assert_eq!(Saturating(u32::MAX), Saturating(u32::MAX) / Saturating(1));
assert_eq!(Saturating(u32::MIN), Saturating(u32::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0u32) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-25)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cu64%3E)

#### [§](#examples-10)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2u64), Saturating(5u64) / Saturating(2));
assert_eq!(Saturating(u64::MAX), Saturating(u64::MAX) / Saturating(1));
assert_eq!(Saturating(u64::MIN), Saturating(u64::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0u64) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-26)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cu128%3E)

#### [§](#examples-11)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2u128), Saturating(5u128) / Saturating(2));
assert_eq!(Saturating(u128::MAX), Saturating(u128::MAX) / Saturating(1));
assert_eq!(Saturating(u128::MIN), Saturating(u128::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0u128) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-27)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div-for-Saturating%3Cusize%3E)

#### [§](#examples-12)Examples

```rust
use std::num::Saturating;

assert_eq!(Saturating(2usize), Saturating(5usize) / Saturating(2));
assert_eq!(Saturating(usize::MAX), Saturating(usize::MAX) / Saturating(1));
assert_eq!(Saturating(usize::MIN), Saturating(usize::MIN) / Saturating(1));
```

[ⓘ](# "This example panics")

```rust
use std::num::Saturating;

let _ = Saturating(0usize) / Saturating(0);
```

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-28)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-29)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-30)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-31)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-32)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-33)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-34)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-35)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-36)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-37)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-38)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-39)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div-for-Wrapping%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-40)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-41)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-42)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-43)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-44)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f64%3E-for-%26f64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-45)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f64%3E-for-f64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-46)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f128%3E-for-%26f128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-47)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f128%3E-for-f128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-48)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-49)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-50)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-51)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i16%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-52)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i32%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-53)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i32%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-54)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i64%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-55)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i64%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-56)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i128%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-57)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26i128%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-58)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26isize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-59)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26isize%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-60)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-61)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-62)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-63)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u16%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-64)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u32%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-65)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u32%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-66)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u64%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-67)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u64%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-68)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u128%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-69)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26u128%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-70)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26usize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-71)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3C%26usize%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-72)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci8%3E%3E-for-%26Saturating%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-73)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci8%3E%3E-for-Saturating%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-74)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci16%3E%3E-for-%26Saturating%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-75)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci16%3E%3E-for-Saturating%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-76)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci32%3E%3E-for-%26Saturating%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-77)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci32%3E%3E-for-Saturating%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-78)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci64%3E%3E-for-%26Saturating%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-79)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci64%3E%3E-for-Saturating%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-80)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci128%3E%3E-for-%26Saturating%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-81)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Ci128%3E%3E-for-Saturating%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-82)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cisize%3E%3E-for-%26Saturating%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-83)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cisize%3E%3E-for-Saturating%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-84)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu8%3E%3E-for-%26Saturating%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-85)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu8%3E%3E-for-Saturating%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-86)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu16%3E%3E-for-%26Saturating%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-87)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu16%3E%3E-for-Saturating%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-88)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu32%3E%3E-for-%26Saturating%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-89)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu32%3E%3E-for-Saturating%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-90)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu64%3E%3E-for-%26Saturating%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-91)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu64%3E%3E-for-Saturating%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-92)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu128%3E%3E-for-%26Saturating%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-93)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cu128%3E%3E-for-Saturating%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-94)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cusize%3E%3E-for-%26Saturating%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-95)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3C%26Saturating%3Cusize%3E%3E-for-Saturating%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-96)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci8%3E%3E-for-%26Wrapping%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-97)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci8%3E%3E-for-Wrapping%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-98)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci16%3E%3E-for-%26Wrapping%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-99)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci16%3E%3E-for-Wrapping%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-100)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci32%3E%3E-for-%26Wrapping%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-101)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci32%3E%3E-for-Wrapping%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-102)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci64%3E%3E-for-%26Wrapping%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-103)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci64%3E%3E-for-Wrapping%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-104)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci128%3E%3E-for-%26Wrapping%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-105)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Ci128%3E%3E-for-Wrapping%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-106)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cisize%3E%3E-for-%26Wrapping%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-107)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cisize%3E%3E-for-Wrapping%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-108)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu8%3E%3E-for-%26Wrapping%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-109)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu8%3E%3E-for-Wrapping%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-110)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu16%3E%3E-for-%26Wrapping%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-111)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu16%3E%3E-for-Wrapping%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-112)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu32%3E%3E-for-%26Wrapping%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-113)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu32%3E%3E-for-Wrapping%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-114)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu64%3E%3E-for-%26Wrapping%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-115)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu64%3E%3E-for-Wrapping%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-116)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu128%3E%3E-for-%26Wrapping%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-117)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cu128%3E%3E-for-Wrapping%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-118)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cusize%3E%3E-for-%26Wrapping%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-119)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3C%26Wrapping%3Cusize%3E%3E-for-Wrapping%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-120)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-121)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-122)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf64%3E-for-%26f64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-123)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf128%3E-for-%26f128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-124)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci8%3E-for-%26i8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-125)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci16%3E-for-%26i16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-126)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci32%3E-for-%26i32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-127)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci64%3E-for-%26i64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-128)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Ci128%3E-for-%26i128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-129)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cisize%3E-for-%26isize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-130)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu8%3E-for-%26u8)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-131)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu16%3E-for-%26u16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-132)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu32%3E-for-%26u32)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-133)

1.3.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/time.rs.html#1247)[§](#impl-Div%3Cu32%3E-for-Duration)

[Source](https://doc.rust-lang.org/src/core/time.rs.html#1248)[§](#associatedtype.Output-134)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu64%3E-for-%26u64)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-135)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cu128%3E-for-%26u128)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-136)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#impl-Div%3Cusize%3E-for-%26usize)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#504-507)[§](#associatedtype.Output-137)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#impl-Div%3CNonZero%3Cu8%3E%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2412-2422)[§](#associatedtype.Output-138)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2424-2434)[§](#impl-Div%3CNonZero%3Cu16%3E%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2424-2434)[§](#associatedtype.Output-139)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2436-2446)[§](#impl-Div%3CNonZero%3Cu32%3E%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2436-2446)[§](#associatedtype.Output-140)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2448-2458)[§](#impl-Div%3CNonZero%3Cu64%3E%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2448-2458)[§](#associatedtype.Output-141)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2460-2470)[§](#impl-Div%3CNonZero%3Cu128%3E%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2460-2470)[§](#associatedtype.Output-142)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2499-2509)[§](#impl-Div%3CNonZero%3Cusize%3E%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#2499-2509)[§](#associatedtype.Output-143)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Ci8%3E%3E-for-%26Saturating%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-144)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Ci16%3E%3E-for-%26Saturating%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-145)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Ci32%3E%3E-for-%26Saturating%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-146)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Ci64%3E%3E-for-%26Saturating%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-147)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Ci128%3E%3E-for-%26Saturating%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-148)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cisize%3E%3E-for-%26Saturating%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-149)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cu8%3E%3E-for-%26Saturating%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-150)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cu16%3E%3E-for-%26Saturating%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-151)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cu32%3E%3E-for-%26Saturating%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-152)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cu64%3E%3E-for-%26Saturating%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-153)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cu128%3E%3E-for-%26Saturating%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-154)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#impl-Div%3CSaturating%3Cusize%3E%3E-for-%26Saturating%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/saturating.rs.html#551)[§](#associatedtype.Output-155)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Ci8%3E%3E-for-%26Wrapping%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-156)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Ci16%3E%3E-for-%26Wrapping%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-157)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Ci32%3E%3E-for-%26Wrapping%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-158)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Ci64%3E%3E-for-%26Wrapping%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-159)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Ci128%3E%3E-for-%26Wrapping%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-160)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cisize%3E%3E-for-%26Wrapping%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-161)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cu8%3E%3E-for-%26Wrapping%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-162)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cu16%3E%3E-for-%26Wrapping%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-163)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cu32%3E%3E-for-%26Wrapping%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-164)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cu64%3E%3E-for-%26Wrapping%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-165)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cu128%3E%3E-for-%26Wrapping%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-166)

1.14.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#impl-Div%3CWrapping%3Cusize%3E%3E-for-%26Wrapping%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566)[§](#associatedtype.Output-167)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#impl-Div%3C%26Simd%3CT,+N%3E%3E-for-%26Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#associatedtype.Output-168)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#impl-Div%3C%26Simd%3CT,+N%3E%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#associatedtype.Output-169)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#impl-Div%3CSimd%3CT,+N%3E%3E-for-%26Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops/deref.rs.html#77-119)[§](#associatedtype.Output-170)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#247-272)[§](#impl-Div-for-Simd%3Cf32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#247-272)[§](#associatedtype.Output-171)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#247-272)[§](#impl-Div-for-Simd%3Cf64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#247-272)[§](#associatedtype.Output-172)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Ci8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-173)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-174)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Ci32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-175)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Ci64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-176)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-177)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cu8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-178)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cu16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-179)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cu32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-180)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cu64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-181)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#impl-Div-for-Simd%3Cusize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/ops.rs.html#186-243)[§](#associatedtype.Output-182)