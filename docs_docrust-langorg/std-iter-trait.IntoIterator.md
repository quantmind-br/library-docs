---
title: IntoIterator in std::iter - Rust
url: https://doc.rust-lang.org/std/iter/trait.IntoIterator.html
source: crawler
fetched_at: 2026-05-06T21:23:17.850134236-03:00
rendered_js: false
word_count: 142
summary: This document defines the IntoIterator trait in Rust, which enables types to be converted into iterators and supports usage within for loops.
tags:
    - rust
    - traits
    - iterators
    - collections
    - language-features
category: reference
---

## Trait IntoIterator

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/92476 "Tracking issue for const_iter")) · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#283)

```rust
pub trait IntoIterator {
    type Item;
    type IntoIter: Iterator<Item = Self::Item>;

    // Required method
    fn into_iter(self) -> Self::IntoIter;
}
```

Expand description

Conversion into an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator").

By implementing `IntoIterator` for a type, you define how it will be converted to an iterator. This is common for types which describe a collection of some kind.

One benefit of implementing `IntoIterator` is that your type will [work with Rust’s `for` loop syntax](https://doc.rust-lang.org/std/iter/index.html#for-loops-and-intoiterator "mod std::iter").

See also: [`FromIterator`](https://doc.rust-lang.org/std/iter/trait.FromIterator.html "trait std::iter::FromIterator").

## [§](#examples)Examples

Basic usage:

```rust
let v = [1, 2, 3];
let mut iter = v.into_iter();

assert_eq!(Some(1), iter.next());
assert_eq!(Some(2), iter.next());
assert_eq!(Some(3), iter.next());
assert_eq!(None, iter.next());
```

Implementing `IntoIterator` for your type:

```rust
// A sample collection, that's just a wrapper over Vec<T>
#[derive(Debug)]
struct MyCollection(Vec<i32>);

// Let's give it some methods so we can create one and add things
// to it.
impl MyCollection {
    fn new() -> MyCollection {
        MyCollection(Vec::new())
    }

    fn add(&mut self, elem: i32) {
        self.0.push(elem);
    }
}

// and we'll implement IntoIterator
impl IntoIterator for MyCollection {
    type Item = i32;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.into_iter()
    }
}

// Now we can make a new collection...
let mut c = MyCollection::new();

// ... add some stuff to it ...
c.add(0);
c.add(1);
c.add(2);

// ... and then turn it into an Iterator:
for (i, n) in c.into_iter().enumerate() {
    assert_eq!(i as i32, n);
}
```

It is common to use `IntoIterator` as a trait bound. This allows the input collection type to change, so long as it is still an iterator. Additional bounds can be specified by restricting on `Item`:

```rust
fn collect_as_strings<T>(collection: T) -> Vec<String>
where
    T: IntoIterator,
    T::Item: std::fmt::Debug,
{
    collection
        .into_iter()
        .map(|item| format!("{item:?}"))
        .collect()
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#287)

The type of the elements being iterated over.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#291)

Which kind of iterator are we turning this into?

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#312)

Creates an iterator from a value.

See the [module-level documentation](https://doc.rust-lang.org/std/iter/index.html "mod std::iter") for more.

##### [§](#examples-1)Examples

```rust
let v = [1, 2, 3];
let mut iter = v.into_iter();

assert_eq!(Some(1), iter.next());
assert_eq!(Some(2), iter.next());
assert_eq!(Some(3), iter.next());
assert_eq!(None, iter.next());
```