---
title: SliceIndex in std::slice - Rust
url: https://doc.rust-lang.org/stable/std/slice/trait.SliceIndex.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:33:01.01526928-03:00
rendered_js: false
word_count: 1129
summary: The SliceIndex trait provides a standardized interface for indexing operations on slices and strings, enabling both safe and unchecked access to elements or sub-slices.
tags:
    - rust
    - trait
    - indexing
    - slice
    - memory-safety
    - unsafe-code
category: api
---

## Trait SliceIndex

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#163)

```rust
pub unsafe trait SliceIndex<T>: Sealed
where
    T: ?Sized,{
    type Output: ?Sized;

    // Required methods
    fn get(self, slice: &T) -> Option<&Self::Output>;
    fn get_mut(self, slice: &mut T) -> Option<&mut Self::Output>;
    unsafe fn get_unchecked(self, slice: *const T) -> *const Self::Output;
    unsafe fn get_unchecked_mut(self, slice: *mut T) -> *mut Self::Output;
    fn index(self, slice: &T) -> &Self::Output;
    fn index_mut(self, slice: &mut T) -> &mut Self::Output;
}
```

Expand description

A helper trait used for indexing operations.

Implementations of this trait have to promise that if the argument to `get_unchecked(_mut)` is a safe reference, then so is the result.

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#166)

The output type returned by methods.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#171)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#176)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, if in bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#186)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a pointer to the output at this location, without performing any bounds checking.

Calling this method with an out-of-bounds index or a dangling `slice` pointer is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointer is not used.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#196)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable pointer to the output at this location, without performing any bounds checking.

Calling this method with an out-of-bounds index or a dangling `slice` pointer is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) even if the resulting pointer is not used.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#202)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a shared reference to the output at this location, panicking if out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#208)

🔬This is a nightly-only experimental API. (`slice_index_methods`)

Returns a mutable reference to the output at this location, panicking if out of bounds.

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#380)[§](#impl-SliceIndex%3Cstr%3E-for-%28Bound%3Cusize%3E,+Bound%3Cusize%3E%29)

Implements substring slicing for arbitrary bounds.

Returns a slice of the given string bounded by the byte indices provided by each bound.

This operation is *O*(1).

#### [§](#panics)Panics

Panics if `begin` or `end` (if it exists and once adjusted for inclusion/exclusion) does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `begin > end`, or if `end > len`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#381)[§](#associatedtype.Output-1)

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#158)[§](#impl-SliceIndex%3Cstr%3E-for-Range%3Cusize%3E)

Implements substring slicing with syntax `&self[begin .. end]` or `&mut self[begin .. end]`.

Returns a slice of the given string from the byte range [`begin`, `end`).

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-1)Panics

Panics if `begin` or `end` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `begin > end`, or if `end > len`.

#### [§](#examples)Examples

```rust
let s = "Löwe 老虎 Léopard";
assert_eq!(&s[0 .. 1], "L");

assert_eq!(&s[1 .. 9], "öwe 老");

// these will panic:
// byte 2 lies within `ö`:
// &s[2 ..3];

// byte 8 lies within `老`
// &s[1 .. 8];

// byte 100 is outside the string
// &s[3 .. 100];
```

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#159)[§](#associatedtype.Output-2)

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#504)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFrom%3Cusize%3E)

Implements substring slicing with syntax `&self[begin ..]` or `&mut self[begin ..]`.

Returns a slice of the given string from the byte range \[`begin`, `len`). Equivalent to `&self[begin .. len]` or `&mut self[begin .. len]`.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-2)Panics

Panics if `begin` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), or if `begin > len`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#505)[§](#associatedtype.Output-3)

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#93)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFull)

Implements substring slicing with syntax `&self[..]` or `&mut self[..]`.

Returns a slice of the whole string, i.e., returns `&self` or `&mut self`. Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`. Unlike other indexing operations, this can never panic.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

Equivalent to `&self[0 .. len]` or `&mut self[0 .. len]`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#94)[§](#associatedtype.Output-4)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#632)[§](#impl-SliceIndex%3Cstr%3E-for-RangeInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[begin ..= end]` or `&mut self[begin ..= end]`.

