---
title: f16 - Rust
url: https://doc.rust-lang.org/std/primitive.f16.html
source: crawler
fetched_at: 2026-05-06T21:30:09.358872013-03:00
rendered_js: false
word_count: 7087
summary: This document describes the experimental f16 primitive type in Rust, which implements the IEEE 754-2008 half-precision floating-point format and provides standard mathematical operations.
tags:
    - rust
    - primitive-types
    - floating-point
    - f16
    - experimental-api
    - mathematics
category: reference
---

## Primitive Type f16

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Expand description

A 16-bit floating-point type (specifically, the “binary16” type defined in IEEE 754-2008).

This type is very similar to [`f32`](https://doc.rust-lang.org/std/primitive.f32.html "primitive f32") but has decreased precision because it uses half as many bits. Please see [the documentation for `f32`](https://doc.rust-lang.org/std/primitive.f32.html "primitive f32") or [Wikipedia on half-precision values](https://en.wikipedia.org/wiki/Half-precision_floating-point_format) for more information.

Note that most common platforms will not support `f16` in hardware without enabling extra target features, with the notable exception of Apple Silicon (also known as M1, M2, etc.) processors. Hardware support on x86/x86-64 requires the avx512fp16 or avx10.1 features, while RISC-V requires Zfh, and Arm/AArch64 requires FEAT\_FP16. Usually the fallback implementation will be to use `f32` hardware if it exists, and convert between `f16` and `f32` when performing math.

*[See also the `std::f16::consts` module](https://doc.rust-lang.org/std/f16/consts/index.html "mod std::f16::consts").*

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#19-1046)[§](#impl-f16)

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#52-54)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Raises a number to a floating point power.

Note that this function is special in that it can return non-NaN results for NaN inputs. For example, `f16::powf(f16::NAN, 0.0)` returns `1.0`. However, if an input is a *signaling* NaN, then the result is non-deterministically either a NaN or the result that the corresponding quiet NaN would produce.

##### [§](#unspecified-precision)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples)Examples

```rust
#![feature(f16)]

let x = 2.0_f16;
let abs_difference = (x.powf(2.0) - (x * x)).abs();
assert!(abs_difference <= f16::EPSILON);

assert_eq!(f16::powf(1.0, f16::NAN), 1.0);
assert_eq!(f16::powf(f16::NAN, 0.0), 1.0);
assert_eq!(f16::powf(0.0, 0.0), 1.0);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#84-86)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `e^(self)`, (the exponential function).

##### [§](#unspecified-precision-1)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-1)Examples

```rust
#![feature(f16)]

let one = 1.0f16;
// e^1
let e = one.exp();

// ln(e) - 1 == 0
let abs_difference = (e.ln() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#114-116)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `2^(self)`.

##### [§](#unspecified-precision-2)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-2)Examples

```rust
#![feature(f16)]

let f = 2.0f16;

// 2^2 - 4 == 0
let abs_difference = (f.exp2() - 4.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#159-161)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the natural logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-3)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-3)Examples

```rust
#![feature(f16)]

let one = 1.0f16;
// e^1
let e = one.exp();

// ln(e) - 1 == 0
let abs_difference = (e.ln() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

Non-positive values:

```rust
#![feature(f16)]

assert_eq!(0_f16.ln(), f16::NEG_INFINITY);
assert!((-42_f16).ln().is_nan());
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#206-208)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the logarithm of the number with respect to an arbitrary base.

This returns NaN when the number is negative, and negative infinity when number is zero.

The result might not be correctly rounded owing to implementation details; `self.log2()` can produce more accurate results for base 2, and `self.log10()` can produce more accurate results for base 10.

##### [§](#unspecified-precision-4)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-4)Examples

```rust
#![feature(f16)]

let five = 5.0f16;

// log5(5) - 1 == 0
let abs_difference = (five.log(5.0) - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

Non-positive values:

```rust
#![feature(f16)]

assert_eq!(0_f16.log(10.0), f16::NEG_INFINITY);
assert!((-42_f16).log(10.0).is_nan());
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#249-251)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the base 2 logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-5)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-5)Examples

```rust
#![feature(f16)]

let two = 2.0f16;

// log2(2) - 1 == 0
let abs_difference = (two.log2() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

Non-positive values:

```rust
#![feature(f16)]

assert_eq!(0_f16.log2(), f16::NEG_INFINITY);
assert!((-42_f16).log2().is_nan());
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#292-294)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the base 10 logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-6)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-6)Examples

```rust
#![feature(f16)]

let ten = 10.0f16;

// log10(10) - 1 == 0
let abs_difference = (ten.log10() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

Non-positive values:

```rust
#![feature(f16)]

assert_eq!(0_f16.log10(), f16::NEG_INFINITY);
assert!((-42_f16).log10().is_nan());
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#329-331)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Compute the distance between the origin and a point (`x`, `y`) on the Euclidean plane. Equivalently, compute the length of the hypotenuse of a right-angle triangle with other sides having length `x.abs()` and `y.abs()`.

##### [§](#unspecified-precision-7)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `hypotf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-7)Examples

```rust
#![feature(f16)]

let x = 2.0f16;
let y = 3.0f16;

// sqrt(x^2 + y^2)
let abs_difference = (x.hypot(y) - (x.powi(2) + y.powi(2)).sqrt()).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#358-360)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the sine of a number (in radians).

##### [§](#unspecified-precision-8)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-8)Examples

```rust
#![feature(f16)]

let x = std::f16::consts::FRAC_PI_2;

let abs_difference = (x.sin() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#387-389)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the cosine of a number (in radians).

##### [§](#unspecified-precision-9)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-9)Examples

```rust
#![feature(f16)]

let x = 2.0 * std::f16::consts::PI;

let abs_difference = (x.cos() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#418-420)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the tangent of a number (in radians).

##### [§](#unspecified-precision-10)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `tanf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-10)Examples

```rust
#![feature(f16)]

let x = std::f16::consts::FRAC_PI_4;
let abs_difference = (x.tan() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#454-456)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the arcsine of a number. Return value is in radians in the range \[-pi/2, pi/2] or NaN if the number is outside the range \[-1, 1].

##### [§](#unspecified-precision-11)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `asinf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-11)Examples

```rust
#![feature(f16)]

let f = std::f16::consts::FRAC_PI_4;

// asin(sin(pi/2))
let abs_difference = (f.sin().asin() - f).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#490-492)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the arccosine of a number. Return value is in radians in the range \[0, pi] or NaN if the number is outside the range \[-1, 1].

##### [§](#unspecified-precision-12)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `acosf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-12)Examples

```rust
#![feature(f16)]

let f = std::f16::consts::FRAC_PI_4;

// acos(cos(pi/4))
let abs_difference = (f.cos().acos() - std::f16::consts::FRAC_PI_4).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#525-527)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the arctangent of a number. Return value is in radians in the range \[-pi/2, pi/2];

##### [§](#unspecified-precision-13)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `atanf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-13)Examples

```rust
#![feature(f16)]

let f = 1.0f16;

// atan(tan(1))
let abs_difference = (f.tan().atan() - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#574-576)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the four quadrant arctangent of `self` (`y`) and `other` (`x`) in radians.

`x``y`Piecewise DefinitionRange `>= +0``>= +0``arctan(y/x)``[+0, +pi/2]` `>= +0``<= -0``arctan(y/x)``[-pi/2, -0]` `<= -0``>= +0``arctan(y/x) + pi``[+pi/2, +pi]` `<= -0``<= -0``arctan(y/x) - pi``[-pi, -pi/2]`

##### [§](#unspecified-precision-14)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `atan2f` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-14)Examples

```rust
#![feature(f16)]

// Positive angles measured counter-clockwise
// from positive x axis
// -pi/4 radians (45 deg clockwise)
let x1 = 3.0f16;
let y1 = -3.0f16;

// 3pi/4 radians (135 deg counter-clockwise)
let x2 = -3.0f16;
let y2 = 3.0f16;

let abs_difference_1 = (y1.atan2(x1) - (-std::f16::consts::FRAC_PI_4)).abs();
let abs_difference_2 = (y2.atan2(x2) - (3.0 * std::f16::consts::FRAC_PI_4)).abs();

assert!(abs_difference_1 <= f16::EPSILON);
assert!(abs_difference_2 <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#610-612)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Simultaneously computes the sine and cosine of the number, `x`. Returns `(sin(x), cos(x))`.

##### [§](#unspecified-precision-15)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `(f16::sin(x), f16::cos(x))`. Note that this might change in the future.

##### [§](#examples-15)Examples

```rust
#![feature(f16)]

let x = std::f16::consts::FRAC_PI_4;
let f = x.sin_cos();

let abs_difference_0 = (f.0 - x.sin()).abs();
let abs_difference_1 = (f.1 - x.cos()).abs();

assert!(abs_difference_0 <= f16::EPSILON);
assert!(abs_difference_1 <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#645-647)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `e^(self) - 1` in a way that is accurate even if the number is close to zero.

##### [§](#unspecified-precision-16)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `expm1f` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-16)Examples

```rust
#![feature(f16)]

let x = 1e-4_f16;

// for very small x, e^x is approximately 1 + x + x^2 / 2
let approx = x + x * x / 2.0;
let abs_difference = (x.exp_m1() - approx).abs();

assert!(abs_difference < 1e-4);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#694-696)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `ln(1+n)` (natural logarithm) more accurately than if the operations were performed separately.

This returns NaN when `n < -1.0`, and negative infinity when `n == -1.0`.

##### [§](#unspecified-precision-17)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `log1pf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-17)Examples

```rust
#![feature(f16)]

let x = 1e-4_f16;

// for very small x, ln(1 + x) is approximately x - x^2 / 2
let approx = x - x * x / 2.0;
let abs_difference = (x.ln_1p() - approx).abs();

assert!(abs_difference < 1e-4);
```

Out-of-range values:

```rust
#![feature(f16)]

assert_eq!((-1.0_f16).ln_1p(), f16::NEG_INFINITY);
assert!((-2.0_f16).ln_1p().is_nan());
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#730-732)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Hyperbolic sine function.

##### [§](#unspecified-precision-18)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `sinhf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-18)Examples

```rust
#![feature(f16)]

let e = std::f16::consts::E;
let x = 1.0f16;

let f = x.sinh();
// Solving sinh() at 1 gives `(e^2-1)/(2e)`
let g = ((e * e) - 1.0) / (2.0 * e);
let abs_difference = (f - g).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#766-768)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Hyperbolic cosine function.

##### [§](#unspecified-precision-19)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `coshf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-19)Examples

```rust
#![feature(f16)]

let e = std::f16::consts::E;
let x = 1.0f16;
let f = x.cosh();
// Solving cosh() at 1 gives this result
let g = ((e * e) + 1.0) / (2.0 * e);
let abs_difference = (f - g).abs();

// Same result
assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#802-804)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Hyperbolic tangent function.

##### [§](#unspecified-precision-20)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `tanhf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-20)Examples

```rust
#![feature(f16)]

let e = std::f16::consts::E;
let x = 1.0f16;

let f = x.tanh();
// Solving tanh() at 1 gives `(1 - e^(-2))/(1 + e^(-2))`
let g = (1.0 - e.powi(-2)) / (1.0 + e.powi(-2));
let abs_difference = (f - g).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#833-837)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Inverse hyperbolic sine function.

##### [§](#unspecified-precision-21)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-21)Examples

```rust
#![feature(f16)]

let x = 1.0f16;
let f = x.sinh().asinh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#866-872)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Inverse hyperbolic cosine function.

##### [§](#unspecified-precision-22)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-22)Examples

```rust
#![feature(f16)]

let x = 1.0f16;
let f = x.cosh().acosh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#901-903)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Inverse hyperbolic tangent function.

##### [§](#unspecified-precision-23)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-23)Examples

```rust
#![feature(f16)]

let x = std::f16::consts::FRAC_PI_6;
let f = x.tanh().atanh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= 0.01);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#934-936)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Gamma function.

