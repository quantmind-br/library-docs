---
title: f32 - Rust
url: https://doc.rust-lang.org/stable/std/primitive.f32.html
source: crawler
fetched_at: 2026-05-06T21:28:15.293056028-03:00
rendered_js: false
word_count: 8055
summary: This document provides a technical overview of the f32 32-bit floating-point type, covering its precision limitations, special values like NaN and infinity, rounding behavior, and non-deterministic NaN bit patterns.
tags:
    - f32
    - floating-point
    - ieee-754
    - rust-primitives
    - nan-behavior
    - precision
category: reference
---

Expand description

A 32-bit floating-point type (specifically, the “binary32” type defined in IEEE 754-2008).

This type can represent a wide range of decimal numbers, like `3.5`, `27`, `-113.75`, `0.0078125`, `34359738368`, `0`, `-1`. So unlike integer types (such as `i32`), floating-point types can represent non-integer numbers, too.

However, being able to represent this wide range of numbers comes at the cost of precision: floats can only represent some of the real numbers and calculation with floats round to a nearby representable number. For example, `5.0` and `1.0` can be exactly represented as `f32`, but `1.0 / 5.0` results in `0.20000000298023223876953125` since `0.2` cannot be exactly represented as `f32`. Note, however, that printing floats with `println` and friends will often discard insignificant digits: `println!("{}", 1.0f32 / 5.0f32)` will print `0.2`.

Additionally, `f32` can represent some special values:

