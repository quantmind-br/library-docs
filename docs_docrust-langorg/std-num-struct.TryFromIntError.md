---
title: TryFromIntError in std::num - Rust
url: https://doc.rust-lang.org/std/num/struct.TryFromIntError.html
source: crawler
fetched_at: 2026-05-06T21:30:35.671601674-03:00
rendered_js: false
word_count: 169
summary: This document defines the TryFromIntError struct in Rust, which represents an error that occurs during failed checked integer conversions.
tags:
    - rust
    - error-handling
    - integer-conversion
    - primitive-types
    - standard-library
category: reference
---

## Struct TryFromIntError

1.0.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#10)

```rust
pub struct TryFromIntError(/* private fields */);
```

Expand description

The error type returned when a checked integral type conversion fails.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-Clone-for-TryFromIntError)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-Debug-for-TryFromIntError)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#13)[§](#impl-Display-for-TryFromIntError)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#20)[§](#impl-Error-for-TryFromIntError)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

[Source](https://doc.rust-lang.org/src/core/num/error.rs.html#32)[§](#impl-From%3C!%3E-for-TryFromIntError)

[Source](https://doc.rust-lang.org/src/core/num/error.rs.html#34)[§](#method.from-1)

Converts to this type from the input type.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#24)[§](#impl-From%3CInfallible%3E-for-TryFromIntError)

[Source](https://doc.rust-lang.org/src/core/num/error.rs.html#25)[§](#method.from)

Converts to this type from the input type.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-PartialEq-for-TryFromIntError)

[Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-Copy-for-TryFromIntError)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-Eq-for-TryFromIntError)

1.34.0 · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#9)[§](#impl-StructuralPartialEq-for-TryFromIntError)

[§](#impl-Freeze-for-TryFromIntError)

[§](#impl-RefUnwindSafe-for-TryFromIntError)

[§](#impl-Send-for-TryFromIntError)

[§](#impl-Sync-for-TryFromIntError)

[§](#impl-Unpin-for-TryFromIntError)

[§](#impl-UnsafeUnpin-for-TryFromIntError)

[§](#impl-UnwindSafe-for-TryFromIntError)