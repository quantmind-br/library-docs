---
title: Cell in std::cell - Rust
url: https://doc.rust-lang.org/stable/std/cell/struct.Cell.html
source: crawler
fetched_at: 2026-05-06T21:28:10.774648482-03:00
rendered_js: false
word_count: 686
summary: This document describes the Cell<T> struct in Rust, which provides a mechanism for interior mutability by allowing modification of data even when the container is immutable.
tags:
    - rust
    - memory-management
    - interior-mutability
    - concurrency
    - standard-library
category: reference
---

## Struct Cell

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#312)

```rust
pub struct Cell<T>
where
    T: ?Sized,{ /* private fields */ }
```

Expand description

A mutable memory location.

## [§](#memory-layout)Memory layout

`Cell<T>` has the same [memory layout and caveats as `UnsafeCell<T>`](https://doc.rust-lang.org/stable/std/cell/struct.UnsafeCell.html#memory-layout "struct std::cell::UnsafeCell"). In particular, this means that `Cell<T>` has the same in-memory representation as its inner type `T`.

## [§](#examples)Examples

In this example, you can see that `Cell<T>` enables mutation inside an immutable struct. In other words, it enables “interior mutability”.

```rust
use std::cell::Cell;

struct SomeStruct {
    regular_field: u8,
    special_field: Cell<u8>,
}

let my_struct = SomeStruct {
    regular_field: 0,
    special_field: Cell::new(1),
};

let new_value = 100;

// ERROR: `my_struct` is immutable
// my_struct.regular_field = new_value;

// WORKS: although `my_struct` is immutable, `special_field` is a `Cell`,
// which can always be mutated
my_struct.special_field.set(new_value);
assert_eq!(my_struct.special_field.get(), new_value);
```

See the [module-level documentation](https://doc.rust-lang.org/stable/std/cell/index.html "mod std::cell") for more.

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#401)[§](#impl-Cell%3CT%3E)

1.0.0 (const: 1.24.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#414)

Creates a new `Cell` containing the given value.

##### [§](#examples-1)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/147787 "Tracking issue for const_cell_traits")) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#433-435)

Sets the contained value.

##### [§](#examples-2)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);

c.set(10);
```

1.17.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#465)

Swaps the values of two `Cell`s.

The difference with `std::mem::swap` is that this function doesn’t require a `&mut` reference.

##### [§](#panics)Panics

This function will panic if `self` and `other` are different `Cell`s that partially overlap. (Using just standard library methods, it is impossible to create such partially overlapping `Cell`s. However, unsafe code is allowed to e.g. create two `&Cell<[i32; 2]>` that partially overlap.)

##### [§](#examples-3)Examples

```rust
use std::cell::Cell;

let c1 = Cell::new(5i32);
let c2 = Cell::new(10i32);
c1.swap(&c2);
assert_eq!(10, c1.get());
assert_eq!(5, c2.get());
```

1.17.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#510)

Replaces the contained value with `val`, and returns the old contained value.

##### [§](#examples-4)Examples

```rust
use std::cell::Cell;

let cell = Cell::new(5);
assert_eq!(cell.get(), 5);
assert_eq!(cell.replace(10), 5);
assert_eq!(cell.get(), 10);
```

1.17.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#531)

Unwraps the value, consuming the cell.

##### [§](#examples-5)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);
let five = c.into_inner();

assert_eq!(five, 5);
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#536)[§](#impl-Cell%3CT%3E-1)

1.0.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#552)

Returns a copy of the contained value.

##### [§](#examples-6)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);

let five = c.get();
```

1.88.0 (const: [unstable](https://github.com/rust-lang/rust/issues/147787 "Tracking issue for const_cell_traits")) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#573-576)

Updates the contained value using a function.

##### [§](#examples-7)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);
c.update(|x| x + 1);
assert_eq!(c.get(), 6);
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#583)[§](#impl-Cell%3CT%3E-2)

1.12.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#600)

Returns a raw pointer to the underlying data in this cell.

##### [§](#examples-8)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);

let ptr = c.as_ptr();
```

1.11.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#629)

Returns a mutable reference to the underlying data.

This call borrows `Cell` mutably (at compile-time) which guarantees that we possess the only reference.

However be cautious: this method expects `self` to be mutable, which is generally not the case when using a `Cell`. If you require interior mutability by reference, consider using `RefCell` which provides run-time checked mutable borrows through its [`borrow_mut`](https://doc.rust-lang.org/stable/std/cell/struct.RefCell.html#method.borrow_mut "method std::cell::RefCell::borrow_mut") method.

##### [§](#examples-9)Examples

```rust
use std::cell::Cell;

let mut c = Cell::new(5);
*c.get_mut() += 1;

assert_eq!(c.get(), 6);
```

1.37.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#649)

Returns a `&Cell<T>` from a `&mut T`

##### [§](#examples-10)Examples

```rust
use std::cell::Cell;

let slice: &mut [i32] = &mut [1, 2, 3];
let cell_slice: &Cell<[i32]> = Cell::from_mut(slice);
let slice_cell: &[Cell<i32>] = cell_slice.as_slice_of_cells();

assert_eq!(slice_cell.len(), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#655)[§](#impl-Cell%3CT%3E-3)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/147787 "Tracking issue for const_cell_traits")) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#671-673)

Takes the value of the cell, leaving `Default::default()` in its place.

##### [§](#examples-11)Examples

```rust
use std::cell::Cell;

let c = Cell::new(5);
let five = c.take();

assert_eq!(five, 5);
assert_eq!(c.into_inner(), 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#716)[§](#impl-Cell%3C%5BT%5D%3E)

1.37.0 (const: 1.88.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#732)

Returns a `&[Cell<T>]` from a `&Cell<[T]>`

##### [§](#examples-12)Examples

```rust
use std::cell::Cell;

let slice: &mut [i32] = &mut [1, 2, 3];
let cell_slice: &Cell<[i32]> = Cell::from_mut(slice);
let slice_cell: &[Cell<i32>] = cell_slice.as_slice_of_cells();

assert_eq!(slice_cell.len(), 3);
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#738)[§](#impl-Cell%3C%5BT;+N%5D%3E)

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#752)

Returns a `&[Cell<T>; N]` from a `&Cell<[T; N]>`

##### [§](#examples-13)Examples

```rust
use std::cell::Cell;

let mut array: [i32; 3] = [1, 2, 3];
let cell_array: &Cell<[i32; 3]> = Cell::from_mut(&mut array);
let array_cell: &[Cell<i32>; 3] = cell_array.as_array_of_cells();
```

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#819)[§](#impl-Cell%3CT%3E-4)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#838)

🔬This is a nightly-only experimental API. (`cell_get_cloned` [#145329](https://github.com/rust-lang/rust/issues/145329))

Get a clone of the `Cell` that contains a copy of the original value.

This allows a cheaply `Clone`-able type like an `Rc` to be stored in a `Cell`, exposing the cheaper `clone()` method.

##### [§](#examples-14)Examples

```rust
#![feature(cell_get_cloned)]

use core::cell::Cell;
use std::rc::Rc;

let rc = Rc::new(1usize);
let c1 = Cell::new(rc);
let c2 = c1.get_cloned();
assert_eq!(*c2.into_inner(), 1);
```

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#709)[§](#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#711)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#701)[§](#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#703)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#693)[§](#impl-AsRef%3C%5BCell%3CT%3E;+N%5D%3E-for-Cell%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#695)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#328)[§](#impl-Clone-for-Cell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#3135)[§](#impl-Debug-for-Cell%3CT%3E)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#337)[§](#impl-Default-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#340)[§](#method.default)

Creates a `Cell<T>`, with the `Default` value for T.

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#394)[§](#impl-From%3CT%3E-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#396)[§](#method.from)

Creates a new `Cell<T>` containing the given value.

1.10.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#385)[§](#impl-Ord-for-Cell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#346)[§](#impl-PartialEq-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#348)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.10.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#357)[§](#impl-PartialOrd-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#359)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#364)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#369)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#374)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#379)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#680)[§](#impl-CoerceUnsized%3CCell%3CU%3E%3E-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#690)[§](#impl-DispatchFromDyn%3CCell%3CU%3E%3E-for-Cell%3CT%3E)

1.2.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#354)[§](#impl-Eq-for-Cell%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#2728)[§](#impl-PinCoerceUnsized-for-Cell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#317)[§](#impl-Send-for-Cell%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#325)[§](#impl-Sync-for-Cell%3CT%3E)