---
title: FromUtf16Error in std::string - Rust
url: https://doc.rust-lang.org/std/string/struct.FromUtf16Error.html
source: crawler
fetched_at: 2026-05-06T21:22:13.117792804-03:00
rendered_js: false
word_count: 108
summary: This document defines the FromUtf16Error struct, which represents an error encountered during the conversion of a UTF-16 byte slice into a Rust String.
tags:
    - rust
    - utf-16
    - error-handling
    - string-conversion
    - standard-library
category: reference
---

## Struct FromUtf16Error

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#413)

```rust
pub struct FromUtf16Error(/* private fields */);
```

Expand description

A possible error value when converting a `String` from a UTF-16 byte slice.

This type is the error type for the [`from_utf16`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf16 "associated function std::string::String::from_utf16") method on [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

## [§](#examples)Examples

```rust
// 𝄞mu<invalid>ic
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0xD800, 0x0069, 0x0063];

assert!(String::from_utf16(v).is_err());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#412)[§](#impl-Debug-for-FromUtf16Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2336)[§](#impl-Display-for-FromUtf16Error)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2346)[§](#impl-Error-for-FromUtf16Error)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

[§](#impl-Freeze-for-FromUtf16Error)

[§](#impl-RefUnwindSafe-for-FromUtf16Error)

[§](#impl-Send-for-FromUtf16Error)

[§](#impl-Sync-for-FromUtf16Error)

[§](#impl-Unpin-for-FromUtf16Error)

[§](#impl-UnsafeUnpin-for-FromUtf16Error)

[§](#impl-UnwindSafe-for-FromUtf16Error)