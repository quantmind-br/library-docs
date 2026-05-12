---
title: is_x86_feature_detected in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.is_x86_feature_detected.html
source: crawler
fetched_at: 2026-05-06T21:28:40.171556333-03:00
rendered_js: false
word_count: 194
summary: This document describes the is_x86_feature_detected macro, which allows Rust programs to determine the availability of specific x86 CPU features at runtime.
tags:
    - rust
    - cpu-features
    - runtime-detection
    - x86
    - architecture
    - macro
category: api
---

## Macro is\_x86\_feature\_detected

1.27.0 · [Source](https://doc.rust-lang.org/stable/src/std_detect/detect/arch/x86.rs.html#18-280)

```rust
macro_rules! is_x86_feature_detected {
    ("aes") => { ... };
    ("pclmulqdq") => { ... };
    ("rdrand") => { ... };
    ("rdseed") => { ... };
    ("tsc") => { ... };
    ("mmx") => { ... };
    ("sse") => { ... };
    ("sse2") => { ... };
    ("sse3") => { ... };
    ("ssse3") => { ... };
    ("sse4.1") => { ... };
    ("sse4.2") => { ... };
    ("sse4a") => { ... };
    ("sha") => { ... };
    ("avx") => { ... };
    ("avx2") => { ... };
    ("sha512") => { ... };
    ("sm3") => { ... };
    ("sm4") => { ... };
    ("avx512f") => { ... };
    ("avx512cd") => { ... };
    ("avx512er") => { ... };
    ("avx512pf") => { ... };
    ("avx512bw") => { ... };
    ("avx512dq") => { ... };
    ("avx512vl") => { ... };
    ("avx512ifma") => { ... };
    ("avx512vbmi") => { ... };
    ("avx512vpopcntdq") => { ... };
    ("avx512vbmi2") => { ... };
    ("gfni") => { ... };
    ("vaes") => { ... };
    ("vpclmulqdq") => { ... };
    ("avx512vnni") => { ... };
    ("avx512bitalg") => { ... };
    ("avx512bf16") => { ... };
    ("avx512vp2intersect") => { ... };
    ("avx512fp16") => { ... };
    ("avxifma") => { ... };
    ("avxneconvert") => { ... };
    ("avxvnni") => { ... };
    ("avxvnniint16") => { ... };
    ("avxvnniint8") => { ... };
    ("amx-tile") => { ... };
    ("amx-int8") => { ... };
    ("amx-bf16") => { ... };
    ("amx-fp16") => { ... };
    ("amx-complex") => { ... };
    ("amx-avx512") => { ... };
    ("amx-fp8") => { ... };
    ("amx-movrs") => { ... };
    ("amx-tf32") => { ... };
    ("apxf") => { ... };
    ("avx10.1") => { ... };
    ("avx10.2") => { ... };
    ("f16c") => { ... };
    ("fma") => { ... };
    ("bmi1") => { ... };
    ("bmi2") => { ... };
    ("lzcnt") => { ... };
    ("tbm") => { ... };
    ("popcnt") => { ... };
    ("fxsr") => { ... };
    ("xsave") => { ... };
    ("xsaveopt") => { ... };
    ("xsaves") => { ... };
    ("xsavec") => { ... };
    ("cmpxchg16b") => { ... };
    ("kl") => { ... };
    ("widekl") => { ... };
    ("adx") => { ... };
    ("rtm") => { ... };
    ("movbe") => { ... };
    ("movrs") => { ... };
    ("ermsb") => { ... };
    ("xop") => { ... };
    ("abm") => { ... };
    ("avx512gfni") => { ... };
    ("avx512vaes") => { ... };
    ("avx512vpclmulqdq") => { ... };
    ($t:tt,) => { ... };
    ($t:tt) => { ... };
}
```

Expand description

Check for the presence of a CPU feature at runtime.

When the feature is known to be enabled at compile time (e.g. via `-Ctarget-feature`) the macro expands to `true`.

Runtime detection currently relies mostly on the `cpuid` instruction.

This macro only takes one argument which is a string literal of the feature being tested for. The feature names supported are the lowercase versions of the ones defined by Intel in [their documentation](https://software.intel.com/sites/landingpage/IntrinsicsGuide).

### [§](#supported-arguments)Supported arguments

This macro supports the same names that `#[target_feature]` supports. Unlike `#[target_feature]`, however, this macro does not support names separated with a comma. Instead testing for multiple features must be done through separate macro invocations for now.

Supported arguments are:

- `"aes"`
- `"pclmulqdq"`
- `"rdrand"`
- `"rdseed"`
- `"tsc"`
- `"mmx"`
- `"sse"`
- `"sse2"`
- `"sse3"`
- `"ssse3"`
- `"sse4.1"`
- `"sse4.2"`
- `"sse4a"`
- `"sha"`
- `"avx"`
- `"avx2"`
- `"sha512"`
- `"sm3"`
- `"sm4"`
- `"avx512f"`
- `"avx512cd"`
- `"avx512er"`
- `"avx512pf"`
- `"avx512bw"`
- `"avx512dq"`
- `"avx512vl"`
- `"avx512ifma"`
- `"avx512vbmi"`
- `"avx512vpopcntdq"`
- `"avx512vbmi2"`
- `"gfni"`
- `"vaes"`
- `"vpclmulqdq"`
- `"avx512vnni"`
- `"avx512bitalg"`
- `"avx512bf16"`
- `"avx512vp2intersect"`
- `"avx512fp16"`
- `"avxvnni"`
- `"avxifma"`
- `"avxneconvert"`
- `"avxvnniint8"`
- `"avxvnniint16"`
- `"amx-tile"`
- `"amx-int8"`
- `"amx-bf16"`
- `"amx-fp16"`
- `"amx-complex"`
- `"amx-avx512"`
- `"amx-fp8"`
- `"amx-movrs"`
- `"amx-tf32"`
- `"f16c"`
- `"fma"`
- `"bmi1"`
- `"bmi2"`
- `"abm"`
- `"lzcnt"`
- `"tbm"`
- `"popcnt"`
- `"fxsr"`
- `"xsave"`
- `"xsaveopt"`
- `"xsaves"`
- `"xsavec"`
- `"cmpxchg16b"`
- `"kl"`
- `"widekl"`
- `"adx"`
- `"rtm"`
- `"movbe"`
- `"ermsb"`
- `"movrs"`
- `"xop"`