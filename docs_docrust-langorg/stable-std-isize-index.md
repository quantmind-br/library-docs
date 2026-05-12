---
title: std::isize - Rust
url: https://doc.rust-lang.org/stable/std/isize/index.html
source: crawler
fetched_at: 2026-05-06T21:28:26.383297985-03:00
rendered_js: false
word_count: 76
summary: This document describes the deprecation of the isize constant module in Rust, advising developers to utilize associated constants on the primitive type instead.
tags:
    - rust-programming
    - primitive-types
    - deprecation
    - integer-constants
    - api-migration
category: reference
---

## Module isize

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/shells/legacy_int_modules.rs.html#65)

👎Deprecating in a future version: all constants in this module replaced by associated constants on the type

Expand description

Redundant constants module for the [`isize` primitive type](https://doc.rust-lang.org/stable/std/primitive.isize.html "primitive isize").

New code should use the associated constants directly on the primitive type.

[MAX](https://doc.rust-lang.org/stable/std/isize/constant.MAX.html "constant std::isize::MAX")Deprecation planned

The largest value that can be represented by this integer type. Use [`isize::MAX`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MAX "associated constant isize::MAX") instead.

[MIN](https://doc.rust-lang.org/stable/std/isize/constant.MIN.html "constant std::isize::MIN")Deprecation planned

The smallest value that can be represented by this integer type. Use [`isize::MIN`](https://doc.rust-lang.org/stable/std/primitive.isize.html#associatedconstant.MIN "associated constant isize::MIN") instead.