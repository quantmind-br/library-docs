---
title: Unpin in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.Unpin.html
source: crawler
fetched_at: 2026-05-06T21:24:03.575293093-03:00
rendered_js: false
word_count: 507
summary: The Unpin trait is a marker trait in Rust that signals when a type does not require pinning guarantees, allowing pinned pointers to access the underlying value without restricted APIs.
tags:
    - rust
    - pinning
    - memory-safety
    - auto-trait
    - concurrency
category: reference
---

## Trait Unpin

1.33.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#1015)

```rust
pub auto trait Unpin { }
```

Expand description

Types that do not require any pinning guarantees.

For information on what “pinning” is, see the [`pin` module](https://doc.rust-lang.org/std/pin/index.html "pin module") documentation.

Implementing the `Unpin` trait for `T` expresses the fact that `T` is pinning-agnostic: it shall not expose nor rely on any pinning guarantees. This, in turn, means that a `Pin`-wrapped pointer to such a type can feature a *fully unrestricted* API. In other words, if `T: Unpin`, a value of type `T` will *not* be bound by the invariants which pinning otherwise offers, even when “pinned” by a [`Pin<Ptr>`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin") pointing at it. When a value of type `T` is pointed at by a [`Pin<Ptr>`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin"), [`Pin`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin") will not restrict access to the pointee value like it normally would, thus allowing the user to do anything that they normally could with a non-[`Pin`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin")-wrapped `Ptr` to that value.

The idea of this trait is to alleviate the reduced ergonomics of APIs that require the use of [`Pin`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin") for soundness for some types, but which also want to be used by other types that don’t care about pinning. The prime example of such an API is [`Future::poll`](https://doc.rust-lang.org/std/future/trait.Future.html#tymethod.poll "Future poll"). There are many [`Future`](https://doc.rust-lang.org/std/future/trait.Future.html "Future") types that don’t care about pinning. These futures can implement `Unpin` and therefore get around the pinning related restrictions in the API, while still allowing the subset of [`Future`](https://doc.rust-lang.org/std/future/trait.Future.html "Future")s which *do* require pinning to be implemented soundly.

For more discussion on the consequences of [`Unpin`](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") within the wider scope of the pinning system, see the [section about `Unpin`](https://doc.rust-lang.org/std/pin/index.html#unpin "pin module docs about unpin") in the [`pin` module](https://doc.rust-lang.org/std/pin/index.html "pin module").

`Unpin` has no consequence at all for non-pinned data. In particular, [`mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html "mem replace") happily moves `!Unpin` data, which would be immovable when pinned ([`mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html "mem replace") works for any `&mut T`, not just when `T: Unpin`).

*However*, you cannot use [`mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html "mem replace") on `!Unpin` data which is *pinned* by being wrapped inside a [`Pin<Ptr>`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin") pointing at it. This is because you cannot (safely) use a [`Pin<Ptr>`](https://doc.rust-lang.org/std/pin/struct.Pin.html "Pin") to get a `&mut T` to its pointee value, which you would need to call [`mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html "mem replace"), and *that* is what makes this system work.

So this, for example, can only be done on types implementing `Unpin`:

```rust
use std::mem;
use std::pin::Pin;

let mut string = "this".to_string();
let mut pinned_string = Pin::new(&mut string);

// We need a mutable reference to call `mem::replace`.
// We can obtain such a reference by (implicitly) invoking `Pin::deref_mut`,
// but that is only possible because `String` implements `Unpin`.
mem::replace(&mut *pinned_string, "other".to_string());
```

This trait is automatically implemented for almost every type. The compiler is free to take the conservative stance of marking types as [`Unpin`](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") so long as all of the types that compose its fields are also [`Unpin`](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin"). This is because if a type implements [`Unpin`](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin"), then it is unsound for that type’s implementation to rely on pinning-related guarantees for soundness, *even* when viewed through a “pinning” pointer! It is the responsibility of the implementor of a type that relies upon pinning for soundness to ensure that type is *not* marked as [`Unpin`](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") by adding [`PhantomPinned`](https://doc.rust-lang.org/std/marker/struct.PhantomPinned.html "struct std::marker::PhantomPinned") field. For more details, see the [`pin` module](https://doc.rust-lang.org/std/pin/index.html "pin module") docs.