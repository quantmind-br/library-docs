---
title: std::char - Rust
url: https://doc.rust-lang.org/stable/std/char/index.html
source: crawler
fetched_at: 2026-05-06T21:28:08.704482723-03:00
rendered_js: false
word_count: 364
summary: This module provides utility functions, iterators, and constants for handling the Rust primitive char type and performing Unicode scalar value operations.
tags:
    - rust
    - unicode
    - char
    - primitive-types
    - string-processing
    - iterator-utilities
category: reference
---

## Module char

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#292)

Expand description

Utilities for the `char` primitive type.

*[See also the `char` primitive type](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char").*

The `char` type represents a single character. More specifically, since ‘character’ isn’t a well-defined concept in Unicode, `char` is a ‘[Unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value)’, which is similar to, but not the same as, a ‘[Unicode code point](https://www.unicode.org/glossary/#code_point)’.

This module exists for technical reasons, the primary documentation for `char` is directly on [the `char` primitive type](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char") itself.

This module is the home of the iterator implementations for the iterators implemented on `char`, as well as some useful constants and conversion functions that convert various types to `char`.

[CharTryFromError](https://doc.rust-lang.org/stable/std/char/struct.CharTryFromError.html "struct std::char::CharTryFromError")

The error type returned when a conversion from [`u32`](https://doc.rust-lang.org/stable/std/primitive.u32.html "primitive u32") to [`char`](https://doc.rust-lang.org/stable/std/primitive.char.html "primitive char") fails.

[DecodeUtf16](https://doc.rust-lang.org/stable/std/char/struct.DecodeUtf16.html "struct std::char::DecodeUtf16")

An iterator that decodes UTF-16 encoded code points from an iterator of `u16`s.

[DecodeUtf16Error](https://doc.rust-lang.org/stable/std/char/struct.DecodeUtf16Error.html "struct std::char::DecodeUtf16Error")

An error that can be returned when decoding UTF-16 code points.

[EscapeDebug](https://doc.rust-lang.org/stable/std/char/struct.EscapeDebug.html "struct std::char::EscapeDebug")

An iterator that yields the literal escape code of a `char`.

[EscapeDefault](https://doc.rust-lang.org/stable/std/char/struct.EscapeDefault.html "struct std::char::EscapeDefault")

An iterator that yields the literal escape code of a `char`.

[EscapeUnicode](https://doc.rust-lang.org/stable/std/char/struct.EscapeUnicode.html "struct std::char::EscapeUnicode")

Returns an iterator that yields the hexadecimal Unicode escape of a character, as `char`s.

[ParseCharError](https://doc.rust-lang.org/stable/std/char/struct.ParseCharError.html "struct std::char::ParseCharError")

An error which can be returned when parsing a char.

[ToLowercase](https://doc.rust-lang.org/stable/std/char/struct.ToLowercase.html "struct std::char::ToLowercase")

Returns an iterator that yields the lowercase equivalent of a `char`.

[ToUppercase](https://doc.rust-lang.org/stable/std/char/struct.ToUppercase.html "struct std::char::ToUppercase")

Returns an iterator that yields the uppercase equivalent of a `char`.

[TryFromCharError](https://doc.rust-lang.org/stable/std/char/struct.TryFromCharError.html "struct std::char::TryFromCharError")

The error type returned when a checked char conversion fails.

[MAX](https://doc.rust-lang.org/stable/std/char/constant.MAX.html "constant std::char::MAX")

The highest valid code point a `char` can have, `'\u{10FFFF}'`. Use [`char::MAX`](https://doc.rust-lang.org/stable/std/primitive.char.html#associatedconstant.MAX "associated constant char::MAX") instead.

[REPLACEMENT\_CHARACTER](https://doc.rust-lang.org/stable/std/char/constant.REPLACEMENT_CHARACTER.html "constant std::char::REPLACEMENT_CHARACTER")

`U+FFFD REPLACEMENT CHARACTER` (�) is used in Unicode to represent a decoding error. Use [`char::REPLACEMENT_CHARACTER`](https://doc.rust-lang.org/stable/std/primitive.char.html#associatedconstant.REPLACEMENT_CHARACTER "associated constant char::REPLACEMENT_CHARACTER") instead.

[UNICODE\_VERSION](https://doc.rust-lang.org/stable/std/char/constant.UNICODE_VERSION.html "constant std::char::UNICODE_VERSION")

The version of [Unicode](https://www.unicode.org/) that the Unicode parts of `char` and `str` methods are based on. Use [`char::UNICODE_VERSION`](https://doc.rust-lang.org/stable/std/primitive.char.html#associatedconstant.UNICODE_VERSION "associated constant char::UNICODE_VERSION") instead.

[MAX\_LEN\_UTF8](https://doc.rust-lang.org/stable/std/char/constant.MAX_LEN_UTF8.html "constant std::char::MAX_LEN_UTF8")Experimental

The maximum number of bytes required to [encode](https://doc.rust-lang.org/stable/std/primitive.char.html#method.encode_utf8 "method char::encode_utf8") a `char` to UTF-8 encoding.

[MAX\_LEN\_UTF16](https://doc.rust-lang.org/stable/std/char/constant.MAX_LEN_UTF16.html "constant std::char::MAX_LEN_UTF16")Experimental

The maximum number of two-byte units required to [encode](https://doc.rust-lang.org/stable/std/primitive.char.html#method.encode_utf16 "method char::encode_utf16") a `char` to UTF-16 encoding.

[decode\_utf16](https://doc.rust-lang.org/stable/std/char/fn.decode_utf16.html "fn std::char::decode_utf16")

Creates an iterator over the UTF-16 encoded code points in `iter`, returning unpaired surrogates as `Err`s. Use [`char::decode_utf16`](https://doc.rust-lang.org/stable/std/primitive.char.html#method.decode_utf16 "associated function char::decode_utf16") instead.

[from\_digit](https://doc.rust-lang.org/stable/std/char/fn.from_digit.html "fn std::char::from_digit")

Converts a digit in the given radix to a `char`. Use [`char::from_digit`](https://doc.rust-lang.org/stable/std/primitive.char.html#method.from_digit "associated function char::from_digit") instead.

[from\_u32](https://doc.rust-lang.org/stable/std/char/fn.from_u32.html "fn std::char::from_u32")

Converts a `u32` to a `char`. Use [`char::from_u32`](https://doc.rust-lang.org/stable/std/primitive.char.html#method.from_u32 "associated function char::from_u32") instead.

[from\_u32\_unchecked](https://doc.rust-lang.org/stable/std/char/fn.from_u32_unchecked.html "fn std::char::from_u32_unchecked")⚠

Converts a `u32` to a `char`, ignoring validity. Use [`char::from_u32_unchecked`](https://doc.rust-lang.org/stable/std/primitive.char.html#method.from_u32_unchecked "associated function char::from_u32_unchecked") instead.