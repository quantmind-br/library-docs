---
title: std::mem - Rust
url: https://doc.rust-lang.org/stable/std/mem/index.html
source: crawler
fetched_at: 2026-05-06T21:25:27.116325633-03:00
rendered_js: false
word_count: 404
summary: This module provides essential functions and types for managing memory, querying type layout information, and performing low-level memory manipulations in Rust.
tags:
    - rust
    - memory-management
    - type-layout
    - unsafe-code
    - system-programming
category: reference
---

## Module mem

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#262)

Expand description

Basic functions for dealing with memory.

This module contains functions for querying the size and alignment of types, initializing and manipulating memory.

[type\_info](https://doc.rust-lang.org/stable/std/mem/type_info/index.html "mod std::mem::type_info")Experimental

MVP for exposing compile-time information about types in a runtime or const-eval processable way.

[offset\_of](https://doc.rust-lang.org/stable/std/mem/macro.offset_of.html "macro std::mem::offset_of")

Expands to the offset in bytes of a field from the beginning of the given type.

[Discriminant](https://doc.rust-lang.org/stable/std/mem/struct.Discriminant.html "struct std::mem::Discriminant")

Opaque type representing the discriminant of an enum.

[ManuallyDrop](https://doc.rust-lang.org/stable/std/mem/struct.ManuallyDrop.html "struct std::mem::ManuallyDrop")

A wrapper to inhibit the compiler from automatically calling `T`’s destructor. This wrapper is 0-cost.

[Assume](https://doc.rust-lang.org/stable/std/mem/struct.Assume.html "struct std::mem::Assume")Experimental

Configurable proof assumptions of [`TransmuteFrom`](https://doc.rust-lang.org/stable/std/mem/trait.TransmuteFrom.html "trait std::mem::TransmuteFrom").

[DropGuard](https://doc.rust-lang.org/stable/std/mem/struct.DropGuard.html "struct std::mem::DropGuard")Experimental

Wrap a value and run a closure when dropped.

[MaybeDangling](https://doc.rust-lang.org/stable/std/mem/struct.MaybeDangling.html "struct std::mem::MaybeDangling")Experimental

Allows wrapped [references](https://doc.rust-lang.org/stable/std/primitive.reference.html "primitive reference") and [boxes](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html) to dangle.

[TransmuteFrom](https://doc.rust-lang.org/stable/std/mem/trait.TransmuteFrom.html "trait std::mem::TransmuteFrom")Experimental

Marks that `Src` is transmutable into `Self`.

[align\_of](https://doc.rust-lang.org/stable/std/mem/fn.align_of.html "fn std::mem::align_of")

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of a type in bytes.

[align\_of\_val](https://doc.rust-lang.org/stable/std/mem/fn.align_of_val.html "fn std::mem::align_of_val")

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of the type of the value that `val` points to in bytes.

[discriminant](https://doc.rust-lang.org/stable/std/mem/fn.discriminant.html "fn std::mem::discriminant")

Returns a value uniquely identifying the enum variant in `v`.

[drop](https://doc.rust-lang.org/stable/std/mem/fn.drop.html "fn std::mem::drop")

Disposes of a value.

[forget](https://doc.rust-lang.org/stable/std/mem/fn.forget.html "fn std::mem::forget")

Takes ownership and “forgets” about the value **without running its destructor**.

[min\_align\_of](https://doc.rust-lang.org/stable/std/mem/fn.min_align_of.html "fn std::mem::min_align_of")Deprecated

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of a type in bytes.

[min\_align\_of\_val](https://doc.rust-lang.org/stable/std/mem/fn.min_align_of_val.html "fn std::mem::min_align_of_val")Deprecated

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of the type of the value that `val` points to in bytes.

[needs\_drop](https://doc.rust-lang.org/stable/std/mem/fn.needs_drop.html "fn std::mem::needs_drop")

Returns `true` if dropping values of type `T` matters.

[replace](https://doc.rust-lang.org/stable/std/mem/fn.replace.html "fn std::mem::replace")

Moves `src` into the referenced `dest`, returning the previous `dest` value.

[size\_of](https://doc.rust-lang.org/stable/std/mem/fn.size_of.html "fn std::mem::size_of")

Returns the size of a type in bytes.

[size\_of\_val](https://doc.rust-lang.org/stable/std/mem/fn.size_of_val.html "fn std::mem::size_of_val")

Returns the size of the pointed-to value in bytes.

[swap](https://doc.rust-lang.org/stable/std/mem/fn.swap.html "fn std::mem::swap")

Swaps the values at two mutable locations, without deinitializing either one.

[take](https://doc.rust-lang.org/stable/std/mem/fn.take.html "fn std::mem::take")

Replaces `dest` with the default value of `T`, returning the previous `dest` value.

[transmute](https://doc.rust-lang.org/stable/std/mem/fn.transmute.html "fn std::mem::transmute")⚠

Reinterprets the bits of a value of one type as another type.

[transmute\_copy](https://doc.rust-lang.org/stable/std/mem/fn.transmute_copy.html "fn std::mem::transmute_copy")⚠

Interprets `src` as having type `&Dst`, and then reads `src` without moving the contained value.

[uninitialized](https://doc.rust-lang.org/stable/std/mem/fn.uninitialized.html "fn std::mem::uninitialized")⚠Deprecated

Bypasses Rust’s normal memory-initialization checks by pretending to produce a value of type `T`, while doing nothing at all.

[zeroed](https://doc.rust-lang.org/stable/std/mem/fn.zeroed.html "fn std::mem::zeroed")⚠

Returns the value of type `T` represented by the all-zero byte-pattern.

[align\_of\_val\_raw](https://doc.rust-lang.org/stable/std/mem/fn.align_of_val_raw.html "fn std::mem::align_of_val_raw")⚠Experimental

Returns the [ABI](https://en.wikipedia.org/wiki/Application_binary_interface)-required minimum alignment of the type of the value that `val` points to in bytes.

[conjure\_zst](https://doc.rust-lang.org/stable/std/mem/fn.conjure_zst.html "fn std::mem::conjure_zst")⚠Experimental

Create a fresh instance of the inhabited ZST type `T`.

[copy](https://doc.rust-lang.org/stable/std/mem/fn.copy.html "fn std::mem::copy")Experimental

Bitwise-copies a value.

[forget\_unsized](https://doc.rust-lang.org/stable/std/mem/fn.forget_unsized.html "fn std::mem::forget_unsized")Experimental

Like [`forget`](https://doc.rust-lang.org/stable/std/mem/fn.forget.html "fn std::mem::forget"), but also accepts unsized values.

[size\_of\_val\_raw](https://doc.rust-lang.org/stable/std/mem/fn.size_of_val_raw.html "fn std::mem::size_of_val_raw")⚠Experimental

Returns the size of the pointed-to value in bytes.

[variant\_count](https://doc.rust-lang.org/stable/std/mem/fn.variant_count.html "fn std::mem::variant_count")Experimental

Returns the number of variants in the enum type `T`.

[MaybeUninit](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit")

A wrapper type to construct uninitialized instances of `T`.