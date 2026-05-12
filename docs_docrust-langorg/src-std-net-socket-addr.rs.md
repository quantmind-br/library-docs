---
title: socket_addr.rs - source
url: https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#263-268
source: crawler
fetched_at: 2026-05-06T21:23:56.04878668-03:00
rendered_js: false
word_count: 1054
summary: The ToSocketAddrs trait provides a standardized interface for converting various types, including strings, tuples, and socket address structs, into an iterator of SocketAddr values for network operations.
tags:
    - rust
    - networking
    - socket-address
    - trait
    - dns-resolution
category: reference
---

## std/net/ socket\_addr.rs

````rust
1// Tests for this module
2#[cfg(all(test, not(any(target_os = "emscripten", all(target_os = "wasi", target_env = "p1")))))]
3mod tests;
4
5#[stable(feature = "rust1", since = "1.0.0")]
6pub use core::net::{SocketAddr, SocketAddrV4, SocketAddrV6};
7
8use crate::net::{IpAddr, Ipv4Addr, Ipv6Addr};
9use crate::{io, iter, option, slice, vec};
10
11/// A trait for objects which can be converted or resolved to one or more
12/// [`SocketAddr`] values.
13///
14/// This trait is used for generic address resolution when constructing network
15/// objects. By default it is implemented for the following types:
16///
17///  * [`SocketAddr`]: [`to_socket_addrs`] is the identity function.
18///
19///  * [`SocketAddrV4`], [`SocketAddrV6`], <code>([IpAddr], [u16])</code>,
20///    <code>([Ipv4Addr], [u16])</code>, <code>([Ipv6Addr], [u16])</code>:
21///    [`to_socket_addrs`] constructs a [`SocketAddr`] trivially.
22///
23///  * <code>(&[str], [u16])</code>: <code>&[str]</code> should be either a string representation
24///    of an [`IpAddr`] address as expected by [`FromStr`] implementation or a host
25///    name. [`u16`] is the port number.
26///
27///  * <code>&[str]</code>: the string should be either a string representation of a
28///    [`SocketAddr`] as expected by its [`FromStr`] implementation or a string like
29///    `<host_name>:<port>` pair where `<port>` is a [`u16`] value.
30///
31///  * <code>&[[SocketAddr]]</code>: all [`SocketAddr`] values in the slice will be used.
32///
33/// This trait allows constructing network objects like [`TcpStream`] or
34/// [`UdpSocket`] easily with values of various types for the bind/connection
35/// address. It is needed because sometimes one type is more appropriate than
36/// the other: for simple uses a string like `"localhost:12345"` is much nicer
37/// than manual construction of the corresponding [`SocketAddr`], but sometimes
38/// [`SocketAddr`] value is *the* main source of the address, and converting it to
39/// some other type (e.g., a string) just for it to be converted back to
40/// [`SocketAddr`] in constructor methods is pointless.
41///
42/// Addresses returned by the operating system that are not IP addresses are
43/// silently ignored.
44///
45/// [`FromStr`]: crate::str::FromStr "std::str::FromStr"
46/// [`TcpStream`]: crate::net::TcpStream "net::TcpStream"
47/// [`to_socket_addrs`]: ToSocketAddrs::to_socket_addrs
48/// [`UdpSocket`]: crate::net::UdpSocket "net::UdpSocket"
49///
50/// # Examples
51///
52/// Creating a [`SocketAddr`] iterator that yields one item:
53///
54/// ```
55/// use std::net::{ToSocketAddrs, SocketAddr};
56///
57/// let addr = SocketAddr::from(([127, 0, 0, 1], 443));
58/// let mut addrs_iter = addr.to_socket_addrs().unwrap();
59///
60/// assert_eq!(Some(addr), addrs_iter.next());
61/// assert!(addrs_iter.next().is_none());
62/// ```
63///
64/// Creating a [`SocketAddr`] iterator from a hostname:
65///
66/// ```no_run
67/// use std::net::{SocketAddr, ToSocketAddrs};
68///
69/// // assuming 'localhost' resolves to 127.0.0.1
70/// let mut addrs_iter = "localhost:443".to_socket_addrs().unwrap();
71/// assert_eq!(addrs_iter.next(), Some(SocketAddr::from(([127, 0, 0, 1], 443))));
72/// assert!(addrs_iter.next().is_none());
73///
74/// // assuming 'foo' does not resolve
75/// assert!("foo:443".to_socket_addrs().is_err());
76/// ```
77///
78/// Creating a [`SocketAddr`] iterator that yields multiple items:
79///
80/// ```
81/// use std::net::{SocketAddr, ToSocketAddrs};
82///
83/// let addr1 = SocketAddr::from(([0, 0, 0, 0], 80));
84/// let addr2 = SocketAddr::from(([127, 0, 0, 1], 443));
85/// let addrs = vec![addr1, addr2];
86///
87/// let mut addrs_iter = (&addrs[..]).to_socket_addrs().unwrap();
88///
89/// assert_eq!(Some(addr1), addrs_iter.next());
90/// assert_eq!(Some(addr2), addrs_iter.next());
91/// assert!(addrs_iter.next().is_none());
92/// ```
93///
94/// Attempting to create a [`SocketAddr`] iterator from an improperly formatted
95/// socket address `&str` (missing the port):
96///
97/// ```
98/// use std::io;
99/// use std::net::ToSocketAddrs;
100///
101/// let err = "127.0.0.1".to_socket_addrs().unwrap_err();
102/// assert_eq!(err.kind(), io::ErrorKind::InvalidInput);
103/// ```
104///
105/// [`TcpStream::connect`] is an example of a function that utilizes
106/// `ToSocketAddrs` as a trait bound on its parameter in order to accept
107/// different types:
108///
109/// ```no_run
110/// use std::net::{TcpStream, Ipv4Addr};
111///
112/// let stream = TcpStream::connect(("127.0.0.1", 443));
113/// // or
114/// let stream = TcpStream::connect("127.0.0.1:443");
115/// // or
116/// let stream = TcpStream::connect((Ipv4Addr::new(127, 0, 0, 1), 443));
117/// ```
118///
119/// [`TcpStream::connect`]: crate::net::TcpStream::connect
120#[stable(feature = "rust1", since = "1.0.0")]
121pub trait ToSocketAddrs {
122    /// Returned iterator over socket addresses which this type may correspond
123    /// to.
124    #[stable(feature = "rust1", since = "1.0.0")]
125    type Iter: Iterator<Item = SocketAddr>;
126
127    /// Converts this object to an iterator of resolved [`SocketAddr`]s.
128    ///
129    /// The returned iterator might not actually yield any values depending on the
130    /// outcome of any resolution performed.
131    ///
132    /// Note that this function may block the current thread while resolution is
133    /// performed.
134    #[stable(feature = "rust1", since = "1.0.0")]
135    fn to_socket_addrs(&self) -> io::Result<Self::Iter>;
136}
137
138#[stable(feature = "rust1", since = "1.0.0")]
139impl ToSocketAddrs for SocketAddr {
140    type Iter = option::IntoIter<SocketAddr>;
141    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
142        Ok(Some(*self).into_iter())
143    }
144}
145
146#[stable(feature = "rust1", since = "1.0.0")]
147impl ToSocketAddrs for SocketAddrV4 {
148    type Iter = option::IntoIter<SocketAddr>;
149    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
150        SocketAddr::V4(*self).to_socket_addrs()
151    }
152}
153
154#[stable(feature = "rust1", since = "1.0.0")]
155impl ToSocketAddrs for SocketAddrV6 {
156    type Iter = option::IntoIter<SocketAddr>;
157    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
158        SocketAddr::V6(*self).to_socket_addrs()
159    }
160}
161
162#[stable(feature = "rust1", since = "1.0.0")]
163impl ToSocketAddrs for (IpAddr, u16) {
164    type Iter = option::IntoIter<SocketAddr>;
165    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
166        let (ip, port) = *self;
167        match ip {
168            IpAddr::V4(ref a) => (*a, port).to_socket_addrs(),
169            IpAddr::V6(ref a) => (*a, port).to_socket_addrs(),
170        }
171    }
172}
173
174#[stable(feature = "rust1", since = "1.0.0")]
175impl ToSocketAddrs for (Ipv4Addr, u16) {
176    type Iter = option::IntoIter<SocketAddr>;
177    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
178        let (ip, port) = *self;
179        SocketAddrV4::new(ip, port).to_socket_addrs()
180    }
181}
182
183#[stable(feature = "rust1", since = "1.0.0")]
184impl ToSocketAddrs for (Ipv6Addr, u16) {
185    type Iter = option::IntoIter<SocketAddr>;
186    fn to_socket_addrs(&self) -> io::Result<option::IntoIter<SocketAddr>> {
187        let (ip, port) = *self;
188        SocketAddrV6::new(ip, port, 0, 0).to_socket_addrs()
189    }
190}
191
192fn lookup_host(host: &str, port: u16) -> io::Result<vec::IntoIter<SocketAddr>> {
193    let addrs = crate::sys::net::lookup_host(host, port)?;
194    Ok(Vec::from_iter(addrs).into_iter())
195}
196
197#[stable(feature = "rust1", since = "1.0.0")]
198impl ToSocketAddrs for (&str, u16) {
199    type Iter = vec::IntoIter<SocketAddr>;
200    fn to_socket_addrs(&self) -> io::Result<vec::IntoIter<SocketAddr>> {
201        let (host, port) = *self;
202
203        // Try to parse the host as a regular IP address first
204        if let Ok(addr) = host.parse::<IpAddr>() {
205            let addr = SocketAddr::new(addr, port);
206            return Ok(vec![addr].into_iter());
207        }
208
209        // Otherwise, make the system look it up.
210        lookup_host(host, port)
211    }
212}
213
214#[stable(feature = "string_u16_to_socket_addrs", since = "1.46.0")]
215impl ToSocketAddrs for (String, u16) {
216    type Iter = vec::IntoIter<SocketAddr>;
217    fn to_socket_addrs(&self) -> io::Result<vec::IntoIter<SocketAddr>> {
218        (&*self.0, self.1).to_socket_addrs()
219    }
220}
221
222// accepts strings like 'localhost:12345'
223#[stable(feature = "rust1", since = "1.0.0")]
224impl ToSocketAddrs for str {
225    type Iter = vec::IntoIter<SocketAddr>;
226    fn to_socket_addrs(&self) -> io::Result<vec::IntoIter<SocketAddr>> {
227        // Try to parse as a regular SocketAddr first
228        if let Ok(addr) = self.parse() {
229            return Ok(vec![addr].into_iter());
230        }
231
232        // Otherwise, split the string by ':' and convert the second part to u16...
233        let Some((host, port_str)) = self.rsplit_once(':') else {
234            return Err(io::const_error!(io::ErrorKind::InvalidInput, "invalid socket address"));
235        };
236        let Ok(port) = port_str.parse::<u16>() else {
237            return Err(io::const_error!(io::ErrorKind::InvalidInput, "invalid port value"));
238        };
239
240        // ... and make the system look up the host.
241        lookup_host(host, port)
242    }
243}
244
245#[stable(feature = "slice_to_socket_addrs", since = "1.8.0")]
246impl<'a> ToSocketAddrs for &'a [SocketAddr] {
247    type Iter = iter::Cloned<slice::Iter<'a, SocketAddr>>;
248
249    fn to_socket_addrs(&self) -> io::Result<Self::Iter> {
250        Ok(self.iter().cloned())
251    }
252}
253
254#[stable(feature = "rust1", since = "1.0.0")]
255impl<T: ToSocketAddrs + ?Sized> ToSocketAddrs for &T {
256    type Iter = T::Iter;
257    fn to_socket_addrs(&self) -> io::Result<T::Iter> {
258        (**self).to_socket_addrs()
259    }
260}
261
262#[stable(feature = "string_to_socket_addrs", since = "1.16.0")]
263impl ToSocketAddrs for String {
264    type Iter = vec::IntoIter<SocketAddr>;
265    fn to_socket_addrs(&self) -> io::Result<vec::IntoIter<SocketAddr>> {
266        (&**self).to_socket_addrs()
267    }
268}
````