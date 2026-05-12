---
title: rwlock.rs - source
url: https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#1191
source: crawler
fetched_at: 2026-05-06T21:36:33.060552208-03:00
rendered_js: false
word_count: 6489
summary: This document defines the RwLock structure, a thread-synchronization primitive that allows multiple concurrent readers or exclusive access for a single writer, including details on poisoning and RAII guards.
tags:
    - rust
    - concurrency
    - rwlock
    - synchronization
    - thread-safety
    - raii
category: reference
---

## std/sync/poison/ rwlock.rs

````rust
1use crate::cell::UnsafeCell;
2use crate::fmt;
3use crate::marker::PhantomData;
4use crate::mem::{self, ManuallyDrop, forget};
5use crate::ops::{Deref, DerefMut};
6use crate::ptr::NonNull;
7use crate::sync::{LockResult, PoisonError, TryLockError, TryLockResult, poison};
8use crate::sys::sync as sys;
9
10/// A reader-writer lock
11///
12/// This type of lock allows a number of readers or at most one writer at any
13/// point in time. The write portion of this lock typically allows modification
14/// of the underlying data (exclusive access) and the read portion of this lock
15/// typically allows for read-only access (shared access).
16///
17/// In comparison, a [`Mutex`] does not distinguish between readers or writers
18/// that acquire the lock, therefore blocking any threads waiting for the lock to
19/// become available. An `RwLock` will allow any number of readers to acquire the
20/// lock as long as a writer is not holding the lock.
21///
22/// The priority policy of the lock is dependent on the underlying operating
23/// system's implementation, and this type does not guarantee that any
24/// particular policy will be used. In particular, a writer which is waiting to
25/// acquire the lock in `write` might or might not block concurrent calls to
26/// `read`, e.g.:
27///
28/// <details><summary>Potential deadlock example</summary>
29///
30/// ```text
31/// // Thread 1              |  // Thread 2
32/// let _rg1 = lock.read();  |
33///                          |  // will block
34///                          |  let _wg = lock.write();
35/// // may deadlock          |
36/// let _rg2 = lock.read();  |
37/// ```
38///
39/// </details>
40///
41/// The type parameter `T` represents the data that this lock protects. It is
42/// required that `T` satisfies [`Send`] to be shared across threads and
43/// [`Sync`] to allow concurrent access through readers. The RAII guards
44/// returned from the locking methods implement [`Deref`] (and [`DerefMut`]
45/// for the `write` methods) to allow access to the content of the lock.
46///
47/// # Poisoning
48///
49/// An `RwLock`, like [`Mutex`], will [usually] become poisoned on a panic. Note,
50/// however, that an `RwLock` may only be poisoned if a panic occurs while it is
51/// locked exclusively (write mode). If a panic occurs in any reader, then the
52/// lock will not be poisoned.
53///
54/// [usually]: super::Mutex#poisoning
55///
56/// # Examples
57///
58/// ```
59/// use std::sync::{Arc, RwLock};
60/// use std::thread;
61/// use std::time::Duration;
62///
63/// let data = Arc::new(RwLock::new(5));
64///
65/// // Multiple readers can access in parallel.
66/// for i in 0..3 {
67///     let lock_clone = Arc::clone(&data);
68///
69///     thread::spawn(move || {
70///         let value = lock_clone.read().unwrap();
71///
72///         println!("Reader {}: Read value {}, now holding lock...", i, *value);
73///
74///         // Simulating a long read operation
75///         thread::sleep(Duration::from_secs(1));
76///
77///         println!("Reader {}: Dropping lock.", i);
78///         // Read lock unlocked when going out of scope.
79///     });
80/// }
81///
82/// thread::sleep(Duration::from_millis(100));  // Wait for readers to start
83///
84/// // While all readers can proceed, a call to .write() has to wait for
85//  // current active reader locks.
86/// let mut writable_data = data.write().unwrap();
87/// println!("Writer proceeds...");
88/// *writable_data += 1;
89/// ```
90///
91/// [`Mutex`]: super::Mutex
92#[stable(feature = "rust1", since = "1.0.0")]
93#[cfg_attr(not(test), rustc_diagnostic_item = "RwLock")]
94pub struct RwLock<T: ?Sized> {
95    /// The inner [`sys::RwLock`] that synchronizes thread access to the protected data.
96    inner: sys::RwLock,
97    /// A flag denoting if this `RwLock` has been poisoned.
98    poison: poison::Flag,
99    /// The lock-protected data.
100    data: UnsafeCell<T>,
101}
102
103#[stable(feature = "rust1", since = "1.0.0")]
104unsafe impl<T: ?Sized + Send> Send for RwLock<T> {}
105
106#[stable(feature = "rust1", since = "1.0.0")]
107unsafe impl<T: ?Sized + Send + Sync> Sync for RwLock<T> {}
108
109////////////////////////////////////////////////////////////////////////////////////////////////////
110// Guards
111////////////////////////////////////////////////////////////////////////////////////////////////////
112
113/// RAII structure used to release the shared read access of a lock when
114/// dropped.
115///
116/// This structure is created by the [`read`] and [`try_read`] methods on
117/// [`RwLock`].
118///
119/// [`read`]: RwLock::read
120/// [`try_read`]: RwLock::try_read
121#[must_use = "if unused the RwLock will immediately unlock"]
122#[must_not_suspend = "holding a RwLockReadGuard across suspend \
123                      points can cause deadlocks, delays, \
124                      and cause Futures to not implement `Send`"]
125#[stable(feature = "rust1", since = "1.0.0")]
126#[clippy::has_significant_drop]
127#[cfg_attr(not(test), rustc_diagnostic_item = "RwLockReadGuard")]
128pub struct RwLockReadGuard<'rwlock, T: ?Sized + 'rwlock> {
129    /// A pointer to the data protected by the `RwLock`. Note that we use a pointer here instead of
130    /// `&'rwlock T` to avoid `noalias` violations, because a `RwLockReadGuard` instance only holds
131    /// immutability until it drops, not for its whole scope.
132    /// `NonNull` is preferable over `*const T` to allow for niche optimizations. `NonNull` is also
133    /// covariant over `T`, just like we would have with `&T`.
134    data: NonNull<T>,
135    /// A reference to the internal [`sys::RwLock`] that we have read-locked.
136    inner_lock: &'rwlock sys::RwLock,
137}
138
139#[stable(feature = "rust1", since = "1.0.0")]
140impl<T: ?Sized> !Send for RwLockReadGuard<'_, T> {}
141
142#[stable(feature = "rwlock_guard_sync", since = "1.23.0")]
143unsafe impl<T: ?Sized + Sync> Sync for RwLockReadGuard<'_, T> {}
144
145/// RAII structure used to release the exclusive write access of a lock when
146/// dropped.
147///
148/// This structure is created by the [`write`] and [`try_write`] methods
149/// on [`RwLock`].
150///
151/// [`write`]: RwLock::write
152/// [`try_write`]: RwLock::try_write
153#[must_use = "if unused the RwLock will immediately unlock"]
154#[must_not_suspend = "holding a RwLockWriteGuard across suspend \
155                      points can cause deadlocks, delays, \
156                      and cause Future's to not implement `Send`"]
157#[stable(feature = "rust1", since = "1.0.0")]
158#[clippy::has_significant_drop]
159#[cfg_attr(not(test), rustc_diagnostic_item = "RwLockWriteGuard")]
160pub struct RwLockWriteGuard<'rwlock, T: ?Sized + 'rwlock> {
161    /// A reference to the [`RwLock`] that we have write-locked.
162    lock: &'rwlock RwLock<T>,
163    /// The poison guard. See the [`poison`] module for more information.
164    poison: poison::Guard,
165}
166
167#[stable(feature = "rust1", since = "1.0.0")]
168impl<T: ?Sized> !Send for RwLockWriteGuard<'_, T> {}
169
170#[stable(feature = "rwlock_guard_sync", since = "1.23.0")]
171unsafe impl<T: ?Sized + Sync> Sync for RwLockWriteGuard<'_, T> {}
172
173/// RAII structure used to release the shared read access of a lock when
174/// dropped, which can point to a subfield of the protected data.
175///
176/// This structure is created by the [`map`] and [`filter_map`] methods
177/// on [`RwLockReadGuard`].
178///
179/// [`map`]: RwLockReadGuard::map
180/// [`filter_map`]: RwLockReadGuard::filter_map
181#[must_use = "if unused the RwLock will immediately unlock"]
182#[must_not_suspend = "holding a MappedRwLockReadGuard across suspend \
183                      points can cause deadlocks, delays, \
184                      and cause Futures to not implement `Send`"]
185#[unstable(feature = "mapped_lock_guards", issue = "117108")]
186#[clippy::has_significant_drop]
187pub struct MappedRwLockReadGuard<'rwlock, T: ?Sized + 'rwlock> {
188    /// A pointer to the data protected by the `RwLock`. Note that we use a pointer here instead of
189    /// `&'rwlock T` to avoid `noalias` violations, because a `MappedRwLockReadGuard` instance only
190    /// holds immutability until it drops, not for its whole scope.
191    /// `NonNull` is preferable over `*const T` to allow for niche optimizations. `NonNull` is also
192    /// covariant over `T`, just like we would have with `&T`.
193    data: NonNull<T>,
194    /// A reference to the internal [`sys::RwLock`] that we have read-locked.
195    inner_lock: &'rwlock sys::RwLock,
196}
197
198#[unstable(feature = "mapped_lock_guards", issue = "117108")]
199impl<T: ?Sized> !Send for MappedRwLockReadGuard<'_, T> {}
200
201#[unstable(feature = "mapped_lock_guards", issue = "117108")]
202unsafe impl<T: ?Sized + Sync> Sync for MappedRwLockReadGuard<'_, T> {}
203
204/// RAII structure used to release the exclusive write access of a lock when
205/// dropped, which can point to a subfield of the protected data.
206///
207/// This structure is created by the [`map`] and [`filter_map`] methods
208/// on [`RwLockWriteGuard`].
209///
210/// [`map`]: RwLockWriteGuard::map
211/// [`filter_map`]: RwLockWriteGuard::filter_map
212#[must_use = "if unused the RwLock will immediately unlock"]
213#[must_not_suspend = "holding a MappedRwLockWriteGuard across suspend \
214                      points can cause deadlocks, delays, \
215                      and cause Future's to not implement `Send`"]
216#[unstable(feature = "mapped_lock_guards", issue = "117108")]
217#[clippy::has_significant_drop]
218pub struct MappedRwLockWriteGuard<'rwlock, T: ?Sized + 'rwlock> {
219    /// A pointer to the data protected by the `RwLock`. Note that we use a pointer here instead of
220    /// `&'rwlock T` to avoid `noalias` violations, because a `MappedRwLockWriteGuard` instance only
221    /// holds uniquneness until it drops, not for its whole scope.
222    /// `NonNull` is preferable over `*const T` to allow for niche optimizations.
223    data: NonNull<T>,
224    /// `NonNull` is covariant over `T`, so we add a `PhantomData<&'rwlock mut T>` field here to
225    /// enforce the correct invariance over `T`.
226    _variance: PhantomData<&'rwlock mut T>,
227    /// A reference to the internal [`sys::RwLock`] that we have write-locked.
228    inner_lock: &'rwlock sys::RwLock,
229    /// A reference to the original `RwLock`'s poison state.
230    poison_flag: &'rwlock poison::Flag,
231    /// The poison guard. See the [`poison`] module for more information.
232    poison_guard: poison::Guard,
233}
234
235#[unstable(feature = "mapped_lock_guards", issue = "117108")]
236impl<T: ?Sized> !Send for MappedRwLockWriteGuard<'_, T> {}
237
238#[unstable(feature = "mapped_lock_guards", issue = "117108")]
239unsafe impl<T: ?Sized + Sync> Sync for MappedRwLockWriteGuard<'_, T> {}
240
241////////////////////////////////////////////////////////////////////////////////////////////////////
242// Implementations
243////////////////////////////////////////////////////////////////////////////////////////////////////
244
245impl<T> RwLock<T> {
246    /// Creates a new instance of an `RwLock<T>` which is unlocked.
247    ///
248    /// # Examples
249    ///
250    /// ```
251    /// use std::sync::RwLock;
252    ///
253    /// let lock = RwLock::new(5);
254    /// ```
255    #[stable(feature = "rust1", since = "1.0.0")]
256    #[rustc_const_stable(feature = "const_locks", since = "1.63.0")]
257    #[inline]
258    pub const fn new(t: T) -> RwLock<T> {
259        RwLock { inner: sys::RwLock::new(), poison: poison::Flag::new(), data: UnsafeCell::new(t) }
260    }
261
262    /// Returns the contained value by cloning it.
263    ///
264    /// # Errors
265    ///
266    /// This function will return an error if the `RwLock` is poisoned. An
267    /// `RwLock` is poisoned whenever a writer panics while holding an exclusive
268    /// lock.
269    ///
270    /// # Examples
271    ///
272    /// ```
273    /// #![feature(lock_value_accessors)]
274    ///
275    /// use std::sync::RwLock;
276    ///
277    /// let mut lock = RwLock::new(7);
278    ///
279    /// assert_eq!(lock.get_cloned().unwrap(), 7);
280    /// ```
281    #[unstable(feature = "lock_value_accessors", issue = "133407")]
282    pub fn get_cloned(&self) -> Result<T, PoisonError<()>>
283    where
284        T: Clone,
285    {
286        match self.read() {
287            Ok(guard) => Ok((*guard).clone()),
288            Err(_) => Err(PoisonError::new(())),
289        }
290    }
291
292    /// Sets the contained value.
293    ///
294    /// # Errors
295    ///
296    /// This function will return an error containing the provided `value` if
297    /// the `RwLock` is poisoned. An `RwLock` is poisoned whenever a writer
298    /// panics while holding an exclusive lock.
299    ///
300    /// # Examples
301    ///
302    /// ```
303    /// #![feature(lock_value_accessors)]
304    ///
305    /// use std::sync::RwLock;
306    ///
307    /// let mut lock = RwLock::new(7);
308    ///
309    /// assert_eq!(lock.get_cloned().unwrap(), 7);
310    /// lock.set(11).unwrap();
311    /// assert_eq!(lock.get_cloned().unwrap(), 11);
312    /// ```
313    #[unstable(feature = "lock_value_accessors", issue = "133407")]
314    #[rustc_should_not_be_called_on_const_items]
315    pub fn set(&self, value: T) -> Result<(), PoisonError<T>> {
316        if mem::needs_drop::<T>() {
317            // If the contained value has non-trivial destructor, we
318            // call that destructor after the lock being released.
319            self.replace(value).map(drop)
320        } else {
321            match self.write() {
322                Ok(mut guard) => {
323                    *guard = value;
324
325                    Ok(())
326                }
327                Err(_) => Err(PoisonError::new(value)),
328            }
329        }
330    }
331
332    /// Replaces the contained value with `value`, and returns the old contained value.
333    ///
334    /// # Errors
335    ///
336    /// This function will return an error containing the provided `value` if
337    /// the `RwLock` is poisoned. An `RwLock` is poisoned whenever a writer
338    /// panics while holding an exclusive lock.
339    ///
340    /// # Examples
341    ///
342    /// ```
343    /// #![feature(lock_value_accessors)]
344    ///
345    /// use std::sync::RwLock;
346    ///
347    /// let mut lock = RwLock::new(7);
348    ///
349    /// assert_eq!(lock.replace(11).unwrap(), 7);
350    /// assert_eq!(lock.get_cloned().unwrap(), 11);
351    /// ```
352    #[unstable(feature = "lock_value_accessors", issue = "133407")]
353    #[rustc_should_not_be_called_on_const_items]
354    pub fn replace(&self, value: T) -> LockResult<T> {
355        match self.write() {
356            Ok(mut guard) => Ok(mem::replace(&mut *guard, value)),
357            Err(_) => Err(PoisonError::new(value)),
358        }
359    }
360}
361
362impl<T: ?Sized> RwLock<T> {
363    /// Locks this `RwLock` with shared read access, blocking the current thread
364    /// until it can be acquired.
365    ///
366    /// The calling thread will be blocked until there are no more writers which
367    /// hold the lock. There may be other readers currently inside the lock when
368    /// this method returns. This method does not provide any guarantees with
369    /// respect to the ordering of whether contentious readers or writers will
370    /// acquire the lock first.
371    ///
372    /// Returns an RAII guard which will release this thread's shared access
373    /// once it is dropped.
374    ///
375    /// # Errors
376    ///
377    /// This function will return an error if the `RwLock` is poisoned. An
378    /// `RwLock` is poisoned whenever a writer panics while holding an exclusive
379    /// lock. The failure will occur immediately after the lock has been
380    /// acquired. The acquired lock guard will be contained in the returned
381    /// error.
382    ///
383    /// # Panics
384    ///
385    /// This function might panic when called if the lock is already held by the current thread
386    /// in read or write mode.
387    ///
388    /// # Examples
389    ///
390    /// ```
391    /// use std::sync::{Arc, RwLock};
392    /// use std::thread;
393    ///
394    /// let lock = Arc::new(RwLock::new(1));
395    /// let c_lock = Arc::clone(&lock);
396    ///
397    /// let n = lock.read().unwrap();
398    /// assert_eq!(*n, 1);
399    ///
400    /// thread::spawn(move || {
401    ///     let r = c_lock.read();
402    ///     assert!(r.is_ok());
403    /// }).join().unwrap();
404    /// ```
405    #[inline]
406    #[stable(feature = "rust1", since = "1.0.0")]
407    #[rustc_should_not_be_called_on_const_items]
408    pub fn read(&self) -> LockResult<RwLockReadGuard<'_, T>> {
409        unsafe {
410            self.inner.read();
411            RwLockReadGuard::new(self)
412        }
413    }
414
415    /// Attempts to acquire this `RwLock` with shared read access.
416    ///
417    /// If the access could not be granted at this time, then `Err` is returned.
418    /// Otherwise, an RAII guard is returned which will release the shared access
419    /// when it is dropped.
420    ///
421    /// This function does not block.
422    ///
423    /// This function does not provide any guarantees with respect to the ordering
424    /// of whether contentious readers or writers will acquire the lock first.
425    ///
426    /// # Errors
427    ///
428    /// This function will return the [`Poisoned`] error if the `RwLock` is
429    /// poisoned. An `RwLock` is poisoned whenever a writer panics while holding
430    /// an exclusive lock. `Poisoned` will only be returned if the lock would
431    /// have otherwise been acquired. An acquired lock guard will be contained
432    /// in the returned error.
433    ///
434    /// This function will return the [`WouldBlock`] error if the `RwLock` could
435    /// not be acquired because it was already locked exclusively.
436    ///
437    /// [`Poisoned`]: TryLockError::Poisoned
438    /// [`WouldBlock`]: TryLockError::WouldBlock
439    ///
440    /// # Examples
441    ///
442    /// ```
443    /// use std::sync::RwLock;
444    ///
445    /// let lock = RwLock::new(1);
446    ///
447    /// match lock.try_read() {
448    ///     Ok(n) => assert_eq!(*n, 1),
449    ///     Err(_) => unreachable!(),
450    /// };
451    /// ```
452    #[inline]
453    #[stable(feature = "rust1", since = "1.0.0")]
454    #[rustc_should_not_be_called_on_const_items]
455    pub fn try_read(&self) -> TryLockResult<RwLockReadGuard<'_, T>> {
456        unsafe {
457            if self.inner.try_read() {
458                Ok(RwLockReadGuard::new(self)?)
459            } else {
460                Err(TryLockError::WouldBlock)
461            }
462        }
463    }
464
465    /// Locks this `RwLock` with exclusive write access, blocking the current
466    /// thread until it can be acquired.
467    ///
468    /// This function will not return while other writers or other readers
469    /// currently have access to the lock.
470    ///
471    /// Returns an RAII guard which will drop the write access of this `RwLock`
472    /// when dropped.
473    ///
474    /// # Errors
475    ///
476    /// This function will return an error if the `RwLock` is poisoned. An
477    /// `RwLock` is poisoned whenever a writer panics while holding an exclusive
478    /// lock. An error will be returned when the lock is acquired. The acquired
479    /// lock guard will be contained in the returned error.
480    ///
481    /// # Panics
482    ///
483    /// This function might panic when called if the lock is already held by the current thread
484    /// in read or write mode.
485    ///
486    /// # Examples
487    ///
488    /// ```
489    /// use std::sync::RwLock;
490    ///
491    /// let lock = RwLock::new(1);
492    ///
493    /// let mut n = lock.write().unwrap();
494    /// *n = 2;
495    ///
496    /// assert!(lock.try_read().is_err());
497    /// ```
498    #[inline]
499    #[stable(feature = "rust1", since = "1.0.0")]
500    #[rustc_should_not_be_called_on_const_items]
501    pub fn write(&self) -> LockResult<RwLockWriteGuard<'_, T>> {
502        unsafe {
503            self.inner.write();
504            RwLockWriteGuard::new(self)
505        }
506    }
507
508    /// Attempts to lock this `RwLock` with exclusive write access.
509    ///
510    /// If the lock could not be acquired at this time, then `Err` is returned.
511    /// Otherwise, an RAII guard is returned which will release the lock when
512    /// it is dropped.
513    ///
514    /// This function does not block.
515    ///
516    /// This function does not provide any guarantees with respect to the ordering
517    /// of whether contentious readers or writers will acquire the lock first.
518    ///
519    /// # Errors
520    ///
521    /// This function will return the [`Poisoned`] error if the `RwLock` is
522    /// poisoned. An `RwLock` is poisoned whenever a writer panics while holding
523    /// an exclusive lock. `Poisoned` will only be returned if the lock would
524    /// have otherwise been acquired. An acquired lock guard will be contained
525    /// in the returned error.
526    ///
527    /// This function will return the [`WouldBlock`] error if the `RwLock` could
528    /// not be acquired because it was already locked.
529    ///
530    /// [`Poisoned`]: TryLockError::Poisoned
531    /// [`WouldBlock`]: TryLockError::WouldBlock
532    ///
533    ///
534    /// # Examples
535    ///
536    /// ```
537    /// use std::sync::RwLock;
538    ///
539    /// let lock = RwLock::new(1);
540    ///
541    /// let n = lock.read().unwrap();
542    /// assert_eq!(*n, 1);
543    ///
544    /// assert!(lock.try_write().is_err());
545    /// ```
546    #[inline]
547    #[stable(feature = "rust1", since = "1.0.0")]
548    #[rustc_should_not_be_called_on_const_items]
549    pub fn try_write(&self) -> TryLockResult<RwLockWriteGuard<'_, T>> {
550        unsafe {
551            if self.inner.try_write() {
552                Ok(RwLockWriteGuard::new(self)?)
553            } else {
554                Err(TryLockError::WouldBlock)
555            }
556        }
557    }
558
559    /// Determines whether the lock is poisoned.
560    ///
561    /// If another thread is active, the lock can still become poisoned at any
562    /// time. You should not trust a `false` value for program correctness
563    /// without additional synchronization.
564    ///
565    /// # Examples
566    ///
567    /// ```
568    /// use std::sync::{Arc, RwLock};
569    /// use std::thread;
570    ///
571    /// let lock = Arc::new(RwLock::new(0));
572    /// let c_lock = Arc::clone(&lock);
573    ///
574    /// let _ = thread::spawn(move || {
575    ///     let _lock = c_lock.write().unwrap();
576    ///     panic!(); // the lock gets poisoned
577    /// }).join();
578    /// assert_eq!(lock.is_poisoned(), true);
579    /// ```
580    #[inline]
581    #[stable(feature = "sync_poison", since = "1.2.0")]
582    pub fn is_poisoned(&self) -> bool {
583        self.poison.get()
584    }
585
586    /// Clear the poisoned state from a lock.
587    ///
588    /// If the lock is poisoned, it will remain poisoned until this function is called. This allows
589    /// recovering from a poisoned state and marking that it has recovered. For example, if the
590    /// value is overwritten by a known-good value, then the lock can be marked as un-poisoned. Or
591    /// possibly, the value could be inspected to determine if it is in a consistent state, and if
592    /// so the poison is removed.
593    ///
594    /// # Examples
595    ///
596    /// ```
597    /// use std::sync::{Arc, RwLock};
598    /// use std::thread;
599    ///
600    /// let lock = Arc::new(RwLock::new(0));
601    /// let c_lock = Arc::clone(&lock);
602    ///
603    /// let _ = thread::spawn(move || {
604    ///     let _lock = c_lock.write().unwrap();
605    ///     panic!(); // the lock gets poisoned
606    /// }).join();
607    ///
608    /// assert_eq!(lock.is_poisoned(), true);
609    /// let guard = lock.write().unwrap_or_else(|mut e| {
610    ///     **e.get_mut() = 1;
611    ///     lock.clear_poison();
612    ///     e.into_inner()
613    /// });
614    /// assert_eq!(lock.is_poisoned(), false);
615    /// assert_eq!(*guard, 1);
616    /// ```
617    #[inline]
618    #[stable(feature = "mutex_unpoison", since = "1.77.0")]
619    pub fn clear_poison(&self) {
620        self.poison.clear();
621    }
622
623    /// Consumes this `RwLock`, returning the underlying data.
624    ///
625    /// # Errors
626    ///
627    /// This function will return an error containing the underlying data if
628    /// the `RwLock` is poisoned. An `RwLock` is poisoned whenever a writer
629    /// panics while holding an exclusive lock. An error will only be returned
630    /// if the lock would have otherwise been acquired.
631    ///
632    /// # Examples
633    ///
634    /// ```
635    /// use std::sync::RwLock;
636    ///
637    /// let lock = RwLock::new(String::new());
638    /// {
639    ///     let mut s = lock.write().unwrap();
640    ///     *s = "modified".to_owned();
641    /// }
642    /// assert_eq!(lock.into_inner().unwrap(), "modified");
643    /// ```
644    #[stable(feature = "rwlock_into_inner", since = "1.6.0")]
645    pub fn into_inner(self) -> LockResult<T>
646    where
647        T: Sized,
648    {
649        let data = self.data.into_inner();
650        poison::map_result(self.poison.borrow(), |()| data)
651    }
652
653    /// Returns a mutable reference to the underlying data.
654    ///
655    /// Since this call borrows the `RwLock` mutably, no actual locking needs to
656    /// take place -- the mutable borrow statically guarantees no new locks can be acquired
657    /// while this reference exists. Note that this method does not clear any previously abandoned
658    /// locks (e.g., via [`forget()`] on a [`RwLockReadGuard`] or [`RwLockWriteGuard`]).
659    ///
660    /// # Errors
661    ///
662    /// This function will return an error containing a mutable reference to
663    /// the underlying data if the `RwLock` is poisoned. An `RwLock` is
664    /// poisoned whenever a writer panics while holding an exclusive lock.
665    /// An error will only be returned if the lock would have otherwise been
666    /// acquired.
667    ///
668    /// # Examples
669    ///
670    /// ```
671    /// use std::sync::RwLock;
672    ///
673    /// let mut lock = RwLock::new(0);
674    /// *lock.get_mut().unwrap() = 10;
675    /// assert_eq!(*lock.read().unwrap(), 10);
676    /// ```
677    #[stable(feature = "rwlock_get_mut", since = "1.6.0")]
678    pub fn get_mut(&mut self) -> LockResult<&mut T> {
679        let data = self.data.get_mut();
680        poison::map_result(self.poison.borrow(), |()| data)
681    }
682
683    /// Returns a raw pointer to the underlying data.
684    ///
685    /// The returned pointer is always non-null and properly aligned, but it is
686    /// the user's responsibility to ensure that any reads and writes through it
687    /// are properly synchronized to avoid data races, and that it is not read
688    /// or written through after the lock is dropped.
689    #[unstable(feature = "rwlock_data_ptr", issue = "140368")]
690    pub const fn data_ptr(&self) -> *mut T {
691        self.data.get()
692    }
693}
694
695#[stable(feature = "rust1", since = "1.0.0")]
696impl<T: ?Sized + fmt::Debug> fmt::Debug for RwLock<T> {
697    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
698        let mut d = f.debug_struct("RwLock");
699        match self.try_read() {
700            Ok(guard) => {
701                d.field("data", &&*guard);
702            }
703            Err(TryLockError::Poisoned(err)) => {
704                d.field("data", &&**err.get_ref());
705            }
706            Err(TryLockError::WouldBlock) => {
707                d.field("data", &format_args!("<locked>"));
708            }
709        }
710        d.field("poisoned", &self.poison.get());
711        d.finish_non_exhaustive()
712    }
713}
714
715#[stable(feature = "rw_lock_default", since = "1.10.0")]
716impl<T: Default> Default for RwLock<T> {
717    /// Creates a new `RwLock<T>`, with the `Default` value for T.
718    fn default() -> RwLock<T> {
719        RwLock::new(Default::default())
720    }
721}
722
723#[stable(feature = "rw_lock_from", since = "1.24.0")]
724impl<T> From<T> for RwLock<T> {
725    /// Creates a new instance of an `RwLock<T>` which is unlocked.
726    /// This is equivalent to [`RwLock::new`].
727    fn from(t: T) -> Self {
728        RwLock::new(t)
729    }
730}
731
732impl<'rwlock, T: ?Sized> RwLockReadGuard<'rwlock, T> {
733    /// Creates a new instance of `RwLockReadGuard<T>` from a `RwLock<T>`.
734    ///
735    /// # Safety
736    ///
737    /// This function is safe if and only if the same thread has successfully and safely called
738    /// `lock.inner.read()`, `lock.inner.try_read()`, or `lock.inner.downgrade()` before
739    /// instantiating this object.
740    unsafe fn new(lock: &'rwlock RwLock<T>) -> LockResult<RwLockReadGuard<'rwlock, T>> {
741        poison::map_result(lock.poison.borrow(), |()| RwLockReadGuard {
742            data: unsafe { NonNull::new_unchecked(lock.data.get()) },
743            inner_lock: &lock.inner,
744        })
745    }
746
747    /// Makes a [`MappedRwLockReadGuard`] for a component of the borrowed data, e.g.
748    /// an enum variant.
749    ///
750    /// The `RwLock` is already locked for reading, so this cannot fail.
751    ///
752    /// This is an associated function that needs to be used as
753    /// `RwLockReadGuard::map(...)`. A method would interfere with methods of
754    /// the same name on the contents of the `RwLockReadGuard` used through
755    /// `Deref`.
756    ///
757    /// # Panics
758    ///
759    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will not be
760    /// poisoned.
761    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
762    pub fn map<U, F>(orig: Self, f: F) -> MappedRwLockReadGuard<'rwlock, U>
763    where
764        F: FnOnce(&T) -> &U,
765        U: ?Sized,
766    {
767        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
768        // was created, and have been upheld throughout `map` and/or `filter_map`.
769        // The signature of the closure guarantees that it will not "leak" the lifetime of the
770        // reference passed to it. If the closure panics, the guard will be dropped.
771        let data = NonNull::from(f(unsafe { orig.data.as_ref() }));
772        let orig = ManuallyDrop::new(orig);
773        MappedRwLockReadGuard { data, inner_lock: &orig.inner_lock }
774    }
775
776    /// Makes a [`MappedRwLockReadGuard`] for a component of the borrowed data. The
777    /// original guard is returned as an `Err(...)` if the closure returns
778    /// `None`.
779    ///
780    /// The `RwLock` is already locked for reading, so this cannot fail.
781    ///
782    /// This is an associated function that needs to be used as
783    /// `RwLockReadGuard::filter_map(...)`. A method would interfere with methods
784    /// of the same name on the contents of the `RwLockReadGuard` used through
785    /// `Deref`.
786    ///
787    /// # Panics
788    ///
789    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will not be
790    /// poisoned.
791    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
792    pub fn filter_map<U, F>(orig: Self, f: F) -> Result<MappedRwLockReadGuard<'rwlock, U>, Self>
793    where
794        F: FnOnce(&T) -> Option<&U>,
795        U: ?Sized,
796    {
797        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
798        // was created, and have been upheld throughout `map` and/or `filter_map`.
799        // The signature of the closure guarantees that it will not "leak" the lifetime of the
800        // reference passed to it. If the closure panics, the guard will be dropped.
801        match f(unsafe { orig.data.as_ref() }) {
802            Some(data) => {
803                let data = NonNull::from(data);
804                let orig = ManuallyDrop::new(orig);
805                Ok(MappedRwLockReadGuard { data, inner_lock: &orig.inner_lock })
806            }
807            None => Err(orig),
808        }
809    }
810}
811
812impl<'rwlock, T: ?Sized> RwLockWriteGuard<'rwlock, T> {
813    /// Creates a new instance of `RwLockWriteGuard<T>` from a `RwLock<T>`.
814    ///
815    /// # Safety
816    ///
817    /// This function is safe if and only if the same thread has successfully and safely called
818    /// `lock.inner.write()`, `lock.inner.try_write()`, or `lock.inner.try_upgrade` before
819    /// instantiating this object.
820    unsafe fn new(lock: &'rwlock RwLock<T>) -> LockResult<RwLockWriteGuard<'rwlock, T>> {
821        poison::map_result(lock.poison.guard(), |guard| RwLockWriteGuard { lock, poison: guard })
822    }
823
824    /// Downgrades a write-locked `RwLockWriteGuard` into a read-locked [`RwLockReadGuard`].
825    ///
826    /// Since we have the `RwLockWriteGuard`, the [`RwLock`] must already be locked for writing, so
827    /// this method cannot fail.
828    ///
829    /// After downgrading, other readers will be allowed to read the protected data.
830    ///
831    /// # Examples
832    ///
833    /// `downgrade` takes ownership of the `RwLockWriteGuard` and returns a [`RwLockReadGuard`].
834    ///
835    /// ```
836    /// use std::sync::{RwLock, RwLockWriteGuard};
837    ///
838    /// let rw = RwLock::new(0);
839    ///
840    /// let mut write_guard = rw.write().unwrap();
841    /// *write_guard = 42;
842    ///
843    /// let read_guard = RwLockWriteGuard::downgrade(write_guard);
844    /// assert_eq!(42, *read_guard);
845    /// ```
846    ///
847    /// `downgrade` will _atomically_ change the state of the [`RwLock`] from exclusive mode into
848    /// shared mode. This means that it is impossible for another writing thread to get in between a
849    /// thread calling `downgrade` and any reads it performs after downgrading.
850    ///
851    /// ```
852    /// use std::sync::{Arc, RwLock, RwLockWriteGuard};
853    ///
854    /// let rw = Arc::new(RwLock::new(1));
855    ///
856    /// // Put the lock in write mode.
857    /// let mut main_write_guard = rw.write().unwrap();
858    ///
859    /// let rw_clone = rw.clone();
860    /// let evil_handle = std::thread::spawn(move || {
861    ///     // This will not return until the main thread drops the `main_read_guard`.
862    ///     let mut evil_guard = rw_clone.write().unwrap();
863    ///
864    ///     assert_eq!(*evil_guard, 2);
865    ///     *evil_guard = 3;
866    /// });
867    ///
868    /// *main_write_guard = 2;
869    ///
870    /// // Atomically downgrade the write guard into a read guard.
871    /// let main_read_guard = RwLockWriteGuard::downgrade(main_write_guard);
872    ///
873    /// // Since `downgrade` is atomic, the writer thread cannot have changed the protected data.
874    /// assert_eq!(*main_read_guard, 2, "`downgrade` was not atomic");
875    /// #
876    /// # drop(main_read_guard);
877    /// # evil_handle.join().unwrap();
878    /// #
879    /// # let final_check = rw.read().unwrap();
880    /// # assert_eq!(*final_check, 3);
881    /// ```
882    #[stable(feature = "rwlock_downgrade", since = "1.92.0")]
883    pub fn downgrade(s: Self) -> RwLockReadGuard<'rwlock, T> {
884        let lock = s.lock;
885
886        // We don't want to call the destructor since that calls `write_unlock`.
887        forget(s);
888
889        // SAFETY: We take ownership of a write guard, so we must already have the `RwLock` in write
890        // mode, satisfying the `downgrade` contract.
891        unsafe { lock.inner.downgrade() };
892
893        // SAFETY: We have just successfully called `downgrade`, so we fulfill the safety contract.
894        unsafe { RwLockReadGuard::new(lock).unwrap_or_else(PoisonError::into_inner) }
895    }
896
897    /// Makes a [`MappedRwLockWriteGuard`] for a component of the borrowed data, e.g.
898    /// an enum variant.
899    ///
900    /// The `RwLock` is already locked for writing, so this cannot fail.
901    ///
902    /// This is an associated function that needs to be used as
903    /// `RwLockWriteGuard::map(...)`. A method would interfere with methods of
904    /// the same name on the contents of the `RwLockWriteGuard` used through
905    /// `Deref`.
906    ///
907    /// # Panics
908    ///
909    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.
910    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
911    pub fn map<U, F>(orig: Self, f: F) -> MappedRwLockWriteGuard<'rwlock, U>
912    where
913        F: FnOnce(&mut T) -> &mut U,
914        U: ?Sized,
915    {
916        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
917        // was created, and have been upheld throughout `map` and/or `filter_map`.
918        // The signature of the closure guarantees that it will not "leak" the lifetime of the
919        // reference passed to it. If the closure panics, the guard will be dropped.
920        let data = NonNull::from(f(unsafe { &mut *orig.lock.data.get() }));
921        let orig = ManuallyDrop::new(orig);
922        MappedRwLockWriteGuard {
923            data,
924            inner_lock: &orig.lock.inner,
925            poison_flag: &orig.lock.poison,
926            poison_guard: orig.poison.clone(),
927            _variance: PhantomData,
928        }
929    }
930
931    /// Makes a [`MappedRwLockWriteGuard`] for a component of the borrowed data. The
932    /// original guard is returned as an `Err(...)` if the closure returns
933    /// `None`.
934    ///
935    /// The `RwLock` is already locked for writing, so this cannot fail.
936    ///
937    /// This is an associated function that needs to be used as
938    /// `RwLockWriteGuard::filter_map(...)`. A method would interfere with methods
939    /// of the same name on the contents of the `RwLockWriteGuard` used through
940    /// `Deref`.
941    ///
942    /// # Panics
943    ///
944    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.
945    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
946    pub fn filter_map<U, F>(orig: Self, f: F) -> Result<MappedRwLockWriteGuard<'rwlock, U>, Self>
947    where
948        F: FnOnce(&mut T) -> Option<&mut U>,
949        U: ?Sized,
950    {
951        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
952        // was created, and have been upheld throughout `map` and/or `filter_map`.
953        // The signature of the closure guarantees that it will not "leak" the lifetime of the
954        // reference passed to it. If the closure panics, the guard will be dropped.
955        match f(unsafe { &mut *orig.lock.data.get() }) {
956            Some(data) => {
957                let data = NonNull::from(data);
958                let orig = ManuallyDrop::new(orig);
959                Ok(MappedRwLockWriteGuard {
960                    data,
961                    inner_lock: &orig.lock.inner,
962                    poison_flag: &orig.lock.poison,
963                    poison_guard: orig.poison.clone(),
964                    _variance: PhantomData,
965                })
966            }
967            None => Err(orig),
968        }
969    }
970}
971
972impl<'rwlock, T: ?Sized> MappedRwLockReadGuard<'rwlock, T> {
973    /// Makes a [`MappedRwLockReadGuard`] for a component of the borrowed data,
974    /// e.g. an enum variant.
975    ///
976    /// The `RwLock` is already locked for reading, so this cannot fail.
977    ///
978    /// This is an associated function that needs to be used as
979    /// `MappedRwLockReadGuard::map(...)`. A method would interfere with
980    /// methods of the same name on the contents of the `MappedRwLockReadGuard`
981    /// used through `Deref`.
982    ///
983    /// # Panics
984    ///
985    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will not be
986    /// poisoned.
987    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
988    pub fn map<U, F>(orig: Self, f: F) -> MappedRwLockReadGuard<'rwlock, U>
989    where
990        F: FnOnce(&T) -> &U,
991        U: ?Sized,
992    {
993        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
994        // was created, and have been upheld throughout `map` and/or `filter_map`.
995        // The signature of the closure guarantees that it will not "leak" the lifetime of the
996        // reference passed to it. If the closure panics, the guard will be dropped.
997        let data = NonNull::from(f(unsafe { orig.data.as_ref() }));
998        let orig = ManuallyDrop::new(orig);
999        MappedRwLockReadGuard { data, inner_lock: &orig.inner_lock }
1000    }
1001
1002    /// Makes a [`MappedRwLockReadGuard`] for a component of the borrowed data.
1003    /// The original guard is returned as an `Err(...)` if the closure returns
1004    /// `None`.
1005    ///
1006    /// The `RwLock` is already locked for reading, so this cannot fail.
1007    ///
1008    /// This is an associated function that needs to be used as
1009    /// `MappedRwLockReadGuard::filter_map(...)`. A method would interfere with
1010    /// methods of the same name on the contents of the `MappedRwLockReadGuard`
1011    /// used through `Deref`.
1012    ///
1013    /// # Panics
1014    ///
1015    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will not be
1016    /// poisoned.
1017    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
1018    pub fn filter_map<U, F>(orig: Self, f: F) -> Result<MappedRwLockReadGuard<'rwlock, U>, Self>
1019    where
1020        F: FnOnce(&T) -> Option<&U>,
1021        U: ?Sized,
1022    {
1023        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
1024        // was created, and have been upheld throughout `map` and/or `filter_map`.
1025        // The signature of the closure guarantees that it will not "leak" the lifetime of the
1026        // reference passed to it. If the closure panics, the guard will be dropped.
1027        match f(unsafe { orig.data.as_ref() }) {
1028            Some(data) => {
1029                let data = NonNull::from(data);
1030                let orig = ManuallyDrop::new(orig);
1031                Ok(MappedRwLockReadGuard { data, inner_lock: &orig.inner_lock })
1032            }
1033            None => Err(orig),
1034        }
1035    }
1036}
1037
1038impl<'rwlock, T: ?Sized> MappedRwLockWriteGuard<'rwlock, T> {
1039    /// Makes a [`MappedRwLockWriteGuard`] for a component of the borrowed data,
1040    /// e.g. an enum variant.
1041    ///
1042    /// The `RwLock` is already locked for writing, so this cannot fail.
1043    ///
1044    /// This is an associated function that needs to be used as
1045    /// `MappedRwLockWriteGuard::map(...)`. A method would interfere with
1046    /// methods of the same name on the contents of the `MappedRwLockWriteGuard`
1047    /// used through `Deref`.
1048    ///
1049    /// # Panics
1050    ///
1051    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.
1052    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
1053    pub fn map<U, F>(mut orig: Self, f: F) -> MappedRwLockWriteGuard<'rwlock, U>
1054    where
1055        F: FnOnce(&mut T) -> &mut U,
1056        U: ?Sized,
1057    {
1058        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
1059        // was created, and have been upheld throughout `map` and/or `filter_map`.
1060        // The signature of the closure guarantees that it will not "leak" the lifetime of the
1061        // reference passed to it. If the closure panics, the guard will be dropped.
1062        let data = NonNull::from(f(unsafe { orig.data.as_mut() }));
1063        let orig = ManuallyDrop::new(orig);
1064        MappedRwLockWriteGuard {
1065            data,
1066            inner_lock: orig.inner_lock,
1067            poison_flag: orig.poison_flag,
1068            poison_guard: orig.poison_guard.clone(),
1069            _variance: PhantomData,
1070        }
1071    }
1072
1073    /// Makes a [`MappedRwLockWriteGuard`] for a component of the borrowed data.
1074    /// The original guard is returned as an `Err(...)` if the closure returns
1075    /// `None`.
1076    ///
1077    /// The `RwLock` is already locked for writing, so this cannot fail.
1078    ///
1079    /// This is an associated function that needs to be used as
1080    /// `MappedRwLockWriteGuard::filter_map(...)`. A method would interfere with
1081    /// methods of the same name on the contents of the `MappedRwLockWriteGuard`
1082    /// used through `Deref`.
1083    ///
1084    /// # Panics
1085    ///
1086    /// If the closure panics, the guard will be dropped (unlocked) and the RwLock will be poisoned.
1087    #[unstable(feature = "mapped_lock_guards", issue = "117108")]
1088    pub fn filter_map<U, F>(
1089        mut orig: Self,
1090        f: F,
1091    ) -> Result<MappedRwLockWriteGuard<'rwlock, U>, Self>
1092    where
1093        F: FnOnce(&mut T) -> Option<&mut U>,
1094        U: ?Sized,
1095    {
1096        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
1097        // was created, and have been upheld throughout `map` and/or `filter_map`.
1098        // The signature of the closure guarantees that it will not "leak" the lifetime of the
1099        // reference passed to it. If the closure panics, the guard will be dropped.
1100        match f(unsafe { orig.data.as_mut() }) {
1101            Some(data) => {
1102                let data = NonNull::from(data);
1103                let orig = ManuallyDrop::new(orig);
1104                Ok(MappedRwLockWriteGuard {
1105                    data,
1106                    inner_lock: orig.inner_lock,
1107                    poison_flag: orig.poison_flag,
1108                    poison_guard: orig.poison_guard.clone(),
1109                    _variance: PhantomData,
1110                })
1111            }
1112            None => Err(orig),
1113        }
1114    }
1115}
1116
1117#[stable(feature = "rust1", since = "1.0.0")]
1118impl<T: ?Sized> Drop for RwLockReadGuard<'_, T> {
1119    fn drop(&mut self) {
1120        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when created.
1121        unsafe {
1122            self.inner_lock.read_unlock();
1123        }
1124    }
1125}
1126
1127#[stable(feature = "rust1", since = "1.0.0")]
1128impl<T: ?Sized> Drop for RwLockWriteGuard<'_, T> {
1129    fn drop(&mut self) {
1130        self.lock.poison.done(&self.poison);
1131        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when created.
1132        unsafe {
1133            self.lock.inner.write_unlock();
1134        }
1135    }
1136}
1137
1138#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1139impl<T: ?Sized> Drop for MappedRwLockReadGuard<'_, T> {
1140    fn drop(&mut self) {
1141        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
1142        // was created, and have been upheld throughout `map` and/or `filter_map`.
1143        unsafe {
1144            self.inner_lock.read_unlock();
1145        }
1146    }
1147}
1148
1149#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1150impl<T: ?Sized> Drop for MappedRwLockWriteGuard<'_, T> {
1151    fn drop(&mut self) {
1152        self.poison_flag.done(&self.poison_guard);
1153        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
1154        // was created, and have been upheld throughout `map` and/or `filter_map`.
1155        unsafe {
1156            self.inner_lock.write_unlock();
1157        }
1158    }
1159}
1160
1161#[stable(feature = "rust1", since = "1.0.0")]
1162impl<T: ?Sized> Deref for RwLockReadGuard<'_, T> {
1163    type Target = T;
1164
1165    fn deref(&self) -> &T {
1166        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when created.
1167        unsafe { self.data.as_ref() }
1168    }
1169}
1170
1171#[stable(feature = "rust1", since = "1.0.0")]
1172impl<T: ?Sized> Deref for RwLockWriteGuard<'_, T> {
1173    type Target = T;
1174
1175    fn deref(&self) -> &T {
1176        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when created.
1177        unsafe { &*self.lock.data.get() }
1178    }
1179}
1180
1181#[stable(feature = "rust1", since = "1.0.0")]
1182impl<T: ?Sized> DerefMut for RwLockWriteGuard<'_, T> {
1183    fn deref_mut(&mut self) -> &mut T {
1184        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when created.
1185        unsafe { &mut *self.lock.data.get() }
1186    }
1187}
1188
1189#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1190impl<T: ?Sized> Deref for MappedRwLockReadGuard<'_, T> {
1191    type Target = T;
1192
1193    fn deref(&self) -> &T {
1194        // SAFETY: the conditions of `RwLockReadGuard::new` were satisfied when the original guard
1195        // was created, and have been upheld throughout `map` and/or `filter_map`.
1196        unsafe { self.data.as_ref() }
1197    }
1198}
1199
1200#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1201impl<T: ?Sized> Deref for MappedRwLockWriteGuard<'_, T> {
1202    type Target = T;
1203
1204    fn deref(&self) -> &T {
1205        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
1206        // was created, and have been upheld throughout `map` and/or `filter_map`.
1207        unsafe { self.data.as_ref() }
1208    }
1209}
1210
1211#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1212impl<T: ?Sized> DerefMut for MappedRwLockWriteGuard<'_, T> {
1213    fn deref_mut(&mut self) -> &mut T {
1214        // SAFETY: the conditions of `RwLockWriteGuard::new` were satisfied when the original guard
1215        // was created, and have been upheld throughout `map` and/or `filter_map`.
1216        unsafe { self.data.as_mut() }
1217    }
1218}
1219
1220#[stable(feature = "std_debug", since = "1.16.0")]
1221impl<T: ?Sized + fmt::Debug> fmt::Debug for RwLockReadGuard<'_, T> {
1222    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1223        (**self).fmt(f)
1224    }
1225}
1226
1227#[stable(feature = "std_guard_impls", since = "1.20.0")]
1228impl<T: ?Sized + fmt::Display> fmt::Display for RwLockReadGuard<'_, T> {
1229    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1230        (**self).fmt(f)
1231    }
1232}
1233
1234#[stable(feature = "std_debug", since = "1.16.0")]
1235impl<T: ?Sized + fmt::Debug> fmt::Debug for RwLockWriteGuard<'_, T> {
1236    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1237        (**self).fmt(f)
1238    }
1239}
1240
1241#[stable(feature = "std_guard_impls", since = "1.20.0")]
1242impl<T: ?Sized + fmt::Display> fmt::Display for RwLockWriteGuard<'_, T> {
1243    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1244        (**self).fmt(f)
1245    }
1246}
1247
1248#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1249impl<T: ?Sized + fmt::Debug> fmt::Debug for MappedRwLockReadGuard<'_, T> {
1250    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1251        (**self).fmt(f)
1252    }
1253}
1254
1255#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1256impl<T: ?Sized + fmt::Display> fmt::Display for MappedRwLockReadGuard<'_, T> {
1257    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1258        (**self).fmt(f)
1259    }
1260}
1261
1262#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1263impl<T: ?Sized + fmt::Debug> fmt::Debug for MappedRwLockWriteGuard<'_, T> {
1264    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1265        (**self).fmt(f)
1266    }
1267}
1268
1269#[unstable(feature = "mapped_lock_guards", issue = "117108")]
1270impl<T: ?Sized + fmt::Display> fmt::Display for MappedRwLockWriteGuard<'_, T> {
1271    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1272        (**self).fmt(f)
1273    }
1274}
````