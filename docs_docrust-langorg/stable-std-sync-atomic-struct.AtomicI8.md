---
title: AtomicI8 in std::sync::atomic - Rust
url: https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html
source: crawler
fetched_at: 2026-05-06T21:39:09.818988783-03:00
rendered_js: false
word_count: 2662
summary: This document describes the AtomicI8 type in Rust, which provides an 8-bit signed integer that can be safely accessed and modified across multiple threads using atomic operations.
tags:
    - rust
    - atomic
    - concurrency
    - thread-safety
    - memory-ordering
    - integer-types
category: reference
---

## Struct AtomicI8

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

```rust
pub struct AtomicI8 { /* private fields */ }
```

Expand description

An integer type which can be safely shared between threads.

This type has the same size, alignment, and bit validity as the underlying integer type, [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

For more about the differences between atomic types and non-atomic types as well as information about the portability of this type, please see the [module-level documentation](https://doc.rust-lang.org/stable/std/sync/atomic/index.html "mod std::sync::atomic").

**Note:** This type is only available on platforms that support atomic loads and stores of [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)[§](#impl-AtomicI8)

1.34.0 (const: 1.34.0) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Creates a new atomic integer.

##### [§](#examples)Examples

```rust
use std::sync::atomic::AtomicI8;

let atomic_forty_two = AtomicI8::new(42);
```

1.75.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Creates a new reference to an atomic integer from a pointer.

##### [§](#examples-1)Examples

```rust
use std::sync::atomic::{self, AtomicI8};

// Get a pointer to an allocated value
let ptr: *mut i8 = Box::into_raw(Box::new(0));

assert!(ptr.cast::<AtomicI8>().is_aligned());

{
    // Create an atomic view of the allocated value
    let atomic = unsafe {AtomicI8::from_ptr(ptr) };

    // Use `atomic` for atomic operations, possibly share it with other threads
    atomic.store(1, atomic::Ordering::Relaxed);
}

// It's ok to non-atomically access the value behind `ptr`,
// since the reference to the atomic ended its lifetime in the block above
assert_eq!(unsafe { *ptr }, 1);

// Deallocate the value
unsafe { drop(Box::from_raw(ptr)) }
```

##### [§](#safety)Safety

- `ptr` must be aligned to `align_of::<AtomicI8>()` (note that this is always true, since `align_of::<AtomicI8>() == 1`).
- `ptr` must be [valid](https://doc.rust-lang.org/stable/std/ptr/index.html#safety "mod std::ptr") for both reads and writes for the whole lifetime `'a`.
- You must adhere to the [Memory model for atomic accesses](https://doc.rust-lang.org/stable/std/sync/atomic/index.html#memory-model-for-atomic-accesses "mod std::sync::atomic"). In particular, it is not allowed to mix conflicting atomic and non-atomic accesses, or atomic accesses of different sizes, without synchronization.

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Returns a mutable reference to the underlying integer.

This is safe because the mutable reference guarantees that no other threads are concurrently accessing the atomic data.

##### [§](#examples-2)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let mut some_var = AtomicI8::new(10);
assert_eq!(*some_var.get_mut(), 10);
*some_var.get_mut() = 5;
assert_eq!(some_var.load(Ordering::SeqCst), 5);
```

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

🔬This is a nightly-only experimental API. (`atomic_from_mut` [#76314](https://github.com/rust-lang/rust/issues/76314))

Available on **`target_has_atomic_equal_alignment=8`** only.

Get atomic access to a `&mut i8`.

##### [§](#examples-3)Examples

```rust
#![feature(atomic_from_mut)]
use std::sync::atomic::{AtomicI8, Ordering};

let mut some_int = 123;
let a = AtomicI8::from_mut(&mut some_int);
a.store(100, Ordering::Relaxed);
assert_eq!(some_int, 100);
```

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

🔬This is a nightly-only experimental API. (`atomic_from_mut` [#76314](https://github.com/rust-lang/rust/issues/76314))

Get non-atomic access to a `&mut [AtomicI8]` slice

This is safe because the mutable reference guarantees that no other threads are concurrently accessing the atomic data.

##### [§](#examples-4)Examples

[ⓘ](# "This example is not tested on wasm")

```rust
#![feature(atomic_from_mut)]
use std::sync::atomic::{AtomicI8, Ordering};

let mut some_ints = [const { AtomicI8::new(0) }; 10];

let view: &mut [i8] = AtomicI8::get_mut_slice(&mut some_ints);
assert_eq!(view, [0; 10]);
view
    .iter_mut()
    .enumerate()
    .for_each(|(idx, int)| *int = idx as _);

std::thread::scope(|s| {
    some_ints
        .iter()
        .enumerate()
        .for_each(|(idx, int)| {
            s.spawn(move || assert_eq!(int.load(Ordering::Relaxed), idx as _));
        })
});
```

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

🔬This is a nightly-only experimental API. (`atomic_from_mut` [#76314](https://github.com/rust-lang/rust/issues/76314))

Available on **`target_has_atomic_equal_alignment=8`** only.

Get atomic access to a `&mut [i8]` slice.

##### [§](#examples-5)Examples

[ⓘ](# "This example is not tested on wasm")

```rust
#![feature(atomic_from_mut)]
use std::sync::atomic::{AtomicI8, Ordering};

let mut some_ints = [0; 10];
let a = &*AtomicI8::from_mut_slice(&mut some_ints);
std::thread::scope(|s| {
    for i in 0..a.len() {
        s.spawn(move || a[i].store(i as _, Ordering::Relaxed));
    }
});
for (i, n) in some_ints.into_iter().enumerate() {
    assert_eq!(i, n as usize);
}
```

1.34.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Consumes the atomic and returns the contained value.

This is safe because passing `self` by value guarantees that no other threads are concurrently accessing the atomic data.

##### [§](#examples-6)Examples

```rust
use std::sync::atomic::AtomicI8;

let some_var = AtomicI8::new(5);
assert_eq!(some_var.into_inner(), 5);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Loads a value from the atomic integer.

`load` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. Possible values are [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") and [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

##### [§](#panics)Panics

Panics if `order` is [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") or [`AcqRel`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.AcqRel "variant std::sync::atomic::Ordering::AcqRel").

##### [§](#examples-7)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let some_var = AtomicI8::new(5);

assert_eq!(some_var.load(Ordering::Relaxed), 5);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Stores a value into the atomic integer.

`store` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. Possible values are [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") and [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

##### [§](#panics-1)Panics

Panics if `order` is [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") or [`AcqRel`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.AcqRel "variant std::sync::atomic::Ordering::AcqRel").

##### [§](#examples-8)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let some_var = AtomicI8::new(5);

some_var.store(10, Ordering::Relaxed);
assert_eq!(some_var.load(Ordering::Relaxed), 10);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Stores a value into the atomic integer, returning the previous value.

`swap` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-9)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let some_var = AtomicI8::new(5);

assert_eq!(some_var.swap(10, Ordering::Relaxed), 5);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

👎Deprecated since 1.50.0: Use `compare_exchange` or `compare_exchange_weak` instead

Available on **`target_has_atomic=8`** only.

Stores a value into the atomic integer if the current value is the same as the `current` value.

The return value is always the previous value. If it is equal to `current`, then the value was updated.

`compare_and_swap` also takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. Notice that even when using [`AcqRel`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.AcqRel "variant std::sync::atomic::Ordering::AcqRel"), the operation might fail and hence just perform an `Acquire` load, but not have `Release` semantics. Using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed") if it happens, and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#migrating-to-compare_exchange-and-compare_exchange_weak)Migrating to `compare_exchange` and `compare_exchange_weak`

`compare_and_swap` is equivalent to `compare_exchange` with the following mapping for memory orderings:

OriginalSuccessFailure RelaxedRelaxedRelaxed AcquireAcquireAcquire ReleaseReleaseRelaxed AcqRelAcqRelAcquire SeqCstSeqCstSeqCst

`compare_and_swap` and `compare_exchange` also differ in their return type. You can use `compare_exchange(...).unwrap_or_else(|x| x)` to recover the behavior of `compare_and_swap`, but in most cases it is more idiomatic to check whether the return value is `Ok` or `Err` rather than to infer success vs failure based on the value that was read.

During migration, consider whether it makes sense to use `compare_exchange_weak` instead. `compare_exchange_weak` is allowed to fail spuriously even when the comparison succeeds, which allows the compiler to generate better assembly code when the compare and swap is used in a loop.

##### [§](#examples-10)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let some_var = AtomicI8::new(5);

assert_eq!(some_var.compare_and_swap(5, 10, Ordering::Relaxed), 5);
assert_eq!(some_var.load(Ordering::Relaxed), 10);

assert_eq!(some_var.compare_and_swap(6, 12, Ordering::Relaxed), 10);
assert_eq!(some_var.load(Ordering::Relaxed), 10);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Stores a value into the atomic integer if the current value is the same as the `current` value.

The return value is a result indicating whether the new value was written and containing the previous value. On success this value is guaranteed to be equal to `current`.

`compare_exchange` takes two [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") arguments to describe the memory ordering of this operation. `success` describes the required ordering for the read-modify-write operation that takes place if the comparison with `current` succeeds. `failure` describes the required ordering for the load operation that takes place when the comparison fails. Using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") as success ordering makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the successful load [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"). The failure ordering can only be [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") or [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-11)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let some_var = AtomicI8::new(5);

assert_eq!(some_var.compare_exchange(5, 10,
                                     Ordering::Acquire,
                                     Ordering::Relaxed),
           Ok(5));
assert_eq!(some_var.load(Ordering::Relaxed), 10);

assert_eq!(some_var.compare_exchange(6, 12,
                                     Ordering::SeqCst,
                                     Ordering::Acquire),
           Err(10));
assert_eq!(some_var.load(Ordering::Relaxed), 10);
```

##### [§](#considerations)Considerations

`compare_exchange` is a [compare-and-swap operation](https://en.wikipedia.org/wiki/Compare-and-swap) and thus exhibits the usual downsides of CAS operations. In particular, a load of the value followed by a successful `compare_exchange` with the previous load *does not ensure* that other threads have not changed the value in the interim! This is usually important when the *equality* check in the `compare_exchange` is being used to check the *identity* of a value, but equality does not necessarily imply identity. This is a particularly common case for pointers, as a pointer holding the same address does not imply that the same object exists at that address! In this case, `compare_exchange` can lead to the [ABA problem](https://en.wikipedia.org/wiki/ABA_problem).

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Stores a value into the atomic integer if the current value is the same as the `current` value.

Unlike [`AtomicI8::compare_exchange`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html#method.compare_exchange "method std::sync::atomic::AtomicI8::compare_exchange"), this function is allowed to spuriously fail even when the comparison succeeds, which can result in more efficient code on some platforms. The return value is a result indicating whether the new value was written and containing the previous value.

`compare_exchange_weak` takes two [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") arguments to describe the memory ordering of this operation. `success` describes the required ordering for the read-modify-write operation that takes place if the comparison with `current` succeeds. `failure` describes the required ordering for the load operation that takes place when the comparison fails. Using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") as success ordering makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the successful load [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"). The failure ordering can only be [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") or [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-12)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let val = AtomicI8::new(4);

let mut old = val.load(Ordering::Relaxed);
loop {
    let new = old * 2;
    match val.compare_exchange_weak(old, new, Ordering::SeqCst, Ordering::Relaxed) {
        Ok(_) => break,
        Err(x) => old = x,
    }
}
```

##### [§](#considerations-1)Considerations

`compare_exchange` is a [compare-and-swap operation](https://en.wikipedia.org/wiki/Compare-and-swap) and thus exhibits the usual downsides of CAS operations. In particular, a load of the value followed by a successful `compare_exchange` with the previous load *does not ensure* that other threads have not changed the value in the interim. This is usually important when the *equality* check in the `compare_exchange` is being used to check the *identity* of a value, but equality does not necessarily imply identity. This is a particularly common case for pointers, as a pointer holding the same address does not imply that the same object exists at that address! In this case, `compare_exchange` can lead to the [ABA problem](https://en.wikipedia.org/wiki/ABA_problem).

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Adds to the current value, returning the previous value.

This operation wraps around on overflow.

`fetch_add` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-13)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(0);
assert_eq!(foo.fetch_add(10, Ordering::SeqCst), 0);
assert_eq!(foo.load(Ordering::SeqCst), 10);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Subtracts from the current value, returning the previous value.

This operation wraps around on overflow.

`fetch_sub` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-14)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(20);
assert_eq!(foo.fetch_sub(10, Ordering::SeqCst), 20);
assert_eq!(foo.load(Ordering::SeqCst), 10);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Bitwise “and” with the current value.

Performs a bitwise “and” operation on the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_and` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-15)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(0b101101);
assert_eq!(foo.fetch_and(0b110011, Ordering::SeqCst), 0b101101);
assert_eq!(foo.load(Ordering::SeqCst), 0b100001);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Bitwise “nand” with the current value.

Performs a bitwise “nand” operation on the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_nand` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-16)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(0x13);
assert_eq!(foo.fetch_nand(0x31, Ordering::SeqCst), 0x13);
assert_eq!(foo.load(Ordering::SeqCst), !(0x13 & 0x31));
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Bitwise “or” with the current value.

Performs a bitwise “or” operation on the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_or` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-17)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(0b101101);
assert_eq!(foo.fetch_or(0b110011, Ordering::SeqCst), 0b101101);
assert_eq!(foo.load(Ordering::SeqCst), 0b111111);
```

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Bitwise “xor” with the current value.

Performs a bitwise “xor” operation on the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_xor` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-18)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(0b101101);
assert_eq!(foo.fetch_xor(0b110011, Ordering::SeqCst), 0b101101);
assert_eq!(foo.load(Ordering::SeqCst), 0b011110);
```

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

👎Deprecating in 1.99.0: renamed to `try_update` for consistency

Available on **`target_has_atomic=8`** only.

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Fetches the value, and applies a function to it that returns an optional new value. Returns a `Result` of `Ok(previous_value)` if the function returned `Some(_)`, else `Err(previous_value)`.

See also: [`update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html#method.update "method std::sync::atomic::AtomicI8::update").

Note: This may call the function multiple times if the value has been changed from other threads in the meantime, as long as the function returns `Some(_)`, but the function will have been applied only once to the stored value.

`try_update` takes two [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") arguments to describe the memory ordering of this operation. The first describes the required ordering for when the operation finally succeeds while the second describes the required ordering for loads. These correspond to the success and failure orderings of [`AtomicI8::compare_exchange`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html#method.compare_exchange "method std::sync::atomic::AtomicI8::compare_exchange") respectively.

Using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") as success ordering makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the final successful load [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"). The (failed) load ordering can only be [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") or [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#considerations-2)Considerations

This method is not magic; it is not provided by the hardware, and does not act like a critical section or mutex.

It is implemented on top of an atomic [compare-and-swap operation](https://en.wikipedia.org/wiki/Compare-and-swap), and thus is subject to the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem](https://en.wikipedia.org/wiki/ABA_problem) if this atomic integer is an index or more generally if knowledge of only the *bitwise value* of the atomic is not in and of itself sufficient to ensure any required preconditions.

##### [§](#examples-19)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let x = AtomicI8::new(7);
assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |_| None), Err(7));
assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(x + 1)), Ok(7));
assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(x + 1)), Ok(8));
assert_eq!(x.load(Ordering::SeqCst), 9);
```

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Fetches the value, applies a function to it that it return a new value. The new value is stored and the old value is returned.

See also: [`try_update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html#method.try_update "method std::sync::atomic::AtomicI8::try_update").

Note: This may call the function multiple times if the value has been changed from other threads in the meantime, but the function will have been applied only once to the stored value.

`update` takes two [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") arguments to describe the memory ordering of this operation. The first describes the required ordering for when the operation finally succeeds while the second describes the required ordering for loads. These correspond to the success and failure orderings of [`AtomicI8::compare_exchange`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicI8.html#method.compare_exchange "method std::sync::atomic::AtomicI8::compare_exchange") respectively.

Using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") as success ordering makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the final successful load [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"). The (failed) load ordering can only be [`SeqCst`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.SeqCst "variant std::sync::atomic::Ordering::SeqCst"), [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") or [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#considerations-3)Considerations

This method is not magic; it is not provided by the hardware, and does not act like a critical section or mutex.

It is implemented on top of an atomic [compare-and-swap operation](https://en.wikipedia.org/wiki/Compare-and-swap), and thus is subject to the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem](https://en.wikipedia.org/wiki/ABA_problem) if this atomic integer is an index or more generally if knowledge of only the *bitwise value* of the atomic is not in and of itself sufficient to ensure any required preconditions.

##### [§](#examples-20)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let x = AtomicI8::new(7);
assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| x + 1), 7);
assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| x + 1), 8);
assert_eq!(x.load(Ordering::SeqCst), 9);
```

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Maximum with the current value.

Finds the maximum of the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_max` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-21)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(23);
assert_eq!(foo.fetch_max(42, Ordering::SeqCst), 23);
assert_eq!(foo.load(Ordering::SeqCst), 42);
```

If you want to obtain the maximum value in one step, you can use the following:

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(23);
let bar = 42;
let max_foo = foo.fetch_max(bar, Ordering::SeqCst).max(bar);
assert!(max_foo == 42);
```

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Available on **`target_has_atomic=8`** only.

Minimum with the current value.

Finds the minimum of the current value and the argument `val`, and sets the new value to the result.

Returns the previous value.

`fetch_min` takes an [`Ordering`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") argument which describes the memory ordering of this operation. All ordering modes are possible. Note that using [`Acquire`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Acquire "variant std::sync::atomic::Ordering::Acquire") makes the store part of this operation [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed"), and using [`Release`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Release "variant std::sync::atomic::Ordering::Release") makes the load part [`Relaxed`](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html#variant.Relaxed "variant std::sync::atomic::Ordering::Relaxed").

**Note**: This method is only available on platforms that support atomic operations on [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8").

##### [§](#examples-22)Examples

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(23);
assert_eq!(foo.fetch_min(42, Ordering::Relaxed), 23);
assert_eq!(foo.load(Ordering::Relaxed), 23);
assert_eq!(foo.fetch_min(22, Ordering::Relaxed), 23);
assert_eq!(foo.load(Ordering::Relaxed), 22);
```

If you want to obtain the minimum value in one step, you can use the following:

```rust
use std::sync::atomic::{AtomicI8, Ordering};

let foo = AtomicI8::new(23);
let bar = 12;
let min_foo = foo.fetch_min(bar, Ordering::SeqCst).min(bar);
assert_eq!(min_foo, 12);
```

1.70.0 (const: 1.70.0) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#3596-3613)

Returns a mutable pointer to the underlying integer.

Doing non-atomic reads and writes on the resulting integer can be a data race. This method is mostly useful for FFI, where the function signature may use `*mut i8` instead of `&AtomicI8`.

Returning an `*mut` pointer from a shared reference to this atomic is safe because the atomic types work with interior mutability. All modifications of an atomic change the value through a shared reference, and can do so safely as long as they use atomic operations. Any use of the returned raw pointer requires an `unsafe` block and still has to uphold the requirements of the [memory model](https://doc.rust-lang.org/stable/std/sync/atomic/index.html#memory-model-for-atomic-accesses "mod std::sync::atomic").

##### [§](#examples-23)Examples

[ⓘ](# "This example is not tested")

```rust
use std::sync::atomic::AtomicI8;

extern "C" {
    fn my_atomic_op(arg: *mut i8);
}

let atomic = AtomicI8::new(1);

// SAFETY: Safe as long as `my_atomic_op` is atomic.
unsafe {
    my_atomic_op(atomic.as_ptr());
}
```

[§](#impl-Freeze-for-AtomicI8)

[§](#impl-Send-for-AtomicI8)

[§](#impl-Unpin-for-AtomicI8)

[§](#impl-UnsafeUnpin-for-AtomicI8)

[§](#impl-UnwindSafe-for-AtomicI8)