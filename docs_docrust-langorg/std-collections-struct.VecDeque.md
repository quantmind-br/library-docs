---
title: VecDeque in std::collections - Rust
url: https://doc.rust-lang.org/std/collections/struct.VecDeque.html
source: crawler
fetched_at: 2026-05-06T21:24:49.175156971-03:00
rendered_js: false
word_count: 4806
summary: This document describes the VecDeque structure in Rust, a growable ring buffer implementation providing double-ended queue functionality.
tags:
    - rust
    - data-structures
    - vecdeque
    - ring-buffer
    - collections
    - double-ended-queue
category: reference
---

## Struct VecDeque

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#104-107)

```rust
pub struct VecDeque<T, A = Global>
where
    A: Allocator,{ /* private fields */ }
```

Expand description

A double-ended queue implemented with a growable ring buffer.

The “default” usage of this type as a queue is to use [`push_back`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.push_back "method std::collections::VecDeque::push_back") to add to the queue, and [`pop_front`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.pop_front "method std::collections::VecDeque::pop_front") to remove from the queue. [`extend`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.extend "method std::collections::VecDeque::extend") and [`append`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.append "method std::collections::VecDeque::append") push onto the back in this manner, and iterating over `VecDeque` goes front to back.

A `VecDeque` with a known list of items can be initialized from an array:

```rust
use std::collections::VecDeque;

let deq = VecDeque::from([-1, 0, 1]);
```

Since `VecDeque` is a ring buffer, its elements are not necessarily contiguous in memory. If you want to access the elements as a single slice, such as for efficient sorting, you can use [`make_contiguous`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.make_contiguous "method std::collections::VecDeque::make_contiguous"). It rotates the `VecDeque` so that its elements do not wrap, and returns a mutable slice to the now-contiguous element sequence.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#170)[§](#impl-VecDeque%3CT,+A%3E)

🔬This is a nightly-only experimental API. (`vec_deque_extract_if` [#147750](https://github.com/rust-lang/rust/issues/147750))

Creates an iterator which uses a closure to determine if an element in the range should be removed.

If the closure returns `true`, the element is removed from the deque and yielded. If the closure returns `false`, or panics, the element remains in the deque and will not be yielded.

Only elements that fall in the provided range are considered for extraction, but any elements after the range will still have to be moved if any element has been extracted.

If the returned `ExtractIf` is not exhausted, e.g. because it is dropped without iterating or the iteration short-circuits, then the remaining elements will be retained. Use `extract_if().for_each(drop)` if you do not need the returned iterator, or [`retain_mut`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.retain_mut "method std::collections::VecDeque::retain_mut") with a negated predicate if you also do not need to restrict the range.

Using this method is equivalent to the following code:

```rust
#![feature(vec_deque_extract_if)]
let mut i = range.start;
let end_items = deq.len() - range.end;

while i < deq.len() - end_items {
    if some_predicate(&mut deq[i]) {
        let val = deq.remove(i).unwrap();
        // your code here
    } else {
        i += 1;
    }
}
```

But `extract_if` is easier to use. `extract_if` is also more efficient, because it can backshift the elements of the array in bulk.

The iterator also lets you mutate the value of each element in the closure, regardless of whether you choose to keep or remove it.

##### [§](#panics)Panics

If `range` is out of bounds.

##### [§](#examples)Examples

Splitting a deque into even and odd values, reusing the original deque:

```rust
#![feature(vec_deque_extract_if)]
use std::collections::VecDeque;

let mut numbers = VecDeque::from([1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15]);

let evens = numbers.extract_if(.., |x| *x % 2 == 0).collect::<VecDeque<_>>();
let odds = numbers;

assert_eq!(evens, VecDeque::from([2, 4, 6, 8, 14]));
assert_eq!(odds, VecDeque::from([1, 3, 5, 9, 11, 13, 15]));
```

Using the range argument to only process a part of the deque:

```rust
#![feature(vec_deque_extract_if)]
use std::collections::VecDeque;

let mut items = VecDeque::from([0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2]);
let ones = items.extract_if(7.., |x| *x == 1).collect::<VecDeque<_>>();
assert_eq!(items, VecDeque::from([0, 0, 0, 0, 0, 0, 0, 2, 2, 2]));
assert_eq!(ones.len(), 3);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#767)[§](#impl-VecDeque%3CT%3E)

1.0.0 (const: 1.68.0) · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#781)

Creates an empty deque.

##### [§](#examples-1)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<u32> = VecDeque::new();
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#798)

Creates an empty deque with space for at least `capacity` elements.

##### [§](#examples-2)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<u32> = VecDeque::with_capacity(10);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#822)

🔬This is a nightly-only experimental API. (`try_with_capacity` [#91913](https://github.com/rust-lang/rust/issues/91913))

Creates an empty deque with space for at least `capacity` elements.

##### [§](#errors)Errors

Returns an error if the capacity exceeds `isize::MAX` *bytes*, or if the allocator reports allocation failure.

##### [§](#examples-3)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<u32> = VecDeque::try_with_capacity(10)?;
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#827)[§](#impl-VecDeque%3CT,+A%3E-1)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#839)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates an empty deque.

##### [§](#examples-4)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<u32> = VecDeque::new();
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#853)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Creates an empty deque with space for at least `capacity` elements.

##### [§](#examples-5)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<u32> = VecDeque::with_capacity(10);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#907)

Provides a reference to the element at the given index.

Element at index 0 is the front of the queue.

##### [§](#examples-6)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(3);
buf.push_back(4);
buf.push_back(5);
buf.push_back(6);
assert_eq!(buf.get(1), Some(&4));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#937)

Provides a mutable reference to the element at the given index.

Element at index 0 is the front of the queue.

##### [§](#examples-7)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(3);
buf.push_back(4);
buf.push_back(5);
buf.push_back(6);
assert_eq!(buf[1], 4);
if let Some(elem) = buf.get_mut(1) {
    *elem = 7;
}
assert_eq!(buf[1], 7);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#970)

Swaps elements at indices `i` and `j`.

`i` and `j` may be equal.

Element at index 0 is the front of the queue.

##### [§](#panics-1)Panics

Panics if either index is out of bounds.

##### [§](#examples-8)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(3);
buf.push_back(4);
buf.push_back(5);
assert_eq!(buf, [3, 4, 5]);
buf.swap(0, 2);
assert_eq!(buf, [5, 4, 3]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#991)

Returns the number of elements the deque can hold without reallocating.

##### [§](#examples-9)Examples

```rust
use std::collections::VecDeque;

let buf: VecDeque<i32> = VecDeque::with_capacity(10);
assert!(buf.capacity() >= 10);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1018)

Reserves the minimum capacity for at least `additional` more elements to be inserted in the given deque. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore capacity can not be relied upon to be precisely minimal. Prefer [`reserve`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.reserve "method std::collections::VecDeque::reserve") if future insertions are expected.

##### [§](#panics-2)Panics

Panics if the new capacity overflows `usize`.

##### [§](#examples-10)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<i32> = [1].into();
buf.reserve_exact(10);
assert!(buf.capacity() >= 11);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1048)

