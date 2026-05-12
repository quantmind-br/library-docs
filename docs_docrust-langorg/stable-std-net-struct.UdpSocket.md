---
title: UdpSocket in std::net - Rust
url: https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html
source: crawler
fetched_at: 2026-05-06T21:28:13.596792672-03:00
rendered_js: false
word_count: 2121
summary: This document provides the API reference for the UdpSocket struct in Rust, covering methods for binding, sending, receiving, and managing UDP network communication.
tags:
    - rust
    - udp
    - networking
    - socket-programming
    - std-net
    - api-reference
category: reference
---

## Struct UdpSocket

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#66)

```rust
pub struct UdpSocket(/* private fields */);
```

Expand description

A UDP socket.

After creating a `UdpSocket` by [`bind`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.bind "associated function std::net::UdpSocket::bind")ing it to a socket address, data can be [sent to](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.send_to "method std::net::UdpSocket::send_to") and [received from](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.recv_from "method std::net::UdpSocket::recv_from") any other socket address.

Although UDP is a connectionless protocol, this implementation provides an interface to set an address where data should be sent and received from. After setting a remote address with [`connect`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.connect "method std::net::UdpSocket::connect"), data can be sent to and received from that address with [`send`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.send "method std::net::UdpSocket::send") and [`recv`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.recv "method std::net::UdpSocket::recv").

