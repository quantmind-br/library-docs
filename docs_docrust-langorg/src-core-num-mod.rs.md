---
title: mod.rs - source
url: https://doc.rust-lang.org/src/core/num/mod.rs.html#546-570
source: crawler
fetched_at: 2026-05-06T21:29:34.968397775-03:00
rendered_js: false
word_count: 7142
summary: This module provides fundamental numeric traits, functions, and wrappers for Rust's built-in integer and floating-point types.
tags:
    - rust
    - numeric-types
    - integer-math
    - floating-point
    - core-library
category: reference
---

## core/num/ mod.rs

````rust
1//! Numeric traits and functions for the built-in numeric types.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5use crate::panic::const_panic;
6use crate::str::FromStr;
7use crate::ub_checks::assert_unsafe_precondition;
8use crate::{ascii, intrinsics, mem};
9
10// FIXME(const-hack): Used because the `?` operator is not allowed in a const context.
11macro_rules! try_opt {
12    ($e:expr) => {
13        match $e {
14            Some(x) => x,
15            None => return None,
16        }
17    };
18}
19
20// Use this when the generated code should differ between signed and unsigned types.
21macro_rules! sign_dependent_expr {
22    (signed ? if signed { $signed_case:expr } if unsigned { $unsigned_case:expr } ) => {
23        $signed_case
24    };
25    (unsigned ? if signed { $signed_case:expr } if unsigned { $unsigned_case:expr } ) => {
26        $unsigned_case
27    };
28}
29
30// All these modules are technically private and only exposed for coretests:
31#[cfg(not(no_fp_fmt_parse))]
32pub mod bignum;
33#[cfg(not(no_fp_fmt_parse))]
34pub mod dec2flt;
35#[cfg(not(no_fp_fmt_parse))]
36pub mod diy_float;
37#[cfg(not(no_fp_fmt_parse))]
38pub mod flt2dec;
39pub mod fmt;
40
41#[macro_use]
42mod int_macros; // import int_impl!
43#[macro_use]
44mod uint_macros; // import uint_impl!
45
46mod error;
47mod int_bits;
48mod int_log10;
49mod int_sqrt;
50pub(crate) mod libm;
51mod nonzero;
52mod overflow_panic;
53mod saturating;
54mod wrapping;
55
56/// 100% perma-unstable
57#[doc(hidden)]
58pub mod niche_types;
59
60#[stable(feature = "rust1", since = "1.0.0")]
61#[cfg(not(no_fp_fmt_parse))]
62pub use dec2flt::ParseFloatError;
63#[stable(feature = "int_error_matching", since = "1.55.0")]
64pub use error::IntErrorKind;
65#[stable(feature = "rust1", since = "1.0.0")]
66pub use error::ParseIntError;
67#[stable(feature = "try_from", since = "1.34.0")]
68pub use error::TryFromIntError;
69#[stable(feature = "generic_nonzero", since = "1.79.0")]
70pub use nonzero::NonZero;
71#[unstable(
72    feature = "nonzero_internals",
73    reason = "implementation detail which may disappear or be replaced at any time",
74    issue = "none"
75)]
76pub use nonzero::ZeroablePrimitive;
77#[stable(feature = "signed_nonzero", since = "1.34.0")]
78pub use nonzero::{NonZeroI8, NonZeroI16, NonZeroI32, NonZeroI64, NonZeroI128, NonZeroIsize};
79#[stable(feature = "nonzero", since = "1.28.0")]
80pub use nonzero::{NonZeroU8, NonZeroU16, NonZeroU32, NonZeroU64, NonZeroU128, NonZeroUsize};
81#[stable(feature = "saturating_int_impl", since = "1.74.0")]
82pub use saturating::Saturating;
83#[stable(feature = "rust1", since = "1.0.0")]
84pub use wrapping::Wrapping;
85
86macro_rules! u8_xe_bytes_doc {
87    () => {
88        "
89
90**Note**: This function is meaningless on `u8`. Byte order does not exist as a
91concept for byte-sized integers. This function is only provided in symmetry
92with larger integer types.
93
94"
95    };
96}
97
98macro_rules! i8_xe_bytes_doc {
99    () => {
100        "
101
102**Note**: This function is meaningless on `i8`. Byte order does not exist as a
103concept for byte-sized integers. This function is only provided in symmetry
104with larger integer types. You can cast from and to `u8` using
105[`cast_signed`](u8::cast_signed) and [`cast_unsigned`](Self::cast_unsigned).
106
107"
108    };
109}
110
111macro_rules! usize_isize_to_xe_bytes_doc {
112    () => {
113        "
114
115**Note**: This function returns an array of length 2, 4 or 8 bytes
116depending on the target pointer size.
117
118"
119    };
120}
121
122macro_rules! usize_isize_from_xe_bytes_doc {
123    () => {
124        "
125
126**Note**: This function takes an array of length 2, 4 or 8 bytes
127depending on the target pointer size.
128
129"
130    };
131}
132
133macro_rules! midpoint_impl {
134    ($SelfT:ty, unsigned) => {
135        /// Calculates the midpoint (average) between `self` and `rhs`.
136        ///
137        /// `midpoint(a, b)` is `(a + b) / 2` as if it were performed in a
138        /// sufficiently-large unsigned integral type. This implies that the result is
139        /// always rounded towards zero and that no overflow will ever occur.
140        ///
141        /// # Examples
142        ///
143        /// ```
144        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(4), 2);")]
145        #[doc = concat!("assert_eq!(1", stringify!($SelfT), ".midpoint(4), 2);")]
146        /// ```
147        #[stable(feature = "num_midpoint", since = "1.85.0")]
148        #[rustc_const_stable(feature = "num_midpoint", since = "1.85.0")]
149        #[must_use = "this returns the result of the operation, \
150                      without modifying the original"]
151        #[doc(alias = "average_floor")]
152        #[doc(alias = "average")]
153        #[inline]
154        pub const fn midpoint(self, rhs: $SelfT) -> $SelfT {
155            // Use the well known branchless algorithm from Hacker's Delight to compute
156            // `(a + b) / 2` without overflowing: `((a ^ b) >> 1) + (a & b)`.
157            ((self ^ rhs) >> 1) + (self & rhs)
158        }
159    };
160    ($SelfT:ty, signed) => {
161        /// Calculates the midpoint (average) between `self` and `rhs`.
162        ///
163        /// `midpoint(a, b)` is `(a + b) / 2` as if it were performed in a
164        /// sufficiently-large signed integral type. This implies that the result is
165        /// always rounded towards zero and that no overflow will ever occur.
166        ///
167        /// # Examples
168        ///
169        /// ```
170        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(4), 2);")]
171        #[doc = concat!("assert_eq!((-1", stringify!($SelfT), ").midpoint(2), 0);")]
172        #[doc = concat!("assert_eq!((-7", stringify!($SelfT), ").midpoint(0), -3);")]
173        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(-7), -3);")]
174        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(7), 3);")]
175        /// ```
176        #[stable(feature = "num_midpoint_signed", since = "1.87.0")]
177        #[rustc_const_stable(feature = "num_midpoint_signed", since = "1.87.0")]
178        #[must_use = "this returns the result of the operation, \
179                      without modifying the original"]
180        #[doc(alias = "average_floor")]
181        #[doc(alias = "average_ceil")]
182        #[doc(alias = "average")]
183        #[inline]
184        pub const fn midpoint(self, rhs: Self) -> Self {
185            // Use the well known branchless algorithm from Hacker's Delight to compute
186            // `(a + b) / 2` without overflowing: `((a ^ b) >> 1) + (a & b)`.
187            let t = ((self ^ rhs) >> 1) + (self & rhs);
188            // Except that it fails for integers whose sum is an odd negative number as
189            // their floor is one less than their average. So we adjust the result.
190            t + (if t < 0 { 1 } else { 0 } & (self ^ rhs))
191        }
192    };
193    ($SelfT:ty, $WideT:ty, unsigned) => {
194        /// Calculates the midpoint (average) between `self` and `rhs`.
195        ///
196        /// `midpoint(a, b)` is `(a + b) / 2` as if it were performed in a
197        /// sufficiently-large unsigned integral type. This implies that the result is
198        /// always rounded towards zero and that no overflow will ever occur.
199        ///
200        /// # Examples
201        ///
202        /// ```
203        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(4), 2);")]
204        #[doc = concat!("assert_eq!(1", stringify!($SelfT), ".midpoint(4), 2);")]
205        /// ```
206        #[stable(feature = "num_midpoint", since = "1.85.0")]
207        #[rustc_const_stable(feature = "num_midpoint", since = "1.85.0")]
208        #[must_use = "this returns the result of the operation, \
209                      without modifying the original"]
210        #[doc(alias = "average_floor")]
211        #[doc(alias = "average")]
212        #[inline]
213        pub const fn midpoint(self, rhs: $SelfT) -> $SelfT {
214            ((self as $WideT + rhs as $WideT) / 2) as $SelfT
215        }
216    };
217    ($SelfT:ty, $WideT:ty, signed) => {
218        /// Calculates the midpoint (average) between `self` and `rhs`.
219        ///
220        /// `midpoint(a, b)` is `(a + b) / 2` as if it were performed in a
221        /// sufficiently-large signed integral type. This implies that the result is
222        /// always rounded towards zero and that no overflow will ever occur.
223        ///
224        /// # Examples
225        ///
226        /// ```
227        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(4), 2);")]
228        #[doc = concat!("assert_eq!((-1", stringify!($SelfT), ").midpoint(2), 0);")]
229        #[doc = concat!("assert_eq!((-7", stringify!($SelfT), ").midpoint(0), -3);")]
230        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(-7), -3);")]
231        #[doc = concat!("assert_eq!(0", stringify!($SelfT), ".midpoint(7), 3);")]
232        /// ```
233        #[stable(feature = "num_midpoint_signed", since = "1.87.0")]
234        #[rustc_const_stable(feature = "num_midpoint_signed", since = "1.87.0")]
235        #[must_use = "this returns the result of the operation, \
236                      without modifying the original"]
237        #[doc(alias = "average_floor")]
238        #[doc(alias = "average_ceil")]
239        #[doc(alias = "average")]
240        #[inline]
241        pub const fn midpoint(self, rhs: $SelfT) -> $SelfT {
242            ((self as $WideT + rhs as $WideT) / 2) as $SelfT
243        }
244    };
245}
246
247macro_rules! widening_carryless_mul_impl {
248    ($SelfT:ty, $WideT:ty) => {
249        /// Performs a widening carry-less multiplication.
250        ///
251        /// # Examples
252        ///
253        /// ```
254        /// #![feature(uint_carryless_mul)]
255        ///
256        #[doc = concat!("assert_eq!(", stringify!($SelfT), "::MAX.widening_carryless_mul(",
257                                stringify!($SelfT), "::MAX), ", stringify!($WideT), "::MAX / 3);")]
258        /// ```
259        #[rustc_const_unstable(feature = "uint_carryless_mul", issue = "152080")]
260        #[doc(alias = "clmul")]
261        #[unstable(feature = "uint_carryless_mul", issue = "152080")]
262        #[must_use = "this returns the result of the operation, \
263                      without modifying the original"]
264        #[inline]
265        pub const fn widening_carryless_mul(self, rhs: $SelfT) -> $WideT {
266            (self as $WideT).carryless_mul(rhs as $WideT)
267        }
268    }
269}
270
271macro_rules! carrying_carryless_mul_impl {
272    (u128, u256) => {
273        carrying_carryless_mul_impl! { @internal u128 =>
274            pub const fn carrying_carryless_mul(self, rhs: Self, carry: Self) -> (Self, Self) {
275                let x0 = self as u64;
276                let x1 = (self >> 64) as u64;
277                let y0 = rhs as u64;
278                let y1 = (rhs >> 64) as u64;
279
280                let z0 = u64::widening_carryless_mul(x0, y0);
281                let z2 = u64::widening_carryless_mul(x1, y1);
282
283                // The grade school algorithm would compute:
284                // z1 = x0y1 ^ x1y0
285
286                // Instead, Karatsuba first computes:
287                let z3 = u64::widening_carryless_mul(x0 ^ x1, y0 ^ y1);
288                // Since it distributes over XOR,
289                // z3 == x0y0 ^ x0y1 ^ x1y0 ^ x1y1
290                //       |--|   |---------|   |--|
291                //    ==  z0  ^     z1      ^  z2
292                // so we can compute z1 as
293                let z1 = z3 ^ z0 ^ z2;
294
295                let lo = z0 ^ (z1 << 64);
296                let hi = z2 ^ (z1 >> 64);
297
298                (lo ^ carry, hi)
299            }
300        }
301    };
302    ($SelfT:ty, $WideT:ty) => {
303        carrying_carryless_mul_impl! { @internal $SelfT =>
304            pub const fn carrying_carryless_mul(self, rhs: Self, carry: Self) -> (Self, Self) {
305                // Can't use widening_carryless_mul because it's not implemented for usize.
306                let p = (self as $WideT).carryless_mul(rhs as $WideT);
307
308                let lo = (p as $SelfT);
309                let hi = (p  >> Self::BITS) as $SelfT;
310
311                (lo ^ carry, hi)
312            }
313        }
314    };
315    (@internal $SelfT:ty => $($fn:tt)*) => {
316        /// Calculates the "full carryless multiplication" without the possibility to overflow.
317        ///
318        /// This returns the low-order (wrapping) bits and the high-order (overflow) bits
319        /// of the result as two separate values, in that order.
320        ///
321        /// # Examples
322        ///
323        /// Please note that this example is shared among integer types, which is why `u8` is used.
324        ///
325        /// ```
326        /// #![feature(uint_carryless_mul)]
327        ///
328        /// assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b0000), (0, 0b0100_0000));
329        /// assert_eq!(0b1000_0000u8.carrying_carryless_mul(0b1000_0000, 0b1111), (0b1111, 0b0100_0000));
330        #[doc = concat!("assert_eq!(",
331            stringify!($SelfT), "::MAX.carrying_carryless_mul(", stringify!($SelfT), "::MAX, ", stringify!($SelfT), "::MAX), ",
332            "(!(", stringify!($SelfT), "::MAX / 3), ", stringify!($SelfT), "::MAX / 3));"
333        )]
334        /// ```
335        #[rustc_const_unstable(feature = "uint_carryless_mul", issue = "152080")]
336        #[doc(alias = "clmul")]
337        #[unstable(feature = "uint_carryless_mul", issue = "152080")]
338        #[must_use = "this returns the result of the operation, \
339                      without modifying the original"]
340        #[inline]
341        $($fn)*
342    }
343}
344
345impl i8 {
346    int_impl! {
347        Self = i8,
348        ActualT = i8,
349        UnsignedT = u8,
350        BITS = 8,
351        BITS_MINUS_ONE = 7,
352        Min = -128,
353        Max = 127,
354        rot = 2,
355        rot_op = "-0x7e",
356        rot_result = "0xa",
357        swap_op = "0x12",
358        swapped = "0x12",
359        reversed = "0x48",
360        le_bytes = "[0x12]",
361        be_bytes = "[0x12]",
362        to_xe_bytes_doc = i8_xe_bytes_doc!(),
363        from_xe_bytes_doc = i8_xe_bytes_doc!(),
364        bound_condition = "",
365    }
366    midpoint_impl! { i8, i16, signed }
367}
368
369impl i16 {
370    int_impl! {
371        Self = i16,
372        ActualT = i16,
373        UnsignedT = u16,
374        BITS = 16,
375        BITS_MINUS_ONE = 15,
376        Min = -32768,
377        Max = 32767,
378        rot = 4,
379        rot_op = "-0x5ffd",
380        rot_result = "0x3a",
381        swap_op = "0x1234",
382        swapped = "0x3412",
383        reversed = "0x2c48",
384        le_bytes = "[0x34, 0x12]",
385        be_bytes = "[0x12, 0x34]",
386        to_xe_bytes_doc = "",
387        from_xe_bytes_doc = "",
388        bound_condition = "",
389    }
390    midpoint_impl! { i16, i32, signed }
391}
392
393impl i32 {
394    int_impl! {
395        Self = i32,
396        ActualT = i32,
397        UnsignedT = u32,
398        BITS = 32,
399        BITS_MINUS_ONE = 31,
400        Min = -2147483648,
401        Max = 2147483647,
402        rot = 8,
403        rot_op = "0x10000b3",
404        rot_result = "0xb301",
405        swap_op = "0x12345678",
406        swapped = "0x78563412",
407        reversed = "0x1e6a2c48",
408        le_bytes = "[0x78, 0x56, 0x34, 0x12]",
409        be_bytes = "[0x12, 0x34, 0x56, 0x78]",
410        to_xe_bytes_doc = "",
411        from_xe_bytes_doc = "",
412        bound_condition = "",
413    }
414    midpoint_impl! { i32, i64, signed }
415}
416
417impl i64 {
418    int_impl! {
419        Self = i64,
420        ActualT = i64,
421        UnsignedT = u64,
422        BITS = 64,
423        BITS_MINUS_ONE = 63,
424        Min = -9223372036854775808,
425        Max = 9223372036854775807,
426        rot = 12,
427        rot_op = "0xaa00000000006e1",
428        rot_result = "0x6e10aa",
429        swap_op = "0x1234567890123456",
430        swapped = "0x5634129078563412",
431        reversed = "0x6a2c48091e6a2c48",
432        le_bytes = "[0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
433        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]",
434        to_xe_bytes_doc = "",
435        from_xe_bytes_doc = "",
436        bound_condition = "",
437    }
438    midpoint_impl! { i64, signed }
439}
440
441impl i128 {
442    int_impl! {
443        Self = i128,
444        ActualT = i128,
445        UnsignedT = u128,
446        BITS = 128,
447        BITS_MINUS_ONE = 127,
448        Min = -170141183460469231731687303715884105728,
449        Max = 170141183460469231731687303715884105727,
450        rot = 16,
451        rot_op = "0x13f40000000000000000000000004f76",
452        rot_result = "0x4f7613f4",
453        swap_op = "0x12345678901234567890123456789012",
454        swapped = "0x12907856341290785634129078563412",
455        reversed = "0x48091e6a2c48091e6a2c48091e6a2c48",
456        le_bytes = "[0x12, 0x90, 0x78, 0x56, 0x34, 0x12, 0x90, 0x78, \
457            0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
458        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56, \
459            0x78, 0x90, 0x12, 0x34, 0x56, 0x78, 0x90, 0x12]",
460        to_xe_bytes_doc = "",
461        from_xe_bytes_doc = "",
462        bound_condition = "",
463    }
464    midpoint_impl! { i128, signed }
465}
466
467#[cfg(target_pointer_width = "16")]
468impl isize {
469    int_impl! {
470        Self = isize,
471        ActualT = i16,
472        UnsignedT = usize,
473        BITS = 16,
474        BITS_MINUS_ONE = 15,
475        Min = -32768,
476        Max = 32767,
477        rot = 4,
478        rot_op = "-0x5ffd",
479        rot_result = "0x3a",
480        swap_op = "0x1234",
481        swapped = "0x3412",
482        reversed = "0x2c48",
483        le_bytes = "[0x34, 0x12]",
484        be_bytes = "[0x12, 0x34]",
485        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
486        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
487        bound_condition = " on 16-bit targets",
488    }
489    midpoint_impl! { isize, i32, signed }
490}
491
492#[cfg(target_pointer_width = "32")]
493impl isize {
494    int_impl! {
495        Self = isize,
496        ActualT = i32,
497        UnsignedT = usize,
498        BITS = 32,
499        BITS_MINUS_ONE = 31,
500        Min = -2147483648,
501        Max = 2147483647,
502        rot = 8,
503        rot_op = "0x10000b3",
504        rot_result = "0xb301",
505        swap_op = "0x12345678",
506        swapped = "0x78563412",
507        reversed = "0x1e6a2c48",
508        le_bytes = "[0x78, 0x56, 0x34, 0x12]",
509        be_bytes = "[0x12, 0x34, 0x56, 0x78]",
510        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
511        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
512        bound_condition = " on 32-bit targets",
513    }
514    midpoint_impl! { isize, i64, signed }
515}
516
517#[cfg(target_pointer_width = "64")]
518impl isize {
519    int_impl! {
520        Self = isize,
521        ActualT = i64,
522        UnsignedT = usize,
523        BITS = 64,
524        BITS_MINUS_ONE = 63,
525        Min = -9223372036854775808,
526        Max = 9223372036854775807,
527        rot = 12,
528        rot_op = "0xaa00000000006e1",
529        rot_result = "0x6e10aa",
530        swap_op = "0x1234567890123456",
531        swapped = "0x5634129078563412",
532        reversed = "0x6a2c48091e6a2c48",
533        le_bytes = "[0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
534        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]",
535        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
536        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
537        bound_condition = " on 64-bit targets",
538    }
539    midpoint_impl! { isize, signed }
540}
541
542/// If the bit selected by this mask is set, ascii is lower case.
543const ASCII_CASE_MASK: u8 = 0b0010_0000;
544
545impl u8 {
546    uint_impl! {
547        Self = u8,
548        ActualT = u8,
549        SignedT = i8,
550        BITS = 8,
551        BITS_MINUS_ONE = 7,
552        MAX = 255,
553        rot = 2,
554        rot_op = "0x82",
555        rot_result = "0xa",
556        fsh_op = "0x36",
557        fshl_result = "0x8",
558        fshr_result = "0x8d",
559        clmul_lhs = "0x12",
560        clmul_rhs = "0x34",
561        clmul_result = "0x28",
562        swap_op = "0x12",
563        swapped = "0x12",
564        reversed = "0x48",
565        le_bytes = "[0x12]",
566        be_bytes = "[0x12]",
567        to_xe_bytes_doc = u8_xe_bytes_doc!(),
568        from_xe_bytes_doc = u8_xe_bytes_doc!(),
569        bound_condition = "",
570    }
571    midpoint_impl! { u8, u16, unsigned }
572    widening_carryless_mul_impl! { u8, u16 }
573    carrying_carryless_mul_impl! { u8, u16 }
574
575    /// Checks if the value is within the ASCII range.
576    ///
577    /// # Examples
578    ///
579    /// ```
580    /// let ascii = 97u8;
581    /// let non_ascii = 150u8;
582    ///
583    /// assert!(ascii.is_ascii());
584    /// assert!(!non_ascii.is_ascii());
585    /// ```
586    #[must_use]
587    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
588    #[rustc_const_stable(feature = "const_u8_is_ascii", since = "1.43.0")]
589    #[inline]
590    pub const fn is_ascii(&self) -> bool {
591        *self <= 127
592    }
593
594    /// If the value of this byte is within the ASCII range, returns it as an
595    /// [ASCII character](ascii::Char).  Otherwise, returns `None`.
596    #[must_use]
597    #[unstable(feature = "ascii_char", issue = "110998")]
598    #[inline]
599    pub const fn as_ascii(&self) -> Option<ascii::Char> {
600        ascii::Char::from_u8(*self)
601    }
602
603    /// Converts this byte to an [ASCII character](ascii::Char), without
604    /// checking whether or not it's valid.
605    ///
606    /// # Safety
607    ///
608    /// This byte must be valid ASCII, or else this is UB.
609    #[must_use]
610    #[unstable(feature = "ascii_char", issue = "110998")]
611    #[inline]
612    pub const unsafe fn as_ascii_unchecked(&self) -> ascii::Char {
613        assert_unsafe_precondition!(
614            check_library_ub,
615            "as_ascii_unchecked requires that the byte is valid ASCII",
616            (it: &u8 = self) => it.is_ascii()
617        );
618
619        // SAFETY: the caller promised that this byte is ASCII.
620        unsafe { ascii::Char::from_u8_unchecked(*self) }
621    }
622
623    /// Makes a copy of the value in its ASCII upper case equivalent.
624    ///
625    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
626    /// but non-ASCII letters are unchanged.
627    ///
628    /// To uppercase the value in-place, use [`make_ascii_uppercase`].
629    ///
630    /// # Examples
631    ///
632    /// ```
633    /// let lowercase_a = 97u8;
634    ///
635    /// assert_eq!(65, lowercase_a.to_ascii_uppercase());
636    /// ```
637    ///
638    /// [`make_ascii_uppercase`]: Self::make_ascii_uppercase
639    #[must_use = "to uppercase the value in-place, use `make_ascii_uppercase()`"]
640    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
641    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
642    #[inline]
643    pub const fn to_ascii_uppercase(&self) -> u8 {
644        // Toggle the 6th bit if this is a lowercase letter
645        *self ^ ((self.is_ascii_lowercase() as u8) * ASCII_CASE_MASK)
646    }
647
648    /// Makes a copy of the value in its ASCII lower case equivalent.
649    ///
650    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
651    /// but non-ASCII letters are unchanged.
652    ///
653    /// To lowercase the value in-place, use [`make_ascii_lowercase`].
654    ///
655    /// # Examples
656    ///
657    /// ```
658    /// let uppercase_a = 65u8;
659    ///
660    /// assert_eq!(97, uppercase_a.to_ascii_lowercase());
661    /// ```
662    ///
663    /// [`make_ascii_lowercase`]: Self::make_ascii_lowercase
664    #[must_use = "to lowercase the value in-place, use `make_ascii_lowercase()`"]
665    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
666    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
667    #[inline]
668    pub const fn to_ascii_lowercase(&self) -> u8 {
669        // Set the 6th bit if this is an uppercase letter
670        *self | (self.is_ascii_uppercase() as u8 * ASCII_CASE_MASK)
671    }
672
673    /// Assumes self is ascii
674    #[inline]
675    pub(crate) const fn ascii_change_case_unchecked(&self) -> u8 {
676        *self ^ ASCII_CASE_MASK
677    }
678
679    /// Checks that two values are an ASCII case-insensitive match.
680    ///
681    /// This is equivalent to `to_ascii_lowercase(a) == to_ascii_lowercase(b)`.
682    ///
683    /// # Examples
684    ///
685    /// ```
686    /// let lowercase_a = 97u8;
687    /// let uppercase_a = 65u8;
688    ///
689    /// assert!(lowercase_a.eq_ignore_ascii_case(&uppercase_a));
690    /// ```
691    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
692    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
693    #[inline]
694    pub const fn eq_ignore_ascii_case(&self, other: &u8) -> bool {
695        self.to_ascii_lowercase() == other.to_ascii_lowercase()
696    }
697
698    /// Converts this value to its ASCII upper case equivalent in-place.
699    ///
700    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
701    /// but non-ASCII letters are unchanged.
702    ///
703    /// To return a new uppercased value without modifying the existing one, use
704    /// [`to_ascii_uppercase`].
705    ///
706    /// # Examples
707    ///
708    /// ```
709    /// let mut byte = b'a';
710    ///
711    /// byte.make_ascii_uppercase();
712    ///
713    /// assert_eq!(b'A', byte);
714    /// ```
715    ///
716    /// [`to_ascii_uppercase`]: Self::to_ascii_uppercase
717    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
718    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
719    #[inline]
720    pub const fn make_ascii_uppercase(&mut self) {
721        *self = self.to_ascii_uppercase();
722    }
723
724    /// Converts this value to its ASCII lower case equivalent in-place.
725    ///
726    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
727    /// but non-ASCII letters are unchanged.
728    ///
729    /// To return a new lowercased value without modifying the existing one, use
730    /// [`to_ascii_lowercase`].
731    ///
732    /// # Examples
733    ///
734    /// ```
735    /// let mut byte = b'A';
736    ///
737    /// byte.make_ascii_lowercase();
738    ///
739    /// assert_eq!(b'a', byte);
740    /// ```
741    ///
742    /// [`to_ascii_lowercase`]: Self::to_ascii_lowercase
743    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
744    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
745    #[inline]
746    pub const fn make_ascii_lowercase(&mut self) {
747        *self = self.to_ascii_lowercase();
748    }
749
750    /// Checks if the value is an ASCII alphabetic character:
751    ///
752    /// - U+0041 'A' ..= U+005A 'Z', or
753    /// - U+0061 'a' ..= U+007A 'z'.
754    ///
755    /// # Examples
756    ///
757    /// ```
758    /// let uppercase_a = b'A';
759    /// let uppercase_g = b'G';
760    /// let a = b'a';
761    /// let g = b'g';
762    /// let zero = b'0';
763    /// let percent = b'%';
764    /// let space = b' ';
765    /// let lf = b'\n';
766    /// let esc = b'\x1b';
767    ///
768    /// assert!(uppercase_a.is_ascii_alphabetic());
769    /// assert!(uppercase_g.is_ascii_alphabetic());
770    /// assert!(a.is_ascii_alphabetic());
771    /// assert!(g.is_ascii_alphabetic());
772    /// assert!(!zero.is_ascii_alphabetic());
773    /// assert!(!percent.is_ascii_alphabetic());
774    /// assert!(!space.is_ascii_alphabetic());
775    /// assert!(!lf.is_ascii_alphabetic());
776    /// assert!(!esc.is_ascii_alphabetic());
777    /// ```
778    #[must_use]
779    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
780    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
781    #[inline]
782    pub const fn is_ascii_alphabetic(&self) -> bool {
783        matches!(*self, b'A'..=b'Z' | b'a'..=b'z')
784    }
785
786    /// Checks if the value is an ASCII uppercase character:
787    /// U+0041 'A' ..= U+005A 'Z'.
788    ///
789    /// # Examples
790    ///
791    /// ```
792    /// let uppercase_a = b'A';
793    /// let uppercase_g = b'G';
794    /// let a = b'a';
795    /// let g = b'g';
796    /// let zero = b'0';
797    /// let percent = b'%';
798    /// let space = b' ';
799    /// let lf = b'\n';
800    /// let esc = b'\x1b';
801    ///
802    /// assert!(uppercase_a.is_ascii_uppercase());
803    /// assert!(uppercase_g.is_ascii_uppercase());
804    /// assert!(!a.is_ascii_uppercase());
805    /// assert!(!g.is_ascii_uppercase());
806    /// assert!(!zero.is_ascii_uppercase());
807    /// assert!(!percent.is_ascii_uppercase());
808    /// assert!(!space.is_ascii_uppercase());
809    /// assert!(!lf.is_ascii_uppercase());
810    /// assert!(!esc.is_ascii_uppercase());
811    /// ```
812    #[must_use]
813    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
814    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
815    #[inline]
816    pub const fn is_ascii_uppercase(&self) -> bool {
817        matches!(*self, b'A'..=b'Z')
818    }
819
820    /// Checks if the value is an ASCII lowercase character:
821    /// U+0061 'a' ..= U+007A 'z'.
822    ///
823    /// # Examples
824    ///
825    /// ```
826    /// let uppercase_a = b'A';
827    /// let uppercase_g = b'G';
828    /// let a = b'a';
829    /// let g = b'g';
830    /// let zero = b'0';
831    /// let percent = b'%';
832    /// let space = b' ';
833    /// let lf = b'\n';
834    /// let esc = b'\x1b';
835    ///
836    /// assert!(!uppercase_a.is_ascii_lowercase());
837    /// assert!(!uppercase_g.is_ascii_lowercase());
838    /// assert!(a.is_ascii_lowercase());
839    /// assert!(g.is_ascii_lowercase());
840    /// assert!(!zero.is_ascii_lowercase());
841    /// assert!(!percent.is_ascii_lowercase());
842    /// assert!(!space.is_ascii_lowercase());
843    /// assert!(!lf.is_ascii_lowercase());
844    /// assert!(!esc.is_ascii_lowercase());
845    /// ```
846    #[must_use]
847    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
848    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
849    #[inline]
850    pub const fn is_ascii_lowercase(&self) -> bool {
851        matches!(*self, b'a'..=b'z')
852    }
853
854    /// Checks if the value is an ASCII alphanumeric character:
855    ///
856    /// - U+0041 'A' ..= U+005A 'Z', or
857    /// - U+0061 'a' ..= U+007A 'z', or
858    /// - U+0030 '0' ..= U+0039 '9'.
859    ///
860    /// # Examples
861    ///
862    /// ```
863    /// let uppercase_a = b'A';
864    /// let uppercase_g = b'G';
865    /// let a = b'a';
866    /// let g = b'g';
867    /// let zero = b'0';
868    /// let percent = b'%';
869    /// let space = b' ';
870    /// let lf = b'\n';
871    /// let esc = b'\x1b';
872    ///
873    /// assert!(uppercase_a.is_ascii_alphanumeric());
874    /// assert!(uppercase_g.is_ascii_alphanumeric());
875    /// assert!(a.is_ascii_alphanumeric());
876    /// assert!(g.is_ascii_alphanumeric());
877    /// assert!(zero.is_ascii_alphanumeric());
878    /// assert!(!percent.is_ascii_alphanumeric());
879    /// assert!(!space.is_ascii_alphanumeric());
880    /// assert!(!lf.is_ascii_alphanumeric());
881    /// assert!(!esc.is_ascii_alphanumeric());
882    /// ```
883    #[must_use]
884    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
885    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
886    #[inline]
887    pub const fn is_ascii_alphanumeric(&self) -> bool {
888        matches!(*self, b'0'..=b'9') | matches!(*self, b'A'..=b'Z') | matches!(*self, b'a'..=b'z')
889    }
890
891    /// Checks if the value is an ASCII decimal digit:
892    /// U+0030 '0' ..= U+0039 '9'.
893    ///
894    /// # Examples
895    ///
896    /// ```
897    /// let uppercase_a = b'A';
898    /// let uppercase_g = b'G';
899    /// let a = b'a';
900    /// let g = b'g';
901    /// let zero = b'0';
902    /// let percent = b'%';
903    /// let space = b' ';
904    /// let lf = b'\n';
905    /// let esc = b'\x1b';
906    ///
907    /// assert!(!uppercase_a.is_ascii_digit());
908    /// assert!(!uppercase_g.is_ascii_digit());
909    /// assert!(!a.is_ascii_digit());
910    /// assert!(!g.is_ascii_digit());
911    /// assert!(zero.is_ascii_digit());
912    /// assert!(!percent.is_ascii_digit());
913    /// assert!(!space.is_ascii_digit());
914    /// assert!(!lf.is_ascii_digit());
915    /// assert!(!esc.is_ascii_digit());
916    /// ```
917    #[must_use]
918    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
919    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
920    #[inline]
921    pub const fn is_ascii_digit(&self) -> bool {
922        matches!(*self, b'0'..=b'9')
923    }
924
925    /// Checks if the value is an ASCII octal digit:
926    /// U+0030 '0' ..= U+0037 '7'.
927    ///
928    /// # Examples
929    ///
930    /// ```
931    /// #![feature(is_ascii_octdigit)]
932    ///
933    /// let uppercase_a = b'A';
934    /// let a = b'a';
935    /// let zero = b'0';
936    /// let seven = b'7';
937    /// let nine = b'9';
938    /// let percent = b'%';
939    /// let lf = b'\n';
940    ///
941    /// assert!(!uppercase_a.is_ascii_octdigit());
942    /// assert!(!a.is_ascii_octdigit());
943    /// assert!(zero.is_ascii_octdigit());
944    /// assert!(seven.is_ascii_octdigit());
945    /// assert!(!nine.is_ascii_octdigit());
946    /// assert!(!percent.is_ascii_octdigit());
947    /// assert!(!lf.is_ascii_octdigit());
948    /// ```
949    #[must_use]
950    #[unstable(feature = "is_ascii_octdigit", issue = "101288")]
951    #[inline]
952    pub const fn is_ascii_octdigit(&self) -> bool {
953        matches!(*self, b'0'..=b'7')
954    }
955
956    /// Checks if the value is an ASCII hexadecimal digit:
957    ///
958    /// - U+0030 '0' ..= U+0039 '9', or
959    /// - U+0041 'A' ..= U+0046 'F', or
960    /// - U+0061 'a' ..= U+0066 'f'.
961    ///
962    /// # Examples
963    ///
964    /// ```
965    /// let uppercase_a = b'A';
966    /// let uppercase_g = b'G';
967    /// let a = b'a';
968    /// let g = b'g';
969    /// let zero = b'0';
970    /// let percent = b'%';
971    /// let space = b' ';
972    /// let lf = b'\n';
973    /// let esc = b'\x1b';
974    ///
975    /// assert!(uppercase_a.is_ascii_hexdigit());
976    /// assert!(!uppercase_g.is_ascii_hexdigit());
977    /// assert!(a.is_ascii_hexdigit());
978    /// assert!(!g.is_ascii_hexdigit());
979    /// assert!(zero.is_ascii_hexdigit());
980    /// assert!(!percent.is_ascii_hexdigit());
981    /// assert!(!space.is_ascii_hexdigit());
982    /// assert!(!lf.is_ascii_hexdigit());
983    /// assert!(!esc.is_ascii_hexdigit());
984    /// ```
985    #[must_use]
986    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
987    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
988    #[inline]
989    pub const fn is_ascii_hexdigit(&self) -> bool {
990        matches!(*self, b'0'..=b'9') | matches!(*self, b'A'..=b'F') | matches!(*self, b'a'..=b'f')
991    }
992
993    /// Checks if the value is an ASCII punctuation character:
994    ///
995    /// - U+0021 ..= U+002F `! " # $ % & ' ( ) * + , - . /`, or
996    /// - U+003A ..= U+0040 `: ; < = > ? @`, or
997    /// - U+005B ..= U+0060 `` [ \ ] ^ _ ` ``, or
998    /// - U+007B ..= U+007E `{ | } ~`
999    ///
1000    /// # Examples
1001    ///
1002    /// ```
1003    /// let uppercase_a = b'A';
1004    /// let uppercase_g = b'G';
1005    /// let a = b'a';
1006    /// let g = b'g';
1007    /// let zero = b'0';
1008    /// let percent = b'%';
1009    /// let space = b' ';
1010    /// let lf = b'\n';
1011    /// let esc = b'\x1b';
1012    ///
1013    /// assert!(!uppercase_a.is_ascii_punctuation());
1014    /// assert!(!uppercase_g.is_ascii_punctuation());
1015    /// assert!(!a.is_ascii_punctuation());
1016    /// assert!(!g.is_ascii_punctuation());
1017    /// assert!(!zero.is_ascii_punctuation());
1018    /// assert!(percent.is_ascii_punctuation());
1019    /// assert!(!space.is_ascii_punctuation());
1020    /// assert!(!lf.is_ascii_punctuation());
1021    /// assert!(!esc.is_ascii_punctuation());
1022    /// ```
1023    #[must_use]
1024    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1025    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1026    #[inline]
1027    pub const fn is_ascii_punctuation(&self) -> bool {
1028        matches!(*self, b'!'..=b'/')
1029            | matches!(*self, b':'..=b'@')
1030            | matches!(*self, b'['..=b'`')
1031            | matches!(*self, b'{'..=b'~')
1032    }
1033
1034    /// Checks if the value is an ASCII graphic character:
1035    /// U+0021 '!' ..= U+007E '~'.
1036    ///
1037    /// # Examples
1038    ///
1039    /// ```
1040    /// let uppercase_a = b'A';
1041    /// let uppercase_g = b'G';
1042    /// let a = b'a';
1043    /// let g = b'g';
1044    /// let zero = b'0';
1045    /// let percent = b'%';
1046    /// let space = b' ';
1047    /// let lf = b'\n';
1048    /// let esc = b'\x1b';
1049    ///
1050    /// assert!(uppercase_a.is_ascii_graphic());
1051    /// assert!(uppercase_g.is_ascii_graphic());
1052    /// assert!(a.is_ascii_graphic());
1053    /// assert!(g.is_ascii_graphic());
1054    /// assert!(zero.is_ascii_graphic());
1055    /// assert!(percent.is_ascii_graphic());
1056    /// assert!(!space.is_ascii_graphic());
1057    /// assert!(!lf.is_ascii_graphic());
1058    /// assert!(!esc.is_ascii_graphic());
1059    /// ```
1060    #[must_use]
1061    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1062    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1063    #[inline]
1064    pub const fn is_ascii_graphic(&self) -> bool {
1065        matches!(*self, b'!'..=b'~')
1066    }
1067
1068    /// Checks if the value is an ASCII whitespace character:
1069    /// U+0020 SPACE, U+0009 HORIZONTAL TAB, U+000A LINE FEED,
1070    /// U+000C FORM FEED, or U+000D CARRIAGE RETURN.
1071    ///
1072    /// Rust uses the WhatWG Infra Standard's [definition of ASCII
1073    /// whitespace][infra-aw]. There are several other definitions in
1074    /// wide use. For instance, [the POSIX locale][pct] includes
1075    /// U+000B VERTICAL TAB as well as all the above characters,
1076    /// but—from the very same specification—[the default rule for
1077    /// "field splitting" in the Bourne shell][bfs] considers *only*
1078    /// SPACE, HORIZONTAL TAB, and LINE FEED as whitespace.
1079    ///
1080    /// If you are writing a program that will process an existing
1081    /// file format, check what that format's definition of whitespace is
1082    /// before using this function.
1083    ///
1084    /// [infra-aw]: https://infra.spec.whatwg.org/#ascii-whitespace
1085    /// [pct]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap07.html#tag_07_03_01
1086    /// [bfs]: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05
1087    ///
1088    /// # Examples
1089    ///
1090    /// ```
1091    /// let uppercase_a = b'A';
1092    /// let uppercase_g = b'G';
1093    /// let a = b'a';
1094    /// let g = b'g';
1095    /// let zero = b'0';
1096    /// let percent = b'%';
1097    /// let space = b' ';
1098    /// let lf = b'\n';
1099    /// let esc = b'\x1b';
1100    ///
1101    /// assert!(!uppercase_a.is_ascii_whitespace());
1102    /// assert!(!uppercase_g.is_ascii_whitespace());
1103    /// assert!(!a.is_ascii_whitespace());
1104    /// assert!(!g.is_ascii_whitespace());
1105    /// assert!(!zero.is_ascii_whitespace());
1106    /// assert!(!percent.is_ascii_whitespace());
1107    /// assert!(space.is_ascii_whitespace());
1108    /// assert!(lf.is_ascii_whitespace());
1109    /// assert!(!esc.is_ascii_whitespace());
1110    /// ```
1111    #[must_use]
1112    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1113    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1114    #[inline]
1115    pub const fn is_ascii_whitespace(&self) -> bool {
1116        matches!(*self, b'\t' | b'\n' | b'\x0C' | b'\r' | b' ')
1117    }
1118
1119    /// Checks if the value is an ASCII control character:
1120    /// U+0000 NUL ..= U+001F UNIT SEPARATOR, or U+007F DELETE.
1121    /// Note that most ASCII whitespace characters are control
1122    /// characters, but SPACE is not.
1123    ///
1124    /// # Examples
1125    ///
1126    /// ```
1127    /// let uppercase_a = b'A';
1128    /// let uppercase_g = b'G';
1129    /// let a = b'a';
1130    /// let g = b'g';
1131    /// let zero = b'0';
1132    /// let percent = b'%';
1133    /// let space = b' ';
1134    /// let lf = b'\n';
1135    /// let esc = b'\x1b';
1136    ///
1137    /// assert!(!uppercase_a.is_ascii_control());
1138    /// assert!(!uppercase_g.is_ascii_control());
1139    /// assert!(!a.is_ascii_control());
1140    /// assert!(!g.is_ascii_control());
1141    /// assert!(!zero.is_ascii_control());
1142    /// assert!(!percent.is_ascii_control());
1143    /// assert!(!space.is_ascii_control());
1144    /// assert!(lf.is_ascii_control());
1145    /// assert!(esc.is_ascii_control());
1146    /// ```
1147    #[must_use]
1148    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1149    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1150    #[inline]
1151    pub const fn is_ascii_control(&self) -> bool {
1152        matches!(*self, b'\0'..=b'\x1F' | b'\x7F')
1153    }
1154
1155    /// Returns an iterator that produces an escaped version of a `u8`,
1156    /// treating it as an ASCII character.
1157    ///
1158    /// The behavior is identical to [`ascii::escape_default`].
1159    ///
1160    /// # Examples
1161    ///
1162    /// ```
1163    /// assert_eq!("0", b'0'.escape_ascii().to_string());
1164    /// assert_eq!("\\t", b'\t'.escape_ascii().to_string());
1165    /// assert_eq!("\\r", b'\r'.escape_ascii().to_string());
1166    /// assert_eq!("\\n", b'\n'.escape_ascii().to_string());
1167    /// assert_eq!("\\'", b'\''.escape_ascii().to_string());
1168    /// assert_eq!("\\\"", b'"'.escape_ascii().to_string());
1169    /// assert_eq!("\\\\", b'\\'.escape_ascii().to_string());
1170    /// assert_eq!("\\x9d", b'\x9d'.escape_ascii().to_string());
1171    /// ```
1172    #[must_use = "this returns the escaped byte as an iterator, \
1173                  without modifying the original"]
1174    #[stable(feature = "inherent_ascii_escape", since = "1.60.0")]
1175    #[inline]
1176    pub fn escape_ascii(self) -> ascii::EscapeDefault {
1177        ascii::escape_default(self)
1178    }
1179
1180    #[inline]
1181    pub(crate) const fn is_utf8_char_boundary(self) -> bool {
1182        // This is bit magic equivalent to: b < 128 || b >= 192
1183        (self as i8) >= -0x40
1184    }
1185}
1186
1187impl u16 {
1188    uint_impl! {
1189        Self = u16,
1190        ActualT = u16,
1191        SignedT = i16,
1192        BITS = 16,
1193        BITS_MINUS_ONE = 15,
1194        MAX = 65535,
1195        rot = 4,
1196        rot_op = "0xa003",
1197        rot_result = "0x3a",
1198        fsh_op = "0x2de",
1199        fshl_result = "0x30",
1200        fshr_result = "0x302d",
1201        clmul_lhs = "0x9012",
1202        clmul_rhs = "0xcd34",
1203        clmul_result = "0x928",
1204        swap_op = "0x1234",
1205        swapped = "0x3412",
1206        reversed = "0x2c48",
1207        le_bytes = "[0x34, 0x12]",
1208        be_bytes = "[0x12, 0x34]",
1209        to_xe_bytes_doc = "",
1210        from_xe_bytes_doc = "",
1211        bound_condition = "",
1212    }
1213    midpoint_impl! { u16, u32, unsigned }
1214    widening_carryless_mul_impl! { u16, u32 }
1215    carrying_carryless_mul_impl! { u16, u32 }
1216
1217    /// Checks if the value is a Unicode surrogate code point, which are disallowed values for [`char`].
1218    ///
1219    /// # Examples
1220    ///
1221    /// ```
1222    /// #![feature(utf16_extra)]
1223    ///
1224    /// let low_non_surrogate = 0xA000u16;
1225    /// let low_surrogate = 0xD800u16;
1226    /// let high_surrogate = 0xDC00u16;
1227    /// let high_non_surrogate = 0xE000u16;
1228    ///
1229    /// assert!(!low_non_surrogate.is_utf16_surrogate());
1230    /// assert!(low_surrogate.is_utf16_surrogate());
1231    /// assert!(high_surrogate.is_utf16_surrogate());
1232    /// assert!(!high_non_surrogate.is_utf16_surrogate());
1233    /// ```
1234    #[must_use]
1235    #[unstable(feature = "utf16_extra", issue = "94919")]
1236    #[inline]
1237    pub const fn is_utf16_surrogate(self) -> bool {
1238        matches!(self, 0xD800..=0xDFFF)
1239    }
1240}
1241
1242impl u32 {
1243    uint_impl! {
1244        Self = u32,
1245        ActualT = u32,
1246        SignedT = i32,
1247        BITS = 32,
1248        BITS_MINUS_ONE = 31,
1249        MAX = 4294967295,
1250        rot = 8,
1251        rot_op = "0x10000b3",
1252        rot_result = "0xb301",
1253        fsh_op = "0x2fe78e45",
1254        fshl_result = "0xb32f",
1255        fshr_result = "0xb32fe78e",
1256        clmul_lhs = "0x56789012",
1257        clmul_rhs = "0xf52ecd34",
1258        clmul_result = "0x9b980928",
1259        swap_op = "0x12345678",
1260        swapped = "0x78563412",
1261        reversed = "0x1e6a2c48",
1262        le_bytes = "[0x78, 0x56, 0x34, 0x12]",
1263        be_bytes = "[0x12, 0x34, 0x56, 0x78]",
1264        to_xe_bytes_doc = "",
1265        from_xe_bytes_doc = "",
1266        bound_condition = "",
1267    }
1268    midpoint_impl! { u32, u64, unsigned }
1269    widening_carryless_mul_impl! { u32, u64 }
1270    carrying_carryless_mul_impl! { u32, u64 }
1271}
1272
1273impl u64 {
1274    uint_impl! {
1275        Self = u64,
1276        ActualT = u64,
1277        SignedT = i64,
1278        BITS = 64,
1279        BITS_MINUS_ONE = 63,
1280        MAX = 18446744073709551615,
1281        rot = 12,
1282        rot_op = "0xaa00000000006e1",
1283        rot_result = "0x6e10aa",
1284        fsh_op = "0x2fe78e45983acd98",
1285        fshl_result = "0x6e12fe",
1286        fshr_result = "0x6e12fe78e45983ac",
1287        clmul_lhs = "0x7890123456789012",
1288        clmul_rhs = "0xdd358416f52ecd34",
1289        clmul_result = "0xa6299579b980928",
1290        swap_op = "0x1234567890123456",
1291        swapped = "0x5634129078563412",
1292        reversed = "0x6a2c48091e6a2c48",
1293        le_bytes = "[0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
1294        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]",
1295        to_xe_bytes_doc = "",
1296        from_xe_bytes_doc = "",
1297        bound_condition = "",
1298    }
1299    midpoint_impl! { u64, u128, unsigned }
1300    widening_carryless_mul_impl! { u64, u128 }
1301    carrying_carryless_mul_impl! { u64, u128 }
1302}
1303
1304impl u128 {
1305    uint_impl! {
1306        Self = u128,
1307        ActualT = u128,
1308        SignedT = i128,
1309        BITS = 128,
1310        BITS_MINUS_ONE = 127,
1311        MAX = 340282366920938463463374607431768211455,
1312        rot = 16,
1313        rot_op = "0x13f40000000000000000000000004f76",
1314        rot_result = "0x4f7613f4",
1315        fsh_op = "0x2fe78e45983acd98039000008736273",
1316        fshl_result = "0x4f7602fe",
1317        fshr_result = "0x4f7602fe78e45983acd9803900000873",
1318        clmul_lhs = "0x12345678901234567890123456789012",
1319        clmul_rhs = "0x4317e40ab4ddcf05dd358416f52ecd34",
1320        clmul_result = "0xb9cf660de35d0c170a6299579b980928",
1321        swap_op = "0x12345678901234567890123456789012",
1322        swapped = "0x12907856341290785634129078563412",
1323        reversed = "0x48091e6a2c48091e6a2c48091e6a2c48",
1324        le_bytes = "[0x12, 0x90, 0x78, 0x56, 0x34, 0x12, 0x90, 0x78, \
1325            0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
1326        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56, \
1327            0x78, 0x90, 0x12, 0x34, 0x56, 0x78, 0x90, 0x12]",
1328        to_xe_bytes_doc = "",
1329        from_xe_bytes_doc = "",
1330        bound_condition = "",
1331    }
1332    midpoint_impl! { u128, unsigned }
1333    carrying_carryless_mul_impl! { u128, u256 }
1334}
1335
1336#[cfg(target_pointer_width = "16")]
1337impl usize {
1338    uint_impl! {
1339        Self = usize,
1340        ActualT = u16,
1341        SignedT = isize,
1342        BITS = 16,
1343        BITS_MINUS_ONE = 15,
1344        MAX = 65535,
1345        rot = 4,
1346        rot_op = "0xa003",
1347        rot_result = "0x3a",
1348        fsh_op = "0x2de",
1349        fshl_result = "0x30",
1350        fshr_result = "0x302d",
1351        clmul_lhs = "0x9012",
1352        clmul_rhs = "0xcd34",
1353        clmul_result = "0x928",
1354        swap_op = "0x1234",
1355        swapped = "0x3412",
1356        reversed = "0x2c48",
1357        le_bytes = "[0x34, 0x12]",
1358        be_bytes = "[0x12, 0x34]",
1359        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
1360        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
1361        bound_condition = " on 16-bit targets",
1362    }
1363    midpoint_impl! { usize, u32, unsigned }
1364    carrying_carryless_mul_impl! { usize, u32 }
1365}
1366
1367#[cfg(target_pointer_width = "32")]
1368impl usize {
1369    uint_impl! {
1370        Self = usize,
1371        ActualT = u32,
1372        SignedT = isize,
1373        BITS = 32,
1374        BITS_MINUS_ONE = 31,
1375        MAX = 4294967295,
1376        rot = 8,
1377        rot_op = "0x10000b3",
1378        rot_result = "0xb301",
1379        fsh_op = "0x2fe78e45",
1380        fshl_result = "0xb32f",
1381        fshr_result = "0xb32fe78e",
1382        clmul_lhs = "0x56789012",
1383        clmul_rhs = "0xf52ecd34",
1384        clmul_result = "0x9b980928",
1385        swap_op = "0x12345678",
1386        swapped = "0x78563412",
1387        reversed = "0x1e6a2c48",
1388        le_bytes = "[0x78, 0x56, 0x34, 0x12]",
1389        be_bytes = "[0x12, 0x34, 0x56, 0x78]",
1390        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
1391        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
1392        bound_condition = " on 32-bit targets",
1393    }
1394    midpoint_impl! { usize, u64, unsigned }
1395    carrying_carryless_mul_impl! { usize, u64 }
1396}
1397
1398#[cfg(target_pointer_width = "64")]
1399impl usize {
1400    uint_impl! {
1401        Self = usize,
1402        ActualT = u64,
1403        SignedT = isize,
1404        BITS = 64,
1405        BITS_MINUS_ONE = 63,
1406        MAX = 18446744073709551615,
1407        rot = 12,
1408        rot_op = "0xaa00000000006e1",
1409        rot_result = "0x6e10aa",
1410        fsh_op = "0x2fe78e45983acd98",
1411        fshl_result = "0x6e12fe",
1412        fshr_result = "0x6e12fe78e45983ac",
1413        clmul_lhs = "0x7890123456789012",
1414        clmul_rhs = "0xdd358416f52ecd34",
1415        clmul_result = "0xa6299579b980928",
1416        swap_op = "0x1234567890123456",
1417        swapped = "0x5634129078563412",
1418        reversed = "0x6a2c48091e6a2c48",
1419        le_bytes = "[0x56, 0x34, 0x12, 0x90, 0x78, 0x56, 0x34, 0x12]",
1420        be_bytes = "[0x12, 0x34, 0x56, 0x78, 0x90, 0x12, 0x34, 0x56]",
1421        to_xe_bytes_doc = usize_isize_to_xe_bytes_doc!(),
1422        from_xe_bytes_doc = usize_isize_from_xe_bytes_doc!(),
1423        bound_condition = " on 64-bit targets",
1424    }
1425    midpoint_impl! { usize, u128, unsigned }
1426    carrying_carryless_mul_impl! { usize, u128 }
1427}
1428
1429impl usize {
1430    /// Returns an `usize` where every byte is equal to `x`.
1431    #[inline]
1432    pub(crate) const fn repeat_u8(x: u8) -> usize {
1433        usize::from_ne_bytes([x; size_of::<usize>()])
1434    }
1435
1436    /// Returns an `usize` where every byte pair is equal to `x`.
1437    #[inline]
1438    pub(crate) const fn repeat_u16(x: u16) -> usize {
1439        let mut r = 0usize;
1440        let mut i = 0;
1441        while i < size_of::<usize>() {
1442            // Use `wrapping_shl` to make it work on targets with 16-bit `usize`
1443            r = r.wrapping_shl(16) | (x as usize);
1444            i += 2;
1445        }
1446        r
1447    }
1448}
1449
1450/// A classification of floating point numbers.
1451///
1452/// This `enum` is used as the return type for [`f32::classify`] and [`f64::classify`]. See
1453/// their documentation for more.
1454///
1455/// # Examples
1456///
1457/// ```
1458/// use std::num::FpCategory;
1459///
1460/// let num = 12.4_f32;
1461/// let inf = f32::INFINITY;
1462/// let zero = 0f32;
1463/// let sub: f32 = 1.1754942e-38;
1464/// let nan = f32::NAN;
1465///
1466/// assert_eq!(num.classify(), FpCategory::Normal);
1467/// assert_eq!(inf.classify(), FpCategory::Infinite);
1468/// assert_eq!(zero.classify(), FpCategory::Zero);
1469/// assert_eq!(sub.classify(), FpCategory::Subnormal);
1470/// assert_eq!(nan.classify(), FpCategory::Nan);
1471/// ```
1472#[derive(Copy, Clone, PartialEq, Eq, Debug)]
1473#[stable(feature = "rust1", since = "1.0.0")]
1474pub enum FpCategory {
1475    /// NaN (not a number): this value results from calculations like `(-1.0).sqrt()`.
1476    ///
1477    /// See [the documentation for `f32`](f32) for more information on the unusual properties
1478    /// of NaN.
1479    #[stable(feature = "rust1", since = "1.0.0")]
1480    Nan,
1481
1482    /// Positive or negative infinity, which often results from dividing a nonzero number
1483    /// by zero.
1484    #[stable(feature = "rust1", since = "1.0.0")]
1485    Infinite,
1486
1487    /// Positive or negative zero.
1488    ///
1489    /// See [the documentation for `f32`](f32) for more information on the signedness of zeroes.
1490    #[stable(feature = "rust1", since = "1.0.0")]
1491    Zero,
1492
1493    /// “Subnormal” or “denormal” floating point representation (less precise, relative to
1494    /// their magnitude, than [`Normal`]).
1495    ///
1496    /// Subnormal numbers are larger in magnitude than [`Zero`] but smaller in magnitude than all
1497    /// [`Normal`] numbers.
1498    ///
1499    /// [`Normal`]: Self::Normal
1500    /// [`Zero`]: Self::Zero
1501    #[stable(feature = "rust1", since = "1.0.0")]
1502    Subnormal,
1503
1504    /// A regular floating point number, not any of the exceptional categories.
1505    ///
1506    /// The smallest positive normal numbers are [`f32::MIN_POSITIVE`] and [`f64::MIN_POSITIVE`],
1507    /// and the largest positive normal numbers are [`f32::MAX`] and [`f64::MAX`]. (Unlike signed
1508    /// integers, floating point numbers are symmetric in their range, so negating any of these
1509    /// constants will produce their negative counterpart.)
1510    #[stable(feature = "rust1", since = "1.0.0")]
1511    Normal,
1512}
1513
1514/// Determines if a string of text of that length of that radix could be guaranteed to be
1515/// stored in the given type T.
1516/// Note that if the radix is known to the compiler, it is just the check of digits.len that
1517/// is done at runtime.
1518#[doc(hidden)]
1519#[inline(always)]
1520#[unstable(issue = "none", feature = "std_internals")]
1521pub const fn can_not_overflow<T>(radix: u32, is_signed_ty: bool, digits: &[u8]) -> bool {
1522    radix <= 16 && digits.len() <= size_of::<T>() * 2 - is_signed_ty as usize
1523}
1524
1525#[cfg_attr(not(panic = "immediate-abort"), inline(never))]
1526#[cfg_attr(panic = "immediate-abort", inline)]
1527#[cold]
1528#[track_caller]
1529const fn from_ascii_radix_panic(radix: u32) -> ! {
1530    const_panic!(
1531        "from_ascii_radix: radix must lie in the range `[2, 36]`",
1532        "from_ascii_radix: radix must lie in the range `[2, 36]` - found {radix}",
1533        radix: u32 = radix,
1534    )
1535}
1536
1537macro_rules! from_str_int_impl {
1538    ($signedness:ident $($int_ty:ty)+) => {$(
1539        #[stable(feature = "rust1", since = "1.0.0")]
1540        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1541        impl const FromStr for $int_ty {
1542            type Err = ParseIntError;
1543
1544            /// Parses an integer from a string slice with decimal digits.
1545            ///
1546            /// The characters are expected to be an optional
1547            #[doc = sign_dependent_expr!{
1548                $signedness ?
1549                if signed {
1550                    " `+` or `-` "
1551                }
1552                if unsigned {
1553                    " `+` "
1554                }
1555            }]
1556            /// sign followed by only digits. Leading and trailing non-digit characters (including
1557            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1558            /// also represent an error.
1559            ///
1560            /// # See also
1561            /// For parsing numbers in other bases, such as binary or hexadecimal,
1562            /// see [`from_str_radix`][Self::from_str_radix].
1563            ///
1564            /// # Examples
1565            ///
1566            /// ```
1567            /// use std::str::FromStr;
1568            ///
1569            #[doc = concat!("assert_eq!(", stringify!($int_ty), "::from_str(\"+10\"), Ok(10));")]
1570            /// ```
1571            /// Trailing space returns error:
1572            /// ```
1573            /// # use std::str::FromStr;
1574            /// #
1575            #[doc = concat!("assert!(", stringify!($int_ty), "::from_str(\"1 \").is_err());")]
1576            /// ```
1577            #[inline]
1578            fn from_str(src: &str) -> Result<$int_ty, ParseIntError> {
1579                <$int_ty>::from_str_radix(src, 10)
1580            }
1581        }
1582
1583        impl $int_ty {
1584            /// Parses an integer from a string slice with digits in a given base.
1585            ///
1586            /// The string is expected to be an optional
1587            #[doc = sign_dependent_expr!{
1588                $signedness ?
1589                if signed {
1590                    " `+` or `-` "
1591                }
1592                if unsigned {
1593                    " `+` "
1594                }
1595            }]
1596            /// sign followed by only digits. Leading and trailing non-digit characters (including
1597            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1598            /// also represent an error.
1599            ///
1600            /// Digits are a subset of these characters, depending on `radix`:
1601            /// * `0-9`
1602            /// * `a-z`
1603            /// * `A-Z`
1604            ///
1605            /// # Panics
1606            ///
1607            /// This function panics if `radix` is not in the range from 2 to 36.
1608            ///
1609            /// # See also
1610            /// If the string to be parsed is in base 10 (decimal),
1611            /// [`from_str`] or [`str::parse`] can also be used.
1612            ///
1613            // FIXME(#122566): These HTML links work around a rustdoc-json test failure.
1614            /// [`from_str`]: #method.from_str
1615            /// [`str::parse`]: primitive.str.html#method.parse
1616            ///
1617            /// # Examples
1618            ///
1619            /// ```
1620            #[doc = concat!("assert_eq!(", stringify!($int_ty), "::from_str_radix(\"A\", 16), Ok(10));")]
1621            /// ```
1622            /// Trailing space returns error:
1623            /// ```
1624            #[doc = concat!("assert!(", stringify!($int_ty), "::from_str_radix(\"1 \", 10).is_err());")]
1625            /// ```
1626            #[stable(feature = "rust1", since = "1.0.0")]
1627            #[rustc_const_stable(feature = "const_int_from_str", since = "1.82.0")]
1628            #[inline]
1629            pub const fn from_str_radix(src: &str, radix: u32) -> Result<$int_ty, ParseIntError> {
1630                <$int_ty>::from_ascii_radix(src.as_bytes(), radix)
1631            }
1632
1633            /// Parses an integer from an ASCII-byte slice with decimal digits.
1634            ///
1635            /// The characters are expected to be an optional
1636            #[doc = sign_dependent_expr!{
1637                $signedness ?
1638                if signed {
1639                    " `+` or `-` "
1640                }
1641                if unsigned {
1642                    " `+` "
1643                }
1644            }]
1645            /// sign followed by only digits. Leading and trailing non-digit characters (including
1646            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1647            /// also represent an error.
1648            ///
1649            /// # Examples
1650            ///
1651            /// ```
1652            /// #![feature(int_from_ascii)]
1653            ///
1654            #[doc = concat!("assert_eq!(", stringify!($int_ty), "::from_ascii(b\"+10\"), Ok(10));")]
1655            /// ```
1656            /// Trailing space returns error:
1657            /// ```
1658            /// # #![feature(int_from_ascii)]
1659            /// #
1660            #[doc = concat!("assert!(", stringify!($int_ty), "::from_ascii(b\"1 \").is_err());")]
1661            /// ```
1662            #[unstable(feature = "int_from_ascii", issue = "134821")]
1663            #[inline]
1664            pub const fn from_ascii(src: &[u8]) -> Result<$int_ty, ParseIntError> {
1665                <$int_ty>::from_ascii_radix(src, 10)
1666            }
1667
1668            /// Parses an integer from an ASCII-byte slice with digits in a given base.
1669            ///
1670            /// The characters are expected to be an optional
1671            #[doc = sign_dependent_expr!{
1672                $signedness ?
1673                if signed {
1674                    " `+` or `-` "
1675                }
1676                if unsigned {
1677                    " `+` "
1678                }
1679            }]
1680            /// sign followed by only digits. Leading and trailing non-digit characters (including
1681            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1682            /// also represent an error.
1683            ///
1684            /// Digits are a subset of these characters, depending on `radix`:
1685            /// * `0-9`
1686            /// * `a-z`
1687            /// * `A-Z`
1688            ///
1689            /// # Panics
1690            ///
1691            /// This function panics if `radix` is not in the range from 2 to 36.
1692            ///
1693            /// # Examples
1694            ///
1695            /// ```
1696            /// #![feature(int_from_ascii)]
1697            ///
1698            #[doc = concat!("assert_eq!(", stringify!($int_ty), "::from_ascii_radix(b\"A\", 16), Ok(10));")]
1699            /// ```
1700            /// Trailing space returns error:
1701            /// ```
1702            /// # #![feature(int_from_ascii)]
1703            /// #
1704            #[doc = concat!("assert!(", stringify!($int_ty), "::from_ascii_radix(b\"1 \", 10).is_err());")]
1705            /// ```
1706            #[unstable(feature = "int_from_ascii", issue = "134821")]
1707            #[inline]
1708            pub const fn from_ascii_radix(src: &[u8], radix: u32) -> Result<$int_ty, ParseIntError> {
1709                use self::IntErrorKind::*;
1710                use self::ParseIntError as PIE;
1711
1712                if 2 > radix || radix > 36 {
1713                    from_ascii_radix_panic(radix);
1714                }
1715
1716                if src.is_empty() {
1717                    return Err(PIE { kind: Empty });
1718                }
1719
1720                #[allow(unused_comparisons)]
1721                let is_signed_ty = 0 > <$int_ty>::MIN;
1722
1723                let (is_positive, mut digits) = match src {
1724                    [b'+' | b'-'] => {
1725                        return Err(PIE { kind: InvalidDigit });
1726                    }
1727                    [b'+', rest @ ..] => (true, rest),
1728                    [b'-', rest @ ..] if is_signed_ty => (false, rest),
1729                    _ => (true, src),
1730                };
1731
1732                let mut result = 0;
1733
1734                macro_rules! unwrap_or_PIE {
1735                    ($option:expr, $kind:ident) => {
1736                        match $option {
1737                            Some(value) => value,
1738                            None => return Err(PIE { kind: $kind }),
1739                        }
1740                    };
1741                }
1742
1743                if can_not_overflow::<$int_ty>(radix, is_signed_ty, digits) {
1744                    // If the len of the str is short compared to the range of the type
1745                    // we are parsing into, then we can be certain that an overflow will not occur.
1746                    // This bound is when `radix.pow(digits.len()) - 1 <= T::MAX` but the condition
1747                    // above is a faster (conservative) approximation of this.
1748                    //
1749                    // Consider radix 16 as it has the highest information density per digit and will thus overflow the earliest:
1750                    // `u8::MAX` is `ff` - any str of len 2 is guaranteed to not overflow.
1751                    // `i8::MAX` is `7f` - only a str of len 1 is guaranteed to not overflow.
1752                    macro_rules! run_unchecked_loop {
1753                        ($unchecked_additive_op:tt) => {{
1754                            while let [c, rest @ ..] = digits {
1755                                result = result * (radix as $int_ty);
1756                                let x = unwrap_or_PIE!((*c as char).to_digit(radix), InvalidDigit);
1757                                result = result $unchecked_additive_op (x as $int_ty);
1758                                digits = rest;
1759                            }
1760                        }};
1761                    }
1762                    if is_positive {
1763                        run_unchecked_loop!(+)
1764                    } else {
1765                        run_unchecked_loop!(-)
1766                    };
1767                } else {
1768                    macro_rules! run_checked_loop {
1769                        ($checked_additive_op:ident, $overflow_err:ident) => {{
1770                            while let [c, rest @ ..] = digits {
1771                                // When `radix` is passed in as a literal, rather than doing a slow `imul`
1772                                // the compiler can use shifts if `radix` can be expressed as a
1773                                // sum of powers of 2 (x*10 can be written as x*8 + x*2).
1774                                // When the compiler can't use these optimisations,
1775                                // the latency of the multiplication can be hidden by issuing it
1776                                // before the result is needed to improve performance on
1777                                // modern out-of-order CPU as multiplication here is slower
1778                                // than the other instructions, we can get the end result faster
1779                                // doing multiplication first and let the CPU spends other cycles
1780                                // doing other computation and get multiplication result later.
1781                                let mul = result.checked_mul(radix as $int_ty);
1782                                let x = unwrap_or_PIE!((*c as char).to_digit(radix), InvalidDigit) as $int_ty;
1783                                result = unwrap_or_PIE!(mul, $overflow_err);
1784                                result = unwrap_or_PIE!(<$int_ty>::$checked_additive_op(result, x), $overflow_err);
1785                                digits = rest;
1786                            }
1787                        }};
1788                    }
1789                    if is_positive {
1790                        run_checked_loop!(checked_add, PosOverflow)
1791                    } else {
1792                        run_checked_loop!(checked_sub, NegOverflow)
1793                    };
1794                }
1795                Ok(result)
1796            }
1797        }
1798    )*}
1799}
1800
1801from_str_int_impl! { signed isize i8 i16 i32 i64 i128 }
1802from_str_int_impl! { unsigned usize u8 u16 u32 u64 u128 }
````