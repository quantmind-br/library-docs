---
title: Cow in std::borrow - Rust
url: https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed
source: crawler
fetched_at: 2026-05-06T21:33:56.683851183-03:00
rendered_js: false
word_count: 6957
summary: The Cow smart pointer in Rust enables memory-efficient handling of data by allowing shared immutable access to borrowed data and performing lazy cloning only when mutation or ownership is required.
tags:
    - rust
    - smart-pointer
    - memory-management
    - clone-on-write
    - ownership
    - lazy-evaluation
category: reference
---

```rust
pub enum Cow<'a, B>
where
    B: 'a + ToOwned + ?Sized,{
    Borrowed(&'a B),
    Owned(<B as ToOwned>::Owned),
}
```

Expand description

A clone-on-write smart pointer.

The type `Cow` is a smart pointer providing clone-on-write functionality: it can enclose and provide immutable access to borrowed data, and clone the data lazily when mutation or ownership is required. The type is designed to work with general borrowed data via the `Borrow` trait.

`Cow` implements `Deref`, which means that you can call non-mutating methods directly on the data it encloses. If mutation is desired, `to_mut` will obtain a mutable reference to an owned value, cloning if necessary.

If you need reference-counting pointers, note that [`Rc::make_mut`](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html#method.make_mut "associated function std::rc::Rc::make_mut") and [`Arc::make_mut`](https://doc.rust-lang.org/stable/std/sync/struct.Arc.html#method.make_mut "associated function std::sync::Arc::make_mut") can provide clone-on-write functionality as well.

## [§](#examples)Examples

```rust
use std::borrow::Cow;

fn abs_all(input: &mut Cow<'_, [i32]>) {
    for i in 0..input.len() {
        let v = input[i];
        if v < 0 {
            // Clones into a vector if not already owned.
            input.to_mut()[i] = -v;
        }
    }
}

// No clone occurs because `input` doesn't need to be mutated.
let slice = [0, 1, 2];
let mut input = Cow::from(&slice[..]);
abs_all(&mut input);

// Clone occurs because `input` needs to be mutated.
let slice = [-1, 0, 1];
let mut input = Cow::from(&slice[..]);
abs_all(&mut input);

// No clone occurs because `input` is already owned.
let mut input = Cow::from(vec![-1, 0, 1]);
abs_all(&mut input);
```

Another example showing how to keep `Cow` in a struct:

```rust
use std::borrow::Cow;

struct Items<'a, X> where [X]: ToOwned<Owned = Vec<X>> {
    values: Cow<'a, [X]>,
}

impl<'a, X: Clone + 'a> Items<'a, X> where [X]: ToOwned<Owned = Vec<X>> {
    fn new(v: Cow<'a, [X]>) -> Self {
        Items { values: v }
    }
}

// Creates a container from borrowed values of a slice
let readonly = [1, 2];
let borrowed = Items::new((&readonly[..]).into());
match borrowed {
    Items { values: Cow::Borrowed(b) } => println!("borrowed {b:?}"),
    _ => panic!("expect borrowed value"),
}

let mut clone_on_write = borrowed;
// Mutates the data from slice into owned vec and pushes a new value on top
clone_on_write.values.to_mut().push(3);
println!("clone_on_write = {:?}", clone_on_write.values);

// The data was mutated. Let's check it out.
match clone_on_write {
    Items { values: Cow::Owned(_) } => println!("clone_on_write contains owned data"),
    _ => panic!("expect owned data"),
}
```

[§](#variant.Borrowed)1.0.0

Borrowed data.

[§](#variant.Owned)1.0.0

Owned data.

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#215)[§](#impl-Cow%3C'_,+B%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#235)

🔬This is a nightly-only experimental API. (`cow_is_borrowed` [#65143](https://github.com/rust-lang/rust/issues/65143))

Returns true if the data is borrowed, i.e. if `to_mut` would require additional work.

Note: this is an associated function, which means that you have to call it as `Cow::is_borrowed(&c)` instead of `c.is_borrowed()`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-1)Examples

```rust
#![feature(cow_is_borrowed)]
use std::borrow::Cow;

let cow = Cow::Borrowed("moo");
assert!(Cow::is_borrowed(&cow));

let bull: Cow<'_, str> = Cow::Owned("...moo?".to_string());
assert!(!Cow::is_borrowed(&bull));
```

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#261)

🔬This is a nightly-only experimental API. (`cow_is_borrowed` [#65143](https://github.com/rust-lang/rust/issues/65143))

Returns true if the data is owned, i.e. if `to_mut` would be a no-op.

Note: this is an associated function, which means that you have to call it as `Cow::is_owned(&c)` instead of `c.is_owned()`. This is so that there is no conflict with a method on the inner type.

##### [§](#examples-2)Examples

```rust
#![feature(cow_is_borrowed)]
use std::borrow::Cow;

let cow: Cow<'_, str> = Cow::Owned("moo".to_string());
assert!(Cow::is_owned(&cow));

let bull = Cow::Borrowed("...moo?");
assert!(!Cow::is_owned(&bull));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#283)

Acquires a mutable reference to the owned form of the data.

Clones the data if it is not already owned.

##### [§](#examples-3)Examples

```rust
use std::borrow::Cow;

let mut cow = Cow::Borrowed("foo");
cow.to_mut().make_ascii_uppercase();

assert_eq!(
  cow,
  Cow::Owned(String::from("FOO")) as Cow<'_, str>
);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#331)

Extracts the owned data.

Clones the data if it is not already owned.

##### [§](#examples-4)Examples

Calling `into_owned` on a `Cow::Borrowed` returns a clone of the borrowed data:

```rust
use std::borrow::Cow;

let s = "Hello world!";
let cow = Cow::Borrowed(s);

assert_eq!(
  cow.into_owned(),
  String::from(s)
);
```

Calling `into_owned` on a `Cow::Owned` returns the owned data. The data is moved out of the `Cow` without being cloned.

```rust
use std::borrow::Cow;

let s = "Hello world!";
let cow: Cow<'_, str> = Cow::Owned(String::from(s));

assert_eq!(
  cow.into_owned(),
  String::from(s)
);
```

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#470)[§](#impl-Add%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#471)[§](#associatedtype.Output)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#474)[§](#method.add)

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#482)[§](#impl-Add-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#483)[§](#associatedtype.Output-1)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#486)[§](#method.add-1)

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#494)[§](#impl-AddAssign%3C%26str%3E-for-Cow%3C'a,+str%3E)

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#511)[§](#impl-AddAssign-for-Cow%3C'a,+str%3E)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3784-3789)[§](#impl-AsRef%3CPath%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3786-3788)[§](#method.as_ref-1)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#459)[§](#impl-AsRef%3CT%3E-for-Cow%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#463)[§](#method.as_ref)

Converts this type into a shared reference of the (usually inferred) input type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#186)[§](#impl-Borrow%3CB%3E-for-Cow%3C'a,+B%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#196)[§](#impl-Clone-for-Cow%3C'_,+B%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#408-410)[§](#impl-Debug-for-Cow%3C'_,+B%3E)

1.11.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#434-436)[§](#impl-Default-for-Cow%3C'_,+B%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#439)[§](#method.default)

Creates an owned Cow&lt;’a, B&gt; with the default value for the contained owned value.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#343)[§](#impl-Deref-for-Cow%3C'_,+B%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#347)[§](#associatedtype.Target)

The resulting type after dereferencing.

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#349)[§](#method.deref)

Dereferences the value.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#421-423)[§](#impl-Display-for-Cow%3C'_,+B%3E)

1.52.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1783-1790)[§](#impl-Extend%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1785-1789)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#420)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#method.extend_reserve)

1.19.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2566)[§](#impl-Extend%3CCow%3C'a,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2567)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2572)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#method.extend_reserve)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#5)[§](#impl-From%3C%26%5BT%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#12)[§](#method.from-18)

Creates a [`Borrowed`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed "variant std::borrow::Cow::Borrowed") variant of [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") from a slice.

This conversion does not allocate or clone the data.

1.77.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#18)[§](#impl-From%3C%26%5BT;+N%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#25)[§](#method.from-19)

Creates a [`Borrowed`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed "variant std::borrow::Cow::Borrowed") variant of [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") from a reference to an array.

This conversion does not allocate or clone the data.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#597)[§](#impl-From%3C%26ByteStr%3E-for-Cow%3C'a,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#599)[§](#method.from-6)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#256)[§](#impl-From%3C%26ByteString%3E-for-Cow%3C'a,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#258)[§](#method.from-5)

Converts to this type from the input type.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#880)[§](#impl-From%3C%26CStr%3E-for-Cow%3C'a,+CStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#883)[§](#method.from-10)

Converts a [`CStr`](https://doc.rust-lang.org/stable/std/ffi/struct.CStr.html "struct std::ffi::CStr") into a borrowed [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") without copying or allocating.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#889)[§](#impl-From%3C%26CString%3E-for-Cow%3C'a,+CStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1432-1438)[§](#impl-From%3C%26OsStr%3E-for-Cow%3C'a,+OsStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1441-1447)[§](#impl-From%3C%26OsString%3E-for-Cow%3C'a,+OsStr%3E)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2096-2105)[§](#impl-From%3C%26Path%3E-for-Cow%3C'a,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2102-2104)[§](#method.from-29)

Creates a clone-on-write pointer from a reference to [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path").

This conversion does not clone or allocate.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2120-2129)[§](#impl-From%3C%26PathBuf%3E-for-Cow%3C'a,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2126-2128)[§](#method.from-31)

Creates a clone-on-write pointer from a reference to [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf").

This conversion does not clone or allocate.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3251)[§](#impl-From%3C%26String%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3266)[§](#method.from-16)

Converts a [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") reference into a [`Borrowed`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed "borrow::Cow::Borrowed") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-4)Example

```rust
let s = "eggplant".to_string();
assert_eq!(Cow::from(&s), Cow::Borrowed("eggplant"));
```

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#44)[§](#impl-From%3C%26Vec%3CT%3E%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#51)[§](#method.from-21)

Creates a [`Borrowed`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed "variant std::borrow::Cow::Borrowed") variant of [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") from a reference to [`Vec`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html "struct std::vec::Vec").

This conversion does not allocate or clone the data.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3207)[§](#impl-From%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3221)[§](#method.from-14)

Converts a string slice into a [`Borrowed`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Borrowed "borrow::Cow::Borrowed") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-2)Example

```rust
assert_eq!(Cow::from("eggplant"), Cow::Borrowed("eggplant"));
```

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#248)[§](#impl-From%3CByteString%3E-for-Cow%3C'a,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#250)[§](#method.from-4)

Converts to this type from the input type.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#871)[§](#impl-From%3CCString%3E-for-Cow%3C'a,+CStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#106)[§](#impl-From%3CCow%3C'_,+%5BT%5D%3E%3E-for-Box%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#114)[§](#method.from)

Converts a `Cow<'_, [T]>` into a `Box<[T]>`

When `cow` is the `Cow::Borrowed` variant, this conversion allocates on the heap and copies the underlying slice. Otherwise, it will try to reuse the owned `Vec`’s allocation.

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#783)[§](#impl-From%3CCow%3C'_,+CStr%3E%3E-for-Box%3CCStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#787)[§](#method.from-8)

Converts a `Cow<'a, CStr>` into a `Box<CStr>`, by copying the contents if they are borrowed.

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1313-1323)[§](#impl-From%3CCow%3C'_,+OsStr%3E%3E-for-Box%3COsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1317-1322)[§](#method.from-23)

Converts a `Cow<'a, OsStr>` into a `Box<OsStr>`, by copying the contents if they are borrowed.

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1909-1920)[§](#impl-From%3CCow%3C'_,+Path%3E%3E-for-Box%3CPath%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#1914-1919)[§](#method.from-28)

Creates a boxed [`Path`](https://doc.rust-lang.org/stable/std/path/struct.Path.html "struct std::path::Path") from a clone-on-write pointer.

Converting from a `Cow::Owned` does not clone or allocate.

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#166)[§](#impl-From%3CCow%3C'_,+str%3E%3E-for-Box%3Cstr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#191)[§](#method.from-1)

Converts a `Cow<'_, str>` into a `Box<str>`

When `cow` is the `Cow::Borrowed` variant, this conversion allocates on the heap and copies the underlying `str`. Otherwise, it will try to reuse the owned `String`’s allocation.

##### [§](#examples-5)Examples

```rust
use std::borrow::Cow;

let unboxed = Cow::Borrowed("hello");
let boxed: Box<str> = Box::from(unboxed);
println!("{boxed}");
```

```rust
let unboxed = Cow::Owned("hello".to_string());
let boxed: Box<str> = Box::from(unboxed);
println!("{boxed}");
```

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/mod.rs.html#4352-4354)[§](#impl-From%3CCow%3C'a,+%5BT%5D%3E%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/mod.rs.html#4370)[§](#method.from-22)

Converts a clone-on-write slice into a vector.

If `s` already owns a `Vec<T>`, it will be returned directly. If `s` is borrowing a slice, a new `Vec<T>` will be allocated and filled by cloning `s`’s items into it.

##### [§](#examples-8)Examples

```rust
let o: Cow<'_, [i32]> = Cow::Owned(vec![1, 2, 3]);
let b: Cow<'_, [i32]> = Cow::Borrowed(&[1, 2, 3]);
assert_eq!(Vec::from(o), Vec::from(b));
```

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/sync.rs.html#4036-4039)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Arc%3CB%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/sync.rs.html#4054)[§](#method.from-17)

Creates an atomically reference-counted pointer from a clone-on-write pointer by copying its content.

##### [§](#example-5)Example

```rust
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
let shared: Arc<str> = Arc::from(cow);
assert_eq!("eggplant", &shared[..]);
```

1.45.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/rc.rs.html#3002-3005)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Rc%3CB%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/rc.rs.html#3020)[§](#method.from-12)

Creates a reference-counted pointer from a clone-on-write pointer by copying its content.

##### [§](#example)Example

```rust
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
let shared: Rc<str> = Rc::from(cow);
assert_eq!("eggplant", &shared[..]);
```

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#755)[§](#impl-From%3CCow%3C'a,+CStr%3E%3E-for-CString)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#759)[§](#method.from-7)

Converts a `Cow<'a, CStr>` into a `CString`, by copying the contents if they are borrowed.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1450-1457)[§](#impl-From%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1454-1456)[§](#method.from-27)

Converts a `Cow<'a, OsStr>` into an [`OsString`](https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html "struct std::ffi::OsString"), by copying the contents if they are borrowed.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2132-2140)[§](#impl-From%3CCow%3C'a,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2137-2139)[§](#method.from-32)

Converts a clone-on-write pointer to an owned path.

Converting from a `Cow::Owned` does not clone or allocate.

1.14.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3183)[§](#impl-From%3CCow%3C'a,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3200)[§](#method.from-13)

Converts a clone-on-write string to an owned instance of [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String").

This extracts the owned string, clones the string if it is not already owned.

##### [§](#example-1)Example

```rust
// If the string is not owned...
let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
// It will allocate on the heap and copy the string.
let owned: String = String::from(cow);
assert_eq!(&owned[..], "eggplant");
```

1.22.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#687)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#700)[§](#method.from-3)

Converts a [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") into a box of dyn [`Error`](https://doc.rust-lang.org/stable/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-7)Examples

```rust
use std::error::Error;
use std::borrow::Cow;

let a_cow_str_error = Cow::from("a str error");
let a_boxed_error = Box::<dyn Error>::from(a_cow_str_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.22.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#666)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/boxed/convert.rs.html#680)[§](#method.from-2)

Converts a [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") into a box of dyn [`Error`](https://doc.rust-lang.org/stable/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/stable/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-6)Examples

```rust
use std::error::Error;
use std::borrow::Cow;

let a_cow_str_error = Cow::from("a str error");
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_cow_str_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1423-1429)[§](#impl-From%3COsString%3E-for-Cow%3C'a,+OsStr%3E)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2108-2117)[§](#impl-From%3CPathBuf%3E-for-Cow%3C'a,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#2114-2116)[§](#method.from-30)

Creates a clone-on-write pointer from an owned instance of [`PathBuf`](https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html "struct std::path::PathBuf").

This conversion does not clone or allocate.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3228)[§](#impl-From%3CString%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3244)[§](#method.from-15)

Converts a [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") into an [`Owned`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Owned "borrow::Cow::Owned") variant. No heap allocation is performed, and the string is not copied.

##### [§](#example-3)Example

```rust
let s = "eggplant".to_string();
let s2 = "eggplant".to_string();
assert_eq!(Cow::from(s), Cow::<'static, str>::Owned(s2));
```

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#31)[§](#impl-From%3CVec%3CT%3E%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#38)[§](#method.from-20)

Creates an [`Owned`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html#variant.Owned "variant std::borrow::Cow::Owned") variant of [`Cow`](https://doc.rust-lang.org/stable/std/borrow/enum.Cow.html "enum std::borrow::Cow") from an owned instance of [`Vec`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html "struct std::vec::Vec").

This conversion does not allocate or clone the data.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3281)[§](#impl-FromIterator%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3297)[§](#impl-FromIterator%3CChar%3E-for-Cow%3C'a,+str%3E)

1.52.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1824-1845)[§](#impl-FromIterator%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

1.80.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/boxed/iter.rs.html#190)[§](#impl-FromIterator%3CCow%3C'a,+str%3E%3E-for-Box%3Cstr%3E)

1.19.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2425)[§](#impl-FromIterator%3CCow%3C'a,+str%3E%3E-for-String)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3289)[§](#impl-FromIterator%3CString%3E-for-Cow%3C'a,+str%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/cow.rs.html#57-59)[§](#impl-FromIterator%3CT%3E-for-Cow%3C'a,+%5BT%5D%3E)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#3273)[§](#impl-FromIterator%3Cchar%3E-for-Cow%3C'a,+str%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#445-447)[§](#impl-Hash-for-Cow%3C'_,+B%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#374-376)[§](#impl-Ord-for-Cow%3C'_,+B%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#32)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#32)[§](#method.eq-25)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#32)[§](#method.ne-25)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#impl-PartialEq%3C%26ByteStr%3E-for-Cow%3C'_,+%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#method.eq-12)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-12)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#impl-PartialEq%3C%26ByteStr%3E-for-Cow%3C'_,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#method.eq-8)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-8)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#impl-PartialEq%3C%26ByteStr%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#method.eq-10)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-10)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1256)[§](#impl-PartialEq%3C%26CStr%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1258)[§](#method.eq-16)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1263)[§](#method.ne-16)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialEq%3C%26OsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#method.eq-29)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-29)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#impl-PartialEq%3C%26OsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#method.eq-47)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-47)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#impl-PartialEq%3C%26Path%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#method.eq-44)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-44)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#impl-PartialEq%3C%26Path%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#method.eq-35)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-35)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#34)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#34)[§](#method.eq-26)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#34)[§](#method.ne-26)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#impl-PartialEq%3C%26str%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#method.eq-20)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#method.ne-20)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#impl-PartialEq%3CByteString%3E-for-Cow%3C'_,+%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#impl-PartialEq%3CByteString%3E-for-Cow%3C'_,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#impl-PartialEq%3CByteString%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1242)[§](#impl-PartialEq%3CCStr%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1244)[§](#method.eq-15)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1249)[§](#method.ne-15)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1270)[§](#impl-PartialEq%3CCString%3E-for-Cow%3C'_,+CStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1272)[§](#method.eq-17)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1277)[§](#method.ne-17)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#impl-PartialEq%3CCow%3C'_,+%5Bu8%5D%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#method.eq-11)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-11)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#impl-PartialEq%3CCow%3C'_,+%5Bu8%5D%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#impl-PartialEq%3CCow%3C'_,+ByteStr%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#method.eq-7)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-7)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#impl-PartialEq%3CCow%3C'_,+ByteStr%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1228)[§](#impl-PartialEq%3CCow%3C'_,+CStr%3E%3E-for-CStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1230)[§](#method.eq-14)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1235)[§](#method.ne-14)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.90.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1119)[§](#impl-PartialEq%3CCow%3C'_,+CStr%3E%3E-for-CString)

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1121)[§](#method.eq-13)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/ffi/c_str.rs.html#1126)[§](#method.ne-13)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#method.eq-30)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-30)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#method.eq-43)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-43)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#method.eq-28)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-28)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#method.eq-32)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-32)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#method.eq-41)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-41)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialEq%3CCow%3C'_,+OsStr%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.eq-39)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-39)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#method.eq-48)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-48)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#method.eq-36)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-36)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#method.eq-46)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-46)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#method.eq-50)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-50)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#method.eq-34)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-34)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialEq%3CCow%3C'_,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.eq-38)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-38)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#method.eq-9)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-9)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-%26str)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#method.eq-21)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2694)[§](#method.ne-21)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-String)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#method.eq-23)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#method.ne-23)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#impl-PartialEq%3CCow%3C'_,+str%3E%3E-for-str)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#method.eq-19)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#method.ne-19)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#385-388)[§](#impl-PartialEq%3CCow%3C'b,+C%3E%3E-for-Cow%3C'a,+B%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#391)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialEq%3COsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#method.eq-27)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-27)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#impl-PartialEq%3COsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#method.eq-45)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-45)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialEq%3COsString%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#method.eq-31)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-31)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#impl-PartialEq%3COsString%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#method.eq-49)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-49)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#impl-PartialEq%3CPath%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#method.eq-42)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-42)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#impl-PartialEq%3CPath%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#method.eq-33)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-33)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialEq%3CPathBuf%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.eq-40)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-40)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialEq%3CPathBuf%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.eq-37)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne-37)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#impl-PartialEq%3CString%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#method.eq-22)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2696)[§](#method.ne-22)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#30)[§](#impl-PartialEq%3CVec%3CU,+A%3E%3E-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#30)[§](#method.eq-24)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/vec/partial_eq.rs.html#30)[§](#method.ne-24)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#impl-PartialEq%3Cstr%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#method.eq-18)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2692)[§](#method.ne-18)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#impl-PartialOrd%3C%26ByteStr%3E-for-Cow%3C'_,+%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#method.partial_cmp-12)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-12)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-12)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-12)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-12)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#impl-PartialOrd%3C%26ByteStr%3E-for-Cow%3C'_,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#method.partial_cmp-8)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-8)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-8)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-8)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-8)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#impl-PartialOrd%3C%26ByteStr%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#method.partial_cmp-10)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-10)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-10)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-10)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-10)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialOrd%3C%26OsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#method.partial_cmp-15)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-15)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-15)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-15)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-15)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#impl-PartialOrd%3C%26OsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#method.partial_cmp-33)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-33)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-33)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-33)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-33)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#impl-PartialOrd%3C%26Path%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#method.partial_cmp-30)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-30)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-30)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-30)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-30)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#impl-PartialOrd%3C%26Path%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#method.partial_cmp-21)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-21)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-21)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-21)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-21)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#impl-PartialOrd%3CByteString%3E-for-Cow%3C'_,+%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#method.partial_cmp-6)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-6)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-6)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-6)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-6)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#impl-PartialOrd%3CByteString%3E-for-Cow%3C'_,+ByteStr%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#method.partial_cmp-2)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-2)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-2)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-2)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-2)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#impl-PartialOrd%3CByteString%3E-for-Cow%3C'_,+str%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#method.partial_cmp-4)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-4)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-4)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-4)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-4)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#impl-PartialOrd%3CCow%3C'_,+%5Bu8%5D%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#668)[§](#method.partial_cmp-11)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-11)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-11)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-11)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-11)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#impl-PartialOrd%3CCow%3C'_,+%5Bu8%5D%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#538)[§](#method.partial_cmp-5)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-5)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-5)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-5)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-5)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#impl-PartialOrd%3CCow%3C'_,+ByteStr%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#666)[§](#method.partial_cmp-7)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-7)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-7)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-7)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-7)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#impl-PartialOrd%3CCow%3C'_,+ByteStr%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#536)[§](#method.partial_cmp-1)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-1)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-1)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-1)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-1)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1604)[§](#method.partial_cmp-16)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-16)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-16)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-16)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-16)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3930)[§](#method.partial_cmp-29)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-29)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-29)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-29)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-29)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#method.partial_cmp-14)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-14)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-14)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-14)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-14)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#method.partial_cmp-18)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-18)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-18)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-18)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-18)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#method.partial_cmp-27)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-27)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-27)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-27)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-27)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialOrd%3CCow%3C'_,+OsStr%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.partial_cmp-25)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-25)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-25)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-25)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-25)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-%26OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3933)[§](#method.partial_cmp-34)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-34)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-34)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-34)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-34)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-%26Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3882)[§](#method.partial_cmp-22)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-22)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-22)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-22)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-22)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-OsStr)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#method.partial_cmp-32)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-32)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-32)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-32)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-32)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-OsString)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#method.partial_cmp-36)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-36)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-36)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-36)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-36)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-Path)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#method.partial_cmp-20)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-20)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-20)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-20)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-20)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialOrd%3CCow%3C'_,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.partial_cmp-24)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-24)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-24)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-24)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-24)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#impl-PartialOrd%3CCow%3C'_,+str%3E%3E-for-%26ByteStr)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#667)[§](#method.partial_cmp-9)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-9)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-9)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-9)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-9)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#impl-PartialOrd%3CCow%3C'_,+str%3E%3E-for-ByteString)

[Source](https://doc.rust-lang.org/stable/src/alloc/bstr.rs.html#537)[§](#method.partial_cmp-3)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-3)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-3)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-3)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-3)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#impl-PartialOrd%3COsStr%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1603)[§](#method.partial_cmp-13)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-13)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-13)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-13)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-13)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#impl-PartialOrd%3COsStr%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3932)[§](#method.partial_cmp-31)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-31)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-31)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-31)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-31)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#impl-PartialOrd%3COsString%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1605)[§](#method.partial_cmp-17)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-17)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-17)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-17)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-17)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#impl-PartialOrd%3COsString%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3934)[§](#method.partial_cmp-35)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-35)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-35)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-35)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-35)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#impl-PartialOrd%3CPath%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3927)[§](#method.partial_cmp-28)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-28)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-28)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-28)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-28)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#impl-PartialOrd%3CPath%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3881)[§](#method.partial_cmp-19)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-19)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-19)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-19)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-19)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#impl-PartialOrd%3CPathBuf%3E-for-Cow%3C'_,+OsStr%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3923)[§](#method.partial_cmp-26)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-26)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-26)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-26)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-26)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.8.0 · [Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#impl-PartialOrd%3CPathBuf%3E-for-Cow%3C'_,+Path%3E)

[Source](https://doc.rust-lang.org/stable/src/std/path.rs.html#3883)[§](#method.partial_cmp-23)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt-23)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le-23)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt-23)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge-23)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#397-399)[§](#impl-PartialOrd-for-Cow%3C'a,+B%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#402)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#368)[§](#impl-DerefPure-for-Cow%3C'_,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#362)[§](#impl-DerefPure-for-Cow%3C'_,+T%3E)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#365)[§](#impl-DerefPure-for-Cow%3C'_,+str%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#371)[§](#impl-Eq-for-Cow%3C'_,+B%3E)