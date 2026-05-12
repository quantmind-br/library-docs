---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/vec/mod.rs.html#4423
source: crawler
fetched_at: 2026-05-06T21:33:58.906351913-03:00
rendered_js: false
word_count: 20310
summary: This document defines the Vec<T> type in Rust, which is a contiguous, growable array type that manages heap-allocated memory and provides amortized O(1) performance for common operations.
tags:
    - rust
    - vector
    - dynamic-array
    - memory-allocation
    - standard-library
    - collection-types
category: reference
---

## alloc/vec/ mod.rs

````rust
1//! A contiguous growable array type with heap-allocated contents, written
2//! `Vec<T>`.
3//!
4//! Vectors have *O*(1) indexing, amortized *O*(1) push (to the end) and
5//! *O*(1) pop (from the end).
6//!
7//! Vectors ensure they never allocate more than `isize::MAX` bytes.
8//!
9//! # Examples
10//!
11//! You can explicitly create a [`Vec`] with [`Vec::new`]:
12//!
13//! ```
14//! let v: Vec<i32> = Vec::new();
15//! ```
16//!
17//! ...or by using the [`vec!`] macro:
18//!
19//! ```
20//! let v: Vec<i32> = vec![];
21//!
22//! let v = vec![1, 2, 3, 4, 5];
23//!
24//! let v = vec![0; 10]; // ten zeroes
25//! ```
26//!
27//! You can [`push`] values onto the end of a vector (which will grow the vector
28//! as needed):
29//!
30//! ```
31//! let mut v = vec![1, 2];
32//!
33//! v.push(3);
34//! ```
35//!
36//! Popping values works in much the same way:
37//!
38//! ```
39//! let mut v = vec![1, 2];
40//!
41//! let two = v.pop();
42//! ```
43//!
44//! Vectors also support indexing (through the [`Index`] and [`IndexMut`] traits):
45//!
46//! ```
47//! let mut v = vec![1, 2, 3];
48//! let three = v[2];
49//! v[1] = v[1] + 5;
50//! ```
51//!
52//! # Memory layout
53//!
54//! When the type is non-zero-sized and the capacity is nonzero, [`Vec`] uses the [`Global`]
55//! allocator for its allocation. It is valid to convert both ways between such a [`Vec`] and a raw
56//! pointer allocated with the [`Global`] allocator, provided that the [`Layout`] used with the
57//! allocator is correct for a sequence of `capacity` elements of the type, and the first `len`
58//! values pointed to by the raw pointer are valid. More precisely, a `ptr: *mut T` that has been
59//! allocated with the [`Global`] allocator with [`Layout::array::<T>(capacity)`][Layout::array] may
60//! be converted into a vec using
61//! [`Vec::<T>::from_raw_parts(ptr, len, capacity)`](Vec::from_raw_parts). Conversely, the memory
62//! backing a `value: *mut T` obtained from [`Vec::<T>::as_mut_ptr`] may be deallocated using the
63//! [`Global`] allocator with the same layout.
64//!
65//! For zero-sized types (ZSTs), or when the capacity is zero, the `Vec` pointer must be non-null
66//! and sufficiently aligned. The recommended way to build a `Vec` of ZSTs if [`vec!`] cannot be
67//! used is to use [`ptr::NonNull::dangling`].
68//!
69//! [`push`]: Vec::push
70//! [`ptr::NonNull::dangling`]: NonNull::dangling
71//! [`Layout`]: crate::alloc::Layout
72//! [Layout::array]: crate::alloc::Layout::array
73
74#![stable(feature = "rust1", since = "1.0.0")]
75
76#[cfg(not(no_global_oom_handling))]
77use core::clone::TrivialClone;
78use core::cmp::Ordering;
79use core::hash::{Hash, Hasher};
80#[cfg(not(no_global_oom_handling))]
81use core::iter;
82#[cfg(not(no_global_oom_handling))]
83use core::marker::Destruct;
84use core::marker::{Freeze, PhantomData};
85use core::mem::{self, Assume, ManuallyDrop, MaybeUninit, SizedTypeProperties, TransmuteFrom};
86use core::ops::{self, Index, IndexMut, Range, RangeBounds};
87use core::ptr::{self, NonNull};
88use core::slice::{self, SliceIndex};
89use core::{cmp, fmt, hint, intrinsics, ub_checks};
90
91#[stable(feature = "extract_if", since = "1.87.0")]
92pub use self::extract_if::ExtractIf;
93use crate::alloc::{Allocator, Global};
94use crate::borrow::{Cow, ToOwned};
95use crate::boxed::Box;
96use crate::collections::TryReserveError;
97use crate::raw_vec::RawVec;
98
99mod extract_if;
100
101#[cfg(not(no_global_oom_handling))]
102#[stable(feature = "vec_splice", since = "1.21.0")]
103pub use self::splice::Splice;
104
105#[cfg(not(no_global_oom_handling))]
106mod splice;
107
108#[stable(feature = "drain", since = "1.6.0")]
109pub use self::drain::Drain;
110
111mod drain;
112
113#[cfg(not(no_global_oom_handling))]
114mod cow;
115
116#[cfg(not(no_global_oom_handling))]
117pub(crate) use self::in_place_collect::AsVecIntoIter;
118#[stable(feature = "rust1", since = "1.0.0")]
119pub use self::into_iter::IntoIter;
120
121mod into_iter;
122
123#[cfg(not(no_global_oom_handling))]
124use self::is_zero::IsZero;
125
126#[cfg(not(no_global_oom_handling))]
127mod is_zero;
128
129#[cfg(not(no_global_oom_handling))]
130mod in_place_collect;
131
132mod partial_eq;
133
134#[unstable(feature = "vec_peek_mut", issue = "122742")]
135pub use self::peek_mut::PeekMut;
136
137mod peek_mut;
138
139#[cfg(not(no_global_oom_handling))]
140use self::spec_from_elem::SpecFromElem;
141
142#[cfg(not(no_global_oom_handling))]
143mod spec_from_elem;
144
145#[cfg(not(no_global_oom_handling))]
146use self::set_len_on_drop::SetLenOnDrop;
147
148#[cfg(not(no_global_oom_handling))]
149mod set_len_on_drop;
150
151#[cfg(not(no_global_oom_handling))]
152use self::in_place_drop::{InPlaceDrop, InPlaceDstDataSrcBufDrop};
153
154#[cfg(not(no_global_oom_handling))]
155mod in_place_drop;
156
157#[cfg(not(no_global_oom_handling))]
158use self::spec_from_iter_nested::SpecFromIterNested;
159
160#[cfg(not(no_global_oom_handling))]
161mod spec_from_iter_nested;
162
163#[cfg(not(no_global_oom_handling))]
164use self::spec_from_iter::SpecFromIter;
165
166#[cfg(not(no_global_oom_handling))]
167mod spec_from_iter;
168
169#[cfg(not(no_global_oom_handling))]
170use self::spec_extend::SpecExtend;
171
172#[cfg(not(no_global_oom_handling))]
173mod spec_extend;
174
175/// A contiguous growable array type, written as `Vec<T>`, short for 'vector'.
176///
177/// # Examples
178///
179/// ```
180/// let mut vec = Vec::new();
181/// vec.push(1);
182/// vec.push(2);
183///
184/// assert_eq!(vec.len(), 2);
185/// assert_eq!(vec[0], 1);
186///
187/// assert_eq!(vec.pop(), Some(2));
188/// assert_eq!(vec.len(), 1);
189///
190/// vec[0] = 7;
191/// assert_eq!(vec[0], 7);
192///
193/// vec.extend([1, 2, 3]);
194///
195/// for x in &vec {
196///     println!("{x}");
197/// }
198/// assert_eq!(vec, [7, 1, 2, 3]);
199/// ```
200///
201/// The [`vec!`] macro is provided for convenient initialization:
202///
203/// ```
204/// let mut vec1 = vec![1, 2, 3];
205/// vec1.push(4);
206/// let vec2 = Vec::from([1, 2, 3, 4]);
207/// assert_eq!(vec1, vec2);
208/// ```
209///
210/// It can also initialize each element of a `Vec<T>` with a given value.
211/// This may be more efficient than performing allocation and initialization
212/// in separate steps, especially when initializing a vector of zeros:
213///
214/// ```
215/// let vec = vec![0; 5];
216/// assert_eq!(vec, [0, 0, 0, 0, 0]);
217///
218/// // The following is equivalent, but potentially slower:
219/// let mut vec = Vec::with_capacity(5);
220/// vec.resize(5, 0);
221/// assert_eq!(vec, [0, 0, 0, 0, 0]);
222/// ```
223///
224/// For more information, see
225/// [Capacity and Reallocation](#capacity-and-reallocation).
226///
227/// Use a `Vec<T>` as an efficient stack:
228///
229/// ```
230/// let mut stack = Vec::new();
231///
232/// stack.push(1);
233/// stack.push(2);
234/// stack.push(3);
235///
236/// while let Some(top) = stack.pop() {
237///     // Prints 3, 2, 1
238///     println!("{top}");
239/// }
240/// ```
241///
242/// # Indexing
243///
244/// The `Vec` type allows access to values by index, because it implements the
245/// [`Index`] trait. An example will be more explicit:
246///
247/// ```
248/// let v = vec![0, 2, 4, 6];
249/// println!("{}", v[1]); // it will display '2'
250/// ```
251///
252/// However be careful: if you try to access an index which isn't in the `Vec`,
253/// your software will panic! You cannot do this:
254///
255/// ```should_panic
256/// let v = vec![0, 2, 4, 6];
257/// println!("{}", v[6]); // it will panic!
258/// ```
259///
260/// Use [`get`] and [`get_mut`] if you want to check whether the index is in
261/// the `Vec`.
262///
263/// # Slicing
264///
265/// A `Vec` can be mutable. On the other hand, slices are read-only objects.
266/// To get a [slice][prim@slice], use [`&`]. Example:
267///
268/// ```
269/// fn read_slice(slice: &[usize]) {
270///     // ...
271/// }
272///
273/// let v = vec![0, 1];
274/// read_slice(&v);
275///
276/// // ... and that's all!
277/// // you can also do it like this:
278/// let u: &[usize] = &v;
279/// // or like this:
280/// let u: &[_] = &v;
281/// ```
282///
283/// In Rust, it's more common to pass slices as arguments rather than vectors
284/// when you just want to provide read access. The same goes for [`String`] and
285/// [`&str`].
286///
287/// # Capacity and reallocation
288///
289/// The capacity of a vector is the amount of space allocated for any future
290/// elements that will be added onto the vector. This is not to be confused with
291/// the *length* of a vector, which specifies the number of actual elements
292/// within the vector. If a vector's length exceeds its capacity, its capacity
293/// will automatically be increased, but its elements will have to be
294/// reallocated.
295///
296/// For example, a vector with capacity 10 and length 0 would be an empty vector
297/// with space for 10 more elements. Pushing 10 or fewer elements onto the
298/// vector will not change its capacity or cause reallocation to occur. However,
299/// if the vector's length is increased to 11, it will have to reallocate, which
300/// can be slow. For this reason, it is recommended to use [`Vec::with_capacity`]
301/// whenever possible to specify how big the vector is expected to get.
302///
303/// # Guarantees
304///
305/// Due to its incredibly fundamental nature, `Vec` makes a lot of guarantees
306/// about its design. This ensures that it's as low-overhead as possible in
307/// the general case, and can be correctly manipulated in primitive ways
308/// by unsafe code. Note that these guarantees refer to an unqualified `Vec<T>`.
309/// If additional type parameters are added (e.g., to support custom allocators),
310/// overriding their defaults may change the behavior.
311///
312/// Most fundamentally, `Vec` is and always will be a (pointer, capacity, length)
313/// triplet. No more, no less. The order of these fields is completely
314/// unspecified, and you should use the appropriate methods to modify these.
315/// The pointer will never be null, so this type is null-pointer-optimized.
316///
317/// However, the pointer might not actually point to allocated memory. In particular,
318/// if you construct a `Vec` with capacity 0 via [`Vec::new`], [`vec![]`][`vec!`],
319/// [`Vec::with_capacity(0)`][`Vec::with_capacity`], or by calling [`shrink_to_fit`]
320/// on an empty Vec, it will not allocate memory. Similarly, if you store zero-sized
321/// types inside a `Vec`, it will not allocate space for them. *Note that in this case
322/// the `Vec` might not report a [`capacity`] of 0*. `Vec` will allocate if and only
323/// if <code>[size_of::\<T>]\() * [capacity]\() > 0</code>. In general, `Vec`'s allocation
324/// details are very subtle --- if you intend to allocate memory using a `Vec`
325/// and use it for something else (either to pass to unsafe code, or to build your
326/// own memory-backed collection), be sure to deallocate this memory by using
327/// `from_raw_parts` to recover the `Vec` and then dropping it.
328///
329/// If a `Vec` *has* allocated memory, then the memory it points to is on the heap
330/// (as defined by the allocator Rust is configured to use by default), and its
331/// pointer points to [`len`] initialized, contiguous elements in order (what
332/// you would see if you coerced it to a slice), followed by <code>[capacity] - [len]</code>
333/// logically uninitialized, contiguous elements.
334///
335/// A vector containing the elements `'a'` and `'b'` with capacity 4 can be
336/// visualized as below. The top part is the `Vec` struct, it contains a
337/// pointer to the head of the allocation in the heap, length and capacity.
338/// The bottom part is the allocation on the heap, a contiguous memory block.
339///
340/// ```text
341///             ptr      len  capacity
342///        +--------+--------+--------+
343///        | 0x0123 |      2 |      4 |
344///        +--------+--------+--------+
345///             |
346///             v
347/// Heap   +--------+--------+--------+--------+
348///        |    'a' |    'b' | uninit | uninit |
349///        +--------+--------+--------+--------+
350/// ```
351///
352/// - **uninit** represents memory that is not initialized, see [`MaybeUninit`].
353/// - Note: the ABI is not stable and `Vec` makes no guarantees about its memory
354///   layout (including the order of fields).
355///
356/// `Vec` will never perform a "small optimization" where elements are actually
357/// stored on the stack for two reasons:
358///
359/// * It would make it more difficult for unsafe code to correctly manipulate
360///   a `Vec`. The contents of a `Vec` wouldn't have a stable address if it were
361///   only moved, and it would be more difficult to determine if a `Vec` had
362///   actually allocated memory.
363///
364/// * It would penalize the general case, incurring an additional branch
365///   on every access.
366///
367/// `Vec` will never automatically shrink itself, even if completely empty. This
368/// ensures no unnecessary allocations or deallocations occur. Emptying a `Vec`
369/// and then filling it back up to the same [`len`] should incur no calls to
370/// the allocator. If you wish to free up unused memory, use
371/// [`shrink_to_fit`] or [`shrink_to`].
372///
373/// [`push`] and [`insert`] will never (re)allocate if the reported capacity is
374/// sufficient. [`push`] and [`insert`] *will* (re)allocate if
375/// <code>[len] == [capacity]</code>. That is, the reported capacity is completely
376/// accurate, and can be relied on. It can even be used to manually free the memory
377/// allocated by a `Vec` if desired. Bulk insertion methods *may* reallocate, even
378/// when not necessary.
379///
380/// `Vec` does not guarantee any particular growth strategy when reallocating
381/// when full, nor when [`reserve`] is called. The current strategy is basic
382/// and it may prove desirable to use a non-constant growth factor. Whatever
383/// strategy is used will of course guarantee *O*(1) amortized [`push`].
384///
385/// It is guaranteed, in order to respect the intentions of the programmer, that
386/// all of `vec![e_1, e_2, ..., e_n]`, `vec![x; n]`, and [`Vec::with_capacity(n)`] produce a `Vec`
387/// that requests an allocation of the exact size needed for precisely `n` elements from the allocator,
388/// and no other size (such as, for example: a size rounded up to the nearest power of 2).
389/// The allocator will return an allocation that is at least as large as requested, but it may be larger.
390///
391/// It is guaranteed that the [`Vec::capacity`] method returns a value that is at least the requested capacity
392/// and not more than the allocated capacity.
393///
394/// The method [`Vec::shrink_to_fit`] will attempt to discard excess capacity an allocator has given to a `Vec`.
395/// If <code>[len] == [capacity]</code>, then a `Vec<T>` can be converted
396/// to and from a [`Box<[T]>`][owned slice] without reallocating or moving the elements.
397/// `Vec` exploits this fact as much as reasonable when implementing common conversions
398/// such as [`into_boxed_slice`].
399///
400/// `Vec` will not specifically overwrite any data that is removed from it,
401/// but also won't specifically preserve it. Its uninitialized memory is
402/// scratch space that it may use however it wants. It will generally just do
403/// whatever is most efficient or otherwise easy to implement. Do not rely on
404/// removed data to be erased for security purposes. Even if you drop a `Vec`, its
405/// buffer may simply be reused by another allocation. Even if you zero a `Vec`'s memory
406/// first, that might not actually happen because the optimizer does not consider
407/// this a side-effect that must be preserved. There is one case which we will
408/// not break, however: using `unsafe` code to write to the excess capacity,
409/// and then increasing the length to match, is always valid.
410///
411/// Currently, `Vec` does not guarantee the order in which elements are dropped.
412/// The order has changed in the past and may change again.
413///
414/// [`get`]: slice::get
415/// [`get_mut`]: slice::get_mut
416/// [`String`]: crate::string::String
417/// [`&str`]: type@str
418/// [`shrink_to_fit`]: Vec::shrink_to_fit
419/// [`shrink_to`]: Vec::shrink_to
420/// [capacity]: Vec::capacity
421/// [`capacity`]: Vec::capacity
422/// [`Vec::capacity`]: Vec::capacity
423/// [size_of::\<T>]: size_of
424/// [len]: Vec::len
425/// [`len`]: Vec::len
426/// [`push`]: Vec::push
427/// [`insert`]: Vec::insert
428/// [`reserve`]: Vec::reserve
429/// [`Vec::with_capacity(n)`]: Vec::with_capacity
430/// [`MaybeUninit`]: core::mem::MaybeUninit
431/// [owned slice]: Box
432/// [`into_boxed_slice`]: Vec::into_boxed_slice
433#[stable(feature = "rust1", since = "1.0.0")]
434#[rustc_diagnostic_item = "Vec"]
435#[rustc_insignificant_dtor]
436#[doc(alias = "list")]
437#[doc(alias = "vector")]
438pub struct Vec<T, #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global> {
439    buf: RawVec<T, A>,
440    len: usize,
441}
442
443////////////////////////////////////////////////////////////////////////////////
444// Inherent methods
445////////////////////////////////////////////////////////////////////////////////
446
447impl<T> Vec<T> {
448    /// Constructs a new, empty `Vec<T>`.
449    ///
450    /// The vector will not allocate until elements are pushed onto it.
451    ///
452    /// # Examples
453    ///
454    /// ```
455    /// # #![allow(unused_mut)]
456    /// let mut vec: Vec<i32> = Vec::new();
457    /// ```
458    #[inline]
459    #[rustc_const_stable(feature = "const_vec_new", since = "1.39.0")]
460    #[rustc_diagnostic_item = "vec_new"]
461    #[stable(feature = "rust1", since = "1.0.0")]
462    #[must_use]
463    pub const fn new() -> Self {
464        Vec { buf: RawVec::new(), len: 0 }
465    }
466
467    /// Constructs a new, empty `Vec<T>` with at least the specified capacity.
468    ///
469    /// The vector will be able to hold at least `capacity` elements without
470    /// reallocating. This method is allowed to allocate for more elements than
471    /// `capacity`. If `capacity` is zero, the vector will not allocate.
472    ///
473    /// It is important to note that although the returned vector has the
474    /// minimum *capacity* specified, the vector will have a zero *length*. For
475    /// an explanation of the difference between length and capacity, see
476    /// *[Capacity and reallocation]*.
477    ///
478    /// If it is important to know the exact allocated capacity of a `Vec`,
479    /// always use the [`capacity`] method after construction.
480    ///
481    /// For `Vec<T>` where `T` is a zero-sized type, there will be no allocation
482    /// and the capacity will always be `usize::MAX`.
483    ///
484    /// [Capacity and reallocation]: #capacity-and-reallocation
485    /// [`capacity`]: Vec::capacity
486    ///
487    /// # Panics
488    ///
489    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
490    ///
491    /// # Examples
492    ///
493    /// ```
494    /// let mut vec = Vec::with_capacity(10);
495    ///
496    /// // The vector contains no items, even though it has capacity for more
497    /// assert_eq!(vec.len(), 0);
498    /// assert!(vec.capacity() >= 10);
499    ///
500    /// // These are all done without reallocating...
501    /// for i in 0..10 {
502    ///     vec.push(i);
503    /// }
504    /// assert_eq!(vec.len(), 10);
505    /// assert!(vec.capacity() >= 10);
506    ///
507    /// // ...but this may make the vector reallocate
508    /// vec.push(11);
509    /// assert_eq!(vec.len(), 11);
510    /// assert!(vec.capacity() >= 11);
511    ///
512    /// // A vector of a zero-sized type will always over-allocate, since no
513    /// // allocation is necessary
514    /// let vec_units = Vec::<()>::with_capacity(10);
515    /// assert_eq!(vec_units.capacity(), usize::MAX);
516    /// ```
517    #[cfg(not(no_global_oom_handling))]
518    #[inline]
519    #[stable(feature = "rust1", since = "1.0.0")]
520    #[must_use]
521    #[rustc_diagnostic_item = "vec_with_capacity"]
522    #[rustc_const_unstable(feature = "const_heap", issue = "79597")]
523    pub const fn with_capacity(capacity: usize) -> Self {
524        Self::with_capacity_in(capacity, Global)
525    }
526
527    /// Constructs a new, empty `Vec<T>` with at least the specified capacity.
528    ///
529    /// The vector will be able to hold at least `capacity` elements without
530    /// reallocating. This method is allowed to allocate for more elements than
531    /// `capacity`. If `capacity` is zero, the vector will not allocate.
532    ///
533    /// # Errors
534    ///
535    /// Returns an error if the capacity exceeds `isize::MAX` _bytes_,
536    /// or if the allocator reports allocation failure.
537    #[inline]
538    #[unstable(feature = "try_with_capacity", issue = "91913")]
539    pub fn try_with_capacity(capacity: usize) -> Result<Self, TryReserveError> {
540        Self::try_with_capacity_in(capacity, Global)
541    }
542
543    /// Creates a `Vec<T>` directly from a pointer, a length, and a capacity.
544    ///
545    /// # Safety
546    ///
547    /// This is highly unsafe, due to the number of invariants that aren't
548    /// checked:
549    ///
550    /// * If `T` is not a zero-sized type and the capacity is nonzero, `ptr` must have
551    ///   been allocated using the global allocator, such as via the [`alloc::alloc`]
552    ///   function. If `T` is a zero-sized type or the capacity is zero, `ptr` need
553    ///   only be non-null and aligned.
554    /// * `T` needs to have the same alignment as what `ptr` was allocated with,
555    ///   if the pointer is required to be allocated.
556    ///   (`T` having a less strict alignment is not sufficient, the alignment really
557    ///   needs to be equal to satisfy the [`dealloc`] requirement that memory must be
558    ///   allocated and deallocated with the same layout.)
559    /// * The size of `T` times the `capacity` (ie. the allocated size in bytes), if
560    ///   nonzero, needs to be the same size as the pointer was allocated with.
561    ///   (Because similar to alignment, [`dealloc`] must be called with the same
562    ///   layout `size`.)
563    /// * `length` needs to be less than or equal to `capacity`.
564    /// * The first `length` values must be properly initialized values of type `T`.
565    /// * `capacity` needs to be the capacity that the pointer was allocated with,
566    ///   if the pointer is required to be allocated.
567    /// * The allocated size in bytes must be no larger than `isize::MAX`.
568    ///   See the safety documentation of [`pointer::offset`].
569    ///
570    /// These requirements are always upheld by any `ptr` that has been allocated
571    /// via `Vec<T>`. Other allocation sources are allowed if the invariants are
572    /// upheld.
573    ///
574    /// Violating these may cause problems like corrupting the allocator's
575    /// internal data structures. For example it is normally **not** safe
576    /// to build a `Vec<u8>` from a pointer to a C `char` array with length
577    /// `size_t`, doing so is only safe if the array was initially allocated by
578    /// a `Vec` or `String`.
579    /// It's also not safe to build one from a `Vec<u16>` and its length, because
580    /// the allocator cares about the alignment, and these two types have different
581    /// alignments. The buffer was allocated with alignment 2 (for `u16`), but after
582    /// turning it into a `Vec<u8>` it'll be deallocated with alignment 1. To avoid
583    /// these issues, it is often preferable to do casting/transmuting using
584    /// [`slice::from_raw_parts`] instead.
585    ///
586    /// The ownership of `ptr` is effectively transferred to the
587    /// `Vec<T>` which may then deallocate, reallocate or change the
588    /// contents of memory pointed to by the pointer at will. Ensure
589    /// that nothing else uses the pointer after calling this
590    /// function.
591    ///
592    /// [`String`]: crate::string::String
593    /// [`alloc::alloc`]: crate::alloc::alloc
594    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
595    ///
596    /// # Examples
597    ///
598    /// ```
599    /// use std::ptr;
600    ///
601    /// let v = vec![1, 2, 3];
602    ///
603    /// // Deconstruct the vector into parts.
604    /// let (p, len, cap) = v.into_raw_parts();
605    ///
606    /// unsafe {
607    ///     // Overwrite memory with 4, 5, 6
608    ///     for i in 0..len {
609    ///         ptr::write(p.add(i), 4 + i);
610    ///     }
611    ///
612    ///     // Put everything back together into a Vec
613    ///     let rebuilt = Vec::from_raw_parts(p, len, cap);
614    ///     assert_eq!(rebuilt, [4, 5, 6]);
615    /// }
616    /// ```
617    ///
618    /// Using memory that was allocated elsewhere:
619    ///
620    /// ```rust
621    /// use std::alloc::{alloc, Layout};
622    ///
623    /// fn main() {
624    ///     let layout = Layout::array::<u32>(16).expect("overflow cannot happen");
625    ///
626    ///     let vec = unsafe {
627    ///         let mem = alloc(layout).cast::<u32>();
628    ///         if mem.is_null() {
629    ///             return;
630    ///         }
631    ///
632    ///         mem.write(1_000_000);
633    ///
634    ///         Vec::from_raw_parts(mem, 1, 16)
635    ///     };
636    ///
637    ///     assert_eq!(vec, &[1_000_000]);
638    ///     assert_eq!(vec.capacity(), 16);
639    /// }
640    /// ```
641    #[inline]
642    #[stable(feature = "rust1", since = "1.0.0")]
643    pub unsafe fn from_raw_parts(ptr: *mut T, length: usize, capacity: usize) -> Self {
644        unsafe { Self::from_raw_parts_in(ptr, length, capacity, Global) }
645    }
646
647    #[doc(alias = "from_non_null_parts")]
648    /// Creates a `Vec<T>` directly from a `NonNull` pointer, a length, and a capacity.
649    ///
650    /// # Safety
651    ///
652    /// This is highly unsafe, due to the number of invariants that aren't
653    /// checked:
654    ///
655    /// * `ptr` must have been allocated using the global allocator, such as via
656    ///   the [`alloc::alloc`] function.
657    /// * `T` needs to have the same alignment as what `ptr` was allocated with.
658    ///   (`T` having a less strict alignment is not sufficient, the alignment really
659    ///   needs to be equal to satisfy the [`dealloc`] requirement that memory must be
660    ///   allocated and deallocated with the same layout.)
661    /// * The size of `T` times the `capacity` (ie. the allocated size in bytes) needs
662    ///   to be the same size as the pointer was allocated with. (Because similar to
663    ///   alignment, [`dealloc`] must be called with the same layout `size`.)
664    /// * `length` needs to be less than or equal to `capacity`.
665    /// * The first `length` values must be properly initialized values of type `T`.
666    /// * `capacity` needs to be the capacity that the pointer was allocated with.
667    /// * The allocated size in bytes must be no larger than `isize::MAX`.
668    ///   See the safety documentation of [`pointer::offset`].
669    ///
670    /// These requirements are always upheld by any `ptr` that has been allocated
671    /// via `Vec<T>`. Other allocation sources are allowed if the invariants are
672    /// upheld.
673    ///
674    /// Violating these may cause problems like corrupting the allocator's
675    /// internal data structures. For example it is normally **not** safe
676    /// to build a `Vec<u8>` from a pointer to a C `char` array with length
677    /// `size_t`, doing so is only safe if the array was initially allocated by
678    /// a `Vec` or `String`.
679    /// It's also not safe to build one from a `Vec<u16>` and its length, because
680    /// the allocator cares about the alignment, and these two types have different
681    /// alignments. The buffer was allocated with alignment 2 (for `u16`), but after
682    /// turning it into a `Vec<u8>` it'll be deallocated with alignment 1. To avoid
683    /// these issues, it is often preferable to do casting/transmuting using
684    /// [`NonNull::slice_from_raw_parts`] instead.
685    ///
686    /// The ownership of `ptr` is effectively transferred to the
687    /// `Vec<T>` which may then deallocate, reallocate or change the
688    /// contents of memory pointed to by the pointer at will. Ensure
689    /// that nothing else uses the pointer after calling this
690    /// function.
691    ///
692    /// [`String`]: crate::string::String
693    /// [`alloc::alloc`]: crate::alloc::alloc
694    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
695    ///
696    /// # Examples
697    ///
698    /// ```
699    /// #![feature(box_vec_non_null)]
700    ///
701    /// let v = vec![1, 2, 3];
702    ///
703    /// // Deconstruct the vector into parts.
704    /// let (p, len, cap) = v.into_parts();
705    ///
706    /// unsafe {
707    ///     // Overwrite memory with 4, 5, 6
708    ///     for i in 0..len {
709    ///         p.add(i).write(4 + i);
710    ///     }
711    ///
712    ///     // Put everything back together into a Vec
713    ///     let rebuilt = Vec::from_parts(p, len, cap);
714    ///     assert_eq!(rebuilt, [4, 5, 6]);
715    /// }
716    /// ```
717    ///
718    /// Using memory that was allocated elsewhere:
719    ///
720    /// ```rust
721    /// #![feature(box_vec_non_null)]
722    ///
723    /// use std::alloc::{alloc, Layout};
724    /// use std::ptr::NonNull;
725    ///
726    /// fn main() {
727    ///     let layout = Layout::array::<u32>(16).expect("overflow cannot happen");
728    ///
729    ///     let vec = unsafe {
730    ///         let Some(mem) = NonNull::new(alloc(layout).cast::<u32>()) else {
731    ///             return;
732    ///         };
733    ///
734    ///         mem.write(1_000_000);
735    ///
736    ///         Vec::from_parts(mem, 1, 16)
737    ///     };
738    ///
739    ///     assert_eq!(vec, &[1_000_000]);
740    ///     assert_eq!(vec.capacity(), 16);
741    /// }
742    /// ```
743    #[inline]
744    #[unstable(feature = "box_vec_non_null", issue = "130364")]
745    pub unsafe fn from_parts(ptr: NonNull<T>, length: usize, capacity: usize) -> Self {
746        unsafe { Self::from_parts_in(ptr, length, capacity, Global) }
747    }
748
749    /// Creates a `Vec<T>` where each element is produced by calling `f` with
750    /// that element's index while walking forward through the `Vec<T>`.
751    ///
752    /// This is essentially the same as writing
753    ///
754    /// ```text
755    /// vec![f(0), f(1), f(2), …, f(length - 2), f(length - 1)]
756    /// ```
757    /// and is similar to `(0..i).map(f)`, just for `Vec<T>`s not iterators.
758    ///
759    /// If `length == 0`, this produces an empty `Vec<T>` without ever calling `f`.
760    ///
761    /// # Example
762    ///
763    /// ```rust
764    /// #![feature(vec_from_fn)]
765    ///
766    /// let vec = Vec::from_fn(5, |i| i);
767    ///
768    /// // indexes are:  0  1  2  3  4
769    /// assert_eq!(vec, [0, 1, 2, 3, 4]);
770    ///
771    /// let vec2 = Vec::from_fn(8, |i| i * 2);
772    ///
773    /// // indexes are:   0  1  2  3  4  5   6   7
774    /// assert_eq!(vec2, [0, 2, 4, 6, 8, 10, 12, 14]);
775    ///
776    /// let bool_vec = Vec::from_fn(5, |i| i % 2 == 0);
777    ///
778    /// // indexes are:       0     1      2     3      4
779    /// assert_eq!(bool_vec, [true, false, true, false, true]);
780    /// ```
781    ///
782    /// The `Vec<T>` is generated in ascending index order, starting from the front
783    /// and going towards the back, so you can use closures with mutable state:
784    /// ```
785    /// #![feature(vec_from_fn)]
786    ///
787    /// let mut state = 1;
788    /// let a = Vec::from_fn(6, |_| { let x = state; state *= 2; x });
789    ///
790    /// assert_eq!(a, [1, 2, 4, 8, 16, 32]);
791    /// ```
792    #[cfg(not(no_global_oom_handling))]
793    #[inline]
794    #[unstable(feature = "vec_from_fn", issue = "149698")]
795    pub fn from_fn<F>(length: usize, f: F) -> Self
796    where
797        F: FnMut(usize) -> T,
798    {
799        (0..length).map(f).collect()
800    }
801
802    /// Decomposes a `Vec<T>` into its raw components: `(pointer, length, capacity)`.
803    ///
804    /// Returns the raw pointer to the underlying data, the length of
805    /// the vector (in elements), and the allocated capacity of the
806    /// data (in elements). These are the same arguments in the same
807    /// order as the arguments to [`from_raw_parts`].
808    ///
809    /// After calling this function, the caller is responsible for the
810    /// memory previously managed by the `Vec`. Most often, one does
811    /// this by converting the raw pointer, length, and capacity back
812    /// into a `Vec` with the [`from_raw_parts`] function; more generally,
813    /// if `T` is non-zero-sized and the capacity is nonzero, one may use
814    /// any method that calls [`dealloc`] with a layout of
815    /// `Layout::array::<T>(capacity)`; if `T` is zero-sized or the
816    /// capacity is zero, nothing needs to be done.
817    ///
818    /// [`from_raw_parts`]: Vec::from_raw_parts
819    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
820    ///
821    /// # Examples
822    ///
823    /// ```
824    /// let v: Vec<i32> = vec![-1, 0, 1];
825    ///
826    /// let (ptr, len, cap) = v.into_raw_parts();
827    ///
828    /// let rebuilt = unsafe {
829    ///     // We can now make changes to the components, such as
830    ///     // transmuting the raw pointer to a compatible type.
831    ///     let ptr = ptr as *mut u32;
832    ///
833    ///     Vec::from_raw_parts(ptr, len, cap)
834    /// };
835    /// assert_eq!(rebuilt, [4294967295, 0, 1]);
836    /// ```
837    #[must_use = "losing the pointer will leak memory"]
838    #[stable(feature = "vec_into_raw_parts", since = "1.93.0")]
839    pub fn into_raw_parts(self) -> (*mut T, usize, usize) {
840        let mut me = ManuallyDrop::new(self);
841        (me.as_mut_ptr(), me.len(), me.capacity())
842    }
843
844    #[doc(alias = "into_non_null_parts")]
845    /// Decomposes a `Vec<T>` into its raw components: `(NonNull pointer, length, capacity)`.
846    ///
847    /// Returns the `NonNull` pointer to the underlying data, the length of
848    /// the vector (in elements), and the allocated capacity of the
849    /// data (in elements). These are the same arguments in the same
850    /// order as the arguments to [`from_parts`].
851    ///
852    /// After calling this function, the caller is responsible for the
853    /// memory previously managed by the `Vec`. The only way to do
854    /// this is to convert the `NonNull` pointer, length, and capacity back
855    /// into a `Vec` with the [`from_parts`] function, allowing
856    /// the destructor to perform the cleanup.
857    ///
858    /// [`from_parts`]: Vec::from_parts
859    ///
860    /// # Examples
861    ///
862    /// ```
863    /// #![feature(box_vec_non_null)]
864    ///
865    /// let v: Vec<i32> = vec![-1, 0, 1];
866    ///
867    /// let (ptr, len, cap) = v.into_parts();
868    ///
869    /// let rebuilt = unsafe {
870    ///     // We can now make changes to the components, such as
871    ///     // transmuting the raw pointer to a compatible type.
872    ///     let ptr = ptr.cast::<u32>();
873    ///
874    ///     Vec::from_parts(ptr, len, cap)
875    /// };
876    /// assert_eq!(rebuilt, [4294967295, 0, 1]);
877    /// ```
878    #[must_use = "losing the pointer will leak memory"]
879    #[unstable(feature = "box_vec_non_null", issue = "130364")]
880    pub fn into_parts(self) -> (NonNull<T>, usize, usize) {
881        let (ptr, len, capacity) = self.into_raw_parts();
882        // SAFETY: A `Vec` always has a non-null pointer.
883        (unsafe { NonNull::new_unchecked(ptr) }, len, capacity)
884    }
885
886    /// Interns the `Vec<T>`, making the underlying memory read-only. This method should be
887    /// called during compile time. (This is a no-op if called during runtime)
888    ///
889    /// This method must be called if the memory used by `Vec` needs to appear in the final
890    /// values of constants.
891    #[unstable(feature = "const_heap", issue = "79597")]
892    #[rustc_const_unstable(feature = "const_heap", issue = "79597")]
893    pub const fn const_make_global(mut self) -> &'static [T]
894    where
895        T: Freeze,
896    {
897        unsafe { core::intrinsics::const_make_global(self.as_mut_ptr().cast()) };
898        let me = ManuallyDrop::new(self);
899        unsafe { slice::from_raw_parts(me.as_ptr(), me.len) }
900    }
901}
902
903#[cfg(not(no_global_oom_handling))]
904#[rustc_const_unstable(feature = "const_heap", issue = "79597")]
905#[rustfmt::skip] // FIXME(fee1-dead): temporary measure before rustfmt is bumped
906const impl<T, A: [const] Allocator + [const] Destruct> Vec<T, A> {
907    /// Constructs a new, empty `Vec<T, A>` with at least the specified capacity
908    /// with the provided allocator.
909    ///
910    /// The vector will be able to hold at least `capacity` elements without
911    /// reallocating. This method is allowed to allocate for more elements than
912    /// `capacity`. If `capacity` is zero, the vector will not allocate.
913    ///
914    /// It is important to note that although the returned vector has the
915    /// minimum *capacity* specified, the vector will have a zero *length*. For
916    /// an explanation of the difference between length and capacity, see
917    /// *[Capacity and reallocation]*.
918    ///
919    /// If it is important to know the exact allocated capacity of a `Vec`,
920    /// always use the [`capacity`] method after construction.
921    ///
922    /// For `Vec<T, A>` where `T` is a zero-sized type, there will be no allocation
923    /// and the capacity will always be `usize::MAX`.
924    ///
925    /// [Capacity and reallocation]: #capacity-and-reallocation
926    /// [`capacity`]: Vec::capacity
927    ///
928    /// # Panics
929    ///
930    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
931    ///
932    /// # Examples
933    ///
934    /// ```
935    /// #![feature(allocator_api)]
936    ///
937    /// use std::alloc::System;
938    ///
939    /// let mut vec = Vec::with_capacity_in(10, System);
940    ///
941    /// // The vector contains no items, even though it has capacity for more
942    /// assert_eq!(vec.len(), 0);
943    /// assert!(vec.capacity() >= 10);
944    ///
945    /// // These are all done without reallocating...
946    /// for i in 0..10 {
947    ///     vec.push(i);
948    /// }
949    /// assert_eq!(vec.len(), 10);
950    /// assert!(vec.capacity() >= 10);
951    ///
952    /// // ...but this may make the vector reallocate
953    /// vec.push(11);
954    /// assert_eq!(vec.len(), 11);
955    /// assert!(vec.capacity() >= 11);
956    ///
957    /// // A vector of a zero-sized type will always over-allocate, since no
958    /// // allocation is necessary
959    /// let vec_units = Vec::<(), System>::with_capacity_in(10, System);
960    /// assert_eq!(vec_units.capacity(), usize::MAX);
961    /// ```
962    #[inline]
963    #[unstable(feature = "allocator_api", issue = "32838")]
964    pub fn with_capacity_in(capacity: usize, alloc: A) -> Self {
965        Vec { buf: RawVec::with_capacity_in(capacity, alloc), len: 0 }
966    }
967
968    /// Appends an element to the back of a collection.
969    ///
970    /// # Panics
971    ///
972    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
973    ///
974    /// # Examples
975    ///
976    /// ```
977    /// let mut vec = vec![1, 2];
978    /// vec.push(3);
979    /// assert_eq!(vec, [1, 2, 3]);
980    /// ```
981    ///
982    /// # Time complexity
983    ///
984    /// Takes amortized *O*(1) time. If the vector's length would exceed its
985    /// capacity after the push, *O*(*capacity*) time is taken to copy the
986    /// vector's elements to a larger allocation. This expensive operation is
987    /// offset by the *capacity* *O*(1) insertions it allows.
988    #[inline]
989    #[stable(feature = "rust1", since = "1.0.0")]
990    #[rustc_confusables("push_back", "put", "append")]
991    pub fn push(&mut self, value: T) {
992        let _ = self.push_mut(value);
993    }
994
995    /// Appends an element to the back of a collection, returning a reference to it.
996    ///
997    /// # Panics
998    ///
999    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1000    ///
1001    /// # Examples
1002    ///
1003    /// ```
1004    /// let mut vec = vec![1, 2];
1005    /// let last = vec.push_mut(3);
1006    /// assert_eq!(*last, 3);
1007    /// assert_eq!(vec, [1, 2, 3]);
1008    ///
1009    /// let last = vec.push_mut(3);
1010    /// *last += 1;
1011    /// assert_eq!(vec, [1, 2, 3, 4]);
1012    /// ```
1013    ///
1014    /// # Time complexity
1015    ///
1016    /// Takes amortized *O*(1) time. If the vector's length would exceed its
1017    /// capacity after the push, *O*(*capacity*) time is taken to copy the
1018    /// vector's elements to a larger allocation. This expensive operation is
1019    /// offset by the *capacity* *O*(1) insertions it allows.
1020    #[inline]
1021    #[stable(feature = "push_mut", since = "1.95.0")]
1022    #[must_use = "if you don't need a reference to the value, use `Vec::push` instead"]
1023    pub fn push_mut(&mut self, value: T) -> &mut T {
1024        // Inform codegen that the length does not change across grow_one().
1025        let len = self.len;
1026        // This will panic or abort if we would allocate > isize::MAX bytes
1027        // or if the length increment would overflow for zero-sized types.
1028        if len == self.buf.capacity() {
1029            self.buf.grow_one();
1030        }
1031        unsafe {
1032            let end = self.as_mut_ptr().add(len);
1033            ptr::write(end, value);
1034            self.len = len + 1;
1035            // SAFETY: We just wrote a value to the pointer that will live the lifetime of the reference.
1036            &mut *end
1037        }
1038    }
1039}
1040
1041impl<T, A: Allocator> Vec<T, A> {
1042    /// Constructs a new, empty `Vec<T, A>`.
1043    ///
1044    /// The vector will not allocate until elements are pushed onto it.
1045    ///
1046    /// # Examples
1047    ///
1048    /// ```
1049    /// #![feature(allocator_api)]
1050    ///
1051    /// use std::alloc::System;
1052    ///
1053    /// # #[allow(unused_mut)]
1054    /// let mut vec: Vec<i32, _> = Vec::new_in(System);
1055    /// ```
1056    #[inline]
1057    #[unstable(feature = "allocator_api", issue = "32838")]
1058    pub const fn new_in(alloc: A) -> Self {
1059        Vec { buf: RawVec::new_in(alloc), len: 0 }
1060    }
1061
1062    /// Constructs a new, empty `Vec<T, A>` with at least the specified capacity
1063    /// with the provided allocator.
1064    ///
1065    /// The vector will be able to hold at least `capacity` elements without
1066    /// reallocating. This method is allowed to allocate for more elements than
1067    /// `capacity`. If `capacity` is zero, the vector will not allocate.
1068    ///
1069    /// # Errors
1070    ///
1071    /// Returns an error if the capacity exceeds `isize::MAX` _bytes_,
1072    /// or if the allocator reports allocation failure.
1073    #[inline]
1074    #[unstable(feature = "allocator_api", issue = "32838")]
1075    // #[unstable(feature = "try_with_capacity", issue = "91913")]
1076    pub fn try_with_capacity_in(capacity: usize, alloc: A) -> Result<Self, TryReserveError> {
1077        Ok(Vec { buf: RawVec::try_with_capacity_in(capacity, alloc)?, len: 0 })
1078    }
1079
1080    /// Creates a `Vec<T, A>` directly from a pointer, a length, a capacity,
1081    /// and an allocator.
1082    ///
1083    /// # Safety
1084    ///
1085    /// This is highly unsafe, due to the number of invariants that aren't
1086    /// checked:
1087    ///
1088    /// * `ptr` must be [*currently allocated*] via the given allocator `alloc`.
1089    /// * `T` needs to have the same alignment as what `ptr` was allocated with.
1090    ///   (`T` having a less strict alignment is not sufficient, the alignment really
1091    ///   needs to be equal to satisfy the [`dealloc`] requirement that memory must be
1092    ///   allocated and deallocated with the same layout.)
1093    /// * The size of `T` times the `capacity` (ie. the allocated size in bytes) needs
1094    ///   to be the same size as the pointer was allocated with. (Because similar to
1095    ///   alignment, [`dealloc`] must be called with the same layout `size`.)
1096    /// * `length` needs to be less than or equal to `capacity`.
1097    /// * The first `length` values must be properly initialized values of type `T`.
1098    /// * `capacity` needs to [*fit*] the layout size that the pointer was allocated with.
1099    /// * The allocated size in bytes must be no larger than `isize::MAX`.
1100    ///   See the safety documentation of [`pointer::offset`].
1101    ///
1102    /// These requirements are always upheld by any `ptr` that has been allocated
1103    /// via `Vec<T, A>`. Other allocation sources are allowed if the invariants are
1104    /// upheld.
1105    ///
1106    /// Violating these may cause problems like corrupting the allocator's
1107    /// internal data structures. For example it is **not** safe
1108    /// to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`.
1109    /// It's also not safe to build one from a `Vec<u16>` and its length, because
1110    /// the allocator cares about the alignment, and these two types have different
1111    /// alignments. The buffer was allocated with alignment 2 (for `u16`), but after
1112    /// turning it into a `Vec<u8>` it'll be deallocated with alignment 1.
1113    ///
1114    /// The ownership of `ptr` is effectively transferred to the
1115    /// `Vec<T>` which may then deallocate, reallocate or change the
1116    /// contents of memory pointed to by the pointer at will. Ensure
1117    /// that nothing else uses the pointer after calling this
1118    /// function.
1119    ///
1120    /// [`String`]: crate::string::String
1121    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
1122    /// [*currently allocated*]: crate::alloc::Allocator#currently-allocated-memory
1123    /// [*fit*]: crate::alloc::Allocator#memory-fitting
1124    ///
1125    /// # Examples
1126    ///
1127    /// ```
1128    /// #![feature(allocator_api)]
1129    ///
1130    /// use std::alloc::System;
1131    ///
1132    /// use std::ptr;
1133    ///
1134    /// let mut v = Vec::with_capacity_in(3, System);
1135    /// v.push(1);
1136    /// v.push(2);
1137    /// v.push(3);
1138    ///
1139    /// // Deconstruct the vector into parts.
1140    /// let (p, len, cap, alloc) = v.into_raw_parts_with_alloc();
1141    ///
1142    /// unsafe {
1143    ///     // Overwrite memory with 4, 5, 6
1144    ///     for i in 0..len {
1145    ///         ptr::write(p.add(i), 4 + i);
1146    ///     }
1147    ///
1148    ///     // Put everything back together into a Vec
1149    ///     let rebuilt = Vec::from_raw_parts_in(p, len, cap, alloc.clone());
1150    ///     assert_eq!(rebuilt, [4, 5, 6]);
1151    /// }
1152    /// ```
1153    ///
1154    /// Using memory that was allocated elsewhere:
1155    ///
1156    /// ```rust
1157    /// #![feature(allocator_api)]
1158    ///
1159    /// use std::alloc::{AllocError, Allocator, Global, Layout};
1160    ///
1161    /// fn main() {
1162    ///     let layout = Layout::array::<u32>(16).expect("overflow cannot happen");
1163    ///
1164    ///     let vec = unsafe {
1165    ///         let mem = match Global.allocate(layout) {
1166    ///             Ok(mem) => mem.cast::<u32>().as_ptr(),
1167    ///             Err(AllocError) => return,
1168    ///         };
1169    ///
1170    ///         mem.write(1_000_000);
1171    ///
1172    ///         Vec::from_raw_parts_in(mem, 1, 16, Global)
1173    ///     };
1174    ///
1175    ///     assert_eq!(vec, &[1_000_000]);
1176    ///     assert_eq!(vec.capacity(), 16);
1177    /// }
1178    /// ```
1179    #[inline]
1180    #[unstable(feature = "allocator_api", issue = "32838")]
1181    pub unsafe fn from_raw_parts_in(ptr: *mut T, length: usize, capacity: usize, alloc: A) -> Self {
1182        ub_checks::assert_unsafe_precondition!(
1183            check_library_ub,
1184            "Vec::from_raw_parts_in requires that length <= capacity",
1185            (length: usize = length, capacity: usize = capacity) => length <= capacity
1186        );
1187        unsafe { Vec { buf: RawVec::from_raw_parts_in(ptr, capacity, alloc), len: length } }
1188    }
1189
1190    #[doc(alias = "from_non_null_parts_in")]
1191    /// Creates a `Vec<T, A>` directly from a `NonNull` pointer, a length, a capacity,
1192    /// and an allocator.
1193    ///
1194    /// # Safety
1195    ///
1196    /// This is highly unsafe, due to the number of invariants that aren't
1197    /// checked:
1198    ///
1199    /// * `ptr` must be [*currently allocated*] via the given allocator `alloc`.
1200    /// * `T` needs to have the same alignment as what `ptr` was allocated with.
1201    ///   (`T` having a less strict alignment is not sufficient, the alignment really
1202    ///   needs to be equal to satisfy the [`dealloc`] requirement that memory must be
1203    ///   allocated and deallocated with the same layout.)
1204    /// * The size of `T` times the `capacity` (ie. the allocated size in bytes) needs
1205    ///   to be the same size as the pointer was allocated with. (Because similar to
1206    ///   alignment, [`dealloc`] must be called with the same layout `size`.)
1207    /// * `length` needs to be less than or equal to `capacity`.
1208    /// * The first `length` values must be properly initialized values of type `T`.
1209    /// * `capacity` needs to [*fit*] the layout size that the pointer was allocated with.
1210    /// * The allocated size in bytes must be no larger than `isize::MAX`.
1211    ///   See the safety documentation of [`pointer::offset`].
1212    ///
1213    /// These requirements are always upheld by any `ptr` that has been allocated
1214    /// via `Vec<T, A>`. Other allocation sources are allowed if the invariants are
1215    /// upheld.
1216    ///
1217    /// Violating these may cause problems like corrupting the allocator's
1218    /// internal data structures. For example it is **not** safe
1219    /// to build a `Vec<u8>` from a pointer to a C `char` array with length `size_t`.
1220    /// It's also not safe to build one from a `Vec<u16>` and its length, because
1221    /// the allocator cares about the alignment, and these two types have different
1222    /// alignments. The buffer was allocated with alignment 2 (for `u16`), but after
1223    /// turning it into a `Vec<u8>` it'll be deallocated with alignment 1.
1224    ///
1225    /// The ownership of `ptr` is effectively transferred to the
1226    /// `Vec<T>` which may then deallocate, reallocate or change the
1227    /// contents of memory pointed to by the pointer at will. Ensure
1228    /// that nothing else uses the pointer after calling this
1229    /// function.
1230    ///
1231    /// [`String`]: crate::string::String
1232    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
1233    /// [*currently allocated*]: crate::alloc::Allocator#currently-allocated-memory
1234    /// [*fit*]: crate::alloc::Allocator#memory-fitting
1235    ///
1236    /// # Examples
1237    ///
1238    /// ```
1239    /// #![feature(allocator_api)]
1240    ///
1241    /// use std::alloc::System;
1242    ///
1243    /// let mut v = Vec::with_capacity_in(3, System);
1244    /// v.push(1);
1245    /// v.push(2);
1246    /// v.push(3);
1247    ///
1248    /// // Deconstruct the vector into parts.
1249    /// let (p, len, cap, alloc) = v.into_parts_with_alloc();
1250    ///
1251    /// unsafe {
1252    ///     // Overwrite memory with 4, 5, 6
1253    ///     for i in 0..len {
1254    ///         p.add(i).write(4 + i);
1255    ///     }
1256    ///
1257    ///     // Put everything back together into a Vec
1258    ///     let rebuilt = Vec::from_parts_in(p, len, cap, alloc.clone());
1259    ///     assert_eq!(rebuilt, [4, 5, 6]);
1260    /// }
1261    /// ```
1262    ///
1263    /// Using memory that was allocated elsewhere:
1264    ///
1265    /// ```rust
1266    /// #![feature(allocator_api)]
1267    ///
1268    /// use std::alloc::{AllocError, Allocator, Global, Layout};
1269    ///
1270    /// fn main() {
1271    ///     let layout = Layout::array::<u32>(16).expect("overflow cannot happen");
1272    ///
1273    ///     let vec = unsafe {
1274    ///         let mem = match Global.allocate(layout) {
1275    ///             Ok(mem) => mem.cast::<u32>(),
1276    ///             Err(AllocError) => return,
1277    ///         };
1278    ///
1279    ///         mem.write(1_000_000);
1280    ///
1281    ///         Vec::from_parts_in(mem, 1, 16, Global)
1282    ///     };
1283    ///
1284    ///     assert_eq!(vec, &[1_000_000]);
1285    ///     assert_eq!(vec.capacity(), 16);
1286    /// }
1287    /// ```
1288    #[inline]
1289    #[unstable(feature = "allocator_api", issue = "32838")]
1290    // #[unstable(feature = "box_vec_non_null", issue = "130364")]
1291    pub unsafe fn from_parts_in(ptr: NonNull<T>, length: usize, capacity: usize, alloc: A) -> Self {
1292        ub_checks::assert_unsafe_precondition!(
1293            check_library_ub,
1294            "Vec::from_parts_in requires that length <= capacity",
1295            (length: usize = length, capacity: usize = capacity) => length <= capacity
1296        );
1297        unsafe { Vec { buf: RawVec::from_nonnull_in(ptr, capacity, alloc), len: length } }
1298    }
1299
1300    /// Decomposes a `Vec<T>` into its raw components: `(pointer, length, capacity, allocator)`.
1301    ///
1302    /// Returns the raw pointer to the underlying data, the length of the vector (in elements),
1303    /// the allocated capacity of the data (in elements), and the allocator. These are the same
1304    /// arguments in the same order as the arguments to [`from_raw_parts_in`].
1305    ///
1306    /// After calling this function, the caller is responsible for the
1307    /// memory previously managed by the `Vec`. The only way to do
1308    /// this is to convert the raw pointer, length, and capacity back
1309    /// into a `Vec` with the [`from_raw_parts_in`] function, allowing
1310    /// the destructor to perform the cleanup.
1311    ///
1312    /// [`from_raw_parts_in`]: Vec::from_raw_parts_in
1313    ///
1314    /// # Examples
1315    ///
1316    /// ```
1317    /// #![feature(allocator_api)]
1318    ///
1319    /// use std::alloc::System;
1320    ///
1321    /// let mut v: Vec<i32, System> = Vec::new_in(System);
1322    /// v.push(-1);
1323    /// v.push(0);
1324    /// v.push(1);
1325    ///
1326    /// let (ptr, len, cap, alloc) = v.into_raw_parts_with_alloc();
1327    ///
1328    /// let rebuilt = unsafe {
1329    ///     // We can now make changes to the components, such as
1330    ///     // transmuting the raw pointer to a compatible type.
1331    ///     let ptr = ptr as *mut u32;
1332    ///
1333    ///     Vec::from_raw_parts_in(ptr, len, cap, alloc)
1334    /// };
1335    /// assert_eq!(rebuilt, [4294967295, 0, 1]);
1336    /// ```
1337    #[must_use = "losing the pointer will leak memory"]
1338    #[unstable(feature = "allocator_api", issue = "32838")]
1339    pub fn into_raw_parts_with_alloc(self) -> (*mut T, usize, usize, A) {
1340        let mut me = ManuallyDrop::new(self);
1341        let len = me.len();
1342        let capacity = me.capacity();
1343        let ptr = me.as_mut_ptr();
1344        let alloc = unsafe { ptr::read(me.allocator()) };
1345        (ptr, len, capacity, alloc)
1346    }
1347
1348    #[doc(alias = "into_non_null_parts_with_alloc")]
1349    /// Decomposes a `Vec<T>` into its raw components: `(NonNull pointer, length, capacity, allocator)`.
1350    ///
1351    /// Returns the `NonNull` pointer to the underlying data, the length of the vector (in elements),
1352    /// the allocated capacity of the data (in elements), and the allocator. These are the same
1353    /// arguments in the same order as the arguments to [`from_parts_in`].
1354    ///
1355    /// After calling this function, the caller is responsible for the
1356    /// memory previously managed by the `Vec`. The only way to do
1357    /// this is to convert the `NonNull` pointer, length, and capacity back
1358    /// into a `Vec` with the [`from_parts_in`] function, allowing
1359    /// the destructor to perform the cleanup.
1360    ///
1361    /// [`from_parts_in`]: Vec::from_parts_in
1362    ///
1363    /// # Examples
1364    ///
1365    /// ```
1366    /// #![feature(allocator_api)]
1367    ///
1368    /// use std::alloc::System;
1369    ///
1370    /// let mut v: Vec<i32, System> = Vec::new_in(System);
1371    /// v.push(-1);
1372    /// v.push(0);
1373    /// v.push(1);
1374    ///
1375    /// let (ptr, len, cap, alloc) = v.into_parts_with_alloc();
1376    ///
1377    /// let rebuilt = unsafe {
1378    ///     // We can now make changes to the components, such as
1379    ///     // transmuting the raw pointer to a compatible type.
1380    ///     let ptr = ptr.cast::<u32>();
1381    ///
1382    ///     Vec::from_parts_in(ptr, len, cap, alloc)
1383    /// };
1384    /// assert_eq!(rebuilt, [4294967295, 0, 1]);
1385    /// ```
1386    #[must_use = "losing the pointer will leak memory"]
1387    #[unstable(feature = "allocator_api", issue = "32838")]
1388    // #[unstable(feature = "box_vec_non_null", issue = "130364")]
1389    pub fn into_parts_with_alloc(self) -> (NonNull<T>, usize, usize, A) {
1390        let (ptr, len, capacity, alloc) = self.into_raw_parts_with_alloc();
1391        // SAFETY: A `Vec` always has a non-null pointer.
1392        (unsafe { NonNull::new_unchecked(ptr) }, len, capacity, alloc)
1393    }
1394
1395    /// Returns the total number of elements the vector can hold without
1396    /// reallocating.
1397    ///
1398    /// # Examples
1399    ///
1400    /// ```
1401    /// let mut vec: Vec<i32> = Vec::with_capacity(10);
1402    /// vec.push(42);
1403    /// assert!(vec.capacity() >= 10);
1404    /// ```
1405    ///
1406    /// A vector with zero-sized elements will always have a capacity of usize::MAX:
1407    ///
1408    /// ```
1409    /// #[derive(Clone)]
1410    /// struct ZeroSized;
1411    ///
1412    /// fn main() {
1413    ///     assert_eq!(std::mem::size_of::<ZeroSized>(), 0);
1414    ///     let v = vec![ZeroSized; 0];
1415    ///     assert_eq!(v.capacity(), usize::MAX);
1416    /// }
1417    /// ```
1418    #[inline]
1419    #[stable(feature = "rust1", since = "1.0.0")]
1420    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1421    pub const fn capacity(&self) -> usize {
1422        self.buf.capacity()
1423    }
1424
1425    /// Reserves capacity for at least `additional` more elements to be inserted
1426    /// in the given `Vec<T>`. The collection may reserve more space to
1427    /// speculatively avoid frequent reallocations. After calling `reserve`,
1428    /// capacity will be greater than or equal to `self.len() + additional`.
1429    /// Does nothing if capacity is already sufficient.
1430    ///
1431    /// # Panics
1432    ///
1433    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1434    ///
1435    /// # Examples
1436    ///
1437    /// ```
1438    /// let mut vec = vec![1];
1439    /// vec.reserve(10);
1440    /// assert!(vec.capacity() >= 11);
1441    /// ```
1442    #[cfg(not(no_global_oom_handling))]
1443    #[stable(feature = "rust1", since = "1.0.0")]
1444    #[rustc_diagnostic_item = "vec_reserve"]
1445    pub fn reserve(&mut self, additional: usize) {
1446        self.buf.reserve(self.len, additional);
1447    }
1448
1449    /// Reserves the minimum capacity for at least `additional` more elements to
1450    /// be inserted in the given `Vec<T>`. Unlike [`reserve`], this will not
1451    /// deliberately over-allocate to speculatively avoid frequent allocations.
1452    /// After calling `reserve_exact`, capacity will be greater than or equal to
1453    /// `self.len() + additional`. Does nothing if the capacity is already
1454    /// sufficient.
1455    ///
1456    /// Note that the allocator may give the collection more space than it
1457    /// requests. Therefore, capacity can not be relied upon to be precisely
1458    /// minimal. Prefer [`reserve`] if future insertions are expected.
1459    ///
1460    /// [`reserve`]: Vec::reserve
1461    ///
1462    /// # Panics
1463    ///
1464    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1465    ///
1466    /// # Examples
1467    ///
1468    /// ```
1469    /// let mut vec = vec![1];
1470    /// vec.reserve_exact(10);
1471    /// assert!(vec.capacity() >= 11);
1472    /// ```
1473    #[cfg(not(no_global_oom_handling))]
1474    #[stable(feature = "rust1", since = "1.0.0")]
1475    pub fn reserve_exact(&mut self, additional: usize) {
1476        self.buf.reserve_exact(self.len, additional);
1477    }
1478
1479    /// Tries to reserve capacity for at least `additional` more elements to be inserted
1480    /// in the given `Vec<T>`. The collection may reserve more space to speculatively avoid
1481    /// frequent reallocations. After calling `try_reserve`, capacity will be
1482    /// greater than or equal to `self.len() + additional` if it returns
1483    /// `Ok(())`. Does nothing if capacity is already sufficient. This method
1484    /// preserves the contents even if an error occurs.
1485    ///
1486    /// # Errors
1487    ///
1488    /// If the capacity overflows, or the allocator reports a failure, then an error
1489    /// is returned.
1490    ///
1491    /// # Examples
1492    ///
1493    /// ```
1494    /// use std::collections::TryReserveError;
1495    ///
1496    /// fn process_data(data: &[u32]) -> Result<Vec<u32>, TryReserveError> {
1497    ///     let mut output = Vec::new();
1498    ///
1499    ///     // Pre-reserve the memory, exiting if we can't
1500    ///     output.try_reserve(data.len())?;
1501    ///
1502    ///     // Now we know this can't OOM in the middle of our complex work
1503    ///     output.extend(data.iter().map(|&val| {
1504    ///         val * 2 + 5 // very complicated
1505    ///     }));
1506    ///
1507    ///     Ok(output)
1508    /// }
1509    /// # process_data(&[1, 2, 3]).expect("why is the test harness OOMing on 12 bytes?");
1510    /// ```
1511    #[stable(feature = "try_reserve", since = "1.57.0")]
1512    pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError> {
1513        self.buf.try_reserve(self.len, additional)
1514    }
1515
1516    /// Tries to reserve the minimum capacity for at least `additional`
1517    /// elements to be inserted in the given `Vec<T>`. Unlike [`try_reserve`],
1518    /// this will not deliberately over-allocate to speculatively avoid frequent
1519    /// allocations. After calling `try_reserve_exact`, capacity will be greater
1520    /// than or equal to `self.len() + additional` if it returns `Ok(())`.
1521    /// Does nothing if the capacity is already sufficient.
1522    ///
1523    /// Note that the allocator may give the collection more space than it
1524    /// requests. Therefore, capacity can not be relied upon to be precisely
1525    /// minimal. Prefer [`try_reserve`] if future insertions are expected.
1526    ///
1527    /// [`try_reserve`]: Vec::try_reserve
1528    ///
1529    /// # Errors
1530    ///
1531    /// If the capacity overflows, or the allocator reports a failure, then an error
1532    /// is returned.
1533    ///
1534    /// # Examples
1535    ///
1536    /// ```
1537    /// use std::collections::TryReserveError;
1538    ///
1539    /// fn process_data(data: &[u32]) -> Result<Vec<u32>, TryReserveError> {
1540    ///     let mut output = Vec::new();
1541    ///
1542    ///     // Pre-reserve the memory, exiting if we can't
1543    ///     output.try_reserve_exact(data.len())?;
1544    ///
1545    ///     // Now we know this can't OOM in the middle of our complex work
1546    ///     output.extend(data.iter().map(|&val| {
1547    ///         val * 2 + 5 // very complicated
1548    ///     }));
1549    ///
1550    ///     Ok(output)
1551    /// }
1552    /// # process_data(&[1, 2, 3]).expect("why is the test harness OOMing on 12 bytes?");
1553    /// ```
1554    #[stable(feature = "try_reserve", since = "1.57.0")]
1555    pub fn try_reserve_exact(&mut self, additional: usize) -> Result<(), TryReserveError> {
1556        self.buf.try_reserve_exact(self.len, additional)
1557    }
1558
1559    /// Shrinks the capacity of the vector as much as possible.
1560    ///
1561    /// The behavior of this method depends on the allocator, which may either shrink the vector
1562    /// in-place or reallocate. The resulting vector might still have some excess capacity, just as
1563    /// is the case for [`with_capacity`]. See [`Allocator::shrink`] for more details.
1564    ///
1565    /// [`with_capacity`]: Vec::with_capacity
1566    ///
1567    /// # Examples
1568    ///
1569    /// ```
1570    /// let mut vec = Vec::with_capacity(10);
1571    /// vec.extend([1, 2, 3]);
1572    /// assert!(vec.capacity() >= 10);
1573    /// vec.shrink_to_fit();
1574    /// assert!(vec.capacity() >= 3);
1575    /// ```
1576    #[cfg(not(no_global_oom_handling))]
1577    #[stable(feature = "rust1", since = "1.0.0")]
1578    #[inline]
1579    pub fn shrink_to_fit(&mut self) {
1580        // The capacity is never less than the length, and there's nothing to do when
1581        // they are equal, so we can avoid the panic case in `RawVec::shrink_to_fit`
1582        // by only calling it with a greater capacity.
1583        if self.capacity() > self.len {
1584            self.buf.shrink_to_fit(self.len);
1585        }
1586    }
1587
1588    /// Shrinks the capacity of the vector with a lower bound.
1589    ///
1590    /// The capacity will remain at least as large as both the length
1591    /// and the supplied value.
1592    ///
1593    /// If the current capacity is less than the lower limit, this is a no-op.
1594    ///
1595    /// # Examples
1596    ///
1597    /// ```
1598    /// let mut vec = Vec::with_capacity(10);
1599    /// vec.extend([1, 2, 3]);
1600    /// assert!(vec.capacity() >= 10);
1601    /// vec.shrink_to(4);
1602    /// assert!(vec.capacity() >= 4);
1603    /// vec.shrink_to(0);
1604    /// assert!(vec.capacity() >= 3);
1605    /// ```
1606    #[cfg(not(no_global_oom_handling))]
1607    #[stable(feature = "shrink_to", since = "1.56.0")]
1608    pub fn shrink_to(&mut self, min_capacity: usize) {
1609        if self.capacity() > min_capacity {
1610            self.buf.shrink_to_fit(cmp::max(self.len, min_capacity));
1611        }
1612    }
1613
1614    /// Tries to shrink the capacity of the vector as much as possible
1615    ///
1616    /// The behavior of this method depends on the allocator, which may either shrink the vector
1617    /// in-place or reallocate. The resulting vector might still have some excess capacity, just as
1618    /// is the case for [`with_capacity`]. See [`Allocator::shrink`] for more details.
1619    ///
1620    /// [`with_capacity`]: Vec::with_capacity
1621    ///
1622    /// # Errors
1623    ///
1624    /// This function returns an error if the allocator fails to shrink the allocation,
1625    /// the vector thereafter is still safe to use, the capacity remains unchanged
1626    /// however. See [`Allocator::shrink`].
1627    ///
1628    /// # Examples
1629    ///
1630    /// ```
1631    /// #![feature(vec_fallible_shrink)]
1632    ///
1633    /// let mut vec = Vec::with_capacity(10);
1634    /// vec.extend([1, 2, 3]);
1635    /// assert!(vec.capacity() >= 10);
1636    /// vec.try_shrink_to_fit().expect("why is the test harness failing to shrink to 12 bytes");
1637    /// assert!(vec.capacity() >= 3);
1638    /// ```
1639    #[unstable(feature = "vec_fallible_shrink", issue = "152350")]
1640    #[inline]
1641    pub fn try_shrink_to_fit(&mut self) -> Result<(), TryReserveError> {
1642        if self.capacity() > self.len { self.buf.try_shrink_to_fit(self.len) } else { Ok(()) }
1643    }
1644
1645    /// Shrinks the capacity of the vector with a lower bound.
1646    ///
1647    /// The capacity will remain at least as large as both the length
1648    /// and the supplied value.
1649    ///
1650    /// If the current capacity is less than the lower limit, this is a no-op.
1651    ///
1652    /// # Errors
1653    ///
1654    /// This function returns an error if the allocator fails to shrink the allocation,
1655    /// the vector thereafter is still safe to use, the capacity remains unchanged
1656    /// however. See [`Allocator::shrink`].
1657    ///
1658    /// # Examples
1659    ///
1660    /// ```
1661    /// #![feature(vec_fallible_shrink)]
1662    ///
1663    /// let mut vec = Vec::with_capacity(10);
1664    /// vec.extend([1, 2, 3]);
1665    /// assert!(vec.capacity() >= 10);
1666    /// vec.try_shrink_to(4).expect("why is the test harness failing to shrink to 12 bytes");
1667    /// assert!(vec.capacity() >= 4);
1668    /// vec.try_shrink_to(0).expect("this is a no-op and thus the allocator isn't involved.");
1669    /// assert!(vec.capacity() >= 3);
1670    /// ```
1671    #[unstable(feature = "vec_fallible_shrink", issue = "152350")]
1672    #[inline]
1673    pub fn try_shrink_to(&mut self, min_capacity: usize) -> Result<(), TryReserveError> {
1674        if self.capacity() > min_capacity {
1675            self.buf.try_shrink_to_fit(cmp::max(self.len, min_capacity))
1676        } else {
1677            Ok(())
1678        }
1679    }
1680
1681    /// Converts the vector into [`Box<[T]>`][owned slice].
1682    ///
1683    /// Before doing the conversion, this method discards excess capacity like [`shrink_to_fit`].
1684    ///
1685    /// [owned slice]: Box
1686    /// [`shrink_to_fit`]: Vec::shrink_to_fit
1687    ///
1688    /// # Examples
1689    ///
1690    /// ```
1691    /// let v = vec![1, 2, 3];
1692    ///
1693    /// let slice = v.into_boxed_slice();
1694    /// ```
1695    ///
1696    /// Any excess capacity is removed:
1697    ///
1698    /// ```
1699    /// let mut vec = Vec::with_capacity(10);
1700    /// vec.extend([1, 2, 3]);
1701    ///
1702    /// assert!(vec.capacity() >= 10);
1703    /// let slice = vec.into_boxed_slice();
1704    /// assert_eq!(slice.into_vec().capacity(), 3);
1705    /// ```
1706    #[cfg(not(no_global_oom_handling))]
1707    #[stable(feature = "rust1", since = "1.0.0")]
1708    pub fn into_boxed_slice(mut self) -> Box<[T], A> {
1709        unsafe {
1710            self.shrink_to_fit();
1711            let me = ManuallyDrop::new(self);
1712            let buf = ptr::read(&me.buf);
1713            let len = me.len();
1714            buf.into_box(len).assume_init()
1715        }
1716    }
1717
1718    /// Shortens the vector, keeping the first `len` elements and dropping
1719    /// the rest.
1720    ///
1721    /// If `len` is greater or equal to the vector's current length, this has
1722    /// no effect.
1723    ///
1724    /// The [`drain`] method can emulate `truncate`, but causes the excess
1725    /// elements to be returned instead of dropped.
1726    ///
1727    /// Note that this method has no effect on the allocated capacity
1728    /// of the vector.
1729    ///
1730    /// # Examples
1731    ///
1732    /// Truncating a five element vector to two elements:
1733    ///
1734    /// ```
1735    /// let mut vec = vec![1, 2, 3, 4, 5];
1736    /// vec.truncate(2);
1737    /// assert_eq!(vec, [1, 2]);
1738    /// ```
1739    ///
1740    /// No truncation occurs when `len` is greater than the vector's current
1741    /// length:
1742    ///
1743    /// ```
1744    /// let mut vec = vec![1, 2, 3];
1745    /// vec.truncate(8);
1746    /// assert_eq!(vec, [1, 2, 3]);
1747    /// ```
1748    ///
1749    /// Truncating when `len == 0` is equivalent to calling the [`clear`]
1750    /// method.
1751    ///
1752    /// ```
1753    /// let mut vec = vec![1, 2, 3];
1754    /// vec.truncate(0);
1755    /// assert_eq!(vec, []);
1756    /// ```
1757    ///
1758    /// [`clear`]: Vec::clear
1759    /// [`drain`]: Vec::drain
1760    #[stable(feature = "rust1", since = "1.0.0")]
1761    pub fn truncate(&mut self, len: usize) {
1762        // This is safe because:
1763        //
1764        // * the slice passed to `drop_in_place` is valid; the `len > self.len`
1765        //   case avoids creating an invalid slice, and
1766        // * the `len` of the vector is shrunk before calling `drop_in_place`,
1767        //   such that no value will be dropped twice in case `drop_in_place`
1768        //   were to panic once (if it panics twice, the program aborts).
1769        unsafe {
1770            // Note: It's intentional that this is `>` and not `>=`.
1771            //       Changing it to `>=` has negative performance
1772            //       implications in some cases. See #78884 for more.
1773            if len > self.len {
1774                return;
1775            }
1776            let remaining_len = self.len - len;
1777            let s = ptr::slice_from_raw_parts_mut(self.as_mut_ptr().add(len), remaining_len);
1778            self.len = len;
1779            ptr::drop_in_place(s);
1780        }
1781    }
1782
1783    /// Extracts a slice containing the entire vector.
1784    ///
1785    /// Equivalent to `&s[..]`.
1786    ///
1787    /// # Examples
1788    ///
1789    /// ```
1790    /// use std::io::{self, Write};
1791    /// let buffer = vec![1, 2, 3, 5, 8];
1792    /// io::sink().write(buffer.as_slice()).unwrap();
1793    /// ```
1794    #[inline]
1795    #[stable(feature = "vec_as_slice", since = "1.7.0")]
1796    #[rustc_diagnostic_item = "vec_as_slice"]
1797    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1798    pub const fn as_slice(&self) -> &[T] {
1799        // SAFETY: `slice::from_raw_parts` requires pointee is a contiguous, aligned buffer of size
1800        // `len` containing properly-initialized `T`s. Data must not be mutated for the returned
1801        // lifetime. Further, `len * size_of::<T>` <= `isize::MAX`, and allocation does not
1802        // "wrap" through overflowing memory addresses.
1803        //
1804        // * Vec API guarantees that self.buf:
1805        //      * contains only properly-initialized items within 0..len
1806        //      * is aligned, contiguous, and valid for `len` reads
1807        //      * obeys size and address-wrapping constraints
1808        //
1809        // * We only construct `&mut` references to `self.buf` through `&mut self` methods; borrow-
1810        //   check ensures that it is not possible to mutably alias `self.buf` within the
1811        //   returned lifetime.
1812        unsafe {
1813            // normally this would use `slice::from_raw_parts`, but it's
1814            // instantiated often enough that avoiding the UB check is worth it
1815            &*core::intrinsics::aggregate_raw_ptr::<*const [T], _, _>(self.as_ptr(), self.len)
1816        }
1817    }
1818
1819    /// Extracts a mutable slice of the entire vector.
1820    ///
1821    /// Equivalent to `&mut s[..]`.
1822    ///
1823    /// # Examples
1824    ///
1825    /// ```
1826    /// use std::io::{self, Read};
1827    /// let mut buffer = vec![0; 3];
1828    /// io::repeat(0b101).read_exact(buffer.as_mut_slice()).unwrap();
1829    /// ```
1830    #[inline]
1831    #[stable(feature = "vec_as_slice", since = "1.7.0")]
1832    #[rustc_diagnostic_item = "vec_as_mut_slice"]
1833    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1834    pub const fn as_mut_slice(&mut self) -> &mut [T] {
1835        // SAFETY: `slice::from_raw_parts_mut` requires pointee is a contiguous, aligned buffer of
1836        // size `len` containing properly-initialized `T`s. Data must not be accessed through any
1837        // other pointer for the returned lifetime. Further, `len * size_of::<T>` <=
1838        // `ISIZE::MAX` and allocation does not "wrap" through overflowing memory addresses.
1839        //
1840        // * Vec API guarantees that self.buf:
1841        //      * contains only properly-initialized items within 0..len
1842        //      * is aligned, contiguous, and valid for `len` reads
1843        //      * obeys size and address-wrapping constraints
1844        //
1845        // * We only construct references to `self.buf` through `&self` and `&mut self` methods;
1846        //   borrow-check ensures that it is not possible to construct a reference to `self.buf`
1847        //   within the returned lifetime.
1848        unsafe {
1849            // normally this would use `slice::from_raw_parts_mut`, but it's
1850            // instantiated often enough that avoiding the UB check is worth it
1851            &mut *core::intrinsics::aggregate_raw_ptr::<*mut [T], _, _>(self.as_mut_ptr(), self.len)
1852        }
1853    }
1854
1855    /// Returns a raw pointer to the vector's buffer, or a dangling raw pointer
1856    /// valid for zero sized reads if the vector didn't allocate.
1857    ///
1858    /// The caller must ensure that the vector outlives the pointer this
1859    /// function returns, or else it will end up dangling.
1860    /// Modifying the vector may cause its buffer to be reallocated,
1861    /// which would also make any pointers to it invalid.
1862    ///
1863    /// The caller must also ensure that the memory the pointer (non-transitively) points to
1864    /// is never written to (except inside an `UnsafeCell`) using this pointer or any pointer
1865    /// derived from it. If you need to mutate the contents of the slice, use [`as_mut_ptr`].
1866    ///
1867    /// This method guarantees that for the purpose of the aliasing model, this method
1868    /// does not materialize a reference to the underlying slice, and thus the returned pointer
1869    /// will remain valid when mixed with other calls to [`as_ptr`], [`as_mut_ptr`],
1870    /// and [`as_non_null`].
1871    /// Note that calling other methods that materialize mutable references to the slice,
1872    /// or mutable references to specific elements you are planning on accessing through this pointer,
1873    /// as well as writing to those elements, may still invalidate this pointer.
1874    /// See the second example below for how this guarantee can be used.
1875    ///
1876    ///
1877    /// # Examples
1878    ///
1879    /// ```
1880    /// let x = vec![1, 2, 4];
1881    /// let x_ptr = x.as_ptr();
1882    ///
1883    /// unsafe {
1884    ///     for i in 0..x.len() {
1885    ///         assert_eq!(*x_ptr.add(i), 1 << i);
1886    ///     }
1887    /// }
1888    /// ```
1889    ///
1890    /// Due to the aliasing guarantee, the following code is legal:
1891    ///
1892    /// ```rust
1893    /// unsafe {
1894    ///     let mut v = vec![0, 1, 2];
1895    ///     let ptr1 = v.as_ptr();
1896    ///     let _ = ptr1.read();
1897    ///     let ptr2 = v.as_mut_ptr().offset(2);
1898    ///     ptr2.write(2);
1899    ///     // Notably, the write to `ptr2` did *not* invalidate `ptr1`
1900    ///     // because it mutated a different element:
1901    ///     let _ = ptr1.read();
1902    /// }
1903    /// ```
1904    ///
1905    /// [`as_mut_ptr`]: Vec::as_mut_ptr
1906    /// [`as_ptr`]: Vec::as_ptr
1907    /// [`as_non_null`]: Vec::as_non_null
1908    #[stable(feature = "vec_as_ptr", since = "1.37.0")]
1909    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1910    #[rustc_never_returns_null_ptr]
1911    #[rustc_as_ptr]
1912    #[inline]
1913    pub const fn as_ptr(&self) -> *const T {
1914        // We shadow the slice method of the same name to avoid going through
1915        // `deref`, which creates an intermediate reference.
1916        self.buf.ptr()
1917    }
1918
1919    /// Returns a raw mutable pointer to the vector's buffer, or a dangling
1920    /// raw pointer valid for zero sized reads if the vector didn't allocate.
1921    ///
1922    /// The caller must ensure that the vector outlives the pointer this
1923    /// function returns, or else it will end up dangling.
1924    /// Modifying the vector may cause its buffer to be reallocated,
1925    /// which would also make any pointers to it invalid.
1926    ///
1927    /// This method guarantees that for the purpose of the aliasing model, this method
1928    /// does not materialize a reference to the underlying slice, and thus the returned pointer
1929    /// will remain valid when mixed with other calls to [`as_ptr`], [`as_mut_ptr`],
1930    /// and [`as_non_null`].
1931    /// Note that calling other methods that materialize references to the slice,
1932    /// or references to specific elements you are planning on accessing through this pointer,
1933    /// may still invalidate this pointer.
1934    /// See the second example below for how this guarantee can be used.
1935    ///
1936    /// The method also guarantees that, as long as `T` is not zero-sized and the capacity is
1937    /// nonzero, the pointer may be passed into [`dealloc`] with a layout of
1938    /// `Layout::array::<T>(capacity)` in order to deallocate the backing memory. If this is done,
1939    /// be careful not to run the destructor of the `Vec`, as dropping it will result in
1940    /// double-frees. Wrapping the `Vec` in a [`ManuallyDrop`] is the typical way to achieve this.
1941    ///
1942    /// # Examples
1943    ///
1944    /// ```
1945    /// // Allocate vector big enough for 4 elements.
1946    /// let size = 4;
1947    /// let mut x: Vec<i32> = Vec::with_capacity(size);
1948    /// let x_ptr = x.as_mut_ptr();
1949    ///
1950    /// // Initialize elements via raw pointer writes, then set length.
1951    /// unsafe {
1952    ///     for i in 0..size {
1953    ///         *x_ptr.add(i) = i as i32;
1954    ///     }
1955    ///     x.set_len(size);
1956    /// }
1957    /// assert_eq!(&*x, &[0, 1, 2, 3]);
1958    /// ```
1959    ///
1960    /// Due to the aliasing guarantee, the following code is legal:
1961    ///
1962    /// ```rust
1963    /// unsafe {
1964    ///     let mut v = vec![0];
1965    ///     let ptr1 = v.as_mut_ptr();
1966    ///     ptr1.write(1);
1967    ///     let ptr2 = v.as_mut_ptr();
1968    ///     ptr2.write(2);
1969    ///     // Notably, the write to `ptr2` did *not* invalidate `ptr1`:
1970    ///     ptr1.write(3);
1971    /// }
1972    /// ```
1973    ///
1974    /// Deallocating a vector using [`Box`] (which uses [`dealloc`] internally):
1975    ///
1976    /// ```
1977    /// use std::mem::{ManuallyDrop, MaybeUninit};
1978    ///
1979    /// let mut v = ManuallyDrop::new(vec![0, 1, 2]);
1980    /// let ptr = v.as_mut_ptr();
1981    /// let capacity = v.capacity();
1982    /// let slice_ptr: *mut [MaybeUninit<i32>] =
1983    ///     std::ptr::slice_from_raw_parts_mut(ptr.cast(), capacity);
1984    /// drop(unsafe { Box::from_raw(slice_ptr) });
1985    /// ```
1986    ///
1987    /// [`as_mut_ptr`]: Vec::as_mut_ptr
1988    /// [`as_ptr`]: Vec::as_ptr
1989    /// [`as_non_null`]: Vec::as_non_null
1990    /// [`dealloc`]: crate::alloc::GlobalAlloc::dealloc
1991    /// [`ManuallyDrop`]: core::mem::ManuallyDrop
1992    #[stable(feature = "vec_as_ptr", since = "1.37.0")]
1993    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1994    #[rustc_never_returns_null_ptr]
1995    #[rustc_as_ptr]
1996    #[inline]
1997    pub const fn as_mut_ptr(&mut self) -> *mut T {
1998        // We shadow the slice method of the same name to avoid going through
1999        // `deref_mut`, which creates an intermediate reference.
2000        self.buf.ptr()
2001    }
2002
2003    /// Returns a `NonNull` pointer to the vector's buffer, or a dangling
2004    /// `NonNull` pointer valid for zero sized reads if the vector didn't allocate.
2005    ///
2006    /// The caller must ensure that the vector outlives the pointer this
2007    /// function returns, or else it will end up dangling.
2008    /// Modifying the vector may cause its buffer to be reallocated,
2009    /// which would also make any pointers to it invalid.
2010    ///
2011    /// This method guarantees that for the purpose of the aliasing model, this method
2012    /// does not materialize a reference to the underlying slice, and thus the returned pointer
2013    /// will remain valid when mixed with other calls to [`as_ptr`], [`as_mut_ptr`],
2014    /// and [`as_non_null`].
2015    /// Note that calling other methods that materialize references to the slice,
2016    /// or references to specific elements you are planning on accessing through this pointer,
2017    /// may still invalidate this pointer.
2018    /// See the second example below for how this guarantee can be used.
2019    ///
2020    /// # Examples
2021    ///
2022    /// ```
2023    /// #![feature(box_vec_non_null)]
2024    ///
2025    /// // Allocate vector big enough for 4 elements.
2026    /// let size = 4;
2027    /// let mut x: Vec<i32> = Vec::with_capacity(size);
2028    /// let x_ptr = x.as_non_null();
2029    ///
2030    /// // Initialize elements via raw pointer writes, then set length.
2031    /// unsafe {
2032    ///     for i in 0..size {
2033    ///         x_ptr.add(i).write(i as i32);
2034    ///     }
2035    ///     x.set_len(size);
2036    /// }
2037    /// assert_eq!(&*x, &[0, 1, 2, 3]);
2038    /// ```
2039    ///
2040    /// Due to the aliasing guarantee, the following code is legal:
2041    ///
2042    /// ```rust
2043    /// #![feature(box_vec_non_null)]
2044    ///
2045    /// unsafe {
2046    ///     let mut v = vec![0];
2047    ///     let ptr1 = v.as_non_null();
2048    ///     ptr1.write(1);
2049    ///     let ptr2 = v.as_non_null();
2050    ///     ptr2.write(2);
2051    ///     // Notably, the write to `ptr2` did *not* invalidate `ptr1`:
2052    ///     ptr1.write(3);
2053    /// }
2054    /// ```
2055    ///
2056    /// [`as_mut_ptr`]: Vec::as_mut_ptr
2057    /// [`as_ptr`]: Vec::as_ptr
2058    /// [`as_non_null`]: Vec::as_non_null
2059    #[unstable(feature = "box_vec_non_null", issue = "130364")]
2060    #[rustc_const_unstable(feature = "box_vec_non_null", issue = "130364")]
2061    #[inline]
2062    pub const fn as_non_null(&mut self) -> NonNull<T> {
2063        self.buf.non_null()
2064    }
2065
2066    /// Returns a reference to the underlying allocator.
2067    #[unstable(feature = "allocator_api", issue = "32838")]
2068    #[inline]
2069    pub fn allocator(&self) -> &A {
2070        self.buf.allocator()
2071    }
2072
2073    /// Forces the length of the vector to `new_len`.
2074    ///
2075    /// This is a low-level operation that maintains none of the normal
2076    /// invariants of the type. Normally changing the length of a vector
2077    /// is done using one of the safe operations instead, such as
2078    /// [`truncate`], [`resize`], [`extend`], or [`clear`].
2079    ///
2080    /// [`truncate`]: Vec::truncate
2081    /// [`resize`]: Vec::resize
2082    /// [`extend`]: Extend::extend
2083    /// [`clear`]: Vec::clear
2084    ///
2085    /// # Safety
2086    ///
2087    /// - `new_len` must be less than or equal to [`capacity()`].
2088    /// - The elements at `old_len..new_len` must be initialized.
2089    ///
2090    /// [`capacity()`]: Vec::capacity
2091    ///
2092    /// # Examples
2093    ///
2094    /// See [`spare_capacity_mut()`] for an example with safe
2095    /// initialization of capacity elements and use of this method.
2096    ///
2097    /// `set_len()` can be useful for situations in which the vector
2098    /// is serving as a buffer for other code, particularly over FFI:
2099    ///
2100    /// ```no_run
2101    /// # #![allow(dead_code)]
2102    /// # // This is just a minimal skeleton for the doc example;
2103    /// # // don't use this as a starting point for a real library.
2104    /// # pub struct StreamWrapper { strm: *mut std::ffi::c_void }
2105    /// # const Z_OK: i32 = 0;
2106    /// # unsafe extern "C" {
2107    /// #     fn deflateGetDictionary(
2108    /// #         strm: *mut std::ffi::c_void,
2109    /// #         dictionary: *mut u8,
2110    /// #         dictLength: *mut usize,
2111    /// #     ) -> i32;
2112    /// # }
2113    /// # impl StreamWrapper {
2114    /// pub fn get_dictionary(&self) -> Option<Vec<u8>> {
2115    ///     // Per the FFI method's docs, "32768 bytes is always enough".
2116    ///     let mut dict = Vec::with_capacity(32_768);
2117    ///     let mut dict_length = 0;
2118    ///     // SAFETY: When `deflateGetDictionary` returns `Z_OK`, it holds that:
2119    ///     // 1. `dict_length` elements were initialized.
2120    ///     // 2. `dict_length` <= the capacity (32_768)
2121    ///     // which makes `set_len` safe to call.
2122    ///     unsafe {
2123    ///         // Make the FFI call...
2124    ///         let r = deflateGetDictionary(self.strm, dict.as_mut_ptr(), &mut dict_length);
2125    ///         if r == Z_OK {
2126    ///             // ...and update the length to what was initialized.
2127    ///             dict.set_len(dict_length);
2128    ///             Some(dict)
2129    ///         } else {
2130    ///             None
2131    ///         }
2132    ///     }
2133    /// }
2134    /// # }
2135    /// ```
2136    ///
2137    /// While the following example is sound, there is a memory leak since
2138    /// the inner vectors were not freed prior to the `set_len` call:
2139    ///
2140    /// ```
2141    /// let mut vec = vec![vec![1, 0, 0],
2142    ///                    vec![0, 1, 0],
2143    ///                    vec![0, 0, 1]];
2144    /// // SAFETY:
2145    /// // 1. `old_len..0` is empty so no elements need to be initialized.
2146    /// // 2. `0 <= capacity` always holds whatever `capacity` is.
2147    /// unsafe {
2148    ///     vec.set_len(0);
2149    /// #   // FIXME(https://github.com/rust-lang/miri/issues/3670):
2150    /// #   // use -Zmiri-disable-leak-check instead of unleaking in tests meant to leak.
2151    /// #   vec.set_len(3);
2152    /// }
2153    /// ```
2154    ///
2155    /// Normally, here, one would use [`clear`] instead to correctly drop
2156    /// the contents and thus not leak memory.
2157    ///
2158    /// [`spare_capacity_mut()`]: Vec::spare_capacity_mut
2159    #[inline]
2160    #[stable(feature = "rust1", since = "1.0.0")]
2161    pub unsafe fn set_len(&mut self, new_len: usize) {
2162        ub_checks::assert_unsafe_precondition!(
2163            check_library_ub,
2164            "Vec::set_len requires that new_len <= capacity()",
2165            (new_len: usize = new_len, capacity: usize = self.capacity()) => new_len <= capacity
2166        );
2167
2168        self.len = new_len;
2169    }
2170
2171    /// Removes an element from the vector and returns it.
2172    ///
2173    /// The removed element is replaced by the last element of the vector.
2174    ///
2175    /// This does not preserve ordering of the remaining elements, but is *O*(1).
2176    /// If you need to preserve the element order, use [`remove`] instead.
2177    ///
2178    /// [`remove`]: Vec::remove
2179    ///
2180    /// # Panics
2181    ///
2182    /// Panics if `index` is out of bounds.
2183    ///
2184    /// # Examples
2185    ///
2186    /// ```
2187    /// let mut v = vec!["foo", "bar", "baz", "qux"];
2188    ///
2189    /// assert_eq!(v.swap_remove(1), "bar");
2190    /// assert_eq!(v, ["foo", "qux", "baz"]);
2191    ///
2192    /// assert_eq!(v.swap_remove(0), "foo");
2193    /// assert_eq!(v, ["baz", "qux"]);
2194    /// ```
2195    #[inline]
2196    #[stable(feature = "rust1", since = "1.0.0")]
2197    pub fn swap_remove(&mut self, index: usize) -> T {
2198        #[cold]
2199        #[cfg_attr(not(panic = "immediate-abort"), inline(never))]
2200        #[optimize(size)]
2201        fn assert_failed(index: usize, len: usize) -> ! {
2202            panic!("swap_remove index (is {index}) should be < len (is {len})");
2203        }
2204
2205        let len = self.len();
2206        if index >= len {
2207            assert_failed(index, len);
2208        }
2209        unsafe {
2210            // We replace self[index] with the last element. Note that if the
2211            // bounds check above succeeds there must be a last element (which
2212            // can be self[index] itself).
2213            let value = ptr::read(self.as_ptr().add(index));
2214            let base_ptr = self.as_mut_ptr();
2215            ptr::copy(base_ptr.add(len - 1), base_ptr.add(index), 1);
2216            self.set_len(len - 1);
2217            value
2218        }
2219    }
2220
2221    /// Inserts an element at position `index` within the vector, shifting all
2222    /// elements after it to the right.
2223    ///
2224    /// # Panics
2225    ///
2226    /// Panics if `index > len`.
2227    ///
2228    /// # Examples
2229    ///
2230    /// ```
2231    /// let mut vec = vec!['a', 'b', 'c'];
2232    /// vec.insert(1, 'd');
2233    /// assert_eq!(vec, ['a', 'd', 'b', 'c']);
2234    /// vec.insert(4, 'e');
2235    /// assert_eq!(vec, ['a', 'd', 'b', 'c', 'e']);
2236    /// ```
2237    ///
2238    /// # Time complexity
2239    ///
2240    /// Takes *O*([`Vec::len`]) time. All items after the insertion index must be
2241    /// shifted to the right. In the worst case, all elements are shifted when
2242    /// the insertion index is 0.
2243    #[cfg(not(no_global_oom_handling))]
2244    #[stable(feature = "rust1", since = "1.0.0")]
2245    #[track_caller]
2246    pub fn insert(&mut self, index: usize, element: T) {
2247        let _ = self.insert_mut(index, element);
2248    }
2249
2250    /// Inserts an element at position `index` within the vector, shifting all
2251    /// elements after it to the right, and returning a reference to the new
2252    /// element.
2253    ///
2254    /// # Panics
2255    ///
2256    /// Panics if `index > len`.
2257    ///
2258    /// # Examples
2259    ///
2260    /// ```
2261    /// let mut vec = vec![1, 3, 5, 9];
2262    /// let x = vec.insert_mut(3, 6);
2263    /// *x += 1;
2264    /// assert_eq!(vec, [1, 3, 5, 7, 9]);
2265    /// ```
2266    ///
2267    /// # Time complexity
2268    ///
2269    /// Takes *O*([`Vec::len`]) time. All items after the insertion index must be
2270    /// shifted to the right. In the worst case, all elements are shifted when
2271    /// the insertion index is 0.
2272    #[cfg(not(no_global_oom_handling))]
2273    #[inline]
2274    #[stable(feature = "push_mut", since = "1.95.0")]
2275    #[track_caller]
2276    #[must_use = "if you don't need a reference to the value, use `Vec::insert` instead"]
2277    pub fn insert_mut(&mut self, index: usize, element: T) -> &mut T {
2278        #[cold]
2279        #[cfg_attr(not(panic = "immediate-abort"), inline(never))]
2280        #[track_caller]
2281        #[optimize(size)]
2282        fn assert_failed(index: usize, len: usize) -> ! {
2283            panic!("insertion index (is {index}) should be <= len (is {len})");
2284        }
2285
2286        let len = self.len();
2287        if index > len {
2288            assert_failed(index, len);
2289        }
2290
2291        // space for the new element
2292        if len == self.buf.capacity() {
2293            self.buf.grow_one();
2294        }
2295
2296        unsafe {
2297            // infallible
2298            // The spot to put the new value
2299            let p = self.as_mut_ptr().add(index);
2300            {
2301                if index < len {
2302                    // Shift everything over to make space. (Duplicating the
2303                    // `index`th element into two consecutive places.)
2304                    ptr::copy(p, p.add(1), len - index);
2305                }
2306                // Write it in, overwriting the first copy of the `index`th
2307                // element.
2308                ptr::write(p, element);
2309            }
2310            self.set_len(len + 1);
2311            &mut *p
2312        }
2313    }
2314
2315    /// Removes and returns the element at position `index` within the vector,
2316    /// shifting all elements after it to the left.
2317    ///
2318    /// Note: Because this shifts over the remaining elements, it has a
2319    /// worst-case performance of *O*(*n*). If you don't need the order of elements
2320    /// to be preserved, use [`swap_remove`] instead. If you'd like to remove
2321    /// elements from the beginning of the `Vec`, consider using
2322    /// [`VecDeque::pop_front`] instead.
2323    ///
2324    /// [`swap_remove`]: Vec::swap_remove
2325    /// [`VecDeque::pop_front`]: crate::collections::VecDeque::pop_front
2326    ///
2327    /// # Panics
2328    ///
2329    /// Panics if `index` is out of bounds.
2330    ///
2331    /// # Examples
2332    ///
2333    /// ```
2334    /// let mut v = vec!['a', 'b', 'c'];
2335    /// assert_eq!(v.remove(1), 'b');
2336    /// assert_eq!(v, ['a', 'c']);
2337    /// ```
2338    #[stable(feature = "rust1", since = "1.0.0")]
2339    #[track_caller]
2340    #[rustc_confusables("delete", "take")]
2341    pub fn remove(&mut self, index: usize) -> T {
2342        #[cold]
2343        #[cfg_attr(not(panic = "immediate-abort"), inline(never))]
2344        #[track_caller]
2345        #[optimize(size)]
2346        fn assert_failed(index: usize, len: usize) -> ! {
2347            panic!("removal index (is {index}) should be < len (is {len})");
2348        }
2349
2350        match self.try_remove(index) {
2351            Some(elem) => elem,
2352            None => assert_failed(index, self.len()),
2353        }
2354    }
2355
2356    /// Remove and return the element at position `index` within the vector,
2357    /// shifting all elements after it to the left, or [`None`] if it does not
2358    /// exist.
2359    ///
2360    /// Note: Because this shifts over the remaining elements, it has a
2361    /// worst-case performance of *O*(*n*). If you'd like to remove
2362    /// elements from the beginning of the `Vec`, consider using
2363    /// [`VecDeque::pop_front`] instead.
2364    ///
2365    /// [`VecDeque::pop_front`]: crate::collections::VecDeque::pop_front
2366    ///
2367    /// # Examples
2368    ///
2369    /// ```
2370    /// #![feature(vec_try_remove)]
2371    /// let mut v = vec![1, 2, 3];
2372    /// assert_eq!(v.try_remove(0), Some(1));
2373    /// assert_eq!(v.try_remove(2), None);
2374    /// ```
2375    #[unstable(feature = "vec_try_remove", issue = "146954")]
2376    #[rustc_confusables("delete", "take", "remove")]
2377    pub fn try_remove(&mut self, index: usize) -> Option<T> {
2378        let len = self.len();
2379        if index >= len {
2380            return None;
2381        }
2382        unsafe {
2383            // infallible
2384            let ret;
2385            {
2386                // the place we are taking from.
2387                let ptr = self.as_mut_ptr().add(index);
2388                // copy it out, unsafely having a copy of the value on
2389                // the stack and in the vector at the same time.
2390                ret = ptr::read(ptr);
2391
2392                // Shift everything down to fill in that spot.
2393                ptr::copy(ptr.add(1), ptr, len - index - 1);
2394            }
2395            self.set_len(len - 1);
2396            Some(ret)
2397        }
2398    }
2399
2400    /// Retains only the elements specified by the predicate.
2401    ///
2402    /// In other words, remove all elements `e` for which `f(&e)` returns `false`.
2403    /// This method operates in place, visiting each element exactly once in the
2404    /// original order, and preserves the order of the retained elements.
2405    ///
2406    /// # Examples
2407    ///
2408    /// ```
2409    /// let mut vec = vec![1, 2, 3, 4];
2410    /// vec.retain(|&x| x % 2 == 0);
2411    /// assert_eq!(vec, [2, 4]);
2412    /// ```
2413    ///
2414    /// Because the elements are visited exactly once in the original order,
2415    /// external state may be used to decide which elements to keep.
2416    ///
2417    /// ```
2418    /// let mut vec = vec![1, 2, 3, 4, 5];
2419    /// let keep = [false, true, true, false, true];
2420    /// let mut iter = keep.iter();
2421    /// vec.retain(|_| *iter.next().unwrap());
2422    /// assert_eq!(vec, [2, 3, 5]);
2423    /// ```
2424    #[stable(feature = "rust1", since = "1.0.0")]
2425    pub fn retain<F>(&mut self, mut f: F)
2426    where
2427        F: FnMut(&T) -> bool,
2428    {
2429        self.retain_mut(|elem| f(elem));
2430    }
2431
2432    /// Retains only the elements specified by the predicate, passing a mutable reference to it.
2433    ///
2434    /// In other words, remove all elements `e` such that `f(&mut e)` returns `false`.
2435    /// This method operates in place, visiting each element exactly once in the
2436    /// original order, and preserves the order of the retained elements.
2437    ///
2438    /// # Examples
2439    ///
2440    /// ```
2441    /// let mut vec = vec![1, 2, 3, 4];
2442    /// vec.retain_mut(|x| if *x <= 3 {
2443    ///     *x += 1;
2444    ///     true
2445    /// } else {
2446    ///     false
2447    /// });
2448    /// assert_eq!(vec, [2, 3, 4]);
2449    /// ```
2450    #[stable(feature = "vec_retain_mut", since = "1.61.0")]
2451    pub fn retain_mut<F>(&mut self, mut f: F)
2452    where
2453        F: FnMut(&mut T) -> bool,
2454    {
2455        let original_len = self.len();
2456
2457        if original_len == 0 {
2458            // Empty case: explicit return allows better optimization, vs letting compiler infer it
2459            return;
2460        }
2461
2462        // Vec: [Kept, Kept, Hole, Hole, Hole, Hole, Unchecked, Unchecked]
2463        //      |            ^- write                ^- read             |
2464        //      |<-              original_len                          ->|
2465        // Kept: Elements which predicate returns true on.
2466        // Hole: Moved or dropped element slot.
2467        // Unchecked: Unchecked valid elements.
2468        //
2469        // This drop guard will be invoked when predicate or `drop` of element panicked.
2470        // It shifts unchecked elements to cover holes and `set_len` to the correct length.
2471        // In cases when predicate and `drop` never panick, it will be optimized out.
2472        struct PanicGuard<'a, T, A: Allocator> {
2473            v: &'a mut Vec<T, A>,
2474            read: usize,
2475            write: usize,
2476            original_len: usize,
2477        }
2478
2479        impl<T, A: Allocator> Drop for PanicGuard<'_, T, A> {
2480            #[cold]
2481            fn drop(&mut self) {
2482                let remaining = self.original_len - self.read;
2483                // SAFETY: Trailing unchecked items must be valid since we never touch them.
2484                unsafe {
2485                    ptr::copy(
2486                        self.v.as_ptr().add(self.read),
2487                        self.v.as_mut_ptr().add(self.write),
2488                        remaining,
2489                    );
2490                }
2491                // SAFETY: After filling holes, all items are in contiguous memory.
2492                unsafe {
2493                    self.v.set_len(self.write + remaining);
2494                }
2495            }
2496        }
2497
2498        let mut read = 0;
2499        loop {
2500            // SAFETY: read < original_len
2501            let cur = unsafe { self.get_unchecked_mut(read) };
2502            if hint::unlikely(!f(cur)) {
2503                break;
2504            }
2505            read += 1;
2506            if read == original_len {
2507                // All elements are kept, return early.
2508                return;
2509            }
2510        }
2511
2512        // Critical section starts here and at least one element is going to be removed.
2513        // Advance `g.read` early to avoid double drop if `drop_in_place` panicked.
2514        let mut g = PanicGuard { v: self, read: read + 1, write: read, original_len };
2515        // SAFETY: previous `read` is always less than original_len.
2516        unsafe { ptr::drop_in_place(&mut *g.v.as_mut_ptr().add(read)) };
2517
2518        while g.read < g.original_len {
2519            // SAFETY: `read` is always less than original_len.
2520            let cur = unsafe { &mut *g.v.as_mut_ptr().add(g.read) };
2521            if !f(cur) {
2522                // Advance `read` early to avoid double drop if `drop_in_place` panicked.
2523                g.read += 1;
2524                // SAFETY: We never touch this element again after dropped.
2525                unsafe { ptr::drop_in_place(cur) };
2526            } else {
2527                // SAFETY: `read` > `write`, so the slots don't overlap.
2528                // We use copy for move, and never touch the source element again.
2529                unsafe {
2530                    let hole = g.v.as_mut_ptr().add(g.write);
2531                    ptr::copy_nonoverlapping(cur, hole, 1);
2532                }
2533                g.write += 1;
2534                g.read += 1;
2535            }
2536        }
2537
2538        // We are leaving the critical section and no panic happened,
2539        // Commit the length change and forget the guard.
2540        // SAFETY: `write` is always less than or equal to original_len.
2541        unsafe { g.v.set_len(g.write) };
2542        mem::forget(g);
2543    }
2544
2545    /// Removes all but the first of consecutive elements in the vector that resolve to the same
2546    /// key.
2547    ///
2548    /// If the vector is sorted, this removes all duplicates.
2549    ///
2550    /// # Examples
2551    ///
2552    /// ```
2553    /// let mut vec = vec![10, 20, 21, 30, 20];
2554    ///
2555    /// vec.dedup_by_key(|i| *i / 10);
2556    ///
2557    /// assert_eq!(vec, [10, 20, 30, 20]);
2558    /// ```
2559    #[stable(feature = "dedup_by", since = "1.16.0")]
2560    #[inline]
2561    pub fn dedup_by_key<F, K>(&mut self, mut key: F)
2562    where
2563        F: FnMut(&mut T) -> K,
2564        K: PartialEq,
2565    {
2566        self.dedup_by(|a, b| key(a) == key(b))
2567    }
2568
2569    /// Removes all but the first of consecutive elements in the vector satisfying a given equality
2570    /// relation.
2571    ///
2572    /// The `same_bucket` function is passed references to two elements from the vector and
2573    /// must determine if the elements compare equal. The elements are passed in opposite order
2574    /// from their order in the slice, so if `same_bucket(a, b)` returns `true`, `a` is removed.
2575    ///
2576    /// If the vector is sorted, this removes all duplicates.
2577    ///
2578    /// # Examples
2579    ///
2580    /// ```
2581    /// let mut vec = vec!["foo", "bar", "Bar", "baz", "bar"];
2582    ///
2583    /// vec.dedup_by(|a, b| a.eq_ignore_ascii_case(b));
2584    ///
2585    /// assert_eq!(vec, ["foo", "bar", "baz", "bar"]);
2586    /// ```
2587    #[stable(feature = "dedup_by", since = "1.16.0")]
2588    pub fn dedup_by<F>(&mut self, mut same_bucket: F)
2589    where
2590        F: FnMut(&mut T, &mut T) -> bool,
2591    {
2592        let len = self.len();
2593        if len <= 1 {
2594            return;
2595        }
2596
2597        // Check if we ever want to remove anything.
2598        // This allows to use copy_non_overlapping in next cycle.
2599        // And avoids any memory writes if we don't need to remove anything.
2600        let mut first_duplicate_idx: usize = 1;
2601        let start = self.as_mut_ptr();
2602        while first_duplicate_idx != len {
2603            let found_duplicate = unsafe {
2604                // SAFETY: first_duplicate always in range [1..len)
2605                // Note that we start iteration from 1 so we never overflow.
2606                let prev = start.add(first_duplicate_idx.wrapping_sub(1));
2607                let current = start.add(first_duplicate_idx);
2608                // We explicitly say in docs that references are reversed.
2609                same_bucket(&mut *current, &mut *prev)
2610            };
2611            if found_duplicate {
2612                break;
2613            }
2614            first_duplicate_idx += 1;
2615        }
2616        // Don't need to remove anything.
2617        // We cannot get bigger than len.
2618        if first_duplicate_idx == len {
2619            return;
2620        }
2621
2622        /* INVARIANT: vec.len() > read > write > write-1 >= 0 */
2623        struct FillGapOnDrop<'a, T, A: core::alloc::Allocator> {
2624            /* Offset of the element we want to check if it is duplicate */
2625            read: usize,
2626
2627            /* Offset of the place where we want to place the non-duplicate
2628             * when we find it. */
2629            write: usize,
2630
2631            /* The Vec that would need correction if `same_bucket` panicked */
2632            vec: &'a mut Vec<T, A>,
2633        }
2634
2635        impl<'a, T, A: core::alloc::Allocator> Drop for FillGapOnDrop<'a, T, A> {
2636            fn drop(&mut self) {
2637                /* This code gets executed when `same_bucket` panics */
2638
2639                /* SAFETY: invariant guarantees that `read - write`
2640                 * and `len - read` never overflow and that the copy is always
2641                 * in-bounds. */
2642                unsafe {
2643                    let ptr = self.vec.as_mut_ptr();
2644                    let len = self.vec.len();
2645
2646                    /* How many items were left when `same_bucket` panicked.
2647                     * Basically vec[read..].len() */
2648                    let items_left = len.wrapping_sub(self.read);
2649
2650                    /* Pointer to first item in vec[write..write+items_left] slice */
2651                    let dropped_ptr = ptr.add(self.write);
2652                    /* Pointer to first item in vec[read..] slice */
2653                    let valid_ptr = ptr.add(self.read);
2654
2655                    /* Copy `vec[read..]` to `vec[write..write+items_left]`.
2656                     * The slices can overlap, so `copy_nonoverlapping` cannot be used */
2657                    ptr::copy(valid_ptr, dropped_ptr, items_left);
2658
2659                    /* How many items have been already dropped
2660                     * Basically vec[read..write].len() */
2661                    let dropped = self.read.wrapping_sub(self.write);
2662
2663                    self.vec.set_len(len - dropped);
2664                }
2665            }
2666        }
2667
2668        /* Drop items while going through Vec, it should be more efficient than
2669         * doing slice partition_dedup + truncate */
2670
2671        // Construct gap first and then drop item to avoid memory corruption if `T::drop` panics.
2672        let mut gap =
2673            FillGapOnDrop { read: first_duplicate_idx + 1, write: first_duplicate_idx, vec: self };
2674        unsafe {
2675            // SAFETY: we checked that first_duplicate_idx in bounds before.
2676            // If drop panics, `gap` would remove this item without drop.
2677            ptr::drop_in_place(start.add(first_duplicate_idx));
2678        }
2679
2680        /* SAFETY: Because of the invariant, read_ptr, prev_ptr and write_ptr
2681         * are always in-bounds and read_ptr never aliases prev_ptr */
2682        unsafe {
2683            while gap.read < len {
2684                let read_ptr = start.add(gap.read);
2685                let prev_ptr = start.add(gap.write.wrapping_sub(1));
2686
2687                // We explicitly say in docs that references are reversed.
2688                let found_duplicate = same_bucket(&mut *read_ptr, &mut *prev_ptr);
2689                if found_duplicate {
2690                    // Increase `gap.read` now since the drop may panic.
2691                    gap.read += 1;
2692                    /* We have found duplicate, drop it in-place */
2693                    ptr::drop_in_place(read_ptr);
2694                } else {
2695                    let write_ptr = start.add(gap.write);
2696
2697                    /* read_ptr cannot be equal to write_ptr because at this point
2698                     * we guaranteed to skip at least one element (before loop starts).
2699                     */
2700                    ptr::copy_nonoverlapping(read_ptr, write_ptr, 1);
2701
2702                    /* We have filled that place, so go further */
2703                    gap.write += 1;
2704                    gap.read += 1;
2705                }
2706            }
2707
2708            /* Technically we could let `gap` clean up with its Drop, but
2709             * when `same_bucket` is guaranteed to not panic, this bloats a little
2710             * the codegen, so we just do it manually */
2711            gap.vec.set_len(gap.write);
2712            mem::forget(gap);
2713        }
2714    }
2715
2716    /// Appends an element and returns a reference to it if there is sufficient spare capacity,
2717    /// otherwise an error is returned with the element.
2718    ///
2719    /// Unlike [`push`] this method will not reallocate when there's insufficient capacity.
2720    /// The caller should use [`reserve`] or [`try_reserve`] to ensure that there is enough capacity.
2721    ///
2722    /// [`push`]: Vec::push
2723    /// [`reserve`]: Vec::reserve
2724    /// [`try_reserve`]: Vec::try_reserve
2725    ///
2726    /// # Examples
2727    ///
2728    /// A manual, panic-free alternative to [`FromIterator`]:
2729    ///
2730    /// ```
2731    /// #![feature(vec_push_within_capacity)]
2732    ///
2733    /// use std::collections::TryReserveError;
2734    /// fn from_iter_fallible<T>(iter: impl Iterator<Item=T>) -> Result<Vec<T>, TryReserveError> {
2735    ///     let mut vec = Vec::new();
2736    ///     for value in iter {
2737    ///         if let Err(value) = vec.push_within_capacity(value) {
2738    ///             vec.try_reserve(1)?;
2739    ///             // this cannot fail, the previous line either returned or added at least 1 free slot
2740    ///             let _ = vec.push_within_capacity(value);
2741    ///         }
2742    ///     }
2743    ///     Ok(vec)
2744    /// }
2745    /// assert_eq!(from_iter_fallible(0..100), Ok(Vec::from_iter(0..100)));
2746    /// ```
2747    ///
2748    /// # Time complexity
2749    ///
2750    /// Takes *O*(1) time.
2751    #[inline]
2752    #[unstable(feature = "vec_push_within_capacity", issue = "100486")]
2753    pub fn push_within_capacity(&mut self, value: T) -> Result<&mut T, T> {
2754        if self.len == self.buf.capacity() {
2755            return Err(value);
2756        }
2757
2758        unsafe {
2759            let end = self.as_mut_ptr().add(self.len);
2760            ptr::write(end, value);
2761            self.len += 1;
2762
2763            // SAFETY: We just wrote a value to the pointer that will live the lifetime of the reference.
2764            Ok(&mut *end)
2765        }
2766    }
2767
2768    /// Removes the last element from a vector and returns it, or [`None`] if it
2769    /// is empty.
2770    ///
2771    /// If you'd like to pop the first element, consider using
2772    /// [`VecDeque::pop_front`] instead.
2773    ///
2774    /// [`VecDeque::pop_front`]: crate::collections::VecDeque::pop_front
2775    ///
2776    /// # Examples
2777    ///
2778    /// ```
2779    /// let mut vec = vec![1, 2, 3];
2780    /// assert_eq!(vec.pop(), Some(3));
2781    /// assert_eq!(vec, [1, 2]);
2782    /// ```
2783    ///
2784    /// # Time complexity
2785    ///
2786    /// Takes *O*(1) time.
2787    #[inline]
2788    #[stable(feature = "rust1", since = "1.0.0")]
2789    #[rustc_diagnostic_item = "vec_pop"]
2790    pub fn pop(&mut self) -> Option<T> {
2791        if self.len == 0 {
2792            None
2793        } else {
2794            unsafe {
2795                self.len -= 1;
2796                core::hint::assert_unchecked(self.len < self.capacity());
2797                Some(ptr::read(self.as_ptr().add(self.len())))
2798            }
2799        }
2800    }
2801
2802    /// Removes and returns the last element from a vector if the predicate
2803    /// returns `true`, or [`None`] if the predicate returns false or the vector
2804    /// is empty (the predicate will not be called in that case).
2805    ///
2806    /// # Examples
2807    ///
2808    /// ```
2809    /// let mut vec = vec![1, 2, 3, 4];
2810    /// let pred = |x: &mut i32| *x % 2 == 0;
2811    ///
2812    /// assert_eq!(vec.pop_if(pred), Some(4));
2813    /// assert_eq!(vec, [1, 2, 3]);
2814    /// assert_eq!(vec.pop_if(pred), None);
2815    /// ```
2816    #[stable(feature = "vec_pop_if", since = "1.86.0")]
2817    pub fn pop_if(&mut self, predicate: impl FnOnce(&mut T) -> bool) -> Option<T> {
2818        let last = self.last_mut()?;
2819        if predicate(last) { self.pop() } else { None }
2820    }
2821
2822    /// Returns a mutable reference to the last item in the vector, or
2823    /// `None` if it is empty.
2824    ///
2825    /// # Examples
2826    ///
2827    /// Basic usage:
2828    ///
2829    /// ```
2830    /// #![feature(vec_peek_mut)]
2831    /// let mut vec = Vec::new();
2832    /// assert!(vec.peek_mut().is_none());
2833    ///
2834    /// vec.push(1);
2835    /// vec.push(5);
2836    /// vec.push(2);
2837    /// assert_eq!(vec.last(), Some(&2));
2838    /// if let Some(mut val) = vec.peek_mut() {
2839    ///     *val = 0;
2840    /// }
2841    /// assert_eq!(vec.last(), Some(&0));
2842    /// ```
2843    #[inline]
2844    #[unstable(feature = "vec_peek_mut", issue = "122742")]
2845    pub fn peek_mut(&mut self) -> Option<PeekMut<'_, T, A>> {
2846        PeekMut::new(self)
2847    }
2848
2849    /// Moves all the elements of `other` into `self`, leaving `other` empty.
2850    ///
2851    /// # Panics
2852    ///
2853    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
2854    ///
2855    /// # Examples
2856    ///
2857    /// ```
2858    /// let mut vec = vec![1, 2, 3];
2859    /// let mut vec2 = vec![4, 5, 6];
2860    /// vec.append(&mut vec2);
2861    /// assert_eq!(vec, [1, 2, 3, 4, 5, 6]);
2862    /// assert_eq!(vec2, []);
2863    /// ```
2864    #[cfg(not(no_global_oom_handling))]
2865    #[inline]
2866    #[stable(feature = "append", since = "1.4.0")]
2867    pub fn append(&mut self, other: &mut Self) {
2868        unsafe {
2869            self.append_elements(other.as_slice() as _);
2870            other.set_len(0);
2871        }
2872    }
2873
2874    /// Appends elements to `self` from other buffer.
2875    #[cfg(not(no_global_oom_handling))]
2876    #[inline]
2877    unsafe fn append_elements(&mut self, other: *const [T]) {
2878        let count = other.len();
2879        self.reserve(count);
2880        let len = self.len();
2881        if count > 0 {
2882            unsafe {
2883                ptr::copy_nonoverlapping(other as *const T, self.as_mut_ptr().add(len), count)
2884            };
2885        }
2886        self.len += count;
2887    }
2888
2889    /// Removes the subslice indicated by the given range from the vector,
2890    /// returning a double-ended iterator over the removed subslice.
2891    ///
2892    /// If the iterator is dropped before being fully consumed,
2893    /// it drops the remaining removed elements.
2894    ///
2895    /// The returned iterator keeps a mutable borrow on the vector to optimize
2896    /// its implementation.
2897    ///
2898    /// # Panics
2899    ///
2900    /// Panics if the range has `start_bound > end_bound`, or, if the range is
2901    /// bounded on either end and past the length of the vector.
2902    ///
2903    /// # Leaking
2904    ///
2905    /// If the returned iterator goes out of scope without being dropped (due to
2906    /// [`mem::forget`], for example), the vector may have lost and leaked
2907    /// elements arbitrarily, including elements outside the range.
2908    ///
2909    /// # Examples
2910    ///
2911    /// ```
2912    /// let mut v = vec![1, 2, 3];
2913    /// let u: Vec<_> = v.drain(1..).collect();
2914    /// assert_eq!(v, &[1]);
2915    /// assert_eq!(u, &[2, 3]);
2916    ///
2917    /// // A full range clears the vector, like `clear()` does
2918    /// v.drain(..);
2919    /// assert_eq!(v, &[]);
2920    /// ```
2921    #[stable(feature = "drain", since = "1.6.0")]
2922    pub fn drain<R>(&mut self, range: R) -> Drain<'_, T, A>
2923    where
2924        R: RangeBounds<usize>,
2925    {
2926        // Memory safety
2927        //
2928        // When the Drain is first created, it shortens the length of
2929        // the source vector to make sure no uninitialized or moved-from elements
2930        // are accessible at all if the Drain's destructor never gets to run.
2931        //
2932        // Drain will ptr::read out the values to remove.
2933        // When finished, remaining tail of the vec is copied back to cover
2934        // the hole, and the vector length is restored to the new length.
2935        //
2936        let len = self.len();
2937        let Range { start, end } = slice::range(range, ..len);
2938
2939        unsafe {
2940            // set self.vec length's to start, to be safe in case Drain is leaked
2941            self.set_len(start);
2942            let range_slice = slice::from_raw_parts(self.as_ptr().add(start), end - start);
2943            Drain {
2944                tail_start: end,
2945                tail_len: len - end,
2946                iter: range_slice.iter(),
2947                vec: NonNull::from(self),
2948            }
2949        }
2950    }
2951
2952    /// Clears the vector, removing all values.
2953    ///
2954    /// Note that this method has no effect on the allocated capacity
2955    /// of the vector.
2956    ///
2957    /// # Examples
2958    ///
2959    /// ```
2960    /// let mut v = vec![1, 2, 3];
2961    ///
2962    /// v.clear();
2963    ///
2964    /// assert!(v.is_empty());
2965    /// ```
2966    #[inline]
2967    #[stable(feature = "rust1", since = "1.0.0")]
2968    pub fn clear(&mut self) {
2969        let elems: *mut [T] = self.as_mut_slice();
2970
2971        // SAFETY:
2972        // - `elems` comes directly from `as_mut_slice` and is therefore valid.
2973        // - Setting `self.len` before calling `drop_in_place` means that,
2974        //   if an element's `Drop` impl panics, the vector's `Drop` impl will
2975        //   do nothing (leaking the rest of the elements) instead of dropping
2976        //   some twice.
2977        unsafe {
2978            self.len = 0;
2979            ptr::drop_in_place(elems);
2980        }
2981    }
2982
2983    /// Returns the number of elements in the vector, also referred to
2984    /// as its 'length'.
2985    ///
2986    /// # Examples
2987    ///
2988    /// ```
2989    /// let a = vec![1, 2, 3];
2990    /// assert_eq!(a.len(), 3);
2991    /// ```
2992    #[inline]
2993    #[stable(feature = "rust1", since = "1.0.0")]
2994    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
2995    #[rustc_confusables("length", "size")]
2996    pub const fn len(&self) -> usize {
2997        let len = self.len;
2998
2999        // SAFETY: The maximum capacity of `Vec<T>` is `isize::MAX` bytes, so the maximum value can
3000        // be returned is `usize::checked_div(size_of::<T>()).unwrap_or(usize::MAX)`, which
3001        // matches the definition of `T::MAX_SLICE_LEN`.
3002        unsafe { intrinsics::assume(len <= T::MAX_SLICE_LEN) };
3003
3004        len
3005    }
3006
3007    /// Returns `true` if the vector contains no elements.
3008    ///
3009    /// # Examples
3010    ///
3011    /// ```
3012    /// let mut v = Vec::new();
3013    /// assert!(v.is_empty());
3014    ///
3015    /// v.push(1);
3016    /// assert!(!v.is_empty());
3017    /// ```
3018    #[stable(feature = "rust1", since = "1.0.0")]
3019    #[rustc_diagnostic_item = "vec_is_empty"]
3020    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
3021    pub const fn is_empty(&self) -> bool {
3022        self.len() == 0
3023    }
3024
3025    /// Splits the collection into two at the given index.
3026    ///
3027    /// Returns a newly allocated vector containing the elements in the range
3028    /// `[at, len)`. After the call, the original vector will be left containing
3029    /// the elements `[0, at)` with its previous capacity unchanged.
3030    ///
3031    /// - If you want to take ownership of the entire contents and capacity of
3032    ///   the vector, see [`mem::take`] or [`mem::replace`].
3033    /// - If you don't need the returned vector at all, see [`Vec::truncate`].
3034    /// - If you want to take ownership of an arbitrary subslice, or you don't
3035    ///   necessarily want to store the removed items in a vector, see [`Vec::drain`].
3036    ///
3037    /// # Panics
3038    ///
3039    /// Panics if `at > len`.
3040    ///
3041    /// # Examples
3042    ///
3043    /// ```
3044    /// let mut vec = vec!['a', 'b', 'c'];
3045    /// let vec2 = vec.split_off(1);
3046    /// assert_eq!(vec, ['a']);
3047    /// assert_eq!(vec2, ['b', 'c']);
3048    /// ```
3049    #[cfg(not(no_global_oom_handling))]
3050    #[inline]
3051    #[must_use = "use `.truncate()` if you don't need the other half"]
3052    #[stable(feature = "split_off", since = "1.4.0")]
3053    #[track_caller]
3054    pub fn split_off(&mut self, at: usize) -> Self
3055    where
3056        A: Clone,
3057    {
3058        #[cold]
3059        #[cfg_attr(not(panic = "immediate-abort"), inline(never))]
3060        #[track_caller]
3061        #[optimize(size)]
3062        fn assert_failed(at: usize, len: usize) -> ! {
3063            panic!("`at` split index (is {at}) should be <= len (is {len})");
3064        }
3065
3066        if at > self.len() {
3067            assert_failed(at, self.len());
3068        }
3069
3070        let other_len = self.len - at;
3071        let mut other = Vec::with_capacity_in(other_len, self.allocator().clone());
3072
3073        // Unsafely `set_len` and copy items to `other`.
3074        unsafe {
3075            self.set_len(at);
3076            other.set_len(other_len);
3077
3078            ptr::copy_nonoverlapping(self.as_ptr().add(at), other.as_mut_ptr(), other.len());
3079        }
3080        other
3081    }
3082
3083    /// Resizes the `Vec` in-place so that `len` is equal to `new_len`.
3084    ///
3085    /// If `new_len` is greater than `len`, the `Vec` is extended by the
3086    /// difference, with each additional slot filled with the result of
3087    /// calling the closure `f`. The return values from `f` will end up
3088    /// in the `Vec` in the order they have been generated.
3089    ///
3090    /// If `new_len` is less than `len`, the `Vec` is simply truncated.
3091    ///
3092    /// This method uses a closure to create new values on every push. If
3093    /// you'd rather [`Clone`] a given value, use [`Vec::resize`]. If you
3094    /// want to use the [`Default`] trait to generate values, you can
3095    /// pass [`Default::default`] as the second argument.
3096    ///
3097    /// # Panics
3098    ///
3099    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
3100    ///
3101    /// # Examples
3102    ///
3103    /// ```
3104    /// let mut vec = vec![1, 2, 3];
3105    /// vec.resize_with(5, Default::default);
3106    /// assert_eq!(vec, [1, 2, 3, 0, 0]);
3107    ///
3108    /// let mut vec = vec![];
3109    /// let mut p = 1;
3110    /// vec.resize_with(4, || { p *= 2; p });
3111    /// assert_eq!(vec, [2, 4, 8, 16]);
3112    /// ```
3113    #[cfg(not(no_global_oom_handling))]
3114    #[stable(feature = "vec_resize_with", since = "1.33.0")]
3115    pub fn resize_with<F>(&mut self, new_len: usize, f: F)
3116    where
3117        F: FnMut() -> T,
3118    {
3119        let len = self.len();
3120        if new_len > len {
3121            self.extend_trusted(iter::repeat_with(f).take(new_len - len));
3122        } else {
3123            self.truncate(new_len);
3124        }
3125    }
3126
3127    /// Consumes and leaks the `Vec`, returning a mutable reference to the contents,
3128    /// `&'a mut [T]`.
3129    ///
3130    /// Note that the type `T` must outlive the chosen lifetime `'a`. If the type
3131    /// has only static references, or none at all, then this may be chosen to be
3132    /// `'static`.
3133    ///
3134    /// As of Rust 1.57, this method does not reallocate or shrink the `Vec`,
3135    /// so the leaked allocation may include unused capacity that is not part
3136    /// of the returned slice.
3137    ///
3138    /// This function is mainly useful for data that lives for the remainder of
3139    /// the program's life. Dropping the returned reference will cause a memory
3140    /// leak.
3141    ///
3142    /// # Examples
3143    ///
3144    /// Simple usage:
3145    ///
3146    /// ```
3147    /// let x = vec![1, 2, 3];
3148    /// let static_ref: &'static mut [usize] = x.leak();
3149    /// static_ref[0] += 1;
3150    /// assert_eq!(static_ref, &[2, 2, 3]);
3151    /// # // FIXME(https://github.com/rust-lang/miri/issues/3670):
3152    /// # // use -Zmiri-disable-leak-check instead of unleaking in tests meant to leak.
3153    /// # drop(unsafe { Box::from_raw(static_ref) });
3154    /// ```
3155    #[stable(feature = "vec_leak", since = "1.47.0")]
3156    #[inline]
3157    pub fn leak<'a>(self) -> &'a mut [T]
3158    where
3159        A: 'a,
3160    {
3161        let mut me = ManuallyDrop::new(self);
3162        unsafe { slice::from_raw_parts_mut(me.as_mut_ptr(), me.len) }
3163    }
3164
3165    /// Returns the remaining spare capacity of the vector as a slice of
3166    /// `MaybeUninit<T>`.
3167    ///
3168    /// The returned slice can be used to fill the vector with data (e.g. by
3169    /// reading from a file) before marking the data as initialized using the
3170    /// [`set_len`] method.
3171    ///
3172    /// [`set_len`]: Vec::set_len
3173    ///
3174    /// # Examples
3175    ///
3176    /// ```
3177    /// // Allocate vector big enough for 10 elements.
3178    /// let mut v = Vec::with_capacity(10);
3179    ///
3180    /// // Fill in the first 3 elements.
3181    /// let uninit = v.spare_capacity_mut();
3182    /// uninit[0].write(0);
3183    /// uninit[1].write(1);
3184    /// uninit[2].write(2);
3185    ///
3186    /// // Mark the first 3 elements of the vector as being initialized.
3187    /// unsafe {
3188    ///     v.set_len(3);
3189    /// }
3190    ///
3191    /// assert_eq!(&v, &[0, 1, 2]);
3192    /// ```
3193    #[stable(feature = "vec_spare_capacity", since = "1.60.0")]
3194    #[inline]
3195    pub fn spare_capacity_mut(&mut self) -> &mut [MaybeUninit<T>] {
3196        // Note:
3197        // This method is not implemented in terms of `split_at_spare_mut`,
3198        // to prevent invalidation of pointers to the buffer.
3199        unsafe {
3200            slice::from_raw_parts_mut(
3201                self.as_mut_ptr().add(self.len) as *mut MaybeUninit<T>,
3202                self.buf.capacity() - self.len,
3203            )
3204        }
3205    }
3206
3207    /// Returns vector content as a slice of `T`, along with the remaining spare
3208    /// capacity of the vector as a slice of `MaybeUninit<T>`.
3209    ///
3210    /// The returned spare capacity slice can be used to fill the vector with data
3211    /// (e.g. by reading from a file) before marking the data as initialized using
3212    /// the [`set_len`] method.
3213    ///
3214    /// [`set_len`]: Vec::set_len
3215    ///
3216    /// Note that this is a low-level API, which should be used with care for
3217    /// optimization purposes. If you need to append data to a `Vec`
3218    /// you can use [`push`], [`extend`], [`extend_from_slice`],
3219    /// [`extend_from_within`], [`insert`], [`append`], [`resize`] or
3220    /// [`resize_with`], depending on your exact needs.
3221    ///
3222    /// [`push`]: Vec::push
3223    /// [`extend`]: Vec::extend
3224    /// [`extend_from_slice`]: Vec::extend_from_slice
3225    /// [`extend_from_within`]: Vec::extend_from_within
3226    /// [`insert`]: Vec::insert
3227    /// [`append`]: Vec::append
3228    /// [`resize`]: Vec::resize
3229    /// [`resize_with`]: Vec::resize_with
3230    ///
3231    /// # Examples
3232    ///
3233    /// ```
3234    /// #![feature(vec_split_at_spare)]
3235    ///
3236    /// let mut v = vec![1, 1, 2];
3237    ///
3238    /// // Reserve additional space big enough for 10 elements.
3239    /// v.reserve(10);
3240    ///
3241    /// let (init, uninit) = v.split_at_spare_mut();
3242    /// let sum = init.iter().copied().sum::<u32>();
3243    ///
3244    /// // Fill in the next 4 elements.
3245    /// uninit[0].write(sum);
3246    /// uninit[1].write(sum * 2);
3247    /// uninit[2].write(sum * 3);
3248    /// uninit[3].write(sum * 4);
3249    ///
3250    /// // Mark the 4 elements of the vector as being initialized.
3251    /// unsafe {
3252    ///     let len = v.len();
3253    ///     v.set_len(len + 4);
3254    /// }
3255    ///
3256    /// assert_eq!(&v, &[1, 1, 2, 4, 8, 12, 16]);
3257    /// ```
3258    #[unstable(feature = "vec_split_at_spare", issue = "81944")]
3259    #[inline]
3260    pub fn split_at_spare_mut(&mut self) -> (&mut [T], &mut [MaybeUninit<T>]) {
3261        // SAFETY:
3262        // - len is ignored and so never changed
3263        let (init, spare, _) = unsafe { self.split_at_spare_mut_with_len() };
3264        (init, spare)
3265    }
3266
3267    /// Safety: changing returned .2 (&mut usize) is considered the same as calling `.set_len(_)`.
3268    ///
3269    /// This method provides unique access to all vec parts at once in `extend_from_within`.
3270    unsafe fn split_at_spare_mut_with_len(
3271        &mut self,
3272    ) -> (&mut [T], &mut [MaybeUninit<T>], &mut usize) {
3273        let ptr = self.as_mut_ptr();
3274        // SAFETY:
3275        // - `ptr` is guaranteed to be valid for `self.len` elements
3276        // - but the allocation extends out to `self.buf.capacity()` elements, possibly
3277        // uninitialized
3278        let spare_ptr = unsafe { ptr.add(self.len) };
3279        let spare_ptr = spare_ptr.cast_uninit();
3280        let spare_len = self.buf.capacity() - self.len;
3281
3282        // SAFETY:
3283        // - `ptr` is guaranteed to be valid for `self.len` elements
3284        // - `spare_ptr` is pointing one element past the buffer, so it doesn't overlap with `initialized`
3285        unsafe {
3286            let initialized = slice::from_raw_parts_mut(ptr, self.len);
3287            let spare = slice::from_raw_parts_mut(spare_ptr, spare_len);
3288
3289            (initialized, spare, &mut self.len)
3290        }
3291    }
3292
3293    /// Groups every `N` elements in the `Vec<T>` into chunks to produce a `Vec<[T; N]>`, dropping
3294    /// elements in the remainder. `N` must be greater than zero.
3295    ///
3296    /// If the capacity is not a multiple of the chunk size, the buffer will shrink down to the
3297    /// nearest multiple with a reallocation or deallocation.
3298    ///
3299    /// This function can be used to reverse [`Vec::into_flattened`].
3300    ///
3301    /// # Examples
3302    ///
3303    /// ```
3304    /// #![feature(vec_into_chunks)]
3305    ///
3306    /// let vec = vec![0, 1, 2, 3, 4, 5, 6, 7];
3307    /// assert_eq!(vec.into_chunks::<3>(), [[0, 1, 2], [3, 4, 5]]);
3308    ///
3309    /// let vec = vec![0, 1, 2, 3];
3310    /// let chunks: Vec<[u8; 10]> = vec.into_chunks();
3311    /// assert!(chunks.is_empty());
3312    ///
3313    /// let flat = vec![0; 8 * 8 * 8];
3314    /// let reshaped: Vec<[[[u8; 8]; 8]; 8]> = flat.into_chunks().into_chunks().into_chunks();
3315    /// assert_eq!(reshaped.len(), 1);
3316    /// ```
3317    #[cfg(not(no_global_oom_handling))]
3318    #[unstable(feature = "vec_into_chunks", issue = "142137")]
3319    pub fn into_chunks<const N: usize>(mut self) -> Vec<[T; N], A> {
3320        const {
3321            assert!(N != 0, "chunk size must be greater than zero");
3322        }
3323
3324        let (len, cap) = (self.len(), self.capacity());
3325
3326        let len_remainder = len % N;
3327        if len_remainder != 0 {
3328            self.truncate(len - len_remainder);
3329        }
3330
3331        let cap_remainder = cap % N;
3332        if !T::IS_ZST && cap_remainder != 0 {
3333            self.buf.shrink_to_fit(cap - cap_remainder);
3334        }
3335
3336        let (ptr, _, _, alloc) = self.into_raw_parts_with_alloc();
3337
3338        // SAFETY:
3339        // - `ptr` and `alloc` were just returned from `self.into_raw_parts_with_alloc()`
3340        // - `[T; N]` has the same alignment as `T`
3341        // - `size_of::<[T; N]>() * cap / N == size_of::<T>() * cap`
3342        // - `len / N <= cap / N` because `len <= cap`
3343        // - the allocated memory consists of `len / N` valid values of type `[T; N]`
3344        // - `cap / N` fits the size of the allocated memory after shrinking
3345        unsafe { Vec::from_raw_parts_in(ptr.cast(), len / N, cap / N, alloc) }
3346    }
3347
3348    /// This clears out this `Vec` and recycles the allocation into a new `Vec`.
3349    /// The item type of the resulting `Vec` needs to have the same size and
3350    /// alignment as the item type of the original `Vec`.
3351    ///
3352    /// # Examples
3353    ///
3354    ///  ```
3355    /// #![feature(vec_recycle, transmutability)]
3356    /// let a: Vec<u8> = vec![0; 100];
3357    /// let capacity = a.capacity();
3358    /// let addr = a.as_ptr().addr();
3359    /// let b: Vec<i8> = a.recycle();
3360    /// assert_eq!(b.len(), 0);
3361    /// assert_eq!(b.capacity(), capacity);
3362    /// assert_eq!(b.as_ptr().addr(), addr);
3363    /// ```
3364    ///
3365    /// The `Recyclable` bound prevents this method from being called when `T` and `U` have different sizes; e.g.:
3366    ///
3367    ///  ```compile_fail,E0277
3368    /// #![feature(vec_recycle, transmutability)]
3369    /// let vec: Vec<[u8; 2]> = Vec::new();
3370    /// let _: Vec<[u8; 1]> = vec.recycle();
3371    /// ```
3372    /// ...or different alignments:
3373    ///
3374    ///  ```compile_fail,E0277
3375    /// #![feature(vec_recycle, transmutability)]
3376    /// let vec: Vec<[u16; 0]> = Vec::new();
3377    /// let _: Vec<[u8; 0]> = vec.recycle();
3378    /// ```
3379    ///
3380    /// However, due to temporary implementation limitations of `Recyclable`,
3381    /// this method is not yet callable when `T` or `U` are slices, trait objects,
3382    /// or other exotic types; e.g.:
3383    ///
3384    /// ```compile_fail,E0277
3385    /// #![feature(vec_recycle, transmutability)]
3386    /// # let inputs = ["a b c", "d e f"];
3387    /// # fn process(_: &[&str]) {}
3388    /// let mut storage: Vec<&[&str]> = Vec::new();
3389    ///
3390    /// for input in inputs {
3391    ///     let mut buffer: Vec<&str> = storage.recycle();
3392    ///     buffer.extend(input.split(" "));
3393    ///     process(&buffer);
3394    ///     storage = buffer.recycle();
3395    /// }
3396    /// ```
3397    #[unstable(feature = "vec_recycle", issue = "148227")]
3398    #[expect(private_bounds)]
3399    pub fn recycle<U>(mut self) -> Vec<U, A>
3400    where
3401        U: Recyclable<T>,
3402    {
3403        self.clear();
3404        const {
3405            // FIXME(const-hack, 146097): compare `Layout`s
3406            assert!(size_of::<T>() == size_of::<U>());
3407            assert!(align_of::<T>() == align_of::<U>());
3408        };
3409        let (ptr, length, capacity, alloc) = self.into_parts_with_alloc();
3410        debug_assert_eq!(length, 0);
3411        // SAFETY:
3412        // - `ptr` and `alloc` were just returned from `self.into_raw_parts_with_alloc()`
3413        // - `T` & `U` have the same layout, so `capacity` does not need to be changed and we can safely use `alloc.dealloc` later
3414        // - the original vector was cleared, so there is no problem with "transmuting" the stored values
3415        unsafe { Vec::from_parts_in(ptr.cast::<U>(), length, capacity, alloc) }
3416    }
3417}
3418
3419/// Denotes that an allocation of `From` can be recycled into an allocation of `Self`.
3420///
3421/// # Safety
3422///
3423/// `Self` is `Recyclable<From>` if `Layout::new::<Self>() == Layout::new::<From>()`.
3424unsafe trait Recyclable<From: Sized>: Sized {}
3425
3426#[unstable_feature_bound(transmutability)]
3427// SAFETY: enforced by `TransmuteFrom`
3428unsafe impl<From, To> Recyclable<From> for To
3429where
3430    for<'a> &'a MaybeUninit<To>: TransmuteFrom<&'a MaybeUninit<From>, { Assume::SAFETY }>,
3431    for<'a> &'a MaybeUninit<From>: TransmuteFrom<&'a MaybeUninit<To>, { Assume::SAFETY }>,
3432{
3433}
3434
3435impl<T: Clone, A: Allocator> Vec<T, A> {
3436    /// Resizes the `Vec` in-place so that `len` is equal to `new_len`.
3437    ///
3438    /// If `new_len` is greater than `len`, the `Vec` is extended by the
3439    /// difference, with each additional slot filled with `value`.
3440    /// If `new_len` is less than `len`, the `Vec` is simply truncated.
3441    ///
3442    /// This method requires `T` to implement [`Clone`],
3443    /// in order to be able to clone the passed value.
3444    /// If you need more flexibility (or want to rely on [`Default`] instead of
3445    /// [`Clone`]), use [`Vec::resize_with`].
3446    /// If you only need to resize to a smaller size, use [`Vec::truncate`].
3447    ///
3448    /// # Panics
3449    ///
3450    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
3451    ///
3452    /// # Examples
3453    ///
3454    /// ```
3455    /// let mut vec = vec!["hello"];
3456    /// vec.resize(3, "world");
3457    /// assert_eq!(vec, ["hello", "world", "world"]);
3458    ///
3459    /// let mut vec = vec!['a', 'b', 'c', 'd'];
3460    /// vec.resize(2, '_');
3461    /// assert_eq!(vec, ['a', 'b']);
3462    /// ```
3463    #[cfg(not(no_global_oom_handling))]
3464    #[stable(feature = "vec_resize", since = "1.5.0")]
3465    pub fn resize(&mut self, new_len: usize, value: T) {
3466        let len = self.len();
3467
3468        if new_len > len {
3469            self.extend_with(new_len - len, value)
3470        } else {
3471            self.truncate(new_len);
3472        }
3473    }
3474
3475    /// Clones and appends all elements in a slice to the `Vec`.
3476    ///
3477    /// Iterates over the slice `other`, clones each element, and then appends
3478    /// it to this `Vec`. The `other` slice is traversed in-order.
3479    ///
3480    /// Note that this function is the same as [`extend`],
3481    /// except that it also works with slice elements that are Clone but not Copy.
3482    /// If Rust gets specialization this function may be deprecated.
3483    ///
3484    /// # Panics
3485    ///
3486    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
3487    ///
3488    /// # Examples
3489    ///
3490    /// ```
3491    /// let mut vec = vec![1];
3492    /// vec.extend_from_slice(&[2, 3, 4]);
3493    /// assert_eq!(vec, [1, 2, 3, 4]);
3494    /// ```
3495    ///
3496    /// [`extend`]: Vec::extend
3497    #[cfg(not(no_global_oom_handling))]
3498    #[stable(feature = "vec_extend_from_slice", since = "1.6.0")]
3499    pub fn extend_from_slice(&mut self, other: &[T]) {
3500        self.spec_extend(other.iter())
3501    }
3502
3503    /// Given a range `src`, clones a slice of elements in that range and appends it to the end.
3504    ///
3505    /// `src` must be a range that can form a valid subslice of the `Vec`.
3506    ///
3507    /// # Panics
3508    ///
3509    /// Panics if starting index is greater than the end index, if the index is
3510    /// greater than the length of the vector, or if the new capacity exceeds
3511    /// `isize::MAX` _bytes_.
3512    ///
3513    /// # Examples
3514    ///
3515    /// ```
3516    /// let mut characters = vec!['a', 'b', 'c', 'd', 'e'];
3517    /// characters.extend_from_within(2..);
3518    /// assert_eq!(characters, ['a', 'b', 'c', 'd', 'e', 'c', 'd', 'e']);
3519    ///
3520    /// let mut numbers = vec![0, 1, 2, 3, 4];
3521    /// numbers.extend_from_within(..2);
3522    /// assert_eq!(numbers, [0, 1, 2, 3, 4, 0, 1]);
3523    ///
3524    /// let mut strings = vec![String::from("hello"), String::from("world"), String::from("!")];
3525    /// strings.extend_from_within(1..=2);
3526    /// assert_eq!(strings, ["hello", "world", "!", "world", "!"]);
3527    /// ```
3528    #[cfg(not(no_global_oom_handling))]
3529    #[stable(feature = "vec_extend_from_within", since = "1.53.0")]
3530    pub fn extend_from_within<R>(&mut self, src: R)
3531    where
3532        R: RangeBounds<usize>,
3533    {
3534        let range = slice::range(src, ..self.len());
3535        self.reserve(range.len());
3536
3537        // SAFETY:
3538        // - `slice::range` guarantees that the given range is valid for indexing self
3539        unsafe {
3540            self.spec_extend_from_within(range);
3541        }
3542    }
3543}
3544
3545impl<T, A: Allocator, const N: usize> Vec<[T; N], A> {
3546    /// Takes a `Vec<[T; N]>` and flattens it into a `Vec<T>`.
3547    ///
3548    /// # Panics
3549    ///
3550    /// Panics if the length of the resulting vector would overflow a `usize`.
3551    ///
3552    /// This is only possible when flattening a vector of arrays of zero-sized
3553    /// types, and thus tends to be irrelevant in practice. If
3554    /// `size_of::<T>() > 0`, this will never panic.
3555    ///
3556    /// # Examples
3557    ///
3558    /// ```
3559    /// let mut vec = vec![[1, 2, 3], [4, 5, 6], [7, 8, 9]];
3560    /// assert_eq!(vec.pop(), Some([7, 8, 9]));
3561    ///
3562    /// let mut flattened = vec.into_flattened();
3563    /// assert_eq!(flattened.pop(), Some(6));
3564    /// ```
3565    #[stable(feature = "slice_flatten", since = "1.80.0")]
3566    pub fn into_flattened(self) -> Vec<T, A> {
3567        let (ptr, len, cap, alloc) = self.into_raw_parts_with_alloc();
3568        let (new_len, new_cap) = if T::IS_ZST {
3569            (len.checked_mul(N).expect("vec len overflow"), usize::MAX)
3570        } else {
3571            // SAFETY:
3572            // - `cap * N` cannot overflow because the allocation is already in
3573            // the address space.
3574            // - Each `[T; N]` has `N` valid elements, so there are `len * N`
3575            // valid elements in the allocation.
3576            unsafe { (len.unchecked_mul(N), cap.unchecked_mul(N)) }
3577        };
3578        // SAFETY:
3579        // - `ptr` was allocated by `self`
3580        // - `ptr` is well-aligned because `[T; N]` has the same alignment as `T`.
3581        // - `new_cap` refers to the same sized allocation as `cap` because
3582        // `new_cap * size_of::<T>()` == `cap * size_of::<[T; N]>()`
3583        // - `len` <= `cap`, so `len * N` <= `cap * N`.
3584        unsafe { Vec::<T, A>::from_raw_parts_in(ptr.cast(), new_len, new_cap, alloc) }
3585    }
3586}
3587
3588impl<T: Clone, A: Allocator> Vec<T, A> {
3589    #[cfg(not(no_global_oom_handling))]
3590    /// Extend the vector by `n` clones of value.
3591    fn extend_with(&mut self, n: usize, value: T) {
3592        self.reserve(n);
3593
3594        unsafe {
3595            let mut ptr = self.as_mut_ptr().add(self.len());
3596            // Use SetLenOnDrop to work around bug where compiler
3597            // might not realize the store through `ptr` through self.set_len()
3598            // don't alias.
3599            let mut local_len = SetLenOnDrop::new(&mut self.len);
3600
3601            // Write all elements except the last one
3602            for _ in 1..n {
3603                ptr::write(ptr, value.clone());
3604                ptr = ptr.add(1);
3605                // Increment the length in every step in case clone() panics
3606                local_len.increment_len(1);
3607            }
3608
3609            if n > 0 {
3610                // We can write the last element directly without cloning needlessly
3611                ptr::write(ptr, value);
3612                local_len.increment_len(1);
3613            }
3614
3615            // len set by scope guard
3616        }
3617    }
3618}
3619
3620impl<T: PartialEq, A: Allocator> Vec<T, A> {
3621    /// Removes consecutive repeated elements in the vector according to the
3622    /// [`PartialEq`] trait implementation.
3623    ///
3624    /// If the vector is sorted, this removes all duplicates.
3625    ///
3626    /// # Examples
3627    ///
3628    /// ```
3629    /// let mut vec = vec![1, 2, 2, 3, 2];
3630    ///
3631    /// vec.dedup();
3632    ///
3633    /// assert_eq!(vec, [1, 2, 3, 2]);
3634    /// ```
3635    #[stable(feature = "rust1", since = "1.0.0")]
3636    #[inline]
3637    pub fn dedup(&mut self) {
3638        self.dedup_by(|a, b| a == b)
3639    }
3640}
3641
3642////////////////////////////////////////////////////////////////////////////////
3643// Internal methods and functions
3644////////////////////////////////////////////////////////////////////////////////
3645
3646#[doc(hidden)]
3647#[cfg(not(no_global_oom_handling))]
3648#[stable(feature = "rust1", since = "1.0.0")]
3649#[rustc_diagnostic_item = "vec_from_elem"]
3650pub fn from_elem<T: Clone>(elem: T, n: usize) -> Vec<T> {
3651    <T as SpecFromElem>::from_elem(elem, n, Global)
3652}
3653
3654#[doc(hidden)]
3655#[cfg(not(no_global_oom_handling))]
3656#[unstable(feature = "allocator_api", issue = "32838")]
3657pub fn from_elem_in<T: Clone, A: Allocator>(elem: T, n: usize, alloc: A) -> Vec<T, A> {
3658    <T as SpecFromElem>::from_elem(elem, n, alloc)
3659}
3660
3661#[cfg(not(no_global_oom_handling))]
3662trait ExtendFromWithinSpec {
3663    /// # Safety
3664    ///
3665    /// - `src` needs to be valid index
3666    /// - `self.capacity() - self.len()` must be `>= src.len()`
3667    unsafe fn spec_extend_from_within(&mut self, src: Range<usize>);
3668}
3669
3670#[cfg(not(no_global_oom_handling))]
3671impl<T: Clone, A: Allocator> ExtendFromWithinSpec for Vec<T, A> {
3672    default unsafe fn spec_extend_from_within(&mut self, src: Range<usize>) {
3673        // SAFETY:
3674        // - len is increased only after initializing elements
3675        let (this, spare, len) = unsafe { self.split_at_spare_mut_with_len() };
3676
3677        // SAFETY:
3678        // - caller guarantees that src is a valid index
3679        let to_clone = unsafe { this.get_unchecked(src) };
3680
3681        iter::zip(to_clone, spare)
3682            .map(|(src, dst)| dst.write(src.clone()))
3683            // Note:
3684            // - Element was just initialized with `MaybeUninit::write`, so it's ok to increase len
3685            // - len is increased after each element to prevent leaks (see issue #82533)
3686            .for_each(|_| *len += 1);
3687    }
3688}
3689
3690#[cfg(not(no_global_oom_handling))]
3691impl<T: TrivialClone, A: Allocator> ExtendFromWithinSpec for Vec<T, A> {
3692    unsafe fn spec_extend_from_within(&mut self, src: Range<usize>) {
3693        let count = src.len();
3694        {
3695            let (init, spare) = self.split_at_spare_mut();
3696
3697            // SAFETY:
3698            // - caller guarantees that `src` is a valid index
3699            let source = unsafe { init.get_unchecked(src) };
3700
3701            // SAFETY:
3702            // - Both pointers are created from unique slice references (`&mut [_]`)
3703            //   so they are valid and do not overlap.
3704            // - Elements implement `TrivialClone` so this is equivalent to calling
3705            //   `clone` on every one of them.
3706            // - `count` is equal to the len of `source`, so source is valid for
3707            //   `count` reads
3708            // - `.reserve(count)` guarantees that `spare.len() >= count` so spare
3709            //   is valid for `count` writes
3710            unsafe { ptr::copy_nonoverlapping(source.as_ptr(), spare.as_mut_ptr() as _, count) };
3711        }
3712
3713        // SAFETY:
3714        // - The elements were just initialized by `copy_nonoverlapping`
3715        self.len += count;
3716    }
3717}
3718
3719////////////////////////////////////////////////////////////////////////////////
3720// Common trait implementations for Vec
3721////////////////////////////////////////////////////////////////////////////////
3722
3723#[stable(feature = "rust1", since = "1.0.0")]
3724impl<T, A: Allocator> ops::Deref for Vec<T, A> {
3725    type Target = [T];
3726
3727    #[inline]
3728    fn deref(&self) -> &[T] {
3729        self.as_slice()
3730    }
3731}
3732
3733#[stable(feature = "rust1", since = "1.0.0")]
3734impl<T, A: Allocator> ops::DerefMut for Vec<T, A> {
3735    #[inline]
3736    fn deref_mut(&mut self) -> &mut [T] {
3737        self.as_mut_slice()
3738    }
3739}
3740
3741#[unstable(feature = "deref_pure_trait", issue = "87121")]
3742unsafe impl<T, A: Allocator> ops::DerefPure for Vec<T, A> {}
3743
3744#[cfg(not(no_global_oom_handling))]
3745#[stable(feature = "rust1", since = "1.0.0")]
3746impl<T: Clone, A: Allocator + Clone> Clone for Vec<T, A> {
3747    fn clone(&self) -> Self {
3748        let alloc = self.allocator().clone();
3749        <[T]>::to_vec_in(&**self, alloc)
3750    }
3751
3752    /// Overwrites the contents of `self` with a clone of the contents of `source`.
3753    ///
3754    /// This method is preferred over simply assigning `source.clone()` to `self`,
3755    /// as it avoids reallocation if possible. Additionally, if the element type
3756    /// `T` overrides `clone_from()`, this will reuse the resources of `self`'s
3757    /// elements as well.
3758    ///
3759    /// # Examples
3760    ///
3761    /// ```
3762    /// let x = vec![5, 6, 7];
3763    /// let mut y = vec![8, 9, 10];
3764    /// let yp: *const i32 = y.as_ptr();
3765    ///
3766    /// y.clone_from(&x);
3767    ///
3768    /// // The value is the same
3769    /// assert_eq!(x, y);
3770    ///
3771    /// // And no reallocation occurred
3772    /// assert_eq!(yp, y.as_ptr());
3773    /// ```
3774    fn clone_from(&mut self, source: &Self) {
3775        crate::slice::SpecCloneIntoVec::clone_into(source.as_slice(), self);
3776    }
3777}
3778
3779/// The hash of a vector is the same as that of the corresponding slice,
3780/// as required by the `core::borrow::Borrow` implementation.
3781///
3782/// ```
3783/// use std::hash::BuildHasher;
3784///
3785/// let b = std::hash::RandomState::new();
3786/// let v: Vec<u8> = vec![0xa8, 0x3c, 0x09];
3787/// let s: &[u8] = &[0xa8, 0x3c, 0x09];
3788/// assert_eq!(b.hash_one(v), b.hash_one(s));
3789/// ```
3790#[stable(feature = "rust1", since = "1.0.0")]
3791impl<T: Hash, A: Allocator> Hash for Vec<T, A> {
3792    #[inline]
3793    fn hash<H: Hasher>(&self, state: &mut H) {
3794        Hash::hash(&**self, state)
3795    }
3796}
3797
3798#[stable(feature = "rust1", since = "1.0.0")]
3799impl<T, I: SliceIndex<[T]>, A: Allocator> Index<I> for Vec<T, A> {
3800    type Output = I::Output;
3801
3802    #[inline]
3803    fn index(&self, index: I) -> &Self::Output {
3804        Index::index(&**self, index)
3805    }
3806}
3807
3808#[stable(feature = "rust1", since = "1.0.0")]
3809impl<T, I: SliceIndex<[T]>, A: Allocator> IndexMut<I> for Vec<T, A> {
3810    #[inline]
3811    fn index_mut(&mut self, index: I) -> &mut Self::Output {
3812        IndexMut::index_mut(&mut **self, index)
3813    }
3814}
3815
3816/// Collects an iterator into a Vec, commonly called via [`Iterator::collect()`]
3817///
3818/// # Allocation behavior
3819///
3820/// In general `Vec` does not guarantee any particular growth or allocation strategy.
3821/// That also applies to this trait impl.
3822///
3823/// **Note:** This section covers implementation details and is therefore exempt from
3824/// stability guarantees.
3825///
3826/// Vec may use any or none of the following strategies,
3827/// depending on the supplied iterator:
3828///
3829/// * preallocate based on [`Iterator::size_hint()`]
3830///   * and panic if the number of items is outside the provided lower/upper bounds
3831/// * use an amortized growth strategy similar to `pushing` one item at a time
3832/// * perform the iteration in-place on the original allocation backing the iterator
3833///
3834/// The last case warrants some attention. It is an optimization that in many cases reduces peak memory
3835/// consumption and improves cache locality. But when big, short-lived allocations are created,
3836/// only a small fraction of their items get collected, no further use is made of the spare capacity
3837/// and the resulting `Vec` is moved into a longer-lived structure, then this can lead to the large
3838/// allocations having their lifetimes unnecessarily extended which can result in increased memory
3839/// footprint.
3840///
3841/// In cases where this is an issue, the excess capacity can be discarded with [`Vec::shrink_to()`],
3842/// [`Vec::shrink_to_fit()`] or by collecting into [`Box<[T]>`][owned slice] instead, which additionally reduces
3843/// the size of the long-lived struct.
3844///
3845/// [owned slice]: Box
3846///
3847/// ```rust
3848/// # use std::sync::Mutex;
3849/// static LONG_LIVED: Mutex<Vec<Vec<u16>>> = Mutex::new(Vec::new());
3850///
3851/// for i in 0..10 {
3852///     let big_temporary: Vec<u16> = (0..1024).collect();
3853///     // discard most items
3854///     let mut result: Vec<_> = big_temporary.into_iter().filter(|i| i % 100 == 0).collect();
3855///     // without this a lot of unused capacity might be moved into the global
3856///     result.shrink_to_fit();
3857///     LONG_LIVED.lock().unwrap().push(result);
3858/// }
3859/// ```
3860#[cfg(not(no_global_oom_handling))]
3861#[stable(feature = "rust1", since = "1.0.0")]
3862impl<T> FromIterator<T> for Vec<T> {
3863    #[inline]
3864    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Vec<T> {
3865        <Self as SpecFromIter<T, I::IntoIter>>::from_iter(iter.into_iter())
3866    }
3867}
3868
3869#[stable(feature = "rust1", since = "1.0.0")]
3870impl<T, A: Allocator> IntoIterator for Vec<T, A> {
3871    type Item = T;
3872    type IntoIter = IntoIter<T, A>;
3873
3874    /// Creates a consuming iterator, that is, one that moves each value out of
3875    /// the vector (from start to end). The vector cannot be used after calling
3876    /// this.
3877    ///
3878    /// # Examples
3879    ///
3880    /// ```
3881    /// let v = vec!["a".to_string(), "b".to_string()];
3882    /// let mut v_iter = v.into_iter();
3883    ///
3884    /// let first_element: Option<String> = v_iter.next();
3885    ///
3886    /// assert_eq!(first_element, Some("a".to_string()));
3887    /// assert_eq!(v_iter.next(), Some("b".to_string()));
3888    /// assert_eq!(v_iter.next(), None);
3889    /// ```
3890    #[inline]
3891    fn into_iter(self) -> Self::IntoIter {
3892        unsafe {
3893            let me = ManuallyDrop::new(self);
3894            let alloc = ManuallyDrop::new(ptr::read(me.allocator()));
3895            let buf = me.buf.non_null();
3896            let begin = buf.as_ptr();
3897            let end = if T::IS_ZST {
3898                begin.wrapping_byte_add(me.len())
3899            } else {
3900                begin.add(me.len()) as *const T
3901            };
3902            let cap = me.buf.capacity();
3903            IntoIter { buf, phantom: PhantomData, cap, alloc, ptr: buf, end }
3904        }
3905    }
3906}
3907
3908#[stable(feature = "rust1", since = "1.0.0")]
3909impl<'a, T, A: Allocator> IntoIterator for &'a Vec<T, A> {
3910    type Item = &'a T;
3911    type IntoIter = slice::Iter<'a, T>;
3912
3913    fn into_iter(self) -> Self::IntoIter {
3914        self.iter()
3915    }
3916}
3917
3918#[stable(feature = "rust1", since = "1.0.0")]
3919impl<'a, T, A: Allocator> IntoIterator for &'a mut Vec<T, A> {
3920    type Item = &'a mut T;
3921    type IntoIter = slice::IterMut<'a, T>;
3922
3923    fn into_iter(self) -> Self::IntoIter {
3924        self.iter_mut()
3925    }
3926}
3927
3928#[cfg(not(no_global_oom_handling))]
3929#[stable(feature = "rust1", since = "1.0.0")]
3930impl<T, A: Allocator> Extend<T> for Vec<T, A> {
3931    #[inline]
3932    fn extend<I: IntoIterator<Item = T>>(&mut self, iter: I) {
3933        <Self as SpecExtend<T, I::IntoIter>>::spec_extend(self, iter.into_iter())
3934    }
3935
3936    #[inline]
3937    fn extend_one(&mut self, item: T) {
3938        self.push(item);
3939    }
3940
3941    #[inline]
3942    fn extend_reserve(&mut self, additional: usize) {
3943        self.reserve(additional);
3944    }
3945
3946    #[inline]
3947    unsafe fn extend_one_unchecked(&mut self, item: T) {
3948        // SAFETY: Our preconditions ensure the space has been reserved, and `extend_reserve` is implemented correctly.
3949        unsafe {
3950            let len = self.len();
3951            ptr::write(self.as_mut_ptr().add(len), item);
3952            self.set_len(len + 1);
3953        }
3954    }
3955}
3956
3957impl<T, A: Allocator> Vec<T, A> {
3958    // leaf method to which various SpecFrom/SpecExtend implementations delegate when
3959    // they have no further optimizations to apply
3960    #[cfg(not(no_global_oom_handling))]
3961    fn extend_desugared<I: Iterator<Item = T>>(&mut self, mut iterator: I) {
3962        // This is the case for a general iterator.
3963        //
3964        // This function should be the moral equivalent of:
3965        //
3966        //      for item in iterator {
3967        //          self.push(item);
3968        //      }
3969        while let Some(element) = iterator.next() {
3970            let len = self.len();
3971            if len == self.capacity() {
3972                let (lower, _) = iterator.size_hint();
3973                self.reserve(lower.saturating_add(1));
3974            }
3975            unsafe {
3976                ptr::write(self.as_mut_ptr().add(len), element);
3977                // Since next() executes user code which can panic we have to bump the length
3978                // after each step.
3979                // NB can't overflow since we would have had to alloc the address space
3980                self.set_len(len + 1);
3981            }
3982        }
3983    }
3984
3985    // specific extend for `TrustedLen` iterators, called both by the specializations
3986    // and internal places where resolving specialization makes compilation slower
3987    #[cfg(not(no_global_oom_handling))]
3988    fn extend_trusted(&mut self, iterator: impl iter::TrustedLen<Item = T>) {
3989        let (low, high) = iterator.size_hint();
3990        if let Some(additional) = high {
3991            debug_assert_eq!(
3992                low,
3993                additional,
3994                "TrustedLen iterator's size hint is not exact: {:?}",
3995                (low, high)
3996            );
3997            self.reserve(additional);
3998            unsafe {
3999                let ptr = self.as_mut_ptr();
4000                let mut local_len = SetLenOnDrop::new(&mut self.len);
4001                iterator.for_each(move |element| {
4002                    ptr::write(ptr.add(local_len.current_len()), element);
4003                    // Since the loop executes user code which can panic we have to update
4004                    // the length every step to correctly drop what we've written.
4005                    // NB can't overflow since we would have had to alloc the address space
4006                    local_len.increment_len(1);
4007                });
4008            }
4009        } else {
4010            // Per TrustedLen contract a `None` upper bound means that the iterator length
4011            // truly exceeds usize::MAX, which would eventually lead to a capacity overflow anyway.
4012            // Since the other branch already panics eagerly (via `reserve()`) we do the same here.
4013            // This avoids additional codegen for a fallback code path which would eventually
4014            // panic anyway.
4015            panic!("capacity overflow");
4016        }
4017    }
4018
4019    /// Creates a splicing iterator that replaces the specified range in the vector
4020    /// with the given `replace_with` iterator and yields the removed items.
4021    /// `replace_with` does not need to be the same length as `range`.
4022    ///
4023    /// `range` is removed even if the `Splice` iterator is not consumed before it is dropped.
4024    ///
4025    /// It is unspecified how many elements are removed from the vector
4026    /// if the `Splice` value is leaked.
4027    ///
4028    /// The input iterator `replace_with` is only consumed when the `Splice` value is dropped.
4029    ///
4030    /// This is optimal if:
4031    ///
4032    /// * The tail (elements in the vector after `range`) is empty,
4033    /// * or `replace_with` yields fewer or equal elements than `range`'s length
4034    /// * or the lower bound of its `size_hint()` is exact.
4035    ///
4036    /// Otherwise, a temporary vector is allocated and the tail is moved twice.
4037    ///
4038    /// # Panics
4039    ///
4040    /// Panics if the range has `start_bound > end_bound`, or, if the range is
4041    /// bounded on either end and past the length of the vector.
4042    ///
4043    /// # Examples
4044    ///
4045    /// ```
4046    /// let mut v = vec![1, 2, 3, 4];
4047    /// let new = [7, 8, 9];
4048    /// let u: Vec<_> = v.splice(1..3, new).collect();
4049    /// assert_eq!(v, [1, 7, 8, 9, 4]);
4050    /// assert_eq!(u, [2, 3]);
4051    /// ```
4052    ///
4053    /// Using `splice` to insert new items into a vector efficiently at a specific position
4054    /// indicated by an empty range:
4055    ///
4056    /// ```
4057    /// let mut v = vec![1, 5];
4058    /// let new = [2, 3, 4];
4059    /// v.splice(1..1, new);
4060    /// assert_eq!(v, [1, 2, 3, 4, 5]);
4061    /// ```
4062    #[cfg(not(no_global_oom_handling))]
4063    #[inline]
4064    #[stable(feature = "vec_splice", since = "1.21.0")]
4065    pub fn splice<R, I>(&mut self, range: R, replace_with: I) -> Splice<'_, I::IntoIter, A>
4066    where
4067        R: RangeBounds<usize>,
4068        I: IntoIterator<Item = T>,
4069    {
4070        Splice { drain: self.drain(range), replace_with: replace_with.into_iter() }
4071    }
4072
4073    /// Creates an iterator which uses a closure to determine if an element in the range should be removed.
4074    ///
4075    /// If the closure returns `true`, the element is removed from the vector
4076    /// and yielded. If the closure returns `false`, or panics, the element
4077    /// remains in the vector and will not be yielded.
4078    ///
4079    /// Only elements that fall in the provided range are considered for extraction, but any elements
4080    /// after the range will still have to be moved if any element has been extracted.
4081    ///
4082    /// If the returned `ExtractIf` is not exhausted, e.g. because it is dropped without iterating
4083    /// or the iteration short-circuits, then the remaining elements will be retained.
4084    /// Use `extract_if().for_each(drop)` if you do not need the returned iterator,
4085    /// or [`retain_mut`] with a negated predicate if you also do not need to restrict the range.
4086    ///
4087    /// [`retain_mut`]: Vec::retain_mut
4088    ///
4089    /// Using this method is equivalent to the following code:
4090    ///
4091    /// ```
4092    /// # let some_predicate = |x: &mut i32| { *x % 2 == 1 };
4093    /// # let mut vec = vec![0, 1, 2, 3, 4, 5, 6];
4094    /// # let mut vec2 = vec.clone();
4095    /// # let range = 1..5;
4096    /// let mut i = range.start;
4097    /// let end_items = vec.len() - range.end;
4098    /// # let mut extracted = vec![];
4099    ///
4100    /// while i < vec.len() - end_items {
4101    ///     if some_predicate(&mut vec[i]) {
4102    ///         let val = vec.remove(i);
4103    ///         // your code here
4104    /// #         extracted.push(val);
4105    ///     } else {
4106    ///         i += 1;
4107    ///     }
4108    /// }
4109    ///
4110    /// # let extracted2: Vec<_> = vec2.extract_if(range, some_predicate).collect();
4111    /// # assert_eq!(vec, vec2);
4112    /// # assert_eq!(extracted, extracted2);
4113    /// ```
4114    ///
4115    /// But `extract_if` is easier to use. `extract_if` is also more efficient,
4116    /// because it can backshift the elements of the array in bulk.
4117    ///
4118    /// The iterator also lets you mutate the value of each element in the
4119    /// closure, regardless of whether you choose to keep or remove it.
4120    ///
4121    /// # Panics
4122    ///
4123    /// If `range` is out of bounds.
4124    ///
4125    /// # Examples
4126    ///
4127    /// Splitting a vector into even and odd values, reusing the original vector:
4128    ///
4129    /// ```
4130    /// let mut numbers = vec![1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15];
4131    ///
4132    /// let evens = numbers.extract_if(.., |x| *x % 2 == 0).collect::<Vec<_>>();
4133    /// let odds = numbers;
4134    ///
4135    /// assert_eq!(evens, vec![2, 4, 6, 8, 14]);
4136    /// assert_eq!(odds, vec![1, 3, 5, 9, 11, 13, 15]);
4137    /// ```
4138    ///
4139    /// Using the range argument to only process a part of the vector:
4140    ///
4141    /// ```
4142    /// let mut items = vec![0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2];
4143    /// let ones = items.extract_if(7.., |x| *x == 1).collect::<Vec<_>>();
4144    /// assert_eq!(items, vec![0, 0, 0, 0, 0, 0, 0, 2, 2, 2]);
4145    /// assert_eq!(ones.len(), 3);
4146    /// ```
4147    #[stable(feature = "extract_if", since = "1.87.0")]
4148    pub fn extract_if<F, R>(&mut self, range: R, filter: F) -> ExtractIf<'_, T, F, A>
4149    where
4150        F: FnMut(&mut T) -> bool,
4151        R: RangeBounds<usize>,
4152    {
4153        ExtractIf::new(self, filter, range)
4154    }
4155}
4156
4157/// Extend implementation that copies elements out of references before pushing them onto the Vec.
4158///
4159/// This implementation is specialized for slice iterators, where it uses [`copy_from_slice`] to
4160/// append the entire slice at once.
4161///
4162/// [`copy_from_slice`]: slice::copy_from_slice
4163#[cfg(not(no_global_oom_handling))]
4164#[stable(feature = "extend_ref", since = "1.2.0")]
4165impl<'a, T: Copy + 'a, A: Allocator> Extend<&'a T> for Vec<T, A> {
4166    fn extend<I: IntoIterator<Item = &'a T>>(&mut self, iter: I) {
4167        self.spec_extend(iter.into_iter())
4168    }
4169
4170    #[inline]
4171    fn extend_one(&mut self, &item: &'a T) {
4172        self.push(item);
4173    }
4174
4175    #[inline]
4176    fn extend_reserve(&mut self, additional: usize) {
4177        self.reserve(additional);
4178    }
4179
4180    #[inline]
4181    unsafe fn extend_one_unchecked(&mut self, &item: &'a T) {
4182        // SAFETY: Our preconditions ensure the space has been reserved, and `extend_reserve` is implemented correctly.
4183        unsafe {
4184            let len = self.len();
4185            ptr::write(self.as_mut_ptr().add(len), item);
4186            self.set_len(len + 1);
4187        }
4188    }
4189}
4190
4191/// Implements comparison of vectors, [lexicographically](Ord#lexicographical-comparison).
4192#[stable(feature = "rust1", since = "1.0.0")]
4193impl<T, A1, A2> PartialOrd<Vec<T, A2>> for Vec<T, A1>
4194where
4195    T: PartialOrd,
4196    A1: Allocator,
4197    A2: Allocator,
4198{
4199    #[inline]
4200    fn partial_cmp(&self, other: &Vec<T, A2>) -> Option<Ordering> {
4201        PartialOrd::partial_cmp(&**self, &**other)
4202    }
4203}
4204
4205#[stable(feature = "rust1", since = "1.0.0")]
4206impl<T: Eq, A: Allocator> Eq for Vec<T, A> {}
4207
4208/// Implements ordering of vectors, [lexicographically](Ord#lexicographical-comparison).
4209#[stable(feature = "rust1", since = "1.0.0")]
4210impl<T: Ord, A: Allocator> Ord for Vec<T, A> {
4211    #[inline]
4212    fn cmp(&self, other: &Self) -> Ordering {
4213        Ord::cmp(&**self, &**other)
4214    }
4215}
4216
4217#[stable(feature = "rust1", since = "1.0.0")]
4218unsafe impl<#[may_dangle] T, A: Allocator> Drop for Vec<T, A> {
4219    fn drop(&mut self) {
4220        unsafe {
4221            // use drop for [T]
4222            // use a raw slice to refer to the elements of the vector as weakest necessary type;
4223            // could avoid questions of validity in certain cases
4224            ptr::drop_in_place(ptr::slice_from_raw_parts_mut(self.as_mut_ptr(), self.len))
4225        }
4226        // RawVec handles deallocation
4227    }
4228}
4229
4230#[stable(feature = "rust1", since = "1.0.0")]
4231#[rustc_const_unstable(feature = "const_default", issue = "143894")]
4232impl<T> const Default for Vec<T> {
4233    /// Creates an empty `Vec<T>`.
4234    ///
4235    /// The vector will not allocate until elements are pushed onto it.
4236    fn default() -> Vec<T> {
4237        Vec::new()
4238    }
4239}
4240
4241#[stable(feature = "rust1", since = "1.0.0")]
4242impl<T: fmt::Debug, A: Allocator> fmt::Debug for Vec<T, A> {
4243    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
4244        fmt::Debug::fmt(&**self, f)
4245    }
4246}
4247
4248#[stable(feature = "rust1", since = "1.0.0")]
4249impl<T, A: Allocator> AsRef<Vec<T, A>> for Vec<T, A> {
4250    fn as_ref(&self) -> &Vec<T, A> {
4251        self
4252    }
4253}
4254
4255#[stable(feature = "vec_as_mut", since = "1.5.0")]
4256impl<T, A: Allocator> AsMut<Vec<T, A>> for Vec<T, A> {
4257    fn as_mut(&mut self) -> &mut Vec<T, A> {
4258        self
4259    }
4260}
4261
4262#[stable(feature = "rust1", since = "1.0.0")]
4263impl<T, A: Allocator> AsRef<[T]> for Vec<T, A> {
4264    fn as_ref(&self) -> &[T] {
4265        self
4266    }
4267}
4268
4269#[stable(feature = "vec_as_mut", since = "1.5.0")]
4270impl<T, A: Allocator> AsMut<[T]> for Vec<T, A> {
4271    fn as_mut(&mut self) -> &mut [T] {
4272        self
4273    }
4274}
4275
4276#[cfg(not(no_global_oom_handling))]
4277#[stable(feature = "rust1", since = "1.0.0")]
4278impl<T: Clone> From<&[T]> for Vec<T> {
4279    /// Allocates a `Vec<T>` and fills it by cloning `s`'s items.
4280    ///
4281    /// # Examples
4282    ///
4283    /// ```
4284    /// assert_eq!(Vec::from(&[1, 2, 3][..]), vec![1, 2, 3]);
4285    /// ```
4286    fn from(s: &[T]) -> Vec<T> {
4287        s.to_vec()
4288    }
4289}
4290
4291#[cfg(not(no_global_oom_handling))]
4292#[stable(feature = "vec_from_mut", since = "1.19.0")]
4293impl<T: Clone> From<&mut [T]> for Vec<T> {
4294    /// Allocates a `Vec<T>` and fills it by cloning `s`'s items.
4295    ///
4296    /// # Examples
4297    ///
4298    /// ```
4299    /// assert_eq!(Vec::from(&mut [1, 2, 3][..]), vec![1, 2, 3]);
4300    /// ```
4301    fn from(s: &mut [T]) -> Vec<T> {
4302        s.to_vec()
4303    }
4304}
4305
4306#[cfg(not(no_global_oom_handling))]
4307#[stable(feature = "vec_from_array_ref", since = "1.74.0")]
4308impl<T: Clone, const N: usize> From<&[T; N]> for Vec<T> {
4309    /// Allocates a `Vec<T>` and fills it by cloning `s`'s items.
4310    ///
4311    /// # Examples
4312    ///
4313    /// ```
4314    /// assert_eq!(Vec::from(&[1, 2, 3]), vec![1, 2, 3]);
4315    /// ```
4316    fn from(s: &[T; N]) -> Vec<T> {
4317        Self::from(s.as_slice())
4318    }
4319}
4320
4321#[cfg(not(no_global_oom_handling))]
4322#[stable(feature = "vec_from_array_ref", since = "1.74.0")]
4323impl<T: Clone, const N: usize> From<&mut [T; N]> for Vec<T> {
4324    /// Allocates a `Vec<T>` and fills it by cloning `s`'s items.
4325    ///
4326    /// # Examples
4327    ///
4328    /// ```
4329    /// assert_eq!(Vec::from(&mut [1, 2, 3]), vec![1, 2, 3]);
4330    /// ```
4331    fn from(s: &mut [T; N]) -> Vec<T> {
4332        Self::from(s.as_mut_slice())
4333    }
4334}
4335
4336#[cfg(not(no_global_oom_handling))]
4337#[stable(feature = "vec_from_array", since = "1.44.0")]
4338impl<T, const N: usize> From<[T; N]> for Vec<T> {
4339    /// Allocates a `Vec<T>` and moves `s`'s items into it.
4340    ///
4341    /// # Examples
4342    ///
4343    /// ```
4344    /// assert_eq!(Vec::from([1, 2, 3]), vec![1, 2, 3]);
4345    /// ```
4346    fn from(s: [T; N]) -> Vec<T> {
4347        <[T]>::into_vec(Box::new(s))
4348    }
4349}
4350
4351#[stable(feature = "vec_from_cow_slice", since = "1.14.0")]
4352impl<'a, T> From<Cow<'a, [T]>> for Vec<T>
4353where
4354    [T]: ToOwned<Owned = Vec<T>>,
4355{
4356    /// Converts a clone-on-write slice into a vector.
4357    ///
4358    /// If `s` already owns a `Vec<T>`, it will be returned directly.
4359    /// If `s` is borrowing a slice, a new `Vec<T>` will be allocated and
4360    /// filled by cloning `s`'s items into it.
4361    ///
4362    /// # Examples
4363    ///
4364    /// ```
4365    /// # use std::borrow::Cow;
4366    /// let o: Cow<'_, [i32]> = Cow::Owned(vec![1, 2, 3]);
4367    /// let b: Cow<'_, [i32]> = Cow::Borrowed(&[1, 2, 3]);
4368    /// assert_eq!(Vec::from(o), Vec::from(b));
4369    /// ```
4370    fn from(s: Cow<'a, [T]>) -> Vec<T> {
4371        s.into_owned()
4372    }
4373}
4374
4375// note: test pulls in std, which causes errors here
4376#[stable(feature = "vec_from_box", since = "1.18.0")]
4377impl<T, A: Allocator> From<Box<[T], A>> for Vec<T, A> {
4378    /// Converts a boxed slice into a vector by transferring ownership of
4379    /// the existing heap allocation.
4380    ///
4381    /// # Examples
4382    ///
4383    /// ```
4384    /// let b: Box<[i32]> = vec![1, 2, 3].into_boxed_slice();
4385    /// assert_eq!(Vec::from(b), vec![1, 2, 3]);
4386    /// ```
4387    fn from(s: Box<[T], A>) -> Self {
4388        s.into_vec()
4389    }
4390}
4391
4392// note: test pulls in std, which causes errors here
4393#[cfg(not(no_global_oom_handling))]
4394#[stable(feature = "box_from_vec", since = "1.20.0")]
4395impl<T, A: Allocator> From<Vec<T, A>> for Box<[T], A> {
4396    /// Converts a vector into a boxed slice.
4397    ///
4398    /// Before doing the conversion, this method discards excess capacity like [`Vec::shrink_to_fit`].
4399    ///
4400    /// [owned slice]: Box
4401    /// [`Vec::shrink_to_fit`]: Vec::shrink_to_fit
4402    ///
4403    /// # Examples
4404    ///
4405    /// ```
4406    /// assert_eq!(Box::from(vec![1, 2, 3]), vec![1, 2, 3].into_boxed_slice());
4407    /// ```
4408    ///
4409    /// Any excess capacity is removed:
4410    /// ```
4411    /// let mut vec = Vec::with_capacity(10);
4412    /// vec.extend([1, 2, 3]);
4413    ///
4414    /// assert_eq!(Box::from(vec), vec![1, 2, 3].into_boxed_slice());
4415    /// ```
4416    fn from(v: Vec<T, A>) -> Self {
4417        v.into_boxed_slice()
4418    }
4419}
4420
4421#[cfg(not(no_global_oom_handling))]
4422#[stable(feature = "rust1", since = "1.0.0")]
4423impl From<&str> for Vec<u8> {
4424    /// Allocates a `Vec<u8>` and fills it with a UTF-8 string.
4425    ///
4426    /// # Examples
4427    ///
4428    /// ```
4429    /// assert_eq!(Vec::from("123"), vec![b'1', b'2', b'3']);
4430    /// ```
4431    fn from(s: &str) -> Vec<u8> {
4432        From::from(s.as_bytes())
4433    }
4434}
4435
4436#[stable(feature = "array_try_from_vec", since = "1.48.0")]
4437impl<T, A: Allocator, const N: usize> TryFrom<Vec<T, A>> for [T; N] {
4438    type Error = Vec<T, A>;
4439
4440    /// Gets the entire contents of the `Vec<T>` as an array,
4441    /// if its size exactly matches that of the requested array.
4442    ///
4443    /// # Examples
4444    ///
4445    /// ```
4446    /// assert_eq!(vec![1, 2, 3].try_into(), Ok([1, 2, 3]));
4447    /// assert_eq!(<Vec<i32>>::new().try_into(), Ok([]));
4448    /// ```
4449    ///
4450    /// If the length doesn't match, the input comes back in `Err`:
4451    /// ```
4452    /// let r: Result<[i32; 4], _> = (0..10).collect::<Vec<_>>().try_into();
4453    /// assert_eq!(r, Err(vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
4454    /// ```
4455    ///
4456    /// If you're fine with just getting a prefix of the `Vec<T>`,
4457    /// you can call [`.truncate(N)`](Vec::truncate) first.
4458    /// ```
4459    /// let mut v = String::from("hello world").into_bytes();
4460    /// v.sort();
4461    /// v.truncate(2);
4462    /// let [a, b]: [_; 2] = v.try_into().unwrap();
4463    /// assert_eq!(a, b' ');
4464    /// assert_eq!(b, b'd');
4465    /// ```
4466    fn try_from(mut vec: Vec<T, A>) -> Result<[T; N], Vec<T, A>> {
4467        if vec.len() != N {
4468            return Err(vec);
4469        }
4470
4471        // SAFETY: `.set_len(0)` is always sound.
4472        unsafe { vec.set_len(0) };
4473
4474        // SAFETY: A `Vec`'s pointer is always aligned properly, and
4475        // the alignment the array needs is the same as the items.
4476        // We checked earlier that we have sufficient items.
4477        // The items will not double-drop as the `set_len`
4478        // tells the `Vec` not to also drop them.
4479        let array = unsafe { ptr::read(vec.as_ptr() as *const [T; N]) };
4480        Ok(array)
4481    }
4482}
````