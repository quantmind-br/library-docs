---
title: PathBuf in std::path - Rust
url: https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html
source: crawler
fetched_at: 2026-05-06T21:34:12.599468283-03:00
rendered_js: false
word_count: 5659
summary: PathBuf is an owned, mutable type in the Rust standard library used for representing and manipulating filesystem paths.
tags:
    - rust
    - pathbuf
    - filesystem
    - standard-library
    - path-manipulation
category: reference
---

## Struct PathBuf

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1203-1205)

```rust
pub struct PathBuf { /* private fields */ }
```

Expand description

An owned, mutable path (akin to [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String")).

This type provides methods like [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") and [`set_extension`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.set_extension "method std::path::PathBuf::set_extension") that mutate the path in place. It also implements [`Deref`](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html "trait std::ops::Deref") to [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path"), meaning that all methods on [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path") slices are available on `PathBuf` values as well.

More details about the overall approach can be found in the [module documentation](https://doc.rust-lang.org/stable/std/path/index.html "mod std::path").

## [§](#examples)Examples

You can use [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") to build up a `PathBuf` from components:

```rust
use std::path::PathBuf;

let mut path = PathBuf::new();

path.push(r"C:\");
path.push("windows");
path.push("system32");

path.set_extension("dll");
```

However, [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") is best used for dynamic situations. This is a better way to do this when you know all of the components ahead of time:

```rust
use std::path::PathBuf;

let path: PathBuf = [r"C:\", "windows", "system32.dll"].iter().collect();
```

We can still do better than this! Since these are all strings, we can use `From::from`:

```rust
use std::path::PathBuf;

let path = PathBuf::from(r"C:\windows\system32.dll");
```

Which method works best depends on what kind of situation you’re in.

Note that `PathBuf` does not always sanitize arguments, for example [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") allows paths built from strings which include separators:

```rust
use std::path::PathBuf;

let mut path = PathBuf::new();

path.push(r"C:\");
path.push("windows");
path.push(r"..\otherdir");
path.push("system32");
```

The behavior of `PathBuf` may be changed to a panic on such inputs in the future. [`Extend::extend`](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#tymethod.extend "method std::iter::Extend::extend") should be used to add multi-part paths.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1207-1869)[§](#impl-PathBuf)

1.0.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1221-1223)

Allocates an empty `PathBuf`.

##### [§](#examples-1)Examples

```rust
use std::path::PathBuf;

let path = PathBuf::new();
```

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1246-1248)

Creates a new `PathBuf` with a given capacity used to create the internal [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString"). See [`with_capacity`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html#method.with_capacity "associated function std::ffi::OsString::with_capacity") defined on [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString").

##### [§](#examples-2)Examples

```rust
use std::path::PathBuf;

let mut path = PathBuf::with_capacity(10);
let capacity = path.capacity();

// This push is done without reallocating
path.push(r"C:\");

assert_eq!(capacity, path.capacity());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1264-1266)

Coerces to a [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path") slice.

##### [§](#examples-3)Examples

```rust
use std::path::{Path, PathBuf};

let p = PathBuf::from("/test");
assert_eq!(Path::new("/test"), p.as_path());
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1283-1285)

Consumes and leaks the `PathBuf`, returning a mutable reference to the contents, `&'a mut Path`.

The caller has free choice over the returned lifetime, including ’static. Indeed, this function is ideally used for data that lives for the remainder of the program’s life, as dropping the returned reference will cause a memory leak.

It does not reallocate or shrink the `PathBuf`, so the leaked allocation may include unused capacity that is not part of the returned slice. If you want to discard excess capacity, call [`into_boxed_path`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.into_boxed_path "method std::path::PathBuf::into_boxed_path"), and then [`Box::leak`](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html#method.leak "associated function std::boxed::Box::leak") instead. However, keep in mind that trimming the capacity may result in a reallocation and copy.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1326-1328)

Extends `self` with `path`.

If `path` is absolute, it replaces the current path.

On Windows:

- if `path` has a root but no prefix (e.g., `\windows`), it replaces everything except for the prefix (if any) of `self`.
- if `path` has a prefix but no root, it replaces `self`.
- if `self` has a verbatim prefix (e.g. `\\?\C:\windows`) and `path` is not empty, the new path is normalized: all references to `.` and `..` are removed.

Consider using [`Path::join`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.join "method std::path::Path::join") if you need a new `PathBuf` instead of using this function on a cloned `PathBuf`.

##### [§](#examples-4)Examples

Pushing a relative path extends the existing path:

```rust
use std::path::PathBuf;

let mut path = PathBuf::from("/tmp");
path.push("file.bk");
assert_eq!(path, PathBuf::from("/tmp/file.bk"));
```

Pushing an absolute path replaces the existing path:

```rust
use std::path::PathBuf;

let mut path = PathBuf::from("/tmp");
path.push("/etc");
assert_eq!(path, PathBuf::from("/etc"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1431-1439)

Truncates `self` to [`self.parent`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.parent "method std::path::Path::parent").

Returns `false` and does nothing if [`self.parent`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.parent "method std::path::Path::parent") is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"). Otherwise, returns `true`.

##### [§](#examples-5)Examples

```rust
use std::path::{Path, PathBuf};

let mut p = PathBuf::from("/spirited/away.rs");

p.pop();
assert_eq!(Path::new("/spirited"), p);
p.pop();
assert_eq!(Path::new("/"), p);
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1468-1470)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Sets whether the path has a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR").

The value returned by [`has_trailing_sep`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.has_trailing_sep "method std::path::Path::has_trailing_sep") will be equivalent to the provided value if possible.

##### [§](#examples-6)Examples

```rust
#![feature(path_trailing_sep)]
use std::path::PathBuf;

let mut p = PathBuf::from("dir");

assert!(!p.has_trailing_sep());
p.set_trailing_sep(false);
assert!(!p.has_trailing_sep());
p.set_trailing_sep(true);
assert!(p.has_trailing_sep());
p.set_trailing_sep(false);
assert!(!p.has_trailing_sep());

p = PathBuf::from("/");
assert!(p.has_trailing_sep());
p.set_trailing_sep(false);
assert!(p.has_trailing_sep());
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1496-1500)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Adds a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR") to the path.

This acts similarly to [`Path::with_trailing_sep`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.with_trailing_sep "method std::path::Path::with_trailing_sep"), but mutates the underlying `PathBuf`.

##### [§](#examples-7)Examples

```rust
#![feature(path_trailing_sep)]
use std::ffi::OsStr;
use std::path::PathBuf;

let mut p = PathBuf::from("dir");

assert!(!p.has_trailing_sep());
p.push_trailing_sep();
assert!(p.has_trailing_sep());
p.push_trailing_sep();
assert!(p.has_trailing_sep());

p = PathBuf::from("dir/");
p.push_trailing_sep();
assert_eq!(p.as_os_str(), OsStr::new("dir/"));
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1530-1532)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Removes a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR") from the path, if possible.

This acts similarly to [`Path::trim_trailing_sep`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.trim_trailing_sep "method std::path::Path::trim_trailing_sep"), but mutates the underlying `PathBuf`.

##### [§](#examples-8)Examples

```rust
#![feature(path_trailing_sep)]
use std::ffi::OsStr;
use std::path::PathBuf;

let mut p = PathBuf::from("dir//");

assert!(p.has_trailing_sep());
assert_eq!(p.as_os_str(), OsStr::new("dir//"));
p.pop_trailing_sep();
assert!(!p.has_trailing_sep());
assert_eq!(p.as_os_str(), OsStr::new("dir"));
p.pop_trailing_sep();
assert!(!p.has_trailing_sep());
assert_eq!(p.as_os_str(), OsStr::new("dir"));

p = PathBuf::from("/");
assert!(p.has_trailing_sep());
p.pop_trailing_sep();
assert!(p.has_trailing_sep());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1574-1576)

Updates [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name") to `file_name`.

If [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name") was [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), this is equivalent to pushing `file_name`.

Otherwise it is equivalent to calling [`pop`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.pop "method std::path::PathBuf::pop") and then pushing `file_name`. The new path will be a sibling of the original path. (That is, it will have the same parent.)

The argument is not sanitized, so can include separators. This behavior may be changed to a panic in the future.

##### [§](#examples-9)Examples

```rust
use std::path::PathBuf;

let mut buf = PathBuf::from("/");
assert!(buf.file_name() == None);

buf.set_file_name("foo.txt");
assert!(buf == PathBuf::from("/foo.txt"));
assert!(buf.file_name().is_some());

buf.set_file_name("bar.txt");
assert!(buf == PathBuf::from("/bar.txt"));

buf.set_file_name("baz");
assert!(buf == PathBuf::from("/baz"));

buf.set_file_name("../b/c.txt");
assert!(buf == PathBuf::from("/../b/c.txt"));

buf.set_file_name("baz");
assert!(buf == PathBuf::from("/../b/baz"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1643-1645)

Updates [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension") to `Some(extension)` or to `None` if `extension` is empty.

Returns `false` and does nothing if [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name") is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), returns `true` and updates the extension otherwise.

If [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension") is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), the extension is added; otherwise it is replaced.

If `extension` is the empty string, [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension") will be [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") afterwards, not `Some("")`.

##### [§](#panics)Panics

Panics if the passed extension contains a path separator (see [`is_separator`](https://doc.rust-lang.org/stable/std/path/fn.is_separator.html "fn std::path::is_separator")).

##### [§](#caveats)Caveats

The new `extension` may contain dots and will be used in its entirety, but only the part after the final dot will be reflected in [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension").

If the file stem contains internal dots and `extension` is empty, part of the old file stem will be considered the new [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension").

See the examples below.

##### [§](#examples-10)Examples

```rust
use std::path::{Path, PathBuf};

let mut p = PathBuf::from("/feel/the");

p.set_extension("force");
assert_eq!(Path::new("/feel/the.force"), p.as_path());

p.set_extension("dark.side");
assert_eq!(Path::new("/feel/the.dark.side"), p.as_path());

p.set_extension("cookie");
assert_eq!(Path::new("/feel/the.dark.cookie"), p.as_path());

p.set_extension("");
assert_eq!(Path::new("/feel/the.dark"), p.as_path());

p.set_extension("");
assert_eq!(Path::new("/feel/the"), p.as_path());

p.set_extension("");
assert_eq!(Path::new("/feel/the"), p.as_path());
```

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1717-1719)

Append [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension") with `extension`.

Returns `false` and does nothing if [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name") is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), returns `true` and updates the extension otherwise.

##### [§](#panics-1)Panics

Panics if the passed extension contains a path separator (see [`is_separator`](https://doc.rust-lang.org/stable/std/path/fn.is_separator.html "fn std::path::is_separator")).

##### [§](#caveats-1)Caveats

The appended `extension` may contain dots and will be used in its entirety, but only the part after the final dot will be reflected in [`self.extension`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.extension "method std::path::Path::extension").

See the examples below.

##### [§](#examples-11)Examples

```rust
use std::path::{Path, PathBuf};

let mut p = PathBuf::from("/feel/the");

p.add_extension("formatted");
assert_eq!(Path::new("/feel/the.formatted"), p.as_path());

p.add_extension("dark.side");
assert_eq!(Path::new("/feel/the.formatted.dark.side"), p.as_path());

p.set_extension("cookie");
assert_eq!(Path::new("/feel/the.formatted.dark.cookie"), p.as_path());

p.set_extension("");
assert_eq!(Path::new("/feel/the.formatted.dark"), p.as_path());

p.add_extension("");
assert_eq!(Path::new("/feel/the.formatted.dark"), p.as_path());
```

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1767-1769)

Yields a mutable reference to the underlying [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString") instance.

##### [§](#examples-12)Examples

```rust
use std::path::{Path, PathBuf};

let mut path = PathBuf::from("/foo");

path.push("bar");
assert_eq!(path, Path::new("/foo/bar"));

// OsString's `push` does not add a separator.
path.as_mut_os_string().push("baz");
assert_eq!(path, Path::new("/foo/barbaz"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1784-1786)

Consumes the `PathBuf`, yielding its internal [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString") storage.

##### [§](#examples-13)Examples

```rust
use std::path::PathBuf;

let p = PathBuf::from("/the/head");
let os_str = p.into_os_string();
```

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1792-1795)

Converts this `PathBuf` into a [boxed](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html "struct std::boxed::Box") [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path").

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1803-1805)

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1812-1814)

Invokes [`clear`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html#method.clear "method std::ffi::OsString::clear") on the underlying instance of [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString").

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1821-1823)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1830-1832)

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1839-1841)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1848-1850)

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1857-1859)

1.56.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1866-1868)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2407-2409)

Yields the underlying [`OsStr`](https://doc.rust-lang.org/stable/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") slice.

##### [§](#examples-14)Examples

```rust
use std::path::Path;

let os_str = Path::new("foo.txt").as_os_str();
assert_eq!(os_str, std::ffi::OsStr::new("foo.txt"));
```

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2428-2430)

Yields a mutable reference to the underlying [`OsStr`](https://doc.rust-lang.org/stable/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") slice.

##### [§](#examples-15)Examples

```rust
use std::path::{Path, PathBuf};

let mut path = PathBuf::from("Foo.TXT");

assert_ne!(path, Path::new("foo.txt"));

path.as_mut_os_str().make_ascii_lowercase();
assert_eq!(path, Path::new("foo.txt"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2452-2454)

Yields a [`&str`](https://doc.rust-lang.org/stable/std/primitive.str.html "primitive str") slice if the `Path` is valid unicode.

This conversion may entail doing a check for UTF-8 validity. Note that validation is performed because non-UTF-8 strings are perfectly valid for some OS.

##### [§](#examples-16)Examples

```rust
use std::path::Path;

let path = Path::new("foo.txt");
assert_eq!(path.to_str(), Some("foo.txt"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2480-2482)

Converts a `Path` to a [`Cow<str>`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow").

Any non-UTF-8 sequences are replaced with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/stable/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

##### [§](#examples-17)Examples

Calling `to_string_lossy` on a `Path` with valid unicode:

```rust
use std::path::Path;

let path = Path::new("foo.txt");
assert_eq!(path.to_string_lossy(), "foo.txt");
```

Had `path` contained invalid unicode, the `to_string_lossy` call might have returned `"fo�.txt"`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2499-2501)

Converts a `Path` to an owned [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf").

##### [§](#examples-18)Examples

```rust
use std::path::{Path, PathBuf};

let path_buf = Path::new("foo.txt").to_path_buf();
assert_eq!(path_buf, PathBuf::from("foo.txt"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2524-2526)

Returns `true` if the `Path` is absolute, i.e., if it is independent of the current directory.

- On Unix, a path is absolute if it starts with the root, so `is_absolute` and [`has_root`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.has_root "method std::path::Path::has_root") are equivalent.
- On Windows, a path is absolute if it has a prefix and starts with the root: `c:\windows` is absolute, while `c:temp` and `\temp` are not.

##### [§](#examples-19)Examples

```rust
use std::path::Path;

assert!(!Path::new("foo.txt").is_absolute());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2544-2546)

Returns `true` if the `Path` is relative, i.e., not absolute.

See [`is_absolute`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.is_absolute "method std::path::Path::is_absolute")’s documentation for more details.

##### [§](#examples-20)Examples

```rust
use std::path::Path;

assert!(Path::new("foo.txt").is_relative());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2571-2573)

Returns `true` if the `Path` has a root.

- On Unix, a path has a root if it begins with `/`.
- On Windows, a path has a root if it:
  
  - has no prefix and begins with a separator, e.g., `\windows`
  - has a prefix followed by a separator, e.g., `c:\windows` but not `c:windows`
  - has any non-disk prefix, e.g., `\\server\share`

##### [§](#examples-21)Examples

```rust
use std::path::Path;

assert!(Path::new("/etc/passwd").has_root());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2606-2615)

Returns the `Path` without its final component, if there is one.

This means it returns `Some("")` for relative paths with one component.

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the path terminates in a root or prefix, or if it’s the empty string.

##### [§](#examples-22)Examples

```rust
use std::path::Path;

let path = Path::new("/foo/bar");
let parent = path.parent().unwrap();
assert_eq!(parent, Path::new("/foo"));

let grand_parent = parent.parent().unwrap();
assert_eq!(grand_parent, Path::new("/"));
assert_eq!(grand_parent.parent(), None);

let relative_path = Path::new("foo/bar");
let parent = relative_path.parent();
assert_eq!(parent, Some(Path::new("foo")));
let grand_parent = parent.and_then(Path::parent);
assert_eq!(grand_parent, Some(Path::new("")));
let great_grand_parent = grand_parent.and_then(Path::parent);
assert_eq!(great_grand_parent, None);
```

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2646-2648)

Produces an iterator over `Path` and its ancestors.

The iterator will yield the `Path` that is returned if the [`parent`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.parent "method std::path::Path::parent") method is used zero or more times. If the [`parent`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.parent "method std::path::Path::parent") method returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), the iterator will do likewise. The iterator will always yield at least one value, namely `Some(&self)`. Next it will yield `&self.parent()`, `&self.parent().and_then(Path::parent)` and so on.

##### [§](#examples-23)Examples

```rust
use std::path::Path;

let mut ancestors = Path::new("/foo/bar").ancestors();
assert_eq!(ancestors.next(), Some(Path::new("/foo/bar")));
assert_eq!(ancestors.next(), Some(Path::new("/foo")));
assert_eq!(ancestors.next(), Some(Path::new("/")));
assert_eq!(ancestors.next(), None);

let mut ancestors = Path::new("../foo/bar").ancestors();
assert_eq!(ancestors.next(), Some(Path::new("../foo/bar")));
assert_eq!(ancestors.next(), Some(Path::new("../foo")));
assert_eq!(ancestors.next(), Some(Path::new("..")));
assert_eq!(ancestors.next(), Some(Path::new("")));
assert_eq!(ancestors.next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2673-2678)

Returns the final component of the `Path`, if there is one.

If the path is a normal file, this is the file name. If it’s the path of a directory, this is the directory name.

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the path terminates in `..`.

##### [§](#examples-24)Examples

```rust
use std::path::Path;
use std::ffi::OsStr;

assert_eq!(Some(OsStr::new("bin")), Path::new("/usr/bin/").file_name());
assert_eq!(Some(OsStr::new("foo.txt")), Path::new("tmp/foo.txt").file_name());
assert_eq!(Some(OsStr::new("foo.txt")), Path::new("foo.txt/.").file_name());
assert_eq!(Some(OsStr::new("foo.txt")), Path::new("foo.txt/.//").file_name());
assert_eq!(None, Path::new("foo.txt/..").file_name());
assert_eq!(None, Path::new("/").file_name());
```

1.7.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2710-2715)

Returns a path that, when joined onto `base`, yields `self`.

##### [§](#errors)Errors

If `base` is not a prefix of `self` (i.e., [`starts_with`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.starts_with "method std::path::Path::starts_with") returns `false`), returns [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err").

##### [§](#examples-25)Examples

```rust
use std::path::{Path, PathBuf};

let path = Path::new("/test/haha/foo.txt");

assert_eq!(path.strip_prefix("/"), Ok(Path::new("test/haha/foo.txt")));
assert_eq!(path.strip_prefix("/test"), Ok(Path::new("haha/foo.txt")));
assert_eq!(path.strip_prefix("/test/"), Ok(Path::new("haha/foo.txt")));
assert_eq!(path.strip_prefix("/test/haha/foo.txt"), Ok(Path::new("")));
assert_eq!(path.strip_prefix("/test/haha/foo.txt/"), Ok(Path::new("")));

assert!(path.strip_prefix("test").is_err());
assert!(path.strip_prefix("/te").is_err());
assert!(path.strip_prefix("/haha").is_err());

let prefix = PathBuf::from("/test/");
assert_eq!(path.strip_prefix(prefix), Ok(Path::new("haha/foo.txt")));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2747-2749)

Determines whether `base` is a prefix of `self`.

Only considers whole path components to match.

##### [§](#examples-26)Examples

```rust
use std::path::Path;

let path = Path::new("/etc/passwd");

assert!(path.starts_with("/etc"));
assert!(path.starts_with("/etc/"));
assert!(path.starts_with("/etc/passwd"));
assert!(path.starts_with("/etc/passwd/")); // extra slash is okay
assert!(path.starts_with("/etc/passwd///")); // multiple extra slashes are okay

assert!(!path.starts_with("/e"));
assert!(!path.starts_with("/etc/passwd.txt"));

assert!(!Path::new("/etc/foo.rs").starts_with("/etc/foo"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2775-2777)

Determines whether `child` is a suffix of `self`.

Only considers whole path components to match.

##### [§](#examples-27)Examples

```rust
use std::path::Path;

let path = Path::new("/etc/resolv.conf");

assert!(path.ends_with("resolv.conf"));
assert!(path.ends_with("etc/resolv.conf"));
assert!(path.ends_with("/etc/resolv.conf"));

assert!(!path.ends_with("/resolv.conf"));
assert!(!path.ends_with("conf")); // use .extension() instead
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2801-2803)

🔬This is a nightly-only experimental API. (`path_is_empty` [#148494](https://github.com/rust-lang/rust/issues/148494))

Checks whether the `Path` is empty.

##### [§](#examples-28)Examples

```rust
#![feature(path_is_empty)]
use std::path::Path;

let path = Path::new("");
assert!(path.is_empty());

let path = Path::new("foo");
assert!(!path.is_empty());

let path = Path::new(".");
assert!(!path.is_empty());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2833-2835)

Extracts the stem (non-extension) portion of [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name").

The stem is:

- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), if there is no file name;
- The entire file name if there is no embedded `.`;
- The entire file name if the file name begins with `.` and has no other `.`s within;
- Otherwise, the portion of the file name before the final `.`

##### [§](#examples-29)Examples

```rust
use std::path::Path;

assert_eq!("foo", Path::new("foo.rs").file_stem().unwrap());
assert_eq!("foo.tar", Path::new("foo.tar.gz").file_stem().unwrap());
```

##### [§](#see-also)See Also

This method is similar to [`Path::file_prefix`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_prefix "method std::path::Path::file_prefix"), which extracts the portion of the file name before the *first* `.`

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2868-2870)

Extracts the prefix of [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name").

The prefix is:

- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), if there is no file name;
- The entire file name if there is no embedded `.`;
- The portion of the file name before the first non-beginning `.`;
- The entire file name if the file name begins with `.` and has no other `.`s within;
- The portion of the file name before the second `.` if the file name begins with `.`

##### [§](#examples-30)Examples

```rust
use std::path::Path;

assert_eq!("foo", Path::new("foo.rs").file_prefix().unwrap());
assert_eq!("foo", Path::new("foo.tar.gz").file_prefix().unwrap());
assert_eq!(".config", Path::new(".config").file_prefix().unwrap());
assert_eq!(".config", Path::new(".config.toml").file_prefix().unwrap());
```

##### [§](#see-also-1)See Also

This method is similar to [`Path::file_stem`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_stem "method std::path::Path::file_stem"), which extracts the portion of the file name before the *last* `.`

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2893-2895)

Extracts the extension (without the leading dot) of [`self.file_name`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.file_name "method std::path::Path::file_name"), if possible.

The extension is:

- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), if there is no file name;
- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), if there is no embedded `.`;
- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), if the file name begins with `.` and has no other `.`s within;
- Otherwise, the portion of the file name after the final `.`

##### [§](#examples-31)Examples

```rust
use std::path::Path;

assert_eq!("rs", Path::new("foo.rs").extension().unwrap());
assert_eq!("gz", Path::new("foo.tar.gz").extension().unwrap());
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2918-2920)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Checks whether the path ends in a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR").

This is generally done to ensure that a path is treated as a directory, not a file, although it does not actually guarantee that such a path is a directory on the underlying file system.

Despite this behavior, two paths are still considered the same in Rust whether they have a trailing separator or not.

##### [§](#examples-32)Examples

```rust
#![feature(path_trailing_sep)]
use std::path::Path;

assert!(Path::new("dir/").has_trailing_sep());
assert!(!Path::new("file.rs").has_trailing_sep());
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2942-2944)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Ensures that a path has a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR"), allocating a [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") if necessary.

The resulting path will return true for [`has_trailing_sep`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.has_trailing_sep "method std::path::Path::has_trailing_sep").

##### [§](#examples-33)Examples

```rust
#![feature(path_trailing_sep)]
use std::ffi::OsStr;
use std::path::Path;

assert_eq!(Path::new("dir//").with_trailing_sep().as_os_str(), OsStr::new("dir//"));
assert_eq!(Path::new("dir/").with_trailing_sep().as_os_str(), OsStr::new("dir/"));
assert!(!Path::new("dir").has_trailing_sep());
assert!(Path::new("dir").with_trailing_sep().has_trailing_sep());
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2969-2983)

🔬This is a nightly-only experimental API. (`path_trailing_sep` [#142503](https://github.com/rust-lang/rust/issues/142503))

Trims a trailing [separator](https://doc.rust-lang.org/stable/std/path/constant.MAIN_SEPARATOR.html "constant std::path::MAIN_SEPARATOR") from a path, if possible.

The resulting path will return false for [`has_trailing_sep`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.has_trailing_sep "method std::path::Path::has_trailing_sep") for most paths.

Some paths, like `/`, cannot be trimmed in this way.

##### [§](#examples-34)Examples

```rust
#![feature(path_trailing_sep)]
use std::ffi::OsStr;
use std::path::Path;

assert_eq!(Path::new("dir//").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
assert_eq!(Path::new("dir/").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
assert_eq!(Path::new("dir").trim_trailing_sep().as_os_str(), OsStr::new("dir"));
assert_eq!(Path::new("/").trim_trailing_sep().as_os_str(), OsStr::new("/"));
assert_eq!(Path::new("//").trim_trailing_sep().as_os_str(), OsStr::new("//"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3010-3012)

Creates an owned [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") with `path` adjoined to `self`.

If `path` is absolute, it replaces the current path.

On Windows:

- if `path` has a root but no prefix (e.g., `\windows`), it replaces and returns everything except for the prefix (if any) of `self`.
- if `path` has a prefix but no root, `self` is ignored and `path` is returned.
- if `self` has a verbatim prefix (e.g. `\\?\C:\windows`) and `path` is not empty, the new path is normalized: all references to `.` and `..` are removed.

See [`PathBuf::push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") for more details on what it means to adjoin a path.

##### [§](#examples-35)Examples

```rust
use std::path::{Path, PathBuf};

assert_eq!(Path::new("/etc").join("passwd"), PathBuf::from("/etc/passwd"));
assert_eq!(Path::new("/etc").join("/bin/sh"), PathBuf::from("/bin/sh"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3038-3040)

Creates an owned [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") like `self` but with the given file name.

See [`PathBuf::set_file_name`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.set_file_name "method std::path::PathBuf::set_file_name") for more details.

##### [§](#examples-36)Examples

```rust
use std::path::{Path, PathBuf};

let path = Path::new("/tmp/foo.png");
assert_eq!(path.with_file_name("bar"), PathBuf::from("/tmp/bar"));
assert_eq!(path.with_file_name("bar.txt"), PathBuf::from("/tmp/bar.txt"));

let path = Path::new("/tmp");
assert_eq!(path.with_file_name("var"), PathBuf::from("/var"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3081-3083)

Creates an owned [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") like `self` but with the given extension.

See [`PathBuf::set_extension`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.set_extension "method std::path::PathBuf::set_extension") for more details.

##### [§](#examples-37)Examples

```rust
use std::path::Path;

let path = Path::new("foo.rs");
assert_eq!(path.with_extension("txt"), Path::new("foo.txt"));
assert_eq!(path.with_extension(""), Path::new("foo"));
```

Handling multiple extensions:

```rust
use std::path::Path;

let path = Path::new("foo.tar.gz");
assert_eq!(path.with_extension("xz"), Path::new("foo.tar.xz"));
assert_eq!(path.with_extension("").with_extension("txt"), Path::new("foo.txt"));
```

Adding an extension where one did not exist:

```rust
use std::path::Path;

let path = Path::new("foo");
assert_eq!(path.with_extension("rs"), Path::new("foo.rs"));
```

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3128-3132)

Creates an owned [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") like `self` but with the extension added.

See [`PathBuf::add_extension`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.add_extension "method std::path::PathBuf::add_extension") for more details.

##### [§](#examples-38)Examples

```rust
use std::path::{Path, PathBuf};

let path = Path::new("foo.rs");
assert_eq!(path.with_added_extension("txt"), PathBuf::from("foo.rs.txt"));

let path = Path::new("foo.tar.gz");
assert_eq!(path.with_added_extension(""), PathBuf::from("foo.tar.gz"));
assert_eq!(path.with_added_extension("xz"), PathBuf::from("foo.tar.gz.xz"));
assert_eq!(path.with_added_extension("").with_added_extension("txt"), PathBuf::from("foo.tar.gz.txt"));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3168-3179)

Produces an iterator over the [`Component`](https://doc.rust-lang.org/stable/std/path/enum.Component.html "enum std::path::Component")s of the path.

When parsing the path, there is a small amount of normalization:

- Repeated separators are ignored, so `a/b` and `a//b` both have `a` and `b` as components.
- Occurrences of `.` are normalized away, except if they are at the beginning of the path. For example, `a/./b`, `a/b/`, `a/b/.` and `a/b` all have `a` and `b` as components, but `./a/b` starts with an additional [`CurDir`](https://doc.rust-lang.org/stable/std/path/enum.Component.html#variant.CurDir "variant std::path::Component::CurDir") component.
- Trailing separators are normalized away, so `/a/b` and `/a/b/` are equivalent.

Note that no other normalization takes place; in particular, `a/c` and `a/b/../c` are distinct, to account for the possibility that `b` is a symbolic link (so its parent isn’t `a`).

##### [§](#examples-39)Examples

```rust
use std::path::{Path, Component};
use std::ffi::OsStr;

let mut components = Path::new("/tmp/foo.txt").components();

assert_eq!(components.next(), Some(Component::RootDir));
assert_eq!(components.next(), Some(Component::Normal(OsStr::new("tmp"))));
assert_eq!(components.next(), Some(Component::Normal(OsStr::new("foo.txt"))));
assert_eq!(components.next(), None)
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3203-3205)

Produces an iterator over the path’s components viewed as [`OsStr`](https://doc.rust-lang.org/stable/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") slices.

For more information about the particulars of how the path is separated into components, see [`components`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.components "method std::path::Path::components").

##### [§](#examples-40)Examples

```rust
use std::path::{self, Path};
use std::ffi::OsStr;

let mut it = Path::new("/tmp/foo.txt").iter();
assert_eq!(it.next(), Some(OsStr::new(&path::MAIN_SEPARATOR.to_string())));
assert_eq!(it.next(), Some(OsStr::new("tmp")));
assert_eq!(it.next(), Some(OsStr::new("foo.txt")));
assert_eq!(it.next(), None)
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3228-3230)

Returns an object that implements [`Display`](https://doc.rust-lang.org/stable/std/fmt/trait.Display.html "trait std::fmt::Display") for safely printing paths that may contain non-Unicode data. This may perform lossy conversion, depending on the platform. If you would like an implementation which escapes the path please use [`Debug`](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html "trait std::fmt::Debug") instead.

##### [§](#examples-41)Examples

```rust
use std::path::Path;

let path = Path::new("/tmp/foo.rs");

println!("{}", path.display());
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3239-3241)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same path as `&Path`.

This method is redundant when used directly on `&Path`, but it helps dereferencing other `PathBuf`-like types to `Path`s, for example references to `Box<Path>` or `Arc<Path>`.

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3261-3263)

Queries the file system to get information about a file, directory, etc.

This function will traverse symbolic links to query information about the destination file.

This is an alias to [`fs::metadata`](https://doc.rust-lang.org/stable/std/fs/fn.metadata.html "fn std::fs::metadata").

##### [§](#examples-42)Examples

```rust
use std::path::Path;

let path = Path::new("/Minas/tirith");
let metadata = path.metadata().expect("metadata call failed");
println!("{:?}", metadata.file_type());
```

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3280-3282)

Queries the metadata about a file without following symlinks.

This is an alias to [`fs::symlink_metadata`](https://doc.rust-lang.org/stable/std/fs/fn.symlink_metadata.html "fn std::fs::symlink_metadata").

##### [§](#examples-43)Examples

```rust
use std::path::Path;

let path = Path::new("/Minas/tirith");
let metadata = path.symlink_metadata().expect("symlink_metadata call failed");
println!("{:?}", metadata.file_type());
```

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3307-3309)

Returns the canonical, absolute form of the path with all intermediate components normalized and symbolic links resolved.

This is an alias to [`fs::canonicalize`](https://doc.rust-lang.org/stable/std/fs/fn.canonicalize.html "fn std::fs::canonicalize").

##### [§](#errors-1)Errors

This method will return an error in the following situations, but is not limited to just these cases:

- `path` does not exist.
- A non-final component in path is not a directory.

##### [§](#examples-44)Examples

```rust
use std::path::{Path, PathBuf};

let path = Path::new("/foo/test/../test/bar.rs");
assert_eq!(path.canonicalize().unwrap(), PathBuf::from("/foo/test/bar.rs"));
```

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3326-3370)

🔬This is a nightly-only experimental API. (`normalize_lexically` [#134694](https://github.com/rust-lang/rust/issues/134694))

Normalize a path, including `..` without traversing the filesystem.

Returns an error if normalization would leave leading `..` components.

This function always resolves `..` to the “lexical” parent. That is “a/b/../c” will always resolve to `a/c` which can change the meaning of the path. In particular, `a/c` and `a/b/../c` are distinct on many systems because `b` may be a symbolic link, so its parent isn’t `a`.

[`path::absolute`](https://doc.rust-lang.org/stable/std/path/fn.absolute.html "fn std::path::absolute") is an alternative that preserves `..`. Or [`Path::canonicalize`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.canonicalize "method std::path::Path::canonicalize") can be used to resolve any `..` by querying the filesystem.

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3386-3388)

Reads a symbolic link, returning the file that the link points to.

This is an alias to [`fs::read_link`](https://doc.rust-lang.org/stable/std/fs/fn.read_link.html "fn std::fs::read_link").

##### [§](#examples-45)Examples

```rust
use std::path::Path;

let path = Path::new("/laputa/sky_castle.rs");
let path_link = path.read_link().expect("read_link call failed");
```

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3411-3413)

Returns an iterator over the entries within a directory.

The iterator will yield instances of `io::Result<fs::DirEntry>`. New errors may be encountered after an iterator is initially constructed.

This is an alias to [`fs::read_dir`](https://doc.rust-lang.org/stable/std/fs/fn.read_dir.html "fn std::fs::read_dir").

##### [§](#examples-46)Examples

```rust
use std::path::Path;

let path = Path::new("/laputa");
for entry in path.read_dir().expect("read_dir call failed") {
    if let Ok(entry) = entry {
        println!("{:?}", entry.path());
    }
}
```

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3443-3445)

Returns `true` if the path points at an existing entity.

Warning: this method may be error-prone, consider using [`try_exists()`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.try_exists "method std::path::Path::try_exists") instead! It also has a risk of introducing time-of-check to time-of-use ([TOCTOU](https://doc.rust-lang.org/stable/std/fs/index.html#time-of-check-to-time-of-use-toctou "mod std::fs")) bugs.

This function will traverse symbolic links to query information about the destination file.

If you cannot access the metadata of the file, e.g. because of a permission error or broken symbolic links, this will return `false`.

##### [§](#examples-47)Examples

```rust
use std::path::Path;
assert!(!Path::new("does_not_exist.txt").exists());
```

##### [§](#see-also-2)See Also

This is a convenience function that coerces errors to false. If you want to check errors, call [`Path::try_exists`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.try_exists "method std::path::Path::try_exists").

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3476-3478)

Returns `Ok(true)` if the path points at an existing entity.

This function will traverse symbolic links to query information about the destination file. In case of broken symbolic links this will return `Ok(false)`.

[`Path::exists()`](https://doc.rust-lang.org/stable/std/path/struct.Path.html#method.exists "method std::path::Path::exists") only checks whether or not a path was both found and readable. By contrast, `try_exists` will return `Ok(true)` or `Ok(false)`, respectively, if the path was *verified* to exist or not exist. If its existence can neither be confirmed nor denied, it will propagate an `Err(_)` instead. This can be the case if e.g. listing permission is denied on one of the parent directories.

Note that while this avoids some pitfalls of the `exists()` method, it still can not prevent time-of-check to time-of-use ([TOCTOU](https://doc.rust-lang.org/stable/std/fs/index.html#time-of-check-to-time-of-use-toctou "mod std::fs")) bugs. You should only use it in scenarios where those bugs are not an issue.

This is an alias for [`std::fs::exists`](https://doc.rust-lang.org/stable/std/fs/fn.exists.html "fn std::fs::exists").

##### [§](#examples-48)Examples

```rust
use std::path::Path;
assert!(!Path::new("does_not_exist.txt").try_exists().expect("Can't check existence of file does_not_exist.txt"));
assert!(Path::new("/root/secret_file.txt").try_exists().is_err());
```

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3509-3511)

Returns `true` if the path exists on disk and is pointing at a regular file.

This function will traverse symbolic links to query information about the destination file.

If you cannot access the metadata of the file, e.g. because of a permission error or broken symbolic links, this will return `false`.

##### [§](#examples-49)Examples

```rust
use std::path::Path;
assert_eq!(Path::new("./is_a_directory/").is_file(), false);
assert_eq!(Path::new("a_file.txt").is_file(), true);
```

##### [§](#see-also-3)See Also

This is a convenience function that coerces errors to false. If you want to check errors, call [`fs::metadata`](https://doc.rust-lang.org/stable/std/fs/fn.metadata.html "fn std::fs::metadata") and handle its [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result"). Then call [`fs::Metadata::is_file`](https://doc.rust-lang.org/stable/std/fs/struct.Metadata.html#method.is_file "method std::fs::Metadata::is_file") if it was [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok").

When the goal is simply to read from (or write to) the source, the most reliable way to test the source can be read (or written to) is to open it. Only using `is_file` can break workflows like `diff <( prog_a )` on a Unix-like system for example. See [`fs::File::open`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.open "associated function std::fs::File::open") or [`fs::OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") for more information.

1.5.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3536-3538)

Returns `true` if the path exists on disk and is pointing at a directory.

This function will traverse symbolic links to query information about the destination file.

If you cannot access the metadata of the file, e.g. because of a permission error or broken symbolic links, this will return `false`.

##### [§](#examples-50)Examples

```rust
use std::path::Path;
assert_eq!(Path::new("./is_a_directory/").is_dir(), true);
assert_eq!(Path::new("a_file.txt").is_dir(), false);
```

##### [§](#see-also-4)See Also

This is a convenience function that coerces errors to false. If you want to check errors, call [`fs::metadata`](https://doc.rust-lang.org/stable/std/fs/fn.metadata.html "fn std::fs::metadata") and handle its [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result"). Then call [`fs::Metadata::is_dir`](https://doc.rust-lang.org/stable/std/fs/struct.Metadata.html#method.is_dir "method std::fs::Metadata::is_dir") if it was [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok").

1.58.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3569-3571)

Returns `true` if the path exists on disk and is pointing at a symbolic link.

This function will not traverse symbolic links. In case of a broken symbolic link this will also return true.

If you cannot access the directory containing the file, e.g., because of a permission error, this will return false.

##### [§](#examples-51)Examples

```rust
use std::path::Path;
use std::os::unix::fs::symlink;

let link_path = Path::new("link");
symlink("/origin_does_not_exist/", link_path).unwrap();
assert_eq!(link_path.is_symlink(), true);
assert_eq!(link_path.exists(), false);
```

##### [§](#see-also-5)See Also

This is a convenience function that coerces errors to false. If you want to check errors, call [`fs::symlink_metadata`](https://doc.rust-lang.org/stable/std/fs/fn.symlink_metadata.html "fn std::fs::symlink_metadata") and handle its [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result"). Then call [`fs::Metadata::is_symlink`](https://doc.rust-lang.org/stable/std/fs/struct.Metadata.html#method.is_symlink "method std::fs::Metadata::is_symlink") if it was [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok").

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2282-2287)[§](#impl-AsRef%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2284-2286)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3816-3821)[§](#impl-AsRef%3CPath%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3818-3820)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2080-2085)[§](#impl-Borrow%3CPath%3E-for-PathBuf)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1872-1886)[§](#impl-Clone-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1883-1885)[§](#method.clone_from)

Clones the contents of `source` into `self`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1874-1876)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2056-2060)[§](#impl-Debug-for-PathBuf)

1.17.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2088-2093)[§](#impl-Default-for-PathBuf)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2063-2069)[§](#impl-Deref-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2064)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2066-2068)[§](#method.deref)

Dereferences the value.

1.68.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2072-2077)[§](#impl-DerefMut-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2074-2076)[§](#method.deref_mut)

Mutably dereferences the value.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2030-2053)[§](#impl-Extend%3CP%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2045-2047)[§](#method.extend)

Extends `self` with [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path") elements from `iter`.

This uses [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") to add each element, so can be used to adjoin multiple path [components](https://doc.rust-lang.org/stable/std/path/struct.Components.html "struct std::path::Components").

##### [§](#examples-53)Examples

```rust
let mut path = PathBuf::from("/tmp");
path.extend(["foo", "bar", "file.txt"]);
assert_eq!(path, PathBuf::from("/tmp/foo/bar/file.txt"));
```

See documentation for [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") for more details on how the path is constructed.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2050-2052)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#method.extend_reserve)

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2120-2129)[§](#impl-From%3C%26PathBuf%3E-for-Cow%3C'a,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2126-2128)[§](#method.from-7)

Creates a clone-on-write pointer from a reference to [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf").

This conversion does not clone or allocate.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1954-1962)[§](#impl-From%3C%26T%3E-for-PathBuf)

1.18.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1923-1931)[§](#impl-From%3CBox%3CPath%3E%3E-for-PathBuf)

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2132-2140)[§](#impl-From%3CCow%3C'a,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2137-2139)[§](#method.from-8)

Converts a clone-on-write pointer to an owned path.

Converting from a `Cow::Owned` does not clone or allocate.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1965-1973)[§](#impl-From%3COsString%3E-for-PathBuf)

1.24.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2143-2151)[§](#impl-From%3CPathBuf%3E-for-Arc%3CPath%3E)

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1934-1943)[§](#impl-From%3CPathBuf%3E-for-Box%3CPath%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1940-1942)[§](#method.from-1)

Converts a [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf") into a `Box<Path>`.

This conversion currently should not allocate memory, but this behavior is not guaranteed on all platforms or in all future versions.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2108-2117)[§](#impl-From%3CPathBuf%3E-for-Cow%3C'a,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2114-2116)[§](#method.from-6)

Creates a clone-on-write pointer from an owned instance of [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf").

This conversion does not clone or allocate.

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1976-1984)[§](#impl-From%3CPathBuf%3E-for-OsString)

1.24.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2173-2181)[§](#impl-From%3CPathBuf%3E-for-Rc%3CPath%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1987-1995)[§](#impl-From%3CString%3E-for-PathBuf)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2008-2027)[§](#impl-FromIterator%3CP%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2022-2026)[§](#method.from_iter)

Creates a new `PathBuf` from the [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path") elements of an iterator.

This uses [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") to add each element, so can be used to adjoin multiple path [components](https://doc.rust-lang.org/stable/std/path/struct.Components.html "struct std::path::Components").

##### [§](#examples-52)Examples

```rust
let path = PathBuf::from_iter(["/tmp", "foo", "bar"]);
assert_eq!(path, PathBuf::from("/tmp/foo/bar"));
```

See documentation for [`push`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.push "method std::path::PathBuf::push") for more details on how the path is constructed.

1.32.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1998-2005)[§](#impl-FromStr-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1999)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2002-2004)[§](#method.from_str)

Parses a string `s` to return a value of this type. [Read more](https://doc.rust-lang.org/stable/std/str/trait.FromStr.html#tymethod.from_str)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2256-2260)[§](#impl-Hash-for-PathBuf)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3824-3831)[§](#impl-IntoIterator-for-%26PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3825)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3826)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3828-3830)[§](#method.into_iter)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2274-2279)[§](#impl-Ord-for-PathBuf)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#impl-PartialEq%3C%26OsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#impl-PartialEq%3C%26Path%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#impl-PartialEq%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#impl-PartialEq%3COsString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#impl-PartialEq%3CPath%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#impl-PartialEq%3CPathBuf%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#impl-PartialEq%3CPathBuf%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialEq%3CPathBuf%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialEq%3CPathBuf%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#impl-PartialEq%3CPathBuf%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#impl-PartialEq%3CPathBuf%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#impl-PartialEq%3CPathBuf%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2248-2253)[§](#impl-PartialEq%3CPathBuf%3E-for-String)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2250-2252)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2232-2237)[§](#impl-PartialEq%3CPathBuf%3E-for-str)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2234-2236)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2240-2245)[§](#impl-PartialEq%3CString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2242-2244)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2224-2229)[§](#impl-PartialEq%3Cstr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2226-2228)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2216-2221)[§](#impl-PartialEq-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2218-2220)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#impl-PartialOrd%3C%26OsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#method.partial_cmp-9)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-9)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-9)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-9)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-9)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#impl-PartialOrd%3C%26Path%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#method.partial_cmp-3)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-3)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-3)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-3)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-3)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.partial_cmp-11)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-11)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-11)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-11)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-11)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.partial_cmp-6)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-6)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-6)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-6)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-6)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#impl-PartialOrd%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#method.partial_cmp-7)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-7)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-7)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-7)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-7)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#impl-PartialOrd%3COsString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#method.partial_cmp-13)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-13)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-13)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-13)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-13)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#impl-PartialOrd%3CPath%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#impl-PartialOrd%3CPathBuf%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3922)[§](#method.partial_cmp-10)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-10)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-10)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-10)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-10)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#impl-PartialOrd%3CPathBuf%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3880)[§](#method.partial_cmp-4)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-4)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-4)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-4)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-4)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialOrd%3CPathBuf%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.partial_cmp-12)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-12)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-12)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-12)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-12)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialOrd%3CPathBuf%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.partial_cmp-5)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-5)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-5)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-5)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-5)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#impl-PartialOrd%3CPathBuf%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3921)[§](#method.partial_cmp-8)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-8)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-8)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-8)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-8)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#impl-PartialOrd%3CPathBuf%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3924)[§](#method.partial_cmp-14)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-14)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-14)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-14)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-14)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#impl-PartialOrd%3CPathBuf%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3879)[§](#method.partial_cmp-2)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-2)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-2)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-2)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-2)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2266-2271)[§](#impl-PartialOrd-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2268-2270)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2263)[§](#impl-Eq-for-PathBuf)

[§](#impl-Freeze-for-PathBuf)

[§](#impl-RefUnwindSafe-for-PathBuf)

[§](#impl-Send-for-PathBuf)

[§](#impl-Sync-for-PathBuf)

[§](#impl-Unpin-for-PathBuf)

[§](#impl-UnsafeUnpin-for-PathBuf)

[§](#impl-UnwindSafe-for-PathBuf)