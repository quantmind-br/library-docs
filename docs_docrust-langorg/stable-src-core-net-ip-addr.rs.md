---
title: ip_addr.rs - source
url: https://doc.rust-lang.org/stable/src/core/net/ip_addr.rs.html#354
source: crawler
fetched_at: 2026-05-06T21:38:08.719420877-03:00
rendered_js: false
word_count: 9670
summary: This document defines the Rust data structures for representing IPv4 and IPv6 network addresses, including handling for mapped and compatible address formats.
tags:
    - rust
    - networking
    - ip-address
    - ipv4
    - ipv6
    - network-protocol
category: reference
---

## core/net/ ip\_addr.rs

````rust
1use super::display_buffer::DisplayBuffer;
2use crate::cmp::Ordering;
3use crate::fmt::{self, Write};
4use crate::hash::{Hash, Hasher};
5use crate::mem::transmute;
6use crate::ops::{BitAnd, BitAndAssign, BitOr, BitOrAssign, Not};
7
8/// An IP address, either IPv4 or IPv6.
9///
10/// This enum can contain either an [`Ipv4Addr`] or an [`Ipv6Addr`], see their
11/// respective documentation for more details.
12///
13/// # Examples
14///
15/// ```
16/// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
17///
18/// let localhost_v4 = IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1));
19/// let localhost_v6 = IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1));
20///
21/// assert_eq!("127.0.0.1".parse(), Ok(localhost_v4));
22/// assert_eq!("::1".parse(), Ok(localhost_v6));
23///
24/// assert_eq!(localhost_v4.is_ipv6(), false);
25/// assert_eq!(localhost_v4.is_ipv4(), true);
26/// ```
27#[rustc_diagnostic_item = "IpAddr"]
28#[stable(feature = "ip_addr", since = "1.7.0")]
29#[derive(Copy, Clone, Eq, PartialEq, Hash, PartialOrd, Ord)]
30pub enum IpAddr {
31    /// An IPv4 address.
32    #[stable(feature = "ip_addr", since = "1.7.0")]
33    V4(#[stable(feature = "ip_addr", since = "1.7.0")] Ipv4Addr),
34    /// An IPv6 address.
35    #[stable(feature = "ip_addr", since = "1.7.0")]
36    V6(#[stable(feature = "ip_addr", since = "1.7.0")] Ipv6Addr),
37}
38
39/// An IPv4 address.
40///
41/// IPv4 addresses are defined as 32-bit integers in [IETF RFC 791].
42/// They are usually represented as four octets.
43///
44/// See [`IpAddr`] for a type encompassing both IPv4 and IPv6 addresses.
45///
46/// [IETF RFC 791]: https://tools.ietf.org/html/rfc791
47///
48/// # Textual representation
49///
50/// `Ipv4Addr` provides a [`FromStr`] implementation. The four octets are in decimal
51/// notation, divided by `.` (this is called "dot-decimal notation").
52/// Notably, octal numbers (which are indicated with a leading `0`) and hexadecimal numbers (which
53/// are indicated with a leading `0x`) are not allowed per [IETF RFC 6943].
54///
55/// [IETF RFC 6943]: https://tools.ietf.org/html/rfc6943#section-3.1.1
56/// [`FromStr`]: crate::str::FromStr
57///
58/// # Examples
59///
60/// ```
61/// use std::net::Ipv4Addr;
62///
63/// let localhost = Ipv4Addr::new(127, 0, 0, 1);
64/// assert_eq!("127.0.0.1".parse(), Ok(localhost));
65/// assert_eq!(localhost.is_loopback(), true);
66/// assert!("012.004.002.000".parse::<Ipv4Addr>().is_err()); // all octets are in octal
67/// assert!("0000000.0.0.0".parse::<Ipv4Addr>().is_err()); // first octet is a zero in octal
68/// assert!("0xcb.0x0.0x71.0x00".parse::<Ipv4Addr>().is_err()); // all octets are in hex
69/// ```
70#[rustc_diagnostic_item = "Ipv4Addr"]
71#[derive(Copy, Clone, PartialEq, Eq)]
72#[stable(feature = "rust1", since = "1.0.0")]
73pub struct Ipv4Addr {
74    octets: [u8; 4],
75}
76
77#[stable(feature = "rust1", since = "1.0.0")]
78impl Hash for Ipv4Addr {
79    fn hash<H: Hasher>(&self, state: &mut H) {
80        // Hashers are often more efficient at hashing a fixed-width integer
81        // than a bytestring, so convert before hashing. We don't use to_bits()
82        // here as that may involve a byteswap which is unnecessary.
83        u32::from_ne_bytes(self.octets).hash(state);
84    }
85}
86
87/// An IPv6 address.
88///
89/// IPv6 addresses are defined as 128-bit integers in [IETF RFC 4291].
90/// They are usually represented as eight 16-bit segments.
91///
92/// [IETF RFC 4291]: https://tools.ietf.org/html/rfc4291
93///
94/// # Embedding IPv4 Addresses
95///
96/// See [`IpAddr`] for a type encompassing both IPv4 and IPv6 addresses.
97///
98/// To assist in the transition from IPv4 to IPv6 two types of IPv6 addresses that embed an IPv4 address were defined:
99/// IPv4-compatible and IPv4-mapped addresses. Of these IPv4-compatible addresses have been officially deprecated.
100///
101/// Both types of addresses are not assigned any special meaning by this implementation,
102/// other than what the relevant standards prescribe. This means that an address like `::ffff:127.0.0.1`,
103/// while representing an IPv4 loopback address, is not itself an IPv6 loopback address; only `::1` is.
104/// To handle these so called "IPv4-in-IPv6" addresses, they have to first be converted to their canonical IPv4 address.
105///
106/// ### IPv4-Compatible IPv6 Addresses
107///
108/// IPv4-compatible IPv6 addresses are defined in [IETF RFC 4291 Section 2.5.5.1], and have been officially deprecated.
109/// The RFC describes the format of an "IPv4-Compatible IPv6 address" as follows:
110///
111/// ```text
112/// |                80 bits               | 16 |      32 bits        |
113/// +--------------------------------------+--------------------------+
114/// |0000..............................0000|0000|    IPv4 address     |
115/// +--------------------------------------+----+---------------------+
116/// ```
117/// So `::a.b.c.d` would be an IPv4-compatible IPv6 address representing the IPv4 address `a.b.c.d`.
118///
119/// To convert from an IPv4 address to an IPv4-compatible IPv6 address, use [`Ipv4Addr::to_ipv6_compatible`].
120/// Use [`Ipv6Addr::to_ipv4`] to convert an IPv4-compatible IPv6 address to the canonical IPv4 address.
121///
122/// [IETF RFC 4291 Section 2.5.5.1]: https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.1
123///
124/// ### IPv4-Mapped IPv6 Addresses
125///
126/// IPv4-mapped IPv6 addresses are defined in [IETF RFC 4291 Section 2.5.5.2].
127/// The RFC describes the format of an "IPv4-Mapped IPv6 address" as follows:
128///
129/// ```text
130/// |                80 bits               | 16 |      32 bits        |
131/// +--------------------------------------+--------------------------+
132/// |0000..............................0000|FFFF|    IPv4 address     |
133/// +--------------------------------------+----+---------------------+
134/// ```
135/// So `::ffff:a.b.c.d` would be an IPv4-mapped IPv6 address representing the IPv4 address `a.b.c.d`.
136///
137/// To convert from an IPv4 address to an IPv4-mapped IPv6 address, use [`Ipv4Addr::to_ipv6_mapped`].
138/// Use [`Ipv6Addr::to_ipv4`] to convert an IPv4-mapped IPv6 address to the canonical IPv4 address.
139/// Note that this will also convert the IPv6 loopback address `::1` to `0.0.0.1`. Use
140/// [`Ipv6Addr::to_ipv4_mapped`] to avoid this.
141///
142/// [IETF RFC 4291 Section 2.5.5.2]: https://datatracker.ietf.org/doc/html/rfc4291#section-2.5.5.2
143///
144/// # Textual representation
145///
146/// `Ipv6Addr` provides a [`FromStr`] implementation. There are many ways to represent
147/// an IPv6 address in text, but in general, each segments is written in hexadecimal
148/// notation, and segments are separated by `:`. For more information, see
149/// [IETF RFC 5952].
150///
151/// [`FromStr`]: crate::str::FromStr
152/// [IETF RFC 5952]: https://tools.ietf.org/html/rfc5952
153///
154/// # Examples
155///
156/// ```
157/// use std::net::Ipv6Addr;
158///
159/// let localhost = Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1);
160/// assert_eq!("::1".parse(), Ok(localhost));
161/// assert_eq!(localhost.is_loopback(), true);
162/// ```
163#[rustc_diagnostic_item = "Ipv6Addr"]
164#[derive(Copy, Clone, PartialEq, Eq)]
165#[stable(feature = "rust1", since = "1.0.0")]
166pub struct Ipv6Addr {
167    octets: [u8; 16],
168}
169
170#[stable(feature = "rust1", since = "1.0.0")]
171impl Hash for Ipv6Addr {
172    fn hash<H: Hasher>(&self, state: &mut H) {
173        // Hashers are often more efficient at hashing a fixed-width integer
174        // than a bytestring, so convert before hashing. We don't use to_bits()
175        // here as that may involve unnecessary byteswaps.
176        u128::from_ne_bytes(self.octets).hash(state);
177    }
178}
179
180/// Scope of an [IPv6 multicast address] as defined in [IETF RFC 7346 section 2].
181///
182/// # Stability Guarantees
183///
184/// Not all possible values for a multicast scope have been assigned.
185/// Future RFCs may introduce new scopes, which will be added as variants to this enum;
186/// because of this the enum is marked as `#[non_exhaustive]`.
187///
188/// # Examples
189/// ```
190/// #![feature(ip)]
191///
192/// use std::net::Ipv6Addr;
193/// use std::net::Ipv6MulticastScope::*;
194///
195/// // An IPv6 multicast address with global scope (`ff0e::`).
196/// let address = Ipv6Addr::new(0xff0e, 0, 0, 0, 0, 0, 0, 0);
197///
198/// // Will print "Global scope".
199/// match address.multicast_scope() {
200///     Some(InterfaceLocal) => println!("Interface-Local scope"),
201///     Some(LinkLocal) => println!("Link-Local scope"),
202///     Some(RealmLocal) => println!("Realm-Local scope"),
203///     Some(AdminLocal) => println!("Admin-Local scope"),
204///     Some(SiteLocal) => println!("Site-Local scope"),
205///     Some(OrganizationLocal) => println!("Organization-Local scope"),
206///     Some(Global) => println!("Global scope"),
207///     Some(_) => println!("Unknown scope"),
208///     None => println!("Not a multicast address!")
209/// }
210///
211/// ```
212///
213/// [IPv6 multicast address]: Ipv6Addr
214/// [IETF RFC 7346 section 2]: https://tools.ietf.org/html/rfc7346#section-2
215#[derive(Copy, PartialEq, Eq, Clone, Hash, Debug)]
216#[unstable(feature = "ip", issue = "27709")]
217#[non_exhaustive]
218pub enum Ipv6MulticastScope {
219    /// Interface-Local scope.
220    InterfaceLocal,
221    /// Link-Local scope.
222    LinkLocal,
223    /// Realm-Local scope.
224    RealmLocal,
225    /// Admin-Local scope.
226    AdminLocal,
227    /// Site-Local scope.
228    SiteLocal,
229    /// Organization-Local scope.
230    OrganizationLocal,
231    /// Global scope.
232    Global,
233}
234
235impl IpAddr {
236    /// Returns [`true`] for the special 'unspecified' address.
237    ///
238    /// See the documentation for [`Ipv4Addr::is_unspecified()`] and
239    /// [`Ipv6Addr::is_unspecified()`] for more details.
240    ///
241    /// # Examples
242    ///
243    /// ```
244    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
245    ///
246    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(0, 0, 0, 0)).is_unspecified(), true);
247    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0)).is_unspecified(), true);
248    /// ```
249    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
250    #[stable(feature = "ip_shared", since = "1.12.0")]
251    #[must_use]
252    #[inline]
253    pub const fn is_unspecified(&self) -> bool {
254        match self {
255            IpAddr::V4(ip) => ip.is_unspecified(),
256            IpAddr::V6(ip) => ip.is_unspecified(),
257        }
258    }
259
260    /// Returns [`true`] if this is a loopback address.
261    ///
262    /// See the documentation for [`Ipv4Addr::is_loopback()`] and
263    /// [`Ipv6Addr::is_loopback()`] for more details.
264    ///
265    /// # Examples
266    ///
267    /// ```
268    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
269    ///
270    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)).is_loopback(), true);
271    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0x1)).is_loopback(), true);
272    /// ```
273    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
274    #[stable(feature = "ip_shared", since = "1.12.0")]
275    #[must_use]
276    #[inline]
277    pub const fn is_loopback(&self) -> bool {
278        match self {
279            IpAddr::V4(ip) => ip.is_loopback(),
280            IpAddr::V6(ip) => ip.is_loopback(),
281        }
282    }
283
284    /// Returns [`true`] if the address appears to be globally routable.
285    ///
286    /// See the documentation for [`Ipv4Addr::is_global()`] and
287    /// [`Ipv6Addr::is_global()`] for more details.
288    ///
289    /// # Examples
290    ///
291    /// ```
292    /// #![feature(ip)]
293    ///
294    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
295    ///
296    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(80, 9, 12, 3)).is_global(), true);
297    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0x1c9, 0, 0, 0xafc8, 0, 0x1)).is_global(), true);
298    /// ```
299    #[unstable(feature = "ip", issue = "27709")]
300    #[must_use]
301    #[inline]
302    pub const fn is_global(&self) -> bool {
303        match self {
304            IpAddr::V4(ip) => ip.is_global(),
305            IpAddr::V6(ip) => ip.is_global(),
306        }
307    }
308
309    /// Returns [`true`] if this is a multicast address.
310    ///
311    /// See the documentation for [`Ipv4Addr::is_multicast()`] and
312    /// [`Ipv6Addr::is_multicast()`] for more details.
313    ///
314    /// # Examples
315    ///
316    /// ```
317    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
318    ///
319    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(224, 254, 0, 0)).is_multicast(), true);
320    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0)).is_multicast(), true);
321    /// ```
322    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
323    #[stable(feature = "ip_shared", since = "1.12.0")]
324    #[must_use]
325    #[inline]
326    pub const fn is_multicast(&self) -> bool {
327        match self {
328            IpAddr::V4(ip) => ip.is_multicast(),
329            IpAddr::V6(ip) => ip.is_multicast(),
330        }
331    }
332
333    /// Returns [`true`] if this address is in a range designated for documentation.
334    ///
335    /// See the documentation for [`Ipv4Addr::is_documentation()`] and
336    /// [`Ipv6Addr::is_documentation()`] for more details.
337    ///
338    /// # Examples
339    ///
340    /// ```
341    /// #![feature(ip)]
342    ///
343    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
344    ///
345    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_documentation(), true);
346    /// assert_eq!(
347    ///     IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_documentation(),
348    ///     true
349    /// );
350    /// ```
351    #[unstable(feature = "ip", issue = "27709")]
352    #[must_use]
353    #[inline]
354    pub const fn is_documentation(&self) -> bool {
355        match self {
356            IpAddr::V4(ip) => ip.is_documentation(),
357            IpAddr::V6(ip) => ip.is_documentation(),
358        }
359    }
360
361    /// Returns [`true`] if this address is in a range designated for benchmarking.
362    ///
363    /// See the documentation for [`Ipv4Addr::is_benchmarking()`] and
364    /// [`Ipv6Addr::is_benchmarking()`] for more details.
365    ///
366    /// # Examples
367    ///
368    /// ```
369    /// #![feature(ip)]
370    ///
371    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
372    ///
373    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(198, 19, 255, 255)).is_benchmarking(), true);
374    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0x2, 0, 0, 0, 0, 0, 0)).is_benchmarking(), true);
375    /// ```
376    #[unstable(feature = "ip", issue = "27709")]
377    #[must_use]
378    #[inline]
379    pub const fn is_benchmarking(&self) -> bool {
380        match self {
381            IpAddr::V4(ip) => ip.is_benchmarking(),
382            IpAddr::V6(ip) => ip.is_benchmarking(),
383        }
384    }
385
386    /// Returns [`true`] if this address is an [`IPv4` address], and [`false`]
387    /// otherwise.
388    ///
389    /// [`IPv4` address]: IpAddr::V4
390    ///
391    /// # Examples
392    ///
393    /// ```
394    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
395    ///
396    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_ipv4(), true);
397    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_ipv4(), false);
398    /// ```
399    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
400    #[stable(feature = "ipaddr_checker", since = "1.16.0")]
401    #[must_use]
402    #[inline]
403    pub const fn is_ipv4(&self) -> bool {
404        matches!(self, IpAddr::V4(_))
405    }
406
407    /// Returns [`true`] if this address is an [`IPv6` address], and [`false`]
408    /// otherwise.
409    ///
410    /// [`IPv6` address]: IpAddr::V6
411    ///
412    /// # Examples
413    ///
414    /// ```
415    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
416    ///
417    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(203, 0, 113, 6)).is_ipv6(), false);
418    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0)).is_ipv6(), true);
419    /// ```
420    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
421    #[stable(feature = "ipaddr_checker", since = "1.16.0")]
422    #[must_use]
423    #[inline]
424    pub const fn is_ipv6(&self) -> bool {
425        matches!(self, IpAddr::V6(_))
426    }
427
428    /// Converts this address to an `IpAddr::V4` if it is an IPv4-mapped IPv6
429    /// address, otherwise returns `self` as-is.
430    ///
431    /// # Examples
432    ///
433    /// ```
434    /// use std::net::{IpAddr, Ipv4Addr, Ipv6Addr};
435    ///
436    /// let localhost_v4 = Ipv4Addr::new(127, 0, 0, 1);
437    ///
438    /// assert_eq!(IpAddr::V4(localhost_v4).to_canonical(), localhost_v4);
439    /// assert_eq!(IpAddr::V6(localhost_v4.to_ipv6_mapped()).to_canonical(), localhost_v4);
440    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)).to_canonical().is_loopback(), true);
441    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1)).is_loopback(), false);
442    /// assert_eq!(IpAddr::V6(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1)).to_canonical().is_loopback(), true);
443    /// ```
444    #[inline]
445    #[must_use = "this returns the result of the operation, \
446                  without modifying the original"]
447    #[stable(feature = "ip_to_canonical", since = "1.75.0")]
448    #[rustc_const_stable(feature = "ip_to_canonical", since = "1.75.0")]
449    pub const fn to_canonical(&self) -> IpAddr {
450        match self {
451            IpAddr::V4(_) => *self,
452            IpAddr::V6(v6) => v6.to_canonical(),
453        }
454    }
455
456    /// Returns the eight-bit integers this address consists of as a slice.
457    ///
458    /// # Examples
459    ///
460    /// ```
461    /// #![feature(ip_as_octets)]
462    ///
463    /// use std::net::{Ipv4Addr, Ipv6Addr, IpAddr};
464    ///
465    /// assert_eq!(IpAddr::V4(Ipv4Addr::LOCALHOST).as_octets(), &[127, 0, 0, 1]);
466    /// assert_eq!(IpAddr::V6(Ipv6Addr::LOCALHOST).as_octets(),
467    ///            &[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
468    /// ```
469    #[unstable(feature = "ip_as_octets", issue = "137259")]
470    #[inline]
471    pub const fn as_octets(&self) -> &[u8] {
472        match self {
473            IpAddr::V4(ip) => ip.as_octets().as_slice(),
474            IpAddr::V6(ip) => ip.as_octets().as_slice(),
475        }
476    }
477}
478
479impl Ipv4Addr {
480    /// Creates a new IPv4 address from four eight-bit octets.
481    ///
482    /// The result will represent the IP address `a`.`b`.`c`.`d`.
483    ///
484    /// # Examples
485    ///
486    /// ```
487    /// use std::net::Ipv4Addr;
488    ///
489    /// let addr = Ipv4Addr::new(127, 0, 0, 1);
490    /// ```
491    #[rustc_const_stable(feature = "const_ip_32", since = "1.32.0")]
492    #[stable(feature = "rust1", since = "1.0.0")]
493    #[must_use]
494    #[inline]
495    pub const fn new(a: u8, b: u8, c: u8, d: u8) -> Ipv4Addr {
496        Ipv4Addr { octets: [a, b, c, d] }
497    }
498
499    /// The size of an IPv4 address in bits.
500    ///
501    /// # Examples
502    ///
503    /// ```
504    /// use std::net::Ipv4Addr;
505    ///
506    /// assert_eq!(Ipv4Addr::BITS, 32);
507    /// ```
508    #[stable(feature = "ip_bits", since = "1.80.0")]
509    pub const BITS: u32 = 32;
510
511    /// Converts an IPv4 address into a `u32` representation using native byte order.
512    ///
513    /// Although IPv4 addresses are big-endian, the `u32` value will use the target platform's
514    /// native byte order. That is, the `u32` value is an integer representation of the IPv4
515    /// address and not an integer interpretation of the IPv4 address's big-endian bitstring. This
516    /// means that the `u32` value masked with `0xffffff00` will set the last octet in the address
517    /// to 0, regardless of the target platform's endianness.
518    ///
519    /// # Examples
520    ///
521    /// ```
522    /// use std::net::Ipv4Addr;
523    ///
524    /// let addr = Ipv4Addr::new(0x12, 0x34, 0x56, 0x78);
525    /// assert_eq!(0x12345678, addr.to_bits());
526    /// ```
527    ///
528    /// ```
529    /// use std::net::Ipv4Addr;
530    ///
531    /// let addr = Ipv4Addr::new(0x12, 0x34, 0x56, 0x78);
532    /// let addr_bits = addr.to_bits() & 0xffffff00;
533    /// assert_eq!(Ipv4Addr::new(0x12, 0x34, 0x56, 0x00), Ipv4Addr::from_bits(addr_bits));
534    ///
535    /// ```
536    #[rustc_const_stable(feature = "ip_bits", since = "1.80.0")]
537    #[stable(feature = "ip_bits", since = "1.80.0")]
538    #[must_use]
539    #[inline]
540    pub const fn to_bits(self) -> u32 {
541        u32::from_be_bytes(self.octets)
542    }
543
544    /// Converts a native byte order `u32` into an IPv4 address.
545    ///
546    /// See [`Ipv4Addr::to_bits`] for an explanation on endianness.
547    ///
548    /// # Examples
549    ///
550    /// ```
551    /// use std::net::Ipv4Addr;
552    ///
553    /// let addr = Ipv4Addr::from_bits(0x12345678);
554    /// assert_eq!(Ipv4Addr::new(0x12, 0x34, 0x56, 0x78), addr);
555    /// ```
556    #[rustc_const_stable(feature = "ip_bits", since = "1.80.0")]
557    #[stable(feature = "ip_bits", since = "1.80.0")]
558    #[must_use]
559    #[inline]
560    pub const fn from_bits(bits: u32) -> Ipv4Addr {
561        Ipv4Addr { octets: bits.to_be_bytes() }
562    }
563
564    /// An IPv4 address with the address pointing to localhost: `127.0.0.1`
565    ///
566    /// # Examples
567    ///
568    /// ```
569    /// use std::net::Ipv4Addr;
570    ///
571    /// let addr = Ipv4Addr::LOCALHOST;
572    /// assert_eq!(addr, Ipv4Addr::new(127, 0, 0, 1));
573    /// ```
574    #[stable(feature = "ip_constructors", since = "1.30.0")]
575    pub const LOCALHOST: Self = Ipv4Addr::new(127, 0, 0, 1);
576
577    /// An IPv4 address representing an unspecified address: `0.0.0.0`
578    ///
579    /// This corresponds to the constant `INADDR_ANY` in other languages.
580    ///
581    /// # Examples
582    ///
583    /// ```
584    /// use std::net::Ipv4Addr;
585    ///
586    /// let addr = Ipv4Addr::UNSPECIFIED;
587    /// assert_eq!(addr, Ipv4Addr::new(0, 0, 0, 0));
588    /// ```
589    #[doc(alias = "INADDR_ANY")]
590    #[stable(feature = "ip_constructors", since = "1.30.0")]
591    pub const UNSPECIFIED: Self = Ipv4Addr::new(0, 0, 0, 0);
592
593    /// An IPv4 address representing the broadcast address: `255.255.255.255`.
594    ///
595    /// # Examples
596    ///
597    /// ```
598    /// use std::net::Ipv4Addr;
599    ///
600    /// let addr = Ipv4Addr::BROADCAST;
601    /// assert_eq!(addr, Ipv4Addr::new(255, 255, 255, 255));
602    /// ```
603    #[stable(feature = "ip_constructors", since = "1.30.0")]
604    pub const BROADCAST: Self = Ipv4Addr::new(255, 255, 255, 255);
605
606    /// Returns the four eight-bit integers that make up this address.
607    ///
608    /// # Examples
609    ///
610    /// ```
611    /// use std::net::Ipv4Addr;
612    ///
613    /// let addr = Ipv4Addr::new(127, 0, 0, 1);
614    /// assert_eq!(addr.octets(), [127, 0, 0, 1]);
615    /// ```
616    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
617    #[stable(feature = "rust1", since = "1.0.0")]
618    #[must_use]
619    #[inline]
620    pub const fn octets(&self) -> [u8; 4] {
621        self.octets
622    }
623
624    /// Creates an `Ipv4Addr` from a four element byte array.
625    ///
626    /// # Examples
627    ///
628    /// ```
629    /// use std::net::Ipv4Addr;
630    ///
631    /// let addr = Ipv4Addr::from_octets([13u8, 12u8, 11u8, 10u8]);
632    /// assert_eq!(Ipv4Addr::new(13, 12, 11, 10), addr);
633    /// ```
634    #[stable(feature = "ip_from", since = "1.91.0")]
635    #[rustc_const_stable(feature = "ip_from", since = "1.91.0")]
636    #[must_use]
637    #[inline]
638    pub const fn from_octets(octets: [u8; 4]) -> Ipv4Addr {
639        Ipv4Addr { octets }
640    }
641
642    /// Returns the four eight-bit integers that make up this address
643    /// as a slice.
644    ///
645    /// # Examples
646    ///
647    /// ```
648    /// #![feature(ip_as_octets)]
649    ///
650    /// use std::net::Ipv4Addr;
651    ///
652    /// let addr = Ipv4Addr::new(127, 0, 0, 1);
653    /// assert_eq!(addr.as_octets(), &[127, 0, 0, 1]);
654    /// ```
655    #[unstable(feature = "ip_as_octets", issue = "137259")]
656    #[inline]
657    pub const fn as_octets(&self) -> &[u8; 4] {
658        &self.octets
659    }
660
661    /// Returns [`true`] for the special 'unspecified' address (`0.0.0.0`).
662    ///
663    /// This property is defined in _UNIX Network Programming, Second Edition_,
664    /// W. Richard Stevens, p. 891; see also [ip7].
665    ///
666    /// [ip7]: https://man7.org/linux/man-pages/man7/ip.7.html
667    ///
668    /// # Examples
669    ///
670    /// ```
671    /// use std::net::Ipv4Addr;
672    ///
673    /// assert_eq!(Ipv4Addr::new(0, 0, 0, 0).is_unspecified(), true);
674    /// assert_eq!(Ipv4Addr::new(45, 22, 13, 197).is_unspecified(), false);
675    /// ```
676    #[rustc_const_stable(feature = "const_ip_32", since = "1.32.0")]
677    #[stable(feature = "ip_shared", since = "1.12.0")]
678    #[must_use]
679    #[inline]
680    pub const fn is_unspecified(&self) -> bool {
681        u32::from_be_bytes(self.octets) == 0
682    }
683
684    /// Returns [`true`] if this is a loopback address (`127.0.0.0/8`).
685    ///
686    /// This property is defined by [IETF RFC 1122].
687    ///
688    /// [IETF RFC 1122]: https://tools.ietf.org/html/rfc1122
689    ///
690    /// # Examples
691    ///
692    /// ```
693    /// use std::net::Ipv4Addr;
694    ///
695    /// assert_eq!(Ipv4Addr::new(127, 0, 0, 1).is_loopback(), true);
696    /// assert_eq!(Ipv4Addr::new(45, 22, 13, 197).is_loopback(), false);
697    /// ```
698    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
699    #[stable(since = "1.7.0", feature = "ip_17")]
700    #[must_use]
701    #[inline]
702    pub const fn is_loopback(&self) -> bool {
703        self.octets()[0] == 127
704    }
705
706    /// Returns [`true`] if this is a private address.
707    ///
708    /// The private address ranges are defined in [IETF RFC 1918] and include:
709    ///
710    ///  - `10.0.0.0/8`
711    ///  - `172.16.0.0/12`
712    ///  - `192.168.0.0/16`
713    ///
714    /// [IETF RFC 1918]: https://tools.ietf.org/html/rfc1918
715    ///
716    /// # Examples
717    ///
718    /// ```
719    /// use std::net::Ipv4Addr;
720    ///
721    /// assert_eq!(Ipv4Addr::new(10, 0, 0, 1).is_private(), true);
722    /// assert_eq!(Ipv4Addr::new(10, 10, 10, 10).is_private(), true);
723    /// assert_eq!(Ipv4Addr::new(172, 16, 10, 10).is_private(), true);
724    /// assert_eq!(Ipv4Addr::new(172, 29, 45, 14).is_private(), true);
725    /// assert_eq!(Ipv4Addr::new(172, 32, 0, 2).is_private(), false);
726    /// assert_eq!(Ipv4Addr::new(192, 168, 0, 2).is_private(), true);
727    /// assert_eq!(Ipv4Addr::new(192, 169, 0, 2).is_private(), false);
728    /// ```
729    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
730    #[stable(since = "1.7.0", feature = "ip_17")]
731    #[must_use]
732    #[inline]
733    pub const fn is_private(&self) -> bool {
734        match self.octets() {
735            [10, ..] => true,
736            [172, b, ..] if b >= 16 && b <= 31 => true,
737            [192, 168, ..] => true,
738            _ => false,
739        }
740    }
741
742    /// Returns [`true`] if the address is link-local (`169.254.0.0/16`).
743    ///
744    /// This property is defined by [IETF RFC 3927].
745    ///
746    /// [IETF RFC 3927]: https://tools.ietf.org/html/rfc3927
747    ///
748    /// # Examples
749    ///
750    /// ```
751    /// use std::net::Ipv4Addr;
752    ///
753    /// assert_eq!(Ipv4Addr::new(169, 254, 0, 0).is_link_local(), true);
754    /// assert_eq!(Ipv4Addr::new(169, 254, 10, 65).is_link_local(), true);
755    /// assert_eq!(Ipv4Addr::new(16, 89, 10, 65).is_link_local(), false);
756    /// ```
757    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
758    #[stable(since = "1.7.0", feature = "ip_17")]
759    #[must_use]
760    #[inline]
761    pub const fn is_link_local(&self) -> bool {
762        matches!(self.octets(), [169, 254, ..])
763    }
764
765    /// Returns [`true`] if the address appears to be globally reachable
766    /// as specified by the [IANA IPv4 Special-Purpose Address Registry].
767    ///
768    /// Whether or not an address is practically reachable will depend on your
769    /// network configuration. Most IPv4 addresses are globally reachable, unless
770    /// they are specifically defined as *not* globally reachable.
771    ///
772    /// Non-exhaustive list of notable addresses that are not globally reachable:
773    ///
774    /// - The [unspecified address] ([`is_unspecified`](Ipv4Addr::is_unspecified))
775    /// - Addresses reserved for private use ([`is_private`](Ipv4Addr::is_private))
776    /// - Addresses in the shared address space ([`is_shared`](Ipv4Addr::is_shared))
777    /// - Loopback addresses ([`is_loopback`](Ipv4Addr::is_loopback))
778    /// - Link-local addresses ([`is_link_local`](Ipv4Addr::is_link_local))
779    /// - Addresses reserved for documentation ([`is_documentation`](Ipv4Addr::is_documentation))
780    /// - Addresses reserved for benchmarking ([`is_benchmarking`](Ipv4Addr::is_benchmarking))
781    /// - Reserved addresses ([`is_reserved`](Ipv4Addr::is_reserved))
782    /// - The [broadcast address] ([`is_broadcast`](Ipv4Addr::is_broadcast))
783    ///
784    /// For the complete overview of which addresses are globally reachable, see the table at the [IANA IPv4 Special-Purpose Address Registry].
785    ///
786    /// [IANA IPv4 Special-Purpose Address Registry]: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
787    /// [unspecified address]: Ipv4Addr::UNSPECIFIED
788    /// [broadcast address]: Ipv4Addr::BROADCAST
789    ///
790    /// # Examples
791    ///
792    /// ```
793    /// #![feature(ip)]
794    ///
795    /// use std::net::Ipv4Addr;
796    ///
797    /// // Most IPv4 addresses are globally reachable:
798    /// assert_eq!(Ipv4Addr::new(80, 9, 12, 3).is_global(), true);
799    ///
800    /// // However some addresses have been assigned a special meaning
801    /// // that makes them not globally reachable. Some examples are:
802    ///
803    /// // The unspecified address (`0.0.0.0`)
804    /// assert_eq!(Ipv4Addr::UNSPECIFIED.is_global(), false);
805    ///
806    /// // Addresses reserved for private use (`10.0.0.0/8`, `172.16.0.0/12`, 192.168.0.0/16)
807    /// assert_eq!(Ipv4Addr::new(10, 254, 0, 0).is_global(), false);
808    /// assert_eq!(Ipv4Addr::new(192, 168, 10, 65).is_global(), false);
809    /// assert_eq!(Ipv4Addr::new(172, 16, 10, 65).is_global(), false);
810    ///
811    /// // Addresses in the shared address space (`100.64.0.0/10`)
812    /// assert_eq!(Ipv4Addr::new(100, 100, 0, 0).is_global(), false);
813    ///
814    /// // The loopback addresses (`127.0.0.0/8`)
815    /// assert_eq!(Ipv4Addr::LOCALHOST.is_global(), false);
816    ///
817    /// // Link-local addresses (`169.254.0.0/16`)
818    /// assert_eq!(Ipv4Addr::new(169, 254, 45, 1).is_global(), false);
819    ///
820    /// // Addresses reserved for documentation (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`)
821    /// assert_eq!(Ipv4Addr::new(192, 0, 2, 255).is_global(), false);
822    /// assert_eq!(Ipv4Addr::new(198, 51, 100, 65).is_global(), false);
823    /// assert_eq!(Ipv4Addr::new(203, 0, 113, 6).is_global(), false);
824    ///
825    /// // Addresses reserved for benchmarking (`198.18.0.0/15`)
826    /// assert_eq!(Ipv4Addr::new(198, 18, 0, 0).is_global(), false);
827    ///
828    /// // Reserved addresses (`240.0.0.0/4`)
829    /// assert_eq!(Ipv4Addr::new(250, 10, 20, 30).is_global(), false);
830    ///
831    /// // The broadcast address (`255.255.255.255`)
832    /// assert_eq!(Ipv4Addr::BROADCAST.is_global(), false);
833    ///
834    /// // For a complete overview see the IANA IPv4 Special-Purpose Address Registry.
835    /// ```
836    #[unstable(feature = "ip", issue = "27709")]
837    #[must_use]
838    #[inline]
839    pub const fn is_global(&self) -> bool {
840        !(self.octets()[0] == 0 // "This network"
841            || self.is_private()
842            || self.is_shared()
843            || self.is_loopback()
844            || self.is_link_local()
845            // addresses reserved for future protocols (`192.0.0.0/24`)
846            // .9 and .10 are documented as globally reachable so they're excluded
847            || (
848                self.octets()[0] == 192 && self.octets()[1] == 0 && self.octets()[2] == 0
849                && self.octets()[3] != 9 && self.octets()[3] != 10
850            )
851            || self.is_documentation()
852            || self.is_benchmarking()
853            || self.is_reserved()
854            || self.is_broadcast())
855    }
856
857    /// Returns [`true`] if this address is part of the Shared Address Space defined in
858    /// [IETF RFC 6598] (`100.64.0.0/10`).
859    ///
860    /// [IETF RFC 6598]: https://tools.ietf.org/html/rfc6598
861    ///
862    /// # Examples
863    ///
864    /// ```
865    /// #![feature(ip)]
866    /// use std::net::Ipv4Addr;
867    ///
868    /// assert_eq!(Ipv4Addr::new(100, 64, 0, 0).is_shared(), true);
869    /// assert_eq!(Ipv4Addr::new(100, 127, 255, 255).is_shared(), true);
870    /// assert_eq!(Ipv4Addr::new(100, 128, 0, 0).is_shared(), false);
871    /// ```
872    #[unstable(feature = "ip", issue = "27709")]
873    #[must_use]
874    #[inline]
875    pub const fn is_shared(&self) -> bool {
876        self.octets()[0] == 100 && (self.octets()[1] & 0b1100_0000 == 0b0100_0000)
877    }
878
879    /// Returns [`true`] if this address part of the `198.18.0.0/15` range, which is reserved for
880    /// network devices benchmarking.
881    ///
882    /// This range is defined in [IETF RFC 2544] as `192.18.0.0` through
883    /// `198.19.255.255` but [errata 423] corrects it to `198.18.0.0/15`.
884    ///
885    /// [IETF RFC 2544]: https://tools.ietf.org/html/rfc2544
886    /// [errata 423]: https://www.rfc-editor.org/errata/eid423
887    ///
888    /// # Examples
889    ///
890    /// ```
891    /// #![feature(ip)]
892    /// use std::net::Ipv4Addr;
893    ///
894    /// assert_eq!(Ipv4Addr::new(198, 17, 255, 255).is_benchmarking(), false);
895    /// assert_eq!(Ipv4Addr::new(198, 18, 0, 0).is_benchmarking(), true);
896    /// assert_eq!(Ipv4Addr::new(198, 19, 255, 255).is_benchmarking(), true);
897    /// assert_eq!(Ipv4Addr::new(198, 20, 0, 0).is_benchmarking(), false);
898    /// ```
899    #[unstable(feature = "ip", issue = "27709")]
900    #[must_use]
901    #[inline]
902    pub const fn is_benchmarking(&self) -> bool {
903        self.octets()[0] == 198 && (self.octets()[1] & 0xfe) == 18
904    }
905
906    /// Returns [`true`] if this address is reserved by IANA for future use.
907    ///
908    /// [IETF RFC 1112] defines the block of reserved addresses as `240.0.0.0/4`.
909    /// This range normally includes the broadcast address `255.255.255.255`, but
910    /// this implementation explicitly excludes it, since it is obviously not
911    /// reserved for future use.
912    ///
913    /// [IETF RFC 1112]: https://tools.ietf.org/html/rfc1112
914    ///
915    /// # Warning
916    ///
917    /// As IANA assigns new addresses, this method will be
918    /// updated. This may result in non-reserved addresses being
919    /// treated as reserved in code that relies on an outdated version
920    /// of this method.
921    ///
922    /// # Examples
923    ///
924    /// ```
925    /// #![feature(ip)]
926    /// use std::net::Ipv4Addr;
927    ///
928    /// assert_eq!(Ipv4Addr::new(240, 0, 0, 0).is_reserved(), true);
929    /// assert_eq!(Ipv4Addr::new(255, 255, 255, 254).is_reserved(), true);
930    ///
931    /// assert_eq!(Ipv4Addr::new(239, 255, 255, 255).is_reserved(), false);
932    /// // The broadcast address is not considered as reserved for future use by this implementation
933    /// assert_eq!(Ipv4Addr::new(255, 255, 255, 255).is_reserved(), false);
934    /// ```
935    #[unstable(feature = "ip", issue = "27709")]
936    #[must_use]
937    #[inline]
938    pub const fn is_reserved(&self) -> bool {
939        self.octets()[0] & 240 == 240 && !self.is_broadcast()
940    }
941
942    /// Returns [`true`] if this is a multicast address (`224.0.0.0/4`).
943    ///
944    /// Multicast addresses have a most significant octet between `224` and `239`,
945    /// and is defined by [IETF RFC 5771].
946    ///
947    /// [IETF RFC 5771]: https://tools.ietf.org/html/rfc5771
948    ///
949    /// # Examples
950    ///
951    /// ```
952    /// use std::net::Ipv4Addr;
953    ///
954    /// assert_eq!(Ipv4Addr::new(224, 254, 0, 0).is_multicast(), true);
955    /// assert_eq!(Ipv4Addr::new(236, 168, 10, 65).is_multicast(), true);
956    /// assert_eq!(Ipv4Addr::new(172, 16, 10, 65).is_multicast(), false);
957    /// ```
958    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
959    #[stable(since = "1.7.0", feature = "ip_17")]
960    #[must_use]
961    #[inline]
962    pub const fn is_multicast(&self) -> bool {
963        self.octets()[0] >= 224 && self.octets()[0] <= 239
964    }
965
966    /// Returns [`true`] if this is a broadcast address (`255.255.255.255`).
967    ///
968    /// A broadcast address has all octets set to `255` as defined in [IETF RFC 919].
969    ///
970    /// [IETF RFC 919]: https://tools.ietf.org/html/rfc919
971    ///
972    /// # Examples
973    ///
974    /// ```
975    /// use std::net::Ipv4Addr;
976    ///
977    /// assert_eq!(Ipv4Addr::new(255, 255, 255, 255).is_broadcast(), true);
978    /// assert_eq!(Ipv4Addr::new(236, 168, 10, 65).is_broadcast(), false);
979    /// ```
980    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
981    #[stable(since = "1.7.0", feature = "ip_17")]
982    #[must_use]
983    #[inline]
984    pub const fn is_broadcast(&self) -> bool {
985        u32::from_be_bytes(self.octets()) == u32::from_be_bytes(Self::BROADCAST.octets())
986    }
987
988    /// Returns [`true`] if this address is in a range designated for documentation.
989    ///
990    /// This is defined in [IETF RFC 5737]:
991    ///
992    /// - `192.0.2.0/24` (TEST-NET-1)
993    /// - `198.51.100.0/24` (TEST-NET-2)
994    /// - `203.0.113.0/24` (TEST-NET-3)
995    ///
996    /// [IETF RFC 5737]: https://tools.ietf.org/html/rfc5737
997    ///
998    /// # Examples
999    ///
1000    /// ```
1001    /// use std::net::Ipv4Addr;
1002    ///
1003    /// assert_eq!(Ipv4Addr::new(192, 0, 2, 255).is_documentation(), true);
1004    /// assert_eq!(Ipv4Addr::new(198, 51, 100, 65).is_documentation(), true);
1005    /// assert_eq!(Ipv4Addr::new(203, 0, 113, 6).is_documentation(), true);
1006    /// assert_eq!(Ipv4Addr::new(193, 34, 17, 19).is_documentation(), false);
1007    /// ```
1008    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1009    #[stable(since = "1.7.0", feature = "ip_17")]
1010    #[must_use]
1011    #[inline]
1012    pub const fn is_documentation(&self) -> bool {
1013        matches!(self.octets(), [192, 0, 2, _] | [198, 51, 100, _] | [203, 0, 113, _])
1014    }
1015
1016    /// Converts this address to an [IPv4-compatible] [`IPv6` address].
1017    ///
1018    /// `a.b.c.d` becomes `::a.b.c.d`
1019    ///
1020    /// Note that IPv4-compatible addresses have been officially deprecated.
1021    /// If you don't explicitly need an IPv4-compatible address for legacy reasons, consider using `to_ipv6_mapped` instead.
1022    ///
1023    /// [IPv4-compatible]: Ipv6Addr#ipv4-compatible-ipv6-addresses
1024    /// [`IPv6` address]: Ipv6Addr
1025    ///
1026    /// # Examples
1027    ///
1028    /// ```
1029    /// use std::net::{Ipv4Addr, Ipv6Addr};
1030    ///
1031    /// assert_eq!(
1032    ///     Ipv4Addr::new(192, 0, 2, 255).to_ipv6_compatible(),
1033    ///     Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0xc000, 0x2ff)
1034    /// );
1035    /// ```
1036    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1037    #[stable(feature = "rust1", since = "1.0.0")]
1038    #[must_use = "this returns the result of the operation, \
1039                  without modifying the original"]
1040    #[inline]
1041    pub const fn to_ipv6_compatible(&self) -> Ipv6Addr {
1042        let [a, b, c, d] = self.octets();
1043        Ipv6Addr { octets: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, b, c, d] }
1044    }
1045
1046    /// Converts this address to an [IPv4-mapped] [`IPv6` address].
1047    ///
1048    /// `a.b.c.d` becomes `::ffff:a.b.c.d`
1049    ///
1050    /// [IPv4-mapped]: Ipv6Addr#ipv4-mapped-ipv6-addresses
1051    /// [`IPv6` address]: Ipv6Addr
1052    ///
1053    /// # Examples
1054    ///
1055    /// ```
1056    /// use std::net::{Ipv4Addr, Ipv6Addr};
1057    ///
1058    /// assert_eq!(Ipv4Addr::new(192, 0, 2, 255).to_ipv6_mapped(),
1059    ///            Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc000, 0x2ff));
1060    /// ```
1061    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1062    #[stable(feature = "rust1", since = "1.0.0")]
1063    #[must_use = "this returns the result of the operation, \
1064                  without modifying the original"]
1065    #[inline]
1066    pub const fn to_ipv6_mapped(&self) -> Ipv6Addr {
1067        let [a, b, c, d] = self.octets();
1068        Ipv6Addr { octets: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xFF, 0xFF, a, b, c, d] }
1069    }
1070}
1071
1072#[stable(feature = "ip_addr", since = "1.7.0")]
1073impl fmt::Display for IpAddr {
1074    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1075        match self {
1076            IpAddr::V4(ip) => ip.fmt(fmt),
1077            IpAddr::V6(ip) => ip.fmt(fmt),
1078        }
1079    }
1080}
1081
1082#[stable(feature = "ip_addr", since = "1.7.0")]
1083impl fmt::Debug for IpAddr {
1084    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1085        fmt::Display::fmt(self, fmt)
1086    }
1087}
1088
1089#[stable(feature = "ip_from_ip", since = "1.16.0")]
1090#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1091impl const From<Ipv4Addr> for IpAddr {
1092    /// Copies this address to a new `IpAddr::V4`.
1093    ///
1094    /// # Examples
1095    ///
1096    /// ```
1097    /// use std::net::{IpAddr, Ipv4Addr};
1098    ///
1099    /// let addr = Ipv4Addr::new(127, 0, 0, 1);
1100    ///
1101    /// assert_eq!(
1102    ///     IpAddr::V4(addr),
1103    ///     IpAddr::from(addr)
1104    /// )
1105    /// ```
1106    #[inline]
1107    fn from(ipv4: Ipv4Addr) -> IpAddr {
1108        IpAddr::V4(ipv4)
1109    }
1110}
1111
1112#[stable(feature = "ip_from_ip", since = "1.16.0")]
1113#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1114impl const From<Ipv6Addr> for IpAddr {
1115    /// Copies this address to a new `IpAddr::V6`.
1116    ///
1117    /// # Examples
1118    ///
1119    /// ```
1120    /// use std::net::{IpAddr, Ipv6Addr};
1121    ///
1122    /// let addr = Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff);
1123    ///
1124    /// assert_eq!(
1125    ///     IpAddr::V6(addr),
1126    ///     IpAddr::from(addr)
1127    /// );
1128    /// ```
1129    #[inline]
1130    fn from(ipv6: Ipv6Addr) -> IpAddr {
1131        IpAddr::V6(ipv6)
1132    }
1133}
1134
1135#[stable(feature = "rust1", since = "1.0.0")]
1136impl fmt::Display for Ipv4Addr {
1137    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1138        let octets = self.octets();
1139
1140        // If there are no alignment requirements, write the IP address directly to `f`.
1141        // Otherwise, write it to a local buffer and then use `f.pad`.
1142        if fmt.precision().is_none() && fmt.width().is_none() {
1143            write!(fmt, "{}.{}.{}.{}", octets[0], octets[1], octets[2], octets[3])
1144        } else {
1145            const LONGEST_IPV4_ADDR: &str = "255.255.255.255";
1146
1147            let mut buf = DisplayBuffer::<{ LONGEST_IPV4_ADDR.len() }>::new();
1148            // Buffer is long enough for the longest possible IPv4 address, so this should never fail.
1149            write!(buf, "{}.{}.{}.{}", octets[0], octets[1], octets[2], octets[3]).unwrap();
1150
1151            fmt.pad(buf.as_str())
1152        }
1153    }
1154}
1155
1156#[stable(feature = "rust1", since = "1.0.0")]
1157impl fmt::Debug for Ipv4Addr {
1158    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1159        fmt::Display::fmt(self, fmt)
1160    }
1161}
1162
1163#[stable(feature = "ip_cmp", since = "1.16.0")]
1164impl PartialEq<Ipv4Addr> for IpAddr {
1165    #[inline]
1166    fn eq(&self, other: &Ipv4Addr) -> bool {
1167        match self {
1168            IpAddr::V4(v4) => v4 == other,
1169            IpAddr::V6(_) => false,
1170        }
1171    }
1172}
1173
1174#[stable(feature = "ip_cmp", since = "1.16.0")]
1175impl PartialEq<IpAddr> for Ipv4Addr {
1176    #[inline]
1177    fn eq(&self, other: &IpAddr) -> bool {
1178        match other {
1179            IpAddr::V4(v4) => self == v4,
1180            IpAddr::V6(_) => false,
1181        }
1182    }
1183}
1184
1185#[stable(feature = "rust1", since = "1.0.0")]
1186impl PartialOrd for Ipv4Addr {
1187    #[inline]
1188    fn partial_cmp(&self, other: &Ipv4Addr) -> Option<Ordering> {
1189        Some(self.cmp(other))
1190    }
1191}
1192
1193#[stable(feature = "ip_cmp", since = "1.16.0")]
1194impl PartialOrd<Ipv4Addr> for IpAddr {
1195    #[inline]
1196    fn partial_cmp(&self, other: &Ipv4Addr) -> Option<Ordering> {
1197        match self {
1198            IpAddr::V4(v4) => v4.partial_cmp(other),
1199            IpAddr::V6(_) => Some(Ordering::Greater),
1200        }
1201    }
1202}
1203
1204#[stable(feature = "ip_cmp", since = "1.16.0")]
1205impl PartialOrd<IpAddr> for Ipv4Addr {
1206    #[inline]
1207    fn partial_cmp(&self, other: &IpAddr) -> Option<Ordering> {
1208        match other {
1209            IpAddr::V4(v4) => self.partial_cmp(v4),
1210            IpAddr::V6(_) => Some(Ordering::Less),
1211        }
1212    }
1213}
1214
1215#[stable(feature = "rust1", since = "1.0.0")]
1216impl Ord for Ipv4Addr {
1217    #[inline]
1218    fn cmp(&self, other: &Ipv4Addr) -> Ordering {
1219        self.octets.cmp(&other.octets)
1220    }
1221}
1222
1223#[stable(feature = "ip_u32", since = "1.1.0")]
1224#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1225impl const From<Ipv4Addr> for u32 {
1226    /// Uses [`Ipv4Addr::to_bits`] to convert an IPv4 address to a host byte order `u32`.
1227    #[inline]
1228    fn from(ip: Ipv4Addr) -> u32 {
1229        ip.to_bits()
1230    }
1231}
1232
1233#[stable(feature = "ip_u32", since = "1.1.0")]
1234#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1235impl const From<u32> for Ipv4Addr {
1236    /// Uses [`Ipv4Addr::from_bits`] to convert a host byte order `u32` into an IPv4 address.
1237    #[inline]
1238    fn from(ip: u32) -> Ipv4Addr {
1239        Ipv4Addr::from_bits(ip)
1240    }
1241}
1242
1243#[stable(feature = "from_slice_v4", since = "1.9.0")]
1244#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1245impl const From<[u8; 4]> for Ipv4Addr {
1246    /// Creates an `Ipv4Addr` from a four element byte array.
1247    ///
1248    /// # Examples
1249    ///
1250    /// ```
1251    /// use std::net::Ipv4Addr;
1252    ///
1253    /// let addr = Ipv4Addr::from([13u8, 12u8, 11u8, 10u8]);
1254    /// assert_eq!(Ipv4Addr::new(13, 12, 11, 10), addr);
1255    /// ```
1256    #[inline]
1257    fn from(octets: [u8; 4]) -> Ipv4Addr {
1258        Ipv4Addr { octets }
1259    }
1260}
1261
1262#[stable(feature = "ip_from_slice", since = "1.17.0")]
1263#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1264impl const From<[u8; 4]> for IpAddr {
1265    /// Creates an `IpAddr::V4` from a four element byte array.
1266    ///
1267    /// # Examples
1268    ///
1269    /// ```
1270    /// use std::net::{IpAddr, Ipv4Addr};
1271    ///
1272    /// let addr = IpAddr::from([13u8, 12u8, 11u8, 10u8]);
1273    /// assert_eq!(IpAddr::V4(Ipv4Addr::new(13, 12, 11, 10)), addr);
1274    /// ```
1275    #[inline]
1276    fn from(octets: [u8; 4]) -> IpAddr {
1277        IpAddr::V4(Ipv4Addr::from(octets))
1278    }
1279}
1280
1281impl Ipv6Addr {
1282    /// Creates a new IPv6 address from eight 16-bit segments.
1283    ///
1284    /// The result will represent the IP address `a:b:c:d:e:f:g:h`.
1285    ///
1286    /// # Examples
1287    ///
1288    /// ```
1289    /// use std::net::Ipv6Addr;
1290    ///
1291    /// let addr = Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff);
1292    /// ```
1293    #[rustc_const_stable(feature = "const_ip_32", since = "1.32.0")]
1294    #[stable(feature = "rust1", since = "1.0.0")]
1295    #[must_use]
1296    #[inline]
1297    pub const fn new(a: u16, b: u16, c: u16, d: u16, e: u16, f: u16, g: u16, h: u16) -> Ipv6Addr {
1298        let addr16 = [
1299            a.to_be(),
1300            b.to_be(),
1301            c.to_be(),
1302            d.to_be(),
1303            e.to_be(),
1304            f.to_be(),
1305            g.to_be(),
1306            h.to_be(),
1307        ];
1308        Ipv6Addr {
1309            // All elements in `addr16` are big endian.
1310            // SAFETY: `[u16; 8]` is always safe to transmute to `[u8; 16]`.
1311            octets: unsafe { transmute::<_, [u8; 16]>(addr16) },
1312        }
1313    }
1314
1315    /// The size of an IPv6 address in bits.
1316    ///
1317    /// # Examples
1318    ///
1319    /// ```
1320    /// use std::net::Ipv6Addr;
1321    ///
1322    /// assert_eq!(Ipv6Addr::BITS, 128);
1323    /// ```
1324    #[stable(feature = "ip_bits", since = "1.80.0")]
1325    pub const BITS: u32 = 128;
1326
1327    /// Converts an IPv6 address into a `u128` representation using native byte order.
1328    ///
1329    /// Although IPv6 addresses are big-endian, the `u128` value will use the target platform's
1330    /// native byte order. That is, the `u128` value is an integer representation of the IPv6
1331    /// address and not an integer interpretation of the IPv6 address's big-endian bitstring. This
1332    /// means that the `u128` value masked with `0xffffffffffffffffffffffffffff0000_u128` will set
1333    /// the last segment in the address to 0, regardless of the target platform's endianness.
1334    ///
1335    /// # Examples
1336    ///
1337    /// ```
1338    /// use std::net::Ipv6Addr;
1339    ///
1340    /// let addr = Ipv6Addr::new(
1341    ///     0x1020, 0x3040, 0x5060, 0x7080,
1342    ///     0x90A0, 0xB0C0, 0xD0E0, 0xF00D,
1343    /// );
1344    /// assert_eq!(0x102030405060708090A0B0C0D0E0F00D_u128, addr.to_bits());
1345    /// ```
1346    ///
1347    /// ```
1348    /// use std::net::Ipv6Addr;
1349    ///
1350    /// let addr = Ipv6Addr::new(
1351    ///     0x1020, 0x3040, 0x5060, 0x7080,
1352    ///     0x90A0, 0xB0C0, 0xD0E0, 0xF00D,
1353    /// );
1354    /// let addr_bits = addr.to_bits() & 0xffffffffffffffffffffffffffff0000_u128;
1355    /// assert_eq!(
1356    ///     Ipv6Addr::new(
1357    ///         0x1020, 0x3040, 0x5060, 0x7080,
1358    ///         0x90A0, 0xB0C0, 0xD0E0, 0x0000,
1359    ///     ),
1360    ///     Ipv6Addr::from_bits(addr_bits));
1361    ///
1362    /// ```
1363    #[rustc_const_stable(feature = "ip_bits", since = "1.80.0")]
1364    #[stable(feature = "ip_bits", since = "1.80.0")]
1365    #[must_use]
1366    #[inline]
1367    pub const fn to_bits(self) -> u128 {
1368        u128::from_be_bytes(self.octets)
1369    }
1370
1371    /// Converts a native byte order `u128` into an IPv6 address.
1372    ///
1373    /// See [`Ipv6Addr::to_bits`] for an explanation on endianness.
1374    ///
1375    /// # Examples
1376    ///
1377    /// ```
1378    /// use std::net::Ipv6Addr;
1379    ///
1380    /// let addr = Ipv6Addr::from_bits(0x102030405060708090A0B0C0D0E0F00D_u128);
1381    /// assert_eq!(
1382    ///     Ipv6Addr::new(
1383    ///         0x1020, 0x3040, 0x5060, 0x7080,
1384    ///         0x90A0, 0xB0C0, 0xD0E0, 0xF00D,
1385    ///     ),
1386    ///     addr);
1387    /// ```
1388    #[rustc_const_stable(feature = "ip_bits", since = "1.80.0")]
1389    #[stable(feature = "ip_bits", since = "1.80.0")]
1390    #[must_use]
1391    #[inline]
1392    pub const fn from_bits(bits: u128) -> Ipv6Addr {
1393        Ipv6Addr { octets: bits.to_be_bytes() }
1394    }
1395
1396    /// An IPv6 address representing localhost: `::1`.
1397    ///
1398    /// This corresponds to constant `IN6ADDR_LOOPBACK_INIT` or `in6addr_loopback` in other
1399    /// languages.
1400    ///
1401    /// # Examples
1402    ///
1403    /// ```
1404    /// use std::net::Ipv6Addr;
1405    ///
1406    /// let addr = Ipv6Addr::LOCALHOST;
1407    /// assert_eq!(addr, Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1));
1408    /// ```
1409    #[doc(alias = "IN6ADDR_LOOPBACK_INIT")]
1410    #[doc(alias = "in6addr_loopback")]
1411    #[stable(feature = "ip_constructors", since = "1.30.0")]
1412    pub const LOCALHOST: Self = Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1);
1413
1414    /// An IPv6 address representing the unspecified address: `::`.
1415    ///
1416    /// This corresponds to constant `IN6ADDR_ANY_INIT` or `in6addr_any` in other languages.
1417    ///
1418    /// # Examples
1419    ///
1420    /// ```
1421    /// use std::net::Ipv6Addr;
1422    ///
1423    /// let addr = Ipv6Addr::UNSPECIFIED;
1424    /// assert_eq!(addr, Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0));
1425    /// ```
1426    #[doc(alias = "IN6ADDR_ANY_INIT")]
1427    #[doc(alias = "in6addr_any")]
1428    #[stable(feature = "ip_constructors", since = "1.30.0")]
1429    pub const UNSPECIFIED: Self = Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0);
1430
1431    /// Returns the eight 16-bit segments that make up this address.
1432    ///
1433    /// # Examples
1434    ///
1435    /// ```
1436    /// use std::net::Ipv6Addr;
1437    ///
1438    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).segments(),
1439    ///            [0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff]);
1440    /// ```
1441    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1442    #[stable(feature = "rust1", since = "1.0.0")]
1443    #[must_use]
1444    #[inline]
1445    pub const fn segments(&self) -> [u16; 8] {
1446        // All elements in `self.octets` must be big endian.
1447        // SAFETY: `[u8; 16]` is always safe to transmute to `[u16; 8]`.
1448        let [a, b, c, d, e, f, g, h] = unsafe { transmute::<_, [u16; 8]>(self.octets) };
1449        // We want native endian u16
1450        [
1451            u16::from_be(a),
1452            u16::from_be(b),
1453            u16::from_be(c),
1454            u16::from_be(d),
1455            u16::from_be(e),
1456            u16::from_be(f),
1457            u16::from_be(g),
1458            u16::from_be(h),
1459        ]
1460    }
1461
1462    /// Creates an `Ipv6Addr` from an eight element 16-bit array.
1463    ///
1464    /// # Examples
1465    ///
1466    /// ```
1467    /// use std::net::Ipv6Addr;
1468    ///
1469    /// let addr = Ipv6Addr::from_segments([
1470    ///     0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
1471    ///     0x209u16, 0x208u16, 0x207u16, 0x206u16,
1472    /// ]);
1473    /// assert_eq!(
1474    ///     Ipv6Addr::new(
1475    ///         0x20d, 0x20c, 0x20b, 0x20a,
1476    ///         0x209, 0x208, 0x207, 0x206,
1477    ///     ),
1478    ///     addr
1479    /// );
1480    /// ```
1481    #[stable(feature = "ip_from", since = "1.91.0")]
1482    #[rustc_const_stable(feature = "ip_from", since = "1.91.0")]
1483    #[must_use]
1484    #[inline]
1485    pub const fn from_segments(segments: [u16; 8]) -> Ipv6Addr {
1486        let [a, b, c, d, e, f, g, h] = segments;
1487        Ipv6Addr::new(a, b, c, d, e, f, g, h)
1488    }
1489
1490    /// Returns [`true`] for the special 'unspecified' address (`::`).
1491    ///
1492    /// This property is defined in [IETF RFC 4291].
1493    ///
1494    /// [IETF RFC 4291]: https://tools.ietf.org/html/rfc4291
1495    ///
1496    /// # Examples
1497    ///
1498    /// ```
1499    /// use std::net::Ipv6Addr;
1500    ///
1501    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_unspecified(), false);
1502    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0).is_unspecified(), true);
1503    /// ```
1504    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1505    #[stable(since = "1.7.0", feature = "ip_17")]
1506    #[must_use]
1507    #[inline]
1508    pub const fn is_unspecified(&self) -> bool {
1509        u128::from_be_bytes(self.octets()) == u128::from_be_bytes(Ipv6Addr::UNSPECIFIED.octets())
1510    }
1511
1512    /// Returns [`true`] if this is the [loopback address] (`::1`),
1513    /// as defined in [IETF RFC 4291 section 2.5.3].
1514    ///
1515    /// Contrary to IPv4, in IPv6 there is only one loopback address.
1516    ///
1517    /// [loopback address]: Ipv6Addr::LOCALHOST
1518    /// [IETF RFC 4291 section 2.5.3]: https://tools.ietf.org/html/rfc4291#section-2.5.3
1519    ///
1520    /// # Examples
1521    ///
1522    /// ```
1523    /// use std::net::Ipv6Addr;
1524    ///
1525    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_loopback(), false);
1526    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 0x1).is_loopback(), true);
1527    /// ```
1528    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1529    #[stable(since = "1.7.0", feature = "ip_17")]
1530    #[must_use]
1531    #[inline]
1532    pub const fn is_loopback(&self) -> bool {
1533        u128::from_be_bytes(self.octets()) == u128::from_be_bytes(Ipv6Addr::LOCALHOST.octets())
1534    }
1535
1536    /// Returns [`true`] if the address appears to be globally reachable
1537    /// as specified by the [IANA IPv6 Special-Purpose Address Registry].
1538    ///
1539    /// Whether or not an address is practically reachable will depend on your
1540    /// network configuration. Most IPv6 addresses are globally reachable, unless
1541    /// they are specifically defined as *not* globally reachable.
1542    ///
1543    /// Non-exhaustive list of notable addresses that are not globally reachable:
1544    /// - The [unspecified address] ([`is_unspecified`](Ipv6Addr::is_unspecified))
1545    /// - The [loopback address] ([`is_loopback`](Ipv6Addr::is_loopback))
1546    /// - IPv4-mapped addresses
1547    /// - Addresses reserved for benchmarking ([`is_benchmarking`](Ipv6Addr::is_benchmarking))
1548    /// - Addresses reserved for documentation ([`is_documentation`](Ipv6Addr::is_documentation))
1549    /// - Unique local addresses ([`is_unique_local`](Ipv6Addr::is_unique_local))
1550    /// - Unicast addresses with link-local scope ([`is_unicast_link_local`](Ipv6Addr::is_unicast_link_local))
1551    ///
1552    /// For the complete overview of which addresses are globally reachable, see the table at the [IANA IPv6 Special-Purpose Address Registry].
1553    ///
1554    /// Note that an address having global scope is not the same as being globally reachable,
1555    /// and there is no direct relation between the two concepts: There exist addresses with global scope
1556    /// that are not globally reachable (for example unique local addresses),
1557    /// and addresses that are globally reachable without having global scope
1558    /// (multicast addresses with non-global scope).
1559    ///
1560    /// [IANA IPv6 Special-Purpose Address Registry]: https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml
1561    /// [unspecified address]: Ipv6Addr::UNSPECIFIED
1562    /// [loopback address]: Ipv6Addr::LOCALHOST
1563    ///
1564    /// # Examples
1565    ///
1566    /// ```
1567    /// #![feature(ip)]
1568    ///
1569    /// use std::net::Ipv6Addr;
1570    ///
1571    /// // Most IPv6 addresses are globally reachable:
1572    /// assert_eq!(Ipv6Addr::new(0x26, 0, 0x1c9, 0, 0, 0xafc8, 0x10, 0x1).is_global(), true);
1573    ///
1574    /// // However some addresses have been assigned a special meaning
1575    /// // that makes them not globally reachable. Some examples are:
1576    ///
1577    /// // The unspecified address (`::`)
1578    /// assert_eq!(Ipv6Addr::UNSPECIFIED.is_global(), false);
1579    ///
1580    /// // The loopback address (`::1`)
1581    /// assert_eq!(Ipv6Addr::LOCALHOST.is_global(), false);
1582    ///
1583    /// // IPv4-mapped addresses (`::ffff:0:0/96`)
1584    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_global(), false);
1585    ///
1586    /// // Addresses reserved for benchmarking (`2001:2::/48`)
1587    /// assert_eq!(Ipv6Addr::new(0x2001, 2, 0, 0, 0, 0, 0, 1,).is_global(), false);
1588    ///
1589    /// // Addresses reserved for documentation (`2001:db8::/32` and `3fff::/20`)
1590    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 1).is_global(), false);
1591    /// assert_eq!(Ipv6Addr::new(0x3fff, 0, 0, 0, 0, 0, 0, 0).is_global(), false);
1592    ///
1593    /// // Unique local addresses (`fc00::/7`)
1594    /// assert_eq!(Ipv6Addr::new(0xfc02, 0, 0, 0, 0, 0, 0, 1).is_global(), false);
1595    ///
1596    /// // Unicast addresses with link-local scope (`fe80::/10`)
1597    /// assert_eq!(Ipv6Addr::new(0xfe81, 0, 0, 0, 0, 0, 0, 1).is_global(), false);
1598    ///
1599    /// // For a complete overview see the IANA IPv6 Special-Purpose Address Registry.
1600    /// ```
1601    #[unstable(feature = "ip", issue = "27709")]
1602    #[must_use]
1603    #[inline]
1604    pub const fn is_global(&self) -> bool {
1605        !(self.is_unspecified()
1606            || self.is_loopback()
1607            // IPv4-mapped Address (`::ffff:0:0/96`)
1608            || matches!(self.segments(), [0, 0, 0, 0, 0, 0xffff, _, _])
1609            // IPv4-IPv6 Translat. (`64:ff9b:1::/48`)
1610            || matches!(self.segments(), [0x64, 0xff9b, 1, _, _, _, _, _])
1611            // Discard-Only Address Block (`100::/64`)
1612            || matches!(self.segments(), [0x100, 0, 0, 0, _, _, _, _])
1613            // IETF Protocol Assignments (`2001::/23`)
1614            || (matches!(self.segments(), [0x2001, b, _, _, _, _, _, _] if b < 0x200)
1615                && !(
1616                    // Port Control Protocol Anycast (`2001:1::1`)
1617                    u128::from_be_bytes(self.octets()) == 0x2001_0001_0000_0000_0000_0000_0000_0001
1618                    // Traversal Using Relays around NAT Anycast (`2001:1::2`)
1619                    || u128::from_be_bytes(self.octets()) == 0x2001_0001_0000_0000_0000_0000_0000_0002
1620                    // AMT (`2001:3::/32`)
1621                    || matches!(self.segments(), [0x2001, 3, _, _, _, _, _, _])
1622                    // AS112-v6 (`2001:4:112::/48`)
1623                    || matches!(self.segments(), [0x2001, 4, 0x112, _, _, _, _, _])
1624                    // ORCHIDv2 (`2001:20::/28`)
1625                    // Drone Remote ID Protocol Entity Tags (DETs) Prefix (`2001:30::/28`)`
1626                    || matches!(self.segments(), [0x2001, b, _, _, _, _, _, _] if b >= 0x20 && b <= 0x3F)
1627                ))
1628            // 6to4 (`2002::/16`) – it's not explicitly documented as globally reachable,
1629            // IANA says N/A.
1630            || matches!(self.segments(), [0x2002, _, _, _, _, _, _, _])
1631            || self.is_documentation()
1632            // Segment Routing (SRv6) SIDs (`5f00::/16`)
1633            || matches!(self.segments(), [0x5f00, ..])
1634            || self.is_unique_local()
1635            || self.is_unicast_link_local())
1636    }
1637
1638    /// Returns [`true`] if this is a unique local address (`fc00::/7`).
1639    ///
1640    /// This property is defined in [IETF RFC 4193].
1641    ///
1642    /// [IETF RFC 4193]: https://tools.ietf.org/html/rfc4193
1643    ///
1644    /// # Examples
1645    ///
1646    /// ```
1647    /// use std::net::Ipv6Addr;
1648    ///
1649    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_unique_local(), false);
1650    /// assert_eq!(Ipv6Addr::new(0xfc02, 0, 0, 0, 0, 0, 0, 0).is_unique_local(), true);
1651    /// ```
1652    #[must_use]
1653    #[inline]
1654    #[stable(feature = "ipv6_is_unique_local", since = "1.84.0")]
1655    #[rustc_const_stable(feature = "ipv6_is_unique_local", since = "1.84.0")]
1656    pub const fn is_unique_local(&self) -> bool {
1657        (self.segments()[0] & 0xfe00) == 0xfc00
1658    }
1659
1660    /// Returns [`true`] if this is a unicast address, as defined by [IETF RFC 4291].
1661    /// Any address that is not a [multicast address] (`ff00::/8`) is unicast.
1662    ///
1663    /// [IETF RFC 4291]: https://tools.ietf.org/html/rfc4291
1664    /// [multicast address]: Ipv6Addr::is_multicast
1665    ///
1666    /// # Examples
1667    ///
1668    /// ```
1669    /// #![feature(ip)]
1670    ///
1671    /// use std::net::Ipv6Addr;
1672    ///
1673    /// // The unspecified and loopback addresses are unicast.
1674    /// assert_eq!(Ipv6Addr::UNSPECIFIED.is_unicast(), true);
1675    /// assert_eq!(Ipv6Addr::LOCALHOST.is_unicast(), true);
1676    ///
1677    /// // Any address that is not a multicast address (`ff00::/8`) is unicast.
1678    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0).is_unicast(), true);
1679    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).is_unicast(), false);
1680    /// ```
1681    #[unstable(feature = "ip", issue = "27709")]
1682    #[must_use]
1683    #[inline]
1684    pub const fn is_unicast(&self) -> bool {
1685        !self.is_multicast()
1686    }
1687
1688    /// Returns `true` if the address is a unicast address with link-local scope,
1689    /// as defined in [RFC 4291].
1690    ///
1691    /// A unicast address has link-local scope if it has the prefix `fe80::/10`, as per [RFC 4291 section 2.4].
1692    /// Note that this encompasses more addresses than those defined in [RFC 4291 section 2.5.6],
1693    /// which describes "Link-Local IPv6 Unicast Addresses" as having the following stricter format:
1694    ///
1695    /// ```text
1696    /// | 10 bits  |         54 bits         |          64 bits           |
1697    /// +----------+-------------------------+----------------------------+
1698    /// |1111111010|           0             |       interface ID         |
1699    /// +----------+-------------------------+----------------------------+
1700    /// ```
1701    /// So while currently the only addresses with link-local scope an application will encounter are all in `fe80::/64`,
1702    /// this might change in the future with the publication of new standards. More addresses in `fe80::/10` could be allocated,
1703    /// and those addresses will have link-local scope.
1704    ///
1705    /// Also note that while [RFC 4291 section 2.5.3] mentions about the [loopback address] (`::1`) that "it is treated as having Link-Local scope",
1706    /// this does not mean that the loopback address actually has link-local scope and this method will return `false` on it.
1707    ///
1708    /// [RFC 4291]: https://tools.ietf.org/html/rfc4291
1709    /// [RFC 4291 section 2.4]: https://tools.ietf.org/html/rfc4291#section-2.4
1710    /// [RFC 4291 section 2.5.3]: https://tools.ietf.org/html/rfc4291#section-2.5.3
1711    /// [RFC 4291 section 2.5.6]: https://tools.ietf.org/html/rfc4291#section-2.5.6
1712    /// [loopback address]: Ipv6Addr::LOCALHOST
1713    ///
1714    /// # Examples
1715    ///
1716    /// ```
1717    /// use std::net::Ipv6Addr;
1718    ///
1719    /// // The loopback address (`::1`) does not actually have link-local scope.
1720    /// assert_eq!(Ipv6Addr::LOCALHOST.is_unicast_link_local(), false);
1721    ///
1722    /// // Only addresses in `fe80::/10` have link-local scope.
1723    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0).is_unicast_link_local(), false);
1724    /// assert_eq!(Ipv6Addr::new(0xfe80, 0, 0, 0, 0, 0, 0, 0).is_unicast_link_local(), true);
1725    ///
1726    /// // Addresses outside the stricter `fe80::/64` also have link-local scope.
1727    /// assert_eq!(Ipv6Addr::new(0xfe80, 0, 0, 1, 0, 0, 0, 0).is_unicast_link_local(), true);
1728    /// assert_eq!(Ipv6Addr::new(0xfe81, 0, 0, 0, 0, 0, 0, 0).is_unicast_link_local(), true);
1729    /// ```
1730    #[must_use]
1731    #[inline]
1732    #[stable(feature = "ipv6_is_unique_local", since = "1.84.0")]
1733    #[rustc_const_stable(feature = "ipv6_is_unique_local", since = "1.84.0")]
1734    pub const fn is_unicast_link_local(&self) -> bool {
1735        (self.segments()[0] & 0xffc0) == 0xfe80
1736    }
1737
1738    /// Returns [`true`] if this is an address reserved for documentation
1739    /// (`2001:db8::/32` and `3fff::/20`).
1740    ///
1741    /// This property is defined by [IETF RFC 3849] and [IETF RFC 9637].
1742    ///
1743    /// [IETF RFC 3849]: https://tools.ietf.org/html/rfc3849
1744    /// [IETF RFC 9637]: https://tools.ietf.org/html/rfc9637
1745    ///
1746    /// # Examples
1747    ///
1748    /// ```
1749    /// #![feature(ip)]
1750    ///
1751    /// use std::net::Ipv6Addr;
1752    ///
1753    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_documentation(), false);
1754    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0).is_documentation(), true);
1755    /// assert_eq!(Ipv6Addr::new(0x3fff, 0, 0, 0, 0, 0, 0, 0).is_documentation(), true);
1756    /// ```
1757    #[unstable(feature = "ip", issue = "27709")]
1758    #[must_use]
1759    #[inline]
1760    pub const fn is_documentation(&self) -> bool {
1761        matches!(self.segments(), [0x2001, 0xdb8, ..] | [0x3fff, 0..=0x0fff, ..])
1762    }
1763
1764    /// Returns [`true`] if this is an address reserved for benchmarking (`2001:2::/48`).
1765    ///
1766    /// This property is defined in [IETF RFC 5180], where it is mistakenly specified as covering the range `2001:0200::/48`.
1767    /// This is corrected in [IETF RFC Errata 1752] to `2001:0002::/48`.
1768    ///
1769    /// [IETF RFC 5180]: https://tools.ietf.org/html/rfc5180
1770    /// [IETF RFC Errata 1752]: https://www.rfc-editor.org/errata_search.php?eid=1752
1771    ///
1772    /// ```
1773    /// #![feature(ip)]
1774    ///
1775    /// use std::net::Ipv6Addr;
1776    ///
1777    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc613, 0x0).is_benchmarking(), false);
1778    /// assert_eq!(Ipv6Addr::new(0x2001, 0x2, 0, 0, 0, 0, 0, 0).is_benchmarking(), true);
1779    /// ```
1780    #[unstable(feature = "ip", issue = "27709")]
1781    #[must_use]
1782    #[inline]
1783    pub const fn is_benchmarking(&self) -> bool {
1784        (self.segments()[0] == 0x2001) && (self.segments()[1] == 0x2) && (self.segments()[2] == 0)
1785    }
1786
1787    /// Returns [`true`] if the address is a globally routable unicast address.
1788    ///
1789    /// The following return false:
1790    ///
1791    /// - the loopback address
1792    /// - the link-local addresses
1793    /// - unique local addresses
1794    /// - the unspecified address
1795    /// - the address range reserved for documentation
1796    ///
1797    /// This method returns [`true`] for site-local addresses as per [RFC 4291 section 2.5.7]
1798    ///
1799    /// ```no_rust
1800    /// The special behavior of [the site-local unicast] prefix defined in [RFC3513] must no longer
1801    /// be supported in new implementations (i.e., new implementations must treat this prefix as
1802    /// Global Unicast).
1803    /// ```
1804    ///
1805    /// [RFC 4291 section 2.5.7]: https://tools.ietf.org/html/rfc4291#section-2.5.7
1806    ///
1807    /// # Examples
1808    ///
1809    /// ```
1810    /// #![feature(ip)]
1811    ///
1812    /// use std::net::Ipv6Addr;
1813    ///
1814    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0).is_unicast_global(), false);
1815    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_unicast_global(), true);
1816    /// ```
1817    #[unstable(feature = "ip", issue = "27709")]
1818    #[must_use]
1819    #[inline]
1820    pub const fn is_unicast_global(&self) -> bool {
1821        self.is_unicast()
1822            && !self.is_loopback()
1823            && !self.is_unicast_link_local()
1824            && !self.is_unique_local()
1825            && !self.is_unspecified()
1826            && !self.is_documentation()
1827            && !self.is_benchmarking()
1828    }
1829
1830    /// Returns the address's multicast scope if the address is multicast.
1831    ///
1832    /// # Examples
1833    ///
1834    /// ```
1835    /// #![feature(ip)]
1836    ///
1837    /// use std::net::{Ipv6Addr, Ipv6MulticastScope};
1838    ///
1839    /// assert_eq!(
1840    ///     Ipv6Addr::new(0xff0e, 0, 0, 0, 0, 0, 0, 0).multicast_scope(),
1841    ///     Some(Ipv6MulticastScope::Global)
1842    /// );
1843    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).multicast_scope(), None);
1844    /// ```
1845    #[unstable(feature = "ip", issue = "27709")]
1846    #[must_use]
1847    #[inline]
1848    pub const fn multicast_scope(&self) -> Option<Ipv6MulticastScope> {
1849        if self.is_multicast() {
1850            match self.segments()[0] & 0x000f {
1851                1 => Some(Ipv6MulticastScope::InterfaceLocal),
1852                2 => Some(Ipv6MulticastScope::LinkLocal),
1853                3 => Some(Ipv6MulticastScope::RealmLocal),
1854                4 => Some(Ipv6MulticastScope::AdminLocal),
1855                5 => Some(Ipv6MulticastScope::SiteLocal),
1856                8 => Some(Ipv6MulticastScope::OrganizationLocal),
1857                14 => Some(Ipv6MulticastScope::Global),
1858                _ => None,
1859            }
1860        } else {
1861            None
1862        }
1863    }
1864
1865    /// Returns [`true`] if this is a multicast address (`ff00::/8`).
1866    ///
1867    /// This property is defined by [IETF RFC 4291].
1868    ///
1869    /// [IETF RFC 4291]: https://tools.ietf.org/html/rfc4291
1870    ///
1871    /// # Examples
1872    ///
1873    /// ```
1874    /// use std::net::Ipv6Addr;
1875    ///
1876    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).is_multicast(), true);
1877    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).is_multicast(), false);
1878    /// ```
1879    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1880    #[stable(since = "1.7.0", feature = "ip_17")]
1881    #[must_use]
1882    #[inline]
1883    pub const fn is_multicast(&self) -> bool {
1884        (self.segments()[0] & 0xff00) == 0xff00
1885    }
1886
1887    /// Returns [`true`] if the address is an IPv4-mapped address (`::ffff:0:0/96`).
1888    ///
1889    /// IPv4-mapped addresses can be converted to their canonical IPv4 address with
1890    /// [`to_ipv4_mapped`](Ipv6Addr::to_ipv4_mapped).
1891    ///
1892    /// # Examples
1893    /// ```
1894    /// #![feature(ip)]
1895    ///
1896    /// use std::net::{Ipv4Addr, Ipv6Addr};
1897    ///
1898    /// let ipv4_mapped = Ipv4Addr::new(192, 0, 2, 255).to_ipv6_mapped();
1899    /// assert_eq!(ipv4_mapped.is_ipv4_mapped(), true);
1900    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc000, 0x2ff).is_ipv4_mapped(), true);
1901    ///
1902    /// assert_eq!(Ipv6Addr::new(0x2001, 0xdb8, 0, 0, 0, 0, 0, 0).is_ipv4_mapped(), false);
1903    /// ```
1904    #[unstable(feature = "ip", issue = "27709")]
1905    #[must_use]
1906    #[inline]
1907    pub const fn is_ipv4_mapped(&self) -> bool {
1908        matches!(self.segments(), [0, 0, 0, 0, 0, 0xffff, _, _])
1909    }
1910
1911    /// Converts this address to an [`IPv4` address] if it's an [IPv4-mapped] address,
1912    /// as defined in [IETF RFC 4291 section 2.5.5.2], otherwise returns [`None`].
1913    ///
1914    /// `::ffff:a.b.c.d` becomes `a.b.c.d`.
1915    /// All addresses *not* starting with `::ffff` will return `None`.
1916    ///
1917    /// [`IPv4` address]: Ipv4Addr
1918    /// [IPv4-mapped]: Ipv6Addr
1919    /// [IETF RFC 4291 section 2.5.5.2]: https://tools.ietf.org/html/rfc4291#section-2.5.5.2
1920    ///
1921    /// # Examples
1922    ///
1923    /// ```
1924    /// use std::net::{Ipv4Addr, Ipv6Addr};
1925    ///
1926    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).to_ipv4_mapped(), None);
1927    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).to_ipv4_mapped(),
1928    ///            Some(Ipv4Addr::new(192, 10, 2, 255)));
1929    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1).to_ipv4_mapped(), None);
1930    /// ```
1931    #[inline]
1932    #[must_use = "this returns the result of the operation, \
1933                  without modifying the original"]
1934    #[stable(feature = "ipv6_to_ipv4_mapped", since = "1.63.0")]
1935    #[rustc_const_stable(feature = "const_ipv6_to_ipv4_mapped", since = "1.75.0")]
1936    pub const fn to_ipv4_mapped(&self) -> Option<Ipv4Addr> {
1937        match self.octets() {
1938            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xff, 0xff, a, b, c, d] => {
1939                Some(Ipv4Addr::new(a, b, c, d))
1940            }
1941            _ => None,
1942        }
1943    }
1944
1945    /// Converts this address to an [`IPv4` address] if it is either
1946    /// an [IPv4-compatible] address as defined in [IETF RFC 4291 section 2.5.5.1],
1947    /// or an [IPv4-mapped] address as defined in [IETF RFC 4291 section 2.5.5.2],
1948    /// otherwise returns [`None`].
1949    ///
1950    /// Note that this will return an [`IPv4` address] for the IPv6 loopback address `::1`. Use
1951    /// [`Ipv6Addr::to_ipv4_mapped`] to avoid this.
1952    ///
1953    /// `::a.b.c.d` and `::ffff:a.b.c.d` become `a.b.c.d`. `::1` becomes `0.0.0.1`.
1954    /// All addresses *not* starting with either all zeroes or `::ffff` will return `None`.
1955    ///
1956    /// [`IPv4` address]: Ipv4Addr
1957    /// [IPv4-compatible]: Ipv6Addr#ipv4-compatible-ipv6-addresses
1958    /// [IPv4-mapped]: Ipv6Addr#ipv4-mapped-ipv6-addresses
1959    /// [IETF RFC 4291 section 2.5.5.1]: https://tools.ietf.org/html/rfc4291#section-2.5.5.1
1960    /// [IETF RFC 4291 section 2.5.5.2]: https://tools.ietf.org/html/rfc4291#section-2.5.5.2
1961    ///
1962    /// # Examples
1963    ///
1964    /// ```
1965    /// use std::net::{Ipv4Addr, Ipv6Addr};
1966    ///
1967    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).to_ipv4(), None);
1968    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0xc00a, 0x2ff).to_ipv4(),
1969    ///            Some(Ipv4Addr::new(192, 10, 2, 255)));
1970    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0, 0, 1).to_ipv4(),
1971    ///            Some(Ipv4Addr::new(0, 0, 0, 1)));
1972    /// ```
1973    #[rustc_const_stable(feature = "const_ip_50", since = "1.50.0")]
1974    #[stable(feature = "rust1", since = "1.0.0")]
1975    #[must_use = "this returns the result of the operation, \
1976                  without modifying the original"]
1977    #[inline]
1978    pub const fn to_ipv4(&self) -> Option<Ipv4Addr> {
1979        if let [0, 0, 0, 0, 0, 0 | 0xffff, ab, cd] = self.segments() {
1980            let [a, b] = ab.to_be_bytes();
1981            let [c, d] = cd.to_be_bytes();
1982            Some(Ipv4Addr::new(a, b, c, d))
1983        } else {
1984            None
1985        }
1986    }
1987
1988    /// Converts this address to an `IpAddr::V4` if it is an IPv4-mapped address,
1989    /// otherwise returns self wrapped in an `IpAddr::V6`.
1990    ///
1991    /// # Examples
1992    ///
1993    /// ```
1994    /// use std::net::Ipv6Addr;
1995    ///
1996    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1).is_loopback(), false);
1997    /// assert_eq!(Ipv6Addr::new(0, 0, 0, 0, 0, 0xffff, 0x7f00, 0x1).to_canonical().is_loopback(), true);
1998    /// ```
1999    #[inline]
2000    #[must_use = "this returns the result of the operation, \
2001                  without modifying the original"]
2002    #[stable(feature = "ip_to_canonical", since = "1.75.0")]
2003    #[rustc_const_stable(feature = "ip_to_canonical", since = "1.75.0")]
2004    pub const fn to_canonical(&self) -> IpAddr {
2005        if let Some(mapped) = self.to_ipv4_mapped() {
2006            return IpAddr::V4(mapped);
2007        }
2008        IpAddr::V6(*self)
2009    }
2010
2011    /// Returns the sixteen eight-bit integers the IPv6 address consists of.
2012    ///
2013    /// ```
2014    /// use std::net::Ipv6Addr;
2015    ///
2016    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).octets(),
2017    ///            [0xff, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
2018    /// ```
2019    #[rustc_const_stable(feature = "const_ip_32", since = "1.32.0")]
2020    #[stable(feature = "ipv6_to_octets", since = "1.12.0")]
2021    #[must_use]
2022    #[inline]
2023    pub const fn octets(&self) -> [u8; 16] {
2024        self.octets
2025    }
2026
2027    /// Creates an `Ipv6Addr` from a sixteen element byte array.
2028    ///
2029    /// # Examples
2030    ///
2031    /// ```
2032    /// use std::net::Ipv6Addr;
2033    ///
2034    /// let addr = Ipv6Addr::from_octets([
2035    ///     0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
2036    ///     0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
2037    /// ]);
2038    /// assert_eq!(
2039    ///     Ipv6Addr::new(
2040    ///         0x1918, 0x1716, 0x1514, 0x1312,
2041    ///         0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
2042    ///     ),
2043    ///     addr
2044    /// );
2045    /// ```
2046    #[stable(feature = "ip_from", since = "1.91.0")]
2047    #[rustc_const_stable(feature = "ip_from", since = "1.91.0")]
2048    #[must_use]
2049    #[inline]
2050    pub const fn from_octets(octets: [u8; 16]) -> Ipv6Addr {
2051        Ipv6Addr { octets }
2052    }
2053
2054    /// Returns the sixteen eight-bit integers the IPv6 address consists of
2055    /// as a slice.
2056    ///
2057    /// # Examples
2058    ///
2059    /// ```
2060    /// #![feature(ip_as_octets)]
2061    ///
2062    /// use std::net::Ipv6Addr;
2063    ///
2064    /// assert_eq!(Ipv6Addr::new(0xff00, 0, 0, 0, 0, 0, 0, 0).as_octets(),
2065    ///            &[255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
2066    /// ```
2067    #[unstable(feature = "ip_as_octets", issue = "137259")]
2068    #[inline]
2069    pub const fn as_octets(&self) -> &[u8; 16] {
2070        &self.octets
2071    }
2072}
2073
2074/// Writes an Ipv6Addr, conforming to the canonical style described by
2075/// [RFC 5952](https://tools.ietf.org/html/rfc5952).
2076#[stable(feature = "rust1", since = "1.0.0")]
2077impl fmt::Display for Ipv6Addr {
2078    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2079        // If there are no alignment requirements, write the IP address directly to `f`.
2080        // Otherwise, write it to a local buffer and then use `f.pad`.
2081        if f.precision().is_none() && f.width().is_none() {
2082            let segments = self.segments();
2083
2084            if let Some(ipv4) = self.to_ipv4_mapped() {
2085                write!(f, "::ffff:{}", ipv4)
2086            } else {
2087                #[derive(Copy, Clone, Default)]
2088                struct Span {
2089                    start: usize,
2090                    len: usize,
2091                }
2092
2093                // Find the inner 0 span
2094                let zeroes = {
2095                    let mut longest = Span::default();
2096                    let mut current = Span::default();
2097
2098                    for (i, &segment) in segments.iter().enumerate() {
2099                        if segment == 0 {
2100                            if current.len == 0 {
2101                                current.start = i;
2102                            }
2103
2104                            current.len += 1;
2105
2106                            if current.len > longest.len {
2107                                longest = current;
2108                            }
2109                        } else {
2110                            current = Span::default();
2111                        }
2112                    }
2113
2114                    longest
2115                };
2116
2117                /// Writes a colon-separated part of the address.
2118                #[inline]
2119                fn fmt_subslice(f: &mut fmt::Formatter<'_>, chunk: &[u16]) -> fmt::Result {
2120                    if let Some((first, tail)) = chunk.split_first() {
2121                        write!(f, "{:x}", first)?;
2122                        for segment in tail {
2123                            f.write_char(':')?;
2124                            write!(f, "{:x}", segment)?;
2125                        }
2126                    }
2127                    Ok(())
2128                }
2129
2130                if zeroes.len > 1 {
2131                    fmt_subslice(f, &segments[..zeroes.start])?;
2132                    f.write_str("::")?;
2133                    fmt_subslice(f, &segments[zeroes.start + zeroes.len..])
2134                } else {
2135                    fmt_subslice(f, &segments)
2136                }
2137            }
2138        } else {
2139            const LONGEST_IPV6_ADDR: &str = "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff";
2140
2141            let mut buf = DisplayBuffer::<{ LONGEST_IPV6_ADDR.len() }>::new();
2142            // Buffer is long enough for the longest possible IPv6 address, so this should never fail.
2143            write!(buf, "{}", self).unwrap();
2144
2145            f.pad(buf.as_str())
2146        }
2147    }
2148}
2149
2150#[stable(feature = "rust1", since = "1.0.0")]
2151impl fmt::Debug for Ipv6Addr {
2152    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2153        fmt::Display::fmt(self, fmt)
2154    }
2155}
2156
2157#[stable(feature = "ip_cmp", since = "1.16.0")]
2158impl PartialEq<IpAddr> for Ipv6Addr {
2159    #[inline]
2160    fn eq(&self, other: &IpAddr) -> bool {
2161        match other {
2162            IpAddr::V4(_) => false,
2163            IpAddr::V6(v6) => self == v6,
2164        }
2165    }
2166}
2167
2168#[stable(feature = "ip_cmp", since = "1.16.0")]
2169impl PartialEq<Ipv6Addr> for IpAddr {
2170    #[inline]
2171    fn eq(&self, other: &Ipv6Addr) -> bool {
2172        match self {
2173            IpAddr::V4(_) => false,
2174            IpAddr::V6(v6) => v6 == other,
2175        }
2176    }
2177}
2178
2179#[stable(feature = "rust1", since = "1.0.0")]
2180impl PartialOrd for Ipv6Addr {
2181    #[inline]
2182    fn partial_cmp(&self, other: &Ipv6Addr) -> Option<Ordering> {
2183        Some(self.cmp(other))
2184    }
2185}
2186
2187#[stable(feature = "ip_cmp", since = "1.16.0")]
2188impl PartialOrd<Ipv6Addr> for IpAddr {
2189    #[inline]
2190    fn partial_cmp(&self, other: &Ipv6Addr) -> Option<Ordering> {
2191        match self {
2192            IpAddr::V4(_) => Some(Ordering::Less),
2193            IpAddr::V6(v6) => v6.partial_cmp(other),
2194        }
2195    }
2196}
2197
2198#[stable(feature = "ip_cmp", since = "1.16.0")]
2199impl PartialOrd<IpAddr> for Ipv6Addr {
2200    #[inline]
2201    fn partial_cmp(&self, other: &IpAddr) -> Option<Ordering> {
2202        match other {
2203            IpAddr::V4(_) => Some(Ordering::Greater),
2204            IpAddr::V6(v6) => self.partial_cmp(v6),
2205        }
2206    }
2207}
2208
2209#[stable(feature = "rust1", since = "1.0.0")]
2210impl Ord for Ipv6Addr {
2211    #[inline]
2212    fn cmp(&self, other: &Ipv6Addr) -> Ordering {
2213        self.segments().cmp(&other.segments())
2214    }
2215}
2216
2217#[stable(feature = "i128", since = "1.26.0")]
2218#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2219impl const From<Ipv6Addr> for u128 {
2220    /// Uses [`Ipv6Addr::to_bits`] to convert an IPv6 address to a host byte order `u128`.
2221    #[inline]
2222    fn from(ip: Ipv6Addr) -> u128 {
2223        ip.to_bits()
2224    }
2225}
2226#[stable(feature = "i128", since = "1.26.0")]
2227#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2228impl const From<u128> for Ipv6Addr {
2229    /// Uses [`Ipv6Addr::from_bits`] to convert a host byte order `u128` to an IPv6 address.
2230    #[inline]
2231    fn from(ip: u128) -> Ipv6Addr {
2232        Ipv6Addr::from_bits(ip)
2233    }
2234}
2235
2236#[stable(feature = "ipv6_from_octets", since = "1.9.0")]
2237#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2238impl const From<[u8; 16]> for Ipv6Addr {
2239    /// Creates an `Ipv6Addr` from a sixteen element byte array.
2240    ///
2241    /// # Examples
2242    ///
2243    /// ```
2244    /// use std::net::Ipv6Addr;
2245    ///
2246    /// let addr = Ipv6Addr::from([
2247    ///     0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
2248    ///     0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
2249    /// ]);
2250    /// assert_eq!(
2251    ///     Ipv6Addr::new(
2252    ///         0x1918, 0x1716, 0x1514, 0x1312,
2253    ///         0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
2254    ///     ),
2255    ///     addr
2256    /// );
2257    /// ```
2258    #[inline]
2259    fn from(octets: [u8; 16]) -> Ipv6Addr {
2260        Ipv6Addr { octets }
2261    }
2262}
2263
2264#[stable(feature = "ipv6_from_segments", since = "1.16.0")]
2265#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2266impl const From<[u16; 8]> for Ipv6Addr {
2267    /// Creates an `Ipv6Addr` from an eight element 16-bit array.
2268    ///
2269    /// # Examples
2270    ///
2271    /// ```
2272    /// use std::net::Ipv6Addr;
2273    ///
2274    /// let addr = Ipv6Addr::from([
2275    ///     0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
2276    ///     0x209u16, 0x208u16, 0x207u16, 0x206u16,
2277    /// ]);
2278    /// assert_eq!(
2279    ///     Ipv6Addr::new(
2280    ///         0x20d, 0x20c, 0x20b, 0x20a,
2281    ///         0x209, 0x208, 0x207, 0x206,
2282    ///     ),
2283    ///     addr
2284    /// );
2285    /// ```
2286    #[inline]
2287    fn from(segments: [u16; 8]) -> Ipv6Addr {
2288        let [a, b, c, d, e, f, g, h] = segments;
2289        Ipv6Addr::new(a, b, c, d, e, f, g, h)
2290    }
2291}
2292
2293#[stable(feature = "ip_from_slice", since = "1.17.0")]
2294#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2295impl const From<[u8; 16]> for IpAddr {
2296    /// Creates an `IpAddr::V6` from a sixteen element byte array.
2297    ///
2298    /// # Examples
2299    ///
2300    /// ```
2301    /// use std::net::{IpAddr, Ipv6Addr};
2302    ///
2303    /// let addr = IpAddr::from([
2304    ///     0x19u8, 0x18u8, 0x17u8, 0x16u8, 0x15u8, 0x14u8, 0x13u8, 0x12u8,
2305    ///     0x11u8, 0x10u8, 0x0fu8, 0x0eu8, 0x0du8, 0x0cu8, 0x0bu8, 0x0au8,
2306    /// ]);
2307    /// assert_eq!(
2308    ///     IpAddr::V6(Ipv6Addr::new(
2309    ///         0x1918, 0x1716, 0x1514, 0x1312,
2310    ///         0x1110, 0x0f0e, 0x0d0c, 0x0b0a,
2311    ///     )),
2312    ///     addr
2313    /// );
2314    /// ```
2315    #[inline]
2316    fn from(octets: [u8; 16]) -> IpAddr {
2317        IpAddr::V6(Ipv6Addr::from(octets))
2318    }
2319}
2320
2321#[stable(feature = "ip_from_slice", since = "1.17.0")]
2322#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2323impl const From<[u16; 8]> for IpAddr {
2324    /// Creates an `IpAddr::V6` from an eight element 16-bit array.
2325    ///
2326    /// # Examples
2327    ///
2328    /// ```
2329    /// use std::net::{IpAddr, Ipv6Addr};
2330    ///
2331    /// let addr = IpAddr::from([
2332    ///     0x20du16, 0x20cu16, 0x20bu16, 0x20au16,
2333    ///     0x209u16, 0x208u16, 0x207u16, 0x206u16,
2334    /// ]);
2335    /// assert_eq!(
2336    ///     IpAddr::V6(Ipv6Addr::new(
2337    ///         0x20d, 0x20c, 0x20b, 0x20a,
2338    ///         0x209, 0x208, 0x207, 0x206,
2339    ///     )),
2340    ///     addr
2341    /// );
2342    /// ```
2343    #[inline]
2344    fn from(segments: [u16; 8]) -> IpAddr {
2345        IpAddr::V6(Ipv6Addr::from(segments))
2346    }
2347}
2348
2349#[stable(feature = "ip_bitops", since = "1.75.0")]
2350#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2351impl const Not for Ipv4Addr {
2352    type Output = Ipv4Addr;
2353
2354    #[inline]
2355    fn not(mut self) -> Ipv4Addr {
2356        let mut idx = 0;
2357        while idx < 4 {
2358            self.octets[idx] = !self.octets[idx];
2359            idx += 1;
2360        }
2361        self
2362    }
2363}
2364
2365#[stable(feature = "ip_bitops", since = "1.75.0")]
2366#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2367impl const Not for &'_ Ipv4Addr {
2368    type Output = Ipv4Addr;
2369
2370    #[inline]
2371    fn not(self) -> Ipv4Addr {
2372        !*self
2373    }
2374}
2375
2376#[stable(feature = "ip_bitops", since = "1.75.0")]
2377#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2378impl const Not for Ipv6Addr {
2379    type Output = Ipv6Addr;
2380
2381    #[inline]
2382    fn not(mut self) -> Ipv6Addr {
2383        let mut idx = 0;
2384        while idx < 16 {
2385            self.octets[idx] = !self.octets[idx];
2386            idx += 1;
2387        }
2388        self
2389    }
2390}
2391
2392#[stable(feature = "ip_bitops", since = "1.75.0")]
2393#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2394impl const Not for &'_ Ipv6Addr {
2395    type Output = Ipv6Addr;
2396
2397    #[inline]
2398    fn not(self) -> Ipv6Addr {
2399        !*self
2400    }
2401}
2402
2403macro_rules! bitop_impls {
2404    ($(
2405        $(#[$attr:meta])*
2406        impl ($BitOp:ident, $BitOpAssign:ident) for $ty:ty = ($bitop:ident, $bitop_assign:ident);
2407    )*) => {
2408        $(
2409            $(#[$attr])*
2410            impl const $BitOpAssign for $ty {
2411                fn $bitop_assign(&mut self, rhs: $ty) {
2412                    let mut idx = 0;
2413                    while idx < self.octets.len() {
2414                        self.octets[idx].$bitop_assign(rhs.octets[idx]);
2415                        idx += 1;
2416                    }
2417                }
2418            }
2419
2420            $(#[$attr])*
2421            impl const $BitOpAssign<&'_ $ty> for $ty {
2422                fn $bitop_assign(&mut self, rhs: &'_ $ty) {
2423                    self.$bitop_assign(*rhs);
2424                }
2425            }
2426
2427            $(#[$attr])*
2428            impl const $BitOp for $ty {
2429                type Output = $ty;
2430
2431                #[inline]
2432                fn $bitop(mut self, rhs: $ty) -> $ty {
2433                    self.$bitop_assign(rhs);
2434                    self
2435                }
2436            }
2437
2438            $(#[$attr])*
2439            impl const $BitOp<&'_ $ty> for $ty {
2440                type Output = $ty;
2441
2442                #[inline]
2443                fn $bitop(mut self, rhs: &'_ $ty) -> $ty {
2444                    self.$bitop_assign(*rhs);
2445                    self
2446                }
2447            }
2448
2449            $(#[$attr])*
2450            impl const $BitOp<$ty> for &'_ $ty {
2451                type Output = $ty;
2452
2453                #[inline]
2454                fn $bitop(self, rhs: $ty) -> $ty {
2455                    let mut lhs = *self;
2456                    lhs.$bitop_assign(rhs);
2457                    lhs
2458                }
2459            }
2460
2461            $(#[$attr])*
2462            impl const $BitOp<&'_ $ty> for &'_ $ty {
2463                type Output = $ty;
2464
2465                #[inline]
2466                fn $bitop(self, rhs: &'_ $ty) -> $ty {
2467                    let mut lhs = *self;
2468                    lhs.$bitop_assign(*rhs);
2469                    lhs
2470                }
2471            }
2472        )*
2473    };
2474}
2475
2476bitop_impls! {
2477    #[stable(feature = "ip_bitops", since = "1.75.0")]
2478    #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2479    impl (BitAnd, BitAndAssign) for Ipv4Addr = (bitand, bitand_assign);
2480    #[stable(feature = "ip_bitops", since = "1.75.0")]
2481    #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2482    impl (BitOr, BitOrAssign) for Ipv4Addr = (bitor, bitor_assign);
2483
2484    #[stable(feature = "ip_bitops", since = "1.75.0")]
2485    #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2486    impl (BitAnd, BitAndAssign) for Ipv6Addr = (bitand, bitand_assign);
2487    #[stable(feature = "ip_bitops", since = "1.75.0")]
2488    #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
2489    impl (BitOr, BitOrAssign) for Ipv6Addr = (bitor, bitor_assign);
2490}
````