##### [§](#unspecified-precision-24)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `tgammaf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-24)Examples

```rust
#![feature(f16)]

let x = 5.0f16;

let abs_difference = (x.gamma() - 24.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#969-973)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Natural logarithm of the absolute value of the gamma function

The integer part of the tuple indicates the sign of the gamma function.

##### [§](#unspecified-precision-25)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `lgamma_r` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-25)Examples

```rust
#![feature(f16)]

let x = 2.0f16;

let abs_difference = (x.ln_gamma().0 - 0.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#1010-1012)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Error function.

##### [§](#unspecified-precision-26)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `erff` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-26)Examples

```rust
#![feature(f16)]
/// The error function relates what percent of a normal distribution lies
/// within `x` standard deviations (scaled by `1/sqrt(2)`).
fn within_standard_deviations(x: f16) -> f16 {
    (x * std::f16::consts::FRAC_1_SQRT_2).erf() * 100.0
}

// 68% of a normal distribution is within one standard deviation
assert!((within_standard_deviations(1.0) - 68.269).abs() < 0.1);
// 95% of a normal distribution is within two standard deviations
assert!((within_standard_deviations(2.0) - 95.450).abs() < 0.1);
// 99.7% of a normal distribution is within three standard deviations
assert!((within_standard_deviations(3.0) - 99.730).abs() < 0.1);
```

[Source](https://doc.rust-lang.org/src/std/num/f16.rs.html#1043-1045)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Complementary error function.

##### [§](#unspecified-precision-27)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `erfcf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-27)Examples

```rust
#![feature(f16)]
let x: f16 = 0.123;

let one = x.erf() + x.erfc();
let abs_difference = (one - 1.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#149)[§](#impl-f16-1)

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#152)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

The radix or base of the internal representation of `f16`.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#157)

🔬This is a nightly-only experimental API. (`float_bits_const` [#151073](https://github.com/rust-lang/rust/issues/151073))

The size of this float type in bits.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#164)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Number of significant digits in base 2.

Note that the size of the mantissa in the bitwise representation is one smaller than this since the leading 1 is not stored explicitly.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#175)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Approximate number of significant digits in base 10.

This is the maximum *x* such that any decimal number with *x* significant digits can be converted to `f16` and back without loss.

Equal to floor(log10 2[`MANTISSA_DIGITS`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MANTISSA_DIGITS "associated constant f16::MANTISSA_DIGITS") − 1).

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#187)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#195)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Smallest finite `f16` value.

Equal to −[`MAX`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MAX "associated constant f16::MAX").

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#202)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Smallest positive normal `f16` value.

Equal to 2[`MIN_EXP`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MIN_EXP "associated constant f16::MIN_EXP") − 1.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#211)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#221)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

One greater than the minimum possible *normal* power of 2 exponent for a significand bounded by 1 ≤ x &lt; 2 (i.e. the IEEE definition).

This corresponds to the exact minimum possible *normal* power of 2 exponent for a significand bounded by 0.5 ≤ x &lt; 1 (i.e. the C definition). In other words, all normal numbers representable by this type are greater than or equal to 0.5 × 2*MIN\_EXP*.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#230)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

One greater than the maximum possible power of 2 exponent for a significand bounded by 1 ≤ x &lt; 2 (i.e. the IEEE definition).

This corresponds to the exact maximum possible power of 2 exponent for a significand bounded by 0.5 ≤ x &lt; 1 (i.e. the C definition). In other words, all numbers representable by this type are strictly less than 2*MAX\_EXP*.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#238)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Minimum *x* for which 10*x* is normal.

Equal to ceil(log10 [`MIN_POSITIVE`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MIN_POSITIVE "associated constant f16::MIN_POSITIVE")).

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#245)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Maximum *x* for which 10*x* is normal.

Equal to floor(log10 [`MAX`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MAX "associated constant f16::MAX")).

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#262)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Not a Number (NaN).

Note that IEEE 754 doesn’t define just a single NaN value; a plethora of bit patterns are considered to be NaN. Furthermore, the standard makes a difference between a “signaling” and a “quiet” NaN, and allows inspecting its “payload” (the unspecified bits in the bit pattern) and its sign. See the [specification of NaN bit patterns](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info.

This constant is guaranteed to be a quiet NaN (on targets that follow the Rust assumptions that the quiet/signaling bit being set to 1 indicates a quiet NaN). Beyond that, nothing is guaranteed about the specific bit pattern chosen here: both payload and sign are arbitrary. The concrete bit pattern may change across Rust versions and target platforms.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#266)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Infinity (∞).

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#270)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Negative infinity (−∞).

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#301)

🔬This is a nightly-only experimental API. (`float_exact_integer_constants` [#152466](https://github.com/rust-lang/rust/issues/152466))

Maximum integer that can be represented exactly in an [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") value, with no other integer converting to the same floating point value.

For an integer `x` which satisfies `MIN_EXACT_INTEGER <= x <= MAX_EXACT_INTEGER`, there is a “one-to-one” mapping between [`i16`](https://doc.rust-lang.org/std/primitive.i16.html "primitive i16") and [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") values. `MAX_EXACT_INTEGER + 1` also converts losslessly to [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") and back to [`i16`](https://doc.rust-lang.org/std/primitive.i16.html "primitive i16"), but `MAX_EXACT_INTEGER + 2` converts to the same [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") value (and back to `MAX_EXACT_INTEGER + 1` as an integer) so there is not a “one-to-one” mapping.

```rust
#![feature(f16)]
#![feature(float_exact_integer_constants)]
let max_exact_int = f16::MAX_EXACT_INTEGER;
assert_eq!(max_exact_int, max_exact_int as f16 as i16);
assert_eq!(max_exact_int + 1, (max_exact_int + 1) as f16 as i16);
assert_ne!(max_exact_int + 2, (max_exact_int + 2) as f16 as i16);

// Beyond `f16::MAX_EXACT_INTEGER`, multiple integers can map to one float value
assert_eq!((max_exact_int + 1) as f16, (max_exact_int + 2) as f16);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#334)

🔬This is a nightly-only experimental API. (`float_exact_integer_constants` [#152466](https://github.com/rust-lang/rust/issues/152466))

Minimum integer that can be represented exactly in an [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") value, with no other integer converting to the same floating point value.

For an integer `x` which satisfies `MIN_EXACT_INTEGER <= x <= MAX_EXACT_INTEGER`, there is a “one-to-one” mapping between [`i16`](https://doc.rust-lang.org/std/primitive.i16.html "primitive i16") and [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") values. `MAX_EXACT_INTEGER + 1` also converts losslessly to [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") and back to [`i16`](https://doc.rust-lang.org/std/primitive.i16.html "primitive i16"), but `MAX_EXACT_INTEGER + 2` converts to the same [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") value (and back to `MAX_EXACT_INTEGER + 1` as an integer) so there is not a “one-to-one” mapping.

This constant is equivalent to `-MAX_EXACT_INTEGER`.

```rust
#![feature(f16)]
#![feature(float_exact_integer_constants)]
let min_exact_int = f16::MIN_EXACT_INTEGER;
assert_eq!(min_exact_int, min_exact_int as f16 as i16);
assert_eq!(min_exact_int - 1, (min_exact_int - 1) as f16 as i16);
assert_ne!(min_exact_int - 2, (min_exact_int - 2) as f16 as i16);

// Below `f16::MIN_EXACT_INTEGER`, multiple integers can map to one float value
assert_eq!((min_exact_int - 1) as f16, (min_exact_int - 2) as f16);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#368)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if this value is NaN.

```rust
#![feature(f16)]

let nan = f16::NAN;
let f = 7.0_f16;

assert!(nan.is_nan());
assert!(!f.is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#394)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if this value is positive infinity or negative infinity, and `false` otherwise.

```rust
#![feature(f16)]

let f = 7.0f16;
let inf = f16::INFINITY;
let neg_inf = f16::NEG_INFINITY;
let nan = f16::NAN;

assert!(!f.is_infinite());
assert!(!nan.is_infinite());

assert!(inf.is_infinite());
assert!(neg_inf.is_infinite());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#420)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if this number is neither infinite nor NaN.

```rust
#![feature(f16)]

let f = 7.0f16;
let inf: f16 = f16::INFINITY;
let neg_inf: f16 = f16::NEG_INFINITY;
let nan: f16 = f16::NAN;

assert!(f.is_finite());

assert!(!nan.is_finite());
assert!(!inf.is_finite());
assert!(!neg_inf.is_finite());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#451)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if the number is [subnormal](https://en.wikipedia.org/wiki/Denormal_number).

```rust
#![feature(f16)]

let min = f16::MIN_POSITIVE; // 6.1035e-5
let max = f16::MAX;
let lower_than_min = 1.0e-7_f16;
let zero = 0.0_f16;

assert!(!min.is_subnormal());
assert!(!max.is_subnormal());

assert!(!zero.is_subnormal());
assert!(!f16::NAN.is_subnormal());
assert!(!f16::INFINITY.is_subnormal());
// Values between `0` and `min` are Subnormal.
assert!(lower_than_min.is_subnormal());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#480)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if the number is neither zero, infinite, [subnormal](https://en.wikipedia.org/wiki/Denormal_number), or NaN.

```rust
#![feature(f16)]

let min = f16::MIN_POSITIVE; // 6.1035e-5
let max = f16::MAX;
let lower_than_min = 1.0e-7_f16;
let zero = 0.0_f16;

assert!(min.is_normal());
assert!(max.is_normal());

assert!(!zero.is_normal());
assert!(!f16::NAN.is_normal());
assert!(!f16::INFINITY.is_normal());
// Values between `0` and `min` are Subnormal.
assert!(!lower_than_min.is_normal());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#503)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the floating point category of the number. If only one property is going to be tested, it is generally faster to use the specific predicate instead.

```rust
#![feature(f16)]

use std::num::FpCategory;

let num = 12.4_f16;
let inf = f16::INFINITY;

assert_eq!(num.classify(), FpCategory::Normal);
assert_eq!(inf.classify(), FpCategory::Infinite);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#538)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if `self` has a positive sign, including `+0.0`, NaNs with positive sign bit and positive infinity.

Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `is_sign_positive` on a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info. Use `self.signum() == 1.0` if you need fully portable behavior (will return `false` for all NaNs).

```rust
#![feature(f16)]

let f = 7.0_f16;
let g = -7.0_f16;

assert!(f.is_sign_positive());
assert!(!g.is_sign_positive());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#566)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns `true` if `self` has a negative sign, including `-0.0`, NaNs with negative sign bit and negative infinity.

Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `is_sign_negative` on a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info. Use `self.signum() == -1.0` if you need fully portable behavior (will return `false` for all NaNs).

```rust
#![feature(f16)]

let f = 7.0_f16;
let g = -7.0_f16;

assert!(!f.is_sign_negative());
assert!(g.is_sign_negative());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#607)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the least number greater than `self`.

Let `TINY` be the smallest representable positive `f16`. Then,

- if `self.is_nan()`, this returns `self`;
- if `self` is [`NEG_INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.NEG_INFINITY "associated constant f16::NEG_INFINITY"), this returns [`MIN`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MIN "associated constant f16::MIN");
- if `self` is `-TINY`, this returns -0.0;
- if `self` is -0.0 or +0.0, this returns `TINY`;
- if `self` is [`MAX`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MAX "associated constant f16::MAX") or [`INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.INFINITY "associated constant f16::INFINITY"), this returns [`INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.INFINITY "associated constant f16::INFINITY");
- otherwise the unique least value greater than `self` is returned.

The identity `x.next_up() == -(-x).next_down()` holds for all non-NaN `x`. When `x` is finite `x == x.next_up().next_down()` also holds.

```rust
#![feature(f16)]

// f16::EPSILON is the difference between 1.0 and the next number up.
assert_eq!(1.0f16.next_up(), 1.0 + f16::EPSILON);
// But not for most numbers.
assert!(0.1f16.next_up() < 0.1 + f16::EPSILON);
assert_eq!(4356f16.next_up(), 4360.0);
```

This operation corresponds to IEEE-754 `nextUp`.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#661)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the greatest number less than `self`.

Let `TINY` be the smallest representable positive `f16`. Then,

- if `self.is_nan()`, this returns `self`;
- if `self` is [`INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.INFINITY "associated constant f16::INFINITY"), this returns [`MAX`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MAX "associated constant f16::MAX");
- if `self` is `TINY`, this returns 0.0;
- if `self` is -0.0 or +0.0, this returns `-TINY`;
- if `self` is [`MIN`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.MIN "associated constant f16::MIN") or [`NEG_INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.NEG_INFINITY "associated constant f16::NEG_INFINITY"), this returns [`NEG_INFINITY`](https://doc.rust-lang.org/std/primitive.f16.html#associatedconstant.NEG_INFINITY "associated constant f16::NEG_INFINITY");
- otherwise the unique greatest value less than `self` is returned.

The identity `x.next_down() == -(-x).next_up()` holds for all non-NaN `x`. When `x` is finite `x == x.next_down().next_up()` also holds.

```rust
#![feature(f16)]

let x = 1.0f16;
// Clamp value into range [0, 1).
let clamped = x.clamp(0.0, 1.0f16.next_down());
assert!(clamped < 1.0);
assert_eq!(clamped.next_up(), 1.0);
```

This operation corresponds to IEEE-754 `nextDown`.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#696)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Takes the reciprocal (inverse) of a number, `1/x`.

```rust
#![feature(f16)]

let x = 2.0_f16;
let abs_difference = (x.recip() - (1.0 / x)).abs();

assert!(abs_difference <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#722)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Converts radians to degrees.

##### [§](#unspecified-precision-28)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-28)Examples

```rust
#![feature(f16)]

let angle = std::f16::consts::PI;

let abs_difference = (angle.to_degrees() - 180.0).abs();
assert!(abs_difference <= 0.5);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#752)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Converts degrees to radians.

##### [§](#unspecified-precision-29)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-29)Examples

```rust
#![feature(f16)]

let angle = 180.0f16;

let abs_difference = (angle.to_radians() - std::f16::consts::PI).abs();

assert!(abs_difference <= 0.01);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#786)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the maximum of the two numbers, ignoring NaN.

If exactly one of the arguments is NaN (quiet or signaling), then the other argument is returned. If both arguments are NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32"). If the inputs compare equal (such as for the case of `+0.0` and `-0.0`), either input may be returned non-deterministically.

The handling of NaNs follows the IEEE 754-2019 semantics for `maximumNumber`, treating all NaNs the same way to ensure the operation is associative. The handling of signed zeros follows the IEEE 754-2008 semantics for `maxNum`.

```rust
#![feature(f16)]

let x = 1.0f16;
let y = 2.0f16;

assert_eq!(x.max(y), y);
assert_eq!(x.max(f16::NAN), x);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#817)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the minimum of the two numbers, ignoring NaN.

If exactly one of the arguments is NaN (quiet or signaling), then the other argument is returned. If both arguments are NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32"). If the inputs compare equal (such as for the case of `+0.0` and `-0.0`), either input may be returned non-deterministically.

The handling of NaNs follows the IEEE 754-2019 semantics for `minimumNumber`, treating all NaNs the same way to ensure the operation is associative. The handling of signed zeros follows the IEEE 754-2008 semantics for `minNum`.

```rust
#![feature(f16)]

let x = 1.0f16;
let y = 2.0f16;

assert_eq!(x.min(y), x);
assert_eq!(x.min(f16::NAN), x);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#849)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the maximum of the two numbers, propagating NaN.

If at least one of the arguments is NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32"). Furthermore, `-0.0` is considered to be less than `+0.0`, making this function fully deterministic for non-NaN inputs.

This is in contrast to [`f16::max`](https://doc.rust-lang.org/std/primitive.f16.html#method.max "method f16::max") which only returns NaN when *both* arguments are NaN, and which does not reliably order `-0.0` and `+0.0`.

This follows the IEEE 754-2019 semantics for `maximum`.

```rust
#![feature(f16)]
#![feature(float_minimum_maximum)]

let x = 1.0f16;
let y = 2.0f16;

assert_eq!(x.maximum(y), y);
assert!(x.maximum(f16::NAN).is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#881)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the minimum of the two numbers, propagating NaN.

If at least one of the arguments is NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32"). Furthermore, `-0.0` is considered to be less than `+0.0`, making this function fully deterministic for non-NaN inputs.

This is in contrast to [`f16::min`](https://doc.rust-lang.org/std/primitive.f16.html#method.min "method f16::min") which only returns NaN when *both* arguments are NaN, and which does not reliably order `-0.0` and `+0.0`.

This follows the IEEE 754-2019 semantics for `minimum`.

```rust
#![feature(f16)]
#![feature(float_minimum_maximum)]

let x = 1.0f16;
let y = 2.0f16;

assert_eq!(x.minimum(y), x);
assert!(x.minimum(f16::NAN).is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#904)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Calculates the midpoint (average) between `self` and `rhs`.

This returns NaN when *either* argument is NaN or if a combination of +inf and -inf is provided as arguments.

##### [§](#examples-30)Examples

```rust
#![feature(f16)]

assert_eq!(1f16.midpoint(4.0), 2.5);
assert_eq!((-5.5f16).midpoint(8.0), 1.25);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#946-948)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Rounds toward zero and converts to any primitive integer type, assuming that the value is finite and fits in that type.

```rust
#![feature(f16)]

let value = 4.6_f16;
let rounded = unsafe { value.to_int_unchecked::<u16>() };
assert_eq!(rounded, 4);

let value = -128.9_f16;
let rounded = unsafe { value.to_int_unchecked::<i8>() };
assert_eq!(rounded, i8::MIN);
```

##### [§](#safety)Safety

The value must:

- Not be `NaN`
- Not be infinite
- Be representable in the return type `Int`, after truncating off its fractional part

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#977)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Raw transmutation to `u16`.

This is currently identical to `transmute::<f16, u16>(self)` on all platforms.

See [`from_bits`](#method.from_bits) for some discussion of the portability of this operation (there are almost no issues).

Note that this function is distinct from `as` casting, which attempts to preserve the *numeric* value, and not the bitwise value.

```rust
#![feature(f16)]

assert_ne!((1f16).to_bits(), 1f16 as u16); // to_bits() is not casting!
assert_eq!((12.5f16).to_bits(), 0x4a40);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1024)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Raw transmutation from `u16`.

This is currently identical to `transmute::<u16, f16>(v)` on all platforms. It turns out this is incredibly portable, for two reasons:

- Floats and Ints have the same endianness on all supported platforms.
- IEEE 754 very precisely specifies the bit layout of floats.

However there is one caveat: prior to the 2008 version of IEEE 754, how to interpret the NaN signaling bit wasn’t actually specified. Most platforms (notably x86 and ARM) picked the interpretation that was ultimately standardized in 2008, but some didn’t (notably MIPS). As a result, all signaling NaNs on MIPS are quiet NaNs on x86, and vice-versa.

Rather than trying to preserve signaling-ness cross-platform, this implementation favors preserving the exact bits. This means that any payloads encoded in NaNs will be preserved even if the result of this method is sent over the network from an x86 machine to a MIPS one.

If the results of this method are only manipulated by the same architecture that produced them, then there is no portability concern.

If the input isn’t NaN, then there is no portability concern.

If you don’t care about signalingness (very likely), then there is no portability concern.

Note that this function is distinct from `as` casting, which attempts to preserve the *numeric* value, and not the bitwise value.

```rust
#![feature(f16)]

let v = f16::from_bits(0x4a40);
assert_eq!(v, 12.5);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1049)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the memory representation of this floating point number as a byte array in big-endian (network) byte order.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-31)Examples

```rust
#![feature(f16)]

let bytes = 12.5f16.to_be_bytes();
assert_eq!(bytes, [0x4a, 0x40]);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1072)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the memory representation of this floating point number as a byte array in little-endian byte order.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-32)Examples

```rust
#![feature(f16)]

let bytes = 12.5f16.to_le_bytes();
assert_eq!(bytes, [0x40, 0x4a]);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1108)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the memory representation of this floating point number as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/std/primitive.f16.html#method.to_be_bytes "method f16::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/std/primitive.f16.html#method.to_le_bytes "method f16::to_le_bytes"), as appropriate, instead.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-33)Examples

```rust
#![feature(f16)]

let bytes = 12.5f16.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x4a, 0x40]
    } else {
        [0x40, 0x4a]
    }
);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1130)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Creates a floating point value from its representation as a byte array in big endian.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-34)Examples

```rust
#![feature(f16)]

let value = f16::from_be_bytes([0x4a, 0x40]);
assert_eq!(value, 12.5);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1152)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Creates a floating point value from its representation as a byte array in little endian.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-35)Examples

```rust
#![feature(f16)]

let value = f16::from_le_bytes([0x40, 0x4a]);
assert_eq!(value, 12.5);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1185)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Creates a floating point value from its representation as a byte array in native endian.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_be_bytes "associated function f16::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_le_bytes "associated function f16::from_le_bytes"), as appropriate instead.

See [`from_bits`](https://doc.rust-lang.org/std/primitive.f16.html#method.from_bits "associated function f16::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-36)Examples

```rust
#![feature(f16)]

let value = f16::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x4a, 0x40]
} else {
    [0x40, 0x4a]
});
assert_eq!(value, 12.5);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1256)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the ordering between `self` and `other`.

Unlike the standard partial comparison between floating point numbers, this comparison always produces an ordering in accordance to the `totalOrder` predicate as defined in the IEEE 754 (2008 revision) floating point standard. The values are ordered in the following sequence:

- negative quiet NaN
- negative signaling NaN
- negative infinity
- negative numbers
- negative subnormal numbers
- negative zero
- positive zero
- positive subnormal numbers
- positive numbers
- positive infinity
- positive signaling NaN
- positive quiet NaN.

The ordering established by this function does not always agree with the [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") and [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") implementations of `f16`. For example, they consider negative and positive zero equal, while `total_cmp` doesn’t.

The interpretation of the signaling NaN bit follows the definition in the IEEE 754 standard, which may not match the interpretation by some of the older, non-conformant (e.g. MIPS) hardware implementations.

##### [§](#example)Example

```rust
#![feature(f16)]

struct GoodBoy {
    name: &'static str,
    weight: f16,
}

let mut bois = vec![
    GoodBoy { name: "Pucci", weight: 0.1 },
    GoodBoy { name: "Woofer", weight: 99.0 },
    GoodBoy { name: "Yapper", weight: 10.0 },
    GoodBoy { name: "Chonk", weight: f16::INFINITY },
    GoodBoy { name: "Abs. Unit", weight: f16::NAN },
    GoodBoy { name: "Floaty", weight: -5.0 },
];

bois.sort_by(|a, b| a.weight.total_cmp(&b.weight));

// `f16::NAN` could be positive or negative, which will affect the sort order.
if f16::NAN.is_sign_negative() {
    bois.into_iter().map(|b| b.weight)
        .zip([f16::NAN, -5.0, 0.1, 10.0, 99.0, f16::INFINITY].iter())
        .for_each(|(a, b)| assert_eq!(a.to_bits(), b.to_bits()))
} else {
    bois.into_iter().map(|b| b.weight)
        .zip([-5.0, 0.1, 10.0, 99.0, f16::INFINITY, f16::NAN].iter())
        .for_each(|(a, b)| assert_eq!(a.to_bits(), b.to_bits()))
}
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1322)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Restrict a value to a certain interval unless it is NaN.

Returns `max` if `self` is greater than `max`, and `min` if `self` is less than `min`. Otherwise this returns `self`.

Note that this function returns NaN if the initial value was NaN as well. If the result is zero and among the three inputs `self`, `min`, and `max` there are zeros with different sign, either `0.0` or `-0.0` is returned non-deterministically.

##### [§](#panics)Panics

Panics if `min > max`, `min` is NaN, or `max` is NaN.

##### [§](#examples-37)Examples

```rust
#![feature(f16)]

assert!((-3.0f16).clamp(-2.0, 1.0) == -2.0);
assert!((0.0f16).clamp(-2.0, 1.0) == 0.0);
assert!((2.0f16).clamp(-2.0, 1.0) == 1.0);
assert!((f16::NAN).clamp(-2.0, 1.0).is_nan());

// These always returns zero, but the sign (which is ignored by `==`) is non-deterministic.
assert!((0.0f16).clamp(-0.0, -0.0) == 0.0);
assert!((1.0f16).clamp(-0.0, 0.0) == 0.0);
// This is definitely a negative zero.
assert!((-1.0f16).clamp(-0.0, 1.0).is_sign_negative());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1366)

