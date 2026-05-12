---
title: slice - Rust
url: https://doc.rust-lang.org/std/primitive.slice.html
source: crawler
fetched_at: 2026-05-06T21:22:11.778464054-03:00
rendered_js: false
word_count: 21284
summary: This document describes the primitive slice type in Rust, which serves as a dynamically-sized view into a contiguous sequence of elements in memory.
tags:
    - rust
    - primitive-types
    - slices
    - memory-layout
    - data-structures
    - iterators
category: reference
---

## Primitive Type slice

1.0.0

Expand description

A dynamically-sized view into a contiguous sequence, `[T]`.

Contiguous here means that elements are laid out so that every element is the same distance from its neighbors.

*[See also the `std::slice` module](https://doc.rust-lang.org/std/slice/index.html "mod std::slice").*

Slices are a view into a block of memory represented as a pointer and a length.

```rust
// slicing a Vec
let vec = vec![1, 2, 3];
let int_slice = &vec[..];
// coercing an array to a slice
let str_slice: &[&str] = &["one", "two", "three"];
```

Slices are either mutable or shared. The shared slice type is `&[T]`, while the mutable slice type is `&mut [T]`, where `T` represents the element type. For example, you can mutate the block of memory that a mutable slice points to:

```rust
let mut x = [1, 2, 3];
let x = &mut x[..]; // Take a full slice of `x`.
x[1] = 7;
assert_eq!(x, &[1, 7, 3]);
```

It is possible to slice empty subranges of slices by using empty ranges (including `slice.len()..slice.len()`):

```rust
let x = [1, 2, 3];
let empty = &x[0..0];   // subslice before the first element
assert_eq!(empty, &[]);
let empty = &x[..0];    // same as &x[0..0]
assert_eq!(empty, &[]);
let empty = &x[1..1];   // empty subslice in the middle
assert_eq!(empty, &[]);
let empty = &x[3..3];   // subslice after the last element
assert_eq!(empty, &[]);
let empty = &x[3..];    // same as &x[3..3]
assert_eq!(empty, &[]);
```

It is not allowed to use subranges that start with lower bound bigger than `slice.len()`:

[ⓘ](# "This example panics")

```rust
let x = vec![1, 2, 3];
let _ = &x[4..4];
```

As slices store the length of the sequence they refer to, they have twice the size of pointers to [`Sized`](https://doc.rust-lang.org/std/marker/trait.Sized.html) types. Also see the reference on [dynamically sized types](https://doc.rust-lang.org/reference/dynamically-sized-types.html).

```rust
let pointer_size = size_of::<&u8>();
assert_eq!(2 * pointer_size, size_of::<&[u8]>());
assert_eq!(2 * pointer_size, size_of::<*const [u8]>());
assert_eq!(2 * pointer_size, size_of::<Box<[u8]>>());
assert_eq!(2 * pointer_size, size_of::<Rc<[u8]>>());
```

### [§](#trait-implementations-1)Trait Implementations

Some traits are implemented for slices if the element type implements that trait. This includes [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq"), [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") and [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord").

### [§](#iteration)Iteration

The slices implement `IntoIterator`. The iterator yields references to the slice elements.

```rust
let numbers: &[i32] = &[0, 1, 2];
for n in numbers {
    println!("{n} is a number!");
}
```

The mutable slice yields mutable references to the elements:

```rust
let mut scores: &mut [i32] = &mut [7, 8, 9];
for score in scores {
    *score += 1;
}
```

This iterator yields mutable references to the slice’s elements, so while the element type of the slice is `i32`, the element type of the iterator is `&mut i32`.

- [`.iter`](https://doc.rust-lang.org/std/primitive.slice.html#method.iter "method slice::iter") and [`.iter_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.iter_mut "method slice::iter_mut") are the explicit methods to return the default iterators.
- Further methods that return iterators are [`.split`](https://doc.rust-lang.org/std/primitive.slice.html#method.split "method slice::split"), [`.splitn`](https://doc.rust-lang.org/std/primitive.slice.html#method.splitn "method slice::splitn"), [`.chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks "method slice::chunks"), [`.windows`](https://doc.rust-lang.org/std/primitive.slice.html#method.windows "method slice::windows") and more.

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#889)[§](#impl-Box%3C%5BT%5D%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#907)

Constructs a new boxed slice with uninitialized contents.

##### [§](#examples)Examples

```rust
let mut values = Box::<[u32]>::new_uninit_slice(3);
// Deferred initialization:
values[0].write(1);
values[1].write(2);
values[2].write(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

1.92.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#930)

Constructs a new boxed slice with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-1)Examples

```rust
let values = Box::<[u32]>::new_zeroed_slice(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#954)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents. Returns an error if the allocation fails.

##### [§](#examples-2)Examples

```rust
#![feature(allocator_api)]

let mut values = Box::<[u32]>::try_new_uninit_slice(3)?;
// Deferred initialization:
values[0].write(1);
values[1].write(2);
values[2].write(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3]);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#988)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents, with the memory being filled with `0` bytes. Returns an error if the allocation fails.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-3)Examples

```rust
#![feature(allocator_api)]

let values = Box::<[u32]>::try_new_zeroed_slice(3)?;
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0]);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1009)

🔬This is a nightly-only experimental API. (`alloc_slice_into_array` [#148082](https://github.com/rust-lang/rust/issues/148082))

Converts the boxed slice into a boxed array.

This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1022)[§](#impl-Box%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1044)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents in the provided allocator.

##### [§](#examples-4)Examples

```rust
#![feature(allocator_api)]

use std::alloc::System;

let mut values = Box::<[u32], _>::new_uninit_slice_in(3, System);
// Deferred initialization:
values[0].write(1);
values[1].write(2);
values[2].write(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1071)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents in the provided allocator, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-5)Examples

```rust
#![feature(allocator_api)]

use std::alloc::System;

let values = Box::<[u32], _>::new_zeroed_slice_in(3, System);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1097-1100)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents in the provided allocator. Returns an error if the allocation fails.

##### [§](#examples-6)Examples

```rust
#![feature(allocator_api)]

use std::alloc::System;

let mut values = Box::<[u32], _>::try_new_uninit_slice_in(3, System)?;
// Deferred initialization:
values[0].write(1);
values[1].write(2);
values[2].write(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3]);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1136-1139)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new boxed slice with uninitialized contents in the provided allocator, with the memory being filled with `0` bytes. Returns an error if the allocation fails.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-7)Examples

```rust
#![feature(allocator_api)]

use std::alloc::System;

let values = Box::<[u32], _>::try_new_zeroed_slice_in(3, System)?;
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0]);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1220)[§](#impl-Box%3C%5BMaybeUninit%3CT%3E%5D,+A%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1247)

Converts to `Box<[T], A>`.

##### [§](#safety)Safety

As with [`MaybeUninit::assume_init`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.assume_init "method std::mem::MaybeUninit::assume_init"), it is up to the caller to guarantee that the values really are in an initialized state. Calling this when the content is not yet fully initialized causes immediate undefined behavior.

##### [§](#examples-8)Examples

```rust
let mut values = Box::<[u32]>::new_uninit_slice(3);
// Deferred initialization:
values[0].write(1);
values[1].write(2);
values[2].write(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1101)[§](#impl-%5BMaybeUninit%3CT%3E%5D)

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1144-1146)

Copies the elements from `src` to `self`, returning a mutable reference to the now initialized contents of `self`.

If `T` does not implement `Copy`, use [`write_clone_of_slice`](https://doc.rust-lang.org/std/primitive.slice.html#method.write_clone_of_slice "method slice::write_clone_of_slice") instead.

This is similar to [`slice::copy_from_slice`](https://doc.rust-lang.org/std/primitive.slice.html#method.copy_from_slice "method slice::copy_from_slice").

##### [§](#panics)Panics

This function will panic if the two slices have different lengths.

##### [§](#examples-9)Examples

```rust
use std::mem::MaybeUninit;

let mut dst = [MaybeUninit::uninit(); 32];
let src = [0; 32];

let init = dst.write_copy_of_slice(&src);

assert_eq!(init, src);
```

```rust
let mut vec = Vec::with_capacity(32);
let src = [0; 16];

vec.spare_capacity_mut()[..src.len()].write_copy_of_slice(&src);

// SAFETY: we have just copied all the elements of len into the spare capacity
// the first src.len() elements of the vec are valid now.
unsafe {
    vec.set_len(src.len());
}

assert_eq!(vec, src);
```

1.93.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1204-1206)

Clones the elements from `src` to `self`, returning a mutable reference to the now initialized contents of `self`. Any already initialized elements will not be dropped.

If `T` implements `Copy`, use [`write_copy_of_slice`](https://doc.rust-lang.org/std/primitive.slice.html#method.write_copy_of_slice "method slice::write_copy_of_slice") instead.

This is similar to [`slice::clone_from_slice`](https://doc.rust-lang.org/std/primitive.slice.html#method.clone_from_slice "method slice::clone_from_slice") but does not drop existing elements.

##### [§](#panics-1)Panics

This function will panic if the two slices have different lengths, or if the implementation of `Clone` panics.

If there is a panic, the already cloned elements will be dropped.

##### [§](#examples-10)Examples

```rust
use std::mem::MaybeUninit;

let mut dst = [const { MaybeUninit::uninit() }; 5];
let src = ["wibbly", "wobbly", "timey", "wimey", "stuff"].map(|s| s.to_string());

let init = dst.write_clone_of_slice(&src);

assert_eq!(init, src);
```

```rust
let mut vec = Vec::with_capacity(32);
let src = ["rust", "is", "a", "pretty", "cool", "language"].map(|s| s.to_string());

vec.spare_capacity_mut()[..src.len()].write_clone_of_slice(&src);

// SAFETY: we have just cloned all the elements of len into the spare capacity
// the first src.len() elements of the vec are valid now.
unsafe {
    vec.set_len(src.len());
}

assert_eq!(vec, src);
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1258-1260)

🔬This is a nightly-only experimental API. (`maybe_uninit_fill` [#117428](https://github.com/rust-lang/rust/issues/117428))

Fills a slice with elements by cloning `value`, returning a mutable reference to the now initialized contents of the slice. Any previously initialized elements will not be dropped.

This is similar to [`slice::fill`](https://doc.rust-lang.org/std/primitive.slice.html#method.fill "method slice::fill").

##### [§](#panics-2)Panics

This function will panic if any call to `Clone` panics.

If such a panic occurs, any elements previously initialized during this operation will be dropped.

##### [§](#examples-11)Examples

```rust
#![feature(maybe_uninit_fill)]
use std::mem::MaybeUninit;

let mut buf = [const { MaybeUninit::uninit() }; 10];
let initialized = buf.write_filled(1);
assert_eq!(initialized, &mut [1; 10]);
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1291-1293)

🔬This is a nightly-only experimental API. (`maybe_uninit_fill` [#117428](https://github.com/rust-lang/rust/issues/117428))

Fills a slice with elements returned by calling a closure for each index.

This method uses a closure to create new values. If you’d rather `Clone` a given value, use [slice::write\_filled](https://doc.rust-lang.org/std/primitive.slice.html#method.write_filled "method slice::write_filled"). If you want to use the `Default` trait to generate values, you can pass [`|_| Default::default()`](https://doc.rust-lang.org/std/default/trait.Default.html#tymethod.default "associated function std::default::Default::default") as the argument.

##### [§](#panics-3)Panics

This function will panic if any call to the provided closure panics.

If such a panic occurs, any elements previously initialized during this operation will be dropped.

##### [§](#examples-12)Examples

```rust
#![feature(maybe_uninit_fill)]
use std::mem::MaybeUninit;

let mut buf = [const { MaybeUninit::<usize>::uninit() }; 5];
let initialized = buf.write_with(|idx| idx + 1);
assert_eq!(initialized, &mut [1, 2, 3, 4, 5]);
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1367-1369)

🔬This is a nightly-only experimental API. (`maybe_uninit_fill` [#117428](https://github.com/rust-lang/rust/issues/117428))

Fills a slice with elements yielded by an iterator until either all elements have been initialized or the iterator is empty.

Returns two slices. The first slice contains the initialized portion of the original slice. The second slice is the still-uninitialized remainder of the original slice.

##### [§](#panics-4)Panics

This function panics if the iterator’s `next` function panics.

If such a panic occurs, any elements previously initialized during this operation will be dropped.

##### [§](#examples-13)Examples

Completely filling the slice:

```rust
#![feature(maybe_uninit_fill)]
use std::mem::MaybeUninit;

let mut buf = [const { MaybeUninit::uninit() }; 5];

let iter = [1, 2, 3].into_iter().cycle();
let (initialized, remainder) = buf.write_iter(iter);

assert_eq!(initialized, &mut [1, 2, 3, 1, 2]);
assert_eq!(remainder.len(), 0);
```

Partially filling the slice:

```rust
#![feature(maybe_uninit_fill)]
use std::mem::MaybeUninit;

let mut buf = [const { MaybeUninit::uninit() }; 5];
let iter = [1, 2];
let (initialized, remainder) = buf.write_iter(iter);

assert_eq!(initialized, &mut [1, 2]);
assert_eq!(remainder.len(), 3);
```

Checking an iterator after filling a slice:

```rust
#![feature(maybe_uninit_fill)]
use std::mem::MaybeUninit;

let mut buf = [const { MaybeUninit::uninit() }; 3];
let mut iter = [1, 2, 3, 4, 5].into_iter();
let (initialized, remainder) = buf.write_iter(iter.by_ref());

assert_eq!(initialized, &mut [1, 2, 3]);
assert_eq!(remainder.len(), 0);
assert_eq!(iter.as_slice(), &[4, 5]);
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1409)

🔬This is a nightly-only experimental API. (`maybe_uninit_as_bytes` [#93092](https://github.com/rust-lang/rust/issues/93092))

Returns the contents of this `MaybeUninit` as a slice of potentially uninitialized bytes.

Note that even if the contents of a `MaybeUninit` have been initialized, the value may still contain padding bytes which are left uninitialized.

##### [§](#examples-14)Examples

```rust
#![feature(maybe_uninit_as_bytes)]
use std::mem::MaybeUninit;

let uninit = [MaybeUninit::new(0x1234u16), MaybeUninit::new(0x5678u16)];
let uninit_bytes = uninit.as_bytes();
let bytes = unsafe { uninit_bytes.assume_init_ref() };
let val1 = u16::from_ne_bytes(bytes[0..2].try_into().unwrap());
let val2 = u16::from_ne_bytes(bytes[2..4].try_into().unwrap());
assert_eq!(&[val1, val2], &[0x1234u16, 0x5678u16]);
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1439)

🔬This is a nightly-only experimental API. (`maybe_uninit_as_bytes` [#93092](https://github.com/rust-lang/rust/issues/93092))

Returns the contents of this `MaybeUninit` slice as a mutable slice of potentially uninitialized bytes.

Note that even if the contents of a `MaybeUninit` have been initialized, the value may still contain padding bytes which are left uninitialized.

##### [§](#examples-15)Examples

```rust
#![feature(maybe_uninit_as_bytes)]
use std::mem::MaybeUninit;

let mut uninit = [MaybeUninit::<u16>::uninit(), MaybeUninit::<u16>::uninit()];
let uninit_bytes = uninit.as_bytes_mut();
uninit_bytes.write_copy_of_slice(&[0x12, 0x34, 0x56, 0x78]);
let vals = unsafe { uninit.assume_init_ref() };
if cfg!(target_endian = "little") {
    assert_eq!(vals, &[0x3412u16, 0x7856u16]);
} else {
    assert_eq!(vals, &[0x1234u16, 0x5678u16]);
}
```

1.93.0 (const: [unstable](https://github.com/rust-lang/rust/issues/109342 "Tracking issue for const_drop_in_place")) · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1468-1470)

Drops the contained values in place.

##### [§](#safety-1)Safety

It is up to the caller to guarantee that every `MaybeUninit<T>` in the slice really is in an initialized state. Calling this when the content is not yet fully initialized causes undefined behavior.

On top of that, all additional invariants of the type `T` must be satisfied, as the `Drop` implementation of `T` (or its members) may rely on this. For example, setting a `Vec<T>` to an invalid but non-null address makes it initialized (under the current implementation; this does not constitute a stable guarantee), because the only requirement the compiler knows about it is that the data pointer must be non-null. Dropping such a `Vec<T>` however will cause undefined behaviour.

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1490)

Gets a shared reference to the contained value.

##### [§](#safety-2)Safety

Calling this when the content is not yet fully initialized causes undefined behavior: it is up to the caller to guarantee that every `MaybeUninit<T>` in the slice really is in an initialized state.

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1509)

Gets a mutable (unique) reference to the contained value.

##### [§](#safety-3)Safety

Calling this when the content is not yet fully initialized causes undefined behavior: it is up to the caller to guarantee that every `MaybeUninit<T>` in the slice really is in an initialized state. For instance, `.assume_init_mut()` cannot be used to initialize a `MaybeUninit` slice.

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1173)[§](#impl-%5BChar%5D)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1177)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Views this slice of ASCII characters as a UTF-8 `str`.

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1188)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Views this slice of ASCII characters as a slice of `u8` bytes.

[Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#10)[§](#impl-%5Bu8%5D)

1.23.0 (const: 1.74.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#18)

Checks if all bytes in this slice are within the ASCII range.

An empty slice returns `true`.

[Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#27)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

[Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#45)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this slice of bytes into a slice of ASCII characters, without checking whether they’re valid.

##### [§](#safety-4)Safety

Every byte in the slice must be in `0..=127`, or else this is UB.

1.23.0 (const: 1.89.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#60)

Checks that two slices are an ASCII case-insensitive match.

Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`, but without allocating and copying temporaries.

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#173)

Converts this slice to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`to_ascii_uppercase`](#method.to_ascii_uppercase).

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#195)

Converts this slice to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`to_ascii_lowercase`](#method.to_ascii_lowercase).

1.60.0 · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#218)

Returns an iterator that produces an escaped version of this slice, treating it as an ASCII string.

##### [§](#examples-16)Examples

```rust
let s = b"0\t\r\n'\"\\\x9d";
let escaped = s.escape_ascii().to_string();
assert_eq!(escaped, "0\\t\\r\\n\\'\\\"\\\\\\x9d");
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#237)

Returns a byte slice with leading ASCII whitespace bytes removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-17)Examples

```rust
assert_eq!(b" \t hello world\n".trim_ascii_start(), b"hello world\n");
assert_eq!(b"  ".trim_ascii_start(), b"");
assert_eq!(b"".trim_ascii_start(), b"");
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#266)

Returns a byte slice with trailing ASCII whitespace bytes removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-18)Examples

```rust
assert_eq!(b"\r hello world\n ".trim_ascii_end(), b"\r hello world");
assert_eq!(b"  ".trim_ascii_end(), b"");
assert_eq!(b"".trim_ascii_end(), b"");
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/slice/ascii.rs.html#296)

Returns a byte slice with leading and trailing ASCII whitespace bytes removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-19)Examples

```rust
assert_eq!(b"\r hello world\n ".trim_ascii(), b"hello world");
assert_eq!(b"  ".trim_ascii(), b"");
assert_eq!(b"".trim_ascii(), b"");
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#101)[§](#impl-%5BT%5D)

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#116)

Returns the number of elements in the slice.

##### [§](#examples-20)Examples

```rust
let a = [1, 2, 3];
assert_eq!(a.len(), 3);
```

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#136)

Returns `true` if the slice has a length of 0.

##### [§](#examples-21)Examples

```rust
let a = [1, 2, 3];
assert!(!a.is_empty());

let b: &[i32] = &[];
assert!(b.is_empty());
```

1.0.0 (const: 1.56.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#155)

Returns the first element of the slice, or `None` if it is empty.

##### [§](#examples-22)Examples

```rust
let v = [10, 40, 30];
assert_eq!(Some(&10), v.first());

let w: &[i32] = &[];
assert_eq!(None, w.first());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#178)

Returns a mutable reference to the first element of the slice, or `None` if it is empty.

##### [§](#examples-23)Examples

```rust
let x = &mut [0, 1, 2];

if let Some(first) = x.first_mut() {
    *first = 5;
}
assert_eq!(x, &[5, 1, 2]);

let y: &mut [i32] = &mut [];
assert_eq!(None, y.first_mut());
```

1.5.0 (const: 1.56.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#198)

Returns the first and all the rest of the elements of the slice, or `None` if it is empty.

##### [§](#examples-24)Examples

```rust
let x = &[0, 1, 2];

if let Some((first, elements)) = x.split_first() {
    assert_eq!(first, &0);
    assert_eq!(elements, &[1, 2]);
}
```

1.5.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#220)

Returns the first and all the rest of the elements of the slice, or `None` if it is empty.

##### [§](#examples-25)Examples

```rust
let x = &mut [0, 1, 2];

if let Some((first, elements)) = x.split_first_mut() {
    *first = 3;
    elements[0] = 4;
    elements[1] = 5;
}
assert_eq!(x, &[3, 4, 5]);
```

1.5.0 (const: 1.56.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#240)

Returns the last and all the rest of the elements of the slice, or `None` if it is empty.

##### [§](#examples-26)Examples

```rust
let x = &[0, 1, 2];

if let Some((last, elements)) = x.split_last() {
    assert_eq!(last, &2);
    assert_eq!(elements, &[0, 1]);
}
```

1.5.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#262)

Returns the last and all the rest of the elements of the slice, or `None` if it is empty.

##### [§](#examples-27)Examples

```rust
let x = &mut [0, 1, 2];

if let Some((last, elements)) = x.split_last_mut() {
    *last = 3;
    elements[0] = 4;
    elements[1] = 5;
}
assert_eq!(x, &[4, 5, 3]);
```

1.0.0 (const: 1.56.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#281)

Returns the last element of the slice, or `None` if it is empty.

##### [§](#examples-28)Examples

```rust
let v = [10, 40, 30];
assert_eq!(Some(&30), v.last());

let w: &[i32] = &[];
assert_eq!(None, w.last());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#304)

Returns a mutable reference to the last item in the slice, or `None` if it is empty.

##### [§](#examples-29)Examples

```rust
let x = &mut [0, 1, 2];

if let Some(last) = x.last_mut() {
    *last = 10;
}
assert_eq!(x, &[0, 1, 10]);

let y: &mut [i32] = &mut [];
assert_eq!(None, y.last_mut());
```

1.77.0 (const: 1.77.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#327)

Returns an array reference to the first `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-30)Examples

```rust
let u = [10, 40, 30];
assert_eq!(Some(&[10, 40]), u.first_chunk::<2>());

let v: &[i32] = &[10];
assert_eq!(None, v.first_chunk::<2>());

let w: &[i32] = &[];
assert_eq!(Some(&[]), w.first_chunk::<0>());
```

1.77.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#357)

Returns a mutable array reference to the first `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-31)Examples

```rust
let x = &mut [0, 1, 2];

if let Some(first) = x.first_chunk_mut::<2>() {
    first[0] = 5;
    first[1] = 4;
}
assert_eq!(x, &[5, 4, 2]);

assert_eq!(None, x.first_chunk_mut::<4>());
```

1.77.0 (const: 1.77.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#387)

Returns an array reference to the first `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-32)Examples

```rust
let x = &[0, 1, 2];

if let Some((first, elements)) = x.split_first_chunk::<2>() {
    assert_eq!(first, &[0, 1]);
    assert_eq!(elements, &[2]);
}

assert_eq!(None, x.split_first_chunk::<4>());
```

1.77.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#417-419)

Returns a mutable array reference to the first `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-33)Examples

```rust
let x = &mut [0, 1, 2];

if let Some((first, elements)) = x.split_first_chunk_mut::<2>() {
    first[0] = 3;
    first[1] = 4;
    elements[0] = 5;
}
assert_eq!(x, &[3, 4, 5]);

assert_eq!(None, x.split_first_chunk_mut::<4>());
```

1.77.0 (const: 1.77.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#447)

Returns an array reference to the last `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-34)Examples

```rust
let x = &[0, 1, 2];

if let Some((elements, last)) = x.split_last_chunk::<2>() {
    assert_eq!(elements, &[0]);
    assert_eq!(last, &[1, 2]);
}

assert_eq!(None, x.split_last_chunk::<4>());
```

1.77.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#478-480)

Returns a mutable array reference to the last `N` items in the slice and the remaining slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-35)Examples

```rust
let x = &mut [0, 1, 2];

if let Some((elements, last)) = x.split_last_chunk_mut::<2>() {
    last[0] = 3;
    last[1] = 4;
    elements[0] = 5;
}
assert_eq!(x, &[5, 3, 4]);

assert_eq!(None, x.split_last_chunk_mut::<4>());
```

1.77.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#509)

Returns an array reference to the last `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-36)Examples

```rust
let u = [10, 40, 30];
assert_eq!(Some(&[40, 30]), u.last_chunk::<2>());

let v: &[i32] = &[10];
assert_eq!(None, v.last_chunk::<2>());

let w: &[i32] = &[];
assert_eq!(Some(&[]), w.last_chunk::<0>());
```

1.77.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#539)

Returns a mutable array reference to the last `N` items in the slice.

If the slice is not at least `N` in length, this will return `None`.

##### [§](#examples-37)Examples

```rust
let x = &mut [0, 1, 2];

if let Some(last) = x.last_chunk_mut::<2>() {
    last[0] = 10;
    last[1] = 20;
}
assert_eq!(x, &[0, 10, 20]);

assert_eq!(None, x.last_chunk_mut::<4>());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#572-574)

Returns a reference to an element or subslice depending on the type of index.

- If given a position, returns a reference to the element at that position or `None` if out of bounds.
- If given a range, returns the subslice corresponding to that range, or `None` if out of bounds.

##### [§](#examples-38)Examples

```rust
let v = [10, 40, 30];
assert_eq!(Some(&40), v.get(1));
assert_eq!(Some(&[10, 40][..]), v.get(0..2));
assert_eq!(None, v.get(3));
assert_eq!(None, v.get(0..4));
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#599-601)

Returns a mutable reference to an element or subslice depending on the type of index (see [`get`](https://doc.rust-lang.org/std/primitive.slice.html#method.get "method slice::get")) or `None` if the index is out of bounds.

##### [§](#examples-39)Examples

```rust
let x = &mut [0, 1, 2];

if let Some(elem) = x.get_mut(1) {
    *elem = 42;
}
assert_eq!(x, &[0, 42, 2]);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#639-641)

Returns a reference to an element or subslice, without doing bounds checking.

For a safe alternative see [`get`](https://doc.rust-lang.org/std/primitive.slice.html#method.get "method slice::get").

##### [§](#safety-5)Safety

Calling this method with an out-of-bounds index is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting reference is not used.

You can think of this like `.get(index).unwrap_unchecked()`. It’s UB to call `.get_unchecked(len)`, even if you immediately convert to a pointer. And it’s UB to call `.get_unchecked(..len + 1)`, `.get_unchecked(..=len)`, or similar.

##### [§](#examples-40)Examples

```rust
let x = &[1, 2, 4];

unsafe {
    assert_eq!(x.get_unchecked(1), &2);
}
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#684-686)

Returns a mutable reference to an element or subslice, without doing bounds checking.

For a safe alternative see [`get_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.get_mut "method slice::get_mut").

##### [§](#safety-6)Safety

Calling this method with an out-of-bounds index is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting reference is not used.

You can think of this like `.get_mut(index).unwrap_unchecked()`. It’s UB to call `.get_unchecked_mut(len)`, even if you immediately convert to a pointer. And it’s UB to call `.get_unchecked_mut(..len + 1)`, `.get_unchecked_mut(..=len)`, or similar.

##### [§](#examples-41)Examples

```rust
let x = &mut [1, 2, 4];

unsafe {
    let elem = x.get_unchecked_mut(1);
    *elem = 13;
}
assert_eq!(x, &[1, 13, 4]);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#726)

Returns a raw pointer to the slice’s buffer.

The caller must ensure that the slice outlives the pointer this function returns, or else it will end up dangling.

The caller must also ensure that the memory the pointer (non-transitively) points to is never written to (except inside an `UnsafeCell`) using this pointer or any pointer derived from it. If you need to mutate the contents of the slice, use [`as_mut_ptr`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_mut_ptr "method slice::as_mut_ptr").

Modifying the container referenced by this slice may cause its buffer to be reallocated, which would also make any pointers to it invalid.

##### [§](#examples-42)Examples

```rust
let x = &[1, 2, 4];
let x_ptr = x.as_ptr();

unsafe {
    for i in 0..x.len() {
        assert_eq!(x.get_unchecked(i), &*x_ptr.add(i));
    }
}
```

1.0.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#757)

Returns an unsafe mutable pointer to the slice’s buffer.

The caller must ensure that the slice outlives the pointer this function returns, or else it will end up dangling.

Modifying the container referenced by this slice may cause its buffer to be reallocated, which would also make any pointers to it invalid.

##### [§](#examples-43)Examples

```rust
let x = &mut [1, 2, 4];
let x_ptr = x.as_mut_ptr();

unsafe {
    for i in 0..x.len() {
        *x_ptr.add(i) += 2;
    }
}
assert_eq!(x, &[3, 4, 6]);
```

1.48.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#793)

Returns the two raw pointers spanning the slice.

The returned range is half-open, which means that the end pointer points *one past* the last element of the slice. This way, an empty slice is represented by two equal pointers, and the difference between the two pointers represents the size of the slice.

See [`as_ptr`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_ptr "method slice::as_ptr") for warnings on using these pointers. The end pointer requires extra caution, as it does not point to a valid element in the slice.

This function is useful for interacting with foreign interfaces which use two pointers to refer to a range of elements in memory, as is common in C++.

It can also be useful to check if a pointer to an element refers to an element of this slice:

```rust
let a = [1, 2, 3];
let x = &a[1] as *const _;
let y = &5 as *const _;

assert!(a.as_ptr_range().contains(&x));
assert!(!a.as_ptr_range().contains(&y));
```

1.48.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#836)

Returns the two unsafe mutable pointers spanning the slice.

The returned range is half-open, which means that the end pointer points *one past* the last element of the slice. This way, an empty slice is represented by two equal pointers, and the difference between the two pointers represents the size of the slice.

See [`as_mut_ptr`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_mut_ptr "method slice::as_mut_ptr") for warnings on using these pointers. The end pointer requires extra caution, as it does not point to a valid element in the slice.

This function is useful for interacting with foreign interfaces which use two pointers to refer to a range of elements in memory, as is common in C++.

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#850)

Gets a reference to the underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#869)

Gets a mutable reference to the slice’s underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#905)

Swaps two elements in the slice.

If `a` equals to `b`, it’s guaranteed that elements won’t change value.

##### [§](#arguments)Arguments

- a - The index of the first element
- b - The index of the second element

##### [§](#panics-5)Panics

Panics if `a` or `b` are out of bounds.

##### [§](#examples-44)Examples

```rust
let mut v = ["a", "b", "c", "d", "e"];
v.swap(2, 4);
assert!(v == ["a", "b", "e", "d", "c"]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#948)

🔬This is a nightly-only experimental API. (`slice_swap_unchecked` [#88539](https://github.com/rust-lang/rust/issues/88539))

Swaps two elements in the slice, without doing bounds checking.

For a safe alternative see [`swap`](https://doc.rust-lang.org/std/primitive.slice.html#method.swap "method slice::swap").

##### [§](#arguments-1)Arguments

- a - The index of the first element
- b - The index of the second element

##### [§](#safety-7)Safety

Calling this method with an out-of-bounds index is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html). The caller has to ensure that `a < self.len()` and `b < self.len()`.

##### [§](#examples-45)Examples

```rust
#![feature(slice_swap_unchecked)]

let mut v = ["a", "b", "c", "d"];
// SAFETY: we know that 1 and 3 are both indices of the slice
unsafe { v.swap_unchecked(1, 3) };
assert!(v == ["a", "d", "c", "b"]);
```

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#978)

Reverses the order of elements in the slice, in place.

##### [§](#examples-46)Examples

```rust
let mut v = [1, 2, 3];
v.reverse();
assert!(v == [3, 2, 1]);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1040)

Returns an iterator over the slice.

The iterator yields all items from start to end.

##### [§](#examples-47)Examples

```rust
let x = &[1, 2, 4];
let mut iterator = x.iter();

assert_eq!(iterator.next(), Some(&1));
assert_eq!(iterator.next(), Some(&2));
assert_eq!(iterator.next(), Some(&4));
assert_eq!(iterator.next(), None);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1060)

Returns an iterator that allows modifying each value.

The iterator yields all items from start to end.

##### [§](#examples-48)Examples

```rust
let x = &mut [1, 2, 4];
for elem in x.iter_mut() {
    *elem += 2;
}
assert_eq!(x, &[3, 4, 6]);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1115)

Returns an iterator over all contiguous windows of length `size`. The windows overlap. If the slice is shorter than `size`, the iterator returns no values.

##### [§](#panics-6)Panics

Panics if `size` is zero.

##### [§](#examples-49)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.windows(3);
assert_eq!(iter.next().unwrap(), &['l', 'o', 'r']);
assert_eq!(iter.next().unwrap(), &['o', 'r', 'e']);
assert_eq!(iter.next().unwrap(), &['r', 'e', 'm']);
assert!(iter.next().is_none());
```

If the slice is shorter than `size`:

```rust
let slice = ['f', 'o', 'o'];
let mut iter = slice.windows(4);
assert!(iter.next().is_none());
```

Because the [Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") trait cannot represent the required lifetimes, there is no `windows_mut` analog to `windows`; `[0,1,2].windows_mut(2).collect()` would violate [the rules of references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#the-rules-of-references) (though a [LendingIterator](https://blog.rust-lang.org/2022/10/28/gats-stabilization.html) analog is possible). You can sometimes use [`Cell::as_slice_of_cells`](https://doc.rust-lang.org/std/cell/struct.Cell.html#method.as_slice_of_cells "method std::cell::Cell::as_slice_of_cells") in conjunction with `windows` instead:

```rust
use std::cell::Cell;

let mut array = ['R', 'u', 's', 't', ' ', '2', '0', '1', '5'];
let slice = &mut array[..];
let slice_of_cells: &[Cell<char>] = Cell::from_mut(slice).as_slice_of_cells();
for w in slice_of_cells.windows(3) {
    Cell::swap(&w[0], &w[2]);
}
assert_eq!(array, ['s', 't', ' ', '2', '0', '1', '5', 'u', 'R']);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1155)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See [`chunks_exact`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_exact "method slice::chunks_exact") for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and [`rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks "method slice::rchunks") for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using [`as_chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks "method slice::as_chunks") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-7)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-50)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.chunks(2);
assert_eq!(iter.next().unwrap(), &['l', 'o']);
assert_eq!(iter.next().unwrap(), &['r', 'e']);
assert_eq!(iter.next().unwrap(), &['m']);
assert!(iter.next().is_none());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1199)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See [`chunks_exact_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_exact_mut "method slice::chunks_exact_mut") for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and [`rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_mut "method slice::rchunks_mut") for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using [`as_chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks_mut "method slice::as_chunks_mut") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-8)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-51)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.chunks_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 3]);
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1242)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of [`chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks "method slice::chunks").

See [`chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks "method slice::chunks") for a variant of this iterator that also returns the remainder as a smaller chunk, and [`rchunks_exact`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_exact "method slice::rchunks_exact") for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using [`as_chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks "method slice::as_chunks") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-9)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-52)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.chunks_exact(2);
assert_eq!(iter.next().unwrap(), &['l', 'o']);
assert_eq!(iter.next().unwrap(), &['r', 'e']);
assert!(iter.next().is_none());
assert_eq!(iter.remainder(), &['m']);
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1290)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the beginning of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `into_remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of [`chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_mut "method slice::chunks_mut").

See [`chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_mut "method slice::chunks_mut") for a variant of this iterator that also returns the remainder as a smaller chunk, and [`rchunks_exact_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_exact_mut "method slice::rchunks_exact_mut") for the same iterator but starting at the end of the slice.

If your `chunk_size` is a constant, consider using [`as_chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks_mut "method slice::as_chunks_mut") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-10)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-53)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.chunks_exact_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 0]);
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1338)

Splits the slice into a slice of `N`-element arrays, assuming that there’s no remainder.

This is the inverse operation to [`as_flattened`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened "method slice::as_flattened").

As this is `unsafe`, consider whether you could use [`as_chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks "method slice::as_chunks") or [`as_rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks "method slice::as_rchunks") instead, perhaps via something like `if let (chunks, []) = slice.as_chunks()` or `let (chunks, []) = slice.as_chunks() else { unreachable!() };`.

##### [§](#safety-8)Safety

This may only be called when

- The slice splits exactly into `N`-element chunks (aka `self.len() % N == 0`).
- `N != 0`.

##### [§](#examples-54)Examples

```rust
let slice: &[char] = &['l', 'o', 'r', 'e', 'm', '!'];
let chunks: &[[char; 1]] =
    // SAFETY: 1-element chunks never have remainder
    unsafe { slice.as_chunks_unchecked() };
assert_eq!(chunks, &[['l'], ['o'], ['r'], ['e'], ['m'], ['!']]);
let chunks: &[[char; 3]] =
    // SAFETY: The slice length (6) is a multiple of 3
    unsafe { slice.as_chunks_unchecked() };
assert_eq!(chunks, &[['l', 'o', 'r'], ['e', 'm', '!']]);

// These would be unsound:
// let chunks: &[[_; 5]] = slice.as_chunks_unchecked() // The slice length is not a multiple of 5
// let chunks: &[[_; 0]] = slice.as_chunks_unchecked() // Zero-length chunks are never allowed
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1396)

Splits the slice into a slice of `N`-element arrays, starting at the beginning of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (chunks, remainder) = slice.as_chunks()`, then:

- `chunks.len()` equals `slice.len() / N`,
- `remainder.len()` equals `slice.len() % N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with [`as_flattened`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened "method slice::as_flattened").

##### [§](#panics-11)Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### [§](#examples-55)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let (chunks, remainder) = slice.as_chunks();
assert_eq!(chunks, &[['l', 'o'], ['r', 'e']]);
assert_eq!(remainder, &['m']);
```

If you expect the slice to be an exact multiple, you can combine `let`-`else` with an empty slice pattern:

```rust
let slice = ['R', 'u', 's', 't'];
let (chunks, []) = slice.as_chunks::<2>() else {
    panic!("slice didn't have even length")
};
assert_eq!(chunks, &[['R', 'u'], ['s', 't']]);
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1443)

Splits the slice into a slice of `N`-element arrays, starting at the end of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (remainder, chunks) = slice.as_rchunks()`, then:

- `remainder.len()` equals `slice.len() % N`,
- `chunks.len()` equals `slice.len() / N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with [`as_flattened`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened "method slice::as_flattened").

##### [§](#panics-12)Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### [§](#examples-56)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let (remainder, chunks) = slice.as_rchunks();
assert_eq!(remainder, &['l']);
assert_eq!(chunks, &[['o', 'r'], ['e', 'm']]);
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1498)

Splits the slice into a slice of `N`-element arrays, assuming that there’s no remainder.

This is the inverse operation to [`as_flattened_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened_mut "method slice::as_flattened_mut").

