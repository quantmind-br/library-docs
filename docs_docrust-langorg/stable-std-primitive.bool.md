---
title: bool - Rust
url: https://doc.rust-lang.org/stable/std/primitive.bool.html
source: crawler
fetched_at: 2026-05-06T21:25:43.620917236-03:00
rendered_js: false
word_count: 1782
summary: This document provides the reference documentation for the Rust primitive boolean type, detailing its usage, associated traits, and available methods.
tags:
    - rust
    - primitive-types
    - boolean
    - api-reference
    - language-features
category: reference
---

## Primitive Type bool

1.0.0

Expand description

The boolean type.

The `bool` represents a value, which could only be either [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html) or [`false`](https://doc.rust-lang.org/stable/std/keyword.false.html). If you cast a `bool` into an integer, [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html) will be 1 and [`false`](https://doc.rust-lang.org/stable/std/keyword.false.html) will be 0.

## [§](#basic-usage)Basic usage

`bool` implements various traits, such as [`BitAnd`](https://doc.rust-lang.org/stable/std/ops/trait.BitAnd.html "trait std::ops::BitAnd"), [`BitOr`](https://doc.rust-lang.org/stable/std/ops/trait.BitOr.html "trait std::ops::BitOr"), [`Not`](https://doc.rust-lang.org/stable/std/ops/trait.Not.html "trait std::ops::Not"), etc., which allow us to perform boolean operations using `&`, `|` and `!`.

[`if`](https://doc.rust-lang.org/stable/std/keyword.if.html) requires a `bool` value as its conditional. [`assert!`](https://doc.rust-lang.org/stable/std/macro.assert.html "macro std::assert"), which is an important macro in testing, checks whether an expression is [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html) and panics if it isn’t.

```rust
let bool_val = true & false | false;
assert!(!bool_val);
```

## [§](#examples)Examples

A trivial example of the usage of `bool`:

```rust
let praise_the_borrow_checker = true;

// using the `if` conditional
if praise_the_borrow_checker {
    println!("oh, yeah!");
} else {
    println!("what?!!");
}

// ... or, a match pattern
match praise_the_borrow_checker {
    true => println!("keep praising!"),
    false => println!("you should praise!"),
}
```

Also, since `bool` implements the [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") trait, we don’t have to worry about the move semantics (just like the integer and float primitives).

Now an example of `bool` cast to integer type:

```rust
assert_eq!(true as i32, 1);
assert_eq!(false as i32, 0);
```

[Source](https://doc.rust-lang.org/stable/src/core/bool.rs.html#5)[§](#impl-bool)

1.62.0 (const: [unstable](https://github.com/rust-lang/rust/issues/151531 "Tracking issue for const_bool")) · [Source](https://doc.rust-lang.org/stable/src/core/bool.rs.html#36)

Returns `Some(t)` if the `bool` is [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html), or `None` otherwise.

Arguments passed to `then_some` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`then`](https://doc.rust-lang.org/stable/std/primitive.bool.html#method.then "method bool::then"), which is lazily evaluated.

##### [§](#examples-1)Examples

```rust
assert_eq!(false.then_some(0), None);
assert_eq!(true.then_some(0), Some(0));
```

```rust
let mut a = 0;
let mut function_with_side_effects = || { a += 1; };

true.then_some(function_with_side_effects());
false.then_some(function_with_side_effects());

// `a` is incremented twice because the value passed to `then_some` is
// evaluated eagerly.
assert_eq!(a, 2);
```

1.50.0 (const: [unstable](https://github.com/rust-lang/rust/issues/151531 "Tracking issue for const_bool")) · [Source](https://doc.rust-lang.org/stable/src/core/bool.rs.html#65)

Returns `Some(f())` if the `bool` is [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html), or `None` otherwise.

##### [§](#examples-2)Examples

```rust
assert_eq!(false.then(|| 0), None);
assert_eq!(true.then(|| 0), Some(0));
```

```rust
let mut a = 0;

true.then(|| { a += 1; });
false.then(|| { a += 1; });

// `a` is incremented once because the closure is evaluated lazily by
// `then`.
assert_eq!(a, 1);
```

[Source](https://doc.rust-lang.org/stable/src/core/bool.rs.html#103)

🔬This is a nightly-only experimental API. (`bool_to_result` [#142748](https://github.com/rust-lang/rust/issues/142748))

Returns `Ok(())` if the `bool` is [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html), or `Err(err)` otherwise.

Arguments passed to `ok_or` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`ok_or_else`](https://doc.rust-lang.org/stable/std/primitive.bool.html#method.ok_or_else "method bool::ok_or_else"), which is lazily evaluated.

##### [§](#examples-3)Examples

```rust
#![feature(bool_to_result)]

assert_eq!(false.ok_or(0), Err(0));
assert_eq!(true.ok_or(0), Ok(()));
```

```rust
#![feature(bool_to_result)]

let mut a = 0;
let mut function_with_side_effects = || { a += 1; };

assert!(true.ok_or(function_with_side_effects()).is_ok());
assert!(false.ok_or(function_with_side_effects()).is_err());

// `a` is incremented twice because the value passed to `ok_or` is
// evaluated eagerly.
assert_eq!(a, 2);
```

[Source](https://doc.rust-lang.org/stable/src/core/bool.rs.html#134-137)

🔬This is a nightly-only experimental API. (`bool_to_result` [#142748](https://github.com/rust-lang/rust/issues/142748))

Returns `Ok(())` if the `bool` is [`true`](https://doc.rust-lang.org/stable/std/keyword.true.html), or `Err(f())` otherwise.

##### [§](#examples-4)Examples

```rust
#![feature(bool_to_result)]

assert_eq!(false.ok_or_else(|| 0), Err(0));
assert_eq!(true.ok_or_else(|| 0), Ok(()));
```

```rust
#![feature(bool_to_result)]

let mut a = 0;

assert!(true.ok_or_else(|| { a += 1; }).is_ok());
assert!(false.ok_or_else(|| { a += 1; }).is_err());

// `a` is incremented once because the closure is evaluated lazily by
// `ok_or_else`.
assert_eq!(a, 1);
```

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#297)[§](#impl-AtomicPrimitive-for-bool)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#297)[§](#associatedtype.AtomicInner)

🔬This is a nightly-only experimental API. (`atomic_internals`)

Temporary implementation detail.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26bool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-17)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-16)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-2)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#496-498)[§](#impl-BitAnd%3CMask%3CT,+N%3E%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#500)[§](#associatedtype.Output-19)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#502)[§](#method.bitand-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd%3Cbool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-15)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand-1)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#485-487)[§](#impl-BitAnd%3Cbool%3E-for-Mask%3CT,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#489)[§](#associatedtype.Output-18)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#491)[§](#method.bitand-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#impl-BitAnd-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#associatedtype.Output-14)

The resulting type after applying the `&` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#187)[§](#method.bitand)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#596-598)[§](#impl-BitAndAssign%3Cbool%3E-for-Mask%3CT,+N%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#755)[§](#impl-BitAndAssign-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26bool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-2)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-2)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#530-532)[§](#impl-BitOr%3CMask%3CT,+N%3E%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#534)[§](#associatedtype.Output-5)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#536)[§](#method.bitor-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr%3Cbool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output-1)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor-1)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#519-521)[§](#impl-BitOr%3Cbool%3E-for-Mask%3CT,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#523)[§](#associatedtype.Output-4)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#525)[§](#method.bitor-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#impl-BitOr-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#291)[§](#method.bitor)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#616-618)[§](#impl-BitOrAssign%3Cbool%3E-for-Mask%3CT,+N%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#830)[§](#impl-BitOrAssign-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26bool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-11)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-10)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-2)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#564-566)[§](#impl-BitXor%3CMask%3CT,+N%3E%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#568)[§](#associatedtype.Output-13)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#570)[§](#method.bitxor-5)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor%3Cbool%3E-for-%26bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-9)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor-1)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#553-555)[§](#impl-BitXor%3Cbool%3E-for-Mask%3CT,+N%3E)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#557)[§](#associatedtype.Output-12)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#559)[§](#method.bitxor-4)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#impl-BitXor-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#associatedtype.Output-8)

The resulting type after applying the `^` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#395)[§](#method.bitxor)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign%3C%26bool%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/masks.rs.html#636-638)[§](#impl-BitXorAssign%3Cbool%3E-for-Mask%3CT,+N%3E)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#905)[§](#impl-BitXorAssign-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-bool)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#2894)[§](#impl-Debug-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#165)[§](#impl-Default-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#165)[§](#method.default)

Returns the default value of `false`

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#impl-DisjointBitOr-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/intrinsics/fallback.rs.html#144-148)[§](#method.disjoint_bitor)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/stable/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#2902)[§](#impl-Display-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#30)[§](#impl-Distribution%3Cbool%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/random.rs.html#31)[§](#method.sample)

🔬This is a nightly-only experimental API. (`random` [#130703](https://github.com/rust-lang/rust/issues/130703))

Samples a random value from the distribution, using the specified random source.

1.24.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#2477)[§](#impl-From%3Cbool%3E-for-AtomicBool)

Available on **`target_has_atomic_load_store=8`** only.

[Source](https://doc.rust-lang.org/stable/src/core/sync/atomic.rs.html#2488)[§](#method.from-16)

Converts a `bool` into an `AtomicBool`.

##### [§](#examples-22)Examples

```rust
use std::sync::atomic::AtomicBool;
let atomic_bool = AtomicBool::from(true);
assert_eq!(format!("{atomic_bool:?}"), "true")
```

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#231-240)[§](#impl-From%3Cbool%3E-for-f128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#231-240)[§](#method.from-15)

Converts a [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`f128`](https://doc.rust-lang.org/stable/std/primitive.f128.html "primitive f128") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-21)Examples

```rust
#![feature(f128)]

let x: f128 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f128 = true.into();
assert_eq!(y, 1.0);
```

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#218-228)[§](#impl-From%3Cbool%3E-for-f16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#218-228)[§](#method.from-12)

Converts a [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`f16`](https://doc.rust-lang.org/stable/std/primitive.f16.html "primitive f16") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-18)Examples

```rust
#![feature(f16)]

let x: f16 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f16 = true.into();
assert_eq!(y, 1.0);
```

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#229)[§](#impl-From%3Cbool%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#229)[§](#method.from-13)

Converts a [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-19)Examples

```rust
let x: f32 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f32 = true.into();
assert_eq!(y, 1.0);
```

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#230)[§](#impl-From%3Cbool%3E-for-f64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#230)[§](#method.from-14)

Converts a [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`f64`](https://doc.rust-lang.org/stable/std/primitive.f64.html "primitive f64") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-20)Examples

```rust
let x: f64 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f64 = true.into();
assert_eq!(y, 1.0);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-10)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i128`](https://doc.rust-lang.org/stable/std/primitive.i128.html "primitive i128") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-16)Examples

```rust
assert_eq!(i128::from(false), 0);

assert_eq!(i128::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-7)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i16`](https://doc.rust-lang.org/stable/std/primitive.i16.html "primitive i16") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-13)Examples

```rust
assert_eq!(i16::from(false), 0);

assert_eq!(i16::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-8)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i32`](https://doc.rust-lang.org/stable/std/primitive.i32.html "primitive i32") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-14)Examples

```rust
assert_eq!(i32::from(false), 0);

assert_eq!(i32::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-9)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i64`](https://doc.rust-lang.org/stable/std/primitive.i64.html "primitive i64") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-15)Examples

```rust
assert_eq!(i64::from(false), 0);

assert_eq!(i64::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-6)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`i8`](https://doc.rust-lang.org/stable/std/primitive.i8.html "primitive i8") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-12)Examples

```rust
assert_eq!(i8::from(false), 0);

assert_eq!(i8::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-isize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#69)[§](#method.from-11)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`isize`](https://doc.rust-lang.org/stable/std/primitive.isize.html "primitive isize") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-17)Examples

```rust
assert_eq!(isize::from(false), 0);

assert_eq!(isize::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u128)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from-4)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u128`](https://doc.rust-lang.org/stable/std/primitive.u128.html "primitive u128") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-10)Examples

```rust
assert_eq!(u128::from(false), 0);

assert_eq!(u128::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u16)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from-1)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u16`](https://doc.rust-lang.org/stable/std/primitive.u16.html "primitive u16") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-7)Examples

```rust
assert_eq!(u16::from(false), 0);

assert_eq!(u16::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from-2)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u32`](https://doc.rust-lang.org/stable/std/primitive.u32.html "primitive u32") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-8)Examples

```rust
assert_eq!(u32::from(false), 0);

assert_eq!(u32::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u64)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from-3)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u64`](https://doc.rust-lang.org/stable/std/primitive.u64.html "primitive u64") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-9)Examples

```rust
assert_eq!(u64::from(false), 0);

assert_eq!(u64::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u8)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`u8`](https://doc.rust-lang.org/stable/std/primitive.u8.html "primitive u8") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-6)Examples

```rust
assert_eq!(u8::from(false), 0);

assert_eq!(u8::from(true), 1);
```

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#68)[§](#method.from-5)

Converts from [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`usize`](https://doc.rust-lang.org/stable/std/primitive.usize.html "primitive usize") , by turning `false` into `0` and `true` into `1`.

##### [§](#examples-11)Examples

```rust
assert_eq!(usize::from(false), 0);

assert_eq!(usize::from(true), 1);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#866)[§](#impl-FromStr-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#892)[§](#method.from_str)

Parse a `bool` from a string.

The only accepted values are `"true"` and `"false"`. Any other input will return an error.

##### [§](#examples-5)Examples

```rust
use std::str::FromStr;

assert_eq!(FromStr::from_str("true"), Ok(true));
assert_eq!(FromStr::from_str("false"), Ok(false));
assert!(<bool as FromStr>::from_str("not even a boolean").is_err());
```

Note, in many cases, the `.parse()` method on `str` is more proper.

```rust
assert_eq!("true".parse(), Ok(true));
assert_eq!("false".parse(), Ok(false));
assert!("not even a boolean".parse::<bool>().is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#867)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#846)[§](#impl-Hash-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-%26bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#72)[§](#impl-Not-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2048)[§](#impl-Ord-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1982)[§](#impl-PartialOrd-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1984)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1988)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1988)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1988)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1988)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci128%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from-5)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-28)Examples

```rust
assert_eq!(0_i128.try_into(), Ok(false));

assert_eq!(1_i128.try_into(), Ok(true));

assert!(<i128 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-5)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci16%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from-8)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-31)Examples

```rust
assert_eq!(0_i16.try_into(), Ok(false));

assert_eq!(1_i16.try_into(), Ok(true));

assert!(<i16 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-8)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci32%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from-7)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-30)Examples

```rust
assert_eq!(0_i32.try_into(), Ok(false));

assert_eq!(1_i32.try_into(), Ok(true));

assert!(<i32 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-7)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci64%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from-6)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-29)Examples

```rust
assert_eq!(0_i64.try_into(), Ok(false));

assert_eq!(1_i64.try_into(), Ok(true));

assert!(<i64 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-6)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#impl-TryFrom%3Ci8%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#method.try_from-9)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-32)Examples

```rust
assert_eq!(0_i8.try_into(), Ok(false));

assert_eq!(1_i8.try_into(), Ok(true));

assert!(<i8 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#372)[§](#associatedtype.Error-9)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu128%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-23)Examples

```rust
assert_eq!(0_u128.try_into(), Ok(false));

assert_eq!(1_u128.try_into(), Ok(true));

assert!(<u128 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu16%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from-3)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-26)Examples

```rust
assert_eq!(0_u16.try_into(), Ok(false));

assert_eq!(1_u16.try_into(), Ok(true));

assert!(<u16 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu32%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from-2)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-25)Examples

```rust
assert_eq!(0_u32.try_into(), Ok(false));

assert_eq!(1_u32.try_into(), Ok(true));

assert!(<u32 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu64%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from-1)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-24)Examples

```rust
assert_eq!(0_u64.try_into(), Ok(false));

assert_eq!(1_u64.try_into(), Ok(true));

assert!(<u64 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#impl-TryFrom%3Cu8%3E-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#method.try_from-4)

Tries to create a bool from an integer type. Returns an error if the integer is not 0 or 1.

##### [§](#examples-27)Examples

```rust
assert_eq!(0_u8.try_into(), Ok(false));

assert_eq!(1_u8.try_into(), Ok(true));

assert!(<u8 as TryInto<bool>>::try_into(2).is_err());
```

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#371)[§](#associatedtype.Error-4)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-bool)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-bool)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-bool)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-bool)

[§](#impl-Freeze-for-bool)

[§](#impl-RefUnwindSafe-for-bool)

[§](#impl-Send-for-bool)

[§](#impl-Sync-for-bool)

[§](#impl-Unpin-for-bool)

[§](#impl-UnsafeUnpin-for-bool)

[§](#impl-UnwindSafe-for-bool)