- −0.0: IEEE 754 floating-point numbers have a bit that indicates their sign, so −0.0 is a possible value. For comparison −0.0 = +0.0, but floating-point operations can carry the sign bit through arithmetic operations. This means −0.0 × +0.0 produces −0.0 and a negative number rounded to a value smaller than a float can represent also produces −0.0.
- [∞](#associatedconstant.INFINITY) and [−∞](#associatedconstant.NEG_INFINITY): these result from calculations like `1.0 / 0.0`.
- [NaN (not a number)](#associatedconstant.NAN): this value results from calculations like `(-1.0).sqrt()`. NaN has some potentially unexpected behavior:
  
  - It is not equal to any float, including itself! This is the reason `f32` doesn’t implement the `Eq` trait.
  - It is also neither smaller nor greater than any float, making it impossible to sort by the default comparison operation, which is the reason `f32` doesn’t implement the `Ord` trait.
  - It is also considered *infectious* as almost all calculations where one of the operands is NaN will also result in NaN. The explanations on this page only explicitly document behavior on NaN operands if this default is deviated from.
  - Lastly, there are multiple bit patterns that are considered NaN. Rust does not currently guarantee that the bit patterns of NaN are preserved over arithmetic operations, and they are not guaranteed to be portable or even fully deterministic! This means that there may be some surprising results upon inspecting the bit patterns, as the same calculations might produce NaNs with different bit patterns. This also affects the sign of the NaN: checking `is_sign_positive` or `is_sign_negative` on a NaN is the most common way to run into these surprising results. (Checking `x >= 0.0` or `x <= 0.0` avoids those surprises, but also how negative/positive zero are treated.) See the section below for what exactly is guaranteed about the bit pattern of a NaN.

When a primitive operation (addition, subtraction, multiplication, or division) is performed on this type, the result is rounded according to the roundTiesToEven direction defined in IEEE 754-2008. That means:

- The result is the representable value closest to the true value, if there is a unique closest representable value.
- If the true value is exactly half-way between two representable values, the result is the one with an even least-significant binary digit.
- If the true value’s magnitude is ≥ `f32::MAX` + 2(`f32::MAX_EXP` − `f32::MANTISSA_DIGITS` − 1), the result is ∞ or −∞ (preserving the true value’s sign).
- If the result of a sum exactly equals zero, the outcome is +0.0 unless both arguments were negative, then it is -0.0. Subtraction `a - b` is regarded as a sum `a + (-b)`.

For more information on floating-point numbers, see [Wikipedia](https://en.wikipedia.org/wiki/Single-precision_floating-point_format).

*[See also the `std::f32::consts` module](https://doc.rust-lang.org/stable/std/f32/consts/index.html "mod std::f32::consts").*

## [§](#nan-bit-patterns)NaN bit patterns

This section defines the possible NaN bit patterns returned by floating-point operations.

The bit pattern of a floating-point NaN value is defined by:

- a sign bit.
- a quiet/signaling bit. Rust assumes that the quiet/signaling bit being set to `1` indicates a quiet NaN (QNaN), and a value of `0` indicates a signaling NaN (SNaN). In the following we will hence just call it the “quiet bit”.
- a payload, which makes up the rest of the significand (i.e., the mantissa) except for the quiet bit.

The rules for NaN values differ between *arithmetic* and *non-arithmetic* (or “bitwise”) operations. The non-arithmetic operations are unary `-`, `abs`, `copysign`, `signum`, `{to,from}_bits`, `{to,from}_{be,le,ne}_bytes` and `is_sign_{positive,negative}`. These operations are guaranteed to exactly preserve the bit pattern of their input except for possibly changing the sign bit.

The following rules apply when a NaN value is returned from an arithmetic operation:

- The result has a non-deterministic sign.
- The quiet bit and payload are non-deterministically chosen from the following set of options:
  
  - **Preferred NaN**: The quiet bit is set and the payload is all-zero.
  - **Quieting NaN propagation**: The quiet bit is set and the payload is copied from any input operand that is a NaN. If the inputs and outputs do not have the same payload size (i.e., for `as` casts), then
    
    - If the output is smaller than the input, low-order bits of the payload get dropped.
    - If the output is larger than the input, the payload gets filled up with 0s in the low-order bits.
  - **Unchanged NaN propagation**: The quiet bit and payload are copied from any input operand that is a NaN. If the inputs and outputs do not have the same size (i.e., for `as` casts), the same rules as for “quieting NaN propagation” apply, with one caveat: if the output is smaller than the input, dropping the low-order bits may result in a payload of 0; a payload of 0 is not possible with a signaling NaN (the all-0 significand encodes an infinity) so unchanged NaN propagation cannot occur with some inputs.
  - **Target-specific NaN**: The quiet bit is set and the payload is picked from a target-specific set of “extra” possible NaN payloads. The set can depend on the input operand values. See the table below for the concrete NaNs this set contains on various targets.

In particular, if all input NaNs are quiet (or if there are no input NaNs), then the output NaN is definitely quiet. Signaling NaN outputs can only occur if they are provided as an input value. Similarly, if all input NaNs are preferred (or if there are no input NaNs) and the target does not have any “extra” NaN payloads, then the output NaN is guaranteed to be preferred.

The non-deterministic choice happens when the operation is executed; i.e., the result of a NaN-producing floating-point operation is a stable bit pattern (looking at these bits multiple times will yield consistent results), but running the same operation twice with the same inputs can produce different results.

These guarantees are neither stronger nor weaker than those of IEEE 754: IEEE 754 guarantees that an operation never returns a signaling NaN, whereas it is possible for operations like `SNAN * 1.0` to return a signaling NaN in Rust. Conversely, IEEE 754 makes no statement at all about which quiet NaN is returned, whereas Rust restricts the set of possible results to the ones listed above.

Unless noted otherwise, the same rules also apply to NaNs returned by other library functions (e.g. `min`, `minimum`, `max`, `maximum`); other aspects of their semantics and which IEEE 754 operation they correspond to are documented with the respective functions.

When an arithmetic floating-point operation is executed in `const` context, the same rules apply: no guarantee is made about which of the NaN bit patterns described above will be returned. The result does not have to match what happens when executing the same code at runtime, and the result can vary depending on factors such as compiler version and flags.

`target_arch`Extra payloads possible on this platform `aarch64`, `arm`, `arm64ec`, `loongarch64`, `powerpc` (except when `target_abi = "spe"`), `powerpc64`, `riscv32`, `riscv64`, `s390x`, `x86`, `x86_64`None `nvptx64`All payloads `sparc`, `sparc64`The all-one payload `wasm32`, `wasm64`If all input NaNs are quiet with all-zero payload: None.  
Otherwise: all payloads.

For targets not in this table, all payloads are possible.

## [§](#algebraic-operators)Algebraic operators

Algebraic operators of the form `a.algebraic_*(b)` allow the compiler to optimize floating point operations using all the usual algebraic properties of real numbers – despite the fact that those properties do *not* hold on floating point numbers. This can give a great performance boost since it may unlock vectorization.

The exact set of optimizations is unspecified but typically allows combining operations, rearranging series of operations based on mathematical properties, converting between division and reciprocal multiplication, and disregarding the sign of zero. This means that the results of elementary operations may have undefined precision, and “non-mathematical” values such as NaN, +/-Inf, or -0.0 may behave in unexpected ways, but these operations will never cause undefined behavior.

Because of the unpredictable nature of compiler optimizations, the same inputs may produce different results even within a single program run. **Unsafe code must not rely on any property of the return value for soundness.** However, implementations will generally do their best to pick a reasonable tradeoff between performance and accuracy of the result.

For example:

```rust
x = a.algebraic_add(b).algebraic_add(c).algebraic_add(d);
```

May be rewritten as:

```rust
x = a + b + c + d; // As written
x = (a + c) + (b + d); // Reordered to shorten critical path and enable vectorization
```

[Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#28-1276)[§](#impl-f32)

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#49-51)

Returns the largest integer less than or equal to `self`.

This function always returns the precise result.

##### [§](#examples)Examples

```rust
let f = 3.7_f32;
let g = 3.0_f32;
let h = -3.7_f32;

assert_eq!(f.floor(), 3.0);
assert_eq!(g.floor(), 3.0);
assert_eq!(h.floor(), -4.0);
```

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#72-74)

Returns the smallest integer greater than or equal to `self`.

This function always returns the precise result.

##### [§](#examples-1)Examples

```rust
let f = 3.01_f32;
let g = 4.0_f32;

assert_eq!(f.ceil(), 4.0);
assert_eq!(g.ceil(), 4.0);
```

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#101-103)

Returns the nearest integer to `self`. If a value is half-way between two integers, round away from `0.0`.

This function always returns the precise result.

##### [§](#examples-2)Examples

```rust
let f = 3.3_f32;
let g = -3.3_f32;
let h = -3.7_f32;
let i = 3.5_f32;
let j = 4.5_f32;

assert_eq!(f.round(), 3.0);
assert_eq!(g.round(), -3.0);
assert_eq!(h.round(), -4.0);
assert_eq!(i.round(), 4.0);
assert_eq!(j.round(), 5.0);
```

1.77.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#128-130)

Returns the nearest integer to a number. Rounds half-way cases to the number with an even least significant digit.

This function always returns the precise result.

##### [§](#examples-3)Examples

```rust
let f = 3.3_f32;
let g = -3.3_f32;
let h = 3.5_f32;
let i = 4.5_f32;

assert_eq!(f.round_ties_even(), 3.0);
assert_eq!(g.round_ties_even(), -3.0);
assert_eq!(h.round_ties_even(), 4.0);
assert_eq!(i.round_ties_even(), 4.0);
```

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#154-156)

Returns the integer part of `self`. This means that non-integer numbers are always truncated towards zero.

This function always returns the precise result.

##### [§](#examples-4)Examples

```rust
let f = 3.7_f32;
let g = 3.0_f32;
let h = -3.7_f32;

assert_eq!(f.trunc(), 3.0);
assert_eq!(g.trunc(), 3.0);
assert_eq!(h.trunc(), -3.0);
```

1.0.0 (const: 1.90.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#178-180)

Returns the fractional part of `self`.

This function always returns the precise result.

##### [§](#examples-5)Examples

```rust
let x = 3.6_f32;
let y = -3.6_f32;
let abs_difference_x = (x.fract() - 0.6).abs();
let abs_difference_y = (y.fract() - (-0.6)).abs();

assert!(abs_difference_x <= f32::EPSILON);
assert!(abs_difference_y <= f32::EPSILON);
```

1.0.0 (const: 1.94.0) · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#221-223)

Fused multiply-add. Computes `(self * a) + b` with only one rounding error, yielding a more accurate result than an unfused multiply-add.

Using `mul_add` *may* be more performant than an unfused multiply-add if the target architecture has a dedicated `fma` CPU instruction. However, this is not always true, and will be heavily dependant on designing algorithms with specific target hardware in mind.

##### [§](#precision)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result. It is specified by IEEE 754 as `fusedMultiplyAdd` and guaranteed not to change.

##### [§](#examples-6)Examples

```rust
let m = 10.0_f32;
let x = 4.0_f32;
let b = 60.0_f32;

assert_eq!(m.mul_add(x, b), 100.0);
assert_eq!(m * x + b, 100.0);

let one_plus_eps = 1.0_f32 + f32::EPSILON;
let one_minus_eps = 1.0_f32 - f32::EPSILON;
let minus_one = -1.0_f32;

// The exact result (1 + eps) * (1 - eps) = 1 - eps * eps.
assert_eq!(one_plus_eps.mul_add(one_minus_eps, minus_one), -f32::EPSILON * f32::EPSILON);
// Different rounding with the non-fused multiply and add.
assert_eq!(one_plus_eps * one_minus_eps + minus_one, 0.0);
```

1.38.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#251-253)

Calculates Euclidean division, the matching method for `rem_euclid`.

This computes the integer `n` such that `self = n * rhs + self.rem_euclid(rhs)`. In other words, the result is `self / rhs` rounded to the integer `n` such that `self >= n * rhs`.

##### [§](#precision-1)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result.

##### [§](#examples-7)Examples

```rust
let a: f32 = 7.0;
let b = 4.0;
assert_eq!(a.div_euclid(b), 1.0); // 7.0 > 4.0 * 1.0
assert_eq!((-a).div_euclid(b), -2.0); // -7.0 >= 4.0 * -2.0
assert_eq!(a.div_euclid(-b), -1.0); // 7.0 >= -4.0 * -1.0
assert_eq!((-a).div_euclid(-b), 2.0); // -7.0 >= -4.0 * 2.0
```

1.38.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#289-291)

Calculates the least nonnegative remainder of `self` when divided by `rhs`.

In particular, the return value `r` satisfies `0.0 <= r < rhs.abs()` in most cases. However, due to a floating point round-off error it can result in `r == rhs.abs()`, violating the mathematical definition, if `self` is much smaller than `rhs.abs()` in magnitude and `self < 0.0`. This result is not an element of the function’s codomain, but it is the closest floating point number in the real numbers and thus fulfills the property `self == self.div_euclid(rhs) * rhs + self.rem_euclid(rhs)` approximately.

##### [§](#precision-2)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result.

##### [§](#examples-8)Examples

```rust
let a: f32 = 7.0;
let b = 4.0;
assert_eq!(a.rem_euclid(b), 3.0);
assert_eq!((-a).rem_euclid(b), 1.0);
assert_eq!(a.rem_euclid(-b), 3.0);
assert_eq!((-a).rem_euclid(-b), 1.0);
// limitation due to round-off error
assert!((-f32::EPSILON).rem_euclid(3.0) != 0.0);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#323-325)

Raises a number to an integer power.

Using this function is generally faster than using `powf`. It might have a different sequence of rounding operations than `powf`, so the results are not guaranteed to agree.

Note that this function is special in that it can return non-NaN results for NaN inputs. For example, `f32::powi(f32::NAN, 0)` returns `1.0`. However, if an input is a *signaling* NaN, then the result is non-deterministically either a NaN or the result that the corresponding quiet NaN would produce.

##### [§](#unspecified-precision)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-9)Examples

```rust
let x = 2.0_f32;
let abs_difference = (x.powi(2) - (x * x)).abs();
assert!(abs_difference <= 1e-5);

assert_eq!(f32::powi(f32::NAN, 0), 1.0);
assert_eq!(f32::powi(0.0, 0), 1.0);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#354-356)

Raises a number to a floating point power.

Note that this function is special in that it can return non-NaN results for NaN inputs. For example, `f32::powf(f32::NAN, 0.0)` returns `1.0`. However, if an input is a *signaling* NaN, then the result is non-deterministically either a NaN or the result that the corresponding quiet NaN would produce.

##### [§](#unspecified-precision-1)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-10)Examples

```rust
let x = 2.0_f32;
let abs_difference = (x.powf(2.0) - (x * x)).abs();
assert!(abs_difference <= 1e-5);

assert_eq!(f32::powf(1.0, f32::NAN), 1.0);
assert_eq!(f32::powf(f32::NAN, 0.0), 1.0);
assert_eq!(f32::powf(0.0, 0.0), 1.0);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#384-386)

Returns the square root of a number.

Returns NaN if `self` is a negative number other than `-0.0`.

##### [§](#precision-3)Precision

The result of this operation is guaranteed to be the rounded infinite-precision result. It is specified by IEEE 754 as `squareRoot` and guaranteed not to change.

##### [§](#examples-11)Examples

```rust
let positive = 4.0_f32;
let negative = -4.0_f32;
let negative_zero = -0.0_f32;

assert_eq!(positive.sqrt(), 2.0);
assert!(negative.sqrt().is_nan());
assert!(negative_zero.sqrt() == negative_zero);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#411-413)

Returns `e^(self)`, (the exponential function).

##### [§](#unspecified-precision-2)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-12)Examples

```rust
let one = 1.0f32;
// e^1
let e = one.exp();

// ln(e) - 1 == 0
let abs_difference = (e.ln() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#436-438)

Returns `2^(self)`.

##### [§](#unspecified-precision-3)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-13)Examples

```rust
let f = 2.0f32;

// 2^2 - 4 == 0
let abs_difference = (f.exp2() - 4.0).abs();

assert!(abs_difference <= 1e-5);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#471-473)

Returns the natural logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-4)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-14)Examples

```rust
let one = 1.0f32;
// e^1
let e = one.exp();

// ln(e) - 1 == 0
let abs_difference = (e.ln() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

Non-positive values:

```rust
assert_eq!(0_f32.ln(), f32::NEG_INFINITY);
assert!((-42_f32).ln().is_nan());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#508-510)

Returns the logarithm of the number with respect to an arbitrary base.

This returns NaN when the number is negative, and negative infinity when number is zero.

The result might not be correctly rounded owing to implementation details; `self.log2()` can produce more accurate results for base 2, and `self.log10()` can produce more accurate results for base 10.

##### [§](#unspecified-precision-5)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-15)Examples

```rust
let five = 5.0f32;

// log5(5) - 1 == 0
let abs_difference = (five.log(5.0) - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

Non-positive values:

```rust
assert_eq!(0_f32.log(10.0), f32::NEG_INFINITY);
assert!((-42_f32).log(10.0).is_nan());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#541-543)

Returns the base 2 logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-6)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-16)Examples

```rust
let two = 2.0f32;

// log2(2) - 1 == 0
let abs_difference = (two.log2() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

Non-positive values:

```rust
assert_eq!(0_f32.log2(), f32::NEG_INFINITY);
assert!((-42_f32).log2().is_nan());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#574-576)

Returns the base 10 logarithm of the number.

This returns NaN when the number is negative, and negative infinity when number is zero.

##### [§](#unspecified-precision-7)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-17)Examples

```rust
let ten = 10.0f32;

// log10(10) - 1 == 0
let abs_difference = (ten.log10() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

Non-positive values:

```rust
assert_eq!(0_f32.log10(), f32::NEG_INFINITY);
assert!((-42_f32).log10().is_nan());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#616-619)

👎Deprecated since 1.10.0: you probably meant `(self - other).abs()`: this operation is `(self - other).max(0.0)` except that `abs_sub` also propagates NaNs (also known as `fdimf` in C). If you truly need the positive difference, consider using that expression or the C function `fdimf`, depending on how you wish to handle NaN (please consider filing an issue describing your use-case too).

The positive difference of two numbers.

- If `self <= other`: `0.0`
- Else: `self - other`

##### [§](#unspecified-precision-8)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `fdimf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-18)Examples

```rust
let x = 3.0f32;
let y = -3.0f32;

let abs_difference_x = (x.abs_sub(1.0) - 2.0).abs();
let abs_difference_y = (y.abs_sub(1.0) - 0.0).abs();

assert!(abs_difference_x <= 1e-6);
assert!(abs_difference_y <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#644-646)

Returns the cube root of a number.

##### [§](#unspecified-precision-9)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `cbrtf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-19)Examples

```rust
let x = 8.0f32;

// x^(1/3) - 2 == 0
let abs_difference = (x.cbrt() - 2.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#675-677)

Compute the distance between the origin and a point (`x`, `y`) on the Euclidean plane. Equivalently, compute the length of the hypotenuse of a right-angle triangle with other sides having length `x.abs()` and `y.abs()`.

##### [§](#unspecified-precision-10)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `hypotf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-20)Examples

