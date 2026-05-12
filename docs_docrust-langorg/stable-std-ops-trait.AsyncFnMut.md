---
title: AsyncFnMut in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnMut.html
source: crawler
fetched_at: 2026-05-06T21:25:26.771146312-03:00
rendered_js: false
word_count: 77
summary: This document defines the AsyncFnMut trait, an experimental Rust trait designed for asynchronous closures that can be called multiple times while borrowing captured variables.
tags:
    - rust
    - async-rust
    - traits
    - experimental-api
    - functional-programming
category: reference
---

## Trait AsyncFnMut

1.85.0 · [Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#24)

```rust
pub trait AsyncFnMut<Args>: AsyncFnOnce<Args>
where
    Args: Tuple,{
    type CallRefFuture<'a>: Future<Output = Self::Output>
       where Self: 'a;

    // Required method
    extern "rust-call" fn async_call_mut(
        &mut self,
        args: Args,
    ) -> Self::CallRefFuture<'_>;
}
```

Expand description

An async-aware version of the [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut") trait.

All `async fn` and functions returning futures implement this trait.

[Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#28)

🔬This is a nightly-only experimental API. (`async_fn_traits`)

[Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#34)

🔬This is a nightly-only experimental API. (`async_fn_traits`)

Call the [`AsyncFnMut`](https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnMut.html "trait std::ops::AsyncFnMut"), returning a future which may borrow from the called closure.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*