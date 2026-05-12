---
title: Default in std::default - Rust
url: https://doc.rust-lang.org/std/default/trait.Default.html
source: crawler
fetched_at: 2026-05-06T21:23:14.423841381-03:00
rendered_js: false
word_count: 253
summary: This document explains the Default trait in Rust, which is used to define a standard initial or fallback value for a data type.
tags:
    - rust
    - trait
    - default
    - data-types
    - struct
    - enum
    - derive-macro
category: reference
---

## Trait Default

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/default.rs.html#107)

```rust
pub trait Default: Sized {
    // Required method
    fn default() -> Self;
}
```

Expand description

A trait for giving a type a useful default value.

Sometimes, you want to fall back to some kind of default value, and don’t particularly care what it is. This comes up often with `struct`s that define a set of options:

```rust
struct SomeOptions {
    foo: i32,
    bar: f32,
}
```

How can we define some default values? You can use `Default`:

```rust
#[derive(Default)]
struct SomeOptions {
    foo: i32,
    bar: f32,
}

fn main() {
    let options: SomeOptions = Default::default();
}
```

Now, you get all of the default values. Rust implements `Default` for various primitive types.

If you want to override a particular option, but still retain the other defaults:

```rust
fn main() {
    let options = SomeOptions { foo: 42, ..Default::default() };
}
```

### [§](#derivable)Derivable

This trait can be used with `#[derive]` if all of the type’s fields implement `Default`. When `derive`d, it will use the default value for each field’s type.

#### [§](#enums)`enum`s

When using `#[derive(Default)]` on an `enum`, you need to choose which unit variant will be default. You do this by placing the `#[default]` attribute on the variant.

```rust
#[derive(Default)]
enum Kind {
    #[default]
    A,
    B,
    C,
}
```

You cannot use the `#[default]` attribute on non-unit or non-exhaustive variants.

The `#[default]` attribute was stabilized in Rust 1.62.0.

### [§](#how-can-i-implement-default)How can I implement `Default`?

Provide an implementation for the `default()` method that returns the value of your type that should be the default:

```rust
enum Kind {
    A,
    B,
    C,
}

impl Default for Kind {
    fn default() -> Self { Kind::A }
}
```

## [§](#examples)Examples

```rust
#[derive(Default)]
struct SomeOptions {
    foo: i32,
    bar: f32,
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/default.rs.html#139)

Returns the “default value” for a type.

Default values are often some kind of initial value, identity value, or anything else that may make sense as a default.

##### [§](#examples-1)Examples

Using built-in default values:

```rust
let i: i8 = Default::default();
let (x, y): (Option<String>, f64) = Default::default();
let (a, b, (c, d)): (i32, u32, (bool, bool)) = Default::default();
```

Making your own:

```rust
enum Kind {
    A,
    B,
    C,
}

impl Default for Kind {
    fn default() -> Self { Kind::A }
}
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*