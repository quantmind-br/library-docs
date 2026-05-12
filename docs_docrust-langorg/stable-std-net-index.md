---
title: std::net - Rust
url: https://doc.rust-lang.org/stable/std/net/index.html
source: crawler
fetched_at: 2026-05-06T21:28:11.948846207-03:00
rendered_js: false
word_count: 301
summary: This document outlines the standard library networking module for Rust, providing primitives for TCP and UDP communication along with types for managing IP and socket addresses.
tags:
    - rust
    - networking
    - tcp
    - udp
    - sockets
    - ip-address
    - api-documentation
category: reference
---

## Module net

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/net/mod.rs.html#1-72)

Expand description

Networking primitives for TCP/UDP communication.

This module provides networking functionality for the Transmission Control and User Datagram Protocols, as well as types for IP and socket addresses and functions related to network properties.

## [§](#organization)Organization

- [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener") and [`TcpStream`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html "struct std::net::TcpStream") provide functionality for communication over TCP
- [`UdpSocket`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html "struct std::net::UdpSocket") provides functionality for communication over UDP
- [`IpAddr`](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr") represents IP addresses of either IPv4 or IPv6; [`Ipv4Addr`](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html "struct std::net::Ipv4Addr") and [`Ipv6Addr`](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html "struct std::net::Ipv6Addr") are respectively IPv4 and IPv6 addresses
- [`SocketAddr`](https://doc.rust-lang.org/stable/std/net/enum.SocketAddr.html "enum std::net::SocketAddr") represents socket addresses of either IPv4 or IPv6; [`SocketAddrV4`](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV4.html "struct std::net::SocketAddrV4") and [`SocketAddrV6`](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV6.html "struct std::net::SocketAddrV6") are respectively IPv4 and IPv6 socket addresses
- [`ToSocketAddrs`](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs") is a trait that is used for generic address resolution when interacting with networking objects like [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener"), [`TcpStream`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html "struct std::net::TcpStream") or [`UdpSocket`](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html "struct std::net::UdpSocket")
- Other types are return or parameter types for various methods in this module

Rust disables inheritance of socket objects to child processes by default when possible. For example, through the use of the `CLOEXEC` flag in UNIX systems or the `HANDLE_FLAG_INHERIT` flag on Windows.

[AddrParseError](https://doc.rust-lang.org/stable/std/net/struct.AddrParseError.html "struct std::net::AddrParseError")

An error which can be returned when parsing an IP address or a socket address.

[Incoming](https://doc.rust-lang.org/stable/std/net/struct.Incoming.html "struct std::net::Incoming")

An iterator that infinitely [`accept`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html#method.accept "method std::net::TcpListener::accept")s connections on a [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener").

[Ipv4Addr](https://doc.rust-lang.org/stable/std/net/struct.Ipv4Addr.html "struct std::net::Ipv4Addr")

An IPv4 address.

[Ipv6Addr](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html "struct std::net::Ipv6Addr")

An IPv6 address.

[SocketAddrV4](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV4.html "struct std::net::SocketAddrV4")

An IPv4 socket address.

[SocketAddrV6](https://doc.rust-lang.org/stable/std/net/struct.SocketAddrV6.html "struct std::net::SocketAddrV6")

An IPv6 socket address.

[TcpListener](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener")

A TCP socket server, listening for connections.

[TcpStream](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html "struct std::net::TcpStream")

A TCP stream between a local and a remote socket.

[UdpSocket](https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html "struct std::net::UdpSocket")

A UDP socket.

[IntoIncoming](https://doc.rust-lang.org/stable/std/net/struct.IntoIncoming.html "struct std::net::IntoIncoming")Experimental

An iterator that infinitely [`accept`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html#method.accept "method std::net::TcpListener::accept")s connections on a [`TcpListener`](https://doc.rust-lang.org/stable/std/net/struct.TcpListener.html "struct std::net::TcpListener").

[IpAddr](https://doc.rust-lang.org/stable/std/net/enum.IpAddr.html "enum std::net::IpAddr")

An IP address, either IPv4 or IPv6.

[Shutdown](https://doc.rust-lang.org/stable/std/net/enum.Shutdown.html "enum std::net::Shutdown")

Possible values which can be passed to the [`TcpStream::shutdown`](https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.shutdown "method std::net::TcpStream::shutdown") method.

[SocketAddr](https://doc.rust-lang.org/stable/std/net/enum.SocketAddr.html "enum std::net::SocketAddr")

An internet socket address, either IPv4 or IPv6.

[Ipv6MulticastScope](https://doc.rust-lang.org/stable/std/net/enum.Ipv6MulticastScope.html "enum std::net::Ipv6MulticastScope")Experimental

Scope of an [IPv6 multicast address](https://doc.rust-lang.org/stable/std/net/struct.Ipv6Addr.html "struct std::net::Ipv6Addr") as defined in [IETF RFC 7346 section 2](https://tools.ietf.org/html/rfc7346#section-2).

[ToSocketAddrs](https://doc.rust-lang.org/stable/std/net/trait.ToSocketAddrs.html "trait std::net::ToSocketAddrs")

A trait for objects which can be converted or resolved to one or more [`SocketAddr`](https://doc.rust-lang.org/stable/std/net/enum.SocketAddr.html "enum std::net::SocketAddr") values.

[hostname](https://doc.rust-lang.org/stable/std/net/fn.hostname.html "fn std::net::hostname")Experimental

Returns the system hostname.