Reserves capacity for at least `additional` more elements to be inserted in the given deque. The collection may reserve more space to speculatively avoid frequent reallocations.

##### [§](#panics-3)Panics

Panics if the new capacity overflows `usize`.

##### [§](#examples-11)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<i32> = [1].into();
buf.reserve(10);
assert!(buf.capacity() >= 11);
```

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1100)

Tries to reserve the minimum capacity for at least `additional` more elements to be inserted in the given deque. After calling `try_reserve_exact`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if the capacity is already sufficient.

Note that the allocator may give the collection more space than it requests. Therefore, capacity can not be relied upon to be precisely minimal. Prefer [`try_reserve`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.try_reserve "method std::collections::VecDeque::try_reserve") if future insertions are expected.

##### [§](#errors-1)Errors

If the capacity overflows `usize`, or the allocator reports a failure, then an error is returned.

##### [§](#examples-12)Examples

```rust
use std::collections::TryReserveError;
use std::collections::VecDeque;

fn process_data(data: &[u32]) -> Result<VecDeque<u32>, TryReserveError> {
    let mut output = VecDeque::new();

    // Pre-reserve the memory, exiting if we can't
    output.try_reserve_exact(data.len())?;

    // Now we know this can't OOM(Out-Of-Memory) in the middle of our complex work
    output.extend(data.iter().map(|&val| {
        val * 2 + 5 // very complicated
    }));

    Ok(output)
}
```

1.57.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1148)

Tries to reserve capacity for at least `additional` more elements to be inserted in the given deque. The collection may reserve more space to speculatively avoid frequent reallocations. After calling `try_reserve`, capacity will be greater than or equal to `self.len() + additional` if it returns `Ok(())`. Does nothing if capacity is already sufficient. This method preserves the contents even if an error occurs.

##### [§](#errors-2)Errors

If the capacity overflows `usize`, or the allocator reports a failure, then an error is returned.

##### [§](#examples-13)Examples

```rust
use std::collections::TryReserveError;
use std::collections::VecDeque;

fn process_data(data: &[u32]) -> Result<VecDeque<u32>, TryReserveError> {
    let mut output = VecDeque::new();

    // Pre-reserve the memory, exiting if we can't
    output.try_reserve(data.len())?;

    // Now we know this can't OOM in the middle of our complex work
    output.extend(data.iter().map(|&val| {
        val * 2 + 5 // very complicated
    }));

    Ok(output)
}
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1179)

Shrinks the capacity of the deque as much as possible.

It will drop down as close as possible to the length but the allocator may still inform the deque that there is space for a few more elements.

##### [§](#examples-14)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::with_capacity(15);
buf.extend(0..4);
assert_eq!(buf.capacity(), 15);
buf.shrink_to_fit();
assert!(buf.capacity() >= 4);
```

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1204)

Shrinks the capacity of the deque with a lower bound.

The capacity will remain at least as large as both the length and the supplied value.

If the current capacity is less than the lower limit, this is a no-op.

##### [§](#examples-15)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::with_capacity(15);
buf.extend(0..4);
assert_eq!(buf.capacity(), 15);
buf.shrink_to(6);
assert!(buf.capacity() >= 6);
buf.shrink_to(0);
assert!(buf.capacity() >= 4);
```

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1364)

Shortens the deque, keeping the first `len` elements and dropping the rest.

If `len` is greater or equal to the deque’s current length, this has no effect.

##### [§](#examples-16)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(5);
buf.push_back(10);
buf.push_back(15);
assert_eq!(buf, [5, 10, 15]);
buf.truncate(1);
assert_eq!(buf, [5]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1430)

🔬This is a nightly-only experimental API. (`vec_deque_truncate_front` [#140667](https://github.com/rust-lang/rust/issues/140667))

Shortens the deque, keeping the last `len` elements and dropping the rest.

If `len` is greater or equal to the deque’s current length, this has no effect.

##### [§](#examples-17)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_front(5);
buf.push_front(10);
buf.push_front(15);
assert_eq!(buf, [15, 10, 5]);
assert_eq!(buf.as_slices(), (&[15, 10, 5][..], &[][..]));
buf.truncate_front(1);
assert_eq!(buf.as_slices(), (&[5][..], &[][..]));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1478)

🔬This is a nightly-only experimental API. (`allocator_api` [#32838](https://github.com/rust-lang/rust/issues/32838))

Returns a reference to the underlying allocator.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1499)

Returns a front-to-back iterator.

##### [§](#examples-18)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(5);
buf.push_back(3);
buf.push_back(4);
let b: &[_] = &[&5, &3, &4];
let c: Vec<&i32> = buf.iter().collect();
assert_eq!(&c[..], b);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1522)

Returns a front-to-back iterator that returns mutable references.

##### [§](#examples-19)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(5);
buf.push_back(3);
buf.push_back(4);
for num in buf.iter_mut() {
    *num = *num - 2;
}
let b: &[_] = &[&mut 3, &mut 1, &mut 2];
assert_eq!(&buf.iter_mut().collect::<Vec<&mut i32>>()[..], b);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1563)

