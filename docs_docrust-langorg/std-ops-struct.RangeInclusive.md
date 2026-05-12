---
title: RangeInclusive in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html
source: crawler
fetched_at: 2026-05-06T21:27:55.108183573-03:00
rendered_js: false
word_count: 2908
summary: This document provides the API reference for the RangeInclusive struct in Rust, which represents a range bounded inclusively at both ends.
tags:
    - rust
    - rust-standard-library
    - range
    - iterator
    - inclusive-range
    - programming-primitives
category: reference
---

## Struct RangeInclusive

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#357)

```rust
pub struct RangeInclusive<Idx> { /* private fields */ }
```

Expand description

A range bounded inclusively below and above (`start..=end`).

The `RangeInclusive` `start..=end` contains all values with `x >= start` and `x <= end`. It is empty unless `start <= end`.

This iterator is [fused](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html "trait std::iter::FusedIterator"), but the specific values of `start` and `end` after iteration has finished are **unspecified** other than that [`.is_empty()`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html#method.is_empty "method std::ops::RangeInclusive::is_empty") will return `true` once no more values will be produced.

## [§](#examples)Examples

The `start..=end` syntax is a `RangeInclusive`:

```rust
assert_eq!((3..=5), std::ops::RangeInclusive::new(3, 5));
assert_eq!(3 + 4 + 5, (3..=5).sum());
```

```rust
let arr = [0, 1, 2, 3, 4];
assert_eq!(arr[ ..  ], [0, 1, 2, 3, 4]);
assert_eq!(arr[ .. 3], [0, 1, 2      ]);
assert_eq!(arr[ ..=3], [0, 1, 2, 3   ]);
assert_eq!(arr[1..  ], [   1, 2, 3, 4]);
assert_eq!(arr[1.. 3], [   1, 2      ]);
assert_eq!(arr[1..=3], [   1, 2, 3   ]); // This is a `RangeInclusive`
```

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#375)[§](#impl-RangeInclusive%3CIdx%3E)

1.27.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#390)

Creates a new inclusive range. Equivalent to writing `start..=end`.

##### [§](#examples-1)Examples

```rust
use std::ops::RangeInclusive;

assert_eq!(3..=5, RangeInclusive::new(3, 5));
```

1.27.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#415)

Returns the lower bound of the range (inclusive).

When using an inclusive range for iteration, the values of `start()` and [`end()`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html#method.end "method std::ops::RangeInclusive::end") are unspecified after the iteration ended. To determine whether the inclusive range is empty, use the [`is_empty()`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html#method.is_empty "method std::ops::RangeInclusive::is_empty") method instead of comparing `start() > end()`.

Note: the value returned by this method is unspecified after the range has been iterated to exhaustion.

##### [§](#examples-2)Examples

```rust
assert_eq!((3..=5).start(), &3);
```

1.27.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#440)

Returns the upper bound of the range (inclusive).

When using an inclusive range for iteration, the values of [`start()`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html#method.start "method std::ops::RangeInclusive::start") and `end()` are unspecified after the iteration ended. To determine whether the inclusive range is empty, use the [`is_empty()`](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html#method.is_empty "method std::ops::RangeInclusive::is_empty") method instead of comparing `start() > end()`.

Note: the value returned by this method is unspecified after the range has been iterated to exhaustion.

##### [§](#examples-3)Examples

```rust
assert_eq!((3..=5).end(), &5);
```

1.27.0 (const: [unstable](https://github.com/rust-lang/rust/issues/108082 "Tracking issue for const_range_bounds")) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#457)

Destructures the `RangeInclusive` into (lower bound, upper (inclusive) bound).

Note: the value returned by this method is unspecified after the range has been iterated to exhaustion.

##### [§](#examples-4)Examples

```rust
assert_eq!((3..=5).into_inner(), (3, 5));
```

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#489)[§](#impl-RangeInclusive%3CIdx%3E-1)

1.35.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#522-525)

Returns `true` if `item` is contained in the range.

##### [§](#examples-5)Examples

```rust
assert!(!(3..=5).contains(&2));
assert!( (3..=5).contains(&3));
assert!( (3..=5).contains(&4));
assert!( (3..=5).contains(&5));
assert!(!(3..=5).contains(&6));

assert!( (3..=3).contains(&3));
assert!(!(3..=2).contains(&3));

assert!( (0.0..=1.0).contains(&1.0));
assert!(!(0.0..=1.0).contains(&f32::NAN));
assert!(!(0.0..=f32::NAN).contains(&0.0));
assert!(!(f32::NAN..=1.0).contains(&1.0));
```

This method always returns `false` after iteration has finished:

```rust
let mut r = 3..=5;
assert!(r.contains(&3) && r.contains(&5));
for _ in r.by_ref() {}
// Precise field values are unspecified here
assert!(!r.contains(&3) && !r.contains(&5));
```

1.47.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#559-561)

Returns `true` if the range contains no items.

##### [§](#examples-6)Examples

```rust
assert!(!(3..=5).is_empty());
assert!(!(3..=3).is_empty());
assert!( (3..=2).is_empty());
```

The range is empty if either side is incomparable:

```rust
assert!(!(3.0..=5.0).is_empty());
assert!( (3.0..=f32::NAN).is_empty());
assert!( (f32::NAN..=5.0).is_empty());
```

This method returns `true` after iteration has finished:

```rust
let mut r = 3..=5;
for _ in r.by_ref() {}
// Precise field values are unspecified here
assert!(r.is_empty());
```

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#354)[§](#impl-Clone-for-RangeInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#477)[§](#impl-Debug-for-RangeInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1353)[§](#impl-DoubleEndedIterator-for-RangeInclusive%3CA%3E)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1355)[§](#method.next_back)

Removes and returns an element from the end of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#tymethod.next_back)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1360)[§](#method.nth_back)

Returns the `n`th element from the end of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#method.nth_back)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1388-1392)[§](#method.try_rfold)

This is the reverse version of [`Iterator::try_fold()`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_fold "method std::iter::Iterator::try_fold"): it takes elements starting from the back of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#method.try_rfold)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1397)[§](#method.rfold)

An iterator method that reduces the iterator’s elements to a single, final value, starting from the back. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#method.rfold)

[Source](https://doc.rust-lang.org/src/core/iter/traits/double_ended.rs.html#138)[§](#method.advance_back_by)

🔬This is a nightly-only experimental API. (`iter_advance_by` [#77404](https://github.com/rust-lang/rust/issues/77404))

Advances the iterator from the back by `n` elements. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#method.advance_back_by)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/double_ended.rs.html#366-369)[§](#method.rfind)

Searches for an element of an iterator from the back that satisfies a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html#method.rfind)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#963-973)[§](#impl-ExactSizeIterator-for-RangeInclusive%3Ci16%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#116)[§](#method.len-3)

Returns the exact remaining length of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.len)

[Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#148)[§](#method.is_empty-4)

🔬This is a nightly-only experimental API. (`exact_size_is_empty` [#35428](https://github.com/rust-lang/rust/issues/35428))

Returns `true` if the iterator is empty. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.is_empty)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#963-973)[§](#impl-ExactSizeIterator-for-RangeInclusive%3Ci8%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#116)[§](#method.len-1)

Returns the exact remaining length of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.len)

[Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#148)[§](#method.is_empty-2)

🔬This is a nightly-only experimental API. (`exact_size_is_empty` [#35428](https://github.com/rust-lang/rust/issues/35428))

Returns `true` if the iterator is empty. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.is_empty)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#963-973)[§](#impl-ExactSizeIterator-for-RangeInclusive%3Cu16%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#116)[§](#method.len-2)

Returns the exact remaining length of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.len)

[Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#148)[§](#method.is_empty-3)

🔬This is a nightly-only experimental API. (`exact_size_is_empty` [#35428](https://github.com/rust-lang/rust/issues/35428))

Returns `true` if the iterator is empty. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.is_empty)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#963-973)[§](#impl-ExactSizeIterator-for-RangeInclusive%3Cu8%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#116)[§](#method.len)

Returns the exact remaining length of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.len)

[Source](https://doc.rust-lang.org/src/core/iter/traits/exact_size.rs.html#148)[§](#method.is_empty-1)

🔬This is a nightly-only experimental API. (`exact_size_is_empty` [#35428](https://github.com/rust-lang/rust/issues/35428))

Returns `true` if the iterator is empty. [Read more](https://doc.rust-lang.org/std/iter/trait.ExactSizeIterator.html#method.is_empty)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#401)[§](#impl-From%3CRangeInclusive%3CT%3E%3E-for-RangeInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#403)[§](#method.from)

Converts to this type from the input type.

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#409)[§](#impl-From%3CRangeInclusive%3CT%3E%3E-for-RangeInclusive%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#411)[§](#method.from-1)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5806)[§](#impl-GetDisjointMutIndex-for-RangeInclusive%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5808)[§](#method.is_in_bounds)

🔬This is a nightly-only experimental API. (`get_disjoint_mut_helpers`)

Returns `true` if `self` is in bounds for `len` slice elements.

[Source](https://doc.rust-lang.org/src/core/slice/mod.rs.html#5813)[§](#method.is_overlapping)

🔬This is a nightly-only experimental API. (`get_disjoint_mut_helpers`)

Returns `true` if `self` overlaps with `other`. [Read more](https://doc.rust-lang.org/core/slice/trait.GetDisjointMutIndex.html#tymethod.is_overlapping)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#354)[§](#impl-Hash-for-RangeInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#364)[§](#impl-Index%3CRangeInclusive%3Cusize%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#365)[§](#associatedtype.Output-3)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#368)[§](#method.index-3)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#428)[§](#impl-IndexMut%3CRangeInclusive%3Cusize%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1141)[§](#impl-IntoBounds%3CT%3E-for-RangeInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1142)[§](#method.into_bounds)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Convert this range into the start and end bounds. Returns `(start_bound, end_bound)`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#tymethod.into_bounds)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1000-1004)[§](#method.intersect)

🔬This is a nightly-only experimental API. (`range_into_bounds` [#136903](https://github.com/rust-lang/rust/issues/136903))

Compute the intersection of `self` and `other`. [Read more](https://doc.rust-lang.org/std/ops/trait.IntoBounds.html#method.intersect)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1255)[§](#impl-Iterator-for-RangeInclusive%3CA%3E)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1256)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1259)[§](#method.next)

Advances the iterator and returns the next value. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#tymethod.next)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1264)[§](#method.size_hint)

Returns the bounds on the remaining length of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.size_hint)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1274)[§](#method.count)

Consumes the iterator, counting the number of iterations and returning it. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.count)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1286)[§](#method.nth)

Returns the `n`th element of the iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.nth)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1314-1318)[§](#method.try_fold)

An iterator method that applies a function as long as it returns successfully, producing a single, final value. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_fold)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1323)[§](#method.fold)

Folds every element into an accumulator by applying an operation, returning the final result. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.fold)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1326)[§](#method.last)

Consumes the iterator, returning the last element. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.last)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1331-1333)[§](#method.min)

Returns the minimum element of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.min)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1339-1341)[§](#method.max)

Returns the maximum element of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.max)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1347)[§](#method.is_sorted)

Checks if the elements of this iterator are sorted. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.is_sorted)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#112-116)[§](#method.next_chunk)

🔬This is a nightly-only experimental API. (`iter_next_chunk` [#98326](https://github.com/rust-lang/rust/issues/98326))

Advances the iterator and returns an array containing the next `N` values. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.next_chunk)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#306)[§](#method.advance_by)

🔬This is a nightly-only experimental API. (`iter_advance_by` [#77404](https://github.com/rust-lang/rust/issues/77404))

Advances the iterator by `n` elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.advance_by)

1.28.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#435-437)[§](#method.step_by)

Creates an iterator starting at the same point, but stepping by the given amount at each iteration. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.step_by)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#507-510)[§](#method.chain)

Takes two iterators and creates a new iterator over both in sequence. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#626-629)[§](#method.zip)

‘Zips up’ two iterators into a single iterator of pairs. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.zip)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#670-673)[§](#method.intersperse)

🔬This is a nightly-only experimental API. (`iter_intersperse` [#79524](https://github.com/rust-lang/rust/issues/79524))

Creates a new iterator which places a copy of `separator` between adjacent items of the original iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.intersperse)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#729-732)[§](#method.intersperse_with)

🔬This is a nightly-only experimental API. (`iter_intersperse` [#79524](https://github.com/rust-lang/rust/issues/79524))

Creates a new iterator which places an item generated by `separator` between adjacent items of the original iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.intersperse_with)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#789-792)[§](#method.map)

Takes a closure and creates an iterator which calls that closure on each element. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map)

1.21.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#835-838)[§](#method.for_each)

Calls a closure on each element of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.for_each)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#911-914)[§](#method.filter)

Creates an iterator which uses a closure to determine if an element should be yielded. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#957-960)[§](#method.filter_map)

Creates an iterator that both filters and maps. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter_map)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1005-1007)[§](#method.enumerate)

Creates an iterator which gives the current iteration count as well as the next value. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.enumerate)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1077-1079)[§](#method.peekable)

Creates an iterator which can use the [`peek`](https://doc.rust-lang.org/std/iter/struct.Peekable.html#method.peek "method std::iter::Peekable::peek") and [`peek_mut`](https://doc.rust-lang.org/std/iter/struct.Peekable.html#method.peek_mut "method std::iter::Peekable::peek_mut") methods to look at the next element of the iterator without consuming it. See their documentation for more information. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.peekable)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1143-1146)[§](#method.skip_while)

Creates an iterator that [`skip`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.skip "method std::iter::Iterator::skip")s elements based on a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.skip_while)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1222-1225)[§](#method.take_while)

Creates an iterator that yields elements based on a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.take_while)

1.57.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1311-1314)[§](#method.map_while)

Creates an iterator that both yields elements based on a predicate and maps. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map_while)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1341-1343)[§](#method.skip)

Creates an iterator that skips the first `n` elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.skip)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1414-1416)[§](#method.take)

Creates an iterator that yields the first `n` elements, or fewer if the underlying iterator ends sooner. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.take)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1462-1465)[§](#method.scan)

An iterator adapter which, like [`fold`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.fold "method std::iter::Iterator::fold"), holds internal state, but unlike [`fold`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.fold "method std::iter::Iterator::fold"), produces a new iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.scan)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1501-1505)[§](#method.flat_map)

Creates an iterator that works like map, but flattens nested structure. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.flat_map)

1.29.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1586-1589)[§](#method.flatten)

Creates an iterator that flattens nested structure. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.flatten)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1743-1746)[§](#method.map_windows)

🔬This is a nightly-only experimental API. (`iter_map_windows` [#87155](https://github.com/rust-lang/rust/issues/87155))

Calls the given function `f` for each contiguous window of size `N` over `self` and returns an iterator over the outputs of `f`. Like [`slice::windows()`](https://doc.rust-lang.org/std/primitive.slice.html#method.windows "method slice::windows"), the windows during mapping overlap as well. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map_windows)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1806-1808)[§](#method.fuse)

Creates an iterator which ends after the first [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None"). [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.fuse)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1891-1894)[§](#method.inspect)

Does something with each element of an iterator, passing the value on. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.inspect)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#1928-1930)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Iterator`. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2051-2053)[§](#method.collect)

Transforms an iterator into a collection. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2139-2143)[§](#method.try_collect)

🔬This is a nightly-only experimental API. (`iterator_try_collect` [#94047](https://github.com/rust-lang/rust/issues/94047))

Fallibly transforms an iterator into a collection, short circuiting if a failure is encountered. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_collect)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2212-2214)[§](#method.collect_into)

🔬This is a nightly-only experimental API. (`iter_collect_into` [#94780](https://github.com/rust-lang/rust/issues/94780))

Collects all the items from an iterator into a collection. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect_into)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2245-2249)[§](#method.partition)

Consumes an iterator, creating two collections from it. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.partition)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2308-2311)[§](#method.partition_in_place)

🔬This is a nightly-only experimental API. (`iter_partition_in_place` [#62543](https://github.com/rust-lang/rust/issues/62543))

Reorders the elements of this iterator *in-place* according to the given predicate, such that all those that return `true` precede all those that return `false`. Returns the number of `true` elements found. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.partition_in_place)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2366-2369)[§](#method.is_partitioned)

🔬This is a nightly-only experimental API. (`iter_is_partitioned` [#62544](https://github.com/rust-lang/rust/issues/62544))

Checks if the elements of this iterator are partitioned according to the given predicate, such that all those that return `true` precede all those that return `false`. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.is_partitioned)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2520-2524)[§](#method.try_for_each)

An iterator method that applies a fallible function to each item in the iterator, stopping at the first error and returning that error. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_for_each)

1.51.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2678-2681)[§](#method.reduce)

Reduces the elements to a single one, by repeatedly applying a reducing operation. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.reduce)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2750-2756)[§](#method.try_reduce)

🔬This is a nightly-only experimental API. (`iterator_try_reduce` [#87053](https://github.com/rust-lang/rust/issues/87053))

Reduces the elements to a single one by repeatedly applying a reducing operation. If the closure returns a failure, the failure is propagated back to the caller immediately. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_reduce)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2809-2812)[§](#method.all)

Tests if every element of the iterator matches a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.all)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2863-2866)[§](#method.any)

Tests if any element of the iterator matches a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.any)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2937-2940)[§](#method.find)

Searches for an element of an iterator that satisfies a predicate. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.find)

1.30.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#2969-2972)[§](#method.find_map)

Applies function to the elements of iterator and returns the first non-none result. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.find_map)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3028-3034)[§](#method.try_find)

🔬This is a nightly-only experimental API. (`try_find` [#63178](https://github.com/rust-lang/rust/issues/63178))

Applies function to the elements of iterator and returns the first true result or the first error. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.try_find)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3112-3115)[§](#method.position)

Searches for an element in an iterator, returning its index. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.position)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3178-3181)[§](#method.rposition)

Searches for an element in an iterator from the right, returning its index. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.rposition)

1.6.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3288-3291)[§](#method.max_by_key)

Returns the element that gives the maximum value from the specified function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.max_by_key)

