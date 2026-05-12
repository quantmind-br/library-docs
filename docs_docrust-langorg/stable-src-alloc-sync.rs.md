---
title: sync.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/sync.rs.html#3941
source: crawler
fetched_at: 2026-05-06T21:33:54.479557999-03:00
rendered_js: false
word_count: 22533
summary: This document defines the implementation of Arc, a thread-safe, atomically reference-counted pointer for sharing heap-allocated data across threads in Rust.
tags:
    - rust
    - memory-management
    - concurrency
    - smart-pointers
    - reference-counting
    - atomic
    - thread-safety
category: reference
---

## alloc/ sync.rs

````rust
1#![stable(feature = "rust1", since = "1.0.0")]
2
3//! Thread-safe reference-counting pointers.
4//!
5//! See the [`Arc<T>`][Arc] documentation for more details.
6//!
7//! **Note**: This module is only available on platforms that support atomic
8//! loads and stores of pointers. This may be detected at compile time using
9//! `#[cfg(target_has_atomic = "ptr")]`.
10
11use core::any::Any;
12use core::cell::CloneFromCell;
13#[cfg(not(no_global_oom_handling))]
14use core::clone::TrivialClone;
15use core::clone::{CloneToUninit, UseCloned};
16use core::cmp::Ordering;
17use core::hash::{Hash, Hasher};
18use core::intrinsics::abort;
19#[cfg(not(no_global_oom_handling))]
20use core::iter;
21use core::marker::{PhantomData, Unsize};
22use core::mem::{self, ManuallyDrop};
23use core::num::NonZeroUsize;
24use core::ops::{CoerceUnsized, Deref, DerefMut, DerefPure, DispatchFromDyn, LegacyReceiver};
25#[cfg(not(no_global_oom_handling))]
26use core::ops::{Residual, Try};
27use core::panic::{RefUnwindSafe, UnwindSafe};
28use core::pin::{Pin, PinCoerceUnsized};
29use core::ptr::{self, Alignment, NonNull};
30#[cfg(not(no_global_oom_handling))]
31use core::slice::from_raw_parts_mut;
32use core::sync::atomic::Ordering::{Acquire, Relaxed, Release};
33use core::sync::atomic::{self, Atomic};
34use core::{borrow, fmt, hint};
35
36#[cfg(not(no_global_oom_handling))]
37use crate::alloc::handle_alloc_error;
38use crate::alloc::{AllocError, Allocator, Global, Layout};
39use crate::borrow::{Cow, ToOwned};
40use crate::boxed::Box;
41use crate::rc::is_dangling;
42#[cfg(not(no_global_oom_handling))]
43use crate::string::String;
44#[cfg(not(no_global_oom_handling))]
45use crate::vec::Vec;
46
47/// A soft limit on the amount of references that may be made to an `Arc`.
48///
49/// Going above this limit will abort your program (although not
50/// necessarily) at _exactly_ `MAX_REFCOUNT + 1` references.
51/// Trying to go above it might call a `panic` (if not actually going above it).
52///
53/// This is a global invariant, and also applies when using a compare-exchange loop.
54///
55/// See comment in `Arc::clone`.
56const MAX_REFCOUNT: usize = (isize::MAX) as usize;
57
58/// The error in case either counter reaches above `MAX_REFCOUNT`, and we can `panic` safely.
59const INTERNAL_OVERFLOW_ERROR: &str = "Arc counter overflow";
60
61#[cfg(not(sanitize = "thread"))]
62macro_rules! acquire {
63    ($x:expr) => {
64        atomic::fence(Acquire)
65    };
66}
67
68// ThreadSanitizer does not support memory fences. To avoid false positive
69// reports in Arc / Weak implementation use atomic loads for synchronization
70// instead.
71#[cfg(sanitize = "thread")]
72macro_rules! acquire {
73    ($x:expr) => {
74        $x.load(Acquire)
75    };
76}
77
78/// A thread-safe reference-counting pointer. 'Arc' stands for 'Atomically
79/// Reference Counted'.
80///
81/// The type `Arc<T>` provides shared ownership of a value of type `T`,
82/// allocated in the heap. Invoking [`clone`][clone] on `Arc` produces
83/// a new `Arc` instance, which points to the same allocation on the heap as the
84/// source `Arc`, while increasing a reference count. When the last `Arc`
85/// pointer to a given allocation is destroyed, the value stored in that allocation (often
86/// referred to as "inner value") is also dropped.
87///
88/// Shared references in Rust disallow mutation by default, and `Arc` is no
89/// exception: you cannot generally obtain a mutable reference to something
90/// inside an `Arc`. If you do need to mutate through an `Arc`, you have several options:
91///
92/// 1. Use interior mutability with synchronization primitives like [`Mutex`][mutex],
93///    [`RwLock`][rwlock], or one of the [`Atomic`][atomic] types.
94///
95/// 2. Use clone-on-write semantics with [`Arc::make_mut`] which provides efficient mutation
96///    without requiring interior mutability. This approach clones the data only when
97///    needed (when there are multiple references) and can be more efficient when mutations
98///    are infrequent.
99///
100/// 3. Use [`Arc::get_mut`] when you know your `Arc` is not shared (has a reference count of 1),
101///    which provides direct mutable access to the inner value without any cloning.
102///
103/// ```
104/// use std::sync::Arc;
105///
106/// let mut data = Arc::new(vec![1, 2, 3]);
107///
108/// // This will clone the vector only if there are other references to it
109/// Arc::make_mut(&mut data).push(4);
110///
111/// assert_eq!(*data, vec![1, 2, 3, 4]);
112/// ```
113///
114/// **Note**: This type is only available on platforms that support atomic
115/// loads and stores of pointers, which includes all platforms that support
116/// the `std` crate but not all those which only support [`alloc`](crate).
117/// This may be detected at compile time using `#[cfg(target_has_atomic = "ptr")]`.
118///
119/// ## Thread Safety
120///
121/// Unlike [`Rc<T>`], `Arc<T>` uses atomic operations for its reference
122/// counting. This means that it is thread-safe. The disadvantage is that
123/// atomic operations are more expensive than ordinary memory accesses. If you
124/// are not sharing reference-counted allocations between threads, consider using
125/// [`Rc<T>`] for lower overhead. [`Rc<T>`] is a safe default, because the
126/// compiler will catch any attempt to send an [`Rc<T>`] between threads.
127/// However, a library might choose `Arc<T>` in order to give library consumers
128/// more flexibility.
129///
130/// `Arc<T>` will implement [`Send`] and [`Sync`] as long as the `T` implements
131/// [`Send`] and [`Sync`]. Why can't you put a non-thread-safe type `T` in an
132/// `Arc<T>` to make it thread-safe? This may be a bit counter-intuitive at
133/// first: after all, isn't the point of `Arc<T>` thread safety? The key is
134/// this: `Arc<T>` makes it thread safe to have multiple ownership of the same
135/// data, but it  doesn't add thread safety to its data. Consider
136/// <code>Arc<[RefCell\<T>]></code>. [`RefCell<T>`] isn't [`Sync`], and if `Arc<T>` was always
137/// [`Send`], <code>Arc<[RefCell\<T>]></code> would be as well. But then we'd have a problem:
138/// [`RefCell<T>`] is not thread safe; it keeps track of the borrowing count using
139/// non-atomic operations.
140///
141/// In the end, this means that you may need to pair `Arc<T>` with some sort of
142/// [`std::sync`] type, usually [`Mutex<T>`][mutex].
143///
144/// ## Breaking cycles with `Weak`
145///
146/// The [`downgrade`][downgrade] method can be used to create a non-owning
147/// [`Weak`] pointer. A [`Weak`] pointer can be [`upgrade`][upgrade]d
148/// to an `Arc`, but this will return [`None`] if the value stored in the allocation has
149/// already been dropped. In other words, `Weak` pointers do not keep the value
150/// inside the allocation alive; however, they *do* keep the allocation
151/// (the backing store for the value) alive.
152///
153/// A cycle between `Arc` pointers will never be deallocated. For this reason,
154/// [`Weak`] is used to break cycles. For example, a tree could have
155/// strong `Arc` pointers from parent nodes to children, and [`Weak`]
156/// pointers from children back to their parents.
157///
158/// # Cloning references
159///
160/// Creating a new reference from an existing reference-counted pointer is done using the
161/// `Clone` trait implemented for [`Arc<T>`][Arc] and [`Weak<T>`][Weak].
162///
163/// ```
164/// use std::sync::Arc;
165/// let foo = Arc::new(vec![1.0, 2.0, 3.0]);
166/// // The two syntaxes below are equivalent.
167/// let a = foo.clone();
168/// let b = Arc::clone(&foo);
169/// // a, b, and foo are all Arcs that point to the same memory location
170/// ```
171///
172/// ## `Deref` behavior
173///
174/// `Arc<T>` automatically dereferences to `T` (via the [`Deref`] trait),
175/// so you can call `T`'s methods on a value of type `Arc<T>`. To avoid name
176/// clashes with `T`'s methods, the methods of `Arc<T>` itself are associated
177/// functions, called using [fully qualified syntax]:
178///
179/// ```
180/// use std::sync::Arc;
181///
182/// let my_arc = Arc::new(());
183/// let my_weak = Arc::downgrade(&my_arc);
184/// ```
185///
186/// `Arc<T>`'s implementations of traits like `Clone` may also be called using
187/// fully qualified syntax. Some people prefer to use fully qualified syntax,
188/// while others prefer using method-call syntax.
189///
190/// ```
191/// use std::sync::Arc;
192///
193/// let arc = Arc::new(());
194/// // Method-call syntax
195/// let arc2 = arc.clone();
196/// // Fully qualified syntax
197/// let arc3 = Arc::clone(&arc);
198/// ```
199///
200/// [`Weak<T>`][Weak] does not auto-dereference to `T`, because the inner value may have
201/// already been dropped.
202///
203/// [`Rc<T>`]: crate::rc::Rc
204/// [clone]: Clone::clone
205/// [mutex]: ../../std/sync/struct.Mutex.html
206/// [rwlock]: ../../std/sync/struct.RwLock.html
207/// [atomic]: core::sync::atomic
208/// [downgrade]: Arc::downgrade
209/// [upgrade]: Weak::upgrade
210/// [RefCell\<T>]: core::cell::RefCell
211/// [`RefCell<T>`]: core::cell::RefCell
212/// [`std::sync`]: ../../std/sync/index.html
213/// [`Arc::clone(&from)`]: Arc::clone
214/// [fully qualified syntax]: https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-for-disambiguation-calling-methods-with-the-same-name
215///
216/// # Examples
217///
218/// Sharing some immutable data between threads:
219///
220/// ```
221/// use std::sync::Arc;
222/// use std::thread;
223///
224/// let five = Arc::new(5);
225///
226/// for _ in 0..10 {
227///     let five = Arc::clone(&five);
228///
229///     thread::spawn(move || {
230///         println!("{five:?}");
231///     });
232/// }
233/// ```
234///
235/// Sharing a mutable [`AtomicUsize`]:
236///
237/// [`AtomicUsize`]: core::sync::atomic::AtomicUsize "sync::atomic::AtomicUsize"
238///
239/// ```
240/// use std::sync::Arc;
241/// use std::sync::atomic::{AtomicUsize, Ordering};
242/// use std::thread;
243///
244/// let val = Arc::new(AtomicUsize::new(5));
245///
246/// for _ in 0..10 {
247///     let val = Arc::clone(&val);
248///
249///     thread::spawn(move || {
250///         let v = val.fetch_add(1, Ordering::Relaxed);
251///         println!("{v:?}");
252///     });
253/// }
254/// ```
255///
256/// See the [`rc` documentation][rc_examples] for more examples of reference
257/// counting in general.
258///
259/// [rc_examples]: crate::rc#examples
260#[doc(search_unbox)]
261#[rustc_diagnostic_item = "Arc"]
262#[stable(feature = "rust1", since = "1.0.0")]
263#[rustc_insignificant_dtor]
264pub struct Arc<
265    T: ?Sized,
266    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
267> {
268    ptr: NonNull<ArcInner<T>>,
269    phantom: PhantomData<ArcInner<T>>,
270    alloc: A,
271}
272
273#[stable(feature = "rust1", since = "1.0.0")]
274unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Send> Send for Arc<T, A> {}
275#[stable(feature = "rust1", since = "1.0.0")]
276unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Sync> Sync for Arc<T, A> {}
277
278#[stable(feature = "catch_unwind", since = "1.9.0")]
279impl<T: RefUnwindSafe + ?Sized, A: Allocator + UnwindSafe> UnwindSafe for Arc<T, A> {}
280
281#[unstable(feature = "coerce_unsized", issue = "18598")]
282impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<Arc<U, A>> for Arc<T, A> {}
283
284#[unstable(feature = "dispatch_from_dyn", issue = "none")]
285impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<Arc<U>> for Arc<T> {}
286
287// SAFETY: `Arc::clone` doesn't access any `Cell`s which could contain the `Arc` being cloned.
288#[unstable(feature = "cell_get_cloned", issue = "145329")]
289unsafe impl<T: ?Sized> CloneFromCell for Arc<T> {}
290
291impl<T: ?Sized> Arc<T> {
292    unsafe fn from_inner(ptr: NonNull<ArcInner<T>>) -> Self {
293        unsafe { Self::from_inner_in(ptr, Global) }
294    }
295
296    unsafe fn from_ptr(ptr: *mut ArcInner<T>) -> Self {
297        unsafe { Self::from_ptr_in(ptr, Global) }
298    }
299}
300
301impl<T: ?Sized, A: Allocator> Arc<T, A> {
302    #[inline]
303    fn into_inner_with_allocator(this: Self) -> (NonNull<ArcInner<T>>, A) {
304        let this = mem::ManuallyDrop::new(this);
305        (this.ptr, unsafe { ptr::read(&this.alloc) })
306    }
307
308    #[inline]
309    unsafe fn from_inner_in(ptr: NonNull<ArcInner<T>>, alloc: A) -> Self {
310        Self { ptr, phantom: PhantomData, alloc }
311    }
312
313    #[inline]
314    unsafe fn from_ptr_in(ptr: *mut ArcInner<T>, alloc: A) -> Self {
315        unsafe { Self::from_inner_in(NonNull::new_unchecked(ptr), alloc) }
316    }
317}
318
319/// `Weak` is a version of [`Arc`] that holds a non-owning reference to the
320/// managed allocation.
321///
322/// The allocation is accessed by calling [`upgrade`] on the `Weak`
323/// pointer, which returns an <code>[Option]<[Arc]\<T>></code>.
324///
325/// Since a `Weak` reference does not count towards ownership, it will not
326/// prevent the value stored in the allocation from being dropped, and `Weak` itself makes no
327/// guarantees about the value still being present. Thus it may return [`None`]
328/// when [`upgrade`]d. Note however that a `Weak` reference *does* prevent the allocation
329/// itself (the backing store) from being deallocated.
330///
331/// A `Weak` pointer is useful for keeping a temporary reference to the allocation
332/// managed by [`Arc`] without preventing its inner value from being dropped. It is also used to
333/// prevent circular references between [`Arc`] pointers, since mutual owning references
334/// would never allow either [`Arc`] to be dropped. For example, a tree could
335/// have strong [`Arc`] pointers from parent nodes to children, and `Weak`
336/// pointers from children back to their parents.
337///
338/// The typical way to obtain a `Weak` pointer is to call [`Arc::downgrade`].
339///
340/// [`upgrade`]: Weak::upgrade
341#[stable(feature = "arc_weak", since = "1.4.0")]
342#[rustc_diagnostic_item = "ArcWeak"]
343pub struct Weak<
344    T: ?Sized,
345    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
346> {
347    // This is a `NonNull` to allow optimizing the size of this type in enums,
348    // but it is not necessarily a valid pointer.
349    // `Weak::new` sets this to `usize::MAX` so that it doesn’t need
350    // to allocate space on the heap. That's not a value a real pointer
351    // will ever have because ArcInner has alignment at least 2.
352    ptr: NonNull<ArcInner<T>>,
353    alloc: A,
354}
355
356#[stable(feature = "arc_weak", since = "1.4.0")]
357unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Send> Send for Weak<T, A> {}
358#[stable(feature = "arc_weak", since = "1.4.0")]
359unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Sync> Sync for Weak<T, A> {}
360
361#[unstable(feature = "coerce_unsized", issue = "18598")]
362impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<Weak<U, A>> for Weak<T, A> {}
363#[unstable(feature = "dispatch_from_dyn", issue = "none")]
364impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<Weak<U>> for Weak<T> {}
365
366// SAFETY: `Weak::clone` doesn't access any `Cell`s which could contain the `Weak` being cloned.
367#[unstable(feature = "cell_get_cloned", issue = "145329")]
368unsafe impl<T: ?Sized> CloneFromCell for Weak<T> {}
369
370#[stable(feature = "arc_weak", since = "1.4.0")]
371impl<T: ?Sized, A: Allocator> fmt::Debug for Weak<T, A> {
372    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
373        write!(f, "(Weak)")
374    }
375}
376
377// This is repr(C) to future-proof against possible field-reordering, which
378// would interfere with otherwise safe [into|from]_raw() of transmutable
379// inner types.
380// Unlike RcInner, repr(align(2)) is not strictly required because atomic types
381// have the alignment same as its size, but we use it for consistency and clarity.
382#[repr(C, align(2))]
383struct ArcInner<T: ?Sized> {
384    strong: Atomic<usize>,
385
386    // the value usize::MAX acts as a sentinel for temporarily "locking" the
387    // ability to upgrade weak pointers or downgrade strong ones; this is used
388    // to avoid races in `make_mut` and `get_mut`.
389    weak: Atomic<usize>,
390
391    data: T,
392}
393
394/// Calculate layout for `ArcInner<T>` using the inner value's layout
395fn arcinner_layout_for_value_layout(layout: Layout) -> Layout {
396    // Calculate layout using the given value layout.
397    // Previously, layout was calculated on the expression
398    // `&*(ptr as *const ArcInner<T>)`, but this created a misaligned
399    // reference (see #54908).
400    Layout::new::<ArcInner<()>>().extend(layout).unwrap().0.pad_to_align()
401}
402
403unsafe impl<T: ?Sized + Sync + Send> Send for ArcInner<T> {}
404unsafe impl<T: ?Sized + Sync + Send> Sync for ArcInner<T> {}
405
406impl<T> Arc<T> {
407    /// Constructs a new `Arc<T>`.
408    ///
409    /// # Examples
410    ///
411    /// ```
412    /// use std::sync::Arc;
413    ///
414    /// let five = Arc::new(5);
415    /// ```
416    #[cfg(not(no_global_oom_handling))]
417    #[inline]
418    #[stable(feature = "rust1", since = "1.0.0")]
419    pub fn new(data: T) -> Arc<T> {
420        // Start the weak pointer count as 1 which is the weak pointer that's
421        // held by all the strong pointers (kinda), see std/rc.rs for more info
422        let x: Box<_> = Box::new(ArcInner {
423            strong: atomic::AtomicUsize::new(1),
424            weak: atomic::AtomicUsize::new(1),
425            data,
426        });
427        unsafe { Self::from_inner(Box::leak(x).into()) }
428    }
429
430    /// Constructs a new `Arc<T>` while giving you a `Weak<T>` to the allocation,
431    /// to allow you to construct a `T` which holds a weak pointer to itself.
432    ///
433    /// Generally, a structure circularly referencing itself, either directly or
434    /// indirectly, should not hold a strong reference to itself to prevent a memory leak.
435    /// Using this function, you get access to the weak pointer during the
436    /// initialization of `T`, before the `Arc<T>` is created, such that you can
437    /// clone and store it inside the `T`.
438    ///
439    /// `new_cyclic` first allocates the managed allocation for the `Arc<T>`,
440    /// then calls your closure, giving it a `Weak<T>` to this allocation,
441    /// and only afterwards completes the construction of the `Arc<T>` by placing
442    /// the `T` returned from your closure into the allocation.
443    ///
444    /// Since the new `Arc<T>` is not fully-constructed until `Arc<T>::new_cyclic`
445    /// returns, calling [`upgrade`] on the weak reference inside your closure will
446    /// fail and result in a `None` value.
447    ///
448    /// # Panics
449    ///
450    /// If `data_fn` panics, the panic is propagated to the caller, and the
451    /// temporary [`Weak<T>`] is dropped normally.
452    ///
453    /// # Example
454    ///
455    /// ```
456    /// # #![allow(dead_code)]
457    /// use std::sync::{Arc, Weak};
458    ///
459    /// struct Gadget {
460    ///     me: Weak<Gadget>,
461    /// }
462    ///
463    /// impl Gadget {
464    ///     /// Constructs a reference counted Gadget.
465    ///     fn new() -> Arc<Self> {
466    ///         // `me` is a `Weak<Gadget>` pointing at the new allocation of the
467    ///         // `Arc` we're constructing.
468    ///         Arc::new_cyclic(|me| {
469    ///             // Create the actual struct here.
470    ///             Gadget { me: me.clone() }
471    ///         })
472    ///     }
473    ///
474    ///     /// Returns a reference counted pointer to Self.
475    ///     fn me(&self) -> Arc<Self> {
476    ///         self.me.upgrade().unwrap()
477    ///     }
478    /// }
479    /// ```
480    /// [`upgrade`]: Weak::upgrade
481    #[cfg(not(no_global_oom_handling))]
482    #[inline]
483    #[stable(feature = "arc_new_cyclic", since = "1.60.0")]
484    pub fn new_cyclic<F>(data_fn: F) -> Arc<T>
485    where
486        F: FnOnce(&Weak<T>) -> T,
487    {
488        Self::new_cyclic_in(data_fn, Global)
489    }
490
491    /// Constructs a new `Arc` with uninitialized contents.
492    ///
493    /// # Examples
494    ///
495    /// ```
496    /// use std::sync::Arc;
497    ///
498    /// let mut five = Arc::<u32>::new_uninit();
499    ///
500    /// // Deferred initialization:
501    /// Arc::get_mut(&mut five).unwrap().write(5);
502    ///
503    /// let five = unsafe { five.assume_init() };
504    ///
505    /// assert_eq!(*five, 5)
506    /// ```
507    #[cfg(not(no_global_oom_handling))]
508    #[inline]
509    #[stable(feature = "new_uninit", since = "1.82.0")]
510    #[must_use]
511    pub fn new_uninit() -> Arc<mem::MaybeUninit<T>> {
512        unsafe {
513            Arc::from_ptr(Arc::allocate_for_layout(
514                Layout::new::<T>(),
515                |layout| Global.allocate(layout),
516                <*mut u8>::cast,
517            ))
518        }
519    }
520
521    /// Constructs a new `Arc` with uninitialized contents, with the memory
522    /// being filled with `0` bytes.
523    ///
524    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
525    /// of this method.
526    ///
527    /// # Examples
528    ///
529    /// ```
530    /// use std::sync::Arc;
531    ///
532    /// let zero = Arc::<u32>::new_zeroed();
533    /// let zero = unsafe { zero.assume_init() };
534    ///
535    /// assert_eq!(*zero, 0)
536    /// ```
537    ///
538    /// [zeroed]: mem::MaybeUninit::zeroed
539    #[cfg(not(no_global_oom_handling))]
540    #[inline]
541    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
542    #[must_use]
543    pub fn new_zeroed() -> Arc<mem::MaybeUninit<T>> {
544        unsafe {
545            Arc::from_ptr(Arc::allocate_for_layout(
546                Layout::new::<T>(),
547                |layout| Global.allocate_zeroed(layout),
548                <*mut u8>::cast,
549            ))
550        }
551    }
552
553    /// Constructs a new `Pin<Arc<T>>`. If `T` does not implement `Unpin`, then
554    /// `data` will be pinned in memory and unable to be moved.
555    #[cfg(not(no_global_oom_handling))]
556    #[stable(feature = "pin", since = "1.33.0")]
557    #[must_use]
558    pub fn pin(data: T) -> Pin<Arc<T>> {
559        unsafe { Pin::new_unchecked(Arc::new(data)) }
560    }
561
562    /// Constructs a new `Pin<Arc<T>>`, return an error if allocation fails.
563    #[unstable(feature = "allocator_api", issue = "32838")]
564    #[inline]
565    pub fn try_pin(data: T) -> Result<Pin<Arc<T>>, AllocError> {
566        unsafe { Ok(Pin::new_unchecked(Arc::try_new(data)?)) }
567    }
568
569    /// Constructs a new `Arc<T>`, returning an error if allocation fails.
570    ///
571    /// # Examples
572    ///
573    /// ```
574    /// #![feature(allocator_api)]
575    /// use std::sync::Arc;
576    ///
577    /// let five = Arc::try_new(5)?;
578    /// # Ok::<(), std::alloc::AllocError>(())
579    /// ```
580    #[unstable(feature = "allocator_api", issue = "32838")]
581    #[inline]
582    pub fn try_new(data: T) -> Result<Arc<T>, AllocError> {
583        // Start the weak pointer count as 1 which is the weak pointer that's
584        // held by all the strong pointers (kinda), see std/rc.rs for more info
585        let x: Box<_> = Box::try_new(ArcInner {
586            strong: atomic::AtomicUsize::new(1),
587            weak: atomic::AtomicUsize::new(1),
588            data,
589        })?;
590        unsafe { Ok(Self::from_inner(Box::leak(x).into())) }
591    }
592
593    /// Constructs a new `Arc` with uninitialized contents, returning an error
594    /// if allocation fails.
595    ///
596    /// # Examples
597    ///
598    /// ```
599    /// #![feature(allocator_api)]
600    ///
601    /// use std::sync::Arc;
602    ///
603    /// let mut five = Arc::<u32>::try_new_uninit()?;
604    ///
605    /// // Deferred initialization:
606    /// Arc::get_mut(&mut five).unwrap().write(5);
607    ///
608    /// let five = unsafe { five.assume_init() };
609    ///
610    /// assert_eq!(*five, 5);
611    /// # Ok::<(), std::alloc::AllocError>(())
612    /// ```
613    #[unstable(feature = "allocator_api", issue = "32838")]
614    pub fn try_new_uninit() -> Result<Arc<mem::MaybeUninit<T>>, AllocError> {
615        unsafe {
616            Ok(Arc::from_ptr(Arc::try_allocate_for_layout(
617                Layout::new::<T>(),
618                |layout| Global.allocate(layout),
619                <*mut u8>::cast,
620            )?))
621        }
622    }
623
624    /// Constructs a new `Arc` with uninitialized contents, with the memory
625    /// being filled with `0` bytes, returning an error if allocation fails.
626    ///
627    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
628    /// of this method.
629    ///
630    /// # Examples
631    ///
632    /// ```
633    /// #![feature( allocator_api)]
634    ///
635    /// use std::sync::Arc;
636    ///
637    /// let zero = Arc::<u32>::try_new_zeroed()?;
638    /// let zero = unsafe { zero.assume_init() };
639    ///
640    /// assert_eq!(*zero, 0);
641    /// # Ok::<(), std::alloc::AllocError>(())
642    /// ```
643    ///
644    /// [zeroed]: mem::MaybeUninit::zeroed
645    #[unstable(feature = "allocator_api", issue = "32838")]
646    pub fn try_new_zeroed() -> Result<Arc<mem::MaybeUninit<T>>, AllocError> {
647        unsafe {
648            Ok(Arc::from_ptr(Arc::try_allocate_for_layout(
649                Layout::new::<T>(),
650                |layout| Global.allocate_zeroed(layout),
651                <*mut u8>::cast,
652            )?))
653        }
654    }
655
656    /// Maps the value in an `Arc`, reusing the allocation if possible.
657    ///
658    /// `f` is called on a reference to the value in the `Arc`, and the result is returned, also in
659    /// an `Arc`.
660    ///
661    /// Note: this is an associated function, which means that you have
662    /// to call it as `Arc::map(a, f)` instead of `r.map(a)`. This
663    /// is so that there is no conflict with a method on the inner type.
664    ///
665    /// # Examples
666    ///
667    /// ```
668    /// #![feature(smart_pointer_try_map)]
669    ///
670    /// use std::sync::Arc;
671    ///
672    /// let r = Arc::new(7);
673    /// let new = Arc::map(r, |i| i + 7);
674    /// assert_eq!(*new, 14);
675    /// ```
676    #[cfg(not(no_global_oom_handling))]
677    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
678    pub fn map<U>(this: Self, f: impl FnOnce(&T) -> U) -> Arc<U> {
679        if size_of::<T>() == size_of::<U>()
680            && align_of::<T>() == align_of::<U>()
681            && Arc::is_unique(&this)
682        {
683            unsafe {
684                let ptr = Arc::into_raw(this);
685                let value = ptr.read();
686                let mut allocation = Arc::from_raw(ptr.cast::<mem::MaybeUninit<U>>());
687
688                Arc::get_mut_unchecked(&mut allocation).write(f(&value));
689                allocation.assume_init()
690            }
691        } else {
692            Arc::new(f(&*this))
693        }
694    }
695
696    /// Attempts to map the value in an `Arc`, reusing the allocation if possible.
697    ///
698    /// `f` is called on a reference to the value in the `Arc`, and if the operation succeeds, the
699    /// result is returned, also in an `Arc`.
700    ///
701    /// Note: this is an associated function, which means that you have
702    /// to call it as `Arc::try_map(a, f)` instead of `a.try_map(f)`. This
703    /// is so that there is no conflict with a method on the inner type.
704    ///
705    /// # Examples
706    ///
707    /// ```
708    /// #![feature(smart_pointer_try_map)]
709    ///
710    /// use std::sync::Arc;
711    ///
712    /// let b = Arc::new(7);
713    /// let new = Arc::try_map(b, |&i| u32::try_from(i)).unwrap();
714    /// assert_eq!(*new, 7);
715    /// ```
716    #[cfg(not(no_global_oom_handling))]
717    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
718    pub fn try_map<R>(
719        this: Self,
720        f: impl FnOnce(&T) -> R,
721    ) -> <R::Residual as Residual<Arc<R::Output>>>::TryType
722    where
723        R: Try,
724        R::Residual: Residual<Arc<R::Output>>,
725    {
726        if size_of::<T>() == size_of::<R::Output>()
727            && align_of::<T>() == align_of::<R::Output>()
728            && Arc::is_unique(&this)
729        {
730            unsafe {
731                let ptr = Arc::into_raw(this);
732                let value = ptr.read();
733                let mut allocation = Arc::from_raw(ptr.cast::<mem::MaybeUninit<R::Output>>());
734
735                Arc::get_mut_unchecked(&mut allocation).write(f(&value)?);
736                try { allocation.assume_init() }
737            }
738        } else {
739            try { Arc::new(f(&*this)?) }
740        }
741    }
742}
743
744impl<T, A: Allocator> Arc<T, A> {
745    /// Constructs a new `Arc<T>` in the provided allocator.
746    ///
747    /// # Examples
748    ///
749    /// ```
750    /// #![feature(allocator_api)]
751    ///
752    /// use std::sync::Arc;
753    /// use std::alloc::System;
754    ///
755    /// let five = Arc::new_in(5, System);
756    /// ```
757    #[inline]
758    #[cfg(not(no_global_oom_handling))]
759    #[unstable(feature = "allocator_api", issue = "32838")]
760    pub fn new_in(data: T, alloc: A) -> Arc<T, A> {
761        // Start the weak pointer count as 1 which is the weak pointer that's
762        // held by all the strong pointers (kinda), see std/rc.rs for more info
763        let x = Box::new_in(
764            ArcInner {
765                strong: atomic::AtomicUsize::new(1),
766                weak: atomic::AtomicUsize::new(1),
767                data,
768            },
769            alloc,
770        );
771        let (ptr, alloc) = Box::into_unique(x);
772        unsafe { Self::from_inner_in(ptr.into(), alloc) }
773    }
774
775    /// Constructs a new `Arc` with uninitialized contents in the provided allocator.
776    ///
777    /// # Examples
778    ///
779    /// ```
780    /// #![feature(get_mut_unchecked)]
781    /// #![feature(allocator_api)]
782    ///
783    /// use std::sync::Arc;
784    /// use std::alloc::System;
785    ///
786    /// let mut five = Arc::<u32, _>::new_uninit_in(System);
787    ///
788    /// let five = unsafe {
789    ///     // Deferred initialization:
790    ///     Arc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);
791    ///
792    ///     five.assume_init()
793    /// };
794    ///
795    /// assert_eq!(*five, 5)
796    /// ```
797    #[cfg(not(no_global_oom_handling))]
798    #[unstable(feature = "allocator_api", issue = "32838")]
799    #[inline]
800    pub fn new_uninit_in(alloc: A) -> Arc<mem::MaybeUninit<T>, A> {
801        unsafe {
802            Arc::from_ptr_in(
803                Arc::allocate_for_layout(
804                    Layout::new::<T>(),
805                    |layout| alloc.allocate(layout),
806                    <*mut u8>::cast,
807                ),
808                alloc,
809            )
810        }
811    }
812
813    /// Constructs a new `Arc` with uninitialized contents, with the memory
814    /// being filled with `0` bytes, in the provided allocator.
815    ///
816    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
817    /// of this method.
818    ///
819    /// # Examples
820    ///
821    /// ```
822    /// #![feature(allocator_api)]
823    ///
824    /// use std::sync::Arc;
825    /// use std::alloc::System;
826    ///
827    /// let zero = Arc::<u32, _>::new_zeroed_in(System);
828    /// let zero = unsafe { zero.assume_init() };
829    ///
830    /// assert_eq!(*zero, 0)
831    /// ```
832    ///
833    /// [zeroed]: mem::MaybeUninit::zeroed
834    #[cfg(not(no_global_oom_handling))]
835    #[unstable(feature = "allocator_api", issue = "32838")]
836    #[inline]
837    pub fn new_zeroed_in(alloc: A) -> Arc<mem::MaybeUninit<T>, A> {
838        unsafe {
839            Arc::from_ptr_in(
840                Arc::allocate_for_layout(
841                    Layout::new::<T>(),
842                    |layout| alloc.allocate_zeroed(layout),
843                    <*mut u8>::cast,
844                ),
845                alloc,
846            )
847        }
848    }
849
850    /// Constructs a new `Arc<T, A>` in the given allocator while giving you a `Weak<T, A>` to the allocation,
851    /// to allow you to construct a `T` which holds a weak pointer to itself.
852    ///
853    /// Generally, a structure circularly referencing itself, either directly or
854    /// indirectly, should not hold a strong reference to itself to prevent a memory leak.
855    /// Using this function, you get access to the weak pointer during the
856    /// initialization of `T`, before the `Arc<T, A>` is created, such that you can
857    /// clone and store it inside the `T`.
858    ///
859    /// `new_cyclic_in` first allocates the managed allocation for the `Arc<T, A>`,
860    /// then calls your closure, giving it a `Weak<T, A>` to this allocation,
861    /// and only afterwards completes the construction of the `Arc<T, A>` by placing
862    /// the `T` returned from your closure into the allocation.
863    ///
864    /// Since the new `Arc<T, A>` is not fully-constructed until `Arc<T, A>::new_cyclic_in`
865    /// returns, calling [`upgrade`] on the weak reference inside your closure will
866    /// fail and result in a `None` value.
867    ///
868    /// # Panics
869    ///
870    /// If `data_fn` panics, the panic is propagated to the caller, and the
871    /// temporary [`Weak<T>`] is dropped normally.
872    ///
873    /// # Example
874    ///
875    /// See [`new_cyclic`]
876    ///
877    /// [`new_cyclic`]: Arc::new_cyclic
878    /// [`upgrade`]: Weak::upgrade
879    #[cfg(not(no_global_oom_handling))]
880    #[inline]
881    #[unstable(feature = "allocator_api", issue = "32838")]
882    pub fn new_cyclic_in<F>(data_fn: F, alloc: A) -> Arc<T, A>
883    where
884        F: FnOnce(&Weak<T, A>) -> T,
885    {
886        // Construct the inner in the "uninitialized" state with a single
887        // weak reference.
888        let (uninit_raw_ptr, alloc) = Box::into_raw_with_allocator(Box::new_in(
889            ArcInner {
890                strong: atomic::AtomicUsize::new(0),
891                weak: atomic::AtomicUsize::new(1),
892                data: mem::MaybeUninit::<T>::uninit(),
893            },
894            alloc,
895        ));
896        let uninit_ptr: NonNull<_> = (unsafe { &mut *uninit_raw_ptr }).into();
897        let init_ptr: NonNull<ArcInner<T>> = uninit_ptr.cast();
898
899        let weak = Weak { ptr: init_ptr, alloc };
900
901        // It's important we don't give up ownership of the weak pointer, or
902        // else the memory might be freed by the time `data_fn` returns. If
903        // we really wanted to pass ownership, we could create an additional
904        // weak pointer for ourselves, but this would result in additional
905        // updates to the weak reference count which might not be necessary
906        // otherwise.
907        let data = data_fn(&weak);
908
909        // Now we can properly initialize the inner value and turn our weak
910        // reference into a strong reference.
911        let strong = unsafe {
912            let inner = init_ptr.as_ptr();
913            ptr::write(&raw mut (*inner).data, data);
914
915            // The above write to the data field must be visible to any threads which
916            // observe a non-zero strong count. Therefore we need at least "Release" ordering
917            // in order to synchronize with the `compare_exchange_weak` in `Weak::upgrade`.
918            //
919            // "Acquire" ordering is not required. When considering the possible behaviors
920            // of `data_fn` we only need to look at what it could do with a reference to a
921            // non-upgradeable `Weak`:
922            // - It can *clone* the `Weak`, increasing the weak reference count.
923            // - It can drop those clones, decreasing the weak reference count (but never to zero).
924            //
925            // These side effects do not impact us in any way, and no other side effects are
926            // possible with safe code alone.
927            let prev_value = (*inner).strong.fetch_add(1, Release);
928            debug_assert_eq!(prev_value, 0, "No prior strong references should exist");
929
930            // Strong references should collectively own a shared weak reference,
931            // so don't run the destructor for our old weak reference.
932            // Calling into_raw_with_allocator has the double effect of giving us back the allocator,
933            // and forgetting the weak reference.
934            let alloc = weak.into_raw_with_allocator().1;
935
936            Arc::from_inner_in(init_ptr, alloc)
937        };
938
939        strong
940    }
941
942    /// Constructs a new `Pin<Arc<T, A>>` in the provided allocator. If `T` does not implement `Unpin`,
943    /// then `data` will be pinned in memory and unable to be moved.
944    #[cfg(not(no_global_oom_handling))]
945    #[unstable(feature = "allocator_api", issue = "32838")]
946    #[inline]
947    pub fn pin_in(data: T, alloc: A) -> Pin<Arc<T, A>>
948    where
949        A: 'static,
950    {
951        unsafe { Pin::new_unchecked(Arc::new_in(data, alloc)) }
952    }
953
954    /// Constructs a new `Pin<Arc<T, A>>` in the provided allocator, return an error if allocation
955    /// fails.
956    #[inline]
957    #[unstable(feature = "allocator_api", issue = "32838")]
958    pub fn try_pin_in(data: T, alloc: A) -> Result<Pin<Arc<T, A>>, AllocError>
959    where
960        A: 'static,
961    {
962        unsafe { Ok(Pin::new_unchecked(Arc::try_new_in(data, alloc)?)) }
963    }
964
965    /// Constructs a new `Arc<T, A>` in the provided allocator, returning an error if allocation fails.
966    ///
967    /// # Examples
968    ///
969    /// ```
970    /// #![feature(allocator_api)]
971    ///
972    /// use std::sync::Arc;
973    /// use std::alloc::System;
974    ///
975    /// let five = Arc::try_new_in(5, System)?;
976    /// # Ok::<(), std::alloc::AllocError>(())
977    /// ```
978    #[unstable(feature = "allocator_api", issue = "32838")]
979    #[inline]
980    pub fn try_new_in(data: T, alloc: A) -> Result<Arc<T, A>, AllocError> {
981        // Start the weak pointer count as 1 which is the weak pointer that's
982        // held by all the strong pointers (kinda), see std/rc.rs for more info
983        let x = Box::try_new_in(
984            ArcInner {
985                strong: atomic::AtomicUsize::new(1),
986                weak: atomic::AtomicUsize::new(1),
987                data,
988            },
989            alloc,
990        )?;
991        let (ptr, alloc) = Box::into_unique(x);
992        Ok(unsafe { Self::from_inner_in(ptr.into(), alloc) })
993    }
994
995    /// Constructs a new `Arc` with uninitialized contents, in the provided allocator, returning an
996    /// error if allocation fails.
997    ///
998    /// # Examples
999    ///
1000    /// ```
1001    /// #![feature(allocator_api)]
1002    /// #![feature(get_mut_unchecked)]
1003    ///
1004    /// use std::sync::Arc;
1005    /// use std::alloc::System;
1006    ///
1007    /// let mut five = Arc::<u32, _>::try_new_uninit_in(System)?;
1008    ///
1009    /// let five = unsafe {
1010    ///     // Deferred initialization:
1011    ///     Arc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);
1012    ///
1013    ///     five.assume_init()
1014    /// };
1015    ///
1016    /// assert_eq!(*five, 5);
1017    /// # Ok::<(), std::alloc::AllocError>(())
1018    /// ```
1019    #[unstable(feature = "allocator_api", issue = "32838")]
1020    #[inline]
1021    pub fn try_new_uninit_in(alloc: A) -> Result<Arc<mem::MaybeUninit<T>, A>, AllocError> {
1022        unsafe {
1023            Ok(Arc::from_ptr_in(
1024                Arc::try_allocate_for_layout(
1025                    Layout::new::<T>(),
1026                    |layout| alloc.allocate(layout),
1027                    <*mut u8>::cast,
1028                )?,
1029                alloc,
1030            ))
1031        }
1032    }
1033
1034    /// Constructs a new `Arc` with uninitialized contents, with the memory
1035    /// being filled with `0` bytes, in the provided allocator, returning an error if allocation
1036    /// fails.
1037    ///
1038    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and incorrect usage
1039    /// of this method.
1040    ///
1041    /// # Examples
1042    ///
1043    /// ```
1044    /// #![feature(allocator_api)]
1045    ///
1046    /// use std::sync::Arc;
1047    /// use std::alloc::System;
1048    ///
1049    /// let zero = Arc::<u32, _>::try_new_zeroed_in(System)?;
1050    /// let zero = unsafe { zero.assume_init() };
1051    ///
1052    /// assert_eq!(*zero, 0);
1053    /// # Ok::<(), std::alloc::AllocError>(())
1054    /// ```
1055    ///
1056    /// [zeroed]: mem::MaybeUninit::zeroed
1057    #[unstable(feature = "allocator_api", issue = "32838")]
1058    #[inline]
1059    pub fn try_new_zeroed_in(alloc: A) -> Result<Arc<mem::MaybeUninit<T>, A>, AllocError> {
1060        unsafe {
1061            Ok(Arc::from_ptr_in(
1062                Arc::try_allocate_for_layout(
1063                    Layout::new::<T>(),
1064                    |layout| alloc.allocate_zeroed(layout),
1065                    <*mut u8>::cast,
1066                )?,
1067                alloc,
1068            ))
1069        }
1070    }
1071    /// Returns the inner value, if the `Arc` has exactly one strong reference.
1072    ///
1073    /// Otherwise, an [`Err`] is returned with the same `Arc` that was
1074    /// passed in.
1075    ///
1076    /// This will succeed even if there are outstanding weak references.
1077    ///
1078    /// It is strongly recommended to use [`Arc::into_inner`] instead if you don't
1079    /// keep the `Arc` in the [`Err`] case.
1080    /// Immediately dropping the [`Err`]-value, as the expression
1081    /// `Arc::try_unwrap(this).ok()` does, can cause the strong count to
1082    /// drop to zero and the inner value of the `Arc` to be dropped.
1083    /// For instance, if two threads execute such an expression in parallel,
1084    /// there is a race condition without the possibility of unsafety:
1085    /// The threads could first both check whether they own the last instance
1086    /// in `Arc::try_unwrap`, determine that they both do not, and then both
1087    /// discard and drop their instance in the call to [`ok`][`Result::ok`].
1088    /// In this scenario, the value inside the `Arc` is safely destroyed
1089    /// by exactly one of the threads, but neither thread will ever be able
1090    /// to use the value.
1091    ///
1092    /// # Examples
1093    ///
1094    /// ```
1095    /// use std::sync::Arc;
1096    ///
1097    /// let x = Arc::new(3);
1098    /// assert_eq!(Arc::try_unwrap(x), Ok(3));
1099    ///
1100    /// let x = Arc::new(4);
1101    /// let _y = Arc::clone(&x);
1102    /// assert_eq!(*Arc::try_unwrap(x).unwrap_err(), 4);
1103    /// ```
1104    #[inline]
1105    #[stable(feature = "arc_unique", since = "1.4.0")]
1106    pub fn try_unwrap(this: Self) -> Result<T, Self> {
1107        if this.inner().strong.compare_exchange(1, 0, Relaxed, Relaxed).is_err() {
1108            return Err(this);
1109        }
1110
1111        acquire!(this.inner().strong);
1112
1113        let this = ManuallyDrop::new(this);
1114        let elem: T = unsafe { ptr::read(&this.ptr.as_ref().data) };
1115        let alloc: A = unsafe { ptr::read(&this.alloc) }; // copy the allocator
1116
1117        // Make a weak pointer to clean up the implicit strong-weak reference
1118        let _weak = Weak { ptr: this.ptr, alloc };
1119
1120        Ok(elem)
1121    }
1122
1123    /// Returns the inner value, if the `Arc` has exactly one strong reference.
1124    ///
1125    /// Otherwise, [`None`] is returned and the `Arc` is dropped.
1126    ///
1127    /// This will succeed even if there are outstanding weak references.
1128    ///
1129    /// If `Arc::into_inner` is called on every clone of this `Arc`,
1130    /// it is guaranteed that exactly one of the calls returns the inner value.
1131    /// This means in particular that the inner value is not dropped.
1132    ///
1133    /// [`Arc::try_unwrap`] is conceptually similar to `Arc::into_inner`, but it
1134    /// is meant for different use-cases. If used as a direct replacement
1135    /// for `Arc::into_inner` anyway, such as with the expression
1136    /// <code>[Arc::try_unwrap]\(this).[ok][Result::ok]()</code>, then it does
1137    /// **not** give the same guarantee as described in the previous paragraph.
1138    /// For more information, see the examples below and read the documentation
1139    /// of [`Arc::try_unwrap`].
1140    ///
1141    /// # Examples
1142    ///
1143    /// Minimal example demonstrating the guarantee that `Arc::into_inner` gives.
1144    /// ```
1145    /// use std::sync::Arc;
1146    ///
1147    /// let x = Arc::new(3);
1148    /// let y = Arc::clone(&x);
1149    ///
1150    /// // Two threads calling `Arc::into_inner` on both clones of an `Arc`:
1151    /// let x_thread = std::thread::spawn(|| Arc::into_inner(x));
1152    /// let y_thread = std::thread::spawn(|| Arc::into_inner(y));
1153    ///
1154    /// let x_inner_value = x_thread.join().unwrap();
1155    /// let y_inner_value = y_thread.join().unwrap();
1156    ///
1157    /// // One of the threads is guaranteed to receive the inner value:
1158    /// assert!(matches!(
1159    ///     (x_inner_value, y_inner_value),
1160    ///     (None, Some(3)) | (Some(3), None)
1161    /// ));
1162    /// // The result could also be `(None, None)` if the threads called
1163    /// // `Arc::try_unwrap(x).ok()` and `Arc::try_unwrap(y).ok()` instead.
1164    /// ```
1165    ///
1166    /// A more practical example demonstrating the need for `Arc::into_inner`:
1167    /// ```
1168    /// use std::sync::Arc;
1169    ///
1170    /// // Definition of a simple singly linked list using `Arc`:
1171    /// #[derive(Clone)]
1172    /// struct LinkedList<T>(Option<Arc<Node<T>>>);
1173    /// struct Node<T>(T, Option<Arc<Node<T>>>);
1174    ///
1175    /// // Dropping a long `LinkedList<T>` relying on the destructor of `Arc`
1176    /// // can cause a stack overflow. To prevent this, we can provide a
1177    /// // manual `Drop` implementation that does the destruction in a loop:
1178    /// impl<T> Drop for LinkedList<T> {
1179    ///     fn drop(&mut self) {
1180    ///         let mut link = self.0.take();
1181    ///         while let Some(arc_node) = link.take() {
1182    ///             if let Some(Node(_value, next)) = Arc::into_inner(arc_node) {
1183    ///                 link = next;
1184    ///             }
1185    ///         }
1186    ///     }
1187    /// }
1188    ///
1189    /// // Implementation of `new` and `push` omitted
1190    /// impl<T> LinkedList<T> {
1191    ///     /* ... */
1192    /// #   fn new() -> Self {
1193    /// #       LinkedList(None)
1194    /// #   }
1195    /// #   fn push(&mut self, x: T) {
1196    /// #       self.0 = Some(Arc::new(Node(x, self.0.take())));
1197    /// #   }
1198    /// }
1199    ///
1200    /// // The following code could have still caused a stack overflow
1201    /// // despite the manual `Drop` impl if that `Drop` impl had used
1202    /// // `Arc::try_unwrap(arc).ok()` instead of `Arc::into_inner(arc)`.
1203    ///
1204    /// // Create a long list and clone it
1205    /// let mut x = LinkedList::new();
1206    /// let size = 100000;
1207    /// # let size = if cfg!(miri) { 100 } else { size };
1208    /// for i in 0..size {
1209    ///     x.push(i); // Adds i to the front of x
1210    /// }
1211    /// let y = x.clone();
1212    ///
1213    /// // Drop the clones in parallel
1214    /// let x_thread = std::thread::spawn(|| drop(x));
1215    /// let y_thread = std::thread::spawn(|| drop(y));
1216    /// x_thread.join().unwrap();
1217    /// y_thread.join().unwrap();
1218    /// ```
1219    #[inline]
1220    #[stable(feature = "arc_into_inner", since = "1.70.0")]
1221    pub fn into_inner(this: Self) -> Option<T> {
1222        // Make sure that the ordinary `Drop` implementation isn’t called as well
1223        let mut this = mem::ManuallyDrop::new(this);
1224
1225        // Following the implementation of `drop` and `drop_slow`
1226        if this.inner().strong.fetch_sub(1, Release) != 1 {
1227            return None;
1228        }
1229
1230        acquire!(this.inner().strong);
1231
1232        // SAFETY: This mirrors the line
1233        //
1234        //     unsafe { ptr::drop_in_place(Self::get_mut_unchecked(self)) };
1235        //
1236        // in `drop_slow`. Instead of dropping the value behind the pointer,
1237        // it is read and eventually returned; `ptr::read` has the same
1238        // safety conditions as `ptr::drop_in_place`.
1239
1240        let inner = unsafe { ptr::read(Self::get_mut_unchecked(&mut this)) };
1241        let alloc = unsafe { ptr::read(&this.alloc) };
1242
1243        drop(Weak { ptr: this.ptr, alloc });
1244
1245        Some(inner)
1246    }
1247}
1248
1249impl<T> Arc<[T]> {
1250    /// Constructs a new atomically reference-counted slice with uninitialized contents.
1251    ///
1252    /// # Examples
1253    ///
1254    /// ```
1255    /// use std::sync::Arc;
1256    ///
1257    /// let mut values = Arc::<[u32]>::new_uninit_slice(3);
1258    ///
1259    /// // Deferred initialization:
1260    /// let data = Arc::get_mut(&mut values).unwrap();
1261    /// data[0].write(1);
1262    /// data[1].write(2);
1263    /// data[2].write(3);
1264    ///
1265    /// let values = unsafe { values.assume_init() };
1266    ///
1267    /// assert_eq!(*values, [1, 2, 3])
1268    /// ```
1269    #[cfg(not(no_global_oom_handling))]
1270    #[inline]
1271    #[stable(feature = "new_uninit", since = "1.82.0")]
1272    #[must_use]
1273    pub fn new_uninit_slice(len: usize) -> Arc<[mem::MaybeUninit<T>]> {
1274        unsafe { Arc::from_ptr(Arc::allocate_for_slice(len)) }
1275    }
1276
1277    /// Constructs a new atomically reference-counted slice with uninitialized contents, with the memory being
1278    /// filled with `0` bytes.
1279    ///
1280    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
1281    /// incorrect usage of this method.
1282    ///
1283    /// # Examples
1284    ///
1285    /// ```
1286    /// use std::sync::Arc;
1287    ///
1288    /// let values = Arc::<[u32]>::new_zeroed_slice(3);
1289    /// let values = unsafe { values.assume_init() };
1290    ///
1291    /// assert_eq!(*values, [0, 0, 0])
1292    /// ```
1293    ///
1294    /// [zeroed]: mem::MaybeUninit::zeroed
1295    #[cfg(not(no_global_oom_handling))]
1296    #[inline]
1297    #[stable(feature = "new_zeroed_alloc", since = "1.92.0")]
1298    #[must_use]
1299    pub fn new_zeroed_slice(len: usize) -> Arc<[mem::MaybeUninit<T>]> {
1300        unsafe {
1301            Arc::from_ptr(Arc::allocate_for_layout(
1302                Layout::array::<T>(len).unwrap(),
1303                |layout| Global.allocate_zeroed(layout),
1304                |mem| {
1305                    ptr::slice_from_raw_parts_mut(mem as *mut T, len)
1306                        as *mut ArcInner<[mem::MaybeUninit<T>]>
1307                },
1308            ))
1309        }
1310    }
1311
1312    /// Converts the reference-counted slice into a reference-counted array.
1313    ///
1314    /// This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.
1315    ///
1316    /// If `N` is not exactly equal to the length of `self`, then this method returns `None`.
1317    #[unstable(feature = "alloc_slice_into_array", issue = "148082")]
1318    #[inline]
1319    #[must_use]
1320    pub fn into_array<const N: usize>(self) -> Option<Arc<[T; N]>> {
1321        if self.len() == N {
1322            let ptr = Self::into_raw(self) as *const [T; N];
1323
1324            // SAFETY: The underlying array of a slice has the exact same layout as an actual array `[T; N]` if `N` is equal to the slice's length.
1325            let me = unsafe { Arc::from_raw(ptr) };
1326            Some(me)
1327        } else {
1328            None
1329        }
1330    }
1331}
1332
1333impl<T, A: Allocator> Arc<[T], A> {
1334    /// Constructs a new atomically reference-counted slice with uninitialized contents in the
1335    /// provided allocator.
1336    ///
1337    /// # Examples
1338    ///
1339    /// ```
1340    /// #![feature(get_mut_unchecked)]
1341    /// #![feature(allocator_api)]
1342    ///
1343    /// use std::sync::Arc;
1344    /// use std::alloc::System;
1345    ///
1346    /// let mut values = Arc::<[u32], _>::new_uninit_slice_in(3, System);
1347    ///
1348    /// let values = unsafe {
1349    ///     // Deferred initialization:
1350    ///     Arc::get_mut_unchecked(&mut values)[0].as_mut_ptr().write(1);
1351    ///     Arc::get_mut_unchecked(&mut values)[1].as_mut_ptr().write(2);
1352    ///     Arc::get_mut_unchecked(&mut values)[2].as_mut_ptr().write(3);
1353    ///
1354    ///     values.assume_init()
1355    /// };
1356    ///
1357    /// assert_eq!(*values, [1, 2, 3])
1358    /// ```
1359    #[cfg(not(no_global_oom_handling))]
1360    #[unstable(feature = "allocator_api", issue = "32838")]
1361    #[inline]
1362    pub fn new_uninit_slice_in(len: usize, alloc: A) -> Arc<[mem::MaybeUninit<T>], A> {
1363        unsafe { Arc::from_ptr_in(Arc::allocate_for_slice_in(len, &alloc), alloc) }
1364    }
1365
1366    /// Constructs a new atomically reference-counted slice with uninitialized contents, with the memory being
1367    /// filled with `0` bytes, in the provided allocator.
1368    ///
1369    /// See [`MaybeUninit::zeroed`][zeroed] for examples of correct and
1370    /// incorrect usage of this method.
1371    ///
1372    /// # Examples
1373    ///
1374    /// ```
1375    /// #![feature(allocator_api)]
1376    ///
1377    /// use std::sync::Arc;
1378    /// use std::alloc::System;
1379    ///
1380    /// let values = Arc::<[u32], _>::new_zeroed_slice_in(3, System);
1381    /// let values = unsafe { values.assume_init() };
1382    ///
1383    /// assert_eq!(*values, [0, 0, 0])
1384    /// ```
1385    ///
1386    /// [zeroed]: mem::MaybeUninit::zeroed
1387    #[cfg(not(no_global_oom_handling))]
1388    #[unstable(feature = "allocator_api", issue = "32838")]
1389    #[inline]
1390    pub fn new_zeroed_slice_in(len: usize, alloc: A) -> Arc<[mem::MaybeUninit<T>], A> {
1391        unsafe {
1392            Arc::from_ptr_in(
1393                Arc::allocate_for_layout(
1394                    Layout::array::<T>(len).unwrap(),
1395                    |layout| alloc.allocate_zeroed(layout),
1396                    |mem| {
1397                        ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len)
1398                            as *mut ArcInner<[mem::MaybeUninit<T>]>
1399                    },
1400                ),
1401                alloc,
1402            )
1403        }
1404    }
1405}
1406
1407impl<T, A: Allocator> Arc<mem::MaybeUninit<T>, A> {
1408    /// Converts to `Arc<T>`.
1409    ///
1410    /// # Safety
1411    ///
1412    /// As with [`MaybeUninit::assume_init`],
1413    /// it is up to the caller to guarantee that the inner value
1414    /// really is in an initialized state.
1415    /// Calling this when the content is not yet fully initialized
1416    /// causes immediate undefined behavior.
1417    ///
1418    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1419    ///
1420    /// # Examples
1421    ///
1422    /// ```
1423    /// use std::sync::Arc;
1424    ///
1425    /// let mut five = Arc::<u32>::new_uninit();
1426    ///
1427    /// // Deferred initialization:
1428    /// Arc::get_mut(&mut five).unwrap().write(5);
1429    ///
1430    /// let five = unsafe { five.assume_init() };
1431    ///
1432    /// assert_eq!(*five, 5)
1433    /// ```
1434    #[stable(feature = "new_uninit", since = "1.82.0")]
1435    #[must_use = "`self` will be dropped if the result is not used"]
1436    #[inline]
1437    pub unsafe fn assume_init(self) -> Arc<T, A> {
1438        let (ptr, alloc) = Arc::into_inner_with_allocator(self);
1439        unsafe { Arc::from_inner_in(ptr.cast(), alloc) }
1440    }
1441}
1442
1443impl<T: ?Sized + CloneToUninit> Arc<T> {
1444    /// Constructs a new `Arc<T>` with a clone of `value`.
1445    ///
1446    /// # Examples
1447    ///
1448    /// ```
1449    /// #![feature(clone_from_ref)]
1450    /// use std::sync::Arc;
1451    ///
1452    /// let hello: Arc<str> = Arc::clone_from_ref("hello");
1453    /// ```
1454    #[cfg(not(no_global_oom_handling))]
1455    #[unstable(feature = "clone_from_ref", issue = "149075")]
1456    pub fn clone_from_ref(value: &T) -> Arc<T> {
1457        Arc::clone_from_ref_in(value, Global)
1458    }
1459
1460    /// Constructs a new `Arc<T>` with a clone of `value`, returning an error if allocation fails
1461    ///
1462    /// # Examples
1463    ///
1464    /// ```
1465    /// #![feature(clone_from_ref)]
1466    /// #![feature(allocator_api)]
1467    /// use std::sync::Arc;
1468    ///
1469    /// let hello: Arc<str> = Arc::try_clone_from_ref("hello")?;
1470    /// # Ok::<(), std::alloc::AllocError>(())
1471    /// ```
1472    #[unstable(feature = "clone_from_ref", issue = "149075")]
1473    //#[unstable(feature = "allocator_api", issue = "32838")]
1474    pub fn try_clone_from_ref(value: &T) -> Result<Arc<T>, AllocError> {
1475        Arc::try_clone_from_ref_in(value, Global)
1476    }
1477}
1478
1479impl<T: ?Sized + CloneToUninit, A: Allocator> Arc<T, A> {
1480    /// Constructs a new `Arc<T>` with a clone of `value` in the provided allocator.
1481    ///
1482    /// # Examples
1483    ///
1484    /// ```
1485    /// #![feature(clone_from_ref)]
1486    /// #![feature(allocator_api)]
1487    /// use std::sync::Arc;
1488    /// use std::alloc::System;
1489    ///
1490    /// let hello: Arc<str, System> = Arc::clone_from_ref_in("hello", System);
1491    /// ```
1492    #[cfg(not(no_global_oom_handling))]
1493    #[unstable(feature = "clone_from_ref", issue = "149075")]
1494    //#[unstable(feature = "allocator_api", issue = "32838")]
1495    pub fn clone_from_ref_in(value: &T, alloc: A) -> Arc<T, A> {
1496        // `in_progress` drops the allocation if we panic before finishing initializing it.
1497        let mut in_progress: UniqueArcUninit<T, A> = UniqueArcUninit::new(value, alloc);
1498
1499        // Initialize with clone of value.
1500        let initialized_clone = unsafe {
1501            // Clone. If the clone panics, `in_progress` will be dropped and clean up.
1502            value.clone_to_uninit(in_progress.data_ptr().cast());
1503            // Cast type of pointer, now that it is initialized.
1504            in_progress.into_arc()
1505        };
1506
1507        initialized_clone
1508    }
1509
1510    /// Constructs a new `Arc<T>` with a clone of `value` in the provided allocator, returning an error if allocation fails
1511    ///
1512    /// # Examples
1513    ///
1514    /// ```
1515    /// #![feature(clone_from_ref)]
1516    /// #![feature(allocator_api)]
1517    /// use std::sync::Arc;
1518    /// use std::alloc::System;
1519    ///
1520    /// let hello: Arc<str, System> = Arc::try_clone_from_ref_in("hello", System)?;
1521    /// # Ok::<(), std::alloc::AllocError>(())
1522    /// ```
1523    #[unstable(feature = "clone_from_ref", issue = "149075")]
1524    //#[unstable(feature = "allocator_api", issue = "32838")]
1525    pub fn try_clone_from_ref_in(value: &T, alloc: A) -> Result<Arc<T, A>, AllocError> {
1526        // `in_progress` drops the allocation if we panic before finishing initializing it.
1527        let mut in_progress: UniqueArcUninit<T, A> = UniqueArcUninit::try_new(value, alloc)?;
1528
1529        // Initialize with clone of value.
1530        let initialized_clone = unsafe {
1531            // Clone. If the clone panics, `in_progress` will be dropped and clean up.
1532            value.clone_to_uninit(in_progress.data_ptr().cast());
1533            // Cast type of pointer, now that it is initialized.
1534            in_progress.into_arc()
1535        };
1536
1537        Ok(initialized_clone)
1538    }
1539}
1540
1541impl<T, A: Allocator> Arc<[mem::MaybeUninit<T>], A> {
1542    /// Converts to `Arc<[T]>`.
1543    ///
1544    /// # Safety
1545    ///
1546    /// As with [`MaybeUninit::assume_init`],
1547    /// it is up to the caller to guarantee that the inner value
1548    /// really is in an initialized state.
1549    /// Calling this when the content is not yet fully initialized
1550    /// causes immediate undefined behavior.
1551    ///
1552    /// [`MaybeUninit::assume_init`]: mem::MaybeUninit::assume_init
1553    ///
1554    /// # Examples
1555    ///
1556    /// ```
1557    /// use std::sync::Arc;
1558    ///
1559    /// let mut values = Arc::<[u32]>::new_uninit_slice(3);
1560    ///
1561    /// // Deferred initialization:
1562    /// let data = Arc::get_mut(&mut values).unwrap();
1563    /// data[0].write(1);
1564    /// data[1].write(2);
1565    /// data[2].write(3);
1566    ///
1567    /// let values = unsafe { values.assume_init() };
1568    ///
1569    /// assert_eq!(*values, [1, 2, 3])
1570    /// ```
1571    #[stable(feature = "new_uninit", since = "1.82.0")]
1572    #[must_use = "`self` will be dropped if the result is not used"]
1573    #[inline]
1574    pub unsafe fn assume_init(self) -> Arc<[T], A> {
1575        let (ptr, alloc) = Arc::into_inner_with_allocator(self);
1576        unsafe { Arc::from_ptr_in(ptr.as_ptr() as _, alloc) }
1577    }
1578}
1579
1580impl<T: ?Sized> Arc<T> {
1581    /// Constructs an `Arc<T>` from a raw pointer.
1582    ///
1583    /// The raw pointer must have been previously returned by a call to
1584    /// [`Arc<U>::into_raw`][into_raw] with the following requirements:
1585    ///
1586    /// * If `U` is sized, it must have the same size and alignment as `T`. This
1587    ///   is trivially true if `U` is `T`.
1588    /// * If `U` is unsized, its data pointer must have the same size and
1589    ///   alignment as `T`. This is trivially true if `Arc<U>` was constructed
1590    ///   through `Arc<T>` and then converted to `Arc<U>` through an [unsized
1591    ///   coercion].
1592    ///
1593    /// Note that if `U` or `U`'s data pointer is not `T` but has the same size
1594    /// and alignment, this is basically like transmuting references of
1595    /// different types. See [`mem::transmute`][transmute] for more information
1596    /// on what restrictions apply in this case.
1597    ///
1598    /// The raw pointer must point to a block of memory allocated by the global allocator.
1599    ///
1600    /// The user of `from_raw` has to make sure a specific value of `T` is only
1601    /// dropped once.
1602    ///
1603    /// This function is unsafe because improper use may lead to memory unsafety,
1604    /// even if the returned `Arc<T>` is never accessed.
1605    ///
1606    /// [into_raw]: Arc::into_raw
1607    /// [transmute]: core::mem::transmute
1608    /// [unsized coercion]: https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions
1609    ///
1610    /// # Examples
1611    ///
1612    /// ```
1613    /// use std::sync::Arc;
1614    ///
1615    /// let x = Arc::new("hello".to_owned());
1616    /// let x_ptr = Arc::into_raw(x);
1617    ///
1618    /// unsafe {
1619    ///     // Convert back to an `Arc` to prevent leak.
1620    ///     let x = Arc::from_raw(x_ptr);
1621    ///     assert_eq!(&*x, "hello");
1622    ///
1623    ///     // Further calls to `Arc::from_raw(x_ptr)` would be memory-unsafe.
1624    /// }
1625    ///
1626    /// // The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
1627    /// ```
1628    ///
1629    /// Convert a slice back into its original array:
1630    ///
1631    /// ```
1632    /// use std::sync::Arc;
1633    ///
1634    /// let x: Arc<[u32]> = Arc::new([1, 2, 3]);
1635    /// let x_ptr: *const [u32] = Arc::into_raw(x);
1636    ///
1637    /// unsafe {
1638    ///     let x: Arc<[u32; 3]> = Arc::from_raw(x_ptr.cast::<[u32; 3]>());
1639    ///     assert_eq!(&*x, &[1, 2, 3]);
1640    /// }
1641    /// ```
1642    #[inline]
1643    #[stable(feature = "rc_raw", since = "1.17.0")]
1644    pub unsafe fn from_raw(ptr: *const T) -> Self {
1645        unsafe { Arc::from_raw_in(ptr, Global) }
1646    }
1647
1648    /// Consumes the `Arc`, returning the wrapped pointer.
1649    ///
1650    /// To avoid a memory leak the pointer must be converted back to an `Arc` using
1651    /// [`Arc::from_raw`].
1652    ///
1653    /// # Examples
1654    ///
1655    /// ```
1656    /// use std::sync::Arc;
1657    ///
1658    /// let x = Arc::new("hello".to_owned());
1659    /// let x_ptr = Arc::into_raw(x);
1660    /// assert_eq!(unsafe { &*x_ptr }, "hello");
1661    /// # // Prevent leaks for Miri.
1662    /// # drop(unsafe { Arc::from_raw(x_ptr) });
1663    /// ```
1664    #[must_use = "losing the pointer will leak memory"]
1665    #[stable(feature = "rc_raw", since = "1.17.0")]
1666    #[rustc_never_returns_null_ptr]
1667    pub fn into_raw(this: Self) -> *const T {
1668        let this = ManuallyDrop::new(this);
1669        Self::as_ptr(&*this)
1670    }
1671
1672    /// Increments the strong reference count on the `Arc<T>` associated with the
1673    /// provided pointer by one.
1674    ///
1675    /// # Safety
1676    ///
1677    /// The pointer must have been obtained through `Arc::into_raw` and must satisfy the
1678    /// same layout requirements specified in [`Arc::from_raw_in`][from_raw_in].
1679    /// The associated `Arc` instance must be valid (i.e. the strong count must be at
1680    /// least 1) for the duration of this method, and `ptr` must point to a block of memory
1681    /// allocated by the global allocator.
1682    ///
1683    /// [from_raw_in]: Arc::from_raw_in
1684    ///
1685    /// # Examples
1686    ///
1687    /// ```
1688    /// use std::sync::Arc;
1689    ///
1690    /// let five = Arc::new(5);
1691    ///
1692    /// unsafe {
1693    ///     let ptr = Arc::into_raw(five);
1694    ///     Arc::increment_strong_count(ptr);
1695    ///
1696    ///     // This assertion is deterministic because we haven't shared
1697    ///     // the `Arc` between threads.
1698    ///     let five = Arc::from_raw(ptr);
1699    ///     assert_eq!(2, Arc::strong_count(&five));
1700    /// #   // Prevent leaks for Miri.
1701    /// #   Arc::decrement_strong_count(ptr);
1702    /// }
1703    /// ```
1704    #[inline]
1705    #[stable(feature = "arc_mutate_strong_count", since = "1.51.0")]
1706    pub unsafe fn increment_strong_count(ptr: *const T) {
1707        unsafe { Arc::increment_strong_count_in(ptr, Global) }
1708    }
1709
1710    /// Decrements the strong reference count on the `Arc<T>` associated with the
1711    /// provided pointer by one.
1712    ///
1713    /// # Safety
1714    ///
1715    /// The pointer must have been obtained through `Arc::into_raw` and must satisfy the
1716    /// same layout requirements specified in [`Arc::from_raw_in`][from_raw_in].
1717    /// The associated `Arc` instance must be valid (i.e. the strong count must be at
1718    /// least 1) when invoking this method, and `ptr` must point to a block of memory
1719    /// allocated by the global allocator. This method can be used to release the final
1720    /// `Arc` and backing storage, but **should not** be called after the final `Arc` has been
1721    /// released.
1722    ///
1723    /// [from_raw_in]: Arc::from_raw_in
1724    ///
1725    /// # Examples
1726    ///
1727    /// ```
1728    /// use std::sync::Arc;
1729    ///
1730    /// let five = Arc::new(5);
1731    ///
1732    /// unsafe {
1733    ///     let ptr = Arc::into_raw(five);
1734    ///     Arc::increment_strong_count(ptr);
1735    ///
1736    ///     // Those assertions are deterministic because we haven't shared
1737    ///     // the `Arc` between threads.
1738    ///     let five = Arc::from_raw(ptr);
1739    ///     assert_eq!(2, Arc::strong_count(&five));
1740    ///     Arc::decrement_strong_count(ptr);
1741    ///     assert_eq!(1, Arc::strong_count(&five));
1742    /// }
1743    /// ```
1744    #[inline]
1745    #[stable(feature = "arc_mutate_strong_count", since = "1.51.0")]
1746    pub unsafe fn decrement_strong_count(ptr: *const T) {
1747        unsafe { Arc::decrement_strong_count_in(ptr, Global) }
1748    }
1749}
1750
1751impl<T: ?Sized, A: Allocator> Arc<T, A> {
1752    /// Returns a reference to the underlying allocator.
1753    ///
1754    /// Note: this is an associated function, which means that you have
1755    /// to call it as `Arc::allocator(&a)` instead of `a.allocator()`. This
1756    /// is so that there is no conflict with a method on the inner type.
1757    #[inline]
1758    #[unstable(feature = "allocator_api", issue = "32838")]
1759    pub fn allocator(this: &Self) -> &A {
1760        &this.alloc
1761    }
1762
1763    /// Consumes the `Arc`, returning the wrapped pointer and allocator.
1764    ///
1765    /// To avoid a memory leak the pointer must be converted back to an `Arc` using
1766    /// [`Arc::from_raw_in`].
1767    ///
1768    /// # Examples
1769    ///
1770    /// ```
1771    /// #![feature(allocator_api)]
1772    /// use std::sync::Arc;
1773    /// use std::alloc::System;
1774    ///
1775    /// let x = Arc::new_in("hello".to_owned(), System);
1776    /// let (ptr, alloc) = Arc::into_raw_with_allocator(x);
1777    /// assert_eq!(unsafe { &*ptr }, "hello");
1778    /// let x = unsafe { Arc::from_raw_in(ptr, alloc) };
1779    /// assert_eq!(&*x, "hello");
1780    /// ```
1781    #[must_use = "losing the pointer will leak memory"]
1782    #[unstable(feature = "allocator_api", issue = "32838")]
1783    pub fn into_raw_with_allocator(this: Self) -> (*const T, A) {
1784        let this = mem::ManuallyDrop::new(this);
1785        let ptr = Self::as_ptr(&this);
1786        // Safety: `this` is ManuallyDrop so the allocator will not be double-dropped
1787        let alloc = unsafe { ptr::read(&this.alloc) };
1788        (ptr, alloc)
1789    }
1790
1791    /// Provides a raw pointer to the data.
1792    ///
1793    /// The counts are not affected in any way and the `Arc` is not consumed. The pointer is valid for
1794    /// as long as there are strong counts in the `Arc`.
1795    ///
1796    /// # Examples
1797    ///
1798    /// ```
1799    /// use std::sync::Arc;
1800    ///
1801    /// let x = Arc::new("hello".to_owned());
1802    /// let y = Arc::clone(&x);
1803    /// let x_ptr = Arc::as_ptr(&x);
1804    /// assert_eq!(x_ptr, Arc::as_ptr(&y));
1805    /// assert_eq!(unsafe { &*x_ptr }, "hello");
1806    /// ```
1807    #[must_use]
1808    #[stable(feature = "rc_as_ptr", since = "1.45.0")]
1809    #[rustc_never_returns_null_ptr]
1810    pub fn as_ptr(this: &Self) -> *const T {
1811        let ptr: *mut ArcInner<T> = NonNull::as_ptr(this.ptr);
1812
1813        // SAFETY: This cannot go through Deref::deref or ArcInnerPtr::inner because
1814        // this is required to retain raw/mut provenance such that e.g. `get_mut` can
1815        // write through the pointer after the Arc is recovered through `from_raw`.
1816        unsafe { &raw mut (*ptr).data }
1817    }
1818
1819    /// Constructs an `Arc<T, A>` from a raw pointer.
1820    ///
1821    /// The raw pointer must have been previously returned by a call to [`Arc<U,
1822    /// A>::into_raw`][into_raw] with the following requirements:
1823    ///
1824    /// * If `U` is sized, it must have the same size and alignment as `T`. This
1825    ///   is trivially true if `U` is `T`.
1826    /// * If `U` is unsized, its data pointer must have the same size and
1827    ///   alignment as `T`. This is trivially true if `Arc<U>` was constructed
1828    ///   through `Arc<T>` and then converted to `Arc<U>` through an [unsized
1829    ///   coercion].
1830    ///
1831    /// Note that if `U` or `U`'s data pointer is not `T` but has the same size
1832    /// and alignment, this is basically like transmuting references of
1833    /// different types. See [`mem::transmute`][transmute] for more information
1834    /// on what restrictions apply in this case.
1835    ///
1836    /// The raw pointer must point to a block of memory allocated by `alloc`
1837    ///
1838    /// The user of `from_raw` has to make sure a specific value of `T` is only
1839    /// dropped once.
1840    ///
1841    /// This function is unsafe because improper use may lead to memory unsafety,
1842    /// even if the returned `Arc<T>` is never accessed.
1843    ///
1844    /// [into_raw]: Arc::into_raw
1845    /// [transmute]: core::mem::transmute
1846    /// [unsized coercion]: https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions
1847    ///
1848    /// # Examples
1849    ///
1850    /// ```
1851    /// #![feature(allocator_api)]
1852    ///
1853    /// use std::sync::Arc;
1854    /// use std::alloc::System;
1855    ///
1856    /// let x = Arc::new_in("hello".to_owned(), System);
1857    /// let (x_ptr, alloc) = Arc::into_raw_with_allocator(x);
1858    ///
1859    /// unsafe {
1860    ///     // Convert back to an `Arc` to prevent leak.
1861    ///     let x = Arc::from_raw_in(x_ptr, System);
1862    ///     assert_eq!(&*x, "hello");
1863    ///
1864    ///     // Further calls to `Arc::from_raw(x_ptr)` would be memory-unsafe.
1865    /// }
1866    ///
1867    /// // The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
1868    /// ```
1869    ///
1870    /// Convert a slice back into its original array:
1871    ///
1872    /// ```
1873    /// #![feature(allocator_api)]
1874    ///
1875    /// use std::sync::Arc;
1876    /// use std::alloc::System;
1877    ///
1878    /// let x: Arc<[u32], _> = Arc::new_in([1, 2, 3], System);
1879    /// let x_ptr: *const [u32] = Arc::into_raw_with_allocator(x).0;
1880    ///
1881    /// unsafe {
1882    ///     let x: Arc<[u32; 3], _> = Arc::from_raw_in(x_ptr.cast::<[u32; 3]>(), System);
1883    ///     assert_eq!(&*x, &[1, 2, 3]);
1884    /// }
1885    /// ```
1886    #[inline]
1887    #[unstable(feature = "allocator_api", issue = "32838")]
1888    pub unsafe fn from_raw_in(ptr: *const T, alloc: A) -> Self {
1889        unsafe {
1890            let offset = data_offset(ptr);
1891
1892            // Reverse the offset to find the original ArcInner.
1893            let arc_ptr = ptr.byte_sub(offset) as *mut ArcInner<T>;
1894
1895            Self::from_ptr_in(arc_ptr, alloc)
1896        }
1897    }
1898
1899    /// Creates a new [`Weak`] pointer to this allocation.
1900    ///
1901    /// # Examples
1902    ///
1903    /// ```
1904    /// use std::sync::Arc;
1905    ///
1906    /// let five = Arc::new(5);
1907    ///
1908    /// let weak_five = Arc::downgrade(&five);
1909    /// ```
1910    #[must_use = "this returns a new `Weak` pointer, \
1911                  without modifying the original `Arc`"]
1912    #[stable(feature = "arc_weak", since = "1.4.0")]
1913    pub fn downgrade(this: &Self) -> Weak<T, A>
1914    where
1915        A: Clone,
1916    {
1917        // This Relaxed is OK because we're checking the value in the CAS
1918        // below.
1919        let mut cur = this.inner().weak.load(Relaxed);
1920
1921        loop {
1922            // check if the weak counter is currently "locked"; if so, spin.
1923            if cur == usize::MAX {
1924                hint::spin_loop();
1925                cur = this.inner().weak.load(Relaxed);
1926                continue;
1927            }
1928
1929            // We can't allow the refcount to increase much past `MAX_REFCOUNT`.
1930            assert!(cur <= MAX_REFCOUNT, "{}", INTERNAL_OVERFLOW_ERROR);
1931
1932            // NOTE: this code currently ignores the possibility of overflow
1933            // into usize::MAX; in general both Rc and Arc need to be adjusted
1934            // to deal with overflow.
1935
1936            // Unlike with Clone(), we need this to be an Acquire read to
1937            // synchronize with the write coming from `is_unique`, so that the
1938            // events prior to that write happen before this read.
1939            match this.inner().weak.compare_exchange_weak(cur, cur + 1, Acquire, Relaxed) {
1940                Ok(_) => {
1941                    // Make sure we do not create a dangling Weak
1942                    debug_assert!(!is_dangling(this.ptr.as_ptr()));
1943                    return Weak { ptr: this.ptr, alloc: this.alloc.clone() };
1944                }
1945                Err(old) => cur = old,
1946            }
1947        }
1948    }
1949
1950    /// Gets the number of [`Weak`] pointers to this allocation.
1951    ///
1952    /// # Safety
1953    ///
1954    /// This method by itself is safe, but using it correctly requires extra care.
1955    /// Another thread can change the weak count at any time,
1956    /// including potentially between calling this method and acting on the result.
1957    ///
1958    /// # Examples
1959    ///
1960    /// ```
1961    /// use std::sync::Arc;
1962    ///
1963    /// let five = Arc::new(5);
1964    /// let _weak_five = Arc::downgrade(&five);
1965    ///
1966    /// // This assertion is deterministic because we haven't shared
1967    /// // the `Arc` or `Weak` between threads.
1968    /// assert_eq!(1, Arc::weak_count(&five));
1969    /// ```
1970    #[inline]
1971    #[must_use]
1972    #[stable(feature = "arc_counts", since = "1.15.0")]
1973    pub fn weak_count(this: &Self) -> usize {
1974        let cnt = this.inner().weak.load(Relaxed);
1975        // If the weak count is currently locked, the value of the
1976        // count was 0 just before taking the lock.
1977        if cnt == usize::MAX { 0 } else { cnt - 1 }
1978    }
1979
1980    /// Gets the number of strong (`Arc`) pointers to this allocation.
1981    ///
1982    /// # Safety
1983    ///
1984    /// This method by itself is safe, but using it correctly requires extra care.
1985    /// Another thread can change the strong count at any time,
1986    /// including potentially between calling this method and acting on the result.
1987    ///
1988    /// # Examples
1989    ///
1990    /// ```
1991    /// use std::sync::Arc;
1992    ///
1993    /// let five = Arc::new(5);
1994    /// let _also_five = Arc::clone(&five);
1995    ///
1996    /// // This assertion is deterministic because we haven't shared
1997    /// // the `Arc` between threads.
1998    /// assert_eq!(2, Arc::strong_count(&five));
1999    /// ```
2000    #[inline]
2001    #[must_use]
2002    #[stable(feature = "arc_counts", since = "1.15.0")]
2003    pub fn strong_count(this: &Self) -> usize {
2004        this.inner().strong.load(Relaxed)
2005    }
2006
2007    /// Increments the strong reference count on the `Arc<T>` associated with the
2008    /// provided pointer by one.
2009    ///
2010    /// # Safety
2011    ///
2012    /// The pointer must have been obtained through `Arc::into_raw` and must satisfy the
2013    /// same layout requirements specified in [`Arc::from_raw_in`][from_raw_in].
2014    /// The associated `Arc` instance must be valid (i.e. the strong count must be at
2015    /// least 1) for the duration of this method, and `ptr` must point to a block of memory
2016    /// allocated by `alloc`.
2017    ///
2018    /// [from_raw_in]: Arc::from_raw_in
2019    ///
2020    /// # Examples
2021    ///
2022    /// ```
2023    /// #![feature(allocator_api)]
2024    ///
2025    /// use std::sync::Arc;
2026    /// use std::alloc::System;
2027    ///
2028    /// let five = Arc::new_in(5, System);
2029    ///
2030    /// unsafe {
2031    ///     let (ptr, _alloc) = Arc::into_raw_with_allocator(five);
2032    ///     Arc::increment_strong_count_in(ptr, System);
2033    ///
2034    ///     // This assertion is deterministic because we haven't shared
2035    ///     // the `Arc` between threads.
2036    ///     let five = Arc::from_raw_in(ptr, System);
2037    ///     assert_eq!(2, Arc::strong_count(&five));
2038    /// #   // Prevent leaks for Miri.
2039    /// #   Arc::decrement_strong_count_in(ptr, System);
2040    /// }
2041    /// ```
2042    #[inline]
2043    #[unstable(feature = "allocator_api", issue = "32838")]
2044    pub unsafe fn increment_strong_count_in(ptr: *const T, alloc: A)
2045    where
2046        A: Clone,
2047    {
2048        // Retain Arc, but don't touch refcount by wrapping in ManuallyDrop
2049        let arc = unsafe { mem::ManuallyDrop::new(Arc::from_raw_in(ptr, alloc)) };
2050        // Now increase refcount, but don't drop new refcount either
2051        let _arc_clone: mem::ManuallyDrop<_> = arc.clone();
2052    }
2053
2054    /// Decrements the strong reference count on the `Arc<T>` associated with the
2055    /// provided pointer by one.
2056    ///
2057    /// # Safety
2058    ///
2059    /// The pointer must have been obtained through `Arc::into_raw` and must satisfy the
2060    /// same layout requirements specified in [`Arc::from_raw_in`][from_raw_in].
2061    /// The associated `Arc` instance must be valid (i.e. the strong count must be at
2062    /// least 1) when invoking this method, and `ptr` must point to a block of memory
2063    /// allocated by `alloc`. This method can be used to release the final
2064    /// `Arc` and backing storage, but **should not** be called after the final `Arc` has been
2065    /// released.
2066    ///
2067    /// [from_raw_in]: Arc::from_raw_in
2068    ///
2069    /// # Examples
2070    ///
2071    /// ```
2072    /// #![feature(allocator_api)]
2073    ///
2074    /// use std::sync::Arc;
2075    /// use std::alloc::System;
2076    ///
2077    /// let five = Arc::new_in(5, System);
2078    ///
2079    /// unsafe {
2080    ///     let (ptr, _alloc) = Arc::into_raw_with_allocator(five);
2081    ///     Arc::increment_strong_count_in(ptr, System);
2082    ///
2083    ///     // Those assertions are deterministic because we haven't shared
2084    ///     // the `Arc` between threads.
2085    ///     let five = Arc::from_raw_in(ptr, System);
2086    ///     assert_eq!(2, Arc::strong_count(&five));
2087    ///     Arc::decrement_strong_count_in(ptr, System);
2088    ///     assert_eq!(1, Arc::strong_count(&five));
2089    /// }
2090    /// ```
2091    #[inline]
2092    #[unstable(feature = "allocator_api", issue = "32838")]
2093    pub unsafe fn decrement_strong_count_in(ptr: *const T, alloc: A) {
2094        unsafe { drop(Arc::from_raw_in(ptr, alloc)) };
2095    }
2096
2097    #[inline]
2098    fn inner(&self) -> &ArcInner<T> {
2099        // This unsafety is ok because while this arc is alive we're guaranteed
2100        // that the inner pointer is valid. Furthermore, we know that the
2101        // `ArcInner` structure itself is `Sync` because the inner data is
2102        // `Sync` as well, so we're ok loaning out an immutable pointer to these
2103        // contents.
2104        unsafe { self.ptr.as_ref() }
2105    }
2106
2107    // Non-inlined part of `drop`.
2108    #[inline(never)]
2109    unsafe fn drop_slow(&mut self) {
2110        // Drop the weak ref collectively held by all strong references when this
2111        // variable goes out of scope. This ensures that the memory is deallocated
2112        // even if the destructor of `T` panics.
2113        // Take a reference to `self.alloc` instead of cloning because 1. it'll last long
2114        // enough, and 2. you should be able to drop `Arc`s with unclonable allocators
2115        let _weak = Weak { ptr: self.ptr, alloc: &self.alloc };
2116
2117        // Destroy the data at this time, even though we must not free the box
2118        // allocation itself (there might still be weak pointers lying around).
2119        // We cannot use `get_mut_unchecked` here, because `self.alloc` is borrowed.
2120        unsafe { ptr::drop_in_place(&mut (*self.ptr.as_ptr()).data) };
2121    }
2122
2123    /// Returns `true` if the two `Arc`s point to the same allocation in a vein similar to
2124    /// [`ptr::eq`]. This function ignores the metadata of  `dyn Trait` pointers.
2125    ///
2126    /// # Examples
2127    ///
2128    /// ```
2129    /// use std::sync::Arc;
2130    ///
2131    /// let five = Arc::new(5);
2132    /// let same_five = Arc::clone(&five);
2133    /// let other_five = Arc::new(5);
2134    ///
2135    /// assert!(Arc::ptr_eq(&five, &same_five));
2136    /// assert!(!Arc::ptr_eq(&five, &other_five));
2137    /// ```
2138    ///
2139    /// [`ptr::eq`]: core::ptr::eq "ptr::eq"
2140    #[inline]
2141    #[must_use]
2142    #[stable(feature = "ptr_eq", since = "1.17.0")]
2143    pub fn ptr_eq(this: &Self, other: &Self) -> bool {
2144        ptr::addr_eq(this.ptr.as_ptr(), other.ptr.as_ptr())
2145    }
2146}
2147
2148impl<T: ?Sized> Arc<T> {
2149    /// Allocates an `ArcInner<T>` with sufficient space for
2150    /// a possibly-unsized inner value where the value has the layout provided.
2151    ///
2152    /// The function `mem_to_arcinner` is called with the data pointer
2153    /// and must return back a (potentially fat)-pointer for the `ArcInner<T>`.
2154    #[cfg(not(no_global_oom_handling))]
2155    unsafe fn allocate_for_layout(
2156        value_layout: Layout,
2157        allocate: impl FnOnce(Layout) -> Result<NonNull<[u8]>, AllocError>,
2158        mem_to_arcinner: impl FnOnce(*mut u8) -> *mut ArcInner<T>,
2159    ) -> *mut ArcInner<T> {
2160        let layout = arcinner_layout_for_value_layout(value_layout);
2161
2162        let ptr = allocate(layout).unwrap_or_else(|_| handle_alloc_error(layout));
2163
2164        unsafe { Self::initialize_arcinner(ptr, layout, mem_to_arcinner) }
2165    }
2166
2167    /// Allocates an `ArcInner<T>` with sufficient space for
2168    /// a possibly-unsized inner value where the value has the layout provided,
2169    /// returning an error if allocation fails.
2170    ///
2171    /// The function `mem_to_arcinner` is called with the data pointer
2172    /// and must return back a (potentially fat)-pointer for the `ArcInner<T>`.
2173    unsafe fn try_allocate_for_layout(
2174        value_layout: Layout,
2175        allocate: impl FnOnce(Layout) -> Result<NonNull<[u8]>, AllocError>,
2176        mem_to_arcinner: impl FnOnce(*mut u8) -> *mut ArcInner<T>,
2177    ) -> Result<*mut ArcInner<T>, AllocError> {
2178        let layout = arcinner_layout_for_value_layout(value_layout);
2179
2180        let ptr = allocate(layout)?;
2181
2182        let inner = unsafe { Self::initialize_arcinner(ptr, layout, mem_to_arcinner) };
2183
2184        Ok(inner)
2185    }
2186
2187    unsafe fn initialize_arcinner(
2188        ptr: NonNull<[u8]>,
2189        layout: Layout,
2190        mem_to_arcinner: impl FnOnce(*mut u8) -> *mut ArcInner<T>,
2191    ) -> *mut ArcInner<T> {
2192        let inner = mem_to_arcinner(ptr.as_non_null_ptr().as_ptr());
2193        debug_assert_eq!(unsafe { Layout::for_value_raw(inner) }, layout);
2194
2195        unsafe {
2196            (&raw mut (*inner).strong).write(atomic::AtomicUsize::new(1));
2197            (&raw mut (*inner).weak).write(atomic::AtomicUsize::new(1));
2198        }
2199
2200        inner
2201    }
2202}
2203
2204impl<T: ?Sized, A: Allocator> Arc<T, A> {
2205    /// Allocates an `ArcInner<T>` with sufficient space for an unsized inner value.
2206    #[inline]
2207    #[cfg(not(no_global_oom_handling))]
2208    unsafe fn allocate_for_ptr_in(ptr: *const T, alloc: &A) -> *mut ArcInner<T> {
2209        // Allocate for the `ArcInner<T>` using the given value.
2210        unsafe {
2211            Arc::allocate_for_layout(
2212                Layout::for_value_raw(ptr),
2213                |layout| alloc.allocate(layout),
2214                |mem| mem.with_metadata_of(ptr as *const ArcInner<T>),
2215            )
2216        }
2217    }
2218
2219    #[cfg(not(no_global_oom_handling))]
2220    fn from_box_in(src: Box<T, A>) -> Arc<T, A> {
2221        unsafe {
2222            let value_size = size_of_val(&*src);
2223            let ptr = Self::allocate_for_ptr_in(&*src, Box::allocator(&src));
2224
2225            // Copy value as bytes
2226            ptr::copy_nonoverlapping(
2227                (&raw const *src) as *const u8,
2228                (&raw mut (*ptr).data) as *mut u8,
2229                value_size,
2230            );
2231
2232            // Free the allocation without dropping its contents
2233            let (bptr, alloc) = Box::into_raw_with_allocator(src);
2234            let src = Box::from_raw_in(bptr as *mut mem::ManuallyDrop<T>, alloc.by_ref());
2235            drop(src);
2236
2237            Self::from_ptr_in(ptr, alloc)
2238        }
2239    }
2240}
2241
2242impl<T> Arc<[T]> {
2243    /// Allocates an `ArcInner<[T]>` with the given length.
2244    #[cfg(not(no_global_oom_handling))]
2245    unsafe fn allocate_for_slice(len: usize) -> *mut ArcInner<[T]> {
2246        unsafe {
2247            Self::allocate_for_layout(
2248                Layout::array::<T>(len).unwrap(),
2249                |layout| Global.allocate(layout),
2250                |mem| ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len) as *mut ArcInner<[T]>,
2251            )
2252        }
2253    }
2254
2255    /// Copy elements from slice into newly allocated `Arc<[T]>`
2256    ///
2257    /// Unsafe because the caller must either take ownership, bind `T: Copy` or
2258    /// bind `T: TrivialClone`.
2259    #[cfg(not(no_global_oom_handling))]
2260    unsafe fn copy_from_slice(v: &[T]) -> Arc<[T]> {
2261        unsafe {
2262            let ptr = Self::allocate_for_slice(v.len());
2263
2264            ptr::copy_nonoverlapping(v.as_ptr(), (&raw mut (*ptr).data) as *mut T, v.len());
2265
2266            Self::from_ptr(ptr)
2267        }
2268    }
2269
2270    /// Constructs an `Arc<[T]>` from an iterator known to be of a certain size.
2271    ///
2272    /// Behavior is undefined should the size be wrong.
2273    #[cfg(not(no_global_oom_handling))]
2274    unsafe fn from_iter_exact(iter: impl Iterator<Item = T>, len: usize) -> Arc<[T]> {
2275        // Panic guard while cloning T elements.
2276        // In the event of a panic, elements that have been written
2277        // into the new ArcInner will be dropped, then the memory freed.
2278        struct Guard<T> {
2279            mem: NonNull<u8>,
2280            elems: *mut T,
2281            layout: Layout,
2282            n_elems: usize,
2283        }
2284
2285        impl<T> Drop for Guard<T> {
2286            fn drop(&mut self) {
2287                unsafe {
2288                    let slice = from_raw_parts_mut(self.elems, self.n_elems);
2289                    ptr::drop_in_place(slice);
2290
2291                    Global.deallocate(self.mem, self.layout);
2292                }
2293            }
2294        }
2295
2296        unsafe {
2297            let ptr = Self::allocate_for_slice(len);
2298
2299            let mem = ptr as *mut _ as *mut u8;
2300            let layout = Layout::for_value_raw(ptr);
2301
2302            // Pointer to first element
2303            let elems = (&raw mut (*ptr).data) as *mut T;
2304
2305            let mut guard = Guard { mem: NonNull::new_unchecked(mem), elems, layout, n_elems: 0 };
2306
2307            for (i, item) in iter.enumerate() {
2308                ptr::write(elems.add(i), item);
2309                guard.n_elems += 1;
2310            }
2311
2312            // All clear. Forget the guard so it doesn't free the new ArcInner.
2313            mem::forget(guard);
2314
2315            Self::from_ptr(ptr)
2316        }
2317    }
2318}
2319
2320impl<T, A: Allocator> Arc<[T], A> {
2321    /// Allocates an `ArcInner<[T]>` with the given length.
2322    #[inline]
2323    #[cfg(not(no_global_oom_handling))]
2324    unsafe fn allocate_for_slice_in(len: usize, alloc: &A) -> *mut ArcInner<[T]> {
2325        unsafe {
2326            Arc::allocate_for_layout(
2327                Layout::array::<T>(len).unwrap(),
2328                |layout| alloc.allocate(layout),
2329                |mem| ptr::slice_from_raw_parts_mut(mem.cast::<T>(), len) as *mut ArcInner<[T]>,
2330            )
2331        }
2332    }
2333}
2334
2335/// Specialization trait used for `From<&[T]>`.
2336#[cfg(not(no_global_oom_handling))]
2337trait ArcFromSlice<T> {
2338    fn from_slice(slice: &[T]) -> Self;
2339}
2340
2341#[cfg(not(no_global_oom_handling))]
2342impl<T: Clone> ArcFromSlice<T> for Arc<[T]> {
2343    #[inline]
2344    default fn from_slice(v: &[T]) -> Self {
2345        unsafe { Self::from_iter_exact(v.iter().cloned(), v.len()) }
2346    }
2347}
2348
2349#[cfg(not(no_global_oom_handling))]
2350impl<T: TrivialClone> ArcFromSlice<T> for Arc<[T]> {
2351    #[inline]
2352    fn from_slice(v: &[T]) -> Self {
2353        // SAFETY: `T` implements `TrivialClone`, so this is sound and equivalent
2354        // to the above.
2355        unsafe { Arc::copy_from_slice(v) }
2356    }
2357}
2358
2359#[stable(feature = "rust1", since = "1.0.0")]
2360impl<T: ?Sized, A: Allocator + Clone> Clone for Arc<T, A> {
2361    /// Makes a clone of the `Arc` pointer.
2362    ///
2363    /// This creates another pointer to the same allocation, increasing the
2364    /// strong reference count.
2365    ///
2366    /// # Examples
2367    ///
2368    /// ```
2369    /// use std::sync::Arc;
2370    ///
2371    /// let five = Arc::new(5);
2372    ///
2373    /// let _ = Arc::clone(&five);
2374    /// ```
2375    #[inline]
2376    fn clone(&self) -> Arc<T, A> {
2377        // Using a relaxed ordering is alright here, as knowledge of the
2378        // original reference prevents other threads from erroneously deleting
2379        // the object.
2380        //
2381        // As explained in the [Boost documentation][1], Increasing the
2382        // reference counter can always be done with memory_order_relaxed: New
2383        // references to an object can only be formed from an existing
2384        // reference, and passing an existing reference from one thread to
2385        // another must already provide any required synchronization.
2386        //
2387        // [1]: (www.boost.org/doc/libs/1_55_0/doc/html/atomic/usage_examples.html)
2388        let old_size = self.inner().strong.fetch_add(1, Relaxed);
2389
2390        // However we need to guard against massive refcounts in case someone is `mem::forget`ing
2391        // Arcs. If we don't do this the count can overflow and users will use-after free. This
2392        // branch will never be taken in any realistic program. We abort because such a program is
2393        // incredibly degenerate, and we don't care to support it.
2394        //
2395        // This check is not 100% water-proof: we error when the refcount grows beyond `isize::MAX`.
2396        // But we do that check *after* having done the increment, so there is a chance here that
2397        // the worst already happened and we actually do overflow the `usize` counter. However, that
2398        // requires the counter to grow from `isize::MAX` to `usize::MAX` between the increment
2399        // above and the `abort` below, which seems exceedingly unlikely.
2400        //
2401        // This is a global invariant, and also applies when using a compare-exchange loop to increment
2402        // counters in other methods.
2403        // Otherwise, the counter could be brought to an almost-overflow using a compare-exchange loop,
2404        // and then overflow using a few `fetch_add`s.
2405        if old_size > MAX_REFCOUNT {
2406            abort();
2407        }
2408
2409        unsafe { Self::from_inner_in(self.ptr, self.alloc.clone()) }
2410    }
2411}
2412
2413#[unstable(feature = "ergonomic_clones", issue = "132290")]
2414impl<T: ?Sized, A: Allocator + Clone> UseCloned for Arc<T, A> {}
2415
2416#[stable(feature = "rust1", since = "1.0.0")]
2417impl<T: ?Sized, A: Allocator> Deref for Arc<T, A> {
2418    type Target = T;
2419
2420    #[inline]
2421    fn deref(&self) -> &T {
2422        &self.inner().data
2423    }
2424}
2425
2426#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2427unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for Arc<T, A> {}
2428
2429#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2430unsafe impl<T: ?Sized, A: Allocator> PinCoerceUnsized for Weak<T, A> {}
2431
2432#[unstable(feature = "deref_pure_trait", issue = "87121")]
2433unsafe impl<T: ?Sized, A: Allocator> DerefPure for Arc<T, A> {}
2434
2435#[unstable(feature = "legacy_receiver_trait", issue = "none")]
2436impl<T: ?Sized> LegacyReceiver for Arc<T> {}
2437
2438#[cfg(not(no_global_oom_handling))]
2439impl<T: ?Sized + CloneToUninit, A: Allocator + Clone> Arc<T, A> {
2440    /// Makes a mutable reference into the given `Arc`.
2441    ///
2442    /// If there are other `Arc` pointers to the same allocation, then `make_mut` will
2443    /// [`clone`] the inner value to a new allocation to ensure unique ownership.  This is also
2444    /// referred to as clone-on-write.
2445    ///
2446    /// However, if there are no other `Arc` pointers to this allocation, but some [`Weak`]
2447    /// pointers, then the [`Weak`] pointers will be dissociated and the inner value will not
2448    /// be cloned.
2449    ///
2450    /// See also [`get_mut`], which will fail rather than cloning the inner value
2451    /// or dissociating [`Weak`] pointers.
2452    ///
2453    /// [`clone`]: Clone::clone
2454    /// [`get_mut`]: Arc::get_mut
2455    ///
2456    /// # Examples
2457    ///
2458    /// ```
2459    /// use std::sync::Arc;
2460    ///
2461    /// let mut data = Arc::new(5);
2462    ///
2463    /// *Arc::make_mut(&mut data) += 1;         // Won't clone anything
2464    /// let mut other_data = Arc::clone(&data); // Won't clone inner data
2465    /// *Arc::make_mut(&mut data) += 1;         // Clones inner data
2466    /// *Arc::make_mut(&mut data) += 1;         // Won't clone anything
2467    /// *Arc::make_mut(&mut other_data) *= 2;   // Won't clone anything
2468    ///
2469    /// // Now `data` and `other_data` point to different allocations.
2470    /// assert_eq!(*data, 8);
2471    /// assert_eq!(*other_data, 12);
2472    /// ```
2473    ///
2474    /// [`Weak`] pointers will be dissociated:
2475    ///
2476    /// ```
2477    /// use std::sync::Arc;
2478    ///
2479    /// let mut data = Arc::new(75);
2480    /// let weak = Arc::downgrade(&data);
2481    ///
2482    /// assert!(75 == *data);
2483    /// assert!(75 == *weak.upgrade().unwrap());
2484    ///
2485    /// *Arc::make_mut(&mut data) += 1;
2486    ///
2487    /// assert!(76 == *data);
2488    /// assert!(weak.upgrade().is_none());
2489    /// ```
2490    #[inline]
2491    #[stable(feature = "arc_unique", since = "1.4.0")]
2492    pub fn make_mut(this: &mut Self) -> &mut T {
2493        let size_of_val = size_of_val::<T>(&**this);
2494
2495        // Note that we hold both a strong reference and a weak reference.
2496        // Thus, releasing our strong reference only will not, by itself, cause
2497        // the memory to be deallocated.
2498        //
2499        // Use Acquire to ensure that we see any writes to `weak` that happen
2500        // before release writes (i.e., decrements) to `strong`. Since we hold a
2501        // weak count, there's no chance the ArcInner itself could be
2502        // deallocated.
2503        if this.inner().strong.compare_exchange(1, 0, Acquire, Relaxed).is_err() {
2504            // Another strong pointer exists, so we must clone.
2505            *this = Arc::clone_from_ref_in(&**this, this.alloc.clone());
2506        } else if this.inner().weak.load(Relaxed) != 1 {
2507            // Relaxed suffices in the above because this is fundamentally an
2508            // optimization: we are always racing with weak pointers being
2509            // dropped. Worst case, we end up allocated a new Arc unnecessarily.
2510
2511            // We removed the last strong ref, but there are additional weak
2512            // refs remaining. We'll move the contents to a new Arc, and
2513            // invalidate the other weak refs.
2514
2515            // Note that it is not possible for the read of `weak` to yield
2516            // usize::MAX (i.e., locked), since the weak count can only be
2517            // locked by a thread with a strong reference.
2518
2519            // Materialize our own implicit weak pointer, so that it can clean
2520            // up the ArcInner as needed.
2521            let _weak = Weak { ptr: this.ptr, alloc: this.alloc.clone() };
2522
2523            // Can just steal the data, all that's left is Weaks
2524            //
2525            // We don't need panic-protection like the above branch does, but we might as well
2526            // use the same mechanism.
2527            let mut in_progress: UniqueArcUninit<T, A> =
2528                UniqueArcUninit::new(&**this, this.alloc.clone());
2529            unsafe {
2530                // Initialize `in_progress` with move of **this.
2531                // We have to express this in terms of bytes because `T: ?Sized`; there is no
2532                // operation that just copies a value based on its `size_of_val()`.
2533                ptr::copy_nonoverlapping(
2534                    ptr::from_ref(&**this).cast::<u8>(),
2535                    in_progress.data_ptr().cast::<u8>(),
2536                    size_of_val,
2537                );
2538
2539                ptr::write(this, in_progress.into_arc());
2540            }
2541        } else {
2542            // We were the sole reference of either kind; bump back up the
2543            // strong ref count.
2544            this.inner().strong.store(1, Release);
2545        }
2546
2547        // As with `get_mut()`, the unsafety is ok because our reference was
2548        // either unique to begin with, or became one upon cloning the contents.
2549        unsafe { Self::get_mut_unchecked(this) }
2550    }
2551}
2552
2553impl<T: Clone, A: Allocator> Arc<T, A> {
2554    /// If we have the only reference to `T` then unwrap it. Otherwise, clone `T` and return the
2555    /// clone.
2556    ///
2557    /// Assuming `arc_t` is of type `Arc<T>`, this function is functionally equivalent to
2558    /// `(*arc_t).clone()`, but will avoid cloning the inner value where possible.
2559    ///
2560    /// # Examples
2561    ///
2562    /// ```
2563    /// # use std::{ptr, sync::Arc};
2564    /// let inner = String::from("test");
2565    /// let ptr = inner.as_ptr();
2566    ///
2567    /// let arc = Arc::new(inner);
2568    /// let inner = Arc::unwrap_or_clone(arc);
2569    /// // The inner value was not cloned
2570    /// assert!(ptr::eq(ptr, inner.as_ptr()));
2571    ///
2572    /// let arc = Arc::new(inner);
2573    /// let arc2 = arc.clone();
2574    /// let inner = Arc::unwrap_or_clone(arc);
2575    /// // Because there were 2 references, we had to clone the inner value.
2576    /// assert!(!ptr::eq(ptr, inner.as_ptr()));
2577    /// // `arc2` is the last reference, so when we unwrap it we get back
2578    /// // the original `String`.
2579    /// let inner = Arc::unwrap_or_clone(arc2);
2580    /// assert!(ptr::eq(ptr, inner.as_ptr()));
2581    /// ```
2582    #[inline]
2583    #[stable(feature = "arc_unwrap_or_clone", since = "1.76.0")]
2584    pub fn unwrap_or_clone(this: Self) -> T {
2585        Arc::try_unwrap(this).unwrap_or_else(|arc| (*arc).clone())
2586    }
2587}
2588
2589impl<T: ?Sized, A: Allocator> Arc<T, A> {
2590    /// Returns a mutable reference into the given `Arc`, if there are
2591    /// no other `Arc` or [`Weak`] pointers to the same allocation.
2592    ///
2593    /// Returns [`None`] otherwise, because it is not safe to
2594    /// mutate a shared value.
2595    ///
2596    /// See also [`make_mut`][make_mut], which will [`clone`][clone]
2597    /// the inner value when there are other `Arc` pointers.
2598    ///
2599    /// [make_mut]: Arc::make_mut
2600    /// [clone]: Clone::clone
2601    ///
2602    /// # Examples
2603    ///
2604    /// ```
2605    /// use std::sync::Arc;
2606    ///
2607    /// let mut x = Arc::new(3);
2608    /// *Arc::get_mut(&mut x).unwrap() = 4;
2609    /// assert_eq!(*x, 4);
2610    ///
2611    /// let _y = Arc::clone(&x);
2612    /// assert!(Arc::get_mut(&mut x).is_none());
2613    /// ```
2614    #[inline]
2615    #[stable(feature = "arc_unique", since = "1.4.0")]
2616    pub fn get_mut(this: &mut Self) -> Option<&mut T> {
2617        if Self::is_unique(this) {
2618            // This unsafety is ok because we're guaranteed that the pointer
2619            // returned is the *only* pointer that will ever be returned to T. Our
2620            // reference count is guaranteed to be 1 at this point, and we required
2621            // the Arc itself to be `mut`, so we're returning the only possible
2622            // reference to the inner data.
2623            unsafe { Some(Arc::get_mut_unchecked(this)) }
2624        } else {
2625            None
2626        }
2627    }
2628
2629    /// Returns a mutable reference into the given `Arc`,
2630    /// without any check.
2631    ///
2632    /// See also [`get_mut`], which is safe and does appropriate checks.
2633    ///
2634    /// [`get_mut`]: Arc::get_mut
2635    ///
2636    /// # Safety
2637    ///
2638    /// If any other `Arc` or [`Weak`] pointers to the same allocation exist, then
2639    /// they must not be dereferenced or have active borrows for the duration
2640    /// of the returned borrow, and their inner type must be exactly the same as the
2641    /// inner type of this Arc (including lifetimes). This is trivially the case if no
2642    /// such pointers exist, for example immediately after `Arc::new`.
2643    ///
2644    /// # Examples
2645    ///
2646    /// ```
2647    /// #![feature(get_mut_unchecked)]
2648    ///
2649    /// use std::sync::Arc;
2650    ///
2651    /// let mut x = Arc::new(String::new());
2652    /// unsafe {
2653    ///     Arc::get_mut_unchecked(&mut x).push_str("foo")
2654    /// }
2655    /// assert_eq!(*x, "foo");
2656    /// ```
2657    /// Other `Arc` pointers to the same allocation must be to the same type.
2658    /// ```no_run
2659    /// #![feature(get_mut_unchecked)]
2660    ///
2661    /// use std::sync::Arc;
2662    ///
2663    /// let x: Arc<str> = Arc::from("Hello, world!");
2664    /// let mut y: Arc<[u8]> = x.clone().into();
2665    /// unsafe {
2666    ///     // this is Undefined Behavior, because x's inner type is str, not [u8]
2667    ///     Arc::get_mut_unchecked(&mut y).fill(0xff); // 0xff is invalid in UTF-8
2668    /// }
2669    /// println!("{}", &*x); // Invalid UTF-8 in a str
2670    /// ```
2671    /// Other `Arc` pointers to the same allocation must be to the exact same type, including lifetimes.
2672    /// ```no_run
2673    /// #![feature(get_mut_unchecked)]
2674    ///
2675    /// use std::sync::Arc;
2676    ///
2677    /// let x: Arc<&str> = Arc::new("Hello, world!");
2678    /// {
2679    ///     let s = String::from("Oh, no!");
2680    ///     let mut y: Arc<&str> = x.clone();
2681    ///     unsafe {
2682    ///         // this is Undefined Behavior, because x's inner type
2683    ///         // is &'long str, not &'short str
2684    ///         *Arc::get_mut_unchecked(&mut y) = &s;
2685    ///     }
2686    /// }
2687    /// println!("{}", &*x); // Use-after-free
2688    /// ```
2689    #[inline]
2690    #[unstable(feature = "get_mut_unchecked", issue = "63292")]
2691    pub unsafe fn get_mut_unchecked(this: &mut Self) -> &mut T {
2692        // We are careful to *not* create a reference covering the "count" fields, as
2693        // this would alias with concurrent access to the reference counts (e.g. by `Weak`).
2694        unsafe { &mut (*this.ptr.as_ptr()).data }
2695    }
2696
2697    /// Determine whether this is the unique reference to the underlying data.
2698    ///
2699    /// Returns `true` if there are no other `Arc` or [`Weak`] pointers to the same allocation;
2700    /// returns `false` otherwise.
2701    ///
2702    /// If this function returns `true`, then is guaranteed to be safe to call [`get_mut_unchecked`]
2703    /// on this `Arc`, so long as no clones occur in between.
2704    ///
2705    /// # Examples
2706    ///
2707    /// ```
2708    /// #![feature(arc_is_unique)]
2709    ///
2710    /// use std::sync::Arc;
2711    ///
2712    /// let x = Arc::new(3);
2713    /// assert!(Arc::is_unique(&x));
2714    ///
2715    /// let y = Arc::clone(&x);
2716    /// assert!(!Arc::is_unique(&x));
2717    /// drop(y);
2718    ///
2719    /// // Weak references also count, because they could be upgraded at any time.
2720    /// let z = Arc::downgrade(&x);
2721    /// assert!(!Arc::is_unique(&x));
2722    /// ```
2723    ///
2724    /// # Pointer invalidation
2725    ///
2726    /// This function will always return the same value as `Arc::get_mut(arc).is_some()`. However,
2727    /// unlike that operation it does not produce any mutable references to the underlying data,
2728    /// meaning no pointers to the data inside the `Arc` are invalidated by the call. Thus, the
2729    /// following code is valid, even though it would be UB if it used `Arc::get_mut`:
2730    ///
2731    /// ```
2732    /// #![feature(arc_is_unique)]
2733    ///
2734    /// use std::sync::Arc;
2735    ///
2736    /// let arc = Arc::new(5);
2737    /// let pointer: *const i32 = &*arc;
2738    /// assert!(Arc::is_unique(&arc));
2739    /// assert_eq!(unsafe { *pointer }, 5);
2740    /// ```
2741    ///
2742    /// # Atomic orderings
2743    ///
2744    /// Concurrent drops to other `Arc` pointers to the same allocation will synchronize with this
2745    /// call - that is, this call performs an `Acquire` operation on the underlying strong and weak
2746    /// ref counts. This ensures that calling `get_mut_unchecked` is safe.
2747    ///
2748    /// Note that this operation requires locking the weak ref count, so concurrent calls to
2749    /// `downgrade` may spin-loop for a short period of time.
2750    ///
2751    /// [`get_mut_unchecked`]: Self::get_mut_unchecked
2752    #[inline]
2753    #[unstable(feature = "arc_is_unique", issue = "138938")]
2754    pub fn is_unique(this: &Self) -> bool {
2755        // lock the weak pointer count if we appear to be the sole weak pointer
2756        // holder.
2757        //
2758        // The acquire label here ensures a happens-before relationship with any
2759        // writes to `strong` (in particular in `Weak::upgrade`) prior to decrements
2760        // of the `weak` count (via `Weak::drop`, which uses release). If the upgraded
2761        // weak ref was never dropped, the CAS here will fail so we do not care to synchronize.
2762        if this.inner().weak.compare_exchange(1, usize::MAX, Acquire, Relaxed).is_ok() {
2763            // This needs to be an `Acquire` to synchronize with the decrement of the `strong`
2764            // counter in `drop` -- the only access that happens when any but the last reference
2765            // is being dropped.
2766            let unique = this.inner().strong.load(Acquire) == 1;
2767
2768            // The release write here synchronizes with a read in `downgrade`,
2769            // effectively preventing the above read of `strong` from happening
2770            // after the write.
2771            this.inner().weak.store(1, Release); // release the lock
2772            unique
2773        } else {
2774            false
2775        }
2776    }
2777}
2778
2779#[stable(feature = "rust1", since = "1.0.0")]
2780unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for Arc<T, A> {
2781    /// Drops the `Arc`.
2782    ///
2783    /// This will decrement the strong reference count. If the strong reference
2784    /// count reaches zero then the only other references (if any) are
2785    /// [`Weak`], so we `drop` the inner value.
2786    ///
2787    /// # Examples
2788    ///
2789    /// ```
2790    /// use std::sync::Arc;
2791    ///
2792    /// struct Foo;
2793    ///
2794    /// impl Drop for Foo {
2795    ///     fn drop(&mut self) {
2796    ///         println!("dropped!");
2797    ///     }
2798    /// }
2799    ///
2800    /// let foo  = Arc::new(Foo);
2801    /// let foo2 = Arc::clone(&foo);
2802    ///
2803    /// drop(foo);    // Doesn't print anything
2804    /// drop(foo2);   // Prints "dropped!"
2805    /// ```
2806    #[inline]
2807    fn drop(&mut self) {
2808        // Because `fetch_sub` is already atomic, we do not need to synchronize
2809        // with other threads unless we are going to delete the object. This
2810        // same logic applies to the below `fetch_sub` to the `weak` count.
2811        if self.inner().strong.fetch_sub(1, Release) != 1 {
2812            return;
2813        }
2814
2815        // This fence is needed to prevent reordering of use of the data and
2816        // deletion of the data. Because it is marked `Release`, the decreasing
2817        // of the reference count synchronizes with this `Acquire` fence. This
2818        // means that use of the data happens before decreasing the reference
2819        // count, which happens before this fence, which happens before the
2820        // deletion of the data.
2821        //
2822        // As explained in the [Boost documentation][1],
2823        //
2824        // > It is important to enforce any possible access to the object in one
2825        // > thread (through an existing reference) to *happen before* deleting
2826        // > the object in a different thread. This is achieved by a "release"
2827        // > operation after dropping a reference (any access to the object
2828        // > through this reference must obviously happened before), and an
2829        // > "acquire" operation before deleting the object.
2830        //
2831        // In particular, while the contents of an Arc are usually immutable, it's
2832        // possible to have interior writes to something like a Mutex<T>. Since a
2833        // Mutex is not acquired when it is deleted, we can't rely on its
2834        // synchronization logic to make writes in thread A visible to a destructor
2835        // running in thread B.
2836        //
2837        // Also note that the Acquire fence here could probably be replaced with an
2838        // Acquire load, which could improve performance in highly-contended
2839        // situations. See [2].
2840        //
2841        // [1]: (www.boost.org/doc/libs/1_55_0/doc/html/atomic/usage_examples.html)
2842        // [2]: (https://github.com/rust-lang/rust/pull/41714)
2843        acquire!(self.inner().strong);
2844
2845        // Make sure we aren't trying to "drop" the shared static for empty slices
2846        // used by Default::default.
2847        debug_assert!(
2848            !ptr::addr_eq(self.ptr.as_ptr(), &STATIC_INNER_SLICE.inner),
2849            "Arcs backed by a static should never reach a strong count of 0. \
2850            Likely decrement_strong_count or from_raw were called too many times.",
2851        );
2852
2853        unsafe {
2854            self.drop_slow();
2855        }
2856    }
2857}
2858
2859impl<A: Allocator> Arc<dyn Any + Send + Sync, A> {
2860    /// Attempts to downcast the `Arc<dyn Any + Send + Sync>` to a concrete type.
2861    ///
2862    /// # Examples
2863    ///
2864    /// ```
2865    /// use std::any::Any;
2866    /// use std::sync::Arc;
2867    ///
2868    /// fn print_if_string(value: Arc<dyn Any + Send + Sync>) {
2869    ///     if let Ok(string) = value.downcast::<String>() {
2870    ///         println!("String ({}): {}", string.len(), string);
2871    ///     }
2872    /// }
2873    ///
2874    /// let my_string = "Hello World".to_string();
2875    /// print_if_string(Arc::new(my_string));
2876    /// print_if_string(Arc::new(0i8));
2877    /// ```
2878    #[inline]
2879    #[stable(feature = "rc_downcast", since = "1.29.0")]
2880    pub fn downcast<T>(self) -> Result<Arc<T, A>, Self>
2881    where
2882        T: Any + Send + Sync,
2883    {
2884        if (*self).is::<T>() {
2885            unsafe {
2886                let (ptr, alloc) = Arc::into_inner_with_allocator(self);
2887                Ok(Arc::from_inner_in(ptr.cast(), alloc))
2888            }
2889        } else {
2890            Err(self)
2891        }
2892    }
2893
2894    /// Downcasts the `Arc<dyn Any + Send + Sync>` to a concrete type.
2895    ///
2896    /// For a safe alternative see [`downcast`].
2897    ///
2898    /// # Examples
2899    ///
2900    /// ```
2901    /// #![feature(downcast_unchecked)]
2902    ///
2903    /// use std::any::Any;
2904    /// use std::sync::Arc;
2905    ///
2906    /// let x: Arc<dyn Any + Send + Sync> = Arc::new(1_usize);
2907    ///
2908    /// unsafe {
2909    ///     assert_eq!(*x.downcast_unchecked::<usize>(), 1);
2910    /// }
2911    /// ```
2912    ///
2913    /// # Safety
2914    ///
2915    /// The contained value must be of type `T`. Calling this method
2916    /// with the incorrect type is *undefined behavior*.
2917    ///
2918    ///
2919    /// [`downcast`]: Self::downcast
2920    #[inline]
2921    #[unstable(feature = "downcast_unchecked", issue = "90850")]
2922    pub unsafe fn downcast_unchecked<T>(self) -> Arc<T, A>
2923    where
2924        T: Any + Send + Sync,
2925    {
2926        unsafe {
2927            let (ptr, alloc) = Arc::into_inner_with_allocator(self);
2928            Arc::from_inner_in(ptr.cast(), alloc)
2929        }
2930    }
2931}
2932
2933impl<T> Weak<T> {
2934    /// Constructs a new `Weak<T>`, without allocating any memory.
2935    /// Calling [`upgrade`] on the return value always gives [`None`].
2936    ///
2937    /// [`upgrade`]: Weak::upgrade
2938    ///
2939    /// # Examples
2940    ///
2941    /// ```
2942    /// use std::sync::Weak;
2943    ///
2944    /// let empty: Weak<i64> = Weak::new();
2945    /// assert!(empty.upgrade().is_none());
2946    /// ```
2947    #[inline]
2948    #[stable(feature = "downgraded_weak", since = "1.10.0")]
2949    #[rustc_const_stable(feature = "const_weak_new", since = "1.73.0")]
2950    #[must_use]
2951    pub const fn new() -> Weak<T> {
2952        Weak { ptr: NonNull::without_provenance(NonZeroUsize::MAX), alloc: Global }
2953    }
2954}
2955
2956impl<T, A: Allocator> Weak<T, A> {
2957    /// Constructs a new `Weak<T, A>`, without allocating any memory, technically in the provided
2958    /// allocator.
2959    /// Calling [`upgrade`] on the return value always gives [`None`].
2960    ///
2961    /// [`upgrade`]: Weak::upgrade
2962    ///
2963    /// # Examples
2964    ///
2965    /// ```
2966    /// #![feature(allocator_api)]
2967    ///
2968    /// use std::sync::Weak;
2969    /// use std::alloc::System;
2970    ///
2971    /// let empty: Weak<i64, _> = Weak::new_in(System);
2972    /// assert!(empty.upgrade().is_none());
2973    /// ```
2974    #[inline]
2975    #[unstable(feature = "allocator_api", issue = "32838")]
2976    pub fn new_in(alloc: A) -> Weak<T, A> {
2977        Weak { ptr: NonNull::without_provenance(NonZeroUsize::MAX), alloc }
2978    }
2979}
2980
2981/// Helper type to allow accessing the reference counts without
2982/// making any assertions about the data field.
2983struct WeakInner<'a> {
2984    weak: &'a Atomic<usize>,
2985    strong: &'a Atomic<usize>,
2986}
2987
2988impl<T: ?Sized> Weak<T> {
2989    /// Converts a raw pointer previously created by [`into_raw`] back into `Weak<T>`.
2990    ///
2991    /// This can be used to safely get a strong reference (by calling [`upgrade`]
2992    /// later) or to deallocate the weak count by dropping the `Weak<T>`.
2993    ///
2994    /// It takes ownership of one weak reference (with the exception of pointers created by [`new`],
2995    /// as these don't own anything; the method still works on them).
2996    ///
2997    /// # Safety
2998    ///
2999    /// The pointer must have originated from the [`into_raw`] and must still own its potential
3000    /// weak reference, and must point to a block of memory allocated by global allocator.
3001    ///
3002    /// It is allowed for the strong count to be 0 at the time of calling this. Nevertheless, this
3003    /// takes ownership of one weak reference currently represented as a raw pointer (the weak
3004    /// count is not modified by this operation) and therefore it must be paired with a previous
3005    /// call to [`into_raw`].
3006    /// # Examples
3007    ///
3008    /// ```
3009    /// use std::sync::{Arc, Weak};
3010    ///
3011    /// let strong = Arc::new("hello".to_owned());
3012    ///
3013    /// let raw_1 = Arc::downgrade(&strong).into_raw();
3014    /// let raw_2 = Arc::downgrade(&strong).into_raw();
3015    ///
3016    /// assert_eq!(2, Arc::weak_count(&strong));
3017    ///
3018    /// assert_eq!("hello", &*unsafe { Weak::from_raw(raw_1) }.upgrade().unwrap());
3019    /// assert_eq!(1, Arc::weak_count(&strong));
3020    ///
3021    /// drop(strong);
3022    ///
3023    /// // Decrement the last weak count.
3024    /// assert!(unsafe { Weak::from_raw(raw_2) }.upgrade().is_none());
3025    /// ```
3026    ///
3027    /// [`new`]: Weak::new
3028    /// [`into_raw`]: Weak::into_raw
3029    /// [`upgrade`]: Weak::upgrade
3030    #[inline]
3031    #[stable(feature = "weak_into_raw", since = "1.45.0")]
3032    pub unsafe fn from_raw(ptr: *const T) -> Self {
3033        unsafe { Weak::from_raw_in(ptr, Global) }
3034    }
3035
3036    /// Consumes the `Weak<T>` and turns it into a raw pointer.
3037    ///
3038    /// This converts the weak pointer into a raw pointer, while still preserving the ownership of
3039    /// one weak reference (the weak count is not modified by this operation). It can be turned
3040    /// back into the `Weak<T>` with [`from_raw`].
3041    ///
3042    /// The same restrictions of accessing the target of the pointer as with
3043    /// [`as_ptr`] apply.
3044    ///
3045    /// # Examples
3046    ///
3047    /// ```
3048    /// use std::sync::{Arc, Weak};
3049    ///
3050    /// let strong = Arc::new("hello".to_owned());
3051    /// let weak = Arc::downgrade(&strong);
3052    /// let raw = weak.into_raw();
3053    ///
3054    /// assert_eq!(1, Arc::weak_count(&strong));
3055    /// assert_eq!("hello", unsafe { &*raw });
3056    ///
3057    /// drop(unsafe { Weak::from_raw(raw) });
3058    /// assert_eq!(0, Arc::weak_count(&strong));
3059    /// ```
3060    ///
3061    /// [`from_raw`]: Weak::from_raw
3062    /// [`as_ptr`]: Weak::as_ptr
3063    #[must_use = "losing the pointer will leak memory"]
3064    #[stable(feature = "weak_into_raw", since = "1.45.0")]
3065    pub fn into_raw(self) -> *const T {
3066        ManuallyDrop::new(self).as_ptr()
3067    }
3068}
3069
3070impl<T: ?Sized, A: Allocator> Weak<T, A> {
3071    /// Returns a reference to the underlying allocator.
3072    #[inline]
3073    #[unstable(feature = "allocator_api", issue = "32838")]
3074    pub fn allocator(&self) -> &A {
3075        &self.alloc
3076    }
3077
3078    /// Returns a raw pointer to the object `T` pointed to by this `Weak<T>`.
3079    ///
3080    /// The pointer is valid only if there are some strong references. The pointer may be dangling,
3081    /// unaligned or even [`null`] otherwise.
3082    ///
3083    /// # Examples
3084    ///
3085    /// ```
3086    /// use std::sync::Arc;
3087    /// use std::ptr;
3088    ///
3089    /// let strong = Arc::new("hello".to_owned());
3090    /// let weak = Arc::downgrade(&strong);
3091    /// // Both point to the same object
3092    /// assert!(ptr::eq(&*strong, weak.as_ptr()));
3093    /// // The strong here keeps it alive, so we can still access the object.
3094    /// assert_eq!("hello", unsafe { &*weak.as_ptr() });
3095    ///
3096    /// drop(strong);
3097    /// // But not any more. We can do weak.as_ptr(), but accessing the pointer would lead to
3098    /// // undefined behavior.
3099    /// // assert_eq!("hello", unsafe { &*weak.as_ptr() });
3100    /// ```
3101    ///
3102    /// [`null`]: core::ptr::null "ptr::null"
3103    #[must_use]
3104    #[stable(feature = "weak_into_raw", since = "1.45.0")]
3105    pub fn as_ptr(&self) -> *const T {
3106        let ptr: *mut ArcInner<T> = NonNull::as_ptr(self.ptr);
3107
3108        if is_dangling(ptr) {
3109            // If the pointer is dangling, we return the sentinel directly. This cannot be
3110            // a valid payload address, as the payload is at least as aligned as ArcInner (usize).
3111            ptr as *const T
3112        } else {
3113            // SAFETY: if is_dangling returns false, then the pointer is dereferenceable.
3114            // The payload may be dropped at this point, and we have to maintain provenance,
3115            // so use raw pointer manipulation.
3116            unsafe { &raw mut (*ptr).data }
3117        }
3118    }
3119
3120    /// Consumes the `Weak<T>`, returning the wrapped pointer and allocator.
3121    ///
3122    /// This converts the weak pointer into a raw pointer, while still preserving the ownership of
3123    /// one weak reference (the weak count is not modified by this operation). It can be turned
3124    /// back into the `Weak<T>` with [`from_raw_in`].
3125    ///
3126    /// The same restrictions of accessing the target of the pointer as with
3127    /// [`as_ptr`] apply.
3128    ///
3129    /// # Examples
3130    ///
3131    /// ```
3132    /// #![feature(allocator_api)]
3133    /// use std::sync::{Arc, Weak};
3134    /// use std::alloc::System;
3135    ///
3136    /// let strong = Arc::new_in("hello".to_owned(), System);
3137    /// let weak = Arc::downgrade(&strong);
3138    /// let (raw, alloc) = weak.into_raw_with_allocator();
3139    ///
3140    /// assert_eq!(1, Arc::weak_count(&strong));
3141    /// assert_eq!("hello", unsafe { &*raw });
3142    ///
3143    /// drop(unsafe { Weak::from_raw_in(raw, alloc) });
3144    /// assert_eq!(0, Arc::weak_count(&strong));
3145    /// ```
3146    ///
3147    /// [`from_raw_in`]: Weak::from_raw_in
3148    /// [`as_ptr`]: Weak::as_ptr
3149    #[must_use = "losing the pointer will leak memory"]
3150    #[unstable(feature = "allocator_api", issue = "32838")]
3151    pub fn into_raw_with_allocator(self) -> (*const T, A) {
3152        let this = mem::ManuallyDrop::new(self);
3153        let result = this.as_ptr();
3154        // Safety: `this` is ManuallyDrop so the allocator will not be double-dropped
3155        let alloc = unsafe { ptr::read(&this.alloc) };
3156        (result, alloc)
3157    }
3158
3159    /// Converts a raw pointer previously created by [`into_raw`] back into `Weak<T>` in the provided
3160    /// allocator.
3161    ///
3162    /// This can be used to safely get a strong reference (by calling [`upgrade`]
3163    /// later) or to deallocate the weak count by dropping the `Weak<T>`.
3164    ///
3165    /// It takes ownership of one weak reference (with the exception of pointers created by [`new`],
3166    /// as these don't own anything; the method still works on them).
3167    ///
3168    /// # Safety
3169    ///
3170    /// The pointer must have originated from the [`into_raw`] and must still own its potential
3171    /// weak reference, and must point to a block of memory allocated by `alloc`.
3172    ///
3173    /// It is allowed for the strong count to be 0 at the time of calling this. Nevertheless, this
3174    /// takes ownership of one weak reference currently represented as a raw pointer (the weak
3175    /// count is not modified by this operation) and therefore it must be paired with a previous
3176    /// call to [`into_raw`].
3177    /// # Examples
3178    ///
3179    /// ```
3180    /// use std::sync::{Arc, Weak};
3181    ///
3182    /// let strong = Arc::new("hello".to_owned());
3183    ///
3184    /// let raw_1 = Arc::downgrade(&strong).into_raw();
3185    /// let raw_2 = Arc::downgrade(&strong).into_raw();
3186    ///
3187    /// assert_eq!(2, Arc::weak_count(&strong));
3188    ///
3189    /// assert_eq!("hello", &*unsafe { Weak::from_raw(raw_1) }.upgrade().unwrap());
3190    /// assert_eq!(1, Arc::weak_count(&strong));
3191    ///
3192    /// drop(strong);
3193    ///
3194    /// // Decrement the last weak count.
3195    /// assert!(unsafe { Weak::from_raw(raw_2) }.upgrade().is_none());
3196    /// ```
3197    ///
3198    /// [`new`]: Weak::new
3199    /// [`into_raw`]: Weak::into_raw
3200    /// [`upgrade`]: Weak::upgrade
3201    #[inline]
3202    #[unstable(feature = "allocator_api", issue = "32838")]
3203    pub unsafe fn from_raw_in(ptr: *const T, alloc: A) -> Self {
3204        // See Weak::as_ptr for context on how the input pointer is derived.
3205
3206        let ptr = if is_dangling(ptr) {
3207            // This is a dangling Weak.
3208            ptr as *mut ArcInner<T>
3209        } else {
3210            // Otherwise, we're guaranteed the pointer came from a nondangling Weak.
3211            // SAFETY: data_offset is safe to call, as ptr references a real (potentially dropped) T.
3212            let offset = unsafe { data_offset(ptr) };
3213            // Thus, we reverse the offset to get the whole ArcInner.
3214            // SAFETY: the pointer originated from a Weak, so this offset is safe.
3215            unsafe { ptr.byte_sub(offset) as *mut ArcInner<T> }
3216        };
3217
3218        // SAFETY: we now have recovered the original Weak pointer, so can create the Weak.
3219        Weak { ptr: unsafe { NonNull::new_unchecked(ptr) }, alloc }
3220    }
3221}
3222
3223impl<T: ?Sized, A: Allocator> Weak<T, A> {
3224    /// Attempts to upgrade the `Weak` pointer to an [`Arc`], delaying
3225    /// dropping of the inner value if successful.
3226    ///
3227    /// Returns [`None`] if the inner value has since been dropped.
3228    ///
3229    /// # Examples
3230    ///
3231    /// ```
3232    /// use std::sync::Arc;
3233    ///
3234    /// let five = Arc::new(5);
3235    ///
3236    /// let weak_five = Arc::downgrade(&five);
3237    ///
3238    /// let strong_five: Option<Arc<_>> = weak_five.upgrade();
3239    /// assert!(strong_five.is_some());
3240    ///
3241    /// // Destroy all strong pointers.
3242    /// drop(strong_five);
3243    /// drop(five);
3244    ///
3245    /// assert!(weak_five.upgrade().is_none());
3246    /// ```
3247    #[must_use = "this returns a new `Arc`, \
3248                  without modifying the original weak pointer"]
3249    #[stable(feature = "arc_weak", since = "1.4.0")]
3250    pub fn upgrade(&self) -> Option<Arc<T, A>>
3251    where
3252        A: Clone,
3253    {
3254        #[inline]
3255        fn checked_increment(n: usize) -> Option<usize> {
3256            // Any write of 0 we can observe leaves the field in permanently zero state.
3257            if n == 0 {
3258                return None;
3259            }
3260            // See comments in `Arc::clone` for why we do this (for `mem::forget`).
3261            assert!(n <= MAX_REFCOUNT, "{}", INTERNAL_OVERFLOW_ERROR);
3262            Some(n + 1)
3263        }
3264
3265        // We use a CAS loop to increment the strong count instead of a
3266        // fetch_add as this function should never take the reference count
3267        // from zero to one.
3268        //
3269        // Relaxed is fine for the failure case because we don't have any expectations about the new state.
3270        // Acquire is necessary for the success case to synchronise with `Arc::new_cyclic`, when the inner
3271        // value can be initialized after `Weak` references have already been created. In that case, we
3272        // expect to observe the fully initialized value.
3273        if self.inner()?.strong.try_update(Acquire, Relaxed, checked_increment).is_ok() {
3274            // SAFETY: pointer is not null, verified in checked_increment
3275            unsafe { Some(Arc::from_inner_in(self.ptr, self.alloc.clone())) }
3276        } else {
3277            None
3278        }
3279    }
3280
3281    /// Gets the number of strong (`Arc`) pointers pointing to this allocation.
3282    ///
3283    /// If `self` was created using [`Weak::new`], this will return 0.
3284    #[must_use]
3285    #[stable(feature = "weak_counts", since = "1.41.0")]
3286    pub fn strong_count(&self) -> usize {
3287        if let Some(inner) = self.inner() { inner.strong.load(Relaxed) } else { 0 }
3288    }
3289
3290    /// Gets an approximation of the number of `Weak` pointers pointing to this
3291    /// allocation.
3292    ///
3293    /// If `self` was created using [`Weak::new`], or if there are no remaining
3294    /// strong pointers, this will return 0.
3295    ///
3296    /// # Accuracy
3297    ///
3298    /// Due to implementation details, the returned value can be off by 1 in
3299    /// either direction when other threads are manipulating any `Arc`s or
3300    /// `Weak`s pointing to the same allocation.
3301    #[must_use]
3302    #[stable(feature = "weak_counts", since = "1.41.0")]
3303    pub fn weak_count(&self) -> usize {
3304        if let Some(inner) = self.inner() {
3305            let weak = inner.weak.load(Acquire);
3306            let strong = inner.strong.load(Relaxed);
3307            if strong == 0 {
3308                0
3309            } else {
3310                // Since we observed that there was at least one strong pointer
3311                // after reading the weak count, we know that the implicit weak
3312                // reference (present whenever any strong references are alive)
3313                // was still around when we observed the weak count, and can
3314                // therefore safely subtract it.
3315                weak - 1
3316            }
3317        } else {
3318            0
3319        }
3320    }
3321
3322    /// Returns `None` when the pointer is dangling and there is no allocated `ArcInner`,
3323    /// (i.e., when this `Weak` was created by `Weak::new`).
3324    #[inline]
3325    fn inner(&self) -> Option<WeakInner<'_>> {
3326        let ptr = self.ptr.as_ptr();
3327        if is_dangling(ptr) {
3328            None
3329        } else {
3330            // We are careful to *not* create a reference covering the "data" field, as
3331            // the field may be mutated concurrently (for example, if the last `Arc`
3332            // is dropped, the data field will be dropped in-place).
3333            Some(unsafe { WeakInner { strong: &(*ptr).strong, weak: &(*ptr).weak } })
3334        }
3335    }
3336
3337    /// Returns `true` if the two `Weak`s point to the same allocation similar to [`ptr::eq`], or if
3338    /// both don't point to any allocation (because they were created with `Weak::new()`). However,
3339    /// this function ignores the metadata of  `dyn Trait` pointers.
3340    ///
3341    /// # Notes
3342    ///
3343    /// Since this compares pointers it means that `Weak::new()` will equal each
3344    /// other, even though they don't point to any allocation.
3345    ///
3346    /// # Examples
3347    ///
3348    /// ```
3349    /// use std::sync::Arc;
3350    ///
3351    /// let first_rc = Arc::new(5);
3352    /// let first = Arc::downgrade(&first_rc);
3353    /// let second = Arc::downgrade(&first_rc);
3354    ///
3355    /// assert!(first.ptr_eq(&second));
3356    ///
3357    /// let third_rc = Arc::new(5);
3358    /// let third = Arc::downgrade(&third_rc);
3359    ///
3360    /// assert!(!first.ptr_eq(&third));
3361    /// ```
3362    ///
3363    /// Comparing `Weak::new`.
3364    ///
3365    /// ```
3366    /// use std::sync::{Arc, Weak};
3367    ///
3368    /// let first = Weak::new();
3369    /// let second = Weak::new();
3370    /// assert!(first.ptr_eq(&second));
3371    ///
3372    /// let third_rc = Arc::new(());
3373    /// let third = Arc::downgrade(&third_rc);
3374    /// assert!(!first.ptr_eq(&third));
3375    /// ```
3376    ///
3377    /// [`ptr::eq`]: core::ptr::eq "ptr::eq"
3378    #[inline]
3379    #[must_use]
3380    #[stable(feature = "weak_ptr_eq", since = "1.39.0")]
3381    pub fn ptr_eq(&self, other: &Self) -> bool {
3382        ptr::addr_eq(self.ptr.as_ptr(), other.ptr.as_ptr())
3383    }
3384}
3385
3386#[stable(feature = "arc_weak", since = "1.4.0")]
3387impl<T: ?Sized, A: Allocator + Clone> Clone for Weak<T, A> {
3388    /// Makes a clone of the `Weak` pointer that points to the same allocation.
3389    ///
3390    /// # Examples
3391    ///
3392    /// ```
3393    /// use std::sync::{Arc, Weak};
3394    ///
3395    /// let weak_five = Arc::downgrade(&Arc::new(5));
3396    ///
3397    /// let _ = Weak::clone(&weak_five);
3398    /// ```
3399    #[inline]
3400    fn clone(&self) -> Weak<T, A> {
3401        if let Some(inner) = self.inner() {
3402            // See comments in Arc::clone() for why this is relaxed. This can use a
3403            // fetch_add (ignoring the lock) because the weak count is only locked
3404            // where are *no other* weak pointers in existence. (So we can't be
3405            // running this code in that case).
3406            let old_size = inner.weak.fetch_add(1, Relaxed);
3407
3408            // See comments in Arc::clone() for why we do this (for mem::forget).
3409            if old_size > MAX_REFCOUNT {
3410                abort();
3411            }
3412        }
3413
3414        Weak { ptr: self.ptr, alloc: self.alloc.clone() }
3415    }
3416}
3417
3418#[unstable(feature = "ergonomic_clones", issue = "132290")]
3419impl<T: ?Sized, A: Allocator + Clone> UseCloned for Weak<T, A> {}
3420
3421#[stable(feature = "downgraded_weak", since = "1.10.0")]
3422impl<T> Default for Weak<T> {
3423    /// Constructs a new `Weak<T>`, without allocating memory.
3424    /// Calling [`upgrade`] on the return value always
3425    /// gives [`None`].
3426    ///
3427    /// [`upgrade`]: Weak::upgrade
3428    ///
3429    /// # Examples
3430    ///
3431    /// ```
3432    /// use std::sync::Weak;
3433    ///
3434    /// let empty: Weak<i64> = Default::default();
3435    /// assert!(empty.upgrade().is_none());
3436    /// ```
3437    fn default() -> Weak<T> {
3438        Weak::new()
3439    }
3440}
3441
3442#[stable(feature = "arc_weak", since = "1.4.0")]
3443unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for Weak<T, A> {
3444    /// Drops the `Weak` pointer.
3445    ///
3446    /// # Examples
3447    ///
3448    /// ```
3449    /// use std::sync::{Arc, Weak};
3450    ///
3451    /// struct Foo;
3452    ///
3453    /// impl Drop for Foo {
3454    ///     fn drop(&mut self) {
3455    ///         println!("dropped!");
3456    ///     }
3457    /// }
3458    ///
3459    /// let foo = Arc::new(Foo);
3460    /// let weak_foo = Arc::downgrade(&foo);
3461    /// let other_weak_foo = Weak::clone(&weak_foo);
3462    ///
3463    /// drop(weak_foo);   // Doesn't print anything
3464    /// drop(foo);        // Prints "dropped!"
3465    ///
3466    /// assert!(other_weak_foo.upgrade().is_none());
3467    /// ```
3468    fn drop(&mut self) {
3469        // If we find out that we were the last weak pointer, then its time to
3470        // deallocate the data entirely. See the discussion in Arc::drop() about
3471        // the memory orderings
3472        //
3473        // It's not necessary to check for the locked state here, because the
3474        // weak count can only be locked if there was precisely one weak ref,
3475        // meaning that drop could only subsequently run ON that remaining weak
3476        // ref, which can only happen after the lock is released.
3477        let inner = if let Some(inner) = self.inner() { inner } else { return };
3478
3479        if inner.weak.fetch_sub(1, Release) == 1 {
3480            acquire!(inner.weak);
3481
3482            // Make sure we aren't trying to "deallocate" the shared static for empty slices
3483            // used by Default::default.
3484            debug_assert!(
3485                !ptr::addr_eq(self.ptr.as_ptr(), &STATIC_INNER_SLICE.inner),
3486                "Arc/Weaks backed by a static should never be deallocated. \
3487                Likely decrement_strong_count or from_raw were called too many times.",
3488            );
3489
3490            unsafe {
3491                self.alloc.deallocate(self.ptr.cast(), Layout::for_value_raw(self.ptr.as_ptr()))
3492            }
3493        }
3494    }
3495}
3496
3497#[stable(feature = "rust1", since = "1.0.0")]
3498trait ArcEqIdent<T: ?Sized + PartialEq, A: Allocator> {
3499    fn eq(&self, other: &Arc<T, A>) -> bool;
3500    fn ne(&self, other: &Arc<T, A>) -> bool;
3501}
3502
3503#[stable(feature = "rust1", since = "1.0.0")]
3504impl<T: ?Sized + PartialEq, A: Allocator> ArcEqIdent<T, A> for Arc<T, A> {
3505    #[inline]
3506    default fn eq(&self, other: &Arc<T, A>) -> bool {
3507        **self == **other
3508    }
3509    #[inline]
3510    default fn ne(&self, other: &Arc<T, A>) -> bool {
3511        **self != **other
3512    }
3513}
3514
3515/// We're doing this specialization here, and not as a more general optimization on `&T`, because it
3516/// would otherwise add a cost to all equality checks on refs. We assume that `Arc`s are used to
3517/// store large values, that are slow to clone, but also heavy to check for equality, causing this
3518/// cost to pay off more easily. It's also more likely to have two `Arc` clones, that point to
3519/// the same value, than two `&T`s.
3520///
3521/// We can only do this when `T: Eq` as a `PartialEq` might be deliberately irreflexive.
3522#[stable(feature = "rust1", since = "1.0.0")]
3523impl<T: ?Sized + crate::rc::MarkerEq, A: Allocator> ArcEqIdent<T, A> for Arc<T, A> {
3524    #[inline]
3525    fn eq(&self, other: &Arc<T, A>) -> bool {
3526        Arc::ptr_eq(self, other) || **self == **other
3527    }
3528
3529    #[inline]
3530    fn ne(&self, other: &Arc<T, A>) -> bool {
3531        !Arc::ptr_eq(self, other) && **self != **other
3532    }
3533}
3534
3535#[stable(feature = "rust1", since = "1.0.0")]
3536impl<T: ?Sized + PartialEq, A: Allocator> PartialEq for Arc<T, A> {
3537    /// Equality for two `Arc`s.
3538    ///
3539    /// Two `Arc`s are equal if their inner values are equal, even if they are
3540    /// stored in different allocation.
3541    ///
3542    /// If `T` also implements `Eq` (implying reflexivity of equality),
3543    /// two `Arc`s that point to the same allocation are always equal.
3544    ///
3545    /// # Examples
3546    ///
3547    /// ```
3548    /// use std::sync::Arc;
3549    ///
3550    /// let five = Arc::new(5);
3551    ///
3552    /// assert!(five == Arc::new(5));
3553    /// ```
3554    #[inline]
3555    fn eq(&self, other: &Arc<T, A>) -> bool {
3556        ArcEqIdent::eq(self, other)
3557    }
3558
3559    /// Inequality for two `Arc`s.
3560    ///
3561    /// Two `Arc`s are not equal if their inner values are not equal.
3562    ///
3563    /// If `T` also implements `Eq` (implying reflexivity of equality),
3564    /// two `Arc`s that point to the same value are always equal.
3565    ///
3566    /// # Examples
3567    ///
3568    /// ```
3569    /// use std::sync::Arc;
3570    ///
3571    /// let five = Arc::new(5);
3572    ///
3573    /// assert!(five != Arc::new(6));
3574    /// ```
3575    #[inline]
3576    fn ne(&self, other: &Arc<T, A>) -> bool {
3577        ArcEqIdent::ne(self, other)
3578    }
3579}
3580
3581#[stable(feature = "rust1", since = "1.0.0")]
3582impl<T: ?Sized + PartialOrd, A: Allocator> PartialOrd for Arc<T, A> {
3583    /// Partial comparison for two `Arc`s.
3584    ///
3585    /// The two are compared by calling `partial_cmp()` on their inner values.
3586    ///
3587    /// # Examples
3588    ///
3589    /// ```
3590    /// use std::sync::Arc;
3591    /// use std::cmp::Ordering;
3592    ///
3593    /// let five = Arc::new(5);
3594    ///
3595    /// assert_eq!(Some(Ordering::Less), five.partial_cmp(&Arc::new(6)));
3596    /// ```
3597    fn partial_cmp(&self, other: &Arc<T, A>) -> Option<Ordering> {
3598        (**self).partial_cmp(&**other)
3599    }
3600
3601    /// Less-than comparison for two `Arc`s.
3602    ///
3603    /// The two are compared by calling `<` on their inner values.
3604    ///
3605    /// # Examples
3606    ///
3607    /// ```
3608    /// use std::sync::Arc;
3609    ///
3610    /// let five = Arc::new(5);
3611    ///
3612    /// assert!(five < Arc::new(6));
3613    /// ```
3614    fn lt(&self, other: &Arc<T, A>) -> bool {
3615        *(*self) < *(*other)
3616    }
3617
3618    /// 'Less than or equal to' comparison for two `Arc`s.
3619    ///
3620    /// The two are compared by calling `<=` on their inner values.
3621    ///
3622    /// # Examples
3623    ///
3624    /// ```
3625    /// use std::sync::Arc;
3626    ///
3627    /// let five = Arc::new(5);
3628    ///
3629    /// assert!(five <= Arc::new(5));
3630    /// ```
3631    fn le(&self, other: &Arc<T, A>) -> bool {
3632        *(*self) <= *(*other)
3633    }
3634
3635    /// Greater-than comparison for two `Arc`s.
3636    ///
3637    /// The two are compared by calling `>` on their inner values.
3638    ///
3639    /// # Examples
3640    ///
3641    /// ```
3642    /// use std::sync::Arc;
3643    ///
3644    /// let five = Arc::new(5);
3645    ///
3646    /// assert!(five > Arc::new(4));
3647    /// ```
3648    fn gt(&self, other: &Arc<T, A>) -> bool {
3649        *(*self) > *(*other)
3650    }
3651
3652    /// 'Greater than or equal to' comparison for two `Arc`s.
3653    ///
3654    /// The two are compared by calling `>=` on their inner values.
3655    ///
3656    /// # Examples
3657    ///
3658    /// ```
3659    /// use std::sync::Arc;
3660    ///
3661    /// let five = Arc::new(5);
3662    ///
3663    /// assert!(five >= Arc::new(5));
3664    /// ```
3665    fn ge(&self, other: &Arc<T, A>) -> bool {
3666        *(*self) >= *(*other)
3667    }
3668}
3669#[stable(feature = "rust1", since = "1.0.0")]
3670impl<T: ?Sized + Ord, A: Allocator> Ord for Arc<T, A> {
3671    /// Comparison for two `Arc`s.
3672    ///
3673    /// The two are compared by calling `cmp()` on their inner values.
3674    ///
3675    /// # Examples
3676    ///
3677    /// ```
3678    /// use std::sync::Arc;
3679    /// use std::cmp::Ordering;
3680    ///
3681    /// let five = Arc::new(5);
3682    ///
3683    /// assert_eq!(Ordering::Less, five.cmp(&Arc::new(6)));
3684    /// ```
3685    fn cmp(&self, other: &Arc<T, A>) -> Ordering {
3686        (**self).cmp(&**other)
3687    }
3688}
3689#[stable(feature = "rust1", since = "1.0.0")]
3690impl<T: ?Sized + Eq, A: Allocator> Eq for Arc<T, A> {}
3691
3692#[stable(feature = "rust1", since = "1.0.0")]
3693impl<T: ?Sized + fmt::Display, A: Allocator> fmt::Display for Arc<T, A> {
3694    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3695        fmt::Display::fmt(&**self, f)
3696    }
3697}
3698
3699#[stable(feature = "rust1", since = "1.0.0")]
3700impl<T: ?Sized + fmt::Debug, A: Allocator> fmt::Debug for Arc<T, A> {
3701    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3702        fmt::Debug::fmt(&**self, f)
3703    }
3704}
3705
3706#[stable(feature = "rust1", since = "1.0.0")]
3707impl<T: ?Sized, A: Allocator> fmt::Pointer for Arc<T, A> {
3708    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3709        fmt::Pointer::fmt(&(&raw const **self), f)
3710    }
3711}
3712
3713#[cfg(not(no_global_oom_handling))]
3714#[stable(feature = "rust1", since = "1.0.0")]
3715impl<T: Default> Default for Arc<T> {
3716    /// Creates a new `Arc<T>`, with the `Default` value for `T`.
3717    ///
3718    /// # Examples
3719    ///
3720    /// ```
3721    /// use std::sync::Arc;
3722    ///
3723    /// let x: Arc<i32> = Default::default();
3724    /// assert_eq!(*x, 0);
3725    /// ```
3726    fn default() -> Arc<T> {
3727        unsafe {
3728            Self::from_inner(
3729                Box::leak(Box::write(
3730                    Box::new_uninit(),
3731                    ArcInner {
3732                        strong: atomic::AtomicUsize::new(1),
3733                        weak: atomic::AtomicUsize::new(1),
3734                        data: T::default(),
3735                    },
3736                ))
3737                .into(),
3738            )
3739        }
3740    }
3741}
3742
3743/// Struct to hold the static `ArcInner` used for empty `Arc<str/CStr/[T]>` as
3744/// returned by `Default::default`.
3745///
3746/// Layout notes:
3747/// * `repr(align(16))` so we can use it for `[T]` with `align_of::<T>() <= 16`.
3748/// * `repr(C)` so `inner` is at offset 0 (and thus guaranteed to actually be aligned to 16).
3749/// * `[u8; 1]` (to be initialized with 0) so it can be used for `Arc<CStr>`.
3750#[repr(C, align(16))]
3751struct SliceArcInnerForStatic {
3752    inner: ArcInner<[u8; 1]>,
3753}
3754#[cfg(not(no_global_oom_handling))]
3755const MAX_STATIC_INNER_SLICE_ALIGNMENT: usize = 16;
3756
3757static STATIC_INNER_SLICE: SliceArcInnerForStatic = SliceArcInnerForStatic {
3758    inner: ArcInner {
3759        strong: atomic::AtomicUsize::new(1),
3760        weak: atomic::AtomicUsize::new(1),
3761        data: [0],
3762    },
3763};
3764
3765#[cfg(not(no_global_oom_handling))]
3766#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
3767impl Default for Arc<str> {
3768    /// Creates an empty str inside an Arc
3769    ///
3770    /// This may or may not share an allocation with other Arcs.
3771    #[inline]
3772    fn default() -> Self {
3773        let arc: Arc<[u8]> = Default::default();
3774        debug_assert!(core::str::from_utf8(&*arc).is_ok());
3775        let (ptr, alloc) = Arc::into_inner_with_allocator(arc);
3776        unsafe { Arc::from_ptr_in(ptr.as_ptr() as *mut ArcInner<str>, alloc) }
3777    }
3778}
3779
3780#[cfg(not(no_global_oom_handling))]
3781#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
3782impl Default for Arc<core::ffi::CStr> {
3783    /// Creates an empty CStr inside an Arc
3784    ///
3785    /// This may or may not share an allocation with other Arcs.
3786    #[inline]
3787    fn default() -> Self {
3788        use core::ffi::CStr;
3789        let inner: NonNull<ArcInner<[u8]>> = NonNull::from(&STATIC_INNER_SLICE.inner);
3790        let inner: NonNull<ArcInner<CStr>> =
3791            NonNull::new(inner.as_ptr() as *mut ArcInner<CStr>).unwrap();
3792        // `this` semantically is the Arc "owned" by the static, so make sure not to drop it.
3793        let this: mem::ManuallyDrop<Arc<CStr>> =
3794            unsafe { mem::ManuallyDrop::new(Arc::from_inner(inner)) };
3795        (*this).clone()
3796    }
3797}
3798
3799#[cfg(not(no_global_oom_handling))]
3800#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
3801impl<T> Default for Arc<[T]> {
3802    /// Creates an empty `[T]` inside an Arc
3803    ///
3804    /// This may or may not share an allocation with other Arcs.
3805    #[inline]
3806    fn default() -> Self {
3807        if align_of::<T>() <= MAX_STATIC_INNER_SLICE_ALIGNMENT {
3808            // We take a reference to the whole struct instead of the ArcInner<[u8; 1]> inside it so
3809            // we don't shrink the range of bytes the ptr is allowed to access under Stacked Borrows.
3810            // (Miri complains on 32-bit targets with Arc<[Align16]> otherwise.)
3811            // (Note that NonNull::from(&STATIC_INNER_SLICE.inner) is fine under Tree Borrows.)
3812            let inner: NonNull<SliceArcInnerForStatic> = NonNull::from(&STATIC_INNER_SLICE);
3813            let inner: NonNull<ArcInner<[T; 0]>> = inner.cast();
3814            // `this` semantically is the Arc "owned" by the static, so make sure not to drop it.
3815            let this: mem::ManuallyDrop<Arc<[T; 0]>> =
3816                unsafe { mem::ManuallyDrop::new(Arc::from_inner(inner)) };
3817            return (*this).clone();
3818        }
3819
3820        // If T's alignment is too large for the static, make a new unique allocation.
3821        let arr: [T; 0] = [];
3822        Arc::from(arr)
3823    }
3824}
3825
3826#[cfg(not(no_global_oom_handling))]
3827#[stable(feature = "pin_default_impls", since = "1.91.0")]
3828impl<T> Default for Pin<Arc<T>>
3829where
3830    T: ?Sized,
3831    Arc<T>: Default,
3832{
3833    #[inline]
3834    fn default() -> Self {
3835        unsafe { Pin::new_unchecked(Arc::<T>::default()) }
3836    }
3837}
3838
3839#[stable(feature = "rust1", since = "1.0.0")]
3840impl<T: ?Sized + Hash, A: Allocator> Hash for Arc<T, A> {
3841    fn hash<H: Hasher>(&self, state: &mut H) {
3842        (**self).hash(state)
3843    }
3844}
3845
3846#[cfg(not(no_global_oom_handling))]
3847#[stable(feature = "from_for_ptrs", since = "1.6.0")]
3848impl<T> From<T> for Arc<T> {
3849    /// Converts a `T` into an `Arc<T>`
3850    ///
3851    /// The conversion moves the value into a
3852    /// newly allocated `Arc`. It is equivalent to
3853    /// calling `Arc::new(t)`.
3854    ///
3855    /// # Example
3856    /// ```rust
3857    /// # use std::sync::Arc;
3858    /// let x = 5;
3859    /// let arc = Arc::new(5);
3860    ///
3861    /// assert_eq!(Arc::from(x), arc);
3862    /// ```
3863    fn from(t: T) -> Self {
3864        Arc::new(t)
3865    }
3866}
3867
3868#[cfg(not(no_global_oom_handling))]
3869#[stable(feature = "shared_from_array", since = "1.74.0")]
3870impl<T, const N: usize> From<[T; N]> for Arc<[T]> {
3871    /// Converts a [`[T; N]`](prim@array) into an `Arc<[T]>`.
3872    ///
3873    /// The conversion moves the array into a newly allocated `Arc`.
3874    ///
3875    /// # Example
3876    ///
3877    /// ```
3878    /// # use std::sync::Arc;
3879    /// let original: [i32; 3] = [1, 2, 3];
3880    /// let shared: Arc<[i32]> = Arc::from(original);
3881    /// assert_eq!(&[1, 2, 3], &shared[..]);
3882    /// ```
3883    #[inline]
3884    fn from(v: [T; N]) -> Arc<[T]> {
3885        Arc::<[T; N]>::from(v)
3886    }
3887}
3888
3889#[cfg(not(no_global_oom_handling))]
3890#[stable(feature = "shared_from_slice", since = "1.21.0")]
3891impl<T: Clone> From<&[T]> for Arc<[T]> {
3892    /// Allocates a reference-counted slice and fills it by cloning `v`'s items.
3893    ///
3894    /// # Example
3895    ///
3896    /// ```
3897    /// # use std::sync::Arc;
3898    /// let original: &[i32] = &[1, 2, 3];
3899    /// let shared: Arc<[i32]> = Arc::from(original);
3900    /// assert_eq!(&[1, 2, 3], &shared[..]);
3901    /// ```
3902    #[inline]
3903    fn from(v: &[T]) -> Arc<[T]> {
3904        <Self as ArcFromSlice<T>>::from_slice(v)
3905    }
3906}
3907
3908#[cfg(not(no_global_oom_handling))]
3909#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
3910impl<T: Clone> From<&mut [T]> for Arc<[T]> {
3911    /// Allocates a reference-counted slice and fills it by cloning `v`'s items.
3912    ///
3913    /// # Example
3914    ///
3915    /// ```
3916    /// # use std::sync::Arc;
3917    /// let mut original = [1, 2, 3];
3918    /// let original: &mut [i32] = &mut original;
3919    /// let shared: Arc<[i32]> = Arc::from(original);
3920    /// assert_eq!(&[1, 2, 3], &shared[..]);
3921    /// ```
3922    #[inline]
3923    fn from(v: &mut [T]) -> Arc<[T]> {
3924        Arc::from(&*v)
3925    }
3926}
3927
3928#[cfg(not(no_global_oom_handling))]
3929#[stable(feature = "shared_from_slice", since = "1.21.0")]
3930impl From<&str> for Arc<str> {
3931    /// Allocates a reference-counted `str` and copies `v` into it.
3932    ///
3933    /// # Example
3934    ///
3935    /// ```
3936    /// # use std::sync::Arc;
3937    /// let shared: Arc<str> = Arc::from("eggplant");
3938    /// assert_eq!("eggplant", &shared[..]);
3939    /// ```
3940    #[inline]
3941    fn from(v: &str) -> Arc<str> {
3942        let arc = Arc::<[u8]>::from(v.as_bytes());
3943        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const str) }
3944    }
3945}
3946
3947#[cfg(not(no_global_oom_handling))]
3948#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
3949impl From<&mut str> for Arc<str> {
3950    /// Allocates a reference-counted `str` and copies `v` into it.
3951    ///
3952    /// # Example
3953    ///
3954    /// ```
3955    /// # use std::sync::Arc;
3956    /// let mut original = String::from("eggplant");
3957    /// let original: &mut str = &mut original;
3958    /// let shared: Arc<str> = Arc::from(original);
3959    /// assert_eq!("eggplant", &shared[..]);
3960    /// ```
3961    #[inline]
3962    fn from(v: &mut str) -> Arc<str> {
3963        Arc::from(&*v)
3964    }
3965}
3966
3967#[cfg(not(no_global_oom_handling))]
3968#[stable(feature = "shared_from_slice", since = "1.21.0")]
3969impl From<String> for Arc<str> {
3970    /// Allocates a reference-counted `str` and copies `v` into it.
3971    ///
3972    /// # Example
3973    ///
3974    /// ```
3975    /// # use std::sync::Arc;
3976    /// let unique: String = "eggplant".to_owned();
3977    /// let shared: Arc<str> = Arc::from(unique);
3978    /// assert_eq!("eggplant", &shared[..]);
3979    /// ```
3980    #[inline]
3981    fn from(v: String) -> Arc<str> {
3982        Arc::from(&v[..])
3983    }
3984}
3985
3986#[cfg(not(no_global_oom_handling))]
3987#[stable(feature = "shared_from_slice", since = "1.21.0")]
3988impl<T: ?Sized, A: Allocator> From<Box<T, A>> for Arc<T, A> {
3989    /// Move a boxed object to a new, reference-counted allocation.
3990    ///
3991    /// # Example
3992    ///
3993    /// ```
3994    /// # use std::sync::Arc;
3995    /// let unique: Box<str> = Box::from("eggplant");
3996    /// let shared: Arc<str> = Arc::from(unique);
3997    /// assert_eq!("eggplant", &shared[..]);
3998    /// ```
3999    #[inline]
4000    fn from(v: Box<T, A>) -> Arc<T, A> {
4001        Arc::from_box_in(v)
4002    }
4003}
4004
4005#[cfg(not(no_global_oom_handling))]
4006#[stable(feature = "shared_from_slice", since = "1.21.0")]
4007impl<T, A: Allocator + Clone> From<Vec<T, A>> for Arc<[T], A> {
4008    /// Allocates a reference-counted slice and moves `v`'s items into it.
4009    ///
4010    /// # Example
4011    ///
4012    /// ```
4013    /// # use std::sync::Arc;
4014    /// let unique: Vec<i32> = vec![1, 2, 3];
4015    /// let shared: Arc<[i32]> = Arc::from(unique);
4016    /// assert_eq!(&[1, 2, 3], &shared[..]);
4017    /// ```
4018    #[inline]
4019    fn from(v: Vec<T, A>) -> Arc<[T], A> {
4020        unsafe {
4021            let (vec_ptr, len, cap, alloc) = v.into_raw_parts_with_alloc();
4022
4023            let rc_ptr = Self::allocate_for_slice_in(len, &alloc);
4024            ptr::copy_nonoverlapping(vec_ptr, (&raw mut (*rc_ptr).data) as *mut T, len);
4025
4026            // Create a `Vec<T, &A>` with length 0, to deallocate the buffer
4027            // without dropping its contents or the allocator
4028            let _ = Vec::from_raw_parts_in(vec_ptr, 0, cap, &alloc);
4029
4030            Self::from_ptr_in(rc_ptr, alloc)
4031        }
4032    }
4033}
4034
4035#[stable(feature = "shared_from_cow", since = "1.45.0")]
4036impl<'a, B> From<Cow<'a, B>> for Arc<B>
4037where
4038    B: ToOwned + ?Sized,
4039    Arc<B>: From<&'a B> + From<B::Owned>,
4040{
4041    /// Creates an atomically reference-counted pointer from a clone-on-write
4042    /// pointer by copying its content.
4043    ///
4044    /// # Example
4045    ///
4046    /// ```rust
4047    /// # use std::sync::Arc;
4048    /// # use std::borrow::Cow;
4049    /// let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
4050    /// let shared: Arc<str> = Arc::from(cow);
4051    /// assert_eq!("eggplant", &shared[..]);
4052    /// ```
4053    #[inline]
4054    fn from(cow: Cow<'a, B>) -> Arc<B> {
4055        match cow {
4056            Cow::Borrowed(s) => Arc::from(s),
4057            Cow::Owned(s) => Arc::from(s),
4058        }
4059    }
4060}
4061
4062#[stable(feature = "shared_from_str", since = "1.62.0")]
4063impl From<Arc<str>> for Arc<[u8]> {
4064    /// Converts an atomically reference-counted string slice into a byte slice.
4065    ///
4066    /// # Example
4067    ///
4068    /// ```
4069    /// # use std::sync::Arc;
4070    /// let string: Arc<str> = Arc::from("eggplant");
4071    /// let bytes: Arc<[u8]> = Arc::from(string);
4072    /// assert_eq!("eggplant".as_bytes(), bytes.as_ref());
4073    /// ```
4074    #[inline]
4075    fn from(rc: Arc<str>) -> Self {
4076        // SAFETY: `str` has the same layout as `[u8]`.
4077        unsafe { Arc::from_raw(Arc::into_raw(rc) as *const [u8]) }
4078    }
4079}
4080
4081#[stable(feature = "boxed_slice_try_from", since = "1.43.0")]
4082impl<T, A: Allocator, const N: usize> TryFrom<Arc<[T], A>> for Arc<[T; N], A> {
4083    type Error = Arc<[T], A>;
4084
4085    fn try_from(boxed_slice: Arc<[T], A>) -> Result<Self, Self::Error> {
4086        if boxed_slice.len() == N {
4087            let (ptr, alloc) = Arc::into_inner_with_allocator(boxed_slice);
4088            Ok(unsafe { Arc::from_inner_in(ptr.cast(), alloc) })
4089        } else {
4090            Err(boxed_slice)
4091        }
4092    }
4093}
4094
4095#[cfg(not(no_global_oom_handling))]
4096#[stable(feature = "shared_from_iter", since = "1.37.0")]
4097impl<T> FromIterator<T> for Arc<[T]> {
4098    /// Takes each element in the `Iterator` and collects it into an `Arc<[T]>`.
4099    ///
4100    /// # Performance characteristics
4101    ///
4102    /// ## The general case
4103    ///
4104    /// In the general case, collecting into `Arc<[T]>` is done by first
4105    /// collecting into a `Vec<T>`. That is, when writing the following:
4106    ///
4107    /// ```rust
4108    /// # use std::sync::Arc;
4109    /// let evens: Arc<[u8]> = (0..10).filter(|&x| x % 2 == 0).collect();
4110    /// # assert_eq!(&*evens, &[0, 2, 4, 6, 8]);
4111    /// ```
4112    ///
4113    /// this behaves as if we wrote:
4114    ///
4115    /// ```rust
4116    /// # use std::sync::Arc;
4117    /// let evens: Arc<[u8]> = (0..10).filter(|&x| x % 2 == 0)
4118    ///     .collect::<Vec<_>>() // The first set of allocations happens here.
4119    ///     .into(); // A second allocation for `Arc<[T]>` happens here.
4120    /// # assert_eq!(&*evens, &[0, 2, 4, 6, 8]);
4121    /// ```
4122    ///
4123    /// This will allocate as many times as needed for constructing the `Vec<T>`
4124    /// and then it will allocate once for turning the `Vec<T>` into the `Arc<[T]>`.
4125    ///
4126    /// ## Iterators of known length
4127    ///
4128    /// When your `Iterator` implements `TrustedLen` and is of an exact size,
4129    /// a single allocation will be made for the `Arc<[T]>`. For example:
4130    ///
4131    /// ```rust
4132    /// # use std::sync::Arc;
4133    /// let evens: Arc<[u8]> = (0..10).collect(); // Just a single allocation happens here.
4134    /// # assert_eq!(&*evens, &*(0..10).collect::<Vec<_>>());
4135    /// ```
4136    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
4137        ToArcSlice::to_arc_slice(iter.into_iter())
4138    }
4139}
4140
4141#[cfg(not(no_global_oom_handling))]
4142/// Specialization trait used for collecting into `Arc<[T]>`.
4143trait ToArcSlice<T>: Iterator<Item = T> + Sized {
4144    fn to_arc_slice(self) -> Arc<[T]>;
4145}
4146
4147#[cfg(not(no_global_oom_handling))]
4148impl<T, I: Iterator<Item = T>> ToArcSlice<T> for I {
4149    default fn to_arc_slice(self) -> Arc<[T]> {
4150        self.collect::<Vec<T>>().into()
4151    }
4152}
4153
4154#[cfg(not(no_global_oom_handling))]
4155impl<T, I: iter::TrustedLen<Item = T>> ToArcSlice<T> for I {
4156    fn to_arc_slice(self) -> Arc<[T]> {
4157        // This is the case for a `TrustedLen` iterator.
4158        let (low, high) = self.size_hint();
4159        if let Some(high) = high {
4160            debug_assert_eq!(
4161                low,
4162                high,
4163                "TrustedLen iterator's size hint is not exact: {:?}",
4164                (low, high)
4165            );
4166
4167            unsafe {
4168                // SAFETY: We need to ensure that the iterator has an exact length and we have.
4169                Arc::from_iter_exact(self, low)
4170            }
4171        } else {
4172            // TrustedLen contract guarantees that `upper_bound == None` implies an iterator
4173            // length exceeding `usize::MAX`.
4174            // The default implementation would collect into a vec which would panic.
4175            // Thus we panic here immediately without invoking `Vec` code.
4176            panic!("capacity overflow");
4177        }
4178    }
4179}
4180
4181#[stable(feature = "rust1", since = "1.0.0")]
4182impl<T: ?Sized, A: Allocator> borrow::Borrow<T> for Arc<T, A> {
4183    fn borrow(&self) -> &T {
4184        &**self
4185    }
4186}
4187
4188#[stable(since = "1.5.0", feature = "smart_ptr_as_ref")]
4189impl<T: ?Sized, A: Allocator> AsRef<T> for Arc<T, A> {
4190    fn as_ref(&self) -> &T {
4191        &**self
4192    }
4193}
4194
4195#[stable(feature = "pin", since = "1.33.0")]
4196impl<T: ?Sized, A: Allocator> Unpin for Arc<T, A> {}
4197
4198/// Gets the offset within an `ArcInner` for the payload behind a pointer.
4199///
4200/// # Safety
4201///
4202/// The pointer must point to (and have valid metadata for) a previously
4203/// valid instance of T, but the T is allowed to be dropped.
4204unsafe fn data_offset<T: ?Sized>(ptr: *const T) -> usize {
4205    // Align the unsized value to the end of the ArcInner.
4206    // Because ArcInner is repr(C), it will always be the last field in memory.
4207    // SAFETY: since the only unsized types possible are slices, trait objects,
4208    // and extern types, the input safety requirement is currently enough to
4209    // satisfy the requirements of Alignment::of_val_raw; this is an implementation
4210    // detail of the language that must not be relied upon outside of std.
4211    unsafe { data_offset_alignment(Alignment::of_val_raw(ptr)) }
4212}
4213
4214#[inline]
4215fn data_offset_alignment(alignment: Alignment) -> usize {
4216    let layout = Layout::new::<ArcInner<()>>();
4217    layout.size() + layout.padding_needed_for(alignment)
4218}
4219
4220/// A unique owning pointer to an [`ArcInner`] **that does not imply the contents are initialized,**
4221/// but will deallocate it (without dropping the value) when dropped.
4222///
4223/// This is a helper for [`Arc::make_mut()`] to ensure correct cleanup on panic.
4224struct UniqueArcUninit<T: ?Sized, A: Allocator> {
4225    ptr: NonNull<ArcInner<T>>,
4226    layout_for_value: Layout,
4227    alloc: Option<A>,
4228}
4229
4230impl<T: ?Sized, A: Allocator> UniqueArcUninit<T, A> {
4231    /// Allocates an ArcInner with layout suitable to contain `for_value` or a clone of it.
4232    #[cfg(not(no_global_oom_handling))]
4233    fn new(for_value: &T, alloc: A) -> UniqueArcUninit<T, A> {
4234        let layout = Layout::for_value(for_value);
4235        let ptr = unsafe {
4236            Arc::allocate_for_layout(
4237                layout,
4238                |layout_for_arcinner| alloc.allocate(layout_for_arcinner),
4239                |mem| mem.with_metadata_of(ptr::from_ref(for_value) as *const ArcInner<T>),
4240            )
4241        };
4242        Self { ptr: NonNull::new(ptr).unwrap(), layout_for_value: layout, alloc: Some(alloc) }
4243    }
4244
4245    /// Allocates an ArcInner with layout suitable to contain `for_value` or a clone of it,
4246    /// returning an error if allocation fails.
4247    fn try_new(for_value: &T, alloc: A) -> Result<UniqueArcUninit<T, A>, AllocError> {
4248        let layout = Layout::for_value(for_value);
4249        let ptr = unsafe {
4250            Arc::try_allocate_for_layout(
4251                layout,
4252                |layout_for_arcinner| alloc.allocate(layout_for_arcinner),
4253                |mem| mem.with_metadata_of(ptr::from_ref(for_value) as *const ArcInner<T>),
4254            )?
4255        };
4256        Ok(Self { ptr: NonNull::new(ptr).unwrap(), layout_for_value: layout, alloc: Some(alloc) })
4257    }
4258
4259    /// Returns the pointer to be written into to initialize the [`Arc`].
4260    fn data_ptr(&mut self) -> *mut T {
4261        let offset = data_offset_alignment(self.layout_for_value.alignment());
4262        unsafe { self.ptr.as_ptr().byte_add(offset) as *mut T }
4263    }
4264
4265    /// Upgrade this into a normal [`Arc`].
4266    ///
4267    /// # Safety
4268    ///
4269    /// The data must have been initialized (by writing to [`Self::data_ptr()`]).
4270    unsafe fn into_arc(self) -> Arc<T, A> {
4271        let mut this = ManuallyDrop::new(self);
4272        let ptr = this.ptr.as_ptr();
4273        let alloc = this.alloc.take().unwrap();
4274
4275        // SAFETY: The pointer is valid as per `UniqueArcUninit::new`, and the caller is responsible
4276        // for having initialized the data.
4277        unsafe { Arc::from_ptr_in(ptr, alloc) }
4278    }
4279}
4280
4281#[cfg(not(no_global_oom_handling))]
4282impl<T: ?Sized, A: Allocator> Drop for UniqueArcUninit<T, A> {
4283    fn drop(&mut self) {
4284        // SAFETY:
4285        // * new() produced a pointer safe to deallocate.
4286        // * We own the pointer unless into_arc() was called, which forgets us.
4287        unsafe {
4288            self.alloc.take().unwrap().deallocate(
4289                self.ptr.cast(),
4290                arcinner_layout_for_value_layout(self.layout_for_value),
4291            );
4292        }
4293    }
4294}
4295
4296#[stable(feature = "arc_error", since = "1.52.0")]
4297impl<T: core::error::Error + ?Sized> core::error::Error for Arc<T> {
4298    #[allow(deprecated)]
4299    fn cause(&self) -> Option<&dyn core::error::Error> {
4300        core::error::Error::cause(&**self)
4301    }
4302
4303    fn source(&self) -> Option<&(dyn core::error::Error + 'static)> {
4304        core::error::Error::source(&**self)
4305    }
4306
4307    fn provide<'a>(&'a self, req: &mut core::error::Request<'a>) {
4308        core::error::Error::provide(&**self, req);
4309    }
4310}
4311
4312/// A uniquely owned [`Arc`].
4313///
4314/// This represents an `Arc` that is known to be uniquely owned -- that is, have exactly one strong
4315/// reference. Multiple weak pointers can be created, but attempts to upgrade those to strong
4316/// references will fail unless the `UniqueArc` they point to has been converted into a regular `Arc`.
4317///
4318/// Because it is uniquely owned, the contents of a `UniqueArc` can be freely mutated. A common
4319/// use case is to have an object be mutable during its initialization phase but then have it become
4320/// immutable and converted to a normal `Arc`.
4321///
4322/// This can be used as a flexible way to create cyclic data structures, as in the example below.
4323///
4324/// ```
4325/// #![feature(unique_rc_arc)]
4326/// use std::sync::{Arc, Weak, UniqueArc};
4327///
4328/// struct Gadget {
4329///     me: Weak<Gadget>,
4330/// }
4331///
4332/// fn create_gadget() -> Option<Arc<Gadget>> {
4333///     let mut rc = UniqueArc::new(Gadget {
4334///         me: Weak::new(),
4335///     });
4336///     rc.me = UniqueArc::downgrade(&rc);
4337///     Some(UniqueArc::into_arc(rc))
4338/// }
4339///
4340/// create_gadget().unwrap();
4341/// ```
4342///
4343/// An advantage of using `UniqueArc` over [`Arc::new_cyclic`] to build cyclic data structures is that
4344/// [`Arc::new_cyclic`]'s `data_fn` parameter cannot be async or return a [`Result`]. As shown in the
4345/// previous example, `UniqueArc` allows for more flexibility in the construction of cyclic data,
4346/// including fallible or async constructors.
4347#[unstable(feature = "unique_rc_arc", issue = "112566")]
4348pub struct UniqueArc<
4349    T: ?Sized,
4350    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
4351> {
4352    ptr: NonNull<ArcInner<T>>,
4353    // Define the ownership of `ArcInner<T>` for drop-check
4354    _marker: PhantomData<ArcInner<T>>,
4355    // Invariance is necessary for soundness: once other `Weak`
4356    // references exist, we already have a form of shared mutability!
4357    _marker2: PhantomData<*mut T>,
4358    alloc: A,
4359}
4360
4361#[unstable(feature = "unique_rc_arc", issue = "112566")]
4362unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Send> Send for UniqueArc<T, A> {}
4363
4364#[unstable(feature = "unique_rc_arc", issue = "112566")]
4365unsafe impl<T: ?Sized + Sync + Send, A: Allocator + Sync> Sync for UniqueArc<T, A> {}
4366
4367#[unstable(feature = "unique_rc_arc", issue = "112566")]
4368// #[unstable(feature = "coerce_unsized", issue = "18598")]
4369impl<T: ?Sized + Unsize<U>, U: ?Sized, A: Allocator> CoerceUnsized<UniqueArc<U, A>>
4370    for UniqueArc<T, A>
4371{
4372}
4373
4374//#[unstable(feature = "unique_rc_arc", issue = "112566")]
4375#[unstable(feature = "dispatch_from_dyn", issue = "none")]
4376impl<T: ?Sized + Unsize<U>, U: ?Sized> DispatchFromDyn<UniqueArc<U>> for UniqueArc<T> {}
4377
4378#[unstable(feature = "unique_rc_arc", issue = "112566")]
4379impl<T: ?Sized + fmt::Display, A: Allocator> fmt::Display for UniqueArc<T, A> {
4380    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4381        fmt::Display::fmt(&**self, f)
4382    }
4383}
4384
4385#[unstable(feature = "unique_rc_arc", issue = "112566")]
4386impl<T: ?Sized + fmt::Debug, A: Allocator> fmt::Debug for UniqueArc<T, A> {
4387    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4388        fmt::Debug::fmt(&**self, f)
4389    }
4390}
4391
4392#[unstable(feature = "unique_rc_arc", issue = "112566")]
4393impl<T: ?Sized, A: Allocator> fmt::Pointer for UniqueArc<T, A> {
4394    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4395        fmt::Pointer::fmt(&(&raw const **self), f)
4396    }
4397}
4398
4399#[unstable(feature = "unique_rc_arc", issue = "112566")]
4400impl<T: ?Sized, A: Allocator> borrow::Borrow<T> for UniqueArc<T, A> {
4401    fn borrow(&self) -> &T {
4402        &**self
4403    }
4404}
4405
4406#[unstable(feature = "unique_rc_arc", issue = "112566")]
4407impl<T: ?Sized, A: Allocator> borrow::BorrowMut<T> for UniqueArc<T, A> {
4408    fn borrow_mut(&mut self) -> &mut T {
4409        &mut **self
4410    }
4411}
4412
4413#[unstable(feature = "unique_rc_arc", issue = "112566")]
4414impl<T: ?Sized, A: Allocator> AsRef<T> for UniqueArc<T, A> {
4415    fn as_ref(&self) -> &T {
4416        &**self
4417    }
4418}
4419
4420#[unstable(feature = "unique_rc_arc", issue = "112566")]
4421impl<T: ?Sized, A: Allocator> AsMut<T> for UniqueArc<T, A> {
4422    fn as_mut(&mut self) -> &mut T {
4423        &mut **self
4424    }
4425}
4426
4427#[unstable(feature = "unique_rc_arc", issue = "112566")]
4428impl<T: ?Sized, A: Allocator> Unpin for UniqueArc<T, A> {}
4429
4430#[unstable(feature = "unique_rc_arc", issue = "112566")]
4431impl<T: ?Sized + PartialEq, A: Allocator> PartialEq for UniqueArc<T, A> {
4432    /// Equality for two `UniqueArc`s.
4433    ///
4434    /// Two `UniqueArc`s are equal if their inner values are equal.
4435    ///
4436    /// # Examples
4437    ///
4438    /// ```
4439    /// #![feature(unique_rc_arc)]
4440    /// use std::sync::UniqueArc;
4441    ///
4442    /// let five = UniqueArc::new(5);
4443    ///
4444    /// assert!(five == UniqueArc::new(5));
4445    /// ```
4446    #[inline]
4447    fn eq(&self, other: &Self) -> bool {
4448        PartialEq::eq(&**self, &**other)
4449    }
4450}
4451
4452#[unstable(feature = "unique_rc_arc", issue = "112566")]
4453impl<T: ?Sized + PartialOrd, A: Allocator> PartialOrd for UniqueArc<T, A> {
4454    /// Partial comparison for two `UniqueArc`s.
4455    ///
4456    /// The two are compared by calling `partial_cmp()` on their inner values.
4457    ///
4458    /// # Examples
4459    ///
4460    /// ```
4461    /// #![feature(unique_rc_arc)]
4462    /// use std::sync::UniqueArc;
4463    /// use std::cmp::Ordering;
4464    ///
4465    /// let five = UniqueArc::new(5);
4466    ///
4467    /// assert_eq!(Some(Ordering::Less), five.partial_cmp(&UniqueArc::new(6)));
4468    /// ```
4469    #[inline(always)]
4470    fn partial_cmp(&self, other: &UniqueArc<T, A>) -> Option<Ordering> {
4471        (**self).partial_cmp(&**other)
4472    }
4473
4474    /// Less-than comparison for two `UniqueArc`s.
4475    ///
4476    /// The two are compared by calling `<` on their inner values.
4477    ///
4478    /// # Examples
4479    ///
4480    /// ```
4481    /// #![feature(unique_rc_arc)]
4482    /// use std::sync::UniqueArc;
4483    ///
4484    /// let five = UniqueArc::new(5);
4485    ///
4486    /// assert!(five < UniqueArc::new(6));
4487    /// ```
4488    #[inline(always)]
4489    fn lt(&self, other: &UniqueArc<T, A>) -> bool {
4490        **self < **other
4491    }
4492
4493    /// 'Less than or equal to' comparison for two `UniqueArc`s.
4494    ///
4495    /// The two are compared by calling `<=` on their inner values.
4496    ///
4497    /// # Examples
4498    ///
4499    /// ```
4500    /// #![feature(unique_rc_arc)]
4501    /// use std::sync::UniqueArc;
4502    ///
4503    /// let five = UniqueArc::new(5);
4504    ///
4505    /// assert!(five <= UniqueArc::new(5));
4506    /// ```
4507    #[inline(always)]
4508    fn le(&self, other: &UniqueArc<T, A>) -> bool {
4509        **self <= **other
4510    }
4511
4512    /// Greater-than comparison for two `UniqueArc`s.
4513    ///
4514    /// The two are compared by calling `>` on their inner values.
4515    ///
4516    /// # Examples
4517    ///
4518    /// ```
4519    /// #![feature(unique_rc_arc)]
4520    /// use std::sync::UniqueArc;
4521    ///
4522    /// let five = UniqueArc::new(5);
4523    ///
4524    /// assert!(five > UniqueArc::new(4));
4525    /// ```
4526    #[inline(always)]
4527    fn gt(&self, other: &UniqueArc<T, A>) -> bool {
4528        **self > **other
4529    }
4530
4531    /// 'Greater than or equal to' comparison for two `UniqueArc`s.
4532    ///
4533    /// The two are compared by calling `>=` on their inner values.
4534    ///
4535    /// # Examples
4536    ///
4537    /// ```
4538    /// #![feature(unique_rc_arc)]
4539    /// use std::sync::UniqueArc;
4540    ///
4541    /// let five = UniqueArc::new(5);
4542    ///
4543    /// assert!(five >= UniqueArc::new(5));
4544    /// ```
4545    #[inline(always)]
4546    fn ge(&self, other: &UniqueArc<T, A>) -> bool {
4547        **self >= **other
4548    }
4549}
4550
4551#[unstable(feature = "unique_rc_arc", issue = "112566")]
4552impl<T: ?Sized + Ord, A: Allocator> Ord for UniqueArc<T, A> {
4553    /// Comparison for two `UniqueArc`s.
4554    ///
4555    /// The two are compared by calling `cmp()` on their inner values.
4556    ///
4557    /// # Examples
4558    ///
4559    /// ```
4560    /// #![feature(unique_rc_arc)]
4561    /// use std::sync::UniqueArc;
4562    /// use std::cmp::Ordering;
4563    ///
4564    /// let five = UniqueArc::new(5);
4565    ///
4566    /// assert_eq!(Ordering::Less, five.cmp(&UniqueArc::new(6)));
4567    /// ```
4568    #[inline]
4569    fn cmp(&self, other: &UniqueArc<T, A>) -> Ordering {
4570        (**self).cmp(&**other)
4571    }
4572}
4573
4574#[unstable(feature = "unique_rc_arc", issue = "112566")]
4575impl<T: ?Sized + Eq, A: Allocator> Eq for UniqueArc<T, A> {}
4576
4577#[unstable(feature = "unique_rc_arc", issue = "112566")]
4578impl<T: ?Sized + Hash, A: Allocator> Hash for UniqueArc<T, A> {
4579    fn hash<H: Hasher>(&self, state: &mut H) {
4580        (**self).hash(state);
4581    }
4582}
4583
4584impl<T> UniqueArc<T, Global> {
4585    /// Creates a new `UniqueArc`.
4586    ///
4587    /// Weak references to this `UniqueArc` can be created with [`UniqueArc::downgrade`]. Upgrading
4588    /// these weak references will fail before the `UniqueArc` has been converted into an [`Arc`].
4589    /// After converting the `UniqueArc` into an [`Arc`], any weak references created beforehand will
4590    /// point to the new [`Arc`].
4591    #[cfg(not(no_global_oom_handling))]
4592    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4593    #[must_use]
4594    pub fn new(value: T) -> Self {
4595        Self::new_in(value, Global)
4596    }
4597
4598    /// Maps the value in a `UniqueArc`, reusing the allocation if possible.
4599    ///
4600    /// `f` is called on a reference to the value in the `UniqueArc`, and the result is returned,
4601    /// also in a `UniqueArc`.
4602    ///
4603    /// Note: this is an associated function, which means that you have
4604    /// to call it as `UniqueArc::map(u, f)` instead of `u.map(f)`. This
4605    /// is so that there is no conflict with a method on the inner type.
4606    ///
4607    /// # Examples
4608    ///
4609    /// ```
4610    /// #![feature(smart_pointer_try_map)]
4611    /// #![feature(unique_rc_arc)]
4612    ///
4613    /// use std::sync::UniqueArc;
4614    ///
4615    /// let r = UniqueArc::new(7);
4616    /// let new = UniqueArc::map(r, |i| i + 7);
4617    /// assert_eq!(*new, 14);
4618    /// ```
4619    #[cfg(not(no_global_oom_handling))]
4620    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
4621    pub fn map<U>(this: Self, f: impl FnOnce(T) -> U) -> UniqueArc<U> {
4622        if size_of::<T>() == size_of::<U>()
4623            && align_of::<T>() == align_of::<U>()
4624            && UniqueArc::weak_count(&this) == 0
4625        {
4626            unsafe {
4627                let ptr = UniqueArc::into_raw(this);
4628                let value = ptr.read();
4629                let mut allocation = UniqueArc::from_raw(ptr.cast::<mem::MaybeUninit<U>>());
4630
4631                allocation.write(f(value));
4632                allocation.assume_init()
4633            }
4634        } else {
4635            UniqueArc::new(f(UniqueArc::unwrap(this)))
4636        }
4637    }
4638
4639    /// Attempts to map the value in a `UniqueArc`, reusing the allocation if possible.
4640    ///
4641    /// `f` is called on a reference to the value in the `UniqueArc`, and if the operation succeeds,
4642    /// the result is returned, also in a `UniqueArc`.
4643    ///
4644    /// Note: this is an associated function, which means that you have
4645    /// to call it as `UniqueArc::try_map(u, f)` instead of `u.try_map(f)`. This
4646    /// is so that there is no conflict with a method on the inner type.
4647    ///
4648    /// # Examples
4649    ///
4650    /// ```
4651    /// #![feature(smart_pointer_try_map)]
4652    /// #![feature(unique_rc_arc)]
4653    ///
4654    /// use std::sync::UniqueArc;
4655    ///
4656    /// let b = UniqueArc::new(7);
4657    /// let new = UniqueArc::try_map(b, u32::try_from).unwrap();
4658    /// assert_eq!(*new, 7);
4659    /// ```
4660    #[cfg(not(no_global_oom_handling))]
4661    #[unstable(feature = "smart_pointer_try_map", issue = "144419")]
4662    pub fn try_map<R>(
4663        this: Self,
4664        f: impl FnOnce(T) -> R,
4665    ) -> <R::Residual as Residual<UniqueArc<R::Output>>>::TryType
4666    where
4667        R: Try,
4668        R::Residual: Residual<UniqueArc<R::Output>>,
4669    {
4670        if size_of::<T>() == size_of::<R::Output>()
4671            && align_of::<T>() == align_of::<R::Output>()
4672            && UniqueArc::weak_count(&this) == 0
4673        {
4674            unsafe {
4675                let ptr = UniqueArc::into_raw(this);
4676                let value = ptr.read();
4677                let mut allocation = UniqueArc::from_raw(ptr.cast::<mem::MaybeUninit<R::Output>>());
4678
4679                allocation.write(f(value)?);
4680                try { allocation.assume_init() }
4681            }
4682        } else {
4683            try { UniqueArc::new(f(UniqueArc::unwrap(this))?) }
4684        }
4685    }
4686
4687    #[cfg(not(no_global_oom_handling))]
4688    fn unwrap(this: Self) -> T {
4689        let this = ManuallyDrop::new(this);
4690        let val: T = unsafe { ptr::read(&**this) };
4691
4692        let _weak = Weak { ptr: this.ptr, alloc: Global };
4693
4694        val
4695    }
4696}
4697
4698impl<T: ?Sized> UniqueArc<T> {
4699    #[cfg(not(no_global_oom_handling))]
4700    unsafe fn from_raw(ptr: *const T) -> Self {
4701        let offset = unsafe { data_offset(ptr) };
4702
4703        // Reverse the offset to find the original ArcInner.
4704        let rc_ptr = unsafe { ptr.byte_sub(offset) as *mut ArcInner<T> };
4705
4706        Self {
4707            ptr: unsafe { NonNull::new_unchecked(rc_ptr) },
4708            _marker: PhantomData,
4709            _marker2: PhantomData,
4710            alloc: Global,
4711        }
4712    }
4713
4714    #[cfg(not(no_global_oom_handling))]
4715    fn into_raw(this: Self) -> *const T {
4716        let this = ManuallyDrop::new(this);
4717        Self::as_ptr(&*this)
4718    }
4719}
4720
4721impl<T, A: Allocator> UniqueArc<T, A> {
4722    /// Creates a new `UniqueArc` in the provided allocator.
4723    ///
4724    /// Weak references to this `UniqueArc` can be created with [`UniqueArc::downgrade`]. Upgrading
4725    /// these weak references will fail before the `UniqueArc` has been converted into an [`Arc`].
4726    /// After converting the `UniqueArc` into an [`Arc`], any weak references created beforehand will
4727    /// point to the new [`Arc`].
4728    #[cfg(not(no_global_oom_handling))]
4729    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4730    #[must_use]
4731    // #[unstable(feature = "allocator_api", issue = "32838")]
4732    pub fn new_in(data: T, alloc: A) -> Self {
4733        let (ptr, alloc) = Box::into_unique(Box::new_in(
4734            ArcInner {
4735                strong: atomic::AtomicUsize::new(0),
4736                // keep one weak reference so if all the weak pointers that are created are dropped
4737                // the UniqueArc still stays valid.
4738                weak: atomic::AtomicUsize::new(1),
4739                data,
4740            },
4741            alloc,
4742        ));
4743        Self { ptr: ptr.into(), _marker: PhantomData, _marker2: PhantomData, alloc }
4744    }
4745}
4746
4747impl<T: ?Sized, A: Allocator> UniqueArc<T, A> {
4748    /// Converts the `UniqueArc` into a regular [`Arc`].
4749    ///
4750    /// This consumes the `UniqueArc` and returns a regular [`Arc`] that contains the `value` that
4751    /// is passed to `into_arc`.
4752    ///
4753    /// Any weak references created before this method is called can now be upgraded to strong
4754    /// references.
4755    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4756    #[must_use]
4757    pub fn into_arc(this: Self) -> Arc<T, A> {
4758        let this = ManuallyDrop::new(this);
4759
4760        // Move the allocator out.
4761        // SAFETY: `this.alloc` will not be accessed again, nor dropped because it is in
4762        // a `ManuallyDrop`.
4763        let alloc: A = unsafe { ptr::read(&this.alloc) };
4764
4765        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4766        unsafe {
4767            // Convert our weak reference into a strong reference
4768            (*this.ptr.as_ptr()).strong.store(1, Release);
4769            Arc::from_inner_in(this.ptr, alloc)
4770        }
4771    }
4772
4773    #[cfg(not(no_global_oom_handling))]
4774    fn weak_count(this: &Self) -> usize {
4775        this.inner().weak.load(Acquire) - 1
4776    }
4777
4778    #[cfg(not(no_global_oom_handling))]
4779    fn inner(&self) -> &ArcInner<T> {
4780        // SAFETY: while this UniqueArc is alive we're guaranteed that the inner pointer is valid.
4781        unsafe { self.ptr.as_ref() }
4782    }
4783
4784    #[cfg(not(no_global_oom_handling))]
4785    fn as_ptr(this: &Self) -> *const T {
4786        let ptr: *mut ArcInner<T> = NonNull::as_ptr(this.ptr);
4787
4788        // SAFETY: This cannot go through Deref::deref or UniqueArc::inner because
4789        // this is required to retain raw/mut provenance such that e.g. `get_mut` can
4790        // write through the pointer after the Rc is recovered through `from_raw`.
4791        unsafe { &raw mut (*ptr).data }
4792    }
4793
4794    #[inline]
4795    #[cfg(not(no_global_oom_handling))]
4796    fn into_inner_with_allocator(this: Self) -> (NonNull<ArcInner<T>>, A) {
4797        let this = mem::ManuallyDrop::new(this);
4798        (this.ptr, unsafe { ptr::read(&this.alloc) })
4799    }
4800
4801    #[inline]
4802    #[cfg(not(no_global_oom_handling))]
4803    unsafe fn from_inner_in(ptr: NonNull<ArcInner<T>>, alloc: A) -> Self {
4804        Self { ptr, _marker: PhantomData, _marker2: PhantomData, alloc }
4805    }
4806}
4807
4808impl<T: ?Sized, A: Allocator + Clone> UniqueArc<T, A> {
4809    /// Creates a new weak reference to the `UniqueArc`.
4810    ///
4811    /// Attempting to upgrade this weak reference will fail before the `UniqueArc` has been converted
4812    /// to a [`Arc`] using [`UniqueArc::into_arc`].
4813    #[unstable(feature = "unique_rc_arc", issue = "112566")]
4814    #[must_use]
4815    pub fn downgrade(this: &Self) -> Weak<T, A> {
4816        // Using a relaxed ordering is alright here, as knowledge of the
4817        // original reference prevents other threads from erroneously deleting
4818        // the object or converting the object to a normal `Arc<T, A>`.
4819        //
4820        // Note that we don't need to test if the weak counter is locked because there
4821        // are no such operations like `Arc::get_mut` or `Arc::make_mut` that will lock
4822        // the weak counter.
4823        //
4824        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4825        let old_size = unsafe { (*this.ptr.as_ptr()).weak.fetch_add(1, Relaxed) };
4826
4827        // See comments in Arc::clone() for why we do this (for mem::forget).
4828        if old_size > MAX_REFCOUNT {
4829            abort();
4830        }
4831
4832        Weak { ptr: this.ptr, alloc: this.alloc.clone() }
4833    }
4834}
4835
4836#[cfg(not(no_global_oom_handling))]
4837impl<T, A: Allocator> UniqueArc<mem::MaybeUninit<T>, A> {
4838    unsafe fn assume_init(self) -> UniqueArc<T, A> {
4839        let (ptr, alloc) = UniqueArc::into_inner_with_allocator(self);
4840        unsafe { UniqueArc::from_inner_in(ptr.cast(), alloc) }
4841    }
4842}
4843
4844#[unstable(feature = "unique_rc_arc", issue = "112566")]
4845impl<T: ?Sized, A: Allocator> Deref for UniqueArc<T, A> {
4846    type Target = T;
4847
4848    fn deref(&self) -> &T {
4849        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4850        unsafe { &self.ptr.as_ref().data }
4851    }
4852}
4853
4854// #[unstable(feature = "unique_rc_arc", issue = "112566")]
4855#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
4856unsafe impl<T: ?Sized> PinCoerceUnsized for UniqueArc<T> {}
4857
4858#[unstable(feature = "unique_rc_arc", issue = "112566")]
4859impl<T: ?Sized, A: Allocator> DerefMut for UniqueArc<T, A> {
4860    fn deref_mut(&mut self) -> &mut T {
4861        // SAFETY: This pointer was allocated at creation time so we know it is valid. We know we
4862        // have unique ownership and therefore it's safe to make a mutable reference because
4863        // `UniqueArc` owns the only strong reference to itself.
4864        // We also need to be careful to only create a mutable reference to the `data` field,
4865        // as a mutable reference to the entire `ArcInner` would assert uniqueness over the
4866        // ref count fields too, invalidating any attempt by `Weak`s to access the ref count.
4867        unsafe { &mut (*self.ptr.as_ptr()).data }
4868    }
4869}
4870
4871#[unstable(feature = "unique_rc_arc", issue = "112566")]
4872// #[unstable(feature = "deref_pure_trait", issue = "87121")]
4873unsafe impl<T: ?Sized, A: Allocator> DerefPure for UniqueArc<T, A> {}
4874
4875#[unstable(feature = "unique_rc_arc", issue = "112566")]
4876unsafe impl<#[may_dangle] T: ?Sized, A: Allocator> Drop for UniqueArc<T, A> {
4877    fn drop(&mut self) {
4878        // See `Arc::drop_slow` which drops an `Arc` with a strong count of 0.
4879        // SAFETY: This pointer was allocated at creation time so we know it is valid.
4880        let _weak = Weak { ptr: self.ptr, alloc: &self.alloc };
4881
4882        unsafe { ptr::drop_in_place(&mut (*self.ptr.as_ptr()).data) };
4883    }
4884}
4885
4886#[unstable(feature = "allocator_api", issue = "32838")]
4887unsafe impl<T: ?Sized + Allocator, A: Allocator> Allocator for Arc<T, A> {
4888    #[inline]
4889    fn allocate(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
4890        (**self).allocate(layout)
4891    }
4892
4893    #[inline]
4894    fn allocate_zeroed(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
4895        (**self).allocate_zeroed(layout)
4896    }
4897
4898    #[inline]
4899    unsafe fn deallocate(&self, ptr: NonNull<u8>, layout: Layout) {
4900        // SAFETY: the safety contract must be upheld by the caller
4901        unsafe { (**self).deallocate(ptr, layout) }
4902    }
4903
4904    #[inline]
4905    unsafe fn grow(
4906        &self,
4907        ptr: NonNull<u8>,
4908        old_layout: Layout,
4909        new_layout: Layout,
4910    ) -> Result<NonNull<[u8]>, AllocError> {
4911        // SAFETY: the safety contract must be upheld by the caller
4912        unsafe { (**self).grow(ptr, old_layout, new_layout) }
4913    }
4914
4915    #[inline]
4916    unsafe fn grow_zeroed(
4917        &self,
4918        ptr: NonNull<u8>,
4919        old_layout: Layout,
4920        new_layout: Layout,
4921    ) -> Result<NonNull<[u8]>, AllocError> {
4922        // SAFETY: the safety contract must be upheld by the caller
4923        unsafe { (**self).grow_zeroed(ptr, old_layout, new_layout) }
4924    }
4925
4926    #[inline]
4927    unsafe fn shrink(
4928        &self,
4929        ptr: NonNull<u8>,
4930        old_layout: Layout,
4931        new_layout: Layout,
4932    ) -> Result<NonNull<[u8]>, AllocError> {
4933        // SAFETY: the safety contract must be upheld by the caller
4934        unsafe { (**self).shrink(ptr, old_layout, new_layout) }
4935    }
4936}
````