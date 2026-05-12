---
title: bit.rs - source
url: https://doc.rust-lang.org/src/core/ops/bit.rs.html#830
source: crawler
fetched_at: 2026-05-06T21:29:57.686645292-03:00
rendered_js: false
word_count: 3541
summary: This document defines the core Rust traits for bitwise and logical operators, specifically Not, BitAnd, and BitOr, providing the interfaces required to implement these operations for custom types.
tags:
    - rust
    - bitwise-operators
    - logical-operators
    - traits
    - operator-overloading
    - standard-library
category: reference
---

## core/ops/ bit.rs

````rust
1/// The unary logical negation operator `!`.
2///
3/// # Examples
4///
5/// An implementation of `Not` for `Answer`, which enables the use of `!` to
6/// invert its value.
7///
8/// ```
9/// use std::ops::Not;
10///
11/// #[derive(Debug, PartialEq)]
12/// enum Answer {
13///     Yes,
14///     No,
15/// }
16///
17/// impl Not for Answer {
18///     type Output = Self;
19///
20///     fn not(self) -> Self::Output {
21///         match self {
22///             Answer::Yes => Answer::No,
23///             Answer::No => Answer::Yes
24///         }
25///     }
26/// }
27///
28/// assert_eq!(!Answer::Yes, Answer::No);
29/// assert_eq!(!Answer::No, Answer::Yes);
30/// ```
31#[lang = "not"]
32#[stable(feature = "rust1", since = "1.0.0")]
33#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
34#[doc(alias = "!")]
35pub const trait Not {
36    /// The resulting type after applying the `!` operator.
37    #[stable(feature = "rust1", since = "1.0.0")]
38    type Output;
39
40    /// Performs the unary `!` operation.
41    ///
42    /// # Examples
43    ///
44    /// ```
45    /// assert_eq!(!true, false);
46    /// assert_eq!(!false, true);
47    /// assert_eq!(!1u8, 254);
48    /// assert_eq!(!0u8, 255);
49    /// ```
50    #[must_use]
51    #[stable(feature = "rust1", since = "1.0.0")]
52    fn not(self) -> Self::Output;
53}
54
55macro_rules! not_impl {
56    ($($t:ty)*) => ($(
57        #[stable(feature = "rust1", since = "1.0.0")]
58        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
59        impl const Not for $t {
60            type Output = $t;
61
62            #[inline]
63            fn not(self) -> $t { !self }
64        }
65
66        forward_ref_unop! { impl Not, not for $t,
67        #[stable(feature = "rust1", since = "1.0.0")]
68        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
69    )*)
70}
71
72not_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
73
74#[stable(feature = "not_never", since = "1.60.0")]
75#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
76impl const Not for ! {
77    type Output = !;
78
79    #[inline]
80    fn not(self) -> ! {
81        match self {}
82    }
83}
84
85/// The bitwise AND operator `&`.
86///
87/// Note that `Rhs` is `Self` by default, but this is not mandatory.
88///
89/// # Examples
90///
91/// An implementation of `BitAnd` for a wrapper around `bool`.
92///
93/// ```
94/// use std::ops::BitAnd;
95///
96/// #[derive(Debug, PartialEq)]
97/// struct Scalar(bool);
98///
99/// impl BitAnd for Scalar {
100///     type Output = Self;
101///
102///     // rhs is the "right-hand side" of the expression `a & b`
103///     fn bitand(self, rhs: Self) -> Self::Output {
104///         Self(self.0 & rhs.0)
105///     }
106/// }
107///
108/// assert_eq!(Scalar(true) & Scalar(true), Scalar(true));
109/// assert_eq!(Scalar(true) & Scalar(false), Scalar(false));
110/// assert_eq!(Scalar(false) & Scalar(true), Scalar(false));
111/// assert_eq!(Scalar(false) & Scalar(false), Scalar(false));
112/// ```
113///
114/// An implementation of `BitAnd` for a wrapper around `Vec<bool>`.
115///
116/// ```
117/// use std::ops::BitAnd;
118///
119/// #[derive(Debug, PartialEq)]
120/// struct BooleanVector(Vec<bool>);
121///
122/// impl BitAnd for BooleanVector {
123///     type Output = Self;
124///
125///     fn bitand(self, Self(rhs): Self) -> Self::Output {
126///         let Self(lhs) = self;
127///         assert_eq!(lhs.len(), rhs.len());
128///         Self(
129///             lhs.iter()
130///                 .zip(rhs.iter())
131///                 .map(|(x, y)| *x & *y)
132///                 .collect()
133///         )
134///     }
135/// }
136///
137/// let bv1 = BooleanVector(vec![true, true, false, false]);
138/// let bv2 = BooleanVector(vec![true, false, true, false]);
139/// let expected = BooleanVector(vec![true, false, false, false]);
140/// assert_eq!(bv1 & bv2, expected);
141/// ```
142#[lang = "bitand"]
143#[doc(alias = "&")]
144#[stable(feature = "rust1", since = "1.0.0")]
145#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
146#[diagnostic::on_unimplemented(
147    message = "no implementation for `{Self} & {Rhs}`",
148    label = "no implementation for `{Self} & {Rhs}`"
149)]
150pub const trait BitAnd<Rhs = Self> {
151    /// The resulting type after applying the `&` operator.
152    #[stable(feature = "rust1", since = "1.0.0")]
153    type Output;
154
155    /// Performs the `&` operation.
156    ///
157    /// # Examples
158    ///
159    /// ```
160    /// assert_eq!(true & false, false);
161    /// assert_eq!(true & true, true);
162    /// assert_eq!(5u8 & 1u8, 1);
163    /// assert_eq!(5u8 & 2u8, 0);
164    /// ```
165    #[must_use]
166    #[stable(feature = "rust1", since = "1.0.0")]
167    fn bitand(self, rhs: Rhs) -> Self::Output;
168}
169
170macro_rules! bitand_impl {
171    ($($t:ty)*) => ($(
172        #[stable(feature = "rust1", since = "1.0.0")]
173        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
174        impl const BitAnd for $t {
175            type Output = $t;
176
177            #[inline]
178            fn bitand(self, rhs: $t) -> $t { self & rhs }
179        }
180
181        forward_ref_binop! { impl BitAnd, bitand for $t, $t,
182        #[stable(feature = "rust1", since = "1.0.0")]
183        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
184    )*)
185}
186
187bitand_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
188
189/// The bitwise OR operator `|`.
190///
191/// Note that `Rhs` is `Self` by default, but this is not mandatory.
192///
193/// # Examples
194///
195/// An implementation of `BitOr` for a wrapper around `bool`.
196///
197/// ```
198/// use std::ops::BitOr;
199///
200/// #[derive(Debug, PartialEq)]
201/// struct Scalar(bool);
202///
203/// impl BitOr for Scalar {
204///     type Output = Self;
205///
206///     // rhs is the "right-hand side" of the expression `a | b`
207///     fn bitor(self, rhs: Self) -> Self::Output {
208///         Self(self.0 | rhs.0)
209///     }
210/// }
211///
212/// assert_eq!(Scalar(true) | Scalar(true), Scalar(true));
213/// assert_eq!(Scalar(true) | Scalar(false), Scalar(true));
214/// assert_eq!(Scalar(false) | Scalar(true), Scalar(true));
215/// assert_eq!(Scalar(false) | Scalar(false), Scalar(false));
216/// ```
217///
218/// An implementation of `BitOr` for a wrapper around `Vec<bool>`.
219///
220/// ```
221/// use std::ops::BitOr;
222///
223/// #[derive(Debug, PartialEq)]
224/// struct BooleanVector(Vec<bool>);
225///
226/// impl BitOr for BooleanVector {
227///     type Output = Self;
228///
229///     fn bitor(self, Self(rhs): Self) -> Self::Output {
230///         let Self(lhs) = self;
231///         assert_eq!(lhs.len(), rhs.len());
232///         Self(
233///             lhs.iter()
234///                 .zip(rhs.iter())
235///                 .map(|(x, y)| *x | *y)
236///                 .collect()
237///         )
238///     }
239/// }
240///
241/// let bv1 = BooleanVector(vec![true, true, false, false]);
242/// let bv2 = BooleanVector(vec![true, false, true, false]);
243/// let expected = BooleanVector(vec![true, true, true, false]);
244/// assert_eq!(bv1 | bv2, expected);
245/// ```
246#[lang = "bitor"]
247#[doc(alias = "|")]
248#[stable(feature = "rust1", since = "1.0.0")]
249#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
250#[diagnostic::on_unimplemented(
251    message = "no implementation for `{Self} | {Rhs}`",
252    label = "no implementation for `{Self} | {Rhs}`"
253)]
254pub const trait BitOr<Rhs = Self> {
255    /// The resulting type after applying the `|` operator.
256    #[stable(feature = "rust1", since = "1.0.0")]
257    type Output;
258
259    /// Performs the `|` operation.
260    ///
261    /// # Examples
262    ///
263    /// ```
264    /// assert_eq!(true | false, true);
265    /// assert_eq!(false | false, false);
266    /// assert_eq!(5u8 | 1u8, 5);
267    /// assert_eq!(5u8 | 2u8, 7);
268    /// ```
269    #[must_use]
270    #[stable(feature = "rust1", since = "1.0.0")]
271    fn bitor(self, rhs: Rhs) -> Self::Output;
272}
273
274macro_rules! bitor_impl {
275    ($($t:ty)*) => ($(
276        #[stable(feature = "rust1", since = "1.0.0")]
277        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
278        impl const BitOr for $t {
279            type Output = $t;
280
281            #[inline]
282            fn bitor(self, rhs: $t) -> $t { self | rhs }
283        }
284
285        forward_ref_binop! { impl BitOr, bitor for $t, $t,
286        #[stable(feature = "rust1", since = "1.0.0")]
287        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
288    )*)
289}
290
291bitor_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
292
293/// The bitwise XOR operator `^`.
294///
295/// Note that `Rhs` is `Self` by default, but this is not mandatory.
296///
297/// # Examples
298///
299/// An implementation of `BitXor` that lifts `^` to a wrapper around `bool`.
300///
301/// ```
302/// use std::ops::BitXor;
303///
304/// #[derive(Debug, PartialEq)]
305/// struct Scalar(bool);
306///
307/// impl BitXor for Scalar {
308///     type Output = Self;
309///
310///     // rhs is the "right-hand side" of the expression `a ^ b`
311///     fn bitxor(self, rhs: Self) -> Self::Output {
312///         Self(self.0 ^ rhs.0)
313///     }
314/// }
315///
316/// assert_eq!(Scalar(true) ^ Scalar(true), Scalar(false));
317/// assert_eq!(Scalar(true) ^ Scalar(false), Scalar(true));
318/// assert_eq!(Scalar(false) ^ Scalar(true), Scalar(true));
319/// assert_eq!(Scalar(false) ^ Scalar(false), Scalar(false));
320/// ```
321///
322/// An implementation of `BitXor` trait for a wrapper around `Vec<bool>`.
323///
324/// ```
325/// use std::ops::BitXor;
326///
327/// #[derive(Debug, PartialEq)]
328/// struct BooleanVector(Vec<bool>);
329///
330/// impl BitXor for BooleanVector {
331///     type Output = Self;
332///
333///     fn bitxor(self, Self(rhs): Self) -> Self::Output {
334///         let Self(lhs) = self;
335///         assert_eq!(lhs.len(), rhs.len());
336///         Self(
337///             lhs.iter()
338///                 .zip(rhs.iter())
339///                 .map(|(x, y)| *x ^ *y)
340///                 .collect()
341///         )
342///     }
343/// }
344///
345/// let bv1 = BooleanVector(vec![true, true, false, false]);
346/// let bv2 = BooleanVector(vec![true, false, true, false]);
347/// let expected = BooleanVector(vec![false, true, true, false]);
348/// assert_eq!(bv1 ^ bv2, expected);
349/// ```
350#[lang = "bitxor"]
351#[doc(alias = "^")]
352#[stable(feature = "rust1", since = "1.0.0")]
353#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
354#[diagnostic::on_unimplemented(
355    message = "no implementation for `{Self} ^ {Rhs}`",
356    label = "no implementation for `{Self} ^ {Rhs}`"
357)]
358pub const trait BitXor<Rhs = Self> {
359    /// The resulting type after applying the `^` operator.
360    #[stable(feature = "rust1", since = "1.0.0")]
361    type Output;
362
363    /// Performs the `^` operation.
364    ///
365    /// # Examples
366    ///
367    /// ```
368    /// assert_eq!(true ^ false, true);
369    /// assert_eq!(true ^ true, false);
370    /// assert_eq!(5u8 ^ 1u8, 4);
371    /// assert_eq!(5u8 ^ 2u8, 7);
372    /// ```
373    #[must_use]
374    #[stable(feature = "rust1", since = "1.0.0")]
375    fn bitxor(self, rhs: Rhs) -> Self::Output;
376}
377
378macro_rules! bitxor_impl {
379    ($($t:ty)*) => ($(
380        #[stable(feature = "rust1", since = "1.0.0")]
381        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
382        impl const BitXor for $t {
383            type Output = $t;
384
385            #[inline]
386            fn bitxor(self, other: $t) -> $t { self ^ other }
387        }
388
389        forward_ref_binop! { impl BitXor, bitxor for $t, $t,
390        #[stable(feature = "rust1", since = "1.0.0")]
391        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
392    )*)
393}
394
395bitxor_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
396
397/// The left shift operator `<<`. Note that because this trait is implemented
398/// for all integer types with multiple right-hand-side types, Rust's type
399/// checker has special handling for `_ << _`, setting the result type for
400/// integer operations to the type of the left-hand-side operand. This means
401/// that though `a << b` and `a.shl(b)` are one and the same from an evaluation
402/// standpoint, they are different when it comes to type inference.
403///
404/// # Examples
405///
406/// An implementation of `Shl` that lifts the `<<` operation on integers to a
407/// wrapper around `usize`.
408///
409/// ```
410/// use std::ops::Shl;
411///
412/// #[derive(PartialEq, Debug)]
413/// struct Scalar(usize);
414///
415/// impl Shl<Scalar> for Scalar {
416///     type Output = Self;
417///
418///     fn shl(self, Self(rhs): Self) -> Self::Output {
419///         let Self(lhs) = self;
420///         Self(lhs << rhs)
421///     }
422/// }
423///
424/// assert_eq!(Scalar(4) << Scalar(2), Scalar(16));
425/// ```
426///
427/// An implementation of `Shl` that spins a vector leftward by a given amount.
428///
429/// ```
430/// use std::ops::Shl;
431///
432/// #[derive(PartialEq, Debug)]
433/// struct SpinVector<T: Clone> {
434///     vec: Vec<T>,
435/// }
436///
437/// impl<T: Clone> Shl<usize> for SpinVector<T> {
438///     type Output = Self;
439///
440///     fn shl(self, rhs: usize) -> Self::Output {
441///         // Rotate the vector by `rhs` places.
442///         let (a, b) = self.vec.split_at(rhs);
443///         let mut spun_vector = vec![];
444///         spun_vector.extend_from_slice(b);
445///         spun_vector.extend_from_slice(a);
446///         Self { vec: spun_vector }
447///     }
448/// }
449///
450/// assert_eq!(SpinVector { vec: vec![0, 1, 2, 3, 4] } << 2,
451///            SpinVector { vec: vec![2, 3, 4, 0, 1] });
452/// ```
453#[lang = "shl"]
454#[doc(alias = "<<")]
455#[stable(feature = "rust1", since = "1.0.0")]
456#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
457#[diagnostic::on_unimplemented(
458    message = "no implementation for `{Self} << {Rhs}`",
459    label = "no implementation for `{Self} << {Rhs}`"
460)]
461pub const trait Shl<Rhs = Self> {
462    /// The resulting type after applying the `<<` operator.
463    #[stable(feature = "rust1", since = "1.0.0")]
464    type Output;
465
466    /// Performs the `<<` operation.
467    ///
468    /// # Examples
469    ///
470    /// ```
471    /// assert_eq!(5u8 << 1, 10);
472    /// assert_eq!(1u8 << 1, 2);
473    /// ```
474    #[must_use]
475    #[stable(feature = "rust1", since = "1.0.0")]
476    fn shl(self, rhs: Rhs) -> Self::Output;
477}
478
479macro_rules! shl_impl {
480    ($t:ty, $f:ty) => {
481        #[stable(feature = "rust1", since = "1.0.0")]
482        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
483        impl const Shl<$f> for $t {
484            type Output = $t;
485
486            #[inline]
487            #[rustc_inherit_overflow_checks]
488            fn shl(self, other: $f) -> $t {
489                self << other
490            }
491        }
492
493        forward_ref_binop! { impl Shl, shl for $t, $f,
494        #[stable(feature = "rust1", since = "1.0.0")]
495        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
496    };
497}
498
499macro_rules! shl_impl_all {
500    ($($t:ty)*) => ($(
501        shl_impl! { $t, u8 }
502        shl_impl! { $t, u16 }
503        shl_impl! { $t, u32 }
504        shl_impl! { $t, u64 }
505        shl_impl! { $t, u128 }
506        shl_impl! { $t, usize }
507
508        shl_impl! { $t, i8 }
509        shl_impl! { $t, i16 }
510        shl_impl! { $t, i32 }
511        shl_impl! { $t, i64 }
512        shl_impl! { $t, i128 }
513        shl_impl! { $t, isize }
514    )*)
515}
516
517shl_impl_all! { u8 u16 u32 u64 u128 usize i8 i16 i32 i64 i128 isize }
518
519/// The right shift operator `>>`. Note that because this trait is implemented
520/// for all integer types with multiple right-hand-side types, Rust's type
521/// checker has special handling for `_ >> _`, setting the result type for
522/// integer operations to the type of the left-hand-side operand. This means
523/// that though `a >> b` and `a.shr(b)` are one and the same from an evaluation
524/// standpoint, they are different when it comes to type inference.
525///
526/// # Examples
527///
528/// An implementation of `Shr` that lifts the `>>` operation on integers to a
529/// wrapper around `usize`.
530///
531/// ```
532/// use std::ops::Shr;
533///
534/// #[derive(PartialEq, Debug)]
535/// struct Scalar(usize);
536///
537/// impl Shr<Scalar> for Scalar {
538///     type Output = Self;
539///
540///     fn shr(self, Self(rhs): Self) -> Self::Output {
541///         let Self(lhs) = self;
542///         Self(lhs >> rhs)
543///     }
544/// }
545///
546/// assert_eq!(Scalar(16) >> Scalar(2), Scalar(4));
547/// ```
548///
549/// An implementation of `Shr` that spins a vector rightward by a given amount.
550///
551/// ```
552/// use std::ops::Shr;
553///
554/// #[derive(PartialEq, Debug)]
555/// struct SpinVector<T: Clone> {
556///     vec: Vec<T>,
557/// }
558///
559/// impl<T: Clone> Shr<usize> for SpinVector<T> {
560///     type Output = Self;
561///
562///     fn shr(self, rhs: usize) -> Self::Output {
563///         // Rotate the vector by `rhs` places.
564///         let (a, b) = self.vec.split_at(self.vec.len() - rhs);
565///         let mut spun_vector = vec![];
566///         spun_vector.extend_from_slice(b);
567///         spun_vector.extend_from_slice(a);
568///         Self { vec: spun_vector }
569///     }
570/// }
571///
572/// assert_eq!(SpinVector { vec: vec![0, 1, 2, 3, 4] } >> 2,
573///            SpinVector { vec: vec![3, 4, 0, 1, 2] });
574/// ```
575#[lang = "shr"]
576#[doc(alias = ">>")]
577#[stable(feature = "rust1", since = "1.0.0")]
578#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
579#[diagnostic::on_unimplemented(
580    message = "no implementation for `{Self} >> {Rhs}`",
581    label = "no implementation for `{Self} >> {Rhs}`"
582)]
583pub const trait Shr<Rhs = Self> {
584    /// The resulting type after applying the `>>` operator.
585    #[stable(feature = "rust1", since = "1.0.0")]
586    type Output;
587
588    /// Performs the `>>` operation.
589    ///
590    /// # Examples
591    ///
592    /// ```
593    /// assert_eq!(5u8 >> 1, 2);
594    /// assert_eq!(2u8 >> 1, 1);
595    /// ```
596    #[must_use]
597    #[stable(feature = "rust1", since = "1.0.0")]
598    fn shr(self, rhs: Rhs) -> Self::Output;
599}
600
601macro_rules! shr_impl {
602    ($t:ty, $f:ty) => {
603        #[stable(feature = "rust1", since = "1.0.0")]
604        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
605        impl const Shr<$f> for $t {
606            type Output = $t;
607
608            #[inline]
609            #[rustc_inherit_overflow_checks]
610            fn shr(self, other: $f) -> $t {
611                self >> other
612            }
613        }
614
615        forward_ref_binop! { impl Shr, shr for $t, $f,
616        #[stable(feature = "rust1", since = "1.0.0")]
617        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
618    };
619}
620
621macro_rules! shr_impl_all {
622    ($($t:ty)*) => ($(
623        shr_impl! { $t, u8 }
624        shr_impl! { $t, u16 }
625        shr_impl! { $t, u32 }
626        shr_impl! { $t, u64 }
627        shr_impl! { $t, u128 }
628        shr_impl! { $t, usize }
629
630        shr_impl! { $t, i8 }
631        shr_impl! { $t, i16 }
632        shr_impl! { $t, i32 }
633        shr_impl! { $t, i64 }
634        shr_impl! { $t, i128 }
635        shr_impl! { $t, isize }
636    )*)
637}
638
639shr_impl_all! { u8 u16 u32 u64 u128 usize i8 i16 i32 i64 i128 isize }
640
641/// The bitwise AND assignment operator `&=`.
642///
643/// # Examples
644///
645/// An implementation of `BitAndAssign` that lifts the `&=` operator to a
646/// wrapper around `bool`.
647///
648/// ```
649/// use std::ops::BitAndAssign;
650///
651/// #[derive(Debug, PartialEq)]
652/// struct Scalar(bool);
653///
654/// impl BitAndAssign for Scalar {
655///     // rhs is the "right-hand side" of the expression `a &= b`
656///     fn bitand_assign(&mut self, rhs: Self) {
657///         *self = Self(self.0 & rhs.0)
658///     }
659/// }
660///
661/// let mut scalar = Scalar(true);
662/// scalar &= Scalar(true);
663/// assert_eq!(scalar, Scalar(true));
664///
665/// let mut scalar = Scalar(true);
666/// scalar &= Scalar(false);
667/// assert_eq!(scalar, Scalar(false));
668///
669/// let mut scalar = Scalar(false);
670/// scalar &= Scalar(true);
671/// assert_eq!(scalar, Scalar(false));
672///
673/// let mut scalar = Scalar(false);
674/// scalar &= Scalar(false);
675/// assert_eq!(scalar, Scalar(false));
676/// ```
677///
678/// Here, the `BitAndAssign` trait is implemented for a wrapper around
679/// `Vec<bool>`.
680///
681/// ```
682/// use std::ops::BitAndAssign;
683///
684/// #[derive(Debug, PartialEq)]
685/// struct BooleanVector(Vec<bool>);
686///
687/// impl BitAndAssign for BooleanVector {
688///     // `rhs` is the "right-hand side" of the expression `a &= b`.
689///     fn bitand_assign(&mut self, rhs: Self) {
690///         assert_eq!(self.0.len(), rhs.0.len());
691///         *self = Self(
692///             self.0
693///                 .iter()
694///                 .zip(rhs.0.iter())
695///                 .map(|(x, y)| *x & *y)
696///                 .collect()
697///         );
698///     }
699/// }
700///
701/// let mut bv = BooleanVector(vec![true, true, false, false]);
702/// bv &= BooleanVector(vec![true, false, true, false]);
703/// let expected = BooleanVector(vec![true, false, false, false]);
704/// assert_eq!(bv, expected);
705/// ```
706#[lang = "bitand_assign"]
707#[doc(alias = "&=")]
708#[stable(feature = "op_assign_traits", since = "1.8.0")]
709#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
710#[diagnostic::on_unimplemented(
711    message = "no implementation for `{Self} &= {Rhs}`",
712    label = "no implementation for `{Self} &= {Rhs}`"
713)]
714pub const trait BitAndAssign<Rhs = Self> {
715    /// Performs the `&=` operation.
716    ///
717    /// # Examples
718    ///
719    /// ```
720    /// let mut x = true;
721    /// x &= false;
722    /// assert_eq!(x, false);
723    ///
724    /// let mut x = true;
725    /// x &= true;
726    /// assert_eq!(x, true);
727    ///
728    /// let mut x: u8 = 5;
729    /// x &= 1;
730    /// assert_eq!(x, 1);
731    ///
732    /// let mut x: u8 = 5;
733    /// x &= 2;
734    /// assert_eq!(x, 0);
735    /// ```
736    #[stable(feature = "op_assign_traits", since = "1.8.0")]
737    fn bitand_assign(&mut self, rhs: Rhs);
738}
739
740macro_rules! bitand_assign_impl {
741    ($($t:ty)+) => ($(
742        #[stable(feature = "op_assign_traits", since = "1.8.0")]
743        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
744        impl const BitAndAssign for $t {
745            #[inline]
746            fn bitand_assign(&mut self, other: $t) { *self &= other }
747        }
748
749        forward_ref_op_assign! { impl BitAndAssign, bitand_assign for $t, $t,
750        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
751        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
752    )+)
753}
754
755bitand_assign_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
756
757/// The bitwise OR assignment operator `|=`.
758///
759/// # Examples
760///
761/// ```
762/// use std::ops::BitOrAssign;
763///
764/// #[derive(Debug, PartialEq)]
765/// struct PersonalPreferences {
766///     likes_cats: bool,
767///     likes_dogs: bool,
768/// }
769///
770/// impl BitOrAssign for PersonalPreferences {
771///     fn bitor_assign(&mut self, rhs: Self) {
772///         self.likes_cats |= rhs.likes_cats;
773///         self.likes_dogs |= rhs.likes_dogs;
774///     }
775/// }
776///
777/// let mut prefs = PersonalPreferences { likes_cats: true, likes_dogs: false };
778/// prefs |= PersonalPreferences { likes_cats: false, likes_dogs: true };
779/// assert_eq!(prefs, PersonalPreferences { likes_cats: true, likes_dogs: true });
780/// ```
781#[lang = "bitor_assign"]
782#[doc(alias = "|=")]
783#[stable(feature = "op_assign_traits", since = "1.8.0")]
784#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
785#[diagnostic::on_unimplemented(
786    message = "no implementation for `{Self} |= {Rhs}`",
787    label = "no implementation for `{Self} |= {Rhs}`"
788)]
789pub const trait BitOrAssign<Rhs = Self> {
790    /// Performs the `|=` operation.
791    ///
792    /// # Examples
793    ///
794    /// ```
795    /// let mut x = true;
796    /// x |= false;
797    /// assert_eq!(x, true);
798    ///
799    /// let mut x = false;
800    /// x |= false;
801    /// assert_eq!(x, false);
802    ///
803    /// let mut x: u8 = 5;
804    /// x |= 1;
805    /// assert_eq!(x, 5);
806    ///
807    /// let mut x: u8 = 5;
808    /// x |= 2;
809    /// assert_eq!(x, 7);
810    /// ```
811    #[stable(feature = "op_assign_traits", since = "1.8.0")]
812    fn bitor_assign(&mut self, rhs: Rhs);
813}
814
815macro_rules! bitor_assign_impl {
816    ($($t:ty)+) => ($(
817        #[stable(feature = "op_assign_traits", since = "1.8.0")]
818        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
819        impl const BitOrAssign for $t {
820            #[inline]
821            fn bitor_assign(&mut self, other: $t) { *self |= other }
822        }
823
824        forward_ref_op_assign! { impl BitOrAssign, bitor_assign for $t, $t,
825        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
826        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
827    )+)
828}
829
830bitor_assign_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
831
832/// The bitwise XOR assignment operator `^=`.
833///
834/// # Examples
835///
836/// ```
837/// use std::ops::BitXorAssign;
838///
839/// #[derive(Debug, PartialEq)]
840/// struct Personality {
841///     has_soul: bool,
842///     likes_knitting: bool,
843/// }
844///
845/// impl BitXorAssign for Personality {
846///     fn bitxor_assign(&mut self, rhs: Self) {
847///         self.has_soul ^= rhs.has_soul;
848///         self.likes_knitting ^= rhs.likes_knitting;
849///     }
850/// }
851///
852/// let mut personality = Personality { has_soul: false, likes_knitting: true };
853/// personality ^= Personality { has_soul: true, likes_knitting: true };
854/// assert_eq!(personality, Personality { has_soul: true, likes_knitting: false});
855/// ```
856#[lang = "bitxor_assign"]
857#[doc(alias = "^=")]
858#[stable(feature = "op_assign_traits", since = "1.8.0")]
859#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
860#[diagnostic::on_unimplemented(
861    message = "no implementation for `{Self} ^= {Rhs}`",
862    label = "no implementation for `{Self} ^= {Rhs}`"
863)]
864pub const trait BitXorAssign<Rhs = Self> {
865    /// Performs the `^=` operation.
866    ///
867    /// # Examples
868    ///
869    /// ```
870    /// let mut x = true;
871    /// x ^= false;
872    /// assert_eq!(x, true);
873    ///
874    /// let mut x = true;
875    /// x ^= true;
876    /// assert_eq!(x, false);
877    ///
878    /// let mut x: u8 = 5;
879    /// x ^= 1;
880    /// assert_eq!(x, 4);
881    ///
882    /// let mut x: u8 = 5;
883    /// x ^= 2;
884    /// assert_eq!(x, 7);
885    /// ```
886    #[stable(feature = "op_assign_traits", since = "1.8.0")]
887    fn bitxor_assign(&mut self, rhs: Rhs);
888}
889
890macro_rules! bitxor_assign_impl {
891    ($($t:ty)+) => ($(
892        #[stable(feature = "op_assign_traits", since = "1.8.0")]
893        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
894        impl const BitXorAssign for $t {
895            #[inline]
896            fn bitxor_assign(&mut self, other: $t) { *self ^= other }
897        }
898
899        forward_ref_op_assign! { impl BitXorAssign, bitxor_assign for $t, $t,
900        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
901        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
902    )+)
903}
904
905bitxor_assign_impl! { bool usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
906
907/// The left shift assignment operator `<<=`.
908///
909/// # Examples
910///
911/// An implementation of `ShlAssign` for a wrapper around `usize`.
912///
913/// ```
914/// use std::ops::ShlAssign;
915///
916/// #[derive(Debug, PartialEq)]
917/// struct Scalar(usize);
918///
919/// impl ShlAssign<usize> for Scalar {
920///     fn shl_assign(&mut self, rhs: usize) {
921///         self.0 <<= rhs;
922///     }
923/// }
924///
925/// let mut scalar = Scalar(4);
926/// scalar <<= 2;
927/// assert_eq!(scalar, Scalar(16));
928/// ```
929#[lang = "shl_assign"]
930#[doc(alias = "<<=")]
931#[stable(feature = "op_assign_traits", since = "1.8.0")]
932#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
933#[diagnostic::on_unimplemented(
934    message = "no implementation for `{Self} <<= {Rhs}`",
935    label = "no implementation for `{Self} <<= {Rhs}`"
936)]
937pub const trait ShlAssign<Rhs = Self> {
938    /// Performs the `<<=` operation.
939    ///
940    /// # Examples
941    ///
942    /// ```
943    /// let mut x: u8 = 5;
944    /// x <<= 1;
945    /// assert_eq!(x, 10);
946    ///
947    /// let mut x: u8 = 1;
948    /// x <<= 1;
949    /// assert_eq!(x, 2);
950    /// ```
951    #[stable(feature = "op_assign_traits", since = "1.8.0")]
952    fn shl_assign(&mut self, rhs: Rhs);
953}
954
955macro_rules! shl_assign_impl {
956    ($t:ty, $f:ty) => {
957        #[stable(feature = "op_assign_traits", since = "1.8.0")]
958        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
959        impl const ShlAssign<$f> for $t {
960            #[inline]
961            #[rustc_inherit_overflow_checks]
962            fn shl_assign(&mut self, other: $f) {
963                *self <<= other
964            }
965        }
966
967        forward_ref_op_assign! { impl ShlAssign, shl_assign for $t, $f,
968        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
969        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
970    };
971}
972
973macro_rules! shl_assign_impl_all {
974    ($($t:ty)*) => ($(
975        shl_assign_impl! { $t, u8 }
976        shl_assign_impl! { $t, u16 }
977        shl_assign_impl! { $t, u32 }
978        shl_assign_impl! { $t, u64 }
979        shl_assign_impl! { $t, u128 }
980        shl_assign_impl! { $t, usize }
981
982        shl_assign_impl! { $t, i8 }
983        shl_assign_impl! { $t, i16 }
984        shl_assign_impl! { $t, i32 }
985        shl_assign_impl! { $t, i64 }
986        shl_assign_impl! { $t, i128 }
987        shl_assign_impl! { $t, isize }
988    )*)
989}
990
991shl_assign_impl_all! { u8 u16 u32 u64 u128 usize i8 i16 i32 i64 i128 isize }
992
993/// The right shift assignment operator `>>=`.
994///
995/// # Examples
996///
997/// An implementation of `ShrAssign` for a wrapper around `usize`.
998///
999/// ```
1000/// use std::ops::ShrAssign;
1001///
1002/// #[derive(Debug, PartialEq)]
1003/// struct Scalar(usize);
1004///
1005/// impl ShrAssign<usize> for Scalar {
1006///     fn shr_assign(&mut self, rhs: usize) {
1007///         self.0 >>= rhs;
1008///     }
1009/// }
1010///
1011/// let mut scalar = Scalar(16);
1012/// scalar >>= 2;
1013/// assert_eq!(scalar, Scalar(4));
1014/// ```
1015#[lang = "shr_assign"]
1016#[doc(alias = ">>=")]
1017#[stable(feature = "op_assign_traits", since = "1.8.0")]
1018#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1019#[diagnostic::on_unimplemented(
1020    message = "no implementation for `{Self} >>= {Rhs}`",
1021    label = "no implementation for `{Self} >>= {Rhs}`"
1022)]
1023pub const trait ShrAssign<Rhs = Self> {
1024    /// Performs the `>>=` operation.
1025    ///
1026    /// # Examples
1027    ///
1028    /// ```
1029    /// let mut x: u8 = 5;
1030    /// x >>= 1;
1031    /// assert_eq!(x, 2);
1032    ///
1033    /// let mut x: u8 = 2;
1034    /// x >>= 1;
1035    /// assert_eq!(x, 1);
1036    /// ```
1037    #[stable(feature = "op_assign_traits", since = "1.8.0")]
1038    fn shr_assign(&mut self, rhs: Rhs);
1039}
1040
1041macro_rules! shr_assign_impl {
1042    ($t:ty, $f:ty) => {
1043        #[stable(feature = "op_assign_traits", since = "1.8.0")]
1044        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1045        impl const ShrAssign<$f> for $t {
1046            #[inline]
1047            #[rustc_inherit_overflow_checks]
1048            fn shr_assign(&mut self, other: $f) {
1049                *self >>= other
1050            }
1051        }
1052
1053        forward_ref_op_assign! { impl ShrAssign, shr_assign for $t, $f,
1054        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
1055        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
1056    };
1057}
1058
1059macro_rules! shr_assign_impl_all {
1060    ($($t:ty)*) => ($(
1061        shr_assign_impl! { $t, u8 }
1062        shr_assign_impl! { $t, u16 }
1063        shr_assign_impl! { $t, u32 }
1064        shr_assign_impl! { $t, u64 }
1065        shr_assign_impl! { $t, u128 }
1066        shr_assign_impl! { $t, usize }
1067
1068        shr_assign_impl! { $t, i8 }
1069        shr_assign_impl! { $t, i16 }
1070        shr_assign_impl! { $t, i32 }
1071        shr_assign_impl! { $t, i64 }
1072        shr_assign_impl! { $t, i128 }
1073        shr_assign_impl! { $t, isize }
1074    )*)
1075}
1076
1077shr_assign_impl_all! { u8 u16 u32 u64 u128 usize i8 i16 i32 i64 i128 isize }
````