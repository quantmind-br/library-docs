---
title: Binary in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.Binary.html
source: crawler
fetched_at: 2026-05-06T21:29:52.887130978-03:00
rendered_js: false
word_count: 163
summary: This document defines the Binary trait in Rust, which is used to format values as binary numbers, including support for two's complement representations and alternate flag formatting.
tags:
    - rust
    - trait
    - binary-formatting
    - string-formatting
    - std-fmt
category: reference
---

## Trait Binary

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1321)

```rust
pub trait Binary {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

Expand description

`b` formatting.

The `Binary` trait should format its output as a number in binary.

For primitive signed integers ([`i8`](https://doc.rust-lang.org/std/primitive.i8.html "primitive i8") to [`i128`](https://doc.rust-lang.org/std/primitive.i128.html "primitive i128"), and [`isize`](https://doc.rust-lang.org/std/primitive.isize.html "primitive isize")), negative values are formatted as the two’s complement representation.

The alternate flag, `#`, adds a `0b` in front of the output.

For more information on formatters, see [the module-level documentation](https://doc.rust-lang.org/std/fmt/index.html).

## [§](#examples)Examples

Basic usage with [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32"):

```rust
let x = 42; // 42 is '101010' in binary

assert_eq!(format!("{x:b}"), "101010");
assert_eq!(format!("{x:#b}"), "0b101010");

assert_eq!(format!("{:b}", -16), "11111111111111111111111111110000");
```

Implementing `Binary` on a type:

```rust
use std::fmt;

struct Length(i32);

impl fmt::Binary for Length {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let val = self.0;

        fmt::Binary::fmt(&val, f) // delegate to i32's implementation
    }
}

let l = Length(107);

assert_eq!(format!("l as binary is: {l:b}"), "l as binary is: 1101011");

assert_eq!(
    // Note that the `0b` prefix added by `#` is included in the total width, so we
    // need to add two to correctly display all 32 bits.
    format!("l as binary is: {l:#034b}"),
    "l as binary is: 0b00000000000000000000000001101011"
);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1324)

Formats the value using the given formatter.

##### [§](#errors)Errors

This function should return [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if, and only if, the provided [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). String formatting is considered an infallible operation; this function only returns a [`Result`](https://doc.rust-lang.org/std/fmt/type.Result.html "type std::fmt::Result") because writing to the underlying stream might fail and it must provide a way to propagate the fact that an error has occurred back up the stack.