---
title: drop in std::mem - Rust
url: https://doc.rust-lang.org/stable/std/mem/fn.drop.html
source: crawler
fetched_at: 2026-05-06T21:25:27.957112534-03:00
rendered_js: false
word_count: 137
summary: Explains the purpose and behavior of the drop function in Rust, which manually triggers the disposal of a value by consuming it.
tags:
    - rust-standard-library
    - memory-management
    - ownership-model
    - drop-trait
    - resource-cleanup
category: reference
---

## Function drop

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/133214 "Tracking issue for const_destruct")) · [Source](https://doc.rust-lang.org/stable/src/core/mem/mod.rs.html#971-973)

```rust
pub fn drop<T>(_x: T)
```

Expand description

Disposes of a value.

This effectively does nothing for types which implement `Copy`, e.g. integers. Such values are copied and *then* moved into the function, so the value persists after this function call.

This function is not magic; it is literally defined as

Because `_x` is moved into the function, it is automatically [dropped](https://doc.rust-lang.org/stable/std/ops/trait.Drop.html "trait std::ops::Drop") before the function returns.

## [§](#examples)Examples

Basic usage:

```rust
let v = vec![1, 2, 3];

drop(v); // explicitly drop the vector
```

Since [`RefCell`](https://doc.rust-lang.org/stable/std/cell/struct.RefCell.html "struct std::cell::RefCell") enforces the borrow rules at runtime, `drop` can release a [`RefCell`](https://doc.rust-lang.org/stable/std/cell/struct.RefCell.html "struct std::cell::RefCell") borrow:

```rust
use std::cell::RefCell;

let x = RefCell::new(1);

let mut mutable_borrow = x.borrow_mut();
*mutable_borrow = 1;

drop(mutable_borrow); // relinquish the mutable borrow on this slot

let borrow = x.borrow();
println!("{}", *borrow);
```

Integers and other types implementing [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") are unaffected by `drop`.

```rust
#[derive(Copy, Clone)]
struct Foo(u8);

let x = 1;
let y = Foo(2);
drop(x); // a copy of `x` is moved and dropped
drop(y); // a copy of `y` is moved and dropped

println!("x: {}, y: {}", x, y.0); // still available
```