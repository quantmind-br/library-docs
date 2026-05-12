---
title: Arc in std::sync - Rust
url: https://doc.rust-lang.org/std/sync/struct.Arc.html
source: crawler
fetched_at: 2026-05-06T21:23:26.356523602-03:00
rendered_js: false
word_count: 6048
summary: Arc is a thread-safe, atomically reference-counted pointer in Rust used for shared heap-allocated ownership. It facilitates safe memory management across threads and supports cycles through the use of Weak pointers.
tags:
    - rust
    - concurrency
    - memory-management
    - reference-counting
    - thread-safety
    - smart-pointers
category: reference
---

## Struct Arc

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#264-267)

```rust
pub struct Arc<T, A = Global>
where
    A: Allocator,
    T: ?Sized,{ /* private fields */ }
```

Expand description

A thread-safe reference-counting pointer. ‘Arc’ stands for ‘Atomically Reference Counted’.

The type `Arc<T>` provides shared ownership of a value of type `T`, allocated in the heap. Invoking [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") on `Arc` produces a new `Arc` instance, which points to the same allocation on the heap as the source `Arc`, while increasing a reference count. When the last `Arc` pointer to a given allocation is destroyed, the value stored in that allocation (often referred to as “inner value”) is also dropped.

Shared references in Rust disallow mutation by default, and `Arc` is no exception: you cannot generally obtain a mutable reference to something inside an `Arc`. If you do need to mutate through an `Arc`, you have several options:

1. Use interior mutability with synchronization primitives like [`Mutex`](https://doc.rust-lang.org/std/sync/struct.Mutex.html), [`RwLock`](https://doc.rust-lang.org/std/sync/struct.RwLock.html), or one of the [`Atomic`](https://doc.rust-lang.org/std/sync/atomic/index.html "mod std::sync::atomic") types.
2. Use clone-on-write semantics with [`Arc::make_mut`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.make_mut "associated function std::sync::Arc::make_mut") which provides efficient mutation without requiring interior mutability. This approach clones the data only when needed (when there are multiple references) and can be more efficient when mutations are infrequent.
3. Use [`Arc::get_mut`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.get_mut "associated function std::sync::Arc::get_mut") when you know your `Arc` is not shared (has a reference count of 1), which provides direct mutable access to the inner value without any cloning.

```rust
use std::sync::Arc;

let mut data = Arc::new(vec![1, 2, 3]);

// This will clone the vector only if there are other references to it
Arc::make_mut(&mut data).push(4);

assert_eq!(*data, vec![1, 2, 3, 4]);
```

**Note**: This type is only available on platforms that support atomic loads and stores of pointers, which includes all platforms that support the `std` crate but not all those which only support [`alloc`](https://doc.rust-lang.org/alloc/index.html "mod alloc"). This may be detected at compile time using `#[cfg(target_has_atomic = "ptr")]`.

### [§](#thread-safety)Thread Safety

Unlike [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc"), `Arc<T>` uses atomic operations for its reference counting. This means that it is thread-safe. The disadvantage is that atomic operations are more expensive than ordinary memory accesses. If you are not sharing reference-counted allocations between threads, consider using [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc") for lower overhead. [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc") is a safe default, because the compiler will catch any attempt to send an [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc") between threads. However, a library might choose `Arc<T>` in order to give library consumers more flexibility.

`Arc<T>` will implement [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") and [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") as long as the `T` implements [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") and [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync"). Why can’t you put a non-thread-safe type `T` in an `Arc<T>` to make it thread-safe? This may be a bit counter-intuitive at first: after all, isn’t the point of `Arc<T>` thread safety? The key is this: `Arc<T>` makes it thread safe to have multiple ownership of the same data, but it doesn’t add thread safety to its data. Consider `Arc<RefCell<T>>`. [`RefCell<T>`](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell") isn’t [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync"), and if `Arc<T>` was always [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send"), `Arc<RefCell<T>>` would be as well. But then we’d have a problem: [`RefCell<T>`](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell") is not thread safe; it keeps track of the borrowing count using non-atomic operations.

In the end, this means that you may need to pair `Arc<T>` with some sort of [`std::sync`](https://doc.rust-lang.org/std/sync/index.html) type, usually [`Mutex<T>`](https://doc.rust-lang.org/std/sync/struct.Mutex.html).

### [§](#breaking-cycles-with-weak)Breaking cycles with `Weak`

The [`downgrade`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.downgrade "associated function std::sync::Arc::downgrade") method can be used to create a non-owning [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointer. A [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointer can be [`upgrade`](https://doc.rust-lang.org/std/sync/struct.Weak.html#method.upgrade "method std::sync::Weak::upgrade")d to an `Arc`, but this will return [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the value stored in the allocation has already been dropped. In other words, `Weak` pointers do not keep the value inside the allocation alive; however, they *do* keep the allocation (the backing store for the value) alive.

A cycle between `Arc` pointers will never be deallocated. For this reason, [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") is used to break cycles. For example, a tree could have strong `Arc` pointers from parent nodes to children, and [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers from children back to their parents.

## [§](#cloning-references)Cloning references

Creating a new reference from an existing reference-counted pointer is done using the `Clone` trait implemented for [`Arc<T>`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc") and [`Weak<T>`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak").

```rust
use std::sync::Arc;
let foo = Arc::new(vec![1.0, 2.0, 3.0]);
// The two syntaxes below are equivalent.
let a = foo.clone();
let b = Arc::clone(&foo);
// a, b, and foo are all Arcs that point to the same memory location
```

### [§](#deref-behavior)`Deref` behavior

`Arc<T>` automatically dereferences to `T` (via the [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") trait), so you can call `T`’s methods on a value of type `Arc<T>`. To avoid name clashes with `T`’s methods, the methods of `Arc<T>` itself are associated functions, called using [fully qualified syntax](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-for-disambiguation-calling-methods-with-the-same-name):

```rust
use std::sync::Arc;

let my_arc = Arc::new(());
let my_weak = Arc::downgrade(&my_arc);
```

`Arc<T>`’s implementations of traits like `Clone` may also be called using fully qualified syntax. Some people prefer to use fully qualified syntax, while others prefer using method-call syntax.

```rust
use std::sync::Arc;

let arc = Arc::new(());
// Method-call syntax
let arc2 = arc.clone();
// Fully qualified syntax
let arc3 = Arc::clone(&arc);
```

[`Weak<T>`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") does not auto-dereference to `T`, because the inner value may have already been dropped.

## [§](#examples)Examples

Sharing some immutable data between threads:

```rust
use std::sync::Arc;
use std::thread;

let five = Arc::new(5);

for _ in 0..10 {
    let five = Arc::clone(&five);

    thread::spawn(move || {
        println!("{five:?}");
    });
}
```

Sharing a mutable [`AtomicUsize`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html "sync::atomic::AtomicUsize"):

```rust
use std::sync::Arc;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::thread;

let val = Arc::new(AtomicUsize::new(5));

for _ in 0..10 {
    let val = Arc::clone(&val);

    thread::spawn(move || {
        let v = val.fetch_add(1, Ordering::Relaxed);
        println!("{v:?}");
    });
}
```

See the [`rc` documentation](https://doc.rust-lang.org/std/rc/index.html#examples "mod std::rc") for more examples of reference counting in general.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#406)[§](#impl-Arc%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#419)

Constructs a new `Arc<T>`.

##### [§](#examples-1)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);
```

1.60.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#484-486)

Constructs a new `Arc<T>` while giving you a `Weak<T>` to the allocation, to allow you to construct a `T` which holds a weak pointer to itself.

Generally, a structure circularly referencing itself, either directly or indirectly, should not hold a strong reference to itself to prevent a memory leak. Using this function, you get access to the weak pointer during the initialization of `T`, before the `Arc<T>` is created, such that you can clone and store it inside the `T`.

`new_cyclic` first allocates the managed allocation for the `Arc<T>`, then calls your closure, giving it a `Weak<T>` to this allocation, and only afterwards completes the construction of the `Arc<T>` by placing the `T` returned from your closure into the allocation.

Since the new `Arc<T>` is not fully-constructed until `Arc<T>::new_cyclic` returns, calling [`upgrade`](https://doc.rust-lang.org/std/sync/struct.Weak.html#method.upgrade "method std::sync::Weak::upgrade") on the weak reference inside your closure will fail and result in a `None` value.

##### [§](#panics)Panics

If `data_fn` panics, the panic is propagated to the caller, and the temporary [`Weak<T>`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") is dropped normally.

##### [§](#example)Example

```rust
use std::sync::{Arc, Weak};

struct Gadget {
    me: Weak<Gadget>,
}

impl Gadget {
    /// Constructs a reference counted Gadget.
    fn new() -> Arc<Self> {
        // `me` is a `Weak<Gadget>` pointing at the new allocation of the
        // `Arc` we're constructing.
        Arc::new_cyclic(|me| {
            // Create the actual struct here.
            Gadget { me: me.clone() }
        })
    }

    /// Returns a reference counted pointer to Self.
    fn me(&self) -> Arc<Self> {
        self.me.upgrade().unwrap()
    }
}
```

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#511)

Constructs a new `Arc` with uninitialized contents.

##### [§](#examples-2)Examples

```rust
use std::sync::Arc;

let mut five = Arc::<u32>::new_uninit();

// Deferred initialization:
Arc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5)
```

1.92.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#543)

Constructs a new `Arc` with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-3)Examples

```rust
use std::sync::Arc;

let zero = Arc::<u32>::new_zeroed();
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0)
```

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#558)

Constructs a new `Pin<Arc<T>>`. If `T` does not implement `Unpin`, then `data` will be pinned in memory and unable to be moved.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#565)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Pin<Arc<T>>`, return an error if allocation fails.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#582)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc<T>`, returning an error if allocation fails.

##### [§](#examples-4)Examples

```rust
#![feature(allocator_api)]
use std::sync::Arc;

let five = Arc::try_new(5)?;
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#614)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents, returning an error if allocation fails.

##### [§](#examples-5)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;

let mut five = Arc::<u32>::try_new_uninit()?;

// Deferred initialization:
Arc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#646)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents, with the memory being filled with `0` bytes, returning an error if allocation fails.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-6)Examples

```rust
#![feature( allocator_api)]

use std::sync::Arc;

let zero = Arc::<u32>::try_new_zeroed()?;
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#678)

🔬This is a nightly-only experimental API. (`smart_pointer_try_map` [#144419](https://github.com/rust-lang/rust/issues/144419))

Maps the value in an `Arc`, reusing the allocation if possible.

`f` is called on a reference to the value in the `Arc`, and the result is returned, also in an `Arc`.

Note: this is an associated function, which means that you have to call it as `Arc::map(a, f)` instead of `r.map(a)`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-7)Examples

```rust
#![feature(smart_pointer_try_map)]

use std::sync::Arc;

let r = Arc::new(7);
let new = Arc::map(r, |i| i + 7);
assert_eq!(*new, 14);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#718-724)

🔬This is a nightly-only experimental API. (`smart_pointer_try_map` [#144419](https://github.com/rust-lang/rust/issues/144419))

Attempts to map the value in an `Arc`, reusing the allocation if possible.

`f` is called on a reference to the value in the `Arc`, and if the operation succeeds, the result is returned, also in an `Arc`.

Note: this is an associated function, which means that you have to call it as `Arc::try_map(a, f)` instead of `a.try_map(f)`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-8)Examples

```rust
#![feature(smart_pointer_try_map)]

use std::sync::Arc;

let b = Arc::new(7);
let new = Arc::try_map(b, |&i| u32::try_from(i)).unwrap();
assert_eq!(*new, 7);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#744)[§](#impl-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#760)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc<T>` in the provided allocator.

##### [§](#examples-9)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let five = Arc::new_in(5, System);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#800)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents in the provided allocator.

##### [§](#examples-10)Examples

```rust
#![feature(get_mut_unchecked)]
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let mut five = Arc::<u32, _>::new_uninit_in(System);

let five = unsafe {
    // Deferred initialization:
    Arc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);

    five.assume_init()
};

assert_eq!(*five, 5)
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#837)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents, with the memory being filled with `0` bytes, in the provided allocator.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-11)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let zero = Arc::<u32, _>::new_zeroed_in(System);
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0)
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#882-884)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc<T, A>` in the given allocator while giving you a `Weak<T, A>` to the allocation, to allow you to construct a `T` which holds a weak pointer to itself.

Generally, a structure circularly referencing itself, either directly or indirectly, should not hold a strong reference to itself to prevent a memory leak. Using this function, you get access to the weak pointer during the initialization of `T`, before the `Arc<T, A>` is created, such that you can clone and store it inside the `T`.

`new_cyclic_in` first allocates the managed allocation for the `Arc<T, A>`, then calls your closure, giving it a `Weak<T, A>` to this allocation, and only afterwards completes the construction of the `Arc<T, A>` by placing the `T` returned from your closure into the allocation.

Since the new `Arc<T, A>` is not fully-constructed until `Arc<T, A>::new_cyclic_in` returns, calling [`upgrade`](https://doc.rust-lang.org/std/sync/struct.Weak.html#method.upgrade "method std::sync::Weak::upgrade") on the weak reference inside your closure will fail and result in a `None` value.

##### [§](#panics-1)Panics

If `data_fn` panics, the panic is propagated to the caller, and the temporary [`Weak<T>`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") is dropped normally.

##### [§](#example-1)Example

See [`new_cyclic`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.new_cyclic "associated function std::sync::Arc::new_cyclic")

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#947-949)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Pin<Arc<T, A>>` in the provided allocator. If `T` does not implement `Unpin`, then `data` will be pinned in memory and unable to be moved.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#958-960)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Pin<Arc<T, A>>` in the provided allocator, return an error if allocation fails.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#980)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc<T, A>` in the provided allocator, returning an error if allocation fails.

##### [§](#examples-12)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let five = Arc::try_new_in(5, System)?;
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1021)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents, in the provided allocator, returning an error if allocation fails.

##### [§](#examples-13)Examples

```rust
#![feature(allocator_api)]
#![feature(get_mut_unchecked)]

use std::sync::Arc;
use std::alloc::System;

let mut five = Arc::<u32, _>::try_new_uninit_in(System)?;

let five = unsafe {
    // Deferred initialization:
    Arc::get_mut_unchecked(&mut five).as_mut_ptr().write(5);

    five.assume_init()
};

assert_eq!(*five, 5);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1059)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new `Arc` with uninitialized contents, with the memory being filled with `0` bytes, in the provided allocator, returning an error if allocation fails.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-14)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let zero = Arc::<u32, _>::try_new_zeroed_in(System)?;
let zero = unsafe { zero.assume_init() };

assert_eq!(*zero, 0);
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1106)

Returns the inner value, if the `Arc` has exactly one strong reference.

Otherwise, an [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned with the same `Arc` that was passed in.

This will succeed even if there are outstanding weak references.

It is strongly recommended to use [`Arc::into_inner`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.into_inner "associated function std::sync::Arc::into_inner") instead if you don’t keep the `Arc` in the [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") case. Immediately dropping the [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err")-value, as the expression `Arc::try_unwrap(this).ok()` does, can cause the strong count to drop to zero and the inner value of the `Arc` to be dropped. For instance, if two threads execute such an expression in parallel, there is a race condition without the possibility of unsafety: The threads could first both check whether they own the last instance in `Arc::try_unwrap`, determine that they both do not, and then both discard and drop their instance in the call to [`ok`](https://doc.rust-lang.org/std/result/enum.Result.html#method.ok "method std::result::Result::ok"). In this scenario, the value inside the `Arc` is safely destroyed by exactly one of the threads, but neither thread will ever be able to use the value.

##### [§](#examples-15)Examples

```rust
use std::sync::Arc;

let x = Arc::new(3);
assert_eq!(Arc::try_unwrap(x), Ok(3));

let x = Arc::new(4);
let _y = Arc::clone(&x);
assert_eq!(*Arc::try_unwrap(x).unwrap_err(), 4);
```

1.70.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1221)

Returns the inner value, if the `Arc` has exactly one strong reference.

Otherwise, [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is returned and the `Arc` is dropped.

This will succeed even if there are outstanding weak references.

If `Arc::into_inner` is called on every clone of this `Arc`, it is guaranteed that exactly one of the calls returns the inner value. This means in particular that the inner value is not dropped.

[`Arc::try_unwrap`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.try_unwrap "associated function std::sync::Arc::try_unwrap") is conceptually similar to `Arc::into_inner`, but it is meant for different use-cases. If used as a direct replacement for `Arc::into_inner` anyway, such as with the expression `Arc::try_unwrap(this).ok()`, then it does **not** give the same guarantee as described in the previous paragraph. For more information, see the examples below and read the documentation of [`Arc::try_unwrap`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.try_unwrap "associated function std::sync::Arc::try_unwrap").

##### [§](#examples-16)Examples

Minimal example demonstrating the guarantee that `Arc::into_inner` gives.

```rust
use std::sync::Arc;

let x = Arc::new(3);
let y = Arc::clone(&x);

// Two threads calling `Arc::into_inner` on both clones of an `Arc`:
let x_thread = std::thread::spawn(|| Arc::into_inner(x));
let y_thread = std::thread::spawn(|| Arc::into_inner(y));

let x_inner_value = x_thread.join().unwrap();
let y_inner_value = y_thread.join().unwrap();

// One of the threads is guaranteed to receive the inner value:
assert!(matches!(
    (x_inner_value, y_inner_value),
    (None, Some(3)) | (Some(3), None)
));
// The result could also be `(None, None)` if the threads called
// `Arc::try_unwrap(x).ok()` and `Arc::try_unwrap(y).ok()` instead.
```

A more practical example demonstrating the need for `Arc::into_inner`:

```rust
use std::sync::Arc;

// Definition of a simple singly linked list using `Arc`:
#[derive(Clone)]
struct LinkedList<T>(Option<Arc<Node<T>>>);
struct Node<T>(T, Option<Arc<Node<T>>>);

// Dropping a long `LinkedList<T>` relying on the destructor of `Arc`
// can cause a stack overflow. To prevent this, we can provide a
// manual `Drop` implementation that does the destruction in a loop:
impl<T> Drop for LinkedList<T> {
    fn drop(&mut self) {
        let mut link = self.0.take();
        while let Some(arc_node) = link.take() {
            if let Some(Node(_value, next)) = Arc::into_inner(arc_node) {
                link = next;
            }
        }
    }
}

// Implementation of `new` and `push` omitted
impl<T> LinkedList<T> {
    /* ... */
}

// The following code could have still caused a stack overflow
// despite the manual `Drop` impl if that `Drop` impl had used
// `Arc::try_unwrap(arc).ok()` instead of `Arc::into_inner(arc)`.

// Create a long list and clone it
let mut x = LinkedList::new();
let size = 100000;
for i in 0..size {
    x.push(i); // Adds i to the front of x
}
let y = x.clone();

// Drop the clones in parallel
let x_thread = std::thread::spawn(|| drop(x));
let y_thread = std::thread::spawn(|| drop(y));
x_thread.join().unwrap();
y_thread.join().unwrap();
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1249)[§](#impl-Arc%3C%5BT%5D%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1273)

Constructs a new atomically reference-counted slice with uninitialized contents.

##### [§](#examples-17)Examples

```rust
use std::sync::Arc;

let mut values = Arc::<[u32]>::new_uninit_slice(3);

// Deferred initialization:
let data = Arc::get_mut(&mut values).unwrap();
data[0].write(1);
data[1].write(2);
data[2].write(3);

let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

1.92.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1299)

Constructs a new atomically reference-counted slice with uninitialized contents, with the memory being filled with `0` bytes.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-18)Examples

```rust
use std::sync::Arc;

let values = Arc::<[u32]>::new_zeroed_slice(3);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1320)

🔬This is a nightly-only experimental API. (`alloc_slice_into_array` [#148082](https://github.com/rust-lang/rust/issues/148082))

Converts the reference-counted slice into a reference-counted array.

This operation does not reallocate; the underlying array of the slice is simply reinterpreted as an array type.

If `N` is not exactly equal to the length of `self`, then this method returns `None`.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1333)[§](#impl-Arc%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1362)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new atomically reference-counted slice with uninitialized contents in the provided allocator.

##### [§](#examples-19)Examples

```rust
#![feature(get_mut_unchecked)]
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let mut values = Arc::<[u32], _>::new_uninit_slice_in(3, System);

let values = unsafe {
    // Deferred initialization:
    Arc::get_mut_unchecked(&mut values)[0].as_mut_ptr().write(1);
    Arc::get_mut_unchecked(&mut values)[1].as_mut_ptr().write(2);
    Arc::get_mut_unchecked(&mut values)[2].as_mut_ptr().write(3);

    values.assume_init()
};

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1390)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs a new atomically reference-counted slice with uninitialized contents, with the memory being filled with `0` bytes, in the provided allocator.

See [`MaybeUninit::zeroed`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.zeroed "associated function std::mem::MaybeUninit::zeroed") for examples of correct and incorrect usage of this method.

##### [§](#examples-20)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let values = Arc::<[u32], _>::new_zeroed_slice_in(3, System);
let values = unsafe { values.assume_init() };

assert_eq!(*values, [0, 0, 0])
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1407)[§](#impl-Arc%3CMaybeUninit%3CT%3E,+A%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1437)

Converts to `Arc<T>`.

##### [§](#safety)Safety

As with [`MaybeUninit::assume_init`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.assume_init "method std::mem::MaybeUninit::assume_init"), it is up to the caller to guarantee that the inner value really is in an initialized state. Calling this when the content is not yet fully initialized causes immediate undefined behavior.

##### [§](#examples-21)Examples

```rust
use std::sync::Arc;

let mut five = Arc::<u32>::new_uninit();

// Deferred initialization:
Arc::get_mut(&mut five).unwrap().write(5);

let five = unsafe { five.assume_init() };

assert_eq!(*five, 5)
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1443)[§](#impl-Arc%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1456)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Arc<T>` with a clone of `value`.

##### [§](#examples-22)Examples

```rust
#![feature(clone_from_ref)]
use std::sync::Arc;

let hello: Arc<str> = Arc::clone_from_ref("hello");
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1474)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Arc<T>` with a clone of `value`, returning an error if allocation fails

##### [§](#examples-23)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::sync::Arc;

let hello: Arc<str> = Arc::try_clone_from_ref("hello")?;
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1479)[§](#impl-Arc%3CT,+A%3E-1)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1495)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Arc<T>` with a clone of `value` in the provided allocator.

##### [§](#examples-24)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::sync::Arc;
use std::alloc::System;

let hello: Arc<str, System> = Arc::clone_from_ref_in("hello", System);
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1525)

🔬This is a nightly-only experimental API. (`clone_from_ref` [#149075](https://github.com/rust-lang/rust/issues/149075))

Constructs a new `Arc<T>` with a clone of `value` in the provided allocator, returning an error if allocation fails

##### [§](#examples-25)Examples

```rust
#![feature(clone_from_ref)]
#![feature(allocator_api)]
use std::sync::Arc;
use std::alloc::System;

let hello: Arc<str, System> = Arc::try_clone_from_ref_in("hello", System)?;
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1541)[§](#impl-Arc%3C%5BMaybeUninit%3CT%3E%5D,+A%3E)

1.82.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1574)

Converts to `Arc<[T]>`.

##### [§](#safety-1)Safety

As with [`MaybeUninit::assume_init`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html#method.assume_init "method std::mem::MaybeUninit::assume_init"), it is up to the caller to guarantee that the inner value really is in an initialized state. Calling this when the content is not yet fully initialized causes immediate undefined behavior.

##### [§](#examples-26)Examples

```rust
use std::sync::Arc;

let mut values = Arc::<[u32]>::new_uninit_slice(3);

// Deferred initialization:
let data = Arc::get_mut(&mut values).unwrap();
data[0].write(1);
data[1].write(2);
data[2].write(3);

let values = unsafe { values.assume_init() };

assert_eq!(*values, [1, 2, 3])
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1580)[§](#impl-Arc%3CT%3E-2)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1644)

Constructs an `Arc<T>` from a raw pointer.

The raw pointer must have been previously returned by a call to [`Arc<U>::into_raw`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.into_raw "associated function std::sync::Arc::into_raw") with the following requirements:

- If `U` is sized, it must have the same size and alignment as `T`. This is trivially true if `U` is `T`.
- If `U` is unsized, its data pointer must have the same size and alignment as `T`. This is trivially true if `Arc<U>` was constructed through `Arc<T>` and then converted to `Arc<U>` through an [unsized coercion](https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions).

Note that if `U` or `U`’s data pointer is not `T` but has the same size and alignment, this is basically like transmuting references of different types. See [`mem::transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html "fn std::mem::transmute") for more information on what restrictions apply in this case.

The raw pointer must point to a block of memory allocated by the global allocator.

The user of `from_raw` has to make sure a specific value of `T` is only dropped once.

This function is unsafe because improper use may lead to memory unsafety, even if the returned `Arc<T>` is never accessed.

##### [§](#examples-27)Examples

```rust
use std::sync::Arc;

let x = Arc::new("hello".to_owned());
let x_ptr = Arc::into_raw(x);

unsafe {
    // Convert back to an `Arc` to prevent leak.
    let x = Arc::from_raw(x_ptr);
    assert_eq!(&*x, "hello");

    // Further calls to `Arc::from_raw(x_ptr)` would be memory-unsafe.
}

// The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
```

Convert a slice back into its original array:

```rust
use std::sync::Arc;

let x: Arc<[u32]> = Arc::new([1, 2, 3]);
let x_ptr: *const [u32] = Arc::into_raw(x);

unsafe {
    let x: Arc<[u32; 3]> = Arc::from_raw(x_ptr.cast::<[u32; 3]>());
    assert_eq!(&*x, &[1, 2, 3]);
}
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1667)

Consumes the `Arc`, returning the wrapped pointer.

To avoid a memory leak the pointer must be converted back to an `Arc` using [`Arc::from_raw`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw "associated function std::sync::Arc::from_raw").

##### [§](#examples-28)Examples

```rust
use std::sync::Arc;

let x = Arc::new("hello".to_owned());
let x_ptr = Arc::into_raw(x);
assert_eq!(unsafe { &*x_ptr }, "hello");
```

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1706)

Increments the strong reference count on the `Arc<T>` associated with the provided pointer by one.

##### [§](#safety-2)Safety

The pointer must have been obtained through `Arc::into_raw` and must satisfy the same layout requirements specified in [`Arc::from_raw_in`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw_in "associated function std::sync::Arc::from_raw_in"). The associated `Arc` instance must be valid (i.e. the strong count must be at least 1) for the duration of this method, and `ptr` must point to a block of memory allocated by the global allocator.

##### [§](#examples-29)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

unsafe {
    let ptr = Arc::into_raw(five);
    Arc::increment_strong_count(ptr);

    // This assertion is deterministic because we haven't shared
    // the `Arc` between threads.
    let five = Arc::from_raw(ptr);
    assert_eq!(2, Arc::strong_count(&five));
}
```

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1746)

Decrements the strong reference count on the `Arc<T>` associated with the provided pointer by one.

##### [§](#safety-3)Safety

The pointer must have been obtained through `Arc::into_raw` and must satisfy the same layout requirements specified in [`Arc::from_raw_in`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw_in "associated function std::sync::Arc::from_raw_in"). The associated `Arc` instance must be valid (i.e. the strong count must be at least 1) when invoking this method, and `ptr` must point to a block of memory allocated by the global allocator. This method can be used to release the final `Arc` and backing storage, but **should not** be called after the final `Arc` has been released.

##### [§](#examples-30)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

unsafe {
    let ptr = Arc::into_raw(five);
    Arc::increment_strong_count(ptr);

    // Those assertions are deterministic because we haven't shared
    // the `Arc` between threads.
    let five = Arc::from_raw(ptr);
    assert_eq!(2, Arc::strong_count(&five));
    Arc::decrement_strong_count(ptr);
    assert_eq!(1, Arc::strong_count(&five));
}
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1751)[§](#impl-Arc%3CT,+A%3E-2)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1759)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Returns a reference to the underlying allocator.

Note: this is an associated function, which means that you have to call it as `Arc::allocator(&a)` instead of `a.allocator()`. This is so that there is no conflict with a method on the inner type.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1783)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Consumes the `Arc`, returning the wrapped pointer and allocator.

To avoid a memory leak the pointer must be converted back to an `Arc` using [`Arc::from_raw_in`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw_in "associated function std::sync::Arc::from_raw_in").

##### [§](#examples-31)Examples

```rust
#![feature(allocator_api)]
use std::sync::Arc;
use std::alloc::System;

let x = Arc::new_in("hello".to_owned(), System);
let (ptr, alloc) = Arc::into_raw_with_allocator(x);
assert_eq!(unsafe { &*ptr }, "hello");
let x = unsafe { Arc::from_raw_in(ptr, alloc) };
assert_eq!(&*x, "hello");
```

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1810)

Provides a raw pointer to the data.

The counts are not affected in any way and the `Arc` is not consumed. The pointer is valid for as long as there are strong counts in the `Arc`.

##### [§](#examples-32)Examples

```rust
use std::sync::Arc;

let x = Arc::new("hello".to_owned());
let y = Arc::clone(&x);
let x_ptr = Arc::as_ptr(&x);
assert_eq!(x_ptr, Arc::as_ptr(&y));
assert_eq!(unsafe { &*x_ptr }, "hello");
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1888)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Constructs an `Arc<T, A>` from a raw pointer.

The raw pointer must have been previously returned by a call to [`Arc<U, A>::into_raw`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.into_raw "associated function std::sync::Arc::into_raw") with the following requirements:

- If `U` is sized, it must have the same size and alignment as `T`. This is trivially true if `U` is `T`.
- If `U` is unsized, its data pointer must have the same size and alignment as `T`. This is trivially true if `Arc<U>` was constructed through `Arc<T>` and then converted to `Arc<U>` through an [unsized coercion](https://doc.rust-lang.org/reference/type-coercions.html#unsized-coercions).

Note that if `U` or `U`’s data pointer is not `T` but has the same size and alignment, this is basically like transmuting references of different types. See [`mem::transmute`](https://doc.rust-lang.org/std/mem/fn.transmute.html "fn std::mem::transmute") for more information on what restrictions apply in this case.

The raw pointer must point to a block of memory allocated by `alloc`

The user of `from_raw` has to make sure a specific value of `T` is only dropped once.

This function is unsafe because improper use may lead to memory unsafety, even if the returned `Arc<T>` is never accessed.

##### [§](#examples-33)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let x = Arc::new_in("hello".to_owned(), System);
let (x_ptr, alloc) = Arc::into_raw_with_allocator(x);

unsafe {
    // Convert back to an `Arc` to prevent leak.
    let x = Arc::from_raw_in(x_ptr, System);
    assert_eq!(&*x, "hello");

    // Further calls to `Arc::from_raw(x_ptr)` would be memory-unsafe.
}

// The memory was freed when `x` went out of scope above, so `x_ptr` is now dangling!
```

Convert a slice back into its original array:

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let x: Arc<[u32], _> = Arc::new_in([1, 2, 3], System);
let x_ptr: *const [u32] = Arc::into_raw_with_allocator(x).0;

unsafe {
    let x: Arc<[u32; 3], _> = Arc::from_raw_in(x_ptr.cast::<[u32; 3]>(), System);
    assert_eq!(&*x, &[1, 2, 3]);
}
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1913-1915)

Creates a new [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointer to this allocation.

##### [§](#examples-34)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

let weak_five = Arc::downgrade(&five);
```

1.15.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#1973)

Gets the number of [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers to this allocation.

##### [§](#safety-4)Safety

This method by itself is safe, but using it correctly requires extra care. Another thread can change the weak count at any time, including potentially between calling this method and acting on the result.

##### [§](#examples-35)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);
let _weak_five = Arc::downgrade(&five);

// This assertion is deterministic because we haven't shared
// the `Arc` or `Weak` between threads.
assert_eq!(1, Arc::weak_count(&five));
```

1.15.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2003)

Gets the number of strong (`Arc`) pointers to this allocation.

##### [§](#safety-5)Safety

This method by itself is safe, but using it correctly requires extra care. Another thread can change the strong count at any time, including potentially between calling this method and acting on the result.

##### [§](#examples-36)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);
let _also_five = Arc::clone(&five);

// This assertion is deterministic because we haven't shared
// the `Arc` between threads.
assert_eq!(2, Arc::strong_count(&five));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2044-2046)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Increments the strong reference count on the `Arc<T>` associated with the provided pointer by one.

##### [§](#safety-6)Safety

The pointer must have been obtained through `Arc::into_raw` and must satisfy the same layout requirements specified in [`Arc::from_raw_in`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw_in "associated function std::sync::Arc::from_raw_in"). The associated `Arc` instance must be valid (i.e. the strong count must be at least 1) for the duration of this method, and `ptr` must point to a block of memory allocated by `alloc`.

##### [§](#examples-37)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let five = Arc::new_in(5, System);

unsafe {
    let (ptr, _alloc) = Arc::into_raw_with_allocator(five);
    Arc::increment_strong_count_in(ptr, System);

    // This assertion is deterministic because we haven't shared
    // the `Arc` between threads.
    let five = Arc::from_raw_in(ptr, System);
    assert_eq!(2, Arc::strong_count(&five));
}
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2093)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Decrements the strong reference count on the `Arc<T>` associated with the provided pointer by one.

##### [§](#safety-7)Safety

The pointer must have been obtained through `Arc::into_raw` and must satisfy the same layout requirements specified in [`Arc::from_raw_in`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.from_raw_in "associated function std::sync::Arc::from_raw_in"). The associated `Arc` instance must be valid (i.e. the strong count must be at least 1) when invoking this method, and `ptr` must point to a block of memory allocated by `alloc`. This method can be used to release the final `Arc` and backing storage, but **should not** be called after the final `Arc` has been released.

##### [§](#examples-38)Examples

```rust
#![feature(allocator_api)]

use std::sync::Arc;
use std::alloc::System;

let five = Arc::new_in(5, System);

unsafe {
    let (ptr, _alloc) = Arc::into_raw_with_allocator(five);
    Arc::increment_strong_count_in(ptr, System);

    // Those assertions are deterministic because we haven't shared
    // the `Arc` between threads.
    let five = Arc::from_raw_in(ptr, System);
    assert_eq!(2, Arc::strong_count(&five));
    Arc::decrement_strong_count_in(ptr, System);
    assert_eq!(1, Arc::strong_count(&five));
}
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2143)

Returns `true` if the two `Arc`s point to the same allocation in a vein similar to [`ptr::eq`](https://doc.rust-lang.org/std/ptr/fn.eq.html "ptr::eq"). This function ignores the metadata of `dyn Trait` pointers.

##### [§](#examples-39)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);
let same_five = Arc::clone(&five);
let other_five = Arc::new(5);

assert!(Arc::ptr_eq(&five, &same_five));
assert!(!Arc::ptr_eq(&five, &other_five));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2439)[§](#impl-Arc%3CT,+A%3E-3)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2492)

Makes a mutable reference into the given `Arc`.

If there are other `Arc` pointers to the same allocation, then `make_mut` will [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") the inner value to a new allocation to ensure unique ownership. This is also referred to as clone-on-write.

However, if there are no other `Arc` pointers to this allocation, but some [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers, then the [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers will be dissociated and the inner value will not be cloned.

See also [`get_mut`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.get_mut "associated function std::sync::Arc::get_mut"), which will fail rather than cloning the inner value or dissociating [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers.

##### [§](#examples-40)Examples

```rust
use std::sync::Arc;

let mut data = Arc::new(5);

*Arc::make_mut(&mut data) += 1;         // Won't clone anything
let mut other_data = Arc::clone(&data); // Won't clone inner data
*Arc::make_mut(&mut data) += 1;         // Clones inner data
*Arc::make_mut(&mut data) += 1;         // Won't clone anything
*Arc::make_mut(&mut other_data) *= 2;   // Won't clone anything

// Now `data` and `other_data` point to different allocations.
assert_eq!(*data, 8);
assert_eq!(*other_data, 12);
```

[`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers will be dissociated:

```rust
use std::sync::Arc;

let mut data = Arc::new(75);
let weak = Arc::downgrade(&data);

assert!(75 == *data);
assert!(75 == *weak.upgrade().unwrap());

*Arc::make_mut(&mut data) += 1;

assert!(76 == *data);
assert!(weak.upgrade().is_none());
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2553)[§](#impl-Arc%3CT,+A%3E-4)

1.76.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2584)

If we have the only reference to `T` then unwrap it. Otherwise, clone `T` and return the clone.

Assuming `arc_t` is of type `Arc<T>`, this function is functionally equivalent to `(*arc_t).clone()`, but will avoid cloning the inner value where possible.

##### [§](#examples-41)Examples

```rust
let inner = String::from("test");
let ptr = inner.as_ptr();

let arc = Arc::new(inner);
let inner = Arc::unwrap_or_clone(arc);
// The inner value was not cloned
assert!(ptr::eq(ptr, inner.as_ptr()));

let arc = Arc::new(inner);
let arc2 = arc.clone();
let inner = Arc::unwrap_or_clone(arc);
// Because there were 2 references, we had to clone the inner value.
assert!(!ptr::eq(ptr, inner.as_ptr()));
// `arc2` is the last reference, so when we unwrap it we get back
// the original `String`.
let inner = Arc::unwrap_or_clone(arc2);
assert!(ptr::eq(ptr, inner.as_ptr()));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2589)[§](#impl-Arc%3CT,+A%3E-5)

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2616)

Returns a mutable reference into the given `Arc`, if there are no other `Arc` or [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers to the same allocation.

Returns [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") otherwise, because it is not safe to mutate a shared value.

See also [`make_mut`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.make_mut "associated function std::sync::Arc::make_mut"), which will [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") the inner value when there are other `Arc` pointers.

##### [§](#examples-42)Examples

```rust
use std::sync::Arc;

let mut x = Arc::new(3);
*Arc::get_mut(&mut x).unwrap() = 4;
assert_eq!(*x, 4);

let _y = Arc::clone(&x);
assert!(Arc::get_mut(&mut x).is_none());
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2691)

🔬This is a nightly-only experimental API. (`get_mut_unchecked` [#63292](https://github.com/rust-lang/rust/issues/63292))

Returns a mutable reference into the given `Arc`, without any check.

See also [`get_mut`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.get_mut "associated function std::sync::Arc::get_mut"), which is safe and does appropriate checks.

##### [§](#safety-8)Safety

If any other `Arc` or [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers to the same allocation exist, then they must not be dereferenced or have active borrows for the duration of the returned borrow, and their inner type must be exactly the same as the inner type of this Arc (including lifetimes). This is trivially the case if no such pointers exist, for example immediately after `Arc::new`.

##### [§](#examples-43)Examples

```rust
#![feature(get_mut_unchecked)]

use std::sync::Arc;

let mut x = Arc::new(String::new());
unsafe {
    Arc::get_mut_unchecked(&mut x).push_str("foo")
}
assert_eq!(*x, "foo");
```

Other `Arc` pointers to the same allocation must be to the same type.

```rust
#![feature(get_mut_unchecked)]

use std::sync::Arc;

let x: Arc<str> = Arc::from("Hello, world!");
let mut y: Arc<[u8]> = x.clone().into();
unsafe {
    // this is Undefined Behavior, because x's inner type is str, not [u8]
    Arc::get_mut_unchecked(&mut y).fill(0xff); // 0xff is invalid in UTF-8
}
println!("{}", &*x); // Invalid UTF-8 in a str
```

Other `Arc` pointers to the same allocation must be to the exact same type, including lifetimes.

```rust
#![feature(get_mut_unchecked)]

use std::sync::Arc;

let x: Arc<&str> = Arc::new("Hello, world!");
{
    let s = String::from("Oh, no!");
    let mut y: Arc<&str> = x.clone();
    unsafe {
        // this is Undefined Behavior, because x's inner type
        // is &'long str, not &'short str
        *Arc::get_mut_unchecked(&mut y) = &s;
    }
}
println!("{}", &*x); // Use-after-free
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2754)

🔬This is a nightly-only experimental API. (`arc_is_unique` [#138938](https://github.com/rust-lang/rust/issues/138938))

Determine whether this is the unique reference to the underlying data.

Returns `true` if there are no other `Arc` or [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak") pointers to the same allocation; returns `false` otherwise.

If this function returns `true`, then is guaranteed to be safe to call [`get_mut_unchecked`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.get_mut_unchecked "associated function std::sync::Arc::get_mut_unchecked") on this `Arc`, so long as no clones occur in between.

##### [§](#examples-44)Examples

```rust
#![feature(arc_is_unique)]

use std::sync::Arc;

let x = Arc::new(3);
assert!(Arc::is_unique(&x));

let y = Arc::clone(&x);
assert!(!Arc::is_unique(&x));
drop(y);

// Weak references also count, because they could be upgraded at any time.
let z = Arc::downgrade(&x);
assert!(!Arc::is_unique(&x));
```

##### [§](#pointer-invalidation)Pointer invalidation

This function will always return the same value as `Arc::get_mut(arc).is_some()`. However, unlike that operation it does not produce any mutable references to the underlying data, meaning no pointers to the data inside the `Arc` are invalidated by the call. Thus, the following code is valid, even though it would be UB if it used `Arc::get_mut`:

```rust
#![feature(arc_is_unique)]

use std::sync::Arc;

let arc = Arc::new(5);
let pointer: *const i32 = &*arc;
assert!(Arc::is_unique(&arc));
assert_eq!(unsafe { *pointer }, 5);
```

##### [§](#atomic-orderings)Atomic orderings

Concurrent drops to other `Arc` pointers to the same allocation will synchronize with this call - that is, this call performs an `Acquire` operation on the underlying strong and weak ref counts. This ensures that calling `get_mut_unchecked` is safe.

Note that this operation requires locking the weak ref count, so concurrent calls to `downgrade` may spin-loop for a short period of time.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2859)[§](#impl-Arc%3Cdyn+Any+%2B+Send+%2B+Sync,+A%3E)

1.29.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2880-2882)

Attempts to downcast the `Arc<dyn Any + Send + Sync>` to a concrete type.

##### [§](#examples-45)Examples

```rust
use std::any::Any;
use std::sync::Arc;

fn print_if_string(value: Arc<dyn Any + Send + Sync>) {
    if let Ok(string) = value.downcast::<String>() {
        println!("String ({}): {}", string.len(), string);
    }
}

let my_string = "Hello World".to_string();
print_if_string(Arc::new(my_string));
print_if_string(Arc::new(0i8));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2922-2924)

🔬This is a nightly-only experimental API. (`downcast_unchecked` [#90850](https://github.com/rust-lang/rust/issues/90850))

Downcasts the `Arc<dyn Any + Send + Sync>` to a concrete type.

For a safe alternative see [`downcast`](https://doc.rust-lang.org/std/sync/struct.Arc.html#method.downcast "method std::sync::Arc::downcast").

##### [§](#examples-46)Examples

```rust
#![feature(downcast_unchecked)]

use std::any::Any;
use std::sync::Arc;

let x: Arc<dyn Any + Send + Sync> = Arc::new(1_usize);

unsafe {
    assert_eq!(*x.downcast_unchecked::<usize>(), 1);
}
```

##### [§](#safety-9)Safety

The contained value must be of type `T`. Calling this method with the incorrect type is *undefined behavior*.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4887)[§](#impl-Allocator-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4889)[§](#method.allocate)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to allocate a block of memory. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#tymethod.allocate)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4894)[§](#method.allocate_zeroed)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Behaves like `allocate`, but also ensures that the returned memory is zero-initialized. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.allocate_zeroed)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4899)[§](#method.deallocate)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Deallocates the memory referenced by `ptr`. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#tymethod.deallocate)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4905-4910)[§](#method.grow)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to extend the memory block. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.grow)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4916-4921)[§](#method.grow_zeroed)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Behaves like `grow`, but also ensures that the new contents are set to zero before being returned. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.grow_zeroed)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4927-4932)[§](#method.shrink)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Attempts to shrink the memory block. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.shrink)

[Source](https://doc.rust-lang.org/src/core/alloc/mod.rs.html#363-365)[§](#method.by_ref)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates a “by reference” adapter for this instance of `Allocator`. [Read more](https://doc.rust-lang.org/std/alloc/trait.Allocator.html#method.by_ref)

1.64.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#452-457)[§](#impl-AsFd-for-Arc%3CT%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

This impl allows implementing traits that require `AsFd` on Arc.

```rust
use std::net::UdpSocket;
use std::sync::Arc;

trait MyTrait: AsFd {}
impl MyTrait for Arc<UdpSocket> {}
impl MyTrait for Box<UdpSocket> {}
```

1.71.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#472-477)[§](#impl-AsHandle-for-Arc%3CT%3E)

Available on **Windows** only.

This impl allows implementing traits that require `AsHandle` on Arc.

```rust
use std::fs::File;
use std::sync::Arc;

trait MyTrait: AsHandle {}
impl MyTrait for Arc<File> {}
impl MyTrait for Box<File> {}
```

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#261-266)[§](#impl-AsRawFd-for-Arc%3CT%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

This impl allows implementing traits that require `AsRawFd` on Arc.

```rust
use std::net::UdpSocket;
use std::sync::Arc;
trait MyTrait: AsRawFd {
}
impl MyTrait for Arc<UdpSocket> {}
impl MyTrait for Box<UdpSocket> {}
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4189)[§](#impl-AsRef%3CT%3E-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4190)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.71.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#254-259)[§](#impl-AsSocket-for-Arc%3CT%3E)

Available on **Windows** only.

This impl allows implementing traits that require `AsSocket` on Arc.

```rust
use std::net::UdpSocket;
use std::sync::Arc;

trait MyTrait: AsSocket {}
impl MyTrait for Arc<UdpSocket> {}
impl MyTrait for Box<UdpSocket> {}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4182)[§](#impl-Borrow%3CT%3E-for-Arc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2360)[§](#impl-Clone-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2376)[§](#method.clone)

Makes a clone of the `Arc` pointer.

This creates another pointer to the same allocation, increasing the strong reference count.

##### [§](#examples-48)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

let _ = Arc::clone(&five);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#245-247)[§](#method.clone_from)

Performs copy-assignment from `source`. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3700)[§](#impl-Debug-for-Arc%3CT,+A%3E)

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3801)[§](#impl-Default-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3806)[§](#method.default-3)

Creates an empty `[T]` inside an Arc

This may or may not share an allocation with other Arcs.

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3782)[§](#impl-Default-for-Arc%3CCStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3787)[§](#method.default-2)

Creates an empty CStr inside an Arc

This may or may not share an allocation with other Arcs.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3715)[§](#impl-Default-for-Arc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3726)[§](#method.default)

Creates a new `Arc<T>`, with the `Default` value for `T`.

##### [§](#examples-49)Examples

```rust
use std::sync::Arc;

let x: Arc<i32> = Default::default();
assert_eq!(*x, 0);
```

1.80.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3767)[§](#impl-Default-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3772)[§](#method.default-1)

Creates an empty str inside an Arc

This may or may not share an allocation with other Arcs.

1.91.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3828-3831)[§](#impl-Default-for-Pin%3CArc%3CT%3E%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2417)[§](#impl-Deref-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2418)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2421)[§](#method.deref)

Dereferences the value.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3693)[§](#impl-Display-for-Arc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2780)[§](#impl-Drop-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2807)[§](#method.drop)

Drops the `Arc`.

This will decrement the strong reference count. If the strong reference count reaches zero then the only other references (if any) are [`Weak`](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak"), so we `drop` the inner value.

##### [§](#examples-47)Examples

```rust
use std::sync::Arc;

struct Foo;

impl Drop for Foo {
    fn drop(&mut self) {
        println!("dropped!");
    }
}

let foo  = Arc::new(Foo);
let foo2 = Arc::clone(&foo);

drop(foo);    // Doesn't print anything
drop(foo2);   // Prints "dropped!"
```

1.52.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4297)[§](#impl-Error-for-Arc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4299)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4303)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.source)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4307)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/std/error/trait.Error.html#method.provide)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3891)[§](#impl-From%3C%26%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3903)[§](#method.from-7)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-4)Example

```rust
let original: &[i32] = &[1, 2, 3];
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#911)[§](#impl-From%3C%26CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#915)[§](#method.from-3)

Converts a `&CStr` into a `Arc<CStr>`, by copying the contents into a newly allocated [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc").

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1374-1381)[§](#impl-From%3C%26OsStr%3E-for-Arc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2154-2161)[§](#impl-From%3C%26Path%3E-for-Arc%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3910)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3923)[§](#method.from-8)

Allocates a reference-counted slice and fills it by cloning `v`’s items.

##### [§](#example-5)Example

```rust
let mut original = [1, 2, 3];
let original: &mut [i32] = &mut original;
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#923)[§](#impl-From%3C%26mut+CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#927)[§](#method.from-4)

Converts a `&mut CStr` into a `Arc<CStr>`, by copying the contents into a newly allocated [`Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc").

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1384-1390)[§](#impl-From%3C%26mut+OsStr%3E-for-Arc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2164-2170)[§](#impl-From%3C%26mut+Path%3E-for-Arc%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3949)[§](#impl-From%3C%26mut+str%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3962)[§](#method.from-10)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-7)Example

```rust
let mut original = String::from("eggplant");
let original: &mut str = &mut original;
let shared: Arc<str> = Arc::from(original);
assert_eq!("eggplant", &shared[..]);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3930)[§](#impl-From%3C%26str%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3941)[§](#method.from-9)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-6)Example

```rust
let shared: Arc<str> = Arc::from("eggplant");
assert_eq!("eggplant", &shared[..]);
```

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3870)[§](#impl-From%3C%5BT;+N%5D%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3884)[§](#method.from-6)

Converts a [`[T; N]`](https://doc.rust-lang.org/std/primitive.array.html "primitive array") into an `Arc<[T]>`.

The conversion moves the array into a newly allocated `Arc`.

##### [§](#example-3)Example

```rust
let original: [i32; 3] = [1, 2, 3];
let shared: Arc<[i32]> = Arc::from(original);
assert_eq!(&[1, 2, 3], &shared[..]);
```

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#644)[§](#impl-From%3CArc%3C%5Bu8%5D%3E%3E-for-Arc%3CByteStr%3E)

Available on **non-`no_rc` and non-`no_sync` and `target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#646)[§](#method.from)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#654)[§](#impl-From%3CArc%3CByteStr%3E%3E-for-Arc%3C%5Bu8%5D%3E)

Available on **non-`no_rc` and non-`no_sync` and `target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#656)[§](#method.from-1)

Converts to this type from the input type.

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/task.rs.html#121)[§](#impl-From%3CArc%3CW%3E%3E-for-RawWaker)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#125)[§](#method.from-17)

Use a `Wake`-able type as a `RawWaker`.

No heap allocations or atomic operations are used for this conversion.

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/task.rs.html#109)[§](#impl-From%3CArc%3CW%3E%3E-for-Waker)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#113)[§](#method.from-16)

Use a [`Wake`](https://doc.rust-lang.org/std/task/trait.Wake.html "trait std::task::Wake")-able type as a `Waker`.

No heap allocations or atomic operations are used for this conversion.

1.62.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4063)[§](#impl-From%3CArc%3Cstr%3E%3E-for-Arc%3C%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4075)[§](#method.from-15)

Converts an atomically reference-counted string slice into a byte slice.

##### [§](#example-12)Example

```rust
let string: Arc<str> = Arc::from("eggplant");
let bytes: Arc<[u8]> = Arc::from(string);
assert_eq!("eggplant".as_bytes(), bytes.as_ref());
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3988)[§](#impl-From%3CBox%3CT,+A%3E%3E-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4000)[§](#method.from-12)

Move a boxed object to a new, reference-counted allocation.

##### [§](#example-9)Example

```rust
let unique: Box<str> = Box::from("eggplant");
let shared: Arc<str> = Arc::from(unique);
assert_eq!("eggplant", &shared[..]);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#899)[§](#impl-From%3CCString%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4036-4039)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Arc%3CB%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4054)[§](#method.from-14)

Creates an atomically reference-counted pointer from a clone-on-write pointer by copying its content.

##### [§](#example-11)Example

```rust
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
let shared: Arc<str> = Arc::from(cow);
assert_eq!("eggplant", &shared[..]);
```

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1363-1371)[§](#impl-From%3COsString%3E-for-Arc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2143-2151)[§](#impl-From%3CPathBuf%3E-for-Arc%3CPath%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3969)[§](#impl-From%3CString%3E-for-Arc%3Cstr%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3981)[§](#method.from-11)

Allocates a reference-counted `str` and copies `v` into it.

##### [§](#example-8)Example

```rust
let unique: String = "eggplant".to_owned();
let shared: Arc<str> = Arc::from(unique);
assert_eq!("eggplant", &shared[..]);
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3848)[§](#impl-From%3CT%3E-for-Arc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3863)[§](#method.from-5)

Converts a `T` into an `Arc<T>`

The conversion moves the value into a newly allocated `Arc`. It is equivalent to calling `Arc::new(t)`.

##### [§](#example-2)Example

```rust
let x = 5;
let arc = Arc::new(5);

assert_eq!(Arc::from(x), arc);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4007)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Arc%3C%5BT%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4019)[§](#method.from-13)

Allocates a reference-counted slice and moves `v`’s items into it.

##### [§](#example-10)Example

```rust
let unique: Vec<i32> = vec![1, 2, 3];
let shared: Arc<[i32]> = Arc::from(unique);
assert_eq!(&[1, 2, 3], &shared[..]);
```

1.37.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4097)[§](#impl-FromIterator%3CT%3E-for-Arc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4136)[§](#method.from_iter)

Takes each element in the `Iterator` and collects it into an `Arc<[T]>`.

##### [§](#performance-characteristics)Performance characteristics

###### [§](#the-general-case)The general case

In the general case, collecting into `Arc<[T]>` is done by first collecting into a `Vec<T>`. That is, when writing the following:

```rust
let evens: Arc<[u8]> = (0..10).filter(|&x| x % 2 == 0).collect();
```

this behaves as if we wrote:

```rust
let evens: Arc<[u8]> = (0..10).filter(|&x| x % 2 == 0)
    .collect::<Vec<_>>() // The first set of allocations happens here.
    .into(); // A second allocation for `Arc<[T]>` happens here.
```

This will allocate as many times as needed for constructing the `Vec<T>` and then it will allocate once for turning the `Vec<T>` into the `Arc<[T]>`.

###### [§](#iterators-of-known-length)Iterators of known length

When your `Iterator` implements `TrustedLen` and is of an exact size, a single allocation will be made for the `Arc<[T]>`. For example:

```rust
let evens: Arc<[u8]> = (0..10).collect(); // Just a single allocation happens here.
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3840)[§](#impl-Hash-for-Arc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3670)[§](#impl-Ord-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3685)[§](#method.cmp)

Comparison for two `Arc`s.

The two are compared by calling `cmp()` on their inner values.

##### [§](#examples-50)Examples

```rust
use std::sync::Arc;
use std::cmp::Ordering;

let five = Arc::new(5);

assert_eq!(Ordering::Less, five.cmp(&Arc::new(6)));
```

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1033-1035)[§](#method.max)

Compares and returns the maximum of two values. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.max)

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1072-1074)[§](#method.min)

Compares and returns the minimum of two values. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.min)

1.50.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1098-1100)[§](#method.clamp)

Restrict a value to a certain interval. [Read more](https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.clamp)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3536)[§](#impl-PartialEq-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3555)[§](#method.eq)

Equality for two `Arc`s.

Two `Arc`s are equal if their inner values are equal, even if they are stored in different allocation.

If `T` also implements `Eq` (implying reflexivity of equality), two `Arc`s that point to the same allocation are always equal.

##### [§](#examples-51)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five == Arc::new(5));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3576)[§](#method.ne)

Inequality for two `Arc`s.

Two `Arc`s are not equal if their inner values are not equal.

If `T` also implements `Eq` (implying reflexivity of equality), two `Arc`s that point to the same value are always equal.

##### [§](#examples-52)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five != Arc::new(6));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3582)[§](#impl-PartialOrd-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3597)[§](#method.partial_cmp)

Partial comparison for two `Arc`s.

The two are compared by calling `partial_cmp()` on their inner values.

##### [§](#examples-53)Examples

```rust
use std::sync::Arc;
use std::cmp::Ordering;

let five = Arc::new(5);

assert_eq!(Some(Ordering::Less), five.partial_cmp(&Arc::new(6)));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3614)[§](#method.lt)

Less-than comparison for two `Arc`s.

The two are compared by calling `<` on their inner values.

##### [§](#examples-54)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five < Arc::new(6));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3631)[§](#method.le)

‘Less than or equal to’ comparison for two `Arc`s.

The two are compared by calling `<=` on their inner values.

##### [§](#examples-55)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five <= Arc::new(5));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3648)[§](#method.gt)

Greater-than comparison for two `Arc`s.

The two are compared by calling `>` on their inner values.

##### [§](#examples-56)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five > Arc::new(4));
```

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3665)[§](#method.ge)

‘Greater than or equal to’ comparison for two `Arc`s.

The two are compared by calling `>=` on their inner values.

##### [§](#examples-57)Examples

```rust
use std::sync::Arc;

let five = Arc::new(5);

assert!(five >= Arc::new(5));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3707)[§](#impl-Pointer-for-Arc%3CT,+A%3E)

1.73.0 · [Source](https://doc.rust-lang.org/src/std/fs.rs.html#1544-1564)[§](#impl-Read-for-Arc%3CFile%3E)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1545-1547)[§](#method.read)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1548-1550)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1551-1553)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1555-1557)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1558-1560)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1561-1563)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

1.6.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1044-1046)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1080-1082)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1200-1205)[§](#method.chain)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1239-1244)[§](#method.take)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_array)

1.73.0 · [Source](https://doc.rust-lang.org/src/std/fs.rs.html#1583-1593)[§](#impl-Seek-for-Arc%3CFile%3E)

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4082)[§](#impl-TryFrom%3CArc%3C%5BT%5D,+A%3E%3E-for-Arc%3C%5BT;+N%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4083)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4085)[§](#method.try_from)

Performs the conversion.

1.73.0 · [Source](https://doc.rust-lang.org/src/std/fs.rs.html#1566-1581)[§](#impl-Write-for-Arc%3CFile%3E)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1567-1569)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1570-1572)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1574-1576)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/fs.rs.html#1578-1580)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1875-1887)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1937-1952)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-2)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#289)[§](#impl-CloneFromCell-for-Arc%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#282)[§](#impl-CoerceUnsized%3CArc%3CU,+A%3E%3E-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2433)[§](#impl-DerefPure-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#285)[§](#impl-DispatchFromDyn%3CArc%3CU%3E%3E-for-Arc%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3690)[§](#impl-Eq-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2427)[§](#impl-PinCoerceUnsized-for-Arc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#274)[§](#impl-Send-for-Arc%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#276)[§](#impl-Sync-for-Arc%3CT,+A%3E)

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4196)[§](#impl-Unpin-for-Arc%3CT,+A%3E)

1.9.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#279)[§](#impl-UnwindSafe-for-Arc%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#2414)[§](#impl-UseCloned-for-Arc%3CT,+A%3E)