---
title: borrow.rs - source
url: https://doc.rust-lang.org/src/core/borrow.rs.html#222
source: crawler
fetched_at: 2026-05-06T21:24:06.6621563-03:00
rendered_js: false
word_count: 1223
summary: This document explains the Borrow and BorrowMut traits in Rust, which allow types to be represented or accessed as an underlying type while maintaining consistent behavior for hash and equality operations.
tags:
    - rust
    - trait
    - borrowing
    - memory-management
    - ownership
    - generics
category: reference
---

## core/ borrow.rs

````rust
1//! Utilities for working with borrowed data.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5/// A trait for borrowing data.
6///
7/// In Rust, it is common to provide different representations of a type for
8/// different use cases. For instance, storage location and management for a
9/// value can be specifically chosen as appropriate for a particular use via
10/// pointer types such as [`Box<T>`] or [`Rc<T>`]. Beyond these generic
11/// wrappers that can be used with any type, some types provide optional
12/// facets providing potentially costly functionality. An example for such a
13/// type is [`String`] which adds the ability to extend a string to the basic
14/// [`str`]. This requires keeping additional information unnecessary for a
15/// simple, immutable string.
16///
17/// These types provide access to the underlying data through references
18/// to the type of that data. They are said to be ‘borrowed as’ that type.
19/// For instance, a [`Box<T>`] can be borrowed as `T` while a [`String`]
20/// can be borrowed as `str`.
21///
22/// Types express that they can be borrowed as some type `T` by implementing
23/// `Borrow<T>`, providing a reference to a `T` in the trait’s
24/// [`borrow`] method. A type is free to borrow as several different types.
25/// If it wishes to mutably borrow as the type, allowing the underlying data
26/// to be modified, it can additionally implement [`BorrowMut<T>`].
27///
28/// Further, when providing implementations for additional traits, it needs
29/// to be considered whether they should behave identically to those of the
30/// underlying type as a consequence of acting as a representation of that
31/// underlying type. Generic code typically uses `Borrow<T>` when it relies
32/// on the identical behavior of these additional trait implementations.
33/// These traits will likely appear as additional trait bounds.
34///
35/// In particular `Eq`, `Ord` and `Hash` must be equivalent for
36/// borrowed and owned values: `x.borrow() == y.borrow()` should give the
37/// same result as `x == y`.
38///
39/// If generic code merely needs to work for all types that can
40/// provide a reference to related type `T`, it is often better to use
41/// [`AsRef<T>`] as more types can safely implement it.
42///
43/// [`Box<T>`]: ../../std/boxed/struct.Box.html
44/// [`Mutex<T>`]: ../../std/sync/struct.Mutex.html
45/// [`Rc<T>`]: ../../std/rc/struct.Rc.html
46/// [`String`]: ../../std/string/struct.String.html
47/// [`borrow`]: Borrow::borrow
48///
49/// # Examples
50///
51/// As a data collection, [`HashMap<K, V>`] owns both keys and values. If
52/// the key’s actual data is wrapped in a managing type of some kind, it
53/// should, however, still be possible to search for a value using a
54/// reference to the key’s data. For instance, if the key is a string, then
55/// it is likely stored with the hash map as a [`String`], while it should
56/// be possible to search using a [`&str`][`str`]. Thus, `insert` needs to
57/// operate on a `String` while `get` needs to be able to use a `&str`.
58///
59/// Slightly simplified, the relevant parts of `HashMap<K, V>` look like
60/// this:
61///
62/// ```
63/// use std::borrow::Borrow;
64/// use std::hash::Hash;
65///
66/// pub struct HashMap<K, V> {
67///     # marker: ::std::marker::PhantomData<(K, V)>,
68///     // fields omitted
69/// }
70///
71/// impl<K, V> HashMap<K, V> {
72///     pub fn insert(&self, key: K, value: V) -> Option<V>
73///     where K: Hash + Eq
74///     {
75///         # unimplemented!()
76///         // ...
77///     }
78///
79///     pub fn get<Q>(&self, k: &Q) -> Option<&V>
80///     where
81///         K: Borrow<Q>,
82///         Q: Hash + Eq + ?Sized
83///     {
84///         # unimplemented!()
85///         // ...
86///     }
87/// }
88/// ```
89///
90/// The entire hash map is generic over a key type `K`. Because these keys
91/// are stored with the hash map, this type has to own the key’s data.
92/// When inserting a key-value pair, the map is given such a `K` and needs
93/// to find the correct hash bucket and check if the key is already present
94/// based on that `K`. It therefore requires `K: Hash + Eq`.
95///
96/// When searching for a value in the map, however, having to provide a
97/// reference to a `K` as the key to search for would require to always
98/// create such an owned value. For string keys, this would mean a `String`
99/// value needs to be created just for the search for cases where only a
100/// `str` is available.
101///
102/// Instead, the `get` method is generic over the type of the underlying key
103/// data, called `Q` in the method signature above. It states that `K`
104/// borrows as a `Q` by requiring that `K: Borrow<Q>`. By additionally
105/// requiring `Q: Hash + Eq`, it signals the requirement that `K` and `Q`
106/// have implementations of the `Hash` and `Eq` traits that produce identical
107/// results.
108///
109/// The implementation of `get` relies in particular on identical
110/// implementations of `Hash` by determining the key’s hash bucket by calling
111/// `Hash::hash` on the `Q` value even though it inserted the key based on
112/// the hash value calculated from the `K` value.
113///
114/// As a consequence, the hash map breaks if a `K` wrapping a `Q` value
115/// produces a different hash than `Q`. For instance, imagine you have a
116/// type that wraps a string but compares ASCII letters ignoring their case:
117///
118/// ```
119/// pub struct CaseInsensitiveString(String);
120///
121/// impl PartialEq for CaseInsensitiveString {
122///     fn eq(&self, other: &Self) -> bool {
123///         self.0.eq_ignore_ascii_case(&other.0)
124///     }
125/// }
126///
127/// impl Eq for CaseInsensitiveString { }
128/// ```
129///
130/// Because two equal values need to produce the same hash value, the
131/// implementation of `Hash` needs to ignore ASCII case, too:
132///
133/// ```
134/// # use std::hash::{Hash, Hasher};
135/// # pub struct CaseInsensitiveString(String);
136/// impl Hash for CaseInsensitiveString {
137///     fn hash<H: Hasher>(&self, state: &mut H) {
138///         for c in self.0.as_bytes() {
139///             c.to_ascii_lowercase().hash(state)
140///         }
141///     }
142/// }
143/// ```
144///
145/// Can `CaseInsensitiveString` implement `Borrow<str>`? It certainly can
146/// provide a reference to a string slice via its contained owned string.
147/// But because its `Hash` implementation differs, it behaves differently
148/// from `str` and therefore must not, in fact, implement `Borrow<str>`.
149/// If it wants to allow others access to the underlying `str`, it can do
150/// that via `AsRef<str>` which doesn’t carry any extra requirements.
151///
152/// [`Hash`]: crate::hash::Hash
153/// [`HashMap<K, V>`]: ../../std/collections/struct.HashMap.html
154/// [`String`]: ../../std/string/struct.String.html
155#[stable(feature = "rust1", since = "1.0.0")]
156#[rustc_diagnostic_item = "Borrow"]
157#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
158pub const trait Borrow<Borrowed: ?Sized> {
159    /// Immutably borrows from an owned value.
160    ///
161    /// # Examples
162    ///
163    /// ```
164    /// use std::borrow::Borrow;
165    ///
166    /// fn check<T: Borrow<str>>(s: T) {
167    ///     assert_eq!("Hello", s.borrow());
168    /// }
169    ///
170    /// let s = "Hello".to_string();
171    ///
172    /// check(s);
173    ///
174    /// let s = "Hello";
175    ///
176    /// check(s);
177    /// ```
178    #[stable(feature = "rust1", since = "1.0.0")]
179    fn borrow(&self) -> &Borrowed;
180}
181
182/// A trait for mutably borrowing data.
183///
184/// As a companion to [`Borrow<T>`] this trait allows a type to borrow as
185/// an underlying type by providing a mutable reference. See [`Borrow<T>`]
186/// for more information on borrowing as another type.
187#[stable(feature = "rust1", since = "1.0.0")]
188#[rustc_diagnostic_item = "BorrowMut"]
189#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
190pub const trait BorrowMut<Borrowed: ?Sized>: [const] Borrow<Borrowed> {
191    /// Mutably borrows from an owned value.
192    ///
193    /// # Examples
194    ///
195    /// ```
196    /// use std::borrow::BorrowMut;
197    ///
198    /// fn check<T: BorrowMut<[i32]>>(mut v: T) {
199    ///     assert_eq!(&mut [1, 2, 3], v.borrow_mut());
200    /// }
201    ///
202    /// let v = vec![1, 2, 3];
203    ///
204    /// check(v);
205    /// ```
206    #[stable(feature = "rust1", since = "1.0.0")]
207    fn borrow_mut(&mut self) -> &mut Borrowed;
208}
209
210#[stable(feature = "rust1", since = "1.0.0")]
211#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
212impl<T: ?Sized> const Borrow<T> for T {
213    #[rustc_diagnostic_item = "noop_method_borrow"]
214    fn borrow(&self) -> &T {
215        self
216    }
217}
218
219#[stable(feature = "rust1", since = "1.0.0")]
220#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
221impl<T: ?Sized> const BorrowMut<T> for T {
222    fn borrow_mut(&mut self) -> &mut T {
223        self
224    }
225}
226
227#[stable(feature = "rust1", since = "1.0.0")]
228#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
229impl<T: ?Sized> const Borrow<T> for &T {
230    fn borrow(&self) -> &T {
231        self
232    }
233}
234
235#[stable(feature = "rust1", since = "1.0.0")]
236#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
237impl<T: ?Sized> const Borrow<T> for &mut T {
238    fn borrow(&self) -> &T {
239        self
240    }
241}
242
243#[stable(feature = "rust1", since = "1.0.0")]
244#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
245impl<T: ?Sized> const BorrowMut<T> for &mut T {
246    fn borrow_mut(&mut self) -> &mut T {
247        self
248    }
249}
````