🔬This is a nightly-only experimental API. (`clamp_magnitude` [#148519](https://github.com/rust-lang/rust/issues/148519))

Clamps this number to a symmetric range centered around zero.

The method clamps the number’s magnitude (absolute value) to be at most `limit`.

This is functionally equivalent to `self.clamp(-limit, limit)`, but is more explicit about the intent.

##### [§](#panics-1)Panics

Panics if `limit` is negative or NaN, as this indicates a logic error.

##### [§](#examples-38)Examples

```rust
#![feature(f16)]
#![feature(clamp_magnitude)]
assert_eq!(5.0f16.clamp_magnitude(3.0), 3.0);
assert_eq!((-5.0f16).clamp_magnitude(3.0), -3.0);
assert_eq!(2.0f16.clamp_magnitude(3.0), 2.0);
assert_eq!((-2.0f16).clamp_magnitude(3.0), -2.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1395)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Computes the absolute value of `self`.

This function always returns the precise result.

##### [§](#examples-39)Examples

```rust
#![feature(f16)]

let x = 3.5_f16;
let y = -3.5_f16;

assert_eq!(x.abs(), x);
assert_eq!(y.abs(), -y);

assert!(f16::NAN.abs().is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1423)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns a number that represents the sign of `self`.

- `1.0` if the number is positive, `+0.0` or `INFINITY`
- `-1.0` if the number is negative, `-0.0` or `NEG_INFINITY`
- NaN if the number is NaN

##### [§](#examples-40)Examples

```rust
#![feature(f16)]

let f = 3.5_f16;

assert_eq!(f.signum(), 1.0);
assert_eq!(f16::NEG_INFINITY.signum(), -1.0);

assert!(f16::NAN.signum().is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1461)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns a number composed of the magnitude of `self` and the sign of `sign`.

Equal to `self` if the sign of `self` and `sign` are the same, otherwise equal to `-self`. If `self` is a NaN, then a NaN with the same payload as `self` and the sign bit of `sign` is returned.

If `sign` is a NaN, then this operation will still carry over its sign into the result. Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `copysign` with `sign` being a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info.

##### [§](#examples-41)Examples

```rust
#![feature(f16)]

let f = 3.5_f16;

assert_eq!(f.copysign(0.42), 3.5_f16);
assert_eq!(f.copysign(-0.42), -3.5_f16);
assert_eq!((-f).copysign(0.42), 3.5_f16);
assert_eq!((-f).copysign(-0.42), -3.5_f16);

assert!(f16::NAN.copysign(1.0).is_nan());
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1472)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float addition that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1483)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float subtraction that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1494)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float multiplication that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1505)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float division that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1516)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float remainder that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1525)[§](#impl-f16-2)

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1551)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the largest integer less than or equal to `self`.

