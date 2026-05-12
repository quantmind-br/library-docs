---
title: error.rs - source
url: https://doc.rust-lang.org/src/core/error.rs.html#137
source: crawler
fetched_at: 2026-05-06T21:32:53.213014597-03:00
rendered_js: false
word_count: 4283
summary: This document defines the Error trait in Rust, which establishes standard requirements for error types, including support for display, debug, and error chaining via source methods.
tags:
    - rust
    - error-handling
    - traits
    - error-trait
    - standard-library
    - debug
    - display
category: reference
---

## core/ error.rs

````rust
1#![doc = include_str!("error.md")]
2#![stable(feature = "error_in_core", since = "1.81.0")]
3
4use crate::any::TypeId;
5use crate::fmt::{self, Debug, Display, Formatter};
6
7/// `Error` is a trait representing the basic expectations for error values,
8/// i.e., values of type `E` in [`Result<T, E>`].
9///
10/// Errors must describe themselves through the [`Display`] and [`Debug`]
11/// traits. Error messages are typically concise lowercase sentences without
12/// trailing punctuation:
13///
14/// ```
15/// let err = "NaN".parse::<u32>().unwrap_err();
16/// assert_eq!(err.to_string(), "invalid digit found in string");
17/// ```
18///
19/// # Error source
20///
21/// Errors may provide cause information. [`Error::source()`] is generally
22/// used when errors cross "abstraction boundaries". If one module must report
23/// an error that is caused by an error from a lower-level module, it can allow
24/// accessing that error via `Error::source()`. This makes it possible for the
25/// high-level module to provide its own errors while also revealing some of the
26/// implementation for debugging.
27///
28/// In error types that wrap an underlying error, the underlying error
29/// should be either returned by the outer error's `Error::source()`, or rendered
30/// by the outer error's `Display` implementation, but not both.
31///
32/// # Example
33///
34/// Implementing the `Error` trait only requires that `Debug` and `Display` are implemented too.
35///
36/// ```
37/// use std::error::Error;
38/// use std::fmt;
39/// use std::path::PathBuf;
40///
41/// #[derive(Debug)]
42/// struct ReadConfigError {
43///     path: PathBuf
44/// }
45///
46/// impl fmt::Display for ReadConfigError {
47///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
48///         let path = self.path.display();
49///         write!(f, "unable to read configuration at {path}")
50///     }
51/// }
52///
53/// impl Error for ReadConfigError {}
54/// ```
55#[stable(feature = "rust1", since = "1.0.0")]
56#[rustc_diagnostic_item = "Error"]
57#[rustc_has_incoherent_inherent_impls]
58#[allow(multiple_supertrait_upcastable)]
59pub trait Error: Debug + Display {
60    /// Returns the lower-level source of this error, if any.
61    ///
62    /// # Examples
63    ///
64    /// ```
65    /// use std::error::Error;
66    /// use std::fmt;
67    ///
68    /// #[derive(Debug)]
69    /// struct SuperError {
70    ///     source: SuperErrorSideKick,
71    /// }
72    ///
73    /// impl fmt::Display for SuperError {
74    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
75    ///         write!(f, "SuperError is here!")
76    ///     }
77    /// }
78    ///
79    /// impl Error for SuperError {
80    ///     fn source(&self) -> Option<&(dyn Error + 'static)> {
81    ///         Some(&self.source)
82    ///     }
83    /// }
84    ///
85    /// #[derive(Debug)]
86    /// struct SuperErrorSideKick;
87    ///
88    /// impl fmt::Display for SuperErrorSideKick {
89    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
90    ///         write!(f, "SuperErrorSideKick is here!")
91    ///     }
92    /// }
93    ///
94    /// impl Error for SuperErrorSideKick {}
95    ///
96    /// fn get_super_error() -> Result<(), SuperError> {
97    ///     Err(SuperError { source: SuperErrorSideKick })
98    /// }
99    ///
100    /// fn main() {
101    ///     match get_super_error() {
102    ///         Err(e) => {
103    ///             println!("Error: {e}");
104    ///             println!("Caused by: {}", e.source().unwrap());
105    ///         }
106    ///         _ => println!("No error"),
107    ///     }
108    /// }
109    /// ```
110    #[stable(feature = "error_source", since = "1.30.0")]
111    fn source(&self) -> Option<&(dyn Error + 'static)> {
112        None
113    }
114
115    /// Gets the `TypeId` of `self`.
116    #[doc(hidden)]
117    #[unstable(
118        feature = "error_type_id",
119        reason = "this is memory-unsafe to override in user code",
120        issue = "60784"
121    )]
122    fn type_id(&self, _: private::Internal) -> TypeId
123    where
124        Self: 'static,
125    {
126        TypeId::of::<Self>()
127    }
128
129    /// ```
130    /// if let Err(e) = "xc".parse::<u32>() {
131    ///     // Print `e` itself, no need for description().
132    ///     eprintln!("Error: {e}");
133    /// }
134    /// ```
135    #[stable(feature = "rust1", since = "1.0.0")]
136    #[deprecated(since = "1.42.0", note = "use the Display impl or to_string()")]
137    fn description(&self) -> &str {
138        "description() is deprecated; use Display"
139    }
140
141    #[stable(feature = "rust1", since = "1.0.0")]
142    #[deprecated(
143        since = "1.33.0",
144        note = "replaced by Error::source, which can support downcasting"
145    )]
146    #[allow(missing_docs)]
147    fn cause(&self) -> Option<&dyn Error> {
148        self.source()
149    }
150
151    /// Provides type-based access to context intended for error reports.
152    ///
153    /// Used in conjunction with [`Request::provide_value`] and [`Request::provide_ref`] to extract
154    /// references to member variables from `dyn Error` trait objects.
155    ///
156    /// # Example
157    ///
158    /// ```rust
159    /// #![feature(error_generic_member_access)]
160    /// use core::fmt;
161    /// use core::error::{request_ref, Request};
162    ///
163    /// #[derive(Debug)]
164    /// enum MyLittleTeaPot {
165    ///     Empty,
166    /// }
167    ///
168    /// #[derive(Debug)]
169    /// struct MyBacktrace {
170    ///     // ...
171    /// }
172    ///
173    /// impl MyBacktrace {
174    ///     fn new() -> MyBacktrace {
175    ///         // ...
176    ///         # MyBacktrace {}
177    ///     }
178    /// }
179    ///
180    /// #[derive(Debug)]
181    /// struct Error {
182    ///     backtrace: MyBacktrace,
183    /// }
184    ///
185    /// impl fmt::Display for Error {
186    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
187    ///         write!(f, "Example Error")
188    ///     }
189    /// }
190    ///
191    /// impl std::error::Error for Error {
192    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
193    ///         request
194    ///             .provide_ref::<MyBacktrace>(&self.backtrace);
195    ///     }
196    /// }
197    ///
198    /// fn main() {
199    ///     let backtrace = MyBacktrace::new();
200    ///     let error = Error { backtrace };
201    ///     let dyn_error = &error as &dyn std::error::Error;
202    ///     let backtrace_ref = request_ref::<MyBacktrace>(dyn_error).unwrap();
203    ///
204    ///     assert!(core::ptr::eq(&error.backtrace, backtrace_ref));
205    ///     assert!(request_ref::<MyLittleTeaPot>(dyn_error).is_none());
206    /// }
207    /// ```
208    ///
209    /// # Delegating Impls
210    ///
211    /// <div class="warning">
212    ///
213    /// **Warning**: We recommend implementors avoid delegating implementations of `provide` to
214    /// source error implementations.
215    ///
216    /// </div>
217    ///
218    /// This method should expose context from the current piece of the source chain only, not from
219    /// sources that are exposed in the chain of sources. Delegating `provide` implementations cause
220    /// the same context to be provided by multiple errors in the chain of sources which can cause
221    /// unintended duplication of information in error reports or require heuristics to deduplicate.
222    ///
223    /// In other words, the following implementation pattern for `provide` is discouraged and should
224    /// not be used for [`Error`] types exposed in public APIs to third parties.
225    ///
226    /// ```rust
227    /// # #![feature(error_generic_member_access)]
228    /// # use core::fmt;
229    /// # use core::error::Request;
230    /// # #[derive(Debug)]
231    /// struct MyError {
232    ///     source: Error,
233    /// }
234    /// # #[derive(Debug)]
235    /// # struct Error;
236    /// # impl fmt::Display for Error {
237    /// #     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
238    /// #         write!(f, "Example Source Error")
239    /// #     }
240    /// # }
241    /// # impl fmt::Display for MyError {
242    /// #     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
243    /// #         write!(f, "Example Error")
244    /// #     }
245    /// # }
246    /// # impl std::error::Error for Error { }
247    ///
248    /// impl std::error::Error for MyError {
249    ///     fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
250    ///         Some(&self.source)
251    ///     }
252    ///
253    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
254    ///         self.source.provide(request) // <--- Discouraged
255    ///     }
256    /// }
257    /// ```
258    #[unstable(feature = "error_generic_member_access", issue = "99301")]
259    #[allow(unused_variables)]
260    fn provide<'a>(&'a self, request: &mut Request<'a>) {}
261}
262
263mod private {
264    // This is a hack to prevent `type_id` from being overridden by `Error`
265    // implementations, since that can enable unsound downcasting.
266    #[unstable(feature = "error_type_id", issue = "60784")]
267    #[derive(Debug)]
268    pub struct Internal;
269}
270
271#[unstable(feature = "never_type", issue = "35121")]
272impl Error for ! {}
273
274// Copied from `any.rs`.
275impl dyn Error + 'static {
276    /// Returns `true` if the inner type is the same as `T`.
277    #[stable(feature = "error_downcast", since = "1.3.0")]
278    #[inline]
279    pub fn is<T: Error + 'static>(&self) -> bool {
280        // Get `TypeId` of the type this function is instantiated with.
281        let t = TypeId::of::<T>();
282
283        // Get `TypeId` of the type in the trait object (`self`).
284        let concrete = self.type_id(private::Internal);
285
286        // Compare both `TypeId`s on equality.
287        t == concrete
288    }
289
290    /// Returns some reference to the inner value if it is of type `T`, or
291    /// `None` if it isn't.
292    #[stable(feature = "error_downcast", since = "1.3.0")]
293    #[inline]
294    pub fn downcast_ref<T: Error + 'static>(&self) -> Option<&T> {
295        if self.is::<T>() {
296            // SAFETY: `is` ensures this type cast is correct
297            unsafe { Some(&*(self as *const dyn Error as *const T)) }
298        } else {
299            None
300        }
301    }
302
303    /// Returns some mutable reference to the inner value if it is of type `T`, or
304    /// `None` if it isn't.
305    #[stable(feature = "error_downcast", since = "1.3.0")]
306    #[inline]
307    pub fn downcast_mut<T: Error + 'static>(&mut self) -> Option<&mut T> {
308        if self.is::<T>() {
309            // SAFETY: `is` ensures this type cast is correct
310            unsafe { Some(&mut *(self as *mut dyn Error as *mut T)) }
311        } else {
312            None
313        }
314    }
315}
316
317impl dyn Error + 'static + Send {
318    /// Forwards to the method defined on the type `dyn Error`.
319    #[stable(feature = "error_downcast", since = "1.3.0")]
320    #[inline]
321    pub fn is<T: Error + 'static>(&self) -> bool {
322        <dyn Error + 'static>::is::<T>(self)
323    }
324
325    /// Forwards to the method defined on the type `dyn Error`.
326    #[stable(feature = "error_downcast", since = "1.3.0")]
327    #[inline]
328    pub fn downcast_ref<T: Error + 'static>(&self) -> Option<&T> {
329        <dyn Error + 'static>::downcast_ref::<T>(self)
330    }
331
332    /// Forwards to the method defined on the type `dyn Error`.
333    #[stable(feature = "error_downcast", since = "1.3.0")]
334    #[inline]
335    pub fn downcast_mut<T: Error + 'static>(&mut self) -> Option<&mut T> {
336        <dyn Error + 'static>::downcast_mut::<T>(self)
337    }
338}
339
340impl dyn Error + 'static + Send + Sync {
341    /// Forwards to the method defined on the type `dyn Error`.
342    #[stable(feature = "error_downcast", since = "1.3.0")]
343    #[inline]
344    pub fn is<T: Error + 'static>(&self) -> bool {
345        <dyn Error + 'static>::is::<T>(self)
346    }
347
348    /// Forwards to the method defined on the type `dyn Error`.
349    #[stable(feature = "error_downcast", since = "1.3.0")]
350    #[inline]
351    pub fn downcast_ref<T: Error + 'static>(&self) -> Option<&T> {
352        <dyn Error + 'static>::downcast_ref::<T>(self)
353    }
354
355    /// Forwards to the method defined on the type `dyn Error`.
356    #[stable(feature = "error_downcast", since = "1.3.0")]
357    #[inline]
358    pub fn downcast_mut<T: Error + 'static>(&mut self) -> Option<&mut T> {
359        <dyn Error + 'static>::downcast_mut::<T>(self)
360    }
361}
362
363impl dyn Error {
364    /// Returns an iterator starting with the current error and continuing with
365    /// recursively calling [`Error::source`].
366    ///
367    /// If you want to omit the current error and only use its sources,
368    /// use `skip(1)`.
369    ///
370    /// # Examples
371    ///
372    /// ```
373    /// #![feature(error_iter)]
374    /// use std::error::Error;
375    /// use std::fmt;
376    ///
377    /// #[derive(Debug)]
378    /// struct A;
379    ///
380    /// #[derive(Debug)]
381    /// struct B(Option<Box<dyn Error + 'static>>);
382    ///
383    /// impl fmt::Display for A {
384    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
385    ///         write!(f, "A")
386    ///     }
387    /// }
388    ///
389    /// impl fmt::Display for B {
390    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
391    ///         write!(f, "B")
392    ///     }
393    /// }
394    ///
395    /// impl Error for A {}
396    ///
397    /// impl Error for B {
398    ///     fn source(&self) -> Option<&(dyn Error + 'static)> {
399    ///         self.0.as_ref().map(|e| e.as_ref())
400    ///     }
401    /// }
402    ///
403    /// let b = B(Some(Box::new(A)));
404    ///
405    /// // let err : Box<Error> = b.into(); // or
406    /// let err = &b as &dyn Error;
407    ///
408    /// let mut iter = err.sources();
409    ///
410    /// assert_eq!("B".to_string(), iter.next().unwrap().to_string());
411    /// assert_eq!("A".to_string(), iter.next().unwrap().to_string());
412    /// assert!(iter.next().is_none());
413    /// assert!(iter.next().is_none());
414    /// ```
415    #[unstable(feature = "error_iter", issue = "58520")]
416    #[inline]
417    pub fn sources(&self) -> Source<'_> {
418        // You may think this method would be better in the `Error` trait, and you'd be right.
419        // Unfortunately that doesn't work, not because of the dyn-incompatibility rules but
420        // because we save a reference to `self` in `Source`s below as a trait object.
421        // If this method was declared in `Error`, then `self` would have the type `&T` where
422        // `T` is some concrete type which implements `Error`. We would need to coerce `self`
423        // to have type `&dyn Error`, but that requires that `Self` has a known size
424        // (i.e., `Self: Sized`). We can't put that bound on `Error` since that would forbid
425        // `Error` trait objects, and we can't put that bound on the method because that means
426        // the method can't be called on trait objects (we'd also need the `'static` bound,
427        // but that isn't allowed because methods with bounds on `Self` other than `Sized` are
428        // dyn-incompatible). Requiring an `Unsize` bound is not backwards compatible.
429
430        Source { current: Some(self) }
431    }
432}
433
434/// Requests a value of type `T` from the given `impl Error`.
435///
436/// # Examples
437///
438/// Get a string value from an error.
439///
440/// ```rust
441/// #![feature(error_generic_member_access)]
442/// use std::error::Error;
443/// use core::error::request_value;
444///
445/// fn get_string(err: &impl Error) -> String {
446///     request_value::<String>(err).unwrap()
447/// }
448/// ```
449#[unstable(feature = "error_generic_member_access", issue = "99301")]
450pub fn request_value<'a, T>(err: &'a (impl Error + ?Sized)) -> Option<T>
451where
452    T: 'static,
453{
454    request_by_type_tag::<'a, tags::Value<T>>(err)
455}
456
457/// Requests a reference of type `T` from the given `impl Error`.
458///
459/// # Examples
460///
461/// Get a string reference from an error.
462///
463/// ```rust
464/// #![feature(error_generic_member_access)]
465/// use core::error::Error;
466/// use core::error::request_ref;
467///
468/// fn get_str(err: &impl Error) -> &str {
469///     request_ref::<str>(err).unwrap()
470/// }
471/// ```
472#[unstable(feature = "error_generic_member_access", issue = "99301")]
473pub fn request_ref<'a, T>(err: &'a (impl Error + ?Sized)) -> Option<&'a T>
474where
475    T: 'static + ?Sized,
476{
477    request_by_type_tag::<'a, tags::Ref<tags::MaybeSizedValue<T>>>(err)
478}
479
480/// Request a specific value by tag from the `Error`.
481fn request_by_type_tag<'a, I>(err: &'a (impl Error + ?Sized)) -> Option<I::Reified>
482where
483    I: tags::Type<'a>,
484{
485    let mut tagged = Tagged { tag_id: TypeId::of::<I>(), value: TaggedOption::<'a, I>(None) };
486    err.provide(tagged.as_request());
487    tagged.value.0
488}
489
490///////////////////////////////////////////////////////////////////////////////
491// Request and its methods
492///////////////////////////////////////////////////////////////////////////////
493
494/// `Request` supports generic, type-driven access to data. Its use is currently restricted to the
495/// standard library in cases where trait authors wish to allow trait implementors to share generic
496/// information across trait boundaries. The motivating and prototypical use case is
497/// `core::error::Error` which would otherwise require a method per concrete type (eg.
498/// `std::backtrace::Backtrace` instance that implementors want to expose to users).
499///
500/// # Data flow
501///
502/// To describe the intended data flow for Request objects, let's consider two conceptual users
503/// separated by API boundaries:
504///
505/// * Consumer - the consumer requests objects using a Request instance; eg a crate that offers
506///   fancy `Error`/`Result` reporting to users wants to request a Backtrace from a given `dyn Error`.
507///
508/// * Producer - the producer provides objects when requested via Request; eg. a library with an
509///   an `Error` implementation that automatically captures backtraces at the time instances are
510///   created.
511///
512/// The consumer only needs to know where to submit their request and are expected to handle the
513/// request not being fulfilled by the use of `Option<T>` in the responses offered by the producer.
514///
515/// * A Producer initializes the value of one of its fields of a specific type. (or is otherwise
516///   prepared to generate a value requested). eg, `backtrace::Backtrace` or
517///   `std::backtrace::Backtrace`
518/// * A Consumer requests an object of a specific type (say `std::backtrace::Backtrace`). In the
519///   case of a `dyn Error` trait object (the Producer), there are functions called `request_ref` and
520///   `request_value` to simplify obtaining an `Option<T>` for a given type.
521/// * The Producer, when requested, populates the given Request object which is given as a mutable
522///   reference.
523/// * The Consumer extracts a value or reference to the requested type from the `Request` object
524///   wrapped in an `Option<T>`; in the case of `dyn Error` the aforementioned `request_ref` and `
525///   request_value` methods mean that `dyn Error` users don't have to deal with the `Request` type at
526///   all (but `Error` implementors do). The `None` case of the `Option` suggests only that the
527///   Producer cannot currently offer an instance of the requested type, not it can't or never will.
528///
529/// # Examples
530///
531/// The best way to demonstrate this is using an example implementation of `Error`'s `provide` trait
532/// method:
533///
534/// ```
535/// #![feature(error_generic_member_access)]
536/// use core::fmt;
537/// use core::error::Request;
538/// use core::error::request_ref;
539///
540/// #[derive(Debug)]
541/// enum MyLittleTeaPot {
542///     Empty,
543/// }
544///
545/// #[derive(Debug)]
546/// struct MyBacktrace {
547///     // ...
548/// }
549///
550/// impl MyBacktrace {
551///     fn new() -> MyBacktrace {
552///         // ...
553///         # MyBacktrace {}
554///     }
555/// }
556///
557/// #[derive(Debug)]
558/// struct Error {
559///     backtrace: MyBacktrace,
560/// }
561///
562/// impl fmt::Display for Error {
563///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
564///         write!(f, "Example Error")
565///     }
566/// }
567///
568/// impl std::error::Error for Error {
569///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
570///         request
571///             .provide_ref::<MyBacktrace>(&self.backtrace);
572///     }
573/// }
574///
575/// fn main() {
576///     let backtrace = MyBacktrace::new();
577///     let error = Error { backtrace };
578///     let dyn_error = &error as &dyn std::error::Error;
579///     let backtrace_ref = request_ref::<MyBacktrace>(dyn_error).unwrap();
580///
581///     assert!(core::ptr::eq(&error.backtrace, backtrace_ref));
582///     assert!(request_ref::<MyLittleTeaPot>(dyn_error).is_none());
583/// }
584/// ```
585///
586#[unstable(feature = "error_generic_member_access", issue = "99301")]
587#[repr(transparent)]
588pub struct Request<'a>(Tagged<dyn Erased<'a> + 'a>);
589
590impl<'a> Request<'a> {
591    /// Provides a value or other type with only static lifetimes.
592    ///
593    /// # Examples
594    ///
595    /// Provides an `u8`.
596    ///
597    /// ```rust
598    /// #![feature(error_generic_member_access)]
599    ///
600    /// use core::error::Request;
601    ///
602    /// #[derive(Debug)]
603    /// struct SomeConcreteType { field: u8 }
604    ///
605    /// impl std::fmt::Display for SomeConcreteType {
606    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
607    ///         write!(f, "{} failed", self.field)
608    ///     }
609    /// }
610    ///
611    /// impl std::error::Error for SomeConcreteType {
612    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
613    ///         request.provide_value::<u8>(self.field);
614    ///     }
615    /// }
616    /// ```
617    #[unstable(feature = "error_generic_member_access", issue = "99301")]
618    pub fn provide_value<T>(&mut self, value: T) -> &mut Self
619    where
620        T: 'static,
621    {
622        self.provide::<tags::Value<T>>(value)
623    }
624
625    /// Provides a value or other type with only static lifetimes computed using a closure.
626    ///
627    /// # Examples
628    ///
629    /// Provides a `String` by cloning.
630    ///
631    /// ```rust
632    /// #![feature(error_generic_member_access)]
633    ///
634    /// use core::error::Request;
635    ///
636    /// #[derive(Debug)]
637    /// struct SomeConcreteType { field: String }
638    ///
639    /// impl std::fmt::Display for SomeConcreteType {
640    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
641    ///         write!(f, "{} failed", self.field)
642    ///     }
643    /// }
644    ///
645    /// impl std::error::Error for SomeConcreteType {
646    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
647    ///         request.provide_value_with::<String>(|| self.field.clone());
648    ///     }
649    /// }
650    /// ```
651    #[unstable(feature = "error_generic_member_access", issue = "99301")]
652    pub fn provide_value_with<T>(&mut self, fulfil: impl FnOnce() -> T) -> &mut Self
653    where
654        T: 'static,
655    {
656        self.provide_with::<tags::Value<T>>(fulfil)
657    }
658
659    /// Provides a reference. The referee type must be bounded by `'static`,
660    /// but may be unsized.
661    ///
662    /// # Examples
663    ///
664    /// Provides a reference to a field as a `&str`.
665    ///
666    /// ```rust
667    /// #![feature(error_generic_member_access)]
668    ///
669    /// use core::error::Request;
670    ///
671    /// #[derive(Debug)]
672    /// struct SomeConcreteType { field: String }
673    ///
674    /// impl std::fmt::Display for SomeConcreteType {
675    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
676    ///         write!(f, "{} failed", self.field)
677    ///     }
678    /// }
679    ///
680    /// impl std::error::Error for SomeConcreteType {
681    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
682    ///         request.provide_ref::<str>(&self.field);
683    ///     }
684    /// }
685    /// ```
686    #[unstable(feature = "error_generic_member_access", issue = "99301")]
687    pub fn provide_ref<T: ?Sized + 'static>(&mut self, value: &'a T) -> &mut Self {
688        self.provide::<tags::Ref<tags::MaybeSizedValue<T>>>(value)
689    }
690
691    /// Provides a reference computed using a closure. The referee type
692    /// must be bounded by `'static`, but may be unsized.
693    ///
694    /// # Examples
695    ///
696    /// Provides a reference to a field as a `&str`.
697    ///
698    /// ```rust
699    /// #![feature(error_generic_member_access)]
700    ///
701    /// use core::error::Request;
702    ///
703    /// #[derive(Debug)]
704    /// struct SomeConcreteType { business: String, party: String }
705    /// fn today_is_a_weekday() -> bool { true }
706    ///
707    /// impl std::fmt::Display for SomeConcreteType {
708    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
709    ///         write!(f, "{} failed", self.business)
710    ///     }
711    /// }
712    ///
713    /// impl std::error::Error for SomeConcreteType {
714    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
715    ///         request.provide_ref_with::<str>(|| {
716    ///             if today_is_a_weekday() {
717    ///                 &self.business
718    ///             } else {
719    ///                 &self.party
720    ///             }
721    ///         });
722    ///     }
723    /// }
724    /// ```
725    #[unstable(feature = "error_generic_member_access", issue = "99301")]
726    pub fn provide_ref_with<T: ?Sized + 'static>(
727        &mut self,
728        fulfil: impl FnOnce() -> &'a T,
729    ) -> &mut Self {
730        self.provide_with::<tags::Ref<tags::MaybeSizedValue<T>>>(fulfil)
731    }
732
733    /// Provides a value with the given `Type` tag.
734    fn provide<I>(&mut self, value: I::Reified) -> &mut Self
735    where
736        I: tags::Type<'a>,
737    {
738        if let Some(res @ TaggedOption(None)) = self.0.downcast_mut::<I>() {
739            res.0 = Some(value);
740        }
741        self
742    }
743
744    /// Provides a value with the given `Type` tag, using a closure to prevent unnecessary work.
745    fn provide_with<I>(&mut self, fulfil: impl FnOnce() -> I::Reified) -> &mut Self
746    where
747        I: tags::Type<'a>,
748    {
749        if let Some(res @ TaggedOption(None)) = self.0.downcast_mut::<I>() {
750            res.0 = Some(fulfil());
751        }
752        self
753    }
754
755    /// Checks if the `Request` would be satisfied if provided with a
756    /// value of the specified type. If the type does not match or has
757    /// already been provided, returns false.
758    ///
759    /// # Examples
760    ///
761    /// Checks if a `u8` still needs to be provided and then provides
762    /// it.
763    ///
764    /// ```rust
765    /// #![feature(error_generic_member_access)]
766    ///
767    /// use core::error::Request;
768    /// use core::error::request_value;
769    ///
770    /// #[derive(Debug)]
771    /// struct Parent(Option<u8>);
772    ///
773    /// impl std::fmt::Display for Parent {
774    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
775    ///         write!(f, "a parent failed")
776    ///     }
777    /// }
778    ///
779    /// impl std::error::Error for Parent {
780    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
781    ///         if let Some(v) = self.0 {
782    ///             request.provide_value::<u8>(v);
783    ///         }
784    ///     }
785    /// }
786    ///
787    /// #[derive(Debug)]
788    /// struct Child {
789    ///     parent: Parent,
790    /// }
791    ///
792    /// impl Child {
793    ///     // Pretend that this takes a lot of resources to evaluate.
794    ///     fn an_expensive_computation(&self) -> Option<u8> {
795    ///         Some(99)
796    ///     }
797    /// }
798    ///
799    /// impl std::fmt::Display for Child {
800    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
801    ///         write!(f, "child failed: \n  because of parent: {}", self.parent)
802    ///     }
803    /// }
804    ///
805    /// impl std::error::Error for Child {
806    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
807    ///         // In general, we don't know if this call will provide
808    ///         // an `u8` value or not...
809    ///         self.parent.provide(request);
810    ///
811    ///         // ...so we check to see if the `u8` is needed before
812    ///         // we run our expensive computation.
813    ///         if request.would_be_satisfied_by_value_of::<u8>() {
814    ///             if let Some(v) = self.an_expensive_computation() {
815    ///                 request.provide_value::<u8>(v);
816    ///             }
817    ///         }
818    ///
819    ///         // The request will be satisfied now, regardless of if
820    ///         // the parent provided the value or we did.
821    ///         assert!(!request.would_be_satisfied_by_value_of::<u8>());
822    ///     }
823    /// }
824    ///
825    /// let parent = Parent(Some(42));
826    /// let child = Child { parent };
827    /// assert_eq!(Some(42), request_value::<u8>(&child));
828    ///
829    /// let parent = Parent(None);
830    /// let child = Child { parent };
831    /// assert_eq!(Some(99), request_value::<u8>(&child));
832    ///
833    /// ```
834    #[unstable(feature = "error_generic_member_access", issue = "99301")]
835    pub fn would_be_satisfied_by_value_of<T>(&self) -> bool
836    where
837        T: 'static,
838    {
839        self.would_be_satisfied_by::<tags::Value<T>>()
840    }
841
842    /// Checks if the `Request` would be satisfied if provided with a
843    /// reference to a value of the specified type.
844    ///
845    /// If the type does not match or has already been provided, returns false.
846    ///
847    /// # Examples
848    ///
849    /// Checks if a `&str` still needs to be provided and then provides
850    /// it.
851    ///
852    /// ```rust
853    /// #![feature(error_generic_member_access)]
854    ///
855    /// use core::error::Request;
856    /// use core::error::request_ref;
857    ///
858    /// #[derive(Debug)]
859    /// struct Parent(Option<String>);
860    ///
861    /// impl std::fmt::Display for Parent {
862    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
863    ///         write!(f, "a parent failed")
864    ///     }
865    /// }
866    ///
867    /// impl std::error::Error for Parent {
868    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
869    ///         if let Some(v) = &self.0 {
870    ///             request.provide_ref::<str>(v);
871    ///         }
872    ///     }
873    /// }
874    ///
875    /// #[derive(Debug)]
876    /// struct Child {
877    ///     parent: Parent,
878    ///     name: String,
879    /// }
880    ///
881    /// impl Child {
882    ///     // Pretend that this takes a lot of resources to evaluate.
883    ///     fn an_expensive_computation(&self) -> Option<&str> {
884    ///         Some(&self.name)
885    ///     }
886    /// }
887    ///
888    /// impl std::fmt::Display for Child {
889    ///     fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
890    ///         write!(f, "{} failed: \n  {}", self.name, self.parent)
891    ///     }
892    /// }
893    ///
894    /// impl std::error::Error for Child {
895    ///     fn provide<'a>(&'a self, request: &mut Request<'a>) {
896    ///         // In general, we don't know if this call will provide
897    ///         // a `str` reference or not...
898    ///         self.parent.provide(request);
899    ///
900    ///         // ...so we check to see if the `&str` is needed before
901    ///         // we run our expensive computation.
902    ///         if request.would_be_satisfied_by_ref_of::<str>() {
903    ///             if let Some(v) = self.an_expensive_computation() {
904    ///                 request.provide_ref::<str>(v);
905    ///             }
906    ///         }
907    ///
908    ///         // The request will be satisfied now, regardless of if
909    ///         // the parent provided the reference or we did.
910    ///         assert!(!request.would_be_satisfied_by_ref_of::<str>());
911    ///     }
912    /// }
913    ///
914    /// let parent = Parent(Some("parent".into()));
915    /// let child = Child { parent, name: "child".into() };
916    /// assert_eq!(Some("parent"), request_ref::<str>(&child));
917    ///
918    /// let parent = Parent(None);
919    /// let child = Child { parent, name: "child".into() };
920    /// assert_eq!(Some("child"), request_ref::<str>(&child));
921    /// ```
922    #[unstable(feature = "error_generic_member_access", issue = "99301")]
923    pub fn would_be_satisfied_by_ref_of<T>(&self) -> bool
924    where
925        T: ?Sized + 'static,
926    {
927        self.would_be_satisfied_by::<tags::Ref<tags::MaybeSizedValue<T>>>()
928    }
929
930    fn would_be_satisfied_by<I>(&self) -> bool
931    where
932        I: tags::Type<'a>,
933    {
934        matches!(self.0.downcast::<I>(), Some(TaggedOption(None)))
935    }
936}
937
938#[unstable(feature = "error_generic_member_access", issue = "99301")]
939impl<'a> Debug for Request<'a> {
940    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
941        f.debug_struct("Request").finish_non_exhaustive()
942    }
943}
944
945///////////////////////////////////////////////////////////////////////////////
946// Type tags
947///////////////////////////////////////////////////////////////////////////////
948
949pub(crate) mod tags {
950    //! Type tags are used to identify a type using a separate value. This module includes type tags
951    //! for some very common types.
952    //!
953    //! Currently type tags are not exposed to the user. But in the future, if you want to use the
954    //! Request API with more complex types (typically those including lifetime parameters), you
955    //! will need to write your own tags.
956
957    use crate::marker::PhantomData;
958
959    /// This trait is implemented by specific tag types in order to allow
960    /// describing a type which can be requested for a given lifetime `'a`.
961    ///
962    /// A few example implementations for type-driven tags can be found in this
963    /// module, although crates may also implement their own tags for more
964    /// complex types with internal lifetimes.
965    pub(crate) trait Type<'a>: Sized + 'static {
966        /// The type of values which may be tagged by this tag for the given
967        /// lifetime.
968        type Reified: 'a;
969    }
970
971    /// Similar to the [`Type`] trait, but represents a type which may be unsized (i.e., has a
972    /// `?Sized` bound). E.g., `str`.
973    pub(crate) trait MaybeSizedType<'a>: Sized + 'static {
974        type Reified: 'a + ?Sized;
975    }
976
977    impl<'a, T: Type<'a>> MaybeSizedType<'a> for T {
978        type Reified = T::Reified;
979    }
980
981    /// Type-based tag for types bounded by `'static`, i.e., with no borrowed elements.
982    #[derive(Debug)]
983    pub(crate) struct Value<T: 'static>(PhantomData<T>);
984
985    impl<'a, T: 'static> Type<'a> for Value<T> {
986        type Reified = T;
987    }
988
989    /// Type-based tag similar to [`Value`] but which may be unsized (i.e., has a `?Sized` bound).
990    #[derive(Debug)]
991    pub(crate) struct MaybeSizedValue<T: ?Sized + 'static>(PhantomData<T>);
992
993    impl<'a, T: ?Sized + 'static> MaybeSizedType<'a> for MaybeSizedValue<T> {
994        type Reified = T;
995    }
996
997    /// Type-based tag for reference types (`&'a T`, where T is represented by
998    /// `<I as MaybeSizedType<'a>>::Reified`.
999    #[derive(Debug)]
1000    pub(crate) struct Ref<I>(PhantomData<I>);
1001
1002    impl<'a, I: MaybeSizedType<'a>> Type<'a> for Ref<I> {
1003        type Reified = &'a I::Reified;
1004    }
1005}
1006
1007/// An `Option` with a type tag `I`.
1008///
1009/// Since this struct implements `Erased`, the type can be erased to make a dynamically typed
1010/// option. The type can be checked dynamically using `Tagged::tag_id` and since this is statically
1011/// checked for the concrete type, there is some degree of type safety.
1012#[repr(transparent)]
1013pub(crate) struct TaggedOption<'a, I: tags::Type<'a>>(pub Option<I::Reified>);
1014
1015impl<'a, I: tags::Type<'a>> Tagged<TaggedOption<'a, I>> {
1016    pub(crate) fn as_request(&mut self) -> &mut Request<'a> {
1017        let erased = self as &mut Tagged<dyn Erased<'a> + 'a>;
1018        // SAFETY: transmuting `&mut Tagged<dyn Erased<'a> + 'a>` to `&mut Request<'a>` is safe since
1019        // `Request` is repr(transparent).
1020        unsafe { &mut *(erased as *mut Tagged<dyn Erased<'a>> as *mut Request<'a>) }
1021    }
1022}
1023
1024/// Represents a type-erased but identifiable object.
1025///
1026/// This trait is exclusively implemented by the `TaggedOption` type.
1027unsafe trait Erased<'a>: 'a {}
1028
1029unsafe impl<'a, I: tags::Type<'a>> Erased<'a> for TaggedOption<'a, I> {}
1030
1031struct Tagged<E: ?Sized> {
1032    tag_id: TypeId,
1033    value: E,
1034}
1035
1036impl<'a> Tagged<dyn Erased<'a> + 'a> {
1037    /// Returns some reference to the dynamic value if it is tagged with `I`,
1038    /// or `None` otherwise.
1039    #[inline]
1040    fn downcast<I>(&self) -> Option<&TaggedOption<'a, I>>
1041    where
1042        I: tags::Type<'a>,
1043    {
1044        if self.tag_id == TypeId::of::<I>() {
1045            // SAFETY: Just checked whether we're pointing to an I.
1046            Some(&unsafe { &*(self as *const Self).cast::<Tagged<TaggedOption<'a, I>>>() }.value)
1047        } else {
1048            None
1049        }
1050    }
1051
1052    /// Returns some mutable reference to the dynamic value if it is tagged with `I`,
1053    /// or `None` otherwise.
1054    #[inline]
1055    fn downcast_mut<I>(&mut self) -> Option<&mut TaggedOption<'a, I>>
1056    where
1057        I: tags::Type<'a>,
1058    {
1059        if self.tag_id == TypeId::of::<I>() {
1060            Some(
1061                // SAFETY: Just checked whether we're pointing to an I.
1062                &mut unsafe { &mut *(self as *mut Self).cast::<Tagged<TaggedOption<'a, I>>>() }
1063                    .value,
1064            )
1065        } else {
1066            None
1067        }
1068    }
1069}
1070
1071/// An iterator over an [`Error`] and its sources.
1072///
1073/// If you want to omit the initial error and only process
1074/// its sources, use `skip(1)`.
1075#[unstable(feature = "error_iter", issue = "58520")]
1076#[derive(Clone, Debug)]
1077pub struct Source<'a> {
1078    current: Option<&'a (dyn Error + 'static)>,
1079}
1080
1081#[unstable(feature = "error_iter", issue = "58520")]
1082impl<'a> Iterator for Source<'a> {
1083    type Item = &'a (dyn Error + 'static);
1084
1085    fn next(&mut self) -> Option<Self::Item> {
1086        let current = self.current;
1087        self.current = self.current.and_then(Error::source);
1088        current
1089    }
1090
1091    fn size_hint(&self) -> (usize, Option<usize>) {
1092        if self.current.is_some() { (1, None) } else { (0, Some(0)) }
1093    }
1094}
1095
1096#[unstable(feature = "error_iter", issue = "58520")]
1097impl<'a> crate::iter::FusedIterator for Source<'a> {}
1098
1099#[stable(feature = "error_by_ref", since = "1.51.0")]
1100impl<'a, T: Error + ?Sized> Error for &'a T {
1101    #[allow(deprecated)]
1102    fn cause(&self) -> Option<&dyn Error> {
1103        Error::cause(&**self)
1104    }
1105
1106    fn source(&self) -> Option<&(dyn Error + 'static)> {
1107        Error::source(&**self)
1108    }
1109
1110    fn provide<'b>(&'b self, request: &mut Request<'b>) {
1111        Error::provide(&**self, request);
1112    }
1113}
1114
1115#[stable(feature = "fmt_error", since = "1.11.0")]
1116impl Error for crate::fmt::Error {}
1117
1118#[stable(feature = "try_borrow", since = "1.13.0")]
1119impl Error for crate::cell::BorrowError {}
1120
1121#[stable(feature = "try_borrow", since = "1.13.0")]
1122impl Error for crate::cell::BorrowMutError {}
1123
1124#[stable(feature = "try_from", since = "1.34.0")]
1125impl Error for crate::char::CharTryFromError {}
1126
1127#[stable(feature = "duration_checked_float", since = "1.66.0")]
1128impl Error for crate::time::TryFromFloatSecsError {}
1129
1130#[stable(feature = "cstr_from_bytes_until_nul", since = "1.69.0")]
1131impl Error for crate::ffi::FromBytesUntilNulError {}
1132
1133#[stable(feature = "get_many_mut", since = "1.86.0")]
1134impl Error for crate::slice::GetDisjointMutError {}
````