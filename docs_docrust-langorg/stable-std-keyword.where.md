---
title: where - Rust
url: https://doc.rust-lang.org/stable/std/keyword.where.html
source: crawler
fetched_at: 2026-05-06T21:28:58.959660757-03:00
rendered_js: false
word_count: 142
summary: This document explains the use of the where clause in Rust to define complex constraints on generic type parameters and lifetimes.
tags:
    - rust
    - generics
    - lifetimes
    - where-clause
    - trait-bounds
    - type-systems
category: concept
---

Expand description

Add constraints that must be upheld to use an item.

`where` allows specifying constraints on lifetime and generic parameters. The [RFC](https://github.com/rust-lang/rfcs/blob/master/text/0135-where.md) introducing `where` contains detailed information about the keyword.

## [§](#examples)Examples

`where` can be used for constraints with traits:

```rust
fn new<T: Default>() -> T {
    T::default()
}

fn new_where<T>() -> T
where
    T: Default,
{
    T::default()
}

assert_eq!(0.0, new());
assert_eq!(0.0, new_where());

assert_eq!(0, new());
assert_eq!(0, new_where());
```

`where` can also be used for lifetimes.

This compiles because `longer` outlives `shorter`, thus the constraint is respected:

```rust
fn select<'short, 'long>(s1: &'short str, s2: &'long str, second: bool) -> &'short str
where
    'long: 'short,
{
    if second { s2 } else { s1 }
}

let outer = String::from("Long living ref");
let longer = &outer;
{
    let inner = String::from("Short living ref");
    let shorter = &inner;

    assert_eq!(select(shorter, longer, false), shorter);
    assert_eq!(select(shorter, longer, true), longer);
}
```

On the other hand, this will not compile because the `where 'b: 'a` clause is missing: the `'b` lifetime is not known to live at least as long as `'a` which means this function cannot ensure it always returns a valid reference:

[ⓘ](# "This example deliberately fails to compile")

```rust
fn select<'a, 'b>(s1: &'a str, s2: &'b str, second: bool) -> &'a str
{
    if second { s2 } else { s1 }
}
```

`where` can also be used to express more complicated constraints that cannot be written with the `<T: Trait>` syntax:

```rust
fn first_or_default<I>(mut i: I) -> I::Item
where
    I: Iterator,
    I::Item: Default,
{
    i.next().unwrap_or_else(I::Item::default)
}

assert_eq!(first_or_default([1, 2, 3].into_iter()), 1);
assert_eq!(first_or_default(Vec::<i32>::new().into_iter()), 0);
```

`where` is available anywhere generic and lifetime parameters are available, as can be seen with the [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") type from the standard library:

```rust
pub enum Cow<'a, B>
where
    B: ToOwned + ?Sized,
{
    Borrowed(&'a B),
    Owned(<B as ToOwned>::Owned),
}
```