This function always returns the precise result.

##### [§](#examples-42)Examples

```rust
#![feature(f16)]

let f = 3.7_f16;
let g = 3.0_f16;
let h = -3.7_f16;

assert_eq!(f.floor(), 3.0);
assert_eq!(g.floor(), 3.0);
assert_eq!(h.floor(), -4.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1579)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the smallest integer greater than or equal to `self`.

This function always returns the precise result.

##### [§](#examples-43)Examples

```rust
#![feature(f16)]

let f = 3.01_f16;
let g = 4.0_f16;

assert_eq!(f.ceil(), 4.0);
assert_eq!(g.ceil(), 4.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1613)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the nearest integer to `self`. If a value is half-way between two integers, round away from `0.0`.

This function always returns the precise result.

##### [§](#examples-44)Examples

```rust
#![feature(f16)]

let f = 3.3_f16;
let g = -3.3_f16;
let h = -3.7_f16;
let i = 3.5_f16;
let j = 4.5_f16;

assert_eq!(f.round(), 3.0);
assert_eq!(g.round(), -3.0);
assert_eq!(h.round(), -4.0);
assert_eq!(i.round(), 4.0);
assert_eq!(j.round(), 5.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1645)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the nearest integer to a number. Rounds half-way cases to the number with an even least significant digit.

This function always returns the precise result.

##### [§](#examples-45)Examples

```rust
#![feature(f16)]

