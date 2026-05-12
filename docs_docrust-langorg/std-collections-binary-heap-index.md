---
title: std::collections::binary_heap - Rust
url: https://doc.rust-lang.org/std/collections/binary_heap/index.html
source: crawler
fetched_at: 2026-05-06T21:24:52.201543092-03:00
rendered_js: false
word_count: 297
summary: This document provides a technical overview and interface reference for the binary heap priority queue implementation in Rust's standard library.
tags:
    - rust
    - priority-queue
    - binary-heap
    - data-structures
    - collection-types
category: reference
---

## Module binary\_heap

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#9)

Expand description

A priority queue implemented with a binary heap.

Insertion and popping the largest element have *O*(log(*n*)) time complexity. Checking the largest element is *O*(1). Converting a vector to a binary heap can be done in-place, and has *O*(*n*) complexity. A binary heap can also be converted to a sorted vector in-place, allowing it to be used for an *O*(*n* * log(*n*)) in-place heapsort.

## [§](#examples)Examples

This is a larger example that implements [Dijkstra’s algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to solve the [shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem) on a [directed graph](https://en.wikipedia.org/wiki/Directed_graph). It shows how to use [`BinaryHeap`](https://doc.rust-lang.org/std/collections/struct.BinaryHeap.html "struct std::collections::BinaryHeap") with custom types.

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    position: usize,
}

// The priority queue depends on `Ord`.
// Explicitly implement the trait so the queue becomes a min-heap
// instead of a max-heap.
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        // Notice that we flip the ordering on costs.
        // In case of a tie we compare positions - this step is necessary
        // to make implementations of `PartialEq` and `Ord` consistent.
        other.cost.cmp(&self.cost)
            .then_with(|| self.position.cmp(&other.position))
    }
}

// `PartialOrd` needs to be implemented as well.
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// Each node is represented as a `usize`, for a shorter implementation.
struct Edge {
    node: usize,
    cost: usize,
}

// Dijkstra's shortest path algorithm.

// Start at `start` and use `dist` to track the current shortest distance
// to each node. This implementation isn't memory-efficient as it may leave duplicate
// nodes in the queue. It also uses `usize::MAX` as a sentinel value,
// for a simpler implementation.
fn shortest_path(adj_list: &Vec<Vec<Edge>>, start: usize, goal: usize) -> Option<usize> {
    // dist[node] = current shortest distance from `start` to `node`
    let mut dist: Vec<_> = (0..adj_list.len()).map(|_| usize::MAX).collect();

    let mut heap = BinaryHeap::new();

    // We're at `start`, with a zero cost
    dist[start] = 0;
    heap.push(State { cost: 0, position: start });

    // Examine the frontier with lower cost nodes first (min-heap)
    while let Some(State { cost, position }) = heap.pop() {
        // Alternatively we could have continued to find all shortest paths
        if position == goal { return Some(cost); }

        // Important as we may have already found a better way
        if cost > dist[position] { continue; }

        // For each node we can reach, see if we can find a way with
        // a lower cost going through this node
        for edge in &adj_list[position] {
            let next = State { cost: cost + edge.cost, position: edge.node };

            // If so, add it to the frontier and continue
            if next.cost < dist[next.position] {
                heap.push(next);
                // Relaxation, we have now found a better way
                dist[next.position] = next.cost;
            }
        }
    }

    // Goal not reachable
    None
}

fn main() {
    // This is the directed graph we're going to use.
    // The node numbers correspond to the different states,
    // and the edge weights symbolize the cost of moving
    // from one node to another.
    // Note that the edges are one-way.
    //
    //                  7
    //          +-----------------+
    //          |                 |
    //          v   1        2    |  2
    //          0 -----> 1 -----> 3 ---> 4
    //          |        ^        ^      ^
    //          |        | 1      |      |
    //          |        |        | 3    | 1
    //          +------> 2 -------+      |
    //           10      |               |
    //                   +---------------+
    //
    // The graph is represented as an adjacency list where each index,
    // corresponding to a node value, has a list of outgoing edges.
    // Chosen for its efficiency.
    let graph = vec![
        // Node 0
        vec![Edge { node: 2, cost: 10 },
             Edge { node: 1, cost: 1 }],
        // Node 1
        vec![Edge { node: 3, cost: 2 }],
        // Node 2
        vec![Edge { node: 1, cost: 1 },
             Edge { node: 3, cost: 3 },
             Edge { node: 4, cost: 1 }],
        // Node 3
        vec![Edge { node: 0, cost: 7 },
             Edge { node: 4, cost: 2 }],
        // Node 4
        vec![]];

    assert_eq!(shortest_path(&graph, 0, 1), Some(1));
    assert_eq!(shortest_path(&graph, 0, 3), Some(3));
    assert_eq!(shortest_path(&graph, 3, 0), Some(7));
    assert_eq!(shortest_path(&graph, 0, 4), Some(5));
    assert_eq!(shortest_path(&graph, 4, 0), None);
}
```

[BinaryHeap](https://doc.rust-lang.org/std/collections/binary_heap/struct.BinaryHeap.html "struct std::collections::binary_heap::BinaryHeap")

A priority queue implemented with a binary heap.

[Drain](https://doc.rust-lang.org/std/collections/binary_heap/struct.Drain.html "struct std::collections::binary_heap::Drain")

A draining iterator over the elements of a `BinaryHeap`.

[IntoIter](https://doc.rust-lang.org/std/collections/binary_heap/struct.IntoIter.html "struct std::collections::binary_heap::IntoIter")

An owning iterator over the elements of a `BinaryHeap`.

[Iter](https://doc.rust-lang.org/std/collections/binary_heap/struct.Iter.html "struct std::collections::binary_heap::Iter")

An iterator over the elements of a `BinaryHeap`.

[PeekMut](https://doc.rust-lang.org/std/collections/binary_heap/struct.PeekMut.html "struct std::collections::binary_heap::PeekMut")

Structure wrapping a mutable reference to the greatest item on a `BinaryHeap`.

[DrainSorted](https://doc.rust-lang.org/std/collections/binary_heap/struct.DrainSorted.html "struct std::collections::binary_heap::DrainSorted")Experimental

A draining iterator over the elements of a `BinaryHeap`.

[IntoIterSorted](https://doc.rust-lang.org/std/collections/binary_heap/struct.IntoIterSorted.html "struct std::collections::binary_heap::IntoIterSorted")Experimental