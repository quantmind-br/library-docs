---
title: mod.rs - source
url: https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#154
source: crawler
fetched_at: 2026-05-06T21:38:24.658693949-03:00
rendered_js: false
word_count: 714
summary: This module defines core collection types in Rust and provides error handling mechanisms for memory allocation failures during reservation.
tags:
    - rust
    - collections
    - memory-allocation
    - error-handling
    - data-structures
    - try-reserve
category: reference
---

## alloc/collections/ mod.rs

```rust
1//! Collection types.
2
3// Note: This module is also included in the alloctests crate using #[path] to
4// run the tests. See the comment there for an explanation why this is the case.
5
6#![stable(feature = "rust1", since = "1.0.0")]
7
8#[cfg(not(no_global_oom_handling))]
9pub mod binary_heap;
10#[cfg(not(no_global_oom_handling))]
11mod btree;
12#[cfg(not(no_global_oom_handling))]
13pub mod linked_list;
14#[cfg(not(no_global_oom_handling))]
15pub mod vec_deque;
16
17#[cfg(not(no_global_oom_handling))]
18#[stable(feature = "rust1", since = "1.0.0")]
19pub mod btree_map {
20    //! An ordered map based on a B-Tree.
21    #[stable(feature = "rust1", since = "1.0.0")]
22    pub use super::btree::map::*;
23}
24
25#[cfg(not(no_global_oom_handling))]
26#[stable(feature = "rust1", since = "1.0.0")]
27pub mod btree_set {
28    //! An ordered set based on a B-Tree.
29    #[stable(feature = "rust1", since = "1.0.0")]
30    #[cfg(not(test))]
31    pub use super::btree::set::*;
32}
33
34#[cfg(not(test))]
35use core::fmt::Display;
36
37#[cfg(not(no_global_oom_handling))]
38#[stable(feature = "rust1", since = "1.0.0")]
39#[doc(no_inline)]
40#[cfg(not(test))]
41pub use binary_heap::BinaryHeap;
42#[cfg(not(no_global_oom_handling))]
43#[stable(feature = "rust1", since = "1.0.0")]
44#[doc(no_inline)]
45#[cfg(not(test))]
46pub use btree_map::BTreeMap;
47#[cfg(not(no_global_oom_handling))]
48#[stable(feature = "rust1", since = "1.0.0")]
49#[doc(no_inline)]
50#[cfg(not(test))]
51pub use btree_set::BTreeSet;
52#[cfg(not(no_global_oom_handling))]
53#[stable(feature = "rust1", since = "1.0.0")]
54#[doc(no_inline)]
55#[cfg(not(test))]
56pub use linked_list::LinkedList;
57#[cfg(not(no_global_oom_handling))]
58#[stable(feature = "rust1", since = "1.0.0")]
59#[doc(no_inline)]
60#[cfg(not(test))]
61pub use vec_deque::VecDeque;
62
63#[cfg(not(test))]
64use crate::alloc::{Layout, LayoutError};
65
66/// The error type for `try_reserve` methods.
67#[derive(Clone, PartialEq, Eq, Debug)]
68#[stable(feature = "try_reserve", since = "1.57.0")]
69#[cfg(not(test))]
70pub struct TryReserveError {
71    kind: TryReserveErrorKind,
72}
73
74#[cfg(test)]
75pub use realalloc::collections::TryReserveError;
76
77#[cfg(not(test))]
78impl TryReserveError {
79    /// Details about the allocation that caused the error
80    #[inline]
81    #[must_use]
82    #[unstable(
83        feature = "try_reserve_kind",
84        reason = "Uncertain how much info should be exposed",
85        issue = "48043"
86    )]
87    #[rustc_const_unstable(feature = "const_heap", issue = "79597")]
88    pub const fn kind(&self) -> TryReserveErrorKind {
89        self.kind.clone()
90    }
91}
92
93/// Details of the allocation that caused a `TryReserveError`
94#[derive(PartialEq, Eq, Debug)]
95#[unstable(
96    feature = "try_reserve_kind",
97    reason = "Uncertain how much info should be exposed",
98    issue = "48043"
99)]
100#[cfg(not(test))]
101pub enum TryReserveErrorKind {
102    /// Error due to the computed capacity exceeding the collection's maximum
103    /// (usually `isize::MAX` bytes).
104    CapacityOverflow,
105
106    /// The memory allocator returned an error
107    AllocError {
108        /// The layout of allocation request that failed
109        layout: Layout,
110
111        #[doc(hidden)]
112        #[unstable(
113            feature = "container_error_extra",
114            issue = "none",
115            reason = "\
116            Enable exposing the allocator’s custom error value \
117            if an associated type is added in the future: \
118            https://github.com/rust-lang/wg-allocators/issues/23"
119        )]
120        non_exhaustive: (),
121    },
122}
123
124#[unstable(
125    feature = "try_reserve_kind",
126    reason = "Uncertain how much info should be exposed",
127    issue = "48043"
128)]
129#[rustc_const_unstable(feature = "const_heap", issue = "79597")]
130#[cfg(not(test))]
131impl const Clone for TryReserveErrorKind {
132    fn clone(&self) -> Self {
133        match self {
134            TryReserveErrorKind::CapacityOverflow => TryReserveErrorKind::CapacityOverflow,
135            TryReserveErrorKind::AllocError { layout, non_exhaustive: () } => {
136                TryReserveErrorKind::AllocError { layout: *layout, non_exhaustive: () }
137            }
138        }
139    }
140}
141
142#[cfg(test)]
143pub use realalloc::collections::TryReserveErrorKind;
144
145#[unstable(
146    feature = "try_reserve_kind",
147    reason = "Uncertain how much info should be exposed",
148    issue = "48043"
149)]
150#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
151#[cfg(not(test))]
152impl const From<TryReserveErrorKind> for TryReserveError {
153    #[inline]
154    fn from(kind: TryReserveErrorKind) -> Self {
155        Self { kind }
156    }
157}
158
159#[unstable(feature = "try_reserve_kind", issue = "48043")]
160#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
161#[cfg(not(test))]
162impl const From<LayoutError> for TryReserveErrorKind {
163    /// Always evaluates to [`TryReserveErrorKind::CapacityOverflow`].
164    #[inline]
165    fn from(_: LayoutError) -> Self {
166        TryReserveErrorKind::CapacityOverflow
167    }
168}
169
170#[stable(feature = "try_reserve", since = "1.57.0")]
171#[cfg(not(test))]
172impl Display for TryReserveError {
173    fn fmt(
174        &self,
175        fmt: &mut core::fmt::Formatter<'_>,
176    ) -> core::result::Result<(), core::fmt::Error> {
177        fmt.write_str("memory allocation failed")?;
178        let reason = match self.kind {
179            TryReserveErrorKind::CapacityOverflow => {
180                " because the computed capacity exceeded the collection's maximum"
181            }
182            TryReserveErrorKind::AllocError { .. } => {
183                " because the memory allocator returned an error"
184            }
185        };
186        fmt.write_str(reason)
187    }
188}
189
190/// An intermediate trait for specialization of `Extend`.
191#[doc(hidden)]
192#[cfg(not(no_global_oom_handling))]
193trait SpecExtend<I: IntoIterator> {
194    /// Extends `self` with the contents of the given iterator.
195    fn spec_extend(&mut self, iter: I);
196}
197
198#[stable(feature = "try_reserve", since = "1.57.0")]
199#[cfg(not(test))]
200impl core::error::Error for TryReserveError {}
```