As stated in the User Datagram Protocol’s specification in [IETF RFC 768](https://tools.ietf.org/html/rfc768), UDP is an unordered, unreliable protocol; refer to [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener") and [`TcpStream`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html "struct std::net::TcpStream") for TCP primitives.

## [§](#examples)Examples

```rust
use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    {
        let socket = UdpSocket::bind("127.0.0.1:34254")?;

        // Receives a single datagram message on the socket. If `buf` is too small to hold
        // the message, it will be cut off.
        let mut buf = [0; 10];
        let (amt, src) = socket.recv_from(&mut buf)?;

        // Redeclare `buf` as slice of the received data and send reverse data back to origin.
        let buf = &mut buf[..amt];
        buf.reverse();
        socket.send_to(buf, &src)?;
    } // the socket is closed here
    Ok(())
}
```

[Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#68-816)[§](#impl-UdpSocket)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#121-123)

Creates a UDP socket from the given address.

The address type can be any implementor of [`ToSocketAddrs`](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs") trait. See its documentation for concrete examples.

If `addr` yields multiple addresses, `bind` will be attempted with each of the addresses until one succeeds and returns the socket. If none of the addresses succeed in creating a socket, the error returned from the last attempt (the last address) is returned.

##### [§](#examples-1)Examples

Creates a UDP socket bound to `127.0.0.1:3400`:

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:3400").expect("couldn't bind to address");
```

Creates a UDP socket bound to `127.0.0.1:3400`. If the socket cannot be bound to that address, create a UDP socket bound to `127.0.0.1:3401`:

```rust
use std::net::{SocketAddr, UdpSocket};

let addrs = [
    SocketAddr::from(([127, 0, 0, 1], 3400)),
    SocketAddr::from(([127, 0, 0, 1], 3401)),
];
let socket = UdpSocket::bind(&addrs[..]).expect("couldn't bind to address");
```

Creates a UDP socket bound to a port assigned by the operating system at `127.0.0.1`.

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:0").unwrap();
```

Note that `bind` declares the scope of your network connection. You can only receive datagrams from and send datagrams to participants in that view of the network. For instance, binding to a loopback address as in the example above will prevent you from sending datagrams to another device in your local network.

In order to limit your view of the network the least, `bind` to [`Ipv4Addr::UNSPECIFIED`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#associatedconstant.UNSPECIFIED "associated constant std::net::Ipv4Addr::UNSPECIFIED") or [`Ipv6Addr::UNSPECIFIED`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#associatedconstant.UNSPECIFIED "associated constant std::net::Ipv6Addr::UNSPECIFIED").

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#144-146)

Receives a single datagram message on the socket. On success, returns the number of bytes read and the origin.

The function must be called with valid byte array `buf` of sufficient size to hold the message bytes. If a message is too long to fit in the supplied buffer, excess bytes may be discarded.

##### [§](#examples-2)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
let mut buf = [0; 10];
let (number_of_bytes, src_addr) = socket.recv_from(&mut buf)
                                        .expect("Didn't receive data");
let filled_buf = &mut buf[..number_of_bytes];
```

1.18.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#173-175)

Receives a single datagram message on the socket, without removing it from the queue. On success, returns the number of bytes read and the origin.

The function must be called with valid byte array `buf` of sufficient size to hold the message bytes. If a message is too long to fit in the supplied buffer, excess bytes may be discarded.

Successive calls return the same data. This is accomplished by passing `MSG_PEEK` as a flag to the underlying `recvfrom` system call.

Do not use this function to implement busy waiting, instead use `libc::poll` to synchronize IO events on one or more sockets.

##### [§](#examples-3)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
let mut buf = [0; 10];
let (number_of_bytes, src_addr) = socket.peek_from(&mut buf)
                                        .expect("Didn't receive data");
let filled_buf = &mut buf[..number_of_bytes];
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#204-209)

Sends data on the socket to the given address. On success, returns the number of bytes written. Note that the operating system may refuse buffers larger than 65507. However, partial writes are not possible until buffer sizes above `i32::MAX`.

Address type can be any implementor of [`ToSocketAddrs`](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs") trait. See its documentation for concrete examples.

It is possible for `addr` to yield multiple addresses, but `send_to` will only send data to the first address yielded by `addr`.

This will return an error when the IP version of the local socket does not match that returned from [`ToSocketAddrs`](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs").

See [Issue #34202](https://github.com/rust-lang/rust/issues/34202) for more details.

##### [§](#examples-4)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.send_to(&[0; 10], "127.0.0.1:4242").expect("couldn't send data");
```

1.40.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#236-238)

Returns the socket address of the remote peer this socket was connected to.

##### [§](#examples-5)Examples

```rust
use std::net::{Ipv4Addr, SocketAddr, SocketAddrV4, UdpSocket};

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.connect("192.168.0.1:41203").expect("couldn't connect to address");
assert_eq!(socket.peer_addr().unwrap(),
           SocketAddr::V4(SocketAddrV4::new(Ipv4Addr::new(192, 168, 0, 1), 41203)));
```

If the socket isn’t connected, it will return a [`NotConnected`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.NotConnected "variant std::io::ErrorKind::NotConnected") error.

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
assert_eq!(socket.peer_addr().unwrap_err().kind(),
           std::io::ErrorKind::NotConnected);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#252-254)

Returns the socket address that this socket was created from.

##### [§](#examples-6)Examples

```rust
use std::net::{Ipv4Addr, SocketAddr, SocketAddrV4, UdpSocket};

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
assert_eq!(socket.local_addr().unwrap(),
           SocketAddr::V4(SocketAddrV4::new(Ipv4Addr::new(127, 0, 0, 1), 34254)));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#271-273)

Creates a new independently owned handle to the underlying socket.

The returned `UdpSocket` is a reference to the same socket that this object references. Both handles will read and write the same port, and options set on one socket will be propagated to the other.

##### [§](#examples-7)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
let socket_clone = socket.try_clone().expect("couldn't clone the socket");
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#314-316)

Sets the read timeout to the timeout specified.

If the value specified is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") calls will block indefinitely. An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method.

##### [§](#platform-specific-behavior)Platform-specific behavior

Platforms may return a different error code whenever a read times out as a result of setting this option. For example Unix typically returns an error of the kind [`WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock"), but Windows may return [`TimedOut`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.TimedOut "variant std::io::ErrorKind::TimedOut").

##### [§](#examples-8)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_read_timeout(None).expect("set_read_timeout call failed");
```

An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method:

```rust
use std::io;
use std::net::UdpSocket;
use std::time::Duration;

let socket = UdpSocket::bind("127.0.0.1:34254").unwrap();
let result = socket.set_read_timeout(Some(Duration::new(0, 0)));
let err = result.unwrap_err();
assert_eq!(err.kind(), io::ErrorKind::InvalidInput)
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#357-359)

Sets the write timeout to the timeout specified.

If the value specified is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") calls will block indefinitely. An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method.

##### [§](#platform-specific-behavior-1)Platform-specific behavior

Platforms may return a different error code whenever a write times out as a result of setting this option. For example Unix typically returns an error of the kind [`WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock"), but Windows may return [`TimedOut`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.TimedOut "variant std::io::ErrorKind::TimedOut").

##### [§](#examples-9)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_write_timeout(None).expect("set_write_timeout call failed");
```

An [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned if the zero [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration") is passed to this method:

```rust
use std::io;
use std::net::UdpSocket;
use std::time::Duration;

let socket = UdpSocket::bind("127.0.0.1:34254").unwrap();
let result = socket.set_write_timeout(Some(Duration::new(0, 0)));
let err = result.unwrap_err();
assert_eq!(err.kind(), io::ErrorKind::InvalidInput)
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#377-379)

Returns the read timeout of this socket.

If the timeout is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") calls will block indefinitely.

##### [§](#examples-10)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_read_timeout(None).expect("set_read_timeout call failed");
assert_eq!(socket.read_timeout().unwrap(), None);
```

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#397-399)

Returns the write timeout of this socket.

If the timeout is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") calls will block indefinitely.

##### [§](#examples-11)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_write_timeout(None).expect("set_write_timeout call failed");
assert_eq!(socket.write_timeout().unwrap(), None);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#415-417)

Sets the value of the `SO_BROADCAST` option for this socket.

When enabled, this socket is allowed to send packets to a broadcast address.

##### [§](#examples-12)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_broadcast(false).expect("set_broadcast call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#433-435)

Gets the value of the `SO_BROADCAST` option for this socket.

For more information about this option, see [`UdpSocket::set_broadcast`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.set_broadcast "method std::net::UdpSocket::set_broadcast").

##### [§](#examples-13)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_broadcast(false).expect("set_broadcast call failed");
assert_eq!(socket.broadcast().unwrap(), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#451-453)

Sets the value of the `IP_MULTICAST_LOOP` option for this socket.

If enabled, multicast packets will be looped back to the local socket. Note that this might not have any effect on IPv6 sockets.

##### [§](#examples-14)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_loop_v4(false).expect("set_multicast_loop_v4 call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#469-471)

Gets the value of the `IP_MULTICAST_LOOP` option for this socket.

For more information about this option, see [`UdpSocket::set_multicast_loop_v4`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.set_multicast_loop_v4 "method std::net::UdpSocket::set_multicast_loop_v4").

##### [§](#examples-15)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_loop_v4(false).expect("set_multicast_loop_v4 call failed");
assert_eq!(socket.multicast_loop_v4().unwrap(), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#490-492)

Sets the value of the `IP_MULTICAST_TTL` option for this socket.

Indicates the time-to-live value of outgoing multicast packets for this socket. The default value is 1 which means that multicast packets don’t leave the local network unless explicitly requested.

Note that this might not have any effect on IPv6 sockets.

##### [§](#examples-16)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_ttl_v4(42).expect("set_multicast_ttl_v4 call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#508-510)

Gets the value of the `IP_MULTICAST_TTL` option for this socket.

For more information about this option, see [`UdpSocket::set_multicast_ttl_v4`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.set_multicast_ttl_v4 "method std::net::UdpSocket::set_multicast_ttl_v4").

##### [§](#examples-17)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_ttl_v4(42).expect("set_multicast_ttl_v4 call failed");
assert_eq!(socket.multicast_ttl_v4().unwrap(), 42);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#526-528)

Sets the value of the `IPV6_MULTICAST_LOOP` option for this socket.

Controls whether this socket sees the multicast packets it sends itself. Note that this might not have any affect on IPv4 sockets.

##### [§](#examples-18)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_loop_v6(false).expect("set_multicast_loop_v6 call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#544-546)

Gets the value of the `IPV6_MULTICAST_LOOP` option for this socket.

For more information about this option, see [`UdpSocket::set_multicast_loop_v6`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.set_multicast_loop_v6 "method std::net::UdpSocket::set_multicast_loop_v6").

##### [§](#examples-19)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_multicast_loop_v6(false).expect("set_multicast_loop_v6 call failed");
assert_eq!(socket.multicast_loop_v6().unwrap(), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#562-564)

Sets the value for the `IP_TTL` option on this socket.

This value sets the time-to-live field that is used in every packet sent from this socket.

##### [§](#examples-20)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_ttl(42).expect("set_ttl call failed");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#580-582)

Gets the value of the `IP_TTL` option for this socket.

For more information about this option, see [`UdpSocket::set_ttl`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.set_ttl "method std::net::UdpSocket::set_ttl").

##### [§](#examples-21)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.set_ttl(42).expect("set_ttl call failed");
assert_eq!(socket.ttl().unwrap(), 42);
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#592-594)

Executes an operation of the `IP_ADD_MEMBERSHIP` type.

This function specifies a new multicast group for this socket to join. The address must be a valid multicast address, and `interface` is the address of the local interface with which the system should join the multicast group. If it’s equal to [`UNSPECIFIED`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#associatedconstant.UNSPECIFIED "associated constant std::net::Ipv4Addr::UNSPECIFIED") then an appropriate interface is chosen by the system.

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#602-604)

Executes an operation of the `IPV6_ADD_MEMBERSHIP` type.

This function specifies a new multicast group for this socket to join. The address must be a valid multicast address, and `interface` is the index of the interface to join/leave (or 0 to indicate any interface).

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#610-612)

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#618-620)

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#641-643)

Gets the value of the `SO_ERROR` option on this socket.

This will retrieve the stored error in the underlying socket, clearing the field in the process. This can be useful for checking errors between calls.

##### [§](#examples-22)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
match socket.take_error() {
    Ok(Some(error)) => println!("UdpSocket error: {error:?}"),
    Ok(None) => println!("No error"),
    Err(error) => println!("UdpSocket.take_error failed: {error:?}"),
}
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#678-680)

Connects this UDP socket to a remote address, allowing the `send` and `recv` syscalls to be used to send data and also applies filters to only receive data from the specified address.

If `addr` yields multiple addresses, `connect` will be attempted with each of the addresses until the underlying OS function returns no error. Note that usually, a successful `connect` call does not specify that there is a remote server listening on the port, rather, such an error would only be detected after the first send. If the OS returns an error for each of the specified addresses, the error returned from the last connection attempt (the last address) is returned.

##### [§](#examples-23)Examples

Creates a UDP socket bound to `127.0.0.1:3400` and connect the socket to `127.0.0.1:8080`:

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:3400").expect("couldn't bind to address");
socket.connect("127.0.0.1:8080").expect("connect function failed");
```

Unlike in the TCP case, passing an array of addresses to the `connect` function of a UDP socket is not a useful thing to do: The OS will be unable to determine whether something is listening on the remote address without the application sending data.

If your first `connect` is to a loopback address, subsequent `connect`s to non-loopback addresses might fail, depending on the platform.

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#700-702)

Sends data on the socket to the remote address to which it is connected. On success, returns the number of bytes written. Note that the operating system may refuse buffers larger than 65507. However, partial writes are not possible until buffer sizes above `i32::MAX`.

[`UdpSocket::connect`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.connect "method std::net::UdpSocket::connect") will connect this socket to a remote address. This method will fail if the socket is not connected.

##### [§](#examples-24)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.connect("127.0.0.1:8080").expect("connect function failed");
socket.send(&[0, 1, 2]).expect("couldn't send message");
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#728-730)

Receives a single datagram message on the socket from the remote address to which it is connected. On success, returns the number of bytes read.

The function must be called with valid byte array `buf` of sufficient size to hold the message bytes. If a message is too long to fit in the supplied buffer, excess bytes may be discarded.

[`UdpSocket::connect`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.connect "method std::net::UdpSocket::connect") will connect this socket to a remote address. This method will fail if the socket is not connected.

##### [§](#examples-25)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.connect("127.0.0.1:8080").expect("connect function failed");
let mut buf = [0; 10];
match socket.recv(&mut buf) {
    Ok(received) => println!("received {received} bytes {:?}", &buf[..received]),
    Err(e) => println!("recv function failed: {e:?}"),
}
```

1.18.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#768-770)

Receives single datagram on the socket from the remote address to which it is connected, without removing the message from input queue. On success, returns the number of bytes peeked.

The function must be called with valid byte array `buf` of sufficient size to hold the message bytes. If a message is too long to fit in the supplied buffer, excess bytes may be discarded.

Successive calls return the same data. This is accomplished by passing `MSG_PEEK` as a flag to the underlying `recv` system call.

Do not use this function to implement busy waiting, instead use `libc::poll` to synchronize IO events on one or more sockets.

[`UdpSocket::connect`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.connect "method std::net::UdpSocket::connect") will connect this socket to a remote address. This method will fail if the socket is not connected.

##### [§](#errors)Errors

This method will fail if the socket is not connected. The `connect` method will connect this socket to a remote address.

##### [§](#examples-26)Examples

```rust
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:34254").expect("couldn't bind to address");
socket.connect("127.0.0.1:8080").expect("connect function failed");
let mut buf = [0; 10];
match socket.peek(&mut buf) {
    Ok(received) => println!("received {received} bytes"),
    Err(e) => println!("peek function failed: {e:?}"),
}
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#813-815)

Moves this UDP socket into or out of nonblocking mode.

This will result in `recv`, `recv_from`, `send`, and `send_to` system operations becoming nonblocking, i.e., immediately returning from their calls. If the IO operation is successful, `Ok` is returned and no further action is required. If the IO operation could not be completed and needs to be retried, an error with kind [`io::ErrorKind::WouldBlock`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.WouldBlock "variant std::io::ErrorKind::WouldBlock") is returned.

On Unix platforms, calling this method corresponds to calling `fcntl` `FIONBIO`. On Windows calling this method corresponds to calling `ioctlsocket` `FIONBIO`.

##### [§](#examples-27)Examples

Creates a UDP socket bound to `127.0.0.1:7878` and read bytes in nonblocking mode:

```rust
use std::io;
use std::net::UdpSocket;

let socket = UdpSocket::bind("127.0.0.1:7878").unwrap();
socket.set_nonblocking(true).unwrap();

let mut buf = [0; 10];
let (num_bytes_read, _) = loop {
    match socket.recv_from(&mut buf) {
        Ok(n) => break n,
        Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
            // wait until network socket is ready, typically implemented
            // via platform-specific APIs such as epoll or IOCP
            wait_for_fd();
        }
        Err(e) => panic!("encountered IO error: {e}"),
    }
};
println!("bytes: {:?}", &buf[..num_bytes_read]);
```

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#408-413)[§](#impl-AsFd-for-UdpSocket)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#17)[§](#impl-AsRawFd-for-UdpSocket)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#252-257)[§](#impl-AsRawSocket-for-UdpSocket)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#355-360)[§](#impl-AsSocket-for-UdpSocket)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/udp.rs.html#844-848)[§](#impl-Debug-for-UdpSocket)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#427-434)[§](#impl-From%3COwnedFd%3E-for-UdpSocket)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#429-433)[§](#method.from-3)

Converts to this type from the input type.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#372-377)[§](#impl-From%3COwnedSocket%3E-for-UdpSocket)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#374-376)[§](#method.from-1)

Converts to this type from the input type.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#417-423)[§](#impl-From%3CUdpSocket%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/socket.rs.html#363-369)[§](#impl-From%3CUdpSocket%3E-for-OwnedSocket)

Available on **Windows** only.

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#33)[§](#impl-FromRawFd-for-UdpSocket)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#33)[§](#method.from_raw_fd)

Constructs a new instance of `Self` from the given raw file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.FromRawFd.html#tymethod.from_raw_fd)

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#280-288)[§](#impl-FromRawSocket-for-UdpSocket)

Available on **Windows** only.

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#46)[§](#impl-IntoRawFd-for-UdpSocket)

Available on **non-`target_os=trusty` and (Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`)** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/net.rs.html#46)[§](#method.into_raw_fd)

Consumes this object, returning the raw underlying file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.IntoRawFd.html#tymethod.into_raw_fd)

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#307-312)[§](#impl-IntoRawSocket-for-UdpSocket)

Available on **Windows** only.

[§](#impl-Freeze-for-UdpSocket)

[§](#impl-RefUnwindSafe-for-UdpSocket)

[§](#impl-Send-for-UdpSocket)

[§](#impl-Sync-for-UdpSocket)

[§](#impl-Unpin-for-UdpSocket)

[§](#impl-UnsafeUnpin-for-UdpSocket)

[§](#impl-UnwindSafe-for-UdpSocket)