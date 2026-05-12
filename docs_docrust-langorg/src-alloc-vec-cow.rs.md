---
title: cow.rs - source
url: https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#38
source: crawler
fetched_at: 2026-05-06T21:30:59.512002346-03:00
rendered_js: false
word_count: 303
summary: This document defines the From and FromIterator trait implementations for the Cow (Clone-on-Write) smart pointer, allowing efficient conversion from various slice, array, and vector types.
tags:
    - rust
    - memory-management
    - smart-pointers
    - cow
    - traits
    - standard-library
category: reference
---

## alloc/vec/ cow.rs

```rust
1use super::Vec;
2use crate::borrow::Cow;
3
4#[stable(feature = "cow_from_vec", since = "1.8.0")]
5impl<'a, T: Clone> From<&'a [T]> for Cow<'a, [T]> {
6    /// Creates a [`Borrowed`] variant of [`Cow`]
7    /// from a slice.
8    ///
9    /// This conversion does not allocate or clone the data.
10    ///
11    /// [`Borrowed`]: crate::borrow::Cow::Borrowed
12    fn from(s: &'a [T]) -> Cow<'a, [T]> {
13        Cow::Borrowed(s)
14    }
15}
16
17#[stable(feature = "cow_from_array_ref", since = "1.77.0")]
18impl<'a, T: Clone, const N: usize> From<&'a [T; N]> for Cow<'a, [T]> {
19    /// Creates a [`Borrowed`] variant of [`Cow`]
20    /// from a reference to an array.
21    ///
22    /// This conversion does not allocate or clone the data.
23    ///
24    /// [`Borrowed`]: crate::borrow::Cow::Borrowed
25    fn from(s: &'a [T; N]) -> Cow<'a, [T]> {
26        Cow::Borrowed(s as &[_])
27    }
28}
29
30#[stable(feature = "cow_from_vec", since = "1.8.0")]
31impl<'a, T: Clone> From<Vec<T>> for Cow<'a, [T]> {
32    /// Creates an [`Owned`] variant of [`Cow`]
33    /// from an owned instance of [`Vec`].
34    ///
35    /// This conversion does not allocate or clone the data.
36    ///
37    /// [`Owned`]: crate::borrow::Cow::Owned
38    fn from(v: Vec<T>) -> Cow<'a, [T]> {
39        Cow::Owned(v)
40    }
41}
42
43#[stable(feature = "cow_from_vec_ref", since = "1.28.0")]
44impl<'a, T: Clone> From<&'a Vec<T>> for Cow<'a, [T]> {
45    /// Creates a [`Borrowed`] variant of [`Cow`]
46    /// from a reference to [`Vec`].
47    ///
48    /// This conversion does not allocate or clone the data.
49    ///
50    /// [`Borrowed`]: crate::borrow::Cow::Borrowed
51    fn from(v: &'a Vec<T>) -> Cow<'a, [T]> {
52        Cow::Borrowed(v.as_slice())
53    }
54}
55
56#[stable(feature = "rust1", since = "1.0.0")]
57impl<'a, T> FromIterator<T> for Cow<'a, [T]>
58where
59    T: Clone,
60{
61    fn from_iter<I: IntoIterator<Item = T>>(it: I) -> Cow<'a, [T]> {
62        Cow::Owned(FromIterator::from_iter(it))
63    }
64}
```