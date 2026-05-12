---
title: AsyncFnOnce in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnOnce.html
source: crawler
fetched_at: 2026-05-06T21:25:27.392271055-03:00
rendered_js: false
word_count: 69
summary: This document defines the AsyncFnOnce trait in Rust, which serves as an asynchronous version of FnOnce for functions and closures that return futures.
tags:
    - rust
    - async-programming
    - traits
    - experimental-api
    - functional-programming
category: reference
---

## Trait AsyncFnOnce

1.85.0 · [Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#44)

```rust
pub trait AsyncFnOnce<Args>
where
    Args: Tuple,{
    type CallOnceFuture: Future<Output = Self::Output>;
    type Output;

    // Required method
    extern "rust-call" fn async_call_once(
        self,
        args: Args,
    ) -> Self::CallOnceFuture;
}
```

Expand description

An async-aware version of the [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") trait.

All `async fn` and functions returning futures implement this trait.

[Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#48)

🔬This is a nightly-only experimental API. (`async_fn_traits`)

[Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#53)

🔬This is a nightly-only experimental API. (`async_fn_traits`)

Output type of the called closure’s future.

[Source](https://doc.rust-lang.org/stable/src/core/ops/async_function.rs.html#57)

🔬This is a nightly-only experimental API. (`async_fn_traits`)

Call the [`AsyncFnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.AsyncFnOnce.html "trait std::ops::AsyncFnOnce"), returning a future which may move out of the called closure.