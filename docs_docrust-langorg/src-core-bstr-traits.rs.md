---
title: traits.rs - source
url: https://doc.rust-lang.org/src/core/bstr/traits.rs.html#135
source: crawler
fetched_at: 2026-05-06T21:27:33.163250686-03:00
rendered_js: false
word_count: 1037
summary: This document defines core trait implementations for the ByteStr type in Rust, including comparison, hashing, and indexing capabilities, along with internal helper macros for trait boilerplate.
tags:
    - rust
    - bytestr
    - trait-implementation
    - indexing
    - generic-programming
    - macro-development
category: reference
---

## core/bstr/ traits.rs

```rust
1//! Trait implementations for `ByteStr`.
2
3use crate::bstr::ByteStr;
4use crate::cmp::Ordering;
5use crate::slice::SliceIndex;
6use crate::{hash, ops, range};
7
8#[unstable(feature = "bstr", issue = "134915")]
9impl Ord for ByteStr {
10    #[inline]
11    fn cmp(&self, other: &ByteStr) -> Ordering {
12        Ord::cmp(&self.0, &other.0)
13    }
14}
15
16#[unstable(feature = "bstr", issue = "134915")]
17impl PartialOrd for ByteStr {
18    #[inline]
19    fn partial_cmp(&self, other: &ByteStr) -> Option<Ordering> {
20        PartialOrd::partial_cmp(&self.0, &other.0)
21    }
22}
23
24#[unstable(feature = "bstr", issue = "134915")]
25impl PartialEq<ByteStr> for ByteStr {
26    #[inline]
27    fn eq(&self, other: &ByteStr) -> bool {
28        &self.0 == &other.0
29    }
30}
31
32#[unstable(feature = "bstr", issue = "134915")]
33impl Eq for ByteStr {}
34
35#[unstable(feature = "bstr", issue = "134915")]
36impl hash::Hash for ByteStr {
37    #[inline]
38    fn hash<H: hash::Hasher>(&self, state: &mut H) {
39        self.0.hash(state);
40    }
41}
42
43#[doc(hidden)]
44#[macro_export]
45#[unstable(feature = "bstr_internals", issue = "none")]
46macro_rules! impl_partial_eq {
47    ($lhs:ty, $rhs:ty) => {
48        impl PartialEq<$rhs> for $lhs {
49            #[inline]
50            fn eq(&self, other: &$rhs) -> bool {
51                let other: &[u8] = other.as_ref();
52                PartialEq::eq(self.as_bytes(), other)
53            }
54        }
55
56        impl PartialEq<$lhs> for $rhs {
57            #[inline]
58            fn eq(&self, other: &$lhs) -> bool {
59                let this: &[u8] = self.as_ref();
60                PartialEq::eq(this, other.as_bytes())
61            }
62        }
63    };
64}
65
66#[doc(hidden)]
67#[unstable(feature = "bstr_internals", issue = "none")]
68pub use impl_partial_eq;
69
70#[doc(hidden)]
71#[macro_export]
72#[unstable(feature = "bstr_internals", issue = "none")]
73macro_rules! impl_partial_eq_ord {
74    ($lhs:ty, $rhs:ty) => {
75        $crate::bstr::impl_partial_eq!($lhs, $rhs);
76
77        #[unstable(feature = "bstr", issue = "134915")]
78        impl PartialOrd<$rhs> for $lhs {
79            #[inline]
80            fn partial_cmp(&self, other: &$rhs) -> Option<Ordering> {
81                let other: &[u8] = other.as_ref();
82                PartialOrd::partial_cmp(self.as_bytes(), other)
83            }
84        }
85
86        #[unstable(feature = "bstr", issue = "134915")]
87        impl PartialOrd<$lhs> for $rhs {
88            #[inline]
89            fn partial_cmp(&self, other: &$lhs) -> Option<Ordering> {
90                let this: &[u8] = self.as_ref();
91                PartialOrd::partial_cmp(this, other.as_bytes())
92            }
93        }
94    };
95}
96
97#[doc(hidden)]
98#[unstable(feature = "bstr_internals", issue = "none")]
99pub use impl_partial_eq_ord;
100
101#[doc(hidden)]
102#[macro_export]
103#[unstable(feature = "bstr_internals", issue = "none")]
104macro_rules! impl_partial_eq_n {
105    ($lhs:ty, $rhs:ty) => {
106        #[unstable(feature = "bstr", issue = "134915")]
107        impl<const N: usize> PartialEq<$rhs> for $lhs {
108            #[inline]
109            fn eq(&self, other: &$rhs) -> bool {
110                let other: &[u8] = other.as_ref();
111                PartialEq::eq(self.as_bytes(), other)
112            }
113        }
114
115        #[unstable(feature = "bstr", issue = "134915")]
116        impl<const N: usize> PartialEq<$lhs> for $rhs {
117            #[inline]
118            fn eq(&self, other: &$lhs) -> bool {
119                let this: &[u8] = self.as_ref();
120                PartialEq::eq(this, other.as_bytes())
121            }
122        }
123    };
124}
125
126#[doc(hidden)]
127#[unstable(feature = "bstr_internals", issue = "none")]
128pub use impl_partial_eq_n;
129
130// PartialOrd with `[u8]` omitted to avoid inference failures
131impl_partial_eq!(ByteStr, [u8]);
132// PartialOrd with `&[u8]` omitted to avoid inference failures
133impl_partial_eq!(ByteStr, &[u8]);
134// PartialOrd with `str` omitted to avoid inference failures
135impl_partial_eq!(ByteStr, str);
136// PartialOrd with `&str` omitted to avoid inference failures
137impl_partial_eq!(ByteStr, &str);
138// PartialOrd with `[u8; N]` omitted to avoid inference failures
139impl_partial_eq_n!(ByteStr, [u8; N]);
140// PartialOrd with `[u8; N]` omitted to avoid inference failures
141impl_partial_eq_n!(ByteStr, &[u8; N]);
142
143#[unstable(feature = "bstr", issue = "134915")]
144impl<I> ops::Index<I> for ByteStr
145where
146    I: SliceIndex<ByteStr>,
147{
148    type Output = I::Output;
149
150    #[inline]
151    fn index(&self, index: I) -> &I::Output {
152        index.index(self)
153    }
154}
155
156#[unstable(feature = "bstr", issue = "134915")]
157impl<I> ops::IndexMut<I> for ByteStr
158where
159    I: SliceIndex<ByteStr>,
160{
161    #[inline]
162    fn index_mut(&mut self, index: I) -> &mut I::Output {
163        index.index_mut(self)
164    }
165}
166
167#[unstable(feature = "bstr", issue = "134915")]
168unsafe impl SliceIndex<ByteStr> for ops::RangeFull {
169    type Output = ByteStr;
170    #[inline]
171    fn get(self, slice: &ByteStr) -> Option<&Self::Output> {
172        Some(slice)
173    }
174    #[inline]
175    fn get_mut(self, slice: &mut ByteStr) -> Option<&mut Self::Output> {
176        Some(slice)
177    }
178    #[inline]
179    unsafe fn get_unchecked(self, slice: *const ByteStr) -> *const Self::Output {
180        slice
181    }
182    #[inline]
183    unsafe fn get_unchecked_mut(self, slice: *mut ByteStr) -> *mut Self::Output {
184        slice
185    }
186    #[inline]
187    fn index(self, slice: &ByteStr) -> &Self::Output {
188        slice
189    }
190    #[inline]
191    fn index_mut(self, slice: &mut ByteStr) -> &mut Self::Output {
192        slice
193    }
194}
195
196#[unstable(feature = "bstr", issue = "134915")]
197unsafe impl SliceIndex<ByteStr> for usize {
198    type Output = u8;
199    #[inline]
200    fn get(self, slice: &ByteStr) -> Option<&Self::Output> {
201        self.get(slice.as_bytes())
202    }
203    #[inline]
204    fn get_mut(self, slice: &mut ByteStr) -> Option<&mut Self::Output> {
205        self.get_mut(slice.as_bytes_mut())
206    }
207    #[inline]
208    unsafe fn get_unchecked(self, slice: *const ByteStr) -> *const Self::Output {
209        // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
210        unsafe { self.get_unchecked(slice as *const [u8]) }
211    }
212    #[inline]
213    unsafe fn get_unchecked_mut(self, slice: *mut ByteStr) -> *mut Self::Output {
214        // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
215        unsafe { self.get_unchecked_mut(slice as *mut [u8]) }
216    }
217    #[inline]
218    fn index(self, slice: &ByteStr) -> &Self::Output {
219        self.index(slice.as_bytes())
220    }
221    #[inline]
222    fn index_mut(self, slice: &mut ByteStr) -> &mut Self::Output {
223        self.index_mut(slice.as_bytes_mut())
224    }
225}
226
227macro_rules! impl_slice_index {
228    ($index:ty) => {
229        #[unstable(feature = "bstr", issue = "134915")]
230        unsafe impl SliceIndex<ByteStr> for $index {
231            type Output = ByteStr;
232            #[inline]
233            fn get(self, slice: &ByteStr) -> Option<&Self::Output> {
234                self.get(slice.as_bytes()).map(ByteStr::from_bytes)
235            }
236            #[inline]
237            fn get_mut(self, slice: &mut ByteStr) -> Option<&mut Self::Output> {
238                self.get_mut(slice.as_bytes_mut()).map(ByteStr::from_bytes_mut)
239            }
240            #[inline]
241            unsafe fn get_unchecked(self, slice: *const ByteStr) -> *const Self::Output {
242                // SAFETY: the caller has to uphold the safety contract for `get_unchecked`.
243                unsafe { self.get_unchecked(slice as *const [u8]) as *const ByteStr }
244            }
245            #[inline]
246            unsafe fn get_unchecked_mut(self, slice: *mut ByteStr) -> *mut Self::Output {
247                // SAFETY: the caller has to uphold the safety contract for `get_unchecked_mut`.
248                unsafe { self.get_unchecked_mut(slice as *mut [u8]) as *mut ByteStr }
249            }
250            #[inline]
251            fn index(self, slice: &ByteStr) -> &Self::Output {
252                ByteStr::from_bytes(self.index(slice.as_bytes()))
253            }
254            #[inline]
255            fn index_mut(self, slice: &mut ByteStr) -> &mut Self::Output {
256                ByteStr::from_bytes_mut(self.index_mut(slice.as_bytes_mut()))
257            }
258        }
259    };
260}
261
262impl_slice_index!(ops::IndexRange);
263impl_slice_index!(ops::Range<usize>);
264impl_slice_index!(range::Range<usize>);
265impl_slice_index!(ops::RangeTo<usize>);
266impl_slice_index!(ops::RangeFrom<usize>);
267impl_slice_index!(range::RangeFrom<usize>);
268impl_slice_index!(ops::RangeInclusive<usize>);
269impl_slice_index!(range::RangeInclusive<usize>);
270impl_slice_index!(ops::RangeToInclusive<usize>);
271impl_slice_index!((ops::Bound<usize>, ops::Bound<usize>));
```