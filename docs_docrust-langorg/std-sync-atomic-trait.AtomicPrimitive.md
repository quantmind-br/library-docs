---
title: AtomicPrimitive in std::sync::atomic - Rust
url: https://doc.rust-lang.org/std/sync/atomic/trait.AtomicPrimitive.html
source: crawler
fetched_at: 2026-05-06T21:29:52.137463075-03:00
rendered_js: false
word_count: 197
summary: This document defines the AtomicPrimitive trait, an experimental marker trait in Rust used to identify primitive types that support atomic modifications.
tags:
    - rust
    - atomic
    - concurrency
    - experimental-api
    - primitive-types
category: reference
---

## Trait AtomicPrimitive

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#274)

```rust
pub unsafe trait AtomicPrimitive:
    Sized
    + Copy
    + Sealed {
    type AtomicInner;
}
```

🔬This is a nightly-only experimental API. (`atomic_internals`)

Expand description

A marker trait for primitive types which can be modified atomically.

This is an implementation detail for `Atomic<T>` which may disappear or be replaced at any time.

## [§](#safety)Safety

Types implementing this trait must be primitives that can be modified atomically.

The associated `Self::AtomicInner` type must have the same size and bit validity as `Self`, but may have a higher alignment requirement, so the following `transmute`s are sound:

- `&mut Self::AtomicInner` as `&mut Self`
- `Self` as `Self::AtomicInner` or the reverse

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#276)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#297)[§](#impl-AtomicPrimitive-for-bool)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#297)[§](#associatedtype.AtomicInner-1)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#298)[§](#impl-AtomicPrimitive-for-i8)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#298)[§](#associatedtype.AtomicInner-2)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#300)[§](#impl-AtomicPrimitive-for-i16)

Available on **`target_has_atomic_load_store=16`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#300)[§](#associatedtype.AtomicInner-3)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#302)[§](#impl-AtomicPrimitive-for-i32)

Available on **`target_has_atomic_load_store=32`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#302)[§](#associatedtype.AtomicInner-4)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#304)[§](#impl-AtomicPrimitive-for-i64)

Available on **`target_has_atomic_load_store=64`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#304)[§](#associatedtype.AtomicInner-5)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#314)[§](#impl-AtomicPrimitive-for-isize)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#314)[§](#associatedtype.AtomicInner-6)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#299)[§](#impl-AtomicPrimitive-for-u8)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#299)[§](#associatedtype.AtomicInner-7)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#301)[§](#impl-AtomicPrimitive-for-u16)

Available on **`target_has_atomic_load_store=16`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#301)[§](#associatedtype.AtomicInner-8)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#303)[§](#impl-AtomicPrimitive-for-u32)

Available on **`target_has_atomic_load_store=32`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#303)[§](#associatedtype.AtomicInner-9)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#305)[§](#impl-AtomicPrimitive-for-u64)

Available on **`target_has_atomic_load_store=64`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#305)[§](#associatedtype.AtomicInner-10)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#321)[§](#impl-AtomicPrimitive-for-usize)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#321)[§](#associatedtype.AtomicInner-11)

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#328)[§](#impl-AtomicPrimitive-for-*mut+T)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#328)[§](#associatedtype.AtomicInner-12)