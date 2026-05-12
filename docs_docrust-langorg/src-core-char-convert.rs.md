---
title: convert.rs - source
url: https://doc.rust-lang.org/src/core/char/convert.rs.html#40
source: crawler
fetched_at: 2026-05-06T21:29:17.888195536-03:00
rendered_js: false
word_count: 1493
summary: This document defines conversion traits and utility functions for transforming Rust characters (char) to and from various numeric integer types.
tags:
    - rust
    - unicode
    - type-conversion
    - char
    - primitive-types
category: reference
---

## core/char/ convert.rs

````rust
1//! Character conversions.
2
3use crate::char::TryFromCharError;
4use crate::error::Error;
5use crate::fmt;
6use crate::mem::transmute;
7use crate::str::FromStr;
8use crate::ub_checks::assert_unsafe_precondition;
9
10/// Converts a `u32` to a `char`. See [`char::from_u32`].
11#[must_use]
12#[inline]
13pub(super) const fn from_u32(i: u32) -> Option<char> {
14    // FIXME(const-hack): once Result::ok is const fn, use it here
15    match char_try_from_u32(i) {
16        Ok(c) => Some(c),
17        Err(_) => None,
18    }
19}
20
21/// Converts a `u32` to a `char`, ignoring validity. See [`char::from_u32_unchecked`].
22#[inline]
23#[must_use]
24#[allow(unnecessary_transmutes)]
25#[track_caller]
26pub(super) const unsafe fn from_u32_unchecked(i: u32) -> char {
27    // SAFETY: the caller must guarantee that `i` is a valid char value.
28    unsafe {
29        assert_unsafe_precondition!(
30            check_language_ub,
31            "invalid value for `char`",
32            (i: u32 = i) => char_try_from_u32(i).is_ok()
33        );
34        transmute(i)
35    }
36}
37
38#[stable(feature = "char_convert", since = "1.13.0")]
39#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
40impl const From<char> for u32 {
41    /// Converts a [`char`] into a [`u32`].
42    ///
43    /// # Examples
44    ///
45    /// ```
46    /// let c = 'c';
47    /// let u = u32::from(c);
48    ///
49    /// assert!(4 == size_of_val(&u))
50    /// ```
51    #[inline]
52    fn from(c: char) -> Self {
53        c as u32
54    }
55}
56
57#[stable(feature = "more_char_conversions", since = "1.51.0")]
58#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
59impl const From<char> for u64 {
60    /// Converts a [`char`] into a [`u64`].
61    ///
62    /// # Examples
63    ///
64    /// ```
65    /// let c = '👤';
66    /// let u = u64::from(c);
67    ///
68    /// assert!(8 == size_of_val(&u))
69    /// ```
70    #[inline]
71    fn from(c: char) -> Self {
72        // The char is casted to the value of the code point, then zero-extended to 64 bit.
73        // See [https://doc.rust-lang.org/reference/expressions/operator-expr.html#semantics]
74        c as u64
75    }
76}
77
78#[stable(feature = "more_char_conversions", since = "1.51.0")]
79#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
80impl const From<char> for u128 {
81    /// Converts a [`char`] into a [`u128`].
82    ///
83    /// # Examples
84    ///
85    /// ```
86    /// let c = '⚙';
87    /// let u = u128::from(c);
88    ///
89    /// assert!(16 == size_of_val(&u))
90    /// ```
91    #[inline]
92    fn from(c: char) -> Self {
93        // The char is casted to the value of the code point, then zero-extended to 128 bit.
94        // See [https://doc.rust-lang.org/reference/expressions/operator-expr.html#semantics]
95        c as u128
96    }
97}
98
99/// Maps a `char` with a code point from U+0000 to U+00FF (inclusive) to a byte in `0x00..=0xFF` with
100/// the same value, failing if the code point is greater than U+00FF.
101///
102/// See [`impl From<u8> for char`](char#impl-From<u8>-for-char) for details on the encoding.
103#[stable(feature = "u8_from_char", since = "1.59.0")]
104#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
105impl const TryFrom<char> for u8 {
106    type Error = TryFromCharError;
107
108    /// Tries to convert a [`char`] into a [`u8`].
109    ///
110    /// # Examples
111    ///
112    /// ```
113    /// let a = 'ÿ'; // U+00FF
114    /// let b = 'Ā'; // U+0100
115    ///
116    /// assert_eq!(u8::try_from(a), Ok(0xFF_u8));
117    /// assert!(u8::try_from(b).is_err());
118    /// ```
119    #[inline]
120    fn try_from(c: char) -> Result<u8, Self::Error> {
121        // FIXME(const-hack): this should use map_err instead
122        match u8::try_from(u32::from(c)) {
123            Ok(b) => Ok(b),
124            Err(_) => Err(TryFromCharError(())),
125        }
126    }
127}
128
129/// Maps a `char` with a code point from U+0000 to U+FFFF (inclusive) to a `u16` in `0x0000..=0xFFFF`
130/// with the same value, failing if the code point is greater than U+FFFF.
131///
132/// This corresponds to the UCS-2 encoding, as specified in ISO/IEC 10646:2003.
133#[stable(feature = "u16_from_char", since = "1.74.0")]
134#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
135impl const TryFrom<char> for u16 {
136    type Error = TryFromCharError;
137
138    /// Tries to convert a [`char`] into a [`u16`].
139    ///
140    /// # Examples
141    ///
142    /// ```
143    /// let trans_rights = '⚧'; // U+26A7
144    /// let ninjas = '🥷'; // U+1F977
145    ///
146    /// assert_eq!(u16::try_from(trans_rights), Ok(0x26A7_u16));
147    /// assert!(u16::try_from(ninjas).is_err());
148    /// ```
149    #[inline]
150    fn try_from(c: char) -> Result<u16, Self::Error> {
151        // FIXME(const-hack): this should use map_err instead
152        match u16::try_from(u32::from(c)) {
153            Ok(x) => Ok(x),
154            Err(_) => Err(TryFromCharError(())),
155        }
156    }
157}
158
159/// Maps a `char` with a code point from U+0000 to U+10FFFF (inclusive) to a `usize` in
160/// `0x0000..=0x10FFFF` with the same value, failing if the final value is unrepresentable by
161/// `usize`.
162///
163/// Generally speaking, this conversion can be seen as obtaining the character's corresponding
164/// UTF-32 code point to the extent representable by pointer addresses.
165#[stable(feature = "usize_try_from_char", since = "1.94.0")]
166#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
167impl const TryFrom<char> for usize {
168    type Error = TryFromCharError;
169
170    /// Tries to convert a [`char`] into a [`usize`].
171    ///
172    /// # Examples
173    ///
174    /// ```
175    /// let a = '\u{FFFF}'; // Always succeeds.
176    /// let b = '\u{10FFFF}'; // Conditionally succeeds.
177    ///
178    /// assert_eq!(usize::try_from(a), Ok(0xFFFF));
179    ///
180    /// if size_of::<usize>() >= size_of::<u32>() {
181    ///     assert_eq!(usize::try_from(b), Ok(0x10FFFF));
182    /// } else {
183    ///     assert!(matches!(usize::try_from(b), Err(_)));
184    /// }
185    /// ```
186    #[inline]
187    fn try_from(c: char) -> Result<usize, Self::Error> {
188        // FIXME(const-hack): this should use map_err instead
189        match usize::try_from(u32::from(c)) {
190            Ok(x) => Ok(x),
191            Err(_) => Err(TryFromCharError(())),
192        }
193    }
194}
195
196/// Maps a byte in `0x00..=0xFF` to a `char` whose code point has the same value from U+0000 to U+00FF
197/// (inclusive).
198///
199/// Unicode is designed such that this effectively decodes bytes
200/// with the character encoding that IANA calls ISO-8859-1.
201/// This encoding is compatible with ASCII.
202///
203/// Note that this is different from ISO/IEC 8859-1 a.k.a. ISO 8859-1 (with one less hyphen),
204/// which leaves some "blanks", byte values that are not assigned to any character.
205/// ISO-8859-1 (the IANA one) assigns them to the C0 and C1 control codes.
206///
207/// Note that this is *also* different from Windows-1252 a.k.a. code page 1252,
208/// which is a superset ISO/IEC 8859-1 that assigns some (not all!) blanks
209/// to punctuation and various Latin characters.
210///
211/// To confuse things further, [on the Web](https://encoding.spec.whatwg.org/)
212/// `ascii`, `iso-8859-1`, and `windows-1252` are all aliases
213/// for a superset of Windows-1252 that fills the remaining blanks with corresponding
214/// C0 and C1 control codes.
215#[stable(feature = "char_convert", since = "1.13.0")]
216#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
217impl const From<u8> for char {
218    /// Converts a [`u8`] into a [`char`].
219    ///
220    /// # Examples
221    ///
222    /// ```
223    /// let u = 32 as u8;
224    /// let c = char::from(u);
225    ///
226    /// assert!(4 == size_of_val(&c))
227    /// ```
228    #[inline]
229    fn from(i: u8) -> Self {
230        i as char
231    }
232}
233
234/// An error which can be returned when parsing a char.
235///
236/// This `struct` is created when using the [`char::from_str`] method.
237#[stable(feature = "char_from_str", since = "1.20.0")]
238#[derive(Clone, Debug, PartialEq, Eq)]
239pub struct ParseCharError {
240    kind: CharErrorKind,
241}
242
243#[derive(Copy, Clone, Debug, PartialEq, Eq)]
244enum CharErrorKind {
245    EmptyString,
246    TooManyChars,
247}
248
249#[stable(feature = "char_from_str", since = "1.20.0")]
250impl Error for ParseCharError {}
251
252#[stable(feature = "char_from_str", since = "1.20.0")]
253impl fmt::Display for ParseCharError {
254    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
255        match self.kind {
256            CharErrorKind::EmptyString => "cannot parse char from empty string",
257            CharErrorKind::TooManyChars => "too many characters in string",
258        }
259        .fmt(f)
260    }
261}
262
263#[stable(feature = "char_from_str", since = "1.20.0")]
264impl FromStr for char {
265    type Err = ParseCharError;
266
267    #[inline]
268    fn from_str(s: &str) -> Result<Self, Self::Err> {
269        let mut chars = s.chars();
270        match (chars.next(), chars.next()) {
271            (None, _) => Err(ParseCharError { kind: CharErrorKind::EmptyString }),
272            (Some(c), None) => Ok(c),
273            _ => Err(ParseCharError { kind: CharErrorKind::TooManyChars }),
274        }
275    }
276}
277
278#[inline]
279#[allow(unnecessary_transmutes)]
280const fn char_try_from_u32(i: u32) -> Result<char, CharTryFromError> {
281    // This is an optimized version of the check
282    // (i > MAX as u32) || (i >= 0xD800 && i <= 0xDFFF),
283    // which can also be written as
284    // i >= 0x110000 || (i >= 0xD800 && i < 0xE000).
285    //
286    // The XOR with 0xD800 permutes the ranges such that 0xD800..0xE000 is
287    // mapped to 0x0000..0x0800, while keeping all the high bits outside 0xFFFF the same.
288    // In particular, numbers >= 0x110000 stay in this range.
289    //
290    // Subtracting 0x800 causes 0x0000..0x0800 to wrap, meaning that a single
291    // unsigned comparison against 0x110000 - 0x800 will detect both the wrapped
292    // surrogate range as well as the numbers originally larger than 0x110000.
293    if (i ^ 0xD800).wrapping_sub(0x800) >= 0x110000 - 0x800 {
294        Err(CharTryFromError(()))
295    } else {
296        // SAFETY: checked that it's a legal unicode value
297        Ok(unsafe { transmute(i) })
298    }
299}
300
301#[stable(feature = "try_from", since = "1.34.0")]
302#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
303impl const TryFrom<u32> for char {
304    type Error = CharTryFromError;
305
306    #[inline]
307    fn try_from(i: u32) -> Result<Self, Self::Error> {
308        char_try_from_u32(i)
309    }
310}
311
312/// The error type returned when a conversion from [`prim@u32`] to [`prim@char`] fails.
313///
314/// This `struct` is created by the [`char::try_from<u32>`](char#impl-TryFrom<u32>-for-char) method.
315/// See its documentation for more.
316#[stable(feature = "try_from", since = "1.34.0")]
317#[derive(Copy, Clone, Debug, PartialEq, Eq)]
318pub struct CharTryFromError(());
319
320#[stable(feature = "try_from", since = "1.34.0")]
321impl fmt::Display for CharTryFromError {
322    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
323        "converted integer out of range for `char`".fmt(f)
324    }
325}
326
327/// Converts a digit in the given radix to a `char`. See [`char::from_digit`].
328#[inline]
329#[must_use]
330pub(super) const fn from_digit(num: u32, radix: u32) -> Option<char> {
331    if radix > 36 {
332        panic!("from_digit: radix is too high (maximum 36)");
333    }
334    if num < radix {
335        let num = num as u8;
336        if num < 10 { Some((b'0' + num) as char) } else { Some((b'a' + num - 10) as char) }
337    } else {
338        None
339    }
340}
````