---
title: std::borrow - Rust
url: https://doc.rust-lang.org/stable/std/borrow/index.html
source: crawler
fetched_at: 2026-05-06T21:25:29.110027847-03:00
rendered_js: true
word_count: 46
summary: This document provides an overview of the Rust standard library's borrow module, which offers utilities and traits for managing borrowed and owned data efficiently.
tags:
    - rust-language
    - memory-management
    - smart-pointers
    - borrow-checker
    - traits
    - data-ownership
category: reference
---

[std](https://doc.rust-lang.org/stable/std/index.html)

## Module borrow

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/lib.rs.html#219)

[Search](https://doc.rust-lang.org/stable/std/borrow/index.html?search=)

[Settings](https://doc.rust-lang.org/stable/settings.html)

[Help](https://doc.rust-lang.org/stable/help.html)

Expand description

A module for working with borrowed data.

## Enums[§](#enums)

[Cow](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow")

A clone-on-write smart pointer.

## Traits[§](#traits)

[Borrow](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html "trait std::borrow::Borrow")

A trait for borrowing data.

[BorrowMut](https://doc.rust-lang.org/stable/std/borrow/trait.BorrowMut.html "trait std::borrow::BorrowMut")

A trait for mutably borrowing data.

[ToOwned](https://doc.rust-lang.org/stable/std/borrow/trait.ToOwned.html "trait std::borrow::ToOwned")

A generalization of `Clone` to borrowed data.