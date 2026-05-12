---
title: Distribution in std::random - Rust
url: https://doc.rust-lang.org/std/random/trait.Distribution.html#tymethod.sample
source: crawler
fetched_at: 2026-05-06T21:30:04.777431685-03:00
rendered_js: false
word_count: 69
summary: This document defines the Distribution trait, an experimental interface used for generating random values of a specific type from a random source.
tags:
    - rust
    - random
    - trait
    - experimental-api
    - generics
    - sampling
category: reference
---

## Trait Distribution

[Source](https://doc.rust-lang.org/src/core/random.rs.html#19)

```rust
pub trait Distribution<T> {
    // Required method
    fn sample(&self, source: &mut (impl RandomSource + ?Sized)) -> T;
}
```

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Expand description

A trait representing a distribution of random values for a type.

[Source](https://doc.rust-lang.org/src/core/random.rs.html#21)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*