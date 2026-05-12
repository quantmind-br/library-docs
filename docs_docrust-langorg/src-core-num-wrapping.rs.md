---
title: wrapping.rs - source
url: https://doc.rust-lang.org/src/core/num/wrapping.rs.html#566
source: crawler
fetched_at: 2026-05-06T21:29:51.363756087-03:00
rendered_js: false
word_count: 4625
summary: This document defines the Wrapping<T> type in Rust, which provides an interface for performing arithmetic operations that explicitly use wrapping semantics instead of checking for overflow.
tags:
    - rust
    - wrapping-arithmetic
    - overflow
    - modular-arithmetic
    - primitive-types
    - operator-overloading
category: concept
---

## core/num/ wrapping.rs

````rust
1//! Definitions of `Wrapping<T>`.
2
3use crate::fmt;
4use crate::ops::{
5    Add, AddAssign, BitAnd, BitAndAssign, BitOr, BitOrAssign, BitXor, BitXorAssign, Div, DivAssign,
6    Mul, MulAssign, Neg, Not, Rem, RemAssign, Shl, ShlAssign, Shr, ShrAssign, Sub, SubAssign,
7};
8
9/// Provides intentionally-wrapped arithmetic on `T`.
10///
11/// Operations like `+` on `u32` values are intended to never overflow,
12/// and in some debug configurations overflow is detected and results
13/// in a panic. While most arithmetic falls into this category, some
14/// code explicitly expects and relies upon modular arithmetic (e.g.,
15/// hashing).
16///
17/// Wrapping arithmetic can be achieved either through methods like
18/// `wrapping_add`, or through the `Wrapping<T>` type, which says that
19/// all standard arithmetic operations on the underlying value are
20/// intended to have wrapping semantics.
21///
22/// The underlying value can be retrieved through the `.0` index of the
23/// `Wrapping` tuple.
24///
25/// # Examples
26///
27/// ```
28/// use std::num::Wrapping;
29///
30/// let zero = Wrapping(0u32);
31/// let one = Wrapping(1u32);
32///
33/// assert_eq!(u32::MAX, (zero - one).0);
34/// ```
35///
36/// # Layout
37///
38/// `Wrapping<T>` is guaranteed to have the same layout and ABI as `T`.
39#[stable(feature = "rust1", since = "1.0.0")]
40#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Copy, Default, Hash)]
41#[repr(transparent)]
42#[rustc_diagnostic_item = "Wrapping"]
43pub struct Wrapping<T>(#[stable(feature = "rust1", since = "1.0.0")] pub T);
44
45#[stable(feature = "rust1", since = "1.0.0")]
46impl<T: fmt::Debug> fmt::Debug for Wrapping<T> {
47    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
48        self.0.fmt(f)
49    }
50}
51
52#[stable(feature = "wrapping_display", since = "1.10.0")]
53impl<T: fmt::Display> fmt::Display for Wrapping<T> {
54    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
55        self.0.fmt(f)
56    }
57}
58
59#[stable(feature = "wrapping_fmt", since = "1.11.0")]
60impl<T: fmt::Binary> fmt::Binary for Wrapping<T> {
61    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
62        self.0.fmt(f)
63    }
64}
65
66#[stable(feature = "wrapping_fmt", since = "1.11.0")]
67impl<T: fmt::Octal> fmt::Octal for Wrapping<T> {
68    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
69        self.0.fmt(f)
70    }
71}
72
73#[stable(feature = "wrapping_fmt", since = "1.11.0")]
74impl<T: fmt::LowerHex> fmt::LowerHex for Wrapping<T> {
75    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
76        self.0.fmt(f)
77    }
78}
79
80#[stable(feature = "wrapping_fmt", since = "1.11.0")]
81impl<T: fmt::UpperHex> fmt::UpperHex for Wrapping<T> {
82    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
83        self.0.fmt(f)
84    }
85}
86
87#[allow(unused_macros)]
88macro_rules! sh_impl_signed {
89    ($t:ident, $f:ident) => {
90        #[stable(feature = "rust1", since = "1.0.0")]
91        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
92        impl const Shl<$f> for Wrapping<$t> {
93            type Output = Wrapping<$t>;
94
95            #[inline]
96            fn shl(self, other: $f) -> Wrapping<$t> {
97                if other < 0 {
98                    Wrapping(self.0.wrapping_shr(-other as u32))
99                } else {
100                    Wrapping(self.0.wrapping_shl(other as u32))
101                }
102            }
103        }
104        forward_ref_binop! { impl Shl, shl for Wrapping<$t>, $f,
105        #[stable(feature = "wrapping_ref_ops", since = "1.39.0")]
106        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
107
108        #[stable(feature = "op_assign_traits", since = "1.8.0")]
109        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
110        impl const ShlAssign<$f> for Wrapping<$t> {
111            #[inline]
112            fn shl_assign(&mut self, other: $f) {
113                *self = *self << other;
114            }
115        }
116        forward_ref_op_assign! { impl ShlAssign, shl_assign for Wrapping<$t>, $f,
117        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
118        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
119
120        #[stable(feature = "rust1", since = "1.0.0")]
121        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
122        impl const Shr<$f> for Wrapping<$t> {
123            type Output = Wrapping<$t>;
124
125            #[inline]
126            fn shr(self, other: $f) -> Wrapping<$t> {
127                if other < 0 {
128                    Wrapping(self.0.wrapping_shl(-other as u32))
129                } else {
130                    Wrapping(self.0.wrapping_shr(other as u32))
131                }
132            }
133        }
134        forward_ref_binop! { impl Shr, shr for Wrapping<$t>, $f,
135        #[stable(feature = "wrapping_ref_ops", since = "1.39.0")]
136        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
137
138        #[stable(feature = "op_assign_traits", since = "1.8.0")]
139        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
140        impl const ShrAssign<$f> for Wrapping<$t> {
141            #[inline]
142            fn shr_assign(&mut self, other: $f) {
143                *self = *self >> other;
144            }
145        }
146        forward_ref_op_assign! { impl ShrAssign, shr_assign for Wrapping<$t>, $f,
147        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
148        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
149    };
150}
151
152macro_rules! sh_impl_unsigned {
153    ($t:ident, $f:ident) => {
154        #[stable(feature = "rust1", since = "1.0.0")]
155        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
156        impl const Shl<$f> for Wrapping<$t> {
157            type Output = Wrapping<$t>;
158
159            #[inline]
160            fn shl(self, other: $f) -> Wrapping<$t> {
161                Wrapping(self.0.wrapping_shl(other as u32))
162            }
163        }
164        forward_ref_binop! { impl Shl, shl for Wrapping<$t>, $f,
165        #[stable(feature = "wrapping_ref_ops", since = "1.39.0")]
166        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
167
168        #[stable(feature = "op_assign_traits", since = "1.8.0")]
169        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
170        impl const ShlAssign<$f> for Wrapping<$t> {
171            #[inline]
172            fn shl_assign(&mut self, other: $f) {
173                *self = *self << other;
174            }
175        }
176        forward_ref_op_assign! { impl ShlAssign, shl_assign for Wrapping<$t>, $f,
177        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
178        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
179
180        #[stable(feature = "rust1", since = "1.0.0")]
181        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
182        impl const Shr<$f> for Wrapping<$t> {
183            type Output = Wrapping<$t>;
184
185            #[inline]
186            fn shr(self, other: $f) -> Wrapping<$t> {
187                Wrapping(self.0.wrapping_shr(other as u32))
188            }
189        }
190        forward_ref_binop! { impl Shr, shr for Wrapping<$t>, $f,
191        #[stable(feature = "wrapping_ref_ops", since = "1.39.0")]
192        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
193
194        #[stable(feature = "op_assign_traits", since = "1.8.0")]
195        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
196        impl const ShrAssign<$f> for Wrapping<$t> {
197            #[inline]
198            fn shr_assign(&mut self, other: $f) {
199                *self = *self >> other;
200            }
201        }
202        forward_ref_op_assign! { impl ShrAssign, shr_assign for Wrapping<$t>, $f,
203        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
204        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
205    };
206}
207
208// FIXME (#23545): uncomment the remaining impls
209macro_rules! sh_impl_all {
210    ($($t:ident)*) => ($(
211        //sh_impl_unsigned! { $t, u8 }
212        //sh_impl_unsigned! { $t, u16 }
213        //sh_impl_unsigned! { $t, u32 }
214        //sh_impl_unsigned! { $t, u64 }
215        //sh_impl_unsigned! { $t, u128 }
216        sh_impl_unsigned! { $t, usize }
217
218        //sh_impl_signed! { $t, i8 }
219        //sh_impl_signed! { $t, i16 }
220        //sh_impl_signed! { $t, i32 }
221        //sh_impl_signed! { $t, i64 }
222        //sh_impl_signed! { $t, i128 }
223        //sh_impl_signed! { $t, isize }
224    )*)
225}
226
227sh_impl_all! { u8 u16 u32 u64 u128 usize i8 i16 i32 i64 i128 isize }
228
229// FIXME(30524): impl Op<T> for Wrapping<T>, impl OpAssign<T> for Wrapping<T>
230macro_rules! wrapping_impl {
231    ($($t:ty)*) => ($(
232        #[stable(feature = "rust1", since = "1.0.0")]
233        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
234        impl const Add for Wrapping<$t> {
235            type Output = Wrapping<$t>;
236
237            #[inline]
238            fn add(self, other: Wrapping<$t>) -> Wrapping<$t> {
239                Wrapping(self.0.wrapping_add(other.0))
240            }
241        }
242        forward_ref_binop! { impl Add, add for Wrapping<$t>, Wrapping<$t>,
243        #[stable(feature = "wrapping_ref", since = "1.14.0")]
244        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
245
246        #[stable(feature = "op_assign_traits", since = "1.8.0")]
247        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
248        impl const AddAssign for Wrapping<$t> {
249            #[inline]
250            fn add_assign(&mut self, other: Wrapping<$t>) {
251                *self = *self + other;
252            }
253        }
254        forward_ref_op_assign! { impl AddAssign, add_assign for Wrapping<$t>, Wrapping<$t>,
255        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
256        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
257
258        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
259        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
260        impl const AddAssign<$t> for Wrapping<$t> {
261            #[inline]
262            fn add_assign(&mut self, other: $t) {
263                *self = *self + Wrapping(other);
264            }
265        }
266        forward_ref_op_assign! { impl AddAssign, add_assign for Wrapping<$t>, $t,
267        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
268        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
269
270        #[stable(feature = "rust1", since = "1.0.0")]
271        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
272        impl const Sub for Wrapping<$t> {
273            type Output = Wrapping<$t>;
274
275            #[inline]
276            fn sub(self, other: Wrapping<$t>) -> Wrapping<$t> {
277                Wrapping(self.0.wrapping_sub(other.0))
278            }
279        }
280        forward_ref_binop! { impl Sub, sub for Wrapping<$t>, Wrapping<$t>,
281        #[stable(feature = "wrapping_ref", since = "1.14.0")]
282        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
283
284        #[stable(feature = "op_assign_traits", since = "1.8.0")]
285        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
286        impl const SubAssign for Wrapping<$t> {
287            #[inline]
288            fn sub_assign(&mut self, other: Wrapping<$t>) {
289                *self = *self - other;
290            }
291        }
292        forward_ref_op_assign! { impl SubAssign, sub_assign for Wrapping<$t>, Wrapping<$t>,
293        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
294        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
295
296        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
297        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
298        impl const SubAssign<$t> for Wrapping<$t> {
299            #[inline]
300            fn sub_assign(&mut self, other: $t) {
301                *self = *self - Wrapping(other);
302            }
303        }
304        forward_ref_op_assign! { impl SubAssign, sub_assign for Wrapping<$t>, $t,
305        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
306        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
307
308        #[stable(feature = "rust1", since = "1.0.0")]
309        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
310        impl const Mul for Wrapping<$t> {
311            type Output = Wrapping<$t>;
312
313            #[inline]
314            fn mul(self, other: Wrapping<$t>) -> Wrapping<$t> {
315                Wrapping(self.0.wrapping_mul(other.0))
316            }
317        }
318        forward_ref_binop! { impl Mul, mul for Wrapping<$t>, Wrapping<$t>,
319        #[stable(feature = "wrapping_ref", since = "1.14.0")]
320        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
321
322        #[stable(feature = "op_assign_traits", since = "1.8.0")]
323        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
324        impl const MulAssign for Wrapping<$t> {
325            #[inline]
326            fn mul_assign(&mut self, other: Wrapping<$t>) {
327                *self = *self * other;
328            }
329        }
330        forward_ref_op_assign! { impl MulAssign, mul_assign for Wrapping<$t>, Wrapping<$t>,
331        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
332        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
333
334        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
335        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
336        impl const MulAssign<$t> for Wrapping<$t> {
337            #[inline]
338            fn mul_assign(&mut self, other: $t) {
339                *self = *self * Wrapping(other);
340            }
341        }
342        forward_ref_op_assign! { impl MulAssign, mul_assign for Wrapping<$t>, $t,
343        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
344        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
345
346        #[stable(feature = "wrapping_div", since = "1.3.0")]
347        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
348        impl const Div for Wrapping<$t> {
349            type Output = Wrapping<$t>;
350
351            #[inline]
352            fn div(self, other: Wrapping<$t>) -> Wrapping<$t> {
353                Wrapping(self.0.wrapping_div(other.0))
354            }
355        }
356        forward_ref_binop! { impl Div, div for Wrapping<$t>, Wrapping<$t>,
357        #[stable(feature = "wrapping_ref", since = "1.14.0")]
358        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
359
360        #[stable(feature = "op_assign_traits", since = "1.8.0")]
361        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
362        impl const DivAssign for Wrapping<$t> {
363            #[inline]
364            fn div_assign(&mut self, other: Wrapping<$t>) {
365                *self = *self / other;
366            }
367        }
368        forward_ref_op_assign! { impl DivAssign, div_assign for Wrapping<$t>, Wrapping<$t>,
369        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
370        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
371
372        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
373        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
374        impl const DivAssign<$t> for Wrapping<$t> {
375            #[inline]
376            fn div_assign(&mut self, other: $t) {
377                *self = *self / Wrapping(other);
378            }
379        }
380        forward_ref_op_assign! { impl DivAssign, div_assign for Wrapping<$t>, $t,
381        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
382        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
383
384        #[stable(feature = "wrapping_impls", since = "1.7.0")]
385        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
386        impl const Rem for Wrapping<$t> {
387            type Output = Wrapping<$t>;
388
389            #[inline]
390            fn rem(self, other: Wrapping<$t>) -> Wrapping<$t> {
391                Wrapping(self.0.wrapping_rem(other.0))
392            }
393        }
394        forward_ref_binop! { impl Rem, rem for Wrapping<$t>, Wrapping<$t>,
395        #[stable(feature = "wrapping_ref", since = "1.14.0")]
396        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
397
398        #[stable(feature = "op_assign_traits", since = "1.8.0")]
399        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
400        impl const RemAssign for Wrapping<$t> {
401            #[inline]
402            fn rem_assign(&mut self, other: Wrapping<$t>) {
403                *self = *self % other;
404            }
405        }
406        forward_ref_op_assign! { impl RemAssign, rem_assign for Wrapping<$t>, Wrapping<$t>,
407        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
408        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
409
410        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
411        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
412        impl const RemAssign<$t> for Wrapping<$t> {
413            #[inline]
414            fn rem_assign(&mut self, other: $t) {
415                *self = *self % Wrapping(other);
416            }
417        }
418        forward_ref_op_assign! { impl RemAssign, rem_assign for Wrapping<$t>, $t,
419        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
420        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
421
422        #[stable(feature = "rust1", since = "1.0.0")]
423        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
424        impl const Not for Wrapping<$t> {
425            type Output = Wrapping<$t>;
426
427            #[inline]
428            fn not(self) -> Wrapping<$t> {
429                Wrapping(!self.0)
430            }
431        }
432        forward_ref_unop! { impl Not, not for Wrapping<$t>,
433        #[stable(feature = "wrapping_ref", since = "1.14.0")]
434        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
435
436        #[stable(feature = "rust1", since = "1.0.0")]
437        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
438        impl const BitXor for Wrapping<$t> {
439            type Output = Wrapping<$t>;
440
441            #[inline]
442            fn bitxor(self, other: Wrapping<$t>) -> Wrapping<$t> {
443                Wrapping(self.0 ^ other.0)
444            }
445        }
446        forward_ref_binop! { impl BitXor, bitxor for Wrapping<$t>, Wrapping<$t>,
447        #[stable(feature = "wrapping_ref", since = "1.14.0")]
448        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
449
450        #[stable(feature = "op_assign_traits", since = "1.8.0")]
451        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
452        impl const BitXorAssign for Wrapping<$t> {
453            #[inline]
454            fn bitxor_assign(&mut self, other: Wrapping<$t>) {
455                *self = *self ^ other;
456            }
457        }
458        forward_ref_op_assign! { impl BitXorAssign, bitxor_assign for Wrapping<$t>, Wrapping<$t>,
459        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
460        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
461
462        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
463        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
464        impl const BitXorAssign<$t> for Wrapping<$t> {
465            #[inline]
466            fn bitxor_assign(&mut self, other: $t) {
467                *self = *self ^ Wrapping(other);
468            }
469        }
470        forward_ref_op_assign! { impl BitXorAssign, bitxor_assign for Wrapping<$t>, $t,
471        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
472        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
473
474        #[stable(feature = "rust1", since = "1.0.0")]
475        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
476        impl const BitOr for Wrapping<$t> {
477            type Output = Wrapping<$t>;
478
479            #[inline]
480            fn bitor(self, other: Wrapping<$t>) -> Wrapping<$t> {
481                Wrapping(self.0 | other.0)
482            }
483        }
484        forward_ref_binop! { impl BitOr, bitor for Wrapping<$t>, Wrapping<$t>,
485        #[stable(feature = "wrapping_ref", since = "1.14.0")]
486        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
487
488        #[stable(feature = "op_assign_traits", since = "1.8.0")]
489        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
490        impl const BitOrAssign for Wrapping<$t> {
491            #[inline]
492            fn bitor_assign(&mut self, other: Wrapping<$t>) {
493                *self = *self | other;
494            }
495        }
496        forward_ref_op_assign! { impl BitOrAssign, bitor_assign for Wrapping<$t>, Wrapping<$t>,
497        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
498        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
499
500        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
501        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
502        impl const BitOrAssign<$t> for Wrapping<$t> {
503            #[inline]
504            fn bitor_assign(&mut self, other: $t) {
505                *self = *self | Wrapping(other);
506            }
507        }
508        forward_ref_op_assign! { impl BitOrAssign, bitor_assign for Wrapping<$t>, $t,
509        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
510        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
511
512        #[stable(feature = "rust1", since = "1.0.0")]
513        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
514        impl const BitAnd for Wrapping<$t> {
515            type Output = Wrapping<$t>;
516
517            #[inline]
518            fn bitand(self, other: Wrapping<$t>) -> Wrapping<$t> {
519                Wrapping(self.0 & other.0)
520            }
521        }
522        forward_ref_binop! { impl BitAnd, bitand for Wrapping<$t>, Wrapping<$t>,
523        #[stable(feature = "wrapping_ref", since = "1.14.0")]
524        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
525
526        #[stable(feature = "op_assign_traits", since = "1.8.0")]
527        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
528        impl const BitAndAssign for Wrapping<$t> {
529            #[inline]
530            fn bitand_assign(&mut self, other: Wrapping<$t>) {
531                *self = *self & other;
532            }
533        }
534        forward_ref_op_assign! { impl BitAndAssign, bitand_assign for Wrapping<$t>, Wrapping<$t>,
535        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
536        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
537
538        #[stable(feature = "wrapping_int_assign_impl", since = "1.60.0")]
539        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
540        impl const BitAndAssign<$t> for Wrapping<$t> {
541            #[inline]
542            fn bitand_assign(&mut self, other: $t) {
543                *self = *self & Wrapping(other);
544            }
545        }
546        forward_ref_op_assign! { impl BitAndAssign, bitand_assign for Wrapping<$t>, $t,
547        #[stable(feature = "op_assign_builtins_by_ref", since = "1.22.0")]
548        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
549
550        #[stable(feature = "wrapping_neg", since = "1.10.0")]
551        #[rustc_const_unstable(feature = "const_ops", issue = "143802")]
552        impl const Neg for Wrapping<$t> {
553            type Output = Self;
554            #[inline]
555            fn neg(self) -> Self {
556                Wrapping(0) - self
557            }
558        }
559        forward_ref_unop! { impl Neg, neg for Wrapping<$t>,
560        #[stable(feature = "wrapping_ref", since = "1.14.0")]
561        #[rustc_const_unstable(feature = "const_ops", issue = "143802")] }
562
563    )*)
564}
565
566wrapping_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
567
568macro_rules! wrapping_int_impl {
569    ($($t:ty)*) => ($(
570        impl Wrapping<$t> {
571            /// Returns the smallest value that can be represented by this integer type.
572            ///
573            /// # Examples
574            ///
575            /// Basic usage:
576            ///
577            /// ```
578            /// #![feature(wrapping_int_impl)]
579            /// use std::num::Wrapping;
580            ///
581            #[doc = concat!("assert_eq!(<Wrapping<", stringify!($t), ">>::MIN, Wrapping(", stringify!($t), "::MIN));")]
582            /// ```
583            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
584            pub const MIN: Self = Self(<$t>::MIN);
585
586            /// Returns the largest value that can be represented by this integer type.
587            ///
588            /// # Examples
589            ///
590            /// Basic usage:
591            ///
592            /// ```
593            /// #![feature(wrapping_int_impl)]
594            /// use std::num::Wrapping;
595            ///
596            #[doc = concat!("assert_eq!(<Wrapping<", stringify!($t), ">>::MAX, Wrapping(", stringify!($t), "::MAX));")]
597            /// ```
598            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
599            pub const MAX: Self = Self(<$t>::MAX);
600
601            /// Returns the size of this integer type in bits.
602            ///
603            /// # Examples
604            ///
605            /// Basic usage:
606            ///
607            /// ```
608            /// #![feature(wrapping_int_impl)]
609            /// use std::num::Wrapping;
610            ///
611            #[doc = concat!("assert_eq!(<Wrapping<", stringify!($t), ">>::BITS, ", stringify!($t), "::BITS);")]
612            /// ```
613            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
614            pub const BITS: u32 = <$t>::BITS;
615
616            /// Returns the number of ones in the binary representation of `self`.
617            ///
618            /// # Examples
619            ///
620            /// Basic usage:
621            ///
622            /// ```
623            /// #![feature(wrapping_int_impl)]
624            /// use std::num::Wrapping;
625            ///
626            #[doc = concat!("let n = Wrapping(0b01001100", stringify!($t), ");")]
627            ///
628            /// assert_eq!(n.count_ones(), 3);
629            /// ```
630            #[inline]
631            #[doc(alias = "popcount")]
632            #[doc(alias = "popcnt")]
633            #[must_use = "this returns the result of the operation, \
634                          without modifying the original"]
635            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
636            pub const fn count_ones(self) -> u32 {
637                self.0.count_ones()
638            }
639
640            /// Returns the number of zeros in the binary representation of `self`.
641            ///
642            /// # Examples
643            ///
644            /// Basic usage:
645            ///
646            /// ```
647            /// #![feature(wrapping_int_impl)]
648            /// use std::num::Wrapping;
649            ///
650            #[doc = concat!("assert_eq!(Wrapping(!0", stringify!($t), ").count_zeros(), 0);")]
651            /// ```
652            #[inline]
653            #[must_use = "this returns the result of the operation, \
654                          without modifying the original"]
655            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
656            pub const fn count_zeros(self) -> u32 {
657                self.0.count_zeros()
658            }
659
660            /// Returns the number of trailing zeros in the binary representation of `self`.
661            ///
662            /// # Examples
663            ///
664            /// Basic usage:
665            ///
666            /// ```
667            /// #![feature(wrapping_int_impl)]
668            /// use std::num::Wrapping;
669            ///
670            #[doc = concat!("let n = Wrapping(0b0101000", stringify!($t), ");")]
671            ///
672            /// assert_eq!(n.trailing_zeros(), 3);
673            /// ```
674            #[inline]
675            #[must_use = "this returns the result of the operation, \
676                          without modifying the original"]
677            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
678            pub const fn trailing_zeros(self) -> u32 {
679                self.0.trailing_zeros()
680            }
681
682            /// Shifts the bits to the left by a specified amount, `n`,
683            /// wrapping the truncated bits to the end of the resulting
684            /// integer.
685            ///
686            /// Please note this isn't the same operation as the `<<` shifting
687            /// operator!
688            ///
689            /// # Examples
690            ///
691            /// Basic usage:
692            ///
693            /// ```
694            /// #![feature(wrapping_int_impl)]
695            /// use std::num::Wrapping;
696            ///
697            /// let n: Wrapping<i64> = Wrapping(0x0123456789ABCDEF);
698            /// let m: Wrapping<i64> = Wrapping(-0x76543210FEDCBA99);
699            ///
700            /// assert_eq!(n.rotate_left(32), m);
701            /// ```
702            #[inline]
703            #[must_use = "this returns the result of the operation, \
704                          without modifying the original"]
705            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
706            pub const fn rotate_left(self, n: u32) -> Self {
707                Wrapping(self.0.rotate_left(n))
708            }
709
710            /// Shifts the bits to the right by a specified amount, `n`,
711            /// wrapping the truncated bits to the beginning of the resulting
712            /// integer.
713            ///
714            /// Please note this isn't the same operation as the `>>` shifting
715            /// operator!
716            ///
717            /// # Examples
718            ///
719            /// Basic usage:
720            ///
721            /// ```
722            /// #![feature(wrapping_int_impl)]
723            /// use std::num::Wrapping;
724            ///
725            /// let n: Wrapping<i64> = Wrapping(0x0123456789ABCDEF);
726            /// let m: Wrapping<i64> = Wrapping(-0xFEDCBA987654322);
727            ///
728            /// assert_eq!(n.rotate_right(4), m);
729            /// ```
730            #[inline]
731            #[must_use = "this returns the result of the operation, \
732                          without modifying the original"]
733            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
734            pub const fn rotate_right(self, n: u32) -> Self {
735                Wrapping(self.0.rotate_right(n))
736            }
737
738            /// Reverses the byte order of the integer.
739            ///
740            /// # Examples
741            ///
742            /// Basic usage:
743            ///
744            /// ```
745            /// #![feature(wrapping_int_impl)]
746            /// use std::num::Wrapping;
747            ///
748            /// let n: Wrapping<i16> = Wrapping(0b0000000_01010101);
749            /// assert_eq!(n, Wrapping(85));
750            ///
751            /// let m = n.swap_bytes();
752            ///
753            /// assert_eq!(m, Wrapping(0b01010101_00000000));
754            /// assert_eq!(m, Wrapping(21760));
755            /// ```
756            #[inline]
757            #[must_use = "this returns the result of the operation, \
758                          without modifying the original"]
759            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
760            pub const fn swap_bytes(self) -> Self {
761                Wrapping(self.0.swap_bytes())
762            }
763
764            /// Reverses the bit pattern of the integer.
765            ///
766            /// # Examples
767            ///
768            /// Please note that this example is shared among integer types, which is why `i16`
769            /// is used.
770            ///
771            /// Basic usage:
772            ///
773            /// ```
774            /// use std::num::Wrapping;
775            ///
776            /// let n = Wrapping(0b0000000_01010101i16);
777            /// assert_eq!(n, Wrapping(85));
778            ///
779            /// let m = n.reverse_bits();
780            ///
781            /// assert_eq!(m.0 as u16, 0b10101010_00000000);
782            /// assert_eq!(m, Wrapping(-22016));
783            /// ```
784            #[stable(feature = "reverse_bits", since = "1.37.0")]
785            #[rustc_const_stable(feature = "const_reverse_bits", since = "1.37.0")]
786            #[must_use = "this returns the result of the operation, \
787                          without modifying the original"]
788            #[inline]
789            pub const fn reverse_bits(self) -> Self {
790                Wrapping(self.0.reverse_bits())
791            }
792
793            /// Converts an integer from big endian to the target's endianness.
794            ///
795            /// On big endian this is a no-op. On little endian the bytes are
796            /// swapped.
797            ///
798            /// # Examples
799            ///
800            /// Basic usage:
801            ///
802            /// ```
803            /// #![feature(wrapping_int_impl)]
804            /// use std::num::Wrapping;
805            ///
806            #[doc = concat!("let n = Wrapping(0x1A", stringify!($t), ");")]
807            ///
808            /// if cfg!(target_endian = "big") {
809            #[doc = concat!("    assert_eq!(<Wrapping<", stringify!($t), ">>::from_be(n), n)")]
810            /// } else {
811            #[doc = concat!("    assert_eq!(<Wrapping<", stringify!($t), ">>::from_be(n), n.swap_bytes())")]
812            /// }
813            /// ```
814            #[inline]
815            #[must_use]
816            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
817            pub const fn from_be(x: Self) -> Self {
818                Wrapping(<$t>::from_be(x.0))
819            }
820
821            /// Converts an integer from little endian to the target's endianness.
822            ///
823            /// On little endian this is a no-op. On big endian the bytes are
824            /// swapped.
825            ///
826            /// # Examples
827            ///
828            /// Basic usage:
829            ///
830            /// ```
831            /// #![feature(wrapping_int_impl)]
832            /// use std::num::Wrapping;
833            ///
834            #[doc = concat!("let n = Wrapping(0x1A", stringify!($t), ");")]
835            ///
836            /// if cfg!(target_endian = "little") {
837            #[doc = concat!("    assert_eq!(<Wrapping<", stringify!($t), ">>::from_le(n), n)")]
838            /// } else {
839            #[doc = concat!("    assert_eq!(<Wrapping<", stringify!($t), ">>::from_le(n), n.swap_bytes())")]
840            /// }
841            /// ```
842            #[inline]
843            #[must_use]
844            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
845            pub const fn from_le(x: Self) -> Self {
846                Wrapping(<$t>::from_le(x.0))
847            }
848
849            /// Converts `self` to big endian from the target's endianness.
850            ///
851            /// On big endian this is a no-op. On little endian the bytes are
852            /// swapped.
853            ///
854            /// # Examples
855            ///
856            /// Basic usage:
857            ///
858            /// ```
859            /// #![feature(wrapping_int_impl)]
860            /// use std::num::Wrapping;
861            ///
862            #[doc = concat!("let n = Wrapping(0x1A", stringify!($t), ");")]
863            ///
864            /// if cfg!(target_endian = "big") {
865            ///     assert_eq!(n.to_be(), n)
866            /// } else {
867            ///     assert_eq!(n.to_be(), n.swap_bytes())
868            /// }
869            /// ```
870            #[inline]
871            #[must_use = "this returns the result of the operation, \
872                          without modifying the original"]
873            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
874            pub const fn to_be(self) -> Self {
875                Wrapping(self.0.to_be())
876            }
877
878            /// Converts `self` to little endian from the target's endianness.
879            ///
880            /// On little endian this is a no-op. On big endian the bytes are
881            /// swapped.
882            ///
883            /// # Examples
884            ///
885            /// Basic usage:
886            ///
887            /// ```
888            /// #![feature(wrapping_int_impl)]
889            /// use std::num::Wrapping;
890            ///
891            #[doc = concat!("let n = Wrapping(0x1A", stringify!($t), ");")]
892            ///
893            /// if cfg!(target_endian = "little") {
894            ///     assert_eq!(n.to_le(), n)
895            /// } else {
896            ///     assert_eq!(n.to_le(), n.swap_bytes())
897            /// }
898            /// ```
899            #[inline]
900            #[must_use = "this returns the result of the operation, \
901                          without modifying the original"]
902            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
903            pub const fn to_le(self) -> Self {
904                Wrapping(self.0.to_le())
905            }
906
907            /// Raises self to the power of `exp`, using exponentiation by squaring.
908            ///
909            /// # Examples
910            ///
911            /// Basic usage:
912            ///
913            /// ```
914            /// #![feature(wrapping_int_impl)]
915            /// use std::num::Wrapping;
916            ///
917            #[doc = concat!("assert_eq!(Wrapping(3", stringify!($t), ").pow(4), Wrapping(81));")]
918            /// ```
919            ///
920            /// Results that are too large are wrapped:
921            ///
922            /// ```
923            /// #![feature(wrapping_int_impl)]
924            /// use std::num::Wrapping;
925            ///
926            /// assert_eq!(Wrapping(3i8).pow(5), Wrapping(-13));
927            /// assert_eq!(Wrapping(3i8).pow(6), Wrapping(-39));
928            /// ```
929            #[inline]
930            #[must_use = "this returns the result of the operation, \
931                          without modifying the original"]
932            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
933            pub fn pow(self, exp: u32) -> Self {
934                Wrapping(self.0.wrapping_pow(exp))
935            }
936        }
937    )*)
938}
939
940wrapping_int_impl! { usize u8 u16 u32 u64 u128 isize i8 i16 i32 i64 i128 }
941
942macro_rules! wrapping_int_impl_signed {
943    ($($t:ty)*) => ($(
944        impl Wrapping<$t> {
945            /// Returns the number of leading zeros in the binary representation of `self`.
946            ///
947            /// # Examples
948            ///
949            /// Basic usage:
950            ///
951            /// ```
952            /// #![feature(wrapping_int_impl)]
953            /// use std::num::Wrapping;
954            ///
955            #[doc = concat!("let n = Wrapping(", stringify!($t), "::MAX) >> 2;")]
956            ///
957            /// assert_eq!(n.leading_zeros(), 3);
958            /// ```
959            #[inline]
960            #[must_use = "this returns the result of the operation, \
961                          without modifying the original"]
962            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
963            pub const fn leading_zeros(self) -> u32 {
964                self.0.leading_zeros()
965            }
966
967            /// Computes the absolute value of `self`, wrapping around at
968            /// the boundary of the type.
969            ///
970            /// The only case where such wrapping can occur is when one takes the absolute value of the negative
971            /// minimal value for the type this is a positive value that is too large to represent in the type. In
972            /// such a case, this function returns `MIN` itself.
973            ///
974            /// # Examples
975            ///
976            /// Basic usage:
977            ///
978            /// ```
979            /// #![feature(wrapping_int_impl)]
980            /// use std::num::Wrapping;
981            ///
982            #[doc = concat!("assert_eq!(Wrapping(100", stringify!($t), ").abs(), Wrapping(100));")]
983            #[doc = concat!("assert_eq!(Wrapping(-100", stringify!($t), ").abs(), Wrapping(100));")]
984            #[doc = concat!("assert_eq!(Wrapping(", stringify!($t), "::MIN).abs(), Wrapping(", stringify!($t), "::MIN));")]
985            /// assert_eq!(Wrapping(-128i8).abs().0 as u8, 128u8);
986            /// ```
987            #[inline]
988            #[must_use = "this returns the result of the operation, \
989                          without modifying the original"]
990            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
991            pub fn abs(self) -> Wrapping<$t> {
992                Wrapping(self.0.wrapping_abs())
993            }
994
995            /// Returns a number representing sign of `self`.
996            ///
997            ///  - `0` if the number is zero
998            ///  - `1` if the number is positive
999            ///  - `-1` if the number is negative
1000            ///
1001            /// # Examples
1002            ///
1003            /// Basic usage:
1004            ///
1005            /// ```
1006            /// #![feature(wrapping_int_impl)]
1007            /// use std::num::Wrapping;
1008            ///
1009            #[doc = concat!("assert_eq!(Wrapping(10", stringify!($t), ").signum(), Wrapping(1));")]
1010            #[doc = concat!("assert_eq!(Wrapping(0", stringify!($t), ").signum(), Wrapping(0));")]
1011            #[doc = concat!("assert_eq!(Wrapping(-10", stringify!($t), ").signum(), Wrapping(-1));")]
1012            /// ```
1013            #[inline]
1014            #[must_use = "this returns the result of the operation, \
1015                          without modifying the original"]
1016            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
1017            pub fn signum(self) -> Wrapping<$t> {
1018                Wrapping(self.0.signum())
1019            }
1020
1021            /// Returns `true` if `self` is positive and `false` if the number is zero or
1022            /// negative.
1023            ///
1024            /// # Examples
1025            ///
1026            /// Basic usage:
1027            ///
1028            /// ```
1029            /// #![feature(wrapping_int_impl)]
1030            /// use std::num::Wrapping;
1031            ///
1032            #[doc = concat!("assert!(Wrapping(10", stringify!($t), ").is_positive());")]
1033            #[doc = concat!("assert!(!Wrapping(-10", stringify!($t), ").is_positive());")]
1034            /// ```
1035            #[must_use]
1036            #[inline]
1037            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
1038            pub const fn is_positive(self) -> bool {
1039                self.0.is_positive()
1040            }
1041
1042            /// Returns `true` if `self` is negative and `false` if the number is zero or
1043            /// positive.
1044            ///
1045            /// # Examples
1046            ///
1047            /// Basic usage:
1048            ///
1049            /// ```
1050            /// #![feature(wrapping_int_impl)]
1051            /// use std::num::Wrapping;
1052            ///
1053            #[doc = concat!("assert!(Wrapping(-10", stringify!($t), ").is_negative());")]
1054            #[doc = concat!("assert!(!Wrapping(10", stringify!($t), ").is_negative());")]
1055            /// ```
1056            #[must_use]
1057            #[inline]
1058            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
1059            pub const fn is_negative(self) -> bool {
1060                self.0.is_negative()
1061            }
1062        }
1063    )*)
1064}
1065
1066wrapping_int_impl_signed! { isize i8 i16 i32 i64 i128 }
1067
1068macro_rules! wrapping_int_impl_unsigned {
1069    ($($t:ty)*) => ($(
1070        impl Wrapping<$t> {
1071            /// Returns the number of leading zeros in the binary representation of `self`.
1072            ///
1073            /// # Examples
1074            ///
1075            /// Basic usage:
1076            ///
1077            /// ```
1078            /// #![feature(wrapping_int_impl)]
1079            /// use std::num::Wrapping;
1080            ///
1081            #[doc = concat!("let n = Wrapping(", stringify!($t), "::MAX) >> 2;")]
1082            ///
1083            /// assert_eq!(n.leading_zeros(), 2);
1084            /// ```
1085            #[inline]
1086            #[must_use = "this returns the result of the operation, \
1087                          without modifying the original"]
1088            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
1089            pub const fn leading_zeros(self) -> u32 {
1090                self.0.leading_zeros()
1091            }
1092
1093            /// Returns `true` if and only if `self == 2^k` for some `k`.
1094            ///
1095            /// # Examples
1096            ///
1097            /// Basic usage:
1098            ///
1099            /// ```
1100            /// #![feature(wrapping_int_impl)]
1101            /// use std::num::Wrapping;
1102            ///
1103            #[doc = concat!("assert!(Wrapping(16", stringify!($t), ").is_power_of_two());")]
1104            #[doc = concat!("assert!(!Wrapping(10", stringify!($t), ").is_power_of_two());")]
1105            /// ```
1106            #[must_use]
1107            #[inline]
1108            #[unstable(feature = "wrapping_int_impl", issue = "32463")]
1109            pub fn is_power_of_two(self) -> bool {
1110                self.0.is_power_of_two()
1111            }
1112
1113            /// Returns the smallest power of two greater than or equal to `self`.
1114            ///
1115            /// When return value overflows (i.e., `self > (1 << (N-1))` for type
1116            /// `uN`), overflows to `2^N = 0`.
1117            ///
1118            /// # Examples
1119            ///
1120            /// Basic usage:
1121            ///
1122            /// ```
1123            /// #![feature(wrapping_next_power_of_two)]
1124            /// use std::num::Wrapping;
1125            ///
1126            #[doc = concat!("assert_eq!(Wrapping(2", stringify!($t), ").next_power_of_two(), Wrapping(2));")]
1127            #[doc = concat!("assert_eq!(Wrapping(3", stringify!($t), ").next_power_of_two(), Wrapping(4));")]
1128            #[doc = concat!("assert_eq!(Wrapping(200_u8).next_power_of_two(), Wrapping(0));")]
1129            /// ```
1130            #[inline]
1131            #[must_use = "this returns the result of the operation, \
1132                          without modifying the original"]
1133            #[unstable(feature = "wrapping_next_power_of_two", issue = "32463",
1134                       reason = "needs decision on wrapping behavior")]
1135            pub fn next_power_of_two(self) -> Self {
1136                Wrapping(self.0.wrapping_next_power_of_two())
1137            }
1138        }
1139    )*)
1140}
1141
1142wrapping_int_impl_unsigned! { usize u8 u16 u32 u64 u128 }
````