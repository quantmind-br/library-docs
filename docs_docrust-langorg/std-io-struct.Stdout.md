---
title: Stdout in std::io - Rust
url: https://doc.rust-lang.org/std/io/struct.Stdout.html
source: crawler
fetched_at: 2026-05-06T21:24:38.446818268-03:00
rendered_js: false
word_count: 642
summary: This document describes the Stdout struct in Rust, which provides a handle to the global standard output stream, supporting synchronized writing, locking mechanisms, and platform-specific I/O behavior.
tags:
    - rust
    - standard-library
    - io
    - stdout
    - stream-handling
    - concurrency
    - buffered-io
category: reference
---

## Struct Stdout

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#608-613)

```rust
pub struct Stdout { /* private fields */ }
```

Expand description

A handle to the global standard output stream of the current process.

Each handle shares a global buffer of data to be written to the standard output stream. Access is also synchronized via a lock and explicit control over locking is available via the [`lock`](https://doc.rust-lang.org/std/io/struct.Stdout.html#method.lock "method std::io::Stdout::lock") method.

By default, the handle is line-buffered when connected to a terminal, meaning it flushes automatically when a newline (`\n`) is encountered. For immediate output, you can manually call the [`flush`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush "method std::io::Write::flush") method. When the handle goes out of scope, the buffer is automatically flushed.

Created by the [`io::stdout`](https://doc.rust-lang.org/std/io/fn.stdout.html "fn std::io::stdout") method.

#### [§](#note-windows-portability-considerations)Note: Windows Portability Considerations

When operating in a console, the Windows implementation of this stream does not support non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return an error.

In a process with a detached console, such as one using `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process, the contained handle will be null. In such cases, the standard library’s `Read` and `Write` will do nothing and silently succeed. All other I/O operations, via the standard library or via raw Windows API calls, will fail.

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#744-771)[§](#impl-Stdout)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#765-770)

Locks this handle to the standard output stream, returning a writable guard.

The lock is released when the returned lock goes out of scope. The returned guard also implements the `Write` trait for writing data.

##### [§](#examples)Examples

```rust
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout().lock();

    stdout.write_all(b"hello world")?;

    Ok(())
}
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#501-506)[§](#impl-AsFd-for-Stdout)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#565-570)[§](#impl-AsHandle-for-Stdout)

Available on **Windows** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#205-210)[§](#impl-AsRawFd-for-Stdout)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#109-113)[§](#impl-AsRawHandle-for-Stdout)

Available on **Windows** only.

1.16.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#780-784)[§](#impl-Debug-for-Stdout)

1.74.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1710-1738)[§](#impl-From%3CStdout%3E-for-Stdio)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#1735-1737)[§](#method.from)

Redirect command stdout/stderr to our stdout

##### [§](#examples-1)Examples

```rust
#![feature(exit_status_error)]
use std::io;
use std::process::Command;

let output = Command::new("whoami")
    .stdout(io::stdout())
    .output()?;
output.status.exit_ok()?;
assert!(output.stdout.is_empty());
```

1.70.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-Stdout)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#1265)[§](#method.is_terminal)

Returns `true` if the descriptor/handle refers to a terminal/tty. [Read more](https://doc.rust-lang.org/std/io/trait.IsTerminal.html#tymethod.is_terminal)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#200)[§](#impl-StdioExt-for-Stdout)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#200)[§](#method.set_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to point to the file description underpinning `fd`. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.set_fd)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#200)[§](#method.take_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to the null device (`/dev/null`) and returns a new `OwnedFd` backed by the previous file description. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.take_fd)

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#200)[§](#method.replace_fd)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor and returns a new `OwnedFd` backed by the previous file description. [Read more](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.replace_fd)

1.48.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#813-836)[§](#impl-Write-for-%26Stdout)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#814-816)[§](#method.write-1)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#817-819)[§](#method.write_vectored-1)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#821-823)[§](#method.is_write_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#824-826)[§](#method.flush-1)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#827-829)[§](#method.write_all-1)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#830-832)[§](#method.write_all_vectored-1)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#833-835)[§](#method.write_fmt-1)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#787-810)[§](#impl-Write-for-Stdout)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#788-790)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#791-793)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#795-797)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#798-800)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#801-803)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#804-806)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

[Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#807-809)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#777)[§](#impl-RefUnwindSafe-for-Stdout)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#774)[§](#impl-UnwindSafe-for-Stdout)

[§](#impl-Freeze-for-Stdout)

[§](#impl-Send-for-Stdout)

[§](#impl-Sync-for-Stdout)

[§](#impl-Unpin-for-Stdout)

[§](#impl-UnsafeUnpin-for-Stdout)