Returns a slice of the given string from the byte range \[`begin`, `end`]. Equivalent to `&self [begin .. end + 1]` or `&mut self[begin .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics-3)Panics

Panics if `begin` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset or equal to `len`), if `begin > end`, or if `end >= len`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#633)[§](#associatedtype.Output-5)

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#435)[§](#impl-SliceIndex%3Cstr%3E-for-RangeTo%3Cusize%3E)

Implements substring slicing with syntax `&self[.. end]` or `&mut self[.. end]`.

Returns a slice of the given string from the byte range \[0, `end`). Equivalent to `&self[0 .. end]` or `&mut self[0 .. end]`.

This operation is *O*(1).

Prior to 1.20.0, these indexing operations were still supported by direct implementation of `Index` and `IndexMut`.

#### [§](#panics-4)Panics

Panics if `end` does not point to the starting byte offset of a character (as defined by `is_char_boundary`), or if `end > len`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#436)[§](#associatedtype.Output-6)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#736)[§](#impl-SliceIndex%3Cstr%3E-for-RangeToInclusive%3Cusize%3E)

Implements substring slicing with syntax `&self[..= end]` or `&mut self[..= end]`.

Returns a slice of the given string from the byte range \[0, `end`]. Equivalent to `&self [0 .. end + 1]`, except if `end` has the maximum value for `usize`.

This operation is *O*(1).

#### [§](#panics-5)Panics

Panics if `end` does not point to the ending byte offset of a character (`end + 1` is either a starting byte offset as defined by `is_char_boundary`, or equal to `len`), or if `end >= len`.

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#737)[§](#associatedtype.Output-7)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#263)[§](#impl-SliceIndex%3Cstr%3E-for-Range%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#264)[§](#associatedtype.Output-8)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#560)[§](#impl-SliceIndex%3Cstr%3E-for-RangeFrom%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#561)[§](#associatedtype.Output-9)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#690)[§](#impl-SliceIndex%3Cstr%3E-for-RangeInclusive%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/str/traits.rs.html#691)[§](#associatedtype.Output-10)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#271)[§](#impl-SliceIndex%3CByteStr%3E-for-%28Bound%3Cusize%3E,+Bound%3Cusize%3E%29)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#271)[§](#associatedtype.Output-11)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#197)[§](#impl-SliceIndex%3CByteStr%3E-for-usize)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#198)[§](#associatedtype.Output-12)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#263)[§](#impl-SliceIndex%3CByteStr%3E-for-Range%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#263)[§](#associatedtype.Output-13)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#266)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeFrom%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#266)[§](#associatedtype.Output-14)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#168)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#169)[§](#associatedtype.Output-15)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#268)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeInclusive%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#268)[§](#associatedtype.Output-16)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#265)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeTo%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#265)[§](#associatedtype.Output-17)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#270)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeToInclusive%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#270)[§](#associatedtype.Output-18)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#264)[§](#impl-SliceIndex%3CByteStr%3E-for-Range%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#264)[§](#associatedtype.Output-19)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#267)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeFrom%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#267)[§](#associatedtype.Output-20)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#269)[§](#impl-SliceIndex%3CByteStr%3E-for-RangeInclusive%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/bstr/traits.rs.html#269)[§](#associatedtype.Output-21)

1.53.0 · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#1041)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-%28Bound%3Cusize%3E,+Bound%3Cusize%3E%29)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#1042)[§](#associatedtype.Output-22)

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#214)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-usize)

The methods `index` and `index_mut` panic if the index is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#215)[§](#associatedtype.Output-23)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#53)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3Cusize%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#54)[§](#associatedtype.Output-24)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#127)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRange%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#128)[§](#associatedtype.Output-25)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#287)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFrom%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#288)[§](#associatedtype.Output-26)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#411)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFull%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#412)[§](#associatedtype.Output-27)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#213)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeInclusive%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#214)[§](#associatedtype.Output-28)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#318)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeTo%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#319)[§](#associatedtype.Output-29)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#380)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeToInclusive%3Cusize%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#381)[§](#associatedtype.Output-30)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#84)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRange%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#85)[§](#associatedtype.Output-31)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#256)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeFrom%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#257)[§](#associatedtype.Output-32)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#170)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeInclusive%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#171)[§](#associatedtype.Output-33)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#349)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Clamp%3CRangeToInclusive%3Cusize%3E%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#350)[§](#associatedtype.Output-34)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#442)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Last)

[Source](https://doc.rust-lang.org/stable/src/core/index.rs.html#443)[§](#associatedtype.Output-35)

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#362)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Range%3Cusize%3E)

The methods `index` and `index_mut` panic if:

- the start of the range is greater than the end of the range or
- the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#363)[§](#associatedtype.Output-36)

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#541)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFrom%3Cusize%3E)

The methods `index` and `index_mut` panic if the start of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#542)[§](#associatedtype.Output-37)

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#631)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFull)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#632)[§](#associatedtype.Output-38)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#670)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if:

- the start of the range is greater than the end of the range or
- the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#671)[§](#associatedtype.Output-39)

1.15.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#502)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeTo%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#503)[§](#associatedtype.Output-40)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#767)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#768)[§](#associatedtype.Output-41)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#463)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-Range%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#464)[§](#associatedtype.Output-42)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#593)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeFrom%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#594)[§](#associatedtype.Output-43)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#728)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeInclusive%3Cusize%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#729)[§](#associatedtype.Output-44)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#806)[§](#impl-SliceIndex%3C%5BT%5D%3E-for-RangeToInclusive%3Cusize%3E-1)

The methods `index` and `index_mut` panic if the end of the range is out of bounds.

[Source](https://doc.rust-lang.org/stable/src/core/slice/index.rs.html#807)[§](#associatedtype.Output-45)