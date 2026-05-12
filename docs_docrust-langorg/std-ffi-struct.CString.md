---
title: CString in std::ffi - Rust
url: https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_string
source: crawler
fetched_at: 2026-05-06T21:23:59.152647636-03:00
rendered_js: false
word_count: 2478
summary: This document describes the CString type in Rust, which is used for creating and managing owned, nul-terminated strings for safe interoperability with C-style interfaces.
tags:
    - rust
    - ffi
    - cstring
    - memory-safety
    - interoperability
    - c-strings
category: reference
---

## Struct CString

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#108)

```rust
pub struct CString { /* private fields */ }
```

Expand description

A type representing an owned, C-compatible, nul-terminated string with no nul bytes in the middle.

This type serves the purpose of being able to safely generate a C-compatible string from a Rust byte slice or vector. An instance of this type is a static guarantee that the underlying bytes contain no interior 0 bytes (“nul characters”) and that the final byte is 0 (“nul terminator”).

`CString` is to `&CStr` as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") is to `&str`: the former in each pair are owned strings; the latter are borrowed references.

## [§](#creating-a-cstring)Creating a `CString`

A `CString` is created from either a byte slice or a byte vector, or anything that implements `Into<Vec<u8>>` (for example, you can build a `CString` straight out of a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") or a `&str`, since both implement that trait). You can create a `CString` from a literal with `CString::from(c"Text")`.

The [`CString::new`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.new "associated function std::ffi::CString::new") method will actually check that the provided `&[u8]` does not have 0 bytes in the middle, and return an error if it finds one.

`CString` implements an [`as_ptr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.as_ptr "method std::ffi::CStr::as_ptr") method through the [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") trait. This method will give you a `*const c_char` which you can feed directly to extern functions that expect a nul-terminated string, like C’s `strdup()`. Notice that [`as_ptr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.as_ptr "method std::ffi::CStr::as_ptr") returns a read-only pointer; if the C code writes to it, that causes undefined behavior.

Alternatively, you can obtain a `&[u8]` slice from a `CString` with the [`CString::as_bytes`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.as_bytes "method std::ffi::CString::as_bytes") method. Slices produced in this way do *not* contain the trailing nul terminator. This is useful when you will be calling an extern function that takes a `*const u8` argument which is not necessarily nul-terminated, plus another argument with the length of the string — like C’s `strndup()`. You can of course get the slice’s length with its [`len`](https://doc.rust-lang.org/std/primitive.slice.html#method.len "method slice::len") method.

If you need a `&[u8]` slice *with* the nul terminator, you can use [`CString::as_bytes_with_nul`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.as_bytes_with_nul "method std::ffi::CString::as_bytes_with_nul") instead.

Once you have the kind of slice you need (with or without a nul terminator), you can call the slice’s own [`as_ptr`](https://doc.rust-lang.org/std/primitive.slice.html#method.as_ptr "method slice::as_ptr") method to get a read-only raw pointer to pass to extern functions. See the documentation for that function for a discussion on ensuring the lifetime of the raw pointer.

## [§](#examples)Examples

[ⓘ](# "This example is not tested")

```rust
use std::ffi::CString;
use std::os::raw::c_char;

extern "C" {
    fn my_printer(s: *const c_char);
}

// We are certain that our string doesn't have 0 bytes in the middle,
// so we can .expect()
let c_to_print = CString::new("Hello, world!").expect("CString::new failed");
unsafe {
    my_printer(c_to_print.as_ptr());
}
```

## [§](#safety)Safety

`CString` is intended for working with traditional C-style strings (a sequence of non-nul bytes terminated by a single nul byte); the primary use case for these kinds of strings is interoperating with C-like code. Often you will need to transfer ownership to/from that external code. It is strongly recommended that you thoroughly read through the documentation of `CString` before use, as improper ownership management of `CString` instances can lead to invalid memory accesses, memory leaks, and other memory errors.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#228)[§](#impl-CString)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#257)

Creates a new C-compatible string from a container of bytes.

This function will consume the provided data and use the underlying bytes to construct a new string, ensuring that there is a trailing 0 byte. This trailing 0 byte will be appended by this function; the provided data should *not* contain any 0 bytes in it.

##### [§](#examples-1)Examples

[ⓘ](# "This example is not tested")

```rust
use std::ffi::CString;
use std::os::raw::c_char;

extern "C" { fn puts(s: *const c_char); }

let to_print = CString::new("Hello!").expect("CString::new failed");
unsafe {
    puts(to_print.as_ptr());
}
```

##### [§](#errors)Errors

This function will return an error if the supplied bytes contain an internal 0 byte. The [`NulError`](https://doc.rust-lang.org/std/ffi/struct.NulError.html "struct std::ffi::NulError") returned will contain the bytes as well as the position of the nul byte.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#336)

Creates a C-compatible string by consuming a byte vector, without checking for interior 0 bytes.

Trailing 0 byte will be appended by this function.

This method is equivalent to [`CString::new`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.new "associated function std::ffi::CString::new") except that no runtime assertion is made that `v` contains no 0 bytes, and it requires an actual byte vector, not anything that can be converted to one with Into.

##### [§](#examples-2)Examples

```rust
use std::ffi::CString;

let raw = b"foo".to_vec();
unsafe {
    let c_string = CString::from_vec_unchecked(raw);
}
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#398)

Retakes ownership of a `CString` that was transferred to C via [`CString::into_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_raw "method std::ffi::CString::into_raw").

Additionally, the length of the string will be recalculated from the pointer.

##### [§](#safety-1)Safety

This should only ever be called with a pointer that was earlier obtained by calling [`CString::into_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_raw "method std::ffi::CString::into_raw"), and the memory it points to must not be accessed through any other pointer during the lifetime of reconstructed `CString`. Other usage (e.g., trying to take ownership of a string that was allocated by foreign code) is likely to lead to undefined behavior or allocator corruption.

This function does not validate ownership of the raw pointer’s memory. A double-free may occur if the function is called twice on the same raw pointer. Additionally, the caller must ensure the pointer is not dangling.

It should be noted that the length isn’t just “recomputed,” but that the recomputed length must match the original length from the [`CString::into_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_raw "method std::ffi::CString::into_raw") call. This means the [`CString::into_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_raw "method std::ffi::CString::into_raw")/`from_raw` methods should not be used when passing the string to C functions that can modify the string’s length.

> **Note:** If you need to borrow a string that was allocated by foreign code, use [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr"). If you need to take ownership of a string that was allocated by foreign code, you will need to make your own provisions for freeing it appropriately, likely with the foreign code’s API to do that.

##### [§](#examples-3)Examples

Creates a `CString`, pass ownership to an `extern` function (via raw pointer), then retake ownership with `from_raw`:

[ⓘ](# "This example is not tested")

```rust
use std::ffi::CString;
use std::os::raw::c_char;

extern "C" {
    fn some_extern_function(s: *mut c_char);
}

let c_string = CString::from(c"Hello!");
let raw = c_string.into_raw();
unsafe {
    some_extern_function(raw);
    let c_string = CString::from_raw(raw);
}
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#451)

Consumes the `CString` and transfers ownership of the string to a C caller.

The pointer which this function returns must be returned to Rust and reconstituted using [`CString::from_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.from_raw "associated function std::ffi::CString::from_raw") to be properly deallocated. Specifically, one should *not* use the standard C `free()` function to deallocate this string.

Failure to call [`CString::from_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.from_raw "associated function std::ffi::CString::from_raw") will lead to a memory leak.

The C side must **not** modify the length of the string (by writing a nul byte somewhere inside the string or removing the final one) before it makes it back into Rust using [`CString::from_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.from_raw "associated function std::ffi::CString::from_raw"). See the safety section in [`CString::from_raw`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.from_raw "associated function std::ffi::CString::from_raw").

##### [§](#examples-4)Examples

```rust
use std::ffi::CString;

let c_string = CString::from(c"foo");

let ptr = c_string.into_raw();

unsafe {
    assert_eq!(b'f', *ptr as u8);
    assert_eq!(b'o', *ptr.add(1) as u8);
    assert_eq!(b'o', *ptr.add(2) as u8);
    assert_eq!(b'\0', *ptr.add(3) as u8);

    // retake pointer to free memory
    let _ = CString::from_raw(ptr);
}
```

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#474)

Converts the `CString` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") if it contains valid UTF-8 data.

On failure, ownership of the original `CString` is returned.

##### [§](#examples-5)Examples

```rust
use std::ffi::CString;

let valid_utf8 = vec![b'f', b'o', b'o'];
let cstring = CString::new(valid_utf8).expect("CString::new failed");
assert_eq!(cstring.into_string().expect("into_string() call failed"), "foo");

let invalid_utf8 = vec![b'f', 0xff, b'o', b'o'];
let cstring = CString::new(invalid_utf8).expect("CString::new failed");
let err = cstring.into_string().err().expect("into_string().err() failed");
assert_eq!(err.utf8_error().valid_up_to(), 1);
```

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#498)

Consumes the `CString` and returns the underlying byte buffer.

The returned buffer does **not** contain the trailing nul terminator, and it is guaranteed to not have any interior nul bytes.

##### [§](#examples-6)Examples

```rust
use std::ffi::CString;

let c_string = CString::from(c"foo");
let bytes = c_string.into_bytes();
assert_eq!(bytes, vec![b'f', b'o', b'o']);
```

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#519)

Equivalent to [`CString::into_bytes()`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.into_bytes "method std::ffi::CString::into_bytes") except that the returned vector includes the trailing nul terminator.

##### [§](#examples-7)Examples

```rust
use std::ffi::CString;

let c_string = CString::from(c"foo");
let bytes = c_string.into_bytes_with_nul();
assert_eq!(bytes, vec![b'f', b'o', b'o', b'\0']);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#542)

Returns the contents of this `CString` as a slice of bytes.

The returned slice does **not** contain the trailing nul terminator, and it is guaranteed to not have any interior nul bytes. If you need the nul terminator, use [`CString::as_bytes_with_nul`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.as_bytes_with_nul "method std::ffi::CString::as_bytes_with_nul") instead.

##### [§](#examples-8)Examples

```rust
use std::ffi::CString;

let c_string = CString::from(c"foo");
let bytes = c_string.as_bytes();
assert_eq!(bytes, &[b'f', b'o', b'o']);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#562)

Equivalent to [`CString::as_bytes()`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.as_bytes "method std::ffi::CString::as_bytes") except that the returned slice includes the trailing nul terminator.

##### [§](#examples-9)Examples

```rust
use std::ffi::CString;

let c_string = CString::from(c"foo");
let bytes = c_string.as_bytes_with_nul();
assert_eq!(bytes, &[b'f', b'o', b'o', b'\0']);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#582)

Extracts a [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr") slice containing the entire string.

##### [§](#examples-10)Examples

```rust
use std::ffi::{CString, CStr};

let c_string = CString::from(c"foo");
let cstr = c_string.as_c_str();
assert_eq!(cstr,
           CStr::from_bytes_with_nul(b"foo\0").expect("CStr::from_bytes_with_nul failed"));
```

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#597)

Converts this `CString` into a boxed [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr").

##### [§](#examples-11)Examples

```rust
let c_string = c"foo".to_owned();
let boxed = c_string.into_boxed_c_str();
assert_eq!(boxed.to_bytes_with_nul(), b"foo\0");
```

1.58.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#631)

Converts a `Vec<u8>` to a [`CString`](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString") without checking the invariants on the given [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec").

##### [§](#safety-2)Safety

The given [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") **must** have one nul byte as its last element. This means it cannot be empty nor have any other nul byte anywhere else.

##### [§](#example)Example

```rust
use std::ffi::CString;
assert_eq!(
    unsafe { CString::from_vec_with_nul_unchecked(b"abc\0".to_vec()) },
    unsafe { CString::from_vec_unchecked(b"abc".to_vec()) }
);
```

1.58.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#674)

Attempts to convert a `Vec<u8>` to a [`CString`](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString").

Runtime checks are present to ensure there is only one nul byte in the [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec"), its last element.

##### [§](#errors-1)Errors

If a nul byte is present and not the last element or no nul bytes is present, an error will be returned.

##### [§](#examples-12)Examples

A successful conversion will produce the same result as [`CString::new`](https://doc.rust-lang.org/std/ffi/struct.CString.html#method.new "associated function std::ffi::CString::new") when called without the ending nul byte.

```rust
use std::ffi::CString;
assert_eq!(
    CString::from_vec_with_nul(b"abc\0".to_vec())
        .expect("CString::from_vec_with_nul failed"),
    c"abc".to_owned()
);
```

An incorrectly formatted [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") will produce an error.

```rust
use std::ffi::{CString, FromVecWithNulError};
// Interior nul byte
let _: FromVecWithNulError = CString::from_vec_with_nul(b"a\0bc".to_vec()).unwrap_err();
// No nul byte
let _: FromVecWithNulError = CString::from_vec_with_nul(b"abc".to_vec()).unwrap_err();
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#483)

Returns the inner pointer to this C string.

The returned pointer will be valid for as long as `self` is, and points to a contiguous region of memory terminated with a 0 byte to represent the end of the string.

The type of the returned pointer is [`*const c_char`](https://doc.rust-lang.org/std/ffi/type.c_char.html "type std::ffi::c_char"), and whether it’s an alias for `*const i8` or `*const u8` is platform-specific.

**WARNING**

The returned pointer is read-only; writing to it (including passing it to C code that writes to it) causes undefined behavior.

It is your responsibility to make sure that the underlying memory is not freed too early. For example, the following code will cause undefined behavior when `ptr` is used inside the `unsafe` block:

```rust
use std::ffi::{CStr, CString};

// 💀 The meaning of this entire program is undefined,
// 💀 and nothing about its behavior is guaranteed,
// 💀 not even that its behavior resembles the code as written,
// 💀 just because it contains a single instance of undefined behavior!

// 🚨 creates a dangling pointer to a temporary `CString`
// 🚨 that is deallocated at the end of the statement
let ptr = CString::new("Hi!".to_uppercase()).unwrap().as_ptr();

// without undefined behavior, you would expect that `ptr` equals:
dbg!(CStr::from_bytes_with_nul(b"HI!\0").unwrap());

// 🙏 Possibly the program behaved as expected so far,
// 🙏 and this just shows `ptr` is now garbage..., but
// 💀 this violates `CStr::from_ptr`'s safety contract
// 💀 leading to a dereference of a dangling pointer,
// 💀 which is immediate undefined behavior.
// 💀 *BOOM*, you're dead, your entire program has no meaning.
dbg!(unsafe { CStr::from_ptr(ptr) });
```

This happens because, the pointer returned by `as_ptr` does not carry any lifetime information, and the `CString` is deallocated immediately after the expression that it is part of has been evaluated. To fix the problem, bind the `CString` to a local variable:

```rust
use std::ffi::{CStr, CString};

let c_str = CString::new("Hi!".to_uppercase()).unwrap();
let ptr = c_str.as_ptr();

assert_eq!(unsafe { CStr::from_ptr(ptr) }, c"HI!");
```

1.79.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#514)

Returns the length of `self`. Like C’s `strlen`, this does not include the nul terminator.

> **Note**: This method is currently implemented as a constant-time cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-13)Examples

```rust
assert_eq!(c"foo".count_bytes(), 3);
assert_eq!(c"".count_bytes(), 0);
```

1.71.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#529)

Returns `true` if `self.to_bytes()` has a length of 0.

##### [§](#examples-14)Examples

```rust
assert!(!c"foo".is_empty());
assert!(c"".is_empty());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#555)

Converts this C string to a byte slice.

The returned slice will **not** contain the trailing nul terminator that this C string has.

> **Note**: This method is currently implemented as a constant-time cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-15)Examples

```rust
assert_eq!(c"foo".to_bytes(), b"foo");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#581)

Converts this C string to a byte slice containing the trailing 0 byte.

This function is the equivalent of [`CStr::to_bytes`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.to_bytes "method std::ffi::CStr::to_bytes") except that it will retain the trailing nul terminator instead of chopping it off.

> **Note**: This method is currently implemented as a 0-cost cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-16)Examples

```rust
assert_eq!(c"foo".to_bytes_with_nul(), b"foo\0");
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#601)

🔬This is a nightly-only experimental API. (`cstr_bytes` [#112115](https://github.com/rust-lang/rust/issues/112115))

Iterates over the bytes in this C string.

The returned iterator will **not** contain the trailing nul terminator that this C string has.

##### [§](#examples-17)Examples

```rust
#![feature(cstr_bytes)]

assert!(c"foo".bytes().eq(*b"foo"));
```

1.4.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#620)

Yields a `&str` slice if the `CStr` contains valid UTF-8.

If the contents of the `CStr` are valid UTF-8 data, this function will return the corresponding `&str` slice. Otherwise, it will return an error with details of where UTF-8 validation failed.

##### [§](#examples-18)Examples

```rust
assert_eq!(c"foo".to_str(), Ok("foo"));
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#648)

🔬This is a nightly-only experimental API. (`cstr_display` [#139984](https://github.com/rust-lang/rust/issues/139984))

Returns an object that implements [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") for safely printing a [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr") that may contain non-Unicode data.

Behaves as if `self` were first lossily converted to a `str`, with invalid UTF-8 presented as the Unicode replacement character: �.

##### [§](#examples-19)Examples

```rust
#![feature(cstr_display)]

let cstr = c"Hello, world!";
println!("{}", cstr.display());
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#659)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&CStr`.

This method is redundant when used directly on `&CStr`, but it helps dereferencing other string-like types to string slices, for example references to `Box<CStr>` or `Arc<CStr>`.

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1189)

Converts a `CStr` into a `Cow<str>`.

If the contents of the `CStr` are valid UTF-8 data, this function will return a `Cow::Borrowed(&str)` with the corresponding `&str` slice. Otherwise, it will replace any invalid UTF-8 sequences with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "std::char::REPLACEMENT_CHARACTER") and return a `Cow::Owned(String)` with the result.

##### [§](#examples-20)Examples

Calling `to_string_lossy` on a `CStr` containing valid UTF-8. The leading `c` on the string literal denotes a `CStr`.

```rust
use std::borrow::Cow;

assert_eq!(c"Hello World".to_string_lossy(), Cow::Borrowed("Hello World"));
```

Calling `to_string_lossy` on a `CStr` containing invalid UTF-8:

```rust
use std::borrow::Cow;

assert_eq!(
    c"Hello \xF0\x90\x80World".to_string_lossy(),
    Cow::Owned(String::from("Hello �World")) as Cow<'_, str>
);
```

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1142)[§](#impl-AsRef%3CCStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1144)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#747)[§](#impl-Borrow%3CCStr%3E-for-CString)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-Clone-for-CString)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#720)[§](#impl-Debug-for-CString)

Delegates to the [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr") implementation of [`fmt::Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug"), showing invalid UTF-8 as hex escapes.

1.10.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#738)[§](#impl-Default-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#740)[§](#method.default)

Creates an empty `CString`.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#708)[§](#impl-Deref-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#709)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#712)[§](#method.deref)

Dereferences the value.

1.13.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#698)[§](#impl-Drop-for-CString)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1083)[§](#impl-From%3C%26CStr%3E-for-CString)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#889)[§](#impl-From%3C%26CString%3E-for-Cow%3C'a,+CStr%3E)

1.18.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#796)[§](#impl-From%3CBox%3CCStr%3E%3E-for-CString)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#899)[§](#impl-From%3CCString%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#862)[§](#impl-From%3CCString%3E-for-Box%3CCStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#871)[§](#impl-From%3CCString%3E-for-Cow%3C'a,+CStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#933)[§](#impl-From%3CCString%3E-for-Rc%3CCStr%3E)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#727)[§](#impl-From%3CCString%3E-for-Vec%3Cu8%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#755)[§](#impl-From%3CCow%3C'a,+CStr%3E%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#759)[§](#method.from-1)

Converts a `Cow<'a, CStr>` into a `CString`, by copying the contents if they are borrowed.

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#806)[§](#impl-From%3CVec%3CNonZero%3Cu8%3E%3E%3E-for-CString)

1.85.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#828)[§](#impl-FromStr-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#835)[§](#method.from_str)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#829)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-Hash-for-CString)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1132)[§](#impl-Index%3CRangeFull%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1133)[§](#associatedtype.Output)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1136)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-Ord-for-CString)

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1105)[§](#impl-PartialEq%3C%26CStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1107)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1112)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1092)[§](#impl-PartialEq%3CCStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1094)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1099)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1214)[§](#impl-PartialEq%3CCString%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1216)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1221)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1270)[§](#impl-PartialEq%3CCString%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1272)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1277)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1119)[§](#impl-PartialEq%3CCow%3C'_,+CStr%3E%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1121)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1126)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-PartialEq-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-PartialOrd-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.85.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#841)[§](#impl-TryFrom%3CCString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#848)[§](#method.try_from)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#842)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-Eq-for-CString)

1.64.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#104)[§](#impl-StructuralPartialEq-for-CString)

[§](#impl-Freeze-for-CString)

[§](#impl-RefUnwindSafe-for-CString)

[§](#impl-Send-for-CString)

[§](#impl-Sync-for-CString)

[§](#impl-Unpin-for-CString)

[§](#impl-UnsafeUnpin-for-CString)

[§](#impl-UnwindSafe-for-CString)