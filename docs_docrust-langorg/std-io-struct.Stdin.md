---
title: Stdin in std::io - Rust
url: https://doc.rust-lang.org/std/io/struct.Stdin.html#method.read_line
source: crawler
fetched_at: 2026-05-06T21:21:46.181397998-03:00
rendered_js: false
word_count: 972
summary: This document describes the Stdin struct in Rust, which provides a handle to the standard input stream of a process, including methods for reading data and managing stream locking.
tags:
    - rust
    - standard-input
    - stdin
    - io-streams
    - buffered-reading
    - system-programming
category: reference
---

## Struct Stdin

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#250-252)

```rust
pub struct Stdin { /* private fields */ }
```

Expand description

A handle to the standard input stream of a process.

Each handle is a shared reference to a global buffer of input data to this process. A handle can be `lock`’d to gain full access to [`BufRead`](https://doc.rust-lang.org/std/io/trait.BufRead.html "trait std::io::BufRead") methods (e.g., `.lines()`). Reads to this handle are otherwise locked with respect to other reads.

This handle implements the `Read` trait, but beware that concurrent reads of `Stdin` must be executed with care.

Created by the [`io::stdin`](https://doc.rust-lang.org/std/io/fn.stdin.html "fn std::io::stdin") method.

#### [§](#note-windows-portability-considerations)Note: Windows Portability Considerations

When operating in a console, the Windows implementation of this stream does not support non-UTF-8 byte sequences. Attempting to read bytes that are not valid UTF-8 will return an error.

In a process with a detached console, such as one using `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process, the contained handle will be null. In such cases, the standard library’s `Read` and `Write` will do nothing and silently succeed. All other I/O operations, via the standard library or via raw Windows API calls, will fail.

## [§](#examples)Examples

```rust
use std::io;

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let stdin = io::stdin(); // We get `Stdin` here.
    stdin.read_line(&mut buffer)?;
    Ok(())
}
```

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#349-435)[§](#impl-Stdin)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#372-376)

Locks this handle to the standard input stream, returning a readable guard.

The lock is released when the returned lock goes out of scope. The returned guard also implements the [`Read`](https://doc.rust-lang.org/std/io/trait.Read.html "trait std::io::Read") and [`BufRead`](https://doc.rust-lang.org/std/io/trait.BufRead.html "trait std::io::BufRead") traits for accessing the underlying data.

##### [§](#examples-1)Examples

```rust
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_line(&mut buffer)?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#411-413)

Locks this handle and reads a line of input, appending it to the specified buffer.

For detailed semantics of this method, see the documentation on [`BufRead::read_line`](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line "method std::io::BufRead::read_line"). In particular:

- Previous content of the buffer will be preserved. To avoid appending to the buffer, you need to [`clear`](https://doc.rust-lang.org/std/string/struct.String.html#method.clear "method std::string::String::clear") it first.
- The trailing newline character, if any, is included in the buffer.

##### [§](#examples-2)Examples

```rust
use std::io;

let mut input = String::new();
match io::stdin().read_line(&mut input) {
    Ok(n) => {
        println!("{n} bytes read");
        println!("{input}");
    }
    Err(error) => println!("error: {error}"),
}
```

You can run the example one of two ways:

- Pipe some text to it, e.g., `printf foo | path/to/executable`
- Give it text interactively by running the executable directly, in which case it will wait for the Enter key to be pressed before continuing

1.62.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#432-434)

Consumes this handle and returns an iterator over input lines.

For detailed semantics of this method, see the documentation on [`BufRead::lines`](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines "method std::io::BufRead::lines").

##### [§](#examples-3)Examples

```rust
use std::io;

let lines = io::stdin().lines();
for line in lines {
    println!("got a line: {}", line.unwrap());
}
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#484-489)[§](#impl-AsFd-for-Stdin)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#549-554)[§](#impl-AsHandle-for-Stdin)

Available on **Windows** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#197-202)[§](#impl-AsRawFd-for-Stdin)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#102-106)[§](#impl-AsRawHandle-for-Stdin)

Available on **Windows** only.

1.16.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#438-442)[§](#impl-Debug-for-Stdin)

1.70.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-Stdin)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#method.is_terminal)

Returns `true` if the descriptor/handle refers to a terminal/tty. [Read more](https://doc.rust-lang.org/std/io/trait.IsTerminal.html#tymethod.is_terminal)

1.78.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#474-500)[§](#impl-Read-for-%26Stdin)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#475-477)[§](#method.read-1)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#478-480)[§](#method.read_buf-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#481-483)[§](#method.read_vectored-1)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#485-487)[§](#method.is_read_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#488-490)[§](#method.read_to_end-1)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#491-493)[§](#method.read_to_string-1)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#494-496)[§](#method.read_exact-1)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#497-499)[§](#method.read_buf_exact-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes-1)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1200-1205)[§](#method.chain-1)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1239-1244)[§](#method.take-1)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array-1)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_array)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#445-471)[§](#impl-Read-for-Stdin)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#446-448)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#449-451)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#452-454)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#456-458)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#459-461)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#462-464)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#465-467)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#468-470)[§](#method.read_buf_exact)

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

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#201)[§](#impl-StdioExt-for-Stdin)

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

[§](#impl-Freeze-for-Stdin)

[§](#impl-RefUnwindSafe-for-Stdin)

[§](#impl-Send-for-Stdin)

[§](#impl-Sync-for-Stdin)

[§](#impl-Unpin-for-Stdin)

[§](#impl-UnsafeUnpin-for-Stdin)

[§](#impl-UnwindSafe-for-Stdin)