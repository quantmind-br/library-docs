---
title: std::async_iter - Rust
url: https://doc.rust-lang.org/std/async_iter/index.html
source: crawler
fetched_at: 2026-05-06T21:32:26.598923537-03:00
rendered_js: false
word_count: 544
summary: This document provides an overview of the asynchronous iterator module in Rust, explaining the core AsyncIterator trait, its implementation, and the concept of lazy evaluation in asynchronous collections.
tags:
    - rust
    - async-rust
    - async-iterator
    - asynchronous-programming
    - traits
    - experimental-api
category: reference
---

🔬This is a nightly-only experimental API. (`async_iterator` [#79024](https://github.com/rust-lang/rust/issues/79024))

Expand description

Composable asynchronous iteration.

If you’ve found yourself with an asynchronous collection of some kind, and needed to perform an operation on the elements of said collection, you’ll quickly run into ‘async iterators’. Async Iterators are heavily used in idiomatic asynchronous Rust code, so it’s worth becoming familiar with them.

Before explaining more, let’s talk about how this module is structured:

## [§](#organization)Organization

This module is largely organized by type:

- [Traits](#traits) are the core portion: these traits define what kind of async iterators exist and what you can do with them. The methods of these traits are worth putting some extra study time into.
- Functions provide some helpful ways to create some basic async iterators.
- Structs are often the return types of the various methods on this module’s traits. You’ll usually want to look at the method that creates the `struct`, rather than the `struct` itself. For more detail about why, see ‘[Implementing Async Iterator](#implementing-async-iterator)’.

That’s it! Let’s dig into async iterators.

## [§](#async-iterators)Async Iterators

The heart and soul of this module is the [`AsyncIterator`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html "trait std::async_iter::AsyncIterator") trait. The core of [`AsyncIterator`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html "trait std::async_iter::AsyncIterator") looks like this:

```rust
trait AsyncIterator {
    type Item;
    fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>>;
}
```

Unlike `Iterator`, `AsyncIterator` makes a distinction between the [`poll_next`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html#tymethod.poll_next "method std::async_iter::AsyncIterator::poll_next") method which is used when implementing an `AsyncIterator`, and a (to-be-implemented) `next` method which is used when consuming an async iterator. Consumers of `AsyncIterator` only need to consider `next`, which when called, returns a future which yields `Option<AsyncIterator::Item>`.

The future returned by `next` will yield `Some(Item)` as long as there are elements, and once they’ve all been exhausted, will yield `None` to indicate that iteration is finished. If we’re waiting on something asynchronous to resolve, the future will wait until the async iterator is ready to yield again.

Individual async iterators may choose to resume iteration, and so calling `next` again may or may not eventually yield `Some(Item)` again at some point.

[`AsyncIterator`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html "trait std::async_iter::AsyncIterator")’s full definition includes a number of other methods as well, but they are default methods, built on top of [`poll_next`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html#tymethod.poll_next "method std::async_iter::AsyncIterator::poll_next"), and so you get them for free.

## [§](#implementing-async-iterator)Implementing Async Iterator

Creating an async iterator of your own involves two steps: creating a `struct` to hold the async iterator’s state, and then implementing [`AsyncIterator`](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html "trait std::async_iter::AsyncIterator") for that `struct`.

Let’s make an async iterator named `Counter` which counts from `1` to `5`:

```rust
#![feature(async_iterator)]

// First, the struct:

/// An async iterator which counts from one to five
struct Counter {
    count: usize,
}

// we want our count to start at one, so let's add a new() method to help.
// This isn't strictly necessary, but is convenient. Note that we start
// `count` at zero, we'll see why in `poll_next()`'s implementation below.
impl Counter {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}

// Then, we implement `AsyncIterator` for our `Counter`:

impl AsyncIterator for Counter {
    // we will be counting with usize
    type Item = usize;

    // poll_next() is the only required method
    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {
        // Increment our count. This is why we started at zero.
        self.count += 1;

        // Check to see if we've finished counting or not.
        if self.count < 6 {
            Poll::Ready(Some(self.count))
        } else {
            Poll::Ready(None)
        }
    }
}
```

## [§](#laziness)Laziness

Async iterators are *lazy*. This means that just creating an async iterator doesn’t *do* a whole lot. Nothing really happens until you call `poll_next`. This is sometimes a source of confusion when creating an async iterator solely for its side effects. The compiler will warn us about this kind of behavior:

```text
warning: unused result that must be used: async iterators do nothing unless polled
```

[FromIter](https://doc.rust-lang.org/std/async_iter/struct.FromIter.html "struct std::async_iter::FromIter")Experimental

An async iterator that was created from iterator.

[AsyncIterator](https://doc.rust-lang.org/std/async_iter/trait.AsyncIterator.html "trait std::async_iter::AsyncIterator")Experimental

A trait for dealing with asynchronous iterators.

[IntoAsyncIterator](https://doc.rust-lang.org/std/async_iter/trait.IntoAsyncIterator.html "trait std::async_iter::IntoAsyncIterator")Experimental

Converts something into an async iterator

[from\_iter](https://doc.rust-lang.org/std/async_iter/fn.from_iter.html "fn std::async_iter::from_iter")Experimental

Converts an iterator into an async iterator.