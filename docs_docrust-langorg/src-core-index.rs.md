---
title: index.rs - source
url: https://doc.rust-lang.org/src/core/index.rs.html#442
source: crawler
fetched_at: 2026-05-06T21:38:34.769109786-03:00
rendered_js: false
word_count: 2138
summary: This document defines helper wrappers for Rust slices that provide clamped indexing and access to the last element to prevent out-of-bounds errors.
tags:
    - rust
    - slice-indexing
    - clamping
    - memory-safety
    - wrapper-types
category: api
---

## core/ index.rs

````rust
1#![unstable(feature = "sliceindex_wrappers", issue = "146179")]
2
3//! Helper types for indexing slices.
4
5use crate::intrinsics::slice_get_unchecked;
6use crate::slice::SliceIndex;
7use crate::{cmp, ops, range};
8
9/// Clamps an index, guaranteeing that it will only access valid elements of the slice.
10///
11/// # Examples
12///
13/// ```
14/// #![feature(sliceindex_wrappers)]
15///
16/// use core::index::Clamp;
17///
18/// let s: &[usize] = &[0, 1, 2, 3];
19///
20/// assert_eq!(&3, &s[Clamp(6)]);
21/// assert_eq!(&[1, 2, 3], &s[Clamp(1..6)]);
22/// assert_eq!(&[] as &[usize], &s[Clamp(5..6)]);
23/// assert_eq!(&[0, 1, 2, 3], &s[Clamp(..6)]);
24/// assert_eq!(&[0, 1, 2, 3], &s[Clamp(..=6)]);
25/// assert_eq!(&[] as &[usize], &s[Clamp(6..)]);
26/// ```
27#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
28#[derive(Debug)]
29pub struct Clamp<Idx>(pub Idx);
30
31/// Always accesses the last element of the slice.
32///
33/// # Examples
34///
35/// ```
36/// #![feature(sliceindex_wrappers)]
37/// #![feature(slice_index_methods)]
38///
39/// use core::index::Last;
40/// use core::slice::SliceIndex;
41///
42/// let s = &[0, 1, 2, 3];
43///
44/// assert_eq!(&3, &s[Last]);
45/// assert_eq!(None, Last.get(&[] as &[usize]));
46///
47/// ```
48#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
49#[derive(Debug)]
50pub struct Last;
51
52#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
53unsafe impl<T> SliceIndex<[T]> for Clamp<usize> {
54    type Output = T;
55
56    fn get(self, slice: &[T]) -> Option<&Self::Output> {
57        slice.get(cmp::min(self.0, slice.len() - 1))
58    }
59
60    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
61        slice.get_mut(cmp::min(self.0, slice.len() - 1))
62    }
63
64    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
65        // SAFETY: the caller ensures that the slice isn't empty
66        unsafe { slice_get_unchecked(slice, cmp::min(self.0, slice.len() - 1)) }
67    }
68
69    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
70        // SAFETY: the caller ensures that the slice isn't empty
71        unsafe { slice_get_unchecked(slice, cmp::min(self.0, slice.len() - 1)) }
72    }
73
74    fn index(self, slice: &[T]) -> &Self::Output {
75        &(*slice)[cmp::min(self.0, slice.len() - 1)]
76    }
77
78    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
79        &mut (*slice)[cmp::min(self.0, slice.len() - 1)]
80    }
81}
82
83#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
84unsafe impl<T> SliceIndex<[T]> for Clamp<range::Range<usize>> {
85    type Output = [T];
86
87    fn get(self, slice: &[T]) -> Option<&Self::Output> {
88        let start = cmp::min(self.0.start, slice.len());
89        let end = cmp::min(self.0.end, slice.len());
90        (start..end).get(slice)
91    }
92
93    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
94        let start = cmp::min(self.0.start, slice.len());
95        let end = cmp::min(self.0.end, slice.len());
96        (start..end).get_mut(slice)
97    }
98
99    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
100        let start = cmp::min(self.0.start, slice.len());
101        let end = cmp::min(self.0.end, slice.len());
102        // SAFETY: a range ending before len is always valid
103        unsafe { (start..end).get_unchecked(slice) }
104    }
105
106    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
107        let start = cmp::min(self.0.start, slice.len());
108        let end = cmp::min(self.0.end, slice.len());
109        // SAFETY: a range ending before len is always valid
110        unsafe { (start..end).get_unchecked_mut(slice) }
111    }
112
113    fn index(self, slice: &[T]) -> &Self::Output {
114        let start = cmp::min(self.0.start, slice.len());
115        let end = cmp::min(self.0.end, slice.len());
116        (start..end).index(slice)
117    }
118
119    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
120        let start = cmp::min(self.0.start, slice.len());
121        let end = cmp::min(self.0.end, slice.len());
122        (start..end).index_mut(slice)
123    }
124}
125
126#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
127unsafe impl<T> SliceIndex<[T]> for Clamp<ops::Range<usize>> {
128    type Output = [T];
129
130    fn get(self, slice: &[T]) -> Option<&Self::Output> {
131        let start = cmp::min(self.0.start, slice.len());
132        let end = cmp::min(self.0.end, slice.len());
133        (start..end).get(slice)
134    }
135
136    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
137        let start = cmp::min(self.0.start, slice.len());
138        let end = cmp::min(self.0.end, slice.len());
139        (start..end).get_mut(slice)
140    }
141
142    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
143        let start = cmp::min(self.0.start, slice.len());
144        let end = cmp::min(self.0.end, slice.len());
145        // SAFETY: a range ending before len is always valid
146        unsafe { (start..end).get_unchecked(slice) }
147    }
148
149    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
150        let start = cmp::min(self.0.start, slice.len());
151        let end = cmp::min(self.0.end, slice.len());
152        // SAFETY: a range ending before len is always valid
153        unsafe { (start..end).get_unchecked_mut(slice) }
154    }
155
156    fn index(self, slice: &[T]) -> &Self::Output {
157        let start = cmp::min(self.0.start, slice.len());
158        let end = cmp::min(self.0.end, slice.len());
159        (start..end).index(slice)
160    }
161
162    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
163        let start = cmp::min(self.0.start, slice.len());
164        let end = cmp::min(self.0.end, slice.len());
165        (start..end).index_mut(slice)
166    }
167}
168
169#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
170unsafe impl<T> SliceIndex<[T]> for Clamp<range::RangeInclusive<usize>> {
171    type Output = [T];
172
173    fn get(self, slice: &[T]) -> Option<&Self::Output> {
174        let start = cmp::min(self.0.start, slice.len() - 1);
175        let end = cmp::min(self.0.last, slice.len() - 1);
176        (start..=end).get(slice)
177    }
178
179    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
180        let start = cmp::min(self.0.start, slice.len() - 1);
181        let end = cmp::min(self.0.last, slice.len() - 1);
182        (start..=end).get_mut(slice)
183    }
184
185    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
186        let start = cmp::min(self.0.start, slice.len() - 1);
187        let end = cmp::min(self.0.last, slice.len() - 1);
188        // SAFETY: the caller ensures that the slice isn't empty
189        unsafe { (start..=end).get_unchecked(slice) }
190    }
191
192    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
193        let start = cmp::min(self.0.start, slice.len() - 1);
194        let end = cmp::min(self.0.last, slice.len() - 1);
195        // SAFETY: the caller ensures that the slice isn't empty
196        unsafe { (start..=end).get_unchecked_mut(slice) }
197    }
198
199    fn index(self, slice: &[T]) -> &Self::Output {
200        let start = cmp::min(self.0.start, slice.len() - 1);
201        let end = cmp::min(self.0.last, slice.len() - 1);
202        (start..=end).index(slice)
203    }
204
205    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
206        let start = cmp::min(self.0.start, slice.len() - 1);
207        let end = cmp::min(self.0.last, slice.len() - 1);
208        (start..=end).index_mut(slice)
209    }
210}
211
212#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
213unsafe impl<T> SliceIndex<[T]> for Clamp<ops::RangeInclusive<usize>> {
214    type Output = [T];
215
216    fn get(self, slice: &[T]) -> Option<&Self::Output> {
217        let start = cmp::min(self.0.start, slice.len() - 1);
218        let end = cmp::min(self.0.end, slice.len() - 1);
219        (start..=end).get(slice)
220    }
221
222    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
223        let start = cmp::min(self.0.start, slice.len() - 1);
224        let end = cmp::min(self.0.end, slice.len() - 1);
225        (start..=end).get_mut(slice)
226    }
227
228    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
229        let start = cmp::min(self.0.start, slice.len() - 1);
230        let end = cmp::min(self.0.end, slice.len() - 1);
231        // SAFETY: the caller ensures that the slice isn't empty
232        unsafe { (start..=end).get_unchecked(slice) }
233    }
234
235    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
236        let start = cmp::min(self.0.start, slice.len() - 1);
237        let end = cmp::min(self.0.end, slice.len() - 1);
238        // SAFETY: the caller ensures that the slice isn't empty
239        unsafe { (start..=end).get_unchecked_mut(slice) }
240    }
241
242    fn index(self, slice: &[T]) -> &Self::Output {
243        let start = cmp::min(self.0.start, slice.len() - 1);
244        let end = cmp::min(self.0.end, slice.len() - 1);
245        (start..=end).index(slice)
246    }
247
248    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
249        let start = cmp::min(self.0.start, slice.len() - 1);
250        let end = cmp::min(self.0.end, slice.len() - 1);
251        (start..=end).index_mut(slice)
252    }
253}
254
255#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
256unsafe impl<T> SliceIndex<[T]> for Clamp<range::RangeFrom<usize>> {
257    type Output = [T];
258
259    fn get(self, slice: &[T]) -> Option<&Self::Output> {
260        (cmp::min(self.0.start, slice.len())..).get(slice)
261    }
262
263    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
264        (cmp::min(self.0.start, slice.len())..).get_mut(slice)
265    }
266
267    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
268        // SAFETY: a range starting at len is valid
269        unsafe { (cmp::min(self.0.start, slice.len())..).get_unchecked(slice) }
270    }
271
272    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
273        // SAFETY: a range starting at len is valid
274        unsafe { (cmp::min(self.0.start, slice.len())..).get_unchecked_mut(slice) }
275    }
276
277    fn index(self, slice: &[T]) -> &Self::Output {
278        (cmp::min(self.0.start, slice.len())..).index(slice)
279    }
280
281    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
282        (cmp::min(self.0.start, slice.len())..).index_mut(slice)
283    }
284}
285
286#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
287unsafe impl<T> SliceIndex<[T]> for Clamp<ops::RangeFrom<usize>> {
288    type Output = [T];
289
290    fn get(self, slice: &[T]) -> Option<&Self::Output> {
291        (cmp::min(self.0.start, slice.len())..).get(slice)
292    }
293
294    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
295        (cmp::min(self.0.start, slice.len())..).get_mut(slice)
296    }
297
298    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
299        // SAFETY: a range starting at len is valid
300        unsafe { (cmp::min(self.0.start, slice.len())..).get_unchecked(slice) }
301    }
302
303    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
304        // SAFETY: a range starting at len is valid
305        unsafe { (cmp::min(self.0.start, slice.len())..).get_unchecked_mut(slice) }
306    }
307
308    fn index(self, slice: &[T]) -> &Self::Output {
309        (cmp::min(self.0.start, slice.len())..).index(slice)
310    }
311
312    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
313        (cmp::min(self.0.start, slice.len())..).index_mut(slice)
314    }
315}
316
317#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
318unsafe impl<T> SliceIndex<[T]> for Clamp<ops::RangeTo<usize>> {
319    type Output = [T];
320
321    fn get(self, slice: &[T]) -> Option<&Self::Output> {
322        (..cmp::min(self.0.end, slice.len())).get(slice)
323    }
324
325    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
326        (..cmp::min(self.0.end, slice.len())).get_mut(slice)
327    }
328
329    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
330        // SAFETY: a range ending before len is always valid
331        unsafe { (..cmp::min(self.0.end, slice.len())).get_unchecked(slice) }
332    }
333
334    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
335        // SAFETY: a range ending before len is always valid
336        unsafe { (..cmp::min(self.0.end, slice.len())).get_unchecked_mut(slice) }
337    }
338
339    fn index(self, slice: &[T]) -> &Self::Output {
340        (..cmp::min(self.0.end, slice.len())).index(slice)
341    }
342
343    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
344        (..cmp::min(self.0.end, slice.len())).index_mut(slice)
345    }
346}
347
348#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
349unsafe impl<T> SliceIndex<[T]> for Clamp<range::RangeToInclusive<usize>> {
350    type Output = [T];
351
352    fn get(self, slice: &[T]) -> Option<&Self::Output> {
353        (..=cmp::min(self.0.last, slice.len() - 1)).get(slice)
354    }
355
356    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
357        (..=cmp::min(self.0.last, slice.len() - 1)).get_mut(slice)
358    }
359
360    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
361        // SAFETY: the caller ensures that the slice isn't empty
362        unsafe { (..=cmp::min(self.0.last, slice.len() - 1)).get_unchecked(slice) }
363    }
364
365    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
366        // SAFETY: the caller ensures that the slice isn't empty
367        unsafe { (..=cmp::min(self.0.last, slice.len() - 1)).get_unchecked_mut(slice) }
368    }
369
370    fn index(self, slice: &[T]) -> &Self::Output {
371        (..=cmp::min(self.0.last, slice.len() - 1)).index(slice)
372    }
373
374    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
375        (..=cmp::min(self.0.last, slice.len() - 1)).index_mut(slice)
376    }
377}
378
379#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
380unsafe impl<T> SliceIndex<[T]> for Clamp<ops::RangeToInclusive<usize>> {
381    type Output = [T];
382
383    fn get(self, slice: &[T]) -> Option<&Self::Output> {
384        (..=cmp::min(self.0.end, slice.len() - 1)).get(slice)
385    }
386
387    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
388        (..=cmp::min(self.0.end, slice.len() - 1)).get_mut(slice)
389    }
390
391    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
392        // SAFETY: the caller ensures that the slice isn't empty
393        unsafe { (..=cmp::min(self.0.end, slice.len() - 1)).get_unchecked(slice) }
394    }
395
396    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
397        // SAFETY: the caller ensures that the slice isn't empty
398        unsafe { (..=cmp::min(self.0.end, slice.len() - 1)).get_unchecked_mut(slice) }
399    }
400
401    fn index(self, slice: &[T]) -> &Self::Output {
402        (..=cmp::min(self.0.end, slice.len() - 1)).index(slice)
403    }
404
405    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
406        (..=cmp::min(self.0.end, slice.len() - 1)).index_mut(slice)
407    }
408}
409
410#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
411unsafe impl<T> SliceIndex<[T]> for Clamp<ops::RangeFull> {
412    type Output = [T];
413
414    fn get(self, slice: &[T]) -> Option<&Self::Output> {
415        (..).get(slice)
416    }
417
418    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
419        (..).get_mut(slice)
420    }
421
422    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
423        // SAFETY: RangeFull just returns `slice` here
424        unsafe { (..).get_unchecked(slice) }
425    }
426
427    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
428        // SAFETY: RangeFull just returns `slice` here
429        unsafe { (..).get_unchecked_mut(slice) }
430    }
431
432    fn index(self, slice: &[T]) -> &Self::Output {
433        (..).index(slice)
434    }
435
436    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
437        (..).index_mut(slice)
438    }
439}
440
441#[unstable(feature = "sliceindex_wrappers", issue = "146179")]
442unsafe impl<T> SliceIndex<[T]> for Last {
443    type Output = T;
444
445    fn get(self, slice: &[T]) -> Option<&Self::Output> {
446        slice.last()
447    }
448
449    fn get_mut(self, slice: &mut [T]) -> Option<&mut Self::Output> {
450        slice.last_mut()
451    }
452
453    unsafe fn get_unchecked(self, slice: *const [T]) -> *const Self::Output {
454        // SAFETY: the caller ensures that the slice isn't empty
455        unsafe { slice_get_unchecked(slice, slice.len() - 1) }
456    }
457
458    unsafe fn get_unchecked_mut(self, slice: *mut [T]) -> *mut Self::Output {
459        // SAFETY: the caller ensures that the slice isn't empty
460        unsafe { slice_get_unchecked(slice, slice.len() - 1) }
461    }
462
463    fn index(self, slice: &[T]) -> &Self::Output {
464        // N.B., use intrinsic indexing
465        &(*slice)[slice.len() - 1]
466    }
467
468    fn index_mut(self, slice: &mut [T]) -> &mut Self::Output {
469        // N.B., use intrinsic indexing
470        &mut (*slice)[slice.len() - 1]
471    }
472}
````