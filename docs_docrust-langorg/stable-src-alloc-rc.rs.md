---
title: rc.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/rc.rs.html#2915
source: crawler
fetched_at: 2026-05-06T21:33:53.899410322-03:00
rendered_js: false
word_count: 19248
summary: This document explains the usage of Rc<T> and Weak<T> smart pointers in Rust for single-threaded heap-allocated shared ownership and lifecycle management.
tags:
    - rust
    - memory-management
    - smart-pointers
    - reference-counting
    - ownership
    - shared-state
category: concept
---

## alloc/ rc.rs

````rust
1//! Single-threaded reference-counting pointers. 'Rc' stands for 'Reference
2//! Counted'.
3//!
4//! The type [`Rc<T>`][`Rc`] provides shared ownership of a value of type `T`,
5//! allocated in the heap. Invoking [`clone`][clone] on [`Rc`] produces a new
6//! pointer to the same allocation in the heap. When the last [`Rc`] pointer to a
7//! given allocation is destroyed, the value stored in that allocation (often
8//! referred to as "inner value") is also dropped.
9//!
10//! Shared references in Rust disallow mutation by default, and [`Rc`]
11//! is no exception: you cannot generally obtain a mutable reference to
12//! something inside an [`Rc`]. If you need mutability, put a [`Cell`]
13//! or [`RefCell`] inside the [`Rc`]; see [an example of mutability
14//! inside an `Rc`][mutability].
15//!
16//! [`Rc`] uses non-atomic reference counting. This means that overhead is very
17//! low, but an [`Rc`] cannot be sent between threads, and consequently [`Rc`]
18//! does not implement [`Send`]. As a result, the Rust compiler
19//! will check *at compile time* that you are not sending [`Rc`]s between
20//! threads. If you need multi-threaded, atomic reference counting, use
21//! [`sync::Arc`][arc].
22//!
23//! The [`downgrade`][downgrade] method can be used to create a non-owning
24//! [`Weak`] pointer. A [`Weak`] pointer can be [`upgrade`][upgrade]d
25//! to an [`Rc`], but this will return [`None`] if the value stored in the allocation has
26//! already been dropped. In other words, `Weak` pointers do not keep the value
27//! inside the allocation alive; however, they *do* keep the allocation
28//! (the backing store for the inner value) alive.
29//!
30//! A cycle between [`Rc`] pointers will never be deallocated. For this reason,
31//! [`Weak`] is used to break cycles. For example, a tree could have strong
32//! [`Rc`] pointers from parent nodes to children, and [`Weak`] pointers from
33//! children back to their parents.
34//!
35//! `Rc<T>` automatically dereferences to `T` (via the [`Deref`] trait),
36//! so you can call `T`'s methods on a value of type [`Rc<T>`][`Rc`]. To avoid name
37//! clashes with `T`'s methods, the methods of [`Rc<T>`][`Rc`] itself are associated
38//! functions, called using [fully qualified syntax]:
39//!
40//! ```
41//! use std::rc::Rc;
42//!
43//! let my_rc = Rc::new(());
44//! let my_weak = Rc::downgrade(&my_rc);
45//! ```
46//!
47//! `Rc<T>`'s implementations of traits like `Clone` may also be called using
48//! fully qualified syntax. Some people prefer to use fully qualified syntax,
49//! while others prefer using method-call syntax.
50//!
51//! ```
52//! use std::rc::Rc;
53//!
54//! let rc = Rc::new(());
55//! // Method-call syntax
56//! let rc2 = rc.clone();
57//! // Fully qualified syntax
58//! let rc3 = Rc::clone(&rc);
59//! ```
60//!
61//! [`Weak<T>`][`Weak`] does not auto-dereference to `T`, because the inner value may have
62//! already been dropped.
63//!
64//! # Cloning references
65//!
66//! Creating a new reference to the same allocation as an existing reference counted pointer
67//! is done using the `Clone` trait implemented for [`Rc<T>`][`Rc`] and [`Weak<T>`][`Weak`].
68//!
69//! ```
70//! use std::rc::Rc;
71//!
72//! let foo = Rc::new(vec![1.0, 2.0, 3.0]);
73//! // The two syntaxes below are equivalent.
74//! let a = foo.clone();
75//! let b = Rc::clone(&foo);
76//! // a and b both point to the same memory location as foo.
77//! ```
78//!
79//! The `Rc::clone(&from)` syntax is the most idiomatic because it conveys more explicitly
80//! the meaning of the code. In the example above, this syntax makes it easier to see that
81//! this code is creating a new reference rather than copying the whole content of foo.
82//!
83//! # Examples
84//!
85//! Consider a scenario where a set of `Gadget`s are owned by a given `Owner`.
86//! We want to have our `Gadget`s point to their `Owner`. We can't do this with
87//! unique ownership, because more than one gadget may belong to the same
88//! `Owner`. [`Rc`] allows us to share an `Owner` between multiple `Gadget`s,
89//! and have the `Owner` remain allocated as long as any `Gadget` points at it.
90//!
91//! ```
92//! use std::rc::Rc;
93//!
94//! struct Owner {
95//!     name: String,
96//!     // ...other fields
97//! }
98//!
99//! struct Gadget {
100//!     id: i32,
101//!     owner: Rc<Owner>,
102//!     // ...other fields
103//! }
104//!
105//! fn main() {
106//!     // Create a reference-counted `Owner`.
107//!     let gadget_owner: Rc<Owner> = Rc::new(
108//!         Owner {
109//!             name: "Gadget Man".to_string(),
110//!         }
111//!     );
112//!
113//!     // Create `Gadget`s belonging to `gadget_owner`. Cloning the `Rc<Owner>`
114//!     // gives us a new pointer to the same `Owner` allocation, incrementing
115//!     // the reference count in the process.
116//!     let gadget1 = Gadget {
117//!         id: 1,
118//!         owner: Rc::clone(&gadget_owner),
119//!     };
120//!     let gadget2 = Gadget {
121//!         id: 2,
122//!         owner: Rc::clone(&gadget_owner),
123//!     };
124//!
125//!     // Dispose of our local variable `gadget_owner`.
126//!     drop(gadget_owner);
127//!
128//!     // Despite dropping `gadget_owner`, we're still able to print out the name
129//!     // of the `Owner` of the `Gadget`s. This is because we've only dropped a
130//!     // single `Rc<Owner>`, not the `Owner` it points to. As long as there are
131//!     // other `Rc<Owner>` pointing at the same `Owner` allocation, it will remain
132//!     // live. The field projection `gadget1.owner.name` works because
133//!     // `Rc<Owner>` automatically dereferences to `Owner`.
134//!     println!("Gadget {} owned by {}", gadget1.id, gadget1.owner.name);
135//!     println!("Gadget {} owned by {}", gadget2.id, gadget2.owner.name);
136//!
137//!     // At the end of the function, `gadget1` and `gadget2` are destroyed, and
138//!     // with them the last counted references to our `Owner`. Gadget Man now
139//!     // gets destroyed as well.
140//! }
141//! ```
142//!
143//! If our requirements change, and we also need to be able to traverse from
144//! `Owner` to `Gadget`, we will run into problems. An [`Rc`] pointer from `Owner`
145//! to `Gadget` introduces a cycle. This means that their
146//! reference counts can never reach 0, and the allocation will never be destroyed:
147//! a memory leak. In order to get around this, we can use [`Weak`]
148//! pointers.
149//!
150//! Rust actually makes it somewhat difficult to produce this loop in the first
151//! place. In order to end up with two values that point at each other, one of
152//! them needs to be mutable. This is difficult because [`Rc`] enforces
153//! memory safety by only giving out shared references to the value it wraps,
154//! and these don't allow direct mutation. We need to wrap the part of the
155//! value we wish to mutate in a [`RefCell`], which provides *interior
156//! mutability*: a method to achieve mutability through a shared reference.
157//! [`RefCell`] enforces Rust's borrowing rules at runtime.
158//!
159//! ```
160//! use std::rc::Rc;
161//! use std::rc::Weak;
162//! use std::cell::RefCell;
163//!
164//! struct Owner {
165//!     name: String,
166//!     gadgets: RefCell<Vec<Weak<Gadget>>>,
167//!     // ...other fields
168//! }
169//!
170//! struct Gadget {
171//!     id: i32,
172//!     owner: Rc<Owner>,
173//!     // ...other fields
174//! }
175//!
176//! fn main() {
177//!     // Create a reference-counted `Owner`. Note that we've put the `Owner`'s
178//!     // vector of `Gadget`s inside a `RefCell` so that we can mutate it through
179//!     // a shared reference.
180//!     let gadget_owner: Rc<Owner> = Rc::new(
181//!         Owner {
182//!             name: "Gadget Man".to_string(),
183//!             gadgets: RefCell::new(vec![]),
184//!         }
185//!     );
186//!
187//!     // Create `Gadget`s belonging to `gadget_owner`, as before.
188//!     let gadget1 = Rc::new(
189//!         Gadget {
190//!             id: 1,
191//!             owner: Rc::clone(&gadget_owner),
192//!         }
193//!     );
194//!     let gadget2 = Rc::new(
195//!         Gadget {
196//!             id: 2,
197//!             owner: Rc::clone(&gadget_owner),
198//!         }
199//!     );
200//!
201//!     // Add the `Gadget`s to their `Owner`.
202//!     {
203//!         let mut gadgets = gadget_owner.gadgets.borrow_mut();
204//!         gadgets.push(Rc::downgrade(&gadget1));
205//!         gadgets.push(Rc::downgrade(&gadget2));
206//!
207//!         // `RefCell` dynamic borrow ends here.
208//!     }
209//!
210//!     // Iterate over our `Gadget`s, printing their details out.
211//!     for gadget_weak in gadget_owner.gadgets.borrow().iter() {
212//!
213//!         // `gadget_weak` is a `Weak<Gadget>`. Since `Weak` pointers can't
214//!         // guarantee the allocation still exists, we need to call
215//!         // `upgrade`, which returns an `Option<Rc<Gadget>>`.
216//!         //
217//!         // In this case we know the allocation still exists, so we simply
218//!         // `unwrap` the `Option`. In a more complicated program, you might
219//!         // need graceful error handling for a `None` result.
220//!
221//!         let gadget = gadget_weak.upgrade().unwrap();
222//!         println!("Gadget {} owned by {}", gadget.id, gadget.owner.name);
223//!     }
224//!
225//!     // At the end of the function, `gadget_owner`, `gadget1`, and `gadget2`
226//!     // are destroyed. There are now no strong (`Rc`) pointers to the
227//!     // gadgets, so they are destroyed. This zeroes the reference count on
228//!     // Gadget Man, so he gets destroyed as well.
229//! }
230//! ```
231//!
232//! [clone]: Clone::clone
233//! [`Cell`]: core::cell::Cell
234//! [`RefCell`]: core::cell::RefCell
235//! [arc]: crate::sync::Arc
236//! [`Deref`]: core::ops::Deref
237//! [downgrade]: Rc::downgrade
238//! [upgrade]: Weak::upgrade
239//! [mutability]: core::cell#introducing-mutability-inside-of-something-immutable
240//! [fully qualified syntax]: https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-for-disambiguation-calling-methods-with-the-same-name
241
242#![stable(feature = "rust1", since = "1.0.0")]
243
244use core::any::Any;
245use core::cell::{Cell, CloneFromCell};
246#[cfg(not(no_global_oom_handling))]
247use core::clone::TrivialClone;
248use core::clone::{CloneToUninit, UseCloned};
249use core::cmp::Ordering;
250use core::hash::{Hash, Hasher};
251use core::intrinsics::abort;
252#[cfg(not(no_global_oom_handling))]
253use core::iter;
254use core::marker::{PhantomData, Unsize};
255use core::mem::{self, ManuallyDrop};
256use core::num::NonZeroUsize;
257use core::ops::{CoerceUnsized, Deref, DerefMut, DerefPure, DispatchFromDyn, LegacyReceiver};
258#[cfg(not(no_global_oom_handling))]
259use core::ops::{Residual, Try};
260use core::panic::{RefUnwindSafe, UnwindSafe};
261#[cfg(not(no_global_oom_handling))]
262use core::pin::Pin;
263use core::pin::PinCoerceUnsized;
264use core::ptr::{self, Alignment, NonNull, drop_in_place};
265#[cfg(not(no_global_oom_handling))]
266use core::slice::from_raw_parts_mut;
267use core::{borrow, fmt, hint};
268
269#[cfg(not(no_global_oom_handling))]
270use crate::alloc::handle_alloc_error;
271use crate::alloc::{AllocError, Allocator, Global, Layout};
272use crate::borrow::{Cow, ToOwned};
273use crate::boxed::Box;
274#[cfg(not(no_global_oom_handling))]
275use crate::string::String;
276#[cfg(not(no_global_oom_handling))]
277use crate::vec::Vec;
278
279// This is repr(C) to future-proof against possible field-reordering, which
280// would interfere with otherwise safe [into|from]_raw() of transmutable
281// inner types.
282// repr(align(2)) (forcing alignment to at least 2) is required because usize
283// has 1-byte alignment on AVR.
284#[repr(C, align(2))]
285struct RcInner<T: ?Sized> {
286    strong: Cell<usize>,
287    weak: Cell<usize>,
288    value: T,
289}
290
291/// Calculate layout for `RcInner<T>` using the inner value's layout
292fn rc_inner_layout_for_value_layout(layout: Layout) -> Layout {
293    // Calculate layout using the given value layout.
294    // Previously, layout was calculated on the expression
295    // `&*(ptr as *const RcInner<T>)`, but this created a misaligned
296    // reference (see #54908).
297    Layout::new::<RcInner<()>>().extend(layout).unwrap().0.pad_to_align()
298}
299
300/// A single-threaded reference-counting pointer. 'Rc' stands for 'Reference
301/// Counted'.
302///
303/// See the [module-level documentation](./index.html) for more details.
304///
305/// The inherent methods of `Rc` are all associated functions, which means
306/// that you have to call them as e.g., [`Rc::get_mut(&mut value)`][get_mut] instead of
307/// `value.get_mut()`. This avoids conflicts with methods of the inner type `T`.
308///
309/// [get_mut]: Rc::get_mut
310#[doc(search_unbox)]
311#[rustc_diagnostic_item = "Rc"]
312#[stable(feature = "rust1", since = "1.0.0")]
313#[rustc_insignificant_dtor]
314pub struct Rc<
315    T: ?Sized,
316    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
317> {
318    ptr: NonNull<RcInner<T>>,
319    phantom: PhantomData<RcInner<T>>,
320    alloc: A,
321}
322
323#[stable(feature = "rust1", since = "1.0.0")]
324impl<T: ?Sized, A: Allocator> !Send for Rc<T, A> {}
325
326// Note that this negative impl isn't strictly necessary for correctness,
327// as `Rc` transitively contains a `Cell`, which is itself `!Sync`.
328// However, given how important `Rc`'s `!Sync`-ness is,
329// having an explicit negative impl is nice for documentation purposes
330// and results in nicer error messages.
331#[stable(feature = "rust1", since = "1.0.0")]
332impl<T: ?Sized, A: Allocator> !Sync for Rc<T, A> {}
333
334#[stable(feature = "catch_unwind", since = "1.9.0")]
335impl<T: RefUnwindSafe + ?Sized, A: Allocator + UnwindSafe> UnwindSafe for Rc<T, A> {}
336#[stable(feature = "rc_ref_unwind_safe", since = "1.58.0")]
337impl<T: RefUnwindSafe + ?Sized, A: Allocator + UnwindSafe> RefUnwindSafe for Rc<T, A> {}
338
339#[unstable(feature = "coerce_unsized", issue = "18598")]
340impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<Rc<U, A>> for Rc<T, A> {}
341
342#[unstable(feature = "dispatch_from_dyn", issue = "none")]
343impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<Rc<U>> for Rc<T> {}
344
345// SAFETY: `Rc::clone` doesn't access any `Cell`s which could contain the `Rc` being cloned.
346#[unstable(feature = "cell_get_cloned", issue = "145329")]
347unsafe impl<T: ?Sized> CloneFromCell for Rc<T> {}
348
349impl<T: ?Sized> Rc<T> {
350    #[inline]
351    unsafe fn from_inner(ptr: NonNull<RcInner<T>>) -> Self {
352        unsafe { Self::from_inner_in(ptr, Global) }
353    }
354
355    #[inline]
356    unsafe fn from_ptr(ptr: *mut RcInner<T>) -> Self {
357        unsafe { Self::from_inner(NonNull::new_unchecked(ptr)) }
358    }
359}
360
361impl<T: ?Sized, A: Allocator> Rc<T, A> {
362    #[inline(always)]
363    fn inner(&self) -> &RcInner<T> {
364        // This unsafety is ok because while this Rc is alive we're guaranteed
365        // that the inner pointer is valid.
366        unsafe { self.ptr.as_ref() }
367    }
368
369    #[inline]
370    fn into_inner_with_allocator(this: Self) -> (NonNull<RcInner<T>>, A) {
371        let this = mem::ManuallyDrop::new(this);
372        (this.ptr, unsafe { ptr::read(&this.alloc) })
373    }
374
375    #[inline]
376    unsafe fn from_inner_in(ptr: NonNull<RcInner<T>>, alloc: A) -> Self {
377        Self { ptr, phantom: PhantomData, alloc }
378    }
379
380    #[inline]
381    unsafe fn from_ptr_in(ptr: *mut RcInner<T>, alloc: A) -> Self {
382        unsafe { Self::from_inner_in(NonNull::new_unchecked(ptr), alloc) }
383    }
384
385    // Non-inlined part of `drop`.
386    #[inline(never)]
387    unsafe fn drop_slow(&mut self) {
388        // Reconstruct the "strong weak" pointer and drop it when this
389        // variable goes out of scope. This ensures that the memory is
390        // deallocated even if the destructor of `T` panics.
391        let _weak = Weak { ptr: self.ptr, alloc: &self.alloc };
392
393        // Destroy the contained object.
394        // We cannot use `get_mut_unchecked` here, because `self.alloc` is borrowed.
395        unsafe {
396            ptr::drop_in_place(&mut (*self.ptr.as_ptr()).value);
397        }
398    }
399}
400
401impl<T> Rc<T> {
402    /// Constructs a new `Rc<T>`.
403    ///
404    /// # Examples
405    ///
406    /// ```
407    /// use std::rc::Rc;
408    ///
409    /// let five = Rc::new(5);
410    /// ```
411    #[cfg(not(no_global_oom_handling))]
412    #[stable(feature = "rust1", since = "1.0.0")]
413    pub fn new(value: T) -> Rc<T> {
414        // There is an implicit weak pointer owned by all the strong
415        // pointers, which ensures that the weak destructor never frees
416        // the allocation while the strong destructor is running, even
417        // if the weak pointer is stored inside the strong one.
418        unsafe {
419            Self::from_inner(
420                Box::leak(Box::new(RcInner { strong: Cell::new(1), weak: Cell::new(1), value }))
421                    .into(),
422            )
423        }
424    }
425
426    /// Constructs a new `Rc<T>` while giving you a `Weak<T>` to the allocation,
427    /// to allow you to construct a `T` which holds a weak pointer to itself.
428    ///
429    /// Generally, a structure circularly referencing itself, either directly or
430    /// indirectly, should not hold a strong reference to itself to prevent a memory leak.
431    /// Using this function, you get access to the weak pointer during the
432    /// initialization of `T`, before the `Rc<T>` is created, such that you can
433    /// clone and store it inside the `T`.
434    ///
435    /// `new_cyclic` first allocates the managed allocation for the `Rc<T>`,
436    /// then calls your closure, giving it a `Weak<T>` to this allocation,
437    /// and only afterwards completes the construction of the `Rc<T>` by placing
438    /// the `T` returned from your closure into the allocation.
439    ///
440    /// Since the new `Rc<T>` is not fully-constructed until `Rc<T>::new_cyclic`
441    /// returns, calling [`upgrade`] on the weak reference inside your closure will
442    /// fail and result in a `None` value.
443    ///
444    /// # Panics
445    ///
446    /// If `data_fn` panics, the panic is propagated to the caller, and the
447    /// temporary [`Weak<T>`] is dropped normally.
448    ///
449    /// # Examples
450    ///
451    /// ```
452    /// # #![allow(dead_code)]
453    /// use std::rc::{Rc, Weak};
454    ///
455    /// struct Gadget {
456    ///     me: Weak<Gadget>,
457    /// }
458    ///
459    /// impl Gadget {
460    ///     /// Constructs a reference counted Gadget.
461    ///     fn new() -> Rc<Self> {
462    ///         // `me` is a `Weak<Gadget>` pointing at the new allocation of the
463    ///         // `Rc` we're constructing.
464    ///         Rc::new_cyclic(|me| {
465    ///             // Create the actual struct here.
466    ///             Gadget { me: me.clone() }
467    ///         })
468    ///     }
469    ///
470    ///     /// Returns a reference counted pointer to Self.
471    ///     fn me(&self) -> Rc<Self> {
472    ///         self.me.upgrade().unwrap()
473    ///     }
474    /// }
475    /// ```
476    /// [`upgrade`]: Weak::upgrade
477    #[cfg(not(no_global_oom_handling))]
478    #[stable(feature = "arc_new_cyclic", since = "1.60.0")]
479    pub fn new_cyclic<F>(data_fn: F) -> Rc<T>
480    where
481        F: FnOnce(&Weak<T>) -> T,
482    {
483        Self::new_cyclic_in(data_fn, Global)
484    }
485
486    /// Constructs a new `Rc` with uninitialized contents.
487    ///
488    /// # Examples
489    ///
490    /// ```
491    /// use std::rc::Rc;
492    ///
493    /// let mut five = Rc::<u32>::new_uninit();
494    ///
495    /// // Deferred initialization:
496    /// Rc::get_mut(&mut five).unwrap().write(5);
497    ///
498    /// let five = unsafe { five.assume_init() };
499    ///
500    /// assert_eq!(*five, 5)
501    /// ```
502    #[cfg(not(no_global_oom_handling))]
503    #[stable(feature = "new_uninit", since = "1.82.0")]
504    #[must_use]
505    pub fn new_uninit() -> Rc<mem::MaybeUninit<T>> {
506        unsafe {
507            Rc::from_ptr(Rc::allocate_for_layout(
508                Layout::new::<T>(),
509                |layout| Global.allocate(layout),
510                <*mut u8>::cast,
511            ))
512        }
513    }
514
515    /// Constructs a new `Rc` with uninitialized contents, with the memory
516    /// being filled with `0` bytes.
517    ///
518    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
519    /// incorrect usage of this method.
520    ///
521    /// # Examples
522    ///
523    /// ```
524    /// use std::rc::Rc;
525    ///
526    /// let zero = Rc::<u32>::new_zeroed();
527    /// let zero = unsafe { zero.assume_init() };
528    ///
529    /// assert_eq!(*zero, 0)
530    /// ```
531    ///
532    /// [zeroed]: mem::MaybeUninit::zeroed
533    #[cfg(not(no_global_oom_handling))]
534    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
535    #[must_use]
536    pub fn new_zeroed() -> Rc<mem::MaybeUninit<T>> {
537        unsafe {
538            Rc::from_ptr(Rc::allocate_for_layout(
539                Layout::new::<T>(),
540                |layout| Global.allocate_zeroed(layout),
541                <*mut u8>::cast,
542            ))
543        }
544    }
545
546    /// Constructs a new `Rc<T>`, returning an error if the allocation fails
547    ///
548    /// # Examples
549    ///
550    /// ```
551    /// #![feature(allocator_api)]
552    /// use std::rc::Rc;
553    ///
554    /// let five = Rc::try_new(5);
555    /// # Ok::<(), std::alloc::AllocError>(())
556    /// ```
557    #[unstable(feature = "allocator_api", issue = "32838")]
558    pub fn try_new(value: T) -> Result<Rc<T>, AllocError> {
559        // There is an implicit weak pointer owned by all the strong
560        // pointers, which ensures that the weak destructor never frees
561        // the allocation while the strong destructor is running, even
562        // if the weak pointer is stored inside the strong one.
563        unsafe {
564            Ok(Self::from_inner(
565                Box::leak(Box::try_new(RcInner {
566                    strong: Cell::new(1),
567                    weak: Cell::new(1),
568                    value,
569                })?)
570                .into(),
571            ))
572        }
573    }
574
575    /// Constructs a new `Rc` with uninitialized contents, returning an error if the allocation fails
576    ///
577    /// # Examples
578    ///
579    /// ```
580    /// #![feature(allocator_api)]
581    ///
582    /// use std::rc::Rc;
583    ///
584    /// let mut five = Rc::<u32>::try_new_uninit()?;
585    ///
586    /// // Deferred initialization:
587    /// Rc::get_mut(&mut five).unwrap().write(5);
588    ///
589    /// let five = unsafe { five.assume_init() };
590    ///
591    /// assert_eq!(*five, 5);
592    /// # Ok::<(), std::alloc::AllocError>(())
593    /// ```
594    #[unstable(feature = "allocator_api", issue = "32838")]
595    pub fn try_new_uninit() -> Result<Rc<mem::MaybeUninit<T>>, AllocError> {
596        unsafe {
597            Ok(Rc::from_ptr(Rc::try_allocate_for_layout(
598                Layout::new::<T>(),
599                |layout| Global.allocate(layout),
600                <*mut u8>::cast,
601            )?))
602        }
603    }
604
605    /// Constructs a new `Rc` with uninitialized contents, with the memory
606    /// being filled with `0` bytes, returning an error if the allocation fails
607    ///
608    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
609    /// incorrect usage of this method.
610    ///
611    /// # Examples
612    ///
613    /// ```
614    /// #![feature(allocator_api)]
615    ///
616    /// use std::rc::Rc;
617    ///
618    /// let zero = Rc::<u32>::try_new_zeroed()?;
619    /// let zero = unsafe { zero.assume_init() };
620    ///
621    /// assert_eq!(*zero, 0);
622    /// # Ok::<(), std::alloc::AllocError>(())
623    /// ```
624    ///
625    /// [zeroed]: mem::MaybeUninit::zeroed
626    #[unstable(feature = "allocator_api", issue = "32838")]
627    pub fn try_new_zeroed() -> Result<Rc<mem::MaybeUninit<T>>, AllocError> {
628        unsafe {
629            Ok(Rc::from_ptr(Rc::try_allocate_for_layout(
630                Layout::new::<T>(),
631                |layout| Global.allocate_zeroed(layout),
632                <*mut u8>::cast,
633            )?))
634        }
635    }
636    /// Constructs a new `Pin<Rc<T>>`. If `T` does not implement `Unpin`, then
637    /// `value` will be pinned in memory and unable to be moved.
638    #[cfg(not(no_global_oom_handling))]
639    #[stable(feature = "pin", since = "1.33.0")]
640    #[must_use]
641    pub fn pin(value: T) -> Pin<Rc<T>> {
642        unsafe { Pin::new_unchecked(Rc::new(value)) }
643    }
644
645    /// Maps the value in an `Rc`, reusing the allocation if possible.
646    ///
647    /// `f` is called on a reference to the value in the `Rc`, and the result is returned, also in
648    /// an `Rc`.
649    ///
650    /// Note: this is an associated function, which means that you have
651    /// to call it as `Rc::map(r, f)` instead of `r.map(f)`. This
652    /// is so that there is no conflict with a method on the inner type.
653    ///
654    /// # Examples
655    ///
656    /// ```
657    /// #![feature(smart_pointer_try_map)]
658    ///
659    /// use std::rc::Rc;
660    ///
661    /// let r = Rc::new(7);
662    /// let new = Rc::map(r, |i| i + 7);
663    /// assert_eq!(*new, 14);
664    /// ```
665    #[cfg(not(no_global_oom_handling))]
666    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
667    pub fn map<U>(this: Self, f: impl FnOnce(&T) -> U) -> Rc<U> {
668        if size_of::<T>() == size_of::<U>()
669            && align_of::<T>() == align_of::<U>()
670            && Rc::is_unique(&this)
671        {
672            unsafe {
673                let ptr = Rc::into_raw(this);
674                let value = ptr.read();
675                let mut allocation = Rc::from_raw(ptr.cast::<mem::MaybeUninit<U>>());
676
677                Rc::get_mut_unchecked(&mut allocation).write(f(&value));
678                allocation.assume_init()
679            }
680        } else {
681            Rc::new(f(&*this))
682        }
683    }
684
685    /// Attempts to map the value in an `Rc`, reusing the allocation if possible.
686    ///
687    /// `f` is called on a reference to the value in the `Rc`, and if the operation succeeds, the
688    /// result is returned, also in an `Rc`.
689    ///
690    /// Note: this is an associated function, which means that you have
691    /// to call it as `Rc::try_map(r, f)` instead of `r.try_map(f)`. This
692    /// is so that there is no conflict with a method on the inner type.
693    ///
694    /// # Examples
695    ///
696    /// ```
697    /// #![feature(smart_pointer_try_map)]
698    ///
699    /// use std::rc::Rc;
700    ///
701    /// let b = Rc::new(7);
702    /// let new = Rc::try_map(b, |&i| u32::try_from(i)).unwrap();
703    /// assert_eq!(*new, 7);
704    /// ```
705    #[cfg(not(no_global_oom_handling))]
706    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
707    pub fn try_map<R>(
708        this: Self,
709        f: impl FnOnce(&T) -> R,
710    ) -> <R::Residual as Residual<Rc<R::Output>>>::TryType
711    where
712        R: Try,
713        R::Residual: Residual<Rc<R::Output>>,
714    {
715        if size_of::<T>() == size_of::<R::Output>()
716            && align_of::<T>() == align_of::<R::Output>()
717            && Rc::is_unique(&this)
718        {
719            unsafe {
720                let ptr = Rc::into_raw(this);
721                let value = ptr.read();
722                let mut allocation = Rc::from_raw(ptr.cast::<mem::MaybeUninit<R::Output>>());
723
724                Rc::get_mut_unchecked(&mut allocation).write(f(&value)?);
725                try { allocation.assume_init() }
726            }
727        } else {
728            try { Rc::new(f(&*this)?) }
729        }
730    }
731}
732
733impl<T, A: Allocator> Rc<T, A> {
734    /// Constructs a new `Rc` in the provided allocator.
735    ///
736    /// # Examples
737    ///
738    /// ```
739    /// #![feature(allocator_api)]
740    /// use std::rc::Rc;
741    /// use std::alloc::System;
742    ///
743    /// let five = Rc::new_in(5, System);
744    /// ```
745    #[cfg(not(no_global_oom_handling))]
746    #[unstable(feature = "allocator_api", issue = "32838")]
747    #[inline]
748    pub fn new_in(value: T, alloc: A) -> Rc<T, A> {
749        // NOTE: Prefer match over unwrap_or_else since closure sometimes not inlineable.
750        // That would make code size bigger.
751        match Self::try_new_in(value, alloc) {
752            Ok(m) => m,
753            Err(_) => handle_alloc_error(Layout::new::<RcInner<T>>()),
754        }
755    }
756
757    /// Constructs a new `Rc` with uninitialized contents in the provided allocator.
758    ///
759    /// # Examples
760    ///
761    /// ```
762    /// #![feature(get_mut_unchecked)]
763    /// #![feature(allocator_api)]
764    ///
765    /// use std::rc::Rc;
766    /// use std::alloc::System;
767    ///
768    /// let mut five = Rc::<u32, _>::new_uninit_in(System);
769    ///
770    /// let five = unsafe {
771    ///     // Deferred initialization:
772    ///     Rc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);
773    ///
774    ///     five.assume_init()
775    /// };
776    ///
777    /// assert_eq!(*five, 5)
778    /// ```
779    #[cfg(not(no_global_oom_handling))]
780    #[unstable(feature = "allocator_api", issue = "32838")]
781    #[inline]
782    pub fn new_uninit_in(alloc: A) -> Rc<mem::MaybeUninit<T>, A> {
783        unsafe {
784            Rc::from_ptr_in(
785                Rc::allocate_for_layout(
786                    Layout::new::<T>(),
787                    |layout| alloc.allocate(layout),
788                    <*mut u8>::cast,
789                ),
790                alloc,
791            )
792        }
793    }
794
795    /// Constructs a new `Rc` with uninitialized contents, with the memory
796    /// being filled with `0` bytes, in the provided allocator.
797    ///
798    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
799    /// incorrect usage of this method.
800    ///
801    /// # Examples
802    ///
803    /// ```
804    /// #![feature(allocator_api)]
805    ///
806    /// use std::rc::Rc;
807    /// use std::alloc::System;
808    ///
809    /// let zero = Rc::<u32, _>::new_zeroed_in(System);
810    /// let zero = unsafe { zero.assume_init() };
811    ///
812    /// assert_eq!(*zero, 0)
813    /// ```
814    ///
815    /// [zeroed]: mem::MaybeUninit::zeroed
816    #[cfg(not(no_global_oom_handling))]
817    #[unstable(feature = "allocator_api", issue = "32838")]
818    #[inline]
819    pub fn new_zeroed_in(alloc: A) -> Rc<mem::MaybeUninit<T>, A> {
820        unsafe {
821            Rc::from_ptr_in(
822                Rc::allocate_for_layout(
823                    Layout::new::<T>(),
824                    |layout| alloc.allocate_zeroed(layout),
825                    <*mut u8>::cast,
826                ),
827                alloc,
828            )
829        }
830    }
831
832    /// Constructs a new `Rc<T, A>` in the given allocator while giving you a `Weak<T, A>` to the allocation,
833    /// to allow you to construct a `T` which holds a weak pointer to itself.
834    ///
835    /// Generally, a structure circularly referencing itself, either directly or
836    /// indirectly, should not hold a strong reference to itself to prevent a memory leak.
837    /// Using this function, you get access to the weak pointer during the
838    /// initialization of `T`, before the `Rc<T, A>` is created, such that you can
839    /// clone and store it inside the `T`.
840    ///
841    /// `new_cyclic_in` first allocates the managed allocation for the `Rc<T, A>`,
842    /// then calls your closure, giving it a `Weak<T, A>` to this allocation,
843    /// and only afterwards completes the construction of the `Rc<T, A>` by placing
844    /// the `T` returned from your closure into the allocation.
845    ///
846    /// Since the new `Rc<T, A>` is not fully-constructed until `Rc<T, A>::new_cyclic_in`
847    /// returns, calling [`upgrade`] on the weak reference inside your closure will
848    /// fail and result in a `None` value.
849    ///
850    /// # Panics
851    ///
852    /// If `data_fn` panics, the panic is propagated to the caller, and the
853    /// temporary [`Weak<T, A>`] is dropped normally.
854    ///
855    /// # Examples
856    ///
857    /// See [`new_cyclic`].
858    ///
859    /// [`new_cyclic`]: Rc::new_cyclic
860    /// [`upgrade`]: Weak::upgrade
861    #[cfg(not(no_global_oom_handling))]
862    #[unstable(feature = "allocator_api", issue = "32838")]
863    pub fn new_cyclic_in<F>(data_fn: F, alloc: A) -> Rc<T, A>
864    where
865        F: FnOnce(&Weak<T, A>) -> T,
866    {
867        // Construct the inner in the "uninitialized" state with a single
868        // weak reference.
869        let (uninit_raw_ptr, alloc) = Box::into_raw_with_allocator(Box::new_in(
870            RcInner {
871                strong: Cell::new(0),
872                weak: Cell::new(1),
873                value: mem::MaybeUninit::<T>::uninit(),
874            },
875            alloc,
876        ));
877        let uninit_ptr: NonNull<_> = (unsafe { &mut *uninit_raw_ptr }).into();
878        let init_ptr: NonNull<RcInner<T>> = uninit_ptr.cast();
879
880        let weak = Weak { ptr: init_ptr, alloc };
881
882        // It's important we don't give up ownership of the weak pointer, or
883        // else the memory might be freed by the time `data_fn` returns. If
884        // we really wanted to pass ownership, we could create an additional
885        // weak pointer for ourselves, but this would result in additional
886        // updates to the weak reference count which might not be necessary
887        // otherwise.
888        let data = data_fn(&weak);
889
890        let strong = unsafe {
891            let inner = init_ptr.as_ptr();
892            ptr::write(&raw mut (*inner).value, data);
893
894            let prev_value = (*inner).strong.get();
895            debug_assert_eq!(prev_value, 0, "No prior strong references should exist");
896            (*inner).strong.set(1);
897
898            // Strong references should collectively own a shared weak reference,
899            // so don't run the destructor for our old weak reference.
900            // Calling into_raw_with_allocator has the double effect of giving us back the allocator,
901            // and forgetting the weak reference.
902            let alloc = weak.into_raw_with_allocator().1;
903
904            Rc::from_inner_in(init_ptr, alloc)
905        };
906
907        strong
908    }
909
910    /// Constructs a new `Rc<T>` in the provided allocator, returning an error if the allocation
911    /// fails
912    ///
913    /// # Examples
914    ///
915    /// ```
916    /// #![feature(allocator_api)]
917    /// use std::rc::Rc;
918    /// use std::alloc::System;
919    ///
920    /// let five = Rc::try_new_in(5, System);
921    /// # Ok::<(), std::alloc::AllocError>(())
922    /// ```
923    #[unstable(feature = "allocator_api", issue = "32838")]
924    #[inline]
925    pub fn try_new_in(value: T, alloc: A) -> Result<Self, AllocError> {
926        // There is an implicit weak pointer owned by all the strong
927        // pointers, which ensures that the weak destructor never frees
928        // the allocation while the strong destructor is running, even
929        // if the weak pointer is stored inside the strong one.
930        let (ptr, alloc) = Box::into_unique(Box::try_new_in(
931            RcInner { strong: Cell::new(1), weak: Cell::new(1), value },
932            alloc,
933        )?);
934        Ok(unsafe { Self::from_inner_in(ptr.into(), alloc) })
935    }
936
937    /// Constructs a new `Rc` with uninitialized contents, in the provided allocator, returning an
938    /// error if the allocation fails
939    ///
940    /// # Examples
941    ///
942    /// ```
943    /// #![feature(allocator_api)]
944    /// #![feature(get_mut_unchecked)]
945    ///
946    /// use std::rc::Rc;
947    /// use std::alloc::System;
948    ///
949    /// let mut five = Rc::<u32, _>::try_new_uninit_in(System)?;
950    ///
951    /// let five = unsafe {
952    ///     // Deferred initialization:
953    ///     Rc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);
954    ///
955    ///     five.assume_init()
956    /// };
957    ///
958    /// assert_eq!(*five, 5);
959    /// # Ok::<(), std::alloc::AllocError>(())
960    /// ```
961    #[unstable(feature = "allocator_api", issue = "32838")]
962    #[inline]
963    pub fn try_new_uninit_in(alloc: A) -> Result<Rc<mem::MaybeUninit<T>, A>, AllocError> {
964        unsafe {
965            Ok(Rc::from_ptr_in(
966                Rc::try_allocate_for_layout(
967                    Layout::new::<T>(),
968                    |layout| alloc.allocate(layout),
969                    <*mut u8>::cast,
970                )?,
971                alloc,
972            ))
973        }
974    }
975
976    /// Constructs a new `Rc` with uninitialized contents, with the memory
977    /// being filled with `0` bytes, in the provided allocator, returning an error if the allocation
978    /// fails
979    ///
980    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
981    /// incorrect usage of this method.
982    ///
983    /// # Examples
984    ///
985    /// ```
986    /// #![feature(allocator_api)]
987    ///
988    /// use std::rc::Rc;
989    /// use std::alloc::System;
990    ///
991    /// let zero = Rc::<u32, _>::try_new_zeroed_in(System)?;
992    /// let zero = unsafe { zero.assume_init() };
993    ///
994    /// assert_eq!(*zero, 0);
995    /// # Ok::<(), std::alloc::AllocError>(())
996    /// ```
997    ///
998    /// [zeroed]: mem::MaybeUninit::zeroed
999    #[unstable(feature = "allocator_api", issue = "32838")]
1000    #[inline]
1001    pub fn try_new_zeroed_in(alloc: A) -> Result<Rc<mem::MaybeUninit<T>, A>, AllocError> {
1002        unsafe {
1003            Ok(Rc::from_ptr_in(
1004                Rc::try_allocate_for_layout(
1005                    Layout::new::<T>(),
1006                    |layout| alloc.allocate_zeroed(layout),
1007                    <*mut u8>::cast,
1008                )?,
1009                alloc,
1010            ))
1011        }
1012    }
1013
1014    /// Constructs a new `Pin<Rc<T>>` in the provided allocator. If `T` does not implement `Unpin`, then
1015    /// `value` will be pinned in memory and unable to be moved.
1016    #[cfg(not(no_global_oom_handling))]
1017    #[unstable(feature = "allocator_api", issue = "32838")]
1018    #[inline]
1019    pub fn pin_in(value: T, alloc: A) -> Pin<Self>
1020    where
1021        A: 'static,
1022    {
1023        unsafe { Pin::new_unchecked(Rc::new_in(value, alloc)) }
1024    }
1025
1026    /// Returns the inner value, if the `Rc` has exactly one strong reference.
1027    ///
1028    /// Otherwise, an [`Err`] is returned with the same `Rc` that was
1029    /// passed in.
1030    ///
1031    /// This will succeed even if there are outstanding weak references.
1032    ///
1033    /// # Examples
1034    ///
1035    /// ```
1036    /// use std::rc::Rc;
1037    ///
1038    /// let x = Rc::new(3);
1039    /// assert_eq!(Rc::try_unwrap(x), Ok(3));
1040    ///
1041    /// let x = Rc::new(4);
1042    /// let _y = Rc::clone(&x);
1043    /// assert_eq!(*Rc::try_unwrap(x).unwrap_err(), 4);
1044    /// ```
1045    #[inline]
1046    #[stable(feature = "rc_unique", since = "1.4.0")]
1047    pub fn try_unwrap(this: Self) -> Result<T, Self> {
1048        if Rc::strong_count(&this) == 1 {
1049            let this = ManuallyDrop::new(this);
1050
1051            let val: T = unsafe { ptr::read(&**this) }; // copy the contained object
1052            let alloc: A = unsafe { ptr::read(&this.alloc) }; // copy the allocator
1053
1054            // Indicate to Weaks that they can't be promoted by decrementing
1055            // the strong count, and then remove the implicit "strong weak"
1056            // pointer while also handling drop logic by just crafting a
1057            // fake Weak.
1058            this.inner().dec_strong();
1059            let _weak = Weak { ptr: this.ptr, alloc };
1060            Ok(val)
1061        } else {
1062            Err(this)
1063        }
1064    }
1065
1066    /// Returns the inner value, if the `Rc` has exactly one strong reference.
1067    ///
1068    /// Otherwise, [`None`] is returned and the `Rc` is dropped.
1069    ///
1070    /// This will succeed even if there are outstanding weak references.
1071    ///
1072    /// If `Rc::into_inner` is called on every clone of this `Rc`,
1073    /// it is guaranteed that exactly one of the calls returns the inner value.
1074    /// This means in particular that the inner value is not dropped.
1075    ///
1076    /// [`Rc::try_unwrap`] is conceptually similar to `Rc::into_inner`.
1077    /// And while they are meant for different use-cases, `Rc::into_inner(this)`
1078    /// is in fact equivalent to <code>[Rc::try_unwrap]\(this).[ok][Result::ok]()</code>.
1079    /// (Note that the same kind of equivalence does **not** hold true for
1080    /// [`Arc`](crate::sync::Arc), due to race conditions that do not apply to `Rc`!)
1081    ///
1082    /// # Examples
1083    ///
1084    /// ```
1085    /// use std::rc::Rc;
1086    ///
1087    /// let x = Rc::new(3);
1088    /// assert_eq!(Rc::into_inner(x), Some(3));
1089    ///
1090    /// let x = Rc::new(4);
1091    /// let y = Rc::clone(&x);
1092    ///
1093    /// assert_eq!(Rc::into_inner(y), None);
1094    /// assert_eq!(Rc::into_inner(x), Some(4));
1095    /// ```
1096    #[inline]
1097    #[stable(feature = "rc_into_inner", since = "1.70.0")]
1098    pub fn into_inner(this: Self) -> Option<T> {
1099        Rc::try_unwrap(this).ok()
1100    }
1101}
1102
1103impl<T> Rc<[T]> {
1104    /// Constructs a new reference-counted slice with uninitialized contents.
1105    ///
1106    /// # Examples
1107    ///
1108    /// ```
1109    /// use std::rc::Rc;
1110    ///
1111    /// let mut values = Rc::<[u32]>::new_uninit_slice(3);
1112    ///
1113    /// // Deferred initialization:
1114    /// let data = Rc::get_mut(&mut values).unwrap();
1115    /// data[0].write(1);
1116    /// data[1].write(2);
1117    /// data[2].write(3);
1118    ///
1119    /// let values = unsafe { values.assume_init() };
1120    ///
1121    /// assert_eq!(*values, [1, 2, 3])
1122    /// ```
1123    #[cfg(not(no_global_oom_handling))]
1124    #[stable(feature = "new_uninit", since = "1.82.0")]
1125    #[must_use]
1126    pub fn new_uninit_slice(len: usize) -> Rc<[mem::MaybeUninit<T>]> {
1127        unsafe { Rc::from_ptr(Rc::allocate_for_slice(len)) }
1128    }
1129
1130    /// Constructs a new reference-counted slice with uninitialized contents, with the memory being
1131    /// filled with `0` bytes.
1132    ///
1133    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
1134    /// incorrect usage of this method.
1135    ///
1136    /// # Examples
1137    ///
1138    /// ```
1139    /// use std::rc::Rc;
1140    ///
1141    /// let values = Rc::<[u32]>::new_zeroed_slice(3);
1142    /// let values = unsafe { values.assume_init() };
1143    ///
1144    /// assert_eq!(*values, [0, 0, 0])
1145    /// ```
1146    ///
1147    /// [zeroed]: mem::MaybeUninit::zeroed
1148    #[cfg(not(no_global_oom_handling))]
1149    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
1150    #[must_use]
1151    pub fn new_zeroed_slice(len: usize) -> Rc<[mem::MaybeUninit<T>]> {
1152        unsafe {
1153            Rc::from_ptr(Rc::allocate_for_layout(
1154                Layout::array::<T>(len).unwrap(),
1155                |layout| Global.allocate_zeroed(layout),
1156                |mem| {
1157                    ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len)
1158                        as *mut RcInner<[mem::MaybeUninit<T>]>
1159                },
1160            ))
1161        }
1162    }
1163
1164    /// Converts the reference-counted slice into a reference-counted array.
1165    ///
1166    /// This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.
1167    ///
1168    /// If `N` is not exactly equal to the length of `self`, then this method returns `None`.
1169    #[unstable(feature = "alloc_slice_into_array", issue = "148082")]
1170    #[inline]
1171    #[must_use]
1172    pub fn into_array<const N: usize>(self) -> Option<Rc<[T; N]>> {
1173        if self.len() == N {
1174            let ptr = Self::into_raw(self) as *const [T; N];
1175
1176            // SAFETY: The underlying array of a slice has the exact same layout as an actual array `[T; N]` if `N` is equal to the slice's length.
1177            let me = unsafe { Rc::from_raw(ptr) };
1178            Some(me)
1179        } else {
1180            None
1181        }
1182    }
1183}
1184
1185impl<T, A: Allocator> Rc<[T], A> {
1186    /// Constructs a new reference-counted slice with uninitialized contents.
1187    ///
1188    /// # Examples
1189    ///
1190    /// ```
1191    /// #![feature(get_mut_unchecked)]
1192    /// #![feature(allocator_api)]
1193    ///
1194    /// use std::rc::Rc;
1195    /// use std::alloc::System;
1196    ///
1197    /// let mut values = Rc::<[u32], _>::new_uninit_slice_in(3, System);
1198    ///
1199    /// let values = unsafe {
1200    ///     // Deferred initialization:
1201    ///     Rc::get_mut_unchecked(&mut values)[0].as_mut_ptr().write(1);
1202    ///     Rc::get_mut_unchecked(&mut values)[1].as_mut_ptr().write(2);
1203    ///     Rc::get_mut_unchecked(&mut values)[2].as_mut_ptr().write(3);
1204    ///
1205    ///     values.assume_init()
1206    /// };
1207    ///
1208    /// assert_eq!(*values, [1, 2, 3])
1209    /// ```
1210    #[cfg(not(no_global_oom_handling))]
1211    #[unstable(feature = "allocator_api", issue = "32838")]
1212    #[inline]
1213    pub fn new_uninit_slice_in(len: usize, alloc: A) -> Rc<[mem::MaybeUninit<T>], A> {
1214        unsafe { Rc::from_ptr_in(Rc::allocate_for_slice_in(len, &alloc), alloc) }
1215    }
1216
1217    /// Constructs a new reference-counted slice with uninitialized contents, with the memory being
1218    /// filled with `0` bytes.
1219    ///
1220    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
1221    /// incorrect usage of this method.
1222    ///
1223    /// # Examples
1224    ///
1225    /// ```
1226    /// #![feature(allocator_api)]
1227    ///
1228    /// use std::rc::Rc;
1229    /// use std::alloc::System;
1230    ///
1231    /// let values = Rc::<[u32], _>::new_zeroed_slice_in(3, System);
1232    /// let values = unsafe { values.assume_init() };
1233    ///
1234    /// assert_eq!(*values, [0, 0, 0])
1235    /// ```
1236    ///
1237    /// [zeroed]: mem::MaybeUninit::zeroed
1238    #[cfg(not(no_global_oom_handling))]
1239    #[unstable(feature = "allocator_api", issue = "32838")]
1240    #[inline]
1241    pub fn new_zeroed_slice_in(len: usize, alloc: A) -> Rc<[mem::MaybeUninit<T>], A> {
1242        unsafe {
1243            Rc::from_ptr_in(
1244                Rc::allocate_for_layout(
1245                    Layout::array::<T>(len).unwrap(),
1246                    |layout| alloc.allocate_zeroed(layout),
1247                    |mem| {
1248                        ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len)
1249                            as *mut RcInner<[mem::MaybeUninit<T>]>
1250                    },
1251                ),
1252                alloc,
1253            )
1254        }
1255    }
1256}
1257
1258impl<T, A: Allocator> Rc<mem::MaybeUninit<T>, A> {
1259    /// Converts to `Rc<T>`.
1260    ///
1261    /// # Safety
1262    ///
1263    /// As with [`MaybeUninit::assume_init`],
1264    /// it is up to the caller to guarantee that the inner value
1265    /// really is in an initialized state.
1266    /// Calling this when the content is not yet fully initialized
1267    /// causes immediate undefined behavior.
1268    ///
1269    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1270    ///
1271    /// # Examples
1272    ///
1273    /// ```
1274    /// use std::rc::Rc;
1275    ///
1276    /// let mut five = Rc::<u32>::new_uninit();
1277    ///
1278    /// // Deferred initialization:
1279    /// Rc::get_mut(&mut five).unwrap().write(5);
1280    ///
1281    /// let five = unsafe { five.assume_init() };
1282    ///
1283    /// assert_eq!(*five, 5)
1284    /// ```
1285    #[stable(feature = "new_uninit", since = "1.82.0")]
1286    #[inline]
1287    pub unsafe fn assume_init(self) -> Rc<T, A> {
1288        let (ptr, alloc) = Rc::into_inner_with_allocator(self);
1289        unsafe { Rc::from_inner_in(ptr.cast(), alloc) }
1290    }
1291}
1292
1293impl<T: ?Sized + CloneToUninit> Rc<T> {
1294    /// Constructs a new `Rc<T>` with a clone of `value`.
1295    ///
1296    /// # Examples
1297    ///
1298    /// ```
1299    /// #![feature(clone_from_ref)]
1300    /// use std::rc::Rc;
1301    ///
1302    /// let hello: Rc<str> = Rc::clone_from_ref("hello");
1303    /// ```
1304    #[cfg(not(no_global_oom_handling))]
1305    #[unstable(feature = "clone_from_ref", issue = "149075")]
1306    pub fn clone_from_ref(value: &T) -> Rc<T> {
1307        Rc::clone_from_ref_in(value, Global)
1308    }
1309
1310    /// Constructs a new `Rc<T>` with a clone of `value`, returning an error if allocation fails
1311    ///
1312    /// # Examples
1313    ///
1314    /// ```
1315    /// #![feature(clone_from_ref)]
1316    /// #![feature(allocator_api)]
1317    /// use std::rc::Rc;
1318    ///
1319    /// let hello: Rc<str> = Rc::try_clone_from_ref("hello")?;
1320    /// # Ok::<(), std::alloc::AllocError>(())
1321    /// ```
1322    #[unstable(feature = "clone_from_ref", issue = "149075")]
1323    //#[unstable(feature = "allocator_api", issue = "32838")]
1324    pub fn try_clone_from_ref(value: &T) -> Result<Rc<T>, AllocError> {
1325        Rc::try_clone_from_ref_in(value, Global)
1326    }
1327}
1328
1329impl<T: ?Sized + CloneToUninit, A: Allocator> Rc<T, A> {
1330    /// Constructs a new `Rc<T>` with a clone of `value` in the provided allocator.
1331    ///
1332    /// # Examples
1333    ///
1334    /// ```
1335    /// #![feature(clone_from_ref)]
1336    /// #![feature(allocator_api)]
1337    /// use std::rc::Rc;
1338    /// use std::alloc::System;
1339    ///
1340    /// let hello: Rc<str, System> = Rc::clone_from_ref_in("hello", System);
1341    /// ```
1342    #[cfg(not(no_global_oom_handling))]
1343    #[unstable(feature = "clone_from_ref", issue = "149075")]
1344    //#[unstable(feature = "allocator_api", issue = "32838")]
1345    pub fn clone_from_ref_in(value: &T, alloc: A) -> Rc<T, A> {
1346        // `in_progress` drops the allocation if we panic before finishing initializing it.
1347        let mut in_progress: UniqueRcUninit<T, A> = UniqueRcUninit::new(value, alloc);
1348
1349        // Initialize with clone of value.
1350        let initialized_clone = unsafe {
1351            // Clone. If the clone panics, `in_progress` will be dropped and clean up.
1352            value.clone_to_uninit(in_progress.data_ptr().cast());
1353            // Cast type of pointer, now that it is initialized.
1354            in_progress.into_rc()
1355        };
1356
1357        initialized_clone
1358    }
1359
1360    /// Constructs a new `Rc<T>` with a clone of `value` in the provided allocator, returning an error if allocation fails
1361    ///
1362    /// # Examples
1363    ///
1364    /// ```
1365    /// #![feature(clone_from_ref)]
1366    /// #![feature(allocator_api)]
1367    /// use std::rc::Rc;
1368    /// use std::alloc::System;
1369    ///
1370    /// let hello: Rc<str, System> = Rc::try_clone_from_ref_in("hello", System)?;
1371    /// # Ok::<(), std::alloc::AllocError>(())
1372    /// ```
1373    #[unstable(feature = "clone_from_ref", issue = "149075")]
1374    //#[unstable(feature = "allocator_api", issue = "32838")]
1375    pub fn try_clone_from_ref_in(value: &T, alloc: A) -> Result<Rc<T, A>, AllocError> {
1376        // `in_progress` drops the allocation if we panic before finishing initializing it.
1377        let mut in_progress: UniqueRcUninit<T, A> = UniqueRcUninit::try_new(value, alloc)?;
1378
1379        // Initialize with clone of value.
1380        let initialized_clone = unsafe {
1381            // Clone. If the clone panics, `in_progress` will be dropped and clean up.
1382            value.clone_to_uninit(in_progress.data_ptr().cast());
1383            // Cast type of pointer, now that it is initialized.
1384            in_progress.into_rc()
1385        };
1386
1387        Ok(initialized_clone)
1388    }
1389}
1390
1391impl<T, A: Allocator> Rc<[mem::MaybeUninit<T>], A> {
1392    /// Converts to `Rc<[T]>`.
1393    ///
1394    /// # Safety
1395    ///
1396    /// As with [`MaybeUninit::assume_init`],
1397    /// it is up to the caller to guarantee that the inner value
1398    /// really is in an initialized state.
1399    /// Calling this when the content is not yet fully initialized
1400    /// causes immediate undefined behavior.
1401    ///
1402    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1403    ///
1404    /// # Examples
1405    ///
1406    /// ```
1407    /// use std::rc::Rc;
1408    ///
1409    /// let mut values = Rc::<[u32]>::new_uninit_slice(3);
1410    ///
1411    /// // Deferred initialization:
1412    /// let data = Rc::get_mut(&mut values).unwrap();
1413    /// data[0].write(1);
1414    /// data[1].write(2);
1415    /// data[2].write(3);
1416    ///
1417    /// let values = unsafe { values.assume_init() };
1418    ///
1419    /// assert_eq!(*values, [1, 2, 3])
1420    /// ```
1421    #[stable(feature = "new_uninit", since = "1.82.0")]
1422    #[inline]
1423    pub unsafe fn assume_init(self) -> Rc<[T], A> {
1424        let (ptr, alloc) = Rc::into_inner_with_allocator(self);
1425        unsafe { Rc::from_ptr_in(ptr.as_ptr() as _, alloc) }
1426    }
1427}
1428
1429impl<T: ?Sized> Rc<T> {
1430    /// Constructs an `Rc<T>` from a raw pointer.
1431    ///
1432    /// The raw pointer must have been previously returned by a call to
1433    /// [`Rc<U>::into_raw`][into_raw] with the following requirements:
1434    ///
1435    /// * If `U` is sized, it must have the same size and alignment as `T`. This
1436    ///   is trivially true if `U` is `T`.
1437    /// * If `U` is unsized, its data pointer must have the same size and
1438    ///   alignment as `T`. This is trivially true if `Rc<U>` was constructed
1439    ///   through `Rc<T>` and then converted to `Rc<U>` through an [unsized
1440    ///   coercion].
1441    ///
1442    /// Note that if `U` or `U`'s data pointer is not `T` but has the same size
1443    /// and alignment, this is basically like transmuting references of
1444    /// different types. See [`mem::transmute`][transmute] for more information
1445    /// on what restrictions apply in this case.
1446    ///
1447    /// The raw pointer must point to a block of memory allocated by the global allocator
1448    ///
1449    /// The user of `from_raw` has to make sure a specific value of `T` is only
1450    /// dropped once.
1451    ///
1452    /// This function is unsafe because improper use may lead to memory unsafety,
1453    /// even if the returned `Rc<T>` is never accessed.
1454    ///
1455    /// [into_raw]: Rc::into_raw
1456    /// [transmute]: core::mem::transmute
1457    /// [unsized coercion]: https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions
1458    ///
1459    /// # Examples
1460    ///
1461    /// ```
1462    /// use std::rc::Rc;
1463    ///
1464    /// let x = Rc::new("hello".to_owned());
1465    /// let x_ptr = Rc::into_raw(x);
1466    ///
1467    /// unsafe {
1468    ///     // Convert back to an `Rc` to prevent leak.
1469    ///     let x = Rc::from_raw(x_ptr);
1470    ///     assert_eq!(&*x, "hello");
1471    ///
1472    ///     // Further calls to `Rc::from_raw(x_ptr)` would be memory-unsafe.
1473    /// }
1474    ///
1475    /// // The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
1476    /// ```
1477    ///
1478    /// Convert a slice back into its original array:
1479    ///
1480    /// ```
1481    /// use std::rc::Rc;
1482    ///
1483    /// let x: Rc<[u32]> = Rc::new([1, 2, 3]);
1484    /// let x_ptr: *const [u32] = Rc::into_raw(x);
1485    ///
1486    /// unsafe {
1487    ///     let x: Rc<[u32; 3]> = Rc::from_raw(x_ptr.cast::<[u32; 3]>());
1488    ///     assert_eq!(&*x, &[1, 2, 3]);
1489    /// }
1490    /// ```
1491    #[inline]
1492    #[stable(feature = "rc_raw", since = "1.17.0")]
1493    pub unsafe fn from_raw(ptr: *const T) -> Self {
1494        unsafe { Self::from_raw_in(ptr, Global) }
1495    }
1496
1497    /// Consumes the `Rc`, returning the wrapped pointer.
1498    ///
1499    /// To avoid a memory leak the pointer must be converted back to an `Rc` using
1500    /// [`Rc::from_raw`].
1501    ///
1502    /// # Examples
1503    ///
1504    /// ```
1505    /// use std::rc::Rc;
1506    ///
1507    /// let x = Rc::new("hello".to_owned());
1508    /// let x_ptr = Rc::into_raw(x);
1509    /// assert_eq!(unsafe { &*x_ptr }, "hello");
1510    /// # // Prevent leaks for Miri.
1511    /// # drop(unsafe { Rc::from_raw(x_ptr) });
1512    /// ```
1513    #[must_use = "losing the pointer will leak memory"]
1514    #[stable(feature = "rc_raw", since = "1.17.0")]
1515    #[rustc_never_returns_null_ptr]
1516    pub fn into_raw(this: Self) -> *const T {
1517        let this = ManuallyDrop::new(this);
1518        Self::as_ptr(&*this)
1519    }
1520
1521    /// Increments the strong reference count on the `Rc<T>` associated with the
1522    /// provided pointer by one.
1523    ///
1524    /// # Safety
1525    ///
1526    /// The pointer must have been obtained through `Rc::into_raw` and must satisfy the
1527    /// same layout requirements specified in [`Rc::from_raw_in`][from_raw_in].
1528    /// The associated `Rc` instance must be valid (i.e. the strong count must be at
1529    /// least 1) for the duration of this method, and `ptr` must point to a block of memory
1530    /// allocated by the global allocator.
1531    ///
1532    /// [from_raw_in]: Rc::from_raw_in
1533    ///
1534    /// # Examples
1535    ///
1536    /// ```
1537    /// use std::rc::Rc;
1538    ///
1539    /// let five = Rc::new(5);
1540    ///
1541    /// unsafe {
1542    ///     let ptr = Rc::into_raw(five);
1543    ///     Rc::increment_strong_count(ptr);
1544    ///
1545    ///     let five = Rc::from_raw(ptr);
1546    ///     assert_eq!(2, Rc::strong_count(&five));
1547    /// #   // Prevent leaks for Miri.
1548    /// #   Rc::decrement_strong_count(ptr);
1549    /// }
1550    /// ```
1551    #[inline]
1552    #[stable(feature = "rc_mutate_strong_count", since = "1.53.0")]
1553    pub unsafe fn increment_strong_count(ptr: *const T) {
1554        unsafe { Self::increment_strong_count_in(ptr, Global) }
1555    }
1556
1557    /// Decrements the strong reference count on the `Rc<T>` associated with the
1558    /// provided pointer by one.
1559    ///
1560    /// # Safety
1561    ///
1562    /// The pointer must have been obtained through `Rc::into_raw`and must satisfy the
1563    /// same layout requirements specified in [`Rc::from_raw_in`][from_raw_in].
1564    /// The associated `Rc` instance must be valid (i.e. the strong count must be at
1565    /// least 1) when invoking this method, and `ptr` must point to a block of memory
1566    /// allocated by the global allocator. This method can be used to release the final `Rc` and
1567    /// backing storage, but **should not** be called after the final `Rc` has been released.
1568    ///
1569    /// [from_raw_in]: Rc::from_raw_in
1570    ///
1571    /// # Examples
1572    ///
1573    /// ```
1574    /// use std::rc::Rc;
1575    ///
1576    /// let five = Rc::new(5);
1577    ///
1578    /// unsafe {
1579    ///     let ptr = Rc::into_raw(five);
1580    ///     Rc::increment_strong_count(ptr);
1581    ///
1582    ///     let five = Rc::from_raw(ptr);
1583    ///     assert_eq!(2, Rc::strong_count(&five));
1584    ///     Rc::decrement_strong_count(ptr);
1585    ///     assert_eq!(1, Rc::strong_count(&five));
1586    /// }
1587    /// ```
1588    #[inline]
1589    #[stable(feature = "rc_mutate_strong_count", since = "1.53.0")]
1590    pub unsafe fn decrement_strong_count(ptr: *const T) {
1591        unsafe { Self::decrement_strong_count_in(ptr, Global) }
1592    }
1593}
1594
1595impl<T: ?Sized, A: Allocator> Rc<T, A> {
1596    /// Returns a reference to the underlying allocator.
1597    ///
1598    /// Note: this is an associated function, which means that you have
1599    /// to call it as `Rc::allocator(&r)` instead of `r.allocator()`. This
1600    /// is so that there is no conflict with a method on the inner type.
1601    #[inline]
1602    #[unstable(feature = "allocator_api", issue = "32838")]
1603    pub fn allocator(this: &Self) -> &A {
1604        &this.alloc
1605    }
1606
1607    /// Consumes the `Rc`, returning the wrapped pointer and allocator.
1608    ///
1609    /// To avoid a memory leak the pointer must be converted back to an `Rc` using
1610    /// [`Rc::from_raw_in`].
1611    ///
1612    /// # Examples
1613    ///
1614    /// ```
1615    /// #![feature(allocator_api)]
1616    /// use std::rc::Rc;
1617    /// use std::alloc::System;
1618    ///
1619    /// let x = Rc::new_in("hello".to_owned(), System);
1620    /// let (ptr, alloc) = Rc::into_raw_with_allocator(x);
1621    /// assert_eq!(unsafe { &*ptr }, "hello");
1622    /// let x = unsafe { Rc::from_raw_in(ptr, alloc) };
1623    /// assert_eq!(&*x, "hello");
1624    /// ```
1625    #[must_use = "losing the pointer will leak memory"]
1626    #[unstable(feature = "allocator_api", issue = "32838")]
1627    pub fn into_raw_with_allocator(this: Self) -> (*const T, A) {
1628        let this = mem::ManuallyDrop::new(this);
1629        let ptr = Self::as_ptr(&this);
1630        // Safety: `this` is ManuallyDrop so the allocator will not be double-dropped
1631        let alloc = unsafe { ptr::read(&this.alloc) };
1632        (ptr, alloc)
1633    }
1634
1635    /// Provides a raw pointer to the data.
1636    ///
1637    /// The counts are not affected in any way and the `Rc` is not consumed. The pointer is valid
1638    /// for as long as there are strong counts in the `Rc`.
1639    ///
1640    /// # Examples
1641    ///
1642    /// ```
1643    /// use std::rc::Rc;
1644    ///
1645    /// let x = Rc::new(0);
1646    /// let y = Rc::clone(&x);
1647    /// let x_ptr = Rc::as_ptr(&x);
1648    /// assert_eq!(x_ptr, Rc::as_ptr(&y));
1649    /// assert_eq!(unsafe { *x_ptr }, 0);
1650    /// ```
1651    #[stable(feature = "weak_into_raw", since = "1.45.0")]
1652    #[rustc_never_returns_null_ptr]
1653    pub fn as_ptr(this: &Self) -> *const T {
1654        let ptr: *mut RcInner<T> = NonNull::as_ptr(this.ptr);
1655
1656        // SAFETY: This cannot go through Deref::deref or Rc::inner because
1657        // this is required to retain raw/mut provenance such that e.g. `get_mut` can
1658        // write through the pointer after the Rc is recovered through `from_raw`.
1659        unsafe { &raw mut (*ptr).value }
1660    }
1661
1662    /// Constructs an `Rc<T, A>` from a raw pointer in the provided allocator.
1663    ///
1664    /// The raw pointer must have been previously returned by a call to [`Rc<U,
1665    /// A>::into_raw`][into_raw] with the following requirements:
1666    ///
1667    /// * If `U` is sized, it must have the same size and alignment as `T`. This
1668    ///   is trivially true if `U` is `T`.
1669    /// * If `U` is unsized, its data pointer must have the same size and
1670    ///   alignment as `T`. This is trivially true if `Rc<U>` was constructed
1671    ///   through `Rc<T>` and then converted to `Rc<U>` through an [unsized
1672    ///   coercion].
1673    ///
1674    /// Note that if `U` or `U`'s data pointer is not `T` but has the same size
1675    /// and alignment, this is basically like transmuting references of
1676    /// different types. See [`mem::transmute`][transmute] for more information
1677    /// on what restrictions apply in this case.
1678    ///
1679    /// The raw pointer must point to a block of memory allocated by `alloc`
1680    ///
1681    /// The user of `from_raw` has to make sure a specific value of `T` is only
1682    /// dropped once.
1683    ///
1684    /// This function is unsafe because improper use may lead to memory unsafety,
1685    /// even if the returned `Rc<T>` is never accessed.
1686    ///
1687    /// [into_raw]: Rc::into_raw
1688    /// [transmute]: core::mem::transmute
1689    /// [unsized coercion]: https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions
1690    ///
1691    /// # Examples
1692    ///
1693    /// ```
1694    /// #![feature(allocator_api)]
1695    ///
1696    /// use std::rc::Rc;
1697    /// use std::alloc::System;
1698    ///
1699    /// let x = Rc::new_in("hello".to_owned(), System);
1700    /// let (x_ptr, _alloc) = Rc::into_raw_with_allocator(x);
1701    ///
1702    /// unsafe {
1703    ///     // Convert back to an `Rc` to prevent leak.
1704    ///     let x = Rc::from_raw_in(x_ptr, System);
1705    ///     assert_eq!(&*x, "hello");
1706    ///
1707    ///     // Further calls to `Rc::from_raw(x_ptr)` would be memory-unsafe.
1708    /// }
1709    ///
1710    /// // The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
1711    /// ```
1712    ///
1713    /// Convert a slice back into its original array:
1714    ///
1715    /// ```
1716    /// #![feature(allocator_api)]
1717    ///
1718    /// use std::rc::Rc;
1719    /// use std::alloc::System;
1720    ///
1721    /// let x: Rc<[u32], _> = Rc::new_in([1, 2, 3], System);
1722    /// let x_ptr: *const [u32] = Rc::into_raw_with_allocator(x).0;
1723    ///
1724    /// unsafe {
1725    ///     let x: Rc<[u32; 3], _> = Rc::from_raw_in(x_ptr.cast::<[u32; 3]>(), System);
1726    ///     assert_eq!(&*x, &[1, 2, 3]);
1727    /// }
1728    /// ```
1729    #[unstable(feature = "allocator_api", issue = "32838")]
1730    pub unsafe fn from_raw_in(ptr: *const T, alloc: A) -> Self {
1731        let offset = unsafe { data_offset(ptr) };
1732
1733        // Reverse the offset to find the original RcInner.
1734        let rc_ptr = unsafe { ptr.byte_sub(offset) as *mut RcInner<T> };
1735
1736        unsafe { Self::from_ptr_in(rc_ptr, alloc) }
1737    }
1738
1739    /// Creates a new [`Weak`] pointer to this allocation.
1740    ///
1741    /// # Examples
1742    ///
1743    /// ```
1744    /// use std::rc::Rc;
1745    ///
1746    /// let five = Rc::new(5);
1747    ///
1748    /// let weak_five = Rc::downgrade(&five);
1749    /// ```
1750    #[must_use = "this returns a new `Weak` pointer, \
1751                  without modifying the original `Rc`"]
1752    #[stable(feature = "rc_weak", since = "1.4.0")]
1753    pub fn downgrade(this: &Self) -> Weak<T, A>
1754    where
1755        A: Clone,
1756    {
1757        this.inner().inc_weak();
1758        // Make sure we do not create a dangling Weak
1759        debug_assert!(!is_dangling(this.ptr.as_ptr()));
1760        Weak { ptr: this.ptr, alloc: this.alloc.clone() }
1761    }
1762
1763    /// Gets the number of [`Weak`] pointers to this allocation.
1764    ///
1765    /// # Examples
1766    ///
1767    /// ```
1768    /// use std::rc::Rc;
1769    ///
1770    /// let five = Rc::new(5);
1771    /// let _weak_five = Rc::downgrade(&five);
1772    ///
1773    /// assert_eq!(1, Rc::weak_count(&five));
1774    /// ```
1775    #[inline]
1776    #[stable(feature = "rc_counts", since = "1.15.0")]
1777    pub fn weak_count(this: &Self) -> usize {
1778        this.inner().weak() - 1
1779    }
1780
1781    /// Gets the number of strong (`Rc`) pointers to this allocation.
1782    ///
1783    /// # Examples
1784    ///
1785    /// ```
1786    /// use std::rc::Rc;
1787    ///
1788    /// let five = Rc::new(5);
1789    /// let _also_five = Rc::clone(&five);
1790    ///
1791    /// assert_eq!(2, Rc::strong_count(&five));
1792    /// ```
1793    #[inline]
1794    #[stable(feature = "rc_counts", since = "1.15.0")]
1795    pub fn strong_count(this: &Self) -> usize {
1796        this.inner().strong()
1797    }
1798
1799    /// Increments the strong reference count on the `Rc<T>` associated with the
1800    /// provided pointer by one.
1801    ///
1802    /// # Safety
1803    ///
1804    /// The pointer must have been obtained through `Rc::into_raw` and must satisfy the
1805    /// same layout requirements specified in [`Rc::from_raw_in`][from_raw_in].
1806    /// The associated `Rc` instance must be valid (i.e. the strong count must be at
1807    /// least 1) for the duration of this method, and `ptr` must point to a block of memory
1808    /// allocated by `alloc`.
1809    ///
1810    /// [from_raw_in]: Rc::from_raw_in
1811    ///
1812    /// # Examples
1813    ///
1814    /// ```
1815    /// #![feature(allocator_api)]
1816    ///
1817    /// use std::rc::Rc;
1818    /// use std::alloc::System;
1819    ///
1820    /// let five = Rc::new_in(5, System);
1821    ///
1822    /// unsafe {
1823    ///     let (ptr, _alloc) = Rc::into_raw_with_allocator(five);
1824    ///     Rc::increment_strong_count_in(ptr, System);
1825    ///
1826    ///     let five = Rc::from_raw_in(ptr, System);
1827    ///     assert_eq!(2, Rc::strong_count(&five));
1828    /// #   // Prevent leaks for Miri.
1829    /// #   Rc::decrement_strong_count_in(ptr, System);
1830    /// }
1831    /// ```
1832    #[inline]
1833    #[unstable(feature = "allocator_api", issue = "32838")]
1834    pub unsafe fn increment_strong_count_in(ptr: *const T, alloc: A)
1835    where
1836        A: Clone,
1837    {
1838        // Retain Rc, but don't touch refcount by wrapping in ManuallyDrop
1839        let rc = unsafe { mem::ManuallyDrop::new(Rc::<T, A>::from_raw_in(ptr, alloc)) };
1840        // Now increase refcount, but don't drop new refcount either
1841        let _rc_clone: mem::ManuallyDrop<_> = rc.clone();
1842    }
1843
1844    /// Decrements the strong reference count on the `Rc<T>` associated with the
1845    /// provided pointer by one.
1846    ///
1847    /// # Safety
1848    ///
1849    /// The pointer must have been obtained through `Rc::into_raw`and must satisfy the
1850    /// same layout requirements specified in [`Rc::from_raw_in`][from_raw_in].
1851    /// The associated `Rc` instance must be valid (i.e. the strong count must be at
1852    /// least 1) when invoking this method, and `ptr` must point to a block of memory
1853    /// allocated by `alloc`. This method can be used to release the final `Rc` and
1854    /// backing storage, but **should not** be called after the final `Rc` has been released.
1855    ///
1856    /// [from_raw_in]: Rc::from_raw_in
1857    ///
1858    /// # Examples
1859    ///
1860    /// ```
1861    /// #![feature(allocator_api)]
1862    ///
1863    /// use std::rc::Rc;
1864    /// use std::alloc::System;
1865    ///
1866    /// let five = Rc::new_in(5, System);
1867    ///
1868    /// unsafe {
1869    ///     let (ptr, _alloc) = Rc::into_raw_with_allocator(five);
1870    ///     Rc::increment_strong_count_in(ptr, System);
1871    ///
1872    ///     let five = Rc::from_raw_in(ptr, System);
1873    ///     assert_eq!(2, Rc::strong_count(&five));
1874    ///     Rc::decrement_strong_count_in(ptr, System);
1875    ///     assert_eq!(1, Rc::strong_count(&five));
1876    /// }
1877    /// ```
1878    #[inline]
1879    #[unstable(feature = "allocator_api", issue = "32838")]
1880    pub unsafe fn decrement_strong_count_in(ptr: *const T, alloc: A) {
1881        unsafe { drop(Rc::from_raw_in(ptr, alloc)) };
1882    }
1883
1884    /// Returns `true` if there are no other `Rc` or [`Weak`] pointers to
1885    /// this allocation.
1886    #[inline]
1887    fn is_unique(this: &Self) -> bool {
1888        Rc::weak_count(this) == 0 && Rc::strong_count(this) == 1
1889    }
1890
1891    /// Returns a mutable reference into the given `Rc`, if there are
1892    /// no other `Rc` or [`Weak`] pointers to the same allocation.
1893    ///
1894    /// Returns [`None`] otherwise, because it is not safe to
1895    /// mutate a shared value.
1896    ///
1897    /// See also [`make_mut`][make_mut], which will [`clone`][clone]
1898    /// the inner value when there are other `Rc` pointers.
1899    ///
1900    /// [make_mut]: Rc::make_mut
1901    /// [clone]: Clone::clone
1902    ///
1903    /// # Examples
1904    ///
1905    /// ```
1906    /// use std::rc::Rc;
1907    ///
1908    /// let mut x = Rc::new(3);
1909    /// *Rc::get_mut(&mut x).unwrap() = 4;
1910    /// assert_eq!(*x, 4);
1911    ///
1912    /// let _y = Rc::clone(&x);
1913    /// assert!(Rc::get_mut(&mut x).is_none());
1914    /// ```
1915    #[inline]
1916    #[stable(feature = "rc_unique", since = "1.4.0")]
1917    pub fn get_mut(this: &mut Self) -> Option<&mut T> {
1918        if Rc::is_unique(this) { unsafe { Some(Rc::get_mut_unchecked(this)) } } else { None }
1919    }
1920
1921    /// Returns a mutable reference into the given `Rc`,
1922    /// without any check.
1923    ///
1924    /// See also [`get_mut`], which is safe and does appropriate checks.
1925    ///
1926    /// [`get_mut`]: Rc::get_mut
1927    ///
1928    /// # Safety
1929    ///
1930    /// If any other `Rc` or [`Weak`] pointers to the same allocation exist, then
1931    /// they must not be dereferenced or have active borrows for the duration
1932    /// of the returned borrow, and their inner type must be exactly the same as the
1933    /// inner type of this Rc (including lifetimes). This is trivially the case if no
1934    /// such pointers exist, for example immediately after `Rc::new`.
1935    ///
1936    /// # Examples
1937    ///
1938    /// ```
1939    /// #![feature(get_mut_unchecked)]
1940    ///
1941    /// use std::rc::Rc;
1942    ///
1943    /// let mut x = Rc::new(String::new());
1944    /// unsafe {
1945    ///     Rc::get_mut_unchecked(&mut x).push_str("foo")
1946    /// }
1947    /// assert_eq!(*x, "foo");
1948    /// ```
1949    /// Other `Rc` pointers to the same allocation must be to the same type.
1950    /// ```no_run
1951    /// #![feature(get_mut_unchecked)]
1952    ///
1953    /// use std::rc::Rc;
1954    ///
1955    /// let x: Rc<str> = Rc::from("Hello, world!");
1956    /// let mut y: Rc<[u8]> = x.clone().into();
1957    /// unsafe {
1958    ///     // this is Undefined Behavior, because x's inner type is str, not [u8]
1959    ///     Rc::get_mut_unchecked(&mut y).fill(0xff); // 0xff is invalid in UTF-8
1960    /// }
1961    /// println!("{}", &*x); // Invalid UTF-8 in a str
1962    /// ```
1963    /// Other `Rc` pointers to the same allocation must be to the exact same type, including lifetimes.
1964    /// ```no_run
1965    /// #![feature(get_mut_unchecked)]
1966    ///
1967    /// use std::rc::Rc;
1968    ///
1969    /// let x: Rc<&str> = Rc::new("Hello, world!");
1970    /// {
1971    ///     let s = String::from("Oh, no!");
1972    ///     let mut y: Rc<&str> = x.clone();
1973    ///     unsafe {
1974    ///         // this is Undefined Behavior, because x's inner type
1975    ///         // is &'long str, not &'short str
1976    ///         *Rc::get_mut_unchecked(&mut y) = &s;
1977    ///     }
1978    /// }
1979    /// println!("{}", &*x); // Use-after-free
1980    /// ```
1981    #[inline]
1982    #[unstable(feature = "get_mut_unchecked", issue = "63292")]
1983    pub unsafe fn get_mut_unchecked(this: &mut Self) -> &mut T {
1984        // We are careful to *not* create a reference covering the "count" fields, as
1985        // this would conflict with accesses to the reference counts (e.g. by `Weak`).
1986        unsafe { &mut (*this.ptr.as_ptr()).value }
1987    }
1988
1989    #[inline]
1990    #[stable(feature = "ptr_eq", since = "1.17.0")]
1991    /// Returns `true` if the two `Rc`s point to the same allocation in a vein similar to
1992    /// [`ptr::eq`]. This function ignores the metadata of  `dyn Trait` pointers.
1993    ///
1994    /// # Examples
1995    ///
1996    /// ```
1997    /// use std::rc::Rc;
1998    ///
1999    /// let five = Rc::new(5);
2000    /// let same_five = Rc::clone(&five);
2001    /// let other_five = Rc::new(5);
2002    ///
2003    /// assert!(Rc::ptr_eq(&five, &same_five));
2004    /// assert!(!Rc::ptr_eq(&five, &other_five));
2005    /// ```
2006    pub fn ptr_eq(this: &Self, other: &Self) -> bool {
2007        ptr::addr_eq(this.ptr.as_ptr(), other.ptr.as_ptr())
2008    }
2009}
2010
2011#[cfg(not(no_global_oom_handling))]
2012impl<T: ?Sized + CloneToUninit, A: Allocator + Clone> Rc<T, A> {
2013    /// Makes a mutable reference into the given `Rc`.
2014    ///
2015    /// If there are other `Rc` pointers to the same allocation, then `make_mut` will
2016    /// [`clone`] the inner value to a new allocation to ensure unique ownership.  This is also
2017    /// referred to as clone-on-write.
2018    ///
2019    /// However, if there are no other `Rc` pointers to this allocation, but some [`Weak`]
2020    /// pointers, then the [`Weak`] pointers will be disassociated and the inner value will not
2021    /// be cloned.
2022    ///
2023    /// See also [`get_mut`], which will fail rather than cloning the inner value
2024    /// or disassociating [`Weak`] pointers.
2025    ///
2026    /// [`clone`]: Clone::clone
2027    /// [`get_mut`]: Rc::get_mut
2028    ///
2029    /// # Examples
2030    ///
2031    /// ```
2032    /// use std::rc::Rc;
2033    ///
2034    /// let mut data = Rc::new(5);
2035    ///
2036    /// *Rc::make_mut(&mut data) += 1;         // Won't clone anything
2037    /// let mut other_data = Rc::clone(&data); // Won't clone inner data
2038    /// *Rc::make_mut(&mut data) += 1;         // Clones inner data
2039    /// *Rc::make_mut(&mut data) += 1;         // Won't clone anything
2040    /// *Rc::make_mut(&mut other_data) *= 2;   // Won't clone anything
2041    ///
2042    /// // Now `data` and `other_data` point to different allocations.
2043    /// assert_eq!(*data, 8);
2044    /// assert_eq!(*other_data, 12);
2045    /// ```
2046    ///
2047    /// [`Weak`] pointers will be disassociated:
2048    ///
2049    /// ```
2050    /// use std::rc::Rc;
2051    ///
2052    /// let mut data = Rc::new(75);
2053    /// let weak = Rc::downgrade(&data);
2054    ///
2055    /// assert!(75 == *data);
2056    /// assert!(75 == *weak.upgrade().unwrap());
2057    ///
2058    /// *Rc::make_mut(&mut data) += 1;
2059    ///
2060    /// assert!(76 == *data);
2061    /// assert!(weak.upgrade().is_none());
2062    /// ```
2063    #[inline]
2064    #[stable(feature = "rc_unique", since = "1.4.0")]
2065    pub fn make_mut(this: &mut Self) -> &mut T {
2066        let size_of_val = size_of_val::<T>(&**this);
2067
2068        if Rc::strong_count(this) != 1 {
2069            // Gotta clone the data, there are other Rcs.
2070            *this = Rc::clone_from_ref_in(&**this, this.alloc.clone());
2071        } else if Rc::weak_count(this) != 0 {
2072            // Can just steal the data, all that's left is Weaks
2073
2074            // We don't need panic-protection like the above branch does, but we might as well
2075            // use the same mechanism.
2076            let mut in_progress: UniqueRcUninit<T, A> =
2077                UniqueRcUninit::new(&**this, this.alloc.clone());
2078            unsafe {
2079                // Initialize `in_progress` with move of **this.
2080                // We have to express this in terms of bytes because `T: ?Sized`; there is no
2081                // operation that just copies a value based on its `size_of_val()`.
2082                ptr::copy_nonoverlapping(
2083                    ptr::from_ref(&**this).cast::<u8>(),
2084                    in_progress.data_ptr().cast::<u8>(),
2085                    size_of_val,
2086                );
2087
2088                this.inner().dec_strong();
2089                // Remove implicit strong-weak ref (no need to craft a fake
2090                // Weak here -- we know other Weaks can clean up for us)
2091                this.inner().dec_weak();
2092                // Replace `this` with newly constructed Rc that has the moved data.
2093                ptr::write(this, in_progress.into_rc());
2094            }
2095        }
2096        // This unsafety is ok because we're guaranteed that the pointer
2097        // returned is the *only* pointer that will ever be returned to T. Our
2098        // reference count is guaranteed to be 1 at this point, and we required
2099        // the `Rc<T>` itself to be `mut`, so we're returning the only possible
2100        // reference to the allocation.
2101        unsafe { &mut this.ptr.as_mut().value }
2102    }
2103}
2104
2105impl<T: Clone, A: Allocator> Rc<T, A> {
2106    /// If we have the only reference to `T` then unwrap it. Otherwise, clone `T` and return the
2107    /// clone.
2108    ///
2109    /// Assuming `rc_t` is of type `Rc<T>`, this function is functionally equivalent to
2110    /// `(*rc_t).clone()`, but will avoid cloning the inner value where possible.
2111    ///
2112    /// # Examples
2113    ///
2114    /// ```
2115    /// # use std::{ptr, rc::Rc};
2116    /// let inner = String::from("test");
2117    /// let ptr = inner.as_ptr();
2118    ///
2119    /// let rc = Rc::new(inner);
2120    /// let inner = Rc::unwrap_or_clone(rc);
2121    /// // The inner value was not cloned
2122    /// assert!(ptr::eq(ptr, inner.as_ptr()));
2123    ///
2124    /// let rc = Rc::new(inner);
2125    /// let rc2 = rc.clone();
2126    /// let inner = Rc::unwrap_or_clone(rc);
2127    /// // Because there were 2 references, we had to clone the inner value.
2128    /// assert!(!ptr::eq(ptr, inner.as_ptr()));
2129    /// // `rc2` is the last reference, so when we unwrap it we get back
2130    /// // the original `String`.
2131    /// let inner = Rc::unwrap_or_clone(rc2);
2132    /// assert!(ptr::eq(ptr, inner.as_ptr()));
2133    /// ```
2134    #[inline]
2135    #[stable(feature = "arc_unwrap_or_clone", since = "1.76.0")]
2136    pub fn unwrap_or_clone(this: Self) -> T {
2137        Rc::try_unwrap(this).unwrap_or_else(|rc| (*rc).clone())
2138    }
2139}
2140
2141impl<A: Allocator> Rc<dyn Any, A> {
2142    /// Attempts to downcast the `Rc<dyn Any>` to a concrete type.
2143    ///
2144    /// # Examples
2145    ///
2146    /// ```
2147    /// use std::any::Any;
2148    /// use std::rc::Rc;
2149    ///
2150    /// fn print_if_string(value: Rc<dyn Any>) {
2151    ///     if let Ok(string) = value.downcast::<String>() {
2152    ///         println!("String ({}): {}", string.len(), string);
2153    ///     }
2154    /// }
2155    ///
2156    /// let my_string = "Hello World".to_string();
2157    /// print_if_string(Rc::new(my_string));
2158    /// print_if_string(Rc::new(0i8));
2159    /// ```
2160    #[inline]
2161    #[stable(feature = "rc_downcast", since = "1.29.0")]
2162    pub fn downcast<T: Any>(self) -> Result<Rc<T, A>, Self> {
2163        if (*self).is::<T>() {
2164            unsafe {
2165                let (ptr, alloc) = Rc::into_inner_with_allocator(self);
2166                Ok(Rc::from_inner_in(ptr.cast(), alloc))
2167            }
2168        } else {
2169            Err(self)
2170        }
2171    }
2172
2173    /// Downcasts the `Rc<dyn Any>` to a concrete type.
2174    ///
2175    /// For a safe alternative see [`downcast`].
2176    ///
2177    /// # Examples
2178    ///
2179    /// ```
2180    /// #![feature(downcast_unchecked)]
2181    ///
2182    /// use std::any::Any;
2183    /// use std::rc::Rc;
2184    ///
2185    /// let x: Rc<dyn Any> = Rc::new(1_usize);
2186    ///
2187    /// unsafe {
2188    ///     assert_eq!(*x.downcast_unchecked::<usize>(), 1);
2189    /// }
2190    /// ```
2191    ///
2192    /// # Safety
2193    ///
2194    /// The contained value must be of type `T`. Calling this method
2195    /// with the incorrect type is *undefined behavior*.
2196    ///
2197    ///
2198    /// [`downcast`]: Self::downcast
2199    #[inline]
2200    #[unstable(feature = "downcast_unchecked", issue = "90850")]
2201    pub unsafe fn downcast_unchecked<T: Any>(self) -> Rc<T, A> {
2202        unsafe {
2203            let (ptr, alloc) = Rc::into_inner_with_allocator(self);
2204            Rc::from_inner_in(ptr.cast(), alloc)
2205        }
2206    }
2207}
2208
2209impl<T: ?Sized> Rc<T> {
2210    /// Allocates an `RcInner<T>` with sufficient space for
2211    /// a possibly-unsized inner value where the value has the layout provided.
2212    ///
2213    /// The function `mem_to_rc_inner` is called with the data pointer
2214    /// and must return back a (potentially fat)-pointer for the `RcInner<T>`.
2215    #[cfg(not(no_global_oom_handling))]
2216    unsafe fn allocate_for_layout(
2217        value_layout: Layout,
2218        allocate: impl FnOnce(Layout) -> Result<NonNull<[u8]>, AllocError>,
2219        mem_to_rc_inner: impl FnOnce(*mut u8) -> *mut RcInner<T>,
2220    ) -> *mut RcInner<T> {
2221        let layout = rc_inner_layout_for_value_layout(value_layout);
2222        unsafe {
2223            Rc::try_allocate_for_layout(value_layout, allocate, mem_to_rc_inner)
2224                .unwrap_or_else(|_| handle_alloc_error(layout))
2225        }
2226    }
2227
2228    /// Allocates an `RcInner<T>` with sufficient space for
2229    /// a possibly-unsized inner value where the value has the layout provided,
2230    /// returning an error if allocation fails.
2231    ///
2232    /// The function `mem_to_rc_inner` is called with the data pointer
2233    /// and must return back a (potentially fat)-pointer for the `RcInner<T>`.
2234    #[inline]
2235    unsafe fn try_allocate_for_layout(
2236        value_layout: Layout,
2237        allocate: impl FnOnce(Layout) -> Result<NonNull<[u8]>, AllocError>,
2238        mem_to_rc_inner: impl FnOnce(*mut u8) -> *mut RcInner<T>,
2239    ) -> Result<*mut RcInner<T>, AllocError> {
2240        let layout = rc_inner_layout_for_value_layout(value_layout);
2241
2242        // Allocate for the layout.
2243        let ptr = allocate(layout)?;
2244
2245        // Initialize the RcInner
2246        let inner = mem_to_rc_inner(ptr.as_non_null_ptr().as_ptr());
2247        unsafe {
2248            debug_assert_eq!(Layout::for_value_raw(inner), layout);
2249
2250            (&raw mut (*inner).strong).write(Cell::new(1));
2251            (&raw mut (*inner).weak).write(Cell::new(1));
2252        }
2253
2254        Ok(inner)
2255    }
2256}
2257
2258impl<T: ?Sized, A: Allocator> Rc<T, A> {
2259    /// Allocates an `RcInner<T>` with sufficient space for an unsized inner value
2260    #[cfg(not(no_global_oom_handling))]
2261    unsafe fn allocate_for_ptr_in(ptr: *const T, alloc: &A) -> *mut RcInner<T> {
2262        // Allocate for the `RcInner<T>` using the given value.
2263        unsafe {
2264            Rc::<T>::allocate_for_layout(
2265                Layout::for_value_raw(ptr),
2266                |layout| alloc.allocate(layout),
2267                |mem| mem.with_metadata_of(ptr as *const RcInner<T>),
2268            )
2269        }
2270    }
2271
2272    #[cfg(not(no_global_oom_handling))]
2273    fn from_box_in(src: Box<T, A>) -> Rc<T, A> {
2274        unsafe {
2275            let value_size = size_of_val(&*src);
2276            let ptr = Self::allocate_for_ptr_in(&*src, Box::allocator(&src));
2277
2278            // Copy value as bytes
2279            ptr::copy_nonoverlapping(
2280                (&raw const *src) as *const u8,
2281                (&raw mut (*ptr).value) as *mut u8,
2282                value_size,
2283            );
2284
2285            // Free the allocation without dropping its contents
2286            let (bptr, alloc) = Box::into_raw_with_allocator(src);
2287            let src = Box::from_raw_in(bptr as *mut mem::ManuallyDrop<T>, alloc.by_ref());
2288            drop(src);
2289
2290            Self::from_ptr_in(ptr, alloc)
2291        }
2292    }
2293}
2294
2295impl<T> Rc<[T]> {
2296    /// Allocates an `RcInner<[T]>` with the given length.
2297    #[cfg(not(no_global_oom_handling))]
2298    unsafe fn allocate_for_slice(len: usize) -> *mut RcInner<[T]> {
2299        unsafe {
2300            Self::allocate_for_layout(
2301                Layout::array::<T>(len).unwrap(),
2302                |layout| Global.allocate(layout),
2303                |mem| ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len) as *mut RcInner<[T]>,
2304            )
2305        }
2306    }
2307
2308    /// Copy elements from slice into newly allocated `Rc<[T]>`
2309    ///
2310    /// Unsafe because the caller must either take ownership, bind `T: Copy` or
2311    /// bind `T: TrivialClone`.
2312    #[cfg(not(no_global_oom_handling))]
2313    unsafe fn copy_from_slice(v: &[T]) -> Rc<[T]> {
2314        unsafe {
2315            let ptr = Self::allocate_for_slice(v.len());
2316            ptr::copy_nonoverlapping(v.as_ptr(), (&raw mut (*ptr).value) as *mut T, v.len());
2317            Self::from_ptr(ptr)
2318        }
2319    }
2320
2321    /// Constructs an `Rc<[T]>` from an iterator known to be of a certain size.
2322    ///
2323    /// Behavior is undefined should the size be wrong.
2324    #[cfg(not(no_global_oom_handling))]
2325    unsafe fn from_iter_exact(iter: impl Iterator<Item = T>, len: usize) -> Rc<[T]> {
2326        // Panic guard while cloning T elements.
2327        // In the event of a panic, elements that have been written
2328        // into the new RcInner will be dropped, then the memory freed.
2329        struct Guard<T> {
2330            mem: NonNull<u8>,
2331            elems: *mut T,
2332            layout: Layout,
2333            n_elems: usize,
2334        }
2335
2336        impl<T> Drop for Guard<T> {
2337            fn drop(&mut self) {
2338                unsafe {
2339                    let slice = from_raw_parts_mut(self.elems, self.n_elems);
2340                    ptr::drop_in_place(slice);
2341
2342                    Global.deallocate(self.mem, self.layout);
2343                }
2344            }
2345        }
2346
2347        unsafe {
2348            let ptr = Self::allocate_for_slice(len);
2349
2350            let mem = ptr as *mut _ as *mut u8;
2351            let layout = Layout::for_value_raw(ptr);
2352
2353            // Pointer to first element
2354            let elems = (&raw mut (*ptr).value) as *mut T;
2355
2356            let mut guard = Guard { mem: NonNull::new_unchecked(mem), elems, layout, n_elems: 0 };
2357
2358            for (i, item) in iter.enumerate() {
2359                ptr::write(elems.add(i), item);
2360                guard.n_elems += 1;
2361            }
2362
2363            // All clear. Forget the guard so it doesn't free the new RcInner.
2364            mem::forget(guard);
2365
2366            Self::from_ptr(ptr)
2367        }
2368    }
2369}
2370
2371impl<T, A: Allocator> Rc<[T], A> {
2372    /// Allocates an `RcInner<[T]>` with the given length.
2373    #[inline]
2374    #[cfg(not(no_global_oom_handling))]
2375    unsafe fn allocate_for_slice_in(len: usize, alloc: &A) -> *mut RcInner<[T]> {
2376        unsafe {
2377            Rc::<[T]>::allocate_for_layout(
2378                Layout::array::<T>(len).unwrap(),
2379                |layout| alloc.allocate(layout),
2380                |mem| ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len) as *mut RcInner<[T]>,
2381            )
2382        }
2383    }
2384}
2385
2386#[cfg(not(no_global_oom_handling))]
2387/// Specialization trait used for `From<&[T]>`.
2388trait RcFromSlice<T> {
2389    fn from_slice(slice: &[T]) -> Self;
2390}
2391
2392#[cfg(not(no_global_oom_handling))]
2393impl<T: Clone> RcFromSlice<T> for Rc<[T]> {
2394    #[inline]
2395    default fn from_slice(v: &[T]) -> Self {
2396        unsafe { Self::from_iter_exact(v.iter().cloned(), v.len()) }
2397    }
2398}
2399
2400#[cfg(not(no_global_oom_handling))]
2401impl<T: TrivialClone> RcFromSlice<T> for Rc<[T]> {
2402    #[inline]
2403    fn from_slice(v: &[T]) -> Self {
2404        // SAFETY: `T` implements `TrivialClone`, so this is sound and equivalent
2405        // to the above.
2406        unsafe { Rc::copy_from_slice(v) }
2407    }
2408}
2409
2410#[stable(feature = "rust1", since = "1.0.0")]
2411impl<T: ?Sized, A: Allocator> Deref for Rc<T, A> {
2412    type Target = T;
2413
2414    #[inline(always)]
2415    fn deref(&self) -> &T {
2416        &self.inner().value
2417    }
2418}
2419
2420#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2421unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for Rc<T, A> {}
2422
2423//#[unstable(feature = "unique_rc_arc", issue = "112566")]
2424#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2425unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for UniqueRc<T, A> {}
2426
2427#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2428unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for Weak<T, A> {}
2429
2430#[unstable(feature = "deref_pure_trait", issue = "87121")]
2431unsafe impl<T: ?Sized, A: Allocator> DerefPure for Rc<T, A> {}
2432
2433//#[unstable(feature = "unique_rc_arc", issue = "112566")]
2434#[unstable(feature = "deref_pure_trait", issue = "87121")]
2435unsafe impl<T: ?Sized, A: Allocator> DerefPure for UniqueRc<T, A> {}
2436
2437#[unstable(feature = "legacy_receiver_trait", issue = "none")]
2438impl<T: ?Sized> LegacyReceiver for Rc<T> {}
2439
2440#[stable(feature = "rust1", since = "1.0.0")]
2441unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for Rc<T, A> {
2442    /// Drops the `Rc`.
2443    ///
2444    /// This will decrement the strong reference count. If the strong reference
2445    /// count reaches zero then the only other references (if any) are
2446    /// [`Weak`], so we `drop` the inner value.
2447    ///
2448    /// # Examples
2449    ///
2450    /// ```
2451    /// use std::rc::Rc;
2452    ///
2453    /// struct Foo;
2454    ///
2455    /// impl Drop for Foo {
2456    ///     fn drop(&mut self) {
2457    ///         println!("dropped!");
2458    ///     }
2459    /// }
2460    ///
2461    /// let foo  = Rc::new(Foo);
2462    /// let foo2 = Rc::clone(&foo);
2463    ///
2464    /// drop(foo);    // Doesn't print anything
2465    /// drop(foo2);   // Prints "dropped!"
2466    /// ```
2467    #[inline]
2468    fn drop(&mut self) {
2469        unsafe {
2470            self.inner().dec_strong();
2471            if self.inner().strong() == 0 {
2472                self.drop_slow();
2473            }
2474        }
2475    }
2476}
2477
2478#[stable(feature = "rust1", since = "1.0.0")]
2479impl<T: ?Sized, A: Allocator + Clone> Clone for Rc<T, A> {
2480    /// Makes a clone of the `Rc` pointer.
2481    ///
2482    /// This creates another pointer to the same allocation, increasing the
2483    /// strong reference count.
2484    ///
2485    /// # Examples
2486    ///
2487    /// ```
2488    /// use std::rc::Rc;
2489    ///
2490    /// let five = Rc::new(5);
2491    ///
2492    /// let _ = Rc::clone(&five);
2493    /// ```
2494    #[inline]
2495    fn clone(&self) -> Self {
2496        unsafe {
2497            self.inner().inc_strong();
2498            Self::from_inner_in(self.ptr, self.alloc.clone())
2499        }
2500    }
2501}
2502
2503#[unstable(feature = "ergonomic_clones", issue = "132290")]
2504impl<T: ?Sized, A: Allocator + Clone> UseCloned for Rc<T, A> {}
2505
2506#[cfg(not(no_global_oom_handling))]
2507#[stable(feature = "rust1", since = "1.0.0")]
2508impl<T: Default> Default for Rc<T> {
2509    /// Creates a new `Rc<T>`, with the `Default` value for `T`.
2510    ///
2511    /// # Examples
2512    ///
2513    /// ```
2514    /// use std::rc::Rc;
2515    ///
2516    /// let x: Rc<i32> = Default::default();
2517    /// assert_eq!(*x, 0);
2518    /// ```
2519    #[inline]
2520    fn default() -> Self {
2521        unsafe {
2522            Self::from_inner(
2523                Box::leak(Box::write(
2524                    Box::new_uninit(),
2525                    RcInner { strong: Cell::new(1), weak: Cell::new(1), value: T::default() },
2526                ))
2527                .into(),
2528            )
2529        }
2530    }
2531}
2532
2533#[cfg(not(no_global_oom_handling))]
2534#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
2535impl Default for Rc<str> {
2536    /// Creates an empty `str` inside an `Rc`.
2537    ///
2538    /// This may or may not share an allocation with other Rcs on the same thread.
2539    #[inline]
2540    fn default() -> Self {
2541        let rc = Rc::<[u8]>::default();
2542        // `[u8]` has the same layout as `str`.
2543        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const str) }
2544    }
2545}
2546
2547#[cfg(not(no_global_oom_handling))]
2548#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
2549impl<T> Default for Rc<[T]> {
2550    /// Creates an empty `[T]` inside an `Rc`.
2551    ///
2552    /// This may or may not share an allocation with other Rcs on the same thread.
2553    #[inline]
2554    fn default() -> Self {
2555        let arr: [T; 0] = [];
2556        Rc::from(arr)
2557    }
2558}
2559
2560#[cfg(not(no_global_oom_handling))]
2561#[stable(feature = "pin_default_impls", since = "1.91.0")]
2562impl<T> Default for Pin<Rc<T>>
2563where
2564    T: ?Sized,
2565    Rc<T>: Default,
2566{
2567    #[inline]
2568    fn default() -> Self {
2569        unsafe { Pin::new_unchecked(Rc::<T>::default()) }
2570    }
2571}
2572
2573#[stable(feature = "rust1", since = "1.0.0")]
2574trait RcEqIdent<T: ?Sized + PartialEq, A: Allocator> {
2575    fn eq(&self, other: &Rc<T, A>) -> bool;
2576    fn ne(&self, other: &Rc<T, A>) -> bool;
2577}
2578
2579#[stable(feature = "rust1", since = "1.0.0")]
2580impl<T: ?Sized + PartialEq, A: Allocator> RcEqIdent<T, A> for Rc<T, A> {
2581    #[inline]
2582    default fn eq(&self, other: &Rc<T, A>) -> bool {
2583        **self == **other
2584    }
2585
2586    #[inline]
2587    default fn ne(&self, other: &Rc<T, A>) -> bool {
2588        **self != **other
2589    }
2590}
2591
2592// Hack to allow specializing on `Eq` even though `Eq` has a method.
2593#[rustc_unsafe_specialization_marker]
2594pub(crate) trait MarkerEq: PartialEq<Self> {}
2595
2596impl<T: Eq> MarkerEq for T {}
2597
2598/// We're doing this specialization here, and not as a more general optimization on `&T`, because it
2599/// would otherwise add a cost to all equality checks on refs. We assume that `Rc`s are used to
2600/// store large values, that are slow to clone, but also heavy to check for equality, causing this
2601/// cost to pay off more easily. It's also more likely to have two `Rc` clones, that point to
2602/// the same value, than two `&T`s.
2603///
2604/// We can only do this when `T: Eq` as a `PartialEq` might be deliberately irreflexive.
2605#[stable(feature = "rust1", since = "1.0.0")]
2606impl<T: ?Sized + MarkerEq, A: Allocator> RcEqIdent<T, A> for Rc<T, A> {
2607    #[inline]
2608    fn eq(&self, other: &Rc<T, A>) -> bool {
2609        Rc::ptr_eq(self, other) || **self == **other
2610    }
2611
2612    #[inline]
2613    fn ne(&self, other: &Rc<T, A>) -> bool {
2614        !Rc::ptr_eq(self, other) && **self != **other
2615    }
2616}
2617
2618#[stable(feature = "rust1", since = "1.0.0")]
2619impl<T: ?Sized + PartialEq, A: Allocator> PartialEq for Rc<T, A> {
2620    /// Equality for two `Rc`s.
2621    ///
2622    /// Two `Rc`s are equal if their inner values are equal, even if they are
2623    /// stored in different allocation.
2624    ///
2625    /// If `T` also implements `Eq` (implying reflexivity of equality),
2626    /// two `Rc`s that point to the same allocation are
2627    /// always equal.
2628    ///
2629    /// # Examples
2630    ///
2631    /// ```
2632    /// use std::rc::Rc;
2633    ///
2634    /// let five = Rc::new(5);
2635    ///
2636    /// assert!(five == Rc::new(5));
2637    /// ```
2638    #[inline]
2639    fn eq(&self, other: &Rc<T, A>) -> bool {
2640        RcEqIdent::eq(self, other)
2641    }
2642
2643    /// Inequality for two `Rc`s.
2644    ///
2645    /// Two `Rc`s are not equal if their inner values are not equal.
2646    ///
2647    /// If `T` also implements `Eq` (implying reflexivity of equality),
2648    /// two `Rc`s that point to the same allocation are
2649    /// always equal.
2650    ///
2651    /// # Examples
2652    ///
2653    /// ```
2654    /// use std::rc::Rc;
2655    ///
2656    /// let five = Rc::new(5);
2657    ///
2658    /// assert!(five != Rc::new(6));
2659    /// ```
2660    #[inline]
2661    fn ne(&self, other: &Rc<T, A>) -> bool {
2662        RcEqIdent::ne(self, other)
2663    }
2664}
2665
2666#[stable(feature = "rust1", since = "1.0.0")]
2667impl<T: ?Sized + Eq, A: Allocator> Eq for Rc<T, A> {}
2668
2669#[stable(feature = "rust1", since = "1.0.0")]
2670impl<T: ?Sized + PartialOrd, A: Allocator> PartialOrd for Rc<T, A> {
2671    /// Partial comparison for two `Rc`s.
2672    ///
2673    /// The two are compared by calling `partial_cmp()` on their inner values.
2674    ///
2675    /// # Examples
2676    ///
2677    /// ```
2678    /// use std::rc::Rc;
2679    /// use std::cmp::Ordering;
2680    ///
2681    /// let five = Rc::new(5);
2682    ///
2683    /// assert_eq!(Some(Ordering::Less), five.partial_cmp(&Rc::new(6)));
2684    /// ```
2685    #[inline(always)]
2686    fn partial_cmp(&self, other: &Rc<T, A>) -> Option<Ordering> {
2687        (**self).partial_cmp(&**other)
2688    }
2689
2690    /// Less-than comparison for two `Rc`s.
2691    ///
2692    /// The two are compared by calling `<` on their inner values.
2693    ///
2694    /// # Examples
2695    ///
2696    /// ```
2697    /// use std::rc::Rc;
2698    ///
2699    /// let five = Rc::new(5);
2700    ///
2701    /// assert!(five < Rc::new(6));
2702    /// ```
2703    #[inline(always)]
2704    fn lt(&self, other: &Rc<T, A>) -> bool {
2705        **self < **other
2706    }
2707
2708    /// 'Less than or equal to' comparison for two `Rc`s.
2709    ///
2710    /// The two are compared by calling `<=` on their inner values.
2711    ///
2712    /// # Examples
2713    ///
2714    /// ```
2715    /// use std::rc::Rc;
2716    ///
2717    /// let five = Rc::new(5);
2718    ///
2719    /// assert!(five <= Rc::new(5));
2720    /// ```
2721    #[inline(always)]
2722    fn le(&self, other: &Rc<T, A>) -> bool {
2723        **self <= **other
2724    }
2725
2726    /// Greater-than comparison for two `Rc`s.
2727    ///
2728    /// The two are compared by calling `>` on their inner values.
2729    ///
2730    /// # Examples
2731    ///
2732    /// ```
2733    /// use std::rc::Rc;
2734    ///
2735    /// let five = Rc::new(5);
2736    ///
2737    /// assert!(five > Rc::new(4));
2738    /// ```
2739    #[inline(always)]
2740    fn gt(&self, other: &Rc<T, A>) -> bool {
2741        **self > **other
2742    }
2743
2744    /// 'Greater than or equal to' comparison for two `Rc`s.
2745    ///
2746    /// The two are compared by calling `>=` on their inner values.
2747    ///
2748    /// # Examples
2749    ///
2750    /// ```
2751    /// use std::rc::Rc;
2752    ///
2753    /// let five = Rc::new(5);
2754    ///
2755    /// assert!(five >= Rc::new(5));
2756    /// ```
2757    #[inline(always)]
2758    fn ge(&self, other: &Rc<T, A>) -> bool {
2759        **self >= **other
2760    }
2761}
2762
2763#[stable(feature = "rust1", since = "1.0.0")]
2764impl<T: ?Sized + Ord, A: Allocator> Ord for Rc<T, A> {
2765    /// Comparison for two `Rc`s.
2766    ///
2767    /// The two are compared by calling `cmp()` on their inner values.
2768    ///
2769    /// # Examples
2770    ///
2771    /// ```
2772    /// use std::rc::Rc;
2773    /// use std::cmp::Ordering;
2774    ///
2775    /// let five = Rc::new(5);
2776    ///
2777    /// assert_eq!(Ordering::Less, five.cmp(&Rc::new(6)));
2778    /// ```
2779    #[inline]
2780    fn cmp(&self, other: &Rc<T, A>) -> Ordering {
2781        (**self).cmp(&**other)
2782    }
2783}
2784
2785#[stable(feature = "rust1", since = "1.0.0")]
2786impl<T: ?Sized + Hash, A: Allocator> Hash for Rc<T, A> {
2787    fn hash<H: Hasher>(&self, state: &mut H) {
2788        (**self).hash(state);
2789    }
2790}
2791
2792#[stable(feature = "rust1", since = "1.0.0")]
2793impl<T: ?Sized + fmt::Display, A: Allocator> fmt::Display for Rc<T, A> {
2794    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2795        fmt::Display::fmt(&**self, f)
2796    }
2797}
2798
2799#[stable(feature = "rust1", since = "1.0.0")]
2800impl<T: ?Sized + fmt::Debug, A: Allocator> fmt::Debug for Rc<T, A> {
2801    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2802        fmt::Debug::fmt(&**self, f)
2803    }
2804}
2805
2806#[stable(feature = "rust1", since = "1.0.0")]
2807impl<T: ?Sized, A: Allocator> fmt::Pointer for Rc<T, A> {
2808    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2809        fmt::Pointer::fmt(&(&raw const **self), f)
2810    }
2811}
2812
2813#[cfg(not(no_global_oom_handling))]
2814#[stable(feature = "from_for_ptrs", since = "1.6.0")]
2815impl<T> From<T> for Rc<T> {
2816    /// Converts a generic type `T` into an `Rc<T>`
2817    ///
2818    /// The conversion allocates on the heap and moves `t`
2819    /// from the stack into it.
2820    ///
2821    /// # Example
2822    /// ```rust
2823    /// # use std::rc::Rc;
2824    /// let x = 5;
2825    /// let rc = Rc::new(5);
2826    ///
2827    /// assert_eq!(Rc::from(x), rc);
2828    /// ```
2829    fn from(t: T) -> Self {
2830        Rc::new(t)
2831    }
2832}
2833
2834#[cfg(not(no_global_oom_handling))]
2835#[stable(feature = "shared_from_array", since = "1.74.0")]
2836impl<T, const N: usize> From<[T; N]> for Rc<[T]> {
2837    /// Converts a [`[T; N]`](prim@array) into an `Rc<[T]>`.
2838    ///
2839    /// The conversion moves the array into a newly allocated `Rc`.
2840    ///
2841    /// # Example
2842    ///
2843    /// ```
2844    /// # use std::rc::Rc;
2845    /// let original: [i32; 3] = [1, 2, 3];
2846    /// let shared: Rc<[i32]> = Rc::from(original);
2847    /// assert_eq!(&[1, 2, 3], &shared[..]);
2848    /// ```
2849    #[inline]
2850    fn from(v: [T; N]) -> Rc<[T]> {
2851        Rc::<[T; N]>::from(v)
2852    }
2853}
2854
2855#[cfg(not(no_global_oom_handling))]
2856#[stable(feature = "shared_from_slice", since = "1.21.0")]
2857impl<T: Clone> From<&[T]> for Rc<[T]> {
2858    /// Allocates a reference-counted slice and fills it by cloning `v`'s items.
2859    ///
2860    /// # Example
2861    ///
2862    /// ```
2863    /// # use std::rc::Rc;
2864    /// let original: &[i32] = &[1, 2, 3];
2865    /// let shared: Rc<[i32]> = Rc::from(original);
2866    /// assert_eq!(&[1, 2, 3], &shared[..]);
2867    /// ```
2868    #[inline]
2869    fn from(v: &[T]) -> Rc<[T]> {
2870        <Self as RcFromSlice<T>>::from_slice(v)
2871    }
2872}
2873
2874#[cfg(not(no_global_oom_handling))]
2875#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
2876impl<T: Clone> From<&mut [T]> for Rc<[T]> {
2877    /// Allocates a reference-counted slice and fills it by cloning `v`'s items.
2878    ///
2879    /// # Example
2880    ///
2881    /// ```
2882    /// # use std::rc::Rc;
2883    /// let mut original = [1, 2, 3];
2884    /// let original: &mut [i32] = &mut original;
2885    /// let shared: Rc<[i32]> = Rc::from(original);
2886    /// assert_eq!(&[1, 2, 3], &shared[..]);
2887    /// ```
2888    #[inline]
2889    fn from(v: &mut [T]) -> Rc<[T]> {
2890        Rc::from(&*v)
2891    }
2892}
2893
2894#[cfg(not(no_global_oom_handling))]
2895#[stable(feature = "shared_from_slice", since = "1.21.0")]
2896impl From<&str> for Rc<str> {
2897    /// Allocates a reference-counted string slice and copies `v` into it.
2898    ///
2899    /// # Example
2900    ///
2901    /// ```
2902    /// # use std::rc::Rc;
2903    /// let shared: Rc<str> = Rc::from("statue");
2904    /// assert_eq!("statue", &shared[..]);
2905    /// ```
2906    #[inline]
2907    fn from(v: &str) -> Rc<str> {
2908        let rc = Rc::<[u8]>::from(v.as_bytes());
2909        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const str) }
2910    }
2911}
2912
2913#[cfg(not(no_global_oom_handling))]
2914#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
2915impl From<&mut str> for Rc<str> {
2916    /// Allocates a reference-counted string slice and copies `v` into it.
2917    ///
2918    /// # Example
2919    ///
2920    /// ```
2921    /// # use std::rc::Rc;
2922    /// let mut original = String::from("statue");
2923    /// let original: &mut str = &mut original;
2924    /// let shared: Rc<str> = Rc::from(original);
2925    /// assert_eq!("statue", &shared[..]);
2926    /// ```
2927    #[inline]
2928    fn from(v: &mut str) -> Rc<str> {
2929        Rc::from(&*v)
2930    }
2931}
2932
2933#[cfg(not(no_global_oom_handling))]
2934#[stable(feature = "shared_from_slice", since = "1.21.0")]
2935impl From<String> for Rc<str> {
2936    /// Allocates a reference-counted string slice and copies `v` into it.
2937    ///
2938    /// # Example
2939    ///
2940    /// ```
2941    /// # use std::rc::Rc;
2942    /// let original: String = "statue".to_owned();
2943    /// let shared: Rc<str> = Rc::from(original);
2944    /// assert_eq!("statue", &shared[..]);
2945    /// ```
2946    #[inline]
2947    fn from(v: String) -> Rc<str> {
2948        Rc::from(&v[..])
2949    }
2950}
2951
2952#[cfg(not(no_global_oom_handling))]
2953#[stable(feature = "shared_from_slice", since = "1.21.0")]
2954impl<T: ?Sized, A: Allocator> From<Box<T, A>> for Rc<T, A> {
2955    /// Move a boxed object to a new, reference counted, allocation.
2956    ///
2957    /// # Example
2958    ///
2959    /// ```
2960    /// # use std::rc::Rc;
2961    /// let original: Box<i32> = Box::new(1);
2962    /// let shared: Rc<i32> = Rc::from(original);
2963    /// assert_eq!(1, *shared);
2964    /// ```
2965    #[inline]
2966    fn from(v: Box<T, A>) -> Rc<T, A> {
2967        Rc::from_box_in(v)
2968    }
2969}
2970
2971#[cfg(not(no_global_oom_handling))]
2972#[stable(feature = "shared_from_slice", since = "1.21.0")]
2973impl<T, A: Allocator> From<Vec<T, A>> for Rc<[T], A> {
2974    /// Allocates a reference-counted slice and moves `v`'s items into it.
2975    ///
2976    /// # Example
2977    ///
2978    /// ```
2979    /// # use std::rc::Rc;
2980    /// let unique: Vec<i32> = vec![1, 2, 3];
2981    /// let shared: Rc<[i32]> = Rc::from(unique);
2982    /// assert_eq!(&[1, 2, 3], &shared[..]);
2983    /// ```
2984    #[inline]
2985    fn from(v: Vec<T, A>) -> Rc<[T], A> {
2986        unsafe {
2987            let (vec_ptr, len, cap, alloc) = v.into_raw_parts_with_alloc();
2988
2989            let rc_ptr = Self::allocate_for_slice_in(len, &alloc);
2990            ptr::copy_nonoverlapping(vec_ptr, (&raw mut (*rc_ptr).value) as *mut T, len);
2991
2992            // Create a `Vec<T, &A>` with length 0, to deallocate the buffer
2993            // without dropping its contents or the allocator
2994            let _ = Vec::from_raw_parts_in(vec_ptr, 0, cap, &alloc);
2995
2996            Self::from_ptr_in(rc_ptr, alloc)
2997        }
2998    }
2999}
3000
3001#[stable(feature = "shared_from_cow", since = "1.45.0")]
3002impl<'a, B> From<Cow<'a, B>> for Rc<B>
3003where
3004    B: ToOwned + ?Sized,
3005    Rc<B>: From<&'a B> + From<B::Owned>,
3006{
3007    /// Creates a reference-counted pointer from a clone-on-write pointer by
3008    /// copying its content.
3009    ///
3010    /// # Example
3011    ///
3012    /// ```rust
3013    /// # use std::rc::Rc;
3014    /// # use std::borrow::Cow;
3015    /// let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
3016    /// let shared: Rc<str> = Rc::from(cow);
3017    /// assert_eq!("eggplant", &shared[..]);
3018    /// ```
3019    #[inline]
3020    fn from(cow: Cow<'a, B>) -> Rc<B> {
3021        match cow {
3022            Cow::Borrowed(s) => Rc::from(s),
3023            Cow::Owned(s) => Rc::from(s),
3024        }
3025    }
3026}
3027
3028#[stable(feature = "shared_from_str", since = "1.62.0")]
3029impl From<Rc<str>> for Rc<[u8]> {
3030    /// Converts a reference-counted string slice into a byte slice.
3031    ///
3032    /// # Example
3033    ///
3034    /// ```
3035    /// # use std::rc::Rc;
3036    /// let string: Rc<str> = Rc::from("eggplant");
3037    /// let bytes: Rc<[u8]> = Rc::from(string);
3038    /// assert_eq!("eggplant".as_bytes(), bytes.as_ref());
3039    /// ```
3040    #[inline]
3041    fn from(rc: Rc<str>) -> Self {
3042        // SAFETY: `str` has the same layout as `[u8]`.
3043        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const [u8]) }
3044    }
3045}
3046
3047#[stable(feature = "boxed_slice_try_from", since = "1.43.0")]
3048impl<T, A: Allocator, const N: usize> TryFrom<Rc<[T], A>> for Rc<[T; N], A> {
3049    type Error = Rc<[T], A>;
3050
3051    fn try_from(boxed_slice: Rc<[T], A>) -> Result<Self, Self::Error> {
3052        if boxed_slice.len() == N {
3053            let (ptr, alloc) = Rc::into_inner_with_allocator(boxed_slice);
3054            Ok(unsafe { Rc::from_inner_in(ptr.cast(), alloc) })
3055        } else {
3056            Err(boxed_slice)
3057        }
3058    }
3059}
3060
3061#[cfg(not(no_global_oom_handling))]
3062#[stable(feature = "shared_from_iter", since = "1.37.0")]
3063impl<T> FromIterator<T> for Rc<[T]> {
3064    /// Takes each element in the `Iterator` and collects it into an `Rc<[T]>`.
3065    ///
3066    /// # Performance characteristics
3067    ///
3068    /// ## The general case
3069    ///
3070    /// In the general case, collecting into `Rc<[T]>` is done by first
3071    /// collecting into a `Vec<T>`. That is, when writing the following:
3072    ///
3073    /// ```rust
3074    /// # use std::rc::Rc;
3075    /// let evens: Rc<[u8]> = (0..10).filter(|&x| x % 2 == 0).collect();
3076    /// # assert_eq!(&*evens, &[0, 2, 4, 6, 8]);
3077    /// ```
3078    ///
3079    /// this behaves as if we wrote:
3080    ///
3081    /// ```rust
3082    /// # use std::rc::Rc;
3083    /// let evens: Rc<[u8]> = (0..10).filter(|&x| x % 2 == 0)
3084    ///     .collect::<Vec<_>>() // The first set of allocations happens here.
3085    ///     .into(); // A second allocation for `Rc<[T]>` happens here.
3086    /// # assert_eq!(&*evens, &[0, 2, 4, 6, 8]);
3087    /// ```
3088    ///
3089    /// This will allocate as many times as needed for constructing the `Vec<T>`
3090    /// and then it will allocate once for turning the `Vec<T>` into the `Rc<[T]>`.
3091    ///
3092    /// ## Iterators of known length
3093    ///
3094    /// When your `Iterator` implements `TrustedLen` and is of an exact size,
3095    /// a single allocation will be made for the `Rc<[T]>`. For example:
3096    ///
3097    /// ```rust
3098    /// # use std::rc::Rc;
3099    /// let evens: Rc<[u8]> = (0..10).collect(); // Just a single allocation happens here.
3100    /// # assert_eq!(&*evens, &*(0..10).collect::<Vec<_>>());
3101    /// ```
3102    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
3103        ToRcSlice::to_rc_slice(iter.into_iter())
3104    }
3105}
3106
3107/// Specialization trait used for collecting into `Rc<[T]>`.
3108#[cfg(not(no_global_oom_handling))]
3109trait ToRcSlice<T>: Iterator<Item = T> + Sized {
3110    fn to_rc_slice(self) -> Rc<[T]>;
3111}
3112
3113#[cfg(not(no_global_oom_handling))]
3114impl<T, I: Iterator<Item = T>> ToRcSlice<T> for I {
3115    default fn to_rc_slice(self) -> Rc<[T]> {
3116        self.collect::<Vec<T>>().into()
3117    }
3118}
3119
3120#[cfg(not(no_global_oom_handling))]
3121impl<T, I: iter::TrustedLen<Item = T>> ToRcSlice<T> for I {
3122    fn to_rc_slice(self) -> Rc<[T]> {
3123        // This is the case for a `TrustedLen` iterator.
3124        let (low, high) = self.size_hint();
3125        if let Some(high) = high {
3126            debug_assert_eq!(
3127                low,
3128                high,
3129                "TrustedLen iterator's size hint is not exact: {:?}",
3130                (low, high)
3131            );
3132
3133            unsafe {
3134                // SAFETY: We need to ensure that the iterator has an exact length and we have.
3135                Rc::from_iter_exact(self, low)
3136            }
3137        } else {
3138            // TrustedLen contract guarantees that `upper_bound == None` implies an iterator
3139            // length exceeding `usize::MAX`.
3140            // The default implementation would collect into a vec which would panic.
3141            // Thus we panic here immediately without invoking `Vec` code.
3142            panic!("capacity overflow");
3143        }
3144    }
3145}
3146
3147/// `Weak` is a version of [`Rc`] that holds a non-owning reference to the
3148/// managed allocation.
3149///
3150/// The allocation is accessed by calling [`upgrade`] on the `Weak`
3151/// pointer, which returns an <code>[Option]<[Rc]\<T>></code>.
3152///
3153/// Since a `Weak` reference does not count towards ownership, it will not
3154/// prevent the value stored in the allocation from being dropped, and `Weak` itself makes no
3155/// guarantees about the value still being present. Thus it may return [`None`]
3156/// when [`upgrade`]d. Note however that a `Weak` reference *does* prevent the allocation
3157/// itself (the backing store) from being deallocated.
3158///
3159/// A `Weak` pointer is useful for keeping a temporary reference to the allocation
3160/// managed by [`Rc`] without preventing its inner value from being dropped. It is also used to
3161/// prevent circular references between [`Rc`] pointers, since mutual owning references
3162/// would never allow either [`Rc`] to be dropped. For example, a tree could
3163/// have strong [`Rc`] pointers from parent nodes to children, and `Weak`
3164/// pointers from children back to their parents.
3165///
3166/// The typical way to obtain a `Weak` pointer is to call [`Rc::downgrade`].
3167///
3168/// [`upgrade`]: Weak::upgrade
3169#[stable(feature = "rc_weak", since = "1.4.0")]
3170#[rustc_diagnostic_item = "RcWeak"]
3171pub struct Weak<
3172    T: ?Sized,
3173    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
3174> {
3175    // This is a `NonNull` to allow optimizing the size of this type in enums,
3176    // but it is not necessarily a valid pointer.
3177    // `Weak::new` sets this to `usize::MAX` so that it doesn’t need
3178    // to allocate space on the heap. That's not a value a real pointer
3179    // will ever have because RcInner has alignment at least 2.
3180    ptr: NonNull<RcInner<T>>,
3181    alloc: A,
3182}
3183
3184#[stable(feature = "rc_weak", since = "1.4.0")]
3185impl<T: ?Sized, A: Allocator> !Send for Weak<T, A> {}
3186#[stable(feature = "rc_weak", since = "1.4.0")]
3187impl<T: ?Sized, A: Allocator> !Sync for Weak<T, A> {}
3188
3189#[unstable(feature = "coerce_unsized", issue = "18598")]
3190impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<Weak<U, A>> for Weak<T, A> {}
3191
3192#[unstable(feature = "dispatch_from_dyn", issue = "none")]
3193impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<Weak<U>> for Weak<T> {}
3194
3195// SAFETY: `Weak::clone` doesn't access any `Cell`s which could contain the `Weak` being cloned.
3196#[unstable(feature = "cell_get_cloned", issue = "145329")]
3197unsafe impl<T: ?Sized> CloneFromCell for Weak<T> {}
3198
3199impl<T> Weak<T> {
3200    /// Constructs a new `Weak<T>`, without allocating any memory.
3201    /// Calling [`upgrade`] on the return value always gives [`None`].
3202    ///
3203    /// [`upgrade`]: Weak::upgrade
3204    ///
3205    /// # Examples
3206    ///
3207    /// ```
3208    /// use std::rc::Weak;
3209    ///
3210    /// let empty: Weak<i64> = Weak::new();
3211    /// assert!(empty.upgrade().is_none());
3212    /// ```
3213    #[inline]
3214    #[stable(feature = "downgraded_weak", since = "1.10.0")]
3215    #[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
3216    #[must_use]
3217    pub const fn new() -> Weak<T> {
3218        Weak { ptr: NonNull::without_provenance(NonZeroUsize::MAX), alloc: Global }
3219    }
3220}
3221
3222impl<T, A: Allocator> Weak<T, A> {
3223    /// Constructs a new `Weak<T>`, without allocating any memory, technically in the provided
3224    /// allocator.
3225    /// Calling [`upgrade`] on the return value always gives [`None`].
3226    ///
3227    /// [`upgrade`]: Weak::upgrade
3228    ///
3229    /// # Examples
3230    ///
3231    /// ```
3232    /// use std::rc::Weak;
3233    ///
3234    /// let empty: Weak<i64> = Weak::new();
3235    /// assert!(empty.upgrade().is_none());
3236    /// ```
3237    #[inline]
3238    #[unstable(feature = "allocator_api", issue = "32838")]
3239    pub fn new_in(alloc: A) -> Weak<T, A> {
3240        Weak { ptr: NonNull::without_provenance(NonZeroUsize::MAX), alloc }
3241    }
3242}
3243
3244pub(crate) fn is_dangling<T: ?Sized>(ptr: *const T) -> bool {
3245    (ptr.cast::<()>()).addr() == usize::MAX
3246}
3247
3248/// Helper type to allow accessing the reference counts without
3249/// making any assertions about the data field.
3250struct WeakInner<'a> {
3251    weak: &'a Cell<usize>,
3252    strong: &'a Cell<usize>,
3253}
3254
3255impl<T: ?Sized> Weak<T> {
3256    /// Converts a raw pointer previously created by [`into_raw`] back into `Weak<T>`.
3257    ///
3258    /// This can be used to safely get a strong reference (by calling [`upgrade`]
3259    /// later) or to deallocate the weak count by dropping the `Weak<T>`.
3260    ///
3261    /// It takes ownership of one weak reference (with the exception of pointers created by [`new`],
3262    /// as these don't own anything; the method still works on them).
3263    ///
3264    /// # Safety
3265    ///
3266    /// The pointer must have originated from the [`into_raw`] and must still own its potential
3267    /// weak reference, and `ptr` must point to a block of memory allocated by the global allocator.
3268    ///
3269    /// It is allowed for the strong count to be 0 at the time of calling this. Nevertheless, this
3270    /// takes ownership of one weak reference currently represented as a raw pointer (the weak
3271    /// count is not modified by this operation) and therefore it must be paired with a previous
3272    /// call to [`into_raw`].
3273    ///
3274    /// # Examples
3275    ///
3276    /// ```
3277    /// use std::rc::{Rc, Weak};
3278    ///
3279    /// let strong = Rc::new("hello".to_owned());
3280    ///
3281    /// let raw_1 = Rc::downgrade(&strong).into_raw();
3282    /// let raw_2 = Rc::downgrade(&strong).into_raw();
3283    ///
3284    /// assert_eq!(2, Rc::weak_count(&strong));
3285    ///
3286    /// assert_eq!("hello", &*unsafe { Weak::from_raw(raw_1) }.upgrade().unwrap());
3287    /// assert_eq!(1, Rc::weak_count(&strong));
3288    ///
3289    /// drop(strong);
3290    ///
3291    /// // Decrement the last weak count.
3292    /// assert!(unsafe { Weak::from_raw(raw_2) }.upgrade().is_none());
3293    /// ```
3294    ///
3295    /// [`into_raw`]: Weak::into_raw
3296    /// [`upgrade`]: Weak::upgrade
3297    /// [`new`]: Weak::new
3298    #[inline]
3299    #[stable(feature = "weak_into_raw", since = "1.45.0")]
3300    pub unsafe fn from_raw(ptr: *const T) -> Self {
3301        unsafe { Self::from_raw_in(ptr, Global) }
3302    }
3303
3304    /// Consumes the `Weak<T>` and turns it into a raw pointer.
3305    ///
3306    /// This converts the weak pointer into a raw pointer, while still preserving the ownership of
3307    /// one weak reference (the weak count is not modified by this operation). It can be turned
3308    /// back into the `Weak<T>` with [`from_raw`].
3309    ///
3310    /// The same restrictions of accessing the target of the pointer as with
3311    /// [`as_ptr`] apply.
3312    ///
3313    /// # Examples
3314    ///
3315    /// ```
3316    /// use std::rc::{Rc, Weak};
3317    ///
3318    /// let strong = Rc::new("hello".to_owned());
3319    /// let weak = Rc::downgrade(&strong);
3320    /// let raw = weak.into_raw();
3321    ///
3322    /// assert_eq!(1, Rc::weak_count(&strong));
3323    /// assert_eq!("hello", unsafe { &*raw });
3324    ///
3325    /// drop(unsafe { Weak::from_raw(raw) });
3326    /// assert_eq!(0, Rc::weak_count(&strong));
3327    /// ```
3328    ///
3329    /// [`from_raw`]: Weak::from_raw
3330    /// [`as_ptr`]: Weak::as_ptr
3331    #[must_use = "losing the pointer will leak memory"]
3332    #[stable(feature = "weak_into_raw", since = "1.45.0")]
3333    pub fn into_raw(self) -> *const T {
3334        mem::ManuallyDrop::new(self).as_ptr()
3335    }
3336}
3337
3338impl<T: ?Sized, A: Allocator> Weak<T, A> {
3339    /// Returns a reference to the underlying allocator.
3340    #[inline]
3341    #[unstable(feature = "allocator_api", issue = "32838")]
3342    pub fn allocator(&self) -> &A {
3343        &self.alloc
3344    }
3345
3346    /// Returns a raw pointer to the object `T` pointed to by this `Weak<T>`.
3347    ///
3348    /// The pointer is valid only if there are some strong references. The pointer may be dangling,
3349    /// unaligned or even [`null`] otherwise.
3350    ///
3351    /// # Examples
3352    ///
3353    /// ```
3354    /// use std::rc::Rc;
3355    /// use std::ptr;
3356    ///
3357    /// let strong = Rc::new("hello".to_owned());
3358    /// let weak = Rc::downgrade(&strong);
3359    /// // Both point to the same object
3360    /// assert!(ptr::eq(&*strong, weak.as_ptr()));
3361    /// // The strong here keeps it alive, so we can still access the object.
3362    /// assert_eq!("hello", unsafe { &*weak.as_ptr() });
3363    ///
3364    /// drop(strong);
3365    /// // But not any more. We can do weak.as_ptr(), but accessing the pointer would lead to
3366    /// // undefined behavior.
3367    /// // assert_eq!("hello", unsafe { &*weak.as_ptr() });
3368    /// ```
3369    ///
3370    /// [`null`]: ptr::null
3371    #[must_use]
3372    #[stable(feature = "rc_as_ptr", since = "1.45.0")]
3373    pub fn as_ptr(&self) -> *const T {
3374        let ptr: *mut RcInner<T> = NonNull::as_ptr(self.ptr);
3375
3376        if is_dangling(ptr) {
3377            // If the pointer is dangling, we return the sentinel directly. This cannot be
3378            // a valid payload address, as the payload is at least as aligned as RcInner (usize).
3379            ptr as *const T
3380        } else {
3381            // SAFETY: if is_dangling returns false, then the pointer is dereferenceable.
3382            // The payload may be dropped at this point, and we have to maintain provenance,
3383            // so use raw pointer manipulation.
3384            unsafe { &raw mut (*ptr).value }
3385        }
3386    }
3387
3388    /// Consumes the `Weak<T>`, returning the wrapped pointer and allocator.
3389    ///
3390    /// This converts the weak pointer into a raw pointer, while still preserving the ownership of
3391    /// one weak reference (the weak count is not modified by this operation). It can be turned
3392    /// back into the `Weak<T>` with [`from_raw_in`].
3393    ///
3394    /// The same restrictions of accessing the target of the pointer as with
3395    /// [`as_ptr`] apply.
3396    ///
3397    /// # Examples
3398    ///
3399    /// ```
3400    /// #![feature(allocator_api)]
3401    /// use std::rc::{Rc, Weak};
3402    /// use std::alloc::System;
3403    ///
3404    /// let strong = Rc::new_in("hello".to_owned(), System);
3405    /// let weak = Rc::downgrade(&strong);
3406    /// let (raw, alloc) = weak.into_raw_with_allocator();
3407    ///
3408    /// assert_eq!(1, Rc::weak_count(&strong));
3409    /// assert_eq!("hello", unsafe { &*raw });
3410    ///
3411    /// drop(unsafe { Weak::from_raw_in(raw, alloc) });
3412    /// assert_eq!(0, Rc::weak_count(&strong));
3413    /// ```
3414    ///
3415    /// [`from_raw_in`]: Weak::from_raw_in
3416    /// [`as_ptr`]: Weak::as_ptr
3417    #[must_use = "losing the pointer will leak memory"]
3418    #[inline]
3419    #[unstable(feature = "allocator_api", issue = "32838")]
3420    pub fn into_raw_with_allocator(self) -> (*const T, A) {
3421        let this = mem::ManuallyDrop::new(self);
3422        let result = this.as_ptr();
3423        // Safety: `this` is ManuallyDrop so the allocator will not be double-dropped
3424        let alloc = unsafe { ptr::read(&this.alloc) };
3425        (result, alloc)
3426    }
3427
3428    /// Converts a raw pointer previously created by [`into_raw`] back into `Weak<T>`.
3429    ///
3430    /// This can be used to safely get a strong reference (by calling [`upgrade`]
3431    /// later) or to deallocate the weak count by dropping the `Weak<T>`.
3432    ///
3433    /// It takes ownership of one weak reference (with the exception of pointers created by [`new`],
3434    /// as these don't own anything; the method still works on them).
3435    ///
3436    /// # Safety
3437    ///
3438    /// The pointer must have originated from the [`into_raw`] and must still own its potential
3439    /// weak reference, and `ptr` must point to a block of memory allocated by `alloc`.
3440    ///
3441    /// It is allowed for the strong count to be 0 at the time of calling this. Nevertheless, this
3442    /// takes ownership of one weak reference currently represented as a raw pointer (the weak
3443    /// count is not modified by this operation) and therefore it must be paired with a previous
3444    /// call to [`into_raw`].
3445    ///
3446    /// # Examples
3447    ///
3448    /// ```
3449    /// use std::rc::{Rc, Weak};
3450    ///
3451    /// let strong = Rc::new("hello".to_owned());
3452    ///
3453    /// let raw_1 = Rc::downgrade(&strong).into_raw();
3454    /// let raw_2 = Rc::downgrade(&strong).into_raw();
3455    ///
3456    /// assert_eq!(2, Rc::weak_count(&strong));
3457    ///
3458    /// assert_eq!("hello", &*unsafe { Weak::from_raw(raw_1) }.upgrade().unwrap());
3459    /// assert_eq!(1, Rc::weak_count(&strong));
3460    ///
3461    /// drop(strong);
3462    ///
3463    /// // Decrement the last weak count.
3464    /// assert!(unsafe { Weak::from_raw(raw_2) }.upgrade().is_none());
3465    /// ```
3466    ///
3467    /// [`into_raw`]: Weak::into_raw
3468    /// [`upgrade`]: Weak::upgrade
3469    /// [`new`]: Weak::new
3470    #[inline]
3471    #[unstable(feature = "allocator_api", issue = "32838")]
3472    pub unsafe fn from_raw_in(ptr: *const T, alloc: A) -> Self {
3473        // See Weak::as_ptr for context on how the input pointer is derived.
3474
3475        let ptr = if is_dangling(ptr) {
3476            // This is a dangling Weak.
3477            ptr as *mut RcInner<T>
3478        } else {
3479            // Otherwise, we're guaranteed the pointer came from a nondangling Weak.
3480            // SAFETY: data_offset is safe to call, as ptr references a real (potentially dropped) T.
3481            let offset = unsafe { data_offset(ptr) };
3482            // Thus, we reverse the offset to get the whole RcInner.
3483            // SAFETY: the pointer originated from a Weak, so this offset is safe.
3484            unsafe { ptr.byte_sub(offset) as *mut RcInner<T> }
3485        };
3486
3487        // SAFETY: we now have recovered the original Weak pointer, so can create the Weak.
3488        Weak { ptr: unsafe { NonNull::new_unchecked(ptr) }, alloc }
3489    }
3490
3491    /// Attempts to upgrade the `Weak` pointer to an [`Rc`], delaying
3492    /// dropping of the inner value if successful.
3493    ///
3494    /// Returns [`None`] if the inner value has since been dropped.
3495    ///
3496    /// # Examples
3497    ///
3498    /// ```
3499    /// use std::rc::Rc;
3500    ///
3501    /// let five = Rc::new(5);
3502    ///
3503    /// let weak_five = Rc::downgrade(&five);
3504    ///
3505    /// let strong_five: Option<Rc<_>> = weak_five.upgrade();
3506    /// assert!(strong_five.is_some());
3507    ///
3508    /// // Destroy all strong pointers.
3509    /// drop(strong_five);
3510    /// drop(five);
3511    ///
3512    /// assert!(weak_five.upgrade().is_none());
3513    /// ```
3514    #[must_use = "this returns a new `Rc`, \
3515                  without modifying the original weak pointer"]
3516    #[stable(feature = "rc_weak", since = "1.4.0")]
3517    pub fn upgrade(&self) -> Option<Rc<T, A>>
3518    where
3519        A: Clone,
3520    {
3521        let inner = self.inner()?;
3522
3523        if inner.strong() == 0 {
3524            None
3525        } else {
3526            unsafe {
3527                inner.inc_strong();
3528                Some(Rc::from_inner_in(self.ptr, self.alloc.clone()))
3529            }
3530        }
3531    }
3532
3533    /// Gets the number of strong (`Rc`) pointers pointing to this allocation.
3534    ///
3535    /// If `self` was created using [`Weak::new`], this will return 0.
3536    #[must_use]
3537    #[stable(feature = "weak_counts", since = "1.41.0")]
3538    pub fn strong_count(&self) -> usize {
3539        if let Some(inner) = self.inner() { inner.strong() } else { 0 }
3540    }
3541
3542    /// Gets the number of `Weak` pointers pointing to this allocation.
3543    ///
3544    /// If no strong pointers remain, this will return zero.
3545    #[must_use]
3546    #[stable(feature = "weak_counts", since = "1.41.0")]
3547    pub fn weak_count(&self) -> usize {
3548        if let Some(inner) = self.inner() {
3549            if inner.strong() > 0 {
3550                inner.weak() - 1 // subtract the implicit weak ptr
3551            } else {
3552                0
3553            }
3554        } else {
3555            0
3556        }
3557    }
3558
3559    /// Returns `None` when the pointer is dangling and there is no allocated `RcInner`,
3560    /// (i.e., when this `Weak` was created by `Weak::new`).
3561    #[inline]
3562    fn inner(&self) -> Option<WeakInner<'_>> {
3563        if is_dangling(self.ptr.as_ptr()) {
3564            None
3565        } else {
3566            // We are careful to *not* create a reference covering the "data" field, as
3567            // the field may be mutated concurrently (for example, if the last `Rc`
3568            // is dropped, the data field will be dropped in-place).
3569            Some(unsafe {
3570                let ptr = self.ptr.as_ptr();
3571                WeakInner { strong: &(*ptr).strong, weak: &(*ptr).weak }
3572            })
3573        }
3574    }
3575
3576    /// Returns `true` if the two `Weak`s point to the same allocation similar to [`ptr::eq`], or if
3577    /// both don't point to any allocation (because they were created with `Weak::new()`). However,
3578    /// this function ignores the metadata of  `dyn Trait` pointers.
3579    ///
3580    /// # Notes
3581    ///
3582    /// Since this compares pointers it means that `Weak::new()` will equal each
3583    /// other, even though they don't point to any allocation.
3584    ///
3585    /// # Examples
3586    ///
3587    /// ```
3588    /// use std::rc::Rc;
3589    ///
3590    /// let first_rc = Rc::new(5);
3591    /// let first = Rc::downgrade(&first_rc);
3592    /// let second = Rc::downgrade(&first_rc);
3593    ///
3594    /// assert!(first.ptr_eq(&second));
3595    ///
3596    /// let third_rc = Rc::new(5);
3597    /// let third = Rc::downgrade(&third_rc);
3598    ///
3599    /// assert!(!first.ptr_eq(&third));
3600    /// ```
3601    ///
3602    /// Comparing `Weak::new`.
3603    ///
3604    /// ```
3605    /// use std::rc::{Rc, Weak};
3606    ///
3607    /// let first = Weak::new();
3608    /// let second = Weak::new();
3609    /// assert!(first.ptr_eq(&second));
3610    ///
3611    /// let third_rc = Rc::new(());
3612    /// let third = Rc::downgrade(&third_rc);
3613    /// assert!(!first.ptr_eq(&third));
3614    /// ```
3615    #[inline]
3616    #[must_use]
3617    #[stable(feature = "weak_ptr_eq", since = "1.39.0")]
3618    pub fn ptr_eq(&self, other: &Self) -> bool {
3619        ptr::addr_eq(self.ptr.as_ptr(), other.ptr.as_ptr())
3620    }
3621}
3622
3623#[stable(feature = "rc_weak", since = "1.4.0")]
3624unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for Weak<T, A> {
3625    /// Drops the `Weak` pointer.
3626    ///
3627    /// # Examples
3628    ///
3629    /// ```
3630    /// use std::rc::{Rc, Weak};
3631    ///
3632    /// struct Foo;
3633    ///
3634    /// impl Drop for Foo {
3635    ///     fn drop(&mut self) {
3636    ///         println!("dropped!");
3637    ///     }
3638    /// }
3639    ///
3640    /// let foo = Rc::new(Foo);
3641    /// let weak_foo = Rc::downgrade(&foo);
3642    /// let other_weak_foo = Weak::clone(&weak_foo);
3643    ///
3644    /// drop(weak_foo);   // Doesn't print anything
3645    /// drop(foo);        // Prints "dropped!"
3646    ///
3647    /// assert!(other_weak_foo.upgrade().is_none());
3648    /// ```
3649    fn drop(&mut self) {
3650        let inner = if let Some(inner) = self.inner() { inner } else { return };
3651
3652        inner.dec_weak();
3653        // the weak count starts at 1, and will only go to zero if all
3654        // the strong pointers have disappeared.
3655        if inner.weak() == 0 {
3656            unsafe {
3657                self.alloc.deallocate(self.ptr.cast(), Layout::for_value_raw(self.ptr.as_ptr()));
3658            }
3659        }
3660    }
3661}
3662
3663#[stable(feature = "rc_weak", since = "1.4.0")]
3664impl<T: ?Sized, A: Allocator + Clone> Clone for Weak<T, A> {
3665    /// Makes a clone of the `Weak` pointer that points to the same allocation.
3666    ///
3667    /// # Examples
3668    ///
3669    /// ```
3670    /// use std::rc::{Rc, Weak};
3671    ///
3672    /// let weak_five = Rc::downgrade(&Rc::new(5));
3673    ///
3674    /// let _ = Weak::clone(&weak_five);
3675    /// ```
3676    #[inline]
3677    fn clone(&self) -> Weak<T, A> {
3678        if let Some(inner) = self.inner() {
3679            inner.inc_weak()
3680        }
3681        Weak { ptr: self.ptr, alloc: self.alloc.clone() }
3682    }
3683}
3684
3685#[unstable(feature = "ergonomic_clones", issue = "132290")]
3686impl<T: ?Sized, A: Allocator + Clone> UseCloned for Weak<T, A> {}
3687
3688#[stable(feature = "rc_weak", since = "1.4.0")]
3689impl<T: ?Sized, A: Allocator> fmt::Debug for Weak<T, A> {
3690    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3691        write!(f, "(Weak)")
3692    }
3693}
3694
3695#[stable(feature = "downgraded_weak", since = "1.10.0")]
3696impl<T> Default for Weak<T> {
3697    /// Constructs a new `Weak<T>`, without allocating any memory.
3698    /// Calling [`upgrade`] on the return value always gives [`None`].
3699    ///
3700    /// [`upgrade`]: Weak::upgrade
3701    ///
3702    /// # Examples
3703    ///
3704    /// ```
3705    /// use std::rc::Weak;
3706    ///
3707    /// let empty: Weak<i64> = Default::default();
3708    /// assert!(empty.upgrade().is_none());
3709    /// ```
3710    fn default() -> Weak<T> {
3711        Weak::new()
3712    }
3713}
3714
3715// NOTE: If you mem::forget Rcs (or Weaks), drop is skipped and the ref-count
3716// is not decremented, meaning the ref-count can overflow, and then you can
3717// free the allocation while outstanding Rcs (or Weaks) exist, which would be
3718// unsound. We abort because this is such a degenerate scenario that we don't
3719// care about what happens -- no real program should ever experience this.
3720//
3721// This should have negligible overhead since you don't actually need to
3722// clone these much in Rust thanks to ownership and move-semantics.
3723
3724#[doc(hidden)]
3725trait RcInnerPtr {
3726    fn weak_ref(&self) -> &Cell<usize>;
3727    fn strong_ref(&self) -> &Cell<usize>;
3728
3729    #[inline]
3730    fn strong(&self) -> usize {
3731        self.strong_ref().get()
3732    }
3733
3734    #[inline]
3735    fn inc_strong(&self) {
3736        let strong = self.strong();
3737
3738        // We insert an `assume` here to hint LLVM at an otherwise
3739        // missed optimization.
3740        // SAFETY: The reference count will never be zero when this is
3741        // called.
3742        unsafe {
3743            hint::assert_unchecked(strong != 0);
3744        }
3745
3746        let strong = strong.wrapping_add(1);
3747        self.strong_ref().set(strong);
3748
3749        // We want to abort on overflow instead of dropping the value.
3750        // Checking for overflow after the store instead of before
3751        // allows for slightly better code generation.
3752        if core::intrinsics::unlikely(strong == 0) {
3753            abort();
3754        }
3755    }
3756
3757    #[inline]
3758    fn dec_strong(&self) {
3759        self.strong_ref().set(self.strong() - 1);
3760    }
3761
3762    #[inline]
3763    fn weak(&self) -> usize {
3764        self.weak_ref().get()
3765    }
3766
3767    #[inline]
3768    fn inc_weak(&self) {
3769        let weak = self.weak();
3770
3771        // We insert an `assume` here to hint LLVM at an otherwise
3772        // missed optimization.
3773        // SAFETY: The reference count will never be zero when this is
3774        // called.
3775        unsafe {
3776            hint::assert_unchecked(weak != 0);
3777        }
3778
3779        let weak = weak.wrapping_add(1);
3780        self.weak_ref().set(weak);
3781
3782        // We want to abort on overflow instead of dropping the value.
3783        // Checking for overflow after the store instead of before
3784        // allows for slightly better code generation.
3785        if core::intrinsics::unlikely(weak == 0) {
3786            abort();
3787        }
3788    }
3789
3790    #[inline]
3791    fn dec_weak(&self) {
3792        self.weak_ref().set(self.weak() - 1);
3793    }
3794}
3795
3796impl<T: ?Sized> RcInnerPtr for RcInner<T> {
3797    #[inline(always)]
3798    fn weak_ref(&self) -> &Cell<usize> {
3799        &self.weak
3800    }
3801
3802    #[inline(always)]
3803    fn strong_ref(&self) -> &Cell<usize> {
3804        &self.strong
3805    }
3806}
3807
3808impl<'a> RcInnerPtr for WeakInner<'a> {
3809    #[inline(always)]
3810    fn weak_ref(&self) -> &Cell<usize> {
3811        self.weak
3812    }
3813
3814    #[inline(always)]
3815    fn strong_ref(&self) -> &Cell<usize> {
3816        self.strong
3817    }
3818}
3819
3820#[stable(feature = "rust1", since = "1.0.0")]
3821impl<T: ?Sized, A: Allocator> borrow::Borrow<T> for Rc<T, A> {
3822    fn borrow(&self) -> &T {
3823        &**self
3824    }
3825}
3826
3827#[stable(since = "1.5.0", feature = "smart_ptr_as_ref")]
3828impl<T: ?Sized, A: Allocator> AsRef<T> for Rc<T, A> {
3829    fn as_ref(&self) -> &T {
3830        &**self
3831    }
3832}
3833
3834#[stable(feature = "pin", since = "1.33.0")]
3835impl<T: ?Sized, A: Allocator> Unpin for Rc<T, A> {}
3836
3837/// Gets the offset within an `RcInner` for the payload behind a pointer.
3838///
3839/// # Safety
3840///
3841/// The pointer must point to (and have valid metadata for) a previously
3842/// valid instance of T, but the T is allowed to be dropped.
3843unsafe fn data_offset<T: ?Sized>(ptr: *const T) -> usize {
3844    // Align the unsized value to the end of the RcInner.
3845    // Because RcInner is repr(C), it will always be the last field in memory.
3846    // SAFETY: since the only unsized types possible are slices, trait objects,
3847    // and extern types, the input safety requirement is currently enough to
3848    // satisfy the requirements of Alignment::of_val_raw; this is an implementation
3849    // detail of the language that must not be relied upon outside of std.
3850    unsafe { data_offset_alignment(Alignment::of_val_raw(ptr)) }
3851}
3852
3853#[inline]
3854fn data_offset_alignment(alignment: Alignment) -> usize {
3855    let layout = Layout::new::<RcInner<()>>();
3856    layout.size() + layout.padding_needed_for(alignment)
3857}
3858
3859/// A uniquely owned [`Rc`].
3860///
3861/// This represents an `Rc` that is known to be uniquely owned -- that is, have exactly one strong
3862/// reference. Multiple weak pointers can be created, but attempts to upgrade those to strong
3863/// references will fail unless the `UniqueRc` they point to has been converted into a regular `Rc`.
3864///
3865/// Because they are uniquely owned, the contents of a `UniqueRc` can be freely mutated. A common
3866/// use case is to have an object be mutable during its initialization phase but then have it become
3867/// immutable and converted to a normal `Rc`.
3868///
3869/// This can be used as a flexible way to create cyclic data structures, as in the example below.
3870///
3871/// ```
3872/// #![feature(unique_rc_arc)]
3873/// use std::rc::{Rc, Weak, UniqueRc};
3874///
3875/// struct Gadget {
3876///     #[allow(dead_code)]
3877///     me: Weak<Gadget>,
3878/// }
3879///
3880/// fn create_gadget() -> Option<Rc<Gadget>> {
3881///     let mut rc = UniqueRc::new(Gadget {
3882///         me: Weak::new(),
3883///     });
3884///     rc.me = UniqueRc::downgrade(&rc);
3885///     Some(UniqueRc::into_rc(rc))
3886/// }
3887///
3888/// create_gadget().unwrap();
3889/// ```
3890///
3891/// An advantage of using `UniqueRc` over [`Rc::new_cyclic`] to build cyclic data structures is that
3892/// [`Rc::new_cyclic`]'s `data_fn` parameter cannot be async or return a [`Result`]. As shown in the
3893/// previous example, `UniqueRc` allows for more flexibility in the construction of cyclic data,
3894/// including fallible or async constructors.
3895#[unstable(feature = "unique_rc_arc", issue = "112566")]
3896pub struct UniqueRc<
3897    T: ?Sized,
3898    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
3899> {
3900    ptr: NonNull<RcInner<T>>,
3901    // Define the ownership of `RcInner<T>` for drop-check
3902    _marker: PhantomData<RcInner<T>>,
3903    // Invariance is necessary for soundness: once other `Weak`
3904    // references exist, we already have a form of shared mutability!
3905    _marker2: PhantomData<*mut T>,
3906    alloc: A,
3907}
3908
3909// Not necessary for correctness since `UniqueRc` contains `NonNull`,
3910// but having an explicit negative impl is nice for documentation purposes
3911// and results in nicer error messages.
3912#[unstable(feature = "unique_rc_arc", issue = "112566")]
3913impl<T: ?Sized, A: Allocator> !Send for UniqueRc<T, A> {}
3914
3915// Not necessary for correctness since `UniqueRc` contains `NonNull`,
3916// but having an explicit negative impl is nice for documentation purposes
3917// and results in nicer error messages.
3918#[unstable(feature = "unique_rc_arc", issue = "112566")]
3919impl<T: ?Sized, A: Allocator> !Sync for UniqueRc<T, A> {}
3920
3921#[unstable(feature = "unique_rc_arc", issue = "112566")]
3922impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<UniqueRc<U, A>>
3923    for UniqueRc<T, A>
3924{
3925}
3926
3927//#[unstable(feature = "unique_rc_arc", issue = "112566")]
3928#[unstable(feature = "dispatch_from_dyn", issue = "none")]
3929impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<UniqueRc<U>> for UniqueRc<T> {}
3930
3931#[unstable(feature = "unique_rc_arc", issue = "112566")]
3932impl<T: ?Sized + fmt::Display, A: Allocator> fmt::Display for UniqueRc<T, A> {
3933    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3934        fmt::Display::fmt(&**self, f)
3935    }
3936}
3937
3938#[unstable(feature = "unique_rc_arc", issue = "112566")]
3939impl<T: ?Sized + fmt::Debug, A: Allocator> fmt::Debug for UniqueRc<T, A> {
3940    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3941        fmt::Debug::fmt(&**self, f)
3942    }
3943}
3944
3945#[unstable(feature = "unique_rc_arc", issue = "112566")]
3946impl<T: ?Sized, A: Allocator> fmt::Pointer for UniqueRc<T, A> {
3947    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3948        fmt::Pointer::fmt(&(&raw const **self), f)
3949    }
3950}
3951
3952#[unstable(feature = "unique_rc_arc", issue = "112566")]
3953impl<T: ?Sized, A: Allocator> borrow::Borrow<T> for UniqueRc<T, A> {
3954    fn borrow(&self) -> &T {
3955        &**self
3956    }
3957}
3958
3959#[unstable(feature = "unique_rc_arc", issue = "112566")]
3960impl<T: ?Sized, A: Allocator> borrow::BorrowMut<T> for UniqueRc<T, A> {
3961    fn borrow_mut(&mut self) -> &mut T {
3962        &mut **self
3963    }
3964}
3965
3966#[unstable(feature = "unique_rc_arc", issue = "112566")]
3967impl<T: ?Sized, A: Allocator> AsRef<T> for UniqueRc<T, A> {
3968    fn as_ref(&self) -> &T {
3969        &**self
3970    }
3971}
3972
3973#[unstable(feature = "unique_rc_arc", issue = "112566")]
3974impl<T: ?Sized, A: Allocator> AsMut<T> for UniqueRc<T, A> {
3975    fn as_mut(&mut self) -> &mut T {
3976        &mut **self
3977    }
3978}
3979
3980#[unstable(feature = "unique_rc_arc", issue = "112566")]
3981impl<T: ?Sized, A: Allocator> Unpin for UniqueRc<T, A> {}
3982
3983#[unstable(feature = "unique_rc_arc", issue = "112566")]
3984impl<T: ?Sized + PartialEq, A: Allocator> PartialEq for UniqueRc<T, A> {
3985    /// Equality for two `UniqueRc`s.
3986    ///
3987    /// Two `UniqueRc`s are equal if their inner values are equal.
3988    ///
3989    /// # Examples
3990    ///
3991    /// ```
3992    /// #![feature(unique_rc_arc)]
3993    /// use std::rc::UniqueRc;
3994    ///
3995    /// let five = UniqueRc::new(5);
3996    ///
3997    /// assert!(five == UniqueRc::new(5));
3998    /// ```
3999    #[inline]
4000    fn eq(&self, other: &Self) -> bool {
4001        PartialEq::eq(&**self, &**other)
4002    }
4003
4004    /// Inequality for two `UniqueRc`s.
4005    ///
4006    /// Two `UniqueRc`s are not equal if their inner values are not equal.
4007    ///
4008    /// # Examples
4009    ///
4010    /// ```
4011    /// #![feature(unique_rc_arc)]
4012    /// use std::rc::UniqueRc;
4013    ///
4014    /// let five = UniqueRc::new(5);
4015    ///
4016    /// assert!(five != UniqueRc::new(6));
4017    /// ```
4018    #[inline]
4019    fn ne(&self, other: &Self) -> bool {
4020        PartialEq::ne(&**self, &**other)
4021    }
4022}
4023
4024#[unstable(feature = "unique_rc_arc", issue = "112566")]
4025impl<T: ?Sized + PartialOrd, A: Allocator> PartialOrd for UniqueRc<T, A> {
4026    /// Partial comparison for two `UniqueRc`s.
4027    ///
4028    /// The two are compared by calling `partial_cmp()` on their inner values.
4029    ///
4030    /// # Examples
4031    ///
4032    /// ```
4033    /// #![feature(unique_rc_arc)]
4034    /// use std::rc::UniqueRc;
4035    /// use std::cmp::Ordering;
4036    ///
4037    /// let five = UniqueRc::new(5);
4038    ///
4039    /// assert_eq!(Some(Ordering::Less), five.partial_cmp(&UniqueRc::new(6)));
4040    /// ```
4041    #[inline(always)]
4042    fn partial_cmp(&self, other: &UniqueRc<T, A>) -> Option<Ordering> {
4043        (**self).partial_cmp(&**other)
4044    }
4045
4046    /// Less-than comparison for two `UniqueRc`s.
4047    ///
4048    /// The two are compared by calling `<` on their inner values.
4049    ///
4050    /// # Examples
4051    ///
4052    /// ```
4053    /// #![feature(unique_rc_arc)]
4054    /// use std::rc::UniqueRc;
4055    ///
4056    /// let five = UniqueRc::new(5);
4057    ///
4058    /// assert!(five < UniqueRc::new(6));
4059    /// ```
4060    #[inline(always)]
4061    fn lt(&self, other: &UniqueRc<T, A>) -> bool {
4062        **self < **other
4063    }
4064
4065    /// 'Less than or equal to' comparison for two `UniqueRc`s.
4066    ///
4067    /// The two are compared by calling `<=` on their inner values.
4068    ///
4069    /// # Examples
4070    ///
4071    /// ```
4072    /// #![feature(unique_rc_arc)]
4073    /// use std::rc::UniqueRc;
4074    ///
4075    /// let five = UniqueRc::new(5);
4076    ///
4077    /// assert!(five <= UniqueRc::new(5));
4078    /// ```
4079    #[inline(always)]
4080    fn le(&self, other: &UniqueRc<T, A>) -> bool {
4081        **self <= **other
4082    }
4083
4084    /// Greater-than comparison for two `UniqueRc`s.
4085    ///
4086    /// The two are compared by calling `>` on their inner values.
4087    ///
4088    /// # Examples
4089    ///
4090    /// ```
4091    /// #![feature(unique_rc_arc)]
4092    /// use std::rc::UniqueRc;
4093    ///
4094    /// let five = UniqueRc::new(5);
4095    ///
4096    /// assert!(five > UniqueRc::new(4));
4097    /// ```
4098    #[inline(always)]
4099    fn gt(&self, other: &UniqueRc<T, A>) -> bool {
4100        **self > **other
4101    }
4102
4103    /// 'Greater than or equal to' comparison for two `UniqueRc`s.
4104    ///
4105    /// The two are compared by calling `>=` on their inner values.
4106    ///
4107    /// # Examples
4108    ///
4109    /// ```
4110    /// #![feature(unique_rc_arc)]
4111    /// use std::rc::UniqueRc;
4112    ///
4113    /// let five = UniqueRc::new(5);
4114    ///
4115    /// assert!(five >= UniqueRc::new(5));
4116    /// ```
4117    #[inline(always)]
4118    fn ge(&self, other: &UniqueRc<T, A>) -> bool {
4119        **self >= **other
4120    }
4121}
4122
4123#[unstable(feature = "unique_rc_arc", issue = "112566")]
4124impl<T: ?Sized + Ord, A: Allocator> Ord for UniqueRc<T, A> {
4125    /// Comparison for two `UniqueRc`s.
4126    ///
4127    /// The two are compared by calling `cmp()` on their inner values.
4128    ///
4129    /// # Examples
4130    ///
4131    /// ```
4132    /// #![feature(unique_rc_arc)]
4133    /// use std::rc::UniqueRc;
4134    /// use std::cmp::Ordering;
4135    ///
4136    /// let five = UniqueRc::new(5);
4137    ///
4138    /// assert_eq!(Ordering::Less, five.cmp(&UniqueRc::new(6)));
4139    /// ```
4140    #[inline]
4141    fn cmp(&self, other: &UniqueRc<T, A>) -> Ordering {
4142        (**self).cmp(&**other)
4143    }
4144}
4145
4146#[unstable(feature = "unique_rc_arc", issue = "112566")]
4147impl<T: ?Sized + Eq, A: Allocator> Eq for UniqueRc<T, A> {}
4148
4149#[unstable(feature = "unique_rc_arc", issue = "112566")]
4150impl<T: ?Sized + Hash, A: Allocator> Hash for UniqueRc<T, A> {
4151    fn hash<H: Hasher>(&self, state: &mut H) {
4152        (**self).hash(state);
4153    }
4154}
4155
4156// Depends on A = Global
4157impl<T> UniqueRc<T> {
4158    /// Creates a new `UniqueRc`.
4159    ///
4160    /// Weak references to this `UniqueRc` can be created with [`UniqueRc::downgrade`]. Upgrading
4161    /// these weak references will fail before the `UniqueRc` has been converted into an [`Rc`].
4162    /// After converting the `UniqueRc` into an [`Rc`], any weak references created beforehand will
4163    /// point to the new [`Rc`].
4164    #[cfg(not(no_global_oom_handling))]
4165    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4166    pub fn new(value: T) -> Self {
4167        Self::new_in(value, Global)
4168    }
4169
4170    /// Maps the value in a `UniqueRc`, reusing the allocation if possible.
4171    ///
4172    /// `f` is called on a reference to the value in the `UniqueRc`, and the result is returned,
4173    /// also in a `UniqueRc`.
4174    ///
4175    /// Note: this is an associated function, which means that you have
4176    /// to call it as `UniqueRc::map(u, f)` instead of `u.map(f)`. This
4177    /// is so that there is no conflict with a method on the inner type.
4178    ///
4179    /// # Examples
4180    ///
4181    /// ```
4182    /// #![feature(smart_pointer_try_map)]
4183    /// #![feature(unique_rc_arc)]
4184    ///
4185    /// use std::rc::UniqueRc;
4186    ///
4187    /// let r = UniqueRc::new(7);
4188    /// let new = UniqueRc::map(r, |i| i + 7);
4189    /// assert_eq!(*new, 14);
4190    /// ```
4191    #[cfg(not(no_global_oom_handling))]
4192    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
4193    pub fn map<U>(this: Self, f: impl FnOnce(T) -> U) -> UniqueRc<U> {
4194        if size_of::<T>() == size_of::<U>()
4195            && align_of::<T>() == align_of::<U>()
4196            && UniqueRc::weak_count(&this) == 0
4197        {
4198            unsafe {
4199                let ptr = UniqueRc::into_raw(this);
4200                let value = ptr.read();
4201                let mut allocation = UniqueRc::from_raw(ptr.cast::<mem::MaybeUninit<U>>());
4202
4203                allocation.write(f(value));
4204                allocation.assume_init()
4205            }
4206        } else {
4207            UniqueRc::new(f(UniqueRc::unwrap(this)))
4208        }
4209    }
4210
4211    /// Attempts to map the value in a `UniqueRc`, reusing the allocation if possible.
4212    ///
4213    /// `f` is called on a reference to the value in the `UniqueRc`, and if the operation succeeds,
4214    /// the result is returned, also in a `UniqueRc`.
4215    ///
4216    /// Note: this is an associated function, which means that you have
4217    /// to call it as `UniqueRc::try_map(u, f)` instead of `u.try_map(f)`. This
4218    /// is so that there is no conflict with a method on the inner type.
4219    ///
4220    /// # Examples
4221    ///
4222    /// ```
4223    /// #![feature(smart_pointer_try_map)]
4224    /// #![feature(unique_rc_arc)]
4225    ///
4226    /// use std::rc::UniqueRc;
4227    ///
4228    /// let b = UniqueRc::new(7);
4229    /// let new = UniqueRc::try_map(b, u32::try_from).unwrap();
4230    /// assert_eq!(*new, 7);
4231    /// ```
4232    #[cfg(not(no_global_oom_handling))]
4233    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
4234    pub fn try_map<R>(
4235        this: Self,
4236        f: impl FnOnce(T) -> R,
4237    ) -> <R::Residual as Residual<UniqueRc<R::Output>>>::TryType
4238    where
4239        R: Try,
4240        R::Residual: Residual<UniqueRc<R::Output>>,
4241    {
4242        if size_of::<T>() == size_of::<R::Output>()
4243            && align_of::<T>() == align_of::<R::Output>()
4244            && UniqueRc::weak_count(&this) == 0
4245        {
4246            unsafe {
4247                let ptr = UniqueRc::into_raw(this);
4248                let value = ptr.read();
4249                let mut allocation = UniqueRc::from_raw(ptr.cast::<mem::MaybeUninit<R::Output>>());
4250
4251                allocation.write(f(value)?);
4252                try { allocation.assume_init() }
4253            }
4254        } else {
4255            try { UniqueRc::new(f(UniqueRc::unwrap(this))?) }
4256        }
4257    }
4258
4259    #[cfg(not(no_global_oom_handling))]
4260    fn unwrap(this: Self) -> T {
4261        let this = ManuallyDrop::new(this);
4262        let val: T = unsafe { ptr::read(&**this) };
4263
4264        let _weak = Weak { ptr: this.ptr, alloc: Global };
4265
4266        val
4267    }
4268}
4269
4270impl<T: ?Sized> UniqueRc<T> {
4271    #[cfg(not(no_global_oom_handling))]
4272    unsafe fn from_raw(ptr: *const T) -> Self {
4273        let offset = unsafe { data_offset(ptr) };
4274
4275        // Reverse the offset to find the original RcInner.
4276        let rc_ptr = unsafe { ptr.byte_sub(offset) as *mut RcInner<T> };
4277
4278        Self {
4279            ptr: unsafe { NonNull::new_unchecked(rc_ptr) },
4280            _marker: PhantomData,
4281            _marker2: PhantomData,
4282            alloc: Global,
4283        }
4284    }
4285
4286    #[cfg(not(no_global_oom_handling))]
4287    fn into_raw(this: Self) -> *const T {
4288        let this = ManuallyDrop::new(this);
4289        Self::as_ptr(&*this)
4290    }
4291}
4292
4293impl<T, A: Allocator> UniqueRc<T, A> {
4294    /// Creates a new `UniqueRc` in the provided allocator.
4295    ///
4296    /// Weak references to this `UniqueRc` can be created with [`UniqueRc::downgrade`]. Upgrading
4297    /// these weak references will fail before the `UniqueRc` has been converted into an [`Rc`].
4298    /// After converting the `UniqueRc` into an [`Rc`], any weak references created beforehand will
4299    /// point to the new [`Rc`].
4300    #[cfg(not(no_global_oom_handling))]
4301    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4302    pub fn new_in(value: T, alloc: A) -> Self {
4303        let (ptr, alloc) = Box::into_unique(Box::new_in(
4304            RcInner {
4305                strong: Cell::new(0),
4306                // keep one weak reference so if all the weak pointers that are created are dropped
4307                // the UniqueRc still stays valid.
4308                weak: Cell::new(1),
4309                value,
4310            },
4311            alloc,
4312        ));
4313        Self { ptr: ptr.into(), _marker: PhantomData, _marker2: PhantomData, alloc }
4314    }
4315}
4316
4317impl<T: ?Sized, A: Allocator> UniqueRc<T, A> {
4318    /// Converts the `UniqueRc` into a regular [`Rc`].
4319    ///
4320    /// This consumes the `UniqueRc` and returns a regular [`Rc`] that contains the `value` that
4321    /// is passed to `into_rc`.
4322    ///
4323    /// Any weak references created before this method is called can now be upgraded to strong
4324    /// references.
4325    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4326    pub fn into_rc(this: Self) -> Rc<T, A> {
4327        let mut this = ManuallyDrop::new(this);
4328
4329        // Move the allocator out.
4330        // SAFETY: `this.alloc` will not be accessed again, nor dropped because it is in
4331        // a `ManuallyDrop`.
4332        let alloc: A = unsafe { ptr::read(&this.alloc) };
4333
4334        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4335        unsafe {
4336            // Convert our weak reference into a strong reference
4337            this.ptr.as_mut().strong.set(1);
4338            Rc::from_inner_in(this.ptr, alloc)
4339        }
4340    }
4341
4342    #[cfg(not(no_global_oom_handling))]
4343    fn weak_count(this: &Self) -> usize {
4344        this.inner().weak() - 1
4345    }
4346
4347    #[cfg(not(no_global_oom_handling))]
4348    fn inner(&self) -> &RcInner<T> {
4349        // SAFETY: while this UniqueRc is alive we're guaranteed that the inner pointer is valid.
4350        unsafe { self.ptr.as_ref() }
4351    }
4352
4353    #[cfg(not(no_global_oom_handling))]
4354    fn as_ptr(this: &Self) -> *const T {
4355        let ptr: *mut RcInner<T> = NonNull::as_ptr(this.ptr);
4356
4357        // SAFETY: This cannot go through Deref::deref or UniqueRc::inner because
4358        // this is required to retain raw/mut provenance such that e.g. `get_mut` can
4359        // write through the pointer after the Rc is recovered through `from_raw`.
4360        unsafe { &raw mut (*ptr).value }
4361    }
4362
4363    #[inline]
4364    #[cfg(not(no_global_oom_handling))]
4365    fn into_inner_with_allocator(this: Self) -> (NonNull<RcInner<T>>, A) {
4366        let this = mem::ManuallyDrop::new(this);
4367        (this.ptr, unsafe { ptr::read(&this.alloc) })
4368    }
4369
4370    #[inline]
4371    #[cfg(not(no_global_oom_handling))]
4372    unsafe fn from_inner_in(ptr: NonNull<RcInner<T>>, alloc: A) -> Self {
4373        Self { ptr, _marker: PhantomData, _marker2: PhantomData, alloc }
4374    }
4375}
4376
4377impl<T: ?Sized, A: Allocator + Clone> UniqueRc<T, A> {
4378    /// Creates a new weak reference to the `UniqueRc`.
4379    ///
4380    /// Attempting to upgrade this weak reference will fail before the `UniqueRc` has been converted
4381    /// to a [`Rc`] using [`UniqueRc::into_rc`].
4382    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4383    pub fn downgrade(this: &Self) -> Weak<T, A> {
4384        // SAFETY: This pointer was allocated at creation time and we guarantee that we only have
4385        // one strong reference before converting to a regular Rc.
4386        unsafe {
4387            this.ptr.as_ref().inc_weak();
4388        }
4389        Weak { ptr: this.ptr, alloc: this.alloc.clone() }
4390    }
4391}
4392
4393#[cfg(not(no_global_oom_handling))]
4394impl<T, A: Allocator> UniqueRc<mem::MaybeUninit<T>, A> {
4395    unsafe fn assume_init(self) -> UniqueRc<T, A> {
4396        let (ptr, alloc) = UniqueRc::into_inner_with_allocator(self);
4397        unsafe { UniqueRc::from_inner_in(ptr.cast(), alloc) }
4398    }
4399}
4400
4401#[unstable(feature = "unique_rc_arc", issue = "112566")]
4402impl<T: ?Sized, A: Allocator> Deref for UniqueRc<T, A> {
4403    type Target = T;
4404
4405    fn deref(&self) -> &T {
4406        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4407        unsafe { &self.ptr.as_ref().value }
4408    }
4409}
4410
4411#[unstable(feature = "unique_rc_arc", issue = "112566")]
4412impl<T: ?Sized, A: Allocator> DerefMut for UniqueRc<T, A> {
4413    fn deref_mut(&mut self) -> &mut T {
4414        // SAFETY: This pointer was allocated at creation time so we know it is valid. We know we
4415        // have unique ownership and therefore it's safe to make a mutable reference because
4416        // `UniqueRc` owns the only strong reference to itself.
4417        unsafe { &mut (*self.ptr.as_ptr()).value }
4418    }
4419}
4420
4421#[unstable(feature = "unique_rc_arc", issue = "112566")]
4422unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for UniqueRc<T, A> {
4423    fn drop(&mut self) {
4424        unsafe {
4425            // destroy the contained object
4426            drop_in_place(DerefMut::deref_mut(self));
4427
4428            // remove the implicit "strong weak" pointer now that we've destroyed the contents.
4429            self.ptr.as_ref().dec_weak();
4430
4431            if self.ptr.as_ref().weak() == 0 {
4432                self.alloc.deallocate(self.ptr.cast(), Layout::for_value_raw(self.ptr.as_ptr()));
4433            }
4434        }
4435    }
4436}
4437
4438/// A unique owning pointer to a [`RcInner`] **that does not imply the contents are initialized,**
4439/// but will deallocate it (without dropping the value) when dropped.
4440///
4441/// This is a helper for [`Rc::make_mut()`] to ensure correct cleanup on panic.
4442/// It is nearly a duplicate of `UniqueRc<MaybeUninit<T>, A>` except that it allows `T: !Sized`,
4443/// which `MaybeUninit` does not.
4444struct UniqueRcUninit<T: ?Sized, A: Allocator> {
4445    ptr: NonNull<RcInner<T>>,
4446    layout_for_value: Layout,
4447    alloc: Option<A>,
4448}
4449
4450impl<T: ?Sized, A: Allocator> UniqueRcUninit<T, A> {
4451    /// Allocates a RcInner with layout suitable to contain `for_value` or a clone of it.
4452    #[cfg(not(no_global_oom_handling))]
4453    fn new(for_value: &T, alloc: A) -> UniqueRcUninit<T, A> {
4454        let layout = Layout::for_value(for_value);
4455        let ptr = unsafe {
4456            Rc::allocate_for_layout(
4457                layout,
4458                |layout_for_rc_inner| alloc.allocate(layout_for_rc_inner),
4459                |mem| mem.with_metadata_of(ptr::from_ref(for_value) as *const RcInner<T>),
4460            )
4461        };
4462        Self { ptr: NonNull::new(ptr).unwrap(), layout_for_value: layout, alloc: Some(alloc) }
4463    }
4464
4465    /// Allocates a RcInner with layout suitable to contain `for_value` or a clone of it,
4466    /// returning an error if allocation fails.
4467    fn try_new(for_value: &T, alloc: A) -> Result<UniqueRcUninit<T, A>, AllocError> {
4468        let layout = Layout::for_value(for_value);
4469        let ptr = unsafe {
4470            Rc::try_allocate_for_layout(
4471                layout,
4472                |layout_for_rc_inner| alloc.allocate(layout_for_rc_inner),
4473                |mem| mem.with_metadata_of(ptr::from_ref(for_value) as *const RcInner<T>),
4474            )?
4475        };
4476        Ok(Self { ptr: NonNull::new(ptr).unwrap(), layout_for_value: layout, alloc: Some(alloc) })
4477    }
4478
4479    /// Returns the pointer to be written into to initialize the [`Rc`].
4480    fn data_ptr(&mut self) -> *mut T {
4481        let offset = data_offset_alignment(self.layout_for_value.alignment());
4482        unsafe { self.ptr.as_ptr().byte_add(offset) as *mut T }
4483    }
4484
4485    /// Upgrade this into a normal [`Rc`].
4486    ///
4487    /// # Safety
4488    ///
4489    /// The data must have been initialized (by writing to [`Self::data_ptr()`]).
4490    unsafe fn into_rc(self) -> Rc<T, A> {
4491        let mut this = ManuallyDrop::new(self);
4492        let ptr = this.ptr;
4493        let alloc = this.alloc.take().unwrap();
4494
4495        // SAFETY: The pointer is valid as per `UniqueRcUninit::new`, and the caller is responsible
4496        // for having initialized the data.
4497        unsafe { Rc::from_ptr_in(ptr.as_ptr(), alloc) }
4498    }
4499}
4500
4501impl<T: ?Sized, A: Allocator> Drop for UniqueRcUninit<T, A> {
4502    fn drop(&mut self) {
4503        // SAFETY:
4504        // * new() produced a pointer safe to deallocate.
4505        // * We own the pointer unless into_rc() was called, which forgets us.
4506        unsafe {
4507            self.alloc.take().unwrap().deallocate(
4508                self.ptr.cast(),
4509                rc_inner_layout_for_value_layout(self.layout_for_value),
4510            );
4511        }
4512    }
4513}
4514
4515#[unstable(feature = "allocator_api", issue = "32838")]
4516unsafe impl<T: ?Sized + Allocator, A: Allocator> Allocator for Rc<T, A> {
4517    #[inline]
4518    fn allocate(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
4519        (**self).allocate(layout)
4520    }
4521
4522    #[inline]
4523    fn allocate_zeroed(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
4524        (**self).allocate_zeroed(layout)
4525    }
4526
4527    #[inline]
4528    unsafe fn deallocate(&self, ptr: NonNull<u8>, layout: Layout) {
4529        // SAFETY: the safety contract must be upheld by the caller
4530        unsafe { (**self).deallocate(ptr, layout) }
4531    }
4532
4533    #[inline]
4534    unsafe fn grow(
4535        &self,
4536        ptr: NonNull<u8>,
4537        old_layout: Layout,
4538        new_layout: Layout,
4539    ) -> Result<NonNull<[u8]>, AllocError> {
4540        // SAFETY: the safety contract must be upheld by the caller
4541        unsafe { (**self).grow(ptr, old_layout, new_layout) }
4542    }
4543
4544    #[inline]
4545    unsafe fn grow_zeroed(
4546        &self,
4547        ptr: NonNull<u8>,
4548        old_layout: Layout,
4549        new_layout: Layout,
4550    ) -> Result<NonNull<[u8]>, AllocError> {
4551        // SAFETY: the safety contract must be upheld by the caller
4552        unsafe { (**self).grow_zeroed(ptr, old_layout, new_layout) }
4553    }
4554
4555    #[inline]
4556    unsafe fn shrink(
4557        &self,
4558        ptr: NonNull<u8>,
4559        old_layout: Layout,
4560        new_layout: Layout,
4561    ) -> Result<NonNull<[u8]>, AllocError> {
4562        // SAFETY: the safety contract must be upheld by the caller
4563        unsafe { (**self).shrink(ptr, old_layout, new_layout) }
4564    }
4565}
````