---
title: std::sync::atomic - Rust
url: https://doc.rust-lang.org/std/sync/atomic/index.html
source: crawler
fetched_at: 2026-05-06T21:21:51.660581976-03:00
rendered_js: false
word_count: 1389
summary: This module provides primitive atomic types that enable shared-memory communication and synchronization between threads in Rust, following the C++20 memory model.
tags:
    - rust
    - concurrency
    - atomics
    - multithreading
    - memory-model
    - synchronization
    - thread-safety
category: reference
---

## Module atomic

1.0.0 · [Source](https://doc.rust-lang.org/src/core/sync/mod.rs.html#5)

Expand description

Atomic types

Atomic types provide primitive shared-memory communication between threads, and are the building blocks of other concurrent types.

This module defines atomic versions of a select number of primitive types, including [`AtomicBool`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html "struct std::sync::atomic::AtomicBool"), [`AtomicIsize`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicIsize.html "struct std::sync::atomic::AtomicIsize"), [`AtomicUsize`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html "struct std::sync::atomic::AtomicUsize"), [`AtomicI8`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI8.html "struct std::sync::atomic::AtomicI8"), [`AtomicU16`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU16.html "struct std::sync::atomic::AtomicU16"), etc. Atomic types present operations that, when used correctly, synchronize updates between threads.

Atomic variables are safe to share between threads (they implement [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync")) but they do not themselves provide the mechanism for sharing and follow the [threading model](https://doc.rust-lang.org/std/thread/index.html#the-threading-model) of Rust. The most common way to share an atomic variable is to put it into an [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html) (an atomically-reference-counted shared pointer).

Atomic types may be stored in static variables, initialized using the constant initializers like [`AtomicBool::new`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html#method.new "associated function std::sync::atomic::AtomicBool::new"). Atomic statics are often used for lazy global initialization.

### [§](#memory-model-for-atomic-accesses)Memory model for atomic accesses

Rust atomics currently follow the same rules as [C++20 atomics](https://en.cppreference.com/w/cpp/atomic), specifically the rules from the [`intro.races`](https://timsong-cpp.github.io/cppwp/n4868/intro.multithread#intro.races) section, without the “consume” memory ordering. Since C++ uses an object-based memory model whereas Rust is access-based, a bit of translation work has to be done to apply the C++ rules to Rust: whenever C++ talks about “the value of an object”, we understand that to mean the resulting bytes obtained when doing a read. When the C++ standard talks about “the value of an atomic object”, this refers to the result of doing an atomic load (via the operations provided in this module). A “modification of an atomic object” refers to an atomic store.

The end result is *almost* equivalent to saying that creating a *shared reference* to one of the Rust atomic types corresponds to creating an `atomic_ref` in C++, with the `atomic_ref` being destroyed when the lifetime of the shared reference ends. The main difference is that Rust permits concurrent atomic and non-atomic reads to the same memory as those cause no issue in the C++ memory model, they are just forbidden in C++ because memory is partitioned into “atomic objects” and “non-atomic objects” (with `atomic_ref` temporarily converting a non-atomic object into an atomic object).

The most important aspect of this model is that *data races* are undefined behavior. A data race is defined as conflicting non-synchronized accesses where at least one of the accesses is non-atomic. Here, accesses are *conflicting* if they affect overlapping regions of memory and at least one of them is a write. (A `compare_exchange` or `compare_exchange_weak` that does not succeed is not considered a write.) They are *non-synchronized* if neither of them *happens-before* the other, according to the happens-before order of the memory model.

The other possible cause of undefined behavior in the memory model are mixed-size accesses: Rust inherits the C++ limitation that non-synchronized conflicting atomic accesses may not partially overlap. In other words, every pair of non-synchronized atomic accesses must be either disjoint, access the exact same memory (including using the same access size), or both be reads.

Each atomic access takes an [`Ordering`](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering") which defines how the operation interacts with the happens-before order. These orderings behave the same as the corresponding [C++20 atomic orderings](https://en.cppreference.com/w/cpp/atomic/memory_order). For more information, see the [nomicon](https://doc.rust-lang.org/nomicon/atomics.html).

```rust
use std::sync::atomic::{AtomicU16, AtomicU8, Ordering};
use std::mem::transmute;
use std::thread;

let atomic = AtomicU16::new(0);

thread::scope(|s| {
    // This is UB: conflicting non-synchronized accesses, at least one of which is non-atomic.
    s.spawn(|| atomic.store(1, Ordering::Relaxed)); // atomic store
    s.spawn(|| unsafe { atomic.as_ptr().write(2) }); // non-atomic write
});

thread::scope(|s| {
    // This is fine: the accesses do not conflict (as none of them performs any modification).
    // In C++ this would be disallowed since creating an `atomic_ref` precludes
    // further non-atomic accesses, but Rust does not have that limitation.
    s.spawn(|| atomic.load(Ordering::Relaxed)); // atomic load
    s.spawn(|| unsafe { atomic.as_ptr().read() }); // non-atomic read
});

thread::scope(|s| {
    // This is fine: `join` synchronizes the code in a way such that the atomic
    // store happens-before the non-atomic write.
    let handle = s.spawn(|| atomic.store(1, Ordering::Relaxed)); // atomic store
    handle.join().expect("thread won't panic"); // synchronize
    s.spawn(|| unsafe { atomic.as_ptr().write(2) }); // non-atomic write
});

thread::scope(|s| {
    // This is UB: non-synchronized conflicting differently-sized atomic accesses.
    s.spawn(|| atomic.store(1, Ordering::Relaxed));
    s.spawn(|| unsafe {
        let differently_sized = transmute::<&AtomicU16, &AtomicU8>(&atomic);
        differently_sized.store(2, Ordering::Relaxed);
    });
});

thread::scope(|s| {
    // This is fine: `join` synchronizes the code in a way such that
    // the 1-byte store happens-before the 2-byte store.
    let handle = s.spawn(|| atomic.store(1, Ordering::Relaxed));
    handle.join().expect("thread won't panic");
    s.spawn(|| unsafe {
        let differently_sized = transmute::<&AtomicU16, &AtomicU8>(&atomic);
        differently_sized.store(2, Ordering::Relaxed);
    });
});
```

## [§](#portability)Portability

All atomic types in this module are guaranteed to be [lock-free](https://en.wikipedia.org/wiki/Non-blocking_algorithm) if they’re available. This means they don’t internally acquire a global mutex. Atomic types and operations are not guaranteed to be wait-free. This means that operations like `fetch_or` may be implemented with a compare-and-swap loop.

Atomic operations may be implemented at the instruction layer with larger-size atomics. For example some platforms use 4-byte atomic instructions to implement `AtomicI8`. Note that this emulation should not have an impact on correctness of code, it’s just something to be aware of.

The atomic types in this module might not be available on all platforms. The atomic types here are all widely available, however, and can generally be relied upon existing. Some notable exceptions are:

- PowerPC and MIPS platforms with 32-bit pointers do not have `AtomicU64` or `AtomicI64` types.
- Legacy ARM platforms like ARMv4T and ARMv5TE have very limited hardware support for atomics. The bare-metal targets disable this module entirely, but the Linux targets [use the kernel](https://www.kernel.org/doc/Documentation/arm/kernel_user_helpers.txt) to assist (which comes with a performance penalty). It’s not until ARMv6K onwards that ARM CPUs have support for load/store and Compare and Swap (CAS) atomics in hardware.
- ARMv6-M and ARMv8-M baseline targets (`thumbv6m-*` and `thumbv8m.base-*`) only provide `load` and `store` operations, and do not support Compare and Swap (CAS) operations, such as `swap`, `fetch_add`, etc. Full CAS support is available on ARMv7-M and ARMv8-M Mainline (`thumbv7m-*`, `thumbv7em*` and `thumbv8m.main-*`).

Note that future platforms may be added that also do not have support for some atomic operations. Maximally portable code will want to be careful about which atomic types are used. `AtomicUsize` and `AtomicIsize` are generally the most portable, but even then they’re not available everywhere. For reference, the `std` library requires `AtomicBool`s and pointer-sized atomics, although `core` does not.

The `#[cfg(target_has_atomic)]` attribute can be used to conditionally compile based on the target’s supported bit widths. It is a key-value option set for each supported size, with values “8”, “16”, “32”, “64”, “128”, and “ptr” for pointer-sized atomics.

## [§](#atomic-accesses-to-read-only-memory)Atomic accesses to read-only memory

In general, *all* atomic accesses on read-only memory are undefined behavior. For instance, attempting to do a `compare_exchange` that will definitely fail (making it conceptually a read-only operation) can still cause a segmentation fault if the underlying memory page is mapped read-only. Since atomic `load`s might be implemented using compare-exchange operations, even a `load` can fault on read-only memory.

For the purpose of this section, “read-only memory” is defined as memory that is read-only in the underlying target, i.e., the pages are mapped with a read-only flag and any attempt to write will cause a page fault. In particular, an `&u128` reference that points to memory that is read-write mapped is *not* considered to point to “read-only memory”. In Rust, almost all memory is read-write; the only exceptions are memory created by `const` items or `static` items without interior mutability, and memory that was specifically marked as read-only by the operating system via platform-specific APIs.

As an exception from the general rule stated above, “sufficiently small” atomic loads with `Ordering::Relaxed` are implemented in a way that works on read-only memory, and are hence not undefined behavior. The exact size limit for what makes a load “sufficiently small” varies depending on the target:

`target_arch`Size limit `x86`, `arm`, `loongarch32`, `mips`, `mips32r6`, `powerpc`, `riscv32`, `sparc`, `hexagon`4 bytes `x86_64`, `aarch64`, `loongarch64`, `mips64`, `mips64r6`, `powerpc64`, `riscv64`, `sparc64`, `s390x`8 bytes

Atomics loads that are larger than this limit as well as atomic loads with ordering other than `Relaxed`, as well as *all* atomic loads on targets not listed in the table, might still be read-only under certain conditions, but that is not a stable guarantee and should not be relied upon.

If you need to do an acquire load on read-only memory, you can do a relaxed load followed by an acquire fence instead.

## [§](#examples)Examples

A simple spinlock:

[ⓘ](# "This example is not tested on wasm")

```rust
use std::sync::Arc;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::{hint, thread};

fn main() {
    let spinlock = Arc::new(AtomicUsize::new(1));

    let spinlock_clone = Arc::clone(&spinlock);

    let thread = thread::spawn(move || {
        spinlock_clone.store(0, Ordering::Release);
    });

    // Wait for the other thread to release the lock
    while spinlock.load(Ordering::Acquire) != 0 {
        hint::spin_loop();
    }

    if let Err(panic) = thread.join() {
        println!("Thread had an error: {panic:?}");
    }
}
```

Keep a global count of live threads:

```rust
use std::sync::atomic::{AtomicUsize, Ordering};

static GLOBAL_THREAD_COUNT: AtomicUsize = AtomicUsize::new(0);

// Note that Relaxed ordering doesn't synchronize anything
// except the global thread counter itself.
let old_thread_count = GLOBAL_THREAD_COUNT.fetch_add(1, Ordering::Relaxed);
// Note that this number may not be true at the moment of printing
// because some other thread may have changed static value already.
println!("live threads: {}", old_thread_count + 1);
```

[AtomicBool](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html "struct std::sync::atomic::AtomicBool")`target_has_atomic_load_store=8`

A boolean type which can be safely shared between threads.

[AtomicI8](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI8.html "struct std::sync::atomic::AtomicI8")

An integer type which can be safely shared between threads.

[AtomicI16](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI16.html "struct std::sync::atomic::AtomicI16")

An integer type which can be safely shared between threads.

[AtomicI32](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI32.html "struct std::sync::atomic::AtomicI32")

An integer type which can be safely shared between threads.

[AtomicI64](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI64.html "struct std::sync::atomic::AtomicI64")

An integer type which can be safely shared between threads.

[AtomicIsize](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicIsize.html "struct std::sync::atomic::AtomicIsize")

An integer type which can be safely shared between threads.

[AtomicPtr](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicPtr.html "struct std::sync::atomic::AtomicPtr")`target_has_atomic_load_store=ptr`

A raw pointer type which can be safely shared between threads.

[AtomicU8](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU8.html "struct std::sync::atomic::AtomicU8")

An integer type which can be safely shared between threads.

[AtomicU16](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU16.html "struct std::sync::atomic::AtomicU16")

An integer type which can be safely shared between threads.

[AtomicU32](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU32.html "struct std::sync::atomic::AtomicU32")

An integer type which can be safely shared between threads.

[AtomicU64](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU64.html "struct std::sync::atomic::AtomicU64")

An integer type which can be safely shared between threads.

[AtomicUsize](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html "struct std::sync::atomic::AtomicUsize")

An integer type which can be safely shared between threads.

[Ordering](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering")

Atomic memory orderings

[ATOMIC\_BOOL\_INIT](https://doc.rust-lang.org/std/sync/atomic/constant.ATOMIC_BOOL_INIT.html "constant std::sync::atomic::ATOMIC_BOOL_INIT")Deprecated`target_has_atomic_load_store=8`

An [`AtomicBool`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html "struct std::sync::atomic::AtomicBool") initialized to `false`.

[ATOMIC\_ISIZE\_INIT](https://doc.rust-lang.org/std/sync/atomic/constant.ATOMIC_ISIZE_INIT.html "constant std::sync::atomic::ATOMIC_ISIZE_INIT")Deprecated64-bit

An [`AtomicIsize`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicIsize.html "struct std::sync::atomic::AtomicIsize") initialized to `0`.

[ATOMIC\_USIZE\_INIT](https://doc.rust-lang.org/std/sync/atomic/constant.ATOMIC_USIZE_INIT.html "constant std::sync::atomic::ATOMIC_USIZE_INIT")Deprecated64-bit

An [`AtomicUsize`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html "struct std::sync::atomic::AtomicUsize") initialized to `0`.

[AtomicPrimitive](https://doc.rust-lang.org/std/sync/atomic/trait.AtomicPrimitive.html "trait std::sync::atomic::AtomicPrimitive")Experimental

A marker trait for primitive types which can be modified atomically.

[compiler\_fence](https://doc.rust-lang.org/std/sync/atomic/fn.compiler_fence.html "fn std::sync::atomic::compiler_fence")

A “compiler-only” atomic fence.

[fence](https://doc.rust-lang.org/std/sync/atomic/fn.fence.html "fn std::sync::atomic::fence")

An atomic fence.

[spin\_loop\_hint](https://doc.rust-lang.org/std/sync/atomic/fn.spin_loop_hint.html "fn std::sync::atomic::spin_loop_hint")Deprecated

Signals the processor that it is inside a busy-wait spin-loop (“spin lock”).

[Atomic](https://doc.rust-lang.org/std/sync/atomic/type.Atomic.html "type std::sync::atomic::Atomic")Experimental

A memory location which can be safely modified from multiple threads.