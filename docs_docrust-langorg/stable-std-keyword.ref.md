---
title: ref - Rust
url: https://doc.rust-lang.org/stable/std/keyword.ref.html
source: crawler
fetched_at: 2026-05-06T21:28:54.895413698-03:00
rendered_js: false
word_count: 184
summary: This document explains the usage of the ref keyword in Rust pattern matching to borrow values instead of moving ownership, and distinguishes it from the reference operator.
tags:
    - rust
    - pattern-matching
    - ownership
    - borrowing
    - ref-keyword
    - memory-management
category: concept
---

Expand description

Bind by reference during pattern matching.

`ref` annotates pattern bindings to make them borrow rather than move. It is **not** a part of the pattern as far as matching is concerned: it does not affect *whether* a value is matched, only *how* it is matched.

By default, [`match`](https://doc.rust-lang.org/stable/std/keyword.match.html) statements consume all they can, which can sometimes be a problem, when you don’t really need the value to be moved and owned:

[ⓘ](# "This example deliberately fails to compile")

```rust
let maybe_name = Some(String::from("Alice"));
// The variable 'maybe_name' is consumed here ...
match maybe_name {
    Some(n) => println!("Hello, {n}"),
    _ => println!("Hello, world"),
}
// ... and is now unavailable.
println!("Hello again, {}", maybe_name.unwrap_or("world".into()));
```

Using the `ref` keyword, the value is only borrowed, not moved, making it available for use after the [`match`](https://doc.rust-lang.org/stable/std/keyword.match.html) statement:

```rust
let maybe_name = Some(String::from("Alice"));
// Using `ref`, the value is borrowed, not moved ...
match maybe_name {
    Some(ref n) => println!("Hello, {n}"),
    _ => println!("Hello, world"),
}
// ... so it's available here!
println!("Hello again, {}", maybe_name.unwrap_or("world".into()));
```

## [§](#-vs-ref)`&` vs `ref`

- `&` denotes that your pattern expects a reference to an object. Hence `&` is a part of said pattern: `&Foo` matches different objects than `Foo` does.
- `ref` indicates that you want a reference to an unpacked value. It is not matched against: `Foo(ref foo)` matches the same objects as `Foo(foo)`.

See also the [Reference](https://doc.rust-lang.org/stable/reference/patterns.html#identifier-patterns) for more information.