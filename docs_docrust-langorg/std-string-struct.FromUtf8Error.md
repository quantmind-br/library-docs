---
title: FromUtf8Error in std::string - Rust
url: https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html
source: crawler
fetched_at: 2026-05-06T21:22:11.614333101-03:00
rendered_js: false
word_count: 387
summary: This document describes the FromUtf8Error struct in Rust, which represents an error encountered when converting a byte vector into a String, providing methods to recover the original bytes or inspect the cause of the failure.
tags:
    - rust
    - utf-8
    - error-handling
    - string-conversion
    - memory-allocation
category: reference
---

## Struct FromUtf8Error

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#391)

```rust
pub struct FromUtf8Error { /* private fields */ }
```

Expand description

A possible error value when converting a `String` from a UTF-8 byte vector.

This type is the error type for the [`from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8 "associated function std::string::String::from_utf8") method on [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"). It is designed in such a way to carefully avoid reallocations: the [`into_bytes`](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html#method.into_bytes "method std::string::FromUtf8Error::into_bytes") method will give back the byte vector that was used in the conversion attempt.

The [`Utf8Error`](https://doc.rust-lang.org/std/str/struct.Utf8Error.html "std::str::Utf8Error") type provided by [`std::str`](https://doc.rust-lang.org/core/str/index.html "std::str") represents an error that may occur when converting a slice of [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")s to a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str"). In this sense, it’s an analogue to `FromUtf8Error`, and you can get one from a `FromUtf8Error` through the [`utf8_error`](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html#method.utf8_error "method std::string::FromUtf8Error::utf8_error") method.

## [§](#examples)Examples

```rust
// some invalid bytes, in a vector
let bytes = vec![0, 159];

let value = String::from_utf8(bytes);

assert!(value.is_err());
assert_eq!(vec![0, 159], value.unwrap_err().into_bytes());
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2211)[§](#impl-FromUtf8Error)

1.26.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2226)

Returns a slice of [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")s bytes that were attempted to convert to a `String`.

##### [§](#examples-1)Examples

```rust
// some invalid bytes, in a vector
let bytes = vec![0, 159];

let value = String::from_utf8(bytes);

assert_eq!(&[0, 159], value.unwrap_err().as_bytes());
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2250)

🔬This is a nightly-only experimental API. (`string_from_utf8_lossy_owned` [#129436](https://github.com/rust-lang/rust/issues/129436))

Converts the bytes into a `String` lossily, substituting invalid UTF-8 sequences with replacement characters.

See [`String::from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy "associated function std::string::String::from_utf8_lossy") for more details on replacement of invalid sequences, and [`String::from_utf8_lossy_owned`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy_owned "associated function std::string::String::from_utf8_lossy_owned") for the `String` function which corresponds to this function.

##### [§](#examples-2)Examples

```rust
#![feature(string_from_utf8_lossy_owned)]
// some invalid bytes
let input: Vec<u8> = b"Hello \xF0\x90\x80World".into();
let output = String::from_utf8(input).unwrap_or_else(|e| e.into_utf8_lossy());

assert_eq!(String::from("Hello �World"), output);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2296)

Returns the bytes that were attempted to convert to a `String`.

This method is carefully constructed to avoid allocation. It will consume the error, moving out the bytes, so that a copy of the bytes does not need to be made.

##### [§](#examples-3)Examples

```rust
// some invalid bytes, in a vector
let bytes = vec![0, 159];

let value = String::from_utf8(bytes);

assert_eq!(vec![0, 159], value.unwrap_err().into_bytes());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2323)

Fetch a `Utf8Error` to get more details about the conversion failure.

The [`Utf8Error`](https://doc.rust-lang.org/std/str/struct.Utf8Error.html "struct std::str::Utf8Error") type provided by [`std::str`](https://doc.rust-lang.org/core/str/index.html "std::str") represents an error that may occur when converting a slice of [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")s to a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str"). In this sense, it’s an analogue to `FromUtf8Error`. See its documentation for more details on using it.

##### [§](#examples-4)Examples

```rust
// some invalid bytes, in a vector
let bytes = vec![0, 159];

let error = String::from_utf8(bytes).unwrap_err().utf8_error();

// the first byte is invalid here
assert_eq!(1, error.valid_up_to());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#389)[§](#impl-Clone-for-FromUtf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#390)[§](#impl-Debug-for-FromUtf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2329)[§](#impl-Display-for-FromUtf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2343)[§](#impl-Error-for-FromUtf8Error)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#390)[§](#impl-PartialEq-for-FromUtf8Error)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#390)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#390)[§](#impl-Eq-for-FromUtf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#390)[§](#impl-StructuralPartialEq-for-FromUtf8Error)

[§](#impl-Freeze-for-FromUtf8Error)

[§](#impl-RefUnwindSafe-for-FromUtf8Error)

[§](#impl-Send-for-FromUtf8Error)

[§](#impl-Sync-for-FromUtf8Error)

[§](#impl-Unpin-for-FromUtf8Error)

[§](#impl-UnsafeUnpin-for-FromUtf8Error)

[§](#impl-UnwindSafe-for-FromUtf8Error)