---
title: Write in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/trait.Write.html
source: crawler
fetched_at: 2026-05-06T21:23:59.491960966-03:00
rendered_js: false
word_count: 269
summary: Defines the Write trait for Rust types that provide Unicode-accepting output buffers for text formatting without flushing capabilities.
tags:
    - rust
    - trait
    - formatting
    - unicode
    - buffered-io
    - standard-library
category: reference
---

## Trait Write

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#121)

```rust
pub trait Write {
    // Required method
    fn write_str(&mut self, s: &str) -> Result<(), Error>;

    // Provided methods
    fn write_char(&mut self, c: char) -> Result<(), Error> { ... }
    fn write_fmt(&mut self, args: Arguments<'_>) -> Result<(), Error> { ... }
}
```

Expand description

A trait for writing or formatting into Unicode-accepting buffers or streams.

This trait only accepts UTF-8–encoded data and is not [flushable](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush). If you only want to accept Unicode and you don’t need flushing, you should implement this trait; otherwise you should implement [`std::io::Write`](https://doc.rust-lang.org/std/io/trait.Write.html).

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#154)

Writes a string slice into this writer, returning whether the write succeeded.

This method can only succeed if the entire string slice was successfully written, and this method will not return until all data has been written or an error occurs.

##### [§](#errors)Errors

This function will return an instance of [`std::fmt::Error`](https://doc.rust-lang.org/std/fmt/struct.Error.html "struct std::fmt::Error") on error.

The purpose of that error is to abort the formatting operation when the underlying destination encounters some error preventing it from accepting more text; in particular, it does not communicate any information about *what* error occurred. It should generally be propagated rather than handled, at least when implementing formatting traits.

##### [§](#examples)Examples

```rust
use std::fmt::{Error, Write};

fn writer<W: Write>(f: &mut W, s: &str) -> Result<(), Error> {
    f.write_str(s)
}

let mut buf = String::new();
writer(&mut buf, "hola")?;
assert_eq!(&buf, "hola");
```

1.1.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#183)

Writes a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into this writer, returning whether the write succeeded.

A single [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") may be encoded as more than one byte. This method can only succeed if the entire byte sequence was successfully written, and this method will not return until all data has been written or an error occurs.

##### [§](#errors-1)Errors

This function will return an instance of [`Error`](https://doc.rust-lang.org/std/fmt/struct.Error.html "struct std::fmt::Error") on error.

##### [§](#examples-1)Examples

```rust
use std::fmt::{Error, Write};

fn writer<W: Write>(f: &mut W, c: char) -> Result<(), Error> {
    f.write_char(c)
}

let mut buf = String::new();
writer(&mut buf, 'a')?;
writer(&mut buf, 'b')?;
assert_eq!(&buf, "ab");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#212)

Glue for usage of the [`write!`](https://doc.rust-lang.org/std/macro.write.html "macro std::write") macro with implementors of this trait.

This method should generally not be invoked manually, but rather through the [`write!`](https://doc.rust-lang.org/std/macro.write.html "macro std::write") macro itself.

##### [§](#errors-2)Errors

This function will return an instance of [`Error`](https://doc.rust-lang.org/std/fmt/struct.Error.html "struct std::fmt::Error") on error. Please see [write\_str](https://doc.rust-lang.org/std/fmt/trait.Write.html#tymethod.write_str "method std::fmt::Write::write_str") for details.

##### [§](#examples-2)Examples

```rust
use std::fmt::{Error, Write};

fn writer<W: Write>(f: &mut W, s: &str) -> Result<(), Error> {
    f.write_fmt(format_args!("{s}"))
}

let mut buf = String::new();
writer(&mut buf, "world")?;
assert_eq!(&buf, "world");
```