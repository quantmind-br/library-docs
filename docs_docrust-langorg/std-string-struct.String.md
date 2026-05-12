---
title: String in std::string - Rust
url: https://doc.rust-lang.org/std/string/struct.String.html
source: crawler
fetched_at: 2026-05-06T21:21:45.082702033-03:00
rendered_js: false
word_count: 11504
summary: This document provides an overview of the Rust String type, detailing its heap-allocated, UTF-8 encoded structure, ownership characteristics, and how it interacts with string slices through deref coercion.
tags:
    - rust
    - string
    - utf-8
    - memory-management
    - deref-coercion
    - data-types
category: reference
---

## Struct String

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#353)

```rust
pub struct String { /* private fields */ }
```

Expand description

A UTF-8–encoded, growable string.

`String` is the most common string type. It has ownership over the contents of the string, stored in a heap-allocated buffer (see [Representation](#representation)). It is closely related to its borrowed counterpart, the primitive [`str`](https://doc.rust-lang.org/std/primitive.str.html "str").

## [§](#examples)Examples

You can create a `String` from [a literal string](https://doc.rust-lang.org/std/primitive.str.html "&str") with [`String::from`](https://doc.rust-lang.org/std/convert/trait.From.html#tymethod.from "associated function std::convert::From::from"):

```rust
let hello = String::from("Hello, world!");
```

You can append a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") to a `String` with the [`push`](https://doc.rust-lang.org/std/string/struct.String.html#method.push "method std::string::String::push") method, and append a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str") with the [`push_str`](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str "method std::string::String::push_str") method:

```rust
let mut hello = String::from("Hello, ");

hello.push('w');
hello.push_str("orld!");
```

If you have a vector of UTF-8 bytes, you can create a `String` from it with the [`from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8 "associated function std::string::String::from_utf8") method:

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

// We know these bytes are valid, so we'll use `unwrap()`.
let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);
```

## [§](#utf-8)UTF-8

`String`s are always valid UTF-8. If you need a non-UTF-8 string, consider [`OsString`](https://doc.rust-lang.org/std/ffi/struct.OsString.html "ffi::OsString"). It is similar, but without the UTF-8 constraint. Because UTF-8 is a variable width encoding, `String`s are typically smaller than an array of the same `char`s:

```rust
// `s` is ASCII which represents each `char` as one byte
let s = "hello";
assert_eq!(s.len(), 5);

// A `char` array with the same contents would be longer because
// every `char` is four bytes
let s = ['h', 'e', 'l', 'l', 'o'];
let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
assert_eq!(size, 20);

// However, for non-ASCII strings, the difference will be smaller
// and sometimes they are the same
let s = "💖💖💖💖💖";
assert_eq!(s.len(), 20);

let s = ['💖', '💖', '💖', '💖', '💖'];
let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
assert_eq!(size, 20);
```

This raises interesting questions as to how `s[i]` should work. What should `i` be here? Several options include byte indices and `char` indices but, because of UTF-8 encoding, only byte indices would provide constant time indexing. Getting the `i`th `char`, for example, is available using [`chars`](https://doc.rust-lang.org/std/primitive.str.html#method.chars "method str::chars"):

```rust
let s = "hello";
let third_character = s.chars().nth(2);
assert_eq!(third_character, Some('l'));

let s = "💖💖💖💖💖";
let third_character = s.chars().nth(2);
assert_eq!(third_character, Some('💖'));
```

Next, what should `s[i]` return? Because indexing returns a reference to underlying data it could be `&u8`, `&[u8]`, or something similar. Since we’re only providing one index, `&u8` makes the most sense but that might not be what the user expects and can be explicitly achieved with [`as_bytes()`](https://doc.rust-lang.org/std/primitive.str.html#method.as_bytes "method str::as_bytes"):

```rust
// The first byte is 104 - the byte value of `'h'`
let s = "hello";
assert_eq!(s.as_bytes()[0], 104);
// or
assert_eq!(s.as_bytes()[0], b'h');

// The first byte is 240 which isn't obviously useful
let s = "💖💖💖💖💖";
assert_eq!(s.as_bytes()[0], 240);
```

Due to these ambiguities/restrictions, indexing with a `usize` is simply forbidden:

[ⓘ](# "This example deliberately fails to compile")

```rust
let s = "hello";

// The following will not compile!
println!("The first letter of s is {}", s[0]);
```

It is more clear, however, how `&s[i..j]` should work (that is, indexing with a range). It should accept byte indices (to be constant-time) and return a `&str` which is UTF-8 encoded. This is also called “string slicing”. Note this will panic if the byte indices provided are not character boundaries - see [`is_char_boundary`](https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary "method str::is_char_boundary") for more details. See the implementations for [`SliceIndex<str>`](https://doc.rust-lang.org/std/slice/trait.SliceIndex.html "trait std::slice::SliceIndex") for more details on string slicing. For a non-panicking version of string slicing, see [`get`](https://doc.rust-lang.org/std/primitive.str.html#method.get "method str::get").

The [`bytes`](https://doc.rust-lang.org/std/primitive.str.html#method.bytes "method str::bytes") and [`chars`](https://doc.rust-lang.org/std/primitive.str.html#method.chars "method str::chars") methods return iterators over the bytes and codepoints of the string, respectively. To iterate over codepoints along with byte indices, use [`char_indices`](https://doc.rust-lang.org/std/primitive.str.html#method.char_indices "method str::char_indices").

## [§](#deref)Deref

`String` implements `Deref<Target = str>`, and so inherits all of [`str`](https://doc.rust-lang.org/std/primitive.str.html "str")’s methods. In addition, this means that you can pass a `String` to a function which takes a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str") by using an ampersand (`&`):

```rust
fn takes_str(s: &str) { }

let s = String::from("Hello");

takes_str(&s);
```

This will create a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str") from the `String` and pass it in. This conversion is very inexpensive, and so generally, functions will accept [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str")s as arguments unless they need a `String` for some specific reason.

In certain cases Rust doesn’t have enough information to make this conversion, known as [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "ops::Deref") coercion. In the following example a string slice [`&'a str`](https://doc.rust-lang.org/std/primitive.str.html "&str") implements the trait `TraitExample`, and the function `example_func` takes anything that implements the trait. In this case Rust would need to make two implicit conversions, which Rust doesn’t have the means to do. For that reason, the following example will not compile.

[ⓘ](# "This example deliberately fails to compile")

```rust
trait TraitExample {}

impl<'a> TraitExample for &'a str {}

fn example_func<A: TraitExample>(example_arg: A) {}

let example_string = String::from("example_string");
example_func(&example_string);
```

There are two options that would work instead. The first would be to change the line `example_func(&example_string);` to `example_func(example_string.as_str());`, using the method [`as_str()`](https://doc.rust-lang.org/std/string/struct.String.html#method.as_str "method std::string::String::as_str") to explicitly extract the string slice containing the string. The second way changes `example_func(&example_string);` to `example_func(&*example_string);`. In this case we are dereferencing a `String` to a [`str`](https://doc.rust-lang.org/std/primitive.str.html "str"), then referencing the [`str`](https://doc.rust-lang.org/std/primitive.str.html "str") back to [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str"). The second way is more idiomatic, however both work to do the conversion explicitly rather than relying on the implicit conversion.

## [§](#representation)Representation

A `String` is made up of three components: a pointer to some bytes, a length, and a capacity. The pointer points to the internal buffer which `String` uses to store its data. The length is the number of bytes currently stored in the buffer, and the capacity is the size of the buffer in bytes. As such, the length will always be less than or equal to the capacity.

This buffer is always stored on the heap.

You can look at these with the [`as_ptr`](https://doc.rust-lang.org/std/primitive.str.html#method.as_ptr "method str::as_ptr"), [`len`](https://doc.rust-lang.org/std/string/struct.String.html#method.len "method std::string::String::len"), and [`capacity`](https://doc.rust-lang.org/std/string/struct.String.html#method.capacity "method std::string::String::capacity") methods:

```rust
let story = String::from("Once upon a time...");

// Deconstruct the String into parts.
let (ptr, len, capacity) = story.into_raw_parts();

// story has nineteen bytes
assert_eq!(19, len);

// We can re-build a String out of ptr, len, and capacity. This is all
// unsafe because we are responsible for making sure the components are
// valid:
let s = unsafe { String::from_raw_parts(ptr, len, capacity) } ;

assert_eq!(String::from("Once upon a time..."), s);
```

If a `String` has enough capacity, adding elements to it will not re-allocate. For example, consider this program:

```rust
let mut s = String::new();

println!("{}", s.capacity());

for _ in 0..5 {
    s.push_str("hello");
    println!("{}", s.capacity());
}
```

This will output the following:

At first, we have no memory allocated at all, but as we append to the string, it increases its capacity appropriately. If we instead use the [`with_capacity`](https://doc.rust-lang.org/std/string/struct.String.html#method.with_capacity "associated function std::string::String::with_capacity") method to allocate the correct capacity initially:

```rust
let mut s = String::with_capacity(25);

println!("{}", s.capacity());

for _ in 0..5 {
    s.push_str("hello");
    println!("{}", s.capacity());
}
```

We end up with a different output:

Here, there’s no need to allocate more memory inside the loop.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#415)[§](#impl-String)

1.0.0 (const: 1.39.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#437)

Creates a new empty `String`.

Given that the `String` is empty, this will not allocate any initial buffer. While that means that this initial operation is very inexpensive, it may cause excessive allocation later when you add data. If you have an idea of how much data the `String` will hold, consider the [`with_capacity`](https://doc.rust-lang.org/std/string/struct.String.html#method.with_capacity "associated function std::string::String::with_capacity") method to prevent excessive re-allocation.

##### [§](#examples-1)Examples

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#484)

Creates a new empty `String` with at least the specified capacity.

`String`s have an internal buffer to hold their data. The capacity is the length of that buffer, and can be queried with the [`capacity`](https://doc.rust-lang.org/std/string/struct.String.html#method.capacity "method std::string::String::capacity") method. This method creates an empty `String`, but one with an initial buffer that can hold at least `capacity` bytes. This is useful when you may be appending a bunch of data to the `String`, reducing the number of reallocations it needs to do.

If the given capacity is `0`, no allocation will occur, and this method is identical to the [`new`](https://doc.rust-lang.org/std/string/struct.String.html#method.new "associated function std::string::String::new") method.

##### [§](#panics)Panics

Panics if the capacity exceeds `isize::MAX` *bytes*.

##### [§](#examples-2)Examples

```rust
let mut s = String::with_capacity(10);

// The String contains no chars, even though it has capacity for more
assert_eq!(s.len(), 0);

// These are all done without reallocating...
let cap = s.capacity();
for _ in 0..10 {
    s.push('a');
}

assert_eq!(s.capacity(), cap);

// ...but this may make the string reallocate
s.push('a');
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#497)

🔬This is a nightly-only experimental API. (`try_with_capacity` [#91913](https://github.com/rust-lang/rust/issues/91913))

Creates a new empty `String` with at least the specified capacity.

##### [§](#errors)Errors

Returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if the capacity exceeds `isize::MAX` bytes, or if the memory allocator reports failure.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#560)

Converts a vector of bytes to a `String`.

A string ([`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String")) is made of bytes ([`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")), and a vector of bytes ([`Vec<u8>`](https://doc.rust-lang.org/std/vec/struct.Vec.html "Vec")) is made of bytes, so this function converts between the two. Not all byte slices are valid `String`s, however: `String` requires that it is valid UTF-8. `from_utf8()` checks to ensure that the bytes are valid UTF-8, and then does the conversion.

If you are sure that the byte slice is valid UTF-8, and you don’t want to incur the overhead of the validity check, there is an unsafe version of this function, [`from_utf8_unchecked`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_unchecked "associated function std::string::String::from_utf8_unchecked"), which has the same behavior but skips the check.

This method will take care to not copy the vector, for efficiency’s sake.

If you need a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "&str") instead of a `String`, consider [`str::from_utf8`](https://doc.rust-lang.org/std/str/fn.from_utf8.html "fn std::str::from_utf8").

The inverse of this method is [`into_bytes`](https://doc.rust-lang.org/std/string/struct.String.html#method.into_bytes "method std::string::String::into_bytes").

##### [§](#errors-1)Errors

Returns [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if the slice is not UTF-8 with a description as to why the provided bytes are not UTF-8. The vector you moved in is also included.

##### [§](#examples-3)Examples

Basic usage:

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

// We know these bytes are valid, so we'll use `unwrap()`.
let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();

assert_eq!("💖", sparkle_heart);
```

Incorrect bytes:

```rust
// some invalid bytes, in a vector
let sparkle_heart = vec![0, 159, 146, 150];

assert!(String::from_utf8(sparkle_heart).is_err());
```

See the docs for [`FromUtf8Error`](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html "struct std::string::FromUtf8Error") for more details on what you can do with this error.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#619)

Converts a slice of bytes to a string, including invalid characters.

Strings are made of bytes ([`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8")), and a slice of bytes ([`&[u8]`](https://doc.rust-lang.org/std/primitive.slice.html "primitive slice")) is made of bytes, so this function converts between the two. Not all byte slices are valid strings, however: strings are required to be valid UTF-8. During this conversion, `from_utf8_lossy()` will replace any invalid UTF-8 sequences with [`U+FFFD REPLACEMENT CHARACTER`](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER"), which looks like this: �

If you are sure that the byte slice is valid UTF-8, and you don’t want to incur the overhead of the conversion, there is an unsafe version of this function, [`from_utf8_unchecked`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_unchecked "associated function std::string::String::from_utf8_unchecked"), which has the same behavior but skips the checks.

This function returns a [`Cow<'a, str>`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "borrow::Cow"). If our byte slice is invalid UTF-8, then we need to insert the replacement characters, which will change the size of the string, and hence, require a `String`. But if it’s already valid UTF-8, we don’t need a new allocation. This return type allows us to handle both cases.

##### [§](#examples-4)Examples

Basic usage:

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8_lossy(&sparkle_heart);

assert_eq!("💖", sparkle_heart);
```

Incorrect bytes:

```rust
// some invalid bytes
let input = b"Hello \xF0\x90\x80World";
let output = String::from_utf8_lossy(input);

assert_eq!("Hello �World", output);
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#684)

🔬This is a nightly-only experimental API. (`string_from_utf8_lossy_owned` [#129436](https://github.com/rust-lang/rust/issues/129436))

Converts a [`Vec<u8>`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") to a `String`, substituting invalid UTF-8 sequences with replacement characters.

See [`from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy "associated function std::string::String::from_utf8_lossy") for more details.

Note that this function does not guarantee reuse of the original `Vec` allocation.

##### [§](#examples-5)Examples

Basic usage:

```rust
#![feature(string_from_utf8_lossy_owned)]
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = String::from_utf8_lossy_owned(sparkle_heart);

assert_eq!(String::from("💖"), sparkle_heart);
```

Incorrect bytes:

```rust
#![feature(string_from_utf8_lossy_owned)]
// some invalid bytes
let input: Vec<u8> = b"Hello \xF0\x90\x80World".into();
let output = String::from_utf8_lossy_owned(input);

assert_eq!(String::from("Hello �World"), output);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#716)

Decode a native endian UTF-16–encoded vector `v` into a `String`, returning [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if `v` contains any invalid data.

##### [§](#examples-6)Examples

```rust
// 𝄞music
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0x0073, 0x0069, 0x0063];
assert_eq!(String::from("𝄞music"),
           String::from_utf16(v).unwrap());

// 𝄞mu<invalid>ic
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0xD800, 0x0069, 0x0063];
assert!(String::from_utf16(v).is_err());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#755)

Decode a native endian UTF-16–encoded slice `v` into a `String`, replacing invalid data with [the replacement character (`U+FFFD`)](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

Unlike [`from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy "associated function std::string::String::from_utf8_lossy") which returns a [`Cow<'a, str>`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "borrow::Cow"), `from_utf16_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### [§](#examples-7)Examples

```rust
// 𝄞mus<invalid>ic<invalid>
let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
          0x0073, 0xDD1E, 0x0069, 0x0063,
          0xD834];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16_lossy(v));
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#783)

🔬This is a nightly-only experimental API. (`str_from_utf16_endian` [#116258](https://github.com/rust-lang/rust/issues/116258))

Decode a UTF-16LE–encoded vector `v` into a `String`, returning [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if `v` contains any invalid data.

##### [§](#examples-8)Examples

Basic usage:

```rust
#![feature(str_from_utf16_endian)]
// 𝄞music
let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x73, 0x00, 0x69, 0x00, 0x63, 0x00];
assert_eq!(String::from("𝄞music"),
           String::from_utf16le(v).unwrap());

// 𝄞mu<invalid>ic
let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x00, 0xD8, 0x69, 0x00, 0x63, 0x00];
assert!(String::from_utf16le(v).is_err());
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#822)

🔬This is a nightly-only experimental API. (`str_from_utf16_endian` [#116258](https://github.com/rust-lang/rust/issues/116258))

Decode a UTF-16LE–encoded slice `v` into a `String`, replacing invalid data with [the replacement character (`U+FFFD`)](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

Unlike [`from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy "associated function std::string::String::from_utf8_lossy") which returns a [`Cow<'a, str>`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "borrow::Cow"), `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### [§](#examples-9)Examples

Basic usage:

```rust
#![feature(str_from_utf16_endian)]
// 𝄞mus<invalid>ic<invalid>
let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
          0x73, 0x00, 0x1E, 0xDD, 0x69, 0x00, 0x63, 0x00,
          0x34, 0xD8];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16le_lossy(v));
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#858)

🔬This is a nightly-only experimental API. (`str_from_utf16_endian` [#116258](https://github.com/rust-lang/rust/issues/116258))

Decode a UTF-16BE–encoded vector `v` into a `String`, returning [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") if `v` contains any invalid data.

##### [§](#examples-10)Examples

Basic usage:

```rust
#![feature(str_from_utf16_endian)]
// 𝄞music
let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0x00, 0x73, 0x00, 0x69, 0x00, 0x63];
assert_eq!(String::from("𝄞music"),
           String::from_utf16be(v).unwrap());

// 𝄞mu<invalid>ic
let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0xD8, 0x00, 0x00, 0x69, 0x00, 0x63];
assert!(String::from_utf16be(v).is_err());
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#897)

🔬This is a nightly-only experimental API. (`str_from_utf16_endian` [#116258](https://github.com/rust-lang/rust/issues/116258))

Decode a UTF-16BE–encoded slice `v` into a `String`, replacing invalid data with [the replacement character (`U+FFFD`)](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER").

Unlike [`from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy "associated function std::string::String::from_utf8_lossy") which returns a [`Cow<'a, str>`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "borrow::Cow"), `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8 conversion requires a memory allocation.

##### [§](#examples-11)Examples

Basic usage:

```rust
#![feature(str_from_utf16_endian)]
// 𝄞mus<invalid>ic<invalid>
let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
          0x00, 0x73, 0xDD, 0x1E, 0x00, 0x69, 0x00, 0x63,
          0xD8, 0x34];

assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
           String::from_utf16be_lossy(v));
```

1.93.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#938)

Decomposes a `String` into its raw components: `(pointer, length, capacity)`.

Returns the raw pointer to the underlying data, the length of the string (in bytes), and the allocated capacity of the data (in bytes). These are the same arguments in the same order as the arguments to [`from_raw_parts`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_raw_parts "associated function std::string::String::from_raw_parts").

After calling this function, the caller is responsible for the memory previously managed by the `String`. The only way to do this is to convert the raw pointer, length, and capacity back into a `String` with the [`from_raw_parts`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_raw_parts "associated function std::string::String::from_raw_parts") function, allowing the destructor to perform the cleanup.

##### [§](#examples-12)Examples

```rust
let s = String::from("hello");

let (ptr, len, cap) = s.into_raw_parts();

let rebuilt = unsafe { String::from_raw_parts(ptr, len, cap) };
assert_eq!(rebuilt, "hello");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#980)

Creates a new `String` from a pointer, a length and a capacity.

##### [§](#safety)Safety

This is highly unsafe, due to the number of invariants that aren’t checked:

- all safety requirements for [`Vec::<u8>::from_raw_parts`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.from_raw_parts "associated function std::vec::Vec::from_raw_parts").
- all safety requirements for [`String::from_utf8_unchecked`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_unchecked "associated function std::string::String::from_utf8_unchecked").

Violating these may cause problems like corrupting the allocator’s internal data structures. For example, it is normally **not** safe to build a `String` from a pointer to a C `char` array containing UTF-8 *unless* you are certain that array was originally allocated by the Rust standard library’s allocator.

The ownership of `buf` is effectively transferred to the `String` which may then deallocate, reallocate or change the contents of memory pointed to by the pointer at will. Ensure that nothing else uses the pointer after calling this function.

##### [§](#examples-13)Examples

```rust
unsafe {
    let s = String::from("hello");

    // Deconstruct the String into parts.
    let (ptr, len, capacity) = s.into_raw_parts();

    let s = String::from_raw_parts(ptr, len, capacity);

    assert_eq!(String::from("hello"), s);
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1013)

Converts a vector of bytes to a `String` without checking that the string contains valid UTF-8.

See the safe version, [`from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8 "associated function std::string::String::from_utf8"), for more details.

##### [§](#safety-1)Safety

This function is unsafe because it does not check that the bytes passed to it are valid UTF-8. If this constraint is violated, it may cause memory unsafety issues with future users of the `String`, as the rest of the standard library assumes that `String`s are valid UTF-8.

##### [§](#examples-14)Examples

```rust
// some bytes, in a vector
let sparkle_heart = vec![240, 159, 146, 150];

let sparkle_heart = unsafe {
    String::from_utf8_unchecked(sparkle_heart)
};

assert_eq!("💖", sparkle_heart);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1034)

Converts a `String` into a byte vector.

This consumes the `String`, so we do not need to copy its contents.

##### [§](#examples-15)Examples

```rust
let s = String::from("hello");
let bytes = s.into_bytes();

assert_eq!(&[104, 101, 108, 108, 111][..], &bytes[..]);
```

1.7.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1052)

Extracts a string slice containing the entire `String`.

##### [§](#examples-16)Examples

```rust
let s = String::from("foo");

assert_eq!("foo", s.as_str());
```

1.7.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1075)

Converts a `String` into a mutable string slice.

##### [§](#examples-17)Examples

```rust
let mut s = String::from("foobar");
let s_mut_str = s.as_mut_str();

s_mut_str.make_ascii_uppercase();

assert_eq!("FOOBAR", s_mut_str);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1101)

Appends a given string slice onto the end of this `String`.

##### [§](#panics-1)Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### [§](#examples-18)Examples

```rust
let mut s = String::from("foo");

s.push_str("bar");

assert_eq!("foobar", s);
```

1.87.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1147-1149)

Copies elements from `src` range to the end of the string.

##### [§](#panics-2)Panics

Panics if the range has `start_bound > end_bound`, if the range is bounded on either end and does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary, or if the new capacity exceeds `isize::MAX` bytes.

##### [§](#examples-19)Examples

```rust
let mut string = String::from("abcde");

string.extend_from_within(2..);
assert_eq!(string, "abcdecde");

string.extend_from_within(..2);
assert_eq!(string, "abcdecdeab");

string.extend_from_within(4..8);
assert_eq!(string, "abcdecdeabecde");
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1172)

Returns this `String`’s capacity, in bytes.

##### [§](#examples-20)Examples

```rust
let s = String::with_capacity(10);

assert!(s.capacity() >= 10);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1219)

Reserves capacity for at least `additional` bytes more than the current length. The allocator may reserve more space to speculatively avoid frequent allocations. After calling `reserve`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if capacity is already sufficient.

##### [§](#panics-3)Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### [§](#examples-21)Examples

Basic usage:

```rust
let mut s = String::new();

s.reserve(10);

assert!(s.capacity() >= 10);
```

This might not actually increase the capacity:

```rust
let mut s = String::with_capacity(10);
s.push('a');
s.push('b');

// s now has a length of 2 and a capacity of at least 10
let capacity = s.capacity();
assert_eq!(2, s.len());
assert!(capacity >= 10);

// Since we already have at least an extra 8 capacity, calling this...
s.reserve(8);

// ... doesn't actually increase.
assert_eq!(capacity, s.capacity());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1269)

Reserves the minimum capacity for at least `additional` bytes more than the current length. Unlike [`reserve`](https://doc.rust-lang.org/std/string/struct.String.html#method.reserve "method std::string::String::reserve"), this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `reserve_exact`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if the capacity is already sufficient.

##### [§](#panics-4)Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### [§](#examples-22)Examples

Basic usage:

```rust
let mut s = String::new();

s.reserve_exact(10);

assert!(s.capacity() >= 10);
```

This might not actually increase the capacity:

```rust
let mut s = String::with_capacity(10);
s.push('a');
s.push('b');

// s now has a length of 2 and a capacity of at least 10
let capacity = s.capacity();
assert_eq!(2, s.len());
assert!(capacity >= 10);

// Since we already have at least an extra 8 capacity, calling this...
s.reserve_exact(8);

// ... doesn't actually increase.
assert_eq!(capacity, s.capacity());
```

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1304)

Tries to reserve capacity for at least `additional` bytes more than the current length. The allocator may reserve more space to speculatively avoid frequent allocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient. This method preserves the contents even if an error occurs.

##### [§](#errors-2)Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### [§](#examples-23)Examples

```rust
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<String, TryReserveError> {
    let mut output = String::new();

    // Pre-reserve the memory, exiting if we can't
    output.try_reserve(data.len())?;

    // Now we know this can't OOM in the middle of our complex work
    output.push_str(data);

    Ok(output)
}
```

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1345)

Tries to reserve the minimum capacity for at least `additional` bytes more than the current length. Unlike [`try_reserve`](https://doc.rust-lang.org/std/string/struct.String.html#method.try_reserve "method std::string::String::try_reserve"), this will not deliberately over-allocate to speculatively avoid frequent allocations. After calling `try_reserve_exact`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer [`try_reserve`](https://doc.rust-lang.org/std/string/struct.String.html#method.try_reserve "method std::string::String::try_reserve") if future insertions are expected.

##### [§](#errors-3)Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### [§](#examples-24)Examples

```rust
use std::collections::TryReserveError;

fn process_data(data: &str) -> Result<String, TryReserveError> {
    let mut output = String::new();

    // Pre-reserve the memory, exiting if we can't
    output.try_reserve_exact(data.len())?;

    // Now we know this can't OOM in the middle of our complex work
    output.push_str(data);

    Ok(output)
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1365)

Shrinks the capacity of this `String` to match its length.

##### [§](#examples-25)Examples

```rust
let mut s = String::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to_fit();
assert_eq!(3, s.capacity());
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1392)

Shrinks the capacity of this `String` with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

##### [§](#examples-26)Examples

```rust
let mut s = String::from("foo");

s.reserve(100);
assert!(s.capacity() >= 100);

s.shrink_to(10);
assert!(s.capacity() >= 10);
s.shrink_to(0);
assert!(s.capacity() >= 3);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1416)

Appends the given [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") to the end of this `String`.

##### [§](#panics-5)Panics

Panics if the new capacity exceeds `isize::MAX` *bytes*.

##### [§](#examples-27)Examples

```rust
let mut s = String::from("abc");

s.push('1');
s.push('2');
s.push('3');

assert_eq!("abc123", s);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1445)

Returns a byte slice of this `String`’s contents.

The inverse of this method is [`from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8 "associated function std::string::String::from_utf8").

##### [§](#examples-28)Examples

```rust
let s = String::from("hello");

assert_eq!(&[104, 101, 108, 108, 111], s.as_bytes());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1473)

Shortens this `String` to the specified length.

If `new_len` is greater than or equal to the string’s current length, this has no effect.

Note that this method has no effect on the allocated capacity of the string

##### [§](#panics-6)Panics

Panics if `new_len` does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#examples-29)Examples

```rust
let mut s = String::from("hello");

s.truncate(2);

assert_eq!("he", s);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1497)

Removes the last character from the string buffer and returns it.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if this `String` is empty.

##### [§](#examples-30)Examples

```rust
let mut s = String::from("abč");

assert_eq!(s.pop(), Some('č'));
assert_eq!(s.pop(), Some('b'));
assert_eq!(s.pop(), Some('a'));

assert_eq!(s.pop(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1530)

Removes a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") from this `String` at byte position `idx` and returns it.

Copies all bytes after the removed char to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### [§](#panics-7)Panics

Panics if `idx` is larger than or equal to the `String`’s length, or if it does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#examples-31)Examples

```rust
let mut s = String::from("abç");

assert_eq!(s.remove(0), 'a');
assert_eq!(s.remove(1), 'ç');
assert_eq!(s.remove(0), 'b');
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1567)

🔬This is a nightly-only experimental API. (`string_remove_matches` [#72826](https://github.com/rust-lang/rust/issues/72826))

Remove all matches of pattern `pat` in the `String`.

##### [§](#examples-32)Examples

```rust
#![feature(string_remove_matches)]
let mut s = String::from("Trees are not green, the sky is not blue.");
s.remove_matches("not ");
assert_eq!("Trees are green, the sky is blue.", s);
```

Matches will be detected and removed iteratively, so in cases where patterns overlap, only the first pattern will be removed:

```rust
#![feature(string_remove_matches)]
let mut s = String::from("banana");
s.remove_matches("ana");
assert_eq!("bna", s);
```

1.26.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1644-1646)

Retains only the characters specified by the predicate.

In other words, remove all characters `c` such that `f(c)` returns `false`. This method operates in place, visiting each character exactly once in the original order, and preserves the order of the retained characters.

##### [§](#examples-33)Examples

```rust
let mut s = String::from("f_o_ob_ar");

s.retain(|c| c != '_');

assert_eq!(s, "foobar");
```

Because the elements are visited exactly once in the original order, external state may be used to decide which elements to keep.

```rust
let mut s = String::from("abcde");
let keep = [false, true, true, false, true];
let mut iter = keep.iter();
s.retain(|_| *iter.next().unwrap());
assert_eq!(s, "bce");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1726)

Inserts a character into this `String` at byte position `idx`.

Reallocates if `self.capacity()` is insufficient, which may involve copying all `self.capacity()` bytes. Makes space for the insertion by copying all bytes of `&self[idx..]` to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### [§](#panics-8)Panics

Panics if `idx` is larger than the `String`’s length, or if it does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#examples-34)Examples

```rust
let mut s = String::with_capacity(3);

s.insert(0, 'f');
s.insert(1, 'o');
s.insert(2, 'o');

assert_eq!("foo", s);
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1783)

Inserts a string slice into this `String` at byte position `idx`.

Reallocates if `self.capacity()` is insufficient, which may involve copying all `self.capacity()` bytes. Makes space for the insertion by copying all bytes of `&self[idx..]` to new positions.

Note that calling this in a loop can result in quadratic behavior.

##### [§](#panics-9)Panics

Panics if `idx` is larger than the `String`’s length, or if it does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#examples-35)Examples

```rust
let mut s = String::from("bar");

s.insert_str(0, "foo");

assert_eq!("foobar", s);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1836)

Returns a mutable reference to the contents of this `String`.

##### [§](#safety-2)Safety

This function is unsafe because the returned `&mut Vec` allows writing bytes which are not valid UTF-8. If this constraint is violated, using the original `String` after dropping the `&mut Vec` may violate memory safety, as the rest of the standard library assumes that `String`s are valid UTF-8.

##### [§](#examples-36)Examples

```rust
let mut s = String::from("hello");

unsafe {
    let vec = s.as_mut_vec();
    assert_eq!(&[104, 101, 108, 108, 111][..], &vec[..]);

    vec.reverse();
}
assert_eq!(s, "olleh");
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1860)

Returns the length of this `String`, in bytes, not [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s or graphemes. In other words, it might not be what a human considers the length of the string.

##### [§](#examples-37)Examples

```rust
let a = String::from("foo");
assert_eq!(a.len(), 3);

let fancy_f = String::from("ƒoo");
assert_eq!(fancy_f.len(), 4);
assert_eq!(fancy_f.chars().count(), 3);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1880)

Returns `true` if this `String` has a length of zero, and `false` otherwise.

##### [§](#examples-38)Examples

```rust
let mut v = String::new();
assert!(v.is_empty());

v.push('a');
assert!(!v.is_empty());
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1912)

Splits the string into two at the given byte index.

Returns a newly allocated `String`. `self` contains bytes `[0, at)`, and the returned `String` contains bytes `[at, len)`. `at` must be on the boundary of a UTF-8 code point.

Note that the capacity of `self` does not change.

##### [§](#panics-10)Panics

Panics if `at` is not on a `UTF-8` code point boundary, or if it is beyond the last code point of the string.

##### [§](#examples-39)Examples

```rust
let mut hello = String::from("Hello, World!");
let world = hello.split_off(7);
assert_eq!(hello, "Hello, ");
assert_eq!(world, "World!");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1936)

Truncates this `String`, removing all contents.

While this means the `String` will have a length of zero, it does not touch its capacity.

##### [§](#examples-40)Examples

```rust
let mut s = String::from("foo");

s.clear();

assert!(s.is_empty());
assert_eq!(0, s.len());
assert_eq!(3, s.capacity());
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#1975-1977)

Removes the specified range from the string in bulk, returning all removed characters as an iterator.

The returned iterator keeps a mutable borrow on the string to optimize its implementation.

##### [§](#panics-11)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#leaking)Leaking

If the returned iterator goes out of scope without being dropped (due to [`core::mem::forget`](https://doc.rust-lang.org/std/mem/fn.forget.html "fn std::mem::forget"), for example), the string may still contain a copy of any drained characters, or may have lost characters arbitrarily, including characters outside the range.

##### [§](#examples-41)Examples

```rust
let mut s = String::from("α is alpha, β is beta");
let beta_offset = s.find('β').unwrap_or(s.len());

// Remove the range up until the β from the string
let t: String = s.drain(..beta_offset).collect();
assert_eq!(t, "α is alpha, ");
assert_eq!(s, "β is beta");

// A full range clears the string, like `clear()` does
s.drain(..);
assert_eq!(s, "");
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2049)

🔬This is a nightly-only experimental API. (`string_into_chars` [#133125](https://github.com/rust-lang/rust/issues/133125))

Converts a `String` into an iterator over the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s of the string.

As a string consists of valid UTF-8, we can iterate through a string by [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"). This method returns such an iterator.

It’s important to remember that [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") represents a Unicode Scalar Value, and might not match your idea of what a ‘character’ is. Iteration over grapheme clusters may be what you actually want. That functionality is not provided by Rust’s standard library, check crates.io instead.

##### [§](#examples-42)Examples

Basic usage:

```rust
#![feature(string_into_chars)]

let word = String::from("goodbye");

let mut chars = word.into_chars();

assert_eq!(Some('g'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('d'), chars.next());
assert_eq!(Some('b'), chars.next());
assert_eq!(Some('y'), chars.next());
assert_eq!(Some('e'), chars.next());

assert_eq!(None, chars.next());
```

Remember, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s might not match your intuition about characters:

```rust
#![feature(string_into_chars)]

let y = String::from("y̆");

let mut chars = y.into_chars();

assert_eq!(Some('y'), chars.next()); // not 'y̆'
assert_eq!(Some('\u{0306}'), chars.next());

assert_eq!(None, chars.next());
```

1.27.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2075-2077)

Removes the specified range in the string, and replaces it with the given string. The given string doesn’t need to be the same length as the range.

##### [§](#panics-12)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and does not lie on a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") boundary.

##### [§](#examples-43)Examples

```rust
let mut s = String::from("α is alpha, β is beta");
let beta_offset = s.find('β').unwrap_or(s.len());

// Replace the range up until the β from the string
s.replace_range(..beta_offset, "Α is capital alpha; ");
assert_eq!(s, "Α is capital alpha; β is beta");
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2117)

🔬This is a nightly-only experimental API. (`string_replace_in_place` [#147949](https://github.com/rust-lang/rust/issues/147949))

Replaces the leftmost occurrence of a pattern with another string, in-place.

This method can be preferred over [`string = string.replacen(..., 1);`](https://doc.rust-lang.org/std/primitive.str.html#method.replacen), as it can use the `String`’s existing capacity to prevent a reallocation if sufficient space is available.

##### [§](#examples-44)Examples

Basic usage:

```rust
#![feature(string_replace_in_place)]

let mut s = String::from("Test Results: ❌❌❌");

// Replace the leftmost ❌ with a ✅
s.replace_first('❌', "✅");
assert_eq!(s, "Test Results: ✅❌❌");
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2143-2145)

🔬This is a nightly-only experimental API. (`string_replace_in_place` [#147949](https://github.com/rust-lang/rust/issues/147949))

Replaces the rightmost occurrence of a pattern with another string, in-place.

##### [§](#examples-45)Examples

Basic usage:

```rust
#![feature(string_replace_in_place)]

let mut s = String::from("Test Results: ❌❌❌");

// Replace the rightmost ❌ with a ✅
s.replace_last('❌', "✅");
assert_eq!(s, "Test Results: ❌❌✅");
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2174)

Converts this `String` into a `Box<str>`.

Before doing the conversion, this method discards excess capacity like [`shrink_to_fit`](https://doc.rust-lang.org/std/string/struct.String.html#method.shrink_to_fit "method std::string::String::shrink_to_fit"). Note that this call may reallocate and copy the bytes of the string.

##### [§](#examples-46)Examples

```rust
let s = String::from("hello");

let b = s.into_boxed_str();
```

1.72.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2205)

Consumes and leaks the `String`, returning a mutable reference to the contents, `&'a mut str`.

The caller has free choice over the returned lifetime, including `'static`. Indeed, this function is ideally used for data that lives for the remainder of the program’s life, as dropping the returned reference will cause a memory leak.

It does not reallocate or shrink the `String`, so the leaked allocation may include unused capacity that is not part of the returned slice. If you want to discard excess capacity, call [`into_boxed_str`](https://doc.rust-lang.org/std/string/struct.String.html#method.into_boxed_str "method std::string::String::into_boxed_str"), and then [`Box::leak`](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.leak "associated function std::boxed::Box::leak") instead. However, keep in mind that trimming the capacity may result in a reallocation and copy.

##### [§](#examples-47)Examples

```rust
let x = String::from("bucket");
let static_ref: &'static mut str = x.leak();
assert_eq!(static_ref, "bucket");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#157)

Returns the length of `self`.

This length is in bytes, not [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s or graphemes. In other words, it might not be what a human considers the length of the string.

##### [§](#examples-48)Examples

```rust
let len = "foo".len();
assert_eq!(3, len);

assert_eq!("ƒoo".len(), 4); // fancy f!
assert_eq!("ƒoo".chars().count(), 3);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#177)

Returns `true` if `self` has a length of zero bytes.

##### [§](#examples-49)Examples

```rust
let s = "";
assert!(s.is_empty());

let s = "not empty";
assert!(!s.is_empty());
```

1.9.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#377)

Checks that `index`-th byte is the first byte in a UTF-8 code point sequence or the end of the string.

The start and end of the string (when `index == self.len()`) are considered to be boundaries.

Returns `false` if `index` is greater than `self.len()`.

##### [§](#examples-50)Examples

```rust
let s = "Löwe 老虎 Léopard";
assert!(s.is_char_boundary(0));
// start of `老`
assert!(s.is_char_boundary(6));
assert!(s.is_char_boundary(s.len()));

// second byte of `ö`
assert!(!s.is_char_boundary(2));

// third byte of `老`
assert!(!s.is_char_boundary(8));
```

1.91.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#426)

Finds the closest `x` not exceeding `index` where [`is_char_boundary(x)`](https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary "method str::is_char_boundary") is `true`.

This method can help you truncate a string so that it’s still valid UTF-8, but doesn’t exceed a given number of bytes. Note that this is done purely at the character level and can still visually split graphemes, even though the underlying characters aren’t split. For example, the emoji 🧑‍🔬 (scientist) could be split so that the string only includes 🧑 (person) instead.

##### [§](#examples-51)Examples

```rust
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.floor_char_boundary(13);
assert_eq!(closest, 10);
assert_eq!(&s[..closest], "❤️🧡");
```

1.91.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#469)

Finds the closest `x` not below `index` where [`is_char_boundary(x)`](https://doc.rust-lang.org/std/primitive.str.html#method.is_char_boundary "method str::is_char_boundary") is `true`.

If `index` is greater than the length of the string, this returns the length of the string.

This method is the natural complement to [`floor_char_boundary`](https://doc.rust-lang.org/std/primitive.str.html#method.floor_char_boundary "method str::floor_char_boundary"). See that method for more details.

##### [§](#examples-52)Examples

```rust
let s = "❤️🧡💛💚💙💜";
assert_eq!(s.len(), 26);
assert!(!s.is_char_boundary(13));

let closest = s.ceil_char_boundary(13);
assert_eq!(closest, 14);
assert_eq!(&s[..closest], "❤️🧡💛");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#502)

Converts a string slice to a byte slice. To convert the byte slice back into a string slice, use the [`from_utf8`](https://doc.rust-lang.org/std/str/fn.from_utf8.html "fn std::str::from_utf8") function.

##### [§](#examples-53)Examples

```rust
let bytes = "bors".as_bytes();
assert_eq!(b"bors", bytes);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#547)

Converts a mutable string slice to a mutable byte slice.

##### [§](#safety-3)Safety

The caller must ensure that the content of the slice is valid UTF-8 before the borrow ends and the underlying `str` is used.

Use of a `str` whose contents are not valid UTF-8 is undefined behavior.

##### [§](#examples-54)Examples

Basic usage:

```rust
let mut s = String::from("Hello");
let bytes = unsafe { s.as_bytes_mut() };

assert_eq!(b"Hello", bytes);
```

Mutability:

```rust
let mut s = String::from("🗻∈🌏");

unsafe {
    let bytes = s.as_bytes_mut();

    bytes[0] = 0xF0;
    bytes[1] = 0x9F;
    bytes[2] = 0x8D;
    bytes[3] = 0x94;
}

assert_eq!("🍔∈🌏", s);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#578)

Converts a string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8"). This pointer will be pointing to the first byte of the string slice.

The caller must ensure that the returned pointer is never written to. If you need to mutate the contents of the string slice, use [`as_mut_ptr`](https://doc.rust-lang.org/std/primitive.str.html#method.as_mut_ptr "method str::as_mut_ptr").

##### [§](#examples-55)Examples

```rust
let s = "Hello";
let ptr = s.as_ptr();
```

1.36.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#596)

Converts a mutable string slice to a raw pointer.

As string slices are a slice of bytes, the raw pointer points to a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8"). This pointer will be pointing to the first byte of the string slice.

It is your responsibility to make sure that the string slice only gets modified in a way that it remains valid UTF-8.

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#622)

Returns a subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") whenever equivalent indexing operation would panic.

##### [§](#examples-56)Examples

```rust
let v = String::from("🗻∈🌏");

assert_eq!(Some("🗻"), v.get(0..4));

// indices not on UTF-8 sequence boundaries
assert!(v.get(1..).is_none());
assert!(v.get(..8).is_none());

// out of bounds
assert!(v.get(..42).is_none());
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#655)

Returns a mutable subslice of `str`.

This is the non-panicking alternative to indexing the `str`. Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") whenever equivalent indexing operation would panic.

##### [§](#examples-57)Examples

```rust
let mut v = String::from("hello");
// correct length
assert!(v.get_mut(0..5).is_some());
// out of bounds
assert!(v.get_mut(..42).is_none());
assert_eq!(Some("he"), v.get_mut(0..2).map(|v| &*v));

assert_eq!("hello", v);
{
    let s = v.get_mut(0..2);
    let s = s.map(|s| {
        s.make_ascii_uppercase();
        &*s
    });
    assert_eq!(Some("HE"), s);
}
assert_eq!("HEllo", v);
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#687)

Returns an unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### [§](#safety-4)Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### [§](#examples-58)Examples

```rust
let v = "🗻∈🌏";
unsafe {
    assert_eq!("🗻", v.get_unchecked(0..4));
    assert_eq!("∈", v.get_unchecked(4..7));
    assert_eq!("🌏", v.get_unchecked(7..11));
}
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#722)

Returns a mutable, unchecked subslice of `str`.

This is the unchecked alternative to indexing the `str`.

##### [§](#safety-5)Safety

Callers of this function are responsible that these preconditions are satisfied:

- The starting index must not exceed the ending index;
- Indexes must be within bounds of the original slice;
- Indexes must lie on UTF-8 sequence boundaries.

Failing that, the returned string slice may reference invalid memory or violate the invariants communicated by the `str` type.

##### [§](#examples-59)Examples

```rust
let mut v = String::from("🗻∈🌏");
unsafe {
    assert_eq!("🗻", v.get_unchecked_mut(0..4));
    assert_eq!("∈", v.get_unchecked_mut(4..7));
    assert_eq!("🌏", v.get_unchecked_mut(7..11));
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#773)

👎Deprecated since 1.29.0: use `get_unchecked(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") and [`Index`](https://doc.rust-lang.org/std/ops/trait.Index.html "trait std::ops::Index").

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get a mutable string slice instead, see the [`slice_mut_unchecked`](https://doc.rust-lang.org/std/primitive.str.html#method.slice_mut_unchecked "method str::slice_mut_unchecked") method.

##### [§](#safety-6)Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

##### [§](#examples-60)Examples

```rust
let s = "Löwe 老虎 Léopard";

unsafe {
    assert_eq!("Löwe 老虎 Léopard", s.slice_unchecked(0, 21));
}

let s = "Hello, world!";

unsafe {
    assert_eq!("world", s.slice_unchecked(7, 12));
}
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#807)

👎Deprecated since 1.29.0: use `get_unchecked_mut(begin..end)` instead

Creates a string slice from another string slice, bypassing safety checks.

This is generally not recommended, use with caution! For a safe alternative see [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") and [`IndexMut`](https://doc.rust-lang.org/std/ops/trait.IndexMut.html "trait std::ops::IndexMut").

This new slice goes from `begin` to `end`, including `begin` but excluding `end`.

To get an immutable string slice instead, see the [`slice_unchecked`](https://doc.rust-lang.org/std/primitive.str.html#method.slice_unchecked "method str::slice_unchecked") method.

##### [§](#safety-7)Safety

Callers of this function are responsible that three preconditions are satisfied:

- `begin` must not exceed `end`.
- `begin` and `end` must be byte positions within the string slice.
- `begin` and `end` must lie on UTF-8 sequence boundaries.

1.4.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#847)

Divides one string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the [`split_at_mut`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut "method str::split_at_mut") method.

##### [§](#panics-13)Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see [`split_at_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_checked "method str::split_at_checked").

##### [§](#examples-61)Examples

```rust
let s = "Per Martin-Löf";

let (first, last) = s.split_at(3);

assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);
```

1.4.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#888)

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the [`split_at`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at "method str::split_at") method.

##### [§](#panics-14)Panics

Panics if `mid` is not on a UTF-8 code point boundary, or if it is past the end of the last code point of the string slice. For a non-panicking alternative see [`split_at_mut_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut_checked "method str::split_at_mut_checked").

##### [§](#examples-62)Examples

```rust
let mut s = "Per Martin-Löf".to_string();
{
    let (first, last) = s.split_at_mut(3);
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);
```

1.80.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#928)

Divides one string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get mutable string slices instead, see the [`split_at_mut_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_mut_checked "method str::split_at_mut_checked") method.

##### [§](#examples-63)Examples

```rust
let s = "Per Martin-Löf";

let (first, last) = s.split_at_checked(3).unwrap();
assert_eq!("Per", first);
assert_eq!(" Martin-Löf", last);

assert_eq!(None, s.split_at_checked(13));  // Inside “ö”
assert_eq!(None, s.split_at_checked(16));  // Beyond the string length
```

1.80.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#969)

Divides one mutable string slice into two at an index.

The argument, `mid`, should be a valid byte offset from the start of the string. It must also be on the boundary of a UTF-8 code point. The method returns `None` if that’s not the case.

The two slices returned go from the start of the string slice to `mid`, and from `mid` to the end of the string slice.

To get immutable string slices instead, see the [`split_at_checked`](https://doc.rust-lang.org/std/primitive.str.html#method.split_at_checked "method str::split_at_checked") method.

##### [§](#examples-64)Examples

```rust
let mut s = "Per Martin-Löf".to_string();
if let Some((first, last)) = s.split_at_mut_checked(3) {
    first.make_ascii_uppercase();
    assert_eq!("PER", first);
    assert_eq!(" Martin-Löf", last);
}
assert_eq!("PER Martin-Löf", s);

assert_eq!(None, s.split_at_mut_checked(13));  // Inside “ö”
assert_eq!(None, s.split_at_mut_checked(16));  // Beyond the string length
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1066)

Returns an iterator over the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s of a string slice.

As a string slice consists of valid UTF-8, we can iterate through a string slice by [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"). This method returns such an iterator.

It’s important to remember that [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") represents a Unicode Scalar Value, and might not match your idea of what a ‘character’ is. Iteration over grapheme clusters may be what you actually want. This functionality is not provided by Rust’s standard library, check crates.io instead.

##### [§](#examples-65)Examples

Basic usage:

```rust
let word = "goodbye";

let count = word.chars().count();
assert_eq!(7, count);

let mut chars = word.chars();

assert_eq!(Some('g'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('o'), chars.next());
assert_eq!(Some('d'), chars.next());
assert_eq!(Some('b'), chars.next());
assert_eq!(Some('y'), chars.next());
assert_eq!(Some('e'), chars.next());

assert_eq!(None, chars.next());
```

Remember, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s might not match your intuition about characters:

```rust
let y = "y̆";

let mut chars = y.chars();

assert_eq!(Some('y'), chars.next()); // not 'y̆'
assert_eq!(Some('\u{0306}'), chars.next());

assert_eq!(None, chars.next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1123)

Returns an iterator over the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s of a string slice, and their positions.

As a string slice consists of valid UTF-8, we can iterate through a string slice by [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"). This method returns an iterator of both these [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, as well as their byte positions.

The iterator yields tuples. The position is first, the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") is second.

##### [§](#examples-66)Examples

Basic usage:

```rust
let word = "goodbye";

let count = word.char_indices().count();
assert_eq!(7, count);

let mut char_indices = word.char_indices();

assert_eq!(Some((0, 'g')), char_indices.next());
assert_eq!(Some((1, 'o')), char_indices.next());
assert_eq!(Some((2, 'o')), char_indices.next());
assert_eq!(Some((3, 'd')), char_indices.next());
assert_eq!(Some((4, 'b')), char_indices.next());
assert_eq!(Some((5, 'y')), char_indices.next());
assert_eq!(Some((6, 'e')), char_indices.next());

assert_eq!(None, char_indices.next());
```

Remember, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s might not match your intuition about characters:

```rust
let yes = "y̆es";

let mut char_indices = yes.char_indices();

assert_eq!(Some((0, 'y')), char_indices.next()); // not (0, 'y̆')
assert_eq!(Some((1, '\u{0306}')), char_indices.next());

// note the 3 here - the previous character took up two bytes
assert_eq!(Some((3, 'e')), char_indices.next());
assert_eq!(Some((4, 's')), char_indices.next());

assert_eq!(None, char_indices.next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1146)

Returns an iterator over the bytes of a string slice.

As a string slice consists of a sequence of bytes, we can iterate through a string slice by byte. This method returns such an iterator.

##### [§](#examples-67)Examples

```rust
let mut bytes = "bors".bytes();

assert_eq!(Some(b'b'), bytes.next());
assert_eq!(Some(b'o'), bytes.next());
assert_eq!(Some(b'r'), bytes.next());
assert_eq!(Some(b's'), bytes.next());

assert_eq!(None, bytes.next());
```

1.1.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1198)

Splits a string slice by whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of whitespace.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`. If you only want to split on ASCII whitespace instead, use [`split_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_ascii_whitespace "method str::split_ascii_whitespace").

##### [§](#examples-68)Examples

Basic usage:

```rust
let mut iter = "A few words".split_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

All kinds of whitespace are considered:

```rust
let mut iter = " Mary   had\ta\u{2009}little  \n\t lamb".split_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all whitespace, the iterator yields no string slices:

```rust
assert_eq!("".split_whitespace().next(), None);
assert_eq!("   ".split_whitespace().next(), None);
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1249)

Splits a string slice by ASCII whitespace.

The iterator returned will return string slices that are sub-slices of the original string slice, separated by any amount of ASCII whitespace.

This uses the same definition as [`char::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.char.html#method.is_ascii_whitespace "method char::is_ascii_whitespace"). To split by Unicode `Whitespace` instead, use [`split_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_whitespace "method str::split_whitespace").

##### [§](#examples-69)Examples

Basic usage:

```rust
let mut iter = "A few words".split_ascii_whitespace();

assert_eq!(Some("A"), iter.next());
assert_eq!(Some("few"), iter.next());
assert_eq!(Some("words"), iter.next());

assert_eq!(None, iter.next());
```

Various kinds of ASCII whitespace are considered (see [`char::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.char.html#method.is_ascii_whitespace "method char::is_ascii_whitespace")):

```rust
let mut iter = " Mary   had\ta little  \n\t lamb".split_ascii_whitespace();
assert_eq!(Some("Mary"), iter.next());
assert_eq!(Some("had"), iter.next());
assert_eq!(Some("a"), iter.next());
assert_eq!(Some("little"), iter.next());
assert_eq!(Some("lamb"), iter.next());

assert_eq!(None, iter.next());
```

If the string is empty or all ASCII whitespace, the iterator yields no string slices:

```rust
assert_eq!("".split_ascii_whitespace().next(), None);
assert_eq!("   ".split_ascii_whitespace().next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1313)

Returns an iterator over the lines of a string, as string slices.

Lines are split at line endings that are either newlines (`\n`) or sequences of a carriage return followed by a line feed (`\r\n`).

Line terminators are not included in the lines returned by the iterator.

Note that any carriage return (`\r`) not immediately followed by a line feed (`\n`) does not split a line. These carriage returns are thereby included in the produced lines.

The final line ending is optional. A string that ends with a final line ending will return the same lines as an otherwise identical string without a final line ending.

An empty string returns an empty iterator.

##### [§](#examples-70)Examples

Basic usage:

```rust
let text = "foo\r\nbar\n\nbaz\r";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
// Trailing carriage return is included in the last line
assert_eq!(Some("baz\r"), lines.next());

assert_eq!(None, lines.next());
```

The final line does not require any ending:

```rust
let text = "foo\nbar\n\r\nbaz";
let mut lines = text.lines();

assert_eq!(Some("foo"), lines.next());
assert_eq!(Some("bar"), lines.next());
assert_eq!(Some(""), lines.next());
assert_eq!(Some("baz"), lines.next());

assert_eq!(None, lines.next());
```

An empty string returns an empty iterator:

```rust
let text = "";
let mut lines = text.lines();

assert_eq!(lines.next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1322)

👎Deprecated since 1.4.0: use lines() instead now

Returns an iterator over the lines of a string.

1.8.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1342)

Returns an iterator of `u16` over the string encoded as native endian UTF-16 (without byte-order mark).

##### [§](#examples-71)Examples

```rust
let text = "Zażółć gęślą jaźń";

let utf8_len = text.len();
let utf16_len = text.encode_utf16().count();

assert!(utf16_len <= utf8_len);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1367)

Returns `true` if the given pattern matches a sub-slice of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-72)Examples

```rust
let bananas = "bananas";

assert!(bananas.contains("nana"));
assert!(!bananas.contains("apples"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1405)

Returns `true` if the given pattern matches a prefix of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, in which case this function will return true if the `&str` is a prefix of this string slice.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can also be a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches. These will only be checked against the first character of this string slice. Look at the second example below regarding behavior for slices of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s.

##### [§](#examples-73)Examples

```rust
let bananas = "bananas";

assert!(bananas.starts_with("bana"));
assert!(!bananas.starts_with("nana"));
```

```rust
let bananas = "bananas";

// Note that both of these assert successfully.
assert!(bananas.starts_with(&['b', 'a', 'n', 'a']));
assert!(bananas.starts_with(&['a', 'b', 'c', 'd']));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1430-1432)

Returns `true` if the given pattern matches a suffix of this string slice.

Returns `false` if it does not.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-74)Examples

```rust
let bananas = "bananas";

assert!(bananas.ends_with("anas"));
assert!(!bananas.ends_with("nana"));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1481)

Returns the byte index of the first character of this string slice that matches the pattern.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the pattern doesn’t match.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-75)Examples

Simple patterns:

```rust
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.find('L'), Some(0));
assert_eq!(s.find('é'), Some(14));
assert_eq!(s.find("pard"), Some(17));
```

More complex patterns using point-free style and closures:

```rust
let s = "Löwe 老虎 Léopard";

assert_eq!(s.find(char::is_whitespace), Some(5));
assert_eq!(s.find(char::is_lowercase), Some(1));
assert_eq!(s.find(|c: char| c.is_whitespace() || c.is_lowercase()), Some(1));
assert_eq!(s.find(|c: char| (c < 'o') && (c > 'a')), Some(4));
```

Not finding the pattern:

```rust
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.find(x), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1527-1529)

Returns the byte index for the first character of the last match of the pattern in this string slice.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the pattern doesn’t match.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-76)Examples

Simple patterns:

```rust
let s = "Löwe 老虎 Léopard Gepardi";

assert_eq!(s.rfind('L'), Some(13));
assert_eq!(s.rfind('é'), Some(14));
assert_eq!(s.rfind("pard"), Some(24));
```

More complex patterns with closures:

```rust
let s = "Löwe 老虎 Léopard";

assert_eq!(s.rfind(char::is_whitespace), Some(12));
assert_eq!(s.rfind(char::is_lowercase), Some(20));
```

Not finding the pattern:

```rust
let s = "Löwe 老虎 Léopard";
let x: &[_] = &['1', '2'];

assert_eq!(s.rfind(x), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1655)

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

If there are no matches the full string slice is returned as the only item in the iterator.

##### [§](#iterator-behavior)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rsplit`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplit "method str::rsplit") method can be used.

##### [§](#examples-77)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".split(' ').collect();
assert_eq!(v, ["Mary", "had", "a", "little", "lamb"]);

let v: Vec<&str> = "".split('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".split('X').collect();
assert_eq!(v, ["lion", "", "tiger", "leopard"]);

let v: Vec<&str> = "lion::tiger::leopard".split("::").collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);

let v: Vec<&str> = "AABBCC".split("DD").collect();
assert_eq!(v, ["AABBCC"]);

let v: Vec<&str> = "abc1def2ghi".split(char::is_numeric).collect();
assert_eq!(v, ["abc", "def", "ghi"]);

let v: Vec<&str> = "lionXtigerXleopard".split(char::is_uppercase).collect();
assert_eq!(v, ["lion", "tiger", "leopard"]);
```

If the pattern is a slice of chars, split on each occurrence of any of the characters:

```rust
let v: Vec<&str> = "2020-11-03 23:59".split(&['-', ' ', ':', '@'][..]).collect();
assert_eq!(v, ["2020", "11", "03", "23", "59"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".split(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "def", "ghi"]);
```

If a string contains multiple contiguous separators, you will end up with empty strings in the output:

```rust
let x = "||||a||b|c".to_string();
let d: Vec<_> = x.split('|').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

Contiguous separators are separated by the empty string.

```rust
let x = "(///)".to_string();
let d: Vec<_> = x.split('/').collect();

assert_eq!(d, &["(", "", "", ")"]);
```

Separators at the start or end of a string are neighbored by empty strings.

```rust
let d: Vec<_> = "010".split("0").collect();
assert_eq!(d, &["", "1", ""]);
```

When the empty string is used as a separator, it separates every character in the string, along with the beginning and end of the string.

```rust
let f: Vec<_> = "rust".split("").collect();
assert_eq!(f, &["", "r", "u", "s", "t", ""]);
```

Contiguous separators can lead to possibly surprising behavior when whitespace is used as the separator. This code is correct:

```rust
let x = "    a  b c".to_string();
let d: Vec<_> = x.split(' ').collect();

assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
```

It does *not* give you:

[ⓘ](# "This example is not tested")

```rust
assert_eq!(d, &["a", "b", "c"]);
```

Use [`split_whitespace`](https://doc.rust-lang.org/std/primitive.str.html#method.split_whitespace "method str::split_whitespace") for this behavior.

1.51.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1696)

Returns an iterator over substrings of this string slice, separated by characters matched by a pattern.

Differs from the iterator produced by `split` in that `split_inclusive` leaves the matched part as the terminator of the substring.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-78)Examples

```rust
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb."
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb."]);
```

If the last element of the string is matched, that element will be considered the terminator of the preceding substring. That substring will be the last item returned by the iterator.

```rust
let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb.\n"
    .split_inclusive('\n').collect();
assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb.\n"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1751-1753)

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern and yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-1)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split") method can be used.

##### [§](#examples-79)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);

let v: Vec<&str> = "".rsplit('X').collect();
assert_eq!(v, [""]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplit('X').collect();
assert_eq!(v, ["leopard", "tiger", "", "lion"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplit("::").collect();
assert_eq!(v, ["leopard", "tiger", "lion"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".rsplit(|c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "def", "abc"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1800)

Returns an iterator over substrings of the given string slice, separated by characters matched by a pattern.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

Equivalent to [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split"), except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### [§](#iterator-behavior-2)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rsplit_terminator`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplit_terminator "method str::rsplit_terminator") method can be used.

##### [§](#examples-80)Examples

```rust
let v: Vec<&str> = "A.B.".split_terminator('.').collect();
assert_eq!(v, ["A", "B"]);

let v: Vec<&str> = "A..B..".split_terminator(".").collect();
assert_eq!(v, ["A", "", "B", ""]);

let v: Vec<&str> = "A.B:C.D".split_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["A", "B", "C", "D"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1846-1848)

Returns an iterator over substrings of `self`, separated by characters matched by a pattern and yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

Equivalent to [`split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split"), except that the trailing substring is skipped if empty.

This method can be used for string data that is *terminated*, rather than *separated* by a pattern.

##### [§](#iterator-behavior-3)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be double ended if a forward/reverse search yields the same elements.

For iterating from the front, the [`split_terminator`](https://doc.rust-lang.org/std/primitive.str.html#method.split_terminator "method str::split_terminator") method can be used.

##### [§](#examples-81)Examples

```rust
let v: Vec<&str> = "A.B.".rsplit_terminator('.').collect();
assert_eq!(v, ["B", "A"]);

let v: Vec<&str> = "A..B..".rsplit_terminator(".").collect();
assert_eq!(v, ["", "B", "", "A"]);

let v: Vec<&str> = "A.B:C.D".rsplit_terminator(&['.', ':'][..]).collect();
assert_eq!(v, ["D", "C", "B", "A"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1901)

Returns an iterator over substrings of the given string slice, separated by a pattern, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-4)Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

If the pattern allows a reverse search, the [`rsplitn`](https://doc.rust-lang.org/std/primitive.str.html#method.rsplitn "method str::rsplitn") method can be used.

##### [§](#examples-82)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lambda".splitn(3, ' ').collect();
assert_eq!(v, ["Mary", "had", "a little lambda"]);

let v: Vec<&str> = "lionXXtigerXleopard".splitn(3, "X").collect();
assert_eq!(v, ["lion", "", "tigerXleopard"]);

let v: Vec<&str> = "abcXdef".splitn(1, 'X').collect();
assert_eq!(v, ["abcXdef"]);

let v: Vec<&str> = "".splitn(1, 'X').collect();
assert_eq!(v, [""]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".splitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["abc", "defXghi"]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1950-1952)

Returns an iterator over substrings of this string slice, separated by a pattern, starting from the end of the string, restricted to returning at most `n` items.

If `n` substrings are returned, the last substring (the `n`th substring) will contain the remainder of the string.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-5)Iterator behavior

The returned iterator will not be double ended, because it is not efficient to support.

For splitting from the front, the [`splitn`](https://doc.rust-lang.org/std/primitive.str.html#method.splitn "method str::splitn") method can be used.

##### [§](#examples-83)Examples

Simple patterns:

```rust
let v: Vec<&str> = "Mary had a little lamb".rsplitn(3, ' ').collect();
assert_eq!(v, ["lamb", "little", "Mary had a"]);

let v: Vec<&str> = "lionXXtigerXleopard".rsplitn(3, 'X').collect();
assert_eq!(v, ["leopard", "tiger", "lionX"]);

let v: Vec<&str> = "lion::tiger::leopard".rsplitn(2, "::").collect();
assert_eq!(v, ["leopard", "lion::tiger"]);
```

A more complex pattern, using a closure:

```rust
let v: Vec<&str> = "abc1defXghi".rsplitn(2, |c| c == '1' || c == 'X').collect();
assert_eq!(v, ["ghi", "abc1def"]);
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1970)

Splits the string on the first occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### [§](#examples-84)Examples

```rust
assert_eq!("cfg".split_once('='), None);
assert_eq!("cfg=".split_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".split_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".split_once('='), Some(("cfg", "foo=bar")));
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#1989-1991)

Splits the string on the last occurrence of the specified delimiter and returns prefix before delimiter and suffix after delimiter.

##### [§](#examples-85)Examples

```rust
assert_eq!("cfg".rsplit_once('='), None);
assert_eq!("cfg=".rsplit_once('='), Some(("cfg", "")));
assert_eq!("cfg=foo".rsplit_once('='), Some(("cfg", "foo")));
assert_eq!("cfg=foo=bar".rsplit_once('='), Some(("cfg=foo", "bar")));
```

1.2.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2029)

Returns an iterator over the disjoint matches of a pattern within the given string slice.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-6)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rmatches`](https://doc.rust-lang.org/std/primitive.str.html#method.rmatches "method str::rmatches") method can be used.

##### [§](#examples-86)Examples

```rust
let v: Vec<&str> = "abcXXXabcYYYabc".matches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".matches(char::is_numeric).collect();
assert_eq!(v, ["1", "2", "3"]);
```

1.2.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2063-2065)

Returns an iterator over the disjoint matches of a pattern within this string slice, yielded in reverse order.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-7)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`matches`](https://doc.rust-lang.org/std/primitive.str.html#method.matches "method str::matches") method can be used.

##### [§](#examples-87)Examples

```rust
let v: Vec<&str> = "abcXXXabcYYYabc".rmatches("abc").collect();
assert_eq!(v, ["abc", "abc", "abc"]);

let v: Vec<&str> = "1abc2abc3".rmatches(char::is_numeric).collect();
assert_eq!(v, ["3", "2", "1"]);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2107)

Returns an iterator over the disjoint matches of a pattern within this string slice as well as the index that the match starts at.

For matches of `pat` within `self` that overlap, only the indices corresponding to the first match are returned.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-8)Iterator behavior

The returned iterator will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if the pattern allows a reverse search and forward/reverse search yields the same elements. This is true for, e.g., [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), but not for `&str`.

If the pattern allows a reverse search but its results might differ from a forward search, the [`rmatch_indices`](https://doc.rust-lang.org/std/primitive.str.html#method.rmatch_indices "method str::rmatch_indices") method can be used.

##### [§](#examples-88)Examples

```rust
let v: Vec<_> = "abcXXXabcYYYabc".match_indices("abc").collect();
assert_eq!(v, [(0, "abc"), (6, "abc"), (12, "abc")]);

let v: Vec<_> = "1abcabc2".match_indices("abc").collect();
assert_eq!(v, [(1, "abc"), (4, "abc")]);

let v: Vec<_> = "ababa".match_indices("aba").collect();
assert_eq!(v, [(0, "aba")]); // only the first `aba`
```

1.5.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2147-2149)

Returns an iterator over the disjoint matches of a pattern within `self`, yielded in reverse order along with the index of the match.

For matches of `pat` within `self` that overlap, only the indices corresponding to the last match are returned.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#iterator-behavior-9)Iterator behavior

The returned iterator requires that the pattern supports a reverse search, and it will be a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") if a forward/reverse search yields the same elements.

For iterating from the front, the [`match_indices`](https://doc.rust-lang.org/std/primitive.str.html#method.match_indices "method str::match_indices") method can be used.

##### [§](#examples-89)Examples

```rust
let v: Vec<_> = "abcXXXabcYYYabc".rmatch_indices("abc").collect();
assert_eq!(v, [(12, "abc"), (6, "abc"), (0, "abc")]);

let v: Vec<_> = "1abcabc2".rmatch_indices("abc").collect();
assert_eq!(v, [(4, "abc"), (1, "abc")]);

let v: Vec<_> = "ababa".rmatch_indices("aba").collect();
assert_eq!(v, [(2, "aba")]); // only the last `aba`
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2171)

Returns a string slice with leading and trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#examples-90)Examples

```rust
let s = "\n Hello\tworld\t\n";

assert_eq!("Hello\tworld", s.trim());
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2210)

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#text-directionality)Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### [§](#examples-91)Examples

Basic usage:

```rust
let s = "\n Hello\tworld\t\n";
assert_eq!("Hello\tworld\t\n", s.trim_start());
```

Directionality:

```rust
let s = "  English  ";
assert!(Some('E') == s.trim_start().chars().next());

let s = "  עברית  ";
assert!(Some('ע') == s.trim_start().chars().next());
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2249)

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`, which includes newlines.

##### [§](#text-directionality-1)Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### [§](#examples-92)Examples

Basic usage:

```rust
let s = "\n Hello\tworld\t\n";
assert_eq!("\n Hello\tworld", s.trim_end());
```

Directionality:

```rust
let s = "  English  ";
assert!(Some('h') == s.trim_end().chars().rev().next());

let s = "  עברית  ";
assert!(Some('ת') == s.trim_end().chars().rev().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2289)

👎Deprecated since 1.33.0: superseded by `trim_start`

Returns a string slice with leading whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### [§](#text-directionality-2)Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### [§](#examples-93)Examples

Basic usage:

```rust
let s = " Hello\tworld\t";

assert_eq!("Hello\tworld\t", s.trim_left());
```

Directionality:

```rust
let s = "  English";
assert!(Some('E') == s.trim_left().chars().next());

let s = "  עברית";
assert!(Some('ע') == s.trim_left().chars().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2329)

👎Deprecated since 1.33.0: superseded by `trim_end`

Returns a string slice with trailing whitespace removed.

‘Whitespace’ is defined according to the terms of the Unicode Derived Core Property `White_Space`.

##### [§](#text-directionality-3)Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### [§](#examples-94)Examples

Basic usage:

```rust
let s = " Hello\tworld\t";

assert_eq!(" Hello\tworld", s.trim_right());
```

Directionality:

```rust
let s = "English  ";
assert!(Some('h') == s.trim_right().chars().rev().next());

let s = "עברית  ";
assert!(Some('ת') == s.trim_right().chars().rev().next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2362-2364)

Returns a string slice with all prefixes and suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-95)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_matches('1'), "foo1bar");
assert_eq!("123foo1bar123".trim_matches(char::is_numeric), "foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_matches(x), "foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1foo1barXX".trim_matches(|c| c == '1' || c == 'X'), "foo1bar");
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2409)

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-4)Text directionality

A string is a sequence of bytes. `start` in this context means the first position of that byte string; for a left-to-right language like English or Russian, this will be left side, and for right-to-left languages like Arabic or Hebrew, this will be the right side.

##### [§](#examples-96)Examples

```rust
assert_eq!("11foo1bar11".trim_start_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_start_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_start_matches(x), "foo1bar12");
```

1.45.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2443)

Returns a string slice with the prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix, wrapped in `Some`. Unlike [`trim_start_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_start_matches "method str::trim_start_matches"), this method removes the prefix exactly once.

If the string does not start with `prefix`, returns `None`.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-97)Examples

```rust
assert_eq!("foo:bar".strip_prefix("foo:"), Some("bar"));
assert_eq!("foo:bar".strip_prefix("bar"), None);
assert_eq!("foofoo".strip_prefix("foo"), Some("foo"));
```

1.45.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2471-2473)

Returns a string slice with the suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix, wrapped in `Some`. Unlike [`trim_end_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_end_matches "method str::trim_end_matches"), this method removes the suffix exactly once.

If the string does not end with `suffix`, returns `None`.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-98)Examples

```rust
assert_eq!("bar:foo".strip_suffix(":foo"), Some("bar"));
assert_eq!("bar:foo".strip_suffix("bar"), None);
assert_eq!("foofoo".strip_suffix("foo"), Some("foo"));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2507-2509)

🔬This is a nightly-only experimental API. (`strip_circumfix` [#147946](https://github.com/rust-lang/rust/issues/147946))

Returns a string slice with the prefix and suffix removed.

If the string starts with the pattern `prefix` and ends with the pattern `suffix`, returns the substring after the prefix and before the suffix, wrapped in `Some`. Unlike [`trim_start_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_start_matches "method str::trim_start_matches") and [`trim_end_matches`](https://doc.rust-lang.org/std/primitive.str.html#method.trim_end_matches "method str::trim_end_matches"), this method removes both the prefix and suffix exactly once.

If the string does not start with `prefix` or does not end with `suffix`, returns `None`.

Each [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-99)Examples

```rust
#![feature(strip_circumfix)]

assert_eq!("bar:hello:foo".strip_circumfix("bar:", ":foo"), Some("hello"));
assert_eq!("bar:foo".strip_circumfix("foo", "foo"), None);
assert_eq!("foo:bar;".strip_circumfix("foo:", ';'), Some("bar"));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2547)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a string slice with the optional prefix removed.

If the string starts with the pattern `prefix`, returns the substring after the prefix. Unlike [`strip_prefix`](https://doc.rust-lang.org/std/primitive.str.html#method.strip_prefix "method str::strip_prefix"), this method always returns `&str` for easy method chaining, instead of returning [`Option<&str>`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option").

If the string does not start with `prefix`, returns the original string unchanged.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-100)Examples

```rust
#![feature(trim_prefix_suffix)]

// Prefix present - removes it
assert_eq!("foo:bar".trim_prefix("foo:"), "bar");
assert_eq!("foofoo".trim_prefix("foo"), "foo");

// Prefix absent - returns original string
assert_eq!("foo:bar".trim_prefix("bar"), "foo:bar");

// Method chaining example
assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2584-2586)

🔬This is a nightly-only experimental API. (`trim_prefix_suffix` [#142312](https://github.com/rust-lang/rust/issues/142312))

Returns a string slice with the optional suffix removed.

If the string ends with the pattern `suffix`, returns the substring before the suffix. Unlike [`strip_suffix`](https://doc.rust-lang.org/std/primitive.str.html#method.strip_suffix "method str::strip_suffix"), this method always returns `&str` for easy method chaining, instead of returning [`Option<&str>`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option").

If the string does not end with `suffix`, returns the original string unchanged.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#examples-101)Examples

```rust
#![feature(trim_prefix_suffix)]

// Suffix present - removes it
assert_eq!("bar:foo".trim_suffix(":foo"), "bar");
assert_eq!("foofoo".trim_suffix("foo"), "foo");

// Suffix absent - returns original string
assert_eq!("bar:foo".trim_suffix("bar"), "bar:foo");

// Method chaining example
assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2627-2629)

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-5)Text directionality

A string is a sequence of bytes. `end` in this context means the last position of that byte string; for a left-to-right language like English or Russian, this will be right side, and for right-to-left languages like Arabic or Hebrew, this will be the left side.

##### [§](#examples-102)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_end_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_end_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_end_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1fooX".trim_end_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2671)

👎Deprecated since 1.33.0: superseded by `trim_start_matches`

Returns a string slice with all prefixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-6)Text directionality

A string is a sequence of bytes. ‘Left’ in this context means the first position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *right* side, not the left.

##### [§](#examples-103)Examples

```rust
assert_eq!("11foo1bar11".trim_left_matches('1'), "foo1bar11");
assert_eq!("123foo1bar123".trim_left_matches(char::is_numeric), "foo1bar123");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_left_matches(x), "foo1bar12");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2714-2716)

👎Deprecated since 1.33.0: superseded by `trim_end_matches`

Returns a string slice with all suffixes that match a pattern repeatedly removed.

The [pattern](https://doc.rust-lang.org/std/str/pattern/index.html "mod std::str::pattern") can be a `&str`, [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), a slice of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s, or a function or closure that determines if a character matches.

##### [§](#text-directionality-7)Text directionality

A string is a sequence of bytes. ‘Right’ in this context means the last position of that byte string; for a language like Arabic or Hebrew which are ‘right to left’ rather than ‘left to right’, this will be the *left* side, not the right.

##### [§](#examples-104)Examples

Simple patterns:

```rust
assert_eq!("11foo1bar11".trim_right_matches('1'), "11foo1bar");
assert_eq!("123foo1bar123".trim_right_matches(char::is_numeric), "123foo1bar");

let x: &[_] = &['1', '2'];
assert_eq!("12foo1bar12".trim_right_matches(x), "12foo1bar");
```

A more complex pattern, using a closure:

```rust
assert_eq!("1fooX".trim_right_matches(|c| c == '1' || c == 'X'), "1foo");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2765)

Parses this string slice into another type.

Because `parse` is so general, it can cause problems with type inference. As such, `parse` is one of the few times you’ll see the syntax affectionately known as the ‘turbofish’: `::<>`. This helps the inference algorithm understand specifically which type you’re trying to parse into.

`parse` can parse into any type that implements the [`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html "trait std::str::FromStr") trait.

##### [§](#errors-4)Errors

Will return [`Err`](https://doc.rust-lang.org/std/str/trait.FromStr.html#associatedtype.Err "associated type std::str::FromStr::Err") if it’s not possible to parse this string slice into the desired type.

##### [§](#examples-105)Examples

Basic usage:

```rust
let four: u32 = "4".parse().unwrap();

assert_eq!(4, four);
```

Using the ‘turbofish’ instead of annotating `four`:

```rust
let four = "4".parse::<u32>();

assert_eq!(Ok(4), four);
```

Failing to parse:

```rust
let nope = "j".parse::<u32>();

assert!(nope.is_err());
```

1.23.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2786)

Checks if all characters in this string are within the ASCII range.

An empty string returns `true`.

##### [§](#examples-106)Examples

```rust
let ascii = "hello!\n";
let non_ascii = "Grüße, Jürgen ❤";

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2798)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

If this string slice [`is_ascii`](https://doc.rust-lang.org/std/primitive.str.html#method.is_ascii "method str::is_ascii"), returns it as a slice of [ASCII characters](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), otherwise returns `None`.

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2812)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this string slice into a slice of [ASCII characters](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), without checking whether they are valid.

##### [§](#safety-8)Safety

Every character in this string must be ASCII, or else this is UB.

1.23.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2840)

Checks that two strings are an ASCII case-insensitive match.

Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`, but without allocating and copying temporaries.

##### [§](#examples-107)Examples

```rust
assert!("Ferris".eq_ignore_ascii_case("FERRIS"));
assert!("Ferrös".eq_ignore_ascii_case("FERRöS"));
assert!(!"Ferrös".eq_ignore_ascii_case("FERRÖS"));
```

1.23.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2866)

Converts this string to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`to_ascii_uppercase()`](#method.to_ascii_uppercase).

##### [§](#examples-108)Examples

```rust
let mut s = String::from("Grüße, Jürgen ❤");

s.make_ascii_uppercase();

assert_eq!("GRüßE, JüRGEN ❤", s);
```

1.23.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2894)

Converts this string to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`to_ascii_lowercase()`](#method.to_ascii_lowercase).

##### [§](#examples-109)Examples

```rust
let mut s = String::from("GRÜßE, JÜRGEN ❤");

s.make_ascii_lowercase();

assert_eq!("grÜße, jÜrgen ❤", s);
```

1.80.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2919)

Returns a string slice with leading ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-110)Examples

```rust
assert_eq!(" \t \u{3000}hello world\n".trim_ascii_start(), "\u{3000}hello world\n");
assert_eq!("  ".trim_ascii_start(), "");
assert_eq!("".trim_ascii_start(), "");
```

1.80.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2944)

Returns a string slice with trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-111)Examples

```rust
assert_eq!("\r hello world\u{3000}\n ".trim_ascii_end(), "\r hello world\u{3000}");
assert_eq!("  ".trim_ascii_end(), "");
assert_eq!("".trim_ascii_end(), "");
```

1.80.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#2970)

Returns a string slice with leading and trailing ASCII whitespace removed.

‘Whitespace’ refers to the definition used by [`u8::is_ascii_whitespace`](https://doc.rust-lang.org/std/primitive.u8.html#method.is_ascii_whitespace "method u8::is_ascii_whitespace").

##### [§](#examples-112)Examples

```rust
assert_eq!("\r hello world\n ".trim_ascii(), "hello world");
assert_eq!("  ".trim_ascii(), "");
assert_eq!("".trim_ascii(), "");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3013)

Returns an iterator that escapes each char in `self` with [`char::escape_debug`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_debug "method char::escape_debug").

Note: only extended grapheme codepoints that begin the string will be escaped.

##### [§](#examples-113)Examples

As an iterator:

```rust
for c in "❤\n!".escape_debug() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_debug());
```

Both are equivalent to:

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_debug().to_string(), "❤\\n!");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3059)

Returns an iterator that escapes each char in `self` with [`char::escape_default`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_default "method char::escape_default").

##### [§](#examples-114)Examples

As an iterator:

```rust
for c in "❤\n!".escape_default() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_default());
```

Both are equivalent to:

```rust
println!("\\u{{2764}}\\n!");
```

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_default().to_string(), "\\u{2764}\\n!");
```

1.34.0 · [Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3097)

Returns an iterator that escapes each char in `self` with [`char::escape_unicode`](https://doc.rust-lang.org/std/primitive.char.html#method.escape_unicode "method char::escape_unicode").

##### [§](#examples-115)Examples

As an iterator:

```rust
for c in "❤\n!".escape_unicode() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", "❤\n!".escape_unicode());
```

Both are equivalent to:

```rust
println!("\\u{{2764}}\\u{{a}}\\u{{21}}");
```

Using `to_string`:

```rust
assert_eq!("❤\n!".escape_unicode().to_string(), "\\u{2764}\\u{a}\\u{21}");
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3130)

🔬This is a nightly-only experimental API. (`substr_range` [#126769](https://github.com/rust-lang/rust/issues/126769))

Returns the range that a substring points to.

Returns `None` if `substr` does not point within `self`.

Unlike [`str::find`](https://doc.rust-lang.org/std/primitive.str.html#method.find "method str::find"), **this does not search through the string**. Instead, it uses pointer arithmetic to find where in the string `substr` is derived from.

This is useful for extending [`str::split`](https://doc.rust-lang.org/std/primitive.str.html#method.split "method str::split") and similar methods.

Note that this method may return false positives (typically either `Some(0..0)` or `Some(self.len()..self.len())`) if `substr` is a zero-length `str` that points at the beginning or end of another, independent, `str`.

##### [§](#examples-116)Examples

```rust
#![feature(substr_range)]

let data = "a, b, b, a";
let mut iter = data.split(", ").map(|s| data.substr_range(s).unwrap());

assert_eq!(iter.next(), Some(0..1));
assert_eq!(iter.next(), Some(3..4));
assert_eq!(iter.next(), Some(6..7));
assert_eq!(iter.next(), Some(9..10));
```

[Source](https://doc.rust-lang.org/src/core/str/mod.rs.html#3141)

🔬This is a nightly-only experimental API. (`str_as_str` [#130366](https://github.com/rust-lang/rust/issues/130366))

Returns the same string as a string slice `&str`.

This method is redundant when used directly on `&str`, but it helps dereferencing other string-like types to string slices, for example references to `Box<str>` or `Arc<str>`.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#268)

Replaces all matches of a pattern with another string.

`replace` creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"), and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice.

##### [§](#examples-117)Examples

```rust
let s = "this is old";

assert_eq!("this is new", s.replace("old", "new"));
assert_eq!("than an old", s.replace("is", "an"));
```

When the pattern doesn’t match, it returns this string slice as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"):

```rust
let s = "this is old";
assert_eq!(s, s.replace("cookie monster", "little lamb"));
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#323)

Replaces first N matches of a pattern with another string.

`replacen` creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"), and copies the data from this string slice into it. While doing so, it attempts to find matches of a pattern. If it finds any, it replaces them with the replacement string slice at most `count` times.

##### [§](#examples-118)Examples

```rust
let s = "foo foo 123 foo";
assert_eq!("new new 123 foo", s.replacen("foo", "new", 2));
assert_eq!("faa fao 123 foo", s.replacen('o', "a", 3));
assert_eq!("foo foo new23 foo", s.replacen(char::is_numeric, "new", 1));
```

When the pattern doesn’t match, it returns this string slice as [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"):

```rust
let s = "this is old";
assert_eq!(s, s.replacen("cookie monster", "little lamb", 10));
```

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#380)

Returns the lowercase equivalent of this string slice, as a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

‘Lowercase’ is defined according to the terms of the Unicode Derived Core Property `Lowercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") instead of modifying the parameter in-place.

##### [§](#examples-119)Examples

Basic usage:

```rust
let s = "HELLO";

assert_eq!("hello", s.to_lowercase());
```

A tricky example, with sigma:

```rust
let sigma = "Σ";

assert_eq!("σ", sigma.to_lowercase());

// but at the end of a word, it's ς, not σ:
let odysseus = "ὈΔΥΣΣΕΎΣ";

assert_eq!("ὀδυσσεύς", odysseus.to_lowercase());
```

Languages without case are not changed:

```rust
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_lowercase());
```

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#465)

Returns the uppercase equivalent of this string slice, as a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

‘Uppercase’ is defined according to the terms of the Unicode Derived Core Property `Uppercase`.

Since some characters can expand into multiple characters when changing the case, this function returns a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") instead of modifying the parameter in-place.

##### [§](#examples-120)Examples

Basic usage:

```rust
let s = "hello";

assert_eq!("HELLO", s.to_uppercase());
```

Scripts without case are not changed:

```rust
let new_year = "农历新年";

assert_eq!(new_year, new_year.to_uppercase());
```

One character can become multiple:

```rust
let s = "tschüß";

assert_eq!("TSCHÜSS", s.to_uppercase());
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#529)

Creates a new [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") by repeating a string `n` times.

##### [§](#panics-15)Panics

This function will panic if the capacity would overflow.

##### [§](#examples-121)Examples

Basic usage:

```rust
assert_eq!("abc".repeat(4), String::from("abcabcabcabc"));
```

A panic upon overflow:

[ⓘ](# "This example panics")

```rust
// this will panic at runtime
let huge = "0123456789abcdef".repeat(usize::MAX);
```

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#559)

Returns a copy of this string where each character is mapped to its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`make_ascii_uppercase`](https://doc.rust-lang.org/std/primitive.str.html#method.make_ascii_uppercase "method str::make_ascii_uppercase").

To uppercase ASCII characters in addition to non-ASCII characters, use [`to_uppercase`](#method.to_uppercase).

##### [§](#examples-122)Examples

```rust
let s = "Grüße, Jürgen ❤";

assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
```

1.23.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#591)

Returns a copy of this string where each character is mapped to its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`make_ascii_lowercase`](https://doc.rust-lang.org/std/primitive.str.html#method.make_ascii_lowercase "method str::make_ascii_lowercase").

To lowercase ASCII characters in addition to non-ASCII characters, use [`to_lowercase`](#method.to_lowercase).

##### [§](#examples-123)Examples

```rust
let s = "Grüße, Jürgen ❤";

assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2771)[§](#impl-Add%3C%26str%3E-for-String)

Implements the `+` operator for concatenating two strings.

This consumes the `String` on the left-hand side and re-uses its buffer (growing it if necessary). This is done to avoid allocating a new `String` and copying the entire contents on every operation, which would lead to *O*(*n*^2) running time when building an *n*-byte string by repeated concatenation.

The string on the right-hand side is only borrowed; its contents are copied into the returned `String`.

#### [§](#examples-124)Examples

Concatenating two `String`s takes the first by value and borrows the second:

```rust
let a = String::from("hello");
let b = String::from(" world");
let c = a + &b;
// `a` is moved and can no longer be used here.
```

If you want to keep using the first `String`, you can clone it and append to the clone instead:

```rust
let a = String::from("hello");
let b = String::from(" world");
let c = a.clone() + &b;
// `a` is still valid here.
```

Concatenating `&str` slices can be done by converting the first to a `String`:

```rust
let a = "hello";
let b = " world";
let c = a.to_string() + b;
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2772)[§](#associatedtype.Output)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2775)[§](#method.add)

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2786)[§](#impl-AddAssign%3C%26str%3E-for-String)

Implements the `+=` operator for appending to a `String`.

This has the same behavior as the [`push_str`](https://doc.rust-lang.org/std/string/struct.String.html#method.push_str "method std::string::String::push_str") method.

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3091)[§](#impl-AsMut%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3093)[§](#method.as_mut)

Converts this type into a mutable reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3099)[§](#impl-AsRef%3C%5Bu8%5D%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3101)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1724-1729)[§](#impl-AsRef%3COsStr%3E-for-String)

[Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1726-1728)[§](#method.as_ref-2)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3808-3813)[§](#impl-AsRef%3CPath%3E-for-String)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3810-3812)[§](#method.as_ref-3)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3083)[§](#impl-AsRef%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3085)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#189)[§](#impl-Borrow%3Cstr%3E-for-String)

1.36.0 · [Source](https://doc.rust-lang.org/src/alloc/str.rs.html#197)[§](#impl-BorrowMut%3Cstr%3E-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2350)[§](#impl-Clone-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2359)[§](#method.clone_from)

Clones the contents of `source` into `self`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2351)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2717)[§](#impl-Debug-for-String)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2700)[§](#impl-Default-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2818)[§](#impl-Deref-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2819)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2822)[§](#method.deref)

Dereferences the value.

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2831)[§](#impl-DerefMut-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2833)[§](#method.deref_mut)

Mutably dereferences the value.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2709)[§](#impl-Display-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2593)[§](#impl-Extend%3C%26Char%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2595)[§](#method.extend-7)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2600)[§](#method.extend_one-7)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-7)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2488)[§](#impl-Extend%3C%26char%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2489)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2494)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2499)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2506)[§](#impl-Extend%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2507)[§](#method.extend-2)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2512)[§](#method.extend_one-2)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-2)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2545)[§](#impl-Extend%3CBox%3Cstr,+A%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2546)[§](#method.extend-3)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one-3)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-3)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2579)[§](#impl-Extend%3CChar%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2581)[§](#method.extend-6)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2586)[§](#method.extend_one-6)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-6)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2566)[§](#impl-Extend%3CCow%3C'a,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2567)[§](#method.extend-5)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2572)[§](#method.extend_one-5)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-5)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2553)[§](#impl-Extend%3CString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2554)[§](#method.extend-4)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2559)[§](#method.extend_one-4)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-4)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2467)[§](#impl-Extend%3Cchar%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2468)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2476)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2481)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3251)[§](#impl-From%3C%26String%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3266)[§](#method.from-10)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") reference into a [`Borrowed`](https://doc.rust-lang.org/std/borrow/enum.Cow.html#variant.Borrowed "borrow::Cow::Borrowed") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-3)Example

```rust
let s = "eggplant".to_string();
assert_eq!(Cow::from(&s), Cow::Borrowed("eggplant"));
```

1.35.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3132)[§](#impl-From%3C%26String%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3137)[§](#method.from-5)

Converts a `&String` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

This clones `s` and returns the clone.

1.44.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3120)[§](#impl-From%3C%26mut+str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3125)[§](#method.from-4)

Converts a `&mut str` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

The result is allocated on the heap.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3108)[§](#impl-From%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3113)[§](#method.from-3)

Converts a `&str` into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

The result is allocated on the heap.

1.18.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3144)[§](#impl-From%3CBox%3Cstr%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3157)[§](#method.from-6)

Converts the given boxed `str` slice to a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String"). It is notable that the `str` slice is owned.

##### [§](#examples-127)Examples

```rust
let s1: String = String::from("hello world");
let s2: Box<str> = s1.into_boxed_str();
let s3: String = String::from(s2);

assert_eq!("hello world", s3)
```

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3183)[§](#impl-From%3CCow%3C'a,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3200)[§](#method.from-8)

Converts a clone-on-write string to an owned instance of [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String").

This extracts the owned string, clones the string if it is not already owned.

##### [§](#example-1)Example

```rust
// If the string is not owned...
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
// It will allocate on the heap and copy the string.
let owned: String = String::from(cow);
assert_eq!(&owned[..], "eggplant");
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3969)[§](#impl-From%3CString%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3981)[§](#method.from-13)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-5)Example

```rust
let unique: String = "eggplant".to_owned();
let shared: Arc<str> = Arc::from(unique);
assert_eq!("eggplant", &shared[..]);
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#601)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#613)[§](#method.from-1)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-126)Examples

```rust
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error>::from(a_string_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#563)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#577)[§](#method.from)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-125)Examples

```rust
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_string_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3164)[§](#impl-From%3CString%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3176)[§](#method.from-7)

Converts the given [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") to a boxed `str` slice that is owned.

##### [§](#examples-128)Examples

```rust
let s1: String = String::from("hello world");
let s2: Box<str> = Box::from(s1);
let s3: String = String::from(s2);

assert_eq!("hello world", s3)
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3228)[§](#impl-From%3CString%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3244)[§](#method.from-9)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") into an [`Owned`](https://doc.rust-lang.org/std/borrow/enum.Cow.html#variant.Owned "borrow::Cow::Owned") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-2)Example

```rust
let s = "eggplant".to_string();
let s2 = "eggplant".to_string();
assert_eq!(Cow::from(s), Cow::<'static, str>::Owned(s2));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#609-617)[§](#impl-From%3CString%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1987-1995)[§](#impl-From%3CString%3E-for-PathBuf)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2935)[§](#impl-From%3CString%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2947)[§](#method.from-2)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example)Example

```rust
let original: String = "statue".to_owned();
let shared: Rc<str> = Rc::from(original);
assert_eq!("statue", &shared[..]);
```

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3304)[§](#impl-From%3CString%3E-for-Vec%3Cu8%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3317)[§](#method.from-11)

Converts the given [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") to a vector [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") that holds values of type [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8").

##### [§](#examples-129)Examples

```rust
let s1 = String::from("hello world");
let v1 = Vec::from(s1);

for b in v1 {
    println!("{b}");
}
```

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3593)[§](#impl-From%3Cchar%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3603)[§](#method.from-12)

Allocates an owned [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") from a single character.

##### [§](#example-4)Example

```rust
let c: char = 'a';
let s: String = String::from(c);
assert_eq!("a", &s[..]);
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2456)[§](#impl-FromIterator%3C%26Char%3E-for-String)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2376)[§](#impl-FromIterator%3C%26char%3E-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2386)[§](#impl-FromIterator%3C%26str%3E-for-String)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2415)[§](#impl-FromIterator%3CBox%3Cstr,+A%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2445)[§](#impl-FromIterator%3CChar%3E-for-String)

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2425)[§](#impl-FromIterator%3CCow%3C'a,+str%3E%3E-for-String)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#174)[§](#impl-FromIterator%3CString%3E-for-Box%3Cstr%3E)

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3289)[§](#impl-FromIterator%3CString%3E-for-Cow%3C'a,+str%3E)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2396)[§](#impl-FromIterator%3CString%3E-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2366)[§](#impl-FromIterator%3Cchar%3E-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2848)[§](#impl-FromStr-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2849)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2851)[§](#method.from_str)

Parses a string `s` to return a value of this type. [Read more](https://doc.rust-lang.org/std/str/trait.FromStr.html#tymethod.from_str)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2725)[§](#impl-Hash-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2794-2796)[§](#impl-Index%3CI%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2798)[§](#associatedtype.Output-1)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2801)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2807-2809)[§](#impl-IndexMut%3CI%3E-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#impl-Ord-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#impl-PartialEq%3C%26str%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#665)[§](#impl-PartialEq%3CByteStr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#665)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#525)[§](#impl-PartialEq%3CByteString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#525)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3683-3688)[§](#impl-PartialEq%3CPath%3E-for-String)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3685-3687)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2248-2253)[§](#impl-PartialEq%3CPathBuf%3E-for-String)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#2250-2252)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#impl-PartialEq%3CString%3E-for-%26str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2690)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#665)[§](#impl-PartialEq%3CString%3E-for-ByteStr)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#665)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#525)[§](#impl-PartialEq%3CString%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#525)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#impl-PartialEq%3CString%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2696)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#3675-3680)[§](#impl-PartialEq%3CString%3E-for-Path)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#3677-3679)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.91.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2240-2245)[§](#impl-PartialEq%3CString%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/std/path.rs.html#2242-2244)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#impl-PartialEq%3CString%3E-for-str)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#impl-PartialEq%3Cstr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2689)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#impl-PartialEq-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#impl-PartialOrd-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2617)[§](#impl-Pattern-for-%26String)

A convenience impl that delegates to the impl for `&str`.

#### [§](#examples-131)Examples

```rust
assert_eq!(String::from("Hello world").find("world"), Some(6));
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2618)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2620)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2625)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2630)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2635)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2640-2642)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2648-2650)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2656)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

1.16.0 · [Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#263-268)[§](#impl-ToSocketAddrs-for-String)

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#264)[§](#associatedtype.Iter)

Returned iterator over socket addresses which this type may correspond to.

[Source](https://doc.rust-lang.org/src/std/net/socket_addr.rs.html#265-267)[§](#method.to_socket_addrs)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#671)[§](#impl-TryFrom%3C%26ByteStr%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#672)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#675)[§](#method.try_from-1)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#567)[§](#impl-TryFrom%3CByteString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#568)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#571)[§](#method.try_from)

Performs the conversion.

1.85.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#841)[§](#impl-TryFrom%3CCString%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#848)[§](#method.try_from-2)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#842)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.87.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3323)[§](#impl-TryFrom%3CVec%3Cu8%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3335)[§](#method.try_from-3)

Converts the given [`Vec<u8>`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") into a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") if it contains valid UTF-8 data.

##### [§](#examples-130)Examples

```rust
let s1 = b"hello world".to_vec();
let v1 = String::try_from(s1).unwrap();
assert_eq!(v1, "hello world");
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3324)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3342)[§](#impl-Write-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2828)[§](#impl-DerefPure-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#impl-Eq-for-String)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#350)[§](#impl-StructuralPartialEq-for-String)

[§](#impl-Freeze-for-String)

[§](#impl-RefUnwindSafe-for-String)

[§](#impl-Send-for-String)

[§](#impl-Sync-for-String)

[§](#impl-Unpin-for-String)

[§](#impl-UnsafeUnpin-for-String)

[§](#impl-UnwindSafe-for-String)