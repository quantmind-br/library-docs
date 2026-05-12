---
title: collect.rs - source
url: https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420
source: crawler
fetched_at: 2026-05-06T21:23:20.1890074-03:00
rendered_js: false
word_count: 2497
summary: This document defines the FromIterator and IntoIterator traits, which facilitate the conversion between collections and iterators in Rust.
tags:
    - rust
    - iterator
    - traits
    - collection
    - from-iterator
    - into-iterator
category: reference
---

## core/iter/traits/ collect.rs

````rust
1use super::TrustedLen;
2
3/// Conversion from an [`Iterator`].
4///
5/// By implementing `FromIterator` for a type, you define how it will be
6/// created from an iterator. This is common for types which describe a
7/// collection of some kind.
8///
9/// If you want to create a collection from the contents of an iterator, the
10/// [`Iterator::collect()`] method is preferred. However, when you need to
11/// specify the container type, [`FromIterator::from_iter()`] can be more
12/// readable than using a turbofish (e.g. `::<Vec<_>>()`). See the
13/// [`Iterator::collect()`] documentation for more examples of its use.
14///
15/// See also: [`IntoIterator`].
16///
17/// # Examples
18///
19/// Basic usage:
20///
21/// ```
22/// let five_fives = std::iter::repeat(5).take(5);
23///
24/// let v = Vec::from_iter(five_fives);
25///
26/// assert_eq!(v, vec![5, 5, 5, 5, 5]);
27/// ```
28///
29/// Using [`Iterator::collect()`] to implicitly use `FromIterator`:
30///
31/// ```
32/// let five_fives = std::iter::repeat(5).take(5);
33///
34/// let v: Vec<i32> = five_fives.collect();
35///
36/// assert_eq!(v, vec![5, 5, 5, 5, 5]);
37/// ```
38///
39/// Using [`FromIterator::from_iter()`] as a more readable alternative to
40/// [`Iterator::collect()`]:
41///
42/// ```
43/// use std::collections::VecDeque;
44/// let first = (0..10).collect::<VecDeque<i32>>();
45/// let second = VecDeque::from_iter(0..10);
46///
47/// assert_eq!(first, second);
48/// ```
49///
50/// Implementing `FromIterator` for your type:
51///
52/// ```
53/// // A sample collection, that's just a wrapper over Vec<T>
54/// #[derive(Debug)]
55/// struct MyCollection(Vec<i32>);
56///
57/// // Let's give it some methods so we can create one and add things
58/// // to it.
59/// impl MyCollection {
60///     fn new() -> MyCollection {
61///         MyCollection(Vec::new())
62///     }
63///
64///     fn add(&mut self, elem: i32) {
65///         self.0.push(elem);
66///     }
67/// }
68///
69/// // and we'll implement FromIterator
70/// impl FromIterator<i32> for MyCollection {
71///     fn from_iter<I: IntoIterator<Item=i32>>(iter: I) -> Self {
72///         let mut c = MyCollection::new();
73///
74///         for i in iter {
75///             c.add(i);
76///         }
77///
78///         c
79///     }
80/// }
81///
82/// // Now we can make a new iterator...
83/// let iter = (0..5).into_iter();
84///
85/// // ... and make a MyCollection out of it
86/// let c = MyCollection::from_iter(iter);
87///
88/// assert_eq!(c.0, vec![0, 1, 2, 3, 4]);
89///
90/// // collect works too!
91///
92/// let iter = (0..5).into_iter();
93/// let c: MyCollection = iter.collect();
94///
95/// assert_eq!(c.0, vec![0, 1, 2, 3, 4]);
96/// ```
97#[stable(feature = "rust1", since = "1.0.0")]
98#[rustc_on_unimplemented(
99    on(
100        Self = "&[{A}]",
101        message = "a slice of type `{Self}` cannot be built since we need to store the elements somewhere",
102        label = "try explicitly collecting into a `Vec<{A}>`",
103    ),
104    on(
105        all(A = "{integer}", any(Self = "&[{integral}]",)),
106        message = "a slice of type `{Self}` cannot be built since we need to store the elements somewhere",
107        label = "try explicitly collecting into a `Vec<{A}>`",
108    ),
109    on(
110        Self = "[{A}]",
111        message = "a slice of type `{Self}` cannot be built since `{Self}` has no definite size",
112        label = "try explicitly collecting into a `Vec<{A}>`",
113    ),
114    on(
115        all(A = "{integer}", any(Self = "[{integral}]",)),
116        message = "a slice of type `{Self}` cannot be built since `{Self}` has no definite size",
117        label = "try explicitly collecting into a `Vec<{A}>`",
118    ),
119    on(
120        Self = "[{A}; _]",
121        message = "an array of type `{Self}` cannot be built directly from an iterator",
122        label = "try collecting into a `Vec<{A}>`, then using `.try_into()`",
123    ),
124    on(
125        all(A = "{integer}", any(Self = "[{integral}; _]",)),
126        message = "an array of type `{Self}` cannot be built directly from an iterator",
127        label = "try collecting into a `Vec<{A}>`, then using `.try_into()`",
128    ),
129    message = "a value of type `{Self}` cannot be built from an iterator \
130               over elements of type `{A}`",
131    label = "value of type `{Self}` cannot be built from `std::iter::Iterator<Item={A}>`"
132)]
133#[rustc_diagnostic_item = "FromIterator"]
134pub trait FromIterator<A>: Sized {
135    /// Creates a value from an iterator.
136    ///
137    /// See the [module-level documentation] for more.
138    ///
139    /// [module-level documentation]: crate::iter
140    ///
141    /// # Examples
142    ///
143    /// ```
144    /// let five_fives = std::iter::repeat(5).take(5);
145    ///
146    /// let v = Vec::from_iter(five_fives);
147    ///
148    /// assert_eq!(v, vec![5, 5, 5, 5, 5]);
149    /// ```
150    #[stable(feature = "rust1", since = "1.0.0")]
151    #[rustc_diagnostic_item = "from_iter_fn"]
152    fn from_iter<T: IntoIterator<Item = A>>(iter: T) -> Self;
153}
154
155/// Conversion into an [`Iterator`].
156///
157/// By implementing `IntoIterator` for a type, you define how it will be
158/// converted to an iterator. This is common for types which describe a
159/// collection of some kind.
160///
161/// One benefit of implementing `IntoIterator` is that your type will [work
162/// with Rust's `for` loop syntax](crate::iter#for-loops-and-intoiterator).
163///
164/// See also: [`FromIterator`].
165///
166/// # Examples
167///
168/// Basic usage:
169///
170/// ```
171/// let v = [1, 2, 3];
172/// let mut iter = v.into_iter();
173///
174/// assert_eq!(Some(1), iter.next());
175/// assert_eq!(Some(2), iter.next());
176/// assert_eq!(Some(3), iter.next());
177/// assert_eq!(None, iter.next());
178/// ```
179/// Implementing `IntoIterator` for your type:
180///
181/// ```
182/// // A sample collection, that's just a wrapper over Vec<T>
183/// #[derive(Debug)]
184/// struct MyCollection(Vec<i32>);
185///
186/// // Let's give it some methods so we can create one and add things
187/// // to it.
188/// impl MyCollection {
189///     fn new() -> MyCollection {
190///         MyCollection(Vec::new())
191///     }
192///
193///     fn add(&mut self, elem: i32) {
194///         self.0.push(elem);
195///     }
196/// }
197///
198/// // and we'll implement IntoIterator
199/// impl IntoIterator for MyCollection {
200///     type Item = i32;
201///     type IntoIter = std::vec::IntoIter<Self::Item>;
202///
203///     fn into_iter(self) -> Self::IntoIter {
204///         self.0.into_iter()
205///     }
206/// }
207///
208/// // Now we can make a new collection...
209/// let mut c = MyCollection::new();
210///
211/// // ... add some stuff to it ...
212/// c.add(0);
213/// c.add(1);
214/// c.add(2);
215///
216/// // ... and then turn it into an Iterator:
217/// for (i, n) in c.into_iter().enumerate() {
218///     assert_eq!(i as i32, n);
219/// }
220/// ```
221///
222/// It is common to use `IntoIterator` as a trait bound. This allows
223/// the input collection type to change, so long as it is still an
224/// iterator. Additional bounds can be specified by restricting on
225/// `Item`:
226///
227/// ```rust
228/// fn collect_as_strings<T>(collection: T) -> Vec<String>
229/// where
230///     T: IntoIterator,
231///     T::Item: std::fmt::Debug,
232/// {
233///     collection
234///         .into_iter()
235///         .map(|item| format!("{item:?}"))
236///         .collect()
237/// }
238/// ```
239#[rustc_diagnostic_item = "IntoIterator"]
240#[rustc_on_unimplemented(
241    on(
242        Self = "core::ops::range::RangeTo<Idx>",
243        label = "if you meant to iterate until a value, add a starting value",
244        note = "`..end` is a `RangeTo`, which cannot be iterated on; you might have meant to have a \
245              bounded `Range`: `0..end`"
246    ),
247    on(
248        Self = "core::ops::range::RangeToInclusive<Idx>",
249        label = "if you meant to iterate until a value (including it), add a starting value",
250        note = "`..=end` is a `RangeToInclusive`, which cannot be iterated on; you might have meant \
251              to have a bounded `RangeInclusive`: `0..=end`"
252    ),
253    on(
254        Self = "[]",
255        label = "`{Self}` is not an iterator; try calling `.into_iter()` or `.iter()`"
256    ),
257    on(Self = "&[]", label = "`{Self}` is not an iterator; try calling `.iter()`"),
258    on(
259        Self = "alloc::vec::Vec<T, A>",
260        label = "`{Self}` is not an iterator; try calling `.into_iter()` or `.iter()`"
261    ),
262    on(Self = "&str", label = "`{Self}` is not an iterator; try calling `.chars()` or `.bytes()`"),
263    on(
264        Self = "alloc::string::String",
265        label = "`{Self}` is not an iterator; try calling `.chars()` or `.bytes()`"
266    ),
267    on(
268        Self = "{integral}",
269        note = "if you want to iterate between `start` until a value `end`, use the exclusive range \
270              syntax `start..end` or the inclusive range syntax `start..=end`"
271    ),
272    on(
273        Self = "{float}",
274        note = "if you want to iterate between `start` until a value `end`, use the exclusive range \
275              syntax `start..end` or the inclusive range syntax `start..=end`"
276    ),
277    label = "`{Self}` is not an iterator",
278    message = "`{Self}` is not an iterator"
279)]
280#[rustc_skip_during_method_dispatch(array, boxed_slice)]
281#[stable(feature = "rust1", since = "1.0.0")]
282#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
283pub const trait IntoIterator {
284    /// The type of the elements being iterated over.
285    #[rustc_diagnostic_item = "IntoIteratorItem"]
286    #[stable(feature = "rust1", since = "1.0.0")]
287    type Item;
288
289    /// Which kind of iterator are we turning this into?
290    #[stable(feature = "rust1", since = "1.0.0")]
291    type IntoIter: Iterator<Item = Self::Item>;
292
293    /// Creates an iterator from a value.
294    ///
295    /// See the [module-level documentation] for more.
296    ///
297    /// [module-level documentation]: crate::iter
298    ///
299    /// # Examples
300    ///
301    /// ```
302    /// let v = [1, 2, 3];
303    /// let mut iter = v.into_iter();
304    ///
305    /// assert_eq!(Some(1), iter.next());
306    /// assert_eq!(Some(2), iter.next());
307    /// assert_eq!(Some(3), iter.next());
308    /// assert_eq!(None, iter.next());
309    /// ```
310    #[lang = "into_iter"]
311    #[stable(feature = "rust1", since = "1.0.0")]
312    fn into_iter(self) -> Self::IntoIter;
313}
314
315#[stable(feature = "rust1", since = "1.0.0")]
316#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
317impl<I: [const] Iterator> const IntoIterator for I {
318    type Item = I::Item;
319    type IntoIter = I;
320
321    #[inline]
322    fn into_iter(self) -> I {
323        self
324    }
325}
326
327/// Extend a collection with the contents of an iterator.
328///
329/// Iterators produce a series of values, and collections can also be thought
330/// of as a series of values. The `Extend` trait bridges this gap, allowing you
331/// to extend a collection by including the contents of that iterator. When
332/// extending a collection with an already existing key, that entry is updated
333/// or, in the case of collections that permit multiple entries with equal
334/// keys, that entry is inserted.
335///
336/// # Examples
337///
338/// Basic usage:
339///
340/// ```
341/// // You can extend a String with some chars:
342/// let mut message = String::from("The first three letters are: ");
343///
344/// message.extend(&['a', 'b', 'c']);
345///
346/// assert_eq!("abc", &message[29..32]);
347/// ```
348///
349/// Implementing `Extend`:
350///
351/// ```
352/// // A sample collection, that's just a wrapper over Vec<T>
353/// #[derive(Debug)]
354/// struct MyCollection(Vec<i32>);
355///
356/// // Let's give it some methods so we can create one and add things
357/// // to it.
358/// impl MyCollection {
359///     fn new() -> MyCollection {
360///         MyCollection(Vec::new())
361///     }
362///
363///     fn add(&mut self, elem: i32) {
364///         self.0.push(elem);
365///     }
366/// }
367///
368/// // since MyCollection has a list of i32s, we implement Extend for i32
369/// impl Extend<i32> for MyCollection {
370///
371///     // This is a bit simpler with the concrete type signature: we can call
372///     // extend on anything which can be turned into an Iterator which gives
373///     // us i32s. Because we need i32s to put into MyCollection.
374///     fn extend<T: IntoIterator<Item=i32>>(&mut self, iter: T) {
375///
376///         // The implementation is very straightforward: loop through the
377///         // iterator, and add() each element to ourselves.
378///         for elem in iter {
379///             self.add(elem);
380///         }
381///     }
382/// }
383///
384/// let mut c = MyCollection::new();
385///
386/// c.add(5);
387/// c.add(6);
388/// c.add(7);
389///
390/// // let's extend our collection with three more numbers
391/// c.extend(vec![1, 2, 3]);
392///
393/// // we've added these elements onto the end
394/// assert_eq!("MyCollection([5, 6, 7, 1, 2, 3])", format!("{c:?}"));
395/// ```
396#[stable(feature = "rust1", since = "1.0.0")]
397pub trait Extend<A> {
398    /// Extends a collection with the contents of an iterator.
399    ///
400    /// As this is the only required method for this trait, the [trait-level] docs
401    /// contain more details.
402    ///
403    /// [trait-level]: Extend
404    ///
405    /// # Examples
406    ///
407    /// ```
408    /// // You can extend a String with some chars:
409    /// let mut message = String::from("abc");
410    ///
411    /// message.extend(['d', 'e', 'f'].iter());
412    ///
413    /// assert_eq!("abcdef", &message);
414    /// ```
415    #[stable(feature = "rust1", since = "1.0.0")]
416    fn extend<T: IntoIterator<Item = A>>(&mut self, iter: T);
417
418    /// Extends a collection with exactly one element.
419    #[unstable(feature = "extend_one", issue = "72631")]
420    fn extend_one(&mut self, item: A) {
421        self.extend(Some(item));
422    }
423
424    /// Reserves capacity in a collection for the given number of additional elements.
425    ///
426    /// The default implementation does nothing.
427    #[unstable(feature = "extend_one", issue = "72631")]
428    fn extend_reserve(&mut self, additional: usize) {
429        let _ = additional;
430    }
431
432    /// Extends a collection with one element, without checking there is enough capacity for it.
433    ///
434    /// # Safety
435    ///
436    /// **For callers:** This must only be called when we know the collection has enough capacity
437    /// to contain the new item, for example because we previously called `extend_reserve`.
438    ///
439    /// **For implementors:** For a collection to unsafely rely on this method's safety precondition (that is,
440    /// invoke UB if they are violated), it must implement `extend_reserve` correctly. In other words,
441    /// callers may assume that if they `extend_reserve`ed enough space they can call this method.
442    // This method is for internal usage only. It is only on the trait because of specialization's limitations.
443    #[unstable(feature = "extend_one_unchecked", issue = "none")]
444    #[doc(hidden)]
445    unsafe fn extend_one_unchecked(&mut self, item: A)
446    where
447        Self: Sized,
448    {
449        self.extend_one(item);
450    }
451}
452
453#[stable(feature = "extend_for_unit", since = "1.28.0")]
454impl Extend<()> for () {
455    fn extend<T: IntoIterator<Item = ()>>(&mut self, iter: T) {
456        iter.into_iter().for_each(drop)
457    }
458    fn extend_one(&mut self, _item: ()) {}
459}
460
461/// This trait is implemented for tuples up to twelve items long. The `impl`s for
462/// 1- and 3- through 12-ary tuples were stabilized after 2-tuples, in 1.85.0.
463#[doc(fake_variadic)] // the other implementations are below.
464#[stable(feature = "extend_for_tuple", since = "1.56.0")]
465impl<T, ExtendT> Extend<(T,)> for (ExtendT,)
466where
467    ExtendT: Extend<T>,
468{
469    /// Allows to `extend` a tuple of collections that also implement `Extend`.
470    ///
471    /// See also: [`Iterator::unzip`]
472    ///
473    /// # Examples
474    /// ```
475    /// // Example given for a 2-tuple, but 1- through 12-tuples are supported
476    /// let mut tuple = (vec![0], vec![1]);
477    /// tuple.extend([(2, 3), (4, 5), (6, 7)]);
478    /// assert_eq!(tuple.0, [0, 2, 4, 6]);
479    /// assert_eq!(tuple.1, [1, 3, 5, 7]);
480    ///
481    /// // also allows for arbitrarily nested tuples as elements
482    /// let mut nested_tuple = (vec![1], (vec![2], vec![3]));
483    /// nested_tuple.extend([(4, (5, 6)), (7, (8, 9))]);
484    ///
485    /// let (a, (b, c)) = nested_tuple;
486    /// assert_eq!(a, [1, 4, 7]);
487    /// assert_eq!(b, [2, 5, 8]);
488    /// assert_eq!(c, [3, 6, 9]);
489    /// ```
490    fn extend<I: IntoIterator<Item = (T,)>>(&mut self, iter: I) {
491        self.0.extend(iter.into_iter().map(|t| t.0));
492    }
493
494    fn extend_one(&mut self, item: (T,)) {
495        self.0.extend_one(item.0)
496    }
497
498    fn extend_reserve(&mut self, additional: usize) {
499        self.0.extend_reserve(additional)
500    }
501
502    unsafe fn extend_one_unchecked(&mut self, item: (T,)) {
503        // SAFETY: the caller guarantees all preconditions.
504        unsafe { self.0.extend_one_unchecked(item.0) }
505    }
506}
507
508/// This implementation turns an iterator of tuples into a tuple of types which implement
509/// [`Default`] and [`Extend`].
510///
511/// This is similar to [`Iterator::unzip`], but is also composable with other [`FromIterator`]
512/// implementations:
513///
514/// ```rust
515/// # fn main() -> Result<(), core::num::ParseIntError> {
516/// let string = "1,2,123,4";
517///
518/// // Example given for a 2-tuple, but 1- through 12-tuples are supported
519/// let (numbers, lengths): (Vec<_>, Vec<_>) = string
520///     .split(',')
521///     .map(|s| s.parse().map(|n: u32| (n, s.len())))
522///     .collect::<Result<_, _>>()?;
523///
524/// assert_eq!(numbers, [1, 2, 123, 4]);
525/// assert_eq!(lengths, [1, 1, 3, 1]);
526/// # Ok(()) }
527/// ```
528#[doc(fake_variadic)] // the other implementations are below.
529#[stable(feature = "from_iterator_for_tuple", since = "1.79.0")]
530impl<T, ExtendT> FromIterator<(T,)> for (ExtendT,)
531where
532    ExtendT: Default + Extend<T>,
533{
534    fn from_iter<Iter: IntoIterator<Item = (T,)>>(iter: Iter) -> Self {
535        let mut res = ExtendT::default();
536        res.extend(iter.into_iter().map(|t| t.0));
537        (res,)
538    }
539}
540
541/// An implementation of [`extend`](Extend::extend) that calls `extend_one` or
542/// `extend_one_unchecked` for each element of the iterator.
543fn default_extend<ExtendT, I, T>(collection: &mut ExtendT, iter: I)
544where
545    ExtendT: Extend<T>,
546    I: IntoIterator<Item = T>,
547{
548    // Specialize on `TrustedLen` and call `extend_one_unchecked` where
549    // applicable.
550    trait SpecExtend<I> {
551        fn extend(&mut self, iter: I);
552    }
553
554    // Extracting these to separate functions avoid monomorphising the closures
555    // for every iterator type.
556    fn extender<ExtendT, T>(collection: &mut ExtendT) -> impl FnMut(T) + use<'_, ExtendT, T>
557    where
558        ExtendT: Extend<T>,
559    {
560        move |item| collection.extend_one(item)
561    }
562
563    unsafe fn unchecked_extender<ExtendT, T>(
564        collection: &mut ExtendT,
565    ) -> impl FnMut(T) + use<'_, ExtendT, T>
566    where
567        ExtendT: Extend<T>,
568    {
569        // SAFETY: we make sure that there is enough space at the callsite of
570        // this function.
571        move |item| unsafe { collection.extend_one_unchecked(item) }
572    }
573
574    impl<ExtendT, I, T> SpecExtend<I> for ExtendT
575    where
576        ExtendT: Extend<T>,
577        I: Iterator<Item = T>,
578    {
579        default fn extend(&mut self, iter: I) {
580            let (lower_bound, _) = iter.size_hint();
581            if lower_bound > 0 {
582                self.extend_reserve(lower_bound);
583            }
584
585            iter.for_each(extender(self))
586        }
587    }
588
589    impl<ExtendT, I, T> SpecExtend<I> for ExtendT
590    where
591        ExtendT: Extend<T>,
592        I: TrustedLen<Item = T>,
593    {
594        fn extend(&mut self, iter: I) {
595            let (lower_bound, upper_bound) = iter.size_hint();
596            if lower_bound > 0 {
597                self.extend_reserve(lower_bound);
598            }
599
600            if upper_bound.is_none() {
601                // We cannot reserve more than `usize::MAX` items, and this is likely to go out of memory anyway.
602                iter.for_each(extender(self))
603            } else {
604                // SAFETY: We reserve enough space for the `size_hint`, and the iterator is
605                // `TrustedLen` so its `size_hint` is exact.
606                iter.for_each(unsafe { unchecked_extender(self) })
607            }
608        }
609    }
610
611    SpecExtend::extend(collection, iter.into_iter());
612}
613
614// Implements `Extend` and `FromIterator` for tuples with length larger than one.
615macro_rules! impl_extend_tuple {
616    ($(($ty:tt, $extend_ty:tt, $index:tt)),+) => {
617        #[doc(hidden)]
618        #[stable(feature = "extend_for_tuple", since = "1.56.0")]
619        impl<$($ty,)+ $($extend_ty,)+> Extend<($($ty,)+)> for ($($extend_ty,)+)
620        where
621            $($extend_ty: Extend<$ty>,)+
622        {
623            fn extend<T: IntoIterator<Item = ($($ty,)+)>>(&mut self, iter: T) {
624                default_extend(self, iter)
625            }
626
627            fn extend_one(&mut self, item: ($($ty,)+)) {
628                $(self.$index.extend_one(item.$index);)+
629            }
630
631            fn extend_reserve(&mut self, additional: usize) {
632                $(self.$index.extend_reserve(additional);)+
633            }
634
635            unsafe fn extend_one_unchecked(&mut self, item: ($($ty,)+)) {
636                // SAFETY: Those are our safety preconditions, and we correctly forward `extend_reserve`.
637                unsafe {
638                    $(self.$index.extend_one_unchecked(item.$index);)+
639                }
640            }
641        }
642
643        #[doc(hidden)]
644        #[stable(feature = "from_iterator_for_tuple", since = "1.79.0")]
645        impl<$($ty,)+ $($extend_ty,)+> FromIterator<($($ty,)+)> for ($($extend_ty,)+)
646        where
647            $($extend_ty: Default + Extend<$ty>,)+
648        {
649            fn from_iter<Iter: IntoIterator<Item = ($($ty,)+)>>(iter: Iter) -> Self {
650                let mut res = Self::default();
651                res.extend(iter);
652                res
653            }
654        }
655    };
656}
657
658impl_extend_tuple!((A, ExA, 0), (B, ExB, 1));
659impl_extend_tuple!((A, ExA, 0), (B, ExB, 1), (C, ExC, 2));
660impl_extend_tuple!((A, ExA, 0), (B, ExB, 1), (C, ExC, 2), (D, ExD, 3));
661impl_extend_tuple!((A, ExA, 0), (B, ExB, 1), (C, ExC, 2), (D, ExD, 3), (E, ExE, 4));
662impl_extend_tuple!((A, ExA, 0), (B, ExB, 1), (C, ExC, 2), (D, ExD, 3), (E, ExE, 4), (F, ExF, 5));
663impl_extend_tuple!(
664    (A, ExA, 0),
665    (B, ExB, 1),
666    (C, ExC, 2),
667    (D, ExD, 3),
668    (E, ExE, 4),
669    (F, ExF, 5),
670    (G, ExG, 6)
671);
672impl_extend_tuple!(
673    (A, ExA, 0),
674    (B, ExB, 1),
675    (C, ExC, 2),
676    (D, ExD, 3),
677    (E, ExE, 4),
678    (F, ExF, 5),
679    (G, ExG, 6),
680    (H, ExH, 7)
681);
682impl_extend_tuple!(
683    (A, ExA, 0),
684    (B, ExB, 1),
685    (C, ExC, 2),
686    (D, ExD, 3),
687    (E, ExE, 4),
688    (F, ExF, 5),
689    (G, ExG, 6),
690    (H, ExH, 7),
691    (I, ExI, 8)
692);
693impl_extend_tuple!(
694    (A, ExA, 0),
695    (B, ExB, 1),
696    (C, ExC, 2),
697    (D, ExD, 3),
698    (E, ExE, 4),
699    (F, ExF, 5),
700    (G, ExG, 6),
701    (H, ExH, 7),
702    (I, ExI, 8),
703    (J, ExJ, 9)
704);
705impl_extend_tuple!(
706    (A, ExA, 0),
707    (B, ExB, 1),
708    (C, ExC, 2),
709    (D, ExD, 3),
710    (E, ExE, 4),
711    (F, ExF, 5),
712    (G, ExG, 6),
713    (H, ExH, 7),
714    (I, ExI, 8),
715    (J, ExJ, 9),
716    (K, ExK, 10)
717);
718impl_extend_tuple!(
719    (A, ExA, 0),
720    (B, ExB, 1),
721    (C, ExC, 2),
722    (D, ExD, 3),
723    (E, ExE, 4),
724    (F, ExF, 5),
725    (G, ExG, 6),
726    (H, ExH, 7),
727    (I, ExI, 8),
728    (J, ExJ, 9),
729    (K, ExK, 10),
730    (L, ExL, 11)
731);
````