---
title: Rc in std::rc - Rust
url: https://doc.rust-lang.org/std/rc/struct.Rc.html
source: crawler
fetched_at: 2026-05-06T21:23:29.516196525-03:00
rendered_js: false
word_count: 4131
summary: This document provides technical documentation for the Rc struct in Rust, which is a single-threaded reference-counting pointer used for shared ownership. It outlines various associated functions for construction, memory allocation, and mapping.
tags:
    - rust
    - smart-pointers
    - reference-counting
    - memory-management
    - api-reference
    - rc
category: reference
---

```rust
pub struct Rc<T, A = Global>
where
    A: Allocator,
    T: ?Sized,{ /* private fields */ }
```

Expand description

A single-threaded reference-counting pointer. ‘Rc’ stands for ‘Reference Counted’.

See the [module-level documentation](https://doc.rust-lang.org/std/rc/index.html) for more details.

The inherent methods of `Rc` are all associated functions, which means that you have to call them as e.g., [`Rc::get_mut(&mut value)`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.get_mut "associated function std::rc::Rc::get_mut") instead of `value.get_mut()`. This avoids conflicts with methods of the inner type `T`.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#401)[§](#impl-Rc%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#413)

Constructs a new `Rc<T>`.

##### [§](#examples)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);
```

1.60.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#479-481)

Constructs a new `Rc<T>` while giving you a `Weak<T>` to the allocation, to allow you to construct a `T` which holds a weak pointer to itself.

Generally, a structure circularly referencing itself, either directly or indirectly, should not hold a strong reference to itself to prevent a memory leak. Using this function, you get access to the weak pointer during the initialization of `T`, before the `Rc<T>` is created, such that you can clone and store it inside the `T`.

`new_cyclic` first allocates the managed allocation for the `Rc<T>`, then calls your closure, giving it a `Weak<T>` to this allocation, and only afterwards completes the construction of the `Rc<T>` by placing the `T` returned from your closure into the allocation.

Since the new `Rc<T>` is not fully-constructed until `Rc<T>::new_cyclic` returns, calling [`upgrade`](https://doc.rust-lang.org/std/rc/struct.Weak.html#method.upgrade "method std::rc::Weak::upgrade") on the weak reference inside your closure will fail and result in a `None` value.

##### [§](#panics)Panics

If `data_fn` panics, the panic is propagated to the caller, and the temporary [`Weak<T>`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") is dropped normally.

##### [§](#examples-1)Examples

```rust
use std::rc::{Rc, Weak};

struct Gadget {
    me: Weak<Gadget>,
}

impl Gadget {
    /// Constructs a reference counted Gadget.
    fn new() -> Rc<Self> {
        // `me` is a `Weak<Gadget>` pointing at the new allocation of the
        // `Rc` we're constructing.
        Rc::new_cyclic(|me| {
            // Create the actual struct here.
            Gadget { me: me.clone() }
        })
    }

    /// Returns a reference counted pointer to Self.
    fn me(&self) -> Rc<Self> {
        self.me.upgrade().unwrap()
    }
}
```

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#505)

Constructs a new `Rc` with uninitialized contents.

##### [§](#examples-2)Examples

```rust
use std::rc::Rc;

let mut five = Rc::<u32>::new_uninit();

// Deferred initialization:
Rc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5)
```

1.92.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#536)

Constructs a new `Rc` with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-3)Examples

```rust
use std::rc::Rc;

let zero = Rc::<u32>::new_zeroed();
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0)
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#558)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc<T>`, returning an error if the allocation fails

##### [§](#examples-4)Examples

```rust
#![feature(allocator_api)]
use std::rc::Rc;

let five = Rc::try_new(5);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#595)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents, returning an error if the allocation fails

##### [§](#examples-5)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;

let mut five = Rc::<u32>::try_new_uninit()?;

// Deferred initialization:
Rc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#627)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents, with the memory being filled with `0` bytes, returning an error if the allocation fails

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-6)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;

let zero = Rc::<u32>::try_new_zeroed()?;
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0);
```

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#641)

Constructs a new `Pin<Rc<T>>`. If `T` does not implement `Unpin`, then `value` will be pinned in memory and unable to be moved.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#667)

🔬This is a nightly-only experimental API. (`smart_pointer_try_map` [#144419](https://github.com/rust-lang/rust/issues/144419))

Maps the value in an `Rc`, reusing the allocation if possible.

`f` is called on a reference to the value in the `Rc`, and the result is returned, also in an `Rc`.

Note: this is an associated function, which means that you have to call it as `Rc::map(r, f)` instead of `r.map(f)`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-7)Examples

```rust
#![feature(smart_pointer_try_map)]

use std::rc::Rc;

let r = Rc::new(7);
let new = Rc::map(r, |i| i + 7);
assert_eq!(*new, 14);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#707-713)

🔬This is a nightly-only experimental API. (`smart_pointer_try_map` [#144419](https://github.com/rust-lang/rust/issues/144419))

Attempts to map the value in an `Rc`, reusing the allocation if possible.

`f` is called on a reference to the value in the `Rc`, and if the operation succeeds, the result is returned, also in an `Rc`.

Note: this is an associated function, which means that you have to call it as `Rc::try_map(r, f)` instead of `r.try_map(f)`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-8)Examples

```rust
#![feature(smart_pointer_try_map)]

use std::rc::Rc;

let b = Rc::new(7);
let new = Rc::try_map(b, |&i| u32::try_from(i)).unwrap();
assert_eq!(*new, 7);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#733)[§](#impl-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#748)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` in the provided allocator.

##### [§](#examples-9)Examples

```rust
#![feature(allocator_api)]
use std::rc::Rc;
use std::alloc::System;

let five = Rc::new_in(5, System);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#782)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents in the provided allocator.

##### [§](#examples-10)Examples

```rust
#![feature(get_mut_unchecked)]
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let mut five = Rc::<u32, _>::new_uninit_in(System);

let five = unsafe {
    // Deferred initialization:
    Rc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);

    five.assume_init()
};

