---
title: IntoFuture in std::future - Rust
url: https://doc.rust-lang.org/stable/std/future/trait.IntoFuture.html
source: crawler
fetched_at: 2026-05-06T21:25:41.62728261-03:00
rendered_js: false
word_count: 253
summary: This document describes the Rust IntoFuture trait, which provides a standard mechanism for converting types into futures and enables the .await syntax for custom asynchronous builder patterns.
tags:
    - rust
    - async-programming
    - futures
    - trait-implementation
    - async-builders
    - concurrency
category: reference
---

## Trait IntoFuture

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/core/future/into_future.rs.html#108)

```rust
pub trait IntoFuture {
    type Output;
    type IntoFuture: Future<Output = Self::Output>;

    // Required method
    fn into_future(self) -> Self::IntoFuture;
}
```

Expand description

Conversion into a `Future`.

By implementing `IntoFuture` for a type, you define how it will be converted to a future.

## [§](#await-desugaring)`.await` desugaring

The `.await` keyword desugars into a call to `IntoFuture::into_future` first before polling the future to completion. `IntoFuture` is implemented for all `T: Future` which means the `into_future` method will be available on all futures.

```rust
use std::future::IntoFuture;

let v = async { "meow" };
let mut fut = v.into_future();
assert_eq!("meow", fut.await);
```

## [§](#async-builders)Async builders

When implementing futures manually there will often be a choice between implementing `Future` or `IntoFuture` for a type. Implementing `Future` is a good choice in most cases. But implementing `IntoFuture` is most useful when implementing “async builder” types, which allow their values to be modified multiple times before being `.await`ed.

```rust
use std::future::{ready, Ready, IntoFuture};

/// Eventually multiply two numbers
pub struct Multiply {
    num: u16,
    factor: u16,
}

impl Multiply {
    /// Constructs a new instance of `Multiply`.
    pub fn new(num: u16, factor: u16) -> Self {
        Self { num, factor }
    }

    /// Set the number to multiply by the factor.
    pub fn number(mut self, num: u16) -> Self {
        self.num = num;
        self
    }

    /// Set the factor to multiply the number with.
    pub fn factor(mut self, factor: u16) -> Self {
        self.factor = factor;
        self
    }
}

impl IntoFuture for Multiply {
    type Output = u16;
    type IntoFuture = Ready<Self::Output>;

    fn into_future(self) -> Self::IntoFuture {
        ready(self.num * self.factor)
    }
}

// NOTE: Rust does not yet have an `async fn main` function, that functionality
// currently only exists in the ecosystem.
async fn run() {
    let num = Multiply::new(0, 0)  // initialize the builder to number: 0, factor: 0
        .number(2)                 // change the number to 2
        .factor(2)                 // change the factor to 2
        .await;                    // convert to future and .await

    assert_eq!(num, 4);
}
```

## [§](#usage-in-trait-bounds)Usage in trait bounds

Using `IntoFuture` in trait bounds allows a function to be generic over both `Future` and `IntoFuture`. This is convenient for users of the function, so when they are using it they don’t have to make an extra call to `IntoFuture::into_future` to obtain an instance of `Future`:

```rust
use std::future::IntoFuture;

/// Converts the output of a future to a string.
async fn fut_to_string<Fut>(fut: Fut) -> String
where
    Fut: IntoFuture,
    Fut::Output: std::fmt::Debug,
{
    format!("{:?}", fut.await)
}
```

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/core/future/into_future.rs.html#111)

The output that the future will produce on completion.

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/core/future/into_future.rs.html#115)

Which kind of future are we turning this into?

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/core/future/into_future.rs.html#134)

Creates a future from a value.

##### [§](#examples)Examples

Basic usage:

```rust
use std::future::IntoFuture;

let v = async { "meow" };
let mut fut = v.into_future();
assert_eq!("meow", fut.await);
```