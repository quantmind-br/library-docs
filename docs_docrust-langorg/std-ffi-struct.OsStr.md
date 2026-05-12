---
title: OsStr in std::ffi - Rust
url: https://doc.rust-lang.org/std/ffi/struct.OsStr.html
source: crawler
fetched_at: 2026-05-06T21:23:07.240979219-03:00
rendered_js: false
word_count: 4891
summary: This document describes the OsStr struct in Rust, which represents a borrowed reference to an operating system-specific string, detailing its conversion methods and interface.
tags:
    - rust
    - ffi
    - string-handling
    - os-str
    - standard-library
    - memory-safety
category: reference
---

## Struct OsStr

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#119-121)

```rust
pub struct OsStr { /* private fields */ }
```

Expand description

Borrowed reference to an OS string (see [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString")).

This type represents a borrowed reference to a string in the operating system’s preferred representation.

`&OsStr` is to [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") as `&str` is to [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"): the former in each pair are borrowed references; the latter are owned strings.

See the [module’s toplevel documentation about conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") for a discussion on the traits which `OsStr` implements for [conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") from/to native representations.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#819-1292)[§](#impl-OsStr)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#832-834)

Coerces into an `OsStr` slice.

##### [§](#examples)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("foo");
```

1.74.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#875-877)

Converts a slice of bytes to an OS string slice without checking that the string contains valid `OsStr`-encoded data.

The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8. By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit ASCII.

See the [module’s toplevel documentation about conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") for safe, cross-platform [conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") from/to native representations.

##### [§](#safety)Safety

As the encoding is unspecified, callers must pass in bytes that originated as a mixture of validated UTF-8 and bytes from [`OsStr::as_encoded_bytes`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.as_encoded_bytes "method std::ffi::OsStr::as_encoded_bytes") from within the same Rust version built for the same target platform. For example, reconstructing an `OsStr` from bytes sent over the network or stored in a file will likely violate these safety rules.

Due to the encoding being self-synchronizing, the bytes from [`OsStr::as_encoded_bytes`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.as_encoded_bytes "method std::ffi::OsStr::as_encoded_bytes") can be split either immediately before or immediately after any valid non-empty UTF-8 substring.

##### [§](#example)Example

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("Mary had a little lamb");
let bytes = os_str.as_encoded_bytes();
let words = bytes.split(|b| *b == b' ');
let words: Vec<&OsStr> = words.map(|word| {
    // SAFETY:
    // - Each `word` only contains content that originated from `OsStr::as_encoded_bytes`
    // - Only split with ASCII whitespace which is a non-empty UTF-8 substring
    unsafe { OsStr::from_encoded_bytes_unchecked(word) }
}).collect();
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#913-915)

Yields a `&str` slice if the `OsStr` is valid Unicode.

This conversion may entail doing a check for UTF-8 validity.

##### [§](#examples-1)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("foo");
assert_eq!(os_str.to_str(), Some("foo"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#966-968)

Converts an `OsStr` to a `Cow<str>`.

Any non-UTF-8 sequences are replaced with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

##### [§](#examples-2)Examples

Calling `to_string_lossy` on an `OsStr` with invalid unicode:

```rust
// Note, due to differences in how Unix and Windows represent strings,
// we are forced to complicate this example, setting up example `OsStr`s
// with different source data and via different platform extensions.
// Understand that in reality you could end up with such example invalid
// sequences simply through collecting user command line arguments, for
// example.

#[cfg(unix)] {
    use std::ffi::OsStr;
    use std::os::unix::ffi::OsStrExt;

    // Here, the values 0x66 and 0x6f correspond to 'f' and 'o'
    // respectively. The value 0x80 is a lone continuation byte, invalid
    // in a UTF-8 sequence.
    let source = [0x66, 0x6f, 0x80, 0x6f];
    let os_str = OsStr::from_bytes(&source[..]);

    assert_eq!(os_str.to_string_lossy(), "fo�o");
}
#[cfg(windows)] {
    use std::ffi::OsString;
    use std::os::windows::prelude::*;

    // Here the values 0x0066 and 0x006f correspond to 'f' and 'o'
    // respectively. The value 0xD800 is a lone surrogate half, invalid
    // in a UTF-16 sequence.
    let source = [0x0066, 0x006f, 0xD800, 0x006f];
    let os_string = OsString::from_wide(&source[..]);
    let os_str = os_string.as_os_str();

    assert_eq!(os_str.to_string_lossy(), "fo�o");
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#986-988)

Copies the slice into an owned [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString").

##### [§](#examples-3)Examples

```rust
use std::ffi::{OsStr, OsString};

let os_str = OsStr::new("foo");
let os_string = os_str.to_os_string();
assert_eq!(os_string, OsString::from("foo"));
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1006-1008)

Checks whether the `OsStr` is empty.

##### [§](#examples-4)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("");
assert!(os_str.is_empty());

let os_str = OsStr::new("foo");
assert!(!os_str.is_empty());
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1040-1042)

Returns the length of this `OsStr`.

Note that this does **not** return the number of bytes in the string in OS string form.

The length returned is that of the underlying storage used by `OsStr`. As discussed in the [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") introduction, [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") and `OsStr` store strings in a form best suited for cheap inter-conversion between native-platform and Rust string forms, which may differ significantly from both of them, including in storage size and encoding.

This number is simply useful for passing to other methods, like [`OsString::with_capacity`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.with_capacity "associated function std::ffi::OsString::with_capacity") to avoid reallocations.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-5)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("");
assert_eq!(os_str.len(), 0);

let os_str = OsStr::new("foo");
assert_eq!(os_str.len(), 3);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1047-1050)

Converts a `Box<OsStr>` into an [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") without copying or allocating.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1068-1070)

Converts an OS string slice to a byte slice. To convert the byte slice back into an OS string slice, use the [`OsStr::from_encoded_bytes_unchecked`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.from_encoded_bytes_unchecked "associated function std::ffi::OsStr::from_encoded_bytes_unchecked") function.

The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8. By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit ASCII.

Note: As the encoding is unspecified, any sub-slice of bytes that is not valid UTF-8 should be treated as opaque and only comparable within the same Rust version built for the same target platform. For example, sending the slice over the network or storing it in a file will likely result in incompatible byte slices. See [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") for more encoding details and [`std::ffi`](https://doc.rust-lang.org/std/ffi/index.html "mod std::ffi") for platform-specific, specified conversions.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1104-1120)

🔬This is a nightly-only experimental API. (`os_str_slice` [#118485](https://github.com/rust-lang/rust/issues/118485))

Takes a substring based on a range that corresponds to the return value of [`OsStr::as_encoded_bytes`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.as_encoded_bytes "method std::ffi::OsStr::as_encoded_bytes").

The range’s start and end must lie on valid `OsStr` boundaries. A valid `OsStr` boundary is one of:

- The start of the string
- The end of the string
- Immediately before a valid non-empty UTF-8 substring
- Immediately after a valid non-empty UTF-8 substring

##### [§](#panics)Panics

Panics if `range` does not lie on valid `OsStr` boundaries or if it exceeds the end of the string.

##### [§](#example-1)Example

```rust
#![feature(os_str_slice)]

use std::ffi::OsStr;

let os_str = OsStr::new("foo=bar");
let bytes = os_str.as_encoded_bytes();
if let Some(index) = bytes.iter().position(|b| *b == b'=') {
    let key = os_str.slice_encoded_bytes(..index);
    let value = os_str.slice_encoded_bytes(index + 1..);
    assert_eq!(key, "foo");
    assert_eq!(value, "bar");
}
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1143-1145)

Converts this string to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`OsStr::to_ascii_lowercase`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.to_ascii_lowercase "method std::ffi::OsStr::to_ascii_lowercase").

