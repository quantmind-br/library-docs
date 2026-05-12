---
title: str - Rust
url: https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary
source: crawler
fetched_at: 2026-05-06T21:22:05.840001564-03:00
rendered_js: false
word_count: 11199
summary: This document provides a technical overview of the string slice type (&str) in Rust, detailing its representation, UTF-8 safety invariants, and core methods for conversion and validation.
tags:
    - rust
    - string-slice
    - utf-8
    - memory-safety
    - byte-manipulation
    - primitive-types
category: reference
---

Expand description

String slices.

*[See also the `std::str` module](https://doc.rust-lang.org/std/str/index.html "mod std::str").*

The `str` type, also called a ‘string slice’, is the most primitive string type. It is usually seen in its borrowed form, `&str`. It is also the type of string literals, `&'static str`.

## [§](#basic-usage)Basic Usage

String literals are string slices:

```rust
let hello_world = "Hello, World!";
```

Here we have declared a string slice initialized with a string literal. String literals have a static lifetime, which means the string `hello_world` is guaranteed to be valid for the duration of the entire program. We can explicitly specify `hello_world`’s lifetime as well:

```rust
let hello_world: &'static str = "Hello, world!";
```

## [§](#representation)Representation

A `&str` is made up of two components: a pointer to some bytes, and a length. You can look at these with the [`as_ptr`](https://doc.rust-lang.org/std/primitive.str.html#method.as_ptr "method str::as_ptr") and [`len`](https://doc.rust-lang.org/std/primitive.str.html#method.len "method str::len") methods:

```rust
use std::slice;
use std::str;

let story = "Once upon a time...";

let ptr = story.as_ptr();
let len = story.len();

// story has nineteen bytes
assert_eq!(19, len);

// We can re-build a str out of ptr and len. This is all unsafe because
// we are responsible for making sure the two components are valid:
let s = unsafe {
    // First, we build a &[u8]...
    let slice = slice::from_raw_parts(ptr, len);

    // ... and then convert that slice into a string slice
    str::from_utf8(slice)
};

assert_eq!(s, Ok(story));
```

Note: This example shows the internals of `&str`. `unsafe` should not be used to get a string slice under normal circumstances. Use `as_str` instead.

## [§](#invariant)Invariant

Rust libraries may assume that string slices are always valid UTF-8.

Constructing a non-UTF-8 string slice is not immediate undefined behavior, but any function called on a string slice may assume that it is valid UTF-8, which means that a non-UTF-8 string slice can lead to undefined behavior down the road.

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#134)[§](#impl-str)

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#157)

Returns the length of `self`.

This length is in bytes, not [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s or graphemes. In other words, it might not be what a human considers the length of the string.

##### [§](#examples)Examples

```rust
let len = "foo".len();
assert_eq!(3, len);

assert_eq!("ƒoo".len(), 4); // fancy f!
assert_eq!("ƒoo".chars().count(), 3);
```

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#177)

Returns `true` if `self` has a length of zero bytes.

##### [§](#examples-1)Examples

```rust
let s = "";
assert!(s.is_empty());

let s = "not empty";
assert!(!s.is_empty());
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#255)

Converts a slice of bytes to a string slice.

A string slice ([`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str")) is made of bytes ([`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")), and a byte slice ([`&[u8]`](https://doc.rust-lang.org/std/primitive.slice.html "primitive slice")) is made of bytes, so this function converts between the two. Not all byte slices are valid string slices, however: [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") requires that it is valid UTF-8. `from_utf8()` checks to ensure that the bytes are valid UTF-8, and then does the conversion.

If you are sure that the byte slice is valid UTF-8, and you don’t want to incur the overhead of the validity check, there is an unsafe version of this function, [`from_utf8_unchecked`](https://doc.rust-lang.org/std/str/fn.from_utf8_unchecked.html "fn std::str::from_utf8_unchecked"), which has the same behavior but skips the check.

If you need a `String` instead of a `&str`, consider [`String::from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8).

Because you can stack-allocate a `[u8; N]`, and you can take a [`&[u8]`](https://doc.rust-lang.org/std/primitive.slice.html "primitive slice") of it, this function is one way to have a stack-allocated string. There is an example of this in the examples section below.

##### [§](#errors)Errors

Returns `Err` if the slice is not UTF-8 with a description as to why the provided slice is not UTF-8.

##### [§](#examples-2)Examples

Basic usage:

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

// We can use the ? (try) operator to check if the bytes are valid
let sparkle_heart = str::from_utf8(&sparkle_heart)?;

assert_eq!("💖", sparkle_heart);
```

Incorrect bytes:

```rust
// some invalid bytes, in a vector
let sparkle_heart = vec![0, 159, 146, 150];

assert!(str::from_utf8(&sparkle_heart).is_err());
```

See the docs for [`Utf8Error`](https://doc.rust-lang.org/std/str/struct.Utf8Error.html "struct std::str::Utf8Error") for more details on the kinds of errors that can be returned.

A “stack allocated string”:

```rust
// some bytes, in a stack-allocated array
let sparkle_heart = [240, 159, 146, 150];

// We know these bytes are valid, so just use `unwrap()`.
let sparkle_heart: &str = str::from_utf8(&sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#288)

Converts a mutable slice of bytes to a mutable string slice.

##### [§](#examples-3)Examples

Basic usage:

```rust
// "Hello, Rust!" as a mutable vector
let mut hellorust = vec![72, 101, 108, 108, 111, 44, 32, 82, 117, 115, 116, 33];

// As we know these bytes are valid, we can use `unwrap()`
let outstr = str::from_utf8_mut(&mut hellorust).unwrap();

assert_eq!("Hello, Rust!", outstr);
```

Incorrect bytes:

```rust
// Some invalid bytes in a mutable vector
let mut invalid = vec![128, 223];

assert!(str::from_utf8_mut(&mut invalid).is_err());
```

See the docs for [`Utf8Error`](https://doc.rust-lang.org/std/str/struct.Utf8Error.html "struct std::str::Utf8Error") for more details on the kinds of errors that can be returned.

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#320)

Converts a slice of bytes to a string slice without checking that the string contains valid UTF-8.

See the safe version, [`from_utf8`](https://doc.rust-lang.org/std/str/fn.from_utf8.html "fn std::str::from_utf8"), for more information.

##### [§](#safety)Safety

The bytes passed in must be valid UTF-8.

##### [§](#examples-4)Examples

Basic usage:

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = unsafe {
    str::from_utf8_unchecked(&sparkle_heart)
};

assert_eq!("💖", sparkle_heart);
```

1.87.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#345)

Converts a slice of bytes to a string slice without checking that the string contains valid UTF-8; mutable version.

See the immutable version, [`from_utf8_unchecked()`](https://doc.rust-lang.org/std/str/fn.from_utf8_unchecked.html "fn std::str::from_utf8_unchecked") for documentation and safety requirements.

##### [§](#examples-5)Examples

Basic usage:

```rust
let mut heart = vec![240, 159, 146, 150];
let heart = unsafe { str::from_utf8_unchecked_mut(&mut heart) };

assert_eq!("💖", heart);
```

1.9.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#377)

Checks that `index`-th byte is the first byte in a UTF-8 code point sequence or the end of the string.

The start and end of the string (when `index == self.len()`) are considered to be boundaries.

Returns `false` if `index` is greater than `self.len()`.

##### [§](#examples-6)Examples

```rust
let s = "Löwe 老虎 Léopard";
assert!(s.is_char_boundary(0));
// start of `老`
assert!(s.is_char_boundary(6));
assert!(s.is_char_boundary(s.len()));

// second byte of `ö`
assert!(!s.is_char_boundary(2));

// third byte of `老`
assert!(!s.is_char_boundary(8));
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#426)

Finds the closest `x` not exceeding `index` where [`is_char_boundary(x)`](https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary "method str::is_char_boundary") is `true`.

This method can help you truncate a string so that it’s still valid UTF-8, but doesn’t exceed a given number of bytes. Note that this is done purely at the character level and can still visually split graphemes, even though the underlying characters aren’t split. For example, the emoji 🧑‍🔬 (scientist) could be split so that the string only includes 🧑 (person) instead.

##### [§](#examples-7)Examples

```rust
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.floor_char_boundary(13);
assert_eq!(closest, 10);
assert_eq!(&s[..closest], "❤️🧡");
```

1.91.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#469)

Finds the closest `x` not below `index` where [`is_char_boundary(x)`](https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary "method str::is_char_boundary") is `true`.

If `index` is greater than the length of the string, this returns the length of the string.

This method is the natural complement to [`floor_char_boundary`](https://doc.rust-lang.org/std/primitive.str.html#method.floor_char_boundary "method str::floor_char_boundary"). See that method for more details.

##### [§](#examples-8)Examples

```rust
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.ceil_char_boundary(13);
assert_eq!(closest, 14);
assert_eq!(&s[..closest], "❤️🧡💛");
```

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#502)

Converts a string slice to a byte slice. To convert the byte slice back into a string slice, use the [`from_utf8`](https://doc.rust-lang.org/std/str/fn.from_utf8.html "fn std::str::from_utf8") function.

##### [§](#examples-9)Examples

```rust
let bytes = "bors".as_bytes();
assert_eq!(b"bors", bytes);
```

1.20.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#547)

Converts a mutable string slice to a mutable byte slice.

##### [§](#safety-1)Safety

The caller must ensure that the content of the slice is valid UTF-8 before the borrow ends and the underlying `str` is used.

Use of a `str` whose contents are not valid UTF-8 is undefined behavior.

##### [§](#examples-10)Examples

Basic usage:

```rust
let mut s = String::from("Hello");
let bytes = unsafe { s.as_bytes_mut() };

assert_eq!(b"Hello", bytes);
```

Mutability:

```rust
let mut s = String::from("🗻∈🌏");

unsafe {
    let bytes = s.as_bytes_mut();

    bytes[0] = 0xF0;
    bytes[1] = 0x9F;
    bytes[2] = 0x8D;
    bytes[3] = 0x94;
}

assert_eq!("🍔∈🌏", s);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#578)

Converts a string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8"). This pointer will be pointing to the first byte of the string slice.

The caller must ensure that the returned pointer is never written to. If you need to mutate the contents of the string slice, use [`as_mut_ptr`](https://doc.rust-lang.org/std/primitive.str.html#method.as_mut_ptr "method str::as_mut_ptr").

##### [§](#examples-11)Examples

```rust
let s = "Hello";
let ptr = s.as_ptr();
```

1.36.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#596)

Converts a mutable string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8"). This pointer will be pointing to the first byte of the string slice.

It is your responsibility to make sure that the string slice only gets modified in a way that it remains valid UTF-8.

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#622)

Returns a subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") whenever equivalent indexing operation would panic.

##### [§](#examples-12)Examples

```rust
let v = String::from("🗻∈🌏");

assert_eq!(Some("🗻"), v.get(0..4));

// indices not on UTF-8 sequence boundaries
assert!(v.get(1..).is_none());
assert!(v.get(..8).is_none());

// out of bounds
assert!(v.get(..42).is_none());
```

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#655)

Returns a mutable subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") whenever equivalent indexing operation would panic.

##### [§](#examples-13)Examples

```rust
let mut v = String::from("hello");
// correct length
assert!(v.get_mut(0..5).is_some());
// out of bounds
assert!(v.get_mut(..42).is_none());
assert_eq!(Some("he"), v.get_mut(0..2).map(|v| &*v));

assert_eq!("hello", v);
{
    let s = v.get_mut(0..2);
    let s = s.map(|s| {
        s.make_ascii_uppercase();
        &*s
    });
    assert_eq!(Some("HE"), s);
}
assert_eq!("HEllo", v);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#687)

Returns an unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### [§](#safety-2)Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### [§](#examples-14)Examples

```rust
let v = "🗻∈🌏";
unsafe {
    assert_eq!("🗻", v.get_unchecked(0..4));
    assert_eq!("∈", v.get_unchecked(4..7));
    assert_eq!("🌏", v.get_unchecked(7..11));
}
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#722)

Returns a mutable, unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### [§](#safety-3)Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### [§](#examples-15)Examples

```rust
let mut v = String::from("🗻∈🌏");
unsafe {
    assert_eq!("🗻", v.get_unchecked_mut(0..4));
    assert_eq!("∈", v.get_unchecked_mut(4..7));
    assert_eq!("🌏", v.get_unchecked_mut(7..11));
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#773)

👎Deprecated since 1.29.0: use `get_unchecked(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") and [`Index`](https://doc.rust-lang.org/std/ops/trait.Index.html "trait std::ops::Index").

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get a mutable string slice instead, see the [`slice_mut_unchecked`](https://doc.rust-lang.org/std/primitive.str.html#method.slice_mut_unchecked "method str::slice_mut_unchecked") method.

##### [§](#safety-4)Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

##### [§](#examples-16)Examples

```rust
let s = "Löwe 老虎 Léopard";

unsafe {
    assert_eq!("Löwe 老虎 Léopard", s.slice_unchecked(0, 21));
}

let s = "Hello, world!";

unsafe {
    assert_eq!("world", s.slice_unchecked(7, 12));
}
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#807)

👎Deprecated since 1.29.0: use `get_unchecked_mut(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") and [`IndexMut`](https://doc.rust-lang.org/std/ops/trait.IndexMut.html "trait std::ops::IndexMut").

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get an immutable string slice instead, see the [`slice_unchecked`](https://doc.rust-lang.org/std/primitive.str.html#method.slice_unchecked "method str::slice_unchecked") method.

##### [§](#safety-5)Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

1.4.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#847)

Divides one string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the [`split_at_mut`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut "method str::split_at_mut") method.

##### [§](#panics)Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see [`split_at_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_checked "method str::split_at_checked").

##### [§](#examples-17)Examples

```rust
let s = "Per Martin-Löf";

let (first, last) = s.split_at(3);

assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);
```

1.4.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#888)

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the [`split_at`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at "method str::split_at") method.

##### [§](#panics-1)Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see [`split_at_mut_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut_checked "method str::split_at_mut_checked").

##### [§](#examples-18)Examples

```rust
let mut s = "Per Martin-Löf".to_string();
{
    let (first, last) = s.split_at_mut(3);
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);
```

1.80.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#928)

Divides one string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the [`split_at_mut_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut_checked "method str::split_at_mut_checked") method.

##### [§](#examples-19)Examples

```rust
let s = "Per Martin-Löf";

let (first, last) = s.split_at_checked(3).unwrap();
assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);

assert_eq!(None, s.split_at_checked(13));  // Inside “ö”
assert_eq!(None, s.split_at_checked(16));  // Beyond the string length
```

1.80.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#969)

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the [`split_at_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_checked "method str::split_at_checked") method.

##### [§](#examples-20)Examples

```rust
let mut s = "Per Martin-Löf".to_string();
if let Some((first, last)) = s.split_at_mut_checked(3) {
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);

assert_eq!(None, s.split_at_mut_checked(13));  // Inside “ö”
assert_eq!(None, s.split_at_mut_checked(16));  // Beyond the string length
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1066)

Returns an iterator over the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s of a string slice.

As a string slice consists of valid UTF-8, we can iterate through a string slice by [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"). This method returns such an iterator.

It’s important to remember that [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") represents a Unicode Scalar Value, and might not match your idea of what a ‘character’ is. Iteration over grapheme clusters may be what you actually want. This functionality is not provided by Rust’s standard library, check crates.io instead.

##### [§](#examples-21)Examples

Basic usage:

```rust
let word = "goodbye";

let count = word.chars().count();
assert_eq!(7, count);

let mut chars = word.chars();

assert_eq!(Some('g'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('d'), chars.next());
assert_eq!(Some('b'), chars.next());
assert_eq!(Some('y'), chars.next());
assert_eq!(Some('e'), chars.next());

assert_eq!(None, chars.next());
```

Remember, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s might not match your intuition about characters:

```rust
let y = "y̆";

let mut chars = y.chars();

assert_eq!(Some('y'), chars.next()); // not 'y̆'
assert_eq!(Some('\u{0306}'), chars.next());

assert_eq!(None, chars.next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1123)

Returns an iterator over the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s of a string slice, and their positions.

As a string slice consists of valid UTF-8, we can iterate through a string slice by [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"). This method returns an iterator of both these [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, as well as their byte positions.

The iterator yields tuples. The position is first, the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") is second.

##### [§](#examples-22)Examples

Basic usage:

```rust
let word = "goodbye";

let count = word.char_indices().count();
assert_eq!(7, count);

let mut char_indices = word.char_indices();

assert_eq!(Some((0, 'g')), char_indices.next());
assert_eq!(Some((1, 'o')), char_indices.next());
assert_eq!(Some((2, 'o')), char_indices.next());
assert_eq!(Some((3, 'd')), char_indices.next());
assert_eq!(Some((4, 'b')), char_indices.next());
assert_eq!(Some((5, 'y')), char_indices.next());
assert_eq!(Some((6, 'e')), char_indices.next());

assert_eq!(None, char_indices.next());
```

Remember, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s might not match your intuition about characters:

```rust
let yes = "y̆es";

let mut char_indices = yes.char_indices();

assert_eq!(Some((0, 'y')), char_indices.next()); // not (0, 'y̆')
assert_eq!(Some((1, '\u{0306}')), char_indices.next());

// note the 3 here - the previous character took up two bytes
assert_eq!(Some((3, 'e')), char_indices.next());
assert_eq!(Some((4, 's')), char_indices.next());

assert_eq!(None, char_indices.next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1146)

Returns an iterator over the bytes of a string slice.

As a string slice consists of a sequence of bytes, we can iterate through a string slice by byte. This method returns such an iterator.

##### [§](#examples-23)Examples

```rust
let mut bytes = "bors".bytes();

assert_eq!(Some(b'b'), bytes.next());
assert_eq!(Some(b'o'), bytes.next());
assert_eq!(Some(b'r'), bytes.next());
assert_eq!(Some(b's'), bytes.next());

assert_eq!(None, bytes.next());
```

1.1.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1198)

Splits a string slice by whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of whitespace.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`. If you only want to split on ASCII whitespace instead, use [`split_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_ascii_whitespace "method str::split_ascii_whitespace").

##### [§](#examples-24)Examples

Basic usage:

```rust
let mut iter = "A few words".split_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

All kinds of whitespace are considered:

```rust
let mut iter = " Mary   had\ta\u{2009}little  \n\t lamb".split_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all whitespace, the iterator yields no string slices:

```rust
assert_eq!("".split_whitespace().next(), None);
assert_eq!("   ".split_whitespace().next(), None);
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1249)

Splits a string slice by ASCII whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of ASCII whitespace.

This uses the same definition as [`char::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.char.html#method.is_ascii_whitespace "method char::is_ascii_whitespace"). To split by Unicode `Whitespace` instead, use [`split_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_whitespace "method str::split_whitespace").

##### [§](#examples-25)Examples

Basic usage:

```rust
let mut iter = "A few words".split_ascii_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

Various kinds of ASCII whitespace are considered (see [`char::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.char.html#method.is_ascii_whitespace "method char::is_ascii_whitespace")):

```rust
let mut iter = " Mary   had\ta little  \n\t lamb".split_ascii_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all ASCII whitespace, the iterator yields no string slices:

```rust
assert_eq!("".split_ascii_whitespace().next(), None);
assert_eq!("   ".split_ascii_whitespace().next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1313)

Returns an iterator over the lines of a string, as string slices.

Lines are split at line endings that are either newlines (`\n`) or sequences of a carriage return followed by a line feed (`\r\n`).

Line terminators are not included in the lines returned by the iterator.

Note that any carriage return (`\r`) not immediately followed by a line feed (`\n`) does not split a line. These carriage returns are thereby included in the produced lines.

The final line ending is optional. A string that ends with a final line ending will return the same lines as an otherwise identical string without a final line ending.

An empty string returns an empty iterator.

##### [§](#examples-26)Examples

Basic usage:

```rust
let text = "foo\r\nbar\n\nbaz\r";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
// Trailing carriage return is included in the last line
assert_eq!(Some("baz\r"), lines.next());

assert_eq!(None, lines.next());
```

The final line does not require any ending:

```rust
let text = "foo\nbar\n\r\nbaz";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
assert_eq!(Some("baz"), lines.next());

assert_eq!(None, lines.next());
```

An empty string returns an empty iterator:

```rust
let text = "";
let mut lines = text.lines();

assert_eq!(lines.next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1322)

👎Deprecated since 1.4.0: use lines() instead now

Returns an iterator over the lines of a string.

1.8.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1342)

Returns an iterator of `u16` over the string encoded as native endian UTF-16 (without byte-order mark).

##### [§](#examples-27)Examples

```rust
let text = "Zażółć gęślą jaźń";

let utf8_len = text.len();
let utf16_len = text.encode_utf16().count();

assert!(utf16_len <= utf8_len);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1367)

Returns `true` if the given pattern matches a sub-slice of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-28)Examples

```rust
let bananas = "bananas";

assert!(bananas.contains("nana"));
assert!(!bananas.contains("apples"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1405)

Returns `true` if the given pattern matches a prefix of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, in which case this function will return true if the `&str` is a prefix of this string slice.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can also be a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches. These will only be checked against the first character of this string slice. Look at the second example below regarding behavior for slices of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s.

##### [§](#examples-29)Examples

```rust
let bananas = "bananas";

assert!(bananas.starts_with("bana"));
assert!(!bananas.starts_with("nana"));
```

```rust
let bananas = "bananas";

// Note that both of these assert successfully.
assert!(bananas.starts_with(&['b', 'a', 'n', 'a']));
assert!(bananas.starts_with(&['a', 'b', 'c', 'd']));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1430-1432)

Returns `true` if the given pattern matches a suffix of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-30)Examples

```rust
let bananas = "bananas";

assert!(bananas.ends_with("anas"));
assert!(!bananas.ends_with("nana"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1481)

Returns the byte index of the first character of this string slice that matches the pattern.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the pattern doesn’t match.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-31)Examples

Simple patterns:

```rust
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.find('L'), Some(0));
assert_eq!(s.find('é'), Some(14));
assert_eq!(s.find("pard"), Some(17));
```

More complex patterns using point-free style and closures:

```rust
let s = "Löwe 老虎 Léopard";

assert_eq!(s.find(char::is_whitespace), Some(5));
assert_eq!(s.find(char::is_lowercase), Some(1));
assert_eq!(s.find(|c: char| c.is_whitespace() || c.is_lowercase()), Some(1));
assert_eq!(s.find(|c: char| (c < 'o') && (c > 'a')), Some(4));
```

Not finding the pattern:

```rust
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.find(x), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1527-1529)

Returns the byte index for the first character of the last match of the pattern in this string slice.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the pattern doesn’t match.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-32)Examples

Simple patterns:

```rust
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.rfind('L'), Some(13));
assert_eq!(s.rfind('é'), Some(14));
assert_eq!(s.rfind("pard"), Some(24));
```

More complex patterns with closures:

```rust
let s = "Löwe 老虎 Léopard";

assert_eq!(s.rfind(char::is_whitespace), Some(12));
assert_eq!(s.rfind(char::is_lowercase), Some(20));
```

Not finding the pattern:

```rust
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.rfind(x), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1655)

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

If there are no matches the full string slice is returned as the only item in the iterator.

##### [§](#iterator-behavior)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rsplit`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplit "method str::rsplit") method can be used.

##### [§](#examples-33)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".split(' ').collect();
assert_eq!(v, ["Mary", "had", "a", "little", "lamb"]);

let v: Vec<&str> = "".split('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".split('X').collect();
assert_eq!(v, ["lion", "", "tiger", "leopard"]);

let v: Vec<&str> = "lion::tiger::leopard".split("::").collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);

let v: Vec<&str> = "AABBCC".split("DD").collect();
assert_eq!(v, ["AABBCC"]);

let v: Vec<&str> = "abc1def2ghi".split(char::is_numeric).collect();
assert_eq!(v, ["abc", "def", "ghi"]);

let v: Vec<&str> = "lionXtigerXleopard".split(char::is_uppercase).collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);
```

If the pattern is a slice of chars, split on each occurrence of any of the characters:

```rust
let v: Vec<&str> = "2020-11-03 23:59".split(&['-', ' ', ':', '@'][..]).collect();
assert_eq!(v, ["2020", "11", "03", "23", "59"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".split(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "def", "ghi"]);
```

If a string contains multiple contiguous separators, you will end up with empty strings in the output:

```rust
let x = "||||a||b|c".to_string();
let d: Vec<_> = x.split('|').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

Contiguous separators are separated by the empty string.

```rust
let x = "(///)".to_string();
let d: Vec<_> = x.split('/').collect();

assert_eq!(d, &["(", "", "", ")"]);
```

Separators at the start or end of a string are neighbored by empty strings.

```rust
let d: Vec<_> = "010".split("0").collect();
assert_eq!(d, &["", "1", ""]);
```

When the empty string is used as a separator, it separates every character in the string, along with the beginning and end of the string.

```rust
let f: Vec<_> = "rust".split("").collect();
assert_eq!(f, &["", "r", "u", "s", "t", ""]);
```

Contiguous separators can lead to possibly surprising behavior when whitespace is used as the separator. This code is correct:

```rust
let x = "    a  b c".to_string();
let d: Vec<_> = x.split(' ').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

It does *not* give you:

[ⓘ](# "This example is not tested")

```rust
assert_eq!(d, &["a", "b", "c"]);
```

Use [`split_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_whitespace "method str::split_whitespace") for this behavior.

1.51.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1696)

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

Differs from the iterator produced by `split` in that `split_inclusive` leaves the matched part as the terminator of the substring.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-34)Examples

```rust
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb."
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb."]);
```

If the last element of the string is matched, that element will be considered the terminator of the preceding substring. That substring will be the last item returned by the iterator.

```rust
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb.\n"
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb.\n"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1751-1753)

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern and yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-1)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split") method can be used.

##### [§](#examples-35)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);

let v: Vec<&str> = "".rsplit('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplit('X').collect();
assert_eq!(v, ["leopard", "tiger", "", "lion"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplit("::").collect();
assert_eq!(v, ["leopard", "tiger", "lion"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".rsplit(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "def", "abc"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1800)

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

Equivalent to [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split"), except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### [§](#iterator-behavior-2)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rsplit_terminator`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplit_terminator "method str::rsplit_terminator") method can be used.

##### [§](#examples-36)Examples

```rust
let v: Vec<&str> = "A.B.".split_terminator('.').collect();
assert_eq!(v, ["A", "B"]);

let v: Vec<&str> = "A..B..".split_terminator(".").collect();
assert_eq!(v, ["A", "", "B", ""]);

let v: Vec<&str> = "A.B:C.D".split_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["A", "B", "C", "D"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1846-1848)

Returns an iterator over substrings of `self`, separated by characters matched by a pattern and yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

Equivalent to [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split"), except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### [§](#iterator-behavior-3)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be double ended if a forward/reverse search yields the same elements.

For iterating from the front, the [`split_terminator`](https://doc.rust-lang.org/std/primitive.str.html#method.split_terminator "method str::split_terminator") method can be used.

##### [§](#examples-37)Examples

```rust
let v: Vec<&str> = "A.B.".rsplit_terminator('.').collect();
assert_eq!(v, ["B", "A"]);

let v: Vec<&str> = "A..B..".rsplit_terminator(".").collect();
assert_eq!(v, ["", "B", "", "A"]);

let v: Vec<&str> = "A.B:C.D".rsplit_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["D", "C", "B", "A"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1901)

Returns an iterator over substrings of the given string slice, separated by a pattern, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-4)Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

If the pattern allows a reverse search, the [`rsplitn`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplitn "method str::rsplitn") method can be used.

##### [§](#examples-38)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lambda".splitn(3, ' ').collect();
assert_eq!(v, ["Mary", "had", "a little lambda"]);

let v: Vec<&str> = "lionXXtigerXleopard".splitn(3, "X").collect();
assert_eq!(v, ["lion", "", "tigerXleopard"]);

let v: Vec<&str> = "abcXdef".splitn(1, 'X').collect();
assert_eq!(v, ["abcXdef"]);

let v: Vec<&str> = "".splitn(1, 'X').collect();
assert_eq!(v, [""]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".splitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "defXghi"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1950-1952)

Returns an iterator over substrings of this string slice, separated by a pattern, starting from the end of the string, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-5)Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

For splitting from the front, the [`splitn`](https://doc.rust-lang.org/std/primitive.str.html#method.splitn "method str::splitn") method can be used.

##### [§](#examples-39)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".rsplitn(3, ' ').collect();
assert_eq!(v, ["lamb", "little", "Mary had a"]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplitn(3, 'X').collect();
assert_eq!(v, ["leopard", "tiger", "lionX"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplitn(2, "::").collect();
assert_eq!(v, ["leopard", "lion::tiger"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".rsplitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "abc1def"]);
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1970)

Splits the string on the first occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### [§](#examples-40)Examples

```rust
assert_eq!("cfg".split_once('='), None);
assert_eq!("cfg=".split_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".split_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".split_once('='), Some(("cfg", "foo=bar")));
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1989-1991)

Splits the string on the last occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### [§](#examples-41)Examples

```rust
assert_eq!("cfg".rsplit_once('='), None);
assert_eq!("cfg=".rsplit_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".rsplit_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".rsplit_once('='), Some(("cfg=foo", "bar")));
```

1.2.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2029)

Returns an iterator over the disjoint matches of a pattern within the given string slice.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-6)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rmatches`](https://doc.rust-lang.org/std/primitive.str.html#method.rmatches "method str::rmatches") method can be used.

##### [§](#examples-42)Examples

```rust
let v: Vec<&str> = "abcXXXabcYYYabc".matches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".matches(char::is_numeric).collect();
assert_eq!(v, ["1", "2", "3"]);
```

1.2.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2063-2065)

Returns an iterator over the disjoint matches of a pattern within this string slice, yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-7)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`matches`](https://doc.rust-lang.org/std/primitive.str.html#method.matches "method str::matches") method can be used.

##### [§](#examples-43)Examples

```rust
let v: Vec<&str> = "abcXXXabcYYYabc".rmatches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".rmatches(char::is_numeric).collect();
assert_eq!(v, ["3", "2", "1"]);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2107)

Returns an iterator over the disjoint matches of a pattern within this string slice as well as the index that the match starts at.

For matches of `pat` within `self` that overlap, only the indices corresponding to the first match are returned.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-8)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rmatch_indices`](https://doc.rust-lang.org/std/primitive.str.html#method.rmatch_indices "method str::rmatch_indices") method can be used.

##### [§](#examples-44)Examples

```rust
let v: Vec<_> = "abcXXXabcYYYabc".match_indices("abc").collect();
assert_eq!(v, [(0, "abc"), (6, "abc"), (12, "abc")]);

let v: Vec<_> = "1abcabc2".match_indices("abc").collect();
assert_eq!(v, [(1, "abc"), (4, "abc")]);

let v: Vec<_> = "ababa".match_indices("aba").collect();
assert_eq!(v, [(0, "aba")]); // only the first `aba`
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2147-2149)

Returns an iterator over the disjoint matches of a pattern within `self`, yielded in reverse order along with the index of the match.

For matches of `pat` within `self` that overlap, only the indices corresponding to the last match are returned.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-9)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`match_indices`](https://doc.rust-lang.org/std/primitive.str.html#method.match_indices "method str::match_indices") method can be used.

##### [§](#examples-45)Examples

```rust
let v: Vec<_> = "abcXXXabcYYYabc".rmatch_indices("abc").collect();
assert_eq!(v, [(12, "abc"), (6, "abc"), (0, "abc")]);

let v: Vec<_> = "1abcabc2".rmatch_indices("abc").collect();
assert_eq!(v, [(4, "abc"), (1, "abc")]);

let v: Vec<_> = "ababa".rmatch_indices("aba").collect();
assert_eq!(v, [(2, "aba")]); // only the last `aba`
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2171)

Returns a string slice with leading and trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#examples-46)Examples

```rust
let s = "\n Hello\tworld\t\n";

assert_eq!("Hello\tworld", s.trim());
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2210)

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#text-directionality)Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### [§](#examples-47)Examples

Basic usage:

```rust
let s = "\n Hello\tworld\t\n";
assert_eq!("Hello\tworld\t\n", s.trim_start());
```

Directionality:

```rust
let s = "  English  ";
assert!(Some('E') == s.trim_start().chars().next());

let s = "  עברית  ";
assert!(Some('ע') == s.trim_start().chars().next());
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2249)

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#text-directionality-1)Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### [§](#examples-48)Examples

Basic usage:

```rust
let s = "\n Hello\tworld\t\n";
assert_eq!("\n Hello\tworld", s.trim_end());
```

Directionality:

```rust
let s = "  English  ";
assert!(Some('h') == s.trim_end().chars().rev().next());

let s = "  עברית  ";
assert!(Some('ת') == s.trim_end().chars().rev().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2289)

👎Deprecated since 1.33.0: superseded by `trim_start`

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### [§](#text-directionality-2)Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### [§](#examples-49)Examples

Basic usage:

```rust
let s = " Hello\tworld\t";

assert_eq!("Hello\tworld\t", s.trim_left());
```

Directionality:

```rust
let s = "  English";
assert!(Some('E') == s.trim_left().chars().next());

let s = "  עברית";
assert!(Some('ע') == s.trim_left().chars().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2329)

👎Deprecated since 1.33.0: superseded by `trim_end`

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### [§](#text-directionality-3)Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### [§](#examples-50)Examples

Basic usage:

```rust
let s = " Hello\tworld\t";

assert_eq!(" Hello\tworld", s.trim_right());
```

Directionality:

```rust
let s = "English  ";
assert!(Some('h') == s.trim_right().chars().rev().next());

let s = "עברית  ";
assert!(Some('ת') == s.trim_right().chars().rev().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2362-2364)

Returns a string slice with all prefixes and suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-51)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_matches('1'), "foo1bar");
assert_eq!("123foo1bar123".trim_matches(char::is_numeric), "foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_matches(x), "foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1foo1barXX".trim_matches(|c| c == '1' || c == 'X'), "foo1bar");
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2409)

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-4)Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### [§](#examples-52)Examples

```rust
assert_eq!("11foo1bar11".trim_start_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_start_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_start_matches(x), "foo1bar12");
```

1.45.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2443)

Returns a string slice with the prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix, wrapped in `Some`. Unlike [`trim_start_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_start_matches "method str::trim_start_matches"), this method removes the prefix exactly once.

If the string does not start with `prefix`, returns `None`.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-53)Examples