Returns a pair of slices which contain, in order, the contents of the deque.

If [`make_contiguous`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.make_contiguous "method std::collections::VecDeque::make_contiguous") was previously called, all elements of the deque will be in the first slice and the second slice will be empty. Otherwise, the exact split point depends on implementation details and is not guaranteed.

##### [§](#examples-20)Examples

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::new();

deque.push_back(0);
deque.push_back(1);
deque.push_back(2);

let expected = [0, 1, 2];
let (front, back) = deque.as_slices();
assert_eq!(&expected[..front.len()], front);
assert_eq!(&expected[front.len()..], back);

deque.push_front(10);
deque.push_front(9);

let expected = [9, 10, 0, 1, 2];
let (front, back) = deque.as_slices();
assert_eq!(&expected[..front.len()], front);
assert_eq!(&expected[front.len()..], back);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1612)

Returns a pair of slices which contain, in order, the contents of the deque.

If [`make_contiguous`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.make_contiguous "method std::collections::VecDeque::make_contiguous") was previously called, all elements of the deque will be in the first slice and the second slice will be empty. Otherwise, the exact split point depends on implementation details and is not guaranteed.

##### [§](#examples-21)Examples

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::new();

deque.push_back(0);
deque.push_back(1);

deque.push_front(10);
deque.push_front(9);

// Since the split point is not guaranteed, we may need to update
// either slice.
let mut update_nth = |index: usize, val: u32| {
    let (front, back) = deque.as_mut_slices();
    if index > front.len() - 1 {
        back[index - front.len()] = val;
    } else {
        front[index] = val;
    }
};

update_nth(0, 42);
update_nth(2, 24);

let v: Vec<_> = deque.into();
assert_eq!(v, [42, 10, 24, 1]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1633)

Returns the number of elements in the deque.

##### [§](#examples-22)Examples

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::new();
assert_eq!(deque.len(), 0);
deque.push_back(1);
assert_eq!(deque.len(), 1);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1650)

Returns `true` if the deque is empty.

##### [§](#examples-23)Examples

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::new();
assert!(deque.is_empty());
deque.push_front(1);
assert!(!deque.is_empty());
```

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1719-1721)

Creates an iterator that covers the specified range in the deque.

##### [§](#panics-4)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the deque.

##### [§](#examples-24)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<_> = [1, 2, 3].into();
let range = deque.range(2..).copied().collect::<VecDeque<_>>();
assert_eq!(range, [3]);

// A full range covers all contents
let all = deque.range(..);
assert_eq!(all.len(), 3);
```

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1759-1761)

Creates an iterator that covers the specified mutable range in the deque.

##### [§](#panics-5)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the deque.

##### [§](#examples-25)Examples

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<_> = [1, 2, 3].into();
for v in deque.range_mut(2..) {
  *v *= 2;
}
assert_eq!(deque, [1, 2, 6]);

// A full range covers all contents
for v in deque.range_mut(..) {
  *v *= 2;
}
assert_eq!(deque, [2, 4, 12]);
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1808-1810)

Removes the specified range from the deque in bulk, returning all removed elements as an iterator. If the iterator is dropped before being fully consumed, it drops the remaining removed elements.

The returned iterator keeps a mutable borrow on the queue to optimize its implementation.

##### [§](#panics-6)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the deque.

##### [§](#leaking)Leaking

If the returned iterator goes out of scope without being dropped (due to [`mem::forget`](https://doc.rust-lang.org/std/mem/fn.forget.html "fn std::mem::forget"), for example), the deque may have lost and leaked elements arbitrarily, including elements outside the range.

##### [§](#examples-26)Examples

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<_> = [1, 2, 3].into();
let drained = deque.drain(2..).collect::<VecDeque<_>>();
assert_eq!(drained, [3]);
assert_eq!(deque, [1, 2]);

// A full range clears all contents, like `clear()` does
deque.drain(..);
assert!(deque.is_empty());
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1898-1901)

🔬This is a nightly-only experimental API. (`deque_extend_front` [#146975](https://github.com/rust-lang/rust/issues/146975))

Creates a splicing iterator that replaces the specified range in the deque with the given `replace_with` iterator and yields the removed items. `replace_with` does not need to be the same length as `range`.

`range` is removed even if the `Splice` iterator is not consumed before it is dropped.

It is unspecified how many elements are removed from the deque if the `Splice` value is leaked.

The input iterator `replace_with` is only consumed when the `Splice` value is dropped.

This is optimal if:

- The tail (elements in the deque after `range`) is empty,
- or `replace_with` yields fewer or equal elements than `range`’s length
- or the lower bound of its `size_hint()` is exact.

Otherwise, a temporary vector is allocated and the tail is moved twice.

##### [§](#panics-7)Panics

Panics if the range has `start_bound > end_bound`, or, if the range is bounded on either end and past the length of the deque.

##### [§](#examples-27)Examples

```rust

let mut v = VecDeque::from(vec![1, 2, 3, 4]);
let new = [7, 8, 9];
let u: Vec<_> = v.splice(1..3, new).collect();
assert_eq!(v, [1, 7, 8, 9, 4]);
assert_eq!(u, [2, 3]);
```

Using `splice` to insert new items into a vector efficiently at a specific position indicated by an empty range:

```rust

let mut v = VecDeque::from(vec![1, 5]);
let new = [2, 3, 4];
v.splice(1..1, new);
assert_eq!(v, [1, 2, 3, 4, 5]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1920)

Clears the deque, removing all values.

##### [§](#examples-28)Examples

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::new();
deque.push_back(1);
deque.clear();
assert!(deque.is_empty());
```

1.12.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1949-1951)

Returns `true` if the deque contains an element equal to the given value.

This operation is *O*(*n*).

Note that if you have a sorted `VecDeque`, [`binary_search`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search "method std::collections::VecDeque::binary_search") may be faster.

##### [§](#examples-29)Examples

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<u32> = VecDeque::new();

deque.push_back(0);
deque.push_back(1);

assert_eq!(deque.contains(&1), true);
assert_eq!(deque.contains(&10), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1974)

Provides a reference to the front element, or `None` if the deque is empty.

##### [§](#examples-30)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
assert_eq!(d.front(), None);

d.push_back(1);
d.push_back(2);
assert_eq!(d.front(), Some(&1));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#1998)

Provides a mutable reference to the front element, or `None` if the deque is empty.

##### [§](#examples-31)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
assert_eq!(d.front_mut(), None);

d.push_back(1);
d.push_back(2);
match d.front_mut() {
    Some(x) => *x = 9,
    None => (),
}
assert_eq!(d.front(), Some(&9));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2019)

Provides a reference to the back element, or `None` if the deque is empty.

##### [§](#examples-32)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
assert_eq!(d.back(), None);

d.push_back(1);
d.push_back(2);
assert_eq!(d.back(), Some(&2));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2043)