let f = 3.3_f16;
let g = -3.3_f16;
let h = 3.5_f16;
let i = 4.5_f16;

assert_eq!(f.round_ties_even(), 3.0);
assert_eq!(g.round_ties_even(), -3.0);
assert_eq!(h.round_ties_even(), 4.0);
assert_eq!(i.round_ties_even(), 4.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1676)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the integer part of `self`. This means that non-integer numbers are always truncated towards zero.

This function always returns the precise result.

##### [§](#examples-46)Examples

```rust
#![feature(f16)]

let f = 3.7_f16;
let g = 3.0_f16;
let h = -3.7_f16;

assert_eq!(f.trunc(), 3.0);
assert_eq!(g.trunc(), 3.0);
assert_eq!(h.trunc(), -3.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1705)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the fractional part of `self`.

This function always returns the precise result.

##### [§](#examples-47)Examples

```rust
#![feature(f16)]

let x = 3.6_f16;
let y = -3.6_f16;
let abs_difference_x = (x.fract() - 0.6).abs();
let abs_difference_y = (y.fract() - (-0.6)).abs();

assert!(abs_difference_x <= f16::EPSILON);
assert!(abs_difference_y <= f16::EPSILON);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1752)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Fused multiply-add. Computes `(self * a) + b` with only one rounding error, yielding a more accurate result than an unfused multiply-add.

