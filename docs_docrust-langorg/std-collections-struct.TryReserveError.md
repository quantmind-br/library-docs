---
title: TryReserveError in std::collections - Rust
url: https://doc.rust-lang.org/std/collections/struct.TryReserveError.html
source: crawler
fetched_at: 2026-05-06T21:22:09.860249641-03:00
rendered_js: false
word_count: 191
summary: Defines the error type returned by collection try_reserve methods when an allocation failure occurs in Rust.
tags:
    - rust
    - memory-allocation
    - error-handling
    - api-reference
    - collections
category: reference
---

## Struct TryReserveError

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#70)

```rust
pub struct TryReserveError { /* private fields */ }
```

Expand description

The error type for `try_reserve` methods.

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#78)[§](#impl-TryReserveError)

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#88)

🔬This is a nightly-only experimental API. (`try_reserve_kind` [#48043](https://github.com/rust-lang/rust/issues/48043))

Details about the allocation that caused the error

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#impl-Clone-for-TryReserveError)

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#impl-Debug-for-TryReserveError)

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#172)[§](#impl-Display-for-TryReserveError)

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#200)[§](#impl-Error-for-TryReserveError)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.78.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#119-128)[§](#impl-From%3CTryReserveError%3E-for-Error)

[Source](https://doc.rust-lang.org/src/std/io/error.rs.html#124-127)[§](#method.from-1)

Converts `TryReserveError` to an error with [`ErrorKind::OutOfMemory`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.OutOfMemory "variant std::io::ErrorKind::OutOfMemory").

`TryReserveError` won’t be available as the error `source()`, but this may change in the future.

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#152)[§](#impl-From%3CTryReserveErrorKind%3E-for-TryReserveError)

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#154)[§](#method.from)

Converts to this type from the input type.

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#impl-PartialEq-for-TryReserveError)

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#impl-Eq-for-TryReserveError)

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#67)[§](#impl-StructuralPartialEq-for-TryReserveError)

[§](#impl-Freeze-for-TryReserveError)

[§](#impl-RefUnwindSafe-for-TryReserveError)

[§](#impl-Send-for-TryReserveError)

[§](#impl-Sync-for-TryReserveError)

[§](#impl-Unpin-for-TryReserveError)

[§](#impl-UnsafeUnpin-for-TryReserveError)

[§](#impl-UnwindSafe-for-TryReserveError)