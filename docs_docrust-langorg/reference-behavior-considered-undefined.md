---
title: Behavior considered undefined - The Rust Reference
url: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
source: crawler
fetched_at: 2026-05-06T21:25:54.216466812-03:00
rendered_js: false
word_count: 1862
summary: This document defines the constraints and requirements for writing safe Rust code by outlining specific behaviors that trigger undefined behavior, particularly when using unsafe blocks.
tags:
    - rust
    - unsafe-rust
    - undefined-behavior
    - memory-safety
    - pointers
    - aliasing-rules
category: concept
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Behavior considered undefined](#behavior-considered-undefined)

Rust code is incorrect if it exhibits any of the behaviors in the following list. This includes code within `unsafe` blocks and `unsafe` functions. `unsafe` only means that avoiding undefined behavior is on the programmer; it does not change anything about the fact that Rust programs must never cause undefined behavior.

It is the programmer’s responsibility when writing `unsafe` code to ensure that any safe code interacting with the `unsafe` code cannot trigger these behaviors. `unsafe` code that satisfies this property for any safe client is called *sound*; if `unsafe` code can be misused by safe code to exhibit undefined behavior, it is *unsound*.

> Warning
> 
> The following list is not exhaustive; it may grow or shrink. There is no formal model of Rust’s semantics for what is and is not allowed in unsafe code, so there may be more behavior considered unsafe. We also reserve the right to make some of the behavior in that list defined in the future. In other words, this list does not say that anything will *definitely* always be undefined in all future Rust version (but we might make such commitments for some list items in the future).
> 
> Please read the [Rustonomicon](https://doc.rust-lang.org/nomicon/index.html) before writing unsafe code.

- Data races.

<!--THE END-->

- Accessing (loading from or storing to) a place that is [dangling](#dangling-pointers) or [based on a misaligned pointer](#places-based-on-misaligned-pointers).

<!--THE END-->

- Performing a place projection that violates the requirements of [in-bounds pointer arithmetic](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset). A place projection is a [field expression](https://doc.rust-lang.org/reference/expressions/field-expr.html), a [tuple index expression](https://doc.rust-lang.org/reference/expressions/tuple-expr.html#tuple-indexing-expressions), or an [array/slice index expression](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions).

<!--THE END-->

- Breaking the pointer aliasing rules. The exact aliasing rules are not determined yet, but here is an outline of the general principles: `&T` must point to memory that is not mutated while they are live (except for data inside an [`UnsafeCell<U>`](https://doc.rust-lang.org/core/cell/struct.UnsafeCell.html)), and `&mut T` must point to memory that is not read or written by any pointer not derived from the reference and that no other reference points to while they are live. `Box<T>` is treated similar to `&'static mut T` for the purpose of these rules. The exact liveness duration is not specified, but some bounds exist:
  
  - For references, the liveness duration is upper-bounded by the syntactic lifetime assigned by the borrow checker; it cannot be live any *longer* than that lifetime.
  - Each time a reference or box is dereferenced or reborrowed, it is considered live.
  - Each time a reference or box is passed to or returned from a function, it is considered live.
  - When a reference (but not a `Box`!) is passed to a function, it is live at least as long as that function call, again except if the `&T` contains an [`UnsafeCell<U>`](https://doc.rust-lang.org/core/cell/struct.UnsafeCell.html).
  
  All this also applies when values of these types are passed in a (nested) field of a compound type, but not behind pointer indirections.

<!--THE END-->

- Mutating immutable bytes. All bytes reachable through a [const-promoted](https://doc.rust-lang.org/reference/destructors.html#constant-promotion) expression are immutable, as well as bytes reachable through borrows in `static` and `const` initializers that have been [lifetime-extended](https://doc.rust-lang.org/reference/destructors.html#temporary-lifetime-extension) to `'static`. The bytes owned by an immutable binding or immutable `static` are immutable, unless those bytes are part of an [`UnsafeCell<U>`](https://doc.rust-lang.org/core/cell/struct.UnsafeCell.html).
  
  Moreover, the bytes [pointed to](#pointed-to-bytes) by a shared reference, including transitively through other references (both shared and mutable) and `Box`es, are immutable; transitivity includes those references stored in fields of compound types.
  
  A mutation is any write of more than 0 bytes which overlaps with any of the relevant bytes (even if that write does not change the memory contents).

<!--THE END-->

- Invoking undefined behavior via compiler intrinsics.

<!--THE END-->

- Executing code compiled with platform features that the current platform does not support (see [`target_feature`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-target_feature-attribute)), *except* if the platform explicitly documents this to be safe.

<!--THE END-->

- Calling a function with the wrong [call ABI](https://doc.rust-lang.org/reference/items/external-blocks.html#abi), or unwinding past a stack frame that does not allow unwinding (e.g. by calling a `"C-unwind"` function imported or transmuted as a `"C"` function or function pointer).

<!--THE END-->

- Producing an [invalid value](#invalid-values). “Producing” a value happens any time a value is assigned to or read from a place, passed to a function/primitive operation or returned from a function/primitive operation.

<!--THE END-->

- Incorrect use of inline assembly. For more details, refer to the [rules](https://doc.rust-lang.org/reference/inline-assembly.html#rules-for-inline-assembly) to follow when writing code that uses inline assembly.

<!--THE END-->

- Violating assumptions of the Rust runtime. Most assumptions of the Rust runtime are currently not explicitly documented.
  
  - For assumptions specifically related to unwinding, see the [panic documentation](https://doc.rust-lang.org/reference/panic.html#unwinding-across-ffi-boundaries).
  - The runtime assumes that a Rust stack frame is not deallocated without executing destructors for local variables owned by the stack frame. This assumption can be violated by C functions like `longjmp`.

> Note
> 
> Undefined behavior affects the entire program. For example, calling a function in C that exhibits undefined behavior of C means your entire program contains undefined behaviour that can also affect the Rust code. And vice versa, undefined behavior in Rust can cause adverse affects on code executed by any FFI calls to other languages.

## [Pointed-to bytes](#pointed-to-bytes)

The span of bytes a pointer or reference “points to” is determined by the pointer value and the size of the pointee type (using `size_of_val`).

## [Places based on misaligned pointers](#places-based-on-misaligned-pointers)

A place is said to be “based on a misaligned pointer” if the last `*` projection during place computation was performed on a pointer that was not aligned for its type. (If there is no `*` projection in the place expression, then this is accessing the field of a local or `static` and rustc will guarantee proper alignment. If there are multiple `*` projections, then each of them incurs a load of the pointer-to-be-dereferenced itself from memory, and each of these loads is subject to the alignment constraint. Note that some `*` projections can be omitted in surface Rust syntax due to automatic dereferencing; we are considering the fully expanded place expression here.)

For instance, if `ptr` has type `*const S` where `S` has an alignment of 8, then `ptr` must be 8-aligned or else `(*ptr).f` is “based on an misaligned pointer”. This is true even if the type of the field `f` is `u8` (i.e., a type with alignment 1). In other words, the alignment requirement derives from the type of the pointer that was dereferenced, *not* the type of the field that is being accessed.

Note that a place based on a misaligned pointer only leads to undefined behavior when it is loaded from or stored to.

`&raw const`/`&raw mut` on such a place is allowed.

`&`/`&mut` on a place requires the alignment of the field type (or else the program would be “producing an invalid value”), which generally is a less restrictive requirement than being based on an aligned pointer.

Taking a reference will lead to a compiler error in cases where the field type might be more aligned than the type that contains it, i.e., `repr(packed)`. This means that being based on an aligned pointer is always sufficient to ensure that the new reference is aligned, but it is not always necessary.

## [Dangling pointers](#dangling-pointers)

A reference/pointer is “dangling” if not all of the bytes it [points to](#pointed-to-bytes) are part of the same live allocation (so in particular they all have to be part of *some* allocation).

If the size is 0, then the pointer is trivially never “dangling” (even if it is a null pointer).

Note that dynamically sized types (such as slices and strings) point to their entire range, so it is important that the length metadata is never too large.

In particular, the dynamic size of a Rust value (as determined by `size_of_val`) must never exceed `isize::MAX`, since it is impossible for a single allocation to be larger than `isize::MAX`.

## [Invalid values](#invalid-values)

The Rust compiler assumes that all values produced during program execution are “valid”, and producing an invalid value is hence immediate UB.

Whether a value is valid depends on the type:

- A [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) value must be `false` (`0`) or `true` (`1`).

<!--THE END-->

- A `fn` pointer value must be non-null.

<!--THE END-->

- A `char` value must not be a surrogate (i.e., must not be in the range `0xD800..=0xDFFF`) and must be equal to or less than `char::MAX`.

<!--THE END-->

- A `!` value must never exist.

<!--THE END-->

- An integer (`i*`/`u*`), floating point value (`f*`), or raw pointer must be initialized, i.e., must not be obtained from uninitialized memory.

<!--THE END-->

- A `str` value is treated like `[u8]`, i.e. it must be initialized.

<!--THE END-->

- An `enum` must have a valid discriminant, and all fields of the variant indicated by that discriminant must be valid at their respective type.

<!--THE END-->

- A `struct`, tuple, and array requires all fields/elements to be valid at their respective type.

<!--THE END-->

- For a `union`, the exact validity requirements are not decided yet. Obviously, all values that can be created entirely in safe code are valid. If the union has a zero-sized field, then every possible value is valid. Further details are [still being debated](https://github.com/rust-lang/unsafe-code-guidelines/issues/438).

<!--THE END-->

- A reference or [`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html) must be aligned and non-null, it cannot be [dangling](#dangling-pointers), and it must point to a valid value (in case of dynamically sized types, using the actual dynamic type of the pointee as determined by the metadata). Note that the last point (about pointing to a valid value) remains a subject of some debate.

<!--THE END-->

- The metadata of a wide reference, [`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html), or raw pointer must match the type of the unsized tail:
  
  - `dyn Trait` metadata must be a pointer to a compiler-generated vtable for `Trait`. (For raw pointers, this requirement remains a subject of some debate.)
  - Slice (`[T]`) metadata must be a valid `usize`. Furthermore, for wide references and [`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html), slice metadata is invalid if it makes the total size of the pointed-to value bigger than `isize::MAX`.

<!--THE END-->

- If a type has a custom range of a valid values, then a valid value must be in that range. In the standard library, this affects [`NonNull<T>`](https://doc.rust-lang.org/core/ptr/non_null/struct.NonNull.html) and [`NonZero<T>`](https://doc.rust-lang.org/core/num/nonzero/struct.NonZero.html).
  
  > Note
  > 
  > `rustc` achieves this with the unstable `rustc_layout_scalar_valid_range_*` attributes.

<!--THE END-->

- **In [const contexts](https://doc.rust-lang.org/reference/const_eval.html#r-const-eval.const-context)**: In addition to what is described above, further provenance-related requirements apply during const evaluation. Any value that holds pure integer data (the `i*`/`u*`/`f*` types as well as `bool` and `char`, enum discriminants, and slice metadata) must not carry any provenance. Any value that holds pointer data (references, raw pointers, function pointers, and `dyn Trait` metadata) must either carry no provenance, or all bytes must be fragments of the same original pointer value in the correct order.
  
  This implies that transmuting or otherwise reinterpreting a pointer (reference, raw pointer, or function pointer) into a non-pointer type (such as integers) is undefined behavior if the pointer had provenance.
  
  > Example
  > 
  > All of the following are UB:
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  use core::mem::MaybeUninit;
  use core::ptr;
  // We cannot reinterpret a pointer with provenance as an integer,
  // as then the bytes of the integer will have provenance.
  const _: usize = {
      let ptr = &0;
      unsafe { (&raw const ptr as *const usize).read() }
  };
  
  // We cannot rearrange the bytes of a pointer with provenance and
  // then interpret them as a reference, as then a value holding
  // pointer data will have pointer fragments in the wrong order.
  const _: &i32 = {
      let mut ptr = &0;
      let ptr_bytes = &raw mut ptr as *mut MaybeUninit::<u8>;
      unsafe { ptr::swap(ptr_bytes.add(1), ptr_bytes.add(2)) };
      ptr
  };
  }
  > ```

**Note:** Uninitialized memory is also implicitly invalid for any type that has a restricted set of valid values. In other words, the only cases in which reading uninitialized memory is permitted are inside `union`s and in “padding” (the gaps between the fields of a type).