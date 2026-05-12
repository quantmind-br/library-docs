---
title: CStr in std::ffi - Rust
url: https://doc.rust-lang.org/std/ffi/struct.CStr.html
source: crawler
fetched_at: 2026-05-06T21:30:50.580236916-03:00
rendered_js: false
word_count: 2119
summary: The CStr struct provides a safe, dynamically-sized reference to nul-terminated C-style strings for FFI interoperation in Rust.
tags:
    - rust
    - ffi
    - strings
    - memory-safety
    - interop
    - pointers
category: reference
---

## Struct CStr

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#102)

```rust
pub struct CStr { /* private fields */ }
```

Expand description

A dynamically-sized view of a C string.

The type `&CStr` represents a reference to a borrowed nul-terminated array of bytes. It can be constructed safely from a `&[u8]` slice, or unsafely from a raw `*const c_char`. It can be expressed as a literal in the form `c"Hello world"`.

The `&CStr` can then be converted to a Rust `&str` by performing UTF-8 validation, or into an owned `CString`.

`&CStr` is to `CString` as `&str` is to `String`: the former in each pair are borrowing references; the latter are owned strings.

Note that this structure does **not** have a guaranteed layout (the `repr(transparent)` notwithstanding) and should not be placed in the signatures of FFI functions. Instead, safe wrappers of FFI functions may leverage [`CStr::as_ptr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.as_ptr "method std::ffi::CStr::as_ptr") and the unsafe [`CStr::from_ptr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.from_ptr "associated function std::ffi::CStr::from_ptr") constructor to provide a safe interface to other consumers.

## [§](#examples)Examples

Inspecting a foreign C string:

```rust
use std::ffi::CStr;
use std::os::raw::c_char;

extern "C" { fn my_string() -> *const c_char; }

unsafe {
    let slice = CStr::from_ptr(my_string());
    println!("string buffer size without nul terminator: {}", slice.to_bytes().len());
}
```

Passing a Rust-originating C string:

```rust
use std::ffi::CStr;
use std::os::raw::c_char;

fn work(data: &CStr) {
    unsafe extern "C" fn work_with(s: *const c_char) {}
    unsafe { work_with(data.as_ptr()) }
}

let s = c"Hello world!";
work(&s);
```

Converting a foreign C string into a Rust `String`:

```rust
use std::ffi::CStr;
use std::os::raw::c_char;

extern "C" { fn my_string() -> *const c_char; }

fn my_string_safe() -> String {
    let cstr = unsafe { CStr::from_ptr(my_string()) };
    // Get a copy-on-write Cow<'_, str>, then extract the
    // allocated String (or allocate a fresh one if needed).
    cstr.to_string_lossy().into_owned()
}

println!("string: {}", my_string_safe());
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#186)[§](#impl-CStr)

1.0.0 (const: 1.81.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#253)

Wraps a raw C string with a safe C string wrapper.

This function will wrap the provided `ptr` with a `CStr` wrapper, which allows inspection and interoperation of non-owned C strings. The total size of the terminated buffer must be smaller than [`isize::MAX`](https://doc.rust-lang.org/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX") **bytes** in memory (a restriction from [`slice::from_raw_parts`](https://doc.rust-lang.org/std/slice/fn.from_raw_parts.html "fn std::slice::from_raw_parts")).

##### [§](#safety)Safety

- The memory pointed to by `ptr` must contain a valid nul terminator at the end of the string.
- `ptr` must be [valid](https://doc.rust-lang.org/std/ptr/index.html#safety "mod std::ptr") for reads of bytes up to and including the nul terminator. This means in particular:
  
  - The entire memory range of this `CStr` must be contained within a single allocation!
  - `ptr` must be non-null even for a zero-length cstr.
- The memory referenced by the returned `CStr` must not be mutated for the duration of lifetime `'a`.
- The nul terminator must be within `isize::MAX` from `ptr`

> **Note**: This operation is intended to be a 0-cost cast but it is currently implemented with an up-front calculation of the length of the string. This is not guaranteed to always be the case.

##### [§](#caveat)Caveat

