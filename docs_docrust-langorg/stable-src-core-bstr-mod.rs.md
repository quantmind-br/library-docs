---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/core/bstr/mod.rs.html#358
source: crawler
fetched_at: 2026-05-06T21:34:46.25627107-03:00
rendered_js: false
word_count: 1603
summary: This document defines the ByteStr type in Rust, which serves as a wrapper for byte slices to handle data that is not guaranteed to be valid UTF-8.
tags:
    - rust
    - bytestr
    - data-types
    - utf-8-handling
    - memory-safety
category: reference
---

## core/bstr/ mod.rs

````rust
1//! The `ByteStr` type and trait implementations.
2
3mod traits;
4
5#[unstable(feature = "bstr_internals", issue = "none")]
6pub use traits::{impl_partial_eq, impl_partial_eq_n, impl_partial_eq_ord};
7
8use crate::borrow::{Borrow, BorrowMut};
9use crate::fmt;
10use crate::ops::{Deref, DerefMut, DerefPure};
11
12/// A wrapper for `&[u8]` representing a human-readable string that's conventionally, but not
13/// always, UTF-8.
14///
15/// Unlike `&str`, this type permits non-UTF-8 contents, making it suitable for user input,
16/// non-native filenames (as `Path` only supports native filenames), and other applications that
17/// need to round-trip whatever data the user provides.
18///
19/// For an owned, growable byte string buffer, use
20/// [`ByteString`](../../std/bstr/struct.ByteString.html).
21///
22/// `ByteStr` implements `Deref` to `[u8]`, so all methods available on `[u8]` are available on
23/// `ByteStr`.
24///
25/// # Representation
26///
27/// A `&ByteStr` has the same representation as a `&str`. That is, a `&ByteStr` is a wide pointer
28/// which includes a pointer to some bytes and a length.
29///
30/// # Trait implementations
31///
32/// The `ByteStr` type has a number of trait implementations, and in particular, defines equality
33/// and comparisons between `&ByteStr`, `&str`, and `&[u8]`, for convenience.
34///
35/// The `Debug` implementation for `ByteStr` shows its bytes as a normal string, with invalid UTF-8
36/// presented as hex escape sequences.
37///
38/// The `Display` implementation behaves as if the `ByteStr` were first lossily converted to a
39/// `str`, with invalid UTF-8 presented as the Unicode replacement character (�).
40#[unstable(feature = "bstr", issue = "134915")]
41#[repr(transparent)]
42#[doc(alias = "BStr")]
43pub struct ByteStr(pub [u8]);
44
45impl ByteStr {
46    /// Creates a `ByteStr` slice from anything that can be converted to a byte slice.
47    ///
48    /// This is a zero-cost conversion.
49    ///
50    /// # Example
51    ///
52    /// You can create a `ByteStr` from a byte array, a byte slice or a string slice:
53    ///
54    /// ```
55    /// # #![feature(bstr)]
56    /// # use std::bstr::ByteStr;
57    /// let a = ByteStr::new(b"abc");
58    /// let b = ByteStr::new(&b"abc"[..]);
59    /// let c = ByteStr::new("abc");
60    ///
61    /// assert_eq!(a, b);
62    /// assert_eq!(a, c);
63    /// ```
64    #[inline]
65    #[unstable(feature = "bstr", issue = "134915")]
66    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
67    pub const fn new<B: ?Sized + [const] AsRef<[u8]>>(bytes: &B) -> &Self {
68        ByteStr::from_bytes(bytes.as_ref())
69    }
70
71    /// Returns the same string as `&ByteStr`.
72    ///
73    /// This method is redundant when used directly on `&ByteStr`, but
74    /// it helps dereferencing other "container" types,
75    /// for example `Box<ByteStr>` or `Arc<ByteStr>`.
76    #[inline]
77    // #[unstable(feature = "str_as_str", issue = "130366")]
78    #[unstable(feature = "bstr", issue = "134915")]
79    pub const fn as_byte_str(&self) -> &ByteStr {
80        self
81    }
82
83    /// Returns the same string as `&mut ByteStr`.
84    ///
85    /// This method is redundant when used directly on `&mut ByteStr`, but
86    /// it helps dereferencing other "container" types,
87    /// for example `Box<ByteStr>` or `MutexGuard<ByteStr>`.
88    #[inline]
89    // #[unstable(feature = "str_as_str", issue = "130366")]
90    #[unstable(feature = "bstr", issue = "134915")]
91    pub const fn as_mut_byte_str(&mut self) -> &mut ByteStr {
92        self
93    }
94
95    #[doc(hidden)]
96    #[unstable(feature = "bstr_internals", issue = "none")]
97    #[inline]
98    #[rustc_const_unstable(feature = "bstr_internals", issue = "none")]
99    pub const fn from_bytes(slice: &[u8]) -> &Self {
100        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`, so we can turn a reference to
101        // the wrapped type into a reference to the wrapper type.
102        unsafe { &*(slice as *const [u8] as *const Self) }
103    }
104
105    #[doc(hidden)]
106    #[unstable(feature = "bstr_internals", issue = "none")]
107    #[inline]
108    #[rustc_const_unstable(feature = "bstr_internals", issue = "none")]
109    pub const fn from_bytes_mut(slice: &mut [u8]) -> &mut Self {
110        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`, so we can turn a reference to
111        // the wrapped type into a reference to the wrapper type.
112        unsafe { &mut *(slice as *mut [u8] as *mut Self) }
113    }
114
115    #[doc(hidden)]
116    #[unstable(feature = "bstr_internals", issue = "none")]
117    #[inline]
118    #[rustc_const_unstable(feature = "bstr_internals", issue = "none")]
119    pub const fn as_bytes(&self) -> &[u8] {
120        &self.0
121    }
122
123    #[doc(hidden)]
124    #[unstable(feature = "bstr_internals", issue = "none")]
125    #[inline]
126    #[rustc_const_unstable(feature = "bstr_internals", issue = "none")]
127    pub const fn as_bytes_mut(&mut self) -> &mut [u8] {
128        &mut self.0
129    }
130}
131
132#[unstable(feature = "bstr", issue = "134915")]
133#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
134impl const Deref for ByteStr {
135    type Target = [u8];
136
137    #[inline]
138    fn deref(&self) -> &[u8] {
139        &self.0
140    }
141}
142
143#[unstable(feature = "bstr", issue = "134915")]
144#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
145impl const DerefMut for ByteStr {
146    #[inline]
147    fn deref_mut(&mut self) -> &mut [u8] {
148        &mut self.0
149    }
150}
151
152#[unstable(feature = "deref_pure_trait", issue = "87121")]
153unsafe impl DerefPure for ByteStr {}
154
155#[unstable(feature = "bstr", issue = "134915")]
156impl fmt::Debug for ByteStr {
157    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
158        write!(f, "\"")?;
159        for chunk in self.utf8_chunks() {
160            for c in chunk.valid().chars() {
161                match c {
162                    '\0' => write!(f, "\\0")?,
163                    '\x01'..='\x7f' => write!(f, "{}", (c as u8).escape_ascii())?,
164                    _ => write!(f, "{}", c.escape_debug())?,
165                }
166            }
167            write!(f, "{}", chunk.invalid().escape_ascii())?;
168        }
169        write!(f, "\"")?;
170        Ok(())
171    }
172}
173
174#[unstable(feature = "bstr", issue = "134915")]
175impl fmt::Display for ByteStr {
176    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
177        let nchars: usize = self
178            .utf8_chunks()
179            .map(|chunk| {
180                chunk.valid().chars().count() + if chunk.invalid().is_empty() { 0 } else { 1 }
181            })
182            .sum();
183
184        let padding = f.width().unwrap_or(0).saturating_sub(nchars);
185        let fill = f.fill();
186
187        let (lpad, rpad) = match f.align() {
188            Some(fmt::Alignment::Right) => (padding, 0),
189            Some(fmt::Alignment::Center) => {
190                let half = padding / 2;
191                (half, half + padding % 2)
192            }
193            // Either alignment is not specified or it's left aligned
194            // which behaves the same with padding
195            _ => (0, padding),
196        };
197
198        for _ in 0..lpad {
199            write!(f, "{fill}")?;
200        }
201
202        for chunk in self.utf8_chunks() {
203            f.write_str(chunk.valid())?;
204            if !chunk.invalid().is_empty() {
205                f.write_str("\u{FFFD}")?;
206            }
207        }
208
209        for _ in 0..rpad {
210            write!(f, "{fill}")?;
211        }
212
213        Ok(())
214    }
215}
216
217#[unstable(feature = "bstr", issue = "134915")]
218#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
219impl const AsRef<[u8]> for ByteStr {
220    #[inline]
221    fn as_ref(&self) -> &[u8] {
222        &self.0
223    }
224}
225
226#[unstable(feature = "bstr", issue = "134915")]
227#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
228impl const AsRef<ByteStr> for ByteStr {
229    #[inline]
230    fn as_ref(&self) -> &ByteStr {
231        self
232    }
233}
234
235// `impl AsRef<ByteStr> for [u8]` omitted to avoid widespread inference failures
236
237#[unstable(feature = "bstr", issue = "134915")]
238#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
239impl const AsRef<ByteStr> for str {
240    #[inline]
241    fn as_ref(&self) -> &ByteStr {
242        ByteStr::new(self)
243    }
244}
245
246#[unstable(feature = "bstr", issue = "134915")]
247#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
248impl const AsMut<[u8]> for ByteStr {
249    #[inline]
250    fn as_mut(&mut self) -> &mut [u8] {
251        &mut self.0
252    }
253}
254
255// `impl AsMut<ByteStr> for [u8]` omitted to avoid widespread inference failures
256
257// `impl Borrow<ByteStr> for [u8]` omitted to avoid widespread inference failures
258
259// `impl Borrow<ByteStr> for str` omitted to avoid widespread inference failures
260
261#[unstable(feature = "bstr", issue = "134915")]
262#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
263impl const Borrow<[u8]> for ByteStr {
264    #[inline]
265    fn borrow(&self) -> &[u8] {
266        &self.0
267    }
268}
269
270// `impl BorrowMut<ByteStr> for [u8]` omitted to avoid widespread inference failures
271
272#[unstable(feature = "bstr", issue = "134915")]
273#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
274impl const BorrowMut<[u8]> for ByteStr {
275    #[inline]
276    fn borrow_mut(&mut self) -> &mut [u8] {
277        &mut self.0
278    }
279}
280
281#[unstable(feature = "bstr", issue = "134915")]
282impl<'a> Default for &'a ByteStr {
283    fn default() -> Self {
284        ByteStr::from_bytes(b"")
285    }
286}
287
288#[unstable(feature = "bstr", issue = "134915")]
289impl<'a> Default for &'a mut ByteStr {
290    fn default() -> Self {
291        ByteStr::from_bytes_mut(&mut [])
292    }
293}
294
295// Omitted due to inference failures
296//
297// #[unstable(feature = "bstr", issue = "134915")]
298// impl<'a, const N: usize> From<&'a [u8; N]> for &'a ByteStr {
299//     #[inline]
300//     fn from(s: &'a [u8; N]) -> Self {
301//         ByteStr::from_bytes(s)
302//     }
303// }
304//
305// #[unstable(feature = "bstr", issue = "134915")]
306// impl<'a> From<&'a [u8]> for &'a ByteStr {
307//     #[inline]
308//     fn from(s: &'a [u8]) -> Self {
309//         ByteStr::from_bytes(s)
310//     }
311// }
312
313// Omitted due to slice-from-array-issue-113238:
314//
315// #[unstable(feature = "bstr", issue = "134915")]
316// impl<'a> From<&'a ByteStr> for &'a [u8] {
317//     #[inline]
318//     fn from(s: &'a ByteStr) -> Self {
319//         &s.0
320//     }
321// }
322//
323// #[unstable(feature = "bstr", issue = "134915")]
324// impl<'a> From<&'a mut ByteStr> for &'a mut [u8] {
325//     #[inline]
326//     fn from(s: &'a mut ByteStr) -> Self {
327//         &mut s.0
328//     }
329// }
330
331// Omitted due to inference failures
332//
333// #[unstable(feature = "bstr", issue = "134915")]
334// impl<'a> From<&'a str> for &'a ByteStr {
335//     #[inline]
336//     fn from(s: &'a str) -> Self {
337//         ByteStr::from_bytes(s.as_bytes())
338//     }
339// }
340
341#[unstable(feature = "bstr", issue = "134915")]
342#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
343impl<'a> const TryFrom<&'a ByteStr> for &'a str {
344    type Error = crate::str::Utf8Error;
345
346    #[inline]
347    fn try_from(s: &'a ByteStr) -> Result<Self, Self::Error> {
348        crate::str::from_utf8(&s.0)
349    }
350}
351
352#[unstable(feature = "bstr", issue = "134915")]
353#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
354impl<'a> const TryFrom<&'a mut ByteStr> for &'a mut str {
355    type Error = crate::str::Utf8Error;
356
357    #[inline]
358    fn try_from(s: &'a mut ByteStr) -> Result<Self, Self::Error> {
359        crate::str::from_utf8_mut(&mut s.0)
360    }
361}
````