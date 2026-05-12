---
title: arith.rs - source
url: https://doc.rust-lang.org/src/core/ops/arith.rs.html#613-616
source: crawler
fetched_at: 2026-05-06T21:30:21.607801037-03:00
rendered_js: false
word_count: 3841
summary: This document defines the core arithmetic operator traits Add, Sub, and Mul in Rust, explaining how to implement them for custom types using generics and associated types.
tags:
    - rust
    - traits
    - arithmetic-operators
    - operator-overloading
    - generics
category: reference
---

## core/ops/ arith.rs

````rust
1/// The addition operator `+`.
2///
3/// Note that `Rhs` is `Self` by default, but this is not mandatory. For
4/// example, [`std::time::SystemTime`] implements `Add<Duration>`, which permits
5/// operations of the form `SystemTime = SystemTime + Duration`.
6///
7/// [`std::time::SystemTime`]: ../../std/time/struct.SystemTime.html
8///
9/// # Examples
10///
11/// ## `Add`able points
12///
13/// ```
14/// use std::ops::Add;
15///
16/// #[derive(Debug, Copy, Clone, PartialEq)]
17/// struct Point {
18///     x: i32,
19///     y: i32,
20/// }
21///
22/// impl Add for Point {
23///     type Output = Self;
24///
25///     fn add(self, other: Self) -> Self {
26///         Self {
27///             x: self.x + other.x,
28///             y: self.y + other.y,
29///         }
30///     }
31/// }
32///
33/// assert_eq!(Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
34///            Point { x: 3, y: 3 });
35/// ```
36///
37/// ## Implementing `Add` with generics
38///
39/// Here is an example of the same `Point` struct implementing the `Add` trait
40/// using generics.
41///
42/// ```
43/// use std::ops::Add;
44///
45/// #[derive(Debug, Copy, Clone, PartialEq)]
46/// struct Point<T> {
47///     x: T,
48///     y: T,
49/// }
50///
51/// // Notice that the implementation uses the associated type `Output`.
52/// impl<T: Add<Output = T>> Add for Point<T> {
53///     type Output = Self;
54///
55///     fn add(self, other: Self) -> Self::Output {
56///         Self {
57///             x: self.x + other.x,
58///             y: self.y + other.y,
59///         }
60///     }
61/// }
62///
63/// assert_eq!(Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
64///            Point { x: 3, y: 3 });
65/// ```
66#[lang = "add"]
67#[stable(feature = "rust1", since = "1.0.0")]
68#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
69#[rustc_on_unimplemented(
70    on(all(Self = "{integer}", Rhs = "{float}"), message = "cannot add a float to an integer",),
71    on(all(Self = "{float}", Rhs = "{integer}"), message = "cannot add an integer to a float",),
72    message = "cannot add `{Rhs}` to `{Self}`",
73    label = "no implementation for `{Self} + {Rhs}`",
74    append_const_msg
75)]
76#[doc(alias = "+")]
77pub const trait Add<Rhs = Self> {
78    /// The resulting type after applying the `+` operator.
79    #[stable(feature = "rust1", since = "1.0.0")]
80    type Output;
81
82    /// Performs the `+` operation.
83    ///
84    /// # Example
85    ///
86    /// ```
87    /// assert_eq!(12 + 1, 13);
88    /// ```
89    #[must_use = "this returns the result of the operation, without modifying the original"]
90    #[rustc_diagnostic_item = "add"]
91    #[stable(feature = "rust1", since = "1.0.0")]
92    fn add(self, rhs: Rhs) -> Self::Output;
93}
94
95macro_rules! add_impl {
96    ($($t:ty)*) => ($(
97        #[stable(feature = "rust1", since = "1.0.0")]
98        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
99        impl const Add for $t {
100            type Output = $t;
101
102            #[inline]
103            #[track_caller]
104            #[rustc_inherit_overflow_checks]
105            fn add(self, other: $t) -> $t { self + other }
106        }
107
108        forward_ref_binop! { impl Add, add for $t, $t,
109        #[stable(feature = "rust1", since = "1.0.0")]
110        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
111    )*)
112}
113
114add_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
115
116/// The subtraction operator `-`.
117///
118/// Note that `Rhs` is `Self` by default, but this is not mandatory. For
119/// example, [`std::time::SystemTime`] implements `Sub<Duration>`, which permits
120/// operations of the form `SystemTime = SystemTime - Duration`.
121///
122/// [`std::time::SystemTime`]: ../../std/time/struct.SystemTime.html
123///
124/// # Examples
125///
126/// ## `Sub`tractable points
127///
128/// ```
129/// use std::ops::Sub;
130///
131/// #[derive(Debug, Copy, Clone, PartialEq)]
132/// struct Point {
133///     x: i32,
134///     y: i32,
135/// }
136///
137/// impl Sub for Point {
138///     type Output = Self;
139///
140///     fn sub(self, other: Self) -> Self::Output {
141///         Self {
142///             x: self.x - other.x,
143///             y: self.y - other.y,
144///         }
145///     }
146/// }
147///
148/// assert_eq!(Point { x: 3, y: 3 } - Point { x: 2, y: 3 },
149///            Point { x: 1, y: 0 });
150/// ```
151///
152/// ## Implementing `Sub` with generics
153///
154/// Here is an example of the same `Point` struct implementing the `Sub` trait
155/// using generics.
156///
157/// ```
158/// use std::ops::Sub;
159///
160/// #[derive(Debug, PartialEq)]
161/// struct Point<T> {
162///     x: T,
163///     y: T,
164/// }
165///
166/// // Notice that the implementation uses the associated type `Output`.
167/// impl<T: Sub<Output = T>> Sub for Point<T> {
168///     type Output = Self;
169///
170///     fn sub(self, other: Self) -> Self::Output {
171///         Point {
172///             x: self.x - other.x,
173///             y: self.y - other.y,
174///         }
175///     }
176/// }
177///
178/// assert_eq!(Point { x: 2, y: 3 } - Point { x: 1, y: 0 },
179///            Point { x: 1, y: 3 });
180/// ```
181#[lang = "sub"]
182#[stable(feature = "rust1", since = "1.0.0")]
183#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
184#[rustc_on_unimplemented(
185    message = "cannot subtract `{Rhs}` from `{Self}`",
186    label = "no implementation for `{Self} - {Rhs}`",
187    append_const_msg
188)]
189#[doc(alias = "-")]
190pub const trait Sub<Rhs = Self> {
191    /// The resulting type after applying the `-` operator.
192    #[stable(feature = "rust1", since = "1.0.0")]
193    type Output;
194
195    /// Performs the `-` operation.
196    ///
197    /// # Example
198    ///
199    /// ```
200    /// assert_eq!(12 - 1, 11);
201    /// ```
202    #[must_use = "this returns the result of the operation, without modifying the original"]
203    #[rustc_diagnostic_item = "sub"]
204    #[stable(feature = "rust1", since = "1.0.0")]
205    fn sub(self, rhs: Rhs) -> Self::Output;
206}
207
208macro_rules! sub_impl {
209    ($($t:ty)*) => ($(
210        #[stable(feature = "rust1", since = "1.0.0")]
211        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
212        impl const Sub for $t {
213            type Output = $t;
214
215            #[inline]
216            #[track_caller]
217            #[rustc_inherit_overflow_checks]
218            fn sub(self, other: $t) -> $t { self - other }
219        }
220
221        forward_ref_binop! { impl Sub, sub for $t, $t,
222        #[stable(feature = "rust1", since = "1.0.0")]
223        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
224    )*)
225}
226
227sub_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
228
229/// The multiplication operator `*`.
230///
231/// Note that `Rhs` is `Self` by default, but this is not mandatory.
232///
233/// # Examples
234///
235/// ## `Mul`tipliable rational numbers
236///
237/// ```
238/// use std::ops::Mul;
239///
240/// // By the fundamental theorem of arithmetic, rational numbers in lowest
241/// // terms are unique. So, by keeping `Rational`s in reduced form, we can
242/// // derive `Eq` and `PartialEq`.
243/// #[derive(Debug, Eq, PartialEq)]
244/// struct Rational {
245///     numerator: usize,
246///     denominator: usize,
247/// }
248///
249/// impl Rational {
250///     fn new(numerator: usize, denominator: usize) -> Self {
251///         if denominator == 0 {
252///             panic!("Zero is an invalid denominator!");
253///         }
254///
255///         // Reduce to lowest terms by dividing by the greatest common
256///         // divisor.
257///         let gcd = gcd(numerator, denominator);
258///         Self {
259///             numerator: numerator / gcd,
260///             denominator: denominator / gcd,
261///         }
262///     }
263/// }
264///
265/// impl Mul for Rational {
266///     // The multiplication of rational numbers is a closed operation.
267///     type Output = Self;
268///
269///     fn mul(self, rhs: Self) -> Self {
270///         let numerator = self.numerator * rhs.numerator;
271///         let denominator = self.denominator * rhs.denominator;
272///         Self::new(numerator, denominator)
273///     }
274/// }
275///
276/// // Euclid's two-thousand-year-old algorithm for finding the greatest common
277/// // divisor.
278/// fn gcd(x: usize, y: usize) -> usize {
279///     let mut x = x;
280///     let mut y = y;
281///     while y != 0 {
282///         let t = y;
283///         y = x % y;
284///         x = t;
285///     }
286///     x
287/// }
288///
289/// assert_eq!(Rational::new(1, 2), Rational::new(2, 4));
290/// assert_eq!(Rational::new(2, 3) * Rational::new(3, 4),
291///            Rational::new(1, 2));
292/// ```
293///
294/// ## Multiplying vectors by scalars as in linear algebra
295///
296/// ```
297/// use std::ops::Mul;
298///
299/// struct Scalar { value: usize }
300///
301/// #[derive(Debug, PartialEq)]
302/// struct Vector { value: Vec<usize> }
303///
304/// impl Mul<Scalar> for Vector {
305///     type Output = Self;
306///
307///     fn mul(self, rhs: Scalar) -> Self::Output {
308///         Self { value: self.value.iter().map(|v| v * rhs.value).collect() }
309///     }
310/// }
311///
312/// let vector = Vector { value: vec![2, 4, 6] };
313/// let scalar = Scalar { value: 3 };
314/// assert_eq!(vector * scalar, Vector { value: vec![6, 12, 18] });
315/// ```
316#[lang = "mul"]
317#[stable(feature = "rust1", since = "1.0.0")]
318#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
319#[diagnostic::on_unimplemented(
320    message = "cannot multiply `{Self}` by `{Rhs}`",
321    label = "no implementation for `{Self} * {Rhs}`"
322)]
323#[doc(alias = "*")]
324pub const trait Mul<Rhs = Self> {
325    /// The resulting type after applying the `*` operator.
326    #[stable(feature = "rust1", since = "1.0.0")]
327    type Output;
328
329    /// Performs the `*` operation.
330    ///
331    /// # Example
332    ///
333    /// ```
334    /// assert_eq!(12 * 2, 24);
335    /// ```
336    #[must_use = "this returns the result of the operation, without modifying the original"]
337    #[rustc_diagnostic_item = "mul"]
338    #[stable(feature = "rust1", since = "1.0.0")]
339    fn mul(self, rhs: Rhs) -> Self::Output;
340}
341
342macro_rules! mul_impl {
343    ($($t:ty)*) => ($(
344        #[stable(feature = "rust1", since = "1.0.0")]
345        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
346        impl const Mul for $t {
347            type Output = $t;
348
349            #[inline]
350            #[track_caller]
351            #[rustc_inherit_overflow_checks]
352            fn mul(self, other: $t) -> $t { self * other }
353        }
354
355        forward_ref_binop! { impl Mul, mul for $t, $t,
356        #[stable(feature = "rust1", since = "1.0.0")]
357        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
358    )*)
359}
360
361mul_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
362
363/// The division operator `/`.
364///
365/// Note that `Rhs` is `Self` by default, but this is not mandatory.
366///
367/// # Examples
368///
369/// ## `Div`idable rational numbers
370///
371/// ```
372/// use std::ops::Div;
373///
374/// // By the fundamental theorem of arithmetic, rational numbers in lowest
375/// // terms are unique. So, by keeping `Rational`s in reduced form, we can
376/// // derive `Eq` and `PartialEq`.
377/// #[derive(Debug, Eq, PartialEq)]
378/// struct Rational {
379///     numerator: usize,
380///     denominator: usize,
381/// }
382///
383/// impl Rational {
384///     fn new(numerator: usize, denominator: usize) -> Self {
385///         if denominator == 0 {
386///             panic!("Zero is an invalid denominator!");
387///         }
388///
389///         // Reduce to lowest terms by dividing by the greatest common
390///         // divisor.
391///         let gcd = gcd(numerator, denominator);
392///         Self {
393///             numerator: numerator / gcd,
394///             denominator: denominator / gcd,
395///         }
396///     }
397/// }
398///
399/// impl Div for Rational {
400///     // The division of rational numbers is a closed operation.
401///     type Output = Self;
402///
403///     fn div(self, rhs: Self) -> Self::Output {
404///         if rhs.numerator == 0 {
405///             panic!("Cannot divide by zero-valued `Rational`!");
406///         }
407///
408///         let numerator = self.numerator * rhs.denominator;
409///         let denominator = self.denominator * rhs.numerator;
410///         Self::new(numerator, denominator)
411///     }
412/// }
413///
414/// // Euclid's two-thousand-year-old algorithm for finding the greatest common
415/// // divisor.
416/// fn gcd(x: usize, y: usize) -> usize {
417///     let mut x = x;
418///     let mut y = y;
419///     while y != 0 {
420///         let t = y;
421///         y = x % y;
422///         x = t;
423///     }
424///     x
425/// }
426///
427/// assert_eq!(Rational::new(1, 2), Rational::new(2, 4));
428/// assert_eq!(Rational::new(1, 2) / Rational::new(3, 4),
429///            Rational::new(2, 3));
430/// ```
431///
432/// ## Dividing vectors by scalars as in linear algebra
433///
434/// ```
435/// use std::ops::Div;
436///
437/// struct Scalar { value: f32 }
438///
439/// #[derive(Debug, PartialEq)]
440/// struct Vector { value: Vec<f32> }
441///
442/// impl Div<Scalar> for Vector {
443///     type Output = Self;
444///
445///     fn div(self, rhs: Scalar) -> Self::Output {
446///         Self { value: self.value.iter().map(|v| v / rhs.value).collect() }
447///     }
448/// }
449///
450/// let scalar = Scalar { value: 2f32 };
451/// let vector = Vector { value: vec![2f32, 4f32, 6f32] };
452/// assert_eq!(vector / scalar, Vector { value: vec![1f32, 2f32, 3f32] });
453/// ```
454#[lang = "div"]
455#[stable(feature = "rust1", since = "1.0.0")]
456#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
457#[diagnostic::on_unimplemented(
458    message = "cannot divide `{Self}` by `{Rhs}`",
459    label = "no implementation for `{Self} / {Rhs}`"
460)]
461#[doc(alias = "/")]
462pub const trait Div<Rhs = Self> {
463    /// The resulting type after applying the `/` operator.
464    #[stable(feature = "rust1", since = "1.0.0")]
465    type Output;
466
467    /// Performs the `/` operation.
468    ///
469    /// # Example
470    ///
471    /// ```
472    /// assert_eq!(12 / 2, 6);
473    /// ```
474    #[must_use = "this returns the result of the operation, without modifying the original"]
475    #[rustc_diagnostic_item = "div"]
476    #[stable(feature = "rust1", since = "1.0.0")]
477    fn div(self, rhs: Rhs) -> Self::Output;
478}
479
480macro_rules! div_impl_integer {
481    ($(($($t:ty)*) => $panic:expr),*) => ($($(
482        /// This operation rounds towards zero, truncating any
483        /// fractional part of the exact result.
484        ///
485        /// # Panics
486        ///
487        #[doc = $panic]
488        #[stable(feature = "rust1", since = "1.0.0")]
489        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
490        impl const Div for $t {
491            type Output = $t;
492
493            #[inline]
494            #[track_caller]
495            fn div(self, other: $t) -> $t { self / other }
496        }
497
498        forward_ref_binop! { impl Div, div for $t, $t,
499        #[stable(feature = "rust1", since = "1.0.0")]
500        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
501    )*)*)
502}
503
504div_impl_integer! {
505    (usize u8 u16 u32 u64 u128) => "This operation will panic if `other == 0`.",
506    (isize i8 i16 i32 i64 i128) => "This operation will panic if `other == 0` or the division results in overflow."
507}
508
509macro_rules! div_impl_float {
510    ($($t:ty)*) => ($(
511        #[stable(feature = "rust1", since = "1.0.0")]
512        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
513        impl const Div for $t {
514            type Output = $t;
515
516            #[inline]
517            fn div(self, other: $t) -> $t { self / other }
518        }
519
520        forward_ref_binop! { impl Div, div for $t, $t,
521        #[stable(feature = "rust1", since = "1.0.0")]
522        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
523    )*)
524}
525
526div_impl_float! { f16 f32 f64 f128 }
527
528/// The remainder operator `%`.
529///
530/// Note that `Rhs` is `Self` by default, but this is not mandatory.
531///
532/// # Examples
533///
534/// This example implements `Rem` on a `SplitSlice` object. After `Rem` is
535/// implemented, one can use the `%` operator to find out what the remaining
536/// elements of the slice would be after splitting it into equal slices of a
537/// given length.
538///
539/// ```
540/// use std::ops::Rem;
541///
542/// #[derive(PartialEq, Debug)]
543/// struct SplitSlice<'a, T> {
544///     slice: &'a [T],
545/// }
546///
547/// impl<'a, T> Rem<usize> for SplitSlice<'a, T> {
548///     type Output = Self;
549///
550///     fn rem(self, modulus: usize) -> Self::Output {
551///         let len = self.slice.len();
552///         let rem = len % modulus;
553///         let start = len - rem;
554///         Self {slice: &self.slice[start..]}
555///     }
556/// }
557///
558/// // If we were to divide &[0, 1, 2, 3, 4, 5, 6, 7] into slices of size 3,
559/// // the remainder would be &[6, 7].
560/// assert_eq!(SplitSlice { slice: &[0, 1, 2, 3, 4, 5, 6, 7] } % 3,
561///            SplitSlice { slice: &[6, 7] });
562/// ```
563#[lang = "rem"]
564#[stable(feature = "rust1", since = "1.0.0")]
565#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
566#[diagnostic::on_unimplemented(
567    message = "cannot calculate the remainder of `{Self}` divided by `{Rhs}`",
568    label = "no implementation for `{Self} % {Rhs}`"
569)]
570#[doc(alias = "%")]
571pub const trait Rem<Rhs = Self> {
572    /// The resulting type after applying the `%` operator.
573    #[stable(feature = "rust1", since = "1.0.0")]
574    type Output;
575
576    /// Performs the `%` operation.
577    ///
578    /// # Example
579    ///
580    /// ```
581    /// assert_eq!(12 % 10, 2);
582    /// ```
583    #[must_use = "this returns the result of the operation, without modifying the original"]
584    #[rustc_diagnostic_item = "rem"]
585    #[stable(feature = "rust1", since = "1.0.0")]
586    fn rem(self, rhs: Rhs) -> Self::Output;
587}
588
589macro_rules! rem_impl_integer {
590    ($(($($t:ty)*) => $panic:expr),*) => ($($(
591        /// This operation satisfies `n % d == n - (n / d) * d`. The
592        /// result has the same sign as the left operand.
593        ///
594        /// # Panics
595        ///
596        #[doc = $panic]
597        #[stable(feature = "rust1", since = "1.0.0")]
598        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
599        impl const Rem for $t {
600            type Output = $t;
601
602            #[inline]
603            #[track_caller]
604            fn rem(self, other: $t) -> $t { self % other }
605        }
606
607        forward_ref_binop! { impl Rem, rem for $t, $t,
608        #[stable(feature = "rust1", since = "1.0.0")]
609        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
610    )*)*)
611}
612
613rem_impl_integer! {
614    (usize u8 u16 u32 u64 u128) => "This operation will panic if `other == 0`.",
615    (isize i8 i16 i32 i64 i128) => "This operation will panic if `other == 0` or if `self / other` results in overflow."
616}
617
618macro_rules! rem_impl_float {
619    ($($t:ty)*) => ($(
620
621        /// The remainder from the division of two floats.
622        ///
623        /// The remainder has the same sign as the dividend and is computed as:
624        /// `x - (x / y).trunc() * y`.
625        ///
626        /// # Examples
627        /// ```
628        /// let x: f32 = 50.50;
629        /// let y: f32 = 8.125;
630        /// let remainder = x - (x / y).trunc() * y;
631        ///
632        /// // The answer to both operations is 1.75
633        /// assert_eq!(x % y, remainder);
634        /// ```
635        #[stable(feature = "rust1", since = "1.0.0")]
636        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
637        impl const Rem for $t {
638            type Output = $t;
639
640            #[inline]
641            fn rem(self, other: $t) -> $t { self % other }
642        }
643
644        forward_ref_binop! { impl Rem, rem for $t, $t,
645        #[stable(feature = "rust1", since = "1.0.0")]
646        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
647    )*)
648}
649
650rem_impl_float! { f16 f32 f64 f128 }
651
652/// The unary negation operator `-`.
653///
654/// # Examples
655///
656/// An implementation of `Neg` for `Sign`, which allows the use of `-` to
657/// negate its value.
658///
659/// ```
660/// use std::ops::Neg;
661///
662/// #[derive(Debug, PartialEq)]
663/// enum Sign {
664///     Negative,
665///     Zero,
666///     Positive,
667/// }
668///
669/// impl Neg for Sign {
670///     type Output = Self;
671///
672///     fn neg(self) -> Self::Output {
673///         match self {
674///             Sign::Negative => Sign::Positive,
675///             Sign::Zero => Sign::Zero,
676///             Sign::Positive => Sign::Negative,
677///         }
678///     }
679/// }
680///
681/// // A negative positive is a negative.
682/// assert_eq!(-Sign::Positive, Sign::Negative);
683/// // A double negative is a positive.
684/// assert_eq!(-Sign::Negative, Sign::Positive);
685/// // Zero is its own negation.
686/// assert_eq!(-Sign::Zero, Sign::Zero);
687/// ```
688#[lang = "neg"]
689#[stable(feature = "rust1", since = "1.0.0")]
690#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
691#[doc(alias = "-")]
692pub const trait Neg {
693    /// The resulting type after applying the `-` operator.
694    #[stable(feature = "rust1", since = "1.0.0")]
695    type Output;
696
697    /// Performs the unary `-` operation.
698    ///
699    /// # Example
700    ///
701    /// ```
702    /// let x: i32 = 12;
703    /// assert_eq!(-x, -12);
704    /// ```
705    #[must_use = "this returns the result of the operation, without modifying the original"]
706    #[rustc_diagnostic_item = "neg"]
707    #[stable(feature = "rust1", since = "1.0.0")]
708    fn neg(self) -> Self::Output;
709}
710
711macro_rules! neg_impl {
712    ($($t:ty)*) => ($(
713        #[stable(feature = "rust1", since = "1.0.0")]
714        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
715        impl const Neg for $t {
716            type Output = $t;
717
718            #[inline]
719            #[rustc_inherit_overflow_checks]
720            fn neg(self) -> $t { -self }
721        }
722
723        forward_ref_unop! { impl Neg, neg for $t,
724        #[stable(feature = "rust1", since = "1.0.0")]
725        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
726    )*)
727}
728
729neg_impl! { isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
730
731/// The addition assignment operator `+=`.
732///
733/// # Examples
734///
735/// This example creates a `Point` struct that implements the `AddAssign`
736/// trait, and then demonstrates add-assigning to a mutable `Point`.
737///
738/// ```
739/// use std::ops::AddAssign;
740///
741/// #[derive(Debug, Copy, Clone, PartialEq)]
742/// struct Point {
743///     x: i32,
744///     y: i32,
745/// }
746///
747/// impl AddAssign for Point {
748///     fn add_assign(&mut self, other: Self) {
749///         *self = Self {
750///             x: self.x + other.x,
751///             y: self.y + other.y,
752///         };
753///     }
754/// }
755///
756/// let mut point = Point { x: 1, y: 0 };
757/// point += Point { x: 2, y: 3 };
758/// assert_eq!(point, Point { x: 3, y: 3 });
759/// ```
760#[lang = "add_assign"]
761#[stable(feature = "op_assign_traits", since = "1.8.0")]
762#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
763#[diagnostic::on_unimplemented(
764    message = "cannot add-assign `{Rhs}` to `{Self}`",
765    label = "no implementation for `{Self} += {Rhs}`"
766)]
767#[doc(alias = "+")]
768#[doc(alias = "+=")]
769pub const trait AddAssign<Rhs = Self> {
770    /// Performs the `+=` operation.
771    ///
772    /// # Example
773    ///
774    /// ```
775    /// let mut x: u32 = 12;
776    /// x += 1;
777    /// assert_eq!(x, 13);
778    /// ```
779    #[stable(feature = "op_assign_traits", since = "1.8.0")]
780    fn add_assign(&mut self, rhs: Rhs);
781}
782
783macro_rules! add_assign_impl {
784    ($($t:ty)+) => ($(
785        #[stable(feature = "op_assign_traits", since = "1.8.0")]
786        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
787        impl const AddAssign for $t {
788            #[inline]
789            #[track_caller]
790            #[rustc_inherit_overflow_checks]
791            fn add_assign(&mut self, other: $t) { *self += other }
792        }
793
794        forward_ref_op_assign! { impl AddAssign, add_assign for $t, $t,
795        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
796        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
797    )+)
798}
799
800add_assign_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
801
802/// The subtraction assignment operator `-=`.
803///
804/// # Examples
805///
806/// This example creates a `Point` struct that implements the `SubAssign`
807/// trait, and then demonstrates sub-assigning to a mutable `Point`.
808///
809/// ```
810/// use std::ops::SubAssign;
811///
812/// #[derive(Debug, Copy, Clone, PartialEq)]
813/// struct Point {
814///     x: i32,
815///     y: i32,
816/// }
817///
818/// impl SubAssign for Point {
819///     fn sub_assign(&mut self, other: Self) {
820///         *self = Self {
821///             x: self.x - other.x,
822///             y: self.y - other.y,
823///         };
824///     }
825/// }
826///
827/// let mut point = Point { x: 3, y: 3 };
828/// point -= Point { x: 2, y: 3 };
829/// assert_eq!(point, Point {x: 1, y: 0});
830/// ```
831#[lang = "sub_assign"]
832#[stable(feature = "op_assign_traits", since = "1.8.0")]
833#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
834#[diagnostic::on_unimplemented(
835    message = "cannot subtract-assign `{Rhs}` from `{Self}`",
836    label = "no implementation for `{Self} -= {Rhs}`"
837)]
838#[doc(alias = "-")]
839#[doc(alias = "-=")]
840pub const trait SubAssign<Rhs = Self> {
841    /// Performs the `-=` operation.
842    ///
843    /// # Example
844    ///
845    /// ```
846    /// let mut x: u32 = 12;
847    /// x -= 1;
848    /// assert_eq!(x, 11);
849    /// ```
850    #[stable(feature = "op_assign_traits", since = "1.8.0")]
851    fn sub_assign(&mut self, rhs: Rhs);
852}
853
854macro_rules! sub_assign_impl {
855    ($($t:ty)+) => ($(
856        #[stable(feature = "op_assign_traits", since = "1.8.0")]
857        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
858        impl const SubAssign for $t {
859            #[inline]
860            #[track_caller]
861            #[rustc_inherit_overflow_checks]
862            fn sub_assign(&mut self, other: $t) { *self -= other }
863        }
864
865        forward_ref_op_assign! { impl SubAssign, sub_assign for $t, $t,
866        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
867        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
868    )+)
869}
870
871sub_assign_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
872
873/// The multiplication assignment operator `*=`.
874///
875/// # Examples
876///
877/// ```
878/// use std::ops::MulAssign;
879///
880/// #[derive(Debug, PartialEq)]
881/// struct Frequency { hertz: f64 }
882///
883/// impl MulAssign<f64> for Frequency {
884///     fn mul_assign(&mut self, rhs: f64) {
885///         self.hertz *= rhs;
886///     }
887/// }
888///
889/// let mut frequency = Frequency { hertz: 50.0 };
890/// frequency *= 4.0;
891/// assert_eq!(Frequency { hertz: 200.0 }, frequency);
892/// ```
893#[lang = "mul_assign"]
894#[stable(feature = "op_assign_traits", since = "1.8.0")]
895#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
896#[diagnostic::on_unimplemented(
897    message = "cannot multiply-assign `{Self}` by `{Rhs}`",
898    label = "no implementation for `{Self} *= {Rhs}`"
899)]
900#[doc(alias = "*")]
901#[doc(alias = "*=")]
902pub const trait MulAssign<Rhs = Self> {
903    /// Performs the `*=` operation.
904    ///
905    /// # Example
906    ///
907    /// ```
908    /// let mut x: u32 = 12;
909    /// x *= 2;
910    /// assert_eq!(x, 24);
911    /// ```
912    #[stable(feature = "op_assign_traits", since = "1.8.0")]
913    fn mul_assign(&mut self, rhs: Rhs);
914}
915
916macro_rules! mul_assign_impl {
917    ($($t:ty)+) => ($(
918        #[stable(feature = "op_assign_traits", since = "1.8.0")]
919        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
920        impl const MulAssign for $t {
921            #[inline]
922            #[track_caller]
923            #[rustc_inherit_overflow_checks]
924            fn mul_assign(&mut self, other: $t) { *self *= other }
925        }
926
927        forward_ref_op_assign! { impl MulAssign, mul_assign for $t, $t,
928        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
929        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
930    )+)
931}
932
933mul_assign_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
934
935/// The division assignment operator `/=`.
936///
937/// # Examples
938///
939/// ```
940/// use std::ops::DivAssign;
941///
942/// #[derive(Debug, PartialEq)]
943/// struct Frequency { hertz: f64 }
944///
945/// impl DivAssign<f64> for Frequency {
946///     fn div_assign(&mut self, rhs: f64) {
947///         self.hertz /= rhs;
948///     }
949/// }
950///
951/// let mut frequency = Frequency { hertz: 200.0 };
952/// frequency /= 4.0;
953/// assert_eq!(Frequency { hertz: 50.0 }, frequency);
954/// ```
955#[lang = "div_assign"]
956#[stable(feature = "op_assign_traits", since = "1.8.0")]
957#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
958#[diagnostic::on_unimplemented(
959    message = "cannot divide-assign `{Self}` by `{Rhs}`",
960    label = "no implementation for `{Self} /= {Rhs}`"
961)]
962#[doc(alias = "/")]
963#[doc(alias = "/=")]
964pub const trait DivAssign<Rhs = Self> {
965    /// Performs the `/=` operation.
966    ///
967    /// # Example
968    ///
969    /// ```
970    /// let mut x: u32 = 12;
971    /// x /= 2;
972    /// assert_eq!(x, 6);
973    /// ```
974    #[stable(feature = "op_assign_traits", since = "1.8.0")]
975    fn div_assign(&mut self, rhs: Rhs);
976}
977
978macro_rules! div_assign_impl {
979    ($($t:ty)+) => ($(
980        #[stable(feature = "op_assign_traits", since = "1.8.0")]
981        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
982        impl const DivAssign for $t {
983            #[inline]
984            #[track_caller]
985            fn div_assign(&mut self, other: $t) { *self /= other }
986        }
987
988        forward_ref_op_assign! { impl DivAssign, div_assign for $t, $t,
989        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
990        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
991    )+)
992}
993
994div_assign_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
995
996/// The remainder assignment operator `%=`.
997///
998/// # Examples
999///
1000/// ```
1001/// use std::ops::RemAssign;
1002///
1003/// struct CookieJar { cookies: u32 }
1004///
1005/// impl RemAssign<u32> for CookieJar {
1006///     fn rem_assign(&mut self, piles: u32) {
1007///         self.cookies %= piles;
1008///     }
1009/// }
1010///
1011/// let mut jar = CookieJar { cookies: 31 };
1012/// let piles = 4;
1013///
1014/// println!("Splitting up {} cookies into {} even piles!", jar.cookies, piles);
1015///
1016/// jar %= piles;
1017///
1018/// println!("{} cookies remain in the cookie jar!", jar.cookies);
1019/// ```
1020#[lang = "rem_assign"]
1021#[stable(feature = "op_assign_traits", since = "1.8.0")]
1022#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1023#[diagnostic::on_unimplemented(
1024    message = "cannot calculate and assign the remainder of `{Self}` divided by `{Rhs}`",
1025    label = "no implementation for `{Self} %= {Rhs}`"
1026)]
1027#[doc(alias = "%")]
1028#[doc(alias = "%=")]
1029pub const trait RemAssign<Rhs = Self> {
1030    /// Performs the `%=` operation.
1031    ///
1032    /// # Example
1033    ///
1034    /// ```
1035    /// let mut x: u32 = 12;
1036    /// x %= 10;
1037    /// assert_eq!(x, 2);
1038    /// ```
1039    #[stable(feature = "op_assign_traits", since = "1.8.0")]
1040    fn rem_assign(&mut self, rhs: Rhs);
1041}
1042
1043macro_rules! rem_assign_impl {
1044    ($($t:ty)+) => ($(
1045        #[stable(feature = "op_assign_traits", since = "1.8.0")]
1046        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1047        impl const RemAssign for $t {
1048            #[inline]
1049            #[track_caller]
1050            fn rem_assign(&mut self, other: $t) { *self %= other }
1051        }
1052
1053        forward_ref_op_assign! { impl RemAssign, rem_assign for $t, $t,
1054        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
1055        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
1056    )+)
1057}
1058
1059rem_assign_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128 }
````