---
title: TryFrom in std::convert - Rust
url: https://doc.rust-lang.org/std/convert/trait.TryFrom.html
source: crawler
fetched_at: 2026-05-06T21:23:51.750335684-03:00
rendered_js: false
word_count: 1942
summary: The TryFrom trait provides a standardized interface for performing fallible type conversions in Rust, allowing developers to handle potential errors gracefully.
tags:
    - rust
    - type-conversion
    - trait
    - error-handling
    - fallible-conversion
category: reference
---

## Trait TryFrom

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#694)

```rust
pub trait TryFrom<T>: Sized {
    type Error;

    // Required method
    fn try_from(value: T) -> Result<Self, Self::Error>;
}
```

Expand description

Simple and safe type conversions that may fail in a controlled way under some circumstances. It is the reciprocal of [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto").

This is useful when you are doing a type conversion that may trivially succeed but may also need special handling. For example, there is no way to convert an [`i64`](https://doc.rust-lang.org/std/primitive.i64.html "primitive i64") into an [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32") using the [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") trait, because an [`i64`](https://doc.rust-lang.org/std/primitive.i64.html "primitive i64") may contain a value that an [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32") cannot represent and so the conversion would lose data. This might be handled by truncating the [`i64`](https://doc.rust-lang.org/std/primitive.i64.html "primitive i64") to an [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32") or by simply returning [`i32::MAX`](https://doc.rust-lang.org/std/primitive.i32.html#associatedconstant.MAX "associated constant i32::MAX"), or by some other method. The [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") trait is intended for perfect conversions, so the `TryFrom` trait informs the programmer when a type conversion could go bad and lets them decide how to handle it.

## [§](#generic-implementations)Generic Implementations

- `TryFrom<T> for U` implies [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto")`<U> for T`
- [`try_from`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#tymethod.try_from "associated function std::convert::TryFrom::try_from") is reflexive, which means that `TryFrom<T> for T` is implemented and cannot fail – the associated `Error` type for calling `T::try_from()` on a value of type `T` is [`Infallible`](https://doc.rust-lang.org/std/convert/enum.Infallible.html "enum std::convert::Infallible"). When the [`!`](https://doc.rust-lang.org/std/primitive.never.html "primitive never") type is stabilized [`Infallible`](https://doc.rust-lang.org/std/convert/enum.Infallible.html "enum std::convert::Infallible") and [`!`](https://doc.rust-lang.org/std/primitive.never.html "primitive never") will be equivalent.

Prefer using [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") over [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") when specifying trait bounds on a generic function to ensure that types that only implement [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") can be used as well.

`TryFrom<T>` can be implemented as follows:

```rust
struct GreaterThanZero(i32);

impl TryFrom<i32> for GreaterThanZero {
    type Error = &'static str;

    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value <= 0 {
            Err("GreaterThanZero only accepts values greater than zero!")
        } else {
            Ok(GreaterThanZero(value))
        }
    }
}
```

## [§](#examples)Examples

As described, [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32") implements `TryFrom<`[`i64`](https://doc.rust-lang.org/std/primitive.i64.html "primitive i64")`>`:

```rust
let big_number = 1_000_000_000_000i64;
// Silently truncates `big_number`, requires detecting
// and handling the truncation after the fact.
let smaller_number = big_number as i32;
assert_eq!(smaller_number, -727379968);

// Returns an error because `big_number` is too big to
// fit in an `i32`.
let try_smaller_number = i32::try_from(big_number);
assert!(try_smaller_number.is_err());

// Returns `Ok(3)`.
let try_successful_smaller_number = i32::try_from(3);
assert!(try_successful_smaller_number.is_ok());
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#697)

The type returned in the event of a conversion error.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#702)

Performs the conversion.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*

1.59.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#105)[§](#impl-TryFrom%3Cchar%3E-for-u8)

Maps a `char` with a code point from U+0000 to U+00FF (inclusive) to a byte in `0x00..=0xFF` with the same value, failing if the code point is greater than U+00FF.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#106)[§](#associatedtype.Error-1)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#135)[§](#impl-TryFrom%3Cchar%3E-for-u16)

Maps a `char` with a code point from U+0000 to U+FFFF (inclusive) to a `u16` in `0x0000..=0xFFFF` with the same value, failing if the code point is greater than U+FFFF.

This corresponds to the UCS-2 encoding, as specified in ISO/IEC 10646:2003.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#136)[§](#associatedtype.Error-2)

1.94.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#167)[§](#impl-TryFrom%3Cchar%3E-for-usize)

Maps a `char` with a code point from U+0000 to U+10FFFF (inclusive) to a `usize` in `0x0000..=0x10FFFF` with the same value, failing if the final value is unrepresentable by `usize`.

Generally speaking, this conversion can be seen as obtaining the character’s corresponding UTF-32 code point to the extent representable by pointer addresses.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#168)[§](#associatedtype.Error-3)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci8%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-4)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-5)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-6)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-7)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-8)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#impl-TryFrom%3Ci8%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#394)[§](#associatedtype.Error-9)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#impl-TryFrom%3Ci8%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#associatedtype.Error-10)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#568)[§](#impl-TryFrom%3Ci8%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#568)[§](#associatedtype.Error-11)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci16%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-12)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#381)[§](#impl-TryFrom%3Ci16%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#381)[§](#associatedtype.Error-13)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#395)[§](#impl-TryFrom%3Ci16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#395)[§](#associatedtype.Error-14)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-15)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-16)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-17)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#impl-TryFrom%3Ci16%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#396)[§](#associatedtype.Error-18)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#impl-TryFrom%3Ci16%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#associatedtype.Error-19)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#569)[§](#impl-TryFrom%3Ci16%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#569)[§](#associatedtype.Error-20)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci32%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-21)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#382)[§](#impl-TryFrom%3Ci32%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#382)[§](#associatedtype.Error-22)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#382)[§](#impl-TryFrom%3Ci32%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#382)[§](#associatedtype.Error-23)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#476)[§](#impl-TryFrom%3Ci32%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#476)[§](#associatedtype.Error-24)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#impl-TryFrom%3Ci32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#associatedtype.Error-25)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#impl-TryFrom%3Ci32%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#397)[§](#associatedtype.Error-26)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#impl-TryFrom%3Ci32%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#associatedtype.Error-27)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#impl-TryFrom%3Ci32%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#associatedtype.Error-28)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#impl-TryFrom%3Ci32%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#398)[§](#associatedtype.Error-29)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#impl-TryFrom%3Ci32%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#associatedtype.Error-30)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#570)[§](#impl-TryFrom%3Ci32%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#570)[§](#associatedtype.Error-31)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci64%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-32)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#impl-TryFrom%3Ci64%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#associatedtype.Error-33)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#impl-TryFrom%3Ci64%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#associatedtype.Error-34)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#impl-TryFrom%3Ci64%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#383)[§](#associatedtype.Error-35)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#476)[§](#impl-TryFrom%3Ci64%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#476)[§](#associatedtype.Error-36)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#impl-TryFrom%3Ci64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#associatedtype.Error-37)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#impl-TryFrom%3Ci64%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#associatedtype.Error-38)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#impl-TryFrom%3Ci64%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#399)[§](#associatedtype.Error-39)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#400)[§](#impl-TryFrom%3Ci64%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#400)[§](#associatedtype.Error-40)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#400)[§](#impl-TryFrom%3Ci64%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#400)[§](#associatedtype.Error-41)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#impl-TryFrom%3Ci64%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#471)[§](#associatedtype.Error-42)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#571)[§](#impl-TryFrom%3Ci64%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#571)[§](#associatedtype.Error-43)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci128%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-44)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#impl-TryFrom%3Ci128%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#associatedtype.Error-45)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#impl-TryFrom%3Ci128%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#associatedtype.Error-46)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#impl-TryFrom%3Ci128%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#associatedtype.Error-47)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#impl-TryFrom%3Ci128%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#384)[§](#associatedtype.Error-48)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#477)[§](#impl-TryFrom%3Ci128%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#477)[§](#associatedtype.Error-49)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-50)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-51)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-52)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#impl-TryFrom%3Ci128%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#401)[§](#associatedtype.Error-53)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#402)[§](#impl-TryFrom%3Ci128%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#402)[§](#associatedtype.Error-54)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#472)[§](#impl-TryFrom%3Ci128%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#472)[§](#associatedtype.Error-55)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#572)[§](#impl-TryFrom%3Ci128%3E-for-NonZero%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#572)[§](#associatedtype.Error-56)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-57)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-58)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#impl-TryFrom%3Cisize%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#466)[§](#associatedtype.Error-59)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#467)[§](#impl-TryFrom%3Cisize%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#467)[§](#associatedtype.Error-60)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#467)[§](#impl-TryFrom%3Cisize%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#467)[§](#associatedtype.Error-61)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-62)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-63)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#impl-TryFrom%3Cisize%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#464)[§](#associatedtype.Error-64)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#465)[§](#impl-TryFrom%3Cisize%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#465)[§](#associatedtype.Error-65)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#465)[§](#impl-TryFrom%3Cisize%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#465)[§](#associatedtype.Error-66)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#406)[§](#impl-TryFrom%3Cisize%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#406)[§](#associatedtype.Error-67)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#573)[§](#impl-TryFrom%3Cisize%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#573)[§](#associatedtype.Error-68)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu8%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-69)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#387)[§](#impl-TryFrom%3Cu8%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#387)[§](#associatedtype.Error-70)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#562)[§](#impl-TryFrom%3Cu8%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#562)[§](#associatedtype.Error-71)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu16%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-72)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#388)[§](#impl-TryFrom%3Cu16%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#388)[§](#associatedtype.Error-73)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#388)[§](#impl-TryFrom%3Cu16%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#388)[§](#associatedtype.Error-74)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#474)[§](#impl-TryFrom%3Cu16%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#474)[§](#associatedtype.Error-75)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#375)[§](#impl-TryFrom%3Cu16%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#375)[§](#associatedtype.Error-76)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#563)[§](#impl-TryFrom%3Cu16%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#563)[§](#associatedtype.Error-77)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu32%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-78)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#303)[§](#impl-TryFrom%3Cu32%3E-for-char)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#304)[§](#associatedtype.Error-79)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#impl-TryFrom%3Cu32%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#associatedtype.Error-80)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#impl-TryFrom%3Cu32%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#associatedtype.Error-81)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#impl-TryFrom%3Cu32%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#389)[§](#associatedtype.Error-82)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#474)[§](#impl-TryFrom%3Cu32%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#474)[§](#associatedtype.Error-83)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#impl-TryFrom%3Cu32%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#associatedtype.Error-84)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#impl-TryFrom%3Cu32%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#376)[§](#associatedtype.Error-85)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#469)[§](#impl-TryFrom%3Cu32%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#469)[§](#associatedtype.Error-86)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#564)[§](#impl-TryFrom%3Cu32%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#564)[§](#associatedtype.Error-87)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu64%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-88)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#impl-TryFrom%3Cu64%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#associatedtype.Error-89)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#impl-TryFrom%3Cu64%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#associatedtype.Error-90)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#impl-TryFrom%3Cu64%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#associatedtype.Error-91)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#impl-TryFrom%3Cu64%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#390)[§](#associatedtype.Error-92)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#475)[§](#impl-TryFrom%3Cu64%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#475)[§](#associatedtype.Error-93)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#impl-TryFrom%3Cu64%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#associatedtype.Error-94)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#impl-TryFrom%3Cu64%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#associatedtype.Error-95)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#impl-TryFrom%3Cu64%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#377)[§](#associatedtype.Error-96)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#469)[§](#impl-TryFrom%3Cu64%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#469)[§](#associatedtype.Error-97)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#565)[§](#impl-TryFrom%3Cu64%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#565)[§](#associatedtype.Error-98)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu128%3E-for-bool)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-99)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-100)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-101)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-102)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-103)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#impl-TryFrom%3Cu128%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#391)[§](#associatedtype.Error-104)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#475)[§](#impl-TryFrom%3Cu128%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#475)[§](#associatedtype.Error-105)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-106)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-107)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-108)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#impl-TryFrom%3Cu128%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#378)[§](#associatedtype.Error-109)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#470)[§](#impl-TryFrom%3Cu128%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#470)[§](#associatedtype.Error-110)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#566)[§](#impl-TryFrom%3Cu128%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#566)[§](#associatedtype.Error-111)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#impl-TryFrom%3Cusize%3E-for-i8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#associatedtype.Error-112)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#impl-TryFrom%3Cusize%3E-for-i16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#associatedtype.Error-113)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#impl-TryFrom%3Cusize%3E-for-i32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#associatedtype.Error-114)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#impl-TryFrom%3Cusize%3E-for-i64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#461)[§](#associatedtype.Error-115)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#462)[§](#impl-TryFrom%3Cusize%3E-for-i128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#462)[§](#associatedtype.Error-116)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#405)[§](#impl-TryFrom%3Cusize%3E-for-isize)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#405)[§](#associatedtype.Error-117)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#impl-TryFrom%3Cusize%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#associatedtype.Error-118)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#impl-TryFrom%3Cusize%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#associatedtype.Error-119)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#impl-TryFrom%3Cusize%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#459)[§](#associatedtype.Error-120)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#460)[§](#impl-TryFrom%3Cusize%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#460)[§](#associatedtype.Error-121)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#460)[§](#impl-TryFrom%3Cusize%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#460)[§](#associatedtype.Error-122)

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#567)[§](#impl-TryFrom%3Cusize%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#567)[§](#associatedtype.Error-123)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#266)[§](#impl-TryFrom%3Cusize%3E-for-Alignment)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#267)[§](#associatedtype.Error-124)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#567)[§](#impl-TryFrom%3CByteString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#568)[§](#associatedtype.Error-125)

1.85.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#841)[§](#impl-TryFrom%3CCString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#842)[§](#associatedtype.Error-126)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-127)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-128)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-129)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-130)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-131)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#impl-TryFrom%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#618)[§](#associatedtype.Error-132)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#603)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#603)[§](#associatedtype.Error-133)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-134)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-135)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-136)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-137)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-138)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#impl-TryFrom%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#619)[§](#associatedtype.Error-139)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#associatedtype.Error-140)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#associatedtype.Error-141)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#604)[§](#associatedtype.Error-142)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-143)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-144)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-145)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-146)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-147)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#impl-TryFrom%3CNonZero%3Ci32%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#620)[§](#associatedtype.Error-148)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#associatedtype.Error-149)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#associatedtype.Error-150)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#associatedtype.Error-151)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#605)[§](#associatedtype.Error-152)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-153)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-154)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-155)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-156)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-157)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#impl-TryFrom%3CNonZero%3Ci64%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#621)[§](#associatedtype.Error-158)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#associatedtype.Error-159)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#associatedtype.Error-160)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#associatedtype.Error-161)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#associatedtype.Error-162)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#606)[§](#associatedtype.Error-163)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-164)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-165)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-166)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-167)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-168)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#impl-TryFrom%3CNonZero%3Ci128%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#622)[§](#associatedtype.Error-169)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#associatedtype.Error-170)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#associatedtype.Error-171)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#associatedtype.Error-172)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#associatedtype.Error-173)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#607)[§](#associatedtype.Error-174)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-175)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-176)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-177)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-178)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-179)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#impl-TryFrom%3CNonZero%3Cisize%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#623)[§](#associatedtype.Error-180)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#610)[§](#impl-TryFrom%3CNonZero%3Cu8%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#610)[§](#associatedtype.Error-181)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#impl-TryFrom%3CNonZero%3Cu16%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#associatedtype.Error-182)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#impl-TryFrom%3CNonZero%3Cu16%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#associatedtype.Error-183)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#impl-TryFrom%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#611)[§](#associatedtype.Error-184)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#596)[§](#impl-TryFrom%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#596)[§](#associatedtype.Error-185)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#associatedtype.Error-186)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#associatedtype.Error-187)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#associatedtype.Error-188)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#612)[§](#associatedtype.Error-189)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#associatedtype.Error-190)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#associatedtype.Error-191)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#impl-TryFrom%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#597)[§](#associatedtype.Error-192)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#associatedtype.Error-193)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#associatedtype.Error-194)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#associatedtype.Error-195)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#associatedtype.Error-196)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#613)[§](#associatedtype.Error-197)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#associatedtype.Error-198)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#associatedtype.Error-199)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#associatedtype.Error-200)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#impl-TryFrom%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#598)[§](#associatedtype.Error-201)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-202)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-203)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-204)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-205)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-206)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#614)[§](#associatedtype.Error-207)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#associatedtype.Error-208)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#associatedtype.Error-209)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#associatedtype.Error-210)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#associatedtype.Error-211)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#impl-TryFrom%3CNonZero%3Cu128%3E%3E-for-NonZero%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#599)[§](#associatedtype.Error-212)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Ci8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-213)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Ci16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-214)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Ci32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-215)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Ci64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-216)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Ci128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-217)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cisize%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#615)[§](#associatedtype.Error-218)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#associatedtype.Error-219)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cu16%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#associatedtype.Error-220)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cu32%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#associatedtype.Error-221)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cu64%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#associatedtype.Error-222)

1.49.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#600)[§](#associatedtype.Error-223)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#255)[§](#impl-TryFrom%3CNonZero%3Cusize%3E%3E-for-Alignment)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#256)[§](#associatedtype.Error-224)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#234-247)[§](#impl-TryFrom%3CHandleOrInvalid%3E-for-OwnedHandle)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#235)[§](#associatedtype.Error-225)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#156-169)[§](#impl-TryFrom%3CHandleOrNull%3E-for-OwnedHandle)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#157)[§](#associatedtype.Error-226)

1.87.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3323)[§](#impl-TryFrom%3CVec%3Cu8%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3324)[§](#associatedtype.Error-227)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#343)[§](#impl-TryFrom%3C%26ByteStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#344)[§](#associatedtype.Error-228)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#671)[§](#impl-TryFrom%3C%26ByteStr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#672)[§](#associatedtype.Error-229)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#577)[§](#impl-TryFrom%3C%26ByteString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#578)[§](#associatedtype.Error-230)

1.72.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1460-1475)[§](#impl-TryFrom%3C%26OsStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1461)[§](#associatedtype.Error-231)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#354)[§](#impl-TryFrom%3C%26mut+ByteStr%3E-for-%26mut+str)

[Source](https://doc.rust-lang.org/src/core/bstr/mod.rs.html#355)[§](#associatedtype.Error-232)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#303)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-%26%5BT;+N%5D)

Tries to create an array ref `&[T; N]` from a slice ref `&[T]`. Succeeds if `slice.len() == N`.

```rust
let bytes: [u8; 3] = [1, 0, 2];

let bytes_head: &[u8; 2] = <&[u8; 2]>::try_from(&bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(*bytes_head));

let bytes_tail: &[u8; 2] = bytes[1..3].try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(*bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#304)[§](#associatedtype.Error-233)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#326)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-%26mut+%5BT;+N%5D)

Tries to create a mutable array ref `&mut [T; N]` from a mutable slice ref `&mut [T]`. Succeeds if `slice.len() == N`.

```rust
let mut bytes: [u8; 3] = [1, 0, 2];

let bytes_head: &mut [u8; 2] = <&mut [u8; 2]>::try_from(&mut bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(*bytes_head));

let bytes_tail: &mut [u8; 2] = (&mut bytes[1..3]).try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(*bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#327)[§](#associatedtype.Error-234)

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3048)[§](#impl-TryFrom%3CRc%3C%5BT%5D,+A%3E%3E-for-Rc%3C%5BT;+N%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3049)[§](#associatedtype.Error-235)

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4082)[§](#impl-TryFrom%3CArc%3C%5BT%5D,+A%3E%3E-for-Arc%3C%5BT;+N%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4083)[§](#associatedtype.Error-236)

1.48.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4437)[§](#impl-TryFrom%3CVec%3CT,+A%3E%3E-for-%5BT;+N%5D)

[Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4438)[§](#associatedtype.Error-237)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#827-829)[§](#impl-TryFrom%3CU%3E-for-T)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#831)[§](#associatedtype.Error-238)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#251-253)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-%5BT;+N%5D)

Tries to create an array `[T; N]` by copying from a slice `&[T]`. Succeeds if `slice.len() == N`.

```rust
let bytes: [u8; 3] = [1, 0, 2];

let bytes_head: [u8; 2] = <[u8; 2]>::try_from(&bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(bytes_head));

let bytes_tail: [u8; 2] = bytes[1..3].try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#255)[§](#associatedtype.Error-239)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1038-1040)[§](#impl-TryFrom%3C%26%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1042)[§](#associatedtype.Error-240)

1.59.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#277-279)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-%5BT;+N%5D)

Tries to create an array `[T; N]` by copying from a mutable slice `&mut [T]`. Succeeds if `slice.len() == N`.

```rust
let mut bytes: [u8; 3] = [1, 0, 2];

let bytes_head: [u8; 2] = <[u8; 2]>::try_from(&mut bytes[0..2]).unwrap();
assert_eq!(1, u16::from_le_bytes(bytes_head));

let bytes_tail: [u8; 2] = (&mut bytes[1..3]).try_into().unwrap();
assert_eq!(512, u16::from_le_bytes(bytes_tail));
```

[Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#281)[§](#associatedtype.Error-241)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1050-1052)[§](#impl-TryFrom%3C%26mut+%5BT%5D%3E-for-Simd%3CT,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1054)[§](#associatedtype.Error-242)

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#259)[§](#impl-TryFrom%3CBox%3C%5BT%5D%3E%3E-for-Box%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#260)[§](#associatedtype.Error-243)

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#282)[§](#impl-TryFrom%3CVec%3CT%3E%3E-for-Box%3C%5BT;+N%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#283)[§](#associatedtype.Error-244)