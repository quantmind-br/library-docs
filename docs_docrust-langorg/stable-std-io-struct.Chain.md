---
title: Chain in std::io - Rust
url: https://doc.rust-lang.org/stable/std/io/struct.Chain.html
source: crawler
fetched_at: 2026-05-06T21:31:26.476831665-03:00
rendered_js: false
word_count: 521
summary: The Chain struct in Rust provides an adapter that allows two separate readers to be linked together, enabling sequential reading as if they were a single source.
tags:
    - rust
    - io
    - readers
    - chaining
    - data-processing
    - adapter-pattern
category: reference
---

## Struct Chain

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2718-2722)

```rust
pub struct Chain<T, U> { /* private fields */ }
```

Expand description

Adapter to chain together two readers.

This struct is generally created by calling [`chain`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain "method std::io::Read::chain") on a reader. Please see the documentation of [`chain`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain "method std::io::Read::chain") for more details.

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2724-2801)[§](#impl-Chain%3CT,+U%3E)

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2744-2746)

Consumes the `Chain`, returning the wrapped readers.

##### [§](#examples)Examples

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut foo_file = File::open("foo.txt")?;
    let mut bar_file = File::open("bar.txt")?;

    let chain = foo_file.chain(bar_file);
    let (foo_file, bar_file) = chain.into_inner();
    Ok(())
}
```

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2771-2773)

Gets references to the underlying readers in this `Chain`.

Care should be taken to avoid modifying the internal I/O state of the underlying readers as doing so may corrupt the internal state of this `Chain`.

##### [§](#examples-1)Examples

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut foo_file = File::open("foo.txt")?;
    let mut bar_file = File::open("bar.txt")?;

    let chain = foo_file.chain(bar_file);
    let (foo_file, bar_file) = chain.get_ref();
    Ok(())
}
```

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2798-2800)

Gets mutable references to the underlying readers in this `Chain`.

Care should be taken to avoid modifying the internal I/O state of the underlying readers as doing so may corrupt the internal state of this `Chain`.

##### [§](#examples-2)Examples

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut foo_file = File::open("foo.txt")?;
    let mut bar_file = File::open("bar.txt")?;

    let mut chain = foo_file.chain(bar_file);
    let (foo_file, bar_file) = chain.get_mut();
    Ok(())
}
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2863-2895)[§](#impl-BufRead-for-Chain%3CT,+U%3E)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2864-2872)[§](#method.fill_buf)

Returns the contents of the internal buffer, filling it with more data, via `Read` methods, if empty. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#tymethod.fill_buf)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2874-2876)[§](#method.consume)

Marks the given `amount` of additional bytes from the internal buffer as having been read. Subsequent calls to `read` only return bytes that have not been marked as read. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#tymethod.consume)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2878-2891)[§](#method.read_until)

Reads all bytes into `buf` until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.read_until)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2435-2437)[§](#method.has_data_left)

🔬This is a nightly-only experimental API. (`buf_read_has_data_left` [#86423](https://github.com/rust-lang/rust/issues/86423))

Checks if there is any data left to be `read`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.has_data_left)

1.83.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2559-2561)[§](#method.skip_until)

Skips all bytes until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.skip_until)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2627-2632)[§](#method.read_line)

Reads all bytes until a newline (the `0xA` byte) is reached, and append them to the provided `String` buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.read_line)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2665-2670)[§](#method.split)

Returns an iterator over the contents of this reader split on the byte `byte`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.split)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2702-2707)[§](#method.lines)

Returns an iterator over the lines of this reader. [Read more](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html#method.lines)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2717)[§](#impl-Debug-for-Chain%3CT,+U%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2804-2860)[§](#impl-Read-for-Chain%3CT,+U%3E)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2805-2813)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2815-2823)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2826-2828)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2830-2838)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2843-2859)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#991-993)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_string)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1044-1046)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1080-1082)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1200-1205)[§](#method.chain)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1239-1244)[§](#method.take)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_array)