##### [§](#examples-6)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::from("GRÜßE, JÜRGEN ❤");

s.make_ascii_lowercase();

assert_eq!("grÜße, jÜrgen ❤", s);
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1168-1170)

Converts this string to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`OsStr::to_ascii_uppercase`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.to_ascii_uppercase "method std::ffi::OsStr::to_ascii_uppercase").

##### [§](#examples-7)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::from("Grüße, Jürgen ❤");

s.make_ascii_uppercase();

assert_eq!("GRüßE, JüRGEN ❤", s);
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1190-1192)

Returns a copy of this string where each character is mapped to its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`OsStr::make_ascii_lowercase`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.make_ascii_lowercase "method std::ffi::OsStr::make_ascii_lowercase").

##### [§](#examples-8)Examples

```rust
use std::ffi::OsString;
let s = OsString::from("Grüße, Jürgen ❤");

assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1212-1214)

Returns a copy of this string where each character is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`OsStr::make_ascii_uppercase`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.make_ascii_uppercase "method std::ffi::OsStr::make_ascii_uppercase").

##### [§](#examples-9)Examples

```rust
use std::ffi::OsString;
let s = OsString::from("Grüße, Jürgen ❤");

assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1234-1236)

Checks if all characters in this string are within the ASCII range.

An empty string returns `true`.

##### [§](#examples-10)Examples

```rust
use std::ffi::OsString;

let ascii = OsString::from("hello!\n");
let non_ascii = OsString::from("Grüße, Jürgen ❤");

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1253-1255)

Checks that two strings are an ASCII case-insensitive match.

Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`, but without allocating and copying temporaries.

