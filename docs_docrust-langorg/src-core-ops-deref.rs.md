---
title: deref.rs - source
url: https://doc.rust-lang.org/src/core/ops/deref.rs.html#378-380
source: crawler
fetched_at: 2026-05-06T21:24:09.400349602-03:00
rendered_js: false
word_count: 2084
summary: This document defines the Deref trait in Rust, which enables custom dereferencing behavior and powers implicit deref coercion for smart pointer types.
tags:
    - rust-language
    - trait-implementation
    - deref-coercion
    - smart-pointers
    - memory-safety
category: reference
---

## core/ops/ deref.rs

````rust
1use crate::marker::PointeeSized;
2
3/// Used for immutable dereferencing operations, like `*v`.
4///
5/// In addition to being used for explicit dereferencing operations with the
6/// (unary) `*` operator in immutable contexts, `Deref` is also used implicitly
7/// by the compiler in many circumstances. This mechanism is called
8/// ["`Deref` coercion"][coercion]. In mutable contexts, [`DerefMut`] is used and
9/// mutable deref coercion similarly occurs.
10///
11/// **Warning:** Deref coercion is a powerful language feature which has
12/// far-reaching implications for every type that implements `Deref`. The
13/// compiler will silently insert calls to `Deref::deref`. For this reason, one
14/// should be careful about implementing `Deref` and only do so when deref
15/// coercion is desirable. See [below][implementing] for advice on when this is
16/// typically desirable or undesirable.
17///
18/// Types that implement `Deref` or `DerefMut` are often called "smart
19/// pointers" and the mechanism of deref coercion has been specifically designed
20/// to facilitate the pointer-like behavior that name suggests. Often, the
21/// purpose of a "smart pointer" type is to change the ownership semantics
22/// of a contained value (for example, [`Rc`][rc] or [`Cow`][cow]) or the
23/// storage semantics of a contained value (for example, [`Box`][box]).
24///
25/// # Deref coercion
26///
27/// If `T` implements `Deref<Target = U>`, and `v` is a value of type `T`, then:
28///
29/// * In immutable contexts, `*v` (where `T` is neither a reference nor a raw
30///   pointer) is equivalent to `*Deref::deref(&v)`.
31/// * Values of type `&T` are coerced to values of type `&U`
32/// * `T` implicitly implements all the methods of the type `U` which take the
33///   `&self` receiver.
34///
35/// For more details, visit [the chapter in *The Rust Programming Language*][book]
36/// as well as the reference sections on [the dereference operator][ref-deref-op],
37/// [method resolution], and [type coercions].
38///
39/// # When to implement `Deref` or `DerefMut`
40///
41/// The same advice applies to both deref traits. In general, deref traits
42/// **should** be implemented if:
43///
44/// 1. a value of the type transparently behaves like a value of the target
45///    type;
46/// 1. the implementation of the deref function is cheap; and
47/// 1. users of the type will not be surprised by any deref coercion behavior.
48///
49/// In general, deref traits **should not** be implemented if:
50///
51/// 1. the deref implementations could fail unexpectedly; or
52/// 1. the type has methods that are likely to collide with methods on the
53///    target type; or
54/// 1. committing to deref coercion as part of the public API is not desirable.
55///
56/// Note that there's a large difference between implementing deref traits
57/// generically over many target types, and doing so only for specific target
58/// types.
59///
60/// Generic implementations, such as for [`Box<T>`][box] (which is generic over
61/// every type and dereferences to `T`) should be careful to provide few or no
62/// methods, since the target type is unknown and therefore every method could
63/// collide with one on the target type, causing confusion for users.
64/// `impl<T> Box<T>` has no methods (though several associated functions),
65/// partly for this reason.
66///
67/// Specific implementations, such as for [`String`][string] (whose `Deref`
68/// implementation has `Target = str`) can have many methods, since avoiding
69/// collision is much easier. `String` and `str` both have many methods, and
70/// `String` additionally behaves as if it has every method of `str` because of
71/// deref coercion. The implementing type may also be generic while the
72/// implementation is still specific in this sense; for example, [`Vec<T>`][vec]
73/// dereferences to `[T]`, so methods of `T` are not applicable.
74///
75/// Consider also that deref coercion means that deref traits are a much larger
76/// part of a type's public API than any other trait as it is implicitly called
77/// by the compiler. Therefore, it is advisable to consider whether this is
78/// something you are comfortable supporting as a public API.
79///
80/// The [`AsRef`] and [`Borrow`][core::borrow::Borrow] traits have very similar
81/// signatures to `Deref`. It may be desirable to implement either or both of
82/// these, whether in addition to or rather than deref traits. See their
83/// documentation for details.
84///
85/// # Fallibility
86///
87/// **This trait's method should never unexpectedly fail**. Deref coercion means
88/// the compiler will often insert calls to `Deref::deref` implicitly. Failure
89/// during dereferencing can be extremely confusing when `Deref` is invoked
90/// implicitly. In the majority of uses it should be infallible, though it may
91/// be acceptable to panic if the type is misused through programmer error, for
92/// example.
93///
94/// However, infallibility is not enforced and therefore not guaranteed.
95/// As such, `unsafe` code should not rely on infallibility in general for
96/// soundness.
97///
98/// [book]: ../../book/ch15-02-deref.html
99/// [coercion]: #deref-coercion
100/// [implementing]: #when-to-implement-deref-or-derefmut
101/// [ref-deref-op]: ../../reference/expressions/operator-expr.html#the-dereference-operator
102/// [method resolution]: ../../reference/expressions/method-call-expr.html
103/// [type coercions]: ../../reference/type-coercions.html
104/// [box]: ../../alloc/boxed/struct.Box.html
105/// [string]: ../../alloc/string/struct.String.html
106/// [vec]: ../../alloc/vec/struct.Vec.html
107/// [rc]: ../../alloc/rc/struct.Rc.html
108/// [cow]: ../../alloc/borrow/enum.Cow.html
109///
110/// # Examples
111///
112/// A struct with a single field which is accessible by dereferencing the
113/// struct.
114///
115/// ```
116/// use std::ops::Deref;
117///
118/// struct DerefExample<T> {
119///     value: T
120/// }
121///
122/// impl<T> Deref for DerefExample<T> {
123///     type Target = T;
124///
125///     fn deref(&self) -> &Self::Target {
126///         &self.value
127///     }
128/// }
129///
130/// let x = DerefExample { value: 'a' };
131/// assert_eq!('a', *x);
132/// ```
133#[lang = "deref"]
134#[doc(alias = "*")]
135#[doc(alias = "&*")]
136#[stable(feature = "rust1", since = "1.0.0")]
137#[rustc_diagnostic_item = "Deref"]
138#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
139pub const trait Deref: PointeeSized {
140    /// The resulting type after dereferencing.
141    #[stable(feature = "rust1", since = "1.0.0")]
142    #[rustc_diagnostic_item = "deref_target"]
143    #[lang = "deref_target"]
144    type Target: ?Sized;
145
146    /// Dereferences the value.
147    #[must_use]
148    #[stable(feature = "rust1", since = "1.0.0")]
149    #[rustc_diagnostic_item = "deref_method"]
150    fn deref(&self) -> &Self::Target;
151}
152
153#[stable(feature = "rust1", since = "1.0.0")]
154#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
155impl<T: ?Sized> const Deref for &T {
156    type Target = T;
157
158    #[rustc_diagnostic_item = "noop_method_deref"]
159    fn deref(&self) -> &T {
160        self
161    }
162}
163
164#[stable(feature = "rust1", since = "1.0.0")]
165impl<T: ?Sized> !DerefMut for &T {}
166
167#[stable(feature = "rust1", since = "1.0.0")]
168#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
169impl<T: ?Sized> const Deref for &mut T {
170    type Target = T;
171
172    fn deref(&self) -> &T {
173        self
174    }
175}
176
177/// Used for mutable dereferencing operations, like in `*v = 1;`.
178///
179/// In addition to being used for explicit dereferencing operations with the
180/// (unary) `*` operator in mutable contexts, `DerefMut` is also used implicitly
181/// by the compiler in many circumstances. This mechanism is called
182/// ["mutable deref coercion"][coercion]. In immutable contexts, [`Deref`] is used.
183///
184/// **Warning:** Deref coercion is a powerful language feature which has
185/// far-reaching implications for every type that implements `DerefMut`. The
186/// compiler will silently insert calls to `DerefMut::deref_mut`. For this
187/// reason, one should be careful about implementing `DerefMut` and only do so
188/// when mutable deref coercion is desirable. See [the `Deref` docs][implementing]
189/// for advice on when this is typically desirable or undesirable.
190///
191/// Types that implement `DerefMut` or `Deref` are often called "smart
192/// pointers" and the mechanism of deref coercion has been specifically designed
193/// to facilitate the pointer-like behavior that name suggests. Often, the
194/// purpose of a "smart pointer" type is to change the ownership semantics
195/// of a contained value (for example, [`Rc`][rc] or [`Cow`][cow]) or the
196/// storage semantics of a contained value (for example, [`Box`][box]).
197///
198/// # Mutable deref coercion
199///
200/// If `T` implements `DerefMut<Target = U>`, and `v` is a value of type `T`,
201/// then:
202///
203/// * In mutable contexts, `*v` (where `T` is neither a reference nor a raw pointer)
204///   is equivalent to `*DerefMut::deref_mut(&mut v)`.
205/// * Values of type `&mut T` are coerced to values of type `&mut U`
206/// * `T` implicitly implements all the (mutable) methods of the type `U`.
207///
208/// For more details, visit [the chapter in *The Rust Programming Language*][book]
209/// as well as the reference sections on [the dereference operator][ref-deref-op],
210/// [method resolution] and [type coercions].
211///
212/// # Fallibility
213///
214/// **This trait's method should never unexpectedly fail**. Deref coercion means
215/// the compiler will often insert calls to `DerefMut::deref_mut` implicitly.
216/// Failure during dereferencing can be extremely confusing when `DerefMut` is
217/// invoked implicitly. In the majority of uses it should be infallible, though
218/// it may be acceptable to panic if the type is misused through programmer
219/// error, for example.
220///
221/// However, infallibility is not enforced and therefore not guaranteed.
222/// As such, `unsafe` code should not rely on infallibility in general for
223/// soundness.
224///
225/// [book]: ../../book/ch15-02-deref.html
226/// [coercion]: #mutable-deref-coercion
227/// [implementing]: Deref#when-to-implement-deref-or-derefmut
228/// [ref-deref-op]: ../../reference/expressions/operator-expr.html#the-dereference-operator
229/// [method resolution]: ../../reference/expressions/method-call-expr.html
230/// [type coercions]: ../../reference/type-coercions.html
231/// [box]: ../../alloc/boxed/struct.Box.html
232/// [string]: ../../alloc/string/struct.String.html
233/// [rc]: ../../alloc/rc/struct.Rc.html
234/// [cow]: ../../alloc/borrow/enum.Cow.html
235///
236/// # Examples
237///
238/// A struct with a single field which is modifiable by dereferencing the
239/// struct.
240///
241/// ```
242/// use std::ops::{Deref, DerefMut};
243///
244/// struct DerefMutExample<T> {
245///     value: T
246/// }
247///
248/// impl<T> Deref for DerefMutExample<T> {
249///     type Target = T;
250///
251///     fn deref(&self) -> &Self::Target {
252///         &self.value
253///     }
254/// }
255///
256/// impl<T> DerefMut for DerefMutExample<T> {
257///     fn deref_mut(&mut self) -> &mut Self::Target {
258///         &mut self.value
259///     }
260/// }
261///
262/// let mut x = DerefMutExample { value: 'a' };
263/// *x = 'b';
264/// assert_eq!('b', x.value);
265/// ```
266#[lang = "deref_mut"]
267#[doc(alias = "*")]
268#[stable(feature = "rust1", since = "1.0.0")]
269#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
270pub const trait DerefMut: [const] Deref + PointeeSized {
271    /// Mutably dereferences the value.
272    #[stable(feature = "rust1", since = "1.0.0")]
273    #[rustc_diagnostic_item = "deref_mut_method"]
274    fn deref_mut(&mut self) -> &mut Self::Target;
275}
276
277#[stable(feature = "rust1", since = "1.0.0")]
278#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
279impl<T: ?Sized> const DerefMut for &mut T {
280    fn deref_mut(&mut self) -> &mut T {
281        self
282    }
283}
284
285/// Perma-unstable marker trait. Indicates that the type has a well-behaved [`Deref`]
286/// (and, if applicable, [`DerefMut`]) implementation. This is relied on for soundness
287/// of deref patterns.
288///
289/// FIXME(deref_patterns): The precise semantics are undecided; the rough idea is that
290/// successive calls to `deref`/`deref_mut` without intermediate mutation should be
291/// idempotent, in the sense that they return the same value as far as pattern-matching
292/// is concerned. Calls to `deref`/`deref_mut` must leave the pointer itself likewise
293/// unchanged.
294#[unstable(feature = "deref_pure_trait", issue = "87121")]
295#[lang = "deref_pure"]
296pub unsafe trait DerefPure: PointeeSized {}
297
298#[unstable(feature = "deref_pure_trait", issue = "87121")]
299unsafe impl<T: ?Sized> DerefPure for &T {}
300
301#[unstable(feature = "deref_pure_trait", issue = "87121")]
302unsafe impl<T: ?Sized> DerefPure for &mut T {}
303
304/// Indicates that a struct can be used as a method receiver.
305/// That is, a type can use this type as a type of `self`, like this:
306/// ```compile_fail
307/// # // This is currently compile_fail because the compiler-side parts
308/// # // of arbitrary_self_types are not implemented
309/// use std::ops::Receiver;
310///
311/// struct SmartPointer<T>(T);
312///
313/// impl<T> Receiver for SmartPointer<T> {
314///    type Target = T;
315/// }
316///
317/// struct MyContainedType;
318///
319/// impl MyContainedType {
320///   fn method(self: SmartPointer<Self>) {
321///     // ...
322///   }
323/// }
324///
325/// fn main() {
326///   let ptr = SmartPointer(MyContainedType);
327///   ptr.method();
328/// }
329/// ```
330/// This trait is blanket implemented for any type which implements
331/// [`Deref`], which includes stdlib pointer types like `Box<T>`,`Rc<T>`, `&T`,
332/// and `Pin<P>`. For that reason, it's relatively rare to need to
333/// implement this directly. You'll typically do this only if you need
334/// to implement a smart pointer type which can't implement [`Deref`]; perhaps
335/// because you're interfacing with another programming language and can't
336/// guarantee that references comply with Rust's aliasing rules.
337///
338/// When looking for method candidates, Rust will explore a chain of possible
339/// `Receiver`s, so for example each of the following methods work:
340/// ```
341/// use std::boxed::Box;
342/// use std::rc::Rc;
343///
344/// // Both `Box` and `Rc` (indirectly) implement Receiver
345///
346/// struct MyContainedType;
347///
348/// fn main() {
349///   let t = Rc::new(Box::new(MyContainedType));
350///   t.method_a();
351///   t.method_b();
352///   t.method_c();
353/// }
354///
355/// impl MyContainedType {
356///   fn method_a(&self) {
357///
358///   }
359///   fn method_b(self: &Box<Self>) {
360///
361///   }
362///   fn method_c(self: &Rc<Box<Self>>) {
363///
364///   }
365/// }
366/// ```
367#[lang = "receiver"]
368#[unstable(feature = "arbitrary_self_types", issue = "44874")]
369pub trait Receiver: PointeeSized {
370    /// The target type on which the method may be called.
371    #[rustc_diagnostic_item = "receiver_target"]
372    #[lang = "receiver_target"]
373    #[unstable(feature = "arbitrary_self_types", issue = "44874")]
374    type Target: ?Sized;
375}
376
377#[unstable(feature = "arbitrary_self_types", issue = "44874")]
378impl<P: ?Sized, T: ?Sized> Receiver for P
379where
380    P: Deref<Target = T>,
381{
382    type Target = T;
383}
384
385/// Indicates that a struct can be used as a method receiver, without the
386/// `arbitrary_self_types` feature. This is implemented by stdlib pointer types like `Box<T>`,
387/// `Rc<T>`, `&T`, and `Pin<P>`.
388///
389/// This trait will shortly be removed and replaced with a more generic
390/// facility based around the current "arbitrary self types" unstable feature.
391/// That new facility will use the replacement trait above called `Receiver`
392/// which is why this is now named `LegacyReceiver`.
393#[lang = "legacy_receiver"]
394#[unstable(feature = "legacy_receiver_trait", issue = "none")]
395#[doc(hidden)]
396pub trait LegacyReceiver: PointeeSized {
397    // Empty.
398}
399
400#[unstable(feature = "legacy_receiver_trait", issue = "none")]
401impl<T: PointeeSized> LegacyReceiver for &T {}
402
403#[unstable(feature = "legacy_receiver_trait", issue = "none")]
404impl<T: PointeeSized> LegacyReceiver for &mut T {}
````