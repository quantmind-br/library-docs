---
title: array - Rust
url: https://doc.rust-lang.org/std/primitive.array.html
source: crawler
fetched_at: 2026-05-06T21:24:34.838261213-03:00
rendered_js: false
word_count: 3900
summary: This document provides a technical overview of fixed-size arrays in Rust, covering their construction, trait implementations, slice coercion, and iteration behavior across different language editions.
tags:
    - rust-programming
    - primitive-types
    - data-structures
    - memory-safety
    - arrays
    - language-features
category: reference
---

## Primitive Type array

1.0.0

Expand description

A fixed-size array, denoted `[T; N]`, for the element type, `T`, and the non-negative compile-time constant size, `N`.

There are two syntactic forms for creating an array:

- A list with each element, i.e., `[x, y, z]`.
- A repeat expression `[expr; N]` where `N` is how many times to repeat `expr` in the array. `expr` must either be:
  
  - A value of a type implementing the [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html "trait std::marker::Copy") trait
  - A `const` value

Note that `[expr; 0]` is allowed, and produces an empty array. This will still evaluate `expr`, however, and immediately drop the resulting value, so be mindful of side effects.

Arrays of *any* size implement the following traits if the element type allows it:

- [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html "trait std::marker::Copy")
- [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone")
- [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug")
- [`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html "trait std::iter::IntoIterator") (implemented for `[T; N]`, `&[T; N]` and `&mut [T; N]`)
- [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"), [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd"), [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq"), [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord")
- [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash")
- [`AsRef`](https://doc.rust-lang.org/std/convert/trait.AsRef.html "trait std::convert::AsRef"), [`AsMut`](https://doc.rust-lang.org/std/convert/trait.AsMut.html "trait std::convert::AsMut")
- [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow"), [`BorrowMut`](https://doc.rust-lang.org/std/borrow/trait.BorrowMut.html "trait std::borrow::BorrowMut")

Arrays of sizes from 0 to 32 (inclusive) implement the [`Default`](https://doc.rust-lang.org/std/default/trait.Default.html "trait std::default::Default") trait if the element type allows it. As a stopgap, trait implementations are statically generated up to size 32.

Arrays of sizes from 1 to 12 (inclusive) implement [`From<Tuple>`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From"), where `Tuple` is a homogeneous [tuple](https://doc.rust-lang.org/std/primitive.tuple.html "primitive tuple") of appropriate length.

Arrays coerce to [slices (`[T]`)](https://doc.rust-lang.org/std/primitive.slice.html "primitive slice"), so a slice method may be called on an array. Indeed, this provides most of the API for working with arrays.

Slices have a dynamic size and do not coerce to arrays. Instead, use `slice.try_into().unwrap()` or `<ArrayType>::try_from(slice).unwrap()`.

Array’s `try_from(slice)` implementations (and the corresponding `slice.try_into()` array implementations) succeed if the input slice length is the same as the result array length. They optimize especially well when the optimizer can easily determine the slice length, e.g. `<[u8; 4]>::try_from(&slice[4..8]).unwrap()`. Array implements [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") returning:

- `[T; N]` copies from the slice’s elements
- `&[T; N]` references the original slice’s elements
- `&mut [T; N]` references the original slice’s elements

You can move elements out of an array with a [slice pattern](https://doc.rust-lang.org/reference/patterns.html#slice-patterns). If you want one element, see [`mem::replace`](https://doc.rust-lang.org/std/mem/fn.replace.html "fn std::mem::replace").

## [§](#examples)Examples

```rust
let mut array: [i32; 3] = [0; 3];

array[1] = 1;
array[2] = 2;

assert_eq!([1, 2], &array[1..]);

// This loop prints: 0 1 2
for x in array {
    print!("{x} ");
}
```

You can also iterate over reference to the array’s elements:

```rust
let array: [i32; 3] = [0; 3];

for x in &array { }
```

You can use `<ArrayType>::try_from(slice)` or `slice.try_into()` to get an array from a slice:

```rust
let bytes: [u8; 3] = [1, 0, 2];
assert_eq!(1, u16::from_le_bytes(<[u8; 2]>::try_from(&bytes[0..2]).unwrap()));
assert_eq!(512, u16::from_le_bytes(bytes[1..3].try_into().unwrap()));
```

You can use a [slice pattern](https://doc.rust-lang.org/reference/patterns.html#slice-patterns) to move elements out of an array:

```rust
fn move_away(_: String) { /* Do interesting things. */ }

let [john, roa] = ["John".to_string(), "Roa".to_string()];
move_away(john);
move_away(roa);
```

Arrays can be created from homogeneous tuples of appropriate length:

```rust
let tuple: (u32, u32, u32) = (1, 2, 3);
let array: [u32; 3] = tuple.into();
```

## [§](#editions)Editions

Prior to Rust 1.53, arrays did not implement [`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html "trait std::iter::IntoIterator") by value, so the method call `array.into_iter()` auto-referenced into a [slice iterator](https://doc.rust-lang.org/std/primitive.slice.html#method.iter "method slice::iter"). Right now, the old behavior is preserved in the 2015 and 2018 editions of Rust for compatibility, ignoring [`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html "trait std::iter::IntoIterator") by value. In the future, the behavior on the 2015 and 2018 edition might be made consistent to the behavior of later editions.

[ⓘ](# "This example runs with edition 2018")

```rust
// Rust 2015 and 2018:

let array: [i32; 3] = [0; 3];

// This creates a slice iterator, producing references to each value.
for item in array.into_iter().enumerate() {
    let (i, x): (usize, &i32) = item;
    println!("array[{i}] = {x}");
}

// The `array_into_iter` lint suggests this change for future compatibility:
for item in array.iter().enumerate() {
    let (i, x): (usize, &i32) = item;
    println!("array[{i}] = {x}");
}

// You can explicitly iterate an array by value using `IntoIterator::into_iter`
for item in IntoIterator::into_iter(array).enumerate() {
    let (i, x): (usize, i32) = item;
    println!("array[{i}] = {x}");
}
```

Starting in the 2021 edition, `array.into_iter()` uses `IntoIterator` normally to iterate by value, and `iter()` should be used to iterate by reference like previous editions.

[ⓘ](# "This example runs with edition 2021")

```rust
// Rust 2021:

let array: [i32; 3] = [0; 3];

// This iterates by reference:
for item in array.iter().enumerate() {
    let (i, x): (usize, &i32) = item;
    println!("array[{i}] = {x}");
}

// This iterates by value:
for item in array.into_iter().enumerate() {
    let (i, x): (usize, i32) = item;
    println!("array[{i}] = {x}");
}
```

Future language versions might start treating the `array.into_iter()` syntax on editions 2015 and 2018 the same as on edition 2021. So code using those older editions should still be written with this change in mind, to prevent breakage in the future. The safest way to accomplish this is to avoid the `into_iter` syntax on those editions. If an edition update is not viable/desired, there are multiple alternatives:

- use `iter`, equivalent to the old behavior, creating references
- use [`IntoIterator::into_iter`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter "method std::iter::IntoIterator::into_iter"), equivalent to the post-2021 behavior (Rust 1.53+)
- replace `for ... in array.into_iter() {` with `for ... in array {`, equivalent to the post-2021 behavior (Rust 1.53+)

[ⓘ](# "This example runs with edition 2018")

```rust
// Rust 2015 and 2018:

let array: [i32; 3] = [0; 3];

// This iterates by reference:
for item in array.iter() {
    let x: &i32 = item;
    println!("{x}");
}

// This iterates by value:
for item in IntoIterator::into_iter(array) {
    let x: i32 = item;
    println!("{x}");
}

// This iterates by value:
for item in array {
    let x: i32 = item;
    println!("{x}");
}

// IntoIter can also start a chain.
// This iterates by value:
for item in IntoIterator::into_iter(array).enumerate() {
    let (i, x): (usize, i32) = item;
    println!("array[{i}] = {x}");
}
```

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1585)[§](#impl-%5BMaybeUninit%3CT%3E;+N%5D)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1599)

🔬This is a nightly-only experimental API. (`maybe_uninit_uninit_array_transpose` [#96097](https://github.com/rust-lang/rust/issues/96097))

Transposes a `[MaybeUninit<T>; N]` into a `MaybeUninit<[T; N]>`.

##### [§](#examples-1)Examples

```rust
#![feature(maybe_uninit_uninit_array_transpose)]

let data = [MaybeUninit::<u8>::uninit(); 1000];
let data: MaybeUninit<[u8; 1000]> = data.transpose();
```

[Source](https://doc.rust-lang.org/src/core/array/ascii.rs.html#3)[§](#impl-%5Bu8;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/ascii.rs.html#21)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this array of bytes into an array of ASCII characters, or returns `None` if any of the characters is non-ASCII.

##### [§](#examples-2)Examples

```rust
#![feature(ascii_char)]

const HEX_DIGITS: [std::ascii::Char; 16] =
    *b"0123456789abcdef".as_ascii().unwrap();

assert_eq!(HEX_DIGITS[1].as_str(), "1");
assert_eq!(HEX_DIGITS[10].as_str(), "a");
```

[Source](https://doc.rust-lang.org/src/core/array/ascii.rs.html#39)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this array of bytes into an array of ASCII characters, without checking whether they’re valid.

##### [§](#safety)Safety

Every byte in the array must be in `0..=127`, or else this is UB.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#509)[§](#impl-%5BT;+N%5D)

1.55.0 (const: [unstable](https://github.com/rust-lang/rust/issues/147606 "Tracking issue for const_array")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#581-585)

Returns an array of the same size as `self`, with function `f` applied to each element in order.

If you don’t necessarily need a new fixed-size array, consider using [`Iterator::map`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map "method std::iter::Iterator::map") instead.

##### [§](#note-on-performance-and-stack-usage)Note on performance and stack usage

Note that this method is *eager*. It evaluates `f` all `N` times before returning the new array.

That means that `arr.map(f).map(g)` is, in general, *not* equivalent to `array.map(|x| g(f(x)))`, as the former calls `f` 4 times then `g` 4 times, whereas the latter interleaves the calls (`fgfgfgfg`).

A consequence of this is that it can have fairly-high stack usage, especially in debug mode or for long arrays. The backend may be able to optimize it away, but especially for complicated mappings it might not be able to.

If you’re doing a one-step `map` and really want an array as the result, then absolutely use this method. Its implementation uses a bunch of tricks to help the optimizer handle it well. Particularly for simple arrays, like `[u8; 3]` or `[f32; 4]`, there’s nothing to be concerned about.

However, if you don’t actually need an *array* of the results specifically, just to process them, then you likely want [`Iterator::map`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map "method std::iter::Iterator::map") instead.

For example, rather than doing an array-to-array map of all the elements in the array up-front and only iterating after that completes,

```rust
for x in my_array.map(f) {
    // ...
}
```

It’s often better to use an iterator along the lines of

```rust
for x in my_array.into_iter().map(f) {
    // ...
}
```

as that’s more likely to avoid large temporaries.

##### [§](#examples-3)Examples

```rust
let x = [1, 2, 3];
let y = x.map(|v| v + 1);
assert_eq!(y, [2, 3, 4]);

let x = [1, 2, 3];
let mut temp = 0;
let y = x.map(|v| { temp += 1; v * temp });
assert_eq!(y, [1, 4, 9]);

let x = ["Ferris", "Bueller's", "Day", "Off"];
let y = x.map(|v| v.len());
assert_eq!(y, [6, 9, 3, 3]);
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#622-628)

🔬This is a nightly-only experimental API. (`array_try_map` [#79711](https://github.com/rust-lang/rust/issues/79711))

A fallible function `f` applied to each element on array `self` in order to return an array the same size as `self` or the first error encountered.

The return type of this function depends on the return type of the closure. If you return `Result<T, E>` from the closure, you’ll get a `Result<[T; N], E>`. If you return `Option<T>` from the closure, you’ll get an `Option<[T; N]>`.

##### [§](#examples-4)Examples

```rust
#![feature(array_try_map)]

let a = ["1", "2", "3"];
let b = a.try_map(|v| v.parse::<u32>()).unwrap().map(|v| v + 1);
assert_eq!(b, [2, 3, 4]);

let a = ["1", "2a", "3"];
let b = a.try_map(|v| v.parse::<u32>());
assert!(b.is_err());

use std::num::NonZero;

let z = [1, 2, 0, 3, 4];
assert_eq!(z.try_map(NonZero::new), None);

let a = [1, 2, 3];
let b = a.try_map(NonZero::new);
let c = b.map(|x| x.map(NonZero::get));
assert_eq!(c, Some(a));
```

1.57.0 (const: 1.57.0) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#639)

Returns a slice containing the entire array. Equivalent to `&s[..]`.

1.57.0 (const: 1.89.0) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#647)

Returns a mutable slice containing the entire array. Equivalent to `&mut s[..]`.

1.77.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#677)

Borrows each element and returns an array of references with the same size as `self`.

##### [§](#example)Example

```rust
let floats = [3.1, 2.7, -1.0];
let float_refs: [&f64; 3] = floats.each_ref();
assert_eq!(float_refs, [&3.1, &2.7, &-1.0]);
```

This method is particularly useful if combined with other methods, like [`map`](#method.map). This way, you can avoid moving the original array if its elements are not [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html "trait std::marker::Copy").

```rust
let strings = ["Ferris".to_string(), "♥".to_string(), "Rust".to_string()];
let is_ascii = strings.each_ref().map(|s| s.is_ascii());
assert_eq!(is_ascii, [true, false, true]);

// We can still access the original array: it has not been moved.
assert_eq!(strings.len(), 3);
```

1.77.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#708)

Borrows each element mutably and returns an array of mutable references with the same size as `self`.

##### [§](#example-1)Example

```rust

let mut floats = [3.1, 2.7, -1.0];
let float_refs: [&mut f64; 3] = floats.each_mut();
*float_refs[0] = 0.0;
assert_eq!(float_refs, [&mut 0.0, &mut 2.7, &mut -1.0]);
assert_eq!(floats, [0.0, 2.7, -1.0]);
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#764)

🔬This is a nightly-only experimental API. (`split_array` [#90091](https://github.com/rust-lang/rust/issues/90091))

Divides one array reference into two at an index.

The first will contain all indices from `[0, M)` (excluding the index `M` itself) and the second will contain all indices from `[M, N)` (excluding the index `N` itself).

##### [§](#panics)Panics

Panics if `M > N`.

##### [§](#examples-5)Examples

```rust
#![feature(split_array)]

let v = [1, 2, 3, 4, 5, 6];

{
   let (left, right) = v.split_array_ref::<0>();
   assert_eq!(left, &[]);
   assert_eq!(right, &[1, 2, 3, 4, 5, 6]);
}

{
    let (left, right) = v.split_array_ref::<2>();
    assert_eq!(left, &[1, 2]);
    assert_eq!(right, &[3, 4, 5, 6]);
}

{
    let (left, right) = v.split_array_ref::<6>();
    assert_eq!(left, &[1, 2, 3, 4, 5, 6]);
    assert_eq!(right, &[]);
}
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#797)

🔬This is a nightly-only experimental API. (`split_array` [#90091](https://github.com/rust-lang/rust/issues/90091))

Divides one mutable array reference into two at an index.

The first will contain all indices from `[0, M)` (excluding the index `M` itself) and the second will contain all indices from `[M, N)` (excluding the index `N` itself).

##### [§](#panics-1)Panics

Panics if `M > N`.

##### [§](#examples-6)Examples

```rust
#![feature(split_array)]

let mut v = [1, 0, 3, 0, 5, 6];
let (left, right) = v.split_array_mut::<2>();
assert_eq!(left, &mut [1, 0][..]);
assert_eq!(right, &mut [3, 0, 5, 6]);
left[1] = 2;
right[1] = 4;
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#842)

🔬This is a nightly-only experimental API. (`split_array` [#90091](https://github.com/rust-lang/rust/issues/90091))

Divides one array reference into two at an index from the end.

The first will contain all indices from `[0, N - M)` (excluding the index `N - M` itself) and the second will contain all indices from `[N - M, N)` (excluding the index `N` itself).

##### [§](#panics-2)Panics

Panics if `M > N`.

##### [§](#examples-7)Examples

```rust
#![feature(split_array)]

let v = [1, 2, 3, 4, 5, 6];

{
   let (left, right) = v.rsplit_array_ref::<0>();
   assert_eq!(left, &[1, 2, 3, 4, 5, 6]);
   assert_eq!(right, &[]);
}

{
    let (left, right) = v.rsplit_array_ref::<2>();
    assert_eq!(left, &[1, 2, 3, 4]);
    assert_eq!(right, &[5, 6]);
}

{
    let (left, right) = v.rsplit_array_ref::<6>();
    assert_eq!(left, &[]);
    assert_eq!(right, &[1, 2, 3, 4, 5, 6]);
}
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#875)

🔬This is a nightly-only experimental API. (`split_array` [#90091](https://github.com/rust-lang/rust/issues/90091))

Divides one mutable array reference into two at an index from the end.

The first will contain all indices from `[0, N - M)` (excluding the index `N - M` itself) and the second will contain all indices from `[N - M, N)` (excluding the index `N` itself).

##### [§](#panics-3)Panics

Panics if `M > N`.

##### [§](#examples-8)Examples

```rust
#![feature(split_array)]

let mut v = [1, 0, 3, 0, 5, 6];
let (left, right) = v.rsplit_array_mut::<4>();
assert_eq!(left, &mut [1, 0]);
assert_eq!(right, &mut [3, 0, 5, 6][..]);
left[1] = 2;
right[1] = 4;
assert_eq!(v, [1, 2, 3, 4, 5, 6]);
```

[Source](https://doc.rust-lang.org/src/core/option.rs.html#2929)[§](#impl-%5BOption%3CT%3E;+N%5D)

[Source](https://doc.rust-lang.org/src/core/option.rs.html#2948)

🔬This is a nightly-only experimental API. (`option_array_transpose` [#130828](https://github.com/rust-lang/rust/issues/130828))

Transposes a `[Option<T>; N]` into a `Option<[T; N]>`.

##### [§](#examples-9)Examples

```rust
#![feature(option_array_transpose)]

let data = [Some(0); 1000];
let data: Option<[u8; 1000]> = data.transpose();
assert_eq!(data, Some([0; 1000]));

let data = [Some(0), None];
let data: Option<[u8; 2]> = data.transpose();
assert_eq!(data, None);
```

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1561)[§](#impl-AsMut%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1563)[§](#method.as_mut)

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#214)[§](#impl-AsMut%3C%5BT%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#216)[§](#method.as_mut-1)

Converts this type into a mutable reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#986-988)[§](#impl-AsMut%3C%5BT;+N%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#991)[§](#method.as_mut-2)

Converts this type into a mutable reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#693)[§](#impl-AsRef%3C%5BCell%3CT%3E;+N%5D%3E-for-Cell%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#695)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1544)[§](#impl-AsRef%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1546)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#205)[§](#impl-AsRef%3C%5BT%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#207)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#976-978)[§](#impl-AsRef%3C%5BT;+N%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#981)[§](#method.as_ref-3)

Converts this type into a shared reference of the (usually inferred) input type.

1.4.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#223)[§](#impl-Borrow%3C%5BT%5D%3E-for-%5BT;+N%5D)

1.4.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#231)[§](#impl-BorrowMut%3C%5BT%5D%3E-for-%5BT;+N%5D)

1.58.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#444)[§](#impl-Clone-for-%5BT;+N%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#354)[§](#impl-Debug-for-%5BT;+N%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+32%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2332%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2333%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2334%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2335%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2336%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2337%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2338%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2339%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2340%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2341%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2342%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2343%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2344%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2345%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2346%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2347%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2348%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2349%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2350%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2351%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2352%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2353%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2354%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2355%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2356%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2357%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2358%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2359%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2360%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2361%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2362%7D::%7Bconstant%230%7D%5D)

1.4.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#507)[§](#impl-Default-for-%5BT;+core::::array::%7Bimpl%2363%7D::%7Bconstant%230%7D%5D)

1.77.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#18)[§](#impl-From%3C%26%5BT;+N%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#25)[§](#method.from-22)

Creates a [`Borrowed`](https://doc.rust-lang.org/std/borrow/enum.Cow.html#variant.Borrowed "variant std::borrow::Cow::Borrowed") variant of [`Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow") from a reference to an array.

This conversion does not allocate or clone the data.

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4308)[§](#impl-From%3C%26%5BT;+N%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4316)[§](#method.from-23)

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### [§](#examples-20)Examples

```rust
assert_eq!(Vec::from(&[1, 2, 3]), vec![1, 2, 3]);
```

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4323)[§](#impl-From%3C%26mut+%5BT;+N%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4331)[§](#method.from-24)

Allocates a `Vec<T>` and fills it by cloning `s`’s items.

##### [§](#examples-21)Examples

```rust
assert_eq!(Vec::from(&mut [1, 2, 3]), vec![1, 2, 3]);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/map.rs.html#2653)[§](#impl-From%3C%5B%28K,+V%29;+N%5D%3E-for-BTreeMap%3CK,+V%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/map.rs.html#2666)[§](#method.from-16)

Converts a `[(K, V); N]` into a `BTreeMap<K, V>`.

If any entries in the array have equal keys, all but one of the corresponding values will be dropped.

```rust
use std::collections::BTreeMap;

let map1 = BTreeMap::from([(1, 2), (3, 4)]);
let map2: BTreeMap<_, _> = [(1, 2), (3, 4)].into();
assert_eq!(map1, map2);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/map.rs.html#1493-1514)[§](#impl-From%3C%5B%28K,+V%29;+N%5D%3E-for-HashMap%3CK,+V%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/map.rs.html#1511-1513)[§](#method.from-26)

Converts a `[(K, V); N]` into a `HashMap<K, V>`.

If any entries in the array have equal keys, all but one of the corresponding values will be dropped.

##### [§](#examples-25)Examples

```rust
use std::collections::HashMap;

let map1 = HashMap::from([(1, 2), (3, 4)]);
let map2: HashMap<_, _> = [(1, 2), (3, 4)].into();
assert_eq!(map1, map2);
```

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1536)[§](#impl-From%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1538)[§](#method.from)

Converts to this type from the input type.

1.71.0 · [Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#impl-From%3C%5BT;+1%5D%3E-for-%28T,%29)

This trait is implemented for tuples up to twelve items long.

[Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#method.from-8)

Converts to this type from the input type.

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3870)[§](#impl-From%3C%5BT;+N%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3884)[§](#method.from-21)

Converts a [`[T; N]`](https://doc.rust-lang.org/std/primitive.array.html "primitive array") into an `Arc<[T]>`.

The conversion moves the array into a newly allocated `Arc`.

##### [§](#example-3)Example

```rust
let original: [i32; 3] = [1, 2, 3];
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1491)[§](#impl-From%3C%5BT;+N%5D%3E-for-BTreeSet%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1506)[§](#method.from-17)

Converts a `[T; N]` into a `BTreeSet<T>`.

If the array contains any equal values, all but one will be dropped.

##### [§](#examples-19)Examples

```rust
use std::collections::BTreeSet;

let set1 = BTreeSet::from([1, 2, 3, 4]);
let set2: BTreeSet<_> = [1, 2, 3, 4].into();
assert_eq!(set1, set2);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#1933)[§](#impl-From%3C%5BT;+N%5D%3E-for-BinaryHeap%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#1943)[§](#method.from-15)

```rust
use std::collections::BinaryHeap;

let mut h1 = BinaryHeap::from([1, 4, 2, 3]);
let mut h2: BinaryHeap<_> = [1, 4, 2, 3].into();
while let Some((a, b)) = h1.pop().zip(h2.pop()) {
    assert_eq!(a, b);
}
```

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#226)[§](#impl-From%3C%5BT;+N%5D%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#237)[§](#method.from-14)

Converts a `[T; N]` into a `Box<[T]>`

This conversion moves the array to newly heap-allocated memory.

##### [§](#examples-18)Examples

```rust
let boxed: Box<[u8]> = Box::from([4, 2]);
println!("{boxed:?}");
```

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1169-1190)[§](#impl-From%3C%5BT;+N%5D%3E-for-HashSet%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1187-1189)[§](#method.from-27)

Converts a `[T; N]` into a `HashSet<T>`.

If the array contains any equal values, all but one will be dropped.

##### [§](#examples-26)Examples

```rust
use std::collections::HashSet;

let set1 = HashSet::from([1, 2, 3, 4]);
let set2: HashSet<_> = [1, 2, 3, 4].into();
assert_eq!(set1, set2);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2198)[§](#impl-From%3C%5BT;+N%5D%3E-for-LinkedList%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2208)[§](#method.from-18)

Converts a `[T; N]` into a `LinkedList<T>`.

```rust
use std::collections::LinkedList;

let list1 = LinkedList::from([1, 2, 3, 4]);
let list2: LinkedList<_> = [1, 2, 3, 4].into();
assert_eq!(list1, list2);
```

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2836)[§](#impl-From%3C%5BT;+N%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2850)[§](#method.from-20)

Converts a [`[T; N]`](https://doc.rust-lang.org/std/primitive.array.html "primitive array") into an `Rc<[T]>`.

The conversion moves the array into a newly allocated `Rc`.

##### [§](#example-2)Example

```rust
let original: [i32; 3] = [1, 2, 3];
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1018-1020)[§](#impl-From%3C%5BT;+N%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1023)[§](#method.from-12)

Converts to this type from the input type.

1.44.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4338)[§](#impl-From%3C%5BT;+N%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4346)[§](#method.from-25)

Allocates a `Vec<T>` and moves `s`’s items into it.

##### [§](#examples-22)Examples

```rust
assert_eq!(Vec::from([1, 2, 3]), vec![1, 2, 3]);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3802)[§](#impl-From%3C%5BT;+N%5D%3E-for-VecDeque%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3812)[§](#method.from-19)

Converts a `[T; N]` into a `VecDeque<T>`.

```rust
use std::collections::VecDeque;

let deq1 = VecDeque::from([1, 2, 3, 4]);
let deq2: VecDeque<_> = [1, 2, 3, 4].into();
assert_eq!(deq1, deq2);
```

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#411-413)[§](#impl-From%3C%5Bbool;+N%5D%3E-for-Mask%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#416)[§](#method.from-10)

Converts to this type from the input type.

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2323)[§](#impl-From%3C%5Bu16;+8%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2344)[§](#method.from-7)

Creates an `IpAddr::V6` from an eight element 16-bit array.

##### [§](#examples-15)Examples

```rust
use std::net::{IpAddr, Ipv6Addr};

let addr = IpAddr::from([
    0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
    0x209u16, 0x208u16, 0x207u16, 0x206u16,
]);
assert_eq!(
    IpAddr::V6(Ipv6Addr::new(
        0x20d, 0x20c, 0x20b, 0x20a,
        0x209, 0x208, 0x207, 0x206,
    )),
    addr
);
```

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2266)[§](#impl-From%3C%5Bu16;+8%5D%3E-for-Ipv6Addr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2287)[§](#method.from-5)

Creates an `Ipv6Addr` from an eight element 16-bit array.

##### [§](#examples-13)Examples

```rust
use std::net::Ipv6Addr;

let addr = Ipv6Addr::from([
    0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
    0x209u16, 0x208u16, 0x207u16, 0x206u16,
]);
assert_eq!(
    Ipv6Addr::new(
        0x20d, 0x20c, 0x20b, 0x20a,
        0x209, 0x208, 0x207, 0x206,
    ),
    addr
);
```

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2295)[§](#impl-From%3C%5Bu8;+16%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2316)[§](#method.from-6)

Creates an `IpAddr::V6` from a sixteen element byte array.

##### [§](#examples-14)Examples

```rust
use std::net::{IpAddr, Ipv6Addr};

let addr = IpAddr::from([
    0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
    0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
]);
assert_eq!(
    IpAddr::V6(Ipv6Addr::new(
        0x1918, 0x1716, 0x1514, 0x1312,
        0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
    )),
    addr
);
```

1.9.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2238)[§](#impl-From%3C%5Bu8;+16%5D%3E-for-Ipv6Addr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2259)[§](#method.from-4)

Creates an `Ipv6Addr` from a sixteen element byte array.

##### [§](#examples-12)Examples

```rust
use std::net::Ipv6Addr;

let addr = Ipv6Addr::from([
    0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
    0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
]);
assert_eq!(
    Ipv6Addr::new(
        0x1918, 0x1716, 0x1514, 0x1312,
        0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
    ),
    addr
);
```

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1264)[§](#impl-From%3C%5Bu8;+4%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1276)[§](#method.from-3)

Creates an `IpAddr::V4` from a four element byte array.

##### [§](#examples-11)Examples

```rust
use std::net::{IpAddr, Ipv4Addr};

let addr = IpAddr::from([13u8, 12u8, 11u8, 10u8]);
assert_eq!(IpAddr::V4(Ipv4Addr::new(13, 12, 11, 10)), addr);
```

1.9.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1245)[§](#impl-From%3C%5Bu8;+4%5D%3E-for-Ipv4Addr)

[Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1257)[§](#method.from-2)

Creates an `Ipv4Addr` from a four element byte array.

##### [§](#examples-10)Examples

```rust
use std::net::Ipv4Addr;

let addr = Ipv4Addr::from([13u8, 12u8, 11u8, 10u8]);
assert_eq!(Ipv4Addr::new(13, 12, 11, 10), addr);
```

1.71.0 · [Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#impl-From%3C%28T,%29%3E-for-%5BT;+1%5D)

This trait is implemented for tuples up to twelve items long.

[Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#method.from-9)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#421-423)[§](#impl-From%3CMask%3CT,+N%3E%3E-for-%5Bbool;+N%5D)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#426)[§](#method.from-11)

Converts to this type from the input type.

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1578)[§](#impl-From%3CMaybeUninit%3C%5BT;+N%5D%3E%3E-for-%5BMaybeUninit%3CT%3E;+N%5D)

[Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1580)[§](#method.from-1)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1028-1030)[§](#impl-From%3CSimd%3CT,+N%3E%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1033)[§](#method.from-13)

Converts to this type from the input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#347)[§](#impl-Hash-for-%5BT;+N%5D)

The hash of an array is the same as that of the corresponding slice, as required by the `Borrow` implementation.

```rust
use std::hash::BuildHasher;

let b = std::hash::RandomState::new();
let a: [u8; 3] = [0xa8, 0x3c, 0x09];
let s: &[u8] = &[0xa8, 0x3c, 0x09];
assert_eq!(b.hash_one(a), b.hash_one(s));
```

1.50.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#382-384)[§](#impl-Index%3CI%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#386)[§](#associatedtype.Output)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#389)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.50.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#396-398)[§](#impl-IndexMut%3CI%3E-for-%5BT;+N%5D)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#361)[§](#impl-IntoIterator-for-%26%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#362)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#363)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#365)[§](#method.into_iter-1)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#371)[§](#impl-IntoIterator-for-%26mut+%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#372)[§](#associatedtype.Item-2)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#373)[§](#associatedtype.IntoIter-2)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#375)[§](#method.into_iter-2)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.53.0 · [Source](https://doc.rust-lang.org/src/core/array/iter.rs.html#39)[§](#impl-IntoIterator-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/iter.rs.html#54)[§](#method.into_iter)

Creates a consuming iterator, that is, one that moves each value out of the array (from start to end).

The array cannot be used after calling this unless `T` implements `Copy`, so the whole array is copied.

Arrays have special behavior when calling `.into_iter()` prior to the 2021 edition – see the [array](https://doc.rust-lang.org/std/primitive.array.html "primitive array") Editions section for more information.

[Source](https://doc.rust-lang.org/src/core/array/iter.rs.html#40)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/array/iter.rs.html#41)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#433)[§](#impl-Ord-for-%5BT;+N%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#65-67)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#70)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#74)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#36)[§](#impl-PartialEq%3C%26%5BU;+N%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#36)[§](#method.eq-19)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#36)[§](#method.ne-19)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3589)[§](#impl-PartialEq%3C%26%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3589)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#141)[§](#impl-PartialEq%3C%26%5Bu8;+N%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#141)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#535)[§](#impl-PartialEq%3C%26%5Bu8;+N%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#535)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#97-99)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#102)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#106)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3590)[§](#impl-PartialEq%3C%26mut+%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3590)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#21-23)[§](#impl-PartialEq%3C%5BU%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#26)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#33)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#81-83)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%26%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#86)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#90)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#113-115)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%26mut+%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#118)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#122)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#43-45)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%5BT%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#48)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#55)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#5-7)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#10)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#14)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#35)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#35)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/vec/partial_eq.rs.html#35)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3588)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3588)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#139)[§](#impl-PartialEq%3C%5Bu8;+N%5D%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#139)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#533)[§](#impl-PartialEq%3C%5Bu8;+N%5D%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#533)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#141)[§](#impl-PartialEq%3CByteStr%3E-for-%26%5Bu8;+N%5D)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#141)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#139)[§](#impl-PartialEq%3CByteStr%3E-for-%5Bu8;+N%5D)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#139)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#535)[§](#impl-PartialEq%3CByteString%3E-for-%26%5Bu8;+N%5D)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#535)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#533)[§](#impl-PartialEq%3CByteString%3E-for-%5Bu8;+N%5D)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#533)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#408)[§](#impl-PartialOrd-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#410)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#414)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#418)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#422)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#426)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#850)[§](#impl-Pattern-for-%26%5Bchar;+N%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the array.

#### [§](#examples-17)Examples

```rust
assert_eq!("Hello world".find(&['o', 'l']), Some(2));
assert_eq!("Hello world".find(&['h', 'w']), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#associatedtype.Searcher-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.into_searcher-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.is_contained_in-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.is_prefix_of-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.strip_prefix_of-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.is_suffix_of-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#method.strip_suffix_of-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#165)[§](#method.as_utf8_pattern-1)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#828)[§](#impl-Pattern-for-%5Bchar;+N%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the array.

#### [§](#examples-16)Examples

```rust
assert_eq!("Hello world".find(['o', 'l']), Some(2));
assert_eq!("Hello world".find(['h', 'w']), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#165)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

1.51.0 · [Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5667)[§](#impl-SlicePattern-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5668)[§](#associatedtype.Item-3)

🔬This is a nightly-only experimental API. (`slice_pattern` [#56345](https://github.com/rust-lang/rust/issues/56345))

The element type of the slice being matched on.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5671)[§](#method.as_slice-1)

🔬This is a nightly-only experimental API. (`slice_pattern` [#56345](https://github.com/rust-lang/rust/issues/56345))

Currently, the consumers of `SlicePattern` need a slice.

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

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#259)[§](#impl-TryFrom%3CBox%3C%5BT%5D%3E%3E-for-Box%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#271)[§](#method.try_from-4)

Attempts to convert a `Box<[T]>` into a `Box<[T; N]>`.

The conversion occurs in-place and does not require a new memory allocation.

##### [§](#errors)Errors

Returns the old `Box<[T]>` in the `Err` variant if `boxed_slice.len()` does not equal `N`.

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#260)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#282)[§](#impl-TryFrom%3CVec%3CT%3E%3E-for-Box%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#303)[§](#method.try_from-5)

Attempts to convert a `Vec<T>` into a `Box<[T; N]>`.

Like [`Vec::into_boxed_slice`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.into_boxed_slice "method std::vec::Vec::into_boxed_slice"), this is in-place if `vec.capacity() == N`, but will require a reallocation otherwise.

##### [§](#errors-1)Errors

Returns the original `Vec<T>` in the `Err` variant if `boxed_slice.len()` does not equal `N`.

##### [§](#examples-23)Examples

This can be used with [`vec!`](https://doc.rust-lang.org/std/macro.vec.html "macro std::vec") to create an array on the heap:

```rust
let state: Box<[f32; 100]> = vec![1.0; 100].try_into().unwrap();
assert_eq!(state.len(), 100);
```

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#283)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.48.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4437)[§](#impl-TryFrom%3CVec%3CT,+A%3E%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4466)[§](#method.try_from-6)

Gets the entire contents of the `Vec<T>` as an array, if its size exactly matches that of the requested array.

##### [§](#examples-24)Examples

```rust
assert_eq!(vec![1, 2, 3].try_into(), Ok([1, 2, 3]));
assert_eq!(<Vec<i32>>::new().try_into(), Ok([]));
```

If the length doesn’t match, the input comes back in `Err`:

```rust
let r: Result<[i32; 4], _> = (0..10).collect::<Vec<_>>().try_into();
assert_eq!(r, Err(vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
```

If you’re fine with just getting a prefix of the `Vec<T>`, you can call [`.truncate(N)`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.truncate "method std::vec::Vec::truncate") first.

```rust
let mut v = String::from("hello world").into_bytes();
v.sort();
v.truncate(2);
let [a, b]: [_; 2] = v.try_into().unwrap();
assert_eq!(a, b' ');
assert_eq!(b, b'd');
```

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4438)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#804)[§](#impl-CloneFromCell-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-%5BT;+N%5D)

1.58.0 · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#441)[§](#impl-Copy-for-%5BT;+N%5D)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/array/equality.rs.html#133)[§](#impl-Eq-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-%5BT;+N%5D)