1.15.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3322-3325)[§](#method.max_by)

Returns the element that gives the maximum value with respect to the specified comparison function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.max_by)

1.6.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3350-3353)[§](#method.min_by_key)

Returns the element that gives the minimum value from the specified function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.min_by_key)

1.15.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3384-3387)[§](#method.min_by)

Returns the element that gives the minimum value with respect to the specified comparison function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.min_by)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3422-3424)[§](#method.rev)

Reverses an iterator’s direction. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.rev)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3459-3463)[§](#method.unzip)

Converts an iterator of pairs into a pair of containers. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.unzip)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3491-3494)[§](#method.copied)

Creates an iterator which copies all of its elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.copied)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3540-3543)[§](#method.cloned)

Creates an iterator which [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone")s all of its elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.cloned)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3572-3574)[§](#method.cycle)

Repeats an iterator endlessly. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.cycle)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3616-3618)[§](#method.array_chunks)

🔬This is a nightly-only experimental API. (`iter_array_chunks` [#100450](https://github.com/rust-lang/rust/issues/100450))

Returns an iterator over `N` elements of the iterator at a time. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.array_chunks)

1.11.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3653-3656)[§](#method.sum)

Sums the elements of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.sum)

1.11.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3686-3689)[§](#method.product)

Iterates over the entire iterator, multiplying all the elements [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.product)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3708-3712)[§](#method.cmp)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3736-3740)[§](#method.cmp_by)

🔬This is a nightly-only experimental API. (`iter_order_by` [#64295](https://github.com/rust-lang/rust/issues/64295))

[Lexicographically](https://doc.rust-lang.org/std/cmp/trait.Ord.html#lexicographical-comparison "trait std::cmp::Ord") compares the elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") with those of another with respect to the specified comparison function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.cmp_by)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3793-3797)[§](#method.partial_cmp)

[Lexicographically](https://doc.rust-lang.org/std/cmp/trait.Ord.html#lexicographical-comparison "trait std::cmp::Ord") compares the [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") with those of another. The comparison works like short-circuit evaluation, returning a result without comparing the remaining elements. As soon as an order can be determined, the evaluation stops and a result is returned. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3830-3834)[§](#method.partial_cmp_by)

🔬This is a nightly-only experimental API. (`iter_order_by` [#64295](https://github.com/rust-lang/rust/issues/64295))

[Lexicographically](https://doc.rust-lang.org/std/cmp/trait.Ord.html#lexicographical-comparison "trait std::cmp::Ord") compares the elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") with those of another with respect to the specified comparison function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.partial_cmp_by)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3864-3868)[§](#method.eq-1)

Determines if the elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") are equal to those of another. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.eq)

[Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3888-3892)[§](#method.eq_by)

🔬This is a nightly-only experimental API. (`iter_order_by` [#64295](https://github.com/rust-lang/rust/issues/64295))

Determines if the elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") are equal to those of another with respect to the specified equality function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.eq_by)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3918-3922)[§](#method.ne-1)

Determines if the elements of this [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") are not equal to those of another. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.ne)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3940-3944)[§](#method.lt)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3962-3966)[§](#method.le)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#3984-3988)[§](#method.gt)

1.5.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#4006-4010)[§](#method.ge)

1.82.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#4063-4066)[§](#method.is_sorted_by)

Checks if the elements of this iterator are sorted using the given comparator function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.is_sorted_by)

1.82.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#4108-4112)[§](#method.is_sorted_by_key)

Checks if the elements of this iterator are sorted using the given key extraction function. [Read more](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.is_sorted_by_key)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#355)[§](#impl-PartialEq-for-RangeInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#355)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1274)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3C%26T%3E)

If you need to use this implementation where `T` is unsized, consider using the `RangeBounds` impl for a 2-tuple of [`Bound<&T>`](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound"), i.e. replace `start..=end` with `(Bound::Included(start), Bound::Included(end))`.

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1275)[§](#method.start_bound-1)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1278)[§](#method.end_bound-1)

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)[§](#method.contains-2)

Returns `true` if `item` is contained in the range. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.contains)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)[§](#method.is_empty-6)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.is_empty)

1.28.0 (const: unstable) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1124)[§](#impl-RangeBounds%3CT%3E-for-RangeInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1125)[§](#method.start_bound)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#1128)[§](#method.end_bound)

1.35.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#868-871)[§](#method.contains-1)

Returns `true` if `item` is contained in the range. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.contains)

[Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#936-938)[§](#method.is_empty-5)

🔬This is a nightly-only experimental API. (`range_bounds_is_empty` [#137300](https://github.com/rust-lang/rust/issues/137300))

Returns `true` if the range contains no items. One-sided ranges (`RangeFrom`, etc) always return `false`. [Read more](https://doc.rust-lang.org/std/ops/trait.RangeBounds.html#method.is_empty)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#670)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if:

- the start of the range is greater than the end of the range or
- the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#671)[§](#associatedtype.Output-1)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#674)[§](#method.get-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#679)[§](#method.get_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#684)[§](#method.get_unchecked-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#690)[§](#method.get_unchecked_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#696)[§](#method.index-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/slice/index.rs.html#711)[§](#method.index_mut-1)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeInclusive%3Cusize%3E)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#associatedtype.Output)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.get)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.get_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.get_unchecked)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.get_unchecked_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.index)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/bstr/traits.rs.html#268)[§](#method.index_mut)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#632)[§](#impl-SliceIndex%3Cstr%3E-for-RangeInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[begin ..= end]` or `&mut self[begin ..= end]`.

Returns a slice of the given string from the byte range \[`begin`, `end`]. Equivalent to `&self [begin .. end + 1]` or `&mut self[begin .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics)Panics

Panics if `begin` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset or equal to `len`), if `begin > end`, or if `end >= len`.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#633)[§](#associatedtype.Output-2)

The output type returned by methods.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#635)[§](#method.get-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#639)[§](#method.get_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#643)[§](#method.get_unchecked-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#648)[§](#method.get_unchecked_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking. [Read more](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html#tymethod.get_unchecked_mut)

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#653)[§](#method.index-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#670)[§](#method.index_mut-2)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#355)[§](#impl-Eq-for-RangeInclusive%3CIdx%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1405)[§](#impl-FusedIterator-for-RangeInclusive%3CA%3E)

1.26.0 · [Source](https://doc.rust-lang.org/src/core/ops/range.rs.html#355)[§](#impl-StructuralPartialEq-for-RangeInclusive%3CIdx%3E)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#1402)[§](#impl-TrustedLen-for-RangeInclusive%3CA%3E)