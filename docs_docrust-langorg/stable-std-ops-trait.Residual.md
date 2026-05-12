---
title: Residual in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/trait.Residual.html#associatedtype.TryType
source: crawler
fetched_at: 2026-05-06T21:26:15.569916969-03:00
rendered_js: false
word_count: 119
summary: This document defines the Residual trait, an experimental Rust API used to reconstruct a type implementing the Try trait from its output and residual components.
tags:
    - rust
    - try-trait
    - experimental-api
    - generic-types
    - trait-system
    - nightly-rust
category: reference
---

```rust
pub trait Residual<O>: Sized {
    type TryType: Try<Output = O, Residual = Self>;
}
```

🔬This is a nightly-only experimental API. (`try_trait_v2_residual` [#91285](https://github.com/rust-lang/rust/issues/91285))

Expand description

Allows retrieving the canonical type implementing [`Try`](https://doc.rust-lang.org/stable/std/ops/trait.Try.html "trait std::ops::Try") that has this type as its residual and allows it to hold an `O` as its output.

If you think of the `Try` trait as splitting a type into its [`Try::Output`](https://doc.rust-lang.org/stable/std/ops/trait.Try.html#associatedtype.Output "associated type std::ops::Try::Output") and [`Try::Residual`](https://doc.rust-lang.org/stable/std/ops/trait.Try.html#associatedtype.Residual "associated type std::ops::Try::Residual") components, this allows putting them back together.

For example, `Result<T, E>: Try<Output = T, Residual = Result<Infallible, E>>`, and in the other direction, `<Result<Infallible, E> as Residual<T>>::TryType = Result<T, E>`.

[Source](https://doc.rust-lang.org/stable/src/core/ops/try_trait.rs.html#368)

🔬This is a nightly-only experimental API. (`try_trait_v2_residual` [#91285](https://github.com/rust-lang/rust/issues/91285))

The “return” type of this meta-function.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*