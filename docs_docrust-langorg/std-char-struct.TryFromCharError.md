---
title: TryFromCharError in std::char - Rust
url: https://doc.rust-lang.org/std/char/struct.TryFromCharError.html
source: crawler
fetched_at: 2026-05-06T21:29:30.71448744-03:00
rendered_js: false
word_count: 144
summary: This document provides the reference documentation for the TryFromCharError struct in Rust, which represents the error returned when a character conversion fails.
tags:
    - rust
    - error-handling
    - char-conversion
    - standard-library
category: reference
---

## Struct TryFromCharError

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#595)

```rust
pub struct TryFromCharError(/* private fields */);
```

Expand description

The error type returned when a checked char conversion fails.

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-Clone-for-TryFromCharError)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-Debug-for-TryFromCharError)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#598)[§](#impl-Display-for-TryFromCharError)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#605)[§](#impl-Error-for-TryFromCharError)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-PartialEq-for-TryFromCharError)

[Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-Copy-for-TryFromCharError)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-Eq-for-TryFromCharError)

1.59.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#594)[§](#impl-StructuralPartialEq-for-TryFromCharError)

[§](#impl-Freeze-for-TryFromCharError)

[§](#impl-RefUnwindSafe-for-TryFromCharError)

[§](#impl-Send-for-TryFromCharError)

[§](#impl-Sync-for-TryFromCharError)

[§](#impl-Unpin-for-TryFromCharError)

[§](#impl-UnsafeUnpin-for-TryFromCharError)

[§](#impl-UnwindSafe-for-TryFromCharError)