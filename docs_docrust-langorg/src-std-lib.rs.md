---
title: lib.rs - source
url: https://doc.rust-lang.org/src/std/lib.rs.html#1-763
source: crawler
fetched_at: 2026-05-06T21:32:12.350291559-03:00
rendered_js: false
word_count: 3448
summary: This document serves as the primary entry point and guide for understanding the Rust standard library's structure, documentation, and foundational modules.
tags:
    - rust
    - standard-library
    - documentation-guide
    - programming-language
    - modules
    - primitives
category: reference
---

## std/ lib.rs

```rust
1//! # The Rust Standard Library
2//!
3//! The Rust Standard Library is the foundation of portable Rust software, a
4//! set of minimal and battle-tested shared abstractions for the [broader Rust
5//! ecosystem][crates.io]. It offers core types, like [`Vec<T>`] and
6//! [`Option<T>`], library-defined [operations on language
7//! primitives](#primitives), [standard macros](#macros), [I/O] and
8//! [multithreading], among [many other things][other].
9//!
10//! `std` is available to all Rust crates by default. Therefore, the
11//! standard library can be accessed in [`use`] statements through the path
12//! `std`, as in [`use std::env`].
13//!
14//! # How to read this documentation
15//!
16//! If you already know the name of what you are looking for, the fastest way to
17//! find it is to use the <a href="#" onclick="window.searchState.focus();">search
18//! button</a> at the top of the page.
19//!
20//! Otherwise, you may want to jump to one of these useful sections:
21//!
22//! * [`std::*` modules](#modules)
23//! * [Primitive types](#primitives)
24//! * [Standard macros](#macros)
25//! * [The Rust Prelude]
26//!
27//! If this is your first time, the documentation for the standard library is
28//! written to be casually perused. Clicking on interesting things should
29//! generally lead you to interesting places. Still, there are important bits
30//! you don't want to miss, so read on for a tour of the standard library and
31//! its documentation!
32//!
33//! Once you are familiar with the contents of the standard library you may
34//! begin to find the verbosity of the prose distracting. At this stage in your
35//! development you may want to press the
36//! "<svg style="width:0.75rem;height:0.75rem" viewBox="0 0 12 12" stroke="currentColor" fill="none"><path d="M2,2l4,4l4,-4M2,6l4,4l4,-4"/></svg>&nbsp;Summary"
37//! button near the top of the page to collapse it into a more skimmable view.
38//!
39//! While you are looking at the top of the page, also notice the
40//! "Source" link. Rust's API documentation comes with the source
41//! code and you are encouraged to read it. The standard library source is
42//! generally high quality and a peek behind the curtains is
43//! often enlightening.
44//!
45//! # What is in the standard library documentation?
46//!
47//! First of all, The Rust Standard Library is divided into a number of focused
48//! modules, [all listed further down this page](#modules). These modules are
49//! the bedrock upon which all of Rust is forged, and they have mighty names
50//! like [`std::slice`] and [`std::cmp`]. Modules' documentation typically
51//! includes an overview of the module along with examples, and are a smart
52//! place to start familiarizing yourself with the library.
53//!
54//! Second, implicit methods on [primitive types] are documented here. This can
55//! be a source of confusion for two reasons:
56//!
57//! 1. While primitives are implemented by the compiler, the standard library
58//!    implements methods directly on the primitive types (and it is the only
59//!    library that does so), which are [documented in the section on
60//!    primitives](#primitives).
61//! 2. The standard library exports many modules *with the same name as
62//!    primitive types*. These define additional items related to the primitive
63//!    type, but not the all-important methods.
64//!
65//! So for example there is a [page for the primitive type
66//! `char`](primitive::char) that lists all the methods that can be called on
67//! characters (very useful), and there is a [page for the module
68//! `std::char`](crate::char) that documents iterator and error types created by these methods
69//! (rarely useful).
70//!
71//! Note the documentation for the primitives [`str`] and [`[T]`][prim@slice] (also
72//! called 'slice'). Many method calls on [`String`] and [`Vec<T>`] are actually
73//! calls to methods on [`str`] and [`[T]`][prim@slice] respectively, via [deref
74//! coercions][deref-coercions].
75//!
76//! Third, the standard library defines [The Rust Prelude], a small collection
77//! of items - mostly traits - that are imported into every module of every
78//! crate. The traits in the prelude are pervasive, making the prelude
79//! documentation a good entry point to learning about the library.
80//!
81//! And finally, the standard library exports a number of standard macros, and
82//! [lists them on this page](#macros) (technically, not all of the standard
83//! macros are defined by the standard library - some are defined by the
84//! compiler - but they are documented here the same). Like the prelude, the
85//! standard macros are imported by default into all crates.
86//!
87//! # Contributing changes to the documentation
88//!
89//! Check out the Rust contribution guidelines [here](
90//! https://rustc-dev-guide.rust-lang.org/contributing.html#writing-documentation).
91//! The source for this documentation can be found on
92//! [GitHub](https://github.com/rust-lang/rust) in the 'library/std/' directory.
93//! To contribute changes, make sure you read the guidelines first, then submit
94//! pull-requests for your suggested changes.
95//!
96//! Contributions are appreciated! If you see a part of the docs that can be
97//! improved, submit a PR, or chat with us first on [Zulip][rust-zulip]
98//! #docs.
99//!
100//! # A Tour of The Rust Standard Library
101//!
102//! The rest of this crate documentation is dedicated to pointing out notable
103//! features of The Rust Standard Library.
104//!
105//! ## Containers and collections
106//!
107//! The [`option`] and [`result`] modules define optional and error-handling
108//! types, [`Option<T>`] and [`Result<T, E>`]. The [`iter`] module defines
109//! Rust's iterator trait, [`Iterator`], which works with the [`for`] loop to
110//! access collections.
111//!
112//! The standard library exposes three common ways to deal with contiguous
113//! regions of memory:
114//!
115//! * [`Vec<T>`] - A heap-allocated *vector* that is resizable at runtime.
116//! * [`[T; N]`][prim@array] - An inline *array* with a fixed size at compile time.
117//! * [`[T]`][prim@slice] - A dynamically sized *slice* into any other kind of contiguous
118//!   storage, whether heap-allocated or not.
119//!
120//! Slices can only be handled through some kind of *pointer*, and as such come
121//! in many flavors such as:
122//!
123//! * `&[T]` - *shared slice*
124//! * `&mut [T]` - *mutable slice*
125//! * [`Box<[T]>`][owned slice] - *owned slice*
126//!
127//! [`str`], a UTF-8 string slice, is a primitive type, and the standard library
128//! defines many methods for it. Rust [`str`]s are typically accessed as
129//! immutable references: `&str`. Use the owned [`String`] for building and
130//! mutating strings.
131//!
132//! For converting to strings use the [`format!`] macro, and for converting from
133//! strings use the [`FromStr`] trait.
134//!
135//! Data may be shared by placing it in a reference-counted box or the [`Rc`]
136//! type, and if further contained in a [`Cell`] or [`RefCell`], may be mutated
137//! as well as shared. Likewise, in a concurrent setting it is common to pair an
138//! atomically-reference-counted box, [`Arc`], with a [`Mutex`] to get the same
139//! effect.
140//!
141//! The [`collections`] module defines maps, sets, linked lists and other
142//! typical collection types, including the common [`HashMap<K, V>`].
143//!
144//! ## Platform abstractions and I/O
145//!
146//! Besides basic data types, the standard library is largely concerned with
147//! abstracting over differences in common platforms, most notably Windows and
148//! Unix derivatives.
149//!
150//! Common types of I/O, including [files], [TCP], and [UDP], are defined in
151//! the [`io`], [`fs`], and [`net`] modules.
152//!
153//! The [`thread`] module contains Rust's threading abstractions. [`sync`]
154//! contains further primitive shared memory types, including [`atomic`], [`mpmc`] and
155//! [`mpsc`], which contains the channel types for message passing.
156//!
157//! # Use before and after `main()`
158//!
159//! Many parts of the standard library are expected to work before and after `main()`;
160//! but this is not guaranteed or ensured by tests. It is recommended that you write your own tests
161//! and run them on each platform you wish to support.
162//! This means that use of `std` before/after main, especially of features that interact with the
163//! OS or global state, is exempted from stability and portability guarantees and instead only
164//! provided on a best-effort basis. Nevertheless bug reports are appreciated.
165//!
166//! On the other hand `core` and `alloc` are most likely to work in such environments with
167//! the caveat that any hookable behavior such as panics, oom handling or allocators will also
168//! depend on the compatibility of the hooks.
169//!
170//! Some features may also behave differently outside main, e.g. stdio could become unbuffered,
171//! some panics might turn into aborts, backtraces might not get symbolicated or similar.
172//!
173//! Non-exhaustive list of known limitations:
174//!
175//! - after-main use of thread-locals, which also affects additional features:
176//!   - [`thread::current()`]
177//! - under UNIX, before main, file descriptors 0, 1, and 2 may be unchanged
178//!   (they are guaranteed to be open during main,
179//!    and are opened to /dev/null O_RDWR if they weren't open on program start)
180//!
181//!
182//! [I/O]: io
183//! [TCP]: net::TcpStream
184//! [The Rust Prelude]: prelude
185//! [UDP]: net::UdpSocket
186//! [`Arc`]: sync::Arc
187//! [owned slice]: boxed
188//! [`Cell`]: cell::Cell
189//! [`FromStr`]: str::FromStr
190//! [`HashMap<K, V>`]: collections::HashMap
191//! [`Mutex`]: sync::Mutex
192//! [`Option<T>`]: option::Option
193//! [`Rc`]: rc::Rc
194//! [`RefCell`]: cell::RefCell
195//! [`Result<T, E>`]: result::Result
196//! [`Vec<T>`]: vec::Vec
197//! [`atomic`]: sync::atomic
198//! [`for`]: ../book/ch03-05-control-flow.html#looping-through-a-collection-with-for
199//! [`str`]: prim@str
200//! [`mpmc`]: sync::mpmc
201//! [`mpsc`]: sync::mpsc
202//! [`std::cmp`]: cmp
203//! [`std::slice`]: mod@slice
204//! [`use std::env`]: env/index.html
205//! [`use`]: ../book/ch07-02-defining-modules-to-control-scope-and-privacy.html
206//! [crates.io]: https://crates.io
207//! [deref-coercions]: ../book/ch15-02-deref.html#implicit-deref-coercions-with-functions-and-methods
208//! [files]: fs::File
209//! [multithreading]: thread
210//! [other]: #what-is-in-the-standard-library-documentation
211//! [primitive types]: ../book/ch03-02-data-types.html
212//! [rust-zulip]: https://rust-lang.zulipchat.com/
213//! [array]: prim@array
214//! [slice]: prim@slice
215
216#![cfg_attr(not(restricted_std), stable(feature = "rust1", since = "1.0.0"))]
217#![cfg_attr(
218    restricted_std,
219    unstable(
220        feature = "restricted_std",
221        issue = "none",
222        reason = "You have attempted to use a standard library built for a platform that it doesn't \
223            know how to support. Consider building it for a known environment, disabling it with \
224            `#![no_std]` or overriding this warning by enabling this feature."
225    )
226)]
227#![rustc_preserve_ub_checks]
228#![doc(
229    html_playground_url = "https://play.rust-lang.org/",
230    issue_tracker_base_url = "https://github.com/rust-lang/rust/issues/",
231    test(no_crate_inject, attr(deny(warnings))),
232    test(attr(allow(dead_code, deprecated, unused_variables, unused_mut)))
233)]
234#![doc(rust_logo)]
235#![doc(auto_cfg(hide(no_global_oom_handling)))]
236// Don't link to std. We are std.
237#![no_std]
238// Tell the compiler to link to either panic_abort or panic_unwind
239#![needs_panic_runtime]
240//
241// Lints:
242#![warn(deprecated_in_future)]
243#![warn(missing_docs)]
244#![warn(missing_debug_implementations)]
245#![allow(explicit_outlives_requirements)]
246#![allow(unused_lifetimes)]
247#![allow(internal_features)]
248#![deny(fuzzy_provenance_casts)]
249#![deny(unsafe_op_in_unsafe_fn)]
250#![allow(rustdoc::redundant_explicit_links)]
251#![warn(rustdoc::unescaped_backticks)]
252// Ensure that std can be linked against panic_abort despite compiled with `-C panic=unwind`
253#![deny(ffi_unwind_calls)]
254// std may use features in a platform-specific way
255#![allow(unused_features)]
256//
257// Features:
258#![cfg_attr(test, feature(internal_output_capture, print_internals, update_panic_count, rt))]
259#![cfg_attr(
260    all(target_vendor = "fortanix", target_env = "sgx"),
261    feature(slice_index_methods, coerce_unsized, sgx_platform)
262)]
263#![cfg_attr(all(test, target_os = "uefi"), feature(uefi_std))]
264#![cfg_attr(target_family = "wasm", feature(stdarch_wasm_atomic_wait))]
265#![cfg_attr(target_arch = "wasm64", feature(simd_wasm64))]
266//
267// Language features:
268// tidy-alphabetical-start
269#![feature(alloc_error_handler)]
270#![feature(allocator_internals)]
271#![feature(allow_internal_unsafe)]
272#![feature(allow_internal_unstable)]
273#![feature(asm_experimental_arch)]
274#![feature(autodiff)]
275#![feature(cfg_sanitizer_cfi)]
276#![feature(cfg_target_thread_local)]
277#![feature(cfi_encoding)]
278#![feature(const_default)]
279#![feature(const_trait_impl)]
280#![feature(core_float_math)]
281#![feature(decl_macro)]
282#![feature(deprecated_suggestion)]
283#![feature(doc_cfg)]
284#![feature(doc_masked)]
285#![feature(doc_notable_trait)]
286#![feature(dropck_eyepatch)]
287#![feature(f16)]
288#![feature(f128)]
289#![feature(ffi_const)]
290#![feature(formatting_options)]
291#![feature(funnel_shifts)]
292#![feature(intra_doc_pointers)]
293#![feature(iter_advance_by)]
294#![feature(iter_next_chunk)]
295#![feature(lang_items)]
296#![feature(link_cfg)]
297#![feature(linkage)]
298#![feature(macro_metavar_expr_concat)]
299#![feature(maybe_uninit_fill)]
300#![feature(min_specialization)]
301#![feature(must_not_suspend)]
302#![feature(needs_panic_runtime)]
303#![feature(negative_impls)]
304#![feature(never_type)]
305#![feature(optimize_attribute)]
306#![feature(prelude_import)]
307#![feature(rustc_attrs)]
308#![feature(rustdoc_internals)]
309#![feature(staged_api)]
310#![feature(stmt_expr_attributes)]
311#![feature(strict_provenance_lints)]
312#![feature(target_feature_inline_always)]
313#![feature(thread_local)]
314#![feature(try_blocks)]
315#![feature(try_trait_v2)]
316#![feature(type_alias_impl_trait)]
317#![feature(uint_carryless_mul)]
318// tidy-alphabetical-end
319//
320// Library features (core):
321// tidy-alphabetical-start
322#![feature(bstr)]
323#![feature(bstr_internals)]
324#![feature(cast_maybe_uninit)]
325#![feature(char_internals)]
326#![feature(clone_to_uninit)]
327#![feature(const_convert)]
328#![feature(core_intrinsics)]
329#![feature(core_io_borrowed_buf)]
330#![feature(cstr_display)]
331#![feature(drop_guard)]
332#![feature(duration_constants)]
333#![feature(error_generic_member_access)]
334#![feature(error_iter)]
335#![feature(exact_size_is_empty)]
336#![feature(exclusive_wrapper)]
337#![feature(extend_one)]
338#![feature(float_algebraic)]
339#![feature(float_gamma)]
340#![feature(float_minimum_maximum)]
341#![feature(fmt_internals)]
342#![feature(fn_ptr_trait)]
343#![feature(generic_atomic)]
344#![feature(hasher_prefixfree_extras)]
345#![feature(hashmap_internals)]
346#![feature(hint_must_use)]
347#![feature(int_from_ascii)]
348#![feature(ip)]
349#![feature(maybe_uninit_array_assume_init)]
350#![feature(panic_can_unwind)]
351#![feature(panic_internals)]
352#![feature(pin_coerce_unsized_trait)]
353#![feature(pointer_is_aligned_to)]
354#![feature(portable_simd)]
355#![feature(ptr_as_uninit)]
356#![feature(ptr_mask)]
357#![feature(random)]
358#![feature(slice_internals)]
359#![feature(slice_ptr_get)]
360#![feature(slice_range)]
361#![feature(slice_split_once)]
362#![feature(std_internals)]
363#![feature(str_internals)]
364#![feature(sync_unsafe_cell)]
365#![feature(temporary_niche_types)]
366#![feature(ub_checks)]
367#![feature(used_with_arg)]
368// tidy-alphabetical-end
369//
370// Library features (alloc):
371// tidy-alphabetical-start
372#![feature(allocator_api)]
373#![feature(clone_from_ref)]
374#![feature(get_mut_unchecked)]
375#![feature(map_try_insert)]
376#![feature(slice_concat_trait)]
377#![feature(thin_box)]
378#![feature(try_reserve_kind)]
379#![feature(try_with_capacity)]
380#![feature(unique_rc_arc)]
381#![feature(wtf8_internals)]
382// tidy-alphabetical-end
383//
384// Library features (unwind):
385// tidy-alphabetical-start
386#![feature(panic_unwind)]
387// tidy-alphabetical-end
388//
389// Library features (std_detect):
390// tidy-alphabetical-start
391#![feature(stdarch_internal)]
392// tidy-alphabetical-end
393//
394// Only for re-exporting:
395// tidy-alphabetical-start
396#![feature(assert_matches)]
397#![feature(async_iterator)]
398#![feature(c_variadic)]
399#![feature(cfg_accessible)]
400#![feature(cfg_eval)]
401#![feature(concat_bytes)]
402#![feature(const_format_args)]
403#![feature(custom_test_frameworks)]
404#![feature(edition_panic)]
405#![feature(format_args_nl)]
406#![feature(log_syntax)]
407#![feature(test)]
408#![feature(trace_macros)]
409// tidy-alphabetical-end
410//
411// Only used in tests/benchmarks:
412//
413// Only for const-ness:
414// tidy-alphabetical-start
415#![feature(io_const_error)]
416// tidy-alphabetical-end
417//
418#![default_lib_allocator]
419
420// The Rust prelude
421// The compiler expects the prelude definition to be defined before its use statement.
422pub mod prelude;
423
424// Explicitly import the prelude. The compiler uses this same unstable attribute
425// to import the prelude implicitly when building crates that depend on std.
426#[prelude_import]
427#[allow(unused)]
428use prelude::rust_2024::*;
429
430// Access to Bencher, etc.
431#[cfg(test)]
432extern crate test;
433
434#[allow(unused_imports)] // macros from `alloc` are not used on all platforms
435#[macro_use]
436extern crate alloc as alloc_crate;
437
438// Many compiler tests depend on libc being pulled in by std
439// so include it here even if it's unused.
440#[doc(masked)]
441#[allow(unused_extern_crates)]
442#[cfg(not(all(windows, target_env = "msvc")))]
443extern crate libc;
444
445// We always need an unwinder currently for backtraces
446#[doc(masked)]
447#[allow(unused_extern_crates)]
448extern crate unwind;
449
450// FIXME: #94122 this extern crate definition only exist here to stop
451// miniz_oxide docs leaking into std docs. Find better way to do it.
452// Remove exclusion from tidy platform check when this removed.
453#[doc(masked)]
454#[allow(unused_extern_crates)]
455#[cfg(all(
456    not(all(windows, target_env = "msvc", not(target_vendor = "uwp"))),
457    feature = "miniz_oxide"
458))]
459extern crate miniz_oxide;
460
461// During testing, this crate is not actually the "real" std library, but rather
462// it links to the real std library, which was compiled from this same source
463// code. So any lang items std defines are conditionally excluded (or else they
464// would generate duplicate lang item errors), and any globals it defines are
465// _not_ the globals used by "real" std. So this import, defined only during
466// testing gives test-std access to real-std lang items and globals. See #2912
467#[cfg(test)]
468extern crate std as realstd;
469
470// The standard macros that are not built-in to the compiler.
471#[macro_use]
472mod macros;
473
474// The runtime entry point and a few unstable public functions used by the
475// compiler
476#[macro_use]
477pub mod rt;
478
479#[stable(feature = "rust1", since = "1.0.0")]
480pub use core::any;
481#[stable(feature = "core_array", since = "1.35.0")]
482pub use core::array;
483#[unstable(feature = "async_iterator", issue = "79024")]
484pub use core::async_iter;
485#[stable(feature = "rust1", since = "1.0.0")]
486pub use core::cell;
487#[stable(feature = "rust1", since = "1.0.0")]
488pub use core::char;
489#[stable(feature = "rust1", since = "1.0.0")]
490pub use core::clone;
491#[stable(feature = "rust1", since = "1.0.0")]
492pub use core::cmp;
493#[stable(feature = "rust1", since = "1.0.0")]
494pub use core::convert;
495#[stable(feature = "rust1", since = "1.0.0")]
496pub use core::default;
497#[stable(feature = "futures_api", since = "1.36.0")]
498pub use core::future;
499#[stable(feature = "core_hint", since = "1.27.0")]
500pub use core::hint;
501#[stable(feature = "rust1", since = "1.0.0")]
502#[allow(deprecated, deprecated_in_future)]
503pub use core::i8;
504#[stable(feature = "rust1", since = "1.0.0")]
505#[allow(deprecated, deprecated_in_future)]
506pub use core::i16;
507#[stable(feature = "rust1", since = "1.0.0")]
508#[allow(deprecated, deprecated_in_future)]
509pub use core::i32;
510#[stable(feature = "rust1", since = "1.0.0")]
511#[allow(deprecated, deprecated_in_future)]
512pub use core::i64;
513#[stable(feature = "i128", since = "1.26.0")]
514#[allow(deprecated, deprecated_in_future)]
515pub use core::i128;
516#[stable(feature = "rust1", since = "1.0.0")]
517pub use core::intrinsics;
518#[stable(feature = "rust1", since = "1.0.0")]
519#[allow(deprecated, deprecated_in_future)]
520pub use core::isize;
521#[stable(feature = "rust1", since = "1.0.0")]
522pub use core::iter;
523#[stable(feature = "rust1", since = "1.0.0")]
524pub use core::marker;
525#[stable(feature = "rust1", since = "1.0.0")]
526pub use core::mem;
527#[stable(feature = "rust1", since = "1.0.0")]
528pub use core::ops;
529#[stable(feature = "rust1", since = "1.0.0")]
530pub use core::option;
531#[stable(feature = "pin", since = "1.33.0")]
532pub use core::pin;
533#[stable(feature = "rust1", since = "1.0.0")]
534pub use core::ptr;
535#[unstable(feature = "new_range_api", issue = "125687")]
536pub use core::range;
537#[stable(feature = "rust1", since = "1.0.0")]
538pub use core::result;
539#[stable(feature = "rust1", since = "1.0.0")]
540#[allow(deprecated, deprecated_in_future)]
541pub use core::u8;
542#[stable(feature = "rust1", since = "1.0.0")]
543#[allow(deprecated, deprecated_in_future)]
544pub use core::u16;
545#[stable(feature = "rust1", since = "1.0.0")]
546#[allow(deprecated, deprecated_in_future)]
547pub use core::u32;
548#[stable(feature = "rust1", since = "1.0.0")]
549#[allow(deprecated, deprecated_in_future)]
550pub use core::u64;
551#[stable(feature = "i128", since = "1.26.0")]
552#[allow(deprecated, deprecated_in_future)]
553pub use core::u128;
554#[unstable(feature = "unsafe_binders", issue = "130516")]
555pub use core::unsafe_binder;
556#[stable(feature = "rust1", since = "1.0.0")]
557#[allow(deprecated, deprecated_in_future)]
558pub use core::usize;
559
560#[stable(feature = "rust1", since = "1.0.0")]
561pub use alloc_crate::borrow;
562#[stable(feature = "rust1", since = "1.0.0")]
563pub use alloc_crate::boxed;
564#[stable(feature = "rust1", since = "1.0.0")]
565pub use alloc_crate::fmt;
566#[stable(feature = "rust1", since = "1.0.0")]
567pub use alloc_crate::format;
568#[stable(feature = "rust1", since = "1.0.0")]
569pub use alloc_crate::rc;
570#[stable(feature = "rust1", since = "1.0.0")]
571pub use alloc_crate::slice;
572#[stable(feature = "rust1", since = "1.0.0")]
573pub use alloc_crate::str;
574#[stable(feature = "rust1", since = "1.0.0")]
575pub use alloc_crate::string;
576#[stable(feature = "rust1", since = "1.0.0")]
577pub use alloc_crate::vec;
578
579#[path = "num/f128.rs"]
580pub mod f128;
581#[path = "num/f16.rs"]
582pub mod f16;
583#[path = "num/f32.rs"]
584pub mod f32;
585#[path = "num/f64.rs"]
586pub mod f64;
587
588#[macro_use]
589pub mod thread;
590pub mod ascii;
591pub mod backtrace;
592#[unstable(feature = "bstr", issue = "134915")]
593pub mod bstr;
594pub mod collections;
595pub mod env;
596pub mod error;
597pub mod ffi;
598pub mod fs;
599pub mod hash;
600pub mod io;
601pub mod net;
602pub mod num;
603pub mod os;
604pub mod panic;
605#[unstable(feature = "pattern_type_macro", issue = "123646")]
606pub mod pat;
607pub mod path;
608pub mod process;
609#[unstable(feature = "random", issue = "130703")]
610pub mod random;
611pub mod sync;
612pub mod time;
613
614// Pull in `std_float` crate  into std. The contents of
615// `std_float` are in a different repository: rust-lang/portable-simd.
616#[path = "../../portable-simd/crates/std_float/src/lib.rs"]
617#[allow(missing_debug_implementations, dead_code, unsafe_op_in_unsafe_fn)]
618#[allow(rustdoc::bare_urls)]
619#[unstable(feature = "portable_simd", issue = "86656")]
620mod std_float;
621
622#[unstable(feature = "portable_simd", issue = "86656")]
623pub mod simd {
624    #![doc = include_str!("../../portable-simd/crates/core_simd/src/core_simd_docs.md")]
625
626    #[doc(inline)]
627    pub use core::simd::*;
628
629    #[doc(inline)]
630    pub use crate::std_float::StdFloat;
631}
632
633#[unstable(feature = "autodiff", issue = "124509")]
634/// This module provides support for automatic differentiation.
635pub mod autodiff {
636    /// This macro handles automatic differentiation.
637    pub use core::autodiff::{autodiff_forward, autodiff_reverse};
638}
639
640#[stable(feature = "futures_api", since = "1.36.0")]
641pub mod task {
642    //! Types and Traits for working with asynchronous tasks.
643
644    #[doc(inline)]
645    #[stable(feature = "wake_trait", since = "1.51.0")]
646    pub use alloc::task::*;
647    #[doc(inline)]
648    #[stable(feature = "futures_api", since = "1.36.0")]
649    pub use core::task::*;
650}
651
652#[doc = include_str!("../../stdarch/crates/core_arch/src/core_arch_docs.md")]
653#[stable(feature = "simd_arch", since = "1.27.0")]
654pub mod arch {
655    #[stable(feature = "simd_arch", since = "1.27.0")]
656    // The `no_inline`-attribute is required to make the documentation of all
657    // targets available.
658    // See https://github.com/rust-lang/rust/pull/57808#issuecomment-457390549 for
659    // more information.
660    #[doc(no_inline)] // Note (#82861): required for correct documentation
661    pub use core::arch::*;
662
663    #[stable(feature = "simd_aarch64", since = "1.60.0")]
664    pub use std_detect::is_aarch64_feature_detected;
665    #[unstable(feature = "stdarch_arm_feature_detection", issue = "111190")]
666    pub use std_detect::is_arm_feature_detected;
667    #[unstable(feature = "is_loongarch_feature_detected", issue = "117425")]
668    pub use std_detect::is_loongarch_feature_detected;
669    #[unstable(feature = "is_riscv_feature_detected", issue = "111192")]
670    pub use std_detect::is_riscv_feature_detected;
671    #[stable(feature = "stdarch_s390x_feature_detection", since = "1.93.0")]
672    pub use std_detect::is_s390x_feature_detected;
673    #[stable(feature = "simd_x86", since = "1.27.0")]
674    pub use std_detect::is_x86_feature_detected;
675    #[unstable(feature = "stdarch_mips_feature_detection", issue = "111188")]
676    pub use std_detect::{is_mips_feature_detected, is_mips64_feature_detected};
677    #[unstable(feature = "stdarch_powerpc_feature_detection", issue = "111191")]
678    pub use std_detect::{is_powerpc_feature_detected, is_powerpc64_feature_detected};
679}
680
681// This was stabilized in the crate root so we have to keep it there.
682#[stable(feature = "simd_x86", since = "1.27.0")]
683pub use std_detect::is_x86_feature_detected;
684
685mod sys;
686
687pub mod alloc;
688
689// Private support modules
690mod panicking;
691
692#[path = "../../backtrace/src/lib.rs"]
693#[allow(dead_code, unused_attributes, fuzzy_provenance_casts, unsafe_op_in_unsafe_fn)]
694mod backtrace_rs;
695
696#[stable(feature = "cfg_select", since = "1.95.0")]
697pub use core::cfg_select;
698#[unstable(
699    feature = "concat_bytes",
700    issue = "87555",
701    reason = "`concat_bytes` is not stable enough for use and is subject to change"
702)]
703pub use core::concat_bytes;
704#[stable(feature = "matches_macro", since = "1.42.0")]
705#[allow(deprecated, deprecated_in_future)]
706pub use core::matches;
707#[stable(feature = "core_primitive", since = "1.43.0")]
708pub use core::primitive;
709#[stable(feature = "todo_macro", since = "1.40.0")]
710#[allow(deprecated, deprecated_in_future)]
711pub use core::todo;
712// Re-export built-in macros defined through core.
713#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
714pub use core::{
715    assert, cfg, column, compile_error, concat, const_format_args, env, file, format_args,
716    format_args_nl, include, include_bytes, include_str, line, log_syntax, module_path, option_env,
717    stringify, trace_macros,
718};
719// Re-export macros defined in core.
720#[stable(feature = "rust1", since = "1.0.0")]
721#[allow(deprecated, deprecated_in_future)]
722pub use core::{
723    assert_eq, assert_ne, debug_assert, debug_assert_eq, debug_assert_ne, r#try, unimplemented,
724    unreachable, write, writeln,
725};
726#[unstable(feature = "assert_matches", issue = "82775")]
727pub use core::{assert_matches, debug_assert_matches};
728
729// Re-export unstable derive macro defined through core.
730#[unstable(feature = "derive_from", issue = "144889")]
731/// Unstable module containing the unstable `From` derive macro.
732pub mod from {
733    #[unstable(feature = "derive_from", issue = "144889")]
734    pub use core::from::From;
735}
736
737// Include a number of private modules that exist solely to provide
738// the rustdoc documentation for primitive types. Using `include!`
739// because rustdoc only looks for these modules at the crate level.
740include!("../../core/src/primitive_docs.rs");
741
742// Include a number of private modules that exist solely to provide
743// the rustdoc documentation for the existing keywords. Using `include!`
744// because rustdoc only looks for these modules at the crate level.
745include!("keyword_docs.rs");
746
747// This is required to avoid an unstable error when `restricted-std` is not
748// enabled. The use of #![feature(restricted_std)] in rustc-std-workspace-std
749// is unconditional, so the unstable feature needs to be defined somewhere.
750#[unstable(feature = "restricted_std", issue = "none")]
751mod __restricted_std_workaround {}
752
753mod sealed {
754    /// This trait being unreachable from outside the crate
755    /// prevents outside implementations of our extension traits.
756    /// This allows adding more trait methods in the future.
757    #[unstable(feature = "sealed", issue = "none")]
758    pub trait Sealed {}
759}
760
761#[cfg(test)]
762#[allow(dead_code)] // Not used in all configurations.
763pub(crate) mod test_helpers;
```