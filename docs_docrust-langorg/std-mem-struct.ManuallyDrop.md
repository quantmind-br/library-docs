---
title: ManuallyDrop in std::mem - Rust
url: https://doc.rust-lang.org/std/mem/struct.ManuallyDrop.html
source: crawler
fetched_at: 2026-05-06T21:36:19.011160412-03:00
rendered_js: false
word_count: 856
summary: ManuallyDrop is a wrapper type in Rust that suppresses the compiler's automatic destructor invocation for the wrapped value, providing a safe way to control drop timing and behavior.
tags:
    - rust
    - memory-management
    - destructors
    - unsafe-rust
    - manual-memory-control
category: reference
---

## Struct ManuallyDrop

1.20.0 · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#161)

```rust
pub struct ManuallyDrop<T>
where
    T: ?Sized,{ /* private fields */ }
```

Expand description

A wrapper to inhibit the compiler from automatically calling `T`’s destructor. This wrapper is 0-cost.

`ManuallyDrop<T>` is guaranteed to have the same layout and bit validity as `T`, and is subject to the same layout optimizations as `T`. As a consequence, it has *no effect* on the assumptions that the compiler makes about its contents. For example, initializing a `ManuallyDrop<&mut T>` with [`mem::zeroed`](https://doc.rust-lang.org/std/mem/fn.zeroed.html "fn std::mem::zeroed") is undefined behavior. If you need to handle uninitialized data, use [`MaybeUninit<T>`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit") instead.

Note that accessing the value inside a `ManuallyDrop<T>` is safe. This means that a `ManuallyDrop<T>` whose content has been dropped must not be exposed through a public safe API. Correspondingly, `ManuallyDrop::drop` is unsafe.

## [§](#manuallydrop-and-drop-order)`ManuallyDrop` and drop order

Rust has a well-defined [drop order](https://doc.rust-lang.org/reference/destructors.html) of values. To make sure that fields or locals are dropped in a specific order, reorder the declarations such that the implicit drop order is the correct one.

It is possible to use `ManuallyDrop` to control the drop order, but this requires unsafe code and is hard to do correctly in the presence of unwinding.

For example, if you want to make sure that a specific field is dropped after the others, make it the last field of a struct:

```rust
struct Context;

struct Widget {
    children: Vec<Widget>,
    // `context` will be dropped after `children`.
    // Rust guarantees that fields are dropped in the order of declaration.
    context: Context,
}
```

## [§](#interaction-with-box)Interaction with `Box`

Currently, if you have a `ManuallyDrop<T>`, where the type `T` is a `Box` or contains a `Box` inside, then dropping the `T` followed by moving the `ManuallyDrop<T>` is [considered to be undefined behavior](https://github.com/rust-lang/unsafe-code-guidelines/issues/245). That is, the following code causes undefined behavior:

```rust
use std::mem::ManuallyDrop;

let mut x = ManuallyDrop::new(Box::new(42));
unsafe {
    ManuallyDrop::drop(&mut x);
}
let y = x; // Undefined behavior!
```

This is [likely to change in the future](https://rust-lang.github.io/rfcs/3336-maybe-dangling.html). In the meantime, consider using [`MaybeUninit`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit") instead.

## [§](#safety-hazards-when-storing-manuallydrop-in-a-struct-or-an-enum)Safety hazards when storing `ManuallyDrop` in a struct or an enum.

Special care is needed when all of the conditions below are met:

- A struct or enum contains a `ManuallyDrop`.
- The `ManuallyDrop` is not inside a `union`.
- The struct or enum is part of public API, or is stored in a struct or an enum that is part of public API.
- There is code that drops the contents of the `ManuallyDrop` field, and this code is outside the struct or enum’s `Drop` implementation.

In particular, the following hazards may occur:

##### [§](#storing-generic-types)Storing generic types

If the `ManuallyDrop` contains a client-supplied generic type, the client might provide a `Box` as that type. This would cause undefined behavior when the struct or enum is later moved, as mentioned in the previous section. For example, the following code causes undefined behavior:

```rust
use std::mem::ManuallyDrop;

pub struct BadOption<T> {
    // Invariant: Has been dropped if `is_some` is false.
    value: ManuallyDrop<T>,
    is_some: bool,
}
impl<T> BadOption<T> {
    pub fn new(value: T) -> Self {
        Self { value: ManuallyDrop::new(value), is_some: true }
    }
    pub fn change_to_none(&mut self) {
        if self.is_some {
            self.is_some = false;
            unsafe {
                // SAFETY: `value` hasn't been dropped yet, as per the invariant
                // (This is actually unsound!)
                ManuallyDrop::drop(&mut self.value);
            }
        }
    }
}

// In another crate:

let mut option = BadOption::new(Box::new(42));
option.change_to_none();
let option2 = option; // Undefined behavior!
```

##### [§](#deriving-traits)Deriving traits

Deriving `Debug`, `Clone`, `PartialEq`, `PartialOrd`, `Ord`, or `Hash` on the struct or enum could be unsound, since the derived implementations of these traits would access the `ManuallyDrop` field. For example, the following code causes undefined behavior:

```rust
use std::mem::ManuallyDrop;

// This derive is unsound in combination with the `ManuallyDrop::drop` call.
#[derive(Debug)]
pub struct Foo {
    value: ManuallyDrop<String>,
}
impl Foo {
    pub fn new() -> Self {
        let mut temp = Self {
            value: ManuallyDrop::new(String::from("Unsafe rust is hard."))
        };
        unsafe {
            // SAFETY: `value` hasn't been dropped yet.
            ManuallyDrop::drop(&mut temp.value);
        }
        temp
    }
}

// In another crate:

let foo = Foo::new();
println!("{:?}", foo); // Undefined behavior!
```

[Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#165)[§](#impl-ManuallyDrop%3CT%3E)

1.20.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#184)

Wrap a value to be manually dropped.

##### [§](#examples)Examples

```rust
use std::mem::ManuallyDrop;
let mut x = ManuallyDrop::new(String::from("Hello World!"));
x.truncate(5); // You can still safely operate on the value
assert_eq!(*x, "Hello");
// But `Drop` will not be run here
```

1.20.0 (const: 1.32.0) · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#202)

Extracts the value from the `ManuallyDrop` container.

This allows the value to be dropped again.

##### [§](#examples-1)Examples

```rust
use std::mem::ManuallyDrop;
let x = ManuallyDrop::new(Box::new(()));
let _: Box<()> = ManuallyDrop::into_inner(x); // This drops the `Box`.
```

1.42.0 (const: [unstable](https://github.com/rust-lang/rust/issues/148773 "Tracking issue for const_manually_drop_take")) · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#227)

Takes the value from the `ManuallyDrop<T>` container out.

This method is primarily intended for moving out values in drop. Instead of using [`ManuallyDrop::drop`](https://doc.rust-lang.org/std/mem/struct.ManuallyDrop.html#method.drop "associated function std::mem::ManuallyDrop::drop") to manually drop the value, you can use this method to take the value and use it however desired.

Whenever possible, it is preferable to use [`into_inner`](https://doc.rust-lang.org/std/mem/struct.ManuallyDrop.html#method.into_inner "associated function std::mem::ManuallyDrop::into_inner") instead, which prevents duplicating the content of the `ManuallyDrop<T>`.

##### [§](#safety)Safety

This function semantically moves out the contained value without preventing further usage, leaving the state of this container unchanged. It is your responsibility to ensure that this `ManuallyDrop` is not used again.

[Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#234)[§](#impl-ManuallyDrop%3CT%3E-1)

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/109342 "Tracking issue for const_drop_in_place")) · [Source](https://doc.rust-lang.org/src/core/mem/manually_drop.rs.html#260-262)

Manually drops the contained value.

This is exactly equivalent to calling [`ptr::drop_in_place`](https://doc.rust-lang.org/std/ptr/fn.drop_in_place.html "fn std::ptr::drop_in_place") with a pointer to the contained value. As such, unless the contained value is a packed struct, the destructor will be called in-place without moving the value, and thus can be used to safely drop [pinned](https://doc.rust-lang.org/std/pin/index.html "mod std::pin") data.

If you have ownership of the value, you can use [`ManuallyDrop::into_inner`](https://doc.rust-lang.org/std/mem/struct.ManuallyDrop.html#method.into_inner "associated function std::mem::ManuallyDrop::into_inner") instead.

##### [§](#safety-1)Safety

This function runs the destructor of the contained value. Other than changes made by the destructor itself, the memory is left unchanged, and so as far as the compiler is concerned still holds a bit-pattern which is valid for the type `T`.

However, this “zombie” value should not be exposed to safe code, and this function should not be called more than once. To use a value after it’s been dropped, or drop a value multiple times, can cause Undefined Behavior (depending on what `drop` does). This is normally prevented by the type system, but users of `ManuallyDrop` must uphold those guarantees without assistance from the compiler.