---
title: convert.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#659
source: crawler
fetched_at: 2026-05-06T21:33:55.696652978-03:00
rendered_js: false
word_count: 2497
summary: This document defines the From trait implementations for Box, enabling conversions between heap-allocated boxed types and various source types like slices, strings, arrays, and Cow smart pointers.
tags:
    - rust
    - box
    - memory-management
    - type-conversion
    - heap-allocation
    - smart-pointers
category: reference
---

## alloc/boxed/ convert.rs

````rust
1use core::any::Any;
2use core::error::Error;
3#[cfg(not(no_global_oom_handling))]
4use core::fmt;
5use core::mem;
6use core::pin::Pin;
7
8use crate::alloc::Allocator;
9#[cfg(not(no_global_oom_handling))]
10use crate::borrow::Cow;
11use crate::boxed::Box;
12#[cfg(not(no_global_oom_handling))]
13use crate::string::String;
14#[cfg(not(no_global_oom_handling))]
15use crate::vec::Vec;
16
17#[cfg(not(no_global_oom_handling))]
18#[stable(feature = "from_for_ptrs", since = "1.6.0")]
19impl<T> From<T> for Box<T> {
20    /// Converts a `T` into a `Box<T>`
21    ///
22    /// The conversion allocates on the heap and moves `t`
23    /// from the stack into it.
24    ///
25    /// # Examples
26    ///
27    /// ```rust
28    /// let x = 5;
29    /// let boxed = Box::new(5);
30    ///
31    /// assert_eq!(Box::from(x), boxed);
32    /// ```
33    fn from(t: T) -> Self {
34        Box::new(t)
35    }
36}
37
38#[stable(feature = "pin", since = "1.33.0")]
39impl<T: ?Sized, A: Allocator> From<Box<T, A>> for Pin<Box<T, A>>
40where
41    A: 'static,
42{
43    /// Converts a `Box<T>` into a `Pin<Box<T>>`. If `T` does not implement [`Unpin`], then
44    /// `*boxed` will be pinned in memory and unable to be moved.
45    ///
46    /// This conversion does not allocate on the heap and happens in place.
47    ///
48    /// This is also available via [`Box::into_pin`].
49    ///
50    /// Constructing and pinning a `Box` with <code><Pin<Box\<T>>>::from([Box::new]\(x))</code>
51    /// can also be written more concisely using <code>[Box::pin]\(x)</code>.
52    /// This `From` implementation is useful if you already have a `Box<T>`, or you are
53    /// constructing a (pinned) `Box` in a different way than with [`Box::new`].
54    fn from(boxed: Box<T, A>) -> Self {
55        Box::into_pin(boxed)
56    }
57}
58
59#[cfg(not(no_global_oom_handling))]
60#[stable(feature = "box_from_slice", since = "1.17.0")]
61impl<T: Clone> From<&[T]> for Box<[T]> {
62    /// Converts a `&[T]` into a `Box<[T]>`
63    ///
64    /// This conversion allocates on the heap
65    /// and performs a copy of `slice` and its contents.
66    ///
67    /// # Examples
68    /// ```rust
69    /// // create a &[u8] which will be used to create a Box<[u8]>
70    /// let slice: &[u8] = &[104, 101, 108, 108, 111];
71    /// let boxed_slice: Box<[u8]> = Box::from(slice);
72    ///
73    /// println!("{boxed_slice:?}");
74    /// ```
75    #[inline]
76    fn from(slice: &[T]) -> Box<[T]> {
77        Box::clone_from_ref(slice)
78    }
79}
80
81#[cfg(not(no_global_oom_handling))]
82#[stable(feature = "box_from_mut_slice", since = "1.84.0")]
83impl<T: Clone> From<&mut [T]> for Box<[T]> {
84    /// Converts a `&mut [T]` into a `Box<[T]>`
85    ///
86    /// This conversion allocates on the heap
87    /// and performs a copy of `slice` and its contents.
88    ///
89    /// # Examples
90    /// ```rust
91    /// // create a &mut [u8] which will be used to create a Box<[u8]>
92    /// let mut array = [104, 101, 108, 108, 111];
93    /// let slice: &mut [u8] = &mut array;
94    /// let boxed_slice: Box<[u8]> = Box::from(slice);
95    ///
96    /// println!("{boxed_slice:?}");
97    /// ```
98    #[inline]
99    fn from(slice: &mut [T]) -> Box<[T]> {
100        Self::from(&*slice)
101    }
102}
103
104#[cfg(not(no_global_oom_handling))]
105#[stable(feature = "box_from_cow", since = "1.45.0")]
106impl<T: Clone> From<Cow<'_, [T]>> for Box<[T]> {
107    /// Converts a `Cow<'_, [T]>` into a `Box<[T]>`
108    ///
109    /// When `cow` is the `Cow::Borrowed` variant, this
110    /// conversion allocates on the heap and copies the
111    /// underlying slice. Otherwise, it will try to reuse the owned
112    /// `Vec`'s allocation.
113    #[inline]
114    fn from(cow: Cow<'_, [T]>) -> Box<[T]> {
115        match cow {
116            Cow::Borrowed(slice) => Box::from(slice),
117            Cow::Owned(slice) => Box::from(slice),
118        }
119    }
120}
121
122#[cfg(not(no_global_oom_handling))]
123#[stable(feature = "box_from_slice", since = "1.17.0")]
124impl From<&str> for Box<str> {
125    /// Converts a `&str` into a `Box<str>`
126    ///
127    /// This conversion allocates on the heap
128    /// and performs a copy of `s`.
129    ///
130    /// # Examples
131    ///
132    /// ```rust
133    /// let boxed: Box<str> = Box::from("hello");
134    /// println!("{boxed}");
135    /// ```
136    #[inline]
137    fn from(s: &str) -> Box<str> {
138        Box::clone_from_ref(s)
139    }
140}
141
142#[cfg(not(no_global_oom_handling))]
143#[stable(feature = "box_from_mut_slice", since = "1.84.0")]
144impl From<&mut str> for Box<str> {
145    /// Converts a `&mut str` into a `Box<str>`
146    ///
147    /// This conversion allocates on the heap
148    /// and performs a copy of `s`.
149    ///
150    /// # Examples
151    ///
152    /// ```rust
153    /// let mut original = String::from("hello");
154    /// let original: &mut str = &mut original;
155    /// let boxed: Box<str> = Box::from(original);
156    /// println!("{boxed}");
157    /// ```
158    #[inline]
159    fn from(s: &mut str) -> Box<str> {
160        Self::from(&*s)
161    }
162}
163
164#[cfg(not(no_global_oom_handling))]
165#[stable(feature = "box_from_cow", since = "1.45.0")]
166impl From<Cow<'_, str>> for Box<str> {
167    /// Converts a `Cow<'_, str>` into a `Box<str>`
168    ///
169    /// When `cow` is the `Cow::Borrowed` variant, this
170    /// conversion allocates on the heap and copies the
171    /// underlying `str`. Otherwise, it will try to reuse the owned
172    /// `String`'s allocation.
173    ///
174    /// # Examples
175    ///
176    /// ```rust
177    /// use std::borrow::Cow;
178    ///
179    /// let unboxed = Cow::Borrowed("hello");
180    /// let boxed: Box<str> = Box::from(unboxed);
181    /// println!("{boxed}");
182    /// ```
183    ///
184    /// ```rust
185    /// # use std::borrow::Cow;
186    /// let unboxed = Cow::Owned("hello".to_string());
187    /// let boxed: Box<str> = Box::from(unboxed);
188    /// println!("{boxed}");
189    /// ```
190    #[inline]
191    fn from(cow: Cow<'_, str>) -> Box<str> {
192        match cow {
193            Cow::Borrowed(s) => Box::from(s),
194            Cow::Owned(s) => Box::from(s),
195        }
196    }
197}
198
199#[stable(feature = "boxed_str_conv", since = "1.19.0")]
200impl<A: Allocator> From<Box<str, A>> for Box<[u8], A> {
201    /// Converts a `Box<str>` into a `Box<[u8]>`
202    ///
203    /// This conversion does not allocate on the heap and happens in place.
204    ///
205    /// # Examples
206    /// ```rust
207    /// // create a Box<str> which will be used to create a Box<[u8]>
208    /// let boxed: Box<str> = Box::from("hello");
209    /// let boxed_str: Box<[u8]> = Box::from(boxed);
210    ///
211    /// // create a &[u8] which will be used to create a Box<[u8]>
212    /// let slice: &[u8] = &[104, 101, 108, 108, 111];
213    /// let boxed_slice = Box::from(slice);
214    ///
215    /// assert_eq!(boxed_slice, boxed_str);
216    /// ```
217    #[inline]
218    fn from(s: Box<str, A>) -> Self {
219        let (raw, alloc) = Box::into_raw_with_allocator(s);
220        unsafe { Box::from_raw_in(raw as *mut [u8], alloc) }
221    }
222}
223
224#[cfg(not(no_global_oom_handling))]
225#[stable(feature = "box_from_array", since = "1.45.0")]
226impl<T, const N: usize> From<[T; N]> for Box<[T]> {
227    /// Converts a `[T; N]` into a `Box<[T]>`
228    ///
229    /// This conversion moves the array to newly heap-allocated memory.
230    ///
231    /// # Examples
232    ///
233    /// ```rust
234    /// let boxed: Box<[u8]> = Box::from([4, 2]);
235    /// println!("{boxed:?}");
236    /// ```
237    fn from(array: [T; N]) -> Box<[T]> {
238        Box::new(array)
239    }
240}
241
242/// Casts a boxed slice to a boxed array.
243///
244/// # Safety
245///
246/// `boxed_slice.len()` must be exactly `N`.
247unsafe fn boxed_slice_as_array_unchecked<T, A: Allocator, const N: usize>(
248    boxed_slice: Box<[T], A>,
249) -> Box<[T; N], A> {
250    debug_assert_eq!(boxed_slice.len(), N);
251
252    let (ptr, alloc) = Box::into_raw_with_allocator(boxed_slice);
253    // SAFETY: Pointer and allocator came from an existing box,
254    // and our safety condition requires that the length is exactly `N`
255    unsafe { Box::from_raw_in(ptr as *mut [T; N], alloc) }
256}
257
258#[stable(feature = "boxed_slice_try_from", since = "1.43.0")]
259impl<T, const N: usize> TryFrom<Box<[T]>> for Box<[T; N]> {
260    type Error = Box<[T]>;
261
262    /// Attempts to convert a `Box<[T]>` into a `Box<[T; N]>`.
263    ///
264    /// The conversion occurs in-place and does not require a
265    /// new memory allocation.
266    ///
267    /// # Errors
268    ///
269    /// Returns the old `Box<[T]>` in the `Err` variant if
270    /// `boxed_slice.len()` does not equal `N`.
271    fn try_from(boxed_slice: Box<[T]>) -> Result<Self, Self::Error> {
272        if boxed_slice.len() == N {
273            Ok(unsafe { boxed_slice_as_array_unchecked(boxed_slice) })
274        } else {
275            Err(boxed_slice)
276        }
277    }
278}
279
280#[cfg(not(no_global_oom_handling))]
281#[stable(feature = "boxed_array_try_from_vec", since = "1.66.0")]
282impl<T, const N: usize> TryFrom<Vec<T>> for Box<[T; N]> {
283    type Error = Vec<T>;
284
285    /// Attempts to convert a `Vec<T>` into a `Box<[T; N]>`.
286    ///
287    /// Like [`Vec::into_boxed_slice`], this is in-place if `vec.capacity() == N`,
288    /// but will require a reallocation otherwise.
289    ///
290    /// # Errors
291    ///
292    /// Returns the original `Vec<T>` in the `Err` variant if
293    /// `boxed_slice.len()` does not equal `N`.
294    ///
295    /// # Examples
296    ///
297    /// This can be used with [`vec!`] to create an array on the heap:
298    ///
299    /// ```
300    /// let state: Box<[f32; 100]> = vec![1.0; 100].try_into().unwrap();
301    /// assert_eq!(state.len(), 100);
302    /// ```
303    fn try_from(vec: Vec<T>) -> Result<Self, Self::Error> {
304        if vec.len() == N {
305            let boxed_slice = vec.into_boxed_slice();
306            Ok(unsafe { boxed_slice_as_array_unchecked(boxed_slice) })
307        } else {
308            Err(vec)
309        }
310    }
311}
312
313impl<A: Allocator> Box<dyn Any, A> {
314    /// Attempts to downcast the box to a concrete type.
315    ///
316    /// # Examples
317    ///
318    /// ```
319    /// use std::any::Any;
320    ///
321    /// fn print_if_string(value: Box<dyn Any>) {
322    ///     if let Ok(string) = value.downcast::<String>() {
323    ///         println!("String ({}): {}", string.len(), string);
324    ///     }
325    /// }
326    ///
327    /// let my_string = "Hello World".to_string();
328    /// print_if_string(Box::new(my_string));
329    /// print_if_string(Box::new(0i8));
330    /// ```
331    #[inline]
332    #[stable(feature = "rust1", since = "1.0.0")]
333    pub fn downcast<T: Any>(self) -> Result<Box<T, A>, Self> {
334        if self.is::<T>() { unsafe { Ok(self.downcast_unchecked::<T>()) } } else { Err(self) }
335    }
336
337    /// Downcasts the box to a concrete type.
338    ///
339    /// For a safe alternative see [`downcast`].
340    ///
341    /// # Examples
342    ///
343    /// ```
344    /// #![feature(downcast_unchecked)]
345    ///
346    /// use std::any::Any;
347    ///
348    /// let x: Box<dyn Any> = Box::new(1_usize);
349    ///
350    /// unsafe {
351    ///     assert_eq!(*x.downcast_unchecked::<usize>(), 1);
352    /// }
353    /// ```
354    ///
355    /// # Safety
356    ///
357    /// The contained value must be of type `T`. Calling this method
358    /// with the incorrect type is *undefined behavior*.
359    ///
360    /// [`downcast`]: Self::downcast
361    #[inline]
362    #[unstable(feature = "downcast_unchecked", issue = "90850")]
363    pub unsafe fn downcast_unchecked<T: Any>(self) -> Box<T, A> {
364        debug_assert!(self.is::<T>());
365        unsafe {
366            let (raw, alloc): (*mut dyn Any, _) = Box::into_raw_with_allocator(self);
367            Box::from_raw_in(raw as *mut T, alloc)
368        }
369    }
370}
371
372impl<A: Allocator> Box<dyn Any + Send, A> {
373    /// Attempts to downcast the box to a concrete type.
374    ///
375    /// # Examples
376    ///
377    /// ```
378    /// use std::any::Any;
379    ///
380    /// fn print_if_string(value: Box<dyn Any + Send>) {
381    ///     if let Ok(string) = value.downcast::<String>() {
382    ///         println!("String ({}): {}", string.len(), string);
383    ///     }
384    /// }
385    ///
386    /// let my_string = "Hello World".to_string();
387    /// print_if_string(Box::new(my_string));
388    /// print_if_string(Box::new(0i8));
389    /// ```
390    #[inline]
391    #[stable(feature = "rust1", since = "1.0.0")]
392    pub fn downcast<T: Any>(self) -> Result<Box<T, A>, Self> {
393        if self.is::<T>() { unsafe { Ok(self.downcast_unchecked::<T>()) } } else { Err(self) }
394    }
395
396    /// Downcasts the box to a concrete type.
397    ///
398    /// For a safe alternative see [`downcast`].
399    ///
400    /// # Examples
401    ///
402    /// ```
403    /// #![feature(downcast_unchecked)]
404    ///
405    /// use std::any::Any;
406    ///
407    /// let x: Box<dyn Any + Send> = Box::new(1_usize);
408    ///
409    /// unsafe {
410    ///     assert_eq!(*x.downcast_unchecked::<usize>(), 1);
411    /// }
412    /// ```
413    ///
414    /// # Safety
415    ///
416    /// The contained value must be of type `T`. Calling this method
417    /// with the incorrect type is *undefined behavior*.
418    ///
419    /// [`downcast`]: Self::downcast
420    #[inline]
421    #[unstable(feature = "downcast_unchecked", issue = "90850")]
422    pub unsafe fn downcast_unchecked<T: Any>(self) -> Box<T, A> {
423        debug_assert!(self.is::<T>());
424        unsafe {
425            let (raw, alloc): (*mut (dyn Any + Send), _) = Box::into_raw_with_allocator(self);
426            Box::from_raw_in(raw as *mut T, alloc)
427        }
428    }
429}
430
431impl<A: Allocator> Box<dyn Any + Send + Sync, A> {
432    /// Attempts to downcast the box to a concrete type.
433    ///
434    /// # Examples
435    ///
436    /// ```
437    /// use std::any::Any;
438    ///
439    /// fn print_if_string(value: Box<dyn Any + Send + Sync>) {
440    ///     if let Ok(string) = value.downcast::<String>() {
441    ///         println!("String ({}): {}", string.len(), string);
442    ///     }
443    /// }
444    ///
445    /// let my_string = "Hello World".to_string();
446    /// print_if_string(Box::new(my_string));
447    /// print_if_string(Box::new(0i8));
448    /// ```
449    #[inline]
450    #[stable(feature = "box_send_sync_any_downcast", since = "1.51.0")]
451    pub fn downcast<T: Any>(self) -> Result<Box<T, A>, Self> {
452        if self.is::<T>() { unsafe { Ok(self.downcast_unchecked::<T>()) } } else { Err(self) }
453    }
454
455    /// Downcasts the box to a concrete type.
456    ///
457    /// For a safe alternative see [`downcast`].
458    ///
459    /// # Examples
460    ///
461    /// ```
462    /// #![feature(downcast_unchecked)]
463    ///
464    /// use std::any::Any;
465    ///
466    /// let x: Box<dyn Any + Send + Sync> = Box::new(1_usize);
467    ///
468    /// unsafe {
469    ///     assert_eq!(*x.downcast_unchecked::<usize>(), 1);
470    /// }
471    /// ```
472    ///
473    /// # Safety
474    ///
475    /// The contained value must be of type `T`. Calling this method
476    /// with the incorrect type is *undefined behavior*.
477    ///
478    /// [`downcast`]: Self::downcast
479    #[inline]
480    #[unstable(feature = "downcast_unchecked", issue = "90850")]
481    pub unsafe fn downcast_unchecked<T: Any>(self) -> Box<T, A> {
482        debug_assert!(self.is::<T>());
483        unsafe {
484            let (raw, alloc): (*mut (dyn Any + Send + Sync), _) =
485                Box::into_raw_with_allocator(self);
486            Box::from_raw_in(raw as *mut T, alloc)
487        }
488    }
489}
490
491#[cfg(not(no_global_oom_handling))]
492#[stable(feature = "rust1", since = "1.0.0")]
493impl<'a, E: Error + 'a> From<E> for Box<dyn Error + 'a> {
494    /// Converts a type of [`Error`] into a box of dyn [`Error`].
495    ///
496    /// # Examples
497    ///
498    /// ```
499    /// use std::error::Error;
500    /// use std::fmt;
501    ///
502    /// #[derive(Debug)]
503    /// struct AnError;
504    ///
505    /// impl fmt::Display for AnError {
506    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
507    ///         write!(f, "An error")
508    ///     }
509    /// }
510    ///
511    /// impl Error for AnError {}
512    ///
513    /// let an_error = AnError;
514    /// assert!(0 == size_of_val(&an_error));
515    /// let a_boxed_error = Box::<dyn Error>::from(an_error);
516    /// assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
517    /// ```
518    fn from(err: E) -> Box<dyn Error + 'a> {
519        Box::new(err)
520    }
521}
522
523#[cfg(not(no_global_oom_handling))]
524#[stable(feature = "rust1", since = "1.0.0")]
525impl<'a, E: Error + Send + Sync + 'a> From<E> for Box<dyn Error + Send + Sync + 'a> {
526    /// Converts a type of [`Error`] + [`Send`] + [`Sync`] into a box of
527    /// dyn [`Error`] + [`Send`] + [`Sync`].
528    ///
529    /// # Examples
530    ///
531    /// ```
532    /// use std::error::Error;
533    /// use std::fmt;
534    ///
535    /// #[derive(Debug)]
536    /// struct AnError;
537    ///
538    /// impl fmt::Display for AnError {
539    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
540    ///         write!(f, "An error")
541    ///     }
542    /// }
543    ///
544    /// impl Error for AnError {}
545    ///
546    /// unsafe impl Send for AnError {}
547    ///
548    /// unsafe impl Sync for AnError {}
549    ///
550    /// let an_error = AnError;
551    /// assert!(0 == size_of_val(&an_error));
552    /// let a_boxed_error = Box::<dyn Error + Send + Sync>::from(an_error);
553    /// assert!(
554    ///     size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
555    /// ```
556    fn from(err: E) -> Box<dyn Error + Send + Sync + 'a> {
557        Box::new(err)
558    }
559}
560
561#[cfg(not(no_global_oom_handling))]
562#[stable(feature = "rust1", since = "1.0.0")]
563impl<'a> From<String> for Box<dyn Error + Send + Sync + 'a> {
564    /// Converts a [`String`] into a box of dyn [`Error`] + [`Send`] + [`Sync`].
565    ///
566    /// # Examples
567    ///
568    /// ```
569    /// use std::error::Error;
570    ///
571    /// let a_string_error = "a string error".to_string();
572    /// let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_string_error);
573    /// assert!(
574    ///     size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
575    /// ```
576    #[inline]
577    fn from(err: String) -> Box<dyn Error + Send + Sync + 'a> {
578        struct StringError(String);
579
580        impl Error for StringError {}
581
582        impl fmt::Display for StringError {
583            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
584                fmt::Display::fmt(&self.0, f)
585            }
586        }
587
588        // Purposefully skip printing "StringError(..)"
589        impl fmt::Debug for StringError {
590            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
591                fmt::Debug::fmt(&self.0, f)
592            }
593        }
594
595        Box::new(StringError(err))
596    }
597}
598
599#[cfg(not(no_global_oom_handling))]
600#[stable(feature = "string_box_error", since = "1.6.0")]
601impl<'a> From<String> for Box<dyn Error + 'a> {
602    /// Converts a [`String`] into a box of dyn [`Error`].
603    ///
604    /// # Examples
605    ///
606    /// ```
607    /// use std::error::Error;
608    ///
609    /// let a_string_error = "a string error".to_string();
610    /// let a_boxed_error = Box::<dyn Error>::from(a_string_error);
611    /// assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
612    /// ```
613    fn from(str_err: String) -> Box<dyn Error + 'a> {
614        let err1: Box<dyn Error + Send + Sync> = From::from(str_err);
615        let err2: Box<dyn Error> = err1;
616        err2
617    }
618}
619
620#[cfg(not(no_global_oom_handling))]
621#[stable(feature = "rust1", since = "1.0.0")]
622impl<'a> From<&str> for Box<dyn Error + Send + Sync + 'a> {
623    /// Converts a [`str`] into a box of dyn [`Error`] + [`Send`] + [`Sync`].
624    ///
625    /// [`str`]: prim@str
626    ///
627    /// # Examples
628    ///
629    /// ```
630    /// use std::error::Error;
631    ///
632    /// let a_str_error = "a str error";
633    /// let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_str_error);
634    /// assert!(
635    ///     size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
636    /// ```
637    #[inline]
638    fn from(err: &str) -> Box<dyn Error + Send + Sync + 'a> {
639        From::from(String::from(err))
640    }
641}
642
643#[cfg(not(no_global_oom_handling))]
644#[stable(feature = "string_box_error", since = "1.6.0")]
645impl<'a> From<&str> for Box<dyn Error + 'a> {
646    /// Converts a [`str`] into a box of dyn [`Error`].
647    ///
648    /// [`str`]: prim@str
649    ///
650    /// # Examples
651    ///
652    /// ```
653    /// use std::error::Error;
654    ///
655    /// let a_str_error = "a str error";
656    /// let a_boxed_error = Box::<dyn Error>::from(a_str_error);
657    /// assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
658    /// ```
659    fn from(err: &str) -> Box<dyn Error + 'a> {
660        From::from(String::from(err))
661    }
662}
663
664#[cfg(not(no_global_oom_handling))]
665#[stable(feature = "cow_box_error", since = "1.22.0")]
666impl<'a, 'b> From<Cow<'b, str>> for Box<dyn Error + Send + Sync + 'a> {
667    /// Converts a [`Cow`] into a box of dyn [`Error`] + [`Send`] + [`Sync`].
668    ///
669    /// # Examples
670    ///
671    /// ```
672    /// use std::error::Error;
673    /// use std::borrow::Cow;
674    ///
675    /// let a_cow_str_error = Cow::from("a str error");
676    /// let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_cow_str_error);
677    /// assert!(
678    ///     size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
679    /// ```
680    fn from(err: Cow<'b, str>) -> Box<dyn Error + Send + Sync + 'a> {
681        From::from(String::from(err))
682    }
683}
684
685#[cfg(not(no_global_oom_handling))]
686#[stable(feature = "cow_box_error", since = "1.22.0")]
687impl<'a, 'b> From<Cow<'b, str>> for Box<dyn Error + 'a> {
688    /// Converts a [`Cow`] into a box of dyn [`Error`].
689    ///
690    /// # Examples
691    ///
692    /// ```
693    /// use std::error::Error;
694    /// use std::borrow::Cow;
695    ///
696    /// let a_cow_str_error = Cow::from("a str error");
697    /// let a_boxed_error = Box::<dyn Error>::from(a_cow_str_error);
698    /// assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
699    /// ```
700    fn from(err: Cow<'b, str>) -> Box<dyn Error + 'a> {
701        From::from(String::from(err))
702    }
703}
704
705impl dyn Error {
706    /// Attempts to downcast the box to a concrete type.
707    #[inline]
708    #[stable(feature = "error_downcast", since = "1.3.0")]
709    #[rustc_allow_incoherent_impl]
710    pub fn downcast<T: Error + 'static>(self: Box<Self>) -> Result<Box<T>, Box<dyn Error>> {
711        if self.is::<T>() {
712            unsafe {
713                let raw: *mut dyn Error = Box::into_raw(self);
714                Ok(Box::from_raw(raw as *mut T))
715            }
716        } else {
717            Err(self)
718        }
719    }
720}
721
722impl dyn Error + Send {
723    /// Attempts to downcast the box to a concrete type.
724    #[inline]
725    #[stable(feature = "error_downcast", since = "1.3.0")]
726    #[rustc_allow_incoherent_impl]
727    pub fn downcast<T: Error + 'static>(self: Box<Self>) -> Result<Box<T>, Box<dyn Error + Send>> {
728        let err: Box<dyn Error> = self;
729        <dyn Error>::downcast(err).map_err(|s| unsafe {
730            // Reapply the `Send` marker.
731            mem::transmute::<Box<dyn Error>, Box<dyn Error + Send>>(s)
732        })
733    }
734}
735
736impl dyn Error + Send + Sync {
737    /// Attempts to downcast the box to a concrete type.
738    #[inline]
739    #[stable(feature = "error_downcast", since = "1.3.0")]
740    #[rustc_allow_incoherent_impl]
741    pub fn downcast<T: Error + 'static>(self: Box<Self>) -> Result<Box<T>, Box<Self>> {
742        let err: Box<dyn Error> = self;
743        <dyn Error>::downcast(err).map_err(|s| unsafe {
744            // Reapply the `Send + Sync` markers.
745            mem::transmute::<Box<dyn Error>, Box<dyn Error + Send + Sync>>(s)
746        })
747    }
748}
````