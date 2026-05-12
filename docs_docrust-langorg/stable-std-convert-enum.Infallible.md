---
title: Infallible in std::convert - Rust
url: https://doc.rust-lang.org/stable/std/convert/enum.Infallible.html
source: crawler
fetched_at: 2026-05-06T21:26:00.844761648-03:00
rendered_js: false
word_count: 516
summary: The Infallible enum in Rust is a specialized type representing errors that can never occur, commonly used as a placeholder in generic APIs that return a Result.
tags:
    - rust
    - error-handling
    - enum
    - type-system
    - generic-api
category: reference
---

## Enum Infallible

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#930)

```rust
pub enum Infallible {}
```

Expand description

The error type for errors that can never happen.

Since this enum has no variant, a value of this type can never actually exist. This can be useful for generic APIs that use [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") and parameterize the error type, to indicate that the result is always [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok").

For example, the [`TryFrom`](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom") trait (conversion that returns a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")) has a blanket implementation for all types where a reverse [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") implementation exists.

[ⓘ](# "This example is not tested")

```rust
impl<T, U> TryFrom<U> for T where U: Into<T> {
    type Error = Infallible;

    fn try_from(value: U) -> Result<Self, Infallible> {
        Ok(U::into(value))  // Never returns `Err`
    }
}
```

## [§](#future-compatibility)Future compatibility

This enum has the same role as [the `!` “never” type](https://doc.rust-lang.org/stable/std/primitive.never.html "primitive never"), which is unstable in this version of Rust. When `!` is stabilized, we plan to make `Infallible` a type alias to it:

[ⓘ](# "This example is not tested")

```rust
pub type Infallible = !;
```

… and eventually deprecate `Infallible`.

However there is one case where `!` syntax can be used before `!` is stabilized as a full-fledged type: in the position of a function’s return type. Specifically, it is possible to have implementations for two different function pointer types:

```rust
trait MyTrait {}
impl MyTrait for fn() -> ! {}
impl MyTrait for fn() -> std::convert::Infallible {}
```

With `Infallible` being an enum, this code is valid. However when `Infallible` becomes an alias for the never type, the two `impl`s will start to overlap and therefore will be disallowed by the language’s trait coherence rules.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#934)[§](#impl-Clone-for-Infallible)

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#941)[§](#impl-Debug-for-Infallible)

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#948)[§](#impl-Display-for-Infallible)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#955)[§](#impl-Error-for-Infallible)

1.30.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/stable/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/stable/std/error/trait.Error.html#method.provide)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#987)[§](#impl-From%3C!%3E-for-Infallible)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#989)[§](#method.from-1)

Converts to this type from the input type.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/num/error.rs.html#24)[§](#impl-From%3CInfallible%3E-for-TryFromIntError)

[Source](https://doc.rust-lang.org/stable/src/core/num/error.rs.html#25)[§](#method.from)

Converts to this type from the input type.

1.36.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/array/mod.rs.html#197)[§](#impl-From%3CInfallible%3E-for-TryFromSliceError)

[Source](https://doc.rust-lang.org/stable/src/core/array/mod.rs.html#198)[§](#method.from-2)

Converts to this type from the input type.

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#995)[§](#impl-Hash-for-Infallible)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#979)[§](#impl-Ord-for-Infallible)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#959)[§](#impl-PartialEq-for-Infallible)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#960)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#971)[§](#impl-PartialOrd-for-Infallible)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#972)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.61.0 · [Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2594-2598)[§](#impl-Termination-for-Infallible)

[Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2595-2597)[§](#method.report)

Is called to get the representation of the value as status code. This status code is returned to the operating system.

1.34.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#929)[§](#impl-Copy-for-Infallible)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#967)[§](#impl-Eq-for-Infallible)

[§](#impl-Freeze-for-Infallible)

[§](#impl-RefUnwindSafe-for-Infallible)

[§](#impl-Send-for-Infallible)

[§](#impl-Sync-for-Infallible)

[§](#impl-Unpin-for-Infallible)

[§](#impl-UnsafeUnpin-for-Infallible)

[§](#impl-UnwindSafe-for-Infallible)