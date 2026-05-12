---
title: StdinLock in std::io - Rust
url: https://doc.rust-lang.org/std/io/struct.StdinLock.html
source: crawler
fetched_at: 2026-05-06T21:24:18.466872849-03:00
rendered_js: false
word_count: 684
summary: StdinLock provides a thread-safe, locked reference to standard input, implementing Read and BufRead traits for synchronous console input handling in Rust.
tags:
    - rust
    - standard-library
    - io
    - stdin
    - concurrency
    - buffered-reader
category: reference
---

## Struct StdinLock

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#288-290)

```rust
pub struct StdinLock<'a> { /* private fields */ }
```

Expand description

A locked reference to the [`Stdin`](https://doc.rust-lang.org/std/io/struct.Stdin.html "struct std::io::Stdin") handle.

This handle implements both the [`Read`](https://doc.rust-lang.org/std/io/trait.Read.html "trait std::io::Read") and [`BufRead`](https://doc.rust-lang.org/std/io/trait.BufRead.html "trait std::io::BufRead") traits, and is constructed via the [`Stdin::lock`](https://doc.rust-lang.org/std/io/struct.Stdin.html#method.lock "method std::io::Stdin::lock") method.

#### [§](#note-windows-portability-considerations)Note: Windows Portability Considerations

When operating in a console, the Windows implementation of this stream does not support non-UTF-8 byte sequences. Attempting to read bytes that are not valid UTF-8 will return an error.

In a process with a detached console, such as one using `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process, the contained handle will be null. In such cases, the standard library’s `Read` and `Write` will do nothing and silently succeed. All other I/O operations, via the standard library or via raw Windows API calls, will fail.

## [§](#examples)Examples

```rust
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let stdin = io::stdin(); // We get `Stdin` here.
    {
        let mut handle = stdin.lock(); // We get `StdinLock` here.
        handle.read_line(&mut buffer)?;
    } // `StdinLock` is dropped here.
    Ok(())
}
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#492-498)[§](#impl-AsFd-for-StdinLock%3C'a%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#557-562)[§](#impl-AsHandle-for-StdinLock%3C'a%3E)

Available on **Windows** only.

1.35.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#222-227)[§](#impl-AsRawFd-for-StdinLock%3C'a%3E)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.35.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#123-127)[§](#impl-AsRawHandle-for-StdinLock%3C'a%3E)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#554-570)[§](#impl-BufRead-for-StdinLock%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#555-557)[§](#method.fill_buf)

Returns the contents of the internal buffer, filling it with more data, via `Read` methods, if empty. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#tymethod.fill_buf)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#559-561)[§](#method.consume)

Marks the given `amount` of additional bytes from the internal buffer as having been read. Subsequent calls to `read` only return bytes that have not been marked as read. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#tymethod.consume)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#563-565)[§](#method.read_until)

Reads all bytes into `buf` until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_until)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#567-569)[§](#method.read_line)

Reads all bytes until a newline (the `0xA` byte) is reached, and append them to the provided `String` buffer. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2435-2437)[§](#method.has_data_left)

🔬This is a nightly-only experimental API. (`buf_read_has_data_left` [#86423](https://github.com/rust-lang/rust/issues/86423))

Checks if there is any data left to be `read`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.has_data_left)

1.83.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2559-2561)[§](#method.skip_until)

Skips all bytes until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.skip_until)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2665-2670)[§](#method.split)

Returns an iterator over the contents of this reader split on the byte `byte`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.split)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2702-2707)[§](#method.lines)

Returns an iterator over the lines of this reader. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines)

1.16.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#573-577)[§](#impl-Debug-for-StdinLock%3C'_%3E)

1.70.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-StdinLock%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#method.is_terminal)

Returns `true` if the descriptor/handle refers to a terminal/tty. [Read more](https://doc.rust-lang.org/std/io/trait.IsTerminal.html#tymethod.is_terminal)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#511-544)[§](#impl-Read-for-StdinLock%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#512-514)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#516-518)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#520-522)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#525-527)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#529-531)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#533-535)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#537-539)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#541-543)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1200-1205)[§](#method.chain)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1239-1244)[§](#method.take)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_array)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#201)[§](#impl-StdioExt-for-StdinLock%3C'_%3E)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#201)[§](#method.set_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to point to the file description underpinning `fd`. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.set_fd)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#201)[§](#method.take_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to the null device (`/dev/null`) and returns a new `OwnedFd` backed by the previous file description. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.take_fd)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#201)[§](#method.replace_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor and returns a new `OwnedFd` backed by the previous file description. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.replace_fd)

[§](#impl-Freeze-for-StdinLock%3C'a%3E)

[§](#impl-RefUnwindSafe-for-StdinLock%3C'a%3E)

[§](#impl-Send-for-StdinLock%3C'a%3E)

[§](#impl-Sync-for-StdinLock%3C'a%3E)

[§](#impl-Unpin-for-StdinLock%3C'a%3E)

[§](#impl-UnsafeUnpin-for-StdinLock%3C'a%3E)

[§](#impl-UnwindSafe-for-StdinLock%3C'a%3E)