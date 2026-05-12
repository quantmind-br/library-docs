---
title: OsString in std::ffi - Rust
url: https://doc.rust-lang.org/std/ffi/struct.OsString.html
source: crawler
fetched_at: 2026-05-06T21:22:04.051919429-03:00
rendered_js: false
word_count: 4984
summary: OsString is an owned, mutable string type in Rust designed to represent platform-native strings by providing interoperability between Rust's UTF-8 strings and platform-specific string formats.
tags:
    - rust
    - ffi
    - string-handling
    - os-strings
    - memory-management
    - cross-platform
category: reference
---

## Struct OsString

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#93-95)

```rust
pub struct OsString { /* private fields */ }
```

Expand description

A type that can represent owned, mutable platform-native strings, but is cheaply inter-convertible with Rust strings.

The need for this type arises from the fact that:

- On Unix systems, strings are often arbitrary sequences of non-zero bytes, in many cases interpreted as UTF-8.
- On Windows, strings are often arbitrary sequences of non-zero 16-bit values, interpreted as UTF-16 when it is valid to do so.
- In Rust, strings are always valid UTF-8, which may contain zeros.

`OsString` and [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") bridge this gap by simultaneously representing Rust and platform-native string values, and in particular allowing a Rust string to be converted into an “OS” string with no cost if possible. A consequence of this is that `OsString` instances are *not* `NUL` terminated; in order to pass to e.g., Unix system call, you should create a [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr").

`OsString` is to `&OsStr` as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") is to `&str`: the former in each pair are owned strings; the latter are borrowed references.

