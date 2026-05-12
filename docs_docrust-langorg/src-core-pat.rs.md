---
title: pat.rs - source
url: https://doc.rust-lang.org/src/core/pat.rs.html#72
source: crawler
fetched_at: 2026-05-06T21:29:24.281777053-03:00
rendered_js: false
word_count: 399
summary: Defines the internal pattern_type macro and the RangePattern trait to support compiler-level validation and range-based pattern types for integers and characters.
tags:
    - rust-core
    - pattern-types
    - compiler-macro
    - range-pattern
    - trait-implementation
category: reference
---

## core/ pat.rs

````rust
1//! Helper module for exporting the `pattern_type` macro
2
3use crate::marker::{Freeze, PointeeSized, Unsize};
4use crate::ops::{CoerceUnsized, DispatchFromDyn};
5
6/// Creates a pattern type.
7/// ```ignore (cannot test this from within core yet)
8/// type Positive = std::pat::pattern_type!(i32 is 1..);
9/// ```
10#[macro_export]
11#[rustc_builtin_macro(pattern_type)]
12#[unstable(feature = "pattern_type_macro", issue = "123646")]
13macro_rules! pattern_type {
14    ($($arg:tt)*) => {
15        /* compiler built-in */
16    };
17}
18
19/// A trait implemented for integer types and `char`.
20/// Useful in the future for generic pattern types, but
21/// used right now to simplify ast lowering of pattern type ranges.
22#[unstable(feature = "pattern_type_range_trait", issue = "123646")]
23#[rustc_const_unstable(feature = "pattern_type_range_trait", issue = "123646")]
24#[diagnostic::on_unimplemented(
25    message = "`{Self}` is not a valid base type for range patterns",
26    label = "only integer types and `char` are supported"
27)]
28pub const trait RangePattern {
29    /// Trait version of the inherent `MIN` assoc const.
30    #[lang = "RangeMin"]
31    const MIN: Self;
32
33    /// Trait version of the inherent `MIN` assoc const.
34    #[lang = "RangeMax"]
35    const MAX: Self;
36
37    /// A compile-time helper to subtract 1 for exclusive ranges.
38    #[lang = "RangeSub"]
39    #[track_caller]
40    fn sub_one(self) -> Self;
41}
42
43macro_rules! impl_range_pat {
44    ($($ty:ty,)*) => {
45        $(
46            #[rustc_const_unstable(feature = "pattern_type_range_trait", issue = "123646")]
47            impl const RangePattern for $ty {
48                const MIN: $ty = <$ty>::MIN;
49                const MAX: $ty = <$ty>::MAX;
50                fn sub_one(self) -> Self {
51                    match self.checked_sub(1) {
52                        Some(val) => val,
53                        None => panic!("exclusive range end at minimum value of type")
54                    }
55                }
56            }
57        )*
58    }
59}
60
61impl_range_pat! {
62    i8, i16, i32, i64, i128, isize,
63    u8, u16, u32, u64, u128, usize,
64}
65
66#[rustc_const_unstable(feature = "pattern_type_range_trait", issue = "123646")]
67impl const RangePattern for char {
68    const MIN: Self = char::MIN;
69
70    const MAX: Self = char::MAX;
71
72    fn sub_one(self) -> Self {
73        match char::from_u32(self as u32 - 1) {
74            None => panic!("exclusive range to start of valid chars"),
75            Some(val) => val,
76        }
77    }
78}
79
80impl<T: PointeeSized, U: PointeeSized> CoerceUnsized<pattern_type!(*const U is !null)> for pattern_type!(*const T is !null) where
81    T: Unsize<U>
82{
83}
84
85impl<T: DispatchFromDyn<U>, U> DispatchFromDyn<pattern_type!(U is !null)> for pattern_type!(T is !null) {}
86
87impl<T: PointeeSized> Unpin for pattern_type!(*const T is !null) {}
88
89unsafe impl<T: PointeeSized> Freeze for pattern_type!(*const T is !null) {}
90
91unsafe impl<T: PointeeSized> Freeze for pattern_type!(*mut T is !null) {}
````