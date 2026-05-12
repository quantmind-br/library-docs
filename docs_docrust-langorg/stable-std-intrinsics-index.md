---
title: std::intrinsics - Rust
url: https://doc.rust-lang.org/stable/std/intrinsics/index.html
source: crawler
fetched_at: 2026-05-06T21:28:34.010700956-03:00
rendered_js: false
word_count: 3901
summary: This document provides an overview of Rust compiler intrinsics, which serve as low-level implementation details of the standard library, covering topics such as atomics, volatile memory operations, and compile-time evaluation.
tags:
    - rust
    - compiler-intrinsics
    - low-level
    - core-language
    - atomics
    - volatiles
    - unstable-api
category: reference
---

🔬This is a nightly-only experimental API. (`core_intrinsics`)

Expand description

Compiler intrinsics.

The functions in this module are implementation details of `core` and should not be used outside of the standard library. We generally provide access to intrinsics via stable wrapper functions. Use these instead.

These are the imports making intrinsics available to Rust code. The actual implementations live in the compiler. Some of these intrinsics are lowered to MIR in [https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc\_mir\_transform/src/lower\_intrinsics.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_mir_transform/src/lower_intrinsics.rs). The remaining intrinsics are implemented for the LLVM backend in [https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc\_codegen\_ssa/src/mir/intrinsic.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_codegen_ssa/src/mir/intrinsic.rs) and [https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc\_codegen\_llvm/src/intrinsic.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_codegen_llvm/src/intrinsic.rs), and for const evaluation in [https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc\_const\_eval/src/interpret/intrinsics.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_const_eval/src/interpret/intrinsics.rs).

## [§](#const-intrinsics)Const intrinsics

