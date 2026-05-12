---
title: Add in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/trait.Add.html#tymethod.add
source: crawler
fetched_at: 2026-05-06T21:33:35.272242125-03:00
rendered_js: false
word_count: 128
summary: This document defines the Add trait in Rust, which allows types to overload the addition operator (+) to perform custom arithmetic or combining operations.
tags:
    - rust-language
    - trait-system
    - operator-overloading
    - arithmetic-operations
    - type-system
    - generic-programming
category: reference
---

## Trait Add

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#77)

```rust
pub trait Add<Rhs = Self> {
    type Output;

    // Required method
    fn add(self, rhs: Rhs) -> Self::Output;
}
```

Expand description

The addition operator `+`.

Note that `Rhs` is `Self` by default, but this is not mandatory. For example, [`std::time::SystemTime`](https://doc.rust-lang.org/stable/std/time/struct.SystemTime.html) implements `Add<Duration>`, which permits operations of the form `SystemTime = SystemTime + Duration`.

## [§](#examples)Examples

### [§](#addable-points)`Add`able points

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

assert_eq!(Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
           Point { x: 3, y: 3 });
```

### [§](#implementing-add-with-generics)Implementing `Add` with generics

Here is an example of the same `Point` struct implementing the `Add` trait using generics.

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point<T> {
    x: T,
    y: T,
}

// Notice that the implementation uses the associated type `Output`.
impl<T: Add<Output = T>> Add for Point<T> {
    type Output = Self;

    fn add(self, other: Self) -> Self::Output {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

assert_eq!(Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
           Point { x: 3, y: 3 });
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#80)

The resulting type after applying the `+` operator.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#92)

Performs the `+` operation.

##### [§](#example)Example