##### [§](#examples-11)Examples

```rust
use std::ffi::OsString;

assert!(OsString::from("Ferris").eq_ignore_ascii_case("FERRIS"));
assert!(OsString::from("Ferrös").eq_ignore_ascii_case("FERRöS"));
assert!(!OsString::from("Ferrös").eq_ignore_ascii_case("FERRÖS"));
```

1.87.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1278-1280)

Returns an object that implements [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") for safely printing an [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") that may contain non-Unicode data. This may perform lossy conversion, depending on the platform. If you would like an implementation which escapes the [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") please use [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") instead.

##### [§](#examples-12)Examples

```rust
use std::ffi::OsStr;

let s = OsStr::new("Hello, world!");
println!("{}", s.display());
```

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1289-1291)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&OsStr`.

This method is redundant when used directly on `&OsStr`, but it helps dereferencing other string-like types to string slices, for example references to `Box<OsStr>` or `Arc<OsStr>`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#574-579)[§](#impl-AsRef%3COsStr%3E-for-Component%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#576-578)[§](#method.as_ref-4)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#827-832)[§](#impl-AsRef%3COsStr%3E-for-Components%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#829-831)[§](#method.as_ref-5)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#880-885)[§](#impl-AsRef%3COsStr%3E-for-Iter%3C'_%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#882-884)[§](#method.as_ref-6)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1700-1705)[§](#impl-AsRef%3COsStr%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1702-1704)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1708-1713)[§](#impl-AsRef%3COsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1710-1712)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3596-3601)[§](#impl-AsRef%3COsStr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3598-3600)[§](#method.as_ref-8)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2282-2287)[§](#impl-AsRef%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#2284-2286)[§](#method.as_ref-7)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1724-1729)[§](#impl-AsRef%3COsStr%3E-for-String)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1726-1728)[§](#method.as_ref-3)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1716-1721)[§](#impl-AsRef%3COsStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1718-1720)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3776-3781)[§](#impl-AsRef%3CPath%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3778-3780)[§](#method.as_ref-9)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1678-1683)[§](#impl-Borrow%3COsStr%3E-for-OsString)

1.29.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1345-1350)[§](#impl-Clone-for-Box%3COsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1353-1360)[§](#impl-CloneToUninit-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1356-1359)[§](#method.clone_to_uninit)

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1616-1620)[§](#impl-Debug-for-OsStr)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1487-1493)[§](#impl-Default-for-%26OsStr)

1.17.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1478-1484)[§](#impl-Default-for-Box%3COsStr%3E)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1773-1780)[§](#impl-Extend%3C%26OsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1775-1779)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1374-1381)[§](#impl-From%3C%26OsStr%3E-for-Arc%3COsStr%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1295-1301)[§](#impl-From%3C%26OsStr%3E-for-Box%3COsStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1432-1438)[§](#impl-From%3C%26OsStr%3E-for-Cow%3C'a,+OsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1404-1411)[§](#impl-From%3C%26OsStr%3E-for-Rc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1384-1390)[§](#impl-From%3C%26mut+OsStr%3E-for-Arc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1304-1310)[§](#impl-From%3C%26mut+OsStr%3E-for-Box%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1414-1420)[§](#impl-From%3C%26mut+OsStr%3E-for-Rc%3COsStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1313-1323)[§](#impl-From%3CCow%3C'_,+OsStr%3E%3E-for-Box%3COsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1317-1322)[§](#method.from-2)

Converts a `Cow<'a, OsStr>` into a `Box<OsStr>`, by copying the contents if they are borrowed.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1336-1342)[§](#impl-From%3COsString%3E-for-Box%3COsStr%3E)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1812-1821)[§](#impl-FromIterator%3C%26OsStr%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1608-1613)[§](#impl-Hash-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1661-1675)[§](#impl-Join%3C%26OsStr%3E-for-%5BS%5D)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1662)[§](#associatedtype.Output)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1664-1674)[§](#method.join)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1558-1563)[§](#impl-Ord-for-OsStr)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/ffi/os_str.rs.html#61-70)[§](#impl-OsStrExt-for-OsStr)

Available on **Unix** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/ffi/os_str.rs.html#61-70)[§](#impl-OsStrExt-for-OsStr-1)

Available on **WASI** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/ffi.rs.html#131-136)[§](#impl-OsStrExt-for-OsStr-2)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/src/std/os/windows/ffi.rs.html#133-135)[§](#method.encode_wide)

