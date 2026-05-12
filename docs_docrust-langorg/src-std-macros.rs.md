---
title: macros.rs - source
url: https://doc.rust-lang.org/src/std/macros.rs.html#138-145
source: crawler
fetched_at: 2026-05-06T21:24:36.900979029-03:00
rendered_js: false
word_count: 1394
summary: This document defines the core Rust standard library macros for printing to standard output, standard error, and debugging expressions.
tags:
    - rust
    - macros
    - standard-library
    - io
    - debugging
    - printing
category: reference
---

````rust
1//! Standard library macros
2//!
3//! This module contains a set of macros which are exported from the standard
4//! library. Each macro is available for use when linking against the standard
5//! library.
6// ignore-tidy-dbg
7
8#[doc = include_str!("../../core/src/macros/panic.md")]
9#[macro_export]
10#[rustc_builtin_macro(std_panic)]
11#[stable(feature = "rust1", since = "1.0.0")]
12#[allow_internal_unstable(edition_panic)]
13#[cfg_attr(not(test), rustc_diagnostic_item = "std_panic_macro")]
14macro_rules! panic {
15    // Expands to either `$crate::panic::panic_2015` or `$crate::panic::panic_2021`
16    // depending on the edition of the caller.
17    ($($arg:tt)*) => {
18        /* compiler built-in */
19    };
20}
21
22/// Prints to the standard output.
23///
24/// Equivalent to the [`println!`] macro except that a newline is not printed at
25/// the end of the message.
26///
27/// Note that stdout is frequently line-buffered by default so it may be
28/// necessary to use [`io::stdout().flush()`][flush] to ensure the output is emitted
29/// immediately.
30///
31/// The `print!` macro will lock the standard output on each call. If you call
32/// `print!` within a hot loop, this behavior may be the bottleneck of the loop.
33/// To avoid this, lock stdout with [`io::stdout().lock()`][lock]:
34/// ```
35/// use std::io::{stdout, Write};
36///
37/// let mut lock = stdout().lock();
38/// write!(lock, "hello world").unwrap();
39/// ```
40///
41/// Use `print!` only for the primary output of your program. Use
42/// [`eprint!`] instead to print error and progress messages.
43///
44/// See the formatting documentation in [`std::fmt`](crate::fmt)
45/// for details of the macro argument syntax.
46///
47/// [flush]: crate::io::Write::flush
48/// [`println!`]: crate::println
49/// [`eprint!`]: crate::eprint
50/// [lock]: crate::io::Stdout
51///
52/// # Panics
53///
54/// Panics if writing to `io::stdout()` fails.
55///
56/// Writing to non-blocking stdout can cause an error, which will lead
57/// this macro to panic.
58///
59/// # Examples
60///
61/// ```
62/// use std::io::{self, Write};
63///
64/// print!("this ");
65/// print!("will ");
66/// print!("be ");
67/// print!("on ");
68/// print!("the ");
69/// print!("same ");
70/// print!("line ");
71///
72/// io::stdout().flush().unwrap();
73///
74/// print!("this string has a newline, why not choose println! instead?\n");
75///
76/// io::stdout().flush().unwrap();
77/// ```
78#[macro_export]
79#[stable(feature = "rust1", since = "1.0.0")]
80#[cfg_attr(not(test), rustc_diagnostic_item = "print_macro")]
81#[allow_internal_unstable(print_internals)]
82macro_rules! print {
83    ($($arg:tt)*) => {{
84        $crate::io::_print($crate::format_args!($($arg)*));
85    }};
86}
87
88/// Prints to the standard output, with a newline.
89///
90/// On all platforms, the newline is the LINE FEED character (`\n`/`U+000A`) alone
91/// (no additional CARRIAGE RETURN (`\r`/`U+000D`)).
92///
93/// This macro uses the same syntax as [`format!`], but writes to the standard output instead.
94/// See [`std::fmt`] for more information.
95///
96/// The `println!` macro will lock the standard output on each call. If you call
97/// `println!` within a hot loop, this behavior may be the bottleneck of the loop.
98/// To avoid this, lock stdout with [`io::stdout().lock()`][lock]:
99/// ```
100/// use std::io::{stdout, Write};
101///
102/// let mut lock = stdout().lock();
103/// writeln!(lock, "hello world").unwrap();
104/// ```
105///
106/// Use `println!` only for the primary output of your program. Use
107/// [`eprintln!`] instead to print error and progress messages.
108///
109/// See the formatting documentation in [`std::fmt`](crate::fmt)
110/// for details of the macro argument syntax.
111///
112/// [`std::fmt`]: crate::fmt
113/// [`eprintln!`]: crate::eprintln
114/// [lock]: crate::io::Stdout
115///
116/// # Panics
117///
118/// Panics if writing to [`io::stdout`] fails.
119///
120/// Writing to non-blocking stdout can cause an error, which will lead
121/// this macro to panic.
122///
123/// [`io::stdout`]: crate::io::stdout
124///
125/// # Examples
126///
127/// ```
128/// println!(); // prints just a newline
129/// println!("hello there!");
130/// println!("format {} arguments", "some");
131/// let local_variable = "some";
132/// println!("format {local_variable} arguments");
133/// ```
134#[macro_export]
135#[stable(feature = "rust1", since = "1.0.0")]
136#[cfg_attr(not(test), rustc_diagnostic_item = "println_macro")]
137#[allow_internal_unstable(print_internals, format_args_nl)]
138macro_rules! println {
139    () => {
140        $crate::print!("\n")
141    };
142    ($($arg:tt)*) => {{
143        $crate::io::_print($crate::format_args_nl!($($arg)*));
144    }};
145}
146
147/// Prints to the standard error.
148///
149/// Equivalent to the [`print!`] macro, except that output goes to
150/// [`io::stderr`] instead of [`io::stdout`]. See [`print!`] for
151/// example usage.
152///
153/// Use `eprint!` only for error and progress messages. Use `print!`
154/// instead for the primary output of your program.
155///
156/// [`io::stderr`]: crate::io::stderr
157/// [`io::stdout`]: crate::io::stdout
158///
159/// See the formatting documentation in [`std::fmt`](crate::fmt)
160/// for details of the macro argument syntax.
161///
162/// # Panics
163///
164/// Panics if writing to `io::stderr` fails.
165///
166/// Writing to non-blocking stderr can cause an error, which will lead
167/// this macro to panic.
168///
169/// # Examples
170///
171/// ```
172/// eprint!("Error: Could not complete task");
173/// ```
174#[macro_export]
175#[stable(feature = "eprint", since = "1.19.0")]
176#[cfg_attr(not(test), rustc_diagnostic_item = "eprint_macro")]
177#[allow_internal_unstable(print_internals)]
178macro_rules! eprint {
179    ($($arg:tt)*) => {{
180        $crate::io::_eprint($crate::format_args!($($arg)*));
181    }};
182}
183
184/// Prints to the standard error, with a newline.
185///
186/// Equivalent to the [`println!`] macro, except that output goes to
187/// [`io::stderr`] instead of [`io::stdout`]. See [`println!`] for
188/// example usage.
189///
190/// Use `eprintln!` only for error and progress messages. Use `println!`
191/// instead for the primary output of your program.
192///
193/// See the formatting documentation in [`std::fmt`](crate::fmt)
194/// for details of the macro argument syntax.
195///
196/// [`io::stderr`]: crate::io::stderr
197/// [`io::stdout`]: crate::io::stdout
198/// [`println!`]: crate::println
199///
200/// # Panics
201///
202/// Panics if writing to `io::stderr` fails.
203///
204/// Writing to non-blocking stderr can cause an error, which will lead
205/// this macro to panic.
206///
207/// # Examples
208///
209/// ```
210/// eprintln!("Error: Could not complete task");
211/// ```
212#[macro_export]
213#[stable(feature = "eprint", since = "1.19.0")]
214#[cfg_attr(not(test), rustc_diagnostic_item = "eprintln_macro")]
215#[allow_internal_unstable(print_internals, format_args_nl)]
216macro_rules! eprintln {
217    () => {
218        $crate::eprint!("\n")
219    };
220    ($($arg:tt)*) => {{
221        $crate::io::_eprint($crate::format_args_nl!($($arg)*));
222    }};
223}
224
225/// Prints and returns the value of a given expression for quick and dirty
226/// debugging.
227///
228/// An example:
229///
230/// ```rust
231/// let a = 2;
232/// let b = dbg!(a * 2) + 1;
233/// //      ^-- prints: [src/main.rs:2:9] a * 2 = 4
234/// assert_eq!(b, 5);
235/// ```
236///
237/// The macro works by using the `Debug` implementation of the type of
238/// the given expression to print the value to [stderr] along with the
239/// source location of the macro invocation as well as the source code
240/// of the expression.
241///
242/// Invoking the macro on an expression moves and takes ownership of it
243/// before returning the evaluated expression unchanged. If the type
244/// of the expression does not implement `Copy` and you don't want
245/// to give up ownership, you can instead borrow with `dbg!(&expr)`
246/// for some expression `expr`.
247///
248/// The `dbg!` macro works exactly the same in release builds.
249/// This is useful when debugging issues that only occur in release
250/// builds or when debugging in release mode is significantly faster.
251///
252/// Note that the macro is intended as a debugging tool and therefore you
253/// should avoid having uses of it in version control for long periods
254/// (other than in tests and similar).
255/// Debug output from production code is better done with other facilities
256/// such as the [`debug!`] macro from the [`log`] crate.
257///
258/// # Stability
259///
260/// The exact output printed by this macro should not be relied upon
261/// and is subject to future changes.
262///
263/// # Panics
264///
265/// Panics if writing to `io::stderr` fails.
266///
267/// # Further examples
268///
269/// With a method call:
270///
271/// ```rust
272/// fn foo(n: usize) {
273///     if let Some(_) = dbg!(n.checked_sub(4)) {
274///         // ...
275///     }
276/// }
277///
278/// foo(3)
279/// ```
280///
281/// This prints to [stderr]:
282///
283/// ```text,ignore
284/// [src/main.rs:2:22] n.checked_sub(4) = None
285/// ```
286///
287/// Naive factorial implementation:
288///
289/// ```rust
290/// fn factorial(n: u32) -> u32 {
291///     if dbg!(n <= 1) {
292///         dbg!(1)
293///     } else {
294///         dbg!(n * factorial(n - 1))
295///     }
296/// }
297///
298/// dbg!(factorial(4));
299/// ```
300///
301/// This prints to [stderr]:
302///
303/// ```text,ignore
304/// [src/main.rs:2:8] n <= 1 = false
305/// [src/main.rs:2:8] n <= 1 = false
306/// [src/main.rs:2:8] n <= 1 = false
307/// [src/main.rs:2:8] n <= 1 = true
308/// [src/main.rs:3:9] 1 = 1
309/// [src/main.rs:7:9] n * factorial(n - 1) = 2
310/// [src/main.rs:7:9] n * factorial(n - 1) = 6
311/// [src/main.rs:7:9] n * factorial(n - 1) = 24
312/// [src/main.rs:9:1] factorial(4) = 24
313/// ```
314///
315/// The `dbg!(..)` macro moves the input:
316///
317/// ```compile_fail
318/// /// A wrapper around `usize` which importantly is not Copyable.
319/// #[derive(Debug)]
320/// struct NoCopy(usize);
321///
322/// let a = NoCopy(42);
323/// let _ = dbg!(a); // <-- `a` is moved here.
324/// let _ = dbg!(a); // <-- `a` is moved again; error!
325/// ```
326///
327/// You can also use `dbg!()` without a value to just print the
328/// file and line whenever it's reached.
329///
330/// Finally, if you want to `dbg!(..)` multiple values, it will treat them as
331/// a tuple (and return it, too):
332///
333/// ```
334/// assert_eq!(dbg!(1usize, 2u32), (1, 2));
335/// ```
336///
337/// However, a single argument with a trailing comma will still not be treated
338/// as a tuple, following the convention of ignoring trailing commas in macro
339/// invocations. You can use a 1-tuple directly if you need one:
340///
341/// ```
342/// assert_eq!(1, dbg!(1u32,)); // trailing comma ignored
343/// assert_eq!((1,), dbg!((1u32,))); // 1-tuple
344/// ```
345///
346/// [stderr]: https://en.wikipedia.org/wiki/Standard_streams#Standard_error_(stderr)
347/// [`debug!`]: https://docs.rs/log/*/log/macro.debug.html
348/// [`log`]: https://crates.io/crates/log
349#[macro_export]
350#[cfg_attr(not(test), rustc_diagnostic_item = "dbg_macro")]
351#[stable(feature = "dbg_macro", since = "1.32.0")]
352macro_rules! dbg {
353    // NOTE: We cannot use `concat!` to make a static string as a format argument
354    // of `eprintln!` because `file!` could contain a `{` or
355    // `$val` expression could be a block (`{ .. }`), in which case the `eprintln!`
356    // will be malformed.
357    () => {
358        $crate::eprintln!("[{}:{}:{}]", $crate::file!(), $crate::line!(), $crate::column!())
359    };
360    ($val:expr $(,)?) => {
361        // Use of `match` here is intentional because it affects the lifetimes
362        // of temporaries - https://stackoverflow.com/a/48732525/1063961
363        match $val {
364            tmp => {
365                $crate::eprintln!("[{}:{}:{}] {} = {:#?}",
366                    $crate::file!(),
367                    $crate::line!(),
368                    $crate::column!(),
369                    $crate::stringify!($val),
370                    // The `&T: Debug` check happens here (not in the format literal desugaring)
371                    // to avoid format literal related messages and suggestions.
372                    &&tmp as &dyn $crate::fmt::Debug,
373                );
374                tmp
375            }
376        }
377    };
378    ($($val:expr),+ $(,)?) => {
379        ($($crate::dbg!($val)),+,)
380    };
381}
````