```rust
assert_eq!("foo:bar".strip_prefix("foo:"), Some("bar"));
assert_eq!("foo:bar".strip_prefix("bar"), None);
assert_eq!("foofoo".strip_prefix("foo"), Some("foo"));
```

1.45.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2471-2473)

Returns a string slice with the suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix, wrapped in `Some`. Unlike [`trim_end_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_end_matches "method str::trim_end_matches"), this method removes the suffix exactly once.

If the string does not end with `suffix`, returns `None`.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-54)Examples

```rust
assert_eq!("bar:foo".strip_suffix(":foo"), Some("bar"));
assert_eq!("bar:foo".strip_suffix("bar"), None);
assert_eq!("foofoo".strip_suffix("foo"), Some("foo"));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2507-2509)

🔬This is a nightly-only experimental API. (`strip_circumfix` [#147946](https://github.com/rust-lang/rust/issues/147946))

Returns a string slice with the prefix and suffix removed.

If the string starts with the pattern `prefix` and ends with the pattern `suffix`, returns the substring after the prefix and before the suffix, wrapped in `Some`. Unlike [`trim_start_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_start_matches "method str::trim_start_matches") and [`trim_end_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_end_matches "method str::trim_end_matches"), this method removes both the prefix and suffix exactly once.

If the string does not start with `prefix` or does not end with `suffix`, returns `None`.

Each [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-55)Examples

```rust
#![feature(strip_circumfix)]

assert_eq!("bar:hello:foo".strip_circumfix("bar:", ":foo"), Some("hello"));
assert_eq!("bar:foo".strip_circumfix("foo", "foo"), None);
assert_eq!("foo:bar;".strip_circumfix("foo:", ';'), Some("bar"));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2547)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a string slice with the optional prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix. Unlike [`strip_prefix`](https://doc.rust-lang.org/std/primitive.str.html#method.strip_prefix "method str::strip_prefix"), this method always returns `&str` for easy method chaining, instead of returning [`Option<&str>`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option").

If the string does not start with `prefix`, returns the original string unchanged.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-56)Examples

```rust
#![feature(trim_prefix_suffix)]

// Prefix present - removes it
assert_eq!("foo:bar".trim_prefix("foo:"), "bar");
assert_eq!("foofoo".trim_prefix("foo"), "foo");

// Prefix absent - returns original string
assert_eq!("foo:bar".trim_prefix("bar"), "foo:bar");

// Method chaining example
assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2584-2586)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a string slice with the optional suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix. Unlike [`strip_suffix`](https://doc.rust-lang.org/std/primitive.str.html#method.strip_suffix "method str::strip_suffix"), this method always returns `&str` for easy method chaining, instead of returning [`Option<&str>`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option").

If the string does not end with `suffix`, returns the original string unchanged.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-57)Examples

```rust
#![feature(trim_prefix_suffix)]

// Suffix present - removes it
assert_eq!("bar:foo".trim_suffix(":foo"), "bar");
assert_eq!("foofoo".trim_suffix("foo"), "foo");

// Suffix absent - returns original string
assert_eq!("bar:foo".trim_suffix("bar"), "bar:foo");

// Method chaining example
assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2627-2629)

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-5)Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### [§](#examples-58)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_end_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_end_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_end_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1fooX".trim_end_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2671)

👎Deprecated since 1.33.0: superseded by `trim_start_matches`

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-6)Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### [§](#examples-59)Examples

```rust
assert_eq!("11foo1bar11".trim_left_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_left_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_left_matches(x), "foo1bar12");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2714-2716)

