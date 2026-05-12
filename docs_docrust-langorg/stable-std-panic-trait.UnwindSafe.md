---
title: UnwindSafe in std::panic - Rust
url: https://doc.rust-lang.org/stable/std/panic/trait.UnwindSafe.html
source: crawler
fetched_at: 2026-05-06T21:26:23.713707941-03:00
rendered_js: false
word_count: 584
summary: The UnwindSafe trait is a marker used in Rust to identify types that can safely cross a catch_unwind boundary without exposing logically broken invariants after a panic.
tags:
    - rust
    - panic-safety
    - marker-trait
    - error-handling
    - unwind-safety
    - concurrency
category: reference
---

## Trait UnwindSafe

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/core/panic/unwind_safe.rs.html#90)

```rust
pub auto trait UnwindSafe { }
```

Expand description

A marker trait which represents “panic safe” types in Rust.

This trait is implemented by default for many types and behaves similarly in terms of inference of implementation to the [`Send`](https://doc.rust-lang.org/stable/std/marker/trait.Send.html "trait std::marker::Send") and [`Sync`](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync") traits. The purpose of this trait is to encode what types are safe to cross a [`catch_unwind`](https://doc.rust-lang.org/stable/std/panic/fn.catch_unwind.html) boundary with no fear of unwind safety.

### [§](#what-is-unwind-safety)What is unwind safety?

In Rust a function can “return” early if it either panics or calls a function which transitively panics. This sort of control flow is not always anticipated, and has the possibility of causing subtle bugs through a combination of two critical components:

1. A data structure is in a temporarily invalid state when the thread panics.
2. This broken invariant is then later observed.

Typically in Rust, it is difficult to perform step (2) because catching a panic involves either spawning a thread (which in turn makes it difficult to later witness broken invariants) or using the `catch_unwind` function in this module. Additionally, even if an invariant is witnessed, it typically isn’t a problem in Rust because there are no uninitialized values (like in C or C++).

It is possible, however, for **logical** invariants to be broken in Rust, which can end up causing behavioral bugs. Another key aspect of unwind safety in Rust is that, in the absence of `unsafe` code, a panic cannot lead to memory unsafety.

That was a bit of a whirlwind tour of unwind safety, but for more information about unwind safety and how it applies to Rust, see an [associated RFC](https://github.com/rust-lang/rfcs/blob/master/text/1236-stabilize-catch-panic.md).

### [§](#what-is-unwindsafe)What is `UnwindSafe`?

Now that we’ve got an idea of what unwind safety is in Rust, it’s also important to understand what this trait represents. As mentioned above, one way to witness broken invariants is through the `catch_unwind` function in this module as it allows catching a panic and then re-using the environment of the closure.

Simply put, a type `T` implements `UnwindSafe` if it cannot easily allow witnessing a broken invariant through the use of `catch_unwind` (catching a panic). This trait is an auto trait, so it is automatically implemented for many types, and it is also structurally composed (e.g., a struct is unwind safe if all of its components are unwind safe).

Note, however, that this is not an unsafe trait, so there is not a succinct contract that this trait is providing. Instead it is intended as more of a “speed bump” to alert users of `catch_unwind` that broken invariants may be witnessed and may need to be accounted for.

### [§](#who-implements-unwindsafe)Who implements `UnwindSafe`?

Types such as `&mut T` and `&RefCell<T>` are examples which are **not** unwind safe. The general idea is that any mutable state which can be shared across `catch_unwind` is not unwind safe by default. This is because it is very easy to witness a broken invariant outside of `catch_unwind` as the data is simply accessed as usual.

Types like `&Mutex<T>`, however, are unwind safe because they implement poisoning by default. They still allow witnessing a broken invariant, but they already provide their own “speed bumps” to do so.

### [§](#when-should-unwindsafe-be-used)When should `UnwindSafe` be used?

It is not intended that most types or functions need to worry about this trait. It is only used as a bound on the `catch_unwind` function and as mentioned above, the lack of `unsafe` means it is mostly an advisory. The [`AssertUnwindSafe`](https://doc.rust-lang.org/stable/std/panic/struct.AssertUnwindSafe.html "struct std::panic::AssertUnwindSafe") wrapper struct can be used to force this trait to be implemented for any closed over variables passed to `catch_unwind`.