assert_eq!(*five, 5)
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#819)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents, with the memory being filled with `0` bytes, in the provided allocator.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-11)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let zero = Rc::<u32, _>::new_zeroed_in(System);
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0)
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#863-865)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc<T, A>` in the given allocator while giving you a `Weak<T, A>` to the allocation, to allow you to construct a `T` which holds a weak pointer to itself.

Generally, a structure circularly referencing itself, either directly or indirectly, should not hold a strong reference to itself to prevent a memory leak. Using this function, you get access to the weak pointer during the initialization of `T`, before the `Rc<T, A>` is created, such that you can clone and store it inside the `T`.

`new_cyclic_in` first allocates the managed allocation for the `Rc<T, A>`, then calls your closure, giving it a `Weak<T, A>` to this allocation, and only afterwards completes the construction of the `Rc<T, A>` by placing the `T` returned from your closure into the allocation.

Since the new `Rc<T, A>` is not fully-constructed until `Rc<T, A>::new_cyclic_in` returns, calling [`upgrade`](https://doc.rust-lang.org/std/rc/struct.Weak.html#method.upgrade "method std::rc::Weak::upgrade") on the weak reference inside your closure will fail and result in a `None` value.

##### [§](#panics-1)Panics

If `data_fn` panics, the panic is propagated to the caller, and the temporary [`Weak<T, A>`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") is dropped normally.

##### [§](#examples-12)Examples

See [`new_cyclic`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.new_cyclic "associated function std::rc::Rc::new_cyclic").

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#925)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc<T>` in the provided allocator, returning an error if the allocation fails

##### [§](#examples-13)Examples

```rust
#![feature(allocator_api)]
use std::rc::Rc;
use std::alloc::System;

let five = Rc::try_new_in(5, System);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#963)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents, in the provided allocator, returning an error if the allocation fails

##### [§](#examples-14)Examples

```rust
#![feature(allocator_api)]
#![feature(get_mut_unchecked)]

use std::rc::Rc;
use std::alloc::System;

let mut five = Rc::<u32, _>::try_new_uninit_in(System)?;

let five = unsafe {
    // Deferred initialization:
    Rc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);

    five.assume_init()
};

assert_eq!(*five, 5);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1001)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Rc` with uninitialized contents, with the memory being filled with `0` bytes, in the provided allocator, returning an error if the allocation fails

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-15)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let zero = Rc::<u32, _>::try_new_zeroed_in(System)?;
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1019-1021)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Pin<Rc<T>>` in the provided allocator. If `T` does not implement `Unpin`, then `value` will be pinned in memory and unable to be moved.

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1047)

Returns the inner value, if the `Rc` has exactly one strong reference.

Otherwise, an [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned with the same `Rc` that was passed in.

This will succeed even if there are outstanding weak references.

##### [§](#examples-16)Examples

```rust
use std::rc::Rc;

let x = Rc::new(3);
assert_eq!(Rc::try_unwrap(x), Ok(3));

let x = Rc::new(4);
let _y = Rc::clone(&x);
assert_eq!(*Rc::try_unwrap(x).unwrap_err(), 4);
```

1.70.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1098)

Returns the inner value, if the `Rc` has exactly one strong reference.

