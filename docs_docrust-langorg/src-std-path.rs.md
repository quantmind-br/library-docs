---
title: path.rs - source
url: https://doc.rust-lang.org/src/std/path.rs.html#3810-3812
source: crawler
fetched_at: 2026-05-06T21:23:06.933089492-03:00
rendered_js: false
word_count: 15778
summary: This document provides an overview of Rust's cross-platform path manipulation module, explaining the use of Path and PathBuf for handling file system paths and specific Windows path prefix structures.
tags:
    - rust
    - filesystem
    - path-manipulation
    - windows-api
    - cross-platform
category: reference
---

## std/ path.rs

````rust
1//! Cross-platform path manipulation.
2//!
3//! This module provides two types, [`PathBuf`] and [`Path`] (akin to [`String`]
4//! and [`str`]), for working with paths abstractly. These types are thin wrappers
5//! around [`OsString`] and [`OsStr`] respectively, meaning that they work directly
6//! on strings according to the local platform's path syntax.
7//!
8//! Paths can be parsed into [`Component`]s by iterating over the structure
9//! returned by the [`components`] method on [`Path`]. [`Component`]s roughly
10//! correspond to the substrings between path separators (`/` or `\`). You can
11//! reconstruct an equivalent path from components with the [`push`] method on
12//! [`PathBuf`]; note that the paths may differ syntactically by the
13//! normalization described in the documentation for the [`components`] method.
14//!
15//! ## Case sensitivity
16//!
17//! Unless otherwise indicated path methods that do not access the filesystem,
18//! such as [`Path::starts_with`] and [`Path::ends_with`], are case sensitive no
19//! matter the platform or filesystem. An exception to this is made for Windows
20//! drive letters.
21//!
22//! ## Path normalization
23//!
24//! Several methods in this module perform basic path normalization by disregarding
25//! repeated separators, non-leading `.` components, and trailing separators. These include:
26//! - Methods for iteration, such as [`Path::components`] and [`Path::iter`]
27//! - Methods for inspection, such as [`Path::has_root`]
28//! - Comparisons using [`PartialEq`], [`PartialOrd`], and [`Ord`]
29//!
30//! [`Path::join`] and [`PathBuf::push`] also disregard trailing slashes.
31//!
32// FIXME(normalize_lexically): mention normalize_lexically once stable
33//! These methods **do not** resolve `..` components or symlinks. For full normalization
34//! including `..` resolution, use [`Path::canonicalize`] (which does access the filesystem).
35//!
36//! ## Simple usage
37//!
38//! Path manipulation includes both parsing components from slices and building
39//! new owned paths.
40//!
41//! To parse a path, you can create a [`Path`] slice from a [`str`]
42//! slice and start asking questions:
43//!
44//! ```
45//! use std::path::Path;
46//! use std::ffi::OsStr;
47//!
48//! let path = Path::new("/tmp/foo/bar.txt");
49//!
50//! let parent = path.parent();
51//! assert_eq!(parent, Some(Path::new("/tmp/foo")));
52//!
53//! let file_stem = path.file_stem();
54//! assert_eq!(file_stem, Some(OsStr::new("bar")));
55//!
56//! let extension = path.extension();
57//! assert_eq!(extension, Some(OsStr::new("txt")));
58//! ```
59//!
60//! To build or modify paths, use [`PathBuf`]:
61//!
62//! ```
63//! use std::path::PathBuf;
64//!
65//! // This way works...
66//! let mut path = PathBuf::from("c:\\");
67//!
68//! path.push("windows");
69//! path.push("system32");
70//!
71//! path.set_extension("dll");
72//!
73//! // ... but push is best used if you don't know everything up
74//! // front. If you do, this way is better:
75//! let path: PathBuf = ["c:\\", "windows", "system32.dll"].iter().collect();
76//! ```
77//!
78//! [`components`]: Path::components
79//! [`push`]: PathBuf::push
80
81#![stable(feature = "rust1", since = "1.0.0")]
82#![deny(unsafe_op_in_unsafe_fn)]
83
84use core::clone::CloneToUninit;
85
86use crate::borrow::{Borrow, Cow};
87use crate::collections::TryReserveError;
88use crate::error::Error;
89use crate::ffi::{OsStr, OsString, os_str};
90use crate::hash::{Hash, Hasher};
91use crate::iter::FusedIterator;
92use crate::ops::{self, Deref};
93use crate::rc::Rc;
94use crate::str::FromStr;
95use crate::sync::Arc;
96use crate::sys::path::{HAS_PREFIXES, MAIN_SEP_STR, is_sep_byte, is_verbatim_sep, parse_prefix};
97use crate::{cmp, fmt, fs, io, sys};
98
99////////////////////////////////////////////////////////////////////////////////
100// GENERAL NOTES
101////////////////////////////////////////////////////////////////////////////////
102//
103// Parsing in this module is done by directly transmuting OsStr to [u8] slices,
104// taking advantage of the fact that OsStr always encodes ASCII characters
105// as-is.  Eventually, this transmutation should be replaced by direct uses of
106// OsStr APIs for parsing, but it will take a while for those to become
107// available.
108
109////////////////////////////////////////////////////////////////////////////////
110// Windows Prefixes
111////////////////////////////////////////////////////////////////////////////////
112
113/// Windows path prefixes, e.g., `C:` or `\\server\share`.
114///
115/// Windows uses a variety of path prefix styles, including references to drive
116/// volumes (like `C:`), network shared folders (like `\\server\share`), and
117/// others. In addition, some path prefixes are "verbatim" (i.e., prefixed with
118/// `\\?\`), in which case `/` is *not* treated as a separator and essentially
119/// no normalization is performed.
120///
121/// # Examples
122///
123/// ```
124/// use std::path::{Component, Path, Prefix};
125/// use std::path::Prefix::*;
126/// use std::ffi::OsStr;
127///
128/// fn get_path_prefix(s: &str) -> Prefix<'_> {
129///     let path = Path::new(s);
130///     match path.components().next().unwrap() {
131///         Component::Prefix(prefix_component) => prefix_component.kind(),
132///         _ => panic!(),
133///     }
134/// }
135///
136/// # if cfg!(windows) {
137/// assert_eq!(Verbatim(OsStr::new("pictures")),
138///            get_path_prefix(r"\\?\pictures\kittens"));
139/// assert_eq!(VerbatimUNC(OsStr::new("server"), OsStr::new("share")),
140///            get_path_prefix(r"\\?\UNC\server\share"));
141/// assert_eq!(VerbatimDisk(b'C'), get_path_prefix(r"\\?\c:\"));
142/// assert_eq!(DeviceNS(OsStr::new("BrainInterface")),
143///            get_path_prefix(r"\\.\BrainInterface"));
144/// assert_eq!(UNC(OsStr::new("server"), OsStr::new("share")),
145///            get_path_prefix(r"\\server\share"));
146/// assert_eq!(Disk(b'C'), get_path_prefix(r"C:\Users\Rust\Pictures\Ferris"));
147/// # }
148/// ```
149#[derive(Copy, Clone, Debug, Hash, PartialOrd, Ord, PartialEq, Eq)]
150#[stable(feature = "rust1", since = "1.0.0")]
151pub enum Prefix<'a> {
152    /// Verbatim prefix, e.g., `\\?\cat_pics`.
153    ///
154    /// Verbatim prefixes consist of `\\?\` immediately followed by the given
155    /// component.
156    #[stable(feature = "rust1", since = "1.0.0")]
157    Verbatim(#[stable(feature = "rust1", since = "1.0.0")] &'a OsStr),
158
159    /// Verbatim prefix using Windows' _**U**niform **N**aming **C**onvention_,
160    /// e.g., `\\?\UNC\server\share`.
161    ///
162    /// Verbatim UNC prefixes consist of `\\?\UNC\` immediately followed by the
163    /// server's hostname and a share name.
164    #[stable(feature = "rust1", since = "1.0.0")]
165    VerbatimUNC(
166        #[stable(feature = "rust1", since = "1.0.0")] &'a OsStr,
167        #[stable(feature = "rust1", since = "1.0.0")] &'a OsStr,
168    ),
169
170    /// Verbatim disk prefix, e.g., `\\?\C:`.
171    ///
172    /// Verbatim disk prefixes consist of `\\?\` immediately followed by the
173    /// drive letter and `:`.
174    #[stable(feature = "rust1", since = "1.0.0")]
175    VerbatimDisk(#[stable(feature = "rust1", since = "1.0.0")] u8),
176
177    /// Device namespace prefix, e.g., `\\.\COM42`.
178    ///
179    /// Device namespace prefixes consist of `\\.\` (possibly using `/`
180    /// instead of `\`), immediately followed by the device name.
181    #[stable(feature = "rust1", since = "1.0.0")]
182    DeviceNS(#[stable(feature = "rust1", since = "1.0.0")] &'a OsStr),
183
184    /// Prefix using Windows' _**U**niform **N**aming **C**onvention_, e.g.
185    /// `\\server\share`.
186    ///
187    /// UNC prefixes consist of the server's hostname and a share name.
188    #[stable(feature = "rust1", since = "1.0.0")]
189    UNC(
190        #[stable(feature = "rust1", since = "1.0.0")] &'a OsStr,
191        #[stable(feature = "rust1", since = "1.0.0")] &'a OsStr,
192    ),
193
194    /// Prefix `C:` for the given disk drive.
195    #[stable(feature = "rust1", since = "1.0.0")]
196    Disk(#[stable(feature = "rust1", since = "1.0.0")] u8),
197}
198
199impl<'a> Prefix<'a> {
200    #[inline]
201    fn len(&self) -> usize {
202        use self::Prefix::*;
203        fn os_str_len(s: &OsStr) -> usize {
204            s.as_encoded_bytes().len()
205        }
206        match *self {
207            Verbatim(x) => 4 + os_str_len(x),
208            VerbatimUNC(x, y) => {
209                8 + os_str_len(x) + if os_str_len(y) > 0 { 1 + os_str_len(y) } else { 0 }
210            }
211            VerbatimDisk(_) => 6,
212            UNC(x, y) => 2 + os_str_len(x) + if os_str_len(y) > 0 { 1 + os_str_len(y) } else { 0 },
213            DeviceNS(x) => 4 + os_str_len(x),
214            Disk(_) => 2,
215        }
216    }
217
218    /// Determines if the prefix is verbatim, i.e., begins with `\\?\`.
219    ///
220    /// # Examples
221    ///
222    /// ```
223    /// use std::path::Prefix::*;
224    /// use std::ffi::OsStr;
225    ///
226    /// assert!(Verbatim(OsStr::new("pictures")).is_verbatim());
227    /// assert!(VerbatimUNC(OsStr::new("server"), OsStr::new("share")).is_verbatim());
228    /// assert!(VerbatimDisk(b'C').is_verbatim());
229    /// assert!(!DeviceNS(OsStr::new("BrainInterface")).is_verbatim());
230    /// assert!(!UNC(OsStr::new("server"), OsStr::new("share")).is_verbatim());
231    /// assert!(!Disk(b'C').is_verbatim());
232    /// ```
233    #[inline]
234    #[must_use]
235    #[stable(feature = "rust1", since = "1.0.0")]
236    pub fn is_verbatim(&self) -> bool {
237        use self::Prefix::*;
238        matches!(*self, Verbatim(_) | VerbatimDisk(_) | VerbatimUNC(..))
239    }
240
241    #[inline]
242    fn is_drive(&self) -> bool {
243        matches!(*self, Prefix::Disk(_))
244    }
245
246    #[inline]
247    fn has_implicit_root(&self) -> bool {
248        !self.is_drive()
249    }
250}
251
252////////////////////////////////////////////////////////////////////////////////
253// Exposed parsing helpers
254////////////////////////////////////////////////////////////////////////////////
255
256/// Determines whether the character is one of the permitted path
257/// separators for the current platform.
258///
259/// # Examples
260///
261/// ```
262/// use std::path;
263///
264/// assert!(path::is_separator('/')); // '/' works for both Unix and Windows
265/// assert!(!path::is_separator('❤'));
266/// ```
267#[must_use]
268#[stable(feature = "rust1", since = "1.0.0")]
269pub fn is_separator(c: char) -> bool {
270    c.is_ascii() && is_sep_byte(c as u8)
271}
272
273/// The primary separator of path components for the current platform.
274///
275/// For example, `/` on Unix and `\` on Windows.
276#[stable(feature = "rust1", since = "1.0.0")]
277#[cfg_attr(not(test), rustc_diagnostic_item = "path_main_separator")]
278pub const MAIN_SEPARATOR: char = crate::sys::path::MAIN_SEP;
279
280/// The primary separator of path components for the current platform.
281///
282/// For example, `/` on Unix and `\` on Windows.
283#[stable(feature = "main_separator_str", since = "1.68.0")]
284pub const MAIN_SEPARATOR_STR: &str = crate::sys::path::MAIN_SEP_STR;
285
286////////////////////////////////////////////////////////////////////////////////
287// Misc helpers
288////////////////////////////////////////////////////////////////////////////////
289
290// Iterate through `iter` while it matches `prefix`; return `None` if `prefix`
291// is not a prefix of `iter`, otherwise return `Some(iter_after_prefix)` giving
292// `iter` after having exhausted `prefix`.
293fn iter_after<'a, 'b, I, J>(mut iter: I, mut prefix: J) -> Option<I>
294where
295    I: Iterator<Item = Component<'a>> + Clone,
296    J: Iterator<Item = Component<'b>>,
297{
298    loop {
299        let mut iter_next = iter.clone();
300        match (iter_next.next(), prefix.next()) {
301            (Some(ref x), Some(ref y)) if x == y => (),
302            (Some(_), Some(_)) => return None,
303            (Some(_), None) => return Some(iter),
304            (None, None) => return Some(iter),
305            (None, Some(_)) => return None,
306        }
307        iter = iter_next;
308    }
309}
310
311////////////////////////////////////////////////////////////////////////////////
312// Cross-platform, iterator-independent parsing
313////////////////////////////////////////////////////////////////////////////////
314
315/// Says whether the first byte after the prefix is a separator.
316fn has_physical_root(s: &[u8], prefix: Option<Prefix<'_>>) -> bool {
317    let path = if let Some(p) = prefix { &s[p.len()..] } else { s };
318    !path.is_empty() && is_sep_byte(path[0])
319}
320
321// basic workhorse for splitting stem and extension
322fn rsplit_file_at_dot(file: &OsStr) -> (Option<&OsStr>, Option<&OsStr>) {
323    if file.as_encoded_bytes() == b".." {
324        return (Some(file), None);
325    }
326
327    // The unsafety here stems from converting between &OsStr and &[u8]
328    // and back. This is safe to do because (1) we only look at ASCII
329    // contents of the encoding and (2) new &OsStr values are produced
330    // only from ASCII-bounded slices of existing &OsStr values.
331    let mut iter = file.as_encoded_bytes().rsplitn(2, |b| *b == b'.');
332    let after = iter.next();
333    let before = iter.next();
334    if before == Some(b"") {
335        (Some(file), None)
336    } else {
337        unsafe {
338            (
339                before.map(|s| OsStr::from_encoded_bytes_unchecked(s)),
340                after.map(|s| OsStr::from_encoded_bytes_unchecked(s)),
341            )
342        }
343    }
344}
345
346fn split_file_at_dot(file: &OsStr) -> (&OsStr, Option<&OsStr>) {
347    let slice = file.as_encoded_bytes();
348    if slice == b".." {
349        return (file, None);
350    }
351
352    // The unsafety here stems from converting between &OsStr and &[u8]
353    // and back. This is safe to do because (1) we only look at ASCII
354    // contents of the encoding and (2) new &OsStr values are produced
355    // only from ASCII-bounded slices of existing &OsStr values.
356    let i = match slice[1..].iter().position(|b| *b == b'.') {
357        Some(i) => i + 1,
358        None => return (file, None),
359    };
360    let before = &slice[..i];
361    let after = &slice[i + 1..];
362    unsafe {
363        (
364            OsStr::from_encoded_bytes_unchecked(before),
365            Some(OsStr::from_encoded_bytes_unchecked(after)),
366        )
367    }
368}
369
370/// Checks whether the string is valid as a file extension, or panics otherwise.
371fn validate_extension(extension: &OsStr) {
372    for &b in extension.as_encoded_bytes() {
373        if is_sep_byte(b) {
374            panic!("extension cannot contain path separators: {extension:?}");
375        }
376    }
377}
378
379////////////////////////////////////////////////////////////////////////////////
380// The core iterators
381////////////////////////////////////////////////////////////////////////////////
382
383/// Component parsing works by a double-ended state machine; the cursors at the
384/// front and back of the path each keep track of what parts of the path have
385/// been consumed so far.
386///
387/// Going front to back, a path is made up of a prefix, a starting
388/// directory component, and a body (of normal components)
389#[derive(Copy, Clone, PartialEq, PartialOrd, Debug)]
390enum State {
391    Prefix = 0,   // c:
392    StartDir = 1, // / or . or nothing
393    Body = 2,     // foo/bar/baz
394    Done = 3,
395}
396
397/// A structure wrapping a Windows path prefix as well as its unparsed string
398/// representation.
399///
400/// In addition to the parsed [`Prefix`] information returned by [`kind`],
401/// `PrefixComponent` also holds the raw and unparsed [`OsStr`] slice,
402/// returned by [`as_os_str`].
403///
404/// Instances of this `struct` can be obtained by matching against the
405/// [`Prefix` variant] on [`Component`].
406///
407/// Does not occur on Unix.
408///
409/// # Examples
410///
411/// ```
412/// # if cfg!(windows) {
413/// use std::path::{Component, Path, Prefix};
414/// use std::ffi::OsStr;
415///
416/// let path = Path::new(r"c:\you\later\");
417/// match path.components().next().unwrap() {
418///     Component::Prefix(prefix_component) => {
419///         assert_eq!(Prefix::Disk(b'C'), prefix_component.kind());
420///         assert_eq!(OsStr::new("c:"), prefix_component.as_os_str());
421///     }
422///     _ => unreachable!(),
423/// }
424/// # }
425/// ```
426///
427/// [`as_os_str`]: PrefixComponent::as_os_str
428/// [`kind`]: PrefixComponent::kind
429/// [`Prefix` variant]: Component::Prefix
430#[stable(feature = "rust1", since = "1.0.0")]
431#[derive(Copy, Clone, Eq, Debug)]
432pub struct PrefixComponent<'a> {
433    /// The prefix as an unparsed `OsStr` slice.
434    raw: &'a OsStr,
435
436    /// The parsed prefix data.
437    parsed: Prefix<'a>,
438}
439
440impl<'a> PrefixComponent<'a> {
441    /// Returns the parsed prefix data.
442    ///
443    /// See [`Prefix`]'s documentation for more information on the different
444    /// kinds of prefixes.
445    #[stable(feature = "rust1", since = "1.0.0")]
446    #[must_use]
447    #[inline]
448    pub fn kind(&self) -> Prefix<'a> {
449        self.parsed
450    }
451
452    /// Returns the raw [`OsStr`] slice for this prefix.
453    #[stable(feature = "rust1", since = "1.0.0")]
454    #[must_use]
455    #[inline]
456    pub fn as_os_str(&self) -> &'a OsStr {
457        self.raw
458    }
459}
460
461#[stable(feature = "rust1", since = "1.0.0")]
462impl<'a> PartialEq for PrefixComponent<'a> {
463    #[inline]
464    fn eq(&self, other: &PrefixComponent<'a>) -> bool {
465        self.parsed == other.parsed
466    }
467}
468
469#[stable(feature = "rust1", since = "1.0.0")]
470impl<'a> PartialOrd for PrefixComponent<'a> {
471    #[inline]
472    fn partial_cmp(&self, other: &PrefixComponent<'a>) -> Option<cmp::Ordering> {
473        PartialOrd::partial_cmp(&self.parsed, &other.parsed)
474    }
475}
476
477#[stable(feature = "rust1", since = "1.0.0")]
478impl Ord for PrefixComponent<'_> {
479    #[inline]
480    fn cmp(&self, other: &Self) -> cmp::Ordering {
481        Ord::cmp(&self.parsed, &other.parsed)
482    }
483}
484
485#[stable(feature = "rust1", since = "1.0.0")]
486impl Hash for PrefixComponent<'_> {
487    fn hash<H: Hasher>(&self, h: &mut H) {
488        self.parsed.hash(h);
489    }
490}
491
492/// A single component of a path.
493///
494/// A `Component` roughly corresponds to a substring between path separators
495/// (`/` or `\`).
496///
497/// This `enum` is created by iterating over [`Components`], which in turn is
498/// created by the [`components`](Path::components) method on [`Path`].
499///
500/// # Examples
501///
502/// ```rust
503/// use std::path::{Component, Path};
504///
505/// let path = Path::new("/tmp/foo/bar.txt");
506/// let components = path.components().collect::<Vec<_>>();
507/// assert_eq!(&components, &[
508///     Component::RootDir,
509///     Component::Normal("tmp".as_ref()),
510///     Component::Normal("foo".as_ref()),
511///     Component::Normal("bar.txt".as_ref()),
512/// ]);
513/// ```
514#[derive(Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
515#[stable(feature = "rust1", since = "1.0.0")]
516pub enum Component<'a> {
517    /// A Windows path prefix, e.g., `C:` or `\\server\share`.
518    ///
519    /// There is a large variety of prefix types, see [`Prefix`]'s documentation
520    /// for more.
521    ///
522    /// Does not occur on Unix.
523    #[stable(feature = "rust1", since = "1.0.0")]
524    Prefix(#[stable(feature = "rust1", since = "1.0.0")] PrefixComponent<'a>),
525
526    /// The root directory component, appears after any prefix and before anything else.
527    ///
528    /// It represents a separator that designates that a path starts from root.
529    #[stable(feature = "rust1", since = "1.0.0")]
530    RootDir,
531
532    /// A reference to the current directory, i.e., `.`.
533    #[stable(feature = "rust1", since = "1.0.0")]
534    CurDir,
535
536    /// A reference to the parent directory, i.e., `..`.
537    #[stable(feature = "rust1", since = "1.0.0")]
538    ParentDir,
539
540    /// A normal component, e.g., `a` and `b` in `a/b`.
541    ///
542    /// This variant is the most common one, it represents references to files
543    /// or directories.
544    #[stable(feature = "rust1", since = "1.0.0")]
545    Normal(#[stable(feature = "rust1", since = "1.0.0")] &'a OsStr),
546}
547
548impl<'a> Component<'a> {
549    /// Extracts the underlying [`OsStr`] slice.
550    ///
551    /// # Examples
552    ///
553    /// ```
554    /// use std::path::Path;
555    ///
556    /// let path = Path::new("./tmp/foo/bar.txt");
557    /// let components: Vec<_> = path.components().map(|comp| comp.as_os_str()).collect();
558    /// assert_eq!(&components, &[".", "tmp", "foo", "bar.txt"]);
559    /// ```
560    #[must_use = "`self` will be dropped if the result is not used"]
561    #[stable(feature = "rust1", since = "1.0.0")]
562    pub fn as_os_str(self) -> &'a OsStr {
563        match self {
564            Component::Prefix(p) => p.as_os_str(),
565            Component::RootDir => OsStr::new(MAIN_SEP_STR),
566            Component::CurDir => OsStr::new("."),
567            Component::ParentDir => OsStr::new(".."),
568            Component::Normal(path) => path,
569        }
570    }
571}
572
573#[stable(feature = "rust1", since = "1.0.0")]
574impl AsRef<OsStr> for Component<'_> {
575    #[inline]
576    fn as_ref(&self) -> &OsStr {
577        self.as_os_str()
578    }
579}
580
581#[stable(feature = "path_component_asref", since = "1.25.0")]
582impl AsRef<Path> for Component<'_> {
583    #[inline]
584    fn as_ref(&self) -> &Path {
585        self.as_os_str().as_ref()
586    }
587}
588
589/// An iterator over the [`Component`]s of a [`Path`].
590///
591/// This `struct` is created by the [`components`] method on [`Path`].
592/// See its documentation for more.
593///
594/// # Examples
595///
596/// ```
597/// use std::path::Path;
598///
599/// let path = Path::new("/tmp/foo/bar.txt");
600///
601/// for component in path.components() {
602///     println!("{component:?}");
603/// }
604/// ```
605///
606/// [`components`]: Path::components
607#[derive(Clone)]
608#[must_use = "iterators are lazy and do nothing unless consumed"]
609#[stable(feature = "rust1", since = "1.0.0")]
610pub struct Components<'a> {
611    // The path left to parse components from
612    path: &'a [u8],
613
614    // The prefix as it was originally parsed, if any
615    prefix: Option<Prefix<'a>>,
616
617    // true if path *physically* has a root separator; for most Windows
618    // prefixes, it may have a "logical" root separator for the purposes of
619    // normalization, e.g., \\server\share == \\server\share\.
620    has_physical_root: bool,
621
622    // The iterator is double-ended, and these two states keep track of what has
623    // been produced from either end
624    front: State,
625    back: State,
626}
627
628/// An iterator over the [`Component`]s of a [`Path`], as [`OsStr`] slices.
629///
630/// This `struct` is created by the [`iter`] method on [`Path`].
631/// See its documentation for more.
632///
633/// [`iter`]: Path::iter
634#[derive(Clone)]
635#[must_use = "iterators are lazy and do nothing unless consumed"]
636#[stable(feature = "rust1", since = "1.0.0")]
637pub struct Iter<'a> {
638    inner: Components<'a>,
639}
640
641#[stable(feature = "path_components_debug", since = "1.13.0")]
642impl fmt::Debug for Components<'_> {
643    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
644        struct DebugHelper<'a>(&'a Path);
645
646        impl fmt::Debug for DebugHelper<'_> {
647            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
648                f.debug_list().entries(self.0.components()).finish()
649            }
650        }
651
652        f.debug_tuple("Components").field(&DebugHelper(self.as_path())).finish()
653    }
654}
655
656impl<'a> Components<'a> {
657    // how long is the prefix, if any?
658    #[inline]
659    fn prefix_len(&self) -> usize {
660        if !HAS_PREFIXES {
661            return 0;
662        }
663        self.prefix.as_ref().map(Prefix::len).unwrap_or(0)
664    }
665
666    #[inline]
667    fn prefix_verbatim(&self) -> bool {
668        if !HAS_PREFIXES {
669            return false;
670        }
671        self.prefix.as_ref().map(Prefix::is_verbatim).unwrap_or(false)
672    }
673
674    /// how much of the prefix is left from the point of view of iteration?
675    #[inline]
676    fn prefix_remaining(&self) -> usize {
677        if !HAS_PREFIXES {
678            return 0;
679        }
680        if self.front == State::Prefix { self.prefix_len() } else { 0 }
681    }
682
683    // Given the iteration so far, how much of the pre-State::Body path is left?
684    #[inline]
685    fn len_before_body(&self) -> usize {
686        let root = if self.front <= State::StartDir && self.has_physical_root { 1 } else { 0 };
687        let cur_dir = if self.front <= State::StartDir && self.include_cur_dir() { 1 } else { 0 };
688        self.prefix_remaining() + root + cur_dir
689    }
690
691    // is the iteration complete?
692    #[inline]
693    fn finished(&self) -> bool {
694        self.front == State::Done || self.back == State::Done || self.front > self.back
695    }
696
697    #[inline]
698    fn is_sep_byte(&self, b: u8) -> bool {
699        if self.prefix_verbatim() { is_verbatim_sep(b) } else { is_sep_byte(b) }
700    }
701
702    /// Extracts a slice corresponding to the portion of the path remaining for iteration.
703    ///
704    /// # Examples
705    ///
706    /// ```
707    /// use std::path::Path;
708    ///
709    /// let mut components = Path::new("/tmp/foo/bar.txt").components();
710    /// components.next();
711    /// components.next();
712    ///
713    /// assert_eq!(Path::new("foo/bar.txt"), components.as_path());
714    /// ```
715    #[must_use]
716    #[stable(feature = "rust1", since = "1.0.0")]
717    pub fn as_path(&self) -> &'a Path {
718        let mut comps = self.clone();
719        if comps.front == State::Body {
720            comps.trim_left();
721        }
722        if comps.back == State::Body {
723            comps.trim_right();
724        }
725        unsafe { Path::from_u8_slice(comps.path) }
726    }
727
728    /// Is the *original* path rooted?
729    fn has_root(&self) -> bool {
730        if self.has_physical_root {
731            return true;
732        }
733        if HAS_PREFIXES && let Some(p) = self.prefix {
734            if p.has_implicit_root() {
735                return true;
736            }
737        }
738        false
739    }
740
741    /// Should the normalized path include a leading . ?
742    fn include_cur_dir(&self) -> bool {
743        if self.has_root() {
744            return false;
745        }
746        let slice = &self.path[self.prefix_remaining()..];
747        match slice {
748            [b'.'] => true,
749            [b'.', b, ..] => self.is_sep_byte(*b),
750            _ => false,
751        }
752    }
753
754    // parse a given byte sequence following the OsStr encoding into the
755    // corresponding path component
756    unsafe fn parse_single_component<'b>(&self, comp: &'b [u8]) -> Option<Component<'b>> {
757        match comp {
758            b"." if HAS_PREFIXES && self.prefix_verbatim() => Some(Component::CurDir),
759            b"." => None, // . components are normalized away, except at
760            // the beginning of a path, which is treated
761            // separately via `include_cur_dir`
762            b".." => Some(Component::ParentDir),
763            b"" => None,
764            _ => Some(Component::Normal(unsafe { OsStr::from_encoded_bytes_unchecked(comp) })),
765        }
766    }
767
768    // parse a component from the left, saying how many bytes to consume to
769    // remove the component
770    fn parse_next_component(&self) -> (usize, Option<Component<'a>>) {
771        debug_assert!(self.front == State::Body);
772        let (extra, comp) = match self.path.iter().position(|b| self.is_sep_byte(*b)) {
773            None => (0, self.path),
774            Some(i) => (1, &self.path[..i]),
775        };
776        // SAFETY: `comp` is a valid substring, since it is split on a separator.
777        (comp.len() + extra, unsafe { self.parse_single_component(comp) })
778    }
779
780    // parse a component from the right, saying how many bytes to consume to
781    // remove the component
782    fn parse_next_component_back(&self) -> (usize, Option<Component<'a>>) {
783        debug_assert!(self.back == State::Body);
784        let start = self.len_before_body();
785        let (extra, comp) = match self.path[start..].iter().rposition(|b| self.is_sep_byte(*b)) {
786            None => (0, &self.path[start..]),
787            Some(i) => (1, &self.path[start + i + 1..]),
788        };
789        // SAFETY: `comp` is a valid substring, since it is split on a separator.
790        (comp.len() + extra, unsafe { self.parse_single_component(comp) })
791    }
792
793    // trim away repeated separators (i.e., empty components) on the left
794    fn trim_left(&mut self) {
795        while !self.path.is_empty() {
796            let (size, comp) = self.parse_next_component();
797            if comp.is_some() {
798                return;
799            } else {
800                self.path = &self.path[size..];
801            }
802        }
803    }
804
805    // trim away repeated separators (i.e., empty components) on the right
806    fn trim_right(&mut self) {
807        while self.path.len() > self.len_before_body() {
808            let (size, comp) = self.parse_next_component_back();
809            if comp.is_some() {
810                return;
811            } else {
812                self.path = &self.path[..self.path.len() - size];
813            }
814        }
815    }
816}
817
818#[stable(feature = "rust1", since = "1.0.0")]
819impl AsRef<Path> for Components<'_> {
820    #[inline]
821    fn as_ref(&self) -> &Path {
822        self.as_path()
823    }
824}
825
826#[stable(feature = "rust1", since = "1.0.0")]
827impl AsRef<OsStr> for Components<'_> {
828    #[inline]
829    fn as_ref(&self) -> &OsStr {
830        self.as_path().as_os_str()
831    }
832}
833
834#[stable(feature = "path_iter_debug", since = "1.13.0")]
835impl fmt::Debug for Iter<'_> {
836    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
837        struct DebugHelper<'a>(&'a Path);
838
839        impl fmt::Debug for DebugHelper<'_> {
840            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
841                f.debug_list().entries(self.0.iter()).finish()
842            }
843        }
844
845        f.debug_tuple("Iter").field(&DebugHelper(self.as_path())).finish()
846    }
847}
848
849impl<'a> Iter<'a> {
850    /// Extracts a slice corresponding to the portion of the path remaining for iteration.
851    ///
852    /// # Examples
853    ///
854    /// ```
855    /// use std::path::Path;
856    ///
857    /// let mut iter = Path::new("/tmp/foo/bar.txt").iter();
858    /// iter.next();
859    /// iter.next();
860    ///
861    /// assert_eq!(Path::new("foo/bar.txt"), iter.as_path());
862    /// ```
863    #[stable(feature = "rust1", since = "1.0.0")]
864    #[must_use]
865    #[inline]
866    pub fn as_path(&self) -> &'a Path {
867        self.inner.as_path()
868    }
869}
870
871#[stable(feature = "rust1", since = "1.0.0")]
872impl AsRef<Path> for Iter<'_> {
873    #[inline]
874    fn as_ref(&self) -> &Path {
875        self.as_path()
876    }
877}
878
879#[stable(feature = "rust1", since = "1.0.0")]
880impl AsRef<OsStr> for Iter<'_> {
881    #[inline]
882    fn as_ref(&self) -> &OsStr {
883        self.as_path().as_os_str()
884    }
885}
886
887#[stable(feature = "rust1", since = "1.0.0")]
888impl<'a> Iterator for Iter<'a> {
889    type Item = &'a OsStr;
890
891    #[inline]
892    fn next(&mut self) -> Option<&'a OsStr> {
893        self.inner.next().map(Component::as_os_str)
894    }
895}
896
897#[stable(feature = "rust1", since = "1.0.0")]
898impl<'a> DoubleEndedIterator for Iter<'a> {
899    #[inline]
900    fn next_back(&mut self) -> Option<&'a OsStr> {
901        self.inner.next_back().map(Component::as_os_str)
902    }
903}
904
905#[stable(feature = "fused", since = "1.26.0")]
906impl FusedIterator for Iter<'_> {}
907
908#[stable(feature = "rust1", since = "1.0.0")]
909impl<'a> Iterator for Components<'a> {
910    type Item = Component<'a>;
911
912    fn next(&mut self) -> Option<Component<'a>> {
913        while !self.finished() {
914            match self.front {
915                // most likely case first
916                State::Body if !self.path.is_empty() => {
917                    let (size, comp) = self.parse_next_component();
918                    self.path = &self.path[size..];
919                    if comp.is_some() {
920                        return comp;
921                    }
922                }
923                State::Body => {
924                    self.front = State::Done;
925                }
926                State::StartDir => {
927                    self.front = State::Body;
928                    if self.has_physical_root {
929                        debug_assert!(!self.path.is_empty());
930                        self.path = &self.path[1..];
931                        return Some(Component::RootDir);
932                    } else if HAS_PREFIXES && let Some(p) = self.prefix {
933                        if p.has_implicit_root() && !p.is_verbatim() {
934                            return Some(Component::RootDir);
935                        }
936                    } else if self.include_cur_dir() {
937                        debug_assert!(!self.path.is_empty());
938                        self.path = &self.path[1..];
939                        return Some(Component::CurDir);
940                    }
941                }
942                _ if const { !HAS_PREFIXES } => unreachable!(),
943                State::Prefix if self.prefix_len() == 0 => {
944                    self.front = State::StartDir;
945                }
946                State::Prefix => {
947                    self.front = State::StartDir;
948                    debug_assert!(self.prefix_len() <= self.path.len());
949                    let raw = &self.path[..self.prefix_len()];
950                    self.path = &self.path[self.prefix_len()..];
951                    return Some(Component::Prefix(PrefixComponent {
952                        raw: unsafe { OsStr::from_encoded_bytes_unchecked(raw) },
953                        parsed: self.prefix.unwrap(),
954                    }));
955                }
956                State::Done => unreachable!(),
957            }
958        }
959        None
960    }
961}
962
963#[stable(feature = "rust1", since = "1.0.0")]
964impl<'a> DoubleEndedIterator for Components<'a> {
965    fn next_back(&mut self) -> Option<Component<'a>> {
966        while !self.finished() {
967            match self.back {
968                State::Body if self.path.len() > self.len_before_body() => {
969                    let (size, comp) = self.parse_next_component_back();
970                    self.path = &self.path[..self.path.len() - size];
971                    if comp.is_some() {
972                        return comp;
973                    }
974                }
975                State::Body => {
976                    self.back = State::StartDir;
977                }
978                State::StartDir => {
979                    self.back = if HAS_PREFIXES { State::Prefix } else { State::Done };
980                    if self.has_physical_root {
981                        self.path = &self.path[..self.path.len() - 1];
982                        return Some(Component::RootDir);
983                    } else if HAS_PREFIXES && let Some(p) = self.prefix {
984                        if p.has_implicit_root() && !p.is_verbatim() {
985                            return Some(Component::RootDir);
986                        }
987                    } else if self.include_cur_dir() {
988                        self.path = &self.path[..self.path.len() - 1];
989                        return Some(Component::CurDir);
990                    }
991                }
992                _ if !HAS_PREFIXES => unreachable!(),
993                State::Prefix if self.prefix_len() > 0 => {
994                    self.back = State::Done;
995                    return Some(Component::Prefix(PrefixComponent {
996                        raw: unsafe { OsStr::from_encoded_bytes_unchecked(self.path) },
997                        parsed: self.prefix.unwrap(),
998                    }));
999                }
1000                State::Prefix => {
1001                    self.back = State::Done;
1002                    return None;
1003                }
1004                State::Done => unreachable!(),
1005            }
1006        }
1007        None
1008    }
1009}
1010
1011#[stable(feature = "fused", since = "1.26.0")]
1012impl FusedIterator for Components<'_> {}
1013
1014#[stable(feature = "rust1", since = "1.0.0")]
1015impl<'a> PartialEq for Components<'a> {
1016    #[inline]
1017    fn eq(&self, other: &Components<'a>) -> bool {
1018        let Components { path: _, front: _, back: _, has_physical_root: _, prefix: _ } = self;
1019
1020        // Fast path for exact matches, e.g. for hashmap lookups.
1021        // Don't explicitly compare the prefix or has_physical_root fields since they'll
1022        // either be covered by the `path` buffer or are only relevant for `prefix_verbatim()`.
1023        if self.path.len() == other.path.len()
1024            && self.front == other.front
1025            && self.back == State::Body
1026            && other.back == State::Body
1027            && self.prefix_verbatim() == other.prefix_verbatim()
1028        {
1029            // possible future improvement: this could bail out earlier if there were a
1030            // reverse memcmp/bcmp comparing back to front
1031            if self.path == other.path {
1032                return true;
1033            }
1034        }
1035
1036        // compare back to front since absolute paths often share long prefixes
1037        Iterator::eq(self.clone().rev(), other.clone().rev())
1038    }
1039}
1040
1041#[stable(feature = "rust1", since = "1.0.0")]
1042impl Eq for Components<'_> {}
1043
1044#[stable(feature = "rust1", since = "1.0.0")]
1045impl<'a> PartialOrd for Components<'a> {
1046    #[inline]
1047    fn partial_cmp(&self, other: &Components<'a>) -> Option<cmp::Ordering> {
1048        Some(compare_components(self.clone(), other.clone()))
1049    }
1050}
1051
1052#[stable(feature = "rust1", since = "1.0.0")]
1053impl Ord for Components<'_> {
1054    #[inline]
1055    fn cmp(&self, other: &Self) -> cmp::Ordering {
1056        compare_components(self.clone(), other.clone())
1057    }
1058}
1059
1060fn compare_components(mut left: Components<'_>, mut right: Components<'_>) -> cmp::Ordering {
1061    // Fast path for long shared prefixes
1062    //
1063    // - compare raw bytes to find first mismatch
1064    // - backtrack to find separator before mismatch to avoid ambiguous parsings of '.' or '..' characters
1065    // - if found update state to only do a component-wise comparison on the remainder,
1066    //   otherwise do it on the full path
1067    //
1068    // The fast path isn't taken for paths with a PrefixComponent to avoid backtracking into
1069    // the middle of one
1070    if left.prefix.is_none() && right.prefix.is_none() && left.front == right.front {
1071        // possible future improvement: a [u8]::first_mismatch simd implementation
1072        let first_difference = match left.path.iter().zip(right.path).position(|(&a, &b)| a != b) {
1073            None if left.path.len() == right.path.len() => return cmp::Ordering::Equal,
1074            None => left.path.len().min(right.path.len()),
1075            Some(diff) => diff,
1076        };
1077
1078        if let Some(previous_sep) =
1079            left.path[..first_difference].iter().rposition(|&b| left.is_sep_byte(b))
1080        {
1081            let mismatched_component_start = previous_sep + 1;
1082            left.path = &left.path[mismatched_component_start..];
1083            left.front = State::Body;
1084            right.path = &right.path[mismatched_component_start..];
1085            right.front = State::Body;
1086        }
1087    }
1088
1089    Iterator::cmp(left, right)
1090}
1091
1092/// An iterator over [`Path`] and its ancestors.
1093///
1094/// This `struct` is created by the [`ancestors`] method on [`Path`].
1095/// See its documentation for more.
1096///
1097/// # Examples
1098///
1099/// ```
1100/// use std::path::Path;
1101///
1102/// let path = Path::new("/foo/bar");
1103///
1104/// for ancestor in path.ancestors() {
1105///     println!("{}", ancestor.display());
1106/// }
1107/// ```
1108///
1109/// [`ancestors`]: Path::ancestors
1110#[derive(Copy, Clone, Debug)]
1111#[must_use = "iterators are lazy and do nothing unless consumed"]
1112#[stable(feature = "path_ancestors", since = "1.28.0")]
1113pub struct Ancestors<'a> {
1114    next: Option<&'a Path>,
1115}
1116
1117#[stable(feature = "path_ancestors", since = "1.28.0")]
1118impl<'a> Iterator for Ancestors<'a> {
1119    type Item = &'a Path;
1120
1121    #[inline]
1122    fn next(&mut self) -> Option<Self::Item> {
1123        let next = self.next;
1124        self.next = next.and_then(Path::parent);
1125        next
1126    }
1127}
1128
1129#[stable(feature = "path_ancestors", since = "1.28.0")]
1130impl FusedIterator for Ancestors<'_> {}
1131
1132////////////////////////////////////////////////////////////////////////////////
1133// Basic types and traits
1134////////////////////////////////////////////////////////////////////////////////
1135
1136/// An owned, mutable path (akin to [`String`]).
1137///
1138/// This type provides methods like [`push`] and [`set_extension`] that mutate
1139/// the path in place. It also implements [`Deref`] to [`Path`], meaning that
1140/// all methods on [`Path`] slices are available on `PathBuf` values as well.
1141///
1142/// [`push`]: PathBuf::push
1143/// [`set_extension`]: PathBuf::set_extension
1144///
1145/// More details about the overall approach can be found in
1146/// the [module documentation](self).
1147///
1148/// # Examples
1149///
1150/// You can use [`push`] to build up a `PathBuf` from
1151/// components:
1152///
1153/// ```
1154/// use std::path::PathBuf;
1155///
1156/// let mut path = PathBuf::new();
1157///
1158/// path.push(r"C:\");
1159/// path.push("windows");
1160/// path.push("system32");
1161///
1162/// path.set_extension("dll");
1163/// ```
1164///
1165/// However, [`push`] is best used for dynamic situations. This is a better way
1166/// to do this when you know all of the components ahead of time:
1167///
1168/// ```
1169/// use std::path::PathBuf;
1170///
1171/// let path: PathBuf = [r"C:\", "windows", "system32.dll"].iter().collect();
1172/// ```
1173///
1174/// We can still do better than this! Since these are all strings, we can use
1175/// `From::from`:
1176///
1177/// ```
1178/// use std::path::PathBuf;
1179///
1180/// let path = PathBuf::from(r"C:\windows\system32.dll");
1181/// ```
1182///
1183/// Which method works best depends on what kind of situation you're in.
1184///
1185/// Note that `PathBuf` does not always sanitize arguments, for example
1186/// [`push`] allows paths built from strings which include separators:
1187///
1188/// ```
1189/// use std::path::PathBuf;
1190///
1191/// let mut path = PathBuf::new();
1192///
1193/// path.push(r"C:\");
1194/// path.push("windows");
1195/// path.push(r"..\otherdir");
1196/// path.push("system32");
1197/// ```
1198///
1199/// The behavior of `PathBuf` may be changed to a panic on such inputs
1200/// in the future. [`Extend::extend`] should be used to add multi-part paths.
1201#[cfg_attr(not(test), rustc_diagnostic_item = "PathBuf")]
1202#[stable(feature = "rust1", since = "1.0.0")]
1203pub struct PathBuf {
1204    inner: OsString,
1205}
1206
1207impl PathBuf {
1208    /// Allocates an empty `PathBuf`.
1209    ///
1210    /// # Examples
1211    ///
1212    /// ```
1213    /// use std::path::PathBuf;
1214    ///
1215    /// let path = PathBuf::new();
1216    /// ```
1217    #[stable(feature = "rust1", since = "1.0.0")]
1218    #[must_use]
1219    #[inline]
1220    #[rustc_const_stable(feature = "const_pathbuf_osstring_new", since = "1.91.0")]
1221    pub const fn new() -> PathBuf {
1222        PathBuf { inner: OsString::new() }
1223    }
1224
1225    /// Creates a new `PathBuf` with a given capacity used to create the
1226    /// internal [`OsString`]. See [`with_capacity`] defined on [`OsString`].
1227    ///
1228    /// # Examples
1229    ///
1230    /// ```
1231    /// use std::path::PathBuf;
1232    ///
1233    /// let mut path = PathBuf::with_capacity(10);
1234    /// let capacity = path.capacity();
1235    ///
1236    /// // This push is done without reallocating
1237    /// path.push(r"C:\");
1238    ///
1239    /// assert_eq!(capacity, path.capacity());
1240    /// ```
1241    ///
1242    /// [`with_capacity`]: OsString::with_capacity
1243    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1244    #[must_use]
1245    #[inline]
1246    pub fn with_capacity(capacity: usize) -> PathBuf {
1247        PathBuf { inner: OsString::with_capacity(capacity) }
1248    }
1249
1250    /// Coerces to a [`Path`] slice.
1251    ///
1252    /// # Examples
1253    ///
1254    /// ```
1255    /// use std::path::{Path, PathBuf};
1256    ///
1257    /// let p = PathBuf::from("/test");
1258    /// assert_eq!(Path::new("/test"), p.as_path());
1259    /// ```
1260    #[cfg_attr(not(test), rustc_diagnostic_item = "pathbuf_as_path")]
1261    #[stable(feature = "rust1", since = "1.0.0")]
1262    #[must_use]
1263    #[inline]
1264    pub fn as_path(&self) -> &Path {
1265        self
1266    }
1267
1268    /// Consumes and leaks the `PathBuf`, returning a mutable reference to the contents,
1269    /// `&'a mut Path`.
1270    ///
1271    /// The caller has free choice over the returned lifetime, including 'static.
1272    /// Indeed, this function is ideally used for data that lives for the remainder of
1273    /// the program's life, as dropping the returned reference will cause a memory leak.
1274    ///
1275    /// It does not reallocate or shrink the `PathBuf`, so the leaked allocation may include
1276    /// unused capacity that is not part of the returned slice. If you want to discard excess
1277    /// capacity, call [`into_boxed_path`], and then [`Box::leak`] instead.
1278    /// However, keep in mind that trimming the capacity may result in a reallocation and copy.
1279    ///
1280    /// [`into_boxed_path`]: Self::into_boxed_path
1281    #[stable(feature = "os_string_pathbuf_leak", since = "1.89.0")]
1282    #[inline]
1283    pub fn leak<'a>(self) -> &'a mut Path {
1284        Path::from_inner_mut(self.inner.leak())
1285    }
1286
1287    /// Extends `self` with `path`.
1288    ///
1289    /// If `path` is absolute, it replaces the current path.
1290    ///
1291    /// On Windows:
1292    ///
1293    /// * if `path` has a root but no prefix (e.g., `\windows`), it
1294    ///   replaces everything except for the prefix (if any) of `self`.
1295    /// * if `path` has a prefix but no root, it replaces `self`.
1296    /// * if `self` has a verbatim prefix (e.g. `\\?\C:\windows`)
1297    ///   and `path` is not empty, the new path is normalized: all references
1298    ///   to `.` and `..` are removed.
1299    ///
1300    /// Consider using [`Path::join`] if you need a new `PathBuf` instead of
1301    /// using this function on a cloned `PathBuf`.
1302    ///
1303    /// # Examples
1304    ///
1305    /// Pushing a relative path extends the existing path:
1306    ///
1307    /// ```
1308    /// use std::path::PathBuf;
1309    ///
1310    /// let mut path = PathBuf::from("/tmp");
1311    /// path.push("file.bk");
1312    /// assert_eq!(path, PathBuf::from("/tmp/file.bk"));
1313    /// ```
1314    ///
1315    /// Pushing an absolute path replaces the existing path:
1316    ///
1317    /// ```
1318    /// use std::path::PathBuf;
1319    ///
1320    /// let mut path = PathBuf::from("/tmp");
1321    /// path.push("/etc");
1322    /// assert_eq!(path, PathBuf::from("/etc"));
1323    /// ```
1324    #[stable(feature = "rust1", since = "1.0.0")]
1325    #[rustc_confusables("append", "put")]
1326    pub fn push<P: AsRef<Path>>(&mut self, path: P) {
1327        self._push(path.as_ref())
1328    }
1329
1330    fn _push(&mut self, path: &Path) {
1331        // in general, a separator is needed if the rightmost byte is not a separator
1332        let buf = self.inner.as_encoded_bytes();
1333        let mut need_sep = buf.last().map(|c| !is_sep_byte(*c)).unwrap_or(false);
1334
1335        // in the special case of `C:` on Windows, do *not* add a separator
1336        let comps = self.components();
1337
1338        if comps.prefix_len() > 0
1339            && comps.prefix_len() == comps.path.len()
1340            && comps.prefix.unwrap().is_drive()
1341        {
1342            need_sep = false
1343        }
1344
1345        let need_clear = if cfg!(target_os = "cygwin") {
1346            // If path is absolute and its prefix is none, it is like `/foo`,
1347            // and will be handled below.
1348            path.prefix().is_some()
1349        } else {
1350            // On Unix: prefix is always None.
1351            path.is_absolute() || path.prefix().is_some()
1352        };
1353
1354        // absolute `path` replaces `self`
1355        if need_clear {
1356            self.inner.truncate(0);
1357
1358        // verbatim paths need . and .. removed
1359        } else if comps.prefix_verbatim() && !path.inner.is_empty() {
1360            let mut buf: Vec<_> = comps.collect();
1361            for c in path.components() {
1362                match c {
1363                    Component::RootDir => {
1364                        buf.truncate(1);
1365                        buf.push(c);
1366                    }
1367                    Component::CurDir => (),
1368                    Component::ParentDir => {
1369                        if let Some(Component::Normal(_)) = buf.last() {
1370                            buf.pop();
1371                        }
1372                    }
1373                    _ => buf.push(c),
1374                }
1375            }
1376
1377            let mut res = OsString::new();
1378            let mut need_sep = false;
1379
1380            for c in buf {
1381                if need_sep && c != Component::RootDir {
1382                    res.push(MAIN_SEP_STR);
1383                }
1384                res.push(c.as_os_str());
1385
1386                need_sep = match c {
1387                    Component::RootDir => false,
1388                    Component::Prefix(prefix) => {
1389                        !prefix.parsed.is_drive() && prefix.parsed.len() > 0
1390                    }
1391                    _ => true,
1392                }
1393            }
1394
1395            self.inner = res;
1396            return;
1397
1398        // `path` has a root but no prefix, e.g., `\windows` (Windows only)
1399        } else if path.has_root() {
1400            let prefix_len = self.components().prefix_remaining();
1401            self.inner.truncate(prefix_len);
1402
1403        // `path` is a pure relative path
1404        } else if need_sep {
1405            self.inner.push(MAIN_SEP_STR);
1406        }
1407
1408        self.inner.push(path);
1409    }
1410
1411    /// Truncates `self` to [`self.parent`].
1412    ///
1413    /// Returns `false` and does nothing if [`self.parent`] is [`None`].
1414    /// Otherwise, returns `true`.
1415    ///
1416    /// [`self.parent`]: Path::parent
1417    ///
1418    /// # Examples
1419    ///
1420    /// ```
1421    /// use std::path::{Path, PathBuf};
1422    ///
1423    /// let mut p = PathBuf::from("/spirited/away.rs");
1424    ///
1425    /// p.pop();
1426    /// assert_eq!(Path::new("/spirited"), p);
1427    /// p.pop();
1428    /// assert_eq!(Path::new("/"), p);
1429    /// ```
1430    #[stable(feature = "rust1", since = "1.0.0")]
1431    pub fn pop(&mut self) -> bool {
1432        match self.parent().map(|p| p.as_u8_slice().len()) {
1433            Some(len) => {
1434                self.inner.truncate(len);
1435                true
1436            }
1437            None => false,
1438        }
1439    }
1440
1441    /// Sets whether the path has a trailing [separator](MAIN_SEPARATOR).
1442    ///
1443    /// The value returned by [`has_trailing_sep`](Path::has_trailing_sep) will be equivalent to
1444    /// the provided value if possible.
1445    ///
1446    /// # Examples
1447    ///
1448    /// ```
1449    /// #![feature(path_trailing_sep)]
1450    /// use std::path::PathBuf;
1451    ///
1452    /// let mut p = PathBuf::from("dir");
1453    ///
1454    /// assert!(!p.has_trailing_sep());
1455    /// p.set_trailing_sep(false);
1456    /// assert!(!p.has_trailing_sep());
1457    /// p.set_trailing_sep(true);
1458    /// assert!(p.has_trailing_sep());
1459    /// p.set_trailing_sep(false);
1460    /// assert!(!p.has_trailing_sep());
1461    ///
1462    /// p = PathBuf::from("/");
1463    /// assert!(p.has_trailing_sep());
1464    /// p.set_trailing_sep(false);
1465    /// assert!(p.has_trailing_sep());
1466    /// ```
1467    #[unstable(feature = "path_trailing_sep", issue = "142503")]
1468    pub fn set_trailing_sep(&mut self, trailing_sep: bool) {
1469        if trailing_sep { self.push_trailing_sep() } else { self.pop_trailing_sep() }
1470    }
1471
1472    /// Adds a trailing [separator](MAIN_SEPARATOR) to the path.
1473    ///
1474    /// This acts similarly to [`Path::with_trailing_sep`], but mutates the underlying `PathBuf`.
1475    ///
1476    /// # Examples
1477    ///
1478    /// ```
1479    /// #![feature(path_trailing_sep)]
1480    /// use std::ffi::OsStr;
1481    /// use std::path::PathBuf;
1482    ///
1483    /// let mut p = PathBuf::from("dir");
1484    ///
1485    /// assert!(!p.has_trailing_sep());
1486    /// p.push_trailing_sep();
1487    /// assert!(p.has_trailing_sep());
1488    /// p.push_trailing_sep();
1489    /// assert!(p.has_trailing_sep());
1490    ///
1491    /// p = PathBuf::from("dir/");
1492    /// p.push_trailing_sep();
1493    /// assert_eq!(p.as_os_str(), OsStr::new("dir/"));
1494    /// ```
1495    #[unstable(feature = "path_trailing_sep", issue = "142503")]
1496    pub fn push_trailing_sep(&mut self) {
1497        if !self.has_trailing_sep() {
1498            self.push("");
1499        }
1500    }
1501
1502    /// Removes a trailing [separator](MAIN_SEPARATOR) from the path, if possible.
1503    ///
1504    /// This acts similarly to [`Path::trim_trailing_sep`], but mutates the underlying `PathBuf`.
1505    ///
1506    /// # Examples
1507    ///
1508    /// ```
1509    /// #![feature(path_trailing_sep)]
1510    /// use std::ffi::OsStr;
1511    /// use std::path::PathBuf;
1512    ///
1513    /// let mut p = PathBuf::from("dir//");
1514    ///
1515    /// assert!(p.has_trailing_sep());
1516    /// assert_eq!(p.as_os_str(), OsStr::new("dir//"));
1517    /// p.pop_trailing_sep();
1518    /// assert!(!p.has_trailing_sep());
1519    /// assert_eq!(p.as_os_str(), OsStr::new("dir"));
1520    /// p.pop_trailing_sep();
1521    /// assert!(!p.has_trailing_sep());
1522    /// assert_eq!(p.as_os_str(), OsStr::new("dir"));
1523    ///
1524    /// p = PathBuf::from("/");
1525    /// assert!(p.has_trailing_sep());
1526    /// p.pop_trailing_sep();
1527    /// assert!(p.has_trailing_sep());
1528    /// ```
1529    #[unstable(feature = "path_trailing_sep", issue = "142503")]
1530    pub fn pop_trailing_sep(&mut self) {
1531        self.inner.truncate(self.trim_trailing_sep().as_os_str().len());
1532    }
1533
1534    /// Updates [`self.file_name`] to `file_name`.
1535    ///
1536    /// If [`self.file_name`] was [`None`], this is equivalent to pushing
1537    /// `file_name`.
1538    ///
1539    /// Otherwise it is equivalent to calling [`pop`] and then pushing
1540    /// `file_name`. The new path will be a sibling of the original path.
1541    /// (That is, it will have the same parent.)
1542    ///
1543    /// The argument is not sanitized, so can include separators. This
1544    /// behavior may be changed to a panic in the future.
1545    ///
1546    /// [`self.file_name`]: Path::file_name
1547    /// [`pop`]: PathBuf::pop
1548    ///
1549    /// # Examples
1550    ///
1551    /// ```
1552    /// use std::path::PathBuf;
1553    ///
1554    /// let mut buf = PathBuf::from("/");
1555    /// assert!(buf.file_name() == None);
1556    ///
1557    /// buf.set_file_name("foo.txt");
1558    /// assert!(buf == PathBuf::from("/foo.txt"));
1559    /// assert!(buf.file_name().is_some());
1560    ///
1561    /// buf.set_file_name("bar.txt");
1562    /// assert!(buf == PathBuf::from("/bar.txt"));
1563    ///
1564    /// buf.set_file_name("baz");
1565    /// assert!(buf == PathBuf::from("/baz"));
1566    ///
1567    /// buf.set_file_name("../b/c.txt");
1568    /// assert!(buf == PathBuf::from("/../b/c.txt"));
1569    ///
1570    /// buf.set_file_name("baz");
1571    /// assert!(buf == PathBuf::from("/../b/baz"));
1572    /// ```
1573    #[stable(feature = "rust1", since = "1.0.0")]
1574    pub fn set_file_name<S: AsRef<OsStr>>(&mut self, file_name: S) {
1575        self._set_file_name(file_name.as_ref())
1576    }
1577
1578    fn _set_file_name(&mut self, file_name: &OsStr) {
1579        if self.file_name().is_some() {
1580            let popped = self.pop();
1581            debug_assert!(popped);
1582        }
1583        self.push(file_name);
1584    }
1585
1586    /// Updates [`self.extension`] to `Some(extension)` or to `None` if
1587    /// `extension` is empty.
1588    ///
1589    /// Returns `false` and does nothing if [`self.file_name`] is [`None`],
1590    /// returns `true` and updates the extension otherwise.
1591    ///
1592    /// If [`self.extension`] is [`None`], the extension is added; otherwise
1593    /// it is replaced.
1594    ///
1595    /// If `extension` is the empty string, [`self.extension`] will be [`None`]
1596    /// afterwards, not `Some("")`.
1597    ///
1598    /// # Panics
1599    ///
1600    /// Panics if the passed extension contains a path separator (see
1601    /// [`is_separator`]).
1602    ///
1603    /// # Caveats
1604    ///
1605    /// The new `extension` may contain dots and will be used in its entirety,
1606    /// but only the part after the final dot will be reflected in
1607    /// [`self.extension`].
1608    ///
1609    /// If the file stem contains internal dots and `extension` is empty, part
1610    /// of the old file stem will be considered the new [`self.extension`].
1611    ///
1612    /// See the examples below.
1613    ///
1614    /// [`self.file_name`]: Path::file_name
1615    /// [`self.extension`]: Path::extension
1616    ///
1617    /// # Examples
1618    ///
1619    /// ```
1620    /// use std::path::{Path, PathBuf};
1621    ///
1622    /// let mut p = PathBuf::from("/feel/the");
1623    ///
1624    /// p.set_extension("force");
1625    /// assert_eq!(Path::new("/feel/the.force"), p.as_path());
1626    ///
1627    /// p.set_extension("dark.side");
1628    /// assert_eq!(Path::new("/feel/the.dark.side"), p.as_path());
1629    ///
1630    /// p.set_extension("cookie");
1631    /// assert_eq!(Path::new("/feel/the.dark.cookie"), p.as_path());
1632    ///
1633    /// p.set_extension("");
1634    /// assert_eq!(Path::new("/feel/the.dark"), p.as_path());
1635    ///
1636    /// p.set_extension("");
1637    /// assert_eq!(Path::new("/feel/the"), p.as_path());
1638    ///
1639    /// p.set_extension("");
1640    /// assert_eq!(Path::new("/feel/the"), p.as_path());
1641    /// ```
1642    #[stable(feature = "rust1", since = "1.0.0")]
1643    pub fn set_extension<S: AsRef<OsStr>>(&mut self, extension: S) -> bool {
1644        self._set_extension(extension.as_ref())
1645    }
1646
1647    fn _set_extension(&mut self, extension: &OsStr) -> bool {
1648        validate_extension(extension);
1649
1650        let file_stem = match self.file_stem() {
1651            None => return false,
1652            Some(f) => f.as_encoded_bytes(),
1653        };
1654
1655        // truncate until right after the file stem
1656        let end_file_stem = file_stem[file_stem.len()..].as_ptr().addr();
1657        let start = self.inner.as_encoded_bytes().as_ptr().addr();
1658        self.inner.truncate(end_file_stem.wrapping_sub(start));
1659
1660        // add the new extension, if any
1661        let new = extension.as_encoded_bytes();
1662        if !new.is_empty() {
1663            self.inner.reserve_exact(new.len() + 1);
1664            self.inner.push(".");
1665            // SAFETY: Since a UTF-8 string was just pushed, it is not possible
1666            // for the buffer to end with a surrogate half.
1667            unsafe { self.inner.extend_from_slice_unchecked(new) };
1668        }
1669
1670        true
1671    }
1672
1673    /// Append [`self.extension`] with `extension`.
1674    ///
1675    /// Returns `false` and does nothing if [`self.file_name`] is [`None`],
1676    /// returns `true` and updates the extension otherwise.
1677    ///
1678    /// # Panics
1679    ///
1680    /// Panics if the passed extension contains a path separator (see
1681    /// [`is_separator`]).
1682    ///
1683    /// # Caveats
1684    ///
1685    /// The appended `extension` may contain dots and will be used in its entirety,
1686    /// but only the part after the final dot will be reflected in
1687    /// [`self.extension`].
1688    ///
1689    /// See the examples below.
1690    ///
1691    /// [`self.file_name`]: Path::file_name
1692    /// [`self.extension`]: Path::extension
1693    ///
1694    /// # Examples
1695    ///
1696    /// ```
1697    /// use std::path::{Path, PathBuf};
1698    ///
1699    /// let mut p = PathBuf::from("/feel/the");
1700    ///
1701    /// p.add_extension("formatted");
1702    /// assert_eq!(Path::new("/feel/the.formatted"), p.as_path());
1703    ///
1704    /// p.add_extension("dark.side");
1705    /// assert_eq!(Path::new("/feel/the.formatted.dark.side"), p.as_path());
1706    ///
1707    /// p.set_extension("cookie");
1708    /// assert_eq!(Path::new("/feel/the.formatted.dark.cookie"), p.as_path());
1709    ///
1710    /// p.set_extension("");
1711    /// assert_eq!(Path::new("/feel/the.formatted.dark"), p.as_path());
1712    ///
1713    /// p.add_extension("");
1714    /// assert_eq!(Path::new("/feel/the.formatted.dark"), p.as_path());
1715    /// ```
1716    #[stable(feature = "path_add_extension", since = "1.91.0")]
1717    pub fn add_extension<S: AsRef<OsStr>>(&mut self, extension: S) -> bool {
1718        self._add_extension(extension.as_ref())
1719    }
1720
1721    fn _add_extension(&mut self, extension: &OsStr) -> bool {
1722        validate_extension(extension);
1723
1724        let file_name = match self.file_name() {
1725            None => return false,
1726            Some(f) => f.as_encoded_bytes(),
1727        };
1728
1729        let new = extension.as_encoded_bytes();
1730        if !new.is_empty() {
1731            // truncate until right after the file name
1732            // this is necessary for trimming the trailing separator
1733            let end_file_name = file_name[file_name.len()..].as_ptr().addr();
1734            let start = self.inner.as_encoded_bytes().as_ptr().addr();
1735            self.inner.truncate(end_file_name.wrapping_sub(start));
1736
1737            // append the new extension
1738            self.inner.reserve_exact(new.len() + 1);
1739            self.inner.push(".");
1740            // SAFETY: Since a UTF-8 string was just pushed, it is not possible
1741            // for the buffer to end with a surrogate half.
1742            unsafe { self.inner.extend_from_slice_unchecked(new) };
1743        }
1744
1745        true
1746    }
1747
1748    /// Yields a mutable reference to the underlying [`OsString`] instance.
1749    ///
1750    /// # Examples
1751    ///
1752    /// ```
1753    /// use std::path::{Path, PathBuf};
1754    ///
1755    /// let mut path = PathBuf::from("/foo");
1756    ///
1757    /// path.push("bar");
1758    /// assert_eq!(path, Path::new("/foo/bar"));
1759    ///
1760    /// // OsString's `push` does not add a separator.
1761    /// path.as_mut_os_string().push("baz");
1762    /// assert_eq!(path, Path::new("/foo/barbaz"));
1763    /// ```
1764    #[stable(feature = "path_as_mut_os_str", since = "1.70.0")]
1765    #[must_use]
1766    #[inline]
1767    pub fn as_mut_os_string(&mut self) -> &mut OsString {
1768        &mut self.inner
1769    }
1770
1771    /// Consumes the `PathBuf`, yielding its internal [`OsString`] storage.
1772    ///
1773    /// # Examples
1774    ///
1775    /// ```
1776    /// use std::path::PathBuf;
1777    ///
1778    /// let p = PathBuf::from("/the/head");
1779    /// let os_str = p.into_os_string();
1780    /// ```
1781    #[stable(feature = "rust1", since = "1.0.0")]
1782    #[must_use = "`self` will be dropped if the result is not used"]
1783    #[inline]
1784    pub fn into_os_string(self) -> OsString {
1785        self.inner
1786    }
1787
1788    /// Converts this `PathBuf` into a [boxed](Box) [`Path`].
1789    #[stable(feature = "into_boxed_path", since = "1.20.0")]
1790    #[must_use = "`self` will be dropped if the result is not used"]
1791    #[inline]
1792    pub fn into_boxed_path(self) -> Box<Path> {
1793        let rw = Box::into_raw(self.inner.into_boxed_os_str()) as *mut Path;
1794        unsafe { Box::from_raw(rw) }
1795    }
1796
1797    /// Invokes [`capacity`] on the underlying instance of [`OsString`].
1798    ///
1799    /// [`capacity`]: OsString::capacity
1800    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1801    #[must_use]
1802    #[inline]
1803    pub fn capacity(&self) -> usize {
1804        self.inner.capacity()
1805    }
1806
1807    /// Invokes [`clear`] on the underlying instance of [`OsString`].
1808    ///
1809    /// [`clear`]: OsString::clear
1810    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1811    #[inline]
1812    pub fn clear(&mut self) {
1813        self.inner.clear()
1814    }
1815
1816    /// Invokes [`reserve`] on the underlying instance of [`OsString`].
1817    ///
1818    /// [`reserve`]: OsString::reserve
1819    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1820    #[inline]
1821    pub fn reserve(&mut self, additional: usize) {
1822        self.inner.reserve(additional)
1823    }
1824
1825    /// Invokes [`try_reserve`] on the underlying instance of [`OsString`].
1826    ///
1827    /// [`try_reserve`]: OsString::try_reserve
1828    #[stable(feature = "try_reserve_2", since = "1.63.0")]
1829    #[inline]
1830    pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError> {
1831        self.inner.try_reserve(additional)
1832    }
1833
1834    /// Invokes [`reserve_exact`] on the underlying instance of [`OsString`].
1835    ///
1836    /// [`reserve_exact`]: OsString::reserve_exact
1837    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1838    #[inline]
1839    pub fn reserve_exact(&mut self, additional: usize) {
1840        self.inner.reserve_exact(additional)
1841    }
1842
1843    /// Invokes [`try_reserve_exact`] on the underlying instance of [`OsString`].
1844    ///
1845    /// [`try_reserve_exact`]: OsString::try_reserve_exact
1846    #[stable(feature = "try_reserve_2", since = "1.63.0")]
1847    #[inline]
1848    pub fn try_reserve_exact(&mut self, additional: usize) -> Result<(), TryReserveError> {
1849        self.inner.try_reserve_exact(additional)
1850    }
1851
1852    /// Invokes [`shrink_to_fit`] on the underlying instance of [`OsString`].
1853    ///
1854    /// [`shrink_to_fit`]: OsString::shrink_to_fit
1855    #[stable(feature = "path_buf_capacity", since = "1.44.0")]
1856    #[inline]
1857    pub fn shrink_to_fit(&mut self) {
1858        self.inner.shrink_to_fit()
1859    }
1860
1861    /// Invokes [`shrink_to`] on the underlying instance of [`OsString`].
1862    ///
1863    /// [`shrink_to`]: OsString::shrink_to
1864    #[stable(feature = "shrink_to", since = "1.56.0")]
1865    #[inline]
1866    pub fn shrink_to(&mut self, min_capacity: usize) {
1867        self.inner.shrink_to(min_capacity)
1868    }
1869}
1870
1871#[stable(feature = "rust1", since = "1.0.0")]
1872impl Clone for PathBuf {
1873    #[inline]
1874    fn clone(&self) -> Self {
1875        PathBuf { inner: self.inner.clone() }
1876    }
1877
1878    /// Clones the contents of `source` into `self`.
1879    ///
1880    /// This method is preferred over simply assigning `source.clone()` to `self`,
1881    /// as it avoids reallocation if possible.
1882    #[inline]
1883    fn clone_from(&mut self, source: &Self) {
1884        self.inner.clone_from(&source.inner)
1885    }
1886}
1887
1888#[stable(feature = "box_from_path", since = "1.17.0")]
1889impl From<&Path> for Box<Path> {
1890    /// Creates a boxed [`Path`] from a reference.
1891    ///
1892    /// This will allocate and clone `path` to it.
1893    fn from(path: &Path) -> Box<Path> {
1894        Box::clone_from_ref(path)
1895    }
1896}
1897
1898#[stable(feature = "box_from_mut_slice", since = "1.84.0")]
1899impl From<&mut Path> for Box<Path> {
1900    /// Creates a boxed [`Path`] from a reference.
1901    ///
1902    /// This will allocate and clone `path` to it.
1903    fn from(path: &mut Path) -> Box<Path> {
1904        Self::from(&*path)
1905    }
1906}
1907
1908#[stable(feature = "box_from_cow", since = "1.45.0")]
1909impl From<Cow<'_, Path>> for Box<Path> {
1910    /// Creates a boxed [`Path`] from a clone-on-write pointer.
1911    ///
1912    /// Converting from a `Cow::Owned` does not clone or allocate.
1913    #[inline]
1914    fn from(cow: Cow<'_, Path>) -> Box<Path> {
1915        match cow {
1916            Cow::Borrowed(path) => Box::from(path),
1917            Cow::Owned(path) => Box::from(path),
1918        }
1919    }
1920}
1921
1922#[stable(feature = "path_buf_from_box", since = "1.18.0")]
1923impl From<Box<Path>> for PathBuf {
1924    /// Converts a <code>[Box]&lt;[Path]&gt;</code> into a [`PathBuf`].
1925    ///
1926    /// This conversion does not allocate or copy memory.
1927    #[inline]
1928    fn from(boxed: Box<Path>) -> PathBuf {
1929        boxed.into_path_buf()
1930    }
1931}
1932
1933#[stable(feature = "box_from_path_buf", since = "1.20.0")]
1934impl From<PathBuf> for Box<Path> {
1935    /// Converts a [`PathBuf`] into a <code>[Box]&lt;[Path]&gt;</code>.
1936    ///
1937    /// This conversion currently should not allocate memory,
1938    /// but this behavior is not guaranteed on all platforms or in all future versions.
1939    #[inline]
1940    fn from(p: PathBuf) -> Box<Path> {
1941        p.into_boxed_path()
1942    }
1943}
1944
1945#[stable(feature = "more_box_slice_clone", since = "1.29.0")]
1946impl Clone for Box<Path> {
1947    #[inline]
1948    fn clone(&self) -> Self {
1949        self.to_path_buf().into_boxed_path()
1950    }
1951}
1952
1953#[stable(feature = "rust1", since = "1.0.0")]
1954impl<T: ?Sized + AsRef<OsStr>> From<&T> for PathBuf {
1955    /// Converts a borrowed [`OsStr`] to a [`PathBuf`].
1956    ///
1957    /// Allocates a [`PathBuf`] and copies the data into it.
1958    #[inline]
1959    fn from(s: &T) -> PathBuf {
1960        PathBuf::from(s.as_ref().to_os_string())
1961    }
1962}
1963
1964#[stable(feature = "rust1", since = "1.0.0")]
1965impl From<OsString> for PathBuf {
1966    /// Converts an [`OsString`] into a [`PathBuf`].
1967    ///
1968    /// This conversion does not allocate or copy memory.
1969    #[inline]
1970    fn from(s: OsString) -> PathBuf {
1971        PathBuf { inner: s }
1972    }
1973}
1974
1975#[stable(feature = "from_path_buf_for_os_string", since = "1.14.0")]
1976impl From<PathBuf> for OsString {
1977    /// Converts a [`PathBuf`] into an [`OsString`]
1978    ///
1979    /// This conversion does not allocate or copy memory.
1980    #[inline]
1981    fn from(path_buf: PathBuf) -> OsString {
1982        path_buf.inner
1983    }
1984}
1985
1986#[stable(feature = "rust1", since = "1.0.0")]
1987impl From<String> for PathBuf {
1988    /// Converts a [`String`] into a [`PathBuf`]
1989    ///
1990    /// This conversion does not allocate or copy memory.
1991    #[inline]
1992    fn from(s: String) -> PathBuf {
1993        PathBuf::from(OsString::from(s))
1994    }
1995}
1996
1997#[stable(feature = "path_from_str", since = "1.32.0")]
1998impl FromStr for PathBuf {
1999    type Err = core::convert::Infallible;
2000
2001    #[inline]
2002    fn from_str(s: &str) -> Result<Self, Self::Err> {
2003        Ok(PathBuf::from(s))
2004    }
2005}
2006
2007#[stable(feature = "rust1", since = "1.0.0")]
2008impl<P: AsRef<Path>> FromIterator<P> for PathBuf {
2009    /// Creates a new `PathBuf` from the [`Path`] elements of an iterator.
2010    ///
2011    /// This uses [`push`](Self::push) to add each element, so can be used to adjoin multiple path
2012    /// [components](Components).
2013    ///
2014    /// # Examples
2015    /// ```
2016    /// # use std::path::PathBuf;
2017    /// let path = PathBuf::from_iter(["/tmp", "foo", "bar"]);
2018    /// assert_eq!(path, PathBuf::from("/tmp/foo/bar"));
2019    /// ```
2020    ///
2021    /// See documentation for [`push`](Self::push) for more details on how the path is constructed.
2022    fn from_iter<I: IntoIterator<Item = P>>(iter: I) -> PathBuf {
2023        let mut buf = PathBuf::new();
2024        buf.extend(iter);
2025        buf
2026    }
2027}
2028
2029#[stable(feature = "rust1", since = "1.0.0")]
2030impl<P: AsRef<Path>> Extend<P> for PathBuf {
2031    /// Extends `self` with [`Path`] elements from `iter`.
2032    ///
2033    /// This uses [`push`](Self::push) to add each element, so can be used to adjoin multiple path
2034    /// [components](Components).
2035    ///
2036    /// # Examples
2037    /// ```
2038    /// # use std::path::PathBuf;
2039    /// let mut path = PathBuf::from("/tmp");
2040    /// path.extend(["foo", "bar", "file.txt"]);
2041    /// assert_eq!(path, PathBuf::from("/tmp/foo/bar/file.txt"));
2042    /// ```
2043    ///
2044    /// See documentation for [`push`](Self::push) for more details on how the path is constructed.
2045    fn extend<I: IntoIterator<Item = P>>(&mut self, iter: I) {
2046        iter.into_iter().for_each(move |p| self.push(p.as_ref()));
2047    }
2048
2049    #[inline]
2050    fn extend_one(&mut self, p: P) {
2051        self.push(p.as_ref());
2052    }
2053}
2054
2055#[stable(feature = "rust1", since = "1.0.0")]
2056impl fmt::Debug for PathBuf {
2057    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2058        fmt::Debug::fmt(&**self, formatter)
2059    }
2060}
2061
2062#[stable(feature = "rust1", since = "1.0.0")]
2063impl ops::Deref for PathBuf {
2064    type Target = Path;
2065    #[inline]
2066    fn deref(&self) -> &Path {
2067        Path::new(&self.inner)
2068    }
2069}
2070
2071#[stable(feature = "path_buf_deref_mut", since = "1.68.0")]
2072impl ops::DerefMut for PathBuf {
2073    #[inline]
2074    fn deref_mut(&mut self) -> &mut Path {
2075        Path::from_inner_mut(&mut self.inner)
2076    }
2077}
2078
2079#[stable(feature = "rust1", since = "1.0.0")]
2080impl Borrow<Path> for PathBuf {
2081    #[inline]
2082    fn borrow(&self) -> &Path {
2083        self.deref()
2084    }
2085}
2086
2087#[stable(feature = "default_for_pathbuf", since = "1.17.0")]
2088impl Default for PathBuf {
2089    #[inline]
2090    fn default() -> Self {
2091        PathBuf::new()
2092    }
2093}
2094
2095#[stable(feature = "cow_from_path", since = "1.6.0")]
2096impl<'a> From<&'a Path> for Cow<'a, Path> {
2097    /// Creates a clone-on-write pointer from a reference to
2098    /// [`Path`].
2099    ///
2100    /// This conversion does not clone or allocate.
2101    #[inline]
2102    fn from(s: &'a Path) -> Cow<'a, Path> {
2103        Cow::Borrowed(s)
2104    }
2105}
2106
2107#[stable(feature = "cow_from_path", since = "1.6.0")]
2108impl<'a> From<PathBuf> for Cow<'a, Path> {
2109    /// Creates a clone-on-write pointer from an owned
2110    /// instance of [`PathBuf`].
2111    ///
2112    /// This conversion does not clone or allocate.
2113    #[inline]
2114    fn from(s: PathBuf) -> Cow<'a, Path> {
2115        Cow::Owned(s)
2116    }
2117}
2118
2119#[stable(feature = "cow_from_pathbuf_ref", since = "1.28.0")]
2120impl<'a> From<&'a PathBuf> for Cow<'a, Path> {
2121    /// Creates a clone-on-write pointer from a reference to
2122    /// [`PathBuf`].
2123    ///
2124    /// This conversion does not clone or allocate.
2125    #[inline]
2126    fn from(p: &'a PathBuf) -> Cow<'a, Path> {
2127        Cow::Borrowed(p.as_path())
2128    }
2129}
2130
2131#[stable(feature = "pathbuf_from_cow_path", since = "1.28.0")]
2132impl<'a> From<Cow<'a, Path>> for PathBuf {
2133    /// Converts a clone-on-write pointer to an owned path.
2134    ///
2135    /// Converting from a `Cow::Owned` does not clone or allocate.
2136    #[inline]
2137    fn from(p: Cow<'a, Path>) -> Self {
2138        p.into_owned()
2139    }
2140}
2141
2142#[stable(feature = "shared_from_slice2", since = "1.24.0")]
2143impl From<PathBuf> for Arc<Path> {
2144    /// Converts a [`PathBuf`] into an <code>[Arc]<[Path]></code> by moving the [`PathBuf`] data
2145    /// into a new [`Arc`] buffer.
2146    #[inline]
2147    fn from(s: PathBuf) -> Arc<Path> {
2148        let arc: Arc<OsStr> = Arc::from(s.into_os_string());
2149        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const Path) }
2150    }
2151}
2152
2153#[stable(feature = "shared_from_slice2", since = "1.24.0")]
2154impl From<&Path> for Arc<Path> {
2155    /// Converts a [`Path`] into an [`Arc`] by copying the [`Path`] data into a new [`Arc`] buffer.
2156    #[inline]
2157    fn from(s: &Path) -> Arc<Path> {
2158        let arc: Arc<OsStr> = Arc::from(s.as_os_str());
2159        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const Path) }
2160    }
2161}
2162
2163#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
2164impl From<&mut Path> for Arc<Path> {
2165    /// Converts a [`Path`] into an [`Arc`] by copying the [`Path`] data into a new [`Arc`] buffer.
2166    #[inline]
2167    fn from(s: &mut Path) -> Arc<Path> {
2168        Arc::from(&*s)
2169    }
2170}
2171
2172#[stable(feature = "shared_from_slice2", since = "1.24.0")]
2173impl From<PathBuf> for Rc<Path> {
2174    /// Converts a [`PathBuf`] into an <code>[Rc]<[Path]></code> by moving the [`PathBuf`] data into
2175    /// a new [`Rc`] buffer.
2176    #[inline]
2177    fn from(s: PathBuf) -> Rc<Path> {
2178        let rc: Rc<OsStr> = Rc::from(s.into_os_string());
2179        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const Path) }
2180    }
2181}
2182
2183#[stable(feature = "shared_from_slice2", since = "1.24.0")]
2184impl From<&Path> for Rc<Path> {
2185    /// Converts a [`Path`] into an [`Rc`] by copying the [`Path`] data into a new [`Rc`] buffer.
2186    #[inline]
2187    fn from(s: &Path) -> Rc<Path> {
2188        let rc: Rc<OsStr> = Rc::from(s.as_os_str());
2189        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const Path) }
2190    }
2191}
2192
2193#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
2194impl From<&mut Path> for Rc<Path> {
2195    /// Converts a [`Path`] into an [`Rc`] by copying the [`Path`] data into a new [`Rc`] buffer.
2196    #[inline]
2197    fn from(s: &mut Path) -> Rc<Path> {
2198        Rc::from(&*s)
2199    }
2200}
2201
2202#[stable(feature = "rust1", since = "1.0.0")]
2203impl ToOwned for Path {
2204    type Owned = PathBuf;
2205    #[inline]
2206    fn to_owned(&self) -> PathBuf {
2207        self.to_path_buf()
2208    }
2209    #[inline]
2210    fn clone_into(&self, target: &mut PathBuf) {
2211        self.inner.clone_into(&mut target.inner);
2212    }
2213}
2214
2215#[stable(feature = "rust1", since = "1.0.0")]
2216impl PartialEq for PathBuf {
2217    #[inline]
2218    fn eq(&self, other: &PathBuf) -> bool {
2219        self.components() == other.components()
2220    }
2221}
2222
2223#[stable(feature = "eq_str_for_path", since = "1.91.0")]
2224impl cmp::PartialEq<str> for PathBuf {
2225    #[inline]
2226    fn eq(&self, other: &str) -> bool {
2227        self.as_path() == other
2228    }
2229}
2230
2231#[stable(feature = "eq_str_for_path", since = "1.91.0")]
2232impl cmp::PartialEq<PathBuf> for str {
2233    #[inline]
2234    fn eq(&self, other: &PathBuf) -> bool {
2235        self == other.as_path()
2236    }
2237}
2238
2239#[stable(feature = "eq_str_for_path", since = "1.91.0")]
2240impl cmp::PartialEq<String> for PathBuf {
2241    #[inline]
2242    fn eq(&self, other: &String) -> bool {
2243        self.as_path() == other.as_str()
2244    }
2245}
2246
2247#[stable(feature = "eq_str_for_path", since = "1.91.0")]
2248impl cmp::PartialEq<PathBuf> for String {
2249    #[inline]
2250    fn eq(&self, other: &PathBuf) -> bool {
2251        self.as_str() == other.as_path()
2252    }
2253}
2254
2255#[stable(feature = "rust1", since = "1.0.0")]
2256impl Hash for PathBuf {
2257    fn hash<H: Hasher>(&self, h: &mut H) {
2258        self.as_path().hash(h)
2259    }
2260}
2261
2262#[stable(feature = "rust1", since = "1.0.0")]
2263impl Eq for PathBuf {}
2264
2265#[stable(feature = "rust1", since = "1.0.0")]
2266impl PartialOrd for PathBuf {
2267    #[inline]
2268    fn partial_cmp(&self, other: &PathBuf) -> Option<cmp::Ordering> {
2269        Some(compare_components(self.components(), other.components()))
2270    }
2271}
2272
2273#[stable(feature = "rust1", since = "1.0.0")]
2274impl Ord for PathBuf {
2275    #[inline]
2276    fn cmp(&self, other: &PathBuf) -> cmp::Ordering {
2277        compare_components(self.components(), other.components())
2278    }
2279}
2280
2281#[stable(feature = "rust1", since = "1.0.0")]
2282impl AsRef<OsStr> for PathBuf {
2283    #[inline]
2284    fn as_ref(&self) -> &OsStr {
2285        &self.inner[..]
2286    }
2287}
2288
2289/// A slice of a path (akin to [`str`]).
2290///
2291/// This type supports a number of operations for inspecting a path, including
2292/// breaking the path into its components (separated by `/` on Unix and by either
2293/// `/` or `\` on Windows), extracting the file name, determining whether the path
2294/// is absolute, and so on.
2295///
2296/// This is an *unsized* type, meaning that it must always be used behind a
2297/// pointer like `&` or [`Box`]. For an owned version of this type,
2298/// see [`PathBuf`].
2299///
2300/// More details about the overall approach can be found in
2301/// the [module documentation](self).
2302///
2303/// # Examples
2304///
2305/// ```
2306/// use std::path::Path;
2307/// use std::ffi::OsStr;
2308///
2309/// // Note: this example does work on Windows
2310/// let path = Path::new("./foo/bar.txt");
2311///
2312/// let parent = path.parent();
2313/// assert_eq!(parent, Some(Path::new("./foo")));
2314///
2315/// let file_stem = path.file_stem();
2316/// assert_eq!(file_stem, Some(OsStr::new("bar")));
2317///
2318/// let extension = path.extension();
2319/// assert_eq!(extension, Some(OsStr::new("txt")));
2320/// ```
2321#[cfg_attr(not(test), rustc_diagnostic_item = "Path")]
2322#[stable(feature = "rust1", since = "1.0.0")]
2323// `Path::new` and `impl CloneToUninit for Path` current implementation relies
2324// on `Path` being layout-compatible with `OsStr`.
2325// However, `Path` layout is considered an implementation detail and must not be relied upon.
2326#[repr(transparent)]
2327pub struct Path {
2328    inner: OsStr,
2329}
2330
2331/// An error returned from [`Path::strip_prefix`] if the prefix was not found.
2332///
2333/// This `struct` is created by the [`strip_prefix`] method on [`Path`].
2334/// See its documentation for more.
2335///
2336/// [`strip_prefix`]: Path::strip_prefix
2337#[derive(Debug, Clone, PartialEq, Eq)]
2338#[stable(since = "1.7.0", feature = "strip_prefix")]
2339pub struct StripPrefixError(());
2340
2341/// An error returned from [`Path::normalize_lexically`] if a `..` parent reference
2342/// would escape the path.
2343#[unstable(feature = "normalize_lexically", issue = "134694")]
2344#[derive(Debug, PartialEq)]
2345#[non_exhaustive]
2346pub struct NormalizeError;
2347
2348impl Path {
2349    // The following (private!) function allows construction of a path from a u8
2350    // slice, which is only safe when it is known to follow the OsStr encoding.
2351    unsafe fn from_u8_slice(s: &[u8]) -> &Path {
2352        unsafe { Path::new(OsStr::from_encoded_bytes_unchecked(s)) }
2353    }
2354    // The following (private!) function reveals the byte encoding used for OsStr.
2355    pub(crate) fn as_u8_slice(&self) -> &[u8] {
2356        self.inner.as_encoded_bytes()
2357    }
2358
2359    /// Directly wraps a string slice as a `Path` slice.
2360    ///
2361    /// This is a cost-free conversion.
2362    ///
2363    /// # Examples
2364    ///
2365    /// ```
2366    /// use std::path::Path;
2367    ///
2368    /// Path::new("foo.txt");
2369    /// ```
2370    ///
2371    /// You can create `Path`s from `String`s, or even other `Path`s:
2372    ///
2373    /// ```
2374    /// use std::path::Path;
2375    ///
2376    /// let string = String::from("foo.txt");
2377    /// let from_string = Path::new(&string);
2378    /// let from_path = Path::new(&from_string);
2379    /// assert_eq!(from_string, from_path);
2380    /// ```
2381    #[stable(feature = "rust1", since = "1.0.0")]
2382    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2383    pub const fn new<S: [const] AsRef<OsStr> + ?Sized>(s: &S) -> &Path {
2384        unsafe { &*(s.as_ref() as *const OsStr as *const Path) }
2385    }
2386
2387    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2388    const fn from_inner_mut(inner: &mut OsStr) -> &mut Path {
2389        // SAFETY: Path is just a wrapper around OsStr,
2390        // therefore converting &mut OsStr to &mut Path is safe.
2391        unsafe { &mut *(inner as *mut OsStr as *mut Path) }
2392    }
2393
2394    /// Yields the underlying [`OsStr`] slice.
2395    ///
2396    /// # Examples
2397    ///
2398    /// ```
2399    /// use std::path::Path;
2400    ///
2401    /// let os_str = Path::new("foo.txt").as_os_str();
2402    /// assert_eq!(os_str, std::ffi::OsStr::new("foo.txt"));
2403    /// ```
2404    #[stable(feature = "rust1", since = "1.0.0")]
2405    #[must_use]
2406    #[inline]
2407    pub fn as_os_str(&self) -> &OsStr {
2408        &self.inner
2409    }
2410
2411    /// Yields a mutable reference to the underlying [`OsStr`] slice.
2412    ///
2413    /// # Examples
2414    ///
2415    /// ```
2416    /// use std::path::{Path, PathBuf};
2417    ///
2418    /// let mut path = PathBuf::from("Foo.TXT");
2419    ///
2420    /// assert_ne!(path, Path::new("foo.txt"));
2421    ///
2422    /// path.as_mut_os_str().make_ascii_lowercase();
2423    /// assert_eq!(path, Path::new("foo.txt"));
2424    /// ```
2425    #[stable(feature = "path_as_mut_os_str", since = "1.70.0")]
2426    #[must_use]
2427    #[inline]
2428    pub fn as_mut_os_str(&mut self) -> &mut OsStr {
2429        &mut self.inner
2430    }
2431
2432    /// Yields a [`&str`] slice if the `Path` is valid unicode.
2433    ///
2434    /// This conversion may entail doing a check for UTF-8 validity.
2435    /// Note that validation is performed because non-UTF-8 strings are
2436    /// perfectly valid for some OS.
2437    ///
2438    /// [`&str`]: str
2439    ///
2440    /// # Examples
2441    ///
2442    /// ```
2443    /// use std::path::Path;
2444    ///
2445    /// let path = Path::new("foo.txt");
2446    /// assert_eq!(path.to_str(), Some("foo.txt"));
2447    /// ```
2448    #[stable(feature = "rust1", since = "1.0.0")]
2449    #[must_use = "this returns the result of the operation, \
2450                  without modifying the original"]
2451    #[inline]
2452    pub fn to_str(&self) -> Option<&str> {
2453        self.inner.to_str()
2454    }
2455
2456    /// Converts a `Path` to a [`Cow<str>`].
2457    ///
2458    /// Any non-UTF-8 sequences are replaced with
2459    /// [`U+FFFD REPLACEMENT CHARACTER`][U+FFFD].
2460    ///
2461    /// [U+FFFD]: super::char::REPLACEMENT_CHARACTER
2462    ///
2463    /// # Examples
2464    ///
2465    /// Calling `to_string_lossy` on a `Path` with valid unicode:
2466    ///
2467    /// ```
2468    /// use std::path::Path;
2469    ///
2470    /// let path = Path::new("foo.txt");
2471    /// assert_eq!(path.to_string_lossy(), "foo.txt");
2472    /// ```
2473    ///
2474    /// Had `path` contained invalid unicode, the `to_string_lossy` call might
2475    /// have returned `"fo�.txt"`.
2476    #[stable(feature = "rust1", since = "1.0.0")]
2477    #[must_use = "this returns the result of the operation, \
2478                  without modifying the original"]
2479    #[inline]
2480    pub fn to_string_lossy(&self) -> Cow<'_, str> {
2481        self.inner.to_string_lossy()
2482    }
2483
2484    /// Converts a `Path` to an owned [`PathBuf`].
2485    ///
2486    /// # Examples
2487    ///
2488    /// ```
2489    /// use std::path::{Path, PathBuf};
2490    ///
2491    /// let path_buf = Path::new("foo.txt").to_path_buf();
2492    /// assert_eq!(path_buf, PathBuf::from("foo.txt"));
2493    /// ```
2494    #[rustc_conversion_suggestion]
2495    #[must_use = "this returns the result of the operation, \
2496                  without modifying the original"]
2497    #[stable(feature = "rust1", since = "1.0.0")]
2498    #[cfg_attr(not(test), rustc_diagnostic_item = "path_to_pathbuf")]
2499    pub fn to_path_buf(&self) -> PathBuf {
2500        PathBuf::from(self.inner.to_os_string())
2501    }
2502
2503    /// Returns `true` if the `Path` is absolute, i.e., if it is independent of
2504    /// the current directory.
2505    ///
2506    /// * On Unix, a path is absolute if it starts with the root, so
2507    /// `is_absolute` and [`has_root`] are equivalent.
2508    ///
2509    /// * On Windows, a path is absolute if it has a prefix and starts with the
2510    /// root: `c:\windows` is absolute, while `c:temp` and `\temp` are not.
2511    ///
2512    /// # Examples
2513    ///
2514    /// ```
2515    /// use std::path::Path;
2516    ///
2517    /// assert!(!Path::new("foo.txt").is_absolute());
2518    /// ```
2519    ///
2520    /// [`has_root`]: Path::has_root
2521    #[stable(feature = "rust1", since = "1.0.0")]
2522    #[must_use]
2523    #[allow(deprecated)]
2524    pub fn is_absolute(&self) -> bool {
2525        sys::path::is_absolute(self)
2526    }
2527
2528    /// Returns `true` if the `Path` is relative, i.e., not absolute.
2529    ///
2530    /// See [`is_absolute`]'s documentation for more details.
2531    ///
2532    /// # Examples
2533    ///
2534    /// ```
2535    /// use std::path::Path;
2536    ///
2537    /// assert!(Path::new("foo.txt").is_relative());
2538    /// ```
2539    ///
2540    /// [`is_absolute`]: Path::is_absolute
2541    #[stable(feature = "rust1", since = "1.0.0")]
2542    #[must_use]
2543    #[inline]
2544    pub fn is_relative(&self) -> bool {
2545        !self.is_absolute()
2546    }
2547
2548    pub(crate) fn prefix(&self) -> Option<Prefix<'_>> {
2549        self.components().prefix
2550    }
2551
2552    /// Returns `true` if the `Path` has a root.
2553    ///
2554    /// * On Unix, a path has a root if it begins with `/`.
2555    ///
2556    /// * On Windows, a path has a root if it:
2557    ///     * has no prefix and begins with a separator, e.g., `\windows`
2558    ///     * has a prefix followed by a separator, e.g., `c:\windows` but not `c:windows`
2559    ///     * has any non-disk prefix, e.g., `\\server\share`
2560    ///
2561    /// # Examples
2562    ///
2563    /// ```
2564    /// use std::path::Path;
2565    ///
2566    /// assert!(Path::new("/etc/passwd").has_root());
2567    /// ```
2568    #[stable(feature = "rust1", since = "1.0.0")]
2569    #[must_use]
2570    #[inline]
2571    pub fn has_root(&self) -> bool {
2572        self.components().has_root()
2573    }
2574
2575    /// Returns the `Path` without its final component, if there is one.
2576    ///
2577    /// This means it returns `Some("")` for relative paths with one component.
2578    ///
2579    /// Returns [`None`] if the path terminates in a root or prefix, or if it's
2580    /// the empty string.
2581    ///
2582    /// # Examples
2583    ///
2584    /// ```
2585    /// use std::path::Path;
2586    ///
2587    /// let path = Path::new("/foo/bar");
2588    /// let parent = path.parent().unwrap();
2589    /// assert_eq!(parent, Path::new("/foo"));
2590    ///
2591    /// let grand_parent = parent.parent().unwrap();
2592    /// assert_eq!(grand_parent, Path::new("/"));
2593    /// assert_eq!(grand_parent.parent(), None);
2594    ///
2595    /// let relative_path = Path::new("foo/bar");
2596    /// let parent = relative_path.parent();
2597    /// assert_eq!(parent, Some(Path::new("foo")));
2598    /// let grand_parent = parent.and_then(Path::parent);
2599    /// assert_eq!(grand_parent, Some(Path::new("")));
2600    /// let great_grand_parent = grand_parent.and_then(Path::parent);
2601    /// assert_eq!(great_grand_parent, None);
2602    /// ```
2603    #[stable(feature = "rust1", since = "1.0.0")]
2604    #[doc(alias = "dirname")]
2605    #[must_use]
2606    pub fn parent(&self) -> Option<&Path> {
2607        let mut comps = self.components();
2608        let comp = comps.next_back();
2609        comp.and_then(|p| match p {
2610            Component::Normal(_) | Component::CurDir | Component::ParentDir => {
2611                Some(comps.as_path())
2612            }
2613            _ => None,
2614        })
2615    }
2616
2617    /// Produces an iterator over `Path` and its ancestors.
2618    ///
2619    /// The iterator will yield the `Path` that is returned if the [`parent`] method is used zero
2620    /// or more times. If the [`parent`] method returns [`None`], the iterator will do likewise.
2621    /// The iterator will always yield at least one value, namely `Some(&self)`. Next it will yield
2622    /// `&self.parent()`, `&self.parent().and_then(Path::parent)` and so on.
2623    ///
2624    /// # Examples
2625    ///
2626    /// ```
2627    /// use std::path::Path;
2628    ///
2629    /// let mut ancestors = Path::new("/foo/bar").ancestors();
2630    /// assert_eq!(ancestors.next(), Some(Path::new("/foo/bar")));
2631    /// assert_eq!(ancestors.next(), Some(Path::new("/foo")));
2632    /// assert_eq!(ancestors.next(), Some(Path::new("/")));
2633    /// assert_eq!(ancestors.next(), None);
2634    ///
2635    /// let mut ancestors = Path::new("../foo/bar").ancestors();
2636    /// assert_eq!(ancestors.next(), Some(Path::new("../foo/bar")));
2637    /// assert_eq!(ancestors.next(), Some(Path::new("../foo")));
2638    /// assert_eq!(ancestors.next(), Some(Path::new("..")));
2639    /// assert_eq!(ancestors.next(), Some(Path::new("")));
2640    /// assert_eq!(ancestors.next(), None);
2641    /// ```
2642    ///
2643    /// [`parent`]: Path::parent
2644    #[stable(feature = "path_ancestors", since = "1.28.0")]
2645    #[inline]
2646    pub fn ancestors(&self) -> Ancestors<'_> {
2647        Ancestors { next: Some(&self) }
2648    }
2649
2650    /// Returns the final component of the `Path`, if there is one.
2651    ///
2652    /// If the path is a normal file, this is the file name. If it's the path of a directory, this
2653    /// is the directory name.
2654    ///
2655    /// Returns [`None`] if the path terminates in `..`.
2656    ///
2657    /// # Examples
2658    ///
2659    /// ```
2660    /// use std::path::Path;
2661    /// use std::ffi::OsStr;
2662    ///
2663    /// assert_eq!(Some(OsStr::new("bin")), Path::new("/usr/bin/").file_name());
2664    /// assert_eq!(Some(OsStr::new("foo.txt")), Path::new("tmp/foo.txt").file_name());
2665    /// assert_eq!(Some(OsStr::new("foo.txt")), Path::new("foo.txt/.").file_name());
2666    /// assert_eq!(Some(OsStr::new("foo.txt")), Path::new("foo.txt/.//").file_name());
2667    /// assert_eq!(None, Path::new("foo.txt/..").file_name());
2668    /// assert_eq!(None, Path::new("/").file_name());
2669    /// ```
2670    #[stable(feature = "rust1", since = "1.0.0")]
2671    #[doc(alias = "basename")]
2672    #[must_use]
2673    pub fn file_name(&self) -> Option<&OsStr> {
2674        self.components().next_back().and_then(|p| match p {
2675            Component::Normal(p) => Some(p),
2676            _ => None,
2677        })
2678    }
2679
2680    /// Returns a path that, when joined onto `base`, yields `self`.
2681    ///
2682    /// # Errors
2683    ///
2684    /// If `base` is not a prefix of `self` (i.e., [`starts_with`]
2685    /// returns `false`), returns [`Err`].
2686    ///
2687    /// [`starts_with`]: Path::starts_with
2688    ///
2689    /// # Examples
2690    ///
2691    /// ```
2692    /// use std::path::{Path, PathBuf};
2693    ///
2694    /// let path = Path::new("/test/haha/foo.txt");
2695    ///
2696    /// assert_eq!(path.strip_prefix("/"), Ok(Path::new("test/haha/foo.txt")));
2697    /// assert_eq!(path.strip_prefix("/test"), Ok(Path::new("haha/foo.txt")));
2698    /// assert_eq!(path.strip_prefix("/test/"), Ok(Path::new("haha/foo.txt")));
2699    /// assert_eq!(path.strip_prefix("/test/haha/foo.txt"), Ok(Path::new("")));
2700    /// assert_eq!(path.strip_prefix("/test/haha/foo.txt/"), Ok(Path::new("")));
2701    ///
2702    /// assert!(path.strip_prefix("test").is_err());
2703    /// assert!(path.strip_prefix("/te").is_err());
2704    /// assert!(path.strip_prefix("/haha").is_err());
2705    ///
2706    /// let prefix = PathBuf::from("/test/");
2707    /// assert_eq!(path.strip_prefix(prefix), Ok(Path::new("haha/foo.txt")));
2708    /// ```
2709    #[stable(since = "1.7.0", feature = "path_strip_prefix")]
2710    pub fn strip_prefix<P>(&self, base: P) -> Result<&Path, StripPrefixError>
2711    where
2712        P: AsRef<Path>,
2713    {
2714        self._strip_prefix(base.as_ref())
2715    }
2716
2717    fn _strip_prefix(&self, base: &Path) -> Result<&Path, StripPrefixError> {
2718        iter_after(self.components(), base.components())
2719            .map(|c| c.as_path())
2720            .ok_or(StripPrefixError(()))
2721    }
2722
2723    /// Determines whether `base` is a prefix of `self`.
2724    ///
2725    /// Only considers whole path components to match.
2726    ///
2727    /// # Examples
2728    ///
2729    /// ```
2730    /// use std::path::Path;
2731    ///
2732    /// let path = Path::new("/etc/passwd");
2733    ///
2734    /// assert!(path.starts_with("/etc"));
2735    /// assert!(path.starts_with("/etc/"));
2736    /// assert!(path.starts_with("/etc/passwd"));
2737    /// assert!(path.starts_with("/etc/passwd/")); // extra slash is okay
2738    /// assert!(path.starts_with("/etc/passwd///")); // multiple extra slashes are okay
2739    ///
2740    /// assert!(!path.starts_with("/e"));
2741    /// assert!(!path.starts_with("/etc/passwd.txt"));
2742    ///
2743    /// assert!(!Path::new("/etc/foo.rs").starts_with("/etc/foo"));
2744    /// ```
2745    #[stable(feature = "rust1", since = "1.0.0")]
2746    #[must_use]
2747    pub fn starts_with<P: AsRef<Path>>(&self, base: P) -> bool {
2748        self._starts_with(base.as_ref())
2749    }
2750
2751    fn _starts_with(&self, base: &Path) -> bool {
2752        iter_after(self.components(), base.components()).is_some()
2753    }
2754
2755    /// Determines whether `child` is a suffix of `self`.
2756    ///
2757    /// Only considers whole path components to match.
2758    ///
2759    /// # Examples
2760    ///
2761    /// ```
2762    /// use std::path::Path;
2763    ///
2764    /// let path = Path::new("/etc/resolv.conf");
2765    ///
2766    /// assert!(path.ends_with("resolv.conf"));
2767    /// assert!(path.ends_with("etc/resolv.conf"));
2768    /// assert!(path.ends_with("/etc/resolv.conf"));
2769    ///
2770    /// assert!(!path.ends_with("/resolv.conf"));
2771    /// assert!(!path.ends_with("conf")); // use .extension() instead
2772    /// ```
2773    #[stable(feature = "rust1", since = "1.0.0")]
2774    #[must_use]
2775    pub fn ends_with<P: AsRef<Path>>(&self, child: P) -> bool {
2776        self._ends_with(child.as_ref())
2777    }
2778
2779    fn _ends_with(&self, child: &Path) -> bool {
2780        iter_after(self.components().rev(), child.components().rev()).is_some()
2781    }
2782
2783    /// Checks whether the `Path` is empty.
2784    ///
2785    /// # Examples
2786    ///
2787    /// ```
2788    /// #![feature(path_is_empty)]
2789    /// use std::path::Path;
2790    ///
2791    /// let path = Path::new("");
2792    /// assert!(path.is_empty());
2793    ///
2794    /// let path = Path::new("foo");
2795    /// assert!(!path.is_empty());
2796    ///
2797    /// let path = Path::new(".");
2798    /// assert!(!path.is_empty());
2799    /// ```
2800    #[unstable(feature = "path_is_empty", issue = "148494")]
2801    pub fn is_empty(&self) -> bool {
2802        self.as_os_str().is_empty()
2803    }
2804
2805    /// Extracts the stem (non-extension) portion of [`self.file_name`].
2806    ///
2807    /// [`self.file_name`]: Path::file_name
2808    ///
2809    /// The stem is:
2810    ///
2811    /// * [`None`], if there is no file name;
2812    /// * The entire file name if there is no embedded `.`;
2813    /// * The entire file name if the file name begins with `.` and has no other `.`s within;
2814    /// * Otherwise, the portion of the file name before the final `.`
2815    ///
2816    /// # Examples
2817    ///
2818    /// ```
2819    /// use std::path::Path;
2820    ///
2821    /// assert_eq!("foo", Path::new("foo.rs").file_stem().unwrap());
2822    /// assert_eq!("foo.tar", Path::new("foo.tar.gz").file_stem().unwrap());
2823    /// ```
2824    ///
2825    /// # See Also
2826    /// This method is similar to [`Path::file_prefix`], which extracts the portion of the file name
2827    /// before the *first* `.`
2828    ///
2829    /// [`Path::file_prefix`]: Path::file_prefix
2830    ///
2831    #[stable(feature = "rust1", since = "1.0.0")]
2832    #[must_use]
2833    pub fn file_stem(&self) -> Option<&OsStr> {
2834        self.file_name().map(rsplit_file_at_dot).and_then(|(before, after)| before.or(after))
2835    }
2836
2837    /// Extracts the prefix of [`self.file_name`].
2838    ///
2839    /// The prefix is:
2840    ///
2841    /// * [`None`], if there is no file name;
2842    /// * The entire file name if there is no embedded `.`;
2843    /// * The portion of the file name before the first non-beginning `.`;
2844    /// * The entire file name if the file name begins with `.` and has no other `.`s within;
2845    /// * The portion of the file name before the second `.` if the file name begins with `.`
2846    ///
2847    /// [`self.file_name`]: Path::file_name
2848    ///
2849    /// # Examples
2850    ///
2851    /// ```
2852    /// use std::path::Path;
2853    ///
2854    /// assert_eq!("foo", Path::new("foo.rs").file_prefix().unwrap());
2855    /// assert_eq!("foo", Path::new("foo.tar.gz").file_prefix().unwrap());
2856    /// assert_eq!(".config", Path::new(".config").file_prefix().unwrap());
2857    /// assert_eq!(".config", Path::new(".config.toml").file_prefix().unwrap());
2858    /// ```
2859    ///
2860    /// # See Also
2861    /// This method is similar to [`Path::file_stem`], which extracts the portion of the file name
2862    /// before the *last* `.`
2863    ///
2864    /// [`Path::file_stem`]: Path::file_stem
2865    ///
2866    #[stable(feature = "path_file_prefix", since = "1.91.0")]
2867    #[must_use]
2868    pub fn file_prefix(&self) -> Option<&OsStr> {
2869        self.file_name().map(split_file_at_dot).and_then(|(before, _after)| Some(before))
2870    }
2871
2872    /// Extracts the extension (without the leading dot) of [`self.file_name`], if possible.
2873    ///
2874    /// The extension is:
2875    ///
2876    /// * [`None`], if there is no file name;
2877    /// * [`None`], if there is no embedded `.`;
2878    /// * [`None`], if the file name begins with `.` and has no other `.`s within;
2879    /// * Otherwise, the portion of the file name after the final `.`
2880    ///
2881    /// [`self.file_name`]: Path::file_name
2882    ///
2883    /// # Examples
2884    ///
2885    /// ```
2886    /// use std::path::Path;
2887    ///
2888    /// assert_eq!("rs", Path::new("foo.rs").extension().unwrap());
2889    /// assert_eq!("gz", Path::new("foo.tar.gz").extension().unwrap());
2890    /// ```
2891    #[stable(feature = "rust1", since = "1.0.0")]
2892    #[must_use]
2893    pub fn extension(&self) -> Option<&OsStr> {
2894        self.file_name().map(rsplit_file_at_dot).and_then(|(before, after)| before.and(after))
2895    }
2896
2897    /// Checks whether the path ends in a trailing [separator](MAIN_SEPARATOR).
2898    ///
2899    /// This is generally done to ensure that a path is treated as a directory, not a file,
2900    /// although it does not actually guarantee that such a path is a directory on the underlying
2901    /// file system.
2902    ///
2903    /// Despite this behavior, two paths are still considered the same in Rust whether they have a
2904    /// trailing separator or not.
2905    ///
2906    /// # Examples
2907    ///
2908    /// ```
2909    /// #![feature(path_trailing_sep)]
2910    /// use std::path::Path;
2911    ///
2912    /// assert!(Path::new("dir/").has_trailing_sep());
2913    /// assert!(!Path::new("file.rs").has_trailing_sep());
2914    /// ```
2915    #[unstable(feature = "path_trailing_sep", issue = "142503")]
2916    #[must_use]
2917    #[inline]
2918    pub fn has_trailing_sep(&self) -> bool {
2919        self.as_os_str().as_encoded_bytes().last().copied().is_some_and(is_sep_byte)
2920    }
2921
2922    /// Ensures that a path has a trailing [separator](MAIN_SEPARATOR),
2923    /// allocating a [`PathBuf`] if necessary.
2924    ///
2925    /// The resulting path will return true for [`has_trailing_sep`](Self::has_trailing_sep).
2926    ///
2927    /// # Examples
2928    ///
2929    /// ```
2930    /// #![feature(path_trailing_sep)]
2931    /// use std::ffi::OsStr;
2932    /// use std::path::Path;
2933    ///
2934    /// assert_eq!(Path::new("dir//").with_trailing_sep().as_os_str(), OsStr::new("dir//"));
2935    /// assert_eq!(Path::new("dir/").with_trailing_sep().as_os_str(), OsStr::new("dir/"));
2936    /// assert!(!Path::new("dir").has_trailing_sep());
2937    /// assert!(Path::new("dir").with_trailing_sep().has_trailing_sep());
2938    /// ```
2939    #[unstable(feature = "path_trailing_sep", issue = "142503")]
2940    #[must_use]
2941    #[inline]
2942    pub fn with_trailing_sep(&self) -> Cow<'_, Path> {
2943        if self.has_trailing_sep() { Cow::Borrowed(self) } else { Cow::Owned(self.join("")) }
2944    }
2945
2946    /// Trims a trailing [separator](MAIN_SEPARATOR) from a path, if possible.
2947    ///
2948    /// The resulting path will return false for [`has_trailing_sep`](Self::has_trailing_sep) for
2949    /// most paths.
2950    ///
2951    /// Some paths, like `/`, cannot be trimmed in this way.
2952    ///
2953    /// # Examples
2954    ///
2955    /// ```
2956    /// #![feature(path_trailing_sep)]
2957    /// use std::ffi::OsStr;
2958    /// use std::path::Path;
2959    ///
2960    /// assert_eq!(Path::new("dir//").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
2961    /// assert_eq!(Path::new("dir/").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
2962    /// assert_eq!(Path::new("dir").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
2963    /// assert_eq!(Path::new("/").trim_trailing_sep().as_os_str(), OsStr::new("/"));
2964    /// assert_eq!(Path::new("//").trim_trailing_sep().as_os_str(), OsStr::new("//"));
2965    /// ```
2966    #[unstable(feature = "path_trailing_sep", issue = "142503")]
2967    #[must_use]
2968    #[inline]
2969    pub fn trim_trailing_sep(&self) -> &Path {
2970        if self.has_trailing_sep() && (!self.has_root() || self.parent().is_some()) {
2971            let mut bytes = self.inner.as_encoded_bytes();
2972            while let Some((last, init)) = bytes.split_last()
2973                && is_sep_byte(*last)
2974            {
2975                bytes = init;
2976            }
2977
2978            // SAFETY: Trimming trailing ASCII bytes will retain the validity of the string.
2979            Path::new(unsafe { OsStr::from_encoded_bytes_unchecked(bytes) })
2980        } else {
2981            self
2982        }
2983    }
2984
2985    /// Creates an owned [`PathBuf`] with `path` adjoined to `self`.
2986    ///
2987    /// If `path` is absolute, it replaces the current path.
2988    ///
2989    /// On Windows:
2990    ///
2991    /// * if `path` has a root but no prefix (e.g., `\windows`), it
2992    ///   replaces and returns everything except for the prefix (if any) of `self`.
2993    /// * if `path` has a prefix but no root, `self` is ignored and `path` is returned.
2994    /// * if `self` has a verbatim prefix (e.g. `\\?\C:\windows`)
2995    ///   and `path` is not empty, the new path is normalized: all references
2996    ///   to `.` and `..` are removed.
2997    ///
2998    /// See [`PathBuf::push`] for more details on what it means to adjoin a path.
2999    ///
3000    /// # Examples
3001    ///
3002    /// ```
3003    /// use std::path::{Path, PathBuf};
3004    ///
3005    /// assert_eq!(Path::new("/etc").join("passwd"), PathBuf::from("/etc/passwd"));
3006    /// assert_eq!(Path::new("/etc").join("/bin/sh"), PathBuf::from("/bin/sh"));
3007    /// ```
3008    #[stable(feature = "rust1", since = "1.0.0")]
3009    #[must_use]
3010    pub fn join<P: AsRef<Path>>(&self, path: P) -> PathBuf {
3011        self._join(path.as_ref())
3012    }
3013
3014    fn _join(&self, path: &Path) -> PathBuf {
3015        let mut buf = self.to_path_buf();
3016        buf.push(path);
3017        buf
3018    }
3019
3020    /// Creates an owned [`PathBuf`] like `self` but with the given file name.
3021    ///
3022    /// See [`PathBuf::set_file_name`] for more details.
3023    ///
3024    /// # Examples
3025    ///
3026    /// ```
3027    /// use std::path::{Path, PathBuf};
3028    ///
3029    /// let path = Path::new("/tmp/foo.png");
3030    /// assert_eq!(path.with_file_name("bar"), PathBuf::from("/tmp/bar"));
3031    /// assert_eq!(path.with_file_name("bar.txt"), PathBuf::from("/tmp/bar.txt"));
3032    ///
3033    /// let path = Path::new("/tmp");
3034    /// assert_eq!(path.with_file_name("var"), PathBuf::from("/var"));
3035    /// ```
3036    #[stable(feature = "rust1", since = "1.0.0")]
3037    #[must_use]
3038    pub fn with_file_name<S: AsRef<OsStr>>(&self, file_name: S) -> PathBuf {
3039        self._with_file_name(file_name.as_ref())
3040    }
3041
3042    fn _with_file_name(&self, file_name: &OsStr) -> PathBuf {
3043        let mut buf = self.to_path_buf();
3044        buf.set_file_name(file_name);
3045        buf
3046    }
3047
3048    /// Creates an owned [`PathBuf`] like `self` but with the given extension.
3049    ///
3050    /// See [`PathBuf::set_extension`] for more details.
3051    ///
3052    /// # Examples
3053    ///
3054    /// ```
3055    /// use std::path::Path;
3056    ///
3057    /// let path = Path::new("foo.rs");
3058    /// assert_eq!(path.with_extension("txt"), Path::new("foo.txt"));
3059    /// assert_eq!(path.with_extension(""), Path::new("foo"));
3060    /// ```
3061    ///
3062    /// Handling multiple extensions:
3063    ///
3064    /// ```
3065    /// use std::path::Path;
3066    ///
3067    /// let path = Path::new("foo.tar.gz");
3068    /// assert_eq!(path.with_extension("xz"), Path::new("foo.tar.xz"));
3069    /// assert_eq!(path.with_extension("").with_extension("txt"), Path::new("foo.txt"));
3070    /// ```
3071    ///
3072    /// Adding an extension where one did not exist:
3073    ///
3074    /// ```
3075    /// use std::path::Path;
3076    ///
3077    /// let path = Path::new("foo");
3078    /// assert_eq!(path.with_extension("rs"), Path::new("foo.rs"));
3079    /// ```
3080    #[stable(feature = "rust1", since = "1.0.0")]
3081    pub fn with_extension<S: AsRef<OsStr>>(&self, extension: S) -> PathBuf {
3082        self._with_extension(extension.as_ref())
3083    }
3084
3085    fn _with_extension(&self, extension: &OsStr) -> PathBuf {
3086        let self_len = self.as_os_str().len();
3087        let self_bytes = self.as_os_str().as_encoded_bytes();
3088
3089        let (new_capacity, slice_to_copy) = match self.extension() {
3090            None => {
3091                // Enough capacity for the extension and the dot
3092                let capacity = self_len + extension.len() + 1;
3093                let whole_path = self_bytes;
3094                (capacity, whole_path)
3095            }
3096            Some(previous_extension) => {
3097                let capacity = self_len + extension.len() - previous_extension.len();
3098                let path_till_dot = &self_bytes[..self_len - previous_extension.len()];
3099                (capacity, path_till_dot)
3100            }
3101        };
3102
3103        let mut new_path = PathBuf::with_capacity(new_capacity);
3104        // SAFETY: The path is empty, so cannot have surrogate halves.
3105        unsafe { new_path.inner.extend_from_slice_unchecked(slice_to_copy) };
3106        new_path.set_extension(extension);
3107        new_path
3108    }
3109
3110    /// Creates an owned [`PathBuf`] like `self` but with the extension added.
3111    ///
3112    /// See [`PathBuf::add_extension`] for more details.
3113    ///
3114    /// # Examples
3115    ///
3116    /// ```
3117    /// use std::path::{Path, PathBuf};
3118    ///
3119    /// let path = Path::new("foo.rs");
3120    /// assert_eq!(path.with_added_extension("txt"), PathBuf::from("foo.rs.txt"));
3121    ///
3122    /// let path = Path::new("foo.tar.gz");
3123    /// assert_eq!(path.with_added_extension(""), PathBuf::from("foo.tar.gz"));
3124    /// assert_eq!(path.with_added_extension("xz"), PathBuf::from("foo.tar.gz.xz"));
3125    /// assert_eq!(path.with_added_extension("").with_added_extension("txt"), PathBuf::from("foo.tar.gz.txt"));
3126    /// ```
3127    #[stable(feature = "path_add_extension", since = "1.91.0")]
3128    pub fn with_added_extension<S: AsRef<OsStr>>(&self, extension: S) -> PathBuf {
3129        let mut new_path = self.to_path_buf();
3130        new_path.add_extension(extension);
3131        new_path
3132    }
3133
3134    /// Produces an iterator over the [`Component`]s of the path.
3135    ///
3136    /// When parsing the path, there is a small amount of normalization:
3137    ///
3138    /// * Repeated separators are ignored, so `a/b` and `a//b` both have
3139    ///   `a` and `b` as components.
3140    ///
3141    /// * Occurrences of `.` are normalized away, except if they are at the
3142    ///   beginning of the path. For example, `a/./b`, `a/b/`, `a/b/.` and
3143    ///   `a/b` all have `a` and `b` as components, but `./a/b` starts with
3144    ///   an additional [`CurDir`] component.
3145    ///
3146    /// * Trailing separators are normalized away, so `/a/b` and `/a/b/` are equivalent.
3147    ///
3148    /// Note that no other normalization takes place; in particular, `a/c`
3149    /// and `a/b/../c` are distinct, to account for the possibility that `b`
3150    /// is a symbolic link (so its parent isn't `a`).
3151    ///
3152    /// # Examples
3153    ///
3154    /// ```
3155    /// use std::path::{Path, Component};
3156    /// use std::ffi::OsStr;
3157    ///
3158    /// let mut components = Path::new("/tmp/foo.txt").components();
3159    ///
3160    /// assert_eq!(components.next(), Some(Component::RootDir));
3161    /// assert_eq!(components.next(), Some(Component::Normal(OsStr::new("tmp"))));
3162    /// assert_eq!(components.next(), Some(Component::Normal(OsStr::new("foo.txt"))));
3163    /// assert_eq!(components.next(), None)
3164    /// ```
3165    ///
3166    /// [`CurDir`]: Component::CurDir
3167    #[stable(feature = "rust1", since = "1.0.0")]
3168    pub fn components(&self) -> Components<'_> {
3169        let prefix = parse_prefix(self.as_os_str());
3170        Components {
3171            path: self.as_u8_slice(),
3172            prefix,
3173            has_physical_root: has_physical_root(self.as_u8_slice(), prefix),
3174            // use a platform-specific initial state to avoid one turn of
3175            // the state-machine when the platform doesn't have a Prefix.
3176            front: const { if HAS_PREFIXES { State::Prefix } else { State::StartDir } },
3177            back: State::Body,
3178        }
3179    }
3180
3181    /// Produces an iterator over the path's components viewed as [`OsStr`]
3182    /// slices.
3183    ///
3184    /// For more information about the particulars of how the path is separated
3185    /// into components, see [`components`].
3186    ///
3187    /// [`components`]: Path::components
3188    ///
3189    /// # Examples
3190    ///
3191    /// ```
3192    /// use std::path::{self, Path};
3193    /// use std::ffi::OsStr;
3194    ///
3195    /// let mut it = Path::new("/tmp/foo.txt").iter();
3196    /// assert_eq!(it.next(), Some(OsStr::new(&path::MAIN_SEPARATOR.to_string())));
3197    /// assert_eq!(it.next(), Some(OsStr::new("tmp")));
3198    /// assert_eq!(it.next(), Some(OsStr::new("foo.txt")));
3199    /// assert_eq!(it.next(), None)
3200    /// ```
3201    #[stable(feature = "rust1", since = "1.0.0")]
3202    #[inline]
3203    pub fn iter(&self) -> Iter<'_> {
3204        Iter { inner: self.components() }
3205    }
3206
3207    /// Returns an object that implements [`Display`] for safely printing paths
3208    /// that may contain non-Unicode data. This may perform lossy conversion,
3209    /// depending on the platform.  If you would like an implementation which
3210    /// escapes the path please use [`Debug`] instead.
3211    ///
3212    /// [`Display`]: fmt::Display
3213    /// [`Debug`]: fmt::Debug
3214    ///
3215    /// # Examples
3216    ///
3217    /// ```
3218    /// use std::path::Path;
3219    ///
3220    /// let path = Path::new("/tmp/foo.rs");
3221    ///
3222    /// println!("{}", path.display());
3223    /// ```
3224    #[stable(feature = "rust1", since = "1.0.0")]
3225    #[must_use = "this does not display the path, \
3226                  it returns an object that can be displayed"]
3227    #[inline]
3228    pub fn display(&self) -> Display<'_> {
3229        Display { inner: self.inner.display() }
3230    }
3231
3232    /// Returns the same path as `&Path`.
3233    ///
3234    /// This method is redundant when used directly on `&Path`, but
3235    /// it helps dereferencing other `PathBuf`-like types to `Path`s,
3236    /// for example references to `Box<Path>` or `Arc<Path>`.
3237    #[inline]
3238    #[unstable(feature = "str_as_str", issue = "130366")]
3239    pub const fn as_path(&self) -> &Path {
3240        self
3241    }
3242
3243    /// Queries the file system to get information about a file, directory, etc.
3244    ///
3245    /// This function will traverse symbolic links to query information about the
3246    /// destination file.
3247    ///
3248    /// This is an alias to [`fs::metadata`].
3249    ///
3250    /// # Examples
3251    ///
3252    /// ```no_run
3253    /// use std::path::Path;
3254    ///
3255    /// let path = Path::new("/Minas/tirith");
3256    /// let metadata = path.metadata().expect("metadata call failed");
3257    /// println!("{:?}", metadata.file_type());
3258    /// ```
3259    #[stable(feature = "path_ext", since = "1.5.0")]
3260    #[inline]
3261    pub fn metadata(&self) -> io::Result<fs::Metadata> {
3262        fs::metadata(self)
3263    }
3264
3265    /// Queries the metadata about a file without following symlinks.
3266    ///
3267    /// This is an alias to [`fs::symlink_metadata`].
3268    ///
3269    /// # Examples
3270    ///
3271    /// ```no_run
3272    /// use std::path::Path;
3273    ///
3274    /// let path = Path::new("/Minas/tirith");
3275    /// let metadata = path.symlink_metadata().expect("symlink_metadata call failed");
3276    /// println!("{:?}", metadata.file_type());
3277    /// ```
3278    #[stable(feature = "path_ext", since = "1.5.0")]
3279    #[inline]
3280    pub fn symlink_metadata(&self) -> io::Result<fs::Metadata> {
3281        fs::symlink_metadata(self)
3282    }
3283
3284    /// Returns the canonical, absolute form of the path with all intermediate
3285    /// components normalized and symbolic links resolved.
3286    ///
3287    /// This is an alias to [`fs::canonicalize`].
3288    ///
3289    /// # Errors
3290    ///
3291    /// This method will return an error in the following situations, but is not
3292    /// limited to just these cases:
3293    ///
3294    /// * `path` does not exist.
3295    /// * A non-final component in path is not a directory.
3296    ///
3297    /// # Examples
3298    ///
3299    /// ```no_run
3300    /// use std::path::{Path, PathBuf};
3301    ///
3302    /// let path = Path::new("/foo/test/../test/bar.rs");
3303    /// assert_eq!(path.canonicalize().unwrap(), PathBuf::from("/foo/test/bar.rs"));
3304    /// ```
3305    #[stable(feature = "path_ext", since = "1.5.0")]
3306    #[inline]
3307    pub fn canonicalize(&self) -> io::Result<PathBuf> {
3308        fs::canonicalize(self)
3309    }
3310
3311    /// Normalize a path, including `..` without traversing the filesystem.
3312    ///
3313    /// Returns an error if normalization would leave leading `..` components.
3314    ///
3315    /// <div class="warning">
3316    ///
3317    /// This function always resolves `..` to the "lexical" parent.
3318    /// That is "a/b/../c" will always resolve to `a/c` which can change the meaning of the path.
3319    /// In particular, `a/c` and `a/b/../c` are distinct on many systems because `b` may be a symbolic link, so its parent isn't `a`.
3320    ///
3321    /// </div>
3322    ///
3323    /// [`path::absolute`](absolute) is an alternative that preserves `..`.
3324    /// Or [`Path::canonicalize`] can be used to resolve any `..` by querying the filesystem.
3325    #[unstable(feature = "normalize_lexically", issue = "134694")]
3326    pub fn normalize_lexically(&self) -> Result<PathBuf, NormalizeError> {
3327        let mut lexical = PathBuf::new();
3328        let mut iter = self.components().peekable();
3329
3330        // Find the root, if any, and add it to the lexical path.
3331        // Here we treat the Windows path "C:\" as a single "root" even though
3332        // `components` splits it into two: (Prefix, RootDir).
3333        let root = match iter.peek() {
3334            Some(Component::ParentDir) => return Err(NormalizeError),
3335            Some(p @ Component::RootDir) | Some(p @ Component::CurDir) => {
3336                lexical.push(p);
3337                iter.next();
3338                lexical.as_os_str().len()
3339            }
3340            Some(Component::Prefix(prefix)) => {
3341                lexical.push(prefix.as_os_str());
3342                iter.next();
3343                if let Some(p @ Component::RootDir) = iter.peek() {
3344                    lexical.push(p);
3345                    iter.next();
3346                }
3347                lexical.as_os_str().len()
3348            }
3349            None => return Ok(PathBuf::new()),
3350            Some(Component::Normal(_)) => 0,
3351        };
3352
3353        for component in iter {
3354            match component {
3355                Component::RootDir => unreachable!(),
3356                Component::Prefix(_) => return Err(NormalizeError),
3357                Component::CurDir => continue,
3358                Component::ParentDir => {
3359                    // It's an error if ParentDir causes us to go above the "root".
3360                    if lexical.as_os_str().len() == root {
3361                        return Err(NormalizeError);
3362                    } else {
3363                        lexical.pop();
3364                    }
3365                }
3366                Component::Normal(path) => lexical.push(path),
3367            }
3368        }
3369        Ok(lexical)
3370    }
3371
3372    /// Reads a symbolic link, returning the file that the link points to.
3373    ///
3374    /// This is an alias to [`fs::read_link`].
3375    ///
3376    /// # Examples
3377    ///
3378    /// ```no_run
3379    /// use std::path::Path;
3380    ///
3381    /// let path = Path::new("/laputa/sky_castle.rs");
3382    /// let path_link = path.read_link().expect("read_link call failed");
3383    /// ```
3384    #[stable(feature = "path_ext", since = "1.5.0")]
3385    #[inline]
3386    pub fn read_link(&self) -> io::Result<PathBuf> {
3387        fs::read_link(self)
3388    }
3389
3390    /// Returns an iterator over the entries within a directory.
3391    ///
3392    /// The iterator will yield instances of <code>[io::Result]<[fs::DirEntry]></code>. New
3393    /// errors may be encountered after an iterator is initially constructed.
3394    ///
3395    /// This is an alias to [`fs::read_dir`].
3396    ///
3397    /// # Examples
3398    ///
3399    /// ```no_run
3400    /// use std::path::Path;
3401    ///
3402    /// let path = Path::new("/laputa");
3403    /// for entry in path.read_dir().expect("read_dir call failed") {
3404    ///     if let Ok(entry) = entry {
3405    ///         println!("{:?}", entry.path());
3406    ///     }
3407    /// }
3408    /// ```
3409    #[stable(feature = "path_ext", since = "1.5.0")]
3410    #[inline]
3411    pub fn read_dir(&self) -> io::Result<fs::ReadDir> {
3412        fs::read_dir(self)
3413    }
3414
3415    /// Returns `true` if the path points at an existing entity.
3416    ///
3417    /// Warning: this method may be error-prone, consider using [`try_exists()`] instead!
3418    /// It also has a risk of introducing time-of-check to time-of-use ([TOCTOU]) bugs.
3419    ///
3420    /// This function will traverse symbolic links to query information about the
3421    /// destination file.
3422    ///
3423    /// If you cannot access the metadata of the file, e.g. because of a
3424    /// permission error or broken symbolic links, this will return `false`.
3425    ///
3426    /// # Examples
3427    ///
3428    /// ```no_run
3429    /// use std::path::Path;
3430    /// assert!(!Path::new("does_not_exist.txt").exists());
3431    /// ```
3432    ///
3433    /// # See Also
3434    ///
3435    /// This is a convenience function that coerces errors to false. If you want to
3436    /// check errors, call [`Path::try_exists`].
3437    ///
3438    /// [`try_exists()`]: Self::try_exists
3439    /// [TOCTOU]: fs#time-of-check-to-time-of-use-toctou
3440    #[stable(feature = "path_ext", since = "1.5.0")]
3441    #[must_use]
3442    #[inline]
3443    pub fn exists(&self) -> bool {
3444        fs::metadata(self).is_ok()
3445    }
3446
3447    /// Returns `Ok(true)` if the path points at an existing entity.
3448    ///
3449    /// This function will traverse symbolic links to query information about the
3450    /// destination file. In case of broken symbolic links this will return `Ok(false)`.
3451    ///
3452    /// [`Path::exists()`] only checks whether or not a path was both found and readable. By
3453    /// contrast, `try_exists` will return `Ok(true)` or `Ok(false)`, respectively, if the path
3454    /// was _verified_ to exist or not exist. If its existence can neither be confirmed nor
3455    /// denied, it will propagate an `Err(_)` instead. This can be the case if e.g. listing
3456    /// permission is denied on one of the parent directories.
3457    ///
3458    /// Note that while this avoids some pitfalls of the `exists()` method, it still can not
3459    /// prevent time-of-check to time-of-use ([TOCTOU]) bugs. You should only use it in scenarios
3460    /// where those bugs are not an issue.
3461    ///
3462    /// This is an alias for [`std::fs::exists`](crate::fs::exists).
3463    ///
3464    /// # Examples
3465    ///
3466    /// ```no_run
3467    /// use std::path::Path;
3468    /// assert!(!Path::new("does_not_exist.txt").try_exists().expect("Can't check existence of file does_not_exist.txt"));
3469    /// assert!(Path::new("/root/secret_file.txt").try_exists().is_err());
3470    /// ```
3471    ///
3472    /// [TOCTOU]: fs#time-of-check-to-time-of-use-toctou
3473    /// [`exists()`]: Self::exists
3474    #[stable(feature = "path_try_exists", since = "1.63.0")]
3475    #[inline]
3476    pub fn try_exists(&self) -> io::Result<bool> {
3477        fs::exists(self)
3478    }
3479
3480    /// Returns `true` if the path exists on disk and is pointing at a regular file.
3481    ///
3482    /// This function will traverse symbolic links to query information about the
3483    /// destination file.
3484    ///
3485    /// If you cannot access the metadata of the file, e.g. because of a
3486    /// permission error or broken symbolic links, this will return `false`.
3487    ///
3488    /// # Examples
3489    ///
3490    /// ```no_run
3491    /// use std::path::Path;
3492    /// assert_eq!(Path::new("./is_a_directory/").is_file(), false);
3493    /// assert_eq!(Path::new("a_file.txt").is_file(), true);
3494    /// ```
3495    ///
3496    /// # See Also
3497    ///
3498    /// This is a convenience function that coerces errors to false. If you want to
3499    /// check errors, call [`fs::metadata`] and handle its [`Result`]. Then call
3500    /// [`fs::Metadata::is_file`] if it was [`Ok`].
3501    ///
3502    /// When the goal is simply to read from (or write to) the source, the most
3503    /// reliable way to test the source can be read (or written to) is to open
3504    /// it. Only using `is_file` can break workflows like `diff <( prog_a )` on
3505    /// a Unix-like system for example. See [`fs::File::open`] or
3506    /// [`fs::OpenOptions::open`] for more information.
3507    #[stable(feature = "path_ext", since = "1.5.0")]
3508    #[must_use]
3509    pub fn is_file(&self) -> bool {
3510        fs::metadata(self).map(|m| m.is_file()).unwrap_or(false)
3511    }
3512
3513    /// Returns `true` if the path exists on disk and is pointing at a directory.
3514    ///
3515    /// This function will traverse symbolic links to query information about the
3516    /// destination file.
3517    ///
3518    /// If you cannot access the metadata of the file, e.g. because of a
3519    /// permission error or broken symbolic links, this will return `false`.
3520    ///
3521    /// # Examples
3522    ///
3523    /// ```no_run
3524    /// use std::path::Path;
3525    /// assert_eq!(Path::new("./is_a_directory/").is_dir(), true);
3526    /// assert_eq!(Path::new("a_file.txt").is_dir(), false);
3527    /// ```
3528    ///
3529    /// # See Also
3530    ///
3531    /// This is a convenience function that coerces errors to false. If you want to
3532    /// check errors, call [`fs::metadata`] and handle its [`Result`]. Then call
3533    /// [`fs::Metadata::is_dir`] if it was [`Ok`].
3534    #[stable(feature = "path_ext", since = "1.5.0")]
3535    #[must_use]
3536    pub fn is_dir(&self) -> bool {
3537        fs::metadata(self).map(|m| m.is_dir()).unwrap_or(false)
3538    }
3539
3540    /// Returns `true` if the path exists on disk and is pointing at a symbolic link.
3541    ///
3542    /// This function will not traverse symbolic links.
3543    /// In case of a broken symbolic link this will also return true.
3544    ///
3545    /// If you cannot access the directory containing the file, e.g., because of a
3546    /// permission error, this will return false.
3547    ///
3548    /// # Examples
3549    ///
3550    /// ```rust,no_run
3551    /// # #[cfg(unix)] {
3552    /// use std::path::Path;
3553    /// use std::os::unix::fs::symlink;
3554    ///
3555    /// let link_path = Path::new("link");
3556    /// symlink("/origin_does_not_exist/", link_path).unwrap();
3557    /// assert_eq!(link_path.is_symlink(), true);
3558    /// assert_eq!(link_path.exists(), false);
3559    /// # }
3560    /// ```
3561    ///
3562    /// # See Also
3563    ///
3564    /// This is a convenience function that coerces errors to false. If you want to
3565    /// check errors, call [`fs::symlink_metadata`] and handle its [`Result`]. Then call
3566    /// [`fs::Metadata::is_symlink`] if it was [`Ok`].
3567    #[must_use]
3568    #[stable(feature = "is_symlink", since = "1.58.0")]
3569    pub fn is_symlink(&self) -> bool {
3570        fs::symlink_metadata(self).map(|m| m.is_symlink()).unwrap_or(false)
3571    }
3572
3573    /// Converts a [`Box<Path>`](Box) into a [`PathBuf`] without copying or
3574    /// allocating.
3575    #[stable(feature = "into_boxed_path", since = "1.20.0")]
3576    #[must_use = "`self` will be dropped if the result is not used"]
3577    pub fn into_path_buf(self: Box<Self>) -> PathBuf {
3578        let rw = Box::into_raw(self) as *mut OsStr;
3579        let inner = unsafe { Box::from_raw(rw) };
3580        PathBuf { inner: OsString::from(inner) }
3581    }
3582}
3583
3584#[unstable(feature = "clone_to_uninit", issue = "126799")]
3585unsafe impl CloneToUninit for Path {
3586    #[inline]
3587    #[cfg_attr(debug_assertions, track_caller)]
3588    unsafe fn clone_to_uninit(&self, dst: *mut u8) {
3589        // SAFETY: Path is just a transparent wrapper around OsStr
3590        unsafe { self.inner.clone_to_uninit(dst) }
3591    }
3592}
3593
3594#[stable(feature = "rust1", since = "1.0.0")]
3595#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
3596impl const AsRef<OsStr> for Path {
3597    #[inline]
3598    fn as_ref(&self) -> &OsStr {
3599        &self.inner
3600    }
3601}
3602
3603#[stable(feature = "rust1", since = "1.0.0")]
3604impl fmt::Debug for Path {
3605    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
3606        fmt::Debug::fmt(&self.inner, formatter)
3607    }
3608}
3609
3610/// Helper struct for safely printing paths with [`format!`] and `{}`.
3611///
3612/// A [`Path`] might contain non-Unicode data. This `struct` implements the
3613/// [`Display`] trait in a way that mitigates that. It is created by the
3614/// [`display`](Path::display) method on [`Path`]. This may perform lossy
3615/// conversion, depending on the platform. If you would like an implementation
3616/// which escapes the path please use [`Debug`] instead.
3617///
3618/// # Examples
3619///
3620/// ```
3621/// use std::path::Path;
3622///
3623/// let path = Path::new("/tmp/foo.rs");
3624///
3625/// println!("{}", path.display());
3626/// ```
3627///
3628/// [`Display`]: fmt::Display
3629/// [`format!`]: crate::format
3630#[stable(feature = "rust1", since = "1.0.0")]
3631pub struct Display<'a> {
3632    inner: os_str::Display<'a>,
3633}
3634
3635#[stable(feature = "rust1", since = "1.0.0")]
3636impl fmt::Debug for Display<'_> {
3637    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3638        fmt::Debug::fmt(&self.inner, f)
3639    }
3640}
3641
3642#[stable(feature = "rust1", since = "1.0.0")]
3643impl fmt::Display for Display<'_> {
3644    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3645        fmt::Display::fmt(&self.inner, f)
3646    }
3647}
3648
3649#[stable(feature = "rust1", since = "1.0.0")]
3650impl PartialEq for Path {
3651    #[inline]
3652    fn eq(&self, other: &Path) -> bool {
3653        self.components() == other.components()
3654    }
3655}
3656
3657#[stable(feature = "eq_str_for_path", since = "1.91.0")]
3658impl cmp::PartialEq<str> for Path {
3659    #[inline]
3660    fn eq(&self, other: &str) -> bool {
3661        let other: &OsStr = other.as_ref();
3662        self == other
3663    }
3664}
3665
3666#[stable(feature = "eq_str_for_path", since = "1.91.0")]
3667impl cmp::PartialEq<Path> for str {
3668    #[inline]
3669    fn eq(&self, other: &Path) -> bool {
3670        other == self
3671    }
3672}
3673
3674#[stable(feature = "eq_str_for_path", since = "1.91.0")]
3675impl cmp::PartialEq<String> for Path {
3676    #[inline]
3677    fn eq(&self, other: &String) -> bool {
3678        self == other.as_str()
3679    }
3680}
3681
3682#[stable(feature = "eq_str_for_path", since = "1.91.0")]
3683impl cmp::PartialEq<Path> for String {
3684    #[inline]
3685    fn eq(&self, other: &Path) -> bool {
3686        self.as_str() == other
3687    }
3688}
3689
3690#[stable(feature = "rust1", since = "1.0.0")]
3691impl Hash for Path {
3692    fn hash<H: Hasher>(&self, h: &mut H) {
3693        let bytes = self.as_u8_slice();
3694        let (prefix_len, verbatim) = match parse_prefix(&self.inner) {
3695            Some(prefix) => {
3696                prefix.hash(h);
3697                (prefix.len(), prefix.is_verbatim())
3698            }
3699            None => (0, false),
3700        };
3701        let bytes = &bytes[prefix_len..];
3702
3703        let mut component_start = 0;
3704        // track some extra state to avoid prefix collisions.
3705        // ["foo", "bar"] and ["foobar"], will have the same payload bytes
3706        // but result in different chunk_bits
3707        let mut chunk_bits: usize = 0;
3708
3709        for i in 0..bytes.len() {
3710            let is_sep = if verbatim { is_verbatim_sep(bytes[i]) } else { is_sep_byte(bytes[i]) };
3711            if is_sep {
3712                if i > component_start {
3713                    let to_hash = &bytes[component_start..i];
3714                    chunk_bits = chunk_bits.wrapping_add(to_hash.len());
3715                    chunk_bits = chunk_bits.rotate_right(2);
3716                    h.write(to_hash);
3717                }
3718
3719                // skip over separator and optionally a following CurDir item
3720                // since components() would normalize these away.
3721                component_start = i + 1;
3722
3723                let tail = &bytes[component_start..];
3724
3725                if !verbatim {
3726                    component_start += match tail {
3727                        [b'.'] => 1,
3728                        [b'.', sep, ..] if is_sep_byte(*sep) => 1,
3729                        _ => 0,
3730                    };
3731                }
3732            }
3733        }
3734
3735        if component_start < bytes.len() {
3736            let to_hash = &bytes[component_start..];
3737            chunk_bits = chunk_bits.wrapping_add(to_hash.len());
3738            chunk_bits = chunk_bits.rotate_right(2);
3739            h.write(to_hash);
3740        }
3741
3742        h.write_usize(chunk_bits);
3743    }
3744}
3745
3746#[stable(feature = "rust1", since = "1.0.0")]
3747impl Eq for Path {}
3748
3749#[stable(feature = "rust1", since = "1.0.0")]
3750impl PartialOrd for Path {
3751    #[inline]
3752    fn partial_cmp(&self, other: &Path) -> Option<cmp::Ordering> {
3753        Some(compare_components(self.components(), other.components()))
3754    }
3755}
3756
3757#[stable(feature = "rust1", since = "1.0.0")]
3758impl Ord for Path {
3759    #[inline]
3760    fn cmp(&self, other: &Path) -> cmp::Ordering {
3761        compare_components(self.components(), other.components())
3762    }
3763}
3764
3765#[stable(feature = "rust1", since = "1.0.0")]
3766#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
3767impl const AsRef<Path> for Path {
3768    #[inline]
3769    fn as_ref(&self) -> &Path {
3770        self
3771    }
3772}
3773
3774#[stable(feature = "rust1", since = "1.0.0")]
3775#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
3776impl const AsRef<Path> for OsStr {
3777    #[inline]
3778    fn as_ref(&self) -> &Path {
3779        Path::new(self)
3780    }
3781}
3782
3783#[stable(feature = "cow_os_str_as_ref_path", since = "1.8.0")]
3784impl AsRef<Path> for Cow<'_, OsStr> {
3785    #[inline]
3786    fn as_ref(&self) -> &Path {
3787        Path::new(self)
3788    }
3789}
3790
3791#[stable(feature = "rust1", since = "1.0.0")]
3792impl AsRef<Path> for OsString {
3793    #[inline]
3794    fn as_ref(&self) -> &Path {
3795        Path::new(self)
3796    }
3797}
3798
3799#[stable(feature = "rust1", since = "1.0.0")]
3800impl AsRef<Path> for str {
3801    #[inline]
3802    fn as_ref(&self) -> &Path {
3803        Path::new(self)
3804    }
3805}
3806
3807#[stable(feature = "rust1", since = "1.0.0")]
3808impl AsRef<Path> for String {
3809    #[inline]
3810    fn as_ref(&self) -> &Path {
3811        Path::new(self)
3812    }
3813}
3814
3815#[stable(feature = "rust1", since = "1.0.0")]
3816impl AsRef<Path> for PathBuf {
3817    #[inline]
3818    fn as_ref(&self) -> &Path {
3819        self
3820    }
3821}
3822
3823#[stable(feature = "path_into_iter", since = "1.6.0")]
3824impl<'a> IntoIterator for &'a PathBuf {
3825    type Item = &'a OsStr;
3826    type IntoIter = Iter<'a>;
3827    #[inline]
3828    fn into_iter(self) -> Iter<'a> {
3829        self.iter()
3830    }
3831}
3832
3833#[stable(feature = "path_into_iter", since = "1.6.0")]
3834impl<'a> IntoIterator for &'a Path {
3835    type Item = &'a OsStr;
3836    type IntoIter = Iter<'a>;
3837    #[inline]
3838    fn into_iter(self) -> Iter<'a> {
3839        self.iter()
3840    }
3841}
3842
3843macro_rules! impl_cmp {
3844    ($lhs:ty, $rhs: ty) => {
3845        #[stable(feature = "partialeq_path", since = "1.6.0")]
3846        impl PartialEq<$rhs> for $lhs {
3847            #[inline]
3848            fn eq(&self, other: &$rhs) -> bool {
3849                <Path as PartialEq>::eq(self, other)
3850            }
3851        }
3852
3853        #[stable(feature = "partialeq_path", since = "1.6.0")]
3854        impl PartialEq<$lhs> for $rhs {
3855            #[inline]
3856            fn eq(&self, other: &$lhs) -> bool {
3857                <Path as PartialEq>::eq(self, other)
3858            }
3859        }
3860
3861        #[stable(feature = "cmp_path", since = "1.8.0")]
3862        impl PartialOrd<$rhs> for $lhs {
3863            #[inline]
3864            fn partial_cmp(&self, other: &$rhs) -> Option<cmp::Ordering> {
3865                <Path as PartialOrd>::partial_cmp(self, other)
3866            }
3867        }
3868
3869        #[stable(feature = "cmp_path", since = "1.8.0")]
3870        impl PartialOrd<$lhs> for $rhs {
3871            #[inline]
3872            fn partial_cmp(&self, other: &$lhs) -> Option<cmp::Ordering> {
3873                <Path as PartialOrd>::partial_cmp(self, other)
3874            }
3875        }
3876    };
3877}
3878
3879impl_cmp!(PathBuf, Path);
3880impl_cmp!(PathBuf, &Path);
3881impl_cmp!(Cow<'_, Path>, Path);
3882impl_cmp!(Cow<'_, Path>, &Path);
3883impl_cmp!(Cow<'_, Path>, PathBuf);
3884
3885macro_rules! impl_cmp_os_str {
3886    ($lhs:ty, $rhs: ty) => {
3887        #[stable(feature = "cmp_path", since = "1.8.0")]
3888        impl PartialEq<$rhs> for $lhs {
3889            #[inline]
3890            fn eq(&self, other: &$rhs) -> bool {
3891                <Path as PartialEq>::eq(self, other.as_ref())
3892            }
3893        }
3894
3895        #[stable(feature = "cmp_path", since = "1.8.0")]
3896        impl PartialEq<$lhs> for $rhs {
3897            #[inline]
3898            fn eq(&self, other: &$lhs) -> bool {
3899                <Path as PartialEq>::eq(self.as_ref(), other)
3900            }
3901        }
3902
3903        #[stable(feature = "cmp_path", since = "1.8.0")]
3904        impl PartialOrd<$rhs> for $lhs {
3905            #[inline]
3906            fn partial_cmp(&self, other: &$rhs) -> Option<cmp::Ordering> {
3907                <Path as PartialOrd>::partial_cmp(self, other.as_ref())
3908            }
3909        }
3910
3911        #[stable(feature = "cmp_path", since = "1.8.0")]
3912        impl PartialOrd<$lhs> for $rhs {
3913            #[inline]
3914            fn partial_cmp(&self, other: &$lhs) -> Option<cmp::Ordering> {
3915                <Path as PartialOrd>::partial_cmp(self.as_ref(), other)
3916            }
3917        }
3918    };
3919}
3920
3921impl_cmp_os_str!(PathBuf, OsStr);
3922impl_cmp_os_str!(PathBuf, &OsStr);
3923impl_cmp_os_str!(PathBuf, Cow<'_, OsStr>);
3924impl_cmp_os_str!(PathBuf, OsString);
3925impl_cmp_os_str!(Path, OsStr);
3926impl_cmp_os_str!(Path, &OsStr);
3927impl_cmp_os_str!(Path, Cow<'_, OsStr>);
3928impl_cmp_os_str!(Path, OsString);
3929impl_cmp_os_str!(&Path, OsStr);
3930impl_cmp_os_str!(&Path, Cow<'_, OsStr>);
3931impl_cmp_os_str!(&Path, OsString);
3932impl_cmp_os_str!(Cow<'_, Path>, OsStr);
3933impl_cmp_os_str!(Cow<'_, Path>, &OsStr);
3934impl_cmp_os_str!(Cow<'_, Path>, OsString);
3935
3936#[stable(since = "1.7.0", feature = "strip_prefix")]
3937impl fmt::Display for StripPrefixError {
3938    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3939        "prefix not found".fmt(f)
3940    }
3941}
3942
3943#[stable(since = "1.7.0", feature = "strip_prefix")]
3944impl Error for StripPrefixError {}
3945
3946#[unstable(feature = "normalize_lexically", issue = "134694")]
3947impl fmt::Display for NormalizeError {
3948    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3949        f.write_str("parent reference `..` points outside of base directory")
3950    }
3951}
3952#[unstable(feature = "normalize_lexically", issue = "134694")]
3953impl Error for NormalizeError {}
3954
3955/// Makes the path absolute without accessing the filesystem.
3956///
3957/// If the path is relative, the current directory is used as the base directory.
3958/// All intermediate components will be resolved according to platform-specific
3959/// rules, but unlike [`canonicalize`][crate::fs::canonicalize], this does not
3960/// resolve symlinks and may succeed even if the path does not exist.
3961///
3962/// If the `path` is empty or getting the
3963/// [current directory][crate::env::current_dir] fails, then an error will be
3964/// returned.
3965///
3966/// # Platform-specific behavior
3967///
3968/// On POSIX platforms, the path is resolved using [POSIX semantics][posix-semantics],
3969/// except that it stops short of resolving symlinks. This means it will keep `..`
3970/// components and trailing separators.
3971///
3972/// On Windows, for verbatim paths, this will simply return the path as given. For other
3973/// paths, this is currently equivalent to calling
3974/// [`GetFullPathNameW`][windows-path].
3975///
3976/// On Cygwin, this is currently equivalent to calling [`cygwin_conv_path`][cygwin-path]
3977/// with mode `CCP_WIN_A_TO_POSIX`, and then being processed like other POSIX platforms.
3978/// If a Windows path is given, it will be converted to an absolute POSIX path without
3979/// keeping `..`.
3980///
3981/// Note that these [may change in the future][changes].
3982///
3983/// # Errors
3984///
3985/// This function may return an error in the following situations:
3986///
3987/// * If `path` is syntactically invalid; in particular, if it is empty.
3988/// * If getting the [current directory][crate::env::current_dir] fails.
3989///
3990/// # Examples
3991///
3992/// ## POSIX paths
3993///
3994/// ```
3995/// # #[cfg(unix)]
3996/// fn main() -> std::io::Result<()> {
3997///     use std::path::{self, Path};
3998///
3999///     // Relative to absolute
4000///     let absolute = path::absolute("foo/./bar")?;
4001///     assert!(absolute.ends_with("foo/bar"));
4002///
4003///     // Absolute to absolute
4004///     let absolute = path::absolute("/foo//test/.././bar.rs")?;
4005///     assert_eq!(absolute, Path::new("/foo/test/../bar.rs"));
4006///     Ok(())
4007/// }
4008/// # #[cfg(not(unix))]
4009/// # fn main() {}
4010/// ```
4011///
4012/// ## Windows paths
4013///
4014/// ```
4015/// # #[cfg(windows)]
4016/// fn main() -> std::io::Result<()> {
4017///     use std::path::{self, Path};
4018///
4019///     // Relative to absolute
4020///     let absolute = path::absolute("foo/./bar")?;
4021///     assert!(absolute.ends_with(r"foo\bar"));
4022///
4023///     // Absolute to absolute
4024///     let absolute = path::absolute(r"C:\foo//test\..\./bar.rs")?;
4025///
4026///     assert_eq!(absolute, Path::new(r"C:\foo\bar.rs"));
4027///     Ok(())
4028/// }
4029/// # #[cfg(not(windows))]
4030/// # fn main() {}
4031/// ```
4032///
4033/// Note that this [may change in the future][changes].
4034///
4035/// [changes]: io#platform-specific-behavior
4036/// [posix-semantics]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13
4037/// [windows-path]: https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfullpathnamew
4038/// [cygwin-path]: https://cygwin.com/cygwin-api/func-cygwin-conv-path.html
4039#[stable(feature = "absolute_path", since = "1.79.0")]
4040pub fn absolute<P: AsRef<Path>>(path: P) -> io::Result<PathBuf> {
4041    let path = path.as_ref();
4042    if path.as_os_str().is_empty() {
4043        Err(io::const_error!(io::ErrorKind::InvalidInput, "cannot make an empty path absolute"))
4044    } else {
4045        sys::path::absolute(path)
4046    }
4047}
````