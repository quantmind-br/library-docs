---
title: num.rs - source
url: https://doc.rust-lang.org/src/core/fmt/num.rs.html#74
source: crawler
fetched_at: 2026-05-06T21:36:44.565442624-03:00
rendered_js: false
word_count: 4833
summary: This document defines the internal implementation for formatting numeric types in Rust, utilizing macros and lookup tables for efficient conversion between integers and their string representations across different radices.
tags:
    - rust
    - formatting
    - numeric-types
    - macros
    - radix
    - internal-api
category: concept
---

## core/fmt/ num.rs

````rust
1//! Integer and floating-point number formatting
2
3use crate::fmt::NumBuffer;
4use crate::mem::MaybeUninit;
5use crate::num::fmt as numfmt;
6use crate::{fmt, str};
7
8/// Formatting of integers with a non-decimal radix.
9macro_rules! radix_integer {
10    (fmt::$Trait:ident for $Signed:ident and $Unsigned:ident, $prefix:literal, $dig_tab:literal) => {
11        #[stable(feature = "rust1", since = "1.0.0")]
12        impl fmt::$Trait for $Unsigned {
13            /// Format unsigned integers in the radix.
14            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
15                // Check macro arguments at compile time.
16                const {
17                    assert!($Unsigned::MIN == 0, "need unsigned");
18                    assert!($dig_tab.is_ascii(), "need single-byte entries");
19                }
20
21                // ASCII digits in ascending order are used as a lookup table.
22                const DIG_TAB: &[u8] = $dig_tab;
23                const BASE: $Unsigned = DIG_TAB.len() as $Unsigned;
24                const MAX_DIG_N: usize = $Unsigned::MAX.ilog(BASE) as usize + 1;
25
26                // Buffer digits of self with right alignment.
27                let mut buf = [MaybeUninit::<u8>::uninit(); MAX_DIG_N];
28                // Count the number of bytes in buf that are not initialized.
29                let mut offset = buf.len();
30
31                // Accumulate each digit of the number from the least
32                // significant to the most significant figure.
33                let mut remain = *self;
34                loop {
35                    let digit = remain % BASE;
36                    remain /= BASE;
37
38                    offset -= 1;
39                    // SAFETY: `remain` will reach 0 and we will break before `offset` wraps
40                    unsafe { core::hint::assert_unchecked(offset < buf.len()) }
41                    buf[offset].write(DIG_TAB[digit as usize]);
42                    if remain == 0 {
43                        break;
44                    }
45                }
46
47                // SAFETY: Starting from `offset`, all elements of the slice have been set.
48                let digits = unsafe { slice_buffer_to_str(&buf, offset) };
49                f.pad_integral(true, $prefix, digits)
50            }
51        }
52
53        #[stable(feature = "rust1", since = "1.0.0")]
54        impl fmt::$Trait for $Signed {
55            /// Format signed integers in the two’s-complement form.
56            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
57                fmt::$Trait::fmt(&self.cast_unsigned(), f)
58            }
59        }
60    };
61}
62
63/// Formatting of integers with a non-decimal radix.
64macro_rules! radix_integers {
65    ($Signed:ident, $Unsigned:ident) => {
66        radix_integer! { fmt::Binary   for $Signed and $Unsigned, "0b", b"01" }
67        radix_integer! { fmt::Octal    for $Signed and $Unsigned, "0o", b"01234567" }
68        radix_integer! { fmt::LowerHex for $Signed and $Unsigned, "0x", b"0123456789abcdef" }
69        radix_integer! { fmt::UpperHex for $Signed and $Unsigned, "0x", b"0123456789ABCDEF" }
70    };
71}
72radix_integers! { isize, usize }
73radix_integers! { i8, u8 }
74radix_integers! { i16, u16 }
75radix_integers! { i32, u32 }
76radix_integers! { i64, u64 }
77radix_integers! { i128, u128 }
78
79macro_rules! impl_Debug {
80    ($($T:ident)*) => {
81        $(
82            #[stable(feature = "rust1", since = "1.0.0")]
83            impl fmt::Debug for $T {
84                #[inline]
85                fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
86                    if f.debug_lower_hex() {
87                        fmt::LowerHex::fmt(self, f)
88                    } else if f.debug_upper_hex() {
89                        fmt::UpperHex::fmt(self, f)
90                    } else {
91                        fmt::Display::fmt(self, f)
92                    }
93                }
94            }
95        )*
96    };
97}
98
99// The string of all two-digit numbers in range 00..99 is used as a lookup table.
100static DECIMAL_PAIRS: &[u8; 200] = b"\
101      0001020304050607080910111213141516171819\
102      2021222324252627282930313233343536373839\
103      4041424344454647484950515253545556575859\
104      6061626364656667686970717273747576777879\
105      8081828384858687888990919293949596979899";
106
107/// This function converts a slice of ascii characters into a `&str` starting from `offset`.
108///
109/// # Safety
110///
111/// `buf` content starting from `offset` index MUST BE initialized and MUST BE ascii
112/// characters.
113unsafe fn slice_buffer_to_str(buf: &[MaybeUninit<u8>], offset: usize) -> &str {
114    // SAFETY: `offset` is always included between 0 and `buf`'s length.
115    let written = unsafe { buf.get_unchecked(offset..) };
116    // SAFETY: (`assume_init_ref`) All buf content since offset is set.
117    // SAFETY: (`from_utf8_unchecked`) Writes use ASCII from the lookup table exclusively.
118    unsafe { str::from_utf8_unchecked(written.assume_init_ref()) }
119}
120
121macro_rules! impl_Display {
122    ($($Signed:ident, $Unsigned:ident),* ; as $T:ident into $fmt_fn:ident) => {
123
124        $(
125        const _: () = {
126            assert!($Signed::MIN < 0, "need signed");
127            assert!($Unsigned::MIN == 0, "need unsigned");
128            assert!($Signed::BITS == $Unsigned::BITS, "need counterparts");
129            assert!($Signed::BITS <= $T::BITS, "need lossless conversion");
130            assert!($Unsigned::BITS <= $T::BITS, "need lossless conversion");
131        };
132
133        #[stable(feature = "rust1", since = "1.0.0")]
134        impl fmt::Display for $Unsigned {
135            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
136                #[cfg(not(feature = "optimize_for_size"))]
137                {
138                    const MAX_DEC_N: usize = $Unsigned::MAX.ilog10() as usize + 1;
139                    // Buffer decimals for self with right alignment.
140                    let mut buf = [MaybeUninit::<u8>::uninit(); MAX_DEC_N];
141
142                    // SAFETY: `buf` is always big enough to contain all the digits.
143                    unsafe { f.pad_integral(true, "", self._fmt(&mut buf)) }
144                }
145                #[cfg(feature = "optimize_for_size")]
146                {
147                    // Lossless conversion (with as) is asserted at the top of
148                    // this macro.
149                    ${concat($fmt_fn, _small)}(*self as $T, true, f)
150                }
151            }
152        }
153
154        #[stable(feature = "rust1", since = "1.0.0")]
155        impl fmt::Display for $Signed {
156            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
157                #[cfg(not(feature = "optimize_for_size"))]
158                {
159                    const MAX_DEC_N: usize = $Unsigned::MAX.ilog10() as usize + 1;
160                    // Buffer decimals for self with right alignment.
161                    let mut buf = [MaybeUninit::<u8>::uninit(); MAX_DEC_N];
162
163                    // SAFETY: `buf` is always big enough to contain all the digits.
164                    unsafe { f.pad_integral(*self >= 0, "", self.unsigned_abs()._fmt(&mut buf)) }
165                }
166                #[cfg(feature = "optimize_for_size")]
167                {
168                    // Lossless conversion (with as) is asserted at the top of
169                    // this macro.
170                    return ${concat($fmt_fn, _small)}(self.unsigned_abs() as $T, *self >= 0, f);
171                }
172            }
173        }
174
175        #[cfg(not(feature = "optimize_for_size"))]
176        impl $Unsigned {
177            #[doc(hidden)]
178            #[unstable(
179                feature = "fmt_internals",
180                reason = "specialized method meant to only be used by `SpecToString` implementation",
181                issue = "none"
182            )]
183            pub unsafe fn _fmt<'a>(self, buf: &'a mut [MaybeUninit::<u8>]) -> &'a str {
184                // SAFETY: `buf` will always be big enough to contain all digits.
185                let offset = unsafe { self._fmt_inner(buf) };
186                // SAFETY: Starting from `offset`, all elements of the slice have been set.
187                unsafe { slice_buffer_to_str(buf, offset) }
188            }
189
190            unsafe fn _fmt_inner(self, buf: &mut [MaybeUninit::<u8>]) -> usize {
191                // Count the number of bytes in buf that are not initialized.
192                let mut offset = buf.len();
193                // Consume the least-significant decimals from a working copy.
194                let mut remain = self;
195
196                // Format per four digits from the lookup table.
197                // Four digits need a 16-bit $Unsigned or wider.
198                while size_of::<Self>() > 1 && remain > 999.try_into().expect("branch is not hit for types that cannot fit 999 (u8)") {
199                    // SAFETY: All of the decimals fit in buf due to MAX_DEC_N
200                    // and the while condition ensures at least 4 more decimals.
201                    unsafe { core::hint::assert_unchecked(offset >= 4) }
202                    // SAFETY: The offset counts down from its initial buf.len()
203                    // without underflow due to the previous precondition.
204                    unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
205                    offset -= 4;
206
207                    // pull two pairs
208                    let scale: Self = 1_00_00.try_into().expect("branch is not hit for types that cannot fit 1E4 (u8)");
209                    let quad = remain % scale;
210                    remain /= scale;
211                    let pair1 = (quad / 100) as usize;
212                    let pair2 = (quad % 100) as usize;
213                    buf[offset + 0].write(DECIMAL_PAIRS[pair1 * 2 + 0]);
214                    buf[offset + 1].write(DECIMAL_PAIRS[pair1 * 2 + 1]);
215                    buf[offset + 2].write(DECIMAL_PAIRS[pair2 * 2 + 0]);
216                    buf[offset + 3].write(DECIMAL_PAIRS[pair2 * 2 + 1]);
217                }
218
219                // Format per two digits from the lookup table.
220                if remain > 9 {
221                    // SAFETY: All of the decimals fit in buf due to MAX_DEC_N
222                    // and the if condition ensures at least 2 more decimals.
223                    unsafe { core::hint::assert_unchecked(offset >= 2) }
224                    // SAFETY: The offset counts down from its initial buf.len()
225                    // without underflow due to the previous precondition.
226                    unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
227                    offset -= 2;
228
229                    let pair = (remain % 100) as usize;
230                    remain /= 100;
231                    buf[offset + 0].write(DECIMAL_PAIRS[pair * 2 + 0]);
232                    buf[offset + 1].write(DECIMAL_PAIRS[pair * 2 + 1]);
233                }
234
235                // Format the last remaining digit, if any.
236                if remain != 0 || self == 0 {
237                    // SAFETY: All of the decimals fit in buf due to MAX_DEC_N
238                    // and the if condition ensures (at least) 1 more decimals.
239                    unsafe { core::hint::assert_unchecked(offset >= 1) }
240                    // SAFETY: The offset counts down from its initial buf.len()
241                    // without underflow due to the previous precondition.
242                    unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
243                    offset -= 1;
244
245                    // Either the compiler sees that remain < 10, or it prevents
246                    // a boundary check up next.
247                    let last = (remain & 15) as usize;
248                    buf[offset].write(DECIMAL_PAIRS[last * 2 + 1]);
249                    // not used: remain = 0;
250                }
251
252                offset
253            }
254        }
255
256        impl $Signed {
257            /// Allows users to write an integer (in signed decimal format) into a variable `buf` of
258            /// type [`NumBuffer`] that is passed by the caller by mutable reference.
259            ///
260            /// # Examples
261            ///
262            /// ```
263            /// #![feature(int_format_into)]
264            /// use core::fmt::NumBuffer;
265            ///
266            #[doc = concat!("let n = 0", stringify!($Signed), ";")]
267            /// let mut buf = NumBuffer::new();
268            /// assert_eq!(n.format_into(&mut buf), "0");
269            ///
270            #[doc = concat!("let n1 = 32", stringify!($Signed), ";")]
271            /// assert_eq!(n1.format_into(&mut buf), "32");
272            ///
273            #[doc = concat!("let n2 = ", stringify!($Signed::MAX), ";")]
274            #[doc = concat!("assert_eq!(n2.format_into(&mut buf), ", stringify!($Signed::MAX), ".to_string());")]
275            /// ```
276            #[unstable(feature = "int_format_into", issue = "138215")]
277            pub fn format_into(self, buf: &mut NumBuffer<Self>) -> &str {
278                let mut offset;
279
280                #[cfg(not(feature = "optimize_for_size"))]
281                // SAFETY: `buf` will always be big enough to contain all digits.
282                unsafe {
283                    offset = self.unsigned_abs()._fmt_inner(&mut buf.buf);
284                }
285                #[cfg(feature = "optimize_for_size")]
286                {
287                    // Lossless conversion (with as) is asserted at the top of
288                    // this macro.
289                    offset = ${concat($fmt_fn, _in_buf_small)}(self.unsigned_abs() as $T, &mut buf.buf);
290                }
291                // Only difference between signed and unsigned are these 4 lines.
292                if self < 0 {
293                    offset -= 1;
294                    buf.buf[offset].write(b'-');
295                }
296                // SAFETY: Starting from `offset`, all elements of the slice have been set.
297                unsafe { slice_buffer_to_str(&buf.buf, offset) }
298            }
299        }
300
301        impl $Unsigned {
302            /// Allows users to write an integer (in signed decimal format) into a variable `buf` of
303            /// type [`NumBuffer`] that is passed by the caller by mutable reference.
304            ///
305            /// # Examples
306            ///
307            /// ```
308            /// #![feature(int_format_into)]
309            /// use core::fmt::NumBuffer;
310            ///
311            #[doc = concat!("let n = 0", stringify!($Unsigned), ";")]
312            /// let mut buf = NumBuffer::new();
313            /// assert_eq!(n.format_into(&mut buf), "0");
314            ///
315            #[doc = concat!("let n1 = 32", stringify!($Unsigned), ";")]
316            /// assert_eq!(n1.format_into(&mut buf), "32");
317            ///
318            #[doc = concat!("let n2 = ", stringify!($Unsigned::MAX), ";")]
319            #[doc = concat!("assert_eq!(n2.format_into(&mut buf), ", stringify!($Unsigned::MAX), ".to_string());")]
320            /// ```
321            #[unstable(feature = "int_format_into", issue = "138215")]
322            pub fn format_into(self, buf: &mut NumBuffer<Self>) -> &str {
323                let offset;
324
325                #[cfg(not(feature = "optimize_for_size"))]
326                // SAFETY: `buf` will always be big enough to contain all digits.
327                unsafe {
328                    offset = self._fmt_inner(&mut buf.buf);
329                }
330                #[cfg(feature = "optimize_for_size")]
331                {
332                    // Lossless conversion (with as) is asserted at the top of
333                    // this macro.
334                    offset = ${concat($fmt_fn, _in_buf_small)}(self as $T, &mut buf.buf);
335                }
336                // SAFETY: Starting from `offset`, all elements of the slice have been set.
337                unsafe { slice_buffer_to_str(&buf.buf, offset) }
338            }
339        }
340
341        )*
342
343        #[cfg(feature = "optimize_for_size")]
344        fn ${concat($fmt_fn, _in_buf_small)}(mut n: $T, buf: &mut [MaybeUninit::<u8>]) -> usize {
345            let mut curr = buf.len();
346
347            // SAFETY: To show that it's OK to copy into `buf_ptr`, notice that at the beginning
348            // `curr == buf.len() == 39 > log(n)` since `n < 2^128 < 10^39`, and at
349            // each step this is kept the same as `n` is divided. Since `n` is always
350            // non-negative, this means that `curr > 0` so `buf_ptr[curr..curr + 1]`
351            // is safe to access.
352            loop {
353                curr -= 1;
354                buf[curr].write((n % 10) as u8 + b'0');
355                n /= 10;
356
357                if n == 0 {
358                    break;
359                }
360            }
361            curr
362        }
363
364        #[cfg(feature = "optimize_for_size")]
365        fn ${concat($fmt_fn, _small)}(n: $T, is_nonnegative: bool, f: &mut fmt::Formatter<'_>) -> fmt::Result {
366            const MAX_DEC_N: usize = $T::MAX.ilog(10) as usize + 1;
367            let mut buf = [MaybeUninit::<u8>::uninit(); MAX_DEC_N];
368
369            let offset = ${concat($fmt_fn, _in_buf_small)}(n, &mut buf);
370            // SAFETY: Starting from `offset`, all elements of the slice have been set.
371            let buf_slice = unsafe { slice_buffer_to_str(&buf, offset) };
372            f.pad_integral(is_nonnegative, "", buf_slice)
373        }
374    };
375}
376
377macro_rules! impl_Exp {
378    ($($Signed:ident, $Unsigned:ident),* ; as $T:ident into $fmt_fn:ident) => {
379        const _: () = assert!($T::MIN == 0, "need unsigned");
380
381        fn $fmt_fn(
382            f: &mut fmt::Formatter<'_>,
383            n: $T,
384            is_nonnegative: bool,
385            letter_e: u8
386        ) -> fmt::Result {
387            debug_assert!(letter_e.is_ascii_alphabetic(), "single-byte character");
388
389            // Print the integer as a coefficient in range (-10, 10).
390            let mut exp = n.checked_ilog10().unwrap_or(0) as usize;
391            debug_assert!(n / (10 as $T).pow(exp as u32) < 10);
392
393            // Precisison is counted as the number of digits in the fraction.
394            let mut coef_prec = exp;
395            // Keep the digits as an integer (paired with its coef_prec count).
396            let mut coef = n;
397
398            // A Formatter may set the precision to a fixed number of decimals.
399            let more_prec = match f.precision() {
400                None => {
401                    // Omit any and all trailing zeroes.
402                    while coef_prec != 0 && coef % 10 == 0 {
403                        coef /= 10;
404                        coef_prec -= 1;
405                    }
406                    0
407                },
408
409                Some(fmt_prec) if fmt_prec >= coef_prec => {
410                    // Count the number of additional zeroes needed.
411                    fmt_prec - coef_prec
412                },
413
414                Some(fmt_prec) => {
415                    // Count the number of digits to drop.
416                    let less_prec = coef_prec - fmt_prec;
417                    assert!(less_prec > 0);
418                    // Scale down the coefficient/precision pair. For example,
419                    // coef 123456 gets coef_prec 5 (to make 1.23456). To format
420                    // the number with 2 decimals, i.e., fmt_prec 2, coef should
421                    // be scaled by 10⁵⁻²=1000 to get coef 123 with coef_prec 2.
422
423                    // SAFETY: Any precision less than coef_prec will cause a
424                    // power of ten below the coef value.
425                    let scale = unsafe {
426                        (10 as $T).checked_pow(less_prec as u32).unwrap_unchecked()
427                    };
428                    let floor = coef / scale;
429                    // Round half to even conform documentation.
430                    let over = coef % scale;
431                    let half = scale / 2;
432                    let round_up = if over < half {
433                        0
434                    } else if over > half {
435                        1
436                    } else {
437                        floor & 1 // round odd up to even
438                    };
439                    // Adding one to a scale down of at least 10 won't overflow.
440                    coef = floor + round_up;
441                    coef_prec = fmt_prec;
442
443                    // The round_up may have caused the coefficient to reach 10
444                    // (which is not permitted). For example, anything in range
445                    // [9.95, 10) becomes 10.0 when adjusted to precision 1.
446                    if round_up != 0 && coef.checked_ilog10().unwrap_or(0) as usize > coef_prec {
447                        debug_assert_eq!(coef, (10 as $T).pow(coef_prec as u32 + 1));
448                        coef /= 10; // drop one trailing zero
449                        exp += 1;   // one power of ten higher
450                    }
451                    0
452                },
453            };
454
455            // Allocate a text buffer with lazy initialization.
456            const MAX_DEC_N: usize = $T::MAX.ilog10() as usize + 1;
457            const MAX_COEF_LEN: usize = MAX_DEC_N + ".".len();
458            const MAX_TEXT_LEN: usize = MAX_COEF_LEN + "e99".len();
459            let mut buf = [MaybeUninit::<u8>::uninit(); MAX_TEXT_LEN];
460
461            // Encode the coefficient in buf[..coef_len].
462            let (lead_dec, coef_len) = if coef_prec == 0 && more_prec == 0 {
463                (coef, 1_usize) // single digit; no fraction
464            } else {
465                buf[1].write(b'.');
466                let fraction_range = 2..(2 + coef_prec);
467
468                // Consume the least-significant decimals from a working copy.
469                let mut remain = coef;
470                #[cfg(feature = "optimize_for_size")] {
471                    for i in fraction_range.clone().rev() {
472                        let digit = (remain % 10) as usize;
473                        remain /= 10;
474                        buf[i].write(b'0' + digit as u8);
475                    }
476                }
477                #[cfg(not(feature = "optimize_for_size"))] {
478                    // Write digits per two at a time with a lookup table.
479                    for i in fraction_range.clone().skip(1).rev().step_by(2) {
480                        let pair = (remain % 100) as usize;
481                        remain /= 100;
482                        buf[i - 1].write(DECIMAL_PAIRS[pair * 2 + 0]);
483                        buf[i - 0].write(DECIMAL_PAIRS[pair * 2 + 1]);
484                    }
485                    // An odd number of digits leave one digit remaining.
486                    if coef_prec & 1 != 0 {
487                        let digit = (remain % 10) as usize;
488                        remain /= 10;
489                        buf[fraction_range.start].write(b'0' + digit as u8);
490                    }
491                }
492
493                (remain, fraction_range.end)
494            };
495            debug_assert!(lead_dec < 10);
496            debug_assert!(lead_dec != 0 || coef == 0, "significant digits only");
497            buf[0].write(b'0' + lead_dec as u8);
498
499            // SAFETY: The number of decimals is limited, captured by MAX.
500            unsafe { core::hint::assert_unchecked(coef_len <= MAX_COEF_LEN) }
501            // Encode the scale factor in buf[coef_len..text_len].
502            buf[coef_len].write(letter_e);
503            let text_len: usize = match exp {
504                ..10 => {
505                    buf[coef_len + 1].write(b'0' + exp as u8);
506                    coef_len + 2
507                },
508                10..100 => {
509                    #[cfg(feature = "optimize_for_size")] {
510                        buf[coef_len + 1].write(b'0' + (exp / 10) as u8);
511                        buf[coef_len + 2].write(b'0' + (exp % 10) as u8);
512                    }
513                    #[cfg(not(feature = "optimize_for_size"))] {
514                        buf[coef_len + 1].write(DECIMAL_PAIRS[exp * 2 + 0]);
515                        buf[coef_len + 2].write(DECIMAL_PAIRS[exp * 2 + 1]);
516                    }
517                    coef_len + 3
518                },
519                _ => {
520                    const { assert!($T::MAX.ilog10() < 100) };
521                    // SAFETY: A `u256::MAX` would get exponent 77.
522                    unsafe { core::hint::unreachable_unchecked() }
523                }
524            };
525            // SAFETY: All bytes up until text_len have been set.
526            let text = unsafe { buf[..text_len].assume_init_ref() };
527
528            if more_prec == 0 {
529                // SAFETY: Text is set with ASCII exclusively: either a decimal,
530                // or a LETTER_E, or a dot. ASCII implies valid UTF-8.
531                let as_str = unsafe { str::from_utf8_unchecked(text) };
532                f.pad_integral(is_nonnegative, "", as_str)
533            } else {
534                let parts = &[
535                    numfmt::Part::Copy(&text[..coef_len]),
536                    numfmt::Part::Zero(more_prec),
537                    numfmt::Part::Copy(&text[coef_len..]),
538                ];
539                let sign = if !is_nonnegative {
540                    "-"
541                } else if f.sign_plus() {
542                    "+"
543                } else {
544                    ""
545                };
546                // SAFETY: Text is set with ASCII exclusively: either a decimal,
547                // or a LETTER_E, or a dot. ASCII implies valid UTF-8.
548                unsafe { f.pad_formatted_parts(&numfmt::Formatted { sign, parts }) }
549            }
550        }
551
552        $(
553        const _: () = {
554            assert!($Signed::MIN < 0, "need signed");
555            assert!($Unsigned::MIN == 0, "need unsigned");
556            assert!($Signed::BITS == $Unsigned::BITS, "need counterparts");
557            assert!($Signed::BITS <= $T::BITS, "need lossless conversion");
558            assert!($Unsigned::BITS <= $T::BITS, "need lossless conversion");
559        };
560        #[stable(feature = "integer_exp_format", since = "1.42.0")]
561        impl fmt::LowerExp for $Signed {
562            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
563                $fmt_fn(f, self.unsigned_abs() as $T, *self >= 0, b'e')
564            }
565        }
566        #[stable(feature = "integer_exp_format", since = "1.42.0")]
567        impl fmt::LowerExp for $Unsigned {
568            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
569                $fmt_fn(f, *self as $T, true, b'e')
570            }
571        }
572        #[stable(feature = "integer_exp_format", since = "1.42.0")]
573        impl fmt::UpperExp for $Signed {
574            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
575                $fmt_fn(f, self.unsigned_abs() as $T, *self >= 0, b'E')
576            }
577        }
578        #[stable(feature = "integer_exp_format", since = "1.42.0")]
579        impl fmt::UpperExp for $Unsigned {
580            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
581                $fmt_fn(f, *self as $T, true, b'E')
582            }
583        }
584        )*
585
586    };
587}
588
589impl_Debug! {
590    i8 i16 i32 i64 i128 isize
591    u8 u16 u32 u64 u128 usize
592}
593
594// Include wasm32 in here since it doesn't reflect the native pointer size, and
595// often cares strongly about getting a smaller code size.
596#[cfg(any(target_pointer_width = "64", target_arch = "wasm32"))]
597mod imp {
598    use super::*;
599    impl_Display!(i8, u8, i16, u16, i32, u32, i64, u64, isize, usize; as u64 into display_u64);
600    impl_Exp!(i8, u8, i16, u16, i32, u32, i64, u64, isize, usize; as u64 into exp_u64);
601}
602
603#[cfg(not(any(target_pointer_width = "64", target_arch = "wasm32")))]
604mod imp {
605    use super::*;
606    impl_Display!(i8, u8, i16, u16, i32, u32, isize, usize; as u32 into display_u32);
607    impl_Display!(i64, u64; as u64 into display_u64);
608
609    impl_Exp!(i8, u8, i16, u16, i32, u32, isize, usize; as u32 into exp_u32);
610    impl_Exp!(i64, u64; as u64 into exp_u64);
611}
612impl_Exp!(i128, u128; as u128 into exp_u128);
613
614const U128_MAX_DEC_N: usize = u128::MAX.ilog10() as usize + 1;
615
616#[stable(feature = "rust1", since = "1.0.0")]
617impl fmt::Display for u128 {
618    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
619        let mut buf = [MaybeUninit::<u8>::uninit(); U128_MAX_DEC_N];
620
621        // SAFETY: `buf` is always big enough to contain all the digits.
622        unsafe { f.pad_integral(true, "", self._fmt(&mut buf)) }
623    }
624}
625
626#[stable(feature = "rust1", since = "1.0.0")]
627impl fmt::Display for i128 {
628    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
629        // This is not a typo, we use the maximum number of digits of `u128`, hence why we use
630        // `U128_MAX_DEC_N`.
631        let mut buf = [MaybeUninit::<u8>::uninit(); U128_MAX_DEC_N];
632
633        let is_nonnegative = *self >= 0;
634        // SAFETY: `buf` is always big enough to contain all the digits.
635        unsafe { f.pad_integral(is_nonnegative, "", self.unsigned_abs()._fmt(&mut buf)) }
636    }
637}
638
639impl u128 {
640    /// Format optimized for u128. Computation of 128 bits is limited by processing
641    /// in batches of 16 decimals at a time.
642    #[doc(hidden)]
643    #[unstable(
644        feature = "fmt_internals",
645        reason = "specialized method meant to only be used by `SpecToString` implementation",
646        issue = "none"
647    )]
648    pub unsafe fn _fmt<'a>(self, buf: &'a mut [MaybeUninit<u8>]) -> &'a str {
649        // SAFETY: `buf` will always be big enough to contain all digits.
650        let offset = unsafe { self._fmt_inner(buf) };
651        // SAFETY: Starting from `offset`, all elements of the slice have been set.
652        unsafe { slice_buffer_to_str(buf, offset) }
653    }
654
655    unsafe fn _fmt_inner(self, buf: &mut [MaybeUninit<u8>]) -> usize {
656        // Optimize common-case zero, which would also need special treatment due to
657        // its "leading" zero.
658        if self == 0 {
659            let offset = buf.len() - 1;
660            buf[offset].write(b'0');
661            return offset;
662        }
663        // Take the 16 least-significant decimals.
664        let (quot_1e16, mod_1e16) = div_rem_1e16(self);
665        let (mut remain, mut offset) = if quot_1e16 == 0 {
666            (mod_1e16, U128_MAX_DEC_N)
667        } else {
668            // Write digits at buf[23..39].
669            enc_16lsd::<{ U128_MAX_DEC_N - 16 }>(buf, mod_1e16);
670
671            // Take another 16 decimals.
672            let (quot2, mod2) = div_rem_1e16(quot_1e16);
673            if quot2 == 0 {
674                (mod2, U128_MAX_DEC_N - 16)
675            } else {
676                // Write digits at buf[7..23].
677                enc_16lsd::<{ U128_MAX_DEC_N - 32 }>(buf, mod2);
678                // Quot2 has at most 7 decimals remaining after two 1e16 divisions.
679                (quot2 as u64, U128_MAX_DEC_N - 32)
680            }
681        };
682
683        // Format per four digits from the lookup table.
684        while remain > 999 {
685            // SAFETY: All of the decimals fit in buf due to U128_MAX_DEC_N
686            // and the while condition ensures at least 4 more decimals.
687            unsafe { core::hint::assert_unchecked(offset >= 4) }
688            // SAFETY: The offset counts down from its initial buf.len()
689            // without underflow due to the previous precondition.
690            unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
691            offset -= 4;
692
693            // pull two pairs
694            let quad = remain % 1_00_00;
695            remain /= 1_00_00;
696            let pair1 = (quad / 100) as usize;
697            let pair2 = (quad % 100) as usize;
698            buf[offset + 0].write(DECIMAL_PAIRS[pair1 * 2 + 0]);
699            buf[offset + 1].write(DECIMAL_PAIRS[pair1 * 2 + 1]);
700            buf[offset + 2].write(DECIMAL_PAIRS[pair2 * 2 + 0]);
701            buf[offset + 3].write(DECIMAL_PAIRS[pair2 * 2 + 1]);
702        }
703
704        // Format per two digits from the lookup table.
705        if remain > 9 {
706            // SAFETY: All of the decimals fit in buf due to U128_MAX_DEC_N
707            // and the if condition ensures at least 2 more decimals.
708            unsafe { core::hint::assert_unchecked(offset >= 2) }
709            // SAFETY: The offset counts down from its initial buf.len()
710            // without underflow due to the previous precondition.
711            unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
712            offset -= 2;
713
714            let pair = (remain % 100) as usize;
715            remain /= 100;
716            buf[offset + 0].write(DECIMAL_PAIRS[pair * 2 + 0]);
717            buf[offset + 1].write(DECIMAL_PAIRS[pair * 2 + 1]);
718        }
719
720        // Format the last remaining digit, if any.
721        if remain != 0 {
722            // SAFETY: All of the decimals fit in buf due to U128_MAX_DEC_N
723            // and the if condition ensures (at least) 1 more decimals.
724            unsafe { core::hint::assert_unchecked(offset >= 1) }
725            // SAFETY: The offset counts down from its initial buf.len()
726            // without underflow due to the previous precondition.
727            unsafe { core::hint::assert_unchecked(offset <= buf.len()) }
728            offset -= 1;
729
730            // Either the compiler sees that remain < 10, or it prevents
731            // a boundary check up next.
732            let last = (remain & 15) as usize;
733            buf[offset].write(DECIMAL_PAIRS[last * 2 + 1]);
734            // not used: remain = 0;
735        }
736        offset
737    }
738
739    /// Allows users to write an integer (in signed decimal format) into a variable `buf` of
740    /// type [`NumBuffer`] that is passed by the caller by mutable reference.
741    ///
742    /// # Examples
743    ///
744    /// ```
745    /// #![feature(int_format_into)]
746    /// use core::fmt::NumBuffer;
747    ///
748    /// let n = 0u128;
749    /// let mut buf = NumBuffer::new();
750    /// assert_eq!(n.format_into(&mut buf), "0");
751    ///
752    /// let n1 = 32u128;
753    /// let mut buf1 = NumBuffer::new();
754    /// assert_eq!(n1.format_into(&mut buf1), "32");
755    ///
756    /// let n2 = u128::MAX;
757    /// let mut buf2 = NumBuffer::new();
758    /// assert_eq!(n2.format_into(&mut buf2), u128::MAX.to_string());
759    /// ```
760    #[unstable(feature = "int_format_into", issue = "138215")]
761    pub fn format_into(self, buf: &mut NumBuffer<Self>) -> &str {
762        let diff = buf.capacity() - U128_MAX_DEC_N;
763        // FIXME: Once const generics are better, use `NumberBufferTrait::BUF_SIZE` as generic const
764        // for `fmt_u128_inner`.
765        //
766        // In the meantime, we have to use a slice starting at index 1 and add 1 to the returned
767        // offset to ensure the number is correctly generated at the end of the buffer.
768        // SAFETY: `diff` will always be between 0 and its initial value.
769        unsafe { self._fmt(buf.buf.get_unchecked_mut(diff..)) }
770    }
771}
772
773impl i128 {
774    /// Allows users to write an integer (in signed decimal format) into a variable `buf` of
775    /// type [`NumBuffer`] that is passed by the caller by mutable reference.
776    ///
777    /// # Examples
778    ///
779    /// ```
780    /// #![feature(int_format_into)]
781    /// use core::fmt::NumBuffer;
782    ///
783    /// let n = 0i128;
784    /// let mut buf = NumBuffer::new();
785    /// assert_eq!(n.format_into(&mut buf), "0");
786    ///
787    /// let n1 = i128::MIN;
788    /// assert_eq!(n1.format_into(&mut buf), i128::MIN.to_string());
789    ///
790    /// let n2 = i128::MAX;
791    /// assert_eq!(n2.format_into(&mut buf), i128::MAX.to_string());
792    /// ```
793    #[unstable(feature = "int_format_into", issue = "138215")]
794    pub fn format_into(self, buf: &mut NumBuffer<Self>) -> &str {
795        let diff = buf.capacity() - U128_MAX_DEC_N;
796        // FIXME: Once const generics are better, use `NumberBufferTrait::BUF_SIZE` as generic const
797        // for `fmt_u128_inner`.
798        //
799        // In the meantime, we have to use a slice starting at index 1 and add 1 to the returned
800        // offset to ensure the number is correctly generated at the end of the buffer.
801        let mut offset =
802            // SAFETY: `buf` will always be big enough to contain all digits.
803            unsafe { self.unsigned_abs()._fmt_inner(buf.buf.get_unchecked_mut(diff..)) };
804        // We put back the offset at the right position.
805        offset += diff;
806        // Only difference between signed and unsigned are these 4 lines.
807        if self < 0 {
808            offset -= 1;
809            // SAFETY: `buf` will always be big enough to contain all digits plus the minus sign.
810            unsafe {
811                buf.buf.get_unchecked_mut(offset).write(b'-');
812            }
813        }
814        // SAFETY: Starting from `offset`, all elements of the slice have been set.
815        unsafe { slice_buffer_to_str(&buf.buf, offset) }
816    }
817}
818
819/// Encodes the 16 least-significant decimals of n into `buf[OFFSET .. OFFSET +
820/// 16 ]`.
821fn enc_16lsd<const OFFSET: usize>(buf: &mut [MaybeUninit<u8>], n: u64) {
822    // Consume the least-significant decimals from a working copy.
823    let mut remain = n;
824
825    // Format per four digits from the lookup table.
826    for quad_index in (0..4).rev() {
827        // pull two pairs
828        let quad = remain % 1_00_00;
829        remain /= 1_00_00;
830        let pair1 = (quad / 100) as usize;
831        let pair2 = (quad % 100) as usize;
832        buf[quad_index * 4 + OFFSET + 0].write(DECIMAL_PAIRS[pair1 * 2 + 0]);
833        buf[quad_index * 4 + OFFSET + 1].write(DECIMAL_PAIRS[pair1 * 2 + 1]);
834        buf[quad_index * 4 + OFFSET + 2].write(DECIMAL_PAIRS[pair2 * 2 + 0]);
835        buf[quad_index * 4 + OFFSET + 3].write(DECIMAL_PAIRS[pair2 * 2 + 1]);
836    }
837}
838
839/// Euclidean division plus remainder with constant 1E16 basically consumes 16
840/// decimals from n.
841///
842/// The integer division algorithm is based on the following paper:
843///
844///   T. Granlund and P. Montgomery, “Division by Invariant Integers Using Multiplication”
845///   in Proc. of the SIGPLAN94 Conference on Programming Language Design and
846///   Implementation, 1994, pp. 61–72
847///
848#[inline]
849fn div_rem_1e16(n: u128) -> (u128, u64) {
850    const D: u128 = 1_0000_0000_0000_0000;
851    // The check inlines well with the caller flow.
852    if n < D {
853        return (0, n as u64);
854    }
855
856    // These constant values are computed with the CHOOSE_MULTIPLIER procedure
857    // from the Granlund & Montgomery paper, using N=128, prec=128 and d=1E16.
858    const M_HIGH: u128 = 76624777043294442917917351357515459181;
859    const SH_POST: u8 = 51;
860
861    let quot = n.widening_mul(M_HIGH).1 >> SH_POST;
862    let rem = n - quot * D;
863    (quot, rem as u64)
864}
````