Otherwise, [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is returned and the `Rc` is dropped.

This will succeed even if there are outstanding weak references.

If `Rc::into_inner` is called on every clone of this `Rc`, it is guaranteed that exactly one of the calls returns the inner value. This means in particular that the inner value is not dropped.

[`Rc::try_unwrap`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.try_unwrap "associated function std::rc::Rc::try_unwrap") is conceptually similar to `Rc::into_inner`. And while they are meant for different use-cases, `Rc::into_inner(this)` is in fact equivalent to `Rc::try_unwrap(this).ok()`. (Note that the same kind of equivalence does **not** hold true for [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc"), due to race conditions that do not apply to `Rc`!)

##### [§](#examples-17)Examples

```rust
use std::rc::Rc;

let x = Rc::new(3);
assert_eq!(Rc::into_inner(x), Some(3));

let x = Rc::new(4);
let y = Rc::clone(&x);

assert_eq!(Rc::into_inner(y), None);
assert_eq!(Rc::into_inner(x), Some(4));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1103)[§](#impl-Rc%3C%5BT%5D%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1126)

Constructs a new reference-counted slice with uninitialized contents.

##### [§](#examples-18)Examples

```rust
use std::rc::Rc;

let mut values = Rc::<[u32]>::new_uninit_slice(3);

// Deferred initialization:
let data = Rc::get_mut(&mut values).unwrap();
data[0].write(1);
data[1].write(2);
data[2].write(3);

let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

1.92.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1151)

Constructs a new reference-counted slice with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-19)Examples

```rust
use std::rc::Rc;

let values = Rc::<[u32]>::new_zeroed_slice(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1172)

🔬This is a nightly-only experimental API. (`alloc_slice_into_array` [#148082](https://github.com/rust-lang/rust/issues/148082))

Converts the reference-counted slice into a reference-counted array.

This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1185)[§](#impl-Rc%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1213)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new reference-counted slice with uninitialized contents.

##### [§](#examples-20)Examples

```rust
#![feature(get_mut_unchecked)]
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let mut values = Rc::<[u32], _>::new_uninit_slice_in(3, System);

let values = unsafe {
    // Deferred initialization:
    Rc::get_mut_unchecked(&mut values)[0].as_mut_ptr().write(1);
    Rc::get_mut_unchecked(&mut values)[1].as_mut_ptr().write(2);
    Rc::get_mut_unchecked(&mut values)[2].as_mut_ptr().write(3);

    values.assume_init()
};

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1241)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new reference-counted slice with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-21)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let values = Rc::<[u32], _>::new_zeroed_slice_in(3, System);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1258)[§](#impl-Rc%3CMaybeUninit%3CT%3E,+A%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1287)

Converts to `Rc<T>`.

##### [§](#safety)Safety

As with [`MaybeUninit::assume_init`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.assume_init "method std::mem::MaybeUninit::assume_init"), it is up to the caller to guarantee that the inner value really is in an initialized state. Calling this when the content is not yet fully initialized causes immediate undefined behavior.

##### [§](#examples-22)Examples

```rust
use std::rc::Rc;

let mut five = Rc::<u32>::new_uninit();

// Deferred initialization:
Rc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5)
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1293)[§](#impl-Rc%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1306)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Rc<T>` with a clone of `value`.

##### [§](#examples-23)Examples

```rust
#![feature(clone_from_ref)]
use std::rc::Rc;

let hello: Rc<str> = Rc::clone_from_ref("hello");
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1324)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Rc<T>` with a clone of `value`, returning an error if allocation fails

##### [§](#examples-24)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::rc::Rc;

let hello: Rc<str> = Rc::try_clone_from_ref("hello")?;
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1329)[§](#impl-Rc%3CT,+A%3E-1)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1345)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Rc<T>` with a clone of `value` in the provided allocator.

##### [§](#examples-25)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::rc::Rc;
use std::alloc::System;

let hello: Rc<str, System> = Rc::clone_from_ref_in("hello", System);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1375)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Rc<T>` with a clone of `value` in the provided allocator, returning an error if allocation fails

##### [§](#examples-26)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::rc::Rc;
use std::alloc::System;

let hello: Rc<str, System> = Rc::try_clone_from_ref_in("hello", System)?;
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1391)[§](#impl-Rc%3C%5BMaybeUninit%3CT%3E%5D,+A%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1423)

Converts to `Rc<[T]>`.

##### [§](#safety-1)Safety

As with [`MaybeUninit::assume_init`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.assume_init "method std::mem::MaybeUninit::assume_init"), it is up to the caller to guarantee that the inner value really is in an initialized state. Calling this when the content is not yet fully initialized causes immediate undefined behavior.

##### [§](#examples-27)Examples

```rust
use std::rc::Rc;

let mut values = Rc::<[u32]>::new_uninit_slice(3);

// Deferred initialization:
let data = Rc::get_mut(&mut values).unwrap();
data[0].write(1);
data[1].write(2);
data[2].write(3);

let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1429)[§](#impl-Rc%3CT%3E-2)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1493)

Constructs an `Rc<T>` from a raw pointer.

The raw pointer must have been previously returned by a call to [`Rc<U>::into_raw`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.into_raw "associated function std::rc::Rc::into_raw") with the following requirements:

- If `U` is sized, it must have the same size and alignment as `T`. This is trivially true if `U` is `T`.
- If `U` is unsized, its data pointer must have the same size and alignment as `T`. This is trivially true if `Rc<U>` was constructed through `Rc<T>` and then converted to `Rc<U>` through an [unsized coercion](https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions).

Note that if `U` or `U`’s data pointer is not `T` but has the same size and alignment, this is basically like transmuting references of different types. See [`mem::transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html "fn std::mem::transmute") for more information on what restrictions apply in this case.

The raw pointer must point to a block of memory allocated by the global allocator

The user of `from_raw` has to make sure a specific value of `T` is only dropped once.

This function is unsafe because improper use may lead to memory unsafety, even if the returned `Rc<T>` is never accessed.

##### [§](#examples-28)Examples

```rust
use std::rc::Rc;

let x = Rc::new("hello".to_owned());
let x_ptr = Rc::into_raw(x);

unsafe {
    // Convert back to an `Rc` to prevent leak.
    let x = Rc::from_raw(x_ptr);
    assert_eq!(&*x, "hello");

    // Further calls to `Rc::from_raw(x_ptr)` would be memory-unsafe.
}

// The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
```

Convert a slice back into its original array:

```rust
use std::rc::Rc;

let x: Rc<[u32]> = Rc::new([1, 2, 3]);
let x_ptr: *const [u32] = Rc::into_raw(x);

unsafe {
    let x: Rc<[u32; 3]> = Rc::from_raw(x_ptr.cast::<[u32; 3]>());
    assert_eq!(&*x, &[1, 2, 3]);
}
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1516)

Consumes the `Rc`, returning the wrapped pointer.

To avoid a memory leak the pointer must be converted back to an `Rc` using [`Rc::from_raw`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw "associated function std::rc::Rc::from_raw").

##### [§](#examples-29)Examples

```rust
use std::rc::Rc;

let x = Rc::new("hello".to_owned());
let x_ptr = Rc::into_raw(x);
assert_eq!(unsafe { &*x_ptr }, "hello");
```

1.53.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1553)

Increments the strong reference count on the `Rc<T>` associated with the provided pointer by one.

##### [§](#safety-2)Safety

The pointer must have been obtained through `Rc::into_raw` and must satisfy the same layout requirements specified in [`Rc::from_raw_in`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw_in "associated function std::rc::Rc::from_raw_in"). The associated `Rc` instance must be valid (i.e. the strong count must be at least 1) for the duration of this method, and `ptr` must point to a block of memory allocated by the global allocator.

