---
title: iter.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/boxed/iter.rs.html#151
source: crawler
fetched_at: 2026-05-06T21:34:04.739233629-03:00
rendered_js: false
word_count: 836
summary: This document defines standard library iterator implementations for boxed types in Rust, including support for iteration, double-ended iteration, and collection from iterators into boxed slices and strings.
tags:
    - rust
    - iterator
    - boxed
    - memory-allocation
    - standard-library
    - traits
category: reference
---

## alloc/boxed/ iter.rs

```rust
1use core::async_iter::AsyncIterator;
2use core::iter::FusedIterator;
3use core::pin::Pin;
4use core::slice;
5use core::task::{Context, Poll};
6
7use crate::alloc::Allocator;
8#[cfg(not(no_global_oom_handling))]
9use crate::borrow::Cow;
10use crate::boxed::Box;
11#[cfg(not(no_global_oom_handling))]
12use crate::string::String;
13use crate::vec;
14#[cfg(not(no_global_oom_handling))]
15use crate::vec::Vec;
16
17#[stable(feature = "rust1", since = "1.0.0")]
18impl<I: Iterator + ?Sized, A: Allocator> Iterator for Box<I, A> {
19    type Item = I::Item;
20    fn next(&mut self) -> Option<I::Item> {
21        (**self).next()
22    }
23    fn size_hint(&self) -> (usize, Option<usize>) {
24        (**self).size_hint()
25    }
26    fn nth(&mut self, n: usize) -> Option<I::Item> {
27        (**self).nth(n)
28    }
29    fn last(self) -> Option<I::Item> {
30        BoxIter::last(self)
31    }
32}
33
34trait BoxIter {
35    type Item;
36    fn last(self) -> Option<Self::Item>;
37}
38
39impl<I: Iterator + ?Sized, A: Allocator> BoxIter for Box<I, A> {
40    type Item = I::Item;
41    default fn last(self) -> Option<I::Item> {
42        #[inline]
43        fn some<T>(_: Option<T>, x: T) -> Option<T> {
44            Some(x)
45        }
46
47        self.fold(None, some)
48    }
49}
50
51/// Specialization for sized `I`s that uses `I`s implementation of `last()`
52/// instead of the default.
53#[stable(feature = "rust1", since = "1.0.0")]
54impl<I: Iterator, A: Allocator> BoxIter for Box<I, A> {
55    fn last(self) -> Option<I::Item> {
56        (*self).last()
57    }
58}
59
60#[stable(feature = "rust1", since = "1.0.0")]
61impl<I: DoubleEndedIterator + ?Sized, A: Allocator> DoubleEndedIterator for Box<I, A> {
62    fn next_back(&mut self) -> Option<I::Item> {
63        (**self).next_back()
64    }
65    fn nth_back(&mut self, n: usize) -> Option<I::Item> {
66        (**self).nth_back(n)
67    }
68}
69#[stable(feature = "rust1", since = "1.0.0")]
70impl<I: ExactSizeIterator + ?Sized, A: Allocator> ExactSizeIterator for Box<I, A> {
71    fn len(&self) -> usize {
72        (**self).len()
73    }
74    fn is_empty(&self) -> bool {
75        (**self).is_empty()
76    }
77}
78
79#[stable(feature = "fused", since = "1.26.0")]
80impl<I: FusedIterator + ?Sized, A: Allocator> FusedIterator for Box<I, A> {}
81
82#[unstable(feature = "async_iterator", issue = "79024")]
83impl<S: ?Sized + AsyncIterator + Unpin> AsyncIterator for Box<S> {
84    type Item = S::Item;
85
86    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {
87        Pin::new(&mut **self).poll_next(cx)
88    }
89
90    fn size_hint(&self) -> (usize, Option<usize>) {
91        (**self).size_hint()
92    }
93}
94
95/// This implementation is required to make sure that the `Box<[I]>: IntoIterator`
96/// implementation doesn't overlap with `IntoIterator for T where T: Iterator` blanket.
97#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
98impl<I, A: Allocator> !Iterator for Box<[I], A> {}
99
100/// This implementation is required to make sure that the `&Box<[I]>: IntoIterator`
101/// implementation doesn't overlap with `IntoIterator for T where T: Iterator` blanket.
102#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
103impl<'a, I, A: Allocator> !Iterator for &'a Box<[I], A> {}
104
105/// This implementation is required to make sure that the `&mut Box<[I]>: IntoIterator`
106/// implementation doesn't overlap with `IntoIterator for T where T: Iterator` blanket.
107#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
108impl<'a, I, A: Allocator> !Iterator for &'a mut Box<[I], A> {}
109
110// Note: the `#[rustc_skip_during_method_dispatch(boxed_slice)]` on `trait IntoIterator`
111// hides this implementation from explicit `.into_iter()` calls on editions < 2024,
112// so those calls will still resolve to the slice implementation, by reference.
113#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
114impl<I, A: Allocator> IntoIterator for Box<[I], A> {
115    type IntoIter = vec::IntoIter<I, A>;
116    type Item = I;
117    fn into_iter(self) -> vec::IntoIter<I, A> {
118        self.into_vec().into_iter()
119    }
120}
121
122#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
123impl<'a, I, A: Allocator> IntoIterator for &'a Box<[I], A> {
124    type IntoIter = slice::Iter<'a, I>;
125    type Item = &'a I;
126    fn into_iter(self) -> slice::Iter<'a, I> {
127        self.iter()
128    }
129}
130
131#[stable(feature = "boxed_slice_into_iter", since = "1.80.0")]
132impl<'a, I, A: Allocator> IntoIterator for &'a mut Box<[I], A> {
133    type IntoIter = slice::IterMut<'a, I>;
134    type Item = &'a mut I;
135    fn into_iter(self) -> slice::IterMut<'a, I> {
136        self.iter_mut()
137    }
138}
139
140#[cfg(not(no_global_oom_handling))]
141#[stable(feature = "boxed_slice_from_iter", since = "1.32.0")]
142impl<I> FromIterator<I> for Box<[I]> {
143    fn from_iter<T: IntoIterator<Item = I>>(iter: T) -> Self {
144        iter.into_iter().collect::<Vec<_>>().into_boxed_slice()
145    }
146}
147
148#[cfg(not(no_global_oom_handling))]
149#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
150impl FromIterator<char> for Box<str> {
151    fn from_iter<T: IntoIterator<Item = char>>(iter: T) -> Self {
152        String::from_iter(iter).into_boxed_str()
153    }
154}
155
156#[cfg(not(no_global_oom_handling))]
157#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
158impl<'a> FromIterator<&'a char> for Box<str> {
159    fn from_iter<T: IntoIterator<Item = &'a char>>(iter: T) -> Self {
160        String::from_iter(iter).into_boxed_str()
161    }
162}
163
164#[cfg(not(no_global_oom_handling))]
165#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
166impl<'a> FromIterator<&'a str> for Box<str> {
167    fn from_iter<T: IntoIterator<Item = &'a str>>(iter: T) -> Self {
168        String::from_iter(iter).into_boxed_str()
169    }
170}
171
172#[cfg(not(no_global_oom_handling))]
173#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
174impl FromIterator<String> for Box<str> {
175    fn from_iter<T: IntoIterator<Item = String>>(iter: T) -> Self {
176        String::from_iter(iter).into_boxed_str()
177    }
178}
179
180#[cfg(not(no_global_oom_handling))]
181#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
182impl<A: Allocator> FromIterator<Box<str, A>> for Box<str> {
183    fn from_iter<T: IntoIterator<Item = Box<str, A>>>(iter: T) -> Self {
184        String::from_iter(iter).into_boxed_str()
185    }
186}
187
188#[cfg(not(no_global_oom_handling))]
189#[stable(feature = "boxed_str_from_iter", since = "1.80.0")]
190impl<'a> FromIterator<Cow<'a, str>> for Box<str> {
191    fn from_iter<T: IntoIterator<Item = Cow<'a, str>>>(iter: T) -> Self {
192        String::from_iter(iter).into_boxed_str()
193    }
194}
```