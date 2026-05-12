---
title: IntoStringError in std::ffi - Rust
url: https://doc.rust-lang.org/std/ffi/struct.IntoStringError.html
source: crawler
fetched_at: 2026-05-06T21:23:58.700813567-03:00
rendered_js: false
word_count: 207
summary: The IntoStringError struct represents an error that occurs when a CString fails to convert into a Rust String due to invalid UTF-8 byte sequences.
tags:
    - rust
    - ffi
    - error-handling
    - utf-8
    - cstring
    - string-conversion
category: reference
---

## Struct IntoStringError

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#223)

```rust
pub struct IntoStringError { /* private fields */ }
```

Expand description

An error indicating invalid UTF-8 when converting a [`CString`](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString") into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

`CString` is just a wrapper over a buffer of bytes with a nul terminator; [`CString::into_string`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_string "method std::ffi::CString::into_string") performs UTF-8 validation on those bytes and may return this error.

This `struct` is created by [`CString::into_string()`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_string "method std::ffi::CString::into_string"). See its documentation for more.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1043)[§](#impl-IntoStringError)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1048)

Consumes this error, returning original [`CString`](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString") which generated the error.

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1055)

Access the underlying UTF-8 error that was the cause of this error.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#impl-Clone-for-IntoStringError)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#impl-Debug-for-IntoStringError)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1061)[§](#impl-Display-for-IntoStringError)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1289)[§](#impl-Error-for-IntoStringError)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1290)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#impl-PartialEq-for-IntoStringError)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#impl-Eq-for-IntoStringError)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#221)[§](#impl-StructuralPartialEq-for-IntoStringError)

[§](#impl-Freeze-for-IntoStringError)

[§](#impl-RefUnwindSafe-for-IntoStringError)

[§](#impl-Send-for-IntoStringError)

[§](#impl-Sync-for-IntoStringError)

[§](#impl-Unpin-for-IntoStringError)

[§](#impl-UnsafeUnpin-for-IntoStringError)

[§](#impl-UnwindSafe-for-IntoStringError)