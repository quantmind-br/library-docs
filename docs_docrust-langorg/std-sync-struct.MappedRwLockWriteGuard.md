---
title: MappedRwLockWriteGuard in std::sync - Rust
url: https://doc.rust-lang.org/std/sync/struct.MappedRwLockWriteGuard.html
source: crawler
fetched_at: 2026-05-06T21:36:33.246308466-03:00
rendered_js: false
word_count: 223
summary: The MappedRwLockWriteGuard provides an RAII mechanism to release exclusive write access to a lock while pointing to a subfield of the protected data.
tags:
    - rust
    - sync
    - rwlock
    - concurrency
    - raii
    - memory-safety
category: api
---

## Struct MappedRwLockWriteGuard

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#218-233)

```rust
pub struct MappedRwLockWriteGuard<'rwlock, T: ?Sized + 'rwlock> { /* private fields */ }
```

🔬This is a nightly-only experimental API. (`mapped_lock_guards` [#117108](https://github.com/rust-lang/rust/issues/117108))

Expand description

RAII structure used to release the exclusive write access of a lock when dropped, which can point to a subfield of the protected data.

This structure is created by the [`map`](https://doc.rust-lang.org/std/sync/struct.RwLockWriteGuard.html#method.map "associated function std::sync::RwLockWriteGuard::map") and [`filter_map`](https://doc.rust-lang.org/std/sync/struct.RwLockWriteGuard.html#method.filter_map "associated function std::sync::RwLockWriteGuard::filter_map") methods on [`RwLockWriteGuard`](https://doc.rust-lang.org/std/sync/struct.RwLockWriteGuard.html "struct std::sync::RwLockWriteGuard").

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#1038-1115)[§](#impl-MappedRwLockWriteGuard%3C'rwlock,+T%3E)

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#1053-1071)

🔬This is a nightly-only experimental API. (`mapped_lock_guards` [#117108](https://github.com/rust-lang/rust/issues/117108))

Makes a [`MappedRwLockWriteGuard`](https://doc.rust-lang.org/std/sync/struct.MappedRwLockWriteGuard.html "struct std::sync::MappedRwLockWriteGuard") for a component of the borrowed data, e.g. an enum variant.

The `RwLock` is already locked for writing, so this cannot fail.

This is an associated function that needs to be used as `MappedRwLockWriteGuard::map(...)`. A method would interfere with methods of the same name on the contents of the `MappedRwLockWriteGuard` used through `Deref`.

##### [§](#panics)Panics

If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.

[Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#1088-1114)

🔬This is a nightly-only experimental API. (`mapped_lock_guards` [#117108](https://github.com/rust-lang/rust/issues/117108))

Makes a [`MappedRwLockWriteGuard`](https://doc.rust-lang.org/std/sync/struct.MappedRwLockWriteGuard.html "struct std::sync::MappedRwLockWriteGuard") for a component of the borrowed data. The original guard is returned as an `Err(...)` if the closure returns `None`.

The `RwLock` is already locked for writing, so this cannot fail.

This is an associated function that needs to be used as `MappedRwLockWriteGuard::filter_map(...)`. A method would interfere with methods of the same name on the contents of the `MappedRwLockWriteGuard` used through `Deref`.

##### [§](#panics-1)Panics

If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.