---
title: std::array - Rust
url: https://doc.rust-lang.org/stable/std/array/index.html
source: crawler
fetched_at: 2026-05-06T21:28:21.691849375-03:00
rendered_js: false
word_count: 136
summary: This document provides a technical reference for the Rust standard library array module, outlining available types, functions, and error handling mechanisms for working with fixed-size arrays.
tags:
    - rust-programming
    - array-module
    - standard-library
    - iterator
    - memory-reference
    - type-conversion
category: reference
---

## Module array

1.35.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#284)

Expand description

[IntoIter](https://doc.rust-lang.org/stable/std/array/struct.IntoIter.html "struct std::array::IntoIter")

A by-value [array](https://doc.rust-lang.org/stable/std/primitive.array.html "primitive array") iterator.

[TryFromSliceError](https://doc.rust-lang.org/stable/std/array/struct.TryFromSliceError.html "struct std::array::TryFromSliceError")

The error type returned when a conversion from a slice to an array fails.

[from\_fn](https://doc.rust-lang.org/stable/std/array/fn.from_fn.html "fn std::array::from_fn")

Creates an array where each element is produced by calling `f` with that element’s index while walking forward through the array.

[from\_mut](https://doc.rust-lang.org/stable/std/array/fn.from_mut.html "fn std::array::from_mut")

Converts a mutable reference to `T` into a mutable reference to an array of length 1 (without copying).

[from\_ref](https://doc.rust-lang.org/stable/std/array/fn.from_ref.html "fn std::array::from_ref")

Converts a reference to `T` into a reference to an array of length 1 (without copying).

[repeat](https://doc.rust-lang.org/stable/std/array/fn.repeat.html "fn std::array::repeat")

Creates an array of type `[T; N]` by repeatedly cloning a value.

[try\_from\_fn](https://doc.rust-lang.org/stable/std/array/fn.try_from_fn.html "fn std::array::try_from_fn")Experimental

Creates an array `[T; N]` where each fallible array element `T` is returned by the `cb` call. Unlike [`from_fn`](https://doc.rust-lang.org/stable/std/array/fn.from_fn.html "fn std::array::from_fn"), where the element creation can’t fail, this version will return an error if any element creation was unsuccessful.