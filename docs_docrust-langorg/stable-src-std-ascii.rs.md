---
title: ascii.rs - source
url: https://doc.rust-lang.org/stable/src/std/ascii.rs.html#206-210
source: crawler
fetched_at: 2026-05-06T21:33:33.800044715-03:00
rendered_js: false
word_count: 1013
summary: This document defines the AsciiExt trait, which provides methods for performing ASCII-specific case transformations and comparisons on strings and characters in Rust.
tags:
    - rust
    - ascii
    - string-manipulation
    - deprecated-api
    - character-encoding
category: reference
---

## std/ ascii.rs

````rust
1//! Operations on ASCII strings and characters.
2//!
3//! Most string operations in Rust act on UTF-8 strings. However, at times it
4//! makes more sense to only consider the ASCII character set for a specific
5//! operation.
6//!
7//! The [`AsciiExt`] trait provides methods that allow for character
8//! operations that only act on the ASCII subset and leave non-ASCII characters
9//! alone.
10//!
11//! The [`escape_default`] function provides an iterator over the bytes of an
12//! escaped version of the character given.
13
14#![stable(feature = "rust1", since = "1.0.0")]
15
16#[unstable(feature = "ascii_char", issue = "110998")]
17pub use core::ascii::Char;
18#[stable(feature = "rust1", since = "1.0.0")]
19pub use core::ascii::{EscapeDefault, escape_default};
20
21/// Extension methods for ASCII-subset only operations.
22///
23/// Be aware that operations on seemingly non-ASCII characters can sometimes
24/// have unexpected results. Consider this example:
25///
26/// ```
27/// use std::ascii::AsciiExt;
28///
29/// assert_eq!(AsciiExt::to_ascii_uppercase("café"), "CAFÉ");
30/// assert_eq!(AsciiExt::to_ascii_uppercase("café"), "CAFé");
31/// ```
32///
33/// In the first example, the lowercased string is represented `"cafe\u{301}"`
34/// (the last character is an acute accent [combining character]). Unlike the
35/// other characters in the string, the combining character will not get mapped
36/// to an uppercase variant, resulting in `"CAFE\u{301}"`. In the second
37/// example, the lowercased string is represented `"caf\u{e9}"` (the last
38/// character is a single Unicode character representing an 'e' with an acute
39/// accent). Since the last character is defined outside the scope of ASCII,
40/// it will not get mapped to an uppercase variant, resulting in `"CAF\u{e9}"`.
41///
42/// [combining character]: https://en.wikipedia.org/wiki/Combining_character
43#[stable(feature = "rust1", since = "1.0.0")]
44#[deprecated(since = "1.26.0", note = "use inherent methods instead")]
45pub trait AsciiExt {
46    /// Container type for copied ASCII characters.
47    #[stable(feature = "rust1", since = "1.0.0")]
48    type Owned;
49
50    /// Checks if the value is within the ASCII range.
51    ///
52    /// # Note
53    ///
54    /// This method is deprecated in favor of the identically-named
55    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
56    #[stable(feature = "rust1", since = "1.0.0")]
57    fn is_ascii(&self) -> bool;
58
59    /// Makes a copy of the value in its ASCII upper case equivalent.
60    ///
61    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
62    /// but non-ASCII letters are unchanged.
63    ///
64    /// To uppercase the value in-place, use [`make_ascii_uppercase`].
65    ///
66    /// To uppercase ASCII characters in addition to non-ASCII characters, use
67    /// [`str::to_uppercase`].
68    ///
69    /// # Note
70    ///
71    /// This method is deprecated in favor of the identically-named
72    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
73    ///
74    /// [`make_ascii_uppercase`]: AsciiExt::make_ascii_uppercase
75    #[stable(feature = "rust1", since = "1.0.0")]
76    #[allow(deprecated)]
77    fn to_ascii_uppercase(&self) -> Self::Owned;
78
79    /// Makes a copy of the value in its ASCII lower case equivalent.
80    ///
81    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
82    /// but non-ASCII letters are unchanged.
83    ///
84    /// To lowercase the value in-place, use [`make_ascii_lowercase`].
85    ///
86    /// To lowercase ASCII characters in addition to non-ASCII characters, use
87    /// [`str::to_lowercase`].
88    ///
89    /// # Note
90    ///
91    /// This method is deprecated in favor of the identically-named
92    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
93    ///
94    /// [`make_ascii_lowercase`]: AsciiExt::make_ascii_lowercase
95    #[stable(feature = "rust1", since = "1.0.0")]
96    #[allow(deprecated)]
97    fn to_ascii_lowercase(&self) -> Self::Owned;
98
99    /// Checks that two values are an ASCII case-insensitive match.
100    ///
101    /// Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`,
102    /// but without allocating and copying temporaries.
103    ///
104    /// # Note
105    ///
106    /// This method is deprecated in favor of the identically-named
107    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
108    #[stable(feature = "rust1", since = "1.0.0")]
109    fn eq_ignore_ascii_case(&self, other: &Self) -> bool;
110
111    /// Converts this type to its ASCII upper case equivalent in-place.
112    ///
113    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
114    /// but non-ASCII letters are unchanged.
115    ///
116    /// To return a new uppercased value without modifying the existing one, use
117    /// [`to_ascii_uppercase`].
118    ///
119    /// # Note
120    ///
121    /// This method is deprecated in favor of the identically-named
122    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
123    ///
124    /// [`to_ascii_uppercase`]: AsciiExt::to_ascii_uppercase
125    #[stable(feature = "ascii", since = "1.9.0")]
126    fn make_ascii_uppercase(&mut self);
127
128    /// Converts this type to its ASCII lower case equivalent in-place.
129    ///
130    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
131    /// but non-ASCII letters are unchanged.
132    ///
133    /// To return a new lowercased value without modifying the existing one, use
134    /// [`to_ascii_lowercase`].
135    ///
136    /// # Note
137    ///
138    /// This method is deprecated in favor of the identically-named
139    /// inherent methods on `u8`, `char`, `[u8]` and `str`.
140    ///
141    /// [`to_ascii_lowercase`]: AsciiExt::to_ascii_lowercase
142    #[stable(feature = "ascii", since = "1.9.0")]
143    fn make_ascii_lowercase(&mut self);
144}
145
146macro_rules! delegating_ascii_methods {
147    () => {
148        #[inline]
149        fn is_ascii(&self) -> bool {
150            self.is_ascii()
151        }
152
153        #[inline]
154        fn to_ascii_uppercase(&self) -> Self::Owned {
155            self.to_ascii_uppercase()
156        }
157
158        #[inline]
159        fn to_ascii_lowercase(&self) -> Self::Owned {
160            self.to_ascii_lowercase()
161        }
162
163        #[inline]
164        fn eq_ignore_ascii_case(&self, o: &Self) -> bool {
165            self.eq_ignore_ascii_case(o)
166        }
167
168        #[inline]
169        fn make_ascii_uppercase(&mut self) {
170            self.make_ascii_uppercase();
171        }
172
173        #[inline]
174        fn make_ascii_lowercase(&mut self) {
175            self.make_ascii_lowercase();
176        }
177    };
178}
179
180#[stable(feature = "rust1", since = "1.0.0")]
181#[allow(deprecated)]
182impl AsciiExt for u8 {
183    type Owned = u8;
184
185    delegating_ascii_methods!();
186}
187
188#[stable(feature = "rust1", since = "1.0.0")]
189#[allow(deprecated)]
190impl AsciiExt for char {
191    type Owned = char;
192
193    delegating_ascii_methods!();
194}
195
196#[stable(feature = "rust1", since = "1.0.0")]
197#[allow(deprecated)]
198impl AsciiExt for [u8] {
199    type Owned = Vec<u8>;
200
201    delegating_ascii_methods!();
202}
203
204#[stable(feature = "rust1", since = "1.0.0")]
205#[allow(deprecated)]
206impl AsciiExt for str {
207    type Owned = String;
208
209    delegating_ascii_methods!();
210}
````