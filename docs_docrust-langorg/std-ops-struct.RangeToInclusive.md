---
title: RangeToInclusive in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/struct.RangeToInclusive.html
source: crawler
fetched_at: 2026-05-06T21:27:59.917674104-03:00
rendered_js: false
word_count: 1010
summary: This document describes the RangeToInclusive struct in Rust, which represents an inclusive upper-bounded range used for slicing and range-based operations.
tags:
    - rust
    - range
    - slicing
    - std-ops
    - inclusive-range
category: reference
---

## Struct RangeToInclusive

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#610)

```rust
pub struct RangeToInclusive<Idx> {
    pub end: Idx,
}
```

Expand description

A range only bounded inclusively above (`..=end`).

The `RangeToInclusive` `..=end` contains all values with `x <= end`. It cannot serve as an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") because it doesn’t have a starting point.

## [§](#examples)Examples

The `..=end` syntax is a `RangeToInclusive`:

```rust
assert_eq!((..=5), std::ops::RangeToInclusive{ end: 5 });
```

It does not have an [`IntoIterator`](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html "trait std::iter::IntoIterator") implementation, so you can’t use it in a `for` loop directly. This won’t compile:

[ⓘ](# "This example deliberately fails to compile")

```rust
// error[E0277]: the trait bound `std::ops::RangeToInclusive<{integer}>:
// std::iter::Iterator` is not satisfied
for i in ..=5 {
    // ...
}
```

When used as a [slicing index](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html "trait std::slice::SliceIndex"), `RangeToInclusive` produces a slice of all array elements up to and including the index indicated by `end`.

```rust
let arr = [0, 1, 2, 3, 4];
assert_eq!(arr[ ..  ], [0, 1, 2, 3, 4]);
assert_eq!(arr[ .. 3], [0, 1, 2      ]);
assert_eq!(arr[ ..=3], [0, 1, 2, 3   ]); // This is a `RangeToInclusive`
assert_eq!(arr[1..  ], [   1, 2, 3, 4]);
assert_eq!(arr[1.. 3], [   1, 2      ]);
assert_eq!(arr[1..=3], [   1, 2, 3   ]);
```

The upper bound of the range (inclusive)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#625)[§](#impl-RangeToInclusive%3CIdx%3E)

1.35.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#642-645)

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

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#608)[§](#impl-Clone-for-RangeToInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#617)[§](#impl-Debug-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#665)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#666)[§](#method.from)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/range.rs.html#671)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#672)[§](#method.from-1)

Converts to this type from the input type.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#607)[§](#impl-Hash-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#394)[§](#impl-Index%3CRangeToInclusive%3Cusize%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#395)[§](#associatedtype.Output-3)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#398)[§](#method.index-3)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#452)[§](#impl-IndexMut%3CRangeToInclusive%3Cusize%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1169)[§](#impl-IntoBounds%3CT%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1170)[§](#method.into_bounds)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Convert this range into the start and end bounds. Returns `(start_bound, end_bound)`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#tymethod.into_bounds)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1000-1004)[§](#method.intersect)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Compute the intersection of `self` and `other`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#method.intersect)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1351-1353)[§](#impl-OneSidedRange%3CT%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1355)[§](#method.bound)

🔬This is a nightly-only experimental API. (`one_sided_range` [#69780](https://github.com/rust-lang/rust/issues/69780))

An internal-only helper function for `split_off` and `split_off_mut` that returns the bound of the one-sided range.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#608)[§](#impl-PartialEq-for-RangeToInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#608)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1291)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `..=end` with `(Bound::Unbounded, Bound::Included(end))`.

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1292)[§](#method.start_bound-1)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1295)[§](#method.end_bound-1)

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)[§](#method.contains-2)

Returns `true` if `item` is contained in the range. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.contains)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)[§](#method.is_empty-1)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.is_empty)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1158)[§](#impl-RangeBounds%3CT%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1159)[§](#method.start_bound)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1162)[§](#method.end_bound)

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)[§](#method.contains-1)

Returns `true` if `item` is contained in the range. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.contains)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)[§](#method.is_empty)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.is_empty)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#767)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#768)[§](#associatedtype.Output-1)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#771)[§](#method.get-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#776)[§](#method.get_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#781)[§](#method.get_unchecked-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#787)[§](#method.get_unchecked_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#793)[§](#method.index-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#798)[§](#method.index_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeToInclusive%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#associatedtype.Output)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.get)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.get_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.get_unchecked)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.get_unchecked_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.index)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#270)[§](#method.index_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#736)[§](#impl-SliceIndex%3Cstr%3E-for-RangeToInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[..= end]` or `&mut self[..= end]`.

Returns a slice of the given string from the byte range \[0, `end`]. Equivalent to `&self [0 .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics)Panics

Panics if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset as defined by `is_char_boundary`, or equal to `len`), or if `end >= len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#737)[§](#associatedtype.Output-2)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#739)[§](#method.get-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#743)[§](#method.get_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#747)[§](#method.get_unchecked-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#752)[§](#method.get_unchecked_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#757)[§](#method.index-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#761)[§](#method.index_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#607)[§](#impl-Copy-for-RangeToInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#608)[§](#impl-Eq-for-RangeToInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#608)[§](#impl-StructuralPartialEq-for-RangeToInclusive%3CIdx%3E)