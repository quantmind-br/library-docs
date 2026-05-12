---
title: DoubleEndedIterator in std::iter - Rust
url: https://doc.rust-lang.org/stable/std/iter/trait.DoubleEndedIterator.html
source: crawler
fetched_at: 2026-05-06T21:25:38.655247511-03:00
rendered_js: false
word_count: 862
summary: The DoubleEndedIterator trait extends the base Iterator trait by providing methods to traverse and consume elements from the back end of a collection.
tags:
    - rust
    - iterator
    - collections
    - double-ended-iterator
    - trait
    - functional-programming
category: reference
---

## Trait DoubleEndedIterator

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#41)

```rust
pub trait DoubleEndedIterator: Iterator {
    // Required method
    fn next_back(&mut self) -> Option<Self::Item>;

    // Provided methods
    fn advance_back_by(&mut self, n: usize) -> Result<(), NonZero<usize>> { ... }
    fn nth_back(&mut self, n: usize) -> Option<Self::Item> { ... }
    fn try_rfold<B, F, R>(&mut self, init: B, f: F) -> R
       where Self: Sized,
             F: FnMut(B, Self::Item) -> R,
             R: Try<Output = B> { ... }
    fn rfold<B, F>(self, init: B, f: F) -> B
       where Self: Sized,
             F: FnMut(B, Self::Item) -> B { ... }
    fn rfind<P>(&mut self, predicate: P) -> Option<Self::Item>
       where Self: Sized,
             P: FnMut(&Self::Item) -> bool { ... }
}
```

Expand description

An iterator able to yield elements from both ends.

