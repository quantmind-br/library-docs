---
title: num.rs - source
url: https://doc.rust-lang.org/src/core/convert/num.rs.html#377
source: crawler
fetched_at: 2026-05-06T21:30:37.816569525-03:00
rendered_js: false
word_count: 3047
summary: This document defines conversion traits and implementations for Rust numeric types, providing mechanisms for safe, lossless integer and boolean conversions and unsafe float-to-integer casts.
tags:
    - rust
    - type-conversion
    - numeric-types
    - traits
    - macros
    - lossless-conversion
category: reference
---

## core/convert/ num.rs

````rust
1use crate::num::TryFromIntError;
2
3mod private {
4    /// This trait being unreachable from outside the crate
5    /// prevents other implementations of the `FloatToInt` trait,
6    /// which allows potentially adding more trait methods after the trait is `#[stable]`.
7    #[unstable(feature = "convert_float_to_int", issue = "67057")]
8    pub trait Sealed {}
9}
10
11/// Supporting trait for inherent methods of `f32` and `f64` such as `to_int_unchecked`.
12/// Typically doesn’t need to be used directly.
13#[unstable(feature = "convert_float_to_int", issue = "67057")]
14pub trait FloatToInt<Int>: private::Sealed + Sized {
15    #[unstable(feature = "convert_float_to_int", issue = "67057")]
16    #[doc(hidden)]
17    unsafe fn to_int_unchecked(self) -> Int;
18}
19
20macro_rules! impl_float_to_int {
21    ($Float:ty => $($Int:ty),+) => {
22        #[unstable(feature = "convert_float_to_int", issue = "67057")]
23        impl private::Sealed for $Float {}
24        $(
25            #[unstable(feature = "convert_float_to_int", issue = "67057")]
26            impl FloatToInt<$Int> for $Float {
27                #[inline]
28                unsafe fn to_int_unchecked(self) -> $Int {
29                    // SAFETY: the safety contract must be upheld by the caller.
30                    unsafe { crate::intrinsics::float_to_int_unchecked(self) }
31                }
32            }
33        )+
34    }
35}
36
37impl_float_to_int!(f16 => u8, u16, u32, u64, u128, usize, i8, i16, i32, i64, i128, isize);
38impl_float_to_int!(f32 => u8, u16, u32, u64, u128, usize, i8, i16, i32, i64, i128, isize);
39impl_float_to_int!(f64 => u8, u16, u32, u64, u128, usize, i8, i16, i32, i64, i128, isize);
40impl_float_to_int!(f128 => u8, u16, u32, u64, u128, usize, i8, i16, i32, i64, i128, isize);
41
42/// Implement `From<bool>` for integers
43macro_rules! impl_from_bool {
44    ($($int:ty)*) => {$(
45        #[stable(feature = "from_bool", since = "1.28.0")]
46        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
47        impl const From<bool> for $int {
48            /// Converts from [`bool`] to
49            #[doc = concat!("[`", stringify!($int), "`]")]
50            /// , by turning `false` into `0` and `true` into `1`.
51            ///
52            /// # Examples
53            ///
54            /// ```
55            #[doc = concat!("assert_eq!(", stringify!($int), "::from(false), 0);")]
56            ///
57            #[doc = concat!("assert_eq!(", stringify!($int), "::from(true), 1);")]
58            /// ```
59            #[inline(always)]
60            fn from(b: bool) -> Self {
61                b as Self
62            }
63        }
64    )*}
65}
66
67// boolean -> integer
68impl_from_bool!(u8 u16 u32 u64 u128 usize);
69impl_from_bool!(i8 i16 i32 i64 i128 isize);
70
71/// Implement `From<$small>` for `$large`
72macro_rules! impl_from {
73    ($small:ty => $large:ty, #[$attr:meta]) => {
74        #[$attr]
75        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
76        impl const From<$small> for $large {
77            #[doc = concat!("Converts from [`", stringify!($small), "`] to [`", stringify!($large), "`] losslessly.")]
78            #[inline(always)]
79            fn from(small: $small) -> Self {
80                debug_assert!(<$large>::MIN as i128 <= <$small>::MIN as i128);
81                debug_assert!(<$small>::MAX as u128 <= <$large>::MAX as u128);
82                small as Self
83            }
84        }
85    }
86}
87
88// unsigned integer -> unsigned integer
89impl_from!(u8 => u16, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
90impl_from!(u8 => u32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
91impl_from!(u8 => u64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
92impl_from!(u8 => u128, #[stable(feature = "i128", since = "1.26.0")]);
93impl_from!(u8 => usize, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
94impl_from!(u16 => u32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
95impl_from!(u16 => u64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
96impl_from!(u16 => u128, #[stable(feature = "i128", since = "1.26.0")]);
97impl_from!(u32 => u64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
98impl_from!(u32 => u128, #[stable(feature = "i128", since = "1.26.0")]);
99impl_from!(u64 => u128, #[stable(feature = "i128", since = "1.26.0")]);
100
101// signed integer -> signed integer
102impl_from!(i8 => i16, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
103impl_from!(i8 => i32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
104impl_from!(i8 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
105impl_from!(i8 => i128, #[stable(feature = "i128", since = "1.26.0")]);
106impl_from!(i8 => isize, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
107impl_from!(i16 => i32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
108impl_from!(i16 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
109impl_from!(i16 => i128, #[stable(feature = "i128", since = "1.26.0")]);
110impl_from!(i32 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
111impl_from!(i32 => i128, #[stable(feature = "i128", since = "1.26.0")]);
112impl_from!(i64 => i128, #[stable(feature = "i128", since = "1.26.0")]);
113
114// unsigned integer -> signed integer
115impl_from!(u8 => i16, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
116impl_from!(u8 => i32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
117impl_from!(u8 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
118impl_from!(u8 => i128, #[stable(feature = "i128", since = "1.26.0")]);
119impl_from!(u16 => i32, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
120impl_from!(u16 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
121impl_from!(u16 => i128, #[stable(feature = "i128", since = "1.26.0")]);
122impl_from!(u32 => i64, #[stable(feature = "lossless_int_conv", since = "1.5.0")]);
123impl_from!(u32 => i128, #[stable(feature = "i128", since = "1.26.0")]);
124impl_from!(u64 => i128, #[stable(feature = "i128", since = "1.26.0")]);
125
126// The C99 standard defines bounds on INTPTR_MIN, INTPTR_MAX, and UINTPTR_MAX
127// which imply that pointer-sized integers must be at least 16 bits:
128// https://port70.net/~nsz/c/c99/n1256.html#7.18.2.4
129impl_from!(u16 => usize, #[stable(feature = "lossless_iusize_conv", since = "1.26.0")]);
130impl_from!(u8 => isize, #[stable(feature = "lossless_iusize_conv", since = "1.26.0")]);
131impl_from!(i16 => isize, #[stable(feature = "lossless_iusize_conv", since = "1.26.0")]);
132
133// RISC-V defines the possibility of a 128-bit address space (RV128).
134
135// CHERI proposes 128-bit “capabilities”. Unclear if this would be relevant to usize/isize.
136// https://www.cl.cam.ac.uk/research/security/ctsrd/pdfs/20171017a-cheri-poster.pdf
137// https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-951.pdf
138
139// Note: integers can only be represented with full precision in a float if
140// they fit in the significand, which is:
141// * 11 bits in f16
142// * 24 bits in f32
143// * 53 bits in f64
144// * 113 bits in f128
145// Lossy float conversions are not implemented at this time.
146// FIXME(f16,f128): The `f16`/`f128` impls `#[stable]` attributes should be changed to reference
147// `f16`/`f128` when they are stabilised (trait impls have to have a `#[stable]` attribute, but none
148// of the `f16`/`f128` impls can be used on stable as the `f16` and `f128` types are unstable).
149
150// signed integer -> float
151impl_from!(i8 => f16, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
152impl_from!(i8 => f32, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
153impl_from!(i8 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
154impl_from!(i8 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
155impl_from!(i16 => f32, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
156impl_from!(i16 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
157impl_from!(i16 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
158impl_from!(i32 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
159impl_from!(i32 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
160// FIXME(f128): This impl would allow using `f128` on stable before it is stabilised.
161// impl_from!(i64 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
162
163// unsigned integer -> float
164impl_from!(u8 => f16, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
165impl_from!(u8 => f32, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
166impl_from!(u8 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
167impl_from!(u8 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
168impl_from!(u16 => f32, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
169impl_from!(u16 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
170impl_from!(u16 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
171impl_from!(u32 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
172impl_from!(u32 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
173// FIXME(f128): This impl would allow using `f128` on stable before it is stabilised.
174// impl_from!(u64 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
175
176// float -> float
177// FIXME(f16,f128): adding additional `From<{float}>` impls to `f32` breaks inference. See
178// <https://github.com/rust-lang/rust/issues/123831>
179impl_from!(f16 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
180impl_from!(f16 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
181impl_from!(f32 => f64, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
182impl_from!(f32 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
183impl_from!(f64 => f128, #[stable(feature = "lossless_float_conv", since = "1.6.0")]);
184
185macro_rules! impl_float_from_bool {
186    (
187        $float:ty $(;
188            doctest_prefix: $(#[doc = $doctest_prefix:literal])*
189            doctest_suffix: $(#[doc = $doctest_suffix:literal])*
190        )?
191    ) => {
192        #[stable(feature = "float_from_bool", since = "1.68.0")]
193        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
194            impl const From<bool> for $float {
195            #[doc = concat!("Converts a [`bool`] to [`", stringify!($float),"`] losslessly.")]
196            /// The resulting value is positive `0.0` for `false` and `1.0` for `true` values.
197            ///
198            /// # Examples
199            /// ```
200            $($(#[doc = $doctest_prefix])*)?
201            #[doc = concat!("let x: ", stringify!($float)," = false.into();")]
202            /// assert_eq!(x, 0.0);
203            /// assert!(x.is_sign_positive());
204            ///
205            #[doc = concat!("let y: ", stringify!($float)," = true.into();")]
206            /// assert_eq!(y, 1.0);
207            $($(#[doc = $doctest_suffix])*)?
208            /// ```
209            #[inline]
210            fn from(small: bool) -> Self {
211                small as u8 as Self
212            }
213        }
214    };
215}
216
217// boolean -> float
218impl_float_from_bool!(
219    f16;
220    doctest_prefix:
221    // rustdoc doesn't remove the conventional space after the `///`
222    ///# #![allow(unused_features)]
223    ///#![feature(f16)]
224    ///# #[cfg(all(target_arch = "x86_64", target_os = "linux"))] {
225    ///
226    doctest_suffix:
227    ///# }
228);
229impl_float_from_bool!(f32);
230impl_float_from_bool!(f64);
231impl_float_from_bool!(
232    f128;
233    doctest_prefix:
234    ///# #![allow(unused_features)]
235    ///#![feature(f128)]
236    ///# #[cfg(all(target_arch = "x86_64", target_os = "linux"))] {
237    ///
238    doctest_suffix:
239    ///# }
240);
241
242// no possible bounds violation
243macro_rules! impl_try_from_unbounded {
244    ($source:ty => $($target:ty),+) => {$(
245        #[stable(feature = "try_from", since = "1.34.0")]
246        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
247        impl const TryFrom<$source> for $target {
248            type Error = TryFromIntError;
249
250            /// Tries to create the target number type from a source
251            /// number type. This returns an error if the source value
252            /// is outside of the range of the target type.
253            #[inline]
254            fn try_from(value: $source) -> Result<Self, Self::Error> {
255                Ok(value as Self)
256            }
257        }
258    )*}
259}
260
261// only negative bounds
262macro_rules! impl_try_from_lower_bounded {
263    ($source:ty => $($target:ty),+) => {$(
264        #[stable(feature = "try_from", since = "1.34.0")]
265        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
266        impl const TryFrom<$source> for $target {
267            type Error = TryFromIntError;
268
269            /// Tries to create the target number type from a source
270            /// number type. This returns an error if the source value
271            /// is outside of the range of the target type.
272            #[inline]
273            fn try_from(u: $source) -> Result<Self, Self::Error> {
274                if u >= 0 {
275                    Ok(u as Self)
276                } else {
277                    Err(TryFromIntError(()))
278                }
279            }
280        }
281    )*}
282}
283
284// unsigned to signed (only positive bound)
285macro_rules! impl_try_from_upper_bounded {
286    ($source:ty => $($target:ty),+) => {$(
287        #[stable(feature = "try_from", since = "1.34.0")]
288        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
289        impl const TryFrom<$source> for $target {
290            type Error = TryFromIntError;
291
292            /// Tries to create the target number type from a source
293            /// number type. This returns an error if the source value
294            /// is outside of the range of the target type.
295            #[inline]
296            fn try_from(u: $source) -> Result<Self, Self::Error> {
297                if u > (Self::MAX as $source) {
298                    Err(TryFromIntError(()))
299                } else {
300                    Ok(u as Self)
301                }
302            }
303        }
304    )*}
305}
306
307// all other cases
308macro_rules! impl_try_from_both_bounded {
309    ($source:ty => $($target:ty),+) => {$(
310        #[stable(feature = "try_from", since = "1.34.0")]
311        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
312        impl const TryFrom<$source> for $target {
313            type Error = TryFromIntError;
314
315            /// Tries to create the target number type from a source
316            /// number type. This returns an error if the source value
317            /// is outside of the range of the target type.
318            #[inline]
319            fn try_from(u: $source) -> Result<Self, Self::Error> {
320                let min = Self::MIN as $source;
321                let max = Self::MAX as $source;
322                if u < min || u > max {
323                    Err(TryFromIntError(()))
324                } else {
325                    Ok(u as Self)
326                }
327            }
328        }
329    )*}
330}
331
332/// Implement `TryFrom<integer>` for `bool`
333macro_rules! impl_try_from_integer_for_bool {
334    ($($int:ty)+) => {$(
335        #[stable(feature = "bool_try_from_int", since = "1.95.0")]
336        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
337        impl const TryFrom<$int> for bool {
338            type Error = TryFromIntError;
339
340            /// Tries to create a bool from an integer type.
341            /// Returns an error if the integer is not 0 or 1.
342            ///
343            /// # Examples
344            ///
345            /// ```
346            #[doc = concat!("assert_eq!(0_", stringify!($int), ".try_into(), Ok(false));")]
347            ///
348            #[doc = concat!("assert_eq!(1_", stringify!($int), ".try_into(), Ok(true));")]
349            ///
350            #[doc = concat!("assert!(<", stringify!($int), " as TryInto<bool>>::try_into(2).is_err());")]
351            /// ```
352            #[inline]
353            fn try_from(i: $int) -> Result<Self, Self::Error> {
354                match i {
355                    0 => Ok(false),
356                    1 => Ok(true),
357                    _ => Err(TryFromIntError(())),
358                }
359            }
360        }
361    )*}
362}
363
364macro_rules! rev {
365    ($mac:ident, $source:ty => $($target:ty),+) => {$(
366        $mac!($target => $source);
367    )*}
368}
369
370// integer -> bool
371impl_try_from_integer_for_bool!(u128 u64 u32 u16 u8);
372impl_try_from_integer_for_bool!(i128 i64 i32 i16 i8);
373
374// unsigned integer -> unsigned integer
375impl_try_from_upper_bounded!(u16 => u8);
376impl_try_from_upper_bounded!(u32 => u8, u16);
377impl_try_from_upper_bounded!(u64 => u8, u16, u32);
378impl_try_from_upper_bounded!(u128 => u8, u16, u32, u64);
379
380// signed integer -> signed integer
381impl_try_from_both_bounded!(i16 => i8);
382impl_try_from_both_bounded!(i32 => i8, i16);
383impl_try_from_both_bounded!(i64 => i8, i16, i32);
384impl_try_from_both_bounded!(i128 => i8, i16, i32, i64);
385
386// unsigned integer -> signed integer
387impl_try_from_upper_bounded!(u8 => i8);
388impl_try_from_upper_bounded!(u16 => i8, i16);
389impl_try_from_upper_bounded!(u32 => i8, i16, i32);
390impl_try_from_upper_bounded!(u64 => i8, i16, i32, i64);
391impl_try_from_upper_bounded!(u128 => i8, i16, i32, i64, i128);
392
393// signed integer -> unsigned integer
394impl_try_from_lower_bounded!(i8 => u8, u16, u32, u64, u128);
395impl_try_from_both_bounded!(i16 => u8);
396impl_try_from_lower_bounded!(i16 => u16, u32, u64, u128);
397impl_try_from_both_bounded!(i32 => u8, u16);
398impl_try_from_lower_bounded!(i32 => u32, u64, u128);
399impl_try_from_both_bounded!(i64 => u8, u16, u32);
400impl_try_from_lower_bounded!(i64 => u64, u128);
401impl_try_from_both_bounded!(i128 => u8, u16, u32, u64);
402impl_try_from_lower_bounded!(i128 => u128);
403
404// usize/isize
405impl_try_from_upper_bounded!(usize => isize);
406impl_try_from_lower_bounded!(isize => usize);
407
408#[cfg(target_pointer_width = "16")]
409mod ptr_try_from_impls {
410    use super::TryFromIntError;
411
412    impl_try_from_upper_bounded!(usize => u8);
413    impl_try_from_unbounded!(usize => u16, u32, u64, u128);
414    impl_try_from_upper_bounded!(usize => i8, i16);
415    impl_try_from_unbounded!(usize => i32, i64, i128);
416
417    impl_try_from_both_bounded!(isize => u8);
418    impl_try_from_lower_bounded!(isize => u16, u32, u64, u128);
419    impl_try_from_both_bounded!(isize => i8);
420    impl_try_from_unbounded!(isize => i16, i32, i64, i128);
421
422    rev!(impl_try_from_upper_bounded, usize => u32, u64, u128);
423    rev!(impl_try_from_lower_bounded, usize => i8, i16);
424    rev!(impl_try_from_both_bounded, usize => i32, i64, i128);
425
426    rev!(impl_try_from_upper_bounded, isize => u16, u32, u64, u128);
427    rev!(impl_try_from_both_bounded, isize => i32, i64, i128);
428}
429
430#[cfg(target_pointer_width = "32")]
431mod ptr_try_from_impls {
432    use super::TryFromIntError;
433
434    impl_try_from_upper_bounded!(usize => u8, u16);
435    impl_try_from_unbounded!(usize => u32, u64, u128);
436    impl_try_from_upper_bounded!(usize => i8, i16, i32);
437    impl_try_from_unbounded!(usize => i64, i128);
438
439    impl_try_from_both_bounded!(isize => u8, u16);
440    impl_try_from_lower_bounded!(isize => u32, u64, u128);
441    impl_try_from_both_bounded!(isize => i8, i16);
442    impl_try_from_unbounded!(isize => i32, i64, i128);
443
444    rev!(impl_try_from_unbounded, usize => u32);
445    rev!(impl_try_from_upper_bounded, usize => u64, u128);
446    rev!(impl_try_from_lower_bounded, usize => i8, i16, i32);
447    rev!(impl_try_from_both_bounded, usize => i64, i128);
448
449    rev!(impl_try_from_unbounded, isize => u16);
450    rev!(impl_try_from_upper_bounded, isize => u32, u64, u128);
451    rev!(impl_try_from_unbounded, isize => i32);
452    rev!(impl_try_from_both_bounded, isize => i64, i128);
453}
454
455#[cfg(target_pointer_width = "64")]
456mod ptr_try_from_impls {
457    use super::TryFromIntError;
458
459    impl_try_from_upper_bounded!(usize => u8, u16, u32);
460    impl_try_from_unbounded!(usize => u64, u128);
461    impl_try_from_upper_bounded!(usize => i8, i16, i32, i64);
462    impl_try_from_unbounded!(usize => i128);
463
464    impl_try_from_both_bounded!(isize => u8, u16, u32);
465    impl_try_from_lower_bounded!(isize => u64, u128);
466    impl_try_from_both_bounded!(isize => i8, i16, i32);
467    impl_try_from_unbounded!(isize => i64, i128);
468
469    rev!(impl_try_from_unbounded, usize => u32, u64);
470    rev!(impl_try_from_upper_bounded, usize => u128);
471    rev!(impl_try_from_lower_bounded, usize => i8, i16, i32, i64);
472    rev!(impl_try_from_both_bounded, usize => i128);
473
474    rev!(impl_try_from_unbounded, isize => u16, u32);
475    rev!(impl_try_from_upper_bounded, isize => u64, u128);
476    rev!(impl_try_from_unbounded, isize => i32, i64);
477    rev!(impl_try_from_both_bounded, isize => i128);
478}
479
480// Conversion traits for non-zero integer types
481use crate::num::NonZero;
482
483macro_rules! impl_nonzero_int_from_nonzero_int {
484    ($Small:ty => $Large:ty) => {
485        #[stable(feature = "nz_int_conv", since = "1.41.0")]
486        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
487        impl const From<NonZero<$Small>> for NonZero<$Large> {
488            // Rustdocs on the impl block show a "[+] show undocumented items" toggle.
489            // Rustdocs on functions do not.
490            #[doc = concat!("Converts <code>[NonZero]\\<[", stringify!($Small), "]></code> ")]
491            #[doc = concat!("to <code>[NonZero]\\<[", stringify!($Large), "]></code> losslessly.")]
492            #[inline]
493            fn from(small: NonZero<$Small>) -> Self {
494                // SAFETY: input type guarantees the value is non-zero
495                unsafe { Self::new_unchecked(From::from(small.get())) }
496            }
497        }
498    };
499}
500
501// non-zero unsigned integer -> non-zero unsigned integer
502impl_nonzero_int_from_nonzero_int!(u8 => u16);
503impl_nonzero_int_from_nonzero_int!(u8 => u32);
504impl_nonzero_int_from_nonzero_int!(u8 => u64);
505impl_nonzero_int_from_nonzero_int!(u8 => u128);
506impl_nonzero_int_from_nonzero_int!(u8 => usize);
507impl_nonzero_int_from_nonzero_int!(u16 => u32);
508impl_nonzero_int_from_nonzero_int!(u16 => u64);
509impl_nonzero_int_from_nonzero_int!(u16 => u128);
510impl_nonzero_int_from_nonzero_int!(u16 => usize);
511impl_nonzero_int_from_nonzero_int!(u32 => u64);
512impl_nonzero_int_from_nonzero_int!(u32 => u128);
513impl_nonzero_int_from_nonzero_int!(u64 => u128);
514
515// non-zero signed integer -> non-zero signed integer
516impl_nonzero_int_from_nonzero_int!(i8 => i16);
517impl_nonzero_int_from_nonzero_int!(i8 => i32);
518impl_nonzero_int_from_nonzero_int!(i8 => i64);
519impl_nonzero_int_from_nonzero_int!(i8 => i128);
520impl_nonzero_int_from_nonzero_int!(i8 => isize);
521impl_nonzero_int_from_nonzero_int!(i16 => i32);
522impl_nonzero_int_from_nonzero_int!(i16 => i64);
523impl_nonzero_int_from_nonzero_int!(i16 => i128);
524impl_nonzero_int_from_nonzero_int!(i16 => isize);
525impl_nonzero_int_from_nonzero_int!(i32 => i64);
526impl_nonzero_int_from_nonzero_int!(i32 => i128);
527impl_nonzero_int_from_nonzero_int!(i64 => i128);
528
529// non-zero unsigned -> non-zero signed integer
530impl_nonzero_int_from_nonzero_int!(u8 => i16);
531impl_nonzero_int_from_nonzero_int!(u8 => i32);
532impl_nonzero_int_from_nonzero_int!(u8 => i64);
533impl_nonzero_int_from_nonzero_int!(u8 => i128);
534impl_nonzero_int_from_nonzero_int!(u8 => isize);
535impl_nonzero_int_from_nonzero_int!(u16 => i32);
536impl_nonzero_int_from_nonzero_int!(u16 => i64);
537impl_nonzero_int_from_nonzero_int!(u16 => i128);
538impl_nonzero_int_from_nonzero_int!(u32 => i64);
539impl_nonzero_int_from_nonzero_int!(u32 => i128);
540impl_nonzero_int_from_nonzero_int!(u64 => i128);
541
542macro_rules! impl_nonzero_int_try_from_int {
543    ($Int:ty) => {
544        #[stable(feature = "nzint_try_from_int_conv", since = "1.46.0")]
545        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
546        impl const TryFrom<$Int> for NonZero<$Int> {
547            type Error = TryFromIntError;
548
549            // Rustdocs on the impl block show a "[+] show undocumented items" toggle.
550            // Rustdocs on functions do not.
551            #[doc = concat!("Attempts to convert [`", stringify!($Int), "`] ")]
552            #[doc = concat!("to <code>[NonZero]\\<[", stringify!($Int), "]></code>.")]
553            #[inline]
554            fn try_from(value: $Int) -> Result<Self, Self::Error> {
555                Self::new(value).ok_or(TryFromIntError(()))
556            }
557        }
558    };
559}
560
561// integer -> non-zero integer
562impl_nonzero_int_try_from_int!(u8);
563impl_nonzero_int_try_from_int!(u16);
564impl_nonzero_int_try_from_int!(u32);
565impl_nonzero_int_try_from_int!(u64);
566impl_nonzero_int_try_from_int!(u128);
567impl_nonzero_int_try_from_int!(usize);
568impl_nonzero_int_try_from_int!(i8);
569impl_nonzero_int_try_from_int!(i16);
570impl_nonzero_int_try_from_int!(i32);
571impl_nonzero_int_try_from_int!(i64);
572impl_nonzero_int_try_from_int!(i128);
573impl_nonzero_int_try_from_int!(isize);
574
575macro_rules! impl_nonzero_int_try_from_nonzero_int {
576    ($source:ty => $($target:ty),+) => {$(
577        #[stable(feature = "nzint_try_from_nzint_conv", since = "1.49.0")]
578        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
579        impl const TryFrom<NonZero<$source>> for NonZero<$target> {
580            type Error = TryFromIntError;
581
582            // Rustdocs on the impl block show a "[+] show undocumented items" toggle.
583            // Rustdocs on functions do not.
584            #[doc = concat!("Attempts to convert <code>[NonZero]\\<[", stringify!($source), "]></code> ")]
585            #[doc = concat!("to <code>[NonZero]\\<[", stringify!($target), "]></code>.")]
586            #[inline]
587            fn try_from(value: NonZero<$source>) -> Result<Self, Self::Error> {
588                // SAFETY: Input is guaranteed to be non-zero.
589                Ok(unsafe { Self::new_unchecked(<$target>::try_from(value.get())?) })
590            }
591        }
592    )*};
593}
594
595// unsigned non-zero integer -> unsigned non-zero integer
596impl_nonzero_int_try_from_nonzero_int!(u16 => u8);
597impl_nonzero_int_try_from_nonzero_int!(u32 => u8, u16, usize);
598impl_nonzero_int_try_from_nonzero_int!(u64 => u8, u16, u32, usize);
599impl_nonzero_int_try_from_nonzero_int!(u128 => u8, u16, u32, u64, usize);
600impl_nonzero_int_try_from_nonzero_int!(usize => u8, u16, u32, u64, u128);
601
602// signed non-zero integer -> signed non-zero integer
603impl_nonzero_int_try_from_nonzero_int!(i16 => i8);
604impl_nonzero_int_try_from_nonzero_int!(i32 => i8, i16, isize);
605impl_nonzero_int_try_from_nonzero_int!(i64 => i8, i16, i32, isize);
606impl_nonzero_int_try_from_nonzero_int!(i128 => i8, i16, i32, i64, isize);
607impl_nonzero_int_try_from_nonzero_int!(isize => i8, i16, i32, i64, i128);
608
609// unsigned non-zero integer -> signed non-zero integer
610impl_nonzero_int_try_from_nonzero_int!(u8 => i8);
611impl_nonzero_int_try_from_nonzero_int!(u16 => i8, i16, isize);
612impl_nonzero_int_try_from_nonzero_int!(u32 => i8, i16, i32, isize);
613impl_nonzero_int_try_from_nonzero_int!(u64 => i8, i16, i32, i64, isize);
614impl_nonzero_int_try_from_nonzero_int!(u128 => i8, i16, i32, i64, i128, isize);
615impl_nonzero_int_try_from_nonzero_int!(usize => i8, i16, i32, i64, i128, isize);
616
617// signed non-zero integer -> unsigned non-zero integer
618impl_nonzero_int_try_from_nonzero_int!(i8 => u8, u16, u32, u64, u128, usize);
619impl_nonzero_int_try_from_nonzero_int!(i16 => u8, u16, u32, u64, u128, usize);
620impl_nonzero_int_try_from_nonzero_int!(i32 => u8, u16, u32, u64, u128, usize);
621impl_nonzero_int_try_from_nonzero_int!(i64 => u8, u16, u32, u64, u128, usize);
622impl_nonzero_int_try_from_nonzero_int!(i128 => u8, u16, u32, u64, u128, usize);
623impl_nonzero_int_try_from_nonzero_int!(isize => u8, u16, u32, u64, u128, usize);
````