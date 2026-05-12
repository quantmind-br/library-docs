---
title: atomic.rs - source
url: https://doc.rust-lang.org/src/core/sync/atomic.rs.html#299
source: crawler
fetched_at: 2026-05-06T21:29:52.907393361-03:00
rendered_js: false
word_count: 23237
summary: This document describes the atomic types in Rust, explaining their role in shared-memory thread communication, their memory model, and the requirements for avoiding data races.
tags:
    - concurrency
    - atomics
    - memory-model
    - threading
    - rust-sync
    - data-races
category: concept
---

## core/sync/ atomic.rs

````rust
1//! Atomic types
2//!
3//! Atomic types provide primitive shared-memory communication between
4//! threads, and are the building blocks of other concurrent
5//! types.
6//!
7//! This module defines atomic versions of a select number of primitive
8//! types, including [`AtomicBool`], [`AtomicIsize`], [`AtomicUsize`],
9//! [`AtomicI8`], [`AtomicU16`], etc.
10//! Atomic types present operations that, when used correctly, synchronize
11//! updates between threads.
12//!
13//! Atomic variables are safe to share between threads (they implement [`Sync`])
14//! but they do not themselves provide the mechanism for sharing and follow the
15//! [threading model](../../../std/thread/index.html#the-threading-model) of Rust.
16//! The most common way to share an atomic variable is to put it into an [`Arc`][arc] (an
17//! atomically-reference-counted shared pointer).
18//!
19//! [arc]: ../../../std/sync/struct.Arc.html
20//!
21//! Atomic types may be stored in static variables, initialized using
22//! the constant initializers like [`AtomicBool::new`]. Atomic statics
23//! are often used for lazy global initialization.
24//!
25//! ## Memory model for atomic accesses
26//!
27//! Rust atomics currently follow the same rules as [C++20 atomics][cpp], specifically the rules
28//! from the [`intro.races`][cpp-intro.races] section, without the "consume" memory ordering. Since
29//! C++ uses an object-based memory model whereas Rust is access-based, a bit of translation work
30//! has to be done to apply the C++ rules to Rust: whenever C++ talks about "the value of an
31//! object", we understand that to mean the resulting bytes obtained when doing a read. When the C++
32//! standard talks about "the value of an atomic object", this refers to the result of doing an
33//! atomic load (via the operations provided in this module). A "modification of an atomic object"
34//! refers to an atomic store.
35//!
36//! The end result is *almost* equivalent to saying that creating a *shared reference* to one of the
37//! Rust atomic types corresponds to creating an `atomic_ref` in C++, with the `atomic_ref` being
38//! destroyed when the lifetime of the shared reference ends. The main difference is that Rust
39//! permits concurrent atomic and non-atomic reads to the same memory as those cause no issue in the
40//! C++ memory model, they are just forbidden in C++ because memory is partitioned into "atomic
41//! objects" and "non-atomic objects" (with `atomic_ref` temporarily converting a non-atomic object
42//! into an atomic object).
43//!
44//! The most important aspect of this model is that *data races* are undefined behavior. A data race
45//! is defined as conflicting non-synchronized accesses where at least one of the accesses is
46//! non-atomic. Here, accesses are *conflicting* if they affect overlapping regions of memory and at
47//! least one of them is a write. (A `compare_exchange` or `compare_exchange_weak` that does not
48//! succeed is not considered a write.) They are *non-synchronized* if neither of them
49//! *happens-before* the other, according to the happens-before order of the memory model.
50//!
51//! The other possible cause of undefined behavior in the memory model are mixed-size accesses: Rust
52//! inherits the C++ limitation that non-synchronized conflicting atomic accesses may not partially
53//! overlap. In other words, every pair of non-synchronized atomic accesses must be either disjoint,
54//! access the exact same memory (including using the same access size), or both be reads.
55//!
56//! Each atomic access takes an [`Ordering`] which defines how the operation interacts with the
57//! happens-before order. These orderings behave the same as the corresponding [C++20 atomic
58//! orderings][cpp_memory_order]. For more information, see the [nomicon].
59//!
60//! [cpp]: https://en.cppreference.com/w/cpp/atomic
61//! [cpp-intro.races]: https://timsong-cpp.github.io/cppwp/n4868/intro.multithread#intro.races
62//! [cpp_memory_order]: https://en.cppreference.com/w/cpp/atomic/memory_order
63//! [nomicon]: ../../../nomicon/atomics.html
64//!
65//! ```rust,no_run undefined_behavior
66//! use std::sync::atomic::{AtomicU16, AtomicU8, Ordering};
67//! use std::mem::transmute;
68//! use std::thread;
69//!
70//! let atomic = AtomicU16::new(0);
71//!
72//! thread::scope(|s| {
73//!     // This is UB: conflicting non-synchronized accesses, at least one of which is non-atomic.
74//!     s.spawn(|| atomic.store(1, Ordering::Relaxed)); // atomic store
75//!     s.spawn(|| unsafe { atomic.as_ptr().write(2) }); // non-atomic write
76//! });
77//!
78//! thread::scope(|s| {
79//!     // This is fine: the accesses do not conflict (as none of them performs any modification).
80//!     // In C++ this would be disallowed since creating an `atomic_ref` precludes
81//!     // further non-atomic accesses, but Rust does not have that limitation.
82//!     s.spawn(|| atomic.load(Ordering::Relaxed)); // atomic load
83//!     s.spawn(|| unsafe { atomic.as_ptr().read() }); // non-atomic read
84//! });
85//!
86//! thread::scope(|s| {
87//!     // This is fine: `join` synchronizes the code in a way such that the atomic
88//!     // store happens-before the non-atomic write.
89//!     let handle = s.spawn(|| atomic.store(1, Ordering::Relaxed)); // atomic store
90//!     handle.join().expect("thread won't panic"); // synchronize
91//!     s.spawn(|| unsafe { atomic.as_ptr().write(2) }); // non-atomic write
92//! });
93//!
94//! thread::scope(|s| {
95//!     // This is UB: non-synchronized conflicting differently-sized atomic accesses.
96//!     s.spawn(|| atomic.store(1, Ordering::Relaxed));
97//!     s.spawn(|| unsafe {
98//!         let differently_sized = transmute::<&AtomicU16, &AtomicU8>(&atomic);
99//!         differently_sized.store(2, Ordering::Relaxed);
100//!     });
101//! });
102//!
103//! thread::scope(|s| {
104//!     // This is fine: `join` synchronizes the code in a way such that
105//!     // the 1-byte store happens-before the 2-byte store.
106//!     let handle = s.spawn(|| atomic.store(1, Ordering::Relaxed));
107//!     handle.join().expect("thread won't panic");
108//!     s.spawn(|| unsafe {
109//!         let differently_sized = transmute::<&AtomicU16, &AtomicU8>(&atomic);
110//!         differently_sized.store(2, Ordering::Relaxed);
111//!     });
112//! });
113//! ```
114//!
115//! # Portability
116//!
117//! All atomic types in this module are guaranteed to be [lock-free] if they're
118//! available. This means they don't internally acquire a global mutex. Atomic
119//! types and operations are not guaranteed to be wait-free. This means that
120//! operations like `fetch_or` may be implemented with a compare-and-swap loop.
121//!
122//! Atomic operations may be implemented at the instruction layer with
123//! larger-size atomics. For example some platforms use 4-byte atomic
124//! instructions to implement `AtomicI8`. Note that this emulation should not
125//! have an impact on correctness of code, it's just something to be aware of.
126//!
127//! The atomic types in this module might not be available on all platforms. The
128//! atomic types here are all widely available, however, and can generally be
129//! relied upon existing. Some notable exceptions are:
130//!
131//! * PowerPC and MIPS platforms with 32-bit pointers do not have `AtomicU64` or
132//!   `AtomicI64` types.
133//! * Legacy ARM platforms like ARMv4T and ARMv5TE have very limited hardware
134//!   support for atomics. The bare-metal targets disable this module
135//!   entirely, but the Linux targets [use the kernel] to assist (which comes
136//!   with a performance penalty). It's not until ARMv6K onwards that ARM CPUs
137//!   have support for load/store and Compare and Swap (CAS) atomics in hardware.
138//! * ARMv6-M and ARMv8-M baseline targets (`thumbv6m-*` and
139//!   `thumbv8m.base-*`) only provide `load` and `store` operations, and do
140//!   not support Compare and Swap (CAS) operations, such as `swap`,
141//!   `fetch_add`, etc. Full CAS support is available on ARMv7-M and ARMv8-M
142//!   Mainline (`thumbv7m-*`, `thumbv7em*` and `thumbv8m.main-*`).
143//!
144//! [use the kernel]: https://www.kernel.org/doc/Documentation/arm/kernel_user_helpers.txt
145//!
146//! Note that future platforms may be added that also do not have support for
147//! some atomic operations. Maximally portable code will want to be careful
148//! about which atomic types are used. `AtomicUsize` and `AtomicIsize` are
149//! generally the most portable, but even then they're not available everywhere.
150//! For reference, the `std` library requires `AtomicBool`s and pointer-sized atomics, although
151//! `core` does not.
152//!
153//! The `#[cfg(target_has_atomic)]` attribute can be used to conditionally
154//! compile based on the target's supported bit widths. It is a key-value
155//! option set for each supported size, with values "8", "16", "32", "64",
156//! "128", and "ptr" for pointer-sized atomics.
157//!
158//! [lock-free]: https://en.wikipedia.org/wiki/Non-blocking_algorithm
159//!
160//! # Atomic accesses to read-only memory
161//!
162//! In general, *all* atomic accesses on read-only memory are undefined behavior. For instance, attempting
163//! to do a `compare_exchange` that will definitely fail (making it conceptually a read-only
164//! operation) can still cause a segmentation fault if the underlying memory page is mapped read-only. Since
165//! atomic `load`s might be implemented using compare-exchange operations, even a `load` can fault
166//! on read-only memory.
167//!
168//! For the purpose of this section, "read-only memory" is defined as memory that is read-only in
169//! the underlying target, i.e., the pages are mapped with a read-only flag and any attempt to write
170//! will cause a page fault. In particular, an `&u128` reference that points to memory that is
171//! read-write mapped is *not* considered to point to "read-only memory". In Rust, almost all memory
172//! is read-write; the only exceptions are memory created by `const` items or `static` items without
173//! interior mutability, and memory that was specifically marked as read-only by the operating
174//! system via platform-specific APIs.
175//!
176//! As an exception from the general rule stated above, "sufficiently small" atomic loads with
177//! `Ordering::Relaxed` are implemented in a way that works on read-only memory, and are hence not
178//! undefined behavior. The exact size limit for what makes a load "sufficiently small" varies
179//! depending on the target:
180//!
181//! | `target_arch` | Size limit |
182//! |---------------|---------|
183//! | `x86`, `arm`, `loongarch32`, `mips`, `mips32r6`, `powerpc`, `riscv32`, `sparc`, `hexagon` | 4 bytes |
184//! | `x86_64`, `aarch64`, `loongarch64`, `mips64`, `mips64r6`, `powerpc64`, `riscv64`, `sparc64`, `s390x` | 8 bytes |
185//!
186//! Atomics loads that are larger than this limit as well as atomic loads with ordering other
187//! than `Relaxed`, as well as *all* atomic loads on targets not listed in the table, might still be
188//! read-only under certain conditions, but that is not a stable guarantee and should not be relied
189//! upon.
190//!
191//! If you need to do an acquire load on read-only memory, you can do a relaxed load followed by an
192//! acquire fence instead.
193//!
194//! # Examples
195//!
196//! A simple spinlock:
197//!
198//! ```ignore-wasm
199//! use std::sync::Arc;
200//! use std::sync::atomic::{AtomicUsize, Ordering};
201//! use std::{hint, thread};
202//!
203//! fn main() {
204//!     let spinlock = Arc::new(AtomicUsize::new(1));
205//!
206//!     let spinlock_clone = Arc::clone(&spinlock);
207//!
208//!     let thread = thread::spawn(move || {
209//!         spinlock_clone.store(0, Ordering::Release);
210//!     });
211//!
212//!     // Wait for the other thread to release the lock
213//!     while spinlock.load(Ordering::Acquire) != 0 {
214//!         hint::spin_loop();
215//!     }
216//!
217//!     if let Err(panic) = thread.join() {
218//!         println!("Thread had an error: {panic:?}");
219//!     }
220//! }
221//! ```
222//!
223//! Keep a global count of live threads:
224//!
225//! ```
226//! use std::sync::atomic::{AtomicUsize, Ordering};
227//!
228//! static GLOBAL_THREAD_COUNT: AtomicUsize = AtomicUsize::new(0);
229//!
230//! // Note that Relaxed ordering doesn't synchronize anything
231//! // except the global thread counter itself.
232//! let old_thread_count = GLOBAL_THREAD_COUNT.fetch_add(1, Ordering::Relaxed);
233//! // Note that this number may not be true at the moment of printing
234//! // because some other thread may have changed static value already.
235//! println!("live threads: {}", old_thread_count + 1);
236//! ```
237
238#![stable(feature = "rust1", since = "1.0.0")]
239#![cfg_attr(not(target_has_atomic_load_store = "8"), allow(dead_code))]
240#![cfg_attr(not(target_has_atomic_load_store = "8"), allow(unused_imports))]
241#![rustc_diagnostic_item = "atomic_mod"]
242// Clippy complains about the pattern of "safe function calling unsafe function taking pointers".
243// This happens with AtomicPtr intrinsics but is fine, as the pointers clippy is concerned about
244// are just normal values that get loaded/stored, but not dereferenced.
245#![allow(clippy::not_unsafe_ptr_arg_deref)]
246
247use self::Ordering::*;
248use crate::cell::UnsafeCell;
249use crate::hint::spin_loop;
250use crate::intrinsics::AtomicOrdering as AO;
251use crate::{fmt, intrinsics};
252
253trait Sealed {}
254
255/// A marker trait for primitive types which can be modified atomically.
256///
257/// This is an implementation detail for <code>[Atomic]\<T></code> which may disappear or be replaced at any time.
258///
259/// # Safety
260///
261/// Types implementing this trait must be primitives that can be modified atomically.
262///
263/// The associated `Self::AtomicInner` type must have the same size and bit validity as `Self`,
264/// but may have a higher alignment requirement, so the following `transmute`s are sound:
265///
266/// - `&mut Self::AtomicInner` as `&mut Self`
267/// - `Self` as `Self::AtomicInner` or the reverse
268#[unstable(
269    feature = "atomic_internals",
270    reason = "implementation detail which may disappear or be replaced at any time",
271    issue = "none"
272)]
273#[expect(private_bounds)]
274pub unsafe trait AtomicPrimitive: Sized + Copy + Sealed {
275    /// Temporary implementation detail.
276    type AtomicInner: Sized;
277}
278
279macro impl_atomic_primitive(
280    $Atom:ident $(<$T:ident>)? ($Primitive:ty),
281    size($size:literal),
282    align($align:literal) $(,)?
283) {
284    impl $(<$T>)? Sealed for $Primitive {}
285
286    #[unstable(
287        feature = "atomic_internals",
288        reason = "implementation detail which may disappear or be replaced at any time",
289        issue = "none"
290    )]
291    #[cfg(target_has_atomic_load_store = $size)]
292    unsafe impl $(<$T>)? AtomicPrimitive for $Primitive {
293        type AtomicInner = $Atom $(<$T>)?;
294    }
295}
296
297impl_atomic_primitive!(AtomicBool(bool), size("8"), align(1));
298impl_atomic_primitive!(AtomicI8(i8), size("8"), align(1));
299impl_atomic_primitive!(AtomicU8(u8), size("8"), align(1));
300impl_atomic_primitive!(AtomicI16(i16), size("16"), align(2));
301impl_atomic_primitive!(AtomicU16(u16), size("16"), align(2));
302impl_atomic_primitive!(AtomicI32(i32), size("32"), align(4));
303impl_atomic_primitive!(AtomicU32(u32), size("32"), align(4));
304impl_atomic_primitive!(AtomicI64(i64), size("64"), align(8));
305impl_atomic_primitive!(AtomicU64(u64), size("64"), align(8));
306impl_atomic_primitive!(AtomicI128(i128), size("128"), align(16));
307impl_atomic_primitive!(AtomicU128(u128), size("128"), align(16));
308
309#[cfg(target_pointer_width = "16")]
310impl_atomic_primitive!(AtomicIsize(isize), size("ptr"), align(2));
311#[cfg(target_pointer_width = "32")]
312impl_atomic_primitive!(AtomicIsize(isize), size("ptr"), align(4));
313#[cfg(target_pointer_width = "64")]
314impl_atomic_primitive!(AtomicIsize(isize), size("ptr"), align(8));
315
316#[cfg(target_pointer_width = "16")]
317impl_atomic_primitive!(AtomicUsize(usize), size("ptr"), align(2));
318#[cfg(target_pointer_width = "32")]
319impl_atomic_primitive!(AtomicUsize(usize), size("ptr"), align(4));
320#[cfg(target_pointer_width = "64")]
321impl_atomic_primitive!(AtomicUsize(usize), size("ptr"), align(8));
322
323#[cfg(target_pointer_width = "16")]
324impl_atomic_primitive!(AtomicPtr<T>(*mut T), size("ptr"), align(2));
325#[cfg(target_pointer_width = "32")]
326impl_atomic_primitive!(AtomicPtr<T>(*mut T), size("ptr"), align(4));
327#[cfg(target_pointer_width = "64")]
328impl_atomic_primitive!(AtomicPtr<T>(*mut T), size("ptr"), align(8));
329
330/// A memory location which can be safely modified from multiple threads.
331///
332/// This has the same size and bit validity as the underlying type `T`. However,
333/// the alignment of this type is always equal to its size, even on targets where
334/// `T` has alignment less than its size.
335///
336/// For more about the differences between atomic types and non-atomic types as
337/// well as information about the portability of this type, please see the
338/// [module-level documentation].
339///
340/// **Note:** This type is only available on platforms that support atomic loads
341/// and stores of `T`.
342///
343/// [module-level documentation]: crate::sync::atomic
344#[unstable(feature = "generic_atomic", issue = "130539")]
345pub type Atomic<T> = <T as AtomicPrimitive>::AtomicInner;
346
347// Some architectures don't have byte-sized atomics, which results in LLVM
348// emulating them using a LL/SC loop. However for AtomicBool we can take
349// advantage of the fact that it only ever contains 0 or 1 and use atomic OR/AND
350// instead, which LLVM can emulate using a larger atomic OR/AND operation.
351//
352// This list should only contain architectures which have word-sized atomic-or/
353// atomic-and instructions but don't natively support byte-sized atomics.
354#[cfg(target_has_atomic = "8")]
355const EMULATE_ATOMIC_BOOL: bool = cfg!(any(
356    target_arch = "riscv32",
357    target_arch = "riscv64",
358    target_arch = "loongarch32",
359    target_arch = "loongarch64"
360));
361
362/// A boolean type which can be safely shared between threads.
363///
364/// This type has the same size, alignment, and bit validity as a [`bool`].
365///
366/// **Note**: This type is only available on platforms that support atomic
367/// loads and stores of `u8`.
368#[cfg(target_has_atomic_load_store = "8")]
369#[stable(feature = "rust1", since = "1.0.0")]
370#[rustc_diagnostic_item = "AtomicBool"]
371#[repr(C, align(1))]
372pub struct AtomicBool {
373    v: UnsafeCell<u8>,
374}
375
376#[cfg(target_has_atomic_load_store = "8")]
377#[stable(feature = "rust1", since = "1.0.0")]
378impl Default for AtomicBool {
379    /// Creates an `AtomicBool` initialized to `false`.
380    #[inline]
381    fn default() -> Self {
382        Self::new(false)
383    }
384}
385
386// Send is implicitly implemented for AtomicBool.
387#[cfg(target_has_atomic_load_store = "8")]
388#[stable(feature = "rust1", since = "1.0.0")]
389unsafe impl Sync for AtomicBool {}
390
391/// A raw pointer type which can be safely shared between threads.
392///
393/// This type has the same size and bit validity as a `*mut T`.
394///
395/// **Note**: This type is only available on platforms that support atomic
396/// loads and stores of pointers. Its size depends on the target pointer's size.
397#[cfg(target_has_atomic_load_store = "ptr")]
398#[stable(feature = "rust1", since = "1.0.0")]
399#[rustc_diagnostic_item = "AtomicPtr"]
400#[cfg_attr(target_pointer_width = "16", repr(C, align(2)))]
401#[cfg_attr(target_pointer_width = "32", repr(C, align(4)))]
402#[cfg_attr(target_pointer_width = "64", repr(C, align(8)))]
403pub struct AtomicPtr<T> {
404    p: UnsafeCell<*mut T>,
405}
406
407#[cfg(target_has_atomic_load_store = "ptr")]
408#[stable(feature = "rust1", since = "1.0.0")]
409impl<T> Default for AtomicPtr<T> {
410    /// Creates a null `AtomicPtr<T>`.
411    fn default() -> AtomicPtr<T> {
412        AtomicPtr::new(crate::ptr::null_mut())
413    }
414}
415
416#[cfg(target_has_atomic_load_store = "ptr")]
417#[stable(feature = "rust1", since = "1.0.0")]
418unsafe impl<T> Send for AtomicPtr<T> {}
419#[cfg(target_has_atomic_load_store = "ptr")]
420#[stable(feature = "rust1", since = "1.0.0")]
421unsafe impl<T> Sync for AtomicPtr<T> {}
422
423/// Atomic memory orderings
424///
425/// Memory orderings specify the way atomic operations synchronize memory.
426/// In its weakest [`Ordering::Relaxed`], only the memory directly touched by the
427/// operation is synchronized. On the other hand, a store-load pair of [`Ordering::SeqCst`]
428/// operations synchronize other memory while additionally preserving a total order of such
429/// operations across all threads.
430///
431/// Rust's memory orderings are [the same as those of
432/// C++20](https://en.cppreference.com/w/cpp/atomic/memory_order).
433///
434/// For more information see the [nomicon].
435///
436/// [nomicon]: ../../../nomicon/atomics.html
437#[stable(feature = "rust1", since = "1.0.0")]
438#[derive(Copy, Clone, Debug, Eq, PartialEq, Hash)]
439#[non_exhaustive]
440#[rustc_diagnostic_item = "Ordering"]
441pub enum Ordering {
442    /// No ordering constraints, only atomic operations.
443    ///
444    /// Corresponds to [`memory_order_relaxed`] in C++20.
445    ///
446    /// [`memory_order_relaxed`]: https://en.cppreference.com/w/cpp/atomic/memory_order#Relaxed_ordering
447    #[stable(feature = "rust1", since = "1.0.0")]
448    Relaxed,
449    /// When coupled with a store, all previous operations become ordered
450    /// before any load of this value with [`Acquire`] (or stronger) ordering.
451    /// In particular, all previous writes become visible to all threads
452    /// that perform an [`Acquire`] (or stronger) load of this value.
453    ///
454    /// Notice that using this ordering for an operation that combines loads
455    /// and stores leads to a [`Relaxed`] load operation!
456    ///
457    /// This ordering is only applicable for operations that can perform a store.
458    ///
459    /// Corresponds to [`memory_order_release`] in C++20.
460    ///
461    /// [`memory_order_release`]: https://en.cppreference.com/w/cpp/atomic/memory_order#Release-Acquire_ordering
462    #[stable(feature = "rust1", since = "1.0.0")]
463    Release,
464    /// When coupled with a load, if the loaded value was written by a store operation with
465    /// [`Release`] (or stronger) ordering, then all subsequent operations
466    /// become ordered after that store. In particular, all subsequent loads will see data
467    /// written before the store.
468    ///
469    /// Notice that using this ordering for an operation that combines loads
470    /// and stores leads to a [`Relaxed`] store operation!
471    ///
472    /// This ordering is only applicable for operations that can perform a load.
473    ///
474    /// Corresponds to [`memory_order_acquire`] in C++20.
475    ///
476    /// [`memory_order_acquire`]: https://en.cppreference.com/w/cpp/atomic/memory_order#Release-Acquire_ordering
477    #[stable(feature = "rust1", since = "1.0.0")]
478    Acquire,
479    /// Has the effects of both [`Acquire`] and [`Release`] together:
480    /// For loads it uses [`Acquire`] ordering. For stores it uses the [`Release`] ordering.
481    ///
482    /// Notice that in the case of `compare_and_swap`, it is possible that the operation ends up
483    /// not performing any store and hence it has just [`Acquire`] ordering. However,
484    /// `AcqRel` will never perform [`Relaxed`] accesses.
485    ///
486    /// This ordering is only applicable for operations that combine both loads and stores.
487    ///
488    /// Corresponds to [`memory_order_acq_rel`] in C++20.
489    ///
490    /// [`memory_order_acq_rel`]: https://en.cppreference.com/w/cpp/atomic/memory_order#Release-Acquire_ordering
491    #[stable(feature = "rust1", since = "1.0.0")]
492    AcqRel,
493    /// Like [`Acquire`]/[`Release`]/[`AcqRel`] (for load, store, and load-with-store
494    /// operations, respectively) with the additional guarantee that all threads see all
495    /// sequentially consistent operations in the same order.
496    ///
497    /// Corresponds to [`memory_order_seq_cst`] in C++20.
498    ///
499    /// [`memory_order_seq_cst`]: https://en.cppreference.com/w/cpp/atomic/memory_order#Sequentially-consistent_ordering
500    #[stable(feature = "rust1", since = "1.0.0")]
501    SeqCst,
502}
503
504/// An [`AtomicBool`] initialized to `false`.
505#[cfg(target_has_atomic_load_store = "8")]
506#[stable(feature = "rust1", since = "1.0.0")]
507#[deprecated(
508    since = "1.34.0",
509    note = "the `new` function is now preferred",
510    suggestion = "AtomicBool::new(false)"
511)]
512pub const ATOMIC_BOOL_INIT: AtomicBool = AtomicBool::new(false);
513
514#[cfg(target_has_atomic_load_store = "8")]
515impl AtomicBool {
516    /// Creates a new `AtomicBool`.
517    ///
518    /// # Examples
519    ///
520    /// ```
521    /// use std::sync::atomic::AtomicBool;
522    ///
523    /// let atomic_true = AtomicBool::new(true);
524    /// let atomic_false = AtomicBool::new(false);
525    /// ```
526    #[inline]
527    #[stable(feature = "rust1", since = "1.0.0")]
528    #[rustc_const_stable(feature = "const_atomic_new", since = "1.24.0")]
529    #[must_use]
530    pub const fn new(v: bool) -> AtomicBool {
531        AtomicBool { v: UnsafeCell::new(v as u8) }
532    }
533
534    /// Creates a new `AtomicBool` from a pointer.
535    ///
536    /// # Examples
537    ///
538    /// ```
539    /// use std::sync::atomic::{self, AtomicBool};
540    ///
541    /// // Get a pointer to an allocated value
542    /// let ptr: *mut bool = Box::into_raw(Box::new(false));
543    ///
544    /// assert!(ptr.cast::<AtomicBool>().is_aligned());
545    ///
546    /// {
547    ///     // Create an atomic view of the allocated value
548    ///     let atomic = unsafe { AtomicBool::from_ptr(ptr) };
549    ///
550    ///     // Use `atomic` for atomic operations, possibly share it with other threads
551    ///     atomic.store(true, atomic::Ordering::Relaxed);
552    /// }
553    ///
554    /// // It's ok to non-atomically access the value behind `ptr`,
555    /// // since the reference to the atomic ended its lifetime in the block above
556    /// assert_eq!(unsafe { *ptr }, true);
557    ///
558    /// // Deallocate the value
559    /// unsafe { drop(Box::from_raw(ptr)) }
560    /// ```
561    ///
562    /// # Safety
563    ///
564    /// * `ptr` must be aligned to `align_of::<AtomicBool>()` (note that this is always true, since
565    ///   `align_of::<AtomicBool>() == 1`).
566    /// * `ptr` must be [valid] for both reads and writes for the whole lifetime `'a`.
567    /// * You must adhere to the [Memory model for atomic accesses]. In particular, it is not
568    ///   allowed to mix conflicting atomic and non-atomic accesses, or atomic accesses of different
569    ///   sizes, without synchronization.
570    ///
571    /// [valid]: crate::ptr#safety
572    /// [Memory model for atomic accesses]: self#memory-model-for-atomic-accesses
573    #[inline]
574    #[stable(feature = "atomic_from_ptr", since = "1.75.0")]
575    #[rustc_const_stable(feature = "const_atomic_from_ptr", since = "1.84.0")]
576    pub const unsafe fn from_ptr<'a>(ptr: *mut bool) -> &'a AtomicBool {
577        // SAFETY: guaranteed by the caller
578        unsafe { &*ptr.cast() }
579    }
580
581    /// Returns a mutable reference to the underlying [`bool`].
582    ///
583    /// This is safe because the mutable reference guarantees that no other threads are
584    /// concurrently accessing the atomic data.
585    ///
586    /// # Examples
587    ///
588    /// ```
589    /// use std::sync::atomic::{AtomicBool, Ordering};
590    ///
591    /// let mut some_bool = AtomicBool::new(true);
592    /// assert_eq!(*some_bool.get_mut(), true);
593    /// *some_bool.get_mut() = false;
594    /// assert_eq!(some_bool.load(Ordering::SeqCst), false);
595    /// ```
596    #[inline]
597    #[stable(feature = "atomic_access", since = "1.15.0")]
598    pub fn get_mut(&mut self) -> &mut bool {
599        // SAFETY: the mutable reference guarantees unique ownership.
600        unsafe { &mut *(self.v.get() as *mut bool) }
601    }
602
603    /// Gets atomic access to a `&mut bool`.
604    ///
605    /// # Examples
606    ///
607    /// ```
608    /// #![feature(atomic_from_mut)]
609    /// use std::sync::atomic::{AtomicBool, Ordering};
610    ///
611    /// let mut some_bool = true;
612    /// let a = AtomicBool::from_mut(&mut some_bool);
613    /// a.store(false, Ordering::Relaxed);
614    /// assert_eq!(some_bool, false);
615    /// ```
616    #[inline]
617    #[cfg(target_has_atomic_equal_alignment = "8")]
618    #[unstable(feature = "atomic_from_mut", issue = "76314")]
619    pub fn from_mut(v: &mut bool) -> &mut Self {
620        // SAFETY: the mutable reference guarantees unique ownership, and
621        // alignment of both `bool` and `Self` is 1.
622        unsafe { &mut *(v as *mut bool as *mut Self) }
623    }
624
625    /// Gets non-atomic access to a `&mut [AtomicBool]` slice.
626    ///
627    /// This is safe because the mutable reference guarantees that no other threads are
628    /// concurrently accessing the atomic data.
629    ///
630    /// # Examples
631    ///
632    /// ```ignore-wasm
633    /// #![feature(atomic_from_mut)]
634    /// use std::sync::atomic::{AtomicBool, Ordering};
635    ///
636    /// let mut some_bools = [const { AtomicBool::new(false) }; 10];
637    ///
638    /// let view: &mut [bool] = AtomicBool::get_mut_slice(&mut some_bools);
639    /// assert_eq!(view, [false; 10]);
640    /// view[..5].copy_from_slice(&[true; 5]);
641    ///
642    /// std::thread::scope(|s| {
643    ///     for t in &some_bools[..5] {
644    ///         s.spawn(move || assert_eq!(t.load(Ordering::Relaxed), true));
645    ///     }
646    ///
647    ///     for f in &some_bools[5..] {
648    ///         s.spawn(move || assert_eq!(f.load(Ordering::Relaxed), false));
649    ///     }
650    /// });
651    /// ```
652    #[inline]
653    #[unstable(feature = "atomic_from_mut", issue = "76314")]
654    pub fn get_mut_slice(this: &mut [Self]) -> &mut [bool] {
655        // SAFETY: the mutable reference guarantees unique ownership.
656        unsafe { &mut *(this as *mut [Self] as *mut [bool]) }
657    }
658
659    /// Gets atomic access to a `&mut [bool]` slice.
660    ///
661    /// # Examples
662    ///
663    /// ```rust,ignore-wasm
664    /// #![feature(atomic_from_mut)]
665    /// use std::sync::atomic::{AtomicBool, Ordering};
666    ///
667    /// let mut some_bools = [false; 10];
668    /// let a = &*AtomicBool::from_mut_slice(&mut some_bools);
669    /// std::thread::scope(|s| {
670    ///     for i in 0..a.len() {
671    ///         s.spawn(move || a[i].store(true, Ordering::Relaxed));
672    ///     }
673    /// });
674    /// assert_eq!(some_bools, [true; 10]);
675    /// ```
676    #[inline]
677    #[cfg(target_has_atomic_equal_alignment = "8")]
678    #[unstable(feature = "atomic_from_mut", issue = "76314")]
679    pub fn from_mut_slice(v: &mut [bool]) -> &mut [Self] {
680        // SAFETY: the mutable reference guarantees unique ownership, and
681        // alignment of both `bool` and `Self` is 1.
682        unsafe { &mut *(v as *mut [bool] as *mut [Self]) }
683    }
684
685    /// Consumes the atomic and returns the contained value.
686    ///
687    /// This is safe because passing `self` by value guarantees that no other threads are
688    /// concurrently accessing the atomic data.
689    ///
690    /// # Examples
691    ///
692    /// ```
693    /// use std::sync::atomic::AtomicBool;
694    ///
695    /// let some_bool = AtomicBool::new(true);
696    /// assert_eq!(some_bool.into_inner(), true);
697    /// ```
698    #[inline]
699    #[stable(feature = "atomic_access", since = "1.15.0")]
700    #[rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0")]
701    pub const fn into_inner(self) -> bool {
702        self.v.into_inner() != 0
703    }
704
705    /// Loads a value from the bool.
706    ///
707    /// `load` takes an [`Ordering`] argument which describes the memory ordering
708    /// of this operation. Possible values are [`SeqCst`], [`Acquire`] and [`Relaxed`].
709    ///
710    /// # Panics
711    ///
712    /// Panics if `order` is [`Release`] or [`AcqRel`].
713    ///
714    /// # Examples
715    ///
716    /// ```
717    /// use std::sync::atomic::{AtomicBool, Ordering};
718    ///
719    /// let some_bool = AtomicBool::new(true);
720    ///
721    /// assert_eq!(some_bool.load(Ordering::Relaxed), true);
722    /// ```
723    #[inline]
724    #[stable(feature = "rust1", since = "1.0.0")]
725    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
726    pub fn load(&self, order: Ordering) -> bool {
727        // SAFETY: any data races are prevented by atomic intrinsics and the raw
728        // pointer passed in is valid because we got it from a reference.
729        unsafe { atomic_load(self.v.get(), order) != 0 }
730    }
731
732    /// Stores a value into the bool.
733    ///
734    /// `store` takes an [`Ordering`] argument which describes the memory ordering
735    /// of this operation. Possible values are [`SeqCst`], [`Release`] and [`Relaxed`].
736    ///
737    /// # Panics
738    ///
739    /// Panics if `order` is [`Acquire`] or [`AcqRel`].
740    ///
741    /// # Examples
742    ///
743    /// ```
744    /// use std::sync::atomic::{AtomicBool, Ordering};
745    ///
746    /// let some_bool = AtomicBool::new(true);
747    ///
748    /// some_bool.store(false, Ordering::Relaxed);
749    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
750    /// ```
751    #[inline]
752    #[stable(feature = "rust1", since = "1.0.0")]
753    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
754    #[rustc_should_not_be_called_on_const_items]
755    pub fn store(&self, val: bool, order: Ordering) {
756        // SAFETY: any data races are prevented by atomic intrinsics and the raw
757        // pointer passed in is valid because we got it from a reference.
758        unsafe {
759            atomic_store(self.v.get(), val as u8, order);
760        }
761    }
762
763    /// Stores a value into the bool, returning the previous value.
764    ///
765    /// `swap` takes an [`Ordering`] argument which describes the memory ordering
766    /// of this operation. All ordering modes are possible. Note that using
767    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
768    /// using [`Release`] makes the load part [`Relaxed`].
769    ///
770    /// **Note:** This method is only available on platforms that support atomic
771    /// operations on `u8`.
772    ///
773    /// # Examples
774    ///
775    /// ```
776    /// use std::sync::atomic::{AtomicBool, Ordering};
777    ///
778    /// let some_bool = AtomicBool::new(true);
779    ///
780    /// assert_eq!(some_bool.swap(false, Ordering::Relaxed), true);
781    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
782    /// ```
783    #[inline]
784    #[stable(feature = "rust1", since = "1.0.0")]
785    #[cfg(target_has_atomic = "8")]
786    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
787    #[rustc_should_not_be_called_on_const_items]
788    pub fn swap(&self, val: bool, order: Ordering) -> bool {
789        if EMULATE_ATOMIC_BOOL {
790            if val { self.fetch_or(true, order) } else { self.fetch_and(false, order) }
791        } else {
792            // SAFETY: data races are prevented by atomic intrinsics.
793            unsafe { atomic_swap(self.v.get(), val as u8, order) != 0 }
794        }
795    }
796
797    /// Stores a value into the [`bool`] if the current value is the same as the `current` value.
798    ///
799    /// The return value is always the previous value. If it is equal to `current`, then the value
800    /// was updated.
801    ///
802    /// `compare_and_swap` also takes an [`Ordering`] argument which describes the memory
803    /// ordering of this operation. Notice that even when using [`AcqRel`], the operation
804    /// might fail and hence just perform an `Acquire` load, but not have `Release` semantics.
805    /// Using [`Acquire`] makes the store part of this operation [`Relaxed`] if it
806    /// happens, and using [`Release`] makes the load part [`Relaxed`].
807    ///
808    /// **Note:** This method is only available on platforms that support atomic
809    /// operations on `u8`.
810    ///
811    /// # Migrating to `compare_exchange` and `compare_exchange_weak`
812    ///
813    /// `compare_and_swap` is equivalent to `compare_exchange` with the following mapping for
814    /// memory orderings:
815    ///
816    /// Original | Success | Failure
817    /// -------- | ------- | -------
818    /// Relaxed  | Relaxed | Relaxed
819    /// Acquire  | Acquire | Acquire
820    /// Release  | Release | Relaxed
821    /// AcqRel   | AcqRel  | Acquire
822    /// SeqCst   | SeqCst  | SeqCst
823    ///
824    /// `compare_and_swap` and `compare_exchange` also differ in their return type. You can use
825    /// `compare_exchange(...).unwrap_or_else(|x| x)` to recover the behavior of `compare_and_swap`,
826    /// but in most cases it is more idiomatic to check whether the return value is `Ok` or `Err`
827    /// rather than to infer success vs failure based on the value that was read.
828    ///
829    /// During migration, consider whether it makes sense to use `compare_exchange_weak` instead.
830    /// `compare_exchange_weak` is allowed to fail spuriously even when the comparison succeeds,
831    /// which allows the compiler to generate better assembly code when the compare and swap
832    /// is used in a loop.
833    ///
834    /// # Examples
835    ///
836    /// ```
837    /// use std::sync::atomic::{AtomicBool, Ordering};
838    ///
839    /// let some_bool = AtomicBool::new(true);
840    ///
841    /// assert_eq!(some_bool.compare_and_swap(true, false, Ordering::Relaxed), true);
842    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
843    ///
844    /// assert_eq!(some_bool.compare_and_swap(true, true, Ordering::Relaxed), false);
845    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
846    /// ```
847    #[inline]
848    #[stable(feature = "rust1", since = "1.0.0")]
849    #[deprecated(
850        since = "1.50.0",
851        note = "Use `compare_exchange` or `compare_exchange_weak` instead"
852    )]
853    #[cfg(target_has_atomic = "8")]
854    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
855    #[rustc_should_not_be_called_on_const_items]
856    pub fn compare_and_swap(&self, current: bool, new: bool, order: Ordering) -> bool {
857        match self.compare_exchange(current, new, order, strongest_failure_ordering(order)) {
858            Ok(x) => x,
859            Err(x) => x,
860        }
861    }
862
863    /// Stores a value into the [`bool`] if the current value is the same as the `current` value.
864    ///
865    /// The return value is a result indicating whether the new value was written and containing
866    /// the previous value. On success this value is guaranteed to be equal to `current`.
867    ///
868    /// `compare_exchange` takes two [`Ordering`] arguments to describe the memory
869    /// ordering of this operation. `success` describes the required ordering for the
870    /// read-modify-write operation that takes place if the comparison with `current` succeeds.
871    /// `failure` describes the required ordering for the load operation that takes place when
872    /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
873    /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
874    /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
875    ///
876    /// **Note:** This method is only available on platforms that support atomic
877    /// operations on `u8`.
878    ///
879    /// # Examples
880    ///
881    /// ```
882    /// use std::sync::atomic::{AtomicBool, Ordering};
883    ///
884    /// let some_bool = AtomicBool::new(true);
885    ///
886    /// assert_eq!(some_bool.compare_exchange(true,
887    ///                                       false,
888    ///                                       Ordering::Acquire,
889    ///                                       Ordering::Relaxed),
890    ///            Ok(true));
891    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
892    ///
893    /// assert_eq!(some_bool.compare_exchange(true, true,
894    ///                                       Ordering::SeqCst,
895    ///                                       Ordering::Acquire),
896    ///            Err(false));
897    /// assert_eq!(some_bool.load(Ordering::Relaxed), false);
898    /// ```
899    ///
900    /// # Considerations
901    ///
902    /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
903    /// of CAS operations. In particular, a load of the value followed by a successful
904    /// `compare_exchange` with the previous load *does not ensure* that other threads have not
905    /// changed the value in the interim. This is usually important when the *equality* check in
906    /// the `compare_exchange` is being used to check the *identity* of a value, but equality
907    /// does not necessarily imply identity. In this case, `compare_exchange` can lead to the
908    /// [ABA problem].
909    ///
910    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
911    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
912    #[inline]
913    #[stable(feature = "extended_compare_and_swap", since = "1.10.0")]
914    #[doc(alias = "compare_and_swap")]
915    #[cfg(target_has_atomic = "8")]
916    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
917    #[rustc_should_not_be_called_on_const_items]
918    pub fn compare_exchange(
919        &self,
920        current: bool,
921        new: bool,
922        success: Ordering,
923        failure: Ordering,
924    ) -> Result<bool, bool> {
925        if EMULATE_ATOMIC_BOOL {
926            // Pick the strongest ordering from success and failure.
927            let order = match (success, failure) {
928                (SeqCst, _) => SeqCst,
929                (_, SeqCst) => SeqCst,
930                (AcqRel, _) => AcqRel,
931                (_, AcqRel) => {
932                    panic!("there is no such thing as an acquire-release failure ordering")
933                }
934                (Release, Acquire) => AcqRel,
935                (Acquire, _) => Acquire,
936                (_, Acquire) => Acquire,
937                (Release, Relaxed) => Release,
938                (_, Release) => panic!("there is no such thing as a release failure ordering"),
939                (Relaxed, Relaxed) => Relaxed,
940            };
941            let old = if current == new {
942                // This is a no-op, but we still need to perform the operation
943                // for memory ordering reasons.
944                self.fetch_or(false, order)
945            } else {
946                // This sets the value to the new one and returns the old one.
947                self.swap(new, order)
948            };
949            if old == current { Ok(old) } else { Err(old) }
950        } else {
951            // SAFETY: data races are prevented by atomic intrinsics.
952            match unsafe {
953                atomic_compare_exchange(self.v.get(), current as u8, new as u8, success, failure)
954            } {
955                Ok(x) => Ok(x != 0),
956                Err(x) => Err(x != 0),
957            }
958        }
959    }
960
961    /// Stores a value into the [`bool`] if the current value is the same as the `current` value.
962    ///
963    /// Unlike [`AtomicBool::compare_exchange`], this function is allowed to spuriously fail even when the
964    /// comparison succeeds, which can result in more efficient code on some platforms. The
965    /// return value is a result indicating whether the new value was written and containing the
966    /// previous value.
967    ///
968    /// `compare_exchange_weak` takes two [`Ordering`] arguments to describe the memory
969    /// ordering of this operation. `success` describes the required ordering for the
970    /// read-modify-write operation that takes place if the comparison with `current` succeeds.
971    /// `failure` describes the required ordering for the load operation that takes place when
972    /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
973    /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
974    /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
975    ///
976    /// **Note:** This method is only available on platforms that support atomic
977    /// operations on `u8`.
978    ///
979    /// # Examples
980    ///
981    /// ```
982    /// use std::sync::atomic::{AtomicBool, Ordering};
983    ///
984    /// let val = AtomicBool::new(false);
985    ///
986    /// let new = true;
987    /// let mut old = val.load(Ordering::Relaxed);
988    /// loop {
989    ///     match val.compare_exchange_weak(old, new, Ordering::SeqCst, Ordering::Relaxed) {
990    ///         Ok(_) => break,
991    ///         Err(x) => old = x,
992    ///     }
993    /// }
994    /// ```
995    ///
996    /// # Considerations
997    ///
998    /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
999    /// of CAS operations. In particular, a load of the value followed by a successful
1000    /// `compare_exchange` with the previous load *does not ensure* that other threads have not
1001    /// changed the value in the interim. This is usually important when the *equality* check in
1002    /// the `compare_exchange` is being used to check the *identity* of a value, but equality
1003    /// does not necessarily imply identity. In this case, `compare_exchange` can lead to the
1004    /// [ABA problem].
1005    ///
1006    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
1007    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
1008    #[inline]
1009    #[stable(feature = "extended_compare_and_swap", since = "1.10.0")]
1010    #[doc(alias = "compare_and_swap")]
1011    #[cfg(target_has_atomic = "8")]
1012    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1013    #[rustc_should_not_be_called_on_const_items]
1014    pub fn compare_exchange_weak(
1015        &self,
1016        current: bool,
1017        new: bool,
1018        success: Ordering,
1019        failure: Ordering,
1020    ) -> Result<bool, bool> {
1021        if EMULATE_ATOMIC_BOOL {
1022            return self.compare_exchange(current, new, success, failure);
1023        }
1024
1025        // SAFETY: data races are prevented by atomic intrinsics.
1026        match unsafe {
1027            atomic_compare_exchange_weak(self.v.get(), current as u8, new as u8, success, failure)
1028        } {
1029            Ok(x) => Ok(x != 0),
1030            Err(x) => Err(x != 0),
1031        }
1032    }
1033
1034    /// Logical "and" with a boolean value.
1035    ///
1036    /// Performs a logical "and" operation on the current value and the argument `val`, and sets
1037    /// the new value to the result.
1038    ///
1039    /// Returns the previous value.
1040    ///
1041    /// `fetch_and` takes an [`Ordering`] argument which describes the memory ordering
1042    /// of this operation. All ordering modes are possible. Note that using
1043    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1044    /// using [`Release`] makes the load part [`Relaxed`].
1045    ///
1046    /// **Note:** This method is only available on platforms that support atomic
1047    /// operations on `u8`.
1048    ///
1049    /// # Examples
1050    ///
1051    /// ```
1052    /// use std::sync::atomic::{AtomicBool, Ordering};
1053    ///
1054    /// let foo = AtomicBool::new(true);
1055    /// assert_eq!(foo.fetch_and(false, Ordering::SeqCst), true);
1056    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1057    ///
1058    /// let foo = AtomicBool::new(true);
1059    /// assert_eq!(foo.fetch_and(true, Ordering::SeqCst), true);
1060    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1061    ///
1062    /// let foo = AtomicBool::new(false);
1063    /// assert_eq!(foo.fetch_and(false, Ordering::SeqCst), false);
1064    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1065    /// ```
1066    #[inline]
1067    #[stable(feature = "rust1", since = "1.0.0")]
1068    #[cfg(target_has_atomic = "8")]
1069    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1070    #[rustc_should_not_be_called_on_const_items]
1071    pub fn fetch_and(&self, val: bool, order: Ordering) -> bool {
1072        // SAFETY: data races are prevented by atomic intrinsics.
1073        unsafe { atomic_and(self.v.get(), val as u8, order) != 0 }
1074    }
1075
1076    /// Logical "nand" with a boolean value.
1077    ///
1078    /// Performs a logical "nand" operation on the current value and the argument `val`, and sets
1079    /// the new value to the result.
1080    ///
1081    /// Returns the previous value.
1082    ///
1083    /// `fetch_nand` takes an [`Ordering`] argument which describes the memory ordering
1084    /// of this operation. All ordering modes are possible. Note that using
1085    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1086    /// using [`Release`] makes the load part [`Relaxed`].
1087    ///
1088    /// **Note:** This method is only available on platforms that support atomic
1089    /// operations on `u8`.
1090    ///
1091    /// # Examples
1092    ///
1093    /// ```
1094    /// use std::sync::atomic::{AtomicBool, Ordering};
1095    ///
1096    /// let foo = AtomicBool::new(true);
1097    /// assert_eq!(foo.fetch_nand(false, Ordering::SeqCst), true);
1098    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1099    ///
1100    /// let foo = AtomicBool::new(true);
1101    /// assert_eq!(foo.fetch_nand(true, Ordering::SeqCst), true);
1102    /// assert_eq!(foo.load(Ordering::SeqCst) as usize, 0);
1103    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1104    ///
1105    /// let foo = AtomicBool::new(false);
1106    /// assert_eq!(foo.fetch_nand(false, Ordering::SeqCst), false);
1107    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1108    /// ```
1109    #[inline]
1110    #[stable(feature = "rust1", since = "1.0.0")]
1111    #[cfg(target_has_atomic = "8")]
1112    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1113    #[rustc_should_not_be_called_on_const_items]
1114    pub fn fetch_nand(&self, val: bool, order: Ordering) -> bool {
1115        // We can't use atomic_nand here because it can result in a bool with
1116        // an invalid value. This happens because the atomic operation is done
1117        // with an 8-bit integer internally, which would set the upper 7 bits.
1118        // So we just use fetch_xor or swap instead.
1119        if val {
1120            // !(x & true) == !x
1121            // We must invert the bool.
1122            self.fetch_xor(true, order)
1123        } else {
1124            // !(x & false) == true
1125            // We must set the bool to true.
1126            self.swap(true, order)
1127        }
1128    }
1129
1130    /// Logical "or" with a boolean value.
1131    ///
1132    /// Performs a logical "or" operation on the current value and the argument `val`, and sets the
1133    /// new value to the result.
1134    ///
1135    /// Returns the previous value.
1136    ///
1137    /// `fetch_or` takes an [`Ordering`] argument which describes the memory ordering
1138    /// of this operation. All ordering modes are possible. Note that using
1139    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1140    /// using [`Release`] makes the load part [`Relaxed`].
1141    ///
1142    /// **Note:** This method is only available on platforms that support atomic
1143    /// operations on `u8`.
1144    ///
1145    /// # Examples
1146    ///
1147    /// ```
1148    /// use std::sync::atomic::{AtomicBool, Ordering};
1149    ///
1150    /// let foo = AtomicBool::new(true);
1151    /// assert_eq!(foo.fetch_or(false, Ordering::SeqCst), true);
1152    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1153    ///
1154    /// let foo = AtomicBool::new(false);
1155    /// assert_eq!(foo.fetch_or(true, Ordering::SeqCst), false);
1156    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1157    ///
1158    /// let foo = AtomicBool::new(false);
1159    /// assert_eq!(foo.fetch_or(false, Ordering::SeqCst), false);
1160    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1161    /// ```
1162    #[inline]
1163    #[stable(feature = "rust1", since = "1.0.0")]
1164    #[cfg(target_has_atomic = "8")]
1165    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1166    #[rustc_should_not_be_called_on_const_items]
1167    pub fn fetch_or(&self, val: bool, order: Ordering) -> bool {
1168        // SAFETY: data races are prevented by atomic intrinsics.
1169        unsafe { atomic_or(self.v.get(), val as u8, order) != 0 }
1170    }
1171
1172    /// Logical "xor" with a boolean value.
1173    ///
1174    /// Performs a logical "xor" operation on the current value and the argument `val`, and sets
1175    /// the new value to the result.
1176    ///
1177    /// Returns the previous value.
1178    ///
1179    /// `fetch_xor` takes an [`Ordering`] argument which describes the memory ordering
1180    /// of this operation. All ordering modes are possible. Note that using
1181    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1182    /// using [`Release`] makes the load part [`Relaxed`].
1183    ///
1184    /// **Note:** This method is only available on platforms that support atomic
1185    /// operations on `u8`.
1186    ///
1187    /// # Examples
1188    ///
1189    /// ```
1190    /// use std::sync::atomic::{AtomicBool, Ordering};
1191    ///
1192    /// let foo = AtomicBool::new(true);
1193    /// assert_eq!(foo.fetch_xor(false, Ordering::SeqCst), true);
1194    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1195    ///
1196    /// let foo = AtomicBool::new(true);
1197    /// assert_eq!(foo.fetch_xor(true, Ordering::SeqCst), true);
1198    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1199    ///
1200    /// let foo = AtomicBool::new(false);
1201    /// assert_eq!(foo.fetch_xor(false, Ordering::SeqCst), false);
1202    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1203    /// ```
1204    #[inline]
1205    #[stable(feature = "rust1", since = "1.0.0")]
1206    #[cfg(target_has_atomic = "8")]
1207    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1208    #[rustc_should_not_be_called_on_const_items]
1209    pub fn fetch_xor(&self, val: bool, order: Ordering) -> bool {
1210        // SAFETY: data races are prevented by atomic intrinsics.
1211        unsafe { atomic_xor(self.v.get(), val as u8, order) != 0 }
1212    }
1213
1214    /// Logical "not" with a boolean value.
1215    ///
1216    /// Performs a logical "not" operation on the current value, and sets
1217    /// the new value to the result.
1218    ///
1219    /// Returns the previous value.
1220    ///
1221    /// `fetch_not` takes an [`Ordering`] argument which describes the memory ordering
1222    /// of this operation. All ordering modes are possible. Note that using
1223    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1224    /// using [`Release`] makes the load part [`Relaxed`].
1225    ///
1226    /// **Note:** This method is only available on platforms that support atomic
1227    /// operations on `u8`.
1228    ///
1229    /// # Examples
1230    ///
1231    /// ```
1232    /// use std::sync::atomic::{AtomicBool, Ordering};
1233    ///
1234    /// let foo = AtomicBool::new(true);
1235    /// assert_eq!(foo.fetch_not(Ordering::SeqCst), true);
1236    /// assert_eq!(foo.load(Ordering::SeqCst), false);
1237    ///
1238    /// let foo = AtomicBool::new(false);
1239    /// assert_eq!(foo.fetch_not(Ordering::SeqCst), false);
1240    /// assert_eq!(foo.load(Ordering::SeqCst), true);
1241    /// ```
1242    #[inline]
1243    #[stable(feature = "atomic_bool_fetch_not", since = "1.81.0")]
1244    #[cfg(target_has_atomic = "8")]
1245    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1246    #[rustc_should_not_be_called_on_const_items]
1247    pub fn fetch_not(&self, order: Ordering) -> bool {
1248        self.fetch_xor(true, order)
1249    }
1250
1251    /// Returns a mutable pointer to the underlying [`bool`].
1252    ///
1253    /// Doing non-atomic reads and writes on the resulting boolean can be a data race.
1254    /// This method is mostly useful for FFI, where the function signature may use
1255    /// `*mut bool` instead of `&AtomicBool`.
1256    ///
1257    /// Returning an `*mut` pointer from a shared reference to this atomic is safe because the
1258    /// atomic types work with interior mutability. All modifications of an atomic change the value
1259    /// through a shared reference, and can do so safely as long as they use atomic operations. Any
1260    /// use of the returned raw pointer requires an `unsafe` block and still has to uphold the
1261    /// requirements of the [memory model].
1262    ///
1263    /// # Examples
1264    ///
1265    /// ```ignore (extern-declaration)
1266    /// # fn main() {
1267    /// use std::sync::atomic::AtomicBool;
1268    ///
1269    /// extern "C" {
1270    ///     fn my_atomic_op(arg: *mut bool);
1271    /// }
1272    ///
1273    /// let mut atomic = AtomicBool::new(true);
1274    /// unsafe {
1275    ///     my_atomic_op(atomic.as_ptr());
1276    /// }
1277    /// # }
1278    /// ```
1279    ///
1280    /// [memory model]: self#memory-model-for-atomic-accesses
1281    #[inline]
1282    #[stable(feature = "atomic_as_ptr", since = "1.70.0")]
1283    #[rustc_const_stable(feature = "atomic_as_ptr", since = "1.70.0")]
1284    #[rustc_never_returns_null_ptr]
1285    #[rustc_should_not_be_called_on_const_items]
1286    pub const fn as_ptr(&self) -> *mut bool {
1287        self.v.get().cast()
1288    }
1289
1290    /// An alias for [`AtomicBool::try_update`].
1291    #[inline]
1292    #[stable(feature = "atomic_fetch_update", since = "1.53.0")]
1293    #[cfg(target_has_atomic = "8")]
1294    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1295    #[rustc_should_not_be_called_on_const_items]
1296    #[deprecated(
1297        since = "1.99.0",
1298        note = "renamed to `try_update` for consistency",
1299        suggestion = "try_update"
1300    )]
1301    pub fn fetch_update<F>(
1302        &self,
1303        set_order: Ordering,
1304        fetch_order: Ordering,
1305        f: F,
1306    ) -> Result<bool, bool>
1307    where
1308        F: FnMut(bool) -> Option<bool>,
1309    {
1310        self.try_update(set_order, fetch_order, f)
1311    }
1312
1313    /// Fetches the value, and applies a function to it that returns an optional
1314    /// new value. Returns a `Result` of `Ok(previous_value)` if the function
1315    /// returned `Some(_)`, else `Err(previous_value)`.
1316    ///
1317    /// See also: [`update`](`AtomicBool::update`).
1318    ///
1319    /// Note: This may call the function multiple times if the value has been
1320    /// changed from other threads in the meantime, as long as the function
1321    /// returns `Some(_)`, but the function will have been applied only once to
1322    /// the stored value.
1323    ///
1324    /// `try_update` takes two [`Ordering`] arguments to describe the memory
1325    /// ordering of this operation. The first describes the required ordering for
1326    /// when the operation finally succeeds while the second describes the
1327    /// required ordering for loads. These correspond to the success and failure
1328    /// orderings of [`AtomicBool::compare_exchange`] respectively.
1329    ///
1330    /// Using [`Acquire`] as success ordering makes the store part of this
1331    /// operation [`Relaxed`], and using [`Release`] makes the final successful
1332    /// load [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`],
1333    /// [`Acquire`] or [`Relaxed`].
1334    ///
1335    /// **Note:** This method is only available on platforms that support atomic
1336    /// operations on `u8`.
1337    ///
1338    /// # Considerations
1339    ///
1340    /// This method is not magic; it is not provided by the hardware, and does not act like a
1341    /// critical section or mutex.
1342    ///
1343    /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
1344    /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem].
1345    ///
1346    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
1347    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
1348    ///
1349    /// # Examples
1350    ///
1351    /// ```rust
1352    /// use std::sync::atomic::{AtomicBool, Ordering};
1353    ///
1354    /// let x = AtomicBool::new(false);
1355    /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |_| None), Err(false));
1356    /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(!x)), Ok(false));
1357    /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(!x)), Ok(true));
1358    /// assert_eq!(x.load(Ordering::SeqCst), false);
1359    /// ```
1360    #[inline]
1361    #[stable(feature = "atomic_try_update", since = "1.95.0")]
1362    #[cfg(target_has_atomic = "8")]
1363    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1364    #[rustc_should_not_be_called_on_const_items]
1365    pub fn try_update(
1366        &self,
1367        set_order: Ordering,
1368        fetch_order: Ordering,
1369        mut f: impl FnMut(bool) -> Option<bool>,
1370    ) -> Result<bool, bool> {
1371        let mut prev = self.load(fetch_order);
1372        while let Some(next) = f(prev) {
1373            match self.compare_exchange_weak(prev, next, set_order, fetch_order) {
1374                x @ Ok(_) => return x,
1375                Err(next_prev) => prev = next_prev,
1376            }
1377        }
1378        Err(prev)
1379    }
1380
1381    /// Fetches the value, applies a function to it that it return a new value.
1382    /// The new value is stored and the old value is returned.
1383    ///
1384    /// See also: [`try_update`](`AtomicBool::try_update`).
1385    ///
1386    /// Note: This may call the function multiple times if the value has been changed from other threads in
1387    /// the meantime, but the function will have been applied only once to the stored value.
1388    ///
1389    /// `update` takes two [`Ordering`] arguments to describe the memory
1390    /// ordering of this operation. The first describes the required ordering for
1391    /// when the operation finally succeeds while the second describes the
1392    /// required ordering for loads. These correspond to the success and failure
1393    /// orderings of [`AtomicBool::compare_exchange`] respectively.
1394    ///
1395    /// Using [`Acquire`] as success ordering makes the store part
1396    /// of this operation [`Relaxed`], and using [`Release`] makes the final successful load
1397    /// [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
1398    ///
1399    /// **Note:** This method is only available on platforms that support atomic operations on `u8`.
1400    ///
1401    /// # Considerations
1402    ///
1403    /// This method is not magic; it is not provided by the hardware, and does not act like a
1404    /// critical section or mutex.
1405    ///
1406    /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
1407    /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem].
1408    ///
1409    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
1410    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
1411    ///
1412    /// # Examples
1413    ///
1414    /// ```rust
1415    ///
1416    /// use std::sync::atomic::{AtomicBool, Ordering};
1417    ///
1418    /// let x = AtomicBool::new(false);
1419    /// assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| !x), false);
1420    /// assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| !x), true);
1421    /// assert_eq!(x.load(Ordering::SeqCst), false);
1422    /// ```
1423    #[inline]
1424    #[stable(feature = "atomic_try_update", since = "1.95.0")]
1425    #[cfg(target_has_atomic = "8")]
1426    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1427    #[rustc_should_not_be_called_on_const_items]
1428    pub fn update(
1429        &self,
1430        set_order: Ordering,
1431        fetch_order: Ordering,
1432        mut f: impl FnMut(bool) -> bool,
1433    ) -> bool {
1434        let mut prev = self.load(fetch_order);
1435        loop {
1436            match self.compare_exchange_weak(prev, f(prev), set_order, fetch_order) {
1437                Ok(x) => break x,
1438                Err(next_prev) => prev = next_prev,
1439            }
1440        }
1441    }
1442}
1443
1444#[cfg(target_has_atomic_load_store = "ptr")]
1445impl<T> AtomicPtr<T> {
1446    /// Creates a new `AtomicPtr`.
1447    ///
1448    /// # Examples
1449    ///
1450    /// ```
1451    /// use std::sync::atomic::AtomicPtr;
1452    ///
1453    /// let ptr = &mut 5;
1454    /// let atomic_ptr = AtomicPtr::new(ptr);
1455    /// ```
1456    #[inline]
1457    #[stable(feature = "rust1", since = "1.0.0")]
1458    #[rustc_const_stable(feature = "const_atomic_new", since = "1.24.0")]
1459    pub const fn new(p: *mut T) -> AtomicPtr<T> {
1460        AtomicPtr { p: UnsafeCell::new(p) }
1461    }
1462
1463    /// Creates a new `AtomicPtr` from a pointer.
1464    ///
1465    /// # Examples
1466    ///
1467    /// ```
1468    /// use std::sync::atomic::{self, AtomicPtr};
1469    ///
1470    /// // Get a pointer to an allocated value
1471    /// let ptr: *mut *mut u8 = Box::into_raw(Box::new(std::ptr::null_mut()));
1472    ///
1473    /// assert!(ptr.cast::<AtomicPtr<u8>>().is_aligned());
1474    ///
1475    /// {
1476    ///     // Create an atomic view of the allocated value
1477    ///     let atomic = unsafe { AtomicPtr::from_ptr(ptr) };
1478    ///
1479    ///     // Use `atomic` for atomic operations, possibly share it with other threads
1480    ///     atomic.store(std::ptr::NonNull::dangling().as_ptr(), atomic::Ordering::Relaxed);
1481    /// }
1482    ///
1483    /// // It's ok to non-atomically access the value behind `ptr`,
1484    /// // since the reference to the atomic ended its lifetime in the block above
1485    /// assert!(!unsafe { *ptr }.is_null());
1486    ///
1487    /// // Deallocate the value
1488    /// unsafe { drop(Box::from_raw(ptr)) }
1489    /// ```
1490    ///
1491    /// # Safety
1492    ///
1493    /// * `ptr` must be aligned to `align_of::<AtomicPtr<T>>()` (note that on some platforms this
1494    ///   can be bigger than `align_of::<*mut T>()`).
1495    /// * `ptr` must be [valid] for both reads and writes for the whole lifetime `'a`.
1496    /// * You must adhere to the [Memory model for atomic accesses]. In particular, it is not
1497    ///   allowed to mix conflicting atomic and non-atomic accesses, or atomic accesses of different
1498    ///   sizes, without synchronization.
1499    ///
1500    /// [valid]: crate::ptr#safety
1501    /// [Memory model for atomic accesses]: self#memory-model-for-atomic-accesses
1502    #[inline]
1503    #[stable(feature = "atomic_from_ptr", since = "1.75.0")]
1504    #[rustc_const_stable(feature = "const_atomic_from_ptr", since = "1.84.0")]
1505    pub const unsafe fn from_ptr<'a>(ptr: *mut *mut T) -> &'a AtomicPtr<T> {
1506        // SAFETY: guaranteed by the caller
1507        unsafe { &*ptr.cast() }
1508    }
1509
1510    /// Creates a new `AtomicPtr` initialized with a null pointer.
1511    ///
1512    /// # Examples
1513    ///
1514    /// ```
1515    /// #![feature(atomic_ptr_null)]
1516    /// use std::sync::atomic::{AtomicPtr, Ordering};
1517    ///
1518    /// let atomic_ptr = AtomicPtr::<()>::null();
1519    /// assert!(atomic_ptr.load(Ordering::Relaxed).is_null());
1520    /// ```
1521    #[inline]
1522    #[must_use]
1523    #[unstable(feature = "atomic_ptr_null", issue = "150733")]
1524    pub const fn null() -> AtomicPtr<T> {
1525        AtomicPtr::new(crate::ptr::null_mut())
1526    }
1527
1528    /// Returns a mutable reference to the underlying pointer.
1529    ///
1530    /// This is safe because the mutable reference guarantees that no other threads are
1531    /// concurrently accessing the atomic data.
1532    ///
1533    /// # Examples
1534    ///
1535    /// ```
1536    /// use std::sync::atomic::{AtomicPtr, Ordering};
1537    ///
1538    /// let mut data = 10;
1539    /// let mut atomic_ptr = AtomicPtr::new(&mut data);
1540    /// let mut other_data = 5;
1541    /// *atomic_ptr.get_mut() = &mut other_data;
1542    /// assert_eq!(unsafe { *atomic_ptr.load(Ordering::SeqCst) }, 5);
1543    /// ```
1544    #[inline]
1545    #[stable(feature = "atomic_access", since = "1.15.0")]
1546    pub fn get_mut(&mut self) -> &mut *mut T {
1547        self.p.get_mut()
1548    }
1549
1550    /// Gets atomic access to a pointer.
1551    ///
1552    /// **Note:** This function is only available on targets where `AtomicPtr<T>` has the same alignment as `*const T`
1553    ///
1554    /// # Examples
1555    ///
1556    /// ```
1557    /// #![feature(atomic_from_mut)]
1558    /// use std::sync::atomic::{AtomicPtr, Ordering};
1559    ///
1560    /// let mut data = 123;
1561    /// let mut some_ptr = &mut data as *mut i32;
1562    /// let a = AtomicPtr::from_mut(&mut some_ptr);
1563    /// let mut other_data = 456;
1564    /// a.store(&mut other_data, Ordering::Relaxed);
1565    /// assert_eq!(unsafe { *some_ptr }, 456);
1566    /// ```
1567    #[inline]
1568    #[cfg(target_has_atomic_equal_alignment = "ptr")]
1569    #[unstable(feature = "atomic_from_mut", issue = "76314")]
1570    pub fn from_mut(v: &mut *mut T) -> &mut Self {
1571        let [] = [(); align_of::<AtomicPtr<()>>() - align_of::<*mut ()>()];
1572        // SAFETY:
1573        //  - the mutable reference guarantees unique ownership.
1574        //  - the alignment of `*mut T` and `Self` is the same on all platforms
1575        //    supported by rust, as verified above.
1576        unsafe { &mut *(v as *mut *mut T as *mut Self) }
1577    }
1578
1579    /// Gets non-atomic access to a `&mut [AtomicPtr]` slice.
1580    ///
1581    /// This is safe because the mutable reference guarantees that no other threads are
1582    /// concurrently accessing the atomic data.
1583    ///
1584    /// # Examples
1585    ///
1586    /// ```ignore-wasm
1587    /// #![feature(atomic_from_mut)]
1588    /// use std::ptr::null_mut;
1589    /// use std::sync::atomic::{AtomicPtr, Ordering};
1590    ///
1591    /// let mut some_ptrs = [const { AtomicPtr::new(null_mut::<String>()) }; 10];
1592    ///
1593    /// let view: &mut [*mut String] = AtomicPtr::get_mut_slice(&mut some_ptrs);
1594    /// assert_eq!(view, [null_mut::<String>(); 10]);
1595    /// view
1596    ///     .iter_mut()
1597    ///     .enumerate()
1598    ///     .for_each(|(i, ptr)| *ptr = Box::into_raw(Box::new(format!("iteration#{i}"))));
1599    ///
1600    /// std::thread::scope(|s| {
1601    ///     for ptr in &some_ptrs {
1602    ///         s.spawn(move || {
1603    ///             let ptr = ptr.load(Ordering::Relaxed);
1604    ///             assert!(!ptr.is_null());
1605    ///
1606    ///             let name = unsafe { Box::from_raw(ptr) };
1607    ///             println!("Hello, {name}!");
1608    ///         });
1609    ///     }
1610    /// });
1611    /// ```
1612    #[inline]
1613    #[unstable(feature = "atomic_from_mut", issue = "76314")]
1614    pub fn get_mut_slice(this: &mut [Self]) -> &mut [*mut T] {
1615        // SAFETY: the mutable reference guarantees unique ownership.
1616        unsafe { &mut *(this as *mut [Self] as *mut [*mut T]) }
1617    }
1618
1619    /// Gets atomic access to a slice of pointers.
1620    ///
1621    /// **Note:** This function is only available on targets where `AtomicPtr<T>` has the same alignment as `*const T`
1622    ///
1623    /// # Examples
1624    ///
1625    /// ```ignore-wasm
1626    /// #![feature(atomic_from_mut)]
1627    /// use std::ptr::null_mut;
1628    /// use std::sync::atomic::{AtomicPtr, Ordering};
1629    ///
1630    /// let mut some_ptrs = [null_mut::<String>(); 10];
1631    /// let a = &*AtomicPtr::from_mut_slice(&mut some_ptrs);
1632    /// std::thread::scope(|s| {
1633    ///     for i in 0..a.len() {
1634    ///         s.spawn(move || {
1635    ///             let name = Box::new(format!("thread{i}"));
1636    ///             a[i].store(Box::into_raw(name), Ordering::Relaxed);
1637    ///         });
1638    ///     }
1639    /// });
1640    /// for p in some_ptrs {
1641    ///     assert!(!p.is_null());
1642    ///     let name = unsafe { Box::from_raw(p) };
1643    ///     println!("Hello, {name}!");
1644    /// }
1645    /// ```
1646    #[inline]
1647    #[cfg(target_has_atomic_equal_alignment = "ptr")]
1648    #[unstable(feature = "atomic_from_mut", issue = "76314")]
1649    pub fn from_mut_slice(v: &mut [*mut T]) -> &mut [Self] {
1650        // SAFETY:
1651        //  - the mutable reference guarantees unique ownership.
1652        //  - the alignment of `*mut T` and `Self` is the same on all platforms
1653        //    supported by rust, as verified above.
1654        unsafe { &mut *(v as *mut [*mut T] as *mut [Self]) }
1655    }
1656
1657    /// Consumes the atomic and returns the contained value.
1658    ///
1659    /// This is safe because passing `self` by value guarantees that no other threads are
1660    /// concurrently accessing the atomic data.
1661    ///
1662    /// # Examples
1663    ///
1664    /// ```
1665    /// use std::sync::atomic::AtomicPtr;
1666    ///
1667    /// let mut data = 5;
1668    /// let atomic_ptr = AtomicPtr::new(&mut data);
1669    /// assert_eq!(unsafe { *atomic_ptr.into_inner() }, 5);
1670    /// ```
1671    #[inline]
1672    #[stable(feature = "atomic_access", since = "1.15.0")]
1673    #[rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0")]
1674    pub const fn into_inner(self) -> *mut T {
1675        self.p.into_inner()
1676    }
1677
1678    /// Loads a value from the pointer.
1679    ///
1680    /// `load` takes an [`Ordering`] argument which describes the memory ordering
1681    /// of this operation. Possible values are [`SeqCst`], [`Acquire`] and [`Relaxed`].
1682    ///
1683    /// # Panics
1684    ///
1685    /// Panics if `order` is [`Release`] or [`AcqRel`].
1686    ///
1687    /// # Examples
1688    ///
1689    /// ```
1690    /// use std::sync::atomic::{AtomicPtr, Ordering};
1691    ///
1692    /// let ptr = &mut 5;
1693    /// let some_ptr = AtomicPtr::new(ptr);
1694    ///
1695    /// let value = some_ptr.load(Ordering::Relaxed);
1696    /// ```
1697    #[inline]
1698    #[stable(feature = "rust1", since = "1.0.0")]
1699    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1700    pub fn load(&self, order: Ordering) -> *mut T {
1701        // SAFETY: data races are prevented by atomic intrinsics.
1702        unsafe { atomic_load(self.p.get(), order) }
1703    }
1704
1705    /// Stores a value into the pointer.
1706    ///
1707    /// `store` takes an [`Ordering`] argument which describes the memory ordering
1708    /// of this operation. Possible values are [`SeqCst`], [`Release`] and [`Relaxed`].
1709    ///
1710    /// # Panics
1711    ///
1712    /// Panics if `order` is [`Acquire`] or [`AcqRel`].
1713    ///
1714    /// # Examples
1715    ///
1716    /// ```
1717    /// use std::sync::atomic::{AtomicPtr, Ordering};
1718    ///
1719    /// let ptr = &mut 5;
1720    /// let some_ptr = AtomicPtr::new(ptr);
1721    ///
1722    /// let other_ptr = &mut 10;
1723    ///
1724    /// some_ptr.store(other_ptr, Ordering::Relaxed);
1725    /// ```
1726    #[inline]
1727    #[stable(feature = "rust1", since = "1.0.0")]
1728    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1729    #[rustc_should_not_be_called_on_const_items]
1730    pub fn store(&self, ptr: *mut T, order: Ordering) {
1731        // SAFETY: data races are prevented by atomic intrinsics.
1732        unsafe {
1733            atomic_store(self.p.get(), ptr, order);
1734        }
1735    }
1736
1737    /// Stores a value into the pointer, returning the previous value.
1738    ///
1739    /// `swap` takes an [`Ordering`] argument which describes the memory ordering
1740    /// of this operation. All ordering modes are possible. Note that using
1741    /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
1742    /// using [`Release`] makes the load part [`Relaxed`].
1743    ///
1744    /// **Note:** This method is only available on platforms that support atomic
1745    /// operations on pointers.
1746    ///
1747    /// # Examples
1748    ///
1749    /// ```
1750    /// use std::sync::atomic::{AtomicPtr, Ordering};
1751    ///
1752    /// let ptr = &mut 5;
1753    /// let some_ptr = AtomicPtr::new(ptr);
1754    ///
1755    /// let other_ptr = &mut 10;
1756    ///
1757    /// let value = some_ptr.swap(other_ptr, Ordering::Relaxed);
1758    /// ```
1759    #[inline]
1760    #[stable(feature = "rust1", since = "1.0.0")]
1761    #[cfg(target_has_atomic = "ptr")]
1762    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1763    #[rustc_should_not_be_called_on_const_items]
1764    pub fn swap(&self, ptr: *mut T, order: Ordering) -> *mut T {
1765        // SAFETY: data races are prevented by atomic intrinsics.
1766        unsafe { atomic_swap(self.p.get(), ptr, order) }
1767    }
1768
1769    /// Stores a value into the pointer if the current value is the same as the `current` value.
1770    ///
1771    /// The return value is always the previous value. If it is equal to `current`, then the value
1772    /// was updated.
1773    ///
1774    /// `compare_and_swap` also takes an [`Ordering`] argument which describes the memory
1775    /// ordering of this operation. Notice that even when using [`AcqRel`], the operation
1776    /// might fail and hence just perform an `Acquire` load, but not have `Release` semantics.
1777    /// Using [`Acquire`] makes the store part of this operation [`Relaxed`] if it
1778    /// happens, and using [`Release`] makes the load part [`Relaxed`].
1779    ///
1780    /// **Note:** This method is only available on platforms that support atomic
1781    /// operations on pointers.
1782    ///
1783    /// # Migrating to `compare_exchange` and `compare_exchange_weak`
1784    ///
1785    /// `compare_and_swap` is equivalent to `compare_exchange` with the following mapping for
1786    /// memory orderings:
1787    ///
1788    /// Original | Success | Failure
1789    /// -------- | ------- | -------
1790    /// Relaxed  | Relaxed | Relaxed
1791    /// Acquire  | Acquire | Acquire
1792    /// Release  | Release | Relaxed
1793    /// AcqRel   | AcqRel  | Acquire
1794    /// SeqCst   | SeqCst  | SeqCst
1795    ///
1796    /// `compare_and_swap` and `compare_exchange` also differ in their return type. You can use
1797    /// `compare_exchange(...).unwrap_or_else(|x| x)` to recover the behavior of `compare_and_swap`,
1798    /// but in most cases it is more idiomatic to check whether the return value is `Ok` or `Err`
1799    /// rather than to infer success vs failure based on the value that was read.
1800    ///
1801    /// During migration, consider whether it makes sense to use `compare_exchange_weak` instead.
1802    /// `compare_exchange_weak` is allowed to fail spuriously even when the comparison succeeds,
1803    /// which allows the compiler to generate better assembly code when the compare and swap
1804    /// is used in a loop.
1805    ///
1806    /// # Examples
1807    ///
1808    /// ```
1809    /// use std::sync::atomic::{AtomicPtr, Ordering};
1810    ///
1811    /// let ptr = &mut 5;
1812    /// let some_ptr = AtomicPtr::new(ptr);
1813    ///
1814    /// let other_ptr = &mut 10;
1815    ///
1816    /// let value = some_ptr.compare_and_swap(ptr, other_ptr, Ordering::Relaxed);
1817    /// ```
1818    #[inline]
1819    #[stable(feature = "rust1", since = "1.0.0")]
1820    #[deprecated(
1821        since = "1.50.0",
1822        note = "Use `compare_exchange` or `compare_exchange_weak` instead"
1823    )]
1824    #[cfg(target_has_atomic = "ptr")]
1825    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1826    #[rustc_should_not_be_called_on_const_items]
1827    pub fn compare_and_swap(&self, current: *mut T, new: *mut T, order: Ordering) -> *mut T {
1828        match self.compare_exchange(current, new, order, strongest_failure_ordering(order)) {
1829            Ok(x) => x,
1830            Err(x) => x,
1831        }
1832    }
1833
1834    /// Stores a value into the pointer if the current value is the same as the `current` value.
1835    ///
1836    /// The return value is a result indicating whether the new value was written and containing
1837    /// the previous value. On success this value is guaranteed to be equal to `current`.
1838    ///
1839    /// `compare_exchange` takes two [`Ordering`] arguments to describe the memory
1840    /// ordering of this operation. `success` describes the required ordering for the
1841    /// read-modify-write operation that takes place if the comparison with `current` succeeds.
1842    /// `failure` describes the required ordering for the load operation that takes place when
1843    /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
1844    /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
1845    /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
1846    ///
1847    /// **Note:** This method is only available on platforms that support atomic
1848    /// operations on pointers.
1849    ///
1850    /// # Examples
1851    ///
1852    /// ```
1853    /// use std::sync::atomic::{AtomicPtr, Ordering};
1854    ///
1855    /// let ptr = &mut 5;
1856    /// let some_ptr = AtomicPtr::new(ptr);
1857    ///
1858    /// let other_ptr = &mut 10;
1859    ///
1860    /// let value = some_ptr.compare_exchange(ptr, other_ptr,
1861    ///                                       Ordering::SeqCst, Ordering::Relaxed);
1862    /// ```
1863    ///
1864    /// # Considerations
1865    ///
1866    /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
1867    /// of CAS operations. In particular, a load of the value followed by a successful
1868    /// `compare_exchange` with the previous load *does not ensure* that other threads have not
1869    /// changed the value in the interim. This is usually important when the *equality* check in
1870    /// the `compare_exchange` is being used to check the *identity* of a value, but equality
1871    /// does not necessarily imply identity. This is a particularly common case for pointers, as
1872    /// a pointer holding the same address does not imply that the same object exists at that
1873    /// address! In this case, `compare_exchange` can lead to the [ABA problem].
1874    ///
1875    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
1876    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
1877    #[inline]
1878    #[stable(feature = "extended_compare_and_swap", since = "1.10.0")]
1879    #[cfg(target_has_atomic = "ptr")]
1880    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1881    #[rustc_should_not_be_called_on_const_items]
1882    pub fn compare_exchange(
1883        &self,
1884        current: *mut T,
1885        new: *mut T,
1886        success: Ordering,
1887        failure: Ordering,
1888    ) -> Result<*mut T, *mut T> {
1889        // SAFETY: data races are prevented by atomic intrinsics.
1890        unsafe { atomic_compare_exchange(self.p.get(), current, new, success, failure) }
1891    }
1892
1893    /// Stores a value into the pointer if the current value is the same as the `current` value.
1894    ///
1895    /// Unlike [`AtomicPtr::compare_exchange`], this function is allowed to spuriously fail even when the
1896    /// comparison succeeds, which can result in more efficient code on some platforms. The
1897    /// return value is a result indicating whether the new value was written and containing the
1898    /// previous value.
1899    ///
1900    /// `compare_exchange_weak` takes two [`Ordering`] arguments to describe the memory
1901    /// ordering of this operation. `success` describes the required ordering for the
1902    /// read-modify-write operation that takes place if the comparison with `current` succeeds.
1903    /// `failure` describes the required ordering for the load operation that takes place when
1904    /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
1905    /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
1906    /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
1907    ///
1908    /// **Note:** This method is only available on platforms that support atomic
1909    /// operations on pointers.
1910    ///
1911    /// # Examples
1912    ///
1913    /// ```
1914    /// use std::sync::atomic::{AtomicPtr, Ordering};
1915    ///
1916    /// let some_ptr = AtomicPtr::new(&mut 5);
1917    ///
1918    /// let new = &mut 10;
1919    /// let mut old = some_ptr.load(Ordering::Relaxed);
1920    /// loop {
1921    ///     match some_ptr.compare_exchange_weak(old, new, Ordering::SeqCst, Ordering::Relaxed) {
1922    ///         Ok(_) => break,
1923    ///         Err(x) => old = x,
1924    ///     }
1925    /// }
1926    /// ```
1927    ///
1928    /// # Considerations
1929    ///
1930    /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
1931    /// of CAS operations. In particular, a load of the value followed by a successful
1932    /// `compare_exchange` with the previous load *does not ensure* that other threads have not
1933    /// changed the value in the interim. This is usually important when the *equality* check in
1934    /// the `compare_exchange` is being used to check the *identity* of a value, but equality
1935    /// does not necessarily imply identity. This is a particularly common case for pointers, as
1936    /// a pointer holding the same address does not imply that the same object exists at that
1937    /// address! In this case, `compare_exchange` can lead to the [ABA problem].
1938    ///
1939    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
1940    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
1941    #[inline]
1942    #[stable(feature = "extended_compare_and_swap", since = "1.10.0")]
1943    #[cfg(target_has_atomic = "ptr")]
1944    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1945    #[rustc_should_not_be_called_on_const_items]
1946    pub fn compare_exchange_weak(
1947        &self,
1948        current: *mut T,
1949        new: *mut T,
1950        success: Ordering,
1951        failure: Ordering,
1952    ) -> Result<*mut T, *mut T> {
1953        // SAFETY: This intrinsic is unsafe because it operates on a raw pointer
1954        // but we know for sure that the pointer is valid (we just got it from
1955        // an `UnsafeCell` that we have by reference) and the atomic operation
1956        // itself allows us to safely mutate the `UnsafeCell` contents.
1957        unsafe { atomic_compare_exchange_weak(self.p.get(), current, new, success, failure) }
1958    }
1959
1960    /// An alias for [`AtomicPtr::try_update`].
1961    #[inline]
1962    #[stable(feature = "atomic_fetch_update", since = "1.53.0")]
1963    #[cfg(target_has_atomic = "ptr")]
1964    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
1965    #[rustc_should_not_be_called_on_const_items]
1966    #[deprecated(
1967        since = "1.99.0",
1968        note = "renamed to `try_update` for consistency",
1969        suggestion = "try_update"
1970    )]
1971    pub fn fetch_update<F>(
1972        &self,
1973        set_order: Ordering,
1974        fetch_order: Ordering,
1975        f: F,
1976    ) -> Result<*mut T, *mut T>
1977    where
1978        F: FnMut(*mut T) -> Option<*mut T>,
1979    {
1980        self.try_update(set_order, fetch_order, f)
1981    }
1982    /// Fetches the value, and applies a function to it that returns an optional
1983    /// new value. Returns a `Result` of `Ok(previous_value)` if the function
1984    /// returned `Some(_)`, else `Err(previous_value)`.
1985    ///
1986    /// See also: [`update`](`AtomicPtr::update`).
1987    ///
1988    /// Note: This may call the function multiple times if the value has been
1989    /// changed from other threads in the meantime, as long as the function
1990    /// returns `Some(_)`, but the function will have been applied only once to
1991    /// the stored value.
1992    ///
1993    /// `try_update` takes two [`Ordering`] arguments to describe the memory
1994    /// ordering of this operation. The first describes the required ordering for
1995    /// when the operation finally succeeds while the second describes the
1996    /// required ordering for loads. These correspond to the success and failure
1997    /// orderings of [`AtomicPtr::compare_exchange`] respectively.
1998    ///
1999    /// Using [`Acquire`] as success ordering makes the store part of this
2000    /// operation [`Relaxed`], and using [`Release`] makes the final successful
2001    /// load [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`],
2002    /// [`Acquire`] or [`Relaxed`].
2003    ///
2004    /// **Note:** This method is only available on platforms that support atomic
2005    /// operations on pointers.
2006    ///
2007    /// # Considerations
2008    ///
2009    /// This method is not magic; it is not provided by the hardware, and does not act like a
2010    /// critical section or mutex.
2011    ///
2012    /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
2013    /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem],
2014    /// which is a particularly common pitfall for pointers!
2015    ///
2016    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
2017    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
2018    ///
2019    /// # Examples
2020    ///
2021    /// ```rust
2022    /// use std::sync::atomic::{AtomicPtr, Ordering};
2023    ///
2024    /// let ptr: *mut _ = &mut 5;
2025    /// let some_ptr = AtomicPtr::new(ptr);
2026    ///
2027    /// let new: *mut _ = &mut 10;
2028    /// assert_eq!(some_ptr.try_update(Ordering::SeqCst, Ordering::SeqCst, |_| None), Err(ptr));
2029    /// let result = some_ptr.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| {
2030    ///     if x == ptr {
2031    ///         Some(new)
2032    ///     } else {
2033    ///         None
2034    ///     }
2035    /// });
2036    /// assert_eq!(result, Ok(ptr));
2037    /// assert_eq!(some_ptr.load(Ordering::SeqCst), new);
2038    /// ```
2039    #[inline]
2040    #[stable(feature = "atomic_try_update", since = "1.95.0")]
2041    #[cfg(target_has_atomic = "ptr")]
2042    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2043    #[rustc_should_not_be_called_on_const_items]
2044    pub fn try_update(
2045        &self,
2046        set_order: Ordering,
2047        fetch_order: Ordering,
2048        mut f: impl FnMut(*mut T) -> Option<*mut T>,
2049    ) -> Result<*mut T, *mut T> {
2050        let mut prev = self.load(fetch_order);
2051        while let Some(next) = f(prev) {
2052            match self.compare_exchange_weak(prev, next, set_order, fetch_order) {
2053                x @ Ok(_) => return x,
2054                Err(next_prev) => prev = next_prev,
2055            }
2056        }
2057        Err(prev)
2058    }
2059
2060    /// Fetches the value, applies a function to it that it return a new value.
2061    /// The new value is stored and the old value is returned.
2062    ///
2063    /// See also: [`try_update`](`AtomicPtr::try_update`).
2064    ///
2065    /// Note: This may call the function multiple times if the value has been changed from other threads in
2066    /// the meantime, but the function will have been applied only once to the stored value.
2067    ///
2068    /// `update` takes two [`Ordering`] arguments to describe the memory
2069    /// ordering of this operation. The first describes the required ordering for
2070    /// when the operation finally succeeds while the second describes the
2071    /// required ordering for loads. These correspond to the success and failure
2072    /// orderings of [`AtomicPtr::compare_exchange`] respectively.
2073    ///
2074    /// Using [`Acquire`] as success ordering makes the store part
2075    /// of this operation [`Relaxed`], and using [`Release`] makes the final successful load
2076    /// [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
2077    ///
2078    /// **Note:** This method is only available on platforms that support atomic
2079    /// operations on pointers.
2080    ///
2081    /// # Considerations
2082    ///
2083    /// This method is not magic; it is not provided by the hardware, and does not act like a
2084    /// critical section or mutex.
2085    ///
2086    /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
2087    /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem],
2088    /// which is a particularly common pitfall for pointers!
2089    ///
2090    /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
2091    /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
2092    ///
2093    /// # Examples
2094    ///
2095    /// ```rust
2096    ///
2097    /// use std::sync::atomic::{AtomicPtr, Ordering};
2098    ///
2099    /// let ptr: *mut _ = &mut 5;
2100    /// let some_ptr = AtomicPtr::new(ptr);
2101    ///
2102    /// let new: *mut _ = &mut 10;
2103    /// let result = some_ptr.update(Ordering::SeqCst, Ordering::SeqCst, |_| new);
2104    /// assert_eq!(result, ptr);
2105    /// assert_eq!(some_ptr.load(Ordering::SeqCst), new);
2106    /// ```
2107    #[inline]
2108    #[stable(feature = "atomic_try_update", since = "1.95.0")]
2109    #[cfg(target_has_atomic = "8")]
2110    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2111    #[rustc_should_not_be_called_on_const_items]
2112    pub fn update(
2113        &self,
2114        set_order: Ordering,
2115        fetch_order: Ordering,
2116        mut f: impl FnMut(*mut T) -> *mut T,
2117    ) -> *mut T {
2118        let mut prev = self.load(fetch_order);
2119        loop {
2120            match self.compare_exchange_weak(prev, f(prev), set_order, fetch_order) {
2121                Ok(x) => break x,
2122                Err(next_prev) => prev = next_prev,
2123            }
2124        }
2125    }
2126
2127    /// Offsets the pointer's address by adding `val` (in units of `T`),
2128    /// returning the previous pointer.
2129    ///
2130    /// This is equivalent to using [`wrapping_add`] to atomically perform the
2131    /// equivalent of `ptr = ptr.wrapping_add(val);`.
2132    ///
2133    /// This method operates in units of `T`, which means that it cannot be used
2134    /// to offset the pointer by an amount which is not a multiple of
2135    /// `size_of::<T>()`. This can sometimes be inconvenient, as you may want to
2136    /// work with a deliberately misaligned pointer. In such cases, you may use
2137    /// the [`fetch_byte_add`](Self::fetch_byte_add) method instead.
2138    ///
2139    /// `fetch_ptr_add` takes an [`Ordering`] argument which describes the
2140    /// memory ordering of this operation. All ordering modes are possible. Note
2141    /// that using [`Acquire`] makes the store part of this operation
2142    /// [`Relaxed`], and using [`Release`] makes the load part [`Relaxed`].
2143    ///
2144    /// **Note**: This method is only available on platforms that support atomic
2145    /// operations on [`AtomicPtr`].
2146    ///
2147    /// [`wrapping_add`]: pointer::wrapping_add
2148    ///
2149    /// # Examples
2150    ///
2151    /// ```
2152    /// use core::sync::atomic::{AtomicPtr, Ordering};
2153    ///
2154    /// let atom = AtomicPtr::<i64>::new(core::ptr::null_mut());
2155    /// assert_eq!(atom.fetch_ptr_add(1, Ordering::Relaxed).addr(), 0);
2156    /// // Note: units of `size_of::<i64>()`.
2157    /// assert_eq!(atom.load(Ordering::Relaxed).addr(), 8);
2158    /// ```
2159    #[inline]
2160    #[cfg(target_has_atomic = "ptr")]
2161    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2162    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2163    #[rustc_should_not_be_called_on_const_items]
2164    pub fn fetch_ptr_add(&self, val: usize, order: Ordering) -> *mut T {
2165        self.fetch_byte_add(val.wrapping_mul(size_of::<T>()), order)
2166    }
2167
2168    /// Offsets the pointer's address by subtracting `val` (in units of `T`),
2169    /// returning the previous pointer.
2170    ///
2171    /// This is equivalent to using [`wrapping_sub`] to atomically perform the
2172    /// equivalent of `ptr = ptr.wrapping_sub(val);`.
2173    ///
2174    /// This method operates in units of `T`, which means that it cannot be used
2175    /// to offset the pointer by an amount which is not a multiple of
2176    /// `size_of::<T>()`. This can sometimes be inconvenient, as you may want to
2177    /// work with a deliberately misaligned pointer. In such cases, you may use
2178    /// the [`fetch_byte_sub`](Self::fetch_byte_sub) method instead.
2179    ///
2180    /// `fetch_ptr_sub` takes an [`Ordering`] argument which describes the memory
2181    /// ordering of this operation. All ordering modes are possible. Note that
2182    /// using [`Acquire`] makes the store part of this operation [`Relaxed`],
2183    /// and using [`Release`] makes the load part [`Relaxed`].
2184    ///
2185    /// **Note**: This method is only available on platforms that support atomic
2186    /// operations on [`AtomicPtr`].
2187    ///
2188    /// [`wrapping_sub`]: pointer::wrapping_sub
2189    ///
2190    /// # Examples
2191    ///
2192    /// ```
2193    /// use core::sync::atomic::{AtomicPtr, Ordering};
2194    ///
2195    /// let array = [1i32, 2i32];
2196    /// let atom = AtomicPtr::new(array.as_ptr().wrapping_add(1) as *mut _);
2197    ///
2198    /// assert!(core::ptr::eq(
2199    ///     atom.fetch_ptr_sub(1, Ordering::Relaxed),
2200    ///     &array[1],
2201    /// ));
2202    /// assert!(core::ptr::eq(atom.load(Ordering::Relaxed), &array[0]));
2203    /// ```
2204    #[inline]
2205    #[cfg(target_has_atomic = "ptr")]
2206    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2207    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2208    #[rustc_should_not_be_called_on_const_items]
2209    pub fn fetch_ptr_sub(&self, val: usize, order: Ordering) -> *mut T {
2210        self.fetch_byte_sub(val.wrapping_mul(size_of::<T>()), order)
2211    }
2212
2213    /// Offsets the pointer's address by adding `val` *bytes*, returning the
2214    /// previous pointer.
2215    ///
2216    /// This is equivalent to using [`wrapping_byte_add`] to atomically
2217    /// perform `ptr = ptr.wrapping_byte_add(val)`.
2218    ///
2219    /// `fetch_byte_add` takes an [`Ordering`] argument which describes the
2220    /// memory ordering of this operation. All ordering modes are possible. Note
2221    /// that using [`Acquire`] makes the store part of this operation
2222    /// [`Relaxed`], and using [`Release`] makes the load part [`Relaxed`].
2223    ///
2224    /// **Note**: This method is only available on platforms that support atomic
2225    /// operations on [`AtomicPtr`].
2226    ///
2227    /// [`wrapping_byte_add`]: pointer::wrapping_byte_add
2228    ///
2229    /// # Examples
2230    ///
2231    /// ```
2232    /// use core::sync::atomic::{AtomicPtr, Ordering};
2233    ///
2234    /// let atom = AtomicPtr::<i64>::new(core::ptr::null_mut());
2235    /// assert_eq!(atom.fetch_byte_add(1, Ordering::Relaxed).addr(), 0);
2236    /// // Note: in units of bytes, not `size_of::<i64>()`.
2237    /// assert_eq!(atom.load(Ordering::Relaxed).addr(), 1);
2238    /// ```
2239    #[inline]
2240    #[cfg(target_has_atomic = "ptr")]
2241    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2242    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2243    #[rustc_should_not_be_called_on_const_items]
2244    pub fn fetch_byte_add(&self, val: usize, order: Ordering) -> *mut T {
2245        // SAFETY: data races are prevented by atomic intrinsics.
2246        unsafe { atomic_add(self.p.get(), val, order).cast() }
2247    }
2248
2249    /// Offsets the pointer's address by subtracting `val` *bytes*, returning the
2250    /// previous pointer.
2251    ///
2252    /// This is equivalent to using [`wrapping_byte_sub`] to atomically
2253    /// perform `ptr = ptr.wrapping_byte_sub(val)`.
2254    ///
2255    /// `fetch_byte_sub` takes an [`Ordering`] argument which describes the
2256    /// memory ordering of this operation. All ordering modes are possible. Note
2257    /// that using [`Acquire`] makes the store part of this operation
2258    /// [`Relaxed`], and using [`Release`] makes the load part [`Relaxed`].
2259    ///
2260    /// **Note**: This method is only available on platforms that support atomic
2261    /// operations on [`AtomicPtr`].
2262    ///
2263    /// [`wrapping_byte_sub`]: pointer::wrapping_byte_sub
2264    ///
2265    /// # Examples
2266    ///
2267    /// ```
2268    /// use core::sync::atomic::{AtomicPtr, Ordering};
2269    ///
2270    /// let mut arr = [0i64, 1];
2271    /// let atom = AtomicPtr::<i64>::new(&raw mut arr[1]);
2272    /// assert_eq!(atom.fetch_byte_sub(8, Ordering::Relaxed).addr(), (&raw const arr[1]).addr());
2273    /// assert_eq!(atom.load(Ordering::Relaxed).addr(), (&raw const arr[0]).addr());
2274    /// ```
2275    #[inline]
2276    #[cfg(target_has_atomic = "ptr")]
2277    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2278    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2279    #[rustc_should_not_be_called_on_const_items]
2280    pub fn fetch_byte_sub(&self, val: usize, order: Ordering) -> *mut T {
2281        // SAFETY: data races are prevented by atomic intrinsics.
2282        unsafe { atomic_sub(self.p.get(), val, order).cast() }
2283    }
2284
2285    /// Performs a bitwise "or" operation on the address of the current pointer,
2286    /// and the argument `val`, and stores a pointer with provenance of the
2287    /// current pointer and the resulting address.
2288    ///
2289    /// This is equivalent to using [`map_addr`] to atomically perform
2290    /// `ptr = ptr.map_addr(|a| a | val)`. This can be used in tagged
2291    /// pointer schemes to atomically set tag bits.
2292    ///
2293    /// **Caveat**: This operation returns the previous value. To compute the
2294    /// stored value without losing provenance, you may use [`map_addr`]. For
2295    /// example: `a.fetch_or(val).map_addr(|a| a | val)`.
2296    ///
2297    /// `fetch_or` takes an [`Ordering`] argument which describes the memory
2298    /// ordering of this operation. All ordering modes are possible. Note that
2299    /// using [`Acquire`] makes the store part of this operation [`Relaxed`],
2300    /// and using [`Release`] makes the load part [`Relaxed`].
2301    ///
2302    /// **Note**: This method is only available on platforms that support atomic
2303    /// operations on [`AtomicPtr`].
2304    ///
2305    /// This API and its claimed semantics are part of the Strict Provenance
2306    /// experiment, see the [module documentation for `ptr`][crate::ptr] for
2307    /// details.
2308    ///
2309    /// [`map_addr`]: pointer::map_addr
2310    ///
2311    /// # Examples
2312    ///
2313    /// ```
2314    /// use core::sync::atomic::{AtomicPtr, Ordering};
2315    ///
2316    /// let pointer = &mut 3i64 as *mut i64;
2317    ///
2318    /// let atom = AtomicPtr::<i64>::new(pointer);
2319    /// // Tag the bottom bit of the pointer.
2320    /// assert_eq!(atom.fetch_or(1, Ordering::Relaxed).addr() & 1, 0);
2321    /// // Extract and untag.
2322    /// let tagged = atom.load(Ordering::Relaxed);
2323    /// assert_eq!(tagged.addr() & 1, 1);
2324    /// assert_eq!(tagged.map_addr(|p| p & !1), pointer);
2325    /// ```
2326    #[inline]
2327    #[cfg(target_has_atomic = "ptr")]
2328    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2329    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2330    #[rustc_should_not_be_called_on_const_items]
2331    pub fn fetch_or(&self, val: usize, order: Ordering) -> *mut T {
2332        // SAFETY: data races are prevented by atomic intrinsics.
2333        unsafe { atomic_or(self.p.get(), val, order).cast() }
2334    }
2335
2336    /// Performs a bitwise "and" operation on the address of the current
2337    /// pointer, and the argument `val`, and stores a pointer with provenance of
2338    /// the current pointer and the resulting address.
2339    ///
2340    /// This is equivalent to using [`map_addr`] to atomically perform
2341    /// `ptr = ptr.map_addr(|a| a & val)`. This can be used in tagged
2342    /// pointer schemes to atomically unset tag bits.
2343    ///
2344    /// **Caveat**: This operation returns the previous value. To compute the
2345    /// stored value without losing provenance, you may use [`map_addr`]. For
2346    /// example: `a.fetch_and(val).map_addr(|a| a & val)`.
2347    ///
2348    /// `fetch_and` takes an [`Ordering`] argument which describes the memory
2349    /// ordering of this operation. All ordering modes are possible. Note that
2350    /// using [`Acquire`] makes the store part of this operation [`Relaxed`],
2351    /// and using [`Release`] makes the load part [`Relaxed`].
2352    ///
2353    /// **Note**: This method is only available on platforms that support atomic
2354    /// operations on [`AtomicPtr`].
2355    ///
2356    /// This API and its claimed semantics are part of the Strict Provenance
2357    /// experiment, see the [module documentation for `ptr`][crate::ptr] for
2358    /// details.
2359    ///
2360    /// [`map_addr`]: pointer::map_addr
2361    ///
2362    /// # Examples
2363    ///
2364    /// ```
2365    /// use core::sync::atomic::{AtomicPtr, Ordering};
2366    ///
2367    /// let pointer = &mut 3i64 as *mut i64;
2368    /// // A tagged pointer
2369    /// let atom = AtomicPtr::<i64>::new(pointer.map_addr(|a| a | 1));
2370    /// assert_eq!(atom.fetch_or(1, Ordering::Relaxed).addr() & 1, 1);
2371    /// // Untag, and extract the previously tagged pointer.
2372    /// let untagged = atom.fetch_and(!1, Ordering::Relaxed)
2373    ///     .map_addr(|a| a & !1);
2374    /// assert_eq!(untagged, pointer);
2375    /// ```
2376    #[inline]
2377    #[cfg(target_has_atomic = "ptr")]
2378    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2379    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2380    #[rustc_should_not_be_called_on_const_items]
2381    pub fn fetch_and(&self, val: usize, order: Ordering) -> *mut T {
2382        // SAFETY: data races are prevented by atomic intrinsics.
2383        unsafe { atomic_and(self.p.get(), val, order).cast() }
2384    }
2385
2386    /// Performs a bitwise "xor" operation on the address of the current
2387    /// pointer, and the argument `val`, and stores a pointer with provenance of
2388    /// the current pointer and the resulting address.
2389    ///
2390    /// This is equivalent to using [`map_addr`] to atomically perform
2391    /// `ptr = ptr.map_addr(|a| a ^ val)`. This can be used in tagged
2392    /// pointer schemes to atomically toggle tag bits.
2393    ///
2394    /// **Caveat**: This operation returns the previous value. To compute the
2395    /// stored value without losing provenance, you may use [`map_addr`]. For
2396    /// example: `a.fetch_xor(val).map_addr(|a| a ^ val)`.
2397    ///
2398    /// `fetch_xor` takes an [`Ordering`] argument which describes the memory
2399    /// ordering of this operation. All ordering modes are possible. Note that
2400    /// using [`Acquire`] makes the store part of this operation [`Relaxed`],
2401    /// and using [`Release`] makes the load part [`Relaxed`].
2402    ///
2403    /// **Note**: This method is only available on platforms that support atomic
2404    /// operations on [`AtomicPtr`].
2405    ///
2406    /// This API and its claimed semantics are part of the Strict Provenance
2407    /// experiment, see the [module documentation for `ptr`][crate::ptr] for
2408    /// details.
2409    ///
2410    /// [`map_addr`]: pointer::map_addr
2411    ///
2412    /// # Examples
2413    ///
2414    /// ```
2415    /// use core::sync::atomic::{AtomicPtr, Ordering};
2416    ///
2417    /// let pointer = &mut 3i64 as *mut i64;
2418    /// let atom = AtomicPtr::<i64>::new(pointer);
2419    ///
2420    /// // Toggle a tag bit on the pointer.
2421    /// atom.fetch_xor(1, Ordering::Relaxed);
2422    /// assert_eq!(atom.load(Ordering::Relaxed).addr() & 1, 1);
2423    /// ```
2424    #[inline]
2425    #[cfg(target_has_atomic = "ptr")]
2426    #[stable(feature = "strict_provenance_atomic_ptr", since = "1.91.0")]
2427    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2428    #[rustc_should_not_be_called_on_const_items]
2429    pub fn fetch_xor(&self, val: usize, order: Ordering) -> *mut T {
2430        // SAFETY: data races are prevented by atomic intrinsics.
2431        unsafe { atomic_xor(self.p.get(), val, order).cast() }
2432    }
2433
2434    /// Returns a mutable pointer to the underlying pointer.
2435    ///
2436    /// Doing non-atomic reads and writes on the resulting pointer can be a data race.
2437    /// This method is mostly useful for FFI, where the function signature may use
2438    /// `*mut *mut T` instead of `&AtomicPtr<T>`.
2439    ///
2440    /// Returning an `*mut` pointer from a shared reference to this atomic is safe because the
2441    /// atomic types work with interior mutability. All modifications of an atomic change the value
2442    /// through a shared reference, and can do so safely as long as they use atomic operations. Any
2443    /// use of the returned raw pointer requires an `unsafe` block and still has to uphold the
2444    /// requirements of the [memory model].
2445    ///
2446    /// # Examples
2447    ///
2448    /// ```ignore (extern-declaration)
2449    /// use std::sync::atomic::AtomicPtr;
2450    ///
2451    /// extern "C" {
2452    ///     fn my_atomic_op(arg: *mut *mut u32);
2453    /// }
2454    ///
2455    /// let mut value = 17;
2456    /// let atomic = AtomicPtr::new(&mut value);
2457    ///
2458    /// // SAFETY: Safe as long as `my_atomic_op` is atomic.
2459    /// unsafe {
2460    ///     my_atomic_op(atomic.as_ptr());
2461    /// }
2462    /// ```
2463    ///
2464    /// [memory model]: self#memory-model-for-atomic-accesses
2465    #[inline]
2466    #[stable(feature = "atomic_as_ptr", since = "1.70.0")]
2467    #[rustc_const_stable(feature = "atomic_as_ptr", since = "1.70.0")]
2468    #[rustc_never_returns_null_ptr]
2469    pub const fn as_ptr(&self) -> *mut *mut T {
2470        self.p.get()
2471    }
2472}
2473
2474#[cfg(target_has_atomic_load_store = "8")]
2475#[stable(feature = "atomic_bool_from", since = "1.24.0")]
2476#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2477impl const From<bool> for AtomicBool {
2478    /// Converts a `bool` into an `AtomicBool`.
2479    ///
2480    /// # Examples
2481    ///
2482    /// ```
2483    /// use std::sync::atomic::AtomicBool;
2484    /// let atomic_bool = AtomicBool::from(true);
2485    /// assert_eq!(format!("{atomic_bool:?}"), "true")
2486    /// ```
2487    #[inline]
2488    fn from(b: bool) -> Self {
2489        Self::new(b)
2490    }
2491}
2492
2493#[cfg(target_has_atomic_load_store = "ptr")]
2494#[stable(feature = "atomic_from", since = "1.23.0")]
2495#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2496impl<T> const From<*mut T> for AtomicPtr<T> {
2497    /// Converts a `*mut T` into an `AtomicPtr<T>`.
2498    #[inline]
2499    fn from(p: *mut T) -> Self {
2500        Self::new(p)
2501    }
2502}
2503
2504#[allow(unused_macros)] // This macro ends up being unused on some architectures.
2505macro_rules! if_8_bit {
2506    (u8, $( yes = [$($yes:tt)*], )? $( no = [$($no:tt)*], )? ) => { concat!("", $($($yes)*)?) };
2507    (i8, $( yes = [$($yes:tt)*], )? $( no = [$($no:tt)*], )? ) => { concat!("", $($($yes)*)?) };
2508    ($_:ident, $( yes = [$($yes:tt)*], )? $( no = [$($no:tt)*], )? ) => { concat!("", $($($no)*)?) };
2509}
2510
2511#[cfg(target_has_atomic_load_store)]
2512macro_rules! atomic_int {
2513    ($cfg_cas:meta,
2514     $cfg_align:meta,
2515     $stable:meta,
2516     $stable_cxchg:meta,
2517     $stable_debug:meta,
2518     $stable_access:meta,
2519     $stable_from:meta,
2520     $stable_nand:meta,
2521     $const_stable_new:meta,
2522     $const_stable_into_inner:meta,
2523     $diagnostic_item:meta,
2524     $s_int_type:literal,
2525     $extra_feature:expr,
2526     $min_fn:ident, $max_fn:ident,
2527     $align:expr,
2528     $int_type:ident $atomic_type:ident) => {
2529        /// An integer type which can be safely shared between threads.
2530        ///
2531        /// This type has the same
2532        #[doc = if_8_bit!(
2533            $int_type,
2534            yes = ["size, alignment, and bit validity"],
2535            no = ["size and bit validity"],
2536        )]
2537        /// as the underlying integer type, [`
2538        #[doc = $s_int_type]
2539        /// `].
2540        #[doc = if_8_bit! {
2541            $int_type,
2542            no = [
2543                "However, the alignment of this type is always equal to its ",
2544                "size, even on targets where [`", $s_int_type, "`] has a ",
2545                "lesser alignment."
2546            ],
2547        }]
2548        ///
2549        /// For more about the differences between atomic types and
2550        /// non-atomic types as well as information about the portability of
2551        /// this type, please see the [module-level documentation].
2552        ///
2553        /// **Note:** This type is only available on platforms that support
2554        /// atomic loads and stores of [`
2555        #[doc = $s_int_type]
2556        /// `].
2557        ///
2558        /// [module-level documentation]: crate::sync::atomic
2559        #[$stable]
2560        #[$diagnostic_item]
2561        #[repr(C, align($align))]
2562        pub struct $atomic_type {
2563            v: UnsafeCell<$int_type>,
2564        }
2565
2566        #[$stable]
2567        impl Default for $atomic_type {
2568            #[inline]
2569            fn default() -> Self {
2570                Self::new(Default::default())
2571            }
2572        }
2573
2574        #[$stable_from]
2575        #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2576        impl const From<$int_type> for $atomic_type {
2577            #[doc = concat!("Converts an `", stringify!($int_type), "` into an `", stringify!($atomic_type), "`.")]
2578            #[inline]
2579            fn from(v: $int_type) -> Self { Self::new(v) }
2580        }
2581
2582        #[$stable_debug]
2583        impl fmt::Debug for $atomic_type {
2584            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2585                fmt::Debug::fmt(&self.load(Ordering::Relaxed), f)
2586            }
2587        }
2588
2589        // Send is implicitly implemented.
2590        #[$stable]
2591        unsafe impl Sync for $atomic_type {}
2592
2593        impl $atomic_type {
2594            /// Creates a new atomic integer.
2595            ///
2596            /// # Examples
2597            ///
2598            /// ```
2599            #[doc = concat!($extra_feature, "use std::sync::atomic::", stringify!($atomic_type), ";")]
2600            ///
2601            #[doc = concat!("let atomic_forty_two = ", stringify!($atomic_type), "::new(42);")]
2602            /// ```
2603            #[inline]
2604            #[$stable]
2605            #[$const_stable_new]
2606            #[must_use]
2607            pub const fn new(v: $int_type) -> Self {
2608                Self {v: UnsafeCell::new(v)}
2609            }
2610
2611            /// Creates a new reference to an atomic integer from a pointer.
2612            ///
2613            /// # Examples
2614            ///
2615            /// ```
2616            #[doc = concat!($extra_feature, "use std::sync::atomic::{self, ", stringify!($atomic_type), "};")]
2617            ///
2618            /// // Get a pointer to an allocated value
2619            #[doc = concat!("let ptr: *mut ", stringify!($int_type), " = Box::into_raw(Box::new(0));")]
2620            ///
2621            #[doc = concat!("assert!(ptr.cast::<", stringify!($atomic_type), ">().is_aligned());")]
2622            ///
2623            /// {
2624            ///     // Create an atomic view of the allocated value
2625            // SAFETY: this is a doc comment, tidy, it can't hurt you (also guaranteed by the construction of `ptr` and the assert above)
2626            #[doc = concat!("    let atomic = unsafe {", stringify!($atomic_type), "::from_ptr(ptr) };")]
2627            ///
2628            ///     // Use `atomic` for atomic operations, possibly share it with other threads
2629            ///     atomic.store(1, atomic::Ordering::Relaxed);
2630            /// }
2631            ///
2632            /// // It's ok to non-atomically access the value behind `ptr`,
2633            /// // since the reference to the atomic ended its lifetime in the block above
2634            /// assert_eq!(unsafe { *ptr }, 1);
2635            ///
2636            /// // Deallocate the value
2637            /// unsafe { drop(Box::from_raw(ptr)) }
2638            /// ```
2639            ///
2640            /// # Safety
2641            ///
2642            /// * `ptr` must be aligned to
2643            #[doc = concat!("  `align_of::<", stringify!($atomic_type), ">()`")]
2644            #[doc = if_8_bit!{
2645                $int_type,
2646                yes = [
2647                    "  (note that this is always true, since `align_of::<",
2648                    stringify!($atomic_type), ">() == 1`)."
2649                ],
2650                no = [
2651                    "  (note that on some platforms this can be bigger than `align_of::<",
2652                    stringify!($int_type), ">()`)."
2653                ],
2654            }]
2655            /// * `ptr` must be [valid] for both reads and writes for the whole lifetime `'a`.
2656            /// * You must adhere to the [Memory model for atomic accesses]. In particular, it is not
2657            ///   allowed to mix conflicting atomic and non-atomic accesses, or atomic accesses of different
2658            ///   sizes, without synchronization.
2659            ///
2660            /// [valid]: crate::ptr#safety
2661            /// [Memory model for atomic accesses]: self#memory-model-for-atomic-accesses
2662            #[inline]
2663            #[stable(feature = "atomic_from_ptr", since = "1.75.0")]
2664            #[rustc_const_stable(feature = "const_atomic_from_ptr", since = "1.84.0")]
2665            pub const unsafe fn from_ptr<'a>(ptr: *mut $int_type) -> &'a $atomic_type {
2666                // SAFETY: guaranteed by the caller
2667                unsafe { &*ptr.cast() }
2668            }
2669
2670
2671            /// Returns a mutable reference to the underlying integer.
2672            ///
2673            /// This is safe because the mutable reference guarantees that no other threads are
2674            /// concurrently accessing the atomic data.
2675            ///
2676            /// # Examples
2677            ///
2678            /// ```
2679            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2680            ///
2681            #[doc = concat!("let mut some_var = ", stringify!($atomic_type), "::new(10);")]
2682            /// assert_eq!(*some_var.get_mut(), 10);
2683            /// *some_var.get_mut() = 5;
2684            /// assert_eq!(some_var.load(Ordering::SeqCst), 5);
2685            /// ```
2686            #[inline]
2687            #[$stable_access]
2688            pub fn get_mut(&mut self) -> &mut $int_type {
2689                self.v.get_mut()
2690            }
2691
2692            #[doc = concat!("Get atomic access to a `&mut ", stringify!($int_type), "`.")]
2693            ///
2694            #[doc = if_8_bit! {
2695                $int_type,
2696                no = [
2697                    "**Note:** This function is only available on targets where `",
2698                    stringify!($atomic_type), "` has the same alignment as `", stringify!($int_type), "`."
2699                ],
2700            }]
2701            ///
2702            /// # Examples
2703            ///
2704            /// ```
2705            /// #![feature(atomic_from_mut)]
2706            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2707            ///
2708            /// let mut some_int = 123;
2709            #[doc = concat!("let a = ", stringify!($atomic_type), "::from_mut(&mut some_int);")]
2710            /// a.store(100, Ordering::Relaxed);
2711            /// assert_eq!(some_int, 100);
2712            /// ```
2713            ///
2714            #[inline]
2715            #[$cfg_align]
2716            #[unstable(feature = "atomic_from_mut", issue = "76314")]
2717            pub fn from_mut(v: &mut $int_type) -> &mut Self {
2718                let [] = [(); align_of::<Self>() - align_of::<$int_type>()];
2719                // SAFETY:
2720                //  - the mutable reference guarantees unique ownership.
2721                //  - the alignment of `$int_type` and `Self` is the
2722                //    same, as promised by $cfg_align and verified above.
2723                unsafe { &mut *(v as *mut $int_type as *mut Self) }
2724            }
2725
2726            #[doc = concat!("Get non-atomic access to a `&mut [", stringify!($atomic_type), "]` slice")]
2727            ///
2728            /// This is safe because the mutable reference guarantees that no other threads are
2729            /// concurrently accessing the atomic data.
2730            ///
2731            /// # Examples
2732            ///
2733            /// ```ignore-wasm
2734            /// #![feature(atomic_from_mut)]
2735            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2736            ///
2737            #[doc = concat!("let mut some_ints = [const { ", stringify!($atomic_type), "::new(0) }; 10];")]
2738            ///
2739            #[doc = concat!("let view: &mut [", stringify!($int_type), "] = ", stringify!($atomic_type), "::get_mut_slice(&mut some_ints);")]
2740            /// assert_eq!(view, [0; 10]);
2741            /// view
2742            ///     .iter_mut()
2743            ///     .enumerate()
2744            ///     .for_each(|(idx, int)| *int = idx as _);
2745            ///
2746            /// std::thread::scope(|s| {
2747            ///     some_ints
2748            ///         .iter()
2749            ///         .enumerate()
2750            ///         .for_each(|(idx, int)| {
2751            ///             s.spawn(move || assert_eq!(int.load(Ordering::Relaxed), idx as _));
2752            ///         })
2753            /// });
2754            /// ```
2755            #[inline]
2756            #[unstable(feature = "atomic_from_mut", issue = "76314")]
2757            pub fn get_mut_slice(this: &mut [Self]) -> &mut [$int_type] {
2758                // SAFETY: the mutable reference guarantees unique ownership.
2759                unsafe { &mut *(this as *mut [Self] as *mut [$int_type]) }
2760            }
2761
2762            #[doc = concat!("Get atomic access to a `&mut [", stringify!($int_type), "]` slice.")]
2763            ///
2764            #[doc = if_8_bit! {
2765                $int_type,
2766                no = [
2767                    "**Note:** This function is only available on targets where `",
2768                    stringify!($atomic_type), "` has the same alignment as `", stringify!($int_type), "`."
2769                ],
2770            }]
2771            ///
2772            /// # Examples
2773            ///
2774            /// ```ignore-wasm
2775            /// #![feature(atomic_from_mut)]
2776            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2777            ///
2778            /// let mut some_ints = [0; 10];
2779            #[doc = concat!("let a = &*", stringify!($atomic_type), "::from_mut_slice(&mut some_ints);")]
2780            /// std::thread::scope(|s| {
2781            ///     for i in 0..a.len() {
2782            ///         s.spawn(move || a[i].store(i as _, Ordering::Relaxed));
2783            ///     }
2784            /// });
2785            /// for (i, n) in some_ints.into_iter().enumerate() {
2786            ///     assert_eq!(i, n as usize);
2787            /// }
2788            /// ```
2789            #[inline]
2790            #[$cfg_align]
2791            #[unstable(feature = "atomic_from_mut", issue = "76314")]
2792            pub fn from_mut_slice(v: &mut [$int_type]) -> &mut [Self] {
2793                let [] = [(); align_of::<Self>() - align_of::<$int_type>()];
2794                // SAFETY:
2795                //  - the mutable reference guarantees unique ownership.
2796                //  - the alignment of `$int_type` and `Self` is the
2797                //    same, as promised by $cfg_align and verified above.
2798                unsafe { &mut *(v as *mut [$int_type] as *mut [Self]) }
2799            }
2800
2801            /// Consumes the atomic and returns the contained value.
2802            ///
2803            /// This is safe because passing `self` by value guarantees that no other threads are
2804            /// concurrently accessing the atomic data.
2805            ///
2806            /// # Examples
2807            ///
2808            /// ```
2809            #[doc = concat!($extra_feature, "use std::sync::atomic::", stringify!($atomic_type), ";")]
2810            ///
2811            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
2812            /// assert_eq!(some_var.into_inner(), 5);
2813            /// ```
2814            #[inline]
2815            #[$stable_access]
2816            #[$const_stable_into_inner]
2817            pub const fn into_inner(self) -> $int_type {
2818                self.v.into_inner()
2819            }
2820
2821            /// Loads a value from the atomic integer.
2822            ///
2823            /// `load` takes an [`Ordering`] argument which describes the memory ordering of this operation.
2824            /// Possible values are [`SeqCst`], [`Acquire`] and [`Relaxed`].
2825            ///
2826            /// # Panics
2827            ///
2828            /// Panics if `order` is [`Release`] or [`AcqRel`].
2829            ///
2830            /// # Examples
2831            ///
2832            /// ```
2833            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2834            ///
2835            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
2836            ///
2837            /// assert_eq!(some_var.load(Ordering::Relaxed), 5);
2838            /// ```
2839            #[inline]
2840            #[$stable]
2841            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2842            pub fn load(&self, order: Ordering) -> $int_type {
2843                // SAFETY: data races are prevented by atomic intrinsics.
2844                unsafe { atomic_load(self.v.get(), order) }
2845            }
2846
2847            /// Stores a value into the atomic integer.
2848            ///
2849            /// `store` takes an [`Ordering`] argument which describes the memory ordering of this operation.
2850            ///  Possible values are [`SeqCst`], [`Release`] and [`Relaxed`].
2851            ///
2852            /// # Panics
2853            ///
2854            /// Panics if `order` is [`Acquire`] or [`AcqRel`].
2855            ///
2856            /// # Examples
2857            ///
2858            /// ```
2859            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2860            ///
2861            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
2862            ///
2863            /// some_var.store(10, Ordering::Relaxed);
2864            /// assert_eq!(some_var.load(Ordering::Relaxed), 10);
2865            /// ```
2866            #[inline]
2867            #[$stable]
2868            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2869            #[rustc_should_not_be_called_on_const_items]
2870            pub fn store(&self, val: $int_type, order: Ordering) {
2871                // SAFETY: data races are prevented by atomic intrinsics.
2872                unsafe { atomic_store(self.v.get(), val, order); }
2873            }
2874
2875            /// Stores a value into the atomic integer, returning the previous value.
2876            ///
2877            /// `swap` takes an [`Ordering`] argument which describes the memory ordering
2878            /// of this operation. All ordering modes are possible. Note that using
2879            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
2880            /// using [`Release`] makes the load part [`Relaxed`].
2881            ///
2882            /// **Note**: This method is only available on platforms that support atomic operations on
2883            #[doc = concat!("[`", $s_int_type, "`].")]
2884            ///
2885            /// # Examples
2886            ///
2887            /// ```
2888            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2889            ///
2890            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
2891            ///
2892            /// assert_eq!(some_var.swap(10, Ordering::Relaxed), 5);
2893            /// ```
2894            #[inline]
2895            #[$stable]
2896            #[$cfg_cas]
2897            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2898            #[rustc_should_not_be_called_on_const_items]
2899            pub fn swap(&self, val: $int_type, order: Ordering) -> $int_type {
2900                // SAFETY: data races are prevented by atomic intrinsics.
2901                unsafe { atomic_swap(self.v.get(), val, order) }
2902            }
2903
2904            /// Stores a value into the atomic integer if the current value is the same as
2905            /// the `current` value.
2906            ///
2907            /// The return value is always the previous value. If it is equal to `current`, then the
2908            /// value was updated.
2909            ///
2910            /// `compare_and_swap` also takes an [`Ordering`] argument which describes the memory
2911            /// ordering of this operation. Notice that even when using [`AcqRel`], the operation
2912            /// might fail and hence just perform an `Acquire` load, but not have `Release` semantics.
2913            /// Using [`Acquire`] makes the store part of this operation [`Relaxed`] if it
2914            /// happens, and using [`Release`] makes the load part [`Relaxed`].
2915            ///
2916            /// **Note**: This method is only available on platforms that support atomic operations on
2917            #[doc = concat!("[`", $s_int_type, "`].")]
2918            ///
2919            /// # Migrating to `compare_exchange` and `compare_exchange_weak`
2920            ///
2921            /// `compare_and_swap` is equivalent to `compare_exchange` with the following mapping for
2922            /// memory orderings:
2923            ///
2924            /// Original | Success | Failure
2925            /// -------- | ------- | -------
2926            /// Relaxed  | Relaxed | Relaxed
2927            /// Acquire  | Acquire | Acquire
2928            /// Release  | Release | Relaxed
2929            /// AcqRel   | AcqRel  | Acquire
2930            /// SeqCst   | SeqCst  | SeqCst
2931            ///
2932            /// `compare_and_swap` and `compare_exchange` also differ in their return type. You can use
2933            /// `compare_exchange(...).unwrap_or_else(|x| x)` to recover the behavior of `compare_and_swap`,
2934            /// but in most cases it is more idiomatic to check whether the return value is `Ok` or `Err`
2935            /// rather than to infer success vs failure based on the value that was read.
2936            ///
2937            /// During migration, consider whether it makes sense to use `compare_exchange_weak` instead.
2938            /// `compare_exchange_weak` is allowed to fail spuriously even when the comparison succeeds,
2939            /// which allows the compiler to generate better assembly code when the compare and swap
2940            /// is used in a loop.
2941            ///
2942            /// # Examples
2943            ///
2944            /// ```
2945            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2946            ///
2947            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
2948            ///
2949            /// assert_eq!(some_var.compare_and_swap(5, 10, Ordering::Relaxed), 5);
2950            /// assert_eq!(some_var.load(Ordering::Relaxed), 10);
2951            ///
2952            /// assert_eq!(some_var.compare_and_swap(6, 12, Ordering::Relaxed), 10);
2953            /// assert_eq!(some_var.load(Ordering::Relaxed), 10);
2954            /// ```
2955            #[inline]
2956            #[$stable]
2957            #[deprecated(
2958                since = "1.50.0",
2959                note = "Use `compare_exchange` or `compare_exchange_weak` instead")
2960            ]
2961            #[$cfg_cas]
2962            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2963            #[rustc_should_not_be_called_on_const_items]
2964            pub fn compare_and_swap(&self,
2965                                    current: $int_type,
2966                                    new: $int_type,
2967                                    order: Ordering) -> $int_type {
2968                match self.compare_exchange(current,
2969                                            new,
2970                                            order,
2971                                            strongest_failure_ordering(order)) {
2972                    Ok(x) => x,
2973                    Err(x) => x,
2974                }
2975            }
2976
2977            /// Stores a value into the atomic integer if the current value is the same as
2978            /// the `current` value.
2979            ///
2980            /// The return value is a result indicating whether the new value was written and
2981            /// containing the previous value. On success this value is guaranteed to be equal to
2982            /// `current`.
2983            ///
2984            /// `compare_exchange` takes two [`Ordering`] arguments to describe the memory
2985            /// ordering of this operation. `success` describes the required ordering for the
2986            /// read-modify-write operation that takes place if the comparison with `current` succeeds.
2987            /// `failure` describes the required ordering for the load operation that takes place when
2988            /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
2989            /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
2990            /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
2991            ///
2992            /// **Note**: This method is only available on platforms that support atomic operations on
2993            #[doc = concat!("[`", $s_int_type, "`].")]
2994            ///
2995            /// # Examples
2996            ///
2997            /// ```
2998            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
2999            ///
3000            #[doc = concat!("let some_var = ", stringify!($atomic_type), "::new(5);")]
3001            ///
3002            /// assert_eq!(some_var.compare_exchange(5, 10,
3003            ///                                      Ordering::Acquire,
3004            ///                                      Ordering::Relaxed),
3005            ///            Ok(5));
3006            /// assert_eq!(some_var.load(Ordering::Relaxed), 10);
3007            ///
3008            /// assert_eq!(some_var.compare_exchange(6, 12,
3009            ///                                      Ordering::SeqCst,
3010            ///                                      Ordering::Acquire),
3011            ///            Err(10));
3012            /// assert_eq!(some_var.load(Ordering::Relaxed), 10);
3013            /// ```
3014            ///
3015            /// # Considerations
3016            ///
3017            /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
3018            /// of CAS operations. In particular, a load of the value followed by a successful
3019            /// `compare_exchange` with the previous load *does not ensure* that other threads have not
3020            /// changed the value in the interim! This is usually important when the *equality* check in
3021            /// the `compare_exchange` is being used to check the *identity* of a value, but equality
3022            /// does not necessarily imply identity. This is a particularly common case for pointers, as
3023            /// a pointer holding the same address does not imply that the same object exists at that
3024            /// address! In this case, `compare_exchange` can lead to the [ABA problem].
3025            ///
3026            /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
3027            /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
3028            #[inline]
3029            #[$stable_cxchg]
3030            #[$cfg_cas]
3031            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3032            #[rustc_should_not_be_called_on_const_items]
3033            pub fn compare_exchange(&self,
3034                                    current: $int_type,
3035                                    new: $int_type,
3036                                    success: Ordering,
3037                                    failure: Ordering) -> Result<$int_type, $int_type> {
3038                // SAFETY: data races are prevented by atomic intrinsics.
3039                unsafe { atomic_compare_exchange(self.v.get(), current, new, success, failure) }
3040            }
3041
3042            /// Stores a value into the atomic integer if the current value is the same as
3043            /// the `current` value.
3044            ///
3045            #[doc = concat!("Unlike [`", stringify!($atomic_type), "::compare_exchange`],")]
3046            /// this function is allowed to spuriously fail even
3047            /// when the comparison succeeds, which can result in more efficient code on some
3048            /// platforms. The return value is a result indicating whether the new value was
3049            /// written and containing the previous value.
3050            ///
3051            /// `compare_exchange_weak` takes two [`Ordering`] arguments to describe the memory
3052            /// ordering of this operation. `success` describes the required ordering for the
3053            /// read-modify-write operation that takes place if the comparison with `current` succeeds.
3054            /// `failure` describes the required ordering for the load operation that takes place when
3055            /// the comparison fails. Using [`Acquire`] as success ordering makes the store part
3056            /// of this operation [`Relaxed`], and using [`Release`] makes the successful load
3057            /// [`Relaxed`]. The failure ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
3058            ///
3059            /// **Note**: This method is only available on platforms that support atomic operations on
3060            #[doc = concat!("[`", $s_int_type, "`].")]
3061            ///
3062            /// # Examples
3063            ///
3064            /// ```
3065            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3066            ///
3067            #[doc = concat!("let val = ", stringify!($atomic_type), "::new(4);")]
3068            ///
3069            /// let mut old = val.load(Ordering::Relaxed);
3070            /// loop {
3071            ///     let new = old * 2;
3072            ///     match val.compare_exchange_weak(old, new, Ordering::SeqCst, Ordering::Relaxed) {
3073            ///         Ok(_) => break,
3074            ///         Err(x) => old = x,
3075            ///     }
3076            /// }
3077            /// ```
3078            ///
3079            /// # Considerations
3080            ///
3081            /// `compare_exchange` is a [compare-and-swap operation] and thus exhibits the usual downsides
3082            /// of CAS operations. In particular, a load of the value followed by a successful
3083            /// `compare_exchange` with the previous load *does not ensure* that other threads have not
3084            /// changed the value in the interim. This is usually important when the *equality* check in
3085            /// the `compare_exchange` is being used to check the *identity* of a value, but equality
3086            /// does not necessarily imply identity. This is a particularly common case for pointers, as
3087            /// a pointer holding the same address does not imply that the same object exists at that
3088            /// address! In this case, `compare_exchange` can lead to the [ABA problem].
3089            ///
3090            /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
3091            /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
3092            #[inline]
3093            #[$stable_cxchg]
3094            #[$cfg_cas]
3095            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3096            #[rustc_should_not_be_called_on_const_items]
3097            pub fn compare_exchange_weak(&self,
3098                                         current: $int_type,
3099                                         new: $int_type,
3100                                         success: Ordering,
3101                                         failure: Ordering) -> Result<$int_type, $int_type> {
3102                // SAFETY: data races are prevented by atomic intrinsics.
3103                unsafe {
3104                    atomic_compare_exchange_weak(self.v.get(), current, new, success, failure)
3105                }
3106            }
3107
3108            /// Adds to the current value, returning the previous value.
3109            ///
3110            /// This operation wraps around on overflow.
3111            ///
3112            /// `fetch_add` takes an [`Ordering`] argument which describes the memory ordering
3113            /// of this operation. All ordering modes are possible. Note that using
3114            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3115            /// using [`Release`] makes the load part [`Relaxed`].
3116            ///
3117            /// **Note**: This method is only available on platforms that support atomic operations on
3118            #[doc = concat!("[`", $s_int_type, "`].")]
3119            ///
3120            /// # Examples
3121            ///
3122            /// ```
3123            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3124            ///
3125            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(0);")]
3126            /// assert_eq!(foo.fetch_add(10, Ordering::SeqCst), 0);
3127            /// assert_eq!(foo.load(Ordering::SeqCst), 10);
3128            /// ```
3129            #[inline]
3130            #[$stable]
3131            #[$cfg_cas]
3132            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3133            #[rustc_should_not_be_called_on_const_items]
3134            pub fn fetch_add(&self, val: $int_type, order: Ordering) -> $int_type {
3135                // SAFETY: data races are prevented by atomic intrinsics.
3136                unsafe { atomic_add(self.v.get(), val, order) }
3137            }
3138
3139            /// Subtracts from the current value, returning the previous value.
3140            ///
3141            /// This operation wraps around on overflow.
3142            ///
3143            /// `fetch_sub` takes an [`Ordering`] argument which describes the memory ordering
3144            /// of this operation. All ordering modes are possible. Note that using
3145            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3146            /// using [`Release`] makes the load part [`Relaxed`].
3147            ///
3148            /// **Note**: This method is only available on platforms that support atomic operations on
3149            #[doc = concat!("[`", $s_int_type, "`].")]
3150            ///
3151            /// # Examples
3152            ///
3153            /// ```
3154            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3155            ///
3156            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(20);")]
3157            /// assert_eq!(foo.fetch_sub(10, Ordering::SeqCst), 20);
3158            /// assert_eq!(foo.load(Ordering::SeqCst), 10);
3159            /// ```
3160            #[inline]
3161            #[$stable]
3162            #[$cfg_cas]
3163            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3164            #[rustc_should_not_be_called_on_const_items]
3165            pub fn fetch_sub(&self, val: $int_type, order: Ordering) -> $int_type {
3166                // SAFETY: data races are prevented by atomic intrinsics.
3167                unsafe { atomic_sub(self.v.get(), val, order) }
3168            }
3169
3170            /// Bitwise "and" with the current value.
3171            ///
3172            /// Performs a bitwise "and" operation on the current value and the argument `val`, and
3173            /// sets the new value to the result.
3174            ///
3175            /// Returns the previous value.
3176            ///
3177            /// `fetch_and` takes an [`Ordering`] argument which describes the memory ordering
3178            /// of this operation. All ordering modes are possible. Note that using
3179            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3180            /// using [`Release`] makes the load part [`Relaxed`].
3181            ///
3182            /// **Note**: This method is only available on platforms that support atomic operations on
3183            #[doc = concat!("[`", $s_int_type, "`].")]
3184            ///
3185            /// # Examples
3186            ///
3187            /// ```
3188            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3189            ///
3190            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(0b101101);")]
3191            /// assert_eq!(foo.fetch_and(0b110011, Ordering::SeqCst), 0b101101);
3192            /// assert_eq!(foo.load(Ordering::SeqCst), 0b100001);
3193            /// ```
3194            #[inline]
3195            #[$stable]
3196            #[$cfg_cas]
3197            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3198            #[rustc_should_not_be_called_on_const_items]
3199            pub fn fetch_and(&self, val: $int_type, order: Ordering) -> $int_type {
3200                // SAFETY: data races are prevented by atomic intrinsics.
3201                unsafe { atomic_and(self.v.get(), val, order) }
3202            }
3203
3204            /// Bitwise "nand" with the current value.
3205            ///
3206            /// Performs a bitwise "nand" operation on the current value and the argument `val`, and
3207            /// sets the new value to the result.
3208            ///
3209            /// Returns the previous value.
3210            ///
3211            /// `fetch_nand` takes an [`Ordering`] argument which describes the memory ordering
3212            /// of this operation. All ordering modes are possible. Note that using
3213            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3214            /// using [`Release`] makes the load part [`Relaxed`].
3215            ///
3216            /// **Note**: This method is only available on platforms that support atomic operations on
3217            #[doc = concat!("[`", $s_int_type, "`].")]
3218            ///
3219            /// # Examples
3220            ///
3221            /// ```
3222            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3223            ///
3224            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(0x13);")]
3225            /// assert_eq!(foo.fetch_nand(0x31, Ordering::SeqCst), 0x13);
3226            /// assert_eq!(foo.load(Ordering::SeqCst), !(0x13 & 0x31));
3227            /// ```
3228            #[inline]
3229            #[$stable_nand]
3230            #[$cfg_cas]
3231            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3232            #[rustc_should_not_be_called_on_const_items]
3233            pub fn fetch_nand(&self, val: $int_type, order: Ordering) -> $int_type {
3234                // SAFETY: data races are prevented by atomic intrinsics.
3235                unsafe { atomic_nand(self.v.get(), val, order) }
3236            }
3237
3238            /// Bitwise "or" with the current value.
3239            ///
3240            /// Performs a bitwise "or" operation on the current value and the argument `val`, and
3241            /// sets the new value to the result.
3242            ///
3243            /// Returns the previous value.
3244            ///
3245            /// `fetch_or` takes an [`Ordering`] argument which describes the memory ordering
3246            /// of this operation. All ordering modes are possible. Note that using
3247            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3248            /// using [`Release`] makes the load part [`Relaxed`].
3249            ///
3250            /// **Note**: This method is only available on platforms that support atomic operations on
3251            #[doc = concat!("[`", $s_int_type, "`].")]
3252            ///
3253            /// # Examples
3254            ///
3255            /// ```
3256            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3257            ///
3258            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(0b101101);")]
3259            /// assert_eq!(foo.fetch_or(0b110011, Ordering::SeqCst), 0b101101);
3260            /// assert_eq!(foo.load(Ordering::SeqCst), 0b111111);
3261            /// ```
3262            #[inline]
3263            #[$stable]
3264            #[$cfg_cas]
3265            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3266            #[rustc_should_not_be_called_on_const_items]
3267            pub fn fetch_or(&self, val: $int_type, order: Ordering) -> $int_type {
3268                // SAFETY: data races are prevented by atomic intrinsics.
3269                unsafe { atomic_or(self.v.get(), val, order) }
3270            }
3271
3272            /// Bitwise "xor" with the current value.
3273            ///
3274            /// Performs a bitwise "xor" operation on the current value and the argument `val`, and
3275            /// sets the new value to the result.
3276            ///
3277            /// Returns the previous value.
3278            ///
3279            /// `fetch_xor` takes an [`Ordering`] argument which describes the memory ordering
3280            /// of this operation. All ordering modes are possible. Note that using
3281            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3282            /// using [`Release`] makes the load part [`Relaxed`].
3283            ///
3284            /// **Note**: This method is only available on platforms that support atomic operations on
3285            #[doc = concat!("[`", $s_int_type, "`].")]
3286            ///
3287            /// # Examples
3288            ///
3289            /// ```
3290            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3291            ///
3292            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(0b101101);")]
3293            /// assert_eq!(foo.fetch_xor(0b110011, Ordering::SeqCst), 0b101101);
3294            /// assert_eq!(foo.load(Ordering::SeqCst), 0b011110);
3295            /// ```
3296            #[inline]
3297            #[$stable]
3298            #[$cfg_cas]
3299            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3300            #[rustc_should_not_be_called_on_const_items]
3301            pub fn fetch_xor(&self, val: $int_type, order: Ordering) -> $int_type {
3302                // SAFETY: data races are prevented by atomic intrinsics.
3303                unsafe { atomic_xor(self.v.get(), val, order) }
3304            }
3305
3306            /// An alias for
3307            #[doc = concat!("[`", stringify!($atomic_type), "::try_update`]")]
3308            /// .
3309            #[inline]
3310            #[stable(feature = "no_more_cas", since = "1.45.0")]
3311            #[$cfg_cas]
3312            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3313            #[rustc_should_not_be_called_on_const_items]
3314            #[deprecated(
3315                since = "1.99.0",
3316                note = "renamed to `try_update` for consistency",
3317                suggestion = "try_update"
3318            )]
3319            pub fn fetch_update<F>(&self,
3320                                   set_order: Ordering,
3321                                   fetch_order: Ordering,
3322                                   f: F) -> Result<$int_type, $int_type>
3323            where F: FnMut($int_type) -> Option<$int_type> {
3324                self.try_update(set_order, fetch_order, f)
3325            }
3326
3327            /// Fetches the value, and applies a function to it that returns an optional
3328            /// new value. Returns a `Result` of `Ok(previous_value)` if the function returned `Some(_)`, else
3329            /// `Err(previous_value)`.
3330            ///
3331            #[doc = concat!("See also: [`update`](`", stringify!($atomic_type), "::update`).")]
3332            ///
3333            /// Note: This may call the function multiple times if the value has been changed from other threads in
3334            /// the meantime, as long as the function returns `Some(_)`, but the function will have been applied
3335            /// only once to the stored value.
3336            ///
3337            /// `try_update` takes two [`Ordering`] arguments to describe the memory ordering of this operation.
3338            /// The first describes the required ordering for when the operation finally succeeds while the second
3339            /// describes the required ordering for loads. These correspond to the success and failure orderings of
3340            #[doc = concat!("[`", stringify!($atomic_type), "::compare_exchange`]")]
3341            /// respectively.
3342            ///
3343            /// Using [`Acquire`] as success ordering makes the store part
3344            /// of this operation [`Relaxed`], and using [`Release`] makes the final successful load
3345            /// [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
3346            ///
3347            /// **Note**: This method is only available on platforms that support atomic operations on
3348            #[doc = concat!("[`", $s_int_type, "`].")]
3349            ///
3350            /// # Considerations
3351            ///
3352            /// This method is not magic; it is not provided by the hardware, and does not act like a
3353            /// critical section or mutex.
3354            ///
3355            /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
3356            /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem]
3357            /// if this atomic integer is an index or more generally if knowledge of only the *bitwise value*
3358            /// of the atomic is not in and of itself sufficient to ensure any required preconditions.
3359            ///
3360            /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
3361            /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
3362            ///
3363            /// # Examples
3364            ///
3365            /// ```rust
3366            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3367            ///
3368            #[doc = concat!("let x = ", stringify!($atomic_type), "::new(7);")]
3369            /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |_| None), Err(7));
3370            /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(x + 1)), Ok(7));
3371            /// assert_eq!(x.try_update(Ordering::SeqCst, Ordering::SeqCst, |x| Some(x + 1)), Ok(8));
3372            /// assert_eq!(x.load(Ordering::SeqCst), 9);
3373            /// ```
3374            #[inline]
3375            #[stable(feature = "atomic_try_update", since = "1.95.0")]
3376            #[$cfg_cas]
3377            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3378            #[rustc_should_not_be_called_on_const_items]
3379            pub fn try_update(
3380                &self,
3381                set_order: Ordering,
3382                fetch_order: Ordering,
3383                mut f: impl FnMut($int_type) -> Option<$int_type>,
3384            ) -> Result<$int_type, $int_type> {
3385                let mut prev = self.load(fetch_order);
3386                while let Some(next) = f(prev) {
3387                    match self.compare_exchange_weak(prev, next, set_order, fetch_order) {
3388                        x @ Ok(_) => return x,
3389                        Err(next_prev) => prev = next_prev
3390                    }
3391                }
3392                Err(prev)
3393            }
3394
3395            /// Fetches the value, applies a function to it that it return a new value.
3396            /// The new value is stored and the old value is returned.
3397            ///
3398            #[doc = concat!("See also: [`try_update`](`", stringify!($atomic_type), "::try_update`).")]
3399            ///
3400            /// Note: This may call the function multiple times if the value has been changed from other threads in
3401            /// the meantime, but the function will have been applied only once to the stored value.
3402            ///
3403            /// `update` takes two [`Ordering`] arguments to describe the memory ordering of this operation.
3404            /// The first describes the required ordering for when the operation finally succeeds while the second
3405            /// describes the required ordering for loads. These correspond to the success and failure orderings of
3406            #[doc = concat!("[`", stringify!($atomic_type), "::compare_exchange`]")]
3407            /// respectively.
3408            ///
3409            /// Using [`Acquire`] as success ordering makes the store part
3410            /// of this operation [`Relaxed`], and using [`Release`] makes the final successful load
3411            /// [`Relaxed`]. The (failed) load ordering can only be [`SeqCst`], [`Acquire`] or [`Relaxed`].
3412            ///
3413            /// **Note**: This method is only available on platforms that support atomic operations on
3414            #[doc = concat!("[`", $s_int_type, "`].")]
3415            ///
3416            /// # Considerations
3417            ///
3418            /// [CAS operation]: https://en.wikipedia.org/wiki/Compare-and-swap
3419            /// This method is not magic; it is not provided by the hardware, and does not act like a
3420            /// critical section or mutex.
3421            ///
3422            /// It is implemented on top of an atomic [compare-and-swap operation], and thus is subject to
3423            /// the usual drawbacks of CAS operations. In particular, be careful of the [ABA problem]
3424            /// if this atomic integer is an index or more generally if knowledge of only the *bitwise value*
3425            /// of the atomic is not in and of itself sufficient to ensure any required preconditions.
3426            ///
3427            /// [ABA Problem]: https://en.wikipedia.org/wiki/ABA_problem
3428            /// [compare-and-swap operation]: https://en.wikipedia.org/wiki/Compare-and-swap
3429            ///
3430            /// # Examples
3431            ///
3432            /// ```rust
3433            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3434            ///
3435            #[doc = concat!("let x = ", stringify!($atomic_type), "::new(7);")]
3436            /// assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| x + 1), 7);
3437            /// assert_eq!(x.update(Ordering::SeqCst, Ordering::SeqCst, |x| x + 1), 8);
3438            /// assert_eq!(x.load(Ordering::SeqCst), 9);
3439            /// ```
3440            #[inline]
3441            #[stable(feature = "atomic_try_update", since = "1.95.0")]
3442            #[$cfg_cas]
3443            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3444            #[rustc_should_not_be_called_on_const_items]
3445            pub fn update(
3446                &self,
3447                set_order: Ordering,
3448                fetch_order: Ordering,
3449                mut f: impl FnMut($int_type) -> $int_type,
3450            ) -> $int_type {
3451                let mut prev = self.load(fetch_order);
3452                loop {
3453                    match self.compare_exchange_weak(prev, f(prev), set_order, fetch_order) {
3454                        Ok(x) => break x,
3455                        Err(next_prev) => prev = next_prev,
3456                    }
3457                }
3458            }
3459
3460            /// Maximum with the current value.
3461            ///
3462            /// Finds the maximum of the current value and the argument `val`, and
3463            /// sets the new value to the result.
3464            ///
3465            /// Returns the previous value.
3466            ///
3467            /// `fetch_max` takes an [`Ordering`] argument which describes the memory ordering
3468            /// of this operation. All ordering modes are possible. Note that using
3469            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3470            /// using [`Release`] makes the load part [`Relaxed`].
3471            ///
3472            /// **Note**: This method is only available on platforms that support atomic operations on
3473            #[doc = concat!("[`", $s_int_type, "`].")]
3474            ///
3475            /// # Examples
3476            ///
3477            /// ```
3478            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3479            ///
3480            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(23);")]
3481            /// assert_eq!(foo.fetch_max(42, Ordering::SeqCst), 23);
3482            /// assert_eq!(foo.load(Ordering::SeqCst), 42);
3483            /// ```
3484            ///
3485            /// If you want to obtain the maximum value in one step, you can use the following:
3486            ///
3487            /// ```
3488            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3489            ///
3490            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(23);")]
3491            /// let bar = 42;
3492            /// let max_foo = foo.fetch_max(bar, Ordering::SeqCst).max(bar);
3493            /// assert!(max_foo == 42);
3494            /// ```
3495            #[inline]
3496            #[stable(feature = "atomic_min_max", since = "1.45.0")]
3497            #[$cfg_cas]
3498            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3499            #[rustc_should_not_be_called_on_const_items]
3500            pub fn fetch_max(&self, val: $int_type, order: Ordering) -> $int_type {
3501                // SAFETY: data races are prevented by atomic intrinsics.
3502                unsafe { $max_fn(self.v.get(), val, order) }
3503            }
3504
3505            /// Minimum with the current value.
3506            ///
3507            /// Finds the minimum of the current value and the argument `val`, and
3508            /// sets the new value to the result.
3509            ///
3510            /// Returns the previous value.
3511            ///
3512            /// `fetch_min` takes an [`Ordering`] argument which describes the memory ordering
3513            /// of this operation. All ordering modes are possible. Note that using
3514            /// [`Acquire`] makes the store part of this operation [`Relaxed`], and
3515            /// using [`Release`] makes the load part [`Relaxed`].
3516            ///
3517            /// **Note**: This method is only available on platforms that support atomic operations on
3518            #[doc = concat!("[`", $s_int_type, "`].")]
3519            ///
3520            /// # Examples
3521            ///
3522            /// ```
3523            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3524            ///
3525            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(23);")]
3526            /// assert_eq!(foo.fetch_min(42, Ordering::Relaxed), 23);
3527            /// assert_eq!(foo.load(Ordering::Relaxed), 23);
3528            /// assert_eq!(foo.fetch_min(22, Ordering::Relaxed), 23);
3529            /// assert_eq!(foo.load(Ordering::Relaxed), 22);
3530            /// ```
3531            ///
3532            /// If you want to obtain the minimum value in one step, you can use the following:
3533            ///
3534            /// ```
3535            #[doc = concat!($extra_feature, "use std::sync::atomic::{", stringify!($atomic_type), ", Ordering};")]
3536            ///
3537            #[doc = concat!("let foo = ", stringify!($atomic_type), "::new(23);")]
3538            /// let bar = 12;
3539            /// let min_foo = foo.fetch_min(bar, Ordering::SeqCst).min(bar);
3540            /// assert_eq!(min_foo, 12);
3541            /// ```
3542            #[inline]
3543            #[stable(feature = "atomic_min_max", since = "1.45.0")]
3544            #[$cfg_cas]
3545            #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3546            #[rustc_should_not_be_called_on_const_items]
3547            pub fn fetch_min(&self, val: $int_type, order: Ordering) -> $int_type {
3548                // SAFETY: data races are prevented by atomic intrinsics.
3549                unsafe { $min_fn(self.v.get(), val, order) }
3550            }
3551
3552            /// Returns a mutable pointer to the underlying integer.
3553            ///
3554            /// Doing non-atomic reads and writes on the resulting integer can be a data race.
3555            /// This method is mostly useful for FFI, where the function signature may use
3556            #[doc = concat!("`*mut ", stringify!($int_type), "` instead of `&", stringify!($atomic_type), "`.")]
3557            ///
3558            /// Returning an `*mut` pointer from a shared reference to this atomic is safe because the
3559            /// atomic types work with interior mutability. All modifications of an atomic change the value
3560            /// through a shared reference, and can do so safely as long as they use atomic operations. Any
3561            /// use of the returned raw pointer requires an `unsafe` block and still has to uphold the
3562            /// requirements of the [memory model].
3563            ///
3564            /// # Examples
3565            ///
3566            /// ```ignore (extern-declaration)
3567            /// # fn main() {
3568            #[doc = concat!($extra_feature, "use std::sync::atomic::", stringify!($atomic_type), ";")]
3569            ///
3570            /// extern "C" {
3571            #[doc = concat!("    fn my_atomic_op(arg: *mut ", stringify!($int_type), ");")]
3572            /// }
3573            ///
3574            #[doc = concat!("let atomic = ", stringify!($atomic_type), "::new(1);")]
3575            ///
3576            /// // SAFETY: Safe as long as `my_atomic_op` is atomic.
3577            /// unsafe {
3578            ///     my_atomic_op(atomic.as_ptr());
3579            /// }
3580            /// # }
3581            /// ```
3582            ///
3583            /// [memory model]: self#memory-model-for-atomic-accesses
3584            #[inline]
3585            #[stable(feature = "atomic_as_ptr", since = "1.70.0")]
3586            #[rustc_const_stable(feature = "atomic_as_ptr", since = "1.70.0")]
3587            #[rustc_never_returns_null_ptr]
3588            pub const fn as_ptr(&self) -> *mut $int_type {
3589                self.v.get()
3590            }
3591        }
3592    }
3593}
3594
3595#[cfg(target_has_atomic_load_store = "8")]
3596atomic_int! {
3597    cfg(target_has_atomic = "8"),
3598    cfg(target_has_atomic_equal_alignment = "8"),
3599    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3600    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3601    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3602    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3603    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3604    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3605    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3606    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3607    rustc_diagnostic_item = "AtomicI8",
3608    "i8",
3609    "",
3610    atomic_min, atomic_max,
3611    1,
3612    i8 AtomicI8
3613}
3614#[cfg(target_has_atomic_load_store = "8")]
3615atomic_int! {
3616    cfg(target_has_atomic = "8"),
3617    cfg(target_has_atomic_equal_alignment = "8"),
3618    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3619    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3620    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3621    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3622    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3623    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3624    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3625    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3626    rustc_diagnostic_item = "AtomicU8",
3627    "u8",
3628    "",
3629    atomic_umin, atomic_umax,
3630    1,
3631    u8 AtomicU8
3632}
3633#[cfg(target_has_atomic_load_store = "16")]
3634atomic_int! {
3635    cfg(target_has_atomic = "16"),
3636    cfg(target_has_atomic_equal_alignment = "16"),
3637    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3638    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3639    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3640    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3641    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3642    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3643    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3644    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3645    rustc_diagnostic_item = "AtomicI16",
3646    "i16",
3647    "",
3648    atomic_min, atomic_max,
3649    2,
3650    i16 AtomicI16
3651}
3652#[cfg(target_has_atomic_load_store = "16")]
3653atomic_int! {
3654    cfg(target_has_atomic = "16"),
3655    cfg(target_has_atomic_equal_alignment = "16"),
3656    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3657    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3658    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3659    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3660    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3661    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3662    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3663    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3664    rustc_diagnostic_item = "AtomicU16",
3665    "u16",
3666    "",
3667    atomic_umin, atomic_umax,
3668    2,
3669    u16 AtomicU16
3670}
3671#[cfg(target_has_atomic_load_store = "32")]
3672atomic_int! {
3673    cfg(target_has_atomic = "32"),
3674    cfg(target_has_atomic_equal_alignment = "32"),
3675    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3676    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3677    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3678    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3679    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3680    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3681    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3682    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3683    rustc_diagnostic_item = "AtomicI32",
3684    "i32",
3685    "",
3686    atomic_min, atomic_max,
3687    4,
3688    i32 AtomicI32
3689}
3690#[cfg(target_has_atomic_load_store = "32")]
3691atomic_int! {
3692    cfg(target_has_atomic = "32"),
3693    cfg(target_has_atomic_equal_alignment = "32"),
3694    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3695    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3696    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3697    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3698    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3699    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3700    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3701    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3702    rustc_diagnostic_item = "AtomicU32",
3703    "u32",
3704    "",
3705    atomic_umin, atomic_umax,
3706    4,
3707    u32 AtomicU32
3708}
3709#[cfg(target_has_atomic_load_store = "64")]
3710atomic_int! {
3711    cfg(target_has_atomic = "64"),
3712    cfg(target_has_atomic_equal_alignment = "64"),
3713    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3714    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3715    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3716    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3717    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3718    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3719    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3720    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3721    rustc_diagnostic_item = "AtomicI64",
3722    "i64",
3723    "",
3724    atomic_min, atomic_max,
3725    8,
3726    i64 AtomicI64
3727}
3728#[cfg(target_has_atomic_load_store = "64")]
3729atomic_int! {
3730    cfg(target_has_atomic = "64"),
3731    cfg(target_has_atomic_equal_alignment = "64"),
3732    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3733    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3734    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3735    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3736    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3737    stable(feature = "integer_atomics_stable", since = "1.34.0"),
3738    rustc_const_stable(feature = "const_integer_atomics", since = "1.34.0"),
3739    rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3740    rustc_diagnostic_item = "AtomicU64",
3741    "u64",
3742    "",
3743    atomic_umin, atomic_umax,
3744    8,
3745    u64 AtomicU64
3746}
3747#[cfg(target_has_atomic_load_store = "128")]
3748atomic_int! {
3749    cfg(target_has_atomic = "128"),
3750    cfg(target_has_atomic_equal_alignment = "128"),
3751    unstable(feature = "integer_atomics", issue = "99069"),
3752    unstable(feature = "integer_atomics", issue = "99069"),
3753    unstable(feature = "integer_atomics", issue = "99069"),
3754    unstable(feature = "integer_atomics", issue = "99069"),
3755    unstable(feature = "integer_atomics", issue = "99069"),
3756    unstable(feature = "integer_atomics", issue = "99069"),
3757    rustc_const_unstable(feature = "integer_atomics", issue = "99069"),
3758    rustc_const_unstable(feature = "integer_atomics", issue = "99069"),
3759    rustc_diagnostic_item = "AtomicI128",
3760    "i128",
3761    "#![feature(integer_atomics)]\n\n",
3762    atomic_min, atomic_max,
3763    16,
3764    i128 AtomicI128
3765}
3766#[cfg(target_has_atomic_load_store = "128")]
3767atomic_int! {
3768    cfg(target_has_atomic = "128"),
3769    cfg(target_has_atomic_equal_alignment = "128"),
3770    unstable(feature = "integer_atomics", issue = "99069"),
3771    unstable(feature = "integer_atomics", issue = "99069"),
3772    unstable(feature = "integer_atomics", issue = "99069"),
3773    unstable(feature = "integer_atomics", issue = "99069"),
3774    unstable(feature = "integer_atomics", issue = "99069"),
3775    unstable(feature = "integer_atomics", issue = "99069"),
3776    rustc_const_unstable(feature = "integer_atomics", issue = "99069"),
3777    rustc_const_unstable(feature = "integer_atomics", issue = "99069"),
3778    rustc_diagnostic_item = "AtomicU128",
3779    "u128",
3780    "#![feature(integer_atomics)]\n\n",
3781    atomic_umin, atomic_umax,
3782    16,
3783    u128 AtomicU128
3784}
3785
3786#[cfg(target_has_atomic_load_store = "ptr")]
3787macro_rules! atomic_int_ptr_sized {
3788    ( $($target_pointer_width:literal $align:literal)* ) => { $(
3789        #[cfg(target_pointer_width = $target_pointer_width)]
3790        atomic_int! {
3791            cfg(target_has_atomic = "ptr"),
3792            cfg(target_has_atomic_equal_alignment = "ptr"),
3793            stable(feature = "rust1", since = "1.0.0"),
3794            stable(feature = "extended_compare_and_swap", since = "1.10.0"),
3795            stable(feature = "atomic_debug", since = "1.3.0"),
3796            stable(feature = "atomic_access", since = "1.15.0"),
3797            stable(feature = "atomic_from", since = "1.23.0"),
3798            stable(feature = "atomic_nand", since = "1.27.0"),
3799            rustc_const_stable(feature = "const_ptr_sized_atomics", since = "1.24.0"),
3800            rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3801            rustc_diagnostic_item = "AtomicIsize",
3802            "isize",
3803            "",
3804            atomic_min, atomic_max,
3805            $align,
3806            isize AtomicIsize
3807        }
3808        #[cfg(target_pointer_width = $target_pointer_width)]
3809        atomic_int! {
3810            cfg(target_has_atomic = "ptr"),
3811            cfg(target_has_atomic_equal_alignment = "ptr"),
3812            stable(feature = "rust1", since = "1.0.0"),
3813            stable(feature = "extended_compare_and_swap", since = "1.10.0"),
3814            stable(feature = "atomic_debug", since = "1.3.0"),
3815            stable(feature = "atomic_access", since = "1.15.0"),
3816            stable(feature = "atomic_from", since = "1.23.0"),
3817            stable(feature = "atomic_nand", since = "1.27.0"),
3818            rustc_const_stable(feature = "const_ptr_sized_atomics", since = "1.24.0"),
3819            rustc_const_stable(feature = "const_atomic_into_inner", since = "1.79.0"),
3820            rustc_diagnostic_item = "AtomicUsize",
3821            "usize",
3822            "",
3823            atomic_umin, atomic_umax,
3824            $align,
3825            usize AtomicUsize
3826        }
3827
3828        /// An [`AtomicIsize`] initialized to `0`.
3829        #[cfg(target_pointer_width = $target_pointer_width)]
3830        #[stable(feature = "rust1", since = "1.0.0")]
3831        #[deprecated(
3832            since = "1.34.0",
3833            note = "the `new` function is now preferred",
3834            suggestion = "AtomicIsize::new(0)",
3835        )]
3836        pub const ATOMIC_ISIZE_INIT: AtomicIsize = AtomicIsize::new(0);
3837
3838        /// An [`AtomicUsize`] initialized to `0`.
3839        #[cfg(target_pointer_width = $target_pointer_width)]
3840        #[stable(feature = "rust1", since = "1.0.0")]
3841        #[deprecated(
3842            since = "1.34.0",
3843            note = "the `new` function is now preferred",
3844            suggestion = "AtomicUsize::new(0)",
3845        )]
3846        pub const ATOMIC_USIZE_INIT: AtomicUsize = AtomicUsize::new(0);
3847    )* };
3848}
3849
3850#[cfg(target_has_atomic_load_store = "ptr")]
3851atomic_int_ptr_sized! {
3852    "16" 2
3853    "32" 4
3854    "64" 8
3855}
3856
3857#[inline]
3858#[cfg(target_has_atomic)]
3859fn strongest_failure_ordering(order: Ordering) -> Ordering {
3860    match order {
3861        Release => Relaxed,
3862        Relaxed => Relaxed,
3863        SeqCst => SeqCst,
3864        Acquire => Acquire,
3865        AcqRel => Acquire,
3866    }
3867}
3868
3869#[inline]
3870#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3871unsafe fn atomic_store<T: Copy>(dst: *mut T, val: T, order: Ordering) {
3872    // SAFETY: the caller must uphold the safety contract for `atomic_store`.
3873    unsafe {
3874        match order {
3875            Relaxed => intrinsics::atomic_store::<T, { AO::Relaxed }>(dst, val),
3876            Release => intrinsics::atomic_store::<T, { AO::Release }>(dst, val),
3877            SeqCst => intrinsics::atomic_store::<T, { AO::SeqCst }>(dst, val),
3878            Acquire => panic!("there is no such thing as an acquire store"),
3879            AcqRel => panic!("there is no such thing as an acquire-release store"),
3880        }
3881    }
3882}
3883
3884#[inline]
3885#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3886unsafe fn atomic_load<T: Copy>(dst: *const T, order: Ordering) -> T {
3887    // SAFETY: the caller must uphold the safety contract for `atomic_load`.
3888    unsafe {
3889        match order {
3890            Relaxed => intrinsics::atomic_load::<T, { AO::Relaxed }>(dst),
3891            Acquire => intrinsics::atomic_load::<T, { AO::Acquire }>(dst),
3892            SeqCst => intrinsics::atomic_load::<T, { AO::SeqCst }>(dst),
3893            Release => panic!("there is no such thing as a release load"),
3894            AcqRel => panic!("there is no such thing as an acquire-release load"),
3895        }
3896    }
3897}
3898
3899#[inline]
3900#[cfg(target_has_atomic)]
3901#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3902unsafe fn atomic_swap<T: Copy>(dst: *mut T, val: T, order: Ordering) -> T {
3903    // SAFETY: the caller must uphold the safety contract for `atomic_swap`.
3904    unsafe {
3905        match order {
3906            Relaxed => intrinsics::atomic_xchg::<T, { AO::Relaxed }>(dst, val),
3907            Acquire => intrinsics::atomic_xchg::<T, { AO::Acquire }>(dst, val),
3908            Release => intrinsics::atomic_xchg::<T, { AO::Release }>(dst, val),
3909            AcqRel => intrinsics::atomic_xchg::<T, { AO::AcqRel }>(dst, val),
3910            SeqCst => intrinsics::atomic_xchg::<T, { AO::SeqCst }>(dst, val),
3911        }
3912    }
3913}
3914
3915/// Returns the previous value (like __sync_fetch_and_add).
3916#[inline]
3917#[cfg(target_has_atomic)]
3918#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3919unsafe fn atomic_add<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
3920    // SAFETY: the caller must uphold the safety contract for `atomic_add`.
3921    unsafe {
3922        match order {
3923            Relaxed => intrinsics::atomic_xadd::<T, U, { AO::Relaxed }>(dst, val),
3924            Acquire => intrinsics::atomic_xadd::<T, U, { AO::Acquire }>(dst, val),
3925            Release => intrinsics::atomic_xadd::<T, U, { AO::Release }>(dst, val),
3926            AcqRel => intrinsics::atomic_xadd::<T, U, { AO::AcqRel }>(dst, val),
3927            SeqCst => intrinsics::atomic_xadd::<T, U, { AO::SeqCst }>(dst, val),
3928        }
3929    }
3930}
3931
3932/// Returns the previous value (like __sync_fetch_and_sub).
3933#[inline]
3934#[cfg(target_has_atomic)]
3935#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3936unsafe fn atomic_sub<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
3937    // SAFETY: the caller must uphold the safety contract for `atomic_sub`.
3938    unsafe {
3939        match order {
3940            Relaxed => intrinsics::atomic_xsub::<T, U, { AO::Relaxed }>(dst, val),
3941            Acquire => intrinsics::atomic_xsub::<T, U, { AO::Acquire }>(dst, val),
3942            Release => intrinsics::atomic_xsub::<T, U, { AO::Release }>(dst, val),
3943            AcqRel => intrinsics::atomic_xsub::<T, U, { AO::AcqRel }>(dst, val),
3944            SeqCst => intrinsics::atomic_xsub::<T, U, { AO::SeqCst }>(dst, val),
3945        }
3946    }
3947}
3948
3949/// Publicly exposed for stdarch; nobody else should use this.
3950#[inline]
3951#[cfg(target_has_atomic)]
3952#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
3953#[unstable(feature = "core_intrinsics", issue = "none")]
3954#[doc(hidden)]
3955pub unsafe fn atomic_compare_exchange<T: Copy>(
3956    dst: *mut T,
3957    old: T,
3958    new: T,
3959    success: Ordering,
3960    failure: Ordering,
3961) -> Result<T, T> {
3962    // SAFETY: the caller must uphold the safety contract for `atomic_compare_exchange`.
3963    let (val, ok) = unsafe {
3964        match (success, failure) {
3965            (Relaxed, Relaxed) => {
3966                intrinsics::atomic_cxchg::<T, { AO::Relaxed }, { AO::Relaxed }>(dst, old, new)
3967            }
3968            (Relaxed, Acquire) => {
3969                intrinsics::atomic_cxchg::<T, { AO::Relaxed }, { AO::Acquire }>(dst, old, new)
3970            }
3971            (Relaxed, SeqCst) => {
3972                intrinsics::atomic_cxchg::<T, { AO::Relaxed }, { AO::SeqCst }>(dst, old, new)
3973            }
3974            (Acquire, Relaxed) => {
3975                intrinsics::atomic_cxchg::<T, { AO::Acquire }, { AO::Relaxed }>(dst, old, new)
3976            }
3977            (Acquire, Acquire) => {
3978                intrinsics::atomic_cxchg::<T, { AO::Acquire }, { AO::Acquire }>(dst, old, new)
3979            }
3980            (Acquire, SeqCst) => {
3981                intrinsics::atomic_cxchg::<T, { AO::Acquire }, { AO::SeqCst }>(dst, old, new)
3982            }
3983            (Release, Relaxed) => {
3984                intrinsics::atomic_cxchg::<T, { AO::Release }, { AO::Relaxed }>(dst, old, new)
3985            }
3986            (Release, Acquire) => {
3987                intrinsics::atomic_cxchg::<T, { AO::Release }, { AO::Acquire }>(dst, old, new)
3988            }
3989            (Release, SeqCst) => {
3990                intrinsics::atomic_cxchg::<T, { AO::Release }, { AO::SeqCst }>(dst, old, new)
3991            }
3992            (AcqRel, Relaxed) => {
3993                intrinsics::atomic_cxchg::<T, { AO::AcqRel }, { AO::Relaxed }>(dst, old, new)
3994            }
3995            (AcqRel, Acquire) => {
3996                intrinsics::atomic_cxchg::<T, { AO::AcqRel }, { AO::Acquire }>(dst, old, new)
3997            }
3998            (AcqRel, SeqCst) => {
3999                intrinsics::atomic_cxchg::<T, { AO::AcqRel }, { AO::SeqCst }>(dst, old, new)
4000            }
4001            (SeqCst, Relaxed) => {
4002                intrinsics::atomic_cxchg::<T, { AO::SeqCst }, { AO::Relaxed }>(dst, old, new)
4003            }
4004            (SeqCst, Acquire) => {
4005                intrinsics::atomic_cxchg::<T, { AO::SeqCst }, { AO::Acquire }>(dst, old, new)
4006            }
4007            (SeqCst, SeqCst) => {
4008                intrinsics::atomic_cxchg::<T, { AO::SeqCst }, { AO::SeqCst }>(dst, old, new)
4009            }
4010            (_, AcqRel) => panic!("there is no such thing as an acquire-release failure ordering"),
4011            (_, Release) => panic!("there is no such thing as a release failure ordering"),
4012        }
4013    };
4014    if ok { Ok(val) } else { Err(val) }
4015}
4016
4017#[inline]
4018#[cfg(target_has_atomic)]
4019#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4020unsafe fn atomic_compare_exchange_weak<T: Copy>(
4021    dst: *mut T,
4022    old: T,
4023    new: T,
4024    success: Ordering,
4025    failure: Ordering,
4026) -> Result<T, T> {
4027    // SAFETY: the caller must uphold the safety contract for `atomic_compare_exchange_weak`.
4028    let (val, ok) = unsafe {
4029        match (success, failure) {
4030            (Relaxed, Relaxed) => {
4031                intrinsics::atomic_cxchgweak::<T, { AO::Relaxed }, { AO::Relaxed }>(dst, old, new)
4032            }
4033            (Relaxed, Acquire) => {
4034                intrinsics::atomic_cxchgweak::<T, { AO::Relaxed }, { AO::Acquire }>(dst, old, new)
4035            }
4036            (Relaxed, SeqCst) => {
4037                intrinsics::atomic_cxchgweak::<T, { AO::Relaxed }, { AO::SeqCst }>(dst, old, new)
4038            }
4039            (Acquire, Relaxed) => {
4040                intrinsics::atomic_cxchgweak::<T, { AO::Acquire }, { AO::Relaxed }>(dst, old, new)
4041            }
4042            (Acquire, Acquire) => {
4043                intrinsics::atomic_cxchgweak::<T, { AO::Acquire }, { AO::Acquire }>(dst, old, new)
4044            }
4045            (Acquire, SeqCst) => {
4046                intrinsics::atomic_cxchgweak::<T, { AO::Acquire }, { AO::SeqCst }>(dst, old, new)
4047            }
4048            (Release, Relaxed) => {
4049                intrinsics::atomic_cxchgweak::<T, { AO::Release }, { AO::Relaxed }>(dst, old, new)
4050            }
4051            (Release, Acquire) => {
4052                intrinsics::atomic_cxchgweak::<T, { AO::Release }, { AO::Acquire }>(dst, old, new)
4053            }
4054            (Release, SeqCst) => {
4055                intrinsics::atomic_cxchgweak::<T, { AO::Release }, { AO::SeqCst }>(dst, old, new)
4056            }
4057            (AcqRel, Relaxed) => {
4058                intrinsics::atomic_cxchgweak::<T, { AO::AcqRel }, { AO::Relaxed }>(dst, old, new)
4059            }
4060            (AcqRel, Acquire) => {
4061                intrinsics::atomic_cxchgweak::<T, { AO::AcqRel }, { AO::Acquire }>(dst, old, new)
4062            }
4063            (AcqRel, SeqCst) => {
4064                intrinsics::atomic_cxchgweak::<T, { AO::AcqRel }, { AO::SeqCst }>(dst, old, new)
4065            }
4066            (SeqCst, Relaxed) => {
4067                intrinsics::atomic_cxchgweak::<T, { AO::SeqCst }, { AO::Relaxed }>(dst, old, new)
4068            }
4069            (SeqCst, Acquire) => {
4070                intrinsics::atomic_cxchgweak::<T, { AO::SeqCst }, { AO::Acquire }>(dst, old, new)
4071            }
4072            (SeqCst, SeqCst) => {
4073                intrinsics::atomic_cxchgweak::<T, { AO::SeqCst }, { AO::SeqCst }>(dst, old, new)
4074            }
4075            (_, AcqRel) => panic!("there is no such thing as an acquire-release failure ordering"),
4076            (_, Release) => panic!("there is no such thing as a release failure ordering"),
4077        }
4078    };
4079    if ok { Ok(val) } else { Err(val) }
4080}
4081
4082#[inline]
4083#[cfg(target_has_atomic)]
4084#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4085unsafe fn atomic_and<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
4086    // SAFETY: the caller must uphold the safety contract for `atomic_and`
4087    unsafe {
4088        match order {
4089            Relaxed => intrinsics::atomic_and::<T, U, { AO::Relaxed }>(dst, val),
4090            Acquire => intrinsics::atomic_and::<T, U, { AO::Acquire }>(dst, val),
4091            Release => intrinsics::atomic_and::<T, U, { AO::Release }>(dst, val),
4092            AcqRel => intrinsics::atomic_and::<T, U, { AO::AcqRel }>(dst, val),
4093            SeqCst => intrinsics::atomic_and::<T, U, { AO::SeqCst }>(dst, val),
4094        }
4095    }
4096}
4097
4098#[inline]
4099#[cfg(target_has_atomic)]
4100#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4101unsafe fn atomic_nand<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
4102    // SAFETY: the caller must uphold the safety contract for `atomic_nand`
4103    unsafe {
4104        match order {
4105            Relaxed => intrinsics::atomic_nand::<T, U, { AO::Relaxed }>(dst, val),
4106            Acquire => intrinsics::atomic_nand::<T, U, { AO::Acquire }>(dst, val),
4107            Release => intrinsics::atomic_nand::<T, U, { AO::Release }>(dst, val),
4108            AcqRel => intrinsics::atomic_nand::<T, U, { AO::AcqRel }>(dst, val),
4109            SeqCst => intrinsics::atomic_nand::<T, U, { AO::SeqCst }>(dst, val),
4110        }
4111    }
4112}
4113
4114#[inline]
4115#[cfg(target_has_atomic)]
4116#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4117unsafe fn atomic_or<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
4118    // SAFETY: the caller must uphold the safety contract for `atomic_or`
4119    unsafe {
4120        match order {
4121            SeqCst => intrinsics::atomic_or::<T, U, { AO::SeqCst }>(dst, val),
4122            Acquire => intrinsics::atomic_or::<T, U, { AO::Acquire }>(dst, val),
4123            Release => intrinsics::atomic_or::<T, U, { AO::Release }>(dst, val),
4124            AcqRel => intrinsics::atomic_or::<T, U, { AO::AcqRel }>(dst, val),
4125            Relaxed => intrinsics::atomic_or::<T, U, { AO::Relaxed }>(dst, val),
4126        }
4127    }
4128}
4129
4130#[inline]
4131#[cfg(target_has_atomic)]
4132#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4133unsafe fn atomic_xor<T: Copy, U: Copy>(dst: *mut T, val: U, order: Ordering) -> T {
4134    // SAFETY: the caller must uphold the safety contract for `atomic_xor`
4135    unsafe {
4136        match order {
4137            SeqCst => intrinsics::atomic_xor::<T, U, { AO::SeqCst }>(dst, val),
4138            Acquire => intrinsics::atomic_xor::<T, U, { AO::Acquire }>(dst, val),
4139            Release => intrinsics::atomic_xor::<T, U, { AO::Release }>(dst, val),
4140            AcqRel => intrinsics::atomic_xor::<T, U, { AO::AcqRel }>(dst, val),
4141            Relaxed => intrinsics::atomic_xor::<T, U, { AO::Relaxed }>(dst, val),
4142        }
4143    }
4144}
4145
4146/// Updates `*dst` to the max value of `val` and the old value (signed comparison)
4147#[inline]
4148#[cfg(target_has_atomic)]
4149#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4150unsafe fn atomic_max<T: Copy>(dst: *mut T, val: T, order: Ordering) -> T {
4151    // SAFETY: the caller must uphold the safety contract for `atomic_max`
4152    unsafe {
4153        match order {
4154            Relaxed => intrinsics::atomic_max::<T, { AO::Relaxed }>(dst, val),
4155            Acquire => intrinsics::atomic_max::<T, { AO::Acquire }>(dst, val),
4156            Release => intrinsics::atomic_max::<T, { AO::Release }>(dst, val),
4157            AcqRel => intrinsics::atomic_max::<T, { AO::AcqRel }>(dst, val),
4158            SeqCst => intrinsics::atomic_max::<T, { AO::SeqCst }>(dst, val),
4159        }
4160    }
4161}
4162
4163/// Updates `*dst` to the min value of `val` and the old value (signed comparison)
4164#[inline]
4165#[cfg(target_has_atomic)]
4166#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4167unsafe fn atomic_min<T: Copy>(dst: *mut T, val: T, order: Ordering) -> T {
4168    // SAFETY: the caller must uphold the safety contract for `atomic_min`
4169    unsafe {
4170        match order {
4171            Relaxed => intrinsics::atomic_min::<T, { AO::Relaxed }>(dst, val),
4172            Acquire => intrinsics::atomic_min::<T, { AO::Acquire }>(dst, val),
4173            Release => intrinsics::atomic_min::<T, { AO::Release }>(dst, val),
4174            AcqRel => intrinsics::atomic_min::<T, { AO::AcqRel }>(dst, val),
4175            SeqCst => intrinsics::atomic_min::<T, { AO::SeqCst }>(dst, val),
4176        }
4177    }
4178}
4179
4180/// Updates `*dst` to the max value of `val` and the old value (unsigned comparison)
4181#[inline]
4182#[cfg(target_has_atomic)]
4183#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4184unsafe fn atomic_umax<T: Copy>(dst: *mut T, val: T, order: Ordering) -> T {
4185    // SAFETY: the caller must uphold the safety contract for `atomic_umax`
4186    unsafe {
4187        match order {
4188            Relaxed => intrinsics::atomic_umax::<T, { AO::Relaxed }>(dst, val),
4189            Acquire => intrinsics::atomic_umax::<T, { AO::Acquire }>(dst, val),
4190            Release => intrinsics::atomic_umax::<T, { AO::Release }>(dst, val),
4191            AcqRel => intrinsics::atomic_umax::<T, { AO::AcqRel }>(dst, val),
4192            SeqCst => intrinsics::atomic_umax::<T, { AO::SeqCst }>(dst, val),
4193        }
4194    }
4195}
4196
4197/// Updates `*dst` to the min value of `val` and the old value (unsigned comparison)
4198#[inline]
4199#[cfg(target_has_atomic)]
4200#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4201unsafe fn atomic_umin<T: Copy>(dst: *mut T, val: T, order: Ordering) -> T {
4202    // SAFETY: the caller must uphold the safety contract for `atomic_umin`
4203    unsafe {
4204        match order {
4205            Relaxed => intrinsics::atomic_umin::<T, { AO::Relaxed }>(dst, val),
4206            Acquire => intrinsics::atomic_umin::<T, { AO::Acquire }>(dst, val),
4207            Release => intrinsics::atomic_umin::<T, { AO::Release }>(dst, val),
4208            AcqRel => intrinsics::atomic_umin::<T, { AO::AcqRel }>(dst, val),
4209            SeqCst => intrinsics::atomic_umin::<T, { AO::SeqCst }>(dst, val),
4210        }
4211    }
4212}
4213
4214/// An atomic fence.
4215///
4216/// Fences create synchronization between themselves and atomic operations or fences in other
4217/// threads. To achieve this, a fence prevents the compiler and CPU from reordering certain types of
4218/// memory operations around it.
4219///
4220/// There are 3 different ways to use an atomic fence:
4221///
4222/// - atomic - fence synchronization: an atomic operation with (at least) [`Release`] ordering
4223///   semantics synchronizes with a fence with (at least) [`Acquire`] ordering semantics.
4224/// - fence - atomic synchronization: a fence with (at least) [`Release`] ordering semantics
4225///   synchronizes with an atomic operation with (at least) [`Acquire`] ordering semantics.
4226/// - fence - fence synchronization: a fence with (at least) [`Release`] ordering semantics
4227///   synchronizes with a fence with (at least) [`Acquire`] ordering semantics.
4228///
4229/// These 3 ways complement the regular, fence-less, atomic - atomic synchronization.
4230///
4231/// ## Atomic - Fence
4232///
4233/// An atomic operation on one thread will synchronize with a fence on another thread when:
4234///
4235/// -   on thread 1:
4236///     -   an atomic operation 'X' with (at least) [`Release`] ordering semantics on some atomic
4237///         object 'm',
4238///
4239/// -   is paired on thread 2 with:
4240///     -   an atomic read 'Y' with any order on 'm',
4241///     -   followed by a fence 'B' with (at least) [`Acquire`] ordering semantics.
4242///
4243/// This provides a happens-before dependence between X and B.
4244///
4245/// ```text
4246///     Thread 1                                          Thread 2
4247///
4248/// m.store(3, Release); X ---------
4249///                                |
4250///                                |
4251///                                -------------> Y  if m.load(Relaxed) == 3 {
4252///                                               B      fence(Acquire);
4253///                                                      ...
4254///                                                  }
4255/// ```
4256///
4257/// ## Fence - Atomic
4258///
4259/// A fence on one thread will synchronize with an atomic operation on another thread when:
4260///
4261/// -   on thread:
4262///     -   a fence 'A' with (at least) [`Release`] ordering semantics,
4263///     -   followed by an atomic write 'X' with any ordering on some atomic object 'm',
4264///
4265/// -   is paired on thread 2 with:
4266///     -   an atomic operation 'Y' with (at least) [`Acquire`] ordering semantics.
4267///
4268/// This provides a happens-before dependence between A and Y.
4269///
4270/// ```text
4271///     Thread 1                                          Thread 2
4272///
4273/// fence(Release);      A
4274/// m.store(3, Relaxed); X ---------
4275///                                |
4276///                                |
4277///                                -------------> Y  if m.load(Acquire) == 3 {
4278///                                                      ...
4279///                                                  }
4280/// ```
4281///
4282/// ## Fence - Fence
4283///
4284/// A fence on one thread will synchronize with a fence on another thread when:
4285///
4286/// -   on thread 1:
4287///     -   a fence 'A' which has (at least) [`Release`] ordering semantics,
4288///     -   followed by an atomic write 'X' with any ordering on some atomic object 'm',
4289///
4290/// -   is paired on thread 2 with:
4291///     -   an atomic read 'Y' with any ordering on 'm',
4292///     -   followed by a fence 'B' with (at least) [`Acquire`] ordering semantics.
4293///
4294/// This provides a happens-before dependence between A and B.
4295///
4296/// ```text
4297///     Thread 1                                          Thread 2
4298///
4299/// fence(Release);      A --------------
4300/// m.store(3, Relaxed); X ---------    |
4301///                                |    |
4302///                                |    |
4303///                                -------------> Y  if m.load(Relaxed) == 3 {
4304///                                     |-------> B      fence(Acquire);
4305///                                                      ...
4306///                                                  }
4307/// ```
4308///
4309/// ## Mandatory Atomic
4310///
4311/// Note that in the examples above, it is crucial that the access to `m` are atomic. Fences cannot
4312/// be used to establish synchronization between non-atomic accesses in different threads. However,
4313/// thanks to the happens-before relationship, any non-atomic access that happen-before the atomic
4314/// operation or fence with (at least) [`Release`] ordering semantics are now also properly
4315/// synchronized with any non-atomic accesses that happen-after the atomic operation or fence with
4316/// (at least) [`Acquire`] ordering semantics.
4317///
4318/// ## Memory Ordering
4319///
4320/// A fence which has [`SeqCst`] ordering, in addition to having both [`Acquire`] and [`Release`]
4321/// semantics, participates in the global program order of the other [`SeqCst`] operations and/or
4322/// fences.
4323///
4324/// Accepts [`Acquire`], [`Release`], [`AcqRel`] and [`SeqCst`] orderings.
4325///
4326/// # Panics
4327///
4328/// Panics if `order` is [`Relaxed`].
4329///
4330/// # Examples
4331///
4332/// ```
4333/// use std::sync::atomic::AtomicBool;
4334/// use std::sync::atomic::fence;
4335/// use std::sync::atomic::Ordering;
4336///
4337/// // A mutual exclusion primitive based on spinlock.
4338/// pub struct Mutex {
4339///     flag: AtomicBool,
4340/// }
4341///
4342/// impl Mutex {
4343///     pub fn new() -> Mutex {
4344///         Mutex {
4345///             flag: AtomicBool::new(false),
4346///         }
4347///     }
4348///
4349///     pub fn lock(&self) {
4350///         // Wait until the old value is `false`.
4351///         while self
4352///             .flag
4353///             .compare_exchange_weak(false, true, Ordering::Relaxed, Ordering::Relaxed)
4354///             .is_err()
4355///         {}
4356///         // This fence synchronizes-with store in `unlock`.
4357///         fence(Ordering::Acquire);
4358///     }
4359///
4360///     pub fn unlock(&self) {
4361///         self.flag.store(false, Ordering::Release);
4362///     }
4363/// }
4364/// ```
4365#[inline]
4366#[stable(feature = "rust1", since = "1.0.0")]
4367#[rustc_diagnostic_item = "fence"]
4368#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4369pub fn fence(order: Ordering) {
4370    // SAFETY: using an atomic fence is safe.
4371    unsafe {
4372        match order {
4373            Acquire => intrinsics::atomic_fence::<{ AO::Acquire }>(),
4374            Release => intrinsics::atomic_fence::<{ AO::Release }>(),
4375            AcqRel => intrinsics::atomic_fence::<{ AO::AcqRel }>(),
4376            SeqCst => intrinsics::atomic_fence::<{ AO::SeqCst }>(),
4377            Relaxed => panic!("there is no such thing as a relaxed fence"),
4378        }
4379    }
4380}
4381
4382/// A "compiler-only" atomic fence.
4383///
4384/// Like [`fence`], this function establishes synchronization with other atomic operations and
4385/// fences. However, unlike [`fence`], `compiler_fence` only establishes synchronization with
4386/// operations *in the same thread*. This may at first sound rather useless, since code within a
4387/// thread is typically already totally ordered and does not need any further synchronization.
4388/// However, there are cases where code can run on the same thread without being ordered:
4389/// - The most common case is that of a *signal handler*: a signal handler runs in the same thread
4390///   as the code it interrupted, but it is not ordered with respect to that code. `compiler_fence`
4391///   can be used to establish synchronization between a thread and its signal handler, the same way
4392///   that `fence` can be used to establish synchronization across threads.
4393/// - Similar situations can arise in embedded programming with interrupt handlers, or in custom
4394///   implementations of preemptive green threads. In general, `compiler_fence` can establish
4395///   synchronization with code that is guaranteed to run on the same hardware CPU.
4396///
4397/// See [`fence`] for how a fence can be used to achieve synchronization. Note that just like
4398/// [`fence`], synchronization still requires atomic operations to be used in both threads -- it is
4399/// not possible to perform synchronization entirely with fences and non-atomic operations.
4400///
4401/// `compiler_fence` does not emit any machine code, but restricts the kinds of memory re-ordering
4402/// the compiler is allowed to do. `compiler_fence` corresponds to [`atomic_signal_fence`] in C and
4403/// C++.
4404///
4405/// [`atomic_signal_fence`]: https://en.cppreference.com/w/cpp/atomic/atomic_signal_fence
4406///
4407/// # Panics
4408///
4409/// Panics if `order` is [`Relaxed`].
4410///
4411/// # Examples
4412///
4413/// Without the two `compiler_fence` calls, the read of `IMPORTANT_VARIABLE` in `signal_handler`
4414/// is *undefined behavior* due to a data race, despite everything happening in a single thread.
4415/// This is because the signal handler is considered to run concurrently with its associated
4416/// thread, and explicit synchronization is required to pass data between a thread and its
4417/// signal handler. The code below uses two `compiler_fence` calls to establish the usual
4418/// release-acquire synchronization pattern (see [`fence`] for an image).
4419///
4420/// ```
4421/// use std::sync::atomic::AtomicBool;
4422/// use std::sync::atomic::Ordering;
4423/// use std::sync::atomic::compiler_fence;
4424///
4425/// static mut IMPORTANT_VARIABLE: usize = 0;
4426/// static IS_READY: AtomicBool = AtomicBool::new(false);
4427///
4428/// fn main() {
4429///     unsafe { IMPORTANT_VARIABLE = 42 };
4430///     // Marks earlier writes as being released with future relaxed stores.
4431///     compiler_fence(Ordering::Release);
4432///     IS_READY.store(true, Ordering::Relaxed);
4433/// }
4434///
4435/// fn signal_handler() {
4436///     if IS_READY.load(Ordering::Relaxed) {
4437///         // Acquires writes that were released with relaxed stores that we read from.
4438///         compiler_fence(Ordering::Acquire);
4439///         assert_eq!(unsafe { IMPORTANT_VARIABLE }, 42);
4440///     }
4441/// }
4442/// ```
4443#[inline]
4444#[stable(feature = "compiler_fences", since = "1.21.0")]
4445#[rustc_diagnostic_item = "compiler_fence"]
4446#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
4447pub fn compiler_fence(order: Ordering) {
4448    // SAFETY: using an atomic fence is safe.
4449    unsafe {
4450        match order {
4451            Acquire => intrinsics::atomic_singlethreadfence::<{ AO::Acquire }>(),
4452            Release => intrinsics::atomic_singlethreadfence::<{ AO::Release }>(),
4453            AcqRel => intrinsics::atomic_singlethreadfence::<{ AO::AcqRel }>(),
4454            SeqCst => intrinsics::atomic_singlethreadfence::<{ AO::SeqCst }>(),
4455            Relaxed => panic!("there is no such thing as a relaxed fence"),
4456        }
4457    }
4458}
4459
4460#[cfg(target_has_atomic_load_store = "8")]
4461#[stable(feature = "atomic_debug", since = "1.3.0")]
4462impl fmt::Debug for AtomicBool {
4463    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4464        fmt::Debug::fmt(&self.load(Ordering::Relaxed), f)
4465    }
4466}
4467
4468#[cfg(target_has_atomic_load_store = "ptr")]
4469#[stable(feature = "atomic_debug", since = "1.3.0")]
4470impl<T> fmt::Debug for AtomicPtr<T> {
4471    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4472        fmt::Debug::fmt(&self.load(Ordering::Relaxed), f)
4473    }
4474}
4475
4476#[cfg(target_has_atomic_load_store = "ptr")]
4477#[stable(feature = "atomic_pointer", since = "1.24.0")]
4478impl<T> fmt::Pointer for AtomicPtr<T> {
4479    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4480        fmt::Pointer::fmt(&self.load(Ordering::Relaxed), f)
4481    }
4482}
4483
4484/// Signals the processor that it is inside a busy-wait spin-loop ("spin lock").
4485///
4486/// This function is deprecated in favor of [`hint::spin_loop`].
4487///
4488/// [`hint::spin_loop`]: crate::hint::spin_loop
4489#[inline]
4490#[stable(feature = "spin_loop_hint", since = "1.24.0")]
4491#[deprecated(since = "1.51.0", note = "use hint::spin_loop instead")]
4492pub fn spin_loop_hint() {
4493    spin_loop()
4494}
````