As this is `unsafe`, consider whether you could use [`as_chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks_mut "method slice::as_chunks_mut") or [`as_rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks_mut "method slice::as_rchunks_mut") instead, perhaps via something like `if let (chunks, []) = slice.as_chunks_mut()` or `let (chunks, []) = slice.as_chunks_mut() else { unreachable!() };`.

##### [§](#safety-9)Safety

This may only be called when

- The slice splits exactly into `N`-element chunks (aka `self.len() % N == 0`).
- `N != 0`.

##### [§](#examples-57)Examples

```rust
let slice: &mut [char] = &mut ['l', 'o', 'r', 'e', 'm', '!'];
let chunks: &mut [[char; 1]] =
    // SAFETY: 1-element chunks never have remainder
    unsafe { slice.as_chunks_unchecked_mut() };
chunks[0] = ['L'];
assert_eq!(chunks, &[['L'], ['o'], ['r'], ['e'], ['m'], ['!']]);
let chunks: &mut [[char; 3]] =
    // SAFETY: The slice length (6) is a multiple of 3
    unsafe { slice.as_chunks_unchecked_mut() };
chunks[1] = ['a', 'x', '?'];
assert_eq!(slice, &['L', 'o', 'r', 'a', 'x', '?']);

// These would be unsound:
// let chunks: &[[_; 5]] = slice.as_chunks_unchecked_mut() // The slice length is not a multiple of 5
// let chunks: &[[_; 0]] = slice.as_chunks_unchecked_mut() // Zero-length chunks are never allowed
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1552)

Splits the slice into a slice of `N`-element arrays, starting at the beginning of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (chunks, remainder) = slice.as_chunks_mut()`, then:

