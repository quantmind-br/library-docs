---
title: boxed.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/boxed.rs.html#1963
source: crawler
fetched_at: 2026-05-06T21:33:50.266256623-03:00
rendered_js: false
word_count: 10798
summary: This document explains the functionality, memory layout, and usage of the Box<T> type in Rust, which provides heap allocation with ownership semantics.
tags:
    - rust
    - heap-allocation
    - ownership
    - memory-management
    - smart-pointers
    - ffi
category: reference
---

## alloc/ boxed.rs

````rust
1//! The `Box<T>` type for heap allocation.
2//!
3//! [`Box<T>`], casually referred to as a 'box', provides the simplest form of
4//! heap allocation in Rust. Boxes provide ownership for this allocation, and
5//! drop their contents when they go out of scope. Boxes also ensure that they
6//! never allocate more than `isize::MAX` bytes.
7//!
8//! # Examples
9//!
10//! Move a value from the stack to the heap by creating a [`Box`]:
11//!
12//! ```
13//! let val: u8 = 5;
14//! let boxed: Box<u8> = Box::new(val);
15//! ```
16//!
17//! Move a value from a [`Box`] back to the stack by [dereferencing]:
18//!
19//! ```
20//! let boxed: Box<u8> = Box::new(5);
21//! let val: u8 = *boxed;
22//! ```
23//!
24//! Creating a recursive data structure:
25//!
26//! ```
27//! # #[allow(dead_code)]
28//! #[derive(Debug)]
29//! enum List<T> {
30//!     Cons(T, Box<List<T>>),
31//!     Nil,
32//! }
33//!
34//! let list: List<i32> = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
35//! println!("{list:?}");
36//! ```
37//!
38//! This will print `Cons(1, Cons(2, Nil))`.
39//!
40//! Recursive structures must be boxed, because if the definition of `Cons`
41//! looked like this:
42//!
43//! ```compile_fail,E0072
44//! # enum List<T> {
45//! Cons(T, List<T>),
46//! # }
47//! ```
48//!
49//! It wouldn't work. This is because the size of a `List` depends on how many
50//! elements are in the list, and so we don't know how much memory to allocate
51//! for a `Cons`. By introducing a [`Box<T>`], which has a defined size, we know how
52//! big `Cons` needs to be.
53//!
54//! # Memory layout
55//!
56//! For non-zero-sized values, a [`Box`] will use the [`Global`] allocator for its allocation. It is
57//! valid to convert both ways between a [`Box`] and a raw pointer allocated with the [`Global`]
58//! allocator, given that the [`Layout`] used with the allocator is correct for the type and the raw
59//! pointer points to a valid value of the right type. More precisely, a `value: *mut T` that has
60//! been allocated with the [`Global`] allocator with `Layout::for_value(&*value)` may be converted
61//! into a box using [`Box::<T>::from_raw(value)`]. Conversely, the memory backing a `value: *mut T`
62//! obtained from [`Box::<T>::into_raw`] may be deallocated using the [`Global`] allocator with
63//! [`Layout::for_value(&*value)`].
64//!
65//! For zero-sized values, the `Box` pointer has to be non-null and sufficiently aligned. The
66//! recommended way to build a Box to a ZST if `Box::new` cannot be used is to use
67//! [`ptr::NonNull::dangling`].
68//!
69//! On top of these basic layout requirements, a `Box<T>` must point to a valid value of `T`.
70//!
71//! So long as `T: Sized`, a `Box<T>` is guaranteed to be represented
72//! as a single pointer and is also ABI-compatible with C pointers
73//! (i.e. the C type `T*`). This means that if you have extern "C"
74//! Rust functions that will be called from C, you can define those
75//! Rust functions using `Box<T>` types, and use `T*` as corresponding
76//! type on the C side. As an example, consider this C header which
77//! declares functions that create and destroy some kind of `Foo`
78//! value:
79//!
80//! ```c
81//! /* C header */
82//!
83//! /* Returns ownership to the caller */
84//! struct Foo* foo_new(void);
85//!
86//! /* Takes ownership from the caller; no-op when invoked with null */
87//! void foo_delete(struct Foo*);
88//! ```
89//!
90//! These two functions might be implemented in Rust as follows. Here, the
91//! `struct Foo*` type from C is translated to `Box<Foo>`, which captures
92//! the ownership constraints. Note also that the nullable argument to
93//! `foo_delete` is represented in Rust as `Option<Box<Foo>>`, since `Box<Foo>`
94//! cannot be null.
95//!
96//! ```
97//! #[repr(C)]
98//! pub struct Foo;
99//!
100//! #[unsafe(no_mangle)]
101//! pub extern "C" fn foo_new() -> Box<Foo> {
102//!     Box::new(Foo)
103//! }
104//!
105//! #[unsafe(no_mangle)]
106//! pub extern "C" fn foo_delete(_: Option<Box<Foo>>) {}
107//! ```
108//!
109//! Even though `Box<T>` has the same representation and C ABI as a C pointer,
110//! this does not mean that you can convert an arbitrary `T*` into a `Box<T>`
111//! and expect things to work. `Box<T>` values will always be fully aligned,
112//! non-null pointers. Moreover, the destructor for `Box<T>` will attempt to
113//! free the value with the global allocator. In general, the best practice
114//! is to only use `Box<T>` for pointers that originated from the global
115//! allocator.
116//!
117//! **Important.** At least at present, you should avoid using
118//! `Box<T>` types for functions that are defined in C but invoked
119//! from Rust. In those cases, you should directly mirror the C types
120//! as closely as possible. Using types like `Box<T>` where the C
121//! definition is just using `T*` can lead to undefined behavior, as
122//! described in [rust-lang/unsafe-code-guidelines#198][ucg#198].
123//!
124//! # Considerations for unsafe code
125//!
126//! **Warning: This section is not normative and is subject to change, possibly
127//! being relaxed in the future! It is a simplified summary of the rules
128//! currently implemented in the compiler.**
129//!
130//! The aliasing rules for `Box<T>` are the same as for `&mut T`. `Box<T>`
131//! asserts uniqueness over its content. Using raw pointers derived from a box
132//! after that box has been mutated through, moved or borrowed as `&mut T`
133//! is not allowed. For more guidance on working with box from unsafe code, see
134//! [rust-lang/unsafe-code-guidelines#326][ucg#326].
135//!
136//! # Editions
137//!
138//! A special case exists for the implementation of `IntoIterator` for arrays on the Rust 2021
139//! edition, as documented [here][array]. Unfortunately, it was later found that a similar
140//! workaround should be added for boxed slices, and this was applied in the 2024 edition.
141//!
142//! Specifically, `IntoIterator` is implemented for `Box<[T]>` on all editions, but specific calls
143//! to `into_iter()` for boxed slices will defer to the slice implementation on editions before
144//! 2024:
145//!
146//! ```rust,edition2021
147//! // Rust 2015, 2018, and 2021:
148//!
149//! # #![allow(boxed_slice_into_iter)] // override our `deny(warnings)`
150//! let boxed_slice: Box<[i32]> = vec![0; 3].into_boxed_slice();
151//!
152//! // This creates a slice iterator, producing references to each value.
153//! for item in boxed_slice.into_iter().enumerate() {
154//!     let (i, x): (usize, &i32) = item;
155//!     println!("boxed_slice[{i}] = {x}");
156//! }
157//!
158//! // The `boxed_slice_into_iter` lint suggests this change for future compatibility:
159//! for item in boxed_slice.iter().enumerate() {
160//!     let (i, x): (usize, &i32) = item;
161//!     println!("boxed_slice[{i}] = {x}");
162//! }
163//!
164//! // You can explicitly iterate a boxed slice by value using `IntoIterator::into_iter`
165//! for item in IntoIterator::into_iter(boxed_slice).enumerate() {
166//!     let (i, x): (usize, i32) = item;
167//!     println!("boxed_slice[{i}] = {x}");
168//! }
169//! ```
170//!
171//! Similar to the array implementation, this may be modified in the future to remove this override,
172//! and it's best to avoid relying on this edition-dependent behavior if you wish to preserve
173//! compatibility with future versions of the compiler.
174//!
175//! [ucg#198]: https://github.com/rust-lang/unsafe-code-guidelines/issues/198
176//! [ucg#326]: https://github.com/rust-lang/unsafe-code-guidelines/issues/326
177//! [dereferencing]: core::ops::Deref
178//! [`Box::<T>::from_raw(value)`]: Box::from_raw
179//! [`Global`]: crate::alloc::Global
180//! [`Layout`]: crate::alloc::Layout
181//! [`Layout::for_value(&*value)`]: crate::alloc::Layout::for_value
182//! [valid]: ptr#safety
183
184#![stable(feature = "rust1", since = "1.0.0")]
185
186use core::borrow::{Borrow, BorrowMut};
187use core::clone::CloneToUninit;
188use core::cmp::Ordering;
189use core::error::{self, Error};
190use core::fmt;
191use core::future::Future;
192use core::hash::{Hash, Hasher};
193use core::marker::{Tuple, Unsize};
194#[cfg(not(no_global_oom_handling))]
195use core::mem::MaybeUninit;
196use core::mem::{self, SizedTypeProperties};
197use core::ops::{
198    AsyncFn, AsyncFnMut, AsyncFnOnce, CoerceUnsized, Coroutine, CoroutineState, Deref, DerefMut,
199    DerefPure, DispatchFromDyn, LegacyReceiver,
200};
201#[cfg(not(no_global_oom_handling))]
202use core::ops::{Residual, Try};
203use core::pin::{Pin, PinCoerceUnsized};
204use core::ptr::{self, NonNull, Unique};
205use core::task::{Context, Poll};
206
207#[cfg(not(no_global_oom_handling))]
208use crate::alloc::handle_alloc_error;
209use crate::alloc::{AllocError, Allocator, Global, Layout};
210use crate::raw_vec::RawVec;
211#[cfg(not(no_global_oom_handling))]
212use crate::str::from_boxed_utf8_unchecked;
213
214/// Conversion related impls for `Box<_>` (`From`, `downcast`, etc)
215mod convert;
216/// Iterator related impls for `Box<_>`.
217mod iter;
218/// [`ThinBox`] implementation.
219mod thin;
220
221#[unstable(feature = "thin_box", issue = "92791")]
222pub use thin::ThinBox;
223
224/// A pointer type that uniquely owns a heap allocation of type `T`.
225///
226/// See the [module-level documentation](../../std/boxed/index.html) for more.
227#[lang = "owned_box"]
228#[fundamental]
229#[stable(feature = "rust1", since = "1.0.0")]
230#[rustc_insignificant_dtor]
231#[doc(search_unbox)]
232// The declaration of the `Box` struct must be kept in sync with the
233// compiler or ICEs will happen.
234pub struct Box<
235    T: ?Sized,
236    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
237>(Unique<T>, A);
238
239/// Monomorphic function for allocating an uninit `Box`.
240#[inline]
241// The is a separate function to avoid doing it in every generic version, but it
242// looks small to the mir inliner (particularly in panic=abort) so leave it to
243// the backend to decide whether pulling it in everywhere is worth doing.
244#[rustc_no_mir_inline]
245#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
246#[cfg(not(no_global_oom_handling))]
247fn box_new_uninit(layout: Layout) -> *mut u8 {
248    match Global.allocate(layout) {
249        Ok(ptr) => ptr.as_mut_ptr(),
250        Err(_) => handle_alloc_error(layout),
251    }
252}
253
254/// Helper for `vec!`.
255///
256/// This is unsafe, but has to be marked as safe or else we couldn't use it in `vec!`.
257#[doc(hidden)]
258#[unstable(feature = "liballoc_internals", issue = "none")]
259#[inline(always)]
260#[cfg(not(no_global_oom_handling))]
261#[rustc_diagnostic_item = "box_assume_init_into_vec_unsafe"]
262pub fn box_assume_init_into_vec_unsafe<T, const N: usize>(
263    b: Box<MaybeUninit<[T; N]>>,
264) -> crate::vec::Vec<T> {
265    unsafe { (b.assume_init() as Box<[T]>).into_vec() }
266}
267
268impl<T> Box<T> {
269    /// Allocates memory on the heap and then places `x` into it.
270    ///
271    /// This doesn't actually allocate if `T` is zero-sized.
272    ///
273    /// # Examples
274    ///
275    /// ```
276    /// let five = Box::new(5);
277    /// ```
278    #[cfg(not(no_global_oom_handling))]
279    #[inline(always)]
280    #[stable(feature = "rust1", since = "1.0.0")]
281    #[must_use]
282    #[rustc_diagnostic_item = "box_new"]
283    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
284    pub fn new(x: T) -> Self {
285        // This is `Box::new_uninit` but inlined to avoid build time regressions.
286        let ptr = box_new_uninit(<T as SizedTypeProperties>::LAYOUT) as *mut T;
287        // Nothing below can panic so we do not have to worry about deallocating `ptr`.
288        // SAFETY: we just allocated the box to store `x`.
289        unsafe { core::intrinsics::write_via_move(ptr, x) };
290        // SAFETY: we just initialized `b`.
291        unsafe { mem::transmute(ptr) }
292    }
293
294    /// Constructs a new box with uninitialized contents.
295    ///
296    /// # Examples
297    ///
298    /// ```
299    /// let mut five = Box::<u32>::new_uninit();
300    /// // Deferred initialization:
301    /// five.write(5);
302    /// let five = unsafe { five.assume_init() };
303    ///
304    /// assert_eq!(*five, 5)
305    /// ```
306    #[cfg(not(no_global_oom_handling))]
307    #[stable(feature = "new_uninit", since = "1.82.0")]
308    #[must_use]
309    #[inline(always)]
310    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
311    pub fn new_uninit() -> Box<mem::MaybeUninit<T>> {
312        // This is the same as `Self::new_uninit_in(Global)`, but manually inlined (just like
313        // `Box::new`).
314
315        // SAFETY:
316        // - If `allocate` succeeds, the returned pointer exactly matches what `Box` needs.
317        unsafe { mem::transmute(box_new_uninit(<T as SizedTypeProperties>::LAYOUT)) }
318    }
319
320    /// Constructs a new `Box` with uninitialized contents, with the memory
321    /// being filled with `0` bytes.
322    ///
323    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
324    /// of this method.
325    ///
326    /// # Examples
327    ///
328    /// ```
329    /// let zero = Box::<u32>::new_zeroed();
330    /// let zero = unsafe { zero.assume_init() };
331    ///
332    /// assert_eq!(*zero, 0)
333    /// ```
334    ///
335    /// [zeroed]: mem::MaybeUninit::zeroed
336    #[cfg(not(no_global_oom_handling))]
337    #[inline]
338    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
339    #[must_use]
340    pub fn new_zeroed() -> Box<mem::MaybeUninit<T>> {
341        Self::new_zeroed_in(Global)
342    }
343
344    /// Constructs a new `Pin<Box<T>>`. If `T` does not implement [`Unpin`], then
345    /// `x` will be pinned in memory and unable to be moved.
346    ///
347    /// Constructing and pinning of the `Box` can also be done in two steps: `Box::pin(x)`
348    /// does the same as <code>[Box::into_pin]\([Box::new]\(x))</code>. Consider using
349    /// [`into_pin`](Box::into_pin) if you already have a `Box<T>`, or if you want to
350    /// construct a (pinned) `Box` in a different way than with [`Box::new`].
351    #[cfg(not(no_global_oom_handling))]
352    #[stable(feature = "pin", since = "1.33.0")]
353    #[must_use]
354    #[inline(always)]
355    pub fn pin(x: T) -> Pin<Box<T>> {
356        Box::new(x).into()
357    }
358
359    /// Allocates memory on the heap then places `x` into it,
360    /// returning an error if the allocation fails
361    ///
362    /// This doesn't actually allocate if `T` is zero-sized.
363    ///
364    /// # Examples
365    ///
366    /// ```
367    /// #![feature(allocator_api)]
368    ///
369    /// let five = Box::try_new(5)?;
370    /// # Ok::<(), std::alloc::AllocError>(())
371    /// ```
372    #[unstable(feature = "allocator_api", issue = "32838")]
373    #[inline]
374    pub fn try_new(x: T) -> Result<Self, AllocError> {
375        Self::try_new_in(x, Global)
376    }
377
378    /// Constructs a new box with uninitialized contents on the heap,
379    /// returning an error if the allocation fails
380    ///
381    /// # Examples
382    ///
383    /// ```
384    /// #![feature(allocator_api)]
385    ///
386    /// let mut five = Box::<u32>::try_new_uninit()?;
387    /// // Deferred initialization:
388    /// five.write(5);
389    /// let five = unsafe { five.assume_init() };
390    ///
391    /// assert_eq!(*five, 5);
392    /// # Ok::<(), std::alloc::AllocError>(())
393    /// ```
394    #[unstable(feature = "allocator_api", issue = "32838")]
395    #[inline]
396    pub fn try_new_uninit() -> Result<Box<mem::MaybeUninit<T>>, AllocError> {
397        Box::try_new_uninit_in(Global)
398    }
399
400    /// Constructs a new `Box` with uninitialized contents, with the memory
401    /// being filled with `0` bytes on the heap
402    ///
403    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
404    /// of this method.
405    ///
406    /// # Examples
407    ///
408    /// ```
409    /// #![feature(allocator_api)]
410    ///
411    /// let zero = Box::<u32>::try_new_zeroed()?;
412    /// let zero = unsafe { zero.assume_init() };
413    ///
414    /// assert_eq!(*zero, 0);
415    /// # Ok::<(), std::alloc::AllocError>(())
416    /// ```
417    ///
418    /// [zeroed]: mem::MaybeUninit::zeroed
419    #[unstable(feature = "allocator_api", issue = "32838")]
420    #[inline]
421    pub fn try_new_zeroed() -> Result<Box<mem::MaybeUninit<T>>, AllocError> {
422        Box::try_new_zeroed_in(Global)
423    }
424
425    /// Maps the value in a box, reusing the allocation if possible.
426    ///
427    /// `f` is called on the value in the box, and the result is returned, also boxed.
428    ///
429    /// Note: this is an associated function, which means that you have
430    /// to call it as `Box::map(b, f)` instead of `b.map(f)`. This
431    /// is so that there is no conflict with a method on the inner type.
432    ///
433    /// # Examples
434    ///
435    /// ```
436    /// #![feature(smart_pointer_try_map)]
437    ///
438    /// let b = Box::new(7);
439    /// let new = Box::map(b, |i| i + 7);
440    /// assert_eq!(*new, 14);
441    /// ```
442    #[cfg(not(no_global_oom_handling))]
443    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
444    pub fn map<U>(this: Self, f: impl FnOnce(T) -> U) -> Box<U> {
445        if size_of::<T>() == size_of::<U>() && align_of::<T>() == align_of::<U>() {
446            let (value, allocation) = Box::take(this);
447            Box::write(
448                unsafe { mem::transmute::<Box<MaybeUninit<T>>, Box<MaybeUninit<U>>>(allocation) },
449                f(value),
450            )
451        } else {
452            Box::new(f(*this))
453        }
454    }
455
456    /// Attempts to map the value in a box, reusing the allocation if possible.
457    ///
458    /// `f` is called on the value in the box, and if the operation succeeds, the result is
459    /// returned, also boxed.
460    ///
461    /// Note: this is an associated function, which means that you have
462    /// to call it as `Box::try_map(b, f)` instead of `b.try_map(f)`. This
463    /// is so that there is no conflict with a method on the inner type.
464    ///
465    /// # Examples
466    ///
467    /// ```
468    /// #![feature(smart_pointer_try_map)]
469    ///
470    /// let b = Box::new(7);
471    /// let new = Box::try_map(b, u32::try_from).unwrap();
472    /// assert_eq!(*new, 7);
473    /// ```
474    #[cfg(not(no_global_oom_handling))]
475    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
476    pub fn try_map<R>(
477        this: Self,
478        f: impl FnOnce(T) -> R,
479    ) -> <R::Residual as Residual<Box<R::Output>>>::TryType
480    where
481        R: Try,
482        R::Residual: Residual<Box<R::Output>>,
483    {
484        if size_of::<T>() == size_of::<R::Output>() && align_of::<T>() == align_of::<R::Output>() {
485            let (value, allocation) = Box::take(this);
486            try {
487                Box::write(
488                    unsafe {
489                        mem::transmute::<Box<MaybeUninit<T>>, Box<MaybeUninit<R::Output>>>(
490                            allocation,
491                        )
492                    },
493                    f(value)?,
494                )
495            }
496        } else {
497            try { Box::new(f(*this)?) }
498        }
499    }
500}
501
502impl<T, A: Allocator> Box<T, A> {
503    /// Allocates memory in the given allocator then places `x` into it.
504    ///
505    /// This doesn't actually allocate if `T` is zero-sized.
506    ///
507    /// # Examples
508    ///
509    /// ```
510    /// #![feature(allocator_api)]
511    ///
512    /// use std::alloc::System;
513    ///
514    /// let five = Box::new_in(5, System);
515    /// ```
516    #[cfg(not(no_global_oom_handling))]
517    #[unstable(feature = "allocator_api", issue = "32838")]
518    #[must_use]
519    #[inline]
520    pub fn new_in(x: T, alloc: A) -> Self
521    where
522        A: Allocator,
523    {
524        let mut boxed = Self::new_uninit_in(alloc);
525        boxed.write(x);
526        unsafe { boxed.assume_init() }
527    }
528
529    /// Allocates memory in the given allocator then places `x` into it,
530    /// returning an error if the allocation fails
531    ///
532    /// This doesn't actually allocate if `T` is zero-sized.
533    ///
534    /// # Examples
535    ///
536    /// ```
537    /// #![feature(allocator_api)]
538    ///
539    /// use std::alloc::System;
540    ///
541    /// let five = Box::try_new_in(5, System)?;
542    /// # Ok::<(), std::alloc::AllocError>(())
543    /// ```
544    #[unstable(feature = "allocator_api", issue = "32838")]
545    #[inline]
546    pub fn try_new_in(x: T, alloc: A) -> Result<Self, AllocError>
547    where
548        A: Allocator,
549    {
550        let mut boxed = Self::try_new_uninit_in(alloc)?;
551        boxed.write(x);
552        unsafe { Ok(boxed.assume_init()) }
553    }
554
555    /// Constructs a new box with uninitialized contents in the provided allocator.
556    ///
557    /// # Examples
558    ///
559    /// ```
560    /// #![feature(allocator_api)]
561    ///
562    /// use std::alloc::System;
563    ///
564    /// let mut five = Box::<u32, _>::new_uninit_in(System);
565    /// // Deferred initialization:
566    /// five.write(5);
567    /// let five = unsafe { five.assume_init() };
568    ///
569    /// assert_eq!(*five, 5)
570    /// ```
571    #[unstable(feature = "allocator_api", issue = "32838")]
572    #[cfg(not(no_global_oom_handling))]
573    #[must_use]
574    pub fn new_uninit_in(alloc: A) -> Box<mem::MaybeUninit<T>, A>
575    where
576        A: Allocator,
577    {
578        let layout = Layout::new::<mem::MaybeUninit<T>>();
579        // NOTE: Prefer match over unwrap_or_else since closure sometimes not inlineable.
580        // That would make code size bigger.
581        match Box::try_new_uninit_in(alloc) {
582            Ok(m) => m,
583            Err(_) => handle_alloc_error(layout),
584        }
585    }
586
587    /// Constructs a new box with uninitialized contents in the provided allocator,
588    /// returning an error if the allocation fails
589    ///
590    /// # Examples
591    ///
592    /// ```
593    /// #![feature(allocator_api)]
594    ///
595    /// use std::alloc::System;
596    ///
597    /// let mut five = Box::<u32, _>::try_new_uninit_in(System)?;
598    /// // Deferred initialization:
599    /// five.write(5);
600    /// let five = unsafe { five.assume_init() };
601    ///
602    /// assert_eq!(*five, 5);
603    /// # Ok::<(), std::alloc::AllocError>(())
604    /// ```
605    #[unstable(feature = "allocator_api", issue = "32838")]
606    pub fn try_new_uninit_in(alloc: A) -> Result<Box<mem::MaybeUninit<T>, A>, AllocError>
607    where
608        A: Allocator,
609    {
610        let ptr = if T::IS_ZST {
611            NonNull::dangling()
612        } else {
613            let layout = Layout::new::<mem::MaybeUninit<T>>();
614            alloc.allocate(layout)?.cast()
615        };
616        unsafe { Ok(Box::from_raw_in(ptr.as_ptr(), alloc)) }
617    }
618
619    /// Constructs a new `Box` with uninitialized contents, with the memory
620    /// being filled with `0` bytes in the provided allocator.
621    ///
622    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
623    /// of this method.
624    ///
625    /// # Examples
626    ///
627    /// ```
628    /// #![feature(allocator_api)]
629    ///
630    /// use std::alloc::System;
631    ///
632    /// let zero = Box::<u32, _>::new_zeroed_in(System);
633    /// let zero = unsafe { zero.assume_init() };
634    ///
635    /// assert_eq!(*zero, 0)
636    /// ```
637    ///
638    /// [zeroed]: mem::MaybeUninit::zeroed
639    #[unstable(feature = "allocator_api", issue = "32838")]
640    #[cfg(not(no_global_oom_handling))]
641    #[must_use]
642    pub fn new_zeroed_in(alloc: A) -> Box<mem::MaybeUninit<T>, A>
643    where
644        A: Allocator,
645    {
646        let layout = Layout::new::<mem::MaybeUninit<T>>();
647        // NOTE: Prefer match over unwrap_or_else since closure sometimes not inlineable.
648        // That would make code size bigger.
649        match Box::try_new_zeroed_in(alloc) {
650            Ok(m) => m,
651            Err(_) => handle_alloc_error(layout),
652        }
653    }
654
655    /// Constructs a new `Box` with uninitialized contents, with the memory
656    /// being filled with `0` bytes in the provided allocator,
657    /// returning an error if the allocation fails,
658    ///
659    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
660    /// of this method.
661    ///
662    /// # Examples
663    ///
664    /// ```
665    /// #![feature(allocator_api)]
666    ///
667    /// use std::alloc::System;
668    ///
669    /// let zero = Box::<u32, _>::try_new_zeroed_in(System)?;
670    /// let zero = unsafe { zero.assume_init() };
671    ///
672    /// assert_eq!(*zero, 0);
673    /// # Ok::<(), std::alloc::AllocError>(())
674    /// ```
675    ///
676    /// [zeroed]: mem::MaybeUninit::zeroed
677    #[unstable(feature = "allocator_api", issue = "32838")]
678    pub fn try_new_zeroed_in(alloc: A) -> Result<Box<mem::MaybeUninit<T>, A>, AllocError>
679    where
680        A: Allocator,
681    {
682        let ptr = if T::IS_ZST {
683            NonNull::dangling()
684        } else {
685            let layout = Layout::new::<mem::MaybeUninit<T>>();
686            alloc.allocate_zeroed(layout)?.cast()
687        };
688        unsafe { Ok(Box::from_raw_in(ptr.as_ptr(), alloc)) }
689    }
690
691    /// Constructs a new `Pin<Box<T, A>>`. If `T` does not implement [`Unpin`], then
692    /// `x` will be pinned in memory and unable to be moved.
693    ///
694    /// Constructing and pinning of the `Box` can also be done in two steps: `Box::pin_in(x, alloc)`
695    /// does the same as <code>[Box::into_pin]\([Box::new_in]\(x, alloc))</code>. Consider using
696    /// [`into_pin`](Box::into_pin) if you already have a `Box<T, A>`, or if you want to
697    /// construct a (pinned) `Box` in a different way than with [`Box::new_in`].
698    #[cfg(not(no_global_oom_handling))]
699    #[unstable(feature = "allocator_api", issue = "32838")]
700    #[must_use]
701    #[inline(always)]
702    pub fn pin_in(x: T, alloc: A) -> Pin<Self>
703    where
704        A: 'static + Allocator,
705    {
706        Self::into_pin(Self::new_in(x, alloc))
707    }
708
709    /// Converts a `Box<T>` into a `Box<[T]>`
710    ///
711    /// This conversion does not allocate on the heap and happens in place.
712    #[unstable(feature = "box_into_boxed_slice", issue = "71582")]
713    pub fn into_boxed_slice(boxed: Self) -> Box<[T], A> {
714        let (raw, alloc) = Box::into_raw_with_allocator(boxed);
715        unsafe { Box::from_raw_in(raw as *mut [T; 1], alloc) }
716    }
717
718    /// Consumes the `Box`, returning the wrapped value.
719    ///
720    /// # Examples
721    ///
722    /// ```
723    /// #![feature(box_into_inner)]
724    ///
725    /// let c = Box::new(5);
726    ///
727    /// assert_eq!(Box::into_inner(c), 5);
728    /// ```
729    #[unstable(feature = "box_into_inner", issue = "80437")]
730    #[inline]
731    pub fn into_inner(boxed: Self) -> T {
732        *boxed
733    }
734
735    /// Consumes the `Box` without consuming its allocation, returning the wrapped value and a `Box`
736    /// to the uninitialized memory where the wrapped value used to live.
737    ///
738    /// This can be used together with [`write`](Box::write) to reuse the allocation for multiple
739    /// boxed values.
740    ///
741    /// # Examples
742    ///
743    /// ```
744    /// #![feature(box_take)]
745    ///
746    /// let c = Box::new(5);
747    ///
748    /// // take the value out of the box
749    /// let (value, uninit) = Box::take(c);
750    /// assert_eq!(value, 5);
751    ///
752    /// // reuse the box for a second value
753    /// let c = Box::write(uninit, 6);
754    /// assert_eq!(*c, 6);
755    /// ```
756    #[unstable(feature = "box_take", issue = "147212")]
757    pub fn take(boxed: Self) -> (T, Box<mem::MaybeUninit<T>, A>) {
758        unsafe {
759            let (raw, alloc) = Box::into_non_null_with_allocator(boxed);
760            let value = raw.read();
761            let uninit = Box::from_non_null_in(raw.cast_uninit(), alloc);
762            (value, uninit)
763        }
764    }
765}
766
767impl<T: ?Sized + CloneToUninit> Box<T> {
768    /// Allocates memory on the heap then clones `src` into it.
769    ///
770    /// This doesn't actually allocate if `src` is zero-sized.
771    ///
772    /// # Examples
773    ///
774    /// ```
775    /// #![feature(clone_from_ref)]
776    ///
777    /// let hello: Box<str> = Box::clone_from_ref("hello");
778    /// ```
779    #[cfg(not(no_global_oom_handling))]
780    #[unstable(feature = "clone_from_ref", issue = "149075")]
781    #[must_use]
782    #[inline]
783    pub fn clone_from_ref(src: &T) -> Box<T> {
784        Box::clone_from_ref_in(src, Global)
785    }
786
787    /// Allocates memory on the heap then clones `src` into it, returning an error if allocation fails.
788    ///
789    /// This doesn't actually allocate if `src` is zero-sized.
790    ///
791    /// # Examples
792    ///
793    /// ```
794    /// #![feature(clone_from_ref)]
795    /// #![feature(allocator_api)]
796    ///
797    /// let hello: Box<str> = Box::try_clone_from_ref("hello")?;
798    /// # Ok::<(), std::alloc::AllocError>(())
799    /// ```
800    #[unstable(feature = "clone_from_ref", issue = "149075")]
801    //#[unstable(feature = "allocator_api", issue = "32838")]
802    #[must_use]
803    #[inline]
804    pub fn try_clone_from_ref(src: &T) -> Result<Box<T>, AllocError> {
805        Box::try_clone_from_ref_in(src, Global)
806    }
807}
808
809impl<T: ?Sized + CloneToUninit, A: Allocator> Box<T, A> {
810    /// Allocates memory in the given allocator then clones `src` into it.
811    ///
812    /// This doesn't actually allocate if `src` is zero-sized.
813    ///
814    /// # Examples
815    ///
816    /// ```
817    /// #![feature(clone_from_ref)]
818    /// #![feature(allocator_api)]
819    ///
820    /// use std::alloc::System;
821    ///
822    /// let hello: Box<str, System> = Box::clone_from_ref_in("hello", System);
823    /// ```
824    #[cfg(not(no_global_oom_handling))]
825    #[unstable(feature = "clone_from_ref", issue = "149075")]
826    //#[unstable(feature = "allocator_api", issue = "32838")]
827    #[must_use]
828    #[inline]
829    pub fn clone_from_ref_in(src: &T, alloc: A) -> Box<T, A> {
830        let layout = Layout::for_value::<T>(src);
831        match Box::try_clone_from_ref_in(src, alloc) {
832            Ok(bx) => bx,
833            Err(_) => handle_alloc_error(layout),
834        }
835    }
836
837    /// Allocates memory in the given allocator then clones `src` into it, returning an error if allocation fails.
838    ///
839    /// This doesn't actually allocate if `src` is zero-sized.
840    ///
841    /// # Examples
842    ///
843    /// ```
844    /// #![feature(clone_from_ref)]
845    /// #![feature(allocator_api)]
846    ///
847    /// use std::alloc::System;
848    ///
849    /// let hello: Box<str, System> = Box::try_clone_from_ref_in("hello", System)?;
850    /// # Ok::<(), std::alloc::AllocError>(())
851    /// ```
852    #[unstable(feature = "clone_from_ref", issue = "149075")]
853    //#[unstable(feature = "allocator_api", issue = "32838")]
854    #[must_use]
855    #[inline]
856    pub fn try_clone_from_ref_in(src: &T, alloc: A) -> Result<Box<T, A>, AllocError> {
857        struct DeallocDropGuard<'a, A: Allocator>(Layout, &'a A, NonNull<u8>);
858        impl<'a, A: Allocator> Drop for DeallocDropGuard<'a, A> {
859            fn drop(&mut self) {
860                let &mut DeallocDropGuard(layout, alloc, ptr) = self;
861                // Safety: `ptr` was allocated by `*alloc` with layout `layout`
862                unsafe {
863                    alloc.deallocate(ptr, layout);
864                }
865            }
866        }
867        let layout = Layout::for_value::<T>(src);
868        let (ptr, guard) = if layout.size() == 0 {
869            (layout.dangling_ptr(), None)
870        } else {
871            // Safety: layout is non-zero-sized
872            let ptr = alloc.allocate(layout)?.cast();
873            (ptr, Some(DeallocDropGuard(layout, &alloc, ptr)))
874        };
875        let ptr = ptr.as_ptr();
876        // Safety: `*ptr` is newly allocated, correctly aligned to `align_of_val(src)`,
877        // and is valid for writes for `size_of_val(src)`.
878        // If this panics, then `guard` will deallocate for us (if allocation occuured)
879        unsafe {
880            <T as CloneToUninit>::clone_to_uninit(src, ptr);
881        }
882        // Defuse the deallocate guard
883        core::mem::forget(guard);
884        // Safety: We just initialized `*ptr` as a clone of `src`
885        Ok(unsafe { Box::from_raw_in(ptr.with_metadata_of(src), alloc) })
886    }
887}
888
889impl<T> Box<[T]> {
890    /// Constructs a new boxed slice with uninitialized contents.
891    ///
892    /// # Examples
893    ///
894    /// ```
895    /// let mut values = Box::<[u32]>::new_uninit_slice(3);
896    /// // Deferred initialization:
897    /// values[0].write(1);
898    /// values[1].write(2);
899    /// values[2].write(3);
900    /// let values = unsafe { values.assume_init() };
901    ///
902    /// assert_eq!(*values, [1, 2, 3])
903    /// ```
904    #[cfg(not(no_global_oom_handling))]
905    #[stable(feature = "new_uninit", since = "1.82.0")]
906    #[must_use]
907    pub fn new_uninit_slice(len: usize) -> Box<[mem::MaybeUninit<T>]> {
908        unsafe { RawVec::with_capacity(len).into_box(len) }
909    }
910
911    /// Constructs a new boxed slice with uninitialized contents, with the memory
912    /// being filled with `0` bytes.
913    ///
914    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
915    /// of this method.
916    ///
917    /// # Examples
918    ///
919    /// ```
920    /// let values = Box::<[u32]>::new_zeroed_slice(3);
921    /// let values = unsafe { values.assume_init() };
922    ///
923    /// assert_eq!(*values, [0, 0, 0])
924    /// ```
925    ///
926    /// [zeroed]: mem::MaybeUninit::zeroed
927    #[cfg(not(no_global_oom_handling))]
928    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
929    #[must_use]
930    pub fn new_zeroed_slice(len: usize) -> Box<[mem::MaybeUninit<T>]> {
931        unsafe { RawVec::with_capacity_zeroed(len).into_box(len) }
932    }
933
934    /// Constructs a new boxed slice with uninitialized contents. Returns an error if
935    /// the allocation fails.
936    ///
937    /// # Examples
938    ///
939    /// ```
940    /// #![feature(allocator_api)]
941    ///
942    /// let mut values = Box::<[u32]>::try_new_uninit_slice(3)?;
943    /// // Deferred initialization:
944    /// values[0].write(1);
945    /// values[1].write(2);
946    /// values[2].write(3);
947    /// let values = unsafe { values.assume_init() };
948    ///
949    /// assert_eq!(*values, [1, 2, 3]);
950    /// # Ok::<(), std::alloc::AllocError>(())
951    /// ```
952    #[unstable(feature = "allocator_api", issue = "32838")]
953    #[inline]
954    pub fn try_new_uninit_slice(len: usize) -> Result<Box<[mem::MaybeUninit<T>]>, AllocError> {
955        let ptr = if T::IS_ZST || len == 0 {
956            NonNull::dangling()
957        } else {
958            let layout = match Layout::array::<mem::MaybeUninit<T>>(len) {
959                Ok(l) => l,
960                Err(_) => return Err(AllocError),
961            };
962            Global.allocate(layout)?.cast()
963        };
964        unsafe { Ok(RawVec::from_raw_parts_in(ptr.as_ptr(), len, Global).into_box(len)) }
965    }
966
967    /// Constructs a new boxed slice with uninitialized contents, with the memory
968    /// being filled with `0` bytes. Returns an error if the allocation fails.
969    ///
970    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
971    /// of this method.
972    ///
973    /// # Examples
974    ///
975    /// ```
976    /// #![feature(allocator_api)]
977    ///
978    /// let values = Box::<[u32]>::try_new_zeroed_slice(3)?;
979    /// let values = unsafe { values.assume_init() };
980    ///
981    /// assert_eq!(*values, [0, 0, 0]);
982    /// # Ok::<(), std::alloc::AllocError>(())
983    /// ```
984    ///
985    /// [zeroed]: mem::MaybeUninit::zeroed
986    #[unstable(feature = "allocator_api", issue = "32838")]
987    #[inline]
988    pub fn try_new_zeroed_slice(len: usize) -> Result<Box<[mem::MaybeUninit<T>]>, AllocError> {
989        let ptr = if T::IS_ZST || len == 0 {
990            NonNull::dangling()
991        } else {
992            let layout = match Layout::array::<mem::MaybeUninit<T>>(len) {
993                Ok(l) => l,
994                Err(_) => return Err(AllocError),
995            };
996            Global.allocate_zeroed(layout)?.cast()
997        };
998        unsafe { Ok(RawVec::from_raw_parts_in(ptr.as_ptr(), len, Global).into_box(len)) }
999    }
1000
1001    /// Converts the boxed slice into a boxed array.
1002    ///
1003    /// This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.
1004    ///
1005    /// If `N` is not exactly equal to the length of `self`, then this method returns `None`.
1006    #[unstable(feature = "alloc_slice_into_array", issue = "148082")]
1007    #[inline]
1008    #[must_use]
1009    pub fn into_array<const N: usize>(self) -> Option<Box<[T; N]>> {
1010        if self.len() == N {
1011            let ptr = Self::into_raw(self) as *mut [T; N];
1012
1013            // SAFETY: The underlying array of a slice has the exact same layout as an actual array `[T; N]` if `N` is equal to the slice's length.
1014            let me = unsafe { Box::from_raw(ptr) };
1015            Some(me)
1016        } else {
1017            None
1018        }
1019    }
1020}
1021
1022impl<T, A: Allocator> Box<[T], A> {
1023    /// Constructs a new boxed slice with uninitialized contents in the provided allocator.
1024    ///
1025    /// # Examples
1026    ///
1027    /// ```
1028    /// #![feature(allocator_api)]
1029    ///
1030    /// use std::alloc::System;
1031    ///
1032    /// let mut values = Box::<[u32], _>::new_uninit_slice_in(3, System);
1033    /// // Deferred initialization:
1034    /// values[0].write(1);
1035    /// values[1].write(2);
1036    /// values[2].write(3);
1037    /// let values = unsafe { values.assume_init() };
1038    ///
1039    /// assert_eq!(*values, [1, 2, 3])
1040    /// ```
1041    #[cfg(not(no_global_oom_handling))]
1042    #[unstable(feature = "allocator_api", issue = "32838")]
1043    #[must_use]
1044    pub fn new_uninit_slice_in(len: usize, alloc: A) -> Box<[mem::MaybeUninit<T>], A> {
1045        unsafe { RawVec::with_capacity_in(len, alloc).into_box(len) }
1046    }
1047
1048    /// Constructs a new boxed slice with uninitialized contents in the provided allocator,
1049    /// with the memory being filled with `0` bytes.
1050    ///
1051    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
1052    /// of this method.
1053    ///
1054    /// # Examples
1055    ///
1056    /// ```
1057    /// #![feature(allocator_api)]
1058    ///
1059    /// use std::alloc::System;
1060    ///
1061    /// let values = Box::<[u32], _>::new_zeroed_slice_in(3, System);
1062    /// let values = unsafe { values.assume_init() };
1063    ///
1064    /// assert_eq!(*values, [0, 0, 0])
1065    /// ```
1066    ///
1067    /// [zeroed]: mem::MaybeUninit::zeroed
1068    #[cfg(not(no_global_oom_handling))]
1069    #[unstable(feature = "allocator_api", issue = "32838")]
1070    #[must_use]
1071    pub fn new_zeroed_slice_in(len: usize, alloc: A) -> Box<[mem::MaybeUninit<T>], A> {
1072        unsafe { RawVec::with_capacity_zeroed_in(len, alloc).into_box(len) }
1073    }
1074
1075    /// Constructs a new boxed slice with uninitialized contents in the provided allocator. Returns an error if
1076    /// the allocation fails.
1077    ///
1078    /// # Examples
1079    ///
1080    /// ```
1081    /// #![feature(allocator_api)]
1082    ///
1083    /// use std::alloc::System;
1084    ///
1085    /// let mut values = Box::<[u32], _>::try_new_uninit_slice_in(3, System)?;
1086    /// // Deferred initialization:
1087    /// values[0].write(1);
1088    /// values[1].write(2);
1089    /// values[2].write(3);
1090    /// let values = unsafe { values.assume_init() };
1091    ///
1092    /// assert_eq!(*values, [1, 2, 3]);
1093    /// # Ok::<(), std::alloc::AllocError>(())
1094    /// ```
1095    #[unstable(feature = "allocator_api", issue = "32838")]
1096    #[inline]
1097    pub fn try_new_uninit_slice_in(
1098        len: usize,
1099        alloc: A,
1100    ) -> Result<Box<[mem::MaybeUninit<T>], A>, AllocError> {
1101        let ptr = if T::IS_ZST || len == 0 {
1102            NonNull::dangling()
1103        } else {
1104            let layout = match Layout::array::<mem::MaybeUninit<T>>(len) {
1105                Ok(l) => l,
1106                Err(_) => return Err(AllocError),
1107            };
1108            alloc.allocate(layout)?.cast()
1109        };
1110        unsafe { Ok(RawVec::from_raw_parts_in(ptr.as_ptr(), len, alloc).into_box(len)) }
1111    }
1112
1113    /// Constructs a new boxed slice with uninitialized contents in the provided allocator, with the memory
1114    /// being filled with `0` bytes. Returns an error if the allocation fails.
1115    ///
1116    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
1117    /// of this method.
1118    ///
1119    /// # Examples
1120    ///
1121    /// ```
1122    /// #![feature(allocator_api)]
1123    ///
1124    /// use std::alloc::System;
1125    ///
1126    /// let values = Box::<[u32], _>::try_new_zeroed_slice_in(3, System)?;
1127    /// let values = unsafe { values.assume_init() };
1128    ///
1129    /// assert_eq!(*values, [0, 0, 0]);
1130    /// # Ok::<(), std::alloc::AllocError>(())
1131    /// ```
1132    ///
1133    /// [zeroed]: mem::MaybeUninit::zeroed
1134    #[unstable(feature = "allocator_api", issue = "32838")]
1135    #[inline]
1136    pub fn try_new_zeroed_slice_in(
1137        len: usize,
1138        alloc: A,
1139    ) -> Result<Box<[mem::MaybeUninit<T>], A>, AllocError> {
1140        let ptr = if T::IS_ZST || len == 0 {
1141            NonNull::dangling()
1142        } else {
1143            let layout = match Layout::array::<mem::MaybeUninit<T>>(len) {
1144                Ok(l) => l,
1145                Err(_) => return Err(AllocError),
1146            };
1147            alloc.allocate_zeroed(layout)?.cast()
1148        };
1149        unsafe { Ok(RawVec::from_raw_parts_in(ptr.as_ptr(), len, alloc).into_box(len)) }
1150    }
1151}
1152
1153impl<T, A: Allocator> Box<mem::MaybeUninit<T>, A> {
1154    /// Converts to `Box<T, A>`.
1155    ///
1156    /// # Safety
1157    ///
1158    /// As with [`MaybeUninit::assume_init`],
1159    /// it is up to the caller to guarantee that the value
1160    /// really is in an initialized state.
1161    /// Calling this when the content is not yet fully initialized
1162    /// causes immediate undefined behavior.
1163    ///
1164    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1165    ///
1166    /// # Examples
1167    ///
1168    /// ```
1169    /// let mut five = Box::<u32>::new_uninit();
1170    /// // Deferred initialization:
1171    /// five.write(5);
1172    /// let five: Box<u32> = unsafe { five.assume_init() };
1173    ///
1174    /// assert_eq!(*five, 5)
1175    /// ```
1176    #[stable(feature = "new_uninit", since = "1.82.0")]
1177    #[inline(always)]
1178    pub unsafe fn assume_init(self) -> Box<T, A> {
1179        // This is used in the `vec!` macro, so we optimize for minimal IR generation
1180        // even in debug builds.
1181        // SAFETY: `Box<T>` and `Box<MaybeUninit<T>>` have the same layout.
1182        unsafe { core::intrinsics::transmute_unchecked(self) }
1183    }
1184
1185    /// Writes the value and converts to `Box<T, A>`.
1186    ///
1187    /// This method converts the box similarly to [`Box::assume_init`] but
1188    /// writes `value` into it before conversion thus guaranteeing safety.
1189    /// In some scenarios use of this method may improve performance because
1190    /// the compiler may be able to optimize copying from stack.
1191    ///
1192    /// # Examples
1193    ///
1194    /// ```
1195    /// let big_box = Box::<[usize; 1024]>::new_uninit();
1196    ///
1197    /// let mut array = [0; 1024];
1198    /// for (i, place) in array.iter_mut().enumerate() {
1199    ///     *place = i;
1200    /// }
1201    ///
1202    /// // The optimizer may be able to elide this copy, so previous code writes
1203    /// // to heap directly.
1204    /// let big_box = Box::write(big_box, array);
1205    ///
1206    /// for (i, x) in big_box.iter().enumerate() {
1207    ///     assert_eq!(*x, i);
1208    /// }
1209    /// ```
1210    #[stable(feature = "box_uninit_write", since = "1.87.0")]
1211    #[inline]
1212    pub fn write(mut boxed: Self, value: T) -> Box<T, A> {
1213        unsafe {
1214            (*boxed).write(value);
1215            boxed.assume_init()
1216        }
1217    }
1218}
1219
1220impl<T, A: Allocator> Box<[mem::MaybeUninit<T>], A> {
1221    /// Converts to `Box<[T], A>`.
1222    ///
1223    /// # Safety
1224    ///
1225    /// As with [`MaybeUninit::assume_init`],
1226    /// it is up to the caller to guarantee that the values
1227    /// really are in an initialized state.
1228    /// Calling this when the content is not yet fully initialized
1229    /// causes immediate undefined behavior.
1230    ///
1231    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1232    ///
1233    /// # Examples
1234    ///
1235    /// ```
1236    /// let mut values = Box::<[u32]>::new_uninit_slice(3);
1237    /// // Deferred initialization:
1238    /// values[0].write(1);
1239    /// values[1].write(2);
1240    /// values[2].write(3);
1241    /// let values = unsafe { values.assume_init() };
1242    ///
1243    /// assert_eq!(*values, [1, 2, 3])
1244    /// ```
1245    #[stable(feature = "new_uninit", since = "1.82.0")]
1246    #[inline]
1247    pub unsafe fn assume_init(self) -> Box<[T], A> {
1248        let (raw, alloc) = Box::into_raw_with_allocator(self);
1249        unsafe { Box::from_raw_in(raw as *mut [T], alloc) }
1250    }
1251}
1252
1253impl<T: ?Sized> Box<T> {
1254    /// Constructs a box from a raw pointer.
1255    ///
1256    /// After calling this function, the raw pointer is owned by the
1257    /// resulting `Box`. Specifically, the `Box` destructor will call
1258    /// the destructor of `T` and free the allocated memory. For this
1259    /// to be safe, the memory must have been allocated in accordance
1260    /// with the [memory layout] used by `Box` .
1261    ///
1262    /// # Safety
1263    ///
1264    /// This function is unsafe because improper use may lead to
1265    /// memory problems. For example, a double-free may occur if the
1266    /// function is called twice on the same raw pointer.
1267    ///
1268    /// The raw pointer must point to a block of memory allocated by the global allocator.
1269    ///
1270    /// The safety conditions are described in the [memory layout] section.
1271    ///
1272    /// # Examples
1273    ///
1274    /// Recreate a `Box` which was previously converted to a raw pointer
1275    /// using [`Box::into_raw`]:
1276    /// ```
1277    /// let x = Box::new(5);
1278    /// let ptr = Box::into_raw(x);
1279    /// let x = unsafe { Box::from_raw(ptr) };
1280    /// ```
1281    /// Manually create a `Box` from scratch by using the global allocator:
1282    /// ```
1283    /// use std::alloc::{alloc, Layout};
1284    ///
1285    /// unsafe {
1286    ///     let ptr = alloc(Layout::new::<i32>()) as *mut i32;
1287    ///     // In general .write is required to avoid attempting to destruct
1288    ///     // the (uninitialized) previous contents of `ptr`, though for this
1289    ///     // simple example `*ptr = 5` would have worked as well.
1290    ///     ptr.write(5);
1291    ///     let x = Box::from_raw(ptr);
1292    /// }
1293    /// ```
1294    ///
1295    /// [memory layout]: self#memory-layout
1296    #[stable(feature = "box_raw", since = "1.4.0")]
1297    #[inline]
1298    #[must_use = "call `drop(Box::from_raw(ptr))` if you intend to drop the `Box`"]
1299    pub unsafe fn from_raw(raw: *mut T) -> Self {
1300        unsafe { Self::from_raw_in(raw, Global) }
1301    }
1302
1303    /// Constructs a box from a `NonNull` pointer.
1304    ///
1305    /// After calling this function, the `NonNull` pointer is owned by
1306    /// the resulting `Box`. Specifically, the `Box` destructor will call
1307    /// the destructor of `T` and free the allocated memory. For this
1308    /// to be safe, the memory must have been allocated in accordance
1309    /// with the [memory layout] used by `Box` .
1310    ///
1311    /// # Safety
1312    ///
1313    /// This function is unsafe because improper use may lead to
1314    /// memory problems. For example, a double-free may occur if the
1315    /// function is called twice on the same `NonNull` pointer.
1316    ///
1317    /// The non-null pointer must point to a block of memory allocated by the global allocator.
1318    ///
1319    /// The safety conditions are described in the [memory layout] section.
1320    ///
1321    /// # Examples
1322    ///
1323    /// Recreate a `Box` which was previously converted to a `NonNull`
1324    /// pointer using [`Box::into_non_null`]:
1325    /// ```
1326    /// #![feature(box_vec_non_null)]
1327    ///
1328    /// let x = Box::new(5);
1329    /// let non_null = Box::into_non_null(x);
1330    /// let x = unsafe { Box::from_non_null(non_null) };
1331    /// ```
1332    /// Manually create a `Box` from scratch by using the global allocator:
1333    /// ```
1334    /// #![feature(box_vec_non_null)]
1335    ///
1336    /// use std::alloc::{alloc, Layout};
1337    /// use std::ptr::NonNull;
1338    ///
1339    /// unsafe {
1340    ///     let non_null = NonNull::new(alloc(Layout::new::<i32>()).cast::<i32>())
1341    ///         .expect("allocation failed");
1342    ///     // In general .write is required to avoid attempting to destruct
1343    ///     // the (uninitialized) previous contents of `non_null`.
1344    ///     non_null.write(5);
1345    ///     let x = Box::from_non_null(non_null);
1346    /// }
1347    /// ```
1348    ///
1349    /// [memory layout]: self#memory-layout
1350    #[unstable(feature = "box_vec_non_null", issue = "130364")]
1351    #[inline]
1352    #[must_use = "call `drop(Box::from_non_null(ptr))` if you intend to drop the `Box`"]
1353    pub unsafe fn from_non_null(ptr: NonNull<T>) -> Self {
1354        unsafe { Self::from_raw(ptr.as_ptr()) }
1355    }
1356
1357    /// Consumes the `Box`, returning a wrapped raw pointer.
1358    ///
1359    /// The pointer will be properly aligned and non-null.
1360    ///
1361    /// After calling this function, the caller is responsible for the
1362    /// memory previously managed by the `Box`. In particular, the
1363    /// caller should properly destroy `T` and release the memory, taking
1364    /// into account the [memory layout] used by `Box`. The easiest way to
1365    /// do this is to convert the raw pointer back into a `Box` with the
1366    /// [`Box::from_raw`] function, allowing the `Box` destructor to perform
1367    /// the cleanup.
1368    ///
1369    /// Note: this is an associated function, which means that you have
1370    /// to call it as `Box::into_raw(b)` instead of `b.into_raw()`. This
1371    /// is so that there is no conflict with a method on the inner type.
1372    ///
1373    /// # Examples
1374    /// Converting the raw pointer back into a `Box` with [`Box::from_raw`]
1375    /// for automatic cleanup:
1376    /// ```
1377    /// let x = Box::new(String::from("Hello"));
1378    /// let ptr = Box::into_raw(x);
1379    /// let x = unsafe { Box::from_raw(ptr) };
1380    /// ```
1381    /// Manual cleanup by explicitly running the destructor and deallocating
1382    /// the memory:
1383    /// ```
1384    /// use std::alloc::{dealloc, Layout};
1385    /// use std::ptr;
1386    ///
1387    /// let x = Box::new(String::from("Hello"));
1388    /// let ptr = Box::into_raw(x);
1389    /// unsafe {
1390    ///     ptr::drop_in_place(ptr);
1391    ///     dealloc(ptr as *mut u8, Layout::new::<String>());
1392    /// }
1393    /// ```
1394    /// Note: This is equivalent to the following:
1395    /// ```
1396    /// let x = Box::new(String::from("Hello"));
1397    /// let ptr = Box::into_raw(x);
1398    /// unsafe {
1399    ///     drop(Box::from_raw(ptr));
1400    /// }
1401    /// ```
1402    ///
1403    /// [memory layout]: self#memory-layout
1404    #[must_use = "losing the pointer will leak memory"]
1405    #[stable(feature = "box_raw", since = "1.4.0")]
1406    #[inline]
1407    pub fn into_raw(b: Self) -> *mut T {
1408        // Avoid `into_raw_with_allocator` as that interacts poorly with Miri's Stacked Borrows.
1409        let mut b = mem::ManuallyDrop::new(b);
1410        // We go through the built-in deref for `Box`, which is crucial for Miri to recognize this
1411        // operation for it's alias tracking.
1412        &raw mut **b
1413    }
1414
1415    /// Consumes the `Box`, returning a wrapped `NonNull` pointer.
1416    ///
1417    /// The pointer will be properly aligned.
1418    ///
1419    /// After calling this function, the caller is responsible for the
1420    /// memory previously managed by the `Box`. In particular, the
1421    /// caller should properly destroy `T` and release the memory, taking
1422    /// into account the [memory layout] used by `Box`. The easiest way to
1423    /// do this is to convert the `NonNull` pointer back into a `Box` with the
1424    /// [`Box::from_non_null`] function, allowing the `Box` destructor to
1425    /// perform the cleanup.
1426    ///
1427    /// Note: this is an associated function, which means that you have
1428    /// to call it as `Box::into_non_null(b)` instead of `b.into_non_null()`.
1429    /// This is so that there is no conflict with a method on the inner type.
1430    ///
1431    /// # Examples
1432    /// Converting the `NonNull` pointer back into a `Box` with [`Box::from_non_null`]
1433    /// for automatic cleanup:
1434    /// ```
1435    /// #![feature(box_vec_non_null)]
1436    ///
1437    /// let x = Box::new(String::from("Hello"));
1438    /// let non_null = Box::into_non_null(x);
1439    /// let x = unsafe { Box::from_non_null(non_null) };
1440    /// ```
1441    /// Manual cleanup by explicitly running the destructor and deallocating
1442    /// the memory:
1443    /// ```
1444    /// #![feature(box_vec_non_null)]
1445    ///
1446    /// use std::alloc::{dealloc, Layout};
1447    ///
1448    /// let x = Box::new(String::from("Hello"));
1449    /// let non_null = Box::into_non_null(x);
1450    /// unsafe {
1451    ///     non_null.drop_in_place();
1452    ///     dealloc(non_null.as_ptr().cast::<u8>(), Layout::new::<String>());
1453    /// }
1454    /// ```
1455    /// Note: This is equivalent to the following:
1456    /// ```
1457    /// #![feature(box_vec_non_null)]
1458    ///
1459    /// let x = Box::new(String::from("Hello"));
1460    /// let non_null = Box::into_non_null(x);
1461    /// unsafe {
1462    ///     drop(Box::from_non_null(non_null));
1463    /// }
1464    /// ```
1465    ///
1466    /// [memory layout]: self#memory-layout
1467    #[must_use = "losing the pointer will leak memory"]
1468    #[unstable(feature = "box_vec_non_null", issue = "130364")]
1469    #[inline]
1470    pub fn into_non_null(b: Self) -> NonNull<T> {
1471        // SAFETY: `Box` is guaranteed to be non-null.
1472        unsafe { NonNull::new_unchecked(Self::into_raw(b)) }
1473    }
1474}
1475
1476impl<T: ?Sized, A: Allocator> Box<T, A> {
1477    /// Constructs a box from a raw pointer in the given allocator.
1478    ///
1479    /// After calling this function, the raw pointer is owned by the
1480    /// resulting `Box`. Specifically, the `Box` destructor will call
1481    /// the destructor of `T` and free the allocated memory. For this
1482    /// to be safe, the memory must have been allocated in accordance
1483    /// with the [memory layout] used by `Box` .
1484    ///
1485    /// # Safety
1486    ///
1487    /// This function is unsafe because improper use may lead to
1488    /// memory problems. For example, a double-free may occur if the
1489    /// function is called twice on the same raw pointer.
1490    ///
1491    /// The raw pointer must point to a block of memory allocated by `alloc`.
1492    ///
1493    /// # Examples
1494    ///
1495    /// Recreate a `Box` which was previously converted to a raw pointer
1496    /// using [`Box::into_raw_with_allocator`]:
1497    /// ```
1498    /// #![feature(allocator_api)]
1499    ///
1500    /// use std::alloc::System;
1501    ///
1502    /// let x = Box::new_in(5, System);
1503    /// let (ptr, alloc) = Box::into_raw_with_allocator(x);
1504    /// let x = unsafe { Box::from_raw_in(ptr, alloc) };
1505    /// ```
1506    /// Manually create a `Box` from scratch by using the system allocator:
1507    /// ```
1508    /// #![feature(allocator_api, slice_ptr_get)]
1509    ///
1510    /// use std::alloc::{Allocator, Layout, System};
1511    ///
1512    /// unsafe {
1513    ///     let ptr = System.allocate(Layout::new::<i32>())?.as_mut_ptr() as *mut i32;
1514    ///     // In general .write is required to avoid attempting to destruct
1515    ///     // the (uninitialized) previous contents of `ptr`, though for this
1516    ///     // simple example `*ptr = 5` would have worked as well.
1517    ///     ptr.write(5);
1518    ///     let x = Box::from_raw_in(ptr, System);
1519    /// }
1520    /// # Ok::<(), std::alloc::AllocError>(())
1521    /// ```
1522    ///
1523    /// [memory layout]: self#memory-layout
1524    #[unstable(feature = "allocator_api", issue = "32838")]
1525    #[inline]
1526    pub unsafe fn from_raw_in(raw: *mut T, alloc: A) -> Self {
1527        Box(unsafe { Unique::new_unchecked(raw) }, alloc)
1528    }
1529
1530    /// Constructs a box from a `NonNull` pointer in the given allocator.
1531    ///
1532    /// After calling this function, the `NonNull` pointer is owned by
1533    /// the resulting `Box`. Specifically, the `Box` destructor will call
1534    /// the destructor of `T` and free the allocated memory. For this
1535    /// to be safe, the memory must have been allocated in accordance
1536    /// with the [memory layout] used by `Box` .
1537    ///
1538    /// # Safety
1539    ///
1540    /// This function is unsafe because improper use may lead to
1541    /// memory problems. For example, a double-free may occur if the
1542    /// function is called twice on the same raw pointer.
1543    ///
1544    /// The non-null pointer must point to a block of memory allocated by `alloc`.
1545    ///
1546    /// # Examples
1547    ///
1548    /// Recreate a `Box` which was previously converted to a `NonNull` pointer
1549    /// using [`Box::into_non_null_with_allocator`]:
1550    /// ```
1551    /// #![feature(allocator_api)]
1552    ///
1553    /// use std::alloc::System;
1554    ///
1555    /// let x = Box::new_in(5, System);
1556    /// let (non_null, alloc) = Box::into_non_null_with_allocator(x);
1557    /// let x = unsafe { Box::from_non_null_in(non_null, alloc) };
1558    /// ```
1559    /// Manually create a `Box` from scratch by using the system allocator:
1560    /// ```
1561    /// #![feature(allocator_api)]
1562    ///
1563    /// use std::alloc::{Allocator, Layout, System};
1564    ///
1565    /// unsafe {
1566    ///     let non_null = System.allocate(Layout::new::<i32>())?.cast::<i32>();
1567    ///     // In general .write is required to avoid attempting to destruct
1568    ///     // the (uninitialized) previous contents of `non_null`.
1569    ///     non_null.write(5);
1570    ///     let x = Box::from_non_null_in(non_null, System);
1571    /// }
1572    /// # Ok::<(), std::alloc::AllocError>(())
1573    /// ```
1574    ///
1575    /// [memory layout]: self#memory-layout
1576    #[unstable(feature = "allocator_api", issue = "32838")]
1577    // #[unstable(feature = "box_vec_non_null", issue = "130364")]
1578    #[inline]
1579    pub unsafe fn from_non_null_in(raw: NonNull<T>, alloc: A) -> Self {
1580        // SAFETY: guaranteed by the caller.
1581        unsafe { Box::from_raw_in(raw.as_ptr(), alloc) }
1582    }
1583
1584    /// Consumes the `Box`, returning a wrapped raw pointer and the allocator.
1585    ///
1586    /// The pointer will be properly aligned and non-null.
1587    ///
1588    /// After calling this function, the caller is responsible for the
1589    /// memory previously managed by the `Box`. In particular, the
1590    /// caller should properly destroy `T` and release the memory, taking
1591    /// into account the [memory layout] used by `Box`. The easiest way to
1592    /// do this is to convert the raw pointer back into a `Box` with the
1593    /// [`Box::from_raw_in`] function, allowing the `Box` destructor to perform
1594    /// the cleanup.
1595    ///
1596    /// Note: this is an associated function, which means that you have
1597    /// to call it as `Box::into_raw_with_allocator(b)` instead of `b.into_raw_with_allocator()`. This
1598    /// is so that there is no conflict with a method on the inner type.
1599    ///
1600    /// # Examples
1601    /// Converting the raw pointer back into a `Box` with [`Box::from_raw_in`]
1602    /// for automatic cleanup:
1603    /// ```
1604    /// #![feature(allocator_api)]
1605    ///
1606    /// use std::alloc::System;
1607    ///
1608    /// let x = Box::new_in(String::from("Hello"), System);
1609    /// let (ptr, alloc) = Box::into_raw_with_allocator(x);
1610    /// let x = unsafe { Box::from_raw_in(ptr, alloc) };
1611    /// ```
1612    /// Manual cleanup by explicitly running the destructor and deallocating
1613    /// the memory:
1614    /// ```
1615    /// #![feature(allocator_api)]
1616    ///
1617    /// use std::alloc::{Allocator, Layout, System};
1618    /// use std::ptr::{self, NonNull};
1619    ///
1620    /// let x = Box::new_in(String::from("Hello"), System);
1621    /// let (ptr, alloc) = Box::into_raw_with_allocator(x);
1622    /// unsafe {
1623    ///     ptr::drop_in_place(ptr);
1624    ///     let non_null = NonNull::new_unchecked(ptr);
1625    ///     alloc.deallocate(non_null.cast(), Layout::new::<String>());
1626    /// }
1627    /// ```
1628    ///
1629    /// [memory layout]: self#memory-layout
1630    #[must_use = "losing the pointer will leak memory"]
1631    #[unstable(feature = "allocator_api", issue = "32838")]
1632    #[inline]
1633    pub fn into_raw_with_allocator(b: Self) -> (*mut T, A) {
1634        let mut b = mem::ManuallyDrop::new(b);
1635        // We carefully get the raw pointer out in a way that Miri's aliasing model understands what
1636        // is happening: using the primitive "deref" of `Box`. In case `A` is *not* `Global`, we
1637        // want *no* aliasing requirements here!
1638        // In case `A` *is* `Global`, this does not quite have the right behavior; `into_raw`
1639        // works around that.
1640        let ptr = &raw mut **b;
1641        let alloc = unsafe { ptr::read(&b.1) };
1642        (ptr, alloc)
1643    }
1644
1645    /// Consumes the `Box`, returning a wrapped `NonNull` pointer and the allocator.
1646    ///
1647    /// The pointer will be properly aligned.
1648    ///
1649    /// After calling this function, the caller is responsible for the
1650    /// memory previously managed by the `Box`. In particular, the
1651    /// caller should properly destroy `T` and release the memory, taking
1652    /// into account the [memory layout] used by `Box`. The easiest way to
1653    /// do this is to convert the `NonNull` pointer back into a `Box` with the
1654    /// [`Box::from_non_null_in`] function, allowing the `Box` destructor to
1655    /// perform the cleanup.
1656    ///
1657    /// Note: this is an associated function, which means that you have
1658    /// to call it as `Box::into_non_null_with_allocator(b)` instead of
1659    /// `b.into_non_null_with_allocator()`. This is so that there is no
1660    /// conflict with a method on the inner type.
1661    ///
1662    /// # Examples
1663    /// Converting the `NonNull` pointer back into a `Box` with
1664    /// [`Box::from_non_null_in`] for automatic cleanup:
1665    /// ```
1666    /// #![feature(allocator_api)]
1667    ///
1668    /// use std::alloc::System;
1669    ///
1670    /// let x = Box::new_in(String::from("Hello"), System);
1671    /// let (non_null, alloc) = Box::into_non_null_with_allocator(x);
1672    /// let x = unsafe { Box::from_non_null_in(non_null, alloc) };
1673    /// ```
1674    /// Manual cleanup by explicitly running the destructor and deallocating
1675    /// the memory:
1676    /// ```
1677    /// #![feature(allocator_api)]
1678    ///
1679    /// use std::alloc::{Allocator, Layout, System};
1680    ///
1681    /// let x = Box::new_in(String::from("Hello"), System);
1682    /// let (non_null, alloc) = Box::into_non_null_with_allocator(x);
1683    /// unsafe {
1684    ///     non_null.drop_in_place();
1685    ///     alloc.deallocate(non_null.cast::<u8>(), Layout::new::<String>());
1686    /// }
1687    /// ```
1688    ///
1689    /// [memory layout]: self#memory-layout
1690    #[must_use = "losing the pointer will leak memory"]
1691    #[unstable(feature = "allocator_api", issue = "32838")]
1692    // #[unstable(feature = "box_vec_non_null", issue = "130364")]
1693    #[inline]
1694    pub fn into_non_null_with_allocator(b: Self) -> (NonNull<T>, A) {
1695        let (ptr, alloc) = Box::into_raw_with_allocator(b);
1696        // SAFETY: `Box` is guaranteed to be non-null.
1697        unsafe { (NonNull::new_unchecked(ptr), alloc) }
1698    }
1699
1700    #[unstable(
1701        feature = "ptr_internals",
1702        issue = "none",
1703        reason = "use `Box::leak(b).into()` or `Unique::from(Box::leak(b))` instead"
1704    )]
1705    #[inline]
1706    #[doc(hidden)]
1707    pub fn into_unique(b: Self) -> (Unique<T>, A) {
1708        let (ptr, alloc) = Box::into_raw_with_allocator(b);
1709        unsafe { (Unique::from(&mut *ptr), alloc) }
1710    }
1711
1712    /// Returns a raw mutable pointer to the `Box`'s contents.
1713    ///
1714    /// The caller must ensure that the `Box` outlives the pointer this
1715    /// function returns, or else it will end up dangling.
1716    ///
1717    /// This method guarantees that for the purpose of the aliasing model, this method
1718    /// does not materialize a reference to the underlying memory, and thus the returned pointer
1719    /// will remain valid when mixed with other calls to [`as_ptr`] and [`as_mut_ptr`].
1720    /// Note that calling other methods that materialize references to the memory
1721    /// may still invalidate this pointer.
1722    /// See the example below for how this guarantee can be used.
1723    ///
1724    /// # Examples
1725    ///
1726    /// Due to the aliasing guarantee, the following code is legal:
1727    ///
1728    /// ```rust
1729    /// #![feature(box_as_ptr)]
1730    ///
1731    /// unsafe {
1732    ///     let mut b = Box::new(0);
1733    ///     let ptr1 = Box::as_mut_ptr(&mut b);
1734    ///     ptr1.write(1);
1735    ///     let ptr2 = Box::as_mut_ptr(&mut b);
1736    ///     ptr2.write(2);
1737    ///     // Notably, the write to `ptr2` did *not* invalidate `ptr1`:
1738    ///     ptr1.write(3);
1739    /// }
1740    /// ```
1741    ///
1742    /// [`as_mut_ptr`]: Self::as_mut_ptr
1743    /// [`as_ptr`]: Self::as_ptr
1744    #[unstable(feature = "box_as_ptr", issue = "129090")]
1745    #[rustc_never_returns_null_ptr]
1746    #[rustc_as_ptr]
1747    #[inline]
1748    pub fn as_mut_ptr(b: &mut Self) -> *mut T {
1749        // This is a primitive deref, not going through `DerefMut`, and therefore not materializing
1750        // any references.
1751        &raw mut **b
1752    }
1753
1754    /// Returns a raw pointer to the `Box`'s contents.
1755    ///
1756    /// The caller must ensure that the `Box` outlives the pointer this
1757    /// function returns, or else it will end up dangling.
1758    ///
1759    /// The caller must also ensure that the memory the pointer (non-transitively) points to
1760    /// is never written to (except inside an `UnsafeCell`) using this pointer or any pointer
1761    /// derived from it. If you need to mutate the contents of the `Box`, use [`as_mut_ptr`].
1762    ///
1763    /// This method guarantees that for the purpose of the aliasing model, this method
1764    /// does not materialize a reference to the underlying memory, and thus the returned pointer
1765    /// will remain valid when mixed with other calls to [`as_ptr`] and [`as_mut_ptr`].
1766    /// Note that calling other methods that materialize mutable references to the memory,
1767    /// as well as writing to this memory, may still invalidate this pointer.
1768    /// See the example below for how this guarantee can be used.
1769    ///
1770    /// # Examples
1771    ///
1772    /// Due to the aliasing guarantee, the following code is legal:
1773    ///
1774    /// ```rust
1775    /// #![feature(box_as_ptr)]
1776    ///
1777    /// unsafe {
1778    ///     let mut v = Box::new(0);
1779    ///     let ptr1 = Box::as_ptr(&v);
1780    ///     let ptr2 = Box::as_mut_ptr(&mut v);
1781    ///     let _val = ptr2.read();
1782    ///     // No write to this memory has happened yet, so `ptr1` is still valid.
1783    ///     let _val = ptr1.read();
1784    ///     // However, once we do a write...
1785    ///     ptr2.write(1);
1786    ///     // ... `ptr1` is no longer valid.
1787    ///     // This would be UB: let _val = ptr1.read();
1788    /// }
1789    /// ```
1790    ///
1791    /// [`as_mut_ptr`]: Self::as_mut_ptr
1792    /// [`as_ptr`]: Self::as_ptr
1793    #[unstable(feature = "box_as_ptr", issue = "129090")]
1794    #[rustc_never_returns_null_ptr]
1795    #[rustc_as_ptr]
1796    #[inline]
1797    pub fn as_ptr(b: &Self) -> *const T {
1798        // This is a primitive deref, not going through `DerefMut`, and therefore not materializing
1799        // any references.
1800        &raw const **b
1801    }
1802
1803    /// Returns a reference to the underlying allocator.
1804    ///
1805    /// Note: this is an associated function, which means that you have
1806    /// to call it as `Box::allocator(&b)` instead of `b.allocator()`. This
1807    /// is so that there is no conflict with a method on the inner type.
1808    #[unstable(feature = "allocator_api", issue = "32838")]
1809    #[inline]
1810    pub fn allocator(b: &Self) -> &A {
1811        &b.1
1812    }
1813
1814    /// Consumes and leaks the `Box`, returning a mutable reference,
1815    /// `&'a mut T`.
1816    ///
1817    /// Note that the type `T` must outlive the chosen lifetime `'a`. If the type
1818    /// has only static references, or none at all, then this may be chosen to be
1819    /// `'static`.
1820    ///
1821    /// This function is mainly useful for data that lives for the remainder of
1822    /// the program's life. Dropping the returned reference will cause a memory
1823    /// leak. If this is not acceptable, the reference should first be wrapped
1824    /// with the [`Box::from_raw`] function producing a `Box`. This `Box` can
1825    /// then be dropped which will properly destroy `T` and release the
1826    /// allocated memory.
1827    ///
1828    /// Note: this is an associated function, which means that you have
1829    /// to call it as `Box::leak(b)` instead of `b.leak()`. This
1830    /// is so that there is no conflict with a method on the inner type.
1831    ///
1832    /// # Examples
1833    ///
1834    /// Simple usage:
1835    ///
1836    /// ```
1837    /// let x = Box::new(41);
1838    /// let static_ref: &'static mut usize = Box::leak(x);
1839    /// *static_ref += 1;
1840    /// assert_eq!(*static_ref, 42);
1841    /// # // FIXME(https://github.com/rust-lang/miri/issues/3670):
1842    /// # // use -Zmiri-disable-leak-check instead of unleaking in tests meant to leak.
1843    /// # drop(unsafe { Box::from_raw(static_ref) });
1844    /// ```
1845    ///
1846    /// Unsized data:
1847    ///
1848    /// ```
1849    /// let x = vec![1, 2, 3].into_boxed_slice();
1850    /// let static_ref = Box::leak(x);
1851    /// static_ref[0] = 4;
1852    /// assert_eq!(*static_ref, [4, 2, 3]);
1853    /// # // FIXME(https://github.com/rust-lang/miri/issues/3670):
1854    /// # // use -Zmiri-disable-leak-check instead of unleaking in tests meant to leak.
1855    /// # drop(unsafe { Box::from_raw(static_ref) });
1856    /// ```
1857    #[stable(feature = "box_leak", since = "1.26.0")]
1858    #[inline]
1859    pub fn leak<'a>(b: Self) -> &'a mut T
1860    where
1861        A: 'a,
1862    {
1863        let (ptr, alloc) = Box::into_raw_with_allocator(b);
1864        mem::forget(alloc);
1865        unsafe { &mut *ptr }
1866    }
1867
1868    /// Converts a `Box<T>` into a `Pin<Box<T>>`. If `T` does not implement [`Unpin`], then
1869    /// `*boxed` will be pinned in memory and unable to be moved.
1870    ///
1871    /// This conversion does not allocate on the heap and happens in place.
1872    ///
1873    /// This is also available via [`From`].
1874    ///
1875    /// Constructing and pinning a `Box` with <code>Box::into_pin([Box::new]\(x))</code>
1876    /// can also be written more concisely using <code>[Box::pin]\(x)</code>.
1877    /// This `into_pin` method is useful if you already have a `Box<T>`, or you are
1878    /// constructing a (pinned) `Box` in a different way than with [`Box::new`].
1879    ///
1880    /// # Notes
1881    ///
1882    /// It's not recommended that crates add an impl like `From<Box<T>> for Pin<T>`,
1883    /// as it'll introduce an ambiguity when calling `Pin::from`.
1884    /// A demonstration of such a poor impl is shown below.
1885    ///
1886    /// ```compile_fail
1887    /// # use std::pin::Pin;
1888    /// struct Foo; // A type defined in this crate.
1889    /// impl From<Box<()>> for Pin<Foo> {
1890    ///     fn from(_: Box<()>) -> Pin<Foo> {
1891    ///         Pin::new(Foo)
1892    ///     }
1893    /// }
1894    ///
1895    /// let foo = Box::new(());
1896    /// let bar = Pin::from(foo);
1897    /// ```
1898    #[stable(feature = "box_into_pin", since = "1.63.0")]
1899    pub fn into_pin(boxed: Self) -> Pin<Self>
1900    where
1901        A: 'static,
1902    {
1903        // It's not possible to move or replace the insides of a `Pin<Box<T>>`
1904        // when `T: !Unpin`, so it's safe to pin it directly without any
1905        // additional requirements.
1906        unsafe { Pin::new_unchecked(boxed) }
1907    }
1908}
1909
1910#[stable(feature = "rust1", since = "1.0.0")]
1911unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for Box<T, A> {
1912    #[inline]
1913    fn drop(&mut self) {
1914        // the T in the Box is dropped by the compiler before the destructor is run
1915
1916        let ptr = self.0;
1917
1918        unsafe {
1919            let layout = Layout::for_value_raw(ptr.as_ptr());
1920            if layout.size() != 0 {
1921                self.1.deallocate(From::from(ptr.cast()), layout);
1922            }
1923        }
1924    }
1925}
1926
1927#[cfg(not(no_global_oom_handling))]
1928#[stable(feature = "rust1", since = "1.0.0")]
1929impl<T: Default> Default for Box<T> {
1930    /// Creates a `Box<T>`, with the `Default` value for `T`.
1931    #[inline]
1932    fn default() -> Self {
1933        let mut x: Box<mem::MaybeUninit<T>> = Box::new_uninit();
1934        unsafe {
1935            // SAFETY: `x` is valid for writing and has the same layout as `T`.
1936            // If `T::default()` panics, dropping `x` will just deallocate the Box as `MaybeUninit<T>`
1937            // does not have a destructor.
1938            //
1939            // We use `ptr::write` as `MaybeUninit::write` creates
1940            // extra stack copies of `T` in debug mode.
1941            //
1942            // See https://github.com/rust-lang/rust/issues/136043 for more context.
1943            ptr::write(&raw mut *x as *mut T, T::default());
1944            // SAFETY: `x` was just initialized above.
1945            x.assume_init()
1946        }
1947    }
1948}
1949
1950#[cfg(not(no_global_oom_handling))]
1951#[stable(feature = "rust1", since = "1.0.0")]
1952impl<T> Default for Box<[T]> {
1953    /// Creates an empty `[T]` inside a `Box`.
1954    #[inline]
1955    fn default() -> Self {
1956        let ptr: Unique<[T]> = Unique::<[T; 0]>::dangling();
1957        Box(ptr, Global)
1958    }
1959}
1960
1961#[cfg(not(no_global_oom_handling))]
1962#[stable(feature = "default_box_extra", since = "1.17.0")]
1963impl Default for Box<str> {
1964    #[inline]
1965    fn default() -> Self {
1966        // SAFETY: This is the same as `Unique::cast<U>` but with an unsized `U = str`.
1967        let ptr: Unique<str> = unsafe {
1968            let bytes: Unique<[u8]> = Unique::<[u8; 0]>::dangling();
1969            Unique::new_unchecked(bytes.as_ptr() as *mut str)
1970        };
1971        Box(ptr, Global)
1972    }
1973}
1974
1975#[cfg(not(no_global_oom_handling))]
1976#[stable(feature = "pin_default_impls", since = "1.91.0")]
1977impl<T> Default for Pin<Box<T>>
1978where
1979    T: ?Sized,
1980    Box<T>: Default,
1981{
1982    #[inline]
1983    fn default() -> Self {
1984        Box::into_pin(Box::<T>::default())
1985    }
1986}
1987
1988#[cfg(not(no_global_oom_handling))]
1989#[stable(feature = "rust1", since = "1.0.0")]
1990impl<T: Clone, A: Allocator + Clone> Clone for Box<T, A> {
1991    /// Returns a new box with a `clone()` of this box's contents.
1992    ///
1993    /// # Examples
1994    ///
1995    /// ```
1996    /// let x = Box::new(5);
1997    /// let y = x.clone();
1998    ///
1999    /// // The value is the same
2000    /// assert_eq!(x, y);
2001    ///
2002    /// // But they are unique objects
2003    /// assert_ne!(&*x as *const i32, &*y as *const i32);
2004    /// ```
2005    #[inline]
2006    fn clone(&self) -> Self {
2007        // Pre-allocate memory to allow writing the cloned value directly.
2008        let mut boxed = Self::new_uninit_in(self.1.clone());
2009        unsafe {
2010            (**self).clone_to_uninit(boxed.as_mut_ptr().cast());
2011            boxed.assume_init()
2012        }
2013    }
2014
2015    /// Copies `source`'s contents into `self` without creating a new allocation.
2016    ///
2017    /// # Examples
2018    ///
2019    /// ```
2020    /// let x = Box::new(5);
2021    /// let mut y = Box::new(10);
2022    /// let yp: *const i32 = &*y;
2023    ///
2024    /// y.clone_from(&x);
2025    ///
2026    /// // The value is the same
2027    /// assert_eq!(x, y);
2028    ///
2029    /// // And no allocation occurred
2030    /// assert_eq!(yp, &*y);
2031    /// ```
2032    #[inline]
2033    fn clone_from(&mut self, source: &Self) {
2034        (**self).clone_from(&(**source));
2035    }
2036}
2037
2038#[cfg(not(no_global_oom_handling))]
2039#[stable(feature = "box_slice_clone", since = "1.3.0")]
2040impl<T: Clone, A: Allocator + Clone> Clone for Box<[T], A> {
2041    fn clone(&self) -> Self {
2042        let alloc = Box::allocator(self).clone();
2043        self.to_vec_in(alloc).into_boxed_slice()
2044    }
2045
2046    /// Copies `source`'s contents into `self` without creating a new allocation,
2047    /// so long as the two are of the same length.
2048    ///
2049    /// # Examples
2050    ///
2051    /// ```
2052    /// let x = Box::new([5, 6, 7]);
2053    /// let mut y = Box::new([8, 9, 10]);
2054    /// let yp: *const [i32] = &*y;
2055    ///
2056    /// y.clone_from(&x);
2057    ///
2058    /// // The value is the same
2059    /// assert_eq!(x, y);
2060    ///
2061    /// // And no allocation occurred
2062    /// assert_eq!(yp, &*y);
2063    /// ```
2064    fn clone_from(&mut self, source: &Self) {
2065        if self.len() == source.len() {
2066            self.clone_from_slice(&source);
2067        } else {
2068            *self = source.clone();
2069        }
2070    }
2071}
2072
2073#[cfg(not(no_global_oom_handling))]
2074#[stable(feature = "box_slice_clone", since = "1.3.0")]
2075impl Clone for Box<str> {
2076    fn clone(&self) -> Self {
2077        // this makes a copy of the data
2078        let buf: Box<[u8]> = self.as_bytes().into();
2079        unsafe { from_boxed_utf8_unchecked(buf) }
2080    }
2081}
2082
2083#[stable(feature = "rust1", since = "1.0.0")]
2084impl<T: ?Sized + PartialEq, A: Allocator> PartialEq for Box<T, A> {
2085    #[inline]
2086    fn eq(&self, other: &Self) -> bool {
2087        PartialEq::eq(&**self, &**other)
2088    }
2089    #[inline]
2090    fn ne(&self, other: &Self) -> bool {
2091        PartialEq::ne(&**self, &**other)
2092    }
2093}
2094
2095#[stable(feature = "rust1", since = "1.0.0")]
2096impl<T: ?Sized + PartialOrd, A: Allocator> PartialOrd for Box<T, A> {
2097    #[inline]
2098    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
2099        PartialOrd::partial_cmp(&**self, &**other)
2100    }
2101    #[inline]
2102    fn lt(&self, other: &Self) -> bool {
2103        PartialOrd::lt(&**self, &**other)
2104    }
2105    #[inline]
2106    fn le(&self, other: &Self) -> bool {
2107        PartialOrd::le(&**self, &**other)
2108    }
2109    #[inline]
2110    fn ge(&self, other: &Self) -> bool {
2111        PartialOrd::ge(&**self, &**other)
2112    }
2113    #[inline]
2114    fn gt(&self, other: &Self) -> bool {
2115        PartialOrd::gt(&**self, &**other)
2116    }
2117}
2118
2119#[stable(feature = "rust1", since = "1.0.0")]
2120impl<T: ?Sized + Ord, A: Allocator> Ord for Box<T, A> {
2121    #[inline]
2122    fn cmp(&self, other: &Self) -> Ordering {
2123        Ord::cmp(&**self, &**other)
2124    }
2125}
2126
2127#[stable(feature = "rust1", since = "1.0.0")]
2128impl<T: ?Sized + Eq, A: Allocator> Eq for Box<T, A> {}
2129
2130#[stable(feature = "rust1", since = "1.0.0")]
2131impl<T: ?Sized + Hash, A: Allocator> Hash for Box<T, A> {
2132    fn hash<H: Hasher>(&self, state: &mut H) {
2133        (**self).hash(state);
2134    }
2135}
2136
2137#[stable(feature = "indirect_hasher_impl", since = "1.22.0")]
2138impl<T: ?Sized + Hasher, A: Allocator> Hasher for Box<T, A> {
2139    fn finish(&self) -> u64 {
2140        (**self).finish()
2141    }
2142    fn write(&mut self, bytes: &[u8]) {
2143        (**self).write(bytes)
2144    }
2145    fn write_u8(&mut self, i: u8) {
2146        (**self).write_u8(i)
2147    }
2148    fn write_u16(&mut self, i: u16) {
2149        (**self).write_u16(i)
2150    }
2151    fn write_u32(&mut self, i: u32) {
2152        (**self).write_u32(i)
2153    }
2154    fn write_u64(&mut self, i: u64) {
2155        (**self).write_u64(i)
2156    }
2157    fn write_u128(&mut self, i: u128) {
2158        (**self).write_u128(i)
2159    }
2160    fn write_usize(&mut self, i: usize) {
2161        (**self).write_usize(i)
2162    }
2163    fn write_i8(&mut self, i: i8) {
2164        (**self).write_i8(i)
2165    }
2166    fn write_i16(&mut self, i: i16) {
2167        (**self).write_i16(i)
2168    }
2169    fn write_i32(&mut self, i: i32) {
2170        (**self).write_i32(i)
2171    }
2172    fn write_i64(&mut self, i: i64) {
2173        (**self).write_i64(i)
2174    }
2175    fn write_i128(&mut self, i: i128) {
2176        (**self).write_i128(i)
2177    }
2178    fn write_isize(&mut self, i: isize) {
2179        (**self).write_isize(i)
2180    }
2181    fn write_length_prefix(&mut self, len: usize) {
2182        (**self).write_length_prefix(len)
2183    }
2184    fn write_str(&mut self, s: &str) {
2185        (**self).write_str(s)
2186    }
2187}
2188
2189#[stable(feature = "rust1", since = "1.0.0")]
2190impl<T: fmt::Display + ?Sized, A: Allocator> fmt::Display for Box<T, A> {
2191    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2192        fmt::Display::fmt(&**self, f)
2193    }
2194}
2195
2196#[stable(feature = "rust1", since = "1.0.0")]
2197impl<T: fmt::Debug + ?Sized, A: Allocator> fmt::Debug for Box<T, A> {
2198    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2199        fmt::Debug::fmt(&**self, f)
2200    }
2201}
2202
2203#[stable(feature = "rust1", since = "1.0.0")]
2204impl<T: ?Sized, A: Allocator> fmt::Pointer for Box<T, A> {
2205    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2206        // It's not possible to extract the inner Uniq directly from the Box,
2207        // instead we cast it to a *const which aliases the Unique
2208        let ptr: *const T = &**self;
2209        fmt::Pointer::fmt(&ptr, f)
2210    }
2211}
2212
2213#[stable(feature = "rust1", since = "1.0.0")]
2214impl<T: ?Sized, A: Allocator> Deref for Box<T, A> {
2215    type Target = T;
2216
2217    fn deref(&self) -> &T {
2218        &**self
2219    }
2220}
2221
2222#[stable(feature = "rust1", since = "1.0.0")]
2223impl<T: ?Sized, A: Allocator> DerefMut for Box<T, A> {
2224    fn deref_mut(&mut self) -> &mut T {
2225        &mut **self
2226    }
2227}
2228
2229#[unstable(feature = "deref_pure_trait", issue = "87121")]
2230unsafe impl<T: ?Sized, A: Allocator> DerefPure for Box<T, A> {}
2231
2232#[unstable(feature = "legacy_receiver_trait", issue = "none")]
2233impl<T: ?Sized, A: Allocator> LegacyReceiver for Box<T, A> {}
2234
2235#[stable(feature = "boxed_closure_impls", since = "1.35.0")]
2236impl<Args: Tuple, F: FnOnce<Args> + ?Sized, A: Allocator> FnOnce<Args> for Box<F, A> {
2237    type Output = <F as FnOnce<Args>>::Output;
2238
2239    extern "rust-call" fn call_once(self, args: Args) -> Self::Output {
2240        <F as FnOnce<Args>>::call_once(*self, args)
2241    }
2242}
2243
2244#[stable(feature = "boxed_closure_impls", since = "1.35.0")]
2245impl<Args: Tuple, F: FnMut<Args> + ?Sized, A: Allocator> FnMut<Args> for Box<F, A> {
2246    extern "rust-call" fn call_mut(&mut self, args: Args) -> Self::Output {
2247        <F as FnMut<Args>>::call_mut(self, args)
2248    }
2249}
2250
2251#[stable(feature = "boxed_closure_impls", since = "1.35.0")]
2252impl<Args: Tuple, F: Fn<Args> + ?Sized, A: Allocator> Fn<Args> for Box<F, A> {
2253    extern "rust-call" fn call(&self, args: Args) -> Self::Output {
2254        <F as Fn<Args>>::call(self, args)
2255    }
2256}
2257
2258#[stable(feature = "async_closure", since = "1.85.0")]
2259impl<Args: Tuple, F: AsyncFnOnce<Args> + ?Sized, A: Allocator> AsyncFnOnce<Args> for Box<F, A> {
2260    type Output = F::Output;
2261    type CallOnceFuture = F::CallOnceFuture;
2262
2263    extern "rust-call" fn async_call_once(self, args: Args) -> Self::CallOnceFuture {
2264        F::async_call_once(*self, args)
2265    }
2266}
2267
2268#[stable(feature = "async_closure", since = "1.85.0")]
2269impl<Args: Tuple, F: AsyncFnMut<Args> + ?Sized, A: Allocator> AsyncFnMut<Args> for Box<F, A> {
2270    type CallRefFuture<'a>
2271        = F::CallRefFuture<'a>
2272    where
2273        Self: 'a;
2274
2275    extern "rust-call" fn async_call_mut(&mut self, args: Args) -> Self::CallRefFuture<'_> {
2276        F::async_call_mut(self, args)
2277    }
2278}
2279
2280#[stable(feature = "async_closure", since = "1.85.0")]
2281impl<Args: Tuple, F: AsyncFn<Args> + ?Sized, A: Allocator> AsyncFn<Args> for Box<F, A> {
2282    extern "rust-call" fn async_call(&self, args: Args) -> Self::CallRefFuture<'_> {
2283        F::async_call(self, args)
2284    }
2285}
2286
2287#[unstable(feature = "coerce_unsized", issue = "18598")]
2288impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<Box<U, A>> for Box<T, A> {}
2289
2290#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2291unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for Box<T, A> {}
2292
2293// It is quite crucial that we only allow the `Global` allocator here.
2294// Handling arbitrary custom allocators (which can affect the `Box` layout heavily!)
2295// would need a lot of codegen and interpreter adjustments.
2296#[unstable(feature = "dispatch_from_dyn", issue = "none")]
2297impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<Box<U>> for Box<T, Global> {}
2298
2299#[stable(feature = "box_borrow", since = "1.1.0")]
2300impl<T: ?Sized, A: Allocator> Borrow<T> for Box<T, A> {
2301    fn borrow(&self) -> &T {
2302        &**self
2303    }
2304}
2305
2306#[stable(feature = "box_borrow", since = "1.1.0")]
2307impl<T: ?Sized, A: Allocator> BorrowMut<T> for Box<T, A> {
2308    fn borrow_mut(&mut self) -> &mut T {
2309        &mut **self
2310    }
2311}
2312
2313#[stable(since = "1.5.0", feature = "smart_ptr_as_ref")]
2314impl<T: ?Sized, A: Allocator> AsRef<T> for Box<T, A> {
2315    fn as_ref(&self) -> &T {
2316        &**self
2317    }
2318}
2319
2320#[stable(since = "1.5.0", feature = "smart_ptr_as_ref")]
2321impl<T: ?Sized, A: Allocator> AsMut<T> for Box<T, A> {
2322    fn as_mut(&mut self) -> &mut T {
2323        &mut **self
2324    }
2325}
2326
2327/* Nota bene
2328 *
2329 *  We could have chosen not to add this impl, and instead have written a
2330 *  function of Pin<Box<T>> to Pin<T>. Such a function would not be sound,
2331 *  because Box<T> implements Unpin even when T does not, as a result of
2332 *  this impl.
2333 *
2334 *  We chose this API instead of the alternative for a few reasons:
2335 *      - Logically, it is helpful to understand pinning in regard to the
2336 *        memory region being pointed to. For this reason none of the
2337 *        standard library pointer types support projecting through a pin
2338 *        (Box<T> is the only pointer type in std for which this would be
2339 *        safe.)
2340 *      - It is in practice very useful to have Box<T> be unconditionally
2341 *        Unpin because of trait objects, for which the structural auto
2342 *        trait functionality does not apply (e.g., Box<dyn Foo> would
2343 *        otherwise not be Unpin).
2344 *
2345 *  Another type with the same semantics as Box but only a conditional
2346 *  implementation of `Unpin` (where `T: Unpin`) would be valid/safe, and
2347 *  could have a method to project a Pin<T> from it.
2348 */
2349#[stable(feature = "pin", since = "1.33.0")]
2350impl<T: ?Sized, A: Allocator> Unpin for Box<T, A> {}
2351
2352#[unstable(feature = "coroutine_trait", issue = "43122")]
2353impl<G: ?Sized + Coroutine<R> + Unpin, R, A: Allocator> Coroutine<R> for Box<G, A> {
2354    type Yield = G::Yield;
2355    type Return = G::Return;
2356
2357    fn resume(mut self: Pin<&mut Self>, arg: R) -> CoroutineState<Self::Yield, Self::Return> {
2358        G::resume(Pin::new(&mut *self), arg)
2359    }
2360}
2361
2362#[unstable(feature = "coroutine_trait", issue = "43122")]
2363impl<G: ?Sized + Coroutine<R>, R, A: Allocator> Coroutine<R> for Pin<Box<G, A>>
2364where
2365    A: 'static,
2366{
2367    type Yield = G::Yield;
2368    type Return = G::Return;
2369
2370    fn resume(mut self: Pin<&mut Self>, arg: R) -> CoroutineState<Self::Yield, Self::Return> {
2371        G::resume((*self).as_mut(), arg)
2372    }
2373}
2374
2375#[stable(feature = "futures_api", since = "1.36.0")]
2376impl<F: ?Sized + Future + Unpin, A: Allocator> Future for Box<F, A> {
2377    type Output = F::Output;
2378
2379    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
2380        F::poll(Pin::new(&mut *self), cx)
2381    }
2382}
2383
2384#[stable(feature = "box_error", since = "1.8.0")]
2385impl<E: Error> Error for Box<E> {
2386    #[allow(deprecated)]
2387    fn cause(&self) -> Option<&dyn Error> {
2388        Error::cause(&**self)
2389    }
2390
2391    fn source(&self) -> Option<&(dyn Error + 'static)> {
2392        Error::source(&**self)
2393    }
2394
2395    fn provide<'b>(&'b self, request: &mut error::Request<'b>) {
2396        Error::provide(&**self, request);
2397    }
2398}
2399
2400#[unstable(feature = "allocator_api", issue = "32838")]
2401unsafe impl<T: ?Sized + Allocator, A: Allocator> Allocator for Box<T, A> {
2402    #[inline]
2403    fn allocate(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
2404        (**self).allocate(layout)
2405    }
2406
2407    #[inline]
2408    fn allocate_zeroed(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
2409        (**self).allocate_zeroed(layout)
2410    }
2411
2412    #[inline]
2413    unsafe fn deallocate(&self, ptr: NonNull<u8>, layout: Layout) {
2414        // SAFETY: the safety contract must be upheld by the caller
2415        unsafe { (**self).deallocate(ptr, layout) }
2416    }
2417
2418    #[inline]
2419    unsafe fn grow(
2420        &self,
2421        ptr: NonNull<u8>,
2422        old_layout: Layout,
2423        new_layout: Layout,
2424    ) -> Result<NonNull<[u8]>, AllocError> {
2425        // SAFETY: the safety contract must be upheld by the caller
2426        unsafe { (**self).grow(ptr, old_layout, new_layout) }
2427    }
2428
2429    #[inline]
2430    unsafe fn grow_zeroed(
2431        &self,
2432        ptr: NonNull<u8>,
2433        old_layout: Layout,
2434        new_layout: Layout,
2435    ) -> Result<NonNull<[u8]>, AllocError> {
2436        // SAFETY: the safety contract must be upheld by the caller
2437        unsafe { (**self).grow_zeroed(ptr, old_layout, new_layout) }
2438    }
2439
2440    #[inline]
2441    unsafe fn shrink(
2442        &self,
2443        ptr: NonNull<u8>,
2444        old_layout: Layout,
2445        new_layout: Layout,
2446    ) -> Result<NonNull<[u8]>, AllocError> {
2447        // SAFETY: the safety contract must be upheld by the caller
2448        unsafe { (**self).shrink(ptr, old_layout, new_layout) }
2449    }
2450}
````