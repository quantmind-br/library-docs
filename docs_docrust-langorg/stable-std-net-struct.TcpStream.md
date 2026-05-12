---
title: TcpStream in std::net - Rust
url: https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html
source: crawler
fetched_at: 2026-05-06T21:28:10.929844086-03:00
rendered_js: false
word_count: 2126
summary: This document provides the reference documentation for the TcpStream struct in Rust, covering methods for establishing TCP connections, managing socket communication, and configuring stream behavior.
tags:
    - rust
    - tcp-stream
    - networking
    - socket-programming
    - std-net
category: reference
---

## Struct TcpStream

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#62)

```rust
pub struct TcpStream(/* private fields */);
```

Expand description

A TCP stream between a local and a remote socket.

After creating a `TcpStream` by either [`connect`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.connect "associated function std::net::TcpStream::connect")ing to a remote host or [`accept`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html#method.accept "method std::net::TcpListener::accept")ing a connection on a [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener"), data can be transmitted by [reading](https://doc.rust-lang.org/stable/std/io/trait.Read.html "trait std::io::Read") and [writing](https://doc.rust-lang.org/stable/std/io/trait.Write.html "trait std::io::Write") to it.

The connection will be closed when the value is dropped. The reading and writing portions of the connection can also be shut down individually with the [`shutdown`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.shutdown "method std::net::TcpStream::shutdown") method.

The Transmission Control Protocol is specified in [IETF RFC 793](https://tools.ietf.org/html/rfc793).

## [§](#examples)Examples

```rust
use std::io::prelude::*;
use std::net::TcpStream;

fn main() -> std::io::Result<()> {
    let mut stream = TcpStream::connect("127.0.0.1:34254")?;

    stream.write(&[1])?;
    stream.read(&mut [0; 128])?;
    Ok(())
} // the stream is closed here
```

## [§](#platform-specific-behavior)Platform-specific Behavior

On Unix, writes to the underlying socket in `SOCK_STREAM` mode are made with `MSG_NOSIGNAL` flag. This suppresses the emission of the `SIGPIPE` signal when writing to disconnected socket. In some cases, getting a `SIGPIPE` would trigger process termination.

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#125-620)[§](#impl-TcpStream)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#168-170)

Opens a TCP connection to a remote host.

`addr` is an address of the remote host. Anything which implements [`ToSocketAddrs`](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs") trait can be supplied for the address; see this trait documentation for concrete examples.

If `addr` yields multiple addresses, `connect` will be attempted with each of the addresses until a connection is successful. If none of the addresses result in a successful connection, the error returned from the last connection attempt (the last address) is returned.

##### [§](#examples-1)Examples

Open a TCP connection to `127.0.0.1:8080`:

```rust
use std::net::TcpStream;

if let Ok(stream) = TcpStream::connect("127.0.0.1:8080") {
    println!("Connected to the server!");
} else {
    println!("Couldn't connect to server...");
}
```

Open a TCP connection to `127.0.0.1:8080`. If the connection fails, open a TCP connection to `127.0.0.1:8081`:

```rust
use std::net::{SocketAddr, TcpStream};

let addrs = [
    SocketAddr::from(([127, 0, 0, 1], 8080)),
    SocketAddr::from(([127, 0, 0, 1], 8081)),
];
if let Ok(stream) = TcpStream::connect(&addrs[..]) {
    println!("Connected to the server!");
} else {
    println!("Couldn't connect to server...");
}
```

1.21.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#184-186)

Opens a TCP connection to a remote host with a timeout.

Unlike `connect`, `connect_timeout` takes a single [`SocketAddr`](https://doc.rust-lang.org/stable/std/net/enum.SocketAddr.html "enum std::net::SocketAddr") since timeout must be applied to individual addresses.

It is an error to pass a zero `Duration` to this function.

Unlike other methods on `TcpStream`, this does not correspond to a single system call. It instead calls `connect` in nonblocking mode and then uses an OS-specific mechanism to await the completion of the connection request.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#201-203)

Returns the socket address of the remote peer of this TCP connection.

##### [§](#examples-2)Examples

```rust
use std::net::{Ipv4Addr, SocketAddr, SocketAddrV4, TcpStream};

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
assert_eq!(stream.peer_addr().unwrap(),
           SocketAddr::V4(SocketAddrV4::new(Ipv4Addr::new(127, 0, 0, 1), 8080)));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#218-220)

Returns the socket address of the local half of this TCP connection.

##### [§](#examples-3)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, TcpStream};

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
assert_eq!(stream.local_addr().unwrap().ip(),
           IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#245-247)

Shuts down the read, write, or both halves of this connection.

This function will cause all pending and future I/O on the specified portions to return immediately with an appropriate value (see the documentation of [`Shutdown`](https://doc.rust-lang.org/stable/std/net/enum.Shutdown.html "enum std::net::Shutdown")).

##### [§](#platform-specific-behavior-1)Platform-specific behavior

Calling this function multiple times may result in different behavior, depending on the operating system. On Linux, the second call will return `Ok(())`, but on macOS, it will return `ErrorKind::NotConnected`. This may change in the future.

##### [§](#examples-4)Examples

```rust
use std::net::{Shutdown, TcpStream};

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.shutdown(Shutdown::Both).expect("shutdown call failed");
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#266-268)

Creates a new independently owned handle to the underlying socket.

The returned `TcpStream` is a reference to the same stream that this object references. Both handles will read and write the same stream of data, and options set on one stream will be propagated to the other stream.

##### [§](#examples-5)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
let stream_clone = stream.try_clone().expect("clone failed...");
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#310-312)

Sets the read timeout to the timeout specified.

If the value specified is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") calls will block indefinitely. An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method.

##### [§](#platform-specific-behavior-2)Platform-specific behavior

Platforms may return a different error code whenever a read times out as a result of setting this option. For example Unix typically returns an error of the kind [`WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock"), but Windows may return [`TimedOut`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.TimedOut "variant std::io::ErrorKind::TimedOut").

##### [§](#examples-6)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_read_timeout(None).expect("set_read_timeout call failed");
```

An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method:

```rust
use std::io;
use std::net::TcpStream;
use std::time::Duration;

let stream = TcpStream::connect("127.0.0.1:8080").unwrap();
let result = stream.set_read_timeout(Some(Duration::new(0, 0)));
let err = result.unwrap_err();
assert_eq!(err.kind(), io::ErrorKind::InvalidInput)
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#354-356)

Sets the write timeout to the timeout specified.

If the value specified is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") calls will block indefinitely. An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method.

##### [§](#platform-specific-behavior-3)Platform-specific behavior

Platforms may return a different error code whenever a write times out as a result of setting this option. For example Unix typically returns an error of the kind [`WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock"), but Windows may return [`TimedOut`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.TimedOut "variant std::io::ErrorKind::TimedOut").

##### [§](#examples-7)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_write_timeout(None).expect("set_write_timeout call failed");
```

An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method:

```rust
use std::io;
use std::net::TcpStream;
use std::time::Duration;

let stream = TcpStream::connect("127.0.0.1:8080").unwrap();
let result = stream.set_write_timeout(Some(Duration::new(0, 0)));
let err = result.unwrap_err();
assert_eq!(err.kind(), io::ErrorKind::InvalidInput)
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#379-381)

Returns the read timeout of this socket.

If the timeout is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") calls will block indefinitely.

##### [§](#platform-specific-behavior-4)Platform-specific behavior

Some platforms do not provide access to the current timeout.

##### [§](#examples-8)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_read_timeout(None).expect("set_read_timeout call failed");
assert_eq!(stream.read_timeout().unwrap(), None);
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#404-406)

Returns the write timeout of this socket.

If the timeout is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") calls will block indefinitely.

##### [§](#platform-specific-behavior-5)Platform-specific behavior

Some platforms do not provide access to the current timeout.

##### [§](#examples-9)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_write_timeout(None).expect("set_write_timeout call failed");
assert_eq!(stream.write_timeout().unwrap(), None);
```

1.18.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#426-428)

Receives data on the socket from the remote address to which it is connected, without removing that data from the queue. On success, returns the number of bytes peeked.

Successive calls return the same data. This is accomplished by passing `MSG_PEEK` as a flag to the underlying `recv` system call.

##### [§](#examples-10)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8000")
                       .expect("Couldn't connect to the server...");
let mut buf = [0; 10];
let len = stream.peek(&mut buf).expect("peek failed");
```

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#451-453)

🔬This is a nightly-only experimental API. (`tcp_linger` [#88494](https://github.com/rust-lang/rust/issues/88494))

Sets the value of the `SO_LINGER` option on this socket.

This value controls how the socket is closed when data remains to be sent. If `SO_LINGER` is set, the socket will remain open for the specified duration as the system attempts to send pending data. Otherwise, the system may close the socket immediately, or wait for a default timeout.

##### [§](#examples-11)Examples

```rust
#![feature(tcp_linger)]

use std::net::TcpStream;
use std::time::Duration;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_linger(Some(Duration::from_secs(0))).expect("set_linger call failed");
```

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#473-475)

🔬This is a nightly-only experimental API. (`tcp_linger` [#88494](https://github.com/rust-lang/rust/issues/88494))

Gets the value of the `SO_LINGER` option on this socket.

For more information about this option, see [`TcpStream::set_linger`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.set_linger "method std::net::TcpStream::set_linger").

##### [§](#examples-12)Examples

```rust
#![feature(tcp_linger)]

use std::net::TcpStream;
use std::time::Duration;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_linger(Some(Duration::from_secs(0))).expect("set_linger call failed");
assert_eq!(stream.linger().unwrap(), Some(Duration::from_secs(0)));
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#495-497)

Sets the value of the `TCP_NODELAY` option on this socket.

If set, this option disables the Nagle algorithm. This means that segments are always sent as soon as possible, even if there is only a small amount of data. When not set, data is buffered until there is a sufficient amount to send out, thereby avoiding the frequent sending of small packets.

##### [§](#examples-13)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_nodelay(true).expect("set_nodelay call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#514-516)

Gets the value of the `TCP_NODELAY` option on this socket.

For more information about this option, see [`TcpStream::set_nodelay`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.set_nodelay "method std::net::TcpStream::set_nodelay").

##### [§](#examples-14)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_nodelay(true).expect("set_nodelay call failed");
assert_eq!(stream.nodelay().unwrap_or(false), true);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#533-535)

Sets the value for the `IP_TTL` option on this socket.

This value sets the time-to-live field that is used in every packet sent from this socket.

##### [§](#examples-15)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_ttl(100).expect("set_ttl call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#552-554)

Gets the value of the `IP_TTL` option for this socket.

For more information about this option, see [`TcpStream::set_ttl`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.set_ttl "method std::net::TcpStream::set_ttl").

##### [§](#examples-16)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.set_ttl(100).expect("set_ttl call failed");
assert_eq!(stream.ttl().unwrap_or(0), 100);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#572-574)

Gets the value of the `SO_ERROR` option on this socket.

This will retrieve the stored error in the underlying socket, clearing the field in the process. This can be useful for checking errors between calls.

##### [§](#examples-17)Examples

```rust
use std::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:8080")
                       .expect("Couldn't connect to the server...");
stream.take_error().expect("No error was expected...");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#617-619)

Moves this TCP stream into or out of nonblocking mode.

This will result in `read`, `write`, `recv` and `send` system operations becoming nonblocking, i.e., immediately returning from their calls. If the IO operation is successful, `Ok` is returned and no further action is required. If the IO operation could not be completed and needs to be retried, an error with kind [`io::ErrorKind::WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock") is returned.

On Unix platforms, calling this method corresponds to calling `fcntl` `FIONBIO`. On Windows calling this method corresponds to calling `ioctlsocket` `FIONBIO`.

##### [§](#examples-18)Examples

Reading bytes from a TCP stream in non-blocking mode:

```rust
use std::io::{self, Read};
use std::net::TcpStream;

let mut stream = TcpStream::connect("127.0.0.1:7878")
    .expect("Couldn't connect to the server...");
stream.set_nonblocking(true).expect("set_nonblocking call failed");

let mut buf = vec![];
loop {
    match stream.read_to_end(&mut buf) {
        Ok(_) => break,
        Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
            // wait until network socket is ready, typically implemented
            // via platform-specific APIs such as epoll or IOCP
            wait_for_fd();
        }
        Err(e) => panic!("encountered IO error: {e}"),
    };
};
println!("bytes: {buf:?}");
```

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#348-353)[§](#impl-AsFd-for-TcpStream)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#17)[§](#impl-AsRawFd-for-TcpStream)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#238-243)[§](#impl-AsRawSocket-for-TcpStream)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#305-310)[§](#impl-AsSocket-for-TcpStream)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#727-731)[§](#impl-Debug-for-TcpStream)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#367-374)[§](#impl-From%3COwnedFd%3E-for-TcpStream)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#369-373)[§](#method.from-3)

Converts to this type from the input type.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#322-327)[§](#impl-From%3COwnedSocket%3E-for-TcpStream)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#324-326)[§](#method.from-1)

Converts to this type from the input type.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#357-363)[§](#impl-From%3CTcpStream%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#313-319)[§](#impl-From%3CTcpStream%3E-for-OwnedSocket)

Available on **Windows** only.

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#33)[§](#impl-FromRawFd-for-TcpStream)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#33)[§](#method.from_raw_fd)

Constructs a new instance of `Self` from the given raw file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.FromRawFd.html#tymethod.from_raw_fd)

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#260-268)[§](#impl-FromRawSocket-for-TcpStream)

Available on **Windows** only.

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#46)[§](#impl-IntoRawFd-for-TcpStream)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#46)[§](#method.into_raw_fd)

Consumes this object, returning the raw underlying file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.IntoRawFd.html#tymethod.into_raw_fd)

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#291-296)[§](#impl-IntoRawSocket-for-TcpStream)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#668-685)[§](#impl-Read-for-%26TcpStream)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#669-671)[§](#method.read-1)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#673-675)[§](#method.read_buf-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#677-679)[§](#method.read_vectored-1)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#682-684)[§](#method.is_read_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.is_read_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#935-937)[§](#method.read_to_end-1)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_end)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#991-993)[§](#method.read_to_string-1)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_string)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1044-1046)[§](#method.read_exact-1)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1080-1082)[§](#method.read_buf_exact-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref-2)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes-1)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1200-1205)[§](#method.chain-1)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1239-1244)[§](#method.take-1)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array-1)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_array)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#629-646)[§](#impl-Read-for-TcpStream)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#630-632)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#634-636)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#638-640)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#643-645)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.is_read_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#935-937)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_end)

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

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/net/linux_ext/tcp.rs.html#116-134)[§](#impl-TcpStreamExt-for-TcpStream)

Available on **Linux or Android or Cygwin** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/net/linux_ext/tcp.rs.html#117-119)[§](#method.set_quickack)

Available on **Linux** only.

Enable or disable `TCP_QUICKACK`. [Read more](https://doc.rust-lang.org/stable/std/os/linux/net/trait.TcpStreamExt.html#tymethod.set_quickack)

[Source](https://doc.rust-lang.org/stable/src/std/os/net/linux_ext/tcp.rs.html#121-123)[§](#method.quickack)

Available on **Linux** only.

Gets the value of the `TCP_QUICKACK` option on this socket. [Read more](https://doc.rust-lang.org/stable/std/os/linux/net/trait.TcpStreamExt.html#tymethod.quickack)

[Source](https://doc.rust-lang.org/stable/src/std/os/net/linux_ext/tcp.rs.html#126-128)[§](#method.set_deferaccept)

🔬This is a nightly-only experimental API. (`tcp_deferaccept` [#119639](https://github.com/rust-lang/rust/issues/119639))

Available on **Linux** only.

A socket listener will be awakened solely when data arrives. [Read more](https://doc.rust-lang.org/stable/std/os/linux/net/trait.TcpStreamExt.html#tymethod.set_deferaccept)

[Source](https://doc.rust-lang.org/stable/src/std/os/net/linux_ext/tcp.rs.html#131-133)[§](#method.deferaccept)

🔬This is a nightly-only experimental API. (`tcp_deferaccept` [#119639](https://github.com/rust-lang/rust/issues/119639))

Available on **Linux** only.

Gets the accept delay value of the `TCP_DEFER_ACCEPT` option. [Read more](https://doc.rust-lang.org/stable/std/os/linux/net/trait.TcpStreamExt.html#tymethod.deferaccept)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#687-705)[§](#impl-Write-for-%26TcpStream)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#688-690)[§](#method.write-1)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#692-694)[§](#method.write_vectored-1)

Like [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#697-699)[§](#method.is_write_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#702-704)[§](#method.flush-1)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1875-1887)[§](#method.write_all-1)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1937-1952)[§](#method.write_all_vectored-1)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt-1)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-3)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#648-666)[§](#impl-Write-for-TcpStream)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#649-651)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#653-655)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#658-660)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/stable/src/std/net/tcp.rs.html#663-665)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1875-1887)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1937-1952)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.by_ref)

[§](#impl-Freeze-for-TcpStream)

[§](#impl-RefUnwindSafe-for-TcpStream)

[§](#impl-Send-for-TcpStream)

[§](#impl-Sync-for-TcpStream)

[§](#impl-Unpin-for-TcpStream)

[§](#impl-UnsafeUnpin-for-TcpStream)

[§](#impl-UnwindSafe-for-TcpStream)