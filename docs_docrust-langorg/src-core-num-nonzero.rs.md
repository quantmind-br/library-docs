---
title: nonzero.rs - source
url: https://doc.rust-lang.org/src/core/num/nonzero.rs.html#353-355
source: crawler
fetched_at: 2026-05-06T21:30:40.558732802-03:00
rendered_js: false
word_count: 9667
summary: This document defines the NonZero struct, which enforces a non-zero constraint on primitive types to enable memory layout optimizations like the null pointer optimization.
tags:
    - rust
    - memory-optimization
    - data-types
    - nonzero
    - type-safety
category: concept
---

## core/num/ nonzero.rs

````rust
1//! Definitions of integer that is known not to equal zero.
2
3use super::{IntErrorKind, ParseIntError};
4use crate::clone::{TrivialClone, UseCloned};
5use crate::cmp::Ordering;
6use crate::hash::{Hash, Hasher};
7use crate::marker::{Destruct, Freeze, StructuralPartialEq};
8use crate::ops::{BitOr, BitOrAssign, Div, DivAssign, Neg, Rem, RemAssign};
9use crate::panic::{RefUnwindSafe, UnwindSafe};
10use crate::str::FromStr;
11use crate::{fmt, intrinsics, ptr, ub_checks};
12
13/// A marker trait for primitive types which can be zero.
14///
15/// This is an implementation detail for <code>[NonZero]\<T></code> which may disappear or be replaced at any time.
16///
17/// # Safety
18///
19/// Types implementing this trait must be primitives that are valid when zeroed.
20///
21/// The associated `Self::NonZeroInner` type must have the same size+align as `Self`,
22/// but with a niche and bit validity making it so the following `transmutes` are sound:
23///
24/// - `Self::NonZeroInner` to `Option<Self::NonZeroInner>`
25/// - `Option<Self::NonZeroInner>` to `Self`
26///
27/// (And, consequently, `Self::NonZeroInner` to `Self`.)
28#[unstable(
29    feature = "nonzero_internals",
30    reason = "implementation detail which may disappear or be replaced at any time",
31    issue = "none"
32)]
33pub unsafe trait ZeroablePrimitive: Sized + Copy + private::Sealed {
34    /// A type like `Self` but with a niche that includes zero.
35    type NonZeroInner: Sized + Copy;
36}
37
38macro_rules! impl_zeroable_primitive {
39    ($($NonZeroInner:ident ( $primitive:ty )),+ $(,)?) => {
40        mod private {
41            #[unstable(
42                feature = "nonzero_internals",
43                reason = "implementation detail which may disappear or be replaced at any time",
44                issue = "none"
45            )]
46            pub trait Sealed {}
47        }
48
49        $(
50            #[unstable(
51                feature = "nonzero_internals",
52                reason = "implementation detail which may disappear or be replaced at any time",
53                issue = "none"
54            )]
55            impl private::Sealed for $primitive {}
56
57            #[unstable(
58                feature = "nonzero_internals",
59                reason = "implementation detail which may disappear or be replaced at any time",
60                issue = "none"
61            )]
62            unsafe impl ZeroablePrimitive for $primitive {
63                type NonZeroInner = super::niche_types::$NonZeroInner;
64            }
65        )+
66    };
67}
68
69impl_zeroable_primitive!(
70    NonZeroU8Inner(u8),
71    NonZeroU16Inner(u16),
72    NonZeroU32Inner(u32),
73    NonZeroU64Inner(u64),
74    NonZeroU128Inner(u128),
75    NonZeroUsizeInner(usize),
76    NonZeroI8Inner(i8),
77    NonZeroI16Inner(i16),
78    NonZeroI32Inner(i32),
79    NonZeroI64Inner(i64),
80    NonZeroI128Inner(i128),
81    NonZeroIsizeInner(isize),
82    NonZeroCharInner(char),
83);
84
85/// A value that is known not to equal zero.
86///
87/// This enables some memory layout optimization.
88/// For example, `Option<NonZero<u32>>` is the same size as `u32`:
89///
90/// ```
91/// use core::{num::NonZero};
92///
93/// assert_eq!(size_of::<Option<NonZero<u32>>>(), size_of::<u32>());
94/// ```
95///
96/// # Layout
97///
98/// `NonZero<T>` is guaranteed to have the same layout and bit validity as `T`
99/// with the exception that the all-zero bit pattern is invalid.
100/// `Option<NonZero<T>>` is guaranteed to be compatible with `T`, including in
101/// FFI.
102///
103/// Thanks to the [null pointer optimization], `NonZero<T>` and
104/// `Option<NonZero<T>>` are guaranteed to have the same size and alignment:
105///
106/// ```
107/// use std::num::NonZero;
108///
109/// assert_eq!(size_of::<NonZero<u32>>(), size_of::<Option<NonZero<u32>>>());
110/// assert_eq!(align_of::<NonZero<u32>>(), align_of::<Option<NonZero<u32>>>());
111/// ```
112///
113/// [null pointer optimization]: crate::option#representation
114///
115/// # Note on generic usage
116///
117/// `NonZero<T>` can only be used with some standard library primitive types
118/// (such as `u8`, `i32`, and etc.). The type parameter `T` must implement the
119/// internal trait [`ZeroablePrimitive`], which is currently permanently unstable
120/// and cannot be implemented by users. Therefore, you cannot use `NonZero<T>`
121/// with your own types, nor can you implement traits for all `NonZero<T>`,
122/// only for concrete types.
123#[stable(feature = "generic_nonzero", since = "1.79.0")]
124#[repr(transparent)]
125#[rustc_nonnull_optimization_guaranteed]
126#[rustc_diagnostic_item = "NonZero"]
127pub struct NonZero<T: ZeroablePrimitive>(T::NonZeroInner);
128
129macro_rules! impl_nonzero_fmt {
130    ($(#[$Attribute:meta] $Trait:ident)*) => {
131        $(
132            #[$Attribute]
133            impl<T> fmt::$Trait for NonZero<T>
134            where
135                T: ZeroablePrimitive + fmt::$Trait,
136            {
137                #[inline]
138                fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
139                    self.get().fmt(f)
140                }
141            }
142        )*
143    };
144}
145
146impl_nonzero_fmt! {
147    #[stable(feature = "nonzero", since = "1.28.0")]
148    Debug
149    #[stable(feature = "nonzero", since = "1.28.0")]
150    Display
151    #[stable(feature = "nonzero", since = "1.28.0")]
152    Binary
153    #[stable(feature = "nonzero", since = "1.28.0")]
154    Octal
155    #[stable(feature = "nonzero", since = "1.28.0")]
156    LowerHex
157    #[stable(feature = "nonzero", since = "1.28.0")]
158    UpperHex
159    #[stable(feature = "nonzero_fmt_exp", since = "1.84.0")]
160    LowerExp
161    #[stable(feature = "nonzero_fmt_exp", since = "1.84.0")]
162    UpperExp
163}
164
165macro_rules! impl_nonzero_auto_trait {
166    (unsafe $Trait:ident) => {
167        #[stable(feature = "nonzero", since = "1.28.0")]
168        unsafe impl<T> $Trait for NonZero<T> where T: ZeroablePrimitive + $Trait {}
169    };
170    ($Trait:ident) => {
171        #[stable(feature = "nonzero", since = "1.28.0")]
172        impl<T> $Trait for NonZero<T> where T: ZeroablePrimitive + $Trait {}
173    };
174}
175
176// Implement auto-traits manually based on `T` to avoid docs exposing
177// the `ZeroablePrimitive::NonZeroInner` implementation detail.
178impl_nonzero_auto_trait!(unsafe Freeze);
179impl_nonzero_auto_trait!(RefUnwindSafe);
180impl_nonzero_auto_trait!(unsafe Send);
181impl_nonzero_auto_trait!(unsafe Sync);
182impl_nonzero_auto_trait!(Unpin);
183impl_nonzero_auto_trait!(UnwindSafe);
184
185#[stable(feature = "nonzero", since = "1.28.0")]
186impl<T> Clone for NonZero<T>
187where
188    T: ZeroablePrimitive,
189{
190    #[inline]
191    fn clone(&self) -> Self {
192        *self
193    }
194}
195
196#[unstable(feature = "ergonomic_clones", issue = "132290")]
197impl<T> UseCloned for NonZero<T> where T: ZeroablePrimitive {}
198
199#[stable(feature = "nonzero", since = "1.28.0")]
200impl<T> Copy for NonZero<T> where T: ZeroablePrimitive {}
201
202#[doc(hidden)]
203#[unstable(feature = "trivial_clone", issue = "none")]
204unsafe impl<T> TrivialClone for NonZero<T> where T: ZeroablePrimitive {}
205
206#[stable(feature = "nonzero", since = "1.28.0")]
207#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
208impl<T> const PartialEq for NonZero<T>
209where
210    T: ZeroablePrimitive + [const] PartialEq,
211{
212    #[inline]
213    fn eq(&self, other: &Self) -> bool {
214        self.get() == other.get()
215    }
216
217    #[inline]
218    fn ne(&self, other: &Self) -> bool {
219        self.get() != other.get()
220    }
221}
222
223#[unstable(feature = "structural_match", issue = "31434")]
224impl<T> StructuralPartialEq for NonZero<T> where T: ZeroablePrimitive + StructuralPartialEq {}
225
226#[stable(feature = "nonzero", since = "1.28.0")]
227#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
228impl<T> const Eq for NonZero<T> where T: ZeroablePrimitive + [const] Eq {}
229
230#[stable(feature = "nonzero", since = "1.28.0")]
231#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
232impl<T> const PartialOrd for NonZero<T>
233where
234    T: ZeroablePrimitive + [const] PartialOrd,
235{
236    #[inline]
237    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
238        self.get().partial_cmp(&other.get())
239    }
240
241    #[inline]
242    fn lt(&self, other: &Self) -> bool {
243        self.get() < other.get()
244    }
245
246    #[inline]
247    fn le(&self, other: &Self) -> bool {
248        self.get() <= other.get()
249    }
250
251    #[inline]
252    fn gt(&self, other: &Self) -> bool {
253        self.get() > other.get()
254    }
255
256    #[inline]
257    fn ge(&self, other: &Self) -> bool {
258        self.get() >= other.get()
259    }
260}
261
262#[stable(feature = "nonzero", since = "1.28.0")]
263#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
264impl<T> const Ord for NonZero<T>
265where
266    // FIXME(const_hack): the T: ~const Destruct should be inferred from the Self: ~const Destruct.
267    // See https://github.com/rust-lang/rust/issues/144207
268    T: ZeroablePrimitive + [const] Ord + [const] Destruct,
269{
270    #[inline]
271    fn cmp(&self, other: &Self) -> Ordering {
272        self.get().cmp(&other.get())
273    }
274
275    #[inline]
276    fn max(self, other: Self) -> Self {
277        // SAFETY: The maximum of two non-zero values is still non-zero.
278        unsafe { Self::new_unchecked(self.get().max(other.get())) }
279    }
280
281    #[inline]
282    fn min(self, other: Self) -> Self {
283        // SAFETY: The minimum of two non-zero values is still non-zero.
284        unsafe { Self::new_unchecked(self.get().min(other.get())) }
285    }
286
287    #[inline]
288    fn clamp(self, min: Self, max: Self) -> Self {
289        // SAFETY: A non-zero value clamped between two non-zero values is still non-zero.
290        unsafe { Self::new_unchecked(self.get().clamp(min.get(), max.get())) }
291    }
292}
293
294#[stable(feature = "nonzero", since = "1.28.0")]
295impl<T> Hash for NonZero<T>
296where
297    T: ZeroablePrimitive + Hash,
298{
299    #[inline]
300    fn hash<H>(&self, state: &mut H)
301    where
302        H: Hasher,
303    {
304        self.get().hash(state)
305    }
306}
307
308#[stable(feature = "from_nonzero", since = "1.31.0")]
309#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
310impl<T> const From<NonZero<T>> for T
311where
312    T: ZeroablePrimitive,
313{
314    #[inline]
315    fn from(nonzero: NonZero<T>) -> Self {
316        // Call `get` method to keep range information.
317        nonzero.get()
318    }
319}
320
321#[stable(feature = "nonzero_bitor", since = "1.45.0")]
322#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
323impl<T> const BitOr for NonZero<T>
324where
325    T: ZeroablePrimitive + [const] BitOr<Output = T>,
326{
327    type Output = Self;
328
329    #[inline]
330    fn bitor(self, rhs: Self) -> Self::Output {
331        // SAFETY: Bitwise OR of two non-zero values is still non-zero.
332        unsafe { Self::new_unchecked(self.get() | rhs.get()) }
333    }
334}
335
336#[stable(feature = "nonzero_bitor", since = "1.45.0")]
337#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
338impl<T> const BitOr<T> for NonZero<T>
339where
340    T: ZeroablePrimitive + [const] BitOr<Output = T>,
341{
342    type Output = Self;
343
344    #[inline]
345    fn bitor(self, rhs: T) -> Self::Output {
346        // SAFETY: Bitwise OR of a non-zero value with anything is still non-zero.
347        unsafe { Self::new_unchecked(self.get() | rhs) }
348    }
349}
350
351#[stable(feature = "nonzero_bitor", since = "1.45.0")]
352#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
353impl<T> const BitOr<NonZero<T>> for T
354where
355    T: ZeroablePrimitive + [const] BitOr<Output = T>,
356{
357    type Output = NonZero<T>;
358
359    #[inline]
360    fn bitor(self, rhs: NonZero<T>) -> Self::Output {
361        // SAFETY: Bitwise OR of anything with a non-zero value is still non-zero.
362        unsafe { NonZero::new_unchecked(self | rhs.get()) }
363    }
364}
365
366#[stable(feature = "nonzero_bitor", since = "1.45.0")]
367#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
368impl<T> const BitOrAssign for NonZero<T>
369where
370    T: ZeroablePrimitive,
371    Self: [const] BitOr<Output = Self>,
372{
373    #[inline]
374    fn bitor_assign(&mut self, rhs: Self) {
375        *self = *self | rhs;
376    }
377}
378
379#[stable(feature = "nonzero_bitor", since = "1.45.0")]
380#[rustc_const_unstable(feature = "const_ops", issue = "143802")]
381impl<T> const BitOrAssign<T> for NonZero<T>
382where
383    T: ZeroablePrimitive,
384    Self: [const] BitOr<T, Output = Self>,
385{
386    #[inline]
387    fn bitor_assign(&mut self, rhs: T) {
388        *self = *self | rhs;
389    }
390}
391
392impl<T> NonZero<T>
393where
394    T: ZeroablePrimitive,
395{
396    /// Creates a non-zero if the given value is not zero.
397    #[stable(feature = "nonzero", since = "1.28.0")]
398    #[rustc_const_stable(feature = "const_nonzero_int_methods", since = "1.47.0")]
399    #[must_use]
400    #[inline]
401    pub const fn new(n: T) -> Option<Self> {
402        // SAFETY: Memory layout optimization guarantees that `Option<NonZero<T>>` has
403        //         the same layout and size as `T`, with `0` representing `None`.
404        unsafe { intrinsics::transmute_unchecked(n) }
405    }
406
407    /// Creates a non-zero without checking whether the value is non-zero.
408    /// This results in undefined behavior if the value is zero.
409    ///
410    /// # Safety
411    ///
412    /// The value must not be zero.
413    #[stable(feature = "nonzero", since = "1.28.0")]
414    #[rustc_const_stable(feature = "nonzero", since = "1.28.0")]
415    #[must_use]
416    #[inline]
417    #[track_caller]
418    pub const unsafe fn new_unchecked(n: T) -> Self {
419        match Self::new(n) {
420            Some(n) => n,
421            None => {
422                // SAFETY: The caller guarantees that `n` is non-zero, so this is unreachable.
423                unsafe {
424                    ub_checks::assert_unsafe_precondition!(
425                        check_language_ub,
426                        "NonZero::new_unchecked requires the argument to be non-zero",
427                        () => false,
428                    );
429                    intrinsics::unreachable()
430                }
431            }
432        }
433    }
434
435    /// Converts a reference to a non-zero mutable reference
436    /// if the referenced value is not zero.
437    #[unstable(feature = "nonzero_from_mut", issue = "106290")]
438    #[must_use]
439    #[inline]
440    pub fn from_mut(n: &mut T) -> Option<&mut Self> {
441        // SAFETY: Memory layout optimization guarantees that `Option<NonZero<T>>` has
442        //         the same layout and size as `T`, with `0` representing `None`.
443        let opt_n = unsafe { &mut *(ptr::from_mut(n).cast::<Option<Self>>()) };
444
445        opt_n.as_mut()
446    }
447
448    /// Converts a mutable reference to a non-zero mutable reference
449    /// without checking whether the referenced value is non-zero.
450    /// This results in undefined behavior if the referenced value is zero.
451    ///
452    /// # Safety
453    ///
454    /// The referenced value must not be zero.
455    #[unstable(feature = "nonzero_from_mut", issue = "106290")]
456    #[must_use]
457    #[inline]
458    #[track_caller]
459    pub unsafe fn from_mut_unchecked(n: &mut T) -> &mut Self {
460        match Self::from_mut(n) {
461            Some(n) => n,
462            None => {
463                // SAFETY: The caller guarantees that `n` references a value that is non-zero, so this is unreachable.
464                unsafe {
465                    ub_checks::assert_unsafe_precondition!(
466                        check_library_ub,
467                        "NonZero::from_mut_unchecked requires the argument to dereference as non-zero",
468                        () => false,
469                    );
470                    intrinsics::unreachable()
471                }
472            }
473        }
474    }
475
476    /// Returns the contained value as a primitive type.
477    #[stable(feature = "nonzero", since = "1.28.0")]
478    #[rustc_const_stable(feature = "const_nonzero_get", since = "1.34.0")]
479    #[inline]
480    pub const fn get(self) -> T {
481        // Rustc can set range metadata only if it loads `self` from
482        // memory somewhere. If the value of `self` was from by-value argument
483        // of some not-inlined function, LLVM don't have range metadata
484        // to understand that the value cannot be zero.
485        //
486        // Using the transmute `assume`s the range at runtime.
487        //
488        // Even once LLVM supports `!range` metadata for function arguments
489        // (see <https://github.com/llvm/llvm-project/issues/76628>), this can't
490        // be `.0` because MCP#807 bans field-projecting into `scalar_valid_range`
491        // types, and it arguably wouldn't want to be anyway because if this is
492        // MIR-inlined, there's no opportunity to put that argument metadata anywhere.
493        //
494        // The good answer here will eventually be pattern types, which will hopefully
495        // allow it to go back to `.0`, maybe with a cast of some sort.
496        //
497        // SAFETY: `ZeroablePrimitive` guarantees that the size and bit validity
498        // of `.0` is such that this transmute is sound.
499        unsafe { intrinsics::transmute_unchecked(self) }
500    }
501}
502
503macro_rules! nonzero_integer {
504    (
505        #[$stability:meta]
506        Self = $Ty:ident,
507        Primitive = $signedness:ident $Int:ident,
508        SignedPrimitive = $Sint:ty,
509        UnsignedPrimitive = $Uint:ty,
510
511        // Used in doc comments.
512        rot = $rot:literal,
513        rot_op = $rot_op:literal,
514        rot_result = $rot_result:literal,
515        swap_op = $swap_op:literal,
516        swapped = $swapped:literal,
517        reversed = $reversed:literal,
518        leading_zeros_test = $leading_zeros_test:expr,
519    ) => {
520        #[doc = sign_dependent_expr!{
521            $signedness ?
522            if signed {
523                concat!("An [`", stringify!($Int), "`] that is known not to equal zero.")
524            }
525            if unsigned {
526                concat!("A [`", stringify!($Int), "`] that is known not to equal zero.")
527            }
528        }]
529        ///
530        /// This enables some memory layout optimization.
531        #[doc = concat!("For example, `Option<", stringify!($Ty), ">` is the same size as `", stringify!($Int), "`:")]
532        ///
533        /// ```rust
534        #[doc = concat!("assert_eq!(size_of::<Option<core::num::", stringify!($Ty), ">>(), size_of::<", stringify!($Int), ">());")]
535        /// ```
536        ///
537        /// # Layout
538        ///
539        #[doc = concat!("`", stringify!($Ty), "` is guaranteed to have the same layout and bit validity as `", stringify!($Int), "`")]
540        /// with the exception that `0` is not a valid instance.
541        #[doc = concat!("`Option<", stringify!($Ty), ">` is guaranteed to be compatible with `", stringify!($Int), "`,")]
542        /// including in FFI.
543        ///
544        /// Thanks to the [null pointer optimization],
545        #[doc = concat!("`", stringify!($Ty), "` and `Option<", stringify!($Ty), ">`")]
546        /// are guaranteed to have the same size and alignment:
547        ///
548        /// ```
549        #[doc = concat!("use std::num::", stringify!($Ty), ";")]
550        ///
551        #[doc = concat!("assert_eq!(size_of::<", stringify!($Ty), ">(), size_of::<Option<", stringify!($Ty), ">>());")]
552        #[doc = concat!("assert_eq!(align_of::<", stringify!($Ty), ">(), align_of::<Option<", stringify!($Ty), ">>());")]
553        /// ```
554        ///
555        /// # Compile-time creation
556        ///
557        /// Since both [`Option::unwrap()`] and [`Option::expect()`] are `const`, it is possible to
558        /// define a new
559        #[doc = concat!("`", stringify!($Ty), "`")]
560        /// at compile time via:
561        /// ```
562        #[doc = concat!("use std::num::", stringify!($Ty), ";")]
563        ///
564        #[doc = concat!("const TEN: ", stringify!($Ty), " = ", stringify!($Ty) , r#"::new(10).expect("ten is non-zero");"#)]
565        /// ```
566        ///
567        /// [null pointer optimization]: crate::option#representation
568        #[$stability]
569        pub type $Ty = NonZero<$Int>;
570
571        impl NonZero<$Int> {
572            /// The size of this non-zero integer type in bits.
573            ///
574            #[doc = concat!("This value is equal to [`", stringify!($Int), "::BITS`].")]
575            ///
576            /// # Examples
577            ///
578            /// ```
579            /// # use std::num::NonZero;
580            /// #
581            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::BITS, ", stringify!($Int), "::BITS);")]
582            /// ```
583            #[stable(feature = "nonzero_bits", since = "1.67.0")]
584            pub const BITS: u32 = <$Int>::BITS;
585
586            /// Returns the number of leading zeros in the binary representation of `self`.
587            ///
588            /// On many architectures, this function can perform better than `leading_zeros()` on the underlying integer type, as special handling of zero can be avoided.
589            ///
590            /// # Examples
591            ///
592            /// ```
593            /// # use std::num::NonZero;
594            /// #
595            /// # fn main() { test().unwrap(); }
596            /// # fn test() -> Option<()> {
597            #[doc = concat!("let n = NonZero::<", stringify!($Int), ">::new(", $leading_zeros_test, ")?;")]
598            ///
599            /// assert_eq!(n.leading_zeros(), 0);
600            /// # Some(())
601            /// # }
602            /// ```
603            #[stable(feature = "nonzero_leading_trailing_zeros", since = "1.53.0")]
604            #[rustc_const_stable(feature = "nonzero_leading_trailing_zeros", since = "1.53.0")]
605            #[must_use = "this returns the result of the operation, \
606                          without modifying the original"]
607            #[inline]
608            pub const fn leading_zeros(self) -> u32 {
609                // SAFETY: since `self` cannot be zero, it is safe to call `ctlz_nonzero`.
610                unsafe {
611                    intrinsics::ctlz_nonzero(self.get() as $Uint)
612                }
613            }
614
615            /// Returns the number of trailing zeros in the binary representation
616            /// of `self`.
617            ///
618            /// On many architectures, this function can perform better than `trailing_zeros()` on the underlying integer type, as special handling of zero can be avoided.
619            ///
620            /// # Examples
621            ///
622            /// ```
623            /// # use std::num::NonZero;
624            /// #
625            /// # fn main() { test().unwrap(); }
626            /// # fn test() -> Option<()> {
627            #[doc = concat!("let n = NonZero::<", stringify!($Int), ">::new(0b0101000)?;")]
628            ///
629            /// assert_eq!(n.trailing_zeros(), 3);
630            /// # Some(())
631            /// # }
632            /// ```
633            #[stable(feature = "nonzero_leading_trailing_zeros", since = "1.53.0")]
634            #[rustc_const_stable(feature = "nonzero_leading_trailing_zeros", since = "1.53.0")]
635            #[must_use = "this returns the result of the operation, \
636                          without modifying the original"]
637            #[inline]
638            pub const fn trailing_zeros(self) -> u32 {
639                // SAFETY: since `self` cannot be zero, it is safe to call `cttz_nonzero`.
640                unsafe {
641                    intrinsics::cttz_nonzero(self.get() as $Uint)
642                }
643            }
644
645            /// Returns `self` with only the most significant bit set.
646            ///
647            /// # Example
648            ///
649            /// ```
650            /// #![feature(isolate_most_least_significant_one)]
651            ///
652            /// # use core::num::NonZero;
653            /// # fn main() { test().unwrap(); }
654            /// # fn test() -> Option<()> {
655            #[doc = concat!("let a = NonZero::<", stringify!($Int), ">::new(0b_01100100)?;")]
656            #[doc = concat!("let b = NonZero::<", stringify!($Int), ">::new(0b_01000000)?;")]
657            ///
658            /// assert_eq!(a.isolate_highest_one(), b);
659            /// # Some(())
660            /// # }
661            /// ```
662            #[unstable(feature = "isolate_most_least_significant_one", issue = "136909")]
663            #[must_use = "this returns the result of the operation, \
664                        without modifying the original"]
665            #[inline(always)]
666            pub const fn isolate_highest_one(self) -> Self {
667                // SAFETY:
668                // `self` is non-zero, so masking to preserve only the most
669                // significant set bit will result in a non-zero `n`.
670                // and self.leading_zeros() is always < $INT::BITS since
671                // at least one of the bits in the number is not zero
672                unsafe {
673                    let bit = (((1 as $Uint) << (<$Uint>::BITS - 1)).unchecked_shr(self.leading_zeros()));
674                    NonZero::new_unchecked(bit as $Int)
675                }
676            }
677
678            /// Returns `self` with only the least significant bit set.
679            ///
680            /// # Example
681            ///
682            /// ```
683            /// #![feature(isolate_most_least_significant_one)]
684            ///
685            /// # use core::num::NonZero;
686            /// # fn main() { test().unwrap(); }
687            /// # fn test() -> Option<()> {
688            #[doc = concat!("let a = NonZero::<", stringify!($Int), ">::new(0b_01100100)?;")]
689            #[doc = concat!("let b = NonZero::<", stringify!($Int), ">::new(0b_00000100)?;")]
690            ///
691            /// assert_eq!(a.isolate_lowest_one(), b);
692            /// # Some(())
693            /// # }
694            /// ```
695            #[unstable(feature = "isolate_most_least_significant_one", issue = "136909")]
696            #[must_use = "this returns the result of the operation, \
697                        without modifying the original"]
698            #[inline(always)]
699            pub const fn isolate_lowest_one(self) -> Self {
700                let n = self.get();
701                let n = n & n.wrapping_neg();
702
703                // SAFETY: `self` is non-zero, so `self` with only its least
704                // significant set bit will remain non-zero.
705                unsafe { NonZero::new_unchecked(n) }
706            }
707
708            /// Returns the index of the highest bit set to one in `self`.
709            ///
710            /// # Examples
711            ///
712            /// ```
713            /// #![feature(int_lowest_highest_one)]
714            ///
715            /// # use core::num::NonZero;
716            /// # fn main() { test().unwrap(); }
717            /// # fn test() -> Option<()> {
718            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1)?.highest_one(), 0);")]
719            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1_0000)?.highest_one(), 4);")]
720            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1_1111)?.highest_one(), 4);")]
721            /// # Some(())
722            /// # }
723            /// ```
724            #[unstable(feature = "int_lowest_highest_one", issue = "145203")]
725            #[must_use = "this returns the result of the operation, \
726                          without modifying the original"]
727            #[inline(always)]
728            pub const fn highest_one(self) -> u32 {
729                Self::BITS - 1 - self.leading_zeros()
730            }
731
732            /// Returns the index of the lowest bit set to one in `self`.
733            ///
734            /// # Examples
735            ///
736            /// ```
737            /// #![feature(int_lowest_highest_one)]
738            ///
739            /// # use core::num::NonZero;
740            /// # fn main() { test().unwrap(); }
741            /// # fn test() -> Option<()> {
742            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1)?.lowest_one(), 0);")]
743            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1_0000)?.lowest_one(), 4);")]
744            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1_1111)?.lowest_one(), 0);")]
745            /// # Some(())
746            /// # }
747            /// ```
748            #[unstable(feature = "int_lowest_highest_one", issue = "145203")]
749            #[must_use = "this returns the result of the operation, \
750                          without modifying the original"]
751            #[inline(always)]
752            pub const fn lowest_one(self) -> u32 {
753                self.trailing_zeros()
754            }
755
756            /// Returns the number of ones in the binary representation of `self`.
757            ///
758            /// # Examples
759            ///
760            /// ```
761            /// # use std::num::NonZero;
762            /// #
763            /// # fn main() { test().unwrap(); }
764            /// # fn test() -> Option<()> {
765            #[doc = concat!("let a = NonZero::<", stringify!($Int), ">::new(0b100_0000)?;")]
766            #[doc = concat!("let b = NonZero::<", stringify!($Int), ">::new(0b100_0011)?;")]
767            ///
768            /// assert_eq!(a.count_ones(), NonZero::new(1)?);
769            /// assert_eq!(b.count_ones(), NonZero::new(3)?);
770            /// # Some(())
771            /// # }
772            /// ```
773            ///
774            #[stable(feature = "non_zero_count_ones", since = "1.86.0")]
775            #[rustc_const_stable(feature = "non_zero_count_ones", since = "1.86.0")]
776            #[doc(alias = "popcount")]
777            #[doc(alias = "popcnt")]
778            #[must_use = "this returns the result of the operation, \
779                        without modifying the original"]
780            #[inline(always)]
781            pub const fn count_ones(self) -> NonZero<u32> {
782                // SAFETY:
783                // `self` is non-zero, which means it has at least one bit set, which means
784                // that the result of `count_ones` is non-zero.
785                unsafe { NonZero::new_unchecked(self.get().count_ones()) }
786            }
787
788            /// Shifts the bits to the left by a specified amount, `n`,
789            /// wrapping the truncated bits to the end of the resulting integer.
790            ///
791            /// Please note this isn't the same operation as the `<<` shifting operator!
792            ///
793            /// # Examples
794            ///
795            /// ```
796            /// #![feature(nonzero_bitwise)]
797            /// # use std::num::NonZero;
798            /// #
799            /// # fn main() { test().unwrap(); }
800            /// # fn test() -> Option<()> {
801            #[doc = concat!("let n = NonZero::new(", $rot_op, stringify!($Int), ")?;")]
802            #[doc = concat!("let m = NonZero::new(", $rot_result, ")?;")]
803            ///
804            #[doc = concat!("assert_eq!(n.rotate_left(", $rot, "), m);")]
805            /// # Some(())
806            /// # }
807            /// ```
808            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
809            #[must_use = "this returns the result of the operation, \
810                        without modifying the original"]
811            #[inline(always)]
812            pub const fn rotate_left(self, n: u32) -> Self {
813                let result = self.get().rotate_left(n);
814                // SAFETY: Rotating bits preserves the property int > 0.
815                unsafe { Self::new_unchecked(result) }
816            }
817
818            /// Shifts the bits to the right by a specified amount, `n`,
819            /// wrapping the truncated bits to the beginning of the resulting
820            /// integer.
821            ///
822            /// Please note this isn't the same operation as the `>>` shifting operator!
823            ///
824            /// # Examples
825            ///
826            /// ```
827            /// #![feature(nonzero_bitwise)]
828            /// # use std::num::NonZero;
829            /// #
830            /// # fn main() { test().unwrap(); }
831            /// # fn test() -> Option<()> {
832            #[doc = concat!("let n = NonZero::new(", $rot_result, stringify!($Int), ")?;")]
833            #[doc = concat!("let m = NonZero::new(", $rot_op, ")?;")]
834            ///
835            #[doc = concat!("assert_eq!(n.rotate_right(", $rot, "), m);")]
836            /// # Some(())
837            /// # }
838            /// ```
839            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
840            #[must_use = "this returns the result of the operation, \
841                        without modifying the original"]
842            #[inline(always)]
843            pub const fn rotate_right(self, n: u32) -> Self {
844                let result = self.get().rotate_right(n);
845                // SAFETY: Rotating bits preserves the property int > 0.
846                unsafe { Self::new_unchecked(result) }
847            }
848
849            /// Reverses the byte order of the integer.
850            ///
851            /// # Examples
852            ///
853            /// ```
854            /// #![feature(nonzero_bitwise)]
855            /// # use std::num::NonZero;
856            /// #
857            /// # fn main() { test().unwrap(); }
858            /// # fn test() -> Option<()> {
859            #[doc = concat!("let n = NonZero::new(", $swap_op, stringify!($Int), ")?;")]
860            /// let m = n.swap_bytes();
861            ///
862            #[doc = concat!("assert_eq!(m, NonZero::new(", $swapped, ")?);")]
863            /// # Some(())
864            /// # }
865            /// ```
866            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
867            #[must_use = "this returns the result of the operation, \
868                        without modifying the original"]
869            #[inline(always)]
870            pub const fn swap_bytes(self) -> Self {
871                let result = self.get().swap_bytes();
872                // SAFETY: Shuffling bytes preserves the property int > 0.
873                unsafe { Self::new_unchecked(result) }
874            }
875
876            /// Reverses the order of bits in the integer. The least significant bit becomes the most significant bit,
877            /// second least-significant bit becomes second most-significant bit, etc.
878            ///
879            /// # Examples
880            ///
881            /// ```
882            /// #![feature(nonzero_bitwise)]
883            /// # use std::num::NonZero;
884            /// #
885            /// # fn main() { test().unwrap(); }
886            /// # fn test() -> Option<()> {
887            #[doc = concat!("let n = NonZero::new(", $swap_op, stringify!($Int), ")?;")]
888            /// let m = n.reverse_bits();
889            ///
890            #[doc = concat!("assert_eq!(m, NonZero::new(", $reversed, ")?);")]
891            /// # Some(())
892            /// # }
893            /// ```
894            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
895            #[must_use = "this returns the result of the operation, \
896                        without modifying the original"]
897            #[inline(always)]
898            pub const fn reverse_bits(self) -> Self {
899                let result = self.get().reverse_bits();
900                // SAFETY: Reversing bits preserves the property int > 0.
901                unsafe { Self::new_unchecked(result) }
902            }
903
904            /// Converts an integer from big endian to the target's endianness.
905            ///
906            /// On big endian this is a no-op. On little endian the bytes are
907            /// swapped.
908            ///
909            /// # Examples
910            ///
911            /// ```
912            /// #![feature(nonzero_bitwise)]
913            /// # use std::num::NonZero;
914            #[doc = concat!("use std::num::", stringify!($Ty), ";")]
915            /// #
916            /// # fn main() { test().unwrap(); }
917            /// # fn test() -> Option<()> {
918            #[doc = concat!("let n = NonZero::new(0x1A", stringify!($Int), ")?;")]
919            ///
920            /// if cfg!(target_endian = "big") {
921            #[doc = concat!("    assert_eq!(", stringify!($Ty), "::from_be(n), n)")]
922            /// } else {
923            #[doc = concat!("    assert_eq!(", stringify!($Ty), "::from_be(n), n.swap_bytes())")]
924            /// }
925            /// # Some(())
926            /// # }
927            /// ```
928            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
929            #[must_use]
930            #[inline(always)]
931            pub const fn from_be(x: Self) -> Self {
932                let result = $Int::from_be(x.get());
933                // SAFETY: Shuffling bytes preserves the property int > 0.
934                unsafe { Self::new_unchecked(result) }
935            }
936
937            /// Converts an integer from little endian to the target's endianness.
938            ///
939            /// On little endian this is a no-op. On big endian the bytes are
940            /// swapped.
941            ///
942            /// # Examples
943            ///
944            /// ```
945            /// #![feature(nonzero_bitwise)]
946            /// # use std::num::NonZero;
947            #[doc = concat!("use std::num::", stringify!($Ty), ";")]
948            /// #
949            /// # fn main() { test().unwrap(); }
950            /// # fn test() -> Option<()> {
951            #[doc = concat!("let n = NonZero::new(0x1A", stringify!($Int), ")?;")]
952            ///
953            /// if cfg!(target_endian = "little") {
954            #[doc = concat!("    assert_eq!(", stringify!($Ty), "::from_le(n), n)")]
955            /// } else {
956            #[doc = concat!("    assert_eq!(", stringify!($Ty), "::from_le(n), n.swap_bytes())")]
957            /// }
958            /// # Some(())
959            /// # }
960            /// ```
961            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
962            #[must_use]
963            #[inline(always)]
964            pub const fn from_le(x: Self) -> Self {
965                let result = $Int::from_le(x.get());
966                // SAFETY: Shuffling bytes preserves the property int > 0.
967                unsafe { Self::new_unchecked(result) }
968            }
969
970            /// Converts `self` to big endian from the target's endianness.
971            ///
972            /// On big endian this is a no-op. On little endian the bytes are
973            /// swapped.
974            ///
975            /// # Examples
976            ///
977            /// ```
978            /// #![feature(nonzero_bitwise)]
979            /// # use std::num::NonZero;
980            /// #
981            /// # fn main() { test().unwrap(); }
982            /// # fn test() -> Option<()> {
983            #[doc = concat!("let n = NonZero::new(0x1A", stringify!($Int), ")?;")]
984            ///
985            /// if cfg!(target_endian = "big") {
986            ///     assert_eq!(n.to_be(), n)
987            /// } else {
988            ///     assert_eq!(n.to_be(), n.swap_bytes())
989            /// }
990            /// # Some(())
991            /// # }
992            /// ```
993            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
994            #[must_use = "this returns the result of the operation, \
995                        without modifying the original"]
996            #[inline(always)]
997            pub const fn to_be(self) -> Self {
998                let result = self.get().to_be();
999                // SAFETY: Shuffling bytes preserves the property int > 0.
1000                unsafe { Self::new_unchecked(result) }
1001            }
1002
1003            /// Converts `self` to little endian from the target's endianness.
1004            ///
1005            /// On little endian this is a no-op. On big endian the bytes are
1006            /// swapped.
1007            ///
1008            /// # Examples
1009            ///
1010            /// ```
1011            /// #![feature(nonzero_bitwise)]
1012            /// # use std::num::NonZero;
1013            /// #
1014            /// # fn main() { test().unwrap(); }
1015            /// # fn test() -> Option<()> {
1016            #[doc = concat!("let n = NonZero::new(0x1A", stringify!($Int), ")?;")]
1017            ///
1018            /// if cfg!(target_endian = "little") {
1019            ///     assert_eq!(n.to_le(), n)
1020            /// } else {
1021            ///     assert_eq!(n.to_le(), n.swap_bytes())
1022            /// }
1023            /// # Some(())
1024            /// # }
1025            /// ```
1026            #[unstable(feature = "nonzero_bitwise", issue = "128281")]
1027            #[must_use = "this returns the result of the operation, \
1028                        without modifying the original"]
1029            #[inline(always)]
1030            pub const fn to_le(self) -> Self {
1031                let result = self.get().to_le();
1032                // SAFETY: Shuffling bytes preserves the property int > 0.
1033                unsafe { Self::new_unchecked(result) }
1034            }
1035
1036            nonzero_integer_signedness_dependent_methods! {
1037                Primitive = $signedness $Int,
1038                SignedPrimitive = $Sint,
1039                UnsignedPrimitive = $Uint,
1040            }
1041
1042            /// Multiplies two non-zero integers together.
1043            /// Checks for overflow and returns [`None`] on overflow.
1044            /// As a consequence, the result cannot wrap to zero.
1045            ///
1046            /// # Examples
1047            ///
1048            /// ```
1049            /// # use std::num::NonZero;
1050            /// #
1051            /// # fn main() { test().unwrap(); }
1052            /// # fn test() -> Option<()> {
1053            #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1054            #[doc = concat!("let four = NonZero::new(4", stringify!($Int), ")?;")]
1055            #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1056            ///
1057            /// assert_eq!(Some(four), two.checked_mul(two));
1058            /// assert_eq!(None, max.checked_mul(two));
1059            /// # Some(())
1060            /// # }
1061            /// ```
1062            #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1063            #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1064            #[must_use = "this returns the result of the operation, \
1065                          without modifying the original"]
1066            #[inline]
1067            pub const fn checked_mul(self, other: Self) -> Option<Self> {
1068                if let Some(result) = self.get().checked_mul(other.get()) {
1069                    // SAFETY:
1070                    // - `checked_mul` returns `None` on overflow
1071                    // - `self` and `other` are non-zero
1072                    // - the only way to get zero from a multiplication without overflow is for one
1073                    //   of the sides to be zero
1074                    //
1075                    // So the result cannot be zero.
1076                    Some(unsafe { Self::new_unchecked(result) })
1077                } else {
1078                    None
1079                }
1080            }
1081
1082            /// Multiplies two non-zero integers together.
1083            #[doc = concat!("Return [`NonZero::<", stringify!($Int), ">::MAX`] on overflow.")]
1084            ///
1085            /// # Examples
1086            ///
1087            /// ```
1088            /// # use std::num::NonZero;
1089            /// #
1090            /// # fn main() { test().unwrap(); }
1091            /// # fn test() -> Option<()> {
1092            #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1093            #[doc = concat!("let four = NonZero::new(4", stringify!($Int), ")?;")]
1094            #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1095            ///
1096            /// assert_eq!(four, two.saturating_mul(two));
1097            /// assert_eq!(max, four.saturating_mul(max));
1098            /// # Some(())
1099            /// # }
1100            /// ```
1101            #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1102            #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1103            #[must_use = "this returns the result of the operation, \
1104                          without modifying the original"]
1105            #[inline]
1106            pub const fn saturating_mul(self, other: Self) -> Self {
1107                // SAFETY:
1108                // - `saturating_mul` returns `u*::MAX`/`i*::MAX`/`i*::MIN` on overflow/underflow,
1109                //   all of which are non-zero
1110                // - `self` and `other` are non-zero
1111                // - the only way to get zero from a multiplication without overflow is for one
1112                //   of the sides to be zero
1113                //
1114                // So the result cannot be zero.
1115                unsafe { Self::new_unchecked(self.get().saturating_mul(other.get())) }
1116            }
1117
1118            /// Multiplies two non-zero integers together,
1119            /// assuming overflow cannot occur.
1120            /// Overflow is unchecked, and it is undefined behavior to overflow
1121            /// *even if the result would wrap to a non-zero value*.
1122            /// The behavior is undefined as soon as
1123            #[doc = sign_dependent_expr!{
1124                $signedness ?
1125                if signed {
1126                    concat!("`self * rhs > ", stringify!($Int), "::MAX`, ",
1127                            "or `self * rhs < ", stringify!($Int), "::MIN`.")
1128                }
1129                if unsigned {
1130                    concat!("`self * rhs > ", stringify!($Int), "::MAX`.")
1131                }
1132            }]
1133            ///
1134            /// # Examples
1135            ///
1136            /// ```
1137            /// #![feature(nonzero_ops)]
1138            ///
1139            /// # use std::num::NonZero;
1140            /// #
1141            /// # fn main() { test().unwrap(); }
1142            /// # fn test() -> Option<()> {
1143            #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1144            #[doc = concat!("let four = NonZero::new(4", stringify!($Int), ")?;")]
1145            ///
1146            /// assert_eq!(four, unsafe { two.unchecked_mul(two) });
1147            /// # Some(())
1148            /// # }
1149            /// ```
1150            #[unstable(feature = "nonzero_ops", issue = "84186")]
1151            #[must_use = "this returns the result of the operation, \
1152                          without modifying the original"]
1153            #[inline]
1154            pub const unsafe fn unchecked_mul(self, other: Self) -> Self {
1155                // SAFETY: The caller ensures there is no overflow.
1156                unsafe { Self::new_unchecked(self.get().unchecked_mul(other.get())) }
1157            }
1158
1159            /// Raises non-zero value to an integer power.
1160            /// Checks for overflow and returns [`None`] on overflow.
1161            /// As a consequence, the result cannot wrap to zero.
1162            ///
1163            /// # Examples
1164            ///
1165            /// ```
1166            /// # use std::num::NonZero;
1167            /// #
1168            /// # fn main() { test().unwrap(); }
1169            /// # fn test() -> Option<()> {
1170            #[doc = concat!("let three = NonZero::new(3", stringify!($Int), ")?;")]
1171            #[doc = concat!("let twenty_seven = NonZero::new(27", stringify!($Int), ")?;")]
1172            #[doc = concat!("let half_max = NonZero::new(", stringify!($Int), "::MAX / 2)?;")]
1173            ///
1174            /// assert_eq!(Some(twenty_seven), three.checked_pow(3));
1175            /// assert_eq!(None, half_max.checked_pow(3));
1176            /// # Some(())
1177            /// # }
1178            /// ```
1179            #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1180            #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1181            #[must_use = "this returns the result of the operation, \
1182                          without modifying the original"]
1183            #[inline]
1184            pub const fn checked_pow(self, other: u32) -> Option<Self> {
1185                if let Some(result) = self.get().checked_pow(other) {
1186                    // SAFETY:
1187                    // - `checked_pow` returns `None` on overflow/underflow
1188                    // - `self` is non-zero
1189                    // - the only way to get zero from an exponentiation without overflow is
1190                    //   for base to be zero
1191                    //
1192                    // So the result cannot be zero.
1193                    Some(unsafe { Self::new_unchecked(result) })
1194                } else {
1195                    None
1196                }
1197            }
1198
1199            /// Raise non-zero value to an integer power.
1200            #[doc = sign_dependent_expr!{
1201                $signedness ?
1202                if signed {
1203                    concat!("Return [`NonZero::<", stringify!($Int), ">::MIN`] ",
1204                                "or [`NonZero::<", stringify!($Int), ">::MAX`] on overflow.")
1205                }
1206                if unsigned {
1207                    concat!("Return [`NonZero::<", stringify!($Int), ">::MAX`] on overflow.")
1208                }
1209            }]
1210            ///
1211            /// # Examples
1212            ///
1213            /// ```
1214            /// # use std::num::NonZero;
1215            /// #
1216            /// # fn main() { test().unwrap(); }
1217            /// # fn test() -> Option<()> {
1218            #[doc = concat!("let three = NonZero::new(3", stringify!($Int), ")?;")]
1219            #[doc = concat!("let twenty_seven = NonZero::new(27", stringify!($Int), ")?;")]
1220            #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1221            ///
1222            /// assert_eq!(twenty_seven, three.saturating_pow(3));
1223            /// assert_eq!(max, max.saturating_pow(3));
1224            /// # Some(())
1225            /// # }
1226            /// ```
1227            #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1228            #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1229            #[must_use = "this returns the result of the operation, \
1230                          without modifying the original"]
1231            #[inline]
1232            pub const fn saturating_pow(self, other: u32) -> Self {
1233                // SAFETY:
1234                // - `saturating_pow` returns `u*::MAX`/`i*::MAX`/`i*::MIN` on overflow/underflow,
1235                //   all of which are non-zero
1236                // - `self` is non-zero
1237                // - the only way to get zero from an exponentiation without overflow is
1238                //   for base to be zero
1239                //
1240                // So the result cannot be zero.
1241                unsafe { Self::new_unchecked(self.get().saturating_pow(other)) }
1242            }
1243
1244            /// Parses a non-zero integer from an ASCII-byte slice with decimal digits.
1245            ///
1246            /// The characters are expected to be an optional
1247            #[doc = sign_dependent_expr!{
1248                $signedness ?
1249                if signed {
1250                    " `+` or `-` "
1251                }
1252                if unsigned {
1253                    " `+` "
1254                }
1255            }]
1256            /// sign followed by only digits. Leading and trailing non-digit characters (including
1257            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1258            /// also represent an error.
1259            ///
1260            /// # Examples
1261            ///
1262            /// ```
1263            /// #![feature(int_from_ascii)]
1264            ///
1265            /// # use std::num::NonZero;
1266            /// #
1267            /// # fn main() { test().unwrap(); }
1268            /// # fn test() -> Option<()> {
1269            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::from_ascii(b\"+10\"), Ok(NonZero::new(10)?));")]
1270            /// # Some(())
1271            /// # }
1272            /// ```
1273            ///
1274            /// Trailing space returns error:
1275            ///
1276            /// ```
1277            /// #![feature(int_from_ascii)]
1278            ///
1279            /// # use std::num::NonZero;
1280            /// #
1281            #[doc = concat!("assert!(NonZero::<", stringify!($Int), ">::from_ascii(b\"1 \").is_err());")]
1282            /// ```
1283            #[unstable(feature = "int_from_ascii", issue = "134821")]
1284            #[inline]
1285            pub const fn from_ascii(src: &[u8]) -> Result<Self, ParseIntError> {
1286                Self::from_ascii_radix(src, 10)
1287            }
1288
1289            /// Parses a non-zero integer from an ASCII-byte slice with digits in a given base.
1290            ///
1291            /// The characters are expected to be an optional
1292            #[doc = sign_dependent_expr!{
1293                $signedness ?
1294                if signed {
1295                    " `+` or `-` "
1296                }
1297                if unsigned {
1298                    " `+` "
1299                }
1300            }]
1301            /// sign followed by only digits. Leading and trailing non-digit characters (including
1302            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1303            /// also represent an error.
1304            ///
1305            /// Digits are a subset of these characters, depending on `radix`:
1306            ///
1307            /// - `0-9`
1308            /// - `a-z`
1309            /// - `A-Z`
1310            ///
1311            /// # Panics
1312            ///
1313            /// This method panics if `radix` is not in the range from 2 to 36.
1314            ///
1315            /// # Examples
1316            ///
1317            /// ```
1318            /// #![feature(int_from_ascii)]
1319            ///
1320            /// # use std::num::NonZero;
1321            /// #
1322            /// # fn main() { test().unwrap(); }
1323            /// # fn test() -> Option<()> {
1324            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::from_ascii_radix(b\"A\", 16), Ok(NonZero::new(10)?));")]
1325            /// # Some(())
1326            /// # }
1327            /// ```
1328            ///
1329            /// Trailing space returns error:
1330            ///
1331            /// ```
1332            /// #![feature(int_from_ascii)]
1333            ///
1334            /// # use std::num::NonZero;
1335            /// #
1336            #[doc = concat!("assert!(NonZero::<", stringify!($Int), ">::from_ascii_radix(b\"1 \", 10).is_err());")]
1337            /// ```
1338            #[unstable(feature = "int_from_ascii", issue = "134821")]
1339            #[inline]
1340            pub const fn from_ascii_radix(src: &[u8], radix: u32) -> Result<Self, ParseIntError> {
1341                let n = match <$Int>::from_ascii_radix(src, radix) {
1342                    Ok(n) => n,
1343                    Err(err) => return Err(err),
1344                };
1345                if let Some(n) = Self::new(n) {
1346                    Ok(n)
1347                } else {
1348                    Err(ParseIntError { kind: IntErrorKind::Zero })
1349                }
1350            }
1351
1352            /// Parses a non-zero integer from a string slice with digits in a given base.
1353            ///
1354            /// The string is expected to be an optional
1355            #[doc = sign_dependent_expr!{
1356                $signedness ?
1357                if signed {
1358                    " `+` or `-` "
1359                }
1360                if unsigned {
1361                    " `+` "
1362                }
1363            }]
1364            /// sign followed by only digits. Leading and trailing non-digit characters (including
1365            /// whitespace) represent an error. Underscores (which are accepted in Rust literals)
1366            /// also represent an error.
1367            ///
1368            /// Digits are a subset of these characters, depending on `radix`:
1369            ///
1370            /// - `0-9`
1371            /// - `a-z`
1372            /// - `A-Z`
1373            ///
1374            /// # Panics
1375            ///
1376            /// This method panics if `radix` is not in the range from 2 to 36.
1377            ///
1378            /// # Examples
1379            ///
1380            /// ```
1381            /// #![feature(nonzero_from_str_radix)]
1382            ///
1383            /// # use std::num::NonZero;
1384            /// #
1385            /// # fn main() { test().unwrap(); }
1386            /// # fn test() -> Option<()> {
1387            #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::from_str_radix(\"A\", 16), Ok(NonZero::new(10)?));")]
1388            /// # Some(())
1389            /// # }
1390            /// ```
1391            ///
1392            /// Trailing space returns error:
1393            ///
1394            /// ```
1395            /// #![feature(nonzero_from_str_radix)]
1396            ///
1397            /// # use std::num::NonZero;
1398            /// #
1399            #[doc = concat!("assert!(NonZero::<", stringify!($Int), ">::from_str_radix(\"1 \", 10).is_err());")]
1400            /// ```
1401            #[unstable(feature = "nonzero_from_str_radix", issue = "152193")]
1402            #[inline]
1403            pub const fn from_str_radix(src: &str, radix: u32) -> Result<Self, ParseIntError> {
1404                Self::from_ascii_radix(src.as_bytes(), radix)
1405            }
1406        }
1407
1408        #[stable(feature = "nonzero_parse", since = "1.35.0")]
1409        impl FromStr for NonZero<$Int> {
1410            type Err = ParseIntError;
1411            fn from_str(src: &str) -> Result<Self, Self::Err> {
1412                Self::from_str_radix(src, 10)
1413            }
1414        }
1415
1416        nonzero_integer_signedness_dependent_impls!($signedness $Int);
1417    };
1418
1419    (
1420        Self = $Ty:ident,
1421        Primitive = unsigned $Int:ident,
1422        SignedPrimitive = $Sint:ident,
1423        rot = $rot:literal,
1424        rot_op = $rot_op:literal,
1425        rot_result = $rot_result:literal,
1426        swap_op = $swap_op:literal,
1427        swapped = $swapped:literal,
1428        reversed = $reversed:literal,
1429        $(,)?
1430    ) => {
1431        nonzero_integer! {
1432            #[stable(feature = "nonzero", since = "1.28.0")]
1433            Self = $Ty,
1434            Primitive = unsigned $Int,
1435            SignedPrimitive = $Sint,
1436            UnsignedPrimitive = $Int,
1437            rot = $rot,
1438            rot_op = $rot_op,
1439            rot_result = $rot_result,
1440            swap_op = $swap_op,
1441            swapped = $swapped,
1442            reversed = $reversed,
1443            leading_zeros_test = concat!(stringify!($Int), "::MAX"),
1444        }
1445    };
1446
1447    (
1448        Self = $Ty:ident,
1449        Primitive = signed $Int:ident,
1450        UnsignedPrimitive = $Uint:ident,
1451        rot = $rot:literal,
1452        rot_op = $rot_op:literal,
1453        rot_result = $rot_result:literal,
1454        swap_op = $swap_op:literal,
1455        swapped = $swapped:literal,
1456        reversed = $reversed:literal,
1457    ) => {
1458        nonzero_integer! {
1459            #[stable(feature = "signed_nonzero", since = "1.34.0")]
1460            Self = $Ty,
1461            Primitive = signed $Int,
1462            SignedPrimitive = $Int,
1463            UnsignedPrimitive = $Uint,
1464            rot = $rot,
1465            rot_op = $rot_op,
1466            rot_result = $rot_result,
1467            swap_op = $swap_op,
1468            swapped = $swapped,
1469            reversed = $reversed,
1470            leading_zeros_test = concat!("-1", stringify!($Int)),
1471        }
1472    };
1473}
1474
1475macro_rules! nonzero_integer_signedness_dependent_impls {
1476    // Impls for unsigned nonzero types only.
1477    (unsigned $Int:ty) => {
1478        #[stable(feature = "nonzero_div", since = "1.51.0")]
1479        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1480        impl const Div<NonZero<$Int>> for $Int {
1481            type Output = $Int;
1482
1483            /// Same as `self / other.get()`, but because `other` is a `NonZero<_>`,
1484            /// there's never a runtime check for division-by-zero.
1485            ///
1486            /// This operation rounds towards zero, truncating any fractional
1487            /// part of the exact result, and cannot panic.
1488            #[doc(alias = "unchecked_div")]
1489            #[inline]
1490            fn div(self, other: NonZero<$Int>) -> $Int {
1491                // SAFETY: Division by zero is checked because `other` is non-zero,
1492                // and MIN/-1 is checked because `self` is an unsigned int.
1493                unsafe { intrinsics::unchecked_div(self, other.get()) }
1494            }
1495        }
1496
1497        #[stable(feature = "nonzero_div_assign", since = "1.79.0")]
1498        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1499        impl const DivAssign<NonZero<$Int>> for $Int {
1500            /// Same as `self /= other.get()`, but because `other` is a `NonZero<_>`,
1501            /// there's never a runtime check for division-by-zero.
1502            ///
1503            /// This operation rounds towards zero, truncating any fractional
1504            /// part of the exact result, and cannot panic.
1505            #[inline]
1506            fn div_assign(&mut self, other: NonZero<$Int>) {
1507                *self = *self / other;
1508            }
1509        }
1510
1511        #[stable(feature = "nonzero_div", since = "1.51.0")]
1512        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1513        impl const Rem<NonZero<$Int>> for $Int {
1514            type Output = $Int;
1515
1516            /// This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.
1517            #[inline]
1518            fn rem(self, other: NonZero<$Int>) -> $Int {
1519                // SAFETY: Remainder by zero is checked because `other` is non-zero,
1520                // and MIN/-1 is checked because `self` is an unsigned int.
1521                unsafe { intrinsics::unchecked_rem(self, other.get()) }
1522            }
1523        }
1524
1525        #[stable(feature = "nonzero_div_assign", since = "1.79.0")]
1526        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1527        impl const RemAssign<NonZero<$Int>> for $Int {
1528            /// This operation satisfies `n % d == n - (n / d) * d`, and cannot panic.
1529            #[inline]
1530            fn rem_assign(&mut self, other: NonZero<$Int>) {
1531                *self = *self % other;
1532            }
1533        }
1534
1535        impl NonZero<$Int> {
1536            /// Calculates the quotient of `self` and `rhs`, rounding the result towards positive infinity.
1537            ///
1538            /// The result is guaranteed to be non-zero.
1539            ///
1540            /// # Examples
1541            ///
1542            /// ```
1543            /// # use std::num::NonZero;
1544            #[doc = concat!("let one = NonZero::new(1", stringify!($Int), ").unwrap();")]
1545            #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX).unwrap();")]
1546            /// assert_eq!(one.div_ceil(max), one);
1547            ///
1548            #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ").unwrap();")]
1549            #[doc = concat!("let three = NonZero::new(3", stringify!($Int), ").unwrap();")]
1550            /// assert_eq!(three.div_ceil(two), two);
1551            /// ```
1552            #[stable(feature = "unsigned_nonzero_div_ceil", since = "1.92.0")]
1553            #[rustc_const_stable(feature = "unsigned_nonzero_div_ceil", since = "1.92.0")]
1554            #[must_use = "this returns the result of the operation, \
1555                          without modifying the original"]
1556            #[inline]
1557            pub const fn div_ceil(self, rhs: Self) -> Self {
1558                let v = self.get().div_ceil(rhs.get());
1559                // SAFETY: ceiled division of two positive integers can never be zero.
1560                unsafe { Self::new_unchecked(v) }
1561            }
1562        }
1563    };
1564    // Impls for signed nonzero types only.
1565    (signed $Int:ty) => {
1566        #[stable(feature = "signed_nonzero_neg", since = "1.71.0")]
1567        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
1568        impl const Neg for NonZero<$Int> {
1569            type Output = Self;
1570
1571            #[inline]
1572            fn neg(self) -> Self {
1573                // SAFETY: negation of nonzero cannot yield zero values.
1574                unsafe { Self::new_unchecked(self.get().neg()) }
1575            }
1576        }
1577
1578        forward_ref_unop! { impl Neg, neg for NonZero<$Int>,
1579        #[stable(feature = "signed_nonzero_neg", since = "1.71.0")]
1580        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
1581    };
1582}
1583
1584#[rustfmt::skip] // https://github.com/rust-lang/rustfmt/issues/5974
1585macro_rules! nonzero_integer_signedness_dependent_methods {
1586    // Associated items for unsigned nonzero types only.
1587    (
1588        Primitive = unsigned $Int:ident,
1589        SignedPrimitive = $Sint:ty,
1590        UnsignedPrimitive = $Uint:ty,
1591    ) => {
1592        /// The smallest value that can be represented by this non-zero
1593        /// integer type, 1.
1594        ///
1595        /// # Examples
1596        ///
1597        /// ```
1598        /// # use std::num::NonZero;
1599        /// #
1600        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::MIN.get(), 1", stringify!($Int), ");")]
1601        /// ```
1602        #[stable(feature = "nonzero_min_max", since = "1.70.0")]
1603        pub const MIN: Self = Self::new(1).unwrap();
1604
1605        /// The largest value that can be represented by this non-zero
1606        /// integer type,
1607        #[doc = concat!("equal to [`", stringify!($Int), "::MAX`].")]
1608        ///
1609        /// # Examples
1610        ///
1611        /// ```
1612        /// # use std::num::NonZero;
1613        /// #
1614        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::MAX.get(), ", stringify!($Int), "::MAX);")]
1615        /// ```
1616        #[stable(feature = "nonzero_min_max", since = "1.70.0")]
1617        pub const MAX: Self = Self::new(<$Int>::MAX).unwrap();
1618
1619        /// Adds an unsigned integer to a non-zero value.
1620        /// Checks for overflow and returns [`None`] on overflow.
1621        /// As a consequence, the result cannot wrap to zero.
1622        ///
1623        ///
1624        /// # Examples
1625        ///
1626        /// ```
1627        /// # use std::num::NonZero;
1628        /// #
1629        /// # fn main() { test().unwrap(); }
1630        /// # fn test() -> Option<()> {
1631        #[doc = concat!("let one = NonZero::new(1", stringify!($Int), ")?;")]
1632        #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1633        #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1634        ///
1635        /// assert_eq!(Some(two), one.checked_add(1));
1636        /// assert_eq!(None, max.checked_add(1));
1637        /// # Some(())
1638        /// # }
1639        /// ```
1640        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1641        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1642        #[must_use = "this returns the result of the operation, \
1643                      without modifying the original"]
1644        #[inline]
1645        pub const fn checked_add(self, other: $Int) -> Option<Self> {
1646            if let Some(result) = self.get().checked_add(other) {
1647                // SAFETY:
1648                // - `checked_add` returns `None` on overflow
1649                // - `self` is non-zero
1650                // - the only way to get zero from an addition without overflow is for both
1651                //   sides to be zero
1652                //
1653                // So the result cannot be zero.
1654                Some(unsafe { Self::new_unchecked(result) })
1655            } else {
1656                None
1657            }
1658        }
1659
1660        /// Adds an unsigned integer to a non-zero value.
1661        #[doc = concat!("Return [`NonZero::<", stringify!($Int), ">::MAX`] on overflow.")]
1662        ///
1663        /// # Examples
1664        ///
1665        /// ```
1666        /// # use std::num::NonZero;
1667        /// #
1668        /// # fn main() { test().unwrap(); }
1669        /// # fn test() -> Option<()> {
1670        #[doc = concat!("let one = NonZero::new(1", stringify!($Int), ")?;")]
1671        #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1672        #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1673        ///
1674        /// assert_eq!(two, one.saturating_add(1));
1675        /// assert_eq!(max, max.saturating_add(1));
1676        /// # Some(())
1677        /// # }
1678        /// ```
1679        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1680        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1681        #[must_use = "this returns the result of the operation, \
1682                      without modifying the original"]
1683        #[inline]
1684        pub const fn saturating_add(self, other: $Int) -> Self {
1685            // SAFETY:
1686            // - `saturating_add` returns `u*::MAX` on overflow, which is non-zero
1687            // - `self` is non-zero
1688            // - the only way to get zero from an addition without overflow is for both
1689            //   sides to be zero
1690            //
1691            // So the result cannot be zero.
1692            unsafe { Self::new_unchecked(self.get().saturating_add(other)) }
1693        }
1694
1695        /// Adds an unsigned integer to a non-zero value,
1696        /// assuming overflow cannot occur.
1697        /// Overflow is unchecked, and it is undefined behavior to overflow
1698        /// *even if the result would wrap to a non-zero value*.
1699        /// The behavior is undefined as soon as
1700        #[doc = concat!("`self + rhs > ", stringify!($Int), "::MAX`.")]
1701        ///
1702        /// # Examples
1703        ///
1704        /// ```
1705        /// #![feature(nonzero_ops)]
1706        ///
1707        /// # use std::num::NonZero;
1708        /// #
1709        /// # fn main() { test().unwrap(); }
1710        /// # fn test() -> Option<()> {
1711        #[doc = concat!("let one = NonZero::new(1", stringify!($Int), ")?;")]
1712        #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1713        ///
1714        /// assert_eq!(two, unsafe { one.unchecked_add(1) });
1715        /// # Some(())
1716        /// # }
1717        /// ```
1718        #[unstable(feature = "nonzero_ops", issue = "84186")]
1719        #[must_use = "this returns the result of the operation, \
1720                      without modifying the original"]
1721        #[inline]
1722        pub const unsafe fn unchecked_add(self, other: $Int) -> Self {
1723            // SAFETY: The caller ensures there is no overflow.
1724            unsafe { Self::new_unchecked(self.get().unchecked_add(other)) }
1725        }
1726
1727        /// Returns the smallest power of two greater than or equal to `self`.
1728        /// Checks for overflow and returns [`None`]
1729        /// if the next power of two is greater than the type’s maximum value.
1730        /// As a consequence, the result cannot wrap to zero.
1731        ///
1732        /// # Examples
1733        ///
1734        /// ```
1735        /// # use std::num::NonZero;
1736        /// #
1737        /// # fn main() { test().unwrap(); }
1738        /// # fn test() -> Option<()> {
1739        #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1740        #[doc = concat!("let three = NonZero::new(3", stringify!($Int), ")?;")]
1741        #[doc = concat!("let four = NonZero::new(4", stringify!($Int), ")?;")]
1742        #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
1743        ///
1744        /// assert_eq!(Some(two), two.checked_next_power_of_two() );
1745        /// assert_eq!(Some(four), three.checked_next_power_of_two() );
1746        /// assert_eq!(None, max.checked_next_power_of_two() );
1747        /// # Some(())
1748        /// # }
1749        /// ```
1750        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
1751        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
1752        #[must_use = "this returns the result of the operation, \
1753                      without modifying the original"]
1754        #[inline]
1755        pub const fn checked_next_power_of_two(self) -> Option<Self> {
1756            if let Some(nz) = self.get().checked_next_power_of_two() {
1757                // SAFETY: The next power of two is positive
1758                // and overflow is checked.
1759                Some(unsafe { Self::new_unchecked(nz) })
1760            } else {
1761                None
1762            }
1763        }
1764
1765        /// Returns the base 2 logarithm of the number, rounded down.
1766        ///
1767        /// This is the same operation as
1768        #[doc = concat!("[`", stringify!($Int), "::ilog2`],")]
1769        /// except that it has no failure cases to worry about
1770        /// since this value can never be zero.
1771        ///
1772        /// # Examples
1773        ///
1774        /// ```
1775        /// # use std::num::NonZero;
1776        /// #
1777        /// # fn main() { test().unwrap(); }
1778        /// # fn test() -> Option<()> {
1779        #[doc = concat!("assert_eq!(NonZero::new(7", stringify!($Int), ")?.ilog2(), 2);")]
1780        #[doc = concat!("assert_eq!(NonZero::new(8", stringify!($Int), ")?.ilog2(), 3);")]
1781        #[doc = concat!("assert_eq!(NonZero::new(9", stringify!($Int), ")?.ilog2(), 3);")]
1782        /// # Some(())
1783        /// # }
1784        /// ```
1785        #[stable(feature = "int_log", since = "1.67.0")]
1786        #[rustc_const_stable(feature = "int_log", since = "1.67.0")]
1787        #[must_use = "this returns the result of the operation, \
1788                      without modifying the original"]
1789        #[inline]
1790        pub const fn ilog2(self) -> u32 {
1791            Self::BITS - 1 - self.leading_zeros()
1792        }
1793
1794        /// Returns the base 10 logarithm of the number, rounded down.
1795        ///
1796        /// This is the same operation as
1797        #[doc = concat!("[`", stringify!($Int), "::ilog10`],")]
1798        /// except that it has no failure cases to worry about
1799        /// since this value can never be zero.
1800        ///
1801        /// # Examples
1802        ///
1803        /// ```
1804        /// # use std::num::NonZero;
1805        /// #
1806        /// # fn main() { test().unwrap(); }
1807        /// # fn test() -> Option<()> {
1808        #[doc = concat!("assert_eq!(NonZero::new(99", stringify!($Int), ")?.ilog10(), 1);")]
1809        #[doc = concat!("assert_eq!(NonZero::new(100", stringify!($Int), ")?.ilog10(), 2);")]
1810        #[doc = concat!("assert_eq!(NonZero::new(101", stringify!($Int), ")?.ilog10(), 2);")]
1811        /// # Some(())
1812        /// # }
1813        /// ```
1814        #[stable(feature = "int_log", since = "1.67.0")]
1815        #[rustc_const_stable(feature = "int_log", since = "1.67.0")]
1816        #[must_use = "this returns the result of the operation, \
1817                      without modifying the original"]
1818        #[inline]
1819        pub const fn ilog10(self) -> u32 {
1820            super::int_log10::$Int(self)
1821        }
1822
1823        /// Calculates the midpoint (average) between `self` and `rhs`.
1824        ///
1825        /// `midpoint(a, b)` is `(a + b) >> 1` as if it were performed in a
1826        /// sufficiently-large signed integral type. This implies that the result is
1827        /// always rounded towards negative infinity and that no overflow will ever occur.
1828        ///
1829        /// # Examples
1830        ///
1831        /// ```
1832        /// # use std::num::NonZero;
1833        /// #
1834        /// # fn main() { test().unwrap(); }
1835        /// # fn test() -> Option<()> {
1836        #[doc = concat!("let one = NonZero::new(1", stringify!($Int), ")?;")]
1837        #[doc = concat!("let two = NonZero::new(2", stringify!($Int), ")?;")]
1838        #[doc = concat!("let four = NonZero::new(4", stringify!($Int), ")?;")]
1839        ///
1840        /// assert_eq!(one.midpoint(four), two);
1841        /// assert_eq!(four.midpoint(one), two);
1842        /// # Some(())
1843        /// # }
1844        /// ```
1845        #[stable(feature = "num_midpoint", since = "1.85.0")]
1846        #[rustc_const_stable(feature = "num_midpoint", since = "1.85.0")]
1847        #[must_use = "this returns the result of the operation, \
1848                      without modifying the original"]
1849        #[doc(alias = "average_floor")]
1850        #[doc(alias = "average")]
1851        #[inline]
1852        pub const fn midpoint(self, rhs: Self) -> Self {
1853            // SAFETY: The only way to get `0` with midpoint is to have two opposite or
1854            // near opposite numbers: (-5, 5), (0, 1), (0, 0) which is impossible because
1855            // of the unsignedness of this number and also because `Self` is guaranteed to
1856            // never being 0.
1857            unsafe { Self::new_unchecked(self.get().midpoint(rhs.get())) }
1858        }
1859
1860        /// Returns `true` if and only if `self == (1 << k)` for some `k`.
1861        ///
1862        /// On many architectures, this function can perform better than `is_power_of_two()`
1863        /// on the underlying integer type, as special handling of zero can be avoided.
1864        ///
1865        /// # Examples
1866        ///
1867        /// ```
1868        /// # use std::num::NonZero;
1869        /// #
1870        /// # fn main() { test().unwrap(); }
1871        /// # fn test() -> Option<()> {
1872        #[doc = concat!("let eight = NonZero::new(8", stringify!($Int), ")?;")]
1873        /// assert!(eight.is_power_of_two());
1874        #[doc = concat!("let ten = NonZero::new(10", stringify!($Int), ")?;")]
1875        /// assert!(!ten.is_power_of_two());
1876        /// # Some(())
1877        /// # }
1878        /// ```
1879        #[must_use]
1880        #[stable(feature = "nonzero_is_power_of_two", since = "1.59.0")]
1881        #[rustc_const_stable(feature = "nonzero_is_power_of_two", since = "1.59.0")]
1882        #[inline]
1883        pub const fn is_power_of_two(self) -> bool {
1884            // LLVM 11 normalizes `unchecked_sub(x, 1) & x == 0` to the implementation seen here.
1885            // On the basic x86-64 target, this saves 3 instructions for the zero check.
1886            // On x86_64 with BMI1, being nonzero lets it codegen to `BLSR`, which saves an instruction
1887            // compared to the `POPCNT` implementation on the underlying integer type.
1888
1889            intrinsics::ctpop(self.get()) < 2
1890        }
1891
1892        /// Returns the square root of the number, rounded down.
1893        ///
1894        /// # Examples
1895        ///
1896        /// ```
1897        /// # use std::num::NonZero;
1898        /// #
1899        /// # fn main() { test().unwrap(); }
1900        /// # fn test() -> Option<()> {
1901        #[doc = concat!("let ten = NonZero::new(10", stringify!($Int), ")?;")]
1902        #[doc = concat!("let three = NonZero::new(3", stringify!($Int), ")?;")]
1903        ///
1904        /// assert_eq!(ten.isqrt(), three);
1905        /// # Some(())
1906        /// # }
1907        /// ```
1908        #[stable(feature = "isqrt", since = "1.84.0")]
1909        #[rustc_const_stable(feature = "isqrt", since = "1.84.0")]
1910        #[must_use = "this returns the result of the operation, \
1911                      without modifying the original"]
1912        #[inline]
1913        pub const fn isqrt(self) -> Self {
1914            let result = self.get().isqrt();
1915
1916            // SAFETY: Integer square root is a monotonically nondecreasing
1917            // function, which means that increasing the input will never cause
1918            // the output to decrease. Thus, since the input for nonzero
1919            // unsigned integers has a lower bound of 1, the lower bound of the
1920            // results will be sqrt(1), which is 1, so a result can't be zero.
1921            unsafe { Self::new_unchecked(result) }
1922        }
1923
1924        /// Returns the bit pattern of `self` reinterpreted as a signed integer of the same size.
1925        ///
1926        /// # Examples
1927        ///
1928        /// ```
1929        /// # use std::num::NonZero;
1930        ///
1931        #[doc = concat!("let n = NonZero::<", stringify!($Int), ">::MAX;")]
1932        ///
1933        #[doc = concat!("assert_eq!(n.cast_signed(), NonZero::new(-1", stringify!($Sint), ").unwrap());")]
1934        /// ```
1935        #[stable(feature = "integer_sign_cast", since = "1.87.0")]
1936        #[rustc_const_stable(feature = "integer_sign_cast", since = "1.87.0")]
1937        #[must_use = "this returns the result of the operation, \
1938                      without modifying the original"]
1939        #[inline(always)]
1940        pub const fn cast_signed(self) -> NonZero<$Sint> {
1941            // SAFETY: `self.get()` can't be zero
1942            unsafe { NonZero::new_unchecked(self.get().cast_signed()) }
1943        }
1944
1945        /// Returns the minimum number of bits required to represent `self`.
1946        ///
1947        /// # Examples
1948        ///
1949        /// ```
1950        /// #![feature(uint_bit_width)]
1951        ///
1952        /// # use core::num::NonZero;
1953        /// #
1954        /// # fn main() { test().unwrap(); }
1955        /// # fn test() -> Option<()> {
1956        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::MIN.bit_width(), NonZero::new(1)?);")]
1957        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b111)?.bit_width(), NonZero::new(3)?);")]
1958        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::new(0b1110)?.bit_width(), NonZero::new(4)?);")]
1959        /// # Some(())
1960        /// # }
1961        /// ```
1962        #[unstable(feature = "uint_bit_width", issue = "142326")]
1963        #[must_use = "this returns the result of the operation, \
1964                      without modifying the original"]
1965        #[inline(always)]
1966        pub const fn bit_width(self) -> NonZero<u32> {
1967            // SAFETY: Since `self.leading_zeros()` is always less than
1968            // `Self::BITS`, this subtraction can never be zero.
1969            unsafe { NonZero::new_unchecked(Self::BITS - self.leading_zeros()) }
1970        }
1971    };
1972
1973    // Associated items for signed nonzero types only.
1974    (
1975        Primitive = signed $Int:ident,
1976        SignedPrimitive = $Sint:ty,
1977        UnsignedPrimitive = $Uint:ty,
1978    ) => {
1979        /// The smallest value that can be represented by this non-zero
1980        /// integer type,
1981        #[doc = concat!("equal to [`", stringify!($Int), "::MIN`].")]
1982        ///
1983        /// Note: While most integer types are defined for every whole
1984        /// number between `MIN` and `MAX`, signed non-zero integers are
1985        /// a special case. They have a "gap" at 0.
1986        ///
1987        /// # Examples
1988        ///
1989        /// ```
1990        /// # use std::num::NonZero;
1991        /// #
1992        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::MIN.get(), ", stringify!($Int), "::MIN);")]
1993        /// ```
1994        #[stable(feature = "nonzero_min_max", since = "1.70.0")]
1995        pub const MIN: Self = Self::new(<$Int>::MIN).unwrap();
1996
1997        /// The largest value that can be represented by this non-zero
1998        /// integer type,
1999        #[doc = concat!("equal to [`", stringify!($Int), "::MAX`].")]
2000        ///
2001        /// Note: While most integer types are defined for every whole
2002        /// number between `MIN` and `MAX`, signed non-zero integers are
2003        /// a special case. They have a "gap" at 0.
2004        ///
2005        /// # Examples
2006        ///
2007        /// ```
2008        /// # use std::num::NonZero;
2009        /// #
2010        #[doc = concat!("assert_eq!(NonZero::<", stringify!($Int), ">::MAX.get(), ", stringify!($Int), "::MAX);")]
2011        /// ```
2012        #[stable(feature = "nonzero_min_max", since = "1.70.0")]
2013        pub const MAX: Self = Self::new(<$Int>::MAX).unwrap();
2014
2015        /// Computes the absolute value of self.
2016        #[doc = concat!("See [`", stringify!($Int), "::abs`]")]
2017        /// for documentation on overflow behavior.
2018        ///
2019        /// # Example
2020        ///
2021        /// ```
2022        /// # use std::num::NonZero;
2023        /// #
2024        /// # fn main() { test().unwrap(); }
2025        /// # fn test() -> Option<()> {
2026        #[doc = concat!("let pos = NonZero::new(1", stringify!($Int), ")?;")]
2027        #[doc = concat!("let neg = NonZero::new(-1", stringify!($Int), ")?;")]
2028        ///
2029        /// assert_eq!(pos, pos.abs());
2030        /// assert_eq!(pos, neg.abs());
2031        /// # Some(())
2032        /// # }
2033        /// ```
2034        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2035        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2036        #[must_use = "this returns the result of the operation, \
2037                      without modifying the original"]
2038        #[inline]
2039        pub const fn abs(self) -> Self {
2040            // SAFETY: This cannot overflow to zero.
2041            unsafe { Self::new_unchecked(self.get().abs()) }
2042        }
2043
2044        /// Checked absolute value.
2045        /// Checks for overflow and returns [`None`] if
2046        #[doc = concat!("`self == NonZero::<", stringify!($Int), ">::MIN`.")]
2047        /// The result cannot be zero.
2048        ///
2049        /// # Example
2050        ///
2051        /// ```
2052        /// # use std::num::NonZero;
2053        /// #
2054        /// # fn main() { test().unwrap(); }
2055        /// # fn test() -> Option<()> {
2056        #[doc = concat!("let pos = NonZero::new(1", stringify!($Int), ")?;")]
2057        #[doc = concat!("let neg = NonZero::new(-1", stringify!($Int), ")?;")]
2058        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2059        ///
2060        /// assert_eq!(Some(pos), neg.checked_abs());
2061        /// assert_eq!(None, min.checked_abs());
2062        /// # Some(())
2063        /// # }
2064        /// ```
2065        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2066        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2067        #[must_use = "this returns the result of the operation, \
2068                      without modifying the original"]
2069        #[inline]
2070        pub const fn checked_abs(self) -> Option<Self> {
2071            if let Some(nz) = self.get().checked_abs() {
2072                // SAFETY: absolute value of nonzero cannot yield zero values.
2073                Some(unsafe { Self::new_unchecked(nz) })
2074            } else {
2075                None
2076            }
2077        }
2078
2079        /// Computes the absolute value of self,
2080        /// with overflow information, see
2081        #[doc = concat!("[`", stringify!($Int), "::overflowing_abs`].")]
2082        ///
2083        /// # Example
2084        ///
2085        /// ```
2086        /// # use std::num::NonZero;
2087        /// #
2088        /// # fn main() { test().unwrap(); }
2089        /// # fn test() -> Option<()> {
2090        #[doc = concat!("let pos = NonZero::new(1", stringify!($Int), ")?;")]
2091        #[doc = concat!("let neg = NonZero::new(-1", stringify!($Int), ")?;")]
2092        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2093        ///
2094        /// assert_eq!((pos, false), pos.overflowing_abs());
2095        /// assert_eq!((pos, false), neg.overflowing_abs());
2096        /// assert_eq!((min, true), min.overflowing_abs());
2097        /// # Some(())
2098        /// # }
2099        /// ```
2100        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2101        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2102        #[must_use = "this returns the result of the operation, \
2103                      without modifying the original"]
2104        #[inline]
2105        pub const fn overflowing_abs(self) -> (Self, bool) {
2106            let (nz, flag) = self.get().overflowing_abs();
2107            (
2108                // SAFETY: absolute value of nonzero cannot yield zero values.
2109                unsafe { Self::new_unchecked(nz) },
2110                flag,
2111            )
2112        }
2113
2114        /// Saturating absolute value, see
2115        #[doc = concat!("[`", stringify!($Int), "::saturating_abs`].")]
2116        ///
2117        /// # Example
2118        ///
2119        /// ```
2120        /// # use std::num::NonZero;
2121        /// #
2122        /// # fn main() { test().unwrap(); }
2123        /// # fn test() -> Option<()> {
2124        #[doc = concat!("let pos = NonZero::new(1", stringify!($Int), ")?;")]
2125        #[doc = concat!("let neg = NonZero::new(-1", stringify!($Int), ")?;")]
2126        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2127        #[doc = concat!("let min_plus = NonZero::new(", stringify!($Int), "::MIN + 1)?;")]
2128        #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
2129        ///
2130        /// assert_eq!(pos, pos.saturating_abs());
2131        /// assert_eq!(pos, neg.saturating_abs());
2132        /// assert_eq!(max, min.saturating_abs());
2133        /// assert_eq!(max, min_plus.saturating_abs());
2134        /// # Some(())
2135        /// # }
2136        /// ```
2137        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2138        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2139        #[must_use = "this returns the result of the operation, \
2140                      without modifying the original"]
2141        #[inline]
2142        pub const fn saturating_abs(self) -> Self {
2143            // SAFETY: absolute value of nonzero cannot yield zero values.
2144            unsafe { Self::new_unchecked(self.get().saturating_abs()) }
2145        }
2146
2147        /// Wrapping absolute value, see
2148        #[doc = concat!("[`", stringify!($Int), "::wrapping_abs`].")]
2149        ///
2150        /// # Example
2151        ///
2152        /// ```
2153        /// # use std::num::NonZero;
2154        /// #
2155        /// # fn main() { test().unwrap(); }
2156        /// # fn test() -> Option<()> {
2157        #[doc = concat!("let pos = NonZero::new(1", stringify!($Int), ")?;")]
2158        #[doc = concat!("let neg = NonZero::new(-1", stringify!($Int), ")?;")]
2159        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2160        #[doc = concat!("# let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
2161        ///
2162        /// assert_eq!(pos, pos.wrapping_abs());
2163        /// assert_eq!(pos, neg.wrapping_abs());
2164        /// assert_eq!(min, min.wrapping_abs());
2165        /// assert_eq!(max, (-max).wrapping_abs());
2166        /// # Some(())
2167        /// # }
2168        /// ```
2169        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2170        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2171        #[must_use = "this returns the result of the operation, \
2172                      without modifying the original"]
2173        #[inline]
2174        pub const fn wrapping_abs(self) -> Self {
2175            // SAFETY: absolute value of nonzero cannot yield zero values.
2176            unsafe { Self::new_unchecked(self.get().wrapping_abs()) }
2177        }
2178
2179        /// Computes the absolute value of self
2180        /// without any wrapping or panicking.
2181        ///
2182        /// # Example
2183        ///
2184        /// ```
2185        /// # use std::num::NonZero;
2186        /// #
2187        /// # fn main() { test().unwrap(); }
2188        /// # fn test() -> Option<()> {
2189        #[doc = concat!("let u_pos = NonZero::new(1", stringify!($Uint), ")?;")]
2190        #[doc = concat!("let i_pos = NonZero::new(1", stringify!($Int), ")?;")]
2191        #[doc = concat!("let i_neg = NonZero::new(-1", stringify!($Int), ")?;")]
2192        #[doc = concat!("let i_min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2193        #[doc = concat!("let u_max = NonZero::new(", stringify!($Uint), "::MAX / 2 + 1)?;")]
2194        ///
2195        /// assert_eq!(u_pos, i_pos.unsigned_abs());
2196        /// assert_eq!(u_pos, i_neg.unsigned_abs());
2197        /// assert_eq!(u_max, i_min.unsigned_abs());
2198        /// # Some(())
2199        /// # }
2200        /// ```
2201        #[stable(feature = "nonzero_checked_ops", since = "1.64.0")]
2202        #[rustc_const_stable(feature = "const_nonzero_checked_ops", since = "1.64.0")]
2203        #[must_use = "this returns the result of the operation, \
2204                      without modifying the original"]
2205        #[inline]
2206        pub const fn unsigned_abs(self) -> NonZero<$Uint> {
2207            // SAFETY: absolute value of nonzero cannot yield zero values.
2208            unsafe { NonZero::new_unchecked(self.get().unsigned_abs()) }
2209        }
2210
2211        /// Returns `true` if `self` is positive and `false` if the
2212        /// number is negative.
2213        ///
2214        /// # Example
2215        ///
2216        /// ```
2217        /// # use std::num::NonZero;
2218        /// #
2219        /// # fn main() { test().unwrap(); }
2220        /// # fn test() -> Option<()> {
2221        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2222        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2223        ///
2224        /// assert!(pos_five.is_positive());
2225        /// assert!(!neg_five.is_positive());
2226        /// # Some(())
2227        /// # }
2228        /// ```
2229        #[must_use]
2230        #[inline]
2231        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2232        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2233        pub const fn is_positive(self) -> bool {
2234            self.get().is_positive()
2235        }
2236
2237        /// Returns `true` if `self` is negative and `false` if the
2238        /// number is positive.
2239        ///
2240        /// # Example
2241        ///
2242        /// ```
2243        /// # use std::num::NonZero;
2244        /// #
2245        /// # fn main() { test().unwrap(); }
2246        /// # fn test() -> Option<()> {
2247        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2248        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2249        ///
2250        /// assert!(neg_five.is_negative());
2251        /// assert!(!pos_five.is_negative());
2252        /// # Some(())
2253        /// # }
2254        /// ```
2255        #[must_use]
2256        #[inline]
2257        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2258        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2259        pub const fn is_negative(self) -> bool {
2260            self.get().is_negative()
2261        }
2262
2263        /// Checked negation. Computes `-self`,
2264        #[doc = concat!("returning `None` if `self == NonZero::<", stringify!($Int), ">::MIN`.")]
2265        ///
2266        /// # Example
2267        ///
2268        /// ```
2269        /// # use std::num::NonZero;
2270        /// #
2271        /// # fn main() { test().unwrap(); }
2272        /// # fn test() -> Option<()> {
2273        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2274        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2275        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2276        ///
2277        /// assert_eq!(pos_five.checked_neg(), Some(neg_five));
2278        /// assert_eq!(min.checked_neg(), None);
2279        /// # Some(())
2280        /// # }
2281        /// ```
2282        #[inline]
2283        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2284        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2285        pub const fn checked_neg(self) -> Option<Self> {
2286            if let Some(result) = self.get().checked_neg() {
2287                // SAFETY: negation of nonzero cannot yield zero values.
2288                return Some(unsafe { Self::new_unchecked(result) });
2289            }
2290            None
2291        }
2292
2293        /// Negates self, overflowing if this is equal to the minimum value.
2294        ///
2295        #[doc = concat!("See [`", stringify!($Int), "::overflowing_neg`]")]
2296        /// for documentation on overflow behavior.
2297        ///
2298        /// # Example
2299        ///
2300        /// ```
2301        /// # use std::num::NonZero;
2302        /// #
2303        /// # fn main() { test().unwrap(); }
2304        /// # fn test() -> Option<()> {
2305        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2306        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2307        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2308        ///
2309        /// assert_eq!(pos_five.overflowing_neg(), (neg_five, false));
2310        /// assert_eq!(min.overflowing_neg(), (min, true));
2311        /// # Some(())
2312        /// # }
2313        /// ```
2314        #[inline]
2315        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2316        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2317        pub const fn overflowing_neg(self) -> (Self, bool) {
2318            let (result, overflow) = self.get().overflowing_neg();
2319            // SAFETY: negation of nonzero cannot yield zero values.
2320            ((unsafe { Self::new_unchecked(result) }), overflow)
2321        }
2322
2323        /// Saturating negation. Computes `-self`,
2324        #[doc = concat!("returning [`NonZero::<", stringify!($Int), ">::MAX`]")]
2325        #[doc = concat!("if `self == NonZero::<", stringify!($Int), ">::MIN`")]
2326        /// instead of overflowing.
2327        ///
2328        /// # Example
2329        ///
2330        /// ```
2331        /// # use std::num::NonZero;
2332        /// #
2333        /// # fn main() { test().unwrap(); }
2334        /// # fn test() -> Option<()> {
2335        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2336        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2337        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2338        #[doc = concat!("let min_plus_one = NonZero::new(", stringify!($Int), "::MIN + 1)?;")]
2339        #[doc = concat!("let max = NonZero::new(", stringify!($Int), "::MAX)?;")]
2340        ///
2341        /// assert_eq!(pos_five.saturating_neg(), neg_five);
2342        /// assert_eq!(min.saturating_neg(), max);
2343        /// assert_eq!(max.saturating_neg(), min_plus_one);
2344        /// # Some(())
2345        /// # }
2346        /// ```
2347        #[inline]
2348        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2349        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2350        pub const fn saturating_neg(self) -> Self {
2351            if let Some(result) = self.checked_neg() {
2352                return result;
2353            }
2354            Self::MAX
2355        }
2356
2357        /// Wrapping (modular) negation. Computes `-self`, wrapping around at the boundary
2358        /// of the type.
2359        ///
2360        #[doc = concat!("See [`", stringify!($Int), "::wrapping_neg`]")]
2361        /// for documentation on overflow behavior.
2362        ///
2363        /// # Example
2364        ///
2365        /// ```
2366        /// # use std::num::NonZero;
2367        /// #
2368        /// # fn main() { test().unwrap(); }
2369        /// # fn test() -> Option<()> {
2370        #[doc = concat!("let pos_five = NonZero::new(5", stringify!($Int), ")?;")]
2371        #[doc = concat!("let neg_five = NonZero::new(-5", stringify!($Int), ")?;")]
2372        #[doc = concat!("let min = NonZero::new(", stringify!($Int), "::MIN)?;")]
2373        ///
2374        /// assert_eq!(pos_five.wrapping_neg(), neg_five);
2375        /// assert_eq!(min.wrapping_neg(), min);
2376        /// # Some(())
2377        /// # }
2378        /// ```
2379        #[inline]
2380        #[stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2381        #[rustc_const_stable(feature = "nonzero_negation_ops", since = "1.71.0")]
2382        pub const fn wrapping_neg(self) -> Self {
2383            let result = self.get().wrapping_neg();
2384            // SAFETY: negation of nonzero cannot yield zero values.
2385            unsafe { Self::new_unchecked(result) }
2386        }
2387
2388        /// Returns the bit pattern of `self` reinterpreted as an unsigned integer of the same size.
2389        ///
2390        /// # Examples
2391        ///
2392        /// ```
2393        /// # use std::num::NonZero;
2394        ///
2395        #[doc = concat!("let n = NonZero::new(-1", stringify!($Int), ").unwrap();")]
2396        ///
2397        #[doc = concat!("assert_eq!(n.cast_unsigned(), NonZero::<", stringify!($Uint), ">::MAX);")]
2398        /// ```
2399        #[stable(feature = "integer_sign_cast", since = "1.87.0")]
2400        #[rustc_const_stable(feature = "integer_sign_cast", since = "1.87.0")]
2401        #[must_use = "this returns the result of the operation, \
2402                      without modifying the original"]
2403        #[inline(always)]
2404        pub const fn cast_unsigned(self) -> NonZero<$Uint> {
2405            // SAFETY: `self.get()` can't be zero
2406            unsafe { NonZero::new_unchecked(self.get().cast_unsigned()) }
2407        }
2408
2409    };
2410}
2411
2412nonzero_integer! {
2413    Self = NonZeroU8,
2414    Primitive = unsigned u8,
2415    SignedPrimitive = i8,
2416    rot = 2,
2417    rot_op = "0x82",
2418    rot_result = "0xa",
2419    swap_op = "0x12",
2420    swapped = "0x12",
2421    reversed = "0x48",
2422}
2423
2424nonzero_integer! {
2425    Self = NonZeroU16,
2426    Primitive = unsigned u16,
2427    SignedPrimitive = i16,
2428    rot = 4,
2429    rot_op = "0xa003",
2430    rot_result = "0x3a",
2431    swap_op = "0x1234",
2432    swapped = "0x3412",
2433    reversed = "0x2c48",
2434}
2435
2436nonzero_integer! {
2437    Self = NonZeroU32,
2438    Primitive = unsigned u32,
2439    SignedPrimitive = i32,
2440    rot = 8,
2441    rot_op = "0x10000b3",
2442    rot_result = "0xb301",
2443    swap_op = "0x12345678",
2444    swapped = "0x78563412",
2445    reversed = "0x1e6a2c48",
2446}
2447
2448nonzero_integer! {
2449    Self = NonZeroU64,
2450    Primitive = unsigned u64,
2451    SignedPrimitive = i64,
2452    rot = 12,
2453    rot_op = "0xaa00000000006e1",
2454    rot_result = "0x6e10aa",
2455    swap_op = "0x1234567890123456",
2456    swapped = "0x5634129078563412",
2457    reversed = "0x6a2c48091e6a2c48",
2458}
2459
2460nonzero_integer! {
2461    Self = NonZeroU128,
2462    Primitive = unsigned u128,
2463    SignedPrimitive = i128,
2464    rot = 16,
2465    rot_op = "0x13f40000000000000000000000004f76",
2466    rot_result = "0x4f7613f4",
2467    swap_op = "0x12345678901234567890123456789012",
2468    swapped = "0x12907856341290785634129078563412",
2469    reversed = "0x48091e6a2c48091e6a2c48091e6a2c48",
2470}
2471
2472#[cfg(target_pointer_width = "16")]
2473nonzero_integer! {
2474    Self = NonZeroUsize,
2475    Primitive = unsigned usize,
2476    SignedPrimitive = isize,
2477    rot = 4,
2478    rot_op = "0xa003",
2479    rot_result = "0x3a",
2480    swap_op = "0x1234",
2481    swapped = "0x3412",
2482    reversed = "0x2c48",
2483}
2484
2485#[cfg(target_pointer_width = "32")]
2486nonzero_integer! {
2487    Self = NonZeroUsize,
2488    Primitive = unsigned usize,
2489    SignedPrimitive = isize,
2490    rot = 8,
2491    rot_op = "0x10000b3",
2492    rot_result = "0xb301",
2493    swap_op = "0x12345678",
2494    swapped = "0x78563412",
2495    reversed = "0x1e6a2c48",
2496}
2497
2498#[cfg(target_pointer_width = "64")]
2499nonzero_integer! {
2500    Self = NonZeroUsize,
2501    Primitive = unsigned usize,
2502    SignedPrimitive = isize,
2503    rot = 12,
2504    rot_op = "0xaa00000000006e1",
2505    rot_result = "0x6e10aa",
2506    swap_op = "0x1234567890123456",
2507    swapped = "0x5634129078563412",
2508    reversed = "0x6a2c48091e6a2c48",
2509}
2510
2511nonzero_integer! {
2512    Self = NonZeroI8,
2513    Primitive = signed i8,
2514    UnsignedPrimitive = u8,
2515    rot = 2,
2516    rot_op = "-0x7e",
2517    rot_result = "0xa",
2518    swap_op = "0x12",
2519    swapped = "0x12",
2520    reversed = "0x48",
2521}
2522
2523nonzero_integer! {
2524    Self = NonZeroI16,
2525    Primitive = signed i16,
2526    UnsignedPrimitive = u16,
2527    rot = 4,
2528    rot_op = "-0x5ffd",
2529    rot_result = "0x3a",
2530    swap_op = "0x1234",
2531    swapped = "0x3412",
2532    reversed = "0x2c48",
2533}
2534
2535nonzero_integer! {
2536    Self = NonZeroI32,
2537    Primitive = signed i32,
2538    UnsignedPrimitive = u32,
2539    rot = 8,
2540    rot_op = "0x10000b3",
2541    rot_result = "0xb301",
2542    swap_op = "0x12345678",
2543    swapped = "0x78563412",
2544    reversed = "0x1e6a2c48",
2545}
2546
2547nonzero_integer! {
2548    Self = NonZeroI64,
2549    Primitive = signed i64,
2550    UnsignedPrimitive = u64,
2551    rot = 12,
2552    rot_op = "0xaa00000000006e1",
2553    rot_result = "0x6e10aa",
2554    swap_op = "0x1234567890123456",
2555    swapped = "0x5634129078563412",
2556    reversed = "0x6a2c48091e6a2c48",
2557}
2558
2559nonzero_integer! {
2560    Self = NonZeroI128,
2561    Primitive = signed i128,
2562    UnsignedPrimitive = u128,
2563    rot = 16,
2564    rot_op = "0x13f40000000000000000000000004f76",
2565    rot_result = "0x4f7613f4",
2566    swap_op = "0x12345678901234567890123456789012",
2567    swapped = "0x12907856341290785634129078563412",
2568    reversed = "0x48091e6a2c48091e6a2c48091e6a2c48",
2569}
2570
2571#[cfg(target_pointer_width = "16")]
2572nonzero_integer! {
2573    Self = NonZeroIsize,
2574    Primitive = signed isize,
2575    UnsignedPrimitive = usize,
2576    rot = 4,
2577    rot_op = "-0x5ffd",
2578    rot_result = "0x3a",
2579    swap_op = "0x1234",
2580    swapped = "0x3412",
2581    reversed = "0x2c48",
2582}
2583
2584#[cfg(target_pointer_width = "32")]
2585nonzero_integer! {
2586    Self = NonZeroIsize,
2587    Primitive = signed isize,
2588    UnsignedPrimitive = usize,
2589    rot = 8,
2590    rot_op = "0x10000b3",
2591    rot_result = "0xb301",
2592    swap_op = "0x12345678",
2593    swapped = "0x78563412",
2594    reversed = "0x1e6a2c48",
2595}
2596
2597#[cfg(target_pointer_width = "64")]
2598nonzero_integer! {
2599    Self = NonZeroIsize,
2600    Primitive = signed isize,
2601    UnsignedPrimitive = usize,
2602    rot = 12,
2603    rot_op = "0xaa00000000006e1",
2604    rot_result = "0x6e10aa",
2605    swap_op = "0x1234567890123456",
2606    swapped = "0x5634129078563412",
2607    reversed = "0x6a2c48091e6a2c48",
2608}
````