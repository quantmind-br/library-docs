---
title: Structs - The Rust Reference
url: https://doc.rust-lang.org/reference/items/structs.html#grammar-StructFields
source: crawler
fetched_at: 2026-05-06T21:28:58.209940363-03:00
rendered_js: false
word_count: 187
summary: This document defines the syntax and behavioral characteristics of structs, tuple structs, and unit-like structs in the Rust programming language.
tags:
    - rust-programming
    - structs
    - data-types
    - language-reference
    - memory-layout
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Structs](#structs)

A *struct* is a nominal [struct type](https://doc.rust-lang.org/reference/types/struct.html) defined with the keyword `struct`.

A struct declaration defines the given name in the [type namespace](https://doc.rust-lang.org/reference/names/namespaces.html) of the module or block where it is located.

An example of a `struct` item and its use:

```rust
#![allow(unused)]
fn main() {
struct Point {x: i32, y: i32}
let p = Point {x: 10, y: 11};
let px: i32 = p.x;
}
```

A *tuple struct* is a nominal [tuple type](https://doc.rust-lang.org/reference/types/tuple.html), and is also defined with the keyword `struct`. In addition to defining a type, it also defines a constructor of the same name in the [value namespace](https://doc.rust-lang.org/reference/names/namespaces.html). The constructor is a function which can be called to create a new instance of the struct. For example:

```rust
#![allow(unused)]
fn main() {
struct Point(i32, i32);
let p = Point(10, 11);
let px: i32 = match p { Point(x, _) => x };
}
```

A *unit-like struct* is a struct without any fields, defined by leaving off the list of fields entirely. Such a struct implicitly defines a [constant](https://doc.rust-lang.org/reference/items/constant-items.html) of its type with the same name. For example:

```rust
#![allow(unused)]
fn main() {
struct Cookie;
let c = [Cookie, Cookie {}, Cookie, Cookie {}];
}
```

is equivalent to

```rust
#![allow(unused)]
fn main() {
struct Cookie {}
const Cookie: Cookie = Cookie {};
let c = [Cookie, Cookie {}, Cookie, Cookie {}];
}
```

The precise memory layout of a struct is not specified. One can specify a particular layout using the [`repr` attribute](https://doc.rust-lang.org/reference/type-layout.html#representations).