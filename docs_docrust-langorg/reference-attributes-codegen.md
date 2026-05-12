---
title: Code generation - The Rust Reference
url: https://doc.rust-lang.org/reference/attributes/codegen.html#the-inline-attribute
source: crawler
fetched_at: 2026-05-06T21:38:57.778936276-03:00
rendered_js: false
word_count: 3331
summary: This document describes Rust's code generation attributes, specifically focusing on how developers can use 'inline', 'cold', and 'naked' attributes to influence compiler behavior and performance optimizations.
tags:
    - rust
    - compiler-attributes
    - code-generation
    - performance-optimization
    - inline
    - naked-functions
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Code generation attributes](#code-generation-attributes)

The following [attributes](https://doc.rust-lang.org/reference/attributes.html) are used for controlling code generation.

### [The `inline` attribute](#the-inline-attribute)

The *`inline` [attribute](https://doc.rust-lang.org/reference/attributes.html)* suggests whether a copy of the attributed function’s code should be placed in the caller rather than generating a call to the function.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
#[inline]
pub fn example1() {}

#[inline(always)]
pub fn example2() {}

#[inline(never)]
pub fn example3() {}
}
> ```

> Note
> 
> `rustc` automatically inlines functions when doing so seems worthwhile. Use this attribute carefully as poor decisions about what to inline can slow down programs.

The syntax for the `inline` attribute is:

**Syntax**  
[InlineAttribute](https://doc.rust-lang.org/reference/attributes/codegen.html#railroad-InlineAttribute) →  
      inline ( always )  
    | inline ( never )  
    | inline

The `inline` attribute may only be applied to functions with [bodies](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn.body) — [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure), [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), [free functions](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn), [associated functions](https://doc.rust-lang.org/reference/items/associated-items.html#r-items.associated.fn) in an [inherent impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.inherent) or [trait impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.trait), and associated functions in a [trait definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits) when those functions have a [default definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.associated-item-decls) .

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> Note
> 
> Though the attribute can be applied to [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure) and [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), the usefulness of this is limited as we do not yet support attributes on expressions.
> 
> ```rust
> #![allow(unused)]
fn main() {
// We allow attributes on statements.
#[inline] || (); // OK
#[inline] async {}; // OK
}
> ```
> 
> ```rust
> #![allow(unused)]
fn main() {
// We don't yet allow attributes on expressions.
let f = #[inline] || (); // ERROR
}
> ```

Only the first use of `inline` on a function has effect.

> Note
> 
> `rustc` lints against any use following the first. This may become an error in the future.

The `inline` attribute supports these modes:

- `#[inline]` *suggests* performing inline expansion.
- `#[inline(always)]` *suggests* that inline expansion should always be performed.
- `#[inline(never)]` *suggests* that inline expansion should never be performed.

> Note
> 
> In every form the attribute is a hint. The compiler may ignore it.

When `inline` is applied to a function in a [trait](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits), it applies only to the code of the [default definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.associated-item-decls).

When `inline` is applied to an [async function](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn.async) or [async closure](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure.async), it applies only to the code of the generated `poll` function.

The `inline` attribute is ignored if the function is externally exported with [`no_mangle`](https://doc.rust-lang.org/reference/abi.html#r-abi.no_mangle) or [`export_name`](https://doc.rust-lang.org/reference/abi.html#r-abi.export_name).

### [The `cold` attribute](#the-cold-attribute)

The *`cold` [attribute](https://doc.rust-lang.org/reference/attributes.html)* suggests that the attributed function is unlikely to be called which may help the compiler produce better code.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
#[cold]
pub fn example() {}
}
> ```

The `cold` attribute uses the [MetaWord](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaWord) syntax.

The `cold` attribute may only be applied to functions with [bodies](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn.body) — [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure), [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), [free functions](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn), [associated functions](https://doc.rust-lang.org/reference/items/associated-items.html#r-items.associated.fn) in an [inherent impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.inherent) or [trait impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.trait), and associated functions in a [trait definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits) when those functions have a [default definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.associated-item-decls) .

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> Note
> 
> Though the attribute can be applied to [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure) and [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), the usefulness of this is limited as we do not yet support attributes on expressions.

Only the first use of `cold` on a function has effect.

> Note
> 
> `rustc` lints against any use following the first. This may become an error in the future.

When `cold` is applied to a function in a [trait](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits), it applies only to the code of the [default definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.associated-item-decls).

## [The `naked` attribute](#the-naked-attribute)

The *`naked` [attribute](https://doc.rust-lang.org/reference/attributes.html)* prevents the compiler from emitting a function prologue and epilogue for the attributed function.

[\[attributes.codegen.naked.body\]](#r-attributes.codegen.naked.body "attributes.codegen.naked.body")

The [function body](https://doc.rust-lang.org/reference/items/functions.html#function-body) must consist of exactly one [`naked_asm!`](https://doc.rust-lang.org/reference/inline-assembly.html) macro invocation.

No function prologue or epilogue is generated for the attributed function. The assembly code in the `naked_asm!` block constitutes the full body of a naked function.

The `naked` attribute is an [unsafe attribute](https://doc.rust-lang.org/reference/attributes.html#r-attributes.safety). Annotating a function with `#[unsafe(naked)]` comes with the safety obligation that the body must respect the function’s calling convention, uphold its signature, and either return or diverge (i.e., not fall through past the end of the assembly code).

The assembly code may assume that the call stack and register state are valid on entry as per the signature and calling convention of the function.

The assembly code may not be duplicated by the compiler except when monomorphizing polymorphic functions.

> Note
> 
> Guaranteeing when the assembly code may or may not be duplicated is important for naked functions that define symbols.

The [`unused_variables`](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-variables) lint is suppressed within naked functions.

The [`inline`](#the-inline-attribute) attribute cannot by applied to a naked function.

The [`track_caller`](#the-track_caller-attribute) attribute cannot be applied to a naked function.

The [testing attributes](https://doc.rust-lang.org/reference/attributes/testing.html) cannot be applied to a naked function.

## [The `no_builtins` attribute](#the-no_builtins-attribute)

The *`no_builtins` [attribute](https://doc.rust-lang.org/reference/attributes.html)* disables optimization of certain code patterns related to calls to library functions that are assumed to exist.

> Example
> 
> ```rust
> #![allow(unused)]
#![no_builtins]
fn main() {
}
> ```

The `no_builtins` attribute uses the [MetaWord](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaWord) syntax.

The `no_builtins` attribute can only be applied to the crate root.

Only the first use of the `no_builtins` attribute has effect.

> Note
> 
> `rustc` lints against any use following the first.

## [The `target_feature` attribute](#the-target_feature-attribute)

The *`target_feature` [attribute](https://doc.rust-lang.org/reference/attributes.html)* may be applied to a function to enable code generation of that function for specific platform architecture features. It uses the [MetaListNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaListNameValueStr) syntax with a single key of `enable` whose value is a string of comma-separated feature names to enable.

```rust
#![allow(unused)]
fn main() {
#[cfg(target_feature = "avx2")]
#[target_feature(enable = "avx2")]
fn foo_avx2() {}
}
```

Each [target architecture](https://doc.rust-lang.org/reference/conditional-compilation.html#target_arch) has a set of features that may be enabled. It is an error to specify a feature for a target architecture that the crate is not being compiled for.

Closures defined within a `target_feature`-annotated function inherit the attribute from the enclosing function.

It is [undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) to call a function that is compiled with a feature that is not supported on the current platform the code is running on, *except* if the platform explicitly documents this to be safe.

The following restrictions apply unless otherwise specified by the platform rules below:

- Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be safely called within a caller that enables all the `target_feature`s that the callee enables. This restriction does not apply in an `unsafe` context.
- Safe `#[target_feature]` functions (and closures that inherit the attribute) can only be coerced to *safe* function pointers in contexts that enable all the `target_feature`s that the coercee enables. This restriction does not apply to `unsafe` function pointers.

Implicitly enabled features are included in this rule. For example an `sse2` function can call ones marked with `sse`.

```rust
#![allow(unused)]
fn main() {
#[cfg(target_feature = "sse2")] {
#[target_feature(enable = "sse")]
fn foo_sse() {}

fn bar() {
    // Calling `foo_sse` here is unsafe, as we must ensure that SSE is
    // available first, even if `sse` is enabled by default on the target
    // platform or manually enabled as compiler flags.
    unsafe {
        foo_sse();
    }
}

#[target_feature(enable = "sse")]
fn bar_sse() {
    // Calling `foo_sse` here is safe.
    foo_sse();
    || foo_sse();
}

#[target_feature(enable = "sse2")]
fn bar_sse2() {
    // Calling `foo_sse` here is safe because `sse2` implies `sse`.
    foo_sse();
}
}
}
```

A function with a `#[target_feature]` attribute *never* implements the `Fn` family of traits, although closures inheriting features from the enclosing function do.

The `#[target_feature]` attribute is not allowed on the following places:

- [the `main` function](https://doc.rust-lang.org/reference/crates-and-source-files.html#r-crate.main)
- a [`panic_handler` function](https://doc.rust-lang.org/reference/panic.html#r-panic.panic_handler)
- safe trait methods
- safe default functions in traits

Functions marked with `target_feature` are not inlined into a context that does not support the given features. The `#[inline(always)]` attribute may not be used with a `target_feature` attribute.

### [Available features](#available-features)

The following is a list of the available feature names.

#### [`x86` or `x86_64`](#x86-or-x86_64)

Executing code with unsupported features is undefined behavior on this platform. Hence on this platform usage of `#[target_feature]` functions follows the [above restrictions](https://doc.rust-lang.org/reference/attributes/codegen.html#r-attributes.codegen.target_feature.safety-restrictions).

FeatureImplicitly EnablesDescription `adx`[ADX](https://en.wikipedia.org/wiki/Intel_ADX) — Multi-Precision Add-Carry Instruction Extensions `aes``sse2`[AES](https://en.wikipedia.org/wiki/AES_instruction_set) — Advanced Encryption Standard `avx``sse4.2`[AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) — Advanced Vector Extensions `avx2``avx`[AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX2) — Advanced Vector Extensions 2 `avx512bf16``avx512bw`[AVX512-BF16](https://en.wikipedia.org/wiki/AVX-512#BF16) — Advanced Vector Extensions 512-bit - Bfloat16 Extensions `avx512bitalg``avx512bw`[AVX512-BITALG](https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG) — Advanced Vector Extensions 512-bit - Bit Algorithms `avx512bw``avx512f`[AVX512-BW](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) — Advanced Vector Extensions 512-bit - Byte and Word Instructions `avx512cd``avx512f`[AVX512-CD](https://en.wikipedia.org/wiki/AVX-512#Conflict_detection) — Advanced Vector Extensions 512-bit - Conflict Detection Instructions `avx512dq``avx512f`[AVX512-DQ](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) — Advanced Vector Extensions 512-bit - Doubleword and Quadword Instructions `avx512f``avx2`, `fma`, `f16c`[AVX512-F](https://en.wikipedia.org/wiki/AVX-512) — Advanced Vector Extensions 512-bit - Foundation `avx512fp16``avx512bw`[AVX512-FP16](https://en.wikipedia.org/wiki/AVX-512#FP16) — Advanced Vector Extensions 512-bit - Float16 Extensions `avx512ifma``avx512f`[AVX512-IFMA](https://en.wikipedia.org/wiki/AVX-512#IFMA) — Advanced Vector Extensions 512-bit - Integer Fused Multiply Add `avx512vbmi``avx512bw`[AVX512-VBMI](https://en.wikipedia.org/wiki/AVX-512#BW,_DQ_and_VBMI) — Advanced Vector Extensions 512-bit - Vector Byte Manipulation Instructions `avx512vbmi2``avx512bw`[AVX512-VBMI2](https://en.wikipedia.org/wiki/AVX-512#VBMI2) — Advanced Vector Extensions 512-bit - Vector Byte Manipulation Instructions 2 `avx512vl``avx512f`[AVX512-VL](https://en.wikipedia.org/wiki/AVX-512) — Advanced Vector Extensions 512-bit - Vector Length Extensions `avx512vnni``avx512f`[AVX512-VNNI](https://en.wikipedia.org/wiki/AVX-512#VNNI) — Advanced Vector Extensions 512-bit - Vector Neural Network Instructions `avx512vp2intersect``avx512f`[AVX512-VP2INTERSECT](https://en.wikipedia.org/wiki/AVX-512#VP2INTERSECT) — Advanced Vector Extensions 512-bit - Vector Pair Intersection to a Pair of Mask Registers `avx512vpopcntdq``avx512f`[AVX512-VPOPCNTDQ](https://en.wikipedia.org/wiki/AVX-512#VPOPCNTDQ_and_BITALG) — Advanced Vector Extensions 512-bit - Vector Population Count Instruction `avxifma``avx2`[AVX-IFMA](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA) — Advanced Vector Extensions - Integer Fused Multiply Add `avxneconvert``avx2`[AVX-NE-CONVERT](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA) — Advanced Vector Extensions - No-Exception Floating-Point conversion Instructions `avxvnni``avx2`[AVX-VNNI](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions `avxvnniint16``avx2`[AVX-VNNI-INT16](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions with 16-bit Integers `avxvnniint8``avx2`[AVX-VNNI-INT8](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX-VNNI,_AVX-IFMA) — Advanced Vector Extensions - Vector Neural Network Instructions with 8-bit Integers `bmi1`[BMI1](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets) — Bit Manipulation Instruction Sets `bmi2`[BMI2](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#BMI2) — Bit Manipulation Instruction Sets 2 `cmpxchg16b`[`cmpxchg16b`](https://www.felixcloutier.com/x86/cmpxchg8b:cmpxchg16b) — Compares and exchange 16 bytes (128 bits) of data atomically `f16c``avx`[F16C](https://en.wikipedia.org/wiki/F16C) — 16-bit floating point conversion instructions `fma``avx`[FMA3](https://en.wikipedia.org/wiki/FMA_instruction_set) — Three-operand fused multiply-add `fxsr`[`fxsave`](https://www.felixcloutier.com/x86/fxsave) and [`fxrstor`](https://www.felixcloutier.com/x86/fxrstor) — Save and restore x87 FPU, MMX Technology, and SSE State `gfni``sse2`[GFNI](https://en.wikipedia.org/wiki/AVX-512#GFNI) — Galois Field New Instructions `kl``sse2`[KEYLOCKER](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions) — Intel Key Locker Instructions `lzcnt`[`lzcnt`](https://www.felixcloutier.com/x86/lzcnt) — Leading zeros count `movbe`[`movbe`](https://www.felixcloutier.com/x86/movbe) — Move data after swapping bytes `pclmulqdq``sse2`[`pclmulqdq`](https://www.felixcloutier.com/x86/pclmulqdq) — Packed carry-less multiplication quadword `popcnt`[`popcnt`](https://www.felixcloutier.com/x86/popcnt) — Count of bits set to 1 `rdrand`[`rdrand`](https://en.wikipedia.org/wiki/RdRand) — Read random number `rdseed`[`rdseed`](https://en.wikipedia.org/wiki/RdRand) — Read random seed `sha``sse2`[SHA](https://en.wikipedia.org/wiki/Intel_SHA_extensions) — Secure Hash Algorithm `sha512``avx2`[SHA512](https://en.wikipedia.org/wiki/Intel_SHA_extensions) — Secure Hash Algorithm with 512-bit digest `sm3``avx`[SM3](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions) — ShangMi 3 Hash Algorithm `sm4``avx2`[SM4](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_SHA_and_SM3_instructions) — ShangMi 4 Cipher Algorithm `sse`[SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions) — Streaming SIMD Extensions `sse2``sse`[SSE2](https://en.wikipedia.org/wiki/SSE2) — Streaming SIMD Extensions 2 `sse3``sse2`[SSE3](https://en.wikipedia.org/wiki/SSE3) — Streaming SIMD Extensions 3 `sse4.1``ssse3`[SSE4.1](https://en.wikipedia.org/wiki/SSE4#SSE4.1) — Streaming SIMD Extensions 4.1 `sse4.2``sse4.1`[SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2) — Streaming SIMD Extensions 4.2 `sse4a``sse3`[SSE4a](https://en.wikipedia.org/wiki/SSE4#SSE4a) — Streaming SIMD Extensions 4a `ssse3``sse3`[SSSE3](https://en.wikipedia.org/wiki/SSSE3) — Supplemental Streaming SIMD Extensions 3 `tbm`[TBM](https://en.wikipedia.org/wiki/X86_Bit_manipulation_instruction_set#TBM_%28Trailing_Bit_Manipulation%29) — Trailing Bit Manipulation `vaes``avx2`, `aes`[VAES](https://en.wikipedia.org/wiki/AVX-512#VAES) — Vector AES Instructions `vpclmulqdq``avx`, `pclmulqdq`[VPCLMULQDQ](https://en.wikipedia.org/wiki/AVX-512#VPCLMULQDQ) — Vector Carry-less multiplication of Quadwords `widekl``kl`[KEYLOCKER\_WIDE](https://en.wikipedia.org/wiki/List_of_x86_cryptographic_instructions#Intel_Key_Locker_instructions) — Intel Wide Keylocker Instructions `xsave`[`xsave`](https://www.felixcloutier.com/x86/xsave) — Save processor extended states `xsavec`[`xsavec`](https://www.felixcloutier.com/x86/xsavec) — Save processor extended states with compaction `xsaveopt`[`xsaveopt`](https://www.felixcloutier.com/x86/xsaveopt) — Save processor extended states optimized `xsaves`[`xsaves`](https://www.felixcloutier.com/x86/xsaves) — Save processor extended states supervisor

#### [`aarch64`](#aarch64)

On this platform the usage of `#[target_feature]` functions follows the [above restrictions](https://doc.rust-lang.org/reference/attributes/codegen.html#r-attributes.codegen.target_feature.safety-restrictions).

Further documentation on these features can be found in the [ARM Architecture Reference Manual](https://developer.arm.com/documentation/ddi0487/latest), or elsewhere on [developer.arm.com](https://developer.arm.com).

> Note
> 
> The following pairs of features should both be marked as enabled or disabled together if used:
> 
> - `paca` and `pacg`, which LLVM currently implements as one feature.

FeatureImplicitly EnablesFeature Name `aes``neon`FEAT\_AES & FEAT\_PMULL — Advanced SIMD AES & PMULL instructions `bf16`FEAT\_BF16 — BFloat16 instructions `bti`FEAT\_BTI — Branch Target Identification `crc`FEAT\_CRC — CRC32 checksum instructions `dit`FEAT\_DIT — Data Independent Timing instructions `dotprod``neon`FEAT\_DotProd — Advanced SIMD Int8 dot product instructions `dpb`FEAT\_DPB — Data cache clean to point of persistence `dpb2``dpb`FEAT\_DPB2 — Data cache clean to point of deep persistence `f32mm``sve`FEAT\_F32MM — SVE single-precision FP matrix multiply instruction `f64mm``sve`FEAT\_F64MM — SVE double-precision FP matrix multiply instruction `fcma``neon`FEAT\_FCMA — Floating point complex number support `fhm``fp16`FEAT\_FHM — Half-precision FP FMLAL instructions `flagm`FEAT\_FLAGM — Conditional flag manipulation `fp16``neon`FEAT\_FP16 — Half-precision FP data processing `frintts`FEAT\_FRINTTS — Floating-point to int helper instructions `i8mm`FEAT\_I8MM — Int8 Matrix Multiplication `jsconv``neon`FEAT\_JSCVT — JavaScript conversion instruction `lor`FEAT\_LOR — Limited Ordering Regions extension `lse`FEAT\_LSE — Large System Extensions `mte`FEAT\_MTE & FEAT\_MTE2 — Memory Tagging Extension `neon`FEAT\_AdvSimd & FEAT\_FP — Floating Point and Advanced SIMD extension `paca`FEAT\_PAUTH — Pointer Authentication (address authentication) `pacg`FEAT\_PAUTH — Pointer Authentication (generic authentication) `pan`FEAT\_PAN — Privileged Access-Never extension `pmuv3`FEAT\_PMUv3 — Performance Monitors extension (v3) `rand`FEAT\_RNG — Random Number Generator `ras`FEAT\_RAS & FEAT\_RASv1p1 — Reliability, Availability and Serviceability extension `rcpc`FEAT\_LRCPC — Release consistent Processor Consistent `rcpc2``rcpc`FEAT\_LRCPC2 — RcPc with immediate offsets `rdm``neon`FEAT\_RDM — Rounding Double Multiply accumulate `sb`FEAT\_SB — Speculation Barrier `sha2``neon`FEAT\_SHA1 & FEAT\_SHA256 — Advanced SIMD SHA instructions `sha3``sha2`FEAT\_SHA512 & FEAT\_SHA3 — Advanced SIMD SHA instructions `sm4``neon`FEAT\_SM3 & FEAT\_SM4 — Advanced SIMD SM3/4 instructions `spe`FEAT\_SPE — Statistical Profiling Extension `ssbs`FEAT\_SSBS & FEAT\_SSBS2 — Speculative Store Bypass Safe `sve``neon`FEAT\_SVE — Scalable Vector Extension `sve2``sve`FEAT\_SVE2 — Scalable Vector Extension 2 `sve2-aes``sve2`, `aes`FEAT\_SVE\_AES & FEAT\_SVE\_PMULL128 — SVE AES instructions `sve2-bitperm``sve2`FEAT\_SVE2\_BitPerm — SVE Bit Permute `sve2-sha3``sve2`, `sha3`FEAT\_SVE2\_SHA3 — SVE SHA3 instructions `sve2-sm4``sve2`, `sm4`FEAT\_SVE2\_SM4 — SVE SM4 instructions `tme`FEAT\_TME — Transactional Memory Extension `vh`FEAT\_VHE — Virtualization Host Extensions

#### [`loongarch`](#loongarch)

On this platform the usage of `#[target_feature]` functions follows the [above restrictions](https://doc.rust-lang.org/reference/attributes/codegen.html#r-attributes.codegen.target_feature.safety-restrictions).

FeatureImplicitly EnablesDescription `f`[F](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-fp_sp) — Single-precision float-point instructions `d``f`[D](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-fp_dp) — Double-precision float-point instructions `frecipe`[FRECIPE](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-frecipe) — Reciprocal approximation instructions `lasx``lsx`[LASX](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lasx) — 256-bit vector instructions `lbt`[LBT](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lbt_x86) — Binary translation instructions `lsx``d`[LSX](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lsx) — 128-bit vector instructions `lvz`[LVZ](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html#cpucfg-lvz) — Virtualization instructions

#### [`riscv32` or `riscv64`](#riscv32-or-riscv64)

On this platform the usage of `#[target_feature]` functions follows the [above restrictions](https://doc.rust-lang.org/reference/attributes/codegen.html#r-attributes.codegen.target_feature.safety-restrictions).

Further documentation on these features can be found in their respective specification. Many specifications are described in the [RISC-V ISA Manual](https://github.com/riscv/riscv-isa-manual), [version 20250508](https://github.com/riscv/riscv-isa-manual/tree/20250508), or in another manual hosted on the [RISC-V GitHub Account](https://github.com/riscv).

FeatureImplicitly EnablesDescription `a``zaamo`, `zalrsc`[A](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc) — Atomic instructions `b``zba`, `zbc`, `zbs`[B](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Bit Manipulation instructions `c``zca`[C](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/c-st-ext.adoc) — Compressed instructions `m`[M](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/m-st-ext.adoc) — Integer Multiplication and Division instructions `za64rs``za128rs`[Za64rs](https://github.com/riscv/riscv-profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc) — Platform Behavior: Naturally aligned Reservation sets with ≦ 64 Bytes `za128rs`[Za128rs](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Naturally aligned Reservation sets with ≦ 128 Bytes `zaamo`[Zaamo](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc) — Atomic Memory Operation instructions `zabha``zaamo`[Zabha](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zabha.adoc) — Byte and Halfword Atomic Memory Operation instructions `zacas``zaamo`[Zacas](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zacas.adoc) — Atomic Compare-and-Swap (CAS) instructions `zalrsc`[Zalrsc](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/a-st-ext.adoc) — Load-Reserved/Store-Conditional instructions `zama16b`[Zama16b](https://github.com/riscv/riscv-profiles/blob/rva23-rvb23-ratified/src/rva23-profile.adoc) — Platform Behavior: Misaligned loads, stores, and AMOs to main memory regions that do not cross a naturally aligned 16-byte boundary are atomic `zawrs`[Zawrs](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zawrs.adoc) — Wait-on-Reservation-Set instructions `zba`[Zba](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Address Generation instructions `zbb`[Zbb](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Basic bit-manipulation `zbc``zbkc`[Zbc](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Carry-less multiplication `zbkb`[Zbkb](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Bit Manipulation Instructions for Cryptography `zbkc`[Zbkc](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Carry-less multiplication for Cryptography `zbkx`[Zbkx](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Crossbar permutations `zbs`[Zbs](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/b-st-ext.adoc) — Single-bit instructions `zca`[Zca](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zc.adoc) — Compressed instructions: integer part subset `zcb``zca`[Zcb](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zc.adoc) — Simple Code-size Saving Compressed instructions `zcmop``zca`[Zcmop](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zimop.adoc) — Compressed May-Be-Operations `zic64b`[Zic64b](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Naturally aligned 64 byte Cache blocks `zicbom`[Zicbom](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Management instructions `zicbop`[Zicbop](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Prefetch Hint instructions `zicboz`[Zicboz](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/cmo.adoc) — Cache-Block Zero instruction `ziccamoa`[Ziccamoa](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports all basic atomic operations `ziccif`[Ziccif](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports instruction fetch and fetches of naturally aligned power-of-2 sizes up to `min(ILEN,XLEN)` are atomic `zicclsm`[Zicclsm](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory supports misaligned load/store accesses `ziccrse`[Ziccrse](https://github.com/riscv/riscv-profiles/blob/v1.0/profiles.adoc) — Platform Behavior: Cacheable and Coherent Main memory guarantees eventual success on LR/SC sequences `zicntr``zicsr`[Zicntr](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/counters.adoc) — Base Counters and Timers `zicond`[Zicond](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicond.adoc) — Integer Conditional Operation instructions `zicsr`[Zicsr](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zicsr.adoc) — Control and Status Register (CSR) instructions `zifencei`[Zifencei](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zifencei.adoc) — Instruction-Fetch Fence instruction `zihintntl`[Zihintntl](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintntl.adoc) — Non-Temporal Locality Hint instructions `zihintpause`[Zihintpause](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zihintpause.adoc) — Pause Hint instruction `zihpm``zicsr`[Zihpm](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/counters.adoc) — Hardware Performance Counters `zimop`[Zimop](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/zimop.adoc) — May-Be-Operations `zk``zkn`, `zkr`, `zks`, `zkt`, `zbkb`, `zbkc`, `zkbx`[Zk](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — Scalar Cryptography `zkn``zknd`, `zkne`, `zknh`, `zbkb`, `zbkc`, `zkbx`[Zkn](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Algorithm suite extension `zknd`[Zknd](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: AES Decryption `zkne`[Zkne](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: AES Encryption `zknh`[Zknh](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — NIST Suite: Hash Function Instructions `zkr`[Zkr](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — Entropy Source Extension `zks``zksed`, `zksh`, `zbkb`, `zbkc`, `zkbx`[Zks](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — ShangMi Algorithm Suite `zksed`[Zksed](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — ShangMi Suite: SM4 Block Cipher Instructions `zksh`[Zksh](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — ShangMi Suite: SM3 Hash Function Instructions `zkt`[Zkt](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/scalar-crypto.adoc) — Data Independent Execution Latency Subset `ztso`[Ztso](https://github.com/riscv/riscv-isa-manual/blob/20250508/src/ztso-st-ext.adoc) — Total Store Ordering

#### [`wasm32` or `wasm64`](#wasm32-or-wasm64)

Safe `#[target_feature]` functions may always be used in safe contexts on Wasm platforms. It is impossible to cause undefined behavior via the `#[target_feature]` attribute because attempting to use instructions unsupported by the Wasm engine will fail at load time without the risk of being interpreted in a way different from what the compiler expected.

#### [`s390x`](#s390x)

On `s390x` targets, use of functions with the `#[target_feature]` attribute follows the [above restrictions](https://doc.rust-lang.org/reference/attributes/codegen.html#r-attributes.codegen.target_feature.safety-restrictions).

Further documentation on these features can be found in the “Additions to z/Architecture” section of Chapter 1 of the [*z/Architecture Principles of Operation*](https://publibfp.dhe.ibm.com/epubs/pdf/a227832d.pdf).

FeatureImplicitly EnablesDescription `vector`128-bit vector instructions `vector-enhancements-1``vector`vector enhancements 1 `vector-enhancements-2``vector-enhancements-1`vector enhancements 2 `vector-enhancements-3``vector-enhancements-2`vector enhancements 3 `vector-packed-decimal``vector`vector packed-decimal `vector-packed-decimal-enhancement``vector-packed-decimal`vector packed-decimal enhancement `vector-packed-decimal-enhancement-2``vector-packed-decimal-enhancement-2`vector packed-decimal enhancement 2 `vector-packed-decimal-enhancement-3``vector-packed-decimal-enhancement-3`vector packed-decimal enhancement 3 `nnp-assist``vector`nnp assist `miscellaneous-extensions-2`miscellaneous extensions 2 `miscellaneous-extensions-3`miscellaneous extensions 3 `miscellaneous-extensions-4`miscellaneous extensions 4

### [Additional information](#additional-information)

See the [`target_feature` conditional compilation option](https://doc.rust-lang.org/reference/conditional-compilation.html#target_feature) for selectively enabling or disabling compilation of code based on compile-time settings. Note that this option is not affected by the `target_feature` attribute, and is only driven by the features enabled for the entire crate.

Whether a feature is enabled can be checked at runtime using a platform-specific macro from the standard library, for instance [`is_x86_feature_detected`](https://doc.rust-lang.org/std/arch/macro.is_x86_feature_detected.html) or [`is_aarch64_feature_detected`](https://doc.rust-lang.org/std/arch/macro.is_aarch64_feature_detected.html).

> Note
> 
> `rustc` has a default set of features enabled for each target and CPU. The CPU may be chosen with the [`-C target-cpu`](https://doc.rust-lang.org/rustc/codegen-options/index.html#target-cpu) flag. Individual features may be enabled or disabled for an entire crate with the [`-C target-feature`](https://doc.rust-lang.org/rustc/codegen-options/index.html#target-feature) flag.

## [The `track_caller` attribute](#the-track_caller-attribute)

The `track_caller` attribute may be applied to any function with [`"Rust"` ABI](https://doc.rust-lang.org/reference/items/external-blocks.html#abi) with the exception of the entry point `fn main`.

When applied to functions and methods in trait declarations, the attribute applies to all implementations. If the trait provides a default implementation with the attribute, then the attribute also applies to override implementations.

When applied to a function in an `extern` block the attribute must also be applied to any linked implementations, otherwise undefined behavior results. When applied to a function which is made available to an `extern` block, the declaration in the `extern` block must also have the attribute, otherwise undefined behavior results.

### [Behavior](#behavior)

Applying the attribute to a function `f` allows code within `f` to get a hint of the [`Location`](https://doc.rust-lang.org/core/panic/location/struct.Location.html) of the “topmost” tracked call that led to `f`’s invocation. At the point of observation, an implementation behaves as if it walks up the stack from `f`’s frame to find the nearest frame of an *unattributed* function `outer`, and it returns the [`Location`](https://doc.rust-lang.org/core/panic/location/struct.Location.html) of the tracked call in `outer`.

```rust
#![allow(unused)]
fn main() {
#[track_caller]
fn f() {
    println!("{}", std::panic::Location::caller());
}
}
```

> Note
> 
> Because the resulting `Location` is a hint, an implementation may halt its walk up the stack early. See [Limitations](#limitations) for important caveats.

#### [Examples](#examples)

When `f` is called directly by `calls_f`, code in `f` observes its callsite within `calls_f`:

```rust
#![allow(unused)]
fn main() {
#[track_caller]
fn f() {
    println!("{}", std::panic::Location::caller());
}
fn calls_f() {
    f(); // <-- f() prints this location
}
}
```

When `f` is called by another attributed function `g` which is in turn called by `calls_g`, code in both `f` and `g` observes `g`’s callsite within `calls_g`:

```rust
#![allow(unused)]
fn main() {
#[track_caller]
fn f() {
    println!("{}", std::panic::Location::caller());
}
#[track_caller]
fn g() {
    println!("{}", std::panic::Location::caller());
    f();
}

fn calls_g() {
    g(); // <-- g() prints this location twice, once itself and once from f()
}
}
```

When `g` is called by another attributed function `h` which is in turn called by `calls_h`, all code in `f`, `g`, and `h` observes `h`’s callsite within `calls_h`:

```rust
#![allow(unused)]
fn main() {
#[track_caller]
fn f() {
    println!("{}", std::panic::Location::caller());
}
#[track_caller]
fn g() {
    println!("{}", std::panic::Location::caller());
    f();
}
#[track_caller]
fn h() {
    println!("{}", std::panic::Location::caller());
    g();
}

fn calls_h() {
    h(); // <-- prints this location three times, once itself, once from g(), once from f()
}
}
```

And so on.

### [Limitations](#limitations)

This information is a hint and implementations are not required to preserve it.

In particular, coercing a function with `#[track_caller]` to a function pointer creates a shim which appears to observers to have been called at the attributed function’s definition site, losing actual caller information across virtual calls. A common example of this coercion is the creation of a trait object whose methods are attributed.

> Note
> 
> The aforementioned shim for function pointers is necessary because `rustc` implements `track_caller` in a codegen context by appending an implicit parameter to the function ABI, but this would be unsound for an indirect call because the parameter is not a part of the function’s type and a given function pointer type may or may not refer to a function with the attribute. The creation of a shim hides the implicit parameter from callers of the function pointer, preserving soundness.

## [The `instruction_set` attribute](#the-instruction_set-attribute)

The *`instruction_set` [attribute](https://doc.rust-lang.org/reference/attributes.html)* specifies the instruction set that a function will use during code generation. This allows mixing more than one instruction set in a single program.

> Example
> 
> ```rust
> #[instruction_set(arm::a32)]
fn arm_code() {}

#[instruction_set(arm::t32)]
fn thumb_code() {}
> ```

The `instruction_set` attribute uses the [MetaListPaths](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaListPaths) syntax to specify a single path consisting of the architecture family name and instruction set name.

The `instruction_set` attribute may only be applied to functions with [bodies](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn.body) — [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure), [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), [free functions](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn), [associated functions](https://doc.rust-lang.org/reference/items/associated-items.html#r-items.associated.fn) in an [inherent impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.inherent) or [trait impl](https://doc.rust-lang.org/reference/items/implementations.html#r-items.impl.trait), and associated functions in a [trait definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits) when those functions have a [default definition](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.associated-item-decls) .

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

> Note
> 
> Though the attribute can be applied to [closures](https://doc.rust-lang.org/reference/expressions/closure-expr.html#r-expr.closure) and [async blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.async), the usefulness of this is limited as we do not yet support attributes on expressions.

The `instruction_set` attribute may be used only once on a function.

The `instruction_set` attribute may only be used with a target that supports the given value.

When the `instruction_set` attribute is used, any inline assembly in the function must use the specified instruction set instead of the target default.

### [`instruction_set` on ARM](#instruction_set-on-arm)

When targeting the `ARMv4T` and `ARMv5te` architectures, the supported values for `instruction_set` are:

- `arm::a32` — Generate the function as A32 “ARM” code.
- `arm::t32` — Generate the function as T32 “Thumb” code.

If the address of the function is taken as a function pointer, the low bit of the address will depend on the selected instruction set:

- For `arm::a32` (“ARM”), it will be 0.
- For `arm::t32` (“Thumb”), it will be 1.