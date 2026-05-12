---
title: From in std::convert - Rust
url: https://doc.rust-lang.org/std/convert/trait.From.html#tymethod.from
source: crawler
fetched_at: 2026-05-06T21:22:02.757448537-03:00
rendered_js: false
word_count: 2335
summary: This document lists various trait implementations of the From trait within the Rust standard library, facilitating type conversions across strings, collections, and error types.
tags:
    - rust
    - trait-implementations
    - type-conversion
    - standard-library
    - from-trait
    - memory-management
category: reference
---

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#124)[§](#impl-From%3C%26str%3E-for-Box%3Cstr%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2896)[§](#impl-From%3C%26str%3E-for-Rc%3Cstr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3108)[§](#impl-From%3C%26str%3E-for-String)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3930)[§](#impl-From%3C%26str%3E-for-Arc%3Cstr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4423)[§](#impl-From%3C%26str%3E-for-Vec%3Cu8%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#765)[§](#impl-From%3C%26CStr%3E-for-Box%3CCStr%3E)

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#1083)[§](#impl-From%3C%26CStr%3E-for-CString)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#944)[§](#impl-From%3C%26CStr%3E-for-Rc%3CCStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#911)[§](#impl-From%3C%26CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

1.17.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1295-1301)[§](#impl-From%3C%26OsStr%3E-for-Box%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1404-1411)[§](#impl-From%3C%26OsStr%3E-for-Rc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1374-1381)[§](#impl-From%3C%26OsStr%3E-for-Arc%3COsStr%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1889-1896)[§](#impl-From%3C%26Path%3E-for-Box%3CPath%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2184-2191)[§](#impl-From%3C%26Path%3E-for-Rc%3CPath%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2154-2161)[§](#impl-From%3C%26Path%3E-for-Arc%3CPath%3E)

1.35.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3132)[§](#impl-From%3C%26String%3E-for-String)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#144)[§](#impl-From%3C%26mut+str%3E-for-Box%3Cstr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2915)[§](#impl-From%3C%26mut+str%3E-for-Rc%3Cstr%3E)

1.44.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3120)[§](#impl-From%3C%26mut+str%3E-for-String)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3949)[§](#impl-From%3C%26mut+str%3E-for-Arc%3Cstr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#774)[§](#impl-From%3C%26mut+CStr%3E-for-Box%3CCStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#955)[§](#impl-From%3C%26mut+CStr%3E-for-Rc%3CCStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#923)[§](#impl-From%3C%26mut+CStr%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1304-1310)[§](#impl-From%3C%26mut+OsStr%3E-for-Box%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1414-1420)[§](#impl-From%3C%26mut+OsStr%3E-for-Rc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1384-1390)[§](#impl-From%3C%26mut+OsStr%3E-for-Arc%3COsStr%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1899-1906)[§](#impl-From%3C%26mut+Path%3E-for-Box%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2194-2200)[§](#impl-From%3C%26mut+Path%3E-for-Rc%3CPath%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2164-2170)[§](#impl-From%3C%26mut+Path%3E-for-Arc%3CPath%3E)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-char)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u8)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u16)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u32)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u64)

[Source](https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171)[§](#impl-From%3CChar%3E-for-u128)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#166)[§](#impl-From%3CCow%3C'_,+str%3E%3E-for-Box%3Cstr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#783)[§](#impl-From%3CCow%3C'_,+CStr%3E%3E-for-Box%3CCStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1313-1323)[§](#impl-From%3CCow%3C'_,+OsStr%3E%3E-for-Box%3COsStr%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1909-1920)[§](#impl-From%3CCow%3C'_,+Path%3E%3E-for-Box%3CPath%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#152)[§](#impl-From%3CTryReserveErrorKind%3E-for-TryReserveError)

1.89.0 · [Source](https://doc.rust-lang.org/src/std/fs.rs.html#533-540)[§](#impl-From%3CTryLockError%3E-for-Error)

1.14.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#529-547)[§](#impl-From%3CErrorKind%3E-for-Error)

Intended for use for errors not exposed to the user, where allocating onto the heap (for normal construction via Error::new) is too costly.

1.36.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/array/mod.rs.html#197)[§](#impl-From%3CInfallible%3E-for-TryFromSliceError)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/num/error.rs.html#24)[§](#impl-From%3CInfallible%3E-for-TryFromIntError)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#218-228)[§](#impl-From%3Cbool%3E-for-f16)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#229)[§](#impl-From%3Cbool%3E-for-f32)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#230)[§](#impl-From%3Cbool%3E-for-f64)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#231-240)[§](#impl-From%3Cbool%3E-for-f128)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i8)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i16)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i32)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i64)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-i128)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#69)[§](#impl-From%3Cbool%3E-for-isize)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u8)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u16)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u32)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u64)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-u128)

1.28.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#68)[§](#impl-From%3Cbool%3E-for-usize)

1.24.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#2477)[§](#impl-From%3Cbool%3E-for-AtomicBool)

Available on **`target_has_atomic_load_store=8`** only.

1.13.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#40)[§](#impl-From%3Cchar%3E-for-u32)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#59)[§](#impl-From%3Cchar%3E-for-u64)

1.51.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#80)[§](#impl-From%3Cchar%3E-for-u128)

1.46.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3593)[§](#impl-From%3Cchar%3E-for-String)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#179)[§](#impl-From%3Cf16%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#180)[§](#impl-From%3Cf16%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#181)[§](#impl-From%3Cf32%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#182)[§](#impl-From%3Cf32%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#183)[§](#impl-From%3Cf64%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#151)[§](#impl-From%3Ci8%3E-for-f16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#152)[§](#impl-From%3Ci8%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#153)[§](#impl-From%3Ci8%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#154)[§](#impl-From%3Ci8%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#102)[§](#impl-From%3Ci8%3E-for-i16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#103)[§](#impl-From%3Ci8%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#104)[§](#impl-From%3Ci8%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#105)[§](#impl-From%3Ci8%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#106)[§](#impl-From%3Ci8%3E-for-isize)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3596-3613)[§](#impl-From%3Ci8%3E-for-AtomicI8)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#155)[§](#impl-From%3Ci16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#156)[§](#impl-From%3Ci16%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#157)[§](#impl-From%3Ci16%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#107)[§](#impl-From%3Ci16%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#108)[§](#impl-From%3Ci16%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#109)[§](#impl-From%3Ci16%3E-for-i128)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#131)[§](#impl-From%3Ci16%3E-for-isize)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3634-3651)[§](#impl-From%3Ci16%3E-for-AtomicI16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#158)[§](#impl-From%3Ci32%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#159)[§](#impl-From%3Ci32%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#110)[§](#impl-From%3Ci32%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#111)[§](#impl-From%3Ci32%3E-for-i128)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3672-3689)[§](#impl-From%3Ci32%3E-for-AtomicI32)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#112)[§](#impl-From%3Ci64%3E-for-i128)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3710-3727)[§](#impl-From%3Ci64%3E-for-AtomicI64)

1.23.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3851-3855)[§](#impl-From%3Cisize%3E-for-AtomicIsize)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#987)[§](#impl-From%3C!%3E-for-Infallible)

[Source](https://doc.rust-lang.org/src/core/num/error.rs.html#32)[§](#impl-From%3C!%3E-for-TryFromIntError)

1.13.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/char/convert.rs.html#217)[§](#impl-From%3Cu8%3E-for-char)

Maps a byte in `0x00..=0xFF` to a `char` whose code point has the same value from U+0000 to U+00FF (inclusive).

Unicode is designed such that this effectively decodes bytes with the character encoding that IANA calls ISO-8859-1. This encoding is compatible with ASCII.

Note that this is different from ISO/IEC 8859-1 a.k.a. ISO 8859-1 (with one less hyphen), which leaves some “blanks”, byte values that are not assigned to any character. ISO-8859-1 (the IANA one) assigns them to the C0 and C1 control codes.

Note that this is *also* different from Windows-1252 a.k.a. code page 1252, which is a superset ISO/IEC 8859-1 that assigns some (not all!) blanks to punctuation and various Latin characters.

To confuse things further, [on the Web](https://encoding.spec.whatwg.org/) `ascii`, `iso-8859-1`, and `windows-1252` are all aliases for a superset of Windows-1252 that fills the remaining blanks with corresponding C0 and C1 control codes.

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#164)[§](#impl-From%3Cu8%3E-for-f16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#165)[§](#impl-From%3Cu8%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#166)[§](#impl-From%3Cu8%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#167)[§](#impl-From%3Cu8%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#115)[§](#impl-From%3Cu8%3E-for-i16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#116)[§](#impl-From%3Cu8%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#117)[§](#impl-From%3Cu8%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#118)[§](#impl-From%3Cu8%3E-for-i128)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#130)[§](#impl-From%3Cu8%3E-for-isize)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#89)[§](#impl-From%3Cu8%3E-for-u16)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#90)[§](#impl-From%3Cu8%3E-for-u32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#91)[§](#impl-From%3Cu8%3E-for-u64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#92)[§](#impl-From%3Cu8%3E-for-u128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#93)[§](#impl-From%3Cu8%3E-for-usize)

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2197-2202)[§](#impl-From%3Cu8%3E-for-ExitCode)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3615-3632)[§](#impl-From%3Cu8%3E-for-AtomicU8)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#168)[§](#impl-From%3Cu16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#169)[§](#impl-From%3Cu16%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#170)[§](#impl-From%3Cu16%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#119)[§](#impl-From%3Cu16%3E-for-i32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#120)[§](#impl-From%3Cu16%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#121)[§](#impl-From%3Cu16%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#94)[§](#impl-From%3Cu16%3E-for-u32)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#95)[§](#impl-From%3Cu16%3E-for-u64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#96)[§](#impl-From%3Cu16%3E-for-u128)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#129)[§](#impl-From%3Cu16%3E-for-usize)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3653-3670)[§](#impl-From%3Cu16%3E-for-AtomicU16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#171)[§](#impl-From%3Cu32%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#172)[§](#impl-From%3Cu32%3E-for-f128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#122)[§](#impl-From%3Cu32%3E-for-i64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#123)[§](#impl-From%3Cu32%3E-for-i128)

1.5.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#97)[§](#impl-From%3Cu32%3E-for-u64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#98)[§](#impl-From%3Cu32%3E-for-u128)

1.1.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1235)[§](#impl-From%3Cu32%3E-for-Ipv4Addr)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3691-3708)[§](#impl-From%3Cu32%3E-for-AtomicU32)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#124)[§](#impl-From%3Cu64%3E-for-i128)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#99)[§](#impl-From%3Cu64%3E-for-u128)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3729-3746)[§](#impl-From%3Cu64%3E-for-AtomicU64)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2228)[§](#impl-From%3Cu128%3E-for-Ipv6Addr)

1.23.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#3851-3855)[§](#impl-From%3Cusize%3E-for-AtomicUsize)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#29)[§](#impl-From%3C__m128%3E-for-Simd%3Cf32,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#39)[§](#impl-From%3C__m128d%3E-for-Simd%3Cf64,+2%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#12)[§](#impl-From%3C__m128i%3E-for-Simd%3Ci8,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#19)[§](#impl-From%3C__m128i%3E-for-Simd%3Ci16,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#26)[§](#impl-From%3C__m128i%3E-for-Simd%3Ci32,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#36)[§](#impl-From%3C__m128i%3E-for-Simd%3Ci64,+2%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#9)[§](#impl-From%3C__m128i%3E-for-Simd%3Cu8,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#16)[§](#impl-From%3C__m128i%3E-for-Simd%3Cu16,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#23)[§](#impl-From%3C__m128i%3E-for-Simd%3Cu32,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#33)[§](#impl-From%3C__m128i%3E-for-Simd%3Cu64,+2%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#30)[§](#impl-From%3C__m256%3E-for-Simd%3Cf32,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#40)[§](#impl-From%3C__m256d%3E-for-Simd%3Cf64,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#13)[§](#impl-From%3C__m256i%3E-for-Simd%3Ci8,+32%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#20)[§](#impl-From%3C__m256i%3E-for-Simd%3Ci16,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#27)[§](#impl-From%3C__m256i%3E-for-Simd%3Ci32,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#37)[§](#impl-From%3C__m256i%3E-for-Simd%3Ci64,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#10)[§](#impl-From%3C__m256i%3E-for-Simd%3Cu8,+32%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#17)[§](#impl-From%3C__m256i%3E-for-Simd%3Cu16,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#24)[§](#impl-From%3C__m256i%3E-for-Simd%3Cu32,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#34)[§](#impl-From%3C__m256i%3E-for-Simd%3Cu64,+4%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#31)[§](#impl-From%3C__m512%3E-for-Simd%3Cf32,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#41)[§](#impl-From%3C__m512d%3E-for-Simd%3Cf64,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#14)[§](#impl-From%3C__m512i%3E-for-Simd%3Ci8,+64%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#21)[§](#impl-From%3C__m512i%3E-for-Simd%3Ci16,+32%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#28)[§](#impl-From%3C__m512i%3E-for-Simd%3Ci32,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#38)[§](#impl-From%3C__m512i%3E-for-Simd%3Ci64,+8%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#11)[§](#impl-From%3C__m512i%3E-for-Simd%3Cu8,+64%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#18)[§](#impl-From%3C__m512i%3E-for-Simd%3Cu16,+32%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#25)[§](#impl-From%3C__m512i%3E-for-Simd%3Cu32,+16%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#35)[§](#impl-From%3C__m512i%3E-for-Simd%3Cu64,+8%3E)

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#162)[§](#impl-From%3CLayoutError%3E-for-TryReserveErrorKind)

1.18.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3144)[§](#impl-From%3CBox%3Cstr%3E%3E-for-String)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#614)[§](#impl-From%3CBox%3CByteStr%3E%3E-for-Box%3C%5Bu8%5D%3E)

1.18.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#796)[§](#impl-From%3CBox%3CCStr%3E%3E-for-CString)

1.18.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1326-1333)[§](#impl-From%3CBox%3COsStr%3E%3E-for-OsString)

1.18.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1923-1931)[§](#impl-From%3CBox%3CPath%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#605)[§](#impl-From%3CBox%3C%5Bu8%5D%3E%3E-for-Box%3CByteStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#214)[§](#impl-From%3CByteString%3E-for-Vec%3Cu8%3E)

1.78.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#119-128)[§](#impl-From%3CTryReserveError%3E-for-Error)

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#862)[§](#impl-From%3CCString%3E-for-Box%3CCStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#933)[§](#impl-From%3CCString%3E-for-Rc%3CCStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#899)[§](#impl-From%3CCString%3E-for-Arc%3CCStr%3E)

Available on **`target_has_atomic=ptr`** only.

1.7.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#727)[§](#impl-From%3CCString%3E-for-Vec%3Cu8%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#111-116)[§](#impl-From%3CNulError%3E-for-Error)

1.20.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1336-1342)[§](#impl-From%3COsString%3E-for-Box%3COsStr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1965-1973)[§](#impl-From%3COsString%3E-for-PathBuf)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1393-1401)[§](#impl-From%3COsString%3E-for-Rc%3COsStr%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1363-1371)[§](#impl-From%3COsString%3E-for-Arc%3COsStr%3E)

[Source](https://doc.rust-lang.org/src/std/sys/fs/unix/dir.rs.html#103-107)[§](#impl-From%3CDir%3E-for-OwnedFd)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#327-333)[§](#impl-From%3CFile%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#531-537)[§](#impl-From%3CFile%3E-for-OwnedHandle)

Available on **Windows** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1683-1707)[§](#impl-From%3CFile%3E-for-Stdio)

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#544-548)[§](#impl-From%3CPipeReader%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#671-675)[§](#impl-From%3CPipeReader%3E-for-OwnedHandle)

Available on **Windows** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1777-1781)[§](#impl-From%3CPipeReader%3E-for-Stdio)

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#560-564)[§](#impl-From%3CPipeWriter%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#685-689)[§](#impl-From%3CPipeWriter%3E-for-OwnedHandle)

Available on **Windows** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1770-1774)[§](#impl-From%3CPipeWriter%3E-for-Stdio)

1.74.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1741-1767)[§](#impl-From%3CStderr%3E-for-Stdio)

1.74.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1710-1738)[§](#impl-From%3CStdout%3E-for-Stdio)

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1091)[§](#impl-From%3CIpv4Addr%3E-for-IpAddr)

1.1.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1225)[§](#impl-From%3CIpv4Addr%3E-for-u32)

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1114)[§](#impl-From%3CIpv6Addr%3E-for-IpAddr)

1.26.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2219)[§](#impl-From%3CIpv6Addr%3E-for-u128)

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#596)[§](#impl-From%3CSocketAddrV4%3E-for-SocketAddr)

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#606)[§](#impl-From%3CSocketAddrV6%3E-for-SocketAddr)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#387-393)[§](#impl-From%3CTcpListener%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#338-344)[§](#impl-From%3CTcpListener%3E-for-OwnedSocket)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#357-363)[§](#impl-From%3CTcpStream%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#313-319)[§](#impl-From%3CTcpStream%3E-for-OwnedSocket)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#417-423)[§](#impl-From%3CUdpSocket%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#363-369)[§](#impl-From%3CUdpSocket%3E-for-OwnedSocket)

Available on **Windows** only.

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#516)[§](#impl-From%3CNonZero%3Ci8%3E%3E-for-NonZero%3Ci16%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#517)[§](#impl-From%3CNonZero%3Ci8%3E%3E-for-NonZero%3Ci32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#518)[§](#impl-From%3CNonZero%3Ci8%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#519)[§](#impl-From%3CNonZero%3Ci8%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#520)[§](#impl-From%3CNonZero%3Ci8%3E%3E-for-NonZero%3Cisize%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#521)[§](#impl-From%3CNonZero%3Ci16%3E%3E-for-NonZero%3Ci32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#522)[§](#impl-From%3CNonZero%3Ci16%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#523)[§](#impl-From%3CNonZero%3Ci16%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#524)[§](#impl-From%3CNonZero%3Ci16%3E%3E-for-NonZero%3Cisize%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#525)[§](#impl-From%3CNonZero%3Ci32%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#526)[§](#impl-From%3CNonZero%3Ci32%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#527)[§](#impl-From%3CNonZero%3Ci64%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#530)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Ci16%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#531)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Ci32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#532)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#533)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#534)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cisize%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#502)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cu16%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#503)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cu32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#504)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cu64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#505)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cu128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#506)[§](#impl-From%3CNonZero%3Cu8%3E%3E-for-NonZero%3Cusize%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#535)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Ci32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#536)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#537)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#507)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cu32%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#508)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cu64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#509)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cu128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#510)[§](#impl-From%3CNonZero%3Cu16%3E%3E-for-NonZero%3Cusize%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#538)[§](#impl-From%3CNonZero%3Cu32%3E%3E-for-NonZero%3Ci64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#539)[§](#impl-From%3CNonZero%3Cu32%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#511)[§](#impl-From%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cu64%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#512)[§](#impl-From%3CNonZero%3Cu32%3E%3E-for-NonZero%3Cu128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#540)[§](#impl-From%3CNonZero%3Cu64%3E%3E-for-NonZero%3Ci128%3E)

1.41.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#513)[§](#impl-From%3CNonZero%3Cu64%3E%3E-for-NonZero%3Cu128%3E)

[Source](https://doc.rust-lang.org/src/std/sys/fs/unix/dir.rs.html#110-114)[§](#impl-From%3COwnedFd%3E-for-Dir)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#337-344)[§](#impl-From%3COwnedFd%3E-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#568-572)[§](#impl-From%3COwnedFd%3E-for-PipeReader)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#576-580)[§](#impl-From%3COwnedFd%3E-for-PipeWriter)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#397-404)[§](#impl-From%3COwnedFd%3E-for-TcpListener)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#367-374)[§](#impl-From%3COwnedFd%3E-for-TcpStream)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#427-434)[§](#impl-From%3COwnedFd%3E-for-UdpSocket)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/src/std/os/linux/process.rs.html#135-139)[§](#impl-From%3COwnedFd%3E-for-PidFd)

Available on **Linux** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/datagram.rs.html#1006-1011)[§](#impl-From%3COwnedFd%3E-for-UnixDatagram)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/listener.rs.html#343-348)[§](#impl-From%3COwnedFd%3E-for-UnixListener)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/stream.rs.html#737-742)[§](#impl-From%3COwnedFd%3E-for-UnixStream)

Available on **Unix** only.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#584-590)[§](#impl-From%3COwnedFd%3E-for-ChildStderr)

Available on **Unix** only.

Creates a `ChildStderr` from the provided `OwnedFd`.

The provided file descriptor must point to a pipe with the `CLOEXEC` flag set.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#524-530)[§](#impl-From%3COwnedFd%3E-for-ChildStdin)

Available on **Unix** only.

Creates a `ChildStdin` from the provided `OwnedFd`.

The provided file descriptor must point to a pipe with the `CLOEXEC` flag set.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#554-560)[§](#impl-From%3COwnedFd%3E-for-ChildStdout)

Available on **Unix** only.

Creates a `ChildStdout` from the provided `OwnedFd`.

The provided file descriptor must point to a pipe with the `CLOEXEC` flag set.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#443-452)[§](#impl-From%3COwnedFd%3E-for-Stdio)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/src/std/os/linux/process.rs.html#141-145)[§](#impl-From%3CPidFd%3E-for-OwnedFd)

Available on **Linux** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/datagram.rs.html#997-1003)[§](#impl-From%3CUnixDatagram%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/listener.rs.html#351-357)[§](#impl-From%3CUnixListener%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/net/stream.rs.html#728-734)[§](#impl-From%3CUnixStream%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#540-546)[§](#impl-From%3COwnedHandle%3E-for-File)

Available on **Windows** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#692-696)[§](#impl-From%3COwnedHandle%3E-for-PipeReader)

Available on **Windows** only.

1.87.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#699-703)[§](#impl-From%3COwnedHandle%3E-for-PipeWriter)

Available on **Windows** only.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#143-149)[§](#impl-From%3COwnedHandle%3E-for-ChildStderr)

Available on **Windows** only.

Creates a `ChildStderr` from the provided `OwnedHandle`.

The provided handle must be asynchronous, as reading and writing from and to it is implemented using asynchronous APIs.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#117-123)[§](#impl-From%3COwnedHandle%3E-for-ChildStdin)

Available on **Windows** only.

Creates a `ChildStdin` from the provided `OwnedHandle`.

The provided handle must be asynchronous, as reading and writing from and to it is implemented using asynchronous APIs.

1.74.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#130-136)[§](#impl-From%3COwnedHandle%3E-for-ChildStdout)

Available on **Windows** only.

Creates a `ChildStdout` from the provided `OwnedHandle`.

The provided handle must be asynchronous, as reading and writing from and to it is implemented using asynchronous APIs.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#26-34)[§](#impl-From%3COwnedHandle%3E-for-Stdio)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#347-352)[§](#impl-From%3COwnedSocket%3E-for-TcpListener)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#322-327)[§](#impl-From%3COwnedSocket%3E-for-TcpStream)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/socket.rs.html#372-377)[§](#impl-From%3COwnedSocket%3E-for-UdpSocket)

Available on **Windows** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1934-1943)[§](#impl-From%3CPathBuf%3E-for-Box%3CPath%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1976-1984)[§](#impl-From%3CPathBuf%3E-for-OsString)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2173-2181)[§](#impl-From%3CPathBuf%3E-for-Rc%3CPath%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2143-2151)[§](#impl-From%3CPathBuf%3E-for-Arc%3CPath%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#60-65)[§](#impl-From%3CChild%3E-for-OwnedHandle)

Available on **Windows** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#571-577)[§](#impl-From%3CChildStderr%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#639-645)[§](#impl-From%3CChildStderr%3E-for-OwnedHandle)

Available on **Windows** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1652-1680)[§](#impl-From%3CChildStderr%3E-for-Stdio)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#511-517)[§](#impl-From%3CChildStdin%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#605-611)[§](#impl-From%3CChildStdin%3E-for-OwnedHandle)

Available on **Windows** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1594-1620)[§](#impl-From%3CChildStdin%3E-for-Stdio)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/unix/process.rs.html#541-547)[§](#impl-From%3CChildStdout%3E-for-OwnedFd)

Available on **Unix** only.

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#622-628)[§](#impl-From%3CChildStdout%3E-for-OwnedHandle)

Available on **Windows** only.

1.20.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#1623-1649)[§](#impl-From%3CChildStdout%3E-for-Stdio)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2032-2036)[§](#impl-From%3CExitStatusError%3E-for-ExitStatus)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#286)[§](#impl-From%3CAlignment%3E-for-usize)

[Source](https://doc.rust-lang.org/src/core/ptr/alignment.rs.html#277)[§](#impl-From%3CAlignment%3E-for-NonZero%3Cusize%3E)

1.62.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3029)[§](#impl-From%3CRc%3Cstr%3E%3E-for-Rc%3C%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#634)[§](#impl-From%3CRc%3CByteStr%3E%3E-for-Rc%3C%5Bu8%5D%3E)

Available on **non-`no_rc`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#624)[§](#impl-From%3CRc%3C%5Bu8%5D%3E%3E-for-Rc%3CByteStr%3E)

Available on **non-`no_rc`** only.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#29)[§](#impl-From%3CSimd%3Cf32,+4%3E%3E-for-__m128)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#30)[§](#impl-From%3CSimd%3Cf32,+8%3E%3E-for-__m256)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#31)[§](#impl-From%3CSimd%3Cf32,+16%3E%3E-for-__m512)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#39)[§](#impl-From%3CSimd%3Cf64,+2%3E%3E-for-__m128d)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#40)[§](#impl-From%3CSimd%3Cf64,+4%3E%3E-for-__m256d)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#41)[§](#impl-From%3CSimd%3Cf64,+8%3E%3E-for-__m512d)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#12)[§](#impl-From%3CSimd%3Ci8,+16%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#13)[§](#impl-From%3CSimd%3Ci8,+32%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#14)[§](#impl-From%3CSimd%3Ci8,+64%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#19)[§](#impl-From%3CSimd%3Ci16,+8%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#20)[§](#impl-From%3CSimd%3Ci16,+16%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#21)[§](#impl-From%3CSimd%3Ci16,+32%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#26)[§](#impl-From%3CSimd%3Ci32,+4%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#27)[§](#impl-From%3CSimd%3Ci32,+8%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#28)[§](#impl-From%3CSimd%3Ci32,+16%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#36)[§](#impl-From%3CSimd%3Ci64,+2%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#37)[§](#impl-From%3CSimd%3Ci64,+4%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#38)[§](#impl-From%3CSimd%3Ci64,+8%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#9)[§](#impl-From%3CSimd%3Cu8,+16%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#10)[§](#impl-From%3CSimd%3Cu8,+32%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#11)[§](#impl-From%3CSimd%3Cu8,+64%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#16)[§](#impl-From%3CSimd%3Cu16,+8%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#17)[§](#impl-From%3CSimd%3Cu16,+16%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#18)[§](#impl-From%3CSimd%3Cu16,+32%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#23)[§](#impl-From%3CSimd%3Cu32,+4%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#24)[§](#impl-From%3CSimd%3Cu32,+8%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#25)[§](#impl-From%3CSimd%3Cu32,+16%3E%3E-for-__m512i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#33)[§](#impl-From%3CSimd%3Cu64,+2%3E%3E-for-__m128i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#34)[§](#impl-From%3CSimd%3Cu64,+4%3E%3E-for-__m256i)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vendor/x86.rs.html#35)[§](#impl-From%3CSimd%3Cu64,+8%3E%3E-for-__m512i)

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3164)[§](#impl-From%3CString%3E-for-Box%3Cstr%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#609-617)[§](#impl-From%3CString%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1987-1995)[§](#impl-From%3CString%3E-for-PathBuf)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2935)[§](#impl-From%3CString%3E-for-Rc%3Cstr%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3969)[§](#impl-From%3CString%3E-for-Arc%3Cstr%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3304)[§](#impl-From%3CString%3E-for-Vec%3Cu8%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/sync/mpsc.rs.html#1203-1214)[§](#impl-From%3CRecvError%3E-for-RecvTimeoutError)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/sync/mpsc.rs.html#1176-1187)[§](#impl-From%3CRecvError%3E-for-TryRecvError)

1.62.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4063)[§](#impl-From%3CArc%3Cstr%3E%3E-for-Arc%3C%5Bu8%5D%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#654)[§](#impl-From%3CArc%3CByteStr%3E%3E-for-Arc%3C%5Bu8%5D%3E)

Available on **non-`no_rc` and non-`no_sync` and `target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#644)[§](#impl-From%3CArc%3C%5Bu8%5D%3E%3E-for-Arc%3CByteStr%3E)

Available on **non-`no_rc` and non-`no_sync` and `target_has_atomic=ptr`** only.

1.43.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#806)[§](#impl-From%3CVec%3CNonZero%3Cu8%3E%3E%3E-for-CString)

1.94.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#403-447)[§](#impl-From%3CSimd%3Cf16,+8%3E%3E-for-__m128h)

1.94.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#403-447)[§](#impl-From%3CSimd%3Cf16,+16%3E%3E-for-__m256h)

1.94.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#403-447)[§](#impl-From%3CSimd%3Cf16,+32%3E%3E-for-__m512h)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Cf32,+4%3E%3E-for-__m128-1)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Cf32,+8%3E%3E-for-__m256-1)

1.72.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#281-356)[§](#impl-From%3CSimd%3Cf32,+16%3E%3E-for-__m512-1)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Cf64,+2%3E%3E-for-__m128d-1)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Cf64,+4%3E%3E-for-__m256d-1)

1.72.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#281-356)[§](#impl-From%3CSimd%3Cf64,+8%3E%3E-for-__m512d-1)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Ci64,+2%3E%3E-for-__m128i-1)

1.27.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#8-279)[§](#impl-From%3CSimd%3Ci64,+4%3E%3E-for-__m256i-1)

1.72.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#281-356)[§](#impl-From%3CSimd%3Ci64,+8%3E%3E-for-__m512i-1)

1.89.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#358-401)[§](#impl-From%3CSimd%3Cu16,+8%3E%3E-for-__m128bh)

1.89.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#358-401)[§](#impl-From%3CSimd%3Cu16,+16%3E%3E-for-__m256bh)

1.89.0 · [Source](https://doc.rust-lang.org/src/core/stdarch/crates/core_arch/src/x86/mod.rs.html#358-401)[§](#impl-From%3CSimd%3Cu16,+32%3E%3E-for-__m512bh)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1264)[§](#impl-From%3C%5Bu8;+4%5D%3E-for-IpAddr)

1.9.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#1245)[§](#impl-From%3C%5Bu8;+4%5D%3E-for-Ipv4Addr)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2295)[§](#impl-From%3C%5Bu8;+16%5D%3E-for-IpAddr)

1.9.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2238)[§](#impl-From%3C%5Bu8;+16%5D%3E-for-Ipv6Addr)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2323)[§](#impl-From%3C%5Bu16;+8%5D%3E-for-IpAddr)

1.16.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/ip_addr.rs.html#2266)[§](#impl-From%3C%5Bu16;+8%5D%3E-for-Ipv6Addr)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3207)[§](#impl-From%3C%26str%3E-for-Cow%3C'a,+str%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#597)[§](#impl-From%3C%26ByteStr%3E-for-Cow%3C'a,+ByteStr%3E)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#240)[§](#impl-From%3C%26ByteStr%3E-for-ByteString)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#256)[§](#impl-From%3C%26ByteString%3E-for-Cow%3C'a,+ByteStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#880)[§](#impl-From%3C%26CStr%3E-for-Cow%3C'a,+CStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#889)[§](#impl-From%3C%26CString%3E-for-Cow%3C'a,+CStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1432-1438)[§](#impl-From%3C%26OsStr%3E-for-Cow%3C'a,+OsStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1441-1447)[§](#impl-From%3C%26OsString%3E-for-Cow%3C'a,+OsStr%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2096-2105)[§](#impl-From%3C%26Path%3E-for-Cow%3C'a,+Path%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2120-2129)[§](#impl-From%3C%26PathBuf%3E-for-Cow%3C'a,+Path%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3251)[§](#impl-From%3C%26String%3E-for-Cow%3C'a,+str%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#645)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#622)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3183)[§](#impl-From%3CCow%3C'a,+str%3E%3E-for-String)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#755)[§](#impl-From%3CCow%3C'a,+CStr%3E%3E-for-CString)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1450-1457)[§](#impl-From%3CCow%3C'a,+OsStr%3E%3E-for-OsString)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2132-2140)[§](#impl-From%3CCow%3C'a,+Path%3E%3E-for-PathBuf)

[Source](https://doc.rust-lang.org/src/alloc/bstr.rs.html#248)[§](#impl-From%3CByteString%3E-for-Cow%3C'a,+ByteStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#871)[§](#impl-From%3CCString%3E-for-Cow%3C'a,+CStr%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#1423-1429)[§](#impl-From%3COsString%3E-for-Cow%3C'a,+OsStr%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#2108-2117)[§](#impl-From%3CPathBuf%3E-for-Cow%3C'a,+Path%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/string.rs.html#3228)[§](#impl-From%3CString%3E-for-Cow%3C'a,+str%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#601)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#563)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

1.22.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#687)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error%3E)

1.22.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#666)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#3002-3005)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Rc%3CB%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4036-4039)[§](#impl-From%3CCow%3C'a,+B%3E%3E-for-Arc%3CB%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#493)[§](#impl-From%3CE%3E-for-Box%3Cdyn+Error%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#525)[§](#impl-From%3CE%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

1.30.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/option.rs.html#2366)[§](#impl-From%3C%26Option%3CT%3E%3E-for-Option%3C%26T%3E)

1.8.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#5)[§](#impl-From%3C%26%5BT%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

1.28.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#44)[§](#impl-From%3C%26Vec%3CT%3E%3E-for-Cow%3C'a,+%5BT%5D%3E)

1.30.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/option.rs.html#2394)[§](#impl-From%3C%26mut+Option%3CT%3E%3E-for-Option%3C%26mut+T%3E)

1.14.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4352-4354)[§](#impl-From%3CCow%3C'a,+%5BT%5D%3E%3E-for-Vec%3CT%3E)

1.8.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#31)[§](#impl-From%3CVec%3CT%3E%3E-for-Cow%3C'a,+%5BT%5D%3E)

1.77.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/cow.rs.html#18)[§](#impl-From%3C%26%5BT;+N%5D%3E-for-Cow%3C'a,+%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#48)[§](#impl-From%3C%26mut+%5Bu8%5D%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from a fully initialized slice.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#65)[§](#impl-From%3C%26mut+%5BMaybeUninit%3Cu8%3E%5D%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from an uninitialized buffer.

Use `set_init` if part of the buffer is known to be already initialized.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#75)[§](#impl-From%3CBorrowedCursor%3C'data%3E%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from a cursor.

Use `BorrowedCursor::with_unfilled_buf` instead for a safer alternative.

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#200)[§](#impl-From%3CBox%3Cstr,+A%3E%3E-for-Box%3C%5Bu8%5D,+A%3E)

[Source](https://doc.rust-lang.org/src/std/error.rs.html#510-517)[§](#impl-From%3CE%3E-for-Report%3CE%3E)

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/net/socket_addr.rs.html#616)[§](#impl-From%3C%28I,+u16%29%3E-for-SocketAddr)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/map.rs.html#2653)[§](#impl-From%3C%5B%28K,+V%29;+N%5D%3E-for-BTreeMap%3CK,+V%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/map.rs.html#1493-1514)[§](#impl-From%3C%5B%28K,+V%29;+N%5D%3E-for-HashMap%3CK,+V%3E)

1.17.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#61)[§](#impl-From%3C%26%5BT%5D%3E-for-Box%3C%5BT%5D%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2857)[§](#impl-From%3C%26%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3891)[§](#impl-From%3C%26%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4278)[§](#impl-From%3C%26%5BT%5D%3E-for-Vec%3CT%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#83)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Box%3C%5BT%5D%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2876)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Rc%3C%5BT%5D%3E)

1.84.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3910)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Arc%3C%5BT%5D%3E)

1.19.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4293)[§](#impl-From%3C%26mut+%5BT%5D%3E-for-Vec%3CT%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#106)[§](#impl-From%3CCow%3C'_,+%5BT%5D%3E%3E-for-Box%3C%5BT%5D%3E)

1.71.0 · [Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#impl-From%3C%5BT;+1%5D%3E-for-%28T,%29)

This trait is implemented for tuples up to twelve items long.

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#802)[§](#impl-From%3C!%3E-for-T)

**Stability note:** This impl does not yet exist, but we are “reserving space” to add it in the future. See [rust-lang/rust#64715](https://github.com/rust-lang/rust/issues/64715) for details.

1.23.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/sync/atomic.rs.html#2496)[§](#impl-From%3C*mut+T%3E-for-AtomicPtr%3CT%3E)

Available on **`target_has_atomic_load_store=ptr`** only.

1.25.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/ptr/non_null.rs.html#1773)[§](#impl-From%3C%26T%3E-for-NonNull%3CT%3E)

1.25.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/ptr/non_null.rs.html#1761)[§](#impl-From%3C%26mut+T%3E-for-NonNull%3CT%3E)

1.71.0 · [Source](https://doc.rust-lang.org/src/core/tuple.rs.html#238)[§](#impl-From%3C%28T,%29%3E-for-%5BT;+1%5D)

This trait is implemented for tuples up to twelve items long.

1.31.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#310-312)[§](#impl-From%3CNonZero%3CT%3E%3E-for-T)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#228)[§](#impl-From%3CRange%3CT%3E%3E-for-Range%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#569)[§](#impl-From%3CRangeFrom%3CT%3E%3E-for-RangeFrom%3CT%3E)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#409)[§](#impl-From%3CRangeInclusive%3CT%3E%3E-for-RangeInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#665)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#219)[§](#impl-From%3CRange%3CT%3E%3E-for-Range%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#561)[§](#impl-From%3CRangeFrom%3CT%3E%3E-for-RangeFrom%3CT%3E-1)

1.95.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/range.rs.html#401)[§](#impl-From%3CRangeInclusive%3CT%3E%3E-for-RangeInclusive%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/core/range.rs.html#671)[§](#impl-From%3CRangeToInclusive%3CT%3E%3E-for-RangeToInclusive%3CT%3E-1)

[Source](https://doc.rust-lang.org/src/std/sync/oneshot.rs.html#455-466)[§](#impl-From%3CRecvError%3E-for-RecvTimeoutError%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/oneshot.rs.html#421-432)[§](#impl-From%3CRecvError%3E-for-TryRecvError%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/mpmc/error.rs.html#43-49)[§](#impl-From%3CSendError%3CT%3E%3E-for-SendTimeoutError%3CT%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/sync/mpsc.rs.html#1139-1150)[§](#impl-From%3CSendError%3CT%3E%3E-for-TrySendError%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison.rs.html#333-337)[§](#impl-From%3CPoisonError%3CT%3E%3E-for-TryLockError%3CT%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/os/windows/io/handle.rs.html#656-661)[§](#impl-From%3CJoinHandle%3CT%3E%3E-for-OwnedHandle)

Available on **Windows** only.

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/option.rs.html#2349)[§](#impl-From%3CT%3E-for-Option%3CT%3E)

1.36.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#219)[§](#impl-From%3CT%3E-for-Poll%3CT%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#19)[§](#impl-From%3CT%3E-for-Box%3CT%3E)

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#394)[§](#impl-From%3CT%3E-for-Cell%3CT%3E)

1.70.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/cell/once.rs.html#400)[§](#impl-From%3CT%3E-for-OnceCell%3CT%3E)

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#1542)[§](#impl-From%3CT%3E-for-RefCell%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/cell.rs.html#2686)[§](#impl-From%3CT%3E-for-SyncUnsafeCell%3CT%3E)

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/cell.rs.html#2579)[§](#impl-From%3CT%3E-for-UnsafeCell%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/pin/unsafe_pinned.rs.html#152)[§](#impl-From%3CT%3E-for-UnsafePinned%3CT%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2815)[§](#impl-From%3CT%3E-for-Rc%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/mutex.rs.html#416-422)[§](#impl-From%3CT%3E-for-Mutex%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/nonpoison/rwlock.rs.html#590-596)[§](#impl-From%3CT%3E-for-RwLock%3CT%3E)

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3848)[§](#impl-From%3CT%3E-for-Arc%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/sync/exclusive.rs.html#174)[§](#impl-From%3CT%3E-for-Exclusive%3CT%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/mutex.rs.html#682-688)[§](#impl-From%3CT%3E-for-Mutex%3CT%3E-1)

1.70.0 · [Source](https://doc.rust-lang.org/src/std/sync/once_lock.rs.html#641-665)[§](#impl-From%3CT%3E-for-OnceLock%3CT%3E)

[Source](https://doc.rust-lang.org/src/std/sync/reentrant_lock.rs.html#390-394)[§](#impl-From%3CT%3E-for-ReentrantLock%3CT%3E)

1.24.0 · [Source](https://doc.rust-lang.org/src/std/sync/poison/rwlock.rs.html#724-730)[§](#impl-From%3CT%3E-for-RwLock%3CT%3E-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#785)[§](#impl-From%3CT%3E-for-T)

1.18.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4377)[§](#impl-From%3CBox%3C%5BT%5D,+A%3E%3E-for-Vec%3CT,+A%3E)

1.33.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#39-41)[§](#impl-From%3CBox%3CT,+A%3E%3E-for-Pin%3CBox%3CT,+A%3E%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2954)[§](#impl-From%3CBox%3CT,+A%3E%3E-for-Rc%3CT,+A%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3988)[§](#impl-From%3CBox%3CT,+A%3E%3E-for-Arc%3CT,+A%3E)

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#1949)[§](#impl-From%3CBinaryHeap%3CT,+A%3E%3E-for-Vec%3CT,+A%3E)

1.10.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3753)[§](#impl-From%3CVecDeque%3CT,+A%3E%3E-for-Vec%3CT,+A%3E)

1.20.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4395)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Box%3C%5BT%5D,+A%3E)

1.5.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#1921)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-BinaryHeap%3CT,+A%3E)

1.10.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3736)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-VecDeque%3CT,+A%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2973)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Rc%3C%5BT%5D,+A%3E)

1.21.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#4007)[§](#impl-From%3CVec%3CT,+A%3E%3E-for-Arc%3C%5BT%5D,+A%3E)

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4308)[§](#impl-From%3C%26%5BT;+N%5D%3E-for-Vec%3CT%3E)

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4323)[§](#impl-From%3C%26mut+%5BT;+N%5D%3E-for-Vec%3CT%3E)

1.45.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#226)[§](#impl-From%3C%5BT;+N%5D%3E-for-Box%3C%5BT%5D%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/btree/set.rs.html#1491)[§](#impl-From%3C%5BT;+N%5D%3E-for-BTreeSet%3CT%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/binary_heap/mod.rs.html#1933)[§](#impl-From%3C%5BT;+N%5D%3E-for-BinaryHeap%3CT%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/std/collections/hash/set.rs.html#1169-1190)[§](#impl-From%3C%5BT;+N%5D%3E-for-HashSet%3CT%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/linked_list.rs.html#2198)[§](#impl-From%3C%5BT;+N%5D%3E-for-LinkedList%3CT%3E)

1.56.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/vec_deque/mod.rs.html#3802)[§](#impl-From%3C%5BT;+N%5D%3E-for-VecDeque%3CT%3E)

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/rc.rs.html#2836)[§](#impl-From%3C%5BT;+N%5D%3E-for-Rc%3C%5BT%5D%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1018-1020)[§](#impl-From%3C%5BT;+N%5D%3E-for-Simd%3CT,+N%3E)

1.74.0 · [Source](https://doc.rust-lang.org/src/alloc/sync.rs.html#3870)[§](#impl-From%3C%5BT;+N%5D%3E-for-Arc%3C%5BT%5D%3E)

1.44.0 · [Source](https://doc.rust-lang.org/src/alloc/vec/mod.rs.html#4338)[§](#impl-From%3C%5BT;+N%5D%3E-for-Vec%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#421-423)[§](#impl-From%3CMask%3CT,+N%3E%3E-for-%5Bbool;+N%5D)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1028-1030)[§](#impl-From%3CSimd%3CT,+N%3E%3E-for-%5BT;+N%5D)

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1578)[§](#impl-From%3CMaybeUninit%3C%5BT;+N%5D%3E%3E-for-%5BMaybeUninit%3CT%3E;+N%5D)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#411-413)[§](#impl-From%3C%5Bbool;+N%5D%3E-for-Mask%3CT,+N%3E)

1.95.0 · [Source](https://doc.rust-lang.org/src/core/mem/maybe_uninit.rs.html#1536)[§](#impl-From%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/ffi/os_str.rs.html#620-649)[§](#impl-From%3C%26T%3E-for-OsString)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/path.rs.html#1954-1962)[§](#impl-From%3C%26T%3E-for-PathBuf)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/buffered/mod.rs.html#175-179)[§](#impl-From%3CIntoInnerError%3CW%3E%3E-for-Error)

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#326)[§](#impl-From%3CRc%3CW%3E%3E-for-LocalWaker)

[Source](https://doc.rust-lang.org/src/alloc/task.rs.html#338)[§](#impl-From%3CRc%3CW%3E%3E-for-RawWaker)

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/task.rs.html#121)[§](#impl-From%3CArc%3CW%3E%3E-for-RawWaker)

Available on **`target_has_atomic=ptr`** only.

1.51.0 · [Source](https://doc.rust-lang.org/src/alloc/task.rs.html#109)[§](#impl-From%3CArc%3CW%3E%3E-for-Waker)

Available on **`target_has_atomic=ptr`** only.

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#659)[§](#impl-From%3CMask%3Ci8,+N%3E%3E-for-Mask%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#659)[§](#impl-From%3CMask%3Ci8,+N%3E%3E-for-Mask%3Ci32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#659)[§](#impl-From%3CMask%3Ci8,+N%3E%3E-for-Mask%3Ci64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#659)[§](#impl-From%3CMask%3Ci8,+N%3E%3E-for-Mask%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#660)[§](#impl-From%3CMask%3Ci16,+N%3E%3E-for-Mask%3Ci8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#660)[§](#impl-From%3CMask%3Ci16,+N%3E%3E-for-Mask%3Ci32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#660)[§](#impl-From%3CMask%3Ci16,+N%3E%3E-for-Mask%3Ci64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#660)[§](#impl-From%3CMask%3Ci16,+N%3E%3E-for-Mask%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#661)[§](#impl-From%3CMask%3Ci32,+N%3E%3E-for-Mask%3Ci8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#661)[§](#impl-From%3CMask%3Ci32,+N%3E%3E-for-Mask%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#661)[§](#impl-From%3CMask%3Ci32,+N%3E%3E-for-Mask%3Ci64,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#661)[§](#impl-From%3CMask%3Ci32,+N%3E%3E-for-Mask%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#662)[§](#impl-From%3CMask%3Ci64,+N%3E%3E-for-Mask%3Ci8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#662)[§](#impl-From%3CMask%3Ci64,+N%3E%3E-for-Mask%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#662)[§](#impl-From%3CMask%3Ci64,+N%3E%3E-for-Mask%3Ci32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#662)[§](#impl-From%3CMask%3Ci64,+N%3E%3E-for-Mask%3Cisize,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#663)[§](#impl-From%3CMask%3Cisize,+N%3E%3E-for-Mask%3Ci8,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#663)[§](#impl-From%3CMask%3Cisize,+N%3E%3E-for-Mask%3Ci16,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#663)[§](#impl-From%3CMask%3Cisize,+N%3E%3E-for-Mask%3Ci32,+N%3E)

[Source](https://doc.rust-lang.org/src/core/portable-simd/crates/core_simd/src/masks.rs.html#663)[§](#impl-From%3CMask%3Cisize,+N%3E%3E-for-Mask%3Ci64,+N%3E)