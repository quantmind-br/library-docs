---
title: TypeId in std::any - Rust
url: https://doc.rust-lang.org/std/any/struct.TypeId.html
source: crawler
fetched_at: 2026-05-06T21:24:05.592907923-03:00
rendered_js: false
word_count: 813
summary: This document describes TypeId, a mechanism for obtaining globally unique identifiers for types in Rust, including warnings regarding type variance and stability.
tags:
    - rust
    - type-system
    - runtime-reflection
    - type-safety
    - variance
category: reference
---

## Struct TypeId

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#724)

```rust
pub struct TypeId { /* private fields */ }
```

Expand description

A `TypeId` represents a globally unique identifier for a type.

Each `TypeId` is an opaque object which does not allow inspection of what’s inside but does allow basic operations such as cloning, comparison, printing, and showing.

A `TypeId` is currently only available for types which ascribe to `'static`, but this limitation may be removed in the future.

While `TypeId` implements `Hash`, `PartialOrd`, and `Ord`, it is worth noting that the hashes and ordering will vary between Rust releases. Beware of relying on them inside of your code!

## [§](#layout-1)Layout

Like other [`Rust`-representation](https://doc.rust-lang.org/reference/type-layout.html#r-layout.repr.rust.unspecified) types, `TypeId`’s size and layout are unstable. In particular, this means that you cannot rely on the size and layout of `TypeId` remaining the same between Rust releases; they are subject to change without prior notice between Rust releases.

## [§](#danger-of-improper-variance)Danger of Improper Variance

You might think that subtyping is impossible between two static types, but this is false; there exists a static type with a static subtype. To wit, `fn(&str)`, which is short for `for<'any> fn(&'any str)`, and `fn(&'static str)`, are two distinct, static types, and yet, `fn(&str)` is a subtype of `fn(&'static str)`, since any value of type `fn(&str)` can be used where a value of type `fn(&'static str)` is needed.

This means that abstractions around `TypeId`, despite its `'static` bound on arguments, still need to worry about unnecessary and improper variance: it is advisable to strive for invariance first. The usability impact will be negligible, while the reduction in the risk of unsoundness will be most welcome.

### [§](#examples)Examples

Suppose `SubType` is a subtype of `SuperType`, that is, a value of type `SubType` can be used wherever a value of type `SuperType` is expected. Suppose also that `CoVar<T>` is a generic type, which is covariant over `T` (like many other types, including `PhantomData<T>` and `Vec<T>`).

Then, by covariance, `CoVar<SubType>` is a subtype of `CoVar<SuperType>`, that is, a value of type `CoVar<SubType>` can be used wherever a value of type `CoVar<SuperType>` is expected.

Then if `CoVar<SuperType>` relies on `TypeId::of::<SuperType>()` to uphold any invariants, those invariants may be broken because a value of type `CoVar<SuperType>` can be created without going through any of its methods, like so:

```rust
type SubType = fn(&());
type SuperType = fn(&'static ());
type CoVar<T> = Vec<T>; // imagine something more complicated

let sub: CoVar<SubType> = CoVar::new();
// we have a `CoVar<SuperType>` instance without
// *ever* having called `CoVar::<SuperType>::new()`!
let fake_super: CoVar<SuperType> = sub;
```

The following is an example program that tries to use `TypeId::of` to implement a generic type `Unique<T>` that guarantees unique instances for each `Unique<T>`, that is, and for each type `T` there can be at most one value of type `Unique<T>` at any time.

```rust
mod unique {
    use std::any::TypeId;
    use std::collections::BTreeSet;
    use std::marker::PhantomData;
    use std::sync::Mutex;

    static ID_SET: Mutex<BTreeSet<TypeId>> = Mutex::new(BTreeSet::new());

    // TypeId has only covariant uses, which makes Unique covariant over TypeAsId 🚨
    #[derive(Debug, PartialEq)]
    pub struct Unique<TypeAsId: 'static>(
        // private field prevents creation without `new` outside this module
        PhantomData<TypeAsId>,
    );

    impl<TypeAsId: 'static> Unique<TypeAsId> {
        pub fn new() -> Option<Self> {
            let mut set = ID_SET.lock().unwrap();
            (set.insert(TypeId::of::<TypeAsId>())).then(|| Self(PhantomData))
        }
    }

    impl<TypeAsId: 'static> Drop for Unique<TypeAsId> {
        fn drop(&mut self) {
            let mut set = ID_SET.lock().unwrap();
            (!set.remove(&TypeId::of::<TypeAsId>())).then(|| panic!("duplicity detected"));
        }
    }
}

use unique::Unique;

// `OtherRing` is a subtype of `TheOneRing`. Both are 'static, and thus have a TypeId.
type TheOneRing = fn(&'static ());
type OtherRing = fn(&());

fn main() {
    let the_one_ring: Unique<TheOneRing> = Unique::new().unwrap();
    assert_eq!(Unique::<TheOneRing>::new(), None);

    let other_ring: Unique<OtherRing> = Unique::new().unwrap();
    // Use that `Unique<OtherRing>` is a subtype of `Unique<TheOneRing>` 🚨
    let fake_one_ring: Unique<TheOneRing> = other_ring;
    assert_eq!(fake_one_ring, the_one_ring);

    std::mem::forget(fake_one_ring);
}
```

[Source](https://doc.rust-lang.org/src/core/mem/type_info.rs.html#36)[§](#impl-TypeId)

[Source](https://doc.rust-lang.org/src/core/mem/type_info.rs.html#41)

🔬This is a nightly-only experimental API. (`type_info` [#146922](https://github.com/rust-lang/rust/issues/146922))

Compute the type information of a concrete type. It can only be called at compile time.

[Source](https://doc.rust-lang.org/src/core/any.rs.html#772)[§](#impl-TypeId-1)

1.0.0 (const: 1.91.0) · [Source](https://doc.rust-lang.org/src/core/any.rs.html#790)

Returns the `TypeId` of the generic type parameter.

##### [§](#examples-1)Examples

```rust
use std::any::{Any, TypeId};

fn is_string<T: ?Sized + Any>(_s: &T) -> bool {
    TypeId::of::<String>() == TypeId::of::<T>()
}

assert_eq!(is_string(&0), false);
assert_eq!(is_string(&"cookie monster".to_string()), true);
```

[Source](https://doc.rust-lang.org/src/core/any.rs.html#811-815)

🔬This is a nightly-only experimental API. (`type_info` [#146922](https://github.com/rust-lang/rust/issues/146922))

Checks if the [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId") implements the trait. If it does it returns [TraitImpl](https://doc.rust-lang.org/std/mem/type_info/struct.TraitImpl.html "struct std::mem::type_info::TraitImpl") which can be used to build a fat pointer. It can only be called at compile time. `self` must be the [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId") of a sized type or None will be returned.

##### [§](#examples-2)Examples

```rust
#![feature(type_info)]
use std::any::{TypeId};

pub trait Blah {}
impl Blah for u8 {}

assert!(const { TypeId::of::<u8>().trait_info_of::<dyn Blah>() }.is_some());
assert!(const { TypeId::of::<u16>().trait_info_of::<dyn Blah>() }.is_none());
```

[Source](https://doc.rust-lang.org/src/core/any.rs.html#838-841)

🔬This is a nightly-only experimental API. (`type_info` [#146922](https://github.com/rust-lang/rust/issues/146922))

Checks if the [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId") implements the trait of `trait_represented_by_type_id`. If it does it returns [TraitImpl](https://doc.rust-lang.org/std/mem/type_info/struct.TraitImpl.html "struct std::mem::type_info::TraitImpl") which can be used to build a fat pointer. It can only be called at compile time. `self` must be the [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId") of a sized type or None will be returned.

##### [§](#examples-3)Examples

```rust
#![feature(type_info)]
use std::any::{TypeId};

pub trait Blah {}
impl Blah for u8 {}

assert!(const { TypeId::of::<u8>().trait_info_of_trait_type_id(TypeId::of::<dyn Blah>()) }.is_some());
assert!(const { TypeId::of::<u16>().trait_info_of_trait_type_id(TypeId::of::<dyn Blah>()) }.is_none());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/any.rs.html#721)[§](#impl-Clone-for-TypeId)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#894)[§](#impl-Debug-for-TypeId)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#869)[§](#impl-Hash-for-TypeId)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#720)[§](#impl-Ord-for-TypeId)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/any.rs.html#742)[§](#impl-PartialEq-for-TypeId)

[Source](https://doc.rust-lang.org/src/core/any.rs.html#744)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#720)[§](#impl-PartialOrd-for-TypeId)

[Source](https://doc.rust-lang.org/src/core/any.rs.html#720)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#720)[§](#impl-Copy-for-TypeId)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/src/core/any.rs.html#721)[§](#impl-Eq-for-TypeId)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#735)[§](#impl-Send-for-TypeId)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/any.rs.html#738)[§](#impl-Sync-for-TypeId)

[§](#impl-Freeze-for-TypeId)

[§](#impl-RefUnwindSafe-for-TypeId)

[§](#impl-Unpin-for-TypeId)

[§](#impl-UnsafeUnpin-for-TypeId)

[§](#impl-UnwindSafe-for-TypeId)