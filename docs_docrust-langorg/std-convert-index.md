---
title: std::convert - Rust
url: https://doc.rust-lang.org/std/convert/index.html
source: crawler
fetched_at: 2026-05-06T21:24:46.257211519-03:00
rendered_js: false
word_count: 364
summary: This document outlines the standard library traits used for type conversion in Rust, providing mechanisms for reference, value, and fallible transformations. It explains the relationship between reciprocal traits like From and Into to help developers implement efficient type interoperability.
tags:
    - rust
    - type-conversion
    - traits
    - generic-programming
    - data-transformation
    - api-reference
category: reference
---

## Module convert

1.0.0 · [Source](https://doc.rust-lang.org/src/core/lib.rs.html#274)

Expand description

Traits for conversions between types.

The traits in this module provide a way to convert from one type to another type. Each trait serves a different purpose:

- Implement the [`AsRef`](https://doc.rust-lang.org/std/convert/trait.AsRef.html "trait std::convert::AsRef") trait for cheap reference-to-reference conversions
- Implement the [`AsMut`](https://doc.rust-lang.org/std/convert/trait.AsMut.html "trait std::convert::AsMut") trait for cheap mutable-to-mutable conversions
- Implement the [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") trait for consuming value-to-value conversions
- Implement the [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into") trait for consuming value-to-value conversions to types outside the current crate
- The [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") and [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") traits behave like [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") and [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into"), but should be implemented when the conversion can fail.

The traits in this module are often used as trait bounds for generic functions such that to arguments of multiple types are supported. See the documentation of each trait for examples.

As a library author, you should always prefer implementing [`From<T>`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") or [`TryFrom<T>`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") rather than [`Into<U>`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into") or [`TryInto<U>`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto"), as [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") and [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") provide greater flexibility and offer equivalent [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into") or [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") implementations for free, thanks to a blanket implementation in the standard library. When targeting a version prior to Rust 1.41, it may be necessary to implement [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into") or [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") directly when converting to a type outside the current crate.

## [§](#generic-implementations)Generic Implementations

- [`AsRef`](https://doc.rust-lang.org/std/convert/trait.AsRef.html "trait std::convert::AsRef") and [`AsMut`](https://doc.rust-lang.org/std/convert/trait.AsMut.html "trait std::convert::AsMut") auto-dereference if the inner type is a reference (but not generally for all [dereferenceable types](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref"))
- [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From")`<U> for T` implies [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into")`<T> for U`
- [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")`<U> for T` implies [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto")`<T> for U`
- [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") and [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into") are reflexive, which means that all types can `into` themselves and `from` themselves

See each trait for usage examples.

[Infallible](https://doc.rust-lang.org/std/convert/enum.Infallible.html "enum std::convert::Infallible")

The error type for errors that can never happen.

[AsMut](https://doc.rust-lang.org/std/convert/trait.AsMut.html "trait std::convert::AsMut")

Used to do a cheap mutable-to-mutable reference conversion.

[AsRef](https://doc.rust-lang.org/std/convert/trait.AsRef.html "trait std::convert::AsRef")

Used to do a cheap reference-to-reference conversion.

[From](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From")

Used to do value-to-value conversions while consuming the input value. It is the reciprocal of [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into").

[Into](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into")

A value-to-value conversion that consumes the input value. The opposite of [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From").

[TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")

Simple and safe type conversions that may fail in a controlled way under some circumstances. It is the reciprocal of [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto").

[TryInto](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto")

An attempted conversion that consumes `self`, which may or may not be expensive.

[FloatToInt](https://doc.rust-lang.org/std/convert/trait.FloatToInt.html "trait std::convert::FloatToInt")Experimental

Supporting trait for inherent methods of `f32` and `f64` such as `to_int_unchecked`. Typically doesn’t need to be used directly.

[identity](https://doc.rust-lang.org/std/convert/fn.identity.html "fn std::convert::identity")

The identity function.