Provides a mutable reference to the back element, or `None` if the deque is empty.

##### [§](#examples-33)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
assert_eq!(d.back(), None);

d.push_back(1);
d.push_back(2);
match d.back_mut() {
    Some(x) => *x = 9,
    None => (),
}
assert_eq!(d.back(), Some(&9));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2064)

Removes the first element and returns it, or `None` if the deque is empty.

##### [§](#examples-34)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
d.push_back(1);
d.push_back(2);

assert_eq!(d.pop_front(), Some(1));
assert_eq!(d.pop_front(), Some(2));
assert_eq!(d.pop_front(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2093)

Removes the last element from the deque and returns it, or `None` if it is empty.

##### [§](#examples-35)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
assert_eq!(buf.pop_back(), None);
buf.push_back(1);
buf.push_back(3);
assert_eq!(buf.pop_back(), Some(3));
```

1.93.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2122)

Removes and returns the first element from the deque if the predicate returns `true`, or [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the predicate returns false or the deque is empty (the predicate will not be called in that case).

##### [§](#examples-36)Examples

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<i32> = vec![0, 1, 2, 3, 4].into();
let pred = |x: &mut i32| *x % 2 == 0;

assert_eq!(deque.pop_front_if(pred), Some(0));
assert_eq!(deque, [1, 2, 3, 4]);
assert_eq!(deque.pop_front_if(pred), None);
```

1.93.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2144)

Removes and returns the last element from the deque if the predicate returns `true`, or [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the predicate returns false or the deque is empty (the predicate will not be called in that case).

##### [§](#examples-37)Examples

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<i32> = vec![0, 1, 2, 3, 4].into();
let pred = |x: &mut i32| *x % 2 == 0;

assert_eq!(deque.pop_back_if(pred), Some(4));
assert_eq!(deque, [0, 1, 2, 3]);
assert_eq!(deque.pop_back_if(pred), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2162)

Prepends an element to the deque.

##### [§](#examples-38)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::new();
d.push_front(1);
d.push_front(2);
assert_eq!(d.front(), Some(&2));
```

1.95.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2180)

Prepends an element to the deque, returning a reference to it.

##### [§](#examples-39)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::from([1, 2, 3]);
let x = d.push_front_mut(8);
*x -= 1;
assert_eq!(d.front(), Some(&7));
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2205)

Appends an element to the back of the deque.

##### [§](#examples-40)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(1);
buf.push_back(3);
assert_eq!(3, *buf.back().unwrap());
```

1.95.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2223)

Appends an element to the back of the deque, returning a reference to it.

##### [§](#examples-41)Examples

```rust
use std::collections::VecDeque;

let mut d = VecDeque::from([1, 2, 3]);
let x = d.push_back_mut(9);
*x += 1;
assert_eq!(d.back(), Some(&10));
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2264)

🔬This is a nightly-only experimental API. (`deque_extend_front` [#146975](https://github.com/rust-lang/rust/issues/146975))

Prepends all contents of the iterator to the front of the deque. The order of the contents is preserved.

To get behavior like [`append`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.append "method std::collections::VecDeque::append") where elements are moved from the other collection to this one, use `self.prepend(other.drain(..))`.

##### [§](#examples-42)Examples

```rust
#![feature(deque_extend_front)]
use std::collections::VecDeque;

let mut deque = VecDeque::from([4, 5, 6]);
deque.prepend([1, 2, 3]);
assert_eq!(deque, [1, 2, 3, 4, 5, 6]);
```

Move values between collections like [`append`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.append "method std::collections::VecDeque::append") does but prepend to the front:

```rust
#![feature(deque_extend_front)]
use std::collections::VecDeque;

let mut deque1 = VecDeque::from([4, 5, 6]);
let mut deque2 = VecDeque::from([1, 2, 3]);
deque1.prepend(deque2.drain(..));
assert_eq!(deque1, [1, 2, 3, 4, 5, 6]);
assert!(deque2.is_empty());
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2296)

