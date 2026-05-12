---
title: char - Rust
url: https://doc.rust-lang.org/std/primitive.char.html
source: crawler
fetched_at: 2026-05-06T21:22:03.803363798-03:00
rendered_js: false
word_count: 4443
summary: This document describes the Rust primitive 'char' type, which represents a Unicode scalar value, covering its memory layout, validity requirements, and relationship to Unicode standards.
tags:
    - rust
    - primitive-type
    - unicode
    - character
    - data-layout
    - utf-8
category: reference
---

## Primitive Type char

1.0.0

Expand description

A character type.

The `char` type represents a single character. More specifically, since ‘character’ isn’t a well-defined concept in Unicode, `char` is a ‘[Unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value)’.

This documentation describes a number of methods and trait implementations on the `char` type. For technical reasons, there is additional, separate documentation in [the `std::char` module](https://doc.rust-lang.org/std/char/index.html) as well.

## [§](#validity-and-layout)Validity and Layout

A `char` is a ‘[Unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value)’, which is any ‘[Unicode code point](https://www.unicode.org/glossary/#code_point)’ other than a [surrogate code point](https://www.unicode.org/glossary/#surrogate_code_point). This has a fixed numerical definition: code points are in the range 0 to 0x10FFFF, inclusive. Surrogate code points, used by UTF-16, are in the range 0xD800 to 0xDFFF.

No `char` may be constructed, whether as a literal or at runtime, that is not a Unicode scalar value. Violating this rule causes undefined behavior.

[ⓘ](# "This example deliberately fails to compile")

```rust
// Each of these is a compiler error
['\u{D800}', '\u{DFFF}', '\u{110000}'];
```

[ⓘ](# "This example panics")

```rust
// Panics; from_u32 returns None.
char::from_u32(0xDE01).unwrap();
```

```rust
// Undefined behavior
let _ = unsafe { char::from_u32_unchecked(0x110000) };
```

Unicode scalar values are also the exact set of values that may be encoded in UTF-8. Because `char` values are Unicode scalar values and functions may assume [incoming `str` values are valid UTF-8](https://doc.rust-lang.org/std/primitive.str.html#invariant), it is safe to store any `char` in a `str` or read any character from a `str` as a `char`.

The gap in valid `char` values is understood by the compiler, so in the below example the two ranges are understood to cover the whole range of possible `char` values and there is no error for a [non-exhaustive match](https://doc.rust-lang.org/book/ch06-02-match.html#matches-are-exhaustive).

```rust
let c: char = 'a';
match c {
    '\0' ..= '\u{D7FF}' => false,
    '\u{E000}' ..= '\u{10FFFF}' => true,
};
```

All Unicode scalar values are valid `char` values, but not all of them represent a real character. Many Unicode scalar values are not currently assigned to a character, but may be in the future (“reserved”); some will never be a character (“noncharacters”); and some may be given different meanings by different users (“private use”).

`char` is guaranteed to have the same size, alignment, and function call ABI as `u32` on all platforms.

```rust
use std::alloc::Layout;
assert_eq!(Layout::new::<char>(), Layout::new::<u32>());
```

## [§](#representation)Representation

`char` is always four bytes in size. This is a different representation than a given character would have as part of a [`String`](https://doc.rust-lang.org/std/string/struct.String.html). For example:

```rust
let v = vec!['h', 'e', 'l', 'l', 'o'];

// five elements times four bytes for each element
assert_eq!(20, v.len() * size_of::<char>());

let s = String::from("hello");

// five elements times one byte per element
assert_eq!(5, s.len() * size_of::<u8>());
```

As always, remember that a human intuition for ‘character’ might not map to Unicode’s definitions. For example, despite looking similar, the ‘é’ character is one Unicode code point while ‘é’ is two Unicode code points:

```rust
let mut chars = "é".chars();
// U+00e9: 'latin small letter e with acute'
assert_eq!(Some('\u{00e9}'), chars.next());
assert_eq!(None, chars.next());

let mut chars = "é".chars();
// U+0065: 'latin small letter e'
assert_eq!(Some('\u{0065}'), chars.next());
// U+0301: 'combining acute accent'
assert_eq!(Some('\u{0301}'), chars.next());
assert_eq!(None, chars.next());
```

This means that the contents of the first string above *will* fit into a `char` while the contents of the second string *will not*. Trying to create a `char` literal with the contents of the second string gives an error:

```text
error: character literal may only contain one codepoint: 'é'
let c = 'é';
        ^^^
```

Another implication of the 4-byte fixed size of a `char` is that per-`char` processing can end up using a lot more memory:

```rust
let s = String::from("love: ❤️");
let v: Vec<char> = s.chars().collect();

assert_eq!(12, size_of_val(&s[..]));
assert_eq!(32, size_of_val(&v[..]));
```

[Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#11)[§](#impl-char)

1.83.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#41)

The lowest valid code point a `char` can have, `'\0'`.

Unlike integer types, `char` actually has a gap in the middle, meaning that the range of possible `char`s is smaller than you might expect. Ranges of `char` will automatically hop this gap for you:

```rust
let dist = u32::from(char::MAX) - u32::from(char::MIN);
let size = (char::MIN..=char::MAX).count() as u32;
assert!(size < dist);
```

Despite this gap, the `MIN` and [`MAX`](https://doc.rust-lang.org/std/primitive.char.html#associatedconstant.MAX "associated constant char::MAX") values can be used as bounds for all `char` values.

##### [§](#examples)Examples

```rust
let c: char = something_which_returns_char();
assert!(char::MIN <= c);

let value_at_min = u32::from(char::MIN);
assert_eq!(char::from_u32(value_at_min), Some('\0'));
```

1.52.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#73)

The highest valid code point a `char` can have, `'\u{10FFFF}'`.

Unlike integer types, `char` actually has a gap in the middle, meaning that the range of possible `char`s is smaller than you might expect. Ranges of `char` will automatically hop this gap for you:

```rust
let dist = u32::from(char::MAX) - u32::from(char::MIN);
let size = (char::MIN..=char::MAX).count() as u32;
assert!(size < dist);
```

Despite this gap, the [`MIN`](https://doc.rust-lang.org/std/primitive.char.html#associatedconstant.MIN "associated constant char::MIN") and `MAX` values can be used as bounds for all `char` values.

##### [§](#examples-1)Examples

```rust
let c: char = something_which_returns_char();
assert!(c <= char::MAX);

let value_at_max = u32::from(char::MAX);
assert_eq!(char::from_u32(value_at_max), Some('\u{10FFFF}'));
assert_eq!(char::from_u32(value_at_max + 1), None);
```

1.93.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#78)

The maximum number of bytes required to [encode](https://doc.rust-lang.org/std/primitive.char.html#method.encode_utf8 "method char::encode_utf8") a `char` to UTF-8 encoding.

1.93.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#83)

The maximum number of two-byte units required to [encode](https://doc.rust-lang.org/std/primitive.char.html#method.encode_utf16 "method char::encode_utf16") a `char` to UTF-16 encoding.

1.52.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#91)

`U+FFFD REPLACEMENT CHARACTER` (�) is used in Unicode to represent a decoding error.

It can occur, for example, when giving ill-formed UTF-8 bytes to [`String::from_utf8_lossy`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy).

1.52.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#104)

The version of [Unicode](https://www.unicode.org/) that the Unicode parts of `char` and `str` methods are based on.

New versions of Unicode are released regularly and subsequently all methods in the standard library depending on Unicode are updated. Therefore the behavior of some `char` and `str` methods and the value of this constant changes over time. This is *not* considered to be a breaking change.

The version numbering scheme is explained in [Unicode 11.0 or later, Section 3.1 Versions of the Unicode Standard](https://www.unicode.org/versions/Unicode11.0.0/ch03.pdf#page=4).

1.52.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#150)

Creates an iterator over the native endian UTF-16 encoded code points in `iter`, returning unpaired surrogates as `Err`s.

##### [§](#examples-2)Examples

Basic usage:

```rust
// 𝄞mus<invalid>ic<invalid>
let v = [
    0xD834, 0xDD1E, 0x006d, 0x0075, 0x0073, 0xDD1E, 0x0069, 0x0063, 0xD834,
];

assert_eq!(
    char::decode_utf16(v)
        .map(|r| r.map_err(|e| e.unpaired_surrogate()))
        .collect::<Vec<_>>(),
    vec![
        Ok('𝄞'),
        Ok('m'), Ok('u'), Ok('s'),
        Err(0xDD1E),
        Ok('i'), Ok('c'),
        Err(0xD834)
    ]
);
```

A lossy decoder can be obtained by replacing `Err` results with the replacement character:

```rust
// 𝄞mus<invalid>ic<invalid>
let v = [
    0xD834, 0xDD1E, 0x006d, 0x0075, 0x0073, 0xDD1E, 0x0069, 0x0063, 0xD834,
];

assert_eq!(
    char::decode_utf16(v)
       .map(|r| r.unwrap_or(char::REPLACEMENT_CHARACTER))
       .collect::<String>(),
    "𝄞mus�ic�"
);
```

1.52.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#196)

Converts a `u32` to a `char`.

Note that all `char`s are valid [`u32`](https://doc.rust-lang.org/std/primitive.u32.html "primitive u32")s, and can be cast to one with [`as`](https://doc.rust-lang.org/std/keyword.as.html):

```rust
let c = '💯';
let i = c as u32;

assert_eq!(128175, i);
```

However, the reverse is not true: not all valid [`u32`](https://doc.rust-lang.org/std/primitive.u32.html "primitive u32")s are valid `char`s. `from_u32()` will return `None` if the input is not a valid value for a `char`.

For an unsafe version of this function which ignores these checks, see [`from_u32_unchecked`](#method.from_u32_unchecked).

##### [§](#examples-3)Examples

Basic usage:

```rust
let c = char::from_u32(0x2764);

assert_eq!(Some('❤'), c);
```

Returning `None` when the input is not a valid `char`:

```rust
let c = char::from_u32(0x110000);

assert_eq!(None, c);
```

1.52.0 (const: 1.81.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#237)

Converts a `u32` to a `char`, ignoring validity.

Note that all `char`s are valid [`u32`](https://doc.rust-lang.org/std/primitive.u32.html "primitive u32")s, and can be cast to one with `as`:

```rust
let c = '💯';
let i = c as u32;

assert_eq!(128175, i);
```

However, the reverse is not true: not all valid [`u32`](https://doc.rust-lang.org/std/primitive.u32.html "primitive u32")s are valid `char`s. `from_u32_unchecked()` will ignore this, and blindly cast to `char`, possibly creating an invalid one.

##### [§](#safety)Safety

This function is unsafe, as it may construct invalid `char` values.

For a safe version of this function, see the [`from_u32`](#method.from_u32) function.

##### [§](#examples-4)Examples

Basic usage:

```rust
let c = unsafe { char::from_u32_unchecked(0x2764) };

assert_eq!('❤', c);
```

1.52.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#289)

Converts a digit in the given radix to a `char`.

A ‘radix’ here is sometimes also called a ‘base’. A radix of two indicates a binary number, a radix of ten, decimal, and a radix of sixteen, hexadecimal, to give some common values. Arbitrary radices are supported.

`from_digit()` will return `None` if the input is not a digit in the given radix.

##### [§](#panics)Panics

Panics if given a radix larger than 36.

##### [§](#examples-5)Examples

Basic usage:

```rust
let c = char::from_digit(4, 10);

assert_eq!(Some('4'), c);

// Decimal 11 is a single digit in base 16
let c = char::from_digit(11, 16);

assert_eq!(Some('b'), c);
```

Returning `None` when the input is not a digit:

```rust
let c = char::from_digit(20, 10);

assert_eq!(None, c);
```

Passing a large radix, causing a panic:

[ⓘ](# "This example panics")

```rust
// this panics
let _c = char::from_digit(1, 37);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#343)

Checks if a `char` is a digit in the given radix.

A ‘radix’ here is sometimes also called a ‘base’. A radix of two indicates a binary number, a radix of ten, decimal, and a radix of sixteen, hexadecimal, to give some common values. Arbitrary radices are supported.

Compared to [`is_numeric()`](#method.is_numeric), this function only recognizes the characters `0-9`, `a-z` and `A-Z`.

‘Digit’ is defined to be only the following characters:

- `0-9`
- `a-z`
- `A-Z`

For a more comprehensive understanding of ‘digit’, see [`is_numeric()`](#method.is_numeric).

##### [§](#panics-1)Panics

Panics if given a radix smaller than 2 or larger than 36.

##### [§](#examples-6)Examples

Basic usage:

```rust
assert!('1'.is_digit(10));
assert!('f'.is_digit(16));
assert!(!'f'.is_digit(10));
```

Passing a large radix, causing a panic:

[ⓘ](# "This example panics")

```rust
// this panics
'1'.is_digit(37);
```

Passing a small radix, causing a panic:

[ⓘ](# "This example panics")

```rust
// this panics
'1'.is_digit(1);
```

1.0.0 (const: 1.67.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#402)

Converts a `char` to a digit in the given radix.

A ‘radix’ here is sometimes also called a ‘base’. A radix of two indicates a binary number, a radix of ten, decimal, and a radix of sixteen, hexadecimal, to give some common values. Arbitrary radices are supported.

‘Digit’ is defined to be only the following characters:

- `0-9`
- `a-z`
- `A-Z`

##### [§](#errors)Errors

Returns `None` if the `char` does not refer to a digit in the given radix.

##### [§](#panics-2)Panics

Panics if given a radix smaller than 2 or larger than 36.

##### [§](#examples-7)Examples

Basic usage:

```rust
assert_eq!('1'.to_digit(10), Some(1));
assert_eq!('f'.to_digit(16), Some(15));
```

Passing a non-digit results in failure:

```rust
assert_eq!('f'.to_digit(10), None);
assert_eq!('z'.to_digit(16), None);
```

Passing a large radix, causing a panic:

[ⓘ](# "This example panics")

```rust
// this panics
let _ = '1'.to_digit(37);
```

Passing a small radix, causing a panic:

[ⓘ](# "This example panics")

```rust
// this panics
let _ = '1'.to_digit(1);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#464)

Returns an iterator that yields the hexadecimal Unicode escape of a character as `char`s.

This will escape characters with the Rust syntax of the form `\u{NNNNNN}` where `NNNNNN` is a hexadecimal representation.

##### [§](#examples-8)Examples

As an iterator:

```rust
for c in '❤'.escape_unicode() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", '❤'.escape_unicode());
```

Both are equivalent to:

Using [`to_string`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string):

```rust
assert_eq!('❤'.escape_unicode().to_string(), "\\u{2764}");
```

1.20.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#529)

Returns an iterator that yields the literal escape code of a character as `char`s.

This will escape the characters similar to the [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") implementations of `str` or `char`.

##### [§](#examples-9)Examples

As an iterator:

```rust
for c in '\n'.escape_debug() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", '\n'.escape_debug());
```

Both are equivalent to:

Using [`to_string`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string):

```rust
assert_eq!('\n'.escape_debug().to_string(), "\\n");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#585)

Returns an iterator that yields the literal escape code of a character as `char`s.

The default is chosen with a bias toward producing literals that are legal in a variety of languages, including C++11 and similar C-family languages. The exact rules are:

- Tab is escaped as `\t`.
- Carriage return is escaped as `\r`.
- Line feed is escaped as `\n`.
- Single quote is escaped as `\'`.
- Double quote is escaped as `\"`.
- Backslash is escaped as `\\`.
- Any character in the ‘printable ASCII’ range `0x20` .. `0x7e` inclusive is not escaped.
- All other characters are given hexadecimal Unicode escapes; see [`escape_unicode`](#method.escape_unicode).

##### [§](#examples-10)Examples

As an iterator:

```rust
for c in '"'.escape_default() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", '"'.escape_default());
```

Both are equivalent to:

Using [`to_string`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string):

```rust
assert_eq!('"'.escape_default().to_string(), "\\\"");
```

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#645)

Returns the number of bytes this `char` would need if encoded in UTF-8.

That number of bytes is always between 1 and 4, inclusive.

##### [§](#examples-11)Examples

Basic usage:

```rust
let len = 'A'.len_utf8();
assert_eq!(len, 1);

let len = 'ß'.len_utf8();
assert_eq!(len, 2);

let len = 'ℝ'.len_utf8();
assert_eq!(len, 3);

let len = '💣'.len_utf8();
assert_eq!(len, 4);
```

The `&str` type guarantees that its contents are UTF-8, and so we can compare the length it would take if each code point was represented as a `char` vs in the `&str` itself:

```rust
// as chars
let eastern = '東';
let capital = '京';

// both can be represented as three bytes
assert_eq!(3, eastern.len_utf8());
assert_eq!(3, capital.len_utf8());

// as a &str, these two are encoded in UTF-8
let tokyo = "東京";

let len = eastern.len_utf8() + capital.len_utf8();

// we can see that they take six bytes total...
assert_eq!(6, tokyo.len());

// ... just like the &str
assert_eq!(len, tokyo.len());
```

1.0.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#677)

Returns the number of 16-bit code units this `char` would need if encoded in UTF-16.

That number of code units is always either 1 or 2, for unicode scalar values in the [basic multilingual plane](http://www.unicode.org/glossary/#basic_multilingual_plane) or [supplementary planes](http://www.unicode.org/glossary/#supplementary_planes) respectively.

See the documentation for [`len_utf8()`](#method.len_utf8) for more explanation of this concept. This function is a mirror, but for UTF-16 instead of UTF-8.

##### [§](#examples-12)Examples

Basic usage:

```rust
let n = 'ß'.len_utf16();
assert_eq!(n, 1);

let len = '💣'.len_utf16();
assert_eq!(len, 2);
```

1.15.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#714)

Encodes this character as UTF-8 into the provided byte buffer, and then returns the subslice of the buffer that contains the encoded character.

##### [§](#panics-3)Panics

Panics if the buffer is not large enough. A buffer of length four is large enough to encode any `char`.

##### [§](#examples-13)Examples

In both of these examples, ‘ß’ takes two bytes to encode.

```rust
let mut b = [0; 2];

let result = 'ß'.encode_utf8(&mut b);

assert_eq!(result, "ß");

assert_eq!(result.len(), 2);
```

A buffer that’s too small:

[ⓘ](# "This example panics")

```rust
let mut b = [0; 1];

// this panics
'ß'.encode_utf8(&mut b);
```

1.15.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#750)

Encodes this character as native endian UTF-16 into the provided `u16` buffer, and then returns the subslice of the buffer that contains the encoded character.

##### [§](#panics-4)Panics

Panics if the buffer is not large enough. A buffer of length 2 is large enough to encode any `char`.

##### [§](#examples-14)Examples

In both of these examples, ‘𝕊’ takes two `u16`s to encode.

```rust
let mut b = [0; 2];

let result = '𝕊'.encode_utf16(&mut b);

assert_eq!(result.len(), 2);
```

A buffer that’s too small:

[ⓘ](# "This example panics")

```rust
let mut b = [0; 1];

// this panics
'𝕊'.encode_utf16(&mut b);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#778)

Returns `true` if this `char` has the `Alphabetic` property.

`Alphabetic` is described in Chapter 4 (Character Properties) of the [Unicode Standard](https://www.unicode.org/versions/latest/) and specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`DerivedCoreProperties.txt`](https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt).

##### [§](#examples-15)Examples

Basic usage:

```rust
assert!('a'.is_alphabetic());
assert!('京'.is_alphabetic());

let c = '💝';
// love is many things, but it is not alphabetic
assert!(!c.is_alphabetic());
```

1.0.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#819)

Returns `true` if this `char` has the `Lowercase` property.

`Lowercase` is described in Chapter 4 (Character Properties) of the [Unicode Standard](https://www.unicode.org/versions/latest/) and specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`DerivedCoreProperties.txt`](https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt).

##### [§](#examples-16)Examples

Basic usage:

```rust
assert!('a'.is_lowercase());
assert!('δ'.is_lowercase());
assert!(!'A'.is_lowercase());
assert!(!'Δ'.is_lowercase());

// The various Chinese scripts and punctuation do not have case, and so:
assert!(!'中'.is_lowercase());
assert!(!' '.is_lowercase());
```

In a const context:

```rust
const CAPITAL_DELTA_IS_LOWERCASE: bool = 'Δ'.is_lowercase();
assert!(!CAPITAL_DELTA_IS_LOWERCASE);
```

1.0.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#860)

Returns `true` if this `char` has the `Uppercase` property.

`Uppercase` is described in Chapter 4 (Character Properties) of the [Unicode Standard](https://www.unicode.org/versions/latest/) and specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`DerivedCoreProperties.txt`](https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt).

##### [§](#examples-17)Examples

Basic usage:

```rust
assert!(!'a'.is_uppercase());
assert!(!'δ'.is_uppercase());
assert!('A'.is_uppercase());
assert!('Δ'.is_uppercase());

// The various Chinese scripts and punctuation do not have case, and so:
assert!(!'中'.is_uppercase());
assert!(!' '.is_uppercase());
```

In a const context:

```rust
const CAPITAL_DELTA_IS_UPPERCASE: bool = 'Δ'.is_uppercase();
assert!(CAPITAL_DELTA_IS_UPPERCASE);
```

1.0.0 (const: 1.87.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#893)

Returns `true` if this `char` has the `White_Space` property.

`White_Space` is specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`PropList.txt`](https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt).

##### [§](#examples-18)Examples

Basic usage:

```rust
assert!(' '.is_whitespace());

// line break
assert!('\n'.is_whitespace());

// a non-breaking space
assert!('\u{A0}'.is_whitespace());

assert!(!'越'.is_whitespace());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#922)

Returns `true` if this `char` satisfies either [`is_alphabetic()`](#method.is_alphabetic) or [`is_numeric()`](#method.is_numeric).

##### [§](#examples-19)Examples

Basic usage:

```rust
assert!('٣'.is_alphanumeric());
assert!('7'.is_alphanumeric());
assert!('৬'.is_alphanumeric());
assert!('¾'.is_alphanumeric());
assert!('①'.is_alphanumeric());
assert!('K'.is_alphanumeric());
assert!('و'.is_alphanumeric());
assert!('藏'.is_alphanumeric());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#952)

Returns `true` if this `char` has the general category for control codes.

Control codes (code points with the general category of `Cc`) are described in Chapter 4 (Character Properties) of the [Unicode Standard](https://www.unicode.org/versions/latest/) and specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`UnicodeData.txt`](https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt).

##### [§](#examples-20)Examples

Basic usage:

```rust
// U+009C, STRING TERMINATOR
assert!(''.is_control());
assert!(!'q'.is_control());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1047)

Returns `true` if this `char` has one of the general categories for numbers.

The general categories for numbers (`Nd` for decimal digits, `Nl` for letter-like numeric characters, and `No` for other numeric characters) are specified in the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`UnicodeData.txt`](https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt).

This method doesn’t cover everything that could be considered a number, e.g. ideographic numbers like ‘三’. If you want everything including characters with overlapping purposes then you might want to use a unicode or language-processing library that exposes the appropriate character properties instead of looking at the unicode categories.

If you want to parse ASCII decimal digits (0-9) or ASCII base-N, use `is_ascii_digit` or `is_digit` instead.

##### [§](#examples-21)Examples

Basic usage:

```rust
assert!('٣'.is_numeric());
assert!('7'.is_numeric());
assert!('৬'.is_numeric());
assert!('¾'.is_numeric());
assert!('①'.is_numeric());
assert!(!'K'.is_numeric());
assert!(!'و'.is_numeric());
assert!(!'藏'.is_numeric());
assert!(!'三'.is_numeric());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1117)

Returns an iterator that yields the lowercase mapping of this `char` as one or more `char`s.

If this `char` does not have a lowercase mapping, the iterator yields the same `char`.

If this `char` has a one-to-one lowercase mapping given by the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`UnicodeData.txt`](https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt), the iterator yields that `char`.

If this `char` requires special considerations (e.g. multiple `char`s) the iterator yields the `char`(s) given by [`SpecialCasing.txt`](https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt).

This operation performs an unconditional mapping without tailoring. That is, the conversion is independent of context and language.

In the [Unicode Standard](https://www.unicode.org/versions/latest/), Chapter 4 (Character Properties) discusses case mapping in general and Chapter 3 (Conformance) discusses the default algorithm for case conversion.

##### [§](#examples-22)Examples

As an iterator:

```rust
for c in 'İ'.to_lowercase() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", 'İ'.to_lowercase());
```

Both are equivalent to:

Using [`to_string`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string):

```rust
assert_eq!('C'.to_lowercase().to_string(), "c");

// Sometimes the result is more than one character:
assert_eq!('İ'.to_lowercase().to_string(), "i\u{307}");

// Characters that do not have both uppercase and lowercase
// convert into themselves.
assert_eq!('山'.to_lowercase().to_string(), "山");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1210)

Returns an iterator that yields the uppercase mapping of this `char` as one or more `char`s.

If this `char` does not have an uppercase mapping, the iterator yields the same `char`.

If this `char` has a one-to-one uppercase mapping given by the [Unicode Character Database](https://www.unicode.org/reports/tr44/) [`UnicodeData.txt`](https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt), the iterator yields that `char`.

If this `char` requires special considerations (e.g. multiple `char`s) the iterator yields the `char`(s) given by [`SpecialCasing.txt`](https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt).

This operation performs an unconditional mapping without tailoring. That is, the conversion is independent of context and language.

In the [Unicode Standard](https://www.unicode.org/versions/latest/), Chapter 4 (Character Properties) discusses case mapping in general and Chapter 3 (Conformance) discusses the default algorithm for case conversion.

##### [§](#examples-23)Examples

`'ﬅ'` (U+FB05) is a single Unicode code point (a ligature) that maps to “ST” in uppercase.

As an iterator:

```rust
for c in 'ﬅ'.to_uppercase() {
    print!("{c}");
}
println!();
```

Using `println!` directly:

```rust
println!("{}", 'ﬅ'.to_uppercase());
```

Both are equivalent to:

Using [`to_string`](https://doc.rust-lang.org/std/string/trait.ToString.html#tymethod.to_string):

```rust
assert_eq!('c'.to_uppercase().to_string(), "C");

// Sometimes the result is more than one character:
assert_eq!('ﬅ'.to_uppercase().to_string(), "ST");

// Characters that do not have both uppercase and lowercase
// convert into themselves.
assert_eq!('山'.to_uppercase().to_string(), "山");
```

##### [§](#note-on-locale)Note on locale

In Turkish, the equivalent of ‘i’ in Latin has five forms instead of two:

- ‘Dotless’: I / ı, sometimes written ï
- ‘Dotted’: İ / i

Note that the lowercase dotted ‘i’ is the same as the Latin. Therefore:

```rust
let upper_i = 'i'.to_uppercase().to_string();
```

The value of `upper_i` here relies on the language of the text: if we’re in `en-US`, it should be `"I"`, but if we’re in `tr_TR`, it should be `"İ"`. `to_uppercase()` does not take this into account, and so:

```rust
let upper_i = 'i'.to_uppercase().to_string();

assert_eq!(upper_i, "I");
```

holds across languages.

1.23.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1230)

Checks if the value is within the ASCII range.

##### [§](#examples-24)Examples

```rust
let ascii = 'a';
let non_ascii = '❤';

assert!(ascii.is_ascii());
assert!(!non_ascii.is_ascii());
```

[Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1243)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Returns `Some` if the value is within the ASCII range, or `None` if it’s not.

This is preferred to [`Self::is_ascii`](https://doc.rust-lang.org/std/primitive.char.html#method.is_ascii "method char::is_ascii") when you’re passing the value along to something else that can take [`ascii::Char`](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char") rather than needing to check again for itself whether the value is in ASCII.

[Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1261)

🔬This is a nightly-only experimental API. (`ascii_char` [#110998](https://github.com/rust-lang/rust/issues/110998))

Converts this char into an [ASCII character](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char"), without checking whether it is valid.

##### [§](#safety-1)Safety

This char must be within the ASCII range, or else this is UB.

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1298)

Makes a copy of the value in its ASCII upper case equivalent.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To uppercase the value in-place, use [`make_ascii_uppercase()`](#method.make_ascii_uppercase).

To uppercase ASCII characters in addition to non-ASCII characters, use [`to_uppercase()`](#method.to_uppercase).

##### [§](#examples-25)Examples

```rust
let ascii = 'a';
let non_ascii = '❤';

assert_eq!('A', ascii.to_ascii_uppercase());
assert_eq!('❤', non_ascii.to_ascii_uppercase());
```

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1332)

Makes a copy of the value in its ASCII lower case equivalent.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To lowercase the value in-place, use [`make_ascii_lowercase()`](#method.make_ascii_lowercase).

To lowercase ASCII characters in addition to non-ASCII characters, use [`to_lowercase()`](#method.to_lowercase).

##### [§](#examples-26)Examples

```rust
let ascii = 'A';
let non_ascii = '❤';

assert_eq!('a', ascii.to_ascii_lowercase());
assert_eq!('❤', non_ascii.to_ascii_lowercase());
```

1.23.0 (const: 1.52.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1360)

Checks that two values are an ASCII case-insensitive match.

Equivalent to `to_ascii_lowercase(a) == to_ascii_lowercase(b)`.

##### [§](#examples-27)Examples

```rust
let upper_a = 'A';
let lower_a = 'a';
let lower_z = 'z';

assert!(upper_a.eq_ignore_ascii_case(&lower_a));
assert!(upper_a.eq_ignore_ascii_case(&upper_a));
assert!(!upper_a.eq_ignore_ascii_case(&lower_z));
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1386)

Converts this type to its ASCII upper case equivalent in-place.

ASCII letters ‘a’ to ‘z’ are mapped to ‘A’ to ‘Z’, but non-ASCII letters are unchanged.

To return a new uppercased value without modifying the existing one, use [`to_ascii_uppercase()`](#method.to_ascii_uppercase).

##### [§](#examples-28)Examples

```rust
let mut ascii = 'a';

ascii.make_ascii_uppercase();

assert_eq!('A', ascii);
```

1.23.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1412)

Converts this type to its ASCII lower case equivalent in-place.

ASCII letters ‘A’ to ‘Z’ are mapped to ‘a’ to ‘z’, but non-ASCII letters are unchanged.

To return a new lowercased value without modifying the existing one, use [`to_ascii_lowercase()`](#method.to_ascii_lowercase).

##### [§](#examples-29)Examples

```rust
let mut ascii = 'A';

ascii.make_ascii_lowercase();

assert_eq!('a', ascii);
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1448)

Checks if the value is an ASCII alphabetic character:

- U+0041 ‘A’ ..= U+005A ‘Z’, or
- U+0061 ‘a’ ..= U+007A ‘z’.

##### [§](#examples-30)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(uppercase_a.is_ascii_alphabetic());
assert!(uppercase_g.is_ascii_alphabetic());
assert!(a.is_ascii_alphabetic());
assert!(g.is_ascii_alphabetic());
assert!(!zero.is_ascii_alphabetic());
assert!(!percent.is_ascii_alphabetic());
assert!(!space.is_ascii_alphabetic());
assert!(!lf.is_ascii_alphabetic());
assert!(!esc.is_ascii_alphabetic());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1482)

Checks if the value is an ASCII uppercase character: U+0041 ‘A’ ..= U+005A ‘Z’.

##### [§](#examples-31)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(uppercase_a.is_ascii_uppercase());
assert!(uppercase_g.is_ascii_uppercase());
assert!(!a.is_ascii_uppercase());
assert!(!g.is_ascii_uppercase());
assert!(!zero.is_ascii_uppercase());
assert!(!percent.is_ascii_uppercase());
assert!(!space.is_ascii_uppercase());
assert!(!lf.is_ascii_uppercase());
assert!(!esc.is_ascii_uppercase());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1516)

Checks if the value is an ASCII lowercase character: U+0061 ‘a’ ..= U+007A ‘z’.

##### [§](#examples-32)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(!uppercase_a.is_ascii_lowercase());
assert!(!uppercase_g.is_ascii_lowercase());
assert!(a.is_ascii_lowercase());
assert!(g.is_ascii_lowercase());
assert!(!zero.is_ascii_lowercase());
assert!(!percent.is_ascii_lowercase());
assert!(!space.is_ascii_lowercase());
assert!(!lf.is_ascii_lowercase());
assert!(!esc.is_ascii_lowercase());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1553)

Checks if the value is an ASCII alphanumeric character:

- U+0041 ‘A’ ..= U+005A ‘Z’, or
- U+0061 ‘a’ ..= U+007A ‘z’, or
- U+0030 ‘0’ ..= U+0039 ‘9’.

##### [§](#examples-33)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(uppercase_a.is_ascii_alphanumeric());
assert!(uppercase_g.is_ascii_alphanumeric());
assert!(a.is_ascii_alphanumeric());
assert!(g.is_ascii_alphanumeric());
assert!(zero.is_ascii_alphanumeric());
assert!(!percent.is_ascii_alphanumeric());
assert!(!space.is_ascii_alphanumeric());
assert!(!lf.is_ascii_alphanumeric());
assert!(!esc.is_ascii_alphanumeric());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1587)

Checks if the value is an ASCII decimal digit: U+0030 ‘0’ ..= U+0039 ‘9’.

##### [§](#examples-34)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(!uppercase_a.is_ascii_digit());
assert!(!uppercase_g.is_ascii_digit());
assert!(!a.is_ascii_digit());
assert!(!g.is_ascii_digit());
assert!(zero.is_ascii_digit());
assert!(!percent.is_ascii_digit());
assert!(!space.is_ascii_digit());
assert!(!lf.is_ascii_digit());
assert!(!esc.is_ascii_digit());
```

[Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1618)

🔬This is a nightly-only experimental API. (`is_ascii_octdigit` [#101288](https://github.com/rust-lang/rust/issues/101288))

Checks if the value is an ASCII octal digit: U+0030 ‘0’ ..= U+0037 ‘7’.

##### [§](#examples-35)Examples

```rust
#![feature(is_ascii_octdigit)]

let uppercase_a = 'A';
let a = 'a';
let zero = '0';
let seven = '7';
let nine = '9';
let percent = '%';
let lf = '\n';

assert!(!uppercase_a.is_ascii_octdigit());
assert!(!a.is_ascii_octdigit());
assert!(zero.is_ascii_octdigit());
assert!(seven.is_ascii_octdigit());
assert!(!nine.is_ascii_octdigit());
assert!(!percent.is_ascii_octdigit());
assert!(!lf.is_ascii_octdigit());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1655)

Checks if the value is an ASCII hexadecimal digit:

- U+0030 ‘0’ ..= U+0039 ‘9’, or
- U+0041 ‘A’ ..= U+0046 ‘F’, or
- U+0061 ‘a’ ..= U+0066 ‘f’.

##### [§](#examples-36)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(uppercase_a.is_ascii_hexdigit());
assert!(!uppercase_g.is_ascii_hexdigit());
assert!(a.is_ascii_hexdigit());
assert!(!g.is_ascii_hexdigit());
assert!(zero.is_ascii_hexdigit());
assert!(!percent.is_ascii_hexdigit());
assert!(!space.is_ascii_hexdigit());
assert!(!lf.is_ascii_hexdigit());
assert!(!esc.is_ascii_hexdigit());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1693)

Checks if the value is an ASCII punctuation character:

- U+0021 ..= U+002F `! " # $ % & ' ( ) * + , - . /`, or
- U+003A ..= U+0040 `: ; < = > ? @`, or
- U+005B ..= U+0060 ``[ \ ] ^ _ ` ``, or
- U+007B ..= U+007E `{ | } ~`

##### [§](#examples-37)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(!uppercase_a.is_ascii_punctuation());
assert!(!uppercase_g.is_ascii_punctuation());
assert!(!a.is_ascii_punctuation());
assert!(!g.is_ascii_punctuation());
assert!(!zero.is_ascii_punctuation());
assert!(percent.is_ascii_punctuation());
assert!(!space.is_ascii_punctuation());
assert!(!lf.is_ascii_punctuation());
assert!(!esc.is_ascii_punctuation());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1730)

Checks if the value is an ASCII graphic character: U+0021 ‘!’ ..= U+007E ‘~’.

##### [§](#examples-38)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(uppercase_a.is_ascii_graphic());
assert!(uppercase_g.is_ascii_graphic());
assert!(a.is_ascii_graphic());
assert!(g.is_ascii_graphic());
assert!(zero.is_ascii_graphic());
assert!(percent.is_ascii_graphic());
assert!(!space.is_ascii_graphic());
assert!(!lf.is_ascii_graphic());
assert!(!esc.is_ascii_graphic());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1781)

Checks if the value is an ASCII whitespace character: U+0020 SPACE, U+0009 HORIZONTAL TAB, U+000A LINE FEED, U+000C FORM FEED, or U+000D CARRIAGE RETURN.

Rust uses the WhatWG Infra Standard’s [definition of ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). There are several other definitions in wide use. For instance, [the POSIX locale](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap07.html#tag_07_03_01) includes U+000B VERTICAL TAB as well as all the above characters, but—from the very same specification—[the default rule for “field splitting” in the Bourne shell](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05) considers *only* SPACE, HORIZONTAL TAB, and LINE FEED as whitespace.

If you are writing a program that will process an existing file format, check what that format’s definition of whitespace is before using this function.

##### [§](#examples-39)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(!uppercase_a.is_ascii_whitespace());
assert!(!uppercase_g.is_ascii_whitespace());
assert!(!a.is_ascii_whitespace());
assert!(!g.is_ascii_whitespace());
assert!(!zero.is_ascii_whitespace());
assert!(!percent.is_ascii_whitespace());
assert!(space.is_ascii_whitespace());
assert!(lf.is_ascii_whitespace());
assert!(!esc.is_ascii_whitespace());
```

1.24.0 (const: 1.47.0) · [Source](https://doc.rust-lang.org/src/core/char/methods.rs.html#1817)

Checks if the value is an ASCII control character: U+0000 NUL ..= U+001F UNIT SEPARATOR, or U+007F DELETE. Note that most ASCII whitespace characters are control characters, but SPACE is not.

##### [§](#examples-40)Examples

```rust
let uppercase_a = 'A';
let uppercase_g = 'G';
let a = 'a';
let g = 'g';
let zero = '0';
let percent = '%';
let space = ' ';
let lf = '\n';
let esc = '\x1b';

assert!(!uppercase_a.is_ascii_control());
assert!(!uppercase_g.is_ascii_control());
assert!(!a.is_ascii_control());
assert!(!g.is_ascii_control());
assert!(!zero.is_ascii_control());
assert!(!percent.is_ascii_control());
assert!(!space.is_ascii_control());
assert!(lf.is_ascii_control());
assert!(esc.is_ascii_control());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ascii.rs.html#190-194)[§](#impl-AsciiExt-for-char)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#191)[§](#associatedtype.Owned)

👎Deprecated since 1.26.0: use inherent methods instead

Container type for copied ASCII characters.

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.is_ascii-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks if the value is within the ASCII range. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.is_ascii)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.to_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII upper case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.to_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Makes a copy of the value in its ASCII lower case equivalent. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.to_ascii_lowercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.eq_ignore_ascii_case-1)

👎Deprecated since 1.26.0: use inherent methods instead

Checks that two values are an ASCII case-insensitive match. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.eq_ignore_ascii_case)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.make_ascii_uppercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII upper case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_uppercase)

[Source](https://doc.rust-lang.org/src/std/ascii.rs.html#193)[§](#method.make_ascii_lowercase-1)

👎Deprecated since 1.26.0: use inherent methods instead

Converts this type to its ASCII lower case equivalent in-place. [Read more](https://doc.rust-lang.org/std/ascii/trait.AsciiExt.html#tymethod.make_ascii_lowercase)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-char)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#2965)[§](#impl-Debug-for-char)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/default.rs.html#166)[§](#impl-Default-for-char)

[Source](https://doc.rust-lang.org/src/core/default.rs.html#166)[§](#method.default)

Returns the default value of `\x00`

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#2979)[§](#impl-Display-for-char)

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2488)[§](#impl-Extend%3C%26char%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2489)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2494)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2499)[§](#method.extend_reserve-1)

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

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-char)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#method.from)

Converts to this type from the input type.

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3593)[§](#impl-From%3Cchar%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3603)[§](#method.from-5)

Allocates an owned [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") from a single character.

##### [§](#example)Example

```rust
let c: char = 'a';
let s: String = String::from(c);
assert_eq!("a", &s[..]);
```

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#80)[§](#impl-From%3Cchar%3E-for-u128)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#92)[§](#method.from-3)

Converts a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u128`](https://doc.rust-lang.org/std/primitive.u128.html "primitive u128").

##### [§](#examples-43)Examples

```rust
let c = '⚙';
let u = u128::from(c);

assert!(16 == size_of_val(&u))
```

1.13.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#40)[§](#impl-From%3Cchar%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#52)[§](#method.from-1)

Converts a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u32`](https://doc.rust-lang.org/std/primitive.u32.html "primitive u32").

##### [§](#examples-41)Examples

```rust
let c = 'c';
let u = u32::from(c);

assert!(4 == size_of_val(&u))
```

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#59)[§](#impl-From%3Cchar%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#71)[§](#method.from-2)

Converts a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u64`](https://doc.rust-lang.org/std/primitive.u64.html "primitive u64").

##### [§](#examples-42)Examples

```rust
let c = '👤';
let u = u64::from(c);

assert!(8 == size_of_val(&u))
```

1.13.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#217)[§](#impl-From%3Cu8%3E-for-char)

Maps a byte in `0x00..=0xFF` to a `char` whose code point has the same value from U+0000 to U+00FF (inclusive).

Unicode is designed such that this effectively decodes bytes with the character encoding that IANA calls ISO-8859-1. This encoding is compatible with ASCII.

Note that this is different from ISO/IEC 8859-1 a.k.a. ISO 8859-1 (with one less hyphen), which leaves some “blanks”, byte values that are not assigned to any character. ISO-8859-1 (the IANA one) assigns them to the C0 and C1 control codes.

Note that this is *also* different from Windows-1252 a.k.a. code page 1252, which is a superset ISO/IEC 8859-1 that assigns some (not all!) blanks to punctuation and various Latin characters.

To confuse things further, [on the Web](https://encoding.spec.whatwg.org/) `ascii`, `iso-8859-1`, and `windows-1252` are all aliases for a superset of Windows-1252 that fills the remaining blanks with corresponding C0 and C1 control codes.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#229)[§](#method.from-4)

Converts a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8") into a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char").

##### [§](#examples-44)Examples

```rust
let u = 32 as u8;
let c = char::from(u);

assert!(4 == size_of_val(&c))
```

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#158)[§](#impl-FromIterator%3C%26char%3E-for-Box%3Cstr%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2376)[§](#impl-FromIterator%3C%26char%3E-for-String)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/iter.rs.html#150)[§](#impl-FromIterator%3Cchar%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#264)[§](#impl-FromIterator%3Cchar%3E-for-ByteString)

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3273)[§](#impl-FromIterator%3Cchar%3E-for-Cow%3C'a,+str%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2366)[§](#impl-FromIterator%3Cchar%3E-for-String)

1.20.0 · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#264)[§](#impl-FromStr-for-char)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#265)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#268)[§](#method.from_str)

Parses a string `s` to return a value of this type. [Read more](https://doc.rust-lang.org/std/str/trait.FromStr.html#tymethod.from_str)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/hash/mod.rs.html#854)[§](#impl-Hash-for-char)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#impl-Ord-for-char)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-char)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#impl-PartialOrd-for-char)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#2080)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#560)[§](#impl-Pattern-for-char)

Searches for chars that are equal to a given [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char").

#### [§](#examples-48)Examples

```rust
assert_eq!("Hello world".find('o'), Some(4));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#561)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#564)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#583)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#593)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#598)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#603-605)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#611-613)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#619)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#67)[§](#impl-RangePattern-for-char)

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#68)[§](#associatedconstant.MIN-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#70)[§](#associatedconstant.MAX-1)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#72)[§](#method.sub_one)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#452)[§](#impl-Step-for-char)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#454)[§](#method.steps_between)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the bounds on the number of *successor* steps required to get from `start` to `end` like [`Iterator::size_hint()`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.size_hint "method std::iter::Iterator::size_hint"). [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.steps_between)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#478)[§](#method.forward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.forward_checked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#494)[§](#method.backward_checked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#tymethod.backward_checked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#506)[§](#method.forward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.forward_unchecked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#522)[§](#method.backward_unchecked)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.backward_unchecked)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#90)[§](#method.forward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *successor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.forward)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#160)[§](#method.backward)

🔬This is a nightly-only experimental API. (`step_trait` [#42168](https://github.com/rust-lang/rust/issues/42168))

Returns the value that would be obtained by taking the *predecessor* of `self` `count` times. [Read more](https://doc.rust-lang.org/std/iter/trait.Step.html#method.backward)

1.74.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#135)[§](#impl-TryFrom%3Cchar%3E-for-u16)

Maps a `char` with a code point from U+0000 to U+FFFF (inclusive) to a `u16` in `0x0000..=0xFFFF` with the same value, failing if the code point is greater than U+FFFF.

This corresponds to the UCS-2 encoding, as specified in ISO/IEC 10646:2003.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#150)[§](#method.try_from-1)

Tries to convert a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u16`](https://doc.rust-lang.org/std/primitive.u16.html "primitive u16").

##### [§](#examples-46)Examples

```rust
let trans_rights = '⚧'; // U+26A7
let ninjas = '🥷'; // U+1F977

assert_eq!(u16::try_from(trans_rights), Ok(0x26A7_u16));
assert!(u16::try_from(ninjas).is_err());
```

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#136)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

1.59.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#105)[§](#impl-TryFrom%3Cchar%3E-for-u8)

Maps a `char` with a code point from U+0000 to U+00FF (inclusive) to a byte in `0x00..=0xFF` with the same value, failing if the code point is greater than U+00FF.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#120)[§](#method.try_from)

Tries to convert a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`u8`](https://doc.rust-lang.org/std/primitive.u8.html "primitive u8").

##### [§](#examples-45)Examples

```rust
let a = 'ÿ'; // U+00FF
let b = 'Ā'; // U+0100

assert_eq!(u8::try_from(a), Ok(0xFF_u8));
assert!(u8::try_from(b).is_err());
```

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#106)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

1.94.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#167)[§](#impl-TryFrom%3Cchar%3E-for-usize)

Maps a `char` with a code point from U+0000 to U+10FFFF (inclusive) to a `usize` in `0x0000..=0x10FFFF` with the same value, failing if the final value is unrepresentable by `usize`.

Generally speaking, this conversion can be seen as obtaining the character’s corresponding UTF-32 code point to the extent representable by pointer addresses.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#187)[§](#method.try_from-2)

Tries to convert a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") into a [`usize`](https://doc.rust-lang.org/std/primitive.usize.html "primitive usize").

##### [§](#examples-47)Examples

```rust
let a = '\u{FFFF}'; // Always succeeds.
let b = '\u{10FFFF}'; // Conditionally succeeds.

assert_eq!(usize::try_from(a), Ok(0xFFFF));

if size_of::<usize>() >= size_of::<u32>() {
    assert_eq!(usize::try_from(b), Ok(0x10FFFF));
} else {
    assert!(matches!(usize::try_from(b), Err(_)));
}
```

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#168)[§](#associatedtype.Error-2)

The type returned in the event of a conversion error.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#303)[§](#impl-TryFrom%3Cu32%3E-for-char)

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#304)[§](#associatedtype.Error-3)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#307)[§](#method.try_from-3)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#69-83)[§](#impl-ZeroablePrimitive-for-char)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#69-83)[§](#associatedtype.NonZeroInner)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-char)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-char)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-char)

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-char)

[Source](https://doc.rust-lang.org/src/core/iter/range.rs.html#17)[§](#impl-TrustedStep-for-char)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-char)

[§](#impl-Freeze-for-char)

[§](#impl-RefUnwindSafe-for-char)

[§](#impl-Send-for-char)

[§](#impl-Sync-for-char)

[§](#impl-Unpin-for-char)

[§](#impl-UnsafeUnpin-for-char)

[§](#impl-UnwindSafe-for-char)