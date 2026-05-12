---
title: Identifiers - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/identifiers.html#railroad-IDENTIFIER_OR_KEYWORD
source: crawler
fetched_at: 2026-05-06T21:32:02.577315394-03:00
rendered_js: false
word_count: 284
summary: This document defines the syntax, Unicode compliance, and normalization rules for identifiers in the Rust programming language, including the usage of raw identifiers.
tags:
    - rust
    - programming-language
    - identifiers
    - syntax-rules
    - unicode-standards
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Identifiers](#identifiers)

Identifiers follow the specification in [Unicode Standard Annex #31](https://www.unicode.org/reports/tr31/tr31-43.html) for Unicode version 17.0, with the additions described below. Some examples of identifiers:

- `foo`
- `_identifier`
- `r#true`
- `Москва`
- `東京`

The profile used from UAX #31 is:

- Start := [`XID_Start`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Start%3A%5D&abb=on&g=&i=), plus the underscore character (U+005F)
- Continue := [`XID_Continue`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Continue%3A%5D&abb=on&g=&i=)
- Medial := empty

> Note
> 
> Identifiers starting with an underscore are typically used to indicate an identifier that is intentionally unused, and will silence the unused warning in `rustc`.

Identifiers may not be a [strict](https://doc.rust-lang.org/stable/reference/keywords.html#strict-keywords) or [reserved](https://doc.rust-lang.org/stable/reference/keywords.html#reserved-keywords) keyword without the `r#` prefix described below in [raw identifiers](#raw-identifiers).

Zero width non-joiner (ZWNJ U+200C) and zero width joiner (ZWJ U+200D) characters are not allowed in identifiers.

Identifiers are restricted to the ASCII subset of [`XID_Start`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Start%3A%5D&abb=on&g=&i=) and [`XID_Continue`](http://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AXID_Continue%3A%5D&abb=on&g=&i=) in the following situations:

- [`extern crate`](https://doc.rust-lang.org/stable/reference/items/extern-crates.html) declarations (except the [AsClause](https://doc.rust-lang.org/stable/reference/items/extern-crates.html#grammar-AsClause) identifier)
- External crate names referenced in a [path](https://doc.rust-lang.org/stable/reference/paths.html)
- [Module](https://doc.rust-lang.org/stable/reference/items/modules.html) names loaded from the filesystem without a [`path` attribute](https://doc.rust-lang.org/stable/reference/items/modules.html#the-path-attribute)
- [`no_mangle`](https://doc.rust-lang.org/stable/reference/abi.html#the-no_mangle-attribute) attributed items
- Item names in [external blocks](https://doc.rust-lang.org/stable/reference/items/external-blocks.html)

## [Normalization](#normalization)

Identifiers are normalized using Normalization Form C (NFC) as defined in [Unicode Standard Annex #15](https://www.unicode.org/reports/tr15/tr15-57.html). Two identifiers are equal if their NFC forms are equal.

[Procedural](https://doc.rust-lang.org/stable/reference/procedural-macros.html) and [declarative](https://doc.rust-lang.org/stable/reference/macros-by-example.html) macros receive normalized identifiers in their input.

## [Raw identifiers](#raw-identifiers)

A raw identifier is like a normal identifier, but prefixed by `r#`. (Note that the `r#` prefix is not included as part of the actual identifier.)

Unlike a normal identifier, a raw identifier may be any strict or reserved keyword except the ones listed above for `RAW_IDENTIFIER`.

It is an error to use the [RESERVED\_RAW\_IDENTIFIER](https://doc.rust-lang.org/stable/reference/identifiers.html#grammar-RESERVED_RAW_IDENTIFIER) token.