🔬This is a nightly-only experimental API. (`deque_extend_front` [#146975](https://github.com/rust-lang/rust/issues/146975))

Prepends all contents of the iterator to the front of the deque, as if [`push_front`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.push_front "method std::collections::VecDeque::push_front") was called repeatedly with the values yielded by the iterator.

##### [§](#examples-43)Examples

```rust
#![feature(deque_extend_front)]
use std::collections::VecDeque;

let mut deque = VecDeque::from([4, 5, 6]);
deque.extend_front([3, 2, 1]);
assert_eq!(deque, [1, 2, 3, 4, 5, 6]);
```

This behaves like [`push_front`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.push_front "method std::collections::VecDeque::push_front") was called repeatedly:

```rust
use std::collections::VecDeque;

let mut deque = VecDeque::from([4, 5, 6]);
for v in [3, 2, 1] {
    deque.push_front(v);
}
assert_eq!(deque, [1, 2, 3, 4, 5, 6]);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2331)

Removes an element from anywhere in the deque and returns it, replacing it with the first element.

This does not preserve ordering, but is *O*(1).

Returns `None` if `index` is out of bounds.

Element at index 0 is the front of the queue.

##### [§](#examples-44)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
assert_eq!(buf.swap_remove_front(0), None);
buf.push_back(1);
buf.push_back(2);
buf.push_back(3);
assert_eq!(buf, [1, 2, 3]);

assert_eq!(buf.swap_remove_front(2), Some(3));
assert_eq!(buf, [2, 1]);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2366)

Removes an element from anywhere in the deque and returns it, replacing it with the last element.

This does not preserve ordering, but is *O*(1).

Returns `None` if `index` is out of bounds.

Element at index 0 is the front of the queue.

##### [§](#examples-45)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
assert_eq!(buf.swap_remove_back(0), None);
buf.push_back(1);
buf.push_back(2);
buf.push_back(3);
assert_eq!(buf, [1, 2, 3]);

assert_eq!(buf.swap_remove_back(0), Some(1));
assert_eq!(buf, [3, 2]);
```

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2403)

Inserts an element at `index` within the deque, shifting all elements with indices greater than or equal to `index` towards the back.

Element at index 0 is the front of the queue.

##### [§](#panics-8)Panics

Panics if `index` is strictly greater than the deque’s length.

##### [§](#examples-46)Examples

```rust
use std::collections::VecDeque;

let mut vec_deque = VecDeque::new();
vec_deque.push_back('a');
vec_deque.push_back('b');
vec_deque.push_back('c');
assert_eq!(vec_deque, &['a', 'b', 'c']);

vec_deque.insert(1, 'd');
assert_eq!(vec_deque, &['a', 'd', 'b', 'c']);

vec_deque.insert(4, 'e');
assert_eq!(vec_deque, &['a', 'd', 'b', 'c', 'e']);
```

1.95.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2430)

Inserts an element at `index` within the deque, shifting all elements with indices greater than or equal to `index` towards the back, and returning a reference to it.

Element at index 0 is the front of the queue.

##### [§](#panics-9)Panics

Panics if `index` is strictly greater than the deque’s length.

##### [§](#examples-47)Examples

```rust
use std::collections::VecDeque;

let mut vec_deque = VecDeque::from([1, 2, 3]);

let x = vec_deque.insert_mut(1, 5);
*x += 7;
assert_eq!(vec_deque, &[1, 12, 2, 3]);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2482)

Removes and returns the element at `index` from the deque. Whichever end is closer to the removal point will be moved to make room, and all the affected elements will be moved to new positions. Returns `None` if `index` is out of bounds.

Element at index 0 is the front of the queue.

##### [§](#examples-48)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back('a');
buf.push_back('b');
buf.push_back('c');
assert_eq!(buf, ['a', 'b', 'c']);

assert_eq!(buf.remove(1), Some('b'));
assert_eq!(buf, ['a', 'c']);
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2534-2536)

Splits the deque into two at the given index.

Returns a newly allocated `VecDeque`. `self` contains elements `[0, at)`, and the returned deque contains elements `[at, len)`.

Note that the capacity of `self` does not change.

Element at index 0 is the front of the queue.

##### [§](#panics-10)Panics

Panics if `at > len`.

##### [§](#examples-49)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<_> = ['a', 'b', 'c'].into();
let buf2 = buf.split_off(1);
assert_eq!(buf, ['a']);
assert_eq!(buf2, ['b', 'c']);
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2600)

Moves all the elements of `other` into `self`, leaving `other` empty.

##### [§](#panics-11)Panics

Panics if the new number of elements in self overflows a `usize`.

##### [§](#examples-50)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<_> = [1, 2].into();
let mut buf2: VecDeque<_> = [3, 4].into();
buf.append(&mut buf2);
assert_eq!(buf, [1, 2, 3, 4]);
assert_eq!(buf2, []);
```

1.4.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2655-2657)

Retains only the elements specified by the predicate.

In other words, remove all elements `e` for which `f(&e)` returns false. This method operates in place, visiting each element exactly once in the original order, and preserves the order of the retained elements.

##### [§](#examples-51)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.extend(1..5);
buf.retain(|&x| x % 2 == 0);
assert_eq!(buf, [2, 4]);
```

Because the elements are visited exactly once in the original order, external state may be used to decide which elements to keep.

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.extend(1..6);

let keep = [false, true, true, false, true];
let mut iter = keep.iter();
buf.retain(|_| *iter.next().unwrap());
assert_eq!(buf, [2, 3, 5]);
```

1.61.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2684-2686)

Retains only the elements specified by the predicate.

In other words, remove all elements `e` for which `f(&mut e)` returns false. This method operates in place, visiting each element exactly once in the original order, and preserves the order of the retained elements.

##### [§](#examples-52)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.extend(1..5);
buf.retain_mut(|x| if *x % 2 == 0 {
    *x += 1;
    true
} else {
    false
});
assert_eq!(buf, [3, 5]);
```

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2760)

Modifies the deque in-place so that `len()` is equal to `new_len`, either by removing excess elements from the back or by appending elements generated by calling `generator` to the back.

##### [§](#examples-53)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(5);
buf.push_back(10);
buf.push_back(15);
assert_eq!(buf, [5, 10, 15]);

buf.resize_with(5, Default::default);
assert_eq!(buf, [5, 10, 15, 0, 0]);

buf.resize_with(2, || unreachable!());
assert_eq!(buf, [5, 10]);

let mut state = 100;
buf.resize_with(5, || { state += 1; state });
assert_eq!(buf, [5, 10, 101, 102, 103]);
```

1.48.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2826)

Rearranges the internal storage of this deque so it is one contiguous slice, which is then returned.

This method does not allocate and does not change the order of the inserted elements. As it returns a mutable slice, this can be used to sort a deque.

Once the internal storage is contiguous, the [`as_slices`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.as_slices "method std::collections::VecDeque::as_slices") and [`as_mut_slices`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.as_mut_slices "method std::collections::VecDeque::as_mut_slices") methods will return the entire contents of the deque in a single slice.