##### [§](#examples-30)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

unsafe {
    let ptr = Rc::into_raw(five);
    Rc::increment_strong_count(ptr);

    let five = Rc::from_raw(ptr);
    assert_eq!(2, Rc::strong_count(&five));
}
```

1.53.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1590)

Decrements the strong reference count on the `Rc<T>` associated with the provided pointer by one.

##### [§](#safety-3)Safety

The pointer must have been obtained through `Rc::into_raw`and must satisfy the same layout requirements specified in [`Rc::from_raw_in`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw_in "associated function std::rc::Rc::from_raw_in"). The associated `Rc` instance must be valid (i.e. the strong count must be at least 1) when invoking this method, and `ptr` must point to a block of memory allocated by the global allocator. This method can be used to release the final `Rc` and backing storage, but **should not** be called after the final `Rc` has been released.

##### [§](#examples-31)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

unsafe {
    let ptr = Rc::into_raw(five);
    Rc::increment_strong_count(ptr);

    let five = Rc::from_raw(ptr);
    assert_eq!(2, Rc::strong_count(&five));
    Rc::decrement_strong_count(ptr);
    assert_eq!(1, Rc::strong_count(&five));
}
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1595)[§](#impl-Rc%3CT,+A%3E-2)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1603)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Returns a reference to the underlying allocator.

Note: this is an associated function, which means that you have to call it as `Rc::allocator(&r)` instead of `r.allocator()`. This is so that there is no conflict with a method on the inner type.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1627)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Consumes the `Rc`, returning the wrapped pointer and allocator.

To avoid a memory leak the pointer must be converted back to an `Rc` using [`Rc::from_raw_in`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw_in "associated function std::rc::Rc::from_raw_in").

##### [§](#examples-32)Examples

```rust
#![feature(allocator_api)]
use std::rc::Rc;
use std::alloc::System;

let x = Rc::new_in("hello".to_owned(), System);
let (ptr, alloc) = Rc::into_raw_with_allocator(x);
assert_eq!(unsafe { &*ptr }, "hello");
let x = unsafe { Rc::from_raw_in(ptr, alloc) };
assert_eq!(&*x, "hello");
```

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1653)

Provides a raw pointer to the data.

The counts are not affected in any way and the `Rc` is not consumed. The pointer is valid for as long as there are strong counts in the `Rc`.

##### [§](#examples-33)Examples

```rust
use std::rc::Rc;

let x = Rc::new(0);
let y = Rc::clone(&x);
let x_ptr = Rc::as_ptr(&x);
assert_eq!(x_ptr, Rc::as_ptr(&y));
assert_eq!(unsafe { *x_ptr }, 0);
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1730)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs an `Rc<T, A>` from a raw pointer in the provided allocator.

The raw pointer must have been previously returned by a call to [`Rc<U, A>::into_raw`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.into_raw "associated function std::rc::Rc::into_raw") with the following requirements:

- If `U` is sized, it must have the same size and alignment as `T`. This is trivially true if `U` is `T`.
- If `U` is unsized, its data pointer must have the same size and alignment as `T`. This is trivially true if `Rc<U>` was constructed through `Rc<T>` and then converted to `Rc<U>` through an [unsized coercion](https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions).

Note that if `U` or `U`’s data pointer is not `T` but has the same size and alignment, this is basically like transmuting references of different types. See [`mem::transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html "fn std::mem::transmute") for more information on what restrictions apply in this case.

The raw pointer must point to a block of memory allocated by `alloc`

The user of `from_raw` has to make sure a specific value of `T` is only dropped once.

This function is unsafe because improper use may lead to memory unsafety, even if the returned `Rc<T>` is never accessed.

##### [§](#examples-34)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let x = Rc::new_in("hello".to_owned(), System);
let (x_ptr, _alloc) = Rc::into_raw_with_allocator(x);

unsafe {
    // Convert back to an `Rc` to prevent leak.
    let x = Rc::from_raw_in(x_ptr, System);
    assert_eq!(&*x, "hello");

    // Further calls to `Rc::from_raw(x_ptr)` would be memory-unsafe.
}

// The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
```

Convert a slice back into its original array:

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let x: Rc<[u32], _> = Rc::new_in([1, 2, 3], System);
let x_ptr: *const [u32] = Rc::into_raw_with_allocator(x).0;

unsafe {
    let x: Rc<[u32; 3], _> = Rc::from_raw_in(x_ptr.cast::<[u32; 3]>(), System);
    assert_eq!(&*x, &[1, 2, 3]);
}
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1753-1755)

Creates a new [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointer to this allocation.

##### [§](#examples-35)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

let weak_five = Rc::downgrade(&five);
```

1.15.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1777)

Gets the number of [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers to this allocation.

##### [§](#examples-36)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);
let _weak_five = Rc::downgrade(&five);

assert_eq!(1, Rc::weak_count(&five));
```

1.15.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1795)

Gets the number of strong (`Rc`) pointers to this allocation.

##### [§](#examples-37)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);
let _also_five = Rc::clone(&five);

assert_eq!(2, Rc::strong_count(&five));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1834-1836)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Increments the strong reference count on the `Rc<T>` associated with the provided pointer by one.

##### [§](#safety-4)Safety

The pointer must have been obtained through `Rc::into_raw` and must satisfy the same layout requirements specified in [`Rc::from_raw_in`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw_in "associated function std::rc::Rc::from_raw_in"). The associated `Rc` instance must be valid (i.e. the strong count must be at least 1) for the duration of this method, and `ptr` must point to a block of memory allocated by `alloc`.