- `chunks.len()` equals `slice.len() / N`,
- `remainder.len()` equals `slice.len() % N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with [`as_flattened_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened_mut "method slice::as_flattened_mut").

##### [§](#panics-13)Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### [§](#examples-58)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

let (chunks, remainder) = v.as_chunks_mut();
remainder[0] = 9;
for chunk in chunks {
    *chunk = [count; 2];
    count += 1;
}
assert_eq!(v, &[1, 1, 2, 2, 9]);
```

1.88.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1605)

Splits the slice into a slice of `N`-element arrays, starting at the end of the slice, and a remainder slice with length strictly less than `N`.

The remainder is meaningful in the division sense. Given `let (remainder, chunks) = slice.as_rchunks_mut()`, then:

- `remainder.len()` equals `slice.len() % N`,
- `chunks.len()` equals `slice.len() / N`, and
- `slice.len()` equals `chunks.len() * N + remainder.len()`.

You can flatten the chunks back into a slice-of-`T` with [`as_flattened_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_flattened_mut "method slice::as_flattened_mut").

##### [§](#panics-14)Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### [§](#examples-59)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

let (remainder, chunks) = v.as_rchunks_mut();
remainder[0] = 9;
for chunk in chunks {
    *chunk = [count; 2];
    count += 1;
}
assert_eq!(v, &[9, 1, 1, 2, 2]);
```

1.94.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1646)

Returns an iterator over overlapping windows of `N` elements of a slice, starting at the beginning of the slice.

This is the const generic equivalent of [`windows`](https://doc.rust-lang.org/std/primitive.slice.html#method.windows "method slice::windows").

If `N` is greater than the size of the slice, it will return no windows.

##### [§](#panics-15)Panics

Panics if `N` is zero.

Note that this check is against a const generic parameter, not a runtime value, and thus a particular monomorphization will either always panic or it will never panic.

##### [§](#examples-60)Examples

```rust
let slice = [0, 1, 2, 3];
let mut iter = slice.array_windows();
assert_eq!(iter.next().unwrap(), &[0, 1]);
assert_eq!(iter.next().unwrap(), &[1, 2]);
assert_eq!(iter.next().unwrap(), &[2, 3]);
assert!(iter.next().is_none());
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1686)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See [`rchunks_exact`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_exact "method slice::rchunks_exact") for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and [`chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks "method slice::chunks") for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using [`as_rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks "method slice::as_rchunks") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-16)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-61)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.rchunks(2);
assert_eq!(iter.next().unwrap(), &['e', 'm']);
assert_eq!(iter.next().unwrap(), &['o', 'r']);
assert_eq!(iter.next().unwrap(), &['l']);
assert!(iter.next().is_none());
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1730)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last chunk will not have length `chunk_size`.

See [`rchunks_exact_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_exact_mut "method slice::rchunks_exact_mut") for a variant of this iterator that returns chunks of always exactly `chunk_size` elements, and [`chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_mut "method slice::chunks_mut") for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using [`as_rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks_mut "method slice::as_rchunks_mut") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-17)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-62)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.rchunks_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[3, 2, 2, 1, 1]);
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1775)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are slices and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of [`rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks "method slice::rchunks").

See [`rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks "method slice::rchunks") for a variant of this iterator that also returns the remainder as a smaller chunk, and [`chunks_exact`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_exact "method slice::chunks_exact") for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using [`as_rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks "method slice::as_rchunks") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-18)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-63)Examples

```rust
let slice = ['l', 'o', 'r', 'e', 'm'];
let mut iter = slice.rchunks_exact(2);
assert_eq!(iter.next().unwrap(), &['e', 'm']);
assert_eq!(iter.next().unwrap(), &['o', 'r']);
assert!(iter.next().is_none());
assert_eq!(iter.remainder(), &['l']);
```

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1824)

Returns an iterator over `chunk_size` elements of the slice at a time, starting at the end of the slice.

The chunks are mutable slices, and do not overlap. If `chunk_size` does not divide the length of the slice, then the last up to `chunk_size-1` elements will be omitted and can be retrieved from the `into_remainder` function of the iterator.

Due to each chunk having exactly `chunk_size` elements, the compiler can often optimize the resulting code better than in the case of [`chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_mut "method slice::chunks_mut").

See [`rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.rchunks_mut "method slice::rchunks_mut") for a variant of this iterator that also returns the remainder as a smaller chunk, and [`chunks_exact_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks_exact_mut "method slice::chunks_exact_mut") for the same iterator but starting at the beginning of the slice.

If your `chunk_size` is a constant, consider using [`as_rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks_mut "method slice::as_rchunks_mut") instead, which will give references to arrays of exactly that length, rather than slices.

##### [§](#panics-19)Panics

Panics if `chunk_size` is zero.

##### [§](#examples-64)Examples

```rust
let v = &mut [0, 0, 0, 0, 0];
let mut count = 1;

for chunk in v.rchunks_exact_mut(2) {
    for elem in chunk.iter_mut() {
        *elem += count;
    }
    count += 1;
}
assert_eq!(v, &[0, 2, 2, 1, 1]);
```

1.77.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1864-1866)

Returns an iterator over the slice producing non-overlapping runs of elements using the predicate to separate them.

The predicate is called for every pair of consecutive elements, meaning that it is called on `slice[0]` and `slice[1]`, followed by `slice[1]` and `slice[2]`, and so on.

##### [§](#examples-65)Examples

```rust
let slice = &[1, 1, 1, 3, 3, 2, 2, 2];

let mut iter = slice.chunk_by(|a, b| a == b);

assert_eq!(iter.next(), Some(&[1, 1, 1][..]));
assert_eq!(iter.next(), Some(&[3, 3][..]));
assert_eq!(iter.next(), Some(&[2, 2, 2][..]));
assert_eq!(iter.next(), None);
```

This method can be used to extract the sorted subslices:

```rust
let slice = &[1, 1, 2, 3, 2, 3, 2, 3, 4];

let mut iter = slice.chunk_by(|a, b| a <= b);

assert_eq!(iter.next(), Some(&[1, 1, 2, 3][..]));
assert_eq!(iter.next(), Some(&[2, 3][..]));
assert_eq!(iter.next(), Some(&[2, 3, 4][..]));
assert_eq!(iter.next(), None);
```

1.77.0 (const: [unstable](https://github.com/rust-lang/rust/issues/137737 "Tracking issue for const_slice_make_iter")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1906-1908)

Returns an iterator over the slice producing non-overlapping mutable runs of elements using the predicate to separate them.

The predicate is called for every pair of consecutive elements, meaning that it is called on `slice[0]` and `slice[1]`, followed by `slice[1]` and `slice[2]`, and so on.

##### [§](#examples-66)Examples

```rust
let slice = &mut [1, 1, 1, 3, 3, 2, 2, 2];

let mut iter = slice.chunk_by_mut(|a, b| a == b);

assert_eq!(iter.next(), Some(&mut [1, 1, 1][..]));
assert_eq!(iter.next(), Some(&mut [3, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 2, 2][..]));
assert_eq!(iter.next(), None);
```

This method can be used to extract the sorted subslices:

```rust
let slice = &mut [1, 1, 2, 3, 2, 3, 2, 3, 4];

let mut iter = slice.chunk_by_mut(|a, b| a <= b);

assert_eq!(iter.next(), Some(&mut [1, 1, 2, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 3][..]));
assert_eq!(iter.next(), Some(&mut [2, 3, 4][..]));
assert_eq!(iter.next(), None);
```

1.0.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1952)

Divides one slice into two at an index.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### [§](#panics-20)Panics

Panics if `mid > len`. For a non-panicking alternative see [`split_at_checked`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_checked "method slice::split_at_checked").

##### [§](#examples-67)Examples

```rust
let v = ['a', 'b', 'c'];

{
   let (left, right) = v.split_at(0);
   assert_eq!(left, []);
   assert_eq!(right, ['a', 'b', 'c']);
}

{
    let (left, right) = v.split_at(2);
    assert_eq!(left, ['a', 'b']);
    assert_eq!(right, ['c']);
}

{
    let (left, right) = v.split_at(3);
    assert_eq!(left, ['a', 'b', 'c']);
    assert_eq!(right, []);
}
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#1986)

Divides one mutable slice into two at an index.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### [§](#panics-21)Panics

Panics if `mid > len`. For a non-panicking alternative see [`split_at_mut_checked`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_mut_checked "method slice::split_at_mut_checked").

##### [§](#examples-68)Examples

```rust
let mut v = [1, 0, 3, 0, 5, 6];
let (left, right) = v.split_at_mut(2);
assert_eq!(left, [1, 0]);
assert_eq!(right, [3, 0, 5, 6]);
left[1] = 2;
right[1] = 4;
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

1.79.0 (const: 1.77.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2038)

Divides one slice into two at an index, without doing bounds checking.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

For a safe alternative see [`split_at`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at "method slice::split_at").

##### [§](#safety-10)Safety

Calling this method with an out-of-bounds index is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting reference is not used. The caller has to ensure that `0 <= mid <= self.len()`.

##### [§](#examples-69)Examples

```rust
let v = ['a', 'b', 'c'];

unsafe {
   let (left, right) = v.split_at_unchecked(0);
   assert_eq!(left, []);
   assert_eq!(right, ['a', 'b', 'c']);
}

unsafe {
    let (left, right) = v.split_at_unchecked(2);
    assert_eq!(left, ['a', 'b']);
    assert_eq!(right, ['c']);
}

unsafe {
    let (left, right) = v.split_at_unchecked(3);
    assert_eq!(left, ['a', 'b', 'c']);
    assert_eq!(right, []);
}
```

1.79.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2092)

Divides one mutable slice into two at an index, without doing bounds checking.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

For a safe alternative see [`split_at_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_mut "method slice::split_at_mut").

##### [§](#safety-11)Safety

Calling this method with an out-of-bounds index is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting reference is not used. The caller has to ensure that `0 <= mid <= self.len()`.

##### [§](#examples-70)Examples

```rust
let mut v = [1, 0, 3, 0, 5, 6];
// scoped to restrict the lifetime of the borrows
unsafe {
    let (left, right) = v.split_at_mut_unchecked(2);
    assert_eq!(left, [1, 0]);
    assert_eq!(right, [3, 0, 5, 6]);
    left[1] = 2;
    right[1] = 4;
}
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2153)

Divides one slice into two at an index, returning `None` if the slice is too short.

If `mid ≤ len` returns a pair of slices where the first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

Otherwise, if `mid > len`, returns `None`.

##### [§](#examples-71)Examples

```rust
let v = [1, -2, 3, -4, 5, -6];

{
   let (left, right) = v.split_at_checked(0).unwrap();
   assert_eq!(left, []);
   assert_eq!(right, [1, -2, 3, -4, 5, -6]);
}

{
    let (left, right) = v.split_at_checked(2).unwrap();
    assert_eq!(left, [1, -2]);
    assert_eq!(right, [3, -4, 5, -6]);
}

{
    let (left, right) = v.split_at_checked(6).unwrap();
    assert_eq!(left, [1, -2, 3, -4, 5, -6]);
    assert_eq!(right, []);
}

assert_eq!(None, v.split_at_checked(7));
```

1.80.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2192)

Divides one mutable slice into two at an index, returning `None` if the slice is too short.

If `mid ≤ len` returns a pair of slices where the first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

Otherwise, if `mid > len`, returns `None`.

##### [§](#examples-72)Examples

```rust
let mut v = [1, 0, 3, 0, 5, 6];

if let Some((left, right)) = v.split_at_mut_checked(2) {
    assert_eq!(left, [1, 0]);
    assert_eq!(right, [3, 0, 5, 6]);
    left[1] = 2;
    right[1] = 4;
}
assert_eq!(v, [1, 2, 3, 4, 5, 6]);

assert_eq!(None, v.split_at_mut_checked(7));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2244-2246)

Returns an iterator over subslices separated by elements that match `pred`. The matched element is not contained in the subslices.

##### [§](#examples-73)Examples

```rust
let slice = [10, 40, 33, 20];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

If the first element is matched, an empty slice will be the first item returned by the iterator. Similarly, if the last element in the slice is matched, an empty slice will be the last item returned by the iterator:

```rust
let slice = [10, 40, 33];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40]);
assert_eq!(iter.next().unwrap(), &[]);
assert!(iter.next().is_none());
```

If two matched elements are directly adjacent, an empty slice will be present between them:

```rust
let slice = [10, 6, 33, 20];
let mut iter = slice.split(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10]);
assert_eq!(iter.next().unwrap(), &[]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2266-2268)

Returns an iterator over mutable subslices separated by elements that match `pred`. The matched element is not contained in the subslices.

##### [§](#examples-74)Examples

```rust
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.split_mut(|num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(v, [1, 40, 30, 1, 60, 1]);
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2302-2304)

Returns an iterator over subslices separated by elements that match `pred`. The matched element is contained in the end of the previous subslice as a terminator.

##### [§](#examples-75)Examples

```rust
let slice = [10, 40, 33, 20];
let mut iter = slice.split_inclusive(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[10, 40, 33]);
assert_eq!(iter.next().unwrap(), &[20]);
assert!(iter.next().is_none());
```

If the last element of the slice is matched, that element will be considered the terminator of the preceding slice. That slice will be the last item returned by the iterator.

```rust
let slice = [3, 10, 40, 33];
let mut iter = slice.split_inclusive(|num| num % 3 == 0);

assert_eq!(iter.next().unwrap(), &[3]);
assert_eq!(iter.next().unwrap(), &[10, 40, 33]);
assert!(iter.next().is_none());
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2326-2328)

Returns an iterator over mutable subslices separated by elements that match `pred`. The matched element is contained in the previous subslice as a terminator.

##### [§](#examples-76)Examples

```rust
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.split_inclusive_mut(|num| *num % 3 == 0) {
    let terminator_idx = group.len()-1;
    group[terminator_idx] = 1;
}
assert_eq!(v, [10, 40, 1, 20, 1, 1]);
```

1.27.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2362-2364)

Returns an iterator over subslices separated by elements that match `pred`, starting at the end of the slice and working backwards. The matched element is not contained in the subslices.

##### [§](#examples-77)Examples

```rust
let slice = [11, 22, 33, 0, 44, 55];
let mut iter = slice.rsplit(|num| *num == 0);

assert_eq!(iter.next().unwrap(), &[44, 55]);
assert_eq!(iter.next().unwrap(), &[11, 22, 33]);
assert_eq!(iter.next(), None);
```

As with `split()`, if the first or last element is matched, an empty slice will be the first (or last) item returned by the iterator.

```rust
let v = &[0, 1, 1, 2, 3, 5, 8];
let mut it = v.rsplit(|n| *n % 2 == 0);
assert_eq!(it.next().unwrap(), &[]);
assert_eq!(it.next().unwrap(), &[3, 5]);
assert_eq!(it.next().unwrap(), &[1, 1]);
assert_eq!(it.next().unwrap(), &[]);
assert_eq!(it.next(), None);
```

1.27.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2388-2390)

Returns an iterator over mutable subslices separated by elements that match `pred`, starting at the end of the slice and working backwards. The matched element is not contained in the subslices.

##### [§](#examples-78)Examples

```rust
let mut v = [100, 400, 300, 200, 600, 500];

let mut count = 0;
for group in v.rsplit_mut(|num| *num % 3 == 0) {
    count += 1;
    group[0] = count;
}
assert_eq!(v, [3, 400, 300, 2, 600, 1]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2416-2418)

Returns an iterator over subslices separated by elements that match `pred`, limited to returning at most `n` items. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### [§](#examples-79)Examples

Print the slice split once by numbers divisible by 3 (i.e., `[10, 40]`, `[20, 60, 50]`):

```rust
let v = [10, 40, 30, 20, 60, 50];

for group in v.splitn(2, |num| *num % 3 == 0) {
    println!("{group:?}");
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2442-2444)

Returns an iterator over mutable subslices separated by elements that match `pred`, limited to returning at most `n` items. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### [§](#examples-80)Examples

```rust
let mut v = [10, 40, 30, 20, 60, 50];

