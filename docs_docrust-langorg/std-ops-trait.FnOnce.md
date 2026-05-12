---
title: FnOnce in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.FnOnce.html
source: crawler
fetched_at: 2026-05-06T21:24:40.743459489-03:00
rendered_js: false
word_count: 261
summary: This document defines the FnOnce trait in Rust, which represents functions that can be called at least once and may consume their captured environment.
tags:
    - rust
    - closures
    - traits
    - functional-programming
    - memory-management
    - fn-traits
category: reference
---

## Trait FnOnce

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143874 "Tracking issue for const_trait_impl")) · [Source](https://doc.rust-lang.org/src/core/ops/function.rs.html#242)

```rust
pub trait FnOnce<Args>
where
    Args: Tuple,{
    type Output;

    // Required method
    extern "rust-call" fn call_once(self, args: Args) -> Self::Output;
}
```

Expand description

The version of the call operator that takes a by-value receiver.

Instances of `FnOnce` can be called, but might not be callable multiple times. Because of this, if the only thing known about a type is that it implements `FnOnce`, it can only be called once.

`FnOnce` is implemented automatically by closures that might consume captured variables, as well as all types that implement [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html "trait std::ops::FnMut"), e.g., (safe) [function pointers](https://doc.rust-lang.org/std/primitive.fn.html "primitive fn") (since `FnOnce` is a supertrait of [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html "trait std::ops::FnMut")).

Since both [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn") and [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html "trait std::ops::FnMut") are subtraits of `FnOnce`, any instance of [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn") or [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html "trait std::ops::FnMut") can be used where a `FnOnce` is expected.

Use `FnOnce` as a bound when you want to accept a parameter of function-like type and only need to call it once. If you need to call the parameter repeatedly, use [`FnMut`](https://doc.rust-lang.org/std/ops/trait.FnMut.html "trait std::ops::FnMut") as a bound; if you also need it to not mutate state, use [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn").

See the [chapter on closures in *The Rust Programming Language*](https://doc.rust-lang.org/book/ch13-01-closures.html) for some more information on this topic.

Also of note is the special syntax for `Fn` traits (e.g. `Fn(usize, bool) -> usize`). Those interested in the technical details of this can refer to [the relevant section in the *Rustonomicon*](https://doc.rust-lang.org/nomicon/hrtb.html).

## [§](#examples)Examples

### [§](#using-a-fnonce-parameter)Using a `FnOnce` parameter

```rust
fn consume_with_relish<F>(func: F)
    where F: FnOnce() -> String
{
    // `func` consumes its captured variables, so it cannot be run more
    // than once.
    println!("Consumed: {}", func());

    println!("Delicious!");

    // Attempting to invoke `func()` again will throw a `use of moved
    // value` error for `func`.
}

let x = String::from("x");
let consume_and_return_x = move || x;
consume_with_relish(consume_and_return_x);

// `consume_and_return_x` can no longer be invoked at this point
```

1.12.0 · [Source](https://doc.rust-lang.org/src/core/ops/function.rs.html#246)

The returned type after the call operator is used.

[Source](https://doc.rust-lang.org/src/core/ops/function.rs.html#250)

🔬This is a nightly-only experimental API. (`fn_traits` [#29625](https://github.com/rust-lang/rust/issues/29625))

Performs the call operation.