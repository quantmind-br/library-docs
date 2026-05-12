---
title: super - Rust
url: https://doc.rust-lang.org/std/keyword.super.html
source: crawler
fetched_at: 2026-05-06T21:32:48.726447917-03:00
rendered_js: true
word_count: 35
summary: This document explains the usage of the 'super' keyword in Rust for accessing items defined in the parent module.
tags:
    - rust-language
    - module-system
    - path-resolution
    - namespace-access
category: reference
---

## Keyword super

[Source](https://doc.rust-lang.org/src/std/keyword_docs.rs.html#1773)

[Search](https://doc.rust-lang.org/std/keyword.super.html?search=)

[Settings](https://doc.rust-lang.org/settings.html)

[Help](https://doc.rust-lang.org/help.html)

Expand description

The parent of the current [module](https://doc.rust-lang.org/reference/items/modules.html).

```rust
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        super::a::foo(); // call a's foo function
    }
}
```

It is also possible to use `super` multiple times: `super::super::foo`, going up the ancestor chain.

See the [Reference](https://doc.rust-lang.org/reference/paths.html#super) for more information.