👎Deprecated since 1.33.0: superseded by `trim_end_matches`

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-7)Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### [§](#examples-60)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_right_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_right_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_right_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1fooX".trim_right_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2765)

Parses this string slice into another type.

Because `parse` is so general, it can cause problems with type inference. As such, `parse` is one of the few times you’ll see the syntax affectionately known as the ‘turbofish’: `::<>`. This helps the inference algorithm understand specifically which type you’re trying to parse into.

`parse` can parse into any type that implements the [`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html "trait std::str::FromStr") trait.

##### [§](#errors-1)Errors

Will return [`Err`](https://doc.rust-lang.org/std/str/trait.FromStr.html#associatedtype.Err "associated type std::str::FromStr::Err") if it’s not possible to parse this string slice into the desired type.

##### [§](#examples-61)Examples

Basic usage:

```rust
let four: u32 = "4".parse().unwrap();

assert_eq!(4, four);
```

Using the ‘turbofish’ instead of annotating `four`:

```rust
let four = "4".parse::<u32>();

assert_eq!(Ok(4), four);
```

Failing to parse:

```rust
let nope = "j".parse::<u32>();

assert!(nope.is_err());
```

1.23.0 (const: 1.74.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2786)

Checks if all characters in this string are within the ASCII range.

An empty string returns `true`.

##### [§](#examples-62)Examples

```rust
let ascii = "hello!\n";
let non_ascii = "Grüße, Jürgen ❤";

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2798)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

