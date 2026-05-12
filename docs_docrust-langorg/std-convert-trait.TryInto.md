---
title: TryInto in std::convert - Rust
url: https://doc.rust-lang.org/std/convert/trait.TryInto.html#tymethod.try_into
source: crawler
fetched_at: 2026-05-06T21:24:14.926989177-03:00
rendered_js: false
word_count: 154
summary: This document defines the TryInto trait in Rust, which facilitates fallible type conversions that consume the source value. It provides guidance on when to prefer implementing TryFrom versus TryInto and clarifies its usage within generic trait bounds.
tags:
    - rust
    - trait
    - type-conversion
    - fallible-conversion
    - generics
category: reference
---

## Trait TryInto

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#615)

```rust
pub trait TryInto<T>: Sized {
    type Error;

    // Required method
    fn try_into(self) -> Result<T, Self::Error>;
}
```

Expand description

An attempted conversion that consumes `self`, which may or may not be expensive.

Library authors should usually not directly implement this trait, but should prefer implementing the [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") trait, which offers greater flexibility and provides an equivalent `TryInto` implementation for free, thanks to a blanket implementation in the standard library. For more information on this, see the documentation for [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into").

Prefer using [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") over [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") when specifying trait bounds on a generic function to ensure that types that only implement [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto") can be used as well.

## [§](#implementing-tryinto)Implementing `TryInto`

This suffers the same restrictions and reasoning as implementing [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into"), see there for details.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#618)

The type returned in the event of a conversion error.

1.34.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#622)

Performs the conversion.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*