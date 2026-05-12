---
title: size_of in std::mem - Rust
url: https://doc.rust-lang.org/stable/std/mem/fn.size_of.html
source: crawler
fetched_at: 2026-05-06T21:25:27.397420467-03:00
rendered_js: false
word_count: 537
summary: This document describes the Rust function size_of, which returns the size of a given type in bytes, including detailed explanations of how size is calculated for primitives, pointers, structs, enums, and unions.
tags:
    - rust
    - memory-layout
    - type-size
    - data-structures
    - programming-reference
category: reference
---

## Function size\_of

1.0.0 (const: 1.24.0) · [Source](https://doc.rust-lang.org/stable/src/core/mem/mod.rs.html#344)

```rust
pub const fn size_of<T>() -> usize
```

Expand description

Returns the size of a type in bytes.

More specifically, this is the offset in bytes between successive elements in an array with that item type including alignment padding. Thus, for any type `T` and length `n`, `[T; n]` has a size of `n * size_of::<T>()`.

In general, the size of a type is not stable across compilations, but specific types such as primitives are.

The following table gives the size for primitives.

Type`size_of::<Type>()` ()0 bool1 u81 u162 u324 u648 u12816 i81 i162 i324 i648 i12816 f324 f648 char4

Furthermore, `usize` and `isize` have the same size.

The types [`*const T`](https://doc.rust-lang.org/stable/std/primitive.pointer.html "primitive pointer"), `&T`, [`Box<T>`](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html), [`Option<&T>`](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option"), and `Option<Box<T>>` all have the same size. If `T` is `Sized`, all of those types have the same size as `usize`.

The mutability of a pointer does not change its size. As such, `&T` and `&mut T` have the same size. Likewise for `*const T` and `*mut T`.

## [§](#size-of-reprc-items)Size of `#[repr(C)]` items

The `C` representation for items has a defined layout. With this layout, the size of items is also stable as long as all fields have a stable size.

### [§](#size-of-structs)Size of Structs

For `struct`s, the size is determined by the following algorithm.

For each field in the struct ordered by declaration order:

1. Add the size of the field.
2. Round up the current size to the nearest multiple of the next field’s [alignment](https://doc.rust-lang.org/stable/std/mem/fn.align_of.html "fn std::mem::align_of").

Finally, round the size of the struct to the nearest multiple of its [alignment](https://doc.rust-lang.org/stable/std/mem/fn.align_of.html "fn std::mem::align_of"). The alignment of the struct is usually the largest alignment of all its fields; this can be changed with the use of `repr(align(N))`.

Unlike `C`, zero sized structs are not rounded up to one byte in size.

### [§](#size-of-enums)Size of Enums

Enums that carry no data other than the discriminant have the same size as C enums on the platform they are compiled for.

### [§](#size-of-unions)Size of Unions

The size of a union is the size of its largest field.

Unlike `C`, zero sized unions are not rounded up to one byte in size.

## [§](#examples)Examples

```rust
// Some primitives
assert_eq!(4, size_of::<i32>());
assert_eq!(8, size_of::<f64>());
assert_eq!(0, size_of::<()>());

// Some arrays
assert_eq!(8, size_of::<[i32; 2]>());
assert_eq!(12, size_of::<[i32; 3]>());
assert_eq!(0, size_of::<[i32; 0]>());


// Pointer size equality
assert_eq!(size_of::<&i32>(), size_of::<*const i32>());
assert_eq!(size_of::<&i32>(), size_of::<Box<i32>>());
assert_eq!(size_of::<&i32>(), size_of::<Option<&i32>>());
assert_eq!(size_of::<Box<i32>>(), size_of::<Option<Box<i32>>>());
```

Using `#[repr(C)]`.

```rust
#[repr(C)]
struct FieldStruct {
    first: u8,
    second: u16,
    third: u8
}

// The size of the first field is 1, so add 1 to the size. Size is 1.
// The alignment of the second field is 2, so add 1 to the size for padding. Size is 2.
// The size of the second field is 2, so add 2 to the size. Size is 4.
// The alignment of the third field is 1, so add 0 to the size for padding. Size is 4.
// The size of the third field is 1, so add 1 to the size. Size is 5.
// Finally, the alignment of the struct is 2 (because the largest alignment amongst its
// fields is 2), so add 1 to the size for padding. Size is 6.
assert_eq!(6, size_of::<FieldStruct>());

#[repr(C)]
struct TupleStruct(u8, u16, u8);

// Tuple structs follow the same rules.
assert_eq!(6, size_of::<TupleStruct>());

// Note that reordering the fields can lower the size. We can remove both padding bytes
// by putting `third` before `second`.
#[repr(C)]
struct FieldStructOptimized {
    first: u8,
    third: u8,
    second: u16
}

assert_eq!(4, size_of::<FieldStructOptimized>());

// Union size is the size of the largest field.
#[repr(C)]
union ExampleUnion {
    smaller: u8,
    larger: u16
}

assert_eq!(2, size_of::<ExampleUnion>());
```