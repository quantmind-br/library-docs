---
title: todo in std - Rust
url: https://doc.rust-lang.org/std/macro.todo.html
source: crawler
fetched_at: 2026-05-06T21:32:35.152277657-03:00
rendered_js: false
word_count: 153
summary: This document explains the usage and purpose of the Rust todo! macro, which serves as a placeholder for unfinished code by triggering a panic during execution.
tags:
    - rust-macros
    - error-handling
    - prototyping
    - code-placeholders
    - panic-macros
category: reference
---

## Macro todo

1.40.0 · [Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#879)

```rust
macro_rules! todo {
    () => { ... };
    ($($arg:tt)+) => { ... };
}
```

Expand description

Indicates unfinished code.

This can be useful if you are prototyping and just want a placeholder to let your code pass type analysis.

The difference between [`unimplemented!`](https://doc.rust-lang.org/std/macro.unimplemented.html "macro std::unimplemented") and `todo!` is that while `todo!` conveys an intent of implementing the functionality later and the message is “not yet implemented”, `unimplemented!` makes no such claims. Its message is “not implemented”.

Also, some IDEs will mark `todo!`s.

## [§](#panics)Panics

This will always [`panic!`](https://doc.rust-lang.org/core/macro.panic.html "macro core::panic") because `todo!` is just a shorthand for `panic!` with a fixed, specific message.

Like `panic!`, this macro has a second form for displaying custom values.

## [§](#examples)Examples

Here’s an example of some in-progress code. We have a trait `Foo`:

```rust
trait Foo {
    fn bar(&self) -> u8;
    fn baz(&self);
    fn qux(&self) -> Result<u64, ()>;
}
```

We want to implement `Foo` on one of our types, but we also want to work on just `bar()` first. In order for our code to compile, we need to implement `baz()` and `qux()`, so we can use `todo!`:

```rust
struct MyStruct;

impl Foo for MyStruct {
    fn bar(&self) -> u8 {
        1 + 1
    }

    fn baz(&self) {
        // Let's not worry about implementing baz() for now
        todo!();
    }

    fn qux(&self) -> Result<u64, ()> {
        // We can add a message to todo! to display our omission.
        // This will display:
        // "thread 'main' panicked at 'not yet implemented: MyStruct is not yet quxable'".
        todo!("MyStruct is not yet quxable");
    }
}

fn main() {
    let s = MyStruct;
    s.bar();

    // We aren't even using baz() or qux(), so this is fine.
}
```