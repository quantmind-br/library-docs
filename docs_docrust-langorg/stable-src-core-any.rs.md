---
title: any.rs - source
url: https://doc.rust-lang.org/stable/src/core/any.rs.html#141
source: crawler
fetched_at: 2026-05-06T21:26:22.958646566-03:00
rendered_js: false
word_count: 4434
summary: This document explains the Any trait in Rust, which enables dynamic typing and runtime type reflection through type IDs and downcasting.
tags:
    - rust
    - dynamic-typing
    - type-reflection
    - any-trait
    - type-id
    - downcasting
    - trait-objects
category: concept
---

## core/ any.rs

````rust
1//! Utilities for dynamic typing or type reflection.
2//!
3//! # `Any` and `TypeId`
4//!
5//! `Any` itself can be used to get a `TypeId`, and has more features when used
6//! as a trait object. As `&dyn Any` (a borrowed trait object), it has the `is`
7//! and `downcast_ref` methods, to test if the contained value is of a given type,
8//! and to get a reference to the inner value as a type. As `&mut dyn Any`, there
9//! is also the `downcast_mut` method, for getting a mutable reference to the
10//! inner value. `Box<dyn Any>` adds the `downcast` method, which attempts to
11//! convert to a `Box<T>`. See the [`Box`] documentation for the full details.
12//!
13//! Note that `&dyn Any` is limited to testing whether a value is of a specified
14//! concrete type, and cannot be used to test whether a type implements a trait.
15//!
16//! [`Box`]: ../../std/boxed/struct.Box.html
17//!
18//! # Smart pointers and `dyn Any`
19//!
20//! One piece of behavior to keep in mind when using `Any` as a trait object,
21//! especially with types like `Box<dyn Any>` or `Arc<dyn Any>`, is that simply
22//! calling `.type_id()` on the value will produce the `TypeId` of the
23//! *container*, not the underlying trait object. This can be avoided by
24//! converting the smart pointer into a `&dyn Any` instead, which will return
25//! the object's `TypeId`. For example:
26//!
27//! ```
28//! use std::any::{Any, TypeId};
29//!
30//! let boxed: Box<dyn Any> = Box::new(3_i32);
31//!
32//! // You're more likely to want this:
33//! let actual_id = (&*boxed).type_id();
34//! // ... than this:
35//! let boxed_id = boxed.type_id();
36//!
37//! assert_eq!(actual_id, TypeId::of::<i32>());
38//! assert_eq!(boxed_id, TypeId::of::<Box<dyn Any>>());
39//! ```
40//!
41//! ## Examples
42//!
43//! Consider a situation where we want to log a value passed to a function.
44//! We know the value we're working on implements `Debug`, but we don't know its
45//! concrete type. We want to give special treatment to certain types: in this
46//! case printing out the length of `String` values prior to their value.
47//! We don't know the concrete type of our value at compile time, so we need to
48//! use runtime reflection instead.
49//!
50//! ```rust
51//! use std::fmt::Debug;
52//! use std::any::Any;
53//!
54//! // Logger function for any type that implements `Debug`.
55//! fn log<T: Any + Debug>(value: &T) {
56//!     let value_any = value as &dyn Any;
57//!
58//!     // Try to convert our value to a `String`. If successful, we want to
59//!     // output the `String`'s length as well as its value. If not, it's a
60//!     // different type: just print it out unadorned.
61//!     match value_any.downcast_ref::<String>() {
62//!         Some(as_string) => {
63//!             println!("String ({}): {}", as_string.len(), as_string);
64//!         }
65//!         None => {
66//!             println!("{value:?}");
67//!         }
68//!     }
69//! }
70//!
71//! // This function wants to log its parameter out prior to doing work with it.
72//! fn do_work<T: Any + Debug>(value: &T) {
73//!     log(value);
74//!     // ...do some other work
75//! }
76//!
77//! fn main() {
78//!     let my_string = "Hello World".to_string();
79//!     do_work(&my_string);
80//!
81//!     let my_i8: i8 = 100;
82//!     do_work(&my_i8);
83//! }
84//! ```
85//!
86
87#![stable(feature = "rust1", since = "1.0.0")]
88
89use crate::intrinsics::{self, type_id_vtable};
90use crate::mem::transmute;
91use crate::mem::type_info::{TraitImpl, TypeKind};
92use crate::{fmt, hash, ptr};
93
94///////////////////////////////////////////////////////////////////////////////
95// Any trait
96///////////////////////////////////////////////////////////////////////////////
97
98/// A trait to emulate dynamic typing.
99///
100/// Most types implement `Any`. However, any type which contains a non-`'static` reference does not.
101/// See the [module-level documentation][mod] for more details.
102///
103/// [mod]: crate::any
104// This trait is not unsafe, though we rely on the specifics of it's sole impl's
105// `type_id` function in unsafe code (e.g., `downcast`). Normally, that would be
106// a problem, but because the only impl of `Any` is a blanket implementation, no
107// other code can implement `Any`.
108//
109// We could plausibly make this trait unsafe -- it would not cause breakage,
110// since we control all the implementations -- but we choose not to as that's
111// both not really necessary and may confuse users about the distinction of
112// unsafe traits and unsafe methods (i.e., `type_id` would still be safe to call,
113// but we would likely want to indicate as such in documentation).
114#[stable(feature = "rust1", since = "1.0.0")]
115#[rustc_diagnostic_item = "Any"]
116pub trait Any: 'static {
117    /// Gets the `TypeId` of `self`.
118    ///
119    /// If called on a `dyn Any` trait object
120    /// (or a trait object of a subtrait of `Any`),
121    /// this returns the `TypeId` of the underlying
122    /// concrete type, not that of `dyn Any` itself.
123    ///
124    /// # Examples
125    ///
126    /// ```
127    /// use std::any::{Any, TypeId};
128    ///
129    /// fn is_string(s: &dyn Any) -> bool {
130    ///     TypeId::of::<String>() == s.type_id()
131    /// }
132    ///
133    /// assert_eq!(is_string(&0), false);
134    /// assert_eq!(is_string(&"cookie monster".to_string()), true);
135    /// ```
136    #[stable(feature = "get_type_id", since = "1.34.0")]
137    fn type_id(&self) -> TypeId;
138}
139
140#[stable(feature = "rust1", since = "1.0.0")]
141impl<T: 'static + ?Sized> Any for T {
142    fn type_id(&self) -> TypeId {
143        TypeId::of::<T>()
144    }
145}
146
147///////////////////////////////////////////////////////////////////////////////
148// Extension methods for Any trait objects.
149///////////////////////////////////////////////////////////////////////////////
150
151#[stable(feature = "rust1", since = "1.0.0")]
152impl fmt::Debug for dyn Any {
153    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
154        f.debug_struct("Any").finish_non_exhaustive()
155    }
156}
157
158// Ensure that the result of e.g., joining a thread can be printed and
159// hence used with `unwrap`. May eventually no longer be needed if
160// dispatch works with upcasting.
161#[stable(feature = "rust1", since = "1.0.0")]
162impl fmt::Debug for dyn Any + Send {
163    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
164        f.debug_struct("Any").finish_non_exhaustive()
165    }
166}
167
168#[stable(feature = "any_send_sync_methods", since = "1.28.0")]
169impl fmt::Debug for dyn Any + Send + Sync {
170    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
171        f.debug_struct("Any").finish_non_exhaustive()
172    }
173}
174
175impl dyn Any {
176    /// Returns `true` if the inner type is the same as `T`.
177    ///
178    /// # Examples
179    ///
180    /// ```
181    /// use std::any::Any;
182    ///
183    /// fn is_string(s: &dyn Any) {
184    ///     if s.is::<String>() {
185    ///         println!("It's a string!");
186    ///     } else {
187    ///         println!("Not a string...");
188    ///     }
189    /// }
190    ///
191    /// is_string(&0);
192    /// is_string(&"cookie monster".to_string());
193    /// ```
194    #[stable(feature = "rust1", since = "1.0.0")]
195    #[inline]
196    pub fn is<T: Any>(&self) -> bool {
197        // Get `TypeId` of the type this function is instantiated with.
198        let t = TypeId::of::<T>();
199
200        // Get `TypeId` of the type in the trait object (`self`).
201        let concrete = self.type_id();
202
203        // Compare both `TypeId`s on equality.
204        t == concrete
205    }
206
207    /// Returns some reference to the inner value if it is of type `T`, or
208    /// `None` if it isn't.
209    ///
210    /// # Examples
211    ///
212    /// ```
213    /// use std::any::Any;
214    ///
215    /// fn print_if_string(s: &dyn Any) {
216    ///     if let Some(string) = s.downcast_ref::<String>() {
217    ///         println!("It's a string({}): '{}'", string.len(), string);
218    ///     } else {
219    ///         println!("Not a string...");
220    ///     }
221    /// }
222    ///
223    /// print_if_string(&0);
224    /// print_if_string(&"cookie monster".to_string());
225    /// ```
226    #[stable(feature = "rust1", since = "1.0.0")]
227    #[inline]
228    pub fn downcast_ref<T: Any>(&self) -> Option<&T> {
229        if self.is::<T>() {
230            // SAFETY: just checked whether we are pointing to the correct type, and we can rely on
231            // that check for memory safety because we have implemented Any for all types; no other
232            // impls can exist as they would conflict with our impl.
233            unsafe { Some(self.downcast_unchecked_ref()) }
234        } else {
235            None
236        }
237    }
238
239    /// Returns some mutable reference to the inner value if it is of type `T`, or
240    /// `None` if it isn't.
241    ///
242    /// # Examples
243    ///
244    /// ```
245    /// use std::any::Any;
246    ///
247    /// fn modify_if_u32(s: &mut dyn Any) {
248    ///     if let Some(num) = s.downcast_mut::<u32>() {
249    ///         *num = 42;
250    ///     }
251    /// }
252    ///
253    /// let mut x = 10u32;
254    /// let mut s = "starlord".to_string();
255    ///
256    /// modify_if_u32(&mut x);
257    /// modify_if_u32(&mut s);
258    ///
259    /// assert_eq!(x, 42);
260    /// assert_eq!(&s, "starlord");
261    /// ```
262    #[stable(feature = "rust1", since = "1.0.0")]
263    #[inline]
264    pub fn downcast_mut<T: Any>(&mut self) -> Option<&mut T> {
265        if self.is::<T>() {
266            // SAFETY: just checked whether we are pointing to the correct type, and we can rely on
267            // that check for memory safety because we have implemented Any for all types; no other
268            // impls can exist as they would conflict with our impl.
269            unsafe { Some(self.downcast_unchecked_mut()) }
270        } else {
271            None
272        }
273    }
274
275    /// Returns a reference to the inner value as type `dyn T`.
276    ///
277    /// # Examples
278    ///
279    /// ```
280    /// #![feature(downcast_unchecked)]
281    ///
282    /// use std::any::Any;
283    ///
284    /// let x: Box<dyn Any> = Box::new(1_usize);
285    ///
286    /// unsafe {
287    ///     assert_eq!(*x.downcast_unchecked_ref::<usize>(), 1);
288    /// }
289    /// ```
290    ///
291    /// # Safety
292    ///
293    /// The contained value must be of type `T`. Calling this method
294    /// with the incorrect type is *undefined behavior*.
295    #[unstable(feature = "downcast_unchecked", issue = "90850")]
296    #[inline]
297    pub unsafe fn downcast_unchecked_ref<T: Any>(&self) -> &T {
298        debug_assert!(self.is::<T>());
299        // SAFETY: caller guarantees that T is the correct type
300        unsafe { &*(self as *const dyn Any as *const T) }
301    }
302
303    /// Returns a mutable reference to the inner value as type `dyn T`.
304    ///
305    /// # Examples
306    ///
307    /// ```
308    /// #![feature(downcast_unchecked)]
309    ///
310    /// use std::any::Any;
311    ///
312    /// let mut x: Box<dyn Any> = Box::new(1_usize);
313    ///
314    /// unsafe {
315    ///     *x.downcast_unchecked_mut::<usize>() += 1;
316    /// }
317    ///
318    /// assert_eq!(*x.downcast_ref::<usize>().unwrap(), 2);
319    /// ```
320    ///
321    /// # Safety
322    ///
323    /// The contained value must be of type `T`. Calling this method
324    /// with the incorrect type is *undefined behavior*.
325    #[unstable(feature = "downcast_unchecked", issue = "90850")]
326    #[inline]
327    pub unsafe fn downcast_unchecked_mut<T: Any>(&mut self) -> &mut T {
328        debug_assert!(self.is::<T>());
329        // SAFETY: caller guarantees that T is the correct type
330        unsafe { &mut *(self as *mut dyn Any as *mut T) }
331    }
332}
333
334impl dyn Any + Send {
335    /// Forwards to the method defined on the type `dyn Any`.
336    ///
337    /// # Examples
338    ///
339    /// ```
340    /// use std::any::Any;
341    ///
342    /// fn is_string(s: &(dyn Any + Send)) {
343    ///     if s.is::<String>() {
344    ///         println!("It's a string!");
345    ///     } else {
346    ///         println!("Not a string...");
347    ///     }
348    /// }
349    ///
350    /// is_string(&0);
351    /// is_string(&"cookie monster".to_string());
352    /// ```
353    #[stable(feature = "rust1", since = "1.0.0")]
354    #[inline]
355    pub fn is<T: Any>(&self) -> bool {
356        <dyn Any>::is::<T>(self)
357    }
358
359    /// Forwards to the method defined on the type `dyn Any`.
360    ///
361    /// # Examples
362    ///
363    /// ```
364    /// use std::any::Any;
365    ///
366    /// fn print_if_string(s: &(dyn Any + Send)) {
367    ///     if let Some(string) = s.downcast_ref::<String>() {
368    ///         println!("It's a string({}): '{}'", string.len(), string);
369    ///     } else {
370    ///         println!("Not a string...");
371    ///     }
372    /// }
373    ///
374    /// print_if_string(&0);
375    /// print_if_string(&"cookie monster".to_string());
376    /// ```
377    #[stable(feature = "rust1", since = "1.0.0")]
378    #[inline]
379    pub fn downcast_ref<T: Any>(&self) -> Option<&T> {
380        <dyn Any>::downcast_ref::<T>(self)
381    }
382
383    /// Forwards to the method defined on the type `dyn Any`.
384    ///
385    /// # Examples
386    ///
387    /// ```
388    /// use std::any::Any;
389    ///
390    /// fn modify_if_u32(s: &mut (dyn Any + Send)) {
391    ///     if let Some(num) = s.downcast_mut::<u32>() {
392    ///         *num = 42;
393    ///     }
394    /// }
395    ///
396    /// let mut x = 10u32;
397    /// let mut s = "starlord".to_string();
398    ///
399    /// modify_if_u32(&mut x);
400    /// modify_if_u32(&mut s);
401    ///
402    /// assert_eq!(x, 42);
403    /// assert_eq!(&s, "starlord");
404    /// ```
405    #[stable(feature = "rust1", since = "1.0.0")]
406    #[inline]
407    pub fn downcast_mut<T: Any>(&mut self) -> Option<&mut T> {
408        <dyn Any>::downcast_mut::<T>(self)
409    }
410
411    /// Forwards to the method defined on the type `dyn Any`.
412    ///
413    /// # Examples
414    ///
415    /// ```
416    /// #![feature(downcast_unchecked)]
417    ///
418    /// use std::any::Any;
419    ///
420    /// let x: Box<dyn Any> = Box::new(1_usize);
421    ///
422    /// unsafe {
423    ///     assert_eq!(*x.downcast_unchecked_ref::<usize>(), 1);
424    /// }
425    /// ```
426    ///
427    /// # Safety
428    ///
429    /// The contained value must be of type `T`. Calling this method
430    /// with the incorrect type is *undefined behavior*.
431    #[unstable(feature = "downcast_unchecked", issue = "90850")]
432    #[inline]
433    pub unsafe fn downcast_unchecked_ref<T: Any>(&self) -> &T {
434        // SAFETY: guaranteed by caller
435        unsafe { <dyn Any>::downcast_unchecked_ref::<T>(self) }
436    }
437
438    /// Forwards to the method defined on the type `dyn Any`.
439    ///
440    /// # Examples
441    ///
442    /// ```
443    /// #![feature(downcast_unchecked)]
444    ///
445    /// use std::any::Any;
446    ///
447    /// let mut x: Box<dyn Any> = Box::new(1_usize);
448    ///
449    /// unsafe {
450    ///     *x.downcast_unchecked_mut::<usize>() += 1;
451    /// }
452    ///
453    /// assert_eq!(*x.downcast_ref::<usize>().unwrap(), 2);
454    /// ```
455    ///
456    /// # Safety
457    ///
458    /// The contained value must be of type `T`. Calling this method
459    /// with the incorrect type is *undefined behavior*.
460    #[unstable(feature = "downcast_unchecked", issue = "90850")]
461    #[inline]
462    pub unsafe fn downcast_unchecked_mut<T: Any>(&mut self) -> &mut T {
463        // SAFETY: guaranteed by caller
464        unsafe { <dyn Any>::downcast_unchecked_mut::<T>(self) }
465    }
466}
467
468impl dyn Any + Send + Sync {
469    /// Forwards to the method defined on the type `Any`.
470    ///
471    /// # Examples
472    ///
473    /// ```
474    /// use std::any::Any;
475    ///
476    /// fn is_string(s: &(dyn Any + Send + Sync)) {
477    ///     if s.is::<String>() {
478    ///         println!("It's a string!");
479    ///     } else {
480    ///         println!("Not a string...");
481    ///     }
482    /// }
483    ///
484    /// is_string(&0);
485    /// is_string(&"cookie monster".to_string());
486    /// ```
487    #[stable(feature = "any_send_sync_methods", since = "1.28.0")]
488    #[inline]
489    pub fn is<T: Any>(&self) -> bool {
490        <dyn Any>::is::<T>(self)
491    }
492
493    /// Forwards to the method defined on the type `Any`.
494    ///
495    /// # Examples
496    ///
497    /// ```
498    /// use std::any::Any;
499    ///
500    /// fn print_if_string(s: &(dyn Any + Send + Sync)) {
501    ///     if let Some(string) = s.downcast_ref::<String>() {
502    ///         println!("It's a string({}): '{}'", string.len(), string);
503    ///     } else {
504    ///         println!("Not a string...");
505    ///     }
506    /// }
507    ///
508    /// print_if_string(&0);
509    /// print_if_string(&"cookie monster".to_string());
510    /// ```
511    #[stable(feature = "any_send_sync_methods", since = "1.28.0")]
512    #[inline]
513    pub fn downcast_ref<T: Any>(&self) -> Option<&T> {
514        <dyn Any>::downcast_ref::<T>(self)
515    }
516
517    /// Forwards to the method defined on the type `Any`.
518    ///
519    /// # Examples
520    ///
521    /// ```
522    /// use std::any::Any;
523    ///
524    /// fn modify_if_u32(s: &mut (dyn Any + Send + Sync)) {
525    ///     if let Some(num) = s.downcast_mut::<u32>() {
526    ///         *num = 42;
527    ///     }
528    /// }
529    ///
530    /// let mut x = 10u32;
531    /// let mut s = "starlord".to_string();
532    ///
533    /// modify_if_u32(&mut x);
534    /// modify_if_u32(&mut s);
535    ///
536    /// assert_eq!(x, 42);
537    /// assert_eq!(&s, "starlord");
538    /// ```
539    #[stable(feature = "any_send_sync_methods", since = "1.28.0")]
540    #[inline]
541    pub fn downcast_mut<T: Any>(&mut self) -> Option<&mut T> {
542        <dyn Any>::downcast_mut::<T>(self)
543    }
544
545    /// Forwards to the method defined on the type `Any`.
546    ///
547    /// # Examples
548    ///
549    /// ```
550    /// #![feature(downcast_unchecked)]
551    ///
552    /// use std::any::Any;
553    ///
554    /// let x: Box<dyn Any> = Box::new(1_usize);
555    ///
556    /// unsafe {
557    ///     assert_eq!(*x.downcast_unchecked_ref::<usize>(), 1);
558    /// }
559    /// ```
560    /// # Safety
561    ///
562    /// The contained value must be of type `T`. Calling this method
563    /// with the incorrect type is *undefined behavior*.
564    #[unstable(feature = "downcast_unchecked", issue = "90850")]
565    #[inline]
566    pub unsafe fn downcast_unchecked_ref<T: Any>(&self) -> &T {
567        // SAFETY: guaranteed by caller
568        unsafe { <dyn Any>::downcast_unchecked_ref::<T>(self) }
569    }
570
571    /// Forwards to the method defined on the type `Any`.
572    ///
573    /// # Examples
574    ///
575    /// ```
576    /// #![feature(downcast_unchecked)]
577    ///
578    /// use std::any::Any;
579    ///
580    /// let mut x: Box<dyn Any> = Box::new(1_usize);
581    ///
582    /// unsafe {
583    ///     *x.downcast_unchecked_mut::<usize>() += 1;
584    /// }
585    ///
586    /// assert_eq!(*x.downcast_ref::<usize>().unwrap(), 2);
587    /// ```
588    /// # Safety
589    ///
590    /// The contained value must be of type `T`. Calling this method
591    /// with the incorrect type is *undefined behavior*.
592    #[unstable(feature = "downcast_unchecked", issue = "90850")]
593    #[inline]
594    pub unsafe fn downcast_unchecked_mut<T: Any>(&mut self) -> &mut T {
595        // SAFETY: guaranteed by caller
596        unsafe { <dyn Any>::downcast_unchecked_mut::<T>(self) }
597    }
598}
599
600///////////////////////////////////////////////////////////////////////////////
601// TypeID and its methods
602///////////////////////////////////////////////////////////////////////////////
603
604/// A `TypeId` represents a globally unique identifier for a type.
605///
606/// Each `TypeId` is an opaque object which does not allow inspection of what's
607/// inside but does allow basic operations such as cloning, comparison,
608/// printing, and showing.
609///
610/// A `TypeId` is currently only available for types which ascribe to `'static`,
611/// but this limitation may be removed in the future.
612///
613/// While `TypeId` implements `Hash`, `PartialOrd`, and `Ord`, it is worth
614/// noting that the hashes and ordering will vary between Rust releases. Beware
615/// of relying on them inside of your code!
616///
617/// # Layout
618///
619/// Like other [`Rust`-representation][repr-rust] types, `TypeId`'s size and layout are unstable.
620/// In particular, this means that you cannot rely on the size and layout of `TypeId` remaining the
621/// same between Rust releases; they are subject to change without prior notice between Rust
622/// releases.
623///
624/// [repr-rust]: https://doc.rust-lang.org/reference/type-layout.html#r-layout.repr.rust.unspecified
625///
626/// # Danger of Improper Variance
627///
628/// You might think that subtyping is impossible between two static types,
629/// but this is false; there exists a static type with a static subtype.
630/// To wit, `fn(&str)`, which is short for `for<'any> fn(&'any str)`, and
631/// `fn(&'static str)`, are two distinct, static types, and yet,
632/// `fn(&str)` is a subtype of `fn(&'static str)`, since any value of type
633/// `fn(&str)` can be used where a value of type `fn(&'static str)` is needed.
634///
635/// This means that abstractions around `TypeId`, despite its
636/// `'static` bound on arguments, still need to worry about unnecessary
637/// and improper variance: it is advisable to strive for invariance
638/// first. The usability impact will be negligible, while the reduction
639/// in the risk of unsoundness will be most welcome.
640///
641/// ## Examples
642///
643/// Suppose `SubType` is a subtype of `SuperType`, that is,
644/// a value of type `SubType` can be used wherever
645/// a value of type `SuperType` is expected.
646/// Suppose also that `CoVar<T>` is a generic type, which is covariant over `T`
647/// (like many other types, including `PhantomData<T>` and `Vec<T>`).
648///
649/// Then, by covariance, `CoVar<SubType>` is a subtype of `CoVar<SuperType>`,
650/// that is, a value of type `CoVar<SubType>` can be used wherever
651/// a value of type `CoVar<SuperType>` is expected.
652///
653/// Then if `CoVar<SuperType>` relies on `TypeId::of::<SuperType>()` to uphold any invariants,
654/// those invariants may be broken because a value of type `CoVar<SuperType>` can be created
655/// without going through any of its methods, like so:
656/// ```
657/// type SubType = fn(&());
658/// type SuperType = fn(&'static ());
659/// type CoVar<T> = Vec<T>; // imagine something more complicated
660///
661/// let sub: CoVar<SubType> = CoVar::new();
662/// // we have a `CoVar<SuperType>` instance without
663/// // *ever* having called `CoVar::<SuperType>::new()`!
664/// let fake_super: CoVar<SuperType> = sub;
665/// ```
666///
667/// The following is an example program that tries to use `TypeId::of` to
668/// implement a generic type `Unique<T>` that guarantees unique instances for each `Unique<T>`,
669/// that is, and for each type `T` there can be at most one value of type `Unique<T>` at any time.
670///
671/// ```
672/// mod unique {
673///     use std::any::TypeId;
674///     use std::collections::BTreeSet;
675///     use std::marker::PhantomData;
676///     use std::sync::Mutex;
677///
678///     static ID_SET: Mutex<BTreeSet<TypeId>> = Mutex::new(BTreeSet::new());
679///
680///     // TypeId has only covariant uses, which makes Unique covariant over TypeAsId 🚨
681///     #[derive(Debug, PartialEq)]
682///     pub struct Unique<TypeAsId: 'static>(
683///         // private field prevents creation without `new` outside this module
684///         PhantomData<TypeAsId>,
685///     );
686///
687///     impl<TypeAsId: 'static> Unique<TypeAsId> {
688///         pub fn new() -> Option<Self> {
689///             let mut set = ID_SET.lock().unwrap();
690///             (set.insert(TypeId::of::<TypeAsId>())).then(|| Self(PhantomData))
691///         }
692///     }
693///
694///     impl<TypeAsId: 'static> Drop for Unique<TypeAsId> {
695///         fn drop(&mut self) {
696///             let mut set = ID_SET.lock().unwrap();
697///             (!set.remove(&TypeId::of::<TypeAsId>())).then(|| panic!("duplicity detected"));
698///         }
699///     }
700/// }
701///
702/// use unique::Unique;
703///
704/// // `OtherRing` is a subtype of `TheOneRing`. Both are 'static, and thus have a TypeId.
705/// type TheOneRing = fn(&'static ());
706/// type OtherRing = fn(&());
707///
708/// fn main() {
709///     let the_one_ring: Unique<TheOneRing> = Unique::new().unwrap();
710///     assert_eq!(Unique::<TheOneRing>::new(), None);
711///
712///     let other_ring: Unique<OtherRing> = Unique::new().unwrap();
713///     // Use that `Unique<OtherRing>` is a subtype of `Unique<TheOneRing>` 🚨
714///     let fake_one_ring: Unique<TheOneRing> = other_ring;
715///     assert_eq!(fake_one_ring, the_one_ring);
716///
717///     std::mem::forget(fake_one_ring);
718/// }
719/// ```
720#[derive(Copy, PartialOrd, Ord)]
721#[derive_const(Clone, Eq)]
722#[stable(feature = "rust1", since = "1.0.0")]
723#[lang = "type_id"]
724pub struct TypeId {
725    /// This needs to be an array of pointers, since there is provenance
726    /// in the first array field. This provenance knows exactly which type
727    /// the TypeId actually is, allowing CTFE and miri to operate based off it.
728    /// At runtime all the pointers in the array contain bits of the hash, making
729    /// the entire `TypeId` actually just be a `u128` hash of the type.
730    pub(crate) data: [*const (); 16 / size_of::<*const ()>()],
731}
732
733// SAFETY: the raw pointer is always an integer
734#[stable(feature = "rust1", since = "1.0.0")]
735unsafe impl Send for TypeId {}
736// SAFETY: the raw pointer is always an integer
737#[stable(feature = "rust1", since = "1.0.0")]
738unsafe impl Sync for TypeId {}
739
740#[stable(feature = "rust1", since = "1.0.0")]
741#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
742impl const PartialEq for TypeId {
743    #[inline]
744    fn eq(&self, other: &Self) -> bool {
745        #[cfg(miri)]
746        return crate::intrinsics::type_id_eq(*self, *other);
747        #[cfg(not(miri))]
748        {
749            let this = self;
750            crate::intrinsics::const_eval_select!(
751                @capture { this: &TypeId, other: &TypeId } -> bool:
752                if const {
753                    crate::intrinsics::type_id_eq(*this, *other)
754                } else {
755                    // Ideally we would just invoke `type_id_eq` unconditionally here,
756                    // but since we do not MIR inline intrinsics, because backends
757                    // may want to override them (and miri does!), MIR opts do not
758                    // clean up this call sufficiently for LLVM to turn repeated calls
759                    // of `TypeId` comparisons against one specific `TypeId` into
760                    // a lookup table.
761                    // SAFETY: We know that at runtime none of the bits have provenance and all bits
762                    // are initialized. So we can just convert the whole thing to a `u128` and compare that.
763                    unsafe {
764                        crate::mem::transmute::<_, u128>(*this) == crate::mem::transmute::<_, u128>(*other)
765                    }
766                }
767            )
768        }
769    }
770}
771
772impl TypeId {
773    /// Returns the `TypeId` of the generic type parameter.
774    ///
775    /// # Examples
776    ///
777    /// ```
778    /// use std::any::{Any, TypeId};
779    ///
780    /// fn is_string<T: ?Sized + Any>(_s: &T) -> bool {
781    ///     TypeId::of::<String>() == TypeId::of::<T>()
782    /// }
783    ///
784    /// assert_eq!(is_string(&0), false);
785    /// assert_eq!(is_string(&"cookie monster".to_string()), true);
786    /// ```
787    #[must_use]
788    #[stable(feature = "rust1", since = "1.0.0")]
789    #[rustc_const_stable(feature = "const_type_id", since = "1.91.0")]
790    pub const fn of<T: ?Sized + 'static>() -> TypeId {
791        const { intrinsics::type_id::<T>() }
792    }
793
794    /// Checks if the [TypeId] implements the trait. If it does it returns [TraitImpl] which can be used to build a fat pointer.
795    /// It can only be called at compile time. `self` must be the [TypeId] of a sized type or None will be returned.
796    ///
797    /// # Examples
798    ///
799    /// ```
800    /// #![feature(type_info)]
801    /// use std::any::{TypeId};
802    ///
803    /// pub trait Blah {}
804    /// impl Blah for u8 {}
805    ///
806    /// assert!(const { TypeId::of::<u8>().trait_info_of::<dyn Blah>() }.is_some());
807    /// assert!(const { TypeId::of::<u16>().trait_info_of::<dyn Blah>() }.is_none());
808    /// ```
809    #[unstable(feature = "type_info", issue = "146922")]
810    #[rustc_const_unstable(feature = "type_info", issue = "146922")]
811    pub const fn trait_info_of<
812        T: ptr::Pointee<Metadata = ptr::DynMetadata<T>> + ?Sized + 'static,
813    >(
814        self,
815    ) -> Option<TraitImpl<T>> {
816        // SAFETY: The vtable was obtained for `T`, so it is guaranteed to be `DynMetadata<T>`.
817        // The intrinsic can't infer this because it is designed to work with arbitrary TypeIds.
818        unsafe { transmute(self.trait_info_of_trait_type_id(const { TypeId::of::<T>() })) }
819    }
820
821    /// Checks if the [TypeId] implements the trait of `trait_represented_by_type_id`. If it does it returns [TraitImpl] which can be used to build a fat pointer.
822    /// It can only be called at compile time. `self` must be the [TypeId] of a sized type or None will be returned.
823    ///
824    /// # Examples
825    ///
826    /// ```
827    /// #![feature(type_info)]
828    /// use std::any::{TypeId};
829    ///
830    /// pub trait Blah {}
831    /// impl Blah for u8 {}
832    ///
833    /// assert!(const { TypeId::of::<u8>().trait_info_of_trait_type_id(TypeId::of::<dyn Blah>()) }.is_some());
834    /// assert!(const { TypeId::of::<u16>().trait_info_of_trait_type_id(TypeId::of::<dyn Blah>()) }.is_none());
835    /// ```
836    #[unstable(feature = "type_info", issue = "146922")]
837    #[rustc_const_unstable(feature = "type_info", issue = "146922")]
838    pub const fn trait_info_of_trait_type_id(
839        self,
840        trait_represented_by_type_id: TypeId,
841    ) -> Option<TraitImpl<*const ()>> {
842        if self.info().size.is_none() {
843            return None;
844        }
845
846        if matches!(trait_represented_by_type_id.info().kind, TypeKind::DynTrait(_))
847            && let Some(vtable) = type_id_vtable(self, trait_represented_by_type_id)
848        {
849            Some(TraitImpl { vtable })
850        } else {
851            None
852        }
853    }
854
855    fn as_u128(self) -> u128 {
856        let mut bytes = [0; 16];
857
858        // This is a provenance-stripping memcpy.
859        for (i, chunk) in self.data.iter().copied().enumerate() {
860            let chunk = chunk.addr().to_ne_bytes();
861            let start = i * chunk.len();
862            bytes[start..(start + chunk.len())].copy_from_slice(&chunk);
863        }
864        u128::from_ne_bytes(bytes)
865    }
866}
867
868#[stable(feature = "rust1", since = "1.0.0")]
869impl hash::Hash for TypeId {
870    #[inline]
871    fn hash<H: hash::Hasher>(&self, state: &mut H) {
872        // We only hash the lower 64 bits of our (128 bit) internal numeric ID,
873        // because:
874        // - The hashing algorithm which backs `TypeId` is expected to be
875        //   unbiased and high quality, meaning further mixing would be somewhat
876        //   redundant compared to choosing (the lower) 64 bits arbitrarily.
877        // - `Hasher::finish` returns a u64 anyway, so the extra entropy we'd
878        //   get from hashing the full value would probably not be useful
879        //   (especially given the previous point about the lower 64 bits being
880        //   high quality on their own).
881        // - It is correct to do so -- only hashing a subset of `self` is still
882        //   compatible with an `Eq` implementation that considers the entire
883        //   value, as ours does.
884        let data =
885        // SAFETY: The `offset` stays in-bounds, it just moves the pointer to the 2nd half of the `TypeId`.
886        // Only the first ptr-sized chunk ever has provenance, so that second half is always
887        // fine to read at integer type.
888            unsafe { crate::ptr::read_unaligned(self.data.as_ptr().cast::<u64>().offset(1)) };
889        data.hash(state);
890    }
891}
892
893#[stable(feature = "rust1", since = "1.0.0")]
894impl fmt::Debug for TypeId {
895    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> Result<(), fmt::Error> {
896        write!(f, "TypeId({:#034x})", self.as_u128())
897    }
898}
899
900/// Returns the name of a type as a string slice.
901///
902/// # Note
903///
904/// This is intended for diagnostic use. The exact contents and format of the
905/// string returned are not specified, other than being a best-effort
906/// description of the type. For example, amongst the strings
907/// that `type_name::<Option<String>>()` might return are `"Option<String>"` and
908/// `"std::option::Option<std::string::String>"`.
909///
910/// The returned string must not be considered to be a unique identifier of a
911/// type as multiple types may map to the same type name. Similarly, there is no
912/// guarantee that all parts of a type will appear in the returned string. In
913/// addition, the output may change between versions of the compiler. For
914/// example, lifetime specifiers were omitted in some earlier versions.
915///
916/// The current implementation uses the same infrastructure as compiler
917/// diagnostics and debuginfo, but this is not guaranteed.
918///
919/// # Examples
920///
921/// ```rust
922/// assert_eq!(
923///     std::any::type_name::<Option<String>>(),
924///     "core::option::Option<alloc::string::String>",
925/// );
926/// ```
927#[must_use]
928#[stable(feature = "type_name", since = "1.38.0")]
929#[rustc_const_unstable(feature = "const_type_name", issue = "63084")]
930pub const fn type_name<T: ?Sized>() -> &'static str {
931    const { intrinsics::type_name::<T>() }
932}
933
934/// Returns the type name of the pointed-to value as a string slice.
935///
936/// This is the same as `type_name::<T>()`, but can be used where the type of a
937/// variable is not easily available.
938///
939/// # Note
940///
941/// Like [`type_name`], this is intended for diagnostic use and the exact output is not
942/// guaranteed. It provides a best-effort description, but the output may change between
943/// versions of the compiler.
944///
945/// In short: use this for debugging, avoid using the output to affect program behavior. More
946/// information is available at [`type_name`].
947///
948/// Additionally, this function does not resolve trait objects. This means that
949/// `type_name_of_val(&7u32 as &dyn Debug)` may return `"dyn Debug"`, but will not return `"u32"`
950/// at this time.
951///
952/// # Examples
953///
954/// Prints the default integer and float types.
955///
956/// ```rust
957/// use std::any::type_name_of_val;
958///
959/// let s = "foo";
960/// let x: i32 = 1;
961/// let y: f32 = 1.0;
962///
963/// assert!(type_name_of_val(&s).contains("str"));
964/// assert!(type_name_of_val(&x).contains("i32"));
965/// assert!(type_name_of_val(&y).contains("f32"));
966/// ```
967#[must_use]
968#[stable(feature = "type_name_of_val", since = "1.76.0")]
969#[rustc_const_unstable(feature = "const_type_name", issue = "63084")]
970pub const fn type_name_of_val<T: ?Sized>(_val: &T) -> &'static str {
971    type_name::<T>()
972}
973
974/// Returns `Some(&U)` if `T` can be coerced to the trait object type `U`. Otherwise, it returns `None`.
975///
976/// # Compile-time failures
977/// Determining whether `T` can be coerced to the trait object type `U` requires compiler trait resolution.
978/// In some cases, that resolution can exceed the recursion limit,
979/// and compilation will fail instead of this function returning `None`.
980/// # Examples
981///
982/// ```rust
983/// #![feature(try_as_dyn)]
984///
985/// use core::any::try_as_dyn;
986///
987/// trait Animal {
988///     fn speak(&self) -> &'static str;
989/// }
990///
991/// struct Dog;
992/// impl Animal for Dog {
993///     fn speak(&self) -> &'static str { "woof" }
994/// }
995///
996/// struct Rock; // does not implement Animal
997///
998/// let dog = Dog;
999/// let rock = Rock;
1000///
1001/// let as_animal: Option<&dyn Animal> = try_as_dyn::<Dog, dyn Animal>(&dog);
1002/// assert_eq!(as_animal.unwrap().speak(), "woof");
1003///
1004/// let not_an_animal: Option<&dyn Animal> = try_as_dyn::<Rock, dyn Animal>(&rock);
1005/// assert!(not_an_animal.is_none());
1006/// ```
1007#[must_use]
1008#[unstable(feature = "try_as_dyn", issue = "144361")]
1009pub const fn try_as_dyn<
1010    T: Any + 'static,
1011    U: ptr::Pointee<Metadata = ptr::DynMetadata<U>> + ?Sized + 'static,
1012>(
1013    t: &T,
1014) -> Option<&U> {
1015    let vtable: Option<ptr::DynMetadata<U>> =
1016        const { TypeId::of::<T>().trait_info_of::<U>().as_ref().map(TraitImpl::get_vtable) };
1017    match vtable {
1018        Some(dyn_metadata) => {
1019            let pointer = ptr::from_raw_parts(t, dyn_metadata);
1020            // SAFETY: `t` is a reference to a type, so we know it is valid.
1021            // `dyn_metadata` is a vtable for T, implementing the trait of `U`.
1022            Some(unsafe { &*pointer })
1023        }
1024        None => None,
1025    }
1026}
1027
1028/// Returns `Some(&mut U)` if `T` can be coerced to the trait object type `U`. Otherwise, it returns `None`.
1029///
1030/// # Compile-time failures
1031/// Determining whether `T` can be coerced to the trait object type `U` requires compiler trait resolution.
1032/// In some cases, that resolution can exceed the recursion limit,
1033/// and compilation will fail instead of this function returning `None`.
1034/// # Examples
1035///
1036/// ```rust
1037/// #![feature(try_as_dyn)]
1038///
1039/// use core::any::try_as_dyn_mut;
1040///
1041/// trait Animal {
1042///     fn speak(&self) -> &'static str;
1043/// }
1044///
1045/// struct Dog;
1046/// impl Animal for Dog {
1047///     fn speak(&self) -> &'static str { "woof" }
1048/// }
1049///
1050/// struct Rock; // does not implement Animal
1051///
1052/// let mut dog = Dog;
1053/// let mut rock = Rock;
1054///
1055/// let as_animal: Option<&mut dyn Animal> = try_as_dyn_mut::<Dog, dyn Animal>(&mut dog);
1056/// assert_eq!(as_animal.unwrap().speak(), "woof");
1057///
1058/// let not_an_animal: Option<&mut dyn Animal> = try_as_dyn_mut::<Rock, dyn Animal>(&mut rock);
1059/// assert!(not_an_animal.is_none());
1060/// ```
1061#[must_use]
1062#[unstable(feature = "try_as_dyn", issue = "144361")]
1063pub const fn try_as_dyn_mut<
1064    T: Any + 'static,
1065    U: ptr::Pointee<Metadata = ptr::DynMetadata<U>> + ?Sized + 'static,
1066>(
1067    t: &mut T,
1068) -> Option<&mut U> {
1069    let vtable: Option<ptr::DynMetadata<U>> =
1070        const { TypeId::of::<T>().trait_info_of::<U>().as_ref().map(TraitImpl::get_vtable) };
1071    match vtable {
1072        Some(dyn_metadata) => {
1073            let pointer = ptr::from_raw_parts_mut(t, dyn_metadata);
1074            // SAFETY: `t` is a reference to a type, so we know it is valid.
1075            // `dyn_metadata` is a vtable for T, implementing the trait of `U`.
1076            Some(unsafe { &mut *pointer })
1077        }
1078        None => None,
1079    }
1080}
````