```rust
let x = 2.0f32;
let y = 3.0f32;

// sqrt(x^2 + y^2)
let abs_difference = (x.hypot(y) - (x.powi(2) + y.powi(2)).sqrt()).abs();

assert!(abs_difference <= 1e-5);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#699-701)

Computes the sine of a number (in radians).

##### [§](#unspecified-precision-11)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-21)Examples

```rust
let x = std::f32::consts::FRAC_PI_2;

let abs_difference = (x.sin() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#723-725)

Computes the cosine of a number (in radians).

##### [§](#unspecified-precision-12)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-22)Examples

```rust
let x = 2.0 * std::f32::consts::PI;

let abs_difference = (x.cos() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#748-750)

Computes the tangent of a number (in radians).

##### [§](#unspecified-precision-13)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `tanf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-23)Examples

```rust
let x = std::f32::consts::FRAC_PI_4;
let abs_difference = (x.tan() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#778-780)

Computes the arcsine of a number. Return value is in radians in the range \[-pi/2, pi/2] or NaN if the number is outside the range \[-1, 1].

##### [§](#unspecified-precision-14)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `asinf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-24)Examples

```rust
let f = std::f32::consts::FRAC_PI_4;

// asin(sin(pi/2))
let abs_difference = (f.sin().asin() - f).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#808-810)

Computes the arccosine of a number. Return value is in radians in the range \[0, pi] or NaN if the number is outside the range \[-1, 1].

##### [§](#unspecified-precision-15)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `acosf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-25)Examples

```rust
let f = std::f32::consts::FRAC_PI_4;

// acos(cos(pi/4))
let abs_difference = (f.cos().acos() - std::f32::consts::FRAC_PI_4).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#837-839)

Computes the arctangent of a number. Return value is in radians in the range \[-pi/2, pi/2];

##### [§](#unspecified-precision-16)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `atanf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-26)Examples

```rust
let f = 1.0f32;

// atan(tan(1))
let abs_difference = (f.tan().atan() - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#880-882)

Computes the four quadrant arctangent of `self` (`y`) and `other` (`x`) in radians.

`x``y`Piecewise DefinitionRange `>= +0``>= +0``arctan(y/x)``[+0, +pi/2]` `>= +0``<= -0``arctan(y/x)``[-pi/2, -0]` `<= -0``>= +0``arctan(y/x) + pi``[+pi/2, +pi]` `<= -0``<= -0``arctan(y/x) - pi``[-pi, -pi/2]`

##### [§](#unspecified-precision-17)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `atan2f` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-27)Examples

```rust
// Positive angles measured counter-clockwise
// from positive x axis
// -pi/4 radians (45 deg clockwise)
let x1 = 3.0f32;
let y1 = -3.0f32;

