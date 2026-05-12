---
title: clone.rs - source
url: https://doc.rust-lang.org/src/core/clone.rs.html#549
source: crawler
fetched_at: 2026-05-06T21:24:07.685577666-03:00
rendered_js: false
word_count: 3488
summary: This document defines the Clone trait in Rust, which provides a mechanism for explicitly duplicating values that are not implicitly copyable, and details its requirements, derivation, and relationship with other traits.
tags:
    - rust
    - traits
    - memory-management
    - cloning
    - programming-concepts
category: reference
---

## core/ clone.rs

````rust
1//! The `Clone` trait for types that cannot be 'implicitly copied'.
2//!
3//! In Rust, some simple types are "implicitly copyable" and when you
4//! assign them or pass them as arguments, the receiver will get a copy,
5//! leaving the original value in place. These types do not require
6//! allocation to copy and do not have finalizers (i.e., they do not
7//! contain owned boxes or implement [`Drop`]), so the compiler considers
8//! them cheap and safe to copy. For other types copies must be made
9//! explicitly, by convention implementing the [`Clone`] trait and calling
10//! the [`clone`] method.
11//!
12//! [`clone`]: Clone::clone
13//!
14//! Basic usage example:
15//!
16//! ```
17//! let s = String::new(); // String type implements Clone
18//! let copy = s.clone(); // so we can clone it
19//! ```
20//!
21//! To easily implement the Clone trait, you can also use
22//! `#[derive(Clone)]`. Example:
23//!
24//! ```
25//! #[derive(Clone)] // we add the Clone trait to Morpheus struct
26//! struct Morpheus {
27//!    blue_pill: f32,
28//!    red_pill: i64,
29//! }
30//!
31//! fn main() {
32//!    let f = Morpheus { blue_pill: 0.0, red_pill: 0 };
33//!    let copy = f.clone(); // and now we can clone it!
34//! }
35//! ```
36
37#![stable(feature = "rust1", since = "1.0.0")]
38
39use crate::marker::{Destruct, PointeeSized};
40
41mod uninit;
42
43/// A common trait that allows explicit creation of a duplicate value.
44///
45/// Calling [`clone`] always produces a new value.
46/// However, for types that are references to other data (such as smart pointers or references),
47/// the new value may still point to the same underlying data, rather than duplicating it.
48/// See [`Clone::clone`] for more details.
49///
50/// This distinction is especially important when using `#[derive(Clone)]` on structs containing
51/// smart pointers like `Arc<Mutex<T>>` - the cloned struct will share mutable state with the
52/// original.
53///
54/// Differs from [`Copy`] in that [`Copy`] is implicit and an inexpensive bit-wise copy, while
55/// `Clone` is always explicit and may or may not be expensive. [`Copy`] has no methods, so you
56/// cannot change its behavior, but when implementing `Clone`, the `clone` method you provide
57/// may run arbitrary code.
58///
59/// Since `Clone` is a supertrait of [`Copy`], any type that implements `Copy` must also implement
60/// `Clone`.
61///
62/// ## Derivable
63///
64/// This trait can be used with `#[derive]` if all fields are `Clone`. The `derive`d
65/// implementation of [`Clone`] calls [`clone`] on each field.
66///
67/// [`clone`]: Clone::clone
68///
69/// For a generic struct, `#[derive]` implements `Clone` conditionally by adding bound `Clone` on
70/// generic parameters.
71///
72/// ```
73/// // `derive` implements Clone for Reading<T> when T is Clone.
74/// #[derive(Clone)]
75/// struct Reading<T> {
76///     frequency: T,
77/// }
78/// ```
79///
80/// ## How can I implement `Clone`?
81///
82/// Types that are [`Copy`] should have a trivial implementation of `Clone`. More formally:
83/// if `T: Copy`, `x: T`, and `y: &T`, then `let x = y.clone();` is equivalent to `let x = *y;`.
84/// Manual implementations should be careful to uphold this invariant; however, unsafe code
85/// must not rely on it to ensure memory safety.
86///
87/// An example is a generic struct holding a function pointer. In this case, the
88/// implementation of `Clone` cannot be `derive`d, but can be implemented as:
89///
90/// ```
91/// struct Generate<T>(fn() -> T);
92///
93/// impl<T> Copy for Generate<T> {}
94///
95/// impl<T> Clone for Generate<T> {
96///     fn clone(&self) -> Self {
97///         *self
98///     }
99/// }
100/// ```
101///
102/// If we `derive`:
103///
104/// ```
105/// #[derive(Copy, Clone)]
106/// struct Generate<T>(fn() -> T);
107/// ```
108///
109/// the auto-derived implementations will have unnecessary `T: Copy` and `T: Clone` bounds:
110///
111/// ```
112/// # struct Generate<T>(fn() -> T);
113///
114/// // Automatically derived
115/// impl<T: Copy> Copy for Generate<T> { }
116///
117/// // Automatically derived
118/// impl<T: Clone> Clone for Generate<T> {
119///     fn clone(&self) -> Generate<T> {
120///         Generate(Clone::clone(&self.0))
121///     }
122/// }
123/// ```
124///
125/// The bounds are unnecessary because clearly the function itself should be
126/// copy- and cloneable even if its return type is not:
127///
128/// ```compile_fail,E0599
129/// #[derive(Copy, Clone)]
130/// struct Generate<T>(fn() -> T);
131///
132/// struct NotCloneable;
133///
134/// fn generate_not_cloneable() -> NotCloneable {
135///     NotCloneable
136/// }
137///
138/// Generate(generate_not_cloneable).clone(); // error: trait bounds were not satisfied
139/// // Note: With the manual implementations the above line will compile.
140/// ```
141///
142/// ## `Clone` and `PartialEq`/`Eq`
143/// `Clone` is intended for the duplication of objects. Consequently, when implementing
144/// both `Clone` and [`PartialEq`], the following property is expected to hold:
145/// ```text
146/// x == x -> x.clone() == x
147/// ```
148/// In other words, if an object compares equal to itself,
149/// its clone must also compare equal to the original.
150///
151/// For types that also implement [`Eq`] – for which `x == x` always holds –
152/// this implies that `x.clone() == x` must always be true.
153/// Standard library collections such as
154/// [`HashMap`], [`HashSet`], [`BTreeMap`], [`BTreeSet`] and [`BinaryHeap`]
155/// rely on their keys respecting this property for correct behavior.
156/// Furthermore, these collections require that cloning a key preserves the outcome of the
157/// [`Hash`] and [`Ord`] methods. Thankfully, this follows automatically from `x.clone() == x`
158/// if `Hash` and `Ord` are correctly implemented according to their own requirements.
159///
160/// When deriving both `Clone` and [`PartialEq`] using `#[derive(Clone, PartialEq)]`
161/// or when additionally deriving [`Eq`] using `#[derive(Clone, PartialEq, Eq)]`,
162/// then this property is automatically upheld – provided that it is satisfied by
163/// the underlying types.
164///
165/// Violating this property is a logic error. The behavior resulting from a logic error is not
166/// specified, but users of the trait must ensure that such logic errors do *not* result in
167/// undefined behavior. This means that `unsafe` code **must not** rely on this property
168/// being satisfied.
169///
170/// ## Additional implementors
171///
172/// In addition to the [implementors listed below][impls],
173/// the following types also implement `Clone`:
174///
175/// * Function item types (i.e., the distinct types defined for each function)
176/// * Function pointer types (e.g., `fn() -> i32`)
177/// * Closure types, if they capture no value from the environment
178///   or if all such captured values implement `Clone` themselves.
179///   Note that variables captured by shared reference always implement `Clone`
180///   (even if the referent doesn't),
181///   while variables captured by mutable reference never implement `Clone`.
182///
183/// [`HashMap`]: ../../std/collections/struct.HashMap.html
184/// [`HashSet`]: ../../std/collections/struct.HashSet.html
185/// [`BTreeMap`]: ../../std/collections/struct.BTreeMap.html
186/// [`BTreeSet`]: ../../std/collections/struct.BTreeSet.html
187/// [`BinaryHeap`]: ../../std/collections/struct.BinaryHeap.html
188/// [impls]: #implementors
189#[stable(feature = "rust1", since = "1.0.0")]
190#[lang = "clone"]
191#[rustc_diagnostic_item = "Clone"]
192#[rustc_trivial_field_reads]
193#[rustc_const_unstable(feature = "const_clone", issue = "142757")]
194pub const trait Clone: Sized {
195    /// Returns a duplicate of the value.
196    ///
197    /// Note that what "duplicate" means varies by type:
198    /// - For most types, this creates a deep, independent copy
199    /// - For reference types like `&T`, this creates another reference to the same value
200    /// - For smart pointers like [`Arc`] or [`Rc`], this increments the reference count
201    ///   but still points to the same underlying data
202    ///
203    /// [`Arc`]: ../../std/sync/struct.Arc.html
204    /// [`Rc`]: ../../std/rc/struct.Rc.html
205    ///
206    /// # Examples
207    ///
208    /// ```
209    /// # #![allow(noop_method_call)]
210    /// let hello = "Hello"; // &str implements Clone
211    ///
212    /// assert_eq!("Hello", hello.clone());
213    /// ```
214    ///
215    /// Example with a reference-counted type:
216    ///
217    /// ```
218    /// use std::sync::{Arc, Mutex};
219    ///
220    /// let data = Arc::new(Mutex::new(vec![1, 2, 3]));
221    /// let data_clone = data.clone(); // Creates another Arc pointing to the same Mutex
222    ///
223    /// {
224    ///     let mut lock = data.lock().unwrap();
225    ///     lock.push(4);
226    /// }
227    ///
228    /// // Changes are visible through the clone because they share the same underlying data
229    /// assert_eq!(*data_clone.lock().unwrap(), vec![1, 2, 3, 4]);
230    /// ```
231    #[stable(feature = "rust1", since = "1.0.0")]
232    #[must_use = "cloning is often expensive and is not expected to have side effects"]
233    // Clone::clone is special because the compiler generates MIR to implement it for some types.
234    // See InstanceKind::CloneShim.
235    #[lang = "clone_fn"]
236    fn clone(&self) -> Self;
237
238    /// Performs copy-assignment from `source`.
239    ///
240    /// `a.clone_from(&b)` is equivalent to `a = b.clone()` in functionality,
241    /// but can be overridden to reuse the resources of `a` to avoid unnecessary
242    /// allocations.
243    #[inline]
244    #[stable(feature = "rust1", since = "1.0.0")]
245    fn clone_from(&mut self, source: &Self)
246    where
247        Self: [const] Destruct,
248    {
249        *self = source.clone()
250    }
251}
252
253/// Indicates that the `Clone` implementation is identical to copying the value.
254///
255/// This is used for some optimizations in the standard library, which specializes
256/// on this trait to select faster implementations of functions such as
257/// [`clone_from_slice`](slice::clone_from_slice). It is automatically implemented
258/// when using `#[derive(Clone, Copy)]`.
259///
260/// Note that this trait does not imply that the type is `Copy`, because e.g.
261/// `core::ops::Range<i32>` could soundly implement this trait.
262///
263/// # Safety
264/// `Clone::clone` must be equivalent to copying the value, otherwise calling functions
265/// such as `slice::clone_from_slice` can have undefined behaviour.
266#[unstable(
267    feature = "trivial_clone",
268    reason = "this isn't part of any API guarantee",
269    issue = "none"
270)]
271#[rustc_const_unstable(feature = "const_clone", issue = "142757")]
272#[lang = "trivial_clone"]
273// SAFETY:
274// It is sound to specialize on this because the `clone` implementation cannot be
275// lifetime-dependent. Therefore, if `TrivialClone` is implemented for any lifetime,
276// its invariant holds whenever `Clone` is implemented, even if the actual
277// `TrivialClone` bound would not be satisfied because of lifetime bounds.
278#[rustc_unsafe_specialization_marker]
279// If `#[derive(Clone, Clone, Copy)]` is written, there will be multiple
280// implementations of `TrivialClone`. To keep it from appearing in error
281// messages, make it a `#[marker]` trait.
282#[marker]
283pub const unsafe trait TrivialClone: [const] Clone {}
284
285/// Derive macro generating an impl of the trait `Clone`.
286#[rustc_builtin_macro]
287#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
288#[allow_internal_unstable(core_intrinsics, derive_clone_copy_internals, trivial_clone)]
289pub macro Clone($item:item) {
290    /* compiler built-in */
291}
292
293/// Trait for objects whose [`Clone`] impl is lightweight (e.g. reference-counted)
294///
295/// Cloning an object implementing this trait should in general:
296/// - be O(1) (constant) time regardless of the amount of data managed by the object,
297/// - not require a memory allocation,
298/// - not require copying more than roughly 64 bytes (a typical cache line size),
299/// - not block the current thread,
300/// - not have any semantic side effects (e.g. allocating a file descriptor), and
301/// - not have overhead larger than a couple of atomic operations.
302///
303/// The `UseCloned` trait does not provide a method; instead, it indicates that
304/// `Clone::clone` is lightweight, and allows the use of the `.use` syntax.
305///
306/// ## .use postfix syntax
307///
308/// Values can be `.use`d by adding `.use` postfix to the value you want to use.
309///
310/// ```ignore (this won't work until we land use)
311/// fn foo(f: Foo) {
312///     // if `Foo` implements `Copy` f would be copied into x.
313///     // if `Foo` implements `UseCloned` f would be cloned into x.
314///     // otherwise f would be moved into x.
315///     let x = f.use;
316///     // ...
317/// }
318/// ```
319///
320/// ## use closures
321///
322/// Use closures allow captured values to be automatically used.
323/// This is similar to have a closure that you would call `.use` over each captured value.
324#[unstable(feature = "ergonomic_clones", issue = "132290")]
325#[lang = "use_cloned"]
326pub trait UseCloned: Clone {
327    // Empty.
328}
329
330macro_rules! impl_use_cloned {
331    ($($t:ty)*) => {
332        $(
333            #[unstable(feature = "ergonomic_clones", issue = "132290")]
334            impl UseCloned for $t {}
335        )*
336    }
337}
338
339impl_use_cloned! {
340    usize u8 u16 u32 u64 u128
341    isize i8 i16 i32 i64 i128
342             f16 f32 f64 f128
343    bool char
344}
345
346// FIXME(aburka): these structs are used solely by #[derive] to
347// assert that every component of a type implements Clone or Copy.
348//
349// These structs should never appear in user code.
350#[doc(hidden)]
351#[allow(missing_debug_implementations)]
352#[unstable(
353    feature = "derive_clone_copy_internals",
354    reason = "deriving hack, should not be public",
355    issue = "none"
356)]
357pub struct AssertParamIsClone<T: Clone + PointeeSized> {
358    _field: crate::marker::PhantomData<T>,
359}
360#[doc(hidden)]
361#[allow(missing_debug_implementations)]
362#[unstable(
363    feature = "derive_clone_copy_internals",
364    reason = "deriving hack, should not be public",
365    issue = "none"
366)]
367pub struct AssertParamIsCopy<T: Copy + PointeeSized> {
368    _field: crate::marker::PhantomData<T>,
369}
370
371/// A generalization of [`Clone`] to [dynamically-sized types][DST] stored in arbitrary containers.
372///
373/// This trait is implemented for all types implementing [`Clone`], [slices](slice) of all
374/// such types, and other dynamically-sized types in the standard library.
375/// You may also implement this trait to enable cloning custom DSTs
376/// (structures containing dynamically-sized fields), or use it as a supertrait to enable
377/// cloning a [trait object].
378///
379/// This trait is normally used via operations on container types which support DSTs,
380/// so you should not typically need to call `.clone_to_uninit()` explicitly except when
381/// implementing such a container or otherwise performing explicit management of an allocation,
382/// or when implementing `CloneToUninit` itself.
383///
384/// # Safety
385///
386/// Implementations must ensure that when `.clone_to_uninit(dest)` returns normally rather than
387/// panicking, it always leaves `*dest` initialized as a valid value of type `Self`.
388///
389/// # Examples
390///
391// FIXME(#126799): when `Box::clone` allows use of `CloneToUninit`, rewrite these examples with it
392// since `Rc` is a distraction.
393///
394/// If you are defining a trait, you can add `CloneToUninit` as a supertrait to enable cloning of
395/// `dyn` values of your trait:
396///
397/// ```
398/// #![feature(clone_to_uninit)]
399/// use std::rc::Rc;
400///
401/// trait Foo: std::fmt::Debug + std::clone::CloneToUninit {
402///     fn modify(&mut self);
403///     fn value(&self) -> i32;
404/// }
405///
406/// impl Foo for i32 {
407///     fn modify(&mut self) {
408///         *self *= 10;
409///     }
410///     fn value(&self) -> i32 {
411///         *self
412///     }
413/// }
414///
415/// let first: Rc<dyn Foo> = Rc::new(1234);
416///
417/// let mut second = first.clone();
418/// Rc::make_mut(&mut second).modify(); // make_mut() will call clone_to_uninit()
419///
420/// assert_eq!(first.value(), 1234);
421/// assert_eq!(second.value(), 12340);
422/// ```
423///
424/// The following is an example of implementing `CloneToUninit` for a custom DST.
425/// (It is essentially a limited form of what `derive(CloneToUninit)` would do,
426/// if such a derive macro existed.)
427///
428/// ```
429/// #![feature(clone_to_uninit)]
430/// use std::clone::CloneToUninit;
431/// use std::mem::offset_of;
432/// use std::rc::Rc;
433///
434/// #[derive(PartialEq)]
435/// struct MyDst<T: ?Sized> {
436///     label: String,
437///     contents: T,
438/// }
439///
440/// unsafe impl<T: ?Sized + CloneToUninit> CloneToUninit for MyDst<T> {
441///     unsafe fn clone_to_uninit(&self, dest: *mut u8) {
442///         // The offset of `self.contents` is dynamic because it depends on the alignment of T
443///         // which can be dynamic (if `T = dyn SomeTrait`). Therefore, we have to obtain it
444///         // dynamically by examining `self`, rather than using `offset_of!`.
445///         //
446///         // SAFETY: `self` by definition points somewhere before `&self.contents` in the same
447///         // allocation.
448///         let offset_of_contents = unsafe {
449///             (&raw const self.contents).byte_offset_from_unsigned(self)
450///         };
451///
452///         // Clone the *sized* fields of `self` (just one, in this example).
453///         // (By cloning this first and storing it temporarily in a local variable, we avoid
454///         // leaking it in case of any panic, using the ordinary automatic cleanup of local
455///         // variables. Such a leak would be sound, but undesirable.)
456///         let label = self.label.clone();
457///
458///         // SAFETY: The caller must provide a `dest` such that these field offsets are valid
459///         // to write to.
460///         unsafe {
461///             // Clone the unsized field directly from `self` to `dest`.
462///             self.contents.clone_to_uninit(dest.add(offset_of_contents));
463///
464///             // Now write all the sized fields.
465///             //
466///             // Note that we only do this once all of the clone() and clone_to_uninit() calls
467///             // have completed, and therefore we know that there are no more possible panics;
468///             // this ensures no memory leaks in case of panic.
469///             dest.add(offset_of!(Self, label)).cast::<String>().write(label);
470///         }
471///         // All fields of the struct have been initialized; therefore, the struct is initialized,
472///         // and we have satisfied our `unsafe impl CloneToUninit` obligations.
473///     }
474/// }
475///
476/// fn main() {
477///     // Construct MyDst<[u8; 4]>, then coerce to MyDst<[u8]>.
478///     let first: Rc<MyDst<[u8]>> = Rc::new(MyDst {
479///         label: String::from("hello"),
480///         contents: [1, 2, 3, 4],
481///     });
482///
483///     let mut second = first.clone();
484///     // make_mut() will call clone_to_uninit().
485///     for elem in Rc::make_mut(&mut second).contents.iter_mut() {
486///         *elem *= 10;
487///     }
488///
489///     assert_eq!(first.contents, [1, 2, 3, 4]);
490///     assert_eq!(second.contents, [10, 20, 30, 40]);
491///     assert_eq!(second.label, "hello");
492/// }
493/// ```
494///
495/// # See Also
496///
497/// * [`Clone::clone_from`] is a safe function which may be used instead when [`Self: Sized`](Sized)
498///   and the destination is already initialized; it may be able to reuse allocations owned by
499///   the destination, whereas `clone_to_uninit` cannot, since its destination is assumed to be
500///   uninitialized.
501/// * [`ToOwned`], which allocates a new destination container.
502///
503/// [`ToOwned`]: ../../std/borrow/trait.ToOwned.html
504/// [DST]: https://doc.rust-lang.org/reference/dynamically-sized-types.html
505/// [trait object]: https://doc.rust-lang.org/reference/types/trait-object.html
506#[unstable(feature = "clone_to_uninit", issue = "126799")]
507pub unsafe trait CloneToUninit {
508    /// Performs copy-assignment from `self` to `dest`.
509    ///
510    /// This is analogous to `std::ptr::write(dest.cast(), self.clone())`,
511    /// except that `Self` may be a dynamically-sized type ([`!Sized`](Sized)).
512    ///
513    /// Before this function is called, `dest` may point to uninitialized memory.
514    /// After this function is called, `dest` will point to initialized memory; it will be
515    /// sound to create a `&Self` reference from the pointer with the [pointer metadata]
516    /// from `self`.
517    ///
518    /// # Safety
519    ///
520    /// Behavior is undefined if any of the following conditions are violated:
521    ///
522    /// * `dest` must be [valid] for writes for `size_of_val(self)` bytes.
523    /// * `dest` must be properly aligned to `align_of_val(self)`.
524    ///
525    /// [valid]: crate::ptr#safety
526    /// [pointer metadata]: crate::ptr::metadata()
527    ///
528    /// # Panics
529    ///
530    /// This function may panic. (For example, it might panic if memory allocation for a clone
531    /// of a value owned by `self` fails.)
532    /// If the call panics, then `*dest` should be treated as uninitialized memory; it must not be
533    /// read or dropped, because even if it was previously valid, it may have been partially
534    /// overwritten.
535    ///
536    /// The caller may wish to take care to deallocate the allocation pointed to by `dest`,
537    /// if applicable, to avoid a memory leak (but this is not a requirement).
538    ///
539    /// Implementors should avoid leaking values by, upon unwinding, dropping all component values
540    /// that might have already been created. (For example, if a `[Foo]` of length 3 is being
541    /// cloned, and the second of the three calls to `Foo::clone()` unwinds, then the first `Foo`
542    /// cloned should be dropped.)
543    unsafe fn clone_to_uninit(&self, dest: *mut u8);
544}
545
546#[unstable(feature = "clone_to_uninit", issue = "126799")]
547unsafe impl<T: Clone> CloneToUninit for T {
548    #[inline]
549    unsafe fn clone_to_uninit(&self, dest: *mut u8) {
550        // SAFETY: we're calling a specialization with the same contract
551        unsafe { <T as self::uninit::CopySpec>::clone_one(self, dest.cast::<T>()) }
552    }
553}
554
555#[unstable(feature = "clone_to_uninit", issue = "126799")]
556unsafe impl<T: Clone> CloneToUninit for [T] {
557    #[inline]
558    #[cfg_attr(debug_assertions, track_caller)]
559    unsafe fn clone_to_uninit(&self, dest: *mut u8) {
560        let dest: *mut [T] = dest.with_metadata_of(self);
561        // SAFETY: we're calling a specialization with the same contract
562        unsafe { <T as self::uninit::CopySpec>::clone_slice(self, dest) }
563    }
564}
565
566#[unstable(feature = "clone_to_uninit", issue = "126799")]
567unsafe impl CloneToUninit for str {
568    #[inline]
569    #[cfg_attr(debug_assertions, track_caller)]
570    unsafe fn clone_to_uninit(&self, dest: *mut u8) {
571        // SAFETY: str is just a [u8] with UTF-8 invariant
572        unsafe { self.as_bytes().clone_to_uninit(dest) }
573    }
574}
575
576#[unstable(feature = "clone_to_uninit", issue = "126799")]
577unsafe impl CloneToUninit for crate::ffi::CStr {
578    #[cfg_attr(debug_assertions, track_caller)]
579    unsafe fn clone_to_uninit(&self, dest: *mut u8) {
580        // SAFETY: For now, CStr is just a #[repr(trasnsparent)] [c_char] with some invariants.
581        // And we can cast [c_char] to [u8] on all supported platforms (see: to_bytes_with_nul).
582        // The pointer metadata properly preserves the length (so NUL is also copied).
583        // See: `cstr_metadata_is_length_with_nul` in tests.
584        unsafe { self.to_bytes_with_nul().clone_to_uninit(dest) }
585    }
586}
587
588#[unstable(feature = "bstr", issue = "134915")]
589unsafe impl CloneToUninit for crate::bstr::ByteStr {
590    #[inline]
591    #[cfg_attr(debug_assertions, track_caller)]
592    unsafe fn clone_to_uninit(&self, dst: *mut u8) {
593        // SAFETY: ByteStr is a `#[repr(transparent)]` wrapper around `[u8]`
594        unsafe { self.as_bytes().clone_to_uninit(dst) }
595    }
596}
597
598/// Implementations of `Clone` for primitive types.
599///
600/// Implementations that cannot be described in Rust
601/// are implemented in `traits::SelectionContext::copy_clone_conditions()`
602/// in `rustc_trait_selection`.
603mod impls {
604    use super::TrivialClone;
605    use crate::marker::PointeeSized;
606
607    macro_rules! impl_clone {
608        ($($t:ty)*) => {
609            $(
610                #[stable(feature = "rust1", since = "1.0.0")]
611                #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
612                impl const Clone for $t {
613                    #[inline(always)]
614                    fn clone(&self) -> Self {
615                        *self
616                    }
617                }
618
619                #[doc(hidden)]
620                #[unstable(feature = "trivial_clone", issue = "none")]
621                #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
622                unsafe impl const TrivialClone for $t {}
623            )*
624        }
625    }
626
627    impl_clone! {
628        usize u8 u16 u32 u64 u128
629        isize i8 i16 i32 i64 i128
630        f16 f32 f64 f128
631        bool char
632    }
633
634    #[unstable(feature = "never_type", issue = "35121")]
635    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
636    impl const Clone for ! {
637        #[inline]
638        fn clone(&self) -> Self {
639            *self
640        }
641    }
642
643    #[doc(hidden)]
644    #[unstable(feature = "trivial_clone", issue = "none")]
645    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
646    unsafe impl const TrivialClone for ! {}
647
648    #[stable(feature = "rust1", since = "1.0.0")]
649    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
650    impl<T: PointeeSized> const Clone for *const T {
651        #[inline(always)]
652        fn clone(&self) -> Self {
653            *self
654        }
655    }
656
657    #[doc(hidden)]
658    #[unstable(feature = "trivial_clone", issue = "none")]
659    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
660    unsafe impl<T: PointeeSized> const TrivialClone for *const T {}
661
662    #[stable(feature = "rust1", since = "1.0.0")]
663    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
664    impl<T: PointeeSized> const Clone for *mut T {
665        #[inline(always)]
666        fn clone(&self) -> Self {
667            *self
668        }
669    }
670
671    #[doc(hidden)]
672    #[unstable(feature = "trivial_clone", issue = "none")]
673    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
674    unsafe impl<T: PointeeSized> const TrivialClone for *mut T {}
675
676    /// Shared references can be cloned, but mutable references *cannot*!
677    #[stable(feature = "rust1", since = "1.0.0")]
678    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
679    impl<T: PointeeSized> const Clone for &T {
680        #[inline(always)]
681        #[rustc_diagnostic_item = "noop_method_clone"]
682        fn clone(&self) -> Self {
683            self
684        }
685    }
686
687    #[doc(hidden)]
688    #[unstable(feature = "trivial_clone", issue = "none")]
689    #[rustc_const_unstable(feature = "const_clone", issue = "142757")]
690    unsafe impl<T: PointeeSized> const TrivialClone for &T {}
691
692    /// Shared references can be cloned, but mutable references *cannot*!
693    #[stable(feature = "rust1", since = "1.0.0")]
694    impl<T: PointeeSized> !Clone for &mut T {}
695}
````