Something that implements `DoubleEndedIterator` has one extra capability over something that implements [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"): the ability to also take `Item`s from the back, as well as the front.

It is important to note that both back and forth work on the same range, and do not cross: iteration is over when they meet in the middle.

In a similar fashion to the [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator") protocol, once a `DoubleEndedIterator` returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") from a [`next_back()`](https://doc.rust-lang.org/stable/std/iter/trait.DoubleEndedIterator.html#tymethod.next_back "method std::iter::DoubleEndedIterator::next_back"), calling it again may or may not ever return [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") again. [`next()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#tymethod.next "method std::iter::Iterator::next") and [`next_back()`](https://doc.rust-lang.org/stable/std/iter/trait.DoubleEndedIterator.html#tymethod.next_back "method std::iter::DoubleEndedIterator::next_back") are interchangeable for this purpose.

## [§](#examples)Examples

Basic usage:

```rust
let numbers = vec![1, 2, 3, 4, 5, 6];

let mut iter = numbers.iter();

assert_eq!(Some(&1), iter.next());
assert_eq!(Some(&6), iter.next_back());
assert_eq!(Some(&5), iter.next_back());
assert_eq!(Some(&2), iter.next());
assert_eq!(Some(&3), iter.next());
assert_eq!(Some(&4), iter.next());
assert_eq!(None, iter.next());
assert_eq!(None, iter.next_back());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#94)

Removes and returns an element from the end of the iterator.

Returns `None` when there are no more elements.

The [trait-level](https://doc.rust-lang.org/stable/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") docs contain more details.

##### [§](#examples-1)Examples

Basic usage:

```rust
let numbers = vec![1, 2, 3, 4, 5, 6];

let mut iter = numbers.iter();

assert_eq!(Some(&1), iter.next());
assert_eq!(Some(&6), iter.next_back());
assert_eq!(Some(&5), iter.next_back());
assert_eq!(Some(&2), iter.next());
assert_eq!(Some(&3), iter.next());
assert_eq!(Some(&4), iter.next());
assert_eq!(None, iter.next());
assert_eq!(None, iter.next_back());
```

The elements yielded by `DoubleEndedIterator`’s methods may differ from the ones yielded by [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator")’s methods:

```rust
let vec = vec![(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b')];
let uniq_by_fst_comp = || {
    let mut seen = std::collections::HashSet::new();
    vec.iter().copied().filter(move |x| seen.insert(x.0))
};

assert_eq!(uniq_by_fst_comp().last(), Some((2, 'a')));
assert_eq!(uniq_by_fst_comp().next_back(), Some((2, 'b')));

assert_eq!(
    uniq_by_fst_comp().fold(vec![], |mut v, x| {v.push(x); v}),
    vec![(1, 'a'), (2, 'a')]
);
assert_eq!(
    uniq_by_fst_comp().rfold(vec![], |mut v, x| {v.push(x); v}),
    vec![(2, 'b'), (1, 'c')]
);
```

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#138)

🔬This is a nightly-only experimental API. (`iter_advance_by` [#77404](https://github.com/rust-lang/rust/issues/77404))

Advances the iterator from the back by `n` elements.

`advance_back_by` is the reverse version of [`advance_by`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.advance_by "method std::iter::Iterator::advance_by"). This method will eagerly skip `n` elements starting from the back by calling [`next_back`](https://doc.rust-lang.org/stable/std/iter/trait.DoubleEndedIterator.html#tymethod.next_back "method std::iter::DoubleEndedIterator::next_back") up to `n` times until [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is encountered.

`advance_back_by(n)` will return `Ok(())` if the iterator successfully advances by `n` elements, or a `Err(NonZero<usize>)` with value `k` if [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is encountered, where `k` is remaining number of steps that could not be advanced because the iterator ran out. If `self` is empty and `n` is non-zero, then this returns `Err(n)`. Otherwise, `k` is always less than `n`.

Calling `advance_back_by(0)` can do meaningful work, for example [`Flatten`](https://doc.rust-lang.org/stable/std/iter/struct.Flatten.html "struct std::iter::Flatten") can advance its outer iterator until it finds an inner iterator that is not empty, which then often allows it to return a more accurate `size_hint()` than in its initial state.

##### [§](#examples-2)Examples

Basic usage:

```rust
#![feature(iter_advance_by)]

use std::num::NonZero;

let a = [3, 4, 5, 6];
let mut iter = a.iter();

assert_eq!(iter.advance_back_by(2), Ok(()));
assert_eq!(iter.next_back(), Some(&4));
assert_eq!(iter.advance_back_by(0), Ok(()));
assert_eq!(iter.advance_back_by(100), Err(NonZero::new(99).unwrap())); // only `&3` was skipped
```

1.37.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#191)

Returns the `n`th element from the end of the iterator.

This is essentially the reversed version of [`Iterator::nth()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.nth "method std::iter::Iterator::nth"). Although like most indexing operations, the count starts from zero, so `nth_back(0)` returns the first value from the end, `nth_back(1)` the second, and so on.

Note that all elements between the end and the returned element will be consumed, including the returned element. This also means that calling `nth_back(0)` multiple times on the same iterator will return different elements.

`nth_back()` will return [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if `n` is greater than or equal to the length of the iterator.

##### [§](#examples-3)Examples

Basic usage:

```rust
let a = [1, 2, 3];
assert_eq!(a.iter().nth_back(2), Some(&1));
```

Calling `nth_back()` multiple times doesn’t rewind the iterator:

```rust
let a = [1, 2, 3];

let mut iter = a.iter();

assert_eq!(iter.nth_back(1), Some(&2));
assert_eq!(iter.nth_back(1), None);
```

Returning `None` if there are less than `n + 1` elements:

```rust
let a = [1, 2, 3];
assert_eq!(a.iter().nth_back(10), None);
```

1.27.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#230-234)

This is the reverse version of [`Iterator::try_fold()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.try_fold "method std::iter::Iterator::try_fold"): it takes elements starting from the back of the iterator.

##### [§](#examples-4)Examples

Basic usage:

```rust
let a = ["1", "2", "3"];
let sum = a.iter()
    .map(|&s| s.parse::<i32>())
    .try_rfold(0, |acc, x| x.and_then(|y| Ok(acc + y)));
assert_eq!(sum, Ok(6));
```

Short-circuiting:

```rust
let a = ["1", "rust", "3"];
let mut it = a.iter();
let sum = it
    .by_ref()
    .map(|&s| s.parse::<i32>())
    .try_rfold(0, |acc, x| x.and_then(|y| Ok(acc + y)));
assert!(sum.is_err());

// Because it short-circuited, the remaining elements are still
// available through the iterator.
assert_eq!(it.next_back(), Some(&"1"));
```

1.27.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#301-304)

An iterator method that reduces the iterator’s elements to a single, final value, starting from the back.

This is the reverse version of [`Iterator::fold()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.fold "method std::iter::Iterator::fold"): it takes elements starting from the back of the iterator.

`rfold()` takes two arguments: an initial value, and a closure with two arguments: an ‘accumulator’, and an element. The closure returns the value that the accumulator should have for the next iteration.

The initial value is the value the accumulator will have on the first call.

After applying this closure to every element of the iterator, `rfold()` returns the accumulator.

This operation is sometimes called ‘reduce’ or ‘inject’.

Folding is useful whenever you have a collection of something, and want to produce a single value from it.

Note: `rfold()` combines elements in a *right-associative* fashion. For associative operators like `+`, the order the elements are combined in is not important, but for non-associative operators like `-` the order will affect the final result. For a *left-associative* version of `rfold()`, see [`Iterator::fold()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.fold "method std::iter::Iterator::fold").

##### [§](#examples-5)Examples

Basic usage:

```rust
let a = [1, 2, 3];

// the sum of all of the elements of a
let sum = a.iter()
           .rfold(0, |acc, &x| acc + x);

assert_eq!(sum, 6);
```

This example demonstrates the right-associative nature of `rfold()`: it builds a string, starting with an initial value and continuing with each element from the back until the front:

```rust
let numbers = [1, 2, 3, 4, 5];

let zero = "0".to_string();

let result = numbers.iter().rfold(zero, |acc, &x| {
    format!("({x} + {acc})")
});

assert_eq!(result, "(1 + (2 + (3 + (4 + (5 + 0)))))");
```

1.27.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/double_ended.rs.html#366-369)

Searches for an element of an iterator from the back that satisfies a predicate.

`rfind()` takes a closure that returns `true` or `false`. It applies this closure to each element of the iterator, starting at the end, and if any of them return `true`, then `rfind()` returns [`Some(element)`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some"). If they all return `false`, it returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

`rfind()` is short-circuiting; in other words, it will stop processing as soon as the closure returns `true`.

Because `rfind()` takes a reference, and many iterators iterate over references, this leads to a possibly confusing situation where the argument is a double reference. You can see this effect in the examples below, with `&&x`.

##### [§](#examples-6)Examples

Basic usage:

```rust
let a = [1, 2, 3];

assert_eq!(a.into_iter().rfind(|&x| x == 2), Some(2));
assert_eq!(a.into_iter().rfind(|&x| x == 5), None);
```

Iterating over references:

```rust
let a = [1, 2, 3];

// `iter()` yields references i.e. `&i32` and `rfind()` takes a
// reference to each element.
assert_eq!(a.iter().rfind(|&&x| x == 2), Some(&2));
assert_eq!(a.iter().rfind(|&&x| x == 5), None);
```

Stopping at the first `true`:

```rust
let a = [1, 2, 3];

let mut iter = a.iter();

assert_eq!(iter.rfind(|&&x| x == 2), Some(&2));

// we can still use `iter`, as there are more elements.
assert_eq!(iter.next_back(), Some(&1));
```