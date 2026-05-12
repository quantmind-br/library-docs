---
title: BTreeSet in std::collections - Rust
url: https://doc.rust-lang.org/std/collections/struct.BTreeSet.html
source: crawler
fetched_at: 2026-05-06T21:24:51.391616292-03:00
rendered_js: false
word_count: 2022
summary: BTreeSet is an ordered collection type in Rust that stores unique elements in a B-Tree structure, providing efficient logarithmic time operations and set theory utilities.
tags:
    - rust
    - btree-set
    - collection
    - data-structures
    - set-theory
    - api-reference
category: reference
---

## Struct BTreeSet

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#78-81)

```rust
pub struct BTreeSet<T, A = Global>
where
    A: Allocator + Clone,{ /* private fields */ }
```

Expand description

An ordered set based on a B-Tree.

See [`BTreeMap`](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html "struct std::collections::BTreeMap")’s documentation for a detailed discussion of this collection’s performance benefits and drawbacks.

It is a logic error for an item to be modified in such a way that the item’s ordering relative to any other item, as determined by the [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") trait, changes while it is in the set. This is normally only possible through [`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell"), [`RefCell`](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell"), global state, I/O, or unsafe code. The behavior resulting from such a logic error is not specified, but will be encapsulated to the `BTreeSet` that observed the logic error and not result in undefined behavior. This could include panics, incorrect results, aborts, memory leaks, and non-termination.

Iterators returned by [`BTreeSet::iter`](https://doc.rust-lang.org/std/collections/struct.BTreeSet.html#method.iter "method std::collections::BTreeSet::iter") and [`BTreeSet::into_iter`](https://doc.rust-lang.org/std/collections/struct.BTreeSet.html#method.into_iter "method std::collections::BTreeSet::into_iter") produce their items in order, and take worst-case logarithmic and amortized constant time per item returned.

## [§](#examples)Examples

```rust
use std::collections::BTreeSet;

// Type inference lets us omit an explicit type signature (which
// would be `BTreeSet<&str>` in this example).
let mut books = BTreeSet::new();

// Add some books.
books.insert("A Dance With Dragons");
books.insert("To Kill a Mockingbird");
books.insert("The Odyssey");
books.insert("The Great Gatsby");

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

A `BTreeSet` with a known list of items can be initialized from an array:

```rust
use std::collections::BTreeSet;

let set = BTreeSet::from([1, 2, 3]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#328)[§](#impl-BTreeSet%3CT%3E)

1.0.0 (const: 1.66.0) · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#344)

Makes a new, empty `BTreeSet`.

Does not allocate anything on its own.

##### [§](#examples-1)Examples

```rust
use std::collections::BTreeSet;

let mut set: BTreeSet<i32> = BTreeSet::new();
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#349)[§](#impl-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#364)

🔬This is a nightly-only experimental API. (`btreemap_alloc` [#32838](https://github.com/rust-lang/rust/issues/32838))

Makes a new `BTreeSet` with a reasonable choice of B.

##### [§](#examples-2)Examples

```rust
use std::collections::BTreeSet;
use std::alloc::Global;

let mut set: BTreeSet<i32> = BTreeSet::new_in(Global);
```

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#396-400)

Constructs a double-ended iterator over a sub-range of elements in the set. The simplest way is to use the range syntax `min..max`, thus `range(min..max)` will yield elements from min (inclusive) to max (exclusive). The range may also be entered as `(Bound<T>, Bound<T>)`, so for example `range((Excluded(4), Included(10)))` will yield a left-exclusive, right-inclusive range from 4 to 10.

##### [§](#panics)Panics

Panics if range `start > end`. Panics if range `start == end` and both bounds are `Excluded`.

##### [§](#examples-3)Examples

```rust
use std::collections::BTreeSet;
use std::ops::Bound::Included;

let mut set = BTreeSet::new();
set.insert(3);
set.insert(5);
set.insert(8);
for &elem in set.range((Included(&4), Included(&8))) {
    println!("{elem}");
}
assert_eq!(Some(&5), set.range(4..).next());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#426-428)

Visits the elements representing the difference, i.e., the elements that are in `self` but not in `other`, in ascending order.

##### [§](#examples-4)Examples

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);
a.insert(2);

let mut b = BTreeSet::new();
b.insert(2);
b.insert(3);

let diff: Vec<_> = a.difference(&b).cloned().collect();
assert_eq!(diff, [1]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#483-488)

Visits the elements representing the symmetric difference, i.e., the elements that are in `self` or in `other` but not in both, in ascending order.

##### [§](#examples-5)Examples

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);
a.insert(2);

let mut b = BTreeSet::new();
b.insert(2);
b.insert(3);

let sym_diff: Vec<_> = a.symmetric_difference(&b).cloned().collect();
assert_eq!(sym_diff, [1, 3]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#514-516)

Visits the elements representing the intersection, i.e., the elements that are both in `self` and `other`, in ascending order.

##### [§](#examples-6)Examples

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);
a.insert(2);

let mut b = BTreeSet::new();
b.insert(2);
b.insert(3);

let intersection: Vec<_> = a.intersection(&b).cloned().collect();
assert_eq!(intersection, [2]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#561-563)

Visits the elements representing the union, i.e., all the elements in `self` or `other`, without duplicates, in ascending order.

##### [§](#examples-7)Examples

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);

let mut b = BTreeSet::new();
b.insert(2);

let union: Vec<_> = a.union(&b).cloned().collect();
assert_eq!(union, [1, 2]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#581-583)

Clears the set, removing all elements.

##### [§](#examples-8)Examples

```rust
use std::collections::BTreeSet;

let mut v = BTreeSet::new();
v.insert(1);
v.clear();
assert!(v.is_empty());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#604-607)

Returns `true` if the set contains an element equal to the value.

The value may be any borrowed form of the set’s element type, but the ordering on the borrowed form *must* match the ordering on the element type.

##### [§](#examples-9)Examples

```rust
use std::collections::BTreeSet;

let set = BTreeSet::from([1, 2, 3]);
assert_eq!(set.contains(&1), true);
assert_eq!(set.contains(&4), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#629-632)

Returns a reference to the element in the set, if any, that is equal to the value.

The value may be any borrowed form of the set’s element type, but the ordering on the borrowed form *must* match the ordering on the element type.

##### [§](#examples-10)Examples

```rust
use std::collections::BTreeSet;

let set = BTreeSet::from([1, 2, 3]);
assert_eq!(set.get(&2), Some(&2));
assert_eq!(set.get(&4), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#656-658)

Returns `true` if `self` has no elements in common with `other`. This is equivalent to checking for an empty intersection.

##### [§](#examples-11)Examples

```rust
use std::collections::BTreeSet;

let a = BTreeSet::from([1, 2, 3]);
let mut b = BTreeSet::new();

assert_eq!(a.is_disjoint(&b), true);
b.insert(4);
assert_eq!(a.is_disjoint(&b), true);
b.insert(1);
assert_eq!(a.is_disjoint(&b), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#682-684)

Returns `true` if the set is a subset of another, i.e., `other` contains at least all the elements in `self`.

##### [§](#examples-12)Examples

```rust
use std::collections::BTreeSet;

let sup = BTreeSet::from([1, 2, 3]);
let mut set = BTreeSet::new();

assert_eq!(set.is_subset(&sup), true);
set.insert(2);
assert_eq!(set.is_subset(&sup), true);
set.insert(4);
assert_eq!(set.is_subset(&sup), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#763-765)

Returns `true` if the set is a superset of another, i.e., `self` contains at least all the elements in `other`.

##### [§](#examples-13)Examples

```rust
use std::collections::BTreeSet;

let sub = BTreeSet::from([1, 2]);
let mut set = BTreeSet::new();

assert_eq!(set.is_superset(&sub), false);

set.insert(0);
set.insert(1);
assert_eq!(set.is_superset(&sub), false);

set.insert(2);
assert_eq!(set.is_superset(&sub), true);
```

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#790-792)

Returns a reference to the first element in the set, if any. This element is always the minimum of all elements in the set.

##### [§](#examples-14)Examples

Basic usage:

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();
assert_eq!(set.first(), None);
set.insert(1);
assert_eq!(set.first(), Some(&1));
set.insert(2);
assert_eq!(set.first(), Some(&1));
```

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#817-819)

Returns a reference to the last element in the set, if any. This element is always the maximum of all elements in the set.

##### [§](#examples-15)Examples

Basic usage:

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();
assert_eq!(set.last(), None);
set.insert(1);
assert_eq!(set.last(), Some(&1));
set.insert(2);
assert_eq!(set.last(), Some(&2));
```

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#841-843)

Removes the first element from the set and returns it, if any. The first element is always the minimum element in the set.

##### [§](#examples-16)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();

set.insert(1);
while let Some(n) = set.pop_first() {
    assert_eq!(n, 1);
}
assert!(set.is_empty());
```

1.66.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#865-867)

Removes the last element from the set and returns it, if any. The last element is always the maximum element in the set.

##### [§](#examples-17)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();

set.insert(1);
while let Some(n) = set.pop_last() {
    assert_eq!(n, 1);
}
assert!(set.is_empty());
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#898-900)

Adds a value to the set.

Returns whether the value was newly inserted. That is:

- If the set did not previously contain an equal value, `true` is returned.
- If the set already contained an equal value, `false` is returned, and the entry is not updated.

See the [module-level documentation](https://doc.rust-lang.org/std/collections/index.html#insert-and-complex-keys) for more.

##### [§](#examples-18)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();

assert_eq!(set.insert(2), true);
assert_eq!(set.insert(2), false);
assert_eq!(set.len(), 1);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#922-924)

Adds a value to the set, replacing the existing element, if any, that is equal to the value. Returns the replaced element.

##### [§](#examples-19)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();
set.insert(Vec::<i32>::new());

assert_eq!(set.get(&[][..]).unwrap().capacity(), 0);
set.replace(Vec::with_capacity(10));
assert_eq!(set.get(&[][..]).unwrap().capacity(), 10);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#947-949)

🔬This is a nightly-only experimental API. (`btree_set_entry` [#133549](https://github.com/rust-lang/rust/issues/133549))

Inserts the given `value` into the set if it is not present, then returns a reference to the value in the set.

##### [§](#examples-20)Examples

```rust
#![feature(btree_set_entry)]

use std::collections::BTreeSet;

let mut set = BTreeSet::from([1, 2, 3]);
assert_eq!(set.len(), 3);
assert_eq!(set.get_or_insert(2), &2);
assert_eq!(set.get_or_insert(100), &100);
assert_eq!(set.len(), 4); // 100 was inserted
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#976-980)

🔬This is a nightly-only experimental API. (`btree_set_entry` [#133549](https://github.com/rust-lang/rust/issues/133549))

Inserts a value computed from `f` into the set if the given `value` is not present, then returns a reference to the value in the set.

##### [§](#examples-21)Examples

```rust
#![feature(btree_set_entry)]

use std::collections::BTreeSet;

let mut set: BTreeSet<String> = ["cat", "dog", "horse"]
    .iter().map(|&pet| pet.to_owned()).collect();

assert_eq!(set.len(), 3);
for &pet in &["cat", "dog", "fish"] {
    let value = set.get_or_insert_with(pet, str::to_owned);
    assert_eq!(value, pet);
}
assert_eq!(set.len(), 4); // a new "fish" was inserted
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1022-1024)

🔬This is a nightly-only experimental API. (`btree_set_entry` [#133549](https://github.com/rust-lang/rust/issues/133549))

Gets the given value’s corresponding entry in the set for in-place manipulation.

##### [§](#examples-22)Examples

```rust
#![feature(btree_set_entry)]

use std::collections::BTreeSet;
use std::collections::btree_set::Entry::*;

let mut singles = BTreeSet::new();
let mut dupes = BTreeSet::new();

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

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1051-1054)

If the set contains an element equal to the value, removes it from the set and drops it. Returns whether such an element was present.

The value may be any borrowed form of the set’s element type, but the ordering on the borrowed form *must* match the ordering on the element type.

##### [§](#examples-23)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();

set.insert(2);
assert_eq!(set.remove(&2), true);
assert_eq!(set.remove(&2), false);
```

1.9.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1076-1079)

Removes and returns the element in the set, if any, that is equal to the value.

The value may be any borrowed form of the set’s element type, but the ordering on the borrowed form *must* match the ordering on the element type.

##### [§](#examples-24)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::from([1, 2, 3]);
assert_eq!(set.take(&2), Some(2));
assert_eq!(set.take(&2), None);
```

1.53.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1100-1103)

Retains only the elements specified by the predicate.

In other words, remove all elements `e` for which `f(&e)` returns `false`. The elements are visited in ascending order.

##### [§](#examples-25)Examples

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::from([1, 2, 3, 4, 5, 6]);
// Keep only the even numbers.
set.retain(|&k| k % 2 == 0);
assert!(set.iter().eq([2, 4, 6].iter()));
```

1.11.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1137-1140)

Moves all elements from `other` into `self`, leaving `other` empty.

##### [§](#examples-26)Examples

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);
a.insert(2);
a.insert(3);

let mut b = BTreeSet::new();
b.insert(3);
b.insert(4);
b.insert(5);

a.append(&mut b);

assert_eq!(a.len(), 5);
assert_eq!(b.len(), 0);

assert!(a.contains(&1));
assert!(a.contains(&2));
assert!(a.contains(&3));
assert!(a.contains(&4));
assert!(a.contains(&5));
```

1.11.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1175-1178)

Splits the collection into two at the value. Returns a new collection with all elements greater than or equal to the value.

##### [§](#examples-27)Examples

Basic usage:

```rust
use std::collections::BTreeSet;

let mut a = BTreeSet::new();
a.insert(1);
a.insert(2);
a.insert(3);
a.insert(17);
a.insert(41);

let b = a.split_off(&3);

assert_eq!(a.len(), 2);
assert_eq!(b.len(), 3);

assert!(a.contains(&1));
assert!(a.contains(&2));

assert!(b.contains(&3));
assert!(b.contains(&17));
assert!(b.contains(&41));
```

Creates an iterator that visits elements in the specified range in ascending order and uses a closure to determine if an element should be removed.

If the closure returns `true`, the element is removed from the set and yielded. If the closure returns `false`, or panics, the element remains in the set and will not be yielded.

If the returned `ExtractIf` is not exhausted, e.g. because it is dropped without iterating or the iteration short-circuits, then the remaining elements will be retained. Use `extract_if().for_each(drop)` if you do not need the returned iterator, or [`retain`](https://doc.rust-lang.org/std/collections/struct.BTreeSet.html#method.retain "method std::collections::BTreeSet::retain") with a negated predicate if you also do not need to restrict the range.

##### [§](#examples-28)Examples

```rust
use std::collections::BTreeSet;

// Splitting a set into even and odd values, reusing the original set:
let mut set: BTreeSet<i32> = (0..8).collect();
let evens: BTreeSet<_> = set.extract_if(.., |v| v % 2 == 0).collect();
let odds = set;
assert_eq!(evens.into_iter().collect::<Vec<_>>(), vec![0, 2, 4, 6]);
assert_eq!(odds.into_iter().collect::<Vec<_>>(), vec![1, 3, 5, 7]);

// Splitting a set into low and high halves, reusing the original set:
let mut set: BTreeSet<i32> = (0..8).collect();
let low: BTreeSet<_> = set.extract_if(0..4, |_v| true).collect();
let high = set;
assert_eq!(low.into_iter().collect::<Vec<_>>(), [0, 1, 2, 3]);
assert_eq!(high.into_iter().collect::<Vec<_>>(), [4, 5, 6, 7]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1243)

Gets an iterator that visits the elements in the `BTreeSet` in ascending order.

##### [§](#examples-29)Examples

```rust
use std::collections::BTreeSet;

let set = BTreeSet::from([3, 1, 2]);
let mut set_iter = set.iter();
assert_eq!(set_iter.next(), Some(&1));
assert_eq!(set_iter.next(), Some(&2));
assert_eq!(set_iter.next(), Some(&3));
assert_eq!(set_iter.next(), None);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/71835 "Tracking issue for const_btree_len")) · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1267)

Returns the number of elements in the set.

##### [§](#examples-30)Examples

```rust
use std::collections::BTreeSet;

let mut v = BTreeSet::new();
assert_eq!(v.len(), 0);
v.insert(1);
assert_eq!(v.len(), 1);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/71835 "Tracking issue for const_btree_len")) · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1290)

Returns `true` if the set contains no elements.

##### [§](#examples-31)Examples

```rust
use std::collections::BTreeSet;

let mut v = BTreeSet::new();
assert!(v.is_empty());
v.insert(1);
assert!(!v.is_empty());
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1329-1332)

🔬This is a nightly-only experimental API. (`btree_cursors` [#107540](https://github.com/rust-lang/rust/issues/107540))

Returns a [`Cursor`](https://doc.rust-lang.org/std/collections/btree_set/struct.Cursor.html "struct std::collections::btree_set::Cursor") pointing at the gap before the smallest element greater than the given bound.

Passing `Bound::Included(x)` will return a cursor pointing to the gap before the smallest element greater than or equal to `x`.

Passing `Bound::Excluded(x)` will return a cursor pointing to the gap before the smallest element greater than `x`.

Passing `Bound::Unbounded` will return a cursor pointing to the gap before the smallest element in the set.

##### [§](#examples-32)Examples

```rust
#![feature(btree_cursors)]

use std::collections::BTreeSet;
use std::ops::Bound;

let set = BTreeSet::from([1, 2, 3, 4]);

let cursor = set.lower_bound(Bound::Included(&2));
assert_eq!(cursor.peek_prev(), Some(&1));
assert_eq!(cursor.peek_next(), Some(&2));

let cursor = set.lower_bound(Bound::Excluded(&2));
assert_eq!(cursor.peek_prev(), Some(&2));
assert_eq!(cursor.peek_next(), Some(&3));

let cursor = set.lower_bound(Bound::Unbounded);
assert_eq!(cursor.peek_prev(), None);
assert_eq!(cursor.peek_next(), Some(&1));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1372-1375)

🔬This is a nightly-only experimental API. (`btree_cursors` [#107540](https://github.com/rust-lang/rust/issues/107540))

Returns a [`CursorMut`](https://doc.rust-lang.org/std/collections/btree_set/struct.CursorMut.html "struct std::collections::btree_set::CursorMut") pointing at the gap before the smallest element greater than the given bound.

Passing `Bound::Included(x)` will return a cursor pointing to the gap before the smallest element greater than or equal to `x`.

Passing `Bound::Excluded(x)` will return a cursor pointing to the gap before the smallest element greater than `x`.

Passing `Bound::Unbounded` will return a cursor pointing to the gap before the smallest element in the set.

##### [§](#examples-33)Examples

```rust
#![feature(btree_cursors)]

use std::collections::BTreeSet;
use std::ops::Bound;

let mut set = BTreeSet::from([1, 2, 3, 4]);

let mut cursor = set.lower_bound_mut(Bound::Included(&2));
assert_eq!(cursor.peek_prev(), Some(&1));
assert_eq!(cursor.peek_next(), Some(&2));

let mut cursor = set.lower_bound_mut(Bound::Excluded(&2));
assert_eq!(cursor.peek_prev(), Some(&2));
assert_eq!(cursor.peek_next(), Some(&3));

let mut cursor = set.lower_bound_mut(Bound::Unbounded);
assert_eq!(cursor.peek_prev(), None);
assert_eq!(cursor.peek_next(), Some(&1));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1415-1418)

🔬This is a nightly-only experimental API. (`btree_cursors` [#107540](https://github.com/rust-lang/rust/issues/107540))

Returns a [`Cursor`](https://doc.rust-lang.org/std/collections/btree_set/struct.Cursor.html "struct std::collections::btree_set::Cursor") pointing at the gap after the greatest element smaller than the given bound.

Passing `Bound::Included(x)` will return a cursor pointing to the gap after the greatest element smaller than or equal to `x`.

Passing `Bound::Excluded(x)` will return a cursor pointing to the gap after the greatest element smaller than `x`.

Passing `Bound::Unbounded` will return a cursor pointing to the gap after the greatest element in the set.

##### [§](#examples-34)Examples

```rust
#![feature(btree_cursors)]

use std::collections::BTreeSet;
use std::ops::Bound;

let set = BTreeSet::from([1, 2, 3, 4]);

let cursor = set.upper_bound(Bound::Included(&3));
assert_eq!(cursor.peek_prev(), Some(&3));
assert_eq!(cursor.peek_next(), Some(&4));

let cursor = set.upper_bound(Bound::Excluded(&3));
assert_eq!(cursor.peek_prev(), Some(&2));
assert_eq!(cursor.peek_next(), Some(&3));

let cursor = set.upper_bound(Bound::Unbounded);
assert_eq!(cursor.peek_prev(), Some(&4));
assert_eq!(cursor.peek_next(), None);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1458-1461)

🔬This is a nightly-only experimental API. (`btree_cursors` [#107540](https://github.com/rust-lang/rust/issues/107540))

Returns a [`CursorMut`](https://doc.rust-lang.org/std/collections/btree_set/struct.CursorMut.html "struct std::collections::btree_set::CursorMut") pointing at the gap after the greatest element smaller than the given bound.

Passing `Bound::Included(x)` will return a cursor pointing to the gap after the greatest element smaller than or equal to `x`.

Passing `Bound::Excluded(x)` will return a cursor pointing to the gap after the greatest element smaller than `x`.

Passing `Bound::Unbounded` will return a cursor pointing to the gap after the greatest element in the set.

##### [§](#examples-35)Examples

```rust
#![feature(btree_cursors)]

use std::collections::BTreeSet;
use std::ops::Bound;

let mut set = BTreeSet::from([1, 2, 3, 4]);

let mut cursor = set.upper_bound_mut(Bound::Included(&3));
assert_eq!(cursor.peek_prev(), Some(&3));
assert_eq!(cursor.peek_next(), Some(&4));

let mut cursor = set.upper_bound_mut(Bound::Excluded(&3));
assert_eq!(cursor.peek_prev(), Some(&2));
assert_eq!(cursor.peek_next(), Some(&3));

let mut cursor = set.upper_bound_mut(Bound::Unbounded);
assert_eq!(cursor.peek_prev(), Some(&4));
assert_eq!(cursor.peek_next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1694)[§](#impl-BitAnd%3C%26BTreeSet%3CT,+A%3E%3E-for-%26BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1710)[§](#method.bitand)

Returns the intersection of `self` and `rhs` as a new `BTreeSet<T>`.

##### [§](#examples-40)Examples

```rust
use std::collections::BTreeSet;

let a = BTreeSet::from([1, 2, 3]);
let b = BTreeSet::from([2, 3, 4]);

let result = &a & &b;
assert_eq!(result, BTreeSet::from([2, 3]));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1695)[§](#associatedtype.Output-2)

The resulting type after applying the `&` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1719)[§](#impl-BitOr%3C%26BTreeSet%3CT,+A%3E%3E-for-%26BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1735)[§](#method.bitor)

Returns the union of `self` and `rhs` as a new `BTreeSet<T>`.

##### [§](#examples-41)Examples

```rust
use std::collections::BTreeSet;

let a = BTreeSet::from([1, 2, 3]);
let b = BTreeSet::from([3, 4, 5]);

let result = &a | &b;
assert_eq!(result, BTreeSet::from([1, 2, 3, 4, 5]));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1720)[§](#associatedtype.Output-3)

The resulting type after applying the `|` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1669)[§](#impl-BitXor%3C%26BTreeSet%3CT,+A%3E%3E-for-%26BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1685)[§](#method.bitxor)

Returns the symmetric difference of `self` and `rhs` as a new `BTreeSet<T>`.

##### [§](#examples-39)Examples

```rust
use std::collections::BTreeSet;

let a = BTreeSet::from([1, 2, 3]);
let b = BTreeSet::from([2, 3, 4]);

let result = &a ^ &b;
assert_eq!(result, BTreeSet::from([1, 4]));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1670)[§](#associatedtype.Output-1)

The resulting type after applying the `^` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#117)[§](#impl-Clone-for-BTreeSet%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1744)[§](#impl-Debug-for-BTreeSet%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1636)[§](#impl-Default-for-BTreeSet%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1638)[§](#method.default)

Creates an empty `BTreeSet`.

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1624)[§](#impl-Extend%3C%26T%3E-for-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1625)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1630)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1609)[§](#impl-Extend%3CT%3E-for-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1611)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1618)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1491)[§](#impl-From%3C%5BT;+N%5D%3E-for-BTreeSet%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1506)[§](#method.from)

Converts a `[T; N]` into a `BTreeSet<T>`.

If the array contains any equal values, all but one will be dropped.

##### [§](#examples-36)Examples

```rust
use std::collections::BTreeSet;

let set1 = BTreeSet::from([1, 2, 3, 4]);
let set2: BTreeSet<_> = [1, 2, 3, 4].into();
assert_eq!(set1, set2);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1468)[§](#impl-FromIterator%3CT%3E-for-BTreeSet%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#86)[§](#impl-Hash-for-BTreeSet%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1540)[§](#impl-IntoIterator-for-%26BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1541)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1542)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1544)[§](#method.into_iter-1)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1518)[§](#impl-IntoIterator-for-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1534)[§](#method.into_iter)

Gets an iterator for moving out the `BTreeSet`’s contents in ascending order.

##### [§](#examples-37)Examples

```rust
use std::collections::BTreeSet;

let set = BTreeSet::from([1, 2, 3, 4]);

let v: Vec<_> = set.into_iter().collect();
assert_eq!(v, [1, 2, 3, 4]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1519)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1520)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#110)[§](#impl-Ord-for-BTreeSet%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#93)[§](#impl-PartialEq-for-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#94)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#103)[§](#impl-PartialOrd-for-BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#104)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1644)[§](#impl-Sub%3C%26BTreeSet%3CT,+A%3E%3E-for-%26BTreeSet%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1660)[§](#method.sub)

Returns the difference of `self` and `rhs` as a new `BTreeSet<T>`.

##### [§](#examples-38)Examples

```rust
use std::collections::BTreeSet;

let a = BTreeSet::from([1, 2, 3]);
let b = BTreeSet::from([3, 4, 5]);

let result = &a - &b;
assert_eq!(result, BTreeSet::from([1, 2]));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1645)[§](#associatedtype.Output)

The resulting type after applying the `-` operator.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#100)[§](#impl-Eq-for-BTreeSet%3CT,+A%3E)