---
title: ToString in std::string - Rust
url: https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string
source: crawler
fetched_at: 2026-05-06T21:24:14.156491336-03:00
rendered_js: false
word_count: 93
summary: This document defines the ToString trait, which provides a mechanism to convert values into a String by leveraging the Display trait.
tags:
    - rust
    - string-conversion
    - trait
    - display-trait
    - standard-library
    - data-types
category: reference
---

## Trait ToString

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2866)

```rust
pub trait ToString {
    // Required method
    fn to_string(&self) -> String;
}
```

Expand description

A trait for converting a value to a `String`.

This trait is automatically implemented for any type which implements the [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") trait. As such, `ToString` shouldn’t be implemented directly: [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") should be implemented instead, and you get the `ToString` implementation for free.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2880)

Converts the given value to a `String`.

##### [§](#examples)Examples

```rust
let i = 5;
let five = String::from("5");

assert_eq!(five, i.to_string());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2891)[§](#impl-ToString-for-T)

#### [§](#panics)Panics

In this implementation, the `to_string` method panics if the `Display` implementation returns an error. This indicates an incorrect `Display` implementation since `fmt::Write for String` never returns an error itself.