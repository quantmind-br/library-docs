---
title: FromStr in std::str - Rust
url: https://doc.rust-lang.org/std/str/trait.FromStr.html
source: crawler
fetched_at: 2026-05-06T21:22:53.452681986-03:00
rendered_js: false
word_count: 314
summary: The FromStr trait provides a standardized interface for parsing string slices into typed values, enabling integration with the str::parse method.
tags:
    - rust
    - trait
    - string-parsing
    - type-conversion
    - std-library
category: reference
---

## Trait FromStr

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#837)

```rust
pub trait FromStr: Sized {
    type Err;

    // Required method
    fn from_str(s: &str) -> Result<Self, Self::Err>;
}
```

Expand description

Parse a value from a string

`FromStr`’s [`from_str`](https://doc.rust-lang.org/std/str/trait.FromStr.html#tymethod.from_str "associated function std::str::FromStr::from_str") method is often used implicitly, through [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str")’s [`parse`](https://doc.rust-lang.org/std/primitive.str.html#method.parse "method str::parse") method. See [`parse`](https://doc.rust-lang.org/std/primitive.str.html#method.parse "method str::parse")’s documentation for examples.

`FromStr` does not have a lifetime parameter, and so you can only parse types that do not contain a lifetime parameter themselves. In other words, you can parse an `i32` with `FromStr`, but not a `&i32`. You can parse a struct that contains an `i32`, but not one that contains an `&i32`.

## [§](#input-format-and-round-tripping)Input format and round-tripping

The input format expected by a type’s `FromStr` implementation depends on the type. Check the type’s documentation for the input formats it knows how to parse. Note that the input format of a type’s `FromStr` implementation might not necessarily accept the output format of its `Display` implementation, and even if it does, the `Display` implementation may not be lossless so the round-trip may lose information.

However, if a type has a lossless `Display` implementation whose output is meant to be conveniently machine-parseable and not just meant for human consumption, then the type may wish to accept the same format in `FromStr`, and document that usage. Having both `Display` and `FromStr` implementations where the result of `Display` cannot be parsed with `FromStr` may surprise users.

## [§](#examples)Examples

Basic implementation of `FromStr` on an example `Point` type:

```rust
use std::str::FromStr;

#[derive(Debug, PartialEq)]
struct Point {
    x: i32,
    y: i32
}

#[derive(Debug, PartialEq, Eq)]
struct ParsePointError;

impl FromStr for Point {
    type Err = ParsePointError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (x, y) = s
            .strip_prefix('(')
            .and_then(|s| s.strip_suffix(')'))
            .and_then(|s| s.split_once(','))
            .ok_or(ParsePointError)?;

        let x_fromstr = x.parse::<i32>().map_err(|_| ParsePointError)?;
        let y_fromstr = y.parse::<i32>().map_err(|_| ParsePointError)?;

        Ok(Point { x: x_fromstr, y: y_fromstr })
    }
}

let expected = Ok(Point { x: 1, y: 2 });
// Explicit call
assert_eq!(Point::from_str("(1,2)"), expected);
// Implicit calls, through parse
assert_eq!("(1,2)".parse(), expected);
assert_eq!("(1,2)".parse::<Point>(), expected);
// Invalid input string
assert!(Point::from_str("(1 2)").is_err());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#840)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/traits.rs.html#862)

Parses a string `s` to return a value of this type.

If parsing succeeds, return the value inside [`Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok"), otherwise when the string is ill-formatted return an error specific to the inside [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). The error type is specific to the implementation of the trait.

##### [§](#examples-1)Examples

Basic usage with [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32"), a type that implements `FromStr`:

```rust
use std::str::FromStr;

let s = "5";
let x = i32::from_str(s).unwrap();

assert_eq!(5, x);
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*