##### [§](#examples-54)Examples

Sorting the content of a deque.

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::with_capacity(15);

buf.push_back(2);
buf.push_back(1);
buf.push_front(3);

// sorting the deque
buf.make_contiguous().sort();
assert_eq!(buf.as_slices(), (&[1, 2, 3] as &[_], &[] as &[_]));

// sorting it in reverse order
buf.make_contiguous().sort_by(|a, b| b.cmp(a));
assert_eq!(buf.as_slices(), (&[3, 2, 1] as &[_], &[] as &[_]));
```

Getting immutable access to the contiguous slice.

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();

buf.push_back(2);
buf.push_back(1);
buf.push_front(3);

buf.make_contiguous();
if let (slice, &[]) = buf.as_slices() {
    // we can now be sure that `slice` contains all elements of the deque,
    // while still having immutable access to `buf`.
    assert_eq!(buf.len(), slice.len());
    assert_eq!(slice, &[3, 2, 1] as &[_]);
}
```

1.36.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#2985)

Rotates the double-ended queue `n` places to the left.

Equivalently,

- Rotates item `n` into the first position.
- Pops the first `n` items and pushes them to the end.
- Rotates `len() - n` places to the right.

##### [§](#panics-12)Panics

If `n` is greater than `len()`. Note that `n == len()` does *not* panic and is a no-op rotation.

##### [§](#complexity)Complexity

Takes `*O*(min(n, len() - n))` time and no extra space.

##### [§](#examples-55)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<_> = (0..10).collect();

buf.rotate_left(3);
assert_eq!(buf, [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]);

for i in 1..10 {
    assert_eq!(i * 3 % 10, buf[0]);
    buf.rotate_left(3);
}
assert_eq!(buf, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
```

1.36.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3028)

Rotates the double-ended queue `n` places to the right.

Equivalently,

- Rotates the first item into position `n`.
- Pops the last `n` items and pushes them to the front.
- Rotates `len() - n` places to the left.

##### [§](#panics-13)Panics

If `n` is greater than `len()`. Note that `n == len()` does *not* panic and is a no-op rotation.

##### [§](#complexity-1)Complexity

Takes `*O*(min(n, len() - n))` time and no extra space.

##### [§](#examples-56)Examples

```rust
use std::collections::VecDeque;

let mut buf: VecDeque<_> = (0..10).collect();

buf.rotate_right(3);
assert_eq!(buf, [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]);

for i in 1..10 {
    assert_eq!(0, buf[i * 3 % 10]);
    buf.rotate_right(3);
}
assert_eq!(buf, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
```

1.54.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3113-3115)

Binary searches this `VecDeque` for a given element. If the `VecDeque` is not sorted, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search_by`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by "method std::collections::VecDeque::binary_search_by"), [`binary_search_by_key`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by_key "method std::collections::VecDeque::binary_search_by_key"), and [`partition_point`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.partition_point "method std::collections::VecDeque::partition_point").

##### [§](#examples-57)Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
use std::collections::VecDeque;

let deque: VecDeque<_> = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].into();

assert_eq!(deque.binary_search(&13),  Ok(9));
assert_eq!(deque.binary_search(&4),   Err(7));
assert_eq!(deque.binary_search(&100), Err(13));
let r = deque.binary_search(&1);
assert!(matches!(r, Ok(1..=4)));
```

If you want to insert an item to a sorted deque, while maintaining sort order, consider using [`partition_point`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.partition_point "method std::collections::VecDeque::partition_point"):

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<_> = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].into();
let num = 42;
let idx = deque.partition_point(|&x| x <= num);
// If `num` is unique, `s.partition_point(|&x| x < num)` (with `<`) is equivalent to
// `s.binary_search(&num).unwrap_or_else(|x| x)`, but using `<=` may allow `insert`
// to shift less elements.
deque.insert(idx, num);
assert_eq!(deque, &[0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

1.54.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3159-3161)

Binary searches this `VecDeque` with a comparator function.

The comparator function should return an order code that indicates whether its argument is `Less`, `Equal` or `Greater` the desired target. If the `VecDeque` is not sorted or if the comparator function does not implement an order consistent with the sort order of the underlying `VecDeque`, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search "method std::collections::VecDeque::binary_search"), [`binary_search_by_key`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by_key "method std::collections::VecDeque::binary_search_by_key"), and [`partition_point`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.partition_point "method std::collections::VecDeque::partition_point").

##### [§](#examples-58)Examples

Looks up a series of four elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
use std::collections::VecDeque;

let deque: VecDeque<_> = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].into();

assert_eq!(deque.binary_search_by(|x| x.cmp(&13)),  Ok(9));
assert_eq!(deque.binary_search_by(|x| x.cmp(&4)),   Err(7));
assert_eq!(deque.binary_search_by(|x| x.cmp(&100)), Err(13));
let r = deque.binary_search_by(|x| x.cmp(&1));
assert!(matches!(r, Ok(1..=4)));
```

1.54.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3217-3220)

Binary searches this `VecDeque` with a key extraction function.

Assumes that the deque is sorted by the key, for instance with [`make_contiguous().sort_by_key()`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.make_contiguous "method std::collections::VecDeque::make_contiguous") using the same key extraction function. If the deque is not sorted by the key, the returned result is unspecified and meaningless.

If the value is found then [`Result::Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") is returned, containing the index of the matching element. If there are multiple matches, then any one of the matches could be returned. If the value is not found then [`Result::Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned, containing the index where a matching element could be inserted while maintaining sorted order.

See also [`binary_search`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search "method std::collections::VecDeque::binary_search"), [`binary_search_by`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by "method std::collections::VecDeque::binary_search_by"), and [`partition_point`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.partition_point "method std::collections::VecDeque::partition_point").

##### [§](#examples-59)Examples

Looks up a series of four elements in a slice of pairs sorted by their second elements. The first is found, with a uniquely determined position; the second and third are not found; the fourth could match any position in `[1, 4]`.

```rust
use std::collections::VecDeque;

let deque: VecDeque<_> = [(0, 0), (2, 1), (4, 1), (5, 1),
         (3, 1), (1, 2), (2, 3), (4, 5), (5, 8), (3, 13),
         (1, 21), (2, 34), (4, 55)].into();

assert_eq!(deque.binary_search_by_key(&13, |&(a, b)| b),  Ok(9));
assert_eq!(deque.binary_search_by_key(&4, |&(a, b)| b),   Err(7));
assert_eq!(deque.binary_search_by_key(&100, |&(a, b)| b), Err(13));
let r = deque.binary_search_by_key(&1, |&(a, b)| b);
assert!(matches!(r, Ok(1..=4)));
```

1.54.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3269-3271)

