---
title: builder.rs - source
url: https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#58-263
source: crawler
fetched_at: 2026-05-06T21:26:48.627073248-03:00
rendered_js: false
word_count: 1221
summary: The Builder struct provides a configurable interface for spawning new threads in Rust, allowing users to define thread names, stack sizes, and hook behavior while providing explicit error handling.
tags:
    - rust
    - threading
    - concurrency
    - builder-pattern
    - system-programming
category: api
---

## std/thread/ builder.rs

````rust
1use super::join_handle::JoinHandle;
2use super::lifecycle::spawn_unchecked;
3use crate::io;
4
5/// Thread factory, which can be used in order to configure the properties of
6/// a new thread.
7///
8/// Methods can be chained on it in order to configure it.
9///
10/// The two configurations available are:
11///
12/// - [`name`]: specifies an [associated name for the thread][naming-threads]
13/// - [`stack_size`]: specifies the [desired stack size for the thread][stack-size]
14///
15/// The [`spawn`] method will take ownership of the builder and create an
16/// [`io::Result`] to the thread handle with the given configuration.
17///
18/// The [`thread::spawn`] free function uses a `Builder` with default
19/// configuration and [`unwrap`]s its return value.
20///
21/// You may want to use [`spawn`] instead of [`thread::spawn`], when you want
22/// to recover from a failure to launch a thread, indeed the free function will
23/// panic where the `Builder` method will return a [`io::Result`].
24///
25/// # Examples
26///
27/// ```
28/// use std::thread;
29///
30/// let builder = thread::Builder::new();
31///
32/// let handler = builder.spawn(|| {
33///     // thread code
34/// }).unwrap();
35///
36/// handler.join().unwrap();
37/// ```
38///
39/// [`stack_size`]: Builder::stack_size
40/// [`name`]: Builder::name
41/// [`spawn`]: Builder::spawn
42/// [`thread::spawn`]: super::spawn
43/// [`unwrap`]: crate::result::Result::unwrap
44/// [naming-threads]: ./index.html#naming-threads
45/// [stack-size]: ./index.html#stack-size
46#[must_use = "must eventually spawn the thread"]
47#[stable(feature = "rust1", since = "1.0.0")]
48#[derive(Debug)]
49pub struct Builder {
50    /// A name for the thread-to-be, for identification in panic messages
51    pub(super) name: Option<String>,
52    /// The size of the stack for the spawned thread in bytes
53    pub(super) stack_size: Option<usize>,
54    /// Skip running and inheriting the thread spawn hooks
55    pub(super) no_hooks: bool,
56}
57
58impl Builder {
59    /// Generates the base configuration for spawning a thread, from which
60    /// configuration methods can be chained.
61    ///
62    /// # Examples
63    ///
64    /// ```
65    /// use std::thread;
66    ///
67    /// let builder = thread::Builder::new()
68    ///                               .name("foo".into())
69    ///                               .stack_size(32 * 1024);
70    ///
71    /// let handler = builder.spawn(|| {
72    ///     // thread code
73    /// }).unwrap();
74    ///
75    /// handler.join().unwrap();
76    /// ```
77    #[stable(feature = "rust1", since = "1.0.0")]
78    pub fn new() -> Builder {
79        Builder { name: None, stack_size: None, no_hooks: false }
80    }
81
82    /// Names the thread-to-be. Currently the name is used for identification
83    /// only in panic messages.
84    ///
85    /// The name must not contain null bytes (`\0`).
86    ///
87    /// For more information about named threads, see
88    /// [this module-level documentation][naming-threads].
89    ///
90    /// # Examples
91    ///
92    /// ```
93    /// use std::thread;
94    ///
95    /// let builder = thread::Builder::new()
96    ///     .name("foo".into());
97    ///
98    /// let handler = builder.spawn(|| {
99    ///     assert_eq!(thread::current().name(), Some("foo"))
100    /// }).unwrap();
101    ///
102    /// handler.join().unwrap();
103    /// ```
104    ///
105    /// [naming-threads]: ./index.html#naming-threads
106    #[stable(feature = "rust1", since = "1.0.0")]
107    pub fn name(mut self, name: String) -> Builder {
108        self.name = Some(name);
109        self
110    }
111
112    /// Sets the size of the stack (in bytes) for the new thread.
113    ///
114    /// The actual stack size may be greater than this value if
115    /// the platform specifies a minimal stack size.
116    ///
117    /// For more information about the stack size for threads, see
118    /// [this module-level documentation][stack-size].
119    ///
120    /// # Examples
121    ///
122    /// ```
123    /// use std::thread;
124    ///
125    /// let builder = thread::Builder::new().stack_size(32 * 1024);
126    /// ```
127    ///
128    /// [stack-size]: ./index.html#stack-size
129    #[stable(feature = "rust1", since = "1.0.0")]
130    pub fn stack_size(mut self, size: usize) -> Builder {
131        self.stack_size = Some(size);
132        self
133    }
134
135    /// Disables running and inheriting [spawn hooks].
136    ///
137    /// Use this if the parent thread is in no way relevant for the child thread.
138    /// For example, when lazily spawning threads for a thread pool.
139    ///
140    /// [spawn hooks]: super::add_spawn_hook
141    #[unstable(feature = "thread_spawn_hook", issue = "132951")]
142    pub fn no_hooks(mut self) -> Builder {
143        self.no_hooks = true;
144        self
145    }
146
147    /// Spawns a new thread by taking ownership of the `Builder`, and returns an
148    /// [`io::Result`] to its [`JoinHandle`].
149    ///
150    /// The spawned thread may outlive the caller (unless the caller thread
151    /// is the main thread; the whole process is terminated when the main
152    /// thread finishes). The join handle can be used to block on
153    /// termination of the spawned thread, including recovering its panics.
154    ///
155    /// For a more complete documentation see [`thread::spawn`].
156    ///
157    /// # Errors
158    ///
159    /// Unlike the [`spawn`] free function, this method yields an
160    /// [`io::Result`] to capture any failure to create the thread at
161    /// the OS level.
162    ///
163    /// # Panics
164    ///
165    /// Panics if a thread name was set and it contained null bytes.
166    ///
167    /// # Examples
168    ///
169    /// ```
170    /// use std::thread;
171    ///
172    /// let builder = thread::Builder::new();
173    ///
174    /// let handler = builder.spawn(|| {
175    ///     // thread code
176    /// }).unwrap();
177    ///
178    /// handler.join().unwrap();
179    /// ```
180    ///
181    /// [`thread::spawn`]: super::spawn
182    /// [`spawn`]: super::spawn
183    #[stable(feature = "rust1", since = "1.0.0")]
184    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
185    pub fn spawn<F, T>(self, f: F) -> io::Result<JoinHandle<T>>
186    where
187        F: FnOnce() -> T,
188        F: Send + 'static,
189        T: Send + 'static,
190    {
191        unsafe { self.spawn_unchecked(f) }
192    }
193
194    /// Spawns a new thread without any lifetime restrictions by taking ownership
195    /// of the `Builder`, and returns an [`io::Result`] to its [`JoinHandle`].
196    ///
197    /// The spawned thread may outlive the caller (unless the caller thread
198    /// is the main thread; the whole process is terminated when the main
199    /// thread finishes). The join handle can be used to block on
200    /// termination of the spawned thread, including recovering its panics.
201    ///
202    /// This method is identical to [`thread::Builder::spawn`][`Builder::spawn`],
203    /// except for the relaxed lifetime bounds, which render it unsafe.
204    /// For a more complete documentation see [`thread::spawn`].
205    ///
206    /// # Errors
207    ///
208    /// Unlike the [`spawn`] free function, this method yields an
209    /// [`io::Result`] to capture any failure to create the thread at
210    /// the OS level.
211    ///
212    /// # Panics
213    ///
214    /// Panics if a thread name was set and it contained null bytes.
215    ///
216    /// # Safety
217    ///
218    /// The caller has to ensure that the spawned thread does not outlive any
219    /// references in the supplied thread closure and its return type.
220    /// This can be guaranteed in two ways:
221    ///
222    /// - ensure that [`join`][`JoinHandle::join`] is called before any referenced
223    /// data is dropped
224    /// - use only types with `'static` lifetime bounds, i.e., those with no or only
225    /// `'static` references (both [`thread::Builder::spawn`][`Builder::spawn`]
226    /// and [`thread::spawn`] enforce this property statically)
227    ///
228    /// # Examples
229    ///
230    /// ```
231    /// use std::thread;
232    ///
233    /// let builder = thread::Builder::new();
234    ///
235    /// let x = 1;
236    /// let thread_x = &x;
237    ///
238    /// let handler = unsafe {
239    ///     builder.spawn_unchecked(move || {
240    ///         println!("x = {}", *thread_x);
241    ///     }).unwrap()
242    /// };
243    ///
244    /// // caller has to ensure `join()` is called, otherwise
245    /// // it is possible to access freed memory if `x` gets
246    /// // dropped before the thread closure is executed!
247    /// handler.join().unwrap();
248    /// ```
249    ///
250    /// [`thread::spawn`]: super::spawn
251    /// [`spawn`]: super::spawn
252    #[stable(feature = "thread_spawn_unchecked", since = "1.82.0")]
253    #[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
254    pub unsafe fn spawn_unchecked<F, T>(self, f: F) -> io::Result<JoinHandle<T>>
255    where
256        F: FnOnce() -> T,
257        F: Send,
258        T: Send,
259    {
260        let Builder { name, stack_size, no_hooks } = self;
261        Ok(JoinHandle(unsafe { spawn_unchecked(name, stack_size, no_hooks, None, f) }?))
262    }
263}
````