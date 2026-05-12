---
title: IpAddr in std::net - Rust
url: https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html
source: crawler
fetched_at: 2026-05-06T21:21:57.811250739-03:00
rendered_js: false
word_count: 1144
summary: This document describes the Rust IpAddr enum, which provides a unified type for representing either IPv4 or IPv6 network addresses along with various utility methods for address inspection.
tags:
    - rust
    - ip-address
    - networking
    - enum
    - std-net
    - api-reference
category: reference
---

## Enum IpAddr

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#30)

```rust
pub enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

Expand description

An IP address, either IPv4 or IPv6.

This enum can contain either an [`Ipv4Addr`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html "struct std::net::Ipv4Addr") or an [`Ipv6Addr`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html "struct std::net::Ipv6Addr"), see their respective documentation for more details.

## [§](#examples)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

let localhost_v4 = IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1));
let localhost_v6 = IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1));

assert_eq!("127.0.0.1".parse(), Ok(localhost_v4));
assert_eq!("::1".parse(), Ok(localhost_v6));

assert_eq!(localhost_v4.is_ipv6(), false);
assert_eq!(localhost_v4.is_ipv4(), true);
```

[§](#variant.V4)1.7.0

An IPv4 address.

[§](#variant.V6)1.7.0

An IPv6 address.

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#235)[§](#impl-IpAddr)

1.12.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#253)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") for the special ‘unspecified’ address.

See the documentation for [`Ipv4Addr::is_unspecified()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_unspecified "method std::net::Ipv4Addr::is_unspecified") and [`Ipv6Addr::is_unspecified()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_unspecified "method std::net::Ipv6Addr::is_unspecified") for more details.

##### [§](#examples-1)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(0, 0, 0, 0)).is_unspecified(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0)).is_unspecified(), true);
```

1.12.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#277)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this is a loopback address.

See the documentation for [`Ipv4Addr::is_loopback()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_loopback "method std::net::Ipv4Addr::is_loopback") and [`Ipv6Addr::is_loopback()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_loopback "method std::net::Ipv6Addr::is_loopback") for more details.

##### [§](#examples-2)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)).is_loopback(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0x1)).is_loopback(), true);
```

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#302)

🔬This is a nightly-only experimental API. (`ip` [#27709](https://github.com/rust-lang/rust/issues/27709))

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if the address appears to be globally routable.

See the documentation for [`Ipv4Addr::is_global()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_global "method std::net::Ipv4Addr::is_global") and [`Ipv6Addr::is_global()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_global "method std::net::Ipv6Addr::is_global") for more details.

##### [§](#examples-3)Examples

```rust
#![feature(ip)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(80, 9, 12, 3)).is_global(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0x1c9, 0, 0, 0xafc8, 0, 0x1)).is_global(), true);
```

1.12.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#326)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this is a multicast address.

See the documentation for [`Ipv4Addr::is_multicast()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_multicast "method std::net::Ipv4Addr::is_multicast") and [`Ipv6Addr::is_multicast()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_multicast "method std::net::Ipv6Addr::is_multicast") for more details.

##### [§](#examples-4)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(224, 254, 0, 0)).is_multicast(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0)).is_multicast(), true);
```

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#354)

🔬This is a nightly-only experimental API. (`ip` [#27709](https://github.com/rust-lang/rust/issues/27709))

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this address is in a range designated for documentation.

See the documentation for [`Ipv4Addr::is_documentation()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_documentation "method std::net::Ipv4Addr::is_documentation") and [`Ipv6Addr::is_documentation()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_documentation "method std::net::Ipv6Addr::is_documentation") for more details.

##### [§](#examples-5)Examples

```rust
#![feature(ip)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_documentation(), true);
assert_eq!(
    IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_documentation(),
    true
);
```

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#379)

🔬This is a nightly-only experimental API. (`ip` [#27709](https://github.com/rust-lang/rust/issues/27709))

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this address is in a range designated for benchmarking.

See the documentation for [`Ipv4Addr::is_benchmarking()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html#method.is_benchmarking "method std::net::Ipv4Addr::is_benchmarking") and [`Ipv6Addr::is_benchmarking()`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html#method.is_benchmarking "method std::net::Ipv6Addr::is_benchmarking") for more details.

##### [§](#examples-6)Examples

```rust
#![feature(ip)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(198, 19, 255, 255)).is_benchmarking(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0x2, 0, 0, 0, 0, 0, 0)).is_benchmarking(), true);
```

1.16.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#403)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this address is an [`IPv4` address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html#variant.V4 "variant std::net::IpAddr::V4"), and [`false`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") otherwise.

##### [§](#examples-7)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_ipv4(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_ipv4(), false);
```

1.16.0 (const: 1.50.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#424)

Returns [`true`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") if this address is an [`IPv6` address](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html#variant.V6 "variant std::net::IpAddr::V6"), and [`false`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") otherwise.

##### [§](#examples-8)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_ipv6(), false);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_ipv6(), true);
```

1.75.0 (const: 1.75.0) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#449)

Converts this address to an `IpAddr::V4` if it is an IPv4-mapped IPv6 address, otherwise returns `self` as-is.

##### [§](#examples-9)Examples

```rust
use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

let localhost_v4 = Ipv4Addr::new(127, 0, 0, 1);

assert_eq!(IpAddr::V4(localhost_v4).to_canonical(), localhost_v4);
assert_eq!(IpAddr::V6(localhost_v4.to_ipv6_mapped()).to_canonical(), localhost_v4);
assert_eq!(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)).to_canonical().is_loopback(), true);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1)).is_loopback(), false);
assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1)).to_canonical().is_loopback(), true);
```

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#471)

🔬This is a nightly-only experimental API. (`ip_as_octets` [#137259](https://github.com/rust-lang/rust/issues/137259))

Returns the eight-bit integers this address consists of as a slice.

##### [§](#examples-10)Examples

```rust
#![feature(ip_as_octets)]

use std::net::{Ipv4Addr, Ipv6Addr, IpAddr};

assert_eq!(IpAddr::V4(Ipv4Addr::LOCALHOST).as_octets(), &[127, 0, 0, 1]);
assert_eq!(IpAddr::V6(Ipv6Addr::LOCALHOST).as_octets(),
           &[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
```

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#295)[§](#impl-IpAddr-1)

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#310)

🔬This is a nightly-only experimental API. (`addr_parse_ascii` [#101035](https://github.com/rust-lang/rust/issues/101035))

Parse an IP address from a slice of bytes.

```rust
#![feature(addr_parse_ascii)]

use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};

let localhost_v4 = IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1));
let localhost_v6 = IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1));

assert_eq!(IpAddr::parse_ascii(b"127.0.0.1"), Ok(localhost_v4));
assert_eq!(IpAddr::parse_ascii(b"::1"), Ok(localhost_v6));
```

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-Clone-for-IpAddr)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1083)[§](#impl-Debug-for-IpAddr)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1073)[§](#impl-Display-for-IpAddr)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2323)[§](#impl-From%3C%5Bu16;+8%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2344)[§](#method.from-4)

Creates an `IpAddr::V6` from an eight element 16-bit array.

##### [§](#examples-15)Examples

```rust
use std::net::{IpAddr, Ipv6Addr};

let addr = IpAddr::from([
    0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
    0x209u16, 0x208u16, 0x207u16, 0x206u16,
]);
assert_eq!(
    IpAddr::V6(Ipv6Addr::new(
        0x20d, 0x20c, 0x20b, 0x20a,
        0x209, 0x208, 0x207, 0x206,
    )),
    addr
);
```

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2295)[§](#impl-From%3C%5Bu8;+16%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2316)[§](#method.from-3)

Creates an `IpAddr::V6` from a sixteen element byte array.

##### [§](#examples-14)Examples

```rust
use std::net::{IpAddr, Ipv6Addr};

let addr = IpAddr::from([
    0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
    0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
]);
assert_eq!(
    IpAddr::V6(Ipv6Addr::new(
        0x1918, 0x1716, 0x1514, 0x1312,
        0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
    )),
    addr
);
```

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1264)[§](#impl-From%3C%5Bu8;+4%5D%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1276)[§](#method.from-2)

Creates an `IpAddr::V4` from a four element byte array.

##### [§](#examples-13)Examples

```rust
use std::net::{IpAddr, Ipv4Addr};

let addr = IpAddr::from([13u8, 12u8, 11u8, 10u8]);
assert_eq!(IpAddr::V4(Ipv4Addr::new(13, 12, 11, 10)), addr);
```

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1091)[§](#impl-From%3CIpv4Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1107)[§](#method.from)

Copies this address to a new `IpAddr::V4`.

##### [§](#examples-11)Examples

```rust
use std::net::{IpAddr, Ipv4Addr};

let addr = Ipv4Addr::new(127, 0, 0, 1);

assert_eq!(
    IpAddr::V4(addr),
    IpAddr::from(addr)
)
```

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1114)[§](#impl-From%3CIpv6Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1130)[§](#method.from-1)

Copies this address to a new `IpAddr::V6`.

##### [§](#examples-12)Examples

```rust
use std::net::{IpAddr, Ipv6Addr};

let addr = Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff);

assert_eq!(
    IpAddr::V6(addr),
    IpAddr::from(addr)
);
```

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#316)[§](#impl-FromStr-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#317)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/stable/src/core/net/parser.rs.html#318)[§](#method.from_str)

Parses a string `s` to return a value of this type. [Read more](https://doc.rust-lang.org/stable/std/str/trait.FromStr.html#tymethod.from_str)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-Hash-for-IpAddr)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-Ord-for-IpAddr)

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1175)[§](#impl-PartialEq%3CIpAddr%3E-for-Ipv4Addr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1177)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2158)[§](#impl-PartialEq%3CIpAddr%3E-for-Ipv6Addr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2160)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1164)[§](#impl-PartialEq%3CIpv4Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1166)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2169)[§](#impl-PartialEq%3CIpv6Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2171)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-PartialEq-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1205)[§](#impl-PartialOrd%3CIpAddr%3E-for-Ipv4Addr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1207)[§](#method.partial_cmp-2)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-2)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-2)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-2)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-2)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2199)[§](#impl-PartialOrd%3CIpAddr%3E-for-Ipv6Addr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2201)[§](#method.partial_cmp-4)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-4)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-4)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-4)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-4)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1194)[§](#impl-PartialOrd%3CIpv4Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#1196)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2188)[§](#impl-PartialOrd%3CIpv6Addr%3E-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#2190)[§](#method.partial_cmp-3)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-3)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-3)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-3)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-3)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-PartialOrd-for-IpAddr)

[Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-Copy-for-IpAddr)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-Eq-for-IpAddr)

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#29)[§](#impl-StructuralPartialEq-for-IpAddr)

[§](#impl-Freeze-for-IpAddr)

[§](#impl-RefUnwindSafe-for-IpAddr)

[§](#impl-Send-for-IpAddr)

[§](#impl-Sync-for-IpAddr)

[§](#impl-Unpin-for-IpAddr)

[§](#impl-UnsafeUnpin-for-IpAddr)

[§](#impl-UnwindSafe-for-IpAddr)