If this string slice [`is_ascii`](https://doc.rust-lang.org/std/primitive.str.html#method.is_ascii "method str::is_ascii"), returns it as a slice of [ASCII characters](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), otherwise returns `None`.

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2812)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this string slice into a slice of [ASCII characters](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), without checking whether they are valid.

##### [§](#safety-6)Safety

Every character in this string must be ASCII, or else this is UB.

1.23.0 (const: 1.89.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2840)

Checks that two strings are an ASCII case-insensitive match.

Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`, but without allocating and copying temporaries.

##### [§](#examples-63)Examples

```rust
assert!("Ferris".eq_ignore_ascii_case("FERRIS"));
assert!("Ferrös".eq_ignore_ascii_case("FERRöS"));
assert!(!"Ferrös".eq_ignore_ascii_case("FERRÖS"));
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2866)

Converts this string to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`to_ascii_uppercase()`](#method.to_ascii_uppercase).

##### [§](#examples-64)Examples

```rust
let mut s = String::from("Grüße, Jürgen ❤");

s.make_ascii_uppercase();

assert_eq!("GRüßE, JüRGEN ❤", s);
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2894)

Converts this string to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`to_ascii_lowercase()`](#method.to_ascii_lowercase).

##### [§](#examples-65)Examples

```rust
let mut s = String::from("GRÜßE, JÜRGEN ❤");

s.make_ascii_lowercase();

assert_eq!("grÜße, jÜrgen ❤", s);
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2919)

