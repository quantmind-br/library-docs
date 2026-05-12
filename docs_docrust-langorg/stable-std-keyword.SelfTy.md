---
title: SelfTy - Rust
url: https://doc.rust-lang.org/stable/std/keyword.SelfTy.html
source: crawler
fetched_at: 2026-05-06T21:28:46.507950252-03:00
rendered_js: false
word_count: 47
summary: This document explains the usage of the Self keyword in Rust, which refers to the implementing type within traits, implementation blocks, and type definitions.
tags:
    - rust-programming
    - self-keyword
    - type-definitions
    - traits
    - implementation-blocks
    - language-syntax
category: concept
---

Expand description

The implementing type within a [`trait`](https://doc.rust-lang.org/stable/std/keyword.trait.html) or [`impl`](https://doc.rust-lang.org/stable/std/keyword.impl.html) block, or the current type within a type definition.

Within a type definition:

```rust
struct Node {
    elem: i32,
    // `Self` is a `Node` here.
    next: Option<Box<Self>>,
}
```

In an [`impl`](https://doc.rust-lang.org/stable/std/keyword.impl.html) block:

```rust
struct Foo(i32);

impl Foo {
    fn new() -> Self {
        Self(0)
    }
}

assert_eq!(Foo::new().0, Foo(0).0);
```

Generic parameters are implicit with `Self`:

```rust
struct Wrap<T> {
    elem: T,
}

impl<T> Wrap<T> {
    fn new(elem: T) -> Self {
        Self { elem }
    }
}
```

In a [`trait`](https://doc.rust-lang.org/stable/std/keyword.trait.html) definition and related [`impl`](https://doc.rust-lang.org/stable/std/keyword.impl.html) block:

```rust
trait Example {
    fn example() -> Self;
}

struct Foo(i32);

impl Example for Foo {
    fn example() -> Self {
        Self(42)
    }
}

assert_eq!(Foo::example().0, Foo(42).0);
```