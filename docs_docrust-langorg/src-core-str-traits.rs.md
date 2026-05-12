---
title: traits.rs - source
url: https://doc.rust-lang.org/src/core/str/traits.rs.html#62
source: crawler
fetched_at: 2026-05-06T21:27:28.364393288-03:00
rendered_js: false
word_count: 4679
summary: This document defines the core Rust trait implementations for string slices, including lexicographical comparison, equality, and index-based slicing operations.
tags:
    - rust
    - string-slice
    - traits
    - lexicographical-comparison
    - indexing
    - slice-index
category: reference
---

## core/str/ traits.rs

````rust
1//! Trait implementations for `str`.
2
3use super::ParseBoolError;
4use crate::cmp::Ordering;
5use crate::intrinsics::unchecked_sub;
6use crate::slice::SliceIndex;
7use crate::ub_checks::assert_unsafe_precondition;
8use crate::{ops, ptr, range};
9
10/// Implements ordering of strings.
11///
12/// Strings are ordered  [lexicographically](Ord#lexicographical-comparison) by their byte values. This orders Unicode code
13/// points based on their positions in the code charts. This is not necessarily the same as
14/// "alphabetical" order, which varies by language and locale. Sorting strings according to
15/// culturally-accepted standards requires locale-specific data that is outside the scope of
16/// the `str` type.
17#[stable(feature = "rust1", since = "1.0.0")]
18impl Ord for str {
19    #[inline]
20    fn cmp(&self, other: &str) -> Ordering {
21        self.as_bytes().cmp(other.as_bytes())
22    }
23}
24
25#[stable(feature = "rust1", since = "1.0.0")]
26#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
27impl const PartialEq for str {
28    #[inline]
29    fn eq(&self, other: &str) -> bool {
30        self.as_bytes() == other.as_bytes()
31    }
32}
33
34#[stable(feature = "rust1", since = "1.0.0")]
35#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
36impl const Eq for str {}
37
38/// Implements comparison operations on strings.
39///
40/// Strings are compared [lexicographically](Ord#lexicographical-comparison) by their byte values. This compares Unicode code
41/// points based on their positions in the code charts. This is not necessarily the same as
42/// "alphabetical" order, which varies by language and locale. Comparing strings according to
43/// culturally-accepted standards requires locale-specific data that is outside the scope of
44/// the `str` type.
45#[stable(feature = "rust1", since = "1.0.0")]
46impl PartialOrd for str {
47    #[inline]
48    fn partial_cmp(&self, other: &str) -> Option<Ordering> {
49        Some(self.cmp(other))
50    }
51}
52
53#[stable(feature = "rust1", since = "1.0.0")]
54#[rustc_const_unstable(feature = "const_index", issue = "143775")]
55impl<I> const ops::Index<I> for str
56where
57    I: [const] SliceIndex<str>,
58{
59    type Output = I::Output;
60
61    #[inline]
62    fn index(&self, index: I) -> &I::Output {
63        index.index(self)
64    }
65}
66
67#[stable(feature = "rust1", since = "1.0.0")]
68#[rustc_const_unstable(feature = "const_index", issue = "143775")]
69impl<I> const ops::IndexMut<I> for str
70where
71    I: [const] SliceIndex<str>,
72{
73    #[inline]
74    fn index_mut(&mut self, index: I) -> &mut I::Output {
75        index.index_mut(self)
76    }
77}
78
79/// Implements substring slicing with syntax `&self[..]` or `&mut self[..]`.
80///
81/// Returns a slice of the whole string, i.e., returns `&self` or `&mut
82/// self`. Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`. Unlike
83/// other indexing operations, this can never panic.
84///
85/// This operation is *O*(1).
86///
87/// Prior to 1.20.0, these indexing operations were still supported by
88/// direct implementation of `Index` and `IndexMut`.
89///
90/// Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`.
91#[stable(feature = "str_checked_slicing", since = "1.20.0")]
92#[rustc_const_unstable(feature = "const_index", issue = "143775")]
93unsafe impl const SliceIndex<str> for ops::RangeFull {
94    type Output = str;
95    #[inline]
96    fn get(self, slice: &str) -> Option<&Self::Output> {
97        Some(slice)
98    }
99    #[inline]
100    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
101        Some(slice)
102    }
103    #[inline]
104    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
105        slice
106    }
107    #[inline]
108    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
109        slice
110    }
111    #[inline]
112    fn index(self, slice: &str) -> &Self::Output {
113        slice
114    }
115    #[inline]
116    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
117        slice
118    }
119}
120
121/// Implements substring slicing with syntax `&self[begin .. end]` or `&mut
122/// self[begin .. end]`.
123///
124/// Returns a slice of the given string from the byte range
125/// [`begin`, `end`).
126///
127/// This operation is *O*(1).
128///
129/// Prior to 1.20.0, these indexing operations were still supported by
130/// direct implementation of `Index` and `IndexMut`.
131///
132/// # Panics
133///
134/// Panics if `begin` or `end` does not point to the starting byte offset of
135/// a character (as defined by `is_char_boundary`), if `begin > end`, or if
136/// `end > len`.
137///
138/// # Examples
139///
140/// ```
141/// let s = "Löwe 老虎 Léopard";
142/// assert_eq!(&s[0 .. 1], "L");
143///
144/// assert_eq!(&s[1 .. 9], "öwe 老");
145///
146/// // these will panic:
147/// // byte 2 lies within `ö`:
148/// // &s[2 ..3];
149///
150/// // byte 8 lies within `老`
151/// // &s[1 .. 8];
152///
153/// // byte 100 is outside the string
154/// // &s[3 .. 100];
155/// ```
156#[stable(feature = "str_checked_slicing", since = "1.20.0")]
157#[rustc_const_unstable(feature = "const_index", issue = "143775")]
158unsafe impl const SliceIndex<str> for ops::Range<usize> {
159    type Output = str;
160    #[inline]
161    fn get(self, slice: &str) -> Option<&Self::Output> {
162        if self.start <= self.end
163            && slice.is_char_boundary(self.start)
164            && slice.is_char_boundary(self.end)
165        {
166            // SAFETY: just checked that `start` and `end` are on a char boundary,
167            // and we are passing in a safe reference, so the return value will also be one.
168            // We also checked char boundaries, so this is valid UTF-8.
169            Some(unsafe { &*self.get_unchecked(slice) })
170        } else {
171            None
172        }
173    }
174    #[inline]
175    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
176        if self.start <= self.end
177            && slice.is_char_boundary(self.start)
178            && slice.is_char_boundary(self.end)
179        {
180            // SAFETY: just checked that `start` and `end` are on a char boundary.
181            // We know the pointer is unique because we got it from `slice`.
182            Some(unsafe { &mut *self.get_unchecked_mut(slice) })
183        } else {
184            None
185        }
186    }
187    #[inline]
188    #[track_caller]
189    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
190        let slice = slice as *const [u8];
191
192        assert_unsafe_precondition!(
193            // We'd like to check that the bounds are on char boundaries,
194            // but there's not really a way to do so without reading
195            // behind the pointer, which has aliasing implications.
196            // It's also not possible to move this check up to
197            // `str::get_unchecked` without adding a special function
198            // to `SliceIndex` just for this.
199            check_library_ub,
200            "str::get_unchecked requires that the range is within the string slice",
201            (
202                start: usize = self.start,
203                end: usize = self.end,
204                len: usize = slice.len()
205            ) => end >= start && end <= len,
206        );
207
208        // SAFETY: the caller guarantees that `self` is in bounds of `slice`
209        // which satisfies all the conditions for `add`.
210        unsafe {
211            let new_len = unchecked_sub(self.end, self.start);
212            ptr::slice_from_raw_parts(slice.as_ptr().add(self.start), new_len) as *const str
213        }
214    }
215    #[inline]
216    #[track_caller]
217    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
218        let slice = slice as *mut [u8];
219
220        assert_unsafe_precondition!(
221            check_library_ub,
222            "str::get_unchecked_mut requires that the range is within the string slice",
223            (
224                start: usize = self.start,
225                end: usize = self.end,
226                len: usize = slice.len()
227            ) => end >= start && end <= len,
228        );
229
230        // SAFETY: see comments for `get_unchecked`.
231        unsafe {
232            let new_len = unchecked_sub(self.end, self.start);
233            ptr::slice_from_raw_parts_mut(slice.as_mut_ptr().add(self.start), new_len) as *mut str
234        }
235    }
236    #[inline]
237    fn index(self, slice: &str) -> &Self::Output {
238        let (start, end) = (self.start, self.end);
239        match self.get(slice) {
240            Some(s) => s,
241            None => super::slice_error_fail(slice, start, end),
242        }
243    }
244    #[inline]
245    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
246        // is_char_boundary checks that the index is in [0, .len()]
247        // cannot reuse `get` as above, because of NLL trouble
248        if self.start <= self.end
249            && slice.is_char_boundary(self.start)
250            && slice.is_char_boundary(self.end)
251        {
252            // SAFETY: just checked that `start` and `end` are on a char boundary,
253            // and we are passing in a safe reference, so the return value will also be one.
254            unsafe { &mut *self.get_unchecked_mut(slice) }
255        } else {
256            super::slice_error_fail(slice, self.start, self.end)
257        }
258    }
259}
260
261#[unstable(feature = "new_range_api", issue = "125687")]
262#[rustc_const_unstable(feature = "const_index", issue = "143775")]
263unsafe impl const SliceIndex<str> for range::Range<usize> {
264    type Output = str;
265    #[inline]
266    fn get(self, slice: &str) -> Option<&Self::Output> {
267        if self.start <= self.end
268            && slice.is_char_boundary(self.start)
269            && slice.is_char_boundary(self.end)
270        {
271            // SAFETY: just checked that `start` and `end` are on a char boundary,
272            // and we are passing in a safe reference, so the return value will also be one.
273            // We also checked char boundaries, so this is valid UTF-8.
274            Some(unsafe { &*self.get_unchecked(slice) })
275        } else {
276            None
277        }
278    }
279    #[inline]
280    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
281        if self.start <= self.end
282            && slice.is_char_boundary(self.start)
283            && slice.is_char_boundary(self.end)
284        {
285            // SAFETY: just checked that `start` and `end` are on a char boundary.
286            // We know the pointer is unique because we got it from `slice`.
287            Some(unsafe { &mut *self.get_unchecked_mut(slice) })
288        } else {
289            None
290        }
291    }
292    #[inline]
293    #[track_caller]
294    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
295        let slice = slice as *const [u8];
296
297        assert_unsafe_precondition!(
298            // We'd like to check that the bounds are on char boundaries,
299            // but there's not really a way to do so without reading
300            // behind the pointer, which has aliasing implications.
301            // It's also not possible to move this check up to
302            // `str::get_unchecked` without adding a special function
303            // to `SliceIndex` just for this.
304            check_library_ub,
305            "str::get_unchecked requires that the range is within the string slice",
306            (
307                start: usize = self.start,
308                end: usize = self.end,
309                len: usize = slice.len()
310            ) => end >= start && end <= len,
311        );
312
313        // SAFETY: the caller guarantees that `self` is in bounds of `slice`
314        // which satisfies all the conditions for `add`.
315        unsafe {
316            let new_len = unchecked_sub(self.end, self.start);
317            ptr::slice_from_raw_parts(slice.as_ptr().add(self.start), new_len) as *const str
318        }
319    }
320    #[inline]
321    #[track_caller]
322    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
323        let slice = slice as *mut [u8];
324
325        assert_unsafe_precondition!(
326            check_library_ub,
327            "str::get_unchecked_mut requires that the range is within the string slice",
328            (
329                start: usize = self.start,
330                end: usize = self.end,
331                len: usize = slice.len()
332            ) => end >= start && end <= len,
333        );
334
335        // SAFETY: see comments for `get_unchecked`.
336        unsafe {
337            let new_len = unchecked_sub(self.end, self.start);
338            ptr::slice_from_raw_parts_mut(slice.as_mut_ptr().add(self.start), new_len) as *mut str
339        }
340    }
341    #[inline]
342    fn index(self, slice: &str) -> &Self::Output {
343        let (start, end) = (self.start, self.end);
344        match self.get(slice) {
345            Some(s) => s,
346            None => super::slice_error_fail(slice, start, end),
347        }
348    }
349    #[inline]
350    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
351        // is_char_boundary checks that the index is in [0, .len()]
352        // cannot reuse `get` as above, because of NLL trouble
353        if self.start <= self.end
354            && slice.is_char_boundary(self.start)
355            && slice.is_char_boundary(self.end)
356        {
357            // SAFETY: just checked that `start` and `end` are on a char boundary,
358            // and we are passing in a safe reference, so the return value will also be one.
359            unsafe { &mut *self.get_unchecked_mut(slice) }
360        } else {
361            super::slice_error_fail(slice, self.start, self.end)
362        }
363    }
364}
365
366/// Implements substring slicing for arbitrary bounds.
367///
368/// Returns a slice of the given string bounded by the byte indices
369/// provided by each bound.
370///
371/// This operation is *O*(1).
372///
373/// # Panics
374///
375/// Panics if `begin` or `end` (if it exists and once adjusted for
376/// inclusion/exclusion) does not point to the starting byte offset of
377/// a character (as defined by `is_char_boundary`), if `begin > end`, or if
378/// `end > len`.
379#[stable(feature = "slice_index_str_with_ops_bound_pair", since = "1.73.0")]
380unsafe impl SliceIndex<str> for (ops::Bound<usize>, ops::Bound<usize>) {
381    type Output = str;
382
383    #[inline]
384    fn get(self, slice: &str) -> Option<&str> {
385        crate::slice::index::try_into_slice_range(slice.len(), self)?.get(slice)
386    }
387
388    #[inline]
389    fn get_mut(self, slice: &mut str) -> Option<&mut str> {
390        crate::slice::index::try_into_slice_range(slice.len(), self)?.get_mut(slice)
391    }
392
393    #[inline]
394    unsafe fn get_unchecked(self, slice: *const str) -> *const str {
395        let len = (slice as *const [u8]).len();
396        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
397        unsafe { crate::slice::index::into_range_unchecked(len, self).get_unchecked(slice) }
398    }
399
400    #[inline]
401    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut str {
402        let len = (slice as *mut [u8]).len();
403        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
404        unsafe { crate::slice::index::into_range_unchecked(len, self).get_unchecked_mut(slice) }
405    }
406
407    #[inline]
408    fn index(self, slice: &str) -> &str {
409        crate::slice::index::into_slice_range(slice.len(), self).index(slice)
410    }
411
412    #[inline]
413    fn index_mut(self, slice: &mut str) -> &mut str {
414        crate::slice::index::into_slice_range(slice.len(), self).index_mut(slice)
415    }
416}
417
418/// Implements substring slicing with syntax `&self[.. end]` or `&mut
419/// self[.. end]`.
420///
421/// Returns a slice of the given string from the byte range \[0, `end`).
422/// Equivalent to `&self[0 .. end]` or `&mut self[0 .. end]`.
423///
424/// This operation is *O*(1).
425///
426/// Prior to 1.20.0, these indexing operations were still supported by
427/// direct implementation of `Index` and `IndexMut`.
428///
429/// # Panics
430///
431/// Panics if `end` does not point to the starting byte offset of a
432/// character (as defined by `is_char_boundary`), or if `end > len`.
433#[stable(feature = "str_checked_slicing", since = "1.20.0")]
434#[rustc_const_unstable(feature = "const_index", issue = "143775")]
435unsafe impl const SliceIndex<str> for ops::RangeTo<usize> {
436    type Output = str;
437    #[inline]
438    fn get(self, slice: &str) -> Option<&Self::Output> {
439        if slice.is_char_boundary(self.end) {
440            // SAFETY: just checked that `end` is on a char boundary,
441            // and we are passing in a safe reference, so the return value will also be one.
442            Some(unsafe { &*self.get_unchecked(slice) })
443        } else {
444            None
445        }
446    }
447    #[inline]
448    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
449        if slice.is_char_boundary(self.end) {
450            // SAFETY: just checked that `end` is on a char boundary,
451            // and we are passing in a safe reference, so the return value will also be one.
452            Some(unsafe { &mut *self.get_unchecked_mut(slice) })
453        } else {
454            None
455        }
456    }
457    #[inline]
458    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
459        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
460        unsafe { (0..self.end).get_unchecked(slice) }
461    }
462    #[inline]
463    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
464        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
465        unsafe { (0..self.end).get_unchecked_mut(slice) }
466    }
467    #[inline]
468    fn index(self, slice: &str) -> &Self::Output {
469        let end = self.end;
470        match self.get(slice) {
471            Some(s) => s,
472            None => super::slice_error_fail(slice, 0, end),
473        }
474    }
475    #[inline]
476    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
477        if slice.is_char_boundary(self.end) {
478            // SAFETY: just checked that `end` is on a char boundary,
479            // and we are passing in a safe reference, so the return value will also be one.
480            unsafe { &mut *self.get_unchecked_mut(slice) }
481        } else {
482            super::slice_error_fail(slice, 0, self.end)
483        }
484    }
485}
486
487/// Implements substring slicing with syntax `&self[begin ..]` or `&mut
488/// self[begin ..]`.
489///
490/// Returns a slice of the given string from the byte range \[`begin`, `len`).
491/// Equivalent to `&self[begin .. len]` or `&mut self[begin .. len]`.
492///
493/// This operation is *O*(1).
494///
495/// Prior to 1.20.0, these indexing operations were still supported by
496/// direct implementation of `Index` and `IndexMut`.
497///
498/// # Panics
499///
500/// Panics if `begin` does not point to the starting byte offset of
501/// a character (as defined by `is_char_boundary`), or if `begin > len`.
502#[stable(feature = "str_checked_slicing", since = "1.20.0")]
503#[rustc_const_unstable(feature = "const_index", issue = "143775")]
504unsafe impl const SliceIndex<str> for ops::RangeFrom<usize> {
505    type Output = str;
506    #[inline]
507    fn get(self, slice: &str) -> Option<&Self::Output> {
508        if slice.is_char_boundary(self.start) {
509            // SAFETY: just checked that `start` is on a char boundary,
510            // and we are passing in a safe reference, so the return value will also be one.
511            Some(unsafe { &*self.get_unchecked(slice) })
512        } else {
513            None
514        }
515    }
516    #[inline]
517    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
518        if slice.is_char_boundary(self.start) {
519            // SAFETY: just checked that `start` is on a char boundary,
520            // and we are passing in a safe reference, so the return value will also be one.
521            Some(unsafe { &mut *self.get_unchecked_mut(slice) })
522        } else {
523            None
524        }
525    }
526    #[inline]
527    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
528        let len = (slice as *const [u8]).len();
529        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
530        unsafe { (self.start..len).get_unchecked(slice) }
531    }
532    #[inline]
533    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
534        let len = (slice as *mut [u8]).len();
535        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
536        unsafe { (self.start..len).get_unchecked_mut(slice) }
537    }
538    #[inline]
539    fn index(self, slice: &str) -> &Self::Output {
540        let (start, end) = (self.start, slice.len());
541        match self.get(slice) {
542            Some(s) => s,
543            None => super::slice_error_fail(slice, start, end),
544        }
545    }
546    #[inline]
547    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
548        if slice.is_char_boundary(self.start) {
549            // SAFETY: just checked that `start` is on a char boundary,
550            // and we are passing in a safe reference, so the return value will also be one.
551            unsafe { &mut *self.get_unchecked_mut(slice) }
552        } else {
553            super::slice_error_fail(slice, self.start, slice.len())
554        }
555    }
556}
557
558#[unstable(feature = "new_range_api", issue = "125687")]
559#[rustc_const_unstable(feature = "const_index", issue = "143775")]
560unsafe impl const SliceIndex<str> for range::RangeFrom<usize> {
561    type Output = str;
562    #[inline]
563    fn get(self, slice: &str) -> Option<&Self::Output> {
564        if slice.is_char_boundary(self.start) {
565            // SAFETY: just checked that `start` is on a char boundary,
566            // and we are passing in a safe reference, so the return value will also be one.
567            Some(unsafe { &*self.get_unchecked(slice) })
568        } else {
569            None
570        }
571    }
572    #[inline]
573    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
574        if slice.is_char_boundary(self.start) {
575            // SAFETY: just checked that `start` is on a char boundary,
576            // and we are passing in a safe reference, so the return value will also be one.
577            Some(unsafe { &mut *self.get_unchecked_mut(slice) })
578        } else {
579            None
580        }
581    }
582    #[inline]
583    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
584        let len = (slice as *const [u8]).len();
585        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
586        unsafe { (self.start..len).get_unchecked(slice) }
587    }
588    #[inline]
589    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
590        let len = (slice as *mut [u8]).len();
591        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
592        unsafe { (self.start..len).get_unchecked_mut(slice) }
593    }
594    #[inline]
595    fn index(self, slice: &str) -> &Self::Output {
596        let (start, end) = (self.start, slice.len());
597        match self.get(slice) {
598            Some(s) => s,
599            None => super::slice_error_fail(slice, start, end),
600        }
601    }
602    #[inline]
603    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
604        if slice.is_char_boundary(self.start) {
605            // SAFETY: just checked that `start` is on a char boundary,
606            // and we are passing in a safe reference, so the return value will also be one.
607            unsafe { &mut *self.get_unchecked_mut(slice) }
608        } else {
609            super::slice_error_fail(slice, self.start, slice.len())
610        }
611    }
612}
613
614/// Implements substring slicing with syntax `&self[begin ..= end]` or `&mut
615/// self[begin ..= end]`.
616///
617/// Returns a slice of the given string from the byte range
618/// [`begin`, `end`]. Equivalent to `&self [begin .. end + 1]` or `&mut
619/// self[begin .. end + 1]`, except if `end` has the maximum value for
620/// `usize`.
621///
622/// This operation is *O*(1).
623///
624/// # Panics
625///
626/// Panics if `begin` does not point to the starting byte offset of
627/// a character (as defined by `is_char_boundary`), if `end` does not point
628/// to the ending byte offset of a character (`end + 1` is either a starting
629/// byte offset or equal to `len`), if `begin > end`, or if `end >= len`.
630#[stable(feature = "inclusive_range", since = "1.26.0")]
631#[rustc_const_unstable(feature = "const_index", issue = "143775")]
632unsafe impl const SliceIndex<str> for ops::RangeInclusive<usize> {
633    type Output = str;
634    #[inline]
635    fn get(self, slice: &str) -> Option<&Self::Output> {
636        if *self.end() >= slice.len() { None } else { self.into_slice_range().get(slice) }
637    }
638    #[inline]
639    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
640        if *self.end() >= slice.len() { None } else { self.into_slice_range().get_mut(slice) }
641    }
642    #[inline]
643    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
644        // SAFETY: the caller must uphold the safety contract for `get_unchecked`.
645        unsafe { self.into_slice_range().get_unchecked(slice) }
646    }
647    #[inline]
648    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
649        // SAFETY: the caller must uphold the safety contract for `get_unchecked_mut`.
650        unsafe { self.into_slice_range().get_unchecked_mut(slice) }
651    }
652    #[inline]
653    fn index(self, slice: &str) -> &Self::Output {
654        let Self { mut start, mut end, exhausted } = self;
655        let len = slice.len();
656        if end < len {
657            end = end + 1;
658            start = if exhausted { end } else { start };
659            if start <= end && slice.is_char_boundary(start) && slice.is_char_boundary(end) {
660                // SAFETY: just checked that `start` and `end` are on a char boundary,
661                // and we are passing in a safe reference, so the return value will also be one.
662                // We also checked char boundaries, so this is valid UTF-8.
663                unsafe { return &*(start..end).get_unchecked(slice) }
664            }
665        }
666
667        super::slice_error_fail(slice, start, end)
668    }
669    #[inline]
670    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
671        let Self { mut start, mut end, exhausted } = self;
672        let len = slice.len();
673        if end < len {
674            end = end + 1;
675            start = if exhausted { end } else { start };
676            if start <= end && slice.is_char_boundary(start) && slice.is_char_boundary(end) {
677                // SAFETY: just checked that `start` and `end` are on a char boundary,
678                // and we are passing in a safe reference, so the return value will also be one.
679                // We also checked char boundaries, so this is valid UTF-8.
680                unsafe { return &mut *(start..end).get_unchecked_mut(slice) }
681            }
682        }
683
684        super::slice_error_fail(slice, start, end)
685    }
686}
687
688#[stable(feature = "new_range_inclusive_api", since = "1.95.0")]
689#[rustc_const_unstable(feature = "const_index", issue = "143775")]
690unsafe impl const SliceIndex<str> for range::RangeInclusive<usize> {
691    type Output = str;
692    #[inline]
693    fn get(self, slice: &str) -> Option<&Self::Output> {
694        ops::RangeInclusive::from(self).get(slice)
695    }
696    #[inline]
697    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
698        ops::RangeInclusive::from(self).get_mut(slice)
699    }
700    #[inline]
701    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
702        // SAFETY: the caller must uphold the safety contract for `get_unchecked`.
703        unsafe { ops::RangeInclusive::from(self).get_unchecked(slice) }
704    }
705    #[inline]
706    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
707        // SAFETY: the caller must uphold the safety contract for `get_unchecked_mut`.
708        unsafe { ops::RangeInclusive::from(self).get_unchecked_mut(slice) }
709    }
710    #[inline]
711    fn index(self, slice: &str) -> &Self::Output {
712        ops::RangeInclusive::from(self).index(slice)
713    }
714    #[inline]
715    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
716        ops::RangeInclusive::from(self).index_mut(slice)
717    }
718}
719
720/// Implements substring slicing with syntax `&self[..= end]` or `&mut
721/// self[..= end]`.
722///
723/// Returns a slice of the given string from the byte range \[0, `end`\].
724/// Equivalent to `&self [0 .. end + 1]`, except if `end` has the maximum
725/// value for `usize`.
726///
727/// This operation is *O*(1).
728///
729/// # Panics
730///
731/// Panics if `end` does not point to the ending byte offset of a character
732/// (`end + 1` is either a starting byte offset as defined by
733/// `is_char_boundary`, or equal to `len`), or if `end >= len`.
734#[stable(feature = "inclusive_range", since = "1.26.0")]
735#[rustc_const_unstable(feature = "const_index", issue = "143775")]
736unsafe impl const SliceIndex<str> for ops::RangeToInclusive<usize> {
737    type Output = str;
738    #[inline]
739    fn get(self, slice: &str) -> Option<&Self::Output> {
740        (0..=self.end).get(slice)
741    }
742    #[inline]
743    fn get_mut(self, slice: &mut str) -> Option<&mut Self::Output> {
744        (0..=self.end).get_mut(slice)
745    }
746    #[inline]
747    unsafe fn get_unchecked(self, slice: *const str) -> *const Self::Output {
748        // SAFETY: the caller must uphold the safety contract for `get_unchecked`.
749        unsafe { (0..=self.end).get_unchecked(slice) }
750    }
751    #[inline]
752    unsafe fn get_unchecked_mut(self, slice: *mut str) -> *mut Self::Output {
753        // SAFETY: the caller must uphold the safety contract for `get_unchecked_mut`.
754        unsafe { (0..=self.end).get_unchecked_mut(slice) }
755    }
756    #[inline]
757    fn index(self, slice: &str) -> &Self::Output {
758        (0..=self.end).index(slice)
759    }
760    #[inline]
761    fn index_mut(self, slice: &mut str) -> &mut Self::Output {
762        (0..=self.end).index_mut(slice)
763    }
764}
765
766/// Parse a value from a string
767///
768/// `FromStr`'s [`from_str`] method is often used implicitly, through
769/// [`str`]'s [`parse`] method. See [`parse`]'s documentation for examples.
770///
771/// [`from_str`]: FromStr::from_str
772/// [`parse`]: str::parse
773///
774/// `FromStr` does not have a lifetime parameter, and so you can only parse types
775/// that do not contain a lifetime parameter themselves. In other words, you can
776/// parse an `i32` with `FromStr`, but not a `&i32`. You can parse a struct that
777/// contains an `i32`, but not one that contains an `&i32`.
778///
779/// # Input format and round-tripping
780///
781/// The input format expected by a type's `FromStr` implementation depends on the type. Check the
782/// type's documentation for the input formats it knows how to parse. Note that the input format of
783/// a type's `FromStr` implementation might not necessarily accept the output format of its
784/// `Display` implementation, and even if it does, the `Display` implementation may not be lossless
785/// so the round-trip may lose information.
786///
787/// However, if a type has a lossless `Display` implementation whose output is meant to be
788/// conveniently machine-parseable and not just meant for human consumption, then the type may wish
789/// to accept the same format in `FromStr`, and document that usage. Having both `Display` and
790/// `FromStr` implementations where the result of `Display` cannot be parsed with `FromStr` may
791/// surprise users.
792///
793/// # Examples
794///
795/// Basic implementation of `FromStr` on an example `Point` type:
796///
797/// ```
798/// use std::str::FromStr;
799///
800/// #[derive(Debug, PartialEq)]
801/// struct Point {
802///     x: i32,
803///     y: i32
804/// }
805///
806/// #[derive(Debug, PartialEq, Eq)]
807/// struct ParsePointError;
808///
809/// impl FromStr for Point {
810///     type Err = ParsePointError;
811///
812///     fn from_str(s: &str) -> Result<Self, Self::Err> {
813///         let (x, y) = s
814///             .strip_prefix('(')
815///             .and_then(|s| s.strip_suffix(')'))
816///             .and_then(|s| s.split_once(','))
817///             .ok_or(ParsePointError)?;
818///
819///         let x_fromstr = x.parse::<i32>().map_err(|_| ParsePointError)?;
820///         let y_fromstr = y.parse::<i32>().map_err(|_| ParsePointError)?;
821///
822///         Ok(Point { x: x_fromstr, y: y_fromstr })
823///     }
824/// }
825///
826/// let expected = Ok(Point { x: 1, y: 2 });
827/// // Explicit call
828/// assert_eq!(Point::from_str("(1,2)"), expected);
829/// // Implicit calls, through parse
830/// assert_eq!("(1,2)".parse(), expected);
831/// assert_eq!("(1,2)".parse::<Point>(), expected);
832/// // Invalid input string
833/// assert!(Point::from_str("(1 2)").is_err());
834/// ```
835#[stable(feature = "rust1", since = "1.0.0")]
836#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
837pub const trait FromStr: Sized {
838    /// The associated error which can be returned from parsing.
839    #[stable(feature = "rust1", since = "1.0.0")]
840    type Err;
841
842    /// Parses a string `s` to return a value of this type.
843    ///
844    /// If parsing succeeds, return the value inside [`Ok`], otherwise
845    /// when the string is ill-formatted return an error specific to the
846    /// inside [`Err`]. The error type is specific to the implementation of the trait.
847    ///
848    /// # Examples
849    ///
850    /// Basic usage with [`i32`], a type that implements `FromStr`:
851    ///
852    /// ```
853    /// use std::str::FromStr;
854    ///
855    /// let s = "5";
856    /// let x = i32::from_str(s).unwrap();
857    ///
858    /// assert_eq!(5, x);
859    /// ```
860    #[stable(feature = "rust1", since = "1.0.0")]
861    #[rustc_diagnostic_item = "from_str_method"]
862    fn from_str(s: &str) -> Result<Self, Self::Err>;
863}
864
865#[stable(feature = "rust1", since = "1.0.0")]
866impl FromStr for bool {
867    type Err = ParseBoolError;
868
869    /// Parse a `bool` from a string.
870    ///
871    /// The only accepted values are `"true"` and `"false"`. Any other input
872    /// will return an error.
873    ///
874    /// # Examples
875    ///
876    /// ```
877    /// use std::str::FromStr;
878    ///
879    /// assert_eq!(FromStr::from_str("true"), Ok(true));
880    /// assert_eq!(FromStr::from_str("false"), Ok(false));
881    /// assert!(<bool as FromStr>::from_str("not even a boolean").is_err());
882    /// ```
883    ///
884    /// Note, in many cases, the `.parse()` method on `str` is more proper.
885    ///
886    /// ```
887    /// assert_eq!("true".parse(), Ok(true));
888    /// assert_eq!("false".parse(), Ok(false));
889    /// assert!("not even a boolean".parse::<bool>().is_err());
890    /// ```
891    #[inline]
892    fn from_str(s: &str) -> Result<bool, ParseBoolError> {
893        match s {
894            "true" => Ok(true),
895            "false" => Ok(false),
896            _ => Err(ParseBoolError),
897        }
898    }
899}
````