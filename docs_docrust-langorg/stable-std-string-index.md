---
title: std::string - Rust
url: https://doc.rust-lang.org/stable/std/string/index.html
source: crawler
fetched_at: 2026-05-06T21:25:38.74854503-03:00
rendered_js: false
word_count: 185
summary: This module documents the UTF-8 encoded, growable String type and associated traits, iterators, and error types within the Rust standard library.
tags:
    - rust-language
    - string-manipulation
    - utf-8
    - standard-library
    - data-types
category: reference
---

## Module string

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/lib.rs.html#232)

Expand description

A UTF-8–encoded, growable string.

This module contains the [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") type, the [`ToString`](https://doc.rust-lang.org/stable/std/string/trait.ToString.html "trait std::string::ToString") trait for converting to strings, and several error types that may result from working with [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String")s.

## [§](#examples)Examples

There are multiple ways to create a new [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") from a string literal:

```rust
let s = "Hello".to_string();

let s = String::from("world");
let s: String = "also this".into();
```

You can create a new [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") from an existing one by concatenating with `+`:

```rust
let s = "Hello".to_string();

let message = s + " world!";
```

If you have a vector of valid UTF-8 bytes, you can make a [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") out of it. You can do the reverse too.

```rust
let sparkle_heart = vec![240, 159, 146, 150];

// We know these bytes are valid, so we'll use `unwrap()`.
let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);

let bytes = sparkle_heart.into_bytes();

assert_eq!(bytes, [240, 159, 146, 150]);
```

[Drain](https://doc.rust-lang.org/stable/std/string/struct.Drain.html "struct std::string::Drain")

A draining iterator for `String`.

[FromUtf8Error](https://doc.rust-lang.org/stable/std/string/struct.FromUtf8Error.html "struct std::string::FromUtf8Error")

A possible error value when converting a `String` from a UTF-8 byte vector.

[FromUtf16Error](https://doc.rust-lang.org/stable/std/string/struct.FromUtf16Error.html "struct std::string::FromUtf16Error")

A possible error value when converting a `String` from a UTF-16 byte slice.

[String](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String")

A UTF-8–encoded, growable string.

[IntoChars](https://doc.rust-lang.org/stable/std/string/struct.IntoChars.html "struct std::string::IntoChars")Experimental

An iterator over the [`char`](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char")s of a string.

[ToString](https://doc.rust-lang.org/stable/std/string/trait.ToString.html "trait std::string::ToString")

A trait for converting a value to a `String`.

[ParseError](https://doc.rust-lang.org/stable/std/string/type.ParseError.html "type std::string::ParseError")

A type alias for [`Infallible`](https://doc.rust-lang.org/stable/std/convert/enum.Infallible.html "convert::Infallible").