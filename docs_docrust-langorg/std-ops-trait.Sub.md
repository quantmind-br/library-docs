---
title: Sub in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Sub.html#tymethod.sub
source: crawler
fetched_at: 2026-05-06T21:30:34.718837059-03:00
rendered_js: false
word_count: 126
summary: This document defines the Sub trait in Rust, which allows for custom implementation of the subtraction operator for user-defined types.
tags:
    - rust
    - trait
    - subtraction
    - operator-overloading
    - arithmetic-ops
category: reference
---

## Trait Sub

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#190)

```rust
pub trait Sub<Rhs = Self> {
    type Output;

    // Required method
    fn sub(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The subtraction operator `-`.

Note that `Rhs` is `Self` by default, but this is not mandatory. For example, [`std::time::SystemTime`](https://doc.rust-lang.org/std/time/struct.SystemTime.html) implements `Sub<Duration>`, which permits operations of the form `SystemTime = SystemTime - Duration`.

## [§](#examples)Examples

### [§](#subtractable-points)`Sub`tractable points

```rust
use std::ops::Sub;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Sub for Point {
    type Output = Self;

    fn sub(self, other: Self) -> Self::Output {
        Self {
            x: self.x - other.x,
            y: self.y - other.y,
        }
    }
}

assert_eq!(Point { x: 3, y: 3 } - Point { x: 2, y: 3 },
           Point { x: 1, y: 0 });
```

### [§](#implementing-sub-with-generics)Implementing `Sub` with generics

Here is an example of the same `Point` struct implementing the `Sub` trait using generics.

```rust
use std::ops::Sub;

#[derive(Debug, PartialEq)]
struct Point<T> {
    x: T,
    y: T,
}

// Notice that the implementation uses the associated type `Output`.
impl<T: Sub<Output = T>> Sub for Point<T> {
    type Output = Self;

    fn sub(self, other: Self) -> Self::Output {
        Point {
            x: self.x - other.x,
            y: self.y - other.y,
        }
    }
}

assert_eq!(Point { x: 2, y: 3 } - Point { x: 1, y: 0 },
           Point { x: 1, y: 3 });
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#193)

The resulting type after applying the `-` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#205)

Performs the `-` operation.

##### [§](#example)Example