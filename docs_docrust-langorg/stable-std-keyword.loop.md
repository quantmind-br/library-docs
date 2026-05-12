---
title: loop - Rust
url: https://doc.rust-lang.org/stable/std/keyword.loop.html
source: crawler
fetched_at: 2026-05-06T21:28:52.483884219-03:00
rendered_js: false
word_count: 92
summary: This document explains the functionality of the 'loop' expression in Rust, detailing its use for infinite iteration and its ability to return values via the break keyword.
tags:
    - rust-programming
    - control-flow
    - loop-expression
    - iteration
    - rust-language
category: concept
---

Expand description

Loop indefinitely.

`loop` is used to define the simplest kind of loop supported in Rust. It runs the code inside it until the code uses `break` or the program exits.

```rust
loop {
    println!("hello world forever!");
}

let mut i = 1;
loop {
    println!("i is {i}");
    if i > 100 {
        break;
    }
    i *= 2;
}
assert_eq!(i, 128);
```

Unlike the other kinds of loops in Rust (`while`, `while let`, and `for`), loops can be used as expressions that return values via `break`.

```rust
let mut i = 1;
let something = loop {
    i *= 2;
    if i > 100 {
        break i;
    }
};
assert_eq!(something, 128);
```

Every `break` in a loop has to have the same type. When it’s not explicitly giving something, `break;` returns `()`.

For more information on `loop` and loops in general, see the [Reference](https://doc.rust-lang.org/stable/reference/expressions/loop-expr.html).

See also, [`for`](https://doc.rust-lang.org/stable/std/keyword.for.html), [`while`](https://doc.rust-lang.org/stable/std/keyword.while.html).