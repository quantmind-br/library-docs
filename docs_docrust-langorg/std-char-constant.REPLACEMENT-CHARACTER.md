---
title: REPLACEMENT_CHARACTER in std::char - Rust
url: https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html
source: crawler
fetched_at: 2026-05-06T21:22:12.190065524-03:00
rendered_js: false
word_count: 24
summary: This document defines the REPLACEMENT_CHARACTER constant in the Rust standard library, which represents the Unicode character used to indicate decoding errors.
tags:
    - rust
    - unicode
    - character-encoding
    - constant
    - std-library
category: reference
---

[std](https://doc.rust-lang.org/std/index.html)::[char](https://doc.rust-lang.org/std/char/index.html)

## Constant REPLACEMENT\_CHARACTER

1.9.0 · [Source](https://doc.rust-lang.org/src/core/char/mod.rs.html#111)

```rust
pub const REPLACEMENT_CHARACTER: char = char::REPLACEMENT_CHARACTER; // '�'
```

Expand description

`U+FFFD REPLACEMENT CHARACTER` (�) is used in Unicode to represent a decoding error. Use [`char::REPLACEMENT_CHARACTER`](https://doc.rust-lang.org/std/primitive.char.html#associatedconstant.REPLACEMENT_CHARACTER "associated constant char::REPLACEMENT_CHARACTER") instead.