Note, `OsString` and [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") internally do not necessarily hold strings in the form native to the platform; While on Unix, strings are stored as a sequence of 8-bit values, on Windows, where strings are 16-bit value based as just discussed, strings are also actually stored as a sequence of 8-bit values, encoded in a less-strict variant of UTF-8. This is useful to understand when handling capacity and length values.

## [§](#capacity-of-osstring)Capacity of `OsString`

Capacity uses units of UTF-8 bytes for OS strings which were created from valid unicode, and uses units of bytes in an unspecified encoding for other contents. On a given target, all `OsString` and `OsStr` values use the same units for capacity, so the following will work:

```rust
use std::ffi::{OsStr, OsString};

fn concat_os_strings(a: &OsStr, b: &OsStr) -> OsString {
    let mut ret = OsString::with_capacity(a.len() + b.len()); // This will allocate
    ret.push(a); // This will not allocate further
    ret.push(b); // This will not allocate further
    ret
}
```

## [§](#creating-an-osstring)Creating an `OsString`

**From a Rust string**: `OsString` implements `From<String>`, so you can use `my_string.into()` to create an `OsString` from a normal Rust string.

**From slices:** Just like you can start with an empty Rust [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") and then [`String::push_str`](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str "method std::string::String::push_str") some `&str` sub-string slices into it, you can create an empty `OsString` with the [`OsString::new`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.new "associated function std::ffi::OsString::new") method and then push string slices into it with the [`OsString::push`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.push "method std::ffi::OsString::push") method.

You can use the [`OsString::as_os_str`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.as_os_str "method std::ffi::OsString::as_os_str") method to get an `&OsStr` from an `OsString`; this is effectively a borrowed reference to the whole string.

## [§](#conversions)Conversions

See the [module’s toplevel documentation about conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") for a discussion on the traits which `OsString` implements for [conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") from/to native representations.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#127-606)[§](#impl-OsString)

1.0.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#141-143)

Constructs a new empty `OsString`.

##### [§](#examples)Examples

```rust
use std::ffi::OsString;

let os_string = OsString::new();
```

1.74.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#184-186)

Converts bytes to an `OsString` without checking that the bytes contains valid [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr")-encoded data.

The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8. By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit ASCII.

See the [module’s toplevel documentation about conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") for safe, cross-platform [conversions](https://doc.rust-lang.org/std/ffi/index.html#conversions "mod std::ffi") from/to native representations.

##### [§](#safety)Safety

As the encoding is unspecified, callers must pass in bytes that originated as a mixture of validated UTF-8 and bytes from [`OsStr::as_encoded_bytes`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.as_encoded_bytes "method std::ffi::OsStr::as_encoded_bytes") from within the same Rust version built for the same target platform. For example, reconstructing an `OsString` from bytes sent over the network or stored in a file will likely violate these safety rules.

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

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#203-205)

Converts to an [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") slice.

##### [§](#examples-1)Examples

```rust
use std::ffi::{OsString, OsStr};

let os_string = OsString::from("foo");
let os_str = OsStr::new("foo");
assert_eq!(os_string.as_os_str(), os_str);
```

1.74.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#223-225)

Converts the `OsString` into a byte vector. To convert the byte vector back into an `OsString`, use the [`OsString::from_encoded_bytes_unchecked`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.from_encoded_bytes_unchecked "associated function std::ffi::OsString::from_encoded_bytes_unchecked") function.

The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8. By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit ASCII.

Note: As the encoding is unspecified, any sub-slice of bytes that is not valid UTF-8 should be treated as opaque and only comparable within the same Rust version built for the same target platform. For example, sending the bytes over the network or storing it in a file will likely result in incompatible data. See [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString") for more encoding details and [`std::ffi`](https://doc.rust-lang.org/std/ffi/index.html "mod std::ffi") for platform-specific, specified conversions.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#242-244)

Converts the `OsString` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") if it contains valid Unicode data.

On failure, ownership of the original `OsString` is returned.

##### [§](#examples-2)Examples

```rust
use std::ffi::OsString;

let os_string = OsString::from("foo");
let string = os_string.into_string();
assert_eq!(string, Ok(String::from("foo")));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#260-285)

Extends the string with the given `&OsStr` slice.

##### [§](#examples-3)Examples

```rust
use std::ffi::OsString;

let mut os_string = OsString::from("foo");
os_string.push("bar");
assert_eq!(&os_string, "foobar");
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#312-314)

Creates a new `OsString` with at least the given capacity.

The string will be able to hold at least `capacity` length units of other OS strings without reallocating. This method is allowed to allocate for more units than `capacity`. If `capacity` is 0, the string will not allocate.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-4)Examples

```rust
use std::ffi::OsString;

let mut os_string = OsString::with_capacity(10);
let capacity = os_string.capacity();

// This push is done without reallocating
os_string.push("foo");

assert_eq!(capacity, os_string.capacity());
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#331-333)

Truncates the `OsString` to zero length.

##### [§](#examples-5)Examples

```rust
use std::ffi::OsString;

let mut os_string = OsString::from("foo");
assert_eq!(&os_string, "foo");

os_string.clear();
assert_eq!(&os_string, "");
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#350-352)

Returns the capacity this `OsString` can hold without reallocating.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-6)Examples

```rust
use std::ffi::OsString;

let os_string = OsString::with_capacity(10);
assert!(os_string.capacity() >= 10);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#373-375)

Reserves capacity for at least `additional` more capacity to be inserted in the given `OsString`. Does nothing if the capacity is already sufficient.

The collection may reserve more space to speculatively avoid frequent reallocations.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-7)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::new();
s.reserve(10);
assert!(s.capacity() >= 10);
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#412-414)

Tries to reserve capacity for at least `additional` more length units in the given `OsString`. The string may reserve more space to speculatively avoid frequent reallocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient. This method preserves the contents even if an error occurs.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#errors)Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### [§](#examples-8)Examples

```rust
use std::ffi::{OsStr, OsString};
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<OsString, TryReserveError> {
    let mut s = OsString::new();

    // Pre-reserve the memory, exiting if we can't
    s.try_reserve(OsStr::new(data).len())?;

    // Now we know this can't OOM in the middle of our complex work
    s.push(data);

    Ok(s)
}
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#439-441)

Reserves the minimum capacity for at least `additional` more capacity to be inserted in the given `OsString`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer [`reserve`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.reserve "method std::ffi::OsString::reserve") if future insertions are expected.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-9)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::new();
s.reserve_exact(10);
assert!(s.capacity() >= 10);
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#483-485)

Tries to reserve the minimum capacity for at least `additional` more length units in the given `OsString`. After calling `try_reserve_exact`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the `OsString` more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer [`try_reserve`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.try_reserve "method std::ffi::OsString::try_reserve") if future insertions are expected.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#errors-1)Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### [§](#examples-10)Examples

```rust
use std::ffi::{OsStr, OsString};
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<OsString, TryReserveError> {
    let mut s = OsString::new();

    // Pre-reserve the memory, exiting if we can't
    s.try_reserve_exact(OsStr::new(data).len())?;

    // Now we know this can't OOM in the middle of our complex work
    s.push(data);

    Ok(s)
}
```

1.19.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#506-508)

Shrinks the capacity of the `OsString` to match its length.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-11)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to_fit();
assert_eq!(3, s.capacity());
```

1.56.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#536-538)

Shrinks the capacity of the `OsString` with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

See the main `OsString` documentation information about encoding and capacity units.

##### [§](#examples-12)Examples

```rust
use std::ffi::OsString;

let mut s = OsString::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to(10);
assert!(s.capacity() >= 10);
s.shrink_to(0);
assert!(s.capacity() >= 3);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#553-556)

Converts this `OsString` into a boxed [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr").

##### [§](#examples-13)Examples

```rust
use std::ffi::{OsString, OsStr};

let s = OsString::from("hello");

let b: Box<OsStr> = s.into_boxed_os_str();
```

1.89.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#573-575)

Consumes and leaks the `OsString`, returning a mutable reference to the contents, `&'a mut OsStr`.

The caller has free choice over the returned lifetime, including ’static. Indeed, this function is ideally used for data that lives for the remainder of the program’s life, as dropping the returned reference will cause a memory leak.

It does not reallocate or shrink the `OsString`, so the leaked allocation may include unused capacity that is not part of the returned slice. If you want to discard excess capacity, call [`into_boxed_os_str`](https://doc.rust-lang.org/std/ffi/struct.OsString.html#method.into_boxed_os_str "method std::ffi::OsString::into_boxed_os_str"), and then [`Box::leak`](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.leak "associated function std::boxed::Box::leak") instead. However, keep in mind that trimming the capacity may result in a reallocation and copy.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#584-588)

🔬This is a nightly-only experimental API. (`os_string_truncate` [#133262](https://github.com/rust-lang/rust/issues/133262))

Truncate the `OsString` to the specified length.

##### [§](#panics)Panics

Panics if `len` does not lie on a valid `OsStr` boundary (as described in [`OsStr::slice_encoded_bytes`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.slice_encoded_bytes "method std::ffi::OsStr::slice_encoded_bytes")).

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#913-915)

Yields a `&str` slice if the `OsStr` is valid Unicode.

This conversion may entail doing a check for UTF-8 validity.

##### [§](#examples-14)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("foo");
assert_eq!(os_str.to_str(), Some("foo"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#966-968)

Converts an `OsStr` to a `Cow<str>`.

Any non-UTF-8 sequences are replaced with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

##### [§](#examples-15)Examples

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

##### [§](#examples-16)Examples

```rust
use std::ffi::{OsStr, OsString};

let os_str = OsStr::new("foo");
let os_string = os_str.to_os_string();
assert_eq!(os_string, OsString::from("foo"));
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1006-1008)

Checks whether the `OsStr` is empty.

##### [§](#examples-17)Examples

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

##### [§](#examples-18)Examples

```rust
use std::ffi::OsStr;

let os_str = OsStr::new("");
assert_eq!(os_str.len(), 0);

let os_str = OsStr::new("foo");
assert_eq!(os_str.len(), 3);
```

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

##### [§](#panics-1)Panics

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

##### [§](#examples-19)Examples

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

##### [§](#examples-20)Examples

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

##### [§](#examples-21)Examples

```rust
use std::ffi::OsString;
let s = OsString::from("Grüße, Jürgen ❤");

assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1212-1214)

Returns a copy of this string where each character is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`OsStr::make_ascii_uppercase`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html#method.make_ascii_uppercase "method std::ffi::OsStr::make_ascii_uppercase").

##### [§](#examples-22)Examples

```rust
use std::ffi::OsString;
let s = OsString::from("Grüße, Jürgen ❤");

assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
```

1.53.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1234-1236)

Checks if all characters in this string are within the ASCII range.

An empty string returns `true`.

##### [§](#examples-23)Examples

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

##### [§](#examples-24)Examples

```rust
use std::ffi::OsString;

assert!(OsString::from("Ferris").eq_ignore_ascii_case("FERRIS"));
assert!(OsString::from("Ferrös").eq_ignore_ascii_case("FERRöS"));
assert!(!OsString::from("Ferrös").eq_ignore_ascii_case("FERRÖS"));
```

1.87.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1278-1280)

Returns an object that implements [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") for safely printing an [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") that may contain non-Unicode data. This may perform lossy conversion, depending on the platform. If you would like an implementation which escapes the [`OsStr`](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr") please use [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") instead.

##### [§](#examples-25)Examples

```rust
use std::ffi::OsStr;

let s = OsStr::new("Hello, world!");
println!("{}", s.display());
```

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1289-1291)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&OsStr`.

This method is redundant when used directly on `&OsStr`, but it helps dereferencing other string-like types to string slices, for example references to `Box<OsStr>` or `Arc<OsStr>`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1708-1713)[§](#impl-AsRef%3COsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1710-1712)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3792-3797)[§](#impl-AsRef%3CPath%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3794-3796)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1678-1683)[§](#impl-Borrow%3COsStr%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#697-711)[§](#impl-Clone-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#708-710)[§](#method.clone_from)

Clones the contents of `source` into `self`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#699-701)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#714-718)[§](#impl-Debug-for-OsString)

1.9.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#688-694)[§](#impl-Default-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#691-693)[§](#method.default)

Constructs an empty `OsString`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#670-677)[§](#impl-Deref-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#671)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#674-676)[§](#method.deref)

Dereferences the value.

1.44.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#680-685)[§](#impl-DerefMut-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#682-684)[§](#method.deref_mut)

Mutably dereferences the value.

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1773-1780)[§](#impl-Extend%3C%26OsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1775-1779)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1783-1790)[§](#impl-Extend%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1785-1789)[§](#method.extend-2)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one-2)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-2)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1763-1770)[§](#impl-Extend%3COsString%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1765-1769)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1441-1447)[§](#impl-From%3C%26OsString%3E-for-Cow%3C'a,+OsStr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#620-649)[§](#impl-From%3C%26T%3E-for-OsString)

1.18.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1326-1333)[§](#impl-From%3CBox%3COsStr%3E%3E-for-OsString)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1450-1457)[§](#impl-From%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1454-1456)[§](#method.from-8)

Converts a `Cow<'a, OsStr>` into an [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString"), by copying the contents if they are borrowed.

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1363-1371)[§](#impl-From%3COsString%3E-for-Arc%3COsStr%3E)

1.20.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1336-1342)[§](#impl-From%3COsString%3E-for-Box%3COsStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1423-1429)[§](#impl-From%3COsString%3E-for-Cow%3C'a,+OsStr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1965-1973)[§](#impl-From%3COsString%3E-for-PathBuf)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1393-1401)[§](#impl-From%3COsString%3E-for-Rc%3COsStr%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1976-1984)[§](#impl-From%3CPathBuf%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#609-617)[§](#impl-From%3CString%3E-for-OsString)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1812-1821)[§](#impl-FromIterator%3C%26OsStr%3E-for-OsString)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1824-1845)[§](#impl-FromIterator%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

1.52.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1793-1809)[§](#impl-FromIterator%3COsString%3E-for-OsString)

1.45.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1753-1760)[§](#impl-FromStr-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1754)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1757-1759)[§](#method.from_str)

Parses a string `s` to return a value of this type. [Read more](https://doc.rust-lang.org/std/str/trait.FromStr.html#tymethod.from_str)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#804-809)[§](#impl-Hash-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#652-659)[§](#impl-Index%3CRangeFull%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#653)[§](#associatedtype.Output)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#656-658)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.44.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#662-667)[§](#impl-IndexMut%3CRangeFull%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#796-801)[§](#impl-Ord-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/ffi/os_str.rs.html#30-39)[§](#impl-OsStringExt-for-OsString)

Available on **Unix** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/ffi/os_str.rs.html#30-39)[§](#impl-OsStringExt-for-OsString-1)

Available on **WASI** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/ffi.rs.html#93-97)[§](#impl-OsStringExt-for-OsString-2)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/src/std/os/windows/ffi.rs.html#94-96)[§](#method.from_wide)

Creates an `OsString` from a potentially ill-formed UTF-16 slice of 16-bit code units. [Read more](https://doc.rust-lang.org/std/os/windows/ffi/trait.OsStringExt.html#tymethod.from_wide)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialEq%3C%26OsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#impl-PartialEq%3C%26Path%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.29.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#745-750)[§](#impl-PartialEq%3C%26str%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#747-749)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialEq%3COsStr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#impl-PartialEq%3COsString%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1602)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#impl-PartialEq%3COsString%3E-for-%26Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.29.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#753-758)[§](#impl-PartialEq%3COsString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#755-757)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialEq%3COsString%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#impl-PartialEq%3COsString%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#impl-PartialEq%3COsString%3E-for-OsStr)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1601)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#impl-PartialEq%3COsString%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#impl-PartialEq%3COsString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#737-742)[§](#impl-PartialEq%3COsString%3E-for-str)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#739-741)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#impl-PartialEq%3CPath%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#impl-PartialEq%3CPathBuf%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#729-734)[§](#impl-PartialEq%3Cstr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#731-733)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#721-726)[§](#impl-PartialEq-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#723-725)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

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

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#impl-PartialOrd%3C%26Path%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#method.partial_cmp-13)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-13)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-13)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-13)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-13)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#method.partial_cmp-7)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-7)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-7)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-7)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-7)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#method.partial_cmp-15)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-15)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-15)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-15)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-15)

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

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#impl-PartialOrd%3COsString%3E-for-%26Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3931)[§](#method.partial_cmp-12)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-12)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-12)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-12)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-12)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialOrd%3COsString%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1605)[§](#method.partial_cmp-6)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-6)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-6)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-6)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-6)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#impl-PartialOrd%3COsString%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3934)[§](#method.partial_cmp-14)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-14)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-14)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-14)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-14)

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

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#impl-PartialOrd%3COsString%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#method.partial_cmp-10)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-10)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-10)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-10)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-10)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#impl-PartialOrd%3COsString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#method.partial_cmp-8)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-8)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-8)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-8)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-8)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#impl-PartialOrd%3CPath%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3928)[§](#method.partial_cmp-11)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-11)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-11)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-11)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-11)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#impl-PartialOrd%3CPathBuf%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3924)[§](#method.partial_cmp-9)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-9)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-9)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-9)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-9)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#788-793)[§](#impl-PartialOrd%3Cstr%3E-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#790-792)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#764-785)[§](#impl-PartialOrd-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#766-768)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#770-772)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#774-776)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#778-780)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#782-784)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.64.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#812-817)[§](#impl-Write-for-OsString)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#813-816)[§](#method.write_str)

Writes a string slice into this writer, returning whether the write succeeded. [Read more](https://doc.rust-lang.org/std/fmt/trait.Write.html#tymethod.write_str)

1.1.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#183)[§](#method.write_char)

Writes a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into this writer, returning whether the write succeeded. [Read more](https://doc.rust-lang.org/std/fmt/trait.Write.html#method.write_char)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#212)[§](#method.write_fmt)

Glue for usage of the [`write!`](https://doc.rust-lang.org/std/macro.write.html "macro std::write") macro with implementors of this trait. [Read more](https://doc.rust-lang.org/std/fmt/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#761)[§](#impl-Eq-for-OsString)

[§](#impl-Freeze-for-OsString)

[§](#impl-RefUnwindSafe-for-OsString)

[§](#impl-Send-for-OsString)

[§](#impl-Sync-for-OsString)

[§](#impl-Unpin-for-OsString)

[§](#impl-UnsafeUnpin-for-OsString)

[§](#impl-UnwindSafe-for-OsString)