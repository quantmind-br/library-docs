---
title: RangeBounds in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.RangeBounds.html
source: crawler
fetched_at: 2026-05-06T21:22:17.05249441-03:00
rendered_js: false
word_count: 441
summary: The RangeBounds trait in Rust provides a common interface for range types to define their start and end boundaries, enabling generic range operations like containment checks.
tags:
    - rust
    - trait
    - range
    - bounds
    - generic-programming
    - standard-library
category: reference
---

## Trait RangeBounds

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#820)

```rust
pub trait RangeBounds<T>
where
    T: ?Sized,{
    // Required methods
    fn start_bound(&self) -> Bound<&T>;
    fn end_bound(&self) -> Bound<&T>;

    // Provided methods
    fn contains<U>(&self, item: &U) -> bool
       where T: PartialOrd<U>,
             U: PartialOrd<T> + ?Sized { ... }
    fn is_empty(&self) -> bool
       where T: PartialOrd { ... }
}
```

Expand description

`RangeBounds` is implemented by Rust’s built-in range types, produced by range syntax like `..`, `a..`, `..b`, `..=c`, `d..e`, or `f..=g`.

1.28.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#835)

Start index bound.

Returns the start value as a `Bound`.

##### [§](#examples)Examples

```rust
use std::ops::Bound::*;
use std::ops::RangeBounds;

assert_eq!((..10).start_bound(), Unbounded);
assert_eq!((3..10).start_bound(), Included(&3));
```

1.28.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#851)

End index bound.

Returns the end value as a `Bound`.

##### [§](#examples-1)Examples

```rust
use std::ops::Bound::*;
use std::ops::RangeBounds;

assert_eq!((3..).end_bound(), Unbounded);
assert_eq!((3..10).end_bound(), Excluded(&10));
```

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)

Returns `true` if `item` is contained in the range.

##### [§](#examples-2)Examples

```rust
assert!( (3..5).contains(&4));
assert!(!(3..5).contains(&2));

assert!( (0.0..1.0).contains(&0.5));
assert!(!(0.0..1.0).contains(&f32::NAN));
assert!(!(0.0..f32::NAN).contains(&0.5));
assert!(!(f32::NAN..1.0).contains(&0.5));
```

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`.

##### [§](#examples-3)Examples

```rust
#![feature(range_bounds_is_empty)]
use std::ops::RangeBounds;

assert!(!(3..).is_empty());
assert!(!(..2).is_empty());
assert!(!RangeBounds::is_empty(&(3..5)));
assert!( RangeBounds::is_empty(&(3..3)));
assert!( RangeBounds::is_empty(&(3..2)));
```

The range is empty if either side is incomparable:

```rust
#![feature(range_bounds_is_empty)]
use std::ops::RangeBounds;

assert!(!RangeBounds::is_empty(&(3.0..5.0)));
assert!( RangeBounds::is_empty(&(3.0..f32::NAN)));
assert!( RangeBounds::is_empty(&(f32::NAN..5.0)));
```

But never empty if either side is unbounded:

```rust
#![feature(range_bounds_is_empty)]
use std::ops::RangeBounds;

assert!(!(..0).is_empty());
assert!(!(i32::MAX..).is_empty());
assert!(!RangeBounds::<u8>::is_empty(&(..)));
```

`(Excluded(a), Excluded(b))` is only empty if `a >= b`:

```rust
#![feature(range_bounds_is_empty)]
use std::ops::Bound::*;
use std::ops::RangeBounds;

assert!(!(Excluded(1), Excluded(3)).is_empty());
assert!(!(Excluded(1), Excluded(2)).is_empty());
assert!( (Excluded(1), Excluded(1)).is_empty());
assert!( (Excluded(2), Excluded(1)).is_empty());
assert!( (Excluded(3), Excluded(1)).is_empty());
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1205)[§](#impl-RangeBounds%3CT%3E-for-%28Bound%3C%26T%3E,+Bound%3C%26T%3E%29)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1177)[§](#impl-RangeBounds%3CT%3E-for-%28Bound%3CT%3E,+Bound%3CT%3E%29)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#199)[§](#impl-RangeBounds%3CT%3E-for-Range%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..end` with `(Bound::Included(start), Bound::Excluded(end))`.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#182)[§](#impl-RangeBounds%3CT%3E-for-Range%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#541)[§](#impl-RangeBounds%3CT%3E-for-RangeFrom%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..` with `(Bound::Included(start), Bound::Unbounded)`.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#524)[§](#impl-RangeBounds%3CT%3E-for-RangeFrom%3CT%3E)

1.95.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#381)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..=end` with `(Bound::Included(start), Bound::Included(end))`.

1.95.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#364)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#682)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3CT%3E)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1257)[§](#impl-RangeBounds%3CT%3E-for-Range%3C%26T%3E-1)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..end` with `(Bound::Included(start), Bound::Excluded(end))`.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1105)[§](#impl-RangeBounds%3CT%3E-for-Range%3CT%3E-1)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1223)[§](#impl-RangeBounds%3CT%3E-for-RangeFrom%3C%26T%3E-1)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..` with `(Bound::Included(start), Bound::Unbounded)`.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1067)[§](#impl-RangeBounds%3CT%3E-for-RangeFrom%3CT%3E-1)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1048)[§](#impl-RangeBounds%3CT%3E-for-RangeFull)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1274)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3C%26T%3E-1)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..=end` with `(Bound::Included(start), Bound::Included(end))`.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1124)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3CT%3E-1)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1240)[§](#impl-RangeBounds%3CT%3E-for-RangeTo%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `..end` with `(Bound::Unbounded, Bound::Excluded(end))`.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1086)[§](#impl-RangeBounds%3CT%3E-for-RangeTo%3CT%3E)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1291)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `..=end` with `(Bound::Unbounded, Bound::Included(end))`.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1158)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3CT%3E-1)