Returns a string slice with leading ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-66)Examples

```rust
assert_eq!(" \t \u{3000}hello world\n".trim_ascii_start(), "\u{3000}hello world\n");
assert_eq!("  ".trim_ascii_start(), "");
assert_eq!("".trim_ascii_start(), "");
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2944)

Returns a string slice with trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-67)Examples

```rust
assert_eq!("\r hello world\u{3000}\n ".trim_ascii_end(), "\r hello world\u{3000}");
assert_eq!("  ".trim_ascii_end(), "");
assert_eq!("".trim_ascii_end(), "");
```

1.80.0 (const: 1.80.0) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2970)

Returns a string slice with leading and trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-68)Examples

```rust
assert_eq!("\r hello world\n ".trim_ascii(), "hello world");
assert_eq!("  ".trim_ascii(), "");
assert_eq!("".trim_ascii(), "");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3013)

Returns an iterator that escapes each char in `self` with [`char::escape_debug`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_debug "method char::escape_debug").

Note: only extended grapheme codepoints that begin the string will be escaped.

##### [§](#examples-69)Examples

As an iterator:

```rust
for c in "❤\n!".escape_debug() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_debug());
```

Both are equivalent to:

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_debug().to_string(), "❤\\n!");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3059)

Returns an iterator that escapes each char in `self` with [`char::escape_default`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_default "method char::escape_default").

##### [§](#examples-70)Examples

As an iterator:

```rust
for c in "❤\n!".escape_default() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_default());
```

Both are equivalent to:

```rust
println!("\\u{{2764}}\\n!");
```

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_default().to_string(), "\\u{2764}\\n!");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3097)

Returns an iterator that escapes each char in `self` with [`char::escape_unicode`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_unicode "method char::escape_unicode").

##### [§](#examples-71)Examples

As an iterator:

```rust
for c in "❤\n!".escape_unicode() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_unicode());
```

