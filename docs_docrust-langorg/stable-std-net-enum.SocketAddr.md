---
title: SocketAddr in std::net - Rust
url: https://doc.rust-lang.org/stable/std/net/enum.SocketAddr.html
source: crawler
fetched_at: 2026-05-06T21:34:45.010609999-03:00
rendered_js: false
word_count: 254
summary: This document describes the SocketAddr enum in Rust, which provides a portable representation of IPv4 or IPv6 internet socket addresses consisting of an IP address and a port number.
tags:
    - rust
    - socket-address
    - networking
    - ip-address
    - std-net
category: reference
---

## Enum SocketAddr

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#33)

```rust
pub enum SocketAddr {
    V4(SocketAddrV4),
    V6(SocketAddrV6),
}
```

Expand description

An internet socket address, either IPv4 or IPv6.

Internet socket addresses consist of an [IP address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr"), a 16-bit port number, as well as possibly some version-dependent additional information. See [`SocketAddrV4`](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV4.html "struct std::net::SocketAddrV4")’s and [`SocketAddrV6`](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV6.html "struct std::net::SocketAddrV6")’s respective documentation for more details.

## [§](#portability)Portability

`SocketAddr` is intended to be a portable representation of socket addresses and is likely not the same as the internal socket address type used by the target operating system’s API. Like all `repr(Rust)` structs, however, its exact layout remains undefined and should not be relied upon between builds.

## [§](#examples)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);

assert_eq!("127.0.0.1:8080".parse(), Ok(socket));
assert_eq!(socket.port(), 8080);
assert_eq!(socket.is_ipv4(), true);
```

[§](#variant.V4)1.0.0

An IPv4 socket address.

[§](#variant.V6)1.0.0

An IPv6 socket address.

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#432)[§](#impl-SocketAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#447)

🔬This is a nightly-only experimental API. (`addr_parse_ascii` [#101035](https://github.com/rust-lang/rust/issues/101035))

Parse a socket address from a slice of bytes.

```rust
#![feature(addr_parse_ascii)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr, SocketAddr};

let socket_v4 = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
let socket_v6 = SocketAddr::new(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1)), 8080);

assert_eq!(SocketAddr::parse_ascii(b"127.0.0.1:8080"), Ok(socket_v4));
assert_eq!(SocketAddr::parse_ascii(b"[::1]:8080"), Ok(socket_v6));
```

[Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#154)[§](#impl-SocketAddr-1)

1.7.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#172)

Creates a new socket address from an [IP address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr") and a port number.

##### [§](#examples-1)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
assert_eq!(socket.ip(), IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)));
assert_eq!(socket.port(), 8080);
```

1.7.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#193)

Returns the IP address associated with this socket address.

##### [§](#examples-2)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
assert_eq!(socket.ip(), IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)));
```

1.9.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#214)

Changes the IP address associated with this socket address.

##### [§](#examples-3)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let mut socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
socket.set_ip(IpAddr::V4(Ipv4Addr::new(10, 10, 0, 1)));
assert_eq!(socket.ip(), IpAddr::V4(Ipv4Addr::new(10, 10, 0, 1)));
```

1.0.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#237)

Returns the port number associated with this socket address.

##### [§](#examples-4)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
assert_eq!(socket.port(), 8080);
```

1.9.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#258)

Changes the port number associated with this socket address.

##### [§](#examples-5)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let mut socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
socket.set_port(1025);
assert_eq!(socket.port(), 1025);
```

1.16.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#284)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if the [IP address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr") in this `SocketAddr` is an [`IPv4` address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html#variant.V4 "variant std::net::IpAddr::V4"), and [`false`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") otherwise.

##### [§](#examples-6)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)), 8080);
assert_eq!(socket.is_ipv4(), true);
assert_eq!(socket.is_ipv6(), false);
```

1.16.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/socket_addr.rs.html#307)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if the [IP address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr") in this `SocketAddr` is an [`IPv6` address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html#variant.V6 "variant std::net::IpAddr::V6"), and [`false`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") otherwise.

##### [§](#examples-7)Examples

```rust
use std::net::{IpAddr, Ipv6Addr, SocketAddr};

let socket = SocketAddr::new(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 65535, 0, 1)), 8080);
assert_eq!(socket.is_ipv4(), false);
assert_eq!(socket.is_ipv6(), true);
```

[§](#impl-Freeze-for-SocketAddr)

[§](#impl-RefUnwindSafe-for-SocketAddr)

[§](#impl-Send-for-SocketAddr)

[§](#impl-Sync-for-SocketAddr)

[§](#impl-Unpin-for-SocketAddr)

[§](#impl-UnsafeUnpin-for-SocketAddr)

[§](#impl-UnwindSafe-for-SocketAddr)