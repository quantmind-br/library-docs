---
title: scoped.rs - source
url: https://doc.rust-lang.org/src/std/thread/scoped.rs.html#256-269
source: crawler
fetched_at: 2026-05-06T21:25:21.178133499-03:00
rendered_js: false
word_count: 1808
summary: This document defines the scoped threads implementation in Rust, which allows spawned threads to borrow non-static data by guaranteeing they are joined before the scope ends.
tags:
    - rust
    - concurrency
    - multithreading
    - scoped-threads
    - lifetimes
    - memory-safety
category: concept
---

## std/thread/ scoped.rs

````rust
1use super::Result;
2use super::builder::Builder;
3use super::current::current_or_unnamed;
4use super::lifecycle::{JoinInner, spawn_unchecked};
5use super::thread::Thread;
6use crate::marker::PhantomData;
7use crate::panic::{AssertUnwindSafe, catch_unwind, resume_unwind};
8use crate::sync::Arc;
9use crate::sync::atomic::{Atomic, AtomicBool, AtomicUsize, Ordering};
10use crate::{fmt, io};
11
12/// A scope to spawn scoped threads in.
13///
14/// See [`scope`] for details.
15#[stable(feature = "scoped_threads", since = "1.63.0")]
16pub struct Scope<'scope, 'env: 'scope> {
17    data: Arc<ScopeData>,
18    /// Invariance over 'scope, to make sure 'scope cannot shrink,
19    /// which is necessary for soundness.
20    ///
21    /// Without invariance, this would compile fine but be unsound:
22    ///
23    /// ```compile_fail,E0373
24    /// std::thread::scope(|s| {
25    ///     s.spawn(|| {
26    ///         let a = String::from("abcd");
27    ///         s.spawn(|| println!("{a:?}")); // might run after `a` is dropped
28    ///     });
29    /// });
30    /// ```
31    scope: PhantomData<&'scope mut &'scope ()>,
32    env: PhantomData<&'env mut &'env ()>,
33}
34
35/// An owned permission to join on a scoped thread (block on its termination).
36///
37/// See [`Scope::spawn`] for details.
38#[stable(feature = "scoped_threads", since = "1.63.0")]
39pub struct ScopedJoinHandle<'scope, T>(JoinInner<'scope, T>);
40
41pub(super) struct ScopeData {
42    num_running_threads: Atomic<usize>,
43    a_thread_panicked: Atomic<bool>,
44    main_thread: Thread,
45}
46
47impl ScopeData {
48    pub(super) fn increment_num_running_threads(&self) {
49        // We check for 'overflow' with usize::MAX / 2, to make sure there's no
50        // chance it overflows to 0, which would result in unsoundness.
51        if self.num_running_threads.fetch_add(1, Ordering::Relaxed) > usize::MAX / 2 {
52            // This can only reasonably happen by mem::forget()'ing a lot of ScopedJoinHandles.
53            self.overflow();
54        }
55    }
56
57    #[cold]
58    fn overflow(&self) {
59        self.decrement_num_running_threads(false);
60        panic!("too many running threads in thread scope");
61    }
62
63    pub(super) fn decrement_num_running_threads(&self, panic: bool) {
64        if panic {
65            self.a_thread_panicked.store(true, Ordering::Relaxed);
66        }
67        if self.num_running_threads.fetch_sub(1, Ordering::Release) == 1 {
68            self.main_thread.unpark();
69        }
70    }
71}
72
73/// Creates a scope for spawning scoped threads.
74///
75/// The function passed to `scope` will be provided a [`Scope`] object,
76/// through which scoped threads can be [spawned][`Scope::spawn`].
77///
78/// Unlike non-scoped threads, scoped threads can borrow non-`'static` data,
79/// as the scope guarantees all threads will be joined at the end of the scope.
80///
81/// All threads spawned within the scope that haven't been manually joined
82/// will be automatically joined before this function returns.
83/// However, note that joining will only wait for the main function of these threads to finish; even
84/// when this function returns, destructors of thread-local variables in these threads might still
85/// be running.
86///
87/// # Panics
88///
89/// If any of the automatically joined threads panicked, this function will panic.
90///
91/// If you want to handle panics from spawned threads,
92/// [`join`][ScopedJoinHandle::join] them before the end of the scope.
93///
94/// # Example
95///
96/// ```
97/// use std::thread;
98///
99/// let mut a = vec![1, 2, 3];
100/// let mut x = 0;
101///
102/// thread::scope(|s| {
103///     s.spawn(|| {
104///         println!("hello from the first scoped thread");
105///         // We can borrow `a` here.
106///         dbg!(&a);
107///     });
108///     s.spawn(|| {
109///         println!("hello from the second scoped thread");
110///         // We can even mutably borrow `x` here,
111///         // because no other threads are using it.
112///         x += a[0] + a[2];
113///     });
114///     println!("hello from the main thread");
115/// });
116///
117/// // After the scope, we can modify and access our variables again:
118/// a.push(4);
119/// assert_eq!(x, a.len());
120/// ```
121///
122/// # Lifetimes
123///
124/// Scoped threads involve two lifetimes: `'scope` and `'env`.
125///
126/// The `'scope` lifetime represents the lifetime of the scope itself.
127/// That is: the time during which new scoped threads may be spawned,
128/// and also the time during which they might still be running.
129/// Once this lifetime ends, all scoped threads are joined.
130/// This lifetime starts within the `scope` function, before `f` (the argument to `scope`) starts.
131/// It ends after `f` returns and all scoped threads have been joined, but before `scope` returns.
132///
133/// The `'env` lifetime represents the lifetime of whatever is borrowed by the scoped threads.
134/// This lifetime must outlast the call to `scope`, and thus cannot be smaller than `'scope`.
135/// It can be as small as the call to `scope`, meaning that anything that outlives this call,
136/// such as local variables defined right before the scope, can be borrowed by the scoped threads.
137///
138/// The `'env: 'scope` bound is part of the definition of the `Scope` type.
139#[track_caller]
140#[stable(feature = "scoped_threads", since = "1.63.0")]
141pub fn scope<'env, F, T>(f: F) -> T
142where
143    F: for<'scope> FnOnce(&'scope Scope<'scope, 'env>) -> T,
144{
145    // We put the `ScopeData` into an `Arc` so that other threads can finish their
146    // `decrement_num_running_threads` even after this function returns.
147    let scope = Scope {
148        data: Arc::new(ScopeData {
149            num_running_threads: AtomicUsize::new(0),
150            main_thread: current_or_unnamed(),
151            a_thread_panicked: AtomicBool::new(false),
152        }),
153        env: PhantomData,
154        scope: PhantomData,
155    };
156
157    // Run `f`, but catch panics so we can make sure to wait for all the threads to join.
158    let result = catch_unwind(AssertUnwindSafe(|| f(&scope)));
159
160    // Wait until all the threads are finished.
161    while scope.data.num_running_threads.load(Ordering::Acquire) != 0 {
162        // SAFETY: this is the main thread, the handle belongs to us.
163        unsafe { scope.data.main_thread.park() };
164    }
165
166    // Throw any panic from `f`, or the return value of `f` if no thread panicked.
167    match result {
168        Err(e) => resume_unwind(e),
169        Ok(_) if scope.data.a_thread_panicked.load(Ordering::Relaxed) => {
170            panic!("a scoped thread panicked")
171        }
172        Ok(result) => result,
173    }
174}
175
176impl<'scope, 'env> Scope<'scope, 'env> {
177    /// Spawns a new thread within a scope, returning a [`ScopedJoinHandle`] for it.
178    ///
179    /// Unlike non-scoped threads, threads spawned with this function may
180    /// borrow non-`'static` data from the outside the scope. See [`scope`] for
181    /// details.
182    ///
183    /// The join handle provides a [`join`] method that can be used to join the spawned
184    /// thread. If the spawned thread panics, [`join`] will return an [`Err`] containing
185    /// the panic payload.
186    ///
187    /// If the join handle is dropped, the spawned thread will be implicitly joined at the
188    /// end of the scope. In that case, if the spawned thread panics, [`scope`] will
189    /// panic after all threads are joined.
190    ///
191    /// This function creates a thread with the default parameters of [`Builder`].
192    /// To specify the new thread's stack size or the name, use [`Builder::spawn_scoped`].
193    ///
194    /// # Panics
195    ///
196    /// Panics if the OS fails to create a thread; use [`Builder::spawn_scoped`]
197    /// to recover from such errors.
198    ///
199    /// [`join`]: ScopedJoinHandle::join
200    #[stable(feature = "scoped_threads", since = "1.63.0")]
201    pub fn spawn<F, T>(&'scope self, f: F) -> ScopedJoinHandle<'scope, T>
202    where
203        F: FnOnce() -> T + Send + 'scope,
204        T: Send + 'scope,
205    {
206        Builder::new().spawn_scoped(self, f).expect("failed to spawn thread")
207    }
208}
209
210impl Builder {
211    /// Spawns a new scoped thread using the settings set through this `Builder`.
212    ///
213    /// Unlike [`Scope::spawn`], this method yields an [`io::Result`] to
214    /// capture any failure to create the thread at the OS level.
215    ///
216    /// # Panics
217    ///
218    /// Panics if a thread name was set and it contained null bytes.
219    ///
220    /// # Example
221    ///
222    /// ```
223    /// use std::thread;
224    ///
225    /// let mut a = vec![1, 2, 3];
226    /// let mut x = 0;
227    ///
228    /// thread::scope(|s| {
229    ///     thread::Builder::new()
230    ///         .name("first".to_string())
231    ///         .spawn_scoped(s, ||
232    ///     {
233    ///         println!("hello from the {:?} scoped thread", thread::current().name());
234    ///         // We can borrow `a` here.
235    ///         dbg!(&a);
236    ///     })
237    ///     .unwrap();
238    ///     thread::Builder::new()
239    ///         .name("second".to_string())
240    ///         .spawn_scoped(s, ||
241    ///     {
242    ///         println!("hello from the {:?} scoped thread", thread::current().name());
243    ///         // We can even mutably borrow `x` here,
244    ///         // because no other threads are using it.
245    ///         x += a[0] + a[2];
246    ///     })
247    ///     .unwrap();
248    ///     println!("hello from the main thread");
249    /// });
250    ///
251    /// // After the scope, we can modify and access our variables again:
252    /// a.push(4);
253    /// assert_eq!(x, a.len());
254    /// ```
255    #[stable(feature = "scoped_threads", since = "1.63.0")]
256    pub fn spawn_scoped<'scope, 'env, F, T>(
257        self,
258        scope: &'scope Scope<'scope, 'env>,
259        f: F,
260    ) -> io::Result<ScopedJoinHandle<'scope, T>>
261    where
262        F: FnOnce() -> T + Send + 'scope,
263        T: Send + 'scope,
264    {
265        let Builder { name, stack_size, no_hooks } = self;
266        Ok(ScopedJoinHandle(unsafe {
267            spawn_unchecked(name, stack_size, no_hooks, Some(scope.data.clone()), f)
268        }?))
269    }
270}
271
272impl<'scope, T> ScopedJoinHandle<'scope, T> {
273    /// Extracts a handle to the underlying thread.
274    ///
275    /// # Examples
276    ///
277    /// ```
278    /// use std::thread;
279    ///
280    /// thread::scope(|s| {
281    ///     let t = s.spawn(|| {
282    ///         println!("hello");
283    ///     });
284    ///     println!("thread id: {:?}", t.thread().id());
285    /// });
286    /// ```
287    #[must_use]
288    #[stable(feature = "scoped_threads", since = "1.63.0")]
289    pub fn thread(&self) -> &Thread {
290        self.0.thread()
291    }
292
293    /// Waits for the associated thread to finish.
294    ///
295    /// This function will return immediately if the associated thread has already finished.
296    /// Otherwise, it fully waits for the thread to finish, including all destructors
297    /// for thread-local variables that might be running after the main function of the thread.
298    ///
299    /// In terms of [atomic memory orderings], the completion of the associated
300    /// thread synchronizes with this function returning.
301    /// In other words, all operations performed by that thread
302    /// [happen before](https://doc.rust-lang.org/nomicon/atomics.html#data-accesses)
303    /// all operations that happen after `join` returns.
304    ///
305    /// If the associated thread panics, [`Err`] is returned with the panic payload.
306    ///
307    /// [atomic memory orderings]: crate::sync::atomic
308    ///
309    /// # Examples
310    ///
311    /// ```
312    /// use std::thread;
313    ///
314    /// thread::scope(|s| {
315    ///     let t = s.spawn(|| {
316    ///         panic!("oh no");
317    ///     });
318    ///     assert!(t.join().is_err());
319    /// });
320    /// ```
321    #[stable(feature = "scoped_threads", since = "1.63.0")]
322    pub fn join(self) -> Result<T> {
323        self.0.join()
324    }
325
326    /// Checks if the associated thread has finished running its main function.
327    ///
328    /// `is_finished` supports implementing a non-blocking join operation, by checking
329    /// `is_finished`, and calling `join` if it returns `true`. This function does not block. To
330    /// block while waiting on the thread to finish, use [`join`][Self::join].
331    ///
332    /// This might return `true` for a brief moment after the thread's main
333    /// function has returned, but before the thread itself has stopped running.
334    /// However, once this returns `true`, [`join`][Self::join] can be expected
335    /// to return quickly, without blocking for any significant amount of time.
336    #[stable(feature = "scoped_threads", since = "1.63.0")]
337    pub fn is_finished(&self) -> bool {
338        self.0.is_finished()
339    }
340}
341
342#[stable(feature = "scoped_threads", since = "1.63.0")]
343impl fmt::Debug for Scope<'_, '_> {
344    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
345        f.debug_struct("Scope")
346            .field("num_running_threads", &self.data.num_running_threads.load(Ordering::Relaxed))
347            .field("a_thread_panicked", &self.data.a_thread_panicked.load(Ordering::Relaxed))
348            .field("main_thread", &self.data.main_thread)
349            .finish_non_exhaustive()
350    }
351}
352
353#[stable(feature = "scoped_threads", since = "1.63.0")]
354impl<'scope, T> fmt::Debug for ScopedJoinHandle<'scope, T> {
355    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
356        f.debug_struct("ScopedJoinHandle").finish_non_exhaustive()
357    }
358}
````