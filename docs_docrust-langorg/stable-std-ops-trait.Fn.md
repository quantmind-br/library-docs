---
title: Fn in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/trait.Fn.html
source: crawler
fetched_at: 2026-05-06T21:25:25.272997456-03:00
rendered_js: false
word_count: 229
summary: This document defines the Fn trait in Rust, which represents callable types that can be invoked repeatedly without mutating their internal state.
tags:
    - rust
    - closures
    - traits
    - functional-programming
    - fn-trait
    - language-reference
category: reference
---

## Trait Fn

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143874 "Tracking issue for const_trait_impl")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/function.rs.html#76)

```rust
pub trait Fn<Args>: FnMut<Args>
where
    Args: Tuple,{
    // Required method
    extern "rust-call" fn call(&self, args: Args) -> Self::Output;
}
```

Expand description

The version of the call operator that takes an immutable receiver.

Instances of `Fn` can be called repeatedly without mutating state.

*This trait (`Fn`) is not to be confused with [function pointers](https://doc.rust-lang.org/stable/std/primitive.fn.html "primitive fn") (`fn`).*

`Fn` is implemented automatically by closures which only take immutable references to captured variables or don’t capture anything at all, as well as (safe) [function pointers](https://doc.rust-lang.org/stable/std/primitive.fn.html "primitive fn") (with some caveats, see their documentation for more details). Additionally, for any type `F` that implements `Fn`, `&F` implements `Fn`, too.

Since both [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut") and [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") are supertraits of `Fn`, any instance of `Fn` can be used as a parameter where a [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut") or [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") is expected.

Use `Fn` as a bound when you want to accept a parameter of function-like type and need to call it repeatedly and without mutating state (e.g., when calling it concurrently). If you do not need such strict requirements, use [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut") or [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") as bounds.

See the [chapter on closures in *The Rust Programming Language*](https://doc.rust-lang.org/stable/book/ch13-01-closures.html) for some more information on this topic.

Also of note is the special syntax for `Fn` traits (e.g. `Fn(usize, bool) -> usize`). Those interested in the technical details of this can refer to [the relevant section in the *Rustonomicon*](https://doc.rust-lang.org/stable/nomicon/hrtb.html).

## [§](#examples)Examples

### [§](#calling-a-closure)Calling a closure

```rust
let square = |x| x * x;
assert_eq!(square(5), 25);
```

### [§](#using-a-fn-parameter)Using a `Fn` parameter

```rust
fn call_with_one<F>(func: F) -> usize
    where F: Fn(usize) -> usize {
    func(1)
}

let double = |x| x * 2;
assert_eq!(call_with_one(double), 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/ops/function.rs.html#79)

🔬This is a nightly-only experimental API. (`fn_traits` [#29625](https://github.com/rust-lang/rust/issues/29625))

Performs the call operation.