for group in v.splitn_mut(2, |num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(v, [1, 40, 30, 1, 60, 50]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2471-2473)

Returns an iterator over subslices separated by elements that match `pred` limited to returning at most `n` items. This starts at the end of the slice and works backwards. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### [§](#examples-81)Examples

Print the slice split once, starting from the end, by numbers divisible by 3 (i.e., `[50]`, `[10, 40, 30, 20]`):

```rust
let v = [10, 40, 30, 20, 60, 50];

for group in v.rsplitn(2, |num| *num % 3 == 0) {
    println!("{group:?}");
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2498-2500)

Returns an iterator over subslices separated by elements that match `pred` limited to returning at most `n` items. This starts at the end of the slice and works backwards. The matched element is not contained in the subslices.

The last element returned, if any, will contain the remainder of the slice.

##### [§](#examples-82)Examples

```rust
let mut s = [10, 40, 30, 20, 60, 50];

for group in s.rsplitn_mut(2, |num| *num % 3 == 0) {
    group[0] = 1;
}
assert_eq!(s, [1, 40, 30, 20, 60, 1]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2525-2527)

🔬This is a nightly-only experimental API. (`slice_split_once` [#112811](https://github.com/rust-lang/rust/issues/112811))

Splits the slice on the first element that matches the specified predicate.

If any matching elements are present in the slice, returns the prefix before the match and suffix after. The matching element itself is not included. If no elements match, returns `None`.

##### [§](#examples-83)Examples

```rust
#![feature(slice_split_once)]
let s = [1, 2, 3, 2, 4];
assert_eq!(s.split_once(|&x| x == 2), Some((
    &[1][..],
    &[3, 2, 4][..]
)));
assert_eq!(s.split_once(|&x| x == 0), None);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2553-2555)

🔬This is a nightly-only experimental API. (`slice_split_once` [#112811](https://github.com/rust-lang/rust/issues/112811))

Splits the slice on the last element that matches the specified predicate.

If any matching elements are present in the slice, returns the prefix before the match and suffix after. The matching element itself is not included. If no elements match, returns `None`.

##### [§](#examples-84)Examples

```rust
#![feature(slice_split_once)]
let s = [1, 2, 3, 2, 4];
assert_eq!(s.rsplit_once(|&x| x == 2), Some((
    &[1, 2, 3][..],
    &[4][..]
)));
assert_eq!(s.rsplit_once(|&x| x == 0), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2589-2591)

Returns `true` if the slice contains an element with the given value.

This operation is *O*(*n*).

Note that if you have a sorted slice, [`binary_search`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search "method slice::binary_search") may be faster.

##### [§](#examples-85)Examples

```rust
let v = [10, 40, 30];
assert!(v.contains(&30));
assert!(!v.contains(&50));
```

If you do not have a `&T`, but some other value that you can compare with one (for example, `String` implements `PartialEq<str>`), you can use `iter().any`:

```rust
let v = [String::from("hello"), String::from("world")]; // slice of `String`
assert!(v.iter().any(|e| e == "hello")); // search with `&str`
assert!(!v.iter().any(|e| e == "hi"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2619-2621)

Returns `true` if `needle` is a prefix of the slice or equal to the slice.

##### [§](#examples-86)Examples

```rust
let v = [10, 40, 30];
assert!(v.starts_with(&[10]));
assert!(v.starts_with(&[10, 40]));
assert!(v.starts_with(&v));
assert!(!v.starts_with(&[50]));
assert!(!v.starts_with(&[10, 50]));
```

Always returns `true` if `needle` is an empty slice:

```rust
let v = &[10, 40, 30];
assert!(v.starts_with(&[]));
let v: &[u8] = &[];
assert!(v.starts_with(&[]));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2650-2652)

Returns `true` if `needle` is a suffix of the slice or equal to the slice.

##### [§](#examples-87)Examples

```rust
let v = [10, 40, 30];
assert!(v.ends_with(&[30]));
assert!(v.ends_with(&[40, 30]));
assert!(v.ends_with(&v));
assert!(!v.ends_with(&[50]));
assert!(!v.ends_with(&[50, 30]));
```

Always returns `true` if `needle` is an empty slice:

```rust
let v = &[10, 40, 30];
assert!(v.ends_with(&[]));
let v: &[u8] = &[];
assert!(v.ends_with(&[]));
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2682-2684)

Returns a subslice with the prefix removed.

If the slice starts with `prefix`, returns the subslice after the prefix, wrapped in `Some`. If `prefix` is empty, simply returns the original slice. If `prefix` is equal to the original slice, returns an empty slice.

If the slice does not start with `prefix`, returns `None`.

##### [§](#examples-88)Examples

```rust
let v = &[10, 40, 30];
assert_eq!(v.strip_prefix(&[10]), Some(&[40, 30][..]));
assert_eq!(v.strip_prefix(&[10, 40]), Some(&[30][..]));
assert_eq!(v.strip_prefix(&[10, 40, 30]), Some(&[][..]));
assert_eq!(v.strip_prefix(&[50]), None);
assert_eq!(v.strip_prefix(&[10, 50]), None);

let prefix : &str = "he";
assert_eq!(b"hello".strip_prefix(prefix.as_bytes()),
           Some(b"llo".as_ref()));
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2718-2720)

Returns a subslice with the suffix removed.

If the slice ends with `suffix`, returns the subslice before the suffix, wrapped in `Some`. If `suffix` is empty, simply returns the original slice. If `suffix` is equal to the original slice, returns an empty slice.

If the slice does not end with `suffix`, returns `None`.

##### [§](#examples-89)Examples

```rust
let v = &[10, 40, 30];
assert_eq!(v.strip_suffix(&[30]), Some(&[10, 40][..]));
assert_eq!(v.strip_suffix(&[40, 30]), Some(&[10][..]));
assert_eq!(v.strip_suffix(&[10, 40, 30]), Some(&[][..]));
assert_eq!(v.strip_suffix(&[50]), None);
assert_eq!(v.strip_suffix(&[50, 30]), None);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2757-2761)

🔬This is a nightly-only experimental API. (`strip_circumfix` [#147946](https://github.com/rust-lang/rust/issues/147946))

Returns a subslice with the prefix and suffix removed.

If the slice starts with `prefix` and ends with `suffix`, returns the subslice after the prefix and before the suffix, wrapped in `Some`.

If the slice does not start with `prefix` or does not end with `suffix`, returns `None`.

##### [§](#examples-90)Examples

```rust
#![feature(strip_circumfix)]

let v = &[10, 50, 40, 30];
assert_eq!(v.strip_circumfix(&[10], &[30]), Some(&[50, 40][..]));
assert_eq!(v.strip_circumfix(&[10], &[40, 30]), Some(&[50][..]));
assert_eq!(v.strip_circumfix(&[10, 50], &[40, 30]), Some(&[][..]));
assert_eq!(v.strip_circumfix(&[50], &[30]), None);
assert_eq!(v.strip_circumfix(&[10], &[40]), None);
assert_eq!(v.strip_circumfix(&[], &[40, 30]), Some(&[10, 50][..]));
assert_eq!(v.strip_circumfix(&[10, 50], &[]), Some(&[40, 30][..]));
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2793-2795)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a subslice with the optional prefix removed.

If the slice starts with `prefix`, returns the subslice after the prefix. If `prefix` is empty or the slice does not start with `prefix`, simply returns the original slice. If `prefix` is equal to the original slice, returns an empty slice.

##### [§](#examples-91)Examples

```rust
#![feature(trim_prefix_suffix)]

let v = &[10, 40, 30];

// Prefix present - removes it
assert_eq!(v.trim_prefix(&[10]), &[40, 30][..]);
assert_eq!(v.trim_prefix(&[10, 40]), &[30][..]);
assert_eq!(v.trim_prefix(&[10, 40, 30]), &[][..]);

// Prefix absent - returns original slice
assert_eq!(v.trim_prefix(&[50]), &[10, 40, 30][..]);
assert_eq!(v.trim_prefix(&[10, 50]), &[10, 40, 30][..]);

let prefix : &str = "he";
assert_eq!(b"hello".trim_prefix(prefix.as_bytes()), b"llo".as_ref());
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2833-2835)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a subslice with the optional suffix removed.

If the slice ends with `suffix`, returns the subslice before the suffix. If `suffix` is empty or the slice does not end with `suffix`, simply returns the original slice. If `suffix` is equal to the original slice, returns an empty slice.

##### [§](#examples-92)Examples

```rust
#![feature(trim_prefix_suffix)]

let v = &[10, 40, 30];

// Suffix present - removes it
assert_eq!(v.trim_suffix(&[30]), &[10, 40][..]);
assert_eq!(v.trim_suffix(&[40, 30]), &[10][..]);
assert_eq!(v.trim_suffix(&[10, 40, 30]), &[][..]);

// Suffix absent - returns original slice
assert_eq!(v.trim_suffix(&[50]), &[10, 40, 30][..]);
assert_eq!(v.trim_suffix(&[50, 30]), &[10, 40, 30][..]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2919-2921)

