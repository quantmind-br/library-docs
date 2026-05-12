---
title: marker.rs - source
url: https://doc.rust-lang.org/src/core/marker.rs.html#474-484
source: crawler
fetched_at: 2026-05-06T21:29:32.8543229-03:00
rendered_js: false
word_count: 6735
summary: This document defines fundamental Rust marker traits like Send, Sized, and Unsize, which classify types based on intrinsic properties such as thread-safety and memory layout requirements.
tags:
    - rust
    - marker-traits
    - concurrency
    - memory-layout
    - type-system
    - send
    - sized
category: reference
---

## core/ marker.rs

````rust
1//! Primitive traits and types representing basic properties of types.
2//!
3//! Rust types can be classified in various useful ways according to
4//! their intrinsic properties. These classifications are represented
5//! as traits.
6
7#![stable(feature = "rust1", since = "1.0.0")]
8
9mod variance;
10
11#[unstable(feature = "phantom_variance_markers", issue = "135806")]
12pub use self::variance::{
13    PhantomContravariant, PhantomContravariantLifetime, PhantomCovariant, PhantomCovariantLifetime,
14    PhantomInvariant, PhantomInvariantLifetime, Variance, variance,
15};
16use crate::cell::UnsafeCell;
17use crate::clone::TrivialClone;
18use crate::cmp;
19use crate::fmt::Debug;
20use crate::hash::{Hash, Hasher};
21use crate::pin::UnsafePinned;
22
23// NOTE: for consistent error messages between `core` and `minicore`, all `diagnostic` attributes
24// should be replicated exactly in `minicore` (if `minicore` defines the item).
25
26/// Implements a given marker trait for multiple types at the same time.
27///
28/// The basic syntax looks like this:
29/// ```ignore private macro
30/// marker_impls! { MarkerTrait for u8, i8 }
31/// ```
32/// You can also implement `unsafe` traits
33/// ```ignore private macro
34/// marker_impls! { unsafe MarkerTrait for u8, i8 }
35/// ```
36/// Add attributes to all impls:
37/// ```ignore private macro
38/// marker_impls! {
39///     #[allow(lint)]
40///     #[unstable(feature = "marker_trait", issue = "none")]
41///     MarkerTrait for u8, i8
42/// }
43/// ```
44/// And use generics:
45/// ```ignore private macro
46/// marker_impls! {
47///     MarkerTrait for
48///         u8, i8,
49///         {T: ?Sized} *const T,
50///         {T: ?Sized} *mut T,
51///         {T: MarkerTrait} PhantomData<T>,
52///         u32,
53/// }
54/// ```
55#[unstable(feature = "internal_impls_macro", issue = "none")]
56// Allow implementations of `UnsizedConstParamTy` even though std cannot use that feature.
57#[allow_internal_unstable(unsized_const_params)]
58macro marker_impls {
59    ( $(#[$($meta:tt)*])* $Trait:ident for $({$($bounds:tt)*})? $T:ty $(, $($rest:tt)*)? ) => {
60        $(#[$($meta)*])* impl< $($($bounds)*)? > $Trait for $T {}
61        marker_impls! { $(#[$($meta)*])* $Trait for $($($rest)*)? }
62    },
63    ( $(#[$($meta:tt)*])* $Trait:ident for ) => {},
64
65    ( $(#[$($meta:tt)*])* unsafe $Trait:ident for $({$($bounds:tt)*})? $T:ty $(, $($rest:tt)*)? ) => {
66        $(#[$($meta)*])* unsafe impl< $($($bounds)*)? > $Trait for $T {}
67        marker_impls! { $(#[$($meta)*])* unsafe $Trait for $($($rest)*)? }
68    },
69    ( $(#[$($meta:tt)*])* unsafe $Trait:ident for ) => {},
70}
71
72/// Types that can be transferred across thread boundaries.
73///
74/// This trait is automatically implemented when the compiler determines it's
75/// appropriate.
76///
77/// An example of a non-`Send` type is the reference-counting pointer
78/// [`rc::Rc`][`Rc`]. If two threads attempt to clone [`Rc`]s that point to the same
79/// reference-counted value, they might try to update the reference count at the
80/// same time, which is [undefined behavior][ub] because [`Rc`] doesn't use atomic
81/// operations. Its cousin [`sync::Arc`][arc] does use atomic operations (incurring
82/// some overhead) and thus is `Send`.
83///
84/// See [the Nomicon](../../nomicon/send-and-sync.html) and the [`Sync`] trait for more details.
85///
86/// [`Rc`]: ../../std/rc/struct.Rc.html
87/// [arc]: ../../std/sync/struct.Arc.html
88/// [ub]: ../../reference/behavior-considered-undefined.html
89#[stable(feature = "rust1", since = "1.0.0")]
90#[rustc_diagnostic_item = "Send"]
91#[diagnostic::on_unimplemented(
92    message = "`{Self}` cannot be sent between threads safely",
93    label = "`{Self}` cannot be sent between threads safely"
94)]
95pub unsafe auto trait Send {
96    // empty.
97}
98
99#[stable(feature = "rust1", since = "1.0.0")]
100impl<T: PointeeSized> !Send for *const T {}
101#[stable(feature = "rust1", since = "1.0.0")]
102impl<T: PointeeSized> !Send for *mut T {}
103
104// Most instances arise automatically, but this instance is needed to link up `T: Sync` with
105// `&T: Send` (and it also removes the unsound default instance `T Send` -> `&T: Send` that would
106// otherwise exist).
107#[stable(feature = "rust1", since = "1.0.0")]
108unsafe impl<T: Sync + PointeeSized> Send for &T {}
109
110/// Types with a constant size known at compile time.
111///
112/// All type parameters have an implicit bound of `Sized`. The special syntax
113/// `?Sized` can be used to remove this bound if it's not appropriate.
114///
115/// ```
116/// # #![allow(dead_code)]
117/// struct Foo<T>(T);
118/// struct Bar<T: ?Sized>(T);
119///
120/// // struct FooUse(Foo<[i32]>); // error: Sized is not implemented for [i32]
121/// struct BarUse(Bar<[i32]>); // OK
122/// ```
123///
124/// The one exception is the implicit `Self` type of a trait. A trait does not
125/// have an implicit `Sized` bound as this is incompatible with [trait object]s
126/// where, by definition, the trait needs to work with all possible implementors,
127/// and thus could be any size.
128///
129/// Although Rust will let you bind `Sized` to a trait, you won't
130/// be able to use it to form a trait object later:
131///
132/// ```
133/// # #![allow(unused_variables)]
134/// trait Foo { }
135/// trait Bar: Sized { }
136///
137/// struct Impl;
138/// impl Foo for Impl { }
139/// impl Bar for Impl { }
140///
141/// let x: &dyn Foo = &Impl;    // OK
142/// // let y: &dyn Bar = &Impl; // error: the trait `Bar` cannot be made into an object
143/// ```
144///
145/// [trait object]: ../../book/ch17-02-trait-objects.html
146#[doc(alias = "?", alias = "?Sized")]
147#[stable(feature = "rust1", since = "1.0.0")]
148#[lang = "sized"]
149#[diagnostic::on_unimplemented(
150    message = "the size for values of type `{Self}` cannot be known at compilation time",
151    label = "doesn't have a size known at compile-time"
152)]
153#[fundamental] // for Default, for example, which requires that `[T]: !Default` be evaluatable
154#[rustc_specialization_trait]
155#[rustc_deny_explicit_impl]
156#[rustc_dyn_incompatible_trait]
157// `Sized` being coinductive, despite having supertraits, is okay as there are no user-written impls,
158// and we know that the supertraits are always implemented if the subtrait is just by looking at
159// the builtin impls.
160#[rustc_coinductive]
161pub trait Sized: MetaSized {
162    // Empty.
163}
164
165/// Types with a size that can be determined from pointer metadata.
166#[unstable(feature = "sized_hierarchy", issue = "144404")]
167#[lang = "meta_sized"]
168#[diagnostic::on_unimplemented(
169    message = "the size for values of type `{Self}` cannot be known",
170    label = "doesn't have a known size"
171)]
172#[fundamental]
173#[rustc_specialization_trait]
174#[rustc_deny_explicit_impl]
175// `MetaSized` being coinductive, despite having supertraits, is okay for the same reasons as
176// `Sized` above.
177#[rustc_coinductive]
178pub trait MetaSized: PointeeSized {
179    // Empty
180}
181
182/// Types that may or may not have a size.
183#[unstable(feature = "sized_hierarchy", issue = "144404")]
184#[lang = "pointee_sized"]
185#[diagnostic::on_unimplemented(
186    message = "values of type `{Self}` may or may not have a size",
187    label = "may or may not have a known size"
188)]
189#[fundamental]
190#[rustc_specialization_trait]
191#[rustc_deny_explicit_impl]
192#[rustc_coinductive]
193pub trait PointeeSized {
194    // Empty
195}
196
197/// Types that can be "unsized" to a dynamically-sized type.
198///
199/// For example, the sized array type `[i8; 2]` implements `Unsize<[i8]>` and
200/// `Unsize<dyn fmt::Debug>`.
201///
202/// All implementations of `Unsize` are provided automatically by the compiler.
203/// Those implementations are:
204///
205/// - Arrays `[T; N]` implement `Unsize<[T]>`.
206/// - A type implements `Unsize<dyn Trait + 'a>` if all of these conditions are met:
207///   - The type implements `Trait`.
208///   - `Trait` is dyn-compatible[^1].
209///   - The type is sized.
210///   - The type outlives `'a`.
211/// - Trait objects `dyn TraitA + AutoA... + 'a` implement `Unsize<dyn TraitB + AutoB... + 'b>`
212///    if all of these conditions are met:
213///   - `TraitB` is a supertrait of `TraitA`.
214///   - `AutoB...` is a subset of `AutoA...`.
215///   - `'a` outlives `'b`.
216/// - Structs `Foo<..., T1, ..., Tn, ...>` implement `Unsize<Foo<..., U1, ..., Un, ...>>`
217///   where any number of (type and const) parameters may be changed if all of these conditions
218///   are met:
219///   - Only the last field of `Foo` has a type involving the parameters `T1`, ..., `Tn`.
220///   - All other parameters of the struct are equal.
221///   - `Field<T1, ..., Tn>: Unsize<Field<U1, ..., Un>>`, where `Field<...>` stands for the actual
222///     type of the struct's last field.
223///
224/// `Unsize` is used along with [`ops::CoerceUnsized`] to allow
225/// "user-defined" containers such as [`Rc`] to contain dynamically-sized
226/// types. See the [DST coercion RFC][RFC982] and [the nomicon entry on coercion][nomicon-coerce]
227/// for more details.
228///
229/// [`ops::CoerceUnsized`]: crate::ops::CoerceUnsized
230/// [`Rc`]: ../../std/rc/struct.Rc.html
231/// [RFC982]: https://github.com/rust-lang/rfcs/blob/master/text/0982-dst-coercion.md
232/// [nomicon-coerce]: ../../nomicon/coercions.html
233/// [^1]: Formerly known as *object safe*.
234#[unstable(feature = "unsize", issue = "18598")]
235#[lang = "unsize"]
236#[rustc_deny_explicit_impl]
237#[rustc_dyn_incompatible_trait]
238pub trait Unsize<T: PointeeSized>: PointeeSized {
239    // Empty.
240}
241
242/// Required trait for constants used in pattern matches.
243///
244/// Constants are only allowed as patterns if (a) their type implements
245/// `PartialEq`, and (b) interpreting the value of the constant as a pattern
246/// is equivalent to calling `PartialEq`. This ensures that constants used as
247/// patterns cannot expose implementation details in an unexpected way or
248/// cause semver hazards.
249///
250/// This trait ensures point (b).
251/// Any type that derives `PartialEq` automatically implements this trait.
252///
253/// Implementing this trait (which is unstable) is a way for type authors to explicitly allow
254/// comparing const values of this type; that operation will recursively compare all fields
255/// (including private fields), even if that behavior differs from `PartialEq`. This can make it
256/// semver-breaking to add further private fields to a type.
257#[unstable(feature = "structural_match", issue = "31434")]
258#[diagnostic::on_unimplemented(message = "the type `{Self}` does not `#[derive(PartialEq)]`")]
259#[lang = "structural_peq"]
260pub trait StructuralPartialEq {
261    // Empty.
262}
263
264marker_impls! {
265    #[unstable(feature = "structural_match", issue = "31434")]
266    StructuralPartialEq for
267        usize, u8, u16, u32, u64, u128,
268        isize, i8, i16, i32, i64, i128,
269        bool,
270        char,
271        str /* Technically requires `[u8]: StructuralPartialEq` */,
272        (),
273        {T, const N: usize} [T; N],
274        {T} [T],
275        {T: PointeeSized} &T,
276}
277
278/// Types whose values can be duplicated simply by copying bits.
279///
280/// By default, variable bindings have 'move semantics.' In other
281/// words:
282///
283/// ```
284/// #[derive(Debug)]
285/// struct Foo;
286///
287/// let x = Foo;
288///
289/// let y = x;
290///
291/// // `x` has moved into `y`, and so cannot be used
292///
293/// // println!("{x:?}"); // error: use of moved value
294/// ```
295///
296/// However, if a type implements `Copy`, it instead has 'copy semantics':
297///
298/// ```
299/// // We can derive a `Copy` implementation. `Clone` is also required, as it's
300/// // a supertrait of `Copy`.
301/// #[derive(Debug, Copy, Clone)]
302/// struct Foo;
303///
304/// let x = Foo;
305///
306/// let y = x;
307///
308/// // `y` is a copy of `x`
309///
310/// println!("{x:?}"); // A-OK!
311/// ```
312///
313/// It's important to note that in these two examples, the only difference is whether you
314/// are allowed to access `x` after the assignment. Under the hood, both a copy and a move
315/// can result in bits being copied in memory, although this is sometimes optimized away.
316///
317/// ## How can I implement `Copy`?
318///
319/// There are two ways to implement `Copy` on your type. The simplest is to use `derive`:
320///
321/// ```
322/// #[derive(Copy, Clone)]
323/// struct MyStruct;
324/// ```
325///
326/// You can also implement `Copy` and `Clone` manually:
327///
328/// ```
329/// struct MyStruct;
330///
331/// impl Copy for MyStruct { }
332///
333/// impl Clone for MyStruct {
334///     fn clone(&self) -> MyStruct {
335///         *self
336///     }
337/// }
338/// ```
339///
340/// There is a small difference between the two. The `derive` strategy will also place a `Copy`
341/// bound on type parameters:
342///
343/// ```
344/// #[derive(Clone)]
345/// struct MyStruct<T>(T);
346///
347/// impl<T: Copy> Copy for MyStruct<T> { }
348/// ```
349///
350/// This isn't always desired. For example, shared references (`&T`) can be copied regardless of
351/// whether `T` is `Copy`. Likewise, a generic struct containing markers such as [`PhantomData`]
352/// could potentially be duplicated with a bit-wise copy.
353///
354/// ## What's the difference between `Copy` and `Clone`?
355///
356/// Copies happen implicitly, for example as part of an assignment `y = x`. The behavior of
357/// `Copy` is not overloadable; it is always a simple bit-wise copy.
358///
359/// Cloning is an explicit action, `x.clone()`. The implementation of [`Clone`] can
360/// provide any type-specific behavior necessary to duplicate values safely. For example,
361/// the implementation of [`Clone`] for [`String`] needs to copy the pointed-to string
362/// buffer in the heap. A simple bitwise copy of [`String`] values would merely copy the
363/// pointer, leading to a double free down the line. For this reason, [`String`] is [`Clone`]
364/// but not `Copy`.
365///
366/// [`Clone`] is a supertrait of `Copy`, so everything which is `Copy` must also implement
367/// [`Clone`]. If a type is `Copy` then its [`Clone`] implementation only needs to return `*self`
368/// (see the example above).
369///
370/// ## When can my type be `Copy`?
371///
372/// A type can implement `Copy` if all of its components implement `Copy`. For example, this
373/// struct can be `Copy`:
374///
375/// ```
376/// # #[allow(dead_code)]
377/// #[derive(Copy, Clone)]
378/// struct Point {
379///    x: i32,
380///    y: i32,
381/// }
382/// ```
383///
384/// A struct can be `Copy`, and [`i32`] is `Copy`, therefore `Point` is eligible to be `Copy`.
385/// By contrast, consider
386///
387/// ```
388/// # #![allow(dead_code)]
389/// # struct Point;
390/// struct PointList {
391///     points: Vec<Point>,
392/// }
393/// ```
394///
395/// The struct `PointList` cannot implement `Copy`, because [`Vec<T>`] is not `Copy`. If we
396/// attempt to derive a `Copy` implementation, we'll get an error:
397///
398/// ```text
399/// the trait `Copy` cannot be implemented for this type; field `points` does not implement `Copy`
400/// ```
401///
402/// Shared references (`&T`) are also `Copy`, so a type can be `Copy`, even when it holds
403/// shared references of types `T` that are *not* `Copy`. Consider the following struct,
404/// which can implement `Copy`, because it only holds a *shared reference* to our non-`Copy`
405/// type `PointList` from above:
406///
407/// ```
408/// # #![allow(dead_code)]
409/// # struct PointList;
410/// #[derive(Copy, Clone)]
411/// struct PointListWrapper<'a> {
412///     point_list_ref: &'a PointList,
413/// }
414/// ```
415///
416/// ## When *can't* my type be `Copy`?
417///
418/// Some types can't be copied safely. For example, copying `&mut T` would create an aliased
419/// mutable reference. Copying [`String`] would duplicate responsibility for managing the
420/// [`String`]'s buffer, leading to a double free.
421///
422/// Generalizing the latter case, any type implementing [`Drop`] can't be `Copy`, because it's
423/// managing some resource besides its own [`size_of::<T>`] bytes.
424///
425/// If you try to implement `Copy` on a struct or enum containing non-`Copy` data, you will get
426/// the error [E0204].
427///
428/// [E0204]: ../../error_codes/E0204.html
429///
430/// ## When *should* my type be `Copy`?
431///
432/// Generally speaking, if your type _can_ implement `Copy`, it should. Keep in mind, though,
433/// that implementing `Copy` is part of the public API of your type. If the type might become
434/// non-`Copy` in the future, it could be prudent to omit the `Copy` implementation now, to
435/// avoid a breaking API change.
436///
437/// ## Additional implementors
438///
439/// In addition to the [implementors listed below][impls],
440/// the following types also implement `Copy`:
441///
442/// * Function item types (i.e., the distinct types defined for each function)
443/// * Function pointer types (e.g., `fn() -> i32`)
444/// * Closure types, if they capture no value from the environment
445///   or if all such captured values implement `Copy` themselves.
446///   Note that variables captured by shared reference always implement `Copy`
447///   (even if the referent doesn't),
448///   while variables captured by mutable reference never implement `Copy`.
449///
450/// [`Vec<T>`]: ../../std/vec/struct.Vec.html
451/// [`String`]: ../../std/string/struct.String.html
452/// [`size_of::<T>`]: size_of
453/// [impls]: #implementors
454#[stable(feature = "rust1", since = "1.0.0")]
455#[lang = "copy"]
456#[rustc_diagnostic_item = "Copy"]
457pub trait Copy: Clone {
458    // Empty.
459}
460
461/// Derive macro generating an impl of the trait `Copy`.
462#[rustc_builtin_macro]
463#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
464#[allow_internal_unstable(core_intrinsics, derive_clone_copy_internals)]
465pub macro Copy($item:item) {
466    /* compiler built-in */
467}
468
469// Implementations of `Copy` for primitive types.
470//
471// Implementations that cannot be described in Rust
472// are implemented in `traits::SelectionContext::copy_clone_conditions()`
473// in `rustc_trait_selection`.
474marker_impls! {
475    #[stable(feature = "rust1", since = "1.0.0")]
476    Copy for
477        usize, u8, u16, u32, u64, u128,
478        isize, i8, i16, i32, i64, i128,
479        f16, f32, f64, f128,
480        bool, char,
481        {T: PointeeSized} *const T,
482        {T: PointeeSized} *mut T,
483
484}
485
486#[unstable(feature = "never_type", issue = "35121")]
487impl Copy for ! {}
488
489/// Shared references can be copied, but mutable references *cannot*!
490#[stable(feature = "rust1", since = "1.0.0")]
491impl<T: PointeeSized> Copy for &T {}
492
493/// Marker trait for the types that are allowed in union fields and unsafe
494/// binder types.
495///
496/// Implemented for:
497/// * `&T`, `&mut T` for all `T`,
498/// * `ManuallyDrop<T>` for all `T`,
499/// * tuples and arrays whose elements implement `BikeshedGuaranteedNoDrop`,
500/// * or otherwise, all types that are `Copy`.
501///
502/// Notably, this doesn't include all trivially-destructible types for semver
503/// reasons.
504///
505/// Bikeshed name for now. This trait does not do anything other than reflect the
506/// set of types that are allowed within unions for field validity.
507#[unstable(feature = "bikeshed_guaranteed_no_drop", issue = "none")]
508#[lang = "bikeshed_guaranteed_no_drop"]
509#[rustc_deny_explicit_impl]
510#[rustc_dyn_incompatible_trait]
511#[doc(hidden)]
512pub trait BikeshedGuaranteedNoDrop {}
513
514/// Types for which it is safe to share references between threads.
515///
516/// This trait is automatically implemented when the compiler determines
517/// it's appropriate.
518///
519/// The precise definition is: a type `T` is [`Sync`] if and only if `&T` is
520/// [`Send`]. In other words, if there is no possibility of
521/// [undefined behavior][ub] (including data races) when passing
522/// `&T` references between threads.
523///
524/// As one would expect, primitive types like [`u8`] and [`f64`]
525/// are all [`Sync`], and so are simple aggregate types containing them,
526/// like tuples, structs and enums. More examples of basic [`Sync`]
527/// types include "immutable" types like `&T`, and those with simple
528/// inherited mutability, such as [`Box<T>`][box], [`Vec<T>`][vec] and
529/// most other collection types. (Generic parameters need to be [`Sync`]
530/// for their container to be [`Sync`].)
531///
532/// A somewhat surprising consequence of the definition is that `&mut T`
533/// is `Sync` (if `T` is `Sync`) even though it seems like that might
534/// provide unsynchronized mutation. The trick is that a mutable
535/// reference behind a shared reference (that is, `& &mut T`)
536/// becomes read-only, as if it were a `& &T`. Hence there is no risk
537/// of a data race.
538///
539/// A shorter overview of how [`Sync`] and [`Send`] relate to referencing:
540/// * `&T` is [`Send`] if and only if `T` is [`Sync`]
541/// * `&mut T` is [`Send`] if and only if `T` is [`Send`]
542/// * `&T` and `&mut T` are [`Sync`] if and only if `T` is [`Sync`]
543///
544/// Types that are not `Sync` are those that have "interior
545/// mutability" in a non-thread-safe form, such as [`Cell`][cell]
546/// and [`RefCell`][refcell]. These types allow for mutation of
547/// their contents even through an immutable, shared reference. For
548/// example the `set` method on [`Cell<T>`][cell] takes `&self`, so it requires
549/// only a shared reference [`&Cell<T>`][cell]. The method performs no
550/// synchronization, thus [`Cell`][cell] cannot be `Sync`.
551///
552/// Another example of a non-`Sync` type is the reference-counting
553/// pointer [`Rc`][rc]. Given any reference [`&Rc<T>`][rc], you can clone
554/// a new [`Rc<T>`][rc], modifying the reference counts in a non-atomic way.
555///
556/// For cases when one does need thread-safe interior mutability,
557/// Rust provides [atomic data types], as well as explicit locking via
558/// [`sync::Mutex`][mutex] and [`sync::RwLock`][rwlock]. These types
559/// ensure that any mutation cannot cause data races, hence the types
560/// are `Sync`. Likewise, [`sync::Arc`][arc] provides a thread-safe
561/// analogue of [`Rc`][rc].
562///
563/// Any types with interior mutability must also use the
564/// [`cell::UnsafeCell`][unsafecell] wrapper around the value(s) which
565/// can be mutated through a shared reference. Failing to doing this is
566/// [undefined behavior][ub]. For example, [`transmute`][transmute]-ing
567/// from `&T` to `&mut T` is invalid.
568///
569/// See [the Nomicon][nomicon-send-and-sync] for more details about `Sync`.
570///
571/// [box]: ../../std/boxed/struct.Box.html
572/// [vec]: ../../std/vec/struct.Vec.html
573/// [cell]: crate::cell::Cell
574/// [refcell]: crate::cell::RefCell
575/// [rc]: ../../std/rc/struct.Rc.html
576/// [arc]: ../../std/sync/struct.Arc.html
577/// [atomic data types]: crate::sync::atomic
578/// [mutex]: ../../std/sync/struct.Mutex.html
579/// [rwlock]: ../../std/sync/struct.RwLock.html
580/// [unsafecell]: crate::cell::UnsafeCell
581/// [ub]: ../../reference/behavior-considered-undefined.html
582/// [transmute]: crate::mem::transmute
583/// [nomicon-send-and-sync]: ../../nomicon/send-and-sync.html
584#[stable(feature = "rust1", since = "1.0.0")]
585#[rustc_diagnostic_item = "Sync"]
586#[lang = "sync"]
587#[rustc_on_unimplemented(
588    on(
589        Self = "core::cell::once::OnceCell<T>",
590        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::OnceLock` instead"
591    ),
592    on(
593        Self = "core::cell::Cell<u8>",
594        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicU8` instead",
595    ),
596    on(
597        Self = "core::cell::Cell<u16>",
598        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicU16` instead",
599    ),
600    on(
601        Self = "core::cell::Cell<u32>",
602        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicU32` instead",
603    ),
604    on(
605        Self = "core::cell::Cell<u64>",
606        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicU64` instead",
607    ),
608    on(
609        Self = "core::cell::Cell<usize>",
610        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicUsize` instead",
611    ),
612    on(
613        Self = "core::cell::Cell<i8>",
614        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicI8` instead",
615    ),
616    on(
617        Self = "core::cell::Cell<i16>",
618        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicI16` instead",
619    ),
620    on(
621        Self = "core::cell::Cell<i32>",
622        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicI32` instead",
623    ),
624    on(
625        Self = "core::cell::Cell<i64>",
626        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicI64` instead",
627    ),
628    on(
629        Self = "core::cell::Cell<isize>",
630        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicIsize` instead",
631    ),
632    on(
633        Self = "core::cell::Cell<bool>",
634        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` or `std::sync::atomic::AtomicBool` instead",
635    ),
636    on(
637        all(
638            Self = "core::cell::Cell<T>",
639            not(Self = "core::cell::Cell<u8>"),
640            not(Self = "core::cell::Cell<u16>"),
641            not(Self = "core::cell::Cell<u32>"),
642            not(Self = "core::cell::Cell<u64>"),
643            not(Self = "core::cell::Cell<usize>"),
644            not(Self = "core::cell::Cell<i8>"),
645            not(Self = "core::cell::Cell<i16>"),
646            not(Self = "core::cell::Cell<i32>"),
647            not(Self = "core::cell::Cell<i64>"),
648            not(Self = "core::cell::Cell<isize>"),
649            not(Self = "core::cell::Cell<bool>")
650        ),
651        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock`",
652    ),
653    on(
654        Self = "core::cell::RefCell<T>",
655        note = "if you want to do aliasing and mutation between multiple threads, use `std::sync::RwLock` instead",
656    ),
657    message = "`{Self}` cannot be shared between threads safely",
658    label = "`{Self}` cannot be shared between threads safely"
659)]
660pub unsafe auto trait Sync {
661    // FIXME(estebank): once support to add notes in `rustc_on_unimplemented`
662    // lands in beta, and it has been extended to check whether a closure is
663    // anywhere in the requirement chain, extend it as such (#48534):
664    // ```
665    // on(
666    //     closure,
667    //     note="`{Self}` cannot be shared safely, consider marking the closure `move`"
668    // ),
669    // ```
670
671    // Empty
672}
673
674#[stable(feature = "rust1", since = "1.0.0")]
675impl<T: PointeeSized> !Sync for *const T {}
676#[stable(feature = "rust1", since = "1.0.0")]
677impl<T: PointeeSized> !Sync for *mut T {}
678
679/// Zero-sized type used to mark things that "act like" they own a `T`.
680///
681/// Adding a `PhantomData<T>` field to your type tells the compiler that your
682/// type acts as though it stores a value of type `T`, even though it doesn't
683/// really. This information is used when computing certain safety properties.
684///
685/// For a more in-depth explanation of how to use `PhantomData<T>`, please see
686/// [the Nomicon](../../nomicon/phantom-data.html).
687///
688/// # A ghastly note 👻👻👻
689///
690/// Though they both have scary names, `PhantomData` and 'phantom types' are
691/// related, but not identical. A phantom type parameter is simply a type
692/// parameter which is never used. In Rust, this often causes the compiler to
693/// complain, and the solution is to add a "dummy" use by way of `PhantomData`.
694///
695/// # Examples
696///
697/// ## Unused lifetime parameters
698///
699/// Perhaps the most common use case for `PhantomData` is a struct that has an
700/// unused lifetime parameter, typically as part of some unsafe code. For
701/// example, here is a struct `Slice` that has two pointers of type `*const T`,
702/// presumably pointing into an array somewhere:
703///
704/// ```compile_fail,E0392
705/// struct Slice<'a, T> {
706///     start: *const T,
707///     end: *const T,
708/// }
709/// ```
710///
711/// The intention is that the underlying data is only valid for the
712/// lifetime `'a`, so `Slice` should not outlive `'a`. However, this
713/// intent is not expressed in the code, since there are no uses of
714/// the lifetime `'a` and hence it is not clear what data it applies
715/// to. We can correct this by telling the compiler to act *as if* the
716/// `Slice` struct contained a reference `&'a T`:
717///
718/// ```
719/// use std::marker::PhantomData;
720///
721/// # #[allow(dead_code)]
722/// struct Slice<'a, T> {
723///     start: *const T,
724///     end: *const T,
725///     phantom: PhantomData<&'a T>,
726/// }
727/// ```
728///
729/// This also in turn infers the lifetime bound `T: 'a`, indicating
730/// that any references in `T` are valid over the lifetime `'a`.
731///
732/// When initializing a `Slice` you simply provide the value
733/// `PhantomData` for the field `phantom`:
734///
735/// ```
736/// # #![allow(dead_code)]
737/// # use std::marker::PhantomData;
738/// # struct Slice<'a, T> {
739/// #     start: *const T,
740/// #     end: *const T,
741/// #     phantom: PhantomData<&'a T>,
742/// # }
743/// fn borrow_vec<T>(vec: &Vec<T>) -> Slice<'_, T> {
744///     let ptr = vec.as_ptr();
745///     Slice {
746///         start: ptr,
747///         end: unsafe { ptr.add(vec.len()) },
748///         phantom: PhantomData,
749///     }
750/// }
751/// ```
752///
753/// ## Unused type parameters
754///
755/// It sometimes happens that you have unused type parameters which
756/// indicate what type of data a struct is "tied" to, even though that
757/// data is not actually found in the struct itself. Here is an
758/// example where this arises with [FFI]. The foreign interface uses
759/// handles of type `*mut ()` to refer to Rust values of different
760/// types. We track the Rust type using a phantom type parameter on
761/// the struct `ExternalResource` which wraps a handle.
762///
763/// [FFI]: ../../book/ch19-01-unsafe-rust.html#using-extern-functions-to-call-external-code
764///
765/// ```
766/// # #![allow(dead_code)]
767/// # trait ResType { }
768/// # struct ParamType;
769/// # mod foreign_lib {
770/// #     pub fn new(_: usize) -> *mut () { 42 as *mut () }
771/// #     pub fn do_stuff(_: *mut (), _: usize) {}
772/// # }
773/// # fn convert_params(_: ParamType) -> usize { 42 }
774/// use std::marker::PhantomData;
775///
776/// struct ExternalResource<R> {
777///    resource_handle: *mut (),
778///    resource_type: PhantomData<R>,
779/// }
780///
781/// impl<R: ResType> ExternalResource<R> {
782///     fn new() -> Self {
783///         let size_of_res = size_of::<R>();
784///         Self {
785///             resource_handle: foreign_lib::new(size_of_res),
786///             resource_type: PhantomData,
787///         }
788///     }
789///
790///     fn do_stuff(&self, param: ParamType) {
791///         let foreign_params = convert_params(param);
792///         foreign_lib::do_stuff(self.resource_handle, foreign_params);
793///     }
794/// }
795/// ```
796///
797/// ## Ownership and the drop check
798///
799/// The exact interaction of `PhantomData` with drop check **may change in the future**.
800///
801/// Currently, adding a field of type `PhantomData<T>` indicates that your type *owns* data of type
802/// `T` in very rare circumstances. This in turn has effects on the Rust compiler's [drop check]
803/// analysis. For the exact rules, see the [drop check] documentation.
804///
805/// ## Layout
806///
807/// For all `T`, the following are guaranteed:
808/// * `size_of::<PhantomData<T>>() == 0`
809/// * `align_of::<PhantomData<T>>() == 1`
810///
811/// [drop check]: Drop#drop-check
812#[lang = "phantom_data"]
813#[stable(feature = "rust1", since = "1.0.0")]
814pub struct PhantomData<T: PointeeSized>;
815
816#[stable(feature = "rust1", since = "1.0.0")]
817impl<T: PointeeSized> Hash for PhantomData<T> {
818    #[inline]
819    fn hash<H: Hasher>(&self, _: &mut H) {}
820}
821
822#[stable(feature = "rust1", since = "1.0.0")]
823impl<T: PointeeSized> cmp::PartialEq for PhantomData<T> {
824    fn eq(&self, _other: &PhantomData<T>) -> bool {
825        true
826    }
827}
828
829#[stable(feature = "rust1", since = "1.0.0")]
830impl<T: PointeeSized> cmp::Eq for PhantomData<T> {}
831
832#[stable(feature = "rust1", since = "1.0.0")]
833impl<T: PointeeSized> cmp::PartialOrd for PhantomData<T> {
834    fn partial_cmp(&self, _other: &PhantomData<T>) -> Option<cmp::Ordering> {
835        Option::Some(cmp::Ordering::Equal)
836    }
837}
838
839#[stable(feature = "rust1", since = "1.0.0")]
840impl<T: PointeeSized> cmp::Ord for PhantomData<T> {
841    fn cmp(&self, _other: &PhantomData<T>) -> cmp::Ordering {
842        cmp::Ordering::Equal
843    }
844}
845
846#[stable(feature = "rust1", since = "1.0.0")]
847impl<T: PointeeSized> Copy for PhantomData<T> {}
848
849#[stable(feature = "rust1", since = "1.0.0")]
850impl<T: PointeeSized> Clone for PhantomData<T> {
851    fn clone(&self) -> Self {
852        Self
853    }
854}
855
856#[doc(hidden)]
857#[unstable(feature = "trivial_clone", issue = "none")]
858unsafe impl<T: PointeeSized> TrivialClone for PhantomData<T> {}
859
860#[stable(feature = "rust1", since = "1.0.0")]
861#[rustc_const_unstable(feature = "const_default", issue = "143894")]
862impl<T: PointeeSized> const Default for PhantomData<T> {
863    fn default() -> Self {
864        Self
865    }
866}
867
868#[unstable(feature = "structural_match", issue = "31434")]
869impl<T: PointeeSized> StructuralPartialEq for PhantomData<T> {}
870
871/// Compiler-internal trait used to indicate the type of enum discriminants.
872///
873/// This trait is automatically implemented for every type and does not add any
874/// guarantees to [`mem::Discriminant`]. It is **undefined behavior** to transmute
875/// between `DiscriminantKind::Discriminant` and `mem::Discriminant`.
876///
877/// [`mem::Discriminant`]: crate::mem::Discriminant
878#[unstable(
879    feature = "discriminant_kind",
880    issue = "none",
881    reason = "this trait is unlikely to ever be stabilized, use `mem::discriminant` instead"
882)]
883#[lang = "discriminant_kind"]
884#[rustc_deny_explicit_impl]
885#[rustc_dyn_incompatible_trait]
886pub trait DiscriminantKind {
887    /// The type of the discriminant, which must satisfy the trait
888    /// bounds required by `mem::Discriminant`.
889    #[lang = "discriminant_type"]
890    type Discriminant: Clone + Copy + Debug + Eq + PartialEq + Hash + Send + Sync + Unpin;
891}
892
893/// Used to determine whether a type contains
894/// any `UnsafeCell` internally, but not through an indirection.
895/// This affects, for example, whether a `static` of that type is
896/// placed in read-only static memory or writable static memory.
897/// This can be used to declare that a constant with a generic type
898/// will not contain interior mutability, and subsequently allow
899/// placing the constant behind references.
900///
901/// # Safety
902///
903/// This trait is a core part of the language, it is just expressed as a trait in libcore for
904/// convenience. Do *not* implement it for other types.
905// FIXME: Eventually this trait should become `#[rustc_deny_explicit_impl]`.
906// That requires porting the impls below to native internal impls.
907#[lang = "freeze"]
908#[unstable(feature = "freeze", issue = "121675")]
909pub unsafe auto trait Freeze {}
910
911#[unstable(feature = "freeze", issue = "121675")]
912impl<T: PointeeSized> !Freeze for UnsafeCell<T> {}
913marker_impls! {
914    #[unstable(feature = "freeze", issue = "121675")]
915    unsafe Freeze for
916        {T: PointeeSized} PhantomData<T>,
917        {T: PointeeSized} *const T,
918        {T: PointeeSized} *mut T,
919        {T: PointeeSized} &T,
920        {T: PointeeSized} &mut T,
921}
922
923/// Used to determine whether a type contains any `UnsafePinned` (or `PhantomPinned`) internally,
924/// but not through an indirection. This affects, for example, whether we emit `noalias` metadata
925/// for `&mut T` or not.
926///
927/// This is part of [RFC 3467](https://rust-lang.github.io/rfcs/3467-unsafe-pinned.html), and is
928/// tracked by [#125735](https://github.com/rust-lang/rust/issues/125735).
929#[lang = "unsafe_unpin"]
930#[unstable(feature = "unsafe_unpin", issue = "125735")]
931pub unsafe auto trait UnsafeUnpin {}
932
933#[unstable(feature = "unsafe_unpin", issue = "125735")]
934impl<T: ?Sized> !UnsafeUnpin for UnsafePinned<T> {}
935marker_impls! {
936#[unstable(feature = "unsafe_unpin", issue = "125735")]
937    unsafe UnsafeUnpin for
938        {T: ?Sized} PhantomData<T>,
939        {T: ?Sized} *const T,
940        {T: ?Sized} *mut T,
941        {T: ?Sized} &T,
942        {T: ?Sized} &mut T,
943}
944
945/// Types that do not require any pinning guarantees.
946///
947/// For information on what "pinning" is, see the [`pin` module] documentation.
948///
949/// Implementing the `Unpin` trait for `T` expresses the fact that `T` is pinning-agnostic:
950/// it shall not expose nor rely on any pinning guarantees. This, in turn, means that a
951/// `Pin`-wrapped pointer to such a type can feature a *fully unrestricted* API.
952/// In other words, if `T: Unpin`, a value of type `T` will *not* be bound by the invariants
953/// which pinning otherwise offers, even when "pinned" by a [`Pin<Ptr>`] pointing at it.
954/// When a value of type `T` is pointed at by a [`Pin<Ptr>`], [`Pin`] will not restrict access
955/// to the pointee value like it normally would, thus allowing the user to do anything that they
956/// normally could with a non-[`Pin`]-wrapped `Ptr` to that value.
957///
958/// The idea of this trait is to alleviate the reduced ergonomics of APIs that require the use
959/// of [`Pin`] for soundness for some types, but which also want to be used by other types that
960/// don't care about pinning. The prime example of such an API is [`Future::poll`]. There are many
961/// [`Future`] types that don't care about pinning. These futures can implement `Unpin` and
962/// therefore get around the pinning related restrictions in the API, while still allowing the
963/// subset of [`Future`]s which *do* require pinning to be implemented soundly.
964///
965/// For more discussion on the consequences of [`Unpin`] within the wider scope of the pinning
966/// system, see the [section about `Unpin`] in the [`pin` module].
967///
968/// `Unpin` has no consequence at all for non-pinned data. In particular, [`mem::replace`] happily
969/// moves `!Unpin` data, which would be immovable when pinned ([`mem::replace`] works for any
970/// `&mut T`, not just when `T: Unpin`).
971///
972/// *However*, you cannot use [`mem::replace`] on `!Unpin` data which is *pinned* by being wrapped
973/// inside a [`Pin<Ptr>`] pointing at it. This is because you cannot (safely) use a
974/// [`Pin<Ptr>`] to get a `&mut T` to its pointee value, which you would need to call
975/// [`mem::replace`], and *that* is what makes this system work.
976///
977/// So this, for example, can only be done on types implementing `Unpin`:
978///
979/// ```rust
980/// # #![allow(unused_must_use)]
981/// use std::mem;
982/// use std::pin::Pin;
983///
984/// let mut string = "this".to_string();
985/// let mut pinned_string = Pin::new(&mut string);
986///
987/// // We need a mutable reference to call `mem::replace`.
988/// // We can obtain such a reference by (implicitly) invoking `Pin::deref_mut`,
989/// // but that is only possible because `String` implements `Unpin`.
990/// mem::replace(&mut *pinned_string, "other".to_string());
991/// ```
992///
993/// This trait is automatically implemented for almost every type. The compiler is free
994/// to take the conservative stance of marking types as [`Unpin`] so long as all of the types that
995/// compose its fields are also [`Unpin`]. This is because if a type implements [`Unpin`], then it
996/// is unsound for that type's implementation to rely on pinning-related guarantees for soundness,
997/// *even* when viewed through a "pinning" pointer! It is the responsibility of the implementor of
998/// a type that relies upon pinning for soundness to ensure that type is *not* marked as [`Unpin`]
999/// by adding [`PhantomPinned`] field. For more details, see the [`pin` module] docs.
1000///
1001/// [`mem::replace`]: crate::mem::replace "mem replace"
1002/// [`Future`]: crate::future::Future "Future"
1003/// [`Future::poll`]: crate::future::Future::poll "Future poll"
1004/// [`Pin`]: crate::pin::Pin "Pin"
1005/// [`Pin<Ptr>`]: crate::pin::Pin "Pin"
1006/// [`pin` module]: crate::pin "pin module"
1007/// [section about `Unpin`]: crate::pin#unpin "pin module docs about unpin"
1008/// [`unsafe`]: ../../std/keyword.unsafe.html "keyword unsafe"
1009#[stable(feature = "pin", since = "1.33.0")]
1010#[diagnostic::on_unimplemented(
1011    note = "consider using the `pin!` macro\nconsider using `Box::pin` if you need to access the pinned value outside of the current scope",
1012    message = "`{Self}` cannot be unpinned"
1013)]
1014#[lang = "unpin"]
1015pub auto trait Unpin {}
1016
1017/// A marker type which does not implement `Unpin`.
1018///
1019/// If a type contains a `PhantomPinned`, it will not implement `Unpin` by default.
1020//
1021// FIXME(unsafe_pinned): This is *not* a stable guarantee we want to make, at least not yet.
1022// Note that for backwards compatibility with the new [`UnsafePinned`] wrapper type, placing this
1023// marker in your struct acts as if you wrapped the entire struct in an `UnsafePinned`. This type
1024// will likely eventually be deprecated, and all new code should be using `UnsafePinned` instead.
1025#[stable(feature = "pin", since = "1.33.0")]
1026#[derive(Debug, Default, Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Hash)]
1027pub struct PhantomPinned;
1028
1029#[stable(feature = "pin", since = "1.33.0")]
1030impl !Unpin for PhantomPinned {}
1031
1032// This is a small hack to allow existing code which uses PhantomPinned to opt-out of noalias to
1033// continue working. Ideally PhantomPinned could just wrap an `UnsafePinned<()>` to get the same
1034// effect, but we can't add a new field to an already stable unit struct -- that would be a breaking
1035// change.
1036#[unstable(feature = "unsafe_unpin", issue = "125735")]
1037impl !UnsafeUnpin for PhantomPinned {}
1038
1039marker_impls! {
1040    #[stable(feature = "pin", since = "1.33.0")]
1041    Unpin for
1042        {T: PointeeSized} &T,
1043        {T: PointeeSized} &mut T,
1044}
1045
1046marker_impls! {
1047    #[stable(feature = "pin_raw", since = "1.38.0")]
1048    Unpin for
1049        {T: PointeeSized} *const T,
1050        {T: PointeeSized} *mut T,
1051}
1052
1053/// A marker for types that can be dropped.
1054///
1055/// This should be used for `[const]` bounds,
1056/// as non-const bounds will always hold for every type.
1057#[unstable(feature = "const_destruct", issue = "133214")]
1058#[rustc_const_unstable(feature = "const_destruct", issue = "133214")]
1059#[lang = "destruct"]
1060#[rustc_on_unimplemented(message = "can't drop `{Self}`", append_const_msg)]
1061#[rustc_deny_explicit_impl]
1062#[rustc_dyn_incompatible_trait]
1063pub const trait Destruct: PointeeSized {}
1064
1065/// A marker for tuple types.
1066///
1067/// The implementation of this trait is built-in and cannot be implemented
1068/// for any user type.
1069#[unstable(feature = "tuple_trait", issue = "none")]
1070#[lang = "tuple_trait"]
1071#[diagnostic::on_unimplemented(message = "`{Self}` is not a tuple")]
1072#[rustc_deny_explicit_impl]
1073#[rustc_dyn_incompatible_trait]
1074pub trait Tuple {}
1075
1076/// A marker for types which can be used as types of `const` generic parameters.
1077///
1078/// These types must have a proper equivalence relation (`Eq`) and it must be automatically
1079/// derived (`StructuralPartialEq`). There's a hard-coded check in the compiler ensuring
1080/// that all fields are also `ConstParamTy`, which implies that recursively, all fields
1081/// are `StructuralPartialEq`.
1082#[lang = "const_param_ty"]
1083#[unstable(feature = "unsized_const_params", issue = "95174")]
1084#[diagnostic::on_unimplemented(message = "`{Self}` can't be used as a const parameter type")]
1085#[allow(multiple_supertrait_upcastable)]
1086// We name this differently than the derive macro so that the `adt_const_params` can
1087// be used independently of `unsized_const_params` without requiring a full path
1088// to the derive macro every time it is used. This should be renamed on stabilization.
1089pub trait ConstParamTy_: StructuralPartialEq + Eq {}
1090
1091/// Derive macro generating an impl of the trait `ConstParamTy`.
1092#[rustc_builtin_macro]
1093#[allow_internal_unstable(unsized_const_params)]
1094#[unstable(feature = "adt_const_params", issue = "95174")]
1095pub macro ConstParamTy($item:item) {
1096    /* compiler built-in */
1097}
1098
1099// FIXME(adt_const_params): handle `ty::FnDef`/`ty::Closure`
1100marker_impls! {
1101    #[unstable(feature = "adt_const_params", issue = "95174")]
1102    ConstParamTy_ for
1103        usize, u8, u16, u32, u64, u128,
1104        isize, i8, i16, i32, i64, i128,
1105        bool,
1106        char,
1107        (),
1108        {T: ConstParamTy_, const N: usize} [T; N],
1109}
1110
1111marker_impls! {
1112    #[unstable(feature = "unsized_const_params", issue = "95174")]
1113    #[unstable_feature_bound(unsized_const_params)]
1114    ConstParamTy_ for
1115        str,
1116        {T: ConstParamTy_} [T],
1117        {T: ConstParamTy_ + ?Sized} &T,
1118}
1119
1120/// A common trait implemented by all function pointers.
1121//
1122// Note that while the trait is internal and unstable it is nevertheless
1123// exposed as a public bound of the stable `core::ptr::fn_addr_eq` function.
1124#[unstable(
1125    feature = "fn_ptr_trait",
1126    issue = "none",
1127    reason = "internal trait for implementing various traits for all function pointers"
1128)]
1129#[lang = "fn_ptr_trait"]
1130#[rustc_deny_explicit_impl]
1131#[rustc_dyn_incompatible_trait]
1132pub trait FnPtr: Copy + Clone {
1133    /// Returns the address of the function pointer.
1134    #[lang = "fn_ptr_addr"]
1135    fn addr(self) -> *const ();
1136}
1137
1138/// Derive macro that makes a smart pointer usable with trait objects.
1139///
1140/// # What this macro does
1141///
1142/// This macro is intended to be used with user-defined pointer types, and makes it possible to
1143/// perform coercions on the pointee of the user-defined pointer. There are two aspects to this:
1144///
1145/// ## Unsizing coercions of the pointee
1146///
1147/// By using the macro, the following example will compile:
1148/// ```
1149/// #![feature(derive_coerce_pointee)]
1150/// use std::marker::CoercePointee;
1151/// use std::ops::Deref;
1152///
1153/// #[derive(CoercePointee)]
1154/// #[repr(transparent)]
1155/// struct MySmartPointer<T: ?Sized>(Box<T>);
1156///
1157/// impl<T: ?Sized> Deref for MySmartPointer<T> {
1158///     type Target = T;
1159///     fn deref(&self) -> &T {
1160///         &self.0
1161///     }
1162/// }
1163///
1164/// trait MyTrait {}
1165///
1166/// impl MyTrait for i32 {}
1167///
1168/// fn main() {
1169///     let ptr: MySmartPointer<i32> = MySmartPointer(Box::new(4));
1170///
1171///     // This coercion would be an error without the derive.
1172///     let ptr: MySmartPointer<dyn MyTrait> = ptr;
1173/// }
1174/// ```
1175/// Without the `#[derive(CoercePointee)]` macro, this example would fail with the following error:
1176/// ```text
1177/// error[E0308]: mismatched types
1178///   --> src/main.rs:11:44
1179///    |
1180/// 11 |     let ptr: MySmartPointer<dyn MyTrait> = ptr;
1181///    |              ---------------------------   ^^^ expected `MySmartPointer<dyn MyTrait>`, found `MySmartPointer<i32>`
1182///    |              |
1183///    |              expected due to this
1184///    |
1185///    = note: expected struct `MySmartPointer<dyn MyTrait>`
1186///               found struct `MySmartPointer<i32>`
1187///    = help: `i32` implements `MyTrait` so you could box the found value and coerce it to the trait object `Box<dyn MyTrait>`, you will have to change the expected type as well
1188/// ```
1189///
1190/// ## Dyn compatibility
1191///
1192/// This macro allows you to dispatch on the user-defined pointer type. That is, traits using the
1193/// type as a receiver are dyn-compatible. For example, this compiles:
1194///
1195/// ```
1196/// #![feature(arbitrary_self_types, derive_coerce_pointee)]
1197/// use std::marker::CoercePointee;
1198/// use std::ops::Deref;
1199///
1200/// #[derive(CoercePointee)]
1201/// #[repr(transparent)]
1202/// struct MySmartPointer<T: ?Sized>(Box<T>);
1203///
1204/// impl<T: ?Sized> Deref for MySmartPointer<T> {
1205///     type Target = T;
1206///     fn deref(&self) -> &T {
1207///         &self.0
1208///     }
1209/// }
1210///
1211/// // You can always define this trait. (as long as you have #![feature(arbitrary_self_types)])
1212/// trait MyTrait {
1213///     fn func(self: MySmartPointer<Self>);
1214/// }
1215///
1216/// // But using `dyn MyTrait` requires #[derive(CoercePointee)].
1217/// fn call_func(value: MySmartPointer<dyn MyTrait>) {
1218///     value.func();
1219/// }
1220/// ```
1221/// If you remove the `#[derive(CoercePointee)]` annotation from the struct, then the above example
1222/// will fail with this error message:
1223/// ```text
1224/// error[E0038]: the trait `MyTrait` is not dyn compatible
1225///   --> src/lib.rs:21:36
1226///    |
1227/// 17 |     fn func(self: MySmartPointer<Self>);
1228///    |                   -------------------- help: consider changing method `func`'s `self` parameter to be `&self`: `&Self`
1229/// ...
1230/// 21 | fn call_func(value: MySmartPointer<dyn MyTrait>) {
1231///    |                                    ^^^^^^^^^^^ `MyTrait` is not dyn compatible
1232///    |
1233/// note: for a trait to be dyn compatible it needs to allow building a vtable
1234///       for more information, visit <https://doc.rust-lang.org/reference/items/traits.html#object-safety>
1235///   --> src/lib.rs:17:19
1236///    |
1237/// 16 | trait MyTrait {
1238///    |       ------- this trait is not dyn compatible...
1239/// 17 |     fn func(self: MySmartPointer<Self>);
1240///    |                   ^^^^^^^^^^^^^^^^^^^^ ...because method `func`'s `self` parameter cannot be dispatched on
1241/// ```
1242///
1243/// # Requirements for using the macro
1244///
1245/// This macro can only be used if:
1246/// * The type is a `#[repr(transparent)]` struct.
1247/// * The type of its non-zero-sized field must either be a standard library pointer type
1248///   (reference, raw pointer, `NonNull`, `Box`, `Rc`, `Arc`, etc.) or another user-defined type
1249///   also using the `#[derive(CoercePointee)]` macro.
1250/// * Zero-sized fields must not mention any generic parameters unless the zero-sized field has
1251///   type [`PhantomData`].
1252///
1253/// ## Multiple type parameters
1254///
1255/// If the type has multiple type parameters, then you must explicitly specify which one should be
1256/// used for dynamic dispatch. For example:
1257/// ```
1258/// # #![feature(derive_coerce_pointee)]
1259/// # use std::marker::{CoercePointee, PhantomData};
1260/// #[derive(CoercePointee)]
1261/// #[repr(transparent)]
1262/// struct MySmartPointer<#[pointee] T: ?Sized, U> {
1263///     ptr: Box<T>,
1264///     _phantom: PhantomData<U>,
1265/// }
1266/// ```
1267/// Specifying `#[pointee]` when the struct has only one type parameter is allowed, but not required.
1268///
1269/// # Examples
1270///
1271/// A custom implementation of the `Rc` type:
1272/// ```
1273/// #![feature(derive_coerce_pointee)]
1274/// use std::marker::CoercePointee;
1275/// use std::ops::Deref;
1276/// use std::ptr::NonNull;
1277///
1278/// #[derive(CoercePointee)]
1279/// #[repr(transparent)]
1280/// pub struct Rc<T: ?Sized> {
1281///     inner: NonNull<RcInner<T>>,
1282/// }
1283///
1284/// struct RcInner<T: ?Sized> {
1285///     refcount: usize,
1286///     value: T,
1287/// }
1288///
1289/// impl<T: ?Sized> Deref for Rc<T> {
1290///     type Target = T;
1291///     fn deref(&self) -> &T {
1292///         let ptr = self.inner.as_ptr();
1293///         unsafe { &(*ptr).value }
1294///     }
1295/// }
1296///
1297/// impl<T> Rc<T> {
1298///     pub fn new(value: T) -> Self {
1299///         let inner = Box::new(RcInner {
1300///             refcount: 1,
1301///             value,
1302///         });
1303///         Self {
1304///             inner: NonNull::from(Box::leak(inner)),
1305///         }
1306///     }
1307/// }
1308///
1309/// impl<T: ?Sized> Clone for Rc<T> {
1310///     fn clone(&self) -> Self {
1311///         // A real implementation would handle overflow here.
1312///         unsafe { (*self.inner.as_ptr()).refcount += 1 };
1313///         Self { inner: self.inner }
1314///     }
1315/// }
1316///
1317/// impl<T: ?Sized> Drop for Rc<T> {
1318///     fn drop(&mut self) {
1319///         let ptr = self.inner.as_ptr();
1320///         unsafe { (*ptr).refcount -= 1 };
1321///         if unsafe { (*ptr).refcount } == 0 {
1322///             drop(unsafe { Box::from_raw(ptr) });
1323///         }
1324///     }
1325/// }
1326/// ```
1327#[rustc_builtin_macro(CoercePointee, attributes(pointee))]
1328#[allow_internal_unstable(dispatch_from_dyn, coerce_unsized, unsize, coerce_pointee_validated)]
1329#[rustc_diagnostic_item = "CoercePointee"]
1330#[unstable(feature = "derive_coerce_pointee", issue = "123430")]
1331pub macro CoercePointee($item:item) {
1332    /* compiler built-in */
1333}
1334
1335/// A trait that is implemented for ADTs with `derive(CoercePointee)` so that
1336/// the compiler can enforce the derive impls are valid post-expansion, since
1337/// the derive has stricter requirements than if the impls were written by hand.
1338///
1339/// This trait is not intended to be implemented by users or used other than
1340/// validation, so it should never be stabilized.
1341#[lang = "coerce_pointee_validated"]
1342#[unstable(feature = "coerce_pointee_validated", issue = "none")]
1343#[doc(hidden)]
1344pub trait CoercePointeeValidated {
1345    /* compiler built-in */
1346}
````