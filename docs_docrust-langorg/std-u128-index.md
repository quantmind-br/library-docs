---
title: std::u128 - Rust
url: https://doc.rust-lang.org/std/u128/index.html
source: crawler
fetched_at: 2026-05-06T21:32:25.227543816-03:00
rendered_js: false
word_count: 76
summary: This document documents a legacy module for the u128 primitive type in Rust, noting that its constants are deprecated in favor of associated constants on the type itself.
tags:
    - rust
    - u128
    - primitive-type
    - deprecation
    - constants
    - language-features
category: reference
---

## Module u128

1.26.0 · [Source](https://doc.rust-lang.org/src/core/num/shells/legacy_int_modules.rs.html#66)

👎Deprecating in a future version: all constants in this module replaced by associated constants on the type

Expand description

Redundant constants module for the [`u128` primitive type](https://doc.rust-lang.org/std/primitive.u128.html "primitive u128").

New code should use the associated constants directly on the primitive type.

[MAX](https://doc.rust-lang.org/std/u128/constant.MAX.html "constant std::u128::MAX")Deprecation planned

The largest value that can be represented by this integer type. Use [`u128::MAX`](https://doc.rust-lang.org/std/primitive.u128.html#associatedconstant.MAX "associated constant u128::MAX") instead.

[MIN](https://doc.rust-lang.org/std/u128/constant.MIN.html "constant std::u128::MIN")Deprecation planned

The smallest value that can be represented by this integer type. Use [`u128::MIN`](https://doc.rust-lang.org/std/primitive.u128.html#associatedconstant.MIN "associated constant u128::MIN") instead.