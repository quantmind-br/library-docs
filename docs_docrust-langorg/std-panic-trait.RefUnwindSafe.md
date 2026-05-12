---
title: RefUnwindSafe in std::panic - Rust
url: https://doc.rust-lang.org/std/panic/trait.RefUnwindSafe.html
source: crawler
fetched_at: 2026-05-06T21:24:04.410825956-03:00
rendered_js: false
word_count: 187
summary: RefUnwindSafe is a marker trait in Rust used to identify types where a shared reference is safe to use across panic unwinding boundaries.
tags:
    - rust
    - marker-trait
    - panic-handling
    - unwind-safety
    - concurrency
    - memory-safety
category: reference
---

## Trait RefUnwindSafe

1.9.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#108)

```rust
pub auto trait RefUnwindSafe { }
```

Expand description

A marker trait representing types where a shared reference is considered unwind safe.

This trait is namely not implemented by [`UnsafeCell`](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html "struct std::cell::UnsafeCell"), the root of all interior mutability.

This is a “helper marker trait” used to provide impl blocks for the [`UnwindSafe`](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") trait, for more information see that documentation.

1.9.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#200)[§](#impl-RefUnwindSafe-for-UnsafeCell%3CT%3E)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1009)[§](#impl-RefUnwindSafe-for-Stderr)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1074)[§](#impl-RefUnwindSafe-for-StderrLock%3C'_%3E)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#777)[§](#impl-RefUnwindSafe-for-Stdout)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#842)[§](#impl-RefUnwindSafe-for-StdoutLock%3C'_%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#244)[§](#impl-RefUnwindSafe-for-AtomicBool)

Available on **`target_has_atomic_load_store=8`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#209)[§](#impl-RefUnwindSafe-for-AtomicI8)

Available on **`target_has_atomic_load_store=8`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#212)[§](#impl-RefUnwindSafe-for-AtomicI16)

Available on **`target_has_atomic_load_store=16`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#215)[§](#impl-RefUnwindSafe-for-AtomicI32)

Available on **`target_has_atomic_load_store=32`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#218)[§](#impl-RefUnwindSafe-for-AtomicI64)

Available on **`target_has_atomic_load_store=64`** only.

1.14.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#206)[§](#impl-RefUnwindSafe-for-AtomicIsize)

Available on **`target_has_atomic_load_store=ptr`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#228)[§](#impl-RefUnwindSafe-for-AtomicU8)

Available on **`target_has_atomic_load_store=8`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#231)[§](#impl-RefUnwindSafe-for-AtomicU16)

Available on **`target_has_atomic_load_store=16`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#234)[§](#impl-RefUnwindSafe-for-AtomicU32)

Available on **`target_has_atomic_load_store=32`** only.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#237)[§](#impl-RefUnwindSafe-for-AtomicU64)

Available on **`target_has_atomic_load_store=64`** only.

1.14.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#225)[§](#impl-RefUnwindSafe-for-AtomicUsize)

Available on **`target_has_atomic_load_store=ptr`** only.

1.12.0 · [Source](https://doc.rust-lang.org/src/std/sync/barrier.rs.html#36)[§](#impl-RefUnwindSafe-for-Barrier)

1.12.0 · [Source](https://doc.rust-lang.org/src/std/panic.rs.html#275)[§](#impl-RefUnwindSafe-for-Condvar)

1.59.0 · [Source](https://doc.rust-lang.org/src/std/sync/once.rs.html#43)[§](#impl-RefUnwindSafe-for-Once)

1.28.0 · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#179)[§](#impl-RefUnwindSafe-for-NonZero%3CT%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#248)[§](#impl-RefUnwindSafe-for-AtomicPtr%3CT%3E)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/std/sync/mpmc/mod.rs.html#884)[§](#impl-RefUnwindSafe-for-Receiver%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/mpmc/mod.rs.html#324)[§](#impl-RefUnwindSafe-for-Sender%3CT%3E)

1.9.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#202)[§](#impl-RefUnwindSafe-for-AssertUnwindSafe%3CT%3E)

1.58.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#337)[§](#impl-RefUnwindSafe-for-Rc%3CT,+A%3E)

1.70.0 · [Source](https://doc.rust-lang.org/src/std/sync/once_lock.rs.html#589)[§](#impl-RefUnwindSafe-for-OnceLock%3CT%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/std/sync/lazy_lock.rs.html#420)[§](#impl-RefUnwindSafe-for-LazyLock%3CT,+F%3E)

[Source](https://doc.rust-lang.org/src/std/sync/reentrant_lock.rs.html#190)[§](#impl-RefUnwindSafe-for-ReentrantLock%3CT%3E)

1.12.0 · [Source](https://doc.rust-lang.org/src/std/panic.rs.html#271)[§](#impl-RefUnwindSafe-for-Mutex%3CT%3E)

1.12.0 · [Source](https://doc.rust-lang.org/src/std/panic.rs.html#273)[§](#impl-RefUnwindSafe-for-RwLock%3CT%3E)