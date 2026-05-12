---
title: RangeToInclusive in std::range - Rust
url: https://doc.rust-lang.org/std/range/struct.RangeToInclusive.html
source: crawler
fetched_at: 2026-05-06T21:38:36.417812914-03:00
rendered_js: false
word_count: 534
summary: RangeToInclusive defines a Rust range type that includes all values less than or equal to a specified upper bound, primarily used for slicing operations.
tags:
    - rust
    - range
    - slice-index
    - inclusive-range
    - data-structure
category: reference
---

## Struct RangeToInclusive

[Source](https://doc.rust-lang.org/src/core/range.rs.html#623)

```rust
pub struct RangeToInclusive<Idx> {
    pub last: Idx,
}
```

🔬This is a nightly-only experimental API. (`new_range_api` [#125687](https://github.com/rust-lang/rust/issues/125687))

Expand description

A range only bounded inclusively above.

The `RangeToInclusive` contains all values with `x <= last`. It cannot serve as an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") because it doesn’t have a starting point.

## [§](#examples)Examples

```rust
#![feature(new_range_api)]
#![feature(new_range)]
assert_eq!((..=5), std::range::RangeToInclusive{ last: 5 });
```

It does not have an [`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html "trait std::iter::IntoIterator") implementation, so you can’t use it in a `for` loop directly. This won’t compile:

[ⓘ](# "This example deliberately fails to compile")

```rust
// error[E0277]: the trait bound `std::range::RangeToInclusive<{integer}>:
// std::iter::Iterator` is not satisfied
for i in ..=5 {
    // ...
}
```

When used as a [slicing index](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html "trait std::slice::SliceIndex"), `RangeToInclusive` produces a slice of all array elements up to and including the index indicated by `last`.

```rust
let arr = [0, 1, 2, 3, 4];
assert_eq!(arr[ ..  ], [0, 1, 2, 3, 4]);
assert_eq!(arr[ .. 3], [0, 1, 2      ]);
assert_eq!(arr[ ..=3], [0, 1, 2, 3   ]); // This is a `RangeToInclusive`
assert_eq!(arr[1..  ], [   1, 2, 3, 4]);
assert_eq!(arr[1.. 3], [   1, 2      ]);
assert_eq!(arr[1..=3], [   1, 2, 3   ]);
```

## [§](#edition-notes)Edition notes

It is planned that the syntax `..=last` will construct this type in a future edition, but it does not do so today.

🔬This is a nightly-only experimental API. (`new_range_api` [#125687](https://github.com/rust-lang/rust/issues/125687))

The upper bound of the range (inclusive)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#638)[§](#impl-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#655-658)

🔬This is a nightly-only experimental API. (`new_range_api` [#125687](https://github.com/rust-lang/rust/issues/125687))

Returns `true` if `item` is contained in the range.

##### [§](#examples-1)Examples

```rust
assert!( (..=5).contains(&-1_000_000_000));
assert!( (..=5).contains(&5));
assert!(!(..=5).contains(&6));

assert!( (..=1.0).contains(&1.0));
assert!(!(..=1.0).contains(&f32::NAN));
assert!(!(..=f32::NAN).contains(&0.5));
```

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-Clone-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#630)[§](#impl-Debug-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#665)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#666)[§](#method.from)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#671)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#672)[§](#method.from-1)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-Hash-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#693)[§](#impl-IntoBounds%3CT%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#694)[§](#method.into_bounds)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Convert this range into the start and end bounds. Returns `(start_bound, end_bound)`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#tymethod.into_bounds)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1000-1004)[§](#method.intersect)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Compute the intersection of `self` and `other`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#method.intersect)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-PartialEq-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#682)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#683)[§](#method.start_bound)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#686)[§](#method.end_bound)

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)[§](#method.contains-1)

Returns `true` if `item` is contained in the range. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.contains)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)[§](#method.is_empty)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.is_empty)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#806)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#807)[§](#associatedtype.Output)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#810)[§](#method.get)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#815)[§](#method.get_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#820)[§](#method.get_unchecked)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#826)[§](#method.get_unchecked_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#832)[§](#method.index)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#837)[§](#method.index_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-Copy-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-Eq-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#621)[§](#impl-StructuralPartialEq-for-RangeToInclusive%3CIdx%3E)