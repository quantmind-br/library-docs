---
title: Extend in std::iter - Rust
url: https://doc.rust-lang.org/std/iter/trait.Extend.html
source: crawler
fetched_at: 2026-05-06T21:23:16.005472162-03:00
rendered_js: false
word_count: 183
summary: The Extend trait defines a standard interface for collections to append multiple elements from an iterator, allowing for custom collection types to integrate with Rust's iteration ecosystem.
tags:
    - rust
    - traits
    - iterators
    - collections
    - data-structures
    - generic-programming
category: reference
---

## Trait Extend

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#397)

```rust
pub trait Extend<A> {
    // Required method
    fn extend<T>(&mut self, iter: T)
       where T: IntoIterator<Item = A>;

    // Provided methods
    fn extend_one(&mut self, item: A) { ... }
    fn extend_reserve(&mut self, additional: usize) { ... }
}
```

Expand description

Extend a collection with the contents of an iterator.

Iterators produce a series of values, and collections can also be thought of as a series of values. The `Extend` trait bridges this gap, allowing you to extend a collection by including the contents of that iterator. When extending a collection with an already existing key, that entry is updated or, in the case of collections that permit multiple entries with equal keys, that entry is inserted.

## [§](#examples)Examples

Basic usage:

```rust
// You can extend a String with some chars:
let mut message = String::from("The first three letters are: ");

message.extend(&['a', 'b', 'c']);

assert_eq!("abc", &message[29..32]);
```

Implementing `Extend`:

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

// since MyCollection has a list of i32s, we implement Extend for i32
impl Extend<i32> for MyCollection {

    // This is a bit simpler with the concrete type signature: we can call
    // extend on anything which can be turned into an Iterator which gives
    // us i32s. Because we need i32s to put into MyCollection.
    fn extend<T: IntoIterator<Item=i32>>(&mut self, iter: T) {

        // The implementation is very straightforward: loop through the
        // iterator, and add() each element to ourselves.
        for elem in iter {
            self.add(elem);
        }
    }
}

let mut c = MyCollection::new();

c.add(5);
c.add(6);
c.add(7);

// let's extend our collection with three more numbers
c.extend(vec![1, 2, 3]);

// we've added these elements onto the end
assert_eq!("MyCollection([5, 6, 7, 1, 2, 3])", format!("{c:?}"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#416)

Extends a collection with the contents of an iterator.

As this is the only required method for this trait, the [trait-level](https://doc.rust-lang.org/std/iter/trait.Extend.html "trait std::iter::Extend") docs contain more details.

##### [§](#examples-1)Examples

```rust
// You can extend a String with some chars:
let mut message = String::from("abc");

message.extend(['d', 'e', 'f'].iter());

assert_eq!("abcdef", &message);
```

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements.

The default implementation does nothing.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*