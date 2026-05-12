---
title: Receiver in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Receiver.html#associatedtype.Target
source: crawler
fetched_at: 2026-05-06T21:24:09.609101943-03:00
rendered_js: false
word_count: 192
summary: This document describes the Receiver trait in Rust, which allows custom types to be used as method receivers, enabling smart pointers to support custom self-referential patterns.
tags:
    - rust
    - receiver-trait
    - smart-pointers
    - method-dispatch
    - arbitrary-self-types
    - nightly-api
category: reference
---

```rust
pub trait Receiver {
    type Target: ?Sized;
}
```

🔬This is a nightly-only experimental API. (`arbitrary_self_types` [#44874](https://github.com/rust-lang/rust/issues/44874))

Expand description

Indicates that a struct can be used as a method receiver. That is, a type can use this type as a type of `self`, like this:

[ⓘ](# "This example deliberately fails to compile")

```rust
use std::ops::Receiver;

struct SmartPointer<T>(T);

impl<T> Receiver for SmartPointer<T> {
   type Target = T;
}

struct MyContainedType;

impl MyContainedType {
  fn method(self: SmartPointer<Self>) {
    // ...
  }
}

fn main() {
  let ptr = SmartPointer(MyContainedType);
  ptr.method();
}
```

This trait is blanket implemented for any type which implements [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref"), which includes stdlib pointer types like `Box<T>`,`Rc<T>`, `&T`, and `Pin<P>`. For that reason, it’s relatively rare to need to implement this directly. You’ll typically do this only if you need to implement a smart pointer type which can’t implement [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref"); perhaps because you’re interfacing with another programming language and can’t guarantee that references comply with Rust’s aliasing rules.

When looking for method candidates, Rust will explore a chain of possible `Receiver`s, so for example each of the following methods work:

```rust
use std::boxed::Box;
use std::rc::Rc;

// Both `Box` and `Rc` (indirectly) implement Receiver

struct MyContainedType;

fn main() {
  let t = Rc::new(Box::new(MyContainedType));
  t.method_a();
  t.method_b();
  t.method_c();
}

impl MyContainedType {
  fn method_a(&self) {

  }
  fn method_b(self: &Box<Self>) {

  }
  fn method_c(self: &Rc<Box<Self>>) {

  }
}
```

[Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#374)

🔬This is a nightly-only experimental API. (`arbitrary_self_types` [#44874](https://github.com/rust-lang/rust/issues/44874))

The target type on which the method may be called.