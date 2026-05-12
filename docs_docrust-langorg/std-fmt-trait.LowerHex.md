---
title: LowerHex in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.LowerHex.html
source: crawler
fetched_at: 2026-05-06T21:30:14.973759475-03:00
rendered_js: false
word_count: 142
summary: The LowerHex trait provides a mechanism for formatting primitive integers and custom types into lowercase hexadecimal strings within the Rust standard library.
tags:
    - rust
    - formatting
    - hexadecimal
    - trait
    - std-fmt
category: reference
---

## Trait LowerHex

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1376)

```rust
pub trait LowerHex {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

Expand description

`x` formatting.

The `LowerHex` trait should format its output as a number in hexadecimal, with `a` through `f` in lower case.

For primitive signed integers (`i8` to `i128`, and `isize`), negative values are formatted as the two’s complement representation.

The alternate flag, `#`, adds a `0x` in front of the output.

For more information on formatters, see [the module-level documentation](https://doc.rust-lang.org/std/fmt/index.html).

## [§](#examples)Examples

Basic usage with `i32`:

```rust
let y = 42; // 42 is '2a' in hex

assert_eq!(format!("{y:x}"), "2a");
assert_eq!(format!("{y:#x}"), "0x2a");

assert_eq!(format!("{:x}", -16), "fffffff0");
```

Implementing `LowerHex` on a type:

```rust
use std::fmt;

struct Length(i32);

impl fmt::LowerHex for Length {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let val = self.0;

        fmt::LowerHex::fmt(&val, f) // delegate to i32's implementation
    }
}

let l = Length(9);

assert_eq!(format!("l as hex is: {l:x}"), "l as hex is: 9");

assert_eq!(format!("l as hex is: {l:#010x}"), "l as hex is: 0x00000009");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#1379)

Formats the value using the given formatter.

##### [§](#errors)Errors

This function should return [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if, and only if, the provided [`Formatter`](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter") returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). String formatting is considered an infallible operation; this function only returns a [`Result`](https://doc.rust-lang.org/std/fmt/type.Result.html "type std::fmt::Result") because writing to the underlying stream might fail and it must provide a way to propagate the fact that an error has occurred back up the stack.