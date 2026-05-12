---
title: vector.rs - source
url: https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1084
source: crawler
fetched_at: 2026-05-06T21:30:31.859730093-03:00
rendered_js: false
word_count: 5633
summary: This document describes the Simd<T, N> type in Rust, explaining its use for elementwise parallel operations, its specific alignment constraints, and best practices for safe memory interaction.
tags:
    - simd
    - rust
    - parallel-computing
    - vectorization
    - memory-alignment
    - intrinsic
category: concept
---

## core/portable-simd/crates/core\_simd/src/ vector.rs

````rust
1use core::intrinsics::simd::SimdAlign;
2
3use crate::simd::{
4    Mask, MaskElement,
5    cmp::SimdPartialOrd,
6    num::SimdUint,
7    ptr::{SimdConstPtr, SimdMutPtr},
8};
9
10/// A SIMD vector with the shape of `[T; N]` but the operations of `T`.
11///
12/// `Simd<T, N>` supports the operators (+, *, etc.) that `T` does in "elementwise" fashion.
13/// These take the element at each index from the left-hand side and right-hand side,
14/// perform the operation, then return the result in the same index in a vector of equal size.
15/// However, `Simd` differs from normal iteration and normal arrays:
16/// - `Simd<T, N>` executes `N` operations in a single step with no `break`s
17/// - `Simd<T, N>` can have an alignment greater than `T`, for better mechanical sympathy
18///
19/// By always imposing these constraints on `Simd`, it is easier to compile elementwise operations
20/// into machine instructions that can themselves be executed in parallel.
21///
22/// ```rust
23/// # #![feature(portable_simd)]
24/// # use core::simd::{Simd};
25/// # use core::array;
26/// let a: [i32; 4] = [-2, 0, 2, 4];
27/// let b = [10, 9, 8, 7];
28/// let sum = array::from_fn(|i| a[i] + b[i]);
29/// let prod = array::from_fn(|i| a[i] * b[i]);
30///
31/// // `Simd<T, N>` implements `From<[T; N]>`
32/// let (v, w) = (Simd::from(a), Simd::from(b));
33/// // Which means arrays implement `Into<Simd<T, N>>`.
34/// assert_eq!(v + w, sum.into());
35/// assert_eq!(v * w, prod.into());
36/// ```
37///
38///
39/// `Simd` with integer elements treats operators as wrapping, as if `T` was [`Wrapping<T>`].
40/// Thus, `Simd` does not implement `wrapping_add`, because that is the default behavior.
41/// This means there is no warning on overflows, even in "debug" builds.
42/// For most applications where `Simd` is appropriate, it is "not a bug" to wrap,
43/// and even "debug builds" are unlikely to tolerate the loss of performance.
44/// You may want to consider using explicitly checked arithmetic if such is required.
45/// Division by zero on integers still causes a panic, so
46/// you may want to consider using `f32` or `f64` if that is unacceptable.
47///
48/// [`Wrapping<T>`]: core::num::Wrapping
49///
50/// # Layout
51/// `Simd<T, N>` has a layout similar to `[T; N]` (identical "shapes"), with a greater alignment.
52/// `[T; N]` is aligned to `T`, but `Simd<T, N>` will have an alignment based on both `T` and `N`.
53/// Thus it is sound to [`transmute`] `Simd<T, N>` to `[T; N]` and should optimize to "zero cost",
54/// but the reverse transmutation may require a copy the compiler cannot simply elide.
55///
56/// `N` cannot be 0 and may be at most 64. This limit may be increased in the future.
57///
58/// # ABI "Features"
59/// Due to Rust's safety guarantees, `Simd<T, N>` is currently passed and returned via memory,
60/// not SIMD registers, except as an optimization. Using `#[inline]` on functions that accept
61/// `Simd<T, N>` or return it is recommended, at the cost of code generation time, as
62/// inlining SIMD-using functions can omit a large function prolog or epilog and thus
63/// improve both speed and code size. The need for this may be corrected in the future.
64///
65/// Using `#[inline(always)]` still requires additional care.
66///
67/// # Safe SIMD with Unsafe Rust
68///
69/// Operations with `Simd` are typically safe, but there are many reasons to want to combine SIMD with `unsafe` code.
70/// Care must be taken to respect differences between `Simd` and other types it may be transformed into or derived from.
71/// In particular, the layout of `Simd<T, N>` may be similar to `[T; N]`, and may allow some transmutations,
72/// but references to `[T; N]` are not interchangeable with those to `Simd<T, N>`.
73/// Thus, when using `unsafe` Rust to read and write `Simd<T, N>` through [raw pointers], it is a good idea to first try with
74/// [`read_unaligned`] and [`write_unaligned`]. This is because:
75/// - [`read`] and [`write`] require full alignment (in this case, `Simd<T, N>`'s alignment)
76/// - `Simd<T, N>` is often read from or written to [`[T]`](slice) and other types aligned to `T`
77/// - combining these actions violates the `unsafe` contract and explodes the program into
78///   a puff of **undefined behavior**
79/// - the compiler can implicitly adjust layouts to make unaligned reads or writes fully aligned
80///   if it sees the optimization
81/// - most contemporary processors with "aligned" and "unaligned" read and write instructions
82///   exhibit no performance difference if the "unaligned" variant is aligned at runtime
83///
84/// Less obligations mean unaligned reads and writes are less likely to make the program unsound,
85/// and may be just as fast as stricter alternatives.
86/// When trying to guarantee alignment, [`[T]::as_simd`][as_simd] is an option for
87/// converting `[T]` to `[Simd<T, N>]`, and allows soundly operating on an aligned SIMD body,
88/// but it may cost more time when handling the scalar head and tail.
89/// If these are not enough, it is most ideal to design data structures to be already aligned
90/// to `align_of::<Simd<T, N>>()` before using `unsafe` Rust to read or write.
91/// Other ways to compensate for these facts, like materializing `Simd` to or from an array first,
92/// are handled by safe methods like [`Simd::from_array`] and [`Simd::from_slice`].
93///
94/// [`transmute`]: core::mem::transmute
95/// [raw pointers]: pointer
96/// [`read_unaligned`]: pointer::read_unaligned
97/// [`write_unaligned`]: pointer::write_unaligned
98/// [`read`]: pointer::read
99/// [`write`]: pointer::write
100/// [as_simd]: slice::as_simd
101//
102// NOTE: Accessing the inner array directly in any way (e.g. by using the `.0` field syntax) or
103// directly constructing an instance of the type (i.e. `let vector = Simd(array)`) should be
104// avoided, as it will likely become illegal on `#[repr(simd)]` structs in the future. It also
105// causes rustc to emit illegal LLVM IR in some cases.
106#[repr(simd, packed)]
107#[rustc_simd_monomorphize_lane_limit = "64"]
108pub struct Simd<T, const N: usize>([T; N])
109where
110    T: SimdElement;
111
112impl<T, const N: usize> Simd<T, N>
113where
114    T: SimdElement,
115{
116    /// Number of elements in this vector.
117    pub const LEN: usize = N;
118
119    /// Returns the number of elements in this SIMD vector.
120    ///
121    /// # Examples
122    ///
123    /// ```
124    /// # #![feature(portable_simd)]
125    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
126    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
127    /// # use simd::u32x4;
128    /// let v = u32x4::splat(0);
129    /// assert_eq!(v.len(), 4);
130    /// ```
131    #[inline]
132    #[allow(clippy::len_without_is_empty)]
133    pub const fn len(&self) -> usize {
134        Self::LEN
135    }
136
137    /// Constructs a new SIMD vector with all elements set to the given value.
138    ///
139    /// # Examples
140    ///
141    /// ```
142    /// # #![feature(portable_simd)]
143    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
144    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
145    /// # use simd::u32x4;
146    /// let v = u32x4::splat(8);
147    /// assert_eq!(v.as_array(), &[8, 8, 8, 8]);
148    /// ```
149    #[inline]
150    #[rustc_const_unstable(feature = "portable_simd", issue = "86656")]
151    pub const fn splat(value: T) -> Self {
152        // SAFETY: T is a SimdElement, and the item type of Self.
153        unsafe { core::intrinsics::simd::simd_splat(value) }
154    }
155
156    /// Returns an array reference containing the entire SIMD vector.
157    ///
158    /// # Examples
159    ///
160    /// ```
161    /// # #![feature(portable_simd)]
162    /// # use core::simd::{Simd, u64x4};
163    /// let v: u64x4 = Simd::from_array([0, 1, 2, 3]);
164    /// assert_eq!(v.as_array(), &[0, 1, 2, 3]);
165    /// ```
166    #[inline]
167    pub const fn as_array(&self) -> &[T; N] {
168        // SAFETY: `Simd<T, N>` is just an overaligned `[T; N]` with
169        // potential padding at the end, so pointer casting to a
170        // `&[T; N]` is safe.
171        //
172        // NOTE: This deliberately doesn't just use `&self.0`, see the comment
173        // on the struct definition for details.
174        unsafe { &*(self as *const Self as *const [T; N]) }
175    }
176
177    /// Returns a mutable array reference containing the entire SIMD vector.
178    #[inline]
179    pub const fn as_mut_array(&mut self) -> &mut [T; N] {
180        // SAFETY: `Simd<T, N>` is just an overaligned `[T; N]` with
181        // potential padding at the end, so pointer casting to a
182        // `&mut [T; N]` is safe.
183        //
184        // NOTE: This deliberately doesn't just use `&mut self.0`, see the comment
185        // on the struct definition for details.
186        unsafe { &mut *(self as *mut Self as *mut [T; N]) }
187    }
188
189    /// Loads a vector from an array of `T`.
190    ///
191    /// This function is necessary since `repr(simd)` has padding for non-power-of-2 vectors (at the time of writing).
192    /// With padding, `read_unaligned` will read past the end of an array of N elements.
193    ///
194    /// # Safety
195    /// Reading `ptr` must be safe, as if by `<*const [T; N]>::read`.
196    #[inline]
197    const unsafe fn load(ptr: *const [T; N]) -> Self {
198        // There are potentially simpler ways to write this function, but this should result in
199        // LLVM `load <N x T>`
200
201        let mut tmp = core::mem::MaybeUninit::<Self>::uninit();
202        // SAFETY: `Simd<T, N>` always contains `N` elements of type `T`.  It may have padding
203        // which does not need to be initialized.  The safety of reading `ptr` is ensured by the
204        // caller.
205        unsafe {
206            core::ptr::copy_nonoverlapping(ptr, tmp.as_mut_ptr().cast(), 1);
207            tmp.assume_init()
208        }
209    }
210
211    /// Store a vector to an array of `T`.
212    ///
213    /// See `load` as to why this function is necessary.
214    ///
215    /// # Safety
216    /// Writing to `ptr` must be safe, as if by `<*mut [T; N]>::write`.
217    #[inline]
218    const unsafe fn store(self, ptr: *mut [T; N]) {
219        // There are potentially simpler ways to write this function, but this should result in
220        // LLVM `store <N x T>`
221
222        // Creating a temporary helps LLVM turn the memcpy into a store.
223        let tmp = self;
224        // SAFETY: `Simd<T, N>` always contains `N` elements of type `T`.  The safety of writing
225        // `ptr` is ensured by the caller.
226        unsafe { core::ptr::copy_nonoverlapping(tmp.as_array(), ptr, 1) }
227    }
228
229    /// Converts an array to a SIMD vector.
230    #[inline]
231    pub const fn from_array(array: [T; N]) -> Self {
232        // SAFETY: `&array` is safe to read.
233        //
234        // FIXME: We currently use a pointer load instead of `transmute_copy` because `repr(simd)`
235        // results in padding for non-power-of-2 vectors (so vectors are larger than arrays).
236        //
237        // NOTE: This deliberately doesn't just use `Self(array)`, see the comment
238        // on the struct definition for details.
239        unsafe { Self::load(&array) }
240    }
241
242    /// Converts a SIMD vector to an array.
243    #[inline]
244    pub const fn to_array(self) -> [T; N] {
245        let mut tmp = core::mem::MaybeUninit::uninit();
246        // SAFETY: writing to `tmp` is safe and initializes it.
247        //
248        // FIXME: We currently use a pointer store instead of `transmute_copy` because `repr(simd)`
249        // results in padding for non-power-of-2 vectors (so vectors are larger than arrays).
250        //
251        // NOTE: This deliberately doesn't just use `self.0`, see the comment
252        // on the struct definition for details.
253        unsafe {
254            self.store(tmp.as_mut_ptr());
255            tmp.assume_init()
256        }
257    }
258
259    /// Converts a slice to a SIMD vector containing `slice[..N]`.
260    ///
261    /// # Panics
262    ///
263    /// Panics if the slice's length is less than the vector's `Simd::N`.
264    /// Use `load_or_default` for an alternative that does not panic.
265    ///
266    /// # Example
267    ///
268    /// ```
269    /// # #![feature(portable_simd)]
270    /// # use core::simd::u32x4;
271    /// let source = vec![1, 2, 3, 4, 5, 6];
272    /// let v = u32x4::from_slice(&source);
273    /// assert_eq!(v.as_array(), &[1, 2, 3, 4]);
274    /// ```
275    #[must_use]
276    #[inline]
277    #[track_caller]
278    pub const fn from_slice(slice: &[T]) -> Self {
279        assert!(
280            slice.len() >= Self::LEN,
281            "slice length must be at least the number of elements"
282        );
283        // SAFETY: We just checked that the slice contains
284        // at least `N` elements.
285        unsafe { Self::load(slice.as_ptr().cast()) }
286    }
287
288    /// Writes a SIMD vector to the first `N` elements of a slice.
289    ///
290    /// # Panics
291    ///
292    /// Panics if the slice's length is less than the vector's `Simd::N`.
293    ///
294    /// # Example
295    ///
296    /// ```
297    /// # #![feature(portable_simd)]
298    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
299    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
300    /// # use simd::u32x4;
301    /// let mut dest = vec![0; 6];
302    /// let v = u32x4::from_array([1, 2, 3, 4]);
303    /// v.copy_to_slice(&mut dest);
304    /// assert_eq!(&dest, &[1, 2, 3, 4, 0, 0]);
305    /// ```
306    #[inline]
307    #[track_caller]
308    pub const fn copy_to_slice(self, slice: &mut [T]) {
309        assert!(
310            slice.len() >= Self::LEN,
311            "slice length must be at least the number of elements"
312        );
313        // SAFETY: We just checked that the slice contains
314        // at least `N` elements.
315        unsafe { self.store(slice.as_mut_ptr().cast()) }
316    }
317
318    /// Reads contiguous elements from `slice`. Elements are read so long as they're in-bounds for
319    /// the `slice`. Otherwise, the default value for the element type is returned.
320    ///
321    /// # Examples
322    /// ```
323    /// # #![feature(portable_simd)]
324    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
325    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
326    /// # use simd::Simd;
327    /// let vec: Vec<i32> = vec![10, 11];
328    ///
329    /// let result = Simd::<i32, 4>::load_or_default(&vec);
330    /// assert_eq!(result, Simd::from_array([10, 11, 0, 0]));
331    /// ```
332    #[must_use]
333    #[inline]
334    pub fn load_or_default(slice: &[T]) -> Self
335    where
336        T: Default,
337    {
338        Self::load_or(slice, Default::default())
339    }
340
341    /// Reads contiguous elements from `slice`. Elements are read so long as they're in-bounds for
342    /// the `slice`. Otherwise, the corresponding value from `or` is passed through.
343    ///
344    /// # Examples
345    /// ```
346    /// # #![feature(portable_simd)]
347    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
348    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
349    /// # use simd::Simd;
350    /// let vec: Vec<i32> = vec![10, 11];
351    /// let or = Simd::from_array([-5, -4, -3, -2]);
352    ///
353    /// let result = Simd::load_or(&vec, or);
354    /// assert_eq!(result, Simd::from_array([10, 11, -3, -2]));
355    /// ```
356    #[must_use]
357    #[inline]
358    pub fn load_or(slice: &[T], or: Self) -> Self {
359        Self::load_select(slice, Mask::splat(true), or)
360    }
361
362    /// Reads contiguous elements from `slice`. Each element is read from memory if its
363    /// corresponding element in `enable` is `true`.
364    ///
365    /// When the element is disabled or out of bounds for the slice, that memory location
366    /// is not accessed and the corresponding value from `or` is passed through.
367    ///
368    /// # Examples
369    /// ```
370    /// # #![feature(portable_simd)]
371    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
372    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
373    /// # use simd::{Simd, Mask};
374    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
375    /// let enable = Mask::from_array([true, true, false, true]);
376    /// let or = Simd::from_array([-5, -4, -3, -2]);
377    ///
378    /// let result = Simd::load_select(&vec, enable, or);
379    /// assert_eq!(result, Simd::from_array([10, 11, -3, 13]));
380    /// ```
381    #[must_use]
382    #[inline]
383    pub fn load_select_or_default(slice: &[T], enable: Mask<<T as SimdElement>::Mask, N>) -> Self
384    where
385        T: Default,
386    {
387        Self::load_select(slice, enable, Default::default())
388    }
389
390    /// Reads contiguous elements from `slice`. Each element is read from memory if its
391    /// corresponding element in `enable` is `true`.
392    ///
393    /// When the element is disabled or out of bounds for the slice, that memory location
394    /// is not accessed and the corresponding value from `or` is passed through.
395    ///
396    /// # Examples
397    /// ```
398    /// # #![feature(portable_simd)]
399    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
400    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
401    /// # use simd::{Simd, Mask};
402    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
403    /// let enable = Mask::from_array([true, true, false, true]);
404    /// let or = Simd::from_array([-5, -4, -3, -2]);
405    ///
406    /// let result = Simd::load_select(&vec, enable, or);
407    /// assert_eq!(result, Simd::from_array([10, 11, -3, 13]));
408    /// ```
409    #[must_use]
410    #[inline]
411    pub fn load_select(
412        slice: &[T],
413        mut enable: Mask<<T as SimdElement>::Mask, N>,
414        or: Self,
415    ) -> Self {
416        enable &= mask_up_to(slice.len());
417        // SAFETY: We performed the bounds check by updating the mask. &[T] is properly aligned to
418        // the element.
419        unsafe { Self::load_select_ptr(slice.as_ptr(), enable, or) }
420    }
421
422    /// Reads contiguous elements from `slice`. Each element is read from memory if its
423    /// corresponding element in `enable` is `true`.
424    ///
425    /// When the element is disabled, that memory location is not accessed and the corresponding
426    /// value from `or` is passed through.
427    ///
428    /// # Safety
429    /// Enabled loads must not exceed the length of `slice`.
430    #[must_use]
431    #[inline]
432    pub unsafe fn load_select_unchecked(
433        slice: &[T],
434        enable: Mask<<T as SimdElement>::Mask, N>,
435        or: Self,
436    ) -> Self {
437        let ptr = slice.as_ptr();
438        // SAFETY: The safety of reading elements from `slice` is ensured by the caller.
439        unsafe { Self::load_select_ptr(ptr, enable, or) }
440    }
441
442    /// Reads contiguous elements starting at `ptr`. Each element is read from memory if its
443    /// corresponding element in `enable` is `true`.
444    ///
445    /// When the element is disabled, that memory location is not accessed and the corresponding
446    /// value from `or` is passed through.
447    ///
448    /// # Safety
449    /// Enabled `ptr` elements must be safe to read as if by `core::ptr::read`.
450    #[must_use]
451    #[inline]
452    pub unsafe fn load_select_ptr(
453        ptr: *const T,
454        enable: Mask<<T as SimdElement>::Mask, N>,
455        or: Self,
456    ) -> Self {
457        // SAFETY: The safety of reading elements through `ptr` is ensured by the caller.
458        unsafe {
459            core::intrinsics::simd::simd_masked_load::<_, _, _, { SimdAlign::Element }>(
460                enable.to_simd(),
461                ptr,
462                or,
463            )
464        }
465    }
466
467    /// Reads from potentially discontiguous indices in `slice` to construct a SIMD vector.
468    /// If an index is out-of-bounds, the element is instead selected from the `or` vector.
469    ///
470    /// # Examples
471    /// ```
472    /// # #![feature(portable_simd)]
473    /// # use core::simd::Simd;
474    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
475    /// let idxs = Simd::from_array([9, 3, 0, 5]);  // Note the index that is out-of-bounds
476    /// let alt = Simd::from_array([-5, -4, -3, -2]);
477    ///
478    /// let result = Simd::gather_or(&vec, idxs, alt);
479    /// assert_eq!(result, Simd::from_array([-5, 13, 10, 15]));
480    /// ```
481    #[must_use]
482    #[inline]
483    pub fn gather_or(slice: &[T], idxs: Simd<usize, N>, or: Self) -> Self {
484        Self::gather_select(slice, Mask::splat(true), idxs, or)
485    }
486
487    /// Reads from indices in `slice` to construct a SIMD vector.
488    /// If an index is out-of-bounds, the element is set to the default given by `T: Default`.
489    ///
490    /// # Examples
491    /// ```
492    /// # #![feature(portable_simd)]
493    /// # use core::simd::Simd;
494    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
495    /// let idxs = Simd::from_array([9, 3, 0, 5]);  // Note the index that is out-of-bounds
496    ///
497    /// let result = Simd::gather_or_default(&vec, idxs);
498    /// assert_eq!(result, Simd::from_array([0, 13, 10, 15]));
499    /// ```
500    #[must_use]
501    #[inline]
502    pub fn gather_or_default(slice: &[T], idxs: Simd<usize, N>) -> Self
503    where
504        T: Default,
505    {
506        Self::gather_or(slice, idxs, Self::splat(T::default()))
507    }
508
509    /// Reads from indices in `slice` to construct a SIMD vector.
510    /// The mask `enable`s all `true` indices and disables all `false` indices.
511    /// If an index is disabled or is out-of-bounds, the element is selected from the `or` vector.
512    ///
513    /// # Examples
514    /// ```
515    /// # #![feature(portable_simd)]
516    /// # use core::simd::{Simd, Mask};
517    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
518    /// let idxs = Simd::from_array([9, 3, 0, 5]); // Includes an out-of-bounds index
519    /// let alt = Simd::from_array([-5, -4, -3, -2]);
520    /// let enable = Mask::from_array([true, true, true, false]); // Includes a masked element
521    ///
522    /// let result = Simd::gather_select(&vec, enable, idxs, alt);
523    /// assert_eq!(result, Simd::from_array([-5, 13, 10, -2]));
524    /// ```
525    #[must_use]
526    #[inline]
527    pub fn gather_select(
528        slice: &[T],
529        enable: Mask<isize, N>,
530        idxs: Simd<usize, N>,
531        or: Self,
532    ) -> Self {
533        let enable: Mask<isize, N> = enable & idxs.simd_lt(Simd::splat(slice.len()));
534        // Safety: We have masked-off out-of-bounds indices.
535        unsafe { Self::gather_select_unchecked(slice, enable, idxs, or) }
536    }
537
538    /// Reads from indices in `slice` to construct a SIMD vector.
539    /// The mask `enable`s all `true` indices and disables all `false` indices.
540    /// If an index is disabled, the element is selected from the `or` vector.
541    ///
542    /// # Safety
543    ///
544    /// Calling this function with an `enable`d out-of-bounds index is *[undefined behavior]*
545    /// even if the resulting value is not used.
546    ///
547    /// # Examples
548    /// ```
549    /// # #![feature(portable_simd)]
550    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
551    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
552    /// # use simd::{Simd, cmp::SimdPartialOrd, Mask};
553    /// let vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
554    /// let idxs = Simd::from_array([9, 3, 0, 5]); // Includes an out-of-bounds index
555    /// let alt = Simd::from_array([-5, -4, -3, -2]);
556    /// let enable = Mask::from_array([true, true, true, false]); // Includes a masked element
557    /// // If this mask was used to gather, it would be unsound. Let's fix that.
558    /// let enable = enable & idxs.simd_lt(Simd::splat(vec.len()));
559    ///
560    /// // The out-of-bounds index has been masked, so it's safe to gather now.
561    /// let result = unsafe { Simd::gather_select_unchecked(&vec, enable, idxs, alt) };
562    /// assert_eq!(result, Simd::from_array([-5, 13, 10, -2]));
563    /// ```
564    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
565    #[must_use]
566    #[inline]
567    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
568    pub unsafe fn gather_select_unchecked(
569        slice: &[T],
570        enable: Mask<isize, N>,
571        idxs: Simd<usize, N>,
572        or: Self,
573    ) -> Self {
574        let base_ptr = Simd::<*const T, N>::splat(slice.as_ptr());
575        // Ferris forgive me, I have done pointer arithmetic here.
576        let ptrs = base_ptr.wrapping_add(idxs);
577        // Safety: The caller is responsible for determining the indices are okay to read
578        unsafe { Self::gather_select_ptr(ptrs, enable, or) }
579    }
580
581    /// Reads elementwise from pointers into a SIMD vector.
582    ///
583    /// # Safety
584    ///
585    /// Each read must satisfy the same conditions as [`core::ptr::read`].
586    ///
587    /// # Example
588    /// ```
589    /// # #![feature(portable_simd)]
590    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
591    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
592    /// # use simd::prelude::*;
593    /// let values = [6, 2, 4, 9];
594    /// let offsets = Simd::from_array([1, 0, 0, 3]);
595    /// let source = Simd::splat(values.as_ptr()).wrapping_add(offsets);
596    /// let gathered = unsafe { Simd::gather_ptr(source) };
597    /// assert_eq!(gathered, Simd::from_array([2, 6, 6, 9]));
598    /// ```
599    #[must_use]
600    #[inline]
601    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
602    pub unsafe fn gather_ptr(source: Simd<*const T, N>) -> Self
603    where
604        T: Default,
605    {
606        // TODO: add an intrinsic that doesn't use a passthru vector, and remove the T: Default bound
607        // Safety: The caller is responsible for upholding all invariants
608        unsafe { Self::gather_select_ptr(source, Mask::splat(true), Self::default()) }
609    }
610
611    /// Conditionally read elementwise from pointers into a SIMD vector.
612    /// The mask `enable`s all `true` pointers and disables all `false` pointers.
613    /// If a pointer is disabled, the element is selected from the `or` vector,
614    /// and no read is performed.
615    ///
616    /// # Safety
617    ///
618    /// Enabled elements must satisfy the same conditions as [`core::ptr::read`].
619    ///
620    /// # Example
621    /// ```
622    /// # #![feature(portable_simd)]
623    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
624    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
625    /// # use simd::prelude::*;
626    /// let values = [6, 2, 4, 9];
627    /// let enable = Mask::from_array([true, true, false, true]);
628    /// let offsets = Simd::from_array([1, 0, 0, 3]);
629    /// let source = Simd::splat(values.as_ptr()).wrapping_add(offsets);
630    /// let gathered = unsafe { Simd::gather_select_ptr(source, enable, Simd::splat(0)) };
631    /// assert_eq!(gathered, Simd::from_array([2, 6, 0, 9]));
632    /// ```
633    #[must_use]
634    #[inline]
635    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
636    pub unsafe fn gather_select_ptr(
637        source: Simd<*const T, N>,
638        enable: Mask<isize, N>,
639        or: Self,
640    ) -> Self {
641        // Safety: The caller is responsible for upholding all invariants
642        unsafe { core::intrinsics::simd::simd_gather(or, source, enable.to_simd()) }
643    }
644
645    /// Conditionally write contiguous elements to `slice`. The `enable` mask controls
646    /// which elements are written, as long as they're in-bounds of the `slice`.
647    /// If the element is disabled or out of bounds, no memory access to that location
648    /// is made.
649    ///
650    /// # Examples
651    /// ```
652    /// # #![feature(portable_simd)]
653    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
654    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
655    /// # use simd::{Simd, Mask};
656    /// let mut arr = [0i32; 4];
657    /// let write = Simd::from_array([-5, -4, -3, -2]);
658    /// let enable = Mask::from_array([false, true, true, true]);
659    ///
660    /// write.store_select(&mut arr[..3], enable);
661    /// assert_eq!(arr, [0, -4, -3, 0]);
662    /// ```
663    #[inline]
664    pub fn store_select(self, slice: &mut [T], mut enable: Mask<<T as SimdElement>::Mask, N>) {
665        enable &= mask_up_to(slice.len());
666        // SAFETY: We performed the bounds check by updating the mask. &[T] is properly aligned to
667        // the element.
668        unsafe { self.store_select_ptr(slice.as_mut_ptr(), enable) }
669    }
670
671    /// Conditionally write contiguous elements to `slice`. The `enable` mask controls
672    /// which elements are written.
673    ///
674    /// # Safety
675    ///
676    /// Every enabled element must be in bounds for the `slice`.
677    ///
678    /// # Examples
679    /// ```
680    /// # #![feature(portable_simd)]
681    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
682    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
683    /// # use simd::{Simd, Mask};
684    /// let mut arr = [0i32; 4];
685    /// let write = Simd::from_array([-5, -4, -3, -2]);
686    /// let enable = Mask::from_array([false, true, true, true]);
687    ///
688    /// unsafe { write.store_select_unchecked(&mut arr, enable) };
689    /// assert_eq!(arr, [0, -4, -3, -2]);
690    /// ```
691    #[inline]
692    pub unsafe fn store_select_unchecked(
693        self,
694        slice: &mut [T],
695        enable: Mask<<T as SimdElement>::Mask, N>,
696    ) {
697        let ptr = slice.as_mut_ptr();
698        // SAFETY: The safety of writing elements in `slice` is ensured by the caller.
699        unsafe { self.store_select_ptr(ptr, enable) }
700    }
701
702    /// Conditionally write contiguous elements starting from `ptr`.
703    /// The `enable` mask controls which elements are written.
704    /// When disabled, the memory location corresponding to that element is not accessed.
705    ///
706    /// # Safety
707    ///
708    /// Memory addresses for element are calculated [`pointer::wrapping_offset`] and
709    /// each enabled element must satisfy the same conditions as [`core::ptr::write`].
710    #[inline]
711    pub unsafe fn store_select_ptr(self, ptr: *mut T, enable: Mask<<T as SimdElement>::Mask, N>) {
712        // SAFETY: The safety of writing elements through `ptr` is ensured by the caller.
713        unsafe {
714            core::intrinsics::simd::simd_masked_store::<_, _, _, { SimdAlign::Element }>(
715                enable.to_simd(),
716                ptr,
717                self,
718            )
719        }
720    }
721
722    /// Writes the values in a SIMD vector to potentially discontiguous indices in `slice`.
723    /// If an index is out-of-bounds, the write is suppressed without panicking.
724    /// If two elements in the scattered vector would write to the same index
725    /// only the last element is guaranteed to actually be written.
726    ///
727    /// # Examples
728    /// ```
729    /// # #![feature(portable_simd)]
730    /// # use core::simd::Simd;
731    /// let mut vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
732    /// let idxs = Simd::from_array([9, 3, 0, 0]); // Note the duplicate index.
733    /// let vals = Simd::from_array([-27, 82, -41, 124]);
734    ///
735    /// vals.scatter(&mut vec, idxs); // two logical writes means the last wins.
736    /// assert_eq!(vec, vec![124, 11, 12, 82, 14, 15, 16, 17, 18]);
737    /// ```
738    #[inline]
739    pub fn scatter(self, slice: &mut [T], idxs: Simd<usize, N>) {
740        self.scatter_select(slice, Mask::splat(true), idxs)
741    }
742
743    /// Writes values from a SIMD vector to multiple potentially discontiguous indices in `slice`.
744    /// The mask `enable`s all `true` indices and disables all `false` indices.
745    /// If an enabled index is out-of-bounds, the write is suppressed without panicking.
746    /// If two enabled elements in the scattered vector would write to the same index,
747    /// only the last element is guaranteed to actually be written.
748    ///
749    /// # Examples
750    /// ```
751    /// # #![feature(portable_simd)]
752    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
753    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
754    /// # use simd::{Simd, Mask};
755    /// let mut vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
756    /// let idxs = Simd::from_array([9, 3, 0, 0]); // Includes an out-of-bounds index
757    /// let vals = Simd::from_array([-27, 82, -41, 124]);
758    /// let enable = Mask::from_array([true, true, true, false]); // Includes a masked element
759    ///
760    /// vals.scatter_select(&mut vec, enable, idxs); // The last write is masked, thus omitted.
761    /// assert_eq!(vec, vec![-41, 11, 12, 82, 14, 15, 16, 17, 18]);
762    /// ```
763    #[inline]
764    pub fn scatter_select(self, slice: &mut [T], enable: Mask<isize, N>, idxs: Simd<usize, N>) {
765        let enable: Mask<isize, N> = enable & idxs.simd_lt(Simd::splat(slice.len()));
766        // Safety: We have masked-off out-of-bounds indices.
767        unsafe { self.scatter_select_unchecked(slice, enable, idxs) }
768    }
769
770    /// Writes values from a SIMD vector to multiple potentially discontiguous indices in `slice`.
771    /// The mask `enable`s all `true` indices and disables all `false` indices.
772    /// If two enabled elements in the scattered vector would write to the same index,
773    /// only the last element is guaranteed to actually be written.
774    ///
775    /// # Safety
776    ///
777    /// Calling this function with an enabled out-of-bounds index is *[undefined behavior]*,
778    /// and may lead to memory corruption.
779    ///
780    /// # Examples
781    /// ```
782    /// # #![feature(portable_simd)]
783    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
784    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
785    /// # use simd::{Simd, cmp::SimdPartialOrd, Mask};
786    /// let mut vec: Vec<i32> = vec![10, 11, 12, 13, 14, 15, 16, 17, 18];
787    /// let idxs = Simd::from_array([9, 3, 0, 0]);
788    /// let vals = Simd::from_array([-27, 82, -41, 124]);
789    /// let enable = Mask::from_array([true, true, true, false]); // Masks the final index
790    /// // If this mask was used to scatter, it would be unsound. Let's fix that.
791    /// let enable = enable & idxs.simd_lt(Simd::splat(vec.len()));
792    ///
793    /// // We have masked the OOB index, so it's safe to scatter now.
794    /// unsafe { vals.scatter_select_unchecked(&mut vec, enable, idxs); }
795    /// // The second write to index 0 was masked, thus omitted.
796    /// assert_eq!(vec, vec![-41, 11, 12, 82, 14, 15, 16, 17, 18]);
797    /// ```
798    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
799    #[inline]
800    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
801    pub unsafe fn scatter_select_unchecked(
802        self,
803        slice: &mut [T],
804        enable: Mask<isize, N>,
805        idxs: Simd<usize, N>,
806    ) {
807        // Safety: This block works with *mut T derived from &mut 'a [T],
808        // which means it is delicate in Rust's borrowing model, circa 2021:
809        // &mut 'a [T] asserts uniqueness, so deriving &'a [T] invalidates live *mut Ts!
810        // Even though this block is largely safe methods, it must be exactly this way
811        // to prevent invalidating the raw ptrs while they're live.
812        // Thus, entering this block requires all values to use being already ready:
813        // 0. idxs we want to write to, which are used to construct the mask.
814        // 1. enable, which depends on an initial &'a [T] and the idxs.
815        // 2. actual values to scatter (self).
816        // 3. &mut [T] which will become our base ptr.
817        unsafe {
818            // Now Entering ☢️ *mut T Zone
819            let base_ptr = Simd::<*mut T, N>::splat(slice.as_mut_ptr());
820            // Ferris forgive me, I have done pointer arithmetic here.
821            let ptrs = base_ptr.wrapping_add(idxs);
822            // The ptrs have been bounds-masked to prevent memory-unsafe writes insha'allah
823            self.scatter_select_ptr(ptrs, enable);
824            // Cleared ☢️ *mut T Zone
825        }
826    }
827
828    /// Writes pointers elementwise into a SIMD vector.
829    ///
830    /// # Safety
831    ///
832    /// Each write must satisfy the same conditions as [`core::ptr::write`].
833    ///
834    /// # Example
835    /// ```
836    /// # #![feature(portable_simd)]
837    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
838    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
839    /// # use simd::{Simd, ptr::SimdMutPtr};
840    /// let mut values = [0; 4];
841    /// let offset = Simd::from_array([3, 2, 1, 0]);
842    /// let ptrs = Simd::splat(values.as_mut_ptr()).wrapping_add(offset);
843    /// unsafe { Simd::from_array([6, 3, 5, 7]).scatter_ptr(ptrs); }
844    /// assert_eq!(values, [7, 5, 3, 6]);
845    /// ```
846    #[inline]
847    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
848    pub unsafe fn scatter_ptr(self, dest: Simd<*mut T, N>) {
849        // Safety: The caller is responsible for upholding all invariants
850        unsafe { self.scatter_select_ptr(dest, Mask::splat(true)) }
851    }
852
853    /// Conditionally write pointers elementwise into a SIMD vector.
854    /// The mask `enable`s all `true` pointers and disables all `false` pointers.
855    /// If a pointer is disabled, the write to its pointee is skipped.
856    ///
857    /// # Safety
858    ///
859    /// Enabled pointers must satisfy the same conditions as [`core::ptr::write`].
860    ///
861    /// # Example
862    /// ```
863    /// # #![feature(portable_simd)]
864    /// # #[cfg(feature = "as_crate")] use core_simd::simd;
865    /// # #[cfg(not(feature = "as_crate"))] use core::simd;
866    /// # use simd::{Mask, Simd, ptr::SimdMutPtr};
867    /// let mut values = [0; 4];
868    /// let offset = Simd::from_array([3, 2, 1, 0]);
869    /// let ptrs = Simd::splat(values.as_mut_ptr()).wrapping_add(offset);
870    /// let enable = Mask::from_array([true, true, false, false]);
871    /// unsafe { Simd::from_array([6, 3, 5, 7]).scatter_select_ptr(ptrs, enable); }
872    /// assert_eq!(values, [0, 0, 3, 6]);
873    /// ```
874    #[inline]
875    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
876    pub unsafe fn scatter_select_ptr(self, dest: Simd<*mut T, N>, enable: Mask<isize, N>) {
877        // Safety: The caller is responsible for upholding all invariants
878        unsafe { core::intrinsics::simd::simd_scatter(self, dest, enable.to_simd()) }
879    }
880}
881
882impl<T, const N: usize> Copy for Simd<T, N> where T: SimdElement {}
883
884impl<T, const N: usize> Clone for Simd<T, N>
885where
886    T: SimdElement,
887{
888    #[inline]
889    fn clone(&self) -> Self {
890        *self
891    }
892}
893
894impl<T, const N: usize> Default for Simd<T, N>
895where
896    T: SimdElement + Default,
897{
898    #[inline]
899    fn default() -> Self {
900        Self::splat(T::default())
901    }
902}
903
904impl<T, const N: usize> PartialEq for Simd<T, N>
905where
906    T: SimdElement + PartialEq,
907{
908    #[inline]
909    fn eq(&self, other: &Self) -> bool {
910        // Safety: All SIMD vectors are SimdPartialEq, and the comparison produces a valid mask.
911        let mask = unsafe {
912            let tfvec: Simd<<T as SimdElement>::Mask, N> =
913                core::intrinsics::simd::simd_eq(*self, *other);
914            Mask::from_simd_unchecked(tfvec)
915        };
916
917        // Two vectors are equal if all elements are equal when compared elementwise
918        mask.all()
919    }
920
921    #[allow(clippy::partialeq_ne_impl)]
922    #[inline]
923    fn ne(&self, other: &Self) -> bool {
924        // Safety: All SIMD vectors are SimdPartialEq, and the comparison produces a valid mask.
925        let mask = unsafe {
926            let tfvec: Simd<<T as SimdElement>::Mask, N> =
927                core::intrinsics::simd::simd_ne(*self, *other);
928            Mask::from_simd_unchecked(tfvec)
929        };
930
931        // Two vectors are non-equal if any elements are non-equal when compared elementwise
932        mask.any()
933    }
934}
935
936/// Lexicographic order. For the SIMD elementwise minimum and maximum, use simd_min and simd_max instead.
937impl<T, const N: usize> PartialOrd for Simd<T, N>
938where
939    T: SimdElement + PartialOrd,
940{
941    #[inline]
942    fn partial_cmp(&self, other: &Self) -> Option<core::cmp::Ordering> {
943        // TODO use SIMD equality
944        self.to_array().partial_cmp(other.as_ref())
945    }
946}
947
948impl<T, const N: usize> Eq for Simd<T, N> where T: SimdElement + Eq {}
949
950/// Lexicographic order. For the SIMD elementwise minimum and maximum, use simd_min and simd_max instead.
951impl<T, const N: usize> Ord for Simd<T, N>
952where
953    T: SimdElement + Ord,
954{
955    #[inline]
956    fn cmp(&self, other: &Self) -> core::cmp::Ordering {
957        // TODO use SIMD equality
958        self.to_array().cmp(other.as_ref())
959    }
960}
961
962impl<T, const N: usize> core::hash::Hash for Simd<T, N>
963where
964    T: SimdElement + core::hash::Hash,
965{
966    #[inline]
967    fn hash<H>(&self, state: &mut H)
968    where
969        H: core::hash::Hasher,
970    {
971        self.as_array().hash(state)
972    }
973}
974
975// array references
976impl<T, const N: usize> AsRef<[T; N]> for Simd<T, N>
977where
978    T: SimdElement,
979{
980    #[inline]
981    fn as_ref(&self) -> &[T; N] {
982        self.as_array()
983    }
984}
985
986impl<T, const N: usize> AsMut<[T; N]> for Simd<T, N>
987where
988    T: SimdElement,
989{
990    #[inline]
991    fn as_mut(&mut self) -> &mut [T; N] {
992        self.as_mut_array()
993    }
994}
995
996// slice references
997impl<T, const N: usize> AsRef<[T]> for Simd<T, N>
998where
999    T: SimdElement,
1000{
1001    #[inline]
1002    fn as_ref(&self) -> &[T] {
1003        self.as_array()
1004    }
1005}
1006
1007impl<T, const N: usize> AsMut<[T]> for Simd<T, N>
1008where
1009    T: SimdElement,
1010{
1011    #[inline]
1012    fn as_mut(&mut self) -> &mut [T] {
1013        self.as_mut_array()
1014    }
1015}
1016
1017// vector/array conversion
1018impl<T, const N: usize> From<[T; N]> for Simd<T, N>
1019where
1020    T: SimdElement,
1021{
1022    #[inline]
1023    fn from(array: [T; N]) -> Self {
1024        Self::from_array(array)
1025    }
1026}
1027
1028impl<T, const N: usize> From<Simd<T, N>> for [T; N]
1029where
1030    T: SimdElement,
1031{
1032    #[inline]
1033    fn from(vector: Simd<T, N>) -> Self {
1034        vector.to_array()
1035    }
1036}
1037
1038impl<T, const N: usize> TryFrom<&[T]> for Simd<T, N>
1039where
1040    T: SimdElement,
1041{
1042    type Error = core::array::TryFromSliceError;
1043
1044    #[inline]
1045    fn try_from(slice: &[T]) -> Result<Self, core::array::TryFromSliceError> {
1046        Ok(Self::from_array(slice.try_into()?))
1047    }
1048}
1049
1050impl<T, const N: usize> TryFrom<&mut [T]> for Simd<T, N>
1051where
1052    T: SimdElement,
1053{
1054    type Error = core::array::TryFromSliceError;
1055
1056    #[inline]
1057    fn try_from(slice: &mut [T]) -> Result<Self, core::array::TryFromSliceError> {
1058        Ok(Self::from_array(slice.try_into()?))
1059    }
1060}
1061
1062mod sealed {
1063    pub trait Sealed {}
1064}
1065use sealed::Sealed;
1066
1067/// Marker trait for types that may be used as SIMD vector elements.
1068///
1069/// # Safety
1070/// This trait, when implemented, asserts the compiler can monomorphize
1071/// `#[repr(simd)]` structs with the marked type as an element.
1072/// Strictly, it is valid to impl if the vector will not be miscompiled.
1073/// Practically, it is user-unfriendly to impl it if the vector won't compile,
1074/// even when no soundness guarantees are broken by allowing the user to try.
1075pub unsafe trait SimdElement: Sealed + Copy {
1076    /// The mask element type corresponding to this element type.
1077    type Mask: MaskElement;
1078}
1079
1080impl Sealed for u8 {}
1081
1082// Safety: u8 is a valid SIMD element type, and is supported by this API
1083unsafe impl SimdElement for u8 {
1084    type Mask = i8;
1085}
1086
1087impl Sealed for u16 {}
1088
1089// Safety: u16 is a valid SIMD element type, and is supported by this API
1090unsafe impl SimdElement for u16 {
1091    type Mask = i16;
1092}
1093
1094impl Sealed for u32 {}
1095
1096// Safety: u32 is a valid SIMD element type, and is supported by this API
1097unsafe impl SimdElement for u32 {
1098    type Mask = i32;
1099}
1100
1101impl Sealed for u64 {}
1102
1103// Safety: u64 is a valid SIMD element type, and is supported by this API
1104unsafe impl SimdElement for u64 {
1105    type Mask = i64;
1106}
1107
1108impl Sealed for usize {}
1109
1110// Safety: usize is a valid SIMD element type, and is supported by this API
1111unsafe impl SimdElement for usize {
1112    type Mask = isize;
1113}
1114
1115impl Sealed for i8 {}
1116
1117// Safety: i8 is a valid SIMD element type, and is supported by this API
1118unsafe impl SimdElement for i8 {
1119    type Mask = i8;
1120}
1121
1122impl Sealed for i16 {}
1123
1124// Safety: i16 is a valid SIMD element type, and is supported by this API
1125unsafe impl SimdElement for i16 {
1126    type Mask = i16;
1127}
1128
1129impl Sealed for i32 {}
1130
1131// Safety: i32 is a valid SIMD element type, and is supported by this API
1132unsafe impl SimdElement for i32 {
1133    type Mask = i32;
1134}
1135
1136impl Sealed for i64 {}
1137
1138// Safety: i64 is a valid SIMD element type, and is supported by this API
1139unsafe impl SimdElement for i64 {
1140    type Mask = i64;
1141}
1142
1143impl Sealed for isize {}
1144
1145// Safety: isize is a valid SIMD element type, and is supported by this API
1146unsafe impl SimdElement for isize {
1147    type Mask = isize;
1148}
1149
1150impl Sealed for f32 {}
1151
1152// Safety: f32 is a valid SIMD element type, and is supported by this API
1153unsafe impl SimdElement for f32 {
1154    type Mask = i32;
1155}
1156
1157impl Sealed for f64 {}
1158
1159// Safety: f64 is a valid SIMD element type, and is supported by this API
1160unsafe impl SimdElement for f64 {
1161    type Mask = i64;
1162}
1163
1164impl<T> Sealed for *const T {}
1165
1166// Safety: (thin) const pointers are valid SIMD element types, and are supported by this API
1167//
1168// Fat pointers may be supported in the future.
1169unsafe impl<T> SimdElement for *const T
1170where
1171    T: core::ptr::Pointee<Metadata = ()>,
1172{
1173    type Mask = isize;
1174}
1175
1176impl<T> Sealed for *mut T {}
1177
1178// Safety: (thin) mut pointers are valid SIMD element types, and are supported by this API
1179//
1180// Fat pointers may be supported in the future.
1181unsafe impl<T> SimdElement for *mut T
1182where
1183    T: core::ptr::Pointee<Metadata = ()>,
1184{
1185    type Mask = isize;
1186}
1187
1188#[inline]
1189fn lane_indices<const N: usize>() -> Simd<usize, N> {
1190    #![allow(clippy::needless_range_loop)]
1191    let mut index = [0; N];
1192    for i in 0..N {
1193        index[i] = i;
1194    }
1195    Simd::from_array(index)
1196}
1197
1198#[inline]
1199fn mask_up_to<M, const N: usize>(len: usize) -> Mask<M, N>
1200where
1201    M: MaskElement,
1202{
1203    let index = lane_indices::<N>();
1204    let max_value: u64 = M::max_unsigned();
1205    macro_rules! case {
1206        ($ty:ty) => {
1207            if N < <$ty>::MAX as usize && max_value as $ty as u64 == max_value {
1208                return index.cast().simd_lt(Simd::splat(len.min(N) as $ty)).cast();
1209            }
1210        };
1211    }
1212    case!(u8);
1213    case!(u16);
1214    case!(u32);
1215    case!(u64);
1216    index.simd_lt(Simd::splat(len)).cast()
1217}
````