Re-encodes an `OsStr` as a wide character sequence, i.e., potentially ill-formed UTF-16. [Read more](https://doc.rust-lang.org/std/os/windows/ffi/trait.OsStrExt.html#tymethod.encode_wide)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialEq%3C%26OsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#impl-PartialEq%3C%26OsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#method.eq-23)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-23)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialEq%3C%26OsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#impl-PartialEq%3C%26OsStr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#impl-PartialEq%3C%26OsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#impl-PartialEq%3C%26Path%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#method.eq-20)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-20)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#method.eq-24)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-24)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#method.eq-22)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-22)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#impl-PartialEq%3COsStr%3E-for-%26Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#method.eq-19)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-19)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialEq%3COsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#impl-PartialEq%3COsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#method.eq-21)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-21)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialEq%3COsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#impl-PartialEq%3COsStr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#impl-PartialEq%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1512-1517)[§](#impl-PartialEq%3COsStr%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1514-1516)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialEq%3COsString%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialEq%3COsString%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#impl-PartialEq%3CPath%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#impl-PartialEq%3CPath%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#impl-PartialEq%3CPathBuf%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#impl-PartialEq%3CPathBuf%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1504-1509)[§](#impl-PartialEq%3Cstr%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1506-1508)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1496-1501)[§](#impl-PartialEq-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1498-1500)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialOrd%3C%26OsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#method.partial_cmp-8)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-8)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-8)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-8)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-8)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#impl-PartialOrd%3C%26OsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#method.partial_cmp-22)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-22)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-22)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-22)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-22)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialOrd%3C%26OsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.partial_cmp-4)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-4)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-4)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-4)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-4)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#impl-PartialOrd%3C%26OsStr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#method.partial_cmp-16)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-16)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-16)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-16)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-16)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#impl-PartialOrd%3C%26OsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#method.partial_cmp-12)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-12)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-12)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-12)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-12)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#impl-PartialOrd%3C%26Path%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#method.partial_cmp-19)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-19)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-19)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-19)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-19)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1604)[§](#method.partial_cmp-9)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-9)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-9)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-9)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-9)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#method.partial_cmp-7)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-7)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-7)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-7)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-7)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3933)[§](#method.partial_cmp-23)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-23)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-23)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-23)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-23)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#method.partial_cmp-21)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-21)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-21)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-21)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-21)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#impl-PartialOrd%3COsStr%3E-for-%26Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3929)[§](#method.partial_cmp-18)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-18)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-18)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-18)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-18)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialOrd%3COsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1603)[§](#method.partial_cmp-6)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-6)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-6)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-6)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-6)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#impl-PartialOrd%3COsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3932)[§](#method.partial_cmp-20)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-20)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-20)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-20)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-20)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialOrd%3COsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.partial_cmp-2)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-2)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-2)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-2)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-2)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#impl-PartialOrd%3COsStr%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#method.partial_cmp-14)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-14)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-14)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-14)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-14)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#impl-PartialOrd%3COsStr%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#method.partial_cmp-10)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-10)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-10)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-10)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-10)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialOrd%3COsString%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.partial_cmp-5)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-5)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-5)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-5)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-5)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialOrd%3COsString%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.partial_cmp-3)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-3)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-3)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-3)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-3)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#impl-PartialOrd%3CPath%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3926)[§](#method.partial_cmp-17)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-17)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-17)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-17)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-17)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#impl-PartialOrd%3CPath%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3925)[§](#method.partial_cmp-15)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-15)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-15)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-15)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-15)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#impl-PartialOrd%3CPathBuf%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3922)[§](#method.partial_cmp-13)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-13)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-13)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-13)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-13)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#impl-PartialOrd%3CPathBuf%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3921)[§](#method.partial_cmp-11)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-11)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-11)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-11)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-11)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1547-1552)[§](#impl-PartialOrd%3Cstr%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1549-1551)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1523-1544)[§](#impl-PartialOrd-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1525-1527)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1529-1531)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1533-1535)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1537-1539)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1541-1543)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1686-1696)[§](#impl-ToOwned-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1687)[§](#associatedtype.Owned)

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1689-1691)[§](#method.to_owned)

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1693-1695)[§](#method.clone_into)

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)

1.72.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1460-1475)[§](#impl-TryFrom%3C%26OsStr%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1472-1474)[§](#method.try_from)

Tries to convert an `&OsStr` to a `&str`.

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("foo");
let as_str = <&str>::try_from(os_str).unwrap();
assert_eq!(as_str, "foo");
```

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1461)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1520)[§](#impl-Eq-for-OsStr)

[§](#impl-Freeze-for-OsStr)

[§](#impl-RefUnwindSafe-for-OsStr)

[§](#impl-Send-for-OsStr)

[§](#impl-Sized-for-OsStr)

[§](#impl-Sync-for-OsStr)

[§](#impl-Unpin-for-OsStr)

[§](#impl-UnsafeUnpin-for-OsStr)

[§](#impl-UnwindSafe-for-OsStr)