##### [§](#examples-38)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let five = Rc::new_in(5, System);

unsafe {
    let (ptr, _alloc) = Rc::into_raw_with_allocator(five);
    Rc::increment_strong_count_in(ptr, System);

    let five = Rc::from_raw_in(ptr, System);
    assert_eq!(2, Rc::strong_count(&five));
}
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1880)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Decrements the strong reference count on the `Rc<T>` associated with the provided pointer by one.

##### [§](#safety-5)Safety

The pointer must have been obtained through `Rc::into_raw`and must satisfy the same layout requirements specified in [`Rc::from_raw_in`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.from_raw_in "associated function std::rc::Rc::from_raw_in"). The associated `Rc` instance must be valid (i.e. the strong count must be at least 1) when invoking this method, and `ptr` must point to a block of memory allocated by `alloc`. This method can be used to release the final `Rc` and backing storage, but **should not** be called after the final `Rc` has been released.

##### [§](#examples-39)Examples

```rust
#![feature(allocator_api)]

use std::rc::Rc;
use std::alloc::System;

let five = Rc::new_in(5, System);

unsafe {
    let (ptr, _alloc) = Rc::into_raw_with_allocator(five);
    Rc::increment_strong_count_in(ptr, System);

    let five = Rc::from_raw_in(ptr, System);
    assert_eq!(2, Rc::strong_count(&five));
    Rc::decrement_strong_count_in(ptr, System);
    assert_eq!(1, Rc::strong_count(&five));
}
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1917)

Returns a mutable reference into the given `Rc`, if there are no other `Rc` or [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers to the same allocation.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") otherwise, because it is not safe to mutate a shared value.

See also [`make_mut`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.make_mut "associated function std::rc::Rc::make_mut"), which will [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") the inner value when there are other `Rc` pointers.

##### [§](#examples-40)Examples

```rust
use std::rc::Rc;

let mut x = Rc::new(3);
*Rc::get_mut(&mut x).unwrap() = 4;
assert_eq!(*x, 4);

let _y = Rc::clone(&x);
assert!(Rc::get_mut(&mut x).is_none());
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#1983)

