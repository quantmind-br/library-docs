---
title: PeekMut in std::vec - Rust
url: https://doc.rust-lang.org/std/vec/struct.PeekMut.html
source: crawler
fetched_at: 2026-05-06T21:36:14.648565664-03:00
rendered_js: false
word_count: 170
summary: This document describes the PeekMut struct in Rust, which provides a mutable reference to the last element of a vector, and details its methods and trait implementations.
tags:
    - rust
    - api-reference
    - vec
    - mutable-reference
    - nightly-api
    - memory-management
category: api
---

```rust
pub struct PeekMut<'a, T, A = Global>
where
    A: Allocator,{ /* private fields */ }
```

🔬This is a nightly-only experimental API. (`vec_peek_mut` [#122742](https://github.com/rust-lang/rust/issues/122742))

Expand description

Structure wrapping a mutable reference to the last item in a `Vec`.

This `struct` is created by the [`peek_mut`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.peek_mut "method std::vec::Vec::peek_mut") method on [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec"). See its documentation for more.

## Implementations[§](#implementations)

[Source](https://doc.rust-lang.org/src/alloc/vec/peek_mut.rs.html#30)[§](#impl-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[Source](https://doc.rust-lang.org/src/alloc/vec/peek_mut.rs.html#37)

#### pub fn [pop](#method.pop)(this: [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;) -&gt; T

🔬This is a nightly-only experimental API. (`vec_peek_mut` [#122742](https://github.com/rust-lang/rust/issues/122742))

Removes the peeked value from the vector and returns it.

## Trait Implementations[§](#trait-implementations)

[Source](https://doc.rust-lang.org/src/alloc/vec/peek_mut.rs.html#24)[§](#impl-Debug-for-PeekMut%3C'_,+T,+A%3E)

### impl&lt;T, A&gt; [Debug](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'\_, T, A&gt;

[Source](https://doc.rust-lang.org/src/alloc/vec/peek_mut.rs.html#44)[§](#impl-Deref-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[Source](https://doc.rust-lang.org/src/alloc/vec/peek_mut.rs.html#55)[§](#impl-DerefMut-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [DerefMut](https://doc.rust-lang.org/std/ops/trait.DerefMut.html "trait std::ops::DerefMut") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

## Auto Trait Implementations[§](#synthetic-implementations)

[§](#impl-Freeze-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [Freeze](https://doc.rust-lang.org/std/marker/trait.Freeze.html "trait std::marker::Freeze") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-RefUnwindSafe-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [RefUnwindSafe](https://doc.rust-lang.org/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-Send-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [Send](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-Sync-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [Sync](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-Unpin-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [Unpin](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-UnwindSafe-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A = [Global](https://doc.rust-lang.org/std/alloc/struct.Global.html "struct std::alloc::Global")&gt; \![UnwindSafe](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") for [PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

## Blanket Implementations[§](#blanket-implementations)