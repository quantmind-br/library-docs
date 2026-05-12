---
title: Sync in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.Sync.html
source: crawler
fetched_at: 2026-05-06T21:23:26.203629512-03:00
rendered_js: false
word_count: 1014
summary: The Sync trait identifies types in Rust that are safe to share across threads by ensuring no data races occur when accessing references.
tags:
    - rust
    - concurrency
    - thread-safety
    - marker-trait
    - memory-safety
    - parallelism
category: reference
---

## Trait Sync

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#660)

```rust
pub unsafe auto trait Sync { }
```

Expand description

Types for which it is safe to share references between threads.

This trait is automatically implemented when the compiler determines it’s appropriate.

The precise definition is: a type `T` is [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") if and only if `&T` is [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send"). In other words, if there is no possibility of [undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) (including data races) when passing `&T` references between threads.

As one would expect, primitive types like [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8") and [`f64`](https://doc.rust-lang.org/std/primitive.f64.html "primitive f64") are all [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync"), and so are simple aggregate types containing them, like tuples, structs and enums. More examples of basic [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") types include “immutable” types like `&T`, and those with simple inherited mutability, such as [`Box<T>`](https://doc.rust-lang.org/std/boxed/struct.Box.html), [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html) and most other collection types. (Generic parameters need to be [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") for their container to be [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").)

A somewhat surprising consequence of the definition is that `&mut T` is `Sync` (if `T` is `Sync`) even though it seems like that might provide unsynchronized mutation. The trick is that a mutable reference behind a shared reference (that is, `& &mut T`) becomes read-only, as if it were a `& &T`. Hence there is no risk of a data race.

A shorter overview of how [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") and [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") relate to referencing:

- `&T` is [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") if and only if `T` is [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync")
- `&mut T` is [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") if and only if `T` is [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send")
- `&T` and `&mut T` are [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") if and only if `T` is [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync")

Types that are not `Sync` are those that have “interior mutability” in a non-thread-safe form, such as [`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell") and [`RefCell`](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell"). These types allow for mutation of their contents even through an immutable, shared reference. For example the `set` method on [`Cell<T>`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell") takes `&self`, so it requires only a shared reference [`&Cell<T>`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell"). The method performs no synchronization, thus [`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell") cannot be `Sync`.

Another example of a non-`Sync` type is the reference-counting pointer [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html). Given any reference [`&Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html), you can clone a new [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html), modifying the reference counts in a non-atomic way.

For cases when one does need thread-safe interior mutability, Rust provides [atomic data types](https://doc.rust-lang.org/std/sync/atomic/index.html "mod std::sync::atomic"), as well as explicit locking via [`sync::Mutex`](https://doc.rust-lang.org/std/sync/struct.Mutex.html) and [`sync::RwLock`](https://doc.rust-lang.org/std/sync/struct.RwLock.html). These types ensure that any mutation cannot cause data races, hence the types are `Sync`. Likewise, [`sync::Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html) provides a thread-safe analogue of [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html).

Any types with interior mutability must also use the [`cell::UnsafeCell`](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html "struct std::cell::UnsafeCell") wrapper around the value(s) which can be mutated through a shared reference. Failing to doing this is [undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html). For example, [`transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html "fn std::mem::transmute")-ing from `&T` to `&mut T` is invalid.

See [the Nomicon](https://doc.rust-lang.org/nomicon/send-and-sync.html) for more details about `Sync`.

1.26.0 · [Source](https://doc.rust-lang.org/src/std/env.rs.html#857)[§](#impl-Sync-for-Args)

1.26.0 · [Source](https://doc.rust-lang.org/src/std/env.rs.html#916)[§](#impl-Sync-for-ArgsOs)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#906)[§](#impl-Sync-for-Arguments%3C'_%3E)

[Source](https://doc.rust-lang.org/src/core/task/wake.rs.html#981)[§](#impl-Sync-for-LocalWaker)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#675)[§](#impl-Sync-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#677)[§](#impl-Sync-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#325)[§](#impl-Sync-for-Cell%3CT%3E)

1.70.0 · [Source](https://doc.rust-lang.org/src/core/cell/once.rs.html#410)[§](#impl-Sync-for-OnceCell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#1439)[§](#impl-Sync-for-RefCell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#2328)[§](#impl-Sync-for-UnsafeCell%3CT%3E)

1.25.0 · [Source](https://doc.rust-lang.org/src/core/ptr/non_null.rs.html#90)[§](#impl-Sync-for-NonNull%3CT%3E)

`NonNull` pointers are not `Sync` because the data they reference may be aliased.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/sync/mpsc.rs.html#187)[§](#impl-Sync-for-Receiver%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#332)[§](#impl-Sync-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3919)[§](#impl-Sync-for-UniqueRc%3CT,+A%3E)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3187)[§](#impl-Sync-for-Weak%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#780)[§](#impl-Sync-for-Bytes%3C'_%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#738)[§](#impl-Sync-for-TypeId)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#130)[§](#impl-Sync-for-BorrowedHandle%3C'_%3E)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#128)[§](#impl-Sync-for-HandleOrInvalid)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#126)[§](#impl-Sync-for-HandleOrNull)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#124)[§](#impl-Sync-for-OwnedHandle)

Available on **Windows** only.

1.10.0 · [Source](https://doc.rust-lang.org/src/core/panic/location.rs.html#309)[§](#impl-Sync-for-Location%3C'_%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3510)[§](#impl-Sync-for-Drain%3C'_%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#389)[§](#impl-Sync-for-AtomicBool)

Available on **`target_has_atomic_load_store=8`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3596-3613)[§](#impl-Sync-for-AtomicI8)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3634-3651)[§](#impl-Sync-for-AtomicI16)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3672-3689)[§](#impl-Sync-for-AtomicI32)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3710-3727)[§](#impl-Sync-for-AtomicI64)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3851-3855)[§](#impl-Sync-for-AtomicIsize)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3615-3632)[§](#impl-Sync-for-AtomicU8)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3653-3670)[§](#impl-Sync-for-AtomicU16)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3691-3708)[§](#impl-Sync-for-AtomicU32)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3729-3746)[§](#impl-Sync-for-AtomicU64)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3851-3855)[§](#impl-Sync-for-AtomicUsize)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/wake.rs.html#416)[§](#impl-Sync-for-Waker)

1.44.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1523)[§](#impl-Sync-for-IoSlice%3C'a%3E)

1.44.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1365)[§](#impl-Sync-for-IoSliceMut%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/ptr/metadata.rs.html#214)[§](#impl-Sync-for-DynMetadata%3CDyn%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/thin.rs.html#50)[§](#impl-Sync-for-ThinBox%3CT%3E)

`ThinBox<T>` is `Sync` if `T` is `Sync` because the data is owned.

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#2620)[§](#impl-Sync-for-SyncUnsafeCell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2237)[§](#impl-Sync-for-Iter%3C'_,+T%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2243)[§](#impl-Sync-for-IterMut%3C'_,+T%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#181)[§](#impl-Sync-for-NonZero%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/pin/unsafe_pinned.rs.html#33)[§](#impl-Sync-for-UnsafePinned%3CT%3E)

1.31.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#2158)[§](#impl-Sync-for-ChunksExactMut%3C'_,+T%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#1816)[§](#impl-Sync-for-ChunksMut%3C'_,+T%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#90)[§](#impl-Sync-for-Iter%3C'_,+T%3E-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#215)[§](#impl-Sync-for-IterMut%3C'_,+T%3E-1)

1.31.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#2985)[§](#impl-Sync-for-RChunksExactMut%3C'_,+T%3E)

1.31.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#2626)[§](#impl-Sync-for-RChunksMut%3C'_,+T%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#421)[§](#impl-Sync-for-AtomicPtr%3CT%3E)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/std/sync/oneshot.rs.html#183)[§](#impl-Sync-for-Receiver%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/std/sync/oneshot.rs.html#93)[§](#impl-Sync-for-Sender%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/sync/exclusive.rs.html#96)[§](#impl-Sync-for-Exclusive%3CT%3E)

1.29.0 · [Source](https://doc.rust-lang.org/src/std/thread/join_handle.rs.html#76)[§](#impl-Sync-for-JoinHandle%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2249)[§](#impl-Sync-for-Cursor%3C'_,+T,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2255)[§](#impl-Sync-for-CursorMut%3C'_,+T,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2231)[§](#impl-Sync-for-LinkedList%3CT,+A%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/drain.rs.html#88)[§](#impl-Sync-for-Drain%3C'_,+T,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#276)[§](#impl-Sync-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4365)[§](#impl-Sync-for-UniqueArc%3CT,+A%3E)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#359)[§](#impl-Sync-for-Weak%3CT,+A%3E-1)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/drain.rs.html#146)[§](#impl-Sync-for-Drain%3C'_,+T,+A%3E-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/into_iter.rs.html#206)[§](#impl-Sync-for-IntoIter%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/std/sync/reentrant_lock.rs.html#184)[§](#impl-Sync-for-ReentrantLock%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/mpmc/mod.rs.html#879)[§](#impl-Sync-for-Receiver%3CT%3E-2)

[Source](https://doc.rust-lang.org/src/std/sync/mpmc/mod.rs.html#319)[§](#impl-Sync-for-Sender%3CT%3E-1)

1.72.0 · [Source](https://doc.rust-lang.org/src/std/sync/mpsc.rs.html#343)[§](#impl-Sync-for-Sender%3CT%3E-2)

1.70.0 · [Source](https://doc.rust-lang.org/src/std/sync/once_lock.rs.html#584)[§](#impl-Sync-for-OnceLock%3CT%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/std/sync/lazy_lock.rs.html#416)[§](#impl-Sync-for-LazyLock%3CT,+F%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#54)[§](#impl-Sync-for-RwLock%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#107)[§](#impl-Sync-for-RwLock%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/mutex.rs.html#79)[§](#impl-Sync-for-Mutex%3CT%3E)

`T` must be `Send` for [`Mutex`](https://doc.rust-lang.org/std/sync/nonpoison/struct.Mutex.html "struct std::sync::nonpoison::Mutex") to be `Sync`. This ensures that the protected data can be accessed safely from multiple threads without causing data races or other unsafe behavior.

[`Mutex<T>`](https://doc.rust-lang.org/std/sync/nonpoison/struct.Mutex.html "struct std::sync::nonpoison::Mutex") provides mutable access to `T` to one thread at a time. However, it’s essential for `T` to be `Send` because it’s not safe for non-`Send` structures to be accessed in this manner. For instance, consider [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc"), a non-atomic reference counted smart pointer, which is not `Send`. With `Rc`, we can have multiple copies pointing to the same heap allocation with a non-atomic reference count. If we were to use `Mutex<Rc<_>>`, it would only protect one instance of `Rc` from shared access, leaving other copies vulnerable to potential data races.

Also note that it is not necessary for `T` to be `Sync` as `&T` is only made available to one thread at a time if `T` is not `Sync`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/mutex.rs.html#257)[§](#impl-Sync-for-Mutex%3CT%3E-1)

`T` must be `Send` for [`Mutex`](https://doc.rust-lang.org/std/sync/struct.Mutex.html "struct std::sync::Mutex") to be `Sync`. This ensures that the protected data can be accessed safely from multiple threads without causing data races or other unsafe behavior.

[`Mutex<T>`](https://doc.rust-lang.org/std/sync/struct.Mutex.html "struct std::sync::Mutex") provides mutable access to `T` to one thread at a time. However, it’s essential for `T` to be `Send` because it’s not safe for non-`Send` structures to be accessed in this manner. For instance, consider [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc"), a non-atomic reference counted smart pointer, which is not `Send`. With `Rc`, we can have multiple copies pointing to the same heap allocation with a non-atomic reference count. If we were to use `Mutex<Rc<_>>`, it would only protect one instance of `Rc` from shared access, leaving other copies vulnerable to potential data races.

Also note that it is not necessary for `T` to be `Sync` as `&T` is only made available to one thread at a time if `T` is not `Sync`.

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/mutex.rs.html#156)[§](#impl-Sync-for-MappedMutexGuard%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#150)[§](#impl-Sync-for-MappedRwLockReadGuard%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#186)[§](#impl-Sync-for-MappedRwLockWriteGuard%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/mutex.rs.html#115)[§](#impl-Sync-for-MutexGuard%3C'_,+T%3E)

`T` must be `Sync` for a [`MutexGuard<T>`](https://doc.rust-lang.org/std/sync/nonpoison/struct.MutexGuard.html "struct std::sync::nonpoison::MutexGuard") to be `Sync` because it is possible to get a `&T` from `&MutexGuard` (via `Deref`).

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#90)[§](#impl-Sync-for-RwLockReadGuard%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#116)[§](#impl-Sync-for-RwLockWriteGuard%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/poison/mutex.rs.html#335)[§](#impl-Sync-for-MappedMutexGuard%3C'_,+T%3E-1)

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#202)[§](#impl-Sync-for-MappedRwLockReadGuard%3C'_,+T%3E-1)

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#239)[§](#impl-Sync-for-MappedRwLockWriteGuard%3C'_,+T%3E-1)

1.19.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/mutex.rs.html#294)[§](#impl-Sync-for-MutexGuard%3C'_,+T%3E-1)

`T` must be `Sync` for a [`MutexGuard<T>`](https://doc.rust-lang.org/std/sync/struct.MutexGuard.html "struct std::sync::MutexGuard") to be `Sync` because it is possible to get a `&T` from `&MutexGuard` (via `Deref`).

[Source](https://doc.rust-lang.org/src/std/sync/reentrant_lock.rs.html#218)[§](#impl-Sync-for-ReentrantLockGuard%3C'_,+T%3E)

1.23.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#143)[§](#impl-Sync-for-RwLockReadGuard%3C'_,+T%3E-1)

1.23.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#171)[§](#impl-Sync-for-RwLockWriteGuard%3C'_,+T%3E-1)