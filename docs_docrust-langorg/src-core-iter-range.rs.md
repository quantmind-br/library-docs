---
title: range.rs - source
url: https://doc.rust-lang.org/src/core/iter/range.rs.html#90
source: crawler
fetched_at: 2026-05-06T21:29:27.805296198-03:00
rendered_js: false
word_count: 6531
summary: This document defines the Step trait in Rust, which provides an interface for types that support successor and predecessor operations, enabling them to function within ranges and iterators.
tags:
    - rust
    - trait
    - iterator
    - step
    - generic-programming
    - ranges
category: reference
---

## core/iter/ range.rs

```rust
1use super::{
2    FusedIterator, TrustedLen, TrustedRandomAccess, TrustedRandomAccessNoCoerce, TrustedStep,
3};
4use crate::ascii::Char as AsciiChar;
5use crate::mem;
6use crate::net::{Ipv4Addr, Ipv6Addr};
7use crate::num::NonZero;
8use crate::ops::{self, Try};
9
10// Safety: All invariants are upheld.
11macro_rules! unsafe_impl_trusted_step {
12    ($($type:ty)*) => {$(
13        #[unstable(feature = "trusted_step", issue = "85731")]
14        unsafe impl TrustedStep for $type {}
15    )*};
16}
17unsafe_impl_trusted_step![AsciiChar char i8 i16 i32 i64 i128 isize u8 u16 u32 u64 u128 usize Ipv4Addr Ipv6Addr];
18
19/// Objects that have a notion of *successor* and *predecessor* operations.
20///
21/// The *successor* operation moves towards values that compare greater.
22/// The *predecessor* operation moves towards values that compare lesser.
23#[rustc_diagnostic_item = "range_step"]
24#[rustc_on_unimplemented(
25    message = "`std::ops::Range<{Self}>` is not an iterator",
26    label = "`Range<{Self}>` is not an iterator",
27    note = "`Range` only implements `Iterator` for select types in the standard library, \
28            particularly integers; to see the full list of types, see the documentation for the \
29            unstable `Step` trait"
30)]
31#[unstable(feature = "step_trait", issue = "42168")]
32pub trait Step: Clone + PartialOrd + Sized {
33    /// Returns the bounds on the number of *successor* steps required to get from `start` to `end`
34    /// like [`Iterator::size_hint()`][Iterator::size_hint()].
35    ///
36    /// Returns `(usize::MAX, None)` if the number of steps would overflow `usize`, or is infinite.
37    ///
38    /// # Invariants
39    ///
40    /// For any `a`, `b`, and `n`:
41    ///
42    /// * `steps_between(&a, &b) == (n, Some(n))` if and only if `Step::forward_checked(&a, n) == Some(b)`
43    /// * `steps_between(&a, &b) == (n, Some(n))` if and only if `Step::backward_checked(&b, n) == Some(a)`
44    /// * `steps_between(&a, &b) == (n, Some(n))` only if `a <= b`
45    ///   * Corollary: `steps_between(&a, &b) == (0, Some(0))` if and only if `a == b`
46    /// * `steps_between(&a, &b) == (0, None)` if `a > b`
47    fn steps_between(start: &Self, end: &Self) -> (usize, Option<usize>);
48
49    /// Returns the value that would be obtained by taking the *successor*
50    /// of `self` `count` times.
51    ///
52    /// If this would overflow the range of values supported by `Self`, returns `None`.
53    ///
54    /// # Invariants
55    ///
56    /// For any `a`, `n`, and `m`:
57    ///
58    /// * `Step::forward_checked(a, n).and_then(|x| Step::forward_checked(x, m)) == Step::forward_checked(a, m).and_then(|x| Step::forward_checked(x, n))`
59    /// * `Step::forward_checked(a, n).and_then(|x| Step::forward_checked(x, m)) == try { Step::forward_checked(a, n.checked_add(m)) }`
60    ///
61    /// For any `a` and `n`:
62    ///
63    /// * `Step::forward_checked(a, n) == (0..n).try_fold(a, |x, _| Step::forward_checked(&x, 1))`
64    ///   * Corollary: `Step::forward_checked(a, 0) == Some(a)`
65    fn forward_checked(start: Self, count: usize) -> Option<Self>;
66
67    /// Returns the value that would be obtained by taking the *successor*
68    /// of `self` `count` times.
69    ///
70    /// If this would overflow the range of values supported by `Self`,
71    /// this function is allowed to panic, wrap, or saturate.
72    /// The suggested behavior is to panic when debug assertions are enabled,
73    /// and to wrap or saturate otherwise.
74    ///
75    /// Unsafe code should not rely on the correctness of behavior after overflow.
76    ///
77    /// # Invariants
78    ///
79    /// For any `a`, `n`, and `m`, where no overflow occurs:
80    ///
81    /// * `Step::forward(Step::forward(a, n), m) == Step::forward(a, n + m)`
82    ///
83    /// For any `a` and `n`, where no overflow occurs:
84    ///
85    /// * `Step::forward_checked(a, n) == Some(Step::forward(a, n))`
86    /// * `Step::forward(a, n) == (0..n).fold(a, |x, _| Step::forward(x, 1))`
87    ///   * Corollary: `Step::forward(a, 0) == a`
88    /// * `Step::forward(a, n) >= a`
89    /// * `Step::backward(Step::forward(a, n), n) == a`
90    fn forward(start: Self, count: usize) -> Self {
91        Step::forward_checked(start, count).expect("overflow in `Step::forward`")
92    }
93
94    /// Returns the value that would be obtained by taking the *successor*
95    /// of `self` `count` times.
96    ///
97    /// # Safety
98    ///
99    /// It is undefined behavior for this operation to overflow the
100    /// range of values supported by `Self`. If you cannot guarantee that this
101    /// will not overflow, use `forward` or `forward_checked` instead.
102    ///
103    /// # Invariants
104    ///
105    /// For any `a`:
106    ///
107    /// * if there exists `b` such that `b > a`, it is safe to call `Step::forward_unchecked(a, 1)`
108    /// * if there exists `b`, `n` such that `steps_between(&a, &b) == Some(n)`,
109    ///   it is safe to call `Step::forward_unchecked(a, m)` for any `m <= n`.
110    ///   * Corollary: `Step::forward_unchecked(a, 0)` is always safe.
111    ///
112    /// For any `a` and `n`, where no overflow occurs:
113    ///
114    /// * `Step::forward_unchecked(a, n)` is equivalent to `Step::forward(a, n)`
115    unsafe fn forward_unchecked(start: Self, count: usize) -> Self {
116        Step::forward(start, count)
117    }
118
119    /// Returns the value that would be obtained by taking the *predecessor*
120    /// of `self` `count` times.
121    ///
122    /// If this would overflow the range of values supported by `Self`, returns `None`.
123    ///
124    /// # Invariants
125    ///
126    /// For any `a`, `n`, and `m`:
127    ///
128    /// * `Step::backward_checked(a, n).and_then(|x| Step::backward_checked(x, m)) == n.checked_add(m).and_then(|x| Step::backward_checked(a, x))`
129    /// * `Step::backward_checked(a, n).and_then(|x| Step::backward_checked(x, m)) == try { Step::backward_checked(a, n.checked_add(m)?) }`
130    ///
131    /// For any `a` and `n`:
132    ///
133    /// * `Step::backward_checked(a, n) == (0..n).try_fold(a, |x, _| Step::backward_checked(x, 1))`
134    ///   * Corollary: `Step::backward_checked(a, 0) == Some(a)`
135    fn backward_checked(start: Self, count: usize) -> Option<Self>;
136
137    /// Returns the value that would be obtained by taking the *predecessor*
138    /// of `self` `count` times.
139    ///
140    /// If this would overflow the range of values supported by `Self`,
141    /// this function is allowed to panic, wrap, or saturate.
142    /// The suggested behavior is to panic when debug assertions are enabled,
143    /// and to wrap or saturate otherwise.
144    ///
145    /// Unsafe code should not rely on the correctness of behavior after overflow.
146    ///
147    /// # Invariants
148    ///
149    /// For any `a`, `n`, and `m`, where no overflow occurs:
150    ///
151    /// * `Step::backward(Step::backward(a, n), m) == Step::backward(a, n + m)`
152    ///
153    /// For any `a` and `n`, where no overflow occurs:
154    ///
155    /// * `Step::backward_checked(a, n) == Some(Step::backward(a, n))`
156    /// * `Step::backward(a, n) == (0..n).fold(a, |x, _| Step::backward(x, 1))`
157    ///   * Corollary: `Step::backward(a, 0) == a`
158    /// * `Step::backward(a, n) <= a`
159    /// * `Step::forward(Step::backward(a, n), n) == a`
160    fn backward(start: Self, count: usize) -> Self {
161        Step::backward_checked(start, count).expect("overflow in `Step::backward`")
162    }
163
164    /// Returns the value that would be obtained by taking the *predecessor*
165    /// of `self` `count` times.
166    ///
167    /// # Safety
168    ///
169    /// It is undefined behavior for this operation to overflow the
170    /// range of values supported by `Self`. If you cannot guarantee that this
171    /// will not overflow, use `backward` or `backward_checked` instead.
172    ///
173    /// # Invariants
174    ///
175    /// For any `a`:
176    ///
177    /// * if there exists `b` such that `b < a`, it is safe to call `Step::backward_unchecked(a, 1)`
178    /// * if there exists `b`, `n` such that `steps_between(&b, &a) == (n, Some(n))`,
179    ///   it is safe to call `Step::backward_unchecked(a, m)` for any `m <= n`.
180    ///   * Corollary: `Step::backward_unchecked(a, 0)` is always safe.
181    ///
182    /// For any `a` and `n`, where no overflow occurs:
183    ///
184    /// * `Step::backward_unchecked(a, n)` is equivalent to `Step::backward(a, n)`
185    unsafe fn backward_unchecked(start: Self, count: usize) -> Self {
186        Step::backward(start, count)
187    }
188}
189
190// Separate impls for signed ranges because the distance within a signed range can be larger
191// than the signed::MAX value. Therefore `as` casting to the signed type would be incorrect.
192macro_rules! step_signed_methods {
193    ($unsigned: ty) => {
194        #[inline]
195        unsafe fn forward_unchecked(start: Self, n: usize) -> Self {
196            // SAFETY: the caller has to guarantee that `start + n` doesn't overflow.
197            unsafe { start.checked_add_unsigned(n as $unsigned).unwrap_unchecked() }
198        }
199
200        #[inline]
201        unsafe fn backward_unchecked(start: Self, n: usize) -> Self {
202            // SAFETY: the caller has to guarantee that `start - n` doesn't overflow.
203            unsafe { start.checked_sub_unsigned(n as $unsigned).unwrap_unchecked() }
204        }
205    };
206}
207
208macro_rules! step_unsigned_methods {
209    () => {
210        #[inline]
211        unsafe fn forward_unchecked(start: Self, n: usize) -> Self {
212            // SAFETY: the caller has to guarantee that `start + n` doesn't overflow.
213            unsafe { start.unchecked_add(n as Self) }
214        }
215
216        #[inline]
217        unsafe fn backward_unchecked(start: Self, n: usize) -> Self {
218            // SAFETY: the caller has to guarantee that `start - n` doesn't overflow.
219            unsafe { start.unchecked_sub(n as Self) }
220        }
221    };
222}
223
224// These are still macro-generated because the integer literals resolve to different types.
225macro_rules! step_identical_methods {
226    () => {
227        #[inline]
228        #[allow(arithmetic_overflow)]
229        #[rustc_inherit_overflow_checks]
230        fn forward(start: Self, n: usize) -> Self {
231            // In debug builds, trigger a panic on overflow.
232            // This should optimize completely out in release builds.
233            if Self::forward_checked(start, n).is_none() {
234                let _ = Self::MAX + 1;
235            }
236            // Do wrapping math to allow e.g. `Step::forward(-128i8, 255)`.
237            start.wrapping_add(n as Self)
238        }
239
240        #[inline]
241        #[allow(arithmetic_overflow)]
242        #[rustc_inherit_overflow_checks]
243        fn backward(start: Self, n: usize) -> Self {
244            // In debug builds, trigger a panic on overflow.
245            // This should optimize completely out in release builds.
246            if Self::backward_checked(start, n).is_none() {
247                let _ = Self::MIN - 1;
248            }
249            // Do wrapping math to allow e.g. `Step::backward(127i8, 255)`.
250            start.wrapping_sub(n as Self)
251        }
252    };
253}
254
255macro_rules! step_integer_impls {
256    {
257        narrower than or same width as usize:
258            $( [ $u_narrower:ident $i_narrower:ident ] ),+;
259        wider than usize:
260            $( [ $u_wider:ident $i_wider:ident ] ),+;
261    } => {
262        $(
263            #[allow(unreachable_patterns)]
264            #[unstable(feature = "step_trait", issue = "42168")]
265            impl Step for $u_narrower {
266                step_identical_methods!();
267                step_unsigned_methods!();
268
269                #[inline]
270                fn steps_between(start: &Self, end: &Self) -> (usize, Option<usize>) {
271                    if *start <= *end {
272                        // This relies on $u_narrower <= usize
273                        let steps = (*end - *start) as usize;
274                        (steps, Some(steps))
275                    } else {
276                        (0, None)
277                    }
278                }
279
280                #[inline]
281                fn forward_checked(start: Self, n: usize) -> Option<Self> {
282                    match Self::try_from(n) {
283                        Ok(n) => start.checked_add(n),
284                        Err(_) => None, // if n is out of range, `unsigned_start + n` is too
285                    }
286                }
287
288                #[inline]
289                fn backward_checked(start: Self, n: usize) -> Option<Self> {
290                    match Self::try_from(n) {
291                        Ok(n) => start.checked_sub(n),
292                        Err(_) => None, // if n is out of range, `unsigned_start - n` is too
293                    }
294                }
295            }
296
297            #[allow(unreachable_patterns)]
298            #[unstable(feature = "step_trait", issue = "42168")]
299            impl Step for $i_narrower {
300                step_identical_methods!();
301                step_signed_methods!($u_narrower);
302
303                #[inline]
304                fn steps_between(start: &Self, end: &Self) -> (usize, Option<usize>) {
305                    if *start <= *end {
306                        // This relies on $i_narrower <= usize
307                        //
308                        // Casting to isize extends the width but preserves the sign.
309                        // Use wrapping_sub in isize space and cast to usize to compute
310                        // the difference that might not fit inside the range of isize.
311                        let steps = (*end as isize).wrapping_sub(*start as isize) as usize;
312                        (steps, Some(steps))
313                    } else {
314                        (0, None)
315                    }
316                }
317
318                #[inline]
319                fn forward_checked(start: Self, n: usize) -> Option<Self> {
320                    match $u_narrower::try_from(n) {
321                        Ok(n) => {
322                            // Wrapping handles cases like
323                            // `Step::forward(-120_i8, 200) == Some(80_i8)`,
324                            // even though 200 is out of range for i8.
325                            let wrapped = start.wrapping_add(n as Self);
326                            if wrapped >= start {
327                                Some(wrapped)
328                            } else {
329                                None // Addition overflowed
330                            }
331                        }
332                        // If n is out of range of e.g. u8,
333                        // then it is bigger than the entire range for i8 is wide
334                        // so `any_i8 + n` necessarily overflows i8.
335                        Err(_) => None,
336                    }
337                }
338
339                #[inline]
340                fn backward_checked(start: Self, n: usize) -> Option<Self> {
341                    match $u_narrower::try_from(n) {
342                        Ok(n) => {
343                            // Wrapping handles cases like
344                            // `Step::forward(-120_i8, 200) == Some(80_i8)`,
345                            // even though 200 is out of range for i8.
346                            let wrapped = start.wrapping_sub(n as Self);
347                            if wrapped <= start {
348                                Some(wrapped)
349                            } else {
350                                None // Subtraction overflowed
351                            }
352                        }
353                        // If n is out of range of e.g. u8,
354                        // then it is bigger than the entire range for i8 is wide
355                        // so `any_i8 - n` necessarily overflows i8.
356                        Err(_) => None,
357                    }
358                }
359            }
360        )+
361
362        $(
363            #[allow(unreachable_patterns)]
364            #[unstable(feature = "step_trait", issue = "42168")]
365            impl Step for $u_wider {
366                step_identical_methods!();
367                step_unsigned_methods!();
368
369                #[inline]
370                fn steps_between(start: &Self, end: &Self) -> (usize, Option<usize>) {
371                    if *start <= *end {
372                        if let Ok(steps) = usize::try_from(*end - *start) {
373                            (steps, Some(steps))
374                        } else {
375                            (usize::MAX, None)
376                        }
377                    } else {
378                        (0, None)
379                    }
380                }
381
382                #[inline]
383                fn forward_checked(start: Self, n: usize) -> Option<Self> {
384                    start.checked_add(n as Self)
385                }
386
387                #[inline]
388                fn backward_checked(start: Self, n: usize) -> Option<Self> {
389                    start.checked_sub(n as Self)
390                }
391            }
392
393            #[allow(unreachable_patterns)]
394            #[unstable(feature = "step_trait", issue = "42168")]
395            impl Step for $i_wider {
396                step_identical_methods!();
397                step_signed_methods!($u_wider);
398
399                #[inline]
400                fn steps_between(start: &Self, end: &Self) -> (usize, Option<usize>) {
401                    if *start <= *end {
402                        match end.checked_sub(*start) {
403                            Some(result) => {
404                                if let Ok(steps) = usize::try_from(result) {
405                                    (steps, Some(steps))
406                                } else {
407                                    (usize::MAX, None)
408                                }
409                            }
410                            // If the difference is too big for e.g. i128,
411                            // it's also gonna be too big for usize with fewer bits.
412                            None => (usize::MAX, None),
413                        }
414                    } else {
415                        (0, None)
416                    }
417                }
418
419                #[inline]
420                fn forward_checked(start: Self, n: usize) -> Option<Self> {
421                    start.checked_add(n as Self)
422                }
423
424                #[inline]
425                fn backward_checked(start: Self, n: usize) -> Option<Self> {
426                    start.checked_sub(n as Self)
427                }
428            }
429        )+
430    };
431}
432
433#[cfg(target_pointer_width = "64")]
434step_integer_impls! {
435    narrower than or same width as usize: [u8 i8], [u16 i16], [u32 i32], [u64 i64], [usize isize];
436    wider than usize: [u128 i128];
437}
438
439#[cfg(target_pointer_width = "32")]
440step_integer_impls! {
441    narrower than or same width as usize: [u8 i8], [u16 i16], [u32 i32], [usize isize];
442    wider than usize: [u64 i64], [u128 i128];
443}
444
445#[cfg(target_pointer_width = "16")]
446step_integer_impls! {
447    narrower than or same width as usize: [u8 i8], [u16 i16], [usize isize];
448    wider than usize: [u32 i32], [u64 i64], [u128 i128];
449}
450
451#[unstable(feature = "step_trait", issue = "42168")]
452impl Step for char {
453    #[inline]
454    fn steps_between(&start: &char, &end: &char) -> (usize, Option<usize>) {
455        let start = start as u32;
456        let end = end as u32;
457        if start <= end {
458            let count = end - start;
459            if start < 0xD800 && 0xE000 <= end {
460                if let Ok(steps) = usize::try_from(count - 0x800) {
461                    (steps, Some(steps))
462                } else {
463                    (usize::MAX, None)
464                }
465            } else {
466                if let Ok(steps) = usize::try_from(count) {
467                    (steps, Some(steps))
468                } else {
469                    (usize::MAX, None)
470                }
471            }
472        } else {
473            (0, None)
474        }
475    }
476
477    #[inline]
478    fn forward_checked(start: char, count: usize) -> Option<char> {
479        let start = start as u32;
480        let mut res = Step::forward_checked(start, count)?;
481        if start < 0xD800 && 0xD800 <= res {
482            res = Step::forward_checked(res, 0x800)?;
483        }
484        if res <= char::MAX as u32 {
485            // SAFETY: res is a valid unicode scalar
486            // (below 0x110000 and not in 0xD800..0xE000)
487            Some(unsafe { char::from_u32_unchecked(res) })
488        } else {
489            None
490        }
491    }
492
493    #[inline]
494    fn backward_checked(start: char, count: usize) -> Option<char> {
495        let start = start as u32;
496        let mut res = Step::backward_checked(start, count)?;
497        if start >= 0xE000 && 0xE000 > res {
498            res = Step::backward_checked(res, 0x800)?;
499        }
500        // SAFETY: res is a valid unicode scalar
501        // (below 0x110000 and not in 0xD800..0xE000)
502        Some(unsafe { char::from_u32_unchecked(res) })
503    }
504
505    #[inline]
506    unsafe fn forward_unchecked(start: char, count: usize) -> char {
507        let start = start as u32;
508        // SAFETY: the caller must guarantee that this doesn't overflow
509        // the range of values for a char.
510        let mut res = unsafe { Step::forward_unchecked(start, count) };
511        if start < 0xD800 && 0xD800 <= res {
512            // SAFETY: the caller must guarantee that this doesn't overflow
513            // the range of values for a char.
514            res = unsafe { Step::forward_unchecked(res, 0x800) };
515        }
516        // SAFETY: because of the previous contract, this is guaranteed
517        // by the caller to be a valid char.
518        unsafe { char::from_u32_unchecked(res) }
519    }
520
521    #[inline]
522    unsafe fn backward_unchecked(start: char, count: usize) -> char {
523        let start = start as u32;
524        // SAFETY: the caller must guarantee that this doesn't overflow
525        // the range of values for a char.
526        let mut res = unsafe { Step::backward_unchecked(start, count) };
527        if start >= 0xE000 && 0xE000 > res {
528            // SAFETY: the caller must guarantee that this doesn't overflow
529            // the range of values for a char.
530            res = unsafe { Step::backward_unchecked(res, 0x800) };
531        }
532        // SAFETY: because of the previous contract, this is guaranteed
533        // by the caller to be a valid char.
534        unsafe { char::from_u32_unchecked(res) }
535    }
536}
537
538#[unstable(feature = "step_trait", issue = "42168")]
539impl Step for AsciiChar {
540    #[inline]
541    fn steps_between(&start: &AsciiChar, &end: &AsciiChar) -> (usize, Option<usize>) {
542        Step::steps_between(&start.to_u8(), &end.to_u8())
543    }
544
545    #[inline]
546    fn forward_checked(start: AsciiChar, count: usize) -> Option<AsciiChar> {
547        let end = Step::forward_checked(start.to_u8(), count)?;
548        AsciiChar::from_u8(end)
549    }
550
551    #[inline]
552    fn backward_checked(start: AsciiChar, count: usize) -> Option<AsciiChar> {
553        let end = Step::backward_checked(start.to_u8(), count)?;
554
555        // SAFETY: Values below that of a valid ASCII character are also valid ASCII
556        Some(unsafe { AsciiChar::from_u8_unchecked(end) })
557    }
558
559    #[inline]
560    unsafe fn forward_unchecked(start: AsciiChar, count: usize) -> AsciiChar {
561        // SAFETY: Caller asserts that result is a valid ASCII character,
562        // and therefore it is a valid u8.
563        let end = unsafe { Step::forward_unchecked(start.to_u8(), count) };
564
565        // SAFETY: Caller asserts that result is a valid ASCII character.
566        unsafe { AsciiChar::from_u8_unchecked(end) }
567    }
568
569    #[inline]
570    unsafe fn backward_unchecked(start: AsciiChar, count: usize) -> AsciiChar {
571        // SAFETY: Caller asserts that result is a valid ASCII character,
572        // and therefore it is a valid u8.
573        let end = unsafe { Step::backward_unchecked(start.to_u8(), count) };
574
575        // SAFETY: Caller asserts that result is a valid ASCII character.
576        unsafe { AsciiChar::from_u8_unchecked(end) }
577    }
578}
579
580#[unstable(feature = "step_trait", issue = "42168")]
581impl Step for Ipv4Addr {
582    #[inline]
583    fn steps_between(&start: &Ipv4Addr, &end: &Ipv4Addr) -> (usize, Option<usize>) {
584        u32::steps_between(&start.to_bits(), &end.to_bits())
585    }
586
587    #[inline]
588    fn forward_checked(start: Ipv4Addr, count: usize) -> Option<Ipv4Addr> {
589        u32::forward_checked(start.to_bits(), count).map(Ipv4Addr::from_bits)
590    }
591
592    #[inline]
593    fn backward_checked(start: Ipv4Addr, count: usize) -> Option<Ipv4Addr> {
594        u32::backward_checked(start.to_bits(), count).map(Ipv4Addr::from_bits)
595    }
596
597    #[inline]
598    unsafe fn forward_unchecked(start: Ipv4Addr, count: usize) -> Ipv4Addr {
599        // SAFETY: Since u32 and Ipv4Addr are losslessly convertible,
600        //   this is as safe as the u32 version.
601        Ipv4Addr::from_bits(unsafe { u32::forward_unchecked(start.to_bits(), count) })
602    }
603
604    #[inline]
605    unsafe fn backward_unchecked(start: Ipv4Addr, count: usize) -> Ipv4Addr {
606        // SAFETY: Since u32 and Ipv4Addr are losslessly convertible,
607        //   this is as safe as the u32 version.
608        Ipv4Addr::from_bits(unsafe { u32::backward_unchecked(start.to_bits(), count) })
609    }
610}
611
612#[unstable(feature = "step_trait", issue = "42168")]
613impl Step for Ipv6Addr {
614    #[inline]
615    fn steps_between(&start: &Ipv6Addr, &end: &Ipv6Addr) -> (usize, Option<usize>) {
616        u128::steps_between(&start.to_bits(), &end.to_bits())
617    }
618
619    #[inline]
620    fn forward_checked(start: Ipv6Addr, count: usize) -> Option<Ipv6Addr> {
621        u128::forward_checked(start.to_bits(), count).map(Ipv6Addr::from_bits)
622    }
623
624    #[inline]
625    fn backward_checked(start: Ipv6Addr, count: usize) -> Option<Ipv6Addr> {
626        u128::backward_checked(start.to_bits(), count).map(Ipv6Addr::from_bits)
627    }
628
629    #[inline]
630    unsafe fn forward_unchecked(start: Ipv6Addr, count: usize) -> Ipv6Addr {
631        // SAFETY: Since u128 and Ipv6Addr are losslessly convertible,
632        //   this is as safe as the u128 version.
633        Ipv6Addr::from_bits(unsafe { u128::forward_unchecked(start.to_bits(), count) })
634    }
635
636    #[inline]
637    unsafe fn backward_unchecked(start: Ipv6Addr, count: usize) -> Ipv6Addr {
638        // SAFETY: Since u128 and Ipv6Addr are losslessly convertible,
639        //   this is as safe as the u128 version.
640        Ipv6Addr::from_bits(unsafe { u128::backward_unchecked(start.to_bits(), count) })
641    }
642}
643
644macro_rules! range_exact_iter_impl {
645    ($($t:ty)*) => ($(
646        #[stable(feature = "rust1", since = "1.0.0")]
647        impl ExactSizeIterator for ops::Range<$t> { }
648    )*)
649}
650
651/// Safety: This macro must only be used on types that are `Copy` and result in ranges
652/// which have an exact `size_hint()` where the upper bound must not be `None`.
653macro_rules! unsafe_range_trusted_random_access_impl {
654    ($($t:ty)*) => ($(
655        #[doc(hidden)]
656        #[unstable(feature = "trusted_random_access", issue = "none")]
657        unsafe impl TrustedRandomAccess for ops::Range<$t> {}
658
659        #[doc(hidden)]
660        #[unstable(feature = "trusted_random_access", issue = "none")]
661        unsafe impl TrustedRandomAccessNoCoerce for ops::Range<$t> {
662            const MAY_HAVE_SIDE_EFFECT: bool = false;
663        }
664    )*)
665}
666
667macro_rules! range_incl_exact_iter_impl {
668    ($($t:ty)*) => ($(
669        #[stable(feature = "inclusive_range", since = "1.26.0")]
670        impl ExactSizeIterator for ops::RangeInclusive<$t> { }
671    )*)
672}
673
674/// Specialization implementations for `Range`.
675trait RangeIteratorImpl {
676    type Item;
677
678    // Iterator
679    fn spec_next(&mut self) -> Option<Self::Item>;
680    fn spec_nth(&mut self, n: usize) -> Option<Self::Item>;
681    fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>>;
682
683    // DoubleEndedIterator
684    fn spec_next_back(&mut self) -> Option<Self::Item>;
685    fn spec_nth_back(&mut self, n: usize) -> Option<Self::Item>;
686    fn spec_advance_back_by(&mut self, n: usize) -> Result<(), NonZero<usize>>;
687}
688
689impl<A: Step> RangeIteratorImpl for ops::Range<A> {
690    type Item = A;
691
692    #[inline]
693    default fn spec_next(&mut self) -> Option<A> {
694        if self.start < self.end {
695            let n =
696                Step::forward_checked(self.start.clone(), 1).expect("`Step` invariants not upheld");
697            Some(mem::replace(&mut self.start, n))
698        } else {
699            None
700        }
701    }
702
703    #[inline]
704    default fn spec_nth(&mut self, n: usize) -> Option<A> {
705        if let Some(plus_n) = Step::forward_checked(self.start.clone(), n) {
706            if plus_n < self.end {
707                self.start =
708                    Step::forward_checked(plus_n.clone(), 1).expect("`Step` invariants not upheld");
709                return Some(plus_n);
710            }
711        }
712
713        self.start = self.end.clone();
714        None
715    }
716
717    #[inline]
718    default fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
719        let steps = Step::steps_between(&self.start, &self.end);
720        let available = steps.1.unwrap_or(steps.0);
721
722        let taken = available.min(n);
723
724        self.start =
725            Step::forward_checked(self.start.clone(), taken).expect("`Step` invariants not upheld");
726
727        NonZero::new(n - taken).map_or(Ok(()), Err)
728    }
729
730    #[inline]
731    default fn spec_next_back(&mut self) -> Option<A> {
732        if self.start < self.end {
733            self.end =
734                Step::backward_checked(self.end.clone(), 1).expect("`Step` invariants not upheld");
735            Some(self.end.clone())
736        } else {
737            None
738        }
739    }
740
741    #[inline]
742    default fn spec_nth_back(&mut self, n: usize) -> Option<A> {
743        if let Some(minus_n) = Step::backward_checked(self.end.clone(), n) {
744            if minus_n > self.start {
745                self.end =
746                    Step::backward_checked(minus_n, 1).expect("`Step` invariants not upheld");
747                return Some(self.end.clone());
748            }
749        }
750
751        self.end = self.start.clone();
752        None
753    }
754
755    #[inline]
756    default fn spec_advance_back_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
757        let steps = Step::steps_between(&self.start, &self.end);
758        let available = steps.1.unwrap_or(steps.0);
759
760        let taken = available.min(n);
761
762        self.end =
763            Step::backward_checked(self.end.clone(), taken).expect("`Step` invariants not upheld");
764
765        NonZero::new(n - taken).map_or(Ok(()), Err)
766    }
767}
768
769impl<T: TrustedStep> RangeIteratorImpl for ops::Range<T> {
770    #[inline]
771    fn spec_next(&mut self) -> Option<T> {
772        if self.start < self.end {
773            let old = self.start;
774            // SAFETY: just checked precondition
775            self.start = unsafe { Step::forward_unchecked(old, 1) };
776            Some(old)
777        } else {
778            None
779        }
780    }
781
782    #[inline]
783    fn spec_nth(&mut self, n: usize) -> Option<T> {
784        if let Some(plus_n) = Step::forward_checked(self.start, n) {
785            if plus_n < self.end {
786                // SAFETY: just checked precondition
787                self.start = unsafe { Step::forward_unchecked(plus_n, 1) };
788                return Some(plus_n);
789            }
790        }
791
792        self.start = self.end;
793        None
794    }
795
796    #[inline]
797    fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
798        let steps = Step::steps_between(&self.start, &self.end);
799        let available = steps.1.unwrap_or(steps.0);
800
801        let taken = available.min(n);
802
803        // SAFETY: the conditions above ensure that the count is in bounds. If start <= end
804        // then steps_between either returns a bound to which we clamp or returns None which
805        // together with the initial inequality implies more than usize::MAX steps.
806        // Otherwise 0 is returned which always safe to use.
807        self.start = unsafe { Step::forward_unchecked(self.start, taken) };
808
809        NonZero::new(n - taken).map_or(Ok(()), Err)
810    }
811
812    #[inline]
813    fn spec_next_back(&mut self) -> Option<T> {
814        if self.start < self.end {
815            // SAFETY: just checked precondition
816            self.end = unsafe { Step::backward_unchecked(self.end, 1) };
817            Some(self.end)
818        } else {
819            None
820        }
821    }
822
823    #[inline]
824    fn spec_nth_back(&mut self, n: usize) -> Option<T> {
825        if let Some(minus_n) = Step::backward_checked(self.end, n) {
826            if minus_n > self.start {
827                // SAFETY: just checked precondition
828                self.end = unsafe { Step::backward_unchecked(minus_n, 1) };
829                return Some(self.end);
830            }
831        }
832
833        self.end = self.start;
834        None
835    }
836
837    #[inline]
838    fn spec_advance_back_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
839        let steps = Step::steps_between(&self.start, &self.end);
840        let available = steps.1.unwrap_or(steps.0);
841
842        let taken = available.min(n);
843
844        // SAFETY: same as the spec_advance_by() implementation
845        self.end = unsafe { Step::backward_unchecked(self.end, taken) };
846
847        NonZero::new(n - taken).map_or(Ok(()), Err)
848    }
849}
850
851#[stable(feature = "rust1", since = "1.0.0")]
852impl<A: Step> Iterator for ops::Range<A> {
853    type Item = A;
854
855    #[inline]
856    fn next(&mut self) -> Option<A> {
857        self.spec_next()
858    }
859
860    #[inline]
861    fn size_hint(&self) -> (usize, Option<usize>) {
862        if self.start < self.end {
863            Step::steps_between(&self.start, &self.end)
864        } else {
865            (0, Some(0))
866        }
867    }
868
869    #[inline]
870    fn count(self) -> usize {
871        if self.start < self.end {
872            Step::steps_between(&self.start, &self.end).1.expect("count overflowed usize")
873        } else {
874            0
875        }
876    }
877
878    #[inline]
879    fn nth(&mut self, n: usize) -> Option<A> {
880        self.spec_nth(n)
881    }
882
883    #[inline]
884    fn last(mut self) -> Option<A> {
885        self.next_back()
886    }
887
888    #[inline]
889    fn min(mut self) -> Option<A>
890    where
891        A: Ord,
892    {
893        self.next()
894    }
895
896    #[inline]
897    fn max(mut self) -> Option<A>
898    where
899        A: Ord,
900    {
901        self.next_back()
902    }
903
904    #[inline]
905    fn is_sorted(self) -> bool {
906        true
907    }
908
909    #[inline]
910    fn advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
911        self.spec_advance_by(n)
912    }
913
914    #[inline]
915    unsafe fn __iterator_get_unchecked(&mut self, idx: usize) -> Self::Item
916    where
917        Self: TrustedRandomAccessNoCoerce,
918    {
919        // SAFETY: The TrustedRandomAccess contract requires that callers only pass an index
920        // that is in bounds.
921        // Additionally Self: TrustedRandomAccess is only implemented for Copy types
922        // which means even repeated reads of the same index would be safe.
923        unsafe { Step::forward_unchecked(self.start.clone(), idx) }
924    }
925}
926
927// These macros generate `ExactSizeIterator` impls for various range types.
928//
929// * `ExactSizeIterator::len` is required to always return an exact `usize`,
930//   so no range can be longer than `usize::MAX`.
931// * For integer types in `Range<_>` this is the case for types narrower than or as wide as `usize`.
932//   For integer types in `RangeInclusive<_>`
933//   this is the case for types *strictly narrower* than `usize`
934//   since e.g. `(0..=u64::MAX).len()` would be `u64::MAX + 1`.
935range_exact_iter_impl! {
936    usize u8 u16
937    isize i8 i16
938
939    // These are incorrect per the reasoning above,
940    // but removing them would be a breaking change as they were stabilized in Rust 1.0.0.
941    // So e.g. `(0..66_000_u32).len()` for example will compile without error or warnings
942    // on 16-bit platforms, but continue to give a wrong result.
943    u32
944    i32
945}
946
947unsafe_range_trusted_random_access_impl! {
948    usize u8 u16
949    isize i8 i16
950}
951
952#[cfg(target_pointer_width = "32")]
953unsafe_range_trusted_random_access_impl! {
954    u32 i32
955}
956
957#[cfg(target_pointer_width = "64")]
958unsafe_range_trusted_random_access_impl! {
959    u32 i32
960    u64 i64
961}
962
963range_incl_exact_iter_impl! {
964    u8
965    i8
966
967    // These are incorrect per the reasoning above,
968    // but removing them would be a breaking change as they were stabilized in Rust 1.26.0.
969    // So e.g. `(0..=u16::MAX).len()` for example will compile without error or warnings
970    // on 16-bit platforms, but continue to give a wrong result.
971    u16
972    i16
973}
974
975#[stable(feature = "rust1", since = "1.0.0")]
976impl<A: Step> DoubleEndedIterator for ops::Range<A> {
977    #[inline]
978    fn next_back(&mut self) -> Option<A> {
979        self.spec_next_back()
980    }
981
982    #[inline]
983    fn nth_back(&mut self, n: usize) -> Option<A> {
984        self.spec_nth_back(n)
985    }
986
987    #[inline]
988    fn advance_back_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
989        self.spec_advance_back_by(n)
990    }
991}
992
993// Safety:
994// The following invariants for `Step::steps_between` exist:
995//
996// > * `steps_between(&a, &b) == (n, Some(n))` only if `a <= b`
997// >   * Note that `a <= b` does _not_ imply `steps_between(&a, &b) != (n, None)`;
998// >     this is the case when it would require more than `usize::MAX` steps to
999// >     get to `b`
1000// > * `steps_between(&a, &b) == (0, None)` if `a > b`
1001//
1002// The first invariant is what is generally required for `TrustedLen` to be
1003// sound. The note addendum satisfies an additional `TrustedLen` invariant.
1004//
1005// > The upper bound must only be `None` if the actual iterator length is larger
1006// > than `usize::MAX`
1007//
1008// The second invariant logically follows the first so long as the `PartialOrd`
1009// implementation is correct; regardless it is explicitly stated. If `a < b`
1010// then `(0, Some(0))` is returned by `ops::Range<A: Step>::size_hint`. As such
1011// the second invariant is upheld.
1012#[unstable(feature = "trusted_len", issue = "37572")]
1013unsafe impl<A: TrustedStep> TrustedLen for ops::Range<A> {}
1014
1015#[stable(feature = "fused", since = "1.26.0")]
1016impl<A: Step> FusedIterator for ops::Range<A> {}
1017
1018#[stable(feature = "rust1", since = "1.0.0")]
1019impl<A: Step> Iterator for ops::RangeFrom<A> {
1020    type Item = A;
1021
1022    #[inline]
1023    fn next(&mut self) -> Option<A> {
1024        let n = Step::forward(self.start.clone(), 1);
1025        Some(mem::replace(&mut self.start, n))
1026    }
1027
1028    #[inline]
1029    fn size_hint(&self) -> (usize, Option<usize>) {
1030        (usize::MAX, None)
1031    }
1032
1033    #[inline]
1034    fn nth(&mut self, n: usize) -> Option<A> {
1035        let plus_n = Step::forward(self.start.clone(), n);
1036        self.start = Step::forward(plus_n.clone(), 1);
1037        Some(plus_n)
1038    }
1039}
1040
1041// Safety: See above implementation for `ops::Range<A>`
1042#[unstable(feature = "trusted_len", issue = "37572")]
1043unsafe impl<A: TrustedStep> TrustedLen for ops::RangeFrom<A> {}
1044
1045#[stable(feature = "fused", since = "1.26.0")]
1046impl<A: Step> FusedIterator for ops::RangeFrom<A> {}
1047
1048trait RangeInclusiveIteratorImpl {
1049    type Item;
1050
1051    // Iterator
1052    fn spec_next(&mut self) -> Option<Self::Item>;
1053    fn spec_try_fold<B, F, R>(&mut self, init: B, f: F) -> R
1054    where
1055        Self: Sized,
1056        F: FnMut(B, Self::Item) -> R,
1057        R: Try<Output = B>;
1058
1059    // DoubleEndedIterator
1060    fn spec_next_back(&mut self) -> Option<Self::Item>;
1061    fn spec_try_rfold<B, F, R>(&mut self, init: B, f: F) -> R
1062    where
1063        Self: Sized,
1064        F: FnMut(B, Self::Item) -> R,
1065        R: Try<Output = B>;
1066}
1067
1068impl<A: Step> RangeInclusiveIteratorImpl for ops::RangeInclusive<A> {
1069    type Item = A;
1070
1071    #[inline]
1072    default fn spec_next(&mut self) -> Option<A> {
1073        if self.is_empty() {
1074            return None;
1075        }
1076        let is_iterating = self.start < self.end;
1077        Some(if is_iterating {
1078            let n =
1079                Step::forward_checked(self.start.clone(), 1).expect("`Step` invariants not upheld");
1080            mem::replace(&mut self.start, n)
1081        } else {
1082            self.exhausted = true;
1083            self.start.clone()
1084        })
1085    }
1086
1087    #[inline]
1088    default fn spec_try_fold<B, F, R>(&mut self, init: B, mut f: F) -> R
1089    where
1090        Self: Sized,
1091        F: FnMut(B, A) -> R,
1092        R: Try<Output = B>,
1093    {
1094        if self.is_empty() {
1095            return try { init };
1096        }
1097
1098        let mut accum = init;
1099
1100        while self.start < self.end {
1101            let n =
1102                Step::forward_checked(self.start.clone(), 1).expect("`Step` invariants not upheld");
1103            let n = mem::replace(&mut self.start, n);
1104            accum = f(accum, n)?;
1105        }
1106
1107        self.exhausted = true;
1108
1109        if self.start == self.end {
1110            accum = f(accum, self.start.clone())?;
1111        }
1112
1113        try { accum }
1114    }
1115
1116    #[inline]
1117    default fn spec_next_back(&mut self) -> Option<A> {
1118        if self.is_empty() {
1119            return None;
1120        }
1121        let is_iterating = self.start < self.end;
1122        Some(if is_iterating {
1123            let n =
1124                Step::backward_checked(self.end.clone(), 1).expect("`Step` invariants not upheld");
1125            mem::replace(&mut self.end, n)
1126        } else {
1127            self.exhausted = true;
1128            self.end.clone()
1129        })
1130    }
1131
1132    #[inline]
1133    default fn spec_try_rfold<B, F, R>(&mut self, init: B, mut f: F) -> R
1134    where
1135        Self: Sized,
1136        F: FnMut(B, A) -> R,
1137        R: Try<Output = B>,
1138    {
1139        if self.is_empty() {
1140            return try { init };
1141        }
1142
1143        let mut accum = init;
1144
1145        while self.start < self.end {
1146            let n =
1147                Step::backward_checked(self.end.clone(), 1).expect("`Step` invariants not upheld");
1148            let n = mem::replace(&mut self.end, n);
1149            accum = f(accum, n)?;
1150        }
1151
1152        self.exhausted = true;
1153
1154        if self.start == self.end {
1155            accum = f(accum, self.start.clone())?;
1156        }
1157
1158        try { accum }
1159    }
1160}
1161
1162impl<T: TrustedStep> RangeInclusiveIteratorImpl for ops::RangeInclusive<T> {
1163    #[inline]
1164    fn spec_next(&mut self) -> Option<T> {
1165        if self.is_empty() {
1166            return None;
1167        }
1168        let is_iterating = self.start < self.end;
1169        Some(if is_iterating {
1170            // SAFETY: just checked precondition
1171            let n = unsafe { Step::forward_unchecked(self.start, 1) };
1172            mem::replace(&mut self.start, n)
1173        } else {
1174            self.exhausted = true;
1175            self.start
1176        })
1177    }
1178
1179    #[inline]
1180    fn spec_try_fold<B, F, R>(&mut self, init: B, mut f: F) -> R
1181    where
1182        Self: Sized,
1183        F: FnMut(B, T) -> R,
1184        R: Try<Output = B>,
1185    {
1186        if self.is_empty() {
1187            return try { init };
1188        }
1189
1190        let mut accum = init;
1191
1192        while self.start < self.end {
1193            // SAFETY: just checked precondition
1194            let n = unsafe { Step::forward_unchecked(self.start, 1) };
1195            let n = mem::replace(&mut self.start, n);
1196            accum = f(accum, n)?;
1197        }
1198
1199        self.exhausted = true;
1200
1201        if self.start == self.end {
1202            accum = f(accum, self.start)?;
1203        }
1204
1205        try { accum }
1206    }
1207
1208    #[inline]
1209    fn spec_next_back(&mut self) -> Option<T> {
1210        if self.is_empty() {
1211            return None;
1212        }
1213        let is_iterating = self.start < self.end;
1214        Some(if is_iterating {
1215            // SAFETY: just checked precondition
1216            let n = unsafe { Step::backward_unchecked(self.end, 1) };
1217            mem::replace(&mut self.end, n)
1218        } else {
1219            self.exhausted = true;
1220            self.end
1221        })
1222    }
1223
1224    #[inline]
1225    fn spec_try_rfold<B, F, R>(&mut self, init: B, mut f: F) -> R
1226    where
1227        Self: Sized,
1228        F: FnMut(B, T) -> R,
1229        R: Try<Output = B>,
1230    {
1231        if self.is_empty() {
1232            return try { init };
1233        }
1234
1235        let mut accum = init;
1236
1237        while self.start < self.end {
1238            // SAFETY: just checked precondition
1239            let n = unsafe { Step::backward_unchecked(self.end, 1) };
1240            let n = mem::replace(&mut self.end, n);
1241            accum = f(accum, n)?;
1242        }
1243
1244        self.exhausted = true;
1245
1246        if self.start == self.end {
1247            accum = f(accum, self.start)?;
1248        }
1249
1250        try { accum }
1251    }
1252}
1253
1254#[stable(feature = "inclusive_range", since = "1.26.0")]
1255impl<A: Step> Iterator for ops::RangeInclusive<A> {
1256    type Item = A;
1257
1258    #[inline]
1259    fn next(&mut self) -> Option<A> {
1260        self.spec_next()
1261    }
1262
1263    #[inline]
1264    fn size_hint(&self) -> (usize, Option<usize>) {
1265        if self.is_empty() {
1266            return (0, Some(0));
1267        }
1268
1269        let hint = Step::steps_between(&self.start, &self.end);
1270        (hint.0.saturating_add(1), hint.1.and_then(|steps| steps.checked_add(1)))
1271    }
1272
1273    #[inline]
1274    fn count(self) -> usize {
1275        if self.is_empty() {
1276            return 0;
1277        }
1278
1279        Step::steps_between(&self.start, &self.end)
1280            .1
1281            .and_then(|steps| steps.checked_add(1))
1282            .expect("count overflowed usize")
1283    }
1284
1285    #[inline]
1286    fn nth(&mut self, n: usize) -> Option<A> {
1287        if self.is_empty() {
1288            return None;
1289        }
1290
1291        if let Some(plus_n) = Step::forward_checked(self.start.clone(), n) {
1292            use crate::cmp::Ordering::*;
1293
1294            match plus_n.partial_cmp(&self.end) {
1295                Some(Less) => {
1296                    self.start = Step::forward(plus_n.clone(), 1);
1297                    return Some(plus_n);
1298                }
1299                Some(Equal) => {
1300                    self.start = plus_n.clone();
1301                    self.exhausted = true;
1302                    return Some(plus_n);
1303                }
1304                _ => {}
1305            }
1306        }
1307
1308        self.start = self.end.clone();
1309        self.exhausted = true;
1310        None
1311    }
1312
1313    #[inline]
1314    fn try_fold<B, F, R>(&mut self, init: B, f: F) -> R
1315    where
1316        Self: Sized,
1317        F: FnMut(B, Self::Item) -> R,
1318        R: Try<Output = B>,
1319    {
1320        self.spec_try_fold(init, f)
1321    }
1322
1323    impl_fold_via_try_fold! { fold -> try_fold }
1324
1325    #[inline]
1326    fn last(mut self) -> Option<A> {
1327        self.next_back()
1328    }
1329
1330    #[inline]
1331    fn min(mut self) -> Option<A>
1332    where
1333        A: Ord,
1334    {
1335        self.next()
1336    }
1337
1338    #[inline]
1339    fn max(mut self) -> Option<A>
1340    where
1341        A: Ord,
1342    {
1343        self.next_back()
1344    }
1345
1346    #[inline]
1347    fn is_sorted(self) -> bool {
1348        true
1349    }
1350}
1351
1352#[stable(feature = "inclusive_range", since = "1.26.0")]
1353impl<A: Step> DoubleEndedIterator for ops::RangeInclusive<A> {
1354    #[inline]
1355    fn next_back(&mut self) -> Option<A> {
1356        self.spec_next_back()
1357    }
1358
1359    #[inline]
1360    fn nth_back(&mut self, n: usize) -> Option<A> {
1361        if self.is_empty() {
1362            return None;
1363        }
1364
1365        if let Some(minus_n) = Step::backward_checked(self.end.clone(), n) {
1366            use crate::cmp::Ordering::*;
1367
1368            match minus_n.partial_cmp(&self.start) {
1369                Some(Greater) => {
1370                    self.end = Step::backward(minus_n.clone(), 1);
1371                    return Some(minus_n);
1372                }
1373                Some(Equal) => {
1374                    self.end = minus_n.clone();
1375                    self.exhausted = true;
1376                    return Some(minus_n);
1377                }
1378                _ => {}
1379            }
1380        }
1381
1382        self.end = self.start.clone();
1383        self.exhausted = true;
1384        None
1385    }
1386
1387    #[inline]
1388    fn try_rfold<B, F, R>(&mut self, init: B, f: F) -> R
1389    where
1390        Self: Sized,
1391        F: FnMut(B, Self::Item) -> R,
1392        R: Try<Output = B>,
1393    {
1394        self.spec_try_rfold(init, f)
1395    }
1396
1397    impl_fold_via_try_fold! { rfold -> try_rfold }
1398}
1399
1400// Safety: See above implementation for `ops::Range<A>`
1401#[unstable(feature = "trusted_len", issue = "37572")]
1402unsafe impl<A: TrustedStep> TrustedLen for ops::RangeInclusive<A> {}
1403
1404#[stable(feature = "fused", since = "1.26.0")]
1405impl<A: Step> FusedIterator for ops::RangeInclusive<A> {}
```