Binary searches this slice for a given element. If the slice is not sorted, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by "method slice::binary_search_by"), [`binary_search_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by_key "method slice::binary_search_by_key"), and [`partition_point`](https://doc.rust-lang.org/std/primitive.slice.html#method.partition_point "method slice::partition_point").

##### [§](#examples-93)Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

assert_eq!(s.binary_search(&13),  Ok(9));
assert_eq!(s.binary_search(&4),   Err(7));
assert_eq!(s.binary_search(&100), Err(13));
let r = s.binary_search(&1);
assert!(match r { Ok(1..=4) => true, _ => false, });
```

If you want to find that whole *range* of matching items, rather than an arbitrary matching one, that can be done using [`partition_point`](https://doc.rust-lang.org/std/primitive.slice.html#method.partition_point "method slice::partition_point"):

```rust
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

let low = s.partition_point(|x| x < &1);
assert_eq!(low, 1);
let high = s.partition_point(|x| x <= &1);
assert_eq!(high, 5);
let r = s.binary_search(&1);
assert!((low..high).contains(&r.unwrap()));

assert!(s[..low].iter().all(|&x| x < 1));
assert!(s[low..high].iter().all(|&x| x == 1));
assert!(s[high..].iter().all(|&x| x > 1));

// For something not found, the "range" of equal items is empty
assert_eq!(s.partition_point(|x| x < &11), 9);
assert_eq!(s.partition_point(|x| x <= &11), 9);
assert_eq!(s.binary_search(&11), Err(9));
```

If you want to insert an item to a sorted vector, while maintaining sort order, consider using [`partition_point`](https://doc.rust-lang.org/std/primitive.slice.html#method.partition_point "method slice::partition_point"):

```rust
let mut s = vec![0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
let num = 42;
let idx = s.partition_point(|&x| x <= num);
// If `num` is unique, `s.partition_point(|&x| x < num)` (with `<`) is equivalent to
// `s.binary_search(&num).unwrap_or_else(|x| x)`, but using `<=` will allow `insert`
// to shift less elements.
s.insert(idx, num);
assert_eq!(s, [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#2970-2972)

Binary searches this slice with a comparator function.

The comparator function should return an order code that indicates whether its argument is `Less`, `Equal` or `Greater` the desired target. If the slice is not sorted or if the comparator function does not implement an order consistent with the sort order of the underlying slice, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search "method slice::binary_search"), [`binary_search_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by_key "method slice::binary_search_by_key"), and [`partition_point`](https://doc.rust-lang.org/std/primitive.slice.html#method.partition_point "method slice::partition_point").

##### [§](#examples-94)Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

let seek = 13;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Ok(9));
let seek = 4;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Err(7));
let seek = 100;
assert_eq!(s.binary_search_by(|probe| probe.cmp(&seek)), Err(13));
let seek = 1;
let r = s.binary_search_by(|probe| probe.cmp(&seek));
assert!(match r { Ok(1..=4) => true, _ => false, });
```

1.10.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3071-3074)

Binary searches this slice with a key extraction function.

Assumes that the slice is sorted by the key, for instance with [`sort_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_by_key "method slice::sort_by_key") using the same key extraction function. If the slice is not sorted by the key, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. The index is chosen deterministically, but is subject to change in future versions of Rust. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search "method slice::binary_search"), [`binary_search_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by "method slice::binary_search_by"), and [`partition_point`](https://doc.rust-lang.org/std/primitive.slice.html#method.partition_point "method slice::partition_point").

##### [§](#examples-95)Examples

Looks up a series of four elements in a slice of pairs sorted by their second elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
let s = [(0, 0), (2, 1), (4, 1), (5, 1), (3, 1),
         (1, 2), (2, 3), (4, 5), (5, 8), (3, 13),
         (1, 21), (2, 34), (4, 55)];

assert_eq!(s.binary_search_by_key(&13, |&(a, b)| b),  Ok(9));
assert_eq!(s.binary_search_by_key(&4, |&(a, b)| b),   Err(7));
assert_eq!(s.binary_search_by_key(&100, |&(a, b)| b), Err(13));
let r = s.binary_search_by_key(&1, |&(a, b)| b);
assert!(match r { Ok(1..=4) => true, _ => false, });
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3133-3135)

Sorts the slice in ascending order **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` panics.

Sorting types that only implement [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") such as [`f32`](https://doc.rust-lang.org/std/primitive.f32.html "primitive f32") and [`f64`](https://doc.rust-lang.org/std/primitive.f64.html "primitive f64") require additional precautions. For example, `f32::NAN != f32::NAN`, which doesn’t fulfill the reflexivity requirement of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord"). By using an alternative comparison function with `slice::sort_unstable_by` such as [`f32::total_cmp`](https://doc.rust-lang.org/std/primitive.f32.html#method.total_cmp "method f32::total_cmp") or [`f64::total_cmp`](https://doc.rust-lang.org/std/primitive.f64.html#method.total_cmp "method f64::total_cmp") that defines a [total order](https://en.wikipedia.org/wiki/Total_order) users can sort slices containing floating-point values. Alternatively, if all values in the slice are guaranteed to be in a subset for which [`PartialOrd::partial_cmp`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp "method std::cmp::PartialOrd::partial_cmp") forms a [total order](https://en.wikipedia.org/wiki/Total_order), it’s possible to sort the slice with `sort_unstable_by(|a, b| a.partial_cmp(b).unwrap())`.

##### [§](#current-implementation)Current implementation

The current implementation is based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### [§](#panics-22)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation panics.

##### [§](#examples-96)Examples

```rust
let mut v = [4, -5, 1, -3, 2];

v.sort_unstable();
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3188-3190)

Sorts the slice in ascending order with a comparison function, **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the comparison function `compare` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if `compare` panics.

##### [§](#current-implementation-1)Current implementation

The current implementation is based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### [§](#panics-23)Panics

May panic if the `compare` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the `compare` itself panics.

##### [§](#examples-97)Examples

```rust
let mut v = [4, -5, 1, -3, 2];
v.sort_unstable_by(|a, b| a.cmp(b));
assert_eq!(v, [-5, -3, 1, 2, 4]);

// reverse sorting
v.sort_unstable_by(|a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3240-3243)

Sorts the slice in ascending order with a key extraction function, **without** preserving the initial order of equal elements.

This sort is unstable (i.e., may reorder equal elements), in-place (i.e., does not allocate), and *O*(*n* * log(*n*)) worst-case.

If the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") documentation.

All original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. Same is true if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` panics.

##### [§](#current-implementation-2)Current implementation

The current implementation is based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which combines the fast average case of quicksort with the fast worst case of heapsort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

It is typically faster than stable sorting, except in a few special cases, e.g., when the slice is partially sorted.

##### [§](#panics-24)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation panics.

##### [§](#examples-98)Examples

```rust
let mut v = [4i32, -5, 1, -3, 2];

v.sort_unstable_by_key(|k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3310-3313)

🔬This is a nightly-only experimental API. (`slice_partial_sort_unstable` [#149046](https://github.com/rust-lang/rust/issues/149046))

Partially sorts the slice in ascending order **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of [`sort_unstable`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable "method slice::sort_unstable") for implementation notes.

##### [§](#panics-25)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a total order, or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation panics, or if the specified range is out of bounds.

##### [§](#examples-99)Examples

```rust
#![feature(slice_partial_sort_unstable)]

let mut v = [4, -5, 1, -3, 2];

// empty range at the beginning, nothing changed
v.partial_sort_unstable(0..0);
assert_eq!(v, [4, -5, 1, -3, 2]);

// empty range in the middle, partitioning the slice
v.partial_sort_unstable(2..2);
for i in 0..2 {
   assert!(v[i] <= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] <= v[i]);
}

// single element range, same as select_nth_unstable
v.partial_sort_unstable(2..3);
for i in 0..2 {
   assert!(v[i] <= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] <= v[i]);
}

// partial sort a subrange
v.partial_sort_unstable(1..4);
assert_eq!(&v[1..4], [-3, 1, 2]);

// partial sort the whole range, same as sort_unstable
v.partial_sort_unstable(..);
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3381-3384)

🔬This is a nightly-only experimental API. (`slice_partial_sort_unstable` [#149046](https://github.com/rust-lang/rust/issues/149046))

Partially sorts the slice in ascending order with a comparison function, **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of [`sort_unstable_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by "method slice::sort_unstable_by") for implementation notes.

##### [§](#panics-26)Panics

May panic if the `compare` does not implement a total order, or if the `compare` itself panics, or if the specified range is out of bounds.

##### [§](#examples-100)Examples

```rust
#![feature(slice_partial_sort_unstable)]

let mut v = [4, -5, 1, -3, 2];

// empty range at the beginning, nothing changed
v.partial_sort_unstable_by(0..0, |a, b| b.cmp(a));
assert_eq!(v, [4, -5, 1, -3, 2]);

// empty range in the middle, partitioning the slice
v.partial_sort_unstable_by(2..2, |a, b| b.cmp(a));
for i in 0..2 {
   assert!(v[i] >= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] >= v[i]);
}

// single element range, same as select_nth_unstable
v.partial_sort_unstable_by(2..3, |a, b| b.cmp(a));
for i in 0..2 {
   assert!(v[i] >= v[2]);
}
for i in 3..v.len() {
  assert!(v[2] >= v[i]);
}

// partial sort a subrange
v.partial_sort_unstable_by(1..4, |a, b| b.cmp(a));
assert_eq!(&v[1..4], [2, 1, -3]);

// partial sort the whole range, same as sort_unstable
v.partial_sort_unstable_by(.., |a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3452-3456)

🔬This is a nightly-only experimental API. (`slice_partial_sort_unstable` [#149046](https://github.com/rust-lang/rust/issues/149046))

Partially sorts the slice in ascending order with a key extraction function, **without** preserving the initial order of equal elements.

Upon completion, for the specified range `start..end`, it’s guaranteed that:

1. Every element in `self[..start]` is smaller than or equal to
2. Every element in `self[start..end]`, which is sorted, and smaller than or equal to
3. Every element in `self[end..]`.

This partial sort is unstable, meaning it may reorder equal elements in the specified range. It may reorder elements outside the specified range as well, but the guarantees above still hold.

This partial sort is in-place (i.e., does not allocate), and *O*(*n* + *k* * log(*k*)) worst-case, where *n* is the length of the slice and *k* is the length of the specified range.

See the documentation of [`sort_unstable_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by_key "method slice::sort_unstable_by_key") for implementation notes.

##### [§](#panics-27)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a total order, or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation panics, or if the specified range is out of bounds.

##### [§](#examples-101)Examples

```rust
#![feature(slice_partial_sort_unstable)]

let mut v = [4i32, -5, 1, -3, 2];

// empty range at the beginning, nothing changed
v.partial_sort_unstable_by_key(0..0, |k| k.abs());
assert_eq!(v, [4, -5, 1, -3, 2]);

// empty range in the middle, partitioning the slice
v.partial_sort_unstable_by_key(2..2, |k| k.abs());
for i in 0..2 {
   assert!(v[i].abs() <= v[2].abs());
}
for i in 3..v.len() {
  assert!(v[2].abs() <= v[i].abs());
}

// single element range, same as select_nth_unstable
v.partial_sort_unstable_by_key(2..3, |k| k.abs());
for i in 0..2 {
   assert!(v[i].abs() <= v[2].abs());
}
for i in 3..v.len() {
  assert!(v[2].abs() <= v[i].abs());
}

// partial sort a subrange
v.partial_sort_unstable_by_key(1..4, |k| k.abs());
assert_eq!(&v[1..4], [2, -3, 4]);

// partial sort the whole range, same as sort_unstable
v.partial_sort_unstable_by_key(.., |k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

1.49.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3516-3518)

Reorders the slice such that the element at `index` is at a sort-order position. All elements before `index` will be `<=` to this value, and all elements after will be `>=` to it.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple that partitions the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `x <= self[index]`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `x >= self[index]`.

##### [§](#current-implementation-3)Current implementation

The current algorithm is an introselect implementation based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which is also the basis for [`sort_unstable`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable "method slice::sort_unstable"). The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### [§](#panics-28)Panics

Panics when `index >= len()`, and so always panics on empty slices.

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order).

##### [§](#examples-102)Examples

```rust
let mut v = [-5i32, 4, 2, -3, 1];

// Find the items `<=` to the median, the median itself, and the items `>=` to it.
let (lesser, median, greater) = v.select_nth_unstable(2);

assert!(lesser == [-3, -5] || lesser == [-5, -3]);
assert_eq!(median, &mut 1);
assert!(greater == [4, 2] || greater == [2, 4]);

// We are only guaranteed the slice will be one of the following, based on the way we sort
// about the specified index.
assert!(v == [-3, -5, 1, 2, 4] ||
        v == [-5, -3, 1, 2, 4] ||
        v == [-3, -5, 1, 4, 2] ||
        v == [-5, -3, 1, 4, 2]);
```

1.49.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3581-3587)

Reorders the slice with a comparator function such that the element at `index` is at a sort-order position. All elements before `index` will be `<=` to this value, and all elements after will be `>=` to it, according to the comparator function.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple partitioning the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `compare(x, self[index]).is_le()`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `compare(x, self[index]).is_ge()`.

##### [§](#current-implementation-4)Current implementation

The current algorithm is an introselect implementation based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which is also the basis for [`sort_unstable`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable "method slice::sort_unstable"). The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### [§](#panics-29)Panics

Panics when `index >= len()`, and so always panics on empty slices.

May panic if `compare` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order).

##### [§](#examples-103)Examples

```rust
let mut v = [-5i32, 4, 2, -3, 1];

// Find the items `>=` to the median, the median itself, and the items `<=` to it, by using
// a reversed comparator.
let (before, median, after) = v.select_nth_unstable_by(2, |a, b| b.cmp(a));

assert!(before == [4, 2] || before == [2, 4]);
assert_eq!(median, &mut 1);
assert!(after == [-3, -5] || after == [-5, -3]);

// We are only guaranteed the slice will be one of the following, based on the way we sort
// about the specified index.
assert!(v == [2, 4, 1, -5, -3] ||
        v == [2, 4, 1, -3, -5] ||
        v == [4, 2, 1, -5, -3] ||
        v == [4, 2, 1, -3, -5]);
```

1.49.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3648-3655)

Reorders the slice with a key extraction function such that the element at `index` is at a sort-order position. All elements before `index` will have keys `<=` to the key at `index`, and all elements after will have keys `>=` to it.

This reordering is unstable (i.e. any element that compares equal to the nth element may end up at that position), in-place (i.e. does not allocate), and runs in *O*(*n*) time. This function is also known as “kth element” in other libraries.

Returns a triple partitioning the reordered slice:

- The unsorted subslice before `index`, whose elements all satisfy `f(x) <= f(self[index])`.
- The element at `index`.
- The unsorted subslice after `index`, whose elements all satisfy `f(x) >= f(self[index])`.

##### [§](#current-implementation-5)Current implementation

The current algorithm is an introselect implementation based on [ipnsort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll and Orson Peters, which is also the basis for [`sort_unstable`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable "method slice::sort_unstable"). The fallback algorithm is Median of Medians using Tukey’s Ninther for pivot selection, which guarantees linear runtime for all inputs.

##### [§](#panics-30)Panics

Panics when `index >= len()`, meaning it always panics on empty slices.

May panic if `K: Ord` does not implement a total order.

##### [§](#examples-104)Examples

```rust
let mut v = [-5i32, 4, 1, -3, 2];

// Find the items `<=` to the absolute median, the absolute median itself, and the items
// `>=` to it.
let (lesser, median, greater) = v.select_nth_unstable_by_key(2, |a| a.abs());

assert!(lesser == [1, 2] || lesser == [2, 1]);
assert_eq!(median, &mut -3);
assert!(greater == [4, -5] || greater == [-5, 4]);

// We are only guaranteed the slice will be one of the following, based on the way we sort
// about the specified index.
assert!(v == [1, 2, -3, 4, -5] ||
        v == [1, 2, -3, -5, 4] ||
        v == [2, 1, -3, 4, -5] ||
        v == [2, 1, -3, -5, 4]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3682-3684)

🔬This is a nightly-only experimental API. (`slice_partition_dedup` [#54279](https://github.com/rust-lang/rust/issues/54279))

Moves all consecutive repeated elements to the end of the slice according to the [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") trait implementation.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

If the slice is sorted, the first returned slice contains no duplicates.

##### [§](#examples-105)Examples

```rust
#![feature(slice_partition_dedup)]

let mut slice = [1, 2, 2, 3, 3, 2, 1, 1];

let (dedup, duplicates) = slice.partition_dedup();

assert_eq!(dedup, [1, 2, 3, 2, 1]);
assert_eq!(duplicates, [2, 3, 1]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3716-3718)

🔬This is a nightly-only experimental API. (`slice_partition_dedup` [#54279](https://github.com/rust-lang/rust/issues/54279))

Moves all but the first of consecutive elements to the end of the slice satisfying a given equality relation.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

The `same_bucket` function is passed references to two elements from the slice and must determine if the elements compare equal. The elements are passed in opposite order from their order in the slice, so if `same_bucket(a, b)` returns `true`, `a` is moved at the end of the slice.

If the slice is sorted, the first returned slice contains no duplicates.

##### [§](#examples-106)Examples

```rust
#![feature(slice_partition_dedup)]

let mut slice = ["foo", "Foo", "BAZ", "Bar", "bar", "baz", "BAZ"];

let (dedup, duplicates) = slice.partition_dedup_by(|a, b| a.eq_ignore_ascii_case(b));

assert_eq!(dedup, ["foo", "BAZ", "Bar", "baz"]);
assert_eq!(duplicates, ["bar", "Foo", "BAZ"]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3842-3845)

🔬This is a nightly-only experimental API. (`slice_partition_dedup` [#54279](https://github.com/rust-lang/rust/issues/54279))

Moves all but the first of consecutive elements to the end of the slice that resolve to the same key.

Returns two slices. The first contains no consecutive repeated elements. The second contains all the duplicates in no specified order.

If the slice is sorted, the first returned slice contains no duplicates.

##### [§](#examples-107)Examples

```rust
#![feature(slice_partition_dedup)]

let mut slice = [10, 20, 21, 30, 30, 20, 11, 13];

let (dedup, duplicates) = slice.partition_dedup_by_key(|i| *i / 10);

assert_eq!(dedup, [10, 20, 30, 20, 11]);
assert_eq!(duplicates, [21, 30, 13]);
```

1.26.0 (const: 1.92.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3884)

Rotates the slice in-place such that the first `mid` elements of the slice move to the end while the last `self.len() - mid` elements move to the front.

After calling `rotate_left`, the element previously at index `mid` will become the first element in the slice.

##### [§](#panics-31)Panics

This function will panic if `mid` is greater than the length of the slice. Note that `mid == self.len()` does *not* panic and is a no-op rotation.

##### [§](#complexity)Complexity

Takes linear (in `self.len()`) time.

##### [§](#examples-108)Examples

```rust
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.rotate_left(2);
assert_eq!(a, ['c', 'd', 'e', 'f', 'a', 'b']);
```

Rotating a subslice:

```rust
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a[1..5].rotate_left(1);
assert_eq!(a, ['a', 'c', 'd', 'e', 'b', 'f']);
```

1.26.0 (const: 1.92.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#3930)

Rotates the slice in-place such that the first `self.len() - k` elements of the slice move to the end while the last `k` elements move to the front.

After calling `rotate_right`, the element previously at index `self.len() - k` will become the first element in the slice.

##### [§](#panics-32)Panics

This function will panic if `k` is greater than the length of the slice. Note that `k == self.len()` does *not* panic and is a no-op rotation.

##### [§](#complexity-1)Complexity

Takes linear (in `self.len()`) time.

##### [§](#examples-109)Examples

```rust
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.rotate_right(2);
assert_eq!(a, ['e', 'f', 'a', 'b', 'c', 'd']);
```

Rotating a subslice:

```rust
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
a[1..5].rotate_right(1);
assert_eq!(a, ['a', 'e', 'b', 'c', 'd', 'f']);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4004)

🔬This is a nightly-only experimental API. (`slice_shift` [#151772](https://github.com/rust-lang/rust/issues/151772))

Moves the elements of this slice `N` places to the left, returning the ones that “fall off” the front, and putting `inserted` at the end.

Equivalently, you can think of concatenating `self` and `inserted` into one long sequence, then returning the left-most `N` items and the rest into `self`:

```text
          self (before)    inserted
          vvvvvvvvvvvvvvv  vvv
          [1, 2, 3, 4, 5]  [9]
       ↙   ↙  ↙  ↙  ↙   ↙
     [1]  [2, 3, 4, 5, 9]
     ^^^  ^^^^^^^^^^^^^^^
returned  self (after)
```

See also [`Self::shift_right`](https://doc.rust-lang.org/std/primitive.slice.html#method.shift_right "method slice::shift_right") and compare [`Self::rotate_left`](https://doc.rust-lang.org/std/primitive.slice.html#method.rotate_left "method slice::rotate_left").

##### [§](#examples-110)Examples

```rust
#![feature(slice_shift)]

// Same as the diagram above
let mut a = [1, 2, 3, 4, 5];
let inserted = [9];
let returned = a.shift_left(inserted);
assert_eq!(returned, [1]);
assert_eq!(a, [2, 3, 4, 5, 9]);

// You can shift multiple items at a time
let mut a = *b"Hello world";
assert_eq!(a.shift_left(*b" peace"), *b"Hello ");
assert_eq!(a, *b"world peace");

// The name comes from this operation's similarity to bitshifts
let mut a: u8 = 0b10010110;
a <<= 3;
assert_eq!(a, 0b10110000_u8);
let mut a: [_; 8] = [1, 0, 0, 1, 0, 1, 1, 0];
a.shift_left([0; 3]);
assert_eq!(a, [1, 0, 1, 1, 0, 0, 0, 0]);

// Remember you can sub-slice to affect less that the whole slice.
// For example, this is similar to `.remove(1)` + `.insert(4, 'Z')`
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
assert_eq!(a[1..=4].shift_left(['Z']), ['b']);
assert_eq!(a, ['a', 'c', 'd', 'e', 'Z', 'f']);

// If the size matches it's equivalent to `mem::replace`
let mut a = [1, 2, 3];
assert_eq!(a.shift_left([7, 8, 9]), [1, 2, 3]);
assert_eq!(a, [7, 8, 9]);

// Some of the "inserted" elements end up returned if the slice is too short
let mut a = [];
assert_eq!(a.shift_left([1, 2, 3]), [1, 2, 3]);
let mut a = [9];
assert_eq!(a.shift_left([1, 2, 3]), [9, 1, 2]);
assert_eq!(a, [3]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4108)

🔬This is a nightly-only experimental API. (`slice_shift` [#151772](https://github.com/rust-lang/rust/issues/151772))

Moves the elements of this slice `N` places to the right, returning the ones that “fall off” the back, and putting `inserted` at the beginning.

Equivalently, you can think of concatenating `inserted` and `self` into one long sequence, then returning the right-most `N` items and the rest into `self`:

```text
inserted  self (before)
     vvv  vvvvvvvvvvvvvvv
     [0]  [5, 6, 7, 8, 9]
       ↘   ↘  ↘  ↘  ↘   ↘
          [0, 5, 6, 7, 8]  [9]
          ^^^^^^^^^^^^^^^  ^^^
          self (after)     returned
```

See also [`Self::shift_left`](https://doc.rust-lang.org/std/primitive.slice.html#method.shift_left "method slice::shift_left") and compare [`Self::rotate_right`](https://doc.rust-lang.org/std/primitive.slice.html#method.rotate_right "method slice::rotate_right").

##### [§](#examples-111)Examples

```rust
#![feature(slice_shift)]

// Same as the diagram above
let mut a = [5, 6, 7, 8, 9];
let inserted = [0];
let returned = a.shift_right(inserted);
assert_eq!(returned, [9]);
assert_eq!(a, [0, 5, 6, 7, 8]);

// The name comes from this operation's similarity to bitshifts
let mut a: u8 = 0b10010110;
a >>= 3;
assert_eq!(a, 0b00010010_u8);
let mut a: [_; 8] = [1, 0, 0, 1, 0, 1, 1, 0];
a.shift_right([0; 3]);
assert_eq!(a, [0, 0, 0, 1, 0, 0, 1, 0]);

// Remember you can sub-slice to affect less that the whole slice.
// For example, this is similar to `.remove(4)` + `.insert(1, 'Z')`
let mut a = ['a', 'b', 'c', 'd', 'e', 'f'];
assert_eq!(a[1..=4].shift_right(['Z']), ['e']);
assert_eq!(a, ['a', 'Z', 'b', 'c', 'd', 'f']);

// If the size matches it's equivalent to `mem::replace`
let mut a = [1, 2, 3];
assert_eq!(a.shift_right([7, 8, 9]), [1, 2, 3]);
assert_eq!(a, [7, 8, 9]);

// Some of the "inserted" elements end up returned if the slice is too short
let mut a = [];
assert_eq!(a.shift_right([1, 2, 3]), [1, 2, 3]);
let mut a = [9];
assert_eq!(a.shift_right([1, 2, 3]), [2, 3, 9]);
assert_eq!(a, [1]);
```

1.50.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4166-4168)

Fills `self` with elements by cloning `value`.

##### [§](#examples-112)Examples

```rust
let mut buf = vec![0; 10];
buf.fill(1);
assert_eq!(buf, vec![1; 10]);
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4190-4192)

Fills `self` with elements returned by calling a closure repeatedly.

This method uses a closure to create new values. If you’d rather [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") a given value, use [`fill`](https://doc.rust-lang.org/std/primitive.slice.html#method.fill "method slice::fill"). If you want to use the [`Default`](https://doc.rust-lang.org/std/default/trait.Default.html "trait std::default::Default") trait to generate values, you can pass [`Default::default`](https://doc.rust-lang.org/std/default/trait.Default.html#tymethod.default "associated function std::default::Default::default") as the argument.

##### [§](#examples-113)Examples

```rust
let mut buf = vec![1; 10];
buf.fill_with(Default::default);
assert_eq!(buf, vec![0; 10]);
```

1.7.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4254-4256)

Copies the elements from `src` into `self`.

The length of `src` must be the same as `self`.

##### [§](#panics-33)Panics

This function will panic if the two slices have different lengths.

##### [§](#examples-114)Examples

Cloning two elements from a slice into another:

```rust
let src = [1, 2, 3, 4];
let mut dst = [0, 0];

// Because the slices have to be the same length,
// we slice the source slice from four elements
// to two. It will panic if we don't do this.
dst.clone_from_slice(&src[2..]);

assert_eq!(src, [1, 2, 3, 4]);
assert_eq!(dst, [3, 4]);
```

Rust enforces that there can only be one mutable reference with no immutable references to a particular piece of data in a particular scope. Because of this, attempting to use `clone_from_slice` on a single slice will result in a compile failure:

[ⓘ](# "This example deliberately fails to compile")

```rust
let mut slice = [1, 2, 3, 4, 5];

slice[..2].clone_from_slice(&slice[3..]); // compile fail!
```

To work around this, we can use [`split_at_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_mut "method slice::split_at_mut") to create two distinct sub-slices from a slice:

```rust
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.clone_from_slice(&right[1..]);
}

assert_eq!(slice, [4, 5, 3, 4, 5]);
```

1.9.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4320-4322)

Copies all elements from `src` into `self`, using a memcpy.

The length of `src` must be the same as `self`.

If `T` does not implement `Copy`, use [`clone_from_slice`](https://doc.rust-lang.org/std/primitive.slice.html#method.clone_from_slice "method slice::clone_from_slice").

##### [§](#panics-34)Panics

This function will panic if the two slices have different lengths.

##### [§](#examples-115)Examples

Copying two elements from a slice into another:

```rust
let src = [1, 2, 3, 4];
let mut dst = [0, 0];

// Because the slices have to be the same length,
// we slice the source slice from four elements
// to two. It will panic if we don't do this.
dst.copy_from_slice(&src[2..]);

assert_eq!(src, [1, 2, 3, 4]);
assert_eq!(dst, [3, 4]);
```

Rust enforces that there can only be one mutable reference with no immutable references to a particular piece of data in a particular scope. Because of this, attempting to use `copy_from_slice` on a single slice will result in a compile failure:

[ⓘ](# "This example deliberately fails to compile")

```rust
let mut slice = [1, 2, 3, 4, 5];

slice[..2].copy_from_slice(&slice[3..]); // compile fail!
```

To work around this, we can use [`split_at_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_mut "method slice::split_at_mut") to create two distinct sub-slices from a slice:

```rust
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.copy_from_slice(&right[1..]);
}

assert_eq!(slice, [4, 5, 3, 4, 5]);
```

1.37.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4354-4356)

Copies elements from one part of the slice to another part of itself, using a memmove.

`src` is the range within `self` to copy from. `dest` is the starting index of the range within `self` to copy to, which will have the same length as `src`. The two ranges may overlap. The ends of the two ranges must be less than or equal to `self.len()`.

##### [§](#panics-35)Panics

This function will panic if either range exceeds the end of the slice, or if the end of `src` is before the start.

##### [§](#examples-116)Examples

Copying four bytes within a slice:

```rust
let mut bytes = *b"Hello, World!";

bytes.copy_within(1..5, 8);

assert_eq!(&bytes, b"Hello, Wello!");
```

1.27.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142204 "Tracking issue for const_swap_with_slice")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4422)

Swaps all elements in `self` with those in `other`.

The length of `other` must be the same as `self`.

##### [§](#panics-36)Panics

This function will panic if the two slices have different lengths.

##### [§](#example)Example

Swapping two elements across slices:

```rust
let mut slice1 = [0, 0];
let mut slice2 = [1, 2, 3, 4];

slice1.swap_with_slice(&mut slice2[2..]);

assert_eq!(slice1, [3, 4]);
assert_eq!(slice2, [1, 2, 0, 0]);
```

Rust enforces that there can only be one mutable reference to a particular piece of data in a particular scope. Because of this, attempting to use `swap_with_slice` on a single slice will result in a compile failure:

[ⓘ](# "This example deliberately fails to compile")

```rust
let mut slice = [1, 2, 3, 4, 5];
slice[..2].swap_with_slice(&mut slice[3..]); // compile fail!
```

To work around this, we can use [`split_at_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.split_at_mut "method slice::split_at_mut") to create two distinct mutable sub-slices from a slice:

```rust
let mut slice = [1, 2, 3, 4, 5];

{
    let (left, right) = slice.split_at_mut(2);
    left.swap_with_slice(&mut right[1..]);
}

assert_eq!(slice, [4, 5, 3, 1, 2]);
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4499)

Transmutes the slice to a slice of another type, ensuring alignment of the types is maintained.

This method splits the slice into three distinct slices: prefix, correctly aligned middle slice of a new type, and the suffix slice. The middle part will be as big as possible under the given alignment constraint and element size.

This method has no purpose when either input element `T` or output element `U` are zero-sized and will return the original slice without splitting anything.

##### [§](#safety-12)Safety

This method is essentially a `transmute` with respect to the elements in the returned middle slice, so all the usual caveats pertaining to `transmute::<T, U>` also apply here.

##### [§](#examples-117)Examples

Basic usage:

```rust
unsafe {
    let bytes: [u8; 7] = [1, 2, 3, 4, 5, 6, 7];
    let (prefix, shorts, suffix) = bytes.align_to::<u16>();
    // less_efficient_algorithm_for_bytes(prefix);
    // more_efficient_algorithm_for_aligned_shorts(shorts);
    // less_efficient_algorithm_for_bytes(suffix);
}
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4564)

Transmutes the mutable slice to a mutable slice of another type, ensuring alignment of the types is maintained.

This method splits the slice into three distinct slices: prefix, correctly aligned middle slice of a new type, and the suffix slice. The middle part will be as big as possible under the given alignment constraint and element size.

This method has no purpose when either input element `T` or output element `U` are zero-sized and will return the original slice without splitting anything.

##### [§](#safety-13)Safety

This method is essentially a `transmute` with respect to the elements in the returned middle slice, so all the usual caveats pertaining to `transmute::<T, U>` also apply here.

##### [§](#examples-118)Examples

Basic usage:

```rust
unsafe {
    let mut bytes: [u8; 7] = [1, 2, 3, 4, 5, 6, 7];
    let (prefix, shorts, suffix) = bytes.align_to_mut::<u16>();
    // less_efficient_algorithm_for_bytes(prefix);
    // more_efficient_algorithm_for_aligned_shorts(shorts);
    // less_efficient_algorithm_for_bytes(suffix);
}
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4655-4658)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

Splits a slice into a prefix, a middle of aligned SIMD types, and a suffix.

This is a safe wrapper around [`slice::align_to`](https://doc.rust-lang.org/std/primitive.slice.html#method.align_to "method slice::align_to"), so inherits the same guarantees as that method.

##### [§](#panics-37)Panics

This will panic if the size of the SIMD type is different from `LANES` times that of the scalar.

At the time of writing, the trait restrictions on `Simd<T, LANES>` keeps that from ever happening, as only power-of-two numbers of lanes are supported. It’s possible that, in the future, those restrictions might be lifted in a way that would make it possible to see panics from this method for something like `LANES == 3`.

##### [§](#examples-119)Examples

```rust
#![feature(portable_simd)]
use core::simd::prelude::*;

let short = &[1, 2, 3];
let (prefix, middle, suffix) = short.as_simd::<4>();
assert_eq!(middle, []); // Not enough elements for anything in the middle

// They might be split in any possible way between prefix and suffix
let it = prefix.iter().chain(suffix).copied();
assert_eq!(it.collect::<Vec<_>>(), vec![1, 2, 3]);

fn basic_simd_sum(x: &[f32]) -> f32 {
    use std::ops::Add;
    let (prefix, middle, suffix) = x.as_simd();
    let sums = f32x4::from_array([
        prefix.iter().copied().sum(),
        0.0,
        0.0,
        suffix.iter().copied().sum(),
    ]);
    let sums = middle.iter().copied().fold(sums, f32x4::add);
    sums.reduce_sum()
}

let numbers: Vec<f32> = (1..101).map(|x| x as _).collect();
assert_eq!(basic_simd_sum(&numbers[1..99]), 4949.0);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4690-4693)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

Splits a mutable slice into a mutable prefix, a middle of aligned SIMD types, and a mutable suffix.

This is a safe wrapper around [`slice::align_to_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.align_to_mut "method slice::align_to_mut"), so inherits the same guarantees as that method.

This is the mutable version of [`slice::as_simd`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_simd "method slice::as_simd"); see that for examples.

##### [§](#panics-38)Panics

This will panic if the size of the SIMD type is different from `LANES` times that of the scalar.

At the time of writing, the trait restrictions on `Simd<T, LANES>` keeps that from ever happening, as only power-of-two numbers of lanes are supported. It’s possible that, in the future, those restrictions might be lifted in a way that would make it possible to see panics from this method for something like `LANES == 3`.

1.82.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4728-4730)

Checks if the elements of this slice are sorted.

That is, for each element `a` and its following element `b`, `a <= b` must hold. If the slice yields exactly zero or one element, `true` is returned.

Note that if `Self::Item` is only `PartialOrd`, but not `Ord`, the above definition implies that this function returns `false` if any two consecutive items are not comparable.

##### [§](#examples-120)Examples

```rust
let empty: [i32; 0] = [];

assert!([1, 2, 2, 9].is_sorted());
assert!(![1, 3, 2, 4].is_sorted());
assert!([0].is_sorted());
assert!(empty.is_sorted());
assert!(![0.0, 1.0, f32::NAN].is_sorted());
```

1.82.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4771-4773)

Checks if the elements of this slice are sorted using the given comparator function.

Instead of using `PartialOrd::partial_cmp`, this function uses the given `compare` function to determine whether two elements are to be considered in sorted order.

##### [§](#examples-121)Examples

```rust
assert!([1, 2, 2, 9].is_sorted_by(|a, b| a <= b));
assert!(![1, 2, 2, 9].is_sorted_by(|a, b| a < b));

assert!([0].is_sorted_by(|a, b| true));
assert!([0].is_sorted_by(|a, b| false));

let empty: [i32; 0] = [];
assert!(empty.is_sorted_by(|a, b| false));
assert!(empty.is_sorted_by(|a, b| true));
```

1.82.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4795-4798)

Checks if the elements of this slice are sorted using the given key extraction function.

Instead of comparing the slice’s elements directly, this function compares the keys of the elements, as determined by `f`. Apart from that, it’s equivalent to [`is_sorted`](https://doc.rust-lang.org/std/primitive.slice.html#method.is_sorted "method slice::is_sorted"); see its documentation for more information.

##### [§](#examples-122)Examples

```rust
assert!(["c", "bb", "aaa"].is_sorted_by_key(|s| s.len()));
assert!(![-2i32, -1, 0, 3].is_sorted_by_key(|n| n.abs()));
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4854-4856)

Returns the index of the partition point according to the given predicate (the index of the first element of the second partition).

The slice is assumed to be partitioned according to the given predicate. This means that all elements for which the predicate returns true are at the start of the slice and all elements for which the predicate returns false are at the end. For example, `[7, 15, 3, 5, 4, 12, 6]` is partitioned under the predicate `x % 2 != 0` (all odd numbers are at the start, all even at the end).

If this slice is not partitioned, the returned result is unspecified and meaningless, as this method performs a kind of binary search.

See also [`binary_search`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search "method slice::binary_search"), [`binary_search_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by "method slice::binary_search_by"), and [`binary_search_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.binary_search_by_key "method slice::binary_search_by_key").

##### [§](#examples-123)Examples

```rust
let v = [1, 2, 3, 3, 5, 6, 7];
let i = v.partition_point(|&x| x < 5);

assert_eq!(i, 4);
assert!(v[..i].iter().all(|&x| x < 5));
assert!(v[i..].iter().all(|&x| !(x < 5)));
```

If all elements of the slice match the predicate, including if the slice is empty, then the length of the slice will be returned:

```rust
let a = [2, 4, 8];
assert_eq!(a.partition_point(|x| x < &100), a.len());
let a: [i32; 0] = [];
assert_eq!(a.partition_point(|x| x < &100), 0);
```

If you want to insert an item to a sorted vector, while maintaining sort order:

```rust
let mut s = vec![0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
let num = 42;
let idx = s.partition_point(|&x| x <= num);
s.insert(idx, num);
assert_eq!(s, [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

1.87.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4906-4909)

Removes the subslice corresponding to the given range and returns a reference to it.

Returns `None` and does not modify the slice if the given range is out of bounds.

Note that this method only accepts one-sided ranges such as `2..` or `..6`, but not `2..6`.

##### [§](#examples-124)Examples

Splitting off the first three elements of a slice:

```rust
let mut slice: &[_] = &['a', 'b', 'c', 'd'];
let mut first_three = slice.split_off(..3).unwrap();

assert_eq!(slice, &['d']);
assert_eq!(first_three, &['a', 'b', 'c']);
```

Splitting off a slice starting with the third element:

```rust
let mut slice: &[_] = &['a', 'b', 'c', 'd'];
let mut tail = slice.split_off(2..).unwrap();

assert_eq!(slice, &['a', 'b']);
assert_eq!(tail, &['c', 'd']);
```

Getting `None` when `range` is out of bounds:

```rust
let mut slice: &[_] = &['a', 'b', 'c', 'd'];

assert_eq!(None, slice.split_off(5..));
assert_eq!(None, slice.split_off(..5));
assert_eq!(None, slice.split_off(..=4));
let expected: &[char] = &['a', 'b', 'c', 'd'];
assert_eq!(Some(expected), slice.split_off(..4));
```

1.87.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#4972-4975)

Removes the subslice corresponding to the given range and returns a mutable reference to it.

Returns `None` and does not modify the slice if the given range is out of bounds.

Note that this method only accepts one-sided ranges such as `2..` or `..6`, but not `2..6`.

##### [§](#examples-125)Examples

Splitting off the first three elements of a slice:

```rust
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];
let mut first_three = slice.split_off_mut(..3).unwrap();

assert_eq!(slice, &mut ['d']);
assert_eq!(first_three, &mut ['a', 'b', 'c']);
```

Splitting off a slice starting with the third element:

```rust
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];
let mut tail = slice.split_off_mut(2..).unwrap();

assert_eq!(slice, &mut ['a', 'b']);
assert_eq!(tail, &mut ['c', 'd']);
```

Getting `None` when `range` is out of bounds:

```rust
let mut slice: &mut [_] = &mut ['a', 'b', 'c', 'd'];

assert_eq!(None, slice.split_off_mut(5..));
assert_eq!(None, slice.split_off_mut(..5));
assert_eq!(None, slice.split_off_mut(..=4));
let expected: &mut [_] = &mut ['a', 'b', 'c', 'd'];
assert_eq!(Some(expected), slice.split_off_mut(..4));
```

1.87.0 (const: [unstable](https://github.com/rust-lang/rust/issues/138539 "Tracking issue for const_split_off_first_last")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5010)

Removes the first element of the slice and returns a reference to it.

Returns `None` if the slice is empty.

##### [§](#examples-126)Examples

```rust
let mut slice: &[_] = &['a', 'b', 'c'];
let first = slice.split_off_first().unwrap();

assert_eq!(slice, &['b', 'c']);
assert_eq!(first, &'a');
```

1.87.0 (const: [unstable](https://github.com/rust-lang/rust/issues/138539 "Tracking issue for const_split_off_first_last")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5035)

Removes the first element of the slice and returns a mutable reference to it.

Returns `None` if the slice is empty.

##### [§](#examples-127)Examples

```rust
let mut slice: &mut [_] = &mut ['a', 'b', 'c'];
let first = slice.split_off_first_mut().unwrap();
*first = 'd';

assert_eq!(slice, &['b', 'c']);
assert_eq!(first, &'d');
```

1.87.0 (const: [unstable](https://github.com/rust-lang/rust/issues/138539 "Tracking issue for const_split_off_first_last")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5060)

Removes the last element of the slice and returns a reference to it.

Returns `None` if the slice is empty.

##### [§](#examples-128)Examples

```rust
let mut slice: &[_] = &['a', 'b', 'c'];
let last = slice.split_off_last().unwrap();

assert_eq!(slice, &['a', 'b']);
assert_eq!(last, &'c');
```

1.87.0 (const: [unstable](https://github.com/rust-lang/rust/issues/138539 "Tracking issue for const_split_off_first_last")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5085)

Removes the last element of the slice and returns a mutable reference to it.

Returns `None` if the slice is empty.

##### [§](#examples-129)Examples

```rust
let mut slice: &mut [_] = &mut ['a', 'b', 'c'];
let last = slice.split_off_last_mut().unwrap();
*last = 'd';

assert_eq!(slice, &['a', 'b']);
assert_eq!(last, &'d');
```

1.86.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5142-5147)

Returns mutable references to many indices at once, without doing any checks.

An index can be either a `usize`, a [`Range`](https://doc.rust-lang.org/std/ops/struct.Range.html "struct std::ops::Range") or a [`RangeInclusive`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html "struct std::ops::RangeInclusive"). Note that this method takes an array, so all indices must be of the same type. If passed an array of `usize`s this method gives back an array of mutable references to single elements, while if passed an array of ranges it gives back an array of mutable references to slices.

For a safe alternative see [`get_disjoint_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.get_disjoint_mut "method slice::get_disjoint_mut").

##### [§](#safety-14)Safety

Calling this method with overlapping or out-of-bounds indices is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting references are not used.

##### [§](#examples-130)Examples

```rust
let x = &mut [1, 2, 4];

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([0, 2]);
    *a *= 10;
    *b *= 100;
}
assert_eq!(x, &[10, 2, 400]);

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([0..1, 1..3]);
    a[0] = 8;
    b[0] = 88;
    b[1] = 888;
}
assert_eq!(x, &[8, 88, 888]);

unsafe {
    let [a, b] = x.get_disjoint_unchecked_mut([1..=2, 0..=0]);
    a[0] = 11;
    a[1] = 111;
    b[0] = 1;
}
assert_eq!(x, &[1, 11, 111]);
```

1.86.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5209-5214)

Returns mutable references to many indices at once.

An index can be either a `usize`, a [`Range`](https://doc.rust-lang.org/std/ops/struct.Range.html "struct std::ops::Range") or a [`RangeInclusive`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html "struct std::ops::RangeInclusive"). Note that this method takes an array, so all indices must be of the same type. If passed an array of `usize`s this method gives back an array of mutable references to single elements, while if passed an array of ranges it gives back an array of mutable references to slices.

Returns an error if any index is out-of-bounds, or if there are overlapping indices. An empty range is not considered to overlap if it is located at the beginning or at the end of another range, but is considered to overlap if it is located in the middle.

This method does a O(n^2) check to check that there are no overlapping indices, so be careful when passing many indices.

##### [§](#examples-131)Examples

```rust
let v = &mut [1, 2, 3];
if let Ok([a, b]) = v.get_disjoint_mut([0, 2]) {
    *a = 413;
    *b = 612;
}
assert_eq!(v, &[413, 2, 612]);

if let Ok([a, b]) = v.get_disjoint_mut([0..1, 1..3]) {
    a[0] = 8;
    b[0] = 88;
    b[1] = 888;
}
assert_eq!(v, &[8, 88, 888]);

if let Ok([a, b]) = v.get_disjoint_mut([1..=2, 0..=0]) {
    a[0] = 11;
    a[1] = 111;
    b[0] = 1;
}
assert_eq!(v, &[1, 11, 111]);
```

1.94.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5260)

Returns the index that an element reference points to.

Returns `None` if `element` does not point to the start of an element within the slice.

This method is useful for extending slice iterators like [`slice::split`](https://doc.rust-lang.org/std/primitive.slice.html#method.split "method slice::split").

Note that this uses pointer arithmetic and **does not compare elements**. To find the index of an element via comparison, use [`.iter().position()`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.position "method std::iter::Iterator::position") instead.

##### [§](#panics-39)Panics

Panics if `T` is zero-sized.

##### [§](#examples-132)Examples

Basic usage:

```rust
let nums: &[u32] = &[1, 7, 1, 1];
let num = &nums[2];

assert_eq!(num, &1);
assert_eq!(nums.element_offset(num), Some(2));
```

Returning `None` with an unaligned element:

```rust
let arr: &[[u32; 2]] = &[[0, 1], [2, 3]];
let flat_arr: &[u32] = arr.as_flattened();

let ok_elm: &[u32; 2] = flat_arr[0..2].try_into().unwrap();
let weird_elm: &[u32; 2] = flat_arr[1..3].try_into().unwrap();

assert_eq!(ok_elm, &[0, 1]);
assert_eq!(weird_elm, &[1, 2]);

assert_eq!(arr.element_offset(ok_elm), Some(0)); // Points to element 0
assert_eq!(arr.element_offset(weird_elm), None); // Points between element 0 and 1
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5314)

🔬This is a nightly-only experimental API. (`substr_range` [#126769](https://github.com/rust-lang/rust/issues/126769))

Returns the range of indices that a subslice points to.

Returns `None` if `subslice` does not point within the slice or if it is not aligned with the elements in the slice.

This method **does not compare elements**. Instead, this method finds the location in the slice that `subslice` was obtained from. To find the index of a subslice via comparison, instead use [`.windows()`](https://doc.rust-lang.org/std/primitive.slice.html#method.windows "method slice::windows")[`.position()`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.position "method std::iter::Iterator::position").

This method is useful for extending slice iterators like [`slice::split`](https://doc.rust-lang.org/std/primitive.slice.html#method.split "method slice::split").

Note that this may return a false positive (either `Some(0..0)` or `Some(self.len()..self.len())`) if `subslice` has a length of zero and points to the beginning or end of another, separate, slice.

##### [§](#panics-40)Panics

Panics if `T` is zero-sized.

##### [§](#examples-133)Examples

Basic usage:

```rust
#![feature(substr_range)]

let nums = &[0, 5, 10, 0, 0, 5];

let mut iter = nums
    .split(|t| *t == 0)
    .map(|n| nums.subslice_range(n).unwrap());

assert_eq!(iter.next(), Some(0..0));
assert_eq!(iter.next(), Some(1..3));
assert_eq!(iter.next(), Some(4..4));
assert_eq!(iter.next(), Some(5..6));
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5341)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same slice `&[T]`.

This method is redundant when used directly on `&[T]`, but it helps dereferencing other “container” types to slices, for example `Box<[T]>` or `Arc<[T]>`.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5352)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same slice `&mut [T]`.

This method is redundant when used directly on `&mut [T]`, but it helps dereferencing other “container” types to slices, for example `Box<[T]>` or `MutexGuard<[T]>`.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5357)[§](#impl-%5BMaybeUninit%3CT%3E%5D-1)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5397)

🔬This is a nightly-only experimental API. (`align_to_uninit_mut` [#139062](https://github.com/rust-lang/rust/issues/139062))

Transmutes the mutable uninitialized slice to a mutable uninitialized slice of another type, ensuring alignment of the types is maintained.

This is a safe wrapper around [`slice::align_to_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.align_to_mut "method slice::align_to_mut"), so inherits the same guarantees as that method.

##### [§](#examples-134)Examples

```rust
#![feature(align_to_uninit_mut)]
use std::mem::MaybeUninit;

pub struct BumpAllocator<'scope> {
    memory: &'scope mut [MaybeUninit<u8>],
}

impl<'scope> BumpAllocator<'scope> {
    pub fn new(memory: &'scope mut [MaybeUninit<u8>]) -> Self {
        Self { memory }
    }
    pub fn try_alloc_uninit<T>(&mut self) -> Option<&'scope mut MaybeUninit<T>> {
        let first_end = self.memory.as_ptr().align_offset(align_of::<T>()) + size_of::<T>();
        let prefix = self.memory.split_off_mut(..first_end)?;
        Some(&mut prefix.align_to_uninit_mut::<T>().1[0])
    }
    pub fn try_alloc_u32(&mut self, value: u32) -> Option<&'scope mut u32> {
        let uninit = self.try_alloc_uninit()?;
        Some(uninit.write(value))
    }
}

let mut memory = [MaybeUninit::<u8>::uninit(); 10];
let mut allocator = BumpAllocator::new(&mut memory);
let v = allocator.try_alloc_u32(42);
assert_eq!(v, Some(&mut 42));
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5406)[§](#impl-%5B%5BT;+N%5D%5D)

1.80.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5440)

Takes a `&[[T; N]]`, and flattens it to a `&[T]`.

For the opposite operation, see [`as_chunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks "method slice::as_chunks") and [`as_rchunks`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks "method slice::as_rchunks").

##### [§](#panics-41)Panics

This panics if the length of the resulting slice would overflow a `usize`.

This is only possible when flattening a slice of arrays of zero-sized types, and thus tends to be irrelevant in practice. If `size_of::<T>() > 0`, this will never panic.

##### [§](#examples-135)Examples

```rust
assert_eq!([[1, 2, 3], [4, 5, 6]].as_flattened(), &[1, 2, 3, 4, 5, 6]);

assert_eq!(
    [[1, 2, 3], [4, 5, 6]].as_flattened(),
    [[1, 2], [3, 4], [5, 6]].as_flattened(),
);

let slice_of_empty_arrays: &[[i32; 0]] = &[[], [], [], [], []];
assert!(slice_of_empty_arrays.as_flattened().is_empty());

let empty_slice_of_arrays: &[[u32; 10]] = &[];
assert!(empty_slice_of_arrays.as_flattened().is_empty());
```

1.80.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5482)

Takes a `&mut [[T; N]]`, and flattens it to a `&mut [T]`.

For the opposite operation, see [`as_chunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_chunks_mut "method slice::as_chunks_mut") and [`as_rchunks_mut`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_rchunks_mut "method slice::as_rchunks_mut").

##### [§](#panics-42)Panics

This panics if the length of the resulting slice would overflow a `usize`.

This is only possible when flattening a slice of arrays of zero-sized types, and thus tends to be irrelevant in practice. If `size_of::<T>() > 0`, this will never panic.

##### [§](#examples-136)Examples

```rust
fn add_5_to_all(slice: &mut [i32]) {
    for i in slice {
        *i += 5;
    }
}

let mut array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
add_5_to_all(array.as_flattened_mut());
assert_eq!(array, [[6, 7, 8], [9, 10, 11], [12, 13, 14]]);
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5495)[§](#impl-%5Bf32%5D)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5518)

🔬This is a nightly-only experimental API. (`sort_floats` [#93396](https://github.com/rust-lang/rust/issues/93396))

Sorts the slice of floats.

This sort is in-place (i.e. does not allocate), *O*(*n* * log(*n*)) worst-case, and uses the ordering defined by [`f32::total_cmp`](https://doc.rust-lang.org/std/primitive.f32.html#method.total_cmp "method f32::total_cmp").

##### [§](#current-implementation-6)Current implementation

This uses the same sorting algorithm as [`sort_unstable_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by "method slice::sort_unstable_by").

