---
title: default.rs - source
url: https://doc.rust-lang.org/src/core/default.rs.html#170
source: crawler
fetched_at: 2026-05-06T21:30:01.835431748-03:00
rendered_js: false
word_count: 665
summary: This document defines the Default trait in Rust, which is used to provide a standard default value for types, along with instructions on how to manually implement it or derive it for structs and enums.
tags:
    - rust
    - trait
    - default-trait
    - derive-macro
    - idiomatic-rust
    - type-system
category: reference
---

## core/ default.rs

````rust
1//! The `Default` trait for types with a default value.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5use crate::ascii::Char as AsciiChar;
6
7/// A trait for giving a type a useful default value.
8///
9/// Sometimes, you want to fall back to some kind of default value, and
10/// don't particularly care what it is. This comes up often with `struct`s
11/// that define a set of options:
12///
13/// ```
14/// # #[allow(dead_code)]
15/// struct SomeOptions {
16///     foo: i32,
17///     bar: f32,
18/// }
19/// ```
20///
21/// How can we define some default values? You can use `Default`:
22///
23/// ```
24/// # #[allow(dead_code)]
25/// #[derive(Default)]
26/// struct SomeOptions {
27///     foo: i32,
28///     bar: f32,
29/// }
30///
31/// fn main() {
32///     let options: SomeOptions = Default::default();
33/// }
34/// ```
35///
36/// Now, you get all of the default values. Rust implements `Default` for various primitive types.
37///
38/// If you want to override a particular option, but still retain the other defaults:
39///
40/// ```
41/// # #[allow(dead_code)]
42/// # #[derive(Default)]
43/// # struct SomeOptions {
44/// #     foo: i32,
45/// #     bar: f32,
46/// # }
47/// fn main() {
48///     let options = SomeOptions { foo: 42, ..Default::default() };
49/// }
50/// ```
51///
52/// ## Derivable
53///
54/// This trait can be used with `#[derive]` if all of the type's fields implement
55/// `Default`. When `derive`d, it will use the default value for each field's type.
56///
57/// ### `enum`s
58///
59/// When using `#[derive(Default)]` on an `enum`, you need to choose which unit variant will be
60/// default. You do this by placing the `#[default]` attribute on the variant.
61///
62/// ```
63/// #[derive(Default)]
64/// enum Kind {
65///     #[default]
66///     A,
67///     B,
68///     C,
69/// }
70/// ```
71///
72/// You cannot use the `#[default]` attribute on non-unit or non-exhaustive variants.
73///
74/// The `#[default]` attribute was stabilized in Rust 1.62.0.
75///
76/// ## How can I implement `Default`?
77///
78/// Provide an implementation for the `default()` method that returns the value of
79/// your type that should be the default:
80///
81/// ```
82/// # #![allow(dead_code)]
83/// enum Kind {
84///     A,
85///     B,
86///     C,
87/// }
88///
89/// impl Default for Kind {
90///     fn default() -> Self { Kind::A }
91/// }
92/// ```
93///
94/// # Examples
95///
96/// ```
97/// # #[allow(dead_code)]
98/// #[derive(Default)]
99/// struct SomeOptions {
100///     foo: i32,
101///     bar: f32,
102/// }
103/// ```
104#[rustc_diagnostic_item = "Default"]
105#[stable(feature = "rust1", since = "1.0.0")]
106#[rustc_const_unstable(feature = "const_default", issue = "143894")]
107pub const trait Default: Sized {
108    /// Returns the "default value" for a type.
109    ///
110    /// Default values are often some kind of initial value, identity value, or anything else that
111    /// may make sense as a default.
112    ///
113    /// # Examples
114    ///
115    /// Using built-in default values:
116    ///
117    /// ```
118    /// let i: i8 = Default::default();
119    /// let (x, y): (Option<String>, f64) = Default::default();
120    /// let (a, b, (c, d)): (i32, u32, (bool, bool)) = Default::default();
121    /// ```
122    ///
123    /// Making your own:
124    ///
125    /// ```
126    /// # #[allow(dead_code)]
127    /// enum Kind {
128    ///     A,
129    ///     B,
130    ///     C,
131    /// }
132    ///
133    /// impl Default for Kind {
134    ///     fn default() -> Self { Kind::A }
135    /// }
136    /// ```
137    #[stable(feature = "rust1", since = "1.0.0")]
138    #[rustc_diagnostic_item = "default_fn"]
139    fn default() -> Self;
140}
141
142/// Derive macro generating an impl of the trait `Default`.
143#[rustc_builtin_macro(Default, attributes(default))]
144#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
145#[allow_internal_unstable(core_intrinsics)]
146pub macro Default($item:item) {
147    /* compiler built-in */
148}
149
150macro_rules! default_impl {
151    ($t:ty, $v:expr, $doc:tt) => {
152        #[stable(feature = "rust1", since = "1.0.0")]
153        #[rustc_const_unstable(feature = "const_default", issue = "143894")]
154        impl const Default for $t {
155            #[inline(always)]
156            #[doc = $doc]
157            fn default() -> $t {
158                $v
159            }
160        }
161    };
162}
163
164default_impl! { (), (), "Returns the default value of `()`" }
165default_impl! { bool, false, "Returns the default value of `false`" }
166default_impl! { char, '\x00', "Returns the default value of `\\x00`" }
167default_impl! { AsciiChar, AsciiChar::Null, "Returns the default value of `Null`" }
168
169default_impl! { usize, 0, "Returns the default value of `0`" }
170default_impl! { u8, 0, "Returns the default value of `0`" }
171default_impl! { u16, 0, "Returns the default value of `0`" }
172default_impl! { u32, 0, "Returns the default value of `0`" }
173default_impl! { u64, 0, "Returns the default value of `0`" }
174default_impl! { u128, 0, "Returns the default value of `0`" }
175
176default_impl! { isize, 0, "Returns the default value of `0`" }
177default_impl! { i8, 0, "Returns the default value of `0`" }
178default_impl! { i16, 0, "Returns the default value of `0`" }
179default_impl! { i32, 0, "Returns the default value of `0`" }
180default_impl! { i64, 0, "Returns the default value of `0`" }
181default_impl! { i128, 0, "Returns the default value of `0`" }
182
183default_impl! { f16, 0.0f16, "Returns the default value of `0.0`" }
184default_impl! { f32, 0.0f32, "Returns the default value of `0.0`" }
185default_impl! { f64, 0.0f64, "Returns the default value of `0.0`" }
186default_impl! { f128, 0.0f128, "Returns the default value of `0.0`" }
````