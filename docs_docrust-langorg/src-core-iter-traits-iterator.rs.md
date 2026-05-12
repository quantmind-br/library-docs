---
title: iterator.rs - source
url: https://doc.rust-lang.org/src/core/iter/traits/iterator.rs.html#306
source: crawler
fetched_at: 2026-05-06T21:36:56.932515649-03:00
rendered_js: false
word_count: 16550
summary: This document defines the core Iterator trait in Rust, which provides a standard interface for sequential access to a collection of items.
tags:
    - rust
    - iterator
    - trait
    - functional-programming
    - generic-programming
    - core-library
category: reference
---

## core/iter/traits/ iterator.rs

````rust
1use super::super::{
2    ArrayChunks, ByRefSized, Chain, Cloned, Copied, Cycle, Enumerate, Filter, FilterMap, FlatMap,
3    Flatten, Fuse, Inspect, Intersperse, IntersperseWith, Map, MapWhile, MapWindows, Peekable,
4    Product, Rev, Scan, Skip, SkipWhile, StepBy, Sum, Take, TakeWhile, TrustedRandomAccessNoCoerce,
5    Zip, try_process,
6};
7use super::TrustedLen;
8use crate::array;
9use crate::cmp::{self, Ordering};
10use crate::num::NonZero;
11use crate::ops::{ChangeOutputType, ControlFlow, FromResidual, Residual, Try};
12
13fn _assert_is_dyn_compatible(_: &dyn Iterator<Item = ()>) {}
14
15/// A trait for dealing with iterators.
16///
17/// This is the main iterator trait. For more about the concept of iterators
18/// generally, please see the [module-level documentation]. In particular, you
19/// may want to know how to [implement `Iterator`][impl].
20///
21/// [module-level documentation]: crate::iter
22/// [impl]: crate::iter#implementing-iterator
23#[stable(feature = "rust1", since = "1.0.0")]
24#[rustc_on_unimplemented(
25    on(
26        Self = "core::ops::range::RangeTo<Idx>",
27        note = "you might have meant to use a bounded `Range`"
28    ),
29    on(
30        Self = "core::ops::range::RangeToInclusive<Idx>",
31        note = "you might have meant to use a bounded `RangeInclusive`"
32    ),
33    label = "`{Self}` is not an iterator",
34    message = "`{Self}` is not an iterator"
35)]
36#[doc(notable_trait)]
37#[lang = "iterator"]
38#[rustc_diagnostic_item = "Iterator"]
39#[must_use = "iterators are lazy and do nothing unless consumed"]
40#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
41pub const trait Iterator {
42    /// The type of the elements being iterated over.
43    #[rustc_diagnostic_item = "IteratorItem"]
44    #[stable(feature = "rust1", since = "1.0.0")]
45    type Item;
46
47    /// Advances the iterator and returns the next value.
48    ///
49    /// Returns [`None`] when iteration is finished. Individual iterator
50    /// implementations may choose to resume iteration, and so calling `next()`
51    /// again may or may not eventually start returning [`Some(Item)`] again at some
52    /// point.
53    ///
54    /// [`Some(Item)`]: Some
55    ///
56    /// # Examples
57    ///
58    /// ```
59    /// let a = [1, 2, 3];
60    ///
61    /// let mut iter = a.into_iter();
62    ///
63    /// // A call to next() returns the next value...
64    /// assert_eq!(Some(1), iter.next());
65    /// assert_eq!(Some(2), iter.next());
66    /// assert_eq!(Some(3), iter.next());
67    ///
68    /// // ... and then None once it's over.
69    /// assert_eq!(None, iter.next());
70    ///
71    /// // More calls may or may not return `None`. Here, they always will.
72    /// assert_eq!(None, iter.next());
73    /// assert_eq!(None, iter.next());
74    /// ```
75    #[lang = "next"]
76    #[stable(feature = "rust1", since = "1.0.0")]
77    fn next(&mut self) -> Option<Self::Item>;
78
79    /// Advances the iterator and returns an array containing the next `N` values.
80    ///
81    /// If there are not enough elements to fill the array then `Err` is returned
82    /// containing an iterator over the remaining elements.
83    ///
84    /// # Examples
85    ///
86    /// Basic usage:
87    ///
88    /// ```
89    /// #![feature(iter_next_chunk)]
90    ///
91    /// let mut iter = "lorem".chars();
92    ///
93    /// assert_eq!(iter.next_chunk().unwrap(), ['l', 'o']);              // N is inferred as 2
94    /// assert_eq!(iter.next_chunk().unwrap(), ['r', 'e', 'm']);         // N is inferred as 3
95    /// assert_eq!(iter.next_chunk::<4>().unwrap_err().as_slice(), &[]); // N is explicitly 4
96    /// ```
97    ///
98    /// Split a string and get the first three items.
99    ///
100    /// ```
101    /// #![feature(iter_next_chunk)]
102    ///
103    /// let quote = "not all those who wander are lost";
104    /// let [first, second, third] = quote.split_whitespace().next_chunk().unwrap();
105    /// assert_eq!(first, "not");
106    /// assert_eq!(second, "all");
107    /// assert_eq!(third, "those");
108    /// ```
109    #[inline]
110    #[unstable(feature = "iter_next_chunk", issue = "98326")]
111    #[rustc_non_const_trait_method]
112    fn next_chunk<const N: usize>(
113        &mut self,
114    ) -> Result<[Self::Item; N], array::IntoIter<Self::Item, N>>
115    where
116        Self: Sized,
117    {
118        array::iter_next_chunk(self)
119    }
120
121    /// Returns the bounds on the remaining length of the iterator.
122    ///
123    /// Specifically, `size_hint()` returns a tuple where the first element
124    /// is the lower bound, and the second element is the upper bound.
125    ///
126    /// The second half of the tuple that is returned is an <code>[Option]<[usize]></code>.
127    /// A [`None`] here means that either there is no known upper bound, or the
128    /// upper bound is larger than [`usize`].
129    ///
130    /// # Implementation notes
131    ///
132    /// It is not enforced that an iterator implementation yields the declared
133    /// number of elements. A buggy iterator may yield less than the lower bound
134    /// or more than the upper bound of elements.
135    ///
136    /// `size_hint()` is primarily intended to be used for optimizations such as
137    /// reserving space for the elements of the iterator, but must not be
138    /// trusted to e.g., omit bounds checks in unsafe code. An incorrect
139    /// implementation of `size_hint()` should not lead to memory safety
140    /// violations.
141    ///
142    /// That said, the implementation should provide a correct estimation,
143    /// because otherwise it would be a violation of the trait's protocol.
144    ///
145    /// The default implementation returns <code>(0, [None])</code> which is correct for any
146    /// iterator.
147    ///
148    /// # Examples
149    ///
150    /// Basic usage:
151    ///
152    /// ```
153    /// let a = [1, 2, 3];
154    /// let mut iter = a.iter();
155    ///
156    /// assert_eq!((3, Some(3)), iter.size_hint());
157    /// let _ = iter.next();
158    /// assert_eq!((2, Some(2)), iter.size_hint());
159    /// ```
160    ///
161    /// A more complex example:
162    ///
163    /// ```
164    /// // The even numbers in the range of zero to nine.
165    /// let iter = (0..10).filter(|x| x % 2 == 0);
166    ///
167    /// // We might iterate from zero to ten times. Knowing that it's five
168    /// // exactly wouldn't be possible without executing filter().
169    /// assert_eq!((0, Some(10)), iter.size_hint());
170    ///
171    /// // Let's add five more numbers with chain()
172    /// let iter = (0..10).filter(|x| x % 2 == 0).chain(15..20);
173    ///
174    /// // now both bounds are increased by five
175    /// assert_eq!((5, Some(15)), iter.size_hint());
176    /// ```
177    ///
178    /// Returning `None` for an upper bound:
179    ///
180    /// ```
181    /// // an infinite iterator has no upper bound
182    /// // and the maximum possible lower bound
183    /// let iter = 0..;
184    ///
185    /// assert_eq!((usize::MAX, None), iter.size_hint());
186    /// ```
187    #[inline]
188    #[stable(feature = "rust1", since = "1.0.0")]
189    fn size_hint(&self) -> (usize, Option<usize>) {
190        (0, None)
191    }
192
193    /// Consumes the iterator, counting the number of iterations and returning it.
194    ///
195    /// This method will call [`next`] repeatedly until [`None`] is encountered,
196    /// returning the number of times it saw [`Some`]. Note that [`next`] has to be
197    /// called at least once even if the iterator does not have any elements.
198    ///
199    /// [`next`]: Iterator::next
200    ///
201    /// # Overflow Behavior
202    ///
203    /// The method does no guarding against overflows, so counting elements of
204    /// an iterator with more than [`usize::MAX`] elements either produces the
205    /// wrong result or panics. If overflow checks are enabled, a panic is
206    /// guaranteed.
207    ///
208    /// # Panics
209    ///
210    /// This function might panic if the iterator has more than [`usize::MAX`]
211    /// elements.
212    ///
213    /// # Examples
214    ///
215    /// ```
216    /// let a = [1, 2, 3];
217    /// assert_eq!(a.iter().count(), 3);
218    ///
219    /// let a = [1, 2, 3, 4, 5];
220    /// assert_eq!(a.iter().count(), 5);
221    /// ```
222    #[inline]
223    #[stable(feature = "rust1", since = "1.0.0")]
224    #[rustc_non_const_trait_method]
225    fn count(self) -> usize
226    where
227        Self: Sized,
228    {
229        self.fold(
230            0,
231            #[rustc_inherit_overflow_checks]
232            |count, _| count + 1,
233        )
234    }
235
236    /// Consumes the iterator, returning the last element.
237    ///
238    /// This method will evaluate the iterator until it returns [`None`]. While
239    /// doing so, it keeps track of the current element. After [`None`] is
240    /// returned, `last()` will then return the last element it saw.
241    ///
242    /// # Panics
243    ///
244    /// This function might panic if the iterator is infinite.
245    ///
246    /// # Examples
247    ///
248    /// ```
249    /// let a = [1, 2, 3];
250    /// assert_eq!(a.into_iter().last(), Some(3));
251    ///
252    /// let a = [1, 2, 3, 4, 5];
253    /// assert_eq!(a.into_iter().last(), Some(5));
254    /// ```
255    #[inline]
256    #[stable(feature = "rust1", since = "1.0.0")]
257    #[rustc_non_const_trait_method]
258    fn last(self) -> Option<Self::Item>
259    where
260        Self: Sized,
261    {
262        #[inline]
263        fn some<T>(_: Option<T>, x: T) -> Option<T> {
264            Some(x)
265        }
266
267        self.fold(None, some)
268    }
269
270    /// Advances the iterator by `n` elements.
271    ///
272    /// This method will eagerly skip `n` elements by calling [`next`] up to `n`
273    /// times until [`None`] is encountered.
274    ///
275    /// `advance_by(n)` will return `Ok(())` if the iterator successfully advances by
276    /// `n` elements, or a `Err(NonZero<usize>)` with value `k` if [`None`] is encountered,
277    /// where `k` is remaining number of steps that could not be advanced because the iterator ran out.
278    /// If `self` is empty and `n` is non-zero, then this returns `Err(n)`.
279    /// Otherwise, `k` is always less than `n`.
280    ///
281    /// Calling `advance_by(0)` can do meaningful work, for example [`Flatten`]
282    /// can advance its outer iterator until it finds an inner iterator that is not empty, which
283    /// then often allows it to return a more accurate `size_hint()` than in its initial state.
284    ///
285    /// [`Flatten`]: crate::iter::Flatten
286    /// [`next`]: Iterator::next
287    ///
288    /// # Examples
289    ///
290    /// ```
291    /// #![feature(iter_advance_by)]
292    ///
293    /// use std::num::NonZero;
294    ///
295    /// let a = [1, 2, 3, 4];
296    /// let mut iter = a.into_iter();
297    ///
298    /// assert_eq!(iter.advance_by(2), Ok(()));
299    /// assert_eq!(iter.next(), Some(3));
300    /// assert_eq!(iter.advance_by(0), Ok(()));
301    /// assert_eq!(iter.advance_by(100), Err(NonZero::new(99).unwrap())); // only `4` was skipped
302    /// ```
303    #[inline]
304    #[unstable(feature = "iter_advance_by", issue = "77404")]
305    #[rustc_non_const_trait_method]
306    fn advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
307        /// Helper trait to specialize `advance_by` via `try_fold` for `Sized` iterators.
308        trait SpecAdvanceBy {
309            fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>>;
310        }
311
312        impl<I: Iterator + ?Sized> SpecAdvanceBy for I {
313            default fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
314                for i in 0..n {
315                    if self.next().is_none() {
316                        // SAFETY: `i` is always less than `n`.
317                        return Err(unsafe { NonZero::new_unchecked(n - i) });
318                    }
319                }
320                Ok(())
321            }
322        }
323
324        impl<I: Iterator> SpecAdvanceBy for I {
325            fn spec_advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
326                let Some(n) = NonZero::new(n) else {
327                    return Ok(());
328                };
329
330                let res = self.try_fold(n, |n, _| NonZero::new(n.get() - 1));
331
332                match res {
333                    None => Ok(()),
334                    Some(n) => Err(n),
335                }
336            }
337        }
338
339        self.spec_advance_by(n)
340    }
341
342    /// Returns the `n`th element of the iterator.
343    ///
344    /// Like most indexing operations, the count starts from zero, so `nth(0)`
345    /// returns the first value, `nth(1)` the second, and so on.
346    ///
347    /// Note that all preceding elements, as well as the returned element, will be
348    /// consumed from the iterator. That means that the preceding elements will be
349    /// discarded, and also that calling `nth(0)` multiple times on the same iterator
350    /// will return different elements.
351    ///
352    /// `nth()` will return [`None`] if `n` is greater than or equal to the length of the
353    /// iterator.
354    ///
355    /// # Examples
356    ///
357    /// Basic usage:
358    ///
359    /// ```
360    /// let a = [1, 2, 3];
361    /// assert_eq!(a.into_iter().nth(1), Some(2));
362    /// ```
363    ///
364    /// Calling `nth()` multiple times doesn't rewind the iterator:
365    ///
366    /// ```
367    /// let a = [1, 2, 3];
368    ///
369    /// let mut iter = a.into_iter();
370    ///
371    /// assert_eq!(iter.nth(1), Some(2));
372    /// assert_eq!(iter.nth(1), None);
373    /// ```
374    ///
375    /// Returning `None` if there are less than `n + 1` elements:
376    ///
377    /// ```
378    /// let a = [1, 2, 3];
379    /// assert_eq!(a.into_iter().nth(10), None);
380    /// ```
381    #[inline]
382    #[stable(feature = "rust1", since = "1.0.0")]
383    #[rustc_non_const_trait_method]
384    fn nth(&mut self, n: usize) -> Option<Self::Item> {
385        self.advance_by(n).ok()?;
386        self.next()
387    }
388
389    /// Creates an iterator starting at the same point, but stepping by
390    /// the given amount at each iteration.
391    ///
392    /// Note 1: The first element of the iterator will always be returned,
393    /// regardless of the step given.
394    ///
395    /// Note 2: The time at which ignored elements are pulled is not fixed.
396    /// `StepBy` behaves like the sequence `self.next()`, `self.nth(step-1)`,
397    /// `self.nth(step-1)`, …, but is also free to behave like the sequence
398    /// `advance_n_and_return_first(&mut self, step)`,
399    /// `advance_n_and_return_first(&mut self, step)`, …
400    /// Which way is used may change for some iterators for performance reasons.
401    /// The second way will advance the iterator earlier and may consume more items.
402    ///
403    /// `advance_n_and_return_first` is the equivalent of:
404    /// ```
405    /// fn advance_n_and_return_first<I>(iter: &mut I, n: usize) -> Option<I::Item>
406    /// where
407    ///     I: Iterator,
408    /// {
409    ///     let next = iter.next();
410    ///     if n > 1 {
411    ///         iter.nth(n - 2);
412    ///     }
413    ///     next
414    /// }
415    /// ```
416    ///
417    /// # Panics
418    ///
419    /// The method will panic if the given step is `0`.
420    ///
421    /// # Examples
422    ///
423    /// ```
424    /// let a = [0, 1, 2, 3, 4, 5];
425    /// let mut iter = a.into_iter().step_by(2);
426    ///
427    /// assert_eq!(iter.next(), Some(0));
428    /// assert_eq!(iter.next(), Some(2));
429    /// assert_eq!(iter.next(), Some(4));
430    /// assert_eq!(iter.next(), None);
431    /// ```
432    #[inline]
433    #[stable(feature = "iterator_step_by", since = "1.28.0")]
434    #[rustc_non_const_trait_method]
435    fn step_by(self, step: usize) -> StepBy<Self>
436    where
437        Self: Sized,
438    {
439        StepBy::new(self, step)
440    }
441
442    /// Takes two iterators and creates a new iterator over both in sequence.
443    ///
444    /// `chain()` will return a new iterator which will first iterate over
445    /// values from the first iterator and then over values from the second
446    /// iterator.
447    ///
448    /// In other words, it links two iterators together, in a chain. 🔗
449    ///
450    /// [`once`] is commonly used to adapt a single value into a chain of
451    /// other kinds of iteration.
452    ///
453    /// # Examples
454    ///
455    /// Basic usage:
456    ///
457    /// ```
458    /// let s1 = "abc".chars();
459    /// let s2 = "def".chars();
460    ///
461    /// let mut iter = s1.chain(s2);
462    ///
463    /// assert_eq!(iter.next(), Some('a'));
464    /// assert_eq!(iter.next(), Some('b'));
465    /// assert_eq!(iter.next(), Some('c'));
466    /// assert_eq!(iter.next(), Some('d'));
467    /// assert_eq!(iter.next(), Some('e'));
468    /// assert_eq!(iter.next(), Some('f'));
469    /// assert_eq!(iter.next(), None);
470    /// ```
471    ///
472    /// Since the argument to `chain()` uses [`IntoIterator`], we can pass
473    /// anything that can be converted into an [`Iterator`], not just an
474    /// [`Iterator`] itself. For example, arrays (`[T]`) implement
475    /// [`IntoIterator`], and so can be passed to `chain()` directly:
476    ///
477    /// ```
478    /// let a1 = [1, 2, 3];
479    /// let a2 = [4, 5, 6];
480    ///
481    /// let mut iter = a1.into_iter().chain(a2);
482    ///
483    /// assert_eq!(iter.next(), Some(1));
484    /// assert_eq!(iter.next(), Some(2));
485    /// assert_eq!(iter.next(), Some(3));
486    /// assert_eq!(iter.next(), Some(4));
487    /// assert_eq!(iter.next(), Some(5));
488    /// assert_eq!(iter.next(), Some(6));
489    /// assert_eq!(iter.next(), None);
490    /// ```
491    ///
492    /// If you work with Windows API, you may wish to convert [`OsStr`] to `Vec<u16>`:
493    ///
494    /// ```
495    /// #[cfg(windows)]
496    /// fn os_str_to_utf16(s: &std::ffi::OsStr) -> Vec<u16> {
497    ///     use std::os::windows::ffi::OsStrExt;
498    ///     s.encode_wide().chain(std::iter::once(0)).collect()
499    /// }
500    /// ```
501    ///
502    /// [`once`]: crate::iter::once
503    /// [`OsStr`]: ../../std/ffi/struct.OsStr.html
504    #[inline]
505    #[stable(feature = "rust1", since = "1.0.0")]
506    #[rustc_non_const_trait_method]
507    fn chain<U>(self, other: U) -> Chain<Self, U::IntoIter>
508    where
509        Self: Sized,
510        U: IntoIterator<Item = Self::Item>,
511    {
512        Chain::new(self, other.into_iter())
513    }
514
515    /// 'Zips up' two iterators into a single iterator of pairs.
516    ///
517    /// `zip()` returns a new iterator that will iterate over two other
518    /// iterators, returning a tuple where the first element comes from the
519    /// first iterator, and the second element comes from the second iterator.
520    ///
521    /// In other words, it zips two iterators together, into a single one.
522    ///
523    /// If either iterator returns [`None`], [`next`] from the zipped iterator
524    /// will return [`None`].
525    /// If the zipped iterator has no more elements to return then each further attempt to advance
526    /// it will first try to advance the first iterator at most one time and if it still yielded an item
527    /// try to advance the second iterator at most one time.
528    ///
529    /// To 'undo' the result of zipping up two iterators, see [`unzip`].
530    ///
531    /// [`unzip`]: Iterator::unzip
532    ///
533    /// # Examples
534    ///
535    /// Basic usage:
536    ///
537    /// ```
538    /// let s1 = "abc".chars();
539    /// let s2 = "def".chars();
540    ///
541    /// let mut iter = s1.zip(s2);
542    ///
543    /// assert_eq!(iter.next(), Some(('a', 'd')));
544    /// assert_eq!(iter.next(), Some(('b', 'e')));
545    /// assert_eq!(iter.next(), Some(('c', 'f')));
546    /// assert_eq!(iter.next(), None);
547    /// ```
548    ///
549    /// Since the argument to `zip()` uses [`IntoIterator`], we can pass
550    /// anything that can be converted into an [`Iterator`], not just an
551    /// [`Iterator`] itself. For example, arrays (`[T]`) implement
552    /// [`IntoIterator`], and so can be passed to `zip()` directly:
553    ///
554    /// ```
555    /// let a1 = [1, 2, 3];
556    /// let a2 = [4, 5, 6];
557    ///
558    /// let mut iter = a1.into_iter().zip(a2);
559    ///
560    /// assert_eq!(iter.next(), Some((1, 4)));
561    /// assert_eq!(iter.next(), Some((2, 5)));
562    /// assert_eq!(iter.next(), Some((3, 6)));
563    /// assert_eq!(iter.next(), None);
564    /// ```
565    ///
566    /// `zip()` is often used to zip an infinite iterator to a finite one.
567    /// This works because the finite iterator will eventually return [`None`],
568    /// ending the zipper. Zipping with `(0..)` can look a lot like [`enumerate`]:
569    ///
570    /// ```
571    /// let enumerate: Vec<_> = "foo".chars().enumerate().collect();
572    ///
573    /// let zipper: Vec<_> = (0..).zip("foo".chars()).collect();
574    ///
575    /// assert_eq!((0, 'f'), enumerate[0]);
576    /// assert_eq!((0, 'f'), zipper[0]);
577    ///
578    /// assert_eq!((1, 'o'), enumerate[1]);
579    /// assert_eq!((1, 'o'), zipper[1]);
580    ///
581    /// assert_eq!((2, 'o'), enumerate[2]);
582    /// assert_eq!((2, 'o'), zipper[2]);
583    /// ```
584    ///
585    /// If both iterators have roughly equivalent syntax, it may be more readable to use [`zip`]:
586    ///
587    /// ```
588    /// use std::iter::zip;
589    ///
590    /// let a = [1, 2, 3];
591    /// let b = [2, 3, 4];
592    ///
593    /// let mut zipped = zip(
594    ///     a.into_iter().map(|x| x * 2).skip(1),
595    ///     b.into_iter().map(|x| x * 2).skip(1),
596    /// );
597    ///
598    /// assert_eq!(zipped.next(), Some((4, 6)));
599    /// assert_eq!(zipped.next(), Some((6, 8)));
600    /// assert_eq!(zipped.next(), None);
601    /// ```
602    ///
603    /// compared to:
604    ///
605    /// ```
606    /// # let a = [1, 2, 3];
607    /// # let b = [2, 3, 4];
608    /// #
609    /// let mut zipped = a
610    ///     .into_iter()
611    ///     .map(|x| x * 2)
612    ///     .skip(1)
613    ///     .zip(b.into_iter().map(|x| x * 2).skip(1));
614    /// #
615    /// # assert_eq!(zipped.next(), Some((4, 6)));
616    /// # assert_eq!(zipped.next(), Some((6, 8)));
617    /// # assert_eq!(zipped.next(), None);
618    /// ```
619    ///
620    /// [`enumerate`]: Iterator::enumerate
621    /// [`next`]: Iterator::next
622    /// [`zip`]: crate::iter::zip
623    #[inline]
624    #[stable(feature = "rust1", since = "1.0.0")]
625    #[rustc_non_const_trait_method]
626    fn zip<U>(self, other: U) -> Zip<Self, U::IntoIter>
627    where
628        Self: Sized,
629        U: IntoIterator,
630    {
631        Zip::new(self, other.into_iter())
632    }
633
634    /// Creates a new iterator which places a copy of `separator` between adjacent
635    /// items of the original iterator.
636    ///
637    /// In case `separator` does not implement [`Clone`] or needs to be
638    /// computed every time, use [`intersperse_with`].
639    ///
640    /// # Examples
641    ///
642    /// Basic usage:
643    ///
644    /// ```
645    /// #![feature(iter_intersperse)]
646    ///
647    /// let mut a = [0, 1, 2].into_iter().intersperse(100);
648    /// assert_eq!(a.next(), Some(0));   // The first element from `a`.
649    /// assert_eq!(a.next(), Some(100)); // The separator.
650    /// assert_eq!(a.next(), Some(1));   // The next element from `a`.
651    /// assert_eq!(a.next(), Some(100)); // The separator.
652    /// assert_eq!(a.next(), Some(2));   // The last element from `a`.
653    /// assert_eq!(a.next(), None);       // The iterator is finished.
654    /// ```
655    ///
656    /// `intersperse` can be very useful to join an iterator's items using a common element:
657    /// ```
658    /// #![feature(iter_intersperse)]
659    ///
660    /// let words = ["Hello", "World", "!"];
661    /// let hello: String = words.into_iter().intersperse(" ").collect();
662    /// assert_eq!(hello, "Hello World !");
663    /// ```
664    ///
665    /// [`Clone`]: crate::clone::Clone
666    /// [`intersperse_with`]: Iterator::intersperse_with
667    #[inline]
668    #[unstable(feature = "iter_intersperse", issue = "79524")]
669    #[rustc_non_const_trait_method]
670    fn intersperse(self, separator: Self::Item) -> Intersperse<Self>
671    where
672        Self: Sized,
673        Self::Item: Clone,
674    {
675        Intersperse::new(self, separator)
676    }
677
678    /// Creates a new iterator which places an item generated by `separator`
679    /// between adjacent items of the original iterator.
680    ///
681    /// The closure will be called exactly once each time an item is placed
682    /// between two adjacent items from the underlying iterator; specifically,
683    /// the closure is not called if the underlying iterator yields less than
684    /// two items and after the last item is yielded.
685    ///
686    /// If the iterator's item implements [`Clone`], it may be easier to use
687    /// [`intersperse`].
688    ///
689    /// # Examples
690    ///
691    /// Basic usage:
692    ///
693    /// ```
694    /// #![feature(iter_intersperse)]
695    ///
696    /// #[derive(PartialEq, Debug)]
697    /// struct NotClone(usize);
698    ///
699    /// let v = [NotClone(0), NotClone(1), NotClone(2)];
700    /// let mut it = v.into_iter().intersperse_with(|| NotClone(99));
701    ///
702    /// assert_eq!(it.next(), Some(NotClone(0)));  // The first element from `v`.
703    /// assert_eq!(it.next(), Some(NotClone(99))); // The separator.
704    /// assert_eq!(it.next(), Some(NotClone(1)));  // The next element from `v`.
705    /// assert_eq!(it.next(), Some(NotClone(99))); // The separator.
706    /// assert_eq!(it.next(), Some(NotClone(2)));  // The last element from `v`.
707    /// assert_eq!(it.next(), None);               // The iterator is finished.
708    /// ```
709    ///
710    /// `intersperse_with` can be used in situations where the separator needs
711    /// to be computed:
712    /// ```
713    /// #![feature(iter_intersperse)]
714    ///
715    /// let src = ["Hello", "to", "all", "people", "!!"].iter().copied();
716    ///
717    /// // The closure mutably borrows its context to generate an item.
718    /// let mut happy_emojis = [" ❤️ ", " 😀 "].into_iter();
719    /// let separator = || happy_emojis.next().unwrap_or(" 🦀 ");
720    ///
721    /// let result = src.intersperse_with(separator).collect::<String>();
722    /// assert_eq!(result, "Hello ❤️ to 😀 all 🦀 people 🦀 !!");
723    /// ```
724    /// [`Clone`]: crate::clone::Clone
725    /// [`intersperse`]: Iterator::intersperse
726    #[inline]
727    #[unstable(feature = "iter_intersperse", issue = "79524")]
728    #[rustc_non_const_trait_method]
729    fn intersperse_with<G>(self, separator: G) -> IntersperseWith<Self, G>
730    where
731        Self: Sized,
732        G: FnMut() -> Self::Item,
733    {
734        IntersperseWith::new(self, separator)
735    }
736
737    /// Takes a closure and creates an iterator which calls that closure on each
738    /// element.
739    ///
740    /// `map()` transforms one iterator into another, by means of its argument:
741    /// something that implements [`FnMut`]. It produces a new iterator which
742    /// calls this closure on each element of the original iterator.
743    ///
744    /// If you are good at thinking in types, you can think of `map()` like this:
745    /// If you have an iterator that gives you elements of some type `A`, and
746    /// you want an iterator of some other type `B`, you can use `map()`,
747    /// passing a closure that takes an `A` and returns a `B`.
748    ///
749    /// `map()` is conceptually similar to a [`for`] loop. However, as `map()` is
750    /// lazy, it is best used when you're already working with other iterators.
751    /// If you're doing some sort of looping for a side effect, it's considered
752    /// more idiomatic to use [`for`] than `map()`.
753    ///
754    /// [`for`]: ../../book/ch03-05-control-flow.html#looping-through-a-collection-with-for
755    ///
756    /// # Examples
757    ///
758    /// Basic usage:
759    ///
760    /// ```
761    /// let a = [1, 2, 3];
762    ///
763    /// let mut iter = a.iter().map(|x| 2 * x);
764    ///
765    /// assert_eq!(iter.next(), Some(2));
766    /// assert_eq!(iter.next(), Some(4));
767    /// assert_eq!(iter.next(), Some(6));
768    /// assert_eq!(iter.next(), None);
769    /// ```
770    ///
771    /// If you're doing some sort of side effect, prefer [`for`] to `map()`:
772    ///
773    /// ```
774    /// # #![allow(unused_must_use)]
775    /// // don't do this:
776    /// (0..5).map(|x| println!("{x}"));
777    ///
778    /// // it won't even execute, as it is lazy. Rust will warn you about this.
779    ///
780    /// // Instead, use a for-loop:
781    /// for x in 0..5 {
782    ///     println!("{x}");
783    /// }
784    /// ```
785    #[rustc_diagnostic_item = "IteratorMap"]
786    #[inline]
787    #[stable(feature = "rust1", since = "1.0.0")]
788    #[rustc_non_const_trait_method]
789    fn map<B, F>(self, f: F) -> Map<Self, F>
790    where
791        Self: Sized,
792        F: FnMut(Self::Item) -> B,
793    {
794        Map::new(self, f)
795    }
796
797    /// Calls a closure on each element of an iterator.
798    ///
799    /// This is equivalent to using a [`for`] loop on the iterator, although
800    /// `break` and `continue` are not possible from a closure. It's generally
801    /// more idiomatic to use a `for` loop, but `for_each` may be more legible
802    /// when processing items at the end of longer iterator chains. In some
803    /// cases `for_each` may also be faster than a loop, because it will use
804    /// internal iteration on adapters like `Chain`.
805    ///
806    /// [`for`]: ../../book/ch03-05-control-flow.html#looping-through-a-collection-with-for
807    ///
808    /// # Examples
809    ///
810    /// Basic usage:
811    ///
812    /// ```
813    /// use std::sync::mpsc::channel;
814    ///
815    /// let (tx, rx) = channel();
816    /// (0..5).map(|x| x * 2 + 1)
817    ///       .for_each(move |x| tx.send(x).unwrap());
818    ///
819    /// let v: Vec<_> = rx.iter().collect();
820    /// assert_eq!(v, vec![1, 3, 5, 7, 9]);
821    /// ```
822    ///
823    /// For such a small example, a `for` loop may be cleaner, but `for_each`
824    /// might be preferable to keep a functional style with longer iterators:
825    ///
826    /// ```
827    /// (0..5).flat_map(|x| (x * 100)..(x * 110))
828    ///       .enumerate()
829    ///       .filter(|&(i, x)| (i + x) % 3 == 0)
830    ///       .for_each(|(i, x)| println!("{i}:{x}"));
831    /// ```
832    #[inline]
833    #[stable(feature = "iterator_for_each", since = "1.21.0")]
834    #[rustc_non_const_trait_method]
835    fn for_each<F>(self, f: F)
836    where
837        Self: Sized,
838        F: FnMut(Self::Item),
839    {
840        #[inline]
841        fn call<T>(mut f: impl FnMut(T)) -> impl FnMut((), T) {
842            move |(), item| f(item)
843        }
844
845        self.fold((), call(f));
846    }
847
848    /// Creates an iterator which uses a closure to determine if an element
849    /// should be yielded.
850    ///
851    /// Given an element the closure must return `true` or `false`. The returned
852    /// iterator will yield only the elements for which the closure returns
853    /// `true`.
854    ///
855    /// # Examples
856    ///
857    /// Basic usage:
858    ///
859    /// ```
860    /// let a = [0i32, 1, 2];
861    ///
862    /// let mut iter = a.into_iter().filter(|x| x.is_positive());
863    ///
864    /// assert_eq!(iter.next(), Some(1));
865    /// assert_eq!(iter.next(), Some(2));
866    /// assert_eq!(iter.next(), None);
867    /// ```
868    ///
869    /// Because the closure passed to `filter()` takes a reference, and many
870    /// iterators iterate over references, this leads to a possibly confusing
871    /// situation, where the type of the closure is a double reference:
872    ///
873    /// ```
874    /// let s = &[0, 1, 2];
875    ///
876    /// let mut iter = s.iter().filter(|x| **x > 1); // needs two *s!
877    ///
878    /// assert_eq!(iter.next(), Some(&2));
879    /// assert_eq!(iter.next(), None);
880    /// ```
881    ///
882    /// It's common to instead use destructuring on the argument to strip away one:
883    ///
884    /// ```
885    /// let s = &[0, 1, 2];
886    ///
887    /// let mut iter = s.iter().filter(|&x| *x > 1); // both & and *
888    ///
889    /// assert_eq!(iter.next(), Some(&2));
890    /// assert_eq!(iter.next(), None);
891    /// ```
892    ///
893    /// or both:
894    ///
895    /// ```
896    /// let s = &[0, 1, 2];
897    ///
898    /// let mut iter = s.iter().filter(|&&x| x > 1); // two &s
899    ///
900    /// assert_eq!(iter.next(), Some(&2));
901    /// assert_eq!(iter.next(), None);
902    /// ```
903    ///
904    /// of these layers.
905    ///
906    /// Note that `iter.filter(f).next()` is equivalent to `iter.find(f)`.
907    #[inline]
908    #[stable(feature = "rust1", since = "1.0.0")]
909    #[rustc_diagnostic_item = "iter_filter"]
910    #[rustc_non_const_trait_method]
911    fn filter<P>(self, predicate: P) -> Filter<Self, P>
912    where
913        Self: Sized,
914        P: FnMut(&Self::Item) -> bool,
915    {
916        Filter::new(self, predicate)
917    }
918
919    /// Creates an iterator that both filters and maps.
920    ///
921    /// The returned iterator yields only the `value`s for which the supplied
922    /// closure returns `Some(value)`.
923    ///
924    /// `filter_map` can be used to make chains of [`filter`] and [`map`] more
925    /// concise. The example below shows how a `map().filter().map()` can be
926    /// shortened to a single call to `filter_map`.
927    ///
928    /// [`filter`]: Iterator::filter
929    /// [`map`]: Iterator::map
930    ///
931    /// # Examples
932    ///
933    /// Basic usage:
934    ///
935    /// ```
936    /// let a = ["1", "two", "NaN", "four", "5"];
937    ///
938    /// let mut iter = a.iter().filter_map(|s| s.parse().ok());
939    ///
940    /// assert_eq!(iter.next(), Some(1));
941    /// assert_eq!(iter.next(), Some(5));
942    /// assert_eq!(iter.next(), None);
943    /// ```
944    ///
945    /// Here's the same example, but with [`filter`] and [`map`]:
946    ///
947    /// ```
948    /// let a = ["1", "two", "NaN", "four", "5"];
949    /// let mut iter = a.iter().map(|s| s.parse()).filter(|s| s.is_ok()).map(|s| s.unwrap());
950    /// assert_eq!(iter.next(), Some(1));
951    /// assert_eq!(iter.next(), Some(5));
952    /// assert_eq!(iter.next(), None);
953    /// ```
954    #[inline]
955    #[stable(feature = "rust1", since = "1.0.0")]
956    #[rustc_non_const_trait_method]
957    fn filter_map<B, F>(self, f: F) -> FilterMap<Self, F>
958    where
959        Self: Sized,
960        F: FnMut(Self::Item) -> Option<B>,
961    {
962        FilterMap::new(self, f)
963    }
964
965    /// Creates an iterator which gives the current iteration count as well as
966    /// the next value.
967    ///
968    /// The iterator returned yields pairs `(i, val)`, where `i` is the
969    /// current index of iteration and `val` is the value returned by the
970    /// iterator.
971    ///
972    /// `enumerate()` keeps its count as a [`usize`]. If you want to count by a
973    /// different sized integer, the [`zip`] function provides similar
974    /// functionality.
975    ///
976    /// # Overflow Behavior
977    ///
978    /// The method does no guarding against overflows, so enumerating more than
979    /// [`usize::MAX`] elements either produces the wrong result or panics. If
980    /// overflow checks are enabled, a panic is guaranteed.
981    ///
982    /// # Panics
983    ///
984    /// The returned iterator might panic if the to-be-returned index would
985    /// overflow a [`usize`].
986    ///
987    /// [`zip`]: Iterator::zip
988    ///
989    /// # Examples
990    ///
991    /// ```
992    /// let a = ['a', 'b', 'c'];
993    ///
994    /// let mut iter = a.into_iter().enumerate();
995    ///
996    /// assert_eq!(iter.next(), Some((0, 'a')));
997    /// assert_eq!(iter.next(), Some((1, 'b')));
998    /// assert_eq!(iter.next(), Some((2, 'c')));
999    /// assert_eq!(iter.next(), None);
1000    /// ```
1001    #[inline]
1002    #[stable(feature = "rust1", since = "1.0.0")]
1003    #[rustc_diagnostic_item = "enumerate_method"]
1004    #[rustc_non_const_trait_method]
1005    fn enumerate(self) -> Enumerate<Self>
1006    where
1007        Self: Sized,
1008    {
1009        Enumerate::new(self)
1010    }
1011
1012    /// Creates an iterator which can use the [`peek`] and [`peek_mut`] methods
1013    /// to look at the next element of the iterator without consuming it. See
1014    /// their documentation for more information.
1015    ///
1016    /// Note that the underlying iterator is still advanced when [`peek`] or
1017    /// [`peek_mut`] are called for the first time: In order to retrieve the
1018    /// next element, [`next`] is called on the underlying iterator, hence any
1019    /// side effects (i.e. anything other than fetching the next value) of
1020    /// the [`next`] method will occur.
1021    ///
1022    ///
1023    /// # Examples
1024    ///
1025    /// Basic usage:
1026    ///
1027    /// ```
1028    /// let xs = [1, 2, 3];
1029    ///
1030    /// let mut iter = xs.into_iter().peekable();
1031    ///
1032    /// // peek() lets us see into the future
1033    /// assert_eq!(iter.peek(), Some(&1));
1034    /// assert_eq!(iter.next(), Some(1));
1035    ///
1036    /// assert_eq!(iter.next(), Some(2));
1037    ///
1038    /// // we can peek() multiple times, the iterator won't advance
1039    /// assert_eq!(iter.peek(), Some(&3));
1040    /// assert_eq!(iter.peek(), Some(&3));
1041    ///
1042    /// assert_eq!(iter.next(), Some(3));
1043    ///
1044    /// // after the iterator is finished, so is peek()
1045    /// assert_eq!(iter.peek(), None);
1046    /// assert_eq!(iter.next(), None);
1047    /// ```
1048    ///
1049    /// Using [`peek_mut`] to mutate the next item without advancing the
1050    /// iterator:
1051    ///
1052    /// ```
1053    /// let xs = [1, 2, 3];
1054    ///
1055    /// let mut iter = xs.into_iter().peekable();
1056    ///
1057    /// // `peek_mut()` lets us see into the future
1058    /// assert_eq!(iter.peek_mut(), Some(&mut 1));
1059    /// assert_eq!(iter.peek_mut(), Some(&mut 1));
1060    /// assert_eq!(iter.next(), Some(1));
1061    ///
1062    /// if let Some(p) = iter.peek_mut() {
1063    ///     assert_eq!(*p, 2);
1064    ///     // put a value into the iterator
1065    ///     *p = 1000;
1066    /// }
1067    ///
1068    /// // The value reappears as the iterator continues
1069    /// assert_eq!(iter.collect::<Vec<_>>(), vec![1000, 3]);
1070    /// ```
1071    /// [`peek`]: Peekable::peek
1072    /// [`peek_mut`]: Peekable::peek_mut
1073    /// [`next`]: Iterator::next
1074    #[inline]
1075    #[stable(feature = "rust1", since = "1.0.0")]
1076    #[rustc_non_const_trait_method]
1077    fn peekable(self) -> Peekable<Self>
1078    where
1079        Self: Sized,
1080    {
1081        Peekable::new(self)
1082    }
1083
1084    /// Creates an iterator that [`skip`]s elements based on a predicate.
1085    ///
1086    /// [`skip`]: Iterator::skip
1087    ///
1088    /// `skip_while()` takes a closure as an argument. It will call this
1089    /// closure on each element of the iterator, and ignore elements
1090    /// until it returns `false`.
1091    ///
1092    /// After `false` is returned, `skip_while()`'s job is over, and the
1093    /// rest of the elements are yielded.
1094    ///
1095    /// # Examples
1096    ///
1097    /// Basic usage:
1098    ///
1099    /// ```
1100    /// let a = [-1i32, 0, 1];
1101    ///
1102    /// let mut iter = a.into_iter().skip_while(|x| x.is_negative());
1103    ///
1104    /// assert_eq!(iter.next(), Some(0));
1105    /// assert_eq!(iter.next(), Some(1));
1106    /// assert_eq!(iter.next(), None);
1107    /// ```
1108    ///
1109    /// Because the closure passed to `skip_while()` takes a reference, and many
1110    /// iterators iterate over references, this leads to a possibly confusing
1111    /// situation, where the type of the closure argument is a double reference:
1112    ///
1113    /// ```
1114    /// let s = &[-1, 0, 1];
1115    ///
1116    /// let mut iter = s.iter().skip_while(|x| **x < 0); // need two *s!
1117    ///
1118    /// assert_eq!(iter.next(), Some(&0));
1119    /// assert_eq!(iter.next(), Some(&1));
1120    /// assert_eq!(iter.next(), None);
1121    /// ```
1122    ///
1123    /// Stopping after an initial `false`:
1124    ///
1125    /// ```
1126    /// let a = [-1, 0, 1, -2];
1127    ///
1128    /// let mut iter = a.into_iter().skip_while(|&x| x < 0);
1129    ///
1130    /// assert_eq!(iter.next(), Some(0));
1131    /// assert_eq!(iter.next(), Some(1));
1132    ///
1133    /// // while this would have been false, since we already got a false,
1134    /// // skip_while() isn't used any more
1135    /// assert_eq!(iter.next(), Some(-2));
1136    ///
1137    /// assert_eq!(iter.next(), None);
1138    /// ```
1139    #[inline]
1140    #[doc(alias = "drop_while")]
1141    #[stable(feature = "rust1", since = "1.0.0")]
1142    #[rustc_non_const_trait_method]
1143    fn skip_while<P>(self, predicate: P) -> SkipWhile<Self, P>
1144    where
1145        Self: Sized,
1146        P: FnMut(&Self::Item) -> bool,
1147    {
1148        SkipWhile::new(self, predicate)
1149    }
1150
1151    /// Creates an iterator that yields elements based on a predicate.
1152    ///
1153    /// `take_while()` takes a closure as an argument. It will call this
1154    /// closure on each element of the iterator, and yield elements
1155    /// while it returns `true`.
1156    ///
1157    /// After `false` is returned, `take_while()`'s job is over, and the
1158    /// rest of the elements are ignored.
1159    ///
1160    /// # Examples
1161    ///
1162    /// Basic usage:
1163    ///
1164    /// ```
1165    /// let a = [-1i32, 0, 1];
1166    ///
1167    /// let mut iter = a.into_iter().take_while(|x| x.is_negative());
1168    ///
1169    /// assert_eq!(iter.next(), Some(-1));
1170    /// assert_eq!(iter.next(), None);
1171    /// ```
1172    ///
1173    /// Because the closure passed to `take_while()` takes a reference, and many
1174    /// iterators iterate over references, this leads to a possibly confusing
1175    /// situation, where the type of the closure is a double reference:
1176    ///
1177    /// ```
1178    /// let s = &[-1, 0, 1];
1179    ///
1180    /// let mut iter = s.iter().take_while(|x| **x < 0); // need two *s!
1181    ///
1182    /// assert_eq!(iter.next(), Some(&-1));
1183    /// assert_eq!(iter.next(), None);
1184    /// ```
1185    ///
1186    /// Stopping after an initial `false`:
1187    ///
1188    /// ```
1189    /// let a = [-1, 0, 1, -2];
1190    ///
1191    /// let mut iter = a.into_iter().take_while(|&x| x < 0);
1192    ///
1193    /// assert_eq!(iter.next(), Some(-1));
1194    ///
1195    /// // We have more elements that are less than zero, but since we already
1196    /// // got a false, take_while() ignores the remaining elements.
1197    /// assert_eq!(iter.next(), None);
1198    /// ```
1199    ///
1200    /// Because `take_while()` needs to look at the value in order to see if it
1201    /// should be included or not, consuming iterators will see that it is
1202    /// removed:
1203    ///
1204    /// ```
1205    /// let a = [1, 2, 3, 4];
1206    /// let mut iter = a.into_iter();
1207    ///
1208    /// let result: Vec<i32> = iter.by_ref().take_while(|&n| n != 3).collect();
1209    ///
1210    /// assert_eq!(result, [1, 2]);
1211    ///
1212    /// let result: Vec<i32> = iter.collect();
1213    ///
1214    /// assert_eq!(result, [4]);
1215    /// ```
1216    ///
1217    /// The `3` is no longer there, because it was consumed in order to see if
1218    /// the iteration should stop, but wasn't placed back into the iterator.
1219    #[inline]
1220    #[stable(feature = "rust1", since = "1.0.0")]
1221    #[rustc_non_const_trait_method]
1222    fn take_while<P>(self, predicate: P) -> TakeWhile<Self, P>
1223    where
1224        Self: Sized,
1225        P: FnMut(&Self::Item) -> bool,
1226    {
1227        TakeWhile::new(self, predicate)
1228    }
1229
1230    /// Creates an iterator that both yields elements based on a predicate and maps.
1231    ///
1232    /// `map_while()` takes a closure as an argument. It will call this
1233    /// closure on each element of the iterator, and yield elements
1234    /// while it returns [`Some(_)`][`Some`].
1235    ///
1236    /// # Examples
1237    ///
1238    /// Basic usage:
1239    ///
1240    /// ```
1241    /// let a = [-1i32, 4, 0, 1];
1242    ///
1243    /// let mut iter = a.into_iter().map_while(|x| 16i32.checked_div(x));
1244    ///
1245    /// assert_eq!(iter.next(), Some(-16));
1246    /// assert_eq!(iter.next(), Some(4));
1247    /// assert_eq!(iter.next(), None);
1248    /// ```
1249    ///
1250    /// Here's the same example, but with [`take_while`] and [`map`]:
1251    ///
1252    /// [`take_while`]: Iterator::take_while
1253    /// [`map`]: Iterator::map
1254    ///
1255    /// ```
1256    /// let a = [-1i32, 4, 0, 1];
1257    ///
1258    /// let mut iter = a.into_iter()
1259    ///                 .map(|x| 16i32.checked_div(x))
1260    ///                 .take_while(|x| x.is_some())
1261    ///                 .map(|x| x.unwrap());
1262    ///
1263    /// assert_eq!(iter.next(), Some(-16));
1264    /// assert_eq!(iter.next(), Some(4));
1265    /// assert_eq!(iter.next(), None);
1266    /// ```
1267    ///
1268    /// Stopping after an initial [`None`]:
1269    ///
1270    /// ```
1271    /// let a = [0, 1, 2, -3, 4, 5, -6];
1272    ///
1273    /// let iter = a.into_iter().map_while(|x| u32::try_from(x).ok());
1274    /// let vec: Vec<_> = iter.collect();
1275    ///
1276    /// // We have more elements that could fit in u32 (such as 4, 5), but `map_while` returned `None` for `-3`
1277    /// // (as the `predicate` returned `None`) and `collect` stops at the first `None` encountered.
1278    /// assert_eq!(vec, [0, 1, 2]);
1279    /// ```
1280    ///
1281    /// Because `map_while()` needs to look at the value in order to see if it
1282    /// should be included or not, consuming iterators will see that it is
1283    /// removed:
1284    ///
1285    /// ```
1286    /// let a = [1, 2, -3, 4];
1287    /// let mut iter = a.into_iter();
1288    ///
1289    /// let result: Vec<u32> = iter.by_ref()
1290    ///                            .map_while(|n| u32::try_from(n).ok())
1291    ///                            .collect();
1292    ///
1293    /// assert_eq!(result, [1, 2]);
1294    ///
1295    /// let result: Vec<i32> = iter.collect();
1296    ///
1297    /// assert_eq!(result, [4]);
1298    /// ```
1299    ///
1300    /// The `-3` is no longer there, because it was consumed in order to see if
1301    /// the iteration should stop, but wasn't placed back into the iterator.
1302    ///
1303    /// Note that unlike [`take_while`] this iterator is **not** fused.
1304    /// It is also not specified what this iterator returns after the first [`None`] is returned.
1305    /// If you need a fused iterator, use [`fuse`].
1306    ///
1307    /// [`fuse`]: Iterator::fuse
1308    #[inline]
1309    #[stable(feature = "iter_map_while", since = "1.57.0")]
1310    #[rustc_non_const_trait_method]
1311    fn map_while<B, P>(self, predicate: P) -> MapWhile<Self, P>
1312    where
1313        Self: Sized,
1314        P: FnMut(Self::Item) -> Option<B>,
1315    {
1316        MapWhile::new(self, predicate)
1317    }
1318
1319    /// Creates an iterator that skips the first `n` elements.
1320    ///
1321    /// `skip(n)` skips elements until `n` elements are skipped or the end of the
1322    /// iterator is reached (whichever happens first). After that, all the remaining
1323    /// elements are yielded. In particular, if the original iterator is too short,
1324    /// then the returned iterator is empty.
1325    ///
1326    /// Rather than overriding this method directly, instead override the `nth` method.
1327    ///
1328    /// # Examples
1329    ///
1330    /// ```
1331    /// let a = [1, 2, 3];
1332    ///
1333    /// let mut iter = a.into_iter().skip(2);
1334    ///
1335    /// assert_eq!(iter.next(), Some(3));
1336    /// assert_eq!(iter.next(), None);
1337    /// ```
1338    #[inline]
1339    #[stable(feature = "rust1", since = "1.0.0")]
1340    #[rustc_non_const_trait_method]
1341    fn skip(self, n: usize) -> Skip<Self>
1342    where
1343        Self: Sized,
1344    {
1345        Skip::new(self, n)
1346    }
1347
1348    /// Creates an iterator that yields the first `n` elements, or fewer
1349    /// if the underlying iterator ends sooner.
1350    ///
1351    /// `take(n)` yields elements until `n` elements are yielded or the end of
1352    /// the iterator is reached (whichever happens first).
1353    /// The returned iterator is a prefix of length `n` if the original iterator
1354    /// contains at least `n` elements, otherwise it contains all of the
1355    /// (fewer than `n`) elements of the original iterator.
1356    ///
1357    /// # Examples
1358    ///
1359    /// Basic usage:
1360    ///
1361    /// ```
1362    /// let a = [1, 2, 3];
1363    ///
1364    /// let mut iter = a.into_iter().take(2);
1365    ///
1366    /// assert_eq!(iter.next(), Some(1));
1367    /// assert_eq!(iter.next(), Some(2));
1368    /// assert_eq!(iter.next(), None);
1369    /// ```
1370    ///
1371    /// `take()` is often used with an infinite iterator, to make it finite:
1372    ///
1373    /// ```
1374    /// let mut iter = (0..).take(3);
1375    ///
1376    /// assert_eq!(iter.next(), Some(0));
1377    /// assert_eq!(iter.next(), Some(1));
1378    /// assert_eq!(iter.next(), Some(2));
1379    /// assert_eq!(iter.next(), None);
1380    /// ```
1381    ///
1382    /// If less than `n` elements are available,
1383    /// `take` will limit itself to the size of the underlying iterator:
1384    ///
1385    /// ```
1386    /// let v = [1, 2];
1387    /// let mut iter = v.into_iter().take(5);
1388    /// assert_eq!(iter.next(), Some(1));
1389    /// assert_eq!(iter.next(), Some(2));
1390    /// assert_eq!(iter.next(), None);
1391    /// ```
1392    ///
1393    /// Use [`by_ref`] to take from the iterator without consuming it, and then
1394    /// continue using the original iterator:
1395    ///
1396    /// ```
1397    /// let mut words = ["hello", "world", "of", "Rust"].into_iter();
1398    ///
1399    /// // Take the first two words.
1400    /// let hello_world: Vec<_> = words.by_ref().take(2).collect();
1401    /// assert_eq!(hello_world, vec!["hello", "world"]);
1402    ///
1403    /// // Collect the rest of the words.
1404    /// // We can only do this because we used `by_ref` earlier.
1405    /// let of_rust: Vec<_> = words.collect();
1406    /// assert_eq!(of_rust, vec!["of", "Rust"]);
1407    /// ```
1408    ///
1409    /// [`by_ref`]: Iterator::by_ref
1410    #[doc(alias = "limit")]
1411    #[inline]
1412    #[stable(feature = "rust1", since = "1.0.0")]
1413    #[rustc_non_const_trait_method]
1414    fn take(self, n: usize) -> Take<Self>
1415    where
1416        Self: Sized,
1417    {
1418        Take::new(self, n)
1419    }
1420
1421    /// An iterator adapter which, like [`fold`], holds internal state, but
1422    /// unlike [`fold`], produces a new iterator.
1423    ///
1424    /// [`fold`]: Iterator::fold
1425    ///
1426    /// `scan()` takes two arguments: an initial value which seeds the internal
1427    /// state, and a closure with two arguments, the first being a mutable
1428    /// reference to the internal state and the second an iterator element.
1429    /// The closure can assign to the internal state to share state between
1430    /// iterations.
1431    ///
1432    /// On iteration, the closure will be applied to each element of the
1433    /// iterator and the return value from the closure, an [`Option`], is
1434    /// returned by the `next` method. Thus the closure can return
1435    /// `Some(value)` to yield `value`, or `None` to end the iteration.
1436    ///
1437    /// # Examples
1438    ///
1439    /// ```
1440    /// let a = [1, 2, 3, 4];
1441    ///
1442    /// let mut iter = a.into_iter().scan(1, |state, x| {
1443    ///     // each iteration, we'll multiply the state by the element ...
1444    ///     *state = *state * x;
1445    ///
1446    ///     // ... and terminate if the state exceeds 6
1447    ///     if *state > 6 {
1448    ///         return None;
1449    ///     }
1450    ///     // ... else yield the negation of the state
1451    ///     Some(-*state)
1452    /// });
1453    ///
1454    /// assert_eq!(iter.next(), Some(-1));
1455    /// assert_eq!(iter.next(), Some(-2));
1456    /// assert_eq!(iter.next(), Some(-6));
1457    /// assert_eq!(iter.next(), None);
1458    /// ```
1459    #[inline]
1460    #[stable(feature = "rust1", since = "1.0.0")]
1461    #[rustc_non_const_trait_method]
1462    fn scan<St, B, F>(self, initial_state: St, f: F) -> Scan<Self, St, F>
1463    where
1464        Self: Sized,
1465        F: FnMut(&mut St, Self::Item) -> Option<B>,
1466    {
1467        Scan::new(self, initial_state, f)
1468    }
1469
1470    /// Creates an iterator that works like map, but flattens nested structure.
1471    ///
1472    /// The [`map`] adapter is very useful, but only when the closure
1473    /// argument produces values. If it produces an iterator instead, there's
1474    /// an extra layer of indirection. `flat_map()` will remove this extra layer
1475    /// on its own.
1476    ///
1477    /// You can think of `flat_map(f)` as the semantic equivalent
1478    /// of [`map`]ping, and then [`flatten`]ing as in `map(f).flatten()`.
1479    ///
1480    /// Another way of thinking about `flat_map()`: [`map`]'s closure returns
1481    /// one item for each element, and `flat_map()`'s closure returns an
1482    /// iterator for each element.
1483    ///
1484    /// [`map`]: Iterator::map
1485    /// [`flatten`]: Iterator::flatten
1486    ///
1487    /// # Examples
1488    ///
1489    /// ```
1490    /// let words = ["alpha", "beta", "gamma"];
1491    ///
1492    /// // chars() returns an iterator
1493    /// let merged: String = words.iter()
1494    ///                           .flat_map(|s| s.chars())
1495    ///                           .collect();
1496    /// assert_eq!(merged, "alphabetagamma");
1497    /// ```
1498    #[inline]
1499    #[stable(feature = "rust1", since = "1.0.0")]
1500    #[rustc_non_const_trait_method]
1501    fn flat_map<U, F>(self, f: F) -> FlatMap<Self, U, F>
1502    where
1503        Self: Sized,
1504        U: IntoIterator,
1505        F: FnMut(Self::Item) -> U,
1506    {
1507        FlatMap::new(self, f)
1508    }
1509
1510    /// Creates an iterator that flattens nested structure.
1511    ///
1512    /// This is useful when you have an iterator of iterators or an iterator of
1513    /// things that can be turned into iterators and you want to remove one
1514    /// level of indirection.
1515    ///
1516    /// # Examples
1517    ///
1518    /// Basic usage:
1519    ///
1520    /// ```
1521    /// let data = vec![vec![1, 2, 3, 4], vec![5, 6]];
1522    /// let flattened: Vec<_> = data.into_iter().flatten().collect();
1523    /// assert_eq!(flattened, [1, 2, 3, 4, 5, 6]);
1524    /// ```
1525    ///
1526    /// Mapping and then flattening:
1527    ///
1528    /// ```
1529    /// let words = ["alpha", "beta", "gamma"];
1530    ///
1531    /// // chars() returns an iterator
1532    /// let merged: String = words.iter()
1533    ///                           .map(|s| s.chars())
1534    ///                           .flatten()
1535    ///                           .collect();
1536    /// assert_eq!(merged, "alphabetagamma");
1537    /// ```
1538    ///
1539    /// You can also rewrite this in terms of [`flat_map()`], which is preferable
1540    /// in this case since it conveys intent more clearly:
1541    ///
1542    /// ```
1543    /// let words = ["alpha", "beta", "gamma"];
1544    ///
1545    /// // chars() returns an iterator
1546    /// let merged: String = words.iter()
1547    ///                           .flat_map(|s| s.chars())
1548    ///                           .collect();
1549    /// assert_eq!(merged, "alphabetagamma");
1550    /// ```
1551    ///
1552    /// Flattening works on any `IntoIterator` type, including `Option` and `Result`:
1553    ///
1554    /// ```
1555    /// let options = vec![Some(123), Some(321), None, Some(231)];
1556    /// let flattened_options: Vec<_> = options.into_iter().flatten().collect();
1557    /// assert_eq!(flattened_options, [123, 321, 231]);
1558    ///
1559    /// let results = vec![Ok(123), Ok(321), Err(456), Ok(231)];
1560    /// let flattened_results: Vec<_> = results.into_iter().flatten().collect();
1561    /// assert_eq!(flattened_results, [123, 321, 231]);
1562    /// ```
1563    ///
1564    /// Flattening only removes one level of nesting at a time:
1565    ///
1566    /// ```
1567    /// let d3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
1568    ///
1569    /// let d2: Vec<_> = d3.into_iter().flatten().collect();
1570    /// assert_eq!(d2, [[1, 2], [3, 4], [5, 6], [7, 8]]);
1571    ///
1572    /// let d1: Vec<_> = d3.into_iter().flatten().flatten().collect();
1573    /// assert_eq!(d1, [1, 2, 3, 4, 5, 6, 7, 8]);
1574    /// ```
1575    ///
1576    /// Here we see that `flatten()` does not perform a "deep" flatten.
1577    /// Instead, only one level of nesting is removed. That is, if you
1578    /// `flatten()` a three-dimensional array, the result will be
1579    /// two-dimensional and not one-dimensional. To get a one-dimensional
1580    /// structure, you have to `flatten()` again.
1581    ///
1582    /// [`flat_map()`]: Iterator::flat_map
1583    #[inline]
1584    #[stable(feature = "iterator_flatten", since = "1.29.0")]
1585    #[rustc_non_const_trait_method]
1586    fn flatten(self) -> Flatten<Self>
1587    where
1588        Self: Sized,
1589        Self::Item: IntoIterator,
1590    {
1591        Flatten::new(self)
1592    }
1593
1594    /// Calls the given function `f` for each contiguous window of size `N` over
1595    /// `self` and returns an iterator over the outputs of `f`. Like [`slice::windows()`],
1596    /// the windows during mapping overlap as well.
1597    ///
1598    /// In the following example, the closure is called three times with the
1599    /// arguments `&['a', 'b']`, `&['b', 'c']` and `&['c', 'd']` respectively.
1600    ///
1601    /// ```
1602    /// #![feature(iter_map_windows)]
1603    ///
1604    /// let strings = "abcd".chars()
1605    ///     .map_windows(|[x, y]| format!("{}+{}", x, y))
1606    ///     .collect::<Vec<String>>();
1607    ///
1608    /// assert_eq!(strings, vec!["a+b", "b+c", "c+d"]);
1609    /// ```
1610    ///
1611    /// Note that the const parameter `N` is usually inferred by the
1612    /// destructured argument in the closure.
1613    ///
1614    /// The returned iterator yields 𝑘 − `N` + 1 items (where 𝑘 is the number of
1615    /// items yielded by `self`). If 𝑘 is less than `N`, this method yields an
1616    /// empty iterator.
1617    ///
1618    /// The returned iterator implements [`FusedIterator`], because once `self`
1619    /// returns `None`, even if it returns a `Some(T)` again in the next iterations,
1620    /// we cannot put it into a contiguous array buffer, and thus the returned iterator
1621    /// should be fused.
1622    ///
1623    /// [`slice::windows()`]: slice::windows
1624    /// [`FusedIterator`]: crate::iter::FusedIterator
1625    ///
1626    /// # Panics
1627    ///
1628    /// Panics if `N` is zero. This check will most probably get changed to a
1629    /// compile time error before this method gets stabilized.
1630    ///
1631    /// ```should_panic
1632    /// #![feature(iter_map_windows)]
1633    ///
1634    /// let iter = std::iter::repeat(0).map_windows(|&[]| ());
1635    /// ```
1636    ///
1637    /// # Examples
1638    ///
1639    /// Building the sums of neighboring numbers.
1640    ///
1641    /// ```
1642    /// #![feature(iter_map_windows)]
1643    ///
1644    /// let mut it = [1, 3, 8, 1].iter().map_windows(|&[a, b]| a + b);
1645    /// assert_eq!(it.next(), Some(4));  // 1 + 3
1646    /// assert_eq!(it.next(), Some(11)); // 3 + 8
1647    /// assert_eq!(it.next(), Some(9));  // 8 + 1
1648    /// assert_eq!(it.next(), None);
1649    /// ```
1650    ///
1651    /// Since the elements in the following example implement `Copy`, we can
1652    /// just copy the array and get an iterator over the windows.
1653    ///
1654    /// ```
1655    /// #![feature(iter_map_windows)]
1656    ///
1657    /// let mut it = "ferris".chars().map_windows(|w: &[_; 3]| *w);
1658    /// assert_eq!(it.next(), Some(['f', 'e', 'r']));
1659    /// assert_eq!(it.next(), Some(['e', 'r', 'r']));
1660    /// assert_eq!(it.next(), Some(['r', 'r', 'i']));
1661    /// assert_eq!(it.next(), Some(['r', 'i', 's']));
1662    /// assert_eq!(it.next(), None);
1663    /// ```
1664    ///
1665    /// You can also use this function to check the sortedness of an iterator.
1666    /// For the simple case, rather use [`Iterator::is_sorted`].
1667    ///
1668    /// ```
1669    /// #![feature(iter_map_windows)]
1670    ///
1671    /// let mut it = [0.5, 1.0, 3.5, 3.0, 8.5, 8.5, f32::NAN].iter()
1672    ///     .map_windows(|[a, b]| a <= b);
1673    ///
1674    /// assert_eq!(it.next(), Some(true));  // 0.5 <= 1.0
1675    /// assert_eq!(it.next(), Some(true));  // 1.0 <= 3.5
1676    /// assert_eq!(it.next(), Some(false)); // 3.5 <= 3.0
1677    /// assert_eq!(it.next(), Some(true));  // 3.0 <= 8.5
1678    /// assert_eq!(it.next(), Some(true));  // 8.5 <= 8.5
1679    /// assert_eq!(it.next(), Some(false)); // 8.5 <= NAN
1680    /// assert_eq!(it.next(), None);
1681    /// ```
1682    ///
1683    /// For non-fused iterators, they are fused after `map_windows`.
1684    ///
1685    /// ```
1686    /// #![feature(iter_map_windows)]
1687    ///
1688    /// #[derive(Default)]
1689    /// struct NonFusedIterator {
1690    ///     state: i32,
1691    /// }
1692    ///
1693    /// impl Iterator for NonFusedIterator {
1694    ///     type Item = i32;
1695    ///
1696    ///     fn next(&mut self) -> Option<i32> {
1697    ///         let val = self.state;
1698    ///         self.state = self.state + 1;
1699    ///
1700    ///         // yields `0..5` first, then only even numbers since `6..`.
1701    ///         if val < 5 || val % 2 == 0 {
1702    ///             Some(val)
1703    ///         } else {
1704    ///             None
1705    ///         }
1706    ///     }
1707    /// }
1708    ///
1709    ///
1710    /// let mut iter = NonFusedIterator::default();
1711    ///
1712    /// // yields 0..5 first.
1713    /// assert_eq!(iter.next(), Some(0));
1714    /// assert_eq!(iter.next(), Some(1));
1715    /// assert_eq!(iter.next(), Some(2));
1716    /// assert_eq!(iter.next(), Some(3));
1717    /// assert_eq!(iter.next(), Some(4));
1718    /// // then we can see our iterator going back and forth
1719    /// assert_eq!(iter.next(), None);
1720    /// assert_eq!(iter.next(), Some(6));
1721    /// assert_eq!(iter.next(), None);
1722    /// assert_eq!(iter.next(), Some(8));
1723    /// assert_eq!(iter.next(), None);
1724    ///
1725    /// // however, with `.map_windows()`, it is fused.
1726    /// let mut iter = NonFusedIterator::default()
1727    ///     .map_windows(|arr: &[_; 2]| *arr);
1728    ///
1729    /// assert_eq!(iter.next(), Some([0, 1]));
1730    /// assert_eq!(iter.next(), Some([1, 2]));
1731    /// assert_eq!(iter.next(), Some([2, 3]));
1732    /// assert_eq!(iter.next(), Some([3, 4]));
1733    /// assert_eq!(iter.next(), None);
1734    ///
1735    /// // it will always return `None` after the first time.
1736    /// assert_eq!(iter.next(), None);
1737    /// assert_eq!(iter.next(), None);
1738    /// assert_eq!(iter.next(), None);
1739    /// ```
1740    #[inline]
1741    #[unstable(feature = "iter_map_windows", issue = "87155")]
1742    #[rustc_non_const_trait_method]
1743    fn map_windows<F, R, const N: usize>(self, f: F) -> MapWindows<Self, F, N>
1744    where
1745        Self: Sized,
1746        F: FnMut(&[Self::Item; N]) -> R,
1747    {
1748        MapWindows::new(self, f)
1749    }
1750
1751    /// Creates an iterator which ends after the first [`None`].
1752    ///
1753    /// After an iterator returns [`None`], future calls may or may not yield
1754    /// [`Some(T)`] again. `fuse()` adapts an iterator, ensuring that after a
1755    /// [`None`] is given, it will always return [`None`] forever.
1756    ///
1757    /// Note that the [`Fuse`] wrapper is a no-op on iterators that implement
1758    /// the [`FusedIterator`] trait. `fuse()` may therefore behave incorrectly
1759    /// if the [`FusedIterator`] trait is improperly implemented.
1760    ///
1761    /// [`Some(T)`]: Some
1762    /// [`FusedIterator`]: crate::iter::FusedIterator
1763    ///
1764    /// # Examples
1765    ///
1766    /// ```
1767    /// // an iterator which alternates between Some and None
1768    /// struct Alternate {
1769    ///     state: i32,
1770    /// }
1771    ///
1772    /// impl Iterator for Alternate {
1773    ///     type Item = i32;
1774    ///
1775    ///     fn next(&mut self) -> Option<i32> {
1776    ///         let val = self.state;
1777    ///         self.state = self.state + 1;
1778    ///
1779    ///         // if it's even, Some(i32), else None
1780    ///         (val % 2 == 0).then_some(val)
1781    ///     }
1782    /// }
1783    ///
1784    /// let mut iter = Alternate { state: 0 };
1785    ///
1786    /// // we can see our iterator going back and forth
1787    /// assert_eq!(iter.next(), Some(0));
1788    /// assert_eq!(iter.next(), None);
1789    /// assert_eq!(iter.next(), Some(2));
1790    /// assert_eq!(iter.next(), None);
1791    ///
1792    /// // however, once we fuse it...
1793    /// let mut iter = iter.fuse();
1794    ///
1795    /// assert_eq!(iter.next(), Some(4));
1796    /// assert_eq!(iter.next(), None);
1797    ///
1798    /// // it will always return `None` after the first time.
1799    /// assert_eq!(iter.next(), None);
1800    /// assert_eq!(iter.next(), None);
1801    /// assert_eq!(iter.next(), None);
1802    /// ```
1803    #[inline]
1804    #[stable(feature = "rust1", since = "1.0.0")]
1805    #[rustc_non_const_trait_method]
1806    fn fuse(self) -> Fuse<Self>
1807    where
1808        Self: Sized,
1809    {
1810        Fuse::new(self)
1811    }
1812
1813    /// Does something with each element of an iterator, passing the value on.
1814    ///
1815    /// When using iterators, you'll often chain several of them together.
1816    /// While working on such code, you might want to check out what's
1817    /// happening at various parts in the pipeline. To do that, insert
1818    /// a call to `inspect()`.
1819    ///
1820    /// It's more common for `inspect()` to be used as a debugging tool than to
1821    /// exist in your final code, but applications may find it useful in certain
1822    /// situations when errors need to be logged before being discarded.
1823    ///
1824    /// # Examples
1825    ///
1826    /// Basic usage:
1827    ///
1828    /// ```
1829    /// let a = [1, 4, 2, 3];
1830    ///
1831    /// // this iterator sequence is complex.
1832    /// let sum = a.iter()
1833    ///     .cloned()
1834    ///     .filter(|x| x % 2 == 0)
1835    ///     .fold(0, |sum, i| sum + i);
1836    ///
1837    /// println!("{sum}");
1838    ///
1839    /// // let's add some inspect() calls to investigate what's happening
1840    /// let sum = a.iter()
1841    ///     .cloned()
1842    ///     .inspect(|x| println!("about to filter: {x}"))
1843    ///     .filter(|x| x % 2 == 0)
1844    ///     .inspect(|x| println!("made it through filter: {x}"))
1845    ///     .fold(0, |sum, i| sum + i);
1846    ///
1847    /// println!("{sum}");
1848    /// ```
1849    ///
1850    /// This will print:
1851    ///
1852    /// ```text
1853    /// 6
1854    /// about to filter: 1
1855    /// about to filter: 4
1856    /// made it through filter: 4
1857    /// about to filter: 2
1858    /// made it through filter: 2
1859    /// about to filter: 3
1860    /// 6
1861    /// ```
1862    ///
1863    /// Logging errors before discarding them:
1864    ///
1865    /// ```
1866    /// let lines = ["1", "2", "a"];
1867    ///
1868    /// let sum: i32 = lines
1869    ///     .iter()
1870    ///     .map(|line| line.parse::<i32>())
1871    ///     .inspect(|num| {
1872    ///         if let Err(ref e) = *num {
1873    ///             println!("Parsing error: {e}");
1874    ///         }
1875    ///     })
1876    ///     .filter_map(Result::ok)
1877    ///     .sum();
1878    ///
1879    /// println!("Sum: {sum}");
1880    /// ```
1881    ///
1882    /// This will print:
1883    ///
1884    /// ```text
1885    /// Parsing error: invalid digit found in string
1886    /// Sum: 3
1887    /// ```
1888    #[inline]
1889    #[stable(feature = "rust1", since = "1.0.0")]
1890    #[rustc_non_const_trait_method]
1891    fn inspect<F>(self, f: F) -> Inspect<Self, F>
1892    where
1893        Self: Sized,
1894        F: FnMut(&Self::Item),
1895    {
1896        Inspect::new(self, f)
1897    }
1898
1899    /// Creates a "by reference" adapter for this instance of `Iterator`.
1900    ///
1901    /// Consuming method calls (direct or indirect calls to `next`)
1902    /// on the "by reference" adapter will consume the original iterator,
1903    /// but ownership-taking methods (those with a `self` parameter)
1904    /// only take ownership of the "by reference" iterator.
1905    ///
1906    /// This is useful for applying ownership-taking methods
1907    /// (such as `take` in the example below)
1908    /// without giving up ownership of the original iterator,
1909    /// so you can use the original iterator afterwards.
1910    ///
1911    /// Uses [`impl<I: Iterator + ?Sized> Iterator for &mut I { type Item = I::Item; ...}`](Iterator#impl-Iterator-for-%26mut+I).
1912    ///
1913    /// # Examples
1914    ///
1915    /// ```
1916    /// let mut words = ["hello", "world", "of", "Rust"].into_iter();
1917    ///
1918    /// // Take the first two words.
1919    /// let hello_world: Vec<_> = words.by_ref().take(2).collect();
1920    /// assert_eq!(hello_world, vec!["hello", "world"]);
1921    ///
1922    /// // Collect the rest of the words.
1923    /// // We can only do this because we used `by_ref` earlier.
1924    /// let of_rust: Vec<_> = words.collect();
1925    /// assert_eq!(of_rust, vec!["of", "Rust"]);
1926    /// ```
1927    #[stable(feature = "rust1", since = "1.0.0")]
1928    fn by_ref(&mut self) -> &mut Self
1929    where
1930        Self: Sized,
1931    {
1932        self
1933    }
1934
1935    /// Transforms an iterator into a collection.
1936    ///
1937    /// `collect()` takes ownership of an iterator and produces whichever
1938    /// collection type you request. The iterator itself carries no knowledge of
1939    /// the eventual container; the target collection is chosen entirely by the
1940    /// type you ask `collect()` to return. This makes `collect()` one of the
1941    /// more powerful methods in the standard library, and it shows up in a wide
1942    /// variety of contexts.
1943    ///
1944    /// The most basic pattern in which `collect()` is used is to turn one
1945    /// collection into another. You take a collection, call [`iter`] on it,
1946    /// do a bunch of transformations, and then `collect()` at the end.
1947    ///
1948    /// `collect()` can also create instances of types that are not typical
1949    /// collections. For example, a [`String`] can be built from [`char`]s,
1950    /// and an iterator of [`Result<T, E>`][`Result`] items can be collected
1951    /// into `Result<Collection<T>, E>`. See the examples below for more.
1952    ///
1953    /// Because `collect()` is so general, it can cause problems with type
1954    /// inference. As such, `collect()` is one of the few times you'll see
1955    /// the syntax affectionately known as the 'turbofish': `::<>`. This
1956    /// helps the inference algorithm understand specifically which collection
1957    /// you're trying to collect into.
1958    ///
1959    /// # Examples
1960    ///
1961    /// Basic usage:
1962    ///
1963    /// ```
1964    /// let a = [1, 2, 3];
1965    ///
1966    /// let doubled: Vec<i32> = a.iter()
1967    ///                          .map(|x| x * 2)
1968    ///                          .collect();
1969    ///
1970    /// assert_eq!(vec![2, 4, 6], doubled);
1971    /// ```
1972    ///
1973    /// Note that we needed the `: Vec<i32>` on the left-hand side. This is because
1974    /// we could collect into, for example, a [`VecDeque<T>`] instead:
1975    ///
1976    /// [`VecDeque<T>`]: ../../std/collections/struct.VecDeque.html
1977    ///
1978    /// ```
1979    /// use std::collections::VecDeque;
1980    ///
1981    /// let a = [1, 2, 3];
1982    ///
1983    /// let doubled: VecDeque<i32> = a.iter().map(|x| x * 2).collect();
1984    ///
1985    /// assert_eq!(2, doubled[0]);
1986    /// assert_eq!(4, doubled[1]);
1987    /// assert_eq!(6, doubled[2]);
1988    /// ```
1989    ///
1990    /// Using the 'turbofish' instead of annotating `doubled`:
1991    ///
1992    /// ```
1993    /// let a = [1, 2, 3];
1994    ///
1995    /// let doubled = a.iter().map(|x| x * 2).collect::<Vec<i32>>();
1996    ///
1997    /// assert_eq!(vec![2, 4, 6], doubled);
1998    /// ```
1999    ///
2000    /// Because `collect()` only cares about what you're collecting into, you can
2001    /// still use a partial type hint, `_`, with the turbofish:
2002    ///
2003    /// ```
2004    /// let a = [1, 2, 3];
2005    ///
2006    /// let doubled = a.iter().map(|x| x * 2).collect::<Vec<_>>();
2007    ///
2008    /// assert_eq!(vec![2, 4, 6], doubled);
2009    /// ```
2010    ///
2011    /// Using `collect()` to make a [`String`]:
2012    ///
2013    /// ```
2014    /// let chars = ['g', 'd', 'k', 'k', 'n'];
2015    ///
2016    /// let hello: String = chars.into_iter()
2017    ///     .map(|x| x as u8)
2018    ///     .map(|x| (x + 1) as char)
2019    ///     .collect();
2020    ///
2021    /// assert_eq!("hello", hello);
2022    /// ```
2023    ///
2024    /// If you have a list of [`Result<T, E>`][`Result`]s, you can use `collect()` to
2025    /// see if any of them failed:
2026    ///
2027    /// ```
2028    /// let results = [Ok(1), Err("nope"), Ok(3), Err("bad")];
2029    ///
2030    /// let result: Result<Vec<_>, &str> = results.into_iter().collect();
2031    ///
2032    /// // gives us the first error
2033    /// assert_eq!(Err("nope"), result);
2034    ///
2035    /// let results = [Ok(1), Ok(3)];
2036    ///
2037    /// let result: Result<Vec<_>, &str> = results.into_iter().collect();
2038    ///
2039    /// // gives us the list of answers
2040    /// assert_eq!(Ok(vec![1, 3]), result);
2041    /// ```
2042    ///
2043    /// [`iter`]: Iterator::next
2044    /// [`String`]: ../../std/string/struct.String.html
2045    /// [`char`]: type@char
2046    #[inline]
2047    #[stable(feature = "rust1", since = "1.0.0")]
2048    #[must_use = "if you really need to exhaust the iterator, consider `.for_each(drop)` instead"]
2049    #[rustc_diagnostic_item = "iterator_collect_fn"]
2050    #[rustc_non_const_trait_method]
2051    fn collect<B: FromIterator<Self::Item>>(self) -> B
2052    where
2053        Self: Sized,
2054    {
2055        // This is too aggressive to turn on for everything all the time, but PR#137908
2056        // accidentally noticed that some rustc iterators had malformed `size_hint`s,
2057        // so this will help catch such things in debug-assertions-std runners,
2058        // even if users won't actually ever see it.
2059        if cfg!(debug_assertions) {
2060            let hint = self.size_hint();
2061            assert!(hint.1.is_none_or(|high| high >= hint.0), "Malformed size_hint {hint:?}");
2062        }
2063
2064        FromIterator::from_iter(self)
2065    }
2066
2067    /// Fallibly transforms an iterator into a collection, short circuiting if
2068    /// a failure is encountered.
2069    ///
2070    /// `try_collect()` is a variation of [`collect()`][`collect`] that allows fallible
2071    /// conversions during collection. Its main use case is simplifying conversions from
2072    /// iterators yielding [`Option<T>`][`Option`] into `Option<Collection<T>>`, or similarly for other [`Try`]
2073    /// types (e.g. [`Result`]).
2074    ///
2075    /// Importantly, `try_collect()` doesn't require that the outer [`Try`] type also implements [`FromIterator`];
2076    /// only the inner type produced on `Try::Output` must implement it. Concretely,
2077    /// this means that collecting into `ControlFlow<_, Vec<i32>>` is valid because `Vec<i32>` implements
2078    /// [`FromIterator`], even though [`ControlFlow`] doesn't.
2079    ///
2080    /// Also, if a failure is encountered during `try_collect()`, the iterator is still valid and
2081    /// may continue to be used, in which case it will continue iterating starting after the element that
2082    /// triggered the failure. See the last example below for an example of how this works.
2083    ///
2084    /// # Examples
2085    /// Successfully collecting an iterator of `Option<i32>` into `Option<Vec<i32>>`:
2086    /// ```
2087    /// #![feature(iterator_try_collect)]
2088    ///
2089    /// let u = vec![Some(1), Some(2), Some(3)];
2090    /// let v = u.into_iter().try_collect::<Vec<i32>>();
2091    /// assert_eq!(v, Some(vec![1, 2, 3]));
2092    /// ```
2093    ///
2094    /// Failing to collect in the same way:
2095    /// ```
2096    /// #![feature(iterator_try_collect)]
2097    ///
2098    /// let u = vec![Some(1), Some(2), None, Some(3)];
2099    /// let v = u.into_iter().try_collect::<Vec<i32>>();
2100    /// assert_eq!(v, None);
2101    /// ```
2102    ///
2103    /// A similar example, but with `Result`:
2104    /// ```
2105    /// #![feature(iterator_try_collect)]
2106    ///
2107    /// let u: Vec<Result<i32, ()>> = vec![Ok(1), Ok(2), Ok(3)];
2108    /// let v = u.into_iter().try_collect::<Vec<i32>>();
2109    /// assert_eq!(v, Ok(vec![1, 2, 3]));
2110    ///
2111    /// let u = vec![Ok(1), Ok(2), Err(()), Ok(3)];
2112    /// let v = u.into_iter().try_collect::<Vec<i32>>();
2113    /// assert_eq!(v, Err(()));
2114    /// ```
2115    ///
2116    /// Finally, even [`ControlFlow`] works, despite the fact that it
2117    /// doesn't implement [`FromIterator`]. Note also that the iterator can
2118    /// continue to be used, even if a failure is encountered:
2119    ///
2120    /// ```
2121    /// #![feature(iterator_try_collect)]
2122    ///
2123    /// use core::ops::ControlFlow::{Break, Continue};
2124    ///
2125    /// let u = [Continue(1), Continue(2), Break(3), Continue(4), Continue(5)];
2126    /// let mut it = u.into_iter();
2127    ///
2128    /// let v = it.try_collect::<Vec<_>>();
2129    /// assert_eq!(v, Break(3));
2130    ///
2131    /// let v = it.try_collect::<Vec<_>>();
2132    /// assert_eq!(v, Continue(vec![4, 5]));
2133    /// ```
2134    ///
2135    /// [`collect`]: Iterator::collect
2136    #[inline]
2137    #[unstable(feature = "iterator_try_collect", issue = "94047")]
2138    #[rustc_non_const_trait_method]
2139    fn try_collect<B>(&mut self) -> ChangeOutputType<Self::Item, B>
2140    where
2141        Self: Sized,
2142        Self::Item: Try<Residual: Residual<B>>,
2143        B: FromIterator<<Self::Item as Try>::Output>,
2144    {
2145        try_process(ByRefSized(self), |i| i.collect())
2146    }
2147
2148    /// Collects all the items from an iterator into a collection.
2149    ///
2150    /// This method consumes the iterator and adds all its items to the
2151    /// passed collection. The collection is then returned, so the call chain
2152    /// can be continued.
2153    ///
2154    /// This is useful when you already have a collection and want to add
2155    /// the iterator items to it.
2156    ///
2157    /// This method is a convenience method to call [Extend::extend](trait.Extend.html),
2158    /// but instead of being called on a collection, it's called on an iterator.
2159    ///
2160    /// # Examples
2161    ///
2162    /// Basic usage:
2163    ///
2164    /// ```
2165    /// #![feature(iter_collect_into)]
2166    ///
2167    /// let a = [1, 2, 3];
2168    /// let mut vec: Vec::<i32> = vec![0, 1];
2169    ///
2170    /// a.iter().map(|x| x * 2).collect_into(&mut vec);
2171    /// a.iter().map(|x| x * 10).collect_into(&mut vec);
2172    ///
2173    /// assert_eq!(vec, vec![0, 1, 2, 4, 6, 10, 20, 30]);
2174    /// ```
2175    ///
2176    /// `Vec` can have a manual set capacity to avoid reallocating it:
2177    ///
2178    /// ```
2179    /// #![feature(iter_collect_into)]
2180    ///
2181    /// let a = [1, 2, 3];
2182    /// let mut vec: Vec::<i32> = Vec::with_capacity(6);
2183    ///
2184    /// a.iter().map(|x| x * 2).collect_into(&mut vec);
2185    /// a.iter().map(|x| x * 10).collect_into(&mut vec);
2186    ///
2187    /// assert_eq!(6, vec.capacity());
2188    /// assert_eq!(vec, vec![2, 4, 6, 10, 20, 30]);
2189    /// ```
2190    ///
2191    /// The returned mutable reference can be used to continue the call chain:
2192    ///
2193    /// ```
2194    /// #![feature(iter_collect_into)]
2195    ///
2196    /// let a = [1, 2, 3];
2197    /// let mut vec: Vec::<i32> = Vec::with_capacity(6);
2198    ///
2199    /// let count = a.iter().collect_into(&mut vec).iter().count();
2200    ///
2201    /// assert_eq!(count, vec.len());
2202    /// assert_eq!(vec, vec![1, 2, 3]);
2203    ///
2204    /// let count = a.iter().collect_into(&mut vec).iter().count();
2205    ///
2206    /// assert_eq!(count, vec.len());
2207    /// assert_eq!(vec, vec![1, 2, 3, 1, 2, 3]);
2208    /// ```
2209    #[inline]
2210    #[unstable(feature = "iter_collect_into", issue = "94780")]
2211    #[rustc_non_const_trait_method]
2212    fn collect_into<E: Extend<Self::Item>>(self, collection: &mut E) -> &mut E
2213    where
2214        Self: Sized,
2215    {
2216        collection.extend(self);
2217        collection
2218    }
2219
2220    /// Consumes an iterator, creating two collections from it.
2221    ///
2222    /// The predicate passed to `partition()` can return `true`, or `false`.
2223    /// `partition()` returns a pair, all of the elements for which it returned
2224    /// `true`, and all of the elements for which it returned `false`.
2225    ///
2226    /// See also [`is_partitioned()`] and [`partition_in_place()`].
2227    ///
2228    /// [`is_partitioned()`]: Iterator::is_partitioned
2229    /// [`partition_in_place()`]: Iterator::partition_in_place
2230    ///
2231    /// # Examples
2232    ///
2233    /// ```
2234    /// let a = [1, 2, 3];
2235    ///
2236    /// let (even, odd): (Vec<_>, Vec<_>) = a
2237    ///     .into_iter()
2238    ///     .partition(|n| n % 2 == 0);
2239    ///
2240    /// assert_eq!(even, [2]);
2241    /// assert_eq!(odd, [1, 3]);
2242    /// ```
2243    #[stable(feature = "rust1", since = "1.0.0")]
2244    #[rustc_non_const_trait_method]
2245    fn partition<B, F>(self, f: F) -> (B, B)
2246    where
2247        Self: Sized,
2248        B: Default + Extend<Self::Item>,
2249        F: FnMut(&Self::Item) -> bool,
2250    {
2251        #[inline]
2252        fn extend<'a, T, B: Extend<T>>(
2253            mut f: impl FnMut(&T) -> bool + 'a,
2254            left: &'a mut B,
2255            right: &'a mut B,
2256        ) -> impl FnMut((), T) + 'a {
2257            move |(), x| {
2258                if f(&x) {
2259                    left.extend_one(x);
2260                } else {
2261                    right.extend_one(x);
2262                }
2263            }
2264        }
2265
2266        let mut left: B = Default::default();
2267        let mut right: B = Default::default();
2268
2269        self.fold((), extend(f, &mut left, &mut right));
2270
2271        (left, right)
2272    }
2273
2274    /// Reorders the elements of this iterator *in-place* according to the given predicate,
2275    /// such that all those that return `true` precede all those that return `false`.
2276    /// Returns the number of `true` elements found.
2277    ///
2278    /// The relative order of partitioned items is not maintained.
2279    ///
2280    /// # Current implementation
2281    ///
2282    /// The current algorithm tries to find the first element for which the predicate evaluates
2283    /// to false and the last element for which it evaluates to true, and repeatedly swaps them.
2284    ///
2285    /// Time complexity: *O*(*n*)
2286    ///
2287    /// See also [`is_partitioned()`] and [`partition()`].
2288    ///
2289    /// [`is_partitioned()`]: Iterator::is_partitioned
2290    /// [`partition()`]: Iterator::partition
2291    ///
2292    /// # Examples
2293    ///
2294    /// ```
2295    /// #![feature(iter_partition_in_place)]
2296    ///
2297    /// let mut a = [1, 2, 3, 4, 5, 6, 7];
2298    ///
2299    /// // Partition in-place between evens and odds
2300    /// let i = a.iter_mut().partition_in_place(|n| n % 2 == 0);
2301    ///
2302    /// assert_eq!(i, 3);
2303    /// assert!(a[..i].iter().all(|n| n % 2 == 0)); // evens
2304    /// assert!(a[i..].iter().all(|n| n % 2 == 1)); // odds
2305    /// ```
2306    #[unstable(feature = "iter_partition_in_place", issue = "62543")]
2307    #[rustc_non_const_trait_method]
2308    fn partition_in_place<'a, T: 'a, P>(mut self, ref mut predicate: P) -> usize
2309    where
2310        Self: Sized + DoubleEndedIterator<Item = &'a mut T>,
2311        P: FnMut(&T) -> bool,
2312    {
2313        // FIXME: should we worry about the count overflowing? The only way to have more than
2314        // `usize::MAX` mutable references is with ZSTs, which aren't useful to partition...
2315
2316        // These closure "factory" functions exist to avoid genericity in `Self`.
2317
2318        #[inline]
2319        fn is_false<'a, T>(
2320            predicate: &'a mut impl FnMut(&T) -> bool,
2321            true_count: &'a mut usize,
2322        ) -> impl FnMut(&&mut T) -> bool + 'a {
2323            move |x| {
2324                let p = predicate(&**x);
2325                *true_count += p as usize;
2326                !p
2327            }
2328        }
2329
2330        #[inline]
2331        fn is_true<T>(predicate: &mut impl FnMut(&T) -> bool) -> impl FnMut(&&mut T) -> bool + '_ {
2332            move |x| predicate(&**x)
2333        }
2334
2335        // Repeatedly find the first `false` and swap it with the last `true`.
2336        let mut true_count = 0;
2337        while let Some(head) = self.find(is_false(predicate, &mut true_count)) {
2338            if let Some(tail) = self.rfind(is_true(predicate)) {
2339                crate::mem::swap(head, tail);
2340                true_count += 1;
2341            } else {
2342                break;
2343            }
2344        }
2345        true_count
2346    }
2347
2348    /// Checks if the elements of this iterator are partitioned according to the given predicate,
2349    /// such that all those that return `true` precede all those that return `false`.
2350    ///
2351    /// See also [`partition()`] and [`partition_in_place()`].
2352    ///
2353    /// [`partition()`]: Iterator::partition
2354    /// [`partition_in_place()`]: Iterator::partition_in_place
2355    ///
2356    /// # Examples
2357    ///
2358    /// ```
2359    /// #![feature(iter_is_partitioned)]
2360    ///
2361    /// assert!("Iterator".chars().is_partitioned(char::is_uppercase));
2362    /// assert!(!"IntoIterator".chars().is_partitioned(char::is_uppercase));
2363    /// ```
2364    #[unstable(feature = "iter_is_partitioned", issue = "62544")]
2365    #[rustc_non_const_trait_method]
2366    fn is_partitioned<P>(mut self, mut predicate: P) -> bool
2367    where
2368        Self: Sized,
2369        P: FnMut(Self::Item) -> bool,
2370    {
2371        // Either all items test `true`, or the first clause stops at `false`
2372        // and we check that there are no more `true` items after that.
2373        self.all(&mut predicate) || !self.any(predicate)
2374    }
2375
2376    /// An iterator method that applies a function as long as it returns
2377    /// successfully, producing a single, final value.
2378    ///
2379    /// `try_fold()` takes two arguments: an initial value, and a closure with
2380    /// two arguments: an 'accumulator', and an element. The closure either
2381    /// returns successfully, with the value that the accumulator should have
2382    /// for the next iteration, or it returns failure, with an error value that
2383    /// is propagated back to the caller immediately (short-circuiting).
2384    ///
2385    /// The initial value is the value the accumulator will have on the first
2386    /// call. If applying the closure succeeded against every element of the
2387    /// iterator, `try_fold()` returns the final accumulator as success.
2388    ///
2389    /// Folding is useful whenever you have a collection of something, and want
2390    /// to produce a single value from it.
2391    ///
2392    /// # Note to Implementors
2393    ///
2394    /// Several of the other (forward) methods have default implementations in
2395    /// terms of this one, so try to implement this explicitly if it can
2396    /// do something better than the default `for` loop implementation.
2397    ///
2398    /// In particular, try to have this call `try_fold()` on the internal parts
2399    /// from which this iterator is composed. If multiple calls are needed,
2400    /// the `?` operator may be convenient for chaining the accumulator value
2401    /// along, but beware any invariants that need to be upheld before those
2402    /// early returns. This is a `&mut self` method, so iteration needs to be
2403    /// resumable after hitting an error here.
2404    ///
2405    /// # Examples
2406    ///
2407    /// Basic usage:
2408    ///
2409    /// ```
2410    /// let a = [1, 2, 3];
2411    ///
2412    /// // the checked sum of all of the elements of the array
2413    /// let sum = a.into_iter().try_fold(0i8, |acc, x| acc.checked_add(x));
2414    ///
2415    /// assert_eq!(sum, Some(6));
2416    /// ```
2417    ///
2418    /// Short-circuiting:
2419    ///
2420    /// ```
2421    /// let a = [10, 20, 30, 100, 40, 50];
2422    /// let mut iter = a.into_iter();
2423    ///
2424    /// // This sum overflows when adding the 100 element
2425    /// let sum = iter.try_fold(0i8, |acc, x| acc.checked_add(x));
2426    /// assert_eq!(sum, None);
2427    ///
2428    /// // Because it short-circuited, the remaining elements are still
2429    /// // available through the iterator.
2430    /// assert_eq!(iter.len(), 2);
2431    /// assert_eq!(iter.next(), Some(40));
2432    /// ```
2433    ///
2434    /// While you cannot `break` from a closure, the [`ControlFlow`] type allows
2435    /// a similar idea:
2436    ///
2437    /// ```
2438    /// use std::ops::ControlFlow;
2439    ///
2440    /// let triangular = (1..30).try_fold(0_i8, |prev, x| {
2441    ///     if let Some(next) = prev.checked_add(x) {
2442    ///         ControlFlow::Continue(next)
2443    ///     } else {
2444    ///         ControlFlow::Break(prev)
2445    ///     }
2446    /// });
2447    /// assert_eq!(triangular, ControlFlow::Break(120));
2448    ///
2449    /// let triangular = (1..30).try_fold(0_u64, |prev, x| {
2450    ///     if let Some(next) = prev.checked_add(x) {
2451    ///         ControlFlow::Continue(next)
2452    ///     } else {
2453    ///         ControlFlow::Break(prev)
2454    ///     }
2455    /// });
2456    /// assert_eq!(triangular, ControlFlow::Continue(435));
2457    /// ```
2458    #[inline]
2459    #[stable(feature = "iterator_try_fold", since = "1.27.0")]
2460    #[rustc_non_const_trait_method]
2461    fn try_fold<B, F, R>(&mut self, init: B, mut f: F) -> R
2462    where
2463        Self: Sized,
2464        F: FnMut(B, Self::Item) -> R,
2465        R: Try<Output = B>,
2466    {
2467        let mut accum = init;
2468        while let Some(x) = self.next() {
2469            accum = f(accum, x)?;
2470        }
2471        try { accum }
2472    }
2473
2474    /// An iterator method that applies a fallible function to each item in the
2475    /// iterator, stopping at the first error and returning that error.
2476    ///
2477    /// This can also be thought of as the fallible form of [`for_each()`]
2478    /// or as the stateless version of [`try_fold()`].
2479    ///
2480    /// [`for_each()`]: Iterator::for_each
2481    /// [`try_fold()`]: Iterator::try_fold
2482    ///
2483    /// # Examples
2484    ///
2485    /// ```
2486    /// use std::fs::rename;
2487    /// use std::io::{stdout, Write};
2488    /// use std::path::Path;
2489    ///
2490    /// let data = ["no_tea.txt", "stale_bread.json", "torrential_rain.png"];
2491    ///
2492    /// let res = data.iter().try_for_each(|x| writeln!(stdout(), "{x}"));
2493    /// assert!(res.is_ok());
2494    ///
2495    /// let mut it = data.iter().cloned();
2496    /// let res = it.try_for_each(|x| rename(x, Path::new(x).with_extension("old")));
2497    /// assert!(res.is_err());
2498    /// // It short-circuited, so the remaining items are still in the iterator:
2499    /// assert_eq!(it.next(), Some("stale_bread.json"));
2500    /// ```
2501    ///
2502    /// The [`ControlFlow`] type can be used with this method for the situations
2503    /// in which you'd use `break` and `continue` in a normal loop:
2504    ///
2505    /// ```
2506    /// use std::ops::ControlFlow;
2507    ///
2508    /// let r = (2..100).try_for_each(|x| {
2509    ///     if 323 % x == 0 {
2510    ///         return ControlFlow::Break(x)
2511    ///     }
2512    ///
2513    ///     ControlFlow::Continue(())
2514    /// });
2515    /// assert_eq!(r, ControlFlow::Break(17));
2516    /// ```
2517    #[inline]
2518    #[stable(feature = "iterator_try_fold", since = "1.27.0")]
2519    #[rustc_non_const_trait_method]
2520    fn try_for_each<F, R>(&mut self, f: F) -> R
2521    where
2522        Self: Sized,
2523        F: FnMut(Self::Item) -> R,
2524        R: Try<Output = ()>,
2525    {
2526        #[inline]
2527        fn call<T, R>(mut f: impl FnMut(T) -> R) -> impl FnMut((), T) -> R {
2528            move |(), x| f(x)
2529        }
2530
2531        self.try_fold((), call(f))
2532    }
2533
2534    /// Folds every element into an accumulator by applying an operation,
2535    /// returning the final result.
2536    ///
2537    /// `fold()` takes two arguments: an initial value, and a closure with two
2538    /// arguments: an 'accumulator', and an element. The closure returns the value that
2539    /// the accumulator should have for the next iteration.
2540    ///
2541    /// The initial value is the value the accumulator will have on the first
2542    /// call.
2543    ///
2544    /// After applying this closure to every element of the iterator, `fold()`
2545    /// returns the accumulator.
2546    ///
2547    /// This operation is sometimes called 'reduce' or 'inject'.
2548    ///
2549    /// Folding is useful whenever you have a collection of something, and want
2550    /// to produce a single value from it.
2551    ///
2552    /// Note: `fold()`, and similar methods that traverse the entire iterator,
2553    /// might not terminate for infinite iterators, even on traits for which a
2554    /// result is determinable in finite time.
2555    ///
2556    /// Note: [`reduce()`] can be used to use the first element as the initial
2557    /// value, if the accumulator type and item type is the same.
2558    ///
2559    /// Note: `fold()` combines elements in a *left-associative* fashion. For associative
2560    /// operators like `+`, the order the elements are combined in is not important, but for non-associative
2561    /// operators like `-` the order will affect the final result.
2562    /// For a *right-associative* version of `fold()`, see [`DoubleEndedIterator::rfold()`].
2563    ///
2564    /// # Note to Implementors
2565    ///
2566    /// Several of the other (forward) methods have default implementations in
2567    /// terms of this one, so try to implement this explicitly if it can
2568    /// do something better than the default `for` loop implementation.
2569    ///
2570    /// In particular, try to have this call `fold()` on the internal parts
2571    /// from which this iterator is composed.
2572    ///
2573    /// # Examples
2574    ///
2575    /// Basic usage:
2576    ///
2577    /// ```
2578    /// let a = [1, 2, 3];
2579    ///
2580    /// // the sum of all of the elements of the array
2581    /// let sum = a.iter().fold(0, |acc, x| acc + x);
2582    ///
2583    /// assert_eq!(sum, 6);
2584    /// ```
2585    ///
2586    /// Let's walk through each step of the iteration here:
2587    ///
2588    /// | element | acc | x | result |
2589    /// |---------|-----|---|--------|
2590    /// |         | 0   |   |        |
2591    /// | 1       | 0   | 1 | 1      |
2592    /// | 2       | 1   | 2 | 3      |
2593    /// | 3       | 3   | 3 | 6      |
2594    ///
2595    /// And so, our final result, `6`.
2596    ///
2597    /// This example demonstrates the left-associative nature of `fold()`:
2598    /// it builds a string, starting with an initial value
2599    /// and continuing with each element from the front until the back:
2600    ///
2601    /// ```
2602    /// let numbers = [1, 2, 3, 4, 5];
2603    ///
2604    /// let zero = "0".to_string();
2605    ///
2606    /// let result = numbers.iter().fold(zero, |acc, &x| {
2607    ///     format!("({acc} + {x})")
2608    /// });
2609    ///
2610    /// assert_eq!(result, "(((((0 + 1) + 2) + 3) + 4) + 5)");
2611    /// ```
2612    /// It's common for people who haven't used iterators a lot to
2613    /// use a `for` loop with a list of things to build up a result. Those
2614    /// can be turned into `fold()`s:
2615    ///
2616    /// [`for`]: ../../book/ch03-05-control-flow.html#looping-through-a-collection-with-for
2617    ///
2618    /// ```
2619    /// let numbers = [1, 2, 3, 4, 5];
2620    ///
2621    /// let mut result = 0;
2622    ///
2623    /// // for loop:
2624    /// for i in &numbers {
2625    ///     result = result + i;
2626    /// }
2627    ///
2628    /// // fold:
2629    /// let result2 = numbers.iter().fold(0, |acc, &x| acc + x);
2630    ///
2631    /// // they're the same
2632    /// assert_eq!(result, result2);
2633    /// ```
2634    ///
2635    /// [`reduce()`]: Iterator::reduce
2636    #[doc(alias = "inject", alias = "foldl")]
2637    #[inline]
2638    #[stable(feature = "rust1", since = "1.0.0")]
2639    #[rustc_non_const_trait_method]
2640    fn fold<B, F>(mut self, init: B, mut f: F) -> B
2641    where
2642        Self: Sized,
2643        F: FnMut(B, Self::Item) -> B,
2644    {
2645        let mut accum = init;
2646        while let Some(x) = self.next() {
2647            accum = f(accum, x);
2648        }
2649        accum
2650    }
2651
2652    /// Reduces the elements to a single one, by repeatedly applying a reducing
2653    /// operation.
2654    ///
2655    /// If the iterator is empty, returns [`None`]; otherwise, returns the
2656    /// result of the reduction.
2657    ///
2658    /// The reducing function is a closure with two arguments: an 'accumulator', and an element.
2659    /// For iterators with at least one element, this is the same as [`fold()`]
2660    /// with the first element of the iterator as the initial accumulator value, folding
2661    /// every subsequent element into it.
2662    ///
2663    /// [`fold()`]: Iterator::fold
2664    ///
2665    /// # Example
2666    ///
2667    /// ```
2668    /// let reduced: i32 = (1..10).reduce(|acc, e| acc + e).unwrap_or(0);
2669    /// assert_eq!(reduced, 45);
2670    ///
2671    /// // Which is equivalent to doing it with `fold`:
2672    /// let folded: i32 = (1..10).fold(0, |acc, e| acc + e);
2673    /// assert_eq!(reduced, folded);
2674    /// ```
2675    #[inline]
2676    #[stable(feature = "iterator_fold_self", since = "1.51.0")]
2677    #[rustc_non_const_trait_method]
2678    fn reduce<F>(mut self, f: F) -> Option<Self::Item>
2679    where
2680        Self: Sized,
2681        F: FnMut(Self::Item, Self::Item) -> Self::Item,
2682    {
2683        let first = self.next()?;
2684        Some(self.fold(first, f))
2685    }
2686
2687    /// Reduces the elements to a single one by repeatedly applying a reducing operation. If the
2688    /// closure returns a failure, the failure is propagated back to the caller immediately.
2689    ///
2690    /// The return type of this method depends on the return type of the closure. If the closure
2691    /// returns `Result<Self::Item, E>`, then this function will return `Result<Option<Self::Item>,
2692    /// E>`. If the closure returns `Option<Self::Item>`, then this function will return
2693    /// `Option<Option<Self::Item>>`.
2694    ///
2695    /// When called on an empty iterator, this function will return either `Some(None)` or
2696    /// `Ok(None)` depending on the type of the provided closure.
2697    ///
2698    /// For iterators with at least one element, this is essentially the same as calling
2699    /// [`try_fold()`] with the first element of the iterator as the initial accumulator value.
2700    ///
2701    /// [`try_fold()`]: Iterator::try_fold
2702    ///
2703    /// # Examples
2704    ///
2705    /// Safely calculate the sum of a series of numbers:
2706    ///
2707    /// ```
2708    /// #![feature(iterator_try_reduce)]
2709    ///
2710    /// let numbers: Vec<usize> = vec![10, 20, 5, 23, 0];
2711    /// let sum = numbers.into_iter().try_reduce(|x, y| x.checked_add(y));
2712    /// assert_eq!(sum, Some(Some(58)));
2713    /// ```
2714    ///
2715    /// Determine when a reduction short circuited:
2716    ///
2717    /// ```
2718    /// #![feature(iterator_try_reduce)]
2719    ///
2720    /// let numbers = vec![1, 2, 3, usize::MAX, 4, 5];
2721    /// let sum = numbers.into_iter().try_reduce(|x, y| x.checked_add(y));
2722    /// assert_eq!(sum, None);
2723    /// ```
2724    ///
2725    /// Determine when a reduction was not performed because there are no elements:
2726    ///
2727    /// ```
2728    /// #![feature(iterator_try_reduce)]
2729    ///
2730    /// let numbers: Vec<usize> = Vec::new();
2731    /// let sum = numbers.into_iter().try_reduce(|x, y| x.checked_add(y));
2732    /// assert_eq!(sum, Some(None));
2733    /// ```
2734    ///
2735    /// Use a [`Result`] instead of an [`Option`]:
2736    ///
2737    /// ```
2738    /// #![feature(iterator_try_reduce)]
2739    ///
2740    /// let numbers = vec!["1", "2", "3", "4", "5"];
2741    /// let max: Result<Option<_>, <usize as std::str::FromStr>::Err> =
2742    ///     numbers.into_iter().try_reduce(|x, y| {
2743    ///         if x.parse::<usize>()? > y.parse::<usize>()? { Ok(x) } else { Ok(y) }
2744    ///     });
2745    /// assert_eq!(max, Ok(Some("5")));
2746    /// ```
2747    #[inline]
2748    #[unstable(feature = "iterator_try_reduce", issue = "87053")]
2749    #[rustc_non_const_trait_method]
2750    fn try_reduce<R>(
2751        &mut self,
2752        f: impl FnMut(Self::Item, Self::Item) -> R,
2753    ) -> ChangeOutputType<R, Option<R::Output>>
2754    where
2755        Self: Sized,
2756        R: Try<Output = Self::Item, Residual: Residual<Option<Self::Item>>>,
2757    {
2758        let first = match self.next() {
2759            Some(i) => i,
2760            None => return Try::from_output(None),
2761        };
2762
2763        match self.try_fold(first, f).branch() {
2764            ControlFlow::Break(r) => FromResidual::from_residual(r),
2765            ControlFlow::Continue(i) => Try::from_output(Some(i)),
2766        }
2767    }
2768
2769    /// Tests if every element of the iterator matches a predicate.
2770    ///
2771    /// `all()` takes a closure that returns `true` or `false`. It applies
2772    /// this closure to each element of the iterator, and if they all return
2773    /// `true`, then so does `all()`. If any of them return `false`, it
2774    /// returns `false`.
2775    ///
2776    /// `all()` is short-circuiting; in other words, it will stop processing
2777    /// as soon as it finds a `false`, given that no matter what else happens,
2778    /// the result will also be `false`.
2779    ///
2780    /// An empty iterator returns `true`.
2781    ///
2782    /// # Examples
2783    ///
2784    /// Basic usage:
2785    ///
2786    /// ```
2787    /// let a = [1, 2, 3];
2788    ///
2789    /// assert!(a.into_iter().all(|x| x > 0));
2790    ///
2791    /// assert!(!a.into_iter().all(|x| x > 2));
2792    /// ```
2793    ///
2794    /// Stopping at the first `false`:
2795    ///
2796    /// ```
2797    /// let a = [1, 2, 3];
2798    ///
2799    /// let mut iter = a.into_iter();
2800    ///
2801    /// assert!(!iter.all(|x| x != 2));
2802    ///
2803    /// // we can still use `iter`, as there are more elements.
2804    /// assert_eq!(iter.next(), Some(3));
2805    /// ```
2806    #[inline]
2807    #[stable(feature = "rust1", since = "1.0.0")]
2808    #[rustc_non_const_trait_method]
2809    fn all<F>(&mut self, f: F) -> bool
2810    where
2811        Self: Sized,
2812        F: FnMut(Self::Item) -> bool,
2813    {
2814        #[inline]
2815        fn check<T>(mut f: impl FnMut(T) -> bool) -> impl FnMut((), T) -> ControlFlow<()> {
2816            move |(), x| {
2817                if f(x) { ControlFlow::Continue(()) } else { ControlFlow::Break(()) }
2818            }
2819        }
2820        self.try_fold((), check(f)) == ControlFlow::Continue(())
2821    }
2822
2823    /// Tests if any element of the iterator matches a predicate.
2824    ///
2825    /// `any()` takes a closure that returns `true` or `false`. It applies
2826    /// this closure to each element of the iterator, and if any of them return
2827    /// `true`, then so does `any()`. If they all return `false`, it
2828    /// returns `false`.
2829    ///
2830    /// `any()` is short-circuiting; in other words, it will stop processing
2831    /// as soon as it finds a `true`, given that no matter what else happens,
2832    /// the result will also be `true`.
2833    ///
2834    /// An empty iterator returns `false`.
2835    ///
2836    /// # Examples
2837    ///
2838    /// Basic usage:
2839    ///
2840    /// ```
2841    /// let a = [1, 2, 3];
2842    ///
2843    /// assert!(a.into_iter().any(|x| x > 0));
2844    ///
2845    /// assert!(!a.into_iter().any(|x| x > 5));
2846    /// ```
2847    ///
2848    /// Stopping at the first `true`:
2849    ///
2850    /// ```
2851    /// let a = [1, 2, 3];
2852    ///
2853    /// let mut iter = a.into_iter();
2854    ///
2855    /// assert!(iter.any(|x| x != 2));
2856    ///
2857    /// // we can still use `iter`, as there are more elements.
2858    /// assert_eq!(iter.next(), Some(2));
2859    /// ```
2860    #[inline]
2861    #[stable(feature = "rust1", since = "1.0.0")]
2862    #[rustc_non_const_trait_method]
2863    fn any<F>(&mut self, f: F) -> bool
2864    where
2865        Self: Sized,
2866        F: FnMut(Self::Item) -> bool,
2867    {
2868        #[inline]
2869        fn check<T>(mut f: impl FnMut(T) -> bool) -> impl FnMut((), T) -> ControlFlow<()> {
2870            move |(), x| {
2871                if f(x) { ControlFlow::Break(()) } else { ControlFlow::Continue(()) }
2872            }
2873        }
2874
2875        self.try_fold((), check(f)) == ControlFlow::Break(())
2876    }
2877
2878    /// Searches for an element of an iterator that satisfies a predicate.
2879    ///
2880    /// `find()` takes a closure that returns `true` or `false`. It applies
2881    /// this closure to each element of the iterator, and if any of them return
2882    /// `true`, then `find()` returns [`Some(element)`]. If they all return
2883    /// `false`, it returns [`None`].
2884    ///
2885    /// `find()` is short-circuiting; in other words, it will stop processing
2886    /// as soon as the closure returns `true`.
2887    ///
2888    /// Because `find()` takes a reference, and many iterators iterate over
2889    /// references, this leads to a possibly confusing situation where the
2890    /// argument is a double reference. You can see this effect in the
2891    /// examples below, with `&&x`.
2892    ///
2893    /// If you need the index of the element, see [`position()`].
2894    ///
2895    /// [`Some(element)`]: Some
2896    /// [`position()`]: Iterator::position
2897    ///
2898    /// # Examples
2899    ///
2900    /// Basic usage:
2901    ///
2902    /// ```
2903    /// let a = [1, 2, 3];
2904    ///
2905    /// assert_eq!(a.into_iter().find(|&x| x == 2), Some(2));
2906    /// assert_eq!(a.into_iter().find(|&x| x == 5), None);
2907    /// ```
2908    ///
2909    /// Iterating over references:
2910    ///
2911    /// ```
2912    /// let a = [1, 2, 3];
2913    ///
2914    /// // `iter()` yields references i.e. `&i32` and `find()` takes a
2915    /// // reference to each element.
2916    /// assert_eq!(a.iter().find(|&&x| x == 2), Some(&2));
2917    /// assert_eq!(a.iter().find(|&&x| x == 5), None);
2918    /// ```
2919    ///
2920    /// Stopping at the first `true`:
2921    ///
2922    /// ```
2923    /// let a = [1, 2, 3];
2924    ///
2925    /// let mut iter = a.into_iter();
2926    ///
2927    /// assert_eq!(iter.find(|&x| x == 2), Some(2));
2928    ///
2929    /// // we can still use `iter`, as there are more elements.
2930    /// assert_eq!(iter.next(), Some(3));
2931    /// ```
2932    ///
2933    /// Note that `iter.find(f)` is equivalent to `iter.filter(f).next()`.
2934    #[inline]
2935    #[stable(feature = "rust1", since = "1.0.0")]
2936    #[rustc_non_const_trait_method]
2937    fn find<P>(&mut self, predicate: P) -> Option<Self::Item>
2938    where
2939        Self: Sized,
2940        P: FnMut(&Self::Item) -> bool,
2941    {
2942        #[inline]
2943        fn check<T>(mut predicate: impl FnMut(&T) -> bool) -> impl FnMut((), T) -> ControlFlow<T> {
2944            move |(), x| {
2945                if predicate(&x) { ControlFlow::Break(x) } else { ControlFlow::Continue(()) }
2946            }
2947        }
2948
2949        self.try_fold((), check(predicate)).break_value()
2950    }
2951
2952    /// Applies function to the elements of iterator and returns
2953    /// the first non-none result.
2954    ///
2955    /// `iter.find_map(f)` is equivalent to `iter.filter_map(f).next()`.
2956    ///
2957    /// # Examples
2958    ///
2959    /// ```
2960    /// let a = ["lol", "NaN", "2", "5"];
2961    ///
2962    /// let first_number = a.iter().find_map(|s| s.parse().ok());
2963    ///
2964    /// assert_eq!(first_number, Some(2));
2965    /// ```
2966    #[inline]
2967    #[stable(feature = "iterator_find_map", since = "1.30.0")]
2968    #[rustc_non_const_trait_method]
2969    fn find_map<B, F>(&mut self, f: F) -> Option<B>
2970    where
2971        Self: Sized,
2972        F: FnMut(Self::Item) -> Option<B>,
2973    {
2974        #[inline]
2975        fn check<T, B>(mut f: impl FnMut(T) -> Option<B>) -> impl FnMut((), T) -> ControlFlow<B> {
2976            move |(), x| match f(x) {
2977                Some(x) => ControlFlow::Break(x),
2978                None => ControlFlow::Continue(()),
2979            }
2980        }
2981
2982        self.try_fold((), check(f)).break_value()
2983    }
2984
2985    /// Applies function to the elements of iterator and returns
2986    /// the first true result or the first error.
2987    ///
2988    /// The return type of this method depends on the return type of the closure.
2989    /// If you return `Result<bool, E>` from the closure, you'll get a `Result<Option<Self::Item>, E>`.
2990    /// If you return `Option<bool>` from the closure, you'll get an `Option<Option<Self::Item>>`.
2991    ///
2992    /// # Examples
2993    ///
2994    /// ```
2995    /// #![feature(try_find)]
2996    ///
2997    /// let a = ["1", "2", "lol", "NaN", "5"];
2998    ///
2999    /// let is_my_num = |s: &str, search: i32| -> Result<bool, std::num::ParseIntError> {
3000    ///     Ok(s.parse::<i32>()? == search)
3001    /// };
3002    ///
3003    /// let result = a.into_iter().try_find(|&s| is_my_num(s, 2));
3004    /// assert_eq!(result, Ok(Some("2")));
3005    ///
3006    /// let result = a.into_iter().try_find(|&s| is_my_num(s, 5));
3007    /// assert!(result.is_err());
3008    /// ```
3009    ///
3010    /// This also supports other types which implement [`Try`], not just [`Result`].
3011    ///
3012    /// ```
3013    /// #![feature(try_find)]
3014    ///
3015    /// use std::num::NonZero;
3016    ///
3017    /// let a = [3, 5, 7, 4, 9, 0, 11u32];
3018    /// let result = a.into_iter().try_find(|&x| NonZero::new(x).map(|y| y.is_power_of_two()));
3019    /// assert_eq!(result, Some(Some(4)));
3020    /// let result = a.into_iter().take(3).try_find(|&x| NonZero::new(x).map(|y| y.is_power_of_two()));
3021    /// assert_eq!(result, Some(None));
3022    /// let result = a.into_iter().rev().try_find(|&x| NonZero::new(x).map(|y| y.is_power_of_two()));
3023    /// assert_eq!(result, None);
3024    /// ```
3025    #[inline]
3026    #[unstable(feature = "try_find", issue = "63178")]
3027    #[rustc_non_const_trait_method]
3028    fn try_find<R>(
3029        &mut self,
3030        f: impl FnMut(&Self::Item) -> R,
3031    ) -> ChangeOutputType<R, Option<Self::Item>>
3032    where
3033        Self: Sized,
3034        R: Try<Output = bool, Residual: Residual<Option<Self::Item>>>,
3035    {
3036        #[inline]
3037        fn check<I, V, R>(
3038            mut f: impl FnMut(&I) -> V,
3039        ) -> impl FnMut((), I) -> ControlFlow<R::TryType>
3040        where
3041            V: Try<Output = bool, Residual = R>,
3042            R: Residual<Option<I>>,
3043        {
3044            move |(), x| match f(&x).branch() {
3045                ControlFlow::Continue(false) => ControlFlow::Continue(()),
3046                ControlFlow::Continue(true) => ControlFlow::Break(Try::from_output(Some(x))),
3047                ControlFlow::Break(r) => ControlFlow::Break(FromResidual::from_residual(r)),
3048            }
3049        }
3050
3051        match self.try_fold((), check(f)) {
3052            ControlFlow::Break(x) => x,
3053            ControlFlow::Continue(()) => Try::from_output(None),
3054        }
3055    }
3056
3057    /// Searches for an element in an iterator, returning its index.
3058    ///
3059    /// `position()` takes a closure that returns `true` or `false`. It applies
3060    /// this closure to each element of the iterator, and if one of them
3061    /// returns `true`, then `position()` returns [`Some(index)`]. If all of
3062    /// them return `false`, it returns [`None`].
3063    ///
3064    /// `position()` is short-circuiting; in other words, it will stop
3065    /// processing as soon as it finds a `true`.
3066    ///
3067    /// # Overflow Behavior
3068    ///
3069    /// The method does no guarding against overflows, so if there are more
3070    /// than [`usize::MAX`] non-matching elements, it either produces the wrong
3071    /// result or panics. If overflow checks are enabled, a panic is
3072    /// guaranteed.
3073    ///
3074    /// # Panics
3075    ///
3076    /// This function might panic if the iterator has more than `usize::MAX`
3077    /// non-matching elements.
3078    ///
3079    /// [`Some(index)`]: Some
3080    ///
3081    /// # Examples
3082    ///
3083    /// Basic usage:
3084    ///
3085    /// ```
3086    /// let a = [1, 2, 3];
3087    ///
3088    /// assert_eq!(a.into_iter().position(|x| x == 2), Some(1));
3089    ///
3090    /// assert_eq!(a.into_iter().position(|x| x == 5), None);
3091    /// ```
3092    ///
3093    /// Stopping at the first `true`:
3094    ///
3095    /// ```
3096    /// let a = [1, 2, 3, 4];
3097    ///
3098    /// let mut iter = a.into_iter();
3099    ///
3100    /// assert_eq!(iter.position(|x| x >= 2), Some(1));
3101    ///
3102    /// // we can still use `iter`, as there are more elements.
3103    /// assert_eq!(iter.next(), Some(3));
3104    ///
3105    /// // The returned index depends on iterator state
3106    /// assert_eq!(iter.position(|x| x == 4), Some(0));
3107    ///
3108    /// ```
3109    #[inline]
3110    #[stable(feature = "rust1", since = "1.0.0")]
3111    #[rustc_non_const_trait_method]
3112    fn position<P>(&mut self, predicate: P) -> Option<usize>
3113    where
3114        Self: Sized,
3115        P: FnMut(Self::Item) -> bool,
3116    {
3117        #[inline]
3118        fn check<'a, T>(
3119            mut predicate: impl FnMut(T) -> bool + 'a,
3120            acc: &'a mut usize,
3121        ) -> impl FnMut((), T) -> ControlFlow<usize, ()> + 'a {
3122            #[rustc_inherit_overflow_checks]
3123            move |_, x| {
3124                if predicate(x) {
3125                    ControlFlow::Break(*acc)
3126                } else {
3127                    *acc += 1;
3128                    ControlFlow::Continue(())
3129                }
3130            }
3131        }
3132
3133        let mut acc = 0;
3134        self.try_fold((), check(predicate, &mut acc)).break_value()
3135    }
3136
3137    /// Searches for an element in an iterator from the right, returning its
3138    /// index.
3139    ///
3140    /// `rposition()` takes a closure that returns `true` or `false`. It applies
3141    /// this closure to each element of the iterator, starting from the end,
3142    /// and if one of them returns `true`, then `rposition()` returns
3143    /// [`Some(index)`]. If all of them return `false`, it returns [`None`].
3144    ///
3145    /// `rposition()` is short-circuiting; in other words, it will stop
3146    /// processing as soon as it finds a `true`.
3147    ///
3148    /// [`Some(index)`]: Some
3149    ///
3150    /// # Examples
3151    ///
3152    /// Basic usage:
3153    ///
3154    /// ```
3155    /// let a = [1, 2, 3];
3156    ///
3157    /// assert_eq!(a.into_iter().rposition(|x| x == 3), Some(2));
3158    ///
3159    /// assert_eq!(a.into_iter().rposition(|x| x == 5), None);
3160    /// ```
3161    ///
3162    /// Stopping at the first `true`:
3163    ///
3164    /// ```
3165    /// let a = [-1, 2, 3, 4];
3166    ///
3167    /// let mut iter = a.into_iter();
3168    ///
3169    /// assert_eq!(iter.rposition(|x| x >= 2), Some(3));
3170    ///
3171    /// // we can still use `iter`, as there are more elements.
3172    /// assert_eq!(iter.next(), Some(-1));
3173    /// assert_eq!(iter.next_back(), Some(3));
3174    /// ```
3175    #[inline]
3176    #[stable(feature = "rust1", since = "1.0.0")]
3177    #[rustc_non_const_trait_method]
3178    fn rposition<P>(&mut self, predicate: P) -> Option<usize>
3179    where
3180        P: FnMut(Self::Item) -> bool,
3181        Self: Sized + ExactSizeIterator + DoubleEndedIterator,
3182    {
3183        // No need for an overflow check here, because `ExactSizeIterator`
3184        // implies that the number of elements fits into a `usize`.
3185        #[inline]
3186        fn check<T>(
3187            mut predicate: impl FnMut(T) -> bool,
3188        ) -> impl FnMut(usize, T) -> ControlFlow<usize, usize> {
3189            move |i, x| {
3190                let i = i - 1;
3191                if predicate(x) { ControlFlow::Break(i) } else { ControlFlow::Continue(i) }
3192            }
3193        }
3194
3195        let n = self.len();
3196        self.try_rfold(n, check(predicate)).break_value()
3197    }
3198
3199    /// Returns the maximum element of an iterator.
3200    ///
3201    /// If several elements are equally maximum, the last element is
3202    /// returned. If the iterator is empty, [`None`] is returned.
3203    ///
3204    /// Note that [`f32`]/[`f64`] doesn't implement [`Ord`] due to NaN being
3205    /// incomparable. You can work around this by using [`Iterator::reduce`]:
3206    /// ```
3207    /// assert_eq!(
3208    ///     [2.4, f32::NAN, 1.3]
3209    ///         .into_iter()
3210    ///         .reduce(f32::max)
3211    ///         .unwrap_or(0.),
3212    ///     2.4
3213    /// );
3214    /// ```
3215    ///
3216    /// # Examples
3217    ///
3218    /// ```
3219    /// let a = [1, 2, 3];
3220    /// let b: [u32; 0] = [];
3221    ///
3222    /// assert_eq!(a.into_iter().max(), Some(3));
3223    /// assert_eq!(b.into_iter().max(), None);
3224    /// ```
3225    #[inline]
3226    #[stable(feature = "rust1", since = "1.0.0")]
3227    #[rustc_non_const_trait_method]
3228    fn max(self) -> Option<Self::Item>
3229    where
3230        Self: Sized,
3231        Self::Item: Ord,
3232    {
3233        self.max_by(Ord::cmp)
3234    }
3235
3236    /// Returns the minimum element of an iterator.
3237    ///
3238    /// If several elements are equally minimum, the first element is returned.
3239    /// If the iterator is empty, [`None`] is returned.
3240    ///
3241    /// Note that [`f32`]/[`f64`] doesn't implement [`Ord`] due to NaN being
3242    /// incomparable. You can work around this by using [`Iterator::reduce`]:
3243    /// ```
3244    /// assert_eq!(
3245    ///     [2.4, f32::NAN, 1.3]
3246    ///         .into_iter()
3247    ///         .reduce(f32::min)
3248    ///         .unwrap_or(0.),
3249    ///     1.3
3250    /// );
3251    /// ```
3252    ///
3253    /// # Examples
3254    ///
3255    /// ```
3256    /// let a = [1, 2, 3];
3257    /// let b: [u32; 0] = [];
3258    ///
3259    /// assert_eq!(a.into_iter().min(), Some(1));
3260    /// assert_eq!(b.into_iter().min(), None);
3261    /// ```
3262    #[inline]
3263    #[stable(feature = "rust1", since = "1.0.0")]
3264    #[rustc_non_const_trait_method]
3265    fn min(self) -> Option<Self::Item>
3266    where
3267        Self: Sized,
3268        Self::Item: Ord,
3269    {
3270        self.min_by(Ord::cmp)
3271    }
3272
3273    /// Returns the element that gives the maximum value from the
3274    /// specified function.
3275    ///
3276    /// If several elements are equally maximum, the last element is
3277    /// returned. If the iterator is empty, [`None`] is returned.
3278    ///
3279    /// # Examples
3280    ///
3281    /// ```
3282    /// let a = [-3_i32, 0, 1, 5, -10];
3283    /// assert_eq!(a.into_iter().max_by_key(|x| x.abs()).unwrap(), -10);
3284    /// ```
3285    #[inline]
3286    #[stable(feature = "iter_cmp_by_key", since = "1.6.0")]
3287    #[rustc_non_const_trait_method]
3288    fn max_by_key<B: Ord, F>(self, f: F) -> Option<Self::Item>
3289    where
3290        Self: Sized,
3291        F: FnMut(&Self::Item) -> B,
3292    {
3293        #[inline]
3294        fn key<T, B>(mut f: impl FnMut(&T) -> B) -> impl FnMut(T) -> (B, T) {
3295            move |x| (f(&x), x)
3296        }
3297
3298        #[inline]
3299        fn compare<T, B: Ord>((x_p, _): &(B, T), (y_p, _): &(B, T)) -> Ordering {
3300            x_p.cmp(y_p)
3301        }
3302
3303        let (_, x) = self.map(key(f)).max_by(compare)?;
3304        Some(x)
3305    }
3306
3307    /// Returns the element that gives the maximum value with respect to the
3308    /// specified comparison function.
3309    ///
3310    /// If several elements are equally maximum, the last element is
3311    /// returned. If the iterator is empty, [`None`] is returned.
3312    ///
3313    /// # Examples
3314    ///
3315    /// ```
3316    /// let a = [-3_i32, 0, 1, 5, -10];
3317    /// assert_eq!(a.into_iter().max_by(|x, y| x.cmp(y)).unwrap(), 5);
3318    /// ```
3319    #[inline]
3320    #[stable(feature = "iter_max_by", since = "1.15.0")]
3321    #[rustc_non_const_trait_method]
3322    fn max_by<F>(self, compare: F) -> Option<Self::Item>
3323    where
3324        Self: Sized,
3325        F: FnMut(&Self::Item, &Self::Item) -> Ordering,
3326    {
3327        #[inline]
3328        fn fold<T>(mut compare: impl FnMut(&T, &T) -> Ordering) -> impl FnMut(T, T) -> T {
3329            move |x, y| cmp::max_by(x, y, &mut compare)
3330        }
3331
3332        self.reduce(fold(compare))
3333    }
3334
3335    /// Returns the element that gives the minimum value from the
3336    /// specified function.
3337    ///
3338    /// If several elements are equally minimum, the first element is
3339    /// returned. If the iterator is empty, [`None`] is returned.
3340    ///
3341    /// # Examples
3342    ///
3343    /// ```
3344    /// let a = [-3_i32, 0, 1, 5, -10];
3345    /// assert_eq!(a.into_iter().min_by_key(|x| x.abs()).unwrap(), 0);
3346    /// ```
3347    #[inline]
3348    #[stable(feature = "iter_cmp_by_key", since = "1.6.0")]
3349    #[rustc_non_const_trait_method]
3350    fn min_by_key<B: Ord, F>(self, f: F) -> Option<Self::Item>
3351    where
3352        Self: Sized,
3353        F: FnMut(&Self::Item) -> B,
3354    {
3355        #[inline]
3356        fn key<T, B>(mut f: impl FnMut(&T) -> B) -> impl FnMut(T) -> (B, T) {
3357            move |x| (f(&x), x)
3358        }
3359
3360        #[inline]
3361        fn compare<T, B: Ord>((x_p, _): &(B, T), (y_p, _): &(B, T)) -> Ordering {
3362            x_p.cmp(y_p)
3363        }
3364
3365        let (_, x) = self.map(key(f)).min_by(compare)?;
3366        Some(x)
3367    }
3368
3369    /// Returns the element that gives the minimum value with respect to the
3370    /// specified comparison function.
3371    ///
3372    /// If several elements are equally minimum, the first element is
3373    /// returned. If the iterator is empty, [`None`] is returned.
3374    ///
3375    /// # Examples
3376    ///
3377    /// ```
3378    /// let a = [-3_i32, 0, 1, 5, -10];
3379    /// assert_eq!(a.into_iter().min_by(|x, y| x.cmp(y)).unwrap(), -10);
3380    /// ```
3381    #[inline]
3382    #[stable(feature = "iter_min_by", since = "1.15.0")]
3383    #[rustc_non_const_trait_method]
3384    fn min_by<F>(self, compare: F) -> Option<Self::Item>
3385    where
3386        Self: Sized,
3387        F: FnMut(&Self::Item, &Self::Item) -> Ordering,
3388    {
3389        #[inline]
3390        fn fold<T>(mut compare: impl FnMut(&T, &T) -> Ordering) -> impl FnMut(T, T) -> T {
3391            move |x, y| cmp::min_by(x, y, &mut compare)
3392        }
3393
3394        self.reduce(fold(compare))
3395    }
3396
3397    /// Reverses an iterator's direction.
3398    ///
3399    /// Usually, iterators iterate from left to right. After using `rev()`,
3400    /// an iterator will instead iterate from right to left.
3401    ///
3402    /// This is only possible if the iterator has an end, so `rev()` only
3403    /// works on [`DoubleEndedIterator`]s.
3404    ///
3405    /// # Examples
3406    ///
3407    /// ```
3408    /// let a = [1, 2, 3];
3409    ///
3410    /// let mut iter = a.into_iter().rev();
3411    ///
3412    /// assert_eq!(iter.next(), Some(3));
3413    /// assert_eq!(iter.next(), Some(2));
3414    /// assert_eq!(iter.next(), Some(1));
3415    ///
3416    /// assert_eq!(iter.next(), None);
3417    /// ```
3418    #[inline]
3419    #[doc(alias = "reverse")]
3420    #[stable(feature = "rust1", since = "1.0.0")]
3421    #[rustc_non_const_trait_method]
3422    fn rev(self) -> Rev<Self>
3423    where
3424        Self: Sized + DoubleEndedIterator,
3425    {
3426        Rev::new(self)
3427    }
3428
3429    /// Converts an iterator of pairs into a pair of containers.
3430    ///
3431    /// `unzip()` consumes an entire iterator of pairs, producing two
3432    /// collections: one from the left elements of the pairs, and one
3433    /// from the right elements.
3434    ///
3435    /// This function is, in some sense, the opposite of [`zip`].
3436    ///
3437    /// [`zip`]: Iterator::zip
3438    ///
3439    /// # Examples
3440    ///
3441    /// ```
3442    /// let a = [(1, 2), (3, 4), (5, 6)];
3443    ///
3444    /// let (left, right): (Vec<_>, Vec<_>) = a.into_iter().unzip();
3445    ///
3446    /// assert_eq!(left, [1, 3, 5]);
3447    /// assert_eq!(right, [2, 4, 6]);
3448    ///
3449    /// // you can also unzip multiple nested tuples at once
3450    /// let a = [(1, (2, 3)), (4, (5, 6))];
3451    ///
3452    /// let (x, (y, z)): (Vec<_>, (Vec<_>, Vec<_>)) = a.into_iter().unzip();
3453    /// assert_eq!(x, [1, 4]);
3454    /// assert_eq!(y, [2, 5]);
3455    /// assert_eq!(z, [3, 6]);
3456    /// ```
3457    #[stable(feature = "rust1", since = "1.0.0")]
3458    #[rustc_non_const_trait_method]
3459    fn unzip<A, B, FromA, FromB>(self) -> (FromA, FromB)
3460    where
3461        FromA: Default + Extend<A>,
3462        FromB: Default + Extend<B>,
3463        Self: Sized + Iterator<Item = (A, B)>,
3464    {
3465        let mut unzipped: (FromA, FromB) = Default::default();
3466        unzipped.extend(self);
3467        unzipped
3468    }
3469
3470    /// Creates an iterator which copies all of its elements.
3471    ///
3472    /// This is useful when you have an iterator over `&T`, but you need an
3473    /// iterator over `T`.
3474    ///
3475    /// # Examples
3476    ///
3477    /// ```
3478    /// let a = [1, 2, 3];
3479    ///
3480    /// let v_copied: Vec<_> = a.iter().copied().collect();
3481    ///
3482    /// // copied is the same as .map(|&x| x)
3483    /// let v_map: Vec<_> = a.iter().map(|&x| x).collect();
3484    ///
3485    /// assert_eq!(v_copied, [1, 2, 3]);
3486    /// assert_eq!(v_map, [1, 2, 3]);
3487    /// ```
3488    #[stable(feature = "iter_copied", since = "1.36.0")]
3489    #[rustc_diagnostic_item = "iter_copied"]
3490    #[rustc_non_const_trait_method]
3491    fn copied<'a, T>(self) -> Copied<Self>
3492    where
3493        T: Copy + 'a,
3494        Self: Sized + Iterator<Item = &'a T>,
3495    {
3496        Copied::new(self)
3497    }
3498
3499    /// Creates an iterator which [`clone`]s all of its elements.
3500    ///
3501    /// This is useful when you have an iterator over `&T`, but you need an
3502    /// iterator over `T`.
3503    ///
3504    /// There is no guarantee whatsoever about the `clone` method actually
3505    /// being called *or* optimized away. So code should not depend on
3506    /// either.
3507    ///
3508    /// [`clone`]: Clone::clone
3509    ///
3510    /// # Examples
3511    ///
3512    /// Basic usage:
3513    ///
3514    /// ```
3515    /// let a = [1, 2, 3];
3516    ///
3517    /// let v_cloned: Vec<_> = a.iter().cloned().collect();
3518    ///
3519    /// // cloned is the same as .map(|&x| x), for integers
3520    /// let v_map: Vec<_> = a.iter().map(|&x| x).collect();
3521    ///
3522    /// assert_eq!(v_cloned, [1, 2, 3]);
3523    /// assert_eq!(v_map, [1, 2, 3]);
3524    /// ```
3525    ///
3526    /// To get the best performance, try to clone late:
3527    ///
3528    /// ```
3529    /// let a = [vec![0_u8, 1, 2], vec![3, 4], vec![23]];
3530    /// // don't do this:
3531    /// let slower: Vec<_> = a.iter().cloned().filter(|s| s.len() == 1).collect();
3532    /// assert_eq!(&[vec![23]], &slower[..]);
3533    /// // instead call `cloned` late
3534    /// let faster: Vec<_> = a.iter().filter(|s| s.len() == 1).cloned().collect();
3535    /// assert_eq!(&[vec![23]], &faster[..]);
3536    /// ```
3537    #[stable(feature = "rust1", since = "1.0.0")]
3538    #[rustc_diagnostic_item = "iter_cloned"]
3539    #[rustc_non_const_trait_method]
3540    fn cloned<'a, T>(self) -> Cloned<Self>
3541    where
3542        T: Clone + 'a,
3543        Self: Sized + Iterator<Item = &'a T>,
3544    {
3545        Cloned::new(self)
3546    }
3547
3548    /// Repeats an iterator endlessly.
3549    ///
3550    /// Instead of stopping at [`None`], the iterator will instead start again,
3551    /// from the beginning. After iterating again, it will start at the
3552    /// beginning again. And again. And again. Forever. Note that in case the
3553    /// original iterator is empty, the resulting iterator will also be empty.
3554    ///
3555    /// # Examples
3556    ///
3557    /// ```
3558    /// let a = [1, 2, 3];
3559    ///
3560    /// let mut iter = a.into_iter().cycle();
3561    ///
3562    /// loop {
3563    ///     assert_eq!(iter.next(), Some(1));
3564    ///     assert_eq!(iter.next(), Some(2));
3565    ///     assert_eq!(iter.next(), Some(3));
3566    /// #   break;
3567    /// }
3568    /// ```
3569    #[stable(feature = "rust1", since = "1.0.0")]
3570    #[inline]
3571    #[rustc_non_const_trait_method]
3572    fn cycle(self) -> Cycle<Self>
3573    where
3574        Self: Sized + Clone,
3575    {
3576        Cycle::new(self)
3577    }
3578
3579    /// Returns an iterator over `N` elements of the iterator at a time.
3580    ///
3581    /// The chunks do not overlap. If `N` does not divide the length of the
3582    /// iterator, then the last up to `N-1` elements will be omitted and can be
3583    /// retrieved from the [`.into_remainder()`][ArrayChunks::into_remainder]
3584    /// function of the iterator.
3585    ///
3586    /// # Panics
3587    ///
3588    /// Panics if `N` is zero.
3589    ///
3590    /// # Examples
3591    ///
3592    /// Basic usage:
3593    ///
3594    /// ```
3595    /// #![feature(iter_array_chunks)]
3596    ///
3597    /// let mut iter = "lorem".chars().array_chunks();
3598    /// assert_eq!(iter.next(), Some(['l', 'o']));
3599    /// assert_eq!(iter.next(), Some(['r', 'e']));
3600    /// assert_eq!(iter.next(), None);
3601    /// assert_eq!(iter.into_remainder().as_slice(), &['m']);
3602    /// ```
3603    ///
3604    /// ```
3605    /// #![feature(iter_array_chunks)]
3606    ///
3607    /// let data = [1, 1, 2, -2, 6, 0, 3, 1];
3608    /// //          ^-----^  ^------^
3609    /// for [x, y, z] in data.iter().array_chunks() {
3610    ///     assert_eq!(x + y + z, 4);
3611    /// }
3612    /// ```
3613    #[track_caller]
3614    #[unstable(feature = "iter_array_chunks", issue = "100450")]
3615    #[rustc_non_const_trait_method]
3616    fn array_chunks<const N: usize>(self) -> ArrayChunks<Self, N>
3617    where
3618        Self: Sized,
3619    {
3620        ArrayChunks::new(self)
3621    }
3622
3623    /// Sums the elements of an iterator.
3624    ///
3625    /// Takes each element, adds them together, and returns the result.
3626    ///
3627    /// An empty iterator returns the *additive identity* ("zero") of the type,
3628    /// which is `0` for integers and `-0.0` for floats.
3629    ///
3630    /// `sum()` can be used to sum any type implementing [`Sum`][`core::iter::Sum`],
3631    /// including [`Option`][`Option::sum`] and [`Result`][`Result::sum`].
3632    ///
3633    /// # Panics
3634    ///
3635    /// When calling `sum()` and a primitive integer type is being returned, this
3636    /// method will panic if the computation overflows and overflow checks are
3637    /// enabled.
3638    ///
3639    /// # Examples
3640    ///
3641    /// ```
3642    /// let a = [1, 2, 3];
3643    /// let sum: i32 = a.iter().sum();
3644    ///
3645    /// assert_eq!(sum, 6);
3646    ///
3647    /// let b: Vec<f32> = vec![];
3648    /// let sum: f32 = b.iter().sum();
3649    /// assert_eq!(sum, -0.0_f32);
3650    /// ```
3651    #[stable(feature = "iter_arith", since = "1.11.0")]
3652    #[rustc_non_const_trait_method]
3653    fn sum<S>(self) -> S
3654    where
3655        Self: Sized,
3656        S: Sum<Self::Item>,
3657    {
3658        Sum::sum(self)
3659    }
3660
3661    /// Iterates over the entire iterator, multiplying all the elements
3662    ///
3663    /// An empty iterator returns the one value of the type.
3664    ///
3665    /// `product()` can be used to multiply any type implementing [`Product`][`core::iter::Product`],
3666    /// including [`Option`][`Option::product`] and [`Result`][`Result::product`].
3667    ///
3668    /// # Panics
3669    ///
3670    /// When calling `product()` and a primitive integer type is being returned,
3671    /// method will panic if the computation overflows and overflow checks are
3672    /// enabled.
3673    ///
3674    /// # Examples
3675    ///
3676    /// ```
3677    /// fn factorial(n: u32) -> u32 {
3678    ///     (1..=n).product()
3679    /// }
3680    /// assert_eq!(factorial(0), 1);
3681    /// assert_eq!(factorial(1), 1);
3682    /// assert_eq!(factorial(5), 120);
3683    /// ```
3684    #[stable(feature = "iter_arith", since = "1.11.0")]
3685    #[rustc_non_const_trait_method]
3686    fn product<P>(self) -> P
3687    where
3688        Self: Sized,
3689        P: Product<Self::Item>,
3690    {
3691        Product::product(self)
3692    }
3693
3694    /// [Lexicographically](Ord#lexicographical-comparison) compares the elements of this [`Iterator`] with those
3695    /// of another.
3696    ///
3697    /// # Examples
3698    ///
3699    /// ```
3700    /// use std::cmp::Ordering;
3701    ///
3702    /// assert_eq!([1].iter().cmp([1].iter()), Ordering::Equal);
3703    /// assert_eq!([1].iter().cmp([1, 2].iter()), Ordering::Less);
3704    /// assert_eq!([1, 2].iter().cmp([1].iter()), Ordering::Greater);
3705    /// ```
3706    #[stable(feature = "iter_order", since = "1.5.0")]
3707    #[rustc_non_const_trait_method]
3708    fn cmp<I>(self, other: I) -> Ordering
3709    where
3710        I: IntoIterator<Item = Self::Item>,
3711        Self::Item: Ord,
3712        Self: Sized,
3713    {
3714        self.cmp_by(other, |x, y| x.cmp(&y))
3715    }
3716
3717    /// [Lexicographically](Ord#lexicographical-comparison) compares the elements of this [`Iterator`] with those
3718    /// of another with respect to the specified comparison function.
3719    ///
3720    /// # Examples
3721    ///
3722    /// ```
3723    /// #![feature(iter_order_by)]
3724    ///
3725    /// use std::cmp::Ordering;
3726    ///
3727    /// let xs = [1, 2, 3, 4];
3728    /// let ys = [1, 4, 9, 16];
3729    ///
3730    /// assert_eq!(xs.into_iter().cmp_by(ys, |x, y| x.cmp(&y)), Ordering::Less);
3731    /// assert_eq!(xs.into_iter().cmp_by(ys, |x, y| (x * x).cmp(&y)), Ordering::Equal);
3732    /// assert_eq!(xs.into_iter().cmp_by(ys, |x, y| (2 * x).cmp(&y)), Ordering::Greater);
3733    /// ```
3734    #[unstable(feature = "iter_order_by", issue = "64295")]
3735    #[rustc_non_const_trait_method]
3736    fn cmp_by<I, F>(self, other: I, cmp: F) -> Ordering
3737    where
3738        Self: Sized,
3739        I: IntoIterator,
3740        F: FnMut(Self::Item, I::Item) -> Ordering,
3741    {
3742        #[inline]
3743        fn compare<X, Y, F>(mut cmp: F) -> impl FnMut(X, Y) -> ControlFlow<Ordering>
3744        where
3745            F: FnMut(X, Y) -> Ordering,
3746        {
3747            move |x, y| match cmp(x, y) {
3748                Ordering::Equal => ControlFlow::Continue(()),
3749                non_eq => ControlFlow::Break(non_eq),
3750            }
3751        }
3752
3753        match iter_compare(self, other.into_iter(), compare(cmp)) {
3754            ControlFlow::Continue(ord) => ord,
3755            ControlFlow::Break(ord) => ord,
3756        }
3757    }
3758
3759    /// [Lexicographically](Ord#lexicographical-comparison) compares the [`PartialOrd`] elements of
3760    /// this [`Iterator`] with those of another. The comparison works like short-circuit
3761    /// evaluation, returning a result without comparing the remaining elements.
3762    /// As soon as an order can be determined, the evaluation stops and a result is returned.
3763    ///
3764    /// # Examples
3765    ///
3766    /// ```
3767    /// use std::cmp::Ordering;
3768    ///
3769    /// assert_eq!([1.].iter().partial_cmp([1.].iter()), Some(Ordering::Equal));
3770    /// assert_eq!([1.].iter().partial_cmp([1., 2.].iter()), Some(Ordering::Less));
3771    /// assert_eq!([1., 2.].iter().partial_cmp([1.].iter()), Some(Ordering::Greater));
3772    /// ```
3773    ///
3774    /// For floating-point numbers, NaN does not have a total order and will result
3775    /// in `None` when compared:
3776    ///
3777    /// ```
3778    /// assert_eq!([f64::NAN].iter().partial_cmp([1.].iter()), None);
3779    /// ```
3780    ///
3781    /// The results are determined by the order of evaluation.
3782    ///
3783    /// ```
3784    /// use std::cmp::Ordering;
3785    ///
3786    /// assert_eq!([1.0, f64::NAN].iter().partial_cmp([2.0, f64::NAN].iter()), Some(Ordering::Less));
3787    /// assert_eq!([2.0, f64::NAN].iter().partial_cmp([1.0, f64::NAN].iter()), Some(Ordering::Greater));
3788    /// assert_eq!([f64::NAN, 1.0].iter().partial_cmp([f64::NAN, 2.0].iter()), None);
3789    /// ```
3790    ///
3791    #[stable(feature = "iter_order", since = "1.5.0")]
3792    #[rustc_non_const_trait_method]
3793    fn partial_cmp<I>(self, other: I) -> Option<Ordering>
3794    where
3795        I: IntoIterator,
3796        Self::Item: PartialOrd<I::Item>,
3797        Self: Sized,
3798    {
3799        self.partial_cmp_by(other, |x, y| x.partial_cmp(&y))
3800    }
3801
3802    /// [Lexicographically](Ord#lexicographical-comparison) compares the elements of this [`Iterator`] with those
3803    /// of another with respect to the specified comparison function.
3804    ///
3805    /// # Examples
3806    ///
3807    /// ```
3808    /// #![feature(iter_order_by)]
3809    ///
3810    /// use std::cmp::Ordering;
3811    ///
3812    /// let xs = [1.0, 2.0, 3.0, 4.0];
3813    /// let ys = [1.0, 4.0, 9.0, 16.0];
3814    ///
3815    /// assert_eq!(
3816    ///     xs.iter().partial_cmp_by(ys, |x, y| x.partial_cmp(&y)),
3817    ///     Some(Ordering::Less)
3818    /// );
3819    /// assert_eq!(
3820    ///     xs.iter().partial_cmp_by(ys, |x, y| (x * x).partial_cmp(&y)),
3821    ///     Some(Ordering::Equal)
3822    /// );
3823    /// assert_eq!(
3824    ///     xs.iter().partial_cmp_by(ys, |x, y| (2.0 * x).partial_cmp(&y)),
3825    ///     Some(Ordering::Greater)
3826    /// );
3827    /// ```
3828    #[unstable(feature = "iter_order_by", issue = "64295")]
3829    #[rustc_non_const_trait_method]
3830    fn partial_cmp_by<I, F>(self, other: I, partial_cmp: F) -> Option<Ordering>
3831    where
3832        Self: Sized,
3833        I: IntoIterator,
3834        F: FnMut(Self::Item, I::Item) -> Option<Ordering>,
3835    {
3836        #[inline]
3837        fn compare<X, Y, F>(mut partial_cmp: F) -> impl FnMut(X, Y) -> ControlFlow<Option<Ordering>>
3838        where
3839            F: FnMut(X, Y) -> Option<Ordering>,
3840        {
3841            move |x, y| match partial_cmp(x, y) {
3842                Some(Ordering::Equal) => ControlFlow::Continue(()),
3843                non_eq => ControlFlow::Break(non_eq),
3844            }
3845        }
3846
3847        match iter_compare(self, other.into_iter(), compare(partial_cmp)) {
3848            ControlFlow::Continue(ord) => Some(ord),
3849            ControlFlow::Break(ord) => ord,
3850        }
3851    }
3852
3853    /// Determines if the elements of this [`Iterator`] are equal to those of
3854    /// another.
3855    ///
3856    /// # Examples
3857    ///
3858    /// ```
3859    /// assert_eq!([1].iter().eq([1].iter()), true);
3860    /// assert_eq!([1].iter().eq([1, 2].iter()), false);
3861    /// ```
3862    #[stable(feature = "iter_order", since = "1.5.0")]
3863    #[rustc_non_const_trait_method]
3864    fn eq<I>(self, other: I) -> bool
3865    where
3866        I: IntoIterator,
3867        Self::Item: PartialEq<I::Item>,
3868        Self: Sized,
3869    {
3870        self.eq_by(other, |x, y| x == y)
3871    }
3872
3873    /// Determines if the elements of this [`Iterator`] are equal to those of
3874    /// another with respect to the specified equality function.
3875    ///
3876    /// # Examples
3877    ///
3878    /// ```
3879    /// #![feature(iter_order_by)]
3880    ///
3881    /// let xs = [1, 2, 3, 4];
3882    /// let ys = [1, 4, 9, 16];
3883    ///
3884    /// assert!(xs.iter().eq_by(ys, |x, y| x * x == y));
3885    /// ```
3886    #[unstable(feature = "iter_order_by", issue = "64295")]
3887    #[rustc_non_const_trait_method]
3888    fn eq_by<I, F>(self, other: I, eq: F) -> bool
3889    where
3890        Self: Sized,
3891        I: IntoIterator,
3892        F: FnMut(Self::Item, I::Item) -> bool,
3893    {
3894        #[inline]
3895        fn compare<X, Y, F>(mut eq: F) -> impl FnMut(X, Y) -> ControlFlow<()>
3896        where
3897            F: FnMut(X, Y) -> bool,
3898        {
3899            move |x, y| {
3900                if eq(x, y) { ControlFlow::Continue(()) } else { ControlFlow::Break(()) }
3901            }
3902        }
3903
3904        SpecIterEq::spec_iter_eq(self, other.into_iter(), compare(eq))
3905    }
3906
3907    /// Determines if the elements of this [`Iterator`] are not equal to those of
3908    /// another.
3909    ///
3910    /// # Examples
3911    ///
3912    /// ```
3913    /// assert_eq!([1].iter().ne([1].iter()), false);
3914    /// assert_eq!([1].iter().ne([1, 2].iter()), true);
3915    /// ```
3916    #[stable(feature = "iter_order", since = "1.5.0")]
3917    #[rustc_non_const_trait_method]
3918    fn ne<I>(self, other: I) -> bool
3919    where
3920        I: IntoIterator,
3921        Self::Item: PartialEq<I::Item>,
3922        Self: Sized,
3923    {
3924        !self.eq(other)
3925    }
3926
3927    /// Determines if the elements of this [`Iterator`] are [lexicographically](Ord#lexicographical-comparison)
3928    /// less than those of another.
3929    ///
3930    /// # Examples
3931    ///
3932    /// ```
3933    /// assert_eq!([1].iter().lt([1].iter()), false);
3934    /// assert_eq!([1].iter().lt([1, 2].iter()), true);
3935    /// assert_eq!([1, 2].iter().lt([1].iter()), false);
3936    /// assert_eq!([1, 2].iter().lt([1, 2].iter()), false);
3937    /// ```
3938    #[stable(feature = "iter_order", since = "1.5.0")]
3939    #[rustc_non_const_trait_method]
3940    fn lt<I>(self, other: I) -> bool
3941    where
3942        I: IntoIterator,
3943        Self::Item: PartialOrd<I::Item>,
3944        Self: Sized,
3945    {
3946        self.partial_cmp(other) == Some(Ordering::Less)
3947    }
3948
3949    /// Determines if the elements of this [`Iterator`] are [lexicographically](Ord#lexicographical-comparison)
3950    /// less or equal to those of another.
3951    ///
3952    /// # Examples
3953    ///
3954    /// ```
3955    /// assert_eq!([1].iter().le([1].iter()), true);
3956    /// assert_eq!([1].iter().le([1, 2].iter()), true);
3957    /// assert_eq!([1, 2].iter().le([1].iter()), false);
3958    /// assert_eq!([1, 2].iter().le([1, 2].iter()), true);
3959    /// ```
3960    #[stable(feature = "iter_order", since = "1.5.0")]
3961    #[rustc_non_const_trait_method]
3962    fn le<I>(self, other: I) -> bool
3963    where
3964        I: IntoIterator,
3965        Self::Item: PartialOrd<I::Item>,
3966        Self: Sized,
3967    {
3968        matches!(self.partial_cmp(other), Some(Ordering::Less | Ordering::Equal))
3969    }
3970
3971    /// Determines if the elements of this [`Iterator`] are [lexicographically](Ord#lexicographical-comparison)
3972    /// greater than those of another.
3973    ///
3974    /// # Examples
3975    ///
3976    /// ```
3977    /// assert_eq!([1].iter().gt([1].iter()), false);
3978    /// assert_eq!([1].iter().gt([1, 2].iter()), false);
3979    /// assert_eq!([1, 2].iter().gt([1].iter()), true);
3980    /// assert_eq!([1, 2].iter().gt([1, 2].iter()), false);
3981    /// ```
3982    #[stable(feature = "iter_order", since = "1.5.0")]
3983    #[rustc_non_const_trait_method]
3984    fn gt<I>(self, other: I) -> bool
3985    where
3986        I: IntoIterator,
3987        Self::Item: PartialOrd<I::Item>,
3988        Self: Sized,
3989    {
3990        self.partial_cmp(other) == Some(Ordering::Greater)
3991    }
3992
3993    /// Determines if the elements of this [`Iterator`] are [lexicographically](Ord#lexicographical-comparison)
3994    /// greater than or equal to those of another.
3995    ///
3996    /// # Examples
3997    ///
3998    /// ```
3999    /// assert_eq!([1].iter().ge([1].iter()), true);
4000    /// assert_eq!([1].iter().ge([1, 2].iter()), false);
4001    /// assert_eq!([1, 2].iter().ge([1].iter()), true);
4002    /// assert_eq!([1, 2].iter().ge([1, 2].iter()), true);
4003    /// ```
4004    #[stable(feature = "iter_order", since = "1.5.0")]
4005    #[rustc_non_const_trait_method]
4006    fn ge<I>(self, other: I) -> bool
4007    where
4008        I: IntoIterator,
4009        Self::Item: PartialOrd<I::Item>,
4010        Self: Sized,
4011    {
4012        matches!(self.partial_cmp(other), Some(Ordering::Greater | Ordering::Equal))
4013    }
4014
4015    /// Checks if the elements of this iterator are sorted.
4016    ///
4017    /// That is, for each element `a` and its following element `b`, `a <= b` must hold. If the
4018    /// iterator yields exactly zero or one element, `true` is returned.
4019    ///
4020    /// Note that if `Self::Item` is only `PartialOrd`, but not `Ord`, the above definition
4021    /// implies that this function returns `false` if any two consecutive items are not
4022    /// comparable.
4023    ///
4024    /// # Examples
4025    ///
4026    /// ```
4027    /// assert!([1, 2, 2, 9].iter().is_sorted());
4028    /// assert!(![1, 3, 2, 4].iter().is_sorted());
4029    /// assert!([0].iter().is_sorted());
4030    /// assert!(std::iter::empty::<i32>().is_sorted());
4031    /// assert!(![0.0, 1.0, f32::NAN].iter().is_sorted());
4032    /// ```
4033    #[inline]
4034    #[stable(feature = "is_sorted", since = "1.82.0")]
4035    #[rustc_non_const_trait_method]
4036    fn is_sorted(self) -> bool
4037    where
4038        Self: Sized,
4039        Self::Item: PartialOrd,
4040    {
4041        self.is_sorted_by(|a, b| a <= b)
4042    }
4043
4044    /// Checks if the elements of this iterator are sorted using the given comparator function.
4045    ///
4046    /// Instead of using `PartialOrd::partial_cmp`, this function uses the given `compare`
4047    /// function to determine whether two elements are to be considered in sorted order.
4048    ///
4049    /// # Examples
4050    ///
4051    /// ```
4052    /// assert!([1, 2, 2, 9].iter().is_sorted_by(|a, b| a <= b));
4053    /// assert!(![1, 2, 2, 9].iter().is_sorted_by(|a, b| a < b));
4054    ///
4055    /// assert!([0].iter().is_sorted_by(|a, b| true));
4056    /// assert!([0].iter().is_sorted_by(|a, b| false));
4057    ///
4058    /// assert!(std::iter::empty::<i32>().is_sorted_by(|a, b| false));
4059    /// assert!(std::iter::empty::<i32>().is_sorted_by(|a, b| true));
4060    /// ```
4061    #[stable(feature = "is_sorted", since = "1.82.0")]
4062    #[rustc_non_const_trait_method]
4063    fn is_sorted_by<F>(mut self, compare: F) -> bool
4064    where
4065        Self: Sized,
4066        F: FnMut(&Self::Item, &Self::Item) -> bool,
4067    {
4068        #[inline]
4069        fn check<'a, T>(
4070            last: &'a mut T,
4071            mut compare: impl FnMut(&T, &T) -> bool + 'a,
4072        ) -> impl FnMut(T) -> bool + 'a {
4073            move |curr| {
4074                if !compare(&last, &curr) {
4075                    return false;
4076                }
4077                *last = curr;
4078                true
4079            }
4080        }
4081
4082        let mut last = match self.next() {
4083            Some(e) => e,
4084            None => return true,
4085        };
4086
4087        self.all(check(&mut last, compare))
4088    }
4089
4090    /// Checks if the elements of this iterator are sorted using the given key extraction
4091    /// function.
4092    ///
4093    /// Instead of comparing the iterator's elements directly, this function compares the keys of
4094    /// the elements, as determined by `f`. Apart from that, it's equivalent to [`is_sorted`]; see
4095    /// its documentation for more information.
4096    ///
4097    /// [`is_sorted`]: Iterator::is_sorted
4098    ///
4099    /// # Examples
4100    ///
4101    /// ```
4102    /// assert!(["c", "bb", "aaa"].iter().is_sorted_by_key(|s| s.len()));
4103    /// assert!(![-2i32, -1, 0, 3].iter().is_sorted_by_key(|n| n.abs()));
4104    /// ```
4105    #[inline]
4106    #[stable(feature = "is_sorted", since = "1.82.0")]
4107    #[rustc_non_const_trait_method]
4108    fn is_sorted_by_key<F, K>(self, f: F) -> bool
4109    where
4110        Self: Sized,
4111        F: FnMut(Self::Item) -> K,
4112        K: PartialOrd,
4113    {
4114        self.map(f).is_sorted()
4115    }
4116
4117    /// See [TrustedRandomAccess][super::super::TrustedRandomAccess]
4118    // The unusual name is to avoid name collisions in method resolution
4119    // see #76479.
4120    #[inline]
4121    #[doc(hidden)]
4122    #[unstable(feature = "trusted_random_access", issue = "none")]
4123    #[rustc_non_const_trait_method]
4124    unsafe fn __iterator_get_unchecked(&mut self, _idx: usize) -> Self::Item
4125    where
4126        Self: TrustedRandomAccessNoCoerce,
4127    {
4128        unreachable!("Always specialized");
4129    }
4130}
4131
4132trait SpecIterEq<B: Iterator>: Iterator {
4133    fn spec_iter_eq<F>(self, b: B, f: F) -> bool
4134    where
4135        F: FnMut(Self::Item, <B as Iterator>::Item) -> ControlFlow<()>;
4136}
4137
4138impl<A: Iterator, B: Iterator> SpecIterEq<B> for A {
4139    #[inline]
4140    default fn spec_iter_eq<F>(self, b: B, f: F) -> bool
4141    where
4142        F: FnMut(Self::Item, <B as Iterator>::Item) -> ControlFlow<()>,
4143    {
4144        iter_eq(self, b, f)
4145    }
4146}
4147
4148impl<A: Iterator + TrustedLen, B: Iterator + TrustedLen> SpecIterEq<B> for A {
4149    #[inline]
4150    fn spec_iter_eq<F>(self, b: B, f: F) -> bool
4151    where
4152        F: FnMut(Self::Item, <B as Iterator>::Item) -> ControlFlow<()>,
4153    {
4154        // we *can't* short-circuit if:
4155        match (self.size_hint(), b.size_hint()) {
4156            // ... both iterators have the same length
4157            ((_, Some(a)), (_, Some(b))) if a == b => {}
4158            // ... or both of them are longer than `usize::MAX` (i.e. have an unknown length).
4159            ((_, None), (_, None)) => {}
4160            // otherwise, we can ascertain that they are unequal without actually comparing items
4161            _ => return false,
4162        }
4163
4164        iter_eq(self, b, f)
4165    }
4166}
4167
4168/// Compares two iterators element-wise using the given function.
4169///
4170/// If `ControlFlow::Continue(())` is returned from the function, the comparison moves on to the next
4171/// elements of both iterators. Returning `ControlFlow::Break(x)` short-circuits the iteration and
4172/// returns `ControlFlow::Break(x)`. If one of the iterators runs out of elements,
4173/// `ControlFlow::Continue(ord)` is returned where `ord` is the result of comparing the lengths of
4174/// the iterators.
4175///
4176/// Isolates the logic shared by ['cmp_by'](Iterator::cmp_by),
4177/// ['partial_cmp_by'](Iterator::partial_cmp_by), and ['eq_by'](Iterator::eq_by).
4178#[inline]
4179fn iter_compare<A, B, F, T>(mut a: A, mut b: B, f: F) -> ControlFlow<T, Ordering>
4180where
4181    A: Iterator,
4182    B: Iterator,
4183    F: FnMut(A::Item, B::Item) -> ControlFlow<T>,
4184{
4185    #[inline]
4186    fn compare<'a, B, X, T>(
4187        b: &'a mut B,
4188        mut f: impl FnMut(X, B::Item) -> ControlFlow<T> + 'a,
4189    ) -> impl FnMut(X) -> ControlFlow<ControlFlow<T, Ordering>> + 'a
4190    where
4191        B: Iterator,
4192    {
4193        move |x| match b.next() {
4194            None => ControlFlow::Break(ControlFlow::Continue(Ordering::Greater)),
4195            Some(y) => f(x, y).map_break(ControlFlow::Break),
4196        }
4197    }
4198
4199    match a.try_for_each(compare(&mut b, f)) {
4200        ControlFlow::Continue(()) => ControlFlow::Continue(match b.next() {
4201            None => Ordering::Equal,
4202            Some(_) => Ordering::Less,
4203        }),
4204        ControlFlow::Break(x) => x,
4205    }
4206}
4207
4208#[inline]
4209fn iter_eq<A, B, F>(a: A, b: B, f: F) -> bool
4210where
4211    A: Iterator,
4212    B: Iterator,
4213    F: FnMut(A::Item, B::Item) -> ControlFlow<()>,
4214{
4215    iter_compare(a, b, f).continue_value().is_some_and(|ord| ord == Ordering::Equal)
4216}
4217
4218/// Implements `Iterator` for mutable references to iterators, such as those produced by [`Iterator::by_ref`].
4219///
4220/// This implementation passes all method calls on to the original iterator.
4221#[stable(feature = "rust1", since = "1.0.0")]
4222impl<I: Iterator + ?Sized> Iterator for &mut I {
4223    type Item = I::Item;
4224    #[inline]
4225    fn next(&mut self) -> Option<I::Item> {
4226        (**self).next()
4227    }
4228    fn size_hint(&self) -> (usize, Option<usize>) {
4229        (**self).size_hint()
4230    }
4231    fn advance_by(&mut self, n: usize) -> Result<(), NonZero<usize>> {
4232        (**self).advance_by(n)
4233    }
4234    fn nth(&mut self, n: usize) -> Option<Self::Item> {
4235        (**self).nth(n)
4236    }
4237    fn fold<B, F>(self, init: B, f: F) -> B
4238    where
4239        F: FnMut(B, Self::Item) -> B,
4240    {
4241        self.spec_fold(init, f)
4242    }
4243    fn try_fold<B, F, R>(&mut self, init: B, f: F) -> R
4244    where
4245        F: FnMut(B, Self::Item) -> R,
4246        R: Try<Output = B>,
4247    {
4248        self.spec_try_fold(init, f)
4249    }
4250}
4251
4252/// Helper trait to specialize `fold` and `try_fold` for `&mut I where I: Sized`
4253trait IteratorRefSpec: Iterator {
4254    fn spec_fold<B, F>(self, init: B, f: F) -> B
4255    where
4256        F: FnMut(B, Self::Item) -> B;
4257
4258    fn spec_try_fold<B, F, R>(&mut self, init: B, f: F) -> R
4259    where
4260        F: FnMut(B, Self::Item) -> R,
4261        R: Try<Output = B>;
4262}
4263
4264impl<I: Iterator + ?Sized> IteratorRefSpec for &mut I {
4265    default fn spec_fold<B, F>(self, init: B, mut f: F) -> B
4266    where
4267        F: FnMut(B, Self::Item) -> B,
4268    {
4269        let mut accum = init;
4270        while let Some(x) = self.next() {
4271            accum = f(accum, x);
4272        }
4273        accum
4274    }
4275
4276    default fn spec_try_fold<B, F, R>(&mut self, init: B, mut f: F) -> R
4277    where
4278        F: FnMut(B, Self::Item) -> R,
4279        R: Try<Output = B>,
4280    {
4281        let mut accum = init;
4282        while let Some(x) = self.next() {
4283            accum = f(accum, x)?;
4284        }
4285        try { accum }
4286    }
4287}
4288
4289impl<I: Iterator> IteratorRefSpec for &mut I {
4290    impl_fold_via_try_fold! { spec_fold -> spec_try_fold }
4291
4292    fn spec_try_fold<B, F, R>(&mut self, init: B, f: F) -> R
4293    where
4294        F: FnMut(B, Self::Item) -> R,
4295        R: Try<Output = B>,
4296    {
4297        (**self).try_fold(init, f)
4298    }
4299}
````