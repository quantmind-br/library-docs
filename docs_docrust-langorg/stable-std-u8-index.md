---
title: std::u8 - Rust
url: https://doc.rust-lang.org/stable/std/u8/index.html
source: crawler
fetched_at: 2026-05-06T21:28:29.467273986-03:00
rendered_js: false
word_count: 78
summary: This document describes the deprecation of the u8 module in the Rust standard library, advising developers to use associated constants on the u8 primitive type instead.
tags:
    - rust-standard-library
    - u8-primitive
    - deprecated-api
    - language-reference
    - integer-types
category: reference
---

[std](https://doc.rust-lang.org/stable/std/index.html)

## Module u8

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/shells/legacy_int_modules.rs.html#70)

👎Deprecating in a future version: all constants in this module replaced by associated constants on the type

Expand description

Redundant constants module for the [`u8` primitive type](https://doc.rust-lang.org/stable/std/primitive.u8.html "primitive u8").

New code should use the associated constants directly on the primitive type.

## Constants[§](#constants)

[MAX](https://doc.rust-lang.org/stable/std/u8/constant.MAX.html "constant std::u8::MAX")Deprecation planned

The largest value that can be represented by this integer type. Use [`u8::MAX`](https://doc.rust-lang.org/stable/std/primitive.u8.html#associatedconstant.MAX "associated constant u8::MAX") instead.

[MIN](https://doc.rust-lang.org/stable/std/u8/constant.MIN.html "constant std::u8::MIN")Deprecation planned

The smallest value that can be represented by this integer type. Use [`u8::MIN`](https://doc.rust-lang.org/stable/std/primitive.u8.html#associatedconstant.MIN "associated constant u8::MIN") instead.