Using `mul_add` *may* be more performant than an unfused multiply-add if the target architecture has a dedicated `fma` CPU instruction. However, this is not always true, and will be heavily dependant on designing algorithms with specific target hardware in mind.

##### [§](#precision)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result. It is specified by IEEE 754 as `fusedMultiplyAdd` and guaranteed not to change.

##### [§](#examples-48)Examples

```rust
#![feature(f16)]

let m = 10.0_f16;
let x = 4.0_f16;
let b = 60.0_f16;

assert_eq!(m.mul_add(x, b), 100.0);
assert_eq!(m * x + b, 100.0);

let one_plus_eps = 1.0_f16 + f16::EPSILON;
let one_minus_eps = 1.0_f16 - f16::EPSILON;
let minus_one = -1.0_f16;

// The exact result (1 + eps) * (1 - eps) = 1 - eps * eps.
assert_eq!(one_plus_eps.mul_add(one_minus_eps, minus_one), -f16::EPSILON * f16::EPSILON);
// Different rounding with the non-fused multiply and add.
assert_eq!(one_plus_eps * one_minus_eps + minus_one, 0.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1787)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Calculates Euclidean division, the matching method for `rem_euclid`.

This computes the integer `n` such that `self = n * rhs + self.rem_euclid(rhs)`. In other words, the result is `self / rhs` rounded to the integer `n` such that `self >= n * rhs`.

##### [§](#precision-1)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result.

##### [§](#examples-49)Examples

```rust
#![feature(f16)]

