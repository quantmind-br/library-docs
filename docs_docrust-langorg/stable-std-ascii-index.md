---
title: std::ascii - Rust
url: https://doc.rust-lang.org/stable/std/ascii/index.html
source: crawler
fetched_at: 2026-05-06T21:28:22.424415035-03:00
rendered_js: false
word_count: 125
summary: This document provides an overview of the Rust standard library module for performing operations specifically on ASCII characters and strings.
tags:
    - rust
    - ascii
    - string-manipulation
    - character-encoding
    - standard-library
category: reference
---

## Module ascii

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/ascii.rs.html#1-210)

Expand description

Operations on ASCII strings and characters.

Most string operations in Rust act on UTF-8 strings. However, at times it makes more sense to only consider the ASCII character set for a specific operation.

The [`AsciiExt`](https://doc.rust-lang.org/stable/std/ascii/trait.AsciiExt.html "trait std::ascii::AsciiExt") trait provides methods that allow for character operations that only act on the ASCII subset and leave non-ASCII characters alone.

The [`escape_default`](https://doc.rust-lang.org/stable/std/ascii/fn.escape_default.html "fn std::ascii::escape_default") function provides an iterator over the bytes of an escaped version of the character given.

[EscapeDefault](https://doc.rust-lang.org/stable/std/ascii/struct.EscapeDefault.html "struct std::ascii::EscapeDefault")

An iterator over the escaped version of a byte.

[Char](https://doc.rust-lang.org/stable/std/ascii/enum.Char.html "enum std::ascii::Char")Experimental

One of the 128 Unicode characters from U+0000 through U+007F, often known as the [ASCII](https://www.unicode.org/glossary/index.html#ASCII) subset.

[AsciiExt](https://doc.rust-lang.org/stable/std/ascii/trait.AsciiExt.html "trait std::ascii::AsciiExt")Deprecated

Extension methods for ASCII-subset only operations.

[escape\_default](https://doc.rust-lang.org/stable/std/ascii/fn.escape_default.html "fn std::ascii::escape_default")

Returns an iterator that produces an escaped version of a `u8`.