Both are equivalent to:

```rust
println!("\\u{{2764}}\\u{{a}}\\u{{21}}");
```

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_unicode().to_string(), "\\u{2764}\\u{a}\\u{21}");
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3130)

🔬This is a nightly-only experimental API. (`substr_range` [#126769](https://github.com/rust-lang/rust/issues/126769))

Returns the range that a substring points to.

Returns `None` if `substr` does not point within `self`.

Unlike [`str::find`](https://doc.rust-lang.org/std/primitive.str.html#method.find "method str::find"), **this does not search through the string**. Instead, it uses pointer arithmetic to find where in the string `substr` is derived from.

This is useful for extending [`str::split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split") and similar methods.

Note that this method may return false positives (typically either `Some(0..0)` or `Some(self.len()..self.len())`) if `substr` is a zero-length `str` that points at the beginning or end of another, independent, `str`.

##### [§](#examples-72)Examples

```rust
#![feature(substr_range)]

let data = "a, b, b, a";
let mut iter = data.split(", ").map(|s| data.substr_range(s).unwrap());

assert_eq!(iter.next(), Some(0..1));
assert_eq!(iter.next(), Some(3..4));
assert_eq!(iter.next(), Some(6..7));
assert_eq!(iter.next(), Some(9..10));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3141)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&str`.

This method is redundant when used directly on `&str`, but it helps dereferencing other string-like types to string slices, for example references to `Box<str>` or `Arc<str>`.

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#222)[§](#impl-str-1)

Methods for string slices.

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#237)

Converts a `Box<str>` into a `Box<[u8]>` without copying or allocating.

##### [§](#examples-73)Examples

```rust
let s = "this is a string";
let boxed_str = s.to_owned().into_boxed_str();
let boxed_bytes = boxed_str.into_boxed_bytes();
assert_eq!(*boxed_bytes, *s.as_bytes());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#268)

Replaces all matches of a pattern with another string.

`replace` creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"), and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice.

##### [§](#examples-74)Examples

```rust
let s = "this is old";

assert_eq!("this is new", s.replace("old", "new"));
assert_eq!("than an old", s.replace("is", "an"));
```

When the pattern doesn’t match, it returns this string slice as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"):

```rust
let s = "this is old";
assert_eq!(s, s.replace("cookie monster", "little lamb"));
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#323)

Replaces first N matches of a pattern with another string.

`replacen` creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"), and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice at most `count` times.

##### [§](#examples-75)Examples

```rust
let s = "foo foo 123 foo";
assert_eq!("new new 123 foo", s.replacen("foo", "new", 2));
assert_eq!("faa fao 123 foo", s.replacen('o', "a", 3));
assert_eq!("foo foo new23 foo", s.replacen(char::is_numeric, "new", 1));
```

When the pattern doesn’t match, it returns this string slice as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"):

```rust
let s = "this is old";
assert_eq!(s, s.replacen("cookie monster", "little lamb", 10));
```

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#380)

Returns the lowercase equivalent of this string slice, as a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

‘Lowercase’ is defined according to the terms of the Unicode Derived Core Property `Lowercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") instead of modifying the parameter in-place.

##### [§](#examples-76)Examples

Basic usage:

```rust
let s = "HELLO";

assert_eq!("hello", s.to_lowercase());
```

A tricky example, with sigma:

```rust
let sigma = "Σ";

assert_eq!("σ", sigma.to_lowercase());

// but at the end of a word, it's ς, not σ:
let odysseus = "ὈΔΥΣΣΕΎΣ";

assert_eq!("ὀδυσσεύς", odysseus.to_lowercase());
```

Languages without case are not changed:

```rust
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_lowercase());
```

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#465)

Returns the uppercase equivalent of this string slice, as a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

‘Uppercase’ is defined according to the terms of the Unicode Derived Core Property `Uppercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") instead of modifying the parameter in-place.

##### [§](#examples-77)Examples

Basic usage:

```rust
let s = "hello";

assert_eq!("HELLO", s.to_uppercase());
```

Scripts without case are not changed:

```rust
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_uppercase());
```

One character can become multiple:

```rust
let s = "tschüß";

assert_eq!("TSCHÜSS", s.to_uppercase());
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#499)

Converts a [`Box<str>`](https://doc.rust-lang.org/std/boxed/struct.Box.html "struct std::boxed::Box") into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") without copying or allocating.

##### [§](#examples-78)Examples

```rust
let string = String::from("birthday gift");
let boxed_str = string.clone().into_boxed_str();

assert_eq!(boxed_str.into_string(), string);
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#529)

Creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") by repeating a string `n` times.

##### [§](#panics-2)Panics

This function will panic if the capacity would overflow.

##### [§](#examples-79)Examples

Basic usage:

```rust
assert_eq!("abc".repeat(4), String::from("abcabcabcabc"));
```

A panic upon overflow:

[ⓘ](# "This example panics")

```rust
// this will panic at runtime
let huge = "0123456789abcdef".repeat(usize::MAX);
```

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#559)

Returns a copy of this string where each character is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`make_ascii_uppercase`](https://doc.rust-lang.org/std/primitive.str.html#method.make_ascii_uppercase "method str::make_ascii_uppercase").

To uppercase ASCII characters in addition to non-ASCII characters, use [`to_uppercase`](#method.to_uppercase).

##### [§](#examples-80)Examples

```rust
let s = "Grüße, Jürgen ❤";

assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
```

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#591)

Returns a copy of this string where each character is mapped to its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`make_ascii_lowercase`](https://doc.rust-lang.org/std/primitive.str.html#method.make_ascii_lowercase "method str::make_ascii_lowercase").

To lowercase ASCII characters in addition to non-ASCII characters, use [`to_lowercase`](#method.to_lowercase).

##### [§](#examples-81)Examples

```rust
let s = "Grüße, Jürgen ❤";

assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ascii.rs.html#206-210)[§](#impl-AsciiExt-for-str)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#207)[§](#associatedtype.Owned-1)

👎Deprecated since 1.26.0: use inherent methods instead

Container type for copied ASCII characters.

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.is_ascii-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks if the value is within the ASCII range. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.is_ascii)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.to_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII upper case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.to_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII lower case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_lowercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.eq_ignore_ascii_case-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks that two values are an ASCII case-insensitive match. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.eq_ignore_ascii_case)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.make_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII upper case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#209)[§](#method.make_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII lower case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_lowercase)

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#470)[§](#impl-Add%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#471)[§](#associatedtype.Output-11)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#474)[§](#method.add)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2771)[§](#impl-Add%3C%26str%3E-for-String)

Implements the `+` operator for concatenating two strings.

This consumes the `String` on the left-hand side and re-uses its buffer (growing it if necessary). This is done to avoid allocating a new `String` and copying the entire contents on every operation, which would lead to *O*(*n*^2) running time when building an *n*-byte string by repeated concatenation.

The string on the right-hand side is only borrowed; its contents are copied into the returned `String`.

#### [§](#examples-84)Examples

Concatenating two `String`s takes the first by value and borrows the second:

```rust
let a = String::from("hello");
let b = String::from(" world");
let c = a + &b;
// `a` is moved and can no longer be used here.
```

If you want to keep using the first `String`, you can clone it and append to the clone instead:

```rust
let a = String::from("hello");
let b = String::from(" world");
let c = a.clone() + &b;
// `a` is still valid here.
```

Concatenating `&str` slices can be done by converting the first to a `String`:

```rust
let a = "hello";
let b = " world";
let c = a.to_string() + b;
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2772)[§](#associatedtype.Output-12)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2775)[§](#method.add-1)

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#494)[§](#impl-AddAssign%3C%26str%3E-for-Cow%3C'a,+str%3E)

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2786)[§](#impl-AddAssign%3C%26str%3E-for-String)

Implements the `+=` operator for appending to a `String`.

This has the same behavior as the [`push_str`](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str "method std::string::String::push_str") method.

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3091)[§](#impl-AsMut%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3093)[§](#method.as_mut-1)

Converts this type into a mutable reference of the (usually inferred) input type.

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#872)[§](#impl-AsMut%3Cstr%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#874)[§](#method.as_mut)

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3148)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3150)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#239)[§](#impl-AsRef%3CByteStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#241)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1716-1721)[§](#impl-AsRef%3COsStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1718-1720)[§](#method.as_ref-5)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3800-3805)[§](#impl-AsRef%3CPath%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3802-3804)[§](#method.as_ref-6)

Converts this type into a shared reference of the (usually inferred) input type.

1.55.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3548)[§](#impl-AsRef%3Cstr%3E-for-Drain%3C'a%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3549)[§](#method.as_ref-4)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3083)[§](#impl-AsRef%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3085)[§](#method.as_ref-3)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#863)[§](#impl-AsRef%3Cstr%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#865)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#189)[§](#impl-Borrow%3Cstr%3E-for-String)

1.36.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#197)[§](#impl-BorrowMut%3Cstr%3E-for-String)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#2075)[§](#impl-Clone-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#567)[§](#impl-CloneToUninit-for-str)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#570)[§](#method.clone_to_uninit)

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#62)[§](#impl-Concat%3Cstr%3E-for-%5BS%5D)

Note: `str` in `Concat<str>` is not meaningful here. This type parameter of the trait only exists to enable another impl.

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#63)[§](#associatedtype.Output-13)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#65)[§](#method.concat)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#2909)[§](#impl-Debug-for-str)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3167)[§](#impl-Default-for-%26mut+str)

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3170)[§](#method.default-1)

Creates an empty mutable str

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3157)[§](#impl-Default-for-%26str)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed.rs.html#1963)[§](#impl-Default-for-Box%3Cstr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#2958)[§](#impl-Display-for-str)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2506)[§](#impl-Extend%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2507)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2512)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3949)[§](#impl-From%3C%26mut+str%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3962)[§](#method.from-12)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-4)Example

```rust
let mut original = String::from("eggplant");
let original: &mut str = &mut original;
let shared: Arc<str> = Arc::from(original);
assert_eq!("eggplant", &shared[..]);
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#144)[§](#impl-From%3C%26mut+str%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#159)[§](#method.from-1)

Converts a `&mut str` into a `Box<str>`

This conversion allocates on the heap and performs a copy of `s`.

##### [§](#examples-86)Examples

```rust
let mut original = String::from("hello");
let original: &mut str = &mut original;
let boxed: Box<str> = Box::from(original);
println!("{boxed}");
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2915)[§](#impl-From%3C%26mut+str%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2928)[§](#method.from-6)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example-1)Example

```rust
let mut original = String::from("statue");
let original: &mut str = &mut original;
let shared: Rc<str> = Rc::from(original);
assert_eq!("statue", &shared[..]);
```

1.44.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3120)[§](#impl-From%3C%26mut+str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3125)[§](#method.from-8)

Converts a `&mut str` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

The result is allocated on the heap.

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3930)[§](#impl-From%3C%26str%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3941)[§](#method.from-11)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-3)Example

```rust
let shared: Arc<str> = Arc::from("eggplant");
assert_eq!("eggplant", &shared[..]);
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#645)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#659)[§](#method.from-4)

Converts a [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-89)Examples

```rust
use std::error::Error;

let a_str_error = "a str error";
let a_boxed_error = Box::<dyn Error>::from(a_str_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#622)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#638)[§](#method.from-3)

Converts a [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-88)Examples

```rust
use std::error::Error;

let a_str_error = "a str error";
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_str_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#124)[§](#impl-From%3C%26str%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#137)[§](#method.from)

Converts a `&str` into a `Box<str>`

This conversion allocates on the heap and performs a copy of `s`.

##### [§](#examples-85)Examples

```rust
let boxed: Box<str> = Box::from("hello");
println!("{boxed}");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3207)[§](#impl-From%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3221)[§](#method.from-10)

Converts a string slice into a [`Borrowed`](https://doc.rust-lang.org/std/borrow/enum.Cow.html#variant.Borrowed "borrow::Cow::Borrowed") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-2)Example

```rust
assert_eq!(Cow::from("eggplant"), Cow::Borrowed("eggplant"));
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2896)[§](#impl-From%3C%26str%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2907)[§](#method.from-5)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example)Example

```rust
let shared: Rc<str> = Rc::from("statue");
assert_eq!("statue", &shared[..]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3108)[§](#impl-From%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3113)[§](#method.from-7)

Converts a `&str` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

The result is allocated on the heap.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4423)[§](#impl-From%3C%26str%3E-for-Vec%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4431)[§](#method.from-13)

Allocates a `Vec<u8>` and fills it with a UTF-8 string.

##### [§](#examples-91)Examples

```rust
assert_eq!(Vec::from("123"), vec![b'1', b'2', b'3']);
```

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#166)[§](#impl-From%3CCow%3C'_,+str%3E%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#191)[§](#method.from-2)

Converts a `Cow<'_, str>` into a `Box<str>`

When `cow` is the `Cow::Borrowed` variant, this conversion allocates on the heap and copies the underlying `str`. Otherwise, it will try to reuse the owned `String`’s allocation.

##### [§](#examples-87)Examples

```rust
use std::borrow::Cow;

let unboxed = Cow::Borrowed("hello");
let boxed: Box<str> = Box::from(unboxed);
println!("{boxed}");
```

```rust
let unboxed = Cow::Owned("hello".to_string());
let boxed: Box<str> = Box::from(unboxed);
println!("{boxed}");
```

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3164)[§](#impl-From%3CString%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3176)[§](#method.from-9)

Converts the given [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") to a boxed `str` slice that is owned.

##### [§](#examples-90)Examples

```rust
let s1: String = String::from("hello world");
let s2: Box<str> = Box::from(s1);
let s3: String = String::from(s2);

assert_eq!("hello world", s3)
```

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#158)[§](#impl-FromIterator%3C%26char%3E-for-Box%3Cstr%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#166)[§](#impl-FromIterator%3C%26str%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#280)[§](#impl-FromIterator%3C%26str%3E-for-ByteString)

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3281)[§](#impl-FromIterator%3C%26str%3E-for-Cow%3C'a,+str%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2386)[§](#impl-FromIterator%3C%26str%3E-for-String)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#182)[§](#impl-FromIterator%3CBox%3Cstr,+A%3E%3E-for-Box%3Cstr%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#190)[§](#impl-FromIterator%3CCow%3C'a,+str%3E%3E-for-Box%3Cstr%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#174)[§](#impl-FromIterator%3CString%3E-for-Box%3Cstr%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#150)[§](#impl-FromIterator%3Cchar%3E-for-Box%3Cstr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#862)[§](#impl-Hash-for-str)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#55-57)[§](#impl-Index%3CI%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#59)[§](#associatedtype.Output-10)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#62)[§](#method.index-10)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#69-71)[§](#impl-IndexMut%3CI%3E-for-str)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#72)[§](#impl-Join%3C%26str%3E-for-%5BS%5D)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#73)[§](#associatedtype.Output-14)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#75)[§](#method.join)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#18)[§](#impl-Ord-for-str)

Implements ordering of strings.

Strings are ordered [lexicographically](https://doc.rust-lang.org/std/cmp/trait.Ord.html#lexicographical-comparison "trait std::cmp::Ord") by their byte values. This orders Unicode code points based on their positions in the code charts. This is not necessarily the same as “alphabetical” order, which varies by language and locale. Sorting strings according to culturally-accepted standards requires locale-specific data that is outside the scope of the `str` type.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#137)[§](#impl-PartialEq%3C%26str%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#137)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#529)[§](#impl-PartialEq%3C%26str%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#529)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#impl-PartialEq%3C%26str%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.29.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#745-750)[§](#impl-PartialEq%3C%26str%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#747-749)[§](#method.eq-19)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-19)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#impl-PartialEq%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#137)[§](#impl-PartialEq%3CByteStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#137)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#135)[§](#impl-PartialEq%3CByteStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#135)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#529)[§](#impl-PartialEq%3CByteString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#529)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#527)[§](#impl-PartialEq%3CByteString%3E-for-str)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#527)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2694)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1512-1517)[§](#impl-PartialEq%3COsStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1514-1516)[§](#method.eq-22)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-22)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.29.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#753-758)[§](#impl-PartialEq%3COsString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#755-757)[§](#method.eq-20)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-20)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#737-742)[§](#impl-PartialEq%3COsString%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#739-741)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3667-3672)[§](#impl-PartialEq%3CPath%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3669-3671)[§](#method.eq-26)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-26)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2232-2237)[§](#impl-PartialEq%3CPathBuf%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#2234-2236)[§](#method.eq-24)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-24)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#impl-PartialEq%3CString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#impl-PartialEq%3CString%3E-for-str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#135)[§](#impl-PartialEq%3Cstr%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#135)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#527)[§](#impl-PartialEq%3Cstr%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#527)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#impl-PartialEq%3Cstr%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2692)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1504-1509)[§](#impl-PartialEq%3Cstr%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1506-1508)[§](#method.eq-21)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-21)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#729-734)[§](#impl-PartialEq%3Cstr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#731-733)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3658-3664)[§](#impl-PartialEq%3Cstr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3660-3663)[§](#method.eq-25)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-25)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2224-2229)[§](#impl-PartialEq%3Cstr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#2226-2228)[§](#method.eq-23)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-23)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#impl-PartialEq%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#27)[§](#impl-PartialEq-for-str)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#29)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1547-1552)[§](#impl-PartialOrd%3Cstr%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1549-1551)[§](#method.partial_cmp-2)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-2)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-2)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-2)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-2)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#788-793)[§](#impl-PartialOrd%3Cstr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#790-792)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#46)[§](#impl-PartialOrd-for-str)

Implements comparison operations on strings.

Strings are compared [lexicographically](https://doc.rust-lang.org/std/cmp/trait.Ord.html#lexicographical-comparison "trait std::cmp::Ord") by their byte values. This compares Unicode code points based on their positions in the code charts. This is not necessarily the same as “alphabetical” order, which varies by language and locale. Comparing strings according to culturally-accepted standards requires locale-specific data that is outside the scope of the `str` type.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#48)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#971)[§](#impl-Pattern-for-%26str)

Non-allocating substring search.

Will handle the pattern `""` as returning empty matches at each character boundary.

#### [§](#examples-83)Examples

```rust
assert_eq!("Hello world".find("world"), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#981)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#987)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#1017)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#1028-1030)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#1037-1039)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#972)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#975)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#1051)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

1.73.0 · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#380)[§](#impl-SliceIndex%3Cstr%3E-for-%28Bound%3Cusize%3E,+Bound%3Cusize%3E%29)

Implements substring slicing for arbitrary bounds.

Returns a slice of the given string bounded by the byte indices provided by each bound.

This operation is *O*(1).

#### [§](#panics-4)Panics

Panics if `begin` or `end` (if it exists and once adjusted for inclusion/exclusion) does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `begin > end`, or if `end > len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#381)[§](#associatedtype.Output-3)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#384)[§](#method.get-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#389)[§](#method.get_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#394)[§](#method.get_unchecked-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#401)[§](#method.get_unchecked_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#408)[§](#method.index-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#413)[§](#method.index_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#158)[§](#impl-SliceIndex%3Cstr%3E-for-Range%3Cusize%3E)

Implements substring slicing with syntax `&self[begin .. end]` or `&mut self[begin .. end]`.

Returns a slice of the given string from the byte range [`begin`, `end`).

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-3)Panics

Panics if `begin` or `end` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `begin > end`, or if `end > len`.

#### [§](#examples-82)Examples

```rust
let s = "Löwe 老虎 Léopard";
assert_eq!(&s[0 .. 1], "L");

assert_eq!(&s[1 .. 9], "öwe 老");

// these will panic:
// byte 2 lies within `ö`:
// &s[2 ..3];

// byte 8 lies within `老`
// &s[1 .. 8];

// byte 100 is outside the string
// &s[3 .. 100];
```

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#159)[§](#associatedtype.Output-1)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#161)[§](#method.get-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#175)[§](#method.get_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#189)[§](#method.get_unchecked-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#217)[§](#method.get_unchecked_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#237)[§](#method.index-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#245)[§](#method.index_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#263)[§](#impl-SliceIndex%3Cstr%3E-for-Range%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#264)[§](#associatedtype.Output-2)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#266)[§](#method.get-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#280)[§](#method.get_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#294)[§](#method.get_unchecked-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#322)[§](#method.get_unchecked_mut-3)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#342)[§](#method.index-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#350)[§](#method.index_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#504)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFrom%3Cusize%3E)

Implements substring slicing with syntax `&self[begin ..]` or `&mut self[begin ..]`.

Returns a slice of the given string from the byte range \[`begin`, `len`). Equivalent to `&self[begin .. len]` or `&mut self[begin .. len]`.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-6)Panics

Panics if `begin` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), or if `begin > len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#505)[§](#associatedtype.Output-5)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#507)[§](#method.get-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#517)[§](#method.get_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#527)[§](#method.get_unchecked-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#533)[§](#method.get_unchecked_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#539)[§](#method.index-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#547)[§](#method.index_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#560)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFrom%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#561)[§](#associatedtype.Output-6)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#563)[§](#method.get-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#573)[§](#method.get_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#583)[§](#method.get_unchecked-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#589)[§](#method.get_unchecked_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#595)[§](#method.index-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#603)[§](#method.index_mut-6)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#93)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFull)

Implements substring slicing with syntax `&self[..]` or `&mut self[..]`.

Returns a slice of the whole string, i.e., returns `&self` or `&mut self`. Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`. Unlike other indexing operations, this can never panic.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#94)[§](#associatedtype.Output)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#96)[§](#method.get-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#100)[§](#method.get_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#104)[§](#method.get_unchecked-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#108)[§](#method.get_unchecked_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#112)[§](#method.index)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#116)[§](#method.index_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#632)[§](#impl-SliceIndex%3Cstr%3E-for-RangeInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[begin ..= end]` or `&mut self[begin ..= end]`.

Returns a slice of the given string from the byte range \[`begin`, `end`]. Equivalent to `&self [begin .. end + 1]` or `&mut self[begin .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics-7)Panics

Panics if `begin` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset or equal to `len`), if `begin > end`, or if `end >= len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#633)[§](#associatedtype.Output-7)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#635)[§](#method.get-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#639)[§](#method.get_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#643)[§](#method.get_unchecked-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#648)[§](#method.get_unchecked_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#653)[§](#method.index-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#670)[§](#method.index_mut-7)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#690)[§](#impl-SliceIndex%3Cstr%3E-for-RangeInclusive%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#691)[§](#associatedtype.Output-8)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#693)[§](#method.get-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#697)[§](#method.get_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#701)[§](#method.get_unchecked-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#706)[§](#method.get_unchecked_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#711)[§](#method.index-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#715)[§](#method.index_mut-8)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#435)[§](#impl-SliceIndex%3Cstr%3E-for-RangeTo%3Cusize%3E)

Implements substring slicing with syntax `&self[.. end]` or `&mut self[.. end]`.

Returns a slice of the given string from the byte range \[0, `end`). Equivalent to `&self[0 .. end]` or `&mut self[0 .. end]`.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-5)Panics

