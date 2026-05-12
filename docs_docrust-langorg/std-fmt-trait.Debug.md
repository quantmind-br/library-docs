---
title: Debug in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.Debug.html#tymethod.fmt
source: crawler
fetched_at: 2026-05-06T21:23:12.840183303-03:00
rendered_js: false
word_count: 302
summary: The Debug trait provides a mechanism for programmer-facing formatting of types, enabling automated representation via derive or manual implementation for custom debugging outputs.
tags:
    - rust
    - trait
    - formatting
    - debugging
    - derive
    - fmt
category: reference
---

## Trait Debug

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1052)

```rust
pub trait Debug {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

Expand description

`?` formatting.

`Debug` should format the output in a programmer-facing, debugging context.

Generally speaking, you should just `derive` a `Debug` implementation.

When used with the alternate format specifier `#?`, the output is pretty-printed.

For more information on formatters, see [the module-level documentation](https://doc.rust-lang.org/std/fmt/index.html).

This trait can be used with `#[derive]` if all fields implement `Debug`. When `derive`d for structs, it will use the name of the `struct`, then `{`, then a comma-separated list of each field’s name and `Debug` value, then `}`. For `enum`s, it will use the name of the variant and, if applicable, `(`, then the `Debug` values of the fields, then `)`.

## [§](#stability)Stability

Derived `Debug` formats are not stable, and so may change with future Rust versions. Additionally, `Debug` implementations of types provided by the standard library (`std`, `core`, `alloc`, etc.) are not stable, and may also change with future Rust versions.

## [§](#examples)Examples

Deriving an implementation:

```rust
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

let origin = Point { x: 0, y: 0 };

assert_eq!(
    format!("The origin is: {origin:?}"),
    "The origin is: Point { x: 0, y: 0 }",
);
```

Manually implementing:

```rust
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Point")
         .field("x", &self.x)
         .field("y", &self.y)
         .finish()
    }
}

let origin = Point { x: 0, y: 0 };

assert_eq!(
    format!("The origin is: {origin:?}"),
    "The origin is: Point { x: 0, y: 0 }",
);
```

There are a number of helper methods on the [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") struct to help you with manual implementations, such as [`debug_struct`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html#method.debug_struct "method std::fmt::Formatter::debug_struct").

Types that do not wish to use the standard suite of debug representations provided by the `Formatter` trait (`debug_struct`, `debug_tuple`, `debug_list`, `debug_set`, `debug_map`) can do something totally custom by manually writing an arbitrary representation to the `Formatter`.

```rust
impl fmt::Debug for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Point [{} {}]", self.x, self.y)
    }
}
```

`Debug` implementations using either `derive` or the debug builder API on [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") support pretty-printing using the alternate flag: `{:#?}`.

Pretty-printing with `#?`:

```rust
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

let origin = Point { x: 0, y: 0 };

let expected = "The origin is: Point {
    x: 0,
    y: 0,
}";
assert_eq!(format!("The origin is: {origin:#?}"), expected);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1083)

Formats the value using the given formatter.

##### [§](#errors)Errors

This function should return [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if, and only if, the provided [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). String formatting is considered an infallible operation; this function only returns a [`Result`](https://doc.rust-lang.org/std/fmt/type.Result.html "type std::fmt::Result") because writing to the underlying stream might fail and it must provide a way to propagate the fact that an error has occurred back up the stack.

##### [§](#examples-1)Examples

```rust
use std::fmt;

struct Position {
    longitude: f32,
    latitude: f32,
}

impl fmt::Debug for Position {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_tuple("")
         .field(&self.longitude)
         .field(&self.latitude)
         .finish()
    }
}

let position = Position { longitude: 1.987, latitude: 2.983 };
assert_eq!(format!("{position:?}"), "(1.987, 2.983)");

assert_eq!(format!("{position:#?}"), "(
    1.987,
    2.983,
)");
```