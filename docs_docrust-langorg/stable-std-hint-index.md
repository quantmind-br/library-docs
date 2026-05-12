---
title: std::hint - Rust
url: https://doc.rust-lang.org/stable/std/hint/index.html
source: crawler
fetched_at: 2026-05-06T21:28:24.311122793-03:00
rendered_js: false
word_count: 311
summary: This document provides a reference for the Rust standard library 'hint' module, which contains functions used to provide optimization and execution hints to the compiler and CPU.
tags:
    - rust-programming
    - compiler-hints
    - optimization
    - performance-tuning
    - low-level-programming
category: reference
---

## Module hint

1.27.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#260)

Expand description

Hints to compiler that affects how code should be emitted or optimized.

Hints may be compile time or runtime.

[Locality](https://doc.rust-lang.org/stable/std/hint/enum.Locality.html "enum std::hint::Locality")Experimental

The expected temporal locality of a memory prefetch operation.

[assert\_unchecked](https://doc.rust-lang.org/stable/std/hint/fn.assert_unchecked.html "fn std::hint::assert_unchecked")⚠

Makes a *soundness* promise to the compiler that `cond` holds.

[black\_box](https://doc.rust-lang.org/stable/std/hint/fn.black_box.html "fn std::hint::black_box")

An identity function that ***hints*** to the compiler to be maximally pessimistic about what `black_box` could do.

[cold\_path](https://doc.rust-lang.org/stable/std/hint/fn.cold_path.html "fn std::hint::cold_path")

Hints to the compiler that given path is cold, i.e., unlikely to be taken. The compiler may choose to optimize paths that are not cold at the expense of paths that are cold.

[select\_unpredictable](https://doc.rust-lang.org/stable/std/hint/fn.select_unpredictable.html "fn std::hint::select_unpredictable")

Returns either `true_val` or `false_val` depending on the value of `condition`, with a hint to the compiler that `condition` is unlikely to be correctly predicted by a CPU’s branch predictor.

[spin\_loop](https://doc.rust-lang.org/stable/std/hint/fn.spin_loop.html "fn std::hint::spin_loop")

Emits a machine instruction to signal the processor that it is running in a busy-wait spin-loop (“spin lock”).

[unreachable\_unchecked](https://doc.rust-lang.org/stable/std/hint/fn.unreachable_unchecked.html "fn std::hint::unreachable_unchecked")⚠

Informs the compiler that the site which is calling this function is not reachable, possibly enabling further optimizations.

[likely](https://doc.rust-lang.org/stable/std/hint/fn.likely.html "fn std::hint::likely")Experimental

Hints to the compiler that a branch condition is likely to be true. Returns the value passed to it.

[must\_use](https://doc.rust-lang.org/stable/std/hint/fn.must_use.html "fn std::hint::must_use")Experimental

An identity function that causes an `unused_must_use` warning to be triggered if the given value is not used (returned, stored in a variable, etc) by the caller.

[prefetch\_read](https://doc.rust-lang.org/stable/std/hint/fn.prefetch_read.html "fn std::hint::prefetch_read")Experimental

Prefetch the cache line containing `ptr` for a future read.

[prefetch\_read\_instruction](https://doc.rust-lang.org/stable/std/hint/fn.prefetch_read_instruction.html "fn std::hint::prefetch_read_instruction")Experimental

Prefetch the cache line containing `ptr` into the instruction cache for a future read.

[prefetch\_read\_non\_temporal](https://doc.rust-lang.org/stable/std/hint/fn.prefetch_read_non_temporal.html "fn std::hint::prefetch_read_non_temporal")Experimental

Prefetch the cache line containing `ptr` for a single future read, but attempt to avoid polluting the cache.

[prefetch\_write](https://doc.rust-lang.org/stable/std/hint/fn.prefetch_write.html "fn std::hint::prefetch_write")Experimental

Prefetch the cache line containing `ptr` for a future write.

[prefetch\_write\_non\_temporal](https://doc.rust-lang.org/stable/std/hint/fn.prefetch_write_non_temporal.html "fn std::hint::prefetch_write_non_temporal")Experimental

Prefetch the cache line containing `ptr` for a single future write, but attempt to avoid polluting the cache.

[unlikely](https://doc.rust-lang.org/stable/std/hint/fn.unlikely.html "fn std::hint::unlikely")Experimental

Hints to the compiler that a branch condition is unlikely to be true. Returns the value passed to it.