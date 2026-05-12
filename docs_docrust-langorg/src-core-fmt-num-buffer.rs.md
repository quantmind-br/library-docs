---
title: num_buffer.rs - source
url: https://doc.rust-lang.org/src/core/fmt/num_buffer.rs.html#26-33
source: crawler
fetched_at: 2026-05-06T21:30:20.724015516-03:00
rendered_js: false
word_count: 310
summary: This document defines the NumBufferTrait and NumBuffer structure in Rust to manage memory buffers specifically sized for the decimal representation of integer types.
tags:
    - rust-core
    - integer-formatting
    - buffer-management
    - memory-layout
    - type-traits
category: reference
---

## core/fmt/ num\_buffer.rs

```rust
1use crate::mem::MaybeUninit;
2
3/// Trait used to describe the maximum number of digits in decimal base of the implemented integer.
4#[unstable(feature = "int_format_into", issue = "138215")]
5pub trait NumBufferTrait {
6    /// Maximum number of digits in decimal base of the implemented integer.
7    const BUF_SIZE: usize;
8}
9
10macro_rules! impl_NumBufferTrait {
11    ($($signed:ident, $unsigned:ident,)*) => {
12        $(
13            #[unstable(feature = "int_format_into", issue = "138215")]
14            impl NumBufferTrait for $signed {
15                // `+ 2` and not `+ 1` to include the `-` character.
16                const BUF_SIZE: usize = $signed::MAX.ilog(10) as usize + 2;
17            }
18            #[unstable(feature = "int_format_into", issue = "138215")]
19            impl NumBufferTrait for $unsigned {
20                const BUF_SIZE: usize = $unsigned::MAX.ilog(10) as usize + 1;
21            }
22        )*
23    }
24}
25
26impl_NumBufferTrait! {
27    i8, u8,
28    i16, u16,
29    i32, u32,
30    i64, u64,
31    isize, usize,
32    i128, u128,
33}
34
35/// A buffer wrapper of which the internal size is based on the maximum
36/// number of digits the associated integer can have.
37#[unstable(feature = "int_format_into", issue = "138215")]
38#[derive(Debug)]
39pub struct NumBuffer<T: NumBufferTrait> {
40    // FIXME: Once const generics feature is working, use `T::BUF_SIZE` instead of 40.
41    pub(crate) buf: [MaybeUninit<u8>; 40],
42    // FIXME: Remove this field once we can actually use `T`.
43    phantom: core::marker::PhantomData<T>,
44}
45
46#[unstable(feature = "int_format_into", issue = "138215")]
47impl<T: NumBufferTrait> NumBuffer<T> {
48    /// Initializes internal buffer.
49    #[unstable(feature = "int_format_into", issue = "138215")]
50    pub const fn new() -> Self {
51        // FIXME: Once const generics feature is working, use `T::BUF_SIZE` instead of 40.
52        NumBuffer { buf: [MaybeUninit::<u8>::uninit(); 40], phantom: core::marker::PhantomData }
53    }
54
55    /// Returns the length of the internal buffer.
56    #[unstable(feature = "int_format_into", issue = "138215")]
57    pub const fn capacity(&self) -> usize {
58        self.buf.len()
59    }
60}
```