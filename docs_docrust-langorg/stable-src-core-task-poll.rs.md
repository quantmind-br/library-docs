---
title: poll.rs - source
url: https://doc.rust-lang.org/stable/src/core/task/poll.rs.html#289
source: crawler
fetched_at: 2026-05-06T21:26:00.299119201-03:00
rendered_js: false
word_count: 1134
summary: This document defines the Poll enum, which represents the result of a polling operation in Rust's asynchronous task system, indicating whether a value is ready or if the task is pending.
tags:
    - rust
    - async
    - future
    - polling
    - concurrency
    - task-api
category: reference
---

## core/task/ poll.rs

````rust
1#![stable(feature = "futures_api", since = "1.36.0")]
2
3use crate::convert;
4use crate::ops::{self, ControlFlow};
5
6/// Indicates whether a value is available or if the current task has been
7/// scheduled to receive a wakeup instead.
8///
9/// This is returned by [`Future::poll`](core::future::Future::poll).
10#[must_use = "this `Poll` may be a `Pending` variant, which should be handled"]
11#[derive(Copy, Clone, Debug, Eq, PartialEq, Ord, PartialOrd, Hash)]
12#[lang = "Poll"]
13#[stable(feature = "futures_api", since = "1.36.0")]
14pub enum Poll<T> {
15    /// Represents that a value is immediately ready.
16    #[lang = "Ready"]
17    #[stable(feature = "futures_api", since = "1.36.0")]
18    Ready(#[stable(feature = "futures_api", since = "1.36.0")] T),
19
20    /// Represents that a value is not ready yet.
21    ///
22    /// When a function returns `Pending`, the function *must* also
23    /// ensure that the current task is scheduled to be awoken when
24    /// progress can be made.
25    #[lang = "Pending"]
26    #[stable(feature = "futures_api", since = "1.36.0")]
27    Pending,
28}
29
30impl<T> Poll<T> {
31    /// Maps a `Poll<T>` to `Poll<U>` by applying a function to a contained value.
32    ///
33    /// # Examples
34    ///
35    /// Converts a <code>Poll<[String]></code> into a <code>Poll<[usize]></code>, consuming
36    /// the original:
37    ///
38    /// [String]: ../../std/string/struct.String.html "String"
39    /// ```
40    /// # use core::task::Poll;
41    /// let poll_some_string = Poll::Ready(String::from("Hello, World!"));
42    /// // `Poll::map` takes self *by value*, consuming `poll_some_string`
43    /// let poll_some_len = poll_some_string.map(|s| s.len());
44    ///
45    /// assert_eq!(poll_some_len, Poll::Ready(13));
46    /// ```
47    #[stable(feature = "futures_api", since = "1.36.0")]
48    #[inline]
49    pub fn map<U, F>(self, f: F) -> Poll<U>
50    where
51        F: FnOnce(T) -> U,
52    {
53        match self {
54            Poll::Ready(t) => Poll::Ready(f(t)),
55            Poll::Pending => Poll::Pending,
56        }
57    }
58
59    /// Returns `true` if the poll is a [`Poll::Ready`] value.
60    ///
61    /// # Examples
62    ///
63    /// ```
64    /// # use core::task::Poll;
65    /// let x: Poll<u32> = Poll::Ready(2);
66    /// assert_eq!(x.is_ready(), true);
67    ///
68    /// let x: Poll<u32> = Poll::Pending;
69    /// assert_eq!(x.is_ready(), false);
70    /// ```
71    #[inline]
72    #[rustc_const_stable(feature = "const_poll", since = "1.49.0")]
73    #[stable(feature = "futures_api", since = "1.36.0")]
74    pub const fn is_ready(&self) -> bool {
75        matches!(*self, Poll::Ready(_))
76    }
77
78    /// Returns `true` if the poll is a [`Pending`] value.
79    ///
80    /// [`Pending`]: Poll::Pending
81    ///
82    /// # Examples
83    ///
84    /// ```
85    /// # use core::task::Poll;
86    /// let x: Poll<u32> = Poll::Ready(2);
87    /// assert_eq!(x.is_pending(), false);
88    ///
89    /// let x: Poll<u32> = Poll::Pending;
90    /// assert_eq!(x.is_pending(), true);
91    /// ```
92    #[inline]
93    #[rustc_const_stable(feature = "const_poll", since = "1.49.0")]
94    #[stable(feature = "futures_api", since = "1.36.0")]
95    pub const fn is_pending(&self) -> bool {
96        !self.is_ready()
97    }
98}
99
100impl<T, E> Poll<Result<T, E>> {
101    /// Maps a `Poll<Result<T, E>>` to `Poll<Result<U, E>>` by applying a
102    /// function to a contained `Poll::Ready(Ok)` value, leaving all other
103    /// variants untouched.
104    ///
105    /// This function can be used to compose the results of two functions.
106    ///
107    /// # Examples
108    ///
109    /// ```
110    /// # use core::task::Poll;
111    /// let res: Poll<Result<u8, _>> = Poll::Ready("12".parse());
112    /// let squared = res.map_ok(|n| n * n);
113    /// assert_eq!(squared, Poll::Ready(Ok(144)));
114    /// ```
115    #[stable(feature = "futures_api", since = "1.36.0")]
116    #[inline]
117    pub fn map_ok<U, F>(self, f: F) -> Poll<Result<U, E>>
118    where
119        F: FnOnce(T) -> U,
120    {
121        match self {
122            Poll::Ready(Ok(t)) => Poll::Ready(Ok(f(t))),
123            Poll::Ready(Err(e)) => Poll::Ready(Err(e)),
124            Poll::Pending => Poll::Pending,
125        }
126    }
127
128    /// Maps a `Poll::Ready<Result<T, E>>` to `Poll::Ready<Result<T, U>>` by
129    /// applying a function to a contained `Poll::Ready(Err)` value, leaving all other
130    /// variants untouched.
131    ///
132    /// This function can be used to pass through a successful result while handling
133    /// an error.
134    ///
135    /// # Examples
136    ///
137    /// ```
138    /// # use core::task::Poll;
139    /// let res: Poll<Result<u8, _>> = Poll::Ready("oops".parse());
140    /// let res = res.map_err(|_| 0_u8);
141    /// assert_eq!(res, Poll::Ready(Err(0)));
142    /// ```
143    #[stable(feature = "futures_api", since = "1.36.0")]
144    #[inline]
145    pub fn map_err<U, F>(self, f: F) -> Poll<Result<T, U>>
146    where
147        F: FnOnce(E) -> U,
148    {
149        match self {
150            Poll::Ready(Ok(t)) => Poll::Ready(Ok(t)),
151            Poll::Ready(Err(e)) => Poll::Ready(Err(f(e))),
152            Poll::Pending => Poll::Pending,
153        }
154    }
155}
156
157impl<T, E> Poll<Option<Result<T, E>>> {
158    /// Maps a `Poll<Option<Result<T, E>>>` to `Poll<Option<Result<U, E>>>` by
159    /// applying a function to a contained `Poll::Ready(Some(Ok))` value,
160    /// leaving all other variants untouched.
161    ///
162    /// This function can be used to compose the results of two functions.
163    ///
164    /// # Examples
165    ///
166    /// ```
167    /// # use core::task::Poll;
168    /// let res: Poll<Option<Result<u8, _>>> = Poll::Ready(Some("12".parse()));
169    /// let squared = res.map_ok(|n| n * n);
170    /// assert_eq!(squared, Poll::Ready(Some(Ok(144))));
171    /// ```
172    #[stable(feature = "poll_map", since = "1.51.0")]
173    #[inline]
174    pub fn map_ok<U, F>(self, f: F) -> Poll<Option<Result<U, E>>>
175    where
176        F: FnOnce(T) -> U,
177    {
178        match self {
179            Poll::Ready(Some(Ok(t))) => Poll::Ready(Some(Ok(f(t)))),
180            Poll::Ready(Some(Err(e))) => Poll::Ready(Some(Err(e))),
181            Poll::Ready(None) => Poll::Ready(None),
182            Poll::Pending => Poll::Pending,
183        }
184    }
185
186    /// Maps a `Poll::Ready<Option<Result<T, E>>>` to
187    /// `Poll::Ready<Option<Result<T, F>>>` by applying a function to a
188    /// contained `Poll::Ready(Some(Err))` value, leaving all other variants
189    /// untouched.
190    ///
191    /// This function can be used to pass through a successful result while handling
192    /// an error.
193    ///
194    /// # Examples
195    ///
196    /// ```
197    /// # use core::task::Poll;
198    /// let res: Poll<Option<Result<u8, _>>> = Poll::Ready(Some("oops".parse()));
199    /// let res = res.map_err(|_| 0_u8);
200    /// assert_eq!(res, Poll::Ready(Some(Err(0))));
201    /// ```
202    #[stable(feature = "poll_map", since = "1.51.0")]
203    #[inline]
204    pub fn map_err<U, F>(self, f: F) -> Poll<Option<Result<T, U>>>
205    where
206        F: FnOnce(E) -> U,
207    {
208        match self {
209            Poll::Ready(Some(Ok(t))) => Poll::Ready(Some(Ok(t))),
210            Poll::Ready(Some(Err(e))) => Poll::Ready(Some(Err(f(e)))),
211            Poll::Ready(None) => Poll::Ready(None),
212            Poll::Pending => Poll::Pending,
213        }
214    }
215}
216
217#[stable(feature = "futures_api", since = "1.36.0")]
218#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
219impl<T> const From<T> for Poll<T> {
220    /// Moves the value into a [`Poll::Ready`] to make a `Poll<T>`.
221    ///
222    /// # Example
223    ///
224    /// ```
225    /// # use core::task::Poll;
226    /// assert_eq!(Poll::from(true), Poll::Ready(true));
227    /// ```
228    fn from(t: T) -> Poll<T> {
229        Poll::Ready(t)
230    }
231}
232
233#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
234impl<T, E> ops::Try for Poll<Result<T, E>> {
235    type Output = Poll<T>;
236    type Residual = Result<convert::Infallible, E>;
237
238    #[inline]
239    fn from_output(c: Self::Output) -> Self {
240        c.map(Ok)
241    }
242
243    #[inline]
244    fn branch(self) -> ControlFlow<Self::Residual, Self::Output> {
245        match self {
246            Poll::Ready(Ok(x)) => ControlFlow::Continue(Poll::Ready(x)),
247            Poll::Ready(Err(e)) => ControlFlow::Break(Err(e)),
248            Poll::Pending => ControlFlow::Continue(Poll::Pending),
249        }
250    }
251}
252
253#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
254impl<T, E, F: From<E>> ops::FromResidual<Result<convert::Infallible, E>> for Poll<Result<T, F>> {
255    #[inline]
256    fn from_residual(x: Result<convert::Infallible, E>) -> Self {
257        match x {
258            Err(e) => Poll::Ready(Err(From::from(e))),
259        }
260    }
261}
262
263#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
264impl<T, E> ops::Try for Poll<Option<Result<T, E>>> {
265    type Output = Poll<Option<T>>;
266    type Residual = Result<convert::Infallible, E>;
267
268    #[inline]
269    fn from_output(c: Self::Output) -> Self {
270        c.map(|x| x.map(Ok))
271    }
272
273    #[inline]
274    fn branch(self) -> ControlFlow<Self::Residual, Self::Output> {
275        match self {
276            Poll::Ready(Some(Ok(x))) => ControlFlow::Continue(Poll::Ready(Some(x))),
277            Poll::Ready(Some(Err(e))) => ControlFlow::Break(Err(e)),
278            Poll::Ready(None) => ControlFlow::Continue(Poll::Ready(None)),
279            Poll::Pending => ControlFlow::Continue(Poll::Pending),
280        }
281    }
282}
283
284#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
285impl<T, E, F: From<E>> ops::FromResidual<Result<convert::Infallible, E>>
286    for Poll<Option<Result<T, F>>>
287{
288    #[inline]
289    fn from_residual(x: Result<convert::Infallible, E>) -> Self {
290        match x {
291            Err(e) => Poll::Ready(Some(Err(From::from(e)))),
292        }
293    }
294}
````