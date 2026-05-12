---
title: pointer - Rust
url: https://doc.rust-lang.org/std/primitive.pointer.html
source: crawler
fetched_at: 2026-05-06T21:22:13.799292561-03:00
rendered_js: false
word_count: 12398
summary: This document provides an overview of raw pointers in Rust, explaining their syntax, safety requirements, and common patterns for creation and manipulation.
tags:
    - rust
    - raw-pointers
    - memory-safety
    - unsafe-rust
    - pointers
    - ffi
category: reference
---

## Primitive Type pointer

1.0.0

Expand description

Raw, unsafe pointers, `*const T`, and `*mut T`.

*[See also the `std::ptr` module](https://doc.rust-lang.org/std/ptr/index.html "mod std::ptr").*

Working with raw pointers in Rust is uncommon, typically limited to a few patterns. Raw pointers can be out-of-bounds, unaligned, or [`null`](https://doc.rust-lang.org/std/ptr/fn.null.html "fn std::ptr::null"). However, when loading from or storing to a raw pointer, it must be [valid](https://doc.rust-lang.org/std/ptr/index.html#safety "mod std::ptr") for the given access and aligned. When using a field expression, tuple index expression, or array/slice index expression on a raw pointer, it follows the rules of [in-bounds pointer arithmetic](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset").

Storing through a raw pointer using `*ptr = data` calls `drop` on the old value, so [`write`](https://doc.rust-lang.org/std/ptr/fn.write.html "fn std::ptr::write") must be used if the type has drop glue and memory is not already initialized - otherwise `drop` would be called on the uninitialized memory.

Use the [`null`](https://doc.rust-lang.org/std/ptr/fn.null.html "fn std::ptr::null") and [`null_mut`](https://doc.rust-lang.org/std/ptr/fn.null_mut.html "fn std::ptr::null_mut") functions to create null pointers, and the [`is_null`](https://doc.rust-lang.org/std/primitive.pointer.html#method.is_null "method pointer::is_null") method of the `*const T` and `*mut T` types to check for null. The `*const T` and `*mut T` types also define the [`offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset") method, for pointer math.

## [§](#common-ways-to-create-raw-pointers)Common ways to create raw pointers

### [§](#1-coerce-a-reference-t-or-mutable-reference-mut-t)1. Coerce a reference (`&T`) or mutable reference (`&mut T`).

```rust
let my_num: i32 = 10;
let my_num_ptr: *const i32 = &my_num;
let mut my_speed: i32 = 88;
let my_speed_ptr: *mut i32 = &mut my_speed;
```

To get a pointer to a boxed value, dereference the box:

```rust
let my_num: Box<i32> = Box::new(10);
let my_num_ptr: *const i32 = &*my_num;
let mut my_speed: Box<i32> = Box::new(88);
let my_speed_ptr: *mut i32 = &mut *my_speed;
```

This does not take ownership of the original allocation and requires no resource management later, but you must not use the pointer after its lifetime.

### [§](#2-consume-a-box-boxt)2. Consume a box (`Box<T>`).

The [`into_raw`](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.into_raw) function consumes a box and returns the raw pointer. It doesn’t destroy `T` or deallocate any memory.

```rust
let my_speed: Box<i32> = Box::new(88);
let my_speed: *mut i32 = Box::into_raw(my_speed);

// By taking ownership of the original `Box<T>` though
// we are obligated to put it together later to be destroyed.
unsafe {
    drop(Box::from_raw(my_speed));
}
```

Note that here the call to [`drop`](https://doc.rust-lang.org/std/mem/fn.drop.html "fn std::mem::drop") is for clarity - it indicates that we are done with the given value and it should be destroyed.

### [§](#3-create-it-using-raw)3. Create it using `&raw`

Instead of coercing a reference to a raw pointer, you can use the raw borrow operators `&raw const` (for `*const T`) and `&raw mut` (for `*mut T`). These operators allow you to create raw pointers to fields to which you cannot create a reference (without causing undefined behavior), such as an unaligned field. This might be necessary if packed structs or uninitialized memory is involved.

```rust
#[derive(Debug, Default, Copy, Clone)]
#[repr(C, packed)]
struct S {
    aligned: u8,
    unaligned: u32,
}
let s = S::default();
let p = &raw const s.unaligned; // not allowed with coercion
```

### [§](#4-get-it-from-c)4. Get it from C.

```rust
#[allow(unused_extern_crates)]
extern crate libc;

unsafe {
    let my_num: *mut i32 = libc::malloc(size_of::<i32>()) as *mut i32;
    if my_num.is_null() {
        panic!("failed to allocate memory");
    }
    libc::free(my_num as *mut core::ffi::c_void);
}
```

Usually you wouldn’t literally use `malloc` and `free` from Rust, but C APIs hand out a lot of pointers generally, so are a common source of raw pointers in Rust.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#7)[§](#impl-*const+T)

1.0.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#22)

Returns `true` if the pointer is null.

Note that unsized types have many possible null pointers, as only the raw data pointer is considered, not their length, vtable, etc. Therefore, two pointers that are null may still not compare equal to each other.

##### [§](#panics-during-const-evaluation)Panics during const evaluation

If this method is used during const evaluation, and `self` is a pointer that is offset beyond the bounds of the memory it initially pointed to, then there might not be enough information to determine whether the pointer is null. This is because the absolute address in memory is not known at compile time. If the nullness of the pointer cannot be determined, this method will panic.

In-bounds pointers are never null, so the method will never panic for such pointers.

##### [§](#examples)Examples

```rust
let s: &str = "Follow the rabbit";
let ptr: *const u8 = s.as_ptr();
assert!(!ptr.is_null());
```

1.38.0 (const: 1.38.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#48)

Casts to a pointer of another type.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#74)

🔬This is a nightly-only experimental API. (`pointer_try_cast_aligned` [#141221](https://github.com/rust-lang/rust/issues/141221))

Try to cast to a pointer of another type by checking alignment.

If the pointer is properly aligned to the target type, it will be cast to the target type. Otherwise, `None` is returned.

##### [§](#examples-1)Examples

```rust
#![feature(pointer_try_cast_aligned)]

let x = 0u64;

let aligned: *const u64 = &x;
let unaligned = unsafe { aligned.byte_add(1) };

assert!(aligned.try_cast_aligned::<u32>().is_some());
assert!(unaligned.try_cast_aligned::<u32>().is_none());
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#130-132)

🔬This is a nightly-only experimental API. (`set_ptr_value` [#75091](https://github.com/rust-lang/rust/issues/75091))

Uses the address value in a new pointer of another type.

This operation will ignore the address part of its `meta` operand and discard existing metadata of `self`. For pointers to a sized types (thin pointers), this has the same effect as a simple cast. For pointers to an unsized type (fat pointers) this recombines the address with new metadata such as slice lengths or `dyn`-vtable.

The resulting pointer will have provenance of `self`. This operation is semantically the same as creating a new pointer with the data pointer value of `self` but the metadata of `meta`, being fat or thin depending on the `meta` operand.

##### [§](#examples-2)Examples

This function is primarily useful for enabling pointer arithmetic on potentially fat pointers. The pointer is cast to a sized pointee to utilize offset operations and then recombined with its own original metadata.

```rust
#![feature(set_ptr_value)]
let arr: [i32; 3] = [1, 2, 3];
let mut ptr = arr.as_ptr() as *const dyn Debug;
let thin = ptr as *const u8;
unsafe {
    ptr = thin.add(8).with_metadata_of(ptr);
    println!("{:?}", &*ptr); // will print "3"
}
```

##### [§](#incorrect-usage)*Incorrect* usage

The provenance from pointers is *not* combined. The result must only be used to refer to the address allowed by `self`.

```rust
#![feature(set_ptr_value)]
let x = 0u32;
let y = 1u32;

let x = (&x) as *const u32;
let y = (&y) as *const u32;

let offset = (x as usize - y as usize) / 4;
let bad = x.wrapping_add(offset).with_metadata_of(y);

// This dereference is UB. The pointer only has provenance for `x` but points to `y`.
println!("{:?}", unsafe { &*bad });
```

1.65.0 (const: 1.65.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#145)

Changes constness without changing the type.

This is a bit safer than `as` because it wouldn’t silently change the type if the code is refactored.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#153)

Gets the “address” portion of the pointer.

This is similar to `self as usize`, except that the [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") of the pointer is discarded and not [exposed](https://doc.rust-lang.org/std/ptr/index.html#exposed-provenance "mod std::ptr"). This means that casting the returned address back to a pointer yields a [pointer without provenance](https://doc.rust-lang.org/std/ptr/fn.without_provenance.html "fn std::ptr::without_provenance"), which is undefined behavior to dereference. To properly restore the lost information and obtain a dereferenceable pointer, use [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr") or [`map_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.map_addr "method pointer::map_addr").

If using those APIs is not possible because there is no way to preserve a pointer with the required provenance, then Strict Provenance might not be for you. Use pointer-integer casts or [`expose_provenance`](https://doc.rust-lang.org/std/primitive.pointer.html#method.expose_provenance "method pointer::expose_provenance") and [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") instead. However, note that this makes your code less portable and less amenable to tools that check for compliance with the Rust memory model.

On most platforms this will produce a value with the same bytes as the original pointer, because all the bytes are dedicated to describing the address. Platforms which need to store additional information in the pointer may perform a change of representation to produce a value containing only the address portion of the pointer. What that means is up to the platform to define.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#186)

Exposes the [“provenance”](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") part of the pointer for future use in [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") and returns the “address” portion.

This is equivalent to `self as usize`, which semantically discards provenance information. Furthermore, this (like the `as` cast) has the implicit side-effect of marking the provenance as ‘exposed’, so on platforms that support it you can later call [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") to reconstitute the original pointer including its provenance.

Due to its inherent ambiguity, [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") may not be supported by tools that help you to stay conformant with the Rust memory model. It is recommended to use [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") APIs such as [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr") wherever possible, in which case [`addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") should be used instead of `expose_provenance`.

On most platforms this will produce a value with the same bytes as the original pointer, because all the bytes are dedicated to describing the address. Platforms which need to store additional information in the pointer may not support this operation, since the ‘expose’ side-effect which is required for [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") to work is typically not available.

This is an [Exposed Provenance](https://doc.rust-lang.org/std/ptr/index.html#exposed-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#204)

Creates a new pointer with the given address and the [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") of `self`.

This is similar to a `addr as *const T` cast, but copies the *provenance* of `self` to the new pointer. This avoids the inherent ambiguity of the unary cast.

This is equivalent to using [`wrapping_offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_offset "method pointer::wrapping_offset") to offset `self` to the given address, and therefore has all the same capabilities and restrictions.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#223)

Creates a new pointer by mapping `self`’s address to a new one, preserving the [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") of `self`.

This is a convenience for [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr"), see that method for details.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#232)

🔬This is a nightly-only experimental API. (`ptr_metadata` [#81513](https://github.com/rust-lang/rust/issues/81513))

Decompose a (possibly wide) pointer into its data pointer and metadata components.

The pointer can be later reconstructed with [`from_raw_parts`](https://doc.rust-lang.org/std/ptr/fn.from_raw_parts.html "fn std::ptr::from_raw_parts").

1.9.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#266)

Returns `None` if the pointer is null, or else returns a shared reference to the value wrapped in `Some`. If the value may be uninitialized, [`as_uninit_ref`](#method.as_uninit_ref) must be used instead. If the value is known to be non-null, [`as_ref_unchecked`](#method.as_ref_unchecked) can be used instead.

##### [§](#safety)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#panics-during-const-evaluation-1)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null) for more information.

##### [§](#null-unchecked-version)Null-unchecked version

If you are sure the pointer can never be null, you can use `as_ref_unchecked` which returns `&mut T` instead of `Option<&mut T>`.

```rust
let ptr: *const u8 = &10u8 as *const u8;

unsafe {
    let val_back = ptr.as_ref_unchecked();
    assert_eq!(val_back, &10);
}
```

##### [§](#examples-3)Examples

```rust
let ptr: *const u8 = &10u8 as *const u8;

unsafe {
    if let Some(val_back) = ptr.as_ref() {
        assert_eq!(val_back, &10);
    }
}
```

1.95.0 (const: 1.95.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#297)

Returns a shared reference to the value behind the pointer. If the pointer may be null or the value may be uninitialized, [`as_uninit_ref`](#method.as_uninit_ref) must be used instead. If the pointer may be null, but the value is known to have been initialized, [`as_ref`](#method.as_ref) must be used instead.

##### [§](#safety-1)Safety

When calling this method, you have to ensure that the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#examples-4)Examples

```rust
let ptr: *const u8 = &10u8 as *const u8;

unsafe {
    assert_eq!(ptr.as_ref_unchecked(), &10);
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#322-324)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a shared reference to the value wrapped in `Some`. In contrast to [`as_ref`](#method.as_ref), this does not require that the value has to be initialized.

##### [§](#safety-2)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr"). Note that because the created reference is to `MaybeUninit<T>`, the source pointer can point to uninitialized memory.

##### [§](#panics-during-const-evaluation-2)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null) for more information.

##### [§](#examples-5)Examples

```rust
#![feature(ptr_as_uninit)]

let ptr: *const u8 = &10u8 as *const u8;

unsafe {
    if let Some(val_back) = ptr.as_uninit_ref() {
        assert_eq!(val_back.assume_init(), 10);
    }
}
```

1.0.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#349-351)

Adds a signed offset to a pointer.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-3)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space. Note that “range” here refers to a half-open range as usual in Rust, i.e., `self..result` for non-negative offsets and `result..self` for negative offsets.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_offset`](#method.wrapping_offset) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-6)Examples

```rust
let s: &str = "123";
let ptr: *const u8 = s.as_ptr();

unsafe {
    assert_eq!(*ptr.offset(1) as char, '2');
    assert_eq!(*ptr.offset(2) as char, '3');
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#402)

Adds a signed offset in bytes to a pointer.

`count` is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.16.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#463-465)

Adds a signed offset to a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-4)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to (this is called “[Provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance)”). The pointer must not be used to read or write other allocations.

In other words, `let z = x.wrapping_offset((y as isize) - (x as isize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`offset`](#method.offset), this method basically delays the requirement of staying within the same allocation: [`offset`](#method.offset) is immediate Undefined Behavior when crossing object boundaries; `wrapping_offset` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`offset`](#method.offset) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_offset(o).wrapping_offset(o.wrapping_neg())` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-7)Examples

```rust
// Iterate using a raw pointer in increments of two elements
let data = [1u8, 2, 3, 4, 5];
let mut ptr: *const u8 = data.as_ptr();
let step = 2;
let end_rounded_up = ptr.wrapping_offset(6);

let mut out = String::new();
while ptr != end_rounded_up {
    unsafe {
        write!(&mut out, "{}, ", *ptr)?;
    }
    ptr = ptr.wrapping_offset(step);
}
assert_eq!(out.as_str(), "1, 3, 5, ");
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#485)

Adds a signed offset in bytes to a pointer using wrapping arithmetic.

`count` is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_offset "method pointer::wrapping_offset") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#523)

🔬This is a nightly-only experimental API. (`ptr_mask` [#98290](https://github.com/rust-lang/rust/issues/98290))

Masks out bits of the pointer according to a mask.

This is convenience for `ptr.map_addr(|a| a & mask)`.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

###### [§](#examples-8)Examples

```rust
#![feature(ptr_mask)]
let v = 17_u32;
let ptr: *const u32 = &v;

// `u32` is 4 bytes aligned,
// which means that lower 2 bits are always 0.
let tag_mask = 0b11;
let ptr_mask = !tag_mask;

// We can store something in these lower bits
let tagged_ptr = ptr.map_addr(|a| a | 0b10);

// Get the "tag" back
let tag = tagged_ptr.addr() & tag_mask;
assert_eq!(tag, 0b10);

// Note that `tagged_ptr` is unaligned, it's UB to read from it.
// To get original pointer `mask` can be used:
let masked_ptr = tagged_ptr.mask(ptr_mask);
assert_eq!(unsafe { *masked_ptr }, 17);
```

1.47.0 (const: 1.65.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#612-614)

Calculates the distance between two pointers within the same allocation. The returned value is in units of T: the distance in bytes divided by `size_of::<T>()`.

This is equivalent to `(self as isize - origin as isize) / (size_of::<T>() as isize)`, except that it has a lot more opportunities for UB, in exchange for the compiler better understanding what you are doing.

The primary motivation of this method is for computing the `len` of an array/slice of `T` that you are currently representing as a “start” and “end” pointer (and “end” is “one past the end” of the array). In that case, `end.offset_from(start)` gets you the length of the array.

All of the following safety requirements are trivially satisfied for this usecase.

##### [§](#safety-5)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- `self` and `origin` must either
  
  - point to the same address, or
  - both be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to the same [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the memory range between the two pointers must be in bounds of that object. (See below for an example.)
- The distance between the pointers, in bytes, must be an exact multiple of the size of `T`.

As a consequence, the absolute distance between the pointers, in bytes, computed on mathematical integers (without “wrapping around”), cannot overflow an `isize`. This is implied by the in-bounds requirement, and the fact that no allocation can be larger than `isize::MAX` bytes.

The requirement for pointers to be derived from the same allocation is primarily needed for `const`-compatibility: the distance between pointers into *different* allocated objects is not known at compile-time. However, the requirement also exists at runtime and may be exploited by optimizations. If you wish to compute the difference between pointers that are not guaranteed to be from the same allocation, use `(self as isize - origin as isize) / size_of::<T>()`.

##### [§](#panics)Panics

This function panics if `T` is a Zero-Sized Type (“ZST”).

##### [§](#examples-9)Examples

Basic usage:

```rust
let a = [0; 5];
let ptr1: *const i32 = &a[1];
let ptr2: *const i32 = &a[3];
unsafe {
    assert_eq!(ptr2.offset_from(ptr1), 2);
    assert_eq!(ptr1.offset_from(ptr2), -2);
    assert_eq!(ptr1.offset(2), ptr2);
    assert_eq!(ptr2.offset(-2), ptr1);
}
```

*Incorrect* usage:

```rust
let ptr1 = Box::into_raw(Box::new(0u8)) as *const u8;
let ptr2 = Box::into_raw(Box::new(1u8)) as *const u8;
let diff = (ptr2 as isize).wrapping_sub(ptr1 as isize);
// Make ptr2_other an "alias" of ptr2.add(1), but derived from ptr1.
let ptr2_other = (ptr1 as *const u8).wrapping_offset(diff).wrapping_offset(1);
assert_eq!(ptr2 as usize, ptr2_other as usize);
// Since ptr2_other and ptr2 are derived from pointers to different objects,
// computing their offset is undefined behavior, even though
// they point to addresses that are in-bounds of the same object!
unsafe {
    let one = ptr2_other.offset_from(ptr2); // Undefined Behavior! ⚠️
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#635)

Calculates the distance between two pointers within the same allocation. The returned value is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [`offset_from`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset_from "method pointer::offset_from") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation considers only the data pointers, ignoring the metadata.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#701-703)

Calculates the distance between two pointers within the same allocation, *where it’s known that `self` is equal to or greater than `origin`* . The returned value is in units of T: the distance in bytes is divided by `size_of::<T>()`.

This computes the same value that [`offset_from`](#method.offset_from) would compute, but with the added precondition that the offset is guaranteed to be non-negative. This method is equivalent to `usize::try_from(self.offset_from(origin)).unwrap_unchecked()`, but it provides slightly more information to the optimizer, which can sometimes allow it to optimize slightly better with some backends.

This method can be thought of as recovering the `count` that was passed to [`add`](#method.add) (or, with the parameters in the other order, to [`sub`](#method.sub)). The following are all equivalent, assuming that their safety preconditions are met:

```rust
ptr.offset_from_unsigned(origin) == count
origin.add(count) == ptr
ptr.sub(count) == origin
```

##### [§](#safety-6)Safety

- The distance between the pointers must be non-negative (`self >= origin`)
- *All* the safety conditions of [`offset_from`](#method.offset_from) apply to this method as well; see it for the full details.

Importantly, despite the return type of this method being able to represent a larger offset, it’s still *not permitted* to pass pointers which differ by more than `isize::MAX` *bytes*. As such, the result of this method will always be less than or equal to `isize::MAX as usize`.

##### [§](#panics-1)Panics

This function panics if `T` is a Zero-Sized Type (“ZST”).

##### [§](#examples-10)Examples

```rust
let a = [0; 5];
let ptr1: *const i32 = &a[1];
let ptr2: *const i32 = &a[3];
unsafe {
    assert_eq!(ptr2.offset_from_unsigned(ptr1), 2);
    assert_eq!(ptr1.add(2), ptr2);
    assert_eq!(ptr2.sub(2), ptr1);
    assert_eq!(ptr2.offset_from_unsigned(ptr2), 0);
}

// This would be incorrect, as the pointers are not correctly ordered:
// ptr1.offset_from_unsigned(ptr2)
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#746)

Calculates the distance between two pointers within the same allocation, *where it’s known that `self` is equal to or greater than `origin`* . The returned value is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [`offset_from_unsigned`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset_from_unsigned "method pointer::offset_from_unsigned") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation considers only the data pointers, ignoring the metadata.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#771-773)

🔬This is a nightly-only experimental API. (`const_raw_ptr_comparison` [#53020](https://github.com/rust-lang/rust/issues/53020))

Returns whether two pointers are guaranteed to be equal.

At runtime this function behaves like `Some(self == other)`. However, in some contexts (e.g., compile-time evaluation), it is not always possible to determine equality of two pointers, so this function may spuriously return `None` for pointers that later actually turn out to have its equality known. But when it returns `Some`, the pointers’ equality is guaranteed to be known.

The return value may change from `Some` to `None` and vice versa depending on the compiler version and unsafe code must not rely on the result of this function for soundness. It is suggested to only use this function for performance optimizations where spurious `None` return values by this function do not affect the outcome, but just the performance. The consequences of using this method to make runtime and compile-time code behave differently have not been explored. This method should not be used to introduce such differences, and it should also not be stabilized before we have a better understanding of this issue.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#801-803)

🔬This is a nightly-only experimental API. (`const_raw_ptr_comparison` [#53020](https://github.com/rust-lang/rust/issues/53020))

Returns whether two pointers are guaranteed to be inequal.

At runtime this function behaves like `Some(self != other)`. However, in some contexts (e.g., compile-time evaluation), it is not always possible to determine inequality of two pointers, so this function may spuriously return `None` for pointers that later actually turn out to have its inequality known. But when it returns `Some`, the pointers’ inequality is guaranteed to be known.

The return value may change from `Some` to `None` and vice versa depending on the compiler version and unsafe code must not rely on the result of this function for soundness. It is suggested to only use this function for performance optimizations where spurious `None` return values by this function do not affect the outcome, but just the performance. The consequences of using this method to make runtime and compile-time code behave differently have not been explored. This method should not be used to introduce such differences, and it should also not be stabilized before we have a better understanding of this issue.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#829-831)

Adds an unsigned offset to a pointer.

This can only move the pointer forward (or not move it). If you need to move forward or backward depending on the value, then you might want [`offset`](#method.offset) instead which takes a signed offset.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-7)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_add`](#method.wrapping_add) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-11)Examples

```rust
let s: &str = "123";
let ptr: *const u8 = s.as_ptr();

unsafe {
    assert_eq!(*ptr.add(1), b'2');
    assert_eq!(*ptr.add(2), b'3');
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#881)

Adds an unsigned offset in bytes to a pointer.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [add](https://doc.rust-lang.org/std/primitive.pointer.html#method.add "method pointer::add") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#935-937)

Subtracts an unsigned offset from a pointer.

This can only move the pointer backward (or not move it). If you need to move forward or backward depending on the value, then you might want [`offset`](#method.offset) instead which takes a signed offset.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-8)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_sub`](#method.wrapping_sub) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-12)Examples

```rust
let s: &str = "123";

unsafe {
    let end: *const u8 = s.as_ptr().add(3);
    assert_eq!(*end.sub(1), b'3');
    assert_eq!(*end.sub(2), b'2');
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#993)

Subtracts an unsigned offset in bytes from a pointer.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [sub](https://doc.rust-lang.org/std/primitive.pointer.html#method.sub "method pointer::sub") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1053-1055)

Adds an unsigned offset to a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-9)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to; it must not be used to read or write other allocations.

In other words, `let z = x.wrapping_add((y as usize) - (x as usize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`add`](#method.add), this method basically delays the requirement of staying within the same allocation: [`add`](#method.add) is immediate Undefined Behavior when crossing object boundaries; `wrapping_add` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`add`](#method.add) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_add(o).wrapping_sub(o)` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-13)Examples

```rust
// Iterate using a raw pointer in increments of two elements
let data = [1u8, 2, 3, 4, 5];
let mut ptr: *const u8 = data.as_ptr();
let step = 2;
let end_rounded_up = ptr.wrapping_add(6);

let mut out = String::new();
while ptr != end_rounded_up {
    unsafe {
        write!(&mut out, "{}, ", *ptr)?;
    }
    ptr = ptr.wrapping_add(step);
}
assert_eq!(out, "1, 3, 5, ");
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1073)

Adds an unsigned offset in bytes to a pointer using wrapping arithmetic.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_add](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_add "method pointer::wrapping_add") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1132-1134)

Subtracts an unsigned offset from a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-10)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to; it must not be used to read or write other allocations.

In other words, `let z = x.wrapping_sub((x as usize) - (y as usize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`sub`](#method.sub), this method basically delays the requirement of staying within the same allocation: [`sub`](#method.sub) is immediate Undefined Behavior when crossing object boundaries; `wrapping_sub` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`sub`](#method.sub) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_add(o).wrapping_sub(o)` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-14)Examples

```rust
// Iterate using a raw pointer in increments of two elements (backwards)
let data = [1u8, 2, 3, 4, 5];
let mut ptr: *const u8 = data.as_ptr();
let start_rounded_down = ptr.wrapping_sub(2);
ptr = ptr.wrapping_add(4);
let step = 2;
let mut out = String::new();
while ptr != start_rounded_down {
    unsafe {
        write!(&mut out, "{}, ", *ptr)?;
    }
    ptr = ptr.wrapping_sub(step);
}
assert_eq!(out, "5, 3, 1, ");
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1152)

Subtracts an unsigned offset in bytes from a pointer using wrapping arithmetic.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_sub](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_sub "method pointer::wrapping_sub") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1166-1168)

Reads the value from `self` without moving it. This leaves the memory in `self` unchanged.

See [`ptr::read`](https://doc.rust-lang.org/std/ptr/fn.read.html "fn std::ptr::read") for safety concerns and examples.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1187-1189)

Performs a volatile read of the value from `self` without moving it. This leaves the memory in `self` unchanged.

Volatile operations are intended to act on I/O memory, and are guaranteed to not be elided or reordered by the compiler across other volatile operations.

See [`ptr::read_volatile`](https://doc.rust-lang.org/std/ptr/fn.read_volatile.html "fn std::ptr::read_volatile") for safety concerns and examples.

1.26.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1207-1209)

Reads the value from `self` without moving it. This leaves the memory in `self` unchanged.

Unlike `read`, the pointer may be unaligned.

See [`ptr::read_unaligned`](https://doc.rust-lang.org/std/ptr/fn.read_unaligned.html "fn std::ptr::read_unaligned") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1227-1229)

Copies `count * size_of::<T>()` bytes from `self` to `dest`. The source and destination may overlap.

NOTE: this has the *same* argument order as [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy").

See [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1247-1249)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1294-1296)

Computes the offset that needs to be applied to the pointer in order to make it aligned to `align`.

If it is not possible to align the pointer, the implementation returns `usize::MAX`.

The offset is expressed in number of `T` elements, and not bytes. The value returned can be used with the `wrapping_add` method.

There are no guarantees whatsoever that offsetting the pointer will not overflow or go beyond the allocation that the pointer points into. It is up to the caller to ensure that the returned offset is correct in all terms other than alignment.

##### [§](#panics-2)Panics

The function panics if `align` is not a power-of-two.

##### [§](#examples-15)Examples

Accessing adjacent `u8` as `u16`

```rust
let x = [5_u8, 6, 7, 8, 9];
let ptr = x.as_ptr();
let offset = ptr.align_offset(align_of::<u16>());

if offset < x.len() - 1 {
    let u16_ptr = ptr.add(offset).cast::<u16>();
    assert!(*u16_ptr == u16::from_ne_bytes([5, 6]) || *u16_ptr == u16::from_ne_bytes([6, 7]));
} else {
    // while the pointer can be aligned via `offset`, it would point
    // outside the allocation
}
```

1.79.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1332-1334)

Returns whether the pointer is properly aligned for `T`.

##### [§](#examples-16)Examples

```rust
// On some platforms, the alignment of i32 is less than 4.
#[repr(align(4))]
struct AlignedI32(i32);

let data = AlignedI32(42);
let ptr = &data as *const AlignedI32;

assert!(ptr.is_aligned());
assert!(!ptr.wrapping_byte_add(1).is_aligned());
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1372)

🔬This is a nightly-only experimental API. (`pointer_is_aligned_to` [#96284](https://github.com/rust-lang/rust/issues/96284))

Returns whether the pointer is aligned to `align`.

For non-`Sized` pointees this operation considers only the data pointer, ignoring the metadata.

##### [§](#panics-3)Panics

The function panics if `align` is not a power-of-two (this includes 0).

##### [§](#examples-17)Examples

```rust
#![feature(pointer_is_aligned_to)]

// On some platforms, the alignment of i32 is less than 4.
#[repr(align(4))]
struct AlignedI32(i32);

let data = AlignedI32(42);
let ptr = &data as *const AlignedI32;

assert!(ptr.is_aligned_to(1));
assert!(ptr.is_aligned_to(2));
assert!(ptr.is_aligned_to(4));

assert!(ptr.wrapping_byte_add(2).is_aligned_to(2));
assert!(!ptr.wrapping_byte_add(2).is_aligned_to(4));

assert_ne!(ptr.is_aligned_to(8), ptr.wrapping_add(1).is_aligned_to(8));
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1381)[§](#impl-*const+T-1)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1386)

🔬This is a nightly-only experimental API. (`cast_maybe_uninit` [#145036](https://github.com/rust-lang/rust/issues/145036))

Casts from a type to its maybe-uninitialized version.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1423)

🔬This is a nightly-only experimental API. (`ptr_cast_slice` [#149103](https://github.com/rust-lang/rust/issues/149103))

Forms a raw slice from a pointer and a length.

The `len` argument is the number of **elements**, not the number of bytes.

This function is safe, but actually using the return value is unsafe. See the documentation of [`slice::from_raw_parts`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html "fn std::slice::from_raw_parts") for slice safety requirements.

##### [§](#examples-18)Examples

```rust
#![feature(ptr_cast_slice)]
// create a slice pointer when starting out with a pointer to the first element
let x = [5, 6, 7];
let raw_pointer = x.as_ptr();
let slice = raw_pointer.cast_slice(3);
assert_eq!(unsafe { &*slice }[2], 7);
```

You must ensure that the pointer is valid and not null before dereferencing the raw slice. A slice reference must never have a null pointer, even if it’s empty.

[ⓘ](# "This example panics")

```rust
#![feature(ptr_cast_slice)]
use std::ptr;
let danger: *const [u8] = ptr::null::<u8>().cast_slice(0);
unsafe {
    danger.as_ref().expect("references must not be null");
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1427)[§](#impl-*const+MaybeUninit%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1435)

🔬This is a nightly-only experimental API. (`cast_maybe_uninit` [#145036](https://github.com/rust-lang/rust/issues/145036))

Casts from a maybe-uninitialized type to its initialized version.

This is always safe, since UB can only occur if the pointer is read before being initialized.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1440)[§](#impl-*const+%5BT%5D)

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1459)

Returns the length of a raw slice.

The returned value is the number of **elements**, not the number of bytes.

This function is safe, even when the raw slice cannot be cast to a slice reference because the pointer is null or unaligned.

##### [§](#examples-19)Examples

```rust
use std::ptr;

let slice: *const [i8] = ptr::slice_from_raw_parts(ptr::null(), 3);
assert_eq!(slice.len(), 3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1476)

Returns `true` if the raw slice has a length of 0.

##### [§](#examples-20)Examples

```rust
use std::ptr;

let slice: *const [i8] = ptr::slice_from_raw_parts(ptr::null(), 3);
assert!(!slice.is_empty());
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1495)

🔬This is a nightly-only experimental API. (`slice_ptr_get` [#74265](https://github.com/rust-lang/rust/issues/74265))

Returns a raw pointer to the slice’s buffer.

This is equivalent to casting `self` to `*const T`, but more type-safe.

##### [§](#examples-21)Examples

```rust
#![feature(slice_ptr_get)]
use std::ptr;

let slice: *const [i8] = ptr::slice_from_raw_parts(ptr::null(), 3);
assert_eq!(slice.as_ptr(), ptr::null());
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1506)

Gets a raw pointer to the underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1537-1539)

🔬This is a nightly-only experimental API. (`slice_ptr_get` [#74265](https://github.com/rust-lang/rust/issues/74265))

Returns a raw pointer to an element or subslice, without doing bounds checking.

Calling this method with an out-of-bounds index or when `self` is not dereferenceable is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointer is not used.

##### [§](#examples-22)Examples

```rust
#![feature(slice_ptr_get)]

let x = &[1, 2, 4] as *const [i32];

unsafe {
    assert_eq!(x.get_unchecked(1), x.as_ptr().add(1));
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1548)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a shared slice to the value wrapped in `Some`. In contrast to [`as_ref`](#method.as_ref), this does not require that the value has to be initialized.

##### [§](#safety-11)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* all of the following is true:

- The pointer must be [valid](https://doc.rust-lang.org/std/ptr/index.html#safety "mod std::ptr") for reads for `ptr.len() * size_of::<T>()` many bytes, and it must be properly aligned. This means in particular:
- The entire memory range of this slice must be contained within a single [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr")! Slices can never span across multiple allocations.
- The pointer must be aligned even for zero-length slices. One reason for this is that enum layout optimizations may rely on references (including slices of any length) being aligned and non-null to distinguish them from other data. You can obtain a pointer that is usable as `data` for zero-length slices using [`NonNull::dangling()`](https://doc.rust-lang.org/std/ptr/struct.NonNull.html#method.dangling "associated function std::ptr::NonNull::dangling").
- The total size `ptr.len() * size_of::<T>()` of the slice must be no larger than `isize::MAX`. See the safety documentation of [`pointer::offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset").
- You must enforce Rust’s aliasing rules, since the returned lifetime `'a` is arbitrarily chosen and does not necessarily reflect the actual lifetime of the data. In particular, while this reference exists, the memory the pointer points to must not get mutated (except inside `UnsafeCell`).

This applies even if the result of this method is unused!

See also [`slice::from_raw_parts`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html "fn std::slice::from_raw_parts").

##### [§](#panics-during-const-evaluation-3)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null) for more information.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1558)[§](#impl-*const+T-2)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1562)

🔬This is a nightly-only experimental API. (`ptr_cast_array` [#144514](https://github.com/rust-lang/rust/issues/144514))

Casts from a pointer-to-`T` to a pointer-to-`[T; N]`.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1567)[§](#impl-*const+%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1583)

🔬This is a nightly-only experimental API. (`array_ptr_get` [#119834](https://github.com/rust-lang/rust/issues/119834))

Returns a raw pointer to the array’s buffer.

This is equivalent to casting `self` to `*const T`, but more type-safe.

##### [§](#examples-23)Examples

```rust
#![feature(array_ptr_get)]
use std::ptr;

let arr: *const [i8; 3] = ptr::null();
assert_eq!(arr.as_ptr(), ptr::null());
```

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1600)

🔬This is a nightly-only experimental API. (`array_ptr_get` [#119834](https://github.com/rust-lang/rust/issues/119834))

Returns a raw pointer to a slice containing the entire array.

##### [§](#examples-24)Examples

```rust
#![feature(array_ptr_get)]

let arr: *const [i32; 3] = &[1, 2, 4] as *const [i32; 3];
let slice: *const [i32] = arr.as_slice();
assert_eq!(slice.len(), 3);
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#8)[§](#impl-*mut+T)

1.0.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#22)

Returns `true` if the pointer is null.

Note that unsized types have many possible null pointers, as only the raw data pointer is considered, not their length, vtable, etc. Therefore, two pointers that are null may still not compare equal to each other.

##### [§](#panics-during-const-evaluation-4)Panics during const evaluation

If this method is used during const evaluation, and `self` is a pointer that is offset beyond the bounds of the memory it initially pointed to, then there might not be enough information to determine whether the pointer is null. This is because the absolute address in memory is not known at compile time. If the nullness of the pointer cannot be determined, this method will panic.

In-bounds pointers are never null, so the method will never panic for such pointers.

##### [§](#examples-25)Examples

```rust
let mut s = [1, 2, 3];
let ptr: *mut u32 = s.as_mut_ptr();
assert!(!ptr.is_null());
```

1.38.0 (const: 1.38.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#31)

Casts to a pointer of another type.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#57)

🔬This is a nightly-only experimental API. (`pointer_try_cast_aligned` [#141221](https://github.com/rust-lang/rust/issues/141221))

Try to cast to a pointer of another type by checking alignment.

If the pointer is properly aligned to the target type, it will be cast to the target type. Otherwise, `None` is returned.

##### [§](#examples-26)Examples

```rust
#![feature(pointer_try_cast_aligned)]

let mut x = 0u64;

let aligned: *mut u64 = &mut x;
let unaligned = unsafe { aligned.byte_add(1) };

assert!(aligned.try_cast_aligned::<u32>().is_some());
assert!(unaligned.try_cast_aligned::<u32>().is_none());
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#113-115)

🔬This is a nightly-only experimental API. (`set_ptr_value` [#75091](https://github.com/rust-lang/rust/issues/75091))

Uses the address value in a new pointer of another type.

This operation will ignore the address part of its `meta` operand and discard existing metadata of `self`. For pointers to a sized types (thin pointers), this has the same effect as a simple cast. For pointers to an unsized type (fat pointers) this recombines the address with new metadata such as slice lengths or `dyn`-vtable.

The resulting pointer will have provenance of `self`. This operation is semantically the same as creating a new pointer with the data pointer value of `self` but the metadata of `meta`, being fat or thin depending on the `meta` operand.

##### [§](#examples-27)Examples

This function is primarily useful for enabling pointer arithmetic on potentially fat pointers. The pointer is cast to a sized pointee to utilize offset operations and then recombined with its own original metadata.

```rust
#![feature(set_ptr_value)]
let mut arr: [i32; 3] = [1, 2, 3];
let mut ptr = arr.as_mut_ptr() as *mut dyn Debug;
let thin = ptr as *mut u8;
unsafe {
    ptr = thin.add(8).with_metadata_of(ptr);
    println!("{:?}", &*ptr); // will print "3"
}
```

##### [§](#incorrect-usage-1)*Incorrect* usage

The provenance from pointers is *not* combined. The result must only be used to refer to the address allowed by `self`.

```rust
#![feature(set_ptr_value)]
let mut x = 0u32;
let mut y = 1u32;

let x = (&mut x) as *mut u32;
let y = (&mut y) as *mut u32;

let offset = (x as usize - y as usize) / 4;
let bad = x.wrapping_add(offset).with_metadata_of(y);

// This dereference is UB. The pointer only has provenance for `x` but points to `y`.
println!("{:?}", unsafe { &*bad });
```

1.65.0 (const: 1.65.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#134)

Changes constness without changing the type.

This is a bit safer than `as` because it wouldn’t silently change the type if the code is refactored.

While not strictly required (`*mut T` coerces to `*const T`), this is provided for symmetry with [`cast_mut`](https://doc.rust-lang.org/std/primitive.pointer.html#method.cast_mut "method pointer::cast_mut") on `*const T` and may have documentation value if used instead of implicit coercion.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#144)

Gets the “address” portion of the pointer.

This is similar to `self as usize`, except that the [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") of the pointer is discarded and not [exposed](https://doc.rust-lang.org/std/ptr/index.html#exposed-provenance "mod std::ptr"). This means that casting the returned address back to a pointer yields a [pointer without provenance](https://doc.rust-lang.org/std/ptr/fn.without_provenance_mut.html "fn std::ptr::without_provenance_mut"), which is undefined behavior to dereference. To properly restore the lost information and obtain a dereferenceable pointer, use [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr") or [`map_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.map_addr "method pointer::map_addr").

If using those APIs is not possible because there is no way to preserve a pointer with the required provenance, then Strict Provenance might not be for you. Use pointer-integer casts or [`expose_provenance`](https://doc.rust-lang.org/std/primitive.pointer.html#method.expose_provenance "method pointer::expose_provenance") and [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html "fn std::ptr::with_exposed_provenance") instead. However, note that this makes your code less portable and less amenable to tools that check for compliance with the Rust memory model.

On most platforms this will produce a value with the same bytes as the original pointer, because all the bytes are dedicated to describing the address. Platforms which need to store additional information in the pointer may perform a change of representation to produce a value containing only the address portion of the pointer. What that means is up to the platform to define.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#177)

Exposes the [“provenance”](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") part of the pointer for future use in [`with_exposed_provenance_mut`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance_mut.html "fn std::ptr::with_exposed_provenance_mut") and returns the “address” portion.

This is equivalent to `self as usize`, which semantically discards provenance information. Furthermore, this (like the `as` cast) has the implicit side-effect of marking the provenance as ‘exposed’, so on platforms that support it you can later call [`with_exposed_provenance_mut`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance_mut.html "fn std::ptr::with_exposed_provenance_mut") to reconstitute the original pointer including its provenance.

Due to its inherent ambiguity, [`with_exposed_provenance_mut`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance_mut.html "fn std::ptr::with_exposed_provenance_mut") may not be supported by tools that help you to stay conformant with the Rust memory model. It is recommended to use [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") APIs such as [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr") wherever possible, in which case [`addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") should be used instead of `expose_provenance`.

On most platforms this will produce a value with the same bytes as the original pointer, because all the bytes are dedicated to describing the address. Platforms which need to store additional information in the pointer may not support this operation, since the ‘expose’ side-effect which is required for [`with_exposed_provenance_mut`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance_mut.html "fn std::ptr::with_exposed_provenance_mut") to work is typically not available.

This is an [Exposed Provenance](https://doc.rust-lang.org/std/ptr/index.html#exposed-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#195)

Creates a new pointer with the given address and the [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") of `self`.

This is similar to a `addr as *mut T` cast, but copies the *provenance* of `self` to the new pointer. This avoids the inherent ambiguity of the unary cast.

This is equivalent to using [`wrapping_offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_offset "method pointer::wrapping_offset") to offset `self` to the given address, and therefore has all the same capabilities and restrictions.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

1.84.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#214)

Creates a new pointer by mapping `self`’s address to a new one, preserving the original pointer’s [provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr").

This is a convenience for [`with_addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.with_addr "method pointer::with_addr"), see that method for details.

This is a [Strict Provenance](https://doc.rust-lang.org/std/ptr/index.html#strict-provenance "mod std::ptr") API.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#223)

🔬This is a nightly-only experimental API. (`ptr_metadata` [#81513](https://github.com/rust-lang/rust/issues/81513))

Decompose a (possibly wide) pointer into its data pointer and metadata components.

The pointer can be later reconstructed with [`from_raw_parts_mut`](https://doc.rust-lang.org/std/ptr/fn.from_raw_parts_mut.html "fn std::ptr::from_raw_parts_mut").

1.9.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#262)

Returns `None` if the pointer is null, or else returns a shared reference to the value wrapped in `Some`. If the value may be uninitialized, [`as_uninit_ref`](#method.as_uninit_ref-1) must be used instead. If the value is known to be non-null, [`as_ref_unchecked`](#method.as_ref_unchecked-1) can be used instead.

##### [§](#safety-12)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#panics-during-const-evaluation-5)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null-1) for more information.

##### [§](#null-unchecked-version-1)Null-unchecked version

If you are sure the pointer can never be null, you can use `as_ref_unchecked` which returns `&mut T` instead of `Option<&mut T>`.

```rust
let ptr: *mut u8 = &mut 10u8 as *mut u8;

unsafe {
    let val_back = ptr.as_ref_unchecked();
    println!("We got back the value: {val_back}!");
}
```

##### [§](#examples-28)Examples

```rust
let ptr: *mut u8 = &mut 10u8 as *mut u8;

unsafe {
    if let Some(val_back) = ptr.as_ref() {
        println!("We got back the value: {val_back}!");
    }
}
```

##### [§](#see-also)See Also

For the mutable counterpart see [`as_mut`](#method.as_mut).

1.95.0 (const: 1.95.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#295)

Returns a shared reference to the value behind the pointer. If the pointer may be null or the value may be uninitialized, [`as_uninit_ref`](#method.as_uninit_ref) must be used instead. If the pointer may be null, but the value is known to have been initialized, [`as_ref`](#method.as_ref) must be used instead.

For the mutable counterpart see [`as_mut_unchecked`](#method.as_mut_unchecked).

##### [§](#safety-13)Safety

When calling this method, you have to ensure that the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#examples-29)Examples

```rust
let ptr: *mut u8 = &mut 10u8 as *mut u8;

unsafe {
    println!("We got back the value: {}!", ptr.as_ref_unchecked());
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#325-327)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a shared reference to the value wrapped in `Some`. In contrast to [`as_ref`](https://doc.rust-lang.org/std/primitive.pointer.html#method.as_ref-1 "primitive pointer"), this does not require that the value has to be initialized.

##### [§](#safety-14)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr"). Note that because the created reference is to `MaybeUninit<T>`, the source pointer can point to uninitialized memory.

##### [§](#panics-during-const-evaluation-6)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null-1) for more information.

##### [§](#see-also-1)See Also

For the mutable counterpart see [`as_uninit_mut`](#method.as_uninit_mut).

##### [§](#examples-30)Examples

```rust
#![feature(ptr_as_uninit)]

let ptr: *mut u8 = &mut 10u8 as *mut u8;

unsafe {
    if let Some(val_back) = ptr.as_uninit_ref() {
        println!("We got back the value: {}!", val_back.assume_init());
    }
}
```

1.0.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#352-354)

Adds a signed offset to a pointer.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-15)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space. Note that “range” here refers to a half-open range as usual in Rust, i.e., `self..result` for non-negative offsets and `result..self` for negative offsets.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_offset`](#method.wrapping_offset) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-31)Examples

```rust
let mut s = [1, 2, 3];
let ptr: *mut u32 = s.as_mut_ptr();

unsafe {
    assert_eq!(2, *ptr.offset(1));
    assert_eq!(3, *ptr.offset(2));
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#407)

Adds a signed offset in bytes to a pointer.

`count` is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.16.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#465-467)

Adds a signed offset to a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-16)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to (this is called “[Provenance](https://doc.rust-lang.org/std/ptr/index.html#provenance)”). The pointer must not be used to read or write other allocations.

In other words, `let z = x.wrapping_offset((y as isize) - (x as isize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`offset`](#method.offset), this method basically delays the requirement of staying within the same allocation: [`offset`](#method.offset) is immediate Undefined Behavior when crossing object boundaries; `wrapping_offset` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`offset`](#method.offset) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_offset(o).wrapping_offset(o.wrapping_neg())` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-32)Examples

```rust
// Iterate using a raw pointer in increments of two elements
let mut data = [1u8, 2, 3, 4, 5];
let mut ptr: *mut u8 = data.as_mut_ptr();
let step = 2;
let end_rounded_up = ptr.wrapping_offset(6);

while ptr != end_rounded_up {
    unsafe {
        *ptr = 0;
    }
    ptr = ptr.wrapping_offset(step);
}
assert_eq!(&data, &[0, 2, 0, 4, 0]);
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#487)

Adds a signed offset in bytes to a pointer using wrapping arithmetic.

`count` is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_offset "method pointer::wrapping_offset") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#528)

🔬This is a nightly-only experimental API. (`ptr_mask` [#98290](https://github.com/rust-lang/rust/issues/98290))

Masks out bits of the pointer according to a mask.

This is convenience for `ptr.map_addr(|a| a & mask)`.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

###### [§](#examples-33)Examples

```rust
#![feature(ptr_mask)]
let mut v = 17_u32;
let ptr: *mut u32 = &mut v;

// `u32` is 4 bytes aligned,
// which means that lower 2 bits are always 0.
let tag_mask = 0b11;
let ptr_mask = !tag_mask;

// We can store something in these lower bits
let tagged_ptr = ptr.map_addr(|a| a | 0b10);

// Get the "tag" back
let tag = tagged_ptr.addr() & tag_mask;
assert_eq!(tag, 0b10);

// Note that `tagged_ptr` is unaligned, it's UB to read from/write to it.
// To get original pointer `mask` can be used:
let masked_ptr = tagged_ptr.mask(ptr_mask);
assert_eq!(unsafe { *masked_ptr }, 17);

unsafe { *masked_ptr = 0 };
assert_eq!(v, 0);
```

1.9.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#583)

Returns `None` if the pointer is null, or else returns a unique reference to the value wrapped in `Some`. If the value may be uninitialized, [`as_uninit_mut`](#method.as_uninit_mut) must be used instead. If the value is known to be non-null, [`as_mut_unchecked`](#method.as_mut_unchecked) can be used instead.

For the shared counterpart see [`as_ref`](https://doc.rust-lang.org/std/primitive.pointer.html#method.as_ref-1 "primitive pointer").

##### [§](#safety-17)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#panics-during-const-evaluation-7)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null-1) for more information.

##### [§](#examples-34)Examples

```rust
let mut s = [1, 2, 3];
let ptr: *mut u32 = s.as_mut_ptr();
let first_value = unsafe { ptr.as_mut().unwrap() };
*first_value = 4;
println!("{s:?}"); // It'll print: "[4, 2, 3]".
```

##### [§](#null-unchecked-version-2)Null-unchecked version

If you are sure the pointer can never be null, you can use `as_mut_unchecked` which returns `&mut T` instead of `Option<&mut T>`.

```rust
let mut s = [1, 2, 3];
let ptr: *mut u32 = s.as_mut_ptr();
let first_value = unsafe { ptr.as_mut_unchecked() };
*first_value = 4;
println!("{s:?}"); // It'll print: "[4, 2, 3]".
```

1.95.0 (const: 1.95.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#618)

Returns a unique reference to the value behind the pointer. If the pointer may be null or the value may be uninitialized, [`as_uninit_mut`](#method.as_uninit_mut) must be used instead. If the pointer may be null, but the value is known to have been initialized, [`as_mut`](#method.as_mut) must be used instead.

For the shared counterpart see [`as_ref_unchecked`](#method.as_mut_unchecked).

##### [§](#safety-18)Safety

When calling this method, you have to ensure that the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#examples-35)Examples

```rust
let mut s = [1, 2, 3];
let ptr: *mut u32 = s.as_mut_ptr();
let first_value = unsafe { ptr.as_mut_unchecked() };
*first_value = 4;
println!("{s:?}"); // It'll print: "[4, 2, 3]".
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#645-647)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a unique reference to the value wrapped in `Some`. In contrast to [`as_mut`](#method.as_mut), this does not require that the value has to be initialized.

For the shared counterpart see [`as_uninit_ref`](https://doc.rust-lang.org/std/primitive.pointer.html#method.as_uninit_ref-1 "primitive pointer").

##### [§](#safety-19)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* the pointer is [convertible to a reference](https://doc.rust-lang.org/std/ptr/index.html#pointer-to-reference-conversion "mod std::ptr").

##### [§](#panics-during-const-evaluation-8)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null-1) for more information.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#674-676)

🔬This is a nightly-only experimental API. (`const_raw_ptr_comparison` [#53020](https://github.com/rust-lang/rust/issues/53020))

Returns whether two pointers are guaranteed to be equal.

At runtime this function behaves like `Some(self == other)`. However, in some contexts (e.g., compile-time evaluation), it is not always possible to determine equality of two pointers, so this function may spuriously return `None` for pointers that later actually turn out to have its equality known. But when it returns `Some`, the pointers’ equality is guaranteed to be known.

The return value may change from `Some` to `None` and vice versa depending on the compiler version and unsafe code must not rely on the result of this function for soundness. It is suggested to only use this function for performance optimizations where spurious `None` return values by this function do not affect the outcome, but just the performance. The consequences of using this method to make runtime and compile-time code behave differently have not been explored. This method should not be used to introduce such differences, and it should also not be stabilized before we have a better understanding of this issue.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#701-703)

🔬This is a nightly-only experimental API. (`const_raw_ptr_comparison` [#53020](https://github.com/rust-lang/rust/issues/53020))

Returns whether two pointers are guaranteed to be inequal.

At runtime this function behaves like `Some(self != other)`. However, in some contexts (e.g., compile-time evaluation), it is not always possible to determine inequality of two pointers, so this function may spuriously return `None` for pointers that later actually turn out to have its inequality known. But when it returns `Some`, the pointers’ inequality is guaranteed to be known.

The return value may change from `Some` to `None` and vice versa depending on the compiler version and unsafe code must not rely on the result of this function for soundness. It is suggested to only use this function for performance optimizations where spurious `None` return values by this function do not affect the outcome, but just the performance. The consequences of using this method to make runtime and compile-time code behave differently have not been explored. This method should not be used to introduce such differences, and it should also not be stabilized before we have a better understanding of this issue.

1.47.0 (const: 1.65.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#793-795)

Calculates the distance between two pointers within the same allocation. The returned value is in units of T: the distance in bytes divided by `size_of::<T>()`.

This is equivalent to `(self as isize - origin as isize) / (size_of::<T>() as isize)`, except that it has a lot more opportunities for UB, in exchange for the compiler better understanding what you are doing.

The primary motivation of this method is for computing the `len` of an array/slice of `T` that you are currently representing as a “start” and “end” pointer (and “end” is “one past the end” of the array). In that case, `end.offset_from(start)` gets you the length of the array.

All of the following safety requirements are trivially satisfied for this usecase.

##### [§](#safety-20)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- `self` and `origin` must either
  
  - point to the same address, or
  - both be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to the same [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the memory range between the two pointers must be in bounds of that object. (See below for an example.)
- The distance between the pointers, in bytes, must be an exact multiple of the size of `T`.

As a consequence, the absolute distance between the pointers, in bytes, computed on mathematical integers (without “wrapping around”), cannot overflow an `isize`. This is implied by the in-bounds requirement, and the fact that no allocation can be larger than `isize::MAX` bytes.

The requirement for pointers to be derived from the same allocation is primarily needed for `const`-compatibility: the distance between pointers into *different* allocated objects is not known at compile-time. However, the requirement also exists at runtime and may be exploited by optimizations. If you wish to compute the difference between pointers that are not guaranteed to be from the same allocation, use `(self as isize - origin as isize) / size_of::<T>()`.

##### [§](#panics-4)Panics

This function panics if `T` is a Zero-Sized Type (“ZST”).

##### [§](#examples-36)Examples

Basic usage:

```rust
let mut a = [0; 5];
let ptr1: *mut i32 = &mut a[1];
let ptr2: *mut i32 = &mut a[3];
unsafe {
    assert_eq!(ptr2.offset_from(ptr1), 2);
    assert_eq!(ptr1.offset_from(ptr2), -2);
    assert_eq!(ptr1.offset(2), ptr2);
    assert_eq!(ptr2.offset(-2), ptr1);
}
```

*Incorrect* usage:

```rust
let ptr1 = Box::into_raw(Box::new(0u8));
let ptr2 = Box::into_raw(Box::new(1u8));
let diff = (ptr2 as isize).wrapping_sub(ptr1 as isize);
// Make ptr2_other an "alias" of ptr2.add(1), but derived from ptr1.
let ptr2_other = (ptr1 as *mut u8).wrapping_offset(diff).wrapping_offset(1);
assert_eq!(ptr2 as usize, ptr2_other as usize);
// Since ptr2_other and ptr2 are derived from pointers to different objects,
// computing their offset is undefined behavior, even though
// they point to addresses that are in-bounds of the same object!
unsafe {
    let one = ptr2_other.offset_from(ptr2); // Undefined Behavior! ⚠️
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#814)

Calculates the distance between two pointers within the same allocation. The returned value is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [`offset_from`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset_from "method pointer::offset_from") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation considers only the data pointers, ignoring the metadata.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#882-884)

Calculates the distance between two pointers within the same allocation, *where it’s known that `self` is equal to or greater than `origin`* . The returned value is in units of T: the distance in bytes is divided by `size_of::<T>()`.

This computes the same value that [`offset_from`](#method.offset_from) would compute, but with the added precondition that the offset is guaranteed to be non-negative. This method is equivalent to `usize::try_from(self.offset_from(origin)).unwrap_unchecked()`, but it provides slightly more information to the optimizer, which can sometimes allow it to optimize slightly better with some backends.

This method can be thought of as recovering the `count` that was passed to [`add`](#method.add) (or, with the parameters in the other order, to [`sub`](#method.sub)). The following are all equivalent, assuming that their safety preconditions are met:

```rust
ptr.offset_from_unsigned(origin) == count
origin.add(count) == ptr
ptr.sub(count) == origin
```

##### [§](#safety-21)Safety

- The distance between the pointers must be non-negative (`self >= origin`)
- *All* the safety conditions of [`offset_from`](#method.offset_from) apply to this method as well; see it for the full details.

Importantly, despite the return type of this method being able to represent a larger offset, it’s still *not permitted* to pass pointers which differ by more than `isize::MAX` *bytes*. As such, the result of this method will always be less than or equal to `isize::MAX as usize`.

##### [§](#panics-5)Panics

This function panics if `T` is a Zero-Sized Type (“ZST”).

##### [§](#examples-37)Examples

```rust
let mut a = [0; 5];
let p: *mut i32 = a.as_mut_ptr();
unsafe {
    let ptr1: *mut i32 = p.add(1);
    let ptr2: *mut i32 = p.add(3);

    assert_eq!(ptr2.offset_from_unsigned(ptr1), 2);
    assert_eq!(ptr1.add(2), ptr2);
    assert_eq!(ptr2.sub(2), ptr1);
    assert_eq!(ptr2.offset_from_unsigned(ptr2), 0);
}

// This would be incorrect, as the pointers are not correctly ordered:
// ptr1.offset_from(ptr2)
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#904)

Calculates the distance between two pointers within the same allocation, *where it’s known that `self` is equal to or greater than `origin`* . The returned value is in units of **bytes**.

This is purely a convenience for casting to a `u8` pointer and using [`offset_from_unsigned`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset_from_unsigned "method pointer::offset_from_unsigned") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation considers only the data pointers, ignoring the metadata.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#927-929)

Adds an unsigned offset to a pointer.

This can only move the pointer forward (or not move it). If you need to move forward or backward depending on the value, then you might want [`offset`](#method.offset) instead which takes a signed offset.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-22)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_add`](#method.wrapping_add) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-38)Examples

```rust
let mut s: String = "123".to_string();
let ptr: *mut u8 = s.as_mut_ptr();

unsafe {
    assert_eq!('2', *ptr.add(1) as char);
    assert_eq!('3', *ptr.add(2) as char);
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#979)

Adds an unsigned offset in bytes to a pointer.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [add](https://doc.rust-lang.org/std/primitive.pointer.html#method.add "method pointer::add") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1033-1035)

Subtracts an unsigned offset from a pointer.

This can only move the pointer backward (or not move it). If you need to move forward or backward depending on the value, then you might want [`offset`](#method.offset) instead which takes a signed offset.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-23)Safety

If any of the following conditions are violated, the result is Undefined Behavior:

- The offset in bytes, `count * size_of::<T>()`, computed on mathematical integers (without “wrapping around”), must fit in an `isize`.
- If the computed offset is non-zero, then `self` must be [derived from](https://doc.rust-lang.org/std/ptr/index.html#provenance "mod std::ptr") a pointer to some [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"), and the entire memory range between `self` and the result must be in bounds of that allocation. In particular, this range must not “wrap around” the edge of the address space.

Allocations can never be larger than `isize::MAX` bytes, so if the computed offset stays in bounds of the allocation, it is guaranteed to satisfy the first requirement. This implies, for instance, that `vec.as_ptr().add(vec.len())` (for `vec: Vec<T>`) is always safe.

Consider using [`wrapping_sub`](#method.wrapping_sub) instead if these constraints are difficult to satisfy. The only advantage of this method is that it enables more aggressive compiler optimizations.

##### [§](#examples-39)Examples

```rust
let s: &str = "123";

unsafe {
    let end: *const u8 = s.as_ptr().add(3);
    assert_eq!('3', *end.sub(1) as char);
    assert_eq!('2', *end.sub(2) as char);
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1091)

Subtracts an unsigned offset in bytes from a pointer.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [sub](https://doc.rust-lang.org/std/primitive.pointer.html#method.sub "method pointer::sub") on it. See that method for documentation and safety requirements.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1148-1150)

Adds an unsigned offset to a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-24)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to; it must not be used to read or write other allocations.

In other words, `let z = x.wrapping_add((y as usize) - (x as usize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`add`](#method.add), this method basically delays the requirement of staying within the same allocation: [`add`](#method.add) is immediate Undefined Behavior when crossing object boundaries; `wrapping_add` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`add`](#method.add) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_add(o).wrapping_sub(o)` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-40)Examples

```rust
// Iterate using a raw pointer in increments of two elements
let data = [1u8, 2, 3, 4, 5];
let mut ptr: *const u8 = data.as_ptr();
let step = 2;
let end_rounded_up = ptr.wrapping_add(6);

// This loop prints "1, 3, 5, "
while ptr != end_rounded_up {
    unsafe {
        print!("{}, ", *ptr);
    }
    ptr = ptr.wrapping_add(step);
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1168)

Adds an unsigned offset in bytes to a pointer using wrapping arithmetic.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_add](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_add "method pointer::wrapping_add") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.61.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1224-1226)

Subtracts an unsigned offset from a pointer using wrapping arithmetic.

`count` is in units of T; e.g., a `count` of 3 represents a pointer offset of `3 * size_of::<T>()` bytes.

##### [§](#safety-25)Safety

This operation itself is always safe, but using the resulting pointer is not.

The resulting pointer “remembers” the [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr") that `self` points to; it must not be used to read or write other allocations.

In other words, `let z = x.wrapping_sub((x as usize) - (y as usize))` does *not* make `z` the same as `y` even if we assume `T` has size `1` and there is no overflow: `z` is still attached to the object `x` is attached to, and dereferencing it is Undefined Behavior unless `x` and `y` point into the same allocation.

Compared to [`sub`](#method.sub), this method basically delays the requirement of staying within the same allocation: [`sub`](#method.sub) is immediate Undefined Behavior when crossing object boundaries; `wrapping_sub` produces a pointer but still leads to Undefined Behavior if a pointer is dereferenced when it is out-of-bounds of the object it is attached to. [`sub`](#method.sub) can be optimized better and is thus preferable in performance-sensitive code.

The delayed check only considers the value of the pointer that was dereferenced, not the intermediate values used during the computation of the final result. For example, `x.wrapping_add(o).wrapping_sub(o)` is always the same as `x`. In other words, leaving the allocation and then re-entering it later is permitted.

##### [§](#examples-41)Examples

```rust
// Iterate using a raw pointer in increments of two elements (backwards)
let data = [1u8, 2, 3, 4, 5];
let mut ptr: *const u8 = data.as_ptr();
let start_rounded_down = ptr.wrapping_sub(2);
ptr = ptr.wrapping_add(4);
let step = 2;
// This loop prints "5, 3, 1, "
while ptr != start_rounded_down {
    unsafe {
        print!("{}, ", *ptr);
    }
    ptr = ptr.wrapping_sub(step);
}
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1244)

Subtracts an unsigned offset in bytes from a pointer using wrapping arithmetic.

`count` is in units of bytes.

This is purely a convenience for casting to a `u8` pointer and using [wrapping\_sub](https://doc.rust-lang.org/std/primitive.pointer.html#method.wrapping_sub "method pointer::wrapping_sub") on it. See that method for documentation.

For non-`Sized` pointees this operation changes only the data pointer, leaving the metadata untouched.

1.26.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1258-1260)

Reads the value from `self` without moving it. This leaves the memory in `self` unchanged.

See [`ptr::read`](https://doc.rust-lang.org/std/ptr/fn.read.html "fn std::ptr::read") for safety concerns and examples.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1279-1281)

Performs a volatile read of the value from `self` without moving it. This leaves the memory in `self` unchanged.

Volatile operations are intended to act on I/O memory, and are guaranteed to not be elided or reordered by the compiler across other volatile operations.

See [`ptr::read_volatile`](https://doc.rust-lang.org/std/ptr/fn.read_volatile.html "fn std::ptr::read_volatile") for safety concerns and examples.

1.26.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1299-1301)

Reads the value from `self` without moving it. This leaves the memory in `self` unchanged.

Unlike `read`, the pointer may be unaligned.

See [`ptr::read_unaligned`](https://doc.rust-lang.org/std/ptr/fn.read_unaligned.html "fn std::ptr::read_unaligned") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1319-1321)

Copies `count * size_of::<T>()` bytes from `self` to `dest`. The source and destination may overlap.

NOTE: this has the *same* argument order as [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy").

See [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1339-1341)

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1359-1361)

Copies `count * size_of::<T>()` bytes from `src` to `self`. The source and destination may overlap.

NOTE: this has the *opposite* argument order of [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy").

See [`ptr::copy`](https://doc.rust-lang.org/std/ptr/fn.copy.html "fn std::ptr::copy") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1379-1381)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/109342 "Tracking issue for const_drop_in_place")) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1395-1397)

Executes the destructor (if any) of the pointed-to value.

See [`ptr::drop_in_place`](https://doc.rust-lang.org/std/ptr/fn.drop_in_place.html "fn std::ptr::drop_in_place") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1413-1415)

Overwrites a memory location with the given value without reading or dropping the old value.

See [`ptr::write`](https://doc.rust-lang.org/std/ptr/fn.write.html "fn std::ptr::write") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1432-1434)

Invokes memset on the specified pointer, setting `count * size_of::<T>()` bytes of memory starting at `self` to `val`.

See [`ptr::write_bytes`](https://doc.rust-lang.org/std/ptr/fn.write_bytes.html "fn std::ptr::write_bytes") for safety concerns and examples.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1453-1455)

Performs a volatile write of a memory location with the given value without reading or dropping the old value.

Volatile operations are intended to act on I/O memory, and are guaranteed to not be elided or reordered by the compiler across other volatile operations.

See [`ptr::write_volatile`](https://doc.rust-lang.org/std/ptr/fn.write_volatile.html "fn std::ptr::write_volatile") for safety concerns and examples.

1.26.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1473-1475)

Overwrites a memory location with the given value without reading or dropping the old value.

Unlike `write`, the pointer may be unaligned.

See [`ptr::write_unaligned`](https://doc.rust-lang.org/std/ptr/fn.write_unaligned.html "fn std::ptr::write_unaligned") for safety concerns and examples.

1.26.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1490-1492)

Replaces the value at `self` with `src`, returning the old value, without dropping either.

See [`ptr::replace`](https://doc.rust-lang.org/std/ptr/fn.replace.html "fn std::ptr::replace") for safety concerns and examples.

1.26.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1508-1510)

Swaps the values at two mutable locations of the same type, without deinitializing either. They may overlap, unlike `mem::swap` which is otherwise equivalent.

See [`ptr::swap`](https://doc.rust-lang.org/std/ptr/fn.swap.html "fn std::ptr::swap") for safety concerns and examples.

1.36.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1557-1559)

Computes the offset that needs to be applied to the pointer in order to make it aligned to `align`.

If it is not possible to align the pointer, the implementation returns `usize::MAX`.

The offset is expressed in number of `T` elements, and not bytes. The value returned can be used with the `wrapping_add` method.

There are no guarantees whatsoever that offsetting the pointer will not overflow or go beyond the allocation that the pointer points into. It is up to the caller to ensure that the returned offset is correct in all terms other than alignment.

##### [§](#panics-6)Panics

The function panics if `align` is not a power-of-two.

##### [§](#examples-42)Examples

Accessing adjacent `u8` as `u16`

```rust
let mut x = [5_u8, 6, 7, 8, 9];
let ptr = x.as_mut_ptr();
let offset = ptr.align_offset(align_of::<u16>());

if offset < x.len() - 1 {
    let u16_ptr = ptr.add(offset).cast::<u16>();
    *u16_ptr = 0;

    assert!(x == [0, 0, 7, 8, 9] || x == [5, 0, 0, 8, 9]);
} else {
    // while the pointer can be aligned via `offset`, it would point
    // outside the allocation
}
```

1.79.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1598-1600)

Returns whether the pointer is properly aligned for `T`.

##### [§](#examples-43)Examples

```rust
// On some platforms, the alignment of i32 is less than 4.
#[repr(align(4))]
struct AlignedI32(i32);

let mut data = AlignedI32(42);
let ptr = &mut data as *mut AlignedI32;

assert!(ptr.is_aligned());
assert!(!ptr.wrapping_byte_add(1).is_aligned());
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1638)

🔬This is a nightly-only experimental API. (`pointer_is_aligned_to` [#96284](https://github.com/rust-lang/rust/issues/96284))

Returns whether the pointer is aligned to `align`.

For non-`Sized` pointees this operation considers only the data pointer, ignoring the metadata.

##### [§](#panics-7)Panics

The function panics if `align` is not a power-of-two (this includes 0).

##### [§](#examples-44)Examples

```rust
#![feature(pointer_is_aligned_to)]

// On some platforms, the alignment of i32 is less than 4.
#[repr(align(4))]
struct AlignedI32(i32);

let mut data = AlignedI32(42);
let ptr = &mut data as *mut AlignedI32;

assert!(ptr.is_aligned_to(1));
assert!(ptr.is_aligned_to(2));
assert!(ptr.is_aligned_to(4));

assert!(ptr.wrapping_byte_add(2).is_aligned_to(2));
assert!(!ptr.wrapping_byte_add(2).is_aligned_to(4));

assert_ne!(ptr.is_aligned_to(8), ptr.wrapping_add(1).is_aligned_to(8));
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1647)[§](#impl-*mut+T-1)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1655)

🔬This is a nightly-only experimental API. (`cast_maybe_uninit` [#145036](https://github.com/rust-lang/rust/issues/145036))

Casts from a type to its maybe-uninitialized version.

This is always safe, since UB can only occur if the pointer is read before being initialized.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1700)

🔬This is a nightly-only experimental API. (`ptr_cast_slice` [#149103](https://github.com/rust-lang/rust/issues/149103))

Forms a raw mutable slice from a pointer and a length.

The `len` argument is the number of **elements**, not the number of bytes.

Performs the same functionality as [`cast_slice`](https://doc.rust-lang.org/std/primitive.pointer.html#method.cast_slice "method pointer::cast_slice") on a `*const T`, except that a raw mutable slice is returned, as opposed to a raw immutable slice.

This function is safe, but actually using the return value is unsafe. See the documentation of [`slice::from_raw_parts_mut`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts_mut.html "fn std::slice::from_raw_parts_mut") for slice safety requirements.

##### [§](#examples-45)Examples

```rust
#![feature(ptr_cast_slice)]

let x = &mut [5, 6, 7];
let slice = x.as_mut_ptr().cast_slice(3);

unsafe {
    (*slice)[2] = 99; // assign a value at an index in the slice
};

assert_eq!(unsafe { &*slice }[2], 99);
```

You must ensure that the pointer is valid and not null before dereferencing the raw slice. A slice reference must never have a null pointer, even if it’s empty.

[ⓘ](# "This example panics")

```rust
#![feature(ptr_cast_slice)]
use std::ptr;
let danger: *mut [u8] = ptr::null_mut::<u8>().cast_slice(0);
unsafe {
    danger.as_mut().expect("references must not be null");
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1704)[§](#impl-*mut+MaybeUninit%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1712)

🔬This is a nightly-only experimental API. (`cast_maybe_uninit` [#145036](https://github.com/rust-lang/rust/issues/145036))

Casts from a maybe-uninitialized type to its initialized version.

This is always safe, since UB can only occur if the pointer is read before being initialized.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1717)[§](#impl-*mut+%5BT%5D)

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1736)

Returns the length of a raw slice.

The returned value is the number of **elements**, not the number of bytes.

This function is safe, even when the raw slice cannot be cast to a slice reference because the pointer is null or unaligned.

##### [§](#examples-46)Examples

```rust
use std::ptr;

let slice: *mut [i8] = ptr::slice_from_raw_parts_mut(ptr::null_mut(), 3);
assert_eq!(slice.len(), 3);
```

1.79.0 (const: 1.79.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1753)

Returns `true` if the raw slice has a length of 0.

##### [§](#examples-47)Examples

```rust
use std::ptr;

let slice: *mut [i8] = ptr::slice_from_raw_parts_mut(ptr::null_mut(), 3);
assert!(!slice.is_empty());
```

1.93.0 (const: 1.93.0) · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1764)

Gets a raw, mutable pointer to the underlying array.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1815)

🔬This is a nightly-only experimental API. (`raw_slice_split` [#95595](https://github.com/rust-lang/rust/issues/95595))

Divides one mutable raw slice into two at an index.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### [§](#panics-8)Panics

Panics if `mid > len`.

##### [§](#safety-26)Safety

`mid` must be [in-bounds](#method.add) of the underlying [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"). Which means `self` must be dereferenceable and span a single allocation that is at least `mid * size_of::<T>()` bytes long. Not upholding these requirements is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointers are not used.

Since `len` being in-bounds is not a safety invariant of `*mut [T]` the safety requirements of this method are the same as for [`split_at_mut_unchecked`](#method.split_at_mut_unchecked). The explicit bounds check is only as useful as `len` is correct.

##### [§](#examples-48)Examples

```rust
#![feature(raw_slice_split)]

let mut v = [1, 0, 3, 0, 5, 6];
let ptr = &mut v as *mut [_];
unsafe {
    let (left, right) = ptr.split_at_mut(2);
    assert_eq!(&*left, [1, 0]);
    assert_eq!(&*right, [3, 0, 5, 6]);
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1859)

🔬This is a nightly-only experimental API. (`raw_slice_split` [#95595](https://github.com/rust-lang/rust/issues/95595))

Divides one mutable raw slice into two at an index, without doing bounds checking.

The first will contain all indices from `[0, mid)` (excluding the index `mid` itself) and the second will contain all indices from `[mid, len)` (excluding the index `len` itself).

##### [§](#safety-27)Safety

`mid` must be [in-bounds](#method.add) of the underlying [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr"). Which means `self` must be dereferenceable and span a single allocation that is at least `mid * size_of::<T>()` bytes long. Not upholding these requirements is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointers are not used.

##### [§](#examples-49)Examples

```rust
#![feature(raw_slice_split)]

let mut v = [1, 0, 3, 0, 5, 6];
// scoped to restrict the lifetime of the borrows
unsafe {
    let ptr = &mut v as *mut [_];
    let (left, right) = ptr.split_at_mut_unchecked(2);
    assert_eq!(&*left, [1, 0]);
    assert_eq!(&*right, [3, 0, 5, 6]);
    (&mut *left)[1] = 2;
    (&mut *right)[1] = 4;
}
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1886)

🔬This is a nightly-only experimental API. (`slice_ptr_get` [#74265](https://github.com/rust-lang/rust/issues/74265))

Returns a raw pointer to the slice’s buffer.

This is equivalent to casting `self` to `*mut T`, but more type-safe.

##### [§](#examples-50)Examples

```rust
#![feature(slice_ptr_get)]
use std::ptr;

let slice: *mut [i8] = ptr::slice_from_raw_parts_mut(ptr::null_mut(), 3);
assert_eq!(slice.as_mut_ptr(), ptr::null_mut());
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1913-1915)

🔬This is a nightly-only experimental API. (`slice_ptr_get` [#74265](https://github.com/rust-lang/rust/issues/74265))

Returns a raw pointer to an element or subslice, without doing bounds checking.

Calling this method with an [out-of-bounds index](#method.add) or when `self` is not dereferenceable is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointer is not used.

##### [§](#examples-51)Examples

```rust
#![feature(slice_ptr_get)]

let x = &mut [1, 2, 4] as *mut [i32];

unsafe {
    assert_eq!(x.get_unchecked_mut(1), x.as_mut_ptr().add(1));
}
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1927)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a shared slice to the value wrapped in `Some`. In contrast to [`as_ref`](#method.as_ref), this does not require that the value has to be initialized.

##### [§](#safety-28)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* all of the following is true:

- The pointer must be [valid](https://doc.rust-lang.org/std/ptr/index.html#safety "mod std::ptr") for reads for `ptr.len() * size_of::<T>()` many bytes, and it must be properly aligned. This means in particular:
- The entire memory range of this slice must be contained within a single [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr")! Slices can never span across multiple allocations.
- The pointer must be aligned even for zero-length slices. One reason for this is that enum layout optimizations may rely on references (including slices of any length) being aligned and non-null to distinguish them from other data. You can obtain a pointer that is usable as `data` for zero-length slices using [`NonNull::dangling()`](https://doc.rust-lang.org/std/ptr/struct.NonNull.html#method.dangling "associated function std::ptr::NonNull::dangling").
- The total size `ptr.len() * size_of::<T>()` of the slice must be no larger than `isize::MAX`. See the safety documentation of [`pointer::offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset").
- You must enforce Rust’s aliasing rules, since the returned lifetime `'a` is arbitrarily chosen and does not necessarily reflect the actual lifetime of the data. In particular, while this reference exists, the memory the pointer points to must not get mutated (except inside `UnsafeCell`).

This applies even if the result of this method is unused!

See also [`slice::from_raw_parts`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html "fn std::slice::from_raw_parts").

##### [§](#panics-during-const-evaluation-9)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null) for more information.

##### [§](#see-also-2)See Also

For the mutable counterpart see [`as_uninit_slice_mut`](https://doc.rust-lang.org/std/primitive.pointer.html#method.as_uninit_slice_mut "method pointer::as_uninit_slice_mut").

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1985)

🔬This is a nightly-only experimental API. (`ptr_as_uninit` [#75402](https://github.com/rust-lang/rust/issues/75402))

Returns `None` if the pointer is null, or else returns a unique slice to the value wrapped in `Some`. In contrast to [`as_mut`](#method.as_mut), this does not require that the value has to be initialized.

For the shared counterpart see [`as_uninit_slice`](#method.as_uninit_slice-1).

##### [§](#safety-29)Safety

When calling this method, you have to ensure that *either* the pointer is null *or* all of the following is true:

- The pointer must be [valid](https://doc.rust-lang.org/std/ptr/index.html#safety "mod std::ptr") for reads and writes for `ptr.len() * size_of::<T>()` many bytes, and it must be properly aligned. This means in particular:
  
  - The entire memory range of this slice must be contained within a single [allocation](https://doc.rust-lang.org/std/ptr/index.html#allocation "mod std::ptr")! Slices can never span across multiple allocations.
  - The pointer must be aligned even for zero-length slices. One reason for this is that enum layout optimizations may rely on references (including slices of any length) being aligned and non-null to distinguish them from other data. You can obtain a pointer that is usable as `data` for zero-length slices using [`NonNull::dangling()`](https://doc.rust-lang.org/std/ptr/struct.NonNull.html#method.dangling "associated function std::ptr::NonNull::dangling").
- The total size `ptr.len() * size_of::<T>()` of the slice must be no larger than `isize::MAX`. See the safety documentation of [`pointer::offset`](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset "method pointer::offset").
- You must enforce Rust’s aliasing rules, since the returned lifetime `'a` is arbitrarily chosen and does not necessarily reflect the actual lifetime of the data. In particular, while this reference exists, the memory the pointer points to must not get accessed (read or written) through any other pointer.

This applies even if the result of this method is unused!

See also [`slice::from_raw_parts_mut`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts_mut.html "fn std::slice::from_raw_parts_mut").

##### [§](#panics-during-const-evaluation-10)Panics during const evaluation

This method will panic during const evaluation if the pointer cannot be determined to be null or not. See [`is_null`](#method.is_null-1) for more information.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1995)[§](#impl-*mut+T-2)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#1999)

🔬This is a nightly-only experimental API. (`ptr_cast_array` [#144514](https://github.com/rust-lang/rust/issues/144514))

Casts from a pointer-to-`T` to a pointer-to-`[T; N]`.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2004)[§](#impl-*mut+%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2020)

🔬This is a nightly-only experimental API. (`array_ptr_get` [#119834](https://github.com/rust-lang/rust/issues/119834))

Returns a raw pointer to the array’s buffer.

This is equivalent to casting `self` to `*mut T`, but more type-safe.

##### [§](#examples-52)Examples

```rust
#![feature(array_ptr_get)]
use std::ptr;

let arr: *mut [i8; 3] = ptr::null_mut();
assert_eq!(arr.as_mut_ptr(), ptr::null_mut());
```

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2040)

🔬This is a nightly-only experimental API. (`array_ptr_get` [#119834](https://github.com/rust-lang/rust/issues/119834))

Returns a raw pointer to a mutable slice containing the entire array.

##### [§](#examples-53)Examples

```rust
#![feature(array_ptr_get)]

let mut arr = [1, 2, 5];
let ptr: *mut [i32; 3] = &mut arr;
unsafe {
    (&mut *ptr.as_mut_slice())[..2].copy_from_slice(&[3, 4]);
}
assert_eq!(arr, [3, 4, 5]);
```

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#328)[§](#impl-AtomicPrimitive-for-*mut+T)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#328)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#650)[§](#impl-Clone-for-*const+T)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#664)[§](#impl-Clone-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#3058)[§](#impl-Debug-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#3064)[§](#impl-Debug-for-*mut+T)

1.88.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1686)[§](#impl-Default-for-*const+T)

1.88.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2126)[§](#impl-Default-for-*mut+T)

1.23.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#2496)[§](#impl-From%3C*mut+T%3E-for-AtomicPtr%3CT%3E)

Available on **`target_has_atomic_load_store=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#2499)[§](#method.from)

Converts a `*mut T` into an `AtomicPtr<T>`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#956)[§](#impl-Hash-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#966)[§](#impl-Hash-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1633)[§](#impl-Ord-for-*const+T)

Pointer comparison is by address, as produced by the `[`&lt;\*const T&gt;::addr`](pointer::addr)` method.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2073)[§](#impl-Ord-for-*mut+T)

Pointer comparison is by address, as produced by the [`<*mut T>::addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") method.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1611)[§](#impl-PartialEq-for-*const+T)

Pointer equality is by address, as produced by the [`<*const T>::addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") method.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1614)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2051)[§](#impl-PartialEq-for-*mut+T)

Pointer equality is by address, as produced by the [`<*mut T>::addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") method.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2054)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1653)[§](#impl-PartialOrd-for-*const+T)

Pointer comparison is by address, as produced by the `[`&lt;\*const T&gt;::addr`](pointer::addr)` method.

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1656)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1662)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1668)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1674)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1680)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2093)[§](#impl-PartialOrd-for-*mut+T)

Pointer comparison is by address, as produced by the [`<*mut T>::addr`](https://doc.rust-lang.org/std/primitive.pointer.html#method.addr "method pointer::addr") method.

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2096)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2102)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2108)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2114)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2120)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#2990)[§](#impl-Pointer-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#3035)[§](#impl-Pointer-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1169-1171)[§](#impl-SimdElement-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1173)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1181-1183)[§](#impl-SimdElement-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1185)[§](#associatedtype.Mask-1)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#58)[§](#impl-CoerceUnsized%3C*const+U%3E-for-%26T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#51)[§](#impl-CoerceUnsized%3C*const+U%3E-for-%26mut+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#69)[§](#impl-CoerceUnsized%3C*const+U%3E-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#65)[§](#impl-CoerceUnsized%3C*const+U%3E-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#48)[§](#impl-CoerceUnsized%3C*mut+U%3E-for-%26mut+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#62)[§](#impl-CoerceUnsized%3C*mut+U%3E-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#131)[§](#impl-DispatchFromDyn%3C*const+U%3E-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/ops/unsize.rs.html#134)[§](#impl-DispatchFromDyn%3C*mut+U%3E-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/const_ptr.rs.html#1625)[§](#impl-Eq-for-*const+T)

Pointer equality is an equivalence relation.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ptr/mut_ptr.rs.html#2065)[§](#impl-Eq-for-*mut+T)

Pointer equality is an equivalence relation.

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#913-921)[§](#impl-Freeze-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#913-921)[§](#impl-Freeze-for-*mut+T)

1.33.0 · [Source](https://doc.rust-lang.org/src/core/pin.rs.html#1857)[§](#impl-PinCoerceUnsized-for-*const+T)

1.33.0 · [Source](https://doc.rust-lang.org/src/core/pin.rs.html#1860)[§](#impl-PinCoerceUnsized-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#100)[§](#impl-Send-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#102)[§](#impl-Send-for-*mut+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#675)[§](#impl-Sync-for-*const+T)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#677)[§](#impl-Sync-for-*mut+T)

1.38.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#1046-1051)[§](#impl-Unpin-for-*const+T)

1.38.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#1046-1051)[§](#impl-Unpin-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#935-943)[§](#impl-UnsafeUnpin-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#935-943)[§](#impl-UnsafeUnpin-for-*mut+T)

1.9.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#185)[§](#impl-UnwindSafe-for-*const+T)

1.9.0 · [Source](https://doc.rust-lang.org/src/core/panic/unwind_safe.rs.html#187)[§](#impl-UnwindSafe-for-*mut+T)

[Source](https://doc.rust-lang.org/src/core/ffi/va_list.rs.html#315)[§](#impl-VaArgSafe-for-*const+T)

[Source](https://doc.rust-lang.org/src/core/ffi/va_list.rs.html#314)[§](#impl-VaArgSafe-for-*mut+T)