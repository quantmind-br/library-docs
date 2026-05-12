---
title: UnsafeUnpin in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html
source: crawler
fetched_at: 2026-05-06T21:24:04.477431215-03:00
rendered_js: false
word_count: 3678
summary: The UnsafeUnpin trait is an experimental marker trait used to track whether a type contains pinned data internally, influencing compiler optimizations like noalias metadata emission.
tags:
    - rust
    - unsafe
    - pinned-types
    - compiler-optimization
    - nightly-api
    - marker-trait
category: reference
---

```rust
pub unsafe auto trait UnsafeUnpin { }
```

🔬This is a nightly-only experimental API. (`unsafe_unpin` [#125735](https://github.com/rust-lang/rust/issues/125735))

Expand description

Used to determine whether a type contains any `UnsafePinned` (or `PhantomPinned`) internally, but not through an indirection. This affects, for example, whether we emit `noalias` metadata for `&mut T` or not.

This is part of [RFC 3467](https://rust-lang.github.io/rfcs/3467-unsafe-pinned.html), and is tracked by [#125735](https://github.com/rust-lang/rust/issues/125735).

## Implementors[§](#implementors)

## Auto implementors[§](#synthetic-implementors)

[§](#impl-UnsafeUnpin-for-Request%3C'a%3E)

### impl&lt;'a&gt; \![UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Request](https://doc.rust-lang.org/std/error/struct.Request.html "struct std::error::Request")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-DynMetadata%3CDyn%3E)

### impl&lt;Dyn&gt; \![UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DynMetadata](https://doc.rust-lang.org/std/ptr/struct.DynMetadata.html "struct std::ptr::DynMetadata")&lt;Dyn&gt;

[§](#impl-UnsafeUnpin-for-TraitImpl%3CT%3E)

### impl&lt;T&gt; \![UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TraitImpl](https://doc.rust-lang.org/std/mem/type_info/struct.TraitImpl.html "struct std::mem::type_info::TraitImpl")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Char)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AsciiChar](https://doc.rust-lang.org/std/ascii/enum.Char.html "enum std::ascii::Char")

[§](#impl-UnsafeUnpin-for-BacktraceStatus)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BacktraceStatus](https://doc.rust-lang.org/std/backtrace/enum.BacktraceStatus.html "enum std::backtrace::BacktraceStatus")

[§](#impl-UnsafeUnpin-for-Ordering)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::cmp::[Ordering](https://doc.rust-lang.org/std/cmp/enum.Ordering.html "enum std::cmp::Ordering")

[§](#impl-UnsafeUnpin-for-TryReserveErrorKind)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryReserveErrorKind](https://doc.rust-lang.org/std/collections/enum.TryReserveErrorKind.html "enum std::collections::TryReserveErrorKind")

[§](#impl-UnsafeUnpin-for-Infallible)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Infallible](https://doc.rust-lang.org/std/convert/enum.Infallible.html "enum std::convert::Infallible")

[§](#impl-UnsafeUnpin-for-VarError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [VarError](https://doc.rust-lang.org/std/env/enum.VarError.html "enum std::env::VarError")

[§](#impl-UnsafeUnpin-for-FromBytesWithNulError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromBytesWithNulError](https://doc.rust-lang.org/std/ffi/enum.FromBytesWithNulError.html "enum std::ffi::FromBytesWithNulError")

[§](#impl-UnsafeUnpin-for-c_void)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [c\_void](https://doc.rust-lang.org/std/ffi/enum.c_void.html "enum std::ffi::c_void")

[§](#impl-UnsafeUnpin-for-Alignment)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::fmt::[Alignment](https://doc.rust-lang.org/std/fmt/enum.Alignment.html "enum std::fmt::Alignment")

[§](#impl-UnsafeUnpin-for-DebugAsHex)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugAsHex](https://doc.rust-lang.org/std/fmt/enum.DebugAsHex.html "enum std::fmt::DebugAsHex")

[§](#impl-UnsafeUnpin-for-Sign)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Sign](https://doc.rust-lang.org/std/fmt/enum.Sign.html "enum std::fmt::Sign")

[§](#impl-UnsafeUnpin-for-TryLockError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::fs::[TryLockError](https://doc.rust-lang.org/std/fs/enum.TryLockError.html "enum std::fs::TryLockError")

[§](#impl-UnsafeUnpin-for-Locality)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Locality](https://doc.rust-lang.org/std/hint/enum.Locality.html "enum std::hint::Locality")

[§](#impl-UnsafeUnpin-for-AtomicOrdering)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicOrdering](https://doc.rust-lang.org/std/intrinsics/enum.AtomicOrdering.html "enum std::intrinsics::AtomicOrdering")

[§](#impl-UnsafeUnpin-for-BasicBlock)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BasicBlock](https://doc.rust-lang.org/std/intrinsics/mir/enum.BasicBlock.html "enum std::intrinsics::mir::BasicBlock")

[§](#impl-UnsafeUnpin-for-UnwindTerminateReason)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UnwindTerminateReason](https://doc.rust-lang.org/std/intrinsics/mir/enum.UnwindTerminateReason.html "enum std::intrinsics::mir::UnwindTerminateReason")

[§](#impl-UnsafeUnpin-for-SimdAlign)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SimdAlign](https://doc.rust-lang.org/std/intrinsics/simd/enum.SimdAlign.html "enum std::intrinsics::simd::SimdAlign")

[§](#impl-UnsafeUnpin-for-ErrorKind)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ErrorKind](https://doc.rust-lang.org/std/io/enum.ErrorKind.html "enum std::io::ErrorKind")

[§](#impl-UnsafeUnpin-for-SeekFrom)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SeekFrom](https://doc.rust-lang.org/std/io/enum.SeekFrom.html "enum std::io::SeekFrom")

[§](#impl-UnsafeUnpin-for-Abi)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Abi](https://doc.rust-lang.org/std/mem/type_info/enum.Abi.html "enum std::mem::type_info::Abi")

[§](#impl-UnsafeUnpin-for-Generic)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Generic](https://doc.rust-lang.org/std/mem/type_info/enum.Generic.html "enum std::mem::type_info::Generic")

[§](#impl-UnsafeUnpin-for-TypeKind)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TypeKind](https://doc.rust-lang.org/std/mem/type_info/enum.TypeKind.html "enum std::mem::type_info::TypeKind")

[§](#impl-UnsafeUnpin-for-IpAddr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IpAddr](https://doc.rust-lang.org/std/net/enum.IpAddr.html "enum std::net::IpAddr")

[§](#impl-UnsafeUnpin-for-Ipv6MulticastScope)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ipv6MulticastScope](https://doc.rust-lang.org/std/net/enum.Ipv6MulticastScope.html "enum std::net::Ipv6MulticastScope")

[§](#impl-UnsafeUnpin-for-Shutdown)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Shutdown](https://doc.rust-lang.org/std/net/enum.Shutdown.html "enum std::net::Shutdown")

[§](#impl-UnsafeUnpin-for-SocketAddr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::net::[SocketAddr](https://doc.rust-lang.org/std/net/enum.SocketAddr.html "enum std::net::SocketAddr")

[§](#impl-UnsafeUnpin-for-FpCategory)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FpCategory](https://doc.rust-lang.org/std/num/enum.FpCategory.html "enum std::num::FpCategory")

[§](#impl-UnsafeUnpin-for-IntErrorKind)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntErrorKind](https://doc.rust-lang.org/std/num/enum.IntErrorKind.html "enum std::num::IntErrorKind")

[§](#impl-UnsafeUnpin-for-OneSidedRangeBound)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OneSidedRangeBound](https://doc.rust-lang.org/std/ops/enum.OneSidedRangeBound.html "enum std::ops::OneSidedRangeBound")

[§](#impl-UnsafeUnpin-for-AncillaryError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AncillaryError](https://doc.rust-lang.org/std/os/unix/net/enum.AncillaryError.html "enum std::os::unix::net::AncillaryError")

[§](#impl-UnsafeUnpin-for-BacktraceStyle)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BacktraceStyle](https://doc.rust-lang.org/std/panic/enum.BacktraceStyle.html "enum std::panic::BacktraceStyle")

[§](#impl-UnsafeUnpin-for-GetDisjointMutError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [GetDisjointMutError](https://doc.rust-lang.org/std/slice/enum.GetDisjointMutError.html "enum std::slice::GetDisjointMutError")

[§](#impl-UnsafeUnpin-for-SearchStep)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SearchStep](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html "enum std::str::pattern::SearchStep")

[§](#impl-UnsafeUnpin-for-Ordering-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::atomic::[Ordering](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html "enum std::sync::atomic::Ordering")

[§](#impl-UnsafeUnpin-for-RecvTimeoutError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[RecvTimeoutError](https://doc.rust-lang.org/std/sync/mpsc/enum.RecvTimeoutError.html "enum std::sync::mpsc::RecvTimeoutError")

[§](#impl-UnsafeUnpin-for-TryRecvError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[TryRecvError](https://doc.rust-lang.org/std/sync/mpsc/enum.TryRecvError.html "enum std::sync::mpsc::TryRecvError")

[§](#impl-UnsafeUnpin-for-bool)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [bool](https://doc.rust-lang.org/std/primitive.bool.html)

[§](#impl-UnsafeUnpin-for-char)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [char](https://doc.rust-lang.org/std/primitive.char.html)

[§](#impl-UnsafeUnpin-for-f16)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [f16](https://doc.rust-lang.org/std/primitive.f16.html)

[§](#impl-UnsafeUnpin-for-f32)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [f32](https://doc.rust-lang.org/std/primitive.f32.html)

[§](#impl-UnsafeUnpin-for-f64)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [f64](https://doc.rust-lang.org/std/primitive.f64.html)

[§](#impl-UnsafeUnpin-for-f128)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [f128](https://doc.rust-lang.org/std/primitive.f128.html)

[§](#impl-UnsafeUnpin-for-i8)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [i8](https://doc.rust-lang.org/std/primitive.i8.html)

[§](#impl-UnsafeUnpin-for-i16)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [i16](https://doc.rust-lang.org/std/primitive.i16.html)

[§](#impl-UnsafeUnpin-for-i32)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [i32](https://doc.rust-lang.org/std/primitive.i32.html)

[§](#impl-UnsafeUnpin-for-i64)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [i64](https://doc.rust-lang.org/std/primitive.i64.html)

[§](#impl-UnsafeUnpin-for-i128)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [i128](https://doc.rust-lang.org/std/primitive.i128.html)

[§](#impl-UnsafeUnpin-for-isize)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [isize](https://doc.rust-lang.org/std/primitive.isize.html)

[§](#impl-UnsafeUnpin-for-!)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [!](https://doc.rust-lang.org/std/primitive.never.html)

[§](#impl-UnsafeUnpin-for-str)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [str](https://doc.rust-lang.org/std/primitive.str.html)

[§](#impl-UnsafeUnpin-for-u8)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [u8](https://doc.rust-lang.org/std/primitive.u8.html)

[§](#impl-UnsafeUnpin-for-u16)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [u16](https://doc.rust-lang.org/std/primitive.u16.html)

[§](#impl-UnsafeUnpin-for-u32)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [u32](https://doc.rust-lang.org/std/primitive.u32.html)

[§](#impl-UnsafeUnpin-for-u64)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [u64](https://doc.rust-lang.org/std/primitive.u64.html)

[§](#impl-UnsafeUnpin-for-u128)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [u128](https://doc.rust-lang.org/std/primitive.u128.html)

[§](#impl-UnsafeUnpin-for-%28%29)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [()](https://doc.rust-lang.org/std/primitive.unit.html)

[§](#impl-UnsafeUnpin-for-usize)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [usize](https://doc.rust-lang.org/std/primitive.usize.html)

[§](#impl-UnsafeUnpin-for-AllocError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AllocError](https://doc.rust-lang.org/std/alloc/struct.AllocError.html "struct std::alloc::AllocError")

[§](#impl-UnsafeUnpin-for-Global)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Global](https://doc.rust-lang.org/std/alloc/struct.Global.html "struct std::alloc::Global")

[§](#impl-UnsafeUnpin-for-Layout)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Layout](https://doc.rust-lang.org/std/alloc/struct.Layout.html "struct std::alloc::Layout")

[§](#impl-UnsafeUnpin-for-LayoutError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LayoutError](https://doc.rust-lang.org/std/alloc/struct.LayoutError.html "struct std::alloc::LayoutError")

[§](#impl-UnsafeUnpin-for-System)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [System](https://doc.rust-lang.org/std/alloc/struct.System.html "struct std::alloc::System")

[§](#impl-UnsafeUnpin-for-TypeId)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId")

[§](#impl-UnsafeUnpin-for-TryFromSliceError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryFromSliceError](https://doc.rust-lang.org/std/array/struct.TryFromSliceError.html "struct std::array::TryFromSliceError")

[§](#impl-UnsafeUnpin-for-EscapeDefault)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ascii::[EscapeDefault](https://doc.rust-lang.org/std/ascii/struct.EscapeDefault.html "struct std::ascii::EscapeDefault")

[§](#impl-UnsafeUnpin-for-Backtrace)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Backtrace](https://doc.rust-lang.org/std/backtrace/struct.Backtrace.html "struct std::backtrace::Backtrace")

[§](#impl-UnsafeUnpin-for-BacktraceFrame)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BacktraceFrame](https://doc.rust-lang.org/std/backtrace/struct.BacktraceFrame.html "struct std::backtrace::BacktraceFrame")

[§](#impl-UnsafeUnpin-for-ByteStr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ByteStr](https://doc.rust-lang.org/std/bstr/struct.ByteStr.html "struct std::bstr::ByteStr")

[§](#impl-UnsafeUnpin-for-ByteString)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ByteString](https://doc.rust-lang.org/std/bstr/struct.ByteString.html "struct std::bstr::ByteString")

[§](#impl-UnsafeUnpin-for-BorrowError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowError](https://doc.rust-lang.org/std/cell/struct.BorrowError.html "struct std::cell::BorrowError")

[§](#impl-UnsafeUnpin-for-BorrowMutError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowMutError](https://doc.rust-lang.org/std/cell/struct.BorrowMutError.html "struct std::cell::BorrowMutError")

[§](#impl-UnsafeUnpin-for-CharTryFromError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharTryFromError](https://doc.rust-lang.org/std/char/struct.CharTryFromError.html "struct std::char::CharTryFromError")

[§](#impl-UnsafeUnpin-for-DecodeUtf16Error)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DecodeUtf16Error](https://doc.rust-lang.org/std/char/struct.DecodeUtf16Error.html "struct std::char::DecodeUtf16Error")

[§](#impl-UnsafeUnpin-for-EscapeDebug)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::char::[EscapeDebug](https://doc.rust-lang.org/std/char/struct.EscapeDebug.html "struct std::char::EscapeDebug")

[§](#impl-UnsafeUnpin-for-EscapeDefault-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::char::[EscapeDefault](https://doc.rust-lang.org/std/char/struct.EscapeDefault.html "struct std::char::EscapeDefault")

[§](#impl-UnsafeUnpin-for-EscapeUnicode)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::char::[EscapeUnicode](https://doc.rust-lang.org/std/char/struct.EscapeUnicode.html "struct std::char::EscapeUnicode")

[§](#impl-UnsafeUnpin-for-ParseCharError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ParseCharError](https://doc.rust-lang.org/std/char/struct.ParseCharError.html "struct std::char::ParseCharError")

[§](#impl-UnsafeUnpin-for-ToLowercase)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ToLowercase](https://doc.rust-lang.org/std/char/struct.ToLowercase.html "struct std::char::ToLowercase")

[§](#impl-UnsafeUnpin-for-ToUppercase)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ToUppercase](https://doc.rust-lang.org/std/char/struct.ToUppercase.html "struct std::char::ToUppercase")

[§](#impl-UnsafeUnpin-for-TryFromCharError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryFromCharError](https://doc.rust-lang.org/std/char/struct.TryFromCharError.html "struct std::char::TryFromCharError")

[§](#impl-UnsafeUnpin-for-UnorderedKeyError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UnorderedKeyError](https://doc.rust-lang.org/std/collections/btree_map/struct.UnorderedKeyError.html "struct std::collections::btree_map::UnorderedKeyError")

[§](#impl-UnsafeUnpin-for-TryReserveError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryReserveError](https://doc.rust-lang.org/std/collections/struct.TryReserveError.html "struct std::collections::TryReserveError")

[§](#impl-UnsafeUnpin-for-Args)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Args](https://doc.rust-lang.org/std/env/struct.Args.html "struct std::env::Args")

[§](#impl-UnsafeUnpin-for-ArgsOs)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ArgsOs](https://doc.rust-lang.org/std/env/struct.ArgsOs.html "struct std::env::ArgsOs")

[§](#impl-UnsafeUnpin-for-JoinPathsError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [JoinPathsError](https://doc.rust-lang.org/std/env/struct.JoinPathsError.html "struct std::env::JoinPathsError")

[§](#impl-UnsafeUnpin-for-Vars)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Vars](https://doc.rust-lang.org/std/env/struct.Vars.html "struct std::env::Vars")

[§](#impl-UnsafeUnpin-for-VarsOs)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [VarsOs](https://doc.rust-lang.org/std/env/struct.VarsOs.html "struct std::env::VarsOs")

[§](#impl-UnsafeUnpin-for-CStr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CStr](https://doc.rust-lang.org/std/ffi/struct.CStr.html "struct std::ffi::CStr")

[§](#impl-UnsafeUnpin-for-CString)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CString](https://doc.rust-lang.org/std/ffi/struct.CString.html "struct std::ffi::CString")

[§](#impl-UnsafeUnpin-for-FromBytesUntilNulError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromBytesUntilNulError](https://doc.rust-lang.org/std/ffi/struct.FromBytesUntilNulError.html "struct std::ffi::FromBytesUntilNulError")

[§](#impl-UnsafeUnpin-for-FromVecWithNulError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromVecWithNulError](https://doc.rust-lang.org/std/ffi/struct.FromVecWithNulError.html "struct std::ffi::FromVecWithNulError")

[§](#impl-UnsafeUnpin-for-IntoStringError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntoStringError](https://doc.rust-lang.org/std/ffi/struct.IntoStringError.html "struct std::ffi::IntoStringError")

[§](#impl-UnsafeUnpin-for-NulError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [NulError](https://doc.rust-lang.org/std/ffi/struct.NulError.html "struct std::ffi::NulError")

[§](#impl-UnsafeUnpin-for-OsStr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OsStr](https://doc.rust-lang.org/std/ffi/struct.OsStr.html "struct std::ffi::OsStr")

[§](#impl-UnsafeUnpin-for-OsString)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OsString](https://doc.rust-lang.org/std/ffi/struct.OsString.html "struct std::ffi::OsString")

[§](#impl-UnsafeUnpin-for-Error)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::fmt::[Error](https://doc.rust-lang.org/std/fmt/struct.Error.html "struct std::fmt::Error")

[§](#impl-UnsafeUnpin-for-FormattingOptions)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FormattingOptions](https://doc.rust-lang.org/std/fmt/struct.FormattingOptions.html "struct std::fmt::FormattingOptions")

[§](#impl-UnsafeUnpin-for-Dir)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Dir](https://doc.rust-lang.org/std/fs/struct.Dir.html "struct std::fs::Dir")

[§](#impl-UnsafeUnpin-for-DirBuilder)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DirBuilder](https://doc.rust-lang.org/std/fs/struct.DirBuilder.html "struct std::fs::DirBuilder")

[§](#impl-UnsafeUnpin-for-DirEntry)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DirEntry](https://doc.rust-lang.org/std/fs/struct.DirEntry.html "struct std::fs::DirEntry")

[§](#impl-UnsafeUnpin-for-File)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [File](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")

[§](#impl-UnsafeUnpin-for-FileTimes)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FileTimes](https://doc.rust-lang.org/std/fs/struct.FileTimes.html "struct std::fs::FileTimes")

[§](#impl-UnsafeUnpin-for-FileType)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FileType](https://doc.rust-lang.org/std/fs/struct.FileType.html "struct std::fs::FileType")

[§](#impl-UnsafeUnpin-for-Metadata)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Metadata](https://doc.rust-lang.org/std/fs/struct.Metadata.html "struct std::fs::Metadata")

[§](#impl-UnsafeUnpin-for-OpenOptions)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OpenOptions](https://doc.rust-lang.org/std/fs/struct.OpenOptions.html "struct std::fs::OpenOptions")

[§](#impl-UnsafeUnpin-for-Permissions)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Permissions](https://doc.rust-lang.org/std/fs/struct.Permissions.html "struct std::fs::Permissions")

[§](#impl-UnsafeUnpin-for-ReadDir)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ReadDir](https://doc.rust-lang.org/std/fs/struct.ReadDir.html "struct std::fs::ReadDir")

[§](#impl-UnsafeUnpin-for-DefaultHasher)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DefaultHasher](https://doc.rust-lang.org/std/hash/struct.DefaultHasher.html "struct std::hash::DefaultHasher")

[§](#impl-UnsafeUnpin-for-RandomState)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RandomState](https://doc.rust-lang.org/std/hash/struct.RandomState.html "struct std::hash::RandomState")

[§](#impl-UnsafeUnpin-for-SipHasher)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SipHasher](https://doc.rust-lang.org/std/hash/struct.SipHasher.html "struct std::hash::SipHasher")

[§](#impl-UnsafeUnpin-for-ReturnToArg)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ReturnToArg](https://doc.rust-lang.org/std/intrinsics/mir/struct.ReturnToArg.html "struct std::intrinsics::mir::ReturnToArg")

[§](#impl-UnsafeUnpin-for-UnwindActionArg)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UnwindActionArg](https://doc.rust-lang.org/std/intrinsics/mir/struct.UnwindActionArg.html "struct std::intrinsics::mir::UnwindActionArg")

[§](#impl-UnsafeUnpin-for-Empty)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Empty](https://doc.rust-lang.org/std/io/struct.Empty.html "struct std::io::Empty")

[§](#impl-UnsafeUnpin-for-Error-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Error](https://doc.rust-lang.org/std/io/struct.Error.html "struct std::io::Error")

[§](#impl-UnsafeUnpin-for-PipeReader)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PipeReader](https://doc.rust-lang.org/std/io/struct.PipeReader.html "struct std::io::PipeReader")

[§](#impl-UnsafeUnpin-for-PipeWriter)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PipeWriter](https://doc.rust-lang.org/std/io/struct.PipeWriter.html "struct std::io::PipeWriter")

[§](#impl-UnsafeUnpin-for-Repeat)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Repeat](https://doc.rust-lang.org/std/io/struct.Repeat.html "struct std::io::Repeat")

[§](#impl-UnsafeUnpin-for-Sink)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Sink](https://doc.rust-lang.org/std/io/struct.Sink.html "struct std::io::Sink")

[§](#impl-UnsafeUnpin-for-Stderr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Stderr](https://doc.rust-lang.org/std/io/struct.Stderr.html "struct std::io::Stderr")

[§](#impl-UnsafeUnpin-for-Stdin)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Stdin](https://doc.rust-lang.org/std/io/struct.Stdin.html "struct std::io::Stdin")

[§](#impl-UnsafeUnpin-for-Stdout)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Stdout](https://doc.rust-lang.org/std/io/struct.Stdout.html "struct std::io::Stdout")

[§](#impl-UnsafeUnpin-for-WriterPanicked)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [WriterPanicked](https://doc.rust-lang.org/std/io/struct.WriterPanicked.html "struct std::io::WriterPanicked")

[§](#impl-UnsafeUnpin-for-Assume)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Assume](https://doc.rust-lang.org/std/mem/struct.Assume.html "struct std::mem::Assume")

[§](#impl-UnsafeUnpin-for-Array)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Array](https://doc.rust-lang.org/std/mem/type_info/struct.Array.html "struct std::mem::type_info::Array")

[§](#impl-UnsafeUnpin-for-Bool)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Bool](https://doc.rust-lang.org/std/mem/type_info/struct.Bool.html "struct std::mem::type_info::Bool")

[§](#impl-UnsafeUnpin-for-Char-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Char](https://doc.rust-lang.org/std/mem/type_info/struct.Char.html "struct std::mem::type_info::Char")

[§](#impl-UnsafeUnpin-for-Const)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Const](https://doc.rust-lang.org/std/mem/type_info/struct.Const.html "struct std::mem::type_info::Const")

[§](#impl-UnsafeUnpin-for-DynTrait)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DynTrait](https://doc.rust-lang.org/std/mem/type_info/struct.DynTrait.html "struct std::mem::type_info::DynTrait")

[§](#impl-UnsafeUnpin-for-DynTraitPredicate)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DynTraitPredicate](https://doc.rust-lang.org/std/mem/type_info/struct.DynTraitPredicate.html "struct std::mem::type_info::DynTraitPredicate")

[§](#impl-UnsafeUnpin-for-Enum)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Enum](https://doc.rust-lang.org/std/mem/type_info/struct.Enum.html "struct std::mem::type_info::Enum")

[§](#impl-UnsafeUnpin-for-Field)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Field](https://doc.rust-lang.org/std/mem/type_info/struct.Field.html "struct std::mem::type_info::Field")

[§](#impl-UnsafeUnpin-for-Float)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Float](https://doc.rust-lang.org/std/mem/type_info/struct.Float.html "struct std::mem::type_info::Float")

[§](#impl-UnsafeUnpin-for-FnPtr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FnPtr](https://doc.rust-lang.org/std/mem/type_info/struct.FnPtr.html "struct std::mem::type_info::FnPtr")

[§](#impl-UnsafeUnpin-for-GenericType)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [GenericType](https://doc.rust-lang.org/std/mem/type_info/struct.GenericType.html "struct std::mem::type_info::GenericType")

[§](#impl-UnsafeUnpin-for-Int)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Int](https://doc.rust-lang.org/std/mem/type_info/struct.Int.html "struct std::mem::type_info::Int")

[§](#impl-UnsafeUnpin-for-Lifetime)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Lifetime](https://doc.rust-lang.org/std/mem/type_info/struct.Lifetime.html "struct std::mem::type_info::Lifetime")

[§](#impl-UnsafeUnpin-for-Pointer)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Pointer](https://doc.rust-lang.org/std/mem/type_info/struct.Pointer.html "struct std::mem::type_info::Pointer")

[§](#impl-UnsafeUnpin-for-Reference)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Reference](https://doc.rust-lang.org/std/mem/type_info/struct.Reference.html "struct std::mem::type_info::Reference")

[§](#impl-UnsafeUnpin-for-Slice)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Slice](https://doc.rust-lang.org/std/mem/type_info/struct.Slice.html "struct std::mem::type_info::Slice")

[§](#impl-UnsafeUnpin-for-Str)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Str](https://doc.rust-lang.org/std/mem/type_info/struct.Str.html "struct std::mem::type_info::Str")

[§](#impl-UnsafeUnpin-for-Struct)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Struct](https://doc.rust-lang.org/std/mem/type_info/struct.Struct.html "struct std::mem::type_info::Struct")

[§](#impl-UnsafeUnpin-for-Trait)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Trait](https://doc.rust-lang.org/std/mem/type_info/struct.Trait.html "struct std::mem::type_info::Trait")

[§](#impl-UnsafeUnpin-for-Tuple)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Tuple](https://doc.rust-lang.org/std/mem/type_info/struct.Tuple.html "struct std::mem::type_info::Tuple")

[§](#impl-UnsafeUnpin-for-Type)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Type](https://doc.rust-lang.org/std/mem/type_info/struct.Type.html "struct std::mem::type_info::Type")

[§](#impl-UnsafeUnpin-for-Union)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::mem::type\_info::[Union](https://doc.rust-lang.org/std/mem/type_info/struct.Union.html "struct std::mem::type_info::Union")

[§](#impl-UnsafeUnpin-for-Variant)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Variant](https://doc.rust-lang.org/std/mem/type_info/struct.Variant.html "struct std::mem::type_info::Variant")

[§](#impl-UnsafeUnpin-for-AddrParseError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AddrParseError](https://doc.rust-lang.org/std/net/struct.AddrParseError.html "struct std::net::AddrParseError")

[§](#impl-UnsafeUnpin-for-IntoIncoming)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntoIncoming](https://doc.rust-lang.org/std/net/struct.IntoIncoming.html "struct std::net::IntoIncoming")

[§](#impl-UnsafeUnpin-for-Ipv4Addr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ipv4Addr](https://doc.rust-lang.org/std/net/struct.Ipv4Addr.html "struct std::net::Ipv4Addr")

[§](#impl-UnsafeUnpin-for-Ipv6Addr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ipv6Addr](https://doc.rust-lang.org/std/net/struct.Ipv6Addr.html "struct std::net::Ipv6Addr")

[§](#impl-UnsafeUnpin-for-SocketAddrV4)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SocketAddrV4](https://doc.rust-lang.org/std/net/struct.SocketAddrV4.html "struct std::net::SocketAddrV4")

[§](#impl-UnsafeUnpin-for-SocketAddrV6)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SocketAddrV6](https://doc.rust-lang.org/std/net/struct.SocketAddrV6.html "struct std::net::SocketAddrV6")

[§](#impl-UnsafeUnpin-for-TcpListener)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TcpListener](https://doc.rust-lang.org/std/net/struct.TcpListener.html "struct std::net::TcpListener")

[§](#impl-UnsafeUnpin-for-TcpStream)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TcpStream](https://doc.rust-lang.org/std/net/struct.TcpStream.html "struct std::net::TcpStream")

[§](#impl-UnsafeUnpin-for-UdpSocket)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UdpSocket](https://doc.rust-lang.org/std/net/struct.UdpSocket.html "struct std::net::UdpSocket")

[§](#impl-UnsafeUnpin-for-ParseFloatError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ParseFloatError](https://doc.rust-lang.org/std/num/struct.ParseFloatError.html "struct std::num::ParseFloatError")

[§](#impl-UnsafeUnpin-for-ParseIntError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ParseIntError](https://doc.rust-lang.org/std/num/struct.ParseIntError.html "struct std::num::ParseIntError")

[§](#impl-UnsafeUnpin-for-TryFromIntError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryFromIntError](https://doc.rust-lang.org/std/num/struct.TryFromIntError.html "struct std::num::TryFromIntError")

[§](#impl-UnsafeUnpin-for-RangeFull)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeFull](https://doc.rust-lang.org/std/ops/struct.RangeFull.html "struct std::ops::RangeFull")

[§](#impl-UnsafeUnpin-for-OwnedFd)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OwnedFd](https://doc.rust-lang.org/std/os/fd/struct.OwnedFd.html "struct std::os::fd::OwnedFd")

[§](#impl-UnsafeUnpin-for-PidFd)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PidFd](https://doc.rust-lang.org/std/os/linux/process/struct.PidFd.html "struct std::os::linux::process::PidFd")

[§](#impl-UnsafeUnpin-for-stat)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [stat](https://doc.rust-lang.org/std/os/linux/raw/struct.stat.html "struct std::os::linux::raw::stat")

[§](#impl-UnsafeUnpin-for-SocketAddr-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::unix::net::[SocketAddr](https://doc.rust-lang.org/std/os/unix/net/struct.SocketAddr.html "struct std::os::unix::net::SocketAddr")

[§](#impl-UnsafeUnpin-for-SocketCred)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SocketCred](https://doc.rust-lang.org/std/os/unix/net/struct.SocketCred.html "struct std::os::unix::net::SocketCred")

[§](#impl-UnsafeUnpin-for-UCred)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UCred](https://doc.rust-lang.org/std/os/unix/net/struct.UCred.html "struct std::os::unix::net::UCred")

[§](#impl-UnsafeUnpin-for-UnixDatagram)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UnixDatagram](https://doc.rust-lang.org/std/os/unix/net/struct.UnixDatagram.html "struct std::os::unix::net::UnixDatagram")

[§](#impl-UnsafeUnpin-for-UnixListener)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::unix::net::[UnixListener](https://doc.rust-lang.org/std/os/unix/net/struct.UnixListener.html "struct std::os::unix::net::UnixListener")

[§](#impl-UnsafeUnpin-for-UnixStream)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::unix::net::[UnixStream](https://doc.rust-lang.org/std/os/unix/net/struct.UnixStream.html "struct std::os::unix::net::UnixStream")

[§](#impl-UnsafeUnpin-for-HandleOrInvalid)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [HandleOrInvalid](https://doc.rust-lang.org/std/os/windows/io/struct.HandleOrInvalid.html "struct std::os::windows::io::HandleOrInvalid")

[§](#impl-UnsafeUnpin-for-HandleOrNull)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [HandleOrNull](https://doc.rust-lang.org/std/os/windows/io/struct.HandleOrNull.html "struct std::os::windows::io::HandleOrNull")

[§](#impl-UnsafeUnpin-for-InvalidHandleError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [InvalidHandleError](https://doc.rust-lang.org/std/os/windows/io/struct.InvalidHandleError.html "struct std::os::windows::io::InvalidHandleError")

[§](#impl-UnsafeUnpin-for-NullHandleError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [NullHandleError](https://doc.rust-lang.org/std/os/windows/io/struct.NullHandleError.html "struct std::os::windows::io::NullHandleError")

[§](#impl-UnsafeUnpin-for-OwnedHandle)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OwnedHandle](https://doc.rust-lang.org/std/os/windows/io/struct.OwnedHandle.html "struct std::os::windows::io::OwnedHandle")

[§](#impl-UnsafeUnpin-for-OwnedSocket)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OwnedSocket](https://doc.rust-lang.org/std/os/windows/io/struct.OwnedSocket.html "struct std::os::windows::io::OwnedSocket")

[§](#impl-UnsafeUnpin-for-SocketAddr-2)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::windows::net::[SocketAddr](https://doc.rust-lang.org/std/os/windows/net/struct.SocketAddr.html "struct std::os::windows::net::SocketAddr")

[§](#impl-UnsafeUnpin-for-UnixListener-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::windows::net::[UnixListener](https://doc.rust-lang.org/std/os/windows/net/struct.UnixListener.html "struct std::os::windows::net::UnixListener")

[§](#impl-UnsafeUnpin-for-UnixStream-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::windows::net::[UnixStream](https://doc.rust-lang.org/std/os/windows/net/struct.UnixStream.html "struct std::os::windows::net::UnixStream")

[§](#impl-UnsafeUnpin-for-NormalizeError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [NormalizeError](https://doc.rust-lang.org/std/path/struct.NormalizeError.html "struct std::path::NormalizeError")

[§](#impl-UnsafeUnpin-for-Path)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Path](https://doc.rust-lang.org/std/path/struct.Path.html "struct std::path::Path")

[§](#impl-UnsafeUnpin-for-PathBuf)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PathBuf](https://doc.rust-lang.org/std/path/struct.PathBuf.html "struct std::path::PathBuf")

[§](#impl-UnsafeUnpin-for-StripPrefixError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StripPrefixError](https://doc.rust-lang.org/std/path/struct.StripPrefixError.html "struct std::path::StripPrefixError")

[§](#impl-UnsafeUnpin-for-Child)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Child](https://doc.rust-lang.org/std/process/struct.Child.html "struct std::process::Child")

[§](#impl-UnsafeUnpin-for-ChildStderr)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChildStderr](https://doc.rust-lang.org/std/process/struct.ChildStderr.html "struct std::process::ChildStderr")

[§](#impl-UnsafeUnpin-for-ChildStdin)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChildStdin](https://doc.rust-lang.org/std/process/struct.ChildStdin.html "struct std::process::ChildStdin")

[§](#impl-UnsafeUnpin-for-ChildStdout)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChildStdout](https://doc.rust-lang.org/std/process/struct.ChildStdout.html "struct std::process::ChildStdout")

[§](#impl-UnsafeUnpin-for-Command)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Command](https://doc.rust-lang.org/std/process/struct.Command.html "struct std::process::Command")

[§](#impl-UnsafeUnpin-for-ExitCode)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ExitCode](https://doc.rust-lang.org/std/process/struct.ExitCode.html "struct std::process::ExitCode")

[§](#impl-UnsafeUnpin-for-ExitStatus)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ExitStatus](https://doc.rust-lang.org/std/process/struct.ExitStatus.html "struct std::process::ExitStatus")

[§](#impl-UnsafeUnpin-for-ExitStatusError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ExitStatusError](https://doc.rust-lang.org/std/process/struct.ExitStatusError.html "struct std::process::ExitStatusError")

[§](#impl-UnsafeUnpin-for-Output)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Output](https://doc.rust-lang.org/std/process/struct.Output.html "struct std::process::Output")

[§](#impl-UnsafeUnpin-for-Stdio)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Stdio](https://doc.rust-lang.org/std/process/struct.Stdio.html "struct std::process::Stdio")

[§](#impl-UnsafeUnpin-for-Alignment-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ptr::[Alignment](https://doc.rust-lang.org/std/ptr/struct.Alignment.html "struct std::ptr::Alignment")

[§](#impl-UnsafeUnpin-for-DefaultRandomSource)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DefaultRandomSource](https://doc.rust-lang.org/std/random/struct.DefaultRandomSource.html "struct std::random::DefaultRandomSource")

[§](#impl-UnsafeUnpin-for-ParseBoolError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ParseBoolError](https://doc.rust-lang.org/std/str/struct.ParseBoolError.html "struct std::str::ParseBoolError")

[§](#impl-UnsafeUnpin-for-Utf8Error)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Utf8Error](https://doc.rust-lang.org/std/str/struct.Utf8Error.html "struct std::str::Utf8Error")

[§](#impl-UnsafeUnpin-for-FromUtf8Error)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromUtf8Error](https://doc.rust-lang.org/std/string/struct.FromUtf8Error.html "struct std::string::FromUtf8Error")

[§](#impl-UnsafeUnpin-for-FromUtf16Error)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromUtf16Error](https://doc.rust-lang.org/std/string/struct.FromUtf16Error.html "struct std::string::FromUtf16Error")

[§](#impl-UnsafeUnpin-for-IntoChars)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntoChars](https://doc.rust-lang.org/std/string/struct.IntoChars.html "struct std::string::IntoChars")

[§](#impl-UnsafeUnpin-for-String)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [String](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String")

[§](#impl-UnsafeUnpin-for-AtomicBool)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicBool](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html "struct std::sync::atomic::AtomicBool")

[§](#impl-UnsafeUnpin-for-AtomicI8)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicI8](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI8.html "struct std::sync::atomic::AtomicI8")

[§](#impl-UnsafeUnpin-for-AtomicI16)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicI16](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI16.html "struct std::sync::atomic::AtomicI16")

[§](#impl-UnsafeUnpin-for-AtomicI32)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicI32](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI32.html "struct std::sync::atomic::AtomicI32")

[§](#impl-UnsafeUnpin-for-AtomicI64)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicI64](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicI64.html "struct std::sync::atomic::AtomicI64")

[§](#impl-UnsafeUnpin-for-AtomicIsize)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicIsize](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicIsize.html "struct std::sync::atomic::AtomicIsize")

[§](#impl-UnsafeUnpin-for-AtomicU8)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicU8](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU8.html "struct std::sync::atomic::AtomicU8")

[§](#impl-UnsafeUnpin-for-AtomicU16)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicU16](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU16.html "struct std::sync::atomic::AtomicU16")

[§](#impl-UnsafeUnpin-for-AtomicU32)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicU32](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU32.html "struct std::sync::atomic::AtomicU32")

[§](#impl-UnsafeUnpin-for-AtomicU64)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicU64](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicU64.html "struct std::sync::atomic::AtomicU64")

[§](#impl-UnsafeUnpin-for-AtomicUsize)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicUsize](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicUsize.html "struct std::sync::atomic::AtomicUsize")

[§](#impl-UnsafeUnpin-for-RecvError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RecvError](https://doc.rust-lang.org/std/sync/mpsc/struct.RecvError.html "struct std::sync::mpsc::RecvError")

[§](#impl-UnsafeUnpin-for-Condvar)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[Condvar](https://doc.rust-lang.org/std/sync/nonpoison/struct.Condvar.html "struct std::sync::nonpoison::Condvar")

[§](#impl-UnsafeUnpin-for-WouldBlock)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [WouldBlock](https://doc.rust-lang.org/std/sync/nonpoison/struct.WouldBlock.html "struct std::sync::nonpoison::WouldBlock")

[§](#impl-UnsafeUnpin-for-Barrier)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Barrier](https://doc.rust-lang.org/std/sync/struct.Barrier.html "struct std::sync::Barrier")

[§](#impl-UnsafeUnpin-for-BarrierWaitResult)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BarrierWaitResult](https://doc.rust-lang.org/std/sync/struct.BarrierWaitResult.html "struct std::sync::BarrierWaitResult")

[§](#impl-UnsafeUnpin-for-Condvar-1)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[Condvar](https://doc.rust-lang.org/std/sync/struct.Condvar.html "struct std::sync::Condvar")

[§](#impl-UnsafeUnpin-for-Once)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[Once](https://doc.rust-lang.org/std/sync/struct.Once.html "struct std::sync::Once")

[§](#impl-UnsafeUnpin-for-OnceState)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OnceState](https://doc.rust-lang.org/std/sync/struct.OnceState.html "struct std::sync::OnceState")

[§](#impl-UnsafeUnpin-for-WaitTimeoutResult)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [WaitTimeoutResult](https://doc.rust-lang.org/std/sync/struct.WaitTimeoutResult.html "struct std::sync::WaitTimeoutResult")

[§](#impl-UnsafeUnpin-for-LocalWaker)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LocalWaker](https://doc.rust-lang.org/std/task/struct.LocalWaker.html "struct std::task::LocalWaker")

[§](#impl-UnsafeUnpin-for-RawWaker)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RawWaker](https://doc.rust-lang.org/std/task/struct.RawWaker.html "struct std::task::RawWaker")

[§](#impl-UnsafeUnpin-for-RawWakerVTable)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RawWakerVTable](https://doc.rust-lang.org/std/task/struct.RawWakerVTable.html "struct std::task::RawWakerVTable")

[§](#impl-UnsafeUnpin-for-Waker)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Waker](https://doc.rust-lang.org/std/task/struct.Waker.html "struct std::task::Waker")

[§](#impl-UnsafeUnpin-for-AccessError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AccessError](https://doc.rust-lang.org/std/thread/struct.AccessError.html "struct std::thread::AccessError")

[§](#impl-UnsafeUnpin-for-Builder)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Builder](https://doc.rust-lang.org/std/thread/struct.Builder.html "struct std::thread::Builder")

[§](#impl-UnsafeUnpin-for-Thread)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Thread](https://doc.rust-lang.org/std/thread/struct.Thread.html "struct std::thread::Thread")

[§](#impl-UnsafeUnpin-for-ThreadId)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ThreadId](https://doc.rust-lang.org/std/thread/struct.ThreadId.html "struct std::thread::ThreadId")

[§](#impl-UnsafeUnpin-for-Duration)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Duration](https://doc.rust-lang.org/std/time/struct.Duration.html "struct std::time::Duration")

[§](#impl-UnsafeUnpin-for-Instant)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Instant](https://doc.rust-lang.org/std/time/struct.Instant.html "struct std::time::Instant")

[§](#impl-UnsafeUnpin-for-SystemTime)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SystemTime](https://doc.rust-lang.org/std/time/struct.SystemTime.html "struct std::time::SystemTime")

[§](#impl-UnsafeUnpin-for-SystemTimeError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SystemTimeError](https://doc.rust-lang.org/std/time/struct.SystemTimeError.html "struct std::time::SystemTimeError")

[§](#impl-UnsafeUnpin-for-TryFromFloatSecsError)

### impl [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TryFromFloatSecsError](https://doc.rust-lang.org/std/time/struct.TryFromFloatSecsError.html "struct std::time::TryFromFloatSecsError")

[§](#impl-UnsafeUnpin-for-AncillaryData%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AncillaryData](https://doc.rust-lang.org/std/os/unix/net/enum.AncillaryData.html "enum std::os::unix::net::AncillaryData")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Component%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Component](https://doc.rust-lang.org/std/path/enum.Component.html "enum std::path::Component")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Prefix%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Prefix](https://doc.rust-lang.org/std/path/enum.Prefix.html "enum std::path::Prefix")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Utf8Pattern%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Utf8Pattern](https://doc.rust-lang.org/std/str/pattern/enum.Utf8Pattern.html "enum std::str::pattern::Utf8Pattern")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-SplitPaths%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitPaths](https://doc.rust-lang.org/std/env/struct.SplitPaths.html "struct std::env::SplitPaths")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Display%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ffi::os\_str::[Display](https://doc.rust-lang.org/std/ffi/os_str/struct.Display.html "struct std::ffi::os_str::Display")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-VaList%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [VaList](https://doc.rust-lang.org/std/ffi/struct.VaList.html "struct std::ffi::VaList")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Arguments%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Arguments](https://doc.rust-lang.org/std/fmt/struct.Arguments.html "struct std::fmt::Arguments")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Formatter%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Formatter](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-BorrowedCursor%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowedCursor](https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html "struct std::io::BorrowedCursor")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-IoSlice%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IoSlice](https://doc.rust-lang.org/std/io/struct.IoSlice.html "struct std::io::IoSlice")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-IoSliceMut%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IoSliceMut](https://doc.rust-lang.org/std/io/struct.IoSliceMut.html "struct std::io::IoSliceMut")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-StderrLock%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StderrLock](https://doc.rust-lang.org/std/io/struct.StderrLock.html "struct std::io::StderrLock")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-StdinLock%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StdinLock](https://doc.rust-lang.org/std/io/struct.StdinLock.html "struct std::io::StdinLock")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-StdoutLock%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StdoutLock](https://doc.rust-lang.org/std/io/struct.StdoutLock.html "struct std::io::StdoutLock")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Incoming%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::net::[Incoming](https://doc.rust-lang.org/std/net/struct.Incoming.html "struct std::net::Incoming")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Incoming%3C'a%3E-1)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::unix::net::[Incoming](https://doc.rust-lang.org/std/os/unix/net/struct.Incoming.html "struct std::os::unix::net::Incoming")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Messages%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Messages](https://doc.rust-lang.org/std/os/unix/net/struct.Messages.html "struct std::os::unix::net::Messages")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-ScmCredentials%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ScmCredentials](https://doc.rust-lang.org/std/os/unix/net/struct.ScmCredentials.html "struct std::os::unix::net::ScmCredentials")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-ScmRights%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ScmRights](https://doc.rust-lang.org/std/os/unix/net/struct.ScmRights.html "struct std::os::unix::net::ScmRights")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-SocketAncillary%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SocketAncillary](https://doc.rust-lang.org/std/os/unix/net/struct.SocketAncillary.html "struct std::os::unix::net::SocketAncillary")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EncodeWide%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [EncodeWide](https://doc.rust-lang.org/std/os/windows/ffi/struct.EncodeWide.html "struct std::os::windows::ffi::EncodeWide")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Incoming%3C'a%3E-2)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::os::windows::net::[Incoming](https://doc.rust-lang.org/std/os/windows/net/struct.Incoming.html "struct std::os::windows::net::Incoming")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-ProcThreadAttributeList%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ProcThreadAttributeList](https://doc.rust-lang.org/std/os/windows/process/struct.ProcThreadAttributeList.html "struct std::os::windows::process::ProcThreadAttributeList")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-ProcThreadAttributeListBuilder%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ProcThreadAttributeListBuilder](https://doc.rust-lang.org/std/os/windows/process/struct.ProcThreadAttributeListBuilder.html "struct std::os::windows::process::ProcThreadAttributeListBuilder")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Location%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Location](https://doc.rust-lang.org/std/panic/struct.Location.html "struct std::panic::Location")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-PanicHookInfo%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PanicHookInfo](https://doc.rust-lang.org/std/panic/struct.PanicHookInfo.html "struct std::panic::PanicHookInfo")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Ancestors%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ancestors](https://doc.rust-lang.org/std/path/struct.Ancestors.html "struct std::path::Ancestors")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Components%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Components](https://doc.rust-lang.org/std/path/struct.Components.html "struct std::path::Components")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Display%3C'a%3E-1)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::path::[Display](https://doc.rust-lang.org/std/path/struct.Display.html "struct std::path::Display")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::path::[Iter](https://doc.rust-lang.org/std/path/struct.Iter.html "struct std::path::Iter")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-PrefixComponent%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PrefixComponent](https://doc.rust-lang.org/std/path/struct.PrefixComponent.html "struct std::path::PrefixComponent")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-CommandArgs%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CommandArgs](https://doc.rust-lang.org/std/process/struct.CommandArgs.html "struct std::process::CommandArgs")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-CommandEnvs%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CommandEnvs](https://doc.rust-lang.org/std/process/struct.CommandEnvs.html "struct std::process::CommandEnvs")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EscapeAscii%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [EscapeAscii](https://doc.rust-lang.org/std/slice/struct.EscapeAscii.html "struct std::slice::EscapeAscii")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Bytes%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[Bytes](https://doc.rust-lang.org/std/str/struct.Bytes.html "struct std::str::Bytes")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-CharIndices%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharIndices](https://doc.rust-lang.org/std/str/struct.CharIndices.html "struct std::str::CharIndices")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Chars%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Chars](https://doc.rust-lang.org/std/str/struct.Chars.html "struct std::str::Chars")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EncodeUtf16%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [EncodeUtf16](https://doc.rust-lang.org/std/str/struct.EncodeUtf16.html "struct std::str::EncodeUtf16")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EscapeDebug%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[EscapeDebug](https://doc.rust-lang.org/std/str/struct.EscapeDebug.html "struct std::str::EscapeDebug")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EscapeDefault%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[EscapeDefault](https://doc.rust-lang.org/std/str/struct.EscapeDefault.html "struct std::str::EscapeDefault")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-EscapeUnicode%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[EscapeUnicode](https://doc.rust-lang.org/std/str/struct.EscapeUnicode.html "struct std::str::EscapeUnicode")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Lines%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[Lines](https://doc.rust-lang.org/std/str/struct.Lines.html "struct std::str::Lines")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-LinesAny%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LinesAny](https://doc.rust-lang.org/std/str/struct.LinesAny.html "struct std::str::LinesAny")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-SplitAsciiWhitespace%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitAsciiWhitespace](https://doc.rust-lang.org/std/str/struct.SplitAsciiWhitespace.html "struct std::str::SplitAsciiWhitespace")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-SplitWhitespace%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitWhitespace](https://doc.rust-lang.org/std/str/struct.SplitWhitespace.html "struct std::str::SplitWhitespace")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Utf8Chunk%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Utf8Chunk](https://doc.rust-lang.org/std/str/struct.Utf8Chunk.html "struct std::str::Utf8Chunk")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Utf8Chunks%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Utf8Chunks](https://doc.rust-lang.org/std/str/struct.Utf8Chunks.html "struct std::str::Utf8Chunks")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::string::[Drain](https://doc.rust-lang.org/std/string/struct.Drain.html "struct std::string::Drain")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-Context%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Context](https://doc.rust-lang.org/std/task/struct.Context.html "struct std::task::Context")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-ContextBuilder%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ContextBuilder](https://doc.rust-lang.org/std/task/struct.ContextBuilder.html "struct std::task::ContextBuilder")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-PhantomContravariantLifetime%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomContravariantLifetime](https://doc.rust-lang.org/std/marker/struct.PhantomContravariantLifetime.html "struct std::marker::PhantomContravariantLifetime")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-PhantomCovariantLifetime%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomCovariantLifetime](https://doc.rust-lang.org/std/marker/struct.PhantomCovariantLifetime.html "struct std::marker::PhantomCovariantLifetime")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-PhantomInvariantLifetime%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomInvariantLifetime](https://doc.rust-lang.org/std/marker/struct.PhantomInvariantLifetime.html "struct std::marker::PhantomInvariantLifetime")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-DebugList%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugList](https://doc.rust-lang.org/std/fmt/struct.DebugList.html "struct std::fmt::DebugList")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-DebugMap%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugMap](https://doc.rust-lang.org/std/fmt/struct.DebugMap.html "struct std::fmt::DebugMap")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-DebugSet%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugSet](https://doc.rust-lang.org/std/fmt/struct.DebugSet.html "struct std::fmt::DebugSet")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-DebugStruct%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugStruct](https://doc.rust-lang.org/std/fmt/struct.DebugStruct.html "struct std::fmt::DebugStruct")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-DebugTuple%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DebugTuple](https://doc.rust-lang.org/std/fmt/struct.DebugTuple.html "struct std::fmt::DebugTuple")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-CharSliceSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharSliceSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSliceSearcher.html "struct std::str::pattern::CharSliceSearcher")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+A%3E)

### impl&lt;'a, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::option::[Iter](https://doc.rust-lang.org/std/option/struct.Iter.html "struct std::option::Iter")&lt;'a, A&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+A%3E)

### impl&lt;'a, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::option::[IterMut](https://doc.rust-lang.org/std/option/struct.IterMut.html "struct std::option::IterMut")&lt;'a, A&gt;

[§](#impl-UnsafeUnpin-for-Cow%3C'a,+B%3E)

### impl&lt;'a, B&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Cow](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow")&lt;'a, B&gt;

[§](#impl-UnsafeUnpin-for-CharPredicateSearcher%3C'a,+F%3E)

### impl&lt;'a, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharPredicateSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharPredicateSearcher.html "struct std::str::pattern::CharPredicateSearcher")&lt;'a, F&gt;

[§](#impl-UnsafeUnpin-for-ByRefSized%3C'a,+I%3E)

### impl&lt;'a, I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ByRefSized](https://doc.rust-lang.org/std/iter/struct.ByRefSized.html "struct std::iter::ByRefSized")&lt;'a, I&gt;

[§](#impl-UnsafeUnpin-for-Splice%3C'a,+I,+A%3E)

### impl&lt;'a, I, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[Splice](https://doc.rust-lang.org/std/collections/vec_deque/struct.Splice.html "struct std::collections::vec_deque::Splice")&lt;'a, I, A&gt;

[§](#impl-UnsafeUnpin-for-Splice%3C'a,+I,+A%3E-1)

### impl&lt;'a, I, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::vec::[Splice](https://doc.rust-lang.org/std/vec/struct.Splice.html "struct std::vec::Splice")&lt;'a, I, A&gt;

[§](#impl-UnsafeUnpin-for-Cursor%3C'a,+K%3E)

### impl&lt;'a, K&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Cursor](https://doc.rust-lang.org/std/collections/btree_set/struct.Cursor.html "struct std::collections::btree_set::Cursor")&lt;'a, K&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+K%3E)

### impl&lt;'a, K&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Iter](https://doc.rust-lang.org/std/collections/hash_set/struct.Iter.html "struct std::collections::hash_set::Iter")&lt;'a, K&gt;

[§](#impl-UnsafeUnpin-for-CursorMut%3C'a,+K,+A%3E)

### impl&lt;'a, K, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[CursorMut](https://doc.rust-lang.org/std/collections/btree_set/struct.CursorMut.html "struct std::collections::btree_set::CursorMut")&lt;'a, K, A&gt;

[§](#impl-UnsafeUnpin-for-CursorMutKey%3C'a,+K,+A%3E)

### impl&lt;'a, K, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[CursorMutKey](https://doc.rust-lang.org/std/collections/btree_set/struct.CursorMutKey.html "struct std::collections::btree_set::CursorMutKey")&lt;'a, K, A&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a,+K,+A%3E)

### impl&lt;'a, K, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Drain](https://doc.rust-lang.org/std/collections/hash_set/struct.Drain.html "struct std::collections::hash_set::Drain")&lt;'a, K, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+K,+F,+A%3E)

### impl&lt;'a, K, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[ExtractIf](https://doc.rust-lang.org/std/collections/hash_set/struct.ExtractIf.html "struct std::collections::hash_set::ExtractIf")&lt;'a, K, F, A&gt;

[§](#impl-UnsafeUnpin-for-Cursor%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Cursor](https://doc.rust-lang.org/std/collections/btree_map/struct.Cursor.html "struct std::collections::btree_map::Cursor")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Iter](https://doc.rust-lang.org/std/collections/btree_map/struct.Iter.html "struct std::collections::btree_map::Iter")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[IterMut](https://doc.rust-lang.org/std/collections/btree_map/struct.IterMut.html "struct std::collections::btree_map::IterMut")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Keys%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Keys](https://doc.rust-lang.org/std/collections/btree_map/struct.Keys.html "struct std::collections::btree_map::Keys")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Range%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Range](https://doc.rust-lang.org/std/collections/btree_map/struct.Range.html "struct std::collections::btree_map::Range")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-RangeMut%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeMut](https://doc.rust-lang.org/std/collections/btree_map/struct.RangeMut.html "struct std::collections::btree_map::RangeMut")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Values%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Values](https://doc.rust-lang.org/std/collections/btree_map/struct.Values.html "struct std::collections::btree_map::Values")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-ValuesMut%3C'a,+K,+V%3E)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[ValuesMut](https://doc.rust-lang.org/std/collections/btree_map/struct.ValuesMut.html "struct std::collections::btree_map::ValuesMut")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+K,+V%3E-1)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[Iter](https://doc.rust-lang.org/std/collections/hash_map/struct.Iter.html "struct std::collections::hash_map::Iter")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+K,+V%3E-1)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[IterMut](https://doc.rust-lang.org/std/collections/hash_map/struct.IterMut.html "struct std::collections::hash_map::IterMut")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Keys%3C'a,+K,+V%3E-1)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[Keys](https://doc.rust-lang.org/std/collections/hash_map/struct.Keys.html "struct std::collections::hash_map::Keys")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Values%3C'a,+K,+V%3E-1)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[Values](https://doc.rust-lang.org/std/collections/hash_map/struct.Values.html "struct std::collections::hash_map::Values")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-ValuesMut%3C'a,+K,+V%3E-1)

### impl&lt;'a, K, V&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[ValuesMut](https://doc.rust-lang.org/std/collections/hash_map/struct.ValuesMut.html "struct std::collections::hash_map::ValuesMut")&lt;'a, K, V&gt;

[§](#impl-UnsafeUnpin-for-Entry%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[Entry](https://doc.rust-lang.org/std/collections/btree_map/enum.Entry.html "enum std::collections::btree_map::Entry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-Entry%3C'a,+K,+V,+A%3E-1)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[Entry](https://doc.rust-lang.org/std/collections/hash_map/enum.Entry.html "enum std::collections::hash_map::Entry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-CursorMut%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[CursorMut](https://doc.rust-lang.org/std/collections/btree_map/struct.CursorMut.html "struct std::collections::btree_map::CursorMut")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-CursorMutKey%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[CursorMutKey](https://doc.rust-lang.org/std/collections/btree_map/struct.CursorMutKey.html "struct std::collections::btree_map::CursorMutKey")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedEntry%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[OccupiedEntry](https://doc.rust-lang.org/std/collections/btree_map/struct.OccupiedEntry.html "struct std::collections::btree_map::OccupiedEntry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedError%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[OccupiedError](https://doc.rust-lang.org/std/collections/btree_map/struct.OccupiedError.html "struct std::collections::btree_map::OccupiedError")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-VacantEntry%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[VacantEntry](https://doc.rust-lang.org/std/collections/btree_map/struct.VacantEntry.html "struct std::collections::btree_map::VacantEntry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a,+K,+V,+A%3E)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[Drain](https://doc.rust-lang.org/std/collections/hash_map/struct.Drain.html "struct std::collections::hash_map::Drain")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedEntry%3C'a,+K,+V,+A%3E-1)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[OccupiedEntry](https://doc.rust-lang.org/std/collections/hash_map/struct.OccupiedEntry.html "struct std::collections::hash_map::OccupiedEntry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedError%3C'a,+K,+V,+A%3E-1)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[OccupiedError](https://doc.rust-lang.org/std/collections/hash_map/struct.OccupiedError.html "struct std::collections::hash_map::OccupiedError")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-VacantEntry%3C'a,+K,+V,+A%3E-1)

### impl&lt;'a, K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[VacantEntry](https://doc.rust-lang.org/std/collections/hash_map/struct.VacantEntry.html "struct std::collections::hash_map::VacantEntry")&lt;'a, K, V, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+K,+V,+F,+A%3E)

### impl&lt;'a, K, V, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[ExtractIf](https://doc.rust-lang.org/std/collections/hash_map/struct.ExtractIf.html "struct std::collections::hash_map::ExtractIf")&lt;'a, K, V, F, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+K,+V,+R,+F,+A%3E)

### impl&lt;'a, K, V, R, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[ExtractIf](https://doc.rust-lang.org/std/collections/btree_map/struct.ExtractIf.html "struct std::collections::btree_map::ExtractIf")&lt;'a, K, V, R, F, A&gt;

[§](#impl-UnsafeUnpin-for-MatchIndices%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [MatchIndices](https://doc.rust-lang.org/std/str/struct.MatchIndices.html "struct std::str::MatchIndices")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-Matches%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Matches](https://doc.rust-lang.org/std/str/struct.Matches.html "struct std::str::Matches")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-RMatchIndices%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RMatchIndices](https://doc.rust-lang.org/std/str/struct.RMatchIndices.html "struct std::str::RMatchIndices")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-RMatches%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RMatches](https://doc.rust-lang.org/std/str/struct.RMatches.html "struct std::str::RMatches")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-RSplit%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[RSplit](https://doc.rust-lang.org/std/str/struct.RSplit.html "struct std::str::RSplit")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-RSplitN%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[RSplitN](https://doc.rust-lang.org/std/str/struct.RSplitN.html "struct std::str::RSplitN")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-RSplitTerminator%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RSplitTerminator](https://doc.rust-lang.org/std/str/struct.RSplitTerminator.html "struct std::str::RSplitTerminator")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-Split%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[Split](https://doc.rust-lang.org/std/str/struct.Split.html "struct std::str::Split")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-SplitInclusive%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[SplitInclusive](https://doc.rust-lang.org/std/str/struct.SplitInclusive.html "struct std::str::SplitInclusive")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-SplitN%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::str::[SplitN](https://doc.rust-lang.org/std/str/struct.SplitN.html "struct std::str::SplitN")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-SplitTerminator%3C'a,+P%3E)

### impl&lt;'a, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitTerminator](https://doc.rust-lang.org/std/str/struct.SplitTerminator.html "struct std::str::SplitTerminator")&lt;'a, P&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::binary\_heap::[Iter](https://doc.rust-lang.org/std/collections/binary_heap/struct.Iter.html "struct std::collections::binary_heap::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-1)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Iter](https://doc.rust-lang.org/std/collections/btree_set/struct.Iter.html "struct std::collections::btree_set::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Range%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Range](https://doc.rust-lang.org/std/collections/btree_set/struct.Range.html "struct std::collections::btree_set::Range")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-SymmetricDifference%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[SymmetricDifference](https://doc.rust-lang.org/std/collections/btree_set/struct.SymmetricDifference.html "struct std::collections::btree_set::SymmetricDifference")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Union%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Union](https://doc.rust-lang.org/std/collections/btree_set/struct.Union.html "struct std::collections::btree_set::Union")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-2)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[Iter](https://doc.rust-lang.org/std/collections/linked_list/struct.Iter.html "struct std::collections::linked_list::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[IterMut](https://doc.rust-lang.org/std/collections/linked_list/struct.IterMut.html "struct std::collections::linked_list::IterMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-3)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[Iter](https://doc.rust-lang.org/std/collections/vec_deque/struct.Iter.html "struct std::collections::vec_deque::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+T%3E-1)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[IterMut](https://doc.rust-lang.org/std/collections/vec_deque/struct.IterMut.html "struct std::collections::vec_deque::IterMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-4)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::result::[Iter](https://doc.rust-lang.org/std/result/struct.Iter.html "struct std::result::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+T%3E-2)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::result::[IterMut](https://doc.rust-lang.org/std/result/struct.IterMut.html "struct std::result::IterMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Chunks%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Chunks](https://doc.rust-lang.org/std/slice/struct.Chunks.html "struct std::slice::Chunks")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-ChunksExact%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChunksExact](https://doc.rust-lang.org/std/slice/struct.ChunksExact.html "struct std::slice::ChunksExact")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-ChunksExactMut%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChunksExactMut](https://doc.rust-lang.org/std/slice/struct.ChunksExactMut.html "struct std::slice::ChunksExactMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-ChunksMut%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChunksMut](https://doc.rust-lang.org/std/slice/struct.ChunksMut.html "struct std::slice::ChunksMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-5)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[Iter](https://doc.rust-lang.org/std/slice/struct.Iter.html "struct std::slice::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-IterMut%3C'a,+T%3E-3)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[IterMut](https://doc.rust-lang.org/std/slice/struct.IterMut.html "struct std::slice::IterMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-RChunks%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RChunks](https://doc.rust-lang.org/std/slice/struct.RChunks.html "struct std::slice::RChunks")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-RChunksExact%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RChunksExact](https://doc.rust-lang.org/std/slice/struct.RChunksExact.html "struct std::slice::RChunksExact")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-RChunksExactMut%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RChunksExactMut](https://doc.rust-lang.org/std/slice/struct.RChunksExactMut.html "struct std::slice::RChunksExactMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-RChunksMut%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RChunksMut](https://doc.rust-lang.org/std/slice/struct.RChunksMut.html "struct std::slice::RChunksMut")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Windows%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Windows](https://doc.rust-lang.org/std/slice/struct.Windows.html "struct std::slice::Windows")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-6)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpmc::[Iter](https://doc.rust-lang.org/std/sync/mpmc/struct.Iter.html "struct std::sync::mpmc::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-TryIter%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpmc::[TryIter](https://doc.rust-lang.org/std/sync/mpmc/struct.TryIter.html "struct std::sync::mpmc::TryIter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Iter%3C'a,+T%3E-7)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[Iter](https://doc.rust-lang.org/std/sync/mpsc/struct.Iter.html "struct std::sync::mpsc::Iter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-TryIter%3C'a,+T%3E-1)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[TryIter](https://doc.rust-lang.org/std/sync/mpsc/struct.TryIter.html "struct std::sync::mpsc::TryIter")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-MappedMutexGuard%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[MappedMutexGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.MappedMutexGuard.html "struct std::sync::nonpoison::MappedMutexGuard")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-MutexGuard%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[MutexGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.MutexGuard.html "struct std::sync::nonpoison::MutexGuard")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-MappedMutexGuard%3C'a,+T%3E-1)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[MappedMutexGuard](https://doc.rust-lang.org/std/sync/struct.MappedMutexGuard.html "struct std::sync::MappedMutexGuard")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-MutexGuard%3C'a,+T%3E-1)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[MutexGuard](https://doc.rust-lang.org/std/sync/struct.MutexGuard.html "struct std::sync::MutexGuard")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-ReentrantLockGuard%3C'a,+T%3E)

### impl&lt;'a, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ReentrantLockGuard](https://doc.rust-lang.org/std/sync/struct.ReentrantLockGuard.html "struct std::sync::ReentrantLockGuard")&lt;'a, T&gt;

[§](#impl-UnsafeUnpin-for-Entry%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Entry](https://doc.rust-lang.org/std/collections/btree_set/enum.Entry.html "enum std::collections::btree_set::Entry")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::binary\_heap::[Drain](https://doc.rust-lang.org/std/collections/binary_heap/struct.Drain.html "struct std::collections::binary_heap::Drain")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-DrainSorted%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DrainSorted](https://doc.rust-lang.org/std/collections/binary_heap/struct.DrainSorted.html "struct std::collections::binary_heap::DrainSorted")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-PeekMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::binary\_heap::[PeekMut](https://doc.rust-lang.org/std/collections/binary_heap/struct.PeekMut.html "struct std::collections::binary_heap::PeekMut")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Difference%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Difference](https://doc.rust-lang.org/std/collections/btree_set/struct.Difference.html "struct std::collections::btree_set::Difference")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Intersection%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[Intersection](https://doc.rust-lang.org/std/collections/btree_set/struct.Intersection.html "struct std::collections::btree_set::Intersection")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedEntry%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[OccupiedEntry](https://doc.rust-lang.org/std/collections/btree_set/struct.OccupiedEntry.html "struct std::collections::btree_set::OccupiedEntry")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-VacantEntry%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[VacantEntry](https://doc.rust-lang.org/std/collections/btree_set/struct.VacantEntry.html "struct std::collections::btree_set::VacantEntry")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Cursor%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[Cursor](https://doc.rust-lang.org/std/collections/linked_list/struct.Cursor.html "struct std::collections::linked_list::Cursor")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-CursorMut%3C'a,+T,+A%3E)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[CursorMut](https://doc.rust-lang.org/std/collections/linked_list/struct.CursorMut.html "struct std::collections::linked_list::CursorMut")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a,+T,+A%3E-1)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[Drain](https://doc.rust-lang.org/std/collections/vec_deque/struct.Drain.html "struct std::collections::vec_deque::Drain")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-Drain%3C'a,+T,+A%3E-2)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::vec::[Drain](https://doc.rust-lang.org/std/vec/struct.Drain.html "struct std::vec::Drain")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-PeekMut%3C'a,+T,+A%3E-1)

### impl&lt;'a, T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::vec::[PeekMut](https://doc.rust-lang.org/std/vec/struct.PeekMut.html "struct std::vec::PeekMut")&lt;'a, T, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+T,+F,+A%3E)

### impl&lt;'a, T, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[ExtractIf](https://doc.rust-lang.org/std/collections/linked_list/struct.ExtractIf.html "struct std::collections::linked_list::ExtractIf")&lt;'a, T, F, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+T,+F,+A%3E-1)

### impl&lt;'a, T, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[ExtractIf](https://doc.rust-lang.org/std/collections/vec_deque/struct.ExtractIf.html "struct std::collections::vec_deque::ExtractIf")&lt;'a, T, F, A&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+T,+F,+A%3E-2)

### impl&lt;'a, T, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::vec::[ExtractIf](https://doc.rust-lang.org/std/vec/struct.ExtractIf.html "struct std::vec::ExtractIf")&lt;'a, T, F, A&gt;

[§](#impl-UnsafeUnpin-for-ChunkBy%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChunkBy](https://doc.rust-lang.org/std/slice/struct.ChunkBy.html "struct std::slice::ChunkBy")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-ChunkByMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ChunkByMut](https://doc.rust-lang.org/std/slice/struct.ChunkByMut.html "struct std::slice::ChunkByMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-RSplit%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[RSplit](https://doc.rust-lang.org/std/slice/struct.RSplit.html "struct std::slice::RSplit")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-RSplitMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RSplitMut](https://doc.rust-lang.org/std/slice/struct.RSplitMut.html "struct std::slice::RSplitMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-RSplitN%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[RSplitN](https://doc.rust-lang.org/std/slice/struct.RSplitN.html "struct std::slice::RSplitN")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-RSplitNMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RSplitNMut](https://doc.rust-lang.org/std/slice/struct.RSplitNMut.html "struct std::slice::RSplitNMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-Split%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[Split](https://doc.rust-lang.org/std/slice/struct.Split.html "struct std::slice::Split")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-SplitInclusive%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[SplitInclusive](https://doc.rust-lang.org/std/slice/struct.SplitInclusive.html "struct std::slice::SplitInclusive")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-SplitInclusiveMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitInclusiveMut](https://doc.rust-lang.org/std/slice/struct.SplitInclusiveMut.html "struct std::slice::SplitInclusiveMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-SplitMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitMut](https://doc.rust-lang.org/std/slice/struct.SplitMut.html "struct std::slice::SplitMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-SplitN%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::slice::[SplitN](https://doc.rust-lang.org/std/slice/struct.SplitN.html "struct std::slice::SplitN")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-SplitNMut%3C'a,+T,+P%3E)

### impl&lt;'a, T, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SplitNMut](https://doc.rust-lang.org/std/slice/struct.SplitNMut.html "struct std::slice::SplitNMut")&lt;'a, T, P&gt;

[§](#impl-UnsafeUnpin-for-ExtractIf%3C'a,+T,+R,+F,+A%3E)

### impl&lt;'a, T, R, F, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[ExtractIf](https://doc.rust-lang.org/std/collections/btree_set/struct.ExtractIf.html "struct std::collections::btree_set::ExtractIf")&lt;'a, T, R, F, A&gt;

[§](#impl-UnsafeUnpin-for-Entry%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Entry](https://doc.rust-lang.org/std/collections/hash_set/enum.Entry.html "enum std::collections::hash_set::Entry")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-Difference%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Difference](https://doc.rust-lang.org/std/collections/hash_set/struct.Difference.html "struct std::collections::hash_set::Difference")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-Intersection%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Intersection](https://doc.rust-lang.org/std/collections/hash_set/struct.Intersection.html "struct std::collections::hash_set::Intersection")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-OccupiedEntry%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[OccupiedEntry](https://doc.rust-lang.org/std/collections/hash_set/struct.OccupiedEntry.html "struct std::collections::hash_set::OccupiedEntry")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-SymmetricDifference%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[SymmetricDifference](https://doc.rust-lang.org/std/collections/hash_set/struct.SymmetricDifference.html "struct std::collections::hash_set::SymmetricDifference")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-Union%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[Union](https://doc.rust-lang.org/std/collections/hash_set/struct.Union.html "struct std::collections::hash_set::Union")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-VacantEntry%3C'a,+T,+S,+A%3E)

### impl&lt;'a, T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[VacantEntry](https://doc.rust-lang.org/std/collections/hash_set/struct.VacantEntry.html "struct std::collections::hash_set::VacantEntry")&lt;'a, T, S, A&gt;

[§](#impl-UnsafeUnpin-for-ArrayWindows%3C'a,+T,+N%3E)

### impl&lt;'a, T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ArrayWindows](https://doc.rust-lang.org/std/slice/struct.ArrayWindows.html "struct std::slice::ArrayWindows")&lt;'a, T, N&gt;

[§](#impl-UnsafeUnpin-for-CharArraySearcher%3C'a,+N%3E)

### impl&lt;'a, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharArraySearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArraySearcher.html "struct std::str::pattern::CharArraySearcher")&lt;'a, N&gt;

[§](#impl-UnsafeUnpin-for-Ref%3C'b,+T%3E)

### impl&lt;'b, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ref](https://doc.rust-lang.org/std/cell/struct.Ref.html "struct std::cell::Ref")&lt;'b, T&gt;

[§](#impl-UnsafeUnpin-for-RefMut%3C'b,+T%3E)

### impl&lt;'b, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RefMut](https://doc.rust-lang.org/std/cell/struct.RefMut.html "struct std::cell::RefMut")&lt;'b, T&gt;

[§](#impl-UnsafeUnpin-for-BorrowedBuf%3C'data%3E)

### impl&lt;'data&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowedBuf](https://doc.rust-lang.org/std/io/struct.BorrowedBuf.html "struct std::io::BorrowedBuf")&lt;'data&gt;

[§](#impl-UnsafeUnpin-for-BorrowedFd%3C'fd%3E)

### impl&lt;'fd&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowedFd](https://doc.rust-lang.org/std/os/fd/struct.BorrowedFd.html "struct std::os::fd::BorrowedFd")&lt;'fd&gt;

[§](#impl-UnsafeUnpin-for-BorrowedHandle%3C'handle%3E)

### impl&lt;'handle&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowedHandle](https://doc.rust-lang.org/std/os/windows/io/struct.BorrowedHandle.html "struct std::os::windows::io::BorrowedHandle")&lt;'handle&gt;

[§](#impl-UnsafeUnpin-for-MappedRwLockReadGuard%3C'rwlock,+T%3E)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[MappedRwLockReadGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.MappedRwLockReadGuard.html "struct std::sync::nonpoison::MappedRwLockReadGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-MappedRwLockWriteGuard%3C'rwlock,+T%3E)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[MappedRwLockWriteGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.MappedRwLockWriteGuard.html "struct std::sync::nonpoison::MappedRwLockWriteGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-RwLockReadGuard%3C'rwlock,+T%3E)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[RwLockReadGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.RwLockReadGuard.html "struct std::sync::nonpoison::RwLockReadGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-RwLockWriteGuard%3C'rwlock,+T%3E)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[RwLockWriteGuard](https://doc.rust-lang.org/std/sync/nonpoison/struct.RwLockWriteGuard.html "struct std::sync::nonpoison::RwLockWriteGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-MappedRwLockReadGuard%3C'rwlock,+T%3E-1)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[MappedRwLockReadGuard](https://doc.rust-lang.org/std/sync/struct.MappedRwLockReadGuard.html "struct std::sync::MappedRwLockReadGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-MappedRwLockWriteGuard%3C'rwlock,+T%3E-1)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[MappedRwLockWriteGuard](https://doc.rust-lang.org/std/sync/struct.MappedRwLockWriteGuard.html "struct std::sync::MappedRwLockWriteGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-RwLockReadGuard%3C'rwlock,+T%3E-1)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[RwLockReadGuard](https://doc.rust-lang.org/std/sync/struct.RwLockReadGuard.html "struct std::sync::RwLockReadGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-RwLockWriteGuard%3C'rwlock,+T%3E-1)

### impl&lt;'rwlock, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[RwLockWriteGuard](https://doc.rust-lang.org/std/sync/struct.RwLockWriteGuard.html "struct std::sync::RwLockWriteGuard")&lt;'rwlock, T&gt;

[§](#impl-UnsafeUnpin-for-Scope%3C'scope,+'env%3E)

### impl&lt;'scope, 'env&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Scope](https://doc.rust-lang.org/std/thread/struct.Scope.html "struct std::thread::Scope")&lt;'scope, 'env&gt;

[§](#impl-UnsafeUnpin-for-ScopedJoinHandle%3C'scope,+T%3E)

### impl&lt;'scope, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ScopedJoinHandle](https://doc.rust-lang.org/std/thread/struct.ScopedJoinHandle.html "struct std::thread::ScopedJoinHandle")&lt;'scope, T&gt;

[§](#impl-UnsafeUnpin-for-BorrowedSocket%3C'socket%3E)

### impl&lt;'socket&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BorrowedSocket](https://doc.rust-lang.org/std/os/windows/io/struct.BorrowedSocket.html "struct std::os::windows::io::BorrowedSocket")&lt;'socket&gt;

[§](#impl-UnsafeUnpin-for-Repeat%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[Repeat](https://doc.rust-lang.org/std/iter/struct.Repeat.html "struct std::iter::Repeat")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-RepeatN%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RepeatN](https://doc.rust-lang.org/std/iter/struct.RepeatN.html "struct std::iter::RepeatN")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::option::[IntoIter](https://doc.rust-lang.org/std/option/struct.IntoIter.html "struct std::option::IntoIter")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-OptionFlatten%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OptionFlatten](https://doc.rust-lang.org/std/option/struct.OptionFlatten.html "struct std::option::OptionFlatten")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-RangeFromIter%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeFromIter](https://doc.rust-lang.org/std/range/struct.RangeFromIter.html "struct std::range::RangeFromIter")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-RangeInclusiveIter%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeInclusiveIter](https://doc.rust-lang.org/std/range/struct.RangeInclusiveIter.html "struct std::range::RangeInclusiveIter")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-RangeIter%3CA%3E)

### impl&lt;A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeIter](https://doc.rust-lang.org/std/range/struct.RangeIter.html "struct std::range::RangeIter")&lt;A&gt;

[§](#impl-UnsafeUnpin-for-Chain%3CA,+B%3E)

### impl&lt;A, B&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[Chain](https://doc.rust-lang.org/std/iter/struct.Chain.html "struct std::iter::Chain")&lt;A, B&gt;

[§](#impl-UnsafeUnpin-for-Zip%3CA,+B%3E)

### impl&lt;A, B&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Zip](https://doc.rust-lang.org/std/iter/struct.Zip.html "struct std::iter::Zip")&lt;A, B&gt;

[§](#impl-UnsafeUnpin-for-Lines%3CB%3E)

### impl&lt;B&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Lines](https://doc.rust-lang.org/std/io/struct.Lines.html "struct std::io::Lines")&lt;B&gt;

[§](#impl-UnsafeUnpin-for-Split%3CB%3E)

### impl&lt;B&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Split](https://doc.rust-lang.org/std/io/struct.Split.html "struct std::io::Split")&lt;B&gt;

[§](#impl-UnsafeUnpin-for-ControlFlow%3CB,+C%3E)

### impl&lt;B, C&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ControlFlow](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html "enum std::ops::ControlFlow")&lt;B, C&gt;

[§](#impl-UnsafeUnpin-for-Report%3CE%3E)

### impl&lt;E&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Report](https://doc.rust-lang.org/std/error/struct.Report.html "struct std::error::Report")&lt;E&gt;

[§](#impl-UnsafeUnpin-for-FromFn%3CF%3E)

### impl&lt;F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::fmt::[FromFn](https://doc.rust-lang.org/std/fmt/struct.FromFn.html "struct std::fmt::FromFn")&lt;F&gt;

[§](#impl-UnsafeUnpin-for-PollFn%3CF%3E)

### impl&lt;F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PollFn](https://doc.rust-lang.org/std/future/struct.PollFn.html "struct std::future::PollFn")&lt;F&gt;

[§](#impl-UnsafeUnpin-for-FromFn%3CF%3E-1)

### impl&lt;F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[FromFn](https://doc.rust-lang.org/std/iter/struct.FromFn.html "struct std::iter::FromFn")&lt;F&gt;

[§](#impl-UnsafeUnpin-for-OnceWith%3CF%3E)

### impl&lt;F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OnceWith](https://doc.rust-lang.org/std/iter/struct.OnceWith.html "struct std::iter::OnceWith")&lt;F&gt;

[§](#impl-UnsafeUnpin-for-RepeatWith%3CF%3E)

### impl&lt;F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RepeatWith](https://doc.rust-lang.org/std/iter/struct.RepeatWith.html "struct std::iter::RepeatWith")&lt;F&gt;

[§](#impl-UnsafeUnpin-for-FromCoroutine%3CG%3E)

### impl&lt;G&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromCoroutine](https://doc.rust-lang.org/std/iter/struct.FromCoroutine.html "struct std::iter::FromCoroutine")&lt;G&gt;

[§](#impl-UnsafeUnpin-for-BuildHasherDefault%3CH%3E)

### impl&lt;H&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BuildHasherDefault](https://doc.rust-lang.org/std/hash/struct.BuildHasherDefault.html "struct std::hash::BuildHasherDefault")&lt;H&gt;

[§](#impl-UnsafeUnpin-for-FromIter%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FromIter](https://doc.rust-lang.org/std/async_iter/struct.FromIter.html "struct std::async_iter::FromIter")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-DecodeUtf16%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DecodeUtf16](https://doc.rust-lang.org/std/char/struct.DecodeUtf16.html "struct std::char::DecodeUtf16")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Cloned%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Cloned](https://doc.rust-lang.org/std/iter/struct.Cloned.html "struct std::iter::Cloned")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Copied%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Copied](https://doc.rust-lang.org/std/iter/struct.Copied.html "struct std::iter::Copied")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Cycle%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Cycle](https://doc.rust-lang.org/std/iter/struct.Cycle.html "struct std::iter::Cycle")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Enumerate%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Enumerate](https://doc.rust-lang.org/std/iter/struct.Enumerate.html "struct std::iter::Enumerate")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Flatten%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Flatten](https://doc.rust-lang.org/std/iter/struct.Flatten.html "struct std::iter::Flatten")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Fuse%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Fuse](https://doc.rust-lang.org/std/iter/struct.Fuse.html "struct std::iter::Fuse")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Intersperse%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Intersperse](https://doc.rust-lang.org/std/iter/struct.Intersperse.html "struct std::iter::Intersperse")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Peekable%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Peekable](https://doc.rust-lang.org/std/iter/struct.Peekable.html "struct std::iter::Peekable")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Skip%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Skip](https://doc.rust-lang.org/std/iter/struct.Skip.html "struct std::iter::Skip")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-StepBy%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StepBy](https://doc.rust-lang.org/std/iter/struct.StepBy.html "struct std::iter::StepBy")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-Take%3CI%3E)

### impl&lt;I&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[Take](https://doc.rust-lang.org/std/iter/struct.Take.html "struct std::iter::Take")&lt;I&gt;

[§](#impl-UnsafeUnpin-for-FilterMap%3CI,+F%3E)

### impl&lt;I, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FilterMap](https://doc.rust-lang.org/std/iter/struct.FilterMap.html "struct std::iter::FilterMap")&lt;I, F&gt;

[§](#impl-UnsafeUnpin-for-Inspect%3CI,+F%3E)

### impl&lt;I, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Inspect](https://doc.rust-lang.org/std/iter/struct.Inspect.html "struct std::iter::Inspect")&lt;I, F&gt;

[§](#impl-UnsafeUnpin-for-Map%3CI,+F%3E)

### impl&lt;I, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Map](https://doc.rust-lang.org/std/iter/struct.Map.html "struct std::iter::Map")&lt;I, F&gt;

[§](#impl-UnsafeUnpin-for-MapWindows%3CI,+F,+N%3E)

### impl&lt;I, F, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [MapWindows](https://doc.rust-lang.org/std/iter/struct.MapWindows.html "struct std::iter::MapWindows")&lt;I, F, N&gt;

[§](#impl-UnsafeUnpin-for-IntersperseWith%3CI,+G%3E)

### impl&lt;I, G&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntersperseWith](https://doc.rust-lang.org/std/iter/struct.IntersperseWith.html "struct std::iter::IntersperseWith")&lt;I, G&gt;

[§](#impl-UnsafeUnpin-for-Filter%3CI,+P%3E)

### impl&lt;I, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Filter](https://doc.rust-lang.org/std/iter/struct.Filter.html "struct std::iter::Filter")&lt;I, P&gt;

[§](#impl-UnsafeUnpin-for-MapWhile%3CI,+P%3E)

### impl&lt;I, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [MapWhile](https://doc.rust-lang.org/std/iter/struct.MapWhile.html "struct std::iter::MapWhile")&lt;I, P&gt;

[§](#impl-UnsafeUnpin-for-SkipWhile%3CI,+P%3E)

### impl&lt;I, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SkipWhile](https://doc.rust-lang.org/std/iter/struct.SkipWhile.html "struct std::iter::SkipWhile")&lt;I, P&gt;

[§](#impl-UnsafeUnpin-for-TakeWhile%3CI,+P%3E)

### impl&lt;I, P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TakeWhile](https://doc.rust-lang.org/std/iter/struct.TakeWhile.html "struct std::iter::TakeWhile")&lt;I, P&gt;

[§](#impl-UnsafeUnpin-for-Scan%3CI,+St,+F%3E)

### impl&lt;I, St, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Scan](https://doc.rust-lang.org/std/iter/struct.Scan.html "struct std::iter::Scan")&lt;I, St, F&gt;

[§](#impl-UnsafeUnpin-for-FlatMap%3CI,+U,+F%3E)

### impl&lt;I, U, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [FlatMap](https://doc.rust-lang.org/std/iter/struct.FlatMap.html "struct std::iter::FlatMap")&lt;I, U, F&gt;

[§](#impl-UnsafeUnpin-for-ArrayChunks%3CI,+N%3E)

### impl&lt;I, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ArrayChunks](https://doc.rust-lang.org/std/iter/struct.ArrayChunks.html "struct std::iter::ArrayChunks")&lt;I, N&gt;

[§](#impl-UnsafeUnpin-for-Range%3CIdx%3E)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ops::[Range](https://doc.rust-lang.org/std/ops/struct.Range.html "struct std::ops::Range")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeFrom%3CIdx%3E)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ops::[RangeFrom](https://doc.rust-lang.org/std/ops/struct.RangeFrom.html "struct std::ops::RangeFrom")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeInclusive%3CIdx%3E)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ops::[RangeInclusive](https://doc.rust-lang.org/std/ops/struct.RangeInclusive.html "struct std::ops::RangeInclusive")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeTo%3CIdx%3E)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RangeTo](https://doc.rust-lang.org/std/ops/struct.RangeTo.html "struct std::ops::RangeTo")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeToInclusive%3CIdx%3E)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::ops::[RangeToInclusive](https://doc.rust-lang.org/std/ops/struct.RangeToInclusive.html "struct std::ops::RangeToInclusive")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-Range%3CIdx%3E-1)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::range::[Range](https://doc.rust-lang.org/std/range/struct.Range.html "struct std::range::Range")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeFrom%3CIdx%3E-1)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::range::[RangeFrom](https://doc.rust-lang.org/std/range/struct.RangeFrom.html "struct std::range::RangeFrom")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeInclusive%3CIdx%3E-1)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::range::[RangeInclusive](https://doc.rust-lang.org/std/range/struct.RangeInclusive.html "struct std::range::RangeInclusive")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-RangeToInclusive%3CIdx%3E-1)

### impl&lt;Idx&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::range::[RangeToInclusive](https://doc.rust-lang.org/std/range/struct.RangeToInclusive.html "struct std::range::RangeToInclusive")&lt;Idx&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CK,+A%3E)

### impl&lt;K, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_set::[IntoIter](https://doc.rust-lang.org/std/collections/hash_set/struct.IntoIter.html "struct std::collections::hash_set::IntoIter")&lt;K, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CK,+V,+A%3E)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[IntoIter](https://doc.rust-lang.org/std/collections/btree_map/struct.IntoIter.html "struct std::collections::btree_map::IntoIter")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-IntoKeys%3CK,+V,+A%3E)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[IntoKeys](https://doc.rust-lang.org/std/collections/btree_map/struct.IntoKeys.html "struct std::collections::btree_map::IntoKeys")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-IntoValues%3CK,+V,+A%3E)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_map::[IntoValues](https://doc.rust-lang.org/std/collections/btree_map/struct.IntoValues.html "struct std::collections::btree_map::IntoValues")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CK,+V,+A%3E-1)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[IntoIter](https://doc.rust-lang.org/std/collections/hash_map/struct.IntoIter.html "struct std::collections::hash_map::IntoIter")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-IntoKeys%3CK,+V,+A%3E-1)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[IntoKeys](https://doc.rust-lang.org/std/collections/hash_map/struct.IntoKeys.html "struct std::collections::hash_map::IntoKeys")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-IntoValues%3CK,+V,+A%3E-1)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::hash\_map::[IntoValues](https://doc.rust-lang.org/std/collections/hash_map/struct.IntoValues.html "struct std::collections::hash_map::IntoValues")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-BTreeMap%3CK,+V,+A%3E)

### impl&lt;K, V, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BTreeMap](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html "struct std::collections::BTreeMap")&lt;K, V, A&gt;

[§](#impl-UnsafeUnpin-for-HashMap%3CK,+V,+S,+A%3E)

### impl&lt;K, V, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html "struct std::collections::HashMap")&lt;K, V, S, A&gt;

[§](#impl-UnsafeUnpin-for-MaybeDangling%3CP%3E)

### impl&lt;P&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [MaybeDangling](https://doc.rust-lang.org/std/mem/struct.MaybeDangling.html "struct std::mem::MaybeDangling")&lt;P&gt;

[§](#impl-UnsafeUnpin-for-Pin%3CPtr%3E)

### impl&lt;Ptr&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Pin](https://doc.rust-lang.org/std/pin/struct.Pin.html "struct std::pin::Pin")&lt;Ptr&gt;

[§](#impl-UnsafeUnpin-for-BufReader%3CR%3E)

### impl&lt;R&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BufReader](https://doc.rust-lang.org/std/io/struct.BufReader.html "struct std::io::BufReader")&lt;R&gt;

[§](#impl-UnsafeUnpin-for-Bytes%3CR%3E)

### impl&lt;R&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Bytes](https://doc.rust-lang.org/std/io/struct.Bytes.html "struct std::io::Bytes")&lt;R&gt;

[§](#impl-UnsafeUnpin-for-fn%28T%29+-%3E+Ret)

### impl&lt;Ret, T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [fn(T₁, T₂, …, Tₙ)](https://doc.rust-lang.org/std/primitive.tuple.html#trait-implementations-1) -&gt; Ret

[§](#impl-UnsafeUnpin-for-Bound%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Bound](https://doc.rust-lang.org/std/ops/enum.Bound.html "enum std::ops::Bound")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Option%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-TryLockError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[TryLockError](https://doc.rust-lang.org/std/sync/enum.TryLockError.html "enum std::sync::TryLockError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-SendTimeoutError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SendTimeoutError](https://doc.rust-lang.org/std/sync/mpmc/enum.SendTimeoutError.html "enum std::sync::mpmc::SendTimeoutError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-TrySendError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [TrySendError](https://doc.rust-lang.org/std/sync/mpsc/enum.TrySendError.html "enum std::sync::mpsc::TrySendError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-RecvTimeoutError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::oneshot::[RecvTimeoutError](https://doc.rust-lang.org/std/sync/oneshot/enum.RecvTimeoutError.html "enum std::sync::oneshot::RecvTimeoutError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-TryRecvError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::oneshot::[TryRecvError](https://doc.rust-lang.org/std/sync/oneshot/enum.TryRecvError.html "enum std::sync::oneshot::TryRecvError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Poll%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Poll](https://doc.rust-lang.org/std/task/enum.Poll.html "enum std::task::Poll")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-%5BT%5D)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [\[T\]](https://doc.rust-lang.org/std/primitive.slice.html)

[§](#impl-UnsafeUnpin-for-%28T,%29)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [(T₁, T₂, …, Tₙ)](https://doc.rust-lang.org/std/primitive.tuple.html#trait-implementations-1)

[§](#impl-UnsafeUnpin-for-ThinBox%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ThinBox](https://doc.rust-lang.org/std/boxed/struct.ThinBox.html "struct std::boxed::ThinBox")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Cell%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Cell](https://doc.rust-lang.org/std/cell/struct.Cell.html "struct std::cell::Cell")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-OnceCell%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OnceCell](https://doc.rust-lang.org/std/cell/struct.OnceCell.html "struct std::cell::OnceCell")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-RefCell%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [RefCell](https://doc.rust-lang.org/std/cell/struct.RefCell.html "struct std::cell::RefCell")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-SyncUnsafeCell%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SyncUnsafeCell](https://doc.rust-lang.org/std/cell/struct.SyncUnsafeCell.html "struct std::cell::SyncUnsafeCell")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-UnsafeCell%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UnsafeCell](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html "struct std::cell::UnsafeCell")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Reverse%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Reverse](https://doc.rust-lang.org/std/cmp/struct.Reverse.html "struct std::cmp::Reverse")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Pending%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Pending](https://doc.rust-lang.org/std/future/struct.Pending.html "struct std::future::Pending")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Ready%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Ready](https://doc.rust-lang.org/std/future/struct.Ready.html "struct std::future::Ready")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Cursor%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Cursor](https://doc.rust-lang.org/std/io/struct.Cursor.html "struct std::io::Cursor")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Take%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Take](https://doc.rust-lang.org/std/io/struct.Take.html "struct std::io::Take")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Empty%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[Empty](https://doc.rust-lang.org/std/iter/struct.Empty.html "struct std::iter::Empty")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Once%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::iter::[Once](https://doc.rust-lang.org/std/iter/struct.Once.html "struct std::iter::Once")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Rev%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Rev](https://doc.rust-lang.org/std/iter/struct.Rev.html "struct std::iter::Rev")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Discriminant%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Discriminant](https://doc.rust-lang.org/std/mem/struct.Discriminant.html "struct std::mem::Discriminant")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-ManuallyDrop%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ManuallyDrop](https://doc.rust-lang.org/std/mem/struct.ManuallyDrop.html "struct std::mem::ManuallyDrop")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-NonZero%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [NonZero](https://doc.rust-lang.org/std/num/struct.NonZero.html "struct std::num::NonZero")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Saturating%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Saturating](https://doc.rust-lang.org/std/num/struct.Saturating.html "struct std::num::Saturating")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Wrapping%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Wrapping](https://doc.rust-lang.org/std/num/struct.Wrapping.html "struct std::num::Wrapping")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Yeet%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Yeet](https://doc.rust-lang.org/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-AssertUnwindSafe%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AssertUnwindSafe](https://doc.rust-lang.org/std/panic/struct.AssertUnwindSafe.html "struct std::panic::AssertUnwindSafe")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-NonNull%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [NonNull](https://doc.rust-lang.org/std/ptr/struct.NonNull.html "struct std::ptr::NonNull")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::result::[IntoIter](https://doc.rust-lang.org/std/result/struct.IntoIter.html "struct std::result::IntoIter")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-AtomicPtr%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [AtomicPtr](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicPtr.html "struct std::sync::atomic::AtomicPtr")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT%3E-1)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpmc::[IntoIter](https://doc.rust-lang.org/std/sync/mpmc/struct.IntoIter.html "struct std::sync::mpmc::IntoIter")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Receiver%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpmc::[Receiver](https://doc.rust-lang.org/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Sender%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpmc::[Sender](https://doc.rust-lang.org/std/sync/mpmc/struct.Sender.html "struct std::sync::mpmc::Sender")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT%3E-2)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[IntoIter](https://doc.rust-lang.org/std/sync/mpsc/struct.IntoIter.html "struct std::sync::mpsc::IntoIter")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Receiver%3CT%3E-1)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[Receiver](https://doc.rust-lang.org/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-SendError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SendError](https://doc.rust-lang.org/std/sync/mpsc/struct.SendError.html "struct std::sync::mpsc::SendError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Sender%3CT%3E-1)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::mpsc::[Sender](https://doc.rust-lang.org/std/sync/mpsc/struct.Sender.html "struct std::sync::mpsc::Sender")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-SyncSender%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [SyncSender](https://doc.rust-lang.org/std/sync/mpsc/struct.SyncSender.html "struct std::sync::mpsc::SyncSender")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Mutex%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[Mutex](https://doc.rust-lang.org/std/sync/nonpoison/struct.Mutex.html "struct std::sync::nonpoison::Mutex")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-RwLock%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::nonpoison::[RwLock](https://doc.rust-lang.org/std/sync/nonpoison/struct.RwLock.html "struct std::sync::nonpoison::RwLock")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Receiver%3CT%3E-2)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::oneshot::[Receiver](https://doc.rust-lang.org/std/sync/oneshot/struct.Receiver.html "struct std::sync::oneshot::Receiver")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Sender%3CT%3E-2)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::oneshot::[Sender](https://doc.rust-lang.org/std/sync/oneshot/struct.Sender.html "struct std::sync::oneshot::Sender")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Exclusive%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Exclusive](https://doc.rust-lang.org/std/sync/struct.Exclusive.html "struct std::sync::Exclusive")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Mutex%3CT%3E-1)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[Mutex](https://doc.rust-lang.org/std/sync/struct.Mutex.html "struct std::sync::Mutex")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-OnceLock%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [OnceLock](https://doc.rust-lang.org/std/sync/struct.OnceLock.html "struct std::sync::OnceLock")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-PoisonError%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PoisonError](https://doc.rust-lang.org/std/sync/struct.PoisonError.html "struct std::sync::PoisonError")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-ReentrantLock%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [ReentrantLock](https://doc.rust-lang.org/std/sync/struct.ReentrantLock.html "struct std::sync::ReentrantLock")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-RwLock%3CT%3E-1)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[RwLock](https://doc.rust-lang.org/std/sync/struct.RwLock.html "struct std::sync::RwLock")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-JoinHandle%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [JoinHandle](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html "struct std::thread::JoinHandle")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-LocalKey%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LocalKey](https://doc.rust-lang.org/std/thread/struct.LocalKey.html "struct std::thread::LocalKey")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-PhantomContravariant%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomContravariant](https://doc.rust-lang.org/std/marker/struct.PhantomContravariant.html "struct std::marker::PhantomContravariant")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-PhantomCovariant%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomCovariant](https://doc.rust-lang.org/std/marker/struct.PhantomCovariant.html "struct std::marker::PhantomCovariant")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-PhantomInvariant%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [PhantomInvariant](https://doc.rust-lang.org/std/marker/struct.PhantomInvariant.html "struct std::marker::PhantomInvariant")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-MaybeUninit%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [MaybeUninit](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit")&lt;T&gt;

[§](#impl-UnsafeUnpin-for-Box%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Box](https://doc.rust-lang.org/std/boxed/struct.Box.html "struct std::boxed::Box")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::binary\_heap::[IntoIter](https://doc.rust-lang.org/std/collections/binary_heap/struct.IntoIter.html "struct std::collections::binary_heap::IntoIter")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIterSorted%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntoIterSorted](https://doc.rust-lang.org/std/collections/binary_heap/struct.IntoIterSorted.html "struct std::collections::binary_heap::IntoIterSorted")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+A%3E-1)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::btree\_set::[IntoIter](https://doc.rust-lang.org/std/collections/btree_set/struct.IntoIter.html "struct std::collections::btree_set::IntoIter")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+A%3E-2)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::linked\_list::[IntoIter](https://doc.rust-lang.org/std/collections/linked_list/struct.IntoIter.html "struct std::collections::linked_list::IntoIter")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-BTreeSet%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BTreeSet](https://doc.rust-lang.org/std/collections/struct.BTreeSet.html "struct std::collections::BTreeSet")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-BinaryHeap%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BinaryHeap](https://doc.rust-lang.org/std/collections/struct.BinaryHeap.html "struct std::collections::BinaryHeap")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-LinkedList%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LinkedList](https://doc.rust-lang.org/std/collections/struct.LinkedList.html "struct std::collections::LinkedList")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-VecDeque%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [VecDeque](https://doc.rust-lang.org/std/collections/struct.VecDeque.html "struct std::collections::VecDeque")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+A%3E-3)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::collections::vec\_deque::[IntoIter](https://doc.rust-lang.org/std/collections/vec_deque/struct.IntoIter.html "struct std::collections::vec_deque::IntoIter")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Rc%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Rc](https://doc.rust-lang.org/std/rc/struct.Rc.html "struct std::rc::Rc")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-UniqueRc%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UniqueRc](https://doc.rust-lang.org/std/rc/struct.UniqueRc.html "struct std::rc::UniqueRc")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Weak%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::rc::[Weak](https://doc.rust-lang.org/std/rc/struct.Weak.html "struct std::rc::Weak")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Arc%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html "struct std::sync::Arc")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-UniqueArc%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [UniqueArc](https://doc.rust-lang.org/std/sync/struct.UniqueArc.html "struct std::sync::UniqueArc")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Weak%3CT,+A%3E-1)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::sync::[Weak](https://doc.rust-lang.org/std/sync/struct.Weak.html "struct std::sync::Weak")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+A%3E-4)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::vec::[IntoIter](https://doc.rust-lang.org/std/vec/struct.IntoIter.html "struct std::vec::IntoIter")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Vec%3CT,+A%3E)

### impl&lt;T, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec")&lt;T, A&gt;

[§](#impl-UnsafeUnpin-for-Result%3CT,+E%3E)

### impl&lt;T, E&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Result](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result")&lt;T, E&gt;

[§](#impl-UnsafeUnpin-for-LazyCell%3CT,+F%3E)

### impl&lt;T, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LazyCell](https://doc.rust-lang.org/std/cell/struct.LazyCell.html "struct std::cell::LazyCell")&lt;T, F&gt;

[§](#impl-UnsafeUnpin-for-Successors%3CT,+F%3E)

### impl&lt;T, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Successors](https://doc.rust-lang.org/std/iter/struct.Successors.html "struct std::iter::Successors")&lt;T, F&gt;

[§](#impl-UnsafeUnpin-for-DropGuard%3CT,+F%3E)

### impl&lt;T, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [DropGuard](https://doc.rust-lang.org/std/mem/struct.DropGuard.html "struct std::mem::DropGuard")&lt;T, F&gt;

[§](#impl-UnsafeUnpin-for-LazyLock%3CT,+F%3E)

### impl&lt;T, F&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LazyLock](https://doc.rust-lang.org/std/sync/struct.LazyLock.html "struct std::sync::LazyLock")&lt;T, F&gt;

[§](#impl-UnsafeUnpin-for-HashSet%3CT,+S,+A%3E)

### impl&lt;T, S, A&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [HashSet](https://doc.rust-lang.org/std/collections/struct.HashSet.html "struct std::collections::HashSet")&lt;T, S, A&gt;

[§](#impl-UnsafeUnpin-for-Chain%3CT,+U%3E)

### impl&lt;T, U&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::io::[Chain](https://doc.rust-lang.org/std/io/struct.Chain.html "struct std::io::Chain")&lt;T, U&gt;

[§](#impl-UnsafeUnpin-for-%5BT;+N%5D)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [\[T; N\]](https://doc.rust-lang.org/std/primitive.array.html)

[§](#impl-UnsafeUnpin-for-IntoIter%3CT,+N%3E)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for std::array::[IntoIter](https://doc.rust-lang.org/std/array/struct.IntoIter.html "struct std::array::IntoIter")&lt;T, N&gt;

[§](#impl-UnsafeUnpin-for-Mask%3CT,+N%3E)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Mask](https://doc.rust-lang.org/std/simd/struct.Mask.html "struct std::simd::Mask")&lt;T, N&gt;

[§](#impl-UnsafeUnpin-for-Simd%3CT,+N%3E)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Simd](https://doc.rust-lang.org/std/simd/struct.Simd.html "struct std::simd::Simd")&lt;T, N&gt;

[§](#impl-UnsafeUnpin-for-%5BOption%3CT%3E;+N%5D)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for \[[Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;T&gt;; [N](https://doc.rust-lang.org/std/primitive.array.html)]

[§](#impl-UnsafeUnpin-for-%5BMaybeUninit%3CT%3E;+N%5D)

### impl&lt;T, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for \[[MaybeUninit](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit")&lt;T&gt;; [N](https://doc.rust-lang.org/std/primitive.array.html)]

[§](#impl-UnsafeUnpin-for-BufWriter%3CW%3E)

### impl&lt;W&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [BufWriter](https://doc.rust-lang.org/std/io/struct.BufWriter.html "struct std::io::BufWriter")&lt;W&gt;

[§](#impl-UnsafeUnpin-for-IntoInnerError%3CW%3E)

### impl&lt;W&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [IntoInnerError](https://doc.rust-lang.org/std/io/struct.IntoInnerError.html "struct std::io::IntoInnerError")&lt;W&gt;

[§](#impl-UnsafeUnpin-for-LineWriter%3CW%3E)

### impl&lt;W&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [LineWriter](https://doc.rust-lang.org/std/io/struct.LineWriter.html "struct std::io::LineWriter")&lt;W&gt;

[§](#impl-UnsafeUnpin-for-CoroutineState%3CY,+R%3E)

### impl&lt;Y, R&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CoroutineState](https://doc.rust-lang.org/std/ops/enum.CoroutineState.html "enum std::ops::CoroutineState")&lt;Y, R&gt;

[§](#impl-UnsafeUnpin-for-%5Bu8;+N%5D)

### impl&lt;const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for \[[u8](https://doc.rust-lang.org/std/primitive.u8.html); [N](https://doc.rust-lang.org/std/primitive.array.html)]