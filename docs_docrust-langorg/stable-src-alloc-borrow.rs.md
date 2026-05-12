---
title: borrow.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#72-74
source: crawler
fetched_at: 2026-05-06T21:26:28.925043178-03:00
rendered_js: false
word_count: 1947
summary: This document defines the ToOwned trait for converting borrowed data into owned forms and the Cow enum, which provides a smart pointer for clone-on-write functionality.
tags:
    - rust
    - memory-management
    - borrow-checker
    - smart-pointer
    - data-conversion
category: concept
---

## alloc/ borrow.rs

````rust
1//! A module for working with borrowed data.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5#[stable(feature = "rust1", since = "1.0.0")]
6pub use core::borrow::{Borrow, BorrowMut};
7use core::cmp::Ordering;
8use core::hash::{Hash, Hasher};
9#[cfg(not(no_global_oom_handling))]
10use core::ops::{Add, AddAssign};
11use core::ops::{Deref, DerefPure};
12
13use Cow::*;
14
15use crate::fmt;
16#[cfg(not(no_global_oom_handling))]
17use crate::string::String;
18
19/// A generalization of `Clone` to borrowed data.
20///
21/// Some types make it possible to go from borrowed to owned, usually by
22/// implementing the `Clone` trait. But `Clone` works only for going from `&T`
23/// to `T`. The `ToOwned` trait generalizes `Clone` to construct owned data
24/// from any borrow of a given type.
25#[rustc_diagnostic_item = "ToOwned"]
26#[stable(feature = "rust1", since = "1.0.0")]
27pub trait ToOwned {
28    /// The resulting type after obtaining ownership.
29    #[stable(feature = "rust1", since = "1.0.0")]
30    type Owned: Borrow<Self>;
31
32    /// Creates owned data from borrowed data, usually by cloning.
33    ///
34    /// # Examples
35    ///
36    /// Basic usage:
37    ///
38    /// ```
39    /// let s: &str = "a";
40    /// let ss: String = s.to_owned();
41    ///
42    /// let v: &[i32] = &[1, 2];
43    /// let vv: Vec<i32> = v.to_owned();
44    /// ```
45    #[stable(feature = "rust1", since = "1.0.0")]
46    #[must_use = "cloning is often expensive and is not expected to have side effects"]
47    #[rustc_diagnostic_item = "to_owned_method"]
48    fn to_owned(&self) -> Self::Owned;
49
50    /// Uses borrowed data to replace owned data, usually by cloning.
51    ///
52    /// This is borrow-generalized version of [`Clone::clone_from`].
53    ///
54    /// # Examples
55    ///
56    /// Basic usage:
57    ///
58    /// ```
59    /// let mut s: String = String::new();
60    /// "hello".clone_into(&mut s);
61    ///
62    /// let mut v: Vec<i32> = Vec::new();
63    /// [1, 2][..].clone_into(&mut v);
64    /// ```
65    #[stable(feature = "toowned_clone_into", since = "1.63.0")]
66    fn clone_into(&self, target: &mut Self::Owned) {
67        *target = self.to_owned();
68    }
69}
70
71#[stable(feature = "rust1", since = "1.0.0")]
72impl<T> ToOwned for T
73where
74    T: Clone,
75{
76    type Owned = T;
77    fn to_owned(&self) -> T {
78        self.clone()
79    }
80
81    fn clone_into(&self, target: &mut T) {
82        target.clone_from(self);
83    }
84}
85
86/// A clone-on-write smart pointer.
87///
88/// The type `Cow` is a smart pointer providing clone-on-write functionality: it
89/// can enclose and provide immutable access to borrowed data, and clone the
90/// data lazily when mutation or ownership is required. The type is designed to
91/// work with general borrowed data via the `Borrow` trait.
92///
93/// `Cow` implements `Deref`, which means that you can call
94/// non-mutating methods directly on the data it encloses. If mutation
95/// is desired, `to_mut` will obtain a mutable reference to an owned
96/// value, cloning if necessary.
97///
98/// If you need reference-counting pointers, note that
99/// [`Rc::make_mut`][crate::rc::Rc::make_mut] and
100/// [`Arc::make_mut`][crate::sync::Arc::make_mut] can provide clone-on-write
101/// functionality as well.
102///
103/// # Examples
104///
105/// ```
106/// use std::borrow::Cow;
107///
108/// fn abs_all(input: &mut Cow<'_, [i32]>) {
109///     for i in 0..input.len() {
110///         let v = input[i];
111///         if v < 0 {
112///             // Clones into a vector if not already owned.
113///             input.to_mut()[i] = -v;
114///         }
115///     }
116/// }
117///
118/// // No clone occurs because `input` doesn't need to be mutated.
119/// let slice = [0, 1, 2];
120/// let mut input = Cow::from(&slice[..]);
121/// abs_all(&mut input);
122///
123/// // Clone occurs because `input` needs to be mutated.
124/// let slice = [-1, 0, 1];
125/// let mut input = Cow::from(&slice[..]);
126/// abs_all(&mut input);
127///
128/// // No clone occurs because `input` is already owned.
129/// let mut input = Cow::from(vec![-1, 0, 1]);
130/// abs_all(&mut input);
131/// ```
132///
133/// Another example showing how to keep `Cow` in a struct:
134///
135/// ```
136/// use std::borrow::Cow;
137///
138/// struct Items<'a, X> where [X]: ToOwned<Owned = Vec<X>> {
139///     values: Cow<'a, [X]>,
140/// }
141///
142/// impl<'a, X: Clone + 'a> Items<'a, X> where [X]: ToOwned<Owned = Vec<X>> {
143///     fn new(v: Cow<'a, [X]>) -> Self {
144///         Items { values: v }
145///     }
146/// }
147///
148/// // Creates a container from borrowed values of a slice
149/// let readonly = [1, 2];
150/// let borrowed = Items::new((&readonly[..]).into());
151/// match borrowed {
152///     Items { values: Cow::Borrowed(b) } => println!("borrowed {b:?}"),
153///     _ => panic!("expect borrowed value"),
154/// }
155///
156/// let mut clone_on_write = borrowed;
157/// // Mutates the data from slice into owned vec and pushes a new value on top
158/// clone_on_write.values.to_mut().push(3);
159/// println!("clone_on_write = {:?}", clone_on_write.values);
160///
161/// // The data was mutated. Let's check it out.
162/// match clone_on_write {
163///     Items { values: Cow::Owned(_) } => println!("clone_on_write contains owned data"),
164///     _ => panic!("expect owned data"),
165/// }
166/// ```
167#[stable(feature = "rust1", since = "1.0.0")]
168#[rustc_diagnostic_item = "Cow"]
169pub enum Cow<'a, B: ?Sized + 'a>
170where
171    B: ToOwned,
172{
173    /// Borrowed data.
174    #[stable(feature = "rust1", since = "1.0.0")]
175    Borrowed(#[stable(feature = "rust1", since = "1.0.0")] &'a B),
176
177    /// Owned data.
178    #[stable(feature = "rust1", since = "1.0.0")]
179    Owned(#[stable(feature = "rust1", since = "1.0.0")] <B as ToOwned>::Owned),
180}
181
182// FIXME(inference): const bounds removed due to inference regressions found by crater;
183//   see https://github.com/rust-lang/rust/issues/147964
184// #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
185#[stable(feature = "rust1", since = "1.0.0")]
186impl<'a, B: ?Sized + ToOwned> Borrow<B> for Cow<'a, B>
187// where
188//     B::Owned: [const] Borrow<B>,
189{
190    fn borrow(&self) -> &B {
191        &**self
192    }
193}
194
195#[stable(feature = "rust1", since = "1.0.0")]
196impl<B: ?Sized + ToOwned> Clone for Cow<'_, B> {
197    fn clone(&self) -> Self {
198        match *self {
199            Borrowed(b) => Borrowed(b),
200            Owned(ref o) => {
201                let b: &B = o.borrow();
202                Owned(b.to_owned())
203            }
204        }
205    }
206
207    fn clone_from(&mut self, source: &Self) {
208        match (self, source) {
209            (&mut Owned(ref mut dest), &Owned(ref o)) => o.borrow().clone_into(dest),
210            (t, s) => *t = s.clone(),
211        }
212    }
213}
214
215impl<B: ?Sized + ToOwned> Cow<'_, B> {
216    /// Returns true if the data is borrowed, i.e. if `to_mut` would require additional work.
217    ///
218    /// Note: this is an associated function, which means that you have to call
219    /// it as `Cow::is_borrowed(&c)` instead of `c.is_borrowed()`. This is so
220    /// that there is no conflict with a method on the inner type.
221    ///
222    /// # Examples
223    ///
224    /// ```
225    /// #![feature(cow_is_borrowed)]
226    /// use std::borrow::Cow;
227    ///
228    /// let cow = Cow::Borrowed("moo");
229    /// assert!(Cow::is_borrowed(&cow));
230    ///
231    /// let bull: Cow<'_, str> = Cow::Owned("...moo?".to_string());
232    /// assert!(!Cow::is_borrowed(&bull));
233    /// ```
234    #[unstable(feature = "cow_is_borrowed", issue = "65143")]
235    pub const fn is_borrowed(c: &Self) -> bool {
236        match *c {
237            Borrowed(_) => true,
238            Owned(_) => false,
239        }
240    }
241
242    /// Returns true if the data is owned, i.e. if `to_mut` would be a no-op.
243    ///
244    /// Note: this is an associated function, which means that you have to call
245    /// it as `Cow::is_owned(&c)` instead of `c.is_owned()`. This is so that
246    /// there is no conflict with a method on the inner type.
247    ///
248    /// # Examples
249    ///
250    /// ```
251    /// #![feature(cow_is_borrowed)]
252    /// use std::borrow::Cow;
253    ///
254    /// let cow: Cow<'_, str> = Cow::Owned("moo".to_string());
255    /// assert!(Cow::is_owned(&cow));
256    ///
257    /// let bull = Cow::Borrowed("...moo?");
258    /// assert!(!Cow::is_owned(&bull));
259    /// ```
260    #[unstable(feature = "cow_is_borrowed", issue = "65143")]
261    pub const fn is_owned(c: &Self) -> bool {
262        !Cow::is_borrowed(c)
263    }
264
265    /// Acquires a mutable reference to the owned form of the data.
266    ///
267    /// Clones the data if it is not already owned.
268    ///
269    /// # Examples
270    ///
271    /// ```
272    /// use std::borrow::Cow;
273    ///
274    /// let mut cow = Cow::Borrowed("foo");
275    /// cow.to_mut().make_ascii_uppercase();
276    ///
277    /// assert_eq!(
278    ///   cow,
279    ///   Cow::Owned(String::from("FOO")) as Cow<'_, str>
280    /// );
281    /// ```
282    #[stable(feature = "rust1", since = "1.0.0")]
283    pub fn to_mut(&mut self) -> &mut <B as ToOwned>::Owned {
284        match *self {
285            Borrowed(borrowed) => {
286                *self = Owned(borrowed.to_owned());
287                match *self {
288                    Borrowed(..) => unreachable!(),
289                    Owned(ref mut owned) => owned,
290                }
291            }
292            Owned(ref mut owned) => owned,
293        }
294    }
295
296    /// Extracts the owned data.
297    ///
298    /// Clones the data if it is not already owned.
299    ///
300    /// # Examples
301    ///
302    /// Calling `into_owned` on a `Cow::Borrowed` returns a clone of the borrowed data:
303    ///
304    /// ```
305    /// use std::borrow::Cow;
306    ///
307    /// let s = "Hello world!";
308    /// let cow = Cow::Borrowed(s);
309    ///
310    /// assert_eq!(
311    ///   cow.into_owned(),
312    ///   String::from(s)
313    /// );
314    /// ```
315    ///
316    /// Calling `into_owned` on a `Cow::Owned` returns the owned data. The data is moved out of the
317    /// `Cow` without being cloned.
318    ///
319    /// ```
320    /// use std::borrow::Cow;
321    ///
322    /// let s = "Hello world!";
323    /// let cow: Cow<'_, str> = Cow::Owned(String::from(s));
324    ///
325    /// assert_eq!(
326    ///   cow.into_owned(),
327    ///   String::from(s)
328    /// );
329    /// ```
330    #[stable(feature = "rust1", since = "1.0.0")]
331    pub fn into_owned(self) -> <B as ToOwned>::Owned {
332        match self {
333            Borrowed(borrowed) => borrowed.to_owned(),
334            Owned(owned) => owned,
335        }
336    }
337}
338
339// FIXME(inference): const bounds removed due to inference regressions found by crater;
340//   see https://github.com/rust-lang/rust/issues/147964
341// #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
342#[stable(feature = "rust1", since = "1.0.0")]
343impl<B: ?Sized + ToOwned> Deref for Cow<'_, B>
344// where
345//     B::Owned: [const] Borrow<B>,
346{
347    type Target = B;
348
349    fn deref(&self) -> &B {
350        match *self {
351            Borrowed(borrowed) => borrowed,
352            Owned(ref owned) => owned.borrow(),
353        }
354    }
355}
356
357// `Cow<'_, T>` can only implement `DerefPure` if `<T::Owned as Borrow<T>>` (and `BorrowMut<T>`) is trusted.
358// For now, we restrict `DerefPure for Cow<T>` to `T: Sized` (`T as Borrow<T>` is trusted),
359// `str` (`String as Borrow<str>` is trusted) and `[T]` (`Vec<T> as Borrow<[T]>` is trusted).
360// In the future, a `BorrowPure<T>` trait analogous to `DerefPure` might generalize this.
361#[unstable(feature = "deref_pure_trait", issue = "87121")]
362unsafe impl<T: Clone> DerefPure for Cow<'_, T> {}
363#[cfg(not(no_global_oom_handling))]
364#[unstable(feature = "deref_pure_trait", issue = "87121")]
365unsafe impl DerefPure for Cow<'_, str> {}
366#[cfg(not(no_global_oom_handling))]
367#[unstable(feature = "deref_pure_trait", issue = "87121")]
368unsafe impl<T: Clone> DerefPure for Cow<'_, [T]> {}
369
370#[stable(feature = "rust1", since = "1.0.0")]
371impl<B: ?Sized> Eq for Cow<'_, B> where B: Eq + ToOwned {}
372
373#[stable(feature = "rust1", since = "1.0.0")]
374impl<B: ?Sized> Ord for Cow<'_, B>
375where
376    B: Ord + ToOwned,
377{
378    #[inline]
379    fn cmp(&self, other: &Self) -> Ordering {
380        Ord::cmp(&**self, &**other)
381    }
382}
383
384#[stable(feature = "rust1", since = "1.0.0")]
385impl<'a, 'b, B: ?Sized, C: ?Sized> PartialEq<Cow<'b, C>> for Cow<'a, B>
386where
387    B: PartialEq<C> + ToOwned,
388    C: ToOwned,
389{
390    #[inline]
391    fn eq(&self, other: &Cow<'b, C>) -> bool {
392        PartialEq::eq(&**self, &**other)
393    }
394}
395
396#[stable(feature = "rust1", since = "1.0.0")]
397impl<'a, B: ?Sized> PartialOrd for Cow<'a, B>
398where
399    B: PartialOrd + ToOwned,
400{
401    #[inline]
402    fn partial_cmp(&self, other: &Cow<'a, B>) -> Option<Ordering> {
403        PartialOrd::partial_cmp(&**self, &**other)
404    }
405}
406
407#[stable(feature = "rust1", since = "1.0.0")]
408impl<B: ?Sized> fmt::Debug for Cow<'_, B>
409where
410    B: fmt::Debug + ToOwned<Owned: fmt::Debug>,
411{
412    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
413        match *self {
414            Borrowed(ref b) => fmt::Debug::fmt(b, f),
415            Owned(ref o) => fmt::Debug::fmt(o, f),
416        }
417    }
418}
419
420#[stable(feature = "rust1", since = "1.0.0")]
421impl<B: ?Sized> fmt::Display for Cow<'_, B>
422where
423    B: fmt::Display + ToOwned<Owned: fmt::Display>,
424{
425    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
426        match *self {
427            Borrowed(ref b) => fmt::Display::fmt(b, f),
428            Owned(ref o) => fmt::Display::fmt(o, f),
429        }
430    }
431}
432
433#[stable(feature = "default", since = "1.11.0")]
434impl<B: ?Sized> Default for Cow<'_, B>
435where
436    B: ToOwned<Owned: Default>,
437{
438    /// Creates an owned Cow<'a, B> with the default value for the contained owned value.
439    fn default() -> Self {
440        Owned(<B as ToOwned>::Owned::default())
441    }
442}
443
444#[stable(feature = "rust1", since = "1.0.0")]
445impl<B: ?Sized> Hash for Cow<'_, B>
446where
447    B: Hash + ToOwned,
448{
449    #[inline]
450    fn hash<H: Hasher>(&self, state: &mut H) {
451        Hash::hash(&**self, state)
452    }
453}
454
455// FIXME(inference): const bounds removed due to inference regressions found by crater;
456//   see https://github.com/rust-lang/rust/issues/147964
457// #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
458#[stable(feature = "rust1", since = "1.0.0")]
459impl<T: ?Sized + ToOwned> AsRef<T> for Cow<'_, T>
460// where
461//     T::Owned: [const] Borrow<T>,
462{
463    fn as_ref(&self) -> &T {
464        self
465    }
466}
467
468#[cfg(not(no_global_oom_handling))]
469#[stable(feature = "cow_add", since = "1.14.0")]
470impl<'a> Add<&'a str> for Cow<'a, str> {
471    type Output = Cow<'a, str>;
472
473    #[inline]
474    fn add(mut self, rhs: &'a str) -> Self::Output {
475        self += rhs;
476        self
477    }
478}
479
480#[cfg(not(no_global_oom_handling))]
481#[stable(feature = "cow_add", since = "1.14.0")]
482impl<'a> Add<Cow<'a, str>> for Cow<'a, str> {
483    type Output = Cow<'a, str>;
484
485    #[inline]
486    fn add(mut self, rhs: Cow<'a, str>) -> Self::Output {
487        self += rhs;
488        self
489    }
490}
491
492#[cfg(not(no_global_oom_handling))]
493#[stable(feature = "cow_add", since = "1.14.0")]
494impl<'a> AddAssign<&'a str> for Cow<'a, str> {
495    fn add_assign(&mut self, rhs: &'a str) {
496        if self.is_empty() {
497            *self = Cow::Borrowed(rhs)
498        } else if !rhs.is_empty() {
499            if let Cow::Borrowed(lhs) = *self {
500                let mut s = String::with_capacity(lhs.len() + rhs.len());
501                s.push_str(lhs);
502                *self = Cow::Owned(s);
503            }
504            self.to_mut().push_str(rhs);
505        }
506    }
507}
508
509#[cfg(not(no_global_oom_handling))]
510#[stable(feature = "cow_add", since = "1.14.0")]
511impl<'a> AddAssign<Cow<'a, str>> for Cow<'a, str> {
512    fn add_assign(&mut self, rhs: Cow<'a, str>) {
513        if self.is_empty() {
514            *self = rhs
515        } else if !rhs.is_empty() {
516            if let Cow::Borrowed(lhs) = *self {
517                let mut s = String::with_capacity(lhs.len() + rhs.len());
518                s.push_str(lhs);
519                *self = Cow::Owned(s);
520            }
521            self.to_mut().push_str(&rhs);
522        }
523    }
524}
````