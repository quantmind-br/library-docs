---
title: AsRawFd in std::os::fd - Rust
url: https://doc.rust-lang.org/std/os/fd/trait.AsRawFd.html
source: crawler
fetched_at: 2026-05-06T21:24:22.751128725-03:00
rendered_js: false
word_count: 318
summary: The AsRawFd trait provides a standardized interface for extracting a raw file descriptor from an underlying object on Unix-like and WASI platforms.
tags:
    - rust
    - file-descriptor
    - unix
    - wasi
    - system-programming
    - trait
category: api
---

## Trait AsRawFd

1.66.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#42-70)

```rust
pub trait AsRawFd {
    // Required method
    fn as_raw_fd(&self) -> RawFd;
}
```

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

Expand description

A trait to extract the raw file descriptor from an underlying object.

This is only available on unix and WASI platforms and must be imported in order to call the method. Windows platforms have a corresponding `AsRawHandle` and `AsRawSocket` set of traits.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#69)

Extracts the raw file descriptor.

This function is typically used to **borrow** an owned file descriptor. When used in this way, this method does **not** pass ownership of the raw file descriptor to the caller, and the file descriptor is only guaranteed to be valid while the original object has not yet been destroyed.

However, borrowing is not strictly required. See [`AsFd::as_fd`](https://doc.rust-lang.org/std/os/fd/trait.AsFd.html#tymethod.as_fd "method std::os::fd::AsFd::as_fd") for an API which strictly borrows a file descriptor.

##### [§](#example)Example

```rust
use std::fs::File;
#[cfg(any(unix, target_os = "wasi"))]
use std::os::fd::{AsRawFd, RawFd};

let mut f = File::open("foo.txt")?;
// Note that `raw_fd` is only valid as long as `f` exists.
#[cfg(any(unix, target_os = "wasi"))]
let raw_fd: RawFd = f.as_raw_fd();
```

[Source](https://doc.rust-lang.org/src/std/sys/fs/unix/dir.rs.html#75-79)[§](#impl-AsRawFd-for-Dir)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#172-177)[§](#impl-AsRawFd-for-File)

Available on **non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#294-298)[§](#impl-AsRawFd-for-PipeReader)

Available on **non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#318-322)[§](#impl-AsRawFd-for-PipeWriter)

Available on **non-`target_os=trusty`** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#213-218)[§](#impl-AsRawFd-for-Stderr)

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#197-202)[§](#impl-AsRawFd-for-Stdin)

Available on **non-`target_os=trusty`** only.

1.21.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#205-210)[§](#impl-AsRawFd-for-Stdout)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/net.rs.html#17)[§](#impl-AsRawFd-for-TcpListener)

Available on **non-`target_os=trusty`** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/net.rs.html#17)[§](#impl-AsRawFd-for-TcpStream)

Available on **non-`target_os=trusty`** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/net.rs.html#17)[§](#impl-AsRawFd-for-UdpSocket)

Available on **non-`target_os=trusty`** only.

1.2.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#471-476)[§](#impl-AsRawFd-for-ChildStderr)

Available on **Unix** only.

1.2.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#455-460)[§](#impl-AsRawFd-for-ChildStdin)

Available on **Unix** only.

1.2.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#463-468)[§](#impl-AsRawFd-for-ChildStdout)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/src/std/os/linux/process.rs.html#110-115)[§](#impl-AsRawFd-for-PidFd)

Available on **Linux** only.

1.10.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/datagram.rs.html#965-970)[§](#impl-AsRawFd-for-UnixDatagram)

Available on **Unix** only.

1.10.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/listener.rs.html#311-316)[§](#impl-AsRawFd-for-UnixListener)

Available on **Unix** only.

1.10.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/stream.rs.html#696-701)[§](#impl-AsRawFd-for-UnixStream)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#151-156)[§](#impl-AsRawFd-for-BorrowedFd%3C'_%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#159-164)[§](#impl-AsRawFd-for-OwnedFd)

1.48.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#149-154)[§](#impl-AsRawFd-for-i32)

1.35.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#238-243)[§](#impl-AsRawFd-for-StderrLock%3C'a%3E)

1.35.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#222-227)[§](#impl-AsRawFd-for-StdinLock%3C'a%3E)

Available on **non-`target_os=trusty`** only.

1.35.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#230-235)[§](#impl-AsRawFd-for-StdoutLock%3C'a%3E)

[Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#277-282)[§](#impl-AsRawFd-for-UniqueRc%3CT%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#285-290)[§](#impl-AsRawFd-for-Box%3CT%3E)

1.69.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#269-274)[§](#impl-AsRawFd-for-Rc%3CT%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#261-266)[§](#impl-AsRawFd-for-Arc%3CT%3E)

This impl allows implementing traits that require `AsRawFd` on Arc.

```rust
use std::net::UdpSocket;
use std::sync::Arc;
trait MyTrait: AsRawFd {
}
impl MyTrait for Arc<UdpSocket> {}
impl MyTrait for Box<UdpSocket> {}
```