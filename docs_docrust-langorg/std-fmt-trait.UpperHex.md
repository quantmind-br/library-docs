---
title: UpperHex in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.UpperHex.html
source: crawler
fetched_at: 2026-05-06T21:30:39.518558118-03:00
rendered_js: false
word_count: 142
summary: This document defines the UpperHex trait in Rust, which allows for custom formatting of types as uppercase hexadecimal strings, including support for the alternate prefix flag.
tags:
    - rust
    - traits
    - hexadecimal-formatting
    - fmt
    - programming-interfaces
category: reference
---

## Trait UpperHex

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1431)

```rust
pub trait UpperHex {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

Expand description

`X` formatting.

The `UpperHex` trait should format its output as a number in hexadecimal, with `A` through `F` in upper case.

For primitive signed integers (`i8` to `i128`, and `isize`), negative values are formatted as the two’s complement representation.

The alternate flag, `#`, adds a `0x` in front of the output.

For more information on formatters, see [the module-level documentation](https://doc.rust-lang.org/std/fmt/index.html).

## [§](#examples)Examples

Basic usage with `i32`:

```rust
let y = 42; // 42 is '2A' in hex

assert_eq!(format!("{y:X}"), "2A");
assert_eq!(format!("{y:#X}"), "0x2A");

assert_eq!(format!("{:X}", -16), "FFFFFFF0");
```

Implementing `UpperHex` on a type:

```rust
use std::fmt;

struct Length(i32);

impl fmt::UpperHex for Length {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let val = self.0;

        fmt::UpperHex::fmt(&val, f) // delegate to i32's implementation
    }
}

let l = Length(i32::MAX);

assert_eq!(format!("l as hex is: {l:X}"), "l as hex is: 7FFFFFFF");

assert_eq!(format!("l as hex is: {l:#010X}"), "l as hex is: 0x7FFFFFFF");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1434)

Formats the value using the given formatter.

##### [§](#errors)Errors

This function should return [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if, and only if, the provided [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). String formatting is considered an infallible operation; this function only returns a [`Result`](https://doc.rust-lang.org/std/fmt/type.Result.html "type std::fmt::Result") because writing to the underlying stream might fail and it must provide a way to propagate the fact that an error has occurred back up the stack.