🔬This is a nightly-only experimental API. (`get_mut_unchecked` [#63292](https://github.com/rust-lang/rust/issues/63292))

Returns a mutable reference into the given `Rc`, without any check.

See also [`get_mut`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.get_mut "associated function std::rc::Rc::get_mut"), which is safe and does appropriate checks.

##### [§](#safety-6)Safety

If any other `Rc` or [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers to the same allocation exist, then they must not be dereferenced or have active borrows for the duration of the returned borrow, and their inner type must be exactly the same as the inner type of this Rc (including lifetimes). This is trivially the case if no such pointers exist, for example immediately after `Rc::new`.

##### [§](#examples-41)Examples

```rust
#![feature(get_mut_unchecked)]

use std::rc::Rc;

let mut x = Rc::new(String::new());
unsafe {
    Rc::get_mut_unchecked(&mut x).push_str("foo")
}
assert_eq!(*x, "foo");
```

Other `Rc` pointers to the same allocation must be to the same type.

```rust
#![feature(get_mut_unchecked)]

use std::rc::Rc;

let x: Rc<str> = Rc::from("Hello, world!");
let mut y: Rc<[u8]> = x.clone().into();
unsafe {
    // this is Undefined Behavior, because x's inner type is str, not [u8]
    Rc::get_mut_unchecked(&mut y).fill(0xff); // 0xff is invalid in UTF-8
}
println!("{}", &*x); // Invalid UTF-8 in a str
```

Other `Rc` pointers to the same allocation must be to the exact same type, including lifetimes.

```rust
#![feature(get_mut_unchecked)]

use std::rc::Rc;

let x: Rc<&str> = Rc::new("Hello, world!");
{
    let s = String::from("Oh, no!");
    let mut y: Rc<&str> = x.clone();
    unsafe {
        // this is Undefined Behavior, because x's inner type
        // is &'long str, not &'short str
        *Rc::get_mut_unchecked(&mut y) = &s;
    }
}
println!("{}", &*x); // Use-after-free
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2006)

Returns `true` if the two `Rc`s point to the same allocation in a vein similar to [`ptr::eq`](https://doc.rust-lang.org/std/ptr/fn.eq.html "fn std::ptr::eq"). This function ignores the metadata of `dyn Trait` pointers.

##### [§](#examples-42)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);
let same_five = Rc::clone(&five);
let other_five = Rc::new(5);

assert!(Rc::ptr_eq(&five, &same_five));
assert!(!Rc::ptr_eq(&five, &other_five));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2012)[§](#impl-Rc%3CT,+A%3E-3)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2065)

Makes a mutable reference into the given `Rc`.

If there are other `Rc` pointers to the same allocation, then `make_mut` will [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") the inner value to a new allocation to ensure unique ownership. This is also referred to as clone-on-write.

However, if there are no other `Rc` pointers to this allocation, but some [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers, then the [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers will be disassociated and the inner value will not be cloned.

See also [`get_mut`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.get_mut "associated function std::rc::Rc::get_mut"), which will fail rather than cloning the inner value or disassociating [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers.

##### [§](#examples-43)Examples

```rust
use std::rc::Rc;

let mut data = Rc::new(5);

*Rc::make_mut(&mut data) += 1;         // Won't clone anything
let mut other_data = Rc::clone(&data); // Won't clone inner data
*Rc::make_mut(&mut data) += 1;         // Clones inner data
*Rc::make_mut(&mut data) += 1;         // Won't clone anything
*Rc::make_mut(&mut other_data) *= 2;   // Won't clone anything

// Now `data` and `other_data` point to different allocations.
assert_eq!(*data, 8);
assert_eq!(*other_data, 12);
```

[`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak") pointers will be disassociated:

```rust
use std::rc::Rc;

let mut data = Rc::new(75);
let weak = Rc::downgrade(&data);

assert!(75 == *data);
assert!(75 == *weak.upgrade().unwrap());

*Rc::make_mut(&mut data) += 1;

assert!(76 == *data);
assert!(weak.upgrade().is_none());
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2105)[§](#impl-Rc%3CT,+A%3E-4)

1.76.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2136)

If we have the only reference to `T` then unwrap it. Otherwise, clone `T` and return the clone.

Assuming `rc_t` is of type `Rc<T>`, this function is functionally equivalent to `(*rc_t).clone()`, but will avoid cloning the inner value where possible.

##### [§](#examples-44)Examples

```rust
let inner = String::from("test");
let ptr = inner.as_ptr();

let rc = Rc::new(inner);
let inner = Rc::unwrap_or_clone(rc);
// The inner value was not cloned
assert!(ptr::eq(ptr, inner.as_ptr()));

let rc = Rc::new(inner);
let rc2 = rc.clone();
let inner = Rc::unwrap_or_clone(rc);
// Because there were 2 references, we had to clone the inner value.
assert!(!ptr::eq(ptr, inner.as_ptr()));
// `rc2` is the last reference, so when we unwrap it we get back
// the original `String`.
let inner = Rc::unwrap_or_clone(rc2);
assert!(ptr::eq(ptr, inner.as_ptr()));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2141)[§](#impl-Rc%3Cdyn+Any,+A%3E)

1.29.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2162)

Attempts to downcast the `Rc<dyn Any>` to a concrete type.

##### [§](#examples-45)Examples

```rust
use std::any::Any;
use std::rc::Rc;

fn print_if_string(value: Rc<dyn Any>) {
    if let Ok(string) = value.downcast::<String>() {
        println!("String ({}): {}", string.len(), string);
    }
}

let my_string = "Hello World".to_string();
print_if_string(Rc::new(my_string));
print_if_string(Rc::new(0i8));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2201)

🔬This is a nightly-only experimental API. (`downcast_unchecked` [#90850](https://github.com/rust-lang/rust/issues/90850))

Downcasts the `Rc<dyn Any>` to a concrete type.

For a safe alternative see [`downcast`](https://doc.rust-lang.org/std/rc/struct.Rc.html#method.downcast "method std::rc::Rc::downcast").

##### [§](#examples-46)Examples

```rust
#![feature(downcast_unchecked)]

use std::any::Any;
use std::rc::Rc;

let x: Rc<dyn Any> = Rc::new(1_usize);

unsafe {
    assert_eq!(*x.downcast_unchecked::<usize>(), 1);
}
```

##### [§](#safety-7)Safety

The contained value must be of type `T`. Calling this method with the incorrect type is *undefined behavior*.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4516)[§](#impl-Allocator-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4518)[§](#method.allocate)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to allocate a block of memory. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#tymethod.allocate)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4523)[§](#method.allocate_zeroed)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Behaves like `allocate`, but also ensures that the returned memory is zero-initialized. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.allocate_zeroed)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4528)[§](#method.deallocate)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Deallocates the memory referenced by `ptr`. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#tymethod.deallocate)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4534-4539)[§](#method.grow)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to extend the memory block. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.grow)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4545-4550)[§](#method.grow_zeroed)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Behaves like `grow`, but also ensures that the new contents are set to zero before being returned. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.grow_zeroed)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#4556-4561)[§](#method.shrink)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to shrink the memory block. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.shrink)

[Source](https://doc.rust-lang.org/src/core/alloc/mod.rs.html#363-365)[§](#method.by_ref)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates a “by reference” adapter for this instance of `Allocator`. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.by_ref)

1.69.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#460-465)[§](#impl-AsFd-for-Rc%3CT%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.71.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#480-485)[§](#impl-AsHandle-for-Rc%3CT%3E)

Available on **Windows** only.

1.69.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#269-274)[§](#impl-AsRawFd-for-Rc%3CT%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3828)[§](#impl-AsRef%3CT%3E-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3829)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.71.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#262-267)[§](#impl-AsSocket-for-Rc%3CT%3E)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3821)[§](#impl-Borrow%3CT%3E-for-Rc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2479)[§](#impl-Clone-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2495)[§](#method.clone)

Makes a clone of the `Rc` pointer.

This creates another pointer to the same allocation, increasing the strong reference count.

##### [§](#examples-48)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

let _ = Rc::clone(&five);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#245-247)[§](#method.clone_from)

Performs copy-assignment from `source`. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2800)[§](#impl-Debug-for-Rc%3CT,+A%3E)

1.91.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2562-2565)[§](#impl-Default-for-Pin%3CRc%3CT%3E%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2549)[§](#impl-Default-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2554)[§](#method.default-3)

Creates an empty `[T]` inside an `Rc`.

This may or may not share an allocation with other Rcs on the same thread.

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#966)[§](#impl-Default-for-Rc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#971)[§](#method.default)

Creates an empty CStr inside an Rc

This may or may not share an allocation with other Rcs on the same thread.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2508)[§](#impl-Default-for-Rc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2520)[§](#method.default-1)

Creates a new `Rc<T>`, with the `Default` value for `T`.

##### [§](#examples-49)Examples

```rust
use std::rc::Rc;

let x: Rc<i32> = Default::default();
assert_eq!(*x, 0);
```

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2535)[§](#impl-Default-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2540)[§](#method.default-2)

Creates an empty `str` inside an `Rc`.

This may or may not share an allocation with other Rcs on the same thread.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2411)[§](#impl-Deref-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2412)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2415)[§](#method.deref)

Dereferences the value.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2793)[§](#impl-Display-for-Rc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2441)[§](#impl-Drop-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2468)[§](#method.drop)

Drops the `Rc`.

This will decrement the strong reference count. If the strong reference count reaches zero then the only other references (if any) are [`Weak`](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak"), so we `drop` the inner value.

##### [§](#examples-47)Examples

```rust
use std::rc::Rc;

struct Foo;

impl Drop for Foo {
    fn drop(&mut self) {
        println!("dropped!");
    }
}

let foo  = Rc::new(Foo);
let foo2 = Rc::clone(&foo);

drop(foo);    // Doesn't print anything
drop(foo2);   // Prints "dropped!"
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2857)[§](#impl-From%3C%26%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2869)[§](#method.from-7)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-2)Example

```rust
let original: &[i32] = &[1, 2, 3];
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#944)[§](#impl-From%3C%26CStr%3E-for-Rc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#948)[§](#method.from-3)

Converts a `&CStr` into a `Rc<CStr>`, by copying the contents into a newly allocated [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc").

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1404-1411)[§](#impl-From%3C%26OsStr%3E-for-Rc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2184-2191)[§](#impl-From%3C%26Path%3E-for-Rc%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2876)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2889)[§](#method.from-8)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-3)Example

```rust
let mut original = [1, 2, 3];
let original: &mut [i32] = &mut original;
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#955)[§](#impl-From%3C%26mut+CStr%3E-for-Rc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#959)[§](#method.from-4)

Converts a `&mut CStr` into a `Rc<CStr>`, by copying the contents into a newly allocated [`Rc`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc").

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1414-1420)[§](#impl-From%3C%26mut+OsStr%3E-for-Rc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2194-2200)[§](#impl-From%3C%26mut+Path%3E-for-Rc%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2915)[§](#impl-From%3C%26mut+str%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2928)[§](#method.from-10)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example-5)Example

```rust
let mut original = String::from("statue");
let original: &mut str = &mut original;
let shared: Rc<str> = Rc::from(original);
assert_eq!("statue", &shared[..]);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2896)[§](#impl-From%3C%26str%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2907)[§](#method.from-9)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example-4)Example

```rust
let shared: Rc<str> = Rc::from("statue");
assert_eq!("statue", &shared[..]);
```

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2836)[§](#impl-From%3C%5BT;+N%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2850)[§](#method.from-6)

Converts a [`[T; N]`](https://doc.rust-lang.org/std/primitive.array.html "primitive array") into an `Rc<[T]>`.

The conversion moves the array into a newly allocated `Rc`.

##### [§](#example-1)Example

```rust
let original: [i32; 3] = [1, 2, 3];
let shared: Rc<[i32]> = Rc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2954)[§](#impl-From%3CBox%3CT,+A%3E%3E-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2966)[§](#method.from-12)

Move a boxed object to a new, reference counted, allocation.

##### [§](#example-7)Example

```rust
let original: Box<i32> = Box::new(1);
let shared: Rc<i32> = Rc::from(original);
assert_eq!(1, *shared);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#933)[§](#impl-From%3CCString%3E-for-Rc%3CCStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3002-3005)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Rc%3CB%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3020)[§](#method.from-14)

Creates a reference-counted pointer from a clone-on-write pointer by copying its content.

##### [§](#example-9)Example

```rust
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
let shared: Rc<str> = Rc::from(cow);
assert_eq!("eggplant", &shared[..]);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1393-1401)[§](#impl-From%3COsString%3E-for-Rc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2173-2181)[§](#impl-From%3CPathBuf%3E-for-Rc%3CPath%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#624)[§](#impl-From%3CRc%3C%5Bu8%5D%3E%3E-for-Rc%3CByteStr%3E)

Available on **non-`no_rc`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#626)[§](#method.from)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#634)[§](#impl-From%3CRc%3CByteStr%3E%3E-for-Rc%3C%5Bu8%5D%3E)

Available on **non-`no_rc`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#636)[§](#method.from-1)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#326)[§](#impl-From%3CRc%3CW%3E%3E-for-LocalWaker)

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#330)[§](#method.from-16)

Use a `Wake`-able type as a `LocalWaker`.

No heap allocations or atomic operations are used for this conversion.

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#338)[§](#impl-From%3CRc%3CW%3E%3E-for-RawWaker)

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#342)[§](#method.from-17)

Use a `Wake`-able type as a `RawWaker`.

No heap allocations or atomic operations are used for this conversion.

1.62.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3029)[§](#impl-From%3CRc%3Cstr%3E%3E-for-Rc%3C%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3041)[§](#method.from-15)

Converts a reference-counted string slice into a byte slice.

##### [§](#example-10)Example

```rust
let string: Rc<str> = Rc::from("eggplant");
let bytes: Rc<[u8]> = Rc::from(string);
assert_eq!("eggplant".as_bytes(), bytes.as_ref());
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2935)[§](#impl-From%3CString%3E-for-Rc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2947)[§](#method.from-11)

Allocates a reference-counted string slice and copies `v` into it.

##### [§](#example-6)Example

```rust
let original: String = "statue".to_owned();
let shared: Rc<str> = Rc::from(original);
assert_eq!("statue", &shared[..]);
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2815)[§](#impl-From%3CT%3E-for-Rc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2829)[§](#method.from-5)

Converts a generic type `T` into an `Rc<T>`

The conversion allocates on the heap and moves `t` from the stack into it.

##### [§](#example)Example

```rust
let x = 5;
let rc = Rc::new(5);

assert_eq!(Rc::from(x), rc);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2973)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Rc%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2985)[§](#method.from-13)

Allocates a reference-counted slice and moves `v`’s items into it.

##### [§](#example-8)Example

```rust
let unique: Vec<i32> = vec![1, 2, 3];
let shared: Rc<[i32]> = Rc::from(unique);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.37.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3063)[§](#impl-FromIterator%3CT%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3102)[§](#method.from_iter)

Takes each element in the `Iterator` and collects it into an `Rc<[T]>`.

##### [§](#performance-characteristics)Performance characteristics

###### [§](#the-general-case)The general case

In the general case, collecting into `Rc<[T]>` is done by first collecting into a `Vec<T>`. That is, when writing the following:

```rust
let evens: Rc<[u8]> = (0..10).filter(|&x| x % 2 == 0).collect();
```

this behaves as if we wrote:

```rust
let evens: Rc<[u8]> = (0..10).filter(|&x| x % 2 == 0)
    .collect::<Vec<_>>() // The first set of allocations happens here.
    .into(); // A second allocation for `Rc<[T]>` happens here.
```

This will allocate as many times as needed for constructing the `Vec<T>` and then it will allocate once for turning the `Vec<T>` into the `Rc<[T]>`.

###### [§](#iterators-of-known-length)Iterators of known length

When your `Iterator` implements `TrustedLen` and is of an exact size, a single allocation will be made for the `Rc<[T]>`. For example:

```rust
let evens: Rc<[u8]> = (0..10).collect(); // Just a single allocation happens here.
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2786)[§](#impl-Hash-for-Rc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2764)[§](#impl-Ord-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2780)[§](#method.cmp)

Comparison for two `Rc`s.

The two are compared by calling `cmp()` on their inner values.

##### [§](#examples-50)Examples

```rust
use std::rc::Rc;
use std::cmp::Ordering;

let five = Rc::new(5);

assert_eq!(Ordering::Less, five.cmp(&Rc::new(6)));
```

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1033-1035)[§](#method.max)

Compares and returns the maximum of two values. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.max)

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1072-1074)[§](#method.min)

Compares and returns the minimum of two values. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.min)

1.50.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1098-1100)[§](#method.clamp)

Restrict a value to a certain interval. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.clamp)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2619)[§](#impl-PartialEq-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2639)[§](#method.eq)

Equality for two `Rc`s.

Two `Rc`s are equal if their inner values are equal, even if they are stored in different allocation.

If `T` also implements `Eq` (implying reflexivity of equality), two `Rc`s that point to the same allocation are always equal.

##### [§](#examples-51)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five == Rc::new(5));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2661)[§](#method.ne)

Inequality for two `Rc`s.

Two `Rc`s are not equal if their inner values are not equal.

If `T` also implements `Eq` (implying reflexivity of equality), two `Rc`s that point to the same allocation are always equal.

##### [§](#examples-52)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five != Rc::new(6));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2670)[§](#impl-PartialOrd-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2686)[§](#method.partial_cmp)

Partial comparison for two `Rc`s.

The two are compared by calling `partial_cmp()` on their inner values.

##### [§](#examples-53)Examples

```rust
use std::rc::Rc;
use std::cmp::Ordering;

let five = Rc::new(5);

assert_eq!(Some(Ordering::Less), five.partial_cmp(&Rc::new(6)));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2704)[§](#method.lt)

Less-than comparison for two `Rc`s.

The two are compared by calling `<` on their inner values.

##### [§](#examples-54)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five < Rc::new(6));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2722)[§](#method.le)

‘Less than or equal to’ comparison for two `Rc`s.

The two are compared by calling `<=` on their inner values.

##### [§](#examples-55)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five <= Rc::new(5));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2740)[§](#method.gt)

Greater-than comparison for two `Rc`s.

The two are compared by calling `>` on their inner values.

##### [§](#examples-56)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five > Rc::new(4));
```

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2758)[§](#method.ge)

‘Greater than or equal to’ comparison for two `Rc`s.

The two are compared by calling `>=` on their inner values.

##### [§](#examples-57)Examples

```rust
use std::rc::Rc;

let five = Rc::new(5);

assert!(five >= Rc::new(5));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2807)[§](#impl-Pointer-for-Rc%3CT,+A%3E)

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3048)[§](#impl-TryFrom%3CRc%3C%5BT%5D,+A%3E%3E-for-Rc%3C%5BT;+N%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3049)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3051)[§](#method.try_from)

Performs the conversion.

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#347)[§](#impl-CloneFromCell-for-Rc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#340)[§](#impl-CoerceUnsized%3CRc%3CU,+A%3E%3E-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2431)[§](#impl-DerefPure-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#343)[§](#impl-DispatchFromDyn%3CRc%3CU%3E%3E-for-Rc%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2667)[§](#impl-Eq-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2421)[§](#impl-PinCoerceUnsized-for-Rc%3CT,+A%3E)

1.58.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#337)[§](#impl-RefUnwindSafe-for-Rc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#324)[§](#impl-Send-for-Rc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#332)[§](#impl-Sync-for-Rc%3CT,+A%3E)

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3835)[§](#impl-Unpin-for-Rc%3CT,+A%3E)

1.9.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#335)[§](#impl-UnwindSafe-for-Rc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2504)[§](#impl-UseCloned-for-Rc%3CT,+A%3E)