##### [§](#examples-137)Examples

```rust
#![feature(sort_floats)]
let mut v = [2.6, -5e-8, f32::NAN, 8.29, f32::INFINITY, -1.0, 0.0, -f32::INFINITY, -0.0];

v.sort_floats();
let sorted = [-f32::INFINITY, -1.0, -5e-8, -0.0, 0.0, 2.6, 8.29, f32::INFINITY, f32::NAN];
assert_eq!(&v[..8], &sorted[..8]);
assert!(v[8].is_nan());
```

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5523)[§](#impl-%5Bf64%5D)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5546)

🔬This is a nightly-only experimental API. (`sort_floats` [#93396](https://github.com/rust-lang/rust/issues/93396))

Sorts the slice of floats.

This sort is in-place (i.e. does not allocate), *O*(*n* * log(*n*)) worst-case, and uses the ordering defined by [`f64::total_cmp`](https://doc.rust-lang.org/std/primitive.f64.html#method.total_cmp "method f64::total_cmp").

##### [§](#current-implementation-7)Current implementation

This uses the same sorting algorithm as [`sort_unstable_by`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable_by "method slice::sort_unstable_by").

##### [§](#examples-138)Examples

```rust
#![feature(sort_floats)]
let mut v = [2.6, -5e-8, f64::NAN, 8.29, f64::INFINITY, -1.0, 0.0, -f64::INFINITY, -0.0];

v.sort_floats();
let sorted = [-f64::INFINITY, -1.0, -5e-8, -0.0, 0.0, 2.6, 8.29, f64::INFINITY, f64::NAN];
assert_eq!(&v[..8], &sorted[..8]);
assert!(v[8].is_nan());
```

[Source](https://doc.rust-lang.org/src/core/str/lossy.rs.html#8)[§](#impl-%5Bu8%5D-1)

1.79.0 · [Source](https://doc.rust-lang.org/src/core/str/lossy.rs.html#45)

Creates an iterator over the contiguous valid UTF-8 ranges of this slice, and the non-UTF-8 fragments in between.

See the [`Utf8Chunk`](https://doc.rust-lang.org/std/str/struct.Utf8Chunk.html "struct std::str::Utf8Chunk") type for documentation of the items yielded by this iterator.

##### [§](#examples-139)Examples

This function formats arbitrary but mostly-UTF-8 bytes into Rust source code in the form of a C-string literal (`c"..."`).

```rust
use std::fmt::Write as _;

pub fn cstr_literal(bytes: &[u8]) -> String {
    let mut repr = String::new();
    repr.push_str("c\"");
    for chunk in bytes.utf8_chunks() {
        for ch in chunk.valid().chars() {
            // Escapes \0, \t, \r, \n, \\, \', \", and uses \u{...} for non-printable characters.
            write!(repr, "{}", ch.escape_debug()).unwrap();
        }
        for byte in chunk.invalid() {
            write!(repr, "\\x{:02X}", byte).unwrap();
        }
    }
    repr.push('"');
    repr
}

fn main() {
    let lit = cstr_literal(b"\xferris the \xf0\x9f\xa6\x80\x07");
    let expected = stringify!(c"\xFErris the 🦀\u{7}");
    assert_eq!(lit, expected);
}
```

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#69)[§](#impl-%5BT%5D-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#131-133)

Sorts the slice in ascending order, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*n* * log(*n*)) worst-case.

If the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

When applicable, unstable sorting is preferred because it is generally faster than stable sorting and it doesn’t allocate auxiliary memory. See [`sort_unstable`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_unstable "method slice::sort_unstable"). The exception are partially sorted slices, which may be better served with `slice::sort`.

Sorting types that only implement [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") such as [`f32`](https://doc.rust-lang.org/std/primitive.f32.html "primitive f32") and [`f64`](https://doc.rust-lang.org/std/primitive.f64.html "primitive f64") require additional precautions. For example, `f32::NAN != f32::NAN`, which doesn’t fulfill the reflexivity requirement of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord"). By using an alternative comparison function with `slice::sort_by` such as [`f32::total_cmp`](https://doc.rust-lang.org/std/primitive.f32.html#method.total_cmp "method f32::total_cmp") or [`f64::total_cmp`](https://doc.rust-lang.org/std/primitive.f64.html#method.total_cmp "method f64::total_cmp") that defines a [total order](https://en.wikipedia.org/wiki/Total_order) users can sort slices containing floating-point values. Alternatively, if all values in the slice are guaranteed to be in a subset for which [`PartialOrd::partial_cmp`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp "method std::cmp::PartialOrd::partial_cmp") forms a [total order](https://en.wikipedia.org/wiki/Total_order), it’s possible to sort the slice with `sort_by(|a, b| a.partial_cmp(b).unwrap())`.

##### [§](#current-implementation-8)Current implementation

The current implementation is based on [driftsort](https://github.com/Voultapher/driftsort) by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### [§](#panics-43)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `T` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation itself panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### [§](#examples-140)Examples

```rust
let mut v = [4, -5, 1, -3, 2];

v.sort();
assert_eq!(v, [-5, -3, 1, 2, 4]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#192-194)

Sorts the slice in ascending order with a comparison function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*n* * log(*n*)) worst-case.

If the comparison function `compare` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For example `|a, b| (a - b).cmp(a)` is a comparison function that is neither transitive nor reflexive nor total, `a < b < c < a` with `a = 1, b = 2, c = 3`. For more information and examples see the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") documentation.

##### [§](#current-implementation-9)Current implementation

The current implementation is based on [driftsort](https://github.com/Voultapher/driftsort) by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### [§](#panics-44)Panics

May panic if `compare` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if `compare` itself panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### [§](#examples-141)Examples

```rust
let mut v = [4, -5, 1, -3, 2];
v.sort_by(|a, b| a.cmp(b));
assert_eq!(v, [-5, -3, 1, 2, 4]);

// reverse sorting
v.sort_by(|a, b| b.cmp(a));
assert_eq!(v, [4, 2, 1, -3, -5]);
```

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#247-250)

Sorts the slice in ascending order with a key extraction function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*m* * *n* * log(*n*)) worst-case, where the key function is *O*(*m*).

If the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

##### [§](#current-implementation-10)Current implementation

The current implementation is based on [driftsort](https://github.com/Voultapher/driftsort) by Orson Peters and Lukas Bergdoll, which combines the fast average case of quicksort with the fast worst case and partial run detection of mergesort, achieving linear time on fully sorted and reversed inputs. On inputs with k distinct elements, the expected time to sort the data is *O*(*n* * log(*k*)).

The auxiliary memory allocation behavior depends on the input length. Short slices are handled without allocation, medium sized slices allocate `self.len()` and beyond that it clamps at `self.len() / 2`.

##### [§](#panics-45)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation or the key-function `f` panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### [§](#examples-142)Examples

```rust
let mut v = [4i32, -5, 1, -3, 2];

v.sort_by_key(|k| k.abs());
assert_eq!(v, [1, 2, -3, 4, -5]);
```

1.34.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#312-315)

Sorts the slice in ascending order with a key extraction function, preserving initial order of equal elements.

This sort is stable (i.e., does not reorder equal elements) and *O*(*m* * *n* + *n* * log(*n*)) worst-case, where the key function is *O*(*m*).

During sorting, the key function is called at most once per element, by using temporary storage to remember the results of key evaluation. The order of calls to the key function is unspecified and may change in future versions of the standard library.

If the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), the function may panic; even if the function exits normally, the resulting order of elements in the slice is unspecified. See also the note on panicking below.

For simple key functions (e.g., functions that are property accesses or basic operations), [`sort_by_key`](https://doc.rust-lang.org/std/primitive.slice.html#method.sort_by_key "method slice::sort_by_key") is likely to be faster.

##### [§](#current-implementation-11)Current implementation

The current implementation is based on [instruction-parallel-network sort](https://github.com/Voultapher/sort-research-rs/tree/main/ipnsort) by Lukas Bergdoll, which combines the fast average case of randomized quicksort with the fast worst case of heapsort, while achieving linear time on fully sorted and reversed inputs. And *O*(*k* * log(*n*)) where *k* is the number of distinct elements in the input. It leverages superscalar out-of-order execution capabilities commonly found in CPUs, to efficiently perform the operation.

In the worst case, the algorithm allocates temporary storage in a `Vec<(K, usize)>` the length of the slice.

##### [§](#panics-46)Panics

May panic if the implementation of [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for `K` does not implement a [total order](https://en.wikipedia.org/wiki/Total_order), or if the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") implementation panics.

All safe functions on slices preserve the invariant that even if the function panics, all original elements will remain in the slice and any possible modifications via interior mutability are observed in the input. This ensures that recovery code (for instance inside of a `Drop` or following a `catch_unwind`) will still have access to all the original elements. For instance, if the slice belongs to a `Vec`, the `Vec::drop` method will be able to dispose of all contained elements.

##### [§](#examples-143)Examples

```rust
let mut v = [4i32, -5, 1, -3, 2, 10];

// Strings are sorted by lexicographical order.
v.sort_by_cached_key(|k| k.to_string());
assert_eq!(v, [-3, -5, 1, 10, 2, 4]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#372-374)

Copies `self` into a new `Vec`.

##### [§](#examples-144)Examples

```rust
let s = [10, 40, 30];
let x = s.to_vec();
// Here, `s` and `x` can be modified independently.
```

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#396-398)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Copies `self` into a new `Vec` with an allocator.

##### [§](#examples-145)Examples

```rust
#![feature(allocator_api)]

use std::alloc::System;

let s = [10, 40, 30];
let x = s.to_vec_in(System);
// Here, `s` and `x` can be modified independently.
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#480)

Converts `self` into a vector without clones or allocation.

The resulting vector can be converted back into a box via `Vec<T>`’s `into_boxed_slice` method.

##### [§](#examples-146)Examples

```rust
let s: Box<[i32]> = Box::new([10, 40, 30]);
let x = s.into_vec();
// `s` cannot be used anymore because it has been converted into `x`.

assert_eq!(x, vec![10, 40, 30]);
```

1.40.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#509-511)

Creates a vector by copying a slice `n` times.

##### [§](#panics-47)Panics

This function will panic if the capacity would overflow.

##### [§](#examples-147)Examples

```rust
assert_eq!([1, 2].repeat(3), vec![1, 2, 1, 2, 1, 2]);
```

A panic upon overflow:

[ⓘ](# "This example panics")

```rust
// this will panic at runtime
b"0123456789abcdef".repeat(usize::MAX);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#577-579)

Flattens a slice of `T` into a single value `Self::Output`.

##### [§](#examples-148)Examples

```rust
assert_eq!(["hello", "world"].concat(), "helloworld");
assert_eq!([[1, 2], [3, 4]].concat(), [1, 2, 3, 4]);
```

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#596-598)

Flattens a slice of `T` into a single value `Self::Output`, placing a given separator between each.

##### [§](#examples-149)Examples

```rust
assert_eq!(["hello", "world"].join(" "), "hello world");
assert_eq!([[1, 2], [3, 4]].join(&0), [1, 2, 0, 3, 4]);
assert_eq!([[1, 2], [3, 4]].join(&[0, 0][..]), [1, 2, 0, 0, 3, 4]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#616-618)

👎Deprecated since 1.3.0: renamed to join

Flattens a slice of `T` into a single value `Self::Output`, placing a given separator between each.

##### [§](#examples-150)Examples

```rust
assert_eq!(["hello", "world"].connect(" "), "hello world");
assert_eq!([[1, 2], [3, 4]].connect(&0), [1, 2, 0, 3, 4]);
```

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#624)[§](#impl-%5Bu8%5D-2)

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#640)

Returns a vector containing a copy of this slice where each byte is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`make_ascii_uppercase`](https://doc.rust-lang.org/std/primitive.slice.html#method.make_ascii_uppercase "method slice::make_ascii_uppercase").

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#661)

Returns a vector containing a copy of this slice where each byte is mapped to its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`make_ascii_lowercase`](https://doc.rust-lang.org/std/primitive.slice.html#method.make_ascii_lowercase "method slice::make_ascii_lowercase").

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ascii.rs.html#198-202)[§](#impl-AsciiExt-for-%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#199)[§](#associatedtype.Owned-1)

👎Deprecated since 1.26.0: use inherent methods instead

Container type for copied ASCII characters.

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.is_ascii-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks if the value is within the ASCII range. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.is_ascii)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.to_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII upper case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.to_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII lower case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_lowercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.eq_ignore_ascii_case-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks that two values are an ASCII case-insensitive match. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.eq_ignore_ascii_case)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.make_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII upper case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#201)[§](#method.make_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII lower case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_lowercase)

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1570)[§](#impl-AsMut%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1572)[§](#method.as_mut)

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#854)[§](#impl-AsMut%3C%5BT%5D%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#856)[§](#method.as_mut-1)

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#214)[§](#impl-AsMut%3C%5BT%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#216)[§](#method.as_mut-2)

Converts this type into a mutable reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1007-1009)[§](#impl-AsMut%3C%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1012)[§](#method.as_mut-4)

Converts this type into a mutable reference of the (usually inferred) input type.

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4270)[§](#impl-AsMut%3C%5BT%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4271)[§](#method.as_mut-6)

Converts this type into a mutable reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#248)[§](#impl-AsMut%3C%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#250)[§](#method.as_mut-3)

Converts this type into a mutable reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#120)[§](#impl-AsMut%3C%5Bu8%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#122)[§](#method.as_mut-5)

Converts this type into a mutable reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#709)[§](#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#711)[§](#method.as_ref-5)

Converts this type into a shared reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#701)[§](#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#703)[§](#method.as_ref-4)

Converts this type into a shared reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1553)[§](#impl-AsRef%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1555)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#845)[§](#impl-AsRef%3C%5BT%5D%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#847)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#205)[§](#impl-AsRef%3C%5BT%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#207)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/drain.rs.html#139)[§](#impl-AsRef%3C%5BT%5D%3E-for-Drain%3C'a,+T,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/drain.rs.html#140)[§](#method.as_ref-13)

Converts this type into a shared reference of the (usually inferred) input type.

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/into_iter.rs.html#197)[§](#impl-AsRef%3C%5BT%5D%3E-for-IntoIter%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/into_iter.rs.html#198)[§](#method.as_ref-14)

Converts this type into a shared reference of the (usually inferred) input type.

1.13.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#161)[§](#impl-AsRef%3C%5BT%5D%3E-for-Iter%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#163)[§](#method.as_ref-6)

Converts this type into a shared reference of the (usually inferred) input type.

1.53.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#357)[§](#impl-AsRef%3C%5BT%5D%3E-for-IterMut%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#359)[§](#method.as_ref-7)

Converts this type into a shared reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#997-999)[§](#impl-AsRef%3C%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1002)[§](#method.as_ref-9)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4263)[§](#impl-AsRef%3C%5BT%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4264)[§](#method.as_ref-15)

Converts this type into a shared reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#219)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#221)[§](#method.as_ref-3)

Converts this type into a shared reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#104)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#106)[§](#method.as_ref-10)

Converts this type into a shared reference of the (usually inferred) input type.

1.55.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3555)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-Drain%3C'a%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3556)[§](#method.as_ref-12)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3099)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3101)[§](#method.as_ref-11)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3148)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3150)[§](#method.as_ref-8)

Converts this type into a shared reference of the (usually inferred) input type.

1.4.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#223)[§](#impl-Borrow%3C%5BT%5D%3E-for-%5BT;+N%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#791)[§](#impl-Borrow%3C%5BT%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#263)[§](#impl-Borrow%3C%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#136)[§](#impl-Borrow%3C%5Bu8%5D%3E-for-ByteString)

1.4.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#231)[§](#impl-BorrowMut%3C%5BT%5D%3E-for-%5BT;+N%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#798)[§](#impl-BorrowMut%3C%5BT%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#274)[§](#impl-BorrowMut%3C%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#155)[§](#impl-BorrowMut%3C%5Bu8%5D%3E-for-ByteString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#406-416)[§](#impl-BufRead-for-%26%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#408-410)[§](#method.fill_buf)

Returns the contents of the internal buffer, filling it with more data, via `Read` methods, if empty. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#tymethod.fill_buf)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#413-415)[§](#method.consume)

Marks the given `amount` of additional bytes from the internal buffer as having been read. Subsequent calls to `read` only return bytes that have not been marked as read. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#tymethod.consume)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2435-2437)[§](#method.has_data_left)

🔬This is a nightly-only experimental API. (`buf_read_has_data_left` [#86423](https://github.com/rust-lang/rust/issues/86423))

Checks if there is any data left to be `read`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.has_data_left)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2494-2496)[§](#method.read_until)

Reads all bytes into `buf` until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_until)

1.83.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2559-2561)[§](#method.skip_until)

Skips all bytes until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.skip_until)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2627-2632)[§](#method.read_line)

Reads all bytes until a newline (the `0xA` byte) is reached, and append them to the provided `String` buffer. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2665-2670)[§](#method.split-1)

Returns an iterator over the contents of this reader split on the byte `byte`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.split)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2702-2707)[§](#method.lines)

Returns an iterator over the lines of this reader. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#2040)[§](#impl-Clone-for-Box%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#2064)[§](#method.clone_from)

Copies `source`’s contents into `self` without creating a new allocation, so long as the two are of the same length.

##### [§](#examples-152)Examples

```rust
let x = Box::new([5, 6, 7]);
let mut y = Box::new([8, 9, 10]);
let yp: *const [i32] = &*y;

y.clone_from(&x);

// The value is the same
assert_eq!(x, y);

// And no allocation occurred
assert_eq!(yp, &*y);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#2041)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#556)[§](#impl-CloneToUninit-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#559)[§](#method.clone_to_uninit)

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#726)[§](#impl-Concat%3CT%3E-for-%5BV%5D)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#727)[§](#associatedtype.Output-25)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#729)[§](#method.concat-1)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#62)[§](#impl-Concat%3Cstr%3E-for-%5BS%5D)

Note: `str` in `Concat<str>` is not meaningful here. This type parameter of the trait only exists to enable another impl.

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#63)[§](#associatedtype.Output-26)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#65)[§](#method.concat-2)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#3114)[§](#impl-Debug-for-%5BT%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5628)[§](#impl-Default-for-%26%5BT%5D)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5637)[§](#impl-Default-for-%26mut+%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5639)[§](#method.default-1)

Creates a mutable empty slice.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1952)[§](#impl-Default-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1955)[§](#method.default-2)

Creates an empty `[T]` inside a `Box`.

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3891)[§](#impl-From%3C%26%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3903)[§](#method.from-10)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-3)Example

```rust
let original: &[i32] = &[1, 2, 3];
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#61)[§](#impl-From%3C%26%5BT%5D%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#76)[§](#method.from-2)

Converts a `&[T]` into a `Box<[T]>`

This conversion allocates on the heap and performs a copy of `slice` and its contents.

##### [§](#examples-153)Examples

```rust
// create a &[u8] which will be used to create a Box<[u8]>
let slice: &[u8] = &[104, 101, 108, 108, 111];
let boxed_slice: Box<[u8]> = Box::from(slice);

println!("{boxed_slice:?}");
```

1.8.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#5)[§](#impl-From%3C%26%5BT%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#12)[§](#method.from-12)

Creates a [`Borrowed`](https://doc.rust-lang.org/std/borrow/enum.Cow.html#variant.Borrowed "variant std::borrow::Cow::Borrowed") variant of [`Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow") from a slice.

This conversion does not allocate or clone the data.

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2857)[§](#impl-From%3C%26%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2869)[§](#method.from-8)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-1)Example

```rust
let original: &[i32] = &[1, 2, 3];
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4278)[§](#impl-From%3C%26%5BT%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4286)[§](#method.from-13)

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### [§](#examples-157)Examples

```rust
assert_eq!(Vec::from(&[1, 2, 3][..]), vec![1, 2, 3]);
```

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#65)[§](#impl-From%3C%26mut+%5BMaybeUninit%3Cu8%3E%5D%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from an uninitialized buffer.

Use `set_init` if part of the buffer is known to be already initialized.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#67)[§](#method.from-1)

Converts to this type from the input type.

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3910)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3923)[§](#method.from-11)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-4)Example

```rust
let mut original = [1, 2, 3];
let original: &mut [i32] = &mut original;
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#83)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#99)[§](#method.from-3)

Converts a `&mut [T]` into a `Box<[T]>`

This conversion allocates on the heap and performs a copy of `slice` and its contents.

##### [§](#examples-154)Examples

```rust
// create a &mut [u8] which will be used to create a Box<[u8]>
let mut array = [104, 101, 108, 108, 111];
let slice: &mut [u8] = &mut array;
let boxed_slice: Box<[u8]> = Box::from(slice);

println!("{boxed_slice:?}");
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2876)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2889)[§](#method.from-9)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-2)Example

```rust
let mut original = [1, 2, 3];
let original: &mut [i32] = &mut original;
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4293)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4301)[§](#method.from-14)

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### [§](#examples-158)Examples

```rust
assert_eq!(Vec::from(&mut [1, 2, 3][..]), vec![1, 2, 3]);
```

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#48)[§](#impl-From%3C%26mut+%5Bu8%5D%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from a fully initialized slice.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#50)[§](#method.from)

Converts to this type from the input type.

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#226)[§](#impl-From%3C%5BT;+N%5D%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#237)[§](#method.from-6)

Converts a `[T; N]` into a `Box<[T]>`

This conversion moves the array to newly heap-allocated memory.

##### [§](#examples-156)Examples

```rust
let boxed: Box<[u8]> = Box::from([4, 2]);
println!("{boxed:?}");
```

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#614)[§](#impl-From%3CBox%3CByteStr%3E%3E-for-Box%3C%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#616)[§](#method.from-7)

Converts to this type from the input type.

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#200)[§](#impl-From%3CBox%3Cstr,+A%3E%3E-for-Box%3C%5Bu8%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#218)[§](#method.from-5)

Converts a `Box<str>` into a `Box<[u8]>`

This conversion does not allocate on the heap and happens in place.

##### [§](#examples-155)Examples

```rust
// create a Box<str> which will be used to create a Box<[u8]>
let boxed: Box<str> = Box::from("hello");
let boxed_str: Box<[u8]> = Box::from(boxed);

// create a &[u8] which will be used to create a Box<[u8]>
let slice: &[u8] = &[104, 101, 108, 108, 111];
let boxed_slice = Box::from(slice);

assert_eq!(boxed_slice, boxed_str);
```

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#106)[§](#impl-From%3CCow%3C'_,+%5BT%5D%3E%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#114)[§](#method.from-4)

Converts a `Cow<'_, [T]>` into a `Box<[T]>`

When `cow` is the `Cow::Borrowed` variant, this conversion allocates on the heap and copies the underlying slice. Otherwise, it will try to reuse the owned `Vec`’s allocation.

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4395)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Box%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4416)[§](#method.from-15)

Converts a vector into a boxed slice.

Before doing the conversion, this method discards excess capacity like [`Vec::shrink_to_fit`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.shrink_to_fit "method std::vec::Vec::shrink_to_fit").

##### [§](#examples-159)Examples

```rust
assert_eq!(Box::from(vec![1, 2, 3]), vec![1, 2, 3].into_boxed_slice());
```

Any excess capacity is removed:

```rust
let mut vec = Vec::with_capacity(10);
vec.extend([1, 2, 3]);

assert_eq!(Box::from(vec), vec![1, 2, 3].into_boxed_slice());
```

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#288)[§](#impl-FromIterator%3C%26%5Bu8%5D%3E-for-ByteString)

1.32.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#142)[§](#impl-FromIterator%3CI%3E-for-Box%3C%5BI%5D%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#931)[§](#impl-Hash-for-%5BT%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#11-13)[§](#impl-Index%3CI%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#15)[§](#associatedtype.Output-24)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#18)[§](#method.index-24)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#25-27)[§](#impl-IndexMut%3CI%3E-for-%5BT%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#21)[§](#impl-IntoIterator-for-%26%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#22)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#23)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#25)[§](#method.into_iter)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#123)[§](#impl-IntoIterator-for-%26Box%3C%5BI%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#124)[§](#associatedtype.IntoIter-3)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#125)[§](#associatedtype.Item-4)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#126)[§](#method.into_iter-3)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#31)[§](#impl-IntoIterator-for-%26mut+%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#32)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#33)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#35)[§](#method.into_iter-1)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#132)[§](#impl-IntoIterator-for-%26mut+Box%3C%5BI%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#133)[§](#associatedtype.IntoIter-4)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#134)[§](#associatedtype.Item-5)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#135)[§](#method.into_iter-4)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#114)[§](#impl-IntoIterator-for-Box%3C%5BI%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#115)[§](#associatedtype.IntoIter-2)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#116)[§](#associatedtype.Item-3)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#117)[§](#method.into_iter-2)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#764)[§](#impl-Join%3C%26%5BT%5D%3E-for-%5BV%5D)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#765)[§](#associatedtype.Output-28)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#767)[§](#method.join-2)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1661-1675)[§](#impl-Join%3C%26OsStr%3E-for-%5BS%5D)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1662)[§](#associatedtype.Output-30)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1664-1674)[§](#method.join-4)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#741)[§](#impl-Join%3C%26T%3E-for-%5BV%5D)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#742)[§](#associatedtype.Output-27)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#744)[§](#method.join-1)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#72)[§](#impl-Join%3C%26str%3E-for-%5BS%5D)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#73)[§](#associatedtype.Output-29)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#75)[§](#method.join-3)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#36)[§](#impl-Ord-for-%5BT%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#65-67)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#70)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#74)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#32)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#32)[§](#method.eq-23)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#32)[§](#method.ne-23)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#23)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#23)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#23)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3586)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3586)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#133)[§](#impl-PartialEq%3C%26%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#133)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#523)[§](#impl-PartialEq%3C%26%5Bu8%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#523)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#97-99)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#102)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#106)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#34)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#34)[§](#method.eq-24)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#34)[§](#method.ne-24)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#24)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#24)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#24)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3587)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3587)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#13-15)[§](#impl-PartialEq%3C%5BU%5D%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#18)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#21-23)[§](#impl-PartialEq%3C%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#26)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#33)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.48.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#27)[§](#impl-PartialEq%3C%5BU%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#27)[§](#method.eq-21)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#27)[§](#method.ne-21)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#81-83)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%26%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#86)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#90)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#113-115)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%26mut+%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#118)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#122)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#43-45)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#48)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#55)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#131)[§](#impl-PartialEq%3C%5Bu8%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#131)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#521)[§](#impl-PartialEq%3C%5Bu8%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#521)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#133)[§](#impl-PartialEq%3CByteStr%3E-for-%26%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#133)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#131)[§](#impl-PartialEq%3CByteStr%3E-for-%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#131)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#523)[§](#impl-PartialEq%3CByteString%3E-for-%26%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#523)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#521)[§](#impl-PartialEq%3CByteString%3E-for-%5Bu8%5D)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#521)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#25)[§](#impl-PartialEq%3CVec%3CU,+A%3E%3E-for-%26%5BT%5D)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#25)[§](#method.eq-19)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#25)[§](#method.ne-19)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#26)[§](#impl-PartialEq%3CVec%3CU,+A%3E%3E-for-%26mut+%5BT%5D)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#26)[§](#method.eq-20)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#26)[§](#method.ne-20)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.48.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#28)[§](#impl-PartialEq%3CVec%3CU,+A%3E%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#28)[§](#method.eq-22)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#28)[§](#method.ne-22)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#55)[§](#impl-PartialOrd-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#57)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#61)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#73)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#77)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#81)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#892)[§](#impl-Pattern-for-%26%5Bchar%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the slice.

#### [§](#examples-151)Examples

```rust
assert_eq!("Hello world".find(&['o', 'l'][..]), Some(2));
assert_eq!("Hello world".find(&['h', 'w'][..]), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#165)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#298-403)[§](#impl-Read-for-%26%5Bu8%5D)

Read is implemented for `&[u8]` by copying from the slice.

Note that reading updates the slice to point to the yet unread part. The slice will be empty when EOF is reached.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#300-315)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#318-326)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#329-339)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#342-344)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#347-367)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#370-383)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf_exact)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#386-392)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#395-402)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1200-1205)[§](#method.chain)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1239-1244)[§](#method.take)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_array)

1.53.0 · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1041)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-%28Bound%3Cusize%3E,+Bound%3Cusize%3E%29)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1042)[§](#associatedtype.Output-23)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1045)[§](#method.get-24)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1050)[§](#method.get_mut-24)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1055)[§](#method.get_unchecked-24)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1061)[§](#method.get_unchecked_mut-24)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1067)[§](#method.index-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#1072)[§](#method.index_mut-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#84)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRange%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#85)[§](#associatedtype.Output-1)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#87)[§](#method.get-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#93)[§](#method.get_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#99)[§](#method.get_unchecked-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#106)[§](#method.get_unchecked_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#113)[§](#method.index-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#119)[§](#method.index_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#127)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRange%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#128)[§](#associatedtype.Output-2)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#130)[§](#method.get-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#136)[§](#method.get_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#142)[§](#method.get_unchecked-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#149)[§](#method.get_unchecked_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#156)[§](#method.index-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#162)[§](#method.index_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#256)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFrom%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#257)[§](#associatedtype.Output-5)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#259)[§](#method.get-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#263)[§](#method.get_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#267)[§](#method.get_unchecked-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#272)[§](#method.get_unchecked_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#277)[§](#method.index-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#281)[§](#method.index_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#287)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFrom%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#288)[§](#associatedtype.Output-6)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#290)[§](#method.get-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#294)[§](#method.get_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#298)[§](#method.get_unchecked-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#303)[§](#method.get_unchecked_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#308)[§](#method.index-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#312)[§](#method.index_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#411)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFull%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#412)[§](#associatedtype.Output-10)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#414)[§](#method.get-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#418)[§](#method.get_mut-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#422)[§](#method.get_unchecked-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#427)[§](#method.get_unchecked_mut-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#432)[§](#method.index-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#436)[§](#method.index_mut-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#170)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeInclusive%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#171)[§](#associatedtype.Output-3)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#173)[§](#method.get-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#179)[§](#method.get_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#185)[§](#method.get_unchecked-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#192)[§](#method.get_unchecked_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#199)[§](#method.index-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#205)[§](#method.index_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#213)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeInclusive%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#214)[§](#associatedtype.Output-4)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#216)[§](#method.get-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#222)[§](#method.get_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#228)[§](#method.get_unchecked-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#235)[§](#method.get_unchecked_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#242)[§](#method.index-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#248)[§](#method.index_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#318)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeTo%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#319)[§](#associatedtype.Output-7)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#321)[§](#method.get-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#325)[§](#method.get_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#329)[§](#method.get_unchecked-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#334)[§](#method.get_unchecked_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#339)[§](#method.index-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#343)[§](#method.index_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#349)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeToInclusive%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#350)[§](#associatedtype.Output-8)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#352)[§](#method.get-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#356)[§](#method.get_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#360)[§](#method.get_unchecked-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#365)[§](#method.get_unchecked_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#370)[§](#method.index-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#374)[§](#method.index_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#380)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeToInclusive%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#381)[§](#associatedtype.Output-9)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#383)[§](#method.get-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#387)[§](#method.get_mut-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#391)[§](#method.get_unchecked-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#396)[§](#method.get_unchecked_mut-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#401)[§](#method.index-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#405)[§](#method.index_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#53)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#54)[§](#associatedtype.Output)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#56)[§](#method.get-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#60)[§](#method.get_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#64)[§](#method.get_unchecked-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#69)[§](#method.get_unchecked_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#74)[§](#method.index)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#78)[§](#method.index_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#442)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Last)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#443)[§](#associatedtype.Output-11)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#445)[§](#method.get-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#449)[§](#method.get_mut-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#453)[§](#method.get_unchecked-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#458)[§](#method.get_unchecked_mut-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/index.rs.html#463)[§](#method.index-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/index.rs.html#468)[§](#method.index_mut-11)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#362)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Range%3Cusize%3E)

The methods `index` and `index_mut` panic if:

- the start of the range is greater than the end of the range or
- the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#363)[§](#associatedtype.Output-13)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#366)[§](#method.get-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#379)[§](#method.get_mut-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#392)[§](#method.get_unchecked-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#417)[§](#method.get_unchecked_mut-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#435)[§](#method.index-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#448)[§](#method.index_mut-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#463)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Range%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#464)[§](#associatedtype.Output-14)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#467)[§](#method.get-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#472)[§](#method.get_mut-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#477)[§](#method.get_unchecked-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#483)[§](#method.get_unchecked_mut-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#489)[§](#method.index-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#494)[§](#method.index_mut-14)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#541)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFrom%3Cusize%3E)

The methods `index` and `index_mut` panic if the start of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#542)[§](#associatedtype.Output-16)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#545)[§](#method.get-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#550)[§](#method.get_mut-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#555)[§](#method.get_unchecked-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#561)[§](#method.get_unchecked_mut-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#567)[§](#method.index-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#579)[§](#method.index_mut-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#593)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFrom%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#594)[§](#associatedtype.Output-17)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#597)[§](#method.get-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#602)[§](#method.get_mut-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#607)[§](#method.get_unchecked-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#613)[§](#method.get_unchecked_mut-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#619)[§](#method.index-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#624)[§](#method.index_mut-17)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#631)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#632)[§](#associatedtype.Output-18)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#635)[§](#method.get-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#640)[§](#method.get_mut-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#645)[§](#method.get_unchecked-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#650)[§](#method.get_unchecked_mut-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#655)[§](#method.index-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#660)[§](#method.index_mut-18)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#670)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if:

- the start of the range is greater than the end of the range or
- the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#671)[§](#associatedtype.Output-19)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#674)[§](#method.get-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#679)[§](#method.get_mut-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#684)[§](#method.get_unchecked-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#690)[§](#method.get_unchecked_mut-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#696)[§](#method.index-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#711)[§](#method.index_mut-19)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#728)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeInclusive%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#729)[§](#associatedtype.Output-20)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#732)[§](#method.get-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#737)[§](#method.get_mut-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#742)[§](#method.get_unchecked-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#748)[§](#method.get_unchecked_mut-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#754)[§](#method.index-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#759)[§](#method.index_mut-20)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#502)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeTo%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#503)[§](#associatedtype.Output-15)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#506)[§](#method.get-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#511)[§](#method.get_mut-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#516)[§](#method.get_unchecked-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#522)[§](#method.get_unchecked_mut-16)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#528)[§](#method.index-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#533)[§](#method.index_mut-15)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#767)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#768)[§](#associatedtype.Output-21)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#771)[§](#method.get-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#776)[§](#method.get_mut-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#781)[§](#method.get_unchecked-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#787)[§](#method.get_unchecked_mut-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#793)[§](#method.index-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#798)[§](#method.index_mut-21)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#806)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E-1)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#807)[§](#associatedtype.Output-22)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#810)[§](#method.get-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#815)[§](#method.get_mut-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#820)[§](#method.get_unchecked-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#826)[§](#method.get_unchecked_mut-23)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#832)[§](#method.index-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#837)[§](#method.index_mut-22)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#214)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-usize)

The methods `index` and `index_mut` panic if the index is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#215)[§](#associatedtype.Output-12)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#218)[§](#method.get-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#228)[§](#method.get_mut-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#239)[§](#method.get_unchecked-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#259)[§](#method.get_unchecked_mut-13)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#270)[§](#method.index-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#276)[§](#method.index_mut-12)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5657)[§](#impl-SlicePattern-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5658)[§](#associatedtype.Item-2)

🔬This is a nightly-only experimental API. (`slice_pattern` [#56345](https://github.com/rust-lang/rust/issues/56345))

The element type of the slice being matched on.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5661)[§](#method.as_slice-1)

🔬This is a nightly-only experimental API. (`slice_pattern` [#56345](https://github.com/rust-lang/rust/issues/56345))

Currently, the consumers of `SlicePattern` need a slice.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#838)[§](#impl-ToOwned-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#839)[§](#associatedtype.Owned)

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#841)[§](#method.to_owned)

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#845)[§](#method.clone_into)

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#246-252)[§](#impl-ToSocketAddrs-for-%26%5BSocketAddr%5D)

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#247)[§](#associatedtype.Iter)

Returned iterator over socket addresses which this type may correspond to.

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#249-251)[§](#method.to_socket_addrs)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#303)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-%26%5BT;+N%5D)

Tries to create an array ref `&[T; N]` from a slice ref `&[T]`. Succeeds if `slice.len() == N`.

```rust
let bytes: [u8; 3] = [1, 0, 2];

let bytes_head: &[u8; 2] = <&[u8; 2]>::try_from(&bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(*bytes_head));

let bytes_tail: &[u8; 2] = bytes[1..3].try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(*bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#304)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#307)[§](#method.try_from-2)

Performs the conversion.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#251-253)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-%5BT;+N%5D)

Tries to create an array `[T; N]` by copying from a slice `&[T]`. Succeeds if `slice.len() == N`.

```rust
let bytes: [u8; 3] = [1, 0, 2];

let bytes_head: [u8; 2] = <[u8; 2]>::try_from(&bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(bytes_head));

let bytes_tail: [u8; 2] = bytes[1..3].try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#255)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#258)[§](#method.try_from)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1038-1040)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1042)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1045)[§](#method.try_from-4)

Performs the conversion.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#326)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-%26mut+%5BT;+N%5D)

Tries to create a mutable array ref `&mut [T; N]` from a mutable slice ref `&mut [T]`. Succeeds if `slice.len() == N`.

```rust
let mut bytes: [u8; 3] = [1, 0, 2];

let bytes_head: &mut [u8; 2] = <&mut [u8; 2]>::try_from(&mut bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(*bytes_head));

let bytes_tail: &mut [u8; 2] = (&mut bytes[1..3]).try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(*bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#327)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#330)[§](#method.try_from-3)

Performs the conversion.

1.59.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#277-279)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-%5BT;+N%5D)

Tries to create an array `[T; N]` by copying from a mutable slice `&mut [T]`. Succeeds if `slice.len() == N`.

```rust
let mut bytes: [u8; 3] = [1, 0, 2];

let bytes_head: [u8; 2] = <[u8; 2]>::try_from(&mut bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(bytes_head));

let bytes_tail: [u8; 2] = (&mut bytes[1..3]).try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#281)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#284)[§](#method.try_from-1)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1050-1052)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1054)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1057)[§](#method.try_from-5)

Performs the conversion.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#428-475)[§](#impl-Write-for-%26mut+%5Bu8%5D)

Write is implemented for `&mut [u8]` by copying into the slice, overwriting its data.

Note that writing updates the slice to point to the yet unwritten part. The slice will be empty when it has been completely overwritten.

If the number of bytes to be written exceeds the size of the slice, write operations will return short writes: ultimately, `Ok(0)`; in this situation, `write_all` returns an error of kind `ErrorKind::WriteZero`.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#430-436)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#439-449)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#452-454)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#457-459)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#462-469)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#472-474)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1111-1118)[§](#impl-ConstParamTy_-for-%5BT%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/slice/cmp.rs.html#32)[§](#impl-Eq-for-%5BT%5D)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#103)[§](#impl-Iterator-for-%26Box%3C%5BI%5D,+A%3E)

This implementation is required to make sure that the `&Box<[I]>: IntoIterator` implementation doesn’t overlap with `IntoIterator for T where T: Iterator` blanket.

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#108)[§](#impl-Iterator-for-%26mut+Box%3C%5BI%5D,+A%3E)

This implementation is required to make sure that the `&mut Box<[I]>: IntoIterator` implementation doesn’t overlap with `IntoIterator for T where T: Iterator` blanket.

1.80.0 · [Source](https://doc.rust-lang.org/src/core/slice/iter.rs.html#18)[§](#impl-Iterator-for-%5BT%5D)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#98)[§](#impl-Iterator-for-Box%3C%5BI%5D,+A%3E)

This implementation is required to make sure that the `Box<[I]>: IntoIterator` implementation doesn’t overlap with `IntoIterator for T where T: Iterator` blanket.

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-%5BT%5D)