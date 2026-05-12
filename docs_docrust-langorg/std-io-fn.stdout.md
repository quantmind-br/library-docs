---
title: stdout in std::io - Rust
url: https://doc.rust-lang.org/std/io/fn.stdout.html
source: crawler
fetched_at: 2026-05-06T21:24:37.722469783-03:00
rendered_js: false
word_count: 199
summary: This document describes the std::io::stdout function in Rust, which provides a thread-safe handle for writing to the process's standard output stream.
tags:
    - rust-standard-library
    - standard-output
    - io-operations
    - synchronization
    - buffer-management
category: reference
---

## Function stdout

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/stdio.rs.html#716-721)

```rust
pub fn stdout() -> Stdout ⓘ
```

Expand description

Constructs a new handle to the standard output of the current process.

Each handle returned is a reference to a shared global buffer whose access is synchronized via a mutex. If you need more explicit control over locking, see the [`Stdout::lock`](https://doc.rust-lang.org/std/io/struct.Stdout.html#method.lock "method std::io::Stdout::lock") method.

By default, the handle is line-buffered when connected to a terminal, meaning it flushes automatically when a newline (`\n`) is encountered. For immediate output, you can manually call the [`flush`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush "method std::io::Write::flush") method. When the handle goes out of scope, the buffer is automatically flushed.

#### [§](#note-windows-portability-considerations)Note: Windows Portability Considerations

When operating in a console, the Windows implementation of this stream does not support non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return an error.

In a process with a detached console, such as one using `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process, the contained handle will be null. In such cases, the standard library’s `Read` and `Write` will do nothing and silently succeed. All other I/O operations, via the standard library or via raw Windows API calls, will fail.

## [§](#examples)Examples

Using implicit synchronization:

```rust
use std::io::{self, Write};

fn main() -> io::Result<()> {
    io::stdout().write_all(b"hello world")?;

    Ok(())
}
```

Using explicit synchronization:

```rust
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let stdout = io::stdout();
    let mut handle = stdout.lock();

    handle.write_all(b"hello world")?;

    Ok(())
}
```

Ensuring output is flushed immediately:

```rust
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout();
    stdout.write_all(b"hello, ")?;
    stdout.flush()?;                // Manual flush
    stdout.write_all(b"world!\n")?; // Automatically flushed
    Ok(())
}
```