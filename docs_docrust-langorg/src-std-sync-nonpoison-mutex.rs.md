---
title: mutex.rs - source
url: https://doc.rust-lang.org/src/std/sync/nonpoison/mutex.rs.html#556-562
source: crawler
fetched_at: 2026-05-06T21:36:26.362817019-03:00
rendered_js: false
word_count: 3108
summary: This document defines a non-poisoning Mutex implementation in Rust, providing a thread-synchronization primitive that does not track or propagate lock poisoning when threads panic.
tags:
    - rust
    - concurrency
    - mutex
    - synchronization
    - thread-safety
    - raii
category: reference
---

## std/sync/nonpoison/ mutex.rs

````rust
1use crate::cell::UnsafeCell;
2use crate::fmt;
3use crate::marker::PhantomData;
4use crate::mem::{self, ManuallyDrop};
5use crate::ops::{Deref, DerefMut};
6use crate::ptr::NonNull;
7use crate::sync::nonpoison::{TryLockResult, WouldBlock};
8use crate::sys::sync as sys;
9
10/// A mutual exclusion primitive useful for protecting shared data that does not keep track of
11/// lock poisoning.
12///
13/// For more information about mutexes, check out the documentation for the poisoning variant of
14/// this lock at [`poison::Mutex`].
15///
16/// [`poison::Mutex`]: crate::sync::poison::Mutex
17///
18/// # Examples
19///
20/// Note that this `Mutex` does **not** propagate threads that panic while holding the lock via
21/// poisoning. If you need this functionality, see [`poison::Mutex`].
22///
23/// ```
24/// #![feature(nonpoison_mutex)]
25///
26/// use std::thread;
27/// use std::sync::{Arc, nonpoison::Mutex};
28///
29/// let mutex = Arc::new(Mutex::new(0u32));
30/// let mut handles = Vec::new();
31///
32/// for n in 0..10 {
33///     let m = Arc::clone(&mutex);
34///     let handle = thread::spawn(move || {
35///         let mut guard = m.lock();
36///         *guard += 1;
37///         panic!("panic from thread {n} {guard}")
38///     });
39///     handles.push(handle);
40/// }
41///
42/// for h in handles {
43///     let _ = h.join();
44/// }
45///
46/// println!("Finished, locked {} times", mutex.lock());
47/// ```
48#[unstable(feature = "nonpoison_mutex", issue = "134645")]
49#[cfg_attr(not(test), rustc_diagnostic_item = "NonPoisonMutex")]
50pub struct Mutex<T: ?Sized> {
51    inner: sys::Mutex,
52    data: UnsafeCell<T>,
53}
54
55/// `T` must be `Send` for a [`Mutex`] to be `Send` because it is possible to acquire
56/// the owned `T` from the `Mutex` via [`into_inner`].
57///
58/// [`into_inner`]: Mutex::into_inner
59#[unstable(feature = "nonpoison_mutex", issue = "134645")]
60unsafe impl<T: ?Sized + Send> Send for Mutex<T> {}
61
62/// `T` must be `Send` for [`Mutex`] to be `Sync`.
63/// This ensures that the protected data can be accessed safely from multiple threads
64/// without causing data races or other unsafe behavior.
65///
66/// [`Mutex<T>`] provides mutable access to `T` to one thread at a time. However, it's essential
67/// for `T` to be `Send` because it's not safe for non-`Send` structures to be accessed in
68/// this manner. For instance, consider [`Rc`], a non-atomic reference counted smart pointer,
69/// which is not `Send`. With `Rc`, we can have multiple copies pointing to the same heap
70/// allocation with a non-atomic reference count. If we were to use `Mutex<Rc<_>>`, it would
71/// only protect one instance of `Rc` from shared access, leaving other copies vulnerable
72/// to potential data races.
73///
74/// Also note that it is not necessary for `T` to be `Sync` as `&T` is only made available
75/// to one thread at a time if `T` is not `Sync`.
76///
77/// [`Rc`]: crate::rc::Rc
78#[unstable(feature = "nonpoison_mutex", issue = "134645")]
79unsafe impl<T: ?Sized + Send> Sync for Mutex<T> {}
80
81/// An RAII implementation of a "scoped lock" of a mutex. When this structure is
82/// dropped (falls out of scope), the lock will be unlocked.
83///
84/// The data protected by the mutex can be accessed through this guard via its
85/// [`Deref`] and [`DerefMut`] implementations.
86///
87/// This structure is created by the [`lock`] and [`try_lock`] methods on
88/// [`Mutex`].
89///
90/// [`lock`]: Mutex::lock
91/// [`try_lock`]: Mutex::try_lock
92#[must_use = "if unused the Mutex will immediately unlock"]
93#[must_not_suspend = "holding a MutexGuard across suspend \
94                      points can cause deadlocks, delays, \
95                      and cause Futures to not implement `Send`"]
96#[unstable(feature = "nonpoison_mutex", issue = "134645")]
97#[clippy::has_significant_drop]
98#[cfg_attr(not(test), rustc_diagnostic_item = "NonPoisonMutexGuard")]
99pub struct MutexGuard<'a, T: ?Sized + 'a> {
100    lock: &'a Mutex<T>,
101}
102
103/// A [`MutexGuard`] is not `Send` to maximize platform portability.
104///
105/// On platforms that use POSIX threads (commonly referred to as pthreads) there is a requirement to
106/// release mutex locks on the same thread they were acquired.
107/// For this reason, [`MutexGuard`] must not implement `Send` to prevent it being dropped from
108/// another thread.
109#[unstable(feature = "nonpoison_mutex", issue = "134645")]
110impl<T: ?Sized> !Send for MutexGuard<'_, T> {}
111
112/// `T` must be `Sync` for a [`MutexGuard<T>`] to be `Sync`
113/// because it is possible to get a `&T` from `&MutexGuard` (via `Deref`).
114#[unstable(feature = "nonpoison_mutex", issue = "134645")]
115unsafe impl<T: ?Sized + Sync> Sync for MutexGuard<'_, T> {}
116
117/// An RAII mutex guard returned by `MutexGuard::map`, which can point to a
118/// subfield of the protected data. When this structure is dropped (falls out
119/// of scope), the lock will be unlocked.
120///
121/// The main difference between `MappedMutexGuard` and [`MutexGuard`] is that the
122/// former cannot be used with [`Condvar`], since that could introduce soundness issues if the
123/// locked object is modified by another thread while the `Mutex` is unlocked.
124///
125/// The data protected by the mutex can be accessed through this guard via its
126/// [`Deref`] and [`DerefMut`] implementations.
127///
128/// This structure is created by the [`map`] and [`filter_map`] methods on
129/// [`MutexGuard`].
130///
131/// [`map`]: MutexGuard::map
132/// [`filter_map`]: MutexGuard::filter_map
133/// [`Condvar`]: crate::sync::nonpoison::Condvar
134#[must_use = "if unused the Mutex will immediately unlock"]
135#[must_not_suspend = "holding a MappedMutexGuard across suspend \
136                      points can cause deadlocks, delays, \
137                      and cause Futures to not implement `Send`"]
138#[unstable(feature = "mapped_lock_guards", issue = "117108")]
139// #[unstable(feature = "nonpoison_mutex", issue = "134645")]
140#[clippy::has_significant_drop]
141pub struct MappedMutexGuard<'a, T: ?Sized + 'a> {
142    // NB: we use a pointer instead of `&'a mut T` to avoid `noalias` violations, because a
143    // `MappedMutexGuard` argument doesn't hold uniqueness for its whole scope, only until it drops.
144    // `NonNull` is covariant over `T`, so we add a `PhantomData<&'a mut T>` field
145    // below for the correct variance over `T` (invariance).
146    data: NonNull<T>,
147    inner: &'a sys::Mutex,
148    _variance: PhantomData<&'a mut T>,
149}
150
151#[unstable(feature = "mapped_lock_guards", issue = "117108")]
152// #[unstable(feature = "nonpoison_mutex", issue = "134645")]
153impl<T: ?Sized> !Send for MappedMutexGuard<'_, T> {}
154#[unstable(feature = "mapped_lock_guards", issue = "117108")]
155// #[unstable(feature = "nonpoison_mutex", issue = "134645")]
156unsafe impl<T: ?Sized + Sync> Sync for MappedMutexGuard<'_, T> {}
157
158impl<T> Mutex<T> {
159    /// Creates a new mutex in an unlocked state ready for use.
160    ///
161    /// # Examples
162    ///
163    /// ```
164    /// #![feature(nonpoison_mutex)]
165    ///
166    /// use std::sync::nonpoison::Mutex;
167    ///
168    /// let mutex = Mutex::new(0);
169    /// ```
170    #[unstable(feature = "nonpoison_mutex", issue = "134645")]
171    #[inline]
172    pub const fn new(t: T) -> Mutex<T> {
173        Mutex { inner: sys::Mutex::new(), data: UnsafeCell::new(t) }
174    }
175
176    /// Returns the contained value by cloning it.
177    ///
178    /// # Examples
179    ///
180    /// ```
181    /// #![feature(nonpoison_mutex)]
182    /// #![feature(lock_value_accessors)]
183    ///
184    /// use std::sync::nonpoison::Mutex;
185    ///
186    /// let mut mutex = Mutex::new(7);
187    ///
188    /// assert_eq!(mutex.get_cloned(), 7);
189    /// ```
190    #[unstable(feature = "lock_value_accessors", issue = "133407")]
191    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
192    pub fn get_cloned(&self) -> T
193    where
194        T: Clone,
195    {
196        self.lock().clone()
197    }
198
199    /// Sets the contained value.
200    ///
201    /// # Examples
202    ///
203    /// ```
204    /// #![feature(nonpoison_mutex)]
205    /// #![feature(lock_value_accessors)]
206    ///
207    /// use std::sync::nonpoison::Mutex;
208    ///
209    /// let mut mutex = Mutex::new(7);
210    ///
211    /// assert_eq!(mutex.get_cloned(), 7);
212    /// mutex.set(11);
213    /// assert_eq!(mutex.get_cloned(), 11);
214    /// ```
215    #[unstable(feature = "lock_value_accessors", issue = "133407")]
216    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
217    pub fn set(&self, value: T) {
218        if mem::needs_drop::<T>() {
219            // If the contained value has a non-trivial destructor, we
220            // call that destructor after the lock has been released.
221            drop(self.replace(value))
222        } else {
223            *self.lock() = value;
224        }
225    }
226
227    /// Replaces the contained value with `value`, and returns the old contained value.
228    ///
229    /// # Examples
230    ///
231    /// ```
232    /// #![feature(nonpoison_mutex)]
233    /// #![feature(lock_value_accessors)]
234    ///
235    /// use std::sync::nonpoison::Mutex;
236    ///
237    /// let mut mutex = Mutex::new(7);
238    ///
239    /// assert_eq!(mutex.replace(11), 7);
240    /// assert_eq!(mutex.get_cloned(), 11);
241    /// ```
242    #[unstable(feature = "lock_value_accessors", issue = "133407")]
243    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
244    pub fn replace(&self, value: T) -> T {
245        let mut guard = self.lock();
246        mem::replace(&mut *guard, value)
247    }
248}
249
250impl<T: ?Sized> Mutex<T> {
251    /// Acquires a mutex, blocking the current thread until it is able to do so.
252    ///
253    /// This function will block the local thread until it is available to acquire
254    /// the mutex. Upon returning, the thread is the only thread with the lock
255    /// held. An RAII guard is returned to allow scoped unlock of the lock. When
256    /// the guard goes out of scope, the mutex will be unlocked.
257    ///
258    /// The exact behavior on locking a mutex in the thread which already holds
259    /// the lock is left unspecified. However, this function will not return on
260    /// the second call (it might panic or deadlock, for example).
261    ///
262    /// # Panics
263    ///
264    /// This function might panic when called if the lock is already held by
265    /// the current thread.
266    ///
267    /// # Examples
268    ///
269    /// ```
270    /// #![feature(nonpoison_mutex)]
271    ///
272    /// use std::sync::{Arc, nonpoison::Mutex};
273    /// use std::thread;
274    ///
275    /// let mutex = Arc::new(Mutex::new(0));
276    /// let c_mutex = Arc::clone(&mutex);
277    ///
278    /// thread::spawn(move || {
279    ///     *c_mutex.lock() = 10;
280    /// }).join().expect("thread::spawn failed");
281    /// assert_eq!(*mutex.lock(), 10);
282    /// ```
283    #[unstable(feature = "nonpoison_mutex", issue = "134645")]
284    pub fn lock(&self) -> MutexGuard<'_, T> {
285        unsafe {
286            self.inner.lock();
287            MutexGuard::new(self)
288        }
289    }
290
291    /// Attempts to acquire this lock.
292    ///
293    /// This function does not block. If the lock could not be acquired at this time, then
294    /// [`WouldBlock`] is returned. Otherwise, an RAII guard is returned.
295    ///
296    /// The lock will be unlocked when the guard is dropped.
297    ///
298    /// # Errors
299    ///
300    /// If the mutex could not be acquired because it is already locked, then this call will return
301    /// the [`WouldBlock`] error.
302    ///
303    /// # Examples
304    ///
305    /// ```
306    /// use std::sync::{Arc, Mutex};
307    /// use std::thread;
308    ///
309    /// let mutex = Arc::new(Mutex::new(0));
310    /// let c_mutex = Arc::clone(&mutex);
311    ///
312    /// thread::spawn(move || {
313    ///     let mut lock = c_mutex.try_lock();
314    ///     if let Ok(ref mut mutex) = lock {
315    ///         **mutex = 10;
316    ///     } else {
317    ///         println!("try_lock failed");
318    ///     }
319    /// }).join().expect("thread::spawn failed");
320    /// assert_eq!(*mutex.lock().unwrap(), 10);
321    /// ```
322    #[unstable(feature = "nonpoison_mutex", issue = "134645")]
323    pub fn try_lock(&self) -> TryLockResult<MutexGuard<'_, T>> {
324        unsafe { if self.inner.try_lock() { Ok(MutexGuard::new(self)) } else { Err(WouldBlock) } }
325    }
326
327    /// Consumes this mutex, returning the underlying data.
328    ///
329    /// # Examples
330    ///
331    /// ```
332    /// #![feature(nonpoison_mutex)]
333    ///
334    /// use std::sync::nonpoison::Mutex;
335    ///
336    /// let mutex = Mutex::new(0);
337    /// assert_eq!(mutex.into_inner(), 0);
338    /// ```
339    #[unstable(feature = "nonpoison_mutex", issue = "134645")]
340    pub fn into_inner(self) -> T
341    where
342        T: Sized,
343    {
344        self.data.into_inner()
345    }
346
347    /// Returns a mutable reference to the underlying data.
348    ///
349    /// Since this call borrows the `Mutex` mutably, no actual locking needs to
350    /// take place -- the mutable borrow statically guarantees no locks exist.
351    ///
352    /// # Examples
353    ///
354    /// ```
355    /// #![feature(nonpoison_mutex)]
356    ///
357    /// use std::sync::nonpoison::Mutex;
358    ///
359    /// let mut mutex = Mutex::new(0);
360    /// *mutex.get_mut() = 10;
361    /// assert_eq!(*mutex.lock(), 10);
362    /// ```
363    #[unstable(feature = "nonpoison_mutex", issue = "134645")]
364    pub fn get_mut(&mut self) -> &mut T {
365        self.data.get_mut()
366    }
367
368    /// Returns a raw pointer to the underlying data.
369    ///
370    /// The returned pointer is always non-null and properly aligned, but it is
371    /// the user's responsibility to ensure that any reads and writes through it
372    /// are properly synchronized to avoid data races, and that it is not read
373    /// or written through after the mutex is dropped.
374    #[unstable(feature = "mutex_data_ptr", issue = "140368")]
375    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
376    pub const fn data_ptr(&self) -> *mut T {
377        self.data.get()
378    }
379
380    /// Acquires the mutex and provides mutable access to the underlying data by passing
381    /// a mutable reference to the given closure.
382    ///
383    /// This method acquires the lock, calls the provided closure with a mutable reference
384    /// to the data, and returns the result of the closure. The lock is released after
385    /// the closure completes, even if it panics.
386    ///
387    /// # Examples
388    ///
389    /// ```
390    /// #![feature(lock_value_accessors, nonpoison_mutex)]
391    ///
392    /// use std::sync::nonpoison::Mutex;
393    ///
394    /// let mutex = Mutex::new(2);
395    ///
396    /// let result = mutex.with_mut(|data| {
397    ///     *data += 3;
398    ///
399    ///     *data + 5
400    /// });
401    ///
402    /// assert_eq!(*mutex.lock(), 5);
403    /// assert_eq!(result, 10);
404    /// ```
405    #[unstable(feature = "lock_value_accessors", issue = "133407")]
406    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
407    pub fn with_mut<F, R>(&self, f: F) -> R
408    where
409        F: FnOnce(&mut T) -> R,
410    {
411        f(&mut self.lock())
412    }
413}
414
415#[unstable(feature = "nonpoison_mutex", issue = "134645")]
416impl<T> From<T> for Mutex<T> {
417    /// Creates a new mutex in an unlocked state ready for use.
418    /// This is equivalent to [`Mutex::new`].
419    fn from(t: T) -> Self {
420        Mutex::new(t)
421    }
422}
423
424#[unstable(feature = "nonpoison_mutex", issue = "134645")]
425impl<T: Default> Default for Mutex<T> {
426    /// Creates a `Mutex<T>`, with the `Default` value for T.
427    fn default() -> Mutex<T> {
428        Mutex::new(Default::default())
429    }
430}
431
432#[unstable(feature = "nonpoison_mutex", issue = "134645")]
433impl<T: ?Sized + fmt::Debug> fmt::Debug for Mutex<T> {
434    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
435        let mut d = f.debug_struct("Mutex");
436        match self.try_lock() {
437            Ok(guard) => {
438                d.field("data", &&*guard);
439            }
440            Err(WouldBlock) => {
441                d.field("data", &"<locked>");
442            }
443        }
444        d.finish_non_exhaustive()
445    }
446}
447
448impl<'mutex, T: ?Sized> MutexGuard<'mutex, T> {
449    unsafe fn new(lock: &'mutex Mutex<T>) -> MutexGuard<'mutex, T> {
450        return MutexGuard { lock };
451    }
452}
453
454#[unstable(feature = "nonpoison_mutex", issue = "134645")]
455impl<T: ?Sized> Deref for MutexGuard<'_, T> {
456    type Target = T;
457
458    fn deref(&self) -> &T {
459        unsafe { &*self.lock.data.get() }
460    }
461}
462
463#[unstable(feature = "nonpoison_mutex", issue = "134645")]
464impl<T: ?Sized> DerefMut for MutexGuard<'_, T> {
465    fn deref_mut(&mut self) -> &mut T {
466        unsafe { &mut *self.lock.data.get() }
467    }
468}
469
470#[unstable(feature = "nonpoison_mutex", issue = "134645")]
471impl<T: ?Sized> Drop for MutexGuard<'_, T> {
472    #[inline]
473    fn drop(&mut self) {
474        unsafe {
475            self.lock.inner.unlock();
476        }
477    }
478}
479
480#[unstable(feature = "nonpoison_mutex", issue = "134645")]
481impl<T: ?Sized + fmt::Debug> fmt::Debug for MutexGuard<'_, T> {
482    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
483        fmt::Debug::fmt(&**self, f)
484    }
485}
486
487#[unstable(feature = "nonpoison_mutex", issue = "134645")]
488impl<T: ?Sized + fmt::Display> fmt::Display for MutexGuard<'_, T> {
489    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
490        (**self).fmt(f)
491    }
492}
493
494/// For use in [`nonpoison::condvar`](super::condvar).
495pub(super) fn guard_lock<'a, T: ?Sized>(guard: &MutexGuard<'a, T>) -> &'a sys::Mutex {
496    &guard.lock.inner
497}
498
499impl<'a, T: ?Sized> MutexGuard<'a, T> {
500    /// Makes a [`MappedMutexGuard`] for a component of the borrowed data, e.g.
501    /// an enum variant.
502    ///
503    /// The `Mutex` is already locked, so this cannot fail.
504    ///
505    /// This is an associated function that needs to be used as
506    /// `MutexGuard::map(...)`. A method would interfere with methods of the
507    /// same name on the contents of the `MutexGuard` used through `Deref`.
508    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
509    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
510    pub fn map<U, F>(orig: Self, f: F) -> MappedMutexGuard<'a, U>
511    where
512        F: FnOnce(&mut T) -> &mut U,
513        U: ?Sized,
514    {
515        // SAFETY: the conditions of `MutexGuard::new` were satisfied when the original guard
516        // was created, and have been upheld throughout `map` and/or `filter_map`.
517        // The signature of the closure guarantees that it will not "leak" the lifetime of the reference
518        // passed to it. If the closure panics, the guard will be dropped.
519        let data = NonNull::from(f(unsafe { &mut *orig.lock.data.get() }));
520        let orig = ManuallyDrop::new(orig);
521        MappedMutexGuard { data, inner: &orig.lock.inner, _variance: PhantomData }
522    }
523
524    /// Makes a [`MappedMutexGuard`] for a component of the borrowed data. The
525    /// original guard is returned as an `Err(...)` if the closure returns
526    /// `None`.
527    ///
528    /// The `Mutex` is already locked, so this cannot fail.
529    ///
530    /// This is an associated function that needs to be used as
531    /// `MutexGuard::filter_map(...)`. A method would interfere with methods of the
532    /// same name on the contents of the `MutexGuard` used through `Deref`.
533    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
534    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
535    pub fn filter_map<U, F>(orig: Self, f: F) -> Result<MappedMutexGuard<'a, U>, Self>
536    where
537        F: FnOnce(&mut T) -> Option<&mut U>,
538        U: ?Sized,
539    {
540        // SAFETY: the conditions of `MutexGuard::new` were satisfied when the original guard
541        // was created, and have been upheld throughout `map` and/or `filter_map`.
542        // The signature of the closure guarantees that it will not "leak" the lifetime of the reference
543        // passed to it. If the closure panics, the guard will be dropped.
544        match f(unsafe { &mut *orig.lock.data.get() }) {
545            Some(data) => {
546                let data = NonNull::from(data);
547                let orig = ManuallyDrop::new(orig);
548                Ok(MappedMutexGuard { data, inner: &orig.lock.inner, _variance: PhantomData })
549            }
550            None => Err(orig),
551        }
552    }
553}
554
555#[unstable(feature = "mapped_lock_guards", issue = "117108")]
556impl<T: ?Sized> Deref for MappedMutexGuard<'_, T> {
557    type Target = T;
558
559    fn deref(&self) -> &T {
560        unsafe { self.data.as_ref() }
561    }
562}
563
564#[unstable(feature = "mapped_lock_guards", issue = "117108")]
565impl<T: ?Sized> DerefMut for MappedMutexGuard<'_, T> {
566    fn deref_mut(&mut self) -> &mut T {
567        unsafe { self.data.as_mut() }
568    }
569}
570
571#[unstable(feature = "mapped_lock_guards", issue = "117108")]
572impl<T: ?Sized> Drop for MappedMutexGuard<'_, T> {
573    #[inline]
574    fn drop(&mut self) {
575        unsafe {
576            self.inner.unlock();
577        }
578    }
579}
580
581#[unstable(feature = "mapped_lock_guards", issue = "117108")]
582impl<T: ?Sized + fmt::Debug> fmt::Debug for MappedMutexGuard<'_, T> {
583    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
584        fmt::Debug::fmt(&**self, f)
585    }
586}
587
588#[unstable(feature = "mapped_lock_guards", issue = "117108")]
589impl<T: ?Sized + fmt::Display> fmt::Display for MappedMutexGuard<'_, T> {
590    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
591        (**self).fmt(f)
592    }
593}
594
595impl<'a, T: ?Sized> MappedMutexGuard<'a, T> {
596    /// Makes a [`MappedMutexGuard`] for a component of the borrowed data, e.g.
597    /// an enum variant.
598    ///
599    /// The `Mutex` is already locked, so this cannot fail.
600    ///
601    /// This is an associated function that needs to be used as
602    /// `MappedMutexGuard::map(...)`. A method would interfere with methods of the
603    /// same name on the contents of the `MutexGuard` used through `Deref`.
604    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
605    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
606    pub fn map<U, F>(mut orig: Self, f: F) -> MappedMutexGuard<'a, U>
607    where
608        F: FnOnce(&mut T) -> &mut U,
609        U: ?Sized,
610    {
611        // SAFETY: the conditions of `MutexGuard::new` were satisfied when the original guard
612        // was created, and have been upheld throughout `map` and/or `filter_map`.
613        // The signature of the closure guarantees that it will not "leak" the lifetime of the reference
614        // passed to it. If the closure panics, the guard will be dropped.
615        let data = NonNull::from(f(unsafe { orig.data.as_mut() }));
616        let orig = ManuallyDrop::new(orig);
617        MappedMutexGuard { data, inner: orig.inner, _variance: PhantomData }
618    }
619
620    /// Makes a [`MappedMutexGuard`] for a component of the borrowed data. The
621    /// original guard is returned as an `Err(...)` if the closure returns
622    /// `None`.
623    ///
624    /// The `Mutex` is already locked, so this cannot fail.
625    ///
626    /// This is an associated function that needs to be used as
627    /// `MappedMutexGuard::filter_map(...)`. A method would interfere with methods of the
628    /// same name on the contents of the `MutexGuard` used through `Deref`.
629    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
630    // #[unstable(feature = "nonpoison_mutex", issue = "134645")]
631    pub fn filter_map<U, F>(mut orig: Self, f: F) -> Result<MappedMutexGuard<'a, U>, Self>
632    where
633        F: FnOnce(&mut T) -> Option<&mut U>,
634        U: ?Sized,
635    {
636        // SAFETY: the conditions of `MutexGuard::new` were satisfied when the original guard
637        // was created, and have been upheld throughout `map` and/or `filter_map`.
638        // The signature of the closure guarantees that it will not "leak" the lifetime of the reference
639        // passed to it. If the closure panics, the guard will be dropped.
640        match f(unsafe { orig.data.as_mut() }) {
641            Some(data) => {
642                let data = NonNull::from(data);
643                let orig = ManuallyDrop::new(orig);
644                Ok(MappedMutexGuard { data, inner: orig.inner, _variance: PhantomData })
645            }
646            None => Err(orig),
647        }
648    }
649}
````