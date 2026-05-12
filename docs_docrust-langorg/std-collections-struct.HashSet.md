---
title: HashSet in std::collections - Rust
url: https://doc.rust-lang.org/std/collections/struct.HashSet.html
source: crawler
fetched_at: 2026-05-06T21:24:49.489665246-03:00
rendered_js: false
word_count: 2582
summary: This document describes the Rust HashSet collection, explaining its requirements for hashable and equatable elements, usage guidelines, and initialization methods.
tags:
    - rust
    - hashset
    - collections
    - data-structures
    - hashing
    - memory-management
category: reference
---

## Struct HashSet

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#126-132)

```rust
pub struct HashSet<T, S = RandomState, A: Allocator = Global> { /* private fields */ }
```

Expand description

A [hash set](https://doc.rust-lang.org/std/collections/index.html#use-the-set-variant-of-any-of-these-maps-when "mod std::collections") implemented as a `HashMap` where the value is `()`.

As with the [`HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html "struct std::collections::HashMap") type, a `HashSet` requires that the elements implement the [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") and [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") traits. This can frequently be achieved by using `#[derive(PartialEq, Eq, Hash)]`. If you implement these yourself, it is important that the following property holds:

```text
k1 == k2 -> hash(k1) == hash(k2)
```

In other words, if two keys are equal, their hashes must be equal. Violating this property is a logic error.

It is also a logic error for a key to be modified in such a way that the key’s hash, as determined by the [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") trait, or its equality, as determined by the [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") trait, changes while it is in the map. This is normally only possible through [`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell"), [`RefCell`](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell"), global state, I/O, or unsafe code.

The behavior resulting from either logic error is not specified, but will be encapsulated to the `HashSet` that observed the logic error and not result in undefined behavior. This could include panics, incorrect results, aborts, memory leaks, and non-termination.

## [§](#examples)Examples

```rust
use std::collections::HashSet;
// Type inference lets us omit an explicit type signature (which
// would be `HashSet<String>` in this example).
let mut books = HashSet::new();

// Add some books.
books.insert("A Dance With Dragons".to_string());
books.insert("To Kill a Mockingbird".to_string());
books.insert("The Odyssey".to_string());
books.insert("The Great Gatsby".to_string());

// Check for a specific one.
if !books.contains("The Winds of Winter") {
    println!("We have {} books, but The Winds of Winter ain't one.",
             books.len());
}

// Remove a book.
books.remove("The Odyssey");

// Iterate over everything.
for book in &books {
    println!("{book}");
}
```

The easiest way to use `HashSet` with a custom type is to derive [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") and [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash"). We must also derive [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"), which is required if [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") is derived.

```rust
use std::collections::HashSet;
#[derive(Hash, Eq, PartialEq, Debug)]
struct Viking {
    name: String,
    power: usize,
}

let mut vikings = HashSet::new();

vikings.insert(Viking { name: "Einar".to_string(), power: 9 });
vikings.insert(Viking { name: "Einar".to_string(), power: 9 });
vikings.insert(Viking { name: "Olaf".to_string(), power: 4 });
vikings.insert(Viking { name: "Harald".to_string(), power: 8 });

// Use derived implementation to print the vikings.
for x in &vikings {
    println!("{x:?}");
}
```

A `HashSet` with a known list of items can be initialized from an array:

```rust
use std::collections::HashSet;

let viking_names = HashSet::from(["Einar", "Olaf", "Harald"]);
```

## [§](#usage-in-const-and-static)Usage in `const` and `static`

Like `HashMap`, `HashSet` is randomly seeded: each `HashSet` instance uses a different seed, which means that `HashSet::new` cannot be used in const context. To construct a `HashSet` in the initializer of a `const` or `static` item, you will have to use a different hasher that does not involve a random seed, as demonstrated in the following example. **A `HashSet` constructed this way is not resistant against HashDoS!**

```rust
use std::collections::HashSet;
use std::hash::{BuildHasherDefault, DefaultHasher};
use std::sync::Mutex;

const EMPTY_SET: HashSet<String, BuildHasherDefault<DefaultHasher>> =
    HashSet::with_hasher(BuildHasherDefault::new());
static SET: Mutex<HashSet<String, BuildHasherDefault<DefaultHasher>>> =
    Mutex::new(HashSet::with_hasher(BuildHasherDefault::new()));
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#134-172)[§](#impl-HashSet%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#149-151)

Creates an empty `HashSet`.

The hash set is initially created with a capacity of 0, so it will not allocate until it is first inserted into.

##### [§](#examples-1)Examples

```rust
use std::collections::HashSet;
let set: HashSet<i32> = HashSet::new();
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#169-171)

Creates an empty `HashSet` with at least the specified capacity.

The hash set will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the hash set will not allocate.

##### [§](#examples-2)Examples

```rust
use std::collections::HashSet;
let set: HashSet<i32> = HashSet::with_capacity(10);
assert!(set.capacity() >= 10);
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#174-205)[§](#impl-HashSet%3CT,+RandomState,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#182-184)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates an empty `HashSet` in the provided allocator.

The hash set is initially created with a capacity of 0, so it will not allocate until it is first inserted into.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#202-204)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates an empty `HashSet` with at least the specified capacity.

The hash set will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the hash set will not allocate.

##### [§](#examples-3)Examples

```rust
use std::collections::HashSet;
let set: HashSet<i32> = HashSet::with_capacity(10);
assert!(set.capacity() >= 10);
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#207-268)[§](#impl-HashSet%3CT,+S%3E)

1.7.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#234-236)

Creates a new empty hash set which will use the given hasher to hash keys.

The hash set is also created with the default initial capacity.

Warning: `hasher` is normally randomly generated, and is designed to allow `HashSet`s to be resistant to attacks that cause many collisions and very poor performance. Setting it manually using this function can expose a DoS attack vector.

The `hash_builder` passed should implement the [`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html "trait std::hash::BuildHasher") trait for the `HashSet` to be useful, see its documentation for details.

##### [§](#examples-4)Examples

```rust
use std::collections::HashSet;
use std::hash::RandomState;

let s = RandomState::new();
let mut set = HashSet::with_hasher(s);
set.insert(2);
```

1.7.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#265-267)

Creates an empty `HashSet` with at least the specified capacity, using `hasher` to hash the keys.

The hash set will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the hash set will not allocate.

Warning: `hasher` is normally randomly generated, and is designed to allow `HashSet`s to be resistant to attacks that cause many collisions and very poor performance. Setting it manually using this function can expose a DoS attack vector.

The `hash_builder` passed should implement the [`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html "trait std::hash::BuildHasher") trait for the `HashSet` to be useful, see its documentation for details.

##### [§](#examples-5)Examples

```rust
use std::collections::HashSet;
use std::hash::RandomState;

let s = RandomState::new();
let mut set = HashSet::with_capacity_and_hasher(10, s);
set.insert(1);
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#270-521)[§](#impl-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#285-287)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates a new empty hash set which will use the given hasher to hash keys and will allocate memory using the provided allocator.

The hash set is also created with the default initial capacity.

Warning: `hasher` is normally randomly generated, and is designed to allow `HashSet`s to be resistant to attacks that cause many collisions and very poor performance. Setting it manually using this function can expose a DoS attack vector.

The `hash_builder` passed should implement the [`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html "trait std::hash::BuildHasher") trait for the `HashSet` to be useful, see its documentation for details.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#305-307)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates an empty `HashSet` with at least the specified capacity, using `hasher` to hash the keys and `alloc` to allocate memory.

The hash set will be able to hold at least `capacity` elements without reallocating. This method is allowed to allocate for more elements than `capacity`. If `capacity` is zero, the hash set will not allocate.

Warning: `hasher` is normally randomly generated, and is designed to allow `HashSet`s to be resistant to attacks that cause many collisions and very poor performance. Setting it manually using this function can expose a DoS attack vector.

The `hash_builder` passed should implement the [`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html "trait std::hash::BuildHasher") trait for the `HashSet` to be useful, see its documentation for details.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#320-322)

Returns the number of elements the set can hold without reallocating.

##### [§](#examples-6)Examples

```rust
use std::collections::HashSet;
let set: HashSet<i32> = HashSet::with_capacity(100);
assert!(set.capacity() >= 100);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#349-351)

An iterator visiting all elements in arbitrary order. The iterator element type is `&'a T`.

##### [§](#examples-7)Examples

```rust
use std::collections::HashSet;
let mut set = HashSet::new();
set.insert("a");
set.insert("b");

// Will print in an arbitrary order.
for x in set.iter() {
    println!("{x}");
}
```

##### [§](#performance)Performance

In the current implementation, iterating over set takes O(capacity) time instead of O(len) because it internally visits empty buckets too.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#367-369)

Returns the number of elements in the set.

##### [§](#examples-8)Examples

```rust
use std::collections::HashSet;

let mut v = HashSet::new();
assert_eq!(v.len(), 0);
v.insert(1);
assert_eq!(v.len(), 1);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#385-387)

Returns `true` if the set contains no elements.

##### [§](#examples-9)Examples

```rust
use std::collections::HashSet;

let mut v = HashSet::new();
assert!(v.is_empty());
v.insert(1);
assert!(!v.is_empty());
```

1.6.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#414-416)

Clears the set, returning all elements as an iterator. Keeps the allocated memory for reuse.

If the returned iterator is dropped before being fully consumed, it drops the remaining elements. The returned iterator keeps a mutable borrow on the set to optimize its implementation.

##### [§](#examples-10)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::from([1, 2, 3]);
assert!(!set.is_empty());

// print 1, 2, 3 in an arbitrary order
for i in set.drain() {
    println!("{i}");
}

assert!(set.is_empty());
```

Creates an iterator which uses a closure to determine if an element should be removed.

If the closure returns `true`, the element is removed from the set and yielded. If the closure returns `false`, or panics, the element remains in the set and will not be yielded.

If the returned `ExtractIf` is not exhausted, e.g. because it is dropped without iterating or the iteration short-circuits, then the remaining elements will be retained. Use [`retain`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.retain "method std::collections::HashSet::retain") with a negated predicate if you do not need the returned iterator.

##### [§](#examples-11)Examples

Splitting a set into even and odd values, reusing the original set:

```rust
use std::collections::HashSet;

let mut set: HashSet<i32> = (0..8).collect();
let extracted: HashSet<i32> = set.extract_if(|v| v % 2 == 0).collect();

let mut evens = extracted.into_iter().collect::<Vec<_>>();
let mut odds = set.into_iter().collect::<Vec<_>>();
evens.sort();
odds.sort();

assert_eq!(evens, vec![0, 2, 4, 6]);
assert_eq!(odds, vec![1, 3, 5, 7]);
```

1.18.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#479-484)

Retains only the elements specified by the predicate.

In other words, remove all elements `e` for which `f(&e)` returns `false`. The elements are visited in unsorted (and unspecified) order.

##### [§](#examples-12)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::from([1, 2, 3, 4, 5, 6]);
set.retain(|&k| k % 2 == 0);
assert_eq!(set, HashSet::from([2, 4, 6]));
```

##### [§](#performance-1)Performance

In the current implementation, this operation takes O(capacity) time instead of O(len) because it internally visits empty buckets too.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#500-502)

Clears the set, removing all values.

##### [§](#examples-13)Examples

```rust
use std::collections::HashSet;

let mut v = HashSet::new();
v.insert(1);
v.clear();
assert!(v.is_empty());
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#518-520)

Returns a reference to the set’s [`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html "trait std::hash::BuildHasher").

##### [§](#examples-14)Examples

```rust
use std::collections::HashSet;
use std::hash::RandomState;

let hasher = RandomState::new();
let set: HashSet<i32> = HashSet::with_hasher(hasher);
let hasher: &RandomState = set.hasher();
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#523-1074)[§](#impl-HashSet%3CT,+S,+A%3E-1)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#549-551)

Reserves capacity for at least `additional` more elements to be inserted in the `HashSet`. The collection may reserve more space to speculatively avoid frequent reallocations. After calling `reserve`, capacity will be greater than or equal to `self.len() + additional`. Does nothing if capacity is already sufficient.

##### [§](#panics)Panics

Panics if the new allocation size overflows `usize`.

##### [§](#examples-15)Examples

```rust
use std::collections::HashSet;
let mut set: HashSet<i32> = HashSet::new();
set.reserve(10);
assert!(set.capacity() >= 10);
```

1.57.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#574-576)

Tries to reserve capacity for at least `additional` more elements to be inserted in the `HashSet`. The collection may reserve more space to speculatively avoid frequent reallocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient.

##### [§](#errors)Errors

If the capacity overflows, or the allocator reports a failure, then an error is returned.

##### [§](#examples-16)Examples

```rust
use std::collections::HashSet;
let mut set: HashSet<i32> = HashSet::new();
set.try_reserve(10).expect("why is the test harness OOMing on a handful of bytes?");
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#596-598)

Shrinks the capacity of the set as much as possible. It will drop down as much as possible while maintaining the internal rules and possibly leaving some space in accordance with the resize policy.

##### [§](#examples-17)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::with_capacity(100);
set.insert(1);
set.insert(2);
assert!(set.capacity() >= 100);
set.shrink_to_fit();
assert!(set.capacity() >= 2);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#621-623)

Shrinks the capacity of the set with a lower limit. It will drop down no lower than the supplied limit while maintaining the internal rules and possibly leaving some space in accordance with the resize policy.

If the current capacity is less than the lower limit, this is a no-op.

##### [§](#examples-18)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::with_capacity(100);
set.insert(1);
set.insert(2);
assert!(set.capacity() >= 100);
set.shrink_to(10);
assert!(set.capacity() >= 10);
set.shrink_to(0);
assert!(set.capacity() >= 2);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#651-653)

Visits the values representing the difference, i.e., the values that are in `self` but not in `other`.

##### [§](#examples-19)Examples

```rust
use std::collections::HashSet;
let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([4, 2, 3, 4]);

// Can be seen as `a - b`.
for x in a.difference(&b) {
    println!("{x}"); // Print 1
}

let diff: HashSet<_> = a.difference(&b).collect();
assert_eq!(diff, [1].iter().collect());

// Note that difference is not symmetric,
// and `b - a` means something else:
let diff: HashSet<_> = b.difference(&a).collect();
assert_eq!(diff, [4].iter().collect());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#679-684)

Visits the values representing the symmetric difference, i.e., the values that are in `self` or in `other` but not in both.

##### [§](#examples-20)Examples

```rust
use std::collections::HashSet;
let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([4, 2, 3, 4]);

// Print 1, 4 in arbitrary order.
for x in a.symmetric_difference(&b) {
    println!("{x}");
}

let diff1: HashSet<_> = a.symmetric_difference(&b).collect();
let diff2: HashSet<_> = b.symmetric_difference(&a).collect();

assert_eq!(diff1, diff2);
assert_eq!(diff1, [1, 4].iter().collect());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#713-719)

Visits the values representing the intersection, i.e., the values that are both in `self` and `other`.

When an equal element is present in `self` and `other` then the resulting `Intersection` may yield references to one or the other. This can be relevant if `T` contains fields which are not compared by its `Eq` implementation, and may hold different value between the two equal copies of `T` in the two sets.

##### [§](#examples-21)Examples

```rust
use std::collections::HashSet;
let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([4, 2, 3, 4]);

// Print 2, 3 in arbitrary order.
for x in a.intersection(&b) {
    println!("{x}");
}

let intersection: HashSet<_> = a.intersection(&b).collect();
assert_eq!(intersection, [2, 3].iter().collect());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#742-748)

Visits the values representing the union, i.e., all the values in `self` or `other`, without duplicates.

##### [§](#examples-22)Examples

```rust
use std::collections::HashSet;
let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([4, 2, 3, 4]);

// Print 1, 2, 3, 4 in arbitrary order.
for x in a.union(&b) {
    println!("{x}");
}

let union: HashSet<_> = a.union(&b).collect();
assert_eq!(union, [1, 2, 3, 4].iter().collect());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#767-773)

Returns `true` if the set contains a value.

The value may be any borrowed form of the set’s value type, but [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") on the borrowed form *must* match those for the value type.

##### [§](#examples-23)Examples

```rust
use std::collections::HashSet;

let set = HashSet::from([1, 2, 3]);
assert_eq!(set.contains(&1), true);
assert_eq!(set.contains(&4), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#792-798)

Returns a reference to the value in the set, if any, that is equal to the given value.

The value may be any borrowed form of the set’s value type, but [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") on the borrowed form *must* match those for the value type.

##### [§](#examples-24)Examples

```rust
use std::collections::HashSet;

let set = HashSet::from([1, 2, 3]);
assert_eq!(set.get(&2), Some(&2));
assert_eq!(set.get(&4), None);
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#818-822)

🔬This is a nightly-only experimental API. (`hash_set_entry` [#60896](https://github.com/rust-lang/rust/issues/60896))

Inserts the given `value` into the set if it is not present, then returns a reference to the value in the set.

##### [§](#examples-25)Examples

```rust
#![feature(hash_set_entry)]

use std::collections::HashSet;

let mut set = HashSet::from([1, 2, 3]);
assert_eq!(set.len(), 3);
assert_eq!(set.get_or_insert(2), &2);
assert_eq!(set.get_or_insert(100), &100);
assert_eq!(set.len(), 4); // 100 was inserted
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#846-855)

🔬This is a nightly-only experimental API. (`hash_set_entry` [#60896](https://github.com/rust-lang/rust/issues/60896))

Inserts a value computed from `f` into the set if the given `value` is not present, then returns a reference to the value in the set.

##### [§](#examples-26)Examples

```rust
#![feature(hash_set_entry)]

use std::collections::HashSet;

let mut set: HashSet<String> = ["cat", "dog", "horse"]
    .iter().map(|&pet| pet.to_owned()).collect();

assert_eq!(set.len(), 3);
for &pet in &["cat", "dog", "fish"] {
    let value = set.get_or_insert_with(pet, str::to_owned);
    assert_eq!(value, pet);
}
assert_eq!(set.len(), 4); // a new "fish" was inserted
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#894-896)

🔬This is a nightly-only experimental API. (`hash_set_entry` [#60896](https://github.com/rust-lang/rust/issues/60896))

Gets the given value’s corresponding entry in the set for in-place manipulation.

##### [§](#examples-27)Examples

```rust
#![feature(hash_set_entry)]

use std::collections::HashSet;
use std::collections::hash_set::Entry::*;

let mut singles = HashSet::new();
let mut dupes = HashSet::new();

for ch in "a short treatise on fungi".chars() {
    if let Vacant(dupe_entry) = dupes.entry(ch) {
        // We haven't already seen a duplicate, so
        // check if we've at least seen it once.
        match singles.entry(ch) {
            Vacant(single_entry) => {
                // We found a new character for the first time.
                single_entry.insert()
            }
            Occupied(single_entry) => {
                // We've already seen this once, "move" it to dupes.
                single_entry.remove();
                dupe_entry.insert();
            }
        }
    }
}

assert!(!singles.contains(&'t') && dupes.contains(&'t'));
assert!(singles.contains(&'u') && !dupes.contains(&'u'));
assert!(!singles.contains(&'v') && !dupes.contains(&'v'));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#916-922)

Returns `true` if `self` has no elements in common with `other`. This is equivalent to checking for an empty intersection.

##### [§](#examples-28)Examples

```rust
use std::collections::HashSet;

let a = HashSet::from([1, 2, 3]);
let mut b = HashSet::new();

assert_eq!(a.is_disjoint(&b), true);
b.insert(4);
assert_eq!(a.is_disjoint(&b), true);
b.insert(1);
assert_eq!(a.is_disjoint(&b), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#942-944)

Returns `true` if the set is a subset of another, i.e., `other` contains at least all the values in `self`.

##### [§](#examples-29)Examples

```rust
use std::collections::HashSet;

let sup = HashSet::from([1, 2, 3]);
let mut set = HashSet::new();

assert_eq!(set.is_subset(&sup), true);
set.insert(2);
assert_eq!(set.is_subset(&sup), true);
set.insert(4);
assert_eq!(set.is_subset(&sup), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#968-970)

Returns `true` if the set is a superset of another, i.e., `self` contains at least all the values in `other`.

##### [§](#examples-30)Examples

```rust
use std::collections::HashSet;

let sub = HashSet::from([1, 2]);
let mut set = HashSet::new();

assert_eq!(set.is_superset(&sub), false);

set.insert(0);
set.insert(1);
assert_eq!(set.is_superset(&sub), false);

set.insert(2);
assert_eq!(set.is_superset(&sub), true);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#995-997)

Adds a value to the set.

Returns whether the value was newly inserted. That is:

- If the set did not previously contain this value, `true` is returned.
- If the set already contained this value, `false` is returned, and the set is not modified: original value is not replaced, and the value passed as argument is dropped.

##### [§](#examples-31)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::new();

assert_eq!(set.insert(2), true);
assert_eq!(set.insert(2), false);
assert_eq!(set.len(), 1);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1017-1019)

Adds a value to the set, replacing the existing value, if any, that is equal to the given one. Returns the replaced value.

##### [§](#examples-32)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::new();
set.insert(Vec::<i32>::new());

assert_eq!(set.get(&[][..]).unwrap().capacity(), 0);
set.replace(Vec::with_capacity(10));
assert_eq!(set.get(&[][..]).unwrap().capacity(), 10);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1042-1048)

Removes a value from the set. Returns whether the value was present in the set.

The value may be any borrowed form of the set’s value type, but [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") on the borrowed form *must* match those for the value type.

##### [§](#examples-33)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::new();

set.insert(2);
assert_eq!(set.remove(&2), true);
assert_eq!(set.remove(&2), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1067-1073)

Removes and returns the value in the set, if any, that is equal to the given one.

The value may be any borrowed form of the set’s value type, but [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash") and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") on the borrowed form *must* match those for the value type.

##### [§](#examples-34)Examples

```rust
use std::collections::HashSet;

let mut set = HashSet::from([1, 2, 3]);
assert_eq!(set.take(&2), Some(2));
assert_eq!(set.take(&2), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1285-1315)[§](#impl-BitAnd%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1312-1314)[§](#method.bitand)

Returns the intersection of `self` and `rhs` as a new `HashSet<T, S>`.

##### [§](#examples-37)Examples

```rust
use std::collections::HashSet;

let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([2, 3, 4]);

let set = &a & &b;

let mut i = 0;
let expected = [2, 3];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1290)[§](#associatedtype.Output-1)

The resulting type after applying the `&` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1252-1282)[§](#impl-BitOr%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1279-1281)[§](#method.bitor)

Returns the union of `self` and `rhs` as a new `HashSet<T, S>`.

##### [§](#examples-36)Examples

```rust
use std::collections::HashSet;

let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([3, 4, 5]);

let set = &a | &b;

let mut i = 0;
let expected = [1, 2, 3, 4, 5];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1257)[§](#associatedtype.Output)

The resulting type after applying the `|` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1318-1348)[§](#impl-BitXor%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1345-1347)[§](#method.bitxor)

Returns the symmetric difference of `self` and `rhs` as a new `HashSet<T, S>`.

##### [§](#examples-38)Examples

```rust
use std::collections::HashSet;

let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([3, 4, 5]);

let set = &a ^ &b;

let mut i = 0;
let expected = [1, 2, 4, 5];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1323)[§](#associatedtype.Output-2)

The resulting type after applying the `^` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1085-1104)[§](#impl-Clone-for-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1101-1103)[§](#method.clone_from)

Overwrites the contents of `self` with a clone of the contents of `source`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1092-1094)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1132-1140)[§](#impl-Debug-for-HashSet%3CT,+S,+A%3E)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1240-1249)[§](#impl-Default-for-HashSet%3CT,+S%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1246-1248)[§](#method.default)

Creates an empty `HashSet<T, S>` with the `Default` value for the hasher.

1.4.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1216-1236)[§](#impl-Extend%3C%26T%3E-for-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1223-1225)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1228-1230)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1233-1235)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1193-1213)[§](#impl-Extend%3CT%3E-for-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1200-1202)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1205-1207)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1210-1212)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1169-1190)[§](#impl-From%3C%5BT;+N%5D%3E-for-HashSet%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1187-1189)[§](#method.from)

Converts a `[T; N]` into a `HashSet<T>`.

If the array contains any equal values, all but one will be dropped.

##### [§](#examples-35)Examples

```rust
use std::collections::HashSet;

let set1 = HashSet::from([1, 2, 3, 4]);
let set2: HashSet<_> = [1, 2, 3, 4].into();
assert_eq!(set1, set2);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1143-1154)[§](#impl-FromIterator%3CT%3E-for-HashSet%3CT,+S%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1621-1630)[§](#impl-IntoIterator-for-%26HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1622)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1623)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1627-1629)[§](#method.into_iter)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1633-1662)[§](#impl-IntoIterator-for-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1659-1661)[§](#method.into_iter-1)

Creates a consuming iterator, that is, one that moves each value out of the set in arbitrary order. The set cannot be used after calling this.

##### [§](#examples-40)Examples

```rust
use std::collections::HashSet;
let mut set = HashSet::new();
set.insert("a".to_string());
set.insert("b".to_string());

// Not possible to collect to a Vec<String> with a regular `.iter()`.
let v: Vec<String> = set.into_iter().collect();

// Will print in an arbitrary order.
for x in &v {
    println!("{x}");
}
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1634)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1635)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1107-1120)[§](#impl-PartialEq-for-HashSet%3CT,+S,+A%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1113-1119)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1351-1381)[§](#impl-Sub%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E)

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1378-1380)[§](#method.sub)

Returns the difference of `self` and `rhs` as a new `HashSet<T, S>`.

##### [§](#examples-39)Examples

```rust
use std::collections::HashSet;

let a = HashSet::from([1, 2, 3]);
let b = HashSet::from([3, 4, 5]);

let set = &a - &b;

let mut i = 0;
let expected = [1, 2];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

[Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1356)[§](#associatedtype.Output-3)

The resulting type after applying the `-` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1123-1129)[§](#impl-Eq-for-HashSet%3CT,+S,+A%3E)