// 3pi/4 radians (135 deg counter-clockwise)
let x2 = -3.0f32;
let y2 = 3.0f32;

let abs_difference_1 = (y1.atan2(x1) - (-std::f32::consts::FRAC_PI_4)).abs();
let abs_difference_2 = (y2.atan2(x2) - (3.0 * std::f32::consts::FRAC_PI_4)).abs();

assert!(abs_difference_1 <= 1e-5);
assert!(abs_difference_2 <= 1e-5);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#910-912)

Simultaneously computes the sine and cosine of the number, `x`. Returns `(sin(x), cos(x))`.

##### [§](#unspecified-precision-18)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `(f32::sin(x), f32::cos(x))`. Note that this might change in the future.

##### [§](#examples-28)Examples

```rust
let x = std::f32::consts::FRAC_PI_4;
let f = x.sin_cos();

let abs_difference_0 = (f.0 - x.sin()).abs();
let abs_difference_1 = (f.1 - x.cos()).abs();

assert!(abs_difference_0 <= 1e-4);
assert!(abs_difference_1 <= 1e-4);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#939-941)

Returns `e^(self) - 1` in a way that is accurate even if the number is close to zero.

##### [§](#unspecified-precision-19)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `expm1f` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-29)Examples

```rust
let x = 1e-8_f32;

// for very small x, e^x is approximately 1 + x + x^2 / 2
let approx = x + x * x / 2.0;
let abs_difference = (x.exp_m1() - approx).abs();

assert!(abs_difference < 1e-10);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#977-979)

Returns `ln(1+n)` (natural logarithm) more accurately than if the operations were performed separately.

This returns NaN when `n < -1.0`, and negative infinity when `n == -1.0`.

##### [§](#unspecified-precision-20)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `log1pf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-30)Examples

```rust
let x = 1e-8_f32;

// for very small x, ln(1 + x) is approximately x - x^2 / 2
let approx = x - x * x / 2.0;
let abs_difference = (x.ln_1p() - approx).abs();

assert!(abs_difference < 1e-10);
```

Out-of-range values:

```rust
assert_eq!((-1.0_f32).ln_1p(), f32::NEG_INFINITY);
assert!((-2.0_f32).ln_1p().is_nan());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1007-1009)

Hyperbolic sine function.

##### [§](#unspecified-precision-21)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `sinhf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-31)Examples

```rust
let e = std::f32::consts::E;
let x = 1.0f32;

let f = x.sinh();
// Solving sinh() at 1 gives `(e^2-1)/(2e)`
let g = ((e * e) - 1.0) / (2.0 * e);
let abs_difference = (f - g).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1037-1039)

Hyperbolic cosine function.

##### [§](#unspecified-precision-22)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `coshf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-32)Examples

```rust
let e = std::f32::consts::E;
let x = 1.0f32;
let f = x.cosh();
// Solving cosh() at 1 gives this result
let g = ((e * e) + 1.0) / (2.0 * e);
let abs_difference = (f - g).abs();

// Same result
assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1067-1069)

Hyperbolic tangent function.

##### [§](#unspecified-precision-23)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `tanhf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-33)Examples

```rust
let e = std::f32::consts::E;
let x = 1.0f32;

let f = x.tanh();
// Solving tanh() at 1 gives `(1 - e^(-2))/(1 + e^(-2))`
let g = (1.0 - e.powi(-2)) / (1.0 + e.powi(-2));
let abs_difference = (f - g).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1093-1097)

Inverse hyperbolic sine function.

##### [§](#unspecified-precision-24)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-34)Examples

```rust
let x = 1.0f32;
let f = x.sinh().asinh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1121-1127)

Inverse hyperbolic cosine function.

##### [§](#unspecified-precision-25)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-35)Examples

```rust
let x = 1.0f32;
let f = x.cosh().acosh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= 1e-6);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1151-1153)

Inverse hyperbolic tangent function.

##### [§](#unspecified-precision-26)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-36)Examples

```rust
let x = std::f32::consts::FRAC_PI_6;
let f = x.tanh().atanh();

let abs_difference = (f - x).abs();

assert!(abs_difference <= 1e-5);
```

[Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1178-1180)

🔬This is a nightly-only experimental API. (`float_gamma` [#99842](https://github.com/rust-lang/rust/issues/99842))

Gamma function.

##### [§](#unspecified-precision-27)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `tgammaf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-37)Examples

```rust
#![feature(float_gamma)]
let x = 5.0f32;

let abs_difference = (x.gamma() - 24.0).abs();

assert!(abs_difference <= 1e-5);
```

[Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1207-1211)

