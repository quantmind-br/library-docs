---
title: Utf8Error in std::str - Rust
url: https://doc.rust-lang.org/std/str/struct.Utf8Error.html
source: crawler
fetched_at: 2026-05-06T21:23:59.164295162-03:00
rendered_js: false
word_count: 325
summary: Describes the Utf8Error struct in Rust, which represents errors encountered during the validation of byte sequences as UTF-8 encoded strings.
tags:
    - rust
    - utf8
    - error-handling
    - string-decoding
    - byte-validation
    - standard-library
category: reference
---

## Struct Utf8Error

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#47)

```rust
pub struct Utf8Error { /* private fields */ }
```

Expand description

Errors which can occur when attempting to interpret a sequence of [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8") as a string.

As such, the `from_utf8` family of functions and methods for both [`String`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8)s and [`&str`](https://doc.rust-lang.org/std/str/fn.from_utf8.html "fn std::str::from_utf8")s make use of this error, for example.

## [§](#examples)Examples

This error type’s methods can be used to create functionality similar to `String::from_utf8_lossy` without allocating heap memory:

```rust
fn from_utf8_lossy<F>(mut input: &[u8], mut push: F) where F: FnMut(&str) {
    loop {
        match std::str::from_utf8(input) {
            Ok(valid) => {
                push(valid);
                break
            }
            Err(error) => {
                let (valid, after_valid) = input.split_at(error.valid_up_to());
                unsafe {
                    push(std::str::from_utf8_unchecked(valid))
                }
                push("\u{FFFD}");

                if let Some(invalid_sequence_length) = error.error_len() {
                    input = &after_valid[invalid_sequence_length..]
                } else {
                    break
                }
            }
        }
    }
}
```

[Source](https://doc.rust-lang.org/src/core/str/error.rs.html#52)[§](#impl-Utf8Error)

1.5.0 (const: 1.63.0) · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#79)

Returns the index in the given string up to which valid UTF-8 was verified.

It is the maximum index such that `from_utf8(&input[..index])` would return `Ok(_)`.

##### [§](#examples-1)Examples

Basic usage:

```rust
use std::str;

// some invalid bytes, in a vector
let sparkle_heart = vec![0, 159, 146, 150];

// std::str::from_utf8 returns a Utf8Error
let error = str::from_utf8(&sparkle_heart).unwrap_err();

// the second byte is invalid here
assert_eq!(1, error.valid_up_to());
```

1.20.0 (const: 1.63.0) · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#102)

Provides more information about the failure:

- `None`: the end of the input was reached unexpectedly. `self.valid_up_to()` is 1 to 3 bytes from the end of the input. If a byte stream (such as a file or a network socket) is being decoded incrementally, this could be a valid `char` whose UTF-8 byte sequence is spanning multiple chunks.
- `Some(len)`: an unexpected byte was encountered. The length provided is that of the invalid byte sequence that starts at the index given by `valid_up_to()`. Decoding should resume after that sequence (after inserting a [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html)) in case of lossy decoding.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-Clone-for-Utf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-Debug-for-Utf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#112)[§](#impl-Display-for-Utf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#127)[§](#impl-Error-for-Utf8Error)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-PartialEq-for-Utf8Error)

[Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-Copy-for-Utf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-Eq-for-Utf8Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/error.rs.html#45)[§](#impl-StructuralPartialEq-for-Utf8Error)

[§](#impl-Freeze-for-Utf8Error)

[§](#impl-RefUnwindSafe-for-Utf8Error)

[§](#impl-Send-for-Utf8Error)

[§](#impl-Sync-for-Utf8Error)

[§](#impl-Unpin-for-Utf8Error)

[§](#impl-UnsafeUnpin-for-Utf8Error)

[§](#impl-UnwindSafe-for-Utf8Error)