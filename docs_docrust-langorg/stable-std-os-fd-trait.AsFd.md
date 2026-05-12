---
title: AsFd in std::os::fd - Rust
url: https://doc.rust-lang.org/stable/std/os/fd/trait.AsFd.html
source: crawler
fetched_at: 2026-05-06T21:31:13.944818491-03:00
rendered_js: false
word_count: 206
summary: The AsFd trait provides a standardized interface for borrowing a file descriptor from underlying objects on Unix-like systems.
tags:
    - rust
    - file-descriptor
    - trait
    - unix
    - io
category: reference
---

## Trait AsFd

1.66.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#261-279)

```rust
pub trait AsFd {
    // Required method
    fn as_fd(&self) -> BorrowedFd<'_>;
}
```

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

Expand description

A trait to borrow the file descriptor from an underlying object.

This is only available on unix platforms and must be imported in order to call the method. Windows platforms have a corresponding `AsHandle` and `AsSocket` set of traits.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#278)

Borrows the file descriptor.

##### [§](#example)Example

```rust
use std::fs::File;

let mut f = File::open("foo.txt")?;
let borrowed_fd: BorrowedFd<'_> = f.as_fd();
```

[Source](https://doc.rust-lang.org/stable/src/std/sys/fs/unix/dir.rs.html#96-100)[§](#impl-AsFd-for-Dir)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#318-323)[§](#impl-AsFd-for-File)

Available on **non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#536-540)[§](#impl-AsFd-for-PipeReader)

Available on **non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#552-556)[§](#impl-AsFd-for-PipeWriter)

Available on **non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#518-523)[§](#impl-AsFd-for-Stderr)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#484-489)[§](#impl-AsFd-for-Stdin)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#501-506)[§](#impl-AsFd-for-Stdout)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#378-383)[§](#impl-AsFd-for-TcpListener)

Available on **non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#348-353)[§](#impl-AsFd-for-TcpStream)

Available on **non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#408-413)[§](#impl-AsFd-for-UdpSocket)

Available on **non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/process.rs.html#563-568)[§](#impl-AsFd-for-ChildStderr)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/process.rs.html#503-508)[§](#impl-AsFd-for-ChildStdin)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/process.rs.html#533-538)[§](#impl-AsFd-for-ChildStdout)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/linux/process.rs.html#129-133)[§](#impl-AsFd-for-PidFd)

Available on **Linux** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/net/datagram.rs.html#989-994)[§](#impl-AsFd-for-UnixDatagram)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/net/listener.rs.html#335-340)[§](#impl-AsFd-for-UnixListener)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/net/stream.rs.html#720-725)[§](#impl-AsFd-for-UnixStream)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#298-303)[§](#impl-AsFd-for-BorrowedFd%3C'_%3E)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#306-314)[§](#impl-AsFd-for-OwnedFd)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#526-532)[§](#impl-AsFd-for-StderrLock%3C'a%3E)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#492-498)[§](#impl-AsFd-for-StdinLock%3C'a%3E)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#509-515)[§](#impl-AsFd-for-StdoutLock%3C'a%3E)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#282-287)[§](#impl-AsFd-for-%26T)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#290-295)[§](#impl-AsFd-for-%26mut+T)

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#476-481)[§](#impl-AsFd-for-Box%3CT%3E)

1.69.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#460-465)[§](#impl-AsFd-for-Rc%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#468-473)[§](#impl-AsFd-for-UniqueRc%3CT%3E)

1.64.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#452-457)[§](#impl-AsFd-for-Arc%3CT%3E)

This impl allows implementing traits that require `AsFd` on Arc.

```rust
use std::net::UdpSocket;
use std::sync::Arc;

trait MyTrait: AsFd {}
impl MyTrait for Arc<UdpSocket> {}
impl MyTrait for Box<UdpSocket> {}
```