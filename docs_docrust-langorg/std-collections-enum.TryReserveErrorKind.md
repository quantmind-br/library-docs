---
title: TryReserveErrorKind in std::collections - Rust
url: https://doc.rust-lang.org/std/collections/enum.TryReserveErrorKind.html
source: crawler
fetched_at: 2026-05-06T21:24:54.216048893-03:00
rendered_js: false
word_count: 81
summary: Defines the error variants for allocation reservation failures, including capacity overflow and memory allocator errors within the Rust standard library.
tags:
    - rust
    - memory-allocation
    - error-handling
    - api-reference
    - experimental-api
category: reference
---

## Enum TryReserveErrorKind

[Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#101)

```rust
pub enum TryReserveErrorKind {
    CapacityOverflow,
    AllocError {
        layout: Layout,
        /* private fields */
    },
}
```

🔬This is a nightly-only experimental API. (`try_reserve_kind` [#48043](https://github.com/rust-lang/rust/issues/48043))

Expand description

Details of the allocation that caused a `TryReserveError`

[§](#variant.CapacityOverflow)

🔬This is a nightly-only experimental API. (`try_reserve_kind` [#48043](https://github.com/rust-lang/rust/issues/48043))

Error due to the computed capacity exceeding the collection’s maximum (usually `isize::MAX` bytes).

[§](#variant.AllocError)

🔬This is a nightly-only experimental API. (`try_reserve_kind` [#48043](https://github.com/rust-lang/rust/issues/48043))

The memory allocator returned an error

#### Fields

🔬This is a nightly-only experimental API. (`try_reserve_kind` [#48043](https://github.com/rust-lang/rust/issues/48043))

The layout of allocation request that failed

[§](#impl-Freeze-for-TryReserveErrorKind)

[§](#impl-RefUnwindSafe-for-TryReserveErrorKind)

[§](#impl-Send-for-TryReserveErrorKind)

[§](#impl-Sync-for-TryReserveErrorKind)

[§](#impl-Unpin-for-TryReserveErrorKind)

[§](#impl-UnsafeUnpin-for-TryReserveErrorKind)

[§](#impl-UnwindSafe-for-TryReserveErrorKind)