Panics if `end` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), or if `end > len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#436)[§](#associatedtype.Output-4)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#438)[§](#method.get-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#448)[§](#method.get_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#458)[§](#method.get_unchecked-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#463)[§](#method.get_unchecked_mut-5)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#468)[§](#method.index-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#476)[§](#method.index_mut-4)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#736)[§](#impl-SliceIndex%3Cstr%3E-for-RangeToInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[..= end]` or `&mut self[..= end]`.

Returns a slice of the given string from the byte range \[0, `end`]. Equivalent to `&self [0 .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics-8)Panics

Panics if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset as defined by `is_char_boundary`, or equal to `len`), or if `end >= len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#737)[§](#associatedtype.Output-9)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#739)[§](#method.get-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#743)[§](#method.get_mut-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#747)[§](#method.get_unchecked-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#752)[§](#method.get_unchecked_mut-10)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#757)[§](#method.index-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#761)[§](#method.index_mut-9)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#206)[§](#impl-ToOwned-for-str)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#207)[§](#associatedtype.Owned)

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#210)[§](#method.to_owned)

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/src/alloc/str.rs.html#215)[§](#method.clone_into)

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#224-243)[§](#impl-ToSocketAddrs-for-str)

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#225)[§](#associatedtype.Iter)

Returned iterator over socket addresses which this type may correspond to.

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#226-242)[§](#method.to_socket_addrs)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#343)[§](#impl-TryFrom%3C%26ByteStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#344)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#347)[§](#method.try_from)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#577)[§](#impl-TryFrom%3C%26ByteString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#578)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#581)[§](#method.try_from-2)

Performs the conversion.

1.72.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1460-1475)[§](#impl-TryFrom%3C%26OsStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1472-1474)[§](#method.try_from-3)

Tries to convert an `&OsStr` to a `&str`.

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("foo");
let as_str = <&str>::try_from(os_str).unwrap();
assert_eq!(as_str, "foo");
```

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1461)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#354)[§](#impl-TryFrom%3C%26mut+ByteStr%3E-for-%26mut+str)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#355)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#358)[§](#method.try_from-1)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1111-1118)[§](#impl-ConstParamTy_-for-str)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#36)[§](#impl-Eq-for-str)

1.65.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3232)[§](#impl-Error-for-%26str)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-str)

[§](#impl-Freeze-for-str)

[§](#impl-RefUnwindSafe-for-str)

[§](#impl-Send-for-str)

[§](#impl-Sized-for-str)

[§](#impl-Sync-for-str)

[§](#impl-Unpin-for-str)

[§](#impl-UnsafeUnpin-for-str)

[§](#impl-UnwindSafe-for-str)