🔬This is a nightly-only experimental API. (`float_gamma` [#99842](https://github.com/rust-lang/rust/issues/99842))

Natural logarithm of the absolute value of the gamma function

The integer part of the tuple indicates the sign of the gamma function.

##### [§](#unspecified-precision-28)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next. This function currently corresponds to the `lgamma_r` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-38)Examples

```rust
#![feature(float_gamma)]
let x = 2.0f32;

let abs_difference = (x.ln_gamma().0 - 0.0).abs();

assert!(abs_difference <= f32::EPSILON);
```

[Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1244-1246)

🔬This is a nightly-only experimental API. (`float_erf` [#136321](https://github.com/rust-lang/rust/issues/136321))

Error function.

##### [§](#unspecified-precision-29)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `erff` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-39)Examples

```rust
#![feature(float_erf)]
/// The error function relates what percent of a normal distribution lies
/// within `x` standard deviations (scaled by `1/sqrt(2)`).
fn within_standard_deviations(x: f32) -> f32 {
    (x * std::f32::consts::FRAC_1_SQRT_2).erf() * 100.0
}

// 68% of a normal distribution is within one standard deviation
assert!((within_standard_deviations(1.0) - 68.269).abs() < 0.01);
// 95% of a normal distribution is within two standard deviations
assert!((within_standard_deviations(2.0) - 95.450).abs() < 0.01);
// 99.7% of a normal distribution is within three standard deviations
assert!((within_standard_deviations(3.0) - 99.730).abs() < 0.01);
```

[Source](https://doc.rust-lang.org/stable/src/std/num/f32.rs.html#1273-1275)

🔬This is a nightly-only experimental API. (`float_erf` [#136321](https://github.com/rust-lang/rust/issues/136321))

Complementary error function.

##### [§](#unspecified-precision-30)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

This function currently corresponds to the `erfcf` from libc on Unix and Windows. Note that this might change in the future.

##### [§](#examples-40)Examples

```rust
#![feature(float_erf)]
let x: f32 = 0.123;

let one = x.erf() + x.erfc();
let abs_difference = (one - 1.0).abs();

assert!(abs_difference <= 1e-6);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#396)[§](#impl-f32-1)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#399)

The radix or base of the internal representation of `f32`.

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#403)

🔬This is a nightly-only experimental API. (`float_bits_const` [#151073](https://github.com/rust-lang/rust/issues/151073))

The size of this float type in bits.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#410)

Number of significant digits in base 2.

Note that the size of the mantissa in the bitwise representation is one smaller than this since the leading 1 is not stored explicitly.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#421)

Approximate number of significant digits in base 10.

This is the maximum *x* such that any decimal number with *x* significant digits can be converted to `f32` and back without loss.

Equal to floor(log10 2[`MANTISSA_DIGITS`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MANTISSA_DIGITS "associated constant f32::MANTISSA_DIGITS") − 1).

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#433)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#441)

Smallest finite `f32` value.

Equal to −[`MAX`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MAX "associated constant f32::MAX").

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#448)

Smallest positive normal `f32` value.

Equal to 2[`MIN_EXP`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MIN_EXP "associated constant f32::MIN_EXP") − 1.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#457)

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#467)

One greater than the minimum possible *normal* power of 2 exponent for a significand bounded by 1 ≤ x &lt; 2 (i.e. the IEEE definition).

This corresponds to the exact minimum possible *normal* power of 2 exponent for a significand bounded by 0.5 ≤ x &lt; 1 (i.e. the C definition). In other words, all normal numbers representable by this type are greater than or equal to 0.5 × 2*MIN\_EXP*.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#476)

One greater than the maximum possible power of 2 exponent for a significand bounded by 1 ≤ x &lt; 2 (i.e. the IEEE definition).

This corresponds to the exact maximum possible power of 2 exponent for a significand bounded by 0.5 ≤ x &lt; 1 (i.e. the C definition). In other words, all numbers representable by this type are strictly less than 2*MAX\_EXP*.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#484)

Minimum *x* for which 10*x* is normal.

Equal to ceil(log10 [`MIN_POSITIVE`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MIN_POSITIVE "associated constant f32::MIN_POSITIVE")).

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#491)

Maximum *x* for which 10*x* is normal.

Equal to floor(log10 [`MAX`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MAX "associated constant f32::MAX")).

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#508)

Not a Number (NaN).

Note that IEEE 754 doesn’t define just a single NaN value; a plethora of bit patterns are considered to be NaN. Furthermore, the standard makes a difference between a “signaling” and a “quiet” NaN, and allows inspecting its “payload” (the unspecified bits in the bit pattern) and its sign. See the [specification of NaN bit patterns](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info.

This constant is guaranteed to be a quiet NaN (on targets that follow the Rust assumptions that the quiet/signaling bit being set to 1 indicates a quiet NaN). Beyond that, nothing is guaranteed about the specific bit pattern chosen here: both payload and sign are arbitrary. The concrete bit pattern may change across Rust versions and target platforms.

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#511)

Infinity (∞).

1.43.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#514)

Negative infinity (−∞).

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#542)

🔬This is a nightly-only experimental API. (`float_exact_integer_constants` [#152466](https://github.com/rust-lang/rust/issues/152466))

Maximum integer that can be represented exactly in an [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") value, with no other integer converting to the same floating point value.

For an integer `x` which satisfies `MIN_EXACT_INTEGER <= x <= MAX_EXACT_INTEGER`, there is a “one-to-one” mapping between [`i32`](https://doc.rust-lang.org/stable/std/primitive.i32.html "primitive i32") and [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") values. `MAX_EXACT_INTEGER + 1` also converts losslessly to [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") and back to [`i32`](https://doc.rust-lang.org/stable/std/primitive.i32.html "primitive i32"), but `MAX_EXACT_INTEGER + 2` converts to the same [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") value (and back to `MAX_EXACT_INTEGER + 1` as an integer) so there is not a “one-to-one” mapping.

```rust
#![feature(float_exact_integer_constants)]
let max_exact_int = f32::MAX_EXACT_INTEGER;
assert_eq!(max_exact_int, max_exact_int as f32 as i32);
assert_eq!(max_exact_int + 1, (max_exact_int + 1) as f32 as i32);
assert_ne!(max_exact_int + 2, (max_exact_int + 2) as f32 as i32);

// Beyond `f32::MAX_EXACT_INTEGER`, multiple integers can map to one float value
assert_eq!((max_exact_int + 1) as f32, (max_exact_int + 2) as f32);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#572)

🔬This is a nightly-only experimental API. (`float_exact_integer_constants` [#152466](https://github.com/rust-lang/rust/issues/152466))

Minimum integer that can be represented exactly in an [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") value, with no other integer converting to the same floating point value.

For an integer `x` which satisfies `MIN_EXACT_INTEGER <= x <= MAX_EXACT_INTEGER`, there is a “one-to-one” mapping between [`i32`](https://doc.rust-lang.org/stable/std/primitive.i32.html "primitive i32") and [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") values. `MAX_EXACT_INTEGER + 1` also converts losslessly to [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") and back to [`i32`](https://doc.rust-lang.org/stable/std/primitive.i32.html "primitive i32"), but `MAX_EXACT_INTEGER + 2` converts to the same [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") value (and back to `MAX_EXACT_INTEGER + 1` as an integer) so there is not a “one-to-one” mapping.

This constant is equivalent to `-MAX_EXACT_INTEGER`.

```rust
#![feature(float_exact_integer_constants)]
let min_exact_int = f32::MIN_EXACT_INTEGER;
assert_eq!(min_exact_int, min_exact_int as f32 as i32);
assert_eq!(min_exact_int - 1, (min_exact_int - 1) as f32 as i32);
assert_ne!(min_exact_int - 2, (min_exact_int - 2) as f32 as i32);

// Below `f32::MIN_EXACT_INTEGER`, multiple integers can map to one float value
assert_eq!((min_exact_int - 1) as f32, (min_exact_int - 2) as f32);
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#603)

Returns `true` if this value is NaN.

```rust
let nan = f32::NAN;
let f = 7.0_f32;

assert!(nan.is_nan());
assert!(!f.is_nan());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#626)

Returns `true` if this value is positive infinity or negative infinity, and `false` otherwise.

```rust
let f = 7.0f32;
let inf = f32::INFINITY;
let neg_inf = f32::NEG_INFINITY;
let nan = f32::NAN;

assert!(!f.is_infinite());
assert!(!nan.is_infinite());

assert!(inf.is_infinite());
assert!(neg_inf.is_infinite());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#651)

Returns `true` if this number is neither infinite nor NaN.

```rust
let f = 7.0f32;
let inf = f32::INFINITY;
let neg_inf = f32::NEG_INFINITY;
let nan = f32::NAN;

assert!(f.is_finite());

assert!(!nan.is_finite());
assert!(!inf.is_finite());
assert!(!neg_inf.is_finite());
```

1.53.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#679)

Returns `true` if the number is [subnormal](https://en.wikipedia.org/wiki/Denormal_number).

```rust
let min = f32::MIN_POSITIVE; // 1.17549435e-38f32
let max = f32::MAX;
let lower_than_min = 1.0e-40_f32;
let zero = 0.0_f32;

assert!(!min.is_subnormal());
assert!(!max.is_subnormal());

assert!(!zero.is_subnormal());
assert!(!f32::NAN.is_subnormal());
assert!(!f32::INFINITY.is_subnormal());
// Values between `0` and `min` are Subnormal.
assert!(lower_than_min.is_subnormal());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#706)

Returns `true` if the number is neither zero, infinite, [subnormal](https://en.wikipedia.org/wiki/Denormal_number), or NaN.

```rust
let min = f32::MIN_POSITIVE; // 1.17549435e-38f32
let max = f32::MAX;
let lower_than_min = 1.0e-40_f32;
let zero = 0.0_f32;

assert!(min.is_normal());
assert!(max.is_normal());

assert!(!zero.is_normal());
assert!(!f32::NAN.is_normal());
assert!(!f32::INFINITY.is_normal());
// Values between `0` and `min` are Subnormal.
assert!(!lower_than_min.is_normal());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#725)

Returns the floating point category of the number. If only one property is going to be tested, it is generally faster to use the specific predicate instead.

```rust
use std::num::FpCategory;

let num = 12.4_f32;
let inf = f32::INFINITY;

assert_eq!(num.classify(), FpCategory::Normal);
assert_eq!(inf.classify(), FpCategory::Infinite);
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#762)

Returns `true` if `self` has a positive sign, including `+0.0`, NaNs with positive sign bit and positive infinity.

Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `is_sign_positive` on a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info. Use `self.signum() == 1.0` if you need fully portable behavior (will return `false` for all NaNs).

```rust
let f = 7.0_f32;
let g = -7.0_f32;

assert!(f.is_sign_positive());
assert!(!g.is_sign_positive());
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#787)

Returns `true` if `self` has a negative sign, including `-0.0`, NaNs with negative sign bit and negative infinity.

Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `is_sign_negative` on a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info. Use `self.signum() == -1.0` if you need fully portable behavior (will return `false` for all NaNs).

```rust
let f = 7.0f32;
let g = -7.0f32;

assert!(!f.is_sign_negative());
assert!(g.is_sign_negative());
```

1.86.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#824)

Returns the least number greater than `self`.

Let `TINY` be the smallest representable positive `f32`. Then,

- if `self.is_nan()`, this returns `self`;
- if `self` is [`NEG_INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.NEG_INFINITY "associated constant f32::NEG_INFINITY"), this returns [`MIN`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MIN "associated constant f32::MIN");
- if `self` is `-TINY`, this returns -0.0;
- if `self` is -0.0 or +0.0, this returns `TINY`;
- if `self` is [`MAX`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MAX "associated constant f32::MAX") or [`INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.INFINITY "associated constant f32::INFINITY"), this returns [`INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.INFINITY "associated constant f32::INFINITY");
- otherwise the unique least value greater than `self` is returned.

The identity `x.next_up() == -(-x).next_down()` holds for all non-NaN `x`. When `x` is finite `x == x.next_up().next_down()` also holds.

```rust
// f32::EPSILON is the difference between 1.0 and the next number up.
assert_eq!(1.0f32.next_up(), 1.0 + f32::EPSILON);
// But not for most numbers.
assert!(0.1f32.next_up() < 0.1 + f32::EPSILON);
assert_eq!(16777216f32.next_up(), 16777218.0);
```

This operation corresponds to IEEE-754 `nextUp`.

1.86.0 (const: 1.86.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#875)

Returns the greatest number less than `self`.

Let `TINY` be the smallest representable positive `f32`. Then,

- if `self.is_nan()`, this returns `self`;
- if `self` is [`INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.INFINITY "associated constant f32::INFINITY"), this returns [`MAX`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MAX "associated constant f32::MAX");
- if `self` is `TINY`, this returns 0.0;
- if `self` is -0.0 or +0.0, this returns `-TINY`;
- if `self` is [`MIN`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.MIN "associated constant f32::MIN") or [`NEG_INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.NEG_INFINITY "associated constant f32::NEG_INFINITY"), this returns [`NEG_INFINITY`](https://doc.rust-lang.org/stable/std/primitive.f32.html#associatedconstant.NEG_INFINITY "associated constant f32::NEG_INFINITY");
- otherwise the unique greatest value less than `self` is returned.

The identity `x.next_down() == -(-x).next_up()` holds for all non-NaN `x`. When `x` is finite `x == x.next_down().next_up()` also holds.

```rust
let x = 1.0f32;
// Clamp value into range [0, 1).
let clamped = x.clamp(0.0, 1.0f32.next_down());
assert!(clamped < 1.0);
assert_eq!(clamped.next_up(), 1.0);
```

This operation corresponds to IEEE-754 `nextDown`.

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#907)

Takes the reciprocal (inverse) of a number, `1/x`.

```rust
let x = 2.0_f32;
let abs_difference = (x.recip() - (1.0 / x)).abs();

assert!(abs_difference <= f32::EPSILON);
```

1.7.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#932)

Converts radians to degrees.

##### [§](#unspecified-precision-31)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-41)Examples

```rust
let angle = std::f32::consts::PI;

let abs_difference = (angle.to_degrees() - 180.0).abs();
assert!(abs_difference <= f32::EPSILON);
```

1.7.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#960)

Converts degrees to radians.

##### [§](#unspecified-precision-32)Unspecified precision

The precision of this function is non-deterministic. This means it varies by platform, Rust version, and can even differ within the same execution from one invocation to the next.

##### [§](#examples-42)Examples

```rust
let angle = 180.0f32;

let abs_difference = (angle.to_radians() - std::f32::consts::PI).abs();

assert!(abs_difference <= f32::EPSILON);
```

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#991)

Returns the maximum of the two numbers, ignoring NaN.

If exactly one of the arguments is NaN (quiet or signaling), then the other argument is returned. If both arguments are NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32"). If the inputs compare equal (such as for the case of `+0.0` and `-0.0`), either input may be returned non-deterministically.

The handling of NaNs follows the IEEE 754-2019 semantics for `maximumNumber`, treating all NaNs the same way to ensure the operation is associative. The handling of signed zeros follows the IEEE 754-2008 semantics for `maxNum`.

```rust
let x = 1.0f32;
let y = 2.0f32;

assert_eq!(x.max(y), y);
assert_eq!(x.max(f32::NAN), x);
```

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1018)

Returns the minimum of the two numbers, ignoring NaN.

If exactly one of the arguments is NaN (quiet or signaling), then the other argument is returned. If both arguments are NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32"). If the inputs compare equal (such as for the case of `+0.0` and `-0.0`), either input may be returned non-deterministically.

The handling of NaNs follows the IEEE 754-2019 semantics for `minimumNumber`, treating all NaNs the same way to ensure the operation is associative. The handling of signed zeros follows the IEEE 754-2008 semantics for `minNum`.

```rust
let x = 1.0f32;
let y = 2.0f32;

assert_eq!(x.min(y), x);
assert_eq!(x.min(f32::NAN), x);
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1045)

🔬This is a nightly-only experimental API. (`float_minimum_maximum` [#91079](https://github.com/rust-lang/rust/issues/91079))

Returns the maximum of the two numbers, propagating NaN.

If at least one of the arguments is NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32"). Furthermore, `-0.0` is considered to be less than `+0.0`, making this function fully deterministic for non-NaN inputs.

This is in contrast to [`f32::max`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.max "method f32::max") which only returns NaN when *both* arguments are NaN, and which does not reliably order `-0.0` and `+0.0`.

This follows the IEEE 754-2019 semantics for `maximum`.

```rust
#![feature(float_minimum_maximum)]
let x = 1.0f32;
let y = 2.0f32;

assert_eq!(x.maximum(y), y);
assert!(x.maximum(f32::NAN).is_nan());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1072)

🔬This is a nightly-only experimental API. (`float_minimum_maximum` [#91079](https://github.com/rust-lang/rust/issues/91079))

Returns the minimum of the two numbers, propagating NaN.

If at least one of the arguments is NaN, the return value is NaN, with the bit pattern picked using the usual [rules for arithmetic operations](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32"). Furthermore, `-0.0` is considered to be less than `+0.0`, making this function fully deterministic for non-NaN inputs.

This is in contrast to [`f32::min`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.min "method f32::min") which only returns NaN when *both* arguments are NaN, and which does not reliably order `-0.0` and `+0.0`.

This follows the IEEE 754-2019 semantics for `minimum`.

```rust
#![feature(float_minimum_maximum)]
let x = 1.0f32;
let y = 2.0f32;

assert_eq!(x.minimum(y), x);
assert!(x.minimum(f32::NAN).is_nan());
```

1.85.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1091)

Calculates the midpoint (average) between `self` and `rhs`.

This returns NaN when *either* argument is NaN or if a combination of +inf and -inf is provided as arguments.

##### [§](#examples-43)Examples

```rust
assert_eq!(1f32.midpoint(4.0), 2.5);
assert_eq!((-5.5f32).midpoint(8.0), 1.25);
```

1.44.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1149-1151)

Rounds toward zero and converts to any primitive integer type, assuming that the value is finite and fits in that type.

```rust
let value = 4.6_f32;
let rounded = unsafe { value.to_int_unchecked::<u16>() };
assert_eq!(rounded, 4);

let value = -128.9_f32;
let rounded = unsafe { value.to_int_unchecked::<i8>() };
assert_eq!(rounded, i8::MIN);
```

##### [§](#safety)Safety

The value must:

- Not be `NaN`
- Not be infinite
- Be representable in the return type `Int`, after truncating off its fractional part

1.20.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1181)

Raw transmutation to `u32`.

This is currently identical to `transmute::<f32, u32>(self)` on all platforms.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

Note that this function is distinct from `as` casting, which attempts to preserve the *numeric* value, and not the bitwise value.

##### [§](#examples-44)Examples

```rust
assert_ne!((1f32).to_bits(), 1f32 as u32); // to_bits() is not casting!
assert_eq!((12.5f32).to_bits(), 0x41480000);
```

1.20.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1227)

Raw transmutation from `u32`.

This is currently identical to `transmute::<u32, f32>(v)` on all platforms. It turns out this is incredibly portable, for two reasons:

- Floats and Ints have the same endianness on all supported platforms.
- IEEE 754 very precisely specifies the bit layout of floats.

However there is one caveat: prior to the 2008 version of IEEE 754, how to interpret the NaN signaling bit wasn’t actually specified. Most platforms (notably x86 and ARM) picked the interpretation that was ultimately standardized in 2008, but some didn’t (notably MIPS). As a result, all signaling NaNs on MIPS are quiet NaNs on x86, and vice-versa.

Rather than trying to preserve signaling-ness cross-platform, this implementation favors preserving the exact bits. This means that any payloads encoded in NaNs will be preserved even if the result of this method is sent over the network from an x86 machine to a MIPS one.

If the results of this method are only manipulated by the same architecture that produced them, then there is no portability concern.

If the input isn’t NaN, then there is no portability concern.

If you don’t care about signalingness (very likely), then there is no portability concern.

Note that this function is distinct from `as` casting, which attempts to preserve the *numeric* value, and not the bitwise value.

##### [§](#examples-45)Examples

```rust
let v = f32::from_bits(0x41480000);
assert_eq!(v, 12.5);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1250)

Returns the memory representation of this floating point number as a byte array in big-endian (network) byte order.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-46)Examples

```rust
let bytes = 12.5f32.to_be_bytes();
assert_eq!(bytes, [0x41, 0x48, 0x00, 0x00]);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1271)

Returns the memory representation of this floating point number as a byte array in little-endian byte order.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-47)Examples

```rust
let bytes = 12.5f32.to_le_bytes();
assert_eq!(bytes, [0x00, 0x00, 0x48, 0x41]);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1305)

Returns the memory representation of this floating point number as a byte array in native byte order.

As the target platform’s native endianness is used, portable code should use [`to_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.to_be_bytes "method f32::to_be_bytes") or [`to_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.to_le_bytes "method f32::to_le_bytes"), as appropriate, instead.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-48)Examples

```rust
let bytes = 12.5f32.to_ne_bytes();
assert_eq!(
    bytes,
    if cfg!(target_endian = "big") {
        [0x41, 0x48, 0x00, 0x00]
    } else {
        [0x00, 0x00, 0x48, 0x41]
    }
);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1324)

Creates a floating point value from its representation as a byte array in big endian.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-49)Examples

```rust
let value = f32::from_be_bytes([0x41, 0x48, 0x00, 0x00]);
assert_eq!(value, 12.5);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1343)

Creates a floating point value from its representation as a byte array in little endian.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-50)Examples

```rust
let value = f32::from_le_bytes([0x00, 0x00, 0x48, 0x41]);
assert_eq!(value, 12.5);
```

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1373)

Creates a floating point value from its representation as a byte array in native endian.

As the target platform’s native endianness is used, portable code likely wants to use [`from_be_bytes`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_be_bytes "associated function f32::from_be_bytes") or [`from_le_bytes`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_le_bytes "associated function f32::from_le_bytes"), as appropriate instead.

See [`from_bits`](https://doc.rust-lang.org/stable/std/primitive.f32.html#method.from_bits "associated function f32::from_bits") for some discussion of the portability of this operation (there are almost no issues).

##### [§](#examples-51)Examples

```rust
let value = f32::from_ne_bytes(if cfg!(target_endian = "big") {
    [0x41, 0x48, 0x00, 0x00]
} else {
    [0x00, 0x00, 0x48, 0x41]
});
assert_eq!(value, 12.5);
```

1.62.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1440)

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

The ordering established by this function does not always agree with the [`PartialOrd`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") and [`PartialEq`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") implementations of `f32`. For example, they consider negative and positive zero equal, while `total_cmp` doesn’t.

The interpretation of the signaling NaN bit follows the definition in the IEEE 754 standard, which may not match the interpretation by some of the older, non-conformant (e.g. MIPS) hardware implementations.

##### [§](#example)Example

```rust
struct GoodBoy {
    name: String,
    weight: f32,
}

let mut bois = vec![
    GoodBoy { name: "Pucci".to_owned(), weight: 0.1 },
    GoodBoy { name: "Woofer".to_owned(), weight: 99.0 },
    GoodBoy { name: "Yapper".to_owned(), weight: 10.0 },
    GoodBoy { name: "Chonk".to_owned(), weight: f32::INFINITY },
    GoodBoy { name: "Abs. Unit".to_owned(), weight: f32::NAN },
    GoodBoy { name: "Floaty".to_owned(), weight: -5.0 },
];

bois.sort_by(|a, b| a.weight.total_cmp(&b.weight));

// `f32::NAN` could be positive or negative, which will affect the sort order.
if f32::NAN.is_sign_negative() {
    assert!(bois.into_iter().map(|b| b.weight)
        .zip([f32::NAN, -5.0, 0.1, 10.0, 99.0, f32::INFINITY].iter())
        .all(|(a, b)| a.to_bits() == b.to_bits()))
} else {
    assert!(bois.into_iter().map(|b| b.weight)
        .zip([-5.0, 0.1, 10.0, 99.0, f32::INFINITY, f32::NAN].iter())
        .all(|(a, b)| a.to_bits() == b.to_bits()))
}
```

1.50.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1503)

Restrict a value to a certain interval unless it is NaN.

Returns `max` if `self` is greater than `max`, and `min` if `self` is less than `min`. Otherwise this returns `self`.

Note that this function returns NaN if the initial value was NaN as well. If the result is zero and among the three inputs `self`, `min`, and `max` there are zeros with different sign, either `0.0` or `-0.0` is returned non-deterministically.

##### [§](#panics)Panics

Panics if `min > max`, `min` is NaN, or `max` is NaN.

##### [§](#examples-52)Examples

```rust
assert!((-3.0f32).clamp(-2.0, 1.0) == -2.0);
assert!((0.0f32).clamp(-2.0, 1.0) == 0.0);
assert!((2.0f32).clamp(-2.0, 1.0) == 1.0);
assert!((f32::NAN).clamp(-2.0, 1.0).is_nan());

// These always returns zero, but the sign (which is ignored by `==`) is non-deterministic.
assert!((0.0f32).clamp(-0.0, -0.0) == 0.0);
assert!((1.0f32).clamp(-0.0, 0.0) == 0.0);
// This is definitely a negative zero.
assert!((-1.0f32).clamp(-0.0, 1.0).is_sign_negative());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1544)

🔬This is a nightly-only experimental API. (`clamp_magnitude` [#148519](https://github.com/rust-lang/rust/issues/148519))

Clamps this number to a symmetric range centered around zero.

The method clamps the number’s magnitude (absolute value) to be at most `limit`.

This is functionally equivalent to `self.clamp(-limit, limit)`, but is more explicit about the intent.

##### [§](#panics-1)Panics

Panics if `limit` is negative or NaN, as this indicates a logic error.

##### [§](#examples-53)Examples

```rust
#![feature(clamp_magnitude)]
assert_eq!(5.0f32.clamp_magnitude(3.0), 3.0);
assert_eq!((-5.0f32).clamp_magnitude(3.0), -3.0);
assert_eq!(2.0f32.clamp_magnitude(3.0), 2.0);
assert_eq!((-2.0f32).clamp_magnitude(3.0), -2.0);
```

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1569)

Computes the absolute value of `self`.

This function always returns the precise result.

##### [§](#examples-54)Examples

```rust
let x = 3.5_f32;
let y = -3.5_f32;

assert_eq!(x.abs(), x);
assert_eq!(y.abs(), -y);

assert!(f32::NAN.abs().is_nan());
```

1.0.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1593)

Returns a number that represents the sign of `self`.

- `1.0` if the number is positive, `+0.0` or `INFINITY`
- `-1.0` if the number is negative, `-0.0` or `NEG_INFINITY`
- NaN if the number is NaN

##### [§](#examples-55)Examples

```rust
let f = 3.5_f32;

assert_eq!(f.signum(), 1.0);
assert_eq!(f32::NEG_INFINITY.signum(), -1.0);

assert!(f32::NAN.signum().is_nan());
```

1.35.0 (const: 1.85.0) · [Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1627)

Returns a number composed of the magnitude of `self` and the sign of `sign`.

Equal to `self` if the sign of `self` and `sign` are the same, otherwise equal to `-self`. If `self` is a NaN, then a NaN with the same payload as `self` and the sign bit of `sign` is returned.

If `sign` is a NaN, then this operation will still carry over its sign into the result. Note that IEEE 754 doesn’t assign any meaning to the sign bit in case of a NaN, and as Rust doesn’t guarantee that the bit pattern of NaNs are conserved over arithmetic operations, the result of `copysign` with `sign` being a NaN might produce an unexpected or non-portable result. See the [specification of NaN bit patterns](https://doc.rust-lang.org/stable/std/primitive.f32.html#nan-bit-patterns "primitive f32") for more info.

##### [§](#examples-56)Examples

```rust
let f = 3.5_f32;

assert_eq!(f.copysign(0.42), 3.5_f32);
assert_eq!(f.copysign(-0.42), -3.5_f32);
assert_eq!((-f).copysign(0.42), 3.5_f32);
assert_eq!((-f).copysign(-0.42), -3.5_f32);

assert!(f32::NAN.copysign(1.0).is_nan());
```

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1638)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float addition that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/stable/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1649)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float subtraction that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/stable/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1660)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float multiplication that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/stable/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1671)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float division that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/stable/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

[Source](https://doc.rust-lang.org/stable/src/core/num/f32.rs.html#1682)

🔬This is a nightly-only experimental API. (`float_algebraic` [#136469](https://github.com/rust-lang/rust/issues/136469))

Float remainder that allows optimizations based on algebraic rules.

See [algebraic operators](https://doc.rust-lang.org/stable/std/primitive.f32.html#algebraic-operators "primitive f32") for more info.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-13)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-12)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-11)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#impl-Add-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#associatedtype.Output-10)

The resulting type after applying the `+` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#114)[§](#method.add)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign%3C%26f32%3E-for-f32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#800)[§](#impl-AddAssign-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#627-632)[§](#impl-Clone-for-f32)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/float.rs.html#240)[§](#impl-Debug-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#184)[§](#impl-Default-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#184)[§](#method.default)

Returns the default value of `0.0`

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/float.rs.html#240)[§](#impl-Display-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-3)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#method.div-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#impl-Div%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-2)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#method.div-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#impl-Div%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output-1)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#method.div-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#impl-Div-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#associatedtype.Output)

The resulting type after applying the `/` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#526)[§](#method.div)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign%3C%26f32%3E-for-f32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#994)[§](#impl-DivAssign-for-f32)

1.68.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#229)[§](#impl-From%3Cbool%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#229)[§](#method.from-6)

Converts a [`bool`](https://doc.rust-lang.org/stable/std/primitive.bool.html "primitive bool") to [`f32`](https://doc.rust-lang.org/stable/std/primitive.f32.html "primitive f32") losslessly. The resulting value is positive `0.0` for `false` and `1.0` for `true` values.

##### [§](#examples-57)Examples

```rust
let x: f32 = false.into();
assert_eq!(x, 0.0);
assert!(x.is_sign_positive());

let y: f32 = true.into();
assert_eq!(y, 1.0);
```

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#182)[§](#impl-From%3Cf32%3E-for-f128)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#181)[§](#impl-From%3Cf32%3E-for-f64)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#155)[§](#impl-From%3Ci16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#152)[§](#impl-From%3Ci8%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#168)[§](#impl-From%3Cu16%3E-for-f32)

1.6.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#165)[§](#impl-From%3Cu8%3E-for-f32)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/num/dec2flt/mod.rs.html#179)[§](#impl-FromStr-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/num/dec2flt/mod.rs.html#179)[§](#method.from_str)

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

All strings that adhere to the following [EBNF](https://www.w3.org/TR/REC-xml/#sec-notation) grammar when lowercased will result in an [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") being returned:

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

[Source](https://doc.rust-lang.org/stable/src/core/num/dec2flt/mod.rs.html#179)[§](#associatedtype.Err)

The associated error which can be returned from parsing.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/float.rs.html#240)[§](#impl-LowerExp-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-21)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-20)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-19)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#impl-Mul-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#associatedtype.Output-18)

The resulting type after applying the `*` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#361)[§](#method.mul)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign%3C%26f32%3E-for-f32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#933)[§](#impl-MulAssign-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-%26f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#729)[§](#impl-Neg-for-f32)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#impl-PartialEq-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1898-1900)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#impl-PartialOrd-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1991)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#impl-Product%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#method.product-1)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#impl-Product-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#method.product)

Takes an iterator and generates `Self` from the elements by multiplying the items.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-7)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#method.rem-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-6)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#method.rem-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#impl-Rem%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-5)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#method.rem-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#impl-Rem-for-f32)

The remainder from the division of two floats.

The remainder has the same sign as the dividend and is computed as: `x - (x / y).trunc() * y`.

#### [§](#examples-58)Examples

```rust
let x: f32 = 50.50;
let y: f32 = 8.125;
let remainder = x - (x / y).trunc() * y;

// The answer to both operations is 1.75
assert_eq!(x % y, remainder);
```

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#associatedtype.Output-4)

The resulting type after applying the `%` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#650)[§](#method.rem)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign%3C%26f32%3E-for-f32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#1059)[§](#impl-RemAssign-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1153)[§](#impl-SimdElement-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/vector.rs.html#1154)[§](#associatedtype.Mask)

🔬This is a nightly-only experimental API. (`portable_simd` [#86656](https://github.com/rust-lang/rust/issues/86656))

The mask element type corresponding to this element type.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26f32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-17)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-3)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-16)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-2)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub%3Cf32%3E-for-%26f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-15)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub-1)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#impl-Sub-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#associatedtype.Output-14)

The resulting type after applying the `-` operator.

[Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#227)[§](#method.sub)

1.22.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign%3C%26f32%3E-for-f32)

1.8.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/arith.rs.html#871)[§](#impl-SubAssign-for-f32)

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#impl-Sum%3C%26f32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#method.sum-1)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.12.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#impl-Sum-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#206)[§](#method.sum)

Takes an iterator and generates `Self` from the elements by “summing up” the items.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/float.rs.html#240)[§](#impl-UpperExp-for-f32)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#474-484)[§](#impl-Copy-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci128%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci16%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci64%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Ci8%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cisize%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu128%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu16%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu32%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu64%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cu8%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/convert/num.rs.html#38)[§](#impl-FloatToInt%3Cusize%3E-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/portable-simd/crates/core_simd/src/cast.rs.html#48)[§](#impl-SimdCast-for-f32)

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#339-344)[§](#impl-UseCloned-for-f32)

[§](#impl-Freeze-for-f32)

[§](#impl-RefUnwindSafe-for-f32)

[§](#impl-Send-for-f32)

[§](#impl-Sync-for-f32)

[§](#impl-Unpin-for-f32)

[§](#impl-UnsafeUnpin-for-f32)

[§](#impl-UnwindSafe-for-f32)