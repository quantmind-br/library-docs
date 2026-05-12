---
title: Display in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.Display.html#tymethod.fmt
source: crawler
fetched_at: 2026-05-06T21:23:15.429455142-03:00
rendered_js: false
word_count: 388
summary: This document defines the Display trait in Rust, which is used for creating user-facing textual representations of data types using the {} format specifier.
tags:
    - rust
    - fmt
    - display-trait
    - formatting
    - string-conversion
    - traits
category: reference
---

## Trait Display

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1186)

```rust
pub trait Display {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

Expand description

Format trait for an empty format, `{}`.

Implementing this trait for a type will automatically implement the [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) trait for the type, allowing the usage of the [`.to_string()`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string) method. Prefer implementing the `Display` trait for a type, rather than [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html).

`Display` is similar to [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug"), but `Display` is for user-facing output, and so cannot be derived.

For more information on formatters, see [the module-level documentation](https://doc.rust-lang.org/std/fmt/index.html).

## [§](#completeness-and-parseability)Completeness and parseability

`Display` for a type might not necessarily be a lossless or complete representation of the type. It may omit internal state, precision, or other information the type does not consider important for user-facing output, as determined by the type. As such, the output of `Display` might not be possible to parse, and even if it is, the result of parsing might not exactly match the original value.

However, if a type has a lossless `Display` implementation whose output is meant to be conveniently machine-parseable and not just meant for human consumption, then the type may wish to accept the same format in `FromStr`, and document that usage. Having both `Display` and `FromStr` implementations where the result of `Display` cannot be parsed with `FromStr` may surprise users.

## [§](#internationalization)Internationalization

Because a type can only have one `Display` implementation, it is often preferable to only implement `Display` when there is a single most “obvious” way that values can be formatted as text. This could mean formatting according to the “invariant” culture and “undefined” locale, or it could mean that the type display is designed for a specific culture/locale, such as developer logs.

If not all values have a justifiably canonical textual format or if you want to support alternative formats not covered by the standard set of possible [formatting traits](https://doc.rust-lang.org/std/fmt/index.html#formatting-traits), the most flexible approach is display adapters: methods like [`str::escape_default`](https://doc.rust-lang.org/std/primitive.str.html#method.escape_default "method str::escape_default") or [`Path::display`](https://doc.rust-lang.org/std/path/struct.Path.html#method.display) which create a wrapper implementing `Display` to output the specific display format.

## [§](#examples)Examples

Implementing `Display` on a type:

```rust
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

let origin = Point { x: 0, y: 0 };

assert_eq!(format!("The origin is: {origin}"), "The origin is: (0, 0)");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1211)

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

impl fmt::Display for Position {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.longitude, self.latitude)
    }
}

assert_eq!(
    "(1.987, 2.983)",
    format!("{}", Position { longitude: 1.987, latitude: 2.983, }),
);
```