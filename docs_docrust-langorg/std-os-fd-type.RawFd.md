---
title: RawFd in std::os::fd - Rust
url: https://doc.rust-lang.org/std/os/fd/type.RawFd.html
source: crawler
fetched_at: 2026-05-06T21:24:24.726152177-03:00
rendered_js: false
word_count: 100
summary: This document defines the RawFd type alias in Rust, representing raw file descriptors on Unix-like and compatible operating systems.
tags:
    - rust
    - file-descriptor
    - system-programming
    - rawfd
    - low-level-api
category: reference
---

[std](https://doc.rust-lang.org/std/index.html)::[os](https://doc.rust-lang.org/std/os/index.html)::[fd](https://doc.rust-lang.org/std/os/fd/index.html)

## Type Alias RawFd

1.66.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#31)

```rust
pub type RawFd = c_int;
```

Available on **non-HermitCore and non-`target_os=motor` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

Expand description

Raw file descriptors.

## Trait Implementations[§](#trait-implementations)

1.48.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#149-154)[§](#impl-AsRawFd-for-i32)

### impl [AsRawFd](https://doc.rust-lang.org/std/os/fd/trait.AsRawFd.html "trait std::os::fd::AsRawFd") for [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

[Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#151-153)[§](#method.as_raw_fd)

#### fn [as\_raw\_fd](https://doc.rust-lang.org/std/os/fd/trait.AsRawFd.html#tymethod.as_raw_fd)(&self) -&gt; [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

Extracts the raw file descriptor. [Read more](https://doc.rust-lang.org/std/os/fd/trait.AsRawFd.html#tymethod.as_raw_fd)

1.48.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#163-168)[§](#impl-FromRawFd-for-i32)

### impl [FromRawFd](https://doc.rust-lang.org/std/os/fd/trait.FromRawFd.html "trait std::os::fd::FromRawFd") for [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

[Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#165-167)[§](#method.from_raw_fd)

#### unsafe fn [from\_raw\_fd](https://doc.rust-lang.org/std/os/fd/trait.FromRawFd.html#tymethod.from_raw_fd)(fd: [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")) -&gt; [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

Constructs a new instance of `Self` from the given raw file descriptor. [Read more](https://doc.rust-lang.org/std/os/fd/trait.FromRawFd.html#tymethod.from_raw_fd)

1.48.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#156-161)[§](#impl-IntoRawFd-for-i32)

### impl [IntoRawFd](https://doc.rust-lang.org/std/os/fd/trait.IntoRawFd.html "trait std::os::fd::IntoRawFd") for [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

[Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#158-160)[§](#method.into_raw_fd)

#### fn [into\_raw\_fd](https://doc.rust-lang.org/std/os/fd/trait.IntoRawFd.html#tymethod.into_raw_fd)(self) -&gt; [RawFd](https://doc.rust-lang.org/std/os/fd/type.RawFd.html "type std::os::fd::RawFd")

Consumes this object, returning the raw underlying file descriptor. [Read more](https://doc.rust-lang.org/std/os/fd/trait.IntoRawFd.html#tymethod.into_raw_fd)