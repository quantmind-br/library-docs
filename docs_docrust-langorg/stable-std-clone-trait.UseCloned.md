---
title: UseCloned in std::clone - Rust
url: https://doc.rust-lang.org/stable/std/clone/trait.UseCloned.html
source: crawler
fetched_at: 2026-05-06T21:26:21.793758779-03:00
rendered_js: false
word_count: 188
summary: This document defines the UseCloned trait, an experimental Rust feature used to mark types with lightweight cloning behavior and enable the ergonomic .use postfix syntax.
tags:
    - rust-language
    - experimental-api
    - trait-design
    - memory-management
    - syntax-extension
    - ergonomic-clones
category: reference
---

```rust
pub trait UseCloned: Clone { }
```

🔬This is a nightly-only experimental API. (`ergonomic_clones` [#132290](https://github.com/rust-lang/rust/issues/132290))

Expand description

Trait for objects whose [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone") impl is lightweight (e.g. reference-counted)

Cloning an object implementing this trait should in general:

- be O(1) (constant) time regardless of the amount of data managed by the object,
- not require a memory allocation,
- not require copying more than roughly 64 bytes (a typical cache line size),
- not block the current thread,
- not have any semantic side effects (e.g. allocating a file descriptor), and
- not have overhead larger than a couple of atomic operations.

The `UseCloned` trait does not provide a method; instead, it indicates that `Clone::clone` is lightweight, and allows the use of the `.use` syntax.

### [§](#use-postfix-syntax).use postfix syntax

Values can be `.use`d by adding `.use` postfix to the value you want to use.

[ⓘ](# "This example is not tested")

```rust
fn foo(f: Foo) {
    // if `Foo` implements `Copy` f would be copied into x.
    // if `Foo` implements `UseCloned` f would be cloned into x.
    // otherwise f would be moved into x.
    let x = f.use;
    // ...
}
```

### [§](#use-closures)use closures

Use closures allow captured values to be automatically used. This is similar to have a closure that you would call `.use` over each captured value.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*