let a: f16 = 7.0;
let b = 4.0;
assert_eq!(a.div_euclid(b), 1.0); // 7.0 > 4.0 * 1.0
assert_eq!((-a).div_euclid(b), -2.0); // -7.0 >= 4.0 * -2.0
assert_eq!(a.div_euclid(-b), -1.0); // 7.0 >= -4.0 * -1.0
assert_eq!((-a).div_euclid(-b), 2.0); // -7.0 >= -4.0 * 2.0
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1834)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Calculates the least nonnegative remainder of `self` when divided by `rhs`.

In particular, the return value `r` satisfies `0.0 <= r < rhs.abs()` in most cases. However, due to a floating point round-off error it can result in `r == rhs.abs()`, violating the mathematical definition, if `self` is much smaller than `rhs.abs()` in magnitude and `self < 0.0`. This result is not an element of the function’s codomain, but it is the closest floating point number in the real numbers and thus fulfills the property `self == self.div_euclid(rhs) * rhs + self.rem_euclid(rhs)` approximately.

##### [§](#precision-2)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result.

##### [§](#examples-50)Examples

```rust
#![feature(f16)]

let a: f16 = 7.0;
let b = 4.0;
assert_eq!(a.rem_euclid(b), 3.0);
assert_eq!((-a).rem_euclid(b), 1.0);
assert_eq!(a.rem_euclid(-b), 3.0);
assert_eq!((-a).rem_euclid(-b), 1.0);
// limitation due to round-off error
assert!((-f16::EPSILON).rem_euclid(3.0) != 0.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1874)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Raises a number to an integer power.

Using this function is generally faster than using `powf`. It might have a different sequence of rounding operations than `powf`, so the results are not guaranteed to agree.

Note that this function is special in that it can return non-NaN results for NaN inputs. For example, `f16::powi(f16::NAN, 0)` returns `1.0`. However, if an input is a *signaling* NaN, then the result is non-deterministically either a NaN or the result that the corresponding quiet NaN would produce.

##### [§](#unspecified-precision-30)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-51)Examples

```rust
#![feature(f16)]

