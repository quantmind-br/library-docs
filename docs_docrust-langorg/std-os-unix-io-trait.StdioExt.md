---
title: StdioExt in std::os::unix::io - Rust
url: https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html
source: crawler
fetched_at: 2026-05-06T21:24:36.810904055-03:00
rendered_js: false
word_count: 206
summary: This document defines the StdioExt trait for Unix-based systems, providing an experimental interface for manipulating and swapping standard input/output file descriptors.
tags:
    - rust
    - stdio
    - file-descriptors
    - unix-api
    - experimental-api
    - low-level-io
category: api
---

```rust
pub trait StdioExt: Sealed {
    // Required methods
    fn set_fd<T: Into<OwnedFd>>(&mut self, fd: T) -> Result<()>;
    fn replace_fd<T: Into<OwnedFd>>(
        &mut self,
        replace_with: T,
    ) -> Result<OwnedFd>;
    fn take_fd(&mut self) -> Result<OwnedFd>;
}
```

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Available on **Unix** only.

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#138)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to point to the file description underpinning `fd`.

Rust std::io write buffers (if any) are flushed, but other runtimes (e.g. C stdio) or libraries that acquire a clone of the file descriptor will not be aware of this change.

##### [§](#platform-specific-behavior)Platform-specific behavior

This is [currently](https://doc.rust-lang.org/std/io/index.html#platform-specific-behavior "mod std::io") implemented using

- `fd_renumber` on wasip1
- `dup2` on most unixes

```rust
#![feature(stdio_swap)]
use std::io::{self, Read, Write};
use std::os::unix::io::StdioExt;

fn main() -> io::Result<()> {
   let (reader, mut writer) = io::pipe()?;
   let mut stdin = io::stdin();
   stdin.set_fd(reader)?;
   writer.write_all(b"Hello, world!")?;
   let mut buffer = vec![0; 13];
   assert_eq!(stdin.read(&mut buffer)?, 13);
   assert_eq!(&buffer, b"Hello, world!");
   Ok(())
}
```

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#146)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor and returns a new `OwnedFd` backed by the previous file description.

See [`set_fd()`](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.set_fd "method std::os::unix::io::StdioExt::set_fd") for details.

[Source](https://doc.rust-lang.org/src/std/os/unix/io/mod.rs.html#158)

🔬This is a nightly-only experimental API. (`stdio_swap` [#150667](https://github.com/rust-lang/rust/issues/150667))

Redirects the stdio file descriptor to the null device (`/dev/null`) and returns a new `OwnedFd` backed by the previous file description.

Programs that communicate structured data via stdio can use this early in `main()` to extract the fds, treat them as other IO types (`File`, `UnixStream`, etc), apply custom buffering or avoid interference from stdio use later in the program.

See [`set_fd()`](https://doc.rust-lang.org/std/os/unix/io/trait.StdioExt.html#tymethod.set_fd "method std::os::unix::io::StdioExt::set_fd") for additional details.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*