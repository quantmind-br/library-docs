---
title: AsRawHandle in std::os::windows::io - Rust
url: https://doc.rust-lang.org/std/os/windows/io/trait.AsRawHandle.html
source: crawler
fetched_at: 2026-05-06T21:24:24.331187487-03:00
rendered_js: false
word_count: 102
summary: This trait defines a standard interface for extracting raw OS handles from types on Windows, facilitating the borrowing of underlying system resources.
tags:
    - rust
    - windows-api
    - raw-handle
    - low-level
    - system-programming
    - resource-borrowing
category: reference
---

## Trait AsRawHandle

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#22-41)

```rust
pub trait AsRawHandle {
    // Required method
    fn as_raw_handle(&self) -> RawHandle;
}
```

Available on **Windows** only.

Expand description

Extracts raw handles.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#40)

Extracts the raw handle.

This function is typically used to **borrow** an owned handle. When used in this way, this method does **not** pass ownership of the raw handle to the caller, and the handle is only guaranteed to be valid while the original object has not yet been destroyed.

This function may return null, such as when called on [`Stdin`](https://doc.rust-lang.org/std/io/struct.Stdin.html "struct std::io::Stdin"), [`Stdout`](https://doc.rust-lang.org/std/io/struct.Stdout.html "struct std::io::Stdout"), or [`Stderr`](https://doc.rust-lang.org/std/io/struct.Stderr.html "struct std::io::Stderr") when the console is detached.

However, borrowing is not strictly required. See [`AsHandle::as_handle`](https://doc.rust-lang.org/std/os/windows/io/trait.AsHandle.html#tymethod.as_handle "method std::os::windows::io::AsHandle::as_handle") for an API which strictly borrows a handle.