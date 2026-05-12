---
title: cast.rs - source
url: https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/cast.rs.html#33
source: crawler
fetched_at: 2026-05-06T21:30:41.166068414-03:00
rendered_js: false
word_count: 364
summary: Defines the SimdCast trait and its sealed implementation for primitive numeric types, enabling safe type casting for SIMD vector elements.
tags:
    - rust
    - simd
    - type-casting
    - trait-system
    - vectorization
    - core-library
category: reference
---

## core/portable-simd/crates/core\_simd/src/ cast.rs

```rust
1use crate::simd::SimdElement;
2
3mod sealed {
4    /// Cast vector elements to other types.
5    ///
6    /// # Safety
7    /// Implementing this trait asserts that the type is a valid vector element for the `simd_cast`
8    /// or `simd_as` intrinsics.
9    pub unsafe trait Sealed {}
10}
11use sealed::Sealed;
12
13/// Supporting trait for `Simd::cast`.  Typically doesn't need to be used directly.
14pub trait SimdCast: Sealed + SimdElement {}
15
16// Safety: primitive number types can be cast to other primitive number types
17unsafe impl Sealed for i8 {}
18impl SimdCast for i8 {}
19// Safety: primitive number types can be cast to other primitive number types
20unsafe impl Sealed for i16 {}
21impl SimdCast for i16 {}
22// Safety: primitive number types can be cast to other primitive number types
23unsafe impl Sealed for i32 {}
24impl SimdCast for i32 {}
25// Safety: primitive number types can be cast to other primitive number types
26unsafe impl Sealed for i64 {}
27impl SimdCast for i64 {}
28// Safety: primitive number types can be cast to other primitive number types
29unsafe impl Sealed for isize {}
30impl SimdCast for isize {}
31// Safety: primitive number types can be cast to other primitive number types
32unsafe impl Sealed for u8 {}
33impl SimdCast for u8 {}
34// Safety: primitive number types can be cast to other primitive number types
35unsafe impl Sealed for u16 {}
36impl SimdCast for u16 {}
37// Safety: primitive number types can be cast to other primitive number types
38unsafe impl Sealed for u32 {}
39impl SimdCast for u32 {}
40// Safety: primitive number types can be cast to other primitive number types
41unsafe impl Sealed for u64 {}
42impl SimdCast for u64 {}
43// Safety: primitive number types can be cast to other primitive number types
44unsafe impl Sealed for usize {}
45impl SimdCast for usize {}
46// Safety: primitive number types can be cast to other primitive number types
47unsafe impl Sealed for f32 {}
48impl SimdCast for f32 {}
49// Safety: primitive number types can be cast to other primitive number types
50unsafe impl Sealed for f64 {}
51impl SimdCast for f64 {}
```