Returns the index of the partition point according to the given predicate (the index of the first element of the second partition).

The deque is assumed to be partitioned according to the given predicate. This means that all elements for which the predicate returns true are at the start of the deque and all elements for which the predicate returns false are at the end. For example, `[7, 15, 3, 5, 4, 12, 6]` is partitioned under the predicate `x % 2 != 0` (all odd numbers are at the start, all even at the end).

If the deque is not partitioned, the returned result is unspecified and meaningless, as this method performs a kind of binary search.

See also [`binary_search`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search "method std::collections::VecDeque::binary_search"), [`binary_search_by`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by "method std::collections::VecDeque::binary_search_by"), and [`binary_search_by_key`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.binary_search_by_key "method std::collections::VecDeque::binary_search_by_key").

##### [§](#examples-60)Examples

```rust
use std::collections::VecDeque;

let deque: VecDeque<_> = [1, 2, 3, 3, 5, 6, 7].into();
let i = deque.partition_point(|&x| x < 5);

assert_eq!(i, 4);
assert!(deque.iter().take(i).all(|&x| x < 5));
assert!(deque.iter().skip(i).all(|&x| !(x < 5)));
```

If you want to insert an item to a sorted deque, while maintaining sort order:

```rust
use std::collections::VecDeque;

let mut deque: VecDeque<_> = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].into();
let num = 42;
let idx = deque.partition_point(|&x| x < num);
deque.insert(idx, num);
assert_eq!(deque, &[0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3283)[§](#impl-VecDeque%3CT,+A%3E-2)

1.16.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3306)

Modifies the deque in-place so that `len()` is equal to new\_len, either by removing excess elements from the back or by appending clones of `value` to the back.

##### [§](#examples-61)Examples

```rust
use std::collections::VecDeque;

let mut buf = VecDeque::new();
buf.push_back(5);
buf.push_back(10);
buf.push_back(15);
assert_eq!(buf, [5, 10, 15]);

buf.resize(2, 0);
assert_eq!(buf, [5, 10]);

buf.resize(5, 20);
assert_eq!(buf, [5, 10, 20, 20, 20]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3342-3344)

