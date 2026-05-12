---
title: bstr.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#581
source: crawler
fetched_at: 2026-05-06T21:34:45.559378498-03:00
rendered_js: false
word_count: 2582
summary: This document defines the ByteString type, an owned, growable container for byte sequences that are intended to be human-readable but not strictly enforced as UTF-8.
tags:
    - rust
    - bytestring
    - data-structures
    - memory-management
    - unicode
    - bytestr
category: reference
---

## alloc/ bstr.rs

```rust
1//! The `ByteStr` and `ByteString` types and trait implementations.
2
3// This could be more fine-grained.
4#![cfg(not(no_global_oom_handling))]
5
6use core::borrow::{Borrow, BorrowMut};
7#[unstable(feature = "bstr", issue = "134915")]
8pub use core::bstr::ByteStr;
9use core::bstr::{impl_partial_eq, impl_partial_eq_n, impl_partial_eq_ord};
10use core::cmp::Ordering;
11use core::ops::{
12    Deref, DerefMut, DerefPure, Index, IndexMut, Range, RangeFrom, RangeFull, RangeInclusive,
13    RangeTo, RangeToInclusive,
14};
15use core::str::FromStr;
16use core::{fmt, hash};
17
18use crate::borrow::{Cow, ToOwned};
19use crate::boxed::Box;
20#[cfg(not(no_rc))]
21use crate::rc::Rc;
22use crate::string::String;
23#[cfg(all(not(no_rc), not(no_sync), target_has_atomic = "ptr"))]
24use crate::sync::Arc;
25use crate::vec::Vec;
26
27/// A wrapper for `Vec<u8>` representing a human-readable string that's conventionally, but not
28/// always, UTF-8.
29///
30/// Unlike `String`, this type permits non-UTF-8 contents, making it suitable for user input,
31/// non-native filenames (as `Path` only supports native filenames), and other applications that
32/// need to round-trip whatever data the user provides.
33///
34/// A `ByteString` owns its contents and can grow and shrink, like a `Vec` or `String`. For a
35/// borrowed byte string, see [`ByteStr`](../../std/bstr/struct.ByteStr.html).
36///
37/// `ByteString` implements `Deref` to `&Vec<u8>`, so all methods available on `&Vec<u8>` are
38/// available on `ByteString`. Similarly, `ByteString` implements `DerefMut` to `&mut Vec<u8>`,
39/// so you can modify a `ByteString` using any method available on `&mut Vec<u8>`.
40///
41/// The `Debug` and `Display` implementations for `ByteString` are the same as those for `ByteStr`,
42/// showing invalid UTF-8 as hex escapes or the Unicode replacement character, respectively.
43#[unstable(feature = "bstr", issue = "134915")]
44#[repr(transparent)]
45#[derive(Clone)]
46#[doc(alias = "BString")]
47pub struct ByteString(pub Vec<u8>);
48
49impl ByteString {
50    #[inline]
51    pub(crate) fn as_bytes(&self) -> &[u8] {
52        &self.0
53    }
54
55    #[inline]
56    pub(crate) fn as_bytestr(&self) -> &ByteStr {
57        ByteStr::new(&self.0)
58    }
59
60    #[inline]
61    pub(crate) fn as_mut_bytestr(&mut self) -> &mut ByteStr {
62        ByteStr::from_bytes_mut(&mut self.0)
63    }
64}
65
66#[unstable(feature = "bstr", issue = "134915")]
67impl Deref for ByteString {
68    type Target = Vec<u8>;
69
70    #[inline]
71    fn deref(&self) -> &Self::Target {
72        &self.0
73    }
74}
75
76#[unstable(feature = "bstr", issue = "134915")]
77impl DerefMut for ByteString {
78    #[inline]
79    fn deref_mut(&mut self) -> &mut Self::Target {
80        &mut self.0
81    }
82}
83
84#[unstable(feature = "deref_pure_trait", issue = "87121")]
85unsafe impl DerefPure for ByteString {}
86
87#[unstable(feature = "bstr", issue = "134915")]
88impl fmt::Debug for ByteString {
89    #[inline]
90    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
91        fmt::Debug::fmt(self.as_bytestr(), f)
92    }
93}
94
95#[unstable(feature = "bstr", issue = "134915")]
96impl fmt::Display for ByteString {
97    #[inline]
98    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
99        fmt::Display::fmt(self.as_bytestr(), f)
100    }
101}
102
103#[unstable(feature = "bstr", issue = "134915")]
104impl AsRef<[u8]> for ByteString {
105    #[inline]
106    fn as_ref(&self) -> &[u8] {
107        &self.0
108    }
109}
110
111#[unstable(feature = "bstr", issue = "134915")]
112impl AsRef<ByteStr> for ByteString {
113    #[inline]
114    fn as_ref(&self) -> &ByteStr {
115        self.as_bytestr()
116    }
117}
118
119#[unstable(feature = "bstr", issue = "134915")]
120impl AsMut<[u8]> for ByteString {
121    #[inline]
122    fn as_mut(&mut self) -> &mut [u8] {
123        &mut self.0
124    }
125}
126
127#[unstable(feature = "bstr", issue = "134915")]
128impl AsMut<ByteStr> for ByteString {
129    #[inline]
130    fn as_mut(&mut self) -> &mut ByteStr {
131        self.as_mut_bytestr()
132    }
133}
134
135#[unstable(feature = "bstr", issue = "134915")]
136impl Borrow<[u8]> for ByteString {
137    #[inline]
138    fn borrow(&self) -> &[u8] {
139        &self.0
140    }
141}
142
143#[unstable(feature = "bstr", issue = "134915")]
144impl Borrow<ByteStr> for ByteString {
145    #[inline]
146    fn borrow(&self) -> &ByteStr {
147        self.as_bytestr()
148    }
149}
150
151// `impl Borrow<ByteStr> for Vec<u8>` omitted to avoid inference failures
152// `impl Borrow<ByteStr> for String` omitted to avoid inference failures
153
154#[unstable(feature = "bstr", issue = "134915")]
155impl BorrowMut<[u8]> for ByteString {
156    #[inline]
157    fn borrow_mut(&mut self) -> &mut [u8] {
158        &mut self.0
159    }
160}
161
162#[unstable(feature = "bstr", issue = "134915")]
163impl BorrowMut<ByteStr> for ByteString {
164    #[inline]
165    fn borrow_mut(&mut self) -> &mut ByteStr {
166        self.as_mut_bytestr()
167    }
168}
169
170// `impl BorrowMut<ByteStr> for Vec<u8>` omitted to avoid inference failures
171
172#[unstable(feature = "bstr", issue = "134915")]
173impl Default for ByteString {
174    fn default() -> Self {
175        ByteString(Vec::new())
176    }
177}
178
179// Omitted due to inference failures
180//
181// #[unstable(feature = "bstr", issue = "134915")]
182// impl<'a, const N: usize> From<&'a [u8; N]> for ByteString {
183//     #[inline]
184//     fn from(s: &'a [u8; N]) -> Self {
185//         ByteString(s.as_slice().to_vec())
186//     }
187// }
188//
189// #[unstable(feature = "bstr", issue = "134915")]
190// impl<const N: usize> From<[u8; N]> for ByteString {
191//     #[inline]
192//     fn from(s: [u8; N]) -> Self {
193//         ByteString(s.as_slice().to_vec())
194//     }
195// }
196//
197// #[unstable(feature = "bstr", issue = "134915")]
198// impl<'a> From<&'a [u8]> for ByteString {
199//     #[inline]
200//     fn from(s: &'a [u8]) -> Self {
201//         ByteString(s.to_vec())
202//     }
203// }
204//
205// #[unstable(feature = "bstr", issue = "134915")]
206// impl From<Vec<u8>> for ByteString {
207//     #[inline]
208//     fn from(s: Vec<u8>) -> Self {
209//         ByteString(s)
210//     }
211// }
212
213#[unstable(feature = "bstr", issue = "134915")]
214impl From<ByteString> for Vec<u8> {
215    #[inline]
216    fn from(s: ByteString) -> Self {
217        s.0
218    }
219}
220
221// Omitted due to inference failures
222//
223// #[unstable(feature = "bstr", issue = "134915")]
224// impl<'a> From<&'a str> for ByteString {
225//     #[inline]
226//     fn from(s: &'a str) -> Self {
227//         ByteString(s.as_bytes().to_vec())
228//     }
229// }
230//
231// #[unstable(feature = "bstr", issue = "134915")]
232// impl From<String> for ByteString {
233//     #[inline]
234//     fn from(s: String) -> Self {
235//         ByteString(s.into_bytes())
236//     }
237// }
238
239#[unstable(feature = "bstr", issue = "134915")]
240impl<'a> From<&'a ByteStr> for ByteString {
241    #[inline]
242    fn from(s: &'a ByteStr) -> Self {
243        ByteString(s.0.to_vec())
244    }
245}
246
247#[unstable(feature = "bstr", issue = "134915")]
248impl<'a> From<ByteString> for Cow<'a, ByteStr> {
249    #[inline]
250    fn from(s: ByteString) -> Self {
251        Cow::Owned(s)
252    }
253}
254
255#[unstable(feature = "bstr", issue = "134915")]
256impl<'a> From<&'a ByteString> for Cow<'a, ByteStr> {
257    #[inline]
258    fn from(s: &'a ByteString) -> Self {
259        Cow::Borrowed(s.as_bytestr())
260    }
261}
262
263#[unstable(feature = "bstr", issue = "134915")]
264impl FromIterator<char> for ByteString {
265    #[inline]
266    fn from_iter<T: IntoIterator<Item = char>>(iter: T) -> Self {
267        ByteString(iter.into_iter().collect::<String>().into_bytes())
268    }
269}
270
271#[unstable(feature = "bstr", issue = "134915")]
272impl FromIterator<u8> for ByteString {
273    #[inline]
274    fn from_iter<T: IntoIterator<Item = u8>>(iter: T) -> Self {
275        ByteString(iter.into_iter().collect())
276    }
277}
278
279#[unstable(feature = "bstr", issue = "134915")]
280impl<'a> FromIterator<&'a str> for ByteString {
281    #[inline]
282    fn from_iter<T: IntoIterator<Item = &'a str>>(iter: T) -> Self {
283        ByteString(iter.into_iter().collect::<String>().into_bytes())
284    }
285}
286
287#[unstable(feature = "bstr", issue = "134915")]
288impl<'a> FromIterator<&'a [u8]> for ByteString {
289    #[inline]
290    fn from_iter<T: IntoIterator<Item = &'a [u8]>>(iter: T) -> Self {
291        let mut buf = Vec::new();
292        for b in iter {
293            buf.extend_from_slice(b);
294        }
295        ByteString(buf)
296    }
297}
298
299#[unstable(feature = "bstr", issue = "134915")]
300impl<'a> FromIterator<&'a ByteStr> for ByteString {
301    #[inline]
302    fn from_iter<T: IntoIterator<Item = &'a ByteStr>>(iter: T) -> Self {
303        let mut buf = Vec::new();
304        for b in iter {
305            buf.extend_from_slice(&b.0);
306        }
307        ByteString(buf)
308    }
309}
310
311#[unstable(feature = "bstr", issue = "134915")]
312impl FromIterator<ByteString> for ByteString {
313    #[inline]
314    fn from_iter<T: IntoIterator<Item = ByteString>>(iter: T) -> Self {
315        let mut buf = Vec::new();
316        for mut b in iter {
317            buf.append(&mut b.0);
318        }
319        ByteString(buf)
320    }
321}
322
323#[unstable(feature = "bstr", issue = "134915")]
324impl FromStr for ByteString {
325    type Err = core::convert::Infallible;
326
327    #[inline]
328    fn from_str(s: &str) -> Result<Self, Self::Err> {
329        Ok(ByteString(s.as_bytes().to_vec()))
330    }
331}
332
333#[unstable(feature = "bstr", issue = "134915")]
334impl Index<usize> for ByteString {
335    type Output = u8;
336
337    #[inline]
338    fn index(&self, idx: usize) -> &u8 {
339        &self.0[idx]
340    }
341}
342
343#[unstable(feature = "bstr", issue = "134915")]
344impl Index<RangeFull> for ByteString {
345    type Output = ByteStr;
346
347    #[inline]
348    fn index(&self, _: RangeFull) -> &ByteStr {
349        self.as_bytestr()
350    }
351}
352
353#[unstable(feature = "bstr", issue = "134915")]
354impl Index<Range<usize>> for ByteString {
355    type Output = ByteStr;
356
357    #[inline]
358    fn index(&self, r: Range<usize>) -> &ByteStr {
359        ByteStr::from_bytes(&self.0[r])
360    }
361}
362
363#[unstable(feature = "bstr", issue = "134915")]
364impl Index<RangeInclusive<usize>> for ByteString {
365    type Output = ByteStr;
366
367    #[inline]
368    fn index(&self, r: RangeInclusive<usize>) -> &ByteStr {
369        ByteStr::from_bytes(&self.0[r])
370    }
371}
372
373#[unstable(feature = "bstr", issue = "134915")]
374impl Index<RangeFrom<usize>> for ByteString {
375    type Output = ByteStr;
376
377    #[inline]
378    fn index(&self, r: RangeFrom<usize>) -> &ByteStr {
379        ByteStr::from_bytes(&self.0[r])
380    }
381}
382
383#[unstable(feature = "bstr", issue = "134915")]
384impl Index<RangeTo<usize>> for ByteString {
385    type Output = ByteStr;
386
387    #[inline]
388    fn index(&self, r: RangeTo<usize>) -> &ByteStr {
389        ByteStr::from_bytes(&self.0[r])
390    }
391}
392
393#[unstable(feature = "bstr", issue = "134915")]
394impl Index<RangeToInclusive<usize>> for ByteString {
395    type Output = ByteStr;
396
397    #[inline]
398    fn index(&self, r: RangeToInclusive<usize>) -> &ByteStr {
399        ByteStr::from_bytes(&self.0[r])
400    }
401}
402
403#[unstable(feature = "bstr", issue = "134915")]
404impl IndexMut<usize> for ByteString {
405    #[inline]
406    fn index_mut(&mut self, idx: usize) -> &mut u8 {
407        &mut self.0[idx]
408    }
409}
410
411#[unstable(feature = "bstr", issue = "134915")]
412impl IndexMut<RangeFull> for ByteString {
413    #[inline]
414    fn index_mut(&mut self, _: RangeFull) -> &mut ByteStr {
415        self.as_mut_bytestr()
416    }
417}
418
419#[unstable(feature = "bstr", issue = "134915")]
420impl IndexMut<Range<usize>> for ByteString {
421    #[inline]
422    fn index_mut(&mut self, r: Range<usize>) -> &mut ByteStr {
423        ByteStr::from_bytes_mut(&mut self.0[r])
424    }
425}
426
427#[unstable(feature = "bstr", issue = "134915")]
428impl IndexMut<RangeInclusive<usize>> for ByteString {
429    #[inline]
430    fn index_mut(&mut self, r: RangeInclusive<usize>) -> &mut ByteStr {
431        ByteStr::from_bytes_mut(&mut self.0[r])
432    }
433}
434
435#[unstable(feature = "bstr", issue = "134915")]
436impl IndexMut<RangeFrom<usize>> for ByteString {
437    #[inline]
438    fn index_mut(&mut self, r: RangeFrom<usize>) -> &mut ByteStr {
439        ByteStr::from_bytes_mut(&mut self.0[r])
440    }
441}
442
443#[unstable(feature = "bstr", issue = "134915")]
444impl IndexMut<RangeTo<usize>> for ByteString {
445    #[inline]
446    fn index_mut(&mut self, r: RangeTo<usize>) -> &mut ByteStr {
447        ByteStr::from_bytes_mut(&mut self.0[r])
448    }
449}
450
451#[unstable(feature = "bstr", issue = "134915")]
452impl IndexMut<RangeToInclusive<usize>> for ByteString {
453    #[inline]
454    fn index_mut(&mut self, r: RangeToInclusive<usize>) -> &mut ByteStr {
455        ByteStr::from_bytes_mut(&mut self.0[r])
456    }
457}
458
459#[unstable(feature = "bstr", issue = "134915")]
460impl hash::Hash for ByteString {
461    #[inline]
462    fn hash<H: hash::Hasher>(&self, state: &mut H) {
463        self.0.hash(state);
464    }
465}
466
467#[unstable(feature = "bstr", issue = "134915")]
468impl Eq for ByteString {}
469
470#[unstable(feature = "bstr", issue = "134915")]
471impl PartialEq for ByteString {
472    #[inline]
473    fn eq(&self, other: &ByteString) -> bool {
474        self.0 == other.0
475    }
476}
477
478macro_rules! impl_partial_eq_ord_cow {
479    ($lhs:ty, $rhs:ty) => {
480        #[unstable(feature = "bstr", issue = "134915")]
481        impl PartialEq<$rhs> for $lhs {
482            #[inline]
483            fn eq(&self, other: &$rhs) -> bool {
484                let other: &[u8] = (&**other).as_ref();
485                PartialEq::eq(self.as_bytes(), other)
486            }
487        }
488
489        #[unstable(feature = "bstr", issue = "134915")]
490        impl PartialEq<$lhs> for $rhs {
491            #[inline]
492            fn eq(&self, other: &$lhs) -> bool {
493                let this: &[u8] = (&**self).as_ref();
494                PartialEq::eq(this, other.as_bytes())
495            }
496        }
497
498        #[unstable(feature = "bstr", issue = "134915")]
499        impl PartialOrd<$rhs> for $lhs {
500            #[inline]
501            fn partial_cmp(&self, other: &$rhs) -> Option<Ordering> {
502                let other: &[u8] = (&**other).as_ref();
503                PartialOrd::partial_cmp(self.as_bytes(), other)
504            }
505        }
506
507        #[unstable(feature = "bstr", issue = "134915")]
508        impl PartialOrd<$lhs> for $rhs {
509            #[inline]
510            fn partial_cmp(&self, other: &$lhs) -> Option<Ordering> {
511                let this: &[u8] = (&**self).as_ref();
512                PartialOrd::partial_cmp(this, other.as_bytes())
513            }
514        }
515    };
516}
517
518// PartialOrd with `Vec<u8>` omitted to avoid inference failures
519impl_partial_eq!(ByteString, Vec<u8>);
520// PartialOrd with `[u8]` omitted to avoid inference failures
521impl_partial_eq!(ByteString, [u8]);
522// PartialOrd with `&[u8]` omitted to avoid inference failures
523impl_partial_eq!(ByteString, &[u8]);
524// PartialOrd with `String` omitted to avoid inference failures
525impl_partial_eq!(ByteString, String);
526// PartialOrd with `str` omitted to avoid inference failures
527impl_partial_eq!(ByteString, str);
528// PartialOrd with `&str` omitted to avoid inference failures
529impl_partial_eq!(ByteString, &str);
530impl_partial_eq_ord!(ByteString, ByteStr);
531impl_partial_eq_ord!(ByteString, &ByteStr);
532// PartialOrd with `[u8; N]` omitted to avoid inference failures
533impl_partial_eq_n!(ByteString, [u8; N]);
534// PartialOrd with `&[u8; N]` omitted to avoid inference failures
535impl_partial_eq_n!(ByteString, &[u8; N]);
536impl_partial_eq_ord_cow!(ByteString, Cow<'_, ByteStr>);
537impl_partial_eq_ord_cow!(ByteString, Cow<'_, str>);
538impl_partial_eq_ord_cow!(ByteString, Cow<'_, [u8]>);
539
540#[unstable(feature = "bstr", issue = "134915")]
541impl Ord for ByteString {
542    #[inline]
543    fn cmp(&self, other: &ByteString) -> Ordering {
544        Ord::cmp(&self.0, &other.0)
545    }
546}
547
548#[unstable(feature = "bstr", issue = "134915")]
549impl PartialOrd for ByteString {
550    #[inline]
551    fn partial_cmp(&self, other: &ByteString) -> Option<Ordering> {
552        PartialOrd::partial_cmp(&self.0, &other.0)
553    }
554}
555
556#[unstable(feature = "bstr", issue = "134915")]
557impl ToOwned for ByteStr {
558    type Owned = ByteString;
559
560    #[inline]
561    fn to_owned(&self) -> ByteString {
562        ByteString(self.0.to_vec())
563    }
564}
565
566#[unstable(feature = "bstr", issue = "134915")]
567impl TryFrom<ByteString> for String {
568    type Error = crate::string::FromUtf8Error;
569
570    #[inline]
571    fn try_from(s: ByteString) -> Result<Self, Self::Error> {
572        String::from_utf8(s.0)
573    }
574}
575
576#[unstable(feature = "bstr", issue = "134915")]
577impl<'a> TryFrom<&'a ByteString> for &'a str {
578    type Error = crate::str::Utf8Error;
579
580    #[inline]
581    fn try_from(s: &'a ByteString) -> Result<Self, Self::Error> {
582        crate::str::from_utf8(s.0.as_slice())
583    }
584}
585
586// Additional impls for `ByteStr` that require types from `alloc`:
587
588#[unstable(feature = "bstr", issue = "134915")]
589impl Clone for Box<ByteStr> {
590    #[inline]
591    fn clone(&self) -> Self {
592        Self::from(Box::<[u8]>::from(&self.0))
593    }
594}
595
596#[unstable(feature = "bstr", issue = "134915")]
597impl<'a> From<&'a ByteStr> for Cow<'a, ByteStr> {
598    #[inline]
599    fn from(s: &'a ByteStr) -> Self {
600        Cow::Borrowed(s)
601    }
602}
603
604#[unstable(feature = "bstr", issue = "134915")]
605impl From<Box<[u8]>> for Box<ByteStr> {
606    #[inline]
607    fn from(s: Box<[u8]>) -> Box<ByteStr> {
608        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
609        unsafe { Box::from_raw(Box::into_raw(s) as _) }
610    }
611}
612
613#[unstable(feature = "bstr", issue = "134915")]
614impl From<Box<ByteStr>> for Box<[u8]> {
615    #[inline]
616    fn from(s: Box<ByteStr>) -> Box<[u8]> {
617        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
618        unsafe { Box::from_raw(Box::into_raw(s) as _) }
619    }
620}
621
622#[unstable(feature = "bstr", issue = "134915")]
623#[cfg(not(no_rc))]
624impl From<Rc<[u8]>> for Rc<ByteStr> {
625    #[inline]
626    fn from(s: Rc<[u8]>) -> Rc<ByteStr> {
627        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
628        unsafe { Rc::from_raw(Rc::into_raw(s) as _) }
629    }
630}
631
632#[unstable(feature = "bstr", issue = "134915")]
633#[cfg(not(no_rc))]
634impl From<Rc<ByteStr>> for Rc<[u8]> {
635    #[inline]
636    fn from(s: Rc<ByteStr>) -> Rc<[u8]> {
637        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
638        unsafe { Rc::from_raw(Rc::into_raw(s) as _) }
639    }
640}
641
642#[unstable(feature = "bstr", issue = "134915")]
643#[cfg(all(not(no_rc), not(no_sync), target_has_atomic = "ptr"))]
644impl From<Arc<[u8]>> for Arc<ByteStr> {
645    #[inline]
646    fn from(s: Arc<[u8]>) -> Arc<ByteStr> {
647        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
648        unsafe { Arc::from_raw(Arc::into_raw(s) as _) }
649    }
650}
651
652#[unstable(feature = "bstr", issue = "134915")]
653#[cfg(all(not(no_rc), not(no_sync), target_has_atomic = "ptr"))]
654impl From<Arc<ByteStr>> for Arc<[u8]> {
655    #[inline]
656    fn from(s: Arc<ByteStr>) -> Arc<[u8]> {
657        // SAFETY: `ByteStr` is a transparent wrapper around `[u8]`.
658        unsafe { Arc::from_raw(Arc::into_raw(s) as _) }
659    }
660}
661
662// PartialOrd with `Vec<u8>` omitted to avoid inference failures
663impl_partial_eq!(ByteStr, Vec<u8>);
664// PartialOrd with `String` omitted to avoid inference failures
665impl_partial_eq!(ByteStr, String);
666impl_partial_eq_ord_cow!(&ByteStr, Cow<'_, ByteStr>);
667impl_partial_eq_ord_cow!(&ByteStr, Cow<'_, str>);
668impl_partial_eq_ord_cow!(&ByteStr, Cow<'_, [u8]>);
669
670#[unstable(feature = "bstr", issue = "134915")]
671impl<'a> TryFrom<&'a ByteStr> for String {
672    type Error = core::str::Utf8Error;
673
674    #[inline]
675    fn try_from(s: &'a ByteStr) -> Result<Self, Self::Error> {
676        Ok(core::str::from_utf8(&s.0)?.into())
677    }
678}
```