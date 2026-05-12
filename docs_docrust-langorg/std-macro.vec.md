---
title: vec in std - Rust
url: https://doc.rust-lang.org/std/macro.vec.html
source: crawler
fetched_at: 2026-05-06T21:32:36.902810467-03:00
rendered_js: false
word_count: 147
summary: This document describes the Rust vec! macro, which provides a convenient syntax for initializing Vec collections with either specific elements or a repeated value.
tags:
    - rust
    - macros
    - vector
    - collection-initialization
    - std-library
category: reference
---

```rust
macro_rules! vec {
    () => { ... };
    ($elem:expr; $n:expr) => { ... };
    ($($x:expr),+ $(,)?) => { ... };
}
```

Expand description

Creates a [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") containing the arguments.

`vec!` allows `Vec`s to be defined with the same syntax as array expressions. There are two forms of this macro:

- Create a [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") containing a given list of elements:

```rust
let v = vec![1, 2, 3];
assert_eq!(v[0], 1);
assert_eq!(v[1], 2);
assert_eq!(v[2], 3);
```

- Create a [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") from a given element and size:

```rust
let v = vec![1; 3];
assert_eq!(v, [1, 1, 1]);
```

Note that unlike array expressions this syntax supports all elements which implement [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") and the number of elements doesn’t have to be a constant.

This will use `clone` to duplicate an expression, so one should be careful using this with types having a nonstandard `Clone` implementation. For example, `vec![Rc::new(1); 5]` will create a vector of five references to the same boxed integer value, not five references pointing to independently boxed integers.

Also, note that `vec![expr; 0]` is allowed, and produces an empty vector. This will still evaluate `expr`, however, and immediately drop the resulting value, so be mindful of side effects.