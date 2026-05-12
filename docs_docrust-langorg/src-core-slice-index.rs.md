---
title: index.rs - source
url: https://doc.rust-lang.org/src/core/slice/index.rs.html#463
source: crawler
fetched_at: 2026-05-06T21:38:38.091329856-03:00
rendered_js: false
word_count: 5001
summary: This document defines the core indexing logic for Rust slices, including the `SliceIndex` trait that enables both safe and unchecked element access.
tags:
    - rust
    - slice
    - indexing
    - trait
    - memory-safety
    - bounds-checking
category: api
---

## core/slice/ index.rs

````rust
1//! Indexing implementations for `[T]`.
2
3use crate::intrinsics::slice_get_unchecked;
4use crate::marker::Destruct;
5use crate::panic::const_panic;
6use crate::ub_checks::assert_unsafe_precondition;
7use crate::{ops, range};
8
9#[stable(feature = "rust1", since = "1.0.0")]
10#[rustc_const_unstable(feature = "const_index", issue = "143775")]
11impl<T, I> const ops::Index<I> for [T]
12where
13    I: [const] SliceIndex<[T]>,
14{
15    type Output = I::Output;
16
17    #[inline(always)]
18    fn index(&self, index: I) -> &I::Output {
19        index.index(self)
20    }
21}
22
23#[stable(feature = "rust1", since = "1.0.0")]
24#[rustc_const_unstable(feature = "const_index", issue = "143775")]
25impl<T, I> const ops::IndexMut<I> for [T]
26where
27    I: [const] SliceIndex<[T]>,
28{
29    #[inline(always)]
30    fn index_mut(&mut self, index: I) -> &mut I::Output {
31        index.index_mut(self)
32    }
33}
34
35#[cfg_attr(not(panic = "immediate-abort"), inline(never), cold)]
36#[cfg_attr(panic = "immediate-abort", inline)]
37#[track_caller]
38const fn slice_index_fail(start: usize, end: usize, len: usize) -> ! {
39    if start > len {
40        const_panic!(
41            "slice start index is out of range for slice",
42            "range start index {start} out of range for slice of length {len}",
43            start: usize,
44            len: usize,
45        )
46    }
47
48    if end > len {
49        const_panic!(
50            "slice end index is out of range for slice",
51            "range end index {end} out of range for slice of length {len}",
52            end: usize,
53            len: usize,
54        )
55    }
56
57    if start > end {
58        const_panic!(
59            "slice index start is larger than end",
60            "slice index starts at {start} but ends at {end}",
61            start: usize,
62            end: usize,
63        )
64    }
65
66    // Only reachable if the range was a `RangeInclusive` or a
67    // `RangeToInclusive`, with `end == len`.
68    const_panic!(
69        "slice end index is out of range for slice",
70        "range end index {end} out of range for slice of length {len}",
71        end: usize,
72        len: usize,
73    )
74}
75
76// The UbChecks are great for catching bugs in the unsafe methods, but including
77// them in safe indexing is unnecessary and hurts inlining and debug runtime perf.
78// Both the safe and unsafe public methods share these helpers,
79// which use intrinsics directly to get *no* extra checks.
80
81#[inline(always)]
82const unsafe fn get_offset_len_noubcheck<T>(
83    ptr: *const [T],
84    offset: usize,
85    len: usize,
86) -> *const [T] {
87    let ptr = ptr as *const T;
88    // SAFETY: The caller already checked these preconditions
89    let ptr = unsafe { crate::intrinsics::offset(ptr, offset) };
90    crate::intrinsics::aggregate_raw_ptr(ptr, len)
91}
92
93#[inline(always)]
94const unsafe fn get_offset_len_mut_noubcheck<T>(
95    ptr: *mut [T],
96    offset: usize,
97    len: usize,
98) -> *mut [T] {
99    let ptr = ptr as *mut T;
100    // SAFETY: The caller already checked these preconditions
101    let ptr = unsafe { crate::intrinsics::offset(ptr, offset) };
102    crate::intrinsics::aggregate_raw_ptr(ptr, len)
103}
104
105mod private_slice_index {
106    use super::{ops, range};
107
108    #[stable(feature = "slice_get_slice", since = "1.28.0")]
109    pub trait Sealed {}
110
111    #[stable(feature = "slice_get_slice", since = "1.28.0")]
112    impl Sealed for usize {}
113    #[stable(feature = "slice_get_slice", since = "1.28.0")]
114    impl Sealed for ops::Range<usize> {}
115    #[stable(feature = "slice_get_slice", since = "1.28.0")]
116    impl Sealed for ops::RangeTo<usize> {}
117    #[stable(feature = "slice_get_slice", since = "1.28.0")]
118    impl Sealed for ops::RangeFrom<usize> {}
119    #[stable(feature = "slice_get_slice", since = "1.28.0")]
120    impl Sealed for ops::RangeFull {}
121    #[stable(feature = "slice_get_slice", since = "1.28.0")]
122    impl Sealed for ops::RangeInclusive<usize> {}
123    #[stable(feature = "slice_get_slice", since = "1.28.0")]
124    impl Sealed for ops::RangeToInclusive<usize> {}
125    #[stable(feature = "slice_index_with_ops_bound_pair", since = "1.53.0")]
126    impl Sealed for (ops::Bound<usize>, ops::Bound<usize>) {}
127
128    #[unstable(feature = "new_range_api", issue = "125687")]
129    impl Sealed for range::Range<usize> {}
130    #[stable(feature = "new_range_inclusive_api", since = "1.95.0")]
131    impl Sealed for range::RangeInclusive<usize> {}
132    #[unstable(feature = "new_range_api", issue = "125687")]
133    impl Sealed for range::RangeToInclusive<usize> {}
134    #[unstable(feature = "new_range_api", issue = "125687")]
135    impl Sealed for range::RangeFrom<usize> {}
136
137    impl Sealed for ops::IndexRange {}
138
139    #[unstable(feature = "sliceindex_wrappers", issue = "146179")]
140    impl Sealed for crate::index::Last {}
141    #[unstable(feature = "sliceindex_wrappers", issue = "146179")]
142    impl<T> Sealed for crate::index::Clamp<T> where T: Sealed {}
143}
144
145/// A helper trait used for indexing operations.
146///
147/// Implementations of this trait have to promise that if the argument
148/// to `get_unchecked(_mut)` is a safe reference, then so is the result.
149#[stable(feature = "slice_get_slice", since = "1.28.0")]
150#[rustc_diagnostic_item = "SliceIndex"]
151#[rustc_on_unimplemented(
152    on(T = "str", label = "string indices are ranges of `usize`",),
153    on(
154        all(any(T = "str", T = "&str", T = "alloc::string::String"), Self = "{integer}"),
155        note = "you can use `.chars().nth()` or `.bytes().nth()`\n\
156                for more information, see chapter 8 in The Book: \
157                <https://doc.rust-lang.org/book/ch08-02-strings.html#indexing-into-strings>"
158    ),
159    message = "the type `{T}` cannot be indexed by `{Self}`",
160    label = "slice indices are of type `usize` or ranges of `usize`"
161)]
162#[rustc_const_unstable(feature = "const_index", issue = "143775")]
163pub const unsafe trait SliceIndex<T: ?Sized>: private_slice_index::Sealed {
164    /// The output type returned by methods.
165    #[stable(feature = "slice_get_slice", since = "1.28.0")]
166    type Output: ?Sized;
167
168    /// Returns a shared reference to the output at this location, if in
169    /// bounds.
170    #[unstable(feature = "slice_index_methods", issue = "none")]
171    fn get(self, slice: &T) -> Option<&Self::Output>;
172
173    /// Returns a mutable reference to the output at this location, if in
174    /// bounds.
175    #[unstable(feature = "slice_index_methods", issue = "none")]
176    fn get_mut(self, slice: &mut T) -> Option<&mut Self::Output>;
177
178    /// Returns a pointer to the output at this location, without
179    /// performing any bounds checking.
180    ///
181    /// Calling this method with an out-of-bounds index or a dangling `slice` pointer
182    /// is *[undefined behavior]* even if the resulting pointer is not used.
183    ///
184    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
185    #[unstable(feature = "slice_index_methods", issue = "none")]
186    unsafe fn get_unchecked(self, slice: *const T) -> *const Self::Output;
187
188    /// Returns a mutable pointer to the output at this location, without
189    /// performing any bounds checking.
190    ///
191    /// Calling this method with an out-of-bounds index or a dangling `slice` pointer
192    /// is *[undefined behavior]* even if the resulting pointer is not used.
193    ///
194    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
195    #[unstable(feature = "slice_index_methods", issue = "none")]
196    unsafe fn get_unchecked_mut(self, slice: *mut T) -> *mut Self::Output;
197
198    /// Returns a shared reference to the output at this location, panicking
199    /// if out of bounds.
200    #[unstable(feature = "slice_index_methods", issue = "none")]
201    #[track_caller]
202    fn index(self, slice: &T) -> &Self::Output;
203
204    /// Returns a mutable reference to the output at this location, panicking
205    /// if out of bounds.
206    #[unstable(feature = "slice_index_methods", issue = "none")]
207    #[track_caller]
208    fn index_mut(self, slice: &mut T) -> &mut Self::Output;
209}
210
211/// The methods `index` and `index_mut` panic if the index is out of bounds.
212#[stable(feature = "slice_get_slice_impls", since = "1.15.0")]
213#[rustc_const_unstable(feature = "const_index", issue = "143775")]
214unsafe impl<T> const SliceIndex<[T]> for usize {
215    type Output = T;
216
217    #[inline]
218    fn get(self, slice: &[T]) -> Option<&T> {
219        if self < slice.len() {
220            // SAFETY: `self` is checked to be in bounds.
221            unsafe { Some(slice_get_unchecked(slice, self)) }
222        } else {
223            None
224        }
225    }
226
227    #[inline]
228    fn get_mut(self, slice: &mut [T]) -> Option<&mut T> {
229        if self < slice.len() {
230            // SAFETY: `self` is checked to be in bounds.
231            unsafe { Some(slice_get_unchecked(slice, self)) }
232        } else {
233            None
234        }
235    }
236
237    #[inline]
238    #[track_caller]
239    unsafe fn get_unchecked(self, slice: *const [T]) -> *const T {
240        assert_unsafe_precondition!(
241            check_language_ub, // okay because of the `assume` below
242            "slice::get_unchecked requires that the index is within the slice",
243            (this: usize = self, len: usize = slice.len()) => this < len
244        );
245        // SAFETY: the caller guarantees that `slice` is not dangling, so it
246        // cannot be longer than `isize::MAX`. They also guarantee that
247        // `self` is in bounds of `slice` so `self` cannot overflow an `isize`,
248        // so the call to `add` is safe.
249        unsafe {
250            // Use intrinsics::assume instead of hint::assert_unchecked so that we don't check the
251            // precondition of this function twice.
252            crate::intrinsics::assume(self < slice.len());
253            slice_get_unchecked(slice, self)
254        }
255    }
256
257    #[inline]
258    #[track_caller]
259    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut T {
260        assert_unsafe_precondition!(
261            check_library_ub,
262            "slice::get_unchecked_mut requires that the index is within the slice",
263            (this: usize = self, len: usize = slice.len()) => this < len
264        );
265        // SAFETY: see comments for `get_unchecked` above.
266        unsafe { slice_get_unchecked(slice, self) }
267    }
268
269    #[inline]
270    fn index(self, slice: &[T]) -> &T {
271        // N.B., use intrinsic indexing
272        &(*slice)[self]
273    }
274
275    #[inline]
276    fn index_mut(self, slice: &mut [T]) -> &mut T {
277        // N.B., use intrinsic indexing
278        &mut (*slice)[self]
279    }
280}
281
282/// Because `IndexRange` guarantees `start <= end`, fewer checks are needed here
283/// than there are for a general `Range<usize>` (which might be `100..3`).
284#[rustc_const_unstable(feature = "const_index", issue = "143775")]
285unsafe impl<T> const SliceIndex<[T]> for ops::IndexRange {
286    type Output = [T];
287
288    #[inline]
289    fn get(self, slice: &[T]) -> Option<&[T]> {
290        if self.end() <= slice.len() {
291            // SAFETY: `self` is checked to be valid and in bounds above.
292            unsafe { Some(&*get_offset_len_noubcheck(slice, self.start(), self.len())) }
293        } else {
294            None
295        }
296    }
297
298    #[inline]
299    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
300        if self.end() <= slice.len() {
301            // SAFETY: `self` is checked to be valid and in bounds above.
302            unsafe { Some(&mut *get_offset_len_mut_noubcheck(slice, self.start(), self.len())) }
303        } else {
304            None
305        }
306    }
307
308    #[inline]
309    #[track_caller]
310    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
311        assert_unsafe_precondition!(
312            check_library_ub,
313            "slice::get_unchecked requires that the index is within the slice",
314            (end: usize = self.end(), len: usize = slice.len()) => end <= len
315        );
316        // SAFETY: the caller guarantees that `slice` is not dangling, so it
317        // cannot be longer than `isize::MAX`. They also guarantee that
318        // `self` is in bounds of `slice` so `self` cannot overflow an `isize`,
319        // so the call to `add` is safe.
320        unsafe { get_offset_len_noubcheck(slice, self.start(), self.len()) }
321    }
322
323    #[inline]
324    #[track_caller]
325    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
326        assert_unsafe_precondition!(
327            check_library_ub,
328            "slice::get_unchecked_mut requires that the index is within the slice",
329            (end: usize = self.end(), len: usize = slice.len()) => end <= len
330        );
331
332        // SAFETY: see comments for `get_unchecked` above.
333        unsafe { get_offset_len_mut_noubcheck(slice, self.start(), self.len()) }
334    }
335
336    #[inline]
337    fn index(self, slice: &[T]) -> &[T] {
338        if self.end() <= slice.len() {
339            // SAFETY: `self` is checked to be valid and in bounds above.
340            unsafe { &*get_offset_len_noubcheck(slice, self.start(), self.len()) }
341        } else {
342            slice_index_fail(self.start(), self.end(), slice.len())
343        }
344    }
345
346    #[inline]
347    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
348        if self.end() <= slice.len() {
349            // SAFETY: `self` is checked to be valid and in bounds above.
350            unsafe { &mut *get_offset_len_mut_noubcheck(slice, self.start(), self.len()) }
351        } else {
352            slice_index_fail(self.start(), self.end(), slice.len())
353        }
354    }
355}
356
357/// The methods `index` and `index_mut` panic if:
358/// - the start of the range is greater than the end of the range or
359/// - the end of the range is out of bounds.
360#[stable(feature = "slice_get_slice_impls", since = "1.15.0")]
361#[rustc_const_unstable(feature = "const_index", issue = "143775")]
362unsafe impl<T> const SliceIndex<[T]> for ops::Range<usize> {
363    type Output = [T];
364
365    #[inline]
366    fn get(self, slice: &[T]) -> Option<&[T]> {
367        // Using checked_sub is a safe way to get `SubUnchecked` in MIR
368        if let Some(new_len) = usize::checked_sub(self.end, self.start)
369            && self.end <= slice.len()
370        {
371            // SAFETY: `self` is checked to be valid and in bounds above.
372            unsafe { Some(&*get_offset_len_noubcheck(slice, self.start, new_len)) }
373        } else {
374            None
375        }
376    }
377
378    #[inline]
379    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
380        if let Some(new_len) = usize::checked_sub(self.end, self.start)
381            && self.end <= slice.len()
382        {
383            // SAFETY: `self` is checked to be valid and in bounds above.
384            unsafe { Some(&mut *get_offset_len_mut_noubcheck(slice, self.start, new_len)) }
385        } else {
386            None
387        }
388    }
389
390    #[inline]
391    #[track_caller]
392    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
393        assert_unsafe_precondition!(
394            check_library_ub,
395            "slice::get_unchecked requires that the range is within the slice",
396            (
397                start: usize = self.start,
398                end: usize = self.end,
399                len: usize = slice.len()
400            ) => end >= start && end <= len
401        );
402
403        // SAFETY: the caller guarantees that `slice` is not dangling, so it
404        // cannot be longer than `isize::MAX`. They also guarantee that
405        // `self` is in bounds of `slice` so `self` cannot overflow an `isize`,
406        // so the call to `add` is safe and the length calculation cannot overflow.
407        unsafe {
408            // Using the intrinsic avoids a superfluous UB check,
409            // since the one on this method already checked `end >= start`.
410            let new_len = crate::intrinsics::unchecked_sub(self.end, self.start);
411            get_offset_len_noubcheck(slice, self.start, new_len)
412        }
413    }
414
415    #[inline]
416    #[track_caller]
417    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
418        assert_unsafe_precondition!(
419            check_library_ub,
420            "slice::get_unchecked_mut requires that the range is within the slice",
421            (
422                start: usize = self.start,
423                end: usize = self.end,
424                len: usize = slice.len()
425            ) => end >= start && end <= len
426        );
427        // SAFETY: see comments for `get_unchecked` above.
428        unsafe {
429            let new_len = crate::intrinsics::unchecked_sub(self.end, self.start);
430            get_offset_len_mut_noubcheck(slice, self.start, new_len)
431        }
432    }
433
434    #[inline(always)]
435    fn index(self, slice: &[T]) -> &[T] {
436        // Using checked_sub is a safe way to get `SubUnchecked` in MIR
437        if let Some(new_len) = usize::checked_sub(self.end, self.start)
438            && self.end <= slice.len()
439        {
440            // SAFETY: `self` is checked to be valid and in bounds above.
441            unsafe { &*get_offset_len_noubcheck(slice, self.start, new_len) }
442        } else {
443            slice_index_fail(self.start, self.end, slice.len())
444        }
445    }
446
447    #[inline]
448    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
449        // Using checked_sub is a safe way to get `SubUnchecked` in MIR
450        if let Some(new_len) = usize::checked_sub(self.end, self.start)
451            && self.end <= slice.len()
452        {
453            // SAFETY: `self` is checked to be valid and in bounds above.
454            unsafe { &mut *get_offset_len_mut_noubcheck(slice, self.start, new_len) }
455        } else {
456            slice_index_fail(self.start, self.end, slice.len())
457        }
458    }
459}
460
461#[unstable(feature = "new_range_api", issue = "125687")]
462#[rustc_const_unstable(feature = "const_index", issue = "143775")]
463unsafe impl<T> const SliceIndex<[T]> for range::Range<usize> {
464    type Output = [T];
465
466    #[inline]
467    fn get(self, slice: &[T]) -> Option<&[T]> {
468        ops::Range::from(self).get(slice)
469    }
470
471    #[inline]
472    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
473        ops::Range::from(self).get_mut(slice)
474    }
475
476    #[inline]
477    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
478        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
479        unsafe { ops::Range::from(self).get_unchecked(slice) }
480    }
481
482    #[inline]
483    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
484        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
485        unsafe { ops::Range::from(self).get_unchecked_mut(slice) }
486    }
487
488    #[inline(always)]
489    fn index(self, slice: &[T]) -> &[T] {
490        ops::Range::from(self).index(slice)
491    }
492
493    #[inline]
494    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
495        ops::Range::from(self).index_mut(slice)
496    }
497}
498
499/// The methods `index` and `index_mut` panic if the end of the range is out of bounds.
500#[stable(feature = "slice_get_slice_impls", since = "1.15.0")]
501#[rustc_const_unstable(feature = "const_index", issue = "143775")]
502unsafe impl<T> const SliceIndex<[T]> for ops::RangeTo<usize> {
503    type Output = [T];
504
505    #[inline]
506    fn get(self, slice: &[T]) -> Option<&[T]> {
507        (0..self.end).get(slice)
508    }
509
510    #[inline]
511    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
512        (0..self.end).get_mut(slice)
513    }
514
515    #[inline]
516    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
517        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
518        unsafe { (0..self.end).get_unchecked(slice) }
519    }
520
521    #[inline]
522    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
523        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
524        unsafe { (0..self.end).get_unchecked_mut(slice) }
525    }
526
527    #[inline(always)]
528    fn index(self, slice: &[T]) -> &[T] {
529        (0..self.end).index(slice)
530    }
531
532    #[inline]
533    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
534        (0..self.end).index_mut(slice)
535    }
536}
537
538/// The methods `index` and `index_mut` panic if the start of the range is out of bounds.
539#[stable(feature = "slice_get_slice_impls", since = "1.15.0")]
540#[rustc_const_unstable(feature = "const_index", issue = "143775")]
541unsafe impl<T> const SliceIndex<[T]> for ops::RangeFrom<usize> {
542    type Output = [T];
543
544    #[inline]
545    fn get(self, slice: &[T]) -> Option<&[T]> {
546        (self.start..slice.len()).get(slice)
547    }
548
549    #[inline]
550    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
551        (self.start..slice.len()).get_mut(slice)
552    }
553
554    #[inline]
555    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
556        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
557        unsafe { (self.start..slice.len()).get_unchecked(slice) }
558    }
559
560    #[inline]
561    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
562        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
563        unsafe { (self.start..slice.len()).get_unchecked_mut(slice) }
564    }
565
566    #[inline]
567    fn index(self, slice: &[T]) -> &[T] {
568        if self.start > slice.len() {
569            slice_index_fail(self.start, slice.len(), slice.len())
570        }
571        // SAFETY: `self` is checked to be valid and in bounds above.
572        unsafe {
573            let new_len = crate::intrinsics::unchecked_sub(slice.len(), self.start);
574            &*get_offset_len_noubcheck(slice, self.start, new_len)
575        }
576    }
577
578    #[inline]
579    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
580        if self.start > slice.len() {
581            slice_index_fail(self.start, slice.len(), slice.len())
582        }
583        // SAFETY: `self` is checked to be valid and in bounds above.
584        unsafe {
585            let new_len = crate::intrinsics::unchecked_sub(slice.len(), self.start);
586            &mut *get_offset_len_mut_noubcheck(slice, self.start, new_len)
587        }
588    }
589}
590
591#[unstable(feature = "new_range_api", issue = "125687")]
592#[rustc_const_unstable(feature = "const_index", issue = "143775")]
593unsafe impl<T> const SliceIndex<[T]> for range::RangeFrom<usize> {
594    type Output = [T];
595
596    #[inline]
597    fn get(self, slice: &[T]) -> Option<&[T]> {
598        ops::RangeFrom::from(self).get(slice)
599    }
600
601    #[inline]
602    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
603        ops::RangeFrom::from(self).get_mut(slice)
604    }
605
606    #[inline]
607    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
608        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
609        unsafe { ops::RangeFrom::from(self).get_unchecked(slice) }
610    }
611
612    #[inline]
613    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
614        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
615        unsafe { ops::RangeFrom::from(self).get_unchecked_mut(slice) }
616    }
617
618    #[inline]
619    fn index(self, slice: &[T]) -> &[T] {
620        ops::RangeFrom::from(self).index(slice)
621    }
622
623    #[inline]
624    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
625        ops::RangeFrom::from(self).index_mut(slice)
626    }
627}
628
629#[stable(feature = "slice_get_slice_impls", since = "1.15.0")]
630#[rustc_const_unstable(feature = "const_index", issue = "143775")]
631unsafe impl<T> const SliceIndex<[T]> for ops::RangeFull {
632    type Output = [T];
633
634    #[inline]
635    fn get(self, slice: &[T]) -> Option<&[T]> {
636        Some(slice)
637    }
638
639    #[inline]
640    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
641        Some(slice)
642    }
643
644    #[inline]
645    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
646        slice
647    }
648
649    #[inline]
650    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
651        slice
652    }
653
654    #[inline]
655    fn index(self, slice: &[T]) -> &[T] {
656        slice
657    }
658
659    #[inline]
660    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
661        slice
662    }
663}
664
665/// The methods `index` and `index_mut` panic if:
666/// - the start of the range is greater than the end of the range or
667/// - the end of the range is out of bounds.
668#[stable(feature = "inclusive_range", since = "1.26.0")]
669#[rustc_const_unstable(feature = "const_index", issue = "143775")]
670unsafe impl<T> const SliceIndex<[T]> for ops::RangeInclusive<usize> {
671    type Output = [T];
672
673    #[inline]
674    fn get(self, slice: &[T]) -> Option<&[T]> {
675        if *self.end() >= slice.len() { None } else { self.into_slice_range().get(slice) }
676    }
677
678    #[inline]
679    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
680        if *self.end() >= slice.len() { None } else { self.into_slice_range().get_mut(slice) }
681    }
682
683    #[inline]
684    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
685        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
686        unsafe { self.into_slice_range().get_unchecked(slice) }
687    }
688
689    #[inline]
690    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
691        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
692        unsafe { self.into_slice_range().get_unchecked_mut(slice) }
693    }
694
695    #[inline]
696    fn index(self, slice: &[T]) -> &[T] {
697        let Self { mut start, mut end, exhausted } = self;
698        let len = slice.len();
699        if end < len {
700            end = end + 1;
701            start = if exhausted { end } else { start };
702            if let Some(new_len) = usize::checked_sub(end, start) {
703                // SAFETY: `self` is checked to be valid and in bounds above.
704                unsafe { return &*get_offset_len_noubcheck(slice, start, new_len) }
705            }
706        }
707        slice_index_fail(start, end, slice.len())
708    }
709
710    #[inline]
711    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
712        let Self { mut start, mut end, exhausted } = self;
713        let len = slice.len();
714        if end < len {
715            end = end + 1;
716            start = if exhausted { end } else { start };
717            if let Some(new_len) = usize::checked_sub(end, start) {
718                // SAFETY: `self` is checked to be valid and in bounds above.
719                unsafe { return &mut *get_offset_len_mut_noubcheck(slice, start, new_len) }
720            }
721        }
722        slice_index_fail(start, end, slice.len())
723    }
724}
725
726#[stable(feature = "new_range_inclusive_api", since = "1.95.0")]
727#[rustc_const_unstable(feature = "const_index", issue = "143775")]
728unsafe impl<T> const SliceIndex<[T]> for range::RangeInclusive<usize> {
729    type Output = [T];
730
731    #[inline]
732    fn get(self, slice: &[T]) -> Option<&[T]> {
733        ops::RangeInclusive::from(self).get(slice)
734    }
735
736    #[inline]
737    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
738        ops::RangeInclusive::from(self).get_mut(slice)
739    }
740
741    #[inline]
742    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
743        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
744        unsafe { ops::RangeInclusive::from(self).get_unchecked(slice) }
745    }
746
747    #[inline]
748    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
749        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
750        unsafe { ops::RangeInclusive::from(self).get_unchecked_mut(slice) }
751    }
752
753    #[inline]
754    fn index(self, slice: &[T]) -> &[T] {
755        ops::RangeInclusive::from(self).index(slice)
756    }
757
758    #[inline]
759    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
760        ops::RangeInclusive::from(self).index_mut(slice)
761    }
762}
763
764/// The methods `index` and `index_mut` panic if the end of the range is out of bounds.
765#[stable(feature = "inclusive_range", since = "1.26.0")]
766#[rustc_const_unstable(feature = "const_index", issue = "143775")]
767unsafe impl<T> const SliceIndex<[T]> for ops::RangeToInclusive<usize> {
768    type Output = [T];
769
770    #[inline]
771    fn get(self, slice: &[T]) -> Option<&[T]> {
772        (0..=self.end).get(slice)
773    }
774
775    #[inline]
776    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
777        (0..=self.end).get_mut(slice)
778    }
779
780    #[inline]
781    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
782        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
783        unsafe { (0..=self.end).get_unchecked(slice) }
784    }
785
786    #[inline]
787    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
788        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
789        unsafe { (0..=self.end).get_unchecked_mut(slice) }
790    }
791
792    #[inline]
793    fn index(self, slice: &[T]) -> &[T] {
794        (0..=self.end).index(slice)
795    }
796
797    #[inline]
798    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
799        (0..=self.end).index_mut(slice)
800    }
801}
802
803/// The methods `index` and `index_mut` panic if the end of the range is out of bounds.
804#[stable(feature = "inclusive_range", since = "1.26.0")]
805#[rustc_const_unstable(feature = "const_index", issue = "143775")]
806unsafe impl<T> const SliceIndex<[T]> for range::RangeToInclusive<usize> {
807    type Output = [T];
808
809    #[inline]
810    fn get(self, slice: &[T]) -> Option<&[T]> {
811        (0..=self.last).get(slice)
812    }
813
814    #[inline]
815    fn get_mut(self, slice: &mut [T]) -> Option<&mut [T]> {
816        (0..=self.last).get_mut(slice)
817    }
818
819    #[inline]
820    unsafe fn get_unchecked(self, slice: *const [T]) -> *const [T] {
821        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
822        unsafe { (0..=self.last).get_unchecked(slice) }
823    }
824
825    #[inline]
826    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut [T] {
827        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
828        unsafe { (0..=self.last).get_unchecked_mut(slice) }
829    }
830
831    #[inline]
832    fn index(self, slice: &[T]) -> &[T] {
833        (0..=self.last).index(slice)
834    }
835
836    #[inline]
837    fn index_mut(self, slice: &mut [T]) -> &mut [T] {
838        (0..=self.last).index_mut(slice)
839    }
840}
841
842/// Performs bounds checking of a range.
843///
844/// This method is similar to [`Index::index`] for slices, but it returns a
845/// [`Range`] equivalent to `range`. You can use this method to turn any range
846/// into `start` and `end` values.
847///
848/// `bounds` is the range of the slice to use for bounds checking. It should
849/// be a [`RangeTo`] range that ends at the length of the slice.
850///
851/// The returned [`Range`] is safe to pass to [`slice::get_unchecked`] and
852/// [`slice::get_unchecked_mut`] for slices with the given range.
853///
854/// [`Range`]: ops::Range
855/// [`RangeTo`]: ops::RangeTo
856/// [`slice::get_unchecked`]: slice::get_unchecked
857/// [`slice::get_unchecked_mut`]: slice::get_unchecked_mut
858///
859/// # Panics
860///
861/// Panics if `range` would be out of bounds.
862///
863/// # Examples
864///
865/// ```
866/// #![feature(slice_range)]
867///
868/// use std::slice;
869///
870/// let v = [10, 40, 30];
871/// assert_eq!(1..2, slice::range(1..2, ..v.len()));
872/// assert_eq!(0..2, slice::range(..2, ..v.len()));
873/// assert_eq!(1..3, slice::range(1.., ..v.len()));
874/// ```
875///
876/// Panics when [`Index::index`] would panic:
877///
878/// ```should_panic
879/// #![feature(slice_range)]
880///
881/// use std::slice;
882///
883/// let _ = slice::range(2..1, ..3);
884/// ```
885///
886/// ```should_panic
887/// #![feature(slice_range)]
888///
889/// use std::slice;
890///
891/// let _ = slice::range(1..4, ..3);
892/// ```
893///
894/// ```should_panic
895/// #![feature(slice_range)]
896///
897/// use std::slice;
898///
899/// let _ = slice::range(1..=usize::MAX, ..3);
900/// ```
901///
902/// [`Index::index`]: ops::Index::index
903#[track_caller]
904#[unstable(feature = "slice_range", issue = "76393")]
905#[must_use]
906#[rustc_const_unstable(feature = "const_range", issue = "none")]
907pub const fn range<R>(range: R, bounds: ops::RangeTo<usize>) -> ops::Range<usize>
908where
909    R: [const] ops::RangeBounds<usize> + [const] Destruct,
910{
911    let len = bounds.end;
912    into_slice_range(len, (range.start_bound().copied(), range.end_bound().copied()))
913}
914
915/// Performs bounds checking of a range without panicking.
916///
917/// This is a version of [`range()`] that returns [`None`] instead of panicking.
918///
919/// # Examples
920///
921/// ```
922/// #![feature(slice_range)]
923///
924/// use std::slice;
925///
926/// let v = [10, 40, 30];
927/// assert_eq!(Some(1..2), slice::try_range(1..2, ..v.len()));
928/// assert_eq!(Some(0..2), slice::try_range(..2, ..v.len()));
929/// assert_eq!(Some(1..3), slice::try_range(1.., ..v.len()));
930/// ```
931///
932/// Returns [`None`] when [`Index::index`] would panic:
933///
934/// ```
935/// #![feature(slice_range)]
936///
937/// use std::slice;
938///
939/// assert_eq!(None, slice::try_range(2..1, ..3));
940/// assert_eq!(None, slice::try_range(1..4, ..3));
941/// assert_eq!(None, slice::try_range(1..=usize::MAX, ..3));
942/// ```
943///
944/// [`Index::index`]: ops::Index::index
945#[unstable(feature = "slice_range", issue = "76393")]
946#[must_use]
947pub fn try_range<R>(range: R, bounds: ops::RangeTo<usize>) -> Option<ops::Range<usize>>
948where
949    R: ops::RangeBounds<usize>,
950{
951    let len = bounds.end;
952    try_into_slice_range(len, (range.start_bound().copied(), range.end_bound().copied()))
953}
954
955/// Converts a pair of `ops::Bound`s into `ops::Range` without performing any
956/// bounds checking or (in debug) overflow checking.
957pub(crate) const fn into_range_unchecked(
958    len: usize,
959    (start, end): (ops::Bound<usize>, ops::Bound<usize>),
960) -> ops::Range<usize> {
961    use ops::Bound;
962    let start = match start {
963        Bound::Included(i) => i,
964        Bound::Excluded(i) => i + 1,
965        Bound::Unbounded => 0,
966    };
967    let end = match end {
968        Bound::Included(i) => i + 1,
969        Bound::Excluded(i) => i,
970        Bound::Unbounded => len,
971    };
972    start..end
973}
974
975/// Converts pair of `ops::Bound`s into `ops::Range`.
976/// Returns `None` on overflowing indices.
977#[rustc_const_unstable(feature = "const_range", issue = "none")]
978#[inline]
979pub(crate) const fn try_into_slice_range(
980    len: usize,
981    (start, end): (ops::Bound<usize>, ops::Bound<usize>),
982) -> Option<ops::Range<usize>> {
983    let end = match end {
984        ops::Bound::Included(end) if end >= len => return None,
985        // Cannot overflow because `end < len` implies `end < usize::MAX`.
986        ops::Bound::Included(end) => end + 1,
987
988        ops::Bound::Excluded(end) if end > len => return None,
989        ops::Bound::Excluded(end) => end,
990
991        ops::Bound::Unbounded => len,
992    };
993
994    let start = match start {
995        ops::Bound::Excluded(start) if start >= end => return None,
996        // Cannot overflow because `start < end` implies `start < usize::MAX`.
997        ops::Bound::Excluded(start) => start + 1,
998
999        ops::Bound::Included(start) if start > end => return None,
1000        ops::Bound::Included(start) => start,
1001
1002        ops::Bound::Unbounded => 0,
1003    };
1004
1005    Some(start..end)
1006}
1007
1008/// Converts pair of `ops::Bound`s into `ops::Range`.
1009/// Panics on overflowing indices.
1010#[inline]
1011pub(crate) const fn into_slice_range(
1012    len: usize,
1013    (start, end): (ops::Bound<usize>, ops::Bound<usize>),
1014) -> ops::Range<usize> {
1015    let end = match end {
1016        ops::Bound::Included(end) if end >= len => slice_index_fail(0, end, len),
1017        // Cannot overflow because `end < len` implies `end < usize::MAX`.
1018        ops::Bound::Included(end) => end + 1,
1019
1020        ops::Bound::Excluded(end) if end > len => slice_index_fail(0, end, len),
1021        ops::Bound::Excluded(end) => end,
1022
1023        ops::Bound::Unbounded => len,
1024    };
1025
1026    let start = match start {
1027        ops::Bound::Excluded(start) if start >= end => slice_index_fail(start, end, len),
1028        // Cannot overflow because `start < end` implies `start < usize::MAX`.
1029        ops::Bound::Excluded(start) => start + 1,
1030
1031        ops::Bound::Included(start) if start > end => slice_index_fail(start, end, len),
1032        ops::Bound::Included(start) => start,
1033
1034        ops::Bound::Unbounded => 0,
1035    };
1036
1037    start..end
1038}
1039
1040#[stable(feature = "slice_index_with_ops_bound_pair", since = "1.53.0")]
1041unsafe impl<T> SliceIndex<[T]> for (ops::Bound<usize>, ops::Bound<usize>) {
1042    type Output = [T];
1043
1044    #[inline]
1045    fn get(self, slice: &[T]) -> Option<&Self::Output> {
1046        try_into_slice_range(slice.len(), self)?.get(slice)
1047    }
1048
1049    #[inline]
1050    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
1051        try_into_slice_range(slice.len(), self)?.get_mut(slice)
1052    }
1053
1054    #[inline]
1055    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
1056        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
1057        unsafe { into_range_unchecked(slice.len(), self).get_unchecked(slice) }
1058    }
1059
1060    #[inline]
1061    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
1062        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
1063        unsafe { into_range_unchecked(slice.len(), self).get_unchecked_mut(slice) }
1064    }
1065
1066    #[inline]
1067    fn index(self, slice: &[T]) -> &Self::Output {
1068        into_slice_range(slice.len(), self).index(slice)
1069    }
1070
1071    #[inline]
1072    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
1073        into_slice_range(slice.len(), self).index_mut(slice)
1074    }
1075}
````