In order to make an intrinsic unstable usable at compile-time, copy the implementation from [https://github.com/rust-lang/miri/blob/master/src/intrinsics](https://github.com/rust-lang/miri/blob/master/src/intrinsics) to [https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc\_const\_eval/src/interpret/intrinsics.rs](https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_const_eval/src/interpret/intrinsics.rs) and make the intrinsic declaration below a `const fn`. This should be done in coordination with wg-const-eval.

If an intrinsic is supposed to be used from a `const fn` with a `rustc_const_stable` attribute, `#[rustc_intrinsic_const_stable_indirect]` needs to be added to the intrinsic. Such a change requires T-lang approval, because it may bake a feature into the language that cannot be replicated in user code without compiler support.

## [§](#volatiles)Volatiles

The volatile intrinsics provide operations intended to act on I/O memory, which are guaranteed to not be reordered by the compiler across other volatile intrinsics. See [`read_volatile`](https://doc.rust-lang.org/stable/std/ptr/fn.read_volatile.html "fn std::ptr::read_volatile") and [`write_volatile`](https://doc.rust-lang.org/stable/std/ptr/fn.write_volatile.html "fn std::ptr::write_volatile").

## [§](#atomics)Atomics

The atomic intrinsics provide common atomic operations on machine words, with multiple possible memory orderings. See the [atomic types](https://doc.rust-lang.org/stable/std/sync/atomic/index.html "mod std::sync::atomic") docs for details.

## [§](#unwinding)Unwinding

Rust intrinsics may, in general, unwind. If an intrinsic can never unwind, add the `#[rustc_nounwind]` attribute so that the compiler can make use of this fact.

However, even for intrinsics that may unwind, rustc assumes that a Rust intrinsics will never initiate a foreign (non-Rust) unwind, and thus for panic=abort we can always assume that these intrinsics cannot unwind.

[fallback](https://doc.rust-lang.org/stable/std/intrinsics/fallback/index.html "mod std::intrinsics::fallback")Experimental

[gpu](https://doc.rust-lang.org/stable/std/intrinsics/gpu/index.html "mod std::intrinsics::gpu")Experimental

Intrinsics for GPU targets.

[mir](https://doc.rust-lang.org/stable/std/intrinsics/mir/index.html "mod std::intrinsics::mir")Experimental

Rustc internal tooling for hand-writing MIR.

[simd](https://doc.rust-lang.org/stable/std/intrinsics/simd/index.html "mod std::intrinsics::simd")Experimental

SIMD compiler intrinsics.

[AtomicOrdering](https://doc.rust-lang.org/stable/std/intrinsics/enum.AtomicOrdering.html "enum std::intrinsics::AtomicOrdering")Experimental

A type for atomic ordering parameters for intrinsics. This is a separate type from `atomic::Ordering` so that we can make it `ConstParamTy` and fix the values used here without a risk of leaking that to stable code.

[copy](https://doc.rust-lang.org/stable/std/intrinsics/fn.copy.html "fn std::intrinsics::copy")⚠Deprecated

This is an accidentally-stable alias to [`ptr::copy`](https://doc.rust-lang.org/stable/std/ptr/fn.copy.html "fn std::ptr::copy"); use that instead.

[copy\_nonoverlapping](https://doc.rust-lang.org/stable/std/intrinsics/fn.copy_nonoverlapping.html "fn std::intrinsics::copy_nonoverlapping")⚠Deprecated

This is an accidentally-stable alias to [`ptr::copy_nonoverlapping`](https://doc.rust-lang.org/stable/std/ptr/fn.copy_nonoverlapping.html "fn std::ptr::copy_nonoverlapping"); use that instead.

[transmute](https://doc.rust-lang.org/stable/std/intrinsics/fn.transmute.html "fn std::intrinsics::transmute")⚠Deprecated

Reinterprets the bits of a value of one type as another type.

[write\_bytes](https://doc.rust-lang.org/stable/std/intrinsics/fn.write_bytes.html "fn std::intrinsics::write_bytes")⚠Deprecated

This is an accidentally-stable alias to [`ptr::write_bytes`](https://doc.rust-lang.org/stable/std/ptr/fn.write_bytes.html "fn std::ptr::write_bytes"); use that instead.

[abort](https://doc.rust-lang.org/stable/std/intrinsics/fn.abort.html "fn std::intrinsics::abort")Experimental

Aborts the execution of the process.

[add\_with\_overflow](https://doc.rust-lang.org/stable/std/intrinsics/fn.add_with_overflow.html "fn std::intrinsics::add_with_overflow")Experimental

Performs checked integer addition.

[aggregate\_raw\_ptr](https://doc.rust-lang.org/stable/std/intrinsics/fn.aggregate_raw_ptr.html "fn std::intrinsics::aggregate_raw_ptr")Experimental

Lowers in MIR to `Rvalue::Aggregate` with `AggregateKind::RawPtr`.

[align\_of](https://doc.rust-lang.org/stable/std/intrinsics/fn.align_of.html "fn std::intrinsics::align_of")Experimental

The minimum alignment of a type.

[align\_of\_val](https://doc.rust-lang.org/stable/std/intrinsics/fn.align_of_val.html "fn std::intrinsics::align_of_val")⚠Experimental

The required alignment of the referenced value.

[arith\_offset](https://doc.rust-lang.org/stable/std/intrinsics/fn.arith_offset.html "fn std::intrinsics::arith_offset")⚠Experimental

Calculates the offset from a pointer, potentially wrapping.

[assert\_inhabited](https://doc.rust-lang.org/stable/std/intrinsics/fn.assert_inhabited.html "fn std::intrinsics::assert_inhabited")Experimental

A guard for unsafe functions that cannot ever be executed if `T` is uninhabited: This will statically either panic, or do nothing. It does not *guarantee* to ever panic, and should only be called if an assertion failure will imply language UB in the following code.

[assert\_mem\_uninitialized\_valid](https://doc.rust-lang.org/stable/std/intrinsics/fn.assert_mem_uninitialized_valid.html "fn std::intrinsics::assert_mem_uninitialized_valid")Experimental

A guard for `std::mem::uninitialized`. This will statically either panic, or do nothing. It does not *guarantee* to ever panic, and should only be called if an assertion failure will imply language UB in the following code.

[assert\_zero\_valid](https://doc.rust-lang.org/stable/std/intrinsics/fn.assert_zero_valid.html "fn std::intrinsics::assert_zero_valid")Experimental

A guard for unsafe functions that cannot ever be executed if `T` does not permit zero-initialization: This will statically either panic, or do nothing. It does not *guarantee* to ever panic, and should only be called if an assertion failure will imply language UB in the following code.

[assume](https://doc.rust-lang.org/stable/std/intrinsics/fn.assume.html "fn std::intrinsics::assume")⚠Experimental

Informs the optimizer that a condition is always true. If the condition is false, the behavior is undefined.

[atomic\_and](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_and.html "fn std::intrinsics::atomic_and")⚠Experimental

Bitwise and with the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[atomic\_cxchg](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_cxchg.html "fn std::intrinsics::atomic_cxchg")⚠Experimental

Stores a value if the current value is the same as the `old` value. `T` must be an integer or pointer type.

[atomic\_cxchgweak](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_cxchgweak.html "fn std::intrinsics::atomic_cxchgweak")⚠Experimental

Stores a value if the current value is the same as the `old` value. `T` must be an integer or pointer type. The comparison may spuriously fail.

[atomic\_fence](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_fence.html "fn std::intrinsics::atomic_fence")⚠Experimental

An atomic fence.

[atomic\_load](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_load.html "fn std::intrinsics::atomic_load")⚠Experimental

Loads the current value of the pointer. `T` must be an integer or pointer type.

[atomic\_max](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_max.html "fn std::intrinsics::atomic_max")⚠Experimental

Maximum with the current value using a signed comparison. `T` must be a signed integer type.

[atomic\_min](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_min.html "fn std::intrinsics::atomic_min")⚠Experimental

Minimum with the current value using a signed comparison. `T` must be a signed integer type.

[atomic\_nand](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_nand.html "fn std::intrinsics::atomic_nand")⚠Experimental

Bitwise nand with the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[atomic\_or](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_or.html "fn std::intrinsics::atomic_or")⚠Experimental

Bitwise or with the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[atomic\_singlethreadfence](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_singlethreadfence.html "fn std::intrinsics::atomic_singlethreadfence")⚠Experimental

An atomic fence for synchronization within a single thread.

[atomic\_store](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_store.html "fn std::intrinsics::atomic_store")⚠Experimental

Stores the value at the specified memory location. `T` must be an integer or pointer type.

[atomic\_umax](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_umax.html "fn std::intrinsics::atomic_umax")⚠Experimental

Maximum with the current value using an unsigned comparison. `T` must be an unsigned integer type.

[atomic\_umin](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_umin.html "fn std::intrinsics::atomic_umin")⚠Experimental

Minimum with the current value using an unsigned comparison. `T` must be an unsigned integer type.

[atomic\_xadd](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_xadd.html "fn std::intrinsics::atomic_xadd")⚠Experimental

Adds to the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[atomic\_xchg](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_xchg.html "fn std::intrinsics::atomic_xchg")⚠Experimental

Stores the value at the specified memory location, returning the old value. `T` must be an integer or pointer type.

[atomic\_xor](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_xor.html "fn std::intrinsics::atomic_xor")⚠Experimental

Bitwise xor with the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[atomic\_xsub](https://doc.rust-lang.org/stable/std/intrinsics/fn.atomic_xsub.html "fn std::intrinsics::atomic_xsub")⚠Experimental

Subtract from the current value, returning the previous value. `T` must be an integer or pointer type. `U` must be the same as `T` if that is an integer type, or `usize` if `T` is a pointer type.

[autodiff](https://doc.rust-lang.org/stable/std/intrinsics/fn.autodiff.html "fn std::intrinsics::autodiff")Experimental

Generates the LLVM body for the automatic differentiation of `f` using Enzyme, with `df` as the derivative function and `args` as its arguments.

[bitreverse](https://doc.rust-lang.org/stable/std/intrinsics/fn.bitreverse.html "fn std::intrinsics::bitreverse")Experimental

Reverses the bits in an integer type `T`.

[black\_box](https://doc.rust-lang.org/stable/std/intrinsics/fn.black_box.html "fn std::intrinsics::black_box")Experimental

See documentation of [`std::hint::black_box`](https://doc.rust-lang.org/stable/std/hint/fn.black_box.html "fn std::hint::black_box") for details.

[breakpoint](https://doc.rust-lang.org/stable/std/intrinsics/fn.breakpoint.html "fn std::intrinsics::breakpoint")Experimental

Executes a breakpoint trap, for inspection by a debugger.

[bswap](https://doc.rust-lang.org/stable/std/intrinsics/fn.bswap.html "fn std::intrinsics::bswap")Experimental

Reverses the bytes in an integer type `T`.

[caller\_location](https://doc.rust-lang.org/stable/std/intrinsics/fn.caller_location.html "fn std::intrinsics::caller_location")Experimental

Gets a reference to a static `Location` indicating where it was called.

[carrying\_mul\_add](https://doc.rust-lang.org/stable/std/intrinsics/fn.carrying_mul_add.html "fn std::intrinsics::carrying_mul_add")Experimental

Performs full-width multiplication and addition with a carry: `multiplier * multiplicand + addend + carry`.

[carryless\_mul](https://doc.rust-lang.org/stable/std/intrinsics/fn.carryless_mul.html "fn std::intrinsics::carryless_mul")Experimental

Carryless multiply.

[catch\_unwind](https://doc.rust-lang.org/stable/std/intrinsics/fn.catch_unwind.html "fn std::intrinsics::catch_unwind")⚠Experimental

Rust’s “try catch” construct for unwinding. Invokes the function pointer `try_fn` with the data pointer `data`, and calls `catch_fn` if unwinding occurs while `try_fn` runs. Returns `1` if unwinding occurred and `catch_fn` was called; returns `0` otherwise.

[ceilf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.ceilf16.html "fn std::intrinsics::ceilf16")Experimental

Returns the smallest integer greater than or equal to an `f16`.

[ceilf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.ceilf32.html "fn std::intrinsics::ceilf32")Experimental

Returns the smallest integer greater than or equal to an `f32`.

[ceilf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.ceilf64.html "fn std::intrinsics::ceilf64")Experimental

Returns the smallest integer greater than or equal to an `f64`.

[ceilf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.ceilf128.html "fn std::intrinsics::ceilf128")Experimental

Returns the smallest integer greater than or equal to an `f128`.

[cold\_path](https://doc.rust-lang.org/stable/std/intrinsics/fn.cold_path.html "fn std::intrinsics::cold_path")Experimental

Hints to the compiler that current code path is cold.

[compare\_bytes](https://doc.rust-lang.org/stable/std/intrinsics/fn.compare_bytes.html "fn std::intrinsics::compare_bytes")⚠Experimental

Lexicographically compare `[left, left + bytes)` and `[right, right + bytes)` as unsigned bytes, returning negative if `left` is less, zero if all the bytes match, or positive if `left` is greater.

[const\_allocate](https://doc.rust-lang.org/stable/std/intrinsics/fn.const_allocate.html "fn std::intrinsics::const_allocate")⚠Experimental

Allocates a block of memory at compile time. At runtime, just returns a null pointer.

[const\_deallocate](https://doc.rust-lang.org/stable/std/intrinsics/fn.const_deallocate.html "fn std::intrinsics::const_deallocate")⚠Experimental

Deallocates a memory which allocated by `intrinsics::const_allocate` at compile time. At runtime, it does nothing.

[const\_eval\_select](https://doc.rust-lang.org/stable/std/intrinsics/fn.const_eval_select.html "fn std::intrinsics::const_eval_select")Experimental

Selects which function to call depending on the context.

[const\_make\_global](https://doc.rust-lang.org/stable/std/intrinsics/fn.const_make_global.html "fn std::intrinsics::const_make_global")⚠Experimental

Convert the allocation this pointer points to into immutable global memory. The pointer must point to the beginning of a heap allocation. This operation only makes sense during compile time. At runtime, it does nothing.

[contract\_check\_ensures](https://doc.rust-lang.org/stable/std/intrinsics/fn.contract_check_ensures.html "fn std::intrinsics::contract_check_ensures")Experimental

Check if the post-condition `cond` has been met.

[contract\_check\_requires](https://doc.rust-lang.org/stable/std/intrinsics/fn.contract_check_requires.html "fn std::intrinsics::contract_check_requires")Experimental

Check if the pre-condition `cond` has been met.

[copysignf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.copysignf16.html "fn std::intrinsics::copysignf16")Experimental

Copies the sign from `y` to `x` for `f16` values.

[copysignf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.copysignf32.html "fn std::intrinsics::copysignf32")Experimental

Copies the sign from `y` to `x` for `f32` values.

[copysignf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.copysignf64.html "fn std::intrinsics::copysignf64")Experimental

Copies the sign from `y` to `x` for `f64` values.

[copysignf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.copysignf128.html "fn std::intrinsics::copysignf128")Experimental

Copies the sign from `y` to `x` for `f128` values.

[cosf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.cosf16.html "fn std::intrinsics::cosf16")Experimental

Returns the cosine of an `f16`.

[cosf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.cosf32.html "fn std::intrinsics::cosf32")Experimental

Returns the cosine of an `f32`.

[cosf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.cosf64.html "fn std::intrinsics::cosf64")Experimental

Returns the cosine of an `f64`.

[cosf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.cosf128.html "fn std::intrinsics::cosf128")Experimental

Returns the cosine of an `f128`.

[ctlz](https://doc.rust-lang.org/stable/std/intrinsics/fn.ctlz.html "fn std::intrinsics::ctlz")Experimental

Returns the number of leading unset bits (zeroes) in an integer type `T`.

[ctlz\_nonzero](https://doc.rust-lang.org/stable/std/intrinsics/fn.ctlz_nonzero.html "fn std::intrinsics::ctlz_nonzero")⚠Experimental

Like `ctlz`, but extra-unsafe as it returns `undef` when given an `x` with value `0`.

[ctpop](https://doc.rust-lang.org/stable/std/intrinsics/fn.ctpop.html "fn std::intrinsics::ctpop")Experimental

Returns the number of bits set in an integer type `T`

[cttz](https://doc.rust-lang.org/stable/std/intrinsics/fn.cttz.html "fn std::intrinsics::cttz")Experimental

Returns the number of trailing unset bits (zeroes) in an integer type `T`.

[cttz\_nonzero](https://doc.rust-lang.org/stable/std/intrinsics/fn.cttz_nonzero.html "fn std::intrinsics::cttz_nonzero")⚠Experimental

Like `cttz`, but extra-unsafe as it returns `undef` when given an `x` with value `0`.

[discriminant\_value](https://doc.rust-lang.org/stable/std/intrinsics/fn.discriminant_value.html "fn std::intrinsics::discriminant_value")Experimental

Returns the value of the discriminant for the variant in ‘v’; if `T` has no discriminant, returns `0`.

[disjoint\_bitor](https://doc.rust-lang.org/stable/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor")⚠Experimental

Combine two values which have no bits in common.

[exact\_div](https://doc.rust-lang.org/stable/std/intrinsics/fn.exact_div.html "fn std::intrinsics::exact_div")⚠Experimental

Performs an exact division, resulting in undefined behavior where `x % y != 0` or `y == 0` or `x == T::MIN && y == -1`

[exp2f16](https://doc.rust-lang.org/stable/std/intrinsics/fn.exp2f16.html "fn std::intrinsics::exp2f16")Experimental

Returns 2 raised to the power of an `f16`.

[exp2f32](https://doc.rust-lang.org/stable/std/intrinsics/fn.exp2f32.html "fn std::intrinsics::exp2f32")Experimental

Returns 2 raised to the power of an `f32`.

[exp2f64](https://doc.rust-lang.org/stable/std/intrinsics/fn.exp2f64.html "fn std::intrinsics::exp2f64")Experimental

Returns 2 raised to the power of an `f64`.

[exp2f128](https://doc.rust-lang.org/stable/std/intrinsics/fn.exp2f128.html "fn std::intrinsics::exp2f128")Experimental

Returns 2 raised to the power of an `f128`.

[expf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.expf16.html "fn std::intrinsics::expf16")Experimental

Returns the exponential of an `f16`.

[expf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.expf32.html "fn std::intrinsics::expf32")Experimental

Returns the exponential of an `f32`.

[expf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.expf64.html "fn std::intrinsics::expf64")Experimental

Returns the exponential of an `f64`.

[expf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.expf128.html "fn std::intrinsics::expf128")Experimental

Returns the exponential of an `f128`.

[fabsf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.fabsf16.html "fn std::intrinsics::fabsf16")Experimental

Returns the absolute value of an `f16`.

[fabsf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.fabsf32.html "fn std::intrinsics::fabsf32")Experimental

Returns the absolute value of an `f32`.

[fabsf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.fabsf64.html "fn std::intrinsics::fabsf64")Experimental

Returns the absolute value of an `f64`.

[fabsf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.fabsf128.html "fn std::intrinsics::fabsf128")Experimental

Returns the absolute value of an `f128`.

[fadd\_algebraic](https://doc.rust-lang.org/stable/std/intrinsics/fn.fadd_algebraic.html "fn std::intrinsics::fadd_algebraic")Experimental

Float addition that allows optimizations based on algebraic rules.

[fadd\_fast](https://doc.rust-lang.org/stable/std/intrinsics/fn.fadd_fast.html "fn std::intrinsics::fadd_fast")⚠Experimental

Float addition that allows optimizations based on algebraic rules. Requires that inputs and output of the operation are finite, causing UB otherwise.

[fdiv\_algebraic](https://doc.rust-lang.org/stable/std/intrinsics/fn.fdiv_algebraic.html "fn std::intrinsics::fdiv_algebraic")Experimental

Float division that allows optimizations based on algebraic rules.

[fdiv\_fast](https://doc.rust-lang.org/stable/std/intrinsics/fn.fdiv_fast.html "fn std::intrinsics::fdiv_fast")⚠Experimental

Float division that allows optimizations based on algebraic rules. Requires that inputs and output of the operation are finite, causing UB otherwise.

[float\_to\_int\_unchecked](https://doc.rust-lang.org/stable/std/intrinsics/fn.float_to_int_unchecked.html "fn std::intrinsics::float_to_int_unchecked")⚠Experimental

Converts with LLVM’s fptoui/fptosi, which may return undef for values out of range ([https://github.com/rust-lang/rust/issues/10184](https://github.com/rust-lang/rust/issues/10184))

[floorf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.floorf16.html "fn std::intrinsics::floorf16")Experimental

Returns the largest integer less than or equal to an `f16`.

[floorf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.floorf32.html "fn std::intrinsics::floorf32")Experimental

Returns the largest integer less than or equal to an `f32`.

[floorf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.floorf64.html "fn std::intrinsics::floorf64")Experimental

Returns the largest integer less than or equal to an `f64`.

[floorf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.floorf128.html "fn std::intrinsics::floorf128")Experimental

Returns the largest integer less than or equal to an `f128`.

[fmaf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmaf16.html "fn std::intrinsics::fmaf16")Experimental

Returns `a * b + c` for `f16` values.

[fmaf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmaf32.html "fn std::intrinsics::fmaf32")Experimental

Returns `a * b + c` for `f32` values.

[fmaf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmaf64.html "fn std::intrinsics::fmaf64")Experimental

Returns `a * b + c` for `f64` values.

[fmaf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmaf128.html "fn std::intrinsics::fmaf128")Experimental

Returns `a * b + c` for `f128` values.

[fmul\_algebraic](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmul_algebraic.html "fn std::intrinsics::fmul_algebraic")Experimental

Float multiplication that allows optimizations based on algebraic rules.

[fmul\_fast](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmul_fast.html "fn std::intrinsics::fmul_fast")⚠Experimental

Float multiplication that allows optimizations based on algebraic rules. Requires that inputs and output of the operation are finite, causing UB otherwise.

[fmuladdf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmuladdf16.html "fn std::intrinsics::fmuladdf16")Experimental

Returns `a * b + c` for `f16` values, non-deterministically executing either a fused multiply-add or two operations with rounding of the intermediate result.

[fmuladdf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmuladdf32.html "fn std::intrinsics::fmuladdf32")Experimental

Returns `a * b + c` for `f32` values, non-deterministically executing either a fused multiply-add or two operations with rounding of the intermediate result.

[fmuladdf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmuladdf64.html "fn std::intrinsics::fmuladdf64")Experimental

Returns `a * b + c` for `f64` values, non-deterministically executing either a fused multiply-add or two operations with rounding of the intermediate result.

[fmuladdf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.fmuladdf128.html "fn std::intrinsics::fmuladdf128")Experimental

Returns `a * b + c` for `f128` values, non-deterministically executing either a fused multiply-add or two operations with rounding of the intermediate result.

[forget](https://doc.rust-lang.org/stable/std/intrinsics/fn.forget.html "fn std::intrinsics::forget")Experimental

Moves a value out of scope without running drop glue.

[frem\_algebraic](https://doc.rust-lang.org/stable/std/intrinsics/fn.frem_algebraic.html "fn std::intrinsics::frem_algebraic")Experimental

Float remainder that allows optimizations based on algebraic rules.

[frem\_fast](https://doc.rust-lang.org/stable/std/intrinsics/fn.frem_fast.html "fn std::intrinsics::frem_fast")⚠Experimental

Float remainder that allows optimizations based on algebraic rules. Requires that inputs and output of the operation are finite, causing UB otherwise.

[fsub\_algebraic](https://doc.rust-lang.org/stable/std/intrinsics/fn.fsub_algebraic.html "fn std::intrinsics::fsub_algebraic")Experimental

Float subtraction that allows optimizations based on algebraic rules.

[fsub\_fast](https://doc.rust-lang.org/stable/std/intrinsics/fn.fsub_fast.html "fn std::intrinsics::fsub_fast")⚠Experimental

Float subtraction that allows optimizations based on algebraic rules. Requires that inputs and output of the operation are finite, causing UB otherwise.

[is\_val\_statically\_known](https://doc.rust-lang.org/stable/std/intrinsics/fn.is_val_statically_known.html "fn std::intrinsics::is_val_statically_known")Experimental

Returns whether the argument’s value is statically known at compile-time.

[likely](https://doc.rust-lang.org/stable/std/intrinsics/fn.likely.html "fn std::intrinsics::likely")Experimental

Hints to the compiler that branch condition is likely to be true. Returns the value passed to it.

[log2f16](https://doc.rust-lang.org/stable/std/intrinsics/fn.log2f16.html "fn std::intrinsics::log2f16")Experimental

Returns the base 2 logarithm of an `f16`.

[log2f32](https://doc.rust-lang.org/stable/std/intrinsics/fn.log2f32.html "fn std::intrinsics::log2f32")Experimental

Returns the base 2 logarithm of an `f32`.

[log2f64](https://doc.rust-lang.org/stable/std/intrinsics/fn.log2f64.html "fn std::intrinsics::log2f64")Experimental

Returns the base 2 logarithm of an `f64`.

[log2f128](https://doc.rust-lang.org/stable/std/intrinsics/fn.log2f128.html "fn std::intrinsics::log2f128")Experimental

Returns the base 2 logarithm of an `f128`.

[log10f16](https://doc.rust-lang.org/stable/std/intrinsics/fn.log10f16.html "fn std::intrinsics::log10f16")Experimental

Returns the base 10 logarithm of an `f16`.

[log10f32](https://doc.rust-lang.org/stable/std/intrinsics/fn.log10f32.html "fn std::intrinsics::log10f32")Experimental

Returns the base 10 logarithm of an `f32`.

[log10f64](https://doc.rust-lang.org/stable/std/intrinsics/fn.log10f64.html "fn std::intrinsics::log10f64")Experimental

Returns the base 10 logarithm of an `f64`.

[log10f128](https://doc.rust-lang.org/stable/std/intrinsics/fn.log10f128.html "fn std::intrinsics::log10f128")Experimental

Returns the base 10 logarithm of an `f128`.

[logf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.logf16.html "fn std::intrinsics::logf16")Experimental

Returns the natural logarithm of an `f16`.

[logf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.logf32.html "fn std::intrinsics::logf32")Experimental

Returns the natural logarithm of an `f32`.

[logf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.logf64.html "fn std::intrinsics::logf64")Experimental

Returns the natural logarithm of an `f64`.

[logf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.logf128.html "fn std::intrinsics::logf128")Experimental

Returns the natural logarithm of an `f128`.

[maximumf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.maximumf16.html "fn std::intrinsics::maximumf16")Experimental

Returns the maximum of two `f16` values, propagating NaN.

[maximumf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.maximumf32.html "fn std::intrinsics::maximumf32")Experimental

Returns the maximum of two `f32` values, propagating NaN.

[maximumf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.maximumf64.html "fn std::intrinsics::maximumf64")Experimental

Returns the maximum of two `f64` values, propagating NaN.

[maximumf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.maximumf128.html "fn std::intrinsics::maximumf128")Experimental

Returns the maximum of two `f128` values, propagating NaN.

[maxnumf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.maxnumf16.html "fn std::intrinsics::maxnumf16")Experimental

Returns the maximum of two `f16` values, ignoring NaN.

[maxnumf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.maxnumf32.html "fn std::intrinsics::maxnumf32")Experimental

Returns the maximum of two `f32` values, ignoring NaN.

[maxnumf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.maxnumf64.html "fn std::intrinsics::maxnumf64")Experimental

Returns the maximum of two `f64` values, ignoring NaN.

[maxnumf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.maxnumf128.html "fn std::intrinsics::maxnumf128")Experimental

Returns the maximum of two `f128` values, ignoring NaN.

[minimumf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.minimumf16.html "fn std::intrinsics::minimumf16")Experimental

Returns the minimum of two `f16` values, propagating NaN.

[minimumf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.minimumf32.html "fn std::intrinsics::minimumf32")Experimental

Returns the minimum of two `f32` values, propagating NaN.

[minimumf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.minimumf64.html "fn std::intrinsics::minimumf64")Experimental

Returns the minimum of two `f64` values, propagating NaN.

[minimumf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.minimumf128.html "fn std::intrinsics::minimumf128")Experimental

Returns the minimum of two `f128` values, propagating NaN.

[minnumf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.minnumf16.html "fn std::intrinsics::minnumf16")Experimental

Returns the minimum of two `f16` values, ignoring NaN.

[minnumf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.minnumf32.html "fn std::intrinsics::minnumf32")Experimental

Returns the minimum of two `f32` values, ignoring NaN.

[minnumf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.minnumf64.html "fn std::intrinsics::minnumf64")Experimental

Returns the minimum of two `f64` values, ignoring NaN.

[minnumf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.minnumf128.html "fn std::intrinsics::minnumf128")Experimental

Returns the minimum of two `f128` values, ignoring NaN.

[mul\_with\_overflow](https://doc.rust-lang.org/stable/std/intrinsics/fn.mul_with_overflow.html "fn std::intrinsics::mul_with_overflow")Experimental

Performs checked integer multiplication

[needs\_drop](https://doc.rust-lang.org/stable/std/intrinsics/fn.needs_drop.html "fn std::intrinsics::needs_drop")Experimental

Returns `true` if the actual type given as `T` requires drop glue; returns `false` if the actual type provided for `T` implements `Copy`.

[nontemporal\_store](https://doc.rust-lang.org/stable/std/intrinsics/fn.nontemporal_store.html "fn std::intrinsics::nontemporal_store")⚠Experimental

Emits a `nontemporal` store, which gives a hint to the CPU that the data should not be held in cache. Except for performance, this is fully equivalent to `ptr.write(val)`.

[offload](https://doc.rust-lang.org/stable/std/intrinsics/fn.offload.html "fn std::intrinsics::offload")Experimental

Generates the LLVM body of a wrapper function to offload a kernel `f`.

[offset](https://doc.rust-lang.org/stable/std/intrinsics/fn.offset.html "fn std::intrinsics::offset")⚠Experimental

Calculates the offset from a pointer.

[offset\_of](https://doc.rust-lang.org/stable/std/intrinsics/fn.offset_of.html "fn std::intrinsics::offset_of")Experimental

The offset of a field inside a type.

[overflow\_checks](https://doc.rust-lang.org/stable/std/intrinsics/fn.overflow_checks.html "fn std::intrinsics::overflow_checks")Experimental

Returns whether we should perform some overflow-checking at runtime. This eventually evaluates to `cfg!(overflow_checks)`, but behaves different from `cfg!` when mixing crates built with different flags: if the crate has overflow checks enabled or carries the `#[rustc_inherit_overflow_checks]` attribute, evaluation is delayed until monomorphization (or until the call gets inlined into a crate that does not delay evaluation further); otherwise it can happen any time.

[powf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.powf16.html "fn std::intrinsics::powf16")Experimental

Raises an `f16` to an `f16` power.

[powf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.powf32.html "fn std::intrinsics::powf32")Experimental

Raises an `f32` to an `f32` power.

[powf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.powf64.html "fn std::intrinsics::powf64")Experimental

Raises an `f64` to an `f64` power.

[powf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.powf128.html "fn std::intrinsics::powf128")Experimental

Raises an `f128` to an `f128` power.

[powif16](https://doc.rust-lang.org/stable/std/intrinsics/fn.powif16.html "fn std::intrinsics::powif16")Experimental

Raises an `f16` to an integer power.

[powif32](https://doc.rust-lang.org/stable/std/intrinsics/fn.powif32.html "fn std::intrinsics::powif32")Experimental

Raises an `f32` to an integer power.

[powif64](https://doc.rust-lang.org/stable/std/intrinsics/fn.powif64.html "fn std::intrinsics::powif64")Experimental

Raises an `f64` to an integer power.

[powif128](https://doc.rust-lang.org/stable/std/intrinsics/fn.powif128.html "fn std::intrinsics::powif128")Experimental

Raises an `f128` to an integer power.

[prefetch\_read\_data](https://doc.rust-lang.org/stable/std/intrinsics/fn.prefetch_read_data.html "fn std::intrinsics::prefetch_read_data")Experimental

The `prefetch` intrinsic is a hint to the code generator to insert a prefetch instruction for the given address if supported; otherwise, it is a no-op. Prefetches have no effect on the behavior of the program but can change its performance characteristics.

[prefetch\_read\_instruction](https://doc.rust-lang.org/stable/std/intrinsics/fn.prefetch_read_instruction.html "fn std::intrinsics::prefetch_read_instruction")Experimental

The `prefetch` intrinsic is a hint to the code generator to insert a prefetch instruction for the given address if supported; otherwise, it is a no-op. Prefetches have no effect on the behavior of the program but can change its performance characteristics.

[prefetch\_write\_data](https://doc.rust-lang.org/stable/std/intrinsics/fn.prefetch_write_data.html "fn std::intrinsics::prefetch_write_data")Experimental

The `prefetch` intrinsic is a hint to the code generator to insert a prefetch instruction for the given address if supported; otherwise, it is a no-op. Prefetches have no effect on the behavior of the program but can change its performance characteristics.

[prefetch\_write\_instruction](https://doc.rust-lang.org/stable/std/intrinsics/fn.prefetch_write_instruction.html "fn std::intrinsics::prefetch_write_instruction")Experimental

The `prefetch` intrinsic is a hint to the code generator to insert a prefetch instruction for the given address if supported; otherwise, it is a no-op. Prefetches have no effect on the behavior of the program but can change its performance characteristics.

[ptr\_guaranteed\_cmp](https://doc.rust-lang.org/stable/std/intrinsics/fn.ptr_guaranteed_cmp.html "fn std::intrinsics::ptr_guaranteed_cmp")Experimental

See documentation of `<*const T>::guaranteed_eq` for details. Returns `2` if the result is unknown. Returns `1` if the pointers are guaranteed equal. Returns `0` if the pointers are guaranteed inequal.

[ptr\_mask](https://doc.rust-lang.org/stable/std/intrinsics/fn.ptr_mask.html "fn std::intrinsics::ptr_mask")Experimental

Masks out bits of the pointer according to a mask.

[ptr\_metadata](https://doc.rust-lang.org/stable/std/intrinsics/fn.ptr_metadata.html "fn std::intrinsics::ptr_metadata")Experimental

Lowers in MIR to `Rvalue::UnaryOp` with `UnOp::PtrMetadata`.

[ptr\_offset\_from](https://doc.rust-lang.org/stable/std/intrinsics/fn.ptr_offset_from.html "fn std::intrinsics::ptr_offset_from")⚠Experimental

See documentation of `<*const T>::offset_from` for details.

[ptr\_offset\_from\_unsigned](https://doc.rust-lang.org/stable/std/intrinsics/fn.ptr_offset_from_unsigned.html "fn std::intrinsics::ptr_offset_from_unsigned")⚠Experimental

See documentation of `<*const T>::offset_from_unsigned` for details.

[raw\_eq](https://doc.rust-lang.org/stable/std/intrinsics/fn.raw_eq.html "fn std::intrinsics::raw_eq")⚠Experimental

Determines whether the raw bytes of the two values are equal.

[read\_via\_copy](https://doc.rust-lang.org/stable/std/intrinsics/fn.read_via_copy.html "fn std::intrinsics::read_via_copy")⚠Experimental

This is an implementation detail of [`crate::ptr::read`](https://doc.rust-lang.org/stable/std/ptr/fn.read.html "fn std::ptr::read") and should not be used anywhere else. See its comments for why this exists.

[rotate\_left](https://doc.rust-lang.org/stable/std/intrinsics/fn.rotate_left.html "fn std::intrinsics::rotate_left")Experimental

Performs rotate left.

[rotate\_right](https://doc.rust-lang.org/stable/std/intrinsics/fn.rotate_right.html "fn std::intrinsics::rotate_right")Experimental

Performs rotate right.

[round\_ties\_even\_f16](https://doc.rust-lang.org/stable/std/intrinsics/fn.round_ties_even_f16.html "fn std::intrinsics::round_ties_even_f16")Experimental

Returns the nearest integer to an `f16`. Rounds half-way cases to the number with an even least significant digit.

[round\_ties\_even\_f32](https://doc.rust-lang.org/stable/std/intrinsics/fn.round_ties_even_f32.html "fn std::intrinsics::round_ties_even_f32")Experimental

Returns the nearest integer to an `f32`. Rounds half-way cases to the number with an even least significant digit.

[round\_ties\_even\_f64](https://doc.rust-lang.org/stable/std/intrinsics/fn.round_ties_even_f64.html "fn std::intrinsics::round_ties_even_f64")Experimental

Returns the nearest integer to an `f64`. Rounds half-way cases to the number with an even least significant digit.

[round\_ties\_even\_f128](https://doc.rust-lang.org/stable/std/intrinsics/fn.round_ties_even_f128.html "fn std::intrinsics::round_ties_even_f128")Experimental

Returns the nearest integer to an `f128`. Rounds half-way cases to the number with an even least significant digit.

[roundf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.roundf16.html "fn std::intrinsics::roundf16")Experimental

Returns the nearest integer to an `f16`. Rounds half-way cases away from zero.

[roundf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.roundf32.html "fn std::intrinsics::roundf32")Experimental

Returns the nearest integer to an `f32`. Rounds half-way cases away from zero.

[roundf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.roundf64.html "fn std::intrinsics::roundf64")Experimental

Returns the nearest integer to an `f64`. Rounds half-way cases away from zero.

[roundf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.roundf128.html "fn std::intrinsics::roundf128")Experimental

Returns the nearest integer to an `f128`. Rounds half-way cases away from zero.

[rustc\_peek](https://doc.rust-lang.org/stable/std/intrinsics/fn.rustc_peek.html "fn std::intrinsics::rustc_peek")Experimental

Magic intrinsic that derives its meaning from attributes attached to the function.

[saturating\_add](https://doc.rust-lang.org/stable/std/intrinsics/fn.saturating_add.html "fn std::intrinsics::saturating_add")Experimental

Computes `a + b`, saturating at numeric bounds.

[saturating\_sub](https://doc.rust-lang.org/stable/std/intrinsics/fn.saturating_sub.html "fn std::intrinsics::saturating_sub")Experimental

Computes `a - b`, saturating at numeric bounds.

[select\_unpredictable](https://doc.rust-lang.org/stable/std/intrinsics/fn.select_unpredictable.html "fn std::intrinsics::select_unpredictable")Experimental

Returns either `true_val` or `false_val` depending on condition `b` with a hint to the compiler that this condition is unlikely to be correctly predicted by a CPU’s branch predictor (e.g. a binary search).

[sinf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.sinf16.html "fn std::intrinsics::sinf16")Experimental

Returns the sine of an `f16`.

[sinf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.sinf32.html "fn std::intrinsics::sinf32")Experimental

Returns the sine of an `f32`.

[sinf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.sinf64.html "fn std::intrinsics::sinf64")Experimental

Returns the sine of an `f64`.

[sinf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.sinf128.html "fn std::intrinsics::sinf128")Experimental

Returns the sine of an `f128`.

[size\_of](https://doc.rust-lang.org/stable/std/intrinsics/fn.size_of.html "fn std::intrinsics::size_of")Experimental

The size of a type in bytes.

[size\_of\_val](https://doc.rust-lang.org/stable/std/intrinsics/fn.size_of_val.html "fn std::intrinsics::size_of_val")⚠Experimental

The size of the referenced value in bytes.

[slice\_get\_unchecked](https://doc.rust-lang.org/stable/std/intrinsics/fn.slice_get_unchecked.html "fn std::intrinsics::slice_get_unchecked")⚠Experimental

Projects to the `index`-th element of `slice_ptr`, as the same kind of pointer as the slice was provided – so `&mut [T] → &mut T`, `&[T] → &T`, `*mut [T] → *mut T`, or `*const [T] → *const T` – without a bounds check.

[sqrtf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.sqrtf16.html "fn std::intrinsics::sqrtf16")Experimental

Returns the square root of an `f16`

[sqrtf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.sqrtf32.html "fn std::intrinsics::sqrtf32")Experimental

Returns the square root of an `f32`

[sqrtf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.sqrtf64.html "fn std::intrinsics::sqrtf64")Experimental

Returns the square root of an `f64`

[sqrtf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.sqrtf128.html "fn std::intrinsics::sqrtf128")Experimental

Returns the square root of an `f128`

[sub\_with\_overflow](https://doc.rust-lang.org/stable/std/intrinsics/fn.sub_with_overflow.html "fn std::intrinsics::sub_with_overflow")Experimental

Performs checked integer subtraction

[three\_way\_compare](https://doc.rust-lang.org/stable/std/intrinsics/fn.three_way_compare.html "fn std::intrinsics::three_way_compare")Experimental

Does a three-way comparison between the two arguments, which must be of character or integer (signed or unsigned) type.

[transmute\_unchecked](https://doc.rust-lang.org/stable/std/intrinsics/fn.transmute_unchecked.html "fn std::intrinsics::transmute_unchecked")⚠Experimental

Like [`transmute`](https://doc.rust-lang.org/stable/std/mem/fn.transmute.html "fn std::mem::transmute"), but even less checked at compile-time: rather than giving an error for `size_of::<Src>() != size_of::<Dst>()`, it’s **Undefined Behavior** at runtime.

[truncf16](https://doc.rust-lang.org/stable/std/intrinsics/fn.truncf16.html "fn std::intrinsics::truncf16")Experimental

Returns the integer part of an `f16`.

[truncf32](https://doc.rust-lang.org/stable/std/intrinsics/fn.truncf32.html "fn std::intrinsics::truncf32")Experimental

Returns the integer part of an `f32`.

[truncf64](https://doc.rust-lang.org/stable/std/intrinsics/fn.truncf64.html "fn std::intrinsics::truncf64")Experimental

Returns the integer part of an `f64`.

[truncf128](https://doc.rust-lang.org/stable/std/intrinsics/fn.truncf128.html "fn std::intrinsics::truncf128")Experimental

Returns the integer part of an `f128`.

[type\_id](https://doc.rust-lang.org/stable/std/intrinsics/fn.type_id.html "fn std::intrinsics::type_id")Experimental

Gets an identifier which is globally unique to the specified type. This function will return the same value for a type regardless of whichever crate it is invoked in.

[type\_id\_eq](https://doc.rust-lang.org/stable/std/intrinsics/fn.type_id_eq.html "fn std::intrinsics::type_id_eq")Experimental

Tests (at compile-time) if two [`crate::any::TypeId`](https://doc.rust-lang.org/stable/std/any/struct.TypeId.html "struct std::any::TypeId") instances identify the same type. This is necessary because at const-eval time the actual discriminating data is opaque and cannot be inspected directly.

[type\_id\_vtable](https://doc.rust-lang.org/stable/std/intrinsics/fn.type_id_vtable.html "fn std::intrinsics::type_id_vtable")Experimental

Check if a type represented by a `TypeId` implements a trait represented by a `TypeId`. It can only be called at compile time, the backends do not implement it. If it implements the trait the dyn metadata gets returned for vtable access.

[type\_name](https://doc.rust-lang.org/stable/std/intrinsics/fn.type_name.html "fn std::intrinsics::type_name")Experimental

Gets a static string slice containing the name of a type.

[type\_of](https://doc.rust-lang.org/stable/std/intrinsics/fn.type_of.html "fn std::intrinsics::type_of")Experimental

Compute the type information of a concrete type. It can only be called at compile time, the backends do not implement it.

[typed\_swap\_nonoverlapping](https://doc.rust-lang.org/stable/std/intrinsics/fn.typed_swap_nonoverlapping.html "fn std::intrinsics::typed_swap_nonoverlapping")⚠Experimental

Non-overlapping *typed* swap of a single value.

[ub\_checks](https://doc.rust-lang.org/stable/std/intrinsics/fn.ub_checks.html "fn std::intrinsics::ub_checks")Experimental

Returns whether we should perform some UB-checking at runtime. This eventually evaluates to `cfg!(ub_checks)`, but behaves different from `cfg!` when mixing crates built with different flags: if the crate has UB checks enabled or carries the `#[rustc_preserve_ub_checks]` attribute, evaluation is delayed until monomorphization (or until the call gets inlined into a crate that does not delay evaluation further); otherwise it can happen any time.

[unaligned\_volatile\_load](https://doc.rust-lang.org/stable/std/intrinsics/fn.unaligned_volatile_load.html "fn std::intrinsics::unaligned_volatile_load")⚠Experimental

Performs a volatile load from the `src` pointer The pointer is not required to be aligned.

[unaligned\_volatile\_store](https://doc.rust-lang.org/stable/std/intrinsics/fn.unaligned_volatile_store.html "fn std::intrinsics::unaligned_volatile_store")⚠Experimental

Performs a volatile store to the `dst` pointer. The pointer is not required to be aligned.

[unchecked\_add](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_add.html "fn std::intrinsics::unchecked_add")⚠Experimental

Returns the result of an unchecked addition, resulting in undefined behavior when `x + y > T::MAX` or `x + y < T::MIN`.

[unchecked\_div](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_div.html "fn std::intrinsics::unchecked_div")⚠Experimental

Performs an unchecked division, resulting in undefined behavior where `y == 0` or `x == T::MIN && y == -1`

[unchecked\_funnel\_shl](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_funnel_shl.html "fn std::intrinsics::unchecked_funnel_shl")⚠Experimental

Funnel Shift left.

[unchecked\_funnel\_shr](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_funnel_shr.html "fn std::intrinsics::unchecked_funnel_shr")⚠Experimental

Funnel Shift right.

[unchecked\_mul](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_mul.html "fn std::intrinsics::unchecked_mul")⚠Experimental

Returns the result of an unchecked multiplication, resulting in undefined behavior when `x * y > T::MAX` or `x * y < T::MIN`.

[unchecked\_rem](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_rem.html "fn std::intrinsics::unchecked_rem")⚠Experimental

Returns the remainder of an unchecked division, resulting in undefined behavior when `y == 0` or `x == T::MIN && y == -1`

[unchecked\_shl](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_shl.html "fn std::intrinsics::unchecked_shl")⚠Experimental

Performs an unchecked left shift, resulting in undefined behavior when `y < 0` or `y >= N`, where N is the width of T in bits.

[unchecked\_shr](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_shr.html "fn std::intrinsics::unchecked_shr")⚠Experimental

Performs an unchecked right shift, resulting in undefined behavior when `y < 0` or `y >= N`, where N is the width of T in bits.

[unchecked\_sub](https://doc.rust-lang.org/stable/std/intrinsics/fn.unchecked_sub.html "fn std::intrinsics::unchecked_sub")⚠Experimental

Returns the result of an unchecked subtraction, resulting in undefined behavior when `x - y > T::MAX` or `x - y < T::MIN`.

[unlikely](https://doc.rust-lang.org/stable/std/intrinsics/fn.unlikely.html "fn std::intrinsics::unlikely")Experimental

Hints to the compiler that branch condition is likely to be false. Returns the value passed to it.

[unreachable](https://doc.rust-lang.org/stable/std/intrinsics/fn.unreachable.html "fn std::intrinsics::unreachable")⚠Experimental

Informs the optimizer that this point in the code is not reachable, enabling further optimizations.

[va\_arg](https://doc.rust-lang.org/stable/std/intrinsics/fn.va_arg.html "fn std::intrinsics::va_arg")⚠Experimental

Loads an argument of type `T` from the `va_list` `ap` and increment the argument `ap` points to.

[va\_copy](https://doc.rust-lang.org/stable/std/intrinsics/fn.va_copy.html "fn std::intrinsics::va_copy")Experimental

Duplicates a variable argument list. The returned list is initially at the same position as the one in `src`, but can be advanced independently.

[va\_end](https://doc.rust-lang.org/stable/std/intrinsics/fn.va_end.html "fn std::intrinsics::va_end")⚠Experimental

Destroy the variable argument list `ap` after initialization with `va_start` (part of the desugaring of `...`) or `va_copy`.

[variant\_count](https://doc.rust-lang.org/stable/std/intrinsics/fn.variant_count.html "fn std::intrinsics::variant_count")Experimental

Returns the number of variants of the type `T` cast to a `usize`; if `T` has no variants, returns `0`. Uninhabited variants will be counted.

[volatile\_copy\_memory](https://doc.rust-lang.org/stable/std/intrinsics/fn.volatile_copy_memory.html "fn std::intrinsics::volatile_copy_memory")⚠Experimental

Equivalent to the appropriate `llvm.memmove.p0i8.0i8.*` intrinsic, with a size of `count * size_of::<T>()` and an alignment of `align_of::<T>()`.

[volatile\_copy\_nonoverlapping\_memory](https://doc.rust-lang.org/stable/std/intrinsics/fn.volatile_copy_nonoverlapping_memory.html "fn std::intrinsics::volatile_copy_nonoverlapping_memory")⚠Experimental

Equivalent to the appropriate `llvm.memcpy.p0i8.0i8.*` intrinsic, with a size of `count` * `size_of::<T>()` and an alignment of `align_of::<T>()`.

[volatile\_load](https://doc.rust-lang.org/stable/std/intrinsics/fn.volatile_load.html "fn std::intrinsics::volatile_load")⚠Experimental

Performs a volatile load from the `src` pointer.

[volatile\_set\_memory](https://doc.rust-lang.org/stable/std/intrinsics/fn.volatile_set_memory.html "fn std::intrinsics::volatile_set_memory")⚠Experimental

Equivalent to the appropriate `llvm.memset.p0i8.*` intrinsic, with a size of `count * size_of::<T>()` and an alignment of `align_of::<T>()`.

[volatile\_store](https://doc.rust-lang.org/stable/std/intrinsics/fn.volatile_store.html "fn std::intrinsics::volatile_store")⚠Experimental

Performs a volatile store to the `dst` pointer.

[vtable\_align](https://doc.rust-lang.org/stable/std/intrinsics/fn.vtable_align.html "fn std::intrinsics::vtable_align")⚠Experimental

The intrinsic will return the alignment stored in that vtable.

[vtable\_size](https://doc.rust-lang.org/stable/std/intrinsics/fn.vtable_size.html "fn std::intrinsics::vtable_size")⚠Experimental

The intrinsic will return the size stored in that vtable.

[wrapping\_add](https://doc.rust-lang.org/stable/std/intrinsics/fn.wrapping_add.html "fn std::intrinsics::wrapping_add")Experimental

Returns (a + b) mod 2N, where N is the width of T in bits.

[wrapping\_mul](https://doc.rust-lang.org/stable/std/intrinsics/fn.wrapping_mul.html "fn std::intrinsics::wrapping_mul")Experimental

Returns (a * b) mod 2N, where N is the width of T in bits.

[wrapping\_sub](https://doc.rust-lang.org/stable/std/intrinsics/fn.wrapping_sub.html "fn std::intrinsics::wrapping_sub")Experimental

Returns (a - b) mod 2N, where N is the width of T in bits.

[write\_via\_move](https://doc.rust-lang.org/stable/std/intrinsics/fn.write_via_move.html "fn std::intrinsics::write_via_move")⚠Experimental

This is an implementation detail of [`crate::ptr::write`](https://doc.rust-lang.org/stable/std/ptr/fn.write.html "fn std::ptr::write") and should not be used anywhere else. See its comments for why this exists.