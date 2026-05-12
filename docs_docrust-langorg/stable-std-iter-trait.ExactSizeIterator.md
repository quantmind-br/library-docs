---
title: ExactSizeIterator in std::iter - Rust
url: https://doc.rust-lang.org/stable/std/iter/trait.ExactSizeIterator.html
source: crawler
fetched_at: 2026-05-06T21:25:39.518654201-03:00
rendered_js: false
word_count: 361
summary: This document defines the ExactSizeIterator trait in Rust, which is used for iterators that can provide an exact count of their remaining elements.
tags:
    - rust
    - iterator
    - traits
    - programming
    - collections
category: reference
---

## Trait ExactSizeIterator

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/exact_size.rs.html#86)

```rust
pub trait ExactSizeIterator: Iterator {
    // Provided methods
    fn len(&self) -> usize { ... }
    fn is_empty(&self) -> bool { ... }
}
```

Expand description

An iterator that knows its exact length.

Many [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator")s don’t know how many times they will iterate, but some do. If an iterator knows how many times it can iterate, providing access to that information can be useful. For example, if you want to iterate backwards, a good start is to know where the end is.

When implementing an `ExactSizeIterator`, you must also implement [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"). When doing so, the implementation of [`Iterator::size_hint`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint") *must* return the exact size of the iterator.

The [`len`](https://doc.rust-lang.org/stable/std/iter/trait.ExactSizeIterator.html#method.len "method std::iter::ExactSizeIterator::len") method has a default implementation, so you usually shouldn’t implement it. However, you may be able to provide a more performant implementation than the default, so overriding it in this case makes sense.

Note that this trait is a safe trait and as such does *not* and *cannot* guarantee that the returned length is correct. This means that `unsafe` code **must not** rely on the correctness of [`Iterator::size_hint`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint"). The unstable and unsafe [`TrustedLen`](https://doc.rust-lang.org/stable/std/iter/trait.TrustedLen.html "trait std::iter::TrustedLen") trait gives this additional guarantee.

## [§](#when-shouldnt-an-adapter-be-exactsizeiterator)When *shouldn’t* an adapter be `ExactSizeIterator`?

If an adapter makes an iterator *longer*, then it’s usually incorrect for that adapter to implement `ExactSizeIterator`. The inner exact-sized iterator might already be `usize::MAX`-long, and thus the length of the longer adapted iterator would no longer be exactly representable in `usize`.

This is why [`Chain<A, B>`](https://doc.rust-lang.org/stable/std/iter/struct.Chain.html "struct std::iter::Chain") isn’t `ExactSizeIterator`, even when `A` and `B` are both `ExactSizeIterator`.

## [§](#examples)Examples

Basic usage:

```rust
// a finite range knows exactly how many times it will iterate
let five = 0..5;

assert_eq!(5, five.len());
```

In the [module-level docs](https://doc.rust-lang.org/stable/std/iter/index.html "mod std::iter"), we implemented an [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"), `Counter`. Let’s implement `ExactSizeIterator` for it as well:

```rust
impl ExactSizeIterator for Counter {
    // We can easily calculate the remaining number of iterations.
    fn len(&self) -> usize {
        5 - self.count
    }
}

// And now we can use it!

let mut counter = Counter::new();

assert_eq!(5, counter.len());
let _ = counter.next();
assert_eq!(4, counter.len());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/exact_size.rs.html#116)

Returns the exact remaining length of the iterator.

The implementation ensures that the iterator will return exactly `len()` more times a [`Some(T)`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value, before returning [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"). This method has a default implementation, so you usually should not implement it directly. However, if you can provide a more efficient implementation, you can do so. See the [trait-level](https://doc.rust-lang.org/stable/std/iter/trait.ExactSizeIterator.html "trait std::iter::ExactSizeIterator") docs for an example.

This function has the same safety guarantees as the [`Iterator::size_hint`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint") function.

##### [§](#examples-1)Examples

Basic usage:

```rust
// a finite range knows exactly how many times it will iterate
let mut range = 0..5;

assert_eq!(5, range.len());
let _ = range.next();
assert_eq!(4, range.len());
```

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/exact_size.rs.html#148)

🔬This is a nightly-only experimental API. (`exact_size_is_empty` [#35428](https://github.com/rust-lang/rust/issues/35428))

Returns `true` if the iterator is empty.

This method has a default implementation using [`ExactSizeIterator::len()`](https://doc.rust-lang.org/stable/std/iter/trait.ExactSizeIterator.html#method.len "method std::iter::ExactSizeIterator::len"), so you don’t need to implement it yourself.

##### [§](#examples-2)Examples

Basic usage:

```rust
#![feature(exact_size_is_empty)]

let mut one_element = std::iter::once(0);
assert!(!one_element.is_empty());

assert_eq!(one_element.next(), Some(0));
assert!(one_element.is_empty());

assert_eq!(one_element.next(), None);
```