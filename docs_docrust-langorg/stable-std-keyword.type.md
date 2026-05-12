---
title: type - Rust
url: https://doc.rust-lang.org/stable/std/keyword.type.html
source: crawler
fetched_at: 2026-05-06T21:28:57.218007413-03:00
rendered_js: false
word_count: 39
summary: This document explains the syntax and usage of type aliases and associated types in the Rust programming language.
tags:
    - rust
    - type-alias
    - associated-types
    - programming-syntax
    - type-system
category: reference
---

Expand description

Define an [alias](https://doc.rust-lang.org/stable/reference/items/type-aliases.html) for an existing type.

The syntax is `type Name = ExistingType;`.

## [§](#examples)Examples

`type` does **not** create a new type:

```rust
type Meters = u32;
type Kilograms = u32;

let m: Meters = 3;
let k: Kilograms = 3;

assert_eq!(m, k);
```

A type can be generic:

```rust
type ArcMutex<T> = Arc<Mutex<T>>;
```

In traits, `type` is used to declare an [associated type](https://doc.rust-lang.org/stable/reference/items/associated-items.html#associated-types):

```rust
trait Iterator {
    // associated type declaration
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}

struct Once<T>(Option<T>);

impl<T> Iterator for Once<T> {
    // associated type definition
    type Item = T;
    fn next(&mut self) -> Option<Self::Item> {
        self.0.take()
    }
}
```