The lifetime for the returned slice is inferred from its usage. To prevent accidental misuse, it’s suggested to tie the lifetime to whichever source lifetime is safe in the context, such as by providing a helper function taking the lifetime of a host value for the slice, or by explicit annotation.

##### [§](#examples-1)Examples

```rust
use std::ffi::{c_char, CStr};

fn my_string() -> *const c_char {
    c"hello".as_ptr()
}

unsafe {
    let slice = CStr::from_ptr(my_string());
    assert_eq!(slice.to_str().unwrap(), "hello");
}
```

```rust
use std::ffi::{c_char, CStr};

const HELLO_PTR: *const c_char = {
    const BYTES: &[u8] = b"Hello, world!\0";
    BYTES.as_ptr().cast()
};
const HELLO: &CStr = unsafe { CStr::from_ptr(HELLO_PTR) };

assert_eq!(c"Hello, world!", HELLO);
```

1.69.0 (const: 1.69.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#298)

Creates a C string wrapper from a byte slice with any number of nuls.

This method will create a `CStr` from any byte slice that contains at least one nul byte. Unlike with [`CStr::from_bytes_with_nul`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.from_bytes_with_nul "associated function std::ffi::CStr::from_bytes_with_nul"), the caller does not need to know where the nul byte is located.

If the first byte is a nul character, this method will return an empty `CStr`. If multiple nul characters are present, the `CStr` will end at the first one.

If the slice only has a single nul byte at the end, this method is equivalent to [`CStr::from_bytes_with_nul`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.from_bytes_with_nul "associated function std::ffi::CStr::from_bytes_with_nul").

##### [§](#examples-2)Examples

```rust
use std::ffi::CStr;

let mut buffer = [0u8; 16];
unsafe {
    // Here we might call an unsafe C function that writes a string
    // into the buffer.
    let buf_ptr = buffer.as_mut_ptr();
    buf_ptr.write_bytes(b'A', 8);
}
// Attempt to extract a C nul-terminated string from the buffer.
let c_str = CStr::from_bytes_until_nul(&buffer[..]).unwrap();
assert_eq!(c_str.to_str().unwrap(), "AAAAAAAA");
```

1.10.0 (const: 1.72.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#351)

Creates a C string wrapper from a byte slice with exactly one nul terminator.

This function will cast the provided `bytes` to a `CStr` wrapper after ensuring that the byte slice is nul-terminated and does not contain any interior nul bytes.

If the nul byte may not be at the end, [`CStr::from_bytes_until_nul`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.from_bytes_until_nul "associated function std::ffi::CStr::from_bytes_until_nul") can be used instead.

##### [§](#examples-3)Examples

```rust
use std::ffi::CStr;

let cstr = CStr::from_bytes_with_nul(b"hello\0");
assert_eq!(cstr, Ok(c"hello"));
```

Creating a `CStr` without a trailing nul terminator is an error:

```rust
use std::ffi::{CStr, FromBytesWithNulError};

let cstr = CStr::from_bytes_with_nul(b"hello");
assert_eq!(cstr, Err(FromBytesWithNulError::NotNulTerminated));
```

Creating a `CStr` with an interior nul byte is an error:

```rust
use std::ffi::{CStr, FromBytesWithNulError};

let cstr = CStr::from_bytes_with_nul(b"he\0llo\0");
assert_eq!(cstr, Err(FromBytesWithNulError::InteriorNul { position: 2 }));
```

1.10.0 (const: 1.59.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#388)

Unsafely creates a C string wrapper from a byte slice.

This function will cast the provided `bytes` to a `CStr` wrapper without performing any sanity checks.

##### [§](#safety-1)Safety

The provided slice **must** be nul-terminated and not contain any interior nul bytes.

##### [§](#examples-4)Examples

```rust
use std::ffi::CStr;

let bytes = b"Hello world!\0";

let cstr = unsafe { CStr::from_bytes_with_nul_unchecked(bytes) };
assert_eq!(cstr.to_bytes_with_nul(), bytes);
```

1.0.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#483)

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

1.79.0 (const: 1.81.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#514)

Returns the length of `self`. Like C’s `strlen`, this does not include the nul terminator.

> **Note**: This method is currently implemented as a constant-time cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-5)Examples

```rust
assert_eq!(c"foo".count_bytes(), 3);
assert_eq!(c"".count_bytes(), 0);
```

1.71.0 (const: 1.71.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#529)

Returns `true` if `self.to_bytes()` has a length of 0.

##### [§](#examples-6)Examples

```rust
assert!(!c"foo".is_empty());
assert!(c"".is_empty());
```

1.0.0 (const: 1.72.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#555)

Converts this C string to a byte slice.

The returned slice will **not** contain the trailing nul terminator that this C string has.

> **Note**: This method is currently implemented as a constant-time cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-7)Examples

```rust
assert_eq!(c"foo".to_bytes(), b"foo");
```

1.0.0 (const: 1.72.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#581)

Converts this C string to a byte slice containing the trailing 0 byte.

This function is the equivalent of [`CStr::to_bytes`](https://doc.rust-lang.org/std/ffi/struct.CStr.html#method.to_bytes "method std::ffi::CStr::to_bytes") except that it will retain the trailing nul terminator instead of chopping it off.

> **Note**: This method is currently implemented as a 0-cost cast, but it is planned to alter its definition in the future to perform the length calculation whenever this method is called.

##### [§](#examples-8)Examples

```rust
assert_eq!(c"foo".to_bytes_with_nul(), b"foo\0");
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#601)

🔬This is a nightly-only experimental API. (`cstr_bytes` [#112115](https://github.com/rust-lang/rust/issues/112115))

Iterates over the bytes in this C string.

The returned iterator will **not** contain the trailing nul terminator that this C string has.

##### [§](#examples-9)Examples

```rust
#![feature(cstr_bytes)]

assert!(c"foo".bytes().eq(*b"foo"));
```

1.4.0 (const: 1.72.0) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#620)

Yields a `&str` slice if the `CStr` contains valid UTF-8.

If the contents of the `CStr` are valid UTF-8 data, this function will return the corresponding `&str` slice. Otherwise, it will return an error with details of where UTF-8 validation failed.

##### [§](#examples-10)Examples

```rust
assert_eq!(c"foo".to_str(), Ok("foo"));
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#648)

🔬This is a nightly-only experimental API. (`cstr_display` [#139984](https://github.com/rust-lang/rust/issues/139984))

Returns an object that implements [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") for safely printing a [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr") that may contain non-Unicode data.

Behaves as if `self` were first lossily converted to a `str`, with invalid UTF-8 presented as the Unicode replacement character: �.

##### [§](#examples-11)Examples

```rust
#![feature(cstr_display)]

let cstr = c"Hello, world!";
println!("{}", cstr.display());
```

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#659)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&CStr`.

This method is redundant when used directly on `&CStr`, but it helps dereferencing other string-like types to string slices, for example references to `Box<CStr>` or `Arc<CStr>`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1149)[§](#impl-CStr-1)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1189)

Converts a `CStr` into a `Cow<str>`.

If the contents of the `CStr` are valid UTF-8 data, this function will return a `Cow::Borrowed(&str)` with the corresponding `&str` slice. Otherwise, it will replace any invalid UTF-8 sequences with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "std::char::REPLACEMENT_CHARACTER") and return a `Cow::Owned(String)` with the result.

##### [§](#examples-12)Examples

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

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1208)

Converts a `Box<CStr>` into a [`CString`](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString") without copying or allocating.

##### [§](#examples-13)Examples

```rust
use std::ffi::{CStr, CString};

let boxed: Box<CStr> = Box::from(c"foo");
let c_string: CString = c"foo".to_owned();

assert_eq!(boxed.into_c_string(), c_string);
```

1.7.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#721)[§](#impl-AsRef%3CCStr%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#723)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1142)[§](#impl-AsRef%3CCStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1144)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#747)[§](#impl-Borrow%3CCStr%3E-for-CString)

1.29.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#854)[§](#impl-Clone-for-Box%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#577)[§](#impl-CloneToUninit-for-CStr)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#579)[§](#method.clone_to_uninit)

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

1.3.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#172)[§](#impl-Debug-for-CStr)

Shows the underlying bytes as a normal string, with invalid UTF-8 presented as hex escape sequences.

1.10.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#179)[§](#impl-Default-for-%26CStr)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#977)[§](#impl-Default-for-Box%3CCStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#911)[§](#impl-From%3C%26CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#915)[§](#method.from-5)

Converts a `&CStr` into a `Arc<CStr>`, by copying the contents into a newly allocated [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc").

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#765)[§](#impl-From%3C%26CStr%3E-for-Box%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#768)[§](#method.from)

Converts a `&CStr` into a `Box<CStr>`, by copying the contents into a newly allocated [`Box`](https://doc.rust-lang.org/std/boxed/struct.Box.html "struct std::boxed::Box").

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1083)[§](#impl-From%3C%26CStr%3E-for-CString)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#880)[§](#impl-From%3C%26CStr%3E-for-Cow%3C'a,+CStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#883)[§](#method.from-4)

Converts a [`CStr`](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr") into a borrowed [`Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow") without copying or allocating.

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#944)[§](#impl-From%3C%26CStr%3E-for-Rc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#948)[§](#method.from-7)

Converts a `&CStr` into a `Rc<CStr>`, by copying the contents into a newly allocated [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc").

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#923)[§](#impl-From%3C%26mut+CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#927)[§](#method.from-6)

Converts a `&mut CStr` into a `Arc<CStr>`, by copying the contents into a newly allocated [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc").

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#774)[§](#impl-From%3C%26mut+CStr%3E-for-Box%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#777)[§](#method.from-1)

Converts a `&mut CStr` into a `Box<CStr>`, by copying the contents into a newly allocated [`Box`](https://doc.rust-lang.org/std/boxed/struct.Box.html "struct std::boxed::Box").

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#955)[§](#impl-From%3C%26mut+CStr%3E-for-Rc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#959)[§](#method.from-8)

Converts a `&mut CStr` into a `Rc<CStr>`, by copying the contents into a newly allocated [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc").

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#862)[§](#impl-From%3CCString%3E-for-Box%3CCStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#783)[§](#impl-From%3CCow%3C'_,+CStr%3E%3E-for-Box%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#787)[§](#method.from-2)

Converts a `Cow<'a, CStr>` into a `Box<CStr>`, by copying the contents if they are borrowed.

1.64.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#impl-Hash-for-CStr)

1.47.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#697)[§](#impl-Index%3CRangeFrom%3Cusize%3E%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#698)[§](#associatedtype.Output)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#701)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#689)[§](#impl-Ord-for-CStr)

1.90.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#665)[§](#impl-PartialEq%3C%26CStr%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#667)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#672)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1105)[§](#impl-PartialEq%3C%26CStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1107)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1112)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1256)[§](#impl-PartialEq%3C%26CStr%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1258)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1263)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1092)[§](#impl-PartialEq%3CCStr%3E-for-CString)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1094)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1099)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1242)[§](#impl-PartialEq%3CCStr%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1244)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1249)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1214)[§](#impl-PartialEq%3CCString%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1216)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1221)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1228)[§](#impl-PartialEq%3CCow%3C'_,+CStr%3E%3E-for-CStr)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1230)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1235)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.64.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#impl-PartialEq-for-CStr)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#681)[§](#impl-PartialOrd-for-CStr)

[Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#683)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1068)[§](#impl-ToOwned-for-CStr)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1069)[§](#associatedtype.Owned)

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1071)[§](#method.to_owned)

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1075)[§](#method.clone_into)

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)

1.64.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#impl-Eq-for-CStr)

1.64.0 · [Source](https://doc.rust-lang.org/src/core/ffi/c_str.rs.html#91)[§](#impl-StructuralPartialEq-for-CStr)

[§](#impl-Freeze-for-CStr)

[§](#impl-RefUnwindSafe-for-CStr)

[§](#impl-Send-for-CStr)

[§](#impl-Sized-for-CStr)

[§](#impl-Sync-for-CStr)

[§](#impl-Unpin-for-CStr)

[§](#impl-UnsafeUnpin-for-CStr)

[§](#impl-UnwindSafe-for-CStr)