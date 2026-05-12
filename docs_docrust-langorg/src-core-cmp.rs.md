---
title: cmp.rs - source
url: https://doc.rust-lang.org/src/core/cmp.rs.html#264
source: crawler
fetched_at: 2026-05-06T21:23:45.908224185-03:00
rendered_js: false
word_count: 9013
summary: This document defines the Rust traits used for comparing and ordering values, including PartialEq, Eq, PartialOrd, and Ord, explaining their requirements for symmetry, transitivity, and operator overloading.
tags:
    - rust
    - comparison
    - traits
    - operator-overloading
    - partialeq
    - ordering
category: reference
---

## core/ cmp.rs

````rust
1//! Utilities for comparing and ordering values.
2//!
3//! This module contains various tools for comparing and ordering values. In
4//! summary:
5//!
6//! * [`PartialEq<Rhs>`] overloads the `==` and `!=` operators. In cases where
7//!   `Rhs` (the right hand side's type) is `Self`, this trait corresponds to a
8//!   partial equivalence relation.
9//! * [`Eq`] indicates that the overloaded `==` operator corresponds to an
10//!   equivalence relation.
11//! * [`Ord`] and [`PartialOrd`] are traits that allow you to define total and
12//!   partial orderings between values, respectively. Implementing them overloads
13//!   the `<`, `<=`, `>`, and `>=` operators.
14//! * [`Ordering`] is an enum returned by the main functions of [`Ord`] and
15//!   [`PartialOrd`], and describes an ordering of two values (less, equal, or
16//!   greater).
17//! * [`Reverse`] is a struct that allows you to easily reverse an ordering.
18//! * [`max`] and [`min`] are functions that build off of [`Ord`] and allow you
19//!   to find the maximum or minimum of two values.
20//!
21//! For more details, see the respective documentation of each item in the list.
22//!
23//! [`max`]: Ord::max
24//! [`min`]: Ord::min
25
26#![stable(feature = "rust1", since = "1.0.0")]
27
28mod bytewise;
29pub(crate) use bytewise::BytewiseEq;
30
31use self::Ordering::*;
32use crate::marker::{Destruct, PointeeSized};
33use crate::ops::ControlFlow;
34
35/// Trait for comparisons using the equality operator.
36///
37/// Implementing this trait for types provides the `==` and `!=` operators for
38/// those types.
39///
40/// `x.eq(y)` can also be written `x == y`, and `x.ne(y)` can be written `x != y`.
41/// We use the easier-to-read infix notation in the remainder of this documentation.
42///
43/// This trait allows for comparisons using the equality operator, for types
44/// that do not have a full equivalence relation. For example, in floating point
45/// numbers `NaN != NaN`, so floating point types implement `PartialEq` but not
46/// [`trait@Eq`]. Formally speaking, when `Rhs == Self`, this trait corresponds
47/// to a [partial equivalence relation].
48///
49/// [partial equivalence relation]: https://en.wikipedia.org/wiki/Partial_equivalence_relation
50///
51/// Implementations must ensure that `eq` and `ne` are consistent with each other:
52///
53/// - `a != b` if and only if `!(a == b)`.
54///
55/// The default implementation of `ne` provides this consistency and is almost
56/// always sufficient. It should not be overridden without very good reason.
57///
58/// If [`PartialOrd`] or [`Ord`] are also implemented for `Self` and `Rhs`, their methods must also
59/// be consistent with `PartialEq` (see the documentation of those traits for the exact
60/// requirements). It's easy to accidentally make them disagree by deriving some of the traits and
61/// manually implementing others.
62///
63/// The equality relation `==` must satisfy the following conditions
64/// (for all `a`, `b`, `c` of type `A`, `B`, `C`):
65///
66/// - **Symmetry**: if `A: PartialEq<B>` and `B: PartialEq<A>`, then **`a == b`
67///   implies `b == a`**; and
68///
69/// - **Transitivity**: if `A: PartialEq<B>` and `B: PartialEq<C>` and `A:
70///   PartialEq<C>`, then **`a == b` and `b == c` implies `a == c`**.
71///   This must also work for longer chains, such as when `A: PartialEq<B>`, `B: PartialEq<C>`,
72///   `C: PartialEq<D>`, and `A: PartialEq<D>` all exist.
73///
74/// Note that the `B: PartialEq<A>` (symmetric) and `A: PartialEq<C>`
75/// (transitive) impls are not forced to exist, but these requirements apply
76/// whenever they do exist.
77///
78/// Violating these requirements is a logic error. The behavior resulting from a logic error is not
79/// specified, but users of the trait must ensure that such logic errors do *not* result in
80/// undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these
81/// methods.
82///
83/// ## Cross-crate considerations
84///
85/// Upholding the requirements stated above can become tricky when one crate implements `PartialEq`
86/// for a type of another crate (i.e., to allow comparing one of its own types with a type from the
87/// standard library). The recommendation is to never implement this trait for a foreign type. In
88/// other words, such a crate should do `impl PartialEq<ForeignType> for LocalType`, but it should
89/// *not* do `impl PartialEq<LocalType> for ForeignType`.
90///
91/// This avoids the problem of transitive chains that criss-cross crate boundaries: for all local
92/// types `T`, you may assume that no other crate will add `impl`s that allow comparing `T == U`. In
93/// other words, if other crates add `impl`s that allow building longer transitive chains `U1 == ...
94/// == T == V1 == ...`, then all the types that appear to the right of `T` must be types that the
95/// crate defining `T` already knows about. This rules out transitive chains where downstream crates
96/// can add new `impl`s that "stitch together" comparisons of foreign types in ways that violate
97/// transitivity.
98///
99/// Not having such foreign `impl`s also avoids forward compatibility issues where one crate adding
100/// more `PartialEq` implementations can cause build failures in downstream crates.
101///
102/// ## Derivable
103///
104/// This trait can be used with `#[derive]`. When `derive`d on structs, two
105/// instances are equal if all fields are equal, and not equal if any fields
106/// are not equal. When `derive`d on enums, two instances are equal if they
107/// are the same variant and all fields are equal.
108///
109/// ## How can I implement `PartialEq`?
110///
111/// An example implementation for a domain in which two books are considered
112/// the same book if their ISBN matches, even if the formats differ:
113///
114/// ```
115/// enum BookFormat {
116///     Paperback,
117///     Hardback,
118///     Ebook,
119/// }
120///
121/// struct Book {
122///     isbn: i32,
123///     format: BookFormat,
124/// }
125///
126/// impl PartialEq for Book {
127///     fn eq(&self, other: &Self) -> bool {
128///         self.isbn == other.isbn
129///     }
130/// }
131///
132/// let b1 = Book { isbn: 3, format: BookFormat::Paperback };
133/// let b2 = Book { isbn: 3, format: BookFormat::Ebook };
134/// let b3 = Book { isbn: 10, format: BookFormat::Paperback };
135///
136/// assert!(b1 == b2);
137/// assert!(b1 != b3);
138/// ```
139///
140/// ## How can I compare two different types?
141///
142/// The type you can compare with is controlled by `PartialEq`'s type parameter.
143/// For example, let's tweak our previous code a bit:
144///
145/// ```
146/// // The derive implements <BookFormat> == <BookFormat> comparisons
147/// #[derive(PartialEq)]
148/// enum BookFormat {
149///     Paperback,
150///     Hardback,
151///     Ebook,
152/// }
153///
154/// struct Book {
155///     isbn: i32,
156///     format: BookFormat,
157/// }
158///
159/// // Implement <Book> == <BookFormat> comparisons
160/// impl PartialEq<BookFormat> for Book {
161///     fn eq(&self, other: &BookFormat) -> bool {
162///         self.format == *other
163///     }
164/// }
165///
166/// // Implement <BookFormat> == <Book> comparisons
167/// impl PartialEq<Book> for BookFormat {
168///     fn eq(&self, other: &Book) -> bool {
169///         *self == other.format
170///     }
171/// }
172///
173/// let b1 = Book { isbn: 3, format: BookFormat::Paperback };
174///
175/// assert!(b1 == BookFormat::Paperback);
176/// assert!(BookFormat::Ebook != b1);
177/// ```
178///
179/// By changing `impl PartialEq for Book` to `impl PartialEq<BookFormat> for Book`,
180/// we allow `BookFormat`s to be compared with `Book`s.
181///
182/// A comparison like the one above, which ignores some fields of the struct,
183/// can be dangerous. It can easily lead to an unintended violation of the
184/// requirements for a partial equivalence relation. For example, if we kept
185/// the above implementation of `PartialEq<Book>` for `BookFormat` and added an
186/// implementation of `PartialEq<Book>` for `Book` (either via a `#[derive]` or
187/// via the manual implementation from the first example) then the result would
188/// violate transitivity:
189///
190/// ```should_panic
191/// #[derive(PartialEq)]
192/// enum BookFormat {
193///     Paperback,
194///     Hardback,
195///     Ebook,
196/// }
197///
198/// #[derive(PartialEq)]
199/// struct Book {
200///     isbn: i32,
201///     format: BookFormat,
202/// }
203///
204/// impl PartialEq<BookFormat> for Book {
205///     fn eq(&self, other: &BookFormat) -> bool {
206///         self.format == *other
207///     }
208/// }
209///
210/// impl PartialEq<Book> for BookFormat {
211///     fn eq(&self, other: &Book) -> bool {
212///         *self == other.format
213///     }
214/// }
215///
216/// fn main() {
217///     let b1 = Book { isbn: 1, format: BookFormat::Paperback };
218///     let b2 = Book { isbn: 2, format: BookFormat::Paperback };
219///
220///     assert!(b1 == BookFormat::Paperback);
221///     assert!(BookFormat::Paperback == b2);
222///
223///     // The following should hold by transitivity but doesn't.
224///     assert!(b1 == b2); // <-- PANICS
225/// }
226/// ```
227///
228/// # Examples
229///
230/// ```
231/// let x: u32 = 0;
232/// let y: u32 = 1;
233///
234/// assert_eq!(x == y, false);
235/// assert_eq!(x.eq(&y), false);
236/// ```
237///
238/// [`eq`]: PartialEq::eq
239/// [`ne`]: PartialEq::ne
240#[lang = "eq"]
241#[stable(feature = "rust1", since = "1.0.0")]
242#[doc(alias = "==")]
243#[doc(alias = "!=")]
244#[rustc_on_unimplemented(
245    message = "can't compare `{Self}` with `{Rhs}`",
246    label = "no implementation for `{Self} == {Rhs}`",
247    append_const_msg
248)]
249#[rustc_diagnostic_item = "PartialEq"]
250#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
251pub const trait PartialEq<Rhs: PointeeSized = Self>: PointeeSized {
252    /// Tests for `self` and `other` values to be equal, and is used by `==`.
253    #[must_use]
254    #[stable(feature = "rust1", since = "1.0.0")]
255    #[rustc_diagnostic_item = "cmp_partialeq_eq"]
256    fn eq(&self, other: &Rhs) -> bool;
257
258    /// Tests for `!=`. The default implementation is almost always sufficient,
259    /// and should not be overridden without very good reason.
260    #[inline]
261    #[must_use]
262    #[stable(feature = "rust1", since = "1.0.0")]
263    #[rustc_diagnostic_item = "cmp_partialeq_ne"]
264    fn ne(&self, other: &Rhs) -> bool {
265        !self.eq(other)
266    }
267}
268
269/// Derive macro generating an impl of the trait [`PartialEq`].
270/// The behavior of this macro is described in detail [here](PartialEq#derivable).
271#[rustc_builtin_macro]
272#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
273#[allow_internal_unstable(core_intrinsics, structural_match)]
274pub macro PartialEq($item:item) {
275    /* compiler built-in */
276}
277
278/// Trait for comparisons corresponding to [equivalence relations](
279/// https://en.wikipedia.org/wiki/Equivalence_relation).
280///
281/// The primary difference to [`PartialEq`] is the additional requirement for reflexivity. A type
282/// that implements [`PartialEq`] guarantees that for all `a`, `b` and `c`:
283///
284/// - symmetric: `a == b` implies `b == a` and `a != b` implies `!(a == b)`
285/// - transitive: `a == b` and `b == c` implies `a == c`
286///
287/// `Eq`, which builds on top of [`PartialEq`] also implies:
288///
289/// - reflexive: `a == a`
290///
291/// This property cannot be checked by the compiler, and therefore `Eq` is a trait without methods.
292///
293/// Violating this property is a logic error. The behavior resulting from a logic error is not
294/// specified, but users of the trait must ensure that such logic errors do *not* result in
295/// undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these
296/// methods.
297///
298/// Floating point types such as [`f32`] and [`f64`] implement only [`PartialEq`] but *not* `Eq`
299/// because `NaN` != `NaN`.
300///
301/// ## Derivable
302///
303/// This trait can be used with `#[derive]`. When `derive`d, because `Eq` has no extra methods, it
304/// is only informing the compiler that this is an equivalence relation rather than a partial
305/// equivalence relation. Note that the `derive` strategy requires all fields are `Eq`, which isn't
306/// always desired.
307///
308/// ## How can I implement `Eq`?
309///
310/// If you cannot use the `derive` strategy, specify that your type implements `Eq`, which has no
311/// extra methods:
312///
313/// ```
314/// enum BookFormat {
315///     Paperback,
316///     Hardback,
317///     Ebook,
318/// }
319///
320/// struct Book {
321///     isbn: i32,
322///     format: BookFormat,
323/// }
324///
325/// impl PartialEq for Book {
326///     fn eq(&self, other: &Self) -> bool {
327///         self.isbn == other.isbn
328///     }
329/// }
330///
331/// impl Eq for Book {}
332/// ```
333#[doc(alias = "==")]
334#[doc(alias = "!=")]
335#[stable(feature = "rust1", since = "1.0.0")]
336#[rustc_diagnostic_item = "Eq"]
337#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
338pub const trait Eq: [const] PartialEq<Self> + PointeeSized {
339    // This method was used solely by `#[derive(Eq)]` to assert that every component of a
340    // type implements `Eq` itself.
341    //
342    // This should never be implemented by hand.
343    #[doc(hidden)]
344    #[coverage(off)]
345    #[inline]
346    #[stable(feature = "rust1", since = "1.0.0")]
347    #[rustc_diagnostic_item = "assert_receiver_is_total_eq"]
348    #[deprecated(since = "1.95.0", note = "implementation detail of `#[derive(Eq)]`")]
349    fn assert_receiver_is_total_eq(&self) {}
350
351    // FIXME (#152504): this method is used solely by `#[derive(Eq)]` to assert that
352    // every component of a type implements `Eq` itself. It will be removed again soon.
353    #[doc(hidden)]
354    #[coverage(off)]
355    #[unstable(feature = "derive_eq_internals", issue = "none")]
356    fn assert_fields_are_eq(&self) {}
357}
358
359/// Derive macro generating an impl of the trait [`Eq`].
360#[rustc_builtin_macro]
361#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
362#[allow_internal_unstable(core_intrinsics, derive_eq_internals, structural_match)]
363#[allow_internal_unstable(coverage_attribute)]
364pub macro Eq($item:item) {
365    /* compiler built-in */
366}
367
368// FIXME: this struct is used solely by #[derive] to
369// assert that every component of a type implements Eq.
370//
371// This struct should never appear in user code.
372#[doc(hidden)]
373#[allow(missing_debug_implementations)]
374#[unstable(
375    feature = "derive_eq_internals",
376    reason = "deriving hack, should not be public",
377    issue = "none"
378)]
379pub struct AssertParamIsEq<T: Eq + PointeeSized> {
380    _field: crate::marker::PhantomData<T>,
381}
382
383/// An `Ordering` is the result of a comparison between two values.
384///
385/// # Examples
386///
387/// ```
388/// use std::cmp::Ordering;
389///
390/// assert_eq!(1.cmp(&2), Ordering::Less);
391///
392/// assert_eq!(1.cmp(&1), Ordering::Equal);
393///
394/// assert_eq!(2.cmp(&1), Ordering::Greater);
395/// ```
396#[derive(Copy, Debug, Hash)]
397#[derive_const(Clone, Eq, PartialOrd, Ord, PartialEq)]
398#[stable(feature = "rust1", since = "1.0.0")]
399// This is a lang item only so that `BinOp::Cmp` in MIR can return it.
400// It has no special behavior, but does require that the three variants
401// `Less`/`Equal`/`Greater` remain `-1_i8`/`0_i8`/`+1_i8` respectively.
402#[lang = "Ordering"]
403#[repr(i8)]
404pub enum Ordering {
405    /// An ordering where a compared value is less than another.
406    #[stable(feature = "rust1", since = "1.0.0")]
407    Less = -1,
408    /// An ordering where a compared value is equal to another.
409    #[stable(feature = "rust1", since = "1.0.0")]
410    Equal = 0,
411    /// An ordering where a compared value is greater than another.
412    #[stable(feature = "rust1", since = "1.0.0")]
413    Greater = 1,
414}
415
416impl Ordering {
417    #[inline]
418    const fn as_raw(self) -> i8 {
419        // FIXME(const-hack): just use `PartialOrd` against `Equal` once that's const
420        crate::intrinsics::discriminant_value(&self)
421    }
422
423    /// Returns `true` if the ordering is the `Equal` variant.
424    ///
425    /// # Examples
426    ///
427    /// ```
428    /// use std::cmp::Ordering;
429    ///
430    /// assert_eq!(Ordering::Less.is_eq(), false);
431    /// assert_eq!(Ordering::Equal.is_eq(), true);
432    /// assert_eq!(Ordering::Greater.is_eq(), false);
433    /// ```
434    #[inline]
435    #[must_use]
436    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
437    #[stable(feature = "ordering_helpers", since = "1.53.0")]
438    pub const fn is_eq(self) -> bool {
439        // All the `is_*` methods are implemented as comparisons against zero
440        // to follow how clang's libcxx implements their equivalents in
441        // <https://github.com/llvm/llvm-project/blob/60486292b79885b7800b082754153202bef5b1f0/libcxx/include/__compare/is_eq.h#L23-L28>
442
443        self.as_raw() == 0
444    }
445
446    /// Returns `true` if the ordering is not the `Equal` variant.
447    ///
448    /// # Examples
449    ///
450    /// ```
451    /// use std::cmp::Ordering;
452    ///
453    /// assert_eq!(Ordering::Less.is_ne(), true);
454    /// assert_eq!(Ordering::Equal.is_ne(), false);
455    /// assert_eq!(Ordering::Greater.is_ne(), true);
456    /// ```
457    #[inline]
458    #[must_use]
459    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
460    #[stable(feature = "ordering_helpers", since = "1.53.0")]
461    pub const fn is_ne(self) -> bool {
462        self.as_raw() != 0
463    }
464
465    /// Returns `true` if the ordering is the `Less` variant.
466    ///
467    /// # Examples
468    ///
469    /// ```
470    /// use std::cmp::Ordering;
471    ///
472    /// assert_eq!(Ordering::Less.is_lt(), true);
473    /// assert_eq!(Ordering::Equal.is_lt(), false);
474    /// assert_eq!(Ordering::Greater.is_lt(), false);
475    /// ```
476    #[inline]
477    #[must_use]
478    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
479    #[stable(feature = "ordering_helpers", since = "1.53.0")]
480    pub const fn is_lt(self) -> bool {
481        self.as_raw() < 0
482    }
483
484    /// Returns `true` if the ordering is the `Greater` variant.
485    ///
486    /// # Examples
487    ///
488    /// ```
489    /// use std::cmp::Ordering;
490    ///
491    /// assert_eq!(Ordering::Less.is_gt(), false);
492    /// assert_eq!(Ordering::Equal.is_gt(), false);
493    /// assert_eq!(Ordering::Greater.is_gt(), true);
494    /// ```
495    #[inline]
496    #[must_use]
497    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
498    #[stable(feature = "ordering_helpers", since = "1.53.0")]
499    pub const fn is_gt(self) -> bool {
500        self.as_raw() > 0
501    }
502
503    /// Returns `true` if the ordering is either the `Less` or `Equal` variant.
504    ///
505    /// # Examples
506    ///
507    /// ```
508    /// use std::cmp::Ordering;
509    ///
510    /// assert_eq!(Ordering::Less.is_le(), true);
511    /// assert_eq!(Ordering::Equal.is_le(), true);
512    /// assert_eq!(Ordering::Greater.is_le(), false);
513    /// ```
514    #[inline]
515    #[must_use]
516    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
517    #[stable(feature = "ordering_helpers", since = "1.53.0")]
518    pub const fn is_le(self) -> bool {
519        self.as_raw() <= 0
520    }
521
522    /// Returns `true` if the ordering is either the `Greater` or `Equal` variant.
523    ///
524    /// # Examples
525    ///
526    /// ```
527    /// use std::cmp::Ordering;
528    ///
529    /// assert_eq!(Ordering::Less.is_ge(), false);
530    /// assert_eq!(Ordering::Equal.is_ge(), true);
531    /// assert_eq!(Ordering::Greater.is_ge(), true);
532    /// ```
533    #[inline]
534    #[must_use]
535    #[rustc_const_stable(feature = "ordering_helpers", since = "1.53.0")]
536    #[stable(feature = "ordering_helpers", since = "1.53.0")]
537    pub const fn is_ge(self) -> bool {
538        self.as_raw() >= 0
539    }
540
541    /// Reverses the `Ordering`.
542    ///
543    /// * `Less` becomes `Greater`.
544    /// * `Greater` becomes `Less`.
545    /// * `Equal` becomes `Equal`.
546    ///
547    /// # Examples
548    ///
549    /// Basic behavior:
550    ///
551    /// ```
552    /// use std::cmp::Ordering;
553    ///
554    /// assert_eq!(Ordering::Less.reverse(), Ordering::Greater);
555    /// assert_eq!(Ordering::Equal.reverse(), Ordering::Equal);
556    /// assert_eq!(Ordering::Greater.reverse(), Ordering::Less);
557    /// ```
558    ///
559    /// This method can be used to reverse a comparison:
560    ///
561    /// ```
562    /// let data: &mut [_] = &mut [2, 10, 5, 8];
563    ///
564    /// // sort the array from largest to smallest.
565    /// data.sort_by(|a, b| a.cmp(b).reverse());
566    ///
567    /// let b: &mut [_] = &mut [10, 8, 5, 2];
568    /// assert!(data == b);
569    /// ```
570    #[inline]
571    #[must_use]
572    #[rustc_const_stable(feature = "const_ordering", since = "1.48.0")]
573    #[stable(feature = "rust1", since = "1.0.0")]
574    pub const fn reverse(self) -> Ordering {
575        match self {
576            Less => Greater,
577            Equal => Equal,
578            Greater => Less,
579        }
580    }
581
582    /// Chains two orderings.
583    ///
584    /// Returns `self` when it's not `Equal`. Otherwise returns `other`.
585    ///
586    /// # Examples
587    ///
588    /// ```
589    /// use std::cmp::Ordering;
590    ///
591    /// let result = Ordering::Equal.then(Ordering::Less);
592    /// assert_eq!(result, Ordering::Less);
593    ///
594    /// let result = Ordering::Less.then(Ordering::Equal);
595    /// assert_eq!(result, Ordering::Less);
596    ///
597    /// let result = Ordering::Less.then(Ordering::Greater);
598    /// assert_eq!(result, Ordering::Less);
599    ///
600    /// let result = Ordering::Equal.then(Ordering::Equal);
601    /// assert_eq!(result, Ordering::Equal);
602    ///
603    /// let x: (i64, i64, i64) = (1, 2, 7);
604    /// let y: (i64, i64, i64) = (1, 5, 3);
605    /// let result = x.0.cmp(&y.0).then(x.1.cmp(&y.1)).then(x.2.cmp(&y.2));
606    ///
607    /// assert_eq!(result, Ordering::Less);
608    /// ```
609    #[inline]
610    #[must_use]
611    #[rustc_const_stable(feature = "const_ordering", since = "1.48.0")]
612    #[stable(feature = "ordering_chaining", since = "1.17.0")]
613    pub const fn then(self, other: Ordering) -> Ordering {
614        match self {
615            Equal => other,
616            _ => self,
617        }
618    }
619
620    /// Chains the ordering with the given function.
621    ///
622    /// Returns `self` when it's not `Equal`. Otherwise calls `f` and returns
623    /// the result.
624    ///
625    /// # Examples
626    ///
627    /// ```
628    /// use std::cmp::Ordering;
629    ///
630    /// let result = Ordering::Equal.then_with(|| Ordering::Less);
631    /// assert_eq!(result, Ordering::Less);
632    ///
633    /// let result = Ordering::Less.then_with(|| Ordering::Equal);
634    /// assert_eq!(result, Ordering::Less);
635    ///
636    /// let result = Ordering::Less.then_with(|| Ordering::Greater);
637    /// assert_eq!(result, Ordering::Less);
638    ///
639    /// let result = Ordering::Equal.then_with(|| Ordering::Equal);
640    /// assert_eq!(result, Ordering::Equal);
641    ///
642    /// let x: (i64, i64, i64) = (1, 2, 7);
643    /// let y: (i64, i64, i64) = (1, 5, 3);
644    /// let result = x.0.cmp(&y.0).then_with(|| x.1.cmp(&y.1)).then_with(|| x.2.cmp(&y.2));
645    ///
646    /// assert_eq!(result, Ordering::Less);
647    /// ```
648    #[inline]
649    #[must_use]
650    #[stable(feature = "ordering_chaining", since = "1.17.0")]
651    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
652    pub const fn then_with<F>(self, f: F) -> Ordering
653    where
654        F: [const] FnOnce() -> Ordering + [const] Destruct,
655    {
656        match self {
657            Equal => f(),
658            _ => self,
659        }
660    }
661}
662
663/// A helper struct for reverse ordering.
664///
665/// This struct is a helper to be used with functions like [`Vec::sort_by_key`] and
666/// can be used to reverse order a part of a key.
667///
668/// [`Vec::sort_by_key`]: ../../std/vec/struct.Vec.html#method.sort_by_key
669///
670/// # Examples
671///
672/// ```
673/// use std::cmp::Reverse;
674///
675/// let mut v = vec![1, 2, 3, 4, 5, 6];
676/// v.sort_by_key(|&num| (num > 3, Reverse(num)));
677/// assert_eq!(v, vec![3, 2, 1, 6, 5, 4]);
678/// ```
679#[derive(Copy, Debug, Hash)]
680#[derive_const(PartialEq, Eq, Default)]
681#[stable(feature = "reverse_cmp_key", since = "1.19.0")]
682#[repr(transparent)]
683pub struct Reverse<T>(#[stable(feature = "reverse_cmp_key", since = "1.19.0")] pub T);
684
685#[stable(feature = "reverse_cmp_key", since = "1.19.0")]
686#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
687impl<T: [const] PartialOrd> const PartialOrd for Reverse<T> {
688    #[inline]
689    fn partial_cmp(&self, other: &Reverse<T>) -> Option<Ordering> {
690        other.0.partial_cmp(&self.0)
691    }
692
693    #[inline]
694    fn lt(&self, other: &Self) -> bool {
695        other.0 < self.0
696    }
697    #[inline]
698    fn le(&self, other: &Self) -> bool {
699        other.0 <= self.0
700    }
701    #[inline]
702    fn gt(&self, other: &Self) -> bool {
703        other.0 > self.0
704    }
705    #[inline]
706    fn ge(&self, other: &Self) -> bool {
707        other.0 >= self.0
708    }
709}
710
711#[stable(feature = "reverse_cmp_key", since = "1.19.0")]
712#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
713impl<T: [const] Ord> const Ord for Reverse<T> {
714    #[inline]
715    fn cmp(&self, other: &Reverse<T>) -> Ordering {
716        other.0.cmp(&self.0)
717    }
718}
719
720#[stable(feature = "reverse_cmp_key", since = "1.19.0")]
721impl<T: Clone> Clone for Reverse<T> {
722    #[inline]
723    fn clone(&self) -> Reverse<T> {
724        Reverse(self.0.clone())
725    }
726
727    #[inline]
728    fn clone_from(&mut self, source: &Self) {
729        self.0.clone_from(&source.0)
730    }
731}
732
733/// Trait for types that form a [total order](https://en.wikipedia.org/wiki/Total_order).
734///
735/// Implementations must be consistent with the [`PartialOrd`] implementation, and ensure `max`,
736/// `min`, and `clamp` are consistent with `cmp`:
737///
738/// - `partial_cmp(a, b) == Some(cmp(a, b))`.
739/// - `max(a, b) == max_by(a, b, cmp)` (ensured by the default implementation).
740/// - `min(a, b) == min_by(a, b, cmp)` (ensured by the default implementation).
741/// - For `a.clamp(min, max)`, see the [method docs](#method.clamp) (ensured by the default
742///   implementation).
743///
744/// Violating these requirements is a logic error. The behavior resulting from a logic error is not
745/// specified, but users of the trait must ensure that such logic errors do *not* result in
746/// undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these
747/// methods.
748///
749/// ## Corollaries
750///
751/// From the above and the requirements of `PartialOrd`, it follows that for all `a`, `b` and `c`:
752///
753/// - exactly one of `a < b`, `a == b` or `a > b` is true; and
754/// - `<` is transitive: `a < b` and `b < c` implies `a < c`. The same must hold for both `==` and
755///   `>`.
756///
757/// Mathematically speaking, the `<` operator defines a strict [weak order]. In cases where `==`
758/// conforms to mathematical equality, it also defines a strict [total order].
759///
760/// [weak order]: https://en.wikipedia.org/wiki/Weak_ordering
761/// [total order]: https://en.wikipedia.org/wiki/Total_order
762///
763/// ## Derivable
764///
765/// This trait can be used with `#[derive]`.
766///
767/// When `derive`d on structs, it will produce a
768/// [lexicographic](https://en.wikipedia.org/wiki/Lexicographic_order) ordering based on the
769/// top-to-bottom declaration order of the struct's members.
770///
771/// When `derive`d on enums, variants are ordered primarily by their discriminants. Secondarily,
772/// they are ordered by their fields. By default, the discriminant is smallest for variants at the
773/// top, and largest for variants at the bottom. Here's an example:
774///
775/// ```
776/// #[derive(PartialEq, Eq, PartialOrd, Ord)]
777/// enum E {
778///     Top,
779///     Bottom,
780/// }
781///
782/// assert!(E::Top < E::Bottom);
783/// ```
784///
785/// However, manually setting the discriminants can override this default behavior:
786///
787/// ```
788/// #[derive(PartialEq, Eq, PartialOrd, Ord)]
789/// enum E {
790///     Top = 2,
791///     Bottom = 1,
792/// }
793///
794/// assert!(E::Bottom < E::Top);
795/// ```
796///
797/// ## Lexicographical comparison
798///
799/// Lexicographical comparison is an operation with the following properties:
800///  - Two sequences are compared element by element.
801///  - The first mismatching element defines which sequence is lexicographically less or greater
802///    than the other.
803///  - If one sequence is a prefix of another, the shorter sequence is lexicographically less than
804///    the other.
805///  - If two sequences have equivalent elements and are of the same length, then the sequences are
806///    lexicographically equal.
807///  - An empty sequence is lexicographically less than any non-empty sequence.
808///  - Two empty sequences are lexicographically equal.
809///
810/// ## How can I implement `Ord`?
811///
812/// `Ord` requires that the type also be [`PartialOrd`], [`PartialEq`], and [`Eq`].
813///
814/// Because `Ord` implies a stronger ordering relationship than [`PartialOrd`], and both `Ord` and
815/// [`PartialOrd`] must agree, you must choose how to implement `Ord` **first**. You can choose to
816/// derive it, or implement it manually. If you derive it, you should derive all four traits. If you
817/// implement it manually, you should manually implement all four traits, based on the
818/// implementation of `Ord`.
819///
820/// Here's an example where you want to define the `Character` comparison by `health` and
821/// `experience` only, disregarding the field `mana`:
822///
823/// ```
824/// use std::cmp::Ordering;
825///
826/// struct Character {
827///     health: u32,
828///     experience: u32,
829///     mana: f32,
830/// }
831///
832/// impl Ord for Character {
833///     fn cmp(&self, other: &Self) -> Ordering {
834///         self.experience
835///             .cmp(&other.experience)
836///             .then(self.health.cmp(&other.health))
837///     }
838/// }
839///
840/// impl PartialOrd for Character {
841///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
842///         Some(self.cmp(other))
843///     }
844/// }
845///
846/// impl PartialEq for Character {
847///     fn eq(&self, other: &Self) -> bool {
848///         self.health == other.health && self.experience == other.experience
849///     }
850/// }
851///
852/// impl Eq for Character {}
853/// ```
854///
855/// If all you need is to `slice::sort` a type by a field value, it can be simpler to use
856/// `slice::sort_by_key`.
857///
858/// ## Examples of incorrect `Ord` implementations
859///
860/// ```
861/// use std::cmp::Ordering;
862///
863/// #[derive(Debug)]
864/// struct Character {
865///     health: f32,
866/// }
867///
868/// impl Ord for Character {
869///     fn cmp(&self, other: &Self) -> std::cmp::Ordering {
870///         if self.health < other.health {
871///             Ordering::Less
872///         } else if self.health > other.health {
873///             Ordering::Greater
874///         } else {
875///             Ordering::Equal
876///         }
877///     }
878/// }
879///
880/// impl PartialOrd for Character {
881///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
882///         Some(self.cmp(other))
883///     }
884/// }
885///
886/// impl PartialEq for Character {
887///     fn eq(&self, other: &Self) -> bool {
888///         self.health == other.health
889///     }
890/// }
891///
892/// impl Eq for Character {}
893///
894/// let a = Character { health: 4.5 };
895/// let b = Character { health: f32::NAN };
896///
897/// // Mistake: floating-point values do not form a total order and using the built-in comparison
898/// // operands to implement `Ord` irregardless of that reality does not change it. Use
899/// // `f32::total_cmp` if you need a total order for floating-point values.
900///
901/// // Reflexivity requirement of `Ord` is not given.
902/// assert!(a == a);
903/// assert!(b != b);
904///
905/// // Antisymmetry requirement of `Ord` is not given. Only one of a < c and c < a is allowed to be
906/// // true, not both or neither.
907/// assert_eq!((a < b) as u8 + (b < a) as u8, 0);
908/// ```
909///
910/// ```
911/// use std::cmp::Ordering;
912///
913/// #[derive(Debug)]
914/// struct Character {
915///     health: u32,
916///     experience: u32,
917/// }
918///
919/// impl PartialOrd for Character {
920///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
921///         Some(self.cmp(other))
922///     }
923/// }
924///
925/// impl Ord for Character {
926///     fn cmp(&self, other: &Self) -> std::cmp::Ordering {
927///         if self.health < 50 {
928///             self.health.cmp(&other.health)
929///         } else {
930///             self.experience.cmp(&other.experience)
931///         }
932///     }
933/// }
934///
935/// // For performance reasons implementing `PartialEq` this way is not the idiomatic way, but it
936/// // ensures consistent behavior between `PartialEq`, `PartialOrd` and `Ord` in this example.
937/// impl PartialEq for Character {
938///     fn eq(&self, other: &Self) -> bool {
939///         self.cmp(other) == Ordering::Equal
940///     }
941/// }
942///
943/// impl Eq for Character {}
944///
945/// let a = Character {
946///     health: 3,
947///     experience: 5,
948/// };
949/// let b = Character {
950///     health: 10,
951///     experience: 77,
952/// };
953/// let c = Character {
954///     health: 143,
955///     experience: 2,
956/// };
957///
958/// // Mistake: The implementation of `Ord` compares different fields depending on the value of
959/// // `self.health`, the resulting order is not total.
960///
961/// // Transitivity requirement of `Ord` is not given. If a is smaller than b and b is smaller than
962/// // c, by transitive property a must also be smaller than c.
963/// assert!(a < b && b < c && c < a);
964///
965/// // Antisymmetry requirement of `Ord` is not given. Only one of a < c and c < a is allowed to be
966/// // true, not both or neither.
967/// assert_eq!((a < c) as u8 + (c < a) as u8, 2);
968/// ```
969///
970/// The documentation of [`PartialOrd`] contains further examples, for example it's wrong for
971/// [`PartialOrd`] and [`PartialEq`] to disagree.
972///
973/// [`cmp`]: Ord::cmp
974#[doc(alias = "<")]
975#[doc(alias = ">")]
976#[doc(alias = "<=")]
977#[doc(alias = ">=")]
978#[stable(feature = "rust1", since = "1.0.0")]
979#[rustc_diagnostic_item = "Ord"]
980#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
981pub const trait Ord: [const] Eq + [const] PartialOrd<Self> + PointeeSized {
982    /// This method returns an [`Ordering`] between `self` and `other`.
983    ///
984    /// By convention, `self.cmp(&other)` returns the ordering matching the expression
985    /// `self <operator> other` if true.
986    ///
987    /// # Examples
988    ///
989    /// ```
990    /// use std::cmp::Ordering;
991    ///
992    /// assert_eq!(5.cmp(&10), Ordering::Less);
993    /// assert_eq!(10.cmp(&5), Ordering::Greater);
994    /// assert_eq!(5.cmp(&5), Ordering::Equal);
995    /// ```
996    #[must_use]
997    #[stable(feature = "rust1", since = "1.0.0")]
998    #[rustc_diagnostic_item = "ord_cmp_method"]
999    fn cmp(&self, other: &Self) -> Ordering;
1000
1001    /// Compares and returns the maximum of two values.
1002    ///
1003    /// Returns the second argument if the comparison determines them to be equal.
1004    ///
1005    /// # Examples
1006    ///
1007    /// ```
1008    /// assert_eq!(1.max(2), 2);
1009    /// assert_eq!(2.max(2), 2);
1010    /// ```
1011    /// ```
1012    /// use std::cmp::Ordering;
1013    ///
1014    /// #[derive(Eq)]
1015    /// struct Equal(&'static str);
1016    ///
1017    /// impl PartialEq for Equal {
1018    ///     fn eq(&self, other: &Self) -> bool { true }
1019    /// }
1020    /// impl PartialOrd for Equal {
1021    ///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
1022    /// }
1023    /// impl Ord for Equal {
1024    ///     fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
1025    /// }
1026    ///
1027    /// assert_eq!(Equal("self").max(Equal("other")).0, "other");
1028    /// ```
1029    #[stable(feature = "ord_max_min", since = "1.21.0")]
1030    #[inline]
1031    #[must_use]
1032    #[rustc_diagnostic_item = "cmp_ord_max"]
1033    fn max(self, other: Self) -> Self
1034    where
1035        Self: Sized + [const] Destruct,
1036    {
1037        if other < self { self } else { other }
1038    }
1039
1040    /// Compares and returns the minimum of two values.
1041    ///
1042    /// Returns the first argument if the comparison determines them to be equal.
1043    ///
1044    /// # Examples
1045    ///
1046    /// ```
1047    /// assert_eq!(1.min(2), 1);
1048    /// assert_eq!(2.min(2), 2);
1049    /// ```
1050    /// ```
1051    /// use std::cmp::Ordering;
1052    ///
1053    /// #[derive(Eq)]
1054    /// struct Equal(&'static str);
1055    ///
1056    /// impl PartialEq for Equal {
1057    ///     fn eq(&self, other: &Self) -> bool { true }
1058    /// }
1059    /// impl PartialOrd for Equal {
1060    ///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
1061    /// }
1062    /// impl Ord for Equal {
1063    ///     fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
1064    /// }
1065    ///
1066    /// assert_eq!(Equal("self").min(Equal("other")).0, "self");
1067    /// ```
1068    #[stable(feature = "ord_max_min", since = "1.21.0")]
1069    #[inline]
1070    #[must_use]
1071    #[rustc_diagnostic_item = "cmp_ord_min"]
1072    fn min(self, other: Self) -> Self
1073    where
1074        Self: Sized + [const] Destruct,
1075    {
1076        if other < self { other } else { self }
1077    }
1078
1079    /// Restrict a value to a certain interval.
1080    ///
1081    /// Returns `max` if `self` is greater than `max`, and `min` if `self` is
1082    /// less than `min`. Otherwise this returns `self`.
1083    ///
1084    /// # Panics
1085    ///
1086    /// Panics if `min > max`.
1087    ///
1088    /// # Examples
1089    ///
1090    /// ```
1091    /// assert_eq!((-3).clamp(-2, 1), -2);
1092    /// assert_eq!(0.clamp(-2, 1), 0);
1093    /// assert_eq!(2.clamp(-2, 1), 1);
1094    /// ```
1095    #[must_use]
1096    #[inline]
1097    #[stable(feature = "clamp", since = "1.50.0")]
1098    fn clamp(self, min: Self, max: Self) -> Self
1099    where
1100        Self: Sized + [const] Destruct,
1101    {
1102        assert!(min <= max);
1103        if self < min {
1104            min
1105        } else if self > max {
1106            max
1107        } else {
1108            self
1109        }
1110    }
1111}
1112
1113/// Derive macro generating an impl of the trait [`Ord`].
1114/// The behavior of this macro is described in detail [here](Ord#derivable).
1115#[rustc_builtin_macro]
1116#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
1117#[allow_internal_unstable(core_intrinsics)]
1118pub macro Ord($item:item) {
1119    /* compiler built-in */
1120}
1121
1122/// Trait for types that form a [partial order](https://en.wikipedia.org/wiki/Partial_order).
1123///
1124/// The `lt`, `le`, `gt`, and `ge` methods of this trait can be called using the `<`, `<=`, `>`, and
1125/// `>=` operators, respectively.
1126///
1127/// This trait should **only** contain the comparison logic for a type **if one plans on only
1128/// implementing `PartialOrd` but not [`Ord`]**. Otherwise the comparison logic should be in [`Ord`]
1129/// and this trait implemented with `Some(self.cmp(other))`.
1130///
1131/// The methods of this trait must be consistent with each other and with those of [`PartialEq`].
1132/// The following conditions must hold:
1133///
1134/// 1. `a == b` if and only if `partial_cmp(a, b) == Some(Equal)`.
1135/// 2. `a < b` if and only if `partial_cmp(a, b) == Some(Less)`
1136/// 3. `a > b` if and only if `partial_cmp(a, b) == Some(Greater)`
1137/// 4. `a <= b` if and only if `a < b || a == b`
1138/// 5. `a >= b` if and only if `a > b || a == b`
1139/// 6. `a != b` if and only if `!(a == b)`.
1140///
1141/// Conditions 2–5 above are ensured by the default implementation. Condition 6 is already ensured
1142/// by [`PartialEq`].
1143///
1144/// If [`Ord`] is also implemented for `Self` and `Rhs`, it must also be consistent with
1145/// `partial_cmp` (see the documentation of that trait for the exact requirements). It's easy to
1146/// accidentally make them disagree by deriving some of the traits and manually implementing others.
1147///
1148/// The comparison relations must satisfy the following conditions (for all `a`, `b`, `c` of type
1149/// `A`, `B`, `C`):
1150///
1151/// - **Transitivity**: if `A: PartialOrd<B>` and `B: PartialOrd<C>` and `A: PartialOrd<C>`, then `a
1152///   < b` and `b < c` implies `a < c`. The same must hold for both `==` and `>`. This must also
1153///   work for longer chains, such as when `A: PartialOrd<B>`, `B: PartialOrd<C>`, `C:
1154///   PartialOrd<D>`, and `A: PartialOrd<D>` all exist.
1155/// - **Duality**: if `A: PartialOrd<B>` and `B: PartialOrd<A>`, then `a < b` if and only if `b >
1156///   a`.
1157///
1158/// Note that the `B: PartialOrd<A>` (dual) and `A: PartialOrd<C>` (transitive) impls are not forced
1159/// to exist, but these requirements apply whenever they do exist.
1160///
1161/// Violating these requirements is a logic error. The behavior resulting from a logic error is not
1162/// specified, but users of the trait must ensure that such logic errors do *not* result in
1163/// undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these
1164/// methods.
1165///
1166/// ## Cross-crate considerations
1167///
1168/// Upholding the requirements stated above can become tricky when one crate implements `PartialOrd`
1169/// for a type of another crate (i.e., to allow comparing one of its own types with a type from the
1170/// standard library). The recommendation is to never implement this trait for a foreign type. In
1171/// other words, such a crate should do `impl PartialOrd<ForeignType> for LocalType`, but it should
1172/// *not* do `impl PartialOrd<LocalType> for ForeignType`.
1173///
1174/// This avoids the problem of transitive chains that criss-cross crate boundaries: for all local
1175/// types `T`, you may assume that no other crate will add `impl`s that allow comparing `T < U`. In
1176/// other words, if other crates add `impl`s that allow building longer transitive chains `U1 < ...
1177/// < T < V1 < ...`, then all the types that appear to the right of `T` must be types that the crate
1178/// defining `T` already knows about. This rules out transitive chains where downstream crates can
1179/// add new `impl`s that "stitch together" comparisons of foreign types in ways that violate
1180/// transitivity.
1181///
1182/// Not having such foreign `impl`s also avoids forward compatibility issues where one crate adding
1183/// more `PartialOrd` implementations can cause build failures in downstream crates.
1184///
1185/// ## Corollaries
1186///
1187/// The following corollaries follow from the above requirements:
1188///
1189/// - irreflexivity of `<` and `>`: `!(a < a)`, `!(a > a)`
1190/// - transitivity of `>`: if `a > b` and `b > c` then `a > c`
1191/// - duality of `partial_cmp`: `partial_cmp(a, b) == partial_cmp(b, a).map(Ordering::reverse)`
1192///
1193/// ## Strict and non-strict partial orders
1194///
1195/// The `<` and `>` operators behave according to a *strict* partial order. However, `<=` and `>=`
1196/// do **not** behave according to a *non-strict* partial order. That is because mathematically, a
1197/// non-strict partial order would require reflexivity, i.e. `a <= a` would need to be true for
1198/// every `a`. This isn't always the case for types that implement `PartialOrd`, for example:
1199///
1200/// ```
1201/// let a = f64::NAN;
1202/// assert_eq!(a <= a, false);
1203/// ```
1204///
1205/// ## Derivable
1206///
1207/// This trait can be used with `#[derive]`.
1208///
1209/// When `derive`d on structs, it will produce a
1210/// [lexicographic](https://en.wikipedia.org/wiki/Lexicographic_order) ordering based on the
1211/// top-to-bottom declaration order of the struct's members.
1212///
1213/// When `derive`d on enums, variants are primarily ordered by their discriminants. Secondarily,
1214/// they are ordered by their fields. By default, the discriminant is smallest for variants at the
1215/// top, and largest for variants at the bottom. Here's an example:
1216///
1217/// ```
1218/// #[derive(PartialEq, PartialOrd)]
1219/// enum E {
1220///     Top,
1221///     Bottom,
1222/// }
1223///
1224/// assert!(E::Top < E::Bottom);
1225/// ```
1226///
1227/// However, manually setting the discriminants can override this default behavior:
1228///
1229/// ```
1230/// #[derive(PartialEq, PartialOrd)]
1231/// enum E {
1232///     Top = 2,
1233///     Bottom = 1,
1234/// }
1235///
1236/// assert!(E::Bottom < E::Top);
1237/// ```
1238///
1239/// ## How can I implement `PartialOrd`?
1240///
1241/// `PartialOrd` only requires implementation of the [`partial_cmp`] method, with the others
1242/// generated from default implementations.
1243///
1244/// However it remains possible to implement the others separately for types which do not have a
1245/// total order. For example, for floating point numbers, `NaN < 0 == false` and `NaN >= 0 == false`
1246/// (cf. IEEE 754-2008 section 5.11).
1247///
1248/// `PartialOrd` requires your type to be [`PartialEq`].
1249///
1250/// If your type is [`Ord`], you can implement [`partial_cmp`] by using [`cmp`]:
1251///
1252/// ```
1253/// use std::cmp::Ordering;
1254///
1255/// struct Person {
1256///     id: u32,
1257///     name: String,
1258///     height: u32,
1259/// }
1260///
1261/// impl PartialOrd for Person {
1262///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
1263///         Some(self.cmp(other))
1264///     }
1265/// }
1266///
1267/// impl Ord for Person {
1268///     fn cmp(&self, other: &Self) -> Ordering {
1269///         self.height.cmp(&other.height)
1270///     }
1271/// }
1272///
1273/// impl PartialEq for Person {
1274///     fn eq(&self, other: &Self) -> bool {
1275///         self.height == other.height
1276///     }
1277/// }
1278///
1279/// impl Eq for Person {}
1280/// ```
1281///
1282/// You may also find it useful to use [`partial_cmp`] on your type's fields. Here is an example of
1283/// `Person` types who have a floating-point `height` field that is the only field to be used for
1284/// sorting:
1285///
1286/// ```
1287/// use std::cmp::Ordering;
1288///
1289/// struct Person {
1290///     id: u32,
1291///     name: String,
1292///     height: f64,
1293/// }
1294///
1295/// impl PartialOrd for Person {
1296///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
1297///         self.height.partial_cmp(&other.height)
1298///     }
1299/// }
1300///
1301/// impl PartialEq for Person {
1302///     fn eq(&self, other: &Self) -> bool {
1303///         self.height == other.height
1304///     }
1305/// }
1306/// ```
1307///
1308/// ## Examples of incorrect `PartialOrd` implementations
1309///
1310/// ```
1311/// use std::cmp::Ordering;
1312///
1313/// #[derive(PartialEq, Debug)]
1314/// struct Character {
1315///     health: u32,
1316///     experience: u32,
1317/// }
1318///
1319/// impl PartialOrd for Character {
1320///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
1321///         Some(self.health.cmp(&other.health))
1322///     }
1323/// }
1324///
1325/// let a = Character {
1326///     health: 10,
1327///     experience: 5,
1328/// };
1329/// let b = Character {
1330///     health: 10,
1331///     experience: 77,
1332/// };
1333///
1334/// // Mistake: `PartialEq` and `PartialOrd` disagree with each other.
1335///
1336/// assert_eq!(a.partial_cmp(&b).unwrap(), Ordering::Equal); // a == b according to `PartialOrd`.
1337/// assert_ne!(a, b); // a != b according to `PartialEq`.
1338/// ```
1339///
1340/// # Examples
1341///
1342/// ```
1343/// let x: u32 = 0;
1344/// let y: u32 = 1;
1345///
1346/// assert_eq!(x < y, true);
1347/// assert_eq!(x.lt(&y), true);
1348/// ```
1349///
1350/// [`partial_cmp`]: PartialOrd::partial_cmp
1351/// [`cmp`]: Ord::cmp
1352#[lang = "partial_ord"]
1353#[stable(feature = "rust1", since = "1.0.0")]
1354#[doc(alias = ">")]
1355#[doc(alias = "<")]
1356#[doc(alias = "<=")]
1357#[doc(alias = ">=")]
1358#[rustc_on_unimplemented(
1359    message = "can't compare `{Self}` with `{Rhs}`",
1360    label = "no implementation for `{Self} < {Rhs}` and `{Self} > {Rhs}`",
1361    append_const_msg
1362)]
1363#[rustc_diagnostic_item = "PartialOrd"]
1364#[allow(multiple_supertrait_upcastable)] // FIXME(sized_hierarchy): remove this
1365#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1366pub const trait PartialOrd<Rhs: PointeeSized = Self>:
1367    [const] PartialEq<Rhs> + PointeeSized
1368{
1369    /// This method returns an ordering between `self` and `other` values if one exists.
1370    ///
1371    /// # Examples
1372    ///
1373    /// ```
1374    /// use std::cmp::Ordering;
1375    ///
1376    /// let result = 1.0.partial_cmp(&2.0);
1377    /// assert_eq!(result, Some(Ordering::Less));
1378    ///
1379    /// let result = 1.0.partial_cmp(&1.0);
1380    /// assert_eq!(result, Some(Ordering::Equal));
1381    ///
1382    /// let result = 2.0.partial_cmp(&1.0);
1383    /// assert_eq!(result, Some(Ordering::Greater));
1384    /// ```
1385    ///
1386    /// When comparison is impossible:
1387    ///
1388    /// ```
1389    /// let result = f64::NAN.partial_cmp(&1.0);
1390    /// assert_eq!(result, None);
1391    /// ```
1392    #[must_use]
1393    #[stable(feature = "rust1", since = "1.0.0")]
1394    #[rustc_diagnostic_item = "cmp_partialord_cmp"]
1395    fn partial_cmp(&self, other: &Rhs) -> Option<Ordering>;
1396
1397    /// Tests less than (for `self` and `other`) and is used by the `<` operator.
1398    ///
1399    /// # Examples
1400    ///
1401    /// ```
1402    /// assert_eq!(1.0 < 1.0, false);
1403    /// assert_eq!(1.0 < 2.0, true);
1404    /// assert_eq!(2.0 < 1.0, false);
1405    /// ```
1406    #[inline]
1407    #[must_use]
1408    #[stable(feature = "rust1", since = "1.0.0")]
1409    #[rustc_diagnostic_item = "cmp_partialord_lt"]
1410    fn lt(&self, other: &Rhs) -> bool {
1411        self.partial_cmp(other).is_some_and(Ordering::is_lt)
1412    }
1413
1414    /// Tests less than or equal to (for `self` and `other`) and is used by the
1415    /// `<=` operator.
1416    ///
1417    /// # Examples
1418    ///
1419    /// ```
1420    /// assert_eq!(1.0 <= 1.0, true);
1421    /// assert_eq!(1.0 <= 2.0, true);
1422    /// assert_eq!(2.0 <= 1.0, false);
1423    /// ```
1424    #[inline]
1425    #[must_use]
1426    #[stable(feature = "rust1", since = "1.0.0")]
1427    #[rustc_diagnostic_item = "cmp_partialord_le"]
1428    fn le(&self, other: &Rhs) -> bool {
1429        self.partial_cmp(other).is_some_and(Ordering::is_le)
1430    }
1431
1432    /// Tests greater than (for `self` and `other`) and is used by the `>`
1433    /// operator.
1434    ///
1435    /// # Examples
1436    ///
1437    /// ```
1438    /// assert_eq!(1.0 > 1.0, false);
1439    /// assert_eq!(1.0 > 2.0, false);
1440    /// assert_eq!(2.0 > 1.0, true);
1441    /// ```
1442    #[inline]
1443    #[must_use]
1444    #[stable(feature = "rust1", since = "1.0.0")]
1445    #[rustc_diagnostic_item = "cmp_partialord_gt"]
1446    fn gt(&self, other: &Rhs) -> bool {
1447        self.partial_cmp(other).is_some_and(Ordering::is_gt)
1448    }
1449
1450    /// Tests greater than or equal to (for `self` and `other`) and is used by
1451    /// the `>=` operator.
1452    ///
1453    /// # Examples
1454    ///
1455    /// ```
1456    /// assert_eq!(1.0 >= 1.0, true);
1457    /// assert_eq!(1.0 >= 2.0, false);
1458    /// assert_eq!(2.0 >= 1.0, true);
1459    /// ```
1460    #[inline]
1461    #[must_use]
1462    #[stable(feature = "rust1", since = "1.0.0")]
1463    #[rustc_diagnostic_item = "cmp_partialord_ge"]
1464    fn ge(&self, other: &Rhs) -> bool {
1465        self.partial_cmp(other).is_some_and(Ordering::is_ge)
1466    }
1467
1468    /// If `self == other`, returns `ControlFlow::Continue(())`.
1469    /// Otherwise, returns `ControlFlow::Break(self < other)`.
1470    ///
1471    /// This is useful for chaining together calls when implementing a lexical
1472    /// `PartialOrd::lt`, as it allows types (like primitives) which can cheaply
1473    /// check `==` and `<` separately to do rather than needing to calculate
1474    /// (then optimize out) the three-way `Ordering` result.
1475    #[inline]
1476    // Added to improve the behaviour of tuples; not necessarily stabilization-track.
1477    #[unstable(feature = "partial_ord_chaining_methods", issue = "none")]
1478    #[doc(hidden)]
1479    fn __chaining_lt(&self, other: &Rhs) -> ControlFlow<bool> {
1480        default_chaining_impl(self, other, Ordering::is_lt)
1481    }
1482
1483    /// Same as `__chaining_lt`, but for `<=` instead of `<`.
1484    #[inline]
1485    #[unstable(feature = "partial_ord_chaining_methods", issue = "none")]
1486    #[doc(hidden)]
1487    fn __chaining_le(&self, other: &Rhs) -> ControlFlow<bool> {
1488        default_chaining_impl(self, other, Ordering::is_le)
1489    }
1490
1491    /// Same as `__chaining_lt`, but for `>` instead of `<`.
1492    #[inline]
1493    #[unstable(feature = "partial_ord_chaining_methods", issue = "none")]
1494    #[doc(hidden)]
1495    fn __chaining_gt(&self, other: &Rhs) -> ControlFlow<bool> {
1496        default_chaining_impl(self, other, Ordering::is_gt)
1497    }
1498
1499    /// Same as `__chaining_lt`, but for `>=` instead of `<`.
1500    #[inline]
1501    #[unstable(feature = "partial_ord_chaining_methods", issue = "none")]
1502    #[doc(hidden)]
1503    fn __chaining_ge(&self, other: &Rhs) -> ControlFlow<bool> {
1504        default_chaining_impl(self, other, Ordering::is_ge)
1505    }
1506}
1507
1508#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1509const fn default_chaining_impl<T, U>(
1510    lhs: &T,
1511    rhs: &U,
1512    p: impl [const] FnOnce(Ordering) -> bool + [const] Destruct,
1513) -> ControlFlow<bool>
1514where
1515    T: [const] PartialOrd<U> + PointeeSized,
1516    U: PointeeSized,
1517{
1518    // It's important that this only call `partial_cmp` once, not call `eq` then
1519    // one of the relational operators.  We don't want to `bcmp`-then-`memcp` a
1520    // `String`, for example, or similarly for other data structures (#108157).
1521    match <T as PartialOrd<U>>::partial_cmp(lhs, rhs) {
1522        Some(Equal) => ControlFlow::Continue(()),
1523        Some(c) => ControlFlow::Break(p(c)),
1524        None => ControlFlow::Break(false),
1525    }
1526}
1527
1528/// Derive macro generating an impl of the trait [`PartialOrd`].
1529/// The behavior of this macro is described in detail [here](PartialOrd#derivable).
1530#[rustc_builtin_macro]
1531#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
1532#[allow_internal_unstable(core_intrinsics)]
1533pub macro PartialOrd($item:item) {
1534    /* compiler built-in */
1535}
1536
1537/// Compares and returns the minimum of two values.
1538///
1539/// Returns the first argument if the comparison determines them to be equal.
1540///
1541/// Internally uses an alias to [`Ord::min`].
1542///
1543/// # Examples
1544///
1545/// ```
1546/// use std::cmp;
1547///
1548/// assert_eq!(cmp::min(1, 2), 1);
1549/// assert_eq!(cmp::min(2, 2), 2);
1550/// ```
1551/// ```
1552/// use std::cmp::{self, Ordering};
1553///
1554/// #[derive(Eq)]
1555/// struct Equal(&'static str);
1556///
1557/// impl PartialEq for Equal {
1558///     fn eq(&self, other: &Self) -> bool { true }
1559/// }
1560/// impl PartialOrd for Equal {
1561///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
1562/// }
1563/// impl Ord for Equal {
1564///     fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
1565/// }
1566///
1567/// assert_eq!(cmp::min(Equal("v1"), Equal("v2")).0, "v1");
1568/// ```
1569#[inline]
1570#[must_use]
1571#[stable(feature = "rust1", since = "1.0.0")]
1572#[rustc_diagnostic_item = "cmp_min"]
1573#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1574pub const fn min<T: [const] Ord + [const] Destruct>(v1: T, v2: T) -> T {
1575    v1.min(v2)
1576}
1577
1578/// Returns the minimum of two values with respect to the specified comparison function.
1579///
1580/// Returns the first argument if the comparison determines them to be equal.
1581///
1582/// The parameter order is preserved when calling the `compare` function, i.e. `v1` is
1583/// always passed as the first argument and `v2` as the second.
1584///
1585/// # Examples
1586///
1587/// ```
1588/// use std::cmp;
1589///
1590/// let abs_cmp = |x: &i32, y: &i32| x.abs().cmp(&y.abs());
1591///
1592/// let result = cmp::min_by(2, -1, abs_cmp);
1593/// assert_eq!(result, -1);
1594///
1595/// let result = cmp::min_by(2, -3, abs_cmp);
1596/// assert_eq!(result, 2);
1597///
1598/// let result = cmp::min_by(1, -1, abs_cmp);
1599/// assert_eq!(result, 1);
1600/// ```
1601#[inline]
1602#[must_use]
1603#[stable(feature = "cmp_min_max_by", since = "1.53.0")]
1604#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1605pub const fn min_by<T: [const] Destruct, F: [const] FnOnce(&T, &T) -> Ordering>(
1606    v1: T,
1607    v2: T,
1608    compare: F,
1609) -> T {
1610    if compare(&v1, &v2).is_le() { v1 } else { v2 }
1611}
1612
1613/// Returns the element that gives the minimum value from the specified function.
1614///
1615/// Returns the first argument if the comparison determines them to be equal.
1616///
1617/// # Examples
1618///
1619/// ```
1620/// use std::cmp;
1621///
1622/// let result = cmp::min_by_key(2, -1, |x: &i32| x.abs());
1623/// assert_eq!(result, -1);
1624///
1625/// let result = cmp::min_by_key(2, -3, |x: &i32| x.abs());
1626/// assert_eq!(result, 2);
1627///
1628/// let result = cmp::min_by_key(1, -1, |x: &i32| x.abs());
1629/// assert_eq!(result, 1);
1630/// ```
1631#[inline]
1632#[must_use]
1633#[stable(feature = "cmp_min_max_by", since = "1.53.0")]
1634#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1635pub const fn min_by_key<T, F, K>(v1: T, v2: T, mut f: F) -> T
1636where
1637    T: [const] Destruct,
1638    F: [const] FnMut(&T) -> K + [const] Destruct,
1639    K: [const] Ord + [const] Destruct,
1640{
1641    if f(&v2) < f(&v1) { v2 } else { v1 }
1642}
1643
1644/// Compares and returns the maximum of two values.
1645///
1646/// Returns the second argument if the comparison determines them to be equal.
1647///
1648/// Internally uses an alias to [`Ord::max`].
1649///
1650/// # Examples
1651///
1652/// ```
1653/// use std::cmp;
1654///
1655/// assert_eq!(cmp::max(1, 2), 2);
1656/// assert_eq!(cmp::max(2, 2), 2);
1657/// ```
1658/// ```
1659/// use std::cmp::{self, Ordering};
1660///
1661/// #[derive(Eq)]
1662/// struct Equal(&'static str);
1663///
1664/// impl PartialEq for Equal {
1665///     fn eq(&self, other: &Self) -> bool { true }
1666/// }
1667/// impl PartialOrd for Equal {
1668///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
1669/// }
1670/// impl Ord for Equal {
1671///     fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
1672/// }
1673///
1674/// assert_eq!(cmp::max(Equal("v1"), Equal("v2")).0, "v2");
1675/// ```
1676#[inline]
1677#[must_use]
1678#[stable(feature = "rust1", since = "1.0.0")]
1679#[rustc_diagnostic_item = "cmp_max"]
1680#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1681pub const fn max<T: [const] Ord + [const] Destruct>(v1: T, v2: T) -> T {
1682    v1.max(v2)
1683}
1684
1685/// Returns the maximum of two values with respect to the specified comparison function.
1686///
1687/// Returns the second argument if the comparison determines them to be equal.
1688///
1689/// The parameter order is preserved when calling the `compare` function, i.e. `v1` is
1690/// always passed as the first argument and `v2` as the second.
1691///
1692/// # Examples
1693///
1694/// ```
1695/// use std::cmp;
1696///
1697/// let abs_cmp = |x: &i32, y: &i32| x.abs().cmp(&y.abs());
1698///
1699/// let result = cmp::max_by(3, -2, abs_cmp) ;
1700/// assert_eq!(result, 3);
1701///
1702/// let result = cmp::max_by(1, -2, abs_cmp);
1703/// assert_eq!(result, -2);
1704///
1705/// let result = cmp::max_by(1, -1, abs_cmp);
1706/// assert_eq!(result, -1);
1707/// ```
1708#[inline]
1709#[must_use]
1710#[stable(feature = "cmp_min_max_by", since = "1.53.0")]
1711#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1712pub const fn max_by<T: [const] Destruct, F: [const] FnOnce(&T, &T) -> Ordering>(
1713    v1: T,
1714    v2: T,
1715    compare: F,
1716) -> T {
1717    if compare(&v1, &v2).is_gt() { v1 } else { v2 }
1718}
1719
1720/// Returns the element that gives the maximum value from the specified function.
1721///
1722/// Returns the second argument if the comparison determines them to be equal.
1723///
1724/// # Examples
1725///
1726/// ```
1727/// use std::cmp;
1728///
1729/// let result = cmp::max_by_key(3, -2, |x: &i32| x.abs());
1730/// assert_eq!(result, 3);
1731///
1732/// let result = cmp::max_by_key(1, -2, |x: &i32| x.abs());
1733/// assert_eq!(result, -2);
1734///
1735/// let result = cmp::max_by_key(1, -1, |x: &i32| x.abs());
1736/// assert_eq!(result, -1);
1737/// ```
1738#[inline]
1739#[must_use]
1740#[stable(feature = "cmp_min_max_by", since = "1.53.0")]
1741#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1742pub const fn max_by_key<T, F, K>(v1: T, v2: T, mut f: F) -> T
1743where
1744    T: [const] Destruct,
1745    F: [const] FnMut(&T) -> K + [const] Destruct,
1746    K: [const] Ord + [const] Destruct,
1747{
1748    if f(&v2) < f(&v1) { v1 } else { v2 }
1749}
1750
1751/// Compares and sorts two values, returning minimum and maximum.
1752///
1753/// Returns `[v1, v2]` if the comparison determines them to be equal.
1754///
1755/// # Examples
1756///
1757/// ```
1758/// #![feature(cmp_minmax)]
1759/// use std::cmp;
1760///
1761/// assert_eq!(cmp::minmax(1, 2), [1, 2]);
1762/// assert_eq!(cmp::minmax(2, 1), [1, 2]);
1763///
1764/// // You can destructure the result using array patterns
1765/// let [min, max] = cmp::minmax(42, 17);
1766/// assert_eq!(min, 17);
1767/// assert_eq!(max, 42);
1768/// ```
1769/// ```
1770/// #![feature(cmp_minmax)]
1771/// use std::cmp::{self, Ordering};
1772///
1773/// #[derive(Eq)]
1774/// struct Equal(&'static str);
1775///
1776/// impl PartialEq for Equal {
1777///     fn eq(&self, other: &Self) -> bool { true }
1778/// }
1779/// impl PartialOrd for Equal {
1780///     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
1781/// }
1782/// impl Ord for Equal {
1783///     fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
1784/// }
1785///
1786/// assert_eq!(cmp::minmax(Equal("v1"), Equal("v2")).map(|v| v.0), ["v1", "v2"]);
1787/// ```
1788#[inline]
1789#[must_use]
1790#[unstable(feature = "cmp_minmax", issue = "115939")]
1791#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1792pub const fn minmax<T>(v1: T, v2: T) -> [T; 2]
1793where
1794    T: [const] Ord,
1795{
1796    if v2 < v1 { [v2, v1] } else { [v1, v2] }
1797}
1798
1799/// Returns minimum and maximum values with respect to the specified comparison function.
1800///
1801/// Returns `[v1, v2]` if the comparison determines them to be equal.
1802///
1803/// The parameter order is preserved when calling the `compare` function, i.e. `v1` is
1804/// always passed as the first argument and `v2` as the second.
1805///
1806/// # Examples
1807///
1808/// ```
1809/// #![feature(cmp_minmax)]
1810/// use std::cmp;
1811///
1812/// let abs_cmp = |x: &i32, y: &i32| x.abs().cmp(&y.abs());
1813///
1814/// assert_eq!(cmp::minmax_by(-2, 1, abs_cmp), [1, -2]);
1815/// assert_eq!(cmp::minmax_by(-1, 2, abs_cmp), [-1, 2]);
1816/// assert_eq!(cmp::minmax_by(-2, 2, abs_cmp), [-2, 2]);
1817///
1818/// // You can destructure the result using array patterns
1819/// let [min, max] = cmp::minmax_by(-42, 17, abs_cmp);
1820/// assert_eq!(min, 17);
1821/// assert_eq!(max, -42);
1822/// ```
1823#[inline]
1824#[must_use]
1825#[unstable(feature = "cmp_minmax", issue = "115939")]
1826#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1827pub const fn minmax_by<T, F>(v1: T, v2: T, compare: F) -> [T; 2]
1828where
1829    F: [const] FnOnce(&T, &T) -> Ordering,
1830{
1831    if compare(&v1, &v2).is_le() { [v1, v2] } else { [v2, v1] }
1832}
1833
1834/// Returns minimum and maximum values with respect to the specified key function.
1835///
1836/// Returns `[v1, v2]` if the comparison determines them to be equal.
1837///
1838/// # Examples
1839///
1840/// ```
1841/// #![feature(cmp_minmax)]
1842/// use std::cmp;
1843///
1844/// assert_eq!(cmp::minmax_by_key(-2, 1, |x: &i32| x.abs()), [1, -2]);
1845/// assert_eq!(cmp::minmax_by_key(-2, 2, |x: &i32| x.abs()), [-2, 2]);
1846///
1847/// // You can destructure the result using array patterns
1848/// let [min, max] = cmp::minmax_by_key(-42, 17, |x: &i32| x.abs());
1849/// assert_eq!(min, 17);
1850/// assert_eq!(max, -42);
1851/// ```
1852#[inline]
1853#[must_use]
1854#[unstable(feature = "cmp_minmax", issue = "115939")]
1855#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1856pub const fn minmax_by_key<T, F, K>(v1: T, v2: T, mut f: F) -> [T; 2]
1857where
1858    F: [const] FnMut(&T) -> K + [const] Destruct,
1859    K: [const] Ord + [const] Destruct,
1860{
1861    if f(&v2) < f(&v1) { [v2, v1] } else { [v1, v2] }
1862}
1863
1864// Implementation of PartialEq, Eq, PartialOrd and Ord for primitive types
1865mod impls {
1866    use crate::cmp::Ordering::{self, Equal, Greater, Less};
1867    use crate::hint::unreachable_unchecked;
1868    use crate::marker::PointeeSized;
1869    use crate::ops::ControlFlow::{self, Break, Continue};
1870    use crate::panic::const_assert;
1871
1872    macro_rules! partial_eq_impl {
1873        ($($t:ty)*) => ($(
1874            #[stable(feature = "rust1", since = "1.0.0")]
1875            #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1876            impl const PartialEq for $t {
1877                #[inline]
1878                fn eq(&self, other: &Self) -> bool { *self == *other }
1879                #[inline]
1880                fn ne(&self, other: &Self) -> bool { *self != *other }
1881            }
1882        )*)
1883    }
1884
1885    #[stable(feature = "rust1", since = "1.0.0")]
1886    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1887    impl const PartialEq for () {
1888        #[inline]
1889        fn eq(&self, _other: &()) -> bool {
1890            true
1891        }
1892        #[inline]
1893        fn ne(&self, _other: &()) -> bool {
1894            false
1895        }
1896    }
1897
1898    partial_eq_impl! {
1899        bool char usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 f16 f32 f64 f128
1900    }
1901
1902    macro_rules! eq_impl {
1903        ($($t:ty)*) => ($(
1904            #[stable(feature = "rust1", since = "1.0.0")]
1905            #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1906            impl const Eq for $t {}
1907        )*)
1908    }
1909
1910    eq_impl! { () bool char usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
1911
1912    #[rustfmt::skip]
1913    macro_rules! partial_ord_methods_primitive_impl {
1914        () => {
1915            #[inline(always)]
1916            fn lt(&self, other: &Self) -> bool { *self <  *other }
1917            #[inline(always)]
1918            fn le(&self, other: &Self) -> bool { *self <= *other }
1919            #[inline(always)]
1920            fn gt(&self, other: &Self) -> bool { *self >  *other }
1921            #[inline(always)]
1922            fn ge(&self, other: &Self) -> bool { *self >= *other }
1923
1924            // These implementations are the same for `Ord` or `PartialOrd` types
1925            // because if either is NAN the `==` test will fail so we end up in
1926            // the `Break` case and the comparison will correctly return `false`.
1927
1928            #[inline]
1929            fn __chaining_lt(&self, other: &Self) -> ControlFlow<bool> {
1930                let (lhs, rhs) = (*self, *other);
1931                if lhs == rhs { Continue(()) } else { Break(lhs < rhs) }
1932            }
1933            #[inline]
1934            fn __chaining_le(&self, other: &Self) -> ControlFlow<bool> {
1935                let (lhs, rhs) = (*self, *other);
1936                if lhs == rhs { Continue(()) } else { Break(lhs <= rhs) }
1937            }
1938            #[inline]
1939            fn __chaining_gt(&self, other: &Self) -> ControlFlow<bool> {
1940                let (lhs, rhs) = (*self, *other);
1941                if lhs == rhs { Continue(()) } else { Break(lhs > rhs) }
1942            }
1943            #[inline]
1944            fn __chaining_ge(&self, other: &Self) -> ControlFlow<bool> {
1945                let (lhs, rhs) = (*self, *other);
1946                if lhs == rhs { Continue(()) } else { Break(lhs >= rhs) }
1947            }
1948        };
1949    }
1950
1951    macro_rules! partial_ord_impl {
1952        ($($t:ty)*) => ($(
1953            #[stable(feature = "rust1", since = "1.0.0")]
1954            #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1955            impl const PartialOrd for $t {
1956                #[inline]
1957                fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
1958                    match (*self <= *other, *self >= *other) {
1959                        (false, false) => None,
1960                        (false, true) => Some(Greater),
1961                        (true, false) => Some(Less),
1962                        (true, true) => Some(Equal),
1963                    }
1964                }
1965
1966                partial_ord_methods_primitive_impl!();
1967            }
1968        )*)
1969    }
1970
1971    #[stable(feature = "rust1", since = "1.0.0")]
1972    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1973    impl const PartialOrd for () {
1974        #[inline]
1975        fn partial_cmp(&self, _: &()) -> Option<Ordering> {
1976            Some(Equal)
1977        }
1978    }
1979
1980    #[stable(feature = "rust1", since = "1.0.0")]
1981    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1982    impl const PartialOrd for bool {
1983        #[inline]
1984        fn partial_cmp(&self, other: &bool) -> Option<Ordering> {
1985            Some(self.cmp(other))
1986        }
1987
1988        partial_ord_methods_primitive_impl!();
1989    }
1990
1991    partial_ord_impl! { f16 f32 f64 f128 }
1992
1993    macro_rules! ord_impl {
1994        ($($t:ty)*) => ($(
1995            #[stable(feature = "rust1", since = "1.0.0")]
1996            #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
1997            impl const PartialOrd for $t {
1998                #[inline]
1999                fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
2000                    Some(crate::intrinsics::three_way_compare(*self, *other))
2001                }
2002
2003                partial_ord_methods_primitive_impl!();
2004            }
2005
2006            #[stable(feature = "rust1", since = "1.0.0")]
2007            #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2008            impl const Ord for $t {
2009                #[inline]
2010                fn cmp(&self, other: &Self) -> Ordering {
2011                    crate::intrinsics::three_way_compare(*self, *other)
2012                }
2013
2014                #[inline]
2015                #[track_caller]
2016                fn clamp(self, min: Self, max: Self) -> Self
2017                {
2018                    const_assert!(
2019                        min <= max,
2020                        "min > max",
2021                        "min > max. min = {min:?}, max = {max:?}",
2022                        min: $t,
2023                        max: $t,
2024                    );
2025                    if self < min {
2026                        min
2027                    } else if self > max {
2028                        max
2029                    } else {
2030                        self
2031                    }
2032                }
2033            }
2034        )*)
2035    }
2036
2037    #[stable(feature = "rust1", since = "1.0.0")]
2038    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2039    impl const Ord for () {
2040        #[inline]
2041        fn cmp(&self, _other: &()) -> Ordering {
2042            Equal
2043        }
2044    }
2045
2046    #[stable(feature = "rust1", since = "1.0.0")]
2047    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2048    impl const Ord for bool {
2049        #[inline]
2050        fn cmp(&self, other: &bool) -> Ordering {
2051            // Casting to i8's and converting the difference to an Ordering generates
2052            // more optimal assembly.
2053            // See <https://github.com/rust-lang/rust/issues/66780> for more info.
2054            match (*self as i8) - (*other as i8) {
2055                -1 => Less,
2056                0 => Equal,
2057                1 => Greater,
2058                // SAFETY: bool as i8 returns 0 or 1, so the difference can't be anything else
2059                _ => unsafe { unreachable_unchecked() },
2060            }
2061        }
2062
2063        #[inline]
2064        fn min(self, other: bool) -> bool {
2065            self & other
2066        }
2067
2068        #[inline]
2069        fn max(self, other: bool) -> bool {
2070            self | other
2071        }
2072
2073        #[inline]
2074        fn clamp(self, min: bool, max: bool) -> bool {
2075            assert!(min <= max);
2076            self.max(min).min(max)
2077        }
2078    }
2079
2080    ord_impl! { char usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
2081
2082    #[unstable(feature = "never_type", issue = "35121")]
2083    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2084    impl const PartialEq for ! {
2085        #[inline]
2086        fn eq(&self, _: &!) -> bool {
2087            *self
2088        }
2089    }
2090
2091    #[unstable(feature = "never_type", issue = "35121")]
2092    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2093    impl const Eq for ! {}
2094
2095    #[unstable(feature = "never_type", issue = "35121")]
2096    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2097    impl const PartialOrd for ! {
2098        #[inline]
2099        fn partial_cmp(&self, _: &!) -> Option<Ordering> {
2100            *self
2101        }
2102    }
2103
2104    #[unstable(feature = "never_type", issue = "35121")]
2105    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2106    impl const Ord for ! {
2107        #[inline]
2108        fn cmp(&self, _: &!) -> Ordering {
2109            *self
2110        }
2111    }
2112
2113    // & pointers
2114
2115    #[stable(feature = "rust1", since = "1.0.0")]
2116    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2117    impl<A: PointeeSized, B: PointeeSized> const PartialEq<&B> for &A
2118    where
2119        A: [const] PartialEq<B>,
2120    {
2121        #[inline]
2122        fn eq(&self, other: &&B) -> bool {
2123            PartialEq::eq(*self, *other)
2124        }
2125        #[inline]
2126        fn ne(&self, other: &&B) -> bool {
2127            PartialEq::ne(*self, *other)
2128        }
2129    }
2130    #[stable(feature = "rust1", since = "1.0.0")]
2131    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2132    impl<A: PointeeSized, B: PointeeSized> const PartialOrd<&B> for &A
2133    where
2134        A: [const] PartialOrd<B>,
2135    {
2136        #[inline]
2137        fn partial_cmp(&self, other: &&B) -> Option<Ordering> {
2138            PartialOrd::partial_cmp(*self, *other)
2139        }
2140        #[inline]
2141        fn lt(&self, other: &&B) -> bool {
2142            PartialOrd::lt(*self, *other)
2143        }
2144        #[inline]
2145        fn le(&self, other: &&B) -> bool {
2146            PartialOrd::le(*self, *other)
2147        }
2148        #[inline]
2149        fn gt(&self, other: &&B) -> bool {
2150            PartialOrd::gt(*self, *other)
2151        }
2152        #[inline]
2153        fn ge(&self, other: &&B) -> bool {
2154            PartialOrd::ge(*self, *other)
2155        }
2156        #[inline]
2157        fn __chaining_lt(&self, other: &&B) -> ControlFlow<bool> {
2158            PartialOrd::__chaining_lt(*self, *other)
2159        }
2160        #[inline]
2161        fn __chaining_le(&self, other: &&B) -> ControlFlow<bool> {
2162            PartialOrd::__chaining_le(*self, *other)
2163        }
2164        #[inline]
2165        fn __chaining_gt(&self, other: &&B) -> ControlFlow<bool> {
2166            PartialOrd::__chaining_gt(*self, *other)
2167        }
2168        #[inline]
2169        fn __chaining_ge(&self, other: &&B) -> ControlFlow<bool> {
2170            PartialOrd::__chaining_ge(*self, *other)
2171        }
2172    }
2173    #[stable(feature = "rust1", since = "1.0.0")]
2174    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2175    impl<A: PointeeSized> const Ord for &A
2176    where
2177        A: [const] Ord,
2178    {
2179        #[inline]
2180        fn cmp(&self, other: &Self) -> Ordering {
2181            Ord::cmp(*self, *other)
2182        }
2183    }
2184    #[stable(feature = "rust1", since = "1.0.0")]
2185    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2186    impl<A: PointeeSized> const Eq for &A where A: [const] Eq {}
2187
2188    // &mut pointers
2189
2190    #[stable(feature = "rust1", since = "1.0.0")]
2191    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2192    impl<A: PointeeSized, B: PointeeSized> const PartialEq<&mut B> for &mut A
2193    where
2194        A: [const] PartialEq<B>,
2195    {
2196        #[inline]
2197        fn eq(&self, other: &&mut B) -> bool {
2198            PartialEq::eq(*self, *other)
2199        }
2200        #[inline]
2201        fn ne(&self, other: &&mut B) -> bool {
2202            PartialEq::ne(*self, *other)
2203        }
2204    }
2205    #[stable(feature = "rust1", since = "1.0.0")]
2206    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2207    impl<A: PointeeSized, B: PointeeSized> const PartialOrd<&mut B> for &mut A
2208    where
2209        A: [const] PartialOrd<B>,
2210    {
2211        #[inline]
2212        fn partial_cmp(&self, other: &&mut B) -> Option<Ordering> {
2213            PartialOrd::partial_cmp(*self, *other)
2214        }
2215        #[inline]
2216        fn lt(&self, other: &&mut B) -> bool {
2217            PartialOrd::lt(*self, *other)
2218        }
2219        #[inline]
2220        fn le(&self, other: &&mut B) -> bool {
2221            PartialOrd::le(*self, *other)
2222        }
2223        #[inline]
2224        fn gt(&self, other: &&mut B) -> bool {
2225            PartialOrd::gt(*self, *other)
2226        }
2227        #[inline]
2228        fn ge(&self, other: &&mut B) -> bool {
2229            PartialOrd::ge(*self, *other)
2230        }
2231        #[inline]
2232        fn __chaining_lt(&self, other: &&mut B) -> ControlFlow<bool> {
2233            PartialOrd::__chaining_lt(*self, *other)
2234        }
2235        #[inline]
2236        fn __chaining_le(&self, other: &&mut B) -> ControlFlow<bool> {
2237            PartialOrd::__chaining_le(*self, *other)
2238        }
2239        #[inline]
2240        fn __chaining_gt(&self, other: &&mut B) -> ControlFlow<bool> {
2241            PartialOrd::__chaining_gt(*self, *other)
2242        }
2243        #[inline]
2244        fn __chaining_ge(&self, other: &&mut B) -> ControlFlow<bool> {
2245            PartialOrd::__chaining_ge(*self, *other)
2246        }
2247    }
2248    #[stable(feature = "rust1", since = "1.0.0")]
2249    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2250    impl<A: PointeeSized> const Ord for &mut A
2251    where
2252        A: [const] Ord,
2253    {
2254        #[inline]
2255        fn cmp(&self, other: &Self) -> Ordering {
2256            Ord::cmp(*self, *other)
2257        }
2258    }
2259    #[stable(feature = "rust1", since = "1.0.0")]
2260    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2261    impl<A: PointeeSized> const Eq for &mut A where A: [const] Eq {}
2262
2263    #[stable(feature = "rust1", since = "1.0.0")]
2264    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2265    impl<A: PointeeSized, B: PointeeSized> const PartialEq<&mut B> for &A
2266    where
2267        A: [const] PartialEq<B>,
2268    {
2269        #[inline]
2270        fn eq(&self, other: &&mut B) -> bool {
2271            PartialEq::eq(*self, *other)
2272        }
2273        #[inline]
2274        fn ne(&self, other: &&mut B) -> bool {
2275            PartialEq::ne(*self, *other)
2276        }
2277    }
2278
2279    #[stable(feature = "rust1", since = "1.0.0")]
2280    #[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2281    impl<A: PointeeSized, B: PointeeSized> const PartialEq<&B> for &mut A
2282    where
2283        A: [const] PartialEq<B>,
2284    {
2285        #[inline]
2286        fn eq(&self, other: &&B) -> bool {
2287            PartialEq::eq(*self, *other)
2288        }
2289        #[inline]
2290        fn ne(&self, other: &&B) -> bool {
2291            PartialEq::ne(*self, *other)
2292        }
2293    }
2294}
````