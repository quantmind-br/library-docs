---
title: cell.rs - source
url: https://doc.rust-lang.org/src/core/cell.rs.html#808
source: crawler
fetched_at: 2026-05-06T21:31:58.014230954-03:00
rendered_js: false
word_count: 12725
summary: This document explains the concept of interior mutability in Rust, detailing how types like Cell, RefCell, OnceCell, and LazyCell allow for controlled mutation of data even when aliased.
tags:
    - rust
    - memory-safety
    - interior-mutability
    - borrow-checking
    - cell
    - refcell
category: concept
---

## core/ cell.rs

````rust
1//! Shareable mutable containers.
2//!
3//! Rust memory safety is based on this rule: Given an object `T`, it is only possible to
4//! have one of the following:
5//!
6//! - Several immutable references (`&T`) to the object (also known as **aliasing**).
7//! - One mutable reference (`&mut T`) to the object (also known as **mutability**).
8//!
9//! This is enforced by the Rust compiler. However, there are situations where this rule is not
10//! flexible enough. Sometimes it is required to have multiple references to an object and yet
11//! mutate it.
12//!
13//! Shareable mutable containers exist to permit mutability in a controlled manner, even in the
14//! presence of aliasing. [`Cell<T>`], [`RefCell<T>`], and [`OnceCell<T>`] allow doing this in
15//! a single-threaded way—they do not implement [`Sync`]. (If you need to do aliasing and
16//! mutation among multiple threads, [`Mutex<T>`], [`RwLock<T>`], [`OnceLock<T>`] or [`atomic`]
17//! types are the correct data structures to do so).
18//!
19//! Values of the `Cell<T>`, `RefCell<T>`, and `OnceCell<T>` types may be mutated through shared
20//! references (i.e. the common `&T` type), whereas most Rust types can only be mutated through
21//! unique (`&mut T`) references. We say these cell types provide 'interior mutability'
22//! (mutable via `&T`), in contrast with typical Rust types that exhibit 'inherited mutability'
23//! (mutable only via `&mut T`).
24//!
25//! Cell types come in four flavors: `Cell<T>`, `RefCell<T>`, `OnceCell<T>`, and `LazyCell<T>`.
26//! Each provides a different way of providing safe interior mutability.
27//!
28//! ## `Cell<T>`
29//!
30//! [`Cell<T>`] implements interior mutability by moving values in and out of the cell. That is, a
31//! `&T` to the inner value can never be obtained, and the value itself cannot be directly
32//! obtained without replacing it with something else. This type provides the following
33//! methods:
34//!
35//!  - For types that implement [`Copy`], the [`get`](Cell::get) method retrieves the current
36//!    interior value by duplicating it.
37//!  - For types that implement [`Default`], the [`take`](Cell::take) method replaces the current
38//!    interior value with [`Default::default()`] and returns the replaced value.
39//!  - All types have:
40//!    - [`replace`](Cell::replace): replaces the current interior value and returns the replaced
41//!      value.
42//!    - [`into_inner`](Cell::into_inner): this method consumes the `Cell<T>` and returns the
43//!      interior value.
44//!    - [`set`](Cell::set): this method replaces the interior value, dropping the replaced value.
45//!
46//! `Cell<T>` is typically used for more simple types where copying or moving values isn't too
47//! resource intensive (e.g. numbers), and should usually be preferred over other cell types when
48//! possible. For larger and non-copy types, `RefCell` provides some advantages.
49//!
50//! ## `RefCell<T>`
51//!
52//! [`RefCell<T>`] uses Rust's lifetimes to implement "dynamic borrowing", a process whereby one can
53//! claim temporary, exclusive, mutable access to the inner value. Borrows for `RefCell<T>`s are
54//! tracked at _runtime_, unlike Rust's native reference types which are entirely tracked
55//! statically, at compile time.
56//!
57//! An immutable reference to a `RefCell`'s inner value (`&T`) can be obtained with
58//! [`borrow`](`RefCell::borrow`), and a mutable borrow (`&mut T`) can be obtained with
59//! [`borrow_mut`](`RefCell::borrow_mut`). When these functions are called, they first verify that
60//! Rust's borrow rules will be satisfied: any number of immutable borrows are allowed or a
61//! single mutable borrow is allowed, but never both. If a borrow is attempted that would violate
62//! these rules, the thread will panic.
63//!
64//! The corresponding [`Sync`] version of `RefCell<T>` is [`RwLock<T>`].
65//!
66//! ## `OnceCell<T>`
67//!
68//! [`OnceCell<T>`] is somewhat of a hybrid of `Cell` and `RefCell` that works for values that
69//! typically only need to be set once. This means that a reference `&T` can be obtained without
70//! moving or copying the inner value (unlike `Cell`) but also without runtime checks (unlike
71//! `RefCell`). However, its value can also not be updated once set unless you have a mutable
72//! reference to the `OnceCell`.
73//!
74//! `OnceCell` provides the following methods:
75//!
76//! - [`get`](OnceCell::get): obtain a reference to the inner value
77//! - [`set`](OnceCell::set): set the inner value if it is unset (returns a `Result`)
78//! - [`get_or_init`](OnceCell::get_or_init): return the inner value, initializing it if needed
79//! - [`get_mut`](OnceCell::get_mut): provide a mutable reference to the inner value, only available
80//!   if you have a mutable reference to the cell itself.
81//!
82//! The corresponding [`Sync`] version of `OnceCell<T>` is [`OnceLock<T>`].
83//!
84//! ## `LazyCell<T, F>`
85//!
86//! A common pattern with OnceCell is, for a given OnceCell, to use the same function on every
87//! call to [`OnceCell::get_or_init`] with that cell. This is what is offered by [`LazyCell`],
88//! which pairs cells of `T` with functions of `F`, and always calls `F` before it yields `&T`.
89//! This happens implicitly by simply attempting to dereference the LazyCell to get its contents,
90//! so its use is much more transparent with a place which has been initialized by a constant.
91//!
92//! More complicated patterns that don't fit this description can be built on `OnceCell<T>` instead.
93//!
94//! `LazyCell` works by providing an implementation of `impl Deref` that calls the function,
95//! so you can just use it by dereference (e.g. `*lazy_cell` or `lazy_cell.deref()`).
96//!
97//! The corresponding [`Sync`] version of `LazyCell<T, F>` is [`LazyLock<T, F>`].
98//!
99//! # When to choose interior mutability
100//!
101//! The more common inherited mutability, where one must have unique access to mutate a value, is
102//! one of the key language elements that enables Rust to reason strongly about pointer aliasing,
103//! statically preventing crash bugs. Because of that, inherited mutability is preferred, and
104//! interior mutability is something of a last resort. Since cell types enable mutation where it
105//! would otherwise be disallowed though, there are occasions when interior mutability might be
106//! appropriate, or even *must* be used, e.g.
107//!
108//! * Introducing mutability 'inside' of something immutable
109//! * Implementation details of logically-immutable methods.
110//! * Mutating implementations of [`Clone`].
111//!
112//! ## Introducing mutability 'inside' of something immutable
113//!
114//! Many shared smart pointer types, including [`Rc<T>`] and [`Arc<T>`], provide containers that can
115//! be cloned and shared between multiple parties. Because the contained values may be
116//! multiply-aliased, they can only be borrowed with `&`, not `&mut`. Without cells it would be
117//! impossible to mutate data inside of these smart pointers at all.
118//!
119//! It's very common then to put a `RefCell<T>` inside shared pointer types to reintroduce
120//! mutability:
121//!
122//! ```
123//! use std::cell::{RefCell, RefMut};
124//! use std::collections::HashMap;
125//! use std::rc::Rc;
126//!
127//! fn main() {
128//!     let shared_map: Rc<RefCell<_>> = Rc::new(RefCell::new(HashMap::new()));
129//!     // Create a new block to limit the scope of the dynamic borrow
130//!     {
131//!         let mut map: RefMut<'_, _> = shared_map.borrow_mut();
132//!         map.insert("africa", 92388);
133//!         map.insert("kyoto", 11837);
134//!         map.insert("piccadilly", 11826);
135//!         map.insert("marbles", 38);
136//!     }
137//!
138//!     // Note that if we had not let the previous borrow of the cache fall out
139//!     // of scope then the subsequent borrow would cause a dynamic thread panic.
140//!     // This is the major hazard of using `RefCell`.
141//!     let total: i32 = shared_map.borrow().values().sum();
142//!     println!("{total}");
143//! }
144//! ```
145//!
146//! Note that this example uses `Rc<T>` and not `Arc<T>`. `RefCell<T>`s are for single-threaded
147//! scenarios. Consider using [`RwLock<T>`] or [`Mutex<T>`] if you need shared mutability in a
148//! multi-threaded situation.
149//!
150//! ## Implementation details of logically-immutable methods
151//!
152//! Occasionally it may be desirable not to expose in an API that there is mutation happening
153//! "under the hood". This may be because logically the operation is immutable, but e.g., caching
154//! forces the implementation to perform mutation; or because you must employ mutation to implement
155//! a trait method that was originally defined to take `&self`.
156//!
157//! ```
158//! # #![allow(dead_code)]
159//! use std::cell::OnceCell;
160//!
161//! struct Graph {
162//!     edges: Vec<(i32, i32)>,
163//!     span_tree_cache: OnceCell<Vec<(i32, i32)>>
164//! }
165//!
166//! impl Graph {
167//!     fn minimum_spanning_tree(&self) -> Vec<(i32, i32)> {
168//!         self.span_tree_cache
169//!             .get_or_init(|| self.calc_span_tree())
170//!             .clone()
171//!     }
172//!
173//!     fn calc_span_tree(&self) -> Vec<(i32, i32)> {
174//!         // Expensive computation goes here
175//!         vec![]
176//!     }
177//! }
178//! ```
179//!
180//! ## Mutating implementations of `Clone`
181//!
182//! This is simply a special - but common - case of the previous: hiding mutability for operations
183//! that appear to be immutable. The [`clone`](Clone::clone) method is expected to not change the
184//! source value, and is declared to take `&self`, not `&mut self`. Therefore, any mutation that
185//! happens in the `clone` method must use cell types. For example, [`Rc<T>`] maintains its
186//! reference counts within a `Cell<T>`.
187//!
188//! ```
189//! use std::cell::Cell;
190//! use std::ptr::NonNull;
191//! use std::process::abort;
192//! use std::marker::PhantomData;
193//!
194//! struct Rc<T: ?Sized> {
195//!     ptr: NonNull<RcInner<T>>,
196//!     phantom: PhantomData<RcInner<T>>,
197//! }
198//!
199//! struct RcInner<T: ?Sized> {
200//!     strong: Cell<usize>,
201//!     refcount: Cell<usize>,
202//!     value: T,
203//! }
204//!
205//! impl<T: ?Sized> Clone for Rc<T> {
206//!     fn clone(&self) -> Rc<T> {
207//!         self.inc_strong();
208//!         Rc {
209//!             ptr: self.ptr,
210//!             phantom: PhantomData,
211//!         }
212//!     }
213//! }
214//!
215//! trait RcInnerPtr<T: ?Sized> {
216//!
217//!     fn inner(&self) -> &RcInner<T>;
218//!
219//!     fn strong(&self) -> usize {
220//!         self.inner().strong.get()
221//!     }
222//!
223//!     fn inc_strong(&self) {
224//!         self.inner()
225//!             .strong
226//!             .set(self.strong()
227//!                      .checked_add(1)
228//!                      .unwrap_or_else(|| abort() ));
229//!     }
230//! }
231//!
232//! impl<T: ?Sized> RcInnerPtr<T> for Rc<T> {
233//!    fn inner(&self) -> &RcInner<T> {
234//!        unsafe {
235//!            self.ptr.as_ref()
236//!        }
237//!    }
238//! }
239//! ```
240//!
241//! [`Arc<T>`]: ../../std/sync/struct.Arc.html
242//! [`Rc<T>`]: ../../std/rc/struct.Rc.html
243//! [`RwLock<T>`]: ../../std/sync/struct.RwLock.html
244//! [`Mutex<T>`]: ../../std/sync/struct.Mutex.html
245//! [`OnceLock<T>`]: ../../std/sync/struct.OnceLock.html
246//! [`LazyLock<T, F>`]: ../../std/sync/struct.LazyLock.html
247//! [`Sync`]: ../../std/marker/trait.Sync.html
248//! [`atomic`]: crate::sync::atomic
249
250#![stable(feature = "rust1", since = "1.0.0")]
251
252use crate::cmp::Ordering;
253use crate::fmt::{self, Debug, Display};
254use crate::marker::{Destruct, PhantomData, Unsize};
255use crate::mem::{self, ManuallyDrop};
256use crate::ops::{self, CoerceUnsized, Deref, DerefMut, DerefPure, DispatchFromDyn};
257use crate::panic::const_panic;
258use crate::pin::PinCoerceUnsized;
259use crate::ptr::{self, NonNull};
260use crate::range;
261
262mod lazy;
263mod once;
264
265#[stable(feature = "lazy_cell", since = "1.80.0")]
266pub use lazy::LazyCell;
267#[stable(feature = "once_cell", since = "1.70.0")]
268pub use once::OnceCell;
269
270/// A mutable memory location.
271///
272/// # Memory layout
273///
274/// `Cell<T>` has the same [memory layout and caveats as
275/// `UnsafeCell<T>`](UnsafeCell#memory-layout). In particular, this means that
276/// `Cell<T>` has the same in-memory representation as its inner type `T`.
277///
278/// # Examples
279///
280/// In this example, you can see that `Cell<T>` enables mutation inside an
281/// immutable struct. In other words, it enables "interior mutability".
282///
283/// ```
284/// use std::cell::Cell;
285///
286/// struct SomeStruct {
287///     regular_field: u8,
288///     special_field: Cell<u8>,
289/// }
290///
291/// let my_struct = SomeStruct {
292///     regular_field: 0,
293///     special_field: Cell::new(1),
294/// };
295///
296/// let new_value = 100;
297///
298/// // ERROR: `my_struct` is immutable
299/// // my_struct.regular_field = new_value;
300///
301/// // WORKS: although `my_struct` is immutable, `special_field` is a `Cell`,
302/// // which can always be mutated
303/// my_struct.special_field.set(new_value);
304/// assert_eq!(my_struct.special_field.get(), new_value);
305/// ```
306///
307/// See the [module-level documentation](self) for more.
308#[rustc_diagnostic_item = "Cell"]
309#[stable(feature = "rust1", since = "1.0.0")]
310#[repr(transparent)]
311#[rustc_pub_transparent]
312pub struct Cell<T: ?Sized> {
313    value: UnsafeCell<T>,
314}
315
316#[stable(feature = "rust1", since = "1.0.0")]
317unsafe impl<T: ?Sized> Send for Cell<T> where T: Send {}
318
319// Note that this negative impl isn't strictly necessary for correctness,
320// as `Cell` wraps `UnsafeCell`, which is itself `!Sync`.
321// However, given how important `Cell`'s `!Sync`-ness is,
322// having an explicit negative impl is nice for documentation purposes
323// and results in nicer error messages.
324#[stable(feature = "rust1", since = "1.0.0")]
325impl<T: ?Sized> !Sync for Cell<T> {}
326
327#[stable(feature = "rust1", since = "1.0.0")]
328impl<T: Copy> Clone for Cell<T> {
329    #[inline]
330    fn clone(&self) -> Cell<T> {
331        Cell::new(self.get())
332    }
333}
334
335#[stable(feature = "rust1", since = "1.0.0")]
336#[rustc_const_unstable(feature = "const_default", issue = "143894")]
337impl<T: [const] Default> const Default for Cell<T> {
338    /// Creates a `Cell<T>`, with the `Default` value for T.
339    #[inline]
340    fn default() -> Cell<T> {
341        Cell::new(Default::default())
342    }
343}
344
345#[stable(feature = "rust1", since = "1.0.0")]
346impl<T: PartialEq + Copy> PartialEq for Cell<T> {
347    #[inline]
348    fn eq(&self, other: &Cell<T>) -> bool {
349        self.get() == other.get()
350    }
351}
352
353#[stable(feature = "cell_eq", since = "1.2.0")]
354impl<T: Eq + Copy> Eq for Cell<T> {}
355
356#[stable(feature = "cell_ord", since = "1.10.0")]
357impl<T: PartialOrd + Copy> PartialOrd for Cell<T> {
358    #[inline]
359    fn partial_cmp(&self, other: &Cell<T>) -> Option<Ordering> {
360        self.get().partial_cmp(&other.get())
361    }
362
363    #[inline]
364    fn lt(&self, other: &Cell<T>) -> bool {
365        self.get() < other.get()
366    }
367
368    #[inline]
369    fn le(&self, other: &Cell<T>) -> bool {
370        self.get() <= other.get()
371    }
372
373    #[inline]
374    fn gt(&self, other: &Cell<T>) -> bool {
375        self.get() > other.get()
376    }
377
378    #[inline]
379    fn ge(&self, other: &Cell<T>) -> bool {
380        self.get() >= other.get()
381    }
382}
383
384#[stable(feature = "cell_ord", since = "1.10.0")]
385impl<T: Ord + Copy> Ord for Cell<T> {
386    #[inline]
387    fn cmp(&self, other: &Cell<T>) -> Ordering {
388        self.get().cmp(&other.get())
389    }
390}
391
392#[stable(feature = "cell_from", since = "1.12.0")]
393#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
394impl<T> const From<T> for Cell<T> {
395    /// Creates a new `Cell<T>` containing the given value.
396    fn from(t: T) -> Cell<T> {
397        Cell::new(t)
398    }
399}
400
401impl<T> Cell<T> {
402    /// Creates a new `Cell` containing the given value.
403    ///
404    /// # Examples
405    ///
406    /// ```
407    /// use std::cell::Cell;
408    ///
409    /// let c = Cell::new(5);
410    /// ```
411    #[stable(feature = "rust1", since = "1.0.0")]
412    #[rustc_const_stable(feature = "const_cell_new", since = "1.24.0")]
413    #[inline]
414    pub const fn new(value: T) -> Cell<T> {
415        Cell { value: UnsafeCell::new(value) }
416    }
417
418    /// Sets the contained value.
419    ///
420    /// # Examples
421    ///
422    /// ```
423    /// use std::cell::Cell;
424    ///
425    /// let c = Cell::new(5);
426    ///
427    /// c.set(10);
428    /// ```
429    #[inline]
430    #[stable(feature = "rust1", since = "1.0.0")]
431    #[rustc_const_unstable(feature = "const_cell_traits", issue = "147787")]
432    #[rustc_should_not_be_called_on_const_items]
433    pub const fn set(&self, val: T)
434    where
435        T: [const] Destruct,
436    {
437        self.replace(val);
438    }
439
440    /// Swaps the values of two `Cell`s.
441    ///
442    /// The difference with `std::mem::swap` is that this function doesn't
443    /// require a `&mut` reference.
444    ///
445    /// # Panics
446    ///
447    /// This function will panic if `self` and `other` are different `Cell`s that partially overlap.
448    /// (Using just standard library methods, it is impossible to create such partially overlapping `Cell`s.
449    /// However, unsafe code is allowed to e.g. create two `&Cell<[i32; 2]>` that partially overlap.)
450    ///
451    /// # Examples
452    ///
453    /// ```
454    /// use std::cell::Cell;
455    ///
456    /// let c1 = Cell::new(5i32);
457    /// let c2 = Cell::new(10i32);
458    /// c1.swap(&c2);
459    /// assert_eq!(10, c1.get());
460    /// assert_eq!(5, c2.get());
461    /// ```
462    #[inline]
463    #[stable(feature = "move_cell", since = "1.17.0")]
464    #[rustc_should_not_be_called_on_const_items]
465    pub fn swap(&self, other: &Self) {
466        // This function documents that it *will* panic, and intrinsics::is_nonoverlapping doesn't
467        // do the check in const, so trying to use it here would be inviting unnecessary fragility.
468        fn is_nonoverlapping<T>(src: *const T, dst: *const T) -> bool {
469            let src_usize = src.addr();
470            let dst_usize = dst.addr();
471            let diff = src_usize.abs_diff(dst_usize);
472            diff >= size_of::<T>()
473        }
474
475        if ptr::eq(self, other) {
476            // Swapping wouldn't change anything.
477            return;
478        }
479        if !is_nonoverlapping(self, other) {
480            // See <https://github.com/rust-lang/rust/issues/80778> for why we need to stop here.
481            panic!("`Cell::swap` on overlapping non-identical `Cell`s");
482        }
483        // SAFETY: This can be risky if called from separate threads, but `Cell`
484        // is `!Sync` so this won't happen. This also won't invalidate any
485        // pointers since `Cell` makes sure nothing else will be pointing into
486        // either of these `Cell`s. We also excluded shenanigans like partially overlapping `Cell`s,
487        // so `swap` will just properly copy two full values of type `T` back and forth.
488        unsafe {
489            mem::swap(&mut *self.value.get(), &mut *other.value.get());
490        }
491    }
492
493    /// Replaces the contained value with `val`, and returns the old contained value.
494    ///
495    /// # Examples
496    ///
497    /// ```
498    /// use std::cell::Cell;
499    ///
500    /// let cell = Cell::new(5);
501    /// assert_eq!(cell.get(), 5);
502    /// assert_eq!(cell.replace(10), 5);
503    /// assert_eq!(cell.get(), 10);
504    /// ```
505    #[inline]
506    #[stable(feature = "move_cell", since = "1.17.0")]
507    #[rustc_const_stable(feature = "const_cell", since = "1.88.0")]
508    #[rustc_confusables("swap")]
509    #[rustc_should_not_be_called_on_const_items]
510    pub const fn replace(&self, val: T) -> T {
511        // SAFETY: This can cause data races if called from a separate thread,
512        // but `Cell` is `!Sync` so this won't happen.
513        mem::replace(unsafe { &mut *self.value.get() }, val)
514    }
515
516    /// Unwraps the value, consuming the cell.
517    ///
518    /// # Examples
519    ///
520    /// ```
521    /// use std::cell::Cell;
522    ///
523    /// let c = Cell::new(5);
524    /// let five = c.into_inner();
525    ///
526    /// assert_eq!(five, 5);
527    /// ```
528    #[stable(feature = "move_cell", since = "1.17.0")]
529    #[rustc_const_stable(feature = "const_cell_into_inner", since = "1.83.0")]
530    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
531    pub const fn into_inner(self) -> T {
532        self.value.into_inner()
533    }
534}
535
536impl<T: Copy> Cell<T> {
537    /// Returns a copy of the contained value.
538    ///
539    /// # Examples
540    ///
541    /// ```
542    /// use std::cell::Cell;
543    ///
544    /// let c = Cell::new(5);
545    ///
546    /// let five = c.get();
547    /// ```
548    #[inline]
549    #[stable(feature = "rust1", since = "1.0.0")]
550    #[rustc_const_stable(feature = "const_cell", since = "1.88.0")]
551    #[rustc_should_not_be_called_on_const_items]
552    pub const fn get(&self) -> T {
553        // SAFETY: This can cause data races if called from a separate thread,
554        // but `Cell` is `!Sync` so this won't happen.
555        unsafe { *self.value.get() }
556    }
557
558    /// Updates the contained value using a function.
559    ///
560    /// # Examples
561    ///
562    /// ```
563    /// use std::cell::Cell;
564    ///
565    /// let c = Cell::new(5);
566    /// c.update(|x| x + 1);
567    /// assert_eq!(c.get(), 6);
568    /// ```
569    #[inline]
570    #[stable(feature = "cell_update", since = "1.88.0")]
571    #[rustc_const_unstable(feature = "const_cell_traits", issue = "147787")]
572    #[rustc_should_not_be_called_on_const_items]
573    pub const fn update(&self, f: impl [const] FnOnce(T) -> T)
574    where
575        // FIXME(const-hack): `Copy` should imply `const Destruct`
576        T: [const] Destruct,
577    {
578        let old = self.get();
579        self.set(f(old));
580    }
581}
582
583impl<T: ?Sized> Cell<T> {
584    /// Returns a raw pointer to the underlying data in this cell.
585    ///
586    /// # Examples
587    ///
588    /// ```
589    /// use std::cell::Cell;
590    ///
591    /// let c = Cell::new(5);
592    ///
593    /// let ptr = c.as_ptr();
594    /// ```
595    #[inline]
596    #[stable(feature = "cell_as_ptr", since = "1.12.0")]
597    #[rustc_const_stable(feature = "const_cell_as_ptr", since = "1.32.0")]
598    #[rustc_as_ptr]
599    #[rustc_never_returns_null_ptr]
600    pub const fn as_ptr(&self) -> *mut T {
601        self.value.get()
602    }
603
604    /// Returns a mutable reference to the underlying data.
605    ///
606    /// This call borrows `Cell` mutably (at compile-time) which guarantees
607    /// that we possess the only reference.
608    ///
609    /// However be cautious: this method expects `self` to be mutable, which is
610    /// generally not the case when using a `Cell`. If you require interior
611    /// mutability by reference, consider using `RefCell` which provides
612    /// run-time checked mutable borrows through its [`borrow_mut`] method.
613    ///
614    /// [`borrow_mut`]: RefCell::borrow_mut()
615    ///
616    /// # Examples
617    ///
618    /// ```
619    /// use std::cell::Cell;
620    ///
621    /// let mut c = Cell::new(5);
622    /// *c.get_mut() += 1;
623    ///
624    /// assert_eq!(c.get(), 6);
625    /// ```
626    #[inline]
627    #[stable(feature = "cell_get_mut", since = "1.11.0")]
628    #[rustc_const_stable(feature = "const_cell", since = "1.88.0")]
629    pub const fn get_mut(&mut self) -> &mut T {
630        self.value.get_mut()
631    }
632
633    /// Returns a `&Cell<T>` from a `&mut T`
634    ///
635    /// # Examples
636    ///
637    /// ```
638    /// use std::cell::Cell;
639    ///
640    /// let slice: &mut [i32] = &mut [1, 2, 3];
641    /// let cell_slice: &Cell<[i32]> = Cell::from_mut(slice);
642    /// let slice_cell: &[Cell<i32>] = cell_slice.as_slice_of_cells();
643    ///
644    /// assert_eq!(slice_cell.len(), 3);
645    /// ```
646    #[inline]
647    #[stable(feature = "as_cell", since = "1.37.0")]
648    #[rustc_const_stable(feature = "const_cell", since = "1.88.0")]
649    pub const fn from_mut(t: &mut T) -> &Cell<T> {
650        // SAFETY: `&mut` ensures unique access.
651        unsafe { &*(t as *mut T as *const Cell<T>) }
652    }
653}
654
655impl<T: Default> Cell<T> {
656    /// Takes the value of the cell, leaving `Default::default()` in its place.
657    ///
658    /// # Examples
659    ///
660    /// ```
661    /// use std::cell::Cell;
662    ///
663    /// let c = Cell::new(5);
664    /// let five = c.take();
665    ///
666    /// assert_eq!(five, 5);
667    /// assert_eq!(c.into_inner(), 0);
668    /// ```
669    #[stable(feature = "move_cell", since = "1.17.0")]
670    #[rustc_const_unstable(feature = "const_cell_traits", issue = "147787")]
671    pub const fn take(&self) -> T
672    where
673        T: [const] Default,
674    {
675        self.replace(Default::default())
676    }
677}
678
679#[unstable(feature = "coerce_unsized", issue = "18598")]
680impl<T: CoerceUnsized<U>, U> CoerceUnsized<Cell<U>> for Cell<T> {}
681
682// Allow types that wrap `Cell` to also implement `DispatchFromDyn`
683// and become dyn-compatible method receivers.
684// Note that currently `Cell` itself cannot be a method receiver
685// because it does not implement Deref.
686// In other words:
687// `self: Cell<&Self>` won't work
688// `self: CellWrapper<Self>` becomes possible
689#[unstable(feature = "dispatch_from_dyn", issue = "none")]
690impl<T: DispatchFromDyn<U>, U> DispatchFromDyn<Cell<U>> for Cell<T> {}
691
692#[stable(feature = "more_conversion_trait_impls", since = "1.95.0")]
693impl<T, const N: usize> AsRef<[Cell<T>; N]> for Cell<[T; N]> {
694    #[inline]
695    fn as_ref(&self) -> &[Cell<T>; N] {
696        self.as_array_of_cells()
697    }
698}
699
700#[stable(feature = "more_conversion_trait_impls", since = "1.95.0")]
701impl<T, const N: usize> AsRef<[Cell<T>]> for Cell<[T; N]> {
702    #[inline]
703    fn as_ref(&self) -> &[Cell<T>] {
704        &*self.as_array_of_cells()
705    }
706}
707
708#[stable(feature = "more_conversion_trait_impls", since = "1.95.0")]
709impl<T> AsRef<[Cell<T>]> for Cell<[T]> {
710    #[inline]
711    fn as_ref(&self) -> &[Cell<T>] {
712        self.as_slice_of_cells()
713    }
714}
715
716impl<T> Cell<[T]> {
717    /// Returns a `&[Cell<T>]` from a `&Cell<[T]>`
718    ///
719    /// # Examples
720    ///
721    /// ```
722    /// use std::cell::Cell;
723    ///
724    /// let slice: &mut [i32] = &mut [1, 2, 3];
725    /// let cell_slice: &Cell<[i32]> = Cell::from_mut(slice);
726    /// let slice_cell: &[Cell<i32>] = cell_slice.as_slice_of_cells();
727    ///
728    /// assert_eq!(slice_cell.len(), 3);
729    /// ```
730    #[stable(feature = "as_cell", since = "1.37.0")]
731    #[rustc_const_stable(feature = "const_cell", since = "1.88.0")]
732    pub const fn as_slice_of_cells(&self) -> &[Cell<T>] {
733        // SAFETY: `Cell<T>` has the same memory layout as `T`.
734        unsafe { &*(self as *const Cell<[T]> as *const [Cell<T>]) }
735    }
736}
737
738impl<T, const N: usize> Cell<[T; N]> {
739    /// Returns a `&[Cell<T>; N]` from a `&Cell<[T; N]>`
740    ///
741    /// # Examples
742    ///
743    /// ```
744    /// use std::cell::Cell;
745    ///
746    /// let mut array: [i32; 3] = [1, 2, 3];
747    /// let cell_array: &Cell<[i32; 3]> = Cell::from_mut(&mut array);
748    /// let array_cell: &[Cell<i32>; 3] = cell_array.as_array_of_cells();
749    /// ```
750    #[stable(feature = "as_array_of_cells", since = "1.91.0")]
751    #[rustc_const_stable(feature = "as_array_of_cells", since = "1.91.0")]
752    pub const fn as_array_of_cells(&self) -> &[Cell<T>; N] {
753        // SAFETY: `Cell<T>` has the same memory layout as `T`.
754        unsafe { &*(self as *const Cell<[T; N]> as *const [Cell<T>; N]) }
755    }
756}
757
758/// Types for which cloning `Cell<Self>` is sound.
759///
760/// # Safety
761///
762/// Implementing this trait for a type is sound if and only if the following code is sound for T =
763/// that type.
764///
765/// ```
766/// #![feature(cell_get_cloned)]
767/// # use std::cell::{CloneFromCell, Cell};
768/// fn clone_from_cell<T: CloneFromCell>(cell: &Cell<T>) -> T {
769///     unsafe { T::clone(&*cell.as_ptr()) }
770/// }
771/// ```
772///
773/// Importantly, you can't just implement `CloneFromCell` for any arbitrary `Copy` type, e.g. the
774/// following is unsound:
775///
776/// ```rust
777/// # use std::cell::Cell;
778///
779/// #[derive(Copy, Debug)]
780/// pub struct Bad<'a>(Option<&'a Cell<Bad<'a>>>, u8);
781///
782/// impl Clone for Bad<'_> {
783///     fn clone(&self) -> Self {
784///         let a: &u8 = &self.1;
785///         // when self.0 points to self, we write to self.1 while we have a live `&u8` pointing to
786///         // it -- this is UB
787///         self.0.unwrap().set(Self(None, 1));
788///         dbg!((a, self));
789///         Self(None, 0)
790///     }
791/// }
792///
793/// // this is not sound
794/// // unsafe impl CloneFromCell for Bad<'_> {}
795/// ```
796#[unstable(feature = "cell_get_cloned", issue = "145329")]
797// Allow potential overlapping implementations in user code
798#[marker]
799pub unsafe trait CloneFromCell: Clone {}
800
801// `CloneFromCell` can be implemented for types that don't have indirection and which don't access
802// `Cell`s in their `Clone` implementation. A commonly-used subset is covered here.
803#[unstable(feature = "cell_get_cloned", issue = "145329")]
804unsafe impl<T: CloneFromCell, const N: usize> CloneFromCell for [T; N] {}
805#[unstable(feature = "cell_get_cloned", issue = "145329")]
806unsafe impl<T: CloneFromCell> CloneFromCell for Option<T> {}
807#[unstable(feature = "cell_get_cloned", issue = "145329")]
808unsafe impl<T: CloneFromCell, E: CloneFromCell> CloneFromCell for Result<T, E> {}
809#[unstable(feature = "cell_get_cloned", issue = "145329")]
810unsafe impl<T: ?Sized> CloneFromCell for PhantomData<T> {}
811#[unstable(feature = "cell_get_cloned", issue = "145329")]
812unsafe impl<T: CloneFromCell> CloneFromCell for ManuallyDrop<T> {}
813#[unstable(feature = "cell_get_cloned", issue = "145329")]
814unsafe impl<T: CloneFromCell> CloneFromCell for ops::Range<T> {}
815#[unstable(feature = "cell_get_cloned", issue = "145329")]
816unsafe impl<T: CloneFromCell> CloneFromCell for range::Range<T> {}
817
818#[unstable(feature = "cell_get_cloned", issue = "145329")]
819impl<T: CloneFromCell> Cell<T> {
820    /// Get a clone of the `Cell` that contains a copy of the original value.
821    ///
822    /// This allows a cheaply `Clone`-able type like an `Rc` to be stored in a `Cell`, exposing the
823    /// cheaper `clone()` method.
824    ///
825    /// # Examples
826    ///
827    /// ```
828    /// #![feature(cell_get_cloned)]
829    ///
830    /// use core::cell::Cell;
831    /// use std::rc::Rc;
832    ///
833    /// let rc = Rc::new(1usize);
834    /// let c1 = Cell::new(rc);
835    /// let c2 = c1.get_cloned();
836    /// assert_eq!(*c2.into_inner(), 1);
837    /// ```
838    pub fn get_cloned(&self) -> Self {
839        // SAFETY: T is CloneFromCell, which guarantees that this is sound.
840        Cell::new(T::clone(unsafe { &*self.as_ptr() }))
841    }
842}
843
844/// A mutable memory location with dynamically checked borrow rules
845///
846/// See the [module-level documentation](self) for more.
847#[rustc_diagnostic_item = "RefCell"]
848#[stable(feature = "rust1", since = "1.0.0")]
849pub struct RefCell<T: ?Sized> {
850    borrow: Cell<BorrowCounter>,
851    // Stores the location of the earliest currently active borrow.
852    // This gets updated whenever we go from having zero borrows
853    // to having a single borrow. When a borrow occurs, this gets included
854    // in the generated `BorrowError`/`BorrowMutError`
855    #[cfg(feature = "debug_refcell")]
856    borrowed_at: Cell<Option<&'static crate::panic::Location<'static>>>,
857    value: UnsafeCell<T>,
858}
859
860/// An error returned by [`RefCell::try_borrow`].
861#[stable(feature = "try_borrow", since = "1.13.0")]
862#[non_exhaustive]
863#[derive(Debug)]
864pub struct BorrowError {
865    #[cfg(feature = "debug_refcell")]
866    location: &'static crate::panic::Location<'static>,
867}
868
869#[stable(feature = "try_borrow", since = "1.13.0")]
870impl Display for BorrowError {
871    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
872        #[cfg(feature = "debug_refcell")]
873        let res = write!(
874            f,
875            "RefCell already mutably borrowed; a previous borrow was at {}",
876            self.location
877        );
878
879        #[cfg(not(feature = "debug_refcell"))]
880        let res = Display::fmt("RefCell already mutably borrowed", f);
881
882        res
883    }
884}
885
886/// An error returned by [`RefCell::try_borrow_mut`].
887#[stable(feature = "try_borrow", since = "1.13.0")]
888#[non_exhaustive]
889#[derive(Debug)]
890pub struct BorrowMutError {
891    #[cfg(feature = "debug_refcell")]
892    location: &'static crate::panic::Location<'static>,
893}
894
895#[stable(feature = "try_borrow", since = "1.13.0")]
896impl Display for BorrowMutError {
897    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
898        #[cfg(feature = "debug_refcell")]
899        let res = write!(f, "RefCell already borrowed; a previous borrow was at {}", self.location);
900
901        #[cfg(not(feature = "debug_refcell"))]
902        let res = Display::fmt("RefCell already borrowed", f);
903
904        res
905    }
906}
907
908// This ensures the panicking code is outlined from `borrow_mut` for `RefCell`.
909#[cfg_attr(not(panic = "immediate-abort"), inline(never))]
910#[track_caller]
911#[cold]
912const fn panic_already_borrowed(err: BorrowMutError) -> ! {
913    const_panic!(
914        "RefCell already borrowed",
915        "{err}",
916        err: BorrowMutError = err,
917    )
918}
919
920// This ensures the panicking code is outlined from `borrow` for `RefCell`.
921#[cfg_attr(not(panic = "immediate-abort"), inline(never))]
922#[track_caller]
923#[cold]
924const fn panic_already_mutably_borrowed(err: BorrowError) -> ! {
925    const_panic!(
926        "RefCell already mutably borrowed",
927        "{err}",
928        err: BorrowError = err,
929    )
930}
931
932// Positive values represent the number of `Ref` active. Negative values
933// represent the number of `RefMut` active. Multiple `RefMut`s can only be
934// active at a time if they refer to distinct, nonoverlapping components of a
935// `RefCell` (e.g., different ranges of a slice).
936//
937// `Ref` and `RefMut` are both two words in size, and so there will likely never
938// be enough `Ref`s or `RefMut`s in existence to overflow half of the `usize`
939// range. Thus, a `BorrowCounter` will probably never overflow or underflow.
940// However, this is not a guarantee, as a pathological program could repeatedly
941// create and then mem::forget `Ref`s or `RefMut`s. Thus, all code must
942// explicitly check for overflow and underflow in order to avoid unsafety, or at
943// least behave correctly in the event that overflow or underflow happens (e.g.,
944// see BorrowRef::new).
945type BorrowCounter = isize;
946const UNUSED: BorrowCounter = 0;
947
948#[inline(always)]
949const fn is_writing(x: BorrowCounter) -> bool {
950    x < UNUSED
951}
952
953#[inline(always)]
954const fn is_reading(x: BorrowCounter) -> bool {
955    x > UNUSED
956}
957
958impl<T> RefCell<T> {
959    /// Creates a new `RefCell` containing `value`.
960    ///
961    /// # Examples
962    ///
963    /// ```
964    /// use std::cell::RefCell;
965    ///
966    /// let c = RefCell::new(5);
967    /// ```
968    #[stable(feature = "rust1", since = "1.0.0")]
969    #[rustc_const_stable(feature = "const_refcell_new", since = "1.24.0")]
970    #[inline]
971    pub const fn new(value: T) -> RefCell<T> {
972        RefCell {
973            value: UnsafeCell::new(value),
974            borrow: Cell::new(UNUSED),
975            #[cfg(feature = "debug_refcell")]
976            borrowed_at: Cell::new(None),
977        }
978    }
979
980    /// Consumes the `RefCell`, returning the wrapped value.
981    ///
982    /// # Examples
983    ///
984    /// ```
985    /// use std::cell::RefCell;
986    ///
987    /// let c = RefCell::new(5);
988    ///
989    /// let five = c.into_inner();
990    /// ```
991    #[stable(feature = "rust1", since = "1.0.0")]
992    #[rustc_const_stable(feature = "const_cell_into_inner", since = "1.83.0")]
993    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
994    #[inline]
995    pub const fn into_inner(self) -> T {
996        // Since this function takes `self` (the `RefCell`) by value, the
997        // compiler statically verifies that it is not currently borrowed.
998        self.value.into_inner()
999    }
1000
1001    /// Replaces the wrapped value with a new one, returning the old value,
1002    /// without deinitializing either one.
1003    ///
1004    /// This function corresponds to [`std::mem::replace`](../mem/fn.replace.html).
1005    ///
1006    /// # Panics
1007    ///
1008    /// Panics if the value is currently borrowed.
1009    ///
1010    /// # Examples
1011    ///
1012    /// ```
1013    /// use std::cell::RefCell;
1014    /// let cell = RefCell::new(5);
1015    /// let old_value = cell.replace(6);
1016    /// assert_eq!(old_value, 5);
1017    /// assert_eq!(cell, RefCell::new(6));
1018    /// ```
1019    #[inline]
1020    #[stable(feature = "refcell_replace", since = "1.24.0")]
1021    #[track_caller]
1022    #[rustc_confusables("swap")]
1023    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1024    #[rustc_should_not_be_called_on_const_items]
1025    pub const fn replace(&self, t: T) -> T {
1026        mem::replace(&mut self.borrow_mut(), t)
1027    }
1028
1029    /// Replaces the wrapped value with a new one computed from `f`, returning
1030    /// the old value, without deinitializing either one.
1031    ///
1032    /// # Panics
1033    ///
1034    /// Panics if the value is currently borrowed.
1035    ///
1036    /// # Examples
1037    ///
1038    /// ```
1039    /// use std::cell::RefCell;
1040    /// let cell = RefCell::new(5);
1041    /// let old_value = cell.replace_with(|&mut old| old + 1);
1042    /// assert_eq!(old_value, 5);
1043    /// assert_eq!(cell, RefCell::new(6));
1044    /// ```
1045    #[inline]
1046    #[stable(feature = "refcell_replace_swap", since = "1.35.0")]
1047    #[track_caller]
1048    #[rustc_should_not_be_called_on_const_items]
1049    pub fn replace_with<F: FnOnce(&mut T) -> T>(&self, f: F) -> T {
1050        let mut_borrow = &mut *self.borrow_mut();
1051        let replacement = f(mut_borrow);
1052        mem::replace(mut_borrow, replacement)
1053    }
1054
1055    /// Swaps the wrapped value of `self` with the wrapped value of `other`,
1056    /// without deinitializing either one.
1057    ///
1058    /// This function corresponds to [`std::mem::swap`](../mem/fn.swap.html).
1059    ///
1060    /// # Panics
1061    ///
1062    /// Panics if the value in either `RefCell` is currently borrowed, or
1063    /// if `self` and `other` point to the same `RefCell`.
1064    ///
1065    /// # Examples
1066    ///
1067    /// ```
1068    /// use std::cell::RefCell;
1069    /// let c = RefCell::new(5);
1070    /// let d = RefCell::new(6);
1071    /// c.swap(&d);
1072    /// assert_eq!(c, RefCell::new(6));
1073    /// assert_eq!(d, RefCell::new(5));
1074    /// ```
1075    #[inline]
1076    #[stable(feature = "refcell_swap", since = "1.24.0")]
1077    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1078    #[rustc_should_not_be_called_on_const_items]
1079    pub const fn swap(&self, other: &Self) {
1080        mem::swap(&mut *self.borrow_mut(), &mut *other.borrow_mut())
1081    }
1082}
1083
1084impl<T: ?Sized> RefCell<T> {
1085    /// Immutably borrows the wrapped value.
1086    ///
1087    /// The borrow lasts until the returned `Ref` exits scope. Multiple
1088    /// immutable borrows can be taken out at the same time.
1089    ///
1090    /// # Panics
1091    ///
1092    /// Panics if the value is currently mutably borrowed. For a non-panicking variant, use
1093    /// [`try_borrow`](#method.try_borrow).
1094    ///
1095    /// # Examples
1096    ///
1097    /// ```
1098    /// use std::cell::RefCell;
1099    ///
1100    /// let c = RefCell::new(5);
1101    ///
1102    /// let borrowed_five = c.borrow();
1103    /// let borrowed_five2 = c.borrow();
1104    /// ```
1105    ///
1106    /// An example of panic:
1107    ///
1108    /// ```should_panic
1109    /// use std::cell::RefCell;
1110    ///
1111    /// let c = RefCell::new(5);
1112    ///
1113    /// let m = c.borrow_mut();
1114    /// let b = c.borrow(); // this causes a panic
1115    /// ```
1116    #[stable(feature = "rust1", since = "1.0.0")]
1117    #[inline]
1118    #[track_caller]
1119    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1120    #[rustc_should_not_be_called_on_const_items]
1121    pub const fn borrow(&self) -> Ref<'_, T> {
1122        match self.try_borrow() {
1123            Ok(b) => b,
1124            Err(err) => panic_already_mutably_borrowed(err),
1125        }
1126    }
1127
1128    /// Immutably borrows the wrapped value, returning an error if the value is currently mutably
1129    /// borrowed.
1130    ///
1131    /// The borrow lasts until the returned `Ref` exits scope. Multiple immutable borrows can be
1132    /// taken out at the same time.
1133    ///
1134    /// This is the non-panicking variant of [`borrow`](#method.borrow).
1135    ///
1136    /// # Examples
1137    ///
1138    /// ```
1139    /// use std::cell::RefCell;
1140    ///
1141    /// let c = RefCell::new(5);
1142    ///
1143    /// {
1144    ///     let m = c.borrow_mut();
1145    ///     assert!(c.try_borrow().is_err());
1146    /// }
1147    ///
1148    /// {
1149    ///     let m = c.borrow();
1150    ///     assert!(c.try_borrow().is_ok());
1151    /// }
1152    /// ```
1153    #[stable(feature = "try_borrow", since = "1.13.0")]
1154    #[inline]
1155    #[cfg_attr(feature = "debug_refcell", track_caller)]
1156    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1157    #[rustc_should_not_be_called_on_const_items]
1158    pub const fn try_borrow(&self) -> Result<Ref<'_, T>, BorrowError> {
1159        match BorrowRef::new(&self.borrow) {
1160            Some(b) => {
1161                #[cfg(feature = "debug_refcell")]
1162                {
1163                    // `borrowed_at` is always the *first* active borrow
1164                    if b.borrow.get() == 1 {
1165                        self.borrowed_at.replace(Some(crate::panic::Location::caller()));
1166                    }
1167                }
1168
1169                // SAFETY: `BorrowRef` ensures that there is only immutable access
1170                // to the value while borrowed.
1171                let value = unsafe { NonNull::new_unchecked(self.value.get()) };
1172                Ok(Ref { value, borrow: b })
1173            }
1174            None => Err(BorrowError {
1175                // If a borrow occurred, then we must already have an outstanding borrow,
1176                // so `borrowed_at` will be `Some`
1177                #[cfg(feature = "debug_refcell")]
1178                location: self.borrowed_at.get().unwrap(),
1179            }),
1180        }
1181    }
1182
1183    /// Mutably borrows the wrapped value.
1184    ///
1185    /// The borrow lasts until the returned `RefMut` or all `RefMut`s derived
1186    /// from it exit scope. The value cannot be borrowed while this borrow is
1187    /// active.
1188    ///
1189    /// # Panics
1190    ///
1191    /// Panics if the value is currently borrowed. For a non-panicking variant, use
1192    /// [`try_borrow_mut`](#method.try_borrow_mut).
1193    ///
1194    /// # Examples
1195    ///
1196    /// ```
1197    /// use std::cell::RefCell;
1198    ///
1199    /// let c = RefCell::new("hello".to_owned());
1200    ///
1201    /// *c.borrow_mut() = "bonjour".to_owned();
1202    ///
1203    /// assert_eq!(&*c.borrow(), "bonjour");
1204    /// ```
1205    ///
1206    /// An example of panic:
1207    ///
1208    /// ```should_panic
1209    /// use std::cell::RefCell;
1210    ///
1211    /// let c = RefCell::new(5);
1212    /// let m = c.borrow();
1213    ///
1214    /// let b = c.borrow_mut(); // this causes a panic
1215    /// ```
1216    #[stable(feature = "rust1", since = "1.0.0")]
1217    #[inline]
1218    #[track_caller]
1219    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1220    #[rustc_should_not_be_called_on_const_items]
1221    pub const fn borrow_mut(&self) -> RefMut<'_, T> {
1222        match self.try_borrow_mut() {
1223            Ok(b) => b,
1224            Err(err) => panic_already_borrowed(err),
1225        }
1226    }
1227
1228    /// Mutably borrows the wrapped value, returning an error if the value is currently borrowed.
1229    ///
1230    /// The borrow lasts until the returned `RefMut` or all `RefMut`s derived
1231    /// from it exit scope. The value cannot be borrowed while this borrow is
1232    /// active.
1233    ///
1234    /// This is the non-panicking variant of [`borrow_mut`](#method.borrow_mut).
1235    ///
1236    /// # Examples
1237    ///
1238    /// ```
1239    /// use std::cell::RefCell;
1240    ///
1241    /// let c = RefCell::new(5);
1242    ///
1243    /// {
1244    ///     let m = c.borrow();
1245    ///     assert!(c.try_borrow_mut().is_err());
1246    /// }
1247    ///
1248    /// assert!(c.try_borrow_mut().is_ok());
1249    /// ```
1250    #[stable(feature = "try_borrow", since = "1.13.0")]
1251    #[inline]
1252    #[cfg_attr(feature = "debug_refcell", track_caller)]
1253    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1254    #[rustc_should_not_be_called_on_const_items]
1255    pub const fn try_borrow_mut(&self) -> Result<RefMut<'_, T>, BorrowMutError> {
1256        match BorrowRefMut::new(&self.borrow) {
1257            Some(b) => {
1258                #[cfg(feature = "debug_refcell")]
1259                {
1260                    self.borrowed_at.replace(Some(crate::panic::Location::caller()));
1261                }
1262
1263                // SAFETY: `BorrowRefMut` guarantees unique access.
1264                let value = unsafe { NonNull::new_unchecked(self.value.get()) };
1265                Ok(RefMut { value, borrow: b, marker: PhantomData })
1266            }
1267            None => Err(BorrowMutError {
1268                // If a borrow occurred, then we must already have an outstanding borrow,
1269                // so `borrowed_at` will be `Some`
1270                #[cfg(feature = "debug_refcell")]
1271                location: self.borrowed_at.get().unwrap(),
1272            }),
1273        }
1274    }
1275
1276    /// Returns a raw pointer to the underlying data in this cell.
1277    ///
1278    /// # Examples
1279    ///
1280    /// ```
1281    /// use std::cell::RefCell;
1282    ///
1283    /// let c = RefCell::new(5);
1284    ///
1285    /// let ptr = c.as_ptr();
1286    /// ```
1287    #[inline]
1288    #[stable(feature = "cell_as_ptr", since = "1.12.0")]
1289    #[rustc_as_ptr]
1290    #[rustc_never_returns_null_ptr]
1291    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1292    pub const fn as_ptr(&self) -> *mut T {
1293        self.value.get()
1294    }
1295
1296    /// Returns a mutable reference to the underlying data.
1297    ///
1298    /// Since this method borrows `RefCell` mutably, it is statically guaranteed
1299    /// that no borrows to the underlying data exist. The dynamic checks inherent
1300    /// in [`borrow_mut`] and most other methods of `RefCell` are therefore
1301    /// unnecessary. Note that this method does not reset the borrowing state if borrows were previously leaked
1302    /// (e.g., via [`forget()`] on a [`Ref`] or [`RefMut`]). For that purpose,
1303    /// consider using the unstable [`undo_leak`] method.
1304    ///
1305    /// This method can only be called if `RefCell` can be mutably borrowed,
1306    /// which in general is only the case directly after the `RefCell` has
1307    /// been created. In these situations, skipping the aforementioned dynamic
1308    /// borrowing checks may yield better ergonomics and runtime-performance.
1309    ///
1310    /// In most situations where `RefCell` is used, it can't be borrowed mutably.
1311    /// Use [`borrow_mut`] to get mutable access to the underlying data then.
1312    ///
1313    /// [`borrow_mut`]: RefCell::borrow_mut()
1314    /// [`forget()`]: mem::forget
1315    /// [`undo_leak`]: RefCell::undo_leak()
1316    ///
1317    /// # Examples
1318    ///
1319    /// ```
1320    /// use std::cell::RefCell;
1321    ///
1322    /// let mut c = RefCell::new(5);
1323    /// *c.get_mut() += 1;
1324    ///
1325    /// assert_eq!(c, RefCell::new(6));
1326    /// ```
1327    #[inline]
1328    #[stable(feature = "cell_get_mut", since = "1.11.0")]
1329    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1330    pub const fn get_mut(&mut self) -> &mut T {
1331        self.value.get_mut()
1332    }
1333
1334    /// Undo the effect of leaked guards on the borrow state of the `RefCell`.
1335    ///
1336    /// This call is similar to [`get_mut`] but more specialized. It borrows `RefCell` mutably to
1337    /// ensure no borrows exist and then resets the state tracking shared borrows. This is relevant
1338    /// if some `Ref` or `RefMut` borrows have been leaked.
1339    ///
1340    /// [`get_mut`]: RefCell::get_mut()
1341    ///
1342    /// # Examples
1343    ///
1344    /// ```
1345    /// #![feature(cell_leak)]
1346    /// use std::cell::RefCell;
1347    ///
1348    /// let mut c = RefCell::new(0);
1349    /// std::mem::forget(c.borrow_mut());
1350    ///
1351    /// assert!(c.try_borrow().is_err());
1352    /// c.undo_leak();
1353    /// assert!(c.try_borrow().is_ok());
1354    /// ```
1355    #[unstable(feature = "cell_leak", issue = "69099")]
1356    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1357    pub const fn undo_leak(&mut self) -> &mut T {
1358        *self.borrow.get_mut() = UNUSED;
1359        self.get_mut()
1360    }
1361
1362    /// Immutably borrows the wrapped value, returning an error if the value is
1363    /// currently mutably borrowed.
1364    ///
1365    /// # Safety
1366    ///
1367    /// Unlike `RefCell::borrow`, this method is unsafe because it does not
1368    /// return a `Ref`, thus leaving the borrow flag untouched. Mutably
1369    /// borrowing the `RefCell` while the reference returned by this method
1370    /// is alive is undefined behavior.
1371    ///
1372    /// # Examples
1373    ///
1374    /// ```
1375    /// use std::cell::RefCell;
1376    ///
1377    /// let c = RefCell::new(5);
1378    ///
1379    /// {
1380    ///     let m = c.borrow_mut();
1381    ///     assert!(unsafe { c.try_borrow_unguarded() }.is_err());
1382    /// }
1383    ///
1384    /// {
1385    ///     let m = c.borrow();
1386    ///     assert!(unsafe { c.try_borrow_unguarded() }.is_ok());
1387    /// }
1388    /// ```
1389    #[stable(feature = "borrow_state", since = "1.37.0")]
1390    #[inline]
1391    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1392    pub const unsafe fn try_borrow_unguarded(&self) -> Result<&T, BorrowError> {
1393        if !is_writing(self.borrow.get()) {
1394            // SAFETY: We check that nobody is actively writing now, but it is
1395            // the caller's responsibility to ensure that nobody writes until
1396            // the returned reference is no longer in use.
1397            // Also, `self.value.get()` refers to the value owned by `self`
1398            // and is thus guaranteed to be valid for the lifetime of `self`.
1399            Ok(unsafe { &*self.value.get() })
1400        } else {
1401            Err(BorrowError {
1402                // If a borrow occurred, then we must already have an outstanding borrow,
1403                // so `borrowed_at` will be `Some`
1404                #[cfg(feature = "debug_refcell")]
1405                location: self.borrowed_at.get().unwrap(),
1406            })
1407        }
1408    }
1409}
1410
1411impl<T: Default> RefCell<T> {
1412    /// Takes the wrapped value, leaving `Default::default()` in its place.
1413    ///
1414    /// # Panics
1415    ///
1416    /// Panics if the value is currently borrowed.
1417    ///
1418    /// # Examples
1419    ///
1420    /// ```
1421    /// use std::cell::RefCell;
1422    ///
1423    /// let c = RefCell::new(5);
1424    /// let five = c.take();
1425    ///
1426    /// assert_eq!(five, 5);
1427    /// assert_eq!(c.into_inner(), 0);
1428    /// ```
1429    #[stable(feature = "refcell_take", since = "1.50.0")]
1430    pub fn take(&self) -> T {
1431        self.replace(Default::default())
1432    }
1433}
1434
1435#[stable(feature = "rust1", since = "1.0.0")]
1436unsafe impl<T: ?Sized> Send for RefCell<T> where T: Send {}
1437
1438#[stable(feature = "rust1", since = "1.0.0")]
1439impl<T: ?Sized> !Sync for RefCell<T> {}
1440
1441#[stable(feature = "rust1", since = "1.0.0")]
1442impl<T: Clone> Clone for RefCell<T> {
1443    /// # Panics
1444    ///
1445    /// Panics if the value is currently mutably borrowed.
1446    #[inline]
1447    #[track_caller]
1448    fn clone(&self) -> RefCell<T> {
1449        RefCell::new(self.borrow().clone())
1450    }
1451
1452    /// # Panics
1453    ///
1454    /// Panics if `source` is currently mutably borrowed.
1455    #[inline]
1456    #[track_caller]
1457    fn clone_from(&mut self, source: &Self) {
1458        self.get_mut().clone_from(&source.borrow())
1459    }
1460}
1461
1462#[stable(feature = "rust1", since = "1.0.0")]
1463#[rustc_const_unstable(feature = "const_default", issue = "143894")]
1464impl<T: [const] Default> const Default for RefCell<T> {
1465    /// Creates a `RefCell<T>`, with the `Default` value for T.
1466    #[inline]
1467    fn default() -> RefCell<T> {
1468        RefCell::new(Default::default())
1469    }
1470}
1471
1472#[stable(feature = "rust1", since = "1.0.0")]
1473impl<T: ?Sized + PartialEq> PartialEq for RefCell<T> {
1474    /// # Panics
1475    ///
1476    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1477    #[inline]
1478    fn eq(&self, other: &RefCell<T>) -> bool {
1479        *self.borrow() == *other.borrow()
1480    }
1481}
1482
1483#[stable(feature = "cell_eq", since = "1.2.0")]
1484impl<T: ?Sized + Eq> Eq for RefCell<T> {}
1485
1486#[stable(feature = "cell_ord", since = "1.10.0")]
1487impl<T: ?Sized + PartialOrd> PartialOrd for RefCell<T> {
1488    /// # Panics
1489    ///
1490    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1491    #[inline]
1492    fn partial_cmp(&self, other: &RefCell<T>) -> Option<Ordering> {
1493        self.borrow().partial_cmp(&*other.borrow())
1494    }
1495
1496    /// # Panics
1497    ///
1498    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1499    #[inline]
1500    fn lt(&self, other: &RefCell<T>) -> bool {
1501        *self.borrow() < *other.borrow()
1502    }
1503
1504    /// # Panics
1505    ///
1506    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1507    #[inline]
1508    fn le(&self, other: &RefCell<T>) -> bool {
1509        *self.borrow() <= *other.borrow()
1510    }
1511
1512    /// # Panics
1513    ///
1514    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1515    #[inline]
1516    fn gt(&self, other: &RefCell<T>) -> bool {
1517        *self.borrow() > *other.borrow()
1518    }
1519
1520    /// # Panics
1521    ///
1522    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1523    #[inline]
1524    fn ge(&self, other: &RefCell<T>) -> bool {
1525        *self.borrow() >= *other.borrow()
1526    }
1527}
1528
1529#[stable(feature = "cell_ord", since = "1.10.0")]
1530impl<T: ?Sized + Ord> Ord for RefCell<T> {
1531    /// # Panics
1532    ///
1533    /// Panics if the value in either `RefCell` is currently mutably borrowed.
1534    #[inline]
1535    fn cmp(&self, other: &RefCell<T>) -> Ordering {
1536        self.borrow().cmp(&*other.borrow())
1537    }
1538}
1539
1540#[stable(feature = "cell_from", since = "1.12.0")]
1541#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1542impl<T> const From<T> for RefCell<T> {
1543    /// Creates a new `RefCell<T>` containing the given value.
1544    fn from(t: T) -> RefCell<T> {
1545        RefCell::new(t)
1546    }
1547}
1548
1549#[unstable(feature = "coerce_unsized", issue = "18598")]
1550impl<T: CoerceUnsized<U>, U> CoerceUnsized<RefCell<U>> for RefCell<T> {}
1551
1552struct BorrowRef<'b> {
1553    borrow: &'b Cell<BorrowCounter>,
1554}
1555
1556impl<'b> BorrowRef<'b> {
1557    #[inline]
1558    const fn new(borrow: &'b Cell<BorrowCounter>) -> Option<BorrowRef<'b>> {
1559        let b = borrow.get().wrapping_add(1);
1560        if !is_reading(b) {
1561            // Incrementing borrow can result in a non-reading value (<= 0) in these cases:
1562            // 1. It was < 0, i.e. there are writing borrows, so we can't allow a read borrow
1563            //    due to Rust's reference aliasing rules
1564            // 2. It was isize::MAX (the max amount of reading borrows) and it overflowed
1565            //    into isize::MIN (the max amount of writing borrows) so we can't allow
1566            //    an additional read borrow because isize can't represent so many read borrows
1567            //    (this can only happen if you mem::forget more than a small constant amount of
1568            //    `Ref`s, which is not good practice)
1569            None
1570        } else {
1571            // Incrementing borrow can result in a reading value (> 0) in these cases:
1572            // 1. It was = 0, i.e. it wasn't borrowed, and we are taking the first read borrow
1573            // 2. It was > 0 and < isize::MAX, i.e. there were read borrows, and isize
1574            //    is large enough to represent having one more read borrow
1575            borrow.replace(b);
1576            Some(BorrowRef { borrow })
1577        }
1578    }
1579}
1580
1581#[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1582impl const Drop for BorrowRef<'_> {
1583    #[inline]
1584    fn drop(&mut self) {
1585        let borrow = self.borrow.get();
1586        debug_assert!(is_reading(borrow));
1587        self.borrow.replace(borrow - 1);
1588    }
1589}
1590
1591#[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1592impl const Clone for BorrowRef<'_> {
1593    #[inline]
1594    fn clone(&self) -> Self {
1595        // Since this Ref exists, we know the borrow flag
1596        // is a reading borrow.
1597        let borrow = self.borrow.get();
1598        debug_assert!(is_reading(borrow));
1599        // Prevent the borrow counter from overflowing into
1600        // a writing borrow.
1601        assert!(borrow != BorrowCounter::MAX);
1602        self.borrow.replace(borrow + 1);
1603        BorrowRef { borrow: self.borrow }
1604    }
1605}
1606
1607/// Wraps a borrowed reference to a value in a `RefCell` box.
1608/// A wrapper type for an immutably borrowed value from a `RefCell<T>`.
1609///
1610/// See the [module-level documentation](self) for more.
1611#[stable(feature = "rust1", since = "1.0.0")]
1612#[must_not_suspend = "holding a Ref across suspend points can cause BorrowErrors"]
1613#[rustc_diagnostic_item = "RefCellRef"]
1614pub struct Ref<'b, T: ?Sized + 'b> {
1615    // NB: we use a pointer instead of `&'b T` to avoid `noalias` violations, because a
1616    // `Ref` argument doesn't hold immutability for its whole scope, only until it drops.
1617    // `NonNull` is also covariant over `T`, just like we would have with `&T`.
1618    value: NonNull<T>,
1619    borrow: BorrowRef<'b>,
1620}
1621
1622#[stable(feature = "rust1", since = "1.0.0")]
1623#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1624impl<T: ?Sized> const Deref for Ref<'_, T> {
1625    type Target = T;
1626
1627    #[inline]
1628    fn deref(&self) -> &T {
1629        // SAFETY: the value is accessible as long as we hold our borrow.
1630        unsafe { self.value.as_ref() }
1631    }
1632}
1633
1634#[unstable(feature = "deref_pure_trait", issue = "87121")]
1635unsafe impl<T: ?Sized> DerefPure for Ref<'_, T> {}
1636
1637impl<'b, T: ?Sized> Ref<'b, T> {
1638    /// Copies a `Ref`.
1639    ///
1640    /// The `RefCell` is already immutably borrowed, so this cannot fail.
1641    ///
1642    /// This is an associated function that needs to be used as
1643    /// `Ref::clone(...)`. A `Clone` implementation or a method would interfere
1644    /// with the widespread use of `r.borrow().clone()` to clone the contents of
1645    /// a `RefCell`.
1646    #[stable(feature = "cell_extras", since = "1.15.0")]
1647    #[must_use]
1648    #[inline]
1649    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1650    pub const fn clone(orig: &Ref<'b, T>) -> Ref<'b, T> {
1651        Ref { value: orig.value, borrow: orig.borrow.clone() }
1652    }
1653
1654    /// Makes a new `Ref` for a component of the borrowed data.
1655    ///
1656    /// The `RefCell` is already immutably borrowed, so this cannot fail.
1657    ///
1658    /// This is an associated function that needs to be used as `Ref::map(...)`.
1659    /// A method would interfere with methods of the same name on the contents
1660    /// of a `RefCell` used through `Deref`.
1661    ///
1662    /// # Examples
1663    ///
1664    /// ```
1665    /// use std::cell::{RefCell, Ref};
1666    ///
1667    /// let c = RefCell::new((5, 'b'));
1668    /// let b1: Ref<'_, (u32, char)> = c.borrow();
1669    /// let b2: Ref<'_, u32> = Ref::map(b1, |t| &t.0);
1670    /// assert_eq!(*b2, 5)
1671    /// ```
1672    #[stable(feature = "cell_map", since = "1.8.0")]
1673    #[inline]
1674    pub fn map<U: ?Sized, F>(orig: Ref<'b, T>, f: F) -> Ref<'b, U>
1675    where
1676        F: FnOnce(&T) -> &U,
1677    {
1678        Ref { value: NonNull::from(f(&*orig)), borrow: orig.borrow }
1679    }
1680
1681    /// Makes a new `Ref` for an optional component of the borrowed data. The
1682    /// original guard is returned as an `Err(..)` if the closure returns
1683    /// `None`.
1684    ///
1685    /// The `RefCell` is already immutably borrowed, so this cannot fail.
1686    ///
1687    /// This is an associated function that needs to be used as
1688    /// `Ref::filter_map(...)`. A method would interfere with methods of the same
1689    /// name on the contents of a `RefCell` used through `Deref`.
1690    ///
1691    /// # Examples
1692    ///
1693    /// ```
1694    /// use std::cell::{RefCell, Ref};
1695    ///
1696    /// let c = RefCell::new(vec![1, 2, 3]);
1697    /// let b1: Ref<'_, Vec<u32>> = c.borrow();
1698    /// let b2: Result<Ref<'_, u32>, _> = Ref::filter_map(b1, |v| v.get(1));
1699    /// assert_eq!(*b2.unwrap(), 2);
1700    /// ```
1701    #[stable(feature = "cell_filter_map", since = "1.63.0")]
1702    #[inline]
1703    pub fn filter_map<U: ?Sized, F>(orig: Ref<'b, T>, f: F) -> Result<Ref<'b, U>, Self>
1704    where
1705        F: FnOnce(&T) -> Option<&U>,
1706    {
1707        match f(&*orig) {
1708            Some(value) => Ok(Ref { value: NonNull::from(value), borrow: orig.borrow }),
1709            None => Err(orig),
1710        }
1711    }
1712
1713    /// Tries to makes a new `Ref` for a component of the borrowed data.
1714    /// On failure, the original guard is returned alongside with the error
1715    /// returned by the closure.
1716    ///
1717    /// The `RefCell` is already immutably borrowed, so this cannot fail.
1718    ///
1719    /// This is an associated function that needs to be used as
1720    /// `Ref::try_map(...)`. A method would interfere with methods of the same
1721    /// name on the contents of a `RefCell` used through `Deref`.
1722    ///
1723    /// # Examples
1724    ///
1725    /// ```
1726    /// #![feature(refcell_try_map)]
1727    /// use std::cell::{RefCell, Ref};
1728    /// use std::str::{from_utf8, Utf8Error};
1729    ///
1730    /// let c = RefCell::new(vec![0xF0, 0x9F, 0xA6 ,0x80]);
1731    /// let b1: Ref<'_, Vec<u8>> = c.borrow();
1732    /// let b2: Result<Ref<'_, str>, _> = Ref::try_map(b1, |v| from_utf8(v));
1733    /// assert_eq!(&*b2.unwrap(), "🦀");
1734    ///
1735    /// let c = RefCell::new(vec![0xF0, 0x9F, 0xA6]);
1736    /// let b1: Ref<'_, Vec<u8>> = c.borrow();
1737    /// let b2: Result<_, (Ref<'_, Vec<u8>>, Utf8Error)> = Ref::try_map(b1, |v| from_utf8(v));
1738    /// let (b3, e) = b2.unwrap_err();
1739    /// assert_eq!(*b3, vec![0xF0, 0x9F, 0xA6]);
1740    /// assert_eq!(e.valid_up_to(), 0);
1741    /// ```
1742    #[unstable(feature = "refcell_try_map", issue = "143801")]
1743    #[inline]
1744    pub fn try_map<U: ?Sized, E>(
1745        orig: Ref<'b, T>,
1746        f: impl FnOnce(&T) -> Result<&U, E>,
1747    ) -> Result<Ref<'b, U>, (Self, E)> {
1748        match f(&*orig) {
1749            Ok(value) => Ok(Ref { value: NonNull::from(value), borrow: orig.borrow }),
1750            Err(e) => Err((orig, e)),
1751        }
1752    }
1753
1754    /// Splits a `Ref` into multiple `Ref`s for different components of the
1755    /// borrowed data.
1756    ///
1757    /// The `RefCell` is already immutably borrowed, so this cannot fail.
1758    ///
1759    /// This is an associated function that needs to be used as
1760    /// `Ref::map_split(...)`. A method would interfere with methods of the same
1761    /// name on the contents of a `RefCell` used through `Deref`.
1762    ///
1763    /// # Examples
1764    ///
1765    /// ```
1766    /// use std::cell::{Ref, RefCell};
1767    ///
1768    /// let cell = RefCell::new([1, 2, 3, 4]);
1769    /// let borrow = cell.borrow();
1770    /// let (begin, end) = Ref::map_split(borrow, |slice| slice.split_at(2));
1771    /// assert_eq!(*begin, [1, 2]);
1772    /// assert_eq!(*end, [3, 4]);
1773    /// ```
1774    #[stable(feature = "refcell_map_split", since = "1.35.0")]
1775    #[inline]
1776    pub fn map_split<U: ?Sized, V: ?Sized, F>(orig: Ref<'b, T>, f: F) -> (Ref<'b, U>, Ref<'b, V>)
1777    where
1778        F: FnOnce(&T) -> (&U, &V),
1779    {
1780        let (a, b) = f(&*orig);
1781        let borrow = orig.borrow.clone();
1782        (
1783            Ref { value: NonNull::from(a), borrow },
1784            Ref { value: NonNull::from(b), borrow: orig.borrow },
1785        )
1786    }
1787
1788    /// Converts into a reference to the underlying data.
1789    ///
1790    /// The underlying `RefCell` can never be mutably borrowed from again and will always appear
1791    /// already immutably borrowed. It is not a good idea to leak more than a constant number of
1792    /// references. The `RefCell` can be immutably borrowed again if only a smaller number of leaks
1793    /// have occurred in total.
1794    ///
1795    /// This is an associated function that needs to be used as
1796    /// `Ref::leak(...)`. A method would interfere with methods of the
1797    /// same name on the contents of a `RefCell` used through `Deref`.
1798    ///
1799    /// # Examples
1800    ///
1801    /// ```
1802    /// #![feature(cell_leak)]
1803    /// use std::cell::{RefCell, Ref};
1804    /// let cell = RefCell::new(0);
1805    ///
1806    /// let value = Ref::leak(cell.borrow());
1807    /// assert_eq!(*value, 0);
1808    ///
1809    /// assert!(cell.try_borrow().is_ok());
1810    /// assert!(cell.try_borrow_mut().is_err());
1811    /// ```
1812    #[unstable(feature = "cell_leak", issue = "69099")]
1813    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
1814    pub const fn leak(orig: Ref<'b, T>) -> &'b T {
1815        // By forgetting this Ref we ensure that the borrow counter in the RefCell can't go back to
1816        // UNUSED within the lifetime `'b`. Resetting the reference tracking state would require a
1817        // unique reference to the borrowed RefCell. No further mutable references can be created
1818        // from the original cell.
1819        mem::forget(orig.borrow);
1820        // SAFETY: after forgetting, we can form a reference for the rest of lifetime `'b`.
1821        unsafe { orig.value.as_ref() }
1822    }
1823}
1824
1825#[unstable(feature = "coerce_unsized", issue = "18598")]
1826impl<'b, T: ?Sized + Unsize<U>, U: ?Sized> CoerceUnsized<Ref<'b, U>> for Ref<'b, T> {}
1827
1828#[stable(feature = "std_guard_impls", since = "1.20.0")]
1829impl<T: ?Sized + fmt::Display> fmt::Display for Ref<'_, T> {
1830    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1831        (**self).fmt(f)
1832    }
1833}
1834
1835impl<'b, T: ?Sized> RefMut<'b, T> {
1836    /// Makes a new `RefMut` for a component of the borrowed data, e.g., an enum
1837    /// variant.
1838    ///
1839    /// The `RefCell` is already mutably borrowed, so this cannot fail.
1840    ///
1841    /// This is an associated function that needs to be used as
1842    /// `RefMut::map(...)`. A method would interfere with methods of the same
1843    /// name on the contents of a `RefCell` used through `Deref`.
1844    ///
1845    /// # Examples
1846    ///
1847    /// ```
1848    /// use std::cell::{RefCell, RefMut};
1849    ///
1850    /// let c = RefCell::new((5, 'b'));
1851    /// {
1852    ///     let b1: RefMut<'_, (u32, char)> = c.borrow_mut();
1853    ///     let mut b2: RefMut<'_, u32> = RefMut::map(b1, |t| &mut t.0);
1854    ///     assert_eq!(*b2, 5);
1855    ///     *b2 = 42;
1856    /// }
1857    /// assert_eq!(*c.borrow(), (42, 'b'));
1858    /// ```
1859    #[stable(feature = "cell_map", since = "1.8.0")]
1860    #[inline]
1861    pub fn map<U: ?Sized, F>(mut orig: RefMut<'b, T>, f: F) -> RefMut<'b, U>
1862    where
1863        F: FnOnce(&mut T) -> &mut U,
1864    {
1865        let value = NonNull::from(f(&mut *orig));
1866        RefMut { value, borrow: orig.borrow, marker: PhantomData }
1867    }
1868
1869    /// Makes a new `RefMut` for an optional component of the borrowed data. The
1870    /// original guard is returned as an `Err(..)` if the closure returns
1871    /// `None`.
1872    ///
1873    /// The `RefCell` is already mutably borrowed, so this cannot fail.
1874    ///
1875    /// This is an associated function that needs to be used as
1876    /// `RefMut::filter_map(...)`. A method would interfere with methods of the
1877    /// same name on the contents of a `RefCell` used through `Deref`.
1878    ///
1879    /// # Examples
1880    ///
1881    /// ```
1882    /// use std::cell::{RefCell, RefMut};
1883    ///
1884    /// let c = RefCell::new(vec![1, 2, 3]);
1885    ///
1886    /// {
1887    ///     let b1: RefMut<'_, Vec<u32>> = c.borrow_mut();
1888    ///     let mut b2: Result<RefMut<'_, u32>, _> = RefMut::filter_map(b1, |v| v.get_mut(1));
1889    ///
1890    ///     if let Ok(mut b2) = b2 {
1891    ///         *b2 += 2;
1892    ///     }
1893    /// }
1894    ///
1895    /// assert_eq!(*c.borrow(), vec![1, 4, 3]);
1896    /// ```
1897    #[stable(feature = "cell_filter_map", since = "1.63.0")]
1898    #[inline]
1899    pub fn filter_map<U: ?Sized, F>(mut orig: RefMut<'b, T>, f: F) -> Result<RefMut<'b, U>, Self>
1900    where
1901        F: FnOnce(&mut T) -> Option<&mut U>,
1902    {
1903        // SAFETY: function holds onto an exclusive reference for the duration
1904        // of its call through `orig`, and the pointer is only de-referenced
1905        // inside of the function call never allowing the exclusive reference to
1906        // escape.
1907        match f(&mut *orig) {
1908            Some(value) => {
1909                Ok(RefMut { value: NonNull::from(value), borrow: orig.borrow, marker: PhantomData })
1910            }
1911            None => Err(orig),
1912        }
1913    }
1914
1915    /// Tries to makes a new `RefMut` for a component of the borrowed data.
1916    /// On failure, the original guard is returned alongside with the error
1917    /// returned by the closure.
1918    ///
1919    /// The `RefCell` is already mutably borrowed, so this cannot fail.
1920    ///
1921    /// This is an associated function that needs to be used as
1922    /// `RefMut::try_map(...)`. A method would interfere with methods of the same
1923    /// name on the contents of a `RefCell` used through `Deref`.
1924    ///
1925    /// # Examples
1926    ///
1927    /// ```
1928    /// #![feature(refcell_try_map)]
1929    /// use std::cell::{RefCell, RefMut};
1930    /// use std::str::{from_utf8_mut, Utf8Error};
1931    ///
1932    /// let c = RefCell::new(vec![0x68, 0x65, 0x6C, 0x6C, 0x6F]);
1933    /// {
1934    ///     let b1: RefMut<'_, Vec<u8>> = c.borrow_mut();
1935    ///     let b2: Result<RefMut<'_, str>, _> = RefMut::try_map(b1, |v| from_utf8_mut(v));
1936    ///     let mut b2 = b2.unwrap();
1937    ///     assert_eq!(&*b2, "hello");
1938    ///     b2.make_ascii_uppercase();
1939    /// }
1940    /// assert_eq!(*c.borrow(), "HELLO".as_bytes());
1941    ///
1942    /// let c = RefCell::new(vec![0xFF]);
1943    /// let b1: RefMut<'_, Vec<u8>> = c.borrow_mut();
1944    /// let b2: Result<_, (RefMut<'_, Vec<u8>>, Utf8Error)> = RefMut::try_map(b1, |v| from_utf8_mut(v));
1945    /// let (b3, e) = b2.unwrap_err();
1946    /// assert_eq!(*b3, vec![0xFF]);
1947    /// assert_eq!(e.valid_up_to(), 0);
1948    /// ```
1949    #[unstable(feature = "refcell_try_map", issue = "143801")]
1950    #[inline]
1951    pub fn try_map<U: ?Sized, E>(
1952        mut orig: RefMut<'b, T>,
1953        f: impl FnOnce(&mut T) -> Result<&mut U, E>,
1954    ) -> Result<RefMut<'b, U>, (Self, E)> {
1955        // SAFETY: function holds onto an exclusive reference for the duration
1956        // of its call through `orig`, and the pointer is only de-referenced
1957        // inside of the function call never allowing the exclusive reference to
1958        // escape.
1959        match f(&mut *orig) {
1960            Ok(value) => {
1961                Ok(RefMut { value: NonNull::from(value), borrow: orig.borrow, marker: PhantomData })
1962            }
1963            Err(e) => Err((orig, e)),
1964        }
1965    }
1966
1967    /// Splits a `RefMut` into multiple `RefMut`s for different components of the
1968    /// borrowed data.
1969    ///
1970    /// The underlying `RefCell` will remain mutably borrowed until both
1971    /// returned `RefMut`s go out of scope.
1972    ///
1973    /// The `RefCell` is already mutably borrowed, so this cannot fail.
1974    ///
1975    /// This is an associated function that needs to be used as
1976    /// `RefMut::map_split(...)`. A method would interfere with methods of the
1977    /// same name on the contents of a `RefCell` used through `Deref`.
1978    ///
1979    /// # Examples
1980    ///
1981    /// ```
1982    /// use std::cell::{RefCell, RefMut};
1983    ///
1984    /// let cell = RefCell::new([1, 2, 3, 4]);
1985    /// let borrow = cell.borrow_mut();
1986    /// let (mut begin, mut end) = RefMut::map_split(borrow, |slice| slice.split_at_mut(2));
1987    /// assert_eq!(*begin, [1, 2]);
1988    /// assert_eq!(*end, [3, 4]);
1989    /// begin.copy_from_slice(&[4, 3]);
1990    /// end.copy_from_slice(&[2, 1]);
1991    /// ```
1992    #[stable(feature = "refcell_map_split", since = "1.35.0")]
1993    #[inline]
1994    pub fn map_split<U: ?Sized, V: ?Sized, F>(
1995        mut orig: RefMut<'b, T>,
1996        f: F,
1997    ) -> (RefMut<'b, U>, RefMut<'b, V>)
1998    where
1999        F: FnOnce(&mut T) -> (&mut U, &mut V),
2000    {
2001        let borrow = orig.borrow.clone();
2002        let (a, b) = f(&mut *orig);
2003        (
2004            RefMut { value: NonNull::from(a), borrow, marker: PhantomData },
2005            RefMut { value: NonNull::from(b), borrow: orig.borrow, marker: PhantomData },
2006        )
2007    }
2008
2009    /// Converts into a mutable reference to the underlying data.
2010    ///
2011    /// The underlying `RefCell` can not be borrowed from again and will always appear already
2012    /// mutably borrowed, making the returned reference the only to the interior.
2013    ///
2014    /// This is an associated function that needs to be used as
2015    /// `RefMut::leak(...)`. A method would interfere with methods of the
2016    /// same name on the contents of a `RefCell` used through `Deref`.
2017    ///
2018    /// # Examples
2019    ///
2020    /// ```
2021    /// #![feature(cell_leak)]
2022    /// use std::cell::{RefCell, RefMut};
2023    /// let cell = RefCell::new(0);
2024    ///
2025    /// let value = RefMut::leak(cell.borrow_mut());
2026    /// assert_eq!(*value, 0);
2027    /// *value = 1;
2028    ///
2029    /// assert!(cell.try_borrow_mut().is_err());
2030    /// ```
2031    #[unstable(feature = "cell_leak", issue = "69099")]
2032    #[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
2033    pub const fn leak(mut orig: RefMut<'b, T>) -> &'b mut T {
2034        // By forgetting this BorrowRefMut we ensure that the borrow counter in the RefCell can't
2035        // go back to UNUSED within the lifetime `'b`. Resetting the reference tracking state would
2036        // require a unique reference to the borrowed RefCell. No further references can be created
2037        // from the original cell within that lifetime, making the current borrow the only
2038        // reference for the remaining lifetime.
2039        mem::forget(orig.borrow);
2040        // SAFETY: after forgetting, we can form a reference for the rest of lifetime `'b`.
2041        unsafe { orig.value.as_mut() }
2042    }
2043}
2044
2045struct BorrowRefMut<'b> {
2046    borrow: &'b Cell<BorrowCounter>,
2047}
2048
2049#[rustc_const_unstable(feature = "const_ref_cell", issue = "137844")]
2050impl const Drop for BorrowRefMut<'_> {
2051    #[inline]
2052    fn drop(&mut self) {
2053        let borrow = self.borrow.get();
2054        debug_assert!(is_writing(borrow));
2055        self.borrow.replace(borrow + 1);
2056    }
2057}
2058
2059impl<'b> BorrowRefMut<'b> {
2060    #[inline]
2061    const fn new(borrow: &'b Cell<BorrowCounter>) -> Option<BorrowRefMut<'b>> {
2062        // NOTE: Unlike BorrowRefMut::clone, new is called to create the initial
2063        // mutable reference, and so there must currently be no existing
2064        // references. Thus, while clone increments the mutable refcount, here
2065        // we explicitly only allow going from UNUSED to UNUSED - 1.
2066        match borrow.get() {
2067            UNUSED => {
2068                borrow.replace(UNUSED - 1);
2069                Some(BorrowRefMut { borrow })
2070            }
2071            _ => None,
2072        }
2073    }
2074
2075    // Clones a `BorrowRefMut`.
2076    //
2077    // This is only valid if each `BorrowRefMut` is used to track a mutable
2078    // reference to a distinct, nonoverlapping range of the original object.
2079    // This isn't in a Clone impl so that code doesn't call this implicitly.
2080    #[inline]
2081    fn clone(&self) -> BorrowRefMut<'b> {
2082        let borrow = self.borrow.get();
2083        debug_assert!(is_writing(borrow));
2084        // Prevent the borrow counter from underflowing.
2085        assert!(borrow != BorrowCounter::MIN);
2086        self.borrow.set(borrow - 1);
2087        BorrowRefMut { borrow: self.borrow }
2088    }
2089}
2090
2091/// A wrapper type for a mutably borrowed value from a `RefCell<T>`.
2092///
2093/// See the [module-level documentation](self) for more.
2094#[stable(feature = "rust1", since = "1.0.0")]
2095#[must_not_suspend = "holding a RefMut across suspend points can cause BorrowErrors"]
2096#[rustc_diagnostic_item = "RefCellRefMut"]
2097pub struct RefMut<'b, T: ?Sized + 'b> {
2098    // NB: we use a pointer instead of `&'b mut T` to avoid `noalias` violations, because a
2099    // `RefMut` argument doesn't hold exclusivity for its whole scope, only until it drops.
2100    value: NonNull<T>,
2101    borrow: BorrowRefMut<'b>,
2102    // `NonNull` is covariant over `T`, so we need to reintroduce invariance.
2103    marker: PhantomData<&'b mut T>,
2104}
2105
2106#[stable(feature = "rust1", since = "1.0.0")]
2107#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2108impl<T: ?Sized> const Deref for RefMut<'_, T> {
2109    type Target = T;
2110
2111    #[inline]
2112    fn deref(&self) -> &T {
2113        // SAFETY: the value is accessible as long as we hold our borrow.
2114        unsafe { self.value.as_ref() }
2115    }
2116}
2117
2118#[stable(feature = "rust1", since = "1.0.0")]
2119#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2120impl<T: ?Sized> const DerefMut for RefMut<'_, T> {
2121    #[inline]
2122    fn deref_mut(&mut self) -> &mut T {
2123        // SAFETY: the value is accessible as long as we hold our borrow.
2124        unsafe { self.value.as_mut() }
2125    }
2126}
2127
2128#[unstable(feature = "deref_pure_trait", issue = "87121")]
2129unsafe impl<T: ?Sized> DerefPure for RefMut<'_, T> {}
2130
2131#[unstable(feature = "coerce_unsized", issue = "18598")]
2132impl<'b, T: ?Sized + Unsize<U>, U: ?Sized> CoerceUnsized<RefMut<'b, U>> for RefMut<'b, T> {}
2133
2134#[stable(feature = "std_guard_impls", since = "1.20.0")]
2135impl<T: ?Sized + fmt::Display> fmt::Display for RefMut<'_, T> {
2136    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2137        (**self).fmt(f)
2138    }
2139}
2140
2141/// The core primitive for interior mutability in Rust.
2142///
2143/// If you have a reference `&T`, then normally in Rust the compiler performs optimizations based on
2144/// the knowledge that `&T` points to immutable data. Mutating that data, for example through an
2145/// alias or by transmuting a `&T` into a `&mut T`, is considered undefined behavior.
2146/// `UnsafeCell<T>` opts-out of the immutability guarantee for `&T`: a shared reference
2147/// `&UnsafeCell<T>` may point to data that is being mutated. This is called "interior mutability".
2148///
2149/// All other types that allow internal mutability, such as [`Cell<T>`] and [`RefCell<T>`], internally
2150/// use `UnsafeCell` to wrap their data.
2151///
2152/// Note that only the immutability guarantee for shared references is affected by `UnsafeCell`. The
2153/// uniqueness guarantee for mutable references is unaffected. There is *no* legal way to obtain
2154/// aliasing `&mut`, not even with `UnsafeCell<T>`.
2155///
2156/// `UnsafeCell` does nothing to avoid data races; they are still undefined behavior. If multiple
2157/// threads have access to the same `UnsafeCell`, they must follow the usual rules of the
2158/// [concurrent memory model]: conflicting non-synchronized accesses must be done via the APIs in
2159/// [`core::sync::atomic`].
2160///
2161/// The `UnsafeCell` API itself is technically very simple: [`.get()`] gives you a raw pointer
2162/// `*mut T` to its contents. It is up to _you_ as the abstraction designer to use that raw pointer
2163/// correctly.
2164///
2165/// [`.get()`]: `UnsafeCell::get`
2166/// [concurrent memory model]: ../sync/atomic/index.html#memory-model-for-atomic-accesses
2167///
2168/// # Aliasing rules
2169///
2170/// The precise Rust aliasing rules are somewhat in flux, but the main points are not contentious:
2171///
2172/// - If you create a safe reference with lifetime `'a` (either a `&T` or `&mut T` reference), then
2173///   you must not access the data in any way that contradicts that reference for the remainder of
2174///   `'a`. For example, this means that if you take the `*mut T` from an `UnsafeCell<T>` and cast it
2175///   to an `&T`, then the data in `T` must remain immutable (modulo any `UnsafeCell` data found
2176///   within `T`, of course) until that reference's lifetime expires. Similarly, if you create a
2177///   `&mut T` reference that is released to safe code, then you must not access the data within the
2178///   `UnsafeCell` until that reference expires.
2179///
2180/// - For both `&T` without `UnsafeCell<_>` and `&mut T`, you must also not deallocate the data
2181///   until the reference expires. As a special exception, given an `&T`, any part of it that is
2182///   inside an `UnsafeCell<_>` may be deallocated during the lifetime of the reference, after the
2183///   last time the reference is used (dereferenced or reborrowed). Since you cannot deallocate a part
2184///   of what a reference points to, this means the memory an `&T` points to can be deallocated only if
2185///   *every part of it* (including padding) is inside an `UnsafeCell`.
2186///
2187/// However, whenever a `&UnsafeCell<T>` is constructed or dereferenced, it must still point to
2188/// live memory and the compiler is allowed to insert spurious reads if it can prove that this
2189/// memory has not yet been deallocated.
2190///
2191/// To assist with proper design, the following scenarios are explicitly declared legal
2192/// for single-threaded code:
2193///
2194/// 1. A `&T` reference can be released to safe code and there it can co-exist with other `&T`
2195///    references, but not with a `&mut T`
2196///
2197/// 2. A `&mut T` reference may be released to safe code provided neither other `&mut T` nor `&T`
2198///    co-exist with it. A `&mut T` must always be unique.
2199///
2200/// Note that whilst mutating the contents of an `&UnsafeCell<T>` (even while other
2201/// `&UnsafeCell<T>` references alias the cell) is
2202/// ok (provided you enforce the above invariants some other way), it is still undefined behavior
2203/// to have multiple `&mut UnsafeCell<T>` aliases. That is, `UnsafeCell` is a wrapper
2204/// designed to have a special interaction with _shared_ accesses (_i.e._, through an
2205/// `&UnsafeCell<_>` reference); there is no magic whatsoever when dealing with _exclusive_
2206/// accesses (_e.g._, through a `&mut UnsafeCell<_>`): neither the cell nor the wrapped value
2207/// may be aliased for the duration of that `&mut` borrow.
2208/// This is showcased by the [`.get_mut()`] accessor, which is a _safe_ getter that yields
2209/// a `&mut T`.
2210///
2211/// [`.get_mut()`]: `UnsafeCell::get_mut`
2212///
2213/// # Memory layout
2214///
2215/// `UnsafeCell<T>` has the same in-memory representation as its inner type `T`. A consequence
2216/// of this guarantee is that it is possible to convert between `T` and `UnsafeCell<T>`.
2217/// Special care has to be taken when converting a nested `T` inside of an `Outer<T>` type
2218/// to an `Outer<UnsafeCell<T>>` type: this is not sound when the `Outer<T>` type enables [niche]
2219/// optimizations. For example, the type `Option<NonNull<u8>>` is typically 8 bytes large on
2220/// 64-bit platforms, but the type `Option<UnsafeCell<NonNull<u8>>>` takes up 16 bytes of space.
2221/// Therefore this is not a valid conversion, despite `NonNull<u8>` and `UnsafeCell<NonNull<u8>>>`
2222/// having the same memory layout. This is because `UnsafeCell` disables niche optimizations in
2223/// order to avoid its interior mutability property from spreading from `T` into the `Outer` type,
2224/// thus this can cause distortions in the type size in these cases.
2225///
2226/// Note that the only valid way to obtain a `*mut T` pointer to the contents of a
2227/// _shared_ `UnsafeCell<T>` is through [`.get()`]  or [`.raw_get()`]. A `&mut T` reference
2228/// can be obtained by either dereferencing this pointer or by calling [`.get_mut()`]
2229/// on an _exclusive_ `UnsafeCell<T>`. Even though `T` and `UnsafeCell<T>` have the
2230/// same memory layout, the following is not allowed and undefined behavior:
2231///
2232/// ```rust,compile_fail
2233/// # use std::cell::UnsafeCell;
2234/// unsafe fn not_allowed<T>(ptr: &UnsafeCell<T>) -> &mut T {
2235///   let t = ptr as *const UnsafeCell<T> as *mut T;
2236///   // This is undefined behavior, because the `*mut T` pointer
2237///   // was not obtained through `.get()` nor `.raw_get()`:
2238///   unsafe { &mut *t }
2239/// }
2240/// ```
2241///
2242/// Instead, do this:
2243///
2244/// ```rust
2245/// # use std::cell::UnsafeCell;
2246/// // Safety: the caller must ensure that there are no references that
2247/// // point to the *contents* of the `UnsafeCell`.
2248/// unsafe fn get_mut<T>(ptr: &UnsafeCell<T>) -> &mut T {
2249///   unsafe { &mut *ptr.get() }
2250/// }
2251/// ```
2252///
2253/// Converting in the other direction from a `&mut T`
2254/// to an `&UnsafeCell<T>` is allowed:
2255///
2256/// ```rust
2257/// # use std::cell::UnsafeCell;
2258/// fn get_shared<T>(ptr: &mut T) -> &UnsafeCell<T> {
2259///   let t = ptr as *mut T as *const UnsafeCell<T>;
2260///   // SAFETY: `T` and `UnsafeCell<T>` have the same memory layout
2261///   unsafe { &*t }
2262/// }
2263/// ```
2264///
2265/// [niche]: https://rust-lang.github.io/unsafe-code-guidelines/glossary.html#niche
2266/// [`.raw_get()`]: `UnsafeCell::raw_get`
2267///
2268/// # Examples
2269///
2270/// Here is an example showcasing how to soundly mutate the contents of an `UnsafeCell<_>` despite
2271/// there being multiple references aliasing the cell:
2272///
2273/// ```
2274/// use std::cell::UnsafeCell;
2275///
2276/// let x: UnsafeCell<i32> = 42.into();
2277/// // Get multiple / concurrent / shared references to the same `x`.
2278/// let (p1, p2): (&UnsafeCell<i32>, &UnsafeCell<i32>) = (&x, &x);
2279///
2280/// unsafe {
2281///     // SAFETY: within this scope there are no other references to `x`'s contents,
2282///     // so ours is effectively unique.
2283///     let p1_exclusive: &mut i32 = &mut *p1.get(); // -- borrow --+
2284///     *p1_exclusive += 27; //                                     |
2285/// } // <---------- cannot go beyond this point -------------------+
2286///
2287/// unsafe {
2288///     // SAFETY: within this scope nobody expects to have exclusive access to `x`'s contents,
2289///     // so we can have multiple shared accesses concurrently.
2290///     let p2_shared: &i32 = &*p2.get();
2291///     assert_eq!(*p2_shared, 42 + 27);
2292///     let p1_shared: &i32 = &*p1.get();
2293///     assert_eq!(*p1_shared, *p2_shared);
2294/// }
2295/// ```
2296///
2297/// The following example showcases the fact that exclusive access to an `UnsafeCell<T>`
2298/// implies exclusive access to its `T`:
2299///
2300/// ```rust
2301/// #![forbid(unsafe_code)]
2302/// // with exclusive accesses, `UnsafeCell` is a transparent no-op wrapper, so no need for
2303/// // `unsafe` here.
2304/// use std::cell::UnsafeCell;
2305///
2306/// let mut x: UnsafeCell<i32> = 42.into();
2307///
2308/// // Get a compile-time-checked unique reference to `x`.
2309/// let p_unique: &mut UnsafeCell<i32> = &mut x;
2310/// // With an exclusive reference, we can mutate the contents for free.
2311/// *p_unique.get_mut() = 0;
2312/// // Or, equivalently:
2313/// x = UnsafeCell::new(0);
2314///
2315/// // When we own the value, we can extract the contents for free.
2316/// let contents: i32 = x.into_inner();
2317/// assert_eq!(contents, 0);
2318/// ```
2319#[lang = "unsafe_cell"]
2320#[stable(feature = "rust1", since = "1.0.0")]
2321#[repr(transparent)]
2322#[rustc_pub_transparent]
2323pub struct UnsafeCell<T: ?Sized> {
2324    value: T,
2325}
2326
2327#[stable(feature = "rust1", since = "1.0.0")]
2328impl<T: ?Sized> !Sync for UnsafeCell<T> {}
2329
2330impl<T> UnsafeCell<T> {
2331    /// Constructs a new instance of `UnsafeCell` which will wrap the specified
2332    /// value.
2333    ///
2334    /// All access to the inner value through `&UnsafeCell<T>` requires `unsafe` code.
2335    ///
2336    /// # Examples
2337    ///
2338    /// ```
2339    /// use std::cell::UnsafeCell;
2340    ///
2341    /// let uc = UnsafeCell::new(5);
2342    /// ```
2343    #[stable(feature = "rust1", since = "1.0.0")]
2344    #[rustc_const_stable(feature = "const_unsafe_cell_new", since = "1.32.0")]
2345    #[inline(always)]
2346    pub const fn new(value: T) -> UnsafeCell<T> {
2347        UnsafeCell { value }
2348    }
2349
2350    /// Unwraps the value, consuming the cell.
2351    ///
2352    /// # Examples
2353    ///
2354    /// ```
2355    /// use std::cell::UnsafeCell;
2356    ///
2357    /// let uc = UnsafeCell::new(5);
2358    ///
2359    /// let five = uc.into_inner();
2360    /// ```
2361    #[inline(always)]
2362    #[stable(feature = "rust1", since = "1.0.0")]
2363    #[rustc_const_stable(feature = "const_cell_into_inner", since = "1.83.0")]
2364    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
2365    pub const fn into_inner(self) -> T {
2366        self.value
2367    }
2368
2369    /// Replace the value in this `UnsafeCell` and return the old value.
2370    ///
2371    /// # Safety
2372    ///
2373    /// The caller must take care to avoid aliasing and data races.
2374    ///
2375    /// - It is Undefined Behavior to allow calls to race with
2376    ///   any other access to the wrapped value.
2377    /// - It is Undefined Behavior to call this while any other
2378    ///   reference(s) to the wrapped value are alive.
2379    ///
2380    /// # Examples
2381    ///
2382    /// ```
2383    /// #![feature(unsafe_cell_access)]
2384    /// use std::cell::UnsafeCell;
2385    ///
2386    /// let uc = UnsafeCell::new(5);
2387    ///
2388    /// let old = unsafe { uc.replace(10) };
2389    /// assert_eq!(old, 5);
2390    /// ```
2391    #[inline]
2392    #[unstable(feature = "unsafe_cell_access", issue = "136327")]
2393    #[rustc_should_not_be_called_on_const_items]
2394    pub const unsafe fn replace(&self, value: T) -> T {
2395        // SAFETY: pointer comes from `&self` so naturally satisfies invariants.
2396        unsafe { ptr::replace(self.get(), value) }
2397    }
2398}
2399
2400impl<T: ?Sized> UnsafeCell<T> {
2401    /// Converts from `&mut T` to `&mut UnsafeCell<T>`.
2402    ///
2403    /// # Examples
2404    ///
2405    /// ```
2406    /// use std::cell::UnsafeCell;
2407    ///
2408    /// let mut val = 42;
2409    /// let uc = UnsafeCell::from_mut(&mut val);
2410    ///
2411    /// *uc.get_mut() -= 1;
2412    /// assert_eq!(*uc.get_mut(), 41);
2413    /// ```
2414    #[inline(always)]
2415    #[stable(feature = "unsafe_cell_from_mut", since = "1.84.0")]
2416    #[rustc_const_stable(feature = "unsafe_cell_from_mut", since = "1.84.0")]
2417    pub const fn from_mut(value: &mut T) -> &mut UnsafeCell<T> {
2418        // SAFETY: `UnsafeCell<T>` has the same memory layout as `T` due to #[repr(transparent)].
2419        unsafe { &mut *(value as *mut T as *mut UnsafeCell<T>) }
2420    }
2421
2422    /// Gets a mutable pointer to the wrapped value.
2423    ///
2424    /// This can be cast to a pointer of any kind. When creating references, you must uphold the
2425    /// aliasing rules; see [the type-level docs][UnsafeCell#aliasing-rules] for more discussion and
2426    /// caveats.
2427    ///
2428    /// # Examples
2429    ///
2430    /// ```
2431    /// use std::cell::UnsafeCell;
2432    ///
2433    /// let uc = UnsafeCell::new(5);
2434    ///
2435    /// let five = uc.get();
2436    /// ```
2437    #[inline(always)]
2438    #[stable(feature = "rust1", since = "1.0.0")]
2439    #[rustc_const_stable(feature = "const_unsafecell_get", since = "1.32.0")]
2440    #[rustc_as_ptr]
2441    #[rustc_never_returns_null_ptr]
2442    #[rustc_should_not_be_called_on_const_items]
2443    pub const fn get(&self) -> *mut T {
2444        // We can just cast the pointer from `UnsafeCell<T>` to `T` because of
2445        // #[repr(transparent)]. This exploits std's special status, there is
2446        // no guarantee for user code that this will work in future versions of the compiler!
2447        self as *const UnsafeCell<T> as *const T as *mut T
2448    }
2449
2450    /// Returns a mutable reference to the underlying data.
2451    ///
2452    /// This call borrows the `UnsafeCell` mutably (at compile-time) which
2453    /// guarantees that we possess the only reference.
2454    ///
2455    /// # Examples
2456    ///
2457    /// ```
2458    /// use std::cell::UnsafeCell;
2459    ///
2460    /// let mut c = UnsafeCell::new(5);
2461    /// *c.get_mut() += 1;
2462    ///
2463    /// assert_eq!(*c.get_mut(), 6);
2464    /// ```
2465    #[inline(always)]
2466    #[stable(feature = "unsafe_cell_get_mut", since = "1.50.0")]
2467    #[rustc_const_stable(feature = "const_unsafecell_get_mut", since = "1.83.0")]
2468    pub const fn get_mut(&mut self) -> &mut T {
2469        &mut self.value
2470    }
2471
2472    /// Gets a mutable pointer to the wrapped value.
2473    /// The difference from [`get`] is that this function accepts a raw pointer,
2474    /// which is useful to avoid the creation of temporary references.
2475    ///
2476    /// This can be cast to a pointer of any kind. When creating references, you must uphold the
2477    /// aliasing rules; see [the type-level docs][UnsafeCell#aliasing-rules] for more discussion and
2478    /// caveats.
2479    ///
2480    /// [`get`]: UnsafeCell::get()
2481    ///
2482    /// # Examples
2483    ///
2484    /// Gradual initialization of an `UnsafeCell` requires `raw_get`, as
2485    /// calling `get` would require creating a reference to uninitialized data:
2486    ///
2487    /// ```
2488    /// use std::cell::UnsafeCell;
2489    /// use std::mem::MaybeUninit;
2490    ///
2491    /// let m = MaybeUninit::<UnsafeCell<i32>>::uninit();
2492    /// unsafe { UnsafeCell::raw_get(m.as_ptr()).write(5); }
2493    /// // avoid below which references to uninitialized data
2494    /// // unsafe { UnsafeCell::get(&*m.as_ptr()).write(5); }
2495    /// let uc = unsafe { m.assume_init() };
2496    ///
2497    /// assert_eq!(uc.into_inner(), 5);
2498    /// ```
2499    #[inline(always)]
2500    #[stable(feature = "unsafe_cell_raw_get", since = "1.56.0")]
2501    #[rustc_const_stable(feature = "unsafe_cell_raw_get", since = "1.56.0")]
2502    #[rustc_diagnostic_item = "unsafe_cell_raw_get"]
2503    pub const fn raw_get(this: *const Self) -> *mut T {
2504        // We can just cast the pointer from `UnsafeCell<T>` to `T` because of
2505        // #[repr(transparent)]. This exploits std's special status, there is
2506        // no guarantee for user code that this will work in future versions of the compiler!
2507        this as *const T as *mut T
2508    }
2509
2510    /// Get a shared reference to the value within the `UnsafeCell`.
2511    ///
2512    /// # Safety
2513    ///
2514    /// - It is Undefined Behavior to call this while any mutable
2515    ///   reference to the wrapped value is alive.
2516    /// - Mutating the wrapped value while the returned
2517    ///   reference is alive is Undefined Behavior.
2518    ///
2519    /// # Examples
2520    ///
2521    /// ```
2522    /// #![feature(unsafe_cell_access)]
2523    /// use std::cell::UnsafeCell;
2524    ///
2525    /// let uc = UnsafeCell::new(5);
2526    ///
2527    /// let val = unsafe { uc.as_ref_unchecked() };
2528    /// assert_eq!(val, &5);
2529    /// ```
2530    #[inline]
2531    #[unstable(feature = "unsafe_cell_access", issue = "136327")]
2532    #[rustc_should_not_be_called_on_const_items]
2533    pub const unsafe fn as_ref_unchecked(&self) -> &T {
2534        // SAFETY: pointer comes from `&self` so naturally satisfies ptr-to-ref invariants.
2535        unsafe { self.get().as_ref_unchecked() }
2536    }
2537
2538    /// Get an exclusive reference to the value within the `UnsafeCell`.
2539    ///
2540    /// # Safety
2541    ///
2542    /// - It is Undefined Behavior to call this while any other
2543    ///   reference(s) to the wrapped value are alive.
2544    /// - Mutating the wrapped value through other means while the
2545    ///   returned reference is alive is Undefined Behavior.
2546    ///
2547    /// # Examples
2548    ///
2549    /// ```
2550    /// #![feature(unsafe_cell_access)]
2551    /// use std::cell::UnsafeCell;
2552    ///
2553    /// let uc = UnsafeCell::new(5);
2554    ///
2555    /// unsafe { *uc.as_mut_unchecked() += 1; }
2556    /// assert_eq!(uc.into_inner(), 6);
2557    /// ```
2558    #[inline]
2559    #[unstable(feature = "unsafe_cell_access", issue = "136327")]
2560    #[allow(clippy::mut_from_ref)]
2561    #[rustc_should_not_be_called_on_const_items]
2562    pub const unsafe fn as_mut_unchecked(&self) -> &mut T {
2563        // SAFETY: pointer comes from `&self` so naturally satisfies ptr-to-ref invariants.
2564        unsafe { self.get().as_mut_unchecked() }
2565    }
2566}
2567
2568#[stable(feature = "unsafe_cell_default", since = "1.10.0")]
2569#[rustc_const_unstable(feature = "const_default", issue = "143894")]
2570impl<T: [const] Default> const Default for UnsafeCell<T> {
2571    /// Creates an `UnsafeCell`, with the `Default` value for T.
2572    fn default() -> UnsafeCell<T> {
2573        UnsafeCell::new(Default::default())
2574    }
2575}
2576
2577#[stable(feature = "cell_from", since = "1.12.0")]
2578#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2579impl<T> const From<T> for UnsafeCell<T> {
2580    /// Creates a new `UnsafeCell<T>` containing the given value.
2581    fn from(t: T) -> UnsafeCell<T> {
2582        UnsafeCell::new(t)
2583    }
2584}
2585
2586#[unstable(feature = "coerce_unsized", issue = "18598")]
2587impl<T: CoerceUnsized<U>, U> CoerceUnsized<UnsafeCell<U>> for UnsafeCell<T> {}
2588
2589// Allow types that wrap `UnsafeCell` to also implement `DispatchFromDyn`
2590// and become dyn-compatible method receivers.
2591// Note that currently `UnsafeCell` itself cannot be a method receiver
2592// because it does not implement Deref.
2593// In other words:
2594// `self: UnsafeCell<&Self>` won't work
2595// `self: UnsafeCellWrapper<Self>` becomes possible
2596#[unstable(feature = "dispatch_from_dyn", issue = "none")]
2597impl<T: DispatchFromDyn<U>, U> DispatchFromDyn<UnsafeCell<U>> for UnsafeCell<T> {}
2598
2599/// [`UnsafeCell`], but [`Sync`].
2600///
2601/// This is just an `UnsafeCell`, except it implements `Sync`
2602/// if `T` implements `Sync`.
2603///
2604/// `UnsafeCell` doesn't implement `Sync`, to prevent accidental mis-use.
2605/// You can use `SyncUnsafeCell` instead of `UnsafeCell` to allow it to be
2606/// shared between threads, if that's intentional.
2607/// Providing proper synchronization is still the task of the user,
2608/// making this type just as unsafe to use.
2609///
2610/// See [`UnsafeCell`] for details.
2611#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2612#[repr(transparent)]
2613#[rustc_diagnostic_item = "SyncUnsafeCell"]
2614#[rustc_pub_transparent]
2615pub struct SyncUnsafeCell<T: ?Sized> {
2616    value: UnsafeCell<T>,
2617}
2618
2619#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2620unsafe impl<T: ?Sized + Sync> Sync for SyncUnsafeCell<T> {}
2621
2622#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2623impl<T> SyncUnsafeCell<T> {
2624    /// Constructs a new instance of `SyncUnsafeCell` which will wrap the specified value.
2625    #[inline]
2626    pub const fn new(value: T) -> Self {
2627        Self { value: UnsafeCell { value } }
2628    }
2629
2630    /// Unwraps the value, consuming the cell.
2631    #[inline]
2632    #[rustc_const_unstable(feature = "sync_unsafe_cell", issue = "95439")]
2633    pub const fn into_inner(self) -> T {
2634        self.value.into_inner()
2635    }
2636}
2637
2638#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2639impl<T: ?Sized> SyncUnsafeCell<T> {
2640    /// Gets a mutable pointer to the wrapped value.
2641    ///
2642    /// This can be cast to a pointer of any kind.
2643    /// Ensure that the access is unique (no active references, mutable or not)
2644    /// when casting to `&mut T`, and ensure that there are no mutations
2645    /// or mutable aliases going on when casting to `&T`
2646    #[inline]
2647    #[rustc_as_ptr]
2648    #[rustc_never_returns_null_ptr]
2649    #[rustc_should_not_be_called_on_const_items]
2650    pub const fn get(&self) -> *mut T {
2651        self.value.get()
2652    }
2653
2654    /// Returns a mutable reference to the underlying data.
2655    ///
2656    /// This call borrows the `SyncUnsafeCell` mutably (at compile-time) which
2657    /// guarantees that we possess the only reference.
2658    #[inline]
2659    pub const fn get_mut(&mut self) -> &mut T {
2660        self.value.get_mut()
2661    }
2662
2663    /// Gets a mutable pointer to the wrapped value.
2664    ///
2665    /// See [`UnsafeCell::get`] for details.
2666    #[inline]
2667    pub const fn raw_get(this: *const Self) -> *mut T {
2668        // We can just cast the pointer from `SyncUnsafeCell<T>` to `T` because
2669        // of #[repr(transparent)] on both SyncUnsafeCell and UnsafeCell.
2670        // See UnsafeCell::raw_get.
2671        this as *const T as *mut T
2672    }
2673}
2674
2675#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2676#[rustc_const_unstable(feature = "const_default", issue = "143894")]
2677impl<T: [const] Default> const Default for SyncUnsafeCell<T> {
2678    /// Creates an `SyncUnsafeCell`, with the `Default` value for T.
2679    fn default() -> SyncUnsafeCell<T> {
2680        SyncUnsafeCell::new(Default::default())
2681    }
2682}
2683
2684#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2685#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2686impl<T> const From<T> for SyncUnsafeCell<T> {
2687    /// Creates a new `SyncUnsafeCell<T>` containing the given value.
2688    fn from(t: T) -> SyncUnsafeCell<T> {
2689        SyncUnsafeCell::new(t)
2690    }
2691}
2692
2693#[unstable(feature = "coerce_unsized", issue = "18598")]
2694//#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2695impl<T: CoerceUnsized<U>, U> CoerceUnsized<SyncUnsafeCell<U>> for SyncUnsafeCell<T> {}
2696
2697// Allow types that wrap `SyncUnsafeCell` to also implement `DispatchFromDyn`
2698// and become dyn-compatible method receivers.
2699// Note that currently `SyncUnsafeCell` itself cannot be a method receiver
2700// because it does not implement Deref.
2701// In other words:
2702// `self: SyncUnsafeCell<&Self>` won't work
2703// `self: SyncUnsafeCellWrapper<Self>` becomes possible
2704#[unstable(feature = "dispatch_from_dyn", issue = "none")]
2705//#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
2706impl<T: DispatchFromDyn<U>, U> DispatchFromDyn<SyncUnsafeCell<U>> for SyncUnsafeCell<T> {}
2707
2708#[allow(unused)]
2709fn assert_coerce_unsized(
2710    a: UnsafeCell<&i32>,
2711    b: SyncUnsafeCell<&i32>,
2712    c: Cell<&i32>,
2713    d: RefCell<&i32>,
2714) {
2715    let _: UnsafeCell<&dyn Send> = a;
2716    let _: SyncUnsafeCell<&dyn Send> = b;
2717    let _: Cell<&dyn Send> = c;
2718    let _: RefCell<&dyn Send> = d;
2719}
2720
2721#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2722unsafe impl<T: ?Sized> PinCoerceUnsized for UnsafeCell<T> {}
2723
2724#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2725unsafe impl<T: ?Sized> PinCoerceUnsized for SyncUnsafeCell<T> {}
2726
2727#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2728unsafe impl<T: ?Sized> PinCoerceUnsized for Cell<T> {}
2729
2730#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2731unsafe impl<T: ?Sized> PinCoerceUnsized for RefCell<T> {}
2732
2733#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2734unsafe impl<'b, T: ?Sized> PinCoerceUnsized for Ref<'b, T> {}
2735
2736#[unstable(feature = "pin_coerce_unsized_trait", issue = "150112")]
2737unsafe impl<'b, T: ?Sized> PinCoerceUnsized for RefMut<'b, T> {}
````