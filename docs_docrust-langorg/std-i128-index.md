---
title: std::i128 - Rust
url: https://doc.rust-lang.org/std/i128/index.html
source: crawler
fetched_at: 2026-05-06T21:32:20.007700114-03:00
rendered_js: false
word_count: 76
summary: This document describes a deprecated module for the i128 primitive type in Rust and advises developers to use associated constants on the type instead.
tags:
    - rust
    - primitive-types
    - i128
    - deprecation
    - constants
    - standard-library
category: reference
---

## Module i128

1.26.0 · [Source](https://doc.rust-lang.org/src/core/num/shells/legacy_int_modules.rs.html#60)

👎Deprecating in a future version: all constants in this module replaced by associated constants on the type

Expand description

Redundant constants module for the [`i128` primitive type](https://doc.rust-lang.org/std/primitive.i128.html "primitive i128").

New code should use the associated constants directly on the primitive type.

[MAX](https://doc.rust-lang.org/std/i128/constant.MAX.html "constant std::i128::MAX")Deprecation planned

The largest value that can be represented by this integer type. Use [`i128::MAX`](https://doc.rust-lang.org/std/primitive.i128.html#associatedconstant.MAX "associated constant i128::MAX") instead.

[MIN](https://doc.rust-lang.org/std/i128/constant.MIN.html "constant std::i128::MIN")Deprecation planned

The smallest value that can be represented by this integer type. Use [`i128::MIN`](https://doc.rust-lang.org/std/primitive.i128.html#associatedconstant.MIN "associated constant i128::MIN") instead.