let x = 2.0_f16;
let abs_difference = (x.powi(2) - (x * x)).abs();
assert!(abs_difference <= f16::EPSILON);

assert_eq!(f16::powi(f16::NAN, 0), 1.0);
assert_eq!(f16::powi(0.0, 0), 1.0);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1909)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the square root of a number.

Returns NaN if `self` is a negative number other than `-0.0`.

##### [§](#precision-3)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result. It is specified by IEEE 754 as `squareRoot` and guaranteed not to change.

##### [§](#examples-52)Examples

```rust
#![feature(f16)]

let positive = 4.0_f16;
let negative = -4.0_f16;
let negative_zero = -0.0_f16;

assert_eq!(positive.sqrt(), 2.0);
assert!(negative.sqrt().is_nan());
assert!(negative_zero.sqrt() == negative_zero);
```

[Source](https://doc.rust-lang.org/src/core/num/f16.rs.html#1942)

🔬This is a nightly-only experimental API. (`f16` [#116909](https://github.com/rust-lang/rust/issues/116909))

Returns the cube root of a number.

##### [§](#unspecified-precision-31)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `cbrtf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-53)Examples

```rust
#![feature(f16)]

let x = 8.0f16;

// x^(1/3) - 2 == 0
let abs_difference = (x.cbrt() - 2.0).abs();

assert!(abs_difference <= f16::EPSILON);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-13)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-12)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-11)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-10)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#114)[§](#method.add)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26f16%3E-for-f16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-f16)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/float.rs.html#243)[§](#impl-Debug-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/src/core/default.rs.html#183)[§](#impl-Default-for-f16)

[Source](https://doc.rust-lang.org/src/core/default.rs.html#183)[§](#method.default)

Returns the default value of `0.0`

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/float.rs.html#243)[§](#impl-Display-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-3)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#method.div-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-2)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-1)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#method.div-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#526)[§](#method.div)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26f16%3E-for-f16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-f16)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#218-228)[§](#impl-From%3Cbool%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#218-228)[§](#method.from-4)

Converts a [`bool`](https://doc.rust-lang.org/std/primitive.bool.html "primitive bool") to [`f16`](https://doc.rust-lang.org/std/primitive.f16.html "primitive f16") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-54)Examples

```rust
#![feature(f16)]

let x: f16 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f16 = true.into();
assert_eq!(y, 1.0);
```

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#180)[§](#impl-From%3Cf16%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#179)[§](#impl-From%3Cf16%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#151)[§](#impl-From%3Ci8%3E-for-f16)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#164)[§](#impl-From%3Cu8%3E-for-f16)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/num/dec2flt/mod.rs.html#178)[§](#impl-FromStr-for-f16)

[Source](https://doc.rust-lang.org/src/core/num/dec2flt/mod.rs.html#178)[§](#method.from_str)

Converts a string in base 10 to a float. Accepts an optional decimal exponent.

This function accepts strings such as

- ‘3.14’
- ‘-3.14’
- ‘2.5E10’, or equivalently, ‘2.5e10’
- ‘2.5E-10’
- ‘5.’
- ‘.5’, or, equivalently, ‘0.5’
- ‘7’
- ‘007’
- ‘inf’, ‘-inf’, ‘+infinity’, ‘NaN’

Note that alphabetical characters are not case-sensitive.

Leading and trailing whitespace represent an error.

##### [§](#grammar)Grammar

All strings that adhere to the following [EBNF](https://www.w3.org/TR/REC-xml/#sec-notation) grammar when lowercased will result in an [`Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") being returned:

```txt
Float  ::= Sign? ( 'inf' | 'infinity' | 'nan' | Number )
Number ::= ( Digit+ |
             Digit+ '.' Digit* |
             Digit* '.' Digit+ ) Exp?
Exp    ::= 'e' Sign? Digit+
Sign   ::= [+-]
Digit  ::= [0-9]
```

##### [§](#arguments)Arguments

- src - A string

##### [§](#return-value)Return value

`Err(ParseFloatError)` if the string did not represent a valid number. Otherwise, `Ok(n)` where `n` is the closest representable floating-point number to the number represented by `src` (following the same rules for rounding as for the results of primitive operations).

[Source](https://doc.rust-lang.org/src/core/num/dec2flt/mod.rs.html#178)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/float.rs.html#243)[§](#impl-LowerExp-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-21)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-20)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-19)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-18)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26f16%3E-for-f16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-%26f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-f16)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#impl-PartialOrd-for-f16)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1991)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#impl-Product%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#impl-Product-for-f16)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-7)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#method.rem-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-6)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-5)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#method.rem-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#impl-Rem-for-f16)

The remainder from the division of two floats.

The remainder has the same sign as the dividend and is computed as: `x - (x / y).trunc() * y`.

#### [§](#examples-55)Examples

```rust
let x: f32 = 50.50;
let y: f32 = 8.125;
let remainder = x - (x / y).trunc() * y;

// The answer to both operations is 1.75
assert_eq!(x % y, remainder);
```

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-4)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#650)[§](#method.rem)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26f16%3E-for-f16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-f16)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26f16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-17)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-16)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Cf16%3E-for-%26f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-15)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-f16)

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-14)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26f16%3E-for-f16)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-f16)

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#impl-Sum%3C%26f16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#impl-Sum-for-f16)

[Source](https://doc.rust-lang.org/src/core/iter/traits/accum.rs.html#206)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/float.rs.html#243)[§](#impl-UpperExp-for-f16)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci128%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci32%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci64%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Ci8%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cisize%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu128%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu16%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu32%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu64%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cu8%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/convert/num.rs.html#37)[§](#impl-FloatToInt%3Cusize%3E-for-f16)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-f16)

[§](#impl-Freeze-for-f16)

[§](#impl-RefUnwindSafe-for-f16)

[§](#impl-Send-for-f16)

[§](#impl-Sync-for-f16)

[§](#impl-Unpin-for-f16)

[§](#impl-UnsafeUnpin-for-f16)

[§](#impl-UnwindSafe-for-f16)