🔬This is a nightly-only experimental API. (`deque_extend_front` [#146975](https://github.com/rust-lang/rust/issues/146975))

Clones the elements at the range `src` and appends them to the end.

##### [§](#panics-14)Panics

Panics if the starting index is greater than the end index or if either index is greater than the length of the vector.

##### [§](#examples-62)Examples

```rust
#![feature(deque_extend_front)]
use std::collections::VecDeque;

let mut characters = VecDeque::from(['a', 'b', 'c', 'd', 'e']);
characters.extend_from_within(2..);
assert_eq!(characters, ['a', 'b', 'c', 'd', 'e', 'c', 'd', 'e']);

let mut numbers = VecDeque::from([0, 1, 2, 3, 4]);
numbers.extend_from_within(..2);
assert_eq!(numbers, [0, 1, 2, 3, 4, 0, 1]);

let mut strings = VecDeque::from([String::from("hello"), String::from("world"), String::from("!")]);
strings.extend_from_within(1..=2);
assert_eq!(strings, ["hello", "world", "!", "world", "!"]);
```

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3384-3386)

🔬This is a nightly-only experimental API. (`deque_extend_front` [#146975](https://github.com/rust-lang/rust/issues/146975))

Clones the elements at the range `src` and prepends them to the front.

##### [§](#panics-15)Panics

Panics if the starting index is greater than the end index or if either index is greater than the length of the vector.

##### [§](#examples-63)Examples

```rust
#![feature(deque_extend_front)]
use std::collections::VecDeque;

let mut characters = VecDeque::from(['a', 'b', 'c', 'd', 'e']);
characters.prepend_from_within(2..);
assert_eq!(characters, ['c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']);

let mut numbers = VecDeque::from([0, 1, 2, 3, 4]);
numbers.prepend_from_within(..2);
assert_eq!(numbers, [0, 1, 0, 1, 2, 3, 4]);

let mut strings = VecDeque::from([String::from("hello"), String::from("world"), String::from("!")]);
strings.prepend_from_within(1..=2);
assert_eq!(strings, ["world", "!", "hello", "world", "!"]);
```

1.75.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#613-627)[§](#impl-BufRead-for-VecDeque%3Cu8,+A%3E)

BufRead is implemented for `VecDeque<u8>` by reading bytes from the front of the `VecDeque`.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#618-621)[§](#method.fill_buf)

Returns the contents of the “front” slice as returned by [`as_slices`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.as_slices "method std::collections::VecDeque::as_slices"). If the contained byte slices of the `VecDeque` are discontiguous, multiple calls to `fill_buf` will be needed to read the entire content.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#624-626)[§](#method.consume)

Marks the given `amount` of additional bytes from the internal buffer as having been read. Subsequent calls to `read` only return bytes that have not been marked as read. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#tymethod.consume)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2435-2437)[§](#method.has_data_left)

🔬This is a nightly-only experimental API. (`buf_read_has_data_left` [#86423](https://github.com/rust-lang/rust/issues/86423))

Checks if there is any data left to be `read`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.has_data_left)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2494-2496)[§](#method.read_until)

Reads all bytes into `buf` until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_until)

1.83.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2559-2561)[§](#method.skip_until)

Skips all bytes until the delimiter `byte` or EOF is reached. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.skip_until)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2627-2632)[§](#method.read_line)

Reads all bytes until a newline (the `0xA` byte) is reached, and append them to the provided `String` buffer. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2665-2670)[§](#method.split)

Returns an iterator over the contents of this reader split on the byte `byte`. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.split)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2702-2707)[§](#method.lines)

Returns an iterator over the lines of this reader. [Read more](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#119)[§](#impl-Clone-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#130)[§](#method.clone_from)

Overwrites the contents of `self` with a clone of the contents of `source`.

This method is preferred over simply assigning `source.clone()` to `self`, as it avoids reallocation if possible.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#120)[§](#method.clone)

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3729)[§](#impl-Debug-for-VecDeque%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#162)[§](#impl-Default-for-VecDeque%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#137)[§](#impl-Drop-for-VecDeque%3CT,+A%3E)

1.2.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3704)[§](#impl-Extend%3C%26T%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3705)[§](#method.extend-1)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3710)[§](#method.extend_one-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3715)[§](#method.extend_reserve-1)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3679)[§](#impl-Extend%3CT%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3680)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3685)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3690)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/std/iter/trait.Extend.html#method.extend_reserve)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3802)[§](#impl-From%3C%5BT;+N%5D%3E-for-VecDeque%3CT%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3812)[§](#method.from-2)

Converts a `[T; N]` into a `VecDeque<T>`.

```rust
use std::collections::VecDeque;

let deq1 = VecDeque::from([1, 2, 3, 4]);
let deq2: VecDeque<_> = [1, 2, 3, 4].into();
assert_eq!(deq1, deq2);
```

1.10.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3736)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3746)[§](#method.from)

Turn a [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") into a [`VecDeque<T>`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html "struct std::collections::VecDeque").

This conversion is guaranteed to run in *O*(1) time and to not re-allocate the `Vec`’s buffer or allocate any additional memory.

1.10.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3753)[§](#impl-From%3CVecDeque%3CT,+A%3E%3E-for-Vec%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3783)[§](#method.from-1)

Turn a [`VecDeque<T>`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html "struct std::collections::VecDeque") into a [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec").

This never needs to re-allocate, but does need to do *O*(*n*) data movement if the circular buffer doesn’t happen to be at the beginning of the allocation.

##### [§](#examples-64)Examples

```rust
use std::collections::VecDeque;

// This one is *O*(1).
let deque: VecDeque<_> = (1..5).collect();
let ptr = deque.as_slices().0.as_ptr();
let vec = Vec::from(deque);
assert_eq!(vec, [1, 2, 3, 4]);
assert_eq!(vec.as_ptr(), ptr);

// This one needs data rearranging.
let mut deque: VecDeque<_> = (1..5).collect();
deque.push_front(9);
deque.push_front(8);
let ptr = deque.as_slices().1.as_ptr();
let vec = Vec::from(deque);
assert_eq!(vec, [8, 9, 1, 2, 3, 4]);
assert_eq!(vec.as_ptr(), ptr);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3640)[§](#impl-FromIterator%3CT%3E-for-VecDeque%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3608)[§](#impl-Hash-for-VecDeque%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3622)[§](#impl-Index%3Cusize%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3623)[§](#associatedtype.Output)

The returned type after indexing.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3626)[§](#method.index)

Performs the indexing (`container[index]`) operation. [Read more](https://doc.rust-lang.org/std/ops/trait.Index.html#tymethod.index)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3632)[§](#impl-IndexMut%3Cusize%3E-for-VecDeque%3CT,+A%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3659)[§](#impl-IntoIterator-for-%26VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3660)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3661)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3663)[§](#method.into_iter-1)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3669)[§](#impl-IntoIterator-for-%26mut+VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3670)[§](#associatedtype.Item-2)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3671)[§](#associatedtype.IntoIter-2)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3673)[§](#method.into_iter-2)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3647)[§](#impl-IntoIterator-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3653)[§](#method.into_iter)

Consumes the deque into a front-to-back iterator yielding elements by value.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3648)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3649)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3600)[§](#impl-Ord-for-VecDeque%3CT,+A%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3586)[§](#impl-PartialEq%3C%26%5BU%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3586)[§](#method.eq-2)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-2)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3589)[§](#impl-PartialEq%3C%26%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3589)[§](#method.eq-5)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-5)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3587)[§](#impl-PartialEq%3C%26mut+%5BU%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3587)[§](#method.eq-3)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-3)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3590)[§](#impl-PartialEq%3C%26mut+%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3590)[§](#method.eq-6)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-6)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3588)[§](#impl-PartialEq%3C%5BU;+N%5D%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3588)[§](#method.eq-4)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-4)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3585)[§](#impl-PartialEq%3CVec%3CU,+A%3E%3E-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3585)[§](#method.eq-1)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne-1)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3544)[§](#impl-PartialEq-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3545)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3593)[§](#impl-PartialOrd-for-VecDeque%3CT,+A%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3594)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#522-609)[§](#impl-Read-for-VecDeque%3Cu8,+A%3E)

Read is implemented for `VecDeque<u8>` by consuming bytes from the front of the `VecDeque`.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#527-532)[§](#method.read)

Fill `buf` with the contents of the “front” slice as returned by [`as_slices`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html#method.as_slices "method std::collections::VecDeque::as_slices"). If the contained byte slices of the `VecDeque` are discontiguous, multiple calls to `read` will be needed to read the entire content.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#535-556)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#559-565)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#568-589)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_buf_exact)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#592-602)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#605-608)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_string)

1.36.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#825-827)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#838-840)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/std/io/trait.Read.html#method.is_read_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref)

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

1.63.0 · [Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#631-669)[§](#impl-Write-for-VecDeque%3Cu8,+A%3E)

Write is implemented for `VecDeque<u8>` by appending to the `VecDeque`, growing it as needed.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#633-636)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#639-646)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#649-651)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#654-657)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#660-663)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#666-668)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3583)[§](#impl-Eq-for-VecDeque%3CT,+A%3E)