---
title: std::u64 - Rust
url: https://doc.rust-lang.org/stable/std/u64/index.html
source: crawler
fetched_at: 2026-05-06T21:28:31.134344635-03:00
rendered_js: false
word_count: 77
summary: This document describes a legacy module for the u64 primitive type in Rust and advises developers to use associated constants on the type instead of the deprecated module constants.
tags:
    - rust-programming
    - primitive-types
    - deprecated-api
    - u64
    - code-standards
category: reference
---

## Module u64

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/shells/legacy_int_modules.rs.html#69)

👎Deprecating in a future version: all constants in this module replaced by associated constants on the type

Expand description

Redundant constants module for the [`u64` primitive type](https://doc.rust-lang.org/stable/std/primitive.u64.html "primitive u64").

New code should use the associated constants directly on the primitive type.

## Constants[§](#constants)

[MAX](https://doc.rust-lang.org/stable/std/u64/constant.MAX.html "constant std::u64::MAX")Deprecation planned

The largest value that can be represented by this integer type. Use [`u64::MAX`](https://doc.rust-lang.org/stable/std/primitive.u64.html#associatedconstant.MAX "associated constant u64::MAX") instead.

[MIN](https://doc.rust-lang.org/stable/std/u64/constant.MIN.html "constant std::u64::MIN")Deprecation planned

The smallest value that can be represented by this integer type. Use [`u64::MIN`](https://doc.rust-lang.org/stable/std/primitive.u64.html#associatedconstant.MIN "associated constant u64::MIN") instead.