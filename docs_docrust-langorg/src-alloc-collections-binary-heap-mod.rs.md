---
title: mod.rs - source
url: https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#326
source: crawler
fetched_at: 2026-05-06T21:36:21.370069945-03:00
rendered_js: false
word_count: 8965
summary: This document provides an overview of the BinaryHeap collection in Rust, explaining its priority queue functionality, performance characteristics, and usage patterns.
tags:
    - rust
    - binary-heap
    - priority-queue
    - data-structures
    - collection-types
category: reference
---

## alloc/collections/binary\_heap/ mod.rs

````rust
1//! A priority queue implemented with a binary heap.
2//!
3//! Insertion and popping the largest element have *O*(log(*n*)) time complexity.
4//! Checking the largest element is *O*(1). Converting a vector to a binary heap
5//! can be done in-place, and has *O*(*n*) complexity. A binary heap can also be
6//! converted to a sorted vector in-place, allowing it to be used for an *O*(*n* * log(*n*))
7//! in-place heapsort.
8//!
9//! # Examples
10//!
11//! This is a larger example that implements [Dijkstra's algorithm][dijkstra]
12//! to solve the [shortest path problem][sssp] on a [directed graph][dir_graph].
13//! It shows how to use [`BinaryHeap`] with custom types.
14//!
15//! [dijkstra]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
16//! [sssp]: https://en.wikipedia.org/wiki/Shortest_path_problem
17//! [dir_graph]: https://en.wikipedia.org/wiki/Directed_graph
18//!
19//! ```
20//! use std::cmp::Ordering;
21//! use std::collections::BinaryHeap;
22//!
23//! #[derive(Copy, Clone, Eq, PartialEq)]
24//! struct State {
25//!     cost: usize,
26//!     position: usize,
27//! }
28//!
29//! // The priority queue depends on `Ord`.
30//! // Explicitly implement the trait so the queue becomes a min-heap
31//! // instead of a max-heap.
32//! impl Ord for State {
33//!     fn cmp(&self, other: &Self) -> Ordering {
34//!         // Notice that we flip the ordering on costs.
35//!         // In case of a tie we compare positions - this step is necessary
36//!         // to make implementations of `PartialEq` and `Ord` consistent.
37//!         other.cost.cmp(&self.cost)
38//!             .then_with(|| self.position.cmp(&other.position))
39//!     }
40//! }
41//!
42//! // `PartialOrd` needs to be implemented as well.
43//! impl PartialOrd for State {
44//!     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
45//!         Some(self.cmp(other))
46//!     }
47//! }
48//!
49//! // Each node is represented as a `usize`, for a shorter implementation.
50//! struct Edge {
51//!     node: usize,
52//!     cost: usize,
53//! }
54//!
55//! // Dijkstra's shortest path algorithm.
56//!
57//! // Start at `start` and use `dist` to track the current shortest distance
58//! // to each node. This implementation isn't memory-efficient as it may leave duplicate
59//! // nodes in the queue. It also uses `usize::MAX` as a sentinel value,
60//! // for a simpler implementation.
61//! fn shortest_path(adj_list: &Vec<Vec<Edge>>, start: usize, goal: usize) -> Option<usize> {
62//!     // dist[node] = current shortest distance from `start` to `node`
63//!     let mut dist: Vec<_> = (0..adj_list.len()).map(|_| usize::MAX).collect();
64//!
65//!     let mut heap = BinaryHeap::new();
66//!
67//!     // We're at `start`, with a zero cost
68//!     dist[start] = 0;
69//!     heap.push(State { cost: 0, position: start });
70//!
71//!     // Examine the frontier with lower cost nodes first (min-heap)
72//!     while let Some(State { cost, position }) = heap.pop() {
73//!         // Alternatively we could have continued to find all shortest paths
74//!         if position == goal { return Some(cost); }
75//!
76//!         // Important as we may have already found a better way
77//!         if cost > dist[position] { continue; }
78//!
79//!         // For each node we can reach, see if we can find a way with
80//!         // a lower cost going through this node
81//!         for edge in &adj_list[position] {
82//!             let next = State { cost: cost + edge.cost, position: edge.node };
83//!
84//!             // If so, add it to the frontier and continue
85//!             if next.cost < dist[next.position] {
86//!                 heap.push(next);
87//!                 // Relaxation, we have now found a better way
88//!                 dist[next.position] = next.cost;
89//!             }
90//!         }
91//!     }
92//!
93//!     // Goal not reachable
94//!     None
95//! }
96//!
97//! fn main() {
98//!     // This is the directed graph we're going to use.
99//!     // The node numbers correspond to the different states,
100//!     // and the edge weights symbolize the cost of moving
101//!     // from one node to another.
102//!     // Note that the edges are one-way.
103//!     //
104//!     //                  7
105//!     //          +-----------------+
106//!     //          |                 |
107//!     //          v   1        2    |  2
108//!     //          0 -----> 1 -----> 3 ---> 4
109//!     //          |        ^        ^      ^
110//!     //          |        | 1      |      |
111//!     //          |        |        | 3    | 1
112//!     //          +------> 2 -------+      |
113//!     //           10      |               |
114//!     //                   +---------------+
115//!     //
116//!     // The graph is represented as an adjacency list where each index,
117//!     // corresponding to a node value, has a list of outgoing edges.
118//!     // Chosen for its efficiency.
119//!     let graph = vec![
120//!         // Node 0
121//!         vec![Edge { node: 2, cost: 10 },
122//!              Edge { node: 1, cost: 1 }],
123//!         // Node 1
124//!         vec![Edge { node: 3, cost: 2 }],
125//!         // Node 2
126//!         vec![Edge { node: 1, cost: 1 },
127//!              Edge { node: 3, cost: 3 },
128//!              Edge { node: 4, cost: 1 }],
129//!         // Node 3
130//!         vec![Edge { node: 0, cost: 7 },
131//!              Edge { node: 4, cost: 2 }],
132//!         // Node 4
133//!         vec![]];
134//!
135//!     assert_eq!(shortest_path(&graph, 0, 1), Some(1));
136//!     assert_eq!(shortest_path(&graph, 0, 3), Some(3));
137//!     assert_eq!(shortest_path(&graph, 3, 0), Some(7));
138//!     assert_eq!(shortest_path(&graph, 0, 4), Some(5));
139//!     assert_eq!(shortest_path(&graph, 4, 0), None);
140//! }
141//! ```
142
143#![allow(missing_docs)]
144#![stable(feature = "rust1", since = "1.0.0")]
145
146use core::alloc::Allocator;
147use core::iter::{FusedIterator, InPlaceIterable, SourceIter, TrustedFused, TrustedLen};
148use core::mem::{self, ManuallyDrop, swap};
149use core::num::NonZero;
150use core::ops::{Deref, DerefMut};
151use core::{fmt, ptr};
152
153use crate::alloc::Global;
154use crate::collections::TryReserveError;
155use crate::slice;
156#[cfg(not(test))]
157use crate::vec::AsVecIntoIter;
158use crate::vec::{self, Vec};
159
160/// A priority queue implemented with a binary heap.
161///
162/// This will be a max-heap.
163///
164/// It is a logic error for an item to be modified in such a way that the
165/// item's ordering relative to any other item, as determined by the [`Ord`]
166/// trait, changes while it is in the heap. This is normally only possible
167/// through interior mutability, global state, I/O, or unsafe code. The
168/// behavior resulting from such a logic error is not specified, but will
169/// be encapsulated to the `BinaryHeap` that observed the logic error and not
170/// result in undefined behavior. This could include panics, incorrect results,
171/// aborts, memory leaks, and non-termination.
172///
173/// As long as no elements change their relative order while being in the heap
174/// as described above, the API of `BinaryHeap` guarantees that the heap
175/// invariant remains intact i.e. its methods all behave as documented. For
176/// example if a method is documented as iterating in sorted order, that's
177/// guaranteed to work as long as elements in the heap have not changed order,
178/// even in the presence of closures getting unwinded out of, iterators getting
179/// leaked, and similar foolishness.
180///
181/// # Examples
182///
183/// ```
184/// use std::collections::BinaryHeap;
185///
186/// // Type inference lets us omit an explicit type signature (which
187/// // would be `BinaryHeap<i32>` in this example).
188/// let mut heap = BinaryHeap::new();
189///
190/// // We can use peek to look at the next item in the heap. In this case,
191/// // there's no items in there yet so we get None.
192/// assert_eq!(heap.peek(), None);
193///
194/// // Let's add some scores...
195/// heap.push(1);
196/// heap.push(5);
197/// heap.push(2);
198///
199/// // Now peek shows the most important item in the heap.
200/// assert_eq!(heap.peek(), Some(&5));
201///
202/// // We can check the length of a heap.
203/// assert_eq!(heap.len(), 3);
204///
205/// // We can iterate over the items in the heap, although they are returned in
206/// // a random order.
207/// for x in &heap {
208///     println!("{x}");
209/// }
210///
211/// // If we instead pop these scores, they should come back in order.
212/// assert_eq!(heap.pop(), Some(5));
213/// assert_eq!(heap.pop(), Some(2));
214/// assert_eq!(heap.pop(), Some(1));
215/// assert_eq!(heap.pop(), None);
216///
217/// // We can clear the heap of any remaining items.
218/// heap.clear();
219///
220/// // The heap should now be empty.
221/// assert!(heap.is_empty())
222/// ```
223///
224/// A `BinaryHeap` with a known list of items can be initialized from an array:
225///
226/// ```
227/// use std::collections::BinaryHeap;
228///
229/// let heap = BinaryHeap::from([1, 5, 2]);
230/// ```
231///
232/// ## Min-heap
233///
234/// Either [`core::cmp::Reverse`] or a custom [`Ord`] implementation can be used to
235/// make `BinaryHeap` a min-heap. This makes `heap.pop()` return the smallest
236/// value instead of the greatest one.
237///
238/// ```
239/// use std::collections::BinaryHeap;
240/// use std::cmp::Reverse;
241///
242/// let mut heap = BinaryHeap::new();
243///
244/// // Wrap values in `Reverse`
245/// heap.push(Reverse(1));
246/// heap.push(Reverse(5));
247/// heap.push(Reverse(2));
248///
249/// // If we pop these scores now, they should come back in the reverse order.
250/// assert_eq!(heap.pop(), Some(Reverse(1)));
251/// assert_eq!(heap.pop(), Some(Reverse(2)));
252/// assert_eq!(heap.pop(), Some(Reverse(5)));
253/// assert_eq!(heap.pop(), None);
254/// ```
255///
256/// # Time complexity
257///
258/// | [push]  | [pop]         | [peek]/[peek\_mut] |
259/// |---------|---------------|--------------------|
260/// | *O*(1)~ | *O*(log(*n*)) | *O*(1)             |
261///
262/// The value for `push` is an expected cost; the method documentation gives a
263/// more detailed analysis.
264///
265/// [`core::cmp::Reverse`]: core::cmp::Reverse
266/// [`Cell`]: core::cell::Cell
267/// [`RefCell`]: core::cell::RefCell
268/// [push]: BinaryHeap::push
269/// [pop]: BinaryHeap::pop
270/// [peek]: BinaryHeap::peek
271/// [peek\_mut]: BinaryHeap::peek_mut
272#[stable(feature = "rust1", since = "1.0.0")]
273#[cfg_attr(not(test), rustc_diagnostic_item = "BinaryHeap")]
274pub struct BinaryHeap<
275    T,
276    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
277> {
278    data: Vec<T, A>,
279}
280
281/// Structure wrapping a mutable reference to the greatest item on a
282/// `BinaryHeap`.
283///
284/// This `struct` is created by the [`peek_mut`] method on [`BinaryHeap`]. See
285/// its documentation for more.
286///
287/// [`peek_mut`]: BinaryHeap::peek_mut
288#[stable(feature = "binary_heap_peek_mut", since = "1.12.0")]
289pub struct PeekMut<
290    'a,
291    T: 'a + Ord,
292    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
293> {
294    heap: &'a mut BinaryHeap<T, A>,
295    // If a set_len + sift_down are required, this is Some. If a &mut T has not
296    // yet been exposed to peek_mut()'s caller, it's None.
297    original_len: Option<NonZero<usize>>,
298}
299
300#[stable(feature = "collection_debug", since = "1.17.0")]
301impl<T: Ord + fmt::Debug, A: Allocator> fmt::Debug for PeekMut<'_, T, A> {
302    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
303        f.debug_tuple("PeekMut").field(&self.heap.data[0]).finish()
304    }
305}
306
307#[stable(feature = "binary_heap_peek_mut", since = "1.12.0")]
308impl<T: Ord, A: Allocator> Drop for PeekMut<'_, T, A> {
309    fn drop(&mut self) {
310        if let Some(original_len) = self.original_len {
311            // SAFETY: That's how many elements were in the Vec at the time of
312            // the PeekMut::deref_mut call, and therefore also at the time of
313            // the BinaryHeap::peek_mut call. Since the PeekMut did not end up
314            // getting leaked, we are now undoing the leak amplification that
315            // the DerefMut prepared for.
316            unsafe { self.heap.data.set_len(original_len.get()) };
317
318            // SAFETY: PeekMut is only instantiated for non-empty heaps.
319            unsafe { self.heap.sift_down(0) };
320        }
321    }
322}
323
324#[stable(feature = "binary_heap_peek_mut", since = "1.12.0")]
325impl<T: Ord, A: Allocator> Deref for PeekMut<'_, T, A> {
326    type Target = T;
327    fn deref(&self) -> &T {
328        debug_assert!(!self.heap.is_empty());
329        // SAFE: PeekMut is only instantiated for non-empty heaps
330        unsafe { self.heap.data.get_unchecked(0) }
331    }
332}
333
334#[stable(feature = "binary_heap_peek_mut", since = "1.12.0")]
335impl<T: Ord, A: Allocator> DerefMut for PeekMut<'_, T, A> {
336    fn deref_mut(&mut self) -> &mut T {
337        debug_assert!(!self.heap.is_empty());
338
339        let len = self.heap.len();
340        if len > 1 {
341            // Here we preemptively leak all the rest of the underlying vector
342            // after the currently max element. If the caller mutates the &mut T
343            // we're about to give them, and then leaks the PeekMut, all these
344            // elements will remain leaked. If they don't leak the PeekMut, then
345            // either Drop or PeekMut::pop will un-leak the vector elements.
346            //
347            // This is technique is described throughout several other places in
348            // the standard library as "leak amplification".
349            unsafe {
350                // SAFETY: len > 1 so len != 0.
351                self.original_len = Some(NonZero::new_unchecked(len));
352                // SAFETY: len > 1 so all this does for now is leak elements,
353                // which is safe.
354                self.heap.data.set_len(1);
355            }
356        }
357
358        // SAFE: PeekMut is only instantiated for non-empty heaps
359        unsafe { self.heap.data.get_unchecked_mut(0) }
360    }
361}
362
363impl<'a, T: Ord, A: Allocator> PeekMut<'a, T, A> {
364    /// Sifts the current element to its new position.
365    ///
366    /// Afterwards refers to the new element. Returns if the element changed.
367    ///
368    /// ## Examples
369    ///
370    /// The condition can be used to upper bound all elements in the heap. When only few elements
371    /// are affected, the heap's sort ensures this is faster than a reconstruction from the raw
372    /// element list and requires no additional allocation.
373    ///
374    /// ```
375    /// #![feature(binary_heap_peek_mut_refresh)]
376    /// use std::collections::BinaryHeap;
377    ///
378    /// let mut heap: BinaryHeap<u32> = (0..128).collect();
379    /// let mut peek = heap.peek_mut().unwrap();
380    ///
381    /// loop {
382    ///     *peek = 99;
383    ///
384    ///     if !peek.refresh() {
385    ///         break;
386    ///     }
387    /// }
388    ///
389    /// // Post condition, this is now an upper bound.
390    /// assert!(*peek < 100);
391    /// ```
392    ///
393    /// When the element remains the maximum after modification, the peek remains unchanged:
394    ///
395    /// ```
396    /// #![feature(binary_heap_peek_mut_refresh)]
397    /// use std::collections::BinaryHeap;
398    ///
399    /// let mut heap: BinaryHeap<u32> = [1, 2, 3].into();
400    /// let mut peek = heap.peek_mut().unwrap();
401    ///
402    /// assert_eq!(*peek, 3);
403    /// *peek = 42;
404    ///
405    /// // When we refresh, the peek is updated to the new maximum.
406    /// assert!(!peek.refresh(), "42 is even larger than 3");
407    /// assert_eq!(*peek, 42);
408    /// ```
409    #[unstable(feature = "binary_heap_peek_mut_refresh", issue = "138355")]
410    #[must_use = "is equivalent to dropping and getting a new PeekMut except for return information"]
411    pub fn refresh(&mut self) -> bool {
412        // The length of the underlying heap is unchanged by sifting down. The value stored for leak
413        // amplification thus remains accurate. We erase the leak amplification firstly because the
414        // operation is then equivalent to constructing a new PeekMut and secondly this avoids any
415        // future complication where original_len being non-empty would be interpreted as the heap
416        // having been leak amplified instead of checking the heap itself.
417        if let Some(original_len) = self.original_len.take() {
418            // SAFETY: This is how many elements were in the Vec at the time of
419            // the BinaryHeap::peek_mut call.
420            unsafe { self.heap.data.set_len(original_len.get()) };
421
422            // The length of the heap did not change by sifting, upholding our own invariants.
423
424            // SAFETY: PeekMut is only instantiated for non-empty heaps.
425            (unsafe { self.heap.sift_down(0) }) != 0
426        } else {
427            // The element was not modified.
428            false
429        }
430    }
431
432    /// Removes the peeked value from the heap and returns it.
433    #[stable(feature = "binary_heap_peek_mut_pop", since = "1.18.0")]
434    pub fn pop(mut this: PeekMut<'a, T, A>) -> T {
435        if let Some(original_len) = this.original_len.take() {
436            // SAFETY: This is how many elements were in the Vec at the time of
437            // the BinaryHeap::peek_mut call.
438            unsafe { this.heap.data.set_len(original_len.get()) };
439
440            // Unlike in Drop, here we don't also need to do a sift_down even if
441            // the caller could've mutated the element. It is removed from the
442            // heap on the next line and pop() is not sensitive to its value.
443        }
444
445        // SAFETY: Have a `PeekMut` element proves that the associated binary heap being non-empty,
446        // so the `pop` operation will not fail.
447        unsafe { this.heap.pop().unwrap_unchecked() }
448    }
449}
450
451#[stable(feature = "rust1", since = "1.0.0")]
452impl<T: Clone, A: Allocator + Clone> Clone for BinaryHeap<T, A> {
453    fn clone(&self) -> Self {
454        BinaryHeap { data: self.data.clone() }
455    }
456
457    /// Overwrites the contents of `self` with a clone of the contents of `source`.
458    ///
459    /// This method is preferred over simply assigning `source.clone()` to `self`,
460    /// as it avoids reallocation if possible.
461    ///
462    /// See [`Vec::clone_from()`] for more details.
463    fn clone_from(&mut self, source: &Self) {
464        self.data.clone_from(&source.data);
465    }
466}
467
468#[stable(feature = "rust1", since = "1.0.0")]
469impl<T> Default for BinaryHeap<T> {
470    /// Creates an empty `BinaryHeap<T>`.
471    #[inline]
472    fn default() -> BinaryHeap<T> {
473        BinaryHeap::new()
474    }
475}
476
477#[stable(feature = "binaryheap_debug", since = "1.4.0")]
478impl<T: fmt::Debug, A: Allocator> fmt::Debug for BinaryHeap<T, A> {
479    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
480        f.debug_list().entries(self.iter()).finish()
481    }
482}
483
484struct RebuildOnDrop<
485    'a,
486    T: Ord,
487    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
488> {
489    heap: &'a mut BinaryHeap<T, A>,
490    rebuild_from: usize,
491}
492
493impl<T: Ord, A: Allocator> Drop for RebuildOnDrop<'_, T, A> {
494    fn drop(&mut self) {
495        self.heap.rebuild_tail(self.rebuild_from);
496    }
497}
498
499impl<T> BinaryHeap<T> {
500    /// Creates an empty `BinaryHeap` as a max-heap.
501    ///
502    /// # Examples
503    ///
504    /// Basic usage:
505    ///
506    /// ```
507    /// use std::collections::BinaryHeap;
508    /// let mut heap = BinaryHeap::new();
509    /// heap.push(4);
510    /// ```
511    #[stable(feature = "rust1", since = "1.0.0")]
512    #[rustc_const_stable(feature = "const_binary_heap_constructor", since = "1.80.0")]
513    #[must_use]
514    pub const fn new() -> BinaryHeap<T> {
515        BinaryHeap { data: vec![] }
516    }
517
518    /// Creates an empty `BinaryHeap` with at least the specified capacity.
519    ///
520    /// The binary heap will be able to hold at least `capacity` elements without
521    /// reallocating. This method is allowed to allocate for more elements than
522    /// `capacity`. If `capacity` is zero, the binary heap will not allocate.
523    ///
524    /// # Examples
525    ///
526    /// Basic usage:
527    ///
528    /// ```
529    /// use std::collections::BinaryHeap;
530    /// let mut heap = BinaryHeap::with_capacity(10);
531    /// heap.push(4);
532    /// ```
533    #[stable(feature = "rust1", since = "1.0.0")]
534    #[must_use]
535    pub fn with_capacity(capacity: usize) -> BinaryHeap<T> {
536        BinaryHeap { data: Vec::with_capacity(capacity) }
537    }
538}
539
540impl<T, A: Allocator> BinaryHeap<T, A> {
541    /// Creates an empty `BinaryHeap` as a max-heap, using `A` as allocator.
542    ///
543    /// # Examples
544    ///
545    /// Basic usage:
546    ///
547    /// ```
548    /// #![feature(allocator_api)]
549    ///
550    /// use std::alloc::System;
551    /// use std::collections::BinaryHeap;
552    /// let mut heap = BinaryHeap::new_in(System);
553    /// heap.push(4);
554    /// ```
555    #[unstable(feature = "allocator_api", issue = "32838")]
556    #[must_use]
557    pub const fn new_in(alloc: A) -> BinaryHeap<T, A> {
558        BinaryHeap { data: Vec::new_in(alloc) }
559    }
560
561    /// Creates an empty `BinaryHeap` with at least the specified capacity, using `A` as allocator.
562    ///
563    /// The binary heap will be able to hold at least `capacity` elements without
564    /// reallocating. This method is allowed to allocate for more elements than
565    /// `capacity`. If `capacity` is zero, the binary heap will not allocate.
566    ///
567    /// # Examples
568    ///
569    /// Basic usage:
570    ///
571    /// ```
572    /// #![feature(allocator_api)]
573    ///
574    /// use std::alloc::System;
575    /// use std::collections::BinaryHeap;
576    /// let mut heap = BinaryHeap::with_capacity_in(10, System);
577    /// heap.push(4);
578    /// ```
579    #[unstable(feature = "allocator_api", issue = "32838")]
580    #[must_use]
581    pub fn with_capacity_in(capacity: usize, alloc: A) -> BinaryHeap<T, A> {
582        BinaryHeap { data: Vec::with_capacity_in(capacity, alloc) }
583    }
584
585    /// Creates a `BinaryHeap` using the supplied `vec`. This does not rebuild the heap,
586    /// so `vec` must already be a max-heap.
587    ///
588    /// # Safety
589    ///
590    /// The supplied `vec` must be a max-heap, i.e. for all indices `0 < i < vec.len()`,
591    /// `vec[(i - 1) / 2] >= vec[i]`.
592    ///
593    /// # Examples
594    ///
595    /// Basic usage:
596    ///
597    /// ```
598    /// #![feature(binary_heap_from_raw_vec)]
599    ///
600    /// use std::collections::BinaryHeap;
601    /// let heap = BinaryHeap::from([1, 2, 3]);
602    /// let vec = heap.into_vec();
603    ///
604    /// // Safety: vec is the output of heap.from_vec(), so is a max-heap.
605    /// let mut new_heap = unsafe {
606    ///     BinaryHeap::from_raw_vec(vec)
607    /// };
608    /// assert_eq!(new_heap.pop(), Some(3));
609    /// assert_eq!(new_heap.pop(), Some(2));
610    /// assert_eq!(new_heap.pop(), Some(1));
611    /// assert_eq!(new_heap.pop(), None);
612    /// ```
613    #[unstable(feature = "binary_heap_from_raw_vec", issue = "152500")]
614    #[must_use]
615    pub unsafe fn from_raw_vec(vec: Vec<T, A>) -> BinaryHeap<T, A> {
616        BinaryHeap { data: vec }
617    }
618}
619
620impl<T: Ord, A: Allocator> BinaryHeap<T, A> {
621    /// Returns a mutable reference to the greatest item in the binary heap, or
622    /// `None` if it is empty.
623    ///
624    /// Note: If the `PeekMut` value is leaked, some heap elements might get
625    /// leaked along with it, but the remaining elements will remain a valid
626    /// heap.
627    ///
628    /// # Examples
629    ///
630    /// Basic usage:
631    ///
632    /// ```
633    /// use std::collections::BinaryHeap;
634    /// let mut heap = BinaryHeap::new();
635    /// assert!(heap.peek_mut().is_none());
636    ///
637    /// heap.push(1);
638    /// heap.push(5);
639    /// heap.push(2);
640    /// if let Some(mut val) = heap.peek_mut() {
641    ///     *val = 0;
642    /// }
643    /// assert_eq!(heap.peek(), Some(&2));
644    /// ```
645    ///
646    /// # Time complexity
647    ///
648    /// If the item is modified then the worst case time complexity is *O*(log(*n*)),
649    /// otherwise it's *O*(1).
650    #[stable(feature = "binary_heap_peek_mut", since = "1.12.0")]
651    pub fn peek_mut(&mut self) -> Option<PeekMut<'_, T, A>> {
652        if self.is_empty() { None } else { Some(PeekMut { heap: self, original_len: None }) }
653    }
654
655    /// Removes the greatest item from the binary heap and returns it, or `None` if it
656    /// is empty.
657    ///
658    /// # Examples
659    ///
660    /// Basic usage:
661    ///
662    /// ```
663    /// use std::collections::BinaryHeap;
664    /// let mut heap = BinaryHeap::from([1, 3]);
665    ///
666    /// assert_eq!(heap.pop(), Some(3));
667    /// assert_eq!(heap.pop(), Some(1));
668    /// assert_eq!(heap.pop(), None);
669    /// ```
670    ///
671    /// # Time complexity
672    ///
673    /// The worst case cost of `pop` on a heap containing *n* elements is *O*(log(*n*)).
674    #[stable(feature = "rust1", since = "1.0.0")]
675    pub fn pop(&mut self) -> Option<T> {
676        self.data.pop().map(|mut item| {
677            if !self.is_empty() {
678                swap(&mut item, &mut self.data[0]);
679                // SAFETY: !self.is_empty() means that self.len() > 0
680                unsafe { self.sift_down_to_bottom(0) };
681            }
682            item
683        })
684    }
685
686    /// Removes and returns the greatest item from the binary heap if the predicate
687    /// returns `true`, or [`None`] if the predicate returns false or the heap
688    /// is empty (the predicate will not be called in that case).
689    ///
690    /// # Examples
691    ///
692    /// ```
693    /// #![feature(binary_heap_pop_if)]
694    /// use std::collections::BinaryHeap;
695    /// let mut heap = BinaryHeap::from([1, 2]);
696    /// let pred = |x: &i32| *x % 2 == 0;
697    ///
698    /// assert_eq!(heap.pop_if(pred), Some(2));
699    /// assert_eq!(heap.as_slice(), [1]);
700    /// assert_eq!(heap.pop_if(pred), None);
701    /// assert_eq!(heap.as_slice(), [1]);
702    /// ```
703    ///
704    /// # Time complexity
705    ///
706    /// The worst case cost of `pop_if` on a heap containing *n* elements is *O*(log(*n*)).
707    #[unstable(feature = "binary_heap_pop_if", issue = "151828")]
708    pub fn pop_if(&mut self, predicate: impl FnOnce(&T) -> bool) -> Option<T> {
709        let first = self.peek()?;
710        if predicate(first) { self.pop() } else { None }
711    }
712
713    /// Pushes an item onto the binary heap.
714    ///
715    /// # Examples
716    ///
717    /// Basic usage:
718    ///
719    /// ```
720    /// use std::collections::BinaryHeap;
721    /// let mut heap = BinaryHeap::new();
722    /// heap.push(3);
723    /// heap.push(5);
724    /// heap.push(1);
725    ///
726    /// assert_eq!(heap.len(), 3);
727    /// assert_eq!(heap.peek(), Some(&5));
728    /// ```
729    ///
730    /// # Time complexity
731    ///
732    /// The expected cost of `push`, averaged over every possible ordering of
733    /// the elements being pushed, and over a sufficiently large number of
734    /// pushes, is *O*(1). This is the most meaningful cost metric when pushing
735    /// elements that are *not* already in any sorted pattern.
736    ///
737    /// The time complexity degrades if elements are pushed in predominantly
738    /// ascending order. In the worst case, elements are pushed in ascending
739    /// sorted order and the amortized cost per push is *O*(log(*n*)) against a heap
740    /// containing *n* elements.
741    ///
742    /// The worst case cost of a *single* call to `push` is *O*(*n*). The worst case
743    /// occurs when capacity is exhausted and needs a resize. The resize cost
744    /// has been amortized in the previous figures.
745    #[stable(feature = "rust1", since = "1.0.0")]
746    #[rustc_confusables("append", "put")]
747    pub fn push(&mut self, item: T) {
748        let old_len = self.len();
749        self.data.push(item);
750        // SAFETY: Since we pushed a new item it means that
751        //  old_len = self.len() - 1 < self.len()
752        unsafe { self.sift_up(0, old_len) };
753    }
754
755    /// Consumes the `BinaryHeap` and returns a vector in sorted
756    /// (ascending) order.
757    ///
758    /// # Examples
759    ///
760    /// Basic usage:
761    ///
762    /// ```
763    /// use std::collections::BinaryHeap;
764    ///
765    /// let mut heap = BinaryHeap::from([1, 2, 4, 5, 7]);
766    /// heap.push(6);
767    /// heap.push(3);
768    ///
769    /// let vec = heap.into_sorted_vec();
770    /// assert_eq!(vec, [1, 2, 3, 4, 5, 6, 7]);
771    /// ```
772    #[must_use = "`self` will be dropped if the result is not used"]
773    #[stable(feature = "binary_heap_extras_15", since = "1.5.0")]
774    pub fn into_sorted_vec(mut self) -> Vec<T, A> {
775        let mut end = self.len();
776        while end > 1 {
777            end -= 1;
778            // SAFETY: `end` goes from `self.len() - 1` to 1 (both included),
779            //  so it's always a valid index to access.
780            //  It is safe to access index 0 (i.e. `ptr`), because
781            //  1 <= end < self.len(), which means self.len() >= 2.
782            unsafe {
783                let ptr = self.data.as_mut_ptr();
784                ptr::swap(ptr, ptr.add(end));
785            }
786            // SAFETY: `end` goes from `self.len() - 1` to 1 (both included) so:
787            //  0 < 1 <= end <= self.len() - 1 < self.len()
788            //  Which means 0 < end and end < self.len().
789            unsafe { self.sift_down_range(0, end) };
790        }
791        self.into_vec()
792    }
793
794    // The implementations of sift_up and sift_down use unsafe blocks in
795    // order to move an element out of the vector (leaving behind a
796    // hole), shift along the others and move the removed element back into the
797    // vector at the final location of the hole.
798    // The `Hole` type is used to represent this, and make sure
799    // the hole is filled back at the end of its scope, even on panic.
800    // Using a hole reduces the constant factor compared to using swaps,
801    // which involves twice as many moves.
802
803    /// # Safety
804    ///
805    /// The caller must guarantee that `pos < self.len()`.
806    ///
807    /// Returns the new position of the element.
808    unsafe fn sift_up(&mut self, start: usize, pos: usize) -> usize {
809        // Take out the value at `pos` and create a hole.
810        // SAFETY: The caller guarantees that pos < self.len()
811        let mut hole = unsafe { Hole::new(&mut self.data, pos) };
812
813        while hole.pos() > start {
814            let parent = (hole.pos() - 1) / 2;
815
816            // SAFETY: hole.pos() > start >= 0, which means hole.pos() > 0
817            //  and so hole.pos() - 1 can't underflow.
818            //  This guarantees that parent < hole.pos() so
819            //  it's a valid index and also != hole.pos().
820            if hole.element() <= unsafe { hole.get(parent) } {
821                break;
822            }
823
824            // SAFETY: Same as above
825            unsafe { hole.move_to(parent) };
826        }
827
828        hole.pos()
829    }
830
831    /// Take an element at `pos` and move it down the heap,
832    /// while its children are larger.
833    ///
834    /// Returns the new position of the element.
835    ///
836    /// # Safety
837    ///
838    /// The caller must guarantee that `pos < end <= self.len()`.
839    unsafe fn sift_down_range(&mut self, pos: usize, end: usize) -> usize {
840        // SAFETY: The caller guarantees that pos < end <= self.len().
841        let mut hole = unsafe { Hole::new(&mut self.data, pos) };
842        let mut child = 2 * hole.pos() + 1;
843
844        // Loop invariant: child == 2 * hole.pos() + 1.
845        while child <= end.saturating_sub(2) {
846            // compare with the greater of the two children
847            // SAFETY: child < end - 1 < self.len() and
848            //  child + 1 < end <= self.len(), so they're valid indexes.
849            //  child == 2 * hole.pos() + 1 != hole.pos() and
850            //  child + 1 == 2 * hole.pos() + 2 != hole.pos().
851            // FIXME: 2 * hole.pos() + 1 or 2 * hole.pos() + 2 could overflow
852            //  if T is a ZST
853            child += unsafe { hole.get(child) <= hole.get(child + 1) } as usize;
854
855            // if we are already in order, stop.
856            // SAFETY: child is now either the old child or the old child+1
857            //  We already proven that both are < self.len() and != hole.pos()
858            if hole.element() >= unsafe { hole.get(child) } {
859                return hole.pos();
860            }
861
862            // SAFETY: same as above.
863            unsafe { hole.move_to(child) };
864            child = 2 * hole.pos() + 1;
865        }
866
867        // SAFETY: && short circuit, which means that in the
868        //  second condition it's already true that child == end - 1 < self.len().
869        if child == end - 1 && hole.element() < unsafe { hole.get(child) } {
870            // SAFETY: child is already proven to be a valid index and
871            //  child == 2 * hole.pos() + 1 != hole.pos().
872            unsafe { hole.move_to(child) };
873        }
874
875        hole.pos()
876    }
877
878    /// # Safety
879    ///
880    /// The caller must guarantee that `pos < self.len()`.
881    unsafe fn sift_down(&mut self, pos: usize) -> usize {
882        let len = self.len();
883        // SAFETY: pos < len is guaranteed by the caller and
884        //  obviously len = self.len() <= self.len().
885        unsafe { self.sift_down_range(pos, len) }
886    }
887
888    /// Take an element at `pos` and move it all the way down the heap,
889    /// then sift it up to its position.
890    ///
891    /// Note: This is faster when the element is known to be large / should
892    /// be closer to the bottom.
893    ///
894    /// # Safety
895    ///
896    /// The caller must guarantee that `pos < self.len()`.
897    unsafe fn sift_down_to_bottom(&mut self, mut pos: usize) {
898        let end = self.len();
899        let start = pos;
900
901        // SAFETY: The caller guarantees that pos < self.len().
902        let mut hole = unsafe { Hole::new(&mut self.data, pos) };
903        let mut child = 2 * hole.pos() + 1;
904
905        // Loop invariant: child == 2 * hole.pos() + 1.
906        while child <= end.saturating_sub(2) {
907            // SAFETY: child < end - 1 < self.len() and
908            //  child + 1 < end <= self.len(), so they're valid indexes.
909            //  child == 2 * hole.pos() + 1 != hole.pos() and
910            //  child + 1 == 2 * hole.pos() + 2 != hole.pos().
911            // FIXME: 2 * hole.pos() + 1 or 2 * hole.pos() + 2 could overflow
912            //  if T is a ZST
913            child += unsafe { hole.get(child) <= hole.get(child + 1) } as usize;
914
915            // SAFETY: Same as above
916            unsafe { hole.move_to(child) };
917            child = 2 * hole.pos() + 1;
918        }
919
920        if child == end - 1 {
921            // SAFETY: child == end - 1 < self.len(), so it's a valid index
922            //  and child == 2 * hole.pos() + 1 != hole.pos().
923            unsafe { hole.move_to(child) };
924        }
925        pos = hole.pos();
926        drop(hole);
927
928        // SAFETY: pos is the position in the hole and was already proven
929        //  to be a valid index.
930        unsafe { self.sift_up(start, pos) };
931    }
932
933    /// Rebuild assuming data[0..start] is still a proper heap.
934    fn rebuild_tail(&mut self, start: usize) {
935        if start == self.len() {
936            return;
937        }
938
939        let tail_len = self.len() - start;
940
941        #[inline(always)]
942        fn log2_fast(x: usize) -> usize {
943            (usize::BITS - x.leading_zeros() - 1) as usize
944        }
945
946        // `rebuild` takes O(self.len()) operations
947        // and about 2 * self.len() comparisons in the worst case
948        // while repeating `sift_up` takes O(tail_len * log(start)) operations
949        // and about 1 * tail_len * log_2(start) comparisons in the worst case,
950        // assuming start >= tail_len. For larger heaps, the crossover point
951        // no longer follows this reasoning and was determined empirically.
952        let better_to_rebuild = if start < tail_len {
953            true
954        } else if self.len() <= 2048 {
955            2 * self.len() < tail_len * log2_fast(start)
956        } else {
957            2 * self.len() < tail_len * 11
958        };
959
960        if better_to_rebuild {
961            self.rebuild();
962        } else {
963            for i in start..self.len() {
964                // SAFETY: The index `i` is always less than self.len().
965                unsafe { self.sift_up(0, i) };
966            }
967        }
968    }
969
970    fn rebuild(&mut self) {
971        let mut n = self.len() / 2;
972        while n > 0 {
973            n -= 1;
974            // SAFETY: n starts from self.len() / 2 and goes down to 0.
975            //  The only case when !(n < self.len()) is if
976            //  self.len() == 0, but it's ruled out by the loop condition.
977            unsafe { self.sift_down(n) };
978        }
979    }
980
981    /// Moves all the elements of `other` into `self`, leaving `other` empty.
982    ///
983    /// # Examples
984    ///
985    /// Basic usage:
986    ///
987    /// ```
988    /// use std::collections::BinaryHeap;
989    ///
990    /// let mut a = BinaryHeap::from([-10, 1, 2, 3, 3]);
991    /// let mut b = BinaryHeap::from([-20, 5, 43]);
992    ///
993    /// a.append(&mut b);
994    ///
995    /// assert_eq!(a.into_sorted_vec(), [-20, -10, 1, 2, 3, 3, 5, 43]);
996    /// assert!(b.is_empty());
997    /// ```
998    #[stable(feature = "binary_heap_append", since = "1.11.0")]
999    pub fn append(&mut self, other: &mut Self) {
1000        if self.len() < other.len() {
1001            swap(self, other);
1002        }
1003
1004        let start = self.data.len();
1005
1006        self.data.append(&mut other.data);
1007
1008        self.rebuild_tail(start);
1009    }
1010
1011    /// Clears the binary heap, returning an iterator over the removed elements
1012    /// in heap order. If the iterator is dropped before being fully consumed,
1013    /// it drops the remaining elements in heap order.
1014    ///
1015    /// The returned iterator keeps a mutable borrow on the heap to optimize
1016    /// its implementation.
1017    ///
1018    /// Note:
1019    /// * `.drain_sorted()` is *O*(*n* \* log(*n*)); much slower than `.drain()`.
1020    ///   You should use the latter for most cases.
1021    ///
1022    /// # Examples
1023    ///
1024    /// Basic usage:
1025    ///
1026    /// ```
1027    /// #![feature(binary_heap_drain_sorted)]
1028    /// use std::collections::BinaryHeap;
1029    ///
1030    /// let mut heap = BinaryHeap::from([1, 2, 3, 4, 5]);
1031    /// assert_eq!(heap.len(), 5);
1032    ///
1033    /// drop(heap.drain_sorted()); // removes all elements in heap order
1034    /// assert_eq!(heap.len(), 0);
1035    /// ```
1036    #[inline]
1037    #[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1038    pub fn drain_sorted(&mut self) -> DrainSorted<'_, T, A> {
1039        DrainSorted { inner: self }
1040    }
1041
1042    /// Retains only the elements specified by the predicate.
1043    ///
1044    /// In other words, remove all elements `e` for which `f(&e)` returns
1045    /// `false`. The elements are visited in unsorted (and unspecified) order.
1046    ///
1047    /// # Examples
1048    ///
1049    /// Basic usage:
1050    ///
1051    /// ```
1052    /// use std::collections::BinaryHeap;
1053    ///
1054    /// let mut heap = BinaryHeap::from([-10, -5, 1, 2, 4, 13]);
1055    ///
1056    /// heap.retain(|x| x % 2 == 0); // only keep even numbers
1057    ///
1058    /// assert_eq!(heap.into_sorted_vec(), [-10, 2, 4])
1059    /// ```
1060    #[stable(feature = "binary_heap_retain", since = "1.70.0")]
1061    pub fn retain<F>(&mut self, mut f: F)
1062    where
1063        F: FnMut(&T) -> bool,
1064    {
1065        // rebuild_start will be updated to the first touched element below, and the rebuild will
1066        // only be done for the tail.
1067        let mut guard = RebuildOnDrop { rebuild_from: self.len(), heap: self };
1068        let mut i = 0;
1069
1070        guard.heap.data.retain(|e| {
1071            let keep = f(e);
1072            if !keep && i < guard.rebuild_from {
1073                guard.rebuild_from = i;
1074            }
1075            i += 1;
1076            keep
1077        });
1078    }
1079}
1080
1081impl<T, A: Allocator> BinaryHeap<T, A> {
1082    /// Returns an iterator visiting all values in the underlying vector, in
1083    /// arbitrary order.
1084    ///
1085    /// # Examples
1086    ///
1087    /// Basic usage:
1088    ///
1089    /// ```
1090    /// use std::collections::BinaryHeap;
1091    /// let heap = BinaryHeap::from([1, 2, 3, 4]);
1092    ///
1093    /// // Print 1, 2, 3, 4 in arbitrary order
1094    /// for x in heap.iter() {
1095    ///     println!("{x}");
1096    /// }
1097    /// ```
1098    #[stable(feature = "rust1", since = "1.0.0")]
1099    #[cfg_attr(not(test), rustc_diagnostic_item = "binaryheap_iter")]
1100    pub fn iter(&self) -> Iter<'_, T> {
1101        Iter { iter: self.data.iter() }
1102    }
1103
1104    /// Returns an iterator which retrieves elements in heap order.
1105    ///
1106    /// This method consumes the original heap.
1107    ///
1108    /// # Examples
1109    ///
1110    /// Basic usage:
1111    ///
1112    /// ```
1113    /// #![feature(binary_heap_into_iter_sorted)]
1114    /// use std::collections::BinaryHeap;
1115    /// let heap = BinaryHeap::from([1, 2, 3, 4, 5]);
1116    ///
1117    /// assert_eq!(heap.into_iter_sorted().take(2).collect::<Vec<_>>(), [5, 4]);
1118    /// ```
1119    #[unstable(feature = "binary_heap_into_iter_sorted", issue = "59278")]
1120    pub fn into_iter_sorted(self) -> IntoIterSorted<T, A> {
1121        IntoIterSorted { inner: self }
1122    }
1123
1124    /// Returns the greatest item in the binary heap, or `None` if it is empty.
1125    ///
1126    /// # Examples
1127    ///
1128    /// Basic usage:
1129    ///
1130    /// ```
1131    /// use std::collections::BinaryHeap;
1132    /// let mut heap = BinaryHeap::new();
1133    /// assert_eq!(heap.peek(), None);
1134    ///
1135    /// heap.push(1);
1136    /// heap.push(5);
1137    /// heap.push(2);
1138    /// assert_eq!(heap.peek(), Some(&5));
1139    ///
1140    /// ```
1141    ///
1142    /// # Time complexity
1143    ///
1144    /// Cost is *O*(1) in the worst case.
1145    #[must_use]
1146    #[stable(feature = "rust1", since = "1.0.0")]
1147    pub fn peek(&self) -> Option<&T> {
1148        self.data.get(0)
1149    }
1150
1151    /// Returns the number of elements the binary heap can hold without reallocating.
1152    ///
1153    /// # Examples
1154    ///
1155    /// Basic usage:
1156    ///
1157    /// ```
1158    /// use std::collections::BinaryHeap;
1159    /// let mut heap = BinaryHeap::with_capacity(100);
1160    /// assert!(heap.capacity() >= 100);
1161    /// heap.push(4);
1162    /// ```
1163    #[must_use]
1164    #[stable(feature = "rust1", since = "1.0.0")]
1165    pub fn capacity(&self) -> usize {
1166        self.data.capacity()
1167    }
1168
1169    /// Reserves the minimum capacity for at least `additional` elements more than
1170    /// the current length. Unlike [`reserve`], this will not
1171    /// deliberately over-allocate to speculatively avoid frequent allocations.
1172    /// After calling `reserve_exact`, capacity will be greater than or equal to
1173    /// `self.len() + additional`. Does nothing if the capacity is already
1174    /// sufficient.
1175    ///
1176    /// [`reserve`]: BinaryHeap::reserve
1177    ///
1178    /// # Panics
1179    ///
1180    /// Panics if the new capacity overflows [`usize`].
1181    ///
1182    /// # Examples
1183    ///
1184    /// Basic usage:
1185    ///
1186    /// ```
1187    /// use std::collections::BinaryHeap;
1188    /// let mut heap = BinaryHeap::new();
1189    /// heap.reserve_exact(100);
1190    /// assert!(heap.capacity() >= 100);
1191    /// heap.push(4);
1192    /// ```
1193    ///
1194    /// [`reserve`]: BinaryHeap::reserve
1195    #[stable(feature = "rust1", since = "1.0.0")]
1196    pub fn reserve_exact(&mut self, additional: usize) {
1197        self.data.reserve_exact(additional);
1198    }
1199
1200    /// Reserves capacity for at least `additional` elements more than the
1201    /// current length. The allocator may reserve more space to speculatively
1202    /// avoid frequent allocations. After calling `reserve`,
1203    /// capacity will be greater than or equal to `self.len() + additional`.
1204    /// Does nothing if capacity is already sufficient.
1205    ///
1206    /// # Panics
1207    ///
1208    /// Panics if the new capacity overflows [`usize`].
1209    ///
1210    /// # Examples
1211    ///
1212    /// Basic usage:
1213    ///
1214    /// ```
1215    /// use std::collections::BinaryHeap;
1216    /// let mut heap = BinaryHeap::new();
1217    /// heap.reserve(100);
1218    /// assert!(heap.capacity() >= 100);
1219    /// heap.push(4);
1220    /// ```
1221    #[stable(feature = "rust1", since = "1.0.0")]
1222    pub fn reserve(&mut self, additional: usize) {
1223        self.data.reserve(additional);
1224    }
1225
1226    /// Tries to reserve the minimum capacity for at least `additional` elements
1227    /// more than the current length. Unlike [`try_reserve`], this will not
1228    /// deliberately over-allocate to speculatively avoid frequent allocations.
1229    /// After calling `try_reserve_exact`, capacity will be greater than or
1230    /// equal to `self.len() + additional` if it returns `Ok(())`.
1231    /// Does nothing if the capacity is already sufficient.
1232    ///
1233    /// Note that the allocator may give the collection more space than it
1234    /// requests. Therefore, capacity can not be relied upon to be precisely
1235    /// minimal. Prefer [`try_reserve`] if future insertions are expected.
1236    ///
1237    /// [`try_reserve`]: BinaryHeap::try_reserve
1238    ///
1239    /// # Errors
1240    ///
1241    /// If the capacity overflows, or the allocator reports a failure, then an error
1242    /// is returned.
1243    ///
1244    /// # Examples
1245    ///
1246    /// ```
1247    /// use std::collections::BinaryHeap;
1248    /// use std::collections::TryReserveError;
1249    ///
1250    /// fn find_max_slow(data: &[u32]) -> Result<Option<u32>, TryReserveError> {
1251    ///     let mut heap = BinaryHeap::new();
1252    ///
1253    ///     // Pre-reserve the memory, exiting if we can't
1254    ///     heap.try_reserve_exact(data.len())?;
1255    ///
1256    ///     // Now we know this can't OOM in the middle of our complex work
1257    ///     heap.extend(data.iter());
1258    ///
1259    ///     Ok(heap.pop())
1260    /// }
1261    /// # find_max_slow(&[1, 2, 3]).expect("why is the test harness OOMing on 12 bytes?");
1262    /// ```
1263    #[stable(feature = "try_reserve_2", since = "1.63.0")]
1264    pub fn try_reserve_exact(&mut self, additional: usize) -> Result<(), TryReserveError> {
1265        self.data.try_reserve_exact(additional)
1266    }
1267
1268    /// Tries to reserve capacity for at least `additional` elements more than the
1269    /// current length. The allocator may reserve more space to speculatively
1270    /// avoid frequent allocations. After calling `try_reserve`, capacity will be
1271    /// greater than or equal to `self.len() + additional` if it returns
1272    /// `Ok(())`. Does nothing if capacity is already sufficient. This method
1273    /// preserves the contents even if an error occurs.
1274    ///
1275    /// # Errors
1276    ///
1277    /// If the capacity overflows, or the allocator reports a failure, then an error
1278    /// is returned.
1279    ///
1280    /// # Examples
1281    ///
1282    /// ```
1283    /// use std::collections::BinaryHeap;
1284    /// use std::collections::TryReserveError;
1285    ///
1286    /// fn find_max_slow(data: &[u32]) -> Result<Option<u32>, TryReserveError> {
1287    ///     let mut heap = BinaryHeap::new();
1288    ///
1289    ///     // Pre-reserve the memory, exiting if we can't
1290    ///     heap.try_reserve(data.len())?;
1291    ///
1292    ///     // Now we know this can't OOM in the middle of our complex work
1293    ///     heap.extend(data.iter());
1294    ///
1295    ///     Ok(heap.pop())
1296    /// }
1297    /// # find_max_slow(&[1, 2, 3]).expect("why is the test harness OOMing on 12 bytes?");
1298    /// ```
1299    #[stable(feature = "try_reserve_2", since = "1.63.0")]
1300    pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError> {
1301        self.data.try_reserve(additional)
1302    }
1303
1304    /// Discards as much additional capacity as possible.
1305    ///
1306    /// # Examples
1307    ///
1308    /// Basic usage:
1309    ///
1310    /// ```
1311    /// use std::collections::BinaryHeap;
1312    /// let mut heap: BinaryHeap<i32> = BinaryHeap::with_capacity(100);
1313    ///
1314    /// assert!(heap.capacity() >= 100);
1315    /// heap.shrink_to_fit();
1316    /// assert!(heap.capacity() == 0);
1317    /// ```
1318    #[stable(feature = "rust1", since = "1.0.0")]
1319    pub fn shrink_to_fit(&mut self) {
1320        self.data.shrink_to_fit();
1321    }
1322
1323    /// Discards capacity with a lower bound.
1324    ///
1325    /// The capacity will remain at least as large as both the length
1326    /// and the supplied value.
1327    ///
1328    /// If the current capacity is less than the lower limit, this is a no-op.
1329    ///
1330    /// # Examples
1331    ///
1332    /// ```
1333    /// use std::collections::BinaryHeap;
1334    /// let mut heap: BinaryHeap<i32> = BinaryHeap::with_capacity(100);
1335    ///
1336    /// assert!(heap.capacity() >= 100);
1337    /// heap.shrink_to(10);
1338    /// assert!(heap.capacity() >= 10);
1339    /// ```
1340    #[inline]
1341    #[stable(feature = "shrink_to", since = "1.56.0")]
1342    pub fn shrink_to(&mut self, min_capacity: usize) {
1343        self.data.shrink_to(min_capacity)
1344    }
1345
1346    /// Returns a slice of all values in the underlying vector, in arbitrary
1347    /// order.
1348    ///
1349    /// # Examples
1350    ///
1351    /// Basic usage:
1352    ///
1353    /// ```
1354    /// use std::collections::BinaryHeap;
1355    /// use std::io::{self, Write};
1356    ///
1357    /// let heap = BinaryHeap::from([1, 2, 3, 4, 5, 6, 7]);
1358    ///
1359    /// io::sink().write(heap.as_slice()).unwrap();
1360    /// ```
1361    #[must_use]
1362    #[stable(feature = "binary_heap_as_slice", since = "1.80.0")]
1363    pub fn as_slice(&self) -> &[T] {
1364        self.data.as_slice()
1365    }
1366
1367    /// Consumes the `BinaryHeap` and returns the underlying vector
1368    /// in arbitrary order.
1369    ///
1370    /// # Examples
1371    ///
1372    /// Basic usage:
1373    ///
1374    /// ```
1375    /// use std::collections::BinaryHeap;
1376    /// let heap = BinaryHeap::from([1, 2, 3, 4, 5, 6, 7]);
1377    /// let vec = heap.into_vec();
1378    ///
1379    /// // Will print in some order
1380    /// for x in vec {
1381    ///     println!("{x}");
1382    /// }
1383    /// ```
1384    #[must_use = "`self` will be dropped if the result is not used"]
1385    #[stable(feature = "binary_heap_extras_15", since = "1.5.0")]
1386    pub fn into_vec(self) -> Vec<T, A> {
1387        self.into()
1388    }
1389
1390    /// Returns a reference to the underlying allocator.
1391    #[unstable(feature = "allocator_api", issue = "32838")]
1392    #[inline]
1393    pub fn allocator(&self) -> &A {
1394        self.data.allocator()
1395    }
1396
1397    /// Returns the length of the binary heap.
1398    ///
1399    /// # Examples
1400    ///
1401    /// Basic usage:
1402    ///
1403    /// ```
1404    /// use std::collections::BinaryHeap;
1405    /// let heap = BinaryHeap::from([1, 3]);
1406    ///
1407    /// assert_eq!(heap.len(), 2);
1408    /// ```
1409    #[must_use]
1410    #[stable(feature = "rust1", since = "1.0.0")]
1411    #[rustc_confusables("length", "size")]
1412    pub fn len(&self) -> usize {
1413        self.data.len()
1414    }
1415
1416    /// Checks if the binary heap is empty.
1417    ///
1418    /// # Examples
1419    ///
1420    /// Basic usage:
1421    ///
1422    /// ```
1423    /// use std::collections::BinaryHeap;
1424    /// let mut heap = BinaryHeap::new();
1425    ///
1426    /// assert!(heap.is_empty());
1427    ///
1428    /// heap.push(3);
1429    /// heap.push(5);
1430    /// heap.push(1);
1431    ///
1432    /// assert!(!heap.is_empty());
1433    /// ```
1434    #[must_use]
1435    #[stable(feature = "rust1", since = "1.0.0")]
1436    pub fn is_empty(&self) -> bool {
1437        self.len() == 0
1438    }
1439
1440    /// Clears the binary heap, returning an iterator over the removed elements
1441    /// in arbitrary order. If the iterator is dropped before being fully
1442    /// consumed, it drops the remaining elements in arbitrary order.
1443    ///
1444    /// The returned iterator keeps a mutable borrow on the heap to optimize
1445    /// its implementation.
1446    ///
1447    /// # Examples
1448    ///
1449    /// Basic usage:
1450    ///
1451    /// ```
1452    /// use std::collections::BinaryHeap;
1453    /// let mut heap = BinaryHeap::from([1, 3]);
1454    ///
1455    /// assert!(!heap.is_empty());
1456    ///
1457    /// for x in heap.drain() {
1458    ///     println!("{x}");
1459    /// }
1460    ///
1461    /// assert!(heap.is_empty());
1462    /// ```
1463    #[inline]
1464    #[stable(feature = "drain", since = "1.6.0")]
1465    pub fn drain(&mut self) -> Drain<'_, T, A> {
1466        Drain { iter: self.data.drain(..) }
1467    }
1468
1469    /// Drops all items from the binary heap.
1470    ///
1471    /// # Examples
1472    ///
1473    /// Basic usage:
1474    ///
1475    /// ```
1476    /// use std::collections::BinaryHeap;
1477    /// let mut heap = BinaryHeap::from([1, 3]);
1478    ///
1479    /// assert!(!heap.is_empty());
1480    ///
1481    /// heap.clear();
1482    ///
1483    /// assert!(heap.is_empty());
1484    /// ```
1485    #[stable(feature = "rust1", since = "1.0.0")]
1486    pub fn clear(&mut self) {
1487        self.drain();
1488    }
1489}
1490
1491/// Hole represents a hole in a slice i.e., an index without valid value
1492/// (because it was moved from or duplicated).
1493/// In drop, `Hole` will restore the slice by filling the hole
1494/// position with the value that was originally removed.
1495struct Hole<'a, T: 'a> {
1496    data: &'a mut [T],
1497    elt: ManuallyDrop<T>,
1498    pos: usize,
1499}
1500
1501impl<'a, T> Hole<'a, T> {
1502    /// Creates a new `Hole` at index `pos`.
1503    ///
1504    /// Unsafe because pos must be within the data slice.
1505    #[inline]
1506    unsafe fn new(data: &'a mut [T], pos: usize) -> Self {
1507        debug_assert!(pos < data.len());
1508        // SAFE: pos should be inside the slice
1509        let elt = unsafe { ptr::read(data.get_unchecked(pos)) };
1510        Hole { data, elt: ManuallyDrop::new(elt), pos }
1511    }
1512
1513    #[inline]
1514    fn pos(&self) -> usize {
1515        self.pos
1516    }
1517
1518    /// Returns a reference to the element removed.
1519    #[inline]
1520    fn element(&self) -> &T {
1521        &self.elt
1522    }
1523
1524    /// Returns a reference to the element at `index`.
1525    ///
1526    /// Unsafe because index must be within the data slice and not equal to pos.
1527    #[inline]
1528    unsafe fn get(&self, index: usize) -> &T {
1529        debug_assert!(index != self.pos);
1530        debug_assert!(index < self.data.len());
1531        unsafe { self.data.get_unchecked(index) }
1532    }
1533
1534    /// Move hole to new location
1535    ///
1536    /// Unsafe because index must be within the data slice and not equal to pos.
1537    #[inline]
1538    unsafe fn move_to(&mut self, index: usize) {
1539        debug_assert!(index != self.pos);
1540        debug_assert!(index < self.data.len());
1541        unsafe {
1542            let ptr = self.data.as_mut_ptr();
1543            let index_ptr: *const _ = ptr.add(index);
1544            let hole_ptr = ptr.add(self.pos);
1545            ptr::copy_nonoverlapping(index_ptr, hole_ptr, 1);
1546        }
1547        self.pos = index;
1548    }
1549}
1550
1551impl<T> Drop for Hole<'_, T> {
1552    #[inline]
1553    fn drop(&mut self) {
1554        // fill the hole again
1555        unsafe {
1556            let pos = self.pos;
1557            ptr::copy_nonoverlapping(&*self.elt, self.data.get_unchecked_mut(pos), 1);
1558        }
1559    }
1560}
1561
1562/// An iterator over the elements of a `BinaryHeap`.
1563///
1564/// This `struct` is created by [`BinaryHeap::iter()`]. See its
1565/// documentation for more.
1566///
1567/// [`iter`]: BinaryHeap::iter
1568#[must_use = "iterators are lazy and do nothing unless consumed"]
1569#[stable(feature = "rust1", since = "1.0.0")]
1570pub struct Iter<'a, T: 'a> {
1571    iter: slice::Iter<'a, T>,
1572}
1573
1574#[stable(feature = "default_iters_sequel", since = "1.82.0")]
1575impl<T> Default for Iter<'_, T> {
1576    /// Creates an empty `binary_heap::Iter`.
1577    ///
1578    /// ```
1579    /// # use std::collections::binary_heap;
1580    /// let iter: binary_heap::Iter<'_, u8> = Default::default();
1581    /// assert_eq!(iter.len(), 0);
1582    /// ```
1583    fn default() -> Self {
1584        Iter { iter: Default::default() }
1585    }
1586}
1587
1588#[stable(feature = "collection_debug", since = "1.17.0")]
1589impl<T: fmt::Debug> fmt::Debug for Iter<'_, T> {
1590    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1591        f.debug_tuple("Iter").field(&self.iter.as_slice()).finish()
1592    }
1593}
1594
1595// FIXME(#26925) Remove in favor of `#[derive(Clone)]`
1596#[stable(feature = "rust1", since = "1.0.0")]
1597impl<T> Clone for Iter<'_, T> {
1598    fn clone(&self) -> Self {
1599        Iter { iter: self.iter.clone() }
1600    }
1601}
1602
1603#[stable(feature = "rust1", since = "1.0.0")]
1604impl<'a, T> Iterator for Iter<'a, T> {
1605    type Item = &'a T;
1606
1607    #[inline]
1608    fn next(&mut self) -> Option<&'a T> {
1609        self.iter.next()
1610    }
1611
1612    #[inline]
1613    fn size_hint(&self) -> (usize, Option<usize>) {
1614        self.iter.size_hint()
1615    }
1616
1617    #[inline]
1618    fn last(self) -> Option<&'a T> {
1619        self.iter.last()
1620    }
1621}
1622
1623#[stable(feature = "rust1", since = "1.0.0")]
1624impl<'a, T> DoubleEndedIterator for Iter<'a, T> {
1625    #[inline]
1626    fn next_back(&mut self) -> Option<&'a T> {
1627        self.iter.next_back()
1628    }
1629}
1630
1631#[stable(feature = "rust1", since = "1.0.0")]
1632impl<T> ExactSizeIterator for Iter<'_, T> {
1633    fn is_empty(&self) -> bool {
1634        self.iter.is_empty()
1635    }
1636}
1637
1638#[stable(feature = "fused", since = "1.26.0")]
1639impl<T> FusedIterator for Iter<'_, T> {}
1640
1641/// An owning iterator over the elements of a `BinaryHeap`.
1642///
1643/// This `struct` is created by [`BinaryHeap::into_iter()`]
1644/// (provided by the [`IntoIterator`] trait). See its documentation for more.
1645///
1646/// [`into_iter`]: BinaryHeap::into_iter
1647#[stable(feature = "rust1", since = "1.0.0")]
1648#[derive(Clone)]
1649pub struct IntoIter<
1650    T,
1651    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
1652> {
1653    iter: vec::IntoIter<T, A>,
1654}
1655
1656impl<T, A: Allocator> IntoIter<T, A> {
1657    /// Returns a reference to the underlying allocator.
1658    #[unstable(feature = "allocator_api", issue = "32838")]
1659    pub fn allocator(&self) -> &A {
1660        self.iter.allocator()
1661    }
1662}
1663
1664#[stable(feature = "collection_debug", since = "1.17.0")]
1665impl<T: fmt::Debug, A: Allocator> fmt::Debug for IntoIter<T, A> {
1666    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1667        f.debug_tuple("IntoIter").field(&self.iter.as_slice()).finish()
1668    }
1669}
1670
1671#[stable(feature = "rust1", since = "1.0.0")]
1672impl<T, A: Allocator> Iterator for IntoIter<T, A> {
1673    type Item = T;
1674
1675    #[inline]
1676    fn next(&mut self) -> Option<T> {
1677        self.iter.next()
1678    }
1679
1680    #[inline]
1681    fn size_hint(&self) -> (usize, Option<usize>) {
1682        self.iter.size_hint()
1683    }
1684}
1685
1686#[stable(feature = "rust1", since = "1.0.0")]
1687impl<T, A: Allocator> DoubleEndedIterator for IntoIter<T, A> {
1688    #[inline]
1689    fn next_back(&mut self) -> Option<T> {
1690        self.iter.next_back()
1691    }
1692}
1693
1694#[stable(feature = "rust1", since = "1.0.0")]
1695impl<T, A: Allocator> ExactSizeIterator for IntoIter<T, A> {
1696    fn is_empty(&self) -> bool {
1697        self.iter.is_empty()
1698    }
1699}
1700
1701#[stable(feature = "fused", since = "1.26.0")]
1702impl<T, A: Allocator> FusedIterator for IntoIter<T, A> {}
1703
1704#[doc(hidden)]
1705#[unstable(issue = "none", feature = "trusted_fused")]
1706unsafe impl<T, A: Allocator> TrustedFused for IntoIter<T, A> {}
1707
1708#[stable(feature = "default_iters", since = "1.70.0")]
1709impl<T> Default for IntoIter<T> {
1710    /// Creates an empty `binary_heap::IntoIter`.
1711    ///
1712    /// ```
1713    /// # use std::collections::binary_heap;
1714    /// let iter: binary_heap::IntoIter<u8> = Default::default();
1715    /// assert_eq!(iter.len(), 0);
1716    /// ```
1717    fn default() -> Self {
1718        IntoIter { iter: Default::default() }
1719    }
1720}
1721
1722// In addition to the SAFETY invariants of the following three unsafe traits
1723// also refer to the vec::in_place_collect module documentation to get an overview
1724#[unstable(issue = "none", feature = "inplace_iteration")]
1725#[doc(hidden)]
1726unsafe impl<T, A: Allocator> SourceIter for IntoIter<T, A> {
1727    type Source = IntoIter<T, A>;
1728
1729    #[inline]
1730    unsafe fn as_inner(&mut self) -> &mut Self::Source {
1731        self
1732    }
1733}
1734
1735#[unstable(issue = "none", feature = "inplace_iteration")]
1736#[doc(hidden)]
1737unsafe impl<I, A: Allocator> InPlaceIterable for IntoIter<I, A> {
1738    const EXPAND_BY: Option<NonZero<usize>> = NonZero::new(1);
1739    const MERGE_BY: Option<NonZero<usize>> = NonZero::new(1);
1740}
1741
1742#[cfg(not(test))]
1743unsafe impl<I> AsVecIntoIter for IntoIter<I> {
1744    type Item = I;
1745
1746    fn as_into_iter(&mut self) -> &mut vec::IntoIter<Self::Item> {
1747        &mut self.iter
1748    }
1749}
1750
1751#[must_use = "iterators are lazy and do nothing unless consumed"]
1752#[unstable(feature = "binary_heap_into_iter_sorted", issue = "59278")]
1753#[derive(Clone, Debug)]
1754pub struct IntoIterSorted<
1755    T,
1756    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
1757> {
1758    inner: BinaryHeap<T, A>,
1759}
1760
1761impl<T, A: Allocator> IntoIterSorted<T, A> {
1762    /// Returns a reference to the underlying allocator.
1763    #[unstable(feature = "allocator_api", issue = "32838")]
1764    pub fn allocator(&self) -> &A {
1765        self.inner.allocator()
1766    }
1767}
1768
1769#[unstable(feature = "binary_heap_into_iter_sorted", issue = "59278")]
1770impl<T: Ord, A: Allocator> Iterator for IntoIterSorted<T, A> {
1771    type Item = T;
1772
1773    #[inline]
1774    fn next(&mut self) -> Option<T> {
1775        self.inner.pop()
1776    }
1777
1778    #[inline]
1779    fn size_hint(&self) -> (usize, Option<usize>) {
1780        let exact = self.inner.len();
1781        (exact, Some(exact))
1782    }
1783}
1784
1785#[unstable(feature = "binary_heap_into_iter_sorted", issue = "59278")]
1786impl<T: Ord, A: Allocator> ExactSizeIterator for IntoIterSorted<T, A> {}
1787
1788#[unstable(feature = "binary_heap_into_iter_sorted", issue = "59278")]
1789impl<T: Ord, A: Allocator> FusedIterator for IntoIterSorted<T, A> {}
1790
1791#[unstable(feature = "trusted_len", issue = "37572")]
1792unsafe impl<T: Ord, A: Allocator> TrustedLen for IntoIterSorted<T, A> {}
1793
1794/// A draining iterator over the elements of a `BinaryHeap`.
1795///
1796/// This `struct` is created by [`BinaryHeap::drain()`]. See its
1797/// documentation for more.
1798///
1799/// [`drain`]: BinaryHeap::drain
1800#[stable(feature = "drain", since = "1.6.0")]
1801#[derive(Debug)]
1802pub struct Drain<
1803    'a,
1804    T: 'a,
1805    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
1806> {
1807    iter: vec::Drain<'a, T, A>,
1808}
1809
1810impl<T, A: Allocator> Drain<'_, T, A> {
1811    /// Returns a reference to the underlying allocator.
1812    #[unstable(feature = "allocator_api", issue = "32838")]
1813    pub fn allocator(&self) -> &A {
1814        self.iter.allocator()
1815    }
1816}
1817
1818#[stable(feature = "drain", since = "1.6.0")]
1819impl<T, A: Allocator> Iterator for Drain<'_, T, A> {
1820    type Item = T;
1821
1822    #[inline]
1823    fn next(&mut self) -> Option<T> {
1824        self.iter.next()
1825    }
1826
1827    #[inline]
1828    fn size_hint(&self) -> (usize, Option<usize>) {
1829        self.iter.size_hint()
1830    }
1831}
1832
1833#[stable(feature = "drain", since = "1.6.0")]
1834impl<T, A: Allocator> DoubleEndedIterator for Drain<'_, T, A> {
1835    #[inline]
1836    fn next_back(&mut self) -> Option<T> {
1837        self.iter.next_back()
1838    }
1839}
1840
1841#[stable(feature = "drain", since = "1.6.0")]
1842impl<T, A: Allocator> ExactSizeIterator for Drain<'_, T, A> {
1843    fn is_empty(&self) -> bool {
1844        self.iter.is_empty()
1845    }
1846}
1847
1848#[stable(feature = "fused", since = "1.26.0")]
1849impl<T, A: Allocator> FusedIterator for Drain<'_, T, A> {}
1850
1851/// A draining iterator over the elements of a `BinaryHeap`.
1852///
1853/// This `struct` is created by [`BinaryHeap::drain_sorted()`]. See its
1854/// documentation for more.
1855///
1856/// [`drain_sorted`]: BinaryHeap::drain_sorted
1857#[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1858#[derive(Debug)]
1859pub struct DrainSorted<
1860    'a,
1861    T: Ord,
1862    #[unstable(feature = "allocator_api", issue = "32838")] A: Allocator = Global,
1863> {
1864    inner: &'a mut BinaryHeap<T, A>,
1865}
1866
1867impl<'a, T: Ord, A: Allocator> DrainSorted<'a, T, A> {
1868    /// Returns a reference to the underlying allocator.
1869    #[unstable(feature = "allocator_api", issue = "32838")]
1870    pub fn allocator(&self) -> &A {
1871        self.inner.allocator()
1872    }
1873}
1874
1875#[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1876impl<'a, T: Ord, A: Allocator> Drop for DrainSorted<'a, T, A> {
1877    /// Removes heap elements in heap order.
1878    fn drop(&mut self) {
1879        struct DropGuard<'r, 'a, T: Ord, A: Allocator>(&'r mut DrainSorted<'a, T, A>);
1880
1881        impl<'r, 'a, T: Ord, A: Allocator> Drop for DropGuard<'r, 'a, T, A> {
1882            fn drop(&mut self) {
1883                while self.0.inner.pop().is_some() {}
1884            }
1885        }
1886
1887        while let Some(item) = self.inner.pop() {
1888            let guard = DropGuard(self);
1889            drop(item);
1890            mem::forget(guard);
1891        }
1892    }
1893}
1894
1895#[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1896impl<T: Ord, A: Allocator> Iterator for DrainSorted<'_, T, A> {
1897    type Item = T;
1898
1899    #[inline]
1900    fn next(&mut self) -> Option<T> {
1901        self.inner.pop()
1902    }
1903
1904    #[inline]
1905    fn size_hint(&self) -> (usize, Option<usize>) {
1906        let exact = self.inner.len();
1907        (exact, Some(exact))
1908    }
1909}
1910
1911#[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1912impl<T: Ord, A: Allocator> ExactSizeIterator for DrainSorted<'_, T, A> {}
1913
1914#[unstable(feature = "binary_heap_drain_sorted", issue = "59278")]
1915impl<T: Ord, A: Allocator> FusedIterator for DrainSorted<'_, T, A> {}
1916
1917#[unstable(feature = "trusted_len", issue = "37572")]
1918unsafe impl<T: Ord, A: Allocator> TrustedLen for DrainSorted<'_, T, A> {}
1919
1920#[stable(feature = "binary_heap_extras_15", since = "1.5.0")]
1921impl<T: Ord, A: Allocator> From<Vec<T, A>> for BinaryHeap<T, A> {
1922    /// Converts a `Vec<T>` into a `BinaryHeap<T>`.
1923    ///
1924    /// This conversion happens in-place, and has *O*(*n*) time complexity.
1925    fn from(vec: Vec<T, A>) -> BinaryHeap<T, A> {
1926        let mut heap = BinaryHeap { data: vec };
1927        heap.rebuild();
1928        heap
1929    }
1930}
1931
1932#[stable(feature = "std_collections_from_array", since = "1.56.0")]
1933impl<T: Ord, const N: usize> From<[T; N]> for BinaryHeap<T> {
1934    /// ```
1935    /// use std::collections::BinaryHeap;
1936    ///
1937    /// let mut h1 = BinaryHeap::from([1, 4, 2, 3]);
1938    /// let mut h2: BinaryHeap<_> = [1, 4, 2, 3].into();
1939    /// while let Some((a, b)) = h1.pop().zip(h2.pop()) {
1940    ///     assert_eq!(a, b);
1941    /// }
1942    /// ```
1943    fn from(arr: [T; N]) -> Self {
1944        Self::from_iter(arr)
1945    }
1946}
1947
1948#[stable(feature = "binary_heap_extras_15", since = "1.5.0")]
1949impl<T, A: Allocator> From<BinaryHeap<T, A>> for Vec<T, A> {
1950    /// Converts a `BinaryHeap<T>` into a `Vec<T>`.
1951    ///
1952    /// This conversion requires no data movement or allocation, and has
1953    /// constant time complexity.
1954    fn from(heap: BinaryHeap<T, A>) -> Vec<T, A> {
1955        heap.data
1956    }
1957}
1958
1959#[stable(feature = "rust1", since = "1.0.0")]
1960impl<T: Ord> FromIterator<T> for BinaryHeap<T> {
1961    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> BinaryHeap<T> {
1962        BinaryHeap::from(iter.into_iter().collect::<Vec<_>>())
1963    }
1964}
1965
1966#[stable(feature = "rust1", since = "1.0.0")]
1967impl<T, A: Allocator> IntoIterator for BinaryHeap<T, A> {
1968    type Item = T;
1969    type IntoIter = IntoIter<T, A>;
1970
1971    /// Creates a consuming iterator, that is, one that moves each value out of
1972    /// the binary heap in arbitrary order. The binary heap cannot be used
1973    /// after calling this.
1974    ///
1975    /// # Examples
1976    ///
1977    /// Basic usage:
1978    ///
1979    /// ```
1980    /// use std::collections::BinaryHeap;
1981    /// let heap = BinaryHeap::from([1, 2, 3, 4]);
1982    ///
1983    /// // Print 1, 2, 3, 4 in arbitrary order
1984    /// for x in heap.into_iter() {
1985    ///     // x has type i32, not &i32
1986    ///     println!("{x}");
1987    /// }
1988    /// ```
1989    fn into_iter(self) -> IntoIter<T, A> {
1990        IntoIter { iter: self.data.into_iter() }
1991    }
1992}
1993
1994#[stable(feature = "rust1", since = "1.0.0")]
1995impl<'a, T, A: Allocator> IntoIterator for &'a BinaryHeap<T, A> {
1996    type Item = &'a T;
1997    type IntoIter = Iter<'a, T>;
1998
1999    fn into_iter(self) -> Iter<'a, T> {
2000        self.iter()
2001    }
2002}
2003
2004#[stable(feature = "rust1", since = "1.0.0")]
2005impl<T: Ord, A: Allocator> Extend<T> for BinaryHeap<T, A> {
2006    #[inline]
2007    fn extend<I: IntoIterator<Item = T>>(&mut self, iter: I) {
2008        let guard = RebuildOnDrop { rebuild_from: self.len(), heap: self };
2009        guard.heap.data.extend(iter);
2010    }
2011
2012    #[inline]
2013    fn extend_one(&mut self, item: T) {
2014        self.push(item);
2015    }
2016
2017    #[inline]
2018    fn extend_reserve(&mut self, additional: usize) {
2019        self.reserve(additional);
2020    }
2021}
2022
2023#[stable(feature = "extend_ref", since = "1.2.0")]
2024impl<'a, T: 'a + Ord + Copy, A: Allocator> Extend<&'a T> for BinaryHeap<T, A> {
2025    fn extend<I: IntoIterator<Item = &'a T>>(&mut self, iter: I) {
2026        self.extend(iter.into_iter().cloned());
2027    }
2028
2029    #[inline]
2030    fn extend_one(&mut self, &item: &'a T) {
2031        self.push(item);
2032    }
2033
2034    #[inline]
2035    fn extend_reserve(&mut self, additional: usize) {
2036        self.reserve(additional);
2037    }
2038}
````