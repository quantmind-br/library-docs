---
title: FnMut in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.FnMut.html
source: crawler
fetched_at: 2026-05-06T21:22:22.021295271-03:00
rendered_js: false
word_count: 237
summary: This document defines the FnMut trait in Rust, which represents callable types that can be invoked repeatedly and are permitted to mutate their captured state.
tags:
    - rust
    - closures
    - traits
    - functional-programming
    - fnmut
    - memory-safety
category: reference
---

## Trait FnMut

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143874 "Tracking issue for const_trait_impl")) · [Source](https://doc.rust-lang.org/src/core/ops/function.rs.html#163)

```rust
pub trait FnMut<Args>: FnOnce<Args>
where
    Args: Tuple,{
    // Required method
    extern "rust-call" fn call_mut(
        &mut self,
        args: Args,
    ) -> Self::Output;
}
```

Expand description

The version of the call operator that takes a mutable receiver.

Instances of `FnMut` can be called repeatedly and may mutate state.

`FnMut` is implemented automatically by closures which take mutable references to captured variables, as well as all types that implement [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn"), e.g., (safe) [function pointers](https://doc.rust-lang.org/std/primitive.fn.html "primitive fn") (since `FnMut` is a supertrait of [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn")). Additionally, for any type `F` that implements `FnMut`, `&mut F` implements `FnMut`, too.

Since [`FnOnce`](https://doc.rust-lang.org/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") is a supertrait of `FnMut`, any instance of `FnMut` can be used where a [`FnOnce`](https://doc.rust-lang.org/std/ops/trait.FnOnce.html "trait std::ops::FnOnce") is expected, and since [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn") is a subtrait of `FnMut`, any instance of [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn") can be used where `FnMut` is expected.

Use `FnMut` as a bound when you want to accept a parameter of function-like type and need to call it repeatedly, while allowing it to mutate state. If you don’t want the parameter to mutate state, use [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html "trait std::ops::Fn") as a bound; if you don’t need to call it repeatedly, use [`FnOnce`](https://doc.rust-lang.org/std/ops/trait.FnOnce.html "trait std::ops::FnOnce").

See the [chapter on closures in *The Rust Programming Language*](https://doc.rust-lang.org/book/ch13-01-closures.html) for some more information on this topic.

Also of note is the special syntax for `Fn` traits (e.g. `Fn(usize, bool) -> usize`). Those interested in the technical details of this can refer to [the relevant section in the *Rustonomicon*](https://doc.rust-lang.org/nomicon/hrtb.html).

## [§](#examples)Examples

### [§](#calling-a-mutably-capturing-closure)Calling a mutably capturing closure

```rust
let mut x = 5;
{
    let mut square_x = || x *= x;
    square_x();
}
assert_eq!(x, 25);
```

### [§](#using-a-fnmut-parameter)Using a `FnMut` parameter

```rust
fn do_twice<F>(mut func: F)
    where F: FnMut()
{
    func();
    func();
}

let mut x: usize = 1;
{
    let add_two_to_x = || x += 2;
    do_twice(add_two_to_x);
}

assert_eq!(x, 5);
```

[Source](https://doc.rust-lang.org/src/core/ops/function.rs.html#166)

🔬This is a nightly-only experimental API. (`fn_traits` [#29625](https://github.com/rust-lang/rust/issues/29625))

Performs the call operation.