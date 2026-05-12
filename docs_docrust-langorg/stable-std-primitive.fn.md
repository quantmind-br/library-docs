---
title: fn - Rust
url: https://doc.rust-lang.org/stable/std/primitive.fn.html
source: crawler
fetched_at: 2026-05-06T21:28:16.400422262-03:00
rendered_js: false
word_count: 2081
summary: This document explains the mechanics of function pointers in Rust, covering their safety properties, ABI specifications, variadic support, and memory layout.
tags:
    - rust
    - function-pointers
    - abi
    - ffi
    - memory-safety
    - unsafe-rust
category: concept
---

Expand description

Function pointers, like `fn(usize) -> bool`.

*See also the traits [`Fn`](https://doc.rust-lang.org/stable/std/ops/trait.Fn.html "trait std::ops::Fn"), [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut"), and [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce").*

Function pointers are pointers that point to *code*, not data. They can be called just like functions. Like references, function pointers are, among other things, assumed to not be null, so if you want to pass a function pointer over FFI and be able to accommodate null pointers, make your type [`Option<fn()>`](https://doc.rust-lang.org/stable/std/option/index.html#options-and-pointers-nullable-pointers "mod std::option") with your required signature.

Note that FFI requires additional care to ensure that the ABI for both sides of the call match. The exact requirements are not currently documented.

#### [§](#safety)Safety

Plain function pointers are obtained by casting either plain functions, or closures that don’t capture an environment:

```rust
fn add_one(x: usize) -> usize {
    x + 1
}

let ptr: fn(usize) -> usize = add_one;
assert_eq!(ptr(5), 6);

let clos: fn(usize) -> usize = |x| x + 5;
assert_eq!(clos(5), 10);
```

In addition to varying based on their signature, function pointers come in two flavors: safe and unsafe. Plain `fn()` function pointers can only point to safe functions, while `unsafe fn()` function pointers can point to safe or unsafe functions.

```rust
fn add_one(x: usize) -> usize {
    x + 1
}

unsafe fn add_one_unsafely(x: usize) -> usize {
    x + 1
}

let safe_ptr: fn(usize) -> usize = add_one;

//ERROR: mismatched types: expected normal fn, found unsafe fn
//let bad_ptr: fn(usize) -> usize = add_one_unsafely;

let unsafe_ptr: unsafe fn(usize) -> usize = add_one_unsafely;
let really_safe_ptr: unsafe fn(usize) -> usize = add_one;
```

#### [§](#abi)ABI

On top of that, function pointers can vary based on what ABI they use. This is achieved by adding the `extern` keyword before the type, followed by the ABI in question. The default ABI is “Rust”, i.e., `fn()` is the exact same type as `extern "Rust" fn()`. A pointer to a function with C ABI would have type `extern "C" fn()`.

`extern "ABI" { ... }` blocks declare functions with ABI “ABI”. The default here is “C”, i.e., functions declared in an `extern {...}` block have “C” ABI.

For more information and a list of supported ABIs, see [the nomicon’s section on foreign calling conventions](https://doc.rust-lang.org/stable/nomicon/ffi.html#foreign-calling-conventions).

#### [§](#variadic-functions)Variadic functions

Extern function declarations with the “C” or “cdecl” ABIs can also be *variadic*, allowing them to be called with a variable number of arguments. Normal Rust functions, even those with an `extern "ABI"`, cannot be variadic. For more information, see [the nomicon’s section on variadic functions](https://doc.rust-lang.org/stable/nomicon/ffi.html#variadic-functions).

#### [§](#creating-function-pointers)Creating function pointers

When `bar` is the name of a function, then the expression `bar` is *not* a function pointer. Rather, it denotes a value of an unnameable type that uniquely identifies the function `bar`. The value is zero-sized because the type already identifies the function. This has the advantage that “calling” the value (it implements the `Fn*` traits) does not require dynamic dispatch.

This zero-sized type *coerces* to a regular function pointer. For example:

```rust
fn bar(x: i32) {}

let not_bar_ptr = bar; // `not_bar_ptr` is zero-sized, uniquely identifying `bar`
assert_eq!(size_of_val(&not_bar_ptr), 0);

let bar_ptr: fn(i32) = not_bar_ptr; // force coercion to function pointer
assert_eq!(size_of_val(&bar_ptr), size_of::<usize>());

let footgun = &bar; // this is a shared reference to the zero-sized type identifying `bar`
```

The last line shows that `&bar` is not a function pointer either. Rather, it is a reference to the function-specific ZST. `&bar` is basically never what you want when `bar` is a function.

#### [§](#casting-to-and-from-integers)Casting to and from integers

You can cast function pointers directly to integers:

```rust
let fnptr: fn(i32) -> i32 = |x| x+2;
let fnptr_addr = fnptr as usize;
```

However, a direct cast back is not possible. You need to use `transmute`:

```rust
let fnptr = fnptr_addr as *const ();
let fnptr: fn(i32) -> i32 = unsafe { std::mem::transmute(fnptr) };
assert_eq!(fnptr(40), 42);
```

Crucially, we `as`-cast to a raw pointer before `transmute`ing to a function pointer. This avoids an integer-to-pointer `transmute`, which can be problematic. Transmuting between raw pointers and function pointers (i.e., two pointer types) is fine.

Note that all of this is not portable to platforms where function pointers and data pointers have different sizes.

#### [§](#abi-compatibility)ABI compatibility

Generally, when a function is declared with one signature and called via a function pointer with a different signature, the two signatures must be *ABI-compatible* or else calling the function via that function pointer is Undefined Behavior. ABI compatibility is a lot stricter than merely having the same memory layout; for example, even if `i32` and `f32` have the same size and alignment, they might be passed in different registers and hence not be ABI-compatible.

ABI compatibility as a concern only arises in code that alters the type of function pointers, and code that imports functions via `extern` blocks. Altering the type of function pointers is wildly unsafe (as in, a lot more unsafe than even [`transmute_copy`](https://doc.rust-lang.org/stable/std/mem/fn.transmute_copy.html "fn std::mem::transmute_copy")), and should only occur in the most exceptional circumstances. Most Rust code just imports functions via `use`. So, most likely you do not have to worry about ABI compatibility.

But assuming such circumstances, what are the rules? For this section, we are only considering the ABI of direct Rust-to-Rust calls (with both definition and callsite visible to the Rust compiler), not linking in general – once functions are imported via `extern` blocks, there are more things to consider that we do not go into here. Note that this also applies to passing/calling functions across language boundaries via function pointers.

**Nothing in this section should be taken as a guarantee for non-Rust-to-Rust calls, even with types from `core::ffi` or `libc`** .

For two signatures to be considered *ABI-compatible*, they must use a compatible ABI string, must take the same number of arguments, and the individual argument types and the return types must be ABI-compatible. The ABI string is declared via `extern "ABI" fn(...) -> ...`; note that `fn name(...) -> ...` implicitly uses the `"Rust"` ABI string and `extern fn name(...) -> ...` implicitly uses the `"C"` ABI string.

The ABI strings are guaranteed to be compatible if they are the same, or if the caller ABI string is `$X-unwind` and the callee ABI string is `$X`, where `$X` is one of the following: “C”, “aapcs”, “fastcall”, “stdcall”, “system”, “sysv64”, “thiscall”, “vectorcall”, “win64”.

The following types are guaranteed to be ABI-compatible:

- `*const T`, `*mut T`, `&T`, `&mut T`, `Box<T>` (specifically, only `Box<T, Global>`), and `NonNull<T>` are all ABI-compatible with each other for all `T`. They are also ABI-compatible with each other for *different* `T` if they have the same metadata type (`<T as Pointee>::Metadata`).
- `usize` is ABI-compatible with the `uN` integer type of the same size, and likewise `isize` is ABI-compatible with the `iN` integer type of the same size.
- `char` is ABI-compatible with `u32`.
- Any two `fn` (function pointer) types are ABI-compatible with each other if they have the same ABI string or the ABI string only differs in a trailing `-unwind`, independent of the rest of their signature. (This means you can pass `fn()` to a function expecting `fn(i32)`, and the call will be valid ABI-wise. The callee receives the result of transmuting the function pointer from `fn()` to `fn(i32)`; that transmutation is itself a well-defined operation, it’s just almost certainly UB to later call that function pointer.)
- Any two types with size 0 and alignment 1 are ABI-compatible.
- A `repr(transparent)` type `T` is ABI-compatible with its unique non-trivial field, i.e., the unique field that doesn’t have size 0 and alignment 1 (if there is such a field).
- `i32` is ABI-compatible with `NonZero<i32>`, and similar for all other integer types.
- If `T` is guaranteed to be subject to the [null pointer optimization](https://doc.rust-lang.org/stable/std/option/index.html#representation), and `E` is an enum satisfying the following requirements, then `T` and `E` are ABI-compatible. Such an enum `E` is called “option-like”.
  
  - The enum `E` uses the [`Rust` representation](https://doc.rust-lang.org/reference/type-layout.html#the-rust-representation), and is not modified by the `align` or `packed` representation modifiers.
  - The enum `E` has exactly two variants.
  - One variant has exactly one field, of type `T`.
  - All fields of the other variant are zero-sized with 1-byte alignment.

Furthermore, ABI compatibility satisfies the following general properties:

- Every type is ABI-compatible with itself.
- If `T1` and `T2` are ABI-compatible and `T2` and `T3` are ABI-compatible, then so are `T1` and `T3` (i.e., ABI-compatibility is transitive).
- If `T1` and `T2` are ABI-compatible, then so are `T2` and `T1` (i.e., ABI-compatibility is symmetric).

More signatures can be ABI-compatible on specific targets, but that should not be relied upon since it is not portable and not a stable guarantee.

Noteworthy cases of types *not* being ABI-compatible in general are:

- `bool` vs `u8`, `i32` vs `u32`, `char` vs `i32`: on some targets, the calling conventions for these types differ in terms of what they guarantee for the remaining bits in the register that are not used by the value.
- `i32` vs `f32` are not compatible either, as has already been mentioned above.
- `struct Foo(u32)` and `u32` are not compatible (without `repr(transparent)`) since structs are aggregate types and often passed in a different way than primitives like `i32`.

Note that these rules describe when two completely known types are ABI-compatible. When considering ABI compatibility of a type declared in another crate (including the standard library), consider that any type that has a private field or the `#[non_exhaustive]` attribute may change its layout as a non-breaking update unless documented otherwise – so for instance, even if such a type is a 1-ZST or `repr(transparent)` right now, this might change with any library version bump.

If the declared signature and the signature of the function pointer are ABI-compatible, then the function call behaves as if every argument was [`transmute`d](https://doc.rust-lang.org/stable/std/mem/fn.transmute.html "fn std::mem::transmute") from the type in the function pointer to the type at the function declaration, and the return value is [`transmute`d](https://doc.rust-lang.org/stable/std/mem/fn.transmute.html "fn std::mem::transmute") from the type in the declaration to the type in the pointer. All the usual caveats and concerns around transmutation apply; for instance, if the function expects a `NonZero<i32>` and the function pointer uses the ABI-compatible type `Option<NonZero<i32>>`, and the value used for the argument is `None`, then this call is Undefined Behavior since transmuting `None::<NonZero<i32>>` to `NonZero<i32>` violates the non-zero requirement.

#### [§](#trait-implementations-1)Trait implementations

In this documentation the shorthand `fn(T₁, T₂, …, Tₙ)` is used to represent non-variadic function pointers of varying length. Note that this is a convenience notation to avoid repetitive documentation, not valid Rust syntax.

The following traits are implemented for function pointers with any number of arguments and any ABI.

- [`PartialEq`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq")
- [`Eq`](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq")
- [`PartialOrd`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd")
- [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord")
- [`Hash`](https://doc.rust-lang.org/stable/std/hash/trait.Hash.html "trait std::hash::Hash")
- [`Pointer`](https://doc.rust-lang.org/stable/std/fmt/trait.Pointer.html "trait std::fmt::Pointer")
- [`Debug`](https://doc.rust-lang.org/stable/std/fmt/derive.Debug.html "derive std::fmt::Debug")
- [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone")
- [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy")
- [`Send`](https://doc.rust-lang.org/stable/std/marker/trait.Send.html "trait std::marker::Send")
- [`Sync`](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync")
- [`Unpin`](https://doc.rust-lang.org/stable/std/marker/trait.Unpin.html "trait std::marker::Unpin")
- [`UnwindSafe`](https://doc.rust-lang.org/stable/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe")
- [`RefUnwindSafe`](https://doc.rust-lang.org/stable/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe")

Note that while this type implements `PartialEq`, comparing function pointers is unreliable: pointers to the same function can compare inequal (because functions are duplicated in multiple codegen units), and pointers to *different* functions can compare equal (since identical functions can be deduplicated within a codegen unit).

In addition, all *safe* function pointers implement [`Fn`](https://doc.rust-lang.org/stable/std/ops/trait.Fn.html "trait std::ops::Fn"), [`FnMut`](https://doc.rust-lang.org/stable/std/ops/trait.FnMut.html "trait std::ops::FnMut"), and [`FnOnce`](https://doc.rust-lang.org/stable/std/ops/trait.FnOnce.html "trait std::ops::FnOnce"), because these traits are specially known to the compiler.

[§](#impl-Freeze-for-fn%28T%29+-%3E+Ret)

[§](#impl-RefUnwindSafe-for-fn%28T%29+-%3E+Ret)

[§](#impl-Send-for-fn%28T%29+-%3E+Ret)

[§](#impl-Sync-for-fn%28T%29+-%3E+Ret)

[§](#impl-Unpin-for-fn%28T%29+-%3E+Ret)

[§](#impl-UnsafeUnpin-for-fn%28T%29+-%3E+Ret)

[§](#impl-UnwindSafe-for-fn%28T%29+-%3E+Ret)

[Source](https://doc.rust-lang.org/stable/src/core/any.rs.html#141)[§](#impl-Any-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#212)[§](#impl-Borrow%3CT%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#221)[§](#impl-BorrowMut%3CT%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#547)[§](#impl-CloneToUninit-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#549)[§](#method.clone_to_uninit)

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/stable/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2587)[§](#impl-Debug-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#785)[§](#impl-From%3CT%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#788)[§](#method.from)

Returns the argument unchanged.

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2573)[§](#impl-Hash-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#767-769)[§](#impl-Into%3CU%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#777)[§](#method.into)

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of `From<T> for U` chooses to do.

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2565)[§](#impl-Ord-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2536)[§](#impl-PartialEq-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2538)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2554)[§](#impl-PartialOrd-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2556)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#941-943)[§](#impl-Pattern-for-F)

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#associatedtype.Searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.into_searcher)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.is_contained_in)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.is_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.strip_prefix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.is_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#945)[§](#method.strip_suffix_of)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/stable/src/core/str/pattern.rs.html#165)[§](#method.as_utf8_pattern)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2580)[§](#impl-Pointer-for-F)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#72-74)[§](#impl-ToOwned-for-T)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#76)[§](#associatedtype.Owned)

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#77)[§](#method.to_owned)

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/stable/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/stable/src/alloc/borrow.rs.html#81)[§](#method.clone_into)

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/stable/std/borrow/trait.ToOwned.html#method.clone_into)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#827-829)[§](#impl-TryFrom%3CU%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#831)[§](#associatedtype.Error-1)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#834)[§](#method.try_from)

Performs the conversion.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#811-813)[§](#impl-TryInto%3CU%3E-for-T)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#815)[§](#associatedtype.Error)

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#818)[§](#method.try_into)

Performs the conversion.

[Source](https://doc.rust-lang